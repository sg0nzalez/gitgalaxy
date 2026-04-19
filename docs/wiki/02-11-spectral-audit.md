# The Spectral Audit (Quality Control)

> **Bayesian Accountability**
>
> The Spectral Auditor is the final data-integrity gate of the analysis pipeline. It performs an automated statistical verification of every artifact to ensure that the assigned language and resulting logic metrics are mathematically plausible. This process eliminates "Linguistic Drift"—the misidentification of non-code artifacts (e.g., massive data dumps, logs, or minified blobs) as source files—ensuring anomalous data does not corrupt the project's aggregate metrics.
>
> The Auditor operates on **Bayesian Accountability**. If a file acts as a statistical outlier compared to its peers, the engine refutes the prior assumption and banishes the file to the Singularity (Dark Matter), regardless of its initial metadata claims.

## Empirical Bayes Loop-Back (The Consensus Engine)

Before evaluating signal density, the Auditor attempts to save ambiguous files using local ecosystem consensus.

* **The Triage:** Files that landed at a weak Tier 4 identity lock, or suffered a collision, are placed in an "Ambiguous Pen." Highly confident files form the "Confident Core."
* **Ecosystem Consensus:** The engine maps the exact file extensions of the Confident Core. If it determines that 80% or more of a specific extension in *this specific repository* firmly belongs to a single language, it applies that localized truth to the Ambiguous Pen.
* **The Loop-Back:** Ambiguous files matching that extension are pulled into the dominant orbit, elevated to a Tier 2 Lock, and spared from immediate relegation. Files that remain ambiguous are instantly stripped to Dark Matter to prevent hallucinations.

## Dynamic Auditability (Inert vs. Structural Matter)

Legacy systems use hardcoded lists (e.g., "ignore JSON and Markdown") to bypass audits. The Spectral Auditor dynamically evaluates a language's capability based on its active regex sensors against the 32-key schema.

* **Inert Matter Gate:** If a language triggers 0 active logic sensors (e.g., YAML, CSV, Plaintext), it is classified as *Inert Matter*. It automatically bypasses the statistical audit and is placed directly in the visible galaxy.
* **Structural Gate:** If a language utilizes less than 75% of the total logic sensors (missing concepts like pointers, memory allocation, or globals), it is classified as *Structural* (e.g., HTML, CSS, Dockerfile).

## The Ecosystem Orphan Guard

If a language species has a microscopic population in the galaxy (dynamically calculated based on total repository size, e.g., 3 files or fewer), it triggers the Orphan Guard.

To survive as an isolated species, the files MUST possess an absolute Convergent Lock (Tier 0). If the entire orphan population relies on weak, unverified claims (Tier 1+), the Auditor assumes they are linguistic hallucinations, strips their identities, and converts them to **plaintext** to preserve their mass without polluting the linguistic composition metrics.

## Signal Density & The MAD Protocol

For true executable code, the Auditor calculates **Intent Density** ($\rho$): **(Sum of 32 Verified Signal Hits) / (Total Physical Lines)**. This isolates authorial intent from syntactic noise.

To find outliers, the Auditor uses the **MAD Protocol (Median Absolute Deviation)**:

1. **Statistical Readiness:** The baseline is only trusted if the species has a massive population ($N \ge 50$), high cohesion (R-MAD < 1.0), and at least one high-confidence anchor file ($C_i > 0.85$).
2. **Polyglot Defense:** Highly Blended Polyglots (where the primary language makes up < 80% of the mass) are excluded from the baseline math to prevent embedded languages from skewing the median density.
3. **The Robust Z-Score ($M_i$):** $$M_i = \frac{0.6745 \times (\rho - \text{Median}_\rho)}{\text{MAD}}$$
4. **Bayesian Threshold Gating ($T_{adj}$):** The threshold for relegation is dynamically tied to the file's upstream Confidence Score ($C_i$). The formula ensures that high-confidence files are granted wider statistical leniency, while low-confidence files are held to strict scrutiny.
$$T_{adj} = -5 \times \max(C_i, 0.1)$$

## The Event Horizon: Quarantine, Necrosis, and Relegation

Every file is evaluated against the 50/0 Law (any file >50 lines with 0 signals is a data dump) and the MAD Protocol. If flagged as an outlier, it faces three possible outcomes:

### The Quarantine Guard (Security Override)
Highly obfuscated malware often registers a structural density of zero, attempting to disguise itself as a harmless data dump to evade traditional scanners. If a file fails the audit but the Security Lens detects *ACTIVE THREAT SIGNATURES* (e.g., Glassworm obfuscation, Sub-Atomic Decryption), the Quarantine Guard activates. It explicitly intercepts the relegation, forcing the active threat into the visible galaxy so the Signal Processor and human auditors can flag the anomaly.

### The Necrosis Guard (Reprieve from Relegation)
If a file fails the density audit but contains a massive comment-to-code ratio (e.g., > 5:1) or its active signals are >50% graveyard hits (commented-out logic), it is granted a Reprieve. This ensures that "Dead Code" remains in the visible galaxy for forensic Tech Debt analysis rather than being lost to the Singularity.

### Relegation to Dark Matter
Files failing the audit (and not saved by Quarantine or Necrosis) are stripped of their metadata and cast into the Singularity. To ensure SBOM Traceability, they are formatted into an Inert Dark Matter schema that preserves their "Bayesian Optics" (the failed claim, confidence, and source proof) so engineers can audit *why* the prediction was refuted.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

