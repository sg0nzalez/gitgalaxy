# Signal Processing (Equations & 2nd Pass Calculations)

> **The Post-Processing Pipeline**
>
> The Signal Processor acts as GitGalaxy's core Physics Engine. Once the Splicer has carved the raw structural telemetry (the 60-Point `SIGNAL_SCHEMA`), the Physics Engine resolves these counts into meaningful, scaled insights—the 18-Point `RISK_SCHEMA`.
>
> Rather than executing static math, the modern Protocol introduces a multi-pass architecture. It evaluates a file not just in isolation, but against the physical reality of its surrounding neighborhood and the temporal history of the entire galaxy.

## The Context vs. Entity Matrix (Domain Ontologies)

A file's risk profile changes drastically depending on where it lives. A C++ file in a firmware repository is expected; a C++ file hidden deep inside a frontend JavaScript repository is highly anomalous.

To catch these architectural Trojans, the engine utilizes the **Context vs. Entity Matrix**:

* **Native Ecosystems:** The engine compares the file's language against the dominant language of its parent folder. [cite_start]If they match the same domain ontology (e.g., both are *backend*), the file is processed using standard native weights[cite: 143, 144].
* [cite_start]**Alien Entities (Trojan Detection):** If a severe context mismatch occurs, the file is classified as an "Alien"[cite: 147]. [cite_start]The engine dynamically injects severe risk multipliers[cite: 149]. [cite_start]For example, a systems-level file (`c`, `rust`) hiding in a web neighborhood (`javascript`, `html`) receives massive multipliers to its `logic_bomb` and `memory_corruption` exposures, immediately flagging it as a severe architectural or security anomaly[cite: 153].

## Standardization: The Tiered Physics Model

[cite_start]To ensure comparative fairness across different code "materials," the engine applies Linguistic Normalization[cite: 490]. [cite_start]This accounts for the fact that explicit languages (like Rust) "broadcast" their safety, while implicit languages (like Shell) hide their risks[cite: 491].

[cite_start]The instrument applies specific Trust Constants based on the language's spectral class[cite: 492]:

| Tier | Spectral Class | Examples | Physics Treatment |
| :--- | :--- | :--- | :--- |
| **Tier 1** | **Explicit** | Rust, Go, Swift, Java | Signals are trusted at face value. [cite_start]The Fidelity Coefficient is 1.0, and "Implicit Risk" is zero[cite: 493, 494]. |
| **Tier 2** | **Structured** | Python, JS, C++ | Translucent. [cite_start]A minor "Opacity Tax" is applied to account for potential runtime surprises[cite: 495]. |
| **Tier 3** | **Implicit** | Shell, SQL, Assembly | Opaque. [cite_start]The "Fog of War" penalty adds a baseline phantom risk to all equations, requiring significantly higher defensive density to achieve a "Safe" rating[cite: 496]. |

## Biaxial Weaponization (Global vs. Local Drift)

One of the most advanced features of the Signal Processor is its ability to detect **Biaxial Anomalies**. By using the ML Inference models, the engine measures two distinct types of architectural drift:

* **Global Archetype:** How does this file behave compared to the entire repository? (e.g., Is it a "God Node" or a "Static Configuration"?)
* **Local Micro-Species:** How does this file behave compared *only* to other files written in the exact same language?

**The Trojan Spike:** The Physics Engine cross-multiplies these two drift scores. If a file blends in globally (Low Global Drift) but heavily violates the standard conventions of its native programming language (High Local Drift), it triggers the Biaxial Trojan Spike. This means the file is structurally masquerading as something it is not. The engine applies an exponential multiplier to its `logic_bomb` and `obscured_payload` threat masses, ensuring it glows white-hot on the 3D map.

## The Infrastructure Shields (Bypass Protocols)

To prevent the math engine from hallucinating extreme risks on inert files, the Signal Processor employs several absolute bypass protocols:

* **The Extension Deception Sensor:** Punishes files claiming to be inert data (like `.txt` or `.json`) but evaluated as executable code (like `python` or `shell`), instantly flagging them for a `sec_extension_mismatch` security violation.
* [cite_start]**The Exposed Secret Bypass:** Treat exposed keyfiles (like `.pem` or `.env`) as structural vulnerabilities[cite: 268]. It skips the math and instantly pegs the `secrets_risk` exposure to 100%.
* **The Minified / Vendor Tripwire:** Minified files (like `.min.js` or `node_modules`) are zeroed out of all standard architectural risks (Cognitive Load, Tech Debt). However, if the engine detects *any* malicious intent (eval, network fetching) inside the minified mass, it trips the wire and spikes the Obfuscated Payload risk to 100%.
* **The Documentation Bypass:** Pure literature files (`markdown`, `plaintext`) do not execute logic. Their logic metrics are safely zeroed out (0% Documentation Risk, 0% Cognitive Load), and their Ownership Entropy is zeroed since plaintext changelogs don't have a "Bus Factor."

## Global Synthesis & 2-Pass Normalization

Because temporal metrics (like commit frequency) vary wildly between repositories, a hardcoded churn threshold is useless. A file with 5 commits might be volatile in a dead repository but highly stable in an active one.

GitGalaxy solves this via **Two-Pass Normalization**:

1. **Pass 1 (Raw Extraction):** The engine calculates the absolute Age (Stability) and the raw Churn Frequency (Commits over time) for every individual star.
2. **Pass 2 (The Global Curve):** Once all files are processed, the `_normalize_temporal_metrics` engine scans the entire galaxy to find the "Volcano" (the absolute maximum churn frequency in the repository). It then applies a Logarithmic Curve (`math.log1p`) to scale every file's churn relative to that global ceiling. This guarantees that the UI gradients perfectly highlight the hottest files in the repository, regardless of the team's specific commit culture.

## The Physics Engine: N-Dimensional Systemic Bottlenecks

In the final stage, the engine generates the high-fidelity Forensic Report. [cite_start]To prevent noise, it applies an **Active Logic Mask**, blinding the ranking algorithms to structural assets (like JSON configs or Markdown) so only true executable code competes for the "Highest Risk" spots[cite: 585, 586].

Alongside ranking individual vectors (like highest Tech Debt or lowest Safety), the engine calculates **Systemic Bottlenecks** by cross-multiplying the *Local Risk Exposure* against the *Global Network Graph Theory* metrics provided by the `NetworkRiskSensor`:

* **Contagious Mutation:** `Betweenness * State Flux`. These files act as structural bridges between components but possess highly volatile, mutating state, causing unpredictable side-effects for downstream consumers.
* **House of Cards:** `Closeness * Error Risk`. These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.
* **Blind Bottleneck:** `Blast Radius * Doc Risk`. These are "God Nodes" that the entire ecosystem relies upon, but they lack human intent or documentation. Modifying them is flying blind.