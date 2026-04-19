# The Chronometer (Temporal Telemetry)

> **Adding History to the Map**
>
> The Chronometer (`chronometer.py`) acts as GitGalaxy's high-fidelity Temporal Sensor. While the rest of the pipeline analyzes the static, physical structure of the code at a single point in time, the Chronometer measures Git churn and physical file-system stability. 
>
> By extracting these temporal signals, it provides the "redshift" and volatility of artifacts over time, providing raw telemetry to the Signal Processor for exposure calculations.

## The Melded Protocol (Survey-First Logic)

If the engine attempted to query Git history for every single file during the parallel multiprocessing phase, it would create a catastrophic I/O bottleneck. 

To achieve hyper-scale velocity, the Chronometer utilizes **Survey-First Logic**. It performs a bulk metadata sweep during initialization, caching the results in internal state maps (`entropy_map`, `mtime_map`, `author_map`). When the worker threads later request temporal data for a specific file, the handover is a lightning-fast, zero-I/O $O(1)$ memory lookup.

## Boundary Locks & The Museum Demo Protocol

To accurately calculate how "old" or "stable" a file is, the engine must first establish the absolute boundaries of the universe.

* **Boundary Lock:** The sensor queries the Git `rev-list` and log heads to establish the absolute minimum (first commit) and maximum (latest commit) timestamps of the entire project.
* **Cosmetic Filter:** Before sweeping for churn, the Chronometer automatically loads `.git-blame-ignore-revs` if it exists, filtering out non-functional cosmetic commits (like mass code-formatting) from the volatility math.
* **The Museum Demo Protocol:** Rather than grinding through decades of Git history, the sensor executes a 1-year historical sweep. This guarantees deep churn data for modern volatility without getting bogged down in ancient bedrock.
* **Dynamic Thresholds:** To save RAM and CPU, the scanner dynamically halts once it has mapped 50% of the active repository, or hits a hard cap of 5,000 files.

## Process Management (Kill Switches & Fallbacks)

Streaming Git logs via `Popen` can be dangerous; if the stream hangs, it creates zombie processes that leak file descriptors. The Chronometer enforces strict resource guards.

* **Dual Kill Switches:** The Git stream escalator is bound by two strict kill switches: a hard compute timeout (defaulting to 15.0 seconds) and the dynamic file coverage target. If either is breached, the loop breaks early.
* **Zombie Prevention:** If the stream is broken early, the Chronometer violently kills the `Popen` process and explicitly closes the `stdout`/`stderr` pipes to prevent OS-level zombie processes.
* **OS-Level Fallback:** If the repository is not tracked by Git (or Git is missing from the host machine), the Chronometer falls back to standard operating system `stat` calls to check file modification times (`mtime`). This fallback is capped at 25,000 files to protect disk I/O performance.

## Temporal Outputs (The Handover)

The Chronometer does not calculate final risk scores; it acts as a raw sensor, extracting the temporal data required by the `SignalProcessor` to calculate the final metrics:

* **Stability (Age):** Hands over the exact modification time (`mtime`) and the repository's minimum/maximum timestamps.
* **Raw Churn Frequency:** Captures the total commit count within the historical sweep.
* **Ownership Mapping:** Captures every author who modified the file and their respective commit counts. This powers the downstream **Ownership Entropy** and **Silo Risk** calculations.