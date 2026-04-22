# GitGalaxy

[![PyPI version](https://badge.fury.io/py/gitgalaxy.svg)](https://badge.fury.io/py/gitgalaxy)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: PolyForm Noncommercial](https://img.shields.io/badge/License-PolyForm%20Noncommercial-blue.svg)](https://polyformproject.org/licenses/noncommercial/1.0.0/)

[![Engine](https://img.shields.io/badge/Engine-blAST-8A2BE2.svg)](#)
[![Velocity](https://img.shields.io/badge/Velocity-100k+_LOC%2Fs-00C957.svg)](#)
[![Analysis](https://img.shields.io/badge/Analysis-Code_Bioinformatics-00BFFF.svg)](#)
[![Threat Hunting](https://img.shields.io/badge/Threat_Hunting-Behavioral-FF4500.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Zero__Trust-teal.svg)](#)
[![Coverage](https://img.shields.io/badge/Coverage-50%2B_Languages-00C957.svg)](#)
[![Scale](https://img.shields.io/badge/Scale-100k%2B_LOC%2Fsec-00BFFF.svg)](#)

[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0-brightgreen.svg)](https://pypi.org/project/gitgalaxy/)
[![Airgap Ready](https://img.shields.io/badge/Security-Airgap_Ready-teal.svg)](#)

### **AST-Free Static Analysis & Knowledge Graph Engine**

The blAST (Bypassing LLMs and ASTs) engine is a custom-made knowledge graph engine that resolves repositories at the function level. It scores each function based on 50 unique metrics, rolls that data up to score the file, and finally summarizes the entire repository.

### Scanning Apollo-11 with the blAST Engine

![GitGalaxy CLI Scan](./docs/wiki/assets/apollo11_scan.gif)

By utilizing a custom engine, we retain full control over the search space. We built it to be exceptionally fast, capable of assessing your entire repository without requiring compilable code—a fundamental limitation of standard Abstract Syntax Trees (ASTs). ASTs are great for finding missing commas and memory overflows, but they miss the forest for the trees when generating knowledge graphs. LLMs, on the other hand, suffer from hallucination during large context windows and yield probabilistic, fluctuating answers.

The blAST engine solves this. Because all programming languages utilize keywords and functions, our engine treats code files as text, scanning for these structural anchors to build a deterministic 3D knowledge graph. It seamlessly handles mid-file language switching, assesses the architectural ratio of test files to logic, and extracts invaluable project structure data that ASTs ignore.

Every assumption our system makes has been abstracted into over 300 tunable variables. Think of GitGalaxy as a highly calibrated telescope. You can query the number of active API network nodes, isolate unique external imports, or highlight functions exhibiting extreme cognitive load—all adjusted via custom whitelists and blacklists to eliminate false-positive fatigue. Field-tested on over 1,000 repositories spanning 50+ languages and 250+ extensions, the engine comes equipped with smart defaults ready for immediate deployment.

**Core Codebase Mapping Technology**
* Bypasses LLMs and rigid ASTs.
* Doesn't require code to compile (AST-free).
* Produces full function-to-function call chains.
* Deterministically maps code by 60+ keyword regex profiles (Structural markers, I/O intents, state mutations).
* Regex keyword profiles allow us to classify functions, files, classes, folders and repos.
* Eliminates LLM architectural hallucinations and context window limits.
* Scans 50+ languages, 250+ extensions, fully folder-aware. **([How to add a language in 1 minute and 1 prompt](gitgalaxy/standards/HOW_TO_ADD_LANGUAGE.md))**

**Enterprise Scale & Performance Metrics**
* 100,000 LOC/sec code analysis.
* 0.07 GB/sec raw log ingestion.
* Full-system scans in minutes without data sampling.
* 100% daily system coverage.

**Methodology & Comparative Benchmarks**
GitGalaxy is backed by an academic-grade thesis detailing the equations powering the blAST engine.

* **[Optimum Search Strategies Evolve](https://squid-protocol.github.io/gitgalaxy/03-01-claim-1-search-strategies/):** AST-free mapping. Outperforms rigid parsers and LLM context windows.
* **[Languages are getting easier to regex for meaning and intent](https://squid-protocol.github.io/gitgalaxy/03-02-claim-2-explicitness/):** Quantifies linguistic opacity. Assigns mathematical "trust dampeners" to implicit languages.
* **[All languages have keywords that roughly do the same thing, these can be grouped to make cross-language keyword maps](https://squid-protocol.github.io/gitgalaxy/03-03-claim-3-taxonomy-map/):** Standardizes 50+ languages into a single universal physical framework.
* **[Cross-Language Comparisons of over 1000 repos](https://squid-protocol.github.io/gitgalaxy/03-04-claim-4-comparing-languages/):** Deterministic 1:1 benchmarking of distinct syntax architectures.
* **[Universal File Archetypes by k-means clustering](https://squid-protocol.github.io/gitgalaxy/03-05-claim-5-file-archetypes/):** ML isolation of files into K-means clusters (e.g., "The God Nodes," "Declarative Glue").
* **[Assessing the blAST engines cross-language capbility over 10 different DOOM ports](https://squid-protocol.github.io/gitgalaxy/03-07-claim-7-doom-comparisons/):** Comparative function analysis across 10 distinct DOOM source ports.
* **Mainframe Proven:** Successful from-scratch translation of legacy COBOL monoliths to compiling Spring Boot architectures.

**Data Privacy & On-Premise Deployment**
* 100% air-gapped execution.
* On-premise deployment with zero IP exfiltration risk.
* Zero-trust processing model.

**Installation & Usage**
* Python-based: `pip install gitgalaxy`
* CLI execution
* Outputs forensic JSONs (optimized for AI-agent summary reports) and a native SQLite3 database for robust querying and storage.

> **📖 Official Documentation:** Read the full technical specifications, architecture blueprints, and the Taxonomical Equivalence Map at **[squid-protocol.github.io/gitgalaxy](https://squid-protocol.github.io/gitgalaxy/)**.

---

## Quickstart Guide

### 1. Install

```bash
pip install gitgalaxy
```


### 2. Scan a Repository

Point the GalaxyScope at any local repository or ZIP archive. The engine runs entirely on your local machine—zero data is transmitted.

```bash
galaxyscope /path/to/your/local/repo
```

---

### [GitGalaxy Core Analysis Engine](docs/wiki/01-project-overview.md)
The central blAST engine. It bypasses rigid ASTs using mathematical heuristics to map O(N) multi-dimensional relationships across 50+ languages, managing signal processing, spatial layout, and high-speed SQLite telemetry recording.



## Enterprise Codebase Tools & Use Cases

GitGalaxy operates on a modular Hub-and-Spoke architecture. While the core engine provides the overarching physics and cartography, our specialized toolsets leverage that deterministic graph to execute enterprise-grade operations. The following toolsets provide novel heuristic solutions to several open problems in computing.

### [Automated Legacy Migration: COBOL to Java Spring Boot](gitgalaxy/tools/cobol_to_java/)
A deterministic, high-fidelity translation pipeline. It converts legacy COBOL into fully compiling, modern Spring Boot architectures, mapping memory exactly and scaffolding JPA entities, REST controllers, and Maven builds before utilizing AI to translate isolated business logic.

### [Mainframe Refactoring: COBOL & JCL Optimization](gitgalaxy/tools/cobol_to_cobol/)
A mathematical x-ray suite for sanitizing mainframe monoliths. It safely neutralizes legacy lexical traps, extracts dead "Graveyard" memory, maps topological DAG execution orders, and generates Zero-Trust JCL configurations for modern cloud deployments.

### [Software Supply Chain Security & Pre-Commit Firewalls](gitgalaxy/tools/supply_chain_security/)
Extreme-velocity pre-commit firewalls. Instead of trusting manifest files, it scans physical internals to block steganography, sub-atomic XOR decryption loops, homoglyph typosquatting, and exposed cryptographic vaults before they ever enter your CI/CD pipeline.

### [API Security & Shadow API Detection](gitgalaxy/tools/network_auditing/)
A deterministic mapping tool that hunts undocumented vulnerabilities. It uses structural regex to find active physical routing logic (Express, Spring Boot, FastAPI) and applies set theory against official OpenAPI/Swagger documentation to isolate critical Shadow APIs and outdated Ghost APIs.

### [High-Speed PII Detection & Log Analysis](gitgalaxy/tools/terabyte_log_scanning/)
Unindexed, tactical log analysis operating at 0.07 GB/sec. It streams massive database dumps to deterministically hunt and mask PII (Credit Cards, SSNs, AWS Keys) and uses static architecture maps to prove exact runtime execution frequencies with ASCII time-series histograms.

### [Zero-Trust SBOM Generation & Dependency Auditing](gitgalaxy/tools/compliance/)
A Zero-Trust Software Bill of Materials (SBOM) generator. It refuses to blindly trust `package.json` or `requirements.txt` files, instead locating the physical dependencies on disk, mathematically verifying their entropy and linguistic identity, and generating strict CycloneDX 1.4 JSON reports.

### [AI Agent Guardrails & Codebase Protection](gitgalaxy/tools/ai_guardrails/)
Specialized keyword sensors protecting both your application and your codebase. The AppSec Sensor detects weaponized LLM features (RCE funnels, exfiltration risks), while the Dev Agent Firewall evaluates token mass and blast radius to restrict autonomous coding agents from modifying dangerous over context token-draining files. Helps identify which files need to be chunked to reduce context overload.

  ## Local Browser-Based 3D Codebase Visualization

If you prefer visual analytics, we've built a non-numerical dashboard where each file represents a star, sized and colored according to specific risk metrics.

Simply drag and drop your generated `your_repo_GPU_galaxy.json` file (or a `.zip` of your raw repository) directly into [GitGalaxy.io](https://gitgalaxy.io/). All rendering and scanning happens entirely in your browser's local memory.

![GitGalaxy 3D structural mapping of API exposure and state flux risks in the Apollo 11 legacy codebase](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/apollo-11_state_flux.png)

![GitGalaxy native SQLite3 database schema for AST-free enterprise codebase mapping and cybersecurity auditing](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/sqlite_overview.png)

## Zero-Trust Data Security

Your code never leaves your machine. GitGalaxy performs 100% of its scanning and vectorization locally.

* **No Data Transmission:** Source code is never transmitted to any API, cloud database, or third-party service.
* **Ephemeral Memory Processing:** Repositories are unpacked into a volatile memory buffer (RAM) and are automatically purged when the browser tab is closed.
* **Privacy-by-Design:** Even when using the web-based viewer, the data remains behind the user's firewall at all times.

![GitGalaxy interactive WebGPU data HUD displaying real-time software architecture metrics, forensic analysis, and file-level risk telemetry](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/data_hud.png)

![GitGalaxy Meta Visualizer 3D star map rendering complex software repository structures and K-means clustering archetypes in the browser](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/metavisualizer.png)

## License & Copyright

Copyright (c) 2026 Joe Esquibel

GitGalaxy is released under the PolyForm Noncommercial License 1.0.0. It is completely free for personal use, research, experiment, testing, and hobby projects. Use by educational or charitable organizations is also permitted.

Any commercial use or integration into commercial SaaS products or corporate CI/CD pipelines requires a separate commercial license. Please reach out via gitgalaxy.io to discuss commercial integration.