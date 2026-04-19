# The GalaxyScope Chassis (Optical Orchestration)

> **The Primary Structural Frame**
>
> The GalaxyScope (implemented as the `Orchestrator` class in `galaxyscope.py`) is the primary structural frame of the GitGalaxy engine. It serves as the physical chassis that houses and synchronizes every optical module, ensuring that raw source code flows through the system in a deterministic, scientific sequence. Without a central chassis, the individual sensors and lenses would lack the synchronization required to build a cohesive 3D map; the Orchestrator ensures that data is refracted, analyzed, and recorded with perfect temporal alignment.

## The Adaptive Lightpath System

The analysis is executed as a series of "Lightpath Phases." By organizing the pipeline into distinct sequential passes, the system can discard noise early, allowing the high-compute detectors to focus exclusively on verified logical matter. It also ensures that complex relational math (like dependency mapping, network topology, and AI threat inference) is calculated globally across the entire repository structure.

### Phase 0: The Radar Scan (Ignition)
The engine initiates by building a project "Census" using Git Authority (or a standard filesystem walk as a fallback). The Radar Scan identifies every artifact, performs pre-flight integrity checks to instantly discard phantom/missing files, and tallies extension frequencies. It also enforces the Neighborhood Micro-Mass Quota to filter out low-value debris, creating the global context needed to calculate "Ecosystem Gravity."

### Phase 1: Parallel Refraction (Map-Reduce)
The chassis utilizes a multi-core ProcessPoolExecutor to scatter artifacts into isolated worker memory spaces for concurrent analysis. This bypasses the Python Global Interpreter Lock (GIL), pushing files through the Aperture Filter, Language Lens, Prism, and Primary Detector simultaneously. To prevent Catastrophic Backtracking (ReDoS) from freezing the thread pool, a hardware-level Guillotine interrupt (a 15-second fuse) is attached to the regex engine.

### Phase 1.5: Dependency Resolution & Typosquatting Radar
Before calculating relational physics, the engine must map the dependency graph. A naive approach creates a catastrophic O(N^2) computational bomb on massive repositories.
* **The Optimization:** The chassis builds an O(1) Pre-computed Suffix Hash Map. This instantly resolves raw import strings to their exact physical files.
* **The Air-Gapped Radar:** Simultaneously, it executes a fast Levenshtein-distance Typosquatting check on external dependencies, injecting "Homoglyph" threats into the pipeline before Phase 2.

### Phase 2: Relational Physics (Global Aggregation)
The chassis executes a global pass to calculate project-wide relationships that a single file cannot know in isolation.
* **Domain Ontologies:** It tallies the languages in every folder to determine the "dominant ecosystem" of that neighborhood, passing this context to the physics engine to calculate Alien/Trojan penalties.
* **The Global Test Umbrella:** It calculates the total percentage of the repository dedicated to testing, creating a global defense bonus.

### Phase 3: Network Topology & Blast Radius
The `NetworkRiskSensor` wires the universe into a Directed Graph using the resolved imports. It calculates PageRank (absolute load-bearing gravity), Betweenness (choke points), and Closeness (ripple effects), defining each file's exact Ecosystem Role and systemic threat vector.

### Phase 3.5: AI Guardrails & AppSec Threat Hunting
The `DevAgentFirewall` and `AIAppSecSensor` evaluate the entire ecosystem for agentic vulnerabilities, hunting for over-permissioned "God-Mode" agents, context-window black holes, and prompt injection surfaces that could lead to Agentic RCE.

### Phase 4: Audit Verification
The `SpectralAuditor` executes Bayesian quality control. It enforces the "50/0 Law" and Z-Score linguistic density checks, relegating mathematically hollow or misidentified files into the Dark Matter Singularity.

### Phase 5: 3D Cartography
The `Cartographer` transforms the verified flat list into a deterministic 3D star map utilizing a Ray-Casting Dynamic Mask. This spatial hashing ensures constellations orbit their heavy "Suns" without colliding.

