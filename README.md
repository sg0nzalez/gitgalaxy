# GitGalaxy

[![PyPI version](https://badge.fury.io/py/gitgalaxy.svg)](https://badge.fury.io/py/gitgalaxy)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: PolyForm Noncommercial](https://img.shields.io/badge/License-PolyForm%20Noncommercial-blue.svg)](https://polyformproject.org/licenses/noncommercial/1.0.0/)

[![Engine](https://img.shields.io/badge/Engine-blAST-8A2BE2.svg)](#)
[![Velocity](https://img.shields.io/badge/Velocity-100k+_LOC%2Fs-00C957.svg)](#)
[![Analysis](https://img.shields.io/badge/Analysis-Static_Analysis-00BFFF.svg)](#)
[![Threat Hunting](https://img.shields.io/badge/Threat_Hunting-Behavioral-FF4500.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Zero__Trust-teal.svg)](#)
[![Coverage](https://img.shields.io/badge/Coverage-50%2B_Languages-00C957.svg)](#)

[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0-brightgreen.svg)](https://pypi.org/project/gitgalaxy/)
[![Airgap Ready](https://img.shields.io/badge/Security-Airgap_Ready-teal.svg)](#)
[![Downloads](https://static.pepy.tech/badge/gitgalaxy)](https://pepy.tech/project/gitgalaxy)

### **Whole-Repository Understanding & DevSecOps Topology**

Most tools analyze code line-by-line. GitGalaxy maps the entire architectural ecosystem. By tracking the exact flow of information across network dependencies, identifying local folder constraints, and natively recognizing 50+ languages—even mid-file—GitGalaxy provides a deterministic, macro-level view of your software's structural architecture.

### Scanning Apollo-11 with the blAST Engine

![GitGalaxy CLI Scan](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/apollo11_scan.gif)

**Why we built a custom parsing engine:**
Standard Abstract Syntax Trees (ASTs) are excellent for finding syntax errors, but they require fully compilable code and struggle to map massive-scale information flow efficiently. LLMs suffer from context window saturation and yield probabilistic, fluctuating answers.

The **blAST (Bypassing LLMs and ASTs) engine** solves this by adopting the search philosophy of computational biology. Just as genomic BLAST sequencing scans billions of DNA base pairs to identify protein domains without "executing" the organism, GitGalaxy blAST sequences raw source code to identify **Structural Signatures**. 

Instead of mapping gene starts and genetic mutations, the engine deterministically sequences coding intent, execution boundaries, and architectural risk exposures. This enables the engine to build a deterministic 3D knowledge graph of your entire repository in linear O(N) time without ever requiring the code to compile. It instantly calculates the ratio of test boundaries to core logic, maps network blast radiuses, and extracts the vital project structure data that rigid linters ignore. 

*(Note: Raw structural signatures are simply data points. True risk exposures in GitGalaxy are calculated metrics derived from these structural alignments combined with topological network gravity).*

Think of GitGalaxy as a highly calibrated macro-analyzer for codebase risk. Every assumption the system makes is abstracted into over 300 tunable variables. You can query active API nodes, isolate supply chain threats, or highlight functions exhibiting extreme cognitive load—all adjusted via custom thresholds to eliminate false-positive fatigue. Field-tested on over 1,000 repositories, the engine comes equipped with enterprise-grade defaults ready for immediate CI/CD deployment.

**Core Repository Mapping Technology**
* **Heuristic Structural Alignment:** Bypasses LLMs and rigid ASTs. Sequences code in raw text without requiring it to compile.
* **Deterministic Sequencing:** Maps code using 60+ bounded structural signatures (I/O intents, state mutations, execution wrappers) exactly like sequencing genetic markers.
* **Taxonomical Classification:** These structural profiles allow us to classify functions, files, classes, and entire repositories into distinct architectural archetypes.
* **Topological Cartography:** Produces full network mapping via imports and dynamic execution markers.
* **Zero-Hallucination:** Eliminates LLM architectural hallucinations and context window limits by relying strictly on mathematical constraints.
* **Polyglot Sequencing:** Scans 50+ languages, 250+ extensions, fully folder-aware. **([How to add a language in 1 minute and 1 prompt](https://github.com/squid-protocol/gitgalaxy/blob/main/gitgalaxy/standards/how_to_add_a_language.md))**

**Enterprise Scale & Performance Metrics**
* **Active Pipeline Integration:** Over 11,000 PyPI downloads, driven heavily by automated CI/CD security sweeps and zero-trust DevSecOps workflows.
* **Production Tested:** Backed by an active early-adopter community on GitHub driving real-world issue resolution, architectural forks, and continuous engine hardening.
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
* **[Universal File Archetypes by k-means clustering](https://squid-protocol.github.io/gitgalaxy/03-05-claim-5-file-archetypes/):** ML isolation of files into K-means clusters.
* **[Mainframe Proven: 100% CI/CD Translation Success Rate](https://github.com/squid-protocol/gitgalaxy/tree/main/examples/ibm_cics_translation):** Flawless architectural translation of 27 distinct legacy COBOL repositories (including IBM CICS benchmark apps) into compiling Java Spring Boot environments.

**Data Privacy & On-Premise Deployment**
* 100% air-gapped execution.
* On-premise deployment with zero IP exfiltration risk.
* Zero-trust processing model.

**Installation & Usage**
* Python-based: `pip install gitgalaxy`
* CLI execution
* CI/CD Integration: Native **[GitHub Action](https://github.com/squid-protocol/gitgalaxy/blob/main/github-action-readme.md)** available for zero-trust DevSecOps pipelines.
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

### 3. GitHub Actions CI/CD Integration

GitGalaxy can be integrated directly into your GitHub Actions pipeline for automated DevSecOps auditing, Zero-Trust SBOM generation, or Pre-Commit firewalls. 

**🚀 [View the Full GitHub Action Integration Guide](https://github.com/squid-protocol/gitgalaxy/blob/main/github-action-readme.md)**

Check out our comprehensive guide to set up the **Pipeline Architecture** (Parallel Enforcement & Autonomous Reporting). It covers all available inspection tools, AI guardrails, and advanced configuration options like our hyper-sensitive `--paranoid` threat-hunting mode.

*Minimal Example (Running a single inspection tool):*
```yaml
name: GitGalaxy Security Audit

on:
  pull_request:
    branches: [ "main" ]

jobs:
  gitgalaxy-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Run GitGalaxy Supply Chain Firewall
        uses: squid-protocol/gitgalaxy@main
        with:
          tool: 'supply-chain-firewall' # View the Integration Guide for the full tool directory
          target: '.'
```

---

### [GitGalaxy Core Analysis Engine](https://github.com/squid-protocol/gitgalaxy/blob/main/docs/wiki/01-project-overview.md)
The central blAST engine. It bypasses rigid ASTs using mathematical heuristics to map O(N) multi-dimensional relationships across 50+ languages, managing signal processing, spatial layout, and high-speed SQLite telemetry recording.



## Enterprise Codebase Tools & Use Cases

GitGalaxy operates on a Decoupled Architecture. While the core engine provides the overarching structural mechanics and topological mapping, our specialized Decoupled Execution Controllers leverage that deterministic graph to execute enterprise-grade operations.

### [Automated Legacy Migration: COBOL to Java Spring Boot](https://github.com/squid-protocol/gitgalaxy/tree/main/gitgalaxy/tools/cobol_to_java/)
A deterministic, high-fidelity translation pipeline. It converts legacy COBOL into fully compiling, modern Spring Boot architectures, mapping memory exactly and scaffolding JPA entities, REST controllers, and Maven builds before utilizing AI to translate isolated business logic.
* **Proven Metric:** Achieved a perfect 27/27 Maven compile success rate across a batch test of distinct legacy repos.
* **Verify for Yourself:** [Inspect the raw outputs of the IBM CICS Application Translation here.](https://github.com/squid-protocol/gitgalaxy/tree/main/examples/ibm_cics_translation/)

![Java Forge & Batch Test](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/java_forge_and_batch_test.gif)

### [Mainframe Refactoring: COBOL & JCL Optimization](https://github.com/squid-protocol/gitgalaxy/tree/main/gitgalaxy/tools/cobol_to_cobol/)
An analytical suite for sanitizing mainframe monoliths. It safely neutralizes legacy lexical traps, extracts dead execution memory, maps topological DAG execution orders, and generates Zero-Trust JCL configurations for modern cloud deployments.
* **Proven Metric:** The dead-code extraction engine removed over 6,700 lines of dead execution blocks and orphaned variables from the standard IBM CICS benchmark app in seconds.

### [Software Supply Chain Security & Pre-Commit Firewalls](https://github.com/squid-protocol/gitgalaxy/tree/main/gitgalaxy/tools/supply_chain_security/)
Extreme-velocity pre-commit firewalls. Instead of trusting manifest files, it scans physical internals to block steganography, byte-level XOR decryption loops, homoglyph typosquatting, and exposed cryptographic vaults before they ever enter your CI/CD pipeline. **[Deploy directly via our GitHub Action](https://github.com/squid-protocol/gitgalaxy/blob/main/github-action-readme.md).**

### [Zero-Trust SBOM Generation & Dependency Auditing](https://github.com/squid-protocol/gitgalaxy/tree/main/gitgalaxy/tools/compliance/)
A Zero-Trust Software Bill of Materials (SBOM) generator. It refuses to blindly trust `package.json` or `requirements.txt` files, instead locating the physical dependencies on disk, mathematically verifying their entropy and linguistic identity, and generating strict CycloneDX 1.4 JSON reports.
* **Proven Metric:** Successfully mapped and mathematically verified the physical internals of 170 unique Go modules inside the local Kubernetes repository.

### [API Security & Shadow API Detection](https://github.com/squid-protocol/gitgalaxy/tree/main/gitgalaxy/tools/network_auditing/)
A deterministic mapping tool that hunts undocumented vulnerabilities. It uses structural regex to find active physical routing logic (Express, Spring Boot, FastAPI) and applies set theory against official OpenAPI/Swagger documentation to isolate critical Shadow APIs and outdated Ghost APIs.

### [High-Speed PII Detection & Log Analysis](https://github.com/squid-protocol/gitgalaxy/tree/main/gitgalaxy/tools/terabyte_log_scanning/)
Unindexed, tactical log analysis operating at 0.07 GB/sec. It streams massive database dumps to deterministically hunt and mask PII (Credit Cards, SSNs, AWS Keys) and uses static architecture maps to prove exact runtime execution frequencies with ASCII time-series histograms.

### [AI Agent Guardrails & Codebase Protection](https://github.com/squid-protocol/gitgalaxy/tree/main/gitgalaxy/tools/ai_guardrails/)
Specialized keyword sensors protecting both your application and your codebase. The AppSec Sensor detects weaponized LLM features (RCE funnels, exfiltration risks), while the Dev Agent Firewall evaluates token mass and blast radius to restrict autonomous coding agents from modifying dangerous or context-token-draining files. Helps identify which files need to be chunked to reduce context overload.

## Local Browser-Based 3D Codebase Visualization

If you prefer visual analytics, we've built a topological dashboard where each file represents a node, sized and colored according to specific risk metrics.

Simply drag and drop your generated `your_repo_GPU_galaxy.json` file (or a `.zip` of your raw repository) directly into [GitGalaxy.io](https://gitgalaxy.io/). All rendering and scanning happens entirely in your browser's local memory.

### 🔭 Watch GitGalaxy in Action

**Mapping 3.2 Million Lines of C++ in 11 Seconds | OpenCV** [![OpenCV Demo](https://img.youtube.com/vi/3ScQCSUBdZw/maxresdefault.jpg)](https://youtu.be/3ScQCSUBdZw)

![GitGalaxy Topological Visualizer 3D graph rendering complex software repository structures and K-means clustering archetypes in the browser](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/metavisualizer.png)

## Zero-Trust Data Security

Your code never leaves your machine. GitGalaxy performs 100% of its scanning and vectorization locally.

* **No Data Transmission:** Source code is never transmitted to any API, cloud database, or third-party service.
* **Ephemeral Memory Processing:** Repositories are unpacked into a volatile memory buffer (RAM) and are automatically purged when the browser tab is closed.
* **Privacy-by-Design:** Even when using the web-based viewer, the data remains behind the user's firewall at all times.

## ⚖️ Licensing & Usage

Copyright (c) 2026 Joe Esquibel

GitGalaxy is distributed under the **PolyForm Noncommercial License 1.0.0**. 

### 🎓 Community Free Tier (Academic, Research, & Hobbyist)
We are deeply committed to the open-source and academic communities. If you are using GitGalaxy for personal projects, academic research, or non-commercial development, the engine is 100% free to use.

To suppress the commercial licensing delays in your terminal or personal CI/CD pipelines, simply set the following environment variable:

```bash
export GITGALAXY_LICENSE_KEY="COMMUNITY_FREE_TIER"
```

### 🏢 Commercial & Enterprise Use
Running GitGalaxy in corporate environments, proprietary codebases, or commercial CI/CD pipelines requires an enterprise license. Unlicensed corporate pipelines will experience intentional execution friction, and attempting to use the Community Free Tier key in a corporate environment will trigger explicit non-compliance warnings in your audit logs.

To acquire a zero-trust commercial key for your organization and ensure clean compliance logs, please contact: **joe@gitgalaxy.io**