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
