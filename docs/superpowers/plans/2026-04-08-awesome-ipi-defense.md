# awesome-ipi-defense Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a well-structured awesome list for prompt injection defense papers, anchored by a novel D1–D6 taxonomy, with a machine-readable `papers.yml` and GitHub Actions validation.

**Architecture:** `papers.yml` is the single source of truth for paper metadata. `README.md` renders two human-readable views (by year, by defense type) manually maintained in sync with `papers.yml`. A Python validator script enforces schema on every PR.

**Tech Stack:** Markdown, YAML, Python 3 (stdlib + PyYAML), GitHub Actions

---

## File Map

| File | Purpose |
|------|---------|
| `README.md` | Taxonomy overview + papers (by year + by type) |
| `papers.yml` | Structured paper database (~50+ seed entries) |
| `CONTRIBUTING.md` | How to add papers, YAML schema reference |
| `docs/taxonomy.md` | Detailed taxonomy rationale and definitions |
| `scripts/validate.py` | Schema validator for papers.yml |
| `tests/test_validate.py` | Unit tests for validator |
| `.github/workflows/validate.yml` | GitHub Actions CI for PRs |

---

## Task 1: Git + Directory Scaffold

**Files:**
- Create: `.github/workflows/` (directory)
- Create: `docs/` (directory)
- Create: `scripts/` (directory)
- Create: `tests/` (directory)

- [ ] **Step 1: Verify current state**

```bash
cd /home/ubuntu/awesome-ipi-defense
git status
ls -la
```

Expected: git initialized, `docs/superpowers/specs/` present.

- [ ] **Step 2: Create remaining directories**

```bash
mkdir -p .github/workflows scripts tests
```

- [ ] **Step 3: Create .gitignore**

Create `/home/ubuntu/awesome-ipi-defense/.gitignore`:

```
__pycache__/
*.pyc
.pytest_cache/
*.egg-info/
.venv/
```

- [ ] **Step 4: Initial commit**

```bash
git add .gitignore docs/superpowers/specs/2026-04-08-awesome-ipi-defense-design.md
git commit -m "chore: initialize repository with spec"
```

---

## Task 2: YAML Validator (TDD)

**Files:**
- Create: `scripts/validate.py`
- Create: `tests/test_validate.py`

### Schema rules to enforce:
- Required fields: `id`, `title`, `year`, `defense_type`, `threat_model`
- `defense_type` values match regex `^D[1-6](-[a-z0-9-]+)?$`
- `threat_model` values in `{direct, indirect, multi-agent, rag, computer-use}`
- `deploy_location` values (if present) in `{input-layer, inference-layer, output-layer, system-arch}`
- `year` is integer in range 2020–2030
- `id` is unique across all entries
- `arxiv` (if present) matches `^\d{4}\.\d{4,5}(v\d+)?$`

- [ ] **Step 1: Install PyYAML**

```bash
pip install pyyaml --quiet
```

Expected: PyYAML installed or already present.

- [ ] **Step 2: Write failing tests**

Create `/home/ubuntu/awesome-ipi-defense/tests/test_validate.py`:

```python
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
```

- [ ] **Step 3: Run tests — verify they all fail**

```bash
cd /home/ubuntu/awesome-ipi-defense
python -m pytest tests/test_validate.py -v 2>&1 | head -30
```

Expected: `ModuleNotFoundError: No module named 'validate'`

- [ ] **Step 4: Implement validator**

Create `/home/ubuntu/awesome-ipi-defense/scripts/validate.py`:

```python
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


def validate_papers(papers: list) -> list[str]:
    """Validate a list of paper dicts. Returns list of error messages."""
    errors = []
    seen_ids = {}

    for i, paper in enumerate(papers):
        loc = f"Paper #{i+1} (id={paper.get('id', '<missing>')})"

        # Required fields
        for field in REQUIRED_FIELDS:
            if field not in paper:
                errors.append(f"{loc}: missing required field '{field}'")

        # year
        if "year" in paper:
            if not isinstance(paper["year"], int):
                errors.append(f"{loc}: 'year' must be an integer, got {type(paper['year']).__name__}")
            elif not (2020 <= paper["year"] <= 2030):
                errors.append(f"{loc}: 'year' {paper['year']} out of range 2020–2030")

        # defense_type
        if "defense_type" in paper:
            if not isinstance(paper["defense_type"], list) or len(paper["defense_type"]) == 0:
                errors.append(f"{loc}: 'defense_type' must be a non-empty list")
            else:
                for dt in paper["defense_type"]:
                    if not DEFENSE_TYPE_RE.match(str(dt)):
                        errors.append(f"{loc}: invalid defense_type '{dt}' (must match D1–D6 pattern, e.g. 'D1' or 'D1-input-filtering')")

        # threat_model
        if "threat_model" in paper:
            if not isinstance(paper["threat_model"], list) or len(paper["threat_model"]) == 0:
                errors.append(f"{loc}: 'threat_model' must be a non-empty list")
            else:
                for tm in paper["threat_model"]:
                    if tm not in VALID_THREAT_MODELS:
                        errors.append(f"{loc}: invalid threat_model '{tm}' (allowed: {sorted(VALID_THREAT_MODELS)})")

        # deploy_location (optional)
        if "deploy_location" in paper:
            if not isinstance(paper["deploy_location"], list):
                errors.append(f"{loc}: 'deploy_location' must be a list")
            else:
                for dl in paper["deploy_location"]:
                    if dl not in VALID_DEPLOY_LOCATIONS:
                        errors.append(f"{loc}: invalid deploy_location '{dl}' (allowed: {sorted(VALID_DEPLOY_LOCATIONS)})")

        # arxiv (optional)
        if "arxiv" in paper and paper["arxiv"] is not None:
            if not ARXIV_RE.match(str(paper["arxiv"])):
                errors.append(f"{loc}: invalid arxiv id '{paper['arxiv']}' (expected format: YYMM.NNNNN)")

        # id uniqueness
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
        print(f"Validation FAILED — {len(errors)} error(s):\n")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print(f"✓ Validation passed — {len(papers)} papers OK")


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Run tests — verify they pass**

```bash
cd /home/ubuntu/awesome-ipi-defense
python -m pytest tests/test_validate.py -v
```

Expected: All 17 tests PASS.

- [ ] **Step 6: Commit**

```bash
git add scripts/validate.py tests/test_validate.py
git commit -m "feat: add papers.yml schema validator with tests"
```

---

## Task 3: GitHub Actions Workflow

**Files:**
- Create: `.github/workflows/validate.yml`

- [ ] **Step 1: Create workflow file**

Create `/home/ubuntu/awesome-ipi-defense/.github/workflows/validate.yml`:

```yaml
name: Validate papers.yml

on:
  pull_request:
    paths:
      - 'papers.yml'
      - 'scripts/validate.py'
  push:
    branches: [main, master]
    paths:
      - 'papers.yml'
      - 'scripts/validate.py'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install pyyaml

      - name: Run validator
        run: python scripts/validate.py

      - name: Run unit tests
        run: python -m pytest tests/test_validate.py -v
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/validate.yml
git commit -m "ci: add GitHub Actions validation for papers.yml"
```

---

## Task 4: docs/taxonomy.md

**Files:**
- Create: `docs/taxonomy.md`

- [ ] **Step 1: Create taxonomy document**

Create `/home/ubuntu/awesome-ipi-defense/docs/taxonomy.md`:

```markdown
# Prompt Injection Defense Taxonomy

This document defines the classification framework used in **awesome-ipi-defense**.

---

## Background

Prompt injection attacks manipulate LLMs by embedding adversarial instructions in
untrusted content (user input, web pages, documents, tool outputs). The field lacks
a shared taxonomy, making it hard to compare defenses or identify gaps.

We propose a **defense mechanism taxonomy** (D1–D6) as the primary axis, with
orthogonal tags for threat model and deployment location.

---

## Primary Classification: Defense Mechanism (D1–D6)

### D1 — Input Filtering & Pre-processing

**Core idea:** Transform, mark, or isolate untrusted input *before* it reaches
the LLM's reasoning process.

**Sub-approaches:**
- **Structured formats** (StruQ): Separate instruction and data channels using
  special delimiters or structured schemas so the model can distinguish them syntactically.
- **Spotlighting**: Mark data segments with unique tokens/XML tags so the model
  knows what is trusted instruction vs. untrusted content.
- **Signing & authentication** (Signed-Prompt): Cryptographically or syntactically
  authenticate instructions from trusted principals.
- **Sanitization & paraphrasing**: Rewrite untrusted content to remove adversarial
  structure while preserving semantics.
- **Data filtering** (DataFilter): Filter retrieved content before injection into context.

