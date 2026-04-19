# Data Analysis Pipeline (The Optical Pipeline)

Sometimes code is art. Right now, it's data, and it’s gotta be cleaned up to be meaningful. Basically, we need to assess what to assess, find what language it's in, strip out the comments, regex count, and then calculate risk based on standardization metrics. 

The GalaxyScope is a modular computational instrument designed to resolve raw source code into intuitive 3D physical structures. Rather than a standard "scanner," the system operates as an optical pipeline where each module serves as a discrete component housed within the GalaxyScope Chassis. 

Just as light flows through a telescope, data flows through our GalaxyScope. We adjust the aperture (what files are blocked), we use guidestars (creator’s READMEs), each file’s language is brought into focus, the data stream is sent through a prism to split the `coding_stream` from the `comment_stream` (comment parsing), each info stream is fed to a detector (regex count data), analyzed by a signal processor (2nd pass calculations, equations), and then validated by a spectral auditor (statistical anomaly analysis), where it is finally packaged by a record keeper (saved into a vectorized JSON). 

Just as different telescopes can have different lenses and prisms to see different things, I hope this architecture inspires people to build better versions of these things and view data analysis through the lens of scientific instrumentation.

Incoming data is treated as raw light. To resolve a clear image of the codebase, it must pass through the following interchangeable parts:

| The Component | Digital Module (`.py`) | Operational Function | "Optical" Result |
| :--- | :--- | :--- | :--- |
| **The Adaptive Light Path System** | `galaxyscope.py` | **Orchestrator.** Parses data through specific files and functions during the analysis. | The adaptive light path is able to swap lenses on the fly to ensure focus and visibility. |
| **The Aperture Filter** | `aperture.py` | **Noise reduction.** Strips `.gitignore` noise, binaries, and minified artifacts. | **Clear Field:** Eliminates "Radio Noise" before it hits the sensors. |
| **The GuideStar Protocol** | `guidestar_lens.py` | **Calibration and indexing.** Ensures the instrument is focused on core architectural importance. Reads git lists, `package.json`, etc. | **Alignment:** Establishes the coordinate center of the survey. |
| **The Language Lens** | `language_lens.py` | **Language identification.** Compares lines of evidence (ext/shebang, system context) to assign a language to each file along with a confidence score. | **Focus:** Spectral identification; determines if we have a lens to best focus that wavelength of light. |
| **The Prism** | `prism.py` | Once the language has been identified, the correct comment style can be applied to parse comments from code. | **Spectral Splitting:** Splits the wavelength of light into two streams that can be analyzed separately. |
| **The Primary Detector** | `detector.py` | **Heuristic sensor.** Performs high-speed regex counting to detect functional intent and algorithmic complexity. | **Raw Signal:** Captures the discrete counts of logic hits. Where the photons hit the EMCCD chip. |
| **The Signal Processor** | `signal_processor.py` | **Equation engine.** Converts raw counts into non-linear risk exposures and physical mass. | **Analyzed Signal:** Transforms hits into meaningful 0-100 exposure vectors. |
| **The Spectral Auditor** | `spectral_auditor.py` | **Bayesian Quality control.** Performs statistical Z-score checks to assess if files with low confidence determinations have evidence supporting that label. | **Integrity:** Relegates mysterious signals to the Singularity of Ambiguity to highlight unanalyzable signals. |
| **The Chronometer** | `chronometer.py` | **Temporal sensor.** Analyzes Git commit history and filesystem metadata to measure code churn and stability. | **Temporal Telemetry:** Measures the volatility of artifacts over time, adding history to the map. |
| **The Network Risk Sensor** | `network_risk_sensor.py` | **Graph Topology.** Wires the universe into a Directed Graph to calculate systemic threats. | **Blast Radius:** Determines PageRank, choke points (Betweenness), and ecosystem roles. |
| **The Security Lens** | `security_lens.py` | **Threat detection physics.** Scans raw structural realities for adversarial behaviors (logic bombs, exfiltration, hardcoded secrets). | **Threat Hunting:** Applies a specialized high-contrast filter to illuminate hostile anomalies. |
| **The AI AppSec Sensor** | `ai_appsec_sensor.py` | **Agentic Vulnerability Hunter.** Scans for weaponized AI architectures and LLM prompt injection surfaces. | **The RCE Funnel:** Identifies where LLMs possess unsafe access to OS commands or databases. |
| **The Dev Agent Firewall** | `dev_agent_firewall.py` | **AI Guardrails.** Evaluates if the codebase is safe for autonomous AI agents to modify. | **Token Physics:** Flags context-window black holes and hallucination zones requiring human-in-the-loop. |
| **The Neural Auditor** | `neural_auditor.py` | **Weight Inspection.** Surgically parses massive AI model binaries (.safetensors, .gguf) without RAM bloat. | **Model Metadata:** Extracts architecture, parameters, and quantization from binary headers. |
| **The Security Auditor** | `security_auditor.py` | **Machine Learning Inference.** Executes XGBoost multiclass threat inference across the entire resolved graph. | **AI Threat Confidence:** Predicts the probability of Trojans, Botnets, and Native Infectors. |
| **The Audit Recorder** | `audit_recorder.py` | Full level audit record of every file scanned, results and hits, saved into a large JSON archive. To make your lawyers happy. | **The SHBOM:** A permanent "Black Box" record (Structural Health Bill of Materials). |
| **The Record Keeper** | `record_keeper.py` | **Native SQLite.** Transforms the live RAM state directly into a highly relational SQLite database. | **Master Aggregation:** Bypasses intermediate JSON parsing for advanced SQL analysis. |
| **The LLM Recorder** | `llm_recorder.py` | **AI Translation Layer.** Compresses the galaxy into a high-density Markdown brief. | **Agent Context:** Provides standard LLMs with architectural context windows. |
| **The GPU Recorder** | `gpu_recorder.py` | **Vectorization.** Seals the processed signal into a lightweight, high-density JSON archive. | **The Starmap:** Converts analyzed data into galaxy format for the 3D WebGPU rendering engine. |

