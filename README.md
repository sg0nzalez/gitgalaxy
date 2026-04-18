# GitGalaxy

[![PyPI version](https://badge.fury.io/py/gitgalaxy.svg)](https://badge.fury.io/py/gitgalaxy)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: PolyForm Noncommercial](https://img.shields.io/badge/License-PolyForm%20Noncommercial-blue.svg)](https://polyformproject.org/licenses/noncommercial/1.0.0/)

[![Engine](https://img.shields.io/badge/Engine-blAST-8A2BE2.svg)](#)
[![Velocity](https://img.shields.io/badge/Velocity-100k+_LOC%2Fs-00C957.svg)](#)
[![Analysis](https://img.shields.io/badge/Analysis-Code_Bioinformatics-00BFFF.svg)](#)
[![Threat Hunting](https://img.shields.io/badge/Threat_Hunting-Behavioral-FF4500.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Zero__Trust-teal.svg)](#)

[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0-brightgreen.svg)](https://pypi.org/project/gitgalaxy/)
[![Airgap Ready](https://img.shields.io/badge/Security-Airgap_Ready-teal.svg)](#)

### **The blAST Engine: A custom heuristics-based AST-free Knowledge Graph Generator**

The blAST (Bypassing LLMs and ASTs) engine is a custom-made knowledge graph engine that resolves repositories at the function level. It scores each function based on 50 unique metrics, rolls that data up to score the file, and finally summarizes the entire repository. 

By utilizing a custom engine, we retain full control over the search space. We built it to be exceptionally fast, capable of assessing your entire repository without requiring compilable code—a fundamental limitation of standard Abstract Syntax Trees (ASTs). ASTs are great for finding missing commas and memory overflows, but they miss the forest for the trees when generating knowledge graphs. LLMs, on the other hand, suffer from hallucination during large context windows and yield probabilistic, fluctuating answers. 

The blAST engine solves this. Because all programming languages utilize keywords and functions, our engine treats code files as text, scanning for these structural anchors to build a deterministic 3D knowledge graph. It seamlessly handles mid-file language switching, assesses the architectural ratio of test files to logic, and extracts invaluable project structure data that ASTs ignore. 

Every assumption our system makes has been abstracted into over 300 tunable variables. Think of GitGalaxy as a highly calibrated telescope. You can query the number of active API network nodes, isolate unique external imports, or highlight functions exhibiting extreme cognitive load—all adjusted via custom whitelists and blacklists to eliminate false-positive fatigue. Field-tested on over 1,000 repositories spanning 50+ languages and 250+ extensions, the engine comes equipped with smart defaults ready for immediate deployment.

**Core Technology**
* Bypasses LLMs and rigid ASTs
* Doesn't care if code compiles (AST-free)
* Maps code by keyword regex profiles
* Eliminates LLM architectural hallucinations and context window limits
* Scans 50+ languages, 250+ extensions, fully folder-aware

**Extreme Velocity & Scale**
* 100,000 LOC/sec code analysis
* 0.07 GB/sec raw log ingestion
* Full-system scans in minutes without data sampling
* 100% daily system coverage

**Intelligence & Tracking**
* Builds longitudinal knowledge graphs
* Tracks logic at the function level
* Monitors risk exposures and temporal code evolution over time

**Security & Deployment**
* 100% air-gapped execution
* On-premise deployment with zero IP exfiltration risk
* Zero-trust processing model

**How to use**
* Python-based: `pip install gitgalaxy`
* CLI execution
* Outputs forensic JSONs (optimized for AI-agent summary reports) and a native SQLite3 database for robust querying and storage.

**Validation**
* Population statistics derived from 1,000+ repositories.
* Comparative function and architecture analysis of 10 different DOOM source ports.
* Proven keyword pattern automation for mapping and cleaning COBOL mainframes (JCLs, DAGs, schemas).
* Successful from-scratch translation of legacy COBOL to compiling Java Spring Boot architectures.

> **📖 Official Documentation:** Read the full technical specifications, architecture blueprints, and the Taxonomical Equivalence Map at **[squid-protocol.github.io/gitgalaxy](https://squid-protocol.github.io/gitgalaxy/)**.

---

## Quickstart

### 1. Install

```bash
pip install gitgalaxy

### 2. Scan a Repository

Point the GalaxyScope at any local repository or ZIP archive. The engine runs entirely on your local machine—zero data is transmitted.

```bash
galaxyscope /path/to/your/local/repo
```

---

## The GitGalaxy Ecosystem

GitGalaxy operates on a modular Hub-and-Spoke architecture. While the core engine provides the overarching physics and cartography, our specialized toolsets leverage that graph to execute enterprise-grade operations.

* 🌌 **[The Hub: Orbital Optics & Cartography](docs/wiki/1_Foundation__Architecture.md)**
  The core AST-free parsing engine that handles signal processing, spatial rendering, and telemetry recording.
* 🏭 **[Legacy Modernization: Java Forge](tools/modernization/java_forge/README.md)**
  Automated, high-fidelity pipelines designed to map, slice, and forge legacy COBOL monoliths into compiling Spring Boot microservices.
* 🛠️ **[Legacy Modernization: COBOL Refactoring](tools/modernization/cobol_cleaner/README.md)**
  Maintenance tools for legacy systems, including lexical patchers, graveyard code hunters, and JCL operational auditors.
* 🛡️ **[Supply Chain Security](tools/security_ops/README.md)**
  Pre-commit defense layers including the high-speed Vault Sentinel for secret detection and binary anomaly firewalls.
* 📡 **[Network Auditing](tools/cartography/README.md)**
  Full API network mapping to hunt down undocumented "Shadow APIs" by comparing physical codebase routers against official Swagger documentation.
* 🕵️ **[Terabyte Log Scanning](tools/compliance/README.md)**
  High-velocity PII leak hunters and regex-driven anomaly detectors built to chew through massive server logs.
* 📋 **[Compliance Operations](tools/security_ops/README.md)**
  Automated Software Bill of Materials (SBOM) generation based on the physical reality of the codebase.

  ## The Web Viewer (Frictionless Dashboards)

If you prefer visual analytics, we've built a non-numerical dashboard where each file represents a star, sized and colored according to specific risk metrics. 

Simply drag and drop your generated `your_repo_GPU_galaxy.json` file (or a `.zip` of your raw repository) directly into [GitGalaxy.io](https://gitgalaxy.io/). All rendering and scanning happens entirely in your browser's local memory.

![Apollo 11 State Flux](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/apollo-11_state_flux.png)

![GitGalaxy SQLite Overview](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/sqlite_overview.png)

## Zero-Trust Architecture

Your code never leaves your machine. GitGalaxy performs 100% of its scanning and vectorization locally.

* **No Data Transmission:** Source code is never transmitted to any API, cloud database, or third-party service.
* **Ephemeral Memory Processing:** Repositories are unpacked into a volatile memory buffer (RAM) and are automatically purged when the browser tab is closed.
* **Privacy-by-Design:** Even when using the web-based viewer, the data remains behind the user's firewall at all times.

![GitGalaxy Data HUD](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/data_hud.png)

![GitGalaxy Meta Visualizer](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/metavisualizer.png)

## License & Copyright

Copyright (c) 2026 Joe Esquibel

GitGalaxy is released under the PolyForm Noncommercial License 1.0.0. It is completely free for personal use, research, experiment, testing, and hobby projects. Use by educational or charitable organizations is also permitted.

Any commercial use or integration into commercial SaaS products or corporate CI/CD pipelines requires a separate commercial license. Please reach out via gitgalaxy.io to discuss commercial integration.