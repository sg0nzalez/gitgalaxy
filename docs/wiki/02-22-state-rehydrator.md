# The State Rehydrator (Memory Cryolinks)

> **The Fast-Track for CI/CD**
>
> The State Rehydrator (`state_rehydrator.py`) is the engine that enables GitGalaxy to run efficiently in Continuous Integration/Continuous Deployment (CI/CD) pipelines. 
>
> Scanning a massive 10,000-file repository from scratch takes compute time. However, in a standard CI pipeline, a developer might only modify three files in a single commit. The State Rehydrator bridges this gap by querying the SQLite Record Keeper and instantly "thawing" the repository's previous historical state directly back into live Python RAM.

## The Cryo-Chamber (SQLite to RAM)

When a Delta Mission is initiated, the Rehydrator bypasses the Optical Pipeline entirely and interfaces directly with the `_galaxy_graph.sqlite` database.

* **Commit Targeting:** The engine queries the `repo_data` table to find the absolute most recent `commit_hash` that GitGalaxy successfully scanned for the target repository. 
* **State Reconstruction:** It extracts the physical metrics of every file (e.g., `file_impact`, `total_loc`, `control_flow_ratio`, `ai_threat_score`) from the `file_data` table.
* **The Cryolink Payload:** It maps these static database rows back into a live Python dictionary schema (the `cryolink`), perfectly mimicking the RAM state that the Orchestrator would have generated during a full scan.

## Temporal Diffs and Delta Scans

This rehydration process is the strict mechanical foundation that makes temporal scans, diffs, and deltas computationally viable. 

Instead of re-running regex math on the entire universe, GitGalaxy leverages the rehydrated state to execute a **Delta Mission**:

1. **Surgical Extraction:** The pipeline asks Git which specific files were modified or added in the new commit. It runs the heavy optical scanners (Language Lens, Security Lens) *only* on those isolated files.
2. **State Merging:** The newly calculated file states overwrite their older counterparts inside the rehydrated `cryolink` RAM dictionary.
3. **The Ripple Effect:** With the merged state living in RAM, the Orchestrator instantly triggers the downstream physics engines (Network Graph, XGBoost Security Auditor). Because network topology (Blast Radius, PageRank) is globally interconnected, modifying even one file can shift the gravity of the entire system. 

## Structural Delta Reporting

By having immediate access to both the "Old State" (via SQLite) and the "New State" (via the Delta Mission), GitGalaxy can instantly calculate exact structural diffs. 

Instead of a standard Git diff showing *text* changes, the engine outputs **Physics Deltas**:
* *"This commit increased the system's Tech Debt by 14%."*
* *"This commit shifted the Blast Radius of `auth.py`, making it a system bottleneck."*
* *"This commit introduced a new Agentic RCE vulnerability."*

This allows security and architecture teams to establish hard CI/CD quality gates based on mathematical structural drift rather than subjective code reviews.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
