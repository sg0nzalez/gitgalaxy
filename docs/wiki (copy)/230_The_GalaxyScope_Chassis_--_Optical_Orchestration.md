#### 2.3.0. The GalaxyScope Chassis -- Optical Orchestration

The GalaxyScope (implemented as the Orchestrator class in
galaxyscope.py) is the primary structural frame of the GitGalaxy engine.
It serves as the physical chassis that houses and synchronizes every
optical module, ensuring that raw source code flows through the system
in a deterministic, scientific sequence. Without a central chassis, the
individual sensors and lenses would lack the synchronization required to
build a cohesive 3D map; the Orchestrator ensures that data is
refracted, analyzed, and recorded with perfect temporal alignment.

##### 2.3.0.A. The Adaptive Lightpath System

The analysis is executed as a series of \"Lightpath Phases.\" By
organizing the pipeline into distinct sequential passes, the system can
discard noise early, allowing the high-compute detectors to focus
exclusively on verified logical matter, while enabling complex
relational math (like dependency mapping and folder contexts) to be
calculated globally.

###### 2.3.0.A.1. Phase 0: The Radar Scan (Ignition)

The engine initiates by building a project \"Census\" using Git
Authority (or a standard filesystem walk as a fallback). The Radar Scan
identifies every artifact, performs pre-flight integrity checks to
instantly discard phantom/missing files, and tallies extension
frequencies. This creates the global context needed to calculate
\"Ecosystem Gravity\" before the primary lenses ever engage.

###### 2.3.0.A.2. Phase 1: Parallel Refraction (Map-Reduce)

Before calculating relational physics, the engine must map the
dependency graph. A naive approach (checking every import against every
file) creates a catastrophic *O(N\^2)* computational bomb on massive
repositories.

-   **The Optimization:** The chassis builds an *O(1)* Pre-computed
Suffix Hash Map. This allows it to instantly resolve raw import
strings (like *import core/utils*) to their exact physical files in
a fraction of a second, tallying the \"Popularity Score\" that
determines the gravitational center of the 3D galaxy.

###### 2.3.0.A.3. Phase 2: Relational Physics (Global Aggregation)

Once the dependency graph is resolved, the chassis executes a Second
Pass to calculate project-wide relationships that a single file cannot
know in isolation.

-   **Domain Ontologies:** It tallies the languages in every folder to
determine the \"dominant ecosystem\" of that neighborhood, passing
this context to the physics engine to calculate Alien/Trojan
penalties.
-   **The Global Test Umbrella:** It calculates the total percentage of
the repository dedicated to testing, creating a global defense
bonus.
-   **The Secrets Supernova Injection:** As a final safety measure
before handing data to the GPU, the Orchestrator checks the \"Dark
Matter\" reject pile. If the Security Lens flagged a filtered file
for a *Critical Credential Leak*, the chassis artificially injects a
\"Supernova\" onto the map---forcing the hardcoded secret to be
rendered in the UI despite its architectural insignificance.

##### 2.3.0.B. Adaptive Features and Hardware Overrides

The GalaxyScope is designed as an \"Open Chassis,\" capable of swapping
lenses and patching logic on the fly based on the specific \"Atmospheric
Conditions\" of the target repository.

###### 2.3.0.B.1. The Domain Dialect Pre-Flight Patch

Before ignition, the chassis checks for \"Project Overrides\" in the
scanning configuration. If a project name matches a registered Dialect,
the engine live-patches the language regex geometry (updating both
extensions and structural rules). Standard language rules often fail in
projects with unique coding standards or internal DSLs. Dialect patching
allows the instrument to recalibrate its \"Spectral Focus\" to match the
local reality of a specific project without breaking the global
standard.

###### 2.3.0.B.2. Splicer Pre-loading

To prevent severe performance lag during parallel multiprocessing, the
chassis \"Force-Warms\" the workers by pre-loading the *LogicSplicer*
cache as soon as the worker process initializes.

-   **The \"Plaintext Stutter\":** If a worker had to lazily evaluate
and compile the massive regex dictionaries for every single fallback
file (like Markdown or Plaintext) mid-stream, it would create
redundant *\[AUTO-HEAL\]* log spam and throttle the CPU.
-   **The Fix:** The Orchestrator passes the *ext_tally* (from the Phase
0 Census) to the workers, allowing them to pre-compile the exact
regex rules needed for the active languages in the project, ensuring
the data flows through the pipeline without interruption.

###### 2.3.0.B.3. The Smart Threat Switch (Zero-Trust Mode)

The chassis allows the operator to swap the optical thresholds of the
Security Lens at runtime. If the orchestrator is booted in *\--paranoid*
mode, the chassis injects a maximum-sensitivity threat policy into the
engine. This dynamically lowers the tolerance thresholds for logic
bombs, memory corruption, and injection surfaces, allowing security
teams to audit high-risk environments with a \"Zero-Trust\" posture.

###### 2.3.0.B.4. Exclusive Recorder Routing

Because the final stage of processing (pivoting the data for the WebGPU
visualizer) requires destructively clearing RAM, the chassis features an
intelligent output router. The Orchestrator can split the final
telemetry stream into three distinct artifacts:

-   **The GPU Recorder:** Seals the processed signal into a lightweight,
minified JSON archive for the 3D visualizer.
-   **The Audit Recorder:** Generates a comprehensive, human-readable
forensic log.
-   **The LLM Recorder:** Generates AI-optimized markdown translations
for agentic workflows. By passing exclusive flags (*\--gpu-only*,
*\--audit-only*, *\--llm-only*), the chassis can bypass unneeded
formatting steps to save memory.

###### 2.3.0.B.5. Shared Metadata Locking (The Session Lock)

As the mission concludes, the chassis generates a *session_meta* payload
containing the Engine Identity, Scan Duration, and an immutable Git
Audit (including Branch, SHA-1 Hash, Remote URL, and Latest Commit
Date). The Session Lock ensures that every architectural map is
permanently anchored to a specific point in the project\'s history,
providing the \"Black Box\" data required for SBOM (Software Bill of
Materials) compliance and legal audits.
