# 2.2.J. Documentation Risk Exposure (Metric: Sigmoid Debt)

## 2.2.J.1. The Philosophy: The Duty of Care

Visualizes the \"Duty of Care\" a developer owes to their future self
and the collective. This metric does not reward the raw volume of text;
it measures the Density of Intent. We distinguish between
\"Library-Grade\" engineering---where a component is supported by
structured metadata---and \"Silent Logic,\" which requires the reader to
perform manual mental compilation to understand the *why* behind the
*what*.

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **THOROUGH (Score 0-20, Blue):** Saturated Map. Perfect coverage
with high intent density.
-   **MODERATE (Score 41-60, Yellow):** Functional baseline. Meets
standard safety thresholds.
-   **UNDOCUMENTED (Score 90-100, Red):** Total Opacity. Zero intent
density, representing high maintenance risk.

## 2.2.J.2. The Inputs (Tiered Efficiency)

The regex scanning has been abstracted out of the physics engine. The
*blAST* engine now pre-calculates documentation lines and structured
hits, passing them into the Signal Processor.

------------- --------------- ------- -------- --------------------------------------------------------------------------------------------------------------------------------------------
Doc Hits      **doc**         1.0x    High     Tier 1 (The Interface). Gold standard tags (**\@param**, **///**). One hit provides a full point of intent density.
Header Hits   **ownership**   0.5x    Medium   Tier 2 (The Metadata). Attribution and file-level summaries. Valuable context, but less critical for line-by-line logic comprehension.
Doc LOC       **doc_loc**     0.33x   Low      Tier 3 (The Narrative). General inline comments. Requires 3 lines of text to equal 1 structured tag, honoring effort but demanding volume.
------------- --------------- ------- -------- --------------------------------------------------------------------------------------------------------------------------------------------

## 2.2.J.3. The Universal Framework Integration

-   **Fc (Fidelity Coefficient):** Applied to the final risk reduction.
We trust documentation in Explicit languages (e.g., Rust) more than
in Implicit languages (e.g., Shell), where comments are prone to
\"drifting\" from the actual logic.

-   **Irc (Implicit Risk Correction):** Applied to the Threshold.
Implicit languages require a higher \"Opacity Tax.\" They need more
documentation density just to reach a baseline safety level.

-   **Mp (Path Modifier):**

-   **Public/API (Mp = 1.5):** High Bar. This is the face of the
system. Lack of docs here is punished more severely.
-   **Tests/Experiments (Mp = 0.5):** Low Bar. Internal logic is
more \"forgiven\" for being silent.

## 2.2.J.4. The Equation: The Dynamic Risk Sigmoid

*We calculate the density of intent and map it to a \"Debt Curve\" where
the score represents the Exposure caused by missing documentation.*

**Step A: The Micro-Bypass** Tiny scripts (\<= 2 lines of code) with 0
documentation are automatically granted a *0.0* risk score. A one-line
utility function does not require a map.

**Step B: Calculate Intent Density** We sum the weighted points and
normalize them against the file size (*loc*). A 1000-line file requires
significantly more intent-signaling than a 10-line utility.

**Step C: Determine The Risk Threshold (The Bar)** We calculate the
\"Tipping Point\" where a file transitions from \"Well-Documented\" to
\"High Risk.\" We add the Implicit Risk Correction (*Irc*)---meaning
opaque languages like Shell require a higher density to reach baseline
safety---and multiply by the Path Modifier (*Mp*). For example, public
APIs (high *Mp*) raise the threshold significantly.

**Step D: The Risk Sigmoid Map** We use a sigmoid with a positive
exponent. As Documentation Density increases, the Risk Score
mathematically decreases.

**Step E: Fidelity Trust Multiplier** Finally, we apply the Fidelity
Coefficient (*Fc*). Low-fidelity languages (high *Irc*, low *Fc*) suffer
an inverted trust multiplier, acknowledging that comments in those
languages are more prone to drifting from reality.

## 2.2.J.5. Implementation (Python Reference)

*import math*

*from typing import Dict*

*def \_calc_documentation(self, loc: int, doc_loc: int, eq: Dict\[str,
int\], fc: float, irc: int, mp: float) -\> float:*

* t = self.risk_tuning.get(\"documentation\", {})*

* *

* \# Step B: Calculate Intent Density*

* weighted_points = (eq.get(\"doc\", 0) \* t.get(\"doc_weight\", 1.0)) +
\\*

* (eq.get(\"ownership\", 0) \* t.get(\"ownership_weight\", 0.5)) + \\*

* (doc_loc \* t.get(\"doc_loc_weight\", 0.33))*

* density = (weighted_points / loc) \* 100.0*

* *

* \# Step A: Micro-bypass for tiny utilities*

* if loc \<= 2 and doc_loc == 0:*

* return 0.0*

* *

* \# Step C: Dynamic Threshold*

* threshold = (t.get(\"threshold_base\", 10.0) + irc) \* mp*

* *

* \# Step D: Sigmoid Map*

* try:*

* raw_risk = 100.0 / (1.0 + math.exp(t.get(\"sigmoid_slope\", 0.2) \*
(density - threshold)))*

* except OverflowError:*

* raw_risk = 0.0 if density \> threshold else 100.0*

* *

* \# Step E: Fidelity Trust Multiplier*

* return min(raw_risk \* (2.0 - fc), 100.0)*

## 2.2.J.6. Visual Verification (\"The Risk Audit\")

*Comparison: 100 Line File (Threshold 10)*

------------------ ---------------------- ------ ------ -------------------- ----------------------------------------------------------------
The Architect      15 **\@param** tags    15.0   \~27   LOW (Cyan)           Safe. High documentation density results in low risk exposure.
The Professional   10 **\@param** tags    10.0   \~50   MODERATE (Yellow)    Stable. Hits the threshold exactly; moderate exposure.
The Student        10 lines of comments   3.3    \~79   HIGH (Orange)        Risky. Minimal narrative effort fails to clear the safety bar.
The Silent         0 comments             0.0    \~88   UNDOCUMENTED (Red)   Critical. Zero intent density results in high risk exposure.
------------------ ---------------------- ------ ------ -------------------- ----------------------------------------------------------------
