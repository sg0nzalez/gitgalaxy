# GitGalaxy Metrics: Heuristic Math & Statistical Auditing Engine

This directory houses the advanced mathematical processors, statistical auditors, and temporal engines for GitGalaxy[cite: 48]. 

If the `core` directory acts as the extraction layer (identifying raw structural signatures), the `metrics` directory is the analytical core[cite: 48]. It is responsible for consuming raw lexical signals and translating them into actionable, multi-dimensional risk vectors and architectural telemetry[cite: 48].

## Data Flow Positioning

The Metrics engine sits strictly in the middle of the pipeline (Phases 3, 6, and 8 of the `GalaxyScope` orchestrator)[cite: 48]:

1. **Ingestion (Core):** Raw source code is spliced and structural signatures (regex matches, token frequencies) are extracted[cite: 48].
2. **Translation (Metrics):** Raw hits are piped into the `signal_processor.py`[cite: 48]. **Crucially, risk exposures are calculated metrics derived from the structural hits; they are not used interchangeably with the hits themselves**[cite: 48].
3. **Verification (Metrics):** The `statistical_auditor.py` evaluates the resulting graph to filter out statistical anomalies (e.g., auto-generated data dumps)[cite: 48].
4. **Export (Recorders):** The refined, high-fidelity risk vectors are passed downstream to the LLM, Database, and WebGPU recorders[cite: 48].

## Core Modules & Engineering Defenses

### `signal_processor.py` (The Mathematical Core)
The primary heuristic math engine[cite: 48]. Traditional analysis tools flag raw vulnerabilities, leading to massive false-positive fatigue[cite: 48]. The Signal Processor takes a fundamentally different approach: it translates raw structural hits into an 18-point risk vector (evaluating concepts like Technical Debt, Cognitive Load, and State Flux)[cite: 48]. 
* **Core Mechanics:** It applies contextual dampeners (like testing umbrellas and documentation shields) to raw signals[cite: 48]. For example, a high "flux" signal in a file with 100% test coverage has its ultimate risk exposure mathematically dampened, reflecting true ecosystem reality rather than isolated syntax analysis[cite: 48].

### `statistical_auditor.py` (The Statistical Auditor)
A statistical gatekeeper designed to protect downstream Machine Learning models and LLMs from context poisoning[cite: 48].
* **Core Mechanics:** Even the best regex filters occasionally ingest massive, auto-generated data dumps or static configuration matrices that mimic source code[cite: 48]. The Auditor calculates the standard deviations of logic density and structural mass across the entire assembled repository graph[cite: 48]. Nodes that fall outside mathematical norms are automatically quarantined and dropped before they can distort the final architectural map[cite: 48].

### `chronometer.py` (The Temporal Engine)
Static code analysis is often blind to human behavior[cite: 48]. The Chronometer bridges this gap by merging temporal Git telemetry with structural static analysis[cite: 48].
* **Core Mechanics:** It extracts Git volatility, churn velocity, and ownership entropy without requiring heavy, secondary dependency parsing[cite: 48]. By cross-referencing code mass with developer churn, the engine can identify "Fragile Monoliths" (massive files with high logic density but fractured, transient ownership)[cite: 48].

### `tensor_scanner.py` (The Zero-RAM AI Auditor)
As repositories increasingly embed local AI models, standard parsers crash attempting to evaluate gigabyte-scale binaries[cite: 48].
* **Core Mechanics:** The Tensor Scanner performs a Zero-RAM binary header audit on local model weights (`.gguf`, `.safetensors`)[cite: 48]. It surgically extracts architectural metadata (parameter count, quantization, architecture type) without loading the massive weights into system memory[cite: 48]. It then assigns these artifacts high structural impact scores for the topological map, safely visualizing AI infrastructure without risking an OS-level Out-Of-Memory (OOM) kill[cite: 48].

---

**Architectural Note:** All modules in this directory are engineered to operate on O(1) or O(N) linear time complexity[cite: 48]. By the time data reaches the metrics engine, expensive disk I/O and regex parsing have already concluded, allowing these mathematical operations to execute across tens of thousands of files in milliseconds[cite: 48].

---

## 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://squid-protocol.github.io/gitgalaxy/), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[GitGalaxy Official Documentation](https://squid-protocol.github.io/gitgalaxy/)** - Deep dives into the mathematics and pipeline architecture.
* 🔭 **[GitGalaxy Visualizer](http://gitgalaxy.io/)** - Render your codebase locally in 3D using WebGPU.
* 📖 **[The blAST Paradigm Wiki](https://squid-protocol.github.io/gitgalaxy/docs/wiki/01-03-the-blast-paradigm/)** - The academic and structural thesis backing the engine.
* ⚙️ **[Language Calibration Standards](https://squid-protocol.github.io/gitgalaxy/gitgalaxy/standards/how_to_add_a_language.md)** - Guide to extending the comparative lexical taxonomy.