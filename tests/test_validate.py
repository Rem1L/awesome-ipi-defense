import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from validate import validate_papers, ValidationError

VALID_PAPER = {
    "id": "struq-2024",
    "title": "StruQ: Defending Against Prompt Injection with Structured Queries",
    "year": 2024,
    "defense_type": ["D1-input-filtering"],
    "threat_model": ["direct", "indirect"],
}

def test_valid_paper_passes():
    errors = validate_papers([VALID_PAPER])
    assert errors == []

def test_missing_required_field_id():
    paper = {**VALID_PAPER}
    del paper["id"]
    errors = validate_papers([paper])
    assert any("id" in e for e in errors)

def test_missing_required_field_title():
    paper = {**VALID_PAPER}
    del paper["title"]
    errors = validate_papers([paper])
    assert any("title" in e for e in errors)

def test_missing_required_field_year():
    paper = {**VALID_PAPER}
    del paper["year"]
    errors = validate_papers([paper])
    assert any("year" in e for e in errors)

def test_missing_required_field_defense_type():
    paper = {**VALID_PAPER}
    del paper["defense_type"]
    errors = validate_papers([paper])
    assert any("defense_type" in e for e in errors)

def test_missing_required_field_threat_model():
    paper = {**VALID_PAPER}
    del paper["threat_model"]
    errors = validate_papers([paper])
    assert any("threat_model" in e for e in errors)

def test_invalid_defense_type_value():
    paper = {**VALID_PAPER, "defense_type": ["D7-unknown"]}
    errors = validate_papers([paper])
    assert any("defense_type" in e for e in errors)

def test_invalid_threat_model_value():
    paper = {**VALID_PAPER, "threat_model": ["phishing"]}
    errors = validate_papers([paper])
    assert any("threat_model" in e for e in errors)

def test_year_out_of_range():
    paper = {**VALID_PAPER, "year": 2019}
    errors = validate_papers([paper])
    assert any("year" in e for e in errors)

def test_year_must_be_integer():
    paper = {**VALID_PAPER, "year": "2024"}
    errors = validate_papers([paper])
    assert any("year" in e for e in errors)

def test_duplicate_id():
    papers = [VALID_PAPER, {**VALID_PAPER, "title": "Another Paper"}]
    errors = validate_papers(papers)
    assert any("duplicate" in e.lower() or "id" in e for e in errors)

def test_invalid_arxiv_format():
    paper = {**VALID_PAPER, "arxiv": "not-an-arxiv-id"}
    errors = validate_papers([paper])
    assert any("arxiv" in e for e in errors)

def test_valid_arxiv_format():
    paper = {**VALID_PAPER, "arxiv": "2402.06363"}
    errors = validate_papers([paper])
    assert errors == []

def test_valid_arxiv_with_version():
    paper = {**VALID_PAPER, "arxiv": "2402.06363v2"}
    errors = validate_papers([paper])
    assert errors == []

def test_invalid_deploy_location():
    paper = {**VALID_PAPER, "deploy_location": ["database-layer"]}
    errors = validate_papers([paper])
    assert any("deploy_location" in e for e in errors)

def test_defense_type_d1_no_suffix():
    paper = {**VALID_PAPER, "defense_type": ["D1"]}
    errors = validate_papers([paper])
    assert errors == []

def test_multiple_defense_types():
    paper = {**VALID_PAPER, "defense_type": ["D5-architecture", "D5-information-flow-control"]}
    errors = validate_papers([paper])
    assert errors == []
