# GitGalaxy: Core Lexical Parsing & Topology Engine

[![Core](https://img.shields.io/badge/Core-Lexical_Parsing-00BFFF.svg)](#)
[![Velocity](https://img.shields.io/badge/Velocity-Zero_AST_Overhead-00C957.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Structural_Extraction-8A2BE2.svg)](#)

This directory contains the primary ingestion, lexical tokenization, and topological mapping layers for the **blAST Engine**.

These files form the core ingestion pipeline. They are responsible for reading raw source code from disk, filtering out irrelevant noise (like massive minified files or `.git` directories), slicing the code into measurable architectural components, and wiring the mathematical network graph.

> **⚠️ Configuration Warning:** Do not modify these core files to tune the engine's behavior. Almost all variables, thresholds, language regexes, and mathematical tuning parameters have been abstracted to the **[Standards Registry](../standards/README.md)**. If you need to tweak risk curves or add a language, do it there.

### 🗺️ The Architecture

Each file in this core represents a discrete phase in the GitGalaxy ingestion pipeline. Read the official documentation links for deep dives into the underlying mathematics.

* **`aperture.py` (The Boundary Filter):** The primary perimeter gate. It enforces Zero-Trust ingestion rules, blocking steganography, minified blobs, and infrastructure directories before they consume system memory.
  * 📖 **[Read the Aperture Filter Specs](https://squid-protocol.github.io/gitgalaxy/02-03-aperture-filter/)**

* **`guidestar_lens.py` (The Metadata Resolver):** The contextual intelligence module. It parses standard project manifests (`package.json`, `Cargo.toml`), resolves explicit linguistic overrides via `.gitattributes`, and hunts for evasion tactics (like force-includes) hidden in `.gitignore`.
  * 📖 **[Read the GuideStar Protocol Specs](https://squid-protocol.github.io/gitgalaxy/02-04-guidestar-protocol/)**

* **`prism.py` (The Lexical Tokenizer):** The structural separator. It surgically separates human intent (documentation/comments) from structural execution logic across multiple syntax families, all while safely preserving complex string literals.
  * 📖 **[Read the Prism Optics Specs](https://squid-protocol.github.io/gitgalaxy/02-07-the-prism/)**

* **`detector.py` (The Function Slicer & Spatial Engine):** The architectural extractor. It splices files into discrete functions, calculates Big-O algorithmic nesting depth, tracks recursive functions, and assigns exact 3D coordinates using deterministic fractal distribution algorithms.
  * 📖 **[Read the Detector Mechanics](https://squid-protocol.github.io/gitgalaxy/02-08-the-detector/)**

* **`network_risk_sensor.py` (The Topology Mapper):** The mathematical routing layer. It wires the ingested files into a directed graph, executing PageRank mathematics to determine absolute Blast Radius, betweenness centrality, and ecosystem roles (Producer vs. Consumer).
  * 📖 **[Read the Network Risk Sensor Specs](https://squid-protocol.github.io/gitgalaxy/02-16-network-risk-sensor/)**

* **`state_rehydrator.py` (The Cache Manager):** The incremental differential scanner. It extracts the previous temporal state from the SQLite database and rehydrates it directly into RAM, enabling ultra-fast differential delta scanning for CI/CD pipelines.
  * 📖 **[Read the State Rehydrator Specs](https://squid-protocol.github.io/gitgalaxy/02-22-state-rehydrator/)**

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.