# The LLM Recorder (AI Translation Layer)

> **The Bridge to Autonomous Agents**
>
> The LLM Recorder (`llm_recorder.py`) bridges the gap between GitGalaxy's raw mathematical physics and autonomous AI agents. Rather than forcing a Large Language Model to hallucinate meaning from thousands of lines of raw JSON, this phase translates the pipeline's telemetry into highly optimized, token-dense artifacts designed specifically for LLM context windows and Retrieval-Augmented Generation (RAG) systems.

## Reverse Dependency Resolution

Before generating outputs, the recorder performs a unified reverse-dependency map across the entire galaxy. It traces every `raw_import` back to its origin file to establish a bi-directional graph:

* **Structural Pillars (Blast Radius):** Files with the highest inbound connections ("Imported By"). Tells the AI that modifying this file carries a massive risk of cascading breakages.
* **Orchestrators (Fragility Index):** Files with the highest outbound connections ("Imports"). Tells the AI that this file is highly coupled and fragile to external API changes.

## The Token-Optimized Markdown Brief

The primary output is a dense, pre-engineered Markdown prompt (`_galaxy_llm.md`) that fits cleanly into standard context windows (like Claude 3.5 or GPT-4o). It structurally guides the AI's analysis using advanced contextual headers:

### 1. AI Threat Audit Billboard
Right at the top of the brief, the recorder injects the results from the XGBoost ML model. If the Structural Signatures match known malware, it explicitly flags the hostile files and their AI Confidence scores so the LLM agent knows it is operating in a compromised environment.

### 2. Hardcoded System Instructions & Lexicon
The brief injects strict Prompt Engineering. It explicitly commands the AI to "Measure Risk, Not Quality," enforcing a blameless, objective tone based on structural heuristics rather than subjective coding styles. It provides the LLM with the exact equations for the 18-point risk vector so it understands *how* the scores were calculated.

### 3. Macro-State & AI Topology
To give the LLM a 10,000-foot view of the repository, the recorder injects:
* **Network Topology:** Metrics like Modularity, Assortativity, and Cyclic Density.
* **Architectural Clusters:** The assigned Architectural Z-Scores to show how much the repository drifts from standard patterns.
* **AI & Machine Learning Topology:** Classifies the repository's AI footprint (e.g., "RAG Pipeline", "Autonomous Agentic Fleet", or "Local Compute") based on the concentration of vector stores, tool-calling, and ML frameworks.

### 4. Biaxial Anomalies & Architectural Drift
The recorder automatically calculates and flags "Trojan" files. It points the AI directly to files that blend in globally (low Global Drift) but heavily violate the standard conventions of their native programming language (high Local Drift), highlighting them as severe anti-patterns.

### 5. Strategic Refactoring Targets
Instead of just listing bad files, the recorder cross-multiplies metrics to hand the AI actionable targets:
* **The Hotspot Matrix:** Files with high Volatility (Churn) *and* high Risk.
* **Key Person Dependencies:** Massive, load-bearing files written almost entirely by a single developer (High Impact + Siloed Knowledge).
* **Systemic Network Bottlenecks:** Cross-multiplies Graph Theory with Risk (e.g., `Betweenness * State Flux` to find "Contagious Mutations").

### 6. Autonomous AI Vulnerabilities
Actively isolates the Security Lens metrics, specifically hunting for Agentic RCE (LLM logic flowing directly into OS execution) and Prompt Injection surfaces. If any file breaches these thresholds, the LLM is instructed to prioritize these vulnerabilities in its architectural review.

## The Relational Knowledge Graph (SQLite)

For advanced, autonomous agent workflows that utilize SQL generation (like LangChain or AutoGen), Markdown is insufficient. The recorder generates a fully relational SQLite database (`_galaxy_graph.sqlite`) from the live RAM data, specifically tuned for Agentic RAG.

### Relational Schema
Agents can write dynamic SQL queries against the following constructed tables:

* **`stars`**: The core file telemetry, including pre-calculated columns for Risk Vectors, Mass, Volatility, AI Threat Confidence, and Network Centrality.
* **`constellations`**: Folder-level aggregate metrics.
* **`satellites`**: The extracted functions/classes tied back to their parent `star_id`, complete with their Big-O time complexity.
* **`dna_hits` (The Regex Hit Ledger)**: A flattened, queryable list of every single regex pattern triggered by a file. *(Note: Table name preserved for schema compatibility).*
* **`inbound_dependencies` & `outbound_dependencies`**: The bi-directional RAG graph, allowing an agent to recursively query the blast radius of any file.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

