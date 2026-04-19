# Testing & Verification Exposure

> **Metric: Verification Density (Internal Assertions & Sibling Coverage)**
>
> **Summary:** Visualizes the "Security Blanket" of the knowledge graph. In GitGalaxy, we distinguish between *Defensive Code* (handling errors at runtime) and *Verified Code* (proving correctness at design time). Because this metric has been unified into the Risk Exposure model, a high score now indicates a *lack* of verification (high risk), while a low score indicates ironclad, verified code.
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.
> * 🟦 **IRONCLAD (Score 15-20):** Fortified. The code is heavily backed by internal assertions, mocks, or a dedicated sibling test suite. *(Note: The deterministic engine enforces a hard minimum floor of 15.0, acknowledging that no code is 100% perfectly safe).*
> * 🟨 **MODERATE (Score 40-59):** Partial verification. Meets the bare minimum threshold.
> * 🟥 **VERY HIGH (Score 80-100):** Speculative. The code might work, but there is no programmatic proof. It relies entirely on hope.

## The Inputs (Verification Signals)

We combine internal evidence (assertions) with external evidence (sibling files). The file system checks are now abstracted, passing an `is_protected` boolean directly into the deterministic engine.

| Variable | Target Syntax / System | Weight | Structural Definition |
| :--- | :--- | :--- | :--- |
| `test_hits` | `assert`, `describe`, `mock` | 5.0x | **Internal Tests.** Assertions, mocks, and test definitions inside the file itself. |
| `is_protected` | `X.test.js` next to `X.js` | +30.0 (Flat) | **Sibling Match.** External Coverage. This flat density bonus represents strong verification intent. |
| `Mass Penalty` | `LOC > 300` | Variable | **Monolith Penalty.** Files over 300 lines gain a stacking risk penalty up to +40. Massive files cannot be adequately verified by unit tests alone. |

## Universal Framework Integration

**Exemptions:** Untestable files (e.g., Markdown, Makefiles, CMake, or specific extensions configured in the asset masks) bypass the engine entirely, returning a $0.0$ risk score.

* **$Fc$ (Fidelity Coefficient):** Applied as an inverted multiplier ($2.0 - Fc$). We trust explicit verification in high-fidelity languages more than loose assertions in implicit languages.
* **$Irc$ (Implicit Risk Correction):** Added to the Threshold. Implicit languages (Python, Ruby) rely entirely on tests for type safety, meaning they require a *higher* density of tests to clear the risk bar.
* **$Mp$ (Path Modifier):** Scales the Threshold. Critical infrastructure (`core/`) gets a higher bar; notoriously hard-to-test views (`UI/`) get a lower bar.

## The Equation: The Verification Sigmoid

**Step A: The Exemption Bypass**
If the file matches known untestable patterns (e.g., `readme`, `makefile`), the engine immediately returns $0.0$.

**Step B: Calculate Verification Density**
We calculate the density of internal tests and add the flat Sibling Bonus ($+30.0$). The bonus is added directly to the density because the existence of a test file implies coverage of the whole module.

$$InternalDensity = \left( \frac{test\_hits \times 5.0}{\max(LOC, 1)} \right) \times 100.0$$
$$TotalDensity = InternalDensity + SiblingBonus$$

**Step C: Determine The Bar (Dynamic Threshold)**
This is the "Passing Grade" the density must overcome to lower the risk score.

$$Threshold = (15.0 + (Irc \times 3.0)) \times Mp$$

**Step D: The Inverse Sigmoid Map**
We map density against the dynamic threshold using a positive exponent. As Verification Density *increases*, the denominator grows, and the Risk Exposure mathematically *decreases*.

$$RawExposure = \frac{100.0}{1 + e^{0.25 \times (TotalDensity - Threshold)}}$$

**Step E: Trust Adjustment & Mass Penalty**
We multiply the result by the inverted Fidelity score ($2.0 - Fc$). If the file size exceeds the `MASSIVE_FILE_THRESHOLD` (300 lines), we calculate and add a structural mass penalty, capping the final calculation between the $15.0$ risk floor and $100.0$ maximum.

$$FinalExposure = \min(\max((RawExposure \times (2.0 - Fc)) + MassPenalty, 15.0), 100.0)$$

## Implementation (Python Reference)

```python
import math
import os
from typing import Dict

def _calc_verification(self, loc: int, file_path: str, is_protected: bool, eq: Dict[str, int], irc: int, fc: float, mp: float, umbrella_bonus: float = 0.0) -> float:
    filename = os.path.basename(file_path).lower()
    ext = filename.split('.')[-1] if '.' in filename else ""
    
    exempt_exts = self.asset_masks.get("UNTESTABLE_EXTENSIONS", set())
    exempt_names = self.asset_masks.get("UNTESTABLE_NAMES", set())
    
    # Step A: Untestable Bypass
    if ext in exempt_exts or filename in exempt_names or filename.startswith('readme') or 'makefile' in filename or 'cmake' in filename:
        return 0.0

    t = self.risk_tuning.get("verification", {})
    safe_loc = max(loc, 1)
    
    # Step B: Verification Density
    sibling_bonus = t.get("sibling_bonus", 30.0) if is_protected else 0.0
    internal_density = (eq.get("test", 0) * t.get("internal_test_mult", 5.0) / safe_loc) * 100.0
    total_density = internal_density + sibling_bonus 
    
    # Step C: Dynamic Threshold
    threshold = (t.get("threshold_base", 15.0) + (irc * t.get("irc_mult", 3.0))) * mp
    
    # Step D: Inverse Sigmoid Map
    try:
        raw_exposure = 100.0 / (1.0 + math.exp(t.get("sigmoid_slope", 0.25) * (total_density - threshold)))
    except OverflowError:
        raw_exposure = 0.0 if total_density > threshold else 100.0
        
    # Step E: Trust Adjustment
    final_exposure = raw_exposure * (2.0 - fc)

    # Step F: The Mass Penalty
    if safe_loc > self.MASSIVE_FILE_THRESHOLD:
        mass_penalty = min((safe_loc - self.MASSIVE_FILE_THRESHOLD) / t.get("mass_penalty_div", 20.0), t.get("mass_penalty_max", 40.0)) 
        final_exposure += mass_penalty

    # Enforce the 15.0 Risk Floor
    return min(max(final_exposure, t.get("risk_floor", 15.0)), 100.0)