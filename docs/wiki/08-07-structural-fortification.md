# Structural Fortification (Safety Exposure)

> **Metric: Ratio of Defensive Structures to Execution Risks**
>
> **Summary:** Visualizes the "Load-Bearing Capacity" of the code within the knowledge graph. We treat code like physical infrastructure. A bridge is safe not because it has no cars (complexity), but because it has enough support pillars (guardrails) to hold the traffic.
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.
> * 🟦 **VERY LOW (Score 0-19):** Fortified. Defensive structures (`try/catch`, guards) vastly outnumber the risks.
> * 🟨 **INTERMEDIATE (Score 40-59):** Stable. Risks and defenses are roughly balanced.
> * 🟥 **VERY HIGH (Score 80-100):** Fragile. The structural load (Risk) exceeds the support capacity (Defenses). The code is liable to collapse under edge cases.

## The Inputs (Attackers vs. Defenders)

We classify heuristics into **Attackers** (Risk) and **Defenders** (Safety), assigning a specific structural weight to each based on their impact.

| Variable | Target Syntax | Weight | Classification | Structural Role |
| :--- | :--- | :--- | :--- | :--- |
| `danger_hits` | `eval`, `exec` | 4.0x | **Attacker** | **The Heavy Load.** Critical vulnerabilities that exert massive stress. |
| `safety_neg_hits` | `any`, `@ts-ignore` | 1.5x | **Attacker** | **The Rust.** Anti-patterns that weaken the type system or structure. |
| `flux_hits` | Mutated variables | 0.5x | **Attacker** | **The Vibration.** Mutable state introduces ongoing entropy. |
| `safety_hits` | `try/catch`, guards | 1.0x | **Defender** | **The Pillars.** Explicit runtime protection and boundary management. |
| `test_hits` | `describe`, `assert` | 0.5x | **Defender** | **The Blueprint.** Proximity to tests implies verification. |
| `doc_hits` | JSDoc, comments | 0.1x | **Defender** | **The Warning Labels.** Provides a minor structural defense bonus. |

## Universal Framework Integration

* **$Fc$ (Fidelity Coefficient):** Applied to **Defenders**. We trust a `try/catch` in Java (Explicit) more than a check in Shell (Implicit).
* **$Irc$ (Implicit Risk Correction):** Added to **Attackers**. Implicit languages start with a "Phantom Load"—a baseline risk inherent to the medium.
* **$Mp$ (Path Modifier):** Applied to **Attackers**. We keep the discount small to ensure risks are exposed everywhere.
  * *Experiments/Tests ($Mp = 0.9$):* **Minor Discount.** Risks are slightly forgiven, but unsafe code will still flash Red.
  * *Core/Auth ($Mp = 1.2$):* **Amplified.** Risks are punished heavily. Fragility here is unacceptable.

## The Equation: The Structural Integrity Sigmoid

We calculate **Net Exposure** rather than Integrity Density, utilizing Laplace Smoothing to prevent tiny files from aggressively skewing the spectrum.

**Step A: Zero-Risk Bypass**
If the weighted sum of all Attackers equals exactly `0`, the calculation short-circuits and immediately returns a score of `0.0`. If there is no structural load, the file is perfectly fortified by default.

**Step B: Calculate Smoothed Attack & Defense Densities**
We sum the weighted risks and fortifications. Instead of dividing strictly by LOC, we use **Laplace Smoothing** ($LOC + 20.0$). This prevents a 5-line file with a single `try/catch` from registering as infinitely safe.

$$SmoothedLOC=\max(LOC, 1)+20.0$$
$$AttackDensity=\left(\frac{WeightedAttackers+Irc}{SmoothedLOC}\right)\times Mp$$
$$DefenseDensity=\left(\frac{WeightedDefenders}{SmoothedLOC}\right)\times Fc$$

**Step C: Calculate Net Exposure**
We subtract defense from attack. We also subtract a minor `SystemsBuffer` for implicit languages ($Fc < 1.0$) to account for their naturally looser structures.
* **Positive Exposure:** Risks outweigh Defenses (Fragile / Red).
* **Negative Exposure:** Defenses outweigh Risks (Fortified / Blue).

$$NetExposure=(AttackDensity-DefenseDensity)-SystemsBuffer$$

**Step D: The Sigmoid Score & Breach Floor**
We map the exposure to a $0-100$ scale using a steep Sigmoid slope ($12.0$). 

$$Score=\frac{100}{1+e^{-12.0\times NetExposure}}$$

If the code has a high density of explicit `danger` or `safety_neg` hits (evaluated against the raw $LOC$, bypassing the Laplace smoother) and Attack outpaces Defense, the file is subject to a hard **Breach Floor** (scaling up to a maximum of $80.0$). This mathematically guarantees that catastrophic structural weaknesses cannot be masked by simply adding empty `try/catch` blocks.

## Implementation (Python Reference)

```python
import math
from typing import Dict

def _calc_safety(self, loc: int, eq: Dict[str, int], irc: int, fc: float, mp: float) -> float:
    safe_loc = max(loc, 1)
    t = self.risk_tuning.get("safety", {})

    # 1. Weighted Sums
    attack_hits = (eq.get("danger", 0) * t.get("danger_weight", 4.0)) + \
                  (eq.get("safety_neg", 0) * t.get("safety_neg_weight", 1.5)) + \
                  (eq.get("flux", 0) * t.get("flux_weight", 0.5))

    defense_hits = (eq.get("safety", 0) * self.WEIGHT_DEFENSE) + \
                   (eq.get("test", 0) * t.get("test_weight", 0.5)) + \
                   (eq.get("doc", 0) * t.get("doc_weight", 0.1))

    # Zero-Risk Bypass
    if attack_hits == 0:
        return 0.0

    # 2. Laplace Smoothing (+20 LOC) to prevent tiny-file explosions
    smoothed_loc = safe_loc + t.get("laplace_smoothing", 20.0)

    attack = ((attack_hits + irc) / smoothed_loc) * mp
    defense = (defense_hits / smoothed_loc) * fc

    # 3. Net Exposure Calculation
    systems_buffer = t.get("systems_buffer", 0.25) if fc < 1.0 else 0.0
    net_exposure = (attack - defense) - systems_buffer

    # 4. Sigmoid Mapping
    try:
        score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 12.0) * net_exposure))
    except OverflowError:
        score = 100.0 if net_exposure > 0 else 0.0

    # 5. The Breach Floor (Punishing undefended danger)
    # Note: Evaluated against true safe_loc to ensure pure density mapping
    danger_density = (eq.get("danger", 0) + eq.get("safety_neg", 0)) / safe_loc
    
    if danger_density > t.get("breach_density_min", 0.03) and attack > defense:
        floor = min(t.get("breach_floor_max", 80.0), 30.0 + (danger_density * t.get("breach_floor_mult", 500.0)))
        score = max(score, floor)

    return max(score, 0.0)

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
