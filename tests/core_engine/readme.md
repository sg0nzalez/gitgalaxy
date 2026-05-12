### 🌌 The Core Engine Test Index

This directory is the beating heart of GitGalaxy's structural physics. It validates the AST-free parsers, ReDoS shields, execution lifecycle, and mathematical models that allow the engine to operate flawlessly under extreme, adversarial conditions.

**1. `test_aperture.py` (The Solar Shield)**
* **Purpose:** Validates the first line of defense against noise, binary debris, and oversized payloads.
* **Mechanics Tested:** * **The Lead Shield:** Ensures AI weights (`.safetensors`) and critical secrets (`.pem`) instantly bypass standard optical logic.
    * **The Semantic Path Gate:** Verifies that infrastructure paths (like `node_modules/` or `vendor/`) are dropped unless explicitly overridden by a GuideStar Intent Lock.
    * **The Auto-Gen Shield:** Detects machine-generated HTML/docs and dynamically infects the parent directory to save I/O overhead on subsequent files.
    * **The Embedded Hex Array Shield:** Proves that massive C-header data payloads (hex arrays) are forcibly dropped to protect the regex engine, even if the file possesses a VIP intent lock.
    * **The Infrared Gate:** Proves that massive, minified single-line strings (e.g., 1600+ chars) are cleanly shunted to prevent regex saturation, while exempting prose files like Markdown.

**2. `test_chronometer_timeout.py` (The Hardware Guillotine)**
* **Purpose:** Proves the engine can survive catastrophic infinite loops during Git stream ingestion.
* **Mechanics Tested:** Validates the zombie process kill switch. Simulates a hanging `git log` process and ensures the OS-level `SIGKILL` is sent, pipes are forcefully flushed, and file descriptors are closed to prevent RAM and FD leaks.

**3. `test_detector.py` (The Logic Splicer)**
* **Purpose:** Tests the primary structural extraction engine (AST-free parsing).
* **Mechanics Tested:**
    * **Algorithmic Physics:** Proves the engine can calculate $O(N)$ nesting depth natively via indentation and flag exponential $O(2^N)$ recursion without building an AST.
    * **AppSec Spatial Correlation:** Verifies that threat penalties (e.g., memory scraping combined with a socket send) multiply exponentially if they occur within the same "blast radius" (e.g., 200 characters).
    * **Silencer Regions:** Ensures danger signals (like `strcpy`) are neutralized if wrapped inside a safe context (like `strncpy`).
    * **Anti-ReDoS Line Limiter:** Proves that massive 2000+ character blobs are safely blanked out before hitting the regex engine, preserving LOC counts without locking the CPU.
    * **Mode E (Terminator Cleaving):** Validates that declarative languages (like SQL) are cleanly split by their terminators (`;`) rather than scope braces.

**4. `test_galaxyscope.py` (The Pipeline Orchestrator)**
* **Purpose:** Performs end-to-end integration testing of the entire GitGalaxy mission lifecycle.
* **Mechanics Tested:** Runs a micro-repository (the `iwubi` fixture) through the full pipeline to guarantee that all four output recorders (GPU JSON, Audit JSON, LLM Markdown, and native SQLite DB) fire successfully, populate with valid data, and trigger the CLI success billboard.

**5. `test_guidestar_lens.py` (Sector Intelligence)**
* **Purpose:** Validates the Bayesian "Social Proof" engine that overrides raw syntax heuristics.
* **Mechanics Tested:**
    * **Roadmap Scout:** Parses `package.json` to identify entry points and detect AI ecosystems (e.g., `langchain`).
    * **Authority Scout:** Proves that `.gitattributes` linguistic overrides lock the parser to a specific language with 99% confidence.
    * **Evasion Tactics:** Detects when an attacker uses `.gitignore` to force-include a compiled binary (e.g., `!payload.so`), triggering a max-priority alarm.
    * **Sector Bias:** Ensures files located in structurally important directories (`src/`, `core/`) receive a dynamic intent priority boost.

