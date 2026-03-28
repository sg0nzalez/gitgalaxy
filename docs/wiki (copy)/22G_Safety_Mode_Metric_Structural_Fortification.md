#### 2.2.G. Safety Mode (Metric: Structural Fortification)

##### 2.2.G.A. The Philosophy: Structural Integrity \"The Load-Bearing Capacity of Code.\"

**Summary:** Visualizes the \"Load-Bearing Capacity\" of the code. We
treat code like physical infrastructure. A bridge is safe not because it
has no cars (complexity), but because it has enough support pillars
(guardrails) to hold the traffic.

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **VERY LOW (Score 0-20, Blue):** Fortified. Defensive structures
(try/catch, guards) vastly outnumber the risks.
-   **INTERMEDIATE (Score 41-60, Yellow):** Stable. Risks and defenses
are roughly balanced.
-   **VERY HIGH (Score 81-100, Red):** Fragile. The structural load
(Risk) exceeds the support capacity (Defenses). The code is liable
to collapse under edge cases.

##### 2.2.G.B. The Inputs (Regex & Heuristics)

We classify patterns into **Attackers** (Risk) and **Defenders**
(Safety).

------------ ------------------ ------------- ------------------------------------------------------------------------------------------
RiskHits     **danger**         4.0x          The Heavy Load. Critical vulnerabilities (**eval**, **exec**) that exert massive stress.
NegHits      **safety_n**eg**   1.5x          The Rust. Anti-patterns (**var**, **any**, suppress) that weaken the structure.
FluxHits     **flux**           0.5x          The Vibration. Mutable state introduces entropy.
SafetyHits   **safety**         1.0x (Base)   The Pillars. Try/catch, assertions, type guards.
TestHits     **test**           0.5x          The Blueprint. Proximity to tests implies verification.
DocHits      **doc**            0.1x          The Warning Labels. Provides a minor structural defense bonus.
------------ ------------------ ------------- ------------------------------------------------------------------------------------------

##### 2.2.G.C. The Universal Framework Integration

-   *Fc*** (Fidelity Coefficient):** Applied to **Defenders**. We trust
a *try/catch* in Java (Explicit) more than a check in Shell
(Implicit).

-   *Irc*** (Implicit Risk Correction):** Added to **Attackers**.
Implicit languages start with a \"Phantom Load\"---a baseline risk
inherent to the medium.

-   *Mp*** (Path Modifier):** Applied to **Attackers**. We keep the
discount small to ensure risks are exposed everywhere.

-   *Exp/Tests (Mp = 0.9):* **Minor Discount.** Risks are slightly
forgiven, but unsafe code will still flash Red.
-   *Core/Auth (Mp = 1.2):* **Amplified.** Risks are punished
heavily. Fragility here is unacceptable.
-   *Standard (Mp = 1.0):* Baseline.

##### 2.2.G.D. The Equation: The Structural Integrity Sigmoid

The math has been entirely rewritten to calculate **Net Exposure**
rather than Integrity Density, and introduces Laplace Smoothing to
prevent tiny files from aggressively skewing the spectrum.

**Step A: Calculate Smoothed Attack & Defense Densities** We sum the
weighted risks and fortifications. Instead of dividing strictly by LOC,
we use **Laplace Smoothing** (*LOC + 20.0*). This prevents a 5-line file
with a single *try/catch* from registering as infinitely safe.

-   **Attack** is amplified by *Irc* (Implicit Risk) and scaled by *Mp*
(Path Context).
-   **Defense** is dampened by *Fc* (Fidelity/Trust).

**Step B: Calculate Net Exposure** *Net Exposure = Attack - Defense*. We
also subtract a minor *systems_buffer* for implicit languages to account
for their naturally looser structures.

-   **Positive Exposure:** Risks outweigh Defenses (Fragile / Red).
-   **Negative Exposure:** Defenses outweigh Risks (Fortified / Blue).

