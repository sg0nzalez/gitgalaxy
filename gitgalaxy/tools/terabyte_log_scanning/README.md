# GitGalaxy: High-Velocity Log Scanning & PII Detection

[![Velocity](https://img.shields.io/badge/Velocity-2%2B_GB%2Fmin-00C957.svg)](#)
[![Scale](https://img.shields.io/badge/Tested-10GB%2B_Files-00BFFF.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Single__Pass_Stream-8A2BE2.svg)](#)

Welcome to the **GitGalaxy Terabyte Log Scanning Suite**.

During an active incident response or catastrophic data breach, standard tools fail. Basic `grep` is too rigid and lacks time-series context. Modern SIEMs (like Splunk or ElasticSearch) are incredibly powerful, but they require you to ingest and index the data first—a process that takes hours or days for a 10GB+ database dump. You need answers immediately.

This suite provides a tactical, pipeline-ready solution: **ultra-high-velocity, unindexed binary streaming.** Running at over 2 GB per minute on standard hardware, our custom stream-processing engine reads data continuously without ever loading the massive file into RAM. This makes it perfect for active breach triage, or as an automated CI/CD pipeline job to sanitize server logs before they are permanently archived.

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

### ⚡ Performance & Anomaly Detection Showcases

#### Showcase A: PII Exfiltration & Automated Masking
To demonstrate incident response capabilities, we streamed a raw **1.00 GB compromised log file**. The PII Leak Hunter chewed through the file in **25.72 seconds**, detecting and actively masking over **420,000 sensitive records**.

The resulting time-series histograms immediately exposed two distinct attack patterns: Customer data (VISA/SSNs) was actively exfiltrated at `14:00`, while infrastructure secrets (AWS Keys) were being scraped on an entirely separate cron schedule at `09:00`.

![PII Leak Hunter Demo](../../../docs/wiki/assets/pii_leak_hunt.gif)

#### Showcase B: Runtime Anomaly Detection
We ran the Terabyte Log Scanner against a raw **2.1GB production stream log**, hunting for specific error and failure signatures. The engine completed the single-pass scan in **30.07 seconds**. 

The dynamically scaled ASCII time-series histograms instantly exposed a massive, coordinated anomaly: a brute-force attack occurring exactly at `14:00` every day, perfectly isolated from millions of lines of background noise.

![Terabyte Log Scanner Demo](../../../docs/wiki/assets/mega_log_scan.gif)

```text
 === TIME-SERIES: ERROR ===
 (Filtering to Top 15 Highest Volume Spikes)
 [2026-04-16 14:00] ███████████████████████████████████████ (5,759 hits)  <-- ANOMALY SPIKE
 [2026-04-27 14:00] ███████████████████████████████████████ (5,753 hits)  <-- ANOMALY SPIKE
 [2026-05-02 14:00] ███████████████████████████████████████ (5,718 hits)  <-- ANOMALY SPIKE
 [2026-05-06 14:00] ███████████████████████████████████████ (5,705 hits)  <-- ANOMALY SPIKE
```

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