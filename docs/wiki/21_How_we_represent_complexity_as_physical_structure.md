### 2.1 How we represent complexity as physical structure

Code complexity is mapped to ****physical structure****, creating
organic, distinct shapes for different complexity patterns. This
representation of complexity does not depend on color. They are
summarized below.

**

-------------------------- ------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------
Physical Attribute         Code Metric (Heuristic)               Visual Result (The \"Look\")
**Star's Size**            Lines of Code (LOC) per File          **Mass.** Logarithmic scaling ensures that 10k+ LOC files appear as massive suns, while 10 LOC scripts remain small asteroids.
**Star's Pulse Rate**      Inbound References (Popularity)       **Bioluminescence.** Core utilities pulse with a white-hot \"heartbeat.\" Unreferenced files remain dim and static.
**Star's Shape**           control flow ratio (File Level)       **Geometry.** Morphs from a smooth **Sphere** (Declarative/Data) to a sharp **Tetrahedron** (Pure Algorithmic Logic).
**Satellite Unit**         Function Declaration                  **Moons.** Every discrete function is materialized as a satellite orbiting its parent star. Limits for monorepos.
**Satellite Distance**     Lines of Code (LOC) per Function      **Orbital Reach.** Long functions reach further into the void; small stubs orbit tightly near the star's surface.
**Number of Satellites**   Cyclomatic Complexity                 **Fractal Density.** Highly complex functions spawn sub-clusters or dense swarms of satellites, creating a \"thorny\" silhouette.
**Satellite Position**     control flow ratio (Function Level)   **Branching Angle.** Sharp, jagged angles (\<45°) indicate complex control flow; 90° \"Circuit Board\" patterns indicate linear flow.
**Satellite Size**         Argument Count                        **Volume.** Large moons represent \"Heavy\" functions with many inputs; small dots represent lightweight, encapsulated utilities.
**Star's Rings**           External Library Imports              **Accretion Disks.** Files tethered to many external dependencies manifest glowing rings, symbolizing a large \"Gravity Well.\"
**Star's Position**        Semantic Affinity (Directory/Path)    **Neighborhoods.** Files are grouped into sectoral clusters based on folder structure, creating distinct \"Auth,\" \"UI,\" and \"API\" continents.
-------------------------- ------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------

**

#### 2.1.A. Star's Size

#####

****Purpose: Visualize the sheer \"Gravitational Weight\" of a file
within the system. Why: In a galaxy, size is the first thing you notice.
But in software, \"length\" does not always equal \"weight.\" A 200-line
configuration file is light, while a 50-line recursive algorithm is
heavy. By calculating mass based on complexity, risk, and volume, we
ensure that the most impactful files---the ones that are hard to read,
dangerous to touch, or heavily connected---physically dominate the
screen as super-massive suns. We use size to instantly communicate
structural importance.****

##### 2.1.A.1. The Philosophy: Physical Presence

We treat code as physical matter, but we recognize that matter has
different densities.

Low Density: Simple data, linear lists, and standard config files. These
are large but light, easy to move.

High Density: Complex branching logic, heavy arguments, and high risk
exposure. These are small but incredibly heavy, exerting high gravity.

By scaling the star\'s size based on this Composite Mass, we create a
visual hierarchy where the true \"Main Characters\"---the complex logic
engines---naturally anchor the sector, while simple helper files drift
in the background.

##### 2.1.A.2. The Inputs: Measuring Mass

The mass calculation ingests five distinct dimensions of code structure:

1.  Function Impact: The complexity of every function inside the file.
2.  API Exposure: How publicly visible the file is.
3.  Concurrency Exposure: The density of asynchronous/threading logic.
4.  State Flux Exposure: The density of variable mutation.
5.  LOC (Lines of Code): The raw physical volume (scaled down to act as
a base substrate).

##### 2.1.A.3. The Equation: Structural Mass & Visual Radius

We utilize a multi-stage summation to determine the raw mass. Complexity
multiplies; volume merely adds. We then apply a logarithmic clamp to
determine the final visual radius, ensuring that massive \"God Objects\"
are distinct but do not consume the entire viewport.

Step 1: Calculate Function Impact For every function in the file, we
calculate an impact score based on its decision density (Branches),
connectivity (Args), and length.

Function Impact = ((BranchHits + 1) \* (Args + 1) + (0.05 \* LOC)) \* 10

Step 2: Calculate Total Mass (The Raw Metric) The file\'s final mass is
the sum of its functions plus its system-wide risk exposures.

Total Mass = Sum(Function Impacts) + API + Concurrency + Flux + (LOC /
50)

Step 3: Calculate Visual Radius (The Render Size) We apply a base-2
logarithm to compress the massive range of weights (10 to 1,000,000)
into a renderable scale (10 to 50 units).

Radius = 10 + (Math.log2(Math.max(Total Mass, 1)) \* 2)

##### 2.1.A.4. The Visual Thresholds (The Scale)

The Asteroid (Mass \< 100): Radius \~16 units. Simple DTOs, interfaces,
or small configs. Nimble, low-gravity rocks that drift in the periphery.

The Planet (Mass 100 - 1,000): Radius \~20 to 26 units. Standard
business logic. Visible, stable, but not overwhelming. The \"Middle
Class\" of the galaxy.

The Star (Mass 1,000 - 20,000): Radius \~27 to 38 units. Core utilities,
major controllers, or complex engines. These anchor local clusters and
exert visible gravity.

The Super-Giant (Mass 20,000+): Radius \~40+ units. \"God Objects,\"
massive reducers, or legacy core files. These dominate the screen,
signaling extreme structural density.

****

#### 2.1.B. Star's Pulse Rate

**Metric**: Inbound Reference Count (Popularity). ****

**Purpose**: ****See how popular or highly referenced a file is****.
****

**Why**: ****A fundamental measure of a file's importance in a
system.****

**Effect**: Modulates the Emissive Intensity (Bloom Strength) and Pulse
Floor. ****Pulses**** should feel powerful ****and stately, never blinky
and annoying****. Instead of deadening the colors with opacity fades, we
use Bioluminescence. A \"God Class\" ****file that is**** imported by
****many other files ****shouldn\'t just blink faster; it should burn
hotter ****and**** overwhelm the surrounding atmosphere.****

##### 2.1.B.1. The Philosophy: Bioluminescence

We treat the codebase as a living deep-sea organism.

-   **Hot:** Core utilities or \"God Objects.\" These are the nuclear
reactors of the system. They burn with a high-intensity, white-hot
core that never fully dims.
-   **Cold:** Leaf nodes or configs. They emit a gentle, shallow
phosphorescence.

##### 2.1.B.2. The Inputs: Measuring Gravity

-   **Ref (Inbound References):** The count of *other* files that import
this specific file.
-   **MaxRef:** The highest reference count found in the entire
repository. This sets the \"Ceiling\" for the simulation.

##### 2.1.B.3. The Equation: Intensity Mapping

We don\'t just change speed; we change the **Dynamic Range** of the
glow.

-   **Logic:**

-   **Frequency (Speed):** Capped between 0.5Hz and 1.5Hz. We keep
the pulse \"Stately\" and \"Breathing,\" avoiding rapid
strobing.

-   **Amplitude (Intensity):** Mapped directly to popularity.

-   **Floor:** The minimum brightness. Popular files *never* go
dark.
-   **Ceiling:** The maximum brightness. Popular files bloom
into pure white.

##### 2.1.B.4. Equation:

*// Normalize Popularity (0.0 to 1.0)*

*const P = Math.min(Ref / MaxRef, 1.0);*

*// 1. Stately Speed (0.5Hz to 1.5Hz) - Preventing the \"Hazard
Strobe\"*

*const speed = 0.5 + (P \* 1.0);*

*// 2. The Bloom Floor (0.2 to 1.0)*

*// Important files never fade below 1.0 (Full Brightness)*

*const minIntensity = 0.2 + (P \* 0.8);*

*// 3. The Bloom Ceiling (1.5 to 4.0)*

*// Important files burst into blinding white (4.0) at the peak*

*const maxIntensity = 1.5 + (P \* 2.5);*

*// Final Shader Value*

*emissiveIntensity = minIntensity + (sin(time \* speed) \*
(maxIntensity - minIntensity));*

##### 2.1.B.5. The Visual Thresholds (The Resonance)

-   **The Firefly (Low Refs):**

-   **Pulse:** 0.5 Hz (Slow).
-   **Range:** 0.2 -\> 1.5.
-   **Visual:** A gentle, rhythmic shimmer. The object retains its
rich theme color (e.g., Deep Cyan) and occasionally brightens.

-   **The Reactor (High Refs):**

-   **Pulse:** 1.5 Hz (Moderate/Stately).
-   **Range:** 1.0 -\> 4.0.
-   **Visual:** A powerful, \"Core Saturation\" effect. The center
of the object burns white-hot due to Bloom overload, while the
edges retain the theme color. It feels \"heavy\" and \"alive,\"
anchoring the scene.

#### 2.1.C Star's Shape 

**Metric:** control flow ratio ().

**Purpose:** Give every star a distinctive silhouette that communicates
the \"State of Matter\" of the code.

**Why:** A file isn\'t just a size; it has a temperament. Declarative
code (like a list of variables) is stable and solid. Algorithmic code
(like a sorting method) is energetic and sharp. Without this variance,
the galaxy looks like a generic ball field. By morphing the shape, we
allow developers to \"feel\" the difference between a config file and a
logic core without reading a single character.

**Effect:** Transitions the central mesh through five distinct geometric
tiers.

##### 2.1.C.1. The Philosophy: Smooth vs. Sharp

We categorize code into five \"Phases of Matter\" based on its
decision-making density.

-   **Organic (Smooth):** Passive code that defines things. It feels
safe and \"round.\"
-   **Crystalline (Jagged):** Active code that decides things. It feels
sharp and \"dangerous.\"

##### 2.1.C.2. The Philosophy: Thinking vs. Speaking

Code does two things: it either **computes** (makes decisions) or it
**declares** (defines structures).

-   **Computing (Logic):** \"If X happens, do Y.\" This is jagged,
non-linear, and energetic. It represents the \"Thinking\" brain.
-   **Defining (Structure):** \"Let X equal 5.\" This is flat, linear,
and stable. It represents the \"Memory\" or \"Structure\" of the
system.

**We visualize this tension physically. A file that \"thinks\" a lot
(algorithms) looks sharp and aggressive. A file that \"remembers\" a lot
(configs, interfaces) **has softer angles.****

##### 2.1.C.3. The Inputs: The control flow ratio

The scanner separates every regex hit into one of two buckets:

-   **A. Branch Hits (The Logic)**

-   **Concept:** Points where execution splits.
-   **Variables Used:** *BranchHits* (from scanner).
-   **Triggers:** *if*, *else*, *switch*, *case*, *for*, *while*,
*catch*, *&&*, *\|\|*, ternary *?*.
-   **Meaning:** High counts here mean the code is constantly
changing direction.

-   **B. Linear Hits (The Structure)**

-   **Concept:** Points where execution flows straight or data is
defined.
-   **Variables Used:** *LinearHits*.
-   **Triggers:** *const*, *let*, *return*, *import*, *export*,
*class*, *interface*, *type*.
-   **Meaning:** High counts here mean the code is describing *what*
things are, not *doing* things.

##### 2.1.C.4. The Equation

We calculate the **control flow ratio ()** as the percentage of relevant
code that is dedicated to branching.

1.  **Summation:** We find the total \"Semantic Mass\" of the file.
*TotalFlow = BranchHits + LinearHits*

2.  **Ratio Calculation:** *R_L = BranchHits / TotalFlow*

-   **Result 0.0:** Pure Structure (e.g., a JSON file or TS
Interface).
-   **Result 1.0:** Pure Logic (e.g., a complex regex parser or math
utility).
-   **Result 0.5:** Balanced code (Standard business logic).

##### 2.1.C.5. The Equation: 5-Tier Morphing

The engine selects a *BufferGeometry* based on the following thresholds:

----------------------- ------------------ ---------------------------- --------------------------------------
control flow ratio ()   Geometry Type      Visual Style                 Human Translation
**0 -- **0.59****       **Sphere**         Glowing Orb                  \"The Seed\": Pure data or metadata.
**0.**6 - .69****       **Icosahedron**    20-sided Glowing Wireframe   Mostly declarative/classes.
****0.7 -- 0.79****     **Dodecahedron**   12-sided Glowing Wireframe   Balanced business logic.
**0.**8 -- 0.89****     **Octahedron**     8-sided Glowing Wireframe    Highly algorithmic/complex.
**0.**90** -- 1.0**     **Tetrahedron**    4-sided Glowing Wireframe    Pure logic/Recursion.
----------------------- ------------------ ---------------------------- --------------------------------------

****Note on Matrix Optimization: For wireframe-only modes (like \"The
Matrix\" theme), the Sphere primitive in the 0.0-0.59 range should be
replaced with ****a ****Icosidodecahedron (32 faces --
****Buckyball!)****

##### 2.1.C.6. The Visual Enhancements (Wireframe Logic)

To emphasize the \"Digital\" nature of high-logic code, the rendering
style shifts as the shape sharpens:

-   ****The Low Tier (Sphere):**** Rendered with a solid, emissive
material. It feels like a glowing planet with soft, volumetric
light.
-   ****The High Tiers (Icosahedron -- Tetrahedron):**** Rendered as
****Glow Wireframes****. We expose the edges and facets, making the
star look like a flickering vector projection. As the control flow
ratio increases, the wireframe density thins out, making the final
\"Tetrahedron\" look like **a lethal, minimalist pyramid of pure
calculation**.

#### 2.1.D Satellite Unit

**Metric**: Function Declaration (e.g., *****function*****,
*****=\>*****, *****def*****, *****class method*****). ****

**Purpose**: Represents a discrete unit of logic---a
\"Tool\"---contained within the file (the Toolbox). ****

**Why**: Files are rarely monolithic blocks of text; they are
collections of distinct functions. We visualize these as moons orbiting
the planet to show the granularity and inventory of the file at a
glance. ****

**Effect**: Spawns a small spherical geometry orbiting the central
parent.****

##### 2.1.D.1. The Philosophy: The Toolkit

We treat the file as a container.

-   **The Star:** The Box (Class/Module).
-   **The Satellites:** The Tools (Functions/Methods). A star with no
moons is likely a static data configuration. A star with 50 moons is
a heavy utility class with many diverse tools.

##### 2.1.D.2. The Inputs: Identification

-   **Regex Hits:** *function*, *=\>*, *def*, *func*.
-   **Cap:** \~12 satellites (To prevent rendering swarms, we visualize
a representative sample).

##### 2.1.D.3. Basal Values (The Standard Model)

Every satellite begins with these default physical properties before
other metrics (like complexity) warp them:

-   **Geometry:** *SphereGeometry(2, 4, 4)* (Low-poly \"Moon\").
-   **Radius:** 2 Units (Fixed, small).
-   **Color:** Inherits Parent Star\'s color (Visual Cohesion).
-   **Opacity:** 0.8 (Slightly ghosted to indicate subservience).
-   **Orbit:** Rotates around the parent at a basal speed unless
modified by \"Heat\" metrics.

2.1.D.4. The Function Impact Score

Not all moons are equal. A one-line \"getter\" is a pebble; a 500-line
algorithm is a moon. To ensure the visualization is honest, we calculate
an Impact Score for every function found. This score determines which 12
satellites are rendered (we always show the heaviest) and how \"large\"
they appear.

Logic: We combine Complexity (Branches), Connectivity (Args), and Volume
(LOC) into a single weight metric.

Impact Score = ((BranchHits + 1) \* (Args + 1) + (0.05 \* LOC)) \* 10

BranchHits: The density of decision making. Args: The weight of
inputs/coupling. LOC: The physical length (scaled down by 0.05 to
prioritize logic over verbosity). Multiplier (10): Scales the integer
for storage efficiency in vectorized formats.

****

#### 2.1.E Satellite Orbital Distance

**Metric**: Lines of Code in a function.

**Effect**: Bigger the function, the further the satellite.

**Input**: LOC (Lines of Code for the specific function/block).

**Logic**: Logarithmic Scaling. This ensures that we can visually
differentiate between small (10 lines), large (1,000 lines), and massive
(100,000 lines) files without the graphic growing infinitely off the
screen.

****Equation:****

-   *Length_pixels = 60 + (Math.log2(Math.max(LOC, 1)) \* 30)*

****Scaling Examples: ****

-   -   ****10 LOC:**** \~160px (Visible Stub)
-   ****100 LOC:**** \~260px (Standard Branch)
-   ****1,000 LOC:**** \~360px (Major Limb)
-   ****100,000 LOC:**** \~560px (Megastructure Reach)

****Visual Output:****

-   -   ****3D:**** Distance of the orbiting satellite from the core
(Orbital Radius).

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

#### 2.1.G Satellite's Relative Positioning in a unit

**Metric**: ****Ratio ****of logic to declarative statements****

**Purpose**: Give every function or deployment of satellites a
distinctive shape depending on that function's ratio of logical
statements to declarative statements. ****

**Why: **It looks boring and repetitive without it. ****

**Effect**: Alters how the satellites in a function are arranged in 3D
space.

##### 2.1.G.1. The Visual Translation (The Lerp)

We map the abstract ratio () to physical angles using **Linear
Interpolation (Lerp)** ****and the control flow ratio defined above.
****

**** ****2****.1.****G.**1. The Philosophy: Thinking vs. Speaking**

Code does two things: it either **computes** (makes decisions) or it
**declares** (defines structures).

-   **Computing (Logic):** \"If X happens, do Y.\" This is jagged,
non-linear, and energetic. It represents the \"Thinking\" brain.
-   **Defining (Structure):** \"Let X equal 5.\" This is flat, linear,
and stable. It represents the \"Memory\" or \"Structure\" of the
system.

****We visualize this tension physically. A file that \"thinks\" a lot
(algorithms) looks sharp and aggressive. A file that \"remembers\" a lot
(configs, interfaces) ****has softer angles.****

**Equation:** *Angle = 22.5 + (1.0 - R_L) \* (90 -- 22.5)*

**High Logic ():** Angle . Branches diverge sharply, creating a
\"Lightning Bolt\" look.

**High Structure ():** Angle . Branches diverge at right angles,
creating a \"Circuit Board\" or \"Grid\" look.

Angles are then used to build the position of the satellites.

****

#### 2.1.H Node Size (Metric: Argument Count)

****Metric:****** Argument Count (Args). **

****Purpose:****** Visualizes the \"State Heaviness\" or I/O weight of a
function. **

****Why:****** Functions with many arguments often carry significant
state or context (\"I/O Weight\"). A clean utility usually takes 1-2
arguments, while a legacy handler might take 10. We visualize this
physically to differentiate sleek tools from heavy machinery. **

****Effect:****** Modulates the physical size (Scale) of the orbiting
satellite.**

##### 2.1.H.1. The Philosophy: Heavy vs. Light

We view arguments as \"Inputs\" or \"Cables\" plugged into the function.

-   **Lightweight:** 0-2 arguments. Sharp, encapsulated, easy to move.
-   **Heavyweight:** 5+ arguments. Bloated, carrying too much context,
harder to maintain.

##### 2.1.H.2. The Inputs: Measuring Args

-   **Args:** The count of arguments in the function signature found by
the scanner.
-   **Range:** Typically 0 to 20+.

##### 2.1.H.3. The Equation: Logarithmic Scaling

We use logarithmic scaling to prevent massive orbs for functions with
many arguments (e.g., 20+). A linear scale would make them visually
overwhelming; a log scale highlights the difference between 0 and 5, but
compresses the difference between 10 and 20.

**Equation:** *Scale = 1.0 + (Math.log2(Math.max(Args, 1)) \* 0.2)*

-   **Base Scale:** 1.0 (Standard Unit).
-   **Factor:** \* 0.2 (Gentle growth multiplier).

##### 2.1.H.4. The Visual Output

-   **3D:** Radius of the orbiting Moon particles.

#### 2.1.I. Planetary Rings 

**Metric:** External Library Import Count

**Purpose:** See which files import external libraries

**Why: **Determine which files have dependencies that you don't fully
control.****

**Effect:** Spawns rings around the file to determine

##### 2.1.I.1. The Philosophy: The Gravity Well

A clean file is a sphere. It floats freely. A file with dependencies is
tethered. The more it imports, the heavier it gets. We set a **High
Threshold** for rings. We don\'t want visual noise for a single utility
import. Rings are reserved for \"Heavy Lifters\" and \"Glue Code.\"

##### 2.1.I.2. The Inputs: Measuring Dependencies

-   **ImportHits:** The count of *import*, *require*, or *include*
statements found by the scanner.
-   **Threshold:** **\> 5 Imports**. Anything less is considered
\"Standard Weight\" and renders with **No Rings**.

##### 2.1.I.3. The Equation: Growth and Density

Instead of complex accretion disks, we use a single, evolving ring
system that grows in **Density (Opacity)** and **Mass (Width)** as the
gravity increases.

-   **Logic:**

-   **Opacity (Visibility):** Ranges from **0.0 to 0.6** over the
first 26 imports.

-   *Math:* *Opacity = Math.min((ImportHits / 26) \* 0.6, 0.6)*
-   *Effect:* Rare imports create a barely visible \"Ghost
Ring.\" As dependencies hit the critical mass (26), the ring
becomes a distinct, semi-solid band.

-   **Width (Tube Thickness):** Grows continuously as imports
increase.

-   *Math:* *TubeRadius = BaseWidth + (ImportHits \* 0.1)*
-   *Effect:* The ring gets physically thicker and wider,
consuming more visual space around the planet as the gravity
well deepens.

##### 2.1.I.4. The Visual Output

-   -   **Geometry:** *TorusGeometry*.

-   **Tube Radius:** Scaled linearly by *ImportHits*.

-   **Material:** Transparent with *opacity* capped at 0.6.

-   **Tilt:** Rings are tilted at randomized axes (Euler angles) to
ensure they don\'t look like flat plates, but dynamic,
gyroscope-like orbital paths.

**

#### 2.1.J Relative Positioning (Metric: Sequence & Affinity)

**Metric:** Semantic Affinity (Folder + Type + Importance).

**Purpose:** Group related files into \"Constellations\" or \"Sectors\"
to create a navigable map, rather than a uniform noise field.

**Why:** A standard spiral is predictable but dumb---it places a
*login.js* next to a *utils.js* just because they loaded sequentially.
By sorting and offsetting based on metadata, we create
\"Neighborhoods.\" Auth files cluster together; Tests float above the
plane; Configs sink to the bottom.

**Effect:** Determines the final coordinates through a ****Tri-Phase****
procedural loop.

##### 2.1.J.1. The Philosophy: The Tri-Phase Displacement

We don\'t use expensive physics simulations (N-Body gravity). Instead,
we use a predictable **3-Pass Sort & Offset** algorithm. This ensures
that the same code always generates the same galaxy (deterministic) but
produces organic, organized clusters.

##### 2.1.J.2. Phase 1: The Gravity Sort (Chronology & Importance)

Before positioning, we re-index the file list to determine \"Who sits at
the Head of the Table?\"

-   **Primary Sort:** **Inbound Reference Count (descending).**

-   *Effect:* The \"God Classes\" and Core Utilities (High Gravity)
naturally move to index *0* (The Galactic Center).

-   **Secondary Sort:** **Directory Path.**

-   *Effect:* Files in the same folder (e.g., *src/auth/*) end up
adjacent in the list, ensuring they spiral out together in a
\"Sector.\"

##### 2.1.J.3. Phase 2: The Gap Spiral (Radial Positioning)

We apply the Golden Angle Spiral, but we inject **\"Void Gaps\"** when
the directory changes.

-   **Logic:**

-   Iterate through the sorted list.

-   Calculate standard spiral step: *angle += 0.5*.

-   **The Check:** If *CurrentFile.folder !== PreviousFile.folder*:

-   Add **buffer** to the radius (*radius += 150*).
-   *Result:* This creates physical empty space between the
\"Auth Sector\" and the \"UI Sector,\" visibly grouping them
into islands along the spiral arm.

-   **Standard:** *radius += 12*. (Tight packing for related files).

##### 2.1.J.4. Phase 3: The Stratification (Z-Axis Type Layering)

We use the vertical axis () to separate concerns, preventing the disk
from looking like a flat pancake.

-   **Logic:** instead of random jitter, we map **File Type** to
**Elevation**.

-   **The Logic Plane (Y = 0):** Source Code (*.js*, *.ts*, *.py*,
*.rs*). The active layer.
-   **The Asset Atmosphere (Y = +60):** Styles & Assets (*.css*,
*.png*, *.svg*). Floating above the logic like clouds.
-   **The Bedrock (Y = -60):** Configs & Data (*.json*, *.yml*,
*.dockerfile*, *.md*). Sunk below the logic like a foundation.
-   *Random Jitter:* We add a small *±10* jitter to all layers to
maintain organic volume.

#### 2.1.K Misc Equations

**The code implements a dynamic orbitRadius formula: 40 + (log2(loc) \*
10). This establishes an \"Event Horizon\" for functional moons,
ensuring that high-mass files (Tier 4) do not physically intersect with
their orbiting satellites, maintaining structural legibility at extreme
scales.**

**
