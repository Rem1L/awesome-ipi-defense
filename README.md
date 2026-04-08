# Awesome IPI Defense

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![papers](https://img.shields.io/badge/papers-66-blue)](README.md)
[![arXiv](https://img.shields.io/badge/arXiv-43-red)](README.md)

A curated collection of research papers on defending Large Language Model (LLM) agents against prompt injection attacks. This repository focuses on **indirect prompt injection (IPI)** and related threats, organizing defenses into a structured taxonomy (D1-D6).

## Taxonomy Overview

| ID | Defense Category | Core Idea |
|----|-----------------|-----------|
| **D1** | [Input Filtering & Pre-processing](#d1-input-filtering--pre-processing) | Prevent injection by marking/separating trusted and untrusted data before LLM processing |
| **D2** | [Detection](#d2-detection) | Monitor and flag suspicious prompts or execution patterns |
| **D3** | [Guardrails & Oversight](#d3-guardrails--oversight) | Programmatic and LLM-based safeguards on model inputs/outputs |
| **D4** | [Training-based Robustness](#d4-training-based-robustness) | Fine-tune or preference-optimize models to resist injection |
| **D5** | [Architecture & Privilege Isolation](#d5-architecture--privilege-isolation) | Isolate untrusted data via multi-agent or capability-based designs |
| **D6** | [Runtime Verification & Ensemble](#d6-runtime-verification--ensemble) | Verify execution correctness through re-execution or ensemble consensus |

## Papers by Year

### 2026

- **[AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification](https://arxiv.org/abs/2602.22724)** (2026) `D5,D3` `indirect,multi-agent` `system-arch`
  Combines temporal causal diagnostics and context purification to detect and mitigate indirect prompt injections.

- **[HIPO: Instruction Hierarchy via Constrained Reinforcement Learning](https://arxiv.org/abs/2603.16152)** (2026) `D4` `direct,indirect` `inference-layer`
  Uses constrained RL to train LLMs to follow instruction hierarchies robustly under adversarial conditions.

- **[IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs](https://arxiv.org/abs/2603.10521)** (2026) `D4` `direct,indirect` `inference-layer`
  Training dataset specifically designed to improve instruction hierarchy compliance in frontier LLMs.

- **[RedVisor: Reasoning-Aware Prompt Injection Defense via Zero-Copy KV Cache Reuse](https://arxiv.org/abs/2602.01795)** (2026) `D5,D6` `indirect` `inference-layer,system-arch`
  Defends against prompt injection by isolating trusted reasoning from untrusted context via KV cache separation.

- **[Real User Instruction: Black-Box Instruction Authentication Middleware Against Indirect Prompt Injection](https://arxiv.org/abs/2601.12359)** (2026) `D1` `indirect` `input-layer`
  Middleware that authenticates whether instructions originate from real users vs. injected sources.
  *Venue: Preprints.org*

- **[Zero-Shot Embedding Drift Detection: A Lightweight Defense Against Prompt Injections in LLMs](https://arxiv.org/abs/2601.12359)** (2026) `D2` `indirect` `inference-layer`
  Detects prompt injections by measuring semantic drift in embeddings without task-specific training.

- **[Recursive language models for jailbreak detection: a procedural defense for tool-augmented agents](https://arxiv.org/abs/2602.16520)** (2026) `D3` `indirect,multi-agent` `inference-layer`
  Hierarchical LLM calls for multi-level jailbreak detection in tool-augmented agent systems.

- **[The Autonomy Tax: Defense Training Breaks LLM Agents](https://arxiv.org/abs/2603.19423)** (2026) `D4` `indirect` `inference-layer`
  Studies capability-safety tradeoff showing defense training can degrade agent task performance.

- **[Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats](https://arxiv.org/abs/2603.11619)** (2026) `D5` `indirect,multi-agent` `system-arch`
  Security analysis and architectural mitigations for autonomous LLM agent threat landscape.

- **[A Framework for Formalizing LLM Agent Security](https://arxiv.org/abs/2603.19469)** (2026) `D5` `indirect,multi-agent` `system-arch`
  Formal framework for reasoning about security properties of LLM agent systems.

- **[From Thinker to Society: Security in Hierarchical Autonomy Evolution of AI Agents](https://arxiv.org/abs/2603.07496)** (2026) `D5` `multi-agent` `system-arch`
  Security framework for hierarchical multi-agent systems across autonomy levels.

- **[The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis](https://arxiv.org/abs/2602.10453)** (2026) `D1,D3,D5` `direct,indirect,multi-agent` `system-arch`
  Comprehensive taxonomy and analysis of prompt injection threats in agentic LLM settings.

- **[The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey](https://arxiv.org/abs/2603.11088)** (2026) `D1,D2,D3,D4,D5,D6` `direct,indirect,multi-agent,rag,computer-use` `system-arch`
  Comprehensive survey of attacks and defenses in agentic AI systems.

### 2025

- **[Defending Against Prompt Injection with DataFilter](https://arxiv.org/abs/2510.19207)** (2025) `D1` `indirect,rag` `input-layer`
  Filters retrieved content before injection into context to remove adversarial instructions.

- **[Control Illusion: The Failure of Instruction Hierarchies in Large Language Models](https://arxiv.org/abs/2502.15851)** (2025) `D4` `direct,indirect` `inference-layer`
  Empirically shows that instruction hierarchy training often fails under adversarial conditions; motivates stronger defenses.
  *Venue: AAAI 2025*

- **[DRIFT: Dynamic Rule-Based Defense with Injection Isolation for Securing LLM Agents](https://arxiv.org/abs/2506.12104)** (2025) `D3,D5` `indirect,multi-agent` `inference-layer,system-arch`
  Dynamic rule-based defense that isolates injected instructions from legitimate agent instructions at runtime.

- **[IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2508.15310)** (2025) `D5,D3` `indirect` `system-arch`
  Builds tool dependency graphs to detect and block indirect prompt injection in LLM agents.
  *Venue: EMNLP 2025*

- **[MiniScope: A Least Privilege Framework for Authorizing Tool Calling Agents](https://arxiv.org/abs/2512.11147)** (2025) `D5` `indirect,multi-agent` `system-arch`
  Least-privilege framework that restricts LLM agent tool permissions to the minimum required for each task.

- **[Sentinel: SOTA model to protect against prompt injections](https://arxiv.org/abs/2506.05446)** (2025) `D2` `direct,indirect` `input-layer`
  State-of-the-art prompt injection detection model with strong performance across injection types.

- **[Privacy-Preserving Prompt Injection Detection for LLMs Using Federated Learning and Embedding-Based NLP Classification](https://arxiv.org/abs/2511.12295)** (2025) `D2` `direct,indirect` `input-layer`
  Privacy-preserving prompt injection detection using federated learning to protect sensitive data during classification.

- **[A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks](https://arxiv.org/abs/2509.14285)** (2025) `D3,D6` `direct,indirect` `inference-layer`
  Multi-agent pipeline where specialized LLMs collaboratively detect and neutralize prompt injection attacks.

- **[TraceAegis: Securing LLM-Based Agents via Hierarchical and Behavioral Anomaly Detection](https://arxiv.org/abs/2510.11203)** (2025) `D3,D2` `indirect,multi-agent` `inference-layer`
  Detects prompt injection by monitoring behavioral anomalies and execution traces in LLM agent systems.

- **[CAPTURE: Context-Aware Prompt Injection Testing and Robustness Enhancement](https://arxiv.org/abs/2505.12368)** (2025) `D2,D4` `direct,indirect` `input-layer`
  Context-aware framework for testing and enhancing prompt injection robustness in guardrail models.

- **[RTBAS: Defending LLM Agents Against Prompt Injection and Privacy Leakage](https://arxiv.org/abs/2510.19207)** (2025) `D1,D3` `indirect,multi-agent` `input-layer,output-layer`
  Defends LLM agents against prompt injection and privacy leakage via input/output control.

- **[To Protect the LLM Agent Against the Prompt Injection Attack with Polymorphic Prompt](https://arxiv.org/abs/2506.05739)** (2025) `D1,D4` `indirect` `input-layer`
  Uses polymorphic prompt transformations to make injection attacks harder to craft.

- **[DataSentinel: A Game-Theoretic Detection of Prompt Injection Attacks](https://arxiv.org/abs/2504.11358)** (2025) `D2` `indirect` `input-layer`
  Game-theoretic framework for robust prompt injection detection accounting for adaptive adversaries.

- **[UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models](https://arxiv.org/abs/2502.13141)** (2025) `D2` `direct,indirect` `input-layer`
  Unified detection framework covering prompt injection, backdoor, and adversarial attacks.

- **[Detecting Prompt Injection Attacks Against Application Using Classifiers](https://arxiv.org/abs/2512.12583)** (2025) `D2` `direct,indirect` `input-layer`
  Curates augmented prompt injection dataset and evaluates classifier-based detection approaches.

- **[GuardReasoner: Towards Reasoning-based LLM Safeguards](https://arxiv.org/abs/2501.18492)** (2025) `D3` `direct` `input-layer,output-layer`
  Incorporates chain-of-thought reasoning into LLM safety guards for better explainability.

- **[Adaptive Multi-Layer Framework for Detecting and Mitigating Prompt Injection Attacks in Large Language Models](https://arxiv.org/abs/2504.11358)** (2025) `D2,D3` `direct,indirect` `input-layer,inference-layer,output-layer`
  Multi-layer adaptive framework combining detection and guardrails at multiple pipeline stages.

- **[SecAlign: Defending Against Prompt Injection with Preference Optimization](https://arxiv.org/abs/2410.05451)** (2025) `D4` `direct,indirect` `inference-layer`
  Uses preference optimization (DPO) to train LLMs to ignore injected instructions.
  *Authors: Sizhe Chen, Arman Zharmagambetov, Saeed Mahloujifar, Kamalika Chaudhuri, David Wagner*

- **[Stronger Enforcement of Instruction Hierarchy via Augmented Intermediate Representations](https://arxiv.org/abs/2505.18907)** (2025) `D4` `direct,indirect` `inference-layer`
  Strengthens instruction hierarchy by modifying intermediate representations to enforce priority.

- **[May I have your Attention? Breaking Fine-Tuning based Prompt Injection Defenses using Architecture-Aware Attacks](https://arxiv.org/abs/2507.07417)** (2025) `D4` `direct,indirect` `inference-layer`
  Demonstrates architecture-aware attacks that bypass fine-tuning-based defenses; informs robustness requirements.

- **[CaMeL: Defeating Prompt Injections by Isolating LLM Access to Trusted Data](https://arxiv.org/abs/2505.23643)** (2025) `D5` `indirect,multi-agent` `system-arch`
  Dual-LLM architecture where a reader processes untrusted content and an executor runs capability-restricted plans.
  *Authors: Edoardo Debenedetti, Ilia Shumailov, Tianxiang Fan, Nicholas Carlini, Florian Tramer*

- **[ACE: A Security Architecture for LLM-Integrated App Systems](https://arxiv.org/abs/2504.20984)** (2025) `D5` `indirect,multi-agent` `system-arch`
  Capability-based security architecture for LLM-integrated application systems.

- **[ceLLMate: Sandboxing Browser AI Agents](https://arxiv.org/abs/2512.12594)** (2025) `D5` `indirect,computer-use` `system-arch`
  OS/browser sandboxing for AI agents to limit blast radius of successful injections.

- **[Securing AI Agents with Information-Flow Control](https://arxiv.org/abs/2505.23643)** (2025) `D5` `indirect,multi-agent` `system-arch`
  Applies IFC and taint tracking to AI agents to prevent injected data from affecting trusted operations.

- **[MELON: Indirect Prompt Injection Defense via Masked Re-execution and Tool Comparison](https://arxiv.org/abs/2502.05174)** (2025) `D6` `indirect` `inference-layer`
  Re-executes tasks with masked tool outputs and detects injections by comparing execution traces.

### 2024

- **[Attention Tracker: Detecting Prompt Injection Attacks in LLMs](https://arxiv.org/abs/2411.00348)** (2024) `D2` `direct,indirect` `inference-layer`
  Uses attention pattern analysis to detect prompt injection attacks in LLMs.
  *Venue: NAACL 2025*

- **[Instructional Segment Embedding: Improving LLM Safety with Instruction Hierarchy](https://arxiv.org/abs/2410.09102)** (2024) `D4,D5` `direct,indirect` `inference-layer`
  Adds dedicated segment embeddings to encode instruction privilege levels, improving LLM safety without fine-tuning.
  *Venue: ICLR 2025*

- **[Palisade - Prompt Injection Detection Framework](https://arxiv.org/abs/2410.21146)** (2024) `D2,D3` `direct,indirect` `input-layer`
  Multi-model framework combining classifiers and LLM-based reasoning for prompt injection detection.

- **[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352)** (2024) `D1,D4` `indirect,multi-agent` `system-arch`
  Dynamic benchmark for evaluating prompt injection attacks and defenses in LLM agent pipelines.
  *Authors: Edoardo Debenedetti, Jie Zhang, Mislav Balunovic, Luca Beurer-Kellner, Marc Fischer, Florian Tramer — NeurIPS 2024*

- **[Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644)** (2024) `D1,D3` `direct,indirect,multi-agent` `system-arch`
  Comprehensive benchmark formalizing attack and defense space for LLM-based agents.

- **[StruQ: Defending Against Prompt Injection with Structured Queries](https://arxiv.org/abs/2402.06363)** (2024) `D1` `direct,indirect` `input-layer`
  Separates instructions and data using a structured format so the LLM can distinguish them syntactically.
  *Authors: Sizhe Chen, Julien Piet, Chawin Sitawarin, David Wagner — USENIX Security 2025*

- **[Defending Against Indirect Prompt Injection Attacks With Spotlighting](https://arxiv.org/abs/2403.14720)** (2024) `D1` `indirect,rag` `input-layer`
  Marks untrusted data segments with distinctive tokens so the model knows what is trusted instruction vs. untrusted content.
  *Authors: Keegan Hines, Gary Lopez, Matthew Hall, Federico Zarfati, Yonatan Zunger, Emre Kiciman*

- **[Signed-Prompt: A New Approach to Prevent Prompt Injection Attacks Against LLM-Integrated Applications](https://arxiv.org/abs/2401.07612)** (2024) `D1` `direct,indirect` `input-layer`
  Cryptographically signs trusted instructions to allow models to distinguish them from injected content.

- **[Defending LLMs against Jailbreaking Attacks via Backtranslation](https://arxiv.org/abs/2402.16459)** (2024) `D1` `direct` `input-layer`
  Paraphrases inputs via backtranslation to neutralize adversarial prompt structure.

- **[GradSafe: Detecting Unsafe Prompts for LLMs via Safety-Critical Gradient Analysis](https://arxiv.org/abs/2402.13494)** (2024) `D2` `direct` `inference-layer`
  Detects unsafe prompts by analyzing gradients of safety-critical tokens.

- **[InjecGuard: Benchmarking and Mitigating Over-defense in Prompt Injection Guardrail Models](https://arxiv.org/abs/2410.22770)** (2024) `D2` `direct,indirect` `input-layer`
  Addresses false positive problem in injection detectors; introduces benchmark and mitigation.

- **[Building Guardrails for Large Language Models](https://arxiv.org/abs/2402.01822)** (2024) `D3` `direct,indirect` `input-layer,output-layer`
  Survey and framework for designing comprehensive guardrail systems for LLMs.

- **[The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2412.16682)** (2024) `D3` `indirect` `inference-layer`
  Enforces alignment between agent actions and the original user task to detect indirect injection.

- **[The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions](https://arxiv.org/abs/2404.13208)** (2024) `D4` `direct,indirect` `inference-layer`
  Trains LLMs to prioritize instructions by privilege level (system > user > tool output).
  *Authors: Eric Wallace, Kai Xiao, Reimar Leike, Liang Luo, Johannes Scharfenberg, Andrew Wan*

- **[Protecting Your LLMs with Information Bottleneck](https://arxiv.org/abs/2404.13968)** (2024) `D4` `direct` `inference-layer`
  Applies information bottleneck to LLM representations to remove adversarial information.

- **[Baseline Defenses for Adversarial Attacks Against Aligned Language Models](https://arxiv.org/abs/2309.00614)** (2024) `D1,D2,D4` `direct` `input-layer`
  Evaluates baseline defenses (detection, preprocessing, smoothing) against adversarial LLM attacks.

### 2023 and Earlier

- **[Benchmarking and Defending Against Indirect Prompt Injection Attacks on Large Language Models](https://arxiv.org/abs/2312.14197)** (2023) `D1,D3` `indirect` `input-layer`
  Introduces benchmark for indirect prompt injection and evaluates defense strategies including input filtering and guardrails.

- **[Detecting Language Model Attacks with Perplexity](https://arxiv.org/abs/2308.14132)** (2023) `D2` `direct` `input-layer`
  Uses perplexity scores to detect adversarial prompts and jailbreak attempts.

- **[Token-Level Adversarial Prompt Detection Based on Perplexity Measures and Contextual Information](https://arxiv.org/abs/2311.11509)** (2023) `D2` `direct` `input-layer`
  Token-level perplexity analysis for fine-grained adversarial prompt detection.

- **[JailGuard: A Universal Detection Framework for LLM Prompt-based Attacks](https://arxiv.org/abs/2312.10766)** (2023) `D2` `direct` `input-layer`
  Universal detection framework using input mutation to identify prompt-based attacks.

- **[NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails](https://arxiv.org/abs/2310.10501)** (2023) `D3` `direct` `input-layer,output-layer`
  Open-source toolkit for adding programmable safety guardrails to LLM applications.

- **[Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations](https://arxiv.org/abs/2312.06674)** (2023) `D3` `direct` `input-layer,output-layer`
  LLM-based input-output safety classifier for human-AI conversations.
  *Authors: Hakan Inan, Kartikeya Upasani, Jianfeng Chi*

- **[LLM Self Defense: By Self Examination, LLMs Know They Are Being Tricked](https://arxiv.org/abs/2308.07308)** (2023) `D3` `direct` `inference-layer`
  LLMs can detect jailbreaks by examining their own context for signs of manipulation.

- **[Robust Safety Classifier for Large Language Models: Adversarial Prompt Shield](https://arxiv.org/abs/2311.00172)** (2023) `D3` `direct` `input-layer`
  Robust safety classifier designed to withstand adversarial prompt attacks.

- **[Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://arxiv.org/abs/2308.07308)** (2023) `D3` `direct` `input-layer`
  Adds self-reminder instructions to system prompt to help the model resist jailbreaks.
  *Venue: Nature Machine Intelligence*

- **[Jatmo: Prompt Injection Defense by Task-Specific Finetuning](https://arxiv.org/abs/2312.17673)** (2023) `D4` `direct,indirect` `inference-layer`
  Fine-tunes task-specific models that treat external data as inert, ignoring injected instructions.
  *Authors: Julien Piet, Meder Mirza, Lukas Biewald, Mark Tygert, Dawn Song — ESORICS 2024*

- **[SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks](https://arxiv.org/abs/2310.03684)** (2023) `D4` `direct` `input-layer`
  Applies randomized smoothing via input perturbation to defend against jailbreaking.

- **[PromptBench: Towards Evaluating the Robustness of Large Language Models on Adversarial Prompts](https://arxiv.org/abs/2306.04528)** (2023) `D6` `direct` `inference-layer`
  Benchmark and ensemble-based defense evaluation for adversarial prompt robustness.

## Papers by Defense Type

### D1: Input Filtering & Pre-processing

*Prevent injection by marking/separating trusted and untrusted data before LLM processing*

- **[Benchmarking and Defending Against Indirect Prompt Injection Attacks on Large Language Models](https://arxiv.org/abs/2312.14197)** (2023) `D1,D3` `indirect` `input-layer`
  Introduces benchmark for indirect prompt injection and evaluates defense strategies including input filtering and guardrails.

- **[StruQ: Defending Against Prompt Injection with Structured Queries](https://arxiv.org/abs/2402.06363)** (2024) `D1` `direct,indirect` `input-layer`
  Separates instructions and data using a structured format so the LLM can distinguish them syntactically.
  *Authors: Sizhe Chen, Julien Piet, Chawin Sitawarin, David Wagner — USENIX Security 2025*

- **[Defending Against Indirect Prompt Injection Attacks With Spotlighting](https://arxiv.org/abs/2403.14720)** (2024) `D1` `indirect,rag` `input-layer`
  Marks untrusted data segments with distinctive tokens so the model knows what is trusted instruction vs. untrusted content.
  *Authors: Keegan Hines, Gary Lopez, Matthew Hall, Federico Zarfati, Yonatan Zunger, Emre Kiciman*

- **[Signed-Prompt: A New Approach to Prevent Prompt Injection Attacks Against LLM-Integrated Applications](https://arxiv.org/abs/2401.07612)** (2024) `D1` `direct,indirect` `input-layer`
  Cryptographically signs trusted instructions to allow models to distinguish them from injected content.

- **[Defending Against Prompt Injection with DataFilter](https://arxiv.org/abs/2510.19207)** (2025) `D1` `indirect,rag` `input-layer`
  Filters retrieved content before injection into context to remove adversarial instructions.

- **[RTBAS: Defending LLM Agents Against Prompt Injection and Privacy Leakage](https://arxiv.org/abs/2510.19207)** (2025) `D1,D3` `indirect,multi-agent` `input-layer,output-layer`
  Defends LLM agents against prompt injection and privacy leakage via input/output control.

- **[Real User Instruction: Black-Box Instruction Authentication Middleware Against Indirect Prompt Injection](https://arxiv.org/abs/2601.12359)** (2026) `D1` `indirect` `input-layer`
  Middleware that authenticates whether instructions originate from real users vs. injected sources.
  *Venue: Preprints.org*

- **[Defending LLMs against Jailbreaking Attacks via Backtranslation](https://arxiv.org/abs/2402.16459)** (2024) `D1` `direct` `input-layer`
  Paraphrases inputs via backtranslation to neutralize adversarial prompt structure.

- **[To Protect the LLM Agent Against the Prompt Injection Attack with Polymorphic Prompt](https://arxiv.org/abs/2506.05739)** (2025) `D1,D4` `indirect` `input-layer`
  Uses polymorphic prompt transformations to make injection attacks harder to craft.

- **[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352)** (2024) `D1,D4` `indirect,multi-agent` `system-arch`
  Dynamic benchmark for evaluating prompt injection attacks and defenses in LLM agent pipelines.
  *Authors: Edoardo Debenedetti, Jie Zhang, Mislav Balunovic, Luca Beurer-Kellner, Marc Fischer, Florian Tramer — NeurIPS 2024*

- **[Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644)** (2024) `D1,D3` `direct,indirect,multi-agent` `system-arch`
  Comprehensive benchmark formalizing attack and defense space for LLM-based agents.

- **[Baseline Defenses for Adversarial Attacks Against Aligned Language Models](https://arxiv.org/abs/2309.00614)** (2024) `D1,D2,D4` `direct` `input-layer`
  Evaluates baseline defenses (detection, preprocessing, smoothing) against adversarial LLM attacks.

- **[The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis](https://arxiv.org/abs/2602.10453)** (2026) `D1,D3,D5` `direct,indirect,multi-agent` `system-arch`
  Comprehensive taxonomy and analysis of prompt injection threats in agentic LLM settings.

- **[The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey](https://arxiv.org/abs/2603.11088)** (2026) `D1,D2,D3,D4,D5,D6` `direct,indirect,multi-agent,rag,computer-use` `system-arch`
  Comprehensive survey of attacks and defenses in agentic AI systems.

### D2: Detection

*Monitor and flag suspicious prompts or execution patterns*

- **[Attention Tracker: Detecting Prompt Injection Attacks in LLMs](https://arxiv.org/abs/2411.00348)** (2024) `D2` `direct,indirect` `inference-layer`
  Uses attention pattern analysis to detect prompt injection attacks in LLMs.
  *Venue: NAACL 2025*

- **[Palisade - Prompt Injection Detection Framework](https://arxiv.org/abs/2410.21146)** (2024) `D2,D3` `direct,indirect` `input-layer`
  Multi-model framework combining classifiers and LLM-based reasoning for prompt injection detection.

- **[Sentinel: SOTA model to protect against prompt injections](https://arxiv.org/abs/2506.05446)** (2025) `D2` `direct,indirect` `input-layer`
  State-of-the-art prompt injection detection model with strong performance across injection types.

- **[Privacy-Preserving Prompt Injection Detection for LLMs Using Federated Learning and Embedding-Based NLP Classification](https://arxiv.org/abs/2511.12295)** (2025) `D2` `direct,indirect` `input-layer`
  Privacy-preserving prompt injection detection using federated learning to protect sensitive data during classification.

- **[TraceAegis: Securing LLM-Based Agents via Hierarchical and Behavioral Anomaly Detection](https://arxiv.org/abs/2510.11203)** (2025) `D3,D2` `indirect,multi-agent` `inference-layer`
  Detects prompt injection by monitoring behavioral anomalies and execution traces in LLM agent systems.

- **[CAPTURE: Context-Aware Prompt Injection Testing and Robustness Enhancement](https://arxiv.org/abs/2505.12368)** (2025) `D2,D4` `direct,indirect` `input-layer`
  Context-aware framework for testing and enhancing prompt injection robustness in guardrail models.

- **[Detecting Language Model Attacks with Perplexity](https://arxiv.org/abs/2308.14132)** (2023) `D2` `direct` `input-layer`
  Uses perplexity scores to detect adversarial prompts and jailbreak attempts.

- **[Token-Level Adversarial Prompt Detection Based on Perplexity Measures and Contextual Information](https://arxiv.org/abs/2311.11509)** (2023) `D2` `direct` `input-layer`
  Token-level perplexity analysis for fine-grained adversarial prompt detection.

- **[GradSafe: Detecting Unsafe Prompts for LLMs via Safety-Critical Gradient Analysis](https://arxiv.org/abs/2402.13494)** (2024) `D2` `direct` `inference-layer`
  Detects unsafe prompts by analyzing gradients of safety-critical tokens.

- **[InjecGuard: Benchmarking and Mitigating Over-defense in Prompt Injection Guardrail Models](https://arxiv.org/abs/2410.22770)** (2024) `D2` `direct,indirect` `input-layer`
  Addresses false positive problem in injection detectors; introduces benchmark and mitigation.

- **[JailGuard: A Universal Detection Framework for LLM Prompt-based Attacks](https://arxiv.org/abs/2312.10766)** (2023) `D2` `direct` `input-layer`
  Universal detection framework using input mutation to identify prompt-based attacks.

- **[DataSentinel: A Game-Theoretic Detection of Prompt Injection Attacks](https://arxiv.org/abs/2504.11358)** (2025) `D2` `indirect` `input-layer`
  Game-theoretic framework for robust prompt injection detection accounting for adaptive adversaries.

- **[UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models](https://arxiv.org/abs/2502.13141)** (2025) `D2` `direct,indirect` `input-layer`
  Unified detection framework covering prompt injection, backdoor, and adversarial attacks.

- **[Detecting Prompt Injection Attacks Against Application Using Classifiers](https://arxiv.org/abs/2512.12583)** (2025) `D2` `direct,indirect` `input-layer`
  Curates augmented prompt injection dataset and evaluates classifier-based detection approaches.

- **[Zero-Shot Embedding Drift Detection: A Lightweight Defense Against Prompt Injections in LLMs](https://arxiv.org/abs/2601.12359)** (2026) `D2` `indirect` `inference-layer`
  Detects prompt injections by measuring semantic drift in embeddings without task-specific training.

- **[Adaptive Multi-Layer Framework for Detecting and Mitigating Prompt Injection Attacks in Large Language Models](https://arxiv.org/abs/2504.11358)** (2025) `D2,D3` `direct,indirect` `input-layer,inference-layer,output-layer`
  Multi-layer adaptive framework combining detection and guardrails at multiple pipeline stages.

- **[Baseline Defenses for Adversarial Attacks Against Aligned Language Models](https://arxiv.org/abs/2309.00614)** (2024) `D1,D2,D4` `direct` `input-layer`
  Evaluates baseline defenses (detection, preprocessing, smoothing) against adversarial LLM attacks.

- **[The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey](https://arxiv.org/abs/2603.11088)** (2026) `D1,D2,D3,D4,D5,D6` `direct,indirect,multi-agent,rag,computer-use` `system-arch`
  Comprehensive survey of attacks and defenses in agentic AI systems.

### D3: Guardrails & Oversight

*Programmatic and LLM-based safeguards on model inputs/outputs*

- **[Benchmarking and Defending Against Indirect Prompt Injection Attacks on Large Language Models](https://arxiv.org/abs/2312.14197)** (2023) `D1,D3` `indirect` `input-layer`
  Introduces benchmark for indirect prompt injection and evaluates defense strategies including input filtering and guardrails.

- **[Palisade - Prompt Injection Detection Framework](https://arxiv.org/abs/2410.21146)** (2024) `D2,D3` `direct,indirect` `input-layer`
  Multi-model framework combining classifiers and LLM-based reasoning for prompt injection detection.

- **[DRIFT: Dynamic Rule-Based Defense with Injection Isolation for Securing LLM Agents](https://arxiv.org/abs/2506.12104)** (2025) `D3,D5` `indirect,multi-agent` `inference-layer,system-arch`
  Dynamic rule-based defense that isolates injected instructions from legitimate agent instructions at runtime.

- **[IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2508.15310)** (2025) `D5,D3` `indirect` `system-arch`
  Builds tool dependency graphs to detect and block indirect prompt injection in LLM agents.
  *Venue: EMNLP 2025*

- **[A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks](https://arxiv.org/abs/2509.14285)** (2025) `D3,D6` `direct,indirect` `inference-layer`
  Multi-agent pipeline where specialized LLMs collaboratively detect and neutralize prompt injection attacks.

- **[TraceAegis: Securing LLM-Based Agents via Hierarchical and Behavioral Anomaly Detection](https://arxiv.org/abs/2510.11203)** (2025) `D3,D2` `indirect,multi-agent` `inference-layer`
  Detects prompt injection by monitoring behavioral anomalies and execution traces in LLM agent systems.

- **[AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification](https://arxiv.org/abs/2602.22724)** (2026) `D5,D3` `indirect,multi-agent` `system-arch`
  Combines temporal causal diagnostics and context purification to detect and mitigate indirect prompt injections.

- **[NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails](https://arxiv.org/abs/2310.10501)** (2023) `D3` `direct` `input-layer,output-layer`
  Open-source toolkit for adding programmable safety guardrails to LLM applications.

- **[Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations](https://arxiv.org/abs/2312.06674)** (2023) `D3` `direct` `input-layer,output-layer`
  LLM-based input-output safety classifier for human-AI conversations.
  *Authors: Hakan Inan, Kartikeya Upasani, Jianfeng Chi*

- **[Building Guardrails for Large Language Models](https://arxiv.org/abs/2402.01822)** (2024) `D3` `direct,indirect` `input-layer,output-layer`
  Survey and framework for designing comprehensive guardrail systems for LLMs.

- **[LLM Self Defense: By Self Examination, LLMs Know They Are Being Tricked](https://arxiv.org/abs/2308.07308)** (2023) `D3` `direct` `inference-layer`
  LLMs can detect jailbreaks by examining their own context for signs of manipulation.

- **[Robust Safety Classifier for Large Language Models: Adversarial Prompt Shield](https://arxiv.org/abs/2311.00172)** (2023) `D3` `direct` `input-layer`
  Robust safety classifier designed to withstand adversarial prompt attacks.

- **[Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://arxiv.org/abs/2308.07308)** (2023) `D3` `direct` `input-layer`
  Adds self-reminder instructions to system prompt to help the model resist jailbreaks.
  *Venue: Nature Machine Intelligence*

- **[GuardReasoner: Towards Reasoning-based LLM Safeguards](https://arxiv.org/abs/2501.18492)** (2025) `D3` `direct` `input-layer,output-layer`
  Incorporates chain-of-thought reasoning into LLM safety guards for better explainability.

- **[The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2412.16682)** (2024) `D3` `indirect` `inference-layer`
  Enforces alignment between agent actions and the original user task to detect indirect injection.

- **[RTBAS: Defending LLM Agents Against Prompt Injection and Privacy Leakage](https://arxiv.org/abs/2510.19207)** (2025) `D1,D3` `indirect,multi-agent` `input-layer,output-layer`
  Defends LLM agents against prompt injection and privacy leakage via input/output control.

- **[Recursive language models for jailbreak detection: a procedural defense for tool-augmented agents](https://arxiv.org/abs/2602.16520)** (2026) `D3` `indirect,multi-agent` `inference-layer`
  Hierarchical LLM calls for multi-level jailbreak detection in tool-augmented agent systems.

- **[Adaptive Multi-Layer Framework for Detecting and Mitigating Prompt Injection Attacks in Large Language Models](https://arxiv.org/abs/2504.11358)** (2025) `D2,D3` `direct,indirect` `input-layer,inference-layer,output-layer`
  Multi-layer adaptive framework combining detection and guardrails at multiple pipeline stages.

- **[Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644)** (2024) `D1,D3` `direct,indirect,multi-agent` `system-arch`
  Comprehensive benchmark formalizing attack and defense space for LLM-based agents.

- **[The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis](https://arxiv.org/abs/2602.10453)** (2026) `D1,D3,D5` `direct,indirect,multi-agent` `system-arch`
  Comprehensive taxonomy and analysis of prompt injection threats in agentic LLM settings.

- **[The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey](https://arxiv.org/abs/2603.11088)** (2026) `D1,D2,D3,D4,D5,D6` `direct,indirect,multi-agent,rag,computer-use` `system-arch`
  Comprehensive survey of attacks and defenses in agentic AI systems.

### D4: Training-based Robustness

*Fine-tune or preference-optimize models to resist injection*

- **[Instructional Segment Embedding: Improving LLM Safety with Instruction Hierarchy](https://arxiv.org/abs/2410.09102)** (2024) `D4,D5` `direct,indirect` `inference-layer`
  Adds dedicated segment embeddings to encode instruction privilege levels, improving LLM safety without fine-tuning.
  *Venue: ICLR 2025*

- **[Control Illusion: The Failure of Instruction Hierarchies in Large Language Models](https://arxiv.org/abs/2502.15851)** (2025) `D4` `direct,indirect` `inference-layer`
  Empirically shows that instruction hierarchy training often fails under adversarial conditions; motivates stronger defenses.
  *Venue: AAAI 2025*

- **[CAPTURE: Context-Aware Prompt Injection Testing and Robustness Enhancement](https://arxiv.org/abs/2505.12368)** (2025) `D2,D4` `direct,indirect` `input-layer`
  Context-aware framework for testing and enhancing prompt injection robustness in guardrail models.

- **[HIPO: Instruction Hierarchy via Constrained Reinforcement Learning](https://arxiv.org/abs/2603.16152)** (2026) `D4` `direct,indirect` `inference-layer`
  Uses constrained RL to train LLMs to follow instruction hierarchies robustly under adversarial conditions.

- **[IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs](https://arxiv.org/abs/2603.10521)** (2026) `D4` `direct,indirect` `inference-layer`
  Training dataset specifically designed to improve instruction hierarchy compliance in frontier LLMs.

- **[Jatmo: Prompt Injection Defense by Task-Specific Finetuning](https://arxiv.org/abs/2312.17673)** (2023) `D4` `direct,indirect` `inference-layer`
  Fine-tunes task-specific models that treat external data as inert, ignoring injected instructions.
  *Authors: Julien Piet, Meder Mirza, Lukas Biewald, Mark Tygert, Dawn Song — ESORICS 2024*

- **[SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks](https://arxiv.org/abs/2310.03684)** (2023) `D4` `direct` `input-layer`
  Applies randomized smoothing via input perturbation to defend against jailbreaking.

- **[The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions](https://arxiv.org/abs/2404.13208)** (2024) `D4` `direct,indirect` `inference-layer`
  Trains LLMs to prioritize instructions by privilege level (system > user > tool output).
  *Authors: Eric Wallace, Kai Xiao, Reimar Leike, Liang Luo, Johannes Scharfenberg, Andrew Wan*

- **[Protecting Your LLMs with Information Bottleneck](https://arxiv.org/abs/2404.13968)** (2024) `D4` `direct` `inference-layer`
  Applies information bottleneck to LLM representations to remove adversarial information.

- **[SecAlign: Defending Against Prompt Injection with Preference Optimization](https://arxiv.org/abs/2410.05451)** (2025) `D4` `direct,indirect` `inference-layer`
  Uses preference optimization (DPO) to train LLMs to ignore injected instructions.
  *Authors: Sizhe Chen, Arman Zharmagambetov, Saeed Mahloujifar, Kamalika Chaudhuri, David Wagner*

- **[Stronger Enforcement of Instruction Hierarchy via Augmented Intermediate Representations](https://arxiv.org/abs/2505.18907)** (2025) `D4` `direct,indirect` `inference-layer`
  Strengthens instruction hierarchy by modifying intermediate representations to enforce priority.

- **[May I have your Attention? Breaking Fine-Tuning based Prompt Injection Defenses using Architecture-Aware Attacks](https://arxiv.org/abs/2507.07417)** (2025) `D4` `direct,indirect` `inference-layer`
  Demonstrates architecture-aware attacks that bypass fine-tuning-based defenses; informs robustness requirements.

- **[To Protect the LLM Agent Against the Prompt Injection Attack with Polymorphic Prompt](https://arxiv.org/abs/2506.05739)** (2025) `D1,D4` `indirect` `input-layer`
  Uses polymorphic prompt transformations to make injection attacks harder to craft.

- **[The Autonomy Tax: Defense Training Breaks LLM Agents](https://arxiv.org/abs/2603.19423)** (2026) `D4` `indirect` `inference-layer`
  Studies capability-safety tradeoff showing defense training can degrade agent task performance.

- **[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352)** (2024) `D1,D4` `indirect,multi-agent` `system-arch`
  Dynamic benchmark for evaluating prompt injection attacks and defenses in LLM agent pipelines.
  *Authors: Edoardo Debenedetti, Jie Zhang, Mislav Balunovic, Luca Beurer-Kellner, Marc Fischer, Florian Tramer — NeurIPS 2024*

- **[Baseline Defenses for Adversarial Attacks Against Aligned Language Models](https://arxiv.org/abs/2309.00614)** (2024) `D1,D2,D4` `direct` `input-layer`
  Evaluates baseline defenses (detection, preprocessing, smoothing) against adversarial LLM attacks.

- **[The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey](https://arxiv.org/abs/2603.11088)** (2026) `D1,D2,D3,D4,D5,D6` `direct,indirect,multi-agent,rag,computer-use` `system-arch`
  Comprehensive survey of attacks and defenses in agentic AI systems.

### D5: Architecture & Privilege Isolation

*Isolate untrusted data via multi-agent or capability-based designs*

- **[Instructional Segment Embedding: Improving LLM Safety with Instruction Hierarchy](https://arxiv.org/abs/2410.09102)** (2024) `D4,D5` `direct,indirect` `inference-layer`
  Adds dedicated segment embeddings to encode instruction privilege levels, improving LLM safety without fine-tuning.
  *Venue: ICLR 2025*

- **[DRIFT: Dynamic Rule-Based Defense with Injection Isolation for Securing LLM Agents](https://arxiv.org/abs/2506.12104)** (2025) `D3,D5` `indirect,multi-agent` `inference-layer,system-arch`
  Dynamic rule-based defense that isolates injected instructions from legitimate agent instructions at runtime.

- **[IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2508.15310)** (2025) `D5,D3` `indirect` `system-arch`
  Builds tool dependency graphs to detect and block indirect prompt injection in LLM agents.
  *Venue: EMNLP 2025*

- **[MiniScope: A Least Privilege Framework for Authorizing Tool Calling Agents](https://arxiv.org/abs/2512.11147)** (2025) `D5` `indirect,multi-agent` `system-arch`
  Least-privilege framework that restricts LLM agent tool permissions to the minimum required for each task.

- **[AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification](https://arxiv.org/abs/2602.22724)** (2026) `D5,D3` `indirect,multi-agent` `system-arch`
  Combines temporal causal diagnostics and context purification to detect and mitigate indirect prompt injections.

- **[RedVisor: Reasoning-Aware Prompt Injection Defense via Zero-Copy KV Cache Reuse](https://arxiv.org/abs/2602.01795)** (2026) `D5,D6` `indirect` `inference-layer,system-arch`
  Defends against prompt injection by isolating trusted reasoning from untrusted context via KV cache separation.

- **[CaMeL: Defeating Prompt Injections by Isolating LLM Access to Trusted Data](https://arxiv.org/abs/2505.23643)** (2025) `D5` `indirect,multi-agent` `system-arch`
  Dual-LLM architecture where a reader processes untrusted content and an executor runs capability-restricted plans.
  *Authors: Edoardo Debenedetti, Ilia Shumailov, Tianxiang Fan, Nicholas Carlini, Florian Tramer*

- **[ACE: A Security Architecture for LLM-Integrated App Systems](https://arxiv.org/abs/2504.20984)** (2025) `D5` `indirect,multi-agent` `system-arch`
  Capability-based security architecture for LLM-integrated application systems.

- **[ceLLMate: Sandboxing Browser AI Agents](https://arxiv.org/abs/2512.12594)** (2025) `D5` `indirect,computer-use` `system-arch`
  OS/browser sandboxing for AI agents to limit blast radius of successful injections.

- **[Securing AI Agents with Information-Flow Control](https://arxiv.org/abs/2505.23643)** (2025) `D5` `indirect,multi-agent` `system-arch`
  Applies IFC and taint tracking to AI agents to prevent injected data from affecting trusted operations.

- **[Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats](https://arxiv.org/abs/2603.11619)** (2026) `D5` `indirect,multi-agent` `system-arch`
  Security analysis and architectural mitigations for autonomous LLM agent threat landscape.

- **[A Framework for Formalizing LLM Agent Security](https://arxiv.org/abs/2603.19469)** (2026) `D5` `indirect,multi-agent` `system-arch`
  Formal framework for reasoning about security properties of LLM agent systems.

- **[From Thinker to Society: Security in Hierarchical Autonomy Evolution of AI Agents](https://arxiv.org/abs/2603.07496)** (2026) `D5` `multi-agent` `system-arch`
  Security framework for hierarchical multi-agent systems across autonomy levels.

- **[The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis](https://arxiv.org/abs/2602.10453)** (2026) `D1,D3,D5` `direct,indirect,multi-agent` `system-arch`
  Comprehensive taxonomy and analysis of prompt injection threats in agentic LLM settings.

- **[The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey](https://arxiv.org/abs/2603.11088)** (2026) `D1,D2,D3,D4,D5,D6` `direct,indirect,multi-agent,rag,computer-use` `system-arch`
  Comprehensive survey of attacks and defenses in agentic AI systems.

### D6: Runtime Verification & Ensemble

*Verify execution correctness through re-execution or ensemble consensus*

- **[A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks](https://arxiv.org/abs/2509.14285)** (2025) `D3,D6` `direct,indirect` `inference-layer`
  Multi-agent pipeline where specialized LLMs collaboratively detect and neutralize prompt injection attacks.

- **[RedVisor: Reasoning-Aware Prompt Injection Defense via Zero-Copy KV Cache Reuse](https://arxiv.org/abs/2602.01795)** (2026) `D5,D6` `indirect` `inference-layer,system-arch`
  Defends against prompt injection by isolating trusted reasoning from untrusted context via KV cache separation.

- **[MELON: Indirect Prompt Injection Defense via Masked Re-execution and Tool Comparison](https://arxiv.org/abs/2502.05174)** (2025) `D6` `indirect` `inference-layer`
  Re-executes tasks with masked tool outputs and detects injections by comparing execution traces.

- **[PromptBench: Towards Evaluating the Robustness of Large Language Models on Adversarial Prompts](https://arxiv.org/abs/2306.04528)** (2023) `D6` `direct` `inference-layer`
  Benchmark and ensemble-based defense evaluation for adversarial prompt robustness.

- **[The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey](https://arxiv.org/abs/2603.11088)** (2026) `D1,D2,D3,D4,D5,D6` `direct,indirect,multi-agent,rag,computer-use` `system-arch`
  Comprehensive survey of attacks and defenses in agentic AI systems.

## Benchmarks & Evaluation

- **[AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352)** (2024)
  Dynamic benchmark for evaluating prompt injection attacks and defenses in LLM agent pipelines.
  *Authors: Edoardo Debenedetti, Jie Zhang, Mislav Balunovic, Luca Beurer-Kellner, Marc Fischer, Florian Tramer — NeurIPS 2024*

- **[Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://arxiv.org/abs/2410.02644)** (2024)
  Comprehensive benchmark formalizing attack and defense space for LLM-based agents.

- **[InjecGuard: Benchmarking and Mitigating Over-defense in Prompt Injection Guardrail Models](https://arxiv.org/abs/2410.22770)** (2024)
  Addresses false positive problem in injection detectors; introduces benchmark and mitigation.

- **[Detecting Prompt Injection Attacks Against Application Using Classifiers](https://arxiv.org/abs/2512.12583)** (2025)
  Curates augmented prompt injection dataset and evaluates classifier-based detection approaches.

- **[PromptBench: Towards Evaluating the Robustness of Large Language Models on Adversarial Prompts](https://arxiv.org/abs/2306.04528)** (2023)
  Benchmark and ensemble-based defense evaluation for adversarial prompt robustness.

- **[Baseline Defenses for Adversarial Attacks Against Aligned Language Models](https://arxiv.org/abs/2309.00614)** (2024)
  Evaluates baseline defenses (detection, preprocessing, smoothing) against adversarial LLM attacks.

## Surveys & Taxonomies

- **[Building Guardrails for Large Language Models](https://arxiv.org/abs/2402.01822)** (2024)
  Survey and framework for designing comprehensive guardrail systems for LLMs.

- **[The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis](https://arxiv.org/abs/2602.10453)** (2026)
  Comprehensive taxonomy and analysis of prompt injection threats in agentic LLM settings.

- **[The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey](https://arxiv.org/abs/2603.11088)** (2026)
  Comprehensive survey of attacks and defenses in agentic AI systems.

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to add new papers, suggest improvements, and maintain the quality of this collection.

---

*Last updated: 2026-04-08*
