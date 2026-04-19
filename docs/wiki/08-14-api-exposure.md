# API Exposure

> **Metric: The Surface Area of Logic (Public Endpoints vs. Total Entities)**
>
> **Summary:** Visualizes "The Event Horizon" within the knowledge graph. Every module has an Event Horizon: the boundary between its internal mechanics and the outside world. API Exposure measures how permeable this boundary is. This metric allows developers to instantly distinguish heavily exposed interfaces from internal utility code.
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.
> * 🟦 **VERY LOW (Score 0-19):** Internal Vault. The logic is encapsulated. It exists to support other code but does not offer a public face.
> * 🟨 **MODERATE (Score 40-59):** Standard exposure. A healthy mix of public and private methods.
> * 🟥 **VERY HIGH (Score 80-100):** Public Quasar. The module exists primarily to be consumed by others. It broadcasts a massive volume of functionality to the galaxy.

## The Inputs (Surface Detection)

We compare the count of **Public Signatures** against the **Total Definitions** to calculate the ratio of exposure. We explicitly sum Functions and Classes to get the total "Entity Count."

| Variable | Regex Key | Weight | Structural Definition |
| :--- | :--- | :--- | :--- |
| `ApiHits` | `api` | **Numerator** | **The Broadcast.** Keywords that explicitly expose logic: `export`, `public`, `module.exports`, or capitalization rules (Go/Python). |
| `TotalDeclarations` | `func_start` + `class_start` | **Denominator** | **The Mass.** The total count of logical units (Functions + Classes). We sum both to ensure we don't undercount files that define many classes/structs but few methods. |

## Universal Framework Integration

* **$Fc$ (Fidelity Coefficient):** **Not Applied.** Public is public.
* **$Irc$ (Implicit Risk Correction):** **Not Applied.** The concept of "Public Ratio" is language-agnostic.
* **$Mp$ (Path Modifier):** **Applied to Score (Amplifier).**
  * *API/Public ($Mp = 1.2$):* **Amplify.** We want these files to shine brighter. They are the intended entry points.
  * *Internal/Private ($Mp = 0.8$):* **Dampen.** We want these to remain background noise unless they are egregiously leaking.

## The Equation: Linear Surface Density

We calculate a compound score that balances the direct percentage of public logic (Ratio) with the sheer quantity of exposed endpoints (Volume).

**Step A: The Encapsulation Bypass**
If the file has zero `api` hits, it is perfectly encapsulated. The engine returns $0.0$ immediately.

**Step B: Calculate Exposure Ratio (40% Weight)**
We determine what percentage of the file's defined logic is accessible from the outside. We clamp the ratio to $1.0$ to handle rare edge cases where heuristics might over-count exports.

$$Entities = \max(func\_start + class\_start, 1)$$
$$Ratio = \min\left( \frac{api\_hits}{Entities}, 1.0 \right)$$

**Step C: Calculate Logarithmic Volume (60% Weight)**
A file exposing 100 endpoints is structurally more impactful than a file exposing 1 endpoint. We calculate $\log_{10}(api\_hits + 1)$ divided by a dampening divisor ($1.5$) to curve the volume impact, clamping it at $1.0$.

$$VolumeWeight = \min\left( \frac{\log_{10}(api\_hits + 1)}{1.5}, 1.0 \right)$$

**Step D: Compound Score & Context Adjustment**
We blend the Ratio and Volume using their respective weights ($0.4$ and $0.6$), scale to $100.0$, and apply the Path Modifier ($Mp$) to highlight intended APIs and dampen internal utilities.

$$RawScore = \left( (Ratio \times 0.4) + (VolumeWeight \times 0.6) \right) \times 100.0$$
$$FinalScore = \min(RawScore \times Mp, 100.0)$$

## Implementation (Python Reference)

```python
import math
from typing import Dict

def _calc_api_exposure(self, eq: Dict[str, int], mp: float) -> float:
    # Step A: Encapsulation Bypass
    api_hits = eq.get("api", 0)
    if api_hits == 0:
        return 0.0

    t = self.risk_tuning.get("api_exposure", {})
    entities = max(eq.get("func_start", 0) + eq.get("class_start", 0), 1)

    # Step B: Exposure Ratio
    ratio = min(api_hits / float(entities), 1.0)

    # Step C: Logarithmic Volume
    volume_weight = min(math.log10(api_hits + 1) / t.get("log_divisor", 1.5), 1.0)

    # Step D: Compound Score & Modifier
    raw_score = ((ratio * t.get("ratio_weight", 0.4)) + (volume_weight * t.get("volume_weight", 0.6))) * 100.0

    return min(raw_score * mp, 100.0)

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