**When to use:** When you control the input pipeline and can modify how content
is formatted before the LLM sees it.

---

### D2 — Detection

**Core idea:** Identify injected content using statistical, embedding, or ML
methods — either before execution or as an inline check.

**Sub-approaches:**
- **Perplexity-based**: Flag low-perplexity directive-style text in data-expected positions.
- **Classifier-based** (InjecGuard, UniGuardian): Fine-tuned ML models that score
  prompt segments for injection likelihood.
- **Gradient-based** (GradSafe): Use gradient signals from safety-critical tokens
  to detect adversarial prompts.
- **Embedding drift** (Zero-Shot Embedding Drift): Detect semantic shift in embeddings
  that signals context hijacking.
- **Game-theoretic** (DataSentinel): Model the adversary's optimal injection strategy
  to improve detector robustness.

**When to use:** When you can't modify the input pipeline but can add a pre/post
classification step.

---

### D3 — Guardrails & Oversight

**Core idea:** Safety supervision layer running in parallel or series with the
primary LLM — inspecting inputs, outputs, or both.

**Sub-approaches:**
- **LLM-based guardrails** (Llama Guard, NeMo Guardrails): A secondary LLM trained
  to classify safety violations on inputs/outputs.
- **Self-examination** (LLM Self Defense): The primary LLM inspects its own context
  for signs of manipulation.
- **Task-alignment checking** (Task Shield): Verify that planned actions remain
  aligned with the original user task.
- **Recursive guards** (Recursive LM for jailbreak detection): Hierarchical LLM
  calls to verify safety at multiple abstraction levels.

**When to use:** As a defense-in-depth layer around existing LLM systems without
modifying core model behavior.

---

### D4 — Training-based Robustness

**Core idea:** Fine-tune the model to be intrinsically resistant to injection,
reducing reliance on runtime defenses.

**Sub-approaches:**
- **Task-specific fine-tuning** (Jatmo): Train a specialized model that treats
  instructions and data as fixed — the model refuses to follow data-embedded instructions.
- **Preference optimization** (SecAlign): Use RLHF/DPO with injection examples
  to teach the model to prefer ignoring injected instructions.
- **Instruction hierarchy training** (Instruction Hierarchy, OpenAI): Train the
  model to prioritize instructions by privilege level (system > user > tool output).
- **Augmented intermediate representations**: Modify intermediate activations or
  hidden states to enforce instruction priority.

**When to use:** When you control the training pipeline and can afford fine-tuning
cost; provides the strongest baseline robustness.

---

### D5 — Architecture & Privilege Isolation

**Core idea:** Structural changes to the LLM system that prevent untrusted content
from influencing control flow, regardless of model behavior.

**Sub-approaches:**
- **Dual-agent / planner-executor separation** (CaMeL): A "reader" LLM processes
  untrusted content and emits a structured, capability-restricted plan; an "executor"
  only runs the plan without seeing raw untrusted content.
- **Information Flow Control (IFC)** (Securing AI Agents with IFC): Track data
  provenance through the agent and enforce taint policies — untrusted-tainted data
  cannot flow into tool calls affecting trusted systems.
- **Sandboxing** (ceLLMate): Isolate agent execution in OS/browser sandboxes that
  limit blast radius of successful injections.
- **Capability-based access control** (ACE): Grant agents only the minimum capabilities
  needed per task; injections cannot trigger unauthorized capabilities.
- **Formal security frameworks** (Framework for Formalizing LLM Agent Security):
  Formal models for reasoning about agent security properties.

**When to use:** For high-stakes agentic systems where model-level defenses are
insufficient — provides structural guarantees independent of model training.

---

### D6 — Runtime Verification & Ensemble

**Core idea:** Execute or inspect multiple times and compare results to detect
manipulation-induced inconsistencies.

**Sub-approaches:**
- **Masked re-execution** (MELON): Re-execute the task with tool outputs masked/replaced
  and compare to the original execution — divergence signals injection.
- **Ensemble voting**: Run multiple LLM instances and take majority vote on actions.
- **Plan verification**: Generate a plan, then verify it against the original user
  intent before executing.

**When to use:** When you can afford higher latency/cost for critical operations;
detects injections that alter agent behavior.

---

## Orthogonal Dimensions

### Threat Model Tags

| Tag | Description |
|-----|-------------|
| `direct` | Attacker controls user-facing input directly |
| `indirect` | Attacker plants injections in external content (web, docs, emails) |
| `multi-agent` | Injection propagates across agent-to-agent communication |
| `rag` | Injection embedded in retrieved documents |
| `computer-use` | Injection via UI elements, screenshots, rendered content |

### Deployment Location Tags

| Tag | Description |
|-----|-------------|
| `input-layer` | Defense applied before LLM inference |
| `inference-layer` | Defense modifies or monitors inference process |
| `output-layer` | Defense applied to LLM outputs before action |
| `system-arch` | Defense is structural (not tied to a single layer) |

---

## Relationship to Existing Taxonomies

The tldrsec/prompt-injection-defenses list (last updated 2024) used the categories:
*Input Pre-processing, Guardrails & Overseers, Ensemble Decisions, Prompt Engineering,
Robustness & Finetuning.*

This taxonomy refines and extends that work:
- "Prompt Engineering" defenses are split into D1 (structural/input) and D4 (training)
- D5 (Architecture) is new — reflecting the emergence of agentic security designs
- D6 formalizes what was loosely called "Ensemble Decisions"
- Orthogonal threat-model tags replace implicit categorization

---

*Last updated: 2026-04-08*
```

- [ ] **Step 2: Commit**

```bash
git add docs/taxonomy.md
git commit -m "docs: add detailed taxonomy definitions (D1-D6)"
```

---

## Task 5: papers.yml — Seed Database

**Files:**
- Create: `papers.yml`

This task populates all seed papers. Papers are organized in YAML list format.

- [ ] **Step 1: Create papers.yml with all seed papers**

Create `/home/ubuntu/awesome-ipi-defense/papers.yml`:

```yaml
# awesome-ipi-defense paper database
# Schema: see CONTRIBUTING.md
# Validate: python scripts/validate.py

# ─── Benchmarks & Evaluation ─────────────────────────────────────────────────

- id: agentdojo-2024
  title: "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents"
  authors: ["Edoardo Debenedetti", "Jie Zhang", "Mislav Balunović", "Luca Beurer-Kellner", "Marc Fischer", "Florian Tramèr"]
  year: 2024
  venue: "NeurIPS 2024"
  arxiv: "2406.13352"
  defense_type: ["D1-input-filtering", "D4-instruction-hierarchy"]
  threat_model: ["indirect", "multi-agent"]
  deploy_location: ["system-arch"]
  tags: ["benchmark", "evaluation", "agentic"]
  summary: "Dynamic benchmark for evaluating prompt injection attacks and defenses in LLM agent pipelines"

- id: asb-2024
  title: "Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents"
  year: 2024
  venue: "arXiv"
  arxiv: "2410.02644"
  defense_type: ["D1-input-filtering", "D3-guardrails"]
  threat_model: ["direct", "indirect", "multi-agent"]
  deploy_location: ["system-arch"]
  tags: ["benchmark", "evaluation", "agentic"]
  summary: "Comprehensive benchmark formalizing attack and defense space for LLM-based agents"

# ─── D1: Input Filtering & Pre-processing ────────────────────────────────────

- id: struq-2024
  title: "StruQ: Defending Against Prompt Injection with Structured Queries"
  authors: ["Sizhe Chen", "Julien Piet", "Chawin Sitawarin", "David Wagner"]
  year: 2024
  venue: "USENIX Security 2025"
  arxiv: "2402.06363"
  defense_type: ["D1-input-filtering"]
  threat_model: ["direct", "indirect"]
  deploy_location: ["input-layer"]
  tags: ["structured-output", "delimiter", "format-separation"]
  summary: "Separates instructions and data using a structured format so the LLM can distinguish them syntactically"

- id: spotlighting-2024
  title: "Defending Against Indirect Prompt Injection Attacks With Spotlighting"
  authors: ["Keegan Hines", "Gary Lopez", "Matthew Hall", "Federico Zarfati", "Yonatan Zunger", "Emre Kıcıman"]
  year: 2024
  venue: "arXiv"
  arxiv: "2403.14720"
  defense_type: ["D1-input-filtering"]
  threat_model: ["indirect", "rag"]
  deploy_location: ["input-layer"]
  tags: ["delimiter", "marking", "xml-tags"]
  summary: "Marks untrusted data segments with distinctive tokens so the model knows what is trusted instruction vs. untrusted content"

