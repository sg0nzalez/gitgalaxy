# Hardcoded Secrets Exposure

> **Metric: Data Hemorrhage Risk**
>
> **Summary:** A core Security Lens metric. It detects exposed private info (API keys, passwords, tokens) and evaluates the surrounding logic to determine how likely that secret is to leak into logs or external networks.

## The Equation: The Careless Amplifiers

**Step A: Base Leak Mass**
We rely heavily on the static scanner's regex detection for credentials.
$$BaseLeak = private\_info \times 10.0$$

**Step B: The Amplifiers**
A hardcoded secret is bad. A hardcoded secret being `console.log`'d is catastrophic. We calculate a multiplier based on careless handling.
$$Amplifiers = 1.0 + print\_hits + graveyard\_hits + globals\_hits$$

**Step C: The LLM API Spike**
If the file is calling external LLM APIs (`llm_api > 0`) but has zero global configurations (`globals == 0`), it strongly implies the API keys are hardcoded directly inline with the fetch logic.
* If True, $Amplifiers$ are multiplied by $3.0$.

**Step D: Final Calculation**
$$LeakMass = BaseLeak \times Amplifiers$$
Because a leaked secret is dangerous regardless of file size, we use a much smaller Laplace pad (+50) before mapping the density to the final 0-100 risk score.