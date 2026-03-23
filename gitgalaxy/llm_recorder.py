# ==============================================================================
# GitGalaxy
# Copyright (c) 2026 Joe Esquibel
#
# This source code is licensed under the PolyForm Noncommercial License 1.0.0.
# You may not use this file except in compliance with the License.
# A copy of the license can be found in the LICENSE file in the root directory
# of this project, or at https://polyformproject.org/licenses/noncommercial/1.0.0/
# ==============================================================================
import sqlite3
import logging
import statistics
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
from . import gitgalaxy_standards_v011 as config

# ==============================================================================
# GitGalaxy Phase 10: LLM Recorder (The AI Translation Layer)
# Strategy v6.3.0 Protocol: Token Density, Distribution Physics & RAG Graphs
# ==============================================================================

class LLMRecorder:
    """
    PURPOSE: Translates raw GitGalaxy telemetry into AI-optimized artifacts.
    
    FEATURES:
    1. Statistical Physics: Calculates Min/Max/Mean/Median/Mode for all risks.
    2. Syntactic Bottlenecks: Isolates I/O and Dependency choke points.
    3. God Functions: Ranks top 10 satellites by individual magnitude.
    4. Relational Knowledge Graph: Builds a SQLite DB for autonomous agents.
    5. Markdown Brief: Token-compressed text for standard LLM context windows.
    """

    def __init__(self, parent_logger: Optional[logging.Logger] = None):
        if parent_logger:
            self.logger = parent_logger.getChild("llm_recorder")
            self.logger.setLevel(parent_logger.level)
        else:
            self.logger = logging.getLogger("llm_recorder")
            self.logger.setLevel(logging.INFO)

        # --- DYNAMIC SCHEMA FETCH ---
        schemas = getattr(config, "RECORDING_SCHEMAS", {})
        self.RISK_SCHEMA = schemas.get("RISK_SCHEMA", [])
        self.SIGNAL_SCHEMA = schemas.get("SIGNAL_SCHEMA", [])

    def generate_artifacts(
        self, 
        stars: List[Dict[str, Any]], 
        singularity: List[Dict[str, Any]], 
        summary: Dict[str, Any], 
        session_meta: Dict[str, Any], 
        output_dir: str,
        forensic_report: Optional[Dict[str, Any]] = None
    ):
        """Generates the dual-output AI artifacts: Markdown and SQLite."""
        if forensic_report is None:
            forensic_report = {}
            
        # --- ABSOLUTE ROUTING LOGIC (Matching Audit Recorder) ---
        base_dir = Path("/srv/storage_16tb/projects/gitgalaxy/data")
        base_dir.mkdir(parents=True, exist_ok=True)
            
        target_name = session_meta.get("target", "unknown_project")
        output_path_md = base_dir / f"{target_name}_galaxy_llm.md"
        output_path_db = base_dir / f"{target_name}_galaxy_graph.sqlite"
        
        self.logger.info(f"Initiating LLM Artifact Generation for '{target_name}'...")
        
        # --- REVERSE DEPENDENCY RESOLUTION (Calculated once for both outputs) ---
        resolution_map = {}
        for s in stars:
            path = s.get("path", "")
            name = s.get("name", Path(path).name)
            stem = Path(path).stem
            if path: resolution_map[path] = path
            if name: resolution_map[name] = path
            if stem: resolution_map[stem] = path

        inbound_map = {s.get("path", ""): [] for s in stars}
        for s in stars:
            curr = s.get("path", "")
            for imp in s.get("raw_imports", []):
                if imp in resolution_map:
                    target_path = resolution_map[imp]
                    if target_path != curr and curr not in inbound_map[target_path]:
                        inbound_map[target_path].append(curr)

        # 1. Build the Relational Knowledge Graph
        self._generate_sqlite_graph(stars, singularity, summary, session_meta, output_path_db, inbound_map)
        
        # 2. Build the Token-Optimized Markdown Brief
        md_content = self._build_markdown(stars, singularity, summary, session_meta, forensic_report, inbound_map)
        
        try:
            with open(output_path_md, "w", encoding="utf-8") as f:
                f.write(md_content)
            self.logger.info(f"AI Mission Complete:\n -> Markdown: {output_path_md}\n -> SQLite: {output_path_db}")
        except Exception as e:
            self.logger.error(f"Failed to seal LLM brief: {e}", exc_info=True)
    
    def _build_dependency_analysis(self, stars: List[Dict]) -> str:
        """Generates rankings for the most critical architectural dependencies."""
        if not stars:
            return ""

        # 1. Top Structural Pillars (Imported By / Blast Radius)
        pillars = sorted(
            stars, 
            key=lambda x: x.get("telemetry", {}).get("popularity", 0) if isinstance(x.get("telemetry"), dict) else 0, 
            reverse=True
        )[:5]

        # 2. Top Orchestrators (Imports / Fragility Index)
        orchestrators = sorted(
            stars,
            key=lambda x: len(x.get("raw_imports", [])) if isinstance(x.get("raw_imports"), list) else 0,
            reverse=True
        )[:5]

        lines = ["### Architectural Dependencies\n"]
        
        lines.append("#### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)")
        lines.append("These files act as core load-bearing infrastructure. Changes here carry a high risk of cascading breaks.\n")
        for rank, star in enumerate(pillars, 1):
            name = star.get("name", "Unknown")
            path = star.get("path", "Unknown")
            count = star.get("telemetry", {}).get("popularity", 0) if isinstance(star.get("telemetry"), dict) else 0
            lines.append(f"{rank}. **{name}** (`{path}`) — {count} inbound connections")
        lines.append("\n")

        lines.append("#### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)")
        lines.append("These files pull in the most external dependencies. They are highly coupled and fragile to API changes.\n")
        for rank, star in enumerate(orchestrators, 1):
            name = star.get("name", "Unknown")
            path = star.get("path", "Unknown")
            count = len(star.get("raw_imports", [])) if isinstance(star.get("raw_imports"), list) else 0
            lines.append(f"{rank}. **{name}** (`{path}`) — {count} outbound dependencies")
        lines.append("\n")

        return "\n".join(lines)
    
    def _build_markdown(
        self, 
        stars: List[Dict[str, Any]], 
        singularity: List[Dict[str, Any]], 
        summary: Dict[str, Any], 
        session_meta: Dict[str, Any],
        forensic_report: Dict[str, Any],
        inbound_map: Dict[str, List[str]]
    ) -> str:
        """Constructs a high-density, context-rich Markdown brief for LLM agents."""
        target = session_meta.get("target", "Project")
        sum_data = summary.get("summary", {})
        health = summary.get("health", {})
        comp = summary.get("composition", {})
        git_audit = session_meta.get("git_audit", {})
        
        bypassed_count = summary.get("singularity", {}).get("unparsable", 0)
        total_excluded = len(singularity) + bypassed_count
        visible_count = sum_data.get("visible_stars", len(stars))
        
        lines = []
        lines.append(f"# ARCHITECTURAL_BRIEF: {target}")
        lines.append("> INSTRUCTION: Deterministic Syntactic Physics. Base architectural insights on Mass, DNA, and Risk overlays.\n")
        
        # --- 0. FORENSIC TRACEABILITY ---
        lines.append("## 0. FORENSIC TRACEABILITY")
        lines.append("| Metadata | Value |")
        lines.append("|---|---|")
        lines.append(f"| **Engine** | `{session_meta.get('engine', 'Unknown')}` |")
        lines.append(f"| **Target Path** | `{session_meta.get('target_directory', 'Unknown')}` |")
        lines.append(f"| **Timestamp** | `{session_meta.get('timestamp', 'Unknown')}` |")
        lines.append(f"| **Scan Duration** | `{session_meta.get('duration_seconds', 0.0)}s` |")
        lines.append(f"| **Git Branch** | `{git_audit.get('branch', 'N/A')}` |")
        lines.append(f"| **Git Commit** | `{git_audit.get('commit_hash', 'N/A')}` |")
        lines.append(f"| **Git Remote** | `{git_audit.get('remote_url', 'N/A')}` |")
        lines.append("")
        
        # --- 1. CRITICAL SYSTEM INSTRUCTIONS & LEXICON ---
        lines.append("## 1. SYSTEM ROLE & PHILOSOPHY")
        lines.append("> Code is art. Logic is art. Systems engineering is art.")
        lines.append("> You are analyzing software architecture through the lens of GitGalaxy. GitGalaxy acts as a Rosetta Stone for code complexity, translating the non-visual architecture of repositories into measurable metrics.")
        lines.append("> ")
        lines.append("> **CORE DIRECTIVES:**")
        lines.append("> 1. **Measure Risk, Not Quality:** Do not judge. We do not assess 'Bad Code'; we measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into dangerous territory, not incompetence.")
        lines.append("> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural DNA (regex hit counts). Do not hallucinate meaning.")
        lines.append("> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.")
        lines.append("> ")
        lines.append("> **THE STRUCTURAL DNA LEXICON:**")
        lines.append("> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).")
        lines.append("> * **Risk & Volatility:** `danger` (catastrophic triggers), `flux` (state mutation), `graveyard` (dead code), `safety_neg` (bypassing types).")
        lines.append("> * **Architecture & Domain:** `io` (external latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).")
        lines.append("> * **Defensive Guardrails:** `safety` (error handling), `freeze_hits` (immutability), `cleanup` (state destruction).")
        
        # --- 2. 13-POINT RISK PHYSICS (THE EQUATIONS) ---
        lines.append("## 2. THE 13-POINT RISK EXPOSURE PHYSICS (EQUATIONS & CONTEXT)")
        lines.append("> **How the Physics Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**")
        lines.append("> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.")
        lines.append("> ")
        lines.append("> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`. High scores indicate a high density of decision-making, conditional branching, and complex state management packed into a small area.")
        lines.append("> 2. **Safety Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`. High scores mean risky operations (dynamic execution, type bypasses, unhandled mutations) exceed defensive guardrails (try/catch blocks, type checks, assertions). **Breach Cap:** If danger density is too high, the score is mathematically floored to a high-risk state regardless of defense.")
        lines.append("> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`. High scores indicate a high volume of temporary workarounds, fragile logic, and incomplete implementations relative to the file size.")
        lines.append("> 4. **Verification (Testing) Risk Exposure:** Measures the density of unit testing and programmatic assertions. Evaluates `Test Density` + `Sibling Bonus` (if a dedicated test file exists). High scores (100% risk) mean the logic lacks internal test coverage and has no dedicated sibling test file, increasing the risk of silent failures during refactoring. **Mass Penalty:** Files over 300 LOC get an automatic risk penalty because massive files are inherently harder to test completely.")
        lines.append("> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`. Weighted by logarithmic volume. High scores indicate that a large percentage of the file's functions and classes are explicitly exported or publicly accessible by external systems.")
        lines.append("> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic. `Density(Async/Thread Hits)`. High scores indicate a high risk of race conditions, deadlocks, and complex execution timing issues.")
        lines.append("> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment. `Density(State Mutations / LOC)`. High scores indicate unstable data states with constant side-effects, making state tracking difficult and unpredictable.")
        lines.append("> 8. **Graveyard (commented out code):** Measures the presence of abandoned, commented-out logic blocks. `Density(Commented-out Code / LOC)`. High scores indicate messy refactoring trails that create visual clutter and confusion for maintainers.")
        lines.append("> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements. `Inverse Ratio(Spec Hits / Total Functions)`. 100% Risk means no functions are tagged to a specification (undocumented exploratory logic); 0% means all logic is explicitly anchored to documented requirements.")
        lines.append("> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan. `Ratio(Seconds from Last Edit / Total Repo Lifespan)`. 100% Risk = Edited very recently; 0% Risk = Untouched for a long period.")
        lines.append("> 11. **Deep Churn:** Measures the historical volatility and frequency of modification. `(Commits / sqrt(Age in Weeks))`. Normalized globally so the file with the most commits relative to its age is always 100%, indicating a constant hotspot for changes.")
        lines.append("> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata. `Inverse Density(Doc Hits + Ownership / LOC)`. High risk means the file contains complex logic but lacks explanatory comments or structured metadata tags (like JSDoc) for developers.")
        lines.append("> 13. **Civil War - DONT MENTION:** Measures formatting consistency regarding indentation. 0% = File is in pure Tabs, 100% = File is in Pure Spaces, 50% = Mixed indentation. (Provided for human context, not a functional risk) DO NOT MENTION THIS ONE .")
        lines.append("> ")
        lines.append("> **14. Structural Mass (Gravity):** Calculates total structural complexity. It weights files based on decision-making density (branches), parameter coupling (args), and raw size (LOC) to identify the most logically dense components. `((Branches + 1) * (Args + 1) + (0.05 * LOC))`.")
        lines.append("> **15. Author Distribution (Silo Risk/Bus Factor):** Measures knowledge concentration based on commit history. 100% means a single developer wrote all the code (High Bus Factor); 0% means contributions are evenly distributed across multiple team members. Look for high-mass orchestrators with 100% Silo Risk—these are prime architectural vulnerabilities if that developer leaves.")
        lines.append("")

        # --- 3. MACRO ECOSYSTEM ---
        lines.append("## 3. MACRO STATE")
        lines.append("| Metric | Value |")
        lines.append("|---|---|")
        lines.append(f"| Total Artifacts | {sum_data.get('total_files', 0)} |")
        lines.append(f"| Visible Matter (Scanned) | {visible_count} |")
        lines.append(f"| Dark Matter (Non-scanned - binaries, images, extensions without definitions) | {total_excluded} |")
        lines.append(f"| Total LOC | {sum_data.get('total_loc', 0)} |")
        lines.append(f"| Volatility Index | {sum_data.get('volatility_index', 0.0)} |")
        lines.append(f"| % Scanned of codebase = | {sum_data.get('Percent_Visible', 0)}% |")
        lines.append(f"| Dominant Lang | {sum_data.get('dominant_language', 'UNK').upper()} |")
        lines.append("")

        # --- 4. LINGUISTIC COMPOSITION ---
        lines.append("## 4. COMPOSITION")
        if comp:
            lines.append("| Lang | Files | LOC | Share |")
            lines.append("|---|---|---|---|")
            total_visible = max(visible_count, 1)
            for lang, stats in sorted(comp.items(), key=lambda x: x[1].get("files", 0), reverse=True):
                pct = (stats.get('files', 0) / total_visible) * 100
                lines.append(f"| {lang.upper()} | {stats.get('files', 0)} | {stats.get('loc', 0)} | {pct:.1f}% |")
        lines.append("")

        # --- 5. DARK MATTER ---
        lines.append("## 5. DARK MATTER (Non-scanned items ARTIFACTS)")
        lines.append(f"*Total Excluded Artifacts: {total_excluded}*\n")
        
        comp_breakdown = summary.get("singularity", {}).get("composition_by_extension_and_reason", {})
        
        if comp_breakdown:
            lines.append("**Composition by Extension & Reason:**")
            for ext, reasons in list(comp_breakdown.items())[:15]:
                clean_reasons = []
                for rsn, count in list(reasons.items())[:3]:
                    safe_rsn = (rsn.replace("Unparsable", "Unrecognized Syntax")
                                   .replace("Structural Saturation", "Dense Structure")
                                   .replace("Singularity", "Dark Matter")
                                   .replace("Necrosis", "Optical Bypass")
                                   .replace("Blocked", "Excluded"))
                    clean_reasons.append(f"{count}x {safe_rsn.strip()}")
                
                reason_str = ", ".join(clean_reasons)
                lines.append(f"- `{ext}`: {reason_str}")
        else:
            legacy_breakdown = summary.get("singularity", {}).get("breakdown", {})
            sing_items = []
            for k, v in sorted(legacy_breakdown.items(), key=lambda x: x[1] if isinstance(x[1], int) else 0, reverse=True):
                if isinstance(v, int) and v > 0:
                    safe_k = k.replace("unparsable", "optical_bypass")
                    sing_items.append(f"`{safe_k}`:{v}")
            lines.append(" | ".join(sing_items))
            
        lines.append("")

        # --- 6. RISK DISTRIBUTIONS ---
        lines.append("## 6. RISK EXPOSURE PHYSICS (0-100%)")
        lines.append("| Risk Vector | Min | Max | Mean | Med | Mode |")
        lines.append("|---|---|---|---|---|---|")
        
        schemas = getattr(config, "RECORDING_SCHEMAS", {})
        exposure_labels = schemas.get("EXPOSURE_LABELS", {})
        
        for i, risk_slug in enumerate(self.RISK_SCHEMA):
            vals = [s.get("risk_vector", [])[i] for s in stars if len(s.get("risk_vector", [])) > i]
            risk_label = exposure_labels.get(risk_slug, risk_slug.replace('_', ' ').title())
            
            if vals:
                v_min, v_max = round(min(vals), 1), round(max(vals), 1)
                v_mean, v_med = round(statistics.mean(vals), 1), round(statistics.median(vals), 1)
                try: v_mode = round(statistics.mode(vals), 1)
                except statistics.StatisticsError: v_mode = "N/A"
                lines.append(f"| {risk_label} | {v_min} | {v_max} | {v_mean} | {v_med} | {v_mode} |")
            else:
                lines.append(f"| {risk_label} | - | - | - | - | - |")
        lines.append("")

        # --- 7. SYNTACTIC BOTTLE-NECKS & DEPENDENCIES ---
        lines.append("## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES")
        
        # 7.A: I/O Bottlenecks
        io_idx = self.SIGNAL_SCHEMA.index("io") if "io" in self.SIGNAL_SCHEMA else -1
        if io_idx >= 0:
            top_io = sorted(stars, key=lambda x: x.get("hit_vector", [])[io_idx] if len(x.get("hit_vector", [])) > io_idx else 0, reverse=True)[:3]
            lines.append("### Top I/O Latency Risks")
            for s in top_io: 
                lines.append(f"- `{s.get('path')}` (Hits: {s.get('hit_vector', [])[io_idx]})")
            lines.append("")

        # 7.B: Structural Pillars (Imported By)
        pillars = sorted(stars, key=lambda x: len(inbound_map.get(x.get("path", ""), [])), reverse=True)[:5]
        lines.append("### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)")
        lines.append("These files act as core load-bearing infrastructure. Changes here carry a high risk of cascading breaks.\n")
        for rank, star in enumerate(pillars, 1):
            name = star.get("name", "Unknown")
            path = star.get("path", "Unknown")
            count = len(inbound_map.get(path, []))
            lines.append(f"{rank}. **{name}** (`{path}`) — {count} inbound connections")
        lines.append("")

        # 7.C: Orchestrators (Imports)
        orchestrators = sorted(stars, key=lambda x: len(x.get("raw_imports", [])) if isinstance(x.get("raw_imports"), list) else 0, reverse=True)[:5]
        lines.append("### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)")
        lines.append("These files pull in the most external dependencies. They are highly coupled and fragile to API changes.\n")
        for rank, star in enumerate(orchestrators, 1):
            name = star.get("name", "Unknown")
            path = star.get("path", "Unknown")
            count = len(star.get("raw_imports", [])) if isinstance(star.get("raw_imports"), list) else 0
            lines.append(f"{rank}. **{name}** (`{path}`) — {count} outbound dependencies")
        lines.append("")

        # --- 8. GOD FUNCTIONS (THE SATELLITES) ---
        lines.append("## 8. SATELLITE HITLIST (God Functions)")
        func_impacts = forensic_report.get("function_impact", {}).get("highest", [])
        if func_impacts:
            for f in func_impacts[:10]:
                lines.append(f"- `{f.get('name')}` (@ `{f.get('file')}`) -> Impact: {f.get('impact')} | LOC: {f.get('loc')}")
        else:
            lines.append("*No complex satellites detected.*")
        lines.append("")

        # --- 9. TOP CONSTELLATIONS ---
        lines.append("## 9. CONSTELLATIONS (Top 10 Heaviest Folders)")
        constellations = summary.get("constellations", {})
        if constellations:
            lines.append("| Folder Path | Files | Total Mass | Avg Cog Load | Avg Debt |")
            lines.append("|---|---|---|---|---|")
            
            sorted_consts = sorted(
                constellations.items(), 
                key=lambda x: x[1].get("total_mass", 0.0), 
                reverse=True
            )[:10]
            
            for c_name, c_data in sorted_consts:
                mass = c_data.get('total_mass', 0.0)
                count = c_data.get('file_count', 0)
                exposures = c_data.get('avg_exposures', {})
                cog = exposures.get('cognitive_load', 0.0)
                debt = exposures.get('tech_debt', 0.0)
                lines.append(f"| `{c_name}` | {count} | {mass} | {cog}% | {debt}% |")
        else:
            lines.append("*No deep folder structures detected.*")
        lines.append("")

        # --- 10. TARGETED RISK VECTORS ---
        lines.append("## 10. TARGETED RISK VECTORS (Top 5 by Exposure)")
        
        # Tech Debt Hitlist
        debt_idx = self.RISK_SCHEMA.index("tech_debt") if "tech_debt" in self.RISK_SCHEMA else -1
        if debt_idx >= 0:
            high_debt = sorted([s for s in stars if len(s.get("risk_vector", [])) > debt_idx], key=lambda x: x.get("risk_vector")[debt_idx], reverse=True)[:5]
            if high_debt and high_debt[0].get("risk_vector")[debt_idx] > 0:
                lines.append("### Highest Tech Debt (Fragile/Planned)")
                for s in high_debt:
                    if s.get("risk_vector")[debt_idx] > 0:
                        lines.append(f"- `{s.get('path')}` -> **{s.get('risk_vector')[debt_idx]}%** Exposure")
                        
        # State Flux (Volatility) Hitlist
        flux_idx = self.RISK_SCHEMA.index("state_flux") if "state_flux" in self.RISK_SCHEMA else -1
        if flux_idx >= 0:
            high_flux = sorted([s for s in stars if len(s.get("risk_vector", [])) > flux_idx], key=lambda x: x.get("risk_vector")[flux_idx], reverse=True)[:5]
            if high_flux and high_flux[0].get("risk_vector")[flux_idx] > 0:
                lines.append("### Highest State Flux (Mutation/Volatility)")
                for s in high_flux:
                    if s.get("risk_vector")[flux_idx] > 0:
                        lines.append(f"- `{s.get('path')}` -> **{s.get('risk_vector')[flux_idx]}%** Exposure")
        lines.append("")

        # --- 11. VISIBLE MATTER HITLIST ---
        lines.append("## 11. VISIBLE MATTER HITLIST (Top 25 Heaviest Files)")
        sorted_stars = sorted(stars, key=lambda x: x.get("file_impact", 0.0), reverse=True)[:25]
        
        # DNA Bucketing Sets
        structure_keys = {"branch", "linear", "args", "func_start", "class_start"}
        risk_keys = {"danger", "flux", "graveyard", "safety_neg", "planned_debt", "fragile_debt"}
        arch_keys = {"io", "concurrency", "api", "import"}
        defense_keys = {"safety", "freeze_hits", "cleanup", "test", "sync_locks", "doc"}
        
        for s in sorted_stars:
            p = s.get("path", "UNK")
            l = s.get("lang_id", "UNK").upper()
            m = s.get("file_impact", 0.0)
            loc = s.get("total_loc", 0)
            
            rv = s.get("risk_vector", [])
            tel = s.get("telemetry", {})
            cog = rv[0] if len(rv) > 0 else 0.0
            debt = rv[2] if len(rv) > 2 else 0.0
            
            # Extract advanced telemetry
            lock_tier = s.get("lock_tier", tel.get("identity_lock_tier", 4))
            purpose = tel.get("domain_context", {}).get("purpose", "")
            
            lines.append(f"### `{p}` ({l} | Tier {lock_tier})")
            if purpose:
                lines.append(f"> **Stated Purpose:** *{purpose}*")
                
            lines.append(f"- **Mass:** {m} | **LOC:** {loc} | **CtrlFlow:** {round(tel.get('control_flow_ratio', 0.0) * 100, 1)}% | **Silo Risk:** {round(tel.get('author_distribution', 0.0), 1)}%")
            lines.append(f"- **Risk Profile:** Cognitive Load ({cog}%), Tech Debt ({debt}%)")
            
            # Bucket the DNA Hits
            hv = s.get("hit_vector", [])
            struct_hits, risk_hits, arch_hits, def_hits = [], [], [], []
            
            for i, val in enumerate(hv):
                if val > 0 and i < len(self.SIGNAL_SCHEMA):
                    key = self.SIGNAL_SCHEMA[i]
                    hit_string = f"`{key}: {val}`"
                    if key in structure_keys: struct_hits.append(hit_string)
                    elif key in risk_keys: risk_hits.append(hit_string)
                    elif key in arch_keys: arch_hits.append(hit_string)
                    elif key in defense_keys: def_hits.append(hit_string)
                    
            # --- Add this right below your DNA bucketing lines ---
            sats = sorted(s.get("satellites", []), key=lambda x: x.get("impact", 0), reverse=True)[:5]
            if sats:
                lines.append("**Top Internal Satellites (Functions/Classes):**")
                for sat in sats:
                    lines.append(f"  * `{sat.get('name')}` (Impact: {sat.get('impact')} | LOC: {sat.get('loc')} | Branches: {sat.get('branch', 0)})")
            
            lines.append("**Structural DNA (Raw Regex Hits):**")
            lines.append(f"* *Structure:* {', '.join(struct_hits) if struct_hits else 'None'}")
            lines.append(f"* *Risk/State:* {', '.join(risk_hits) if risk_hits else 'None'}")
            lines.append(f"* *Architecture:* {', '.join(arch_hits) if arch_hits else 'None'}")
            lines.append(f"* *Defense:* {', '.join(def_hits) if def_hits else 'None'}")
            
            # Dependency Graph Mapping (Named Edges)
            inbound = inbound_map.get(p, [])
            outbound = s.get("raw_imports", [])
            
            in_names = ", ".join([Path(x).name for x in inbound[:8]]) + ("..." if len(inbound) > 8 else "")
            out_names = ", ".join([Path(x).name for x in outbound[:8]]) + ("..." if len(outbound) > 8 else "")
            
            lines.append(f"* *Dependencies:*")
            lines.append(f"  * `Imports ({len(outbound)}):` {out_names if out_names else 'None'}")
            lines.append(f"  * `Imported By ({len(inbound)}):` {in_names if in_names else 'None (Orphan / Entrypoint)'}")
            lines.append("")
            
            # --- 11. SYSTEM PROMPT: HOW TO RESPOND ---
        lines.append("## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)")
        lines.append("> **When the user asks for an architectural review, structure your response using plain, common descriptions suitable for engineers and managers:**")
        lines.append("> 1. **The Bird's Eye View (Executive Summary):** Look at the Language Composition and Top Dependencies to provide a high-level description of what the system actually *is* and how data flows (e.g., 'This system operates as a C++ core surrounded by Python wrappers for data orchestration'). Diagnose the overarching health and paradigm of the codebase.")
        lines.append("> 2. **Key Files & Functions:** Identify the top 2-3 files that have the greatest impact on the system (cross-reference high Mass, high Dependencies/Imports, and high Risk Exposures). Explain *why* they are risky using plain language.")
        lines.append("> 3. **Risk Exposure impacts, Assess for multiple high or conflicting risk exposures and describe what these likely mean for the system at learge")
        lines.append("> 4. **Architecture consistency:** Assess for consistent practices, structure, if the system seems to be experiencing under or over growth based on provided data for architecture")
        lines.append("> 5. **Recommended Next Steps:** Provide 2-3 pragmatic, blameless refactoring targets based on the data. Focus on mitigating cognitive load and increasing testing on the heaviest components.")
        lines.append("")
            
        return "\n".join(lines)
    
    def _generate_sqlite_graph(
        self, 
        stars: List[Dict[str, Any]], 
        singularity: List[Dict[str, Any]], 
        summary: Dict[str, Any], 
        session: Dict[str, Any], 
        db_path: Path,
        inbound_map: Dict[str, List[str]]
    ):
        """Creates a relational database for advanced SQL-based AI analysis."""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute('DROP TABLE IF EXISTS meta')
            cursor.execute('CREATE TABLE meta (key TEXT, value TEXT)')
            cursor.executemany('INSERT INTO meta VALUES (?, ?)', [
                ("engine", session.get("engine")),
                ("project", session.get("target")),
                ("timestamp", session.get("timestamp")),
                ("branch", session.get("git_audit", {}).get("branch")),
                ("commit", session.get("git_audit", {}).get("commit_hash"))
            ])

            cursor.execute('DROP TABLE IF EXISTS stars')
            risk_cols = ", ".join([f"{r} REAL" for r in self.RISK_SCHEMA])
            cursor.execute(f'''
                CREATE TABLE stars (
                    id INTEGER PRIMARY KEY,
                    path TEXT,
                    filename TEXT,
                    constellation TEXT,
                    language TEXT,
                    lock_tier INTEGER,
                    total_loc INTEGER,
                    coding_loc INTEGER,
                    file_impact REAL,
                    control_flow_ratio REAL,
                    author_distribution REAL,
                    popularity INTEGER,
                    {risk_cols}
                )
            ''')

            cursor.execute('DROP TABLE IF EXISTS constellations')
            cursor.execute('''
                CREATE TABLE constellations (
                    name TEXT PRIMARY KEY,
                    file_count INTEGER,
                    total_mass REAL,
                    avg_cognitive_load REAL,
                    avg_safety_score REAL,
                    avg_tech_debt REAL,
                    avg_verification REAL
                )
            ''')

            cursor.execute('DROP TABLE IF EXISTS satellites')
            cursor.execute('''
                CREATE TABLE satellites (
                    id INTEGER PRIMARY KEY,
                    star_id INTEGER,
                    name TEXT,
                    type_id TEXT,
                    loc INTEGER,
                    impact REAL,
                    FOREIGN KEY(star_id) REFERENCES stars(id)
                )
            ''')

            cursor.execute('DROP TABLE IF EXISTS dna_hits')
            cursor.execute('''
                CREATE TABLE dna_hits (
                    star_id INTEGER,
                    signal_type TEXT,
                    hit_count INTEGER,
                    FOREIGN KEY(star_id) REFERENCES stars(id)
                )
            ''')

            # --- Explicit Bi-Directional Dependency Tables ---
            cursor.execute('DROP TABLE IF EXISTS outbound_dependencies')
            cursor.execute('''
                CREATE TABLE outbound_dependencies (
                    star_id INTEGER,
                    imported_path TEXT,
                    FOREIGN KEY(star_id) REFERENCES stars(id)
                )
            ''')

            cursor.execute('DROP TABLE IF EXISTS inbound_dependencies')
            cursor.execute('''
                CREATE TABLE inbound_dependencies (
                    star_id INTEGER,
                    imported_by_path TEXT,
                    FOREIGN KEY(star_id) REFERENCES stars(id)
                )
            ''')

            const_meta = summary.get("constellations", {})
            for c_name, c_data in const_meta.items():
                exps = c_data.get("avg_exposures", {})
                cursor.execute('''
                    INSERT INTO constellations (name, file_count, total_mass, avg_cognitive_load, avg_safety_score, avg_tech_debt, avg_verification)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    c_name, 
                    c_data.get("file_count", 0), 
                    c_data.get("total_mass", 0.0),
                    exps.get("cognitive_load", 0.0),
                    exps.get("safety_score", 0.0),
                    exps.get("tech_debt", 0.0),
                    exps.get("verification", 0.0)
                ))

            for star in stars:
                p = star.get("path")
                c_name = star.get("constellation", "__monolith__")
                tel = star.get("telemetry", {})
                rv = star.get("risk_vector", [0.0] * 13)
                
                # We inject the len() of the inbound map directly into the popularity column!
                pop_count = len(inbound_map.get(p, []))
                
                cursor.execute(f'''
                    INSERT INTO stars (path, filename, constellation, language, lock_tier, total_loc, coding_loc, file_impact, control_flow_ratio, author_distribution, popularity, {", ".join(self.RISK_SCHEMA)})
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, {", ".join(['?'] * len(self.RISK_SCHEMA))})
                ''', (
                    p, Path(p).name, c_name, star.get("lang_id"), star.get("lock_tier"), 
                    star.get("total_loc"), star.get("coding_loc"), star.get("file_impact"),
                    tel.get("control_flow_ratio"), tel.get("author_distribution"), pop_count,
                    *rv
                ))
                
                sid = cursor.lastrowid
                
                hv = star.get("hit_vector", [])
                dna_data = [(sid, self.SIGNAL_SCHEMA[i], hv[i]) for i in range(len(hv)) if hv[i] > 0]
                cursor.executemany('INSERT INTO dna_hits VALUES (?, ?, ?)', dna_data)
                
                for sat in star.get("satellites", []):
                    cursor.execute('INSERT INTO satellites (star_id, name, type_id, loc, impact) VALUES (?, ?, ?, ?, ?)', (
                        sid, sat.get("name"), sat.get("type_id"), sat.get("loc"), sat.get("impact")
                    ))

                # Inject Outbound Data
                raw_imports = star.get("raw_imports", [])
                if raw_imports:
                    out_data = [(sid, imp) for imp in raw_imports]
                    cursor.executemany('INSERT INTO outbound_dependencies VALUES (?, ?)', out_data)

                # Inject Inbound Data
                inbound = inbound_map.get(p, [])
                if inbound:
                    in_data = [(sid, imp_by) for imp_by in inbound]
                    cursor.executemany('INSERT INTO inbound_dependencies VALUES (?, ?)', in_data)

            conn.commit()
            conn.close()
        except Exception as e:
            self.logger.error(f"SQL Graph generation failed: {e}", exc_info=True)