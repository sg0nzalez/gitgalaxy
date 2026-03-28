# 2.3.3. Focusing the Language Lens

> **Phase 1: The Entity Census**
>
> Before the GitGalaxy pipeline can calculate the physics of Star Mass or determine security risk, it must perform a comprehensive Entity Census. This phase is responsible for assigning a high-fidelity "Identity Lock" (`lang_id`) to every artifact in the repository.
>
> In the era of AI-generated code and automated refactoring, single-point metadata is no longer a source of absolute truth. We live in a world where assuming a file's language based solely on its extension is one hallucination away from disaster. The Language Lens operates on a Bayesian model of Contextual Convergence, treating every file as a "claim" that must be proven through a strict hierarchy of evidence.

## 2.3.3.A. The Bayesian Engine: Prediction vs. Audit

GitGalaxy adopts a rigorous stance on identity: True confidence requires convergence. A single metadata signature (like an extension alone) is merely a suggestion. The engine evaluates files against an 8-Tier Trust Matrix to establish their identity.

| Tier | Lock Type | Source Evidence | Confidence | Structural Definition |
| :--- | :--- | :--- | :--- | :--- |
| **0** | **Convergent Lock** | Dual Evidence | **0.95 - 0.99** | Verified Identity: Two independent signals match (e.g., Ext + Shebang, or Ext + GuideStar Prior). Perfect focus achieved. |
| **1** | **Roadmap Lock** | GuideStar Manifest | **0.95** | Authoritative Proof: The project's build system (e.g., `package.json`) explicitly defines the file. |
| **1.5** | **Ecosystem Gravity** | Neighborhood Dominance | **0.95** | Collision Resolution: Resolves highly contested extensions (like `.h`) by analyzing the dominant languages in the repository. |
| **1.7** | **Exo-Species** | Unknown Extension | **0.95** | Fallback Trust: Acknowledges short, alphanumeric custom extensions as valid unknown structures. |
| **2** | **Single Signature** | Extension OR Shebang | **0.91** | Unverified Claim: Single-point metadata is a suggestion. Triggers mandatory spectral verification. |
| **3** | **Contextual Proof** | GuideStar Bias | **0.90** | Suggested Intent: Context suggests importance, but identity requires spectral scanning. |
| **4** | **Discovery** | Zero Context | **0.10** | Deep Space Mystery: No roadmap or extension. Must pass rigorous structural density checks to be acknowledged. |
| **5** | **Absolute Distrust** | Identity Crisis | **0.00** | Security Anomaly: Extension and Shebang explicitly contradict each other. Banished to the Singularity. |

## 2.3.3.B. The Pre-Flight Sequence: Anchors & Wrappers

Before engaging the heavy regex detectors, the Lens secures the perimeter, resolves hidden names, and defends against prose hijacking.

* **Dotfile & Hidden Extension Resolution:** The Lens intelligently bypasses false extensions on dotfiles (e.g., `.bashrc`). Furthermore, it peels back safe wrapper extensions (`.template`, `.bak`, `.orig`) to discover the true hidden extension beneath (e.g., extracting `.sh` from `script.sh.template`).
* **Metadata Anchors:** Instantly locks exact matches like `Dockerfile` or `Jenkinsfile`.
* **The Code Shield:** A critical security feature preventing "Prose Hijacking." If a developer names a C++ file `README.cpp`, the engine will not treat it as Markdown. If a file has a known executable extension, it strictly bypasses prose checks so hostile logic cannot hide inside fake documentation.

## 2.3.3.C. The Identity Crisis Trap (Security Integration)

The Lens acts as the first line of defense for the Security Module. It performs a cross-examination of physical signals. If a file claims to be a Python script (`.py`) but contains a Bash shebang (`#!/bin/bash`), the file is lying about its physical identity.

* **The Result:** The Lens flags this as an "Identity Masking" anomaly, caches it in the RAM `anomaly_flags` for the Security Lens, and forces the file into Tier 5 Absolute Distrust, destroying its identity and banishing it to the Singularity (`undeterminable`).