**6. `test_language_lens.py` (Dialect Detection)**
* **Purpose:** Tests the security boundaries of file identification.
* **Mechanics Tested:** Validates the "Identity Crisis Trap"—if a file claims to be a harmless `.txt` file but contains a `#!/bin/bash` shebang, the engine successfully strips its identity, flags the anomaly, and banishes it to Tier 5 (Absolute Distrust).

**7. `test_language_standards_strict.py` (The Blast Chamber)**
* **Purpose:** The ultimate ReDoS (Regular Expression Denial of Service) proving ground.
* **Mechanics Tested:** Fires pathological, maliciously formatted strings at the engine inside an isolated process pool with a 0.1-second fuse.
    * **C/C++ K&R Ambiguity Trap:** Survives massive parameter gaps and the MS-DOS `BEGIN` macro.
    * **C# "Iron Wall":** Defeats return-type spirals on deeply nested generics.
    * **C++ Macro Multiline Spiral:** Prevents regex from crossing into preprocessor directives.
    * **Pointer Ambiguity Overlap:** Proves O(1) alternation prevents exponential evaluation on asterisk strings.
    * **COBOL Ghost Satellite Prevention:** Blocks indented SQL columns or `01` data levels from hallucinating as paragraphs.
    * **Thermodynamic Operator Collisions:** Ensures operators don't cannibalize each other (e.g., C++ bitwise `<<` ignoring `std::cout <<`).
    * **Global Fuzzer:** Iterates over all 1,200+ regexes to ensure compilation integrity.

**8. `test_prism.py` (Structural Refraction)**
* **Purpose:** Tests the "Optical Split" that separates executable logic from ghost mass (comments/literature).
* **Mechanics Tested:**
    * **Prose & Metadata Bypasses:** Ensures Shebangs and markdown files survive refraction intact.
    * **String Shielding:** Ensures that URLs like `https://github.com` inside a string literal do not accidentally trigger the `//` comment stripper.
    * **Nested Block Peeler:** Proves the engine can iteratively peel recursively nested comments (`/* /* */ */`) common in Rust, Swift, and Scala.
    * **Positional Anchors:** Validates column-specific comment stripping for legacy formats like COBOL and Fortran.
    * **Hardened Python Docstrings:** Correctly extracts `"""` multi-line strings into the documentation stream.

**9. `test_signal_processor.py` (The Physics Engine)**
* **Purpose:** Validates the 18-point risk exposure math and structural mass equations.
* **Mechanics Tested:**
    * **Zero-State Resiliency:** Ensures completely empty files do not trigger `ZeroDivisionError` crashes.
    * **Sigmoid Overflow Clamping:** Proves that mathematically absurd densities (e.g., 50,000 branches on 1 line of minified code) trigger the Overflow rescue block and clamp strictly to 100.0.
    * **Inert Mass Bypass:** Verifies that documentation files skip the logic risk engine entirely, registering 0.0 for execution risks while maintaining their physical mass.
    * **Temporal Normalization:** Proves the engine dynamically finds the global maximum churn in a repository and scales all other files logarithmically against it.

**10. `test_state_rehydrator.py` (The Delta Engine Memory)**
* **Purpose:** Validates the SQLite-backed RAM rehydration for Delta scans.
* **Mechanics Tested:** Proves the system can gracefully handle Cold Starts and Ghost Repositories (missing data). Validates Temporal Accuracy by fetching the most recent commit based on time, and verifies the exact schema mapping of flat SQL columns back into the deeply nested `cryolink` dictionary required by the orchestrator.

**11. `test_zero_dependency.py` (The Environmental Fallback)**
* **Purpose:** Proves the system degrades gracefully in restrictive environments.
* **Mechanics Tested:** Ensures that running GalaxyScope without heavy C-backed libraries (`networkx`, `xgboost`, `pandas`, `tiktoken`) does not hard-crash the `SignalProcessor` or `SecurityAuditor`. It validates that None-type fallbacks safely populate as 0.0 floats and bypass ML inferences without breaking the dependency graph mapping.