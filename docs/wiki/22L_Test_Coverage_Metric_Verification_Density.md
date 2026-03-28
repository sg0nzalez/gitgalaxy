#### 2.2.L. Test Coverage (Metric: Verification Density)

##### 2.2.L.A. The Philosophy: Trust vs. Verification

****Visualizes the \"Security Blanket\" of the codebase. In GitGalaxy,
we distinguish between Defensive Code (handling errors at runtime) and
Verified Code (proving correctness at design time). Because this metric
has been unified into the Risk Exposure model, a high score now
indicates a *****lack***** of verification (high risk), while a low
score indicates ironclad, verified code.****

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **IRONCLAD (Score 15-20, Blue):** Fortified. The code is heavily
backed by internal assertions, mocks, or a dedicated sibling test
suite. *(Note: The physics engine enforces a hard minimum floor of
15.0, acknowledging that no code is 100% perfectly safe).*
-   **MODERATE (Score 41-60, Yellow):** Partial verification. Meets the
bare minimum threshold.
-   **VERY HIGH (Score 81-100, Red):** Speculative. The code might work,
but there is no programmatic proof. It relies entirely on hope.

##### 2.2.L.B. The Inputs (Verification Signals)

We combine internal evidence (assertions) with external evidence
(sibling files). The file system checks are now abstracted, passing an
*is_protected* boolean directly to the physics engine.

---------------- ------------------ -------------- -------------------------------------------------------------------------------------------------------------------------------------------
Internal Tests   **test**           5.0x           Assertions, mocks, and test definitions inside the file itself.
Sibling Match    **is_protected**   +30.0 (Flat)   External Coverage. Indicates a **X.test.js** or **X_spec.rb** exists next to **X.js**. This flat density bonus represents strong intent.
Mass Penalty     **loc \> 300**     Variable       Monoliths (files over 300 lines) gain a stacking risk penalty up to +40. Massive files cannot be adequately verified by unit tests alone.
---------------- ------------------ -------------- -------------------------------------------------------------------------------------------------------------------------------------------

##### 2.2.L.C. The Universal Framework Integration

**Exemptions:** Untestable files (e.g., Markdown, Makefiles, CMake, or
specific extensions configured in the asset masks) bypass the engine
entirely, returning *0.0* risk.

-   **Fc (Fidelity Coefficient):** Applied as an inverted multiplier
(*2.0 - Fc*). We trust explicit verification in high-fidelity
languages more than loose assertions in implicit languages.

```{=html}
<!-- -->
```
-   **Irc (Implicit Risk Correction):** Added to the Threshold. Implicit
languages (Python, Ruby) rely entirely on tests for type safety,
meaning they require a *higher* density of tests to clear the risk
bar.

