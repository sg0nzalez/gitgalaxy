# GitGalaxy: High-Velocity Log Scanning & PII Detection

[![Velocity](https://img.shields.io/badge/Velocity-2%2B_GB%2Fmin-00C957.svg)](#)
[![Scale](https://img.shields.io/badge/Tested-10GB%2B_Files-00BFFF.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Single__Pass_Stream-8A2BE2.svg)](#)

During an active incident response or catastrophic data breach, standard tools fail. Basic `grep` lacks time-series context. Modern SIEMs (Splunk, ElasticSearch) require you to ingest and index data first—taking hours or days for massive database dumps.

This suite provides a tactical, pipeline-ready solution: **ultra-high-velocity, unindexed binary streaming.** Running at over 2 GB per minute, our custom stream-processing engine reads data continuously without loading massive files into RAM. Perfect for active breach triage or automated CI/CD pipeline sanitization.

---

## Part 1: The PII Data Leak Hunter (`pii-leak-hunter`)
[📖 Official Documentation](https://squid-protocol.github.io/gitgalaxy/04-06-pii-leak-hunter/)

A specialized incident response tool. Designed to find hemorrhaging Personally Identifiable Information inside massive, raw data dumps.

**How it works:**
* **Binary-Level Regex:** Compiles structural patterns to raw bytes. Extreme CPU efficiency.
* **Automated Masking:** Redacts toxic payloads before writing to safe evidence logs.
* **Exfiltration Histograms:** Generates ASCII charts. Pinpoints exact breach minutes.

**Performance Showcase:** Streamed a raw **1.00 GB compromised log file**. Completed in **25.72 seconds**. Detected and actively masked over **420,000 sensitive records**. Immediately exposed two distinct attack vectors (Customer data at 14:00, AWS Keys at 09:00).

### Targeted Patterns
The stream engine currently bypasses standard indexing to hunt and actively mask:
* **VISA** (Credit Cards)
* **MASTERCARD** (Credit Cards)
* **SSN** (US Social Security Numbers)
* **AWS_KEY** (AKIA, ASIA, AGPA, etc.)

### Quickstart & Integration
**Local CLI Execution:**
By default, the tool saves the masked evidence log in the same directory as the target.
```bash
pii-leak-hunter /path/to/massive_database_dump.sql
```

**Using the `--out` Flag:**
Route the safe, masked telemetry to a secure directory for analysis. 
```bash
pii-leak-hunter /path/to/production.log --out /var/secure_logs/
```

**GitHub Actions CI/CD Integration:**
Automate sanitization before archiving logs.
```yaml
      - name: Run PII Leak Hunter
        uses: squid-protocol/gitgalaxy@main
        with:
          tool: 'pii-leak-hunter'
          target: './logs/production_dump.sql'
          args: '--out ./sanitized_logs/'
```

---

## Part 2: The Terabyte Log Scanner (`terabyte-log-scanner`)
[📖 Official Documentation](https://squid-protocol.github.io/gitgalaxy/04-07-terabyte-log-scanner/)

A runtime execution tracer. Connects static codebase architecture to physical runtime reality. Parses massive mainframe SMF logs or distributed traces to prove what code actually executes.

**How it works:**
* **Single-Pass Streaming:** Never loads the full file into RAM.
* **Execution Verification:** Proves exact runtime execution frequencies.
* **Zero-Hit Detection:** Mathematically proves if compiled legacy code is abandoned.
* **Dynamic Sidecars:** Outputs telemetry JSON for 3D WebGPU traffic heatmaps.

**Performance Showcase:**
Ran against a raw **2.1GB production stream log**. Completed single-pass scan in **30.07 seconds**. Dynamically scaled ASCII histograms instantly exposed a massive brute-force anomaly isolated from background noise:

```text
 === TIME-SERIES: ERROR ===
 (Filtering to Top 15 Highest Volume Spikes)
 [2026-04-16 14:00] ███████████████████████████████████████ (5,759 hits)  <-- ANOMALY SPIKE
 [2026-04-27 14:00] ███████████████████████████████████████ (5,753 hits)  <-- ANOMALY SPIKE
 [2026-05-02 14:00] ███████████████████████████████████████ (5,718 hits)  <-- ANOMALY SPIKE
```

### Input Methods: Manual vs. Automated
The tool requires one of two input methods to function. It will not run without a target list.

**1. Manual Mode (`-k` or `--keywords`)**
Best for quick, grep-style tactical hunts. Supply a space-separated list of targets.
```bash
terabyte-log-scanner /path/to/production.log -k ERROR TIMEOUT "DATA EXCEPTION"
```

**2. Automated Pipeline Mode (`--input_state`)**
Best for CI/CD modernization pipelines. Supply a GitGalaxy Intermediate Representation (IR) JSON file. The script will automatically extract the targets from the `known_programs` array to hunt for dead code.
```bash
terabyte-log-scanner /path/to/production.log --input_state ../core/ir_state.json
```

*Required JSON Schema for Automated Mode:*
```json
{
  "analysis": {
    "known_programs": ["PROGRAM1", "PROGRAM2"]
  }
}
```

---
### 🌌 Powered by the blAST Engine (Bypassing LLMs and ASTs)
This suite is driven by our custom deterministic heuristics engine. It processes multi-dimensional data at extreme velocity without requiring rigid ASTs or hallucinating LLMs. 

* 📖 **[The blAST Paradigm (ASTs vs LLMs)](https://squid-protocol.github.io/gitgalaxy/01-03-the-blast-paradigm/)**
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)**