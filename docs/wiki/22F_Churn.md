# 2.2.F. Churn

## 2.2.F.A. The Philosophy: Relative Historical Volatility

Churn measures the \"Frequency of Interruption.\" However, \"High
Churn\" is relative. In a startup, 10 commits/week is normal. In a
legacy bank system, 1 commit/week is alarming.

We use Auto-Scaling Normalization to make this metric useful for any
project. The most volatile file in the repository always defines the
\"100\" mark. All other files are measured relative to this local
maximum.

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum,
scaling from cool blue (static, settled code) to intense red (highly
active, fluid code).

We rely on the version control history (Git) to extract \"Deep Time\"
metrics.

-   **STATIC (Score 0 - 20, Blue):** The most stable files in this
specific repo. Rarely touched since creation.
-   **HIGHLY ACTIVE (Score 80 - 100, Red):** The absolute hotspots of
the repository, taking into account their age and commit density.

## 2.2.F.B. The Inputs (Git History Data)

We rely on the version control history (Git) to extract \"Deep Time\"
metrics.

------------------ ---------------------- --------- ---------------------------------------------------------------------------------
CommitCount        **commit_count**       Integer   The raw volume of change. Every commit is a \"stress event.\"
SecondsFromMax     **repo_max - mtime**   Seconds   The duration the file has existed relative to the newest commit in the repo.
RepoMaxFrequency   Calculated             Float     The highest \"Seismic Frequency\" found in the entire repository during Pass 1.
------------------ ---------------------- --------- ---------------------------------------------------------------------------------

## 2.2.F.C. The Universal Framework Integration

While Churn is auto-scaled globally, we still apply the Path Modifier
(*Mp*) to account for architectural expectations after normalization.

-   **Fc (Fidelity Coefficient):** Not Applied. History is absolute.
-   **Irc (Implicit Risk Correction):** Not Applied.
-   **Mp (Path Modifier):** Applied. We expect high churn in
*experiments/* (Low Mp), but high churn in *kernel/* or *core/* is a
critical warning (High Mp).

## 2.2.F.D. The Equation: The Two-Pass Relative Seismic Model

During the initial scan, we calculate the Raw Seismic Frequency for
every file. We divide commits by the square root of its age in weeks.
The square root dampens the penalty for very old files. A 10-year-old
file with 1000 commits (sustained activity) is a hotspot, but less so
than a 1-month-old file with 100 commits (explosive activity).

**Phase 2: Logarithmic Normalization (The Second Pass)** Once all files
are scanned and the true Global Max Frequency is found, we revisit every
file. We apply *math.log1p()* to both the global max and the individual
file frequency before dividing them. This flattens extreme outliers and
ensures a beautiful, smooth color gradient across the 3D galaxy.

**Phase 3: Context Adjustment** Finally, we multiply the normalized
logarithmic score by the Path Modifier (*Mp*) to dampen or amplify the
significance based on its location in the directory tree.

## 2.2.F.E. Implementation (Python Reference)

import math

from typing import List, Dict, Any

def \_normalize_temporal_metrics(self, stars: List\[Dict\[str, Any\]\]):

\"\"\"\[PASS 2\] Normalizes churn using a Logarithmic Curve for better
UI gradients.\"\"\"

if not stars: return

max_freq = 0.0

\# Phase 1: Find the volcano (Global Max)

for s in stars:

freq = s.get(\"telemetry\", {}).get(\"raw_churn_freq\", 0.0)

if freq \> max_freq:

max_freq = freq

\# THE FIX: Apply a logarithmic curve to the maximum ceiling

\# math.log1p safely handles 0 values (log(1 + x))

safe_max_f = math.log1p(max(max_freq, 1.0))

idx = self.RISK_SCHEMA.index(\"churn\")

\# Phase 2: Normalize every star against the logarithmic curve

for s in stars:

freq = s.get(\"telemetry\", {}).get(\"raw_churn_freq\", 0.0)

\# Apply the same logarithmic curve to the individual file

base_score = (math.log1p(freq) / safe_max_f) \* 100.0

\# Phase 3: Apply Path Modifiers

mp = s.get(\"telemetry\", {}).get(\"multipliers\", {}).get(\"churn\",
1.0)

final_churn = min(base_score \* mp, 100.0)

\# Inject Churn directly into the dynamic Risk Vector index

if \"risk_vector\" in s and len(s\[\"risk_vector\"\]) \> idx:

s\[\"risk_vector\"\]\[idx\] = round(final_churn, 2)

## 2.2.F.F. Visual Verification (\"The Truth\")

**Scenario:** A 5-year-old Legacy project vs. a 2-month-old Startup
project.

Project A: The Startup (High Velocity)

-   **Most Changed File:** *App.tsx* (50 commits, 8 weeks old).
-   **Result:** Normalizes to *100.0*. Glows intense Red.
-   **Average File:** *Button.tsx* (5 commits, 8 weeks old).
-   **Result:** Scales logarithmically. Glows Yellow/Orange.

Project B: The Enterprise Monolith (Low Velocity)

-   **Most Changed File:** *TransactionCore.java* (200 commits, 5 years
old).
-   **Result:** Normalizes to *100.0*. Glows intense Red. It is the
hotspot of this specific repo.
-   **Average File:** *Utils.java* (10 commits, 5 years old).
-   **Result:** Scales logarithmically. Glows cool Blue.

**Result:** The \"Hotspot\" is clearly identified as a danger zone
relative to its surroundings in both projects, completely independent of
the massive difference in raw commit counts.
