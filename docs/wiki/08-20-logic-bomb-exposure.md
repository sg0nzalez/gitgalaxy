# Logic Bomb Exposure

> **Metric: Sabotage Mass (Delayed Execution & Destruction)**
>
> **Summary:** A core Security Lens metric. Logic bombs sit dormant until a specific condition is met, at which point they execute a destructive payload. This metric hunts for condition-heavy code that ends in system halts, bailouts, or aggressive execution.
>
> **Effect:** Highlights files containing highly conditional destructive commands. 

## The Equation: Trigger & Payload

We calculate Sabotage Mass by multiplying the "Trigger" (the conditional logic) by the "Payload" (the destructive outcome).

**Step A: Define the Trigger**
We weigh standard branching heavily against thread-halting commands (which are often used to delay execution).
$$Trigger = branch\_hits + (halt\_hits \times 3.0)$$

**Step B: Define the Payload**
We look for system exits, manual memory cleanup, and dynamic execution.
$$Payload = (bailout \times 2.0) + (cleanup \times 1.5) + (danger \times 4.0)$$

**Step C: The Agentic & Hardware Shields**
AI orchestration and hardware bridges naturally use dynamic execution and halting. We divide the Payload by the presence of these heuristics to prevent false positives in robotics/ML repositories.

**Step D: The Taint Spike**
If the static engine explicitly confirmed that tainted input flowed directly into an execution sink, this is an absolute vulnerability.
$$SabotageMass += (TaintedInjection \times 500.0)$$

**Step E: Sigmoid Mapping**
The $SabotageMass$ is normalized against the padded LOC and mapped to the 0-100 scale using the security sigmoid curve.