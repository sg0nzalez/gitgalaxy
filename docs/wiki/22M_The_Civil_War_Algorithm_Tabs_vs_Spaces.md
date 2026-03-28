# 2.2.M. The "Civil War" Algorithm (Tabs vs. Spaces)

> **Metric: Layout Unity (Indentation Polarization)**
>
> **Summary:** While colloquially referred to as "Civil War," this equation measures Layout Unity. It visualizes the structural formatting consistency of a file by calculating the ratio of space-indented lines to tab-indented lines. 
>
> **Effect:** This metric **bypasses the Universal Risk Spectrum** because it does not measure escalating danger. Instead, it uses a custom Diverging Spectrum.
> * 🟩 **TABS (Score 0-19):** Pure Tabs. Glowing Green (`#39ff14`). Emissive intensity is maxed.
> * 🟦 **MIXED (Score 20-79):** The "War Zone". Maximum conflict sits at exactly $50$. Deep Blue (`#0000ff`). Triggers the "Bifurcation Shimmer" (geometry flickering).
> * 🟨 **SPACES (Score 80-100):** Pure Spaces. Glowing Yellow (`#ffff00`). Emissive intensity is maxed.

## 2.2.M.1. The Philosophy: The Linear Polarization Model

By mapping Tabs to $0$ and Spaces to $100$, the "War Zone" (a 50/50 mix of indentation styles) naturally falls into the center of the spectrum (Score $50$). 

This visually exposes files that lack a unified formatting standard. A file glowing bright green or bright yellow is unified and clean. A file glowing deep blue is structurally fractured, indicating that multiple developers with conflicting IDE configurations are fighting over the layout.

## 2.2.M.2. The Inputs (Indentation Context)

The scanner counts the absolute number of lines that lead with either tabs or spaces.

| Variable | Source | Structural Definition |
| :--- | :--- | :--- |
| `indent_tabs` | Scanner | Count of lines starting with one or more Tabs. |
| `indent_spaces` | Scanner | Count of lines starting with one or more Spaces. |

## 2.2.M.3. The Equation: The Polarization Ratio

**Step A: Gather Indentation Context**
We calculate the total number of lines that contain measurable indentation context. If a file has no indentation at all, it defaults to the neutral center ($50$).

$$L_{total} = L_t + L_s$$

**Step B: Calculate Space-Ratio ($R$)**
We calculate the percentage of indented lines that are controlled by spaces. A result of $0.0$ means $100\%$ Tabs. A result of $1.0$ means $100\%$ Spaces.

$$R = \frac{L_s}{\max(L_{total}, 1)}$$

**Step C: Final Score Mapping**
We map the ratio to a standard $0-100$ visual scale.

$$\text{FinalScore} = R \times 100.0$$

## 2.2.M.4. Implementation (Python Reference)

```python
def _calc_civil_war(self, eq: Dict[str, int]) -> float:
    """
    Calculates Layout Unity (Tabs vs Spaces). 
    0 = Pure Tabs (Green), 100 = Pure Spaces (Yellow), 50 = War Zone (Blue).
    """
    tab_lines = eq.get('indent_tabs', 0)
    space_lines = eq.get('indent_spaces', 0)
    
    l_total = tab_lines + space_lines
    
    # Handle Void States (No indentation at all)
    if l_total == 0:
        return 50.0 # Default to Neutral Blue
        
    # Calculate Space-Ratio (R)
    space_ratio = space_lines / l_total
    
    # Final Score Mapping (0-100)
    return space_ratio * 100.0
