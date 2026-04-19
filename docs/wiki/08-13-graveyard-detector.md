# Graveyard Exposure (Dead Code)

> **Metric: Architectural Transparency (The Fear of Deletion)**
>
> **Summary:** Visualizes "Code Necrosis" or "The Fear of Deletion" within the knowledge graph. Commented-out code ("Ghost Logic") is not documentation; it is hesitation. It implies a lack of trust in Version Control. It creates cognitive noise, forcing the reader to mentally parse and discard logic that is no longer active.
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.
> * 🟦 **CLEAN (Score 0-19):** Active, clean, executed. Pure life. No dead code found.
> * 🟨 **INTERMEDIATE (Score 40-59):** Minor scraps. Tolerable depending on the context.
> * 🟥 **GRAVEYARD (Score 80-100):** Heavily polluted with dead blocks. The file is "Haunted" by its past.

## The Inputs (Heuristic Detection)

We distinguish between Documentation (English text) and Graveyards (Inactive Code) by scanning for syntax density within comment blocks. The deterministic engine calculates the raw blocks, and the signal processor extrapolates the lines.

| Variable | Weight/Role | Structural Definition |
| :--- | :--- | :--- |
| `graveyard_hits` | 3.0x | The deterministic engine identifies blocks of dead code. The signal processor assumes an average of 3 lines of ghost logic per block hit to estimate the total necrotic mass. |
| `total_loc` | Denominator | We measure density against the absolute physical size of the file, not just the active logic. |

## Universal Framework Integration

* **$Fc$ (Fidelity Coefficient):** **Not Applied.** Dead code is language-agnostic.
* **$Irc$ (Implicit Risk Correction):** **Not Applied.**
* **$Mp$ (Path Modifier):** **Applied to Threshold.**
  * *Experiments/Scratch ($Mp = 2.0$):* **High Tolerance.** It is acceptable to keep snippets while prototyping. (Note: A higher modifier here *lowers* the threshold penalty in the math).
  * *Legacy ($Mp = 1.5$):* **Moderate Tolerance.** We expect some rot in the archives.
  * *Core/Kernel ($Mp = 0.5$):* **Zero Tolerance.** Production architecture must be strictly clean.

## The Equation: The Necrosis Sigmoid

We calculate the density of dead code and map it to a curve that forgives minor "scraps" but punishes "hoarding."

**Step A: The Clean File Bypass**
If there are zero graveyard hits, the engine immediately returns a $0.0$ risk score to save processing time.

**Step B: Calculate Necrosis Density**
We estimate the total `ghost_lines` by multiplying the graveyard hits by $3.0$. We then divide this by the file's `total_loc`. To prevent a 5-line script with a single commented-out line from instantly registering as highly necrotic, we enforce a minimum file mass floor of $50.0$ lines.

$$GhostLines = graveyard\_hits \times 3.0$$
$$Density = \left( \frac{GhostLines}{\max(TotalLOC, 50.0)} \right) \times 100.0$$

**Step C: Determine The Tolerance (Dynamic Threshold)**
This is the "Tipping Point" where the file is considered "Haunted." We start with a base tolerance of $10.0$ (we tolerate up to 10% dead code before the score spikes). The threshold is then divided by the Path Modifier ($Mp$). If a file is in `core/` (low $Mp$), the tolerance threshold drops. If it is in `experiments/` (high $Mp$), the tolerance threshold rises.

$$Threshold = \frac{10.0}{\max(Mp, 0.1)}$$

**Step D: The Sigmoid Map**
We map density against the threshold using a slope of $0.3$, which creates a smooth transition from "Clean" to "Haunted".

$$Score = \frac{100.0}{1 + e^{-0.3 \times (Density - Threshold)}}$$

## Implementation (Python Reference)

```python
import math
from typing import Dict

def _calc_graveyard(self, total_loc: float, eq: Dict[str, int], mp: float) -> float:
    # Step A: Clean File Bypass
    hits = eq.get("graveyard", 0)
    if hits == 0:
        return 0.0
        
    t = self.risk_tuning.get("graveyard", {})
    
    # Step B: Calculate Necrosis Density
    ghost_lines = hits * t.get("hit_mult", 3.0)
    
    # Safe Mass Floor prevents micro-files from exploding in density
    density = (ghost_lines / max(total_loc, t.get("safe_mass_floor", 50.0))) * 100.0
    
    # Step C: Dynamic Threshold 
    threshold = t.get("threshold_base", 10.0) / max(mp, 0.1) 
    
    # Step D: Sigmoid Map
    try:
        score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 0.3) * (density - threshold)))
    except OverflowError:
        score = 100.0 if density > threshold else 0.0
        
    return min(score, 100.0)

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