### Phase 6: Metrics Synthesis
The `SignalProcessor` executes Pass 2 Normalization (scaling metrics like Churn logarithmically against the repository's maximum) and evaluates Biaxial Anomalies (Global vs Local architectural drift).

### Phase 7.8: Advanced ML Threat Hunting
The `SecurityAuditor` ingests the fully resolved feature matrix into an XGBoost Multiclass inference model, predicting the exact probability of malicious payloads (Trojans, Botnets, Native Infectors) natively in RAM.

### Phase 8 & 9: Multi-Format Recording
The mission concludes by routing the finalized state through the designated Recorders (Audit, LLM, SQLite, GPU) based on the operator's output parameters.

---

## Adaptive Features and Hardware Overrides

The GalaxyScope is designed as an "Open Chassis," capable of swapping lenses and patching logic on the fly based on the specific "Atmospheric Conditions" of the target repository.

### The Domain Dialect Pre-Flight Patch
Before ignition, the chassis checks for "Project Overrides" in the scanning configuration. If a project name matches a registered Dialect (e.g., `cpython`, `ansible`), the engine live-patches the language regex geometry (updating both extensions and structural rules). Dialect patching allows the instrument to recalibrate its "Spectral Focus" to match the local reality of a specific project without breaking the global standard.

### Splicer Pre-loading
To prevent severe performance lag during parallel multiprocessing, the chassis "Force-Warms" the workers by pre-loading the `LogicSplicer` cache as soon as the worker process initializes.
* **The "Plaintext Stutter":** If a worker had to lazily evaluate and compile massive regex dictionaries for fallback files mid-stream, it would create redundant `[AUTO-HEAL]` log spam and throttle the CPU.
* **The Fix:** The Orchestrator passes the `ext_tally` (from the Phase 0 Census) to the workers, allowing them to pre-compile the exact regex rules needed for the active languages in the project.

### The Smart Threat Switch (Zero-Trust Mode)
The chassis allows the operator to swap the optical thresholds of the Security Lens at runtime. If the orchestrator is booted in `--paranoid` mode, the chassis injects a maximum-sensitivity threat policy into the engine. This dynamically lowers the tolerance thresholds for logic bombs, memory corruption, and injection surfaces, allowing security teams to audit high-risk environments with a "Zero-Trust" posture.

### Supernova Injections
As a final safety measure before handing data to the GPU, the Orchestrator checks the "Dark Matter" reject pile to artificially inject massive localized threats onto the 3D map.
* **Secrets Supernova:** Forces leaked credentials or API keys (flagged by the Security Lens) to render as critical threats.
* **Neural Supernova:** Extracts architecture and parameters from massive, inert AI model weights (`.safetensors`, `.gguf`), rendering them visually to show heavy local compute gravity.

### Delta Missions (RAM Rehydration)
For rapid continuous integration, the GalaxyScope supports `execute_delta_mission`. Rather than re-scanning tens of thousands of files, the chassis rehydrates the previous scan's state directly into RAM, surgically processes only the added/modified files through the Optical Pipeline (Pass 1), and then instantly recalculates the entire Network Graph and ML Inference (Passes 2-7) in a fraction of the time.

### Exclusive Recorder Routing
Because the final stage of processing (pivoting the data for WebGPU) requires destructively clearing RAM, the chassis features an intelligent output router. By passing exclusive flags (`--gpu-only`, `--audit-only`, `--llm-only`, `--db-only`), the chassis can bypass unneeded formatting steps (like compiling the Markdown brief or building the SQLite schema) to save memory and reduce I/O latency.

### Shared Metadata Locking (The Session Lock)
As the mission concludes, the chassis generates a `session_meta` payload containing the Engine Identity, Scan Duration, and an immutable Git Audit (including Branch, SHA-1 Hash, Remote URL, and Latest Commit Date). The Session Lock ensures that every architectural map is permanently anchored to a specific point in the project's history, providing the "Black Box" data required for SBOM (Software Bill of Materials) compliance and legal audits.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

