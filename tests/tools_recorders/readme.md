# 🛠️ Tools & Recorders Test Suite

Welcome to the **Tools & Recorders** domain.

While the Core Engine handles physics and extraction, this domain tests the final translation layer. It mathematically proves that GitGalaxy securely, losslessly, and rapidly maps massive volumes of forensic data to output mediums (like WebGL GPU payloads) and validates the scaffolding engines that auto-generate AI tickets and Java boilerplate.

## 📂 Architecture & File Index

### 1. Telemetry & Memory Management
Validates the data pivoting layers that prepare telemetry for visualization and UI consumption.
* `test_gpu_recorder.py` - Validates the destructive memory pivot. Proves the recorder correctly maps complex, nested Python dictionaries into a minified, flattened columnar structure (AoS -> SoA) optimized for WebGL 3D rendering. Crucially, it verifies the **Destructive RAM Eviction** contract—ensuring original arrays are popped from memory to prevent Out-Of-Memory (OOM) crashes on massive repositories.

### 2. Automation & Continuous Integration
Validates the orchestration wrappers that run GitGalaxy across massive, multi-repository environments.
* `test_batch_test_harness.py` - Validates the mass-directory batch scanner and starvation monitors. Proves the orchestrator correctly traverses repositories, catches compilation errors (e.g., Maven build failures), and safely triggers the 5-minute hardware kill-switch to terminate frozen external subprocesses.

### 3. The Code Generation Forges (Golden Images)
Validates the scaffolding algorithms that automatically generate boilerplate code, test fixtures, and architectural foundations based on GitGalaxy's intermediate representation (IR) blueprints. These tests rely on exact byte-for-byte comparisons against "Golden Images."
* `test_agent_forge.py` - Validates the LLM Hallucination Guard. Proves the forge accurately extracts strict architectural constraints (external dependencies, "honesty flags") from the COBOL IR state and injects them into the JSON ticket so the downstream AI agent does not fly blind.
* `test_decoder_forge.py` - Validates the EBCDIC/COMP-3 Decoder generation. Proves the generated Java utility perfectly matches the mathematically proven Golden Image, preventing fatal regressions in the mainframe bitwise unpacking logic.
* `test_golden_forge.py` - Validates the API Contract and Spring Entity generation. Proves that known IR states and JSON schemas are correctly translated into strict Spring Boot `@RestController` and JPA `@Entity` Java classes.
* `test_service_forge.py` - Validates the Service Skeleton DAG resolver. Proves the engine accurately translates COBOL hyphens to Java CamelCase to scaffold autowired `@Service` classes, injecting explicit `TODO: AI AGENT` boundaries based on unresolved external calls.

## 🚀 Execution Commands

Execute these tests from the project root while within the `galaxy_venv`.

**Run the entire Tools & Recorders gauntlet:**
```bash
python -m pytest tests/tools_recorders/ -v
```

**Run the GPU Recorder memory eviction test specifically:**
```bash
python -m pytest tests/tools_recorders/test_gpu_recorder.py -v
```