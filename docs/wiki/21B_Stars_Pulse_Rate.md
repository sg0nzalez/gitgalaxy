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
