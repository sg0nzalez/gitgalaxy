# Injection Surface Exposure

> **Metric: RCE & XSS Vulnerability Surface**
>
> **Summary:** A core Security Lens metric. It tracks external network I/O flowing near dynamic execution boundaries without adequate safety nets.
>
> **Effect:** Illuminates the physical attack surface of the repository.

## The Equation: Input vs. Execution

**Step A: Define the Vectors**
$$InputVectors = io\_hits + (ssr\_boundaries \times 2.0)$$
$$ExecutionVectors = (danger \times 4.0) + (safety\_neg \times 2.0)$$

**Step B: The Agentic RCE Spike (Prompt Injection)**
If an LLM orchestrator or Agentic Tool has direct proximity to an `eval` or OS command, it is an extreme vulnerability (Agentic RCE). 
* If Agentic logic + Danger logic are both present, $ExecutionVectors$ are multiplied by $10.0$, and the AI is classified as a hostile input vector itself.

**Step C: Synthesize Mass**
$$InjectionMass = (InputVectors \times ExecutionVectors) \times ArchetypeMultiplier$$

**Step D: Taint & Sigmoid**
Like the Logic Bomb, confirmed Tainted Injections add a massive +500.0 gravity spike before being routed through the standard Laplace-smoothed Sigmoid curve.