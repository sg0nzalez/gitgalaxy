#### 2.3.4. The Prism -- Splitting the comments from the code

Following the successful completion of the language identification, the
engine performs a Structural Refraction---splitting a single source file
into mutually exclusive streams. Under the Strategy v6.2.0 Protocol,
this dual-capture process yields the pure logic *code_stream* (Active
Matter), the documentation *comment_stream* (Ghost Mass), and accurate
LOC metrics (*coding_loc* and *doc_loc*).

This phase is critical for preventing \"Logic Erosion,\" where
documentation or URLs inside strings might otherwise inflate the
perceived mass or branching density of the star. The split is a
non-destructive process allowing the system to analyze the skeleton of
the code and the spirit of the documentation independently.

##### 2.3.4.A. The Refraction Mechanics (The Prism Protocol)

The refraction process relies on the linguistic parameters established
by the Language Lens. By operating on verified signals, the Prism
eliminates the \"Neighborhood Guessing\" common in standard scanners,
achieving near-perfect accuracy in its separation of code from comments.
Note that in v6.2.0, multi-language (*lang_mix*) tracking is fully
delegated upstream to the Detector.

###### 2.3.4.A.1. Verified Hand-off & Singularity Bypass

The Optical Splitter is the primary \"Refraction Gate\" in the physics
pipeline. It utilizes two absolute bypasses to protect edge cases and
preserve structural integrity:

-   **The Singularity Bypass:** Any file identified as *undeterminable*
or *unknown* bypasses the split entirely. All content is routed to
the *code_stream* as intact \"Dark Matter\" to ensure no potentially
vital logic is lost.
-   **The Prose Bypass:** Files identified as pure literature
(*markdown*, *plaintext*, *xml*) route their entire payload directly
to the *comment_stream* (Ghost Mass), instantly protecting human
prose and markup from being miscalculated as structural logic.

###### 2.3.4.A.2. The 8 Mechanical Families (COMMENT_DEFINITIONS)

The engine utilizes a standardized execution matrix to route files based
on their mechanical stripping requirements.

