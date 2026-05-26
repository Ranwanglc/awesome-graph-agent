# skill/

This directory contains the automated paper collection skill for this repository.

## Files

- **SKILL.md** — Full workflow documentation (OpenClaw skill format)
- **collect_papers.py** — Standalone Python script that automates the pipeline

## Quick Start

```bash
# Dry run (search only, no downloads)
python3 skill/collect_papers.py --repo-dir . --dry-run

# Full run — PDFs to separate private repo
python3 skill/collect_papers.py --repo-dir . --pdfs-repo /path/to/awesome-graph-agent-pdfs

# Full run — PDFs stored locally (legacy mode)
python3 skill/collect_papers.py --repo-dir . --keywords "graph agent LLM" "GraphRAG" --venues "AAAI,ACL,NeurIPS,ICML"

# Specify minimum year
python3 skill/collect_papers.py --repo-dir . --pdfs-repo /tmp/pdfs --min-year 2025
```

## Repository Structure

- **Public repo** (`awesome-graph-agent`): paper metadata, README, venue files, skill
- **Private repo** (`awesome-graph-agent-pdfs`): PDF full-text files

This separation keeps the public repo lightweight and avoids copyright issues with hosting PDFs publicly.

## Integration with OpenClaw

Copy `SKILL.md` to your OpenClaw skills directory to use it as an agent skill:

```bash
cp skill/SKILL.md ~/.openclaw/skills/paper-collector/SKILL.md
```

Then the agent can be triggered with: "帮我收集最新的 graph agent 论文"
