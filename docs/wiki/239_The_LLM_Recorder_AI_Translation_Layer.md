# 2.3.11. The LLM Recorder (AI Translation Layer)

> **The Bridge to Autonomous Agents**
>
> The LLM Recorder (`llm_recorder.py`) bridges the gap between GitGalaxy's raw mathematical physics and autonomous AI agents. Rather than forcing a Large Language Model to hallucinate meaning from thousands of lines of raw JSON, this phase translates the pipeline's telemetry into highly optimized, token-dense artifacts designed specifically for LLM context windows and Retrieval-Augmented Generation (RAG) systems.

## 2.3.11.A. Reverse Dependency Resolution

Before generating outputs, the recorder performs a unified reverse-dependency map across the entire galaxy. It traces every `raw_import` back to its origin file to establish a bi-directional graph:

* **Structural Pillars (Blast Radius):** Files with the highest inbound connections ("Imported By"). Tells the AI that modifying this file carries a massive risk of cascading breakages.
* **Orchestrators (Fragility Index):** Files with the highest outbound connections ("Imports"). Tells the AI that this file is highly coupled and fragile to external API changes.

## 2.3.11.B. The Token-Optimized Markdown Brief

The primary output is a dense, pre-engineered Markdown prompt (`_galaxy_llm.md`) that fits cleanly into standard context windows (like Claude 3.5 or GPT-4o). It structurally guides the AI's analysis:

### 1. Hardcoded System Instructions
The brief injects strict Prompt Engineering at the header and footer. It explicitly commands the AI to "Measure Risk, Not Quality," enforcing a blameless, objective tone based on physical DNA (regex hits) rather than subjective coding styles. It instructs the AI exactly how to read the 18-point risk vector.

### 2. The Cumulative Risk Hitlist
Calculates and surfaces the top 10 most dangerous files in the repository by mathematically summing their individual risk exposures. It extracts the top 4 "Primary Risk Drivers" for each file so the AI instantly knows *why* the file is failing.

### 3. The Visible Matter Hitlist
Details the top 25 heaviest load-bearing files in the system. To save tokens, the raw 60-point `hit_vector` is intelligently bucketed into readable categories: *Structure*, *Risk/State*, *Architecture*, and *Defense*. It also lists the heaviest internal functions (Satellites) so the AI knows exactly where to target refactoring efforts.

### 4. Security Triage
Actively isolates the Security Lens metrics (Memory Corruption, Obscured Payloads, Secrets Leaks). If any file breaches a security threshold, it is explicitly flagged in a dedicated section, instructing the AI to prioritize these vulnerabilities in its response.

## 2.3.11.C. The Relational Knowledge Graph (SQLite)

For advanced, autonomous agent workflows that utilize SQL generation (like LangChain or AutoGen), Markdown is insufficient. The recorder generates a fully relational SQLite database (`_galaxy_graph.sqlite`) from the live RAM data.

### Relational Schema
Agents can write dynamic SQL queries against the following constructed tables:

* **`stars`**: The core file telemetry, including pre-calculated columns for all 18 Risk Vectors, Mass, Volatility, and Silo Risk (Ownership Entropy).
* **`constellations`**: Folder-level aggregate metrics.
* **`satellites`**: The extracted functions/classes tied back to their parent `star_id`.
* **`dna_hits`**: A flattened, queryable list of every single regex pattern triggered by a file.
* **`inbound_dependencies` & `outbound_dependencies`**: The bi-directional RAG graph, allowing an agent to recursively query the blast radius of any file.
