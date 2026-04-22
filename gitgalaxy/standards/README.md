# GitGalaxy: Core Heuristics & Standards Registry

[![Core](https://img.shields.io/badge/Core-Heuristics_Engine-00BFFF.svg)](#)
[![Coverage](https://img.shields.io/badge/Coverage-50%2B_Languages-00C957.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-AST--Free_Regex-8A2BE2.svg)](#)

Welcome to the configuration and tuning layer of the **blAST Engine**.

This directory contains the immutable mathematical constants, structural regex dictionaries, and security thresholds that dictate how GitGalaxy maps a codebase. No active execution or file reading happens here; these files serve as the universal rulesets and configurations consumed by the central `signal_processor.py`.

If you need to teach GitGalaxy a new language, tune a risk exposure curve, or update the AI AppSec sensors, you do it here.

> **💡 Note:** Adding a new language to the engine typically takes just **1 LLM prompt**. Check out the **[How to Add a Language](HOW_TO_ADD_LANGUAGE.md)** guide to see how to generate the ReDoS-proof structural rules for any new syntax.

### 1. The Boundary Shield (`gitgalaxy_config.py`)
Defines global ingestion rules and zero-trust boundaries before static analysis processing begins.

* **Zero-Trust Import Control:** Defines banned supply chain dependencies.
* **Directory Exclusion Rules:** Defines architectural black holes and massive build folders to skip.
* **Hardcoded Secrets Traps:** Instantly traps cryptographic keys and cloud tokens.

### 2. Language & Identity Heuristics (`language_lens.py`)
The identification engine responsible for converting raw text into high-fidelity ecosystem locks.

* **Collision Resolution:** Mathematically resolves ambiguous file extensions.
* **Contextual Ecosystem Resolution:** Uses neighborhood files (like `package.json` or `pom.xml`) to prove identity.
* **Entropy & Anomaly Detection:** Identifies unknown files or obfuscated malware via spectral density and Shannon entropy.

### 3. The Structural Syntax Dictionary (`language_standards.py`)
The massive heuristic dictionary mapping the syntax of 50+ languages to standard GitGalaxy architectural dimensions.

* **Complexity Mapping:** Translates text to branch logic, state mutation, and cognitive load.
* **Behavioral Sensors:** Universal regex for mapping AI boundaries, Authentication routing, and IPC calls.
* **Technical Debt Tracking:** Detects formatting discrepancies and mixed architectural paradigms.

### 4. The Scoring & Risk Engine (`analysis_lens.py`)
The mathematical core defining how raw structural signals are converted into 0-100% risk exposures.

* **Risk Normalization Curves:** Mathematical sigmoid clamps for tuning risk exposures.
* **Contextual Dampeners:** Modifiers that reduce risk weight for test files and documentation.
* **Architectural Anomaly Detection:** Penalizes code acting alien to its ecosystem.
* **Machine Learning Inference:** Houses K-means clustering models for archetype classification.

---

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.