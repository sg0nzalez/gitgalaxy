# GitGalaxy: The Recording & Export Layer

[![Export](https://img.shields.io/badge/Export-Multi--Format-00BFFF.svg)](#)
[![WebGPU](https://img.shields.io/badge/WebGPU-Columnar_JSON-00C957.svg)](#)
[![AI](https://img.shields.io/badge/AI-Context_Optimized-8A2BE2.svg)](#)

This directory contains the export engines that translate the internal RAM state of the **blAST Engine** into usable, forensic data formats for downstream systems.

GitGalaxy is designed to be headless and API-first. These recorders ensure that the data can be consumed by interactive 3D visualizers, autonomous AI coding agents, or enterprise SIEMs.

> **⚠️ Configuration Warning:** Do not modify these core recorder files to add new data columns or change schema mappings. All schemas, UI string labels, and key mappings have been abstracted to the **[Standards Registry](../standards/README.md)**.

### 🗺️ The Architecture

Each file represents a specific data serialization strategy. Read the official documentation links for deep dives into the underlying schema formatting.

* **`record_keeper.py`:** The native SQLite3 recorder. It transforms the live RAM state directly into a highly relational database (`_master.db`), bypassing intermediate JSON parsing to create a time-series schema perfectly aligned for Master Database aggregation and complex querying.
  * 📖 **[Read the SQLite Database Specs](https://squid-protocol.github.io/gitgalaxy/02-21-record-keeper/)**

* **`gpu_recorder.py`:** Generates the highly optimized `_GPU_galaxy.json` payload. This recorder performs a destructive RAM eviction (destroying the Python dictionaries as it writes) to compress the data into a Columnar Arrays of Structs (AoS to SoA) format, utilizing string interning for extreme WebGPU rendering performance.
  * 📖 **[Read the GPU Payload Formatting Specs](https://squid-protocol.github.io/gitgalaxy/02-13-gpu-recorder/)**

* **`llm_recorder.py`:** The AI Translation Layer. It generates condensed, token-optimized Markdown (`_llm.md`) and a relational knowledge graph (`_graph.sqlite`). These artifacts are explicitly designed to be ingested by autonomous AI coding agents (like Claude or Cursor) or RAG pipelines, highlighting choke points, God Nodes, and AI threat scores.
  * 📖 **[Read the LLM Context Optimization Specs](https://squid-protocol.github.io/gitgalaxy/02-14-llm-recorder/)**

* **`audit_recorder.py`:** Generates a verbose, human-readable forensic log (`_audit.json`). This file retains the raw dictionary structure and translates internal metrics into descriptive English labels. Designed for compliance, debugging, and deep-dive architectural analysis.
  * 📖 **[Read the Forensic Audit Specs](https://squid-protocol.github.io/gitgalaxy/02-12-audit-recorder/)**

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.