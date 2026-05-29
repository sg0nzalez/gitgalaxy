# Analysis Lens (Math Constants & Schemas)

> **The Universal Schemas**
>
> The `analysis_lens.py` file operates as the strict mathematical and schema registry for GitGalaxy. While `language_standards.py` defines *how* to parse code, the Analysis Lens defines *what* that parsed data actually means. 
>
> It enforces the exact array structures, string translations, and mathematical thresholds required to turn raw regex counts into meaningful 3D visuals and forensic audits without breaking downstream Python dictionaries or GPU shaders.

## The Triad of Schemas (`RECORDING_SCHEMAS`)

Because GitGalaxy eventually pivots data from object-oriented Python into flattened C-style arrays for WebGL, array order is critical. The Analysis Lens hardcodes the exact order of elements for the entire pipeline:

### 1. `SIGNAL_SCHEMA` (The 60-Point Heuristic Matrix)
This defines the absolute layout of the raw telemetry extracted by the `LogicSplicer`. Every language's regex hits are aggregated into this exact 60-element array. It represents the foundational signal data of the file, including active logic (e.g., `branch`, `memory_alloc`), passive data (e.g., `doc`, `graveyard`), and raw security triggers (e.g., `sec_danger`, `sec_io`).

### 2. `RISK_SCHEMA` (The 18-Point Exposure Vector)
This schema defines the final, processed risk metrics calculated by the `SignalProcessor`. It transforms the raw 60-point signal array into 18 standardized exposures (e.g., `cognitive_load`, `tech_debt`, `logic_bomb`, `memory_corruption`). Every file in the visible galaxy receives a score from 0.0 to 100.0 for every element in this array.

### 3. `SAT_SCHEMA` (Satellite Data)
Defines the strict 10-element array used to flatten individual internal functions (Satellites) into the GPU manifest. It enforces the order of metrics like LOC, Control Flow Ratio, and Big-O Depth.

## The Translation Dictionaries

LLMs and human auditors cannot easily read raw backend keys like `sec_bitwise_hits` or `cog_raw`. The Analysis Lens contains the master translation maps utilized by the `AuditRecorder` and `LLMRecorder`:

* **`FRIENDLY_MAP`:** Translates raw heuristic keys into descriptive text (e.g., converting `sec_bitwise_hits` into "Sub-Atomic Decryption (Custom XOR)").
* **`EXPOSURE_LABELS`:** Formats the 18-point risk vector for the JSON audit (e.g., formatting `secrets_risk` as "Secrets Risk Exposure").
* **`GPU_TEXTURE_LOOKUPS`:** A fixed string-interning dictionary that maps functional archetypes (like `io`, `mutation`, `event`, `logic`) into strict integers so the GPU knows exactly which 3D material to apply to a satellite node.

## Mathematical Constants & Thresholds

The file houses the global physics constants used to calculate mass, momentum, and risk degradation:

* **Trust Constants (The Fog of War):** Defines the "Opacity Tax" for dynamically typed or implicit languages (like Shell or SQL). Languages with higher opacity receive an artificial boost to their baseline risk scores to account for runtime unpredictability.
* **Network Load-Bearing Multipliers:** Determines exactly how heavily PageRank and Betweenness scores are weighted when calculating a file's Systemic Threat Vector.
* **Security Tripewires:** Houses the exact floating-point thresholds (e.g., > 60.0%) that trigger the `ELEVATED_SURFACE_RISK` and `CRITICAL_THREATS_DETECTED` statuses in the final SHBOM audit.

## Architectural Stability

By centralizing these schemas, GitGalaxy achieves extreme stability. If a developer needs to add a new security metric to the engine, they do not have to update 15 different Python modules. They simply add the key to the `RISK_SCHEMA` array in the Analysis Lens, and the Splicer, Signal Processor, GPU Recorder, and Audit Recorder will automatically inherit, process, and serialize the new metric perfectly.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
