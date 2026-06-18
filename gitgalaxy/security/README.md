# GitGalaxy Security: Threat Inference & Application Security Engine

This directory houses the Machine Learning models, Static Application Security Testing (SAST) engines, and Software Supply Chain Security (SSCS) auditors for GitGalaxy. 

Unlike traditional security tools that rely on matching specific CVEs or static known-vulnerable package versions, this security engine evaluates the **structural intent and behavioral signatures** of a codebase. It calculates risk exposures by combining raw heuristic hits with topological network graph data to accurately model a threat's true exploitable attack surface.

## Architectural Philosophy & Defensive Engineering

Modern malware, supply chain attacks, and Agentic RCE (Remote Code Execution) vulnerabilities frequently evade traditional static analysis through obfuscation, dynamically loaded strings, or distributed payload execution. To counter this, the GitGalaxy Security engine employs several advanced defensive paradigms:

### 1. Network-Weighted Threat Scoring
A vulnerability in a core utility file has a radically different systemic impact than a vulnerability in an isolated, unimported test script. The engine dynamically scales vulnerability thresholds based on a node's **Blast Radius**. It multiplies raw SAST hits by PageRank and Betweenness Centrality metrics, ensuring that highly centralized network nodes face strictly hardened security tolerances.

### 2. O(H) Data Flow Taint Tracking
Tracking execution paths (from an I/O input to a Database sink) typically requires compiling a massive, memory-intensive Abstract Syntax Tree (AST). The security engine bypasses this by utilizing an O(H) Offset Mapper. It only evaluates the spatial distance between targeted heuristic hits (e.g., `sec_danger` and `sec_io`), executing variable assignment extraction and downward flow scans in linear time without compiling the file.

### 3. C-Optimized Shannon Entropy
To catch obfuscated payloads and custom decryption routines hidden inside massive string literals, the engine utilizes mathematically optimized Shannon Entropy calculations. By restructuring the standard entropy formula to execute division operations completely outside the evaluation loop, it can process thousands of massive strings in milliseconds without computational bottlenecks.

### 4. Software Supply Chain & Registry Defenses
Dependencies are heavily audited for Namespace Hijacking, Package Aliasing, and Insecure Registry Routing. The parser actively flags Direct URI resolutions (e.g., direct GitHub links or local file paths) that bypass Subresource Integrity (SRI) checks, and intercepts insecure tunneling protocols (like `ngrok` or plain `http`) hidden inside package configuration files.

### 5. Shadow Patch & Evasion Detection
The engine correlates runtime metrics with structural mass to detect "Shadow Patches"—files where the cryptographic hash has mutated without a corresponding version bump. It forcefully overrides standard logic to classify these unauthorized modifications as critical security threats.

---

## The Core Pipeline (Data Flow)

Each file in this directory represents a distinct phase of the security validation and threat hunting pipeline:

* **`manifest_parser.py` (The SSCS Auditor):** The dependency and configuration parser. It builds a deterministic, O(1) global resolution map by auditing `package.json`, `package-lock.json`, `requirements.txt`, and `pip.conf`. It prevents Supply Chain Substitution attacks by identifying non-standard registries and untrusted VCS routing.
* **`security_lens.py` (The SAST Engine):** The raw heuristic sensor. It applies highly optimized regular expressions to detect 13 distinct threat categories (e.g., Prompt Injection, Agentic RCE funnels, Memory Corruption, Hardcoded Secrets). It executes multi-line Taint Tracking and memory-efficient binary header inspection to validate file extension integrity.
* **`security_auditor.py` (The ML Orchestrator):** The threat classification engine. It resolves N-th degree transitive dependency graphs to calculate precise upstream/downstream ratios. It then compiles a 50-dimensional feature matrix (evaluating Control Flow Ratio, API Exposure, Ownership Entropy, etc.) and executes it against the local XGBoost model.
* **`gitgalaxy_malware_xgb_multiclass.json`:** The pre-trained, serialized XGBoost Machine Learning model. It evaluates the 50-dimensional feature matrix to classify the specific type of anomalous payload present across 5 distinct taxonomies (Safe Code, Botnet/DDoS, Stealer/Trojan, Dropper/Webshell, Native Infector).

---

## 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://squid-protocol.github.io/gitgalaxy/), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[GitGalaxy Official Documentation](https://squid-protocol.github.io/gitgalaxy/)** - Deep dives into the mathematics and pipeline architecture.
* 🔭 **[GitGalaxy Visualizer](http://gitgalaxy.io/)** - Render your codebase locally in 3D using WebGPU.
* 📖 **[The blAST Paradigm Wiki](https://squid-protocol.github.io/gitgalaxy/docs/wiki/01-03-the-blast-paradigm/)** - The academic and structural thesis backing the engine.
* ⚙️ **[Language Calibration Standards](https://github.com/squid-protocol/gitgalaxy/blob/main/gitgalaxy/standards/how_to_add_a_language.md)** - Guide to extending the comparative lexical taxonomy.