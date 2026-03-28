# 2.2.N. The \"Graveyard\" Detector (Metric: Architectural Transparency)

## 2.2.N.A. The Philosophy: \"The Fear of Deletion.\"

Visualizes \"Code Necrosis\" or \"The Fear of Deletion.\" Commented-out
code (\"Ghost Logic\") is not documentation; it is hesitation. It
implies a lack of trust in Version Control. It creates cognitive noise,
forcing the reader to mentally parse and discard logic that is no longer
active.

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **CLEAN (Score 0-20, Blue):** Active, clean, executed. Pure life.
-   **INTERMEDIATE (Score 41-60, Yellow):** Minor scraps. Tolerable
depending on the context.
-   **GRAVEYARD (Score 81-100, Red):** Heavily polluted with dead
blocks. The file is \"Haunted\" by its past.

## 2.2.N.B. The Inputs (Heuristic Detection)

We distinguish between Documentation (English text) and Graveyards
(Inactive Code) by scanning for syntax density within comment blocks.
The backend now calculates the raw blocks, and the physics engine
extrapolates the lines.

---------------- --------------- ------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------
Graveyard Hits   **graveyard**   3.0x          The backend identifies blocks of dead code. The physics engine assumes an average of 3 lines of ghost logic per block hit to estimate the total necrotic mass.
Total LOC        **total_loc**   Denominator   We measure density against the absolute size of the file, not just the active logic.
---------------- --------------- ------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------

## 2.2.N.C. The Universal Framework Integration

-   *Fc*** (Fidelity Coefficient):** **Not Applied.** Dead code is
language-agnostic.

-   *Irc*** (Implicit Risk Correction):** **Not Applied.**

-   *Mp*** (Path Modifier):** **Applied to Threshold.**

-   *Experiments/Scratch (Mp = 2.0):* **High Tolerance.** It is
acceptable to keep snippets while prototyping.
-   *Core/Kernel (Mp = 0.5):* **Zero Tolerance.** Production
architecture must be clean.
-   *Legacy (Mp = 1.5):* **Moderate Tolerance.** We expect some rot
in the archives.

## 2.2.N.D. The Equation: The Necrosis Sigmoid

*We calculate the density of dead code and map it to a curve that
forgives minor \"scraps\" but punishes \"hoarding.\"*

**Step A: The Clean File Bypass** If there are zero graveyard hits, the
engine immediately returns a *0.0* risk score to save processing time.

**Step B: Calculate Necrosis Density** We estimate the total
*ghost_lines* by multiplying the graveyard hits by *3.0*. We then divide
this by the file\'s *total_loc*.

-   **The Safe Mass Floor:** To prevent a 5-line script with a single
commented-out line from instantly registering as 60% necrotic, we
enforce a minimum file mass of *50.0* lines for the density
calculation.

**Step C: Determine The Tolerance (Dynamic Threshold)** This is the
\"Tipping Point\" where the file is considered \"Haunted.\"

-   **Base:** *10.0* (We tolerate up to 10% dead code before the score
spikes).
-   **Context Scaling:** The threshold is divided by the Path Modifier
(*Mp*). Therefore, if a file is in the *core/* (high *Mp* punishing
risk), the tolerance threshold drops. If it is in *experiments/*
(low *Mp* forgiving risk), the tolerance threshold rises.

**Step D: The Sigmoid Map** We map density against the threshold using a
slope of *0.3*, which creates a smooth transition from \"Clean\" to
\"Haunted\".

## 2.2.N.E. Implementation (Python Reference)

*import math*

*from typing import Dict*

*def \_calc_graveyard(self, total_loc: float, eq: Dict\[str, int\], mp:
float) -\> float:*

* \# Step A: Clean File Bypass*

* hits = eq.get(\"graveyard\", 0)*

* if hits == 0:*

* return 0.0*

* *

* t = self.risk_tuning.get(\"graveyard\", {})*

* *

* \# Step B: Calculate Necrosis Density*

* ghost_lines = hits \* t.get(\"hit_mult\", 3.0)*

* \# Safe Mass Floor prevents micro-files from exploding in density*

* density = (ghost_lines / max(total_loc, t.get(\"safe_mass_floor\",
50.0))) \* 100.0*

* *

* \# Step C: Dynamic Threshold *

* threshold = t.get(\"threshold_base\", 10.0) / max(mp, 0.1) *

* *

* \# Step D: Sigmoid Map*

* try:*

* score = 100.0 / (1.0 + math.exp(-t.get(\"sigmoid_slope\", 0.3) \*
(density - threshold)))*

* except OverflowError:*

* score = 100.0 if density \> threshold else 0.0*

* *

* return min(score, 100.0)*

## 2.2.N.F. Visual Verification (\"The Truth\")

**Comparison: 200 Line File**

--------------- ------ ----- ---------------- -------- ------------ ----------------------- --------------------------------------------------------------------
Clean Core      0      0%    Core (1.2)       \~8.3%   **0.0**      CLEAN (Blue)            Pure life. No dead code found.
Standard Dev    \~10   5%    Standard (1.0)   10.0%    **\~18.0**   CLEAN (Blue)            Minor scraps. Fully tolerated beneath the threshold.
Haunted Core    \~20   10%   Core (1.2)       \~8.3%   **\~62.0**   HIGH (Orange)           10% is tolerated elsewhere, but \"Haunted\" in a strict core path.
The Hoarder     \~40   20%   Standard (1.0)   10.0%    **\~95.0**   GRAVEYARD (Red)         20% dead code is clearly necrotic.
The Prototype   \~40   20%   Exp (0.5)        20.0%    **50.0**     INTERMEDIATE (Yellow)   High necrosis, but the experimental context safely allows it.
--------------- ------ ----- ---------------- -------- ------------ ----------------------- --------------------------------------------------------------------


