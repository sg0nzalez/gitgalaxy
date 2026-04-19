# State Flux Exposure

> **Metric: Data Volatility (Density of Mutation)**
>
> **Summary:** Visualizes "Data Volatility" within the knowledge graph. State Flux measures the Density of Mutation. It answers the question: "How stable is the data in this file?" The "Tiger in the Cage" rule applies: we do not dampen the signal for state management folders (`store/`, `reducers/`). A file dedicated to mutating state is a high-flux file and should glow red/orange to reflect its true nature as a volatility engine.
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.
> * 🟦 **VERY LOW (Score 0-19):** Frozen. Variables are defined once and rarely changed. The logic is predictable and referentially transparent.
> * 🟨 **MODERATE (Score 40-59):** Warming. Standard levels of local state management and loop counters.
> * 🟥 **VERY HIGH (Score 80-100):** Boiling. Variables are constantly reassigned, properties are updated, and side effects are triggered. The data state is in constant flux, making it difficult to track "who changed what and when."

## The Inputs (Mutation Heuristics)

We count the heuristics that imply reassignment or side effects. The deterministic engine pre-calculates these and passes them to the Signal Processor.

| Variable | Weight | Structural Definition |
| :--- | :--- | :--- |
| `flux_hits` | 1.0x | **The Change.** Keywords that mutate data: `let`, `var`, `mut`, `setState`, `push`, `pop`, `+=`, `=`. |
| `loc` | Denominator | We measure density. A loop counter `i++` in a 1,000-line file is negligible. 50 setters in a 100-line file is a "Boiling" class. |

## Universal Framework Integration

* **$Fc$ (Fidelity Coefficient):** **Not Applied.** Mutation is an absolute action.
* **$Irc$ (Implicit Risk Correction):** **Applied to Numerator (Dampened).** Implicit languages (JS, Python) default to mutability. We add a small "Ghost Load" ($Irc \times 0.15$) to the density. This acts as a tie-breaker, pushing implicit code slightly higher on the volatility scale than explicit immutable languages for the exact same operation count.
* **$Mp$ (Path Modifier):** **Applied to the Threshold.**
  * *UI/Views ($Mp = 0.8$):* **Low Tolerance.** Heavy internal state mutation in UI components (`setState` spaghetti) is a prime source of bugs. We lower the bar to highlight this risk.
  * *Standard/Store ($Mp = 1.0$):* **Standard Tolerance.** We accept that Stores exist to mutate data. We let them show their true colors without artificial dampening.

## The Equation: The Mutation Threshold Sigmoid

Most code requires some local mutation (e.g., loop counters). We use a Sigmoid curve to ignore this background noise but react sharply once mutation becomes a structural pattern.

**Step A: Pre-Filter (The Zero Check)**
If the file contains zero `flux` hits, the score is $0.0$.

**Step B: Calculate Volatility Density**
We determine what percentage of the code involves changing data, adding the dampened $Irc$ penalty.

$$Density = \left( \frac{flux\_hits + (Irc \times 0.15)}{\max(LOC, 1)} \right) \times 100.0$$

**Step C: Determine The Threshold (The Boiling Point)**
This is the density required to "Boil" the file. We start with a base of $15.0$ (15% density), which safely absorbs standard loops and local variables before triggering warnings. We then scale it by $Mp$. (e.g., If $Mp$ is $0.8$ for UI, the threshold drops to $12.0\%$).

$$Threshold = 15.0 \times Mp$$

**Step D: The Sigmoid Map**
We map density against the threshold using a relaxed slope ($0.20$), creating a smooth curve that ramps up as mutation becomes dominant.

$$Score = \frac{100.0}{1 + e^{-0.20 \times (Density - Threshold)}}$$

## Implementation (Python Reference)

```python
import math
from typing import Dict

def _calc_state_flux(self, loc: int, eq: Dict[str, int], irc: int, mp: float) -> float:
    # Step A: Pre-Filter
    hits = eq.get("flux", 0)
    if hits == 0: 
        return 0.0

    t = self.risk_tuning.get("state_flux", {})

    # Step B: Volatility Density (with 0.15 IRC dampener)
    density = ((hits + (irc * t.get("irc_mult", 0.15))) / max(loc, 1)) * 100.0

    # Step C: Dynamic Threshold
    threshold = t.get("threshold_base", 15.0) * mp

    # Step D: Sigmoid Map
    try:
        score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 0.20) * (density - threshold)))
    except OverflowError:
        score = 100.0 if density > threshold else 0.0

    return min(score, 100.0)

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

