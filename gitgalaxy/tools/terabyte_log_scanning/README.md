# GitGalaxy: High-Velocity Log Scanning & PII Detection

[![Velocity](https://img.shields.io/badge/Velocity-4%2B_GB%2Fmin-00C957.svg)](#)
[![Scale](https://img.shields.io/badge/Tested-10GB%2B_Files-00BFFF.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Single__Pass_Stream-8A2BE2.svg)](#)

Welcome to the **GitGalaxy Terabyte Log Scanning Suite**.

During an active incident response or catastrophic data breach, standard tools fail. Basic `grep` is too rigid and lacks time-series context. Modern SIEMs (like Splunk or ElasticSearch) are incredibly powerful, but they require you to ingest and index the data first—a process that takes hours or days for a 10GB+ database dump. You need answers immediately.

This suite provides a tactical, pipeline-ready solution: **ultra-high-velocity, unindexed binary streaming.** Running at over 4 GB per minute (70+ MB/sec) on standard laptop hardware, our custom stream-processing engine reads data continuously. It never loads the massive file into RAM. This makes it perfect for active breach triage, or as an automated CI/CD pipeline job to sanitize server logs before they are permanently archived.

### 1. The PII Data Leak Hunter (`pii_leak_hunter.py`)

A specialized incident response tool designed to find hemorrhaging Personally Identifiable Information (Credit Cards, SSNs, AWS API Keys) inside massive, raw data dumps.

* **Binary-Level Regex Evaluation:** Compiles structural patterns to raw bytes for extreme CPU efficiency.
* **Automated Data Masking:** Redacts toxic payloads before writing to evidence logs.
* **Exfiltration Histograms:** Generates terminal ASCII charts to pinpoint exact breach minutes.
* **Pipeline Sanitization:** Runs automatically in CI/CD to block PII log archiving.

### 2. The Terabyte Log Scanner (`terabyte_log_scanner.py`)

A runtime execution tracer that connects static codebase architecture to physical runtime reality. It parses massive mainframe SMF logs or distributed traces to prove what code is actually executing.

* **Intermediate Representation (IR) Ingestion:** Ingests static repository maps to hunt known compiled programs in the logs.
* **Execution Verification:** Proves exact runtime execution frequencies in production environments.
* **Zero-Hit Dead Code:** Mathematically proves if compiled legacy code is truly abandoned.
* **Dynamic Telemetry:** Outputs sidecar JSON for 3D WebGPU traffic heatmaps.

---

### 🚀 Quickstart: Scanning at Scale

Because these tools operate via single-pass streaming, they require zero environment setup, database indexing, or heavy JVMs. 

**Hunt for PII Leaks in a raw database dump:**
```bash
python3 pii_leak_hunter.py /path/to/massive_database_dump.sql
```

**Stream logs to prove runtime execution of static code:**
```bash
python3 terabyte_log_scanner.py /path/to/production.log --ir ../core/ir_state.json
```

---
### 🌌 Powered by the blAST Engine (Bypassing LLMs and ASTs)
This tool is a modular enterprise integration within the broader GitGalaxy architecture. It is driven by our custom mathematical heuristics engine, capable of processing multi-dimensional data at extreme velocity without requiring rigid ASTs or cloud APIs. Read the official documentation to see the structural methodologies powering this high-speed log analysis:

* 📖 **[PII Leak Hunter Architecture](../../../docs/wiki/04-06-pii-leak-hunter.md)**
* 📖 **[Terabyte Log Scanner Mechanics](../../../docs/wiki/04-07-terabyte-log-scanner.md)**
* 📖 **[Time-Series Execution Histograms](../../../docs/wiki/08-25-execution-histograms.md)**
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)**