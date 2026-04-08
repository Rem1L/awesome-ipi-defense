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
