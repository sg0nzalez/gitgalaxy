# 2.3.10. The GPU Recorder (Hypercompressed Data Storage)

> **The Starmap**
>
> The GPU Recorder (`gpu_recorder.py`) is the instrument's high-performance recording head. It prepares project telemetry for real-time 3D WebGL rendering by transforming verbose, row-based JSON into a hypercompressed, columnar format. Unlike the Audit Recorder, it prioritizes memory efficiency, bandwidth reduction, and raw computational speed over human readability.

## 2.3.10.A. Destructive RAM Eviction (Stage 3.3 Protocol)

To handle massive repositories (10,000+ files) without exhausting system memory, the engine employs an aggressive eviction strategy during the final serialization phase.

* **Iterative Destruction:** As each file (Star) is converted into its columnar components, it is physically removed from the RAM-resident list using `.pop()`.
* **Explicit Garbage Collection:** The original object references are explicitly deleted (`del s`), followed by a manual Python garbage collection cycle (`gc.collect()`) to completely clear the heap before the massive file-write operation.

## 2.3.10.B. The Columnar Pivot & Dependency Graphing

The recorder converts the object-oriented manifest into a "Structure of Arrays" (SoA). The v6.2.0 Protocol introduces advanced dependency graphing directly into this pivot:

* **Primary Arrays:** Parallel columns for spatial coordinates (`pos_x`, `pos_y`, `pos_z`), masses, and the new DNA signals (`cog_raw`, `raw_churn_freq`, `ownership_entropy`).
* **The WebGL Edge Engine:** The recorder builds a pre-computed Dependency Resolution Map. It maps every raw import to its target file's exact array index, generating `edges` (inbound connections) and `outbound_edges`. This allows the UI to render thousands of 3D relational lines instantly without performing expensive string-matching in the browser.

## 2.3.10.C. String Interning & Numerical Quantization

To achieve maximum compression, the recorder eliminates repetitive text and floating-point bloat.

### 1. String Interning Registries
Repeated strings are stored once in a master header registry and replaced in the columns with lightweight integer IDs. Registries include standard metadata (Languages, Authors) as well as the newly added `import_lookup`, `ext_lookup`, and `const_lookup` (Constellations).

### 2. Physics and Exposure Scaling
Floating-point values are precision-scaled and converted to integers to match the input expectations of vertex shaders:
* **Physics Scaling (x10):** Applied to Spatial Coordinates and Structural Mass (e.g., `150.45` becomes `1505`).
* **Exposure Scaling (x1000):** Applied to the 18-point Risk Vectors and Control Flow Ratios (e.g., `85.4%` becomes `854`).

## 2.3.10.D. Dynamic Lore & Final Sealing

Before final serialization, the recorder shapes the payload for the frontend UI:

* **Flattened Singularity:** The heavily nested Dark Matter statistics are flattened into a UI-friendly breakdown, explicitly separating binaries, unparsable formats, and OS permission blocks.
* **Dynamic Lore Injection:** Fetches the `PROJECT_STORIES` registry to inject the specific narrative, historical significance, and highlighted artifacts into the root of the GPU manifest, bridging the gap between raw data and human storytelling.
* **Final Sealing:** The JSON is serialized with `indent=None` and `separators=(',', ':')` to strip all whitespace, yielding the absolute lowest latency payload possible for the 3D visualizer.
