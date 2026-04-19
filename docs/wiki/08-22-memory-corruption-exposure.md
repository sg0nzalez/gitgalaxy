# Memory Corruption Exposure

> **Metric: Unsafe Memory Management (UAF / Buffer Overflows)**
>
> **Summary:** A core Security Lens metric focused exclusively on low-level, unmanaged memory manipulation.
>
> **Effect:** Highlights areas at risk for memory leaks, Use-After-Free (UAF), and buffer overflows.

## The Opt-In Whitelist

Memory Corruption is **Strictly Opt-In**. If the file is not written in a native memory-managed language (e.g., `c`, `cpp`, `rust`, `zig`, `assembly`), the engine immediately bypasses the math and returns $0.0$.

## The Equation: Raw vs. Managed Memory

**Step A: Calculate Raw Memory Mass**
We sum the weighted heuristics for direct memory addressing.
$$RawMass = (pointers \times 2.5) + (alloc \times 3.0) + (asm \times 5.0) + (casts \times 1.5)$$

**Step B: Calculate Mitigation Mass**
We look for explicit memory cleanup and standard safety guardrails.
$$Mitigation = cleanup + (safety \times 1.5)$$

**Step C: Net Risk**
$$NetRisk = \max(RawMass - Mitigation, 0.0) \times ArchetypeMultiplier$$
The result is mapped through the standard security Sigmoid curve.