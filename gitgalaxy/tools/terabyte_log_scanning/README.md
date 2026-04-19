# GitGalaxy: Terabyte Log Scanning & Compliance

[![Velocity](https://img.shields.io/badge/Velocity-0.07_GB%2Fs-00C957.svg)](#)
[![Scale](https://img.shields.io/badge/Tested-10GB%2B_Files-00BFFF.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Single__Pass_Stream-8A2BE2.svg)](#)

Welcome to the **Terabyte Log Scanning Suite**.

When a catastrophic breach occurs, or when auditing decades of unindexed mainframe logs, standard tools fail. `grep` is too rigid and doesn't provide time-series context. Modern SIEMs (like Splunk or ElasticSearch) are incredibly powerful, but they require you to ingest and index the data first—a process that can take hours or days for massive database dumps.

You need an answer *now*. 

This suite provides a much-needed tactical solution: **ultra-high-velocity, unindexed binary log scanning.** Field-tested against raw 10GB+ server dumps, our custom regex physics engine chews through data at an unparalleled **0.07 GB/sec**. It streams data continuously, meaning it never bloats your RAM, allowing you to run it on a standard laptop.

### 🛡️ 1. The PII Data Leak Hunter (`pii_leak_hunter.py`)

A specialized incident response tool designed to find hemorrhaging Personally Identifiable Information (PII) like Credit Cards, SSNs, and AWS API Keys inside massive raw logs or DB dumps.

* **Binary Regex Physics:** We compile our search patterns down to raw bytes (`br'...'`). The engine only decodes a line into UTF-8 if a mathematical hit is explicitly detected, preserving extreme CPU velocity.
* **The Memory Shield (Safe Evidence):** Security teams shouldn't handle toxic data. As the hunter streams the logs, it deterministically masks the payloads (e.g., `VISA-MASKED-1234`, `XXX-XX-1234`) and writes them directly to a safe evidence log.
* **Exfiltration Histograms:** It automatically extracts timestamps and generates dynamically scaled ASCII histograms in the terminal. If a specific minute spikes past the anomaly threshold, it alerts you to a **MASSIVE EXFILTRATION SPIKE**, pinpointing exactly when the database hemorrhage occurred.

### 🔭 2. The Terabyte Log Scanner (`terabyte_log_scanner.py`)

A foundational cartography tool that connects static codebase architecture to physical runtime reality. It parses massive mainframe SMF logs or distributed system traces to prove what code is *actually* executing.

* **The IR State Handshake:** Instead of manually typing keywords, you feed it your GitGalaxy `ir_state.json`. The scanner automatically extracts all known programs in your repository and hunts for them in the logs. 
* **The "0-Hit" Dead Code Rule:** By comparing the static repository map against the runtime logs, it can definitively prove if a compiled program was never actually executed in production.
* **Dynamic Telemetry Sidecar:** It outputs a `dynamic_telemetry.json` sidecar payload containing exact execution counts. This allows the GitGalaxy WebGPU visualizer to overlay real-time traffic heatmaps directly onto your static 3D architectural galaxy!

---

### 🚀 Quickstart: Scanning at Scale

Because these tools operate via single-pass streaming, they require zero setup or database indexing.

**Hunt for PII Leaks in a raw database dump:**
```bash
python3 pii_leak_hunter.py /path/to/massive_database_dump.sql