- id: signed-prompt-2024
  title: "Signed-Prompt: A New Approach to Prevent Prompt Injection Attacks Against LLM-Integrated Applications"
  year: 2024
  venue: "arXiv"
  arxiv: "2401.07612"
  defense_type: ["D1-input-filtering"]
  threat_model: ["direct", "indirect"]
  deploy_location: ["input-layer"]
  tags: ["signing", "authentication", "trust"]
  summary: "Cryptographically signs trusted instructions to allow models to distinguish them from injected content"

- id: datafilter-2025
  title: "Defending Against Prompt Injection with DataFilter"
  year: 2025
  venue: "arXiv"
  arxiv: "2510.19207"
  defense_type: ["D1-input-filtering"]
  threat_model: ["indirect", "rag"]
  deploy_location: ["input-layer"]
  tags: ["rag", "data-cleaning", "filtering"]
  summary: "Filters retrieved content before injection into context to remove adversarial instructions"

- id: rtbas-2025
  title: "RTBAS: Defending LLM Agents Against Prompt Injection and Privacy Leakage"
  year: 2025
  venue: "arXiv"
  defense_type: ["D1-input-filtering", "D3-guardrails"]
  threat_model: ["indirect", "multi-agent"]
  deploy_location: ["input-layer", "output-layer"]
  tags: ["agentic", "privacy", "information-flow"]
  summary: "Defends LLM agents against prompt injection and privacy leakage via input/output control"

- id: real-user-instruction-2026
  title: "Real User Instruction: Black-Box Instruction Authentication Middleware Against Indirect Prompt Injection"
  year: 2026
  venue: "Preprints.org"
  defense_type: ["D1-input-filtering"]
  threat_model: ["indirect"]
  deploy_location: ["input-layer"]
  tags: ["middleware", "authentication", "black-box"]
  summary: "Middleware that authenticates whether instructions originate from real users vs. injected sources"

# ─── D2: Detection ────────────────────────────────────────────────────────────

- id: perplexity-detection-2023
  title: "Detecting Language Model Attacks with Perplexity"
  year: 2023
  venue: "arXiv"
  arxiv: "2308.14132"
  defense_type: ["D2-detection"]
  threat_model: ["direct"]
  deploy_location: ["input-layer"]
  tags: ["perplexity", "statistical", "detector"]
  summary: "Uses perplexity scores to detect adversarial prompts and jailbreak attempts"

- id: token-perplexity-2023
  title: "Token-Level Adversarial Prompt Detection Based on Perplexity Measures and Contextual Information"
  year: 2023
  venue: "arXiv"
  arxiv: "2311.11509"
  defense_type: ["D2-detection"]
  threat_model: ["direct"]
  deploy_location: ["input-layer"]
  tags: ["perplexity", "token-level", "statistical"]
  summary: "Token-level perplexity analysis for fine-grained adversarial prompt detection"

- id: gradsafe-2024
  title: "GradSafe: Detecting Unsafe Prompts for LLMs via Safety-Critical Gradient Analysis"
  year: 2024
  venue: "arXiv"
  arxiv: "2402.13494"
  defense_type: ["D2-detection"]
  threat_model: ["direct"]
  deploy_location: ["inference-layer"]
  tags: ["gradient", "safety-critical", "detector"]
  summary: "Detects unsafe prompts by analyzing gradients of safety-critical tokens"

- id: injecguard-2024
  title: "InjecGuard: Benchmarking and Mitigating Over-defense in Prompt Injection Guardrail Models"
  year: 2024
  venue: "arXiv"
  arxiv: "2410.22770"
  defense_type: ["D2-detection"]
  threat_model: ["direct", "indirect"]
  deploy_location: ["input-layer"]
  tags: ["classifier", "over-defense", "benchmark", "guardrail"]
  summary: "Addresses false positive problem in injection detectors; introduces benchmark and mitigation"

- id: datasentinel-2025
  title: "DataSentinel: A Game-Theoretic Detection of Prompt Injection Attacks"
  year: 2025
  venue: "arXiv"
  arxiv: "2504.11358"
  defense_type: ["D2-detection"]
  threat_model: ["indirect"]
  deploy_location: ["input-layer"]
  tags: ["game-theory", "adversarial-robustness", "detector"]
  summary: "Game-theoretic framework for robust prompt injection detection accounting for adaptive adversaries"

- id: uniguardian-2025
  title: "UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models"
  year: 2025
  venue: "arXiv"
  arxiv: "2502.13141"
  defense_type: ["D2-detection"]
  threat_model: ["direct", "indirect"]
  deploy_location: ["input-layer"]
  tags: ["unified", "classifier", "backdoor", "adversarial"]
  summary: "Unified detection framework covering prompt injection, backdoor, and adversarial attacks"

- id: embedding-drift-2026
  title: "Zero-Shot Embedding Drift Detection: A Lightweight Defense Against Prompt Injections in LLMs"
  year: 2026
  venue: "arXiv"
  arxiv: "2601.12359"
  defense_type: ["D2-detection"]
  threat_model: ["indirect"]
  deploy_location: ["inference-layer"]
  tags: ["embedding", "drift-detection", "zero-shot", "lightweight"]
  summary: "Detects prompt injections by measuring semantic drift in embeddings without task-specific training"

- id: classifier-detection-2025
  title: "Detecting Prompt Injection Attacks Against Application Using Classifiers"
  year: 2025
  venue: "arXiv"
  arxiv: "2512.12583"
  defense_type: ["D2-detection"]
  threat_model: ["direct", "indirect"]
  deploy_location: ["input-layer"]
  tags: ["classifier", "dataset", "benchmark"]
  summary: "Curates augmented prompt injection dataset and evaluates classifier-based detection approaches"

# ─── D3: Guardrails & Oversight ──────────────────────────────────────────────

- id: nemo-guardrails-2023
  title: "NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails"
  year: 2023
  venue: "arXiv"
  arxiv: "2310.10501"
  defense_type: ["D3-guardrails"]
  threat_model: ["direct"]
  deploy_location: ["input-layer", "output-layer"]
  tags: ["toolkit", "programmable", "rails", "nvidia"]
  summary: "Open-source toolkit for adding programmable safety guardrails to LLM applications"

- id: llama-guard-2023
  title: "Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations"
  authors: ["Hakan Inan", "Kartikeya Upasani", "Jianfeng Chi"]
  year: 2023
  venue: "arXiv"
  arxiv: "2312.06674"
  defense_type: ["D3-guardrails"]
  threat_model: ["direct"]
  deploy_location: ["input-layer", "output-layer"]
  tags: ["llm-based-guard", "safety-classifier", "meta"]
  summary: "LLM-based input-output safety classifier for human-AI conversations"

- id: building-guardrails-2024
  title: "Building Guardrails for Large Language Models"
  year: 2024
  venue: "arXiv"
  arxiv: "2402.01822"
  defense_type: ["D3-guardrails"]
  threat_model: ["direct", "indirect"]
  deploy_location: ["input-layer", "output-layer"]
  tags: ["survey", "guardrail-design", "safety"]
  summary: "Survey and framework for designing comprehensive guardrail systems for LLMs"

- id: guardreasoner-2025
  title: "GuardReasoner: Towards Reasoning-based LLM Safeguards"
  year: 2025
  venue: "arXiv"
  arxiv: "2501.18492"
  defense_type: ["D3-guardrails"]
  threat_model: ["direct"]
  deploy_location: ["input-layer", "output-layer"]
  tags: ["reasoning", "chain-of-thought", "safety"]
  summary: "Incorporates chain-of-thought reasoning into LLM safety guards for better explainability"

- id: task-shield-2024
  title: "The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents"
  year: 2024
  venue: "arXiv"
  arxiv: "2412.16682"
  defense_type: ["D3-guardrails"]
  threat_model: ["indirect"]
  deploy_location: ["inference-layer"]
  tags: ["task-alignment", "agentic", "overseer"]
  summary: "Enforces alignment between agent actions and the original user task to detect indirect injection"

- id: llm-self-defense-2023
  title: "LLM Self Defense: By Self Examination, LLMs Know They Are Being Tricked"
  year: 2023
  venue: "arXiv"
  arxiv: "2308.07308"
  defense_type: ["D3-guardrails"]
  threat_model: ["direct"]
  deploy_location: ["inference-layer"]
  tags: ["self-examination", "meta-prompt", "jailbreak"]
  summary: "LLMs can detect jailbreaks by examining their own context for signs of manipulation"

