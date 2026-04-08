"""
find_new_papers.py

Tracks citations of seed papers via Semantic Scholar API.
For each high-citation paper in papers.yml, fetches papers that recently
cited it, then filters out entries already in the database.

Outputs a markdown report for use in a GitHub Issue.

No API keys required.
"""
import sys
import time
import yaml
import requests
from datetime import datetime, timedelta, timezone
from pathlib import Path

PAPERS_YML = Path(__file__).parent.parent / "papers.yml"
S2_BASE = "https://api.semanticscholar.org/graph/v1"
HEADERS = {"User-Agent": "awesome-ipi-defense/1.0 (citation-tracker)"}

# Only track seed papers with ArXiv IDs (Semantic Scholar lookup requires an ID)
MIN_CITATIONS = 0   # include all seed papers with arxiv IDs
LOOKBACK_DAYS = 35  # look for citing papers published in last 35 days


def load_existing(path: Path) -> tuple[set, set]:
    """Return (set of arxiv IDs, set of lowercase titles) already in DB."""
    papers = yaml.safe_load(path.read_text())
    arxiv_ids = {p["arxiv"].split("v")[0] for p in papers if p.get("arxiv")}
    titles = {p["title"].lower() for p in papers}
    return arxiv_ids, titles


def get_s2_paper_id(arxiv_id: str) -> str | None:
    """Resolve arxiv ID → Semantic Scholar internal ID."""
    r = requests.get(
        f"{S2_BASE}/paper/arXiv:{arxiv_id}",
        params={"fields": "paperId,title,citationCount"},
        headers=HEADERS,
        timeout=10,
    )
    if r.status_code == 200:
        return r.json().get("paperId")
    return None


def get_recent_citations(s2_id: str, since_date: str) -> list[dict]:
    """Fetch papers that cite the given paper, published after since_date."""
    results = []
    offset = 0
    limit = 100

    while True:
        r = requests.get(
            f"{S2_BASE}/paper/{s2_id}/citations",
            params={
                "fields": "paperId,title,year,externalIds,abstract,citationCount,venue,publicationDate",
                "limit": limit,
                "offset": offset,
            },
            headers=HEADERS,
            timeout=15,
        )
        if r.status_code == 429:
            print("  Rate limited, waiting 15s...", file=sys.stderr)
            time.sleep(15)
            continue
        if r.status_code != 200:
            break

        data = r.json()
        batch = data.get("data", [])
        if not batch:
            break

        for item in batch:
            paper = item.get("citingPaper", {})
            pub_date = paper.get("publicationDate") or ""
            if pub_date and pub_date >= since_date:
                results.append(paper)

        if len(batch) < limit:
            break
        offset += limit
        time.sleep(0.5)

    return results


def format_issue_body(candidates: list[dict], since_date: str) -> str:
    lines = [
        f"## New Candidate Papers (citing tracked seeds since {since_date})",
        "",
        f"Found **{len(candidates)}** candidate(s). Please review and add relevant ones to `papers.yml` and `README.md`.",
        "",
        "---",
        "",
    ]

    for p in sorted(candidates, key=lambda x: -(x.get("citationCount") or 0)):
        title = p.get("title", "Unknown")
        arxiv_id = (p.get("externalIds") or {}).get("ArXiv", "")
        year = p.get("year", "")
        venue = p.get("venue", "")
        cites = p.get("citationCount", 0)
        pub_date = p.get("publicationDate", "")
        abstract = (p.get("abstract") or "")[:250]
        url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else ""
        cited_by = p.get("_cited_by", "")

        lines.append(f"### {title}")
        if url:
            lines.append(f"- **ArXiv**: [{arxiv_id}]({url})")
        lines.append(f"- **Year**: {year}  |  **Published**: {pub_date}")
        if venue:
            lines.append(f"- **Venue**: {venue}")
        lines.append(f"- **Citations**: {cites}")
        lines.append(f"- **Cites our paper**: {cited_by}")
        if abstract:
            lines.append(f"- **Abstract**: {abstract}...")
        lines.append("")
        lines.append("**Suggested classification** (fill in before adding):")
        lines.append("```yaml")
        slug = title.lower()[:30].replace(" ", "-").replace(":", "").replace(",", "")
        lines.append(f"- id: {slug}-{year}")
        lines.append(f'  title: "{title}"')
        lines.append(f"  year: {year}")
        if venue:
            lines.append(f'  venue: "{venue}"')
        if arxiv_id:
            lines.append(f'  arxiv: "{arxiv_id}"')
        lines.append("  defense_type: []  # TODO: D1-D6")
        lines.append("  threat_model: []  # TODO: direct/indirect/multi-agent/rag/computer-use")
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main():
    since_date = (datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)).strftime("%Y-%m-%d")
    print(f"Looking for citing papers published since {since_date}", file=sys.stderr)

    existing_arxiv, existing_titles = load_existing(PAPERS_YML)
    papers = yaml.safe_load(PAPERS_YML.read_text())

    # Seed papers: those with arxiv IDs
    seeds = [p for p in papers if p.get("arxiv")]
    print(f"Tracking {len(seeds)} seed papers", file=sys.stderr)

    candidates = {}

    for seed in seeds:
        arxiv_id = seed["arxiv"].split("v")[0]
        seed_title = seed["title"][:50]
        print(f"  Checking citations of: {seed_title}...", file=sys.stderr)

        s2_id = get_s2_paper_id(arxiv_id)
        if not s2_id:
            print(f"    Not found in S2, skipping", file=sys.stderr)
            time.sleep(1)
            continue

        citing = get_recent_citations(s2_id, since_date)
        print(f"    Found {len(citing)} recent citing papers", file=sys.stderr)

        for p in citing:
            p_arxiv = (p.get("externalIds") or {}).get("ArXiv", "").split("v")[0]
            p_title = p.get("title", "")

            # Skip if already in database
            if p_arxiv and p_arxiv in existing_arxiv:
                continue
            if p_title.lower() in existing_titles:
                continue

            key = p_arxiv or p.get("paperId", p_title)
            if key and key not in candidates:
                p["_cited_by"] = seed_title
                candidates[key] = p

        time.sleep(1.5)

    candidates_list = list(candidates.values())
    print(f"\nTotal new candidates: {len(candidates_list)}", file=sys.stderr)

    if not candidates_list:
        print("NO_NEW_PAPERS")
        return

    print(format_issue_body(candidates_list, since_date))


if __name__ == "__main__":
    main()
