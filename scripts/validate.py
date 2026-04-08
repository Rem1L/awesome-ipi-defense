"""Validates papers.yml against the awesome-ipi-defense schema."""
import re
import sys
import yaml
from pathlib import Path

VALID_THREAT_MODELS = {"direct", "indirect", "multi-agent", "rag", "computer-use"}
VALID_DEPLOY_LOCATIONS = {"input-layer", "inference-layer", "output-layer", "system-arch"}
DEFENSE_TYPE_RE = re.compile(r"^D[1-6](-[a-z0-9-]+)?$")
ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")
REQUIRED_FIELDS = ["id", "title", "year", "defense_type", "threat_model"]


class ValidationError(Exception):
    pass


def validate_papers(papers: list) -> list:
    """Validate a list of paper dicts. Returns list of error messages."""
    errors = []
    seen_ids = {}

    for i, paper in enumerate(papers):
        loc = f"Paper #{i+1} (id={paper.get('id', '<missing>')})"

        for field in REQUIRED_FIELDS:
            if field not in paper:
                errors.append(f"{loc}: missing required field '{field}'")

        if "year" in paper:
            if not isinstance(paper["year"], int):
                errors.append(f"{loc}: 'year' must be an integer, got {type(paper['year']).__name__}")
            elif not (2020 <= paper["year"] <= 2030):
                errors.append(f"{loc}: 'year' {paper['year']} out of range 2020-2030")

        if "defense_type" in paper:
            if not isinstance(paper["defense_type"], list) or len(paper["defense_type"]) == 0:
                errors.append(f"{loc}: 'defense_type' must be a non-empty list")
            else:
                for dt in paper["defense_type"]:
                    if not DEFENSE_TYPE_RE.match(str(dt)):
                        errors.append(f"{loc}: invalid defense_type '{dt}' (must match D1-D6 pattern, e.g. 'D1' or 'D1-input-filtering')")

        if "threat_model" in paper:
            if not isinstance(paper["threat_model"], list) or len(paper["threat_model"]) == 0:
                errors.append(f"{loc}: 'threat_model' must be a non-empty list")
            else:
                for tm in paper["threat_model"]:
                    if tm not in VALID_THREAT_MODELS:
                        errors.append(f"{loc}: invalid threat_model '{tm}' (allowed: {sorted(VALID_THREAT_MODELS)})")

        if "deploy_location" in paper:
            if not isinstance(paper["deploy_location"], list):
                errors.append(f"{loc}: 'deploy_location' must be a list")
            else:
                for dl in paper["deploy_location"]:
                    if dl not in VALID_DEPLOY_LOCATIONS:
                        errors.append(f"{loc}: invalid deploy_location '{dl}' (allowed: {sorted(VALID_DEPLOY_LOCATIONS)})")

        if "arxiv" in paper and paper["arxiv"] is not None:
            if not ARXIV_RE.match(str(paper["arxiv"])):
                errors.append(f"{loc}: invalid arxiv id '{paper['arxiv']}' (expected format: YYMM.NNNNN)")

        if "id" in paper:
            pid = paper["id"]
            if pid in seen_ids:
                errors.append(f"{loc}: duplicate id '{pid}' (first seen at Paper #{seen_ids[pid]+1})")
            else:
                seen_ids[pid] = i

    return errors


def main():
    papers_path = Path(__file__).parent.parent / "papers.yml"
    if not papers_path.exists():
        print(f"ERROR: {papers_path} not found", file=sys.stderr)
        sys.exit(1)

    with open(papers_path, encoding="utf-8") as f:
        papers = yaml.safe_load(f)

    if not isinstance(papers, list):
        print("ERROR: papers.yml must be a YAML list", file=sys.stderr)
        sys.exit(1)

    errors = validate_papers(papers)

    if errors:
        print(f"Validation FAILED - {len(errors)} error(s):\n")
        for e in errors:
            print(f"  x {e}")
        sys.exit(1)
    else:
        print(f"Validation passed - {len(papers)} papers OK")


if __name__ == "__main__":
    main()