## 2.3.3.D. Tier 1.5: Ecosystem Gravity (Collision Resolution)

Certain extensions, like `.h`, are heavily collided (used primarily by C, C++, and Objective-C). The Lens uses "Ecosystem Gravity" to resolve these ties without expensive deep-packet inspection, actively pulling files into the orbit of the repository's dominant language.

**The Physics Engine:** It evaluates candidates by looking at the repository's `ext_tally` to calculate three specific masses:
* **Base Mass:** The standard supporting extensions in the ecosystem.
* **Discriminator Mass:** Highly specific extensions that strongly prove an ecosystem exists. These are heavily weighted (multiplying the base score by 2.0x).
* **Toxic Mass:** Disqualifying extensions. If a single toxic extension is present in the repository, it triggers "Thermodynamic collapse" (Score = 0.0), instantly disqualifying that language.

**The Dominance Threshold:** To achieve a Tier 1.5 lock, the winning language must not only survive the physics engine but must achieve a dominance ratio of at least 70% (`ECOSYSTEM_DOMINANCE_MIN`) over all other competitors. *(Note: The engine includes a hardcoded failsafe ensuring C++ is always allowed to compete for `.h` files, even if not explicitly mapped).*

## 2.3.3.E. Tier 3: Spectral Verification & The Iron Wall

Files that land at Tier 2 (Single Signature) must undergo Mandatory Spectral Verification to prove they contain the structural logic they claim to hold.

**The Iron Wall Scanner:** To prevent the engine from hallucinating, the Lens enforces a strict boundary. If a file has an extension, it MUST be claimed by one of the known languages associated with that extension. If the candidates fail, falling back to an "all languages" scan is strictly forbidden for files with extensions, ensuring mathematical bounds are respected.

**The Verification Mechanics:** The spectral scan relies on a multi-stage scoring system:
* **Phase 2 Pruning:** Candidates are first checked against a `DISQUALIFIERS` blacklist based on their lexical family to prevent impossible matches.
* **Delimiter Bonus:** The engine awards a flat +15.0 bonus if it detects the native comment delimiters of the claimed language's lexical family (e.g., `//` or `/*`).
* **Language Handicaps:** Legacy species with highly generic syntax keywords (ABAP, Fortran, COBOL) are automatically assigned a 0.4x multiplier to prevent their broad regex rules from artificially swallowing other languages.
* **The Scoring Equation:** The raw score (`Regex Hits * 10.0 + Delimiter Bonus`) is normalized against the file's length using a logarithmic scale (`math.log1p(loc)`). The file must pass a minimum baseline signal threshold to be verified.

## 2.3.3.F. Tier 4: The Deep Space Discovery Funnel

For true unknown files (no extension, no shebang), the Lens engages a redesigned 4-Phase Discovery Funnel. It prioritizes graceful failure over guessing.

1. **Phase 1: Comment Family Isolation:** The engine scans for structural delimiters (`//`, `#`, `--`, etc.) to lock the file into a specific mechanical family. If no comment family can be established, it fails gracefully.
2. **Phase 2: Heuristic Disqualification:** The surviving candidates are passed through the Blacklist engine to aggressively prune impossible matches.
3. **Phase 3: Structural Density Scan:** The engine calculates a Density Score (`Regex Hits / LOC`). This phase includes a Macro Blindspot Fix (boosting `std_c` families for `#define`/`#include` tags) and an ABAP Handicap to normalize scoring.
4. **Phase 4: The Ensemble Reconciliation Engine:** If multiple languages compete for the lock, the engine demands a 1.5x Density Margin. If the margin is weak, it utilizes a **Temporal Friction Tie-Breaker**, measuring the raw execution time of the regex engines to deduce the true language based on parser resistance.

## 2.3.3.G. Hybrid Detection (Language Sliding)

Many files in modern repositories are multi-language. To map the true complexity of a codebase, the engine implements Mid-File Language Sliding.