------- ----------------- ------------------------------------------------------- --------------------------------------------------------------
ID      Key               Refraction Strategy                                     Coverage
**1**   **std_c**         Standard Line (*//*) and Block (*/\* \*/*)              JS, TS, Java, C#, C++, C, Go, Kotlin, Obj-C, Apex, Dart, CSS
**2**   **nested_c**      Recursive \"While-Peel\" extraction for nested blocks   Rust, Swift, Scala
**3**   **pure_hash**     Single-pass hash (*\#*) extraction                      Python, MicroPython, Shell, AGC, Dockerfile, Makefile
**4**   **hybrid_hash**   Hash line + Custom blocks (*\<#*, *=pod*)               PowerShell, Perl, Ruby
**5**   **hybrid_dash**   Double-dash (*\--*) + Unique blocks (*{-*)              SQL, Lua, Haskell
**6**   **polyglot**      Multi-token extraction (*//*, *\#*, */\**)              PHP, LiveCode
**7**   **positional**    Column-Anchored (Col 1/7) extraction                    COBOL, Fortran, ABAP
**8**   **singular**      Unique markup/logic delimiters (*\<!\--*, *;*)          HTML, Assembly, Zig
------- ----------------- ------------------------------------------------------- --------------------------------------------------------------

###### 2.3.4.A.3. The Integrated Protection Shields

To preserve the mathematical integrity of the Logic Stream, the Prism
implements surgical extraction via specialized hardware-level filters.

-   **The String Literal Shield:** The engine employs a Tier 1
Match-and-Bypass regex (*SHIELD_PATTERN*). Sequence data (URLs, file
paths, regex strings) caught by the shield are routed exclusively to
the *code_stream*. This prevents the engine from accidentally
stripping a \"comment marker\" found inside a legitimate string
(e.g., *const url = \"http://\...\"*).

-   **The Metadata Guard:** The first line of the file (metadata intent)
is extracted and cached. Explicit guards for Shebangs (*#!*), PHP
tags (*\<?php*), and XML headers (*\<?xml*) ensure this \"Metadata
Logic\" is re-attached to the *code_stream* so downstream
risk-scaling engines maintain execution context.

-   **Nested Recursion & Active String Masking:** For languages in the
*nested_c* family (Rust, Swift, Scala), the engine uses a
programmatic loop to \"peel\" literature from the innermost layers
outward. Under v6.2.0, this is hardened with **Active String
Masking**---temporarily swapping string literals with safe cache
keys---to prevent the mathematical *.rfind* loop from tearing apart
valid string logic. A *NESTED_PEEL_LIMIT* (default 500) acts as a
circuit breaker against infinite regex loops.

-   Hardened Post-Processing (Python & PHP):

-   *Python/Ruby:* Standalone triple-quoted blocks (*\"\"\"* or
*\'\'\'*) are surgically identified and diverted to the Ghost
Mass, preventing large docstring blocks from inflating the
*coding_loc* metric.
-   *PHP:* Heredoc, Nowdoc, and massive multi-line strings are
extracted to the Ghost Mass and replaced in the logic stream
with safe, empty string literals (*\"\"*). This prevents
structural hallucinations while perfectly preserving PHP array
syntax.

###### 2.3.4.A.4. Polyglot Partitioning & Language Sliding

Modern codebases frequently shift wavelengths mid-file. The Prism
implements Mid-File Language Sliding to maintain accuracy across
linguistic boundaries, with *lang_mix* tracking now fully delegated to
the upstream Detector.

-   **The Handshake Protocol:** The engine monitors for transitions
configured in the *HANDSHAKE_REGISTRY* (e.g., *\<script\>*,
*asm!()*, or *SELECT*). When a handshake trigger is detected, the
engine pauses the primary prism and activates the secondary
spectrum\'s lens for that specific alien segment.
-   **Balanced Scoping with Exact Escape Handling:** For paired-bracket
segments (like Assembly blocks or embedded SQL), the Prism tracks
nesting depth via a Handshake Stack. The v6.2.0 protocol introduces
**Exact Escape Handling**, which calculates even/odd consecutive
backslash counts to determine if a quote is real or escaped. This
prevents the lens from falsely triggering scope closures while
trapped inside an escaped string literal.
-   **Optical Partitioning:** The file is split into distinct segments,
each refracted using its native mechanical family. The
*HANDSHAKE_LOOKAHEAD_LIMIT* ensures the scope guard does not cause
extreme performance degradation before synthesizing the final
dual-stream result.

###### 2.3.4.A.5. Mutual Exclusivity (The Double-Dip Fix)

To guarantee mathematical precision in metric tracking, the Prism
enforces strict mutual exclusivity between logic and literature. By
counting the pure coding lines (*coding_loc*) and subtracting them from
the total active lines of the un-split file, the engine derives the
documentation lines (*doc_loc*). This entirely prevents the \"Inline
Comment Double-Dip,\" ensuring that a line containing both executable
code and an inline comment is strictly scored as Active Matter.

###### 2.3.4.A.6. Output Streams: The Dual-Mass Result

****The structural refraction yields a high-fidelity data payload (the
*****RefractionResult*****) containing four distinct channels that feed
independent analysis tracks:****

-   ***code_stream***** (Active Matter):** The pure executable
information of the file. It directly drives Meaningful LOC, Branch
Angle, and Structural Flux. Its integrity is guaranteed by the
absolute removal of all documentation noise.
-   ***comment_stream***** (Ghost Mass):** The isolated literature of
the project. It is scanned for Technical Debt markers (TODO, HACK),
authorship, and compliance tags. It serves as the baseline for Trust
Dampening, measuring the delta between the logic\'s behavior and the
author\'s stated intent.
-   ***coding_loc*****:** The exact integer count of non-empty,
pure-logic lines.
-   ***doc_loc*****:** The exact integer count of documentation lines,
normalized to prevent double-counting.

####
