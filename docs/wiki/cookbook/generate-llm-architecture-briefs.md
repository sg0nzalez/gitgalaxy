# How to Generate LLM-Optimized Architecture Briefs

Onboarding a new developer—or an AI coding agent—onto a massive, monolithic codebase takes weeks. If you simply dump raw source code into an LLM (like Claude or GPT-4), it will quickly blow out the context window and hallucinate architectural relationships because it lacks global graph visibility.

GitGalaxy solves this using the **LLM Recorder**. It condenses the entire repository's physical constraints, dependency graphs, historical Git churn, and structural risk into a single, highly-optimized Markdown brief (`_llm.md`). 

This brief acts as a "Rosetta Stone," allowing any standard LLM to instantly understand the ecosystem with the exact same mathematical context as a Principal Systems Architect.

## The AI Translation Layer

The LLM Recorder bridges the gap between the raw mathematical output of the GitGalaxy engines (PageRank, Shannon Entropy, Big-O depths) and natural language reasoning.

### 1. Execute the Scan
You can run the full GalaxyScope pipeline, or pass the `--llm-only` flag to exclusively generate the AI artifacts without rendering the 3D WebGPU payload.

```bash
galaxyscope /path/to/target_repository --llm-only
```

### 2. Feed the Brief to your AI
The engine outputs a `<repo>_galaxy_llm.md` file. Upload this file directly into ChatGPT, Claude, or your local autonomous agent framework (like SWE-agent). 

The brief strictly categorizes the codebase into actionable intelligence:

* **The 13-Point Risk Physics:** Summarizes the Min/Max/Mean of every risk vector (Cognitive Load, State Flux, Tech Debt) across the entire repository.
* **Architectural Choke Points:** Identifies "God Nodes" (highest 'Imported By' / Blast Radius) and "Orchestrators" (highest outbound imports / fragility).
* **The Hotspot Matrix:** Cross-references historical Git volatility (Churn) against high Cognitive Load to pinpoint the exact files causing the most developer friction.
* **Systemic Network Bottlenecks:** Uses N-Dimensional physics to flag catastrophic intersections, such as the **"House of Cards"** (files that are deeply embedded in the graph *and* possess extreme Error/Exception exposure).
* **Key Person Dependencies:** Flags massive, load-bearing files written almost entirely by a single developer (High Silo Risk / Bus Factor).

### 3. The Enforced System Prompt
To prevent the LLM from outputting sensationalized, useless jargon, GitGalaxy automatically injects a strict System Prompt at the bottom of the brief.

```markdown
## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon...
> 1. Information Flow & Purpose (The Executive Summary)
> 2. Notable Structures & Architecture
> 3. Security & Vulnerabilities
> 4. Outliers & Extremes
> 5. Recommended Next Steps (Refactoring for Stability)
```

By providing the AI with mathematically proven network topology rather than raw text, you guarantee deterministic, actionable refactoring advice.

> **Read the full technical specification:** [LLM Recorder](../02-14-llm-recorder.md)