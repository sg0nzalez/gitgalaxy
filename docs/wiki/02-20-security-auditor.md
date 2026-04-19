# The Security Auditor (Machine Learning Inference)

> **XGBoost Threat Hunting**
>
> While the Security Lens relies on rule-based physics and regex signatures to detect vulnerabilities, advanced adversaries constantly evolve their obfuscation techniques. 
>
> The Security Auditor (`security_auditor.py`) serves as GitGalaxy's predictive AI brain. It executes a trained XGBoost multiclass inference model across the entire resolved repository graph, evaluating the holistic, N-dimensional shape of every file to predict the probability of malicious payloads natively in RAM.

## N-th Degree Graph Resolution

Before the Machine Learning model can evaluate a file, it must understand the file's position within the broader ecosystem. While the `NetworkRiskSensor` handles high-level topology (like PageRank), the Security Auditor calculates specific, transitive fragility paths for the feature matrix.

* **Breadth-First Search (BFS) Limits:** The Auditor traces the `raw_imports` graph both upstream and downstream. To prevent memory bombs on massively circular architectures, the BFS traversal is capped at 10,000 nodes.
* **Blast Radius Metrics:** It calculates the `total_upstream` (how many files ultimately feed into this file) and `total_downstream` (how many files rely on this file). These are then converted into ratios against the total repository size to feed standardized features to the ML model.

## The Feature Matrix

To generate accurate predictions, the Auditor reconstructs the exact Pandas DataFrame schema used during the model's original training phase. It synthesizes dozens of data points into a flattened, heavily sanitized vector:

* **Logarithmic Transforms:** Because file sizes and complexity vary wildly, structural counts (like `logic_loc`, `max_func_complexity`, and `import_count`) are log-transformed (`np.log1p`) to prevent extreme outliers from blinding the decision trees.
* **Design Slop & Density:** The matrix incorporates advanced heuristics like `func_complexity_gini` (structural inequality), `func_internal_density`, and orphaned/duplicated functions (`design_slop_orphans`).
* **Contextual Mitigations:** Raw danger hits are mapped alongside their specific mitigations (e.g., `raw_danger`, `raw_sec_tainted_injection`).
* **Global Architectural Context:** The matrix pulls in the global repository context (e.g., `primary_z_score` and distances to various archetype clusters) to determine if a file is acting anomalously compared to the rest of the project.
* **Safe Degradation:** If `xgboost` or `pandas` are not installed in the host environment, the Auditor gracefully degrades, running only the graph resolution and skipping the ML inference without crashing the pipeline.

## Multiclass Threat Inference

Once the feature matrix is sanitized (removing all `NaN` or infinite values), it is passed to the XGBoost model (`XGBClassifier`). The model predicts probabilities across five distinct architectural classes:

1. **Safe Code**
2. **Botnet / DDoS**
3. **Stealer / Trojan**
4. **Dropper / Webshell**
5. **Native Infector**

If a file scores above the dynamic `AI_THREAT_THRESHOLD` (defaulting to 90.0%) in any of the hostile classes, it is explicitly flagged as a threat. 

## The Shadow Patch Override

To support advanced CI/CD supply chain firewalls, the Security Auditor accepts an `is_shadow_patch` flag. 

If a file's cryptographic hash has mutated without a corresponding version bump in the repository, and the file contains actual executable mass (`structural_mass > 0.5`), the Auditor bypasses the ML math. It forcefully pegs the file as a **"Stealer / Trojan"** with 100.0% confidence, instantly highlighting the stealth mutation as a Tier 1 Threat.

## Telemetry Injection

The predictions are not siloed. The Auditor injects the `AI Threat Class`, the exact `AI Threat Confidence` percentage, and an `is_ml_threat` boolean directly back into the star's central `domain_context` telemetry. 

This guarantees that downstream systems—like the `AuditRecorder` and `LLMRecorder`—can place these ML-confirmed threats at the very top of their respective security reports.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

