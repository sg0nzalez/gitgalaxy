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
