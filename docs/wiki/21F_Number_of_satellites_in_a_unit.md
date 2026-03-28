#### 2.1.F Number of satellites in a unit

**Metric**: ****Extended Cyclomatic Complexity**** Visualizes the
\"Knotty\" nature of logic. High cognitive load manifests as dense,
recursive fractals or clusters of satellites.

**Input**: ****C**** (Composite Complexity Score), defined in depth
below.

**Effect**:

-   3D: Number of satellites in satellite/function unit.

##### 2.1.F.1. The Philosophy: Cognitive Friction

Computers don\'t care about *try/catch* blocks or nested *if*
statements; they execute them in nanoseconds. Humans, however, have
limited working memory. Every time a developer reads an *if*, a loop, or
an error handler, they have to \"fork\" their mental model of what the
code is doing. We call this ****Cognitive Friction****.

In GitGalaxy, we visualize this friction physically. A simple, linear
script grows like a straight bamboo shoot. A complex, defensive,
branching function grows like a dense, thorny thicket.

##### 2.1.F.2. The Inputs: Anatomy of Complexity

To calculate this, we look at two distinct types of code patterns found
by the scanner:

-   **A. Structural Complexity (The Skeleton)**

-   **What it is:** The actual decision points in the logic.
-   **Variables Used:** *BranchHits* (from scanner).
-   **Triggers:** *if*, *else*, *for*, *while*, *switch*, logical
operators (*&&*, *\|\|*), and ternaries (*?*).
-   **Why it matters:** Each of these represents a split in reality.
\"If X is true, go left; otherwise, go right.\" Too many splits
make the path impossible to follow.

-   **B. Defensive Overhead (The Armor)**

-   **What it is:** Code written to protect against failure, not to
perform the primary task.
-   **Variables Used:** *SafetyHits*.
-   **Triggers:** *try*, *catch*, *finally*, *assert*, *guard*,
*validate*.
-   **Why it matters:** While safety is good, it creates visual
noise. A function wrapped in three layers of error handling is
structurally denser than one that just does the math. We count
this as complexity, but we weight it differently because it\'s
\"necessary\" complexity.

##### 2.1.F.3. The Equation: Calculating \'C\'

We calculate the **Composite Complexity Score (C)** using a weighted
sum.

1.  **Count the Branches:** We take the raw count of structural
elements. *Structural = BranchHits*
2.  **Weigh the Armor:** We take the count of safety elements and
multiply by **0.5**. *Defensive = SafetyHits \* 0.5* *Human
Translation:* Two safety checks consume as much \"mental space\" as
one actual logic branch. This prevents well-protected code from
looking unfairly \"spaghetti-like\" while acknowledging that it is
still denser than unsafe code.
3.  **Summation:** ****Composite Complexity Score (C****)***** =
Structural + Defensive = BranchHits + 0.5 \* SafetyHits*

##### 2.1.F.4. The Visual Thresholds (The Step Function)

We map the abstract number *C* to a physical **Fractal Depth**. This
determines how many times the geometry splits or how many moons orbit
the planet.

-   **Level 0: The Bamboo (C ≤ 2)**

-   **Code looks like:** A simple list of instructions. Do A, then
B, then C.
-   **Visual:** A single, straight line or a planet with 0-1 moons.

-   **Level 1: The Fork (C \> 2)**

-   **Code looks like:** A basic function with one or two checks.
-   **Visual:** The unit splits once.

-   **Level 2: The Tree (C \> 8)**

-   **Code looks like:** Standard business logic. Loops inside
conditions.
-   **Visual:** Distinct branching structure. 3-4 moons.

-   **Level 3: The Thicket (C \> 15)**

-   **Code looks like:** Complex algorithms, state machines, or
legacy parsers.
-   **Visual:** Dense, aggressive branching. A swarm of moons.

-   **Level 4: The Jungle (C \> 25)**

-   **Code looks like:** \"God Objects,\" massive switch statements,
or deep recursion.
-   **Visual:** A chaotic, fractal explosion. The geometry is almost
solid with branches.

****2****.1.****F****.****5 **Equation Implementation:**

*// 1. Control Flow & Logic (The Skeleton)*

*// Matches: if, else, for, while, switch, &&, \|\|, ?, ??*

*const Structural = count(Rules.branch);*

*// 2. Defensive Overhead (The Armor)*

*// We use the standard \'SafetyHits\' sub-equation from Spec 3.3.*

*// Matches: try, catch, finally, assert, sanitize, validate, checkAuth,
isinstance*

*// We weight these at 50% because they add noise/density but often wrap
existing logic.*

*const Defensive = SafetyHits \* 0.5;*

*// 3. Composite Score*

*const C = Structural + Defensive;*

*// 4. Fractal Mapping (Step Function)*

*if (C \> 25) Depth = 4 // \"Dense Thicket\" (The Jungle)*

*else if (C \> 15) Depth = 3*

*else if (C \> 8) Depth = 2*

*else if (C \> 2) Depth = 1*

*else Depth = 0 // \"Line\" (The Bamboo)*
