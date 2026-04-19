# 2.1.J. Relative Positioning

> **Metric: Semantic Affinity (Folder + Type + Importance)**
>
> **Purpose:** Group related files into "Constellations" or "Sectors" to create a navigable map, rather than a uniform noise field.
>
> **Why:** A standard spiral is predictable but dumb—it places a `login.js` next to a `utils.js` just because they loaded sequentially. By sorting and offsetting based on metadata, we create "Neighborhoods." Auth files cluster together; Tests float above the plane; Configs sink to the bottom.
>
> **Effect:** Determines the final 3D coordinates through a Tri-Phase procedural loop.

## 2.1.J.1. The Philosophy: The Tri-Phase Displacement

We don't use expensive physics simulations (like N-Body gravity). Instead, we use a predictable **3-Pass Sort & Offset** algorithm. This ensures that the same codebase always generates the exact same galaxy (deterministic) but still produces organic, organized clusters.

## 2.1.J.2. Phase 1: The Gravity Sort (Chronology & Importance)

Before positioning anything in 3D space, we re-index the file list to determine "Who sits at the Head of the Table?"

1. **Primary Sort: Inbound Reference Count (Descending)**
   * *Effect:* The "God Classes" and Core Utilities (High Gravity) naturally move to index $0$ (The Galactic Center).
2. **Secondary Sort: Directory Path**
   * *Effect:* Files in the same folder (e.g., `src/auth/`) end up adjacent in the list, ensuring they spiral out together in a dedicated "Sector."

## 2.1.J.3. Phase 2: The Gap Spiral (Radial Positioning)

We apply the Golden Angle Spiral, but we strategically inject **"Void Gaps"** when the directory changes. As we iterate through the sorted list, we calculate the standard spiral step:

$$\text{Angle} \mathrel{+}= 0.5$$

**The Check:** If `CurrentFile.folder !== PreviousFile.folder`:
* We add a massive buffer to the radius: $\text{Radius} \mathrel{+}= 150$
* *Result:* This creates physical empty space between the "Auth Sector" and the "UI Sector," visibly grouping them into islands along the spiral arm.

**The Standard:** If the directory is the same:
* We use tight packing for related files: $\text{Radius} \mathrel{+}= 12$

## 2.1.J.4. Phase 3: The Stratification (Z-Axis Type Layering)

We use the vertical axis (the Y-Axis in WebGL) to separate concerns, preventing the galactic disk from looking like a flat pancake. Instead of random jitter, we map **File Type** to **Elevation**.

| Stratification Layer | Y-Elevation | File Types | Visual Effect |
| :--- | :--- | :--- | :--- |
| **The Asset Atmosphere** | $+60$ units | `.css`, `.png`, `.svg` | Styles and assets float above the logic like clouds. |
| **The Logic Plane** | $0$ units | `.js`, `.ts`, `.py`, `.rs` | Source code forms the active, dense middle layer. |
| **The Bedrock** | $-60$ units | `.json`, `.yml`, `.dockerfile`, `.md` | Configs and data sink below the logic like a foundation. |

*(Note: We add a small random jitter to all layers to maintain organic volume instead of rigid geometric planes).*
