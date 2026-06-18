# GitGalaxy: Static Analysis & Heuristics Engine

[![Analysis](https://img.shields.io/badge/Analysis-Sigmoid_Curves-00BFFF.svg)](#)
[![Machine Learning](https://img.shields.io/badge/ML-K--Means_Clustering-00C957.svg)](#)
[![Security](https://img.shields.io/badge/Security-Statistical_Auditing-8A2BE2.svg)](#)

This directory contains the mathematical core of the **blAST Engine**.

Once the `/core` lexical parsing layer has sliced the source code into structural signals, this engine takes over. It applies mathematical heuristics to generate 0-100% risk exposures, classifies architectural intent using Machine Learning, and maps the temporal churn of the repository over time.

> **⚠️ Configuration Warning:** Do not modify these core analysis files to tune the engine's behavior. Almost all variables, Sigmoid curve slopes, risk thresholds, and path modifiers have been abstracted to the **[Standards Registry](../standards/README.md)**.

### 🗺️ The Architecture

* **`signal_processor.py`:** The core analytical engine. It takes the raw regex hits (e.g., number of branches, number of allocations) and applies Sigmoid curves and domain-specific path modifiers to calculate Cognitive Load, Tech Debt, and Security risks. It also executes statistical anomaly detection to identify obfuscated malware or mismatched files hiding in foreign ecosystems.
  * 📖 **[Read the Signal Processing Equations](https://squid-protocol.github.io/gitgalaxy/02-09-signal-processing/)**

* **`chronometer.py`:** The version control telemetry engine. It interfaces with the local `.git` history using a high-speed stream-processing pipeline to calculate the pulse rate (churn) and stability of individual files over a rolling dynamic window.
  * 📖 **[Read the Chronometer Mechanics](https://squid-protocol.github.io/gitgalaxy/02-15-chronometer/)**

* **`neural_auditor.py`:** The machine learning inference engine. It uses pre-trained K-means clustering models to assign every file and function to a specific "Archetype" (e.g., *The God Node*, *Declarative Glue*, *Async Orchestrator*). It also contains sensors to surgically audit massive LLM weights (`.safetensors`, `.gguf`) without loading them into RAM.
  * 📖 **[Read the Neural Auditor & Archetypes Specs](https://squid-protocol.github.io/gitgalaxy/02-19-neural-auditor/)**

* **`spectral_auditor.py`:** The quality control gate. It uses statistical normalization to detect Structural Drift. If a file acts as a statistical outlier compared to its peers (e.g., a massive data dump disguised as code), it is quarantined to prevent it from corrupting the architectural knowledge graph.
  * 📖 **[Read the Spectral Audit Specs](https://squid-protocol.github.io/gitgalaxy/02-11-spectral-audit/)**

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.