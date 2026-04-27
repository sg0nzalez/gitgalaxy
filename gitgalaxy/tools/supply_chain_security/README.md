# GitGalaxy: Supply Chain Security & Pre-Commit Sentinels

[![Integration](https://img.shields.io/badge/Integration-CI%2FCD_Ready-00C957.svg)](#)
[![Accuracy](https://img.shields.io/badge/Accuracy-Internal_File_Scanning-00BFFF.svg)](#)
[![Defense](https://img.shields.io/badge/Defense-Zero__Trust-FF4500.svg)](#)

Welcome to the **GitGalaxy Supply Chain Security Suite**.

Standard security scanners ([like Snyk, Dependabot, or Trivy](https://squid-protocol.github.io/gitgalaxy/04-00-security_landscape/)) have a massive blind spot: they read your `package.json` or `requirements.txt` and check those names against CVE databases. They act as manifest readers, never looking inside the actual downloaded files. 

Modern attackers (like the **XZ-Utils** or **Glassworm** campaigns) exploit this. They don't announce their malware in a manifest.

GitGalaxy operates differently. Powered by the [blAST Engine](https://squid-protocol.github.io/gitgalaxy/01-03-the-blast-paradigm/), we bypass compilation and rigid ASTs entirely. We scan the physical internals of every dependency file at extreme velocities (100k+ LOC/sec) before it enters your system, identifying threats via minimal keyword permutations rather than waiting for a CVE to be published.

### 🛡️ What We Stop
We provide highly effective, zero-trust defense against structural threats:
* **Hidden Executables:** Steganography and [XZ-Utils attack patterns](https://squid-protocol.github.io/gitgalaxy/04-05-binary-anomaly-detector/).
* **Malicious Typosquatting:** Unicode homoglyphs tricking developer imports.
* **Encrypted Payloads:** Sub-atomic XOR decryption loops hiding inside utility files.
* **Hostile I/O:** Shadow imports establishing covert outbound connections.
* **API Drift:** Network sockets hidden inside undocumented [Shadow APIs](https://squid-protocol.github.io/gitgalaxy/04-01-full-api-network-map/).

---

### 🛠️ The Sentinel Tools

Wired directly into your Git Pre-Commit hooks or CI/CD pipelines, these sentinels act as a physical firewall to fail poisoned builds early.

#### 1. [The Supply Chain Firewall](https://squid-protocol.github.io/gitgalaxy/04-03-supply-chain-firewall/) (`supply-chain-firewall`)
Scans massive `node_modules` or `venv` directories in seconds.
* **Zero-Trust Verification:** Checks every physical `import` against strict allowlists.
* **Behavioral Heuristics:** Scans for tainted data injection routines and parasitic logic.

#### 2. [Zero-Trust SBOM Generator](https://squid-protocol.github.io/gitgalaxy/04-02-sbom-generator/) (`sbom-generator`)
Standard SBOMs blindly trust manifests. Ours doesn't.
* **Physical Audits:** Extracts and micro-scans files from every downloaded dependency.
* **CycloneDX 1.4:** Generates compliant manifests injected with physical threat telemetry.

#### 3. [X-Ray Inspector](https://squid-protocol.github.io/gitgalaxy/04-05-binary-anomaly-detector/) (`xray-inspector`)
Designed to fast-triage binary files and encrypted malware without cloud processing.
* **Magic Byte Validation:** Catches executable scripts disguised as harmless `.png` images.
* **Entropy Math:** Flags high-entropy encrypted text payloads (Shannon Entropy > 4.8).
* **Parasitic Headers:** Detects executable logic inside static data blobs.

#### 4. [Vault Sentinel](https://squid-protocol.github.io/gitgalaxy/04-04-vault-sentinel/) (`vault-sentinel`)
A hyper-speed pre-commit hook strictly for localized secret detection.
* **Tier 0 Path Blocking:** Instantly blocks sensitive file path commits (e.g., `.pem`, `id_rsa`).
* **Deep Content Scanning:** Hunts for hardcoded cloud cryptographic keys and SaaS tokens.
* **Graveyard Detection:** Finds abandoned passwords sitting in [commented-out dead code](https://squid-protocol.github.io/gitgalaxy/08-13-graveyard-detector/).

---

### ⚡ Performance Showcases

#### Showcase A: Vault Sentinel (Secret Detection)
To prove this engine operates fast enough to be a synchronous pre-commit hook without frustrating developers, we unleashed the **Vault Sentinel** on the massive **tRPC** TypeScript monorepo. 

The engine evaluated 871 files and performed deep-content cryptographic scans on 695 of them in **0.53 seconds** (processing over 1,300 files per second). It successfully intercepted 7 exposed environment files and caught a hardcoded API key before the commit could execute.

![Vault Sentinel Demo](../../../docs/wiki/assets/vault_sentinel_scan.gif)

#### Showcase B: X-Ray Inspector (Malware & Binary Triage)
To test binary detection, we ran the **X-Ray Inspector** against **pwntools**, an exploit development framework containing actual compiled binaries and shellcode.

The engine ripped through the repository at **2,825 files per second**. By reading the raw physical bytes rather than trusting file extensions, it instantly detected 13 parasitic `ELF` execution headers embedded inside the source tree.

![X-Ray Inspector Demo](../../../docs/wiki/assets/xray_inspector_scan.gif)

```text
===========================================================================
 ☢️  X-RAY INSPECTOR: MISSION REPORT
===========================================================================
 Files Evaluated    : 95
 Files Deep Scanned : 95
 Time Elapsed       : 0.03 seconds
 Scan Velocity      : 2,825 files/sec
---------------------------------------------------------------------------
 Active Anomalies   : 13
---------------------------------------------------------------------------
 ❌ TRIAGE ALERT: 13 structural anomalies detected. Blocking commit/PR.
```

#### Showcase C: Supply Chain Firewall (Infrastructure-as-Code Audit)
To prove the firewall can handle diverse polyglot ecosystems without throwing false positives, we ran it against the **Terraform** repository. 

The engine parsed 1,834 files at a velocity of **436 files per second**. It successfully verified the integrity of the dependency tree, identified 54 unknown packages for audit, and cleared the build without tripping any false alarms on standard Go/HCL syntax.

![Supply Chain Firewall Demo](../../../docs/wiki/assets/terraform_firewall_scan.gif)

```text
===========================================================================
 🧱 SUPPLY CHAIN FIREWALL: MISSION REPORT
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
 ✅ BUILD PASSED: Dependency supply chain is clean.
```

---

### 🚀 Quickstart: CI/CD & Pre-Commit Integration

GitGalaxy is designed for frictionless adoption. You can install it globally via PyPI (`pip install gitgalaxy`) or run it natively in GitHub Actions without installing anything. 

#### 1. Global GitHub Marketplace Action (Recommended)
You can drop GitGalaxy into any repository immediately using our official [GitHub Marketplace Action](https://github.com/marketplace/actions/gitgalaxy-scanner).

Add this to your `.github/workflows/security.yml` file:

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

#### 2. Local CLI Execution
```bash
supply-chain-firewall ./node_modules/
xray-inspector ./src/
vault-sentinel .
```

#### 3. Local Pre-Commit Hook Integration
To run the Vault Sentinel automatically before every commit, add this to your `.pre-commit-config.yaml` file:

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

---
### 🌌 Explore the GitGalaxy Wiki
This toolsuite is just one spoke in the larger GitGalaxy ecosystem. Explore the official documentation to see the math and methodology behind our AST-free engine:

* 📖 **[The Competitive Landscape (How We Beat the Status Quo)](https://squid-protocol.github.io/gitgalaxy/04-00-security_landscape/)**
* 📖 **[Supply Chain Firewall Architecture](https://squid-protocol.github.io/gitgalaxy/04-03-supply-chain-firewall/)**
* 📖 **[Binary Anomaly & Entropy Mathematics](https://squid-protocol.github.io/gitgalaxy/04-05-binary-anomaly-detector/)**
* 📖 **[Hardcoded Secrets Exposure Equations](https://squid-protocol.github.io/gitgalaxy/08-23-hardcoded-secrets-exposure/)**
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)**