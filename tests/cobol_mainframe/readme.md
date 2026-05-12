# GitGalaxy Master Test Suite

This directory contains the testing architecture for the GitGalaxy engine. 

GitGalaxy operates as an **AST-free, polyglot structural parser**. Because it relies on heavily bounded mathematical regex and structural physics rather than standard compiler toolchains, this test suite is designed to aggressively validate structural extraction, prevent Catastrophic Backtracking (ReDoS), and ensure absolute accuracy across 30+ programming languages.

## 📂 Architecture & File Index

### 1. `/core_engine` (The Physics & Parsing Core)
Validates the fundamental optical physics and execution lifecycle of the engine.
* `test_aperture.py` - Validates the Solar Shield (filtering out binaries, minified files, and generated debris).
* `test_prism.py` - Validates the Optical Split (separating active code from ghost mass/comments).
* `test_detector.py` - Validates the Logic Splicer (extracting complexity and scope without ASTs).
* `test_signal_processor.py` - Validates the 18-point risk exposure math and structural mass equations.
* `test_galaxyscope.py` - Validates the main orchestrator, multi-processing worker IPC, and hardware timeouts.
* `test_language_lens.py` & `test_language_standards_strict.py` - Validates dialect detection and baseline regex integrity.
* `test_guidestar_lens.py` - Validates social/roadmap proof (manifests, `.gitattributes`, `.gitignore` overrides).
* `test_chronometer_timeout.py` - Validates the strict POSIX hardware guillotine for frozen threads.
* `test_state_rehydrator.py` & `test_zero_dependency.py` - Validates Delta scans and safe fallbacks for missing C-libs.

### 2. `/extraction` (The Strict Gauntlets)
Massive, parameterized testing matrices that run across all supported languages. They mathematically prove that the engine can isolate structures while ignoring strings, comments, and pathological formatting.
* `test_args_extraction_strict.py` - Validates parameter and coupling mass extraction.
* `test_class_extraction_strict.py` - Validates entity (Class/Struct/Trait) boundary extraction.
* `test_dependency_extraction_strict.py` - Validates import/dependency linkage extraction.
* `test_function_extraction_strict.py` - Validates executable logic (Function/Method) extraction.

### 3. `/security_auditing` (Threat Intelligence & AppSec)
Tests the vulnerability, compliance, and threat intelligence sensors.
* `test_ai_appsec_sensor.py` - Validates detection of Agentic RCE, prompt injections, and autonomous AI threats.
* `test_redos_poison.py` - Proves the engine's immunity against Catastrophic Backtracking attacks.
* `test_vault_sentinel.py` & `test_pii_leak_hunter.py` - Validates the detection of hardcoded secrets and PII.
* `test_supply_chain_firewall.py` & `test_binary_anomaly_detector.py` - Validates the X-Ray binary scans and import blacklists.
* `test_network_risk_sensor.py` - Validates the N-Dimensional graph physics (Blast Radius, Betweenness).
* `test_neural_auditor.py` - Validates the zero-RAM header extraction of AI model weights (GGUF/Safetensors).
* `test_api_network_map.py` & `test_sbom_generator.py` - Validates shadow API detection and SBOM manifest generation.

### 4. `/cobol_mainframe` (Legacy Modernization)
Dedicated tests for the Mainframe/Z-System modernization toolchain.
* `test_cobol_lexical_patcher.py` - Validates the safe normalization of COBOL-74 and COBOL-85 dialects.
* `test_cobol_etl_unpacker.py` - Validates the EBCDIC translation and COMP-3 packed decimal hexadecimal decoding.
* `test_cobol_dag_architect.py` & `test_cobol_microservice_slicer.py` - Validates Execution Order DAGs and Taint Tracking.
* `test_cobol_jcl_auditor.py` & `test_cobol_jcl_forge.py` - Validates the auditing and zero-trust generation of JCL scripts.
* `test_cobol_compiler_forge.py` & `test_cobol_agent_task_forge.py` - Validates copybook flattening and AI agent ticket creation.
* `test_cobol_graveyard_finder.py` - Validates AST dead-code math and orphaned variable detection.

### 5. `/tools_recorders` (Telemetry & Output Generation)
Validates the telemetry translation layer and continuous integration harnesses.
* `test_gpu_recorder.py` - Validates the destructive memory pivot that generates WebGL-optimized 3D map payloads.
* `test_batch_test_harness.py` - Validates the mass-directory batch scanner and starvation monitors.
* `test_agent_forge.py`, `test_decoder_forge.py`, `test_golden_forge.py`, `test_service_forge.py` - Validates auxiliary data generation tools.

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