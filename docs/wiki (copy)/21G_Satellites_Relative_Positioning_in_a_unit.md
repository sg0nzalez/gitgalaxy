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
