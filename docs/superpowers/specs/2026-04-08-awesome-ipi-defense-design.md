# Design Spec: awesome-ipi-defense

**Date:** 2026-04-08
**Status:** Approved
**Scope:** New awesome list for prompt injection defense papers with taxonomy

---

## Problem

The [tldrsec/prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses) collection stopped being updated in 2024. The field has grown significantly, particularly in agentic settings, and lacks a structured taxonomy. This project fills both gaps.

---

## Goals

1. Maintain an up-to-date collection of prompt injection defense papers
2. Provide the field's first structured defense taxonomy (primary contribution)
3. Serve both researchers (paper discovery, citation) and engineers (implementable defenses)
4. Support machine-readable data for automation and tooling

---

## Audience

- Academic researchers tracking the literature
- Engineers looking for implementable defense mechanisms

---

## Approach: README + Structured Data (Approach B)

- `README.md`: Human-readable taxonomy framework + paper listings (two views: by year, by defense type)
- `papers.yml`: Machine-readable full database with schema-validated fields
- GitHub Actions: YAML schema validation on PRs
- Future: automated paper discovery via OpenAlex/Semantic Scholar

---

## Taxonomy

### Primary Defense Classification (D1–D6)

| ID | Category | Core Idea |
|----|----------|-----------|
| D1 | Input Filtering & Pre-processing | Transform/mark/isolate input before it reaches the LLM |
| D2 | Detection | Statistical or ML methods to identify injection behavior |
| D3 | Guardrails & Oversight | Safety supervision layers running in parallel or series |
| D4 | Training-based Robustness | Fine-tuning to make models natively resistant |
| D5 | Architecture & Privilege Isolation | Structural isolation (dual-agent, IFC, capability, sandboxing) |
| D6 | Runtime Verification & Ensemble | Multi-execution comparison, voting, plan verification |

### Orthogonal Tags

**Threat model:** `direct` / `indirect` / `multi-agent` / `rag` / `computer-use`

**Deployment location:** `input-layer` / `inference-layer` / `output-layer` / `system-arch`

### Classification Notes

- Papers may have multiple `defense_type` tags (e.g., CaMeL: `D5-architecture` + `D5-information-flow-control`)
- D5 intentionally groups capability-based, IFC, sandboxing, and dual-agent designs into one category for now; may be split in future versions as literature matures

---

## Repository Structure

```
awesome-ipi-defense/
├── README.md              # Taxonomy overview + papers (by year and by type)
├── papers.yml             # Full structured paper database
├── CONTRIBUTING.md        # Contribution guide + YAML schema docs
├── .github/
│   └── workflows/
│       └── validate.yml   # PR-time YAML schema validation
└── docs/
    └── taxonomy.md        # Detailed taxonomy rationale and definitions
    └── superpowers/
        └── specs/
            └── 2026-04-08-awesome-ipi-defense-design.md
```

---

## papers.yml Schema

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique slug, e.g. `struq-2024` |
| `title` | string | Full paper title |
| `year` | integer | Publication year |
| `defense_type` | list[string] | One or more of D1–D6 subcategory codes |
| `threat_model` | list[string] | `direct`, `indirect`, `multi-agent`, `rag`, `computer-use` |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `authors` | list[string] | Author names |
| `venue` | string | Conference/journal name |
| `arxiv` | string | ArXiv ID without prefix |
| `doi` | string | DOI |
| `deploy_location` | list[string] | `input-layer`, `inference-layer`, `output-layer`, `system-arch` |
| `tags` | list[string] | Free-form keywords |
| `summary` | string | One-sentence description |

### Example Entry

```yaml
- id: struq-2024
  title: "StruQ: Defending Against Prompt Injection with Structured Queries"
  authors: ["Sizhe Chen", "Julien Piet", "Chawin Sitawarin", "David Wagner"]
  year: 2024
  venue: "USENIX Security 2025"
  arxiv: "2402.06363"
  defense_type: ["D1-input-filtering"]
  threat_model: ["direct", "indirect"]
  deploy_location: ["input-layer"]
  tags: ["structured-output", "delimiter"]
  summary: "Separates instructions and data with structured format to prevent injection"
```

---

## README Structure

```markdown
# Awesome Prompt Injection Defense

## Taxonomy
(compact table + link to docs/taxonomy.md)

## Papers by Year
### 2026
### 2025
### 2024
### 2023 and Earlier

## Papers by Defense Type
### D1: Input Filtering & Pre-processing
### D2: Detection
### D3: Guardrails & Oversight
### D4: Training-based Robustness
### D5: Architecture & Privilege Isolation
### D6: Runtime Verification & Ensemble

## Benchmarks & Evaluation
(AgentDojo, ASB, etc.)

## Surveys & Taxonomies

## Contributing
```

### Paper Entry Format

```markdown
- **[StruQ](https://arxiv.org/abs/2402.06363)** (2024) `D1` `indirect` `input-layer`
  Separates instructions and data using structured formats to prevent injection.
  *Chen et al. — USENIX Security 2025*
```

Papers appear in both "By Year" and "By Defense Type" sections; anchor links prevent content duplication.

---

## Seed Papers

Initial corpus built from:
1. All papers in tldrsec/prompt-injection-defenses (≈38 papers)
2. Papers citing AgentDojo (OpenAlex + Semantic Scholar)
3. OpenAlex search for "prompt injection defense" 2023–2026
4. Key known papers: StruQ, SecAlign, Spotlighting, Instruction Hierarchy, Jatmo, CaMeL, MELON, Task Shield, DataFilter, InjecGuard, RTBAS, DataSentinel, ACE, ceLLMate

---

## GitHub Actions: YAML Validation

On every PR, validate `papers.yml` against schema:
- Required fields present
- `defense_type` values are valid D1–D6 codes
- `threat_model` values are from allowed set
- `year` is integer in range 2020–2030
- `id` is unique

Simple Python script, no external dependencies beyond PyYAML.

---

## Out of Scope (v1)

- Web frontend / search UI
- Automated paper ingestion (future GitHub Action)
- Jailbreak-only papers with no prompt injection component
- Papers on hallucination, data poisoning unrelated to injection
