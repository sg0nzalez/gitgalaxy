# 2.2.P. Concurrency Exposure

## 2.2.P.A. The Philosophy:

Visualizes \"Temporal Static\" and the Signal-to-Noise Ratio of a file.
Concurrency is treated as \"Information Static\" because it fractures
the linear execution timeline, increasing the cognitive load required to
understand the file. The Tiger in the Cage rule applies here: We do not
discount concurrency just because it lives in a \"Worker\" or \"API\"
folder. A tiger in a cage is still dangerous. High concurrency is always
high cognitive load and high risk, regardless of where it lives.

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **LOW (Score 0-20, Blue):** Linear. The code executes sequentially
(1, then 2, then 3). The signal is clear and stable.
-   **MODERATE (Score 21-50, Yellow):** Standard async operations. Minor
temporal branching.
-   **VERY HIGH (Score 81-100, Red):** Noisy. The code manages multiple
parallel timelines (Promises, threads, channels). The signal is
highly fractured, warning that execution timing is
non-deterministic.

## 2.2.P.B. The Inputs (Temporal Markers)

We count the keywords that \"Fork\" time.

---------------- ------------------ ----------------- -----------------------------------------------------------------------------------------------------------------------------------------------
Input Variable   Regex Key          Weight            Rationale
**AsyncHits**    *concurrency*      **1.0x**          **The Fork.** Keywords that spawn or manage parallel execution: *async*, *await*, *Promise*, *thread*, *spawn*, *go*, *chan*, *synchronized*.
**LOC**          *meaningful_loc*   **Denominator**   We measure density. A 1000-line file with 1 *await* is linear. A 10-line file with 5 *await*s is a temporal knot.
---------------- ------------------ ----------------- -----------------------------------------------------------------------------------------------------------------------------------------------

## 2.2.P.C. The Universal Framework Integration

-   *Fc*** (Fidelity Coefficient):** **Not Applied.** Time is absolute.

-   *Irc*** (Implicit Risk Correction):** **Applied to Numerator
(Dampened).** Implicit languages (JS, Python) hide race conditions
better than explicit ones (Rust, Go). We add a small \"Ghost Load\"
to density, but we scale it down (*Irc \* 0.1*) so it acts as a
\"Tie Breaker\" rather than a false positive generator.

-   *Mp*** (Path Modifier):** **Applied to Threshold.**

-   *UI/Views (Mp = 0.5):* **Low Tolerance (High Scream).** Async
logic in UI code is a primary source of bugs (race conditions,
jank). We lower the bar so even minor concurrency glows here.
-   *Standard/Workers (Mp = 1.0):* **Standard Tolerance.** We do NOT
discount workers. If a worker is complex, it should look
complex.

## 2.2.P.D. The Equation: The Tipping Point Sigmoid

Concurrency complexity is non-linear. A single *await* is standard. Ten
*await* calls in a small function is a \"Logic Tangle.\" We use a
Sigmoid to create a visual \"Tipping Point.\"

Step 1: Pre-Filter (The Zero Check)

If the file contains **Zero** async hits, the score is **0**. No amount
of implicit risk can turn synchronous code into concurrent code.

*If AsyncHits == 0 -\> Score = 0*

Step 2: Calculate Temporal Density

We determine what percentage of the code is dedicated to managing time.
We add a *fraction* of *Irc* (0.1x) to penalize implicit safety gaps
without creating noise.

*Density = ((AsyncHits + (Irc \* 0.1)) / max(MeaningfulLOC, 1)) \* 100*

Step 3: Determine The Threshold (The Breakdown)

This is the density required to \"Fracture\" the signal.

-   **Base:** 4.0 (4% density). This provides a safe buffer for standard
async patterns before triggering warnings.
-   **Context:** Scaled by *Mp*. In UI (*Mp=0.5*), the threshold drops
to 2.0%.

*Threshold = 4.0 \* Mp*

Step 4: The Sigmoid Map

We map density against the threshold.

-   **Slope (K):** **0.4**. A moderately steep slope. Concurrency risk
escalates quickly.

*RawScore = 100 / (1 + e\^(-0.4 \* (Density - Threshold)))*

Step 5: Final Clamp

*FinalScore = min(RawScore, 100)*

## 2.2.P.E. Implementation (Python Reference)

*import math*

*def calculate_concurrency_exposure(self, hits_async, loc, irc, mp):*

* \"\"\"*

* Calculates 2.2.P Concurrency Exposure (Temporal Static).*

* Returns int 0-100.*

* \"\"\"*

* \# 1. Step A: Pre-Filter (Zero Check)*

* if hits_async == 0:*

* return 0*

* \# 2. Step B: Temporal Density*

* \# Scaled Irc (0.1x) prevents false positives in small files*

* weighted_hits = hits_async + (irc \* 0.1)*

* density = (weighted_hits / max(loc, 1)) \* 100*

* \# 3. Step C: Dynamic Threshold*

* \# Base = 4% density.*

* \# UI (Mp 0.5) -\> Threshold 2.0%.*

* \# Workers/Standard (Mp 1.0) -\> Threshold 4.0%.*

* path_mod = mp.get(\'Concurrency Exposure\', 1.0)*

* threshold = 4.0 \* path_mod*

* \# 4. Step D: Sigmoid Map*

* try:*

* raw_score = 100 / (1 + math.exp(-0.4 \* (density - threshold)))*

* except OverflowError:*

* raw_score = 100 if density \> threshold else 0*

* return int(min(raw_score, 100))*

## 2.2.P.F. Visual Verification (\"The Truth\")

**Comparison: 100 Line File**

------------------ ------ ------- ---------------- ------ ------------ ------------------- ---------------------------------------------------------------------------------------------
Synchronous Code   0      0.0%    Any              4.0%   **0.0**      LOW (Blue)          Zero hits = Zero score. Linear and safe.
Standard Async     \~4    4.5%    Standard (1.0)   4.0%   **\~55.0**   MODERATE (Yellow)   The tipping point. Just crossing the threshold.
The UI Tangle      \~5    5.5%    UI (0.5)         2.0%   **\~80.0**   HIGH (Orange)       Moderate async in UI triggers a high warning.
The Worker         \~10   10.5%   Worker (1.0)     4.0%   **\~93.0**   VERY HIGH (Red)     High density. Even though it\'s a worker, it is objectively complex. Correctly glowing red.
------------------ ------ ------- ---------------- ------ ------------ ------------------- ---------------------------------------------------------------------------------------------


