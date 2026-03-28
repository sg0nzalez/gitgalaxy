# 2.2.M. The \"Civil War\" Algorithm: Tabs vs. Spaces

-   Visual Mapping:

-   Score 0 (Pure Tabs): Visual: Glowing Green
(#00FF00). Emissive intensity is maxed.
-   Score 100 (Pure Spaces): Visual: Glowing Yellow
(#FFFF00). Emissive intensity is maxed.
-   Score 50 (Maximum Conflict): Visual: Deep Blue
(#0000FF). 50/50 split triggers the \"Bifurcation Shimmer\"
(geometry flickering).
-   Gradient: Linear transition from Green (0) → Blue (50) →
Yellow (100).

-   Equation:

*\# 1. Gather Indentation Context:*

*\# Lt = Count of lines starting with Tabs*

*\# Ls = Count of lines starting with Spaces*

*\# Ltotal = Total lines with indentation context*

*Ltotal = TabLines + SpaceLines*

*\# 2. Calculate Space-Ratio (R):*

*\# 0.0 means 100% Tabs. 1.0 means 100% Spaces.*

*R = SpaceLines / max(Ltotal, 1)*

*\# 3. Final Score Mapping (0-100):*

*FinalScore = R \* 100*

-   Range: **0** (Pure Tabs) to **100** (Pure Spaces).

-   Why this works: This is a Linear Polarization Model.

-   Terminology: While colloquially referred to as \"Civil
War,\" the equation measures Layout Unity.
-   Logic: By mapping Tabs to 0 and Spaces to 100, the \"War
Zone\" (50/50 mix) naturally sits at the center of the spectrum
(Score 50).
