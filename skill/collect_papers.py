#!/usr/bin/env python3
"""
Paper Collector — Automated pipeline for awesome-graph-agent.

Usage:
    python3 collect_papers.py --repo-dir <path> --keywords "graph agent LLM" --venues "AAAI,ACL,NeurIPS"

Steps:
    1. Read existing README for dedup
    2. Search DBLP for new papers
    3. Match arXiv IDs
    4. Download PDFs
    5. Update README and venue files
"""

import argparse
import json
import os
import re
import subprocess
import time
import urllib.parse


def search_dblp(query, max_results=20):
    """Search DBLP API and return parsed results."""
    url = f'https://dblp.org/search/publ/api?q={urllib.parse.quote(query)}&format=json&h={max_results}'
    cmd = f'curl -s --max-time 15 "{url}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=20)
    try:
        data = json.loads(result.stdout)
        return data.get('result', {}).get('hits', {}).get('hit', [])
    except (json.JSONDecodeError, Exception):
        return []


def search_arxiv(keywords):
    """Search arXiv web and extract first matching ID."""
    query = keywords.replace(' ', '+')
    cmd = f'curl -sL --max-time 15 "https://arxiv.org/search/?query={query}&searchtype=all"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=20)
    ids = re.findall(r'arXiv:(\d{4}\.\d{4,5})', result.stdout)
    return ids[0] if ids else None


def download_pdf(arxiv_id, output_path):
    """Download PDF from arXiv. Returns True if successful."""
    cmd = f'curl -sL --max-time 30 "https://arxiv.org/pdf/{arxiv_id}" -o "{output_path}"'
    subprocess.run(cmd, shell=True, timeout=35)
    if os.path.exists(output_path) and os.path.getsize(output_path) > 50000:
        return True
    if os.path.exists(output_path):
        os.remove(output_path)
    return False


def get_existing_titles(readme_path):
    """Extract existing paper titles from README for deduplication."""
    titles = set()
    with open(readme_path) as f:
        for line in f:
            matches = re.findall(r'\*\*([^*]+)\*\*', line)
            for m in matches:
                titles.add(m.lower().strip().rstrip('.'))
    return titles


def main():
    parser = argparse.ArgumentParser(description='Paper Collector for awesome-graph-agent')
    parser.add_argument('--repo-dir', required=True, help='Path to the main repo')
    parser.add_argument('--pdfs-repo', default='', help='Path to the private PDF repo (if empty, PDFs saved to <repo-dir>/papers/pdfs/)')
    parser.add_argument('--keywords', nargs='+', default=['graph agent LLM', 'GraphRAG', 'graph multi-agent', 'knowledge graph LLM reasoning'])
    parser.add_argument('--venues', default='AAAI,ACL,NeurIPS,ICML,IJCAI,KDD,WWW')
    parser.add_argument('--min-year', type=int, default=2024)
    parser.add_argument('--dry-run', action='store_true', help='Search only, no downloads')
    args = parser.parse_args()

    repo_dir = args.repo_dir
    readme_path = os.path.join(repo_dir, 'README.md')
    
    # PDF storage: use separate repo if specified, otherwise local
    if args.pdfs_repo:
        pdfs_dir = args.pdfs_repo
    else:
        pdfs_dir = os.path.join(repo_dir, 'papers', 'pdfs')
    os.makedirs(pdfs_dir, exist_ok=True)

    ccf_a_venues = set(v.strip().upper() for v in args.venues.split(','))
    existing_titles = get_existing_titles(readme_path)
    print(f"Existing papers: {len(existing_titles)}")

    # Step 1: Search DBLP
    all_papers = []
    for venue in ccf_a_venues:
        for kw in args.keywords:
            query = f'venue:{venue} {kw}'
            print(f"Searching: {query}")
            hits = search_dblp(query)
            for h in hits:
                info = h.get('info', {})
                year = int(info.get('year', 0))
                if year < args.min_year:
                    continue
                title = info.get('title', '').rstrip('.')
                if title.lower().strip() in existing_titles:
                    continue
                authors = info.get('authors', {}).get('author', [])
                if isinstance(authors, dict):
                    authors = [authors]
                all_papers.append({
                    'title': title,
                    'year': str(year),
                    'venue': info.get('venue', venue),
                    'doi': info.get('doi', ''),
                    'authors': ', '.join([a.get('text', '') for a in authors[:5]]),
                })
            time.sleep(2)

    # Dedup within results
    seen = set()
    unique_papers = []
    for p in all_papers:
        key = p['title'].lower().strip()
        if key not in seen:
            seen.add(key)
            unique_papers.append(p)

    print(f"\nNew papers found: {len(unique_papers)}")

    if args.dry_run:
        for p in unique_papers:
            print(f"  [{p['year']}] {p['title']} — {p['venue']}")
        return

    # Step 2: Match arXiv IDs and download
    for p in unique_papers:
        short_name = p['title'].split(':')[0].strip() if ':' in p['title'] else p['title'].split()[0]
        arxiv_id = search_arxiv(short_name)
        p['arxiv'] = arxiv_id or ''
        if arxiv_id:
            safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', f"{p['venue']}_{p['year']}_{short_name[:30]}")
            pdf_path = os.path.join(pdfs_dir, f"{safe_name}.pdf")
            if download_pdf(arxiv_id, pdf_path):
                p['pdf_status'] = 'downloaded'
                p['pdf_path'] = pdf_path
                print(f"  ✅ {p['title'][:50]}... → {arxiv_id}")
            else:
                p['pdf_status'] = 'download_failed'
                print(f"  ⚠️ {p['title'][:50]}... → {arxiv_id} (download failed)")
        else:
            p['pdf_status'] = 'no_arxiv'
            print(f"  ❌ {p['title'][:50]}... → no arXiv match")
        time.sleep(3)

    # Save results for manual review
    output_file = os.path.join(repo_dir, 'papers', 'latest_collection.json')
    with open(output_file, 'w') as f:
        json.dump(unique_papers, f, ensure_ascii=False, indent=2)
    print(f"\nResults saved to: {output_file}")
    print(f"Downloaded: {sum(1 for p in unique_papers if p.get('pdf_status') == 'downloaded')}/{len(unique_papers)}")


if __name__ == '__main__':
    main()
