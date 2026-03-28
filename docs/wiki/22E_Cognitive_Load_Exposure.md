# 2.2.E. Cognitive Load Exposure

**Summary:** Visualizes the \"Mental RAM\" required to understand a
file. Unlike Lines of Code (which measures physical size), Cognitive
Load measures the density of decision-making and the \"tangleness\" of
logic. A healthy engineering culture admits that human working memory is
a finite resource. This metric is a tool for Engineering Empathy. We
recognize that complex problems often require complex solutions; we
don\'t measure \'Tangled Logic\' to critique the necessity of the code,
but to surface it so the team can be honest about which files require
the most mental overhead. Surfacing \'Brain Melting\' zones is an act of
transparency that protects the team from burnout by identifying where
the highest cognitive tax is being paid.

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum,
scaling from cool blue (linear, easy-to-read data) to intense red
(high-friction, multi-state async logic).

## 2.2.E.1. The Philosophy: The Entropy of Understanding

Human working memory is a biological bottleneck. Every time a developer
encounters a nested *if*, a complex ternary, or a manual memory
management keyword, they must \"cache\" the current state in their
brain. This represents the total Cognitive Load of a module.

In GitGalaxy, we treat code as a thermal system where logic generates
heat and documentation provides cooling. By being honest about where the
Cognitive Load is \"hot,\" we move away from performance judgment and
toward resource management. We acknowledge that \"High Load\" is often a
requirement of high-performance or high-utility code; the goal is
visibility, not elimination.

-   **Low Cognitive Load:** Linear code that reads like a story; low
impact on the developer\'s working memory.
-   **High Cognitive Load:** Necessary but complex logic that requires
the developer to simulate multiple realities simultaneously;
identifies areas that require peak focus.

## 2.2.E.2. The Philosophy: Mental Friction Density

**\"Not how big it is, but how hard it is to read.\"**

We measure the density of decision-making per line of code. Unlike
\"Mass\" (Star Size), which measures volume, this exposure highlights
\"Brain Melting\" zones---code that requires a developer to hold
multiple states, timelines, or abstract concepts in their working memory
simultaneously.

-   **Low Score (0 - 20, Blue):** Linear flow. Data definitions.
Configs. (e.g., HTML, JSON, simple DTOs).
-   **High Score (90 - 100, Red):** High branching, async timing, state
mutation, and meta-programming packed into a tight space.

## 2.2.E.3. The Inputs (Regex & Heuristics)

We utilize the pre-calculated hits from the blAST engine and weight them
based on the \"Mental Tax\" they impose on the reader.

-------------- ------------------- ------- -------------- -------------------------------------------------------------------------------------------------------------------------------
BranchHits     **branch**          1.0x    0.5 density    The baseline of decision making (**if**/**else**). Clamped to prevent massive, flat switch-statements from breaking the math.
FluxHits       **flux**            2.0x    0.75 density   State Mutation. Tracking variables changing values taxes short-term memory more than static logic.
AsyncHits      **concurrency**     3.0x    None           Temporal Complexity. Logic that jumps in time forces the reader to track non-linear execution.
HeatTriggers   **heat_triggers**   5.0x    None           Abstraction penalty. Macros, reflection, and dynamic dispatch hide the true logic, forcing \"mental compilation.\"
DangerHits     **danger**          5.0x    None           Anxiety. **eval** or unsafe code forces the brain into a slow, high-alert verification mode.
DocHits        **doc**             10.0x   None           Structured documentation provides mental shortcuts, reducing the effective load (acts as a cooling agent).
-------------- ------------------- ------- -------------- -------------------------------------------------------------------------------------------------------------------------------

## 2.2.E.4. The Universal Framework Integration

We apply the standard physics variables to ensure fairness across
languages and environments.

-   **Irc (Implicit Risk Correction):** Added to the total density.
Opaque languages (Shell, Perl) get a baseline complexity penalty
because the syntax itself implies hidden logic.
-   **Fc (Fidelity Coefficient):** Applied to the Cooling Factor. We
trust documentation in explicit languages (Java) more than in
implicit ones (Ruby) where comments might drift from reality.
-   **Mp (Path Modifier):** Utilized to allow contextual overrides. For
example, highly complex mocking logic in a *tests/* directory may
receive an Mp reduction, as the cognitive expectations there differ
from a production runtime core.

## 2.2.E.5. The Equation: The \"Badge of Honor\" Sigmoid

We use a Logistic Function (Sigmoid) tuned to be forgiving of moderate
complexity but demanding of high complexity.

**Step A: Calculate Clamped Densities** We calculate the per-line
density of each stressor. Branch and Flux densities are clamped. A file
with 5,000 lines of simple *case* statements shouldn\'t be flagged as
brain-melting just because of high branch counts.

**Step B: The Synergistic Sum** We sum the clamped densities and heavy
logic multipliers, then add the baseline *Irc* density.

**Step C: The Sigmoid Curve (The Score)** We map the total density to a
0-100 scale using a Sigmoid with tunable levers.

-   **Threshold:** *0.75*. This pushes the \"center\" of the curve to
the right. Code must have a high density (0.75 weighted points per
line) just to reach a score of 50.
-   **Slope:** *4.0*. A moderate slope ensures a smooth transition
rather than a sudden wall. It allows for nuance in the 50-80 range.

**Step D: The Cooling Factor (The Antidote)** Documentation reduces
load, but never to zero. Complex logic is still complex, even if
explained well. We cap the cooling effect at a maximum reduction of 50%.
The final score is then multiplied by the Path Modifier (*Mp*).

## 2.2.E.6. Implementation (Python Reference)

*import math*

*from typing import Dict, Tuple*

*def \_calc_cog_load(self, loc: int, eq: Dict\[str, int\], irc: int, fc:
float, mp: float) -\> Tuple\[float, float\]:*

* safe_loc = max(loc, 1)*

* t = self.risk_tuning.get(\"cognitive_load\", {})*

* *

* \# Bypass 1: Tiny scripts don\'t have enough mass to be cognitively
overwhelming*

* if safe_loc \< 15:*

* total_density = sum(\[eq.get(k, 0) for k in \[\"branch\", \"flux\",
\"concurrency\", \"heat_triggers\", \"danger\"\]\]) / safe_loc + (irc /
safe_loc)*

* return 5.0, total_density*

* *

* branches = eq.get(\"branch\", 0)*

* *

* \# Bypass 2: Massive, flat files (data dumps) are safe*

* if branches == 0 and safe_loc \> 50:*

* return 0.0, 0.0*

* *

* branch_density = branches / safe_loc*

* flux_density = eq.get(\"flux\", 0) / safe_loc*

* concurrency_density = eq.get(\"concurrency\", 0) / safe_loc*

* heat_density = eq.get(\"heat_triggers\", 0) / safe_loc*

* danger_density = eq.get(\"danger\", 0) / safe_loc*

* *

* \# Step A: Apply Clamping*

* clamped_branch = min(branch_density \* 1.0, t.get(\"branch_clamp\",
0.5))*

* clamped_flux = min(flux_density \* t.get(\"flux_mult\", 2.0),
t.get(\"flux_clamp\", 0.75)) *

* *

* \# Step B: Synergistic Sum of Heavy Logic*

* heavy_logic = (concurrency_density \* t.get(\"async_mult\", 3.0)) +
\\*

* (heat_density \* t.get(\"heat_mult\", 5.0)) + \\*

* (danger_density \* t.get(\"danger_mult\", 5.0))*

* *

* total_density = clamped_branch + clamped_flux + heavy_logic + (irc /
safe_loc)*

* *

* if safe_loc \<= 2 and total_density == 0:*

* return 0.0, total_density*

* *

* \# Step C: Sigmoid Curve*

* try:*

* raw_score = 100.0 / (1.0 + math.exp(-t.get(\"sigmoid_slope\", 4.0) \*
(total_density - t.get(\"sigmoid_offset\", 0.75))))*

* except OverflowError:*

* raw_score = 100.0 if total_density \> t.get(\"sigmoid_offset\", 0.75)
else 0.0*

* *

* \# Step D: Cooling Factor & Path Multiplier*

* doc_coverage = (eq.get(\"doc\", 0) \* t.get(\"doc_mult\", 10.0)) /
safe_loc*

* cooling = max(0.5, 1.0 - (doc_coverage \* fc))*

* *

* return min(raw_score \* cooling \* mp, 100.0), total_density*

## 2.2.E.7. Visual Verification (\"The Truth\")

-------------------------- ---------------- --------- -------------- ----------------------------------------------------------------
Big JSON Config            **\[0-19\]**     \~0-5     VERY LOW       Zero branching. Minimal baseline density.
Standard UI Component      **\[20-39\]**    \~10-25   LOW            Standard complexity. Easily held in working memory.
Complex Algorithm          **\[40-59\]**    \~40-55   INTERMEDIATE   Noticeable, but not alarming. \"Doing work.\"
Heavy Logic Core           **\[60-89\]**    \~65-85   HIGH           The Tipping Point. Heavy branching mixed with state flux.
Extreme Meta-Programming   **\[90-100\]**   \~95+     VERY HIGH      Rare. Dense cluster of async, reflection, and danger per line.
-------------------------- ---------------- --------- -------------- ----------------------------------------------------------------

**
