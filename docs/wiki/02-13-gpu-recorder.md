# The GPU Recorder (Hypercompressed Data Storage)

> **The Starmap**
>
> The GPU Recorder (`gpu_recorder.py`) is the instrument's high-performance recording head. It prepares project telemetry for real-time 3D WebGL/WebGPU rendering by transforming verbose, row-based JSON into a hypercompressed, columnar format. Unlike the Audit Recorder, it prioritizes memory efficiency, bandwidth reduction, and raw computational speed over human readability.

## Destructive RAM Eviction

To handle massive repositories without exhausting system memory, the engine employs an aggressive eviction strategy during the final serialization phase.

* **Iterative Destruction:** As each file (Star) or anomaly (Singularity) is converted into its columnar components, it is physically removed from the RAM-resident list using `.pop()`. This ensures the list is physically emptied as the new structure is built.
* **Explicit Garbage Collection:** The original object references are explicitly deleted (e.g., `del s`, `del d`), followed by a manual Python garbage collection cycle (`gc.collect()`) to completely clear the heap before the massive file-write operation.

## The Columnar Pivot & Dependency Graphing

The recorder converts the object-oriented manifest into a "Structure of Arrays" (SoA). It introduces advanced dependency graphing and Machine Learning clustering directly into this pivot:

* **Primary Arrays:** Parallel columns for spatial coordinates (`pos_x`, `pos_y`, `pos_z`), masses, and DNA signals (`cog_raw`, `raw_churn_freq`, `ownership_entropy`).
* **The WebGL Edge Engine:** The recorder builds a pre-computed Dependency Resolution Map *before* destruction. It maps every raw import to its target file's exact array index, generating `edges` (inbound connections) and `outbound_edges`. This allows the UI to render thousands of 3D relational lines instantly without performing expensive string-matching in the browser.
* **Satellite Minification:** Flattens the internal function (satellite) data into a single 1D array (`satellite_data_flat`), tracking block sizes using `satellite_offsets`. It reverses the chunks to maintain a highest-first order.
* **ML Archetypes & AI Threats:** Extracts dynamic Machine Learning fingerprint data (`a_ids`, `a_dists`) and injects the XGBoost AI Threat Confidence scores directly into a dedicated `ai_threats` column.

## String Interning & Numerical Quantization

To achieve maximum compression, the recorder eliminates repetitive text and floating-point bloat.

### String Interning Registries
Repeated strings are stored once in a master header registry and replaced in the columns with lightweight integer IDs. Registries include standard metadata (Languages, Authors, Proofs) as well as vectorized lookups for `ext_lookup`, `import_lookup`, `const_lookup` (Constellations), and `archetype_lookup` (ML Archetypes).

### Physics and Exposure Scaling
Floating-point values are precision-scaled and converted to integers to match the input expectations of vertex shaders:
* **Physics Scaling (x10):** Applied to Spatial Coordinates, Structural Mass, and Satellite Angles (e.g., `150.45` becomes `1505`).
* **Exposure Scaling (x1000):** Applied to AI Threat Scores, Control Flow Ratios, Ownership Entropy, and Author Distribution (e.g., a float `0.854` becomes `854`).

## Dynamic Lore & Final Sealing

Before final serialization, the recorder shapes the payload for the frontend UI:

* **Flattened Singularity:** The heavily nested Dark Matter composition statistics are flattened into a UI-friendly breakdown, explicitly separating formats and mapping their specific diagnostic reasons.
* **Dynamic Lore Injection:** Fetches the `PROJECT_STORIES` registry to inject the specific narrative, historical significance, and highlighted artifacts into the root of the GPU manifest, bridging the gap between raw data and human storytelling.
* **Final Sealing:** The JSON is serialized with `indent=None` and `separators=(',', ':')` to strip all whitespace, yielding the absolute lowest latency payload possible for the 3D visualizer.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
