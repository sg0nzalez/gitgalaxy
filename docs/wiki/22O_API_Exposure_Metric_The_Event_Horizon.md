#### 2.2.O. API Exposure (Metric: The Event Horizon)

##### 2.2.O.A. The Philosophy: The Event Horizon

****Visualizes \"The Surface Area of Logic.\" Every module has an Event
Horizon: the boundary between its internal mechanics and the outside
world. API Exposure measures how permeable this boundary is. This metric
allows developers to instantly distinguish heavily exposed interfaces
from internal utility code.****

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **VERY LOW (Score 0-20, Blue):** Internal Vault. The logic is
encapsulated. It exists to support other code but does not offer a
public face.
-   **MODERATE (Score 41-60, Yellow):** Standard exposure. A healthy mix
of public and private methods.
-   **VERY HIGH (Score 81-100, Red):** Public Quasar. The module exists
primarily to be consumed by others. It broadcasts a massive volume
of functionality to the galaxy.

##### 2.2.O.B. The Inputs (Surface Detection)

We compare the count of **Public Signatures** against the **Total
Definitions** to calculate the ratio of exposure. We explicitly sum
Functions and Classes to get the total \"Entity Count.\"

----------------------- ------------------------------ ----------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Input Variable          Regex Key                      Weight            Rationale
**ApiHits**             *api*                          **Numerator**     **The Broadcast.** Keywords that explicitly expose logic: *export*, *public*, *module.exports*, or capitalization rules (Go/Python).
**TotalDeclarations**   *func_start* + *class_start*   **Denominator**   **The Mass.** The total count of logical units (Functions + Classes). We need to sum both regex hits to ensure we don\'t undercount files that define many classes/structs but few methods.
----------------------- ------------------------------ ----------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##### 2.2.O.C. The Universal Framework Integration

-   *Fc*** (Fidelity Coefficient):** **Not Applied.** Public is public.

-   *Irc*** (Implicit Risk Correction):** **Not Applied.** The concept
of \"Public Ratio\" is language-agnostic.

-   *Mp*** (Path Modifier):** **Applied to Score (Amplifier).**

-   *API/Public (Mp = 1.2):* **Amplify.** We want these files to
shine brighter. They are the intended entry points.
-   *Internal/Private (Mp = 0.8):* **Dampen.** We want these to
remain background noise unless they are egregiously leaking.

##### 2.2.O.D. The Equation: Linear Surface Density

We calculate a compound score that balances the direct percentage of
public logic (Ratio) with the sheer quantity of exposed endpoints
(Volume).

**Step A: The Encapsulation Bypass** If the file has zero *api* hits, it
is perfectly encapsulated. The engine returns *0.0* immediately.

**Step B: Calculate Exposure Ratio (40% Weight)** We determine what
percentage of the file\'s defined logic is accessible from the outside
(*api_hits / total_entities*). We clamp the ratio to *1.0* to handle
rare edge cases where heuristics might over-count exports.

**Step C: Calculate Logarithmic Volume (60% Weight)** A file exposing
100 endpoints is structurally more impactful than a file exposing 1
endpoint. We calculate *log10(api_hits + 1)* divided by a dampening
divisor (*1.5*) to curve the volume impact, clamping it at *1.0*.

**Step D: Compound Score & Context Adjustment** We blend the Ratio and
Volume using their respective weights (*0.4* and *0.6*), scale to
*100.0*, and apply the Path Modifier (*Mp*) to highlight intended APIs
and dampen internal utilities.

##### 2.2.O.E. Implementation (Python Reference)

*import math*

*from typing import Dict*

*def \_calc_api_exposure(self, eq: Dict\[str, int\], mp: float) -\>
float:*

* \# Step A: Encapsulation Bypass*

* api_hits = eq.get(\"api\", 0)*

* if api_hits == 0:*

* return 0.0*

* *

* t = self.risk_tuning.get(\"api_exposure\", {})*

* entities = max(eq.get(\"func_start\", 0) + eq.get(\"class_start\", 0),
1)*

* *

* \# Step B: Exposure Ratio*

* ratio = min(api_hits / float(entities), 1.0)*

* *

* \# Step C: Logarithmic Volume*

* volume_weight = min(math.log10(api_hits + 1) / t.get(\"log_divisor\",
1.5), 1.0)*

* *

* \# Step D: Compound Score & Modifier*

* raw_score = ((ratio \* t.get(\"ratio_weight\", 0.4)) + (volume_weight
\* t.get(\"volume_weight\", 0.6))) \* 100.0*

* *

* return min(raw_score \* mp, 100.0)*

##### 2.2.O.F. Visual Verification (\"The Truth\")

**Comparison: 20 Entity File (Functions + Classes)**

---------------- ---- ------ ---------------- ---------- ------------------- -------------------------------------------------------------------------------------------------
The Utility      2    10%    Internal (0.8)   **\~18**   VERY LOW (Blue)     Mostly private helpers. Correctly dim.
The Leaky Core   8    40%    Internal (0.8)   **\~43**   MODERATE (Yellow)   Moderate exposure in an internal folder. Visible, but dampened because it shouldn\'t be public.
The Interface    10   50%    API (1.2)        **\~74**   HIGH (Orange)       Half the file is public. Amplified heavily because it is a designated entry point.
The Library      20   100%   Standard (1.0)   **\~93**   VERY HIGH (Red)     Pure public interface broadcasting maximum volume.
---------------- ---- ------ ---------------- ---------- ------------------- -------------------------------------------------------------------------------------------------

****
