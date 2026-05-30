# Focusing the Language Lens

> **The Entity Census**
>
> Before the GitGalaxy pipeline can calculate the physics of Star Mass or determine security risk, it must perform a comprehensive Entity Census. This phase is responsible for assigning a high-fidelity "Identity Lock" (`lang_id`) to every artifact in the repository.
>
> In the era of AI-generated code and automated refactoring, single-point metadata is no longer a source of absolute truth. Assuming a file's language based solely on its extension is one hallucination away from disaster. The Language Lens operates on a Bayesian model of Contextual Convergence, treating every file as a "claim" that must be proven through a strict hierarchy of evidence.

## The Bayesian Engine: Prediction vs. Audit

GitGalaxy adopts a rigorous stance on identity: True confidence requires convergence. A single metadata signature (like an extension alone) is merely a suggestion. The engine evaluates files against a multi-tier Trust Matrix to establish their absolute identity.

| Tier | Lock Type | Source Evidence | Confidence | Structural Definition |
| :--- | :--- | :--- | :--- | :--- |
| **0** | **Convergent Lock** | Dual Evidence | **0.95 - 0.99** | Verified Identity: Two independent signals match (e.g., Ext + Shebang, or Ext + GuideStar Prior). Perfect focus achieved. |
| **1** | **Roadmap Lock** | GuideStar Manifest | **0.95** | Authoritative Proof: The project's build system (e.g., `package.json`) explicitly defines the file. |
| **1.5** | **Ecosystem Gravity** | Neighborhood Dominance | **0.95** | Collision Resolution: Resolves highly contested extensions (like `.h`) by analyzing the local folder and global repository composition. |
| **1.7** | **Exo-Species** | Unknown Extension | **0.95** | Fallback Trust: Acknowledges short, alphanumeric custom extensions as valid unknown structures rather than defaulting to plaintext. |
| **2** | **Single Signature** | Extension OR Shebang | **0.91** | Unverified Claim: Single-point metadata is a suggestion. Triggers mandatory spectral verification. |
| **3** | **Contextual Proof** | GuideStar Bias | **0.90** | Suggested Intent: Context suggests importance, but identity requires spectral scanning. |
| **4** | **Discovery** | Zero Context | **0.10** | Deep Space Mystery: No roadmap or extension. Must pass rigorous structural density checks to be acknowledged. |
| **5** | **Absolute Distrust** | Identity Crisis | **0.00** | Security Anomaly: Extension and Shebang explicitly contradict each other. Banished to the Singularity. |

## The Pre-Flight Sequence: Anchors & Wrappers

Before engaging the heavy regex detectors, the Lens secures the perimeter, resolves hidden names, and defends against prose hijacking.

* **Dotfile & Hidden Extension Resolution:** The Lens intelligently bypasses false extensions on dotfiles (e.g., `.bashrc`). Furthermore, it peels back safe wrapper extensions (`.template`, `.bak`, `.orig`, `.in`) to discover the true hidden extension beneath (e.g., extracting `.sh` from `script.sh.template`).
* **Sibling Anchors:** The Lens looks at the surrounding files in the directory. If it sees a `.h` file next to a `.c` file, it instantly locks it as C. If it's next to `.cpp`, it locks it as C++.
* **The Code Shield:** A critical security feature preventing "Prose Hijacking." If a developer names a C++ file `README.cpp`, the engine will not treat it as Markdown. If a file has a known executable extension, it strictly bypasses prose checks so hostile logic cannot hide inside fake documentation.

## The Identity Crisis Trap (Security Integration)

The Lens acts as the first line of defense for the Security Module by cross-examining physical signals. If a file claims to be a Python script (`.py`) but contains a Bash shebang (`#!/bin/bash`), the file is lying about its physical identity.

* **The Result:** The Lens flags this as an "Identity Masking" anomaly, caches it in RAM for the Security Lens, and forces the file into Tier 5 Absolute Distrust, destroying its identity and banishing it to the Dark Matter Singularity (`undeterminable`).

## Tier 1.5: Ecosystem Gravity (Collision Resolution)

Certain extensions, like `.h` or `.m`, are heavily collided (used primarily by C, C++, Objective-C, or MATLAB). The Lens uses a two-pass "Ecosystem Gravity" check to resolve these ties without expensive deep-packet inspection, actively pulling files into the orbit of the repository's dominant language.

**The Physics Engine:** It evaluates candidates by looking first at the *Local Folder Census*, and if inconclusive, falls back to the *Global Repository Tally*. It calculates three specific masses:
* **Base Mass:** The standard supporting extensions in the ecosystem.
* **Discriminator Mass:** Highly specific extensions (like `CMakeLists.txt` or `project.pbxproj`) that strongly prove an ecosystem exists. These are heavily weighted (multiplying the base score by 2.0x).
* **Toxic Mass:** Disqualifying extensions. If a single toxic extension is present, it triggers "Thermodynamic collapse" (Score = 0.0), instantly disqualifying that language.

