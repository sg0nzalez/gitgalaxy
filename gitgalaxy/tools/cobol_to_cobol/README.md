# GitGalaxy: Mainframe Refactoring & COBOL Modernization Suite

[![Mainframe Tested](https://img.shields.io/badge/Tested-MVS_3.8j_(1974)-000000.svg?style=flat&logo=ibm)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Deterministic_Regex-00BFFF.svg)](#)
[![State Manager](https://img.shields.io/badge/State-Hybrid_RAM%2FSQLite-8A2BE2.svg)](#)

Welcome to the **GitGalaxy Mainframe Modernization Suite**. This is a deterministic, high-speed static analysis suite designed to safely slice, sanitize, and modernize monolithic legacy systems. 

**Mainframe Proven:** The outputs of these architectural tools natively compile against raw MVS 3.8j operating systems (1974 Hercules Mainframe), while simultaneously scaffolding modern cloud environments.

### 🔄 The Modernization Pipeline

You point the Migration Controller at a massive, undocumented COBOL repository. It translates a chaotic folder of `.cbl` files into a deterministic execution pipeline:

* **The Assessment:** Dynamically scales between high-speed RAM and SQLite3.
* **Dead Code Extraction:** Uses structural heuristics to mathematically map and extract orphaned memory and dead code bloat. *(AST-Free)*
* **Dependency Mapping:** Maps data lineage to deflect dead dependencies.
* **Asset Generation:** Generates pristine PostgreSQL schemas, JSON APIs, and compile-ready JCLs.

---

### 🛠️ The Enterprise Toolsets

This suite is built on a modular Hub-and-Spoke architecture. Every Python script acts as an independent CLI tool or is orchestrated centrally.

#### 1. Pre-Processors & Sensors
* **Lexical Patcher (`cobol_lexical_patcher.py`):** Safely neutralizes legacy compiler traps.
* **System Limits Reporter (`cobol_system_limits_reporter.py`):** Flags non-deterministic routing logic and system constraint breaches.

#### 2. Extractors & Slicers
* **Graveyard Finder (`cobol_graveyard_finder.py`):** Expands copybooks to calculate dead code bloat.
* **Microservice Slicer (`cobol_microservice_slicer.py`):** Executes 3-pass recursive variable taint-tracking.
* **ETL Unpacker (`cobol_etl_unpacker.py`):** Translates binary EBCDIC and Packed Decimal to CSVs.

#### 3. Cloud & Mainframe Forges
* **Compiler Forge (`cobol_compiler_forge.py`):** Flattens copybooks and generates era-aware build JCLs.
* **Cloud Schema Forge (`cobol_schema_forge.py`):** Translates `PIC` clauses to strict PostgreSQL DDLs.
* **Zero-Trust JCL Forge (`cobol_jcl_forge.py`):** Extracts `SELECT` mappings to auto-generate strict, least-privilege JCL emulators.

#### 4. The AI Remediation Boundary
* **Anomaly Task Forge (`cobol_agent_task_forge.py`):** Isolates structural anomalies into bounded JSON job tickets for LLM remediation.

---

### 🚀 Quickstart: Running the Controller

You don't need to run the tools individually. The central orchestrator handles the execution pipeline.

**Basic Modernization (Sanitize, Map, and Forge JCL/Schemas):**
```bash
python3 cobol_refractor_controller.py /path/to/legacy/repo
```

### 📁 What You Get (The Clean Room)
The controller generates a timestamped `_gitgalaxy_clean` directory containing:
1. `01_zero_trust_jcls/`: Fully compiling, least-privilege IBM JCLs.
2. `02_cloud_schemas/`: PostgreSQL `.sql` and `.json` schema translations.
3. `03_audit_reports/`: The Master Audit (quantifying lines of code saved and excess I/O blocked).
4. `04_ir_state_dumps/`: Relational JSON graphs mapping dead-code state and DAG lineage.
5. `05_microservice_slices/`: Isolated JSON business logic ready for translation.
6. `06_ai_agent_jobs/`: Structured JSON tickets for LLM remediation.

---
### 🌌 Powered by the blAST Engine (Bypassing LLMs and ASTs)
This tool is a modular enterprise integration within the broader GitGalaxy architecture. It is driven by our custom mathematical heuristics engine, capable of mapping multi-dimensional relationships at extreme velocity without requiring rigid ASTs. Read the official documentation to explore the architecture of the modernization controllers:

* 📖 **[The Legacy Modernization Controller](../../../docs/wiki/05-01-legacy-refraction-controller.md)**
* 📖 **[Dead Code Extraction Mathematics](../../../docs/wiki/05-10-graveyard-reaper.md)**
* 📖 **[Zero-Trust JCL Forge Mechanics](../../../docs/wiki/05-12-zero-trust-jcl-forge.md)**
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)**