# GitGalaxy: Supply Chain Security & Pre-Commit Sentinels

[![Integration](https://img.shields.io/badge/Integration-CI%2FCD_Ready-00C957.svg)](#)
[![Accuracy](https://img.shields.io/badge/Accuracy-Internal_File_Scanning-00BFFF.svg)](#)
[![Defense](https://img.shields.io/badge/Defense-Zero__Trust-FF4500.svg)](#)

Welcome to the **GitGalaxy Supply Chain Security Suite**.

Standard security scanners have a massive blind spot: they read your `package.json` or `requirements.txt` to see what you *intended* to download, and they check those names against a CVE database. But they never look inside the actual files that arrive on your machine. 

Modern attackers know this. Sophisticated supply chain compromises like the **XZ-Utils backdoor** or the **Glassworm** campaign don't announce themselves in a manifest. They hide in obfuscated binaries, typosquatted imports, and encrypted test files.

GitGalaxy covers the holes no one else is looking at. Because our engine operates at extreme velocities (100k+ LOC/sec), we don't just scan the manifest—**we scan the physical internals of every single dependency file before it enters your system.**

### 🛡️ How We Shield Your Codebase

Finding a network socket keyword (`net.connect`, `socket()`) inside a purely declarative frontend CSS/JSON library is a dead giveaway that the package is hostile. Our scanners don't wait for a CVE to be published; they use mathematical heuristics to flag the anomalous behavior the second it hits your disk.

**We provide absolute defense against:**
* **Steganography & Hidden Executables:** (e.g., The XZ-Utils attack pattern).
* **Unicode Homoglyphs & Typosquatting:** Developers accidentally importing `rèquests` instead of `requests`.
* **Encrypted Payloads:** Sub-atomic XOR decryption loops hiding in plain sight.
* **Shadow Imports & Hostile I/O:** Libraries covertly establishing outbound connections.

---

### 🛠️ The Sentinel Tools

Designed to be wired directly into your Git Pre-Commit hooks or GitHub Actions CI/CD pipelines. They act as a physical firewall, failing the build *before* the poison enters your bloodstream.

#### 1. The Supply Chain Firewall (`supply_chain_firewall.py`)
Scans massive `node_modules` or `venv` directories in seconds.
* **Zero-Trust Verification:** Checks every physical `import` and `require()` against your strict Allowlist/Denylist.
* **Behavioral Heuristics:** Scans the actual code logic for tainted data injection, homoglyphs, and shadow I/O operations.

#### 2. X-Ray Inspector (`binary_anomaly_detector.py`)
Designed to triage binary files and encrypted malware.
* **Magic Byte Validation:** Catches executable scripts disguised as `.png` or `.jpg` files.
* **Entropy Math:** Calculates Shannon Entropy. If a standard text file hits an entropy score of > 4.8, it is mathematically proven to contain highly packed, encrypted, or obfuscated payloads.
* **Parasitic Headers:** Detects executable logic buried deep within static data blobs.

#### 3. Vault Sentinel (`vault_sentinel.py`)
A hyper-speed pre-commit hook designed strictly for secret detection.
* **Tier 0 Path Blocking:** Instantly blocks `.pem`, `id_rsa`, and `.env` files from ever reaching the commit phase.
* **Deep Content Scanning:** Rips through code to find hardcoded AWS keys, database passwords, and cryptographic vaults.
* **Graveyard Detection:** Identifies commented-out passwords left behind by careless debugging.

---

### 🚀 Quickstart: CI/CD & Pre-Commit Integration

Because GitGalaxy bypasses slow ASTs, these scripts execute in seconds, making them perfect for synchronous pipeline blockers.

**Run the Supply Chain Firewall against your dependencies:**
```bash
python3 supply_chain_firewall.py ./node_modules/