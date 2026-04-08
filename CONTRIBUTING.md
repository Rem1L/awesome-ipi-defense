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
1. Under `## Papers by Year` in the correct year section
2. Under `## Papers by Defense Type` in the correct D1–D6 section

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
2. Evidence from 3+ papers that don't fit existing categories
3. Proposed new category or sub-category with definition

---

## Questions?

Open an issue. We're happy to help classify papers or discuss taxonomy edge cases.
