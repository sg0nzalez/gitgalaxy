# GitGalaxy Core: Lexical Parsing & Topology Engine

This directory contains the primary ingestion, lexical tokenization, and topological mapping layers for the GitGalaxy engine. 

These core modules are responsible for reading raw source code from disk, filtering out irrelevant noise (such as minified files or infrastructure directories), slicing the code into measurable architectural components, and wiring the mathematical network graph.

## Architectural Philosophy & Defensive Engineering

Traditional static analysis tools rely heavily on Abstract Syntax Trees (ASTs). While ASTs offer granular syntax precision, they are inherently brittle, language-specific, and require fully compilable, error-free code to function. 

GitGalaxy explicitly bypasses ASTs to **prioritize visualizing functional intent over rigid syntax parsing**. By utilizing highly bounded, ReDoS-proof regular expressions and fluid-state counters, the engine extracts the core structural signatures (DNA) of a codebase across 50+ languages, even if the code is legacy, fragmented, or currently broken. 

To achieve this at scale without collapsing under the weight of massive enterprise repositories, the engine employs several layers of defensive engineering:

### 1. O(1) Pre-I/O Path Evaluation
Before the pipeline wastes CPU cycles or RAM opening a file, it evaluates OS-level metadata (size, extension, path). This immediately shunts oversized monoliths, binary masquerades (via null byte `\x00` detection), and machine-generated debris before triggering disk I/O, preventing OS-level locks and Out-Of-Memory (OOM) kills.

### 2. Bayesian Intent Bypasses
Rather than inferring the purpose of a file purely from its extension, the engine parses explicit project manifests (`package.json`, `Cargo.toml`, `.gitattributes`) first. If a file is defined as a roadmap anchor or explicitly typed by the developer, the engine assigns an "Intent Lock," bypassing expensive heuristic guessing downstream.

### 3. O(1) Angular Spatial Hashing
Standard physics engines crash on O(N^2) collision detection loops when attempting to place thousands of nodes in a 3D space. GitGalaxy neutralizes this computational bottleneck by bucketing the Cartesian coordinate map into 360 angular degrees. A placement ray only checks the exact degree bin it points at, securing O(1) collision avoidance and guaranteeing deterministic visual generation.

### 4. Graph Centrality Deadlock Prevention
Centrality algorithms (Betweenness/Closeness) scale non-linearly at roughly O(V^3). For monolithic repositories exceeding 1,500 nodes, attempting exact calculations will trigger CI/CD timeout deadlocks. GitGalaxy utilizes safe iterative convergence (PageRank) for primary blast radius calculations, while enforcing strict sampling limits or hard bypasses on secondary centrality metrics when node counts exceed safe thresholds.

---

## The Core Pipeline (Data Flow)

Each file in this core represents a discrete, highly optimized phase in the GitGalaxy ingestion pipeline:

* **`aperture.py` (Phase 0.1 - The Boundary Filter):** The primary perimeter gate enforcing Zero-Trust ingestion rules. It utilizes lexical monotony shields and strict array limits to block minified blobs, data-heavy payload files, and generated documentation before they enter the processing pool.
* **`guidestar_lens.py` (Phase 0.5 - The Metadata Resolver):** The contextual intelligence module. It provides "Social Proof" by deep-inspecting package manifests and `.gitignore` files. Crucially, it intercepts hostile force-includes (e.g., `!payload.so`) used by attackers to sneak binaries into repositories.
* **`prism.py` (Phase 2 - The Lexical Tokenizer):** The structural separator. It surgically decouples a unified file into mutually exclusive executable logic and documentation streams. It utilizes an O(1) atomic literal shield to temporarily mask strings, preventing the regex scanner from accidentally mutating URLs or string contents that mimic comment delimiters.
* **`detector.py` (Phase 2.5 - The Structural Extractor):** The architectural slicer. It splices files into discrete functions and calculates Big-O algorithmic complexity. *Engineering Note: Instead of using heavy AST compilation to determine cyclomatic nesting depth, this module uses standard code indentation as a high-speed, 95% accurate proxy for O(N) complexity.*
* **`network_risk_sensor.py` (Phase 4 - The Topology Mapper):** The mathematical routing layer. It wires the ingested files into a Directed Graph (DAG), executing PageRank mathematics to determine absolute Blast Radius, test coverage gaps, and ecosystem roles (Producer vs. Consumer).
* **`spatial_mapper.py` (Phase 7.5 - The Positioning Engine):** Transforms the flat list of parsed files into a deterministic 3D Cartesian coordinate map. It groups files into directory clusters relative to high-impact central nodes while maintaining dynamic spatial clearance.
* **`state_rehydrator.py` (The Cache Manager):** The incremental differential scanner. During CI/CD Delta Scans, it is highly inefficient to re-parse 10,000 unchanged files. This module extracts the previous temporal state from SQLite and rehydrates it directly into RAM, enabling instant graph recalculation for just the modified files.

---

## 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://squid-protocol.github.io/gitgalaxy/), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[GitGalaxy Official Documentation](https://squid-protocol.github.io/gitgalaxy/)** - Deep dives into the mathematics and pipeline architecture.
* 🔭 **[GitGalaxy Visualizer](http://gitgalaxy.io/)** - Render your codebase locally in 3D using WebGPU.
* 📖 **[The blAST Paradigm Wiki](https://squid-protocol.github.io/gitgalaxy/docs/wiki/01-03-the-blast-paradigm/)** - The academic and structural thesis backing the engine.
* ⚙️ **[Language Calibration Standards](https://squid-protocol.github.io/gitgalaxy/gitgalaxy/standards/how_to_add_a_language.md)** - Guide to extending the comparative lexical taxonomy.