# 2.3.6. Signal Processing (Equations and 2nd Pass scanning Calculations)

## 2.3.6.A. Overview: The Post-Processing Pipeline

The Signal Processor acts as GitGalaxy\'s core Physics Engine. Once the
Splicer has carved the raw structural telemetry (the 60-Point
*SIGNAL_SCHEMA*), the Physics Engine resolves these counts into
meaningful, scaled insights---the 18-Point *RISK_SCHEMA*.

Rather than executing static math, the v6.2.0 Protocol introduces a
multi-pass architecture. It evaluates a file not just in isolation, but
against the physical reality of its surrounding neighborhood and the
temporal history of the entire galaxy.

## 2.3.6.B. The Context vs. Entity Matrix (Domain Ontologies)

A file\'s risk profile changes drastically depending on where it lives.
A C++ file in a firmware repository is expected; a C++ file hidden deep
inside a frontend JavaScript repository is highly anomalous.

To catch these architectural Trojans, the engine utilizes the **Context
vs. Entity Matrix**:

-   **Native Ecosystems:** The engine compares the file\'s language
against the dominant language of its parent folder. If they match
the same domain ontology (e.g., both are *backend*), the file is
processed using standard native weights.
-   **Alien Entities (Trojan Detection):** If a severe context mismatch
occurs, the file is classified as an \"Alien.\" The engine
dynamically injects severe risk multipliers. For example, a
systems-level file (*c*, *rust*) hiding in a web neighborhood
(*javascript*, *html*) receives massive multipliers to its
*logic_bomb* and *memory_corruption* exposures, immediately flagging
it as a severe architectural or security anomaly.

## 2.3.6.C. Standardization: The Tiered Physics Model

To ensure comparative fairness across different code \"materials,\" the
engine applies Linguistic Normalization. This accounts for the fact that
explicit languages (like Rust) \"broadcast\" their safety, while
implicit languages (like Shell) hide their risks.

The instrument applies specific Trust Constants based on the language\'s
spectral class:

-   **Tier 1: Explicit (Rust, Go, Swift, Java):** Signals are trusted at
face value. The Fidelity Coefficient is 1.0, and \"Implicit Risk\"
is zero.
-   **Tier 2: Structured (Python, JS, C++):** Translucent. A minor
\"Opacity Tax\" is applied to account for potential runtime
surprises.
-   **Tier 3: Implicit (Shell, SQL, Assembly):** Opaque. The \"Fog of
War\" penalty adds a baseline phantom risk to all equations,
requiring significantly higher defensive density to achieve a
\"Safe\" rating.

## 2.3.6.D. The Documentation Bypass & Silo Risk

Pure literature files (*markdown*, *plaintext*) do not execute logic. To
prevent them from skewing the galaxy\'s structural averages, the engine
routes them through a strict **Documentation Bypass**.

While their logic metrics are safely zeroed out, they still undergo
rigorous temporal and ownership physics:

-   **Ownership Entropy:** Calculates the Shannon Entropy of the file\'s
Git commit history. A score of 0 indicates a single author (stable
but siloed), while 100 indicates massive community distribution.
-   **Silo Risk (The Bus Factor):** Calculates the specific dependency
the file has on its dominant author. If one developer wrote 95% of a
critical architecture file, the Splicer flags a high Silo Risk,
alerting management to critical \"Bus Factor\" vulnerabilities.

## 2.3.6.E. Global Synthesis & 2-Pass Normalization

Because temporal metrics (like commit frequency) vary wildly between
repositories, a hardcoded churn threshold is useless. A file with 5
commits might be volatile in a dead repository but highly stable in an
active one.

GitGalaxy solves this via **Two-Pass Normalization**:

1.  **Pass 1 (Raw Extraction):** The engine calculates the absolute Age
(Stability) and the raw Churn Frequency (Commits over time) for
every individual star.
2.  **Pass 2 (The Global Curve):** Once all files are processed, the
*\_normalize_temporal_metrics* engine scans the entire galaxy to
find the \"Volcano\" (the absolute maximum churn frequency in the
repository). It then applies a Logarithmic Curve (*math.log1p*) to
scale every file\'s churn relative to that global ceiling. This
guarantees that the UI gradients perfectly highlight the hottest
files in the repository, regardless of the team\'s specific commit
culture.

## 2.3.6.F. The Physics Engine: Weighted Asymmetry & Mass

In the final stage, the engine generates the high-fidelity Forensic
Report. To prevent noise, it applies an **Active Logic Mask**, blinding
the ranking algorithms to structural assets (like JSON configs or
Markdown) so only true executable code competes for the \"Highest Risk\"
spots.

Alongside ranking individual vectors (like highest Tech Debt or lowest
Safety), the v6.2.0 engine calculates **Cumulative Risk**. It
mathematically sums all 17 active exposure vectors (excluding formatting
metrics like Civil War) to identify the absolute most dangerous, dense,
and volatile artifacts in the repository.