```{=html}
<!-- -->
```
-   **Mp (Path Modifier):** Scales the Threshold. Critical
infrastructure (*core/*) gets a higher bar; notoriously hard-to-test
views (*UI/*) get a lower bar.

##### 2.2.L.D. The Equation: The Verification Sigmoid

**Step A: The Exemption Bypass** If the file matches known untestable
patterns (e.g., *readme*, *makefile*), the engine immediately returns
*0.0*.

**Step B: Calculate Verification Density** We calculate the density of
internal tests (*test hits \* 5.0 / LOC*) and add the flat Sibling Bonus
(*+30.0*). The bonus is added directly to density because the existence
of a test file implies coverage of the whole module.

**Step C: Determine The Bar (Dynamic Threshold)** This is the \"Passing
Grade\" the density must overcome to lower the risk score. *Threshold =
(15.0 + (Irc \* 3.0)) \* Mp*.

**Step D: The Inverse Sigmoid Map** We map density against the dynamic
threshold using a positive exponent. As Verification Density
*increases*, the Risk Exposure mathematically *decreases*.

**Step E: Trust Adjustment & Mass Penalty** We multiply the result by
the inverted Fidelity score (*2.0 - Fc*). If the file size exceeds the
*MASSIVE_FILE_THRESHOLD* (300 lines), we calculate and add a structural
mass penalty, capping the final calculation between the *15.0* risk
floor and *100.0* maximum.

##### 2.2.L.E. Implementation (Python Reference)

*import math*

*import os*

*from typing import Dict*

*def \_calc_verification(self, loc: int, file_path: str, is_protected:
bool, eq: Dict\[str, int\], irc: int, fc: float, mp: float,
umbrella_bonus: float = 0.0) -\> float:*

* filename = os.path.basename(file_path).lower()*

* ext = filename.split(\'.\')\[-1\] if \'.\' in filename else \"\"*

* *

* exempt_exts = self.asset_masks.get(\"UNTESTABLE_EXTENSIONS\", set())*

* exempt_names = self.asset_masks.get(\"UNTESTABLE_NAMES\", set())*

* *

* \# Step A: Untestable Bypass*

* if ext in exempt_exts or filename in exempt_names or
filename.startswith(\'readme\') or \'makefile\' in filename or \'cmake\'
in filename:*

* return 0.0*

* t = self.risk_tuning.get(\"verification\", {})*

* safe_loc = max(loc, 1)*

* *

* \# Step B: Verification Density*

* sibling_bonus = t.get(\"sibling_bonus\", 30.0) if is_protected else
0.0*

* internal_density = (eq.get(\"test\", 0) \*
t.get(\"internal_test_mult\", 5.0) / safe_loc) \* 100.0*

* total_density = internal_density + sibling_bonus *

* *

* \# Step C: Dynamic Threshold*

* threshold = (t.get(\"threshold_base\", 15.0) + (irc \*
t.get(\"irc_mult\", 3.0))) \* mp*

* *

* \# Step D: Inverse Sigmoid Map*

* try:*

* raw_exposure = 100.0 / (1.0 + math.exp(t.get(\"sigmoid_slope\", 0.25)
\* (total_density - threshold)))*

* except OverflowError:*

* raw_exposure = 0.0 if total_density \> threshold else 100.0*

* *

* \# Step E: Trust Adjustment*

* final_exposure = raw_exposure \* (2.0 - fc)*

* \# Step F: The Mass Penalty*

* if safe_loc \> self.MASSIVE_FILE_THRESHOLD:*

* mass_penalty = min((safe_loc - self.MASSIVE_FILE_THRESHOLD) /
t.get(\"mass_penalty_div\", 20.0), t.get(\"mass_penalty_max\", 40.0)) *

* final_exposure += mass_penalty*

* \# Enforce the 15.0 Risk Floor*

* return min(max(final_exposure, t.get(\"risk_floor\", 15.0)), 100.0)*

* *

##### 2.2.L.F. Visual Verification (\"The Truth\")

**Comparison: 100 Line File (Base Threshold 15)**

**

---------------- --------------------- --------------- ------------ ------------------- ----------------------------------------------------------------------------------------------------------------------------------------------
The Test File    20 internal asserts   N/A             **15.0**     IRONCLAD (Blue)     High internal density drops exposure to the absolute risk floor.
Paired Source    0 asserts             Yes             **\~15.0**   IRONCLAD (Blue)     Covered by sibling. The flat +30 density bonus clears the threshold easily.
Defensive Code   3 asserts             No              **\~50.0**   MODERATE (Yellow)   Internal checks meet the bare minimum threshold.
The Orphan       0 asserts             No              **100.0**    VERY HIGH (Red)     Unverified. No internal checks, no sibling coverage.
The Monolith     0 asserts             Yes (Sibling)   **\~45.0**   MODERATE (Yellow)   A 900-line file *with* a sibling test. The mass penalty overrides the sibling bonus, preventing massive files from hiding behind thin tests.
---------------- --------------------- --------------- ------------ ------------------- ----------------------------------------------------------------------------------------------------------------------------------------------

**
