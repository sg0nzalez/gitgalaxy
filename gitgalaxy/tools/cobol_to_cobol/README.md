# GitGalaxy: Legacy Refraction & COBOL Cleaner Suite

[![Mainframe Tested](https://img.shields.io/badge/Tested-MVS_3.8j_(1974)-000000.svg?style=flat&logo=ibm)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Deterministic_Regex-00BFFF.svg)](#)
[![State Manager](https://img.shields.io/badge/State-Hybrid_RAM%2FSQLite-8A2BE2.svg)](#)

Welcome to the **COBOL Cleaner & Refraction Suite**. This isn't just a linter; it's a deterministic, mathematical x-ray designed to slice, sanitize, and modernize monolithic legacy systems. 

**🔥 Proven in the Iron:** The outputs of these architectural tools have been fully compile-tested against raw MVS 3.8j operating systems running on a 1974 Hercules Mainframe emulator. They generate code and JCL that natively compiles on legacy iron while perfectly scaffolding modern cloud environments.

### 🧠 The Narrative: From Chaos to Compilable

Imagine dropping into a massive, undocumented COBOL mainframe repository. You have no idea what runs, what is dead, or how the data flows. 

You point the `cobol_refractor_controller.py` at the directory.
1. **The Assessment:** The controller weighs the repository mass. If it's under 200MB, it operates in high-speed RAM. If it's massive, it spins up a hybrid SQLite3 database to prevent OOM crashes.
2. **The Graveyard Reaper:** It maps the entire AST, hunting down "Orphaned Memory" (variables declared but never used) and "Phantom Logic" (paragraphs that are never executed).
3. **The Ghost Deflector (DAG Architect):** Knowing what code is dead, the DAG Architect mathematically maps the exact data lineage (Inputs/Outputs). Because it knows the dead code, it mathematically deflects "Ghost Dependencies"—files that appear to be requested but exist in dead execution blocks.
4. **The Forges:** With the exact execution intent mapped, the suite generates pristine PostgreSQL cloud schemas, JSON API models, and 100% compile-ready IBM JCLs.

You turn a chaotic folder of `.cbl` files into a deterministic, topological execution pipeline.

---

### 🛠️ The Spoke Tools

This suite is built on a "Unix philosophy" modular architecture. Every Python script acts as an independent CLI tool or is orchestrated by the Refractor Controller.

#### 1. The Pre-Processors & Sensors
* **Lexical Patcher (`cobol_lexical_patcher.py`):** Features a Dialect Sensor that determines if the code is COBOL-74 or COBOL-85+. Safely neutralizes legacy traps like `NEXT SENTENCE` without triggering catastrophic `0C1` compiler crashes.
* **System Limits Reporter (`cobol_system_limits_reporter.py`):** The "Honesty Protocol." Scans the repository for "Ancient Dragons"—commands that break deterministic math (e.g., `ALTER` statements dynamically rewriting `GO TO` jumps, or `CICS ASYNC` error routing).

#### 2. The Extractors & Slicers
* **Graveyard Reaper (`cobol_graveyard_finder.py`):** Recursively expands inline copybooks to trace memory across files, calculating exactly how much dead bloat exists.
* **Microservice Slicer (`cobol_microservice_slicer.py`):** Provide it a target variable, and it executes a 3-pass recursive taint-tracking algorithm across aliases to extract *only* the business rules relevant to that variable.
* **ETL Unpacker (`cobol_etl_unpacker.py`):** The Data Bridge. Translates raw binary EBCDIC mainframe files into UTF-8 CSVs, unpacking legacy `COMP-3` (Packed Decimal) formats on the fly using calculated byte layouts.

#### 3. The Cloud & Mainframe Forges
* **Compiler Forge (`cobol_compiler_forge.py`):** Flattens copybooks into a single payload and generates era-aware build JCLs. If it detects modern syntax, it routes to the Enterprise Compiler (`IGYWCL`); if old, it uses the OS/VS Compiler (`COBUCL`).
* **Cloud Schema Forge (`cobol_schema_forge.py`):** Translates legacy `PIC` clauses into strict PostgreSQL DDL and JSON schemas. Actively drops columns if the IR state flags them as dead memory.
* **Zero-Trust JCL Forge & Auditor (`cobol_jcl_forge.py`, `cobol_jcl_auditor.py`):** Rips through punch-card formatting to extract `SELECT ... ASSIGN TO` mappings, auto-generating strict JCL emulators. The Auditor then compares the new JCL against the legacy JCL to calculate exact bloat reduction and shedding of over-permissioned I/O.

#### 4. The AI Boundary
* **Anomaly Agent Task Forge (`cobol_agent_task_forge.py`):** When the Honesty Protocol finds a structural dragon, this forge isolates the context (including data lineage) and generates a strict, bounded JSON job ticket designed to be resolved by autonomous LLM agents without hallucinating external dependencies.

---

### 🚀 Quickstart: Running the Controller

You don't need to run the tools individually. The Orchestrator handles the physics.

**Basic Refraction (Sanitize, Map, and Forge JCL/Schemas):**
`python3 cobol_refractor_controller.py /path/to/legacy/repo`

**Global Taint-Tracking (Extract a specific business rule across the entire repo):**
`python3 cobol_refractor_controller.py /path/to/legacy/repo --var "TAX-CALCULATION-TOTAL"`

### 📁 What You Get (The Clean Room)
The controller generates a timestamped `_gitgalaxy_clean` directory containing:
1. `01_zero_trust_jcls/`: Fully compiling, least-privilege IBM JCLs.
2. `02_cloud_schemas/`: PostgreSQL `.sql` and `.json` schema translations.
3. `03_audit_reports/`: The Master Refraction Audit (quantifying lines of code saved and excess I/O blocked).
4. `04_ir_state_dumps/`: The relational JSON graphs capturing the dead-code state and DAG lineage.
5. `05_microservice_slices/`: (Optional) The isolated JSON business logic ready for Java/Python translation.
6. `06_ai_agent_jobs/`: The structured JSON tickets for LLM remediation if structural anomalies were detected.