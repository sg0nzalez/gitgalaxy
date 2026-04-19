# GitGalaxy: Legacy Refraction & COBOL Cleaner Suite

[![Mainframe Tested](https://img.shields.io/badge/Tested-MVS_3.8j_(1974)-000000.svg?style=flat&logo=ibm)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Deterministic_Regex-00BFFF.svg)](#)
[![State Manager](https://img.shields.io/badge/State-Hybrid_RAM%2FSQLite-8A2BE2.svg)](#)

Welcome to the **COBOL Cleaner & Refraction Suite**. This is a deterministic, mathematical x-ray designed to slice, sanitize, and modernize monolithic legacy systems. 

**Proven in the Iron:** The outputs of these architectural tools natively compile against raw MVS 3.8j operating systems (1974 Hercules Mainframe), while simultaneously scaffolding modern cloud environments.

### The Narrative: From Chaos to Compilable

You point the Refractor Controller at a massive, undocumented COBOL repository. It turns a chaotic folder of `.cbl` files into a deterministic execution pipeline:

* **The Assessment:** Dynamically scales between high-speed RAM and SQLite3.
* **The Graveyard Reaper:** Maps the AST to hunt orphaned memory.
* **The Ghost Deflector:** Mathematically maps data lineage to deflect dead dependencies.
* **The Forges:** Generates pristine PostgreSQL schemas, JSON APIs, and compile-ready JCLs.

---

### The Spoke Tools

This suite is built on a modular Hub-and-Spoke architecture. Every Python script acts as an independent CLI tool or is orchestrated centrally.

#### 1. The Pre-Processors & Sensors
* **Lexical Patcher (`cobol_lexical_patcher.py`):** Safely neutralizes legacy compiler traps.
* **System Limits (`cobol_system_limits_reporter.py`):** The Honesty Protocol. Flags non-deterministic routing logic.

#### 2. The Extractors & Slicers
* **Graveyard Reaper (`cobol_graveyard_finder.py`):** Expands copybooks to calculate dead code bloat.
* **Microservice Slicer (`cobol_microservice_slicer.py`):** Executes 3-pass recursive variable taint-tracking.
* **ETL Unpacker (`cobol_etl_unpacker.py`):** Translates binary EBCDIC and Packed Decimal to CSVs.

#### 3. The Cloud & Mainframe Forges
* **Compiler Forge (`cobol_compiler_forge.py`):** Flattens copybooks and generates era-aware build JCLs.
* **Cloud Schema Forge (`cobol_schema_forge.py`):** Translates `PIC` clauses to strict PostgreSQL DDLs.
* **Zero-Trust JCL (`cobol_jcl_forge.py`):** Extracts `SELECT` mappings to auto-generate strict JCL emulators.

#### 4. The AI Boundary
* **Anomaly Task Forge (`cobol_agent_task_forge.py`):** Isolates structural anomalies into bounded JSON job tickets.

---

### Quickstart: Running the Controller

You don't need to run the tools individually. The Orchestrator handles the physics.

**Basic Refraction (Sanitize, Map, and Forge JCL/Schemas):**
```bash
python3 cobol_refractor_controller.py /path/to/legacy/repo
```

### What You Get (The Clean Room)
The controller generates a timestamped `_gitgalaxy_clean` directory containing:
1. `01_zero_trust_jcls/`: Fully compiling, least-privilege IBM JCLs.
2. `02_cloud_schemas/`: PostgreSQL `.sql` and `.json` schema translations.
3. `03_audit_reports/`: The Master Refraction Audit (quantifying lines of code saved and excess I/O blocked).
4. `04_ir_state_dumps/`: Relational JSON graphs mapping dead-code state and DAG lineage.
5. `05_microservice_slices/`: Isolated JSON business logic ready for translation.
6. `06_ai_agent_jobs/`: Structured JSON tickets for LLM remediation.


---
### 🌌 Powered by the blAST Engine (Bypassing LLMs and ASTs)
This tool is a specialized spoke in the larger GitGalaxy ecosystem. It is driven by our custom mathematical heuristics engine, capable of mapping multi-dimensional relationships at extreme velocity. Read the official documentation to explore the internal physics of the refraction controllers:

* 📖 **[The Legacy Refraction Controller](../../../docs/wiki/05-01-legacy-refraction-controller.md)**
* 📖 **[Graveyard Reaper & Dead Code Mathematics](../../../docs/wiki/05-10-graveyard-reaper.md)**
* 📖 **[Zero-Trust JCL Forge Mechanics](../../../docs/wiki/05-12-zero-trust-jcl-forge.md)**
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)**
