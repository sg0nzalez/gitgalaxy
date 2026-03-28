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