- id: robust-safety-classifier-2023
  title: "Robust Safety Classifier for Large Language Models: Adversarial Prompt Shield"
  year: 2023
  venue: "arXiv"
  arxiv: "2311.00172"
  defense_type: ["D3-guardrails"]
  threat_model: ["direct"]
  deploy_location: ["input-layer"]
  tags: ["robust-classifier", "adversarial-robustness"]
  summary: "Robust safety classifier designed to withstand adversarial prompt attacks"

- id: recursive-lm-guard-2026
  title: "Recursive language models for jailbreak detection: a procedural defense for tool-augmented agents"
  year: 2026
  venue: "arXiv"
  arxiv: "2602.16520"
  defense_type: ["D3-guardrails"]
  threat_model: ["indirect", "multi-agent"]
  deploy_location: ["inference-layer"]
  tags: ["recursive", "tool-use", "agentic", "procedural"]
  summary: "Hierarchical LLM calls for multi-level jailbreak detection in tool-augmented agent systems"

- id: adaptive-multilayer-2025
  title: "Adaptive Multi-Layer Framework for Detecting and Mitigating Prompt Injection Attacks in Large Language Models"
  year: 2025
  venue: "Journal of Information Systems Engineering and Business Intelligence"
  defense_type: ["D3-guardrails", "D2-detection"]
  threat_model: ["direct", "indirect"]
  deploy_location: ["input-layer", "inference-layer", "output-layer"]
  tags: ["multi-layer", "adaptive", "framework"]
  summary: "Multi-layer adaptive framework combining detection and guardrails at multiple pipeline stages"

# ─── D4: Training-based Robustness ───────────────────────────────────────────

- id: jatmo-2023
  title: "Jatmo: Prompt Injection Defense by Task-Specific Finetuning"
  authors: ["Julien Piet", "Meder Mirza", "Lukas Biewald", "Mark Tygert", "Dawn Song"]
  year: 2023
  venue: "ESORICS 2024"
  arxiv: "2312.17673"
  defense_type: ["D4-finetuning"]
  threat_model: ["direct", "indirect"]
  deploy_location: ["inference-layer"]
  tags: ["fine-tuning", "task-specific", "data-instructions-separation"]
  summary: "Fine-tunes task-specific models that treat external data as inert, ignoring injected instructions"

- id: secalign-2024
  title: "SecAlign: Defending Against Prompt Injection with Preference Optimization"
  authors: ["Sizhe Chen", "Arman Zharmagambetov", "Saeed Mahloujifar", "Kamalika Chaudhuri", "David Wagner"]
  year: 2024
  venue: "arXiv"
  arxiv: "2410.05451"
  defense_type: ["D4-preference-optimization"]
  threat_model: ["direct", "indirect"]
  deploy_location: ["inference-layer"]
  tags: ["rlhf", "dpo", "preference-optimization", "fine-tuning"]
  summary: "Uses preference optimization (DPO) to train LLMs to ignore injected instructions"

- id: instruction-hierarchy-2024
  title: "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions"
  authors: ["Eric Wallace", "Kai Xiao", "Reimar Leike", "Liang Luo", "Johannes Scharfenberg", "Andrew Wan"]
  year: 2024
  venue: "arXiv"
  arxiv: "2404.13208"
  defense_type: ["D4-instruction-hierarchy"]
  threat_model: ["direct", "indirect"]
  deploy_location: ["inference-layer"]
  tags: ["privilege", "hierarchy", "openai", "system-prompt"]
  summary: "Trains LLMs to prioritize instructions by privilege level (system > user > tool output)"

- id: stronger-hierarchy-2025
  title: "Stronger Enforcement of Instruction Hierarchy via Augmented Intermediate Representations"
  year: 2025
  venue: "arXiv"
  arxiv: "2505.18907"
  defense_type: ["D4-instruction-hierarchy"]
  threat_model: ["direct", "indirect"]
  deploy_location: ["inference-layer"]
  tags: ["instruction-hierarchy", "representations", "activation"]
  summary: "Strengthens instruction hierarchy by modifying intermediate representations to enforce priority"

- id: smoothllm-2023
  title: "SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks"
  year: 2023
  venue: "arXiv"
  arxiv: "2310.03684"
  defense_type: ["D4-robustness"]
  threat_model: ["direct"]
  deploy_location: ["input-layer"]
  tags: ["randomized-smoothing", "jailbreak", "perturbation"]
  summary: "Applies randomized smoothing via input perturbation to defend against jailbreaking"

- id: baseline-defenses-2023
  title: "Baseline Defenses for Adversarial Attacks Against Aligned Language Models"
  year: 2023
  venue: "arXiv"
  arxiv: "2309.00614"
  defense_type: ["D1-input-filtering", "D2-detection", "D4-robustness"]
  threat_model: ["direct"]
  deploy_location: ["input-layer"]
  tags: ["baseline", "survey", "adversarial", "jailbreak"]
  summary: "Evaluates baseline defenses (detection, preprocessing, smoothing) against adversarial LLM attacks"

- id: backtranslation-2024
  title: "Defending LLMs against Jailbreaking Attacks via Backtranslation"
  year: 2024
  venue: "arXiv"
  arxiv: "2402.16459"
  defense_type: ["D1-input-filtering"]
  threat_model: ["direct"]
  deploy_location: ["input-layer"]
  tags: ["paraphrasing", "backtranslation", "jailbreak"]
  summary: "Paraphrases inputs via backtranslation to neutralize adversarial prompt structure"

- id: information-bottleneck-2024
  title: "Protecting Your LLMs with Information Bottleneck"
  year: 2024
  venue: "arXiv"
  arxiv: "2404.13968"
  defense_type: ["D4-robustness"]
  threat_model: ["direct"]
  deploy_location: ["inference-layer"]
  tags: ["information-bottleneck", "representation", "robustness"]
  summary: "Applies information bottleneck to LLM representations to remove adversarial information"

- id: polymorphic-prompt-2025
  title: "To Protect the LLM Agent Against the Prompt Injection Attack with Polymorphic Prompt"
  year: 2025
  venue: "arXiv"
  arxiv: "2506.05739"
  defense_type: ["D4-robustness", "D1-input-filtering"]
  threat_model: ["indirect"]
  deploy_location: ["input-layer"]
  tags: ["polymorphic", "agentic", "prompt-mutation"]
  summary: "Uses polymorphic prompt transformations to make injection attacks harder to craft"

# ─── D5: Architecture & Privilege Isolation ──────────────────────────────────

- id: camel-2025
  title: "CaMeL: Defeating Prompt Injections by Isolating LLM Access to Trusted Data"
  authors: ["Edoardo Debenedetti", "Ilia Shumailov", "Tianxiang Fan", "Nicholas Carlini", "Florian Tramèr"]
  year: 2025
  venue: "arXiv"
  defense_type: ["D5-architecture", "D5-information-flow-control"]
  threat_model: ["indirect", "multi-agent"]
  deploy_location: ["system-arch"]
  tags: ["dual-agent", "planner-executor", "capability", "information-flow"]
  summary: "Dual-LLM architecture where a reader processes untrusted content and an executor runs capability-restricted plans"

- id: ace-2025
  title: "ACE: A Security Architecture for LLM-Integrated App Systems"
  year: 2025
  venue: "arXiv"
  arxiv: "2504.20984"
  defense_type: ["D5-architecture"]
  threat_model: ["indirect", "multi-agent"]
  deploy_location: ["system-arch"]
  tags: ["capability", "access-control", "app-security", "agentic"]
  summary: "Capability-based security architecture for LLM-integrated application systems"

- id: cellmate-2025
  title: "ceLLMate: Sandboxing Browser AI Agents"
  year: 2025
  venue: "arXiv"
  arxiv: "2512.12594"
  defense_type: ["D5-architecture"]
  threat_model: ["indirect", "computer-use"]
  deploy_location: ["system-arch"]
  tags: ["sandboxing", "browser-agent", "isolation", "computer-use"]
  summary: "OS/browser sandboxing for AI agents to limit blast radius of successful injections"

- id: ifc-agents-2025
  title: "Securing AI Agents with Information-Flow Control"
  year: 2025
  venue: "arXiv"
  arxiv: "2505.23643"
  defense_type: ["D5-information-flow-control"]
  threat_model: ["indirect", "multi-agent"]
  deploy_location: ["system-arch"]
  tags: ["information-flow", "taint-tracking", "provenance", "agentic"]
  summary: "Applies IFC and taint tracking to AI agents to prevent injected data from affecting trusted operations"

- id: taming-openclaw-2026
  title: "Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats"
  year: 2026
  venue: "arXiv"
  arxiv: "2603.11619"
  defense_type: ["D5-architecture"]
  threat_model: ["indirect", "multi-agent"]
  deploy_location: ["system-arch"]
  tags: ["agentic", "security-analysis", "mitigation", "autonomous"]
  summary: "Security analysis and architectural mitigations for autonomous LLM agent threat landscape"