---

## The GalaxyScope Chassis – Optical Orchestration

The GalaxyScope (implemented as the `Orchestrator` class in `galaxyscope.py`) is the primary structural frame of the GitGalaxy engine. It serves as the physical chassis that houses and synchronizes every optical module, ensuring that raw source code flows through the system in a deterministic, scientific sequence. Without a central chassis, the individual sensors and lenses would lack the synchronization required to build a cohesive 3D map; the Orchestrator ensures that data is refracted, analyzed, and recorded with perfect temporal alignment.

### The Adaptive Lightpath System

The analysis is executed as a series of "Lightpath Phases." By organizing the pipeline into distinct sequential passes, the system can discard noise early, allowing the high-compute detectors to focus exclusively on verified logical matter, while enabling complex relational math (like dependency mapping and network topology) to be calculated globally.

* **Phase 0: The Radar Scan (Ignition)**
    The engine initiates by building a project "Census" using Git Authority (or a standard filesystem walk as a fallback). The Radar Scan identifies every artifact, tallies extension frequencies, and enforces the Neighborhood Micro-Mass Quota to eliminate micro-debris. This creates the global context needed to calculate "Ecosystem Gravity."
* **Phase 1: Workers & IPC Transfer (Map-Reduce)**
    The chassis utilizes a multi-core ProcessPoolExecutor to scatter artifacts into isolated worker memory spaces for concurrent analysis. This bypasses the Python GIL, passing files through the Aperture Filter, Language Lens, Prism, and Primary Detector. To prevent Catastrophic Backtracking (ReDoS) from freezing the thread pool, a hardware-level Guillotine interrupt (15-second fuse) is attached to the regex engine.
* **Phase 1.5: Dependency Resolution & Typosquatting Radar**
    Before calculating relational physics, the engine must map the dependency graph. 
    * *The Optimization:* The chassis builds an O(1) Pre-computed Suffix Hash Map to instantly resolve raw import strings to their exact physical files.
    * *The Air-Gapped Radar:* It simultaneously executes a Levenshtein-distance Typosquatting check on external dependencies, injecting "Homoglyph" threats into the pipeline before Phase 2.
* **Phase 2: Relational Physics**
    The chassis executes a global pass to calculate project-wide relationships. It evaluates Domain Ontologies (determining the dominant ecosystem of a folder to apply Alien/Trojan penalties) and calculates the Global Test Umbrella (applying defensive density bonuses repository-wide).
* **Phase 3: Network Topology & Blast Radius**
    The `NetworkRiskSensor` wires the universe into a Directed Graph using the resolved imports. It calculates PageRank (absolute load-bearing gravity), Betweenness (choke points), and Closeness (ripple effects), defining each file's exact Ecosystem Role.
* **Phase 3.5: AI Guardrails & AppSec Threat Hunting**
    The `DevAgentFirewall` and `AIAppSecSensor` evaluate the entire ecosystem for agentic vulnerabilities, hunting for over-permissioned "God-Mode" agents, context-window black holes, and prompt injection surfaces.
* **Phase 4: Audit Verification**
    The `SpectralAuditor` executes Bayesian quality control, relegating mathematically hollow or misidentified files into the Dark Matter Singularity.
* **Phase 5: 3D Cartography**
    The `Cartographer` transforms the verified flat list into a deterministic 3D star map utilizing a Ray-Casting Dynamic Mask to spatially hash and layout constellations.
* **Phase 6: Metrics Synthesis**
    The `SignalProcessor` executes Pass 2 Normalization, generating the forensic report and evaluating Biaxial Anomalies (Global vs Local architectural drift).
* **Phase 7.8: Advanced ML Threat Hunting**
    The `SecurityAuditor` ingests the fully resolved feature matrix into an XGBoost Multiclass inference model, predicting the probability of malicious payloads (Trojans, Botnets, Native Infectors) natively in RAM.
* **Phase 8-9: Multi-Format Recording**
    The mission concludes by routing the finalized state through the designated Recorders (Audit, LLM, SQLite, GPU) based on the operator's output parameters.

### Adaptive Features and Hardware Overrides

The GalaxyScope is designed as an "Open Chassis," capable of swapping lenses and patching logic on the fly based on the specific "Atmospheric Conditions" of the target repository.

* **The Domain Dialect Pre-Flight Patch**
    Before ignition, the chassis checks for "Project Overrides" in the scanning configuration. If a project name matches a registered Dialect (e.g., CPython, Ansible, Redis), the engine live-patches the language regex geometry and custom Aperture shields to match the local reality of the project without breaking global standards.
* **Splicer Pre-loading**
    To prevent severe performance lag during parallel multiprocessing, the chassis "Force-Warms" the workers by pre-loading the `LogicSplicer` cache as soon as the worker process initializes, preventing redundant regex compilation logs and CPU throttling on standard text files.
* **The Smart Threat Switch (Zero-Trust Mode)**
    If the orchestrator is booted in `--paranoid` mode, the chassis injects a maximum-sensitivity threat policy into the engine. This dynamically lowers the tolerance thresholds for logic bombs and memory corruption, allowing security teams to audit high-risk environments with a "Zero-Trust" posture.
* **Neural Supernova Injection**
    As a final safety measure before graphing, the Orchestrator checks the "Dark Matter" pile. If the `NeuralAuditor` or `SecurityLens` flagged a filtered file (like a 4GB `.safetensors` model or a leaked `.pem` key), the chassis artificially injects a "Supernova" onto the map—forcing the massive localized threat to render in the UI despite being structurally inert.
* **Delta Missions (RAM Rehydration)**
    For continuous integration, the GalaxyScope supports `execute_delta_mission`. Rather than re-scanning 10,000 files, the chassis rehydrates the previous scan's state directly into RAM, surgically processes only the modified files through the Optical Pipeline (Pass 1), and then instantly recalculates the entire Network Graph and ML Inference (Passes 2-7) in a fraction of the time.
* **Exclusive Recorder Routing**
    Because the final stage of processing requires destructively clearing RAM, the chassis features an intelligent output router. By passing exclusive flags (`--gpu-only`, `--audit-only`, `--llm-only`, `--db-only`), the chassis can bypass unneeded formatting steps (like the SQLite schema construction or Markdown parsing) to save memory and I/O latency.
* **Shared Metadata Locking (The Session Lock)**
    As the mission concludes, the chassis generates a `session_meta` payload containing the Engine Identity, Scan Duration, and an immutable Git Audit (including Branch, SHA-1 Hash, Remote URL, and Latest Commit Date). The Session Lock ensures that every architectural map is permanently anchored to a specific point in the project's history.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

