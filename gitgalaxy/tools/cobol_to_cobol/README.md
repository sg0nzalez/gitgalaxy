# GitGalaxy: Mainframe Refactoring & COBOL Modernization Suite

[![Mainframe Tested](https://img.shields.io/badge/Tested-MVS_3.8j_(1974)-000000.svg?style=flat&logo=ibm)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Deterministic_Regex-00BFFF.svg)](#)
[![State Manager](https://img.shields.io/badge/State-Hybrid_RAM%2FSQLite-8A2BE2.svg)](#)

Welcome to the **GitGalaxy Mainframe Modernization Suite**. This is a deterministic, high-speed static analysis suite designed to safely slice, sanitize, and [map monolithic legacy systems](https://squid-protocol.github.io/gitgalaxy/cookbook/map-cobol-monoliths/). 

**Mainframe Proven:** The outputs of these architectural tools natively compile against raw MVS 3.8j operating systems (1974 Hercules Mainframe), while simultaneously scaffolding modern cloud environments.

### 🔄 The Modernization Pipeline

You point the [Legacy Refraction Controller](https://squid-protocol.github.io/gitgalaxy/05-01-legacy-refraction-controller/) at a massive, undocumented COBOL repository. It translates a chaotic folder of `.cbl` files into a deterministic execution pipeline:

* **The Assessment:** Dynamically scales between high-speed RAM and SQLite3.
* **Dead Code Extraction:** Uses structural heuristics to mathematically map and [extract orphaned memory and dead code bloat](https://squid-protocol.github.io/gitgalaxy/cookbook/identifying-dead-code-in-cobol/). *(AST-Free)*
* **Dependency Mapping:** Maps data lineage to deflect dead dependencies.
* **Asset Generation:** Generates pristine PostgreSQL schemas, JSON APIs, and compile-ready JCLs.

---

### 🛠️ The Enterprise Toolsets

This suite is built on a modular Hub-and-Spoke architecture. Every Python script acts as an independent CLI tool or is orchestrated centrally.

#### 1. Pre-Processors & Sensors
* **[Lexical Patcher](https://squid-protocol.github.io/gitgalaxy/05-13-lexical-patcher/) (`cobol_lexical_patcher.py`):** Safely neutralizes legacy compiler traps.
* **[System Limits Reporter](https://squid-protocol.github.io/gitgalaxy/05-17-system-limits-reporter/) (`cobol_system_limits_reporter.py`):** Flags non-deterministic routing logic and system constraint breaches.
  <br>![System Limits Reporter](../../../docs/wiki/assets/system_limits_reporter.gif)

#### 2. Extractors & Slicers
* **[Graveyard Reaper](https://squid-protocol.github.io/gitgalaxy/05-10-graveyard-reaper/) (`cobol_graveyard_finder.py`):** Expands copybooks to calculate dead code bloat.
  <br>![Graveyard Reaper](../../../docs/wiki/assets/graveyard_reaper.gif)
* **[DAG Architect](https://squid-protocol.github.io/gitgalaxy/05-08-dag-architect/) (`cobol_dag_architect.py`):** Maps data lineage to [mathematically calculate zero-trust execution topology](https://squid-protocol.github.io/gitgalaxy/cookbook/creating-dag-from-cobol-files/).
  <br>![DAG Architect](../../../docs/wiki/assets/dag_architect.gif)
* **[Microservice Slicer](https://squid-protocol.github.io/gitgalaxy/05-14-microservice-slicer/) (`cobol_microservice_slicer.py`):** Executes 3-pass recursive variable taint-tracking for safe [business logic extraction](https://squid-protocol.github.io/gitgalaxy/cookbook/cobol-microservice-slicing/).
  <br>![Microservice Slicer](../../../docs/wiki/assets/microservice_slicer.gif)
* **[ETL Unpacker](https://squid-protocol.github.io/gitgalaxy/05-09-etl-unpacker/) (`cobol_etl_unpacker.py`):** Translates binary EBCDIC and Packed Decimal to CSVs to [unpack hidden ETL flows](https://squid-protocol.github.io/gitgalaxy/cookbook/unpacking-etl-from-cbl-files/).

#### 3. Cloud & Mainframe Forges
* **[Compiler Forge](https://squid-protocol.github.io/gitgalaxy/05-07-mainframe-compiler-forge/) (`cobol_compiler_forge.py`):** Flattens copybooks and generates era-aware build JCLs.
  <br>![Compiler Forge](../../../docs/wiki/assets/compiler_forge.gif)
* **[Cloud Schema Forge](https://squid-protocol.github.io/gitgalaxy/05-15-cloud-schema-forge/) (`cobol_schema_forge.py`):** Translates `PIC` clauses to [strict PostgreSQL DDL schemas](https://squid-protocol.github.io/gitgalaxy/cookbook/creating-schema-from-cobol-files/).
  <br>![Cloud Schema Forge](../../../docs/wiki/assets/cloud_schema_forge.gif)
* **[Zero-Trust JCL Forge](https://squid-protocol.github.io/gitgalaxy/05-12-zero-trust-jcl-forge/) (`cobol_jcl_forge.py`):** Extracts `SELECT` mappings to [auto-generate strict, least-privilege JCL emulators](https://squid-protocol.github.io/gitgalaxy/cookbook/creating-jcl-from-cobol-files/).
  <br>![Zero-Trust JCL Forge](../../../docs/wiki/assets/jcl_forge_demo.gif)
  
#### 4. The AI Remediation Boundary
* **[Anomaly Task Forge](https://squid-protocol.github.io/gitgalaxy/05-16-anomaly-agent-task-forge/) (`cobol_agent_task_forge.py`):** Isolates structural anomalies into bounded JSON job tickets for LLM remediation.

---

### 🚀 Quickstart: Running the Controller

You don't need to run the tools individually. The central orchestrator handles the execution pipeline.

**Basic Modernization (Sanitize, Map, and Forge JCL/Schemas):**
```bash
python3 cobol_refractor_controller.py /path/to/legacy/repo
```
![Refractor Controller Pipeline](../../../docs/wiki/assets/refractor_controller.gif)

---

### 🖥️ Real-World Telemetry: CICS Banking Application
Below is the live console output of the GitGalaxy orchestrator processing a legacy IBM CICS banking application. Notice the engine identifying over 6,700 lines of dead code, warning about macro substitutions, and automatically routing the compiler based on the detected COBOL dialect (74 vs 85).

```text
=== 1. INITIATING GRAVEYARD REAPER ===
🪦 GitGalaxy Reaper scanning cics-banking-sample-application-cbsa for dead code...
[... File Scans Omitted for Brevity ...]
==========================================================
 📉 DEAD CODE ELIMINATION REPORT
==========================================================
 Files Flagged for Cleanup : 29
 Unused Memory Addresses   : 817 orphaned variables
 Unreachable Logic Blocks  : 590 phantom paragraphs
 ✂️ Estimated Bloat Removed : ~6717 Lines of Code
==========================================================

=== 2. INITIATING DAG ARCHITECT ===
🕸️ GitGalaxy DAG Architect mapping data lineage in: cics-banking-sample-application-cbsa...
==========================================================
 ⚡ ZERO-TRUST EXECUTION PIPELINE (TOPOLOGICAL SORT)
==========================================================
 STEP 01: Run [BANKDATA]
          ↳ Reads : None
          ↳ Writes: VSAM
----------------------------------------------------------

=== 3. INITIATING SYSTEM LIMITS REPORTER ===
📠 Scanning directory for System Limits: cics-banking-sample-application-cbsa...
🔎 GitGalaxy Honesty Protocol scanning 29 files for structural dragons...
==========================================================================================
 ⚠️ [XFRFUN.cbl : Line 0128] HIGH LIMIT - Macro substitution detected. AST math may drift from actual compiled execution.
 ⚠️ [CREACC.cbl : Line 0260] HIGH LIMIT - Macro substitution detected. AST math may drift from actual compiled execution.
 ⚠️ [INQACC.cbl : Line 0199] HIGH LIMIT - Macro substitution detected. AST math may drift from actual compiled execution.
 ⚠️ [DELACC.cbl : Line 0200] HIGH LIMIT - Macro substitution detected. AST math may drift from actual compiled execution.
 ⚠️ [GETSCODE.cbl : Line 0028] HIGH LIMIT - Macro substitution detected. AST math may drift from actual compiled execution.
==========================================================================================
 🚨 WARNING: Found 5 structural anomalies requiring human architectural review.
==========================================================================================

=== 4. INITIATING CLOUD SCHEMA FORGE ===
🔨 GitGalaxy Schema Forge striking anvil for: BNK1UAC.cbl...
==========================================================
 🐘 POSTGRESQL DDL (CLOUD DATABASE SCHEMA)
==========================================================
CREATE TABLE DFHCOMMAREA (
    WS_CICS_RESP                   INTEGER,
    WS_CICS_RESP2                  INTEGER,
    WS_CICS_FAIL_MSG               VARCHAR(70),
    WS_COMM_EYE                    VARCHAR(4),
    WS_COMM_CUSTNO                 VARCHAR(10),
    WS_COMM_ACCNO                  DECIMAL(8, 0),
    WS_COMM_AVAIL_BAL              DECIMAL(12, 2),
    WS_COMM_ACTUAL_BAL             DECIMAL(12, 2)
    -- [Schema Omitted for Brevity]
);

=== 5. INITIATING MICROSERVICE SLICER ===
🔪 GitGalaxy Slicer hunting aliases for [WS-ACCOUNT-BALANCE] in BNK1UAC.cbl...
==========================================================
 🎯 Sliced 0 distinct business rules.
==========================================================

=== 6. INITIATING COMPILER FORGE ===
======================================================================
 🏗️  GITGALAXY MAINFRAME COMPILER FORGE (PRE-COMPILER ACTIVE)
======================================================================
  [+] Forged COBOL-85 Pipeline : BUILD_BNK1UAC.jcl
  [+] Forged COBOL-85 Pipeline : BUILD_DBCRFUN.jcl
  [+] Forged COBOL-74 Pipeline : BUILD_GETSCODE.jcl
  [+] Forged COBOL-85 Pipeline : BUILD_BANKDATA.jcl
  [+] Forged COBOL-74 Pipeline : BUILD_GETCOMPY.jcl
======================================================================

=== 7. INITIATING MASTER ORCHESTRATOR (REFRACTOR CONTROLLER) ===
======================================================================
 🚀 COBOL REFRACTOR CONTROLLER (v4.0) ENGAGED
 Target: cics-banking-sample-application-cbsa
======================================================================
🛰️ Scouting repository mass...
   ↳ Found: 29 executable files (0.83 MB)
   ↳ OPTIMAL MASS: Engaging High-Speed RAM Dictionary.
 Forging Context-Aware Artifacts at: cics-banking-sample-application-cbsa_gitgalaxy_clean_20260422_153624
----------------------------------------------------------------------
======================================================================
 🏁 REFRACTION COMPLETE: Hybrid Pipeline execution successful.
 📁 Location: /srv/storage_16tb/projects/gitgalaxy/data/cobol_corpus/cics-banking-sample-application-cbsa_gitgalaxy_clean_20260422_153624
======================================================================
```

---

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

* 📖 **[The Legacy Refraction Controller](https://squid-protocol.github.io/gitgalaxy/05-01-legacy-refraction-controller/)**
* 📖 **[Dead Code Extraction Mathematics](https://squid-protocol.github.io/gitgalaxy/05-10-graveyard-reaper/)**
* 📖 **[Zero-Trust JCL Forge Mechanics](https://squid-protocol.github.io/gitgalaxy/05-12-zero-trust-jcl-forge/)**
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)**