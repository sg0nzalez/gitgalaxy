# 2.3.7. Phase 0: Mission Control (The GalaxyScope Orchestrator)

The GalaxyScope Orchestrator (**galaxyscope.py**) is the central nervous
system of the blAST engine. It acts as Mission Control, managing the
flow of data from the initial file-system radar ping down to the final
serialization of the 3D map. Its primary responsibility is maximizing
computational velocity while preventing catastrophic memory leaks or
regex deadlocks during hyper-scale scans.

## 2.3.7.A. Multi-Core Extraction (The Worker Pool)

Parsing millions of lines of code on a single thread is a bottleneck. To
achieve hyper-scale velocity (100,000+ LOC/s), the Orchestrator
implements a highly tuned **ProcessPoolExecutor** Map-Reduce
architecture.

-   **Isolated Memory Spaces:** The **\_init_worker** function boots
copies of the heavy regex engines (**LogicSplicer**, **Prism**,
**LanguageDetector**) directly into the isolated memory of each CPU
core. This prevents cross-thread lockups.
-   **Cache Warming:** The workers force-warm the regex compilers for
the specific languages found in the repository during the radar
ping, completely eliminating the \"Plaintext Stutter\" (lazy-loading
lag) on the first few thousand files.
-   **The Phantom Check:** Workers perform an instantaneous disk-check
before parsing. If a file was reported by Git but has since vanished
from the disk, it is silently evaporated as a \"Phantom,\"
preventing the main thread from logging false anomalies.

## 2.3.7.B. The Starvation Monitor (ReDoS Shield)

When scanning massive, auto-generated codebases, poorly written files
can occasionally trigger Catastrophic Regex Backtracking (ReDoS), which
locks a CPU core in an infinite loop.

-   **The 60-Second Guillotine:** Instead of blindly waiting for the
worker pool to finish, the Orchestrator uses a
**concurrent.futures.wait** loop. If all CPU workers freeze and fail
to return a single processed file within 60 seconds, the Starvation
Monitor detects the deadlock.
-   **Graceful Abort:** It instantly logs the exact file paths that
caused the hang, relegates them to the Singularity audit log, and
forcefully shuts down the executor pool to unfreeze the user\'s
terminal.

## 2.3.7.C. O(1) Relational Resolution (Pass 1.5)

To build the dependency graph, the engine must figure out which files
are importing which other files. Cross-referencing thousands of raw
import strings (e.g., **import utils**) against thousands of file paths
(e.g., **src/core/utils.py**) originally created an exponential
\$O(N\^2)\$ compute bomb.

-   **The Suffix Hash Map:** Pass 1.5 defuses this bomb. It pre-computes
every possible valid path suffix for every file in the repository
and stores them in a lightning-fast hash map.
-   **O(1) Lookups:** When evaluating a raw import string, the engine
simply checks if the string exists as a key in the map. This turns
an exponential search into an instantaneous \$O(1)\$ lookup,
allowing GitGalaxy to resolve millions of dependency links in
milliseconds.

## 2.3.7.D. Relational Context & Mass Dampeners (Pass 2)

In Pass 2, the Orchestrator evaluates files based on their surrounding
neighborhood before handing them off to the Signal Processor.

-   **Domain Ontologies:** It tallies the languages in every folder to
determine the \"Dominant Ecosystem,\" allowing downstream engines to
spot Trojan files (e.g., a C++ file hiding in a JavaScript folder).
-   **The Umbrella Shield:** It calculates the total percentage of the
repository dedicated to testing (**/tests/** folders). If a repo is
heavily tested globally, the Orchestrator applies an \"Umbrella
Bonus\" that mathematically dampens the testing risk for individual
logic files.
-   **Structural Mass Dampeners:** It intercepts files acting as heavy,
non-executable data dumps (like Wycheproof test vectors, vendored
Kubernetes code-gen, or massive translation dictionaries) and
physically crushes their mass multiplier so they do not
mathematically eclipse the human-written architecture in the 3D
view.

## 2.3.7.E. The CLI & Smart Threat Switch

The **main()** entry point manages user interaction and environment
overrides.

-   **Dialect Injection:** It intercepts the **PROJECT_OVERRIDES**
registry. If the user is scanning a known legacy repository (like
the FreeBSD kernel), it dynamically hot-patches the
**LANGUAGE_DEFINITIONS** in RAM to parse its specific dialect
perfectly.
-   **The Smart Threat Switch (**\--paranoid**):** If invoked,
the Orchestrator loads the \"Hazmat Suit\" threat policy, lowering
the threshold for the Security Lens to flag deeply hidden
steganography and logic bombs.
-   **Instant RAM Eviction:** Once the artifacts are sealed to the disk,
the CLI invokes a hard **os.\_exit(0)**. This violently drops the
Python process, instantly freeing gigabytes of RAM back to the
operating system without waiting for the garbage collector to slowly
unwind the massive AST dictionaries.
