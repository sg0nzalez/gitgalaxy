# GitGalaxy: The Core Engine & GalaxyScope Orchestrator

[![Architecture](https://img.shields.io/badge/Architecture-blAST_Engine-00BFFF.svg)](#)
[![Velocity](https://img.shields.io/badge/Velocity-40k%2B_LOC%2Fsec-00C957.svg)](#)
[![CLI](https://img.shields.io/badge/Interface-GalaxyScope_CLI-8A2BE2.svg)](#)

Welcome to the internal source code for the **GitGalaxy Core Engine**. 

This directory contains the central orchestrator—**GalaxyScope**—alongside the core physics, optical routing, and mathematical heuristics that power the entire system. If you are a developer looking to contribute, understand the pipeline, or run the primary CLI, here is your architectural map.

### 🗺️ The Developer Map (How the Pipeline Flows)

When you trigger the `galaxyscope` command, the data flows through these five physical directories:

* **`/core/` (The Frontline):** The optical routing layer. Contains the [Aperture Filter](https://squid-protocol.github.io/gitgalaxy/02-03-aperture-filter/) and [The Prism](https://squid-protocol.github.io/gitgalaxy/02-07-the-prism/), which break down source code into structural signals, separating executable logic from ghost mass (comments) and inert binaries.
* **`/physics/` (The Math):** The heuristics engine. Contains the [Signal Processor](https://squid-protocol.github.io/gitgalaxy/02-09-signal-processing/) and [Neural Auditor](https://squid-protocol.github.io/gitgalaxy/02-19-neural-auditor/), which apply GitGalaxy mathematics to score O(N) complexity, topological blast radius, and state flux without using ASTs.
* **`/recorders/` (The Exporters):** The translation layer. Converts the internal state maps into highly relational [SQLite Databases](https://squid-protocol.github.io/gitgalaxy/02-21-record-keeper/), AI-agent JSON tickets, and the final 3D WebGPU payload.
* **`/security/` (The Sentinel):** The zero-trust validation layer. Contains the [Security Lens](https://squid-protocol.github.io/gitgalaxy/02-06-security-lens/) responsible for intercepting embedded malware, hardcoded secrets, and logic bombs on the fly.
* **`/tools/` (The Spokes):** The enterprise automation layer. Contains specialized controllers for CI/CD pipelines—like the [Supply Chain Firewall](https://squid-protocol.github.io/gitgalaxy/04-03-supply-chain-firewall/) and [PII Leak Hunter](https://squid-protocol.github.io/gitgalaxy/04-06-pii-leak-hunter/)—that consume the core engine's telemetry. **These specialized tools power our official [Zero-Trust DevSecOps GitHub Action](../github-action-read-me.md).**

---

### ⚡ Performance Showcase: NVDA (NonVisual Desktop Access)

To demonstrate the GalaxyScope orchestrator's capability on complex, cross-language system architecture, we unleashed it on **NVDA**, the open-source Windows screen reader. 

Because NVDA relies heavily on bridging Python application logic with low-level C++ system hooks, it requires advanced polyglot dependency mapping. The blAST engine successfully parsed the mixed-language architecture, analyzing **236,754 lines of code** in just **5.59 seconds** (a velocity of 42,357 LOC/sec). 

Crucially, during the import resolution phase, the Air-Gapped Dependency Radar successfully intercepted a structural naming collision (`fstream` vs `sstream`), proving the real-time typosquatting defenses are fully operational without relying on cloud APIs.

> **Note on False Positives:** Because `fstream` and `sstream` are both standard C++ libraries, this specific flag is a false positive. To prevent the engine from halting on trusted internal libraries, contributors can whitelist them by adding them to the global `approved_imports.json` registry (see [GitGalaxy Config](https://squid-protocol.github.io/gitgalaxy/06-01-gitgalaxy-config/)).

![NVDA Processing Demo](../../docs/wiki/assets/nvda_processing.gif)

```text
[INFO] PASS_1.5: Running Air-Gapped Typosquatting & Dependency Confusion Radar...
[CRITICAL] 🚨 TYPOSQUATTING DETECTED: 'fstream' in nvdaHelper/vbufBase/storage.cpp closely matches anchor 'sstream'!
[WARNING] Intercepted 1 typosquatting attempts via repository baseline analysis.
...
[INFO] --- MISSION_SUCCESS: 849 files mapped in 5.59s ---
[INFO] --- ENGINE_TELEMETRY: Processed 236,754 lines of code at 42,357 LOC/s ---
```

---

### 🛠️ Local Development & GalaxyScope Execution

If you are modifying the internal physics or optical routing, it is highly recommended to install the package in editable mode so your CLI commands instantly reflect your local code changes.

From the **root directory** of the repository, run:
```bash
pip install -e .
```

**Important:** GitGalaxy contains an embedded commercial licensing guardrail. To prevent a 5-second execution delay while testing your code locally, you must export the Community Free Tier key into your development environment before running the orchestrator:
```bash
export GITGALAXY_LICENSE_KEY="COMMUNITY_FREE_TIER"
```

Once installed and the key is set, you can trigger the main orchestrator globally from your terminal. This command runs the full [Data Pipeline](https://squid-protocol.github.io/gitgalaxy/02-01-pipeline-overview/) and outputs the final artifact.
```bash
galaxyscope /path/to/test/repo --debug
```

Before submitting a Pull Request, ensure your changes do not skew the core baseline risk equations by running the test suite:
```bash
python3 -m unittest discover tests/
```

---
### 🌌 Deep Dive into the Pipeline Architecture
To fully understand how GalaxyScope processes data, maps files, and applies risk exposures, explore the official documentation:

* 📖 **[GalaxyScope CLI Reference](https://squid-protocol.github.io/gitgalaxy/01-02-galaxyscope-cli-reference/)** (Flags, outputs, and behaviors)
* 📖 **[The Data Pipeline Overview](https://squid-protocol.github.io/gitgalaxy/02-01-pipeline-overview/)** (Step-by-step breakdown of the runtime)
* 📖 **[Risk Exposures & Methodology](https://squid-protocol.github.io/gitgalaxy/08-01-methodology/)** (The math behind the heuristics)
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)**