**Step C: The Sigmoid Score & Breach Floor** We map the exposure to a
0-100 scale using a steep Sigmoid slope (*12.0*).

-   **The Breach Floor:** If the code has a high density of explicit
*danger* hits and Attack outpaces Defense, the file is subject to a
hard risk floor (scaling up to 80.0), guaranteeing that catastrophic
structural weaknesses cannot be \"math-ed away\" by simply adding
empty *try/catch* blocks.

##### 2.2.G.E. Implementation (Python Reference)

*import math*

*from typing import Dict*

*def \_calc_safety(self, loc: int, eq: Dict\[str, int\], irc: int, fc:
float, mp: float) -\> float:*

* safe_loc = max(loc, 1)*

* t = self.risk_tuning.get(\"safety\", {})*

* *

* \# 1. Weighted Sums*

* attack_hits = (eq.get(\"danger\", 0) \* t.get(\"danger_weight\",
4.0)) + \\*

* (eq.get(\"safety_neg\", 0) \* t.get(\"safety_neg_weight\", 1.5)) + \\*

* (eq.get(\"flux\", 0) \* t.get(\"flux_weight\", 0.5))*

* *

* defense_hits = (eq.get(\"safety\", 0) \* self.WEIGHT_DEFENSE) + \\*

* (eq.get(\"test\", 0) \* t.get(\"test_weight\", 0.5)) + \\*

* (eq.get(\"doc\", 0) \* t.get(\"doc_weight\", 0.1))*

* *

* if attack_hits == 0:*

* return 0.0*

* *

* \# 2. Laplace Smoothing (+20 LOC) to prevent tiny-file explosions*

* smoothed_loc = safe_loc + t.get(\"laplace_smoothing\", 20.0)*

* *

* attack = ((attack_hits + irc) / smoothed_loc) \* mp*

* defense = (defense_hits / smoothed_loc) \* fc*

* *

* \# 3. Net Exposure Calculation*

* systems_buffer = t.get(\"systems_buffer\", 0.25) if fc \< 1.0 else
0.0*

* net_exposure = (attack - defense) - systems_buffer*

* *

* \# 4. Sigmoid Mapping*

* try:*

* score = 100.0 / (1.0 + math.exp(-t.get(\"sigmoid_slope\", 12.0) \*
net_exposure))*

* except OverflowError:*

* score = 100.0 if net_exposure \> 0 else 0.0*

* \# 5. The Breach Floor (Punishing undefended danger)*

* danger_density = (eq.get(\"danger\", 0) + eq.get(\"safety_neg\", 0)) /
safe_loc*

* if danger_density \> t.get(\"breach_density_min\", 0.03) and attack \>
defense:*

* floor = min(t.get(\"breach_floor_max\", 80.0), 30.0 + (danger_density
\* t.get(\"breach_floor_mult\", 500.0)))*

* score = max(score, floor)*

* *

* return max(score, 0.0)*

##### 2.2.G.F. Visual Verification (\"The Truth\")

---------------------- -------- --------- ----------- -------- -------------- -----------------------------------------------------------------------------
Scenario               Attack   Defense   Net / LOC   Score    Color          Interpretation
**Stable Logic**       5        5         0.0         **50**   **White**      Balanced. Risks matched by guards.
**The Bunker**         2        20        +0.18       **86**   **Cyan**       Highly fortified. Guards vastly outnumber risks.
**Glass Cannon**       20       2         -0.18       **14**   **Red**        Fragile. Heavy risks with no support pillars.
**Experiment (Old)**   20       2         -0.09       **29**   **Pale Red**   *With Mp=0.5*. Risk was hidden/dampened.
**Experiment (New)**   20       2         -0.16       **17**   **Red**        *With Mp=0.9*. Risk is now clearly visible.
**Implicit Script**    5        5         -0.05       **37**   **Pale Red**   *With Irc=5*. Even \"balanced\" code looks fragile due to language opacity.
---------------------- -------- --------- ----------- -------- -------------- -----------------------------------------------------------------------------
