# 🛡️ Security & Auditing Test Suite

Welcome to the **Security & Auditing** domain.

Because GitGalaxy is utilized as a zero-trust forensic engine, its security sensors must be mathematically flawless. This test suite proves that the engine can successfully detect agentic threats, supply chain poisons, shadow APIs, and Catastrophic Backtracking attacks entirely through static structural physics, without ever requiring dynamic execution or external sandboxes.

## 📂 The Intelligence Sensors

### 1. AppSec & AI Guardrails
Validates the sensors designed to monitor Large Language Models (LLMs) and autonomous agent frameworks interacting with the codebase.
* `test_ai_appsec_sensor.py` - Proves the engine can correctly flag AI-specific vulnerabilities: **RCE Funnels** (Agentic code execution), **God-Mode Agents** (over-permissioned database writes + autonomous tools), and **Exfiltration Vectors** (AI models with access to both network sockets and raw secrets).
* `test_dev_agent_firewall.py` - Validates the DevAgent architectural guardrails. Proves the engine can flag **Context Window Shredders** (massive $O(N^3)$ files that hallucinate LLMs), enforce **HITL (Human-in-the-Loop) Mandates** via blast radius math, and detect **Silent Mutation Risks**.
* `test_neural_auditor.py` - Validates the Local Compute AI scanner. Proves the auditor can execute zero-RAM binary header parsing on `.safetensors` and `.gguf` files to extract the exact Architecture, Quantization, and Parameter Math (e.g., 16.8M) without loading massive payloads into memory, while explicitly blocking OOM hallucination attacks.

### 2. Supply Chain & Vault Security
Validates the perimeter defenses that prevent malicious code, exposed secrets, and unauthorized dependencies from entering the build pipeline.
* `test_vault_sentinel.py` - Validates the multi-tiered secrets scanner. Proves the Denylist Wall instantly blocks files like `id_rsa`, while the Deep Scan Trap successfully crashes the pipeline if it catches hardcoded `AKIA` AWS keys in otherwise benign files.
* `test_supply_chain_firewall.py` - Validates the Zero-Trust Import Slicer. Proves the firewall can cross-reference package imports against Approved/Blacklisted arrays, enforce Strict Mode, and safely bypass minified inert data files.
* `test_binary_anomaly_detector.py` - Validates the X-Ray engine. Proves the detector can spot **Magic Byte Mismatches** (e.g., an executable disguised as a `.jpg`), flag high-entropy packed payloads, and enforce the Shebang Shield.
* `test_sbom_generator.py` - Validates the Universal Manifest Slicer. Proves the regex can extract packages natively across diverse ecosystems (NPM, PyPI, Cargo) and securely translate threat states (`SPOOF_DETECTED`, `UNVERIFIED_MISSING_ON_DISK`) into a compliant CycloneDX JSON specification.

### 3. Data Physics & Ecosystem Compliance
Validates the mathematical graph theory and data-destruction pipelines.
* `test_network_risk_sensor.py` - Validates the N-Dimensional graph physics. Proves the engine can calculate PageRank (Blast Radius) and Betweenness Centrality without NetworkX installed, while safely surviving mathematically impossible states like Isolated Islands (0 edges) and A->B->A infinite cyclic deadlocks.
* `test_api_network_map.py` - Validates the Set-Theory API auditor. Proves it can cross-reference physical code boundaries across multiple languages against Swagger specifications to definitively flag **Ghost APIs** (documented but missing) and **Shadow APIs** (actively listening but undocumented).
* `test_pii_leak_hunter.py` - Validates the Terabyte Data Destroyer. Proves the log-scanner can mathematically intercept, mask, and safely write PII (Credit Cards, SSNs, AWS Keys) at the streaming level, guaranteeing zero raw data ever touches the output evidence log.
* `test_terabyte_log_scanner.py` - Validates the binary stream log filter. Proves the tool correctly parses the GitGalaxy IR state JSON, applies the target whitelist to a live, gigabyte-scale log stream, and safely extracts only matching telemetry.
* `test_spectral_auditor.py` - Validates the Heuristic Physics Filter. Proves the engine enforces the **50/0 Law** (rejecting massive files with 0 logic structures) and the **Supernova Guard** (rejecting minified payloads with impossible signal densities), while using a Consensus Engine to rescue ambiguous files.

### 4. The Core Stability Proving Ground
* `test_redos_poison.py` - The ultimate stability test. Spawns an isolated 8-core multiprocessing pool to blast every single regex in the production pipeline (1,200+ rules) with the "Toxic Arsenal" of classic ReDoS payloads (unclosed scopes, exponential overlapping whitespace, escaping quote hell), utilizing a 0.25-second kill-switch to guarantee that no regular expression can ever lock the CPU.

## 🚀 Execution Commands

Execute these tests from the project root while within the `galaxy_venv`.

**Run the entire security gauntlet:**
```bash
python -m pytest tests/security_auditing/ -v
```

**Run the ReDoS poison fuzzer specifically:**
```bash
python -m pytest tests/security_auditing/test_redos_poison.py -v
```