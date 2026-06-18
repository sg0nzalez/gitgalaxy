# GitGalaxy Standards: Heuristics Registry & Calibration Layer

This directory contains the immutable mathematical constants, structural regex dictionaries, security thresholds, and ingestion constraints that govern the GitGalaxy engine[cite: 51]. 

No active execution or file I/O occurs in this directory[cite: 51]. Instead, this is the **Central Calibration Matrix**[cite: 51]. It defines the universal rulesets consumed by the Orchestrator, the Prism, the Signal Processor, and the Security Lens[cite: 51]. 

## Architectural Philosophy & Defensive Engineering

Engineers accustomed to traditional AST (Abstract Syntax Tree) parsers often view regular expressions with skepticism, assuming they are too brittle or prone to Catastrophic Backtracking (ReDoS) to parse enterprise code[cite: 51]. 

GitGalaxy explicitly bypasses ASTs to **visualize functional intent rather than rigid syntax**, allowing it to map severely fragmented, legacy, or un-compilable code[cite: 51]. To achieve 100,000+ LOC/sec parsing without crashing the Python GIL, the dictionaries in this directory are engineered with extreme defensive boundaries[cite: 51]:

### 1. ReDoS Immunity & Strict Bounding
The regex dictionaries defined in `language_standards.py` strictly prohibit unbounded quantifiers (like `.*` or `\s+`)[cite: 51]. To safely leap across multi-line function declarations and modern attribute stacking (e.g., C++23 `[[attributes]]` or Java `@Annotations`), the engine utilizes strict boundary limits[cite: 51]. It enforces rigid numeric clamps (e.g., `{0,5}`) and mutually exclusive character sets, guaranteeing O(1) or linear O(N) evaluation time per match[cite: 51].

### 2. Bayesian Confidence Hierarchy
Inferring a file's language purely by its extension leads to catastrophic collisions (e.g., `.m` being Objective-C, MATLAB, or Mathematica)[cite: 51]. `language_lens.py` resolves these collisions natively without AST evaluation[cite: 51]. It builds a Bayesian confidence score by cross-referencing sibling files, structural neighborhood context, and package manifests, only falling back to an expensive lexical scan if the file's identity drops below a strict ambiguity threshold[cite: 51].

### 3. Contextual Threat Calibration (The Anomaly Matrix)
A vulnerability’s severity is dictated by its environment[cite: 51]. Standard OS shell execution is expected in a bash script but highly anomalous in a React frontend component[cite: 51]. `analysis_lens.py` defines an **Ecosystem Mismatch Matrix** that dynamically multiplies threat scores when an asset exhibits behaviors hostile to its native architecture (e.g., detecting C-style memory pointers inside a Node.js web layer), instantly flagging it as a high-risk anomaly or potential backdoor[cite: 51].

### 4. Structural Weight Normalization
AST parsers typically collapse when analyzing massive machine-generated files (e.g., Swagger JSONs, Webpack chunks, Protobuf definitions)[cite: 51]. `analysis_lens.py` deploys pre-calculated "Structural Normalizers" to programmatically reduce the calculated weight of generated code, ensuring human-written architecture remains the focal point of the analysis without risking Out-Of-Memory (OOM) exceptions or skewing repository metrics[cite: 51].

---

## Core Configurations

Each file in this directory serves a distinct calibration purpose for the downstream engines[cite: 51]:

* **`gitgalaxy_config.py` (The Global Firewall):** Defines Zero-Trust ingestion boundaries[cite: 51]. It houses the Supply Chain Firewall configurations (approved vs. blacklisted imports), global file denylists, X-Ray binary scanner bypasses, and physical file-size clamps[cite: 51].
* **`language_lens.py` (The Identity Classifier):** The Bayesian engine that assigns "Identity Locks" to files[cite: 51]. It defines the multi-tiered confidence hierarchy, resolving extension collisions by weighing exact filename matches against ecosystem anchors[cite: 51].
* **`language_standards.py` (The Optical Dictionary):** The massive, highly optimized structural mapping registry for 50+ languages[cite: 51]. It defines exactly how to slice a language into Branch Logic, State Flux, High-Risk Execution, and Object Declarations using ReDoS-proof regular expressions[cite: 51].
* **`analysis_lens.py` (The Mathematical Constants):** The repository of Threat Policies, Sigmoid Curves, and K-Means clustering medians[cite: 51]. It dictates how raw structural signals are mathematically converted into 0-100% risk exposure vectors (e.g., Technical Debt, Cognitive Load, Algorithmic DoS)[cite: 51]. 
* **`how_to_add_a_language.md` (The Extension Guide):** Contains the strict prompt engineering protocols required to generate ReDoS-proof dictionaries via LLMs[cite: 51].

## Extending the Engine

Because GitGalaxy is AST-free, adding support for a new language does not require writing a complex, brittle parser[cite: 51]. You simply need to calibrate the structural heuristics of the target language by generating a new dictionary entry[cite: 51]. 

For strict guidelines and the LLM Master Prompt required to generate ReDoS-proof structural definitions, review: **[Architecting a New Language](https://github.com/squid-protocol/gitgalaxy/blob/main/gitgalaxy/standards/how_to_add_a_language.md)**[cite: 51].

---

## 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://squid-protocol.github.io/gitgalaxy/), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[GitGalaxy Official Documentation](https://squid-protocol.github.io/gitgalaxy/)** - Deep dives into the mathematics and pipeline architecture.
* 🔭 **[GitGalaxy Visualizer](http://gitgalaxy.io/)** - Render your codebase locally in 3D using WebGPU.
* 📖 **[The blAST Paradigm Wiki](https://squid-protocol.github.io/gitgalaxy/docs/wiki/01-03-the-blast-paradigm/)** - The academic and structural thesis backing the engine.
* ⚙️ **[Language Calibration Standards](https://github.com/squid-protocol/gitgalaxy/blob/main/gitgalaxy/standards/how_to_add_a_language.md)** - Guide to extending the comparative lexical taxonomy.