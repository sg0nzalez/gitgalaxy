# GitGalaxy: Supply Chain Security & Pre-Commit Sentinels

[![Integration](https://img.shields.io/badge/Integration-CI%2FCD_Ready-00C957.svg)](#)
[![Accuracy](https://img.shields.io/badge/Accuracy-Internal_File_Scanning-00BFFF.svg)](#)
[![Defense](https://img.shields.io/badge/Defense-Zero__Trust-FF4500.svg)](#)

Welcome to the **GitGalaxy Supply Chain Security Suite**.

Standard security scanners have a massive blind spot: they read your `package.json` or `requirements.txt` and check those names against CVE databases. They never look inside the actual downloaded files. 

Modern attackers (like the **XZ-Utils** or **Glassworm** campaigns) exploit this. They don't announce themselves in a manifest.

GitGalaxy operates differently. We scan the physical internals of every dependency file at extreme velocities (100k+ LOC/sec) before it enters your system. 

### 🛡️ What We Stop
We provide highly effective defense against structural threats:
* **Hidden Executables:** Steganography and XZ-Utils attack patterns.
* **Malicious Typosquatting:** Unicode homoglyphs tricking developer imports.
* **Encrypted Payloads:** Sub-atomic XOR decryption loops.
* **Hostile I/O:** Shadow imports establishing covert outbound connections.
* **Anomalous Logic:** Network sockets hidden inside declarative CSS/JSON.

---

### 🛠️ The Sentinel Tools

Wired directly into your Git Pre-Commit hooks or CI/CD pipelines, these sentinels act as a physical firewall to fail poisoned builds early.

#### 1. The Supply Chain Firewall (`supply_chain_firewall.py`)
Scans massive `node_modules` or `venv` directories in seconds.
* **Zero-Trust Verification:** Checks every physical `import` against allowlists.
* **Behavioral Heuristics:** Scans for tainted data injection routines.

#### 2. X-Ray Inspector (`binary_anomaly_detector.py`)
Designed to triage binary files and encrypted malware.
* **Magic Byte Validation:** Catches executable scripts disguised as images.
* **Entropy Math:** Flags high-entropy encrypted text payloads.
* **Parasitic Headers:** Detects executable logic inside static data blobs.

#### 3. Vault Sentinel (`vault_sentinel.py`)
A hyper-speed pre-commit hook strictly for secret detection.
* **Tier 0 Path Blocking:** Instantly blocks sensitive file path commits.
* **Deep Content Scanning:** Hunts for hardcoded cloud cryptographic keys.
* **Graveyard Detection:** Finds abandoned passwords in commented code.

---

### 🚀 Quickstart: CI/CD & Pre-Commit Integration

Because GitGalaxy bypasses slow ASTs, these scripts execute in seconds, making them perfect for synchronous pipeline blockers.

**Run the Supply Chain Firewall against your dependencies:**
```bash
python3 supply_chain_firewall.py ./node_modules/
```

**Run the X-Ray Inspector against an incoming PR:**
```bash
python3 binary_anomaly_detector.py ./src/
```

**Run the Vault Sentinel as a Git pre-commit hook:**
```bash
python3 vault_sentinel.py .
```

---
### 🌌 Powered by the blAST Engine (Bypassing LLMs and ASTs)
This tool is a specialized spoke in the larger GitGalaxy ecosystem. It is driven by our custom mathematical heuristics engine, capable of mapping multi-dimensional relationships at extreme velocity. Explore the official wiki to see the sub-atomic heuristics used to catch obfuscated malware:

* 📖 **[Supply Chain Firewall Architecture](../../../docs/wiki/04-03-supply-chain-firewall.md)**
* 📖 **[Binary Anomaly & Entropy Mathematics](../../../docs/wiki/04-05-binary-anomaly-detector.md)**
* 📖 **[Hardcoded Secrets Exposure Equations](../../../docs/wiki/08-23-hardcoded-secrets-exposure.md)**
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)**
