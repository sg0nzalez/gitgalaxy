# 2.2.I. Technical Debt Exposure

## 2.2.I.A. The Philosophy: Markers of Honesty

**\"The Topography of Compromise.\"**

Visualizes the \"Topography of Compromise.\" We view Technical Debt not
as a failure, but as a deliberate engineering trade-off. No engineer
writes a HACK out of laziness; they write it to ship. This metric is
about Honesty. It relies on the developer\'s own annotations (in the
Literature/Comment Stream) to identify where the \"Structural Stress\"
lies. By visualizing these markers, we move from vague anxiety about
\"bad code\" to a concrete map of where the team knows improvements are
needed.

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **VERY LOW (Score 0-20, Blue):** Polished. The code matches the
spec. No known shortcuts.
-   **INTERMEDIATE (Score 41-60, Yellow):** Honest work-in-progress. A
balanced mix of planned tasks.
-   **VERY HIGH (Score 81-100, Red):** Fractured. The file is held
together by temporary fixes (*HACK*) and unfinished thoughts
(*TODO*). It is structurally compromised.

## 2.2.I.B. The Inputs (Regex & Heuristics)

The regex scanning has been entirely decoupled from the physics engine.
The *blAST* engine now pre-calculates these hits and passes them into
the Signal Processor\'s *eq* dictionary.

--------------- ---------------------------------------- ------ ------------------------------------------------------------------------------------------------------------------------------------------------------
Planned Debt    **planned_debt**                         1.0x   The Promise. Future work that doesn\'t necessarily imply current brokenness. Includes **TODO**, **WIP**, **STUB**, **REFACTOR**.
Fragile Debt    **fragile_debt** (or **keyword_debt**)   3.0x   The Fracture. An explicit admission that the current logic is fragile or dangerous. Includes **HACK**, **FIXME**, **XXX**, **WORKAROUND**, **UGLY**.
Stub Hits       **func_empty**                           0.5x   The Skeleton. Empty functions (**{}**) found in the Logic Stream. Implies placeholder logic independent of comments.
Implicit Risk   **irc**                                  0.5x   The Fog. Implicit languages hide debt better, so we add a weighted baseline load to the stress sum.
--------------- ---------------------------------------- ------ ------------------------------------------------------------------------------------------------------------------------------------------------------

## 2.2.I.C. The Universal Framework Integration

-   *Fc*** (Fidelity Coefficient):** **Not Applied.** A *TODO* is a
*TODO*, regardless of language.

-   *Irc*** (Implicit Risk Correction):** **Applied.** Added to the
Stress Sum.

-   *Mp*** (Path Modifier):** **Applied.**

-   *Archive/Legacy (Mp = 0.5):* Debt is expected here. Discount it.
-   *Core/Kernel (Mp = 1.2):* Debt here is dangerous. Amplify it.
-   *Scratchpad (Mp = 0.8):* Allow messy thoughts.

## 2.2.I.D. The Equation: The Structural Stress Density

We calculate the Density of Debt per line of code.

**Step A: Calculate Stress Sum** We sum the markers, applying weights to
distinguish \"Planned Work\" (Good Debt) from \"Broken Logic\" (Bad
Debt). We also add the Implicit Risk Correction (*Irc*), dampened by its
own weight multiplier (*0.5*).

**Step B: Calculate Stress Density** We normalize against the file size
to calculate the stress points per 100 lines. A 1000-line file with 1
*TODO* is fine. A 10-line file with 1 *HACK* is structurally critical.

**Step C: The Sigmoid Map** We use a Sigmoid function to create a
\"Tolerance Threshold\".

-   **Threshold (T):** *5.0*. We tolerate \~5 points of stress per 100
lines before the score spikes.
-   **Slope (K):** *0.5*. A gentle slope allows for nuance as debt
accumulates.

**Step D: Final Calculation** We apply the Path Modifier (*Mp*) to
dampen or amplify the final score based on the file\'s architectural
context.

## 2.2.I.E. Implementation (Python Reference)

*import math*

*from typing import Dict*

*def \_calc_tech_debt(self, loc: int, eq: Dict\[str, int\], irc: int,
mp: float) -\> float:*

* t = self.risk_tuning.get(\"tech_debt\", {})*

* good_debt = eq.get(\"planned_debt\", 0)*

* bad_debt = eq.get(\"fragile_debt\", eq.get(\"keyword_debt\", 0))*

* stubs = eq.get(\"func_empty\", 0)*

* *

* if good_debt == 0 and bad_debt == 0 and stubs == 0:*

* return 0.0*

* *

* \# Step A: Stress Sum*

* stress = (good_debt \* t.get(\"good_debt_weight\", 1.0)) + \\*

* (bad_debt \* t.get(\"bad_debt_weight\", 3.0)) + \\*

* (stubs \* t.get(\"stub_weight\", 0.5)) + \\*

* (irc \* t.get(\"irc_weight\", 0.5))*

* *

* \# Step B: Density Calculation*

* density = (stress / max(loc, 1)) \* 100.0*

* threshold = t.get(\"threshold\", 5.0)*

* *

* \# Step C: Sigmoid Map*

* try:*

* raw_score = 100.0 / (1.0 + math.exp(-t.get(\"sigmoid_slope\", 0.5) \*
(density - threshold)))*

* except OverflowError:*

* raw_score = 100.0 if density \> threshold else 0.0*

* *

* \# Step D: Apply Context Modifier*

* return min(raw_score \* mp, 100.0)*

## 2.2.I.F. Visual Verification (\"The Truth\")

---------------- ------ ---------------------------- ------ ------ -------- -------------------------------------------------------------------------------------------------
Clean Core       200    0                            0.0    0      Blue     Pristine. Zero structural stress.
Honest Dev       200    2 **REFACTOR**, 3 **TODO**   2.5    22     Cyan     Good citizenship. Admitting work is needed, but well under the threshold.
The Prototype    100    2 STUBs, 4 **WIP**s          5.0    50     Yellow   Halfway point. Rough but honest.
Frustrated Dev   50     1 **WTF**, 1 **HACK**        12.0   \~97   Red      High emotional and structural stress. Severe technical debt.
Legacy Dump      1000   20 **HARDCODED**             6.0    \~31   Cyan     With Mp=0.5. Large volume and high debt, but heavily discounted because it is marked as legacy.
---------------- ------ ---------------------------- ------ ------ -------- -------------------------------------------------------------------------------------------------
