# GitGalaxy Tools: Supply Chain Security Suite

This directory contains the CI/CD gating mechanisms, pre-commit hooks, and dependency validation engines for GitGalaxy.

Standard software composition analysis (SCA) tools inherently possess a critical blind spot: they act as manifest readers. They scan `package.json` or `requirements.txt` and cross-reference those declarations against known CVE databases. Modern supply chain compromises bypass this entirely by omitting malicious payloads from the manifest declarations.

The GitGalaxy Supply Chain Security Suite operates on a strict Zero-Trust model. Powered by the core blAST Engine, these tools bypass manifest assumptions and physically scan the structural mechanics of every dependency file on disk before it enters the build pipeline.

## Architectural Philosophy & Defensive Engineering

To intercept zero-day supply chain compromises, steganography, and credential leaks without introducing developer friction or CI/CD bottlenecks, these modules employ several high-velocity defensive paradigms:

### 1. Zero-Trust Dependency Verification
Manifests can be spoofed. The `supply_chain_firewall.py` ignores dependency declarations and instead parses the actual, physical `import` and `require` statements within the downloaded `node_modules` or `venv` directories. It maps this physical execution graph against strict enterprise allowlists, instantly flagging unauthorized network requests, nested typosquatting, or anomalous I/O hooks.

### 2. High-Velocity Secret Detection
Pre-commit hooks must operate in milliseconds, or developers will bypass them. `vault_sentinel.py` utilizes a two-tier approach. Tier 0 performs instant O(1) path evaluation, blocking high-risk file extensions (e.g., `.pem`, `id_rsa`) before disk I/O occurs. Tier 1 executes deep content scanning to isolate exposed cryptographic keys and SaaS tokens—even if they are buried in commented-out dead code.

### 3. Heuristic Binary Triage (Zero-Cloud Execution)
Advanced compromises often hide executable logic inside seemingly inert data blobs. `binary_anomaly_detector.py` performs localized binary triage without uploading artifacts to cloud sandboxes. It validates structural magic bytes to catch scripts disguised as images, and utilizes mathematically optimized Shannon Entropy calculations to flag highly obfuscated or packed payloads (Entropy > 4.8).

---

## Core Modules (The Sentinels)

Each file in this directory acts as a discrete, specialized firewall for your development and deployment pipelines:

* **`supply_chain_firewall.py` (Dependency Integrity Gate):** Scans the physical execution graph of downloaded dependencies. It cross-references the core engine's structural telemetry to block packages exhibiting unauthorized behavioral heuristics (e.g., unexpected data injection routines, execution of OS-level processes during installation).
* **`binary_anomaly_detector.py` (Binary Anomaly Detector):** Designed for rapid triage of binaries and obfuscated files. It detects embedded execution headers hidden inside static data, validates file extension integrity, and flags extreme cryptographic entropy indicating packed malware or byte-level obfuscation loops.
* **`vault_sentinel.py` (Vault Sentinel):** A hyper-speed pre-commit hook strictly for localized credential detection. It enforces Tier 0 path blocking and executes deep-content cryptographic scans to prevent hardcoded cloud keys, database passwords, and API tokens from entering version control.

---

## ⚡ Performance Showcases

#### Showcase A: Vault Sentinel (Secret Detection)
To prove this engine operates fast enough to be a synchronous pre-commit hook without frustrating developers, we executed the **Vault Sentinel** against the massive **tRPC** TypeScript monorepo. 

The engine evaluated 871 files and performed deep-content cryptographic scans on 695 of them in **0.53 seconds** (processing over 1,300 files per second). It successfully intercepted 7 exposed environment files and caught a hardcoded API key before the commit could execute.

![Vault Sentinel Demo](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/vault_sentinel_scan.gif)

#### Showcase B: Binary Anomaly Detector (Malware & Binary Triage)
To test binary detection, we ran the **Binary Anomaly Detector** against **pwntools**, an exploit development framework containing actual compiled binaries and shellcode.

The engine processed the repository at a velocity of **2,825 files per second**. By reading the raw physical bytes rather than trusting file extensions, it instantly detected 13 embedded `ELF` execution headers hidden inside the source tree.

![Binary Anomaly Detector Demo](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/xray_inspector_scan.gif)

```text
===========================================================================
 BINARY ANOMALY DETECTOR: SCAN SUMMARY
===========================================================================
 Files Evaluated    : 95
 Files Deep Scanned : 95
 Time Elapsed       : 0.03 seconds
 Scan Velocity      : 2,825 files/sec
---------------------------------------------------------------------------
 Anomalies Detected : 13
---------------------------------------------------------------------------
 [BLOCKING ACTION] 13 structural anomalies detected. Failing pipeline.
```

#### Showcase C: Supply Chain Firewall (Infrastructure-as-Code Audit)
To prove the firewall can handle diverse polyglot ecosystems without throwing false positives, we ran it against the **Terraform** repository. 

The engine parsed 1,834 files at a velocity of **436 files per second**. It successfully verified the integrity of the dependency tree, identified 54 unknown packages for audit, and cleared the build without tripping any false alarms on standard Go/HCL syntax.

![Supply Chain Firewall Demo](https://raw.githubusercontent.com/squid-protocol/gitgalaxy/main/docs/wiki/assets/terraform_firewall_scan.gif)

```text
===========================================================================
 SUPPLY CHAIN FIREWALL: SCAN SUMMARY
===========================================================================
 Mode               : Audit (Allow Whitelist + Unknown, Exclude Blacklist)
 Files Deep Scanned : 1,834
 Scan Velocity      : 436 files/sec
---------------------------------------------------------------------------
 Approved Packages    : 0
 Banned Packages      : 0
 Unknown Packages     : 54
---------------------------------------------------------------------------
 Active Threats       : 0
---------------------------------------------------------------------------
 [SUCCESS] Dependency supply chain is clean.
```

---

## CI/CD & Pre-Commit Integration

These sentinels are designed to be wired directly into your Git workflows to fail compromised builds autonomously.

**Local Pre-Commit Hook Integration:**
To run the Vault Sentinel automatically before every commit, add this configuration to your `.pre-commit-config.yaml` file:

```yaml
repos:
  - repo: local
    hooks:
      - id: gitgalaxy-vault-sentinel
        name: GitGalaxy Vault Sentinel
        entry: vault-sentinel
        language: system
        types: [text]
        pass_filenames: true
```

**GitHub Actions Integration:**
You can deploy these sentinels directly into your CI/CD pipeline using the official [GitGalaxy GitHub Action](https://github.com/marketplace/actions/gitgalaxy-scanner).

```yaml
name: GitGalaxy Zero-Trust Audit
on: [pull_request]

jobs:
  gitgalaxy-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run GitGalaxy Supply Chain Firewall
        uses: squid-protocol/gitgalaxy@v2.0.7
        with:
          tool: 'supply-chain-firewall'
```

---

## 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://squid-protocol.github.io/gitgalaxy/), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[GitGalaxy Official Documentation](https://squid-protocol.github.io/gitgalaxy/)** - Deep dives into the mathematics and pipeline architecture.
* 🔭 **[GitGalaxy Visualizer](http://gitgalaxy.io/)** - Render your codebase locally in 3D using WebGPU.
* 📖 **[The blAST Paradigm Wiki](https://squid-protocol.github.io/gitgalaxy/docs/wiki/01-03-the-blast-paradigm/)** - The academic and structural thesis backing the engine.
* ⚙️ **[Language Calibration Standards](https://github.com/squid-protocol/gitgalaxy/blob/main/gitgalaxy/standards/how_to_add_a_language.md)** - Guide to extending the comparative lexical taxonomy.