# GitGalaxy: Software Supply Chain Security & DevSecOps Automation

[![Integration](https://img.shields.io/badge/Integration-CI%2FCD_Ready-00C957.svg)](#)
[![Accuracy](https://img.shields.io/badge/Accuracy-Internal_File_Scanning-00BFFF.svg)](#)
[![Defense](https://img.shields.io/badge/Defense-Zero__Trust-FF4500.svg)](#)

Welcome to the **GitGalaxy Supply Chain Security Suite**.

Standard security scanners have a massive blind spot: they read your `package.json` or `requirements.txt` manifests and simply check those names against CVE databases. They never look inside the actual downloaded files. 

Modern attackers (like the **XZ-Utils** or **Glassworm** campaigns) exploit this exact gap. They don't announce themselves in a manifest.

GitGalaxy operates differently. We shift security entirely left by scanning the physical internals of every dependency file at extreme velocities (100k+ LOC/sec) before it enters your system. 

### 🛡️ What We Block
We provide highly effective, zero-trust defense against structural supply chain threats:
* **Hidden Executables:** Steganography and XZ-Utils attack patterns.
* **Malicious Typosquatting:** Unicode homoglyphs tricking developer imports.
* **Encrypted Payloads:** Obfuscated XOR decryption loops.
* **Hostile I/O:** Shadow imports establishing covert outbound connections.
* **Anomalous Logic:** Network sockets hidden inside declarative CSS or JSON files.

---

### 🛠️ Shift-Left Security Automation

Wired directly into your Git Pre-Commit hooks or CI/CD pipelines, these automation tools act as a physical firewall to fail poisoned builds instantly.

#### 1. The Supply Chain Firewall (`supply_chain_firewall.py`)
Scans massive `node_modules` or `venv` directories in seconds.
* **Zero-Trust Verification:** Checks every physical `import` against strict allowlists.
* **Behavioral Heuristics:** Scans for tainted data injection routines and runtime modifications.

#### 2. Binary Anomaly Inspector (`binary_anomaly_detector.py`)
Designed to triage binary files and detect encrypted malware hidden in plain sight.
* **Magic Byte Validation:** Catches executable scripts disguised as harmless images.
* **Entropy Math:** Flags high-entropy encrypted text payloads.
* **Parasitic Headers:** Detects executable logic nested inside static data blobs.

#### 3. Secrets Detection Hook (`vault_sentinel.py`)
A hyper-speed pre-commit hook strictly for credential and secret detection.
* **Critical Path Blocking:** Instantly blocks sensitive file path commits (e.g., `.env`, `.pem`).
* **Deep Content Scanning:** Hunts for hardcoded cloud cryptographic keys and AWS tokens.
* **Dead Code Secrets:** Finds abandoned passwords hidden deep in commented code.

---

### 🚀 Quickstart: CI/CD & Pre-Commit Integration

Because GitGalaxy bypasses slow ASTs, these scripts execute in seconds, making them perfect for synchronous pipeline blockers.

**Run the Supply Chain Firewall against your local dependencies:**
```bash
python3 supply_chain_firewall.py ./node_modules/
```

**Run the Binary Anomaly Inspector against an incoming Pull Request:**
```bash
python3 binary_anomaly_detector.py ./src/
```

**Run the Secrets Detection script as a Git pre-commit hook:**
```bash
python3 vault_sentinel.py .
```

---
### 🌌 Powered by the blAST Engine (Bypassing LLMs and ASTs)
This tool is a specialized integration in the larger GitGalaxy ecosystem. It is driven by our custom mathematical heuristics engine, capable of mapping multi-dimensional relationships at extreme velocity. Explore the official documentation to see the structural heuristics used to catch obfuscated malware:

* 📖 **[Supply Chain Firewall Architecture](../../../docs/wiki/04-03-supply-chain-firewall.md)**
* 📖 **[Binary Anomaly & Entropy Mathematics](../../../docs/wiki/04-05-binary-anomaly-detector.md)**
* 📖 **[Hardcoded Secrets Exposure Equations](../../../docs/wiki/08-23-hardcoded-secrets-exposure.md)**
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)**