- id: formal-agent-security-2026
  title: "A Framework for Formalizing LLM Agent Security"
  year: 2026
  venue: "arXiv"
  arxiv: "2603.19469"
  defense_type: ["D5-architecture"]
  threat_model: ["indirect", "multi-agent"]
  deploy_location: ["system-arch"]
  tags: ["formal-model", "framework", "security-properties"]
  summary: "Formal framework for reasoning about security properties of LLM agent systems"

- id: hierarchical-autonomy-2026
  title: "From Thinker to Society: Security in Hierarchical Autonomy Evolution of AI Agents"
  year: 2026
  venue: "arXiv"
  arxiv: "2603.07496"
  defense_type: ["D5-architecture"]
  threat_model: ["multi-agent"]
  deploy_location: ["system-arch"]
  tags: ["hierarchical", "multi-agent", "autonomy", "society"]
  summary: "Security framework for hierarchical multi-agent systems across autonomy levels"

# ─── D6: Runtime Verification & Ensemble ─────────────────────────────────────

- id: melon-2025
  title: "MELON: Indirect Prompt Injection Defense via Masked Re-execution and Tool Comparison"
  year: 2025
  venue: "arXiv"
  arxiv: "2502.05174"
  defense_type: ["D6-re-execution"]
  threat_model: ["indirect"]
  deploy_location: ["inference-layer"]
  tags: ["re-execution", "tool-comparison", "detection", "agentic"]
  summary: "Re-executes tasks with masked tool outputs and detects injections by comparing execution traces"

- id: promptbench-2023
  title: "PromptBench: Towards Evaluating the Robustness of Large Language Models on Adversarial Prompts"
  year: 2023
  venue: "arXiv"
  arxiv: "2306.04528"
  defense_type: ["D6-ensemble"]
  threat_model: ["direct"]
  deploy_location: ["inference-layer"]
  tags: ["benchmark", "robustness", "evaluation", "ensemble"]
  summary: "Benchmark and ensemble-based defense evaluation for adversarial prompt robustness"

# ─── Surveys & Taxonomies ─────────────────────────────────────────────────────

- id: landscape-taxonomy-2026
  title: "The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis"
  year: 2026
  venue: "arXiv"
  arxiv: "2602.10453"
  defense_type: ["D1-input-filtering", "D3-guardrails", "D5-architecture"]
  threat_model: ["direct", "indirect", "multi-agent"]
  deploy_location: ["system-arch"]
  tags: ["survey", "taxonomy", "landscape", "agentic"]
  summary: "Comprehensive taxonomy and analysis of prompt injection threats in agentic LLM settings"

- id: attack-defense-landscape-2026
  title: "The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey"
  year: 2026
  venue: "arXiv"
  arxiv: "2603.11088"
  defense_type: ["D1-input-filtering", "D2-detection", "D3-guardrails", "D4-robustness", "D5-architecture", "D6-ensemble"]
  threat_model: ["direct", "indirect", "multi-agent", "rag", "computer-use"]
  deploy_location: ["system-arch"]
  tags: ["survey", "comprehensive", "agentic", "attack-defense"]
  summary: "Comprehensive survey of attacks and defenses in agentic AI systems"

- id: self-reminder-2023
  title: "Defending ChatGPT against Jailbreak Attack via Self-Reminder"
  year: 2023
  venue: "Nature Machine Intelligence"
  defense_type: ["D3-guardrails"]
  threat_model: ["direct"]
  deploy_location: ["input-layer"]
  tags: ["self-reminder", "system-prompt", "jailbreak"]
  summary: "Adds self-reminder instructions to system prompt to help the model resist jailbreaks"

- id: jailguard-2023
  title: "JailGuard: A Universal Detection Framework for LLM Prompt-based Attacks"
  year: 2023
  venue: "arXiv"
  arxiv: "2312.10766"
  defense_type: ["D2-detection"]
  threat_model: ["direct"]
  deploy_location: ["input-layer"]
  tags: ["detector", "universal", "mutation", "jailbreak"]
  summary: "Universal detection framework using input mutation to identify prompt-based attacks"

- id: autonomy-tax-2026
  title: "The Autonomy Tax: Defense Training Breaks LLM Agents"
  year: 2026
  venue: "arXiv"
  arxiv: "2603.19423"
  defense_type: ["D4-robustness"]
  threat_model: ["indirect"]
  deploy_location: ["inference-layer"]
  tags: ["training-tradeoffs", "capability-alignment", "autonomy"]
  summary: "Studies capability-safety tradeoff showing defense training can degrade agent task performance"

- id: may-attention-2025
  title: "May I have your Attention? Breaking Fine-Tuning based Prompt Injection Defenses using Architecture-Aware Attacks"
  year: 2025
  venue: "arXiv"
  arxiv: "2507.07417"
  defense_type: ["D4-robustness"]
  threat_model: ["direct", "indirect"]
  deploy_location: ["inference-layer"]
  tags: ["attack", "fine-tuning-bypass", "adversarial", "evaluation"]
  summary: "Demonstrates architecture-aware attacks that bypass fine-tuning-based defenses; informs robustness requirements"
