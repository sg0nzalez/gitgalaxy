# GitGalaxy Config (The Master Registry)

> **The Central Nervous System**
>
> The `gitgalaxy_config.py` file serves as the master configuration registry for the entire GitGalaxy engine. Rather than hardcoding thresholds, timeouts, and project-specific quirks deep inside the analytical lenses, all global constants and dynamic overrides are centrally managed here. 
>
> This design allows architects to instantly tune the engine's performance—from adjusting the AI threat tolerance to extending the Chronometer's historical lookback—without modifying the core physics engines.

## The Chronometer Configuration (`CHRONOMETER_CONFIG`)

To maintain hyper-scale velocity when reading Git histories, the config defines strict temporal boundaries and kill-switches:

* **`DYNAMIC_WINDOW_MIN_DAYS` (30):** The absolute minimum lookback period. Ensures brand-new repositories still generate a sufficient volatility baseline.
* **`DYNAMIC_WINDOW_MAX_DAYS` (365):** The "Museum Demo Protocol" cap. Prevents the engine from grinding through decades of ancient bedrock on massive legacy projects.
* **`DORMANT_FALLBACK_COMMITS` (500):** If the dynamic time window yields zero events, the engine falls back to fetching this flat volume of commits.
* **`STREAM_TIMEOUT_SECONDS` (15.0 - 60.0):** The hardware guillotine limit for the `Popen` Git log stream, preventing OS-level zombie processes if Git hangs.
* **`FALLBACK_SCAN_LIMIT` (25000):** The maximum number of files to evaluate when falling back to OS-level `mtime` scans in non-Git environments, protecting disk I/O.

## Project Overrides (Dialect Injection)

Because programming languages are not monolithic, the `PROJECT_OVERRIDES` registry acts as a hot-patching system for specific repositories. 

If the user targets a known legacy or idiosyncratic repository (e.g., the FreeBSD kernel, `cpython`, or an `ansible` playbook repo), the Orchestrator intercepts the `PROJECT_OVERRIDES` dictionary before the scan begins. It dynamically patches the standard `LANGUAGE_DEFINITIONS` in RAM, allowing the regex sensors to perfectly parse the specific structural dialect of that project without polluting the global language standards.

## Dynamic Lore & Story Injection (`PROJECT_STORIES`)

GitGalaxy is not just a security tool; it is an architectural visualizer. The `PROJECT_STORIES` registry maps specific repository names to human-readable narratives. 

When the `GPURecorder` serializes the final 3D map, it pulls from this config to inject:
* **Status & Why:** The high-level objective and health status of the repository.
* **Significance:** Why this specific codebase matters to the broader enterprise.
* **Highlighted Artifacts:** Specific files or clusters that the user should be drawn to in the visualizer (e.g., the core event loop, a specific vulnerability cluster).

## Aperture Black Holes (`APERTURE_CONFIG`)

While the `.gitignore` specifies what shouldn't be tracked by version control, the `APERTURE_CONFIG` defines what should be completely invisible to the physics engines. It contains the `BLACK_HOLES` set—a global list of directories (`node_modules`, `.venv`, `dist`, `__pycache__`) that are violently bypassed during both the initial filesystem survey and the Chronometer's OS-level fallbacks.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
