# 2.2.G. Structural Fortification (Safety Exposure)

> **Metric: Ratio of Defensive Structures to Execution Risks**
>
> **Summary:** Visualizes the "Load-Bearing Capacity" of the code. We treat code like physical infrastructure. A bridge is safe not because it has no cars (complexity), but because it has enough support pillars (guardrails) to hold the traffic.
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.
> * 🟦 **VERY LOW (Score 0-19):** Fortified. Defensive structures (`try/catch`, guards) vastly outnumber the risks.
> * 🟨 **INTERMEDIATE (Score 40-59):** Stable. Risks and defenses are roughly balanced.
> * 🟥 **VERY HIGH (Score 80-100):** Fragile. The structural load (Risk) exceeds the support capacity (Defenses). The code is liable to collapse under edge cases.

## 2.2.G.1. The Inputs (Attackers vs. Defenders)

We classify regex patterns into **Attackers** (Risk) and **Defenders** (Safety), assigning a specific structural weight to each.

| Variable | Target Syntax | Weight | Classification | Structural Role |
| :--- | :--- | :--- | :--- | :--- |
| `danger_hits` | `eval`, `exec` | 4.0x | **Attacker** | **The Heavy Load.** Critical vulnerabilities that exert massive stress. |
| `safety_neg_hits` | `any`, `@ts-ignore` | 1.5x | **Attacker** | **The Rust.** Anti-patterns that weaken the type system or structure. |
| `flux_hits` | Mutated variables | 0.5x | **Attacker** | **The Vibration.** Mutable state introduces ongoing entropy. |
| `safety_hits` | `try/catch`, guards | 1.0x | **Defender** | **The Pillars.** Explicit runtime protection and boundary management. |
| `test_hits` | `describe`, `assert` | 0.5x | **Defender** | **The Blueprint.** Proximity to tests implies verification. |
| `doc_hits` | JSDoc, comments | 0.1x | **Defender** | **The Warning Labels.** Provides a minor structural defense bonus. |

## 2.2.G.2. The Universal Framework Integration

* **$\text{Fc}$ (Fidelity Coefficient):** Applied to **Defenders**. We trust a `try/catch` in Java (Explicit) more than a check in Shell (Implicit).
* **$\text{Irc}$ (Implicit Risk Correction):** Added to **Attackers**. Implicit languages start with a "Phantom Load"—a baseline risk inherent to the medium.
* **$\text{Mp}$ (Path Modifier):** Applied to **Attackers**. We keep the discount small to ensure risks are exposed everywhere.
  * *Experiments/Tests ($\text{Mp} = 0.9$):* **Minor Discount.** Risks are slightly forgiven, but unsafe code will still flash Red.
  * *Core/Auth ($\text{Mp} = 1.2$):* **Amplified.** Risks are punished heavily. Fragility here is unacceptable.

## 2.2.G.3. The Equation: The Structural Integrity Sigmoid

We calculate **Net Exposure** rather than Integrity Density, utilizing Laplace Smoothing to prevent tiny files from aggressively skewing the spectrum.

**Step A: Calculate Smoothed Attack & Defense Densities**
We sum the weighted risks and fortifications. Instead of dividing strictly by LOC, we use **Laplace Smoothing** ($\text{LOC} + 20.0$). This prevents a 5-line file with a single `try/catch` from registering as infinitely safe.

$$\text{SmoothedLOC} = \max(\text{LOC}, 1) + 20.0$$
$$\text{AttackDensity} = \left( \frac{\text{WeightedAttackers} + \text{Irc}}{\text{SmoothedLOC}} \right) \times \text{Mp}$$
$$\text{DefenseDensity} = \left( \frac{\text{WeightedDefenders}}{\text{SmoothedLOC}} \right) \times \text{Fc}$$

**Step B: Calculate Net Exposure**
We subtract defense from attack. We also subtract a minor `systems_buffer` for implicit languages to account for their naturally looser structures.
* **Positive Exposure:** Risks outweigh Defenses (Fragile / Red).
* **Negative Exposure:** Defenses outweigh Risks (Fortified / Blue).

$$\text{NetExposure} = (\text{AttackDensity} - \text{DefenseDensity}) - \text{SystemsBuffer}$$

**Step C: The Sigmoid Score & Breach Floor**
We map the exposure to a $0-100$ scale using a steep Sigmoid slope ($12.0$). 

$$\text{Score} = \frac{100}{1 + e^{-12.0 \times \text{NetExposure}}}$$

If the code has a high density of explicit `danger` hits and Attack outpaces Defense, the file is subject to a hard **Breach Floor** (scaling up to $80.0$). This guarantees that catastrophic structural weaknesses cannot be "math-ed away" by simply adding empty `try/catch` blocks.

## 2.2.G.4. Implementation (Python Reference)

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
    danger_density = (eq.get("danger", 0) + eq.get("safety_neg", 0)) / safe_loc
    
    if danger_density > t.get("breach_density_min", 0.03) and attack > defense:
        floor = min(t.get("breach_floor_max", 80.0), 30.0 + (danger_density * t.get("breach_floor_mult", 500.0)))
        score = max(score, floor)

    return max(score, 0.0)
