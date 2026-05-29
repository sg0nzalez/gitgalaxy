### 🛡️ Mathematical Proofs: Zero-Trust Security & Auditing

This directory contains the strict mathematical and physical validation suite for GitGalaxy's Security, Auditing, and Threat Intelligence sensors.

Most enterprise security tools rely on fragile dynamic execution, slow sandboxing, or shallow manifest scanning (which misses typosquatting and hidden payloads). GitGalaxy approaches DevSecOps as a problem of **structural physics**. This test suite exists to mathematically prove that our AST-free engine can definitively detect autonomous agent threats, supply chain poisons, Shadow APIs, and catastrophic algorithmic vulnerabilities using pure static mathematics—without ever executing the target code.

---

### 🧪 Execution Protocols

These gauntlets stress-test the threat sensors against embedded malware, corrupted JSON schemas, infinite cyclic loops, and RCE injection vectors. To run the security matrix in isolation:

```bash
python -m pytest tests/security_auditing/ -v
```

---

### 📂 Verified Capabilities & Documentation Index

The following tests validate the core perimeter defenses and intelligence sensors. Click on any component to review its underlying structural physics.

#### 1. AI Governance & Autonomous Guardrails
Validates the sensors designed to monitor Large Language Models (LLMs) and autonomous agents interacting with your codebase.
* **`test_dev_agent_firewall.py`** — Validates the [Dev Agent Firewall](../../docs/wiki/02-18-dev-agent-firewall.md). Proves the engine mathematically identifies **Context Window Shredders** (O(N^3) logic in massive files), flags **Silent Mutation Risks**, and enforces **HITL (Human-in-the-Loop) Mandates** based on calculated blast radii.
* **`test_ai_appsec_sensor.py`** — Validates the [AI AppSec Sensor](../../docs/wiki/02-17-ai-appsec-sensor.md). Proves the engine can flag AI-specific vulnerabilities, including **RCE Funnels** (Agentic code execution) and **God-Mode Agents** (over-permissioned database writes).
* **`test_neural_auditor.py`** — Validates the [Neural Auditor](../../docs/wiki/02-19-neural-auditor.md). Proves the local scanner can execute zero-RAM binary header parsing on `.safetensors` and `.gguf` payloads to extract quantization and parameter math without causing OOM crashes.

#### 2. Supply Chain & Vault Security
Validates the Zero-Trust perimeter defenses that block hostile dependencies and credential leaks.
* **`test_supply_chain_firewall.py`** — Validates the [Supply Chain Firewall](../../docs/wiki/04-03-supply-chain-firewall.md). Proves the Zero-Trust Import Slicer successfully enforces Strict Mode allowlists, cross-references physical imports against known poisons, and safely bypasses minified data files.
* **`test_vault_sentinel.py`** — Validates the [Vault Sentinel](../../docs/wiki/04-04-vault-sentinel.md). Proves the dual-layer perimeter instantly blocks forbidden extensions (Denylist Wall) and executes a Deep Scan Trap to crash the pipeline if hardcoded `AKIA` AWS keys are found in otherwise benign source code.
* **`test_binary_anomaly_detector.py`** — Validates the [Binary Anomaly Detector](../../docs/wiki/04-05-binary-anomaly-detector.md). Proves the X-Ray engine catches **Magic Byte Mismatches** (e.g., an executable disguised as a `.jpg`), flags high-entropy encrypted payloads, and enforces the Shebang Shield.
* **`test_sbom_generator.py`** — Validates the [SBOM Generator](../../docs/wiki/04-02-sbom-generator.md). Proves the Universal Manifest Slicer securely translates threat states into compliant CycloneDX JSON without blindly trusting package names.

#### 3. Structural Threat Physics & Ecosystem Compliance
Validates the mathematical graph theory and data-destruction pipelines.
* **`test_security_auditor.py`** — Validates the [Security Auditor](../../docs/wiki/02-20-security-auditor.md). Proves the XGBoost multiclass ML inference engine successfully formats spatial data into Pandas matrices to predict threats, while utilizing an O(1) pure-Python fallback to resolve dependency graphs if NetworkX is missing.
* **`test_network_risk_sensor.py`** — Validates the [Network Risk Sensor](../../docs/wiki/02-16-network-risk-sensor.md). Proves the engine calculates **PageRank (Blast Radius)** and