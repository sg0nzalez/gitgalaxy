# 2.1.B. Star's Pulse Rate

> **Metric: Inbound Reference Count (Popularity)**
>
> **Purpose:** See how popular or highly referenced a file is, which is a fundamental measure of its importance in the system.
> 
> **Effect:** Modulates the Emissive Intensity (Bloom Strength) and Pulse Floor. Pulses should feel powerful and stately, never blinky and annoying. Instead of deadening the colors with opacity fades, we use Bioluminescence. A "God Class" file that is imported by many other files shouldn't just blink faster; it should burn hotter and overwhelm the surrounding atmosphere.

## 2.1.B.1. The Philosophy: Bioluminescence

We treat the codebase as a living, deep-sea organism:

* **Hot (High Gravity):** Core utilities or "God Objects." These are the nuclear reactors of the system. They burn with a high-intensity, white-hot core that never fully dims.
* **Cold (Low Gravity):** Leaf nodes or standalone configs. They emit a gentle, shallow phosphorescence.

## 2.1.B.2. The Inputs: Measuring Gravity

* **Ref (Inbound References):** The count of *other* files that import this specific file.
* **MaxRef:** The highest reference count found in the entire repository. This sets the global "Ceiling" for the simulation.

## 2.1.B.3. The Equation: Intensity Mapping

We don't just change the speed of the pulse; we change the **Dynamic Range** of the glow.

* **Frequency (Speed):** Capped between 0.5Hz and 1.5Hz. We keep the pulse "Stately" and "Breathing" to avoid rapid, fatiguing strobing.
* **Amplitude (Intensity):** Mapped directly to popularity.
* **Floor:** The minimum brightness. Popular files *never* go completely dark.
* **Ceiling:** The maximum brightness. Popular files bloom into pure white at their peak.

## 2.1.B.4. The Math: Calculating Emissive Intensity

First, we normalize the popularity ($P$) into a clean scale from $0.0$ to $1.0$.

$$P = \min\left(\frac{\text{Ref}}{\text{MaxRef}}, 1.0\right)$$

Next, we establish the boundaries for speed, the bloom floor, and the bloom ceiling based on that popularity.

**1. Stately Speed:** Prevents the "Hazard Strobe" effect.
$$\text{Speed} = 0.5 + (P \times 1.0)$$

**2. The Bloom Floor:** Important files never fade below $1.0$ (Full Brightness).
$$\text{MinIntensity} = 0.2 + (P \times 0.8)$$

**3. The Bloom Ceiling:** Important files burst into blinding white ($4.0$) at the peak.
$$\text{MaxIntensity} = 1.5 + (P \times 2.5)$$

Finally, we apply a sine wave over time to calculate the exact shader value for the current frame.

$$\text{EmissiveIntensity} = \text{MinIntensity} + \left( \sin(\text{Time} \times \text{Speed}) \times (\text{MaxIntensity} - \text{MinIntensity}) \right)$$

## 2.1.B.5. The Visual Thresholds (The Resonance)

| Classification | Pulse Frequency | Dynamic Range | Visual Effect |
| :--- | :--- | :--- | :--- |
| **The Firefly** (Low Refs) | 0.5 Hz *(Slow)* | 0.2 $\rightarrow$ 1.5 | A gentle, rhythmic shimmer. The object retains its rich theme color (e.g., Deep Cyan) and occasionally brightens. |
| **The Reactor** (High Refs) | 1.5 Hz *(Stately)* | 1.0 $\rightarrow$ 4.0 | A powerful, "Core Saturation" effect. The center burns white-hot due to Bloom overload while the edges retain the theme color. It feels "heavy" and anchors the scene. |