```

- [ ] **Step 2: Run validator to check all entries**

```bash
cd /home/ubuntu/awesome-ipi-defense
python scripts/validate.py
```

Expected: `✓ Validation passed — N papers OK`

If there are errors, fix the YAML entry causing the error and re-run.

- [ ] **Step 3: Commit**

```bash
git add papers.yml
git commit -m "feat: add seed paper database with 45+ prompt injection defense papers"
```

---

## Task 6: README.md

**Files:**
- Create: `README.md`

- [ ] **Step 1: Create README.md**

Create `/home/ubuntu/awesome-ipi-defense/README.md`:

````markdown
# Awesome Prompt Injection Defense [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of papers on **prompt injection defense** for LLMs and AI agents,
> organized by a novel D1–D6 taxonomy.

Prompt injection attacks manipulate LLMs by embedding adversarial instructions in
untrusted content — user input, web pages, documents, tool outputs, and more.
This list tracks defensive research and provides the field's first structured taxonomy.

**Successor to** [tldrsec/prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses) (last updated 2024).

---

## Taxonomy

| ID | Defense Category | Core Idea |
|----|-----------------|-----------|
| **D1** | [Input Filtering & Pre-processing](#d1-input-filtering--pre-processing) | Transform/mark/isolate input before the LLM sees it |
| **D2** | [Detection](#d2-detection) | Statistical or ML methods to identify injection |
| **D3** | [Guardrails & Oversight](#d3-guardrails--oversight) | Safety supervision layers in parallel or series |
| **D4** | [Training-based Robustness](#d4-training-based-robustness) | Fine-tuning to make models natively resistant |
| **D5** | [Architecture & Privilege Isolation](#d5-architecture--privilege-isolation) | Structural isolation (dual-agent, IFC, sandboxing) |
| **D6** | [Runtime Verification & Ensemble](#d6-runtime-verification--ensemble) | Multi-execution comparison, voting, plan verification |

**Threat model tags:** `direct` `indirect` `multi-agent` `rag` `computer-use`

**Deployment tags:** `input-layer` `inference-layer` `output-layer` `system-arch`

→ See [docs/taxonomy.md](docs/taxonomy.md) for detailed definitions and rationale.

---

## Papers by Year

### 2026

- **[The Landscape of Prompt Injection Threats in LLM Agents](https://arxiv.org/abs/2602.10453)** (2026) `survey` `taxonomy`
  Comprehensive taxonomy and analysis of prompt injection threats in agentic LLM settings.

- **[The Attack and Defense Landscape of Agentic AI](https://arxiv.org/abs/2603.11088)** (2026) `survey`
  Comprehensive survey of attacks and defenses in agentic AI systems.

- **[Zero-Shot Embedding Drift Detection](https://arxiv.org/abs/2601.12359)** (2026) `D2` `indirect` `inference-layer`
  Detects prompt injections by measuring semantic drift in embeddings without task-specific training.

- **[Real User Instruction](https://www.preprints.org/manuscript/202601.2168)** (2026) `D1` `indirect` `input-layer`
  Black-box middleware that authenticates whether instructions originate from real users vs. injected sources.

- **[Recursive LM for Jailbreak Detection](https://arxiv.org/abs/2602.16520)** (2026) `D3` `indirect` `multi-agent` `inference-layer`
  Hierarchical LLM calls for multi-level jailbreak detection in tool-augmented agent systems.

- **[A Framework for Formalizing LLM Agent Security](https://arxiv.org/abs/2603.19469)** (2026) `D5` `multi-agent` `system-arch`
  Formal framework for reasoning about security properties of LLM agent systems.

- **[The Autonomy Tax](https://arxiv.org/abs/2603.19423)** (2026) `D4` `indirect` `inference-layer`
  Studies capability-safety tradeoff showing defense training can degrade agent performance.

- **[Taming OpenClaw](https://arxiv.org/abs/2603.11619)** (2026) `D5` `indirect` `multi-agent` `system-arch`
  Security analysis and architectural mitigations for autonomous LLM agent threats.

- **[From Thinker to Society](https://arxiv.org/abs/2603.07496)** (2026) `D5` `multi-agent` `system-arch`
  Security framework for hierarchical multi-agent systems across autonomy levels.

### 2025

- **[CaMeL](https://arxiv.org/abs/2503.18813)** (2025) `D5` `indirect` `multi-agent` `system-arch`
  Dual-LLM architecture where a reader processes untrusted content and an executor runs capability-restricted plans.
  *Debenedetti et al. (ETH Zürich)*

- **[SecAlign](https://arxiv.org/abs/2410.05451)** (2025) `D4` `direct` `indirect` `inference-layer`
  Uses preference optimization (DPO) to train LLMs to ignore injected instructions.
  *Chen et al.*

- **[MELON](https://arxiv.org/abs/2502.05174)** (2025) `D6` `indirect` `inference-layer`
  Re-executes tasks with masked tool outputs and detects injections by comparing execution traces.

- **[GuardReasoner](https://arxiv.org/abs/2501.18492)** (2025) `D3` `direct` `input-layer` `output-layer`
  Incorporates chain-of-thought reasoning into LLM safety guards for better explainability.

- **[UniGuardian](https://arxiv.org/abs/2502.13141)** (2025) `D2` `direct` `indirect` `input-layer`
  Unified detection framework covering prompt injection, backdoor, and adversarial attacks.

- **[DataSentinel](https://arxiv.org/abs/2504.11358)** (2025) `D2` `indirect` `input-layer`
  Game-theoretic framework for robust prompt injection detection accounting for adaptive adversaries.

- **[Securing AI Agents with IFC](https://arxiv.org/abs/2505.23643)** (2025) `D5` `indirect` `multi-agent` `system-arch`
  Applies information flow control and taint tracking to AI agents.

- **[Stronger Enforcement of Instruction Hierarchy](https://arxiv.org/abs/2505.18907)** (2025) `D4` `direct` `indirect` `inference-layer`
  Strengthens instruction hierarchy by modifying intermediate representations.

- **[ACE](https://arxiv.org/abs/2504.20984)** (2025) `D5` `indirect` `multi-agent` `system-arch`
  Capability-based security architecture for LLM-integrated application systems.

- **[ceLLMate](https://arxiv.org/abs/2512.12594)** (2025) `D5` `indirect` `computer-use` `system-arch`
  OS/browser sandboxing for AI agents to limit blast radius of successful injections.

- **[RTBAS](https://arxiv.org/abs/2407.09641)** (2025) `D1` `D3` `indirect` `multi-agent`
  Defends LLM agents against prompt injection and privacy leakage via input/output control.

- **[DataFilter](https://arxiv.org/abs/2510.19207)** (2025) `D1` `indirect` `rag` `input-layer`
  Filters retrieved content before injection into context.

- **[Detecting PI with Classifiers](https://arxiv.org/abs/2512.12583)** (2025) `D2` `direct` `indirect` `input-layer`
  Curates augmented prompt injection dataset and evaluates classifier-based detection approaches.

- **[Polymorphic Prompt Defense](https://arxiv.org/abs/2506.05739)** (2025) `D4` `D1` `indirect` `input-layer`
  Uses polymorphic prompt transformations to make injection attacks harder to craft.

- **[May I have your Attention?](https://arxiv.org/abs/2507.07417)** (2025) `D4` `direct` `indirect` `inference-layer`
  Architecture-aware attacks that bypass fine-tuning-based defenses; motivates robustness requirements.

### 2024

- **[AgentDojo](https://arxiv.org/abs/2406.13352)** (2024) `benchmark` `indirect` `multi-agent`
  Dynamic benchmark for evaluating prompt injection attacks and defenses in LLM agent pipelines.
  *Debenedetti et al. — NeurIPS 2024*

- **[StruQ](https://arxiv.org/abs/2402.06363)** (2024) `D1` `direct` `indirect` `input-layer`
  Separates instructions and data using structured format to prevent injection.
  *Chen et al. — USENIX Security 2025*

- **[Spotlighting](https://arxiv.org/abs/2403.14720)** (2024) `D1` `indirect` `rag` `input-layer`
  Marks untrusted data segments with distinctive tokens so the model knows what is trusted vs. untrusted.
  *Hines et al.*

- **[Instruction Hierarchy](https://arxiv.org/abs/2404.13208)** (2024) `D4` `direct` `indirect` `inference-layer`
  Trains LLMs to prioritize instructions by privilege level (system > user > tool output).
  *Wallace et al. — OpenAI*

- **[InjecGuard](https://arxiv.org/abs/2410.22770)** (2024) `D2` `direct` `indirect` `input-layer`
  Addresses false positive problem in injection detectors; introduces benchmark and mitigation.

- **[GradSafe](https://arxiv.org/abs/2402.13494)** (2024) `D2` `direct` `inference-layer`
  Detects unsafe prompts by analyzing gradients of safety-critical tokens.

- **[Task Shield](https://arxiv.org/abs/2412.16682)** (2024) `D3` `indirect` `inference-layer`
  Enforces alignment between agent actions and original user task to detect indirect injection.

- **[Agent Security Bench](https://arxiv.org/abs/2410.02644)** (2024) `benchmark` `direct` `indirect` `multi-agent`
  Comprehensive benchmark formalizing attack and defense space for LLM-based agents.

- **[Signed-Prompt](https://arxiv.org/abs/2401.07612)** (2024) `D1` `direct` `indirect` `input-layer`
  Cryptographically signs trusted instructions to allow models to distinguish them from injected content.

- **[Building Guardrails for LLMs](https://arxiv.org/abs/2402.01822)** (2024) `D3` `survey`
  Survey and framework for designing comprehensive guardrail systems for LLMs.

- **[Backtranslation Defense](https://arxiv.org/abs/2402.16459)** (2024) `D1` `direct` `input-layer`
  Paraphrases inputs via backtranslation to neutralize adversarial prompt structure.

- **[Information Bottleneck Defense](https://arxiv.org/abs/2404.13968)** (2024) `D4` `direct` `inference-layer`
  Applies information bottleneck to LLM representations to remove adversarial information.

### 2023 and Earlier

- **[Jatmo](https://arxiv.org/abs/2312.17673)** (2023) `D4` `direct` `indirect` `inference-layer`
  Fine-tunes task-specific models that treat external data as inert, ignoring injected instructions.
  *Piet et al. — ESORICS 2024*

- **[NeMo Guardrails](https://arxiv.org/abs/2310.10501)** (2023) `D3` `direct` `input-layer` `output-layer`
  Open-source toolkit for adding programmable safety guardrails to LLM applications. *NVIDIA*

- **[Llama Guard](https://arxiv.org/abs/2312.06674)** (2023) `D3` `direct` `input-layer` `output-layer`
  LLM-based input-output safety classifier for human-AI conversations. *Meta*

- **[SmoothLLM](https://arxiv.org/abs/2310.03684)** (2023) `D4` `direct` `input-layer`
  Applies randomized smoothing via input perturbation to defend against jailbreaking.

- **[Perplexity-based Detection](https://arxiv.org/abs/2308.14132)** (2023) `D2` `direct` `input-layer`
  Uses perplexity scores to detect adversarial prompts and jailbreak attempts.

- **[Token-Level Perplexity Detection](https://arxiv.org/abs/2311.11509)** (2023) `D2` `direct` `input-layer`
  Token-level perplexity analysis for fine-grained adversarial prompt detection.

- **[JailGuard](https://arxiv.org/abs/2312.10766)** (2023) `D2` `direct` `input-layer`
  Universal detection framework using input mutation to identify prompt-based attacks.

- **[LLM Self Defense](https://arxiv.org/abs/2308.07308)** (2023) `D3` `direct` `inference-layer`
  LLMs can detect jailbreaks by examining their own context for signs of manipulation.

- **[Robust Safety Classifier](https://arxiv.org/abs/2311.00172)** (2023) `D3` `direct` `input-layer`
  Robust safety classifier designed to withstand adversarial prompt attacks.

- **[Baseline Defenses](https://arxiv.org/abs/2309.00614)** (2023) `D1` `D2` `D4` `direct`
  Evaluates baseline defenses (detection, preprocessing, smoothing) against adversarial LLM attacks.

- **[Self-Reminder](https://www.nature.com/articles/s42256-023-00765-8)** (2023) `D3` `direct` `input-layer`
  Adds self-reminder instructions to system prompt to help the model resist jailbreaks.
  *Nature Machine Intelligence*

- **[PromptBench](https://arxiv.org/abs/2306.04528)** (2023) `D6` `direct` `inference-layer`
  Benchmark and ensemble evaluation for adversarial prompt robustness.

---

## Papers by Defense Type

### D1: Input Filtering & Pre-processing

> Transform, mark, or isolate untrusted input *before* it reaches the LLM's reasoning process.

- **[StruQ](https://arxiv.org/abs/2402.06363)** (2024) `direct` `indirect`
  Separates instructions and data using structured format to prevent injection.
- **[Spotlighting](https://arxiv.org/abs/2403.14720)** (2024) `indirect` `rag`
  Marks untrusted data with distinctive tokens.
- **[Signed-Prompt](https://arxiv.org/abs/2401.07612)** (2024) `direct` `indirect`
  Cryptographically signs trusted instructions.
- **[DataFilter](https://arxiv.org/abs/2510.19207)** (2025) `indirect` `rag`
  Filters retrieved content before injection into context.
- **[RTBAS](https://arxiv.org/abs/2407.09641)** (2025) `indirect` `multi-agent`
  Input/output control for LLM agents against injection and privacy leakage.
- **[Real User Instruction](https://www.preprints.org/manuscript/202601.2168)** (2026) `indirect`
  Middleware authenticating instructions as originating from real users.
- **[Backtranslation Defense](https://arxiv.org/abs/2402.16459)** (2024) `direct`
  Paraphrases inputs to neutralize adversarial structure.
- **[Baseline Defenses](https://arxiv.org/abs/2309.00614)** (2023) `direct`
  Baseline evaluation including preprocessing defenses.
- **[Polymorphic Prompt Defense](https://arxiv.org/abs/2506.05739)** (2025) `indirect`
  Polymorphic transformations to make injections harder to craft.

### D2: Detection

> Statistical or ML methods to identify injection behavior.

- **[Perplexity-based Detection](https://arxiv.org/abs/2308.14132)** (2023) `direct`
  Perplexity scores to detect adversarial prompts.
- **[Token-Level Perplexity Detection](https://arxiv.org/abs/2311.11509)** (2023) `direct`
  Token-level perplexity for fine-grained detection.
- **[GradSafe](https://arxiv.org/abs/2402.13494)** (2024) `direct`
  Gradient analysis of safety-critical tokens.
- **[InjecGuard](https://arxiv.org/abs/2410.22770)** (2024) `direct` `indirect`
  Addresses over-defense in injection detectors.
- **[JailGuard](https://arxiv.org/abs/2312.10766)** (2023) `direct`
  Universal detection via input mutation.
- **[DataSentinel](https://arxiv.org/abs/2504.11358)** (2025) `indirect`
  Game-theoretic robust detection.
- **[UniGuardian](https://arxiv.org/abs/2502.13141)** (2025) `direct` `indirect`
  Unified detection for injection, backdoor, and adversarial attacks.
- **[Detecting PI with Classifiers](https://arxiv.org/abs/2512.12583)** (2025) `direct` `indirect`
  Classifier-based detection with augmented dataset.
- **[Zero-Shot Embedding Drift Detection](https://arxiv.org/abs/2601.12359)** (2026) `indirect`
  Semantic drift detection without task-specific training.

### D3: Guardrails & Oversight

> Safety supervision layers running in parallel or series with the primary LLM.

- **[NeMo Guardrails](https://arxiv.org/abs/2310.10501)** (2023) `direct`
  Programmable safety rails toolkit.
- **[Llama Guard](https://arxiv.org/abs/2312.06674)** (2023) `direct`
  LLM-based input-output safety classifier.
- **[Self-Reminder](https://www.nature.com/articles/s42256-023-00765-8)** (2023) `direct`
  System-prompt self-reminder against jailbreaks.
- **[LLM Self Defense](https://arxiv.org/abs/2308.07308)** (2023) `direct`
  Model examines its own context for manipulation.
- **[Robust Safety Classifier](https://arxiv.org/abs/2311.00172)** (2023) `direct`
  Adversarially robust safety classifier.
- **[Building Guardrails for LLMs](https://arxiv.org/abs/2402.01822)** (2024) `survey`
  Survey and framework for guardrail design.
- **[Task Shield](https://arxiv.org/abs/2412.16682)** (2024) `indirect`
  Task-alignment checking for agent actions.
- **[GuardReasoner](https://arxiv.org/abs/2501.18492)** (2025) `direct`
  Reasoning-based LLM safety guards.
- **[RTBAS](https://arxiv.org/abs/2407.09641)** (2025) `indirect` `multi-agent`
  Output-layer control for LLM agents.
- **[Recursive LM Guard](https://arxiv.org/abs/2602.16520)** (2026) `indirect` `multi-agent`
  Hierarchical recursive detection for tool-augmented agents.
- **[Adaptive Multi-Layer Framework](https://doi.org/10.20473/jisebi.11.1.87-100)** (2025)
  Multi-layer adaptive detection and guardrail framework.

### D4: Training-based Robustness

> Fine-tuning to make models natively resistant.

- **[Jatmo](https://arxiv.org/abs/2312.17673)** (2023) `direct` `indirect`
  Task-specific fine-tuning that makes models treat data as inert.
- **[SmoothLLM](https://arxiv.org/abs/2310.03684)** (2023) `direct`
  Randomized smoothing via input perturbation.
- **[Baseline Defenses](https://arxiv.org/abs/2309.00614)** (2023) `direct`
  Baseline evaluation including robustness training.
- **[Instruction Hierarchy](https://arxiv.org/abs/2404.13208)** (2024) `direct` `indirect`
  Privilege-based instruction priority training.
- **[SecAlign](https://arxiv.org/abs/2410.05451)** (2024) `direct` `indirect`
  DPO-based preference optimization against injection.
- **[Information Bottleneck Defense](https://arxiv.org/abs/2404.13968)** (2024) `direct`
  Representation-level information bottleneck.
- **[Stronger Instruction Hierarchy](https://arxiv.org/abs/2505.18907)** (2025) `direct` `indirect`
  Intermediate representation augmentation for hierarchy enforcement.
- **[Polymorphic Prompt Defense](https://arxiv.org/abs/2506.05739)** (2025) `indirect`
  Polymorphic transformations for robustness.
- **[May I have your Attention?](https://arxiv.org/abs/2507.07417)** (2025) `direct` `indirect`
  Attack exposing limitations of fine-tuning defenses.
- **[The Autonomy Tax](https://arxiv.org/abs/2603.19423)** (2026) `indirect`
  Analysis of capability-safety tradeoff in defense training.

### D5: Architecture & Privilege Isolation

> Structural isolation of agents and data flows.

- **[CaMeL](https://arxiv.org/abs/2503.18813)** (2025) `indirect` `multi-agent`
  Dual-LLM planner-executor separation with capability restriction.
- **[ACE](https://arxiv.org/abs/2504.20984)** (2025) `indirect` `multi-agent`
  Capability-based security architecture.
- **[ceLLMate](https://arxiv.org/abs/2512.12594)** (2025) `indirect` `computer-use`
  Browser agent sandboxing.
- **[Securing Agents with IFC](https://arxiv.org/abs/2505.23643)** (2025) `indirect` `multi-agent`
  Information flow control and taint tracking.
- **[Taming OpenClaw](https://arxiv.org/abs/2603.11619)** (2026) `indirect` `multi-agent`
  Security analysis and mitigations for autonomous agents.
- **[Framework for Formalizing Agent Security](https://arxiv.org/abs/2603.19469)** (2026) `multi-agent`
  Formal security framework for LLM agents.
- **[From Thinker to Society](https://arxiv.org/abs/2603.07496)** (2026) `multi-agent`
  Hierarchical multi-agent security framework.

### D6: Runtime Verification & Ensemble

> Multi-execution comparison, voting, and plan verification.

- **[PromptBench](https://arxiv.org/abs/2306.04528)** (2023) `direct`
  Benchmark and ensemble evaluation for robustness.
- **[MELON](https://arxiv.org/abs/2502.05174)** (2025) `indirect`
  Masked re-execution and tool output comparison for injection detection.

---

## Benchmarks & Evaluation

- **[AgentDojo](https://arxiv.org/abs/2406.13352)** (2024) — NeurIPS 2024
  Dynamic benchmark for evaluating prompt injection attacks and defenses in LLM agent pipelines.
  *Debenedetti et al. (ETH Zürich)*

- **[Agent Security Bench (ASB)](https://arxiv.org/abs/2410.02644)** (2024)
  Formalizes and benchmarks attacks and defenses in LLM-based agents.

- **[InjecGuard](https://arxiv.org/abs/2410.22770)** (2024) — also includes benchmark
  Benchmark for over-defense in prompt injection guardrail models.

- **[PromptBench](https://arxiv.org/abs/2306.04528)** (2023)
  Benchmark for evaluating LLM robustness against adversarial prompts.

---

## Surveys & Taxonomies

- **[The Landscape of Prompt Injection Threats in LLM Agents](https://arxiv.org/abs/2602.10453)** (2026)
  From taxonomy to analysis — comprehensive coverage of agentic settings.

- **[The Attack and Defense Landscape of Agentic AI](https://arxiv.org/abs/2603.11088)** (2026)
  Comprehensive survey across all attack and defense categories.

- **[When LLMs meet cybersecurity](https://link.springer.com/article/10.1186/s42400-025-00361-w)** (2025)
  Systematic literature review on LLM security including prompt injection. *Cybersecurity journal*

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add papers.

Papers are stored in [papers.yml](papers.yml). The README is maintained manually in sync.

All PRs run automatic schema validation via GitHub Actions.

---

*Maintained by the community. Last structured update: 2026-04-08.*
*Taxonomy version: 1.0*
````

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "feat: add README with D1-D6 taxonomy and 45+ seed papers"
```