**The Dominance Threshold:** To achieve a Tier 1.5 lock, the winning language must not only survive the physics engine but must achieve a dominance ratio of at least 70% over all other competitors (or 60% if resolved strictly within the local folder).

## Tier 3: Spectral Verification & The Iron Wall

Files that land at Tier 2 (Single Signature) must undergo Mandatory Spectral Verification to prove they contain the structural logic they claim to hold.

**The Iron Wall Scanner:** To prevent the engine from hallucinating, the Lens enforces a strict boundary. If a file has an extension, it MUST be claimed by one of the known languages associated with that extension. Falling back to an "all languages" scan is strictly forbidden for files with extensions.

**The Verification Mechanics:** The spectral scan relies on a multi-stage scoring system:
* **Phase 1 Pruning:** Candidates are checked against a lexical `DISQUALIFIERS` blacklist (e.g., rejecting a file claiming to be C if it contains `<?php`).
* **Delimiter Bonus:** The engine awards a flat +15.0 bonus if it detects the native comment delimiters of the claimed language's lexical family.
* **Language Handicaps:** Legacy species with highly generic syntax keywords (ABAP, Fortran, COBOL) are automatically assigned a 0.4x multiplier to prevent their broad regex rules from artificially swallowing other languages.
* **The Scoring Equation:** The raw score is normalized against the file's length using a logarithmic scale (`math.log1p(loc)`). The file must pass a minimum baseline signal threshold to be verified.

## Tier 4: The Deep Space Discovery Funnel

For true unknown files (no extension, no shebang, no prior), the Lens engages a 4-Phase Discovery Funnel. It prioritizes graceful failure over guessing.

1. **Phase 1: Comment Family Isolation:** The engine scans for structural delimiters (`//`, `#`, `--`, `/*`, etc.) to lock the file into a specific mechanical family. If no comment family can be established, it fails gracefully to `plaintext`.
2. **Phase 2: Heuristic Disqualification:** The surviving candidates are passed through the Blacklist engine to aggressively prune impossible matches.
3. **Phase 3: Structural Density Scan:** The engine calculates a Density Score (`Regex Hits / LOC`). This phase includes a Macro Blindspot Fix (boosting `std_c` families for `#define`/`#include` tags) and an ABAP Handicap to normalize scoring.
4. **Phase 4: The Ensemble Reconciliation Engine:** If multiple languages compete for the lock, the engine demands a 1.5x Density Margin. If the margin is weak, it utilizes a **Temporal Friction Tie-Breaker**, measuring the raw execution time of the regex engines to deduce the true language based on parser resistance (slower regex execution implies higher friction and an incorrect guess).

## Hybrid Detection (The Language Mix)

Many files in modern repositories are multi-language. To prepare the Cartographer for mapping the true complexity of a codebase, the Language Lens performs a preliminary Hybrid Detection scan.

* **The Handshake Protocol:** The engine uses a predefined `HANDSHAKE_REGISTRY` to monitor for transition triggers (e.g., `<script>`, `asm!()`, or `SELECT`).
* **Balanced Scoping:** For paired-bracket segments, the Lens tracks the nesting depth. It calculates the exact byte-length of the embedded alien segments.
* **The Telemetry Payload:** The Lens outputs a `lang_mix` array (e.g., `80% HTML, 20% JavaScript`). This telemetry is passed down the pipeline, signaling the Primary Detector to actively swap its regular expressions (Language Sliding) when processing the file's structural physics.

## Determinism and Inventory Integrity

For enterprise file inventory management, the Language Lens provides a fundamentally **deterministic and repeatable** framework. Unlike black-box LLMs that might return varying results based on floating-point drift or prompt phrasing, GitGalaxy's Bayesian engine is anchored in traceable linguistic physics.

* **Absolute Repeatability:** The same file, scanned under the same Roadmap context, will *always* yield the exact same Identity Lock and Confidence Score. This consistency is vital for Software Bill of Materials (SBOM) generation.
* **Traceable Inventory Logic:** Every identification is accompanied by its "Lock Tier" and "Source Proof". If a script is flagged as Python, the user can see precisely why (e.g., "Tier 1: Roadmap Lock via package.json" vs "Tier 4: Spectral Discovery"). This transparency allows security teams to distinguish between contextual certainty and heuristic discovery.

## Extending the Language Lens

GitGalaxy is designed to be infinitely extensible. To add native parsing support for a new language, you do not need to write a complex AST parser. You simply need to calibrate the thermodynamic physics of the target language using our strict LLM Master Prompt. Review the integration protocol here: **[Architecting a Review the integration protocol here: **[Architecting a New Language](./06-02-language-standards.md)**. Language](../../gitgalaxy/standards/how_to_add_a_language.md)**.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**