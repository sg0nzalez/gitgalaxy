# GitGalaxy: Threat Detection & Security Validation Models

[![AppSec](https://img.shields.io/badge/AppSec-Dual--Sided_Guardrails-FF4500.svg)](#)
[![Machine Learning](https://img.shields.io/badge/ML-XGBoost_Inference-8A2BE2.svg)](#)
[![Threat Hunting](https://img.shields.io/badge/Threat_Hunting-Structural_Heuristics-00BFFF.svg)](#)

This directory houses the specialized security definitions, threat threshold policies, and pre-trained classification models used by the **blAST Engine** to hunt for vulnerabilities and malicious payloads.

Unlike traditional static analysis tools that look for specific CVEs or known vulnerable package versions, GitGalaxy looks for the structural intent of a threat. Risk exposures are calculated metrics derived from structural regex hits, rather than relying on static "threat DNA" or rigid signatures. It measures the physical distance between an I/O input node and a dangerous execution command to calculate the exact exploitable attack surface.

> **⚠️ Configuration Warning:** Do not modify the threshold numbers or dictionaries in these files directly. All security baseline thresholds (e.g., `Baseline` vs. `Paranoid` mode) have been abstracted to the **[Standards Registry](../standards/README.md)**.

### 🗺️ The Architecture

* **`security_lens.py`:** The mathematical engine for threat detection. It houses the 13 raw Heuristic Sensors (e.g., `sec_heat_triggers`, `sec_shadow_imports`, `sec_homoglyphs`). It uses C-backed Shannon Entropy math to catch obfuscated malware and byte-level XOR decryption loops hidden inside massive string literals.
  * 📖 **[Read the Security Lens Architecture Specs](https://squid-protocol.github.io/gitgalaxy/02-06-security-lens/)**

* **`security_auditor.py`:** The threat classification orchestrator. It evaluates the raw structural anomalies discovered by the `security_lens` against your chosen threat policies. It is responsible for blocking Logic Bombs, RCE funnels, and exposed secrets before they can be deployed.
  * 📖 **[Read the Security Auditor Specs](https://squid-protocol.github.io/gitgalaxy/02-20-security-auditor/)**

* **`gitgalaxy_malware_xgb_multiclass.json`:** The serialized XGBoost Machine Learning model. During the scanning phase, GitGalaxy builds a 50-dimensional feature vector for every file based on its structural metrics (e.g., Control Flow Ratio, API Exposure, Ownership Entropy). This pre-trained model evaluates that vector locally to classify the exact strain of malicious payload present (e.g., *Botnet*, *Trojan*, *Dropper/Webshell*).

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.