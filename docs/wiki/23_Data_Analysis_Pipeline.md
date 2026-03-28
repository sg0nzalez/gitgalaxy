## 2.3. Data Analysis Pipeline (The Optical Pipeline)

Sometimes code is art. Right now, it's data, and it’s gotta be cleaned up to be meaningful. Basically, we need to assess what to assess, find what language it's in, strip out the comments, regex count, and then calculate risk based on standardization metrics. 

The GalaxyScope is a modular computational instrument designed to resolve raw source code into intuitive 3D physical structures. Rather than a standard "scanner," the system operates as an optical pipeline where each module serves as a discrete component housed within the GalaxyScope Chassis. 

Just as light flows through a telescope, data flows through our GalaxyScope. We adjust the aperture (what files are blocked), we use guidestars (creator’s READMEs), each file’s language is brought into focus, the data stream is sent through a prism to split the `coding_stream` from the `comment_stream` (comment parsing), each info stream is fed to a detector (regex count data), analyzed by a signal processor (2nd pass calculations, equations), and then validated by a spectral auditor (statistical anomaly analysis), where it is finally packaged by a record keeper (saved into a vectorized JSON). 

Just as different telescopes can have different lenses and prisms to see different things, I hope this architecture inspires people to build better versions of these things and view data analysis through the lens of scientific instrumentation.

Incoming data is treated as raw light. To resolve a clear image of the codebase, it must pass through the following interchangeable parts:

| The Component | Digital Module (`.py`) | Operational Function | "Optical" Result |
| :--- | :--- | :--- | :--- |
| **The Adaptive Light Path System** | `galaxyscope.py` | **Orchestrator.** Parses data through specific files and functions during the analysis. | The adaptive light path is able to swap lenses on the fly to ensure focus and visibility. |
| **The Aperture Filter** | `aperture_filter.py` | **Noise reduction.** Strips `.gitignore` noise, binaries, and minified artifacts. | **Clear Field:** Eliminates "Radio Noise" before it hits the sensors. |
| **The Security Lens** | `security_lens.py` | **The threat detection physics engine.** Scans raw structural realities using specialized heuristics to detect adversarial behaviors (obfuscated payloads, logic bombs, exfiltration vectors, and hardcoded secrets), evaluating them against dynamic policy thresholds. | **Threat Hunting:** Applies a specialized high-contrast filter to the incoming light, illuminating hostile anomalies, killer asteroids, and structural vulnerabilities. |
| **The GuideStar Protocol** | `guidestar_protocol.py` | **Calibration and indexing.** Ensures the instrument is focused on core architectural importance. Reads git lists, `package.json`, etc. | **Alignment:** Establishes the coordinate center of the survey. |
| **The Language Lens** | `language_lens.py` | **Language identification.** Compares lines of evidence (ext/shebang, system context) to assign a language to each file along with a confidence score, allowing us to thoroughly assess if our determinations seem plausible. | **Focus:** Spectral identification; determines if we have a lens to best focus that wavelength of light. |
| **The Prism** | `prism.py` | Once the language has been identified, the correct comment style can be applied to parse comments from code. | **Spectral Splitting:** Splits the wavelength of light into two streams that can be analyzed separately. |
| **The Primary Detector** | `detector.py` | **Heuristic sensor.** Performs high-speed regex counting to detect functional intent. | **Raw Signal:** Captures the discrete counts of logic hits. Where the photons hit the EMCCD chip. |
| **The Signal Processor** | `signal_processor.py` | **Equation engine.** Converts raw counts into non-linear risk exposures and physical mass. | **Analyzed Signal:** Transforms hits into meaningful 0-100 exposure scores. |
| **The Spectral Auditor** | `spectral_auditor.py` | **Bayesian Quality control.** If sample size permits, performs statistical Z-score checks to assess if files with low confidence language determinations have further evidence supporting that label. | **Integrity:** Relegates mysterious signals to the Singularity of Ambiguity to highlight unanalyzable signals. |
| **The Chronometer** | `chronometer.py` | **A high-fidelity temporal sensor.** Analyzes Git commit history and filesystem metadata to measure code churn, file stability, and ownership entropy. | **Temporal Telemetry:** Measures the "redshift" and volatility of artifacts over time, adding history and movement to the static star map. |
| **The Audit Recorder** | `audit_recorder.py` | Full level audit record of every file scanned, results and hits, saved into a large JSON archive. To make your lawyers happy. | **The SHBOM:** A permanent "Black Box" record (Structural Health Bill of Materials). |
| **The GPU Recorder** | `gpu_recorder.py` | **Vectorization.** Seals the processed signal into a lightweight, high-density JSON archive. | **The Starmap:** Converts analyzed data into galaxy format for the 3D rendering engine. |

---

### 2.3.0. The GalaxyScope Chassis – Optical Orchestration

The GalaxyScope (implemented as the `Orchestrator` class in `galaxyscope.py`) is the primary structural frame of the GitGalaxy engine. It serves as the physical chassis that houses and synchronizes every optical module, ensuring that raw source code flows through the system in a deterministic, scientific sequence. Without a central chassis, the individual sensors and lenses would lack the synchronization required to build a cohesive 3D map; the Orchestrator ensures that data is refracted, analyzed, and recorded with perfect temporal alignment.

#### 2.3.0.A. The Adaptive Lightpath System

The analysis is executed as a series of "Lightpath Phases." By organizing the pipeline into distinct sequential passes, the system can discard noise early, allowing the high-compute detectors to focus exclusively on verified logical matter, while enabling complex relational math (like dependency mapping and folder contexts) to be calculated globally.

* **2.3.0.A.1. Phase 0: The Radar Scan (Ignition)**
    The engine initiates by building a project "Census" using Git Authority (or a standard filesystem walk as a fallback). The Radar Scan identifies every artifact, performs pre-flight integrity checks to instantly discard phantom/missing files, and tallies extension frequencies. This creates the global context needed to calculate "Ecosystem Gravity" before the primary lenses ever engage.
* **2.3.0.A.2. Phase 1: Parallel Refraction (Map-Reduce)**
    Before calculating relational physics, the engine must map the dependency graph. A naive approach (checking every import against every file) creates a catastrophic O(N^2) computational bomb on massive repositories.
    * *The Optimization:* The chassis builds an O(1) Pre-computed Suffix Hash Map. This allows it to instantly resolve raw import strings (like `import core/utils`) to their exact physical files in a fraction of a second, tallying the "Popularity Score" that determines the gravitational center of the 3D galaxy.
* **2.3.0.A.3. Phase 2: Relational Physics (Global Aggregation)**
    Once the dependency graph is resolved, the chassis executes a Second Pass to calculate project-wide relationships that a single file cannot know in isolation.
    * *Domain Ontologies:* It tallies the languages in every folder to determine the "dominant ecosystem" of that neighborhood, passing this context to the physics engine to calculate Alien/Trojan penalties.
    * *The Global Test Umbrella:* It calculates the total percentage of the repository dedicated to testing, creating a global defense bonus.
    * *The Secrets Supernova Injection:* As a final safety measure before handing data to the GPU, the Orchestrator checks the "Dark Matter" reject pile. If the Security Lens flagged a filtered file for a Critical Credential Leak, the chassis artificially injects a "Supernova" onto the map—forcing the hardcoded secret to be rendered in the UI despite its architectural insignificance.

#### 2.3.0.B. Adaptive Features and Hardware Overrides

The GalaxyScope is designed as an "Open Chassis," capable of swapping lenses and patching logic on the fly based on the specific "Atmospheric Conditions" of the target repository.

* **2.3.0.B.1. The Domain Dialect Pre-Flight Patch**
    Before ignition, the chassis checks for "Project Overrides" in the scanning configuration. If a project name matches a registered Dialect, the engine live-patches the language regex geometry (updating both extensions and structural rules). Standard language rules often fail in projects with unique coding standards or internal DSLs. Dialect patching allows the instrument to recalibrate its "Spectral Focus" to match the local reality of a specific project without breaking the global standard.
* **2.3.0.B.2. Splicer Pre-loading**
    To prevent severe performance lag during parallel multiprocessing, the chassis "Force-Warms" the workers by pre-loading the `LogicSplicer` cache as soon as the worker process initializes.
    * *The "Plaintext Stutter":* If a worker had to lazily evaluate and compile the massive regex dictionaries for every single fallback file (like Markdown or Plaintext) mid-stream, it would create redundant `[AUTO-HEAL]` log spam and throttle the CPU.
    * *The Fix:* The Orchestrator passes the `ext_tally` (from the Phase 0 Census) to the workers, allowing them to pre-compile the exact regex rules needed for the active languages in the project, ensuring the data flows through the pipeline without interruption.
* **2.3.0.B.3. The Smart Threat Switch (Zero-Trust Mode)**
    The chassis allows the operator to swap the optical thresholds of the Security Lens at runtime. If the orchestrator is booted in `--paranoid` mode, the chassis injects a maximum-sensitivity threat policy into the engine. This dynamically lowers the tolerance thresholds for logic bombs, memory corruption, and injection surfaces, allowing security teams to audit high-risk environments with a "Zero-Trust" posture.
* **2.3.0.B.4. Exclusive Recorder Routing**
    Because the final stage of processing (pivoting the data for the WebGPU visualizer) requires destructively clearing RAM, the chassis features an intelligent output router. The Orchestrator can split the final telemetry stream into three distinct artifacts:
    * *The GPU Recorder:* Seals the processed signal into a lightweight, minified JSON archive for the 3D visualizer.
    * *The Audit Recorder:* Generates a comprehensive, human-readable forensic log.
    * *The LLM Recorder:* Generates AI-optimized markdown translations for agentic workflows. By passing exclusive flags (`--gpu-only`, `--audit-only`, `--llm-only`), the chassis can bypass unneeded formatting steps to save memory.
* **2.3.0.B.5. Shared Metadata Locking (The Session Lock)**
    As the mission concludes, the chassis generates a `session_meta` payload containing the Engine Identity, Scan Duration, and an immutable Git Audit (including Branch, SHA-1 Hash, Remote URL, and Latest Commit Date). The Session Lock ensures that every architectural map is permanently anchored to a specific point in the project's history, providing the "Black Box" data required for SBOM (Software Bill of Materials) compliance and legal audits.