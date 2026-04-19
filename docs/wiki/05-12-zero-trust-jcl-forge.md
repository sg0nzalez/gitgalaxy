# Zero-Trust JCL Forge

> **Architecture: Intent Extraction & Secure Provisioning**
>
> **Summary:** The Zero-Trust JCL Forge translates the raw structural intent of a COBOL program into a highly restricted Job Control Language (JCL) emulator. It guarantees that the resulting execution environment only provisions the exact data access the program mathematically requires to run.

## The AST Flattener
Legacy COBOL is strictly formatted to 80-character punch cards, meaning long file assignments frequently break across multiple lines. To parse this accurately, the forge utilizes an AST Flattener:
* It strips out punch-card formatting and ignores any text located in Column 7 (legacy comments).
* It merges the remaining code into a single continuous string.
* This allows the regex engine to successfully extract `SELECT ... ASSIGN TO` file bindings even if the keywords are separated by 20 lines of whitespace or line breaks.

## DAG-Driven I/O Provisioning
Once the required physical files (DD names) are extracted, the forge queries the DAG Architect's lineage data to determine the exact execution intent for each file, assigning strict Data Set Parameters (`DISP`):
* **Outputs (Write-Only or I/O):** The forge provisions the file with `DISP=(NEW,CATLG,DELETE)`, allocating fresh tracking space (`SPACE=(CYL,(5,1),RLSE)`) for the output generation.
* **Inputs (Read-Only):** The forge restricts the file to `DISP=SHR` (Shared Read). 
* **The Anomaly Warning:** If the program requests a file in its Data Division, but the DAG Architect proves the program *never actually opens it* in the execution logic, the forge defaults to read-only access and injects an explicit `WARNING: NO EXPLICIT OPEN INTENT` comment into the JCL for architectural review.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

