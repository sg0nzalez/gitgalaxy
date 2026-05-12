# 🌌 GitGalaxy Master Test Suite

This directory contains the testing architecture for the GitGalaxy engine. 

GitGalaxy operates as an **AST-free, polyglot structural parser**. Because it relies on heavily bounded mathematical regex and structural physics rather than standard compiler toolchains, this test suite is designed to aggressively validate structural extraction, prevent Catastrophic Backtracking (ReDoS), and ensure absolute accuracy across 30+ programming languages.

---

## 📂 Architectural File Index

### 1. `/core_engine` (The Physics & Parsing Core)
This domain is the beating heart of GitGalaxy's structural physics. It validates the AST-free parsers, ReDoS shields, execution lifecycle, and mathematical models that allow the engine to operate flawlessly under extreme, adversarial conditions.

* `test_aperture.py` - Validates the Solar Shield. Proves the Lead Shield instantly blocks AI weights (`.safetensors`) and secrets (`.pem`). Validates the Semantic Path Gate, the Auto-Gen dynamic infection shield, the Embedded Hex Array Shield, and the Infrared Gate (minification saturation).
* `test_chronometer_timeout.py` - Validates the Hardware Guillotine. Simulates a hanging `git log` process and ensures the OS-level `SIGKILL` is sent, pipes are forcefully flushed, and file descriptors are closed to prevent RAM and FD leaks.
* `test_detector.py` - Tests the Logic Splicer (AST-free parsing). Proves the engine calculates $O(N)$ nesting depth natively, flags exponential $O(2^N)$ recursion, applies AppSec Spatial Correlation (blast radius multipliers), and safely implements the Anti-ReDoS Line Limiter.
* `test_galaxyscope.py` - Performs end-to-end integration testing of the entire mission lifecycle, guaranteeing all four output recorders (GPU, Audit, LLM, SQLite) fire successfully.
* `test_guidestar_lens.py` - Validates the Bayesian "Social Proof" engine. Parses `package.json` for AI ecosystems, enforces `.gitattributes` authority, detects `.gitignore` evasion tactics, and applies Sector Bias.
* `test_language_lens.py` - Tests the Identity Crisis Trap—ensuring files claiming to be `.txt` but containing `#!/bin/bash` are stripped of identity and banished to Tier 5 (Absolute Distrust).
* `test_language_standards_strict.py` - The ultimate ReDoS proving ground. Fires pathological formatting (C/C++ K&R Ambiguity, C# Iron Wall spirals, Pointer Overlaps) at the engine inside an isolated process pool with a 0.1-second fuse to guarantee regex immunity.
* `test_prism.py` - Tests the "Optical Split" (Structural Refraction). Proves the engine can safely peel nested block comments (`/* /* */ */`), shield string literals containing URLs, and bypass metadata (Shebangs/Markdown).
* `test_signal_processor.py` - Validates the 18-point risk exposure math. Ensures Zero-State Resiliency (no divide-by-zero crashes), Sigmoid Overflow Clamping for massive densities, Inert Mass Bypasses for documentation, and Logarithmic Temporal Normalization.
* `test_state_rehydrator.py` - Validates the SQLite-backed RAM rehydration for fast Delta scans, proving Temporal Accuracy and exact schema mapping.
* `test_zero_dependency.py` - Proves the system degrades gracefully without heavy C-backed libraries (`networkx`, `xgboost`), bypassing ML inferences safely without breaking the dependency graph mapping.

### 2. `/extraction` (The Strict Gauntlets)
Because our regular expressions *are* the compiler, a poorly written regex will hallucinate architecture. These massive, parameterized testing matrices run across all supported languages, executing a 3-Tier Testing Matrix: **Valid** (Iron Wall), **Invalid** (Ghost Prevention), and **Pathological** (Frankenstein formatting).

* `test_function_extraction_strict.py` (The Satellite Spawner) - Proves the engine can pinpoint exact function and method names while stepping over massive attribute stacks, explicit return types, and C++ macro garbage.
* `test_class_extraction_strict.py` (The Entity Census) - Proves the engine can isolate the precise name of an Object-Oriented entity while ignoring complex inheritance chains, generics, and visibility modifiers.
* `test_args_extraction_strict.py` (The Coupling Mass) - Proves the engine can swallow massive parameter blocks, default arguments, and multi-line lambda closures without collapsing into a ReDoS spiral caused by nested parentheses.
* `test_dependency_extraction_strict.py` (The Gravity Links) - Proves the engine can trace information flow by extracting the exact file path from an import statement, ignoring aliases, destructuring syntax, and `require()` wrappers.

### 3. `/security_auditing` (Threat Intelligence & AppSec)
Tests the vulnerability, compliance, and zero-trust intelligence sensors.

* `test_ai_appsec_sensor.py` - Proves the engine flags AI-specific vulnerabilities: RCE Funnels, God-Mode Agents, and Exfiltration Vectors.
* `test_dev_agent_firewall.py` - Validates DevAgent guardrails, flagging Context Window Shredders (massive $O(N^3)$ files), enforcing HITL Mandates, and detecting Silent Mutation Risks.
* `test_neural_auditor.py` - Validates zero-RAM binary header parsing on `.safetensors` and `.gguf` files to extract exact Architecture and Parameter Math without loading massive payloads.
* `test_vault_sentinel.py` - Validates the multi-tiered secrets scanner (Denylist Wall & Deep Scan Trap).
* `test_supply_chain_firewall.py` - Validates the Zero-Trust Import Slicer and Strict Mode enforcement.
* `test_binary_anomaly_detector.py` - Validates the X-Ray engine, spotting Magic Byte Mismatches and High-Entropy payloads.
* `test_sbom_generator.py` - Proves the Universal Manifest Slicer securely translates threat states into CycloneDX JSON.
* `test_network_risk_sensor.py` - Validates N-Dimensional graph physics (PageRank, Betweenness) without NetworkX.
* `test_api_network_map.py` - Validates the Set-Theory API auditor to definitively flag Ghost APIs and Shadow APIs.
* `test_pii_leak_hunter.py` - Proves the log-scanner mathematically intercepts and masks PII (Credit Cards, SSNs) at the streaming level.
* `test_terabyte_log_scanner.py` - Validates binary stream log filtering against GitGalaxy IR JSON states.
* `test_spectral_auditor.py` - Enforces the 50/0 Law (rejecting massive files with 0 logic) and the Supernova Guard.
* `test_redos_poison.py` - Spawns an isolated 8-core multiprocessing pool to blast all 1,200+ production regexes with classic ReDoS payloads.

### 4. `/cobol_mainframe` (Legacy Modernization)
Mathematically proves the engine can bridge the gap between EBCDIC IBM mainframes and modern Zero-Trust architectures without relying on compilers or emulators.

* `test_cobol_agent_task_forge.py` - Validates the context merger for autonomous agents (Remediation Tickets).
* `test_cobol_compiler_forge.py` - Validates physical JCL and copybook provisioning, mathematically breaking infinite recursion loops.
* `test_cobol_dag_architect.py` - Validates Topological Sorts and the "Ghost Deflector".
* `test_cobol_etl_unpacker.py` - Validates EBCDIC string translation and `COMP-3` packed decimal hex decoding.
* `test_cobol_graveyard_finder.py` - Validates AST dead-code math and orphaned variable detection.
* `test_cobol_jcl_auditor.py` & `test_cobol_jcl_forge.py` - Validates JCL intent parsing, Bloat Reduction math, and Zero-Trust JCL generation.
* `test_cobol_lexical_patcher.py` - Validates safe normalization of COBOL-74/85 dialects and eradicating `NEXT SENTENCE` traps.
* `test_cobol_microservice_slicer.py` - Validates the Recursive Alias Engine (Taint Tracking).
* `test_cobol_refractor_controller.py` - Validates the Hybrid State Manager (OOM protection via SQLite toggling).
* `test_cobol_schema_forge.py` & `test_cobol_system_limits_reporter.py` - Validates PIC clause extraction and system limitation scanning.

### 5. `/tools_recorders` (Telemetry & Output Generation)
Validates the data pivoting layers, continuous integration harnesses, and automated code generation forges.

* `test_gpu_recorder.py` - Validates the destructive memory pivot (AoS -> SoA) optimized for WebGL 3D rendering and strictly enforces Destructive RAM Eviction.
* `test_batch_test_harness.py` - Validates the mass-directory batch scanner, starvation monitors, and 5-minute hardware kill-switches.
* `test_agent_forge.py` - Validates the LLM Hallucination Guard (extracting strict architectural constraints from the IR state).
* `test_decoder_forge.py` - Proves the EBCDIC/COMP-3 Decoder generation perfectly matches the Golden Image.
* `test_golden_forge.py` - Proves API Contracts and Spring Entities match strict JPA/Spring Boot Golden Images.
* `test_service_forge.py` - Validates the Service Skeleton DAG resolver (translating COBOL hyphens to Java CamelCase).

---

## 🚀 Execution Commands

Execute tests from the project root while within the `galaxy_venv`.

**Run the entire gauntlet:**
```bash
python -m pytest tests/ -v
```

**Run a specific domain (e.g., Security & Auditing):**
```bash
python -m pytest tests/security_auditing/ -v
```

**Run a specific file with fast-fail (stops on the first error):**
```bash
python -m pytest tests/extraction/test_dependency_extraction_strict.py -v -x
```