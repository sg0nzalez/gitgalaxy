# The Dev Agent Firewall (AI Guardrails)

> **Regulating Autonomous AI Editors**
>
> The Dev Agent Firewall (`dev_agent_firewall.py`) evaluates the repository specifically to determine if it is safe to allow an autonomous AI agent (like Claude, Cursor, or Devin) to modify the code.
>
> While standard linters check for human errors, this firewall evaluates **Token Physics** and **Architectural Complexity** to anticipate where a Large Language Model is statistically likely to fail, hallucinate, or cause catastrophic cascading breakages.

## Token Physics & Agentic Constraints

The firewall scans the telemetry, risk vectors, and network metrics of every file in the ecosystem to assess its compatibility with standard LLM context windows and reasoning capabilities. It enforces four primary guardrails:

### 1. The Context Window Shredder (The Black Hole)
If a file has a massive token footprint (e.g., `token_mass > 8000`) AND terrible algorithmic complexity (e.g., $O(N^3)$ or worse), it is flagged as an `is_agentic_black_hole`. 
* **The Threat:** Feeding this file to an AI agent will completely shred its context window and reasoning capabilities, leading to severe logical omissions and "forgetfulness" during refactoring.

### 2. The HITL Mandate (Human-In-The-Loop)
The firewall cross-references the file's Network Graph topology against its local risk. If a file has a massive Blast Radius (Normalized PageRank > 1.0) and severe technical debt (cumulative risk vector > 200), it triggers the `requires_hitl` flag.
* **The Threat:** The file is too structurally critical and too fragile to trust to autonomous modification. An agent making a mistake here will shatter the entire application. A human must explicitly review any AI-generated changes.

### 3. The Hallucination Zone
Detects areas of the codebase relying heavily on metaprogramming, reflection, or dynamic dispatch (`heat_triggers > 2`) but lacking adequate documentation (`doc_density < 0.2`).
* **The Threat:** Because the code's behavior is determined dynamically at runtime and lacks human-readable explanations, static LLM analysis will fail. The AI is highly likely to hallucinate missing methods or incorrect data structures.

### 4. The Silent Mutation Risk
Flags files that possess high state volatility (`state_flux > 50`) and act as heavily relied-upon foundational producers (`in_degree > 5`), but have absolutely zero unit tests.
* **The Threat:** If an autonomous agent refactors this file and introduces a subtle state-mutation bug, there are no tests to catch it. The AI cannot verify its own fixes, leading to silent, cascading corruption across all downstream dependencies.

## Telemetry Injection

Once the firewall completes its evaluation, it compiles the triggered guardrails and specific warning messages into an `ai_guardrails` report. This payload is injected directly back into the star's central telemetry. 

This ensures that downstream output modules—specifically the LLM Recorder—can explicitly warn downstream AI agents about the physical constraints and dangers of the files they are attempting to edit.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