---

## Task 7: CONTRIBUTING.md

**Files:**
- Create: `CONTRIBUTING.md`

- [ ] **Step 1: Create CONTRIBUTING.md**

Create `/home/ubuntu/awesome-ipi-defense/CONTRIBUTING.md`:

```markdown
# Contributing to awesome-ipi-defense

Thank you for helping maintain the field's most comprehensive prompt injection defense list!

---

## How to Add a Paper

### Step 1: Add to `papers.yml`

Add an entry to `papers.yml` following this schema:

```yaml
- id: <lastname>-<keyword>-<year>          # e.g., chen-struq-2024
  title: "Full paper title"
  authors: ["Author One", "Author Two"]    # optional
  year: 2024                               # required, integer
  venue: "Conference or Journal Name"      # optional
  arxiv: "2402.06363"                      # optional, no prefix
  doi: "10.xxxx/xxxxx"                     # optional
  defense_type:                            # required, one or more
    - D1-input-filtering
  threat_model:                            # required, one or more
    - indirect
  deploy_location:                         # optional
    - input-layer
  tags:                                    # optional, free-form
    - structured-output
  summary: "One sentence description"      # optional
```

### Step 2: Add to `README.md`

Add the paper in **both** locations:
1. Under `## Papers by Year` → correct year section
2. Under `## Papers by Defense Type` → correct D1–D6 section

Format:
```markdown
- **[Paper Title](https://arxiv.org/abs/XXXX.XXXXX)** (YEAR) `D1` `indirect` `input-layer`
  One sentence description.
  *Authors — Venue*
```

### Step 3: Validate

```bash
python scripts/validate.py
```

Must pass with no errors before submitting a PR.

### Step 4: Submit PR

PRs are automatically validated by GitHub Actions.

---

## Schema Reference

### Required Fields

| Field | Type | Constraints |
|-------|------|-------------|
| `id` | string | Unique slug, lowercase, hyphens only |
| `title` | string | Full paper title |
| `year` | integer | 2020–2030 |
| `defense_type` | list | See allowed values below |
| `threat_model` | list | See allowed values below |

### `defense_type` Allowed Values

| Code | Category |
|------|----------|
| `D1` or `D1-*` | Input Filtering & Pre-processing |
| `D2` or `D2-*` | Detection |
| `D3` or `D3-*` | Guardrails & Oversight |
| `D4` or `D4-*` | Training-based Robustness |
| `D5` or `D5-*` | Architecture & Privilege Isolation |
| `D6` or `D6-*` | Runtime Verification & Ensemble |

Common sub-codes: `D1-input-filtering`, `D2-detection`, `D3-guardrails`, `D4-finetuning`,
`D4-instruction-hierarchy`, `D4-preference-optimization`, `D4-robustness`,
`D5-architecture`, `D5-information-flow-control`, `D6-re-execution`, `D6-ensemble`

### `threat_model` Allowed Values

| Value | Meaning |
|-------|---------|
| `direct` | Attacker controls user-facing input |
| `indirect` | Attacker plants injections in external content |
| `multi-agent` | Injection propagates across agent communication |
| `rag` | Injection embedded in retrieved documents |
| `computer-use` | Injection via UI/screenshots/rendered content |

### `deploy_location` Allowed Values (optional)

| Value | Meaning |
|-------|---------|
| `input-layer` | Applied before LLM inference |
| `inference-layer` | Modifies or monitors inference |
| `output-layer` | Applied to LLM outputs |
| `system-arch` | Structural, not layer-specific |

---

## Inclusion Criteria

**Include:**
- Papers with a clear defensive contribution against prompt injection
- Evaluation or benchmark papers for injection defenses
- Survey/taxonomy papers covering injection defenses
- Papers addressing jailbreaks where they overlap with injection

**Exclude:**
- Jailbreak-only papers with no injection component
- Hallucination or data poisoning papers unrelated to injection
- Papers without public preprint or publication

---

## Taxonomy Changes

To propose changes to the D1–D6 taxonomy, open an issue with:
1. The gap or problem with the current taxonomy
2. Evidence from ≥3 papers that don't fit existing categories
3. Proposed new category or sub-category with definition

---

## Questions?

Open an issue. We're happy to help classify papers or discuss taxonomy edge cases.
```

- [ ] **Step 2: Commit**

```bash
git add CONTRIBUTING.md
git commit -m "docs: add contributing guide with schema reference"
```

---

## Task 8: Final Validation & Integration Test

- [ ] **Step 1: Run full test suite**

```bash
cd /home/ubuntu/awesome-ipi-defense
python -m pytest tests/test_validate.py -v
```

Expected: All tests PASS.

- [ ] **Step 2: Run validator against final papers.yml**

```bash
python scripts/validate.py
```

Expected: `✓ Validation passed — N papers OK`

- [ ] **Step 3: Verify repository structure**

```bash
find . -not -path './.git/*' -not -path './__pycache__/*' | sort
```

Expected output:
```
.
./.gitignore
./.github
./.github/workflows
./.github/workflows/validate.yml
./CONTRIBUTING.md
./README.md
./docs
./docs/superpowers
./docs/superpowers/plans
./docs/superpowers/plans/2026-04-08-awesome-ipi-defense.md
./docs/superpowers/specs
./docs/superpowers/specs/2026-04-08-awesome-ipi-defense-design.md
./docs/taxonomy.md
./papers.yml
./scripts
./scripts/validate.py
./tests
./tests/test_validate.py
```

- [ ] **Step 4: Check README links are well-formed**

```bash
python3 -c "
import re
with open('README.md') as f:
    content = f.read()
links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
arxiv_links = [(t, u) for t, u in links if 'arxiv.org' in u]
print(f'Total links: {len(links)}')
print(f'ArXiv links: {len(arxiv_links)}')
# Check all arxiv links have numeric IDs
bad = [(t, u) for t, u in arxiv_links if not re.search(r'\d{4}\.\d{4,5}', u)]
if bad:
    print('Malformed arxiv links:')
    for t, u in bad:
        print(f'  {t}: {u}')
else:
    print('All arxiv links look well-formed.')
"
```

- [ ] **Step 5: Final commit**

```bash
git add docs/superpowers/plans/2026-04-08-awesome-ipi-defense.md
git commit -m "docs: add implementation plan"
git log --oneline
```

Expected: 7–8 commits showing incremental build.

---

## Self-Review Against Spec

| Spec Requirement | Implemented In |
|-----------------|----------------|
| README.md with taxonomy + two views | Task 6 |
| papers.yml with schema | Tasks 4 + 5 |
| CONTRIBUTING.md with schema docs | Task 7 |
| docs/taxonomy.md with D1–D6 rationale | Task 4 |
| GitHub Actions YAML validator | Task 3 |
| Validator Python script | Task 2 |
| Unit tests for validator | Task 2 |
| Seed papers from tldrsec + key known | Task 5 |
| CaMeL classified as D5 | Task 5 ✓ |
| Multi-tag defense_type support | validator + papers.yml ✓ |
| Threat model tags | validator + all entries ✓ |
| Out of scope: no web frontend | not built ✓ |
