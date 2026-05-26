# Paper Collector — Awesome Graph Agent

> Automated paper collection workflow for the awesome-graph-agent repository.
> Searches DBLP for CCF-A papers matching the repository's research focus,
> deduplicates against existing entries, downloads PDFs from arXiv,
> and commits updates to the repository.

## Trigger

Use this skill when the user asks to:
- "收集论文" / "collect papers" / "update papers"
- "搜索最新的 graph agent 论文"
- "从 DBLP/arXiv 找论文"
- "更新 awesome-graph-agent 仓库"

## Prerequisites

- `curl` — HTTP requests to DBLP/arXiv APIs
- `python3` — data processing and PDF management
- `git` — repository operations
- `pdftotext` (optional) — PDF text extraction for verification

## Workflow

### Step 1: Pull Latest Repository

```bash
cd <repo_dir>
git checkout main
git pull origin main
git checkout -b feat/add-papers-<date>
```

### Step 2: Identify Research Focus

Read the repository's `README.md` to understand:
- What topics are tracked (e.g., Graph × Agent, GraphRAG, Multi-Agent, LLM Reasoning)
- What conferences/journals are in scope (CCF-A: ICML, AAAI, NeurIPS, IJCAI, ACL, KDD, WWW, CVPR, ICCV)
- What format the paper entries follow

### Step 3: Search DBLP

Query DBLP API for relevant papers:

```
https://dblp.org/search/publ/api?q=<keywords>&format=json&h=30
```

**Search strategies:**
1. `venue:<VENUE> graph agent` — venue-specific search
2. `graph LLM <keyword>` — topic-based search
3. Filter results by year (≥ 2024) and CCF-A venues

**CCF-A venues to target:**
- AI: AAAI, NeurIPS, ICML, IJCAI
- NLP: ACL
- Data Mining: KDD, WWW
- Vision: CVPR, ICCV

**Rate limiting:** Wait 2 seconds between DBLP API calls.

### Step 4: Deduplicate

Compare search results against existing `README.md` entries:
- Extract all paper titles from README (case-insensitive match)
- Remove any papers already listed
- Report dedup stats

### Step 5: Match arXiv IDs

For each new paper, search arXiv:

```
https://arxiv.org/search/?query=<paper_keywords>&searchtype=all
```

Extract arXiv IDs from search results page using regex:
```python
re.findall(r'arXiv:(\d{4}\.\d{4,5})', html)
```

**Tips:**
- Use the paper's short name or first distinctive keyword for better matches
- If full title search fails, try the acronym (e.g., "BayesAgent", "GraphCogent")
- Wait 2-3 seconds between arXiv searches

### Step 6: Download PDFs

For each paper with an arXiv ID:

```bash
curl -sL "https://arxiv.org/pdf/<arxiv_id>" -o "papers/pdfs/<VENUE>_<YEAR>_<CATEGORY>_<SHORT_NAME>.pdf"
```

**Naming convention:** `<VENUE>_<YEAR>_<CATEGORY>_<SHORT_NAME>.pdf`
- Example: `AAAI_2026_planning_BayesAgent.pdf`
- Example: `ACL_2025_reasoning_Graph_Counselor.pdf`

**Validation:** File must be > 50KB to be considered valid.

### Step 7: Update README.md

Add new papers to the appropriate category sections in README.md:
- Follow existing table format: `| # | Paper | Venue | Year | Keywords |`
- Update the Statistics section with new totals
- Mark papers without arXiv PDF as "⚠️ No arXiv preprint"

### Step 8: Generate Venue Files

For each new venue+year combination, create/update:
`papers/<venue>-<year>-graph-llm.md`

Format:
```markdown
# <VENUE> <YEAR> — Graph × Agent/LLM Papers

Total: N papers

## 1. <Paper Title>

- **Venue:** <VENUE> <YEAR>
- **DOI:** https://doi.org/<doi>
- **Authors:** <author list>
- **arXiv:** https://arxiv.org/abs/<id>
- **Category:** <category>
- **PDF Status:** ✅ downloaded / ❌ not available (reason)
```

### Step 9: Commit and Push

```bash
git add -A
git commit -m "feat: add N papers from <venues> (<years>) with M PDFs"
git push origin feat/add-papers-<date>
```

Then request merge to main (via collaborator or PR).

## Error Handling

- **DBLP rate limited:** Wait 60 seconds, retry with exponential backoff
- **arXiv not responding:** Try alternative sources (Semantic Scholar API, direct DOI resolution)
- **PDF download failed:** Mark in README and venue file, continue with next paper
- **Git push denied:** Report to user, suggest token refresh or permission fix

## Configuration

The skill reads research focus from the repository's README.md automatically.
No additional configuration files needed.

## Example Usage

```
User: 帮我从 AAAI 2026 和 ACL 2025 搜集 graph+agent 相关的新论文
Agent: [Executes workflow Steps 1-9]
```

## Limitations

- Only finds papers with arXiv preprints for PDF download
- DBLP/arXiv have rate limits (~30 requests/minute)
- Papers behind paywalls (IEEE/ACM/Springer) cannot be downloaded
- Some very new papers may not yet be indexed by DBLP
