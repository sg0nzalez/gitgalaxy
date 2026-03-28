# 2.2.F. Deep Churn

> **Metric: Relative Historical Volatility (Frequency of Interruption)**
>
> **Summary:** Churn measures how often a file is changed. However, "High Churn" is relative. In a startup, 10 commits/week is normal. In a legacy bank system, 1 commit/week is alarming. We use Auto-Scaling Normalization to make this metric useful for any project. The most volatile file in the repository always defines the "100" mark. All other files are measured relative to this local maximum.
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum, scaling from 🟦 **Deep Blue** (static, settled code) to 🟥 **Intense Red** (highly active, fluid code).

## 2.2.F.1. The Philosophy: Deep Time Analysis

We rely on the version control history (Git) to extract "Deep Time" metrics.

* **STATIC (Score 0 - 20, Blue):** The most stable files in this specific repo. Rarely touched since creation.
* **HIGHLY ACTIVE (Score 80 - 100, Red):** The absolute hotspots of the repository, taking into account their age and commit density.

## 2.2.F.2. The Inputs (Git History Data)

| Variable | Source | Data Type | Structural Definition |
| :--- | :--- | :--- | :--- |
| `commit_count` | Scanner | Integer | The raw volume of change. Every commit is a "stress event." |
| `age_in_weeks` | Calculated | Float | The duration the file has existed relative to the newest commit in the repo. |
| `max_freq` | Calculated | Float | The highest "Seismic Frequency" found in the entire repository during Pass 1. |

## 2.2.F.3. The Universal Framework Integration

While Churn is auto-scaled globally, we still apply the Path Modifier ($\text{Mp}$) to account for architectural expectations after normalization.

* **$\text{Fc}$ (Fidelity Coefficient):** Not Applied. Version control history is absolute.
* **$\text{Irc}$ (Implicit Risk Correction):** Not Applied.
* **$\text{Mp}$ (Path Modifier):** Applied. We expect high churn in an `experiments/` folder (Low $\text{Mp}$ penalty), but high churn in a `kernel/` or `core/` folder is a critical architectural warning (High $\text{Mp}$ penalty).

## 2.2.F.4. The Equation: The Two-Pass Relative Seismic Model

**Phase 1: Raw Seismic Frequency**
During the initial scan, we calculate the Raw Seismic Frequency for every file. We divide commits by the square root of its age in weeks. The square root dampens the penalty for very old files. A 10-year-old file with 1,000 commits (sustained activity) is a hotspot, but less so than a 1-month-old file with 100 commits (explosive activity).

$$\text{Freq} = \frac{\text{Commits}}{\sqrt{\max(\text{AgeInWeeks},\ 1.0)}}$$

**Phase 2: Logarithmic Normalization**
Once all files are scanned and the true Global Max Frequency ($\text{MaxFreq}$) is found, we revisit every file. We apply $\ln(1 + x)$ to both the global max and the individual file frequency before dividing them. This flattens extreme outliers and ensures a smooth, readable color gradient across the 3D galaxy.

$$\text{BaseScore} = \left( \frac{\ln(1 + \text{Freq})}{\ln(1 + \text{MaxFreq})} \right) \times 100$$

**Phase 3: Context Adjustment**
Finally, we multiply the normalized logarithmic score by the Path Modifier ($\text{Mp}$) to dampen or amplify the significance based on its location in the directory tree.

$$\text{FinalScore} = \min(\text{BaseScore} \times \text{Mp},\ 100)$$

## 2.2.F.5. Implementation (Python Reference)

```python
import math
from typing import List, Dict, Any

def _normalize_temporal_metrics(self, stars: List[Dict[str, Any]]):
    """[PASS 2] Normalizes churn using a Logarithmic Curve for better UI gradients."""
    if not stars: return

    max_freq = 0.0

    # Phase 1: Find the volcano (Global Max)
    for s in stars:
        freq = s.get("telemetry", {}).get("raw_churn_freq", 0.0)
        if freq > max_freq:
            max_freq = freq

    # THE FIX: Apply a logarithmic curve to the maximum ceiling
    # math.log1p safely handles 0 values (log(1 + x))
    safe_max_f = math.log1p(max(max_freq, 1.0))
    idx = self.RISK_SCHEMA.index("churn")

    # Phase 2: Normalize every star against the logarithmic curve
    for s in stars:
        freq = s.get("telemetry", {}).get("raw_churn_freq", 0.0)
        
        # Apply the same logarithmic curve to the individual file
        base_score = (math.log1p(freq) / safe_max_f) * 100.0

        # Phase 3: Apply Path Modifiers
        mp = s.get("telemetry", {}).get("multipliers", {}).get("churn", 1.0)
        final_churn = min(base_score * mp, 100.0)

        # Inject Churn directly into the dynamic Risk Vector index
        if "risk_vector" in s and len(s["risk_vector"]) > idx:
            s["risk_vector"][idx] = round(final_churn, 2)
