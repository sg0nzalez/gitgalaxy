# 🌌 Mathematical Proofs: The Master Test Suite

This directory contains the testing architecture and physics gauntlets for the GitGalaxy engine. 

Building a planetary-scale, polyglot parser without relying on an Abstract Syntax Tree (AST) or a compiler toolchain is widely considered impossible. Traditional regex approaches hallucinate architecture and inevitably crash corporate pipelines via Catastrophic Backtracking (ReDoS). 

This test suite exists to mathematically prove the opposite. It aggressively validates GitGalaxy's structural extraction, enforces absolute ReDoS immunity across 1,200+ heuristics, and ensures zero-trust deterministic accuracy across 30+ programming languages and 40-year-old legacy mainframes.

---

## 📂 Architectural Proof Index

### 1. `/core_engine` (The Physics & Parsing Core)
This domain is the beating heart of GitGalaxy's structural physics. It validates the AST-free parsers, ReDoS shields, execution lifecycles, and mathematical models that allow the engine to operate flawlessly under extreme, adversarial conditions.

* **`test_detector.py`** — Validates the Logic Splicer. Proves the engine calculates $O(N)$ nesting depth natively, flags exponential $O(2^N)$ recursion, applies AppSec Spatial Correlation (blast radius multipliers), and safely implements the Anti-ReDoS Line Limiter.
* **`test_signal_processor.py`** — Validates the 18-point risk exposure math. Ensures Zero-State Resiliency (no divide-by-zero crashes), Sigmoid Overflow Clamping for massive densities, and Logarithmic Temporal Normalization.
* **`test_documentation_sensor.py`** — Validates the heuristic physics for code-to-comment density. Proves the engine correctly applies mass multipliers and complexity accelerants to eliminate false-positive fatigue on small files.
* **`test_licensing_guard.py`** — Validates the PolyForm compliance gate, offline HMAC-SHA256 cryptographic key verification, and the execution of CI/CD audit tripwires for enterprise environments.
* **`test_chronometer_timeout.py`** — Validates the Hardware Guillotine. Simulates a hanging Git stream and ensures the OS-level `SIGKILL` is sent, pipes are forcefully flushed, and file descriptors are closed to prevent RAM leaks.
* *(See the [Core Engine README](core_engine/README.md) for the full 13-file index, including Optical Splitters, Bayesian Guidestars, and Identity Traps).*

### 2. `/extraction` (The Strict Gauntlets)
Because our heuristics *are* the compiler, these massive, parameterized testing matrices fire thousands of mutated code snippets across all supported languages using a 3-Tier Matrix: **Valid** (The Iron Wall), **Invalid** (Ghost Prevention), and **Pathological** (Frankenstein formatting).

* **`test_function_extraction_strict.py`** — Proves the engine can pinpoint exact function names while stepping over massive attribute stacks, explicit return types, and C++ macro garbage.
* **`test_class_extraction_strict.py`** — Proves the engine can isolate the precise name of an Object-Oriented entity while ignoring complex inheritance chains, generics, and visibility modifiers.
* **`test_args_extraction_strict.py`** — Proves the engine can swallow massive parameter blocks and multi-line lambda closures without collapsing into a ReDoS spiral caused by nested parentheses.
* **`test_dependency_extraction_strict.py`** — Proves the engine can trace information flow by extracting the exact file path from an import statement, ignoring aliases and destructuring syntax.

### 3. `/security_auditing` (Threat Intelligence & AppSec)
Validates the vulnerability, compliance, and zero-trust intelligence sensors. Instead of relying on fragile dynamic execution, these tests prove we can spot threats using pure structural mathematics.

* **`test_dev_agent_firewall.py`** — Validates AI guardrails, mathematically flagging Context Window Shredders (massive $O(N^3)$ files), enforcing HITL (Human-in-the-Loop) Mandates, and detecting Silent Mutation Risks.
* **`test_vault_sentinel.py`** — Validates the multi-tiered secrets scanner, proving the Denylist Wall and Deep Scan Traps can instantly halt pipelines leaking credentials.
* **`test_binary_anomaly_detector.py`** — Validates the X-Ray engine, spotting Magic Byte Mismatches (e.g., an executable disguised as a `.jpg`) and High-Entropy encrypted payloads.
* **`test_network_risk_sensor.py`** — Validates N-Dimensional graph physics (PageRank, Betweenness centrality) without relying on heavy external dependencies.
* **`test_redos_poison.py`** — Spawns an isolated 8-core multiprocessing pool to blast all 1,200+ production heuristics with classic ReDoS payloads to guarantee absolute pipeline stability.
* *(See the [Security Auditing README](security_auditing/README.md) for the full 13-file index, including Swagger API mapping, PII Leak Hunters, and Supply Chain Firewalls).*

### 4. `/cobol_mainframe` (Legacy Modernization)
Mathematically proves the engine can bridge the gap between 40-year-old EBCDIC IBM mainframes and modern Zero-Trust architectures without relying on compilers or emulators.

* **`test_cobol_etl_unpacker.py`** — Validates EBCDIC string translation and mathematical decoding of `COMP-3` packed decimal hexadecimal boundaries.
* **`test_cobol_dag_architect.py`** — Validates Topological Sorts and the "Ghost Deflector" for mapping exact execution flow.
* **`test_cobol_jcl_auditor.py` & `test_cobol_jcl_forge.py`** — Validates JCL intent parsing, Bloat Reduction math, and Zero-Trust least-privilege JCL generation.
* **`test_cobol_agent_task_forge.py`** — Validates the context merger for autonomous agents, ensuring LLMs receive strict JSON remediation tickets bounded by reality.
* *(See the [Main