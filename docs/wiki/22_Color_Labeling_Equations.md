### 2.2 Color Labeling Equations

#### 2.2.A. Overview of methodology

+----------------+----------------+----------------+----------------+
| Labeling Mode  | ****What It    | Color          | Visual Effect  |
|                | Checks****     |                |                |
+----------------+----------------+----------------+----------------+
| ****Ownership  | **Who wrote    | **** White**** | **Rainbow.**   |
| ****           | this?** Shows  |                | Single colors  |
|                | if a file is   |                | are            |
|                | owned by one   |                | individuals;   |
|                | person (Solo)  |                | bright White   |
|                | or everyone    |                | is a team      |
|                | (Collective).  |                | effort.        |
+----------------+----------------+----------------+----------------+
| ****Cognitive  | **How hard is  | ****           | **Purple.**    |
| Load ****      | it to read?**  | ****           | The deeper the |
|                | Highlights     | P****urple**** | purple, the    |
|                | confusing      |                | harder the     |
|                | logic that     |                | logic is to    |
|                | requires high  |                | follow.        |
|                | mental effort. |                |                |
+----------------+----------------+----------------+----------------+
| ****Churn****  | **How often    | ****Orange**** | **Orange.**    |
| ****           | does it        |                | Bright orange  |
|                | change?**      |                | indicates a    |
|                | Identifies     |                | file that      |
|                | files that are |                | refuses to     |
|                | constantly     |                | settle down.   |
|                | being          |                |                |
|                | rewritten or   |                |                |
|                | patched.       |                |                |
+----------------+----------------+----------------+----------------+
| ****Safety     | **Is it        | ****Red ****   | **Red to       |
| ****           | bulletproof?** |                | Cyan.** Red is |
|                | Checks for     | ****to****     | fragile/risky; |
|                | defensive code |                | Cyan is        |
|                | (error         | **** Cyan****  | f              |
|                | handling) vs.  |                | ortified/safe. |
|                | risky code.    |                |                |
+----------------+----------------+----------------+----------------+
| ****Tech       | **Are there    | ****Red****    | **Red.**       |
| Debt****       | shortcuts?**   |                | Glowing red    |
|                | Scans for      |                | highlights     |
|                | \"TODOs\",     |                | unfinished     |
|                | \"Hacks\", and |                | business.      |
|                | temporary      |                |                |
|                | fixes.         |                |                |
+----------------+----------------+----------------+----------------+
| ****Doc        | **Is it        | ****Library    | **Gold.**      |
| Mode****       | explained?**   | Gold****       | Bright gold    |
|                | Measures the   |                | indicates      |
|                | quality of     |                | library-grade  |
|                | instruction    |                | documentation. |
|                | manuals and    |                |                |
|                | comments.      |                |                |
+----------------+----------------+----------------+----------------+
| ****Commit     | **Is it        | Green          | **Green.**     |
| Heat****       | fresh?** Shows |                | Radioactive    |
|                | where work is  |                | green means it |
|                | happening      |                | was edited     |
|                | *right now*    |                | today.         |
|                | vs. months     |                |                |
|                | ago.           |                |                |
+----------------+----------------+----------------+----------------+
| ****Test       | **Is it        | Pink           | **Pink.**      |
| Coverage****   | verified?**    |                | Glowing pink   |
|                | Checks if the  |                | means the code |
|                | code has a     |                | is heavily     |
|                | safety net of  |                | tested.        |
|                | tests proving  |                |                |
|                | it works.      |                |                |
+----------------+----------------+----------------+----------------+
| []{#a          | **Tabs or      | Green Vs.      | **Green vs     |
| nchor-63}Civil | Spaces?**      | Yellow         | Yellow.** Blue |
| War            | Checks for     |                | indicates a    |
|                | indentation    |                | messy mix of   |
|                | consistency.   |                | both.          |
+----------------+----------------+----------------+----------------+
| []{#ancho      | **Is there     | Purple         | **Purple.** A  |
| r-64}Graveyard | dead code?**   |                | \"haunted\"    |
|                | Finds blocks   |                | purple glow    |
|                | of code that   |                | indicates      |
|                | were commented |                | historical     |
|                | out and        |                | hoarding.      |
|                | abandoned.     |                |                |
+----------------+----------------+----------------+----------------+
| API Exposure   | **Is it        | #ff007f        | **Electric     |
|                | public?**      |                | Rose.**        |
|                | Highlights the | Electric Rose  | Indicates a    |
|                | entry points   |                | public         |
|                | where the      |                | interface or   |
|                | system talks   |                | endpoint.      |
|                | to the outside |                |                |
|                | world.         |                |                |
+----------------+----------------+----------------+----------------+
| Concurrency    | **Is it        | #7b2ff7        | **             |
| Exposure       | m              |                | Ultraviolet.** |
|                | ultitasking?** | Electric       | Indicates      |
|                | Highlights     | Ultraviolet    | potential race |
|                | complex        |                | conditions or  |
|                | timing,        |                | timing risks.  |
|                | threads, or    |                |                |
|                | asynchronous   |                |                |
|                | logic.         |                |                |
+----------------+----------------+----------------+----------------+
| State Flux     | **Is the data  | #ffb84e        | **Clyde        |
| Exposure       | changing?**    |                | Orange.**      |
|                | Highlights     | Clyde Orange   | Indicates      |
|                | variables that |                | \"boiling\"    |
|                | are constantly |                | data that is   |
|                | being          |                | hard to track. |
|                | mod            |                |                |
|                | ified/mutated. |                |                |
+----------------+----------------+----------------+----------------+

****

#### 2.2.B. Sub-Equations

To ensure the equations above are actionable, the following variables
are defined based on the scanner\'s regex hits:

**branch_hits:** Control flow constructs including
conditionals (*****if*****, *****switch*****), loops (*****for*****,
*****while*****), jumps (*****break*****, *****throw*****), and logical
operators (*****&&*****, *****\|\|*****) that divert execution paths.
****

-   **args_hits:** Function signatures, parameter lists,
input registers, or lambda arguments that define the data inputs for
a logic block.

```{=html}
<!-- -->
```
-   **linear_hits:** Sequential flow markers, including
variable declarations (*const*, *var*), imports, returns, and
structural keywords that indicate non-branching logic.

```{=html}
<!-- -->
```
-   **func_start_hits:** The syntactic anchor identifying
the beginning of a named function, method, subroutine, or procedure
definition (excluding classes/interfaces).

```{=html}
<!-- -->
```
-   **class_start_hits:** The syntax that defines an
object-oriented class, struct, record, or enum, driving API surface
area calculations.

```{=html}
<!-- -->
```
-   **safety_hits:** Defensive constructs such as
exception handling (*try/catch*), type assertions, null checks, and
memory protection mechanisms (*readonly*).

```{=html}
<!-- -->
```
-   **safety_neg_hits:** Risk factors including error
suppression, dynamic code execution (*eval*), type-system bypasses
(*any*, *!*), and unsafe pointer usage.

```{=html}
<!-- -->
```
-   **danger_hits:** Critical indicators of technical debt
(*TODO/FIXME*), destructive system calls (*process.exit*), hardcoded
secrets, or catastrophic failure modes.

```{=html}
<!-- -->
```
-   **io_hits:** Interactions with external boundaries,
including file systems, network requests (*fetch*), database
queries, and hardware I/O.

```{=html}
<!-- -->
```
-   **api_hits:** Keywords identifying public interfaces
(*export*, *public*), exported members, or globally accessible entry
points that define surface area.

```{=html}
<!-- -->
```
-   **flux_hits:** Markers of state change, including
variable assignment (*let*, *mut*), mutable collections, pointer
updates, and side-effect triggers.

```{=html}
<!-- -->
```
-   **graveyard_hits:** Patterns detecting commented-out
code blocks (*// if*), legacy logic, or \"zombie\" code (*//
console.log*) that remains in the source file.

```{=html}
<!-- -->
```
-   **doc_hits:** Structured documentation syntax,
including JSDoc (*/\*\**), XML comments, and standard metadata tags
describing code intent.

```{=html}
<!-- -->
```
-   **test_hits:** Framework-specific keywords for
assertions, unit test definitions, mocks, and verification suites
(*describe*, *assert*, *mock*).

```{=html}
<!-- -->
```
-   **concurrency_hits:** Constructs for asynchronous
execution (*async/await*), threading, parallel processing,
coroutines, and synchronization primitives.

```{=html}
<!-- -->
```
-   **ui_framework_hits:** Patterns specific to frontend
or UI development, including component definitions, view bindings
(*document.getElementById*), and rendering logic.

```{=html}
<!-- -->
```
-   **closures_hits:** Syntax for anonymous functions,
lambdas, blocks, or inline delegates that capture local context
(*=\>*).

```{=html}
<!-- -->
```
-   **globals_hits:** References to global scope
(*window.*, *process.env*), environment variables, singletons, or
system-wide shared state.

```{=html}
<!-- -->
```
-   **decorators_hits:** Annotations, attributes, or
wrapper syntax used to modify or tag classes and methods with
metadata (*\@Injectable*).

```{=html}
<!-- -->
```
-   **generics_hits:** Syntax defining type parameters
(*\<T\>*), templates, or polymorphic structures for type-agnostic
logic.

```{=html}
<!-- -->
```
-   **comprehensions_hits:** High-density logic patterns
including list comprehensions, functional chains (*.map*,
*.filter*), and array transformations.

```{=html}
<!-- -->
```
-   **scientific_hits:** Usage of mathematical libraries
(*Math.*, *numpy*), tensor operations, arbitrary precision
arithmetic, or complex number processing.

```{=html}
<!-- -->
```
-   **heat_triggers_hits:** High-complexity constructs
such as metaprogramming, reflection (*Proxy*, *eval*), macros, or
dynamic dispatch that increase cognitive load.

```{=html}
<!-- -->
```
-   **import_hits:** Syntax for dependency management,
module loading (*import*, *require*), file inclusion, or library
linking.

```{=html}
<!-- -->
```
-   **ownership_hits:** Metadata extraction patterns for
identifying authors, maintainers, or copyright holders within file
headers (*\@author*).

****

#### 2.2.C. Transforming Noisy Regex Counts Into Something Meaningful

We recognize that raw heuristic counts are inherently fragile; they are
easily fooled by \"safety theater\" (like empty catch blocks) and lack
the deep contextual awareness of a compiler. To transform this fuzzy,
easily manipulated data into actionable intelligence, we implemented a
**Universal Exposure Framework** that treats code metrics not as
absolute truths, but as weighted signals within a \"Physics Engine.\"
This approach applies four specific stabilizing forces to counteract the
noise of static analysis:

-   **Weighted Asymmetry (The Entropy Check):** A simple counter treats
a vulnerability and a safeguard as equal opposites (1 - 1 = 0). In
reality, it is significantly harder to secure a system than to break
it. We apply a **2.5x multiplier** to all detected risks, forcing
the code to demonstrate disproportionate defensive density before it
can achieve a \"Safe\" rating. This prevents minor cosmetic fixes
from masking structural brittleness.
-   **The Breach Cap (Zero-Trust Logic):** To prevent large files with
high test coverage from masking critical flaws, we enforce a hard
limit: if the raw count of **Risk Hits** exceeds **Guardrail Hits**,
the module is capped at a \"Fragile\" rating regardless of its other
qualities. This overrides the math with a reality check---no amount
of unit testing can neutralize a fundamentally insecure
architecture.
-   **The Sigmoid Clamp (Noise Gating):** Linear counting penalizes
large files for having trace amounts of technical debt. We utilize a
logistic function to act as a noise gate, suppressing trivial
findings (0-5% density) while aggressively highlighting clusters of
debt once they cross a critical threshold (\~20%). This ensures the
visualization focuses on systemic patterns rather than isolated
infractions.
-   **Quantized Final Tiering (Removing False Precision):** Presenting a
\"Safety Score\" of 87.4% implies a level of precision that regex
cannot provide. By binning complex scores into five distinct
**Qualitative Tiers** (Unshielded, Fragile, Stable, Defended,
Fortified), we remove false precision and deliver a binary truth:
the module is either sufficiently defended for its context, or it is
not.

**Instead of a single \"Master Equation\" **for **all** Risk
Exposure**s**,** we employ a ******Universal Framework****** that is
instantiated and calibrated for each of the Risk Exposure domains. ** **

**The Standardization:** While each Risk Exposure equation is unique,
they all adhere to the same physics:

Each coding language is set in a tier that determines the value for Fc,
Irc.

-   **Tier 1** = Explicit Languages (High Trust, e.g., Rust).

-   **Tier 2** = Structured Languages (Minor Doubt, e.g., Java).

-   ****Tier 3**** = Implicit Languages (Fog of War, e.g., Shell).**

****

```{=html}
<!-- -->
```
-   **Fc** = Fidelity Coefficient. (A dampener used to reduce trust in
ambiguous languages).
-   **Irc** = Implicit Risk Correction. (A flat penalty added to
ambiguous languages aka \"Opacity Tax\").
-   **Mp** = Multiplier / Path Modifier. (Scales risk based on file
location, e.g., Core vs. Lab). We reward people for good file
structure, when we can.

While each risk domain has a unique formula, they all follow this
general form. We weigh risk (Asymmetry) heavier than defenses, add the
\"Opacity Tax\" to the risk, and dampen the defenses with the \"Trust
Coefficient.\"

*RiskExposure = \[ ((RiskHits + Irc) \* Weight) - (DefenseHits \* Fc) \]
/ LOC \* Mp*

#### 2.2.D. Ownership Mode: Shannon Entropy

Ownership displays the distribution of authorship within a file.
Ownership isn't about blaming a single author; it's about visualizing
the Collective Mind. A healthy culture is transparent about where
knowledge is shared and where it is siloed.

Rather than a linear author count, this system utilizes Shannon Entropy
to determine the concentration or dispersion of contributions. This
entropy score is then mapped directly to the GitGalaxy Universal Risk
Spectrum, allowing you to instantly spot heavily siloed knowledge (\"Bus
Factor\" risks) versus highly distributed community code.

##### 2.2.D.1. The Philosophy: Knowledge Concentration

Authorship is analyzed as a variable of structural clarity versus
architectural diffusion.

-   **Low Entropy (Individual Ownership):** Contributions are highly
concentrated within a single primary author. This represents a
unified mental model, but also a potential \"Silo Risk\" if that
developer is unavailable.
-   **High Entropy (Community Diffusion):** Contributions are
distributed across multiple authors. As more developers influence
the file, the architectural intent becomes shared, indicating a
high-traffic module maintained by the collective.

##### 2.2.D.2. The Inputs: Contribution Share

-   **Authors:** A data map of author identifiers to their specific
commit frequencies for the file.
-   **TotalCommits:** The aggregate sum of all commits recorded for the
file.
-   **GlobalAuthorCount:** The total number of unique contributors
across the entire repository.

##### 2.2.D.3. Equation

**p_i:** The proportion of total commits made by author \"i\" (e.g., if
Author A made 20/100 commits, p = 0.2).

Entropy = H = -sum(p_i \* log2(p_i))

OwnershipScore = min(H \* 32, 100)

##### 2.2.D.4. Why This Model is Superior

1.  **It Solves the \"Long Tail\" Problem:** A file with 1 Major Author
(90%) and 1 Minor Author (10%) is relatively stable. A file with 1
Major Author (90%) and 10 Minor Authors (1% each) is chaotic. The
Linear model scores these identical (Score: 10). The Entropy model
correctly identifies the second file as significantly more
\"active\" or \"noisy\" because it accounts for the sheer number of
distinct voices in the mix while still marking it mostly with the
color of the main author. While the Linear model only asks \"Who is
the biggest author, regardless of commit size?\", the entropy model
displays \"How much **uncertainty** exists in the authorship?\". In
GitGalaxy, high entropy means di****ffusion of ****authorship****.

-   #####

##### 2.2.D.5. Visual Interpretation: Ownership vs. Collective Diffusion

-

**GitGalaxy utilizes the standard 5-stop Universal Risk Spectrum to
visualize the entropy score, scaling from cool, isolated development to
hot, multi-author environments.**

-   INDIVIDUAL (Score 0 - 20):

-   **Visual:** Deep Blue (*#0055ff*).
-   **Definition:** Pure Ownership. The logic represents a single
individual\'s architectural intent.

-   SMALL TEAM / SQUAD (Score 21 - 60):

-   **Visual:** Cyan (*#00ffff*) transitioning to Yellow
(*#ffff00*).
-   **Definition:** Core Collaboration. Responsibility is shared
among a tight-knit group of contributors.

-   DEPT / COMMUNITY (Score 61 - 100):

-   **Visual:** Orange (*#ff8800*) transitioning to intense Red
(*#ff0000*).
-   **Definition:** Collective Maintenance. The module experiences
constant, multi-author input and has reached a state of complete
architectural diffusion.

##### 2.2.D.6. RQM: Scaling Logic & Visual Overload

By unifying Ownership under the v6.0 Universal Risk Spectrum, GitGalaxy
eliminates the need for expensive, multi-pass chromatic aberration
shaders and per-author deterministic hashing.

Because the Shannon Entropy calculation condenses infinite author
complexity into a clean *0.0 - 100.0* exposure vector in the backend
*signal_processor.py*, the frontend renderer instantly inherently
scales. Whether a file has 2 authors or 2,000, the WebGPU engine simply
translates the float into the static linear gradient. This guarantees
smooth 60 FPS performance even when mapping planetary-scale
megastructures like Linux or Kubernetes, without requiring visual
fallbacks or macroscopic LOD (Level of Detail) toggles.

#### 2.2.E. Cognitive Load Exposure

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

##### 2.2.E.1. The Philosophy: The Entropy of Understanding

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

##### 2.2.E.2. The Philosophy: Mental Friction Density

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

##### 2.2.E.3. The Inputs (Regex & Heuristics)

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

##### 2.2.E.4. The Universal Framework Integration

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

##### 2.2.E.5. The Equation: The \"Badge of Honor\" Sigmoid

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

##### 2.2.E.6. Implementation (Python Reference)

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

##### 2.2.E.7. Visual Verification (\"The Truth\")

-------------------------- ---------------- --------- -------------- ----------------------------------------------------------------
Big JSON Config            **\[0-19\]**     \~0-5     VERY LOW       Zero branching. Minimal baseline density.
Standard UI Component      **\[20-39\]**    \~10-25   LOW            Standard complexity. Easily held in working memory.
Complex Algorithm          **\[40-59\]**    \~40-55   INTERMEDIATE   Noticeable, but not alarming. \"Doing work.\"
Heavy Logic Core           **\[60-89\]**    \~65-85   HIGH           The Tipping Point. Heavy branching mixed with state flux.
Extreme Meta-Programming   **\[90-100\]**   \~95+     VERY HIGH      Rare. Dense cluster of async, reflection, and danger per line.
-------------------------- ---------------- --------- -------------- ----------------------------------------------------------------

**

#### 2.2.F. Churn

##### 2.2.F.A. The Philosophy: Relative Historical Volatility

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

##### 2.2.F.B. The Inputs (Git History Data)

We rely on the version control history (Git) to extract \"Deep Time\"
metrics.

------------------ ---------------------- --------- ---------------------------------------------------------------------------------
CommitCount        **commit_count**       Integer   The raw volume of change. Every commit is a \"stress event.\"
SecondsFromMax     **repo_max - mtime**   Seconds   The duration the file has existed relative to the newest commit in the repo.
RepoMaxFrequency   Calculated             Float     The highest \"Seismic Frequency\" found in the entire repository during Pass 1.
------------------ ---------------------- --------- ---------------------------------------------------------------------------------

##### 2.2.F.C. The Universal Framework Integration

While Churn is auto-scaled globally, we still apply the Path Modifier
(*Mp*) to account for architectural expectations after normalization.

-   **Fc (Fidelity Coefficient):** Not Applied. History is absolute.
-   **Irc (Implicit Risk Correction):** Not Applied.
-   **Mp (Path Modifier):** Applied. We expect high churn in
*experiments/* (Low Mp), but high churn in *kernel/* or *core/* is a
critical warning (High Mp).

##### 2.2.F.D. The Equation: The Two-Pass Relative Seismic Model

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

##### 2.2.F.E. Implementation (Python Reference)

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

##### 2.2.F.F. Visual Verification (\"The Truth\")

**Scenario:** A 5-year-old Legacy project vs. a 2-month-old Startup
project.****

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

#### 2.2.G. Safety Mode (Metric: Structural Fortification)

##### 2.2.G.A. The Philosophy: Structural Integrity \"The Load-Bearing Capacity of Code.\"

**Summary:** Visualizes the \"Load-Bearing Capacity\" of the code. We
treat code like physical infrastructure. A bridge is safe not because it
has no cars (complexity), but because it has enough support pillars
(guardrails) to hold the traffic.

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **VERY LOW (Score 0-20, Blue):** Fortified. Defensive structures
(try/catch, guards) vastly outnumber the risks.
-   **INTERMEDIATE (Score 41-60, Yellow):** Stable. Risks and defenses
are roughly balanced.
-   **VERY HIGH (Score 81-100, Red):** Fragile. The structural load
(Risk) exceeds the support capacity (Defenses). The code is liable
to collapse under edge cases.

##### 2.2.G.B. The Inputs (Regex & Heuristics)

We classify patterns into **Attackers** (Risk) and **Defenders**
(Safety).

------------ ------------------ ------------- ------------------------------------------------------------------------------------------
RiskHits     **danger**         4.0x          The Heavy Load. Critical vulnerabilities (**eval**, **exec**) that exert massive stress.
NegHits      **safety_n**eg**   1.5x          The Rust. Anti-patterns (**var**, **any**, suppress) that weaken the structure.
FluxHits     **flux**           0.5x          The Vibration. Mutable state introduces entropy.
SafetyHits   **safety**         1.0x (Base)   The Pillars. Try/catch, assertions, type guards.
TestHits     **test**           0.5x          The Blueprint. Proximity to tests implies verification.
DocHits      **doc**            0.1x          The Warning Labels. Provides a minor structural defense bonus.
------------ ------------------ ------------- ------------------------------------------------------------------------------------------

##### 2.2.G.C. The Universal Framework Integration

-   *Fc*** (Fidelity Coefficient):** Applied to **Defenders**. We trust
a *try/catch* in Java (Explicit) more than a check in Shell
(Implicit).

-   *Irc*** (Implicit Risk Correction):** Added to **Attackers**.
Implicit languages start with a \"Phantom Load\"---a baseline risk
inherent to the medium.

-   *Mp*** (Path Modifier):** Applied to **Attackers**. We keep the
discount small to ensure risks are exposed everywhere.

-   *Exp/Tests (Mp = 0.9):* **Minor Discount.** Risks are slightly
forgiven, but unsafe code will still flash Red.
-   *Core/Auth (Mp = 1.2):* **Amplified.** Risks are punished
heavily. Fragility here is unacceptable.
-   *Standard (Mp = 1.0):* Baseline.

##### 2.2.G.D. The Equation: The Structural Integrity Sigmoid

The math has been entirely rewritten to calculate **Net Exposure**
rather than Integrity Density, and introduces Laplace Smoothing to
prevent tiny files from aggressively skewing the spectrum.

**Step A: Calculate Smoothed Attack & Defense Densities** We sum the
weighted risks and fortifications. Instead of dividing strictly by LOC,
we use **Laplace Smoothing** (*LOC + 20.0*). This prevents a 5-line file
with a single *try/catch* from registering as infinitely safe.

-   **Attack** is amplified by *Irc* (Implicit Risk) and scaled by *Mp*
(Path Context).
-   **Defense** is dampened by *Fc* (Fidelity/Trust).

**Step B: Calculate Net Exposure** *Net Exposure = Attack - Defense*. We
also subtract a minor *systems_buffer* for implicit languages to account
for their naturally looser structures.

-   **Positive Exposure:** Risks outweigh Defenses (Fragile / Red).
-   **Negative Exposure:** Defenses outweigh Risks (Fortified / Blue).

**Step C: The Sigmoid Score & Breach Floor** We map the exposure to a
0-100 scale using a steep Sigmoid slope (*12.0*).

-   **The Breach Floor:** If the code has a high density of explicit
*danger* hits and Attack outpaces Defense, the file is subject to a
hard risk floor (scaling up to 80.0), guaranteeing that catastrophic
structural weaknesses cannot be \"math-ed away\" by simply adding
empty *try/catch* blocks.

##### 2.2.G.E. Implementation (Python Reference)

*import math*

*from typing import Dict*

*def \_calc_safety(self, loc: int, eq: Dict\[str, int\], irc: int, fc:
float, mp: float) -\> float:*

* safe_loc = max(loc, 1)*

* t = self.risk_tuning.get(\"safety\", {})*

* *

* \# 1. Weighted Sums*

* attack_hits = (eq.get(\"danger\", 0) \* t.get(\"danger_weight\",
4.0)) + \\*

* (eq.get(\"safety_neg\", 0) \* t.get(\"safety_neg_weight\", 1.5)) + \\*

* (eq.get(\"flux\", 0) \* t.get(\"flux_weight\", 0.5))*

* *

* defense_hits = (eq.get(\"safety\", 0) \* self.WEIGHT_DEFENSE) + \\*

* (eq.get(\"test\", 0) \* t.get(\"test_weight\", 0.5)) + \\*

* (eq.get(\"doc\", 0) \* t.get(\"doc_weight\", 0.1))*

* *

* if attack_hits == 0:*

* return 0.0*

* *

* \# 2. Laplace Smoothing (+20 LOC) to prevent tiny-file explosions*

* smoothed_loc = safe_loc + t.get(\"laplace_smoothing\", 20.0)*

* *

* attack = ((attack_hits + irc) / smoothed_loc) \* mp*

* defense = (defense_hits / smoothed_loc) \* fc*

* *

* \# 3. Net Exposure Calculation*

* systems_buffer = t.get(\"systems_buffer\", 0.25) if fc \< 1.0 else
0.0*

* net_exposure = (attack - defense) - systems_buffer*

* *

* \# 4. Sigmoid Mapping*

* try:*

* score = 100.0 / (1.0 + math.exp(-t.get(\"sigmoid_slope\", 12.0) \*
net_exposure))*

* except OverflowError:*

* score = 100.0 if net_exposure \> 0 else 0.0*

* \# 5. The Breach Floor (Punishing undefended danger)*

* danger_density = (eq.get(\"danger\", 0) + eq.get(\"safety_neg\", 0)) /
safe_loc*

* if danger_density \> t.get(\"breach_density_min\", 0.03) and attack \>
defense:*

* floor = min(t.get(\"breach_floor_max\", 80.0), 30.0 + (danger_density
\* t.get(\"breach_floor_mult\", 500.0)))*

* score = max(score, floor)*

* *

* return max(score, 0.0)*

##### 2.2.G.F. Visual Verification (\"The Truth\")

---------------------- -------- --------- ----------- -------- -------------- -----------------------------------------------------------------------------
Scenario               Attack   Defense   Net / LOC   Score    Color          Interpretation
**Stable Logic**       5        5         0.0         **50**   **White**      Balanced. Risks matched by guards.
**The Bunker**         2        20        +0.18       **86**   **Cyan**       Highly fortified. Guards vastly outnumber risks.
**Glass Cannon**       20       2         -0.18       **14**   **Red**        Fragile. Heavy risks with no support pillars.
**Experiment (Old)**   20       2         -0.09       **29**   **Pale Red**   *With Mp=0.5*. Risk was hidden/dampened.
**Experiment (New)**   20       2         -0.16       **17**   **Red**        *With Mp=0.9*. Risk is now clearly visible.
**Implicit Script**    5        5         -0.05       **37**   **Pale Red**   *With Irc=5*. Even \"balanced\" code looks fragile due to language opacity.
---------------------- -------- --------- ----------- -------- -------------- -----------------------------------------------------------------------------

#### 2.2.I. Technical Debt Exposure

##### 2.2.I.A. The Philosophy: Markers of Honesty

**\"The Topography of Compromise.\"**

Visualizes the \"Topography of Compromise.\" We view Technical Debt not
as a failure, but as a deliberate engineering trade-off. No engineer
writes a HACK out of laziness; they write it to ship. This metric is
about Honesty. It relies on the developer\'s own annotations (in the
Literature/Comment Stream) to identify where the \"Structural Stress\"
lies. By visualizing these markers, we move from vague anxiety about
\"bad code\" to a concrete map of where the team knows improvements are
needed.

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **VERY LOW (Score 0-20, Blue):** Polished. The code matches the
spec. No known shortcuts.
-   **INTERMEDIATE (Score 41-60, Yellow):** Honest work-in-progress. A
balanced mix of planned tasks.
-   **VERY HIGH (Score 81-100, Red):** Fractured. The file is held
together by temporary fixes (*HACK*) and unfinished thoughts
(*TODO*). It is structurally compromised.

##### 2.2.I.B. The Inputs (Regex & Heuristics)

The regex scanning has been entirely decoupled from the physics engine.
The *blAST* engine now pre-calculates these hits and passes them into
the Signal Processor\'s *eq* dictionary.

--------------- ---------------------------------------- ------ ------------------------------------------------------------------------------------------------------------------------------------------------------
Planned Debt    **planned_debt**                         1.0x   The Promise. Future work that doesn\'t necessarily imply current brokenness. Includes **TODO**, **WIP**, **STUB**, **REFACTOR**.
Fragile Debt    **fragile_debt** (or **keyword_debt**)   3.0x   The Fracture. An explicit admission that the current logic is fragile or dangerous. Includes **HACK**, **FIXME**, **XXX**, **WORKAROUND**, **UGLY**.
Stub Hits       **func_empty**                           0.5x   The Skeleton. Empty functions (**{}**) found in the Logic Stream. Implies placeholder logic independent of comments.
Implicit Risk   **irc**                                  0.5x   The Fog. Implicit languages hide debt better, so we add a weighted baseline load to the stress sum.
--------------- ---------------------------------------- ------ ------------------------------------------------------------------------------------------------------------------------------------------------------

##### 2.2.I.C. The Universal Framework Integration

-   *Fc*** (Fidelity Coefficient):** **Not Applied.** A *TODO* is a
*TODO*, regardless of language.

-   *Irc*** (Implicit Risk Correction):** **Applied.** Added to the
Stress Sum.

-   *Mp*** (Path Modifier):** **Applied.**

-   *Archive/Legacy (Mp = 0.5):* Debt is expected here. Discount it.
-   *Core/Kernel (Mp = 1.2):* Debt here is dangerous. Amplify it.
-   *Scratchpad (Mp = 0.8):* Allow messy thoughts.

##### 2.2.I.D. The Equation: The Structural Stress Density

We calculate the Density of Debt per line of code.

**Step A: Calculate Stress Sum** We sum the markers, applying weights to
distinguish \"Planned Work\" (Good Debt) from \"Broken Logic\" (Bad
Debt). We also add the Implicit Risk Correction (*Irc*), dampened by its
own weight multiplier (*0.5*).

**Step B: Calculate Stress Density** We normalize against the file size
to calculate the stress points per 100 lines. A 1000-line file with 1
*TODO* is fine. A 10-line file with 1 *HACK* is structurally critical.

**Step C: The Sigmoid Map** We use a Sigmoid function to create a
\"Tolerance Threshold\".

-   **Threshold (T):** *5.0*. We tolerate \~5 points of stress per 100
lines before the score spikes.
-   **Slope (K):** *0.5*. A gentle slope allows for nuance as debt
accumulates.

**Step D: Final Calculation** We apply the Path Modifier (*Mp*) to
dampen or amplify the final score based on the file\'s architectural
context.

##### 2.2.I.E. Implementation (Python Reference)

*import math*

*from typing import Dict*

*def \_calc_tech_debt(self, loc: int, eq: Dict\[str, int\], irc: int,
mp: float) -\> float:*

* t = self.risk_tuning.get(\"tech_debt\", {})*

* good_debt = eq.get(\"planned_debt\", 0)*

* bad_debt = eq.get(\"fragile_debt\", eq.get(\"keyword_debt\", 0))*

* stubs = eq.get(\"func_empty\", 0)*

* *

* if good_debt == 0 and bad_debt == 0 and stubs == 0:*

* return 0.0*

* *

* \# Step A: Stress Sum*

* stress = (good_debt \* t.get(\"good_debt_weight\", 1.0)) + \\*

* (bad_debt \* t.get(\"bad_debt_weight\", 3.0)) + \\*

* (stubs \* t.get(\"stub_weight\", 0.5)) + \\*

* (irc \* t.get(\"irc_weight\", 0.5))*

* *

* \# Step B: Density Calculation*

* density = (stress / max(loc, 1)) \* 100.0*

* threshold = t.get(\"threshold\", 5.0)*

* *

* \# Step C: Sigmoid Map*

* try:*

* raw_score = 100.0 / (1.0 + math.exp(-t.get(\"sigmoid_slope\", 0.5) \*
(density - threshold)))*

* except OverflowError:*

* raw_score = 100.0 if density \> threshold else 0.0*

* *

* \# Step D: Apply Context Modifier*

* return min(raw_score \* mp, 100.0)*

##### 2.2.I.F. Visual Verification (\"The Truth\")

---------------- ------ ---------------------------- ------ ------ -------- -------------------------------------------------------------------------------------------------
Clean Core       200    0                            0.0    0      Blue     Pristine. Zero structural stress.
Honest Dev       200    2 **REFACTOR**, 3 **TODO**   2.5    22     Cyan     Good citizenship. Admitting work is needed, but well under the threshold.
The Prototype    100    2 STUBs, 4 **WIP**s          5.0    50     Yellow   Halfway point. Rough but honest.
Frustrated Dev   50     1 **WTF**, 1 **HACK**        12.0   \~97   Red      High emotional and structural stress. Severe technical debt.
Legacy Dump      1000   20 **HARDCODED**             6.0    \~31   Cyan     With Mp=0.5. Large volume and high debt, but heavily discounted because it is marked as legacy.
---------------- ------ ---------------------------- ------ ------ -------- -------------------------------------------------------------------------------------------------

#### 2.2.J. Documentation Risk Exposure (Metric: Sigmoid Debt)

##### 2.2.J.1. The Philosophy: The Duty of Care

Visualizes the \"Duty of Care\" a developer owes to their future self
and the collective. This metric does not reward the raw volume of text;
it measures the Density of Intent. We distinguish between
\"Library-Grade\" engineering---where a component is supported by
structured metadata---and \"Silent Logic,\" which requires the reader to
perform manual mental compilation to understand the *why* behind the
*what*.

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **THOROUGH (Score 0-20, Blue):** Saturated Map. Perfect coverage
with high intent density.
-   **MODERATE (Score 41-60, Yellow):** Functional baseline. Meets
standard safety thresholds.
-   **UNDOCUMENTED (Score 90-100, Red):** Total Opacity. Zero intent
density, representing high maintenance risk.

##### 2.2.J.2. The Inputs (Tiered Efficiency)

The regex scanning has been abstracted out of the physics engine. The
*blAST* engine now pre-calculates documentation lines and structured
hits, passing them into the Signal Processor.

------------- --------------- ------- -------- --------------------------------------------------------------------------------------------------------------------------------------------
Doc Hits      **doc**         1.0x    High     Tier 1 (The Interface). Gold standard tags (**\@param**, **///**). One hit provides a full point of intent density.
Header Hits   **ownership**   0.5x    Medium   Tier 2 (The Metadata). Attribution and file-level summaries. Valuable context, but less critical for line-by-line logic comprehension.
Doc LOC       **doc_loc**     0.33x   Low      Tier 3 (The Narrative). General inline comments. Requires 3 lines of text to equal 1 structured tag, honoring effort but demanding volume.
------------- --------------- ------- -------- --------------------------------------------------------------------------------------------------------------------------------------------

##### 2.2.J.3. The Universal Framework Integration

-   **Fc (Fidelity Coefficient):** Applied to the final risk reduction.
We trust documentation in Explicit languages (e.g., Rust) more than
in Implicit languages (e.g., Shell), where comments are prone to
\"drifting\" from the actual logic.

-   **Irc (Implicit Risk Correction):** Applied to the Threshold.
Implicit languages require a higher \"Opacity Tax.\" They need more
documentation density just to reach a baseline safety level.

-   **Mp (Path Modifier):**

-   **Public/API (Mp = 1.5):** High Bar. This is the face of the
system. Lack of docs here is punished more severely.
-   **Tests/Experiments (Mp = 0.5):** Low Bar. Internal logic is
more \"forgiven\" for being silent.

##### 2.2.J.4. The Equation: The Dynamic Risk Sigmoid

*We calculate the density of intent and map it to a \"Debt Curve\" where
the score represents the Exposure caused by missing documentation.*

**Step A: The Micro-Bypass** Tiny scripts (\<= 2 lines of code) with 0
documentation are automatically granted a *0.0* risk score. A one-line
utility function does not require a map.

**Step B: Calculate Intent Density** We sum the weighted points and
normalize them against the file size (*loc*). A 1000-line file requires
significantly more intent-signaling than a 10-line utility.

**Step C: Determine The Risk Threshold (The Bar)** We calculate the
\"Tipping Point\" where a file transitions from \"Well-Documented\" to
\"High Risk.\" We add the Implicit Risk Correction (*Irc*)---meaning
opaque languages like Shell require a higher density to reach baseline
safety---and multiply by the Path Modifier (*Mp*). For example, public
APIs (high *Mp*) raise the threshold significantly.

**Step D: The Risk Sigmoid Map** We use a sigmoid with a positive
exponent. As Documentation Density increases, the Risk Score
mathematically decreases.

**Step E: Fidelity Trust Multiplier** Finally, we apply the Fidelity
Coefficient (*Fc*). Low-fidelity languages (high *Irc*, low *Fc*) suffer
an inverted trust multiplier, acknowledging that comments in those
languages are more prone to drifting from reality.

##### 2.2.J.5. Implementation (Python Reference)

*import math*

*from typing import Dict*

*def \_calc_documentation(self, loc: int, doc_loc: int, eq: Dict\[str,
int\], fc: float, irc: int, mp: float) -\> float:*

* t = self.risk_tuning.get(\"documentation\", {})*

* *

* \# Step B: Calculate Intent Density*

* weighted_points = (eq.get(\"doc\", 0) \* t.get(\"doc_weight\", 1.0)) +
\\*

* (eq.get(\"ownership\", 0) \* t.get(\"ownership_weight\", 0.5)) + \\*

* (doc_loc \* t.get(\"doc_loc_weight\", 0.33))*

* density = (weighted_points / loc) \* 100.0*

* *

* \# Step A: Micro-bypass for tiny utilities*

* if loc \<= 2 and doc_loc == 0:*

* return 0.0*

* *

* \# Step C: Dynamic Threshold*

* threshold = (t.get(\"threshold_base\", 10.0) + irc) \* mp*

* *

* \# Step D: Sigmoid Map*

* try:*

* raw_risk = 100.0 / (1.0 + math.exp(t.get(\"sigmoid_slope\", 0.2) \*
(density - threshold)))*

* except OverflowError:*

* raw_risk = 0.0 if density \> threshold else 100.0*

* *

* \# Step E: Fidelity Trust Multiplier*

* return min(raw_risk \* (2.0 - fc), 100.0)*

##### 2.2.J.6. Visual Verification (\"The Risk Audit\")

*Comparison: 100 Line File (Threshold 10)*

------------------ ---------------------- ------ ------ -------------------- ----------------------------------------------------------------
The Architect      15 **\@param** tags    15.0   \~27   LOW (Cyan)           Safe. High documentation density results in low risk exposure.
The Professional   10 **\@param** tags    10.0   \~50   MODERATE (Yellow)    Stable. Hits the threshold exactly; moderate exposure.
The Student        10 lines of comments   3.3    \~79   HIGH (Orange)        Risky. Minimal narrative effort fails to clear the safety bar.
The Silent         0 comments             0.0    \~88   UNDOCUMENTED (Red)   Critical. Zero intent density results in high risk exposure.
------------------ ---------------------- ------ ------ -------------------- ----------------------------------------------------------------

#### 2.2.K. File Stability (Commit Heat)

##### 2.2.K.A. The Philosophy

Visualizes the \"Geological Layers\" of the repository. Instead of
measuring \"Freshness\" (which implies old code is bad/stale), we
measure Stability. We use Auto-Scaling Normalization to scan the entire
repository and find the absolute oldest and newest timestamps, creating
a relative timeframe specific to that galaxy.

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **HOT/NEW (Score 0-20, Blue):** The \"Active Front.\" Code written
or heavily modified very recently.
-   **ACTIVE (Score 41-60, Yellow):** Settled. Halfway down the
repository\'s timeline.
-   **ENDURING (Score 81-100, Red):** The \"Foundation.\" The oldest,
most untouched files in the repository.

##### 2.2.K.B. The Inputs (File System)

We use **Auto-Scaling Normalization**. We scan the entire repository to
find the absolute oldest and newest timestamps, creating a relative
time-frame for this specific galaxy.

----------------- ----------------------- ------- --------------------------------------------------------
Input Variable    Source                  Unit    Rationale
**FileMTime**     *os.path.getmtime*      Epoch   The last modified timestamp of the specific file.
**RepoMinTime**   *Calculated (Pass 1)*   Epoch   The timestamp of the *oldest* file in the entire repo.
**RepoMaxTime**   *Calculated (Pass 1)*   Epoch   The timestamp of the *newest* file in the entire repo.
----------------- ----------------------- ------- --------------------------------------------------------

##### 2.2.K.C. The Universal Framework Integration

Stability is a pure temporal measurement. It is not a risk factor that
requires dampening or amplification.

-   **Fc (Fidelity Coefficient):** Not Applied. Time is absolute.
-   **Irc (Implicit Risk Correction):** Not Applied.
-   **Mp (Path Modifier):** Not Applied. The age of a file is a physical
constant.

##### 2.2.K.D. The Equation: Relative Time Normalization

We define Stability as the \"Distance from the Newest moment.\"

**Step A: Calculate Temporal Distance** We subtract the file\'s last
modified time (*mtime*) from the newest moment in the repository
(*repo_max*). We clamp this difference to *0.0* at a minimum to prevent
negative time errors if a file\'s timestamp somehow drifts ahead of the
global max during processing.

**Step B: Calculate Relative Ratio** We divide the file\'s temporal
distance by the total time range of the repository. We enforce a minimum
range of *1.0* second to prevent division-by-zero crashes in brand-new
or single-file repositories.

-   If *FileTime == RepoMaxTime* (Newest), the distance is *0*, so
*Stability = 0.0*.
-   If *FileTime == RepoMinTime* (Oldest), the distance equals the full
range, so *Stability = 100.0*.

##### 2.2.K.E. Implementation (Python Reference)

*from typing import Dict, Tuple*

*def \_calc_raw_temporal_signals(self, temp: Dict\[str, Any\]) -\>
Tuple\[float, float\]:*

* \"\"\"Calculates Stability (Age) and Raw Churn (Seismic
Frequency).\"\"\"*

* if not temp or not temp.get(\"is_git_tracked\", False):*

* return 50.0, 0.0 *

* mtime = temp.get(\"mtime\", 0.0)*

* repo_min = temp.get(\"repo_min_time\", mtime)*

* repo_max = temp.get(\"repo_max_time\", mtime)*

* commits = temp.get(\"commit_count\", 0)*

* \# \-\--\> THE FIX: Clamp the time difference so it never goes
negative \<\-\--*

* seconds_from_max = max(repo_max - mtime, 0.0)*

* time_range = max(repo_max - repo_min, 1.0)*

* *

* \# 1. Stability (0 = Newest/Surface, 100 = Oldest/Bedrock)*

* stability_ratio = seconds_from_max / time_range*

* stability_score = min(stability_ratio \* 100.0, 100.0)*

* \# 2. Raw Churn Frequency (Calculated alongside stability)*

* age_weeks = max(seconds_from_max / 604800.0, 1.0) *

* raw_churn_freq = commits / math.sqrt(age_weeks)*

* *

* return stability_score, raw_churn_freq*

##### 2.2.K.F. Visual Verification (\"The Truth\")

**Scenario:** A project started on Jan 1st (*Min*) and released on Dec
31st (*Max*). Range = 365 Days.

------------------- ------------------ ------------ ----------- ----------------- --------------------------------------------
**NewFeature.ts**   Dec 31st (Today)   0 Days       **0.0**     HOT/NEW (Blue)    New. The active surface layer.
**MidYear.ts**      July 1st           \~182 Days   **50.0**    ACTIVE (Yellow)   Settled. Halfway down the timeline.
**Init.ts**         Jan 1st (Start)    365 Days     **100.0**   ENDURING (Red)    Foundation. The oldest rock in the strata.
------------------- ------------------ ------------ ----------- ----------------- --------------------------------------------

#### 2.2.L. Test Coverage (Metric: Verification Density)

##### 2.2.L.A. The Philosophy: Trust vs. Verification

****Visualizes the \"Security Blanket\" of the codebase. In GitGalaxy,
we distinguish between Defensive Code (handling errors at runtime) and
Verified Code (proving correctness at design time). Because this metric
has been unified into the Risk Exposure model, a high score now
indicates a *****lack***** of verification (high risk), while a low
score indicates ironclad, verified code.****

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **IRONCLAD (Score 15-20, Blue):** Fortified. The code is heavily
backed by internal assertions, mocks, or a dedicated sibling test
suite. *(Note: The physics engine enforces a hard minimum floor of
15.0, acknowledging that no code is 100% perfectly safe).*
-   **MODERATE (Score 41-60, Yellow):** Partial verification. Meets the
bare minimum threshold.
-   **VERY HIGH (Score 81-100, Red):** Speculative. The code might work,
but there is no programmatic proof. It relies entirely on hope.

##### 2.2.L.B. The Inputs (Verification Signals)

We combine internal evidence (assertions) with external evidence
(sibling files). The file system checks are now abstracted, passing an
*is_protected* boolean directly to the physics engine.

---------------- ------------------ -------------- -------------------------------------------------------------------------------------------------------------------------------------------
Internal Tests   **test**           5.0x           Assertions, mocks, and test definitions inside the file itself.
Sibling Match    **is_protected**   +30.0 (Flat)   External Coverage. Indicates a **X.test.js** or **X_spec.rb** exists next to **X.js**. This flat density bonus represents strong intent.
Mass Penalty     **loc \> 300**     Variable       Monoliths (files over 300 lines) gain a stacking risk penalty up to +40. Massive files cannot be adequately verified by unit tests alone.
---------------- ------------------ -------------- -------------------------------------------------------------------------------------------------------------------------------------------

##### 2.2.L.C. The Universal Framework Integration

**Exemptions:** Untestable files (e.g., Markdown, Makefiles, CMake, or
specific extensions configured in the asset masks) bypass the engine
entirely, returning *0.0* risk.

-   **Fc (Fidelity Coefficient):** Applied as an inverted multiplier
(*2.0 - Fc*). We trust explicit verification in high-fidelity
languages more than loose assertions in implicit languages.

```{=html}
<!-- -->
```
-   **Irc (Implicit Risk Correction):** Added to the Threshold. Implicit
languages (Python, Ruby) rely entirely on tests for type safety,
meaning they require a *higher* density of tests to clear the risk
bar.

```{=html}
<!-- -->
```
-   **Mp (Path Modifier):** Scales the Threshold. Critical
infrastructure (*core/*) gets a higher bar; notoriously hard-to-test
views (*UI/*) get a lower bar.

##### 2.2.L.D. The Equation: The Verification Sigmoid

**Step A: The Exemption Bypass** If the file matches known untestable
patterns (e.g., *readme*, *makefile*), the engine immediately returns
*0.0*.

**Step B: Calculate Verification Density** We calculate the density of
internal tests (*test hits \* 5.0 / LOC*) and add the flat Sibling Bonus
(*+30.0*). The bonus is added directly to density because the existence
of a test file implies coverage of the whole module.

**Step C: Determine The Bar (Dynamic Threshold)** This is the \"Passing
Grade\" the density must overcome to lower the risk score. *Threshold =
(15.0 + (Irc \* 3.0)) \* Mp*.

**Step D: The Inverse Sigmoid Map** We map density against the dynamic
threshold using a positive exponent. As Verification Density
*increases*, the Risk Exposure mathematically *decreases*.

**Step E: Trust Adjustment & Mass Penalty** We multiply the result by
the inverted Fidelity score (*2.0 - Fc*). If the file size exceeds the
*MASSIVE_FILE_THRESHOLD* (300 lines), we calculate and add a structural
mass penalty, capping the final calculation between the *15.0* risk
floor and *100.0* maximum.

##### 2.2.L.E. Implementation (Python Reference)

*import math*

*import os*

*from typing import Dict*

*def \_calc_verification(self, loc: int, file_path: str, is_protected:
bool, eq: Dict\[str, int\], irc: int, fc: float, mp: float,
umbrella_bonus: float = 0.0) -\> float:*

* filename = os.path.basename(file_path).lower()*

* ext = filename.split(\'.\')\[-1\] if \'.\' in filename else \"\"*

* *

* exempt_exts = self.asset_masks.get(\"UNTESTABLE_EXTENSIONS\", set())*

* exempt_names = self.asset_masks.get(\"UNTESTABLE_NAMES\", set())*

* *

* \# Step A: Untestable Bypass*

* if ext in exempt_exts or filename in exempt_names or
filename.startswith(\'readme\') or \'makefile\' in filename or \'cmake\'
in filename:*

* return 0.0*

* t = self.risk_tuning.get(\"verification\", {})*

* safe_loc = max(loc, 1)*

* *

* \# Step B: Verification Density*

* sibling_bonus = t.get(\"sibling_bonus\", 30.0) if is_protected else
0.0*

* internal_density = (eq.get(\"test\", 0) \*
t.get(\"internal_test_mult\", 5.0) / safe_loc) \* 100.0*

* total_density = internal_density + sibling_bonus *

* *

* \# Step C: Dynamic Threshold*

* threshold = (t.get(\"threshold_base\", 15.0) + (irc \*
t.get(\"irc_mult\", 3.0))) \* mp*

* *

* \# Step D: Inverse Sigmoid Map*

* try:*

* raw_exposure = 100.0 / (1.0 + math.exp(t.get(\"sigmoid_slope\", 0.25)
\* (total_density - threshold)))*

* except OverflowError:*

* raw_exposure = 0.0 if total_density \> threshold else 100.0*

* *

* \# Step E: Trust Adjustment*

* final_exposure = raw_exposure \* (2.0 - fc)*

* \# Step F: The Mass Penalty*

* if safe_loc \> self.MASSIVE_FILE_THRESHOLD:*

* mass_penalty = min((safe_loc - self.MASSIVE_FILE_THRESHOLD) /
t.get(\"mass_penalty_div\", 20.0), t.get(\"mass_penalty_max\", 40.0)) *

* final_exposure += mass_penalty*

* \# Enforce the 15.0 Risk Floor*

* return min(max(final_exposure, t.get(\"risk_floor\", 15.0)), 100.0)*

* *

##### 2.2.L.F. Visual Verification (\"The Truth\")

**Comparison: 100 Line File (Base Threshold 15)**

**

---------------- --------------------- --------------- ------------ ------------------- ----------------------------------------------------------------------------------------------------------------------------------------------
The Test File    20 internal asserts   N/A             **15.0**     IRONCLAD (Blue)     High internal density drops exposure to the absolute risk floor.
Paired Source    0 asserts             Yes             **\~15.0**   IRONCLAD (Blue)     Covered by sibling. The flat +30 density bonus clears the threshold easily.
Defensive Code   3 asserts             No              **\~50.0**   MODERATE (Yellow)   Internal checks meet the bare minimum threshold.
The Orphan       0 asserts             No              **100.0**    VERY HIGH (Red)     Unverified. No internal checks, no sibling coverage.
The Monolith     0 asserts             Yes (Sibling)   **\~45.0**   MODERATE (Yellow)   A 900-line file *with* a sibling test. The mass penalty overrides the sibling bonus, preventing massive files from hiding behind thin tests.
---------------- --------------------- --------------- ------------ ------------------- ----------------------------------------------------------------------------------------------------------------------------------------------

**

#### 2.2.M. The \"Civil War\" Algorithm: Tabs vs. Spaces

-   ****Visual Mapping:****

-   ****Score 0 (Pure Tabs):**** Visual: ****Glowing Green****
(#00FF00). Emissive intensity is maxed.
-   ****Score 100 (Pure Spaces):**** Visual: ****Glowing Yellow****
(#FFFF00). Emissive intensity is maxed.
-   ****Score 50 (Maximum Conflict):**** Visual: ****Deep Blue****
(#0000FF). 50/50 split triggers the \"Bifurcation Shimmer\"
(geometry flickering).
-   ****Gradient:**** Linear transition from Green (0) → Blue (50) →
Yellow (100).

-   ****Equation:****

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

-   ****Range:**** **0** (Pure Tabs) to **100** (Pure Spaces).

-   ****Why this works:**** This is a ****Linear Polarization Model****.

-   ****Terminology:**** While colloquially referred to as \"Civil
War,\" the equation measures ****Layout Unity****.
-   ****Logic:**** By mapping Tabs to 0 and Spaces to 100, the \"War
Zone\" (50/50 mix) naturally sits at the center of the spectrum
(Score 50).

#### 2.2.N. The \"Graveyard\" Detector (Metric: Architectural Transparency)

##### 2.2.N.A. The Philosophy: \"The Fear of Deletion.\"

Visualizes \"Code Necrosis\" or \"The Fear of Deletion.\" Commented-out
code (\"Ghost Logic\") is not documentation; it is hesitation. It
implies a lack of trust in Version Control. It creates cognitive noise,
forcing the reader to mentally parse and discard logic that is no longer
active.

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **CLEAN (Score 0-20, Blue):** Active, clean, executed. Pure life.
-   **INTERMEDIATE (Score 41-60, Yellow):** Minor scraps. Tolerable
depending on the context.
-   **GRAVEYARD (Score 81-100, Red):** Heavily polluted with dead
blocks. The file is \"Haunted\" by its past.

##### 2.2.N.B. The Inputs (Heuristic Detection)

We distinguish between Documentation (English text) and Graveyards
(Inactive Code) by scanning for syntax density within comment blocks.
The backend now calculates the raw blocks, and the physics engine
extrapolates the lines.

---------------- --------------- ------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------
Graveyard Hits   **graveyard**   3.0x          The backend identifies blocks of dead code. The physics engine assumes an average of 3 lines of ghost logic per block hit to estimate the total necrotic mass.
Total LOC        **total_loc**   Denominator   We measure density against the absolute size of the file, not just the active logic.
---------------- --------------- ------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------

##### 2.2.N.C. The Universal Framework Integration

-   *Fc*** (Fidelity Coefficient):** **Not Applied.** Dead code is
language-agnostic.

-   *Irc*** (Implicit Risk Correction):** **Not Applied.**

-   *Mp*** (Path Modifier):** **Applied to Threshold.**

-   *Experiments/Scratch (Mp = 2.0):* **High Tolerance.** It is
acceptable to keep snippets while prototyping.
-   *Core/Kernel (Mp = 0.5):* **Zero Tolerance.** Production
architecture must be clean.
-   *Legacy (Mp = 1.5):* **Moderate Tolerance.** We expect some rot
in the archives.

##### 2.2.N.D. The Equation: The Necrosis Sigmoid

*We calculate the density of dead code and map it to a curve that
forgives minor \"scraps\" but punishes \"hoarding.\"*

**Step A: The Clean File Bypass** If there are zero graveyard hits, the
engine immediately returns a *0.0* risk score to save processing time.

**Step B: Calculate Necrosis Density** We estimate the total
*ghost_lines* by multiplying the graveyard hits by *3.0*. We then divide
this by the file\'s *total_loc*.

-   **The Safe Mass Floor:** To prevent a 5-line script with a single
commented-out line from instantly registering as 60% necrotic, we
enforce a minimum file mass of *50.0* lines for the density
calculation.

**Step C: Determine The Tolerance (Dynamic Threshold)** This is the
\"Tipping Point\" where the file is considered \"Haunted.\"

-   **Base:** *10.0* (We tolerate up to 10% dead code before the score
spikes).
-   **Context Scaling:** The threshold is divided by the Path Modifier
(*Mp*). Therefore, if a file is in the *core/* (high *Mp* punishing
risk), the tolerance threshold drops. If it is in *experiments/*
(low *Mp* forgiving risk), the tolerance threshold rises.

**Step D: The Sigmoid Map** We map density against the threshold using a
slope of *0.3*, which creates a smooth transition from \"Clean\" to
\"Haunted\".

##### 2.2.N.E. Implementation (Python Reference)

*import math*

*from typing import Dict*

*def \_calc_graveyard(self, total_loc: float, eq: Dict\[str, int\], mp:
float) -\> float:*

* \# Step A: Clean File Bypass*

* hits = eq.get(\"graveyard\", 0)*

* if hits == 0:*

* return 0.0*

* *

* t = self.risk_tuning.get(\"graveyard\", {})*

* *

* \# Step B: Calculate Necrosis Density*

* ghost_lines = hits \* t.get(\"hit_mult\", 3.0)*

* \# Safe Mass Floor prevents micro-files from exploding in density*

* density = (ghost_lines / max(total_loc, t.get(\"safe_mass_floor\",
50.0))) \* 100.0*

* *

* \# Step C: Dynamic Threshold *

* threshold = t.get(\"threshold_base\", 10.0) / max(mp, 0.1) *

* *

* \# Step D: Sigmoid Map*

* try:*

* score = 100.0 / (1.0 + math.exp(-t.get(\"sigmoid_slope\", 0.3) \*
(density - threshold)))*

* except OverflowError:*

* score = 100.0 if density \> threshold else 0.0*

* *

* return min(score, 100.0)*

##### 2.2.N.F. Visual Verification (\"The Truth\")

**Comparison: 200 Line File**

--------------- ------ ----- ---------------- -------- ------------ ----------------------- --------------------------------------------------------------------
Clean Core      0      0%    Core (1.2)       \~8.3%   **0.0**      CLEAN (Blue)            Pure life. No dead code found.
Standard Dev    \~10   5%    Standard (1.0)   10.0%    **\~18.0**   CLEAN (Blue)            Minor scraps. Fully tolerated beneath the threshold.
Haunted Core    \~20   10%   Core (1.2)       \~8.3%   **\~62.0**   HIGH (Orange)           10% is tolerated elsewhere, but \"Haunted\" in a strict core path.
The Hoarder     \~40   20%   Standard (1.0)   10.0%    **\~95.0**   GRAVEYARD (Red)         20% dead code is clearly necrotic.
The Prototype   \~40   20%   Exp (0.5)        20.0%    **50.0**     INTERMEDIATE (Yellow)   High necrosis, but the experimental context safely allows it.
--------------- ------ ----- ---------------- -------- ------------ ----------------------- --------------------------------------------------------------------



#### 2.2.O. API Exposure (Metric: The Event Horizon)

##### 2.2.O.A. The Philosophy: The Event Horizon

****Visualizes \"The Surface Area of Logic.\" Every module has an Event
Horizon: the boundary between its internal mechanics and the outside
world. API Exposure measures how permeable this boundary is. This metric
allows developers to instantly distinguish heavily exposed interfaces
from internal utility code.****

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **VERY LOW (Score 0-20, Blue):** Internal Vault. The logic is
encapsulated. It exists to support other code but does not offer a
public face.
-   **MODERATE (Score 41-60, Yellow):** Standard exposure. A healthy mix
of public and private methods.
-   **VERY HIGH (Score 81-100, Red):** Public Quasar. The module exists
primarily to be consumed by others. It broadcasts a massive volume
of functionality to the galaxy.

##### 2.2.O.B. The Inputs (Surface Detection)

We compare the count of **Public Signatures** against the **Total
Definitions** to calculate the ratio of exposure. We explicitly sum
Functions and Classes to get the total \"Entity Count.\"

----------------------- ------------------------------ ----------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Input Variable          Regex Key                      Weight            Rationale
**ApiHits**             *api*                          **Numerator**     **The Broadcast.** Keywords that explicitly expose logic: *export*, *public*, *module.exports*, or capitalization rules (Go/Python).
**TotalDeclarations**   *func_start* + *class_start*   **Denominator**   **The Mass.** The total count of logical units (Functions + Classes). We need to sum both regex hits to ensure we don\'t undercount files that define many classes/structs but few methods.
----------------------- ------------------------------ ----------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##### 2.2.O.C. The Universal Framework Integration

-   *Fc*** (Fidelity Coefficient):** **Not Applied.** Public is public.

-   *Irc*** (Implicit Risk Correction):** **Not Applied.** The concept
of \"Public Ratio\" is language-agnostic.

-   *Mp*** (Path Modifier):** **Applied to Score (Amplifier).**

-   *API/Public (Mp = 1.2):* **Amplify.** We want these files to
shine brighter. They are the intended entry points.
-   *Internal/Private (Mp = 0.8):* **Dampen.** We want these to
remain background noise unless they are egregiously leaking.

##### 2.2.O.D. The Equation: Linear Surface Density

We calculate a compound score that balances the direct percentage of
public logic (Ratio) with the sheer quantity of exposed endpoints
(Volume).

**Step A: The Encapsulation Bypass** If the file has zero *api* hits, it
is perfectly encapsulated. The engine returns *0.0* immediately.

**Step B: Calculate Exposure Ratio (40% Weight)** We determine what
percentage of the file\'s defined logic is accessible from the outside
(*api_hits / total_entities*). We clamp the ratio to *1.0* to handle
rare edge cases where heuristics might over-count exports.

**Step C: Calculate Logarithmic Volume (60% Weight)** A file exposing
100 endpoints is structurally more impactful than a file exposing 1
endpoint. We calculate *log10(api_hits + 1)* divided by a dampening
divisor (*1.5*) to curve the volume impact, clamping it at *1.0*.

**Step D: Compound Score & Context Adjustment** We blend the Ratio and
Volume using their respective weights (*0.4* and *0.6*), scale to
*100.0*, and apply the Path Modifier (*Mp*) to highlight intended APIs
and dampen internal utilities.

##### 2.2.O.E. Implementation (Python Reference)

*import math*

*from typing import Dict*

*def \_calc_api_exposure(self, eq: Dict\[str, int\], mp: float) -\>
float:*

* \# Step A: Encapsulation Bypass*

* api_hits = eq.get(\"api\", 0)*

* if api_hits == 0:*

* return 0.0*

* *

* t = self.risk_tuning.get(\"api_exposure\", {})*

* entities = max(eq.get(\"func_start\", 0) + eq.get(\"class_start\", 0),
1)*

* *

* \# Step B: Exposure Ratio*

* ratio = min(api_hits / float(entities), 1.0)*

* *

* \# Step C: Logarithmic Volume*

* volume_weight = min(math.log10(api_hits + 1) / t.get(\"log_divisor\",
1.5), 1.0)*

* *

* \# Step D: Compound Score & Modifier*

* raw_score = ((ratio \* t.get(\"ratio_weight\", 0.4)) + (volume_weight
\* t.get(\"volume_weight\", 0.6))) \* 100.0*

* *

* return min(raw_score \* mp, 100.0)*

##### 2.2.O.F. Visual Verification (\"The Truth\")

**Comparison: 20 Entity File (Functions + Classes)**

---------------- ---- ------ ---------------- ---------- ------------------- -------------------------------------------------------------------------------------------------
The Utility      2    10%    Internal (0.8)   **\~18**   VERY LOW (Blue)     Mostly private helpers. Correctly dim.
The Leaky Core   8    40%    Internal (0.8)   **\~43**   MODERATE (Yellow)   Moderate exposure in an internal folder. Visible, but dampened because it shouldn\'t be public.
The Interface    10   50%    API (1.2)        **\~74**   HIGH (Orange)       Half the file is public. Amplified heavily because it is a designated entry point.
The Library      20   100%   Standard (1.0)   **\~93**   VERY HIGH (Red)     Pure public interface broadcasting maximum volume.
---------------- ---- ------ ---------------- ---------- ------------------- -------------------------------------------------------------------------------------------------

****

#### 2.2.P. Concurrency Exposure

##### 2.2.P.A. The Philosophy:

Visualizes \"Temporal Static\" and the Signal-to-Noise Ratio of a file.
Concurrency is treated as \"Information Static\" because it fractures
the linear execution timeline, increasing the cognitive load required to
understand the file. The Tiger in the Cage rule applies here: We do not
discount concurrency just because it lives in a \"Worker\" or \"API\"
folder. A tiger in a cage is still dangerous. High concurrency is always
high cognitive load and high risk, regardless of where it lives.

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **LOW (Score 0-20, Blue):** Linear. The code executes sequentially
(1, then 2, then 3). The signal is clear and stable.
-   **MODERATE (Score 21-50, Yellow):** Standard async operations. Minor
temporal branching.
-   **VERY HIGH (Score 81-100, Red):** Noisy. The code manages multiple
parallel timelines (Promises, threads, channels). The signal is
highly fractured, warning that execution timing is
non-deterministic.

##### 2.2.P.B. The Inputs (Temporal Markers)

We count the keywords that \"Fork\" time.

---------------- ------------------ ----------------- -----------------------------------------------------------------------------------------------------------------------------------------------
Input Variable   Regex Key          Weight            Rationale
**AsyncHits**    *concurrency*      **1.0x**          **The Fork.** Keywords that spawn or manage parallel execution: *async*, *await*, *Promise*, *thread*, *spawn*, *go*, *chan*, *synchronized*.
**LOC**          *meaningful_loc*   **Denominator**   We measure density. A 1000-line file with 1 *await* is linear. A 10-line file with 5 *await*s is a temporal knot.
---------------- ------------------ ----------------- -----------------------------------------------------------------------------------------------------------------------------------------------

##### 2.2.P.C. The Universal Framework Integration

-   *Fc*** (Fidelity Coefficient):** **Not Applied.** Time is absolute.

-   *Irc*** (Implicit Risk Correction):** **Applied to Numerator
(Dampened).** Implicit languages (JS, Python) hide race conditions
better than explicit ones (Rust, Go). We add a small \"Ghost Load\"
to density, but we scale it down (*Irc \* 0.1*) so it acts as a
\"Tie Breaker\" rather than a false positive generator.

-   *Mp*** (Path Modifier):** **Applied to Threshold.**

-   *UI/Views (Mp = 0.5):* **Low Tolerance (High Scream).** Async
logic in UI code is a primary source of bugs (race conditions,
jank). We lower the bar so even minor concurrency glows here.
-   *Standard/Workers (Mp = 1.0):* **Standard Tolerance.** We do NOT
discount workers. If a worker is complex, it should look
complex.

##### 2.2.P.D. The Equation: The Tipping Point Sigmoid

Concurrency complexity is non-linear. A single *await* is standard. Ten
*await* calls in a small function is a \"Logic Tangle.\" We use a
Sigmoid to create a visual \"Tipping Point.\"

Step 1: Pre-Filter (The Zero Check)

If the file contains **Zero** async hits, the score is **0**. No amount
of implicit risk can turn synchronous code into concurrent code.

*If AsyncHits == 0 -\> Score = 0*

Step 2: Calculate Temporal Density

We determine what percentage of the code is dedicated to managing time.
We add a *fraction* of *Irc* (0.1x) to penalize implicit safety gaps
without creating noise.

*Density = ((AsyncHits + (Irc \* 0.1)) / max(MeaningfulLOC, 1)) \* 100*

Step 3: Determine The Threshold (The Breakdown)

This is the density required to \"Fracture\" the signal.

-   **Base:** 4.0 (4% density). This provides a safe buffer for standard
async patterns before triggering warnings.
-   **Context:** Scaled by *Mp*. In UI (*Mp=0.5*), the threshold drops
to 2.0%.

*Threshold = 4.0 \* Mp*

Step 4: The Sigmoid Map

We map density against the threshold.

-   **Slope (K):** **0.4**. A moderately steep slope. Concurrency risk
escalates quickly.

*RawScore = 100 / (1 + e\^(-0.4 \* (Density - Threshold)))*

Step 5: Final Clamp

*FinalScore = min(RawScore, 100)*

##### 2.2.P.E. Implementation (Python Reference)

*import math*

*def calculate_concurrency_exposure(self, hits_async, loc, irc, mp):*

* \"\"\"*

* Calculates 2.2.P Concurrency Exposure (Temporal Static).*

* Returns int 0-100.*

* \"\"\"*

* \# 1. Step A: Pre-Filter (Zero Check)*

* if hits_async == 0:*

* return 0*

* \# 2. Step B: Temporal Density*

* \# Scaled Irc (0.1x) prevents false positives in small files*

* weighted_hits = hits_async + (irc \* 0.1)*

* density = (weighted_hits / max(loc, 1)) \* 100*

* \# 3. Step C: Dynamic Threshold*

* \# Base = 4% density.*

* \# UI (Mp 0.5) -\> Threshold 2.0%.*

* \# Workers/Standard (Mp 1.0) -\> Threshold 4.0%.*

* path_mod = mp.get(\'Concurrency Exposure\', 1.0)*

* threshold = 4.0 \* path_mod*

* \# 4. Step D: Sigmoid Map*

* try:*

* raw_score = 100 / (1 + math.exp(-0.4 \* (density - threshold)))*

* except OverflowError:*

* raw_score = 100 if density \> threshold else 0*

* return int(min(raw_score, 100))*

##### 2.2.P.F. Visual Verification (\"The Truth\")

**Comparison: 100 Line File**

------------------ ------ ------- ---------------- ------ ------------ ------------------- ---------------------------------------------------------------------------------------------
Synchronous Code   0      0.0%    Any              4.0%   **0.0**      LOW (Blue)          Zero hits = Zero score. Linear and safe.
Standard Async     \~4    4.5%    Standard (1.0)   4.0%   **\~55.0**   MODERATE (Yellow)   The tipping point. Just crossing the threshold.
The UI Tangle      \~5    5.5%    UI (0.5)         2.0%   **\~80.0**   HIGH (Orange)       Moderate async in UI triggers a high warning.
The Worker         \~10   10.5%   Worker (1.0)     4.0%   **\~93.0**   VERY HIGH (Red)     High density. Even though it\'s a worker, it is objectively complex. Correctly glowing red.
------------------ ------ ------- ---------------- ------ ------------ ------------------- ---------------------------------------------------------------------------------------------



#### 2.2.Q. State Flux Exposure

##### 2.2.Q.A. The Philosophy:

*Visualizes \"Data Volatility.\" State Flux measures the Density of
Mutation. It answers the question: \"How stable is the data in this
file?\" The Tiger in the Cage rule applies: we do not dampen the signal
for state management folders (**store/**, **reducers/**). A file
dedicated to mutating state is a high-flux file and should glow
red/orange to reflect its nature as a volatility engine.*

**Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.

-   **VERY LOW (Score 0-20, Blue):** Frozen. Variables are defined once
and rarely changed. The logic is predictable and referentially
transparent.
-   **MODERATE (Score 41-60, Yellow):** Warming. Standard levels of
local state management and loop counters.
-   **VERY HIGH (Score 81-100, Red):** Boiling. Variables are constantly
reassigned, properties are updated, and side effects are triggered.
The data state is in constant flux, making it difficult to track
\"who changed what and when\".

##### 2.2.Q.B. The Inputs (Mutation Markers)

We count the keywords that imply reassignment or side effects. The
*blAST* engine pre-calculates these and passes them to the Signal
Processor.

----------- ---------- ------------- -------------------------------------------------------------------------------------------------------------------------------------
Flux Hits   **flux**   1.0x          The Change. Keywords that mutate data: **let**, **var**, **mut**, **setState**, **reassign**, **push**, **pop**, **+=**, **=**.
Total LOC   **loc**    Denominator   We measure density. A loop counter **i++** in a 1000-line file is negligible. 50 setters in a 100-line file is a \"Boiling\" class.
----------- ---------- ------------- -------------------------------------------------------------------------------------------------------------------------------------

##### 2.2.Q.C. The Universal Framework Integration

-   **Fc (Fidelity Coefficient):** Not Applied. Mutation is an absolute
action.
-   **Irc (Implicit Risk Correction):** Applied to the Numerator
(Dampened). Implicit languages (JS, Python) default to mutability.
We add a small \"Ghost Load\" (*Irc \* 0.15*) to the density. This
acts as a tie-breaker, pushing implicit code slightly higher on the
volatility scale than explicit immutable languages for the same
operation count.
-   **Mp (Path Modifier):** Applied to the Threshold.
-   **UI/Views (Mp = 0.8):** Low Tolerance. Heavy internal state
mutation in UI components (*setState* spaghetti) is a prime source
of bugs. We lower the bar to highlight this risk.
-   **Standard/Store (Mp = 1.0):** Standard Tolerance. We accept that
Stores exist to mutate data. We let them show their true colors
without artificial dampening.

##### 2.2.Q.D. The Equation: The Mutation Threshold Sigmoid

*Most code requires some local mutation (e.g., loop counters). We use a
Sigmoid curve to ignore this background noise but react sharply once
mutation becomes a structural pattern.*

**Step A: Pre-Filter (The Zero Check)** If the file contains zero *flux*
hits, the score is *0.0*.

**Step B: Calculate Volatility Density** We determine what percentage of
the code involves changing data, adding the dampened *Irc* penalty
(*0.15* multiplier).

**Step C: Determine The Threshold (The Boiling Point)** This is the
density required to \"Boil\" the file.

-   **Base:** *15.0* (15% density). This safely absorbs standard loop
and local variable declarations before triggering warnings.
-   **Context:** Scaled by *Mp*. If *Mp* is *0.8* (UI), the threshold
drops to *12.0%*.

**Step D: The Sigmoid Map** We map density against the threshold using a
relaxed slope (*0.20*), creating a smooth curve that ramps up as
mutation becomes dominant.

##### 2.2.Q.E. Implementation (Python Reference)

*import math*

*from typing import Dict*

*def \_calc_state_flux(self, loc: int, eq: Dict\[str, int\], irc: int,
mp: float) -\> float:*

* \# Step A: Pre-Filter*

* hits = eq.get(\"flux\", 0)*

* if hits == 0: *

* return 0.0*

* *

* t = self.risk_tuning.get(\"state_flux\", {})*

* *

* \# Step B: Volatility Density (with 0.15 IRC dampener)*

* density = ((hits + (irc \* t.get(\"irc_mult\", 0.15))) / max(loc, 1))
\* 100.0*

* *

* \# Step C: Dynamic Threshold*

* threshold = t.get(\"threshold_base\", 15.0) \* mp*

* *

* \# Step D: Sigmoid Map*

* try:*

* score = 100.0 / (1.0 + math.exp(-t.get(\"sigmoid_slope\", 0.20) \*
(density - threshold)))*

* except OverflowError:*

* score = 100.0 if density \> threshold else 0.0*

* *

* return min(score, 100.0)*

##### 2.2.Q.F. Visual Verification (\"The Truth\")

**Comparison: 100 Line File**

------------------ ------ -------- ---------------- ------- ------------ ------------------- ---------------------------------------------------------------------------
Pure Functional    0      0.0%     Any              15.0%   **0.0**      VERY LOW (Blue)     Zero hits = Zero score. Predictable and stable.
Standard Logic     \~3    3.0%     Standard (1.0)   15.0%   **\~8.0**    VERY LOW (Blue)     Local loops/vars. Well below the boiling point.
Implicit Script    \~14   14.75%   Standard (1.0)   15.0%   **\~48.0**   MODERATE (Yellow)   With **Irc=5**. The implicit penalty pushes it toward the tipping point.
The UI Spaghetti   \~15   15.0%    UI (0.8)         12.0%   **\~64.0**   HIGH (Orange)       Heavy state changes in UI. The dampened threshold makes it scream louder.
The Redux Store    \~20   20.0%    Store (1.0)      15.0%   **\~73.0**   HIGH (Orange)       High flux. Correctly identified as a volatile state engine.
------------------ ------ -------- ---------------- ------- ------------ ------------------- ---------------------------------------------------------------------------