### 1. The Handshake Protocol (Detection)
As the engine processes the logic stream, it monitors for **Linguistic Handshakes**. These are specific tokens that broadcast a transition into a secondary spectrum, signaling the detector to swap its "Regex Lens" and define the boundaries of the secondary star.

| Linguistic Transition | Start Marker (Trigger) | End Trigger | Assessment Logic |
| :--- | :--- | :--- | :--- |
| **HTML** to **JavaScript** | `<script` | `</script>` | Pause HTML; activate JS Registry. |
| **HTML** to **CSS** | `<style` | `</style>` | Pause HTML; activate CSS Registry. |
| **Any** to **SQLite** | `SELECT\s+.*\s+FROM` | `['"]` (String End) | Scan segment with SQL registry. |
| **Config** to **Shell** | `RUN\s+` or `script:` | De-indentation or `\n` | Switch to Shell for the block. |
| **Systems** to **Assembly**| `asm!\(` or `__asm__` | **Balanced Scoping** | Switch to Assembly for logic block. |

### 2. The Fluid State Counter (Language Sliding)
Because the 40+ regex key schema is standardized across all languages, the results dictionary acts as a **Universal Vessel**. This allows for "Fluid State" counting:
* **Lens Swapping:** When a handshake is detected, the engine pauses the primary registry and activates the secondary registry.
* **Bucket Continuation:** Hits in the secondary language feed the **same regex buckets** as the primary language. For example, an `if` statement in an embedded JS block increments the same `branch` counter that the parent HTML tags were previously feeding.
* **Fidelity Handover:** The Fidelity Coefficient ($\text{Fc}$) and Implicit Risk ($\text{Irc}$) parameters are swapped dynamically to reflect the trust levels of the active segment (e.g., switching from Tier 3 HTML trust to Tier 2 JS trust mid-file).

### 3. The Polyglot Advantage
This fluid transition ensures that regex can switch languages with the user. Without Language Sliding, a file that is 50% HTML and 50% JavaScript would appear falsely lower in exposure risk (false security). By sliding the focus, GitGalaxy captures the full score of the file, capturing every `await`, `fetch`, and `try/catch` across linguistic boundaries with less than 5% extra compute overhead. *(Note: This version does not offer triple-nested language recognition at this point).*

### 4. Scoping Integrity (The Termination Logic)
To prevent premature lens-swapping—particularly in complex, multi-line Assembly or Logic-to-SQL shifts—the engine employs **Balanced Scoping**. Instead of stopping at the first closing character, the detector maintains a "Handshake Stack."
* **Balanced Pairs:** For triggers using braces `{}` or parentheses `()`, the engine tracks the nesting depth. The lens only reverts to the primary spectrum when the stack depth returns to zero.
* **Heuristic Confidence:** In ambiguous scenarios (like SQL embedded in dynamic strings), the engine uses a **Logic Anchor Check**. If the scanner encounters the end-trigger but the next few tokens significantly deviate from the primary language's frequency, it maintains the focus until a higher-confidence "Safe Exit" is found.

## 2.3.3.H. Determinism and Inventory Integrity

For enterprise file inventory management, the Language Lens provides a fundamentally **deterministic and repeatable** framework. Unlike "black-box" AI models that might return varying results based on floating-point drift or model versioning, GitGalaxy's Bayesian engine is anchored in traceable linguistic physics.

* **Absolute Repeatability:** The same file, scanned under the same Roadmap context, will *always* yield the exact same Identity Lock and Confidence Score. This level of consistency is vital for security compliance and Software Bill of Materials (SBOM) generation, ensuring that inventory lists do not fluctuate during repeated scans of static repositories.
* **Traceable Inventory Logic:** Every identification could be accompanied by its "Lock Tier" (0–4). This could provide a forensic audit trail for every artifact in the galaxy. If a script is flagged as Python, the user can see precisely why (e.g., "Tier 1: Roadmap Lock via package.json"). This transparency allows inventory managers to distinguish between "Contextual Certainty" and "Spectral Discovery," enabling high-integrity auditing of the codebase.
