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
from gitgalaxy.standards import analysis_lens as config

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

    def _parse_threat_score(self, star: Dict) -> tuple[float, str]:
        """Safely extracts and converts the AI threat score string to a float."""
        score_str = star.get("telemetry", {}).get("domain_context", {}).get("AI Threat Score", "0.0%")
        try:
            return float(score_str.replace('%', '')), score_str
        except ValueError:
            return 0.0, score_str

    def generate_artifacts(
        self, 
        parsed_files: List[Dict[str, Any]], 
        unparsable_files: List[Dict[str, Any]], 
        summary: Dict[str, Any], 
        session_meta: Dict[str, Any], 
        output_dir: str,
        forensic_report: Optional[Dict[str, Any]] = None
    ):
        """Generates the dual-output AI artifacts: Markdown and SQLite."""
        if forensic_report is None:
            forensic_report = {}
            
            
        target_name = session_meta.get("target", "unknown_project")
        safe_dir = Path(output_dir)
        
        # Use safe_dir instead of base_dir!
        output_path_md = safe_dir / f"{target_name}_galaxy_llm.md"
        output_path_db = safe_dir / f"{target_name}_galaxy_graph.sqlite"
        
        self.logger.info(f"Initiating LLM Artifact Generation for '{target_name}'...")
        
        # --- REVERSE DEPENDENCY RESOLUTION (Calculated once for both outputs) ---
        resolution_map = {}
        for s in parsed_files:
            path = s.get("path", "")
            name = s.get("name", Path(path).name)
            stem = Path(path).stem
            if path: resolution_map[path] = path
            if name: resolution_map[name] = path
            if stem: resolution_map[stem] = path

        inbound_map = {s.get("path", ""): [] for s in parsed_files}
        outbound_map = {s.get("path", ""): [] for s in parsed_files}
        
        for s in parsed_files:
            curr = s.get("path", "")
            for imp in s.get("raw_imports", []):
                if imp in resolution_map:
                    target_path = resolution_map[imp]
                    if target_path != curr:
                        if curr not in inbound_map[target_path]: inbound_map[target_path].append(curr)
                        if target_path not in outbound_map[curr]: outbound_map[curr].append(target_path)

        # 1. Build the Relational Knowledge Graph
        self._generate_sqlite_graph(parsed_files, unparsable_files, summary, session_meta, output_path_db, inbound_map)
        
        # 2. Build the Token-Optimized Markdown Brief
        md_content = self._build_markdown(parsed_files, unparsable_files, summary, session_meta, forensic_report, inbound_map, outbound_map)
        
        try:
            with open(output_path_md, "w", encoding="utf-8") as f:
                f.write(md_content)
            self.logger.info(f"AI Mission Complete:\n -> Markdown: {output_path_md}\n -> SQLite: {output_path_db}")
        except Exception as e:
            self.logger.error(f"Failed to seal LLM brief: {e}", exc_info=True)
    
    def _build_markdown(
        self, 
        parsed_files: List[Dict[str, Any]], 
        unparsable_files: List[Dict[str, Any]], 
        summary: Dict[str, Any], 
        session_meta: Dict[str, Any],
        forensic_report: Dict[str, Any],
        inbound_map: Dict[str, List[str]],
        outbound_map: Dict[str, List[str]]
    ) -> str:
        """Constructs a high-density, context-rich Markdown brief for LLM agents."""
        target = session_meta.get("target", "Project")
        sum_data = summary.get("summary", {})
        health = summary.get("health", {})
        comp = summary.get("composition", {})
        git_audit = session_meta.get("git_audit", {})
        
        bypassed_count = summary.get("unparsable_files", {}).get("ambig_file_count", 0)
        total_excluded = len(unparsable_files) + bypassed_count
        visible_count = sum_data.get("verified_files", len(parsed_files))
        
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
        lines.append(f"| **Zero-Dependency Mode** | `{'ACTIVE (Degraded Precision)' if session_meta.get('zero_dependency_mode') else 'Inactive (Full Precision)'}` |")
        lines.append("")
        
        if session_meta.get("zero_dependency_mode"):
            lines.append("> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**")
            lines.append("> External C-backed calculation engines (`networkx`, `tiktoken`) were not installed during this scan. Advanced metrics like Token Mass, Financial Read Cost, and N-Dimensional Network Topology (Blast Radius, Betweenness Centrality) are intentionally recorded as `null` or `0` to prevent data poisoning. Do not hallucinate values for these metrics.")
            lines.append("")
        
        # ---> NEW: HARVEST AI THREAT SCORES & CREATE BILLBOARD <---
        ml_threats = []
        for s in parsed_files:
            score_val, score_str = self._parse_threat_score(s)
            if s.get("is_ml_threat", False) or score_val >= 50.0:
                ml_threats.append((s, score_val, score_str))
                
        ml_threats.sort(key=lambda x: x[1], reverse=True)

        lines.append("## 0.5 AI THREAT AUDIT STATUS")
        if ml_threats:
            lines.append("> **🚨 AI_CONFIRMED_MALWARE_DETECTED**")
            lines.append(f"> XGBoost Structural DNA model identified {len(ml_threats)} malicious artifacts.")
        else:
            lines.append("> **✅ SECURE_NO_MALWARE_DETECTED**")
            lines.append("> XGBoost Structural DNA model found no malicious artifacts.")
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
        lines.append("> * **Defensive Guardrails:** `Error & Exception handling, `freeze_hits` (immutability), `cleanup` (state destruction).")
        
        # --- 2. 13-POINT RISK PHYSICS (THE EQUATIONS) ---
        lines.append("## 2. THE 13-POINT RISK EXPOSURE PHYSICS (EQUATIONS & CONTEXT)")
        lines.append("> **How the Physics Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**")
        lines.append("> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.")
        lines.append("> ")
        lines.append("> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`. High scores indicate a high density of decision-making, conditional branching, and complex state management packed into a small area.")
        lines.append("> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`. High scores mean risky operations (dynamic execution, type bypasses, unhandled mutations) exceed defensive guardrails (try/catch blocks, type checks, assertions). **Breach Cap:** If danger density is too high, the score is mathematically floored to a high-risk state regardless of defense. A value of near 30 is near minimum floor as gitgalaxy tests for testing file pairs, testing folders but not actually their contents.")
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
        lines.append("> **--- THE SECURITY & VULNERABILITY LENS ---**")
        lines.append("> 14. **Obfuscation & Evasion Risk (obscured_payload):** Measures the density of obfuscated logic, packed strings, and non-standard encoding. High scores indicate code that is structurally evading human readability or static analysis.")
        lines.append("> 15. **Destructive Execution Surface (logic_bomb):** Measures condition-heavy execution leading to destructive OS, memory, or process commands. High scores indicate a weaponizable surface where logic could easily be hijacked for sabotage.")
        lines.append("> 16. **Injection Surface Risk Exposure (injection_surface):** Measures external network/I/O input flowing directly into dynamic execution contexts without safety nets (XSS, SQLi, RCE).")
        lines.append("> 17. **Memory Corruption Risk Exposure (memory_corruption):** Measures the density of raw pointer math, manual memory allocations, and forceful casts without mitigations (Buffer Overflows, UAF). Primarily affects C/C++/Rust.")
        lines.append("> 18. **Secrets Risk Exposure (secrets_risk):** Measures the presence of hardcoded credentials (RHS assignments) exposed to logs, globals, or graveyard code. Any score > 0 is a critical alert.")
        lines.append("> ")
        lines.append("> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**")
        lines.append("> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. **This is NOT a risk score.** It measures the volume of decision-making, parameter coupling, and length. High impact means the function is a load-bearing 'Main Character' in the logic.")
        lines.append("> **20. File Magnitude (Total Mass):** Measures the total gravitational pull of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. **This is NOT a risk score.** A massive file simply means it is a heavily connected, structurally dense hub, whereas a lightweight file is a simple utility or config.")
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

        # --- 3.5 MACRO-NETWORK TOPOLOGY ---
        net_macro = summary.get("network_macro", {})
        if net_macro:
            lines.append("## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)")
            lines.append("| Metric | Value | Interpretation |")
            lines.append("|---|---|---|")
            lines.append(f"| Modularity | {net_macro.get('modularity', 0.0)} | High = Clean micro-boundaries. Low = Spaghetti coupling. |")
            lines.append(f"| Assortativity | {net_macro.get('assortativity', 0.0)} | Positive = Resilient core. Negative = Fragile single-points-of-failure. |")
            lines.append(f"| Cyclic Density | {net_macro.get('cyclic_density', 0.0)*100:.1f}% | % of files trapped in dependency loops (Static Friction). |")
            lines.append(f"| Avg Path Length | {net_macro.get('avg_path_length', 0.0)} | Hops between files. Lower = Tighter coupling. |")
            lines.append(f"| Articulation Pts | {net_macro.get('articulation_points', 0)} | Number of single files that, if removed, shatter the network. |")
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

        # --- 4.5 REPOSITORY MACRO-SPECIES (THE OVERARCHING PURPOSE) ---
        lines.append("## 4.5 REPOSITORY MACRO-SPECIES (GLOBAL ARCHITECTURE)")
        macro = summary.get("repo_macro_species", {})
        macro_name = macro.get('name', 'Unclassified')
        z_score = macro.get('z_score', 0.0)
        
        lines.append(f"> **Assigned Macro-Species:** `{macro_name}`")
        lines.append(f"> **Architectural Drift Z-Score:** `{z_score}`")
        
        if z_score > 2.0:
            lines.append("> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.")
        elif z_score < -1.0:
            lines.append("> **✅ STANDARD INTERPRETATION:** This repository has a negative Z-Score, meaning it is a textbook, highly standard interpretation of this archetype's structural patterns.")
        else:
            lines.append("> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.")
        lines.append("")

        lines.append("## 4.6 MICRO-SPECIES (FILE ARCHETYPES & STATIC MASS)")
        fingerprint = summary.get("ecosystem_fingerprint", {})
        ml_clusters = fingerprint.get("ml_clusters", {})
        static_mass = fingerprint.get("static_mass", {})
        
        if ml_clusters:
            lines.append("### Active Execution Logic (ML Clusters)")
            lines.append("| Archetype | Count | Repo % |")
            lines.append("|---|---|---|")
            for arch, data in ml_clusters.items():
                lines.append(f"| {arch} | {data['count']} | {data['pct']}% |")
            lines.append("")
            
        if static_mass:
            lines.append("### Inert Structural Mass (Static Categories)")
            lines.append("| Category | Count | Repo % |")
            lines.append("|---|---|---|")
            for arch, data in static_mass.items():
                lines.append(f"| {arch} | {data['count']} | {data['pct']}% |")
            lines.append("")

        # --- 4.7 AI & DATA TOPOLOGY ---
        ai_top = summary.get("ai_topology", {})
        if ai_top:
            lines.append("## 4.7 AI & MACHINE LEARNING TOPOLOGY")
            lines.append(f"> **Classification:** `{ai_top.get('classification', 'Unknown')}`")
            for insight in ai_top.get("insights", []):
                lines.append(f"> - {insight}")
            lines.append("")

        data_top = summary.get("data_topology", {})
        if data_top:
            lines.append("## 4.8 DATA TOPOLOGY & RELATIONAL GRAVITY")
            lines.append(f"> **Classification:** `{data_top.get('classification', 'Unknown')}`")
            for insight in data_top.get("insights", []):
                lines.append(f"> - {insight}")
            lines.append("")

        # --- 5. DARK MATTER ---
        lines.append("## 5. DARK MATTER (Non-scanned items ARTIFACTS)")
        lines.append(f"*Total Excluded Artifacts: {total_excluded}*\n")
        
        comp_breakdown = summary.get("unparsable_files", {}).get("composition_by_extension_and_reason", {})
        
        if comp_breakdown:
            lines.append("**Composition by Extension & Reason:**")
            for ext, reasons in list(comp_breakdown.items())[:15]:
                clean_reasons = []
                for rsn, count in list(reasons.items())[:3]:
                    safe_rsn = (rsn.replace("Unparsable", "Unrecognized Syntax")
                                   .replace("Structural Saturation", "Dense Structure")
                                   .replace("Necrosis", "Optical Bypass")
                                   .replace("Blocked", "Excluded"))
                    clean_reasons.append(f"{count}x {safe_rsn.strip()}")
                
                reason_str = ", ".join(clean_reasons)
                lines.append(f"- `{ext}`: {reason_str}")
        else:
            legacy_breakdown = summary.get("unparsable_files", {}).get("breakdown", {})
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
            # THE FIX: Explicitly banish Civil War from the LLM context
            if risk_slug == "civil_war":
                continue
                
            vals = [s.get("risk_vector", [])[i] for s in parsed_files if len(s.get("risk_vector", [])) > i]
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
            top_io = sorted(parsed_files, key=lambda x: x.get("hit_vector", [])[io_idx] if len(x.get("hit_vector", [])) > io_idx else 0, reverse=True)[:3]
            lines.append("### Top I/O Latency Risks")
            for s in top_io: 
                lines.append(f"- `{s.get('path')}` (Hits: {s.get('hit_vector', [])[io_idx]})")
            lines.append("")

        # 7.B: Structural Pillars (Imported By)
        pillars = sorted(parsed_files, key=lambda x: x.get("telemetry", {}).get("popularity", 0), reverse=True)[:5]
        lines.append("### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)")
        lines.append("These files act as core load-bearing infrastructure. Changes here carry a high risk of cascading breaks.\n")
        for rank, file_data in enumerate(pillars, 1):
            name = file_data.get("name", "Unknown")
            path = file_data.get("path", "Unknown")
            count = file_data.get("telemetry", {}).get("popularity", 0)
            lines.append(f"{rank}. **{name}** (`{path}`) — {count} inbound connections")
        lines.append("")

        # 7.C: Orchestrators (Imports)
        orchestrators = sorted(parsed_files, key=lambda x: len(x.get("raw_imports", [])) if isinstance(x.get("raw_imports"), list) else 0, reverse=True)[:5]
        lines.append("### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)")
        lines.append("These files pull in the most external dependencies. They are highly coupled and fragile to API changes.\n")
        for rank, file_data in enumerate(orchestrators, 1):
            name = file_data.get("name", "Unknown")
            path = file_data.get("path", "Unknown")
            count = len(file_data.get("raw_imports", [])) if isinstance(file_data.get("raw_imports"), list) else 0
            lines.append(f"{rank}. **{name}** (`{path}`) — {count} outbound dependencies")
        lines.append("")

        # --- 8. GOD FUNCTIONS (THE FUNCTIONS) ---
        lines.append("## 8. FUNCTION HITLIST (Heaviest Functions)")
        lines.append("> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*\n")
        
        # Flatten all functions to sort them globally
        all_sats = []
        for s in parsed_files:
            for sat in s.get("functions", []):
                sat_copy = sat.copy()
                sat_copy["file"] = s.get("path", "Unknown")
                all_sats.append(sat_copy)
                
        sorted_by_impact = sorted(all_sats, key=lambda x: x.get("impact", 0), reverse=True)
        if sorted_by_impact:
            for f in sorted_by_impact[:10]:
                lines.append(f"- `{f.get('name')}` (@ `{f.get('file')}`) -> Impact: **{f.get('impact')}** | LOC: {f.get('loc')}")
                doc = f.get('docstring', '').strip()
                if doc:
                    clean_doc = " ".join(doc.split())[:150] + ("..." if len(doc) > 150 else "")
                    lines.append(f"  * *Intent:* {clean_doc}")
        else:
            lines.append("*No complex satellites detected.*")
        lines.append("")

        # --- 8.5 ALGORITHMIC & DATABASE BOTTLENECKS ---
        lines.append("## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS")
        lines.append("> Highlights the most computationally expensive and database-heavy functions across the repository.\n")
        
        # Sort by recursion first, then big-o depth
        sorted_by_big_o = sorted(all_sats, key=lambda x: (x.get("is_recursive", False), x.get("big_o_depth", 1)), reverse=True)
        complex_sats = [s for s in sorted_by_big_o if s.get("is_recursive", False) or s.get("big_o_depth", 1) > 2]
        
        if complex_sats:
            lines.append("### Highest Time Complexity (Big-O)")
            for f in complex_sats[:10]:
                o_str = "O(2^N) [Recursive]" if f.get("is_recursive", False) else f"O(N^{f.get('big_o_depth', 1)})"
                lines.append(f"- `{f.get('name')}` (@ `{f.get('file')}`) -> **{o_str}**")
                doc = f.get('docstring', '').strip()
                if doc:
                    clean_doc = " ".join(doc.split())[:150] + ("..." if len(doc) > 150 else "")
                    lines.append(f"  * *Intent:* {clean_doc}")
            lines.append("")
            
        sorted_by_db = sorted(all_sats, key=lambda x: x.get("db_complexity", 0), reverse=True)
        db_sats = [s for s in sorted_by_db if s.get("db_complexity", 0) > 0]
        
        if db_sats:
            lines.append("### Highest Data Gravity (Database Complexity)")
            for f in db_sats[:10]:
                lines.append(f"- `{f.get('name')}` (@ `{f.get('file')}`) -> DB Complexity: **{f.get('db_complexity', 0)}**")
                doc = f.get('docstring', '').strip()
                if doc:
                    clean_doc = " ".join(doc.split())[:150] + ("..." if len(doc) > 150 else "")
                    lines.append(f"  * *Intent:* {clean_doc}")
            lines.append("")

        # --- 9. DIRECTORY GROUPS ---
        lines.append("## 9. DIRECTORY GROUPS (Top 10 Heaviest Folders)")
        constellations = summary.get("directory_groups", {})
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
            high_debt = sorted([s for s in parsed_files if len(s.get("risk_vector", [])) > debt_idx], key=lambda x: x.get("risk_vector")[debt_idx], reverse=True)[:5]
            if high_debt and high_debt[0].get("risk_vector")[debt_idx] > 0:
                lines.append("### Highest Tech Debt (Fragile/Planned)")
                for s in high_debt:
                    if s.get("risk_vector")[debt_idx] > 0:
                        lines.append(f"- `{s.get('path')}` -> **{s.get('risk_vector')[debt_idx]}%** Exposure")
                        
        # State Flux (Volatility) Hitlist
        flux_idx = self.RISK_SCHEMA.index("state_flux") if "state_flux" in self.RISK_SCHEMA else -1
        if flux_idx >= 0:
            high_flux = sorted([s for s in parsed_files if len(s.get("risk_vector", [])) > flux_idx], key=lambda x: x.get("risk_vector")[flux_idx], reverse=True)[:5]
            if high_flux and high_flux[0].get("risk_vector")[flux_idx] > 0:
                lines.append("### Highest State Flux (Mutation/Volatility)")
                for s in high_flux:
                    if s.get("risk_vector")[flux_idx] > 0:
                        lines.append(f"- `{s.get('path')}` -> **{s.get('risk_vector')[flux_idx]}%** Exposure")
                        
        # Design Slop (Orphans & Duplicates) Hitlist
        orphan_idx = self.SIGNAL_SCHEMA.index("design_slop_orphans") if "design_slop_orphans" in self.SIGNAL_SCHEMA else -1
        dup_idx = self.SIGNAL_SCHEMA.index("design_slop_duplicates") if "design_slop_duplicates" in self.SIGNAL_SCHEMA else -1
        
        if orphan_idx >= 0 and dup_idx >= 0:
            # Sort by total slop (orphans + duplicates)
            high_slop = sorted(
                [s for s in parsed_files if len(s.get("hit_vector", [])) > max(orphan_idx, dup_idx)], 
                key=lambda x: x.get("hit_vector")[orphan_idx] + x.get("hit_vector")[dup_idx], 
                reverse=True
            )[:5]
            
            if high_slop and (high_slop[0].get("hit_vector")[orphan_idx] + high_slop[0].get("hit_vector")[dup_idx]) > 0:
                lines.append("### Highest Design Slop (Dead & Duplicated Logic)")
                for s in high_slop:
                    o_hits = s.get("hit_vector")[orphan_idx]
                    d_hits = s.get("hit_vector")[dup_idx]
                    if o_hits > 0 or d_hits > 0:
                        lines.append(f"- `{s.get('path')}` -> **{o_hits}** Orphaned Functions | **{d_hits}** Duplicates")
        lines.append("")

        # --- 10.5 AI THREAT INTELLIGENCE ---
        lines.append("## 10.5 AI THREAT INTELLIGENCE (XGBoost)")
        if ml_threats:
            lines.append("> **CRITICAL THREATS DETECTED.** The following files possess the structural DNA of known malware.\n")
            # Show top 10% of threats, or at least the top 10
            cutoff = max(10, int(len(ml_threats) * 0.10))
            for i, (s, val, string_val) in enumerate(ml_threats[:cutoff]):
                lines.append(f"{i+1}. **`{s.get('path')}`** -> AI Confidence: **{string_val}**")
        else:
            lines.append("*No files met the threshold for malicious structural DNA.*")
        lines.append("")

        # --- 10.6 CRITICAL VULNERABILITY EXPOSURES (RULE-BASED) ---
        lines.append("## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED LENS)")
        lines.append("> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.\n")
        
        vuln_keys = ["obscured_payload", "logic_bomb", "injection_surface", "memory_corruption", "secrets_risk"]
        vuln_found = False
        for v_key in vuln_keys:
            if v_key in self.RISK_SCHEMA:
                v_idx = self.RISK_SCHEMA.index(v_key)
                v_files = sorted([s for s in parsed_files if len(s.get("risk_vector", [])) > v_idx and s.get("risk_vector")[v_idx] > 0.0], key=lambda x: x.get("risk_vector")[v_idx], reverse=True)
                
                if v_files:
                    vuln_found = True
                    label = exposure_labels.get(v_key, v_key.replace('_', ' ').title())
                    lines.append(f"### {label}")
                    for s in v_files[:5]:
                        lines.append(f"- `{s.get('path')}` -> **{s.get('risk_vector')[v_idx]}%** Exposure")
        
        if not vuln_found:
            lines.append("*No critical vulnerabilities or security lens thresholds breached.*")
        lines.append("")
        
        # --- 10.7 AUTONOMOUS AI VULNERABILITIES ---
        lines.append("## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)")
        lines.append("> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).\n")
        
        pi_idx = self.SIGNAL_SCHEMA.index("prompt_injection") if "prompt_injection" in self.SIGNAL_SCHEMA else -1
        rce_idx = self.SIGNAL_SCHEMA.index("agentic_rce") if "agentic_rce" in self.SIGNAL_SCHEMA else -1
        
        ai_vuln_found = False
        
        if rce_idx >= 0:
            rce_files = sorted([s for s in parsed_files if len(s.get("hit_vector", [])) > rce_idx and s.get("hit_vector")[rce_idx] > 0], key=lambda x: x.get("hit_vector")[rce_idx], reverse=True)
            if rce_files:
                ai_vuln_found = True
                lines.append("### 🚨 Agentic RCE (Critical)")
                lines.append("The following files pass autonomous LLM output directly into system execution commands. This allows the AI to run arbitrary code on the host machine.\n")
                for s in rce_files[:5]:
                    lines.append(f"- `{s.get('path')}` -> **{s.get('hit_vector')[rce_idx]}** confirmed execution vectors")
                lines.append("")
                
        if pi_idx >= 0:
            pi_files = sorted([s for s in parsed_files if len(s.get("hit_vector", [])) > pi_idx and s.get("hit_vector")[pi_idx] > 0], key=lambda x: x.get("hit_vector")[pi_idx], reverse=True)
            if pi_files:
                ai_vuln_found = True
                lines.append("### 💉 Prompt Injection Surface")
                lines.append("The following files pass raw, untrusted external I/O directly into an LLM context window without sanitization.\n")
                for s in pi_files[:5]:
                    lines.append(f"- `{s.get('path')}` -> **{s.get('hit_vector')[pi_idx]}** exposed injection surfaces")
                lines.append("")
                
        if not ai_vuln_found:
            lines.append("*No autonomous AI vulnerabilities detected.*")
        lines.append("")

        # ==============================================================================
        # --- 11. CUMULATIVE RISK HITLIST (NEW) ---
        # ==============================================================================
        lines.append("## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)")
        lines.append("> Cumulative Risk is the sum of all individual risk exposures (excluding Civil War). These files represent the highest multi-dimensional technical debt and architectural fragility.\n")
        
        cumulative_risks = forensic_report.get("cumulative_risk", {}).get("highest", [])
        if cumulative_risks:
            # Create a fast-lookup map to pull detailed file stats by path
            file_map = {f.get("path"): f for f in parsed_files}
            
            for rank, cr in enumerate(cumulative_risks[:10], 1):
                p = cr.get("path")
                c_val = cr.get("value")
                s = file_map.get(p)
                
                # Fallback if the star object is somehow missing
                if not s:
                    lines.append(f"### {rank}. `{p}` -> Cumulative Risk: **{c_val}**")
                    continue
                
                l = s.get("lang_id", "UNK").upper()
                m = s.get("file_impact", 0.0)
                loc = s.get("total_loc", 0)
                tel = s.get("telemetry", {})
                rv = s.get("risk_vector", [])
                
                lines.append(f"### {rank}. `{p}` ({l}) -> Cumulative Risk: **{c_val}**")
                arch = tel.get('archetype', 'Unknown Archetype')
                dist = tel.get('archetype_fingerprint', {}).get(arch, 'N/A')
                lines.append(f"- **Archetype:** `{arch}` (Distance: {dist} IQR)")
                lines.append(f"- **Mass:** {m} | **LOC:** {loc} | **CtrlFlow:** {round(tel.get('control_flow_ratio', 0.0) * 100, 1)}% | **Silo Risk:** {round(tel.get('author_distribution', 0.0), 1)}%")
                            
                # Dynamically calculate the top 4 risk drivers pushing this file's score up
                file_risks = []
                for i, r_val in enumerate(rv):
                    if i < len(self.RISK_SCHEMA) and self.RISK_SCHEMA[i] != "civil_war" and r_val > 0:
                        file_risks.append((self.RISK_SCHEMA[i], r_val))
                
                file_risks.sort(key=lambda x: x[1], reverse=True)
                top_file_risks = [f"{k.replace('_', ' ').title()} ({r_val}%)" for k, r_val in file_risks[:4]]
                lines.append(f"- **Primary Risk Drivers:** {', '.join(top_file_risks) if top_file_risks else 'None'}")
                
                # Fetch the top 3 heaviest functions in this specific file
                sats = sorted(s.get("functions", []), key=lambda x: x.get("impact", 0), reverse=True)[:3]
                if sats:
                    sat_strs = [f"`{sat.get('name')}` (Impact: {sat.get('impact')})" for sat in sats]
                    lines.append(f"- **Heaviest Functions:** {', '.join(sat_strs)}")
                    
                lines.append("")
        else:
            lines.append("*No cumulative risk data available.*")
            lines.append("")

        # ==============================================================================
        # --- 12. VISIBLE MATTER HITLIST (Top 25 Heaviest Files) ---
        # ==============================================================================
        lines.append("## 12. VISIBLE MATTER HITLIST (Top 25 Heaviest Files)")
        lines.append("> *Note: 'Mass' represents the file's total Structural Magnitude and gravitational pull within the system. It is independent of its Risk Profile. High mass implies high structural importance and centralization.*\n")

        sorted_files = sorted(parsed_files, key=lambda x: x.get("file_impact", 0.0), reverse=True)[:25]
        
        # DNA Bucketing Sets
        structure_keys = {"branch", "linear", "args", "func_start", "class_start"}
        risk_keys = {"danger", "flux", "graveyard", "safety_neg", "planned_debt", "fragile_debt", "design_slop_orphans", "design_slop_duplicates"}
        arch_keys = {"io", "concurrency", "api", "import"}
        defense_keys = {"safety", "freeze_hits", "cleanup", "test", "sync_locks", "doc"}
        
        for s in sorted_files:
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
            
            # ---> NEW: INJECT AI SCORE INTO FILE HEADER <---
            ai_score_val, ai_score_str = self._parse_threat_score(s)
            threat_flag = f" | 🚨 AI THREAT: {ai_score_str}" if ai_score_val >= 50.0 else f" | AI Safe: {ai_score_str}"
            
            lines.append(f"### `{p}` ({l} | Tier {lock_tier}{threat_flag})")
            if purpose:
                lines.append(f"> **Stated Purpose:** *{purpose}*")
                
            arch = tel.get('archetype', 'Unknown Archetype')
            g_drift = tel.get('global_drift', 'N/A')
            l_arch = tel.get('local_archetype')
            l_drift = tel.get('local_drift', 'N/A')
            
            lines.append(f"- **Global Archetype:** `{arch}` (Drift: {g_drift} IQR)")
            if l_arch and l_arch != "N/A":
                lines.append(f"- **Local Micro-Species:** `{l_arch}` (Drift: {l_drift} IQR)")
                
            fingerprint = tel.get('archetype_fingerprint', {})
            if fingerprint:
                fp_strs = [f"{k.split(':')[0]}: {v}" for k, v in sorted(fingerprint.items(), key=lambda x: x[1])[:3]]
                lines.append(f"- **Top Global Matches:** {', '.join(fp_strs)}")
                
            lines.append(f"- **Mass:** {m} | **LOC:** {loc} | **CtrlFlow:** {round(tel.get('control_flow_ratio', 0.0) * 100, 1)}% | **Silo Risk:** {round(tel.get('author_distribution', 0.0), 1)}%")
            lines.append(f"- **Algorithmic:** {tel.get('max_algorithmic_complexity', 'O(N)')} | **DB Complexity:** {tel.get('max_db_complexity', 0)}")
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
            sats = sorted(s.get("functions", []), key=lambda x: x.get("impact", 0), reverse=True)[:5]
            if sats:
                lines.append("**Top Internal Functions/Classes:**")
                for sat in sats:
                    o_str = "O(2^N)" if sat.get("is_recursive", False) else f"O(N^{sat.get('big_o_depth', 1)})"
                    db_str = f" | DB: {sat.get('db_complexity', 0)}" if sat.get("db_complexity", 0) > 0 else ""
                    lines.append(f"  * `{sat.get('name')}` (Impact: {sat.get('impact')} | {o_str}{db_str})")
                    doc = sat.get('docstring', '').strip()
                    if doc:
                        clean_doc = " ".join(doc.split())[:100] + ("..." if len(doc) > 100 else "")
                        lines.append(f"    * *Intent:* {clean_doc}")
            
            # --- NEW MITIGATION TELEMETRY BLOCK ---
            mitigations = tel.get("mitigation_telemetry", {})
            active_mitigations = {k: v for k, v in mitigations.items() if v > 0}
            if active_mitigations:
                lines.append("**Contextual Mitigations & Amplifications:**")
                for m_key, m_val in active_mitigations.items():
                    clean_key = m_key.replace('_', ' ').title()
                    lines.append(f"* *{clean_key}:* {m_val} instances")

            # --- UPDATED STRING LABEL ---
            lines.append("**Structural DNA (Net Mitigated Signals):**")
            lines.append(f"* *Structure:* {', '.join(struct_hits) if struct_hits else 'None'}")
            lines.append(f"* *Risk/State:* {', '.join(risk_hits) if risk_hits else 'None'}")
            lines.append(f"* *Architecture:* {', '.join(arch_hits) if arch_hits else 'None'}")
            lines.append(f"* *Defense:* {', '.join(def_hits) if def_hits else 'None'}")
            
            # Dependency Graph Mapping (Named Edges)
            outbound = s.get("raw_imports", [])
            net_mets = tel.get("network_metrics", {})
            in_d = net_mets.get("in_degree", 0)
            out_d = net_mets.get("out_degree", 0)
            blast_rad = net_mets.get("normalized_blast_radius", 0.0)
            between_score = net_mets.get("betweenness_score", 0.0)
            close_score = net_mets.get("closeness_score", 0.0)
            eco_role = net_mets.get("ecosystem_role", "Unknown")
            
            out_names = ", ".join([Path(x).name for x in outbound[:8]]) + ("..." if len(outbound) > 8 else "")
            
            lines.append(f"* *Network Topology:*")
            lines.append(f"  * `Ecosystem Role:` {eco_role} | `Blast Radius (PageRank):` {blast_rad}")
            lines.append(f"  * `Choke Point (Betweenness):` {between_score} | `Ripple Effect (Closeness):` {close_score}")
            lines.append(f"  * `Imports (Out-Degree: {out_d}):` {out_names if out_names else 'None'}")
            lines.append(f"  * `Imported By (In-Degree: {in_d}):` {'(Excluded from Brief to save tokens)' if in_d > 0 else 'None (Orphan / Entrypoint)'}")
            lines.append("")
        
        # ==============================================================================
        # --- 13. BIAXIAL ANOMALY & ARCHITECTURAL DRIFT ---
        # ==============================================================================
        lines.append("## 13. BIAXIAL ANOMALY & ARCHITECTURAL DRIFT")
        lines.append("> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.\n")
        
        drifting_files = []
        trojan_files = []
        
        for s in parsed_files:
            tel = s.get("telemetry", {})
            
            # 1. Biaxial Trojan Check
            g_drift = tel.get("global_drift", 0.0)
            l_drift = tel.get("local_drift", 0.0)
            
            if g_drift > 0 and l_drift > 0:
                biaxial_ratio = l_drift / g_drift
                if biaxial_ratio > 1.5:
                    trojan_files.append({
                        "file_data": s, "ratio": biaxial_ratio, "g_drift": g_drift, "l_drift": l_drift,
                        "g_arch": tel.get("archetype"), "l_arch": tel.get("local_archetype")
                    })
            
            # 2. Chimeric Global Drift Check
            fingerprint = tel.get("archetype_fingerprint", {})
            if len(fingerprint) >= 2:
                sorted_archs = sorted(fingerprint.items(), key=lambda x: x[1])
                primary_arch, primary_dist = sorted_archs[0]
                secondary_arch, secondary_dist = sorted_archs[1]
                delta = secondary_dist - primary_dist
                
                if delta <= 0.9:
                    drifting_files.append({
                        "file_data": s, "delta": delta,
                        "primary": (primary_arch, primary_dist),
                        "secondary": (secondary_arch, secondary_dist)
                    })
        
        if trojan_files:
            lines.append("### 🚨 Biaxial Anomalies (Severe Anti-Patterns / Language Violations)")
            trojan_files.sort(key=lambda x: x["ratio"], reverse=True)
            for t in trojan_files[:5]:
                s = t["file_data"]
                lines.append(f"- `{s.get('path')}` ({s.get('lang_id', 'UNK').upper()}) | **Biaxial Ratio: {round(t['ratio'], 2)}x**")
                lines.append(f"  * **Global Archetype:** `{t['g_arch']}` (Drift: {t['g_drift']} IQR)")
                lines.append(f"  * **Local Reality:** `{t['l_arch']}` (Drift: {t['l_drift']} IQR)")
            lines.append("")
                    
        if drifting_files:
            from collections import defaultdict
            drift_by_cluster = defaultdict(list)
            
            for drift in drifting_files:
                drift_by_cluster[drift["primary"][0]].append(drift)
                
            for cluster_name, files in sorted(drift_by_cluster.items()):
                lines.append(f"### Refactoring Targets for: {cluster_name}")
                files.sort(key=lambda x: x["delta"])
                
                for drift in files[:5]:
                    s = drift["file_data"]
                    p = s.get("path", "UNK")
                    l = s.get("lang_id", "UNK").upper()
                    m = s.get("file_impact", 0.0)
                    sec_a, sec_d = drift["secondary"]
                    
                    lines.append(f"- `{p}` ({l}) | Mass: {m} | Delta: **{round(drift['delta'], 3)} IQR** | Secondary Pull: `{sec_a}`")
                    
                    struct_hits = [(self.SIGNAL_SCHEMA[i], val) for i, val in enumerate(s.get("hit_vector", [])) if val > 0 and i < len(self.SIGNAL_SCHEMA)]
                    struct_hits.sort(key=lambda x: x[1], reverse=True)
                    top_hits = ", ".join([f"{k}: {v}" for k, v in struct_hits[:4]])
                    
                    lines.append(f"  * Top DNA Signatures: {top_hits if top_hits else 'None'}")
                lines.append("")
        else:
            lines.append("*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*")
            lines.append("")
        
        # ==============================================================================
        # --- 13.5 ARCHITECTURAL CHOKE POINTS (The AI Action Matrix) ---
        # ==============================================================================
        lines.append("## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Silos)")
        lines.append("> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high silo risk (single points of failure).\n")
        
        # 1. The Hotspot Matrix (High Risk + High Churn)
        churn_idx = self.RISK_SCHEMA.index("churn") if "churn" in self.RISK_SCHEMA else -1
        if churn_idx >= 0:
            # Find files with > 50% Churn AND > 50% Cognitive Load or Tech Debt
            cog_idx = self.RISK_SCHEMA.index("cognitive_load")
            debt_idx = self.RISK_SCHEMA.index("tech_debt")
            
            hotspots = []
            for s in parsed_files:
                rv = s.get("risk_vector", [])
                if len(rv) > max(churn_idx, cog_idx, debt_idx):
                    if rv[churn_idx] > 50.0 and (rv[cog_idx] > 50.0 or rv[debt_idx] > 50.0):
                        hotspots.append(s)
                        
            if hotspots:
                lines.append("### 🔥 The Hotspot Matrix (High Volatility + High Risk)")
                lines.append("These files are messy, complex, and modified frequently. They are the primary source of developer friction.\n")
                hotspots.sort(key=lambda x: x.get("risk_vector")[churn_idx], reverse=True)
                for s in hotspots[:5]:
                    rv = s.get("risk_vector")
                    lines.append(f"- `{s.get('path')}` -> Churn: **{rv[churn_idx]}%** | Cog Load: {rv[cog_idx]}% | Debt: {rv[debt_idx]}%")
                lines.append("")

        # 2. Key Person Dependencies (High Impact + High Silo)
        siloed_pillars = [
            s for s in parsed_files 
            if s.get("telemetry", {}).get("author_distribution", 0.0) > 80.0 
            and s.get("file_impact", 0.0) > 50.0
        ]
        
        if siloed_pillars:
            lines.append("### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)")
            lines.append("These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.\n")
            siloed_pillars.sort(key=lambda x: x.get("file_impact", 0.0), reverse=True)
            for s in siloed_pillars[:5]:
                owner = s.get("telemetry", {}).get("ownership", "Unknown")
                silo_score = s.get("telemetry", {}).get("author_distribution", 0.0)
                lines.append(f"- `{s.get('path')}` -> **{owner}** ({silo_score}% isolated ownership) | Mass: {s.get('file_impact')}")
            lines.append("")

        # ==============================================================================
        # --- 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Physics) ---
        # ==============================================================================
        sys_bots = forensic_report.get("systemic_bottlenecks", {})
        if any(v and v[0]["score"] > 0 for v in sys_bots.values()):
            lines.append("## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Physics)")
            lines.append("> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.\n")
            
            # Contagious Mutation
            cm = sys_bots.get("contagious_mutation", [])
            if cm and cm[0]["score"] > 0:
                lines.append("### ☣️ Contagious Mutation (Betweenness * State Flux)")
                lines.append("These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.\n")
                for c in cm:
                    if c["score"] > 0:
                        lines.append(f"- `{c['path']}` -> **Severity: {c['score']}** (Bridge: {c['btw']} * Flux: {c['flux']}%)")
                lines.append("")

            # House of Cards
            hoc = sys_bots.get("house_of_cards", [])
            if hoc and hoc[0]["score"] > 0:
                lines.append("### 🃏 House of Cards (Closeness * Error Risk)")
                lines.append("These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.\n")
                for h in hoc:
                    if h["score"] > 0:
                        lines.append(f"- `{h['path']}` -> **Severity: {h['score']}** (Embedded: {h['close']} * Error Risk: {h['err']}%)")
                lines.append("")

            # Blind Bottleneck
            bb = sys_bots.get("blind_bottleneck", [])
            if bb and bb[0]["score"] > 0:
                lines.append("### 🙈 Blind Bottlenecks (Blast Radius * Doc Risk)")
                lines.append("These are 'God Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.\n")
                for b in bb:
                    if b["score"] > 0:
                        lines.append(f"- `{b['path']}` -> **Severity: {b['score']}** (Blast Radius: {b['pr']} * Doc Risk: {b['doc']}%)")
                lines.append("")

        # ==============================================================================
        # --- 14. SYSTEM PROMPT: HOW TO RESPOND ---
        # ==============================================================================
        lines.append("## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)")
        lines.append("> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.")
        lines.append("> **When the user asks for an architectural review, structure your response using these directives:**")
        lines.append("> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.")
        lines.append("> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).")
        lines.append("> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.")
        lines.append("> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or constellations with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.")
        lines.append("> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive 'God Nodes', or mitigate extreme risk exposures to stabilize the system's architecture.")
        lines.append("")
            
        return "\n".join(lines)
                
    def _generate_sqlite_graph(
        self, 
        parsed_files: List[Dict[str, Any]], 
        unparsable_files: List[Dict[str, Any]], 
        summary: Dict[str, Any], 
        session: Dict[str, Any], 
        db_path: Path,
        inbound_map: Dict[str, List[str]]
    ):
        """Creates a relational database for advanced SQL-based AI analysis and DNA Fingerprinting."""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute('DROP TABLE IF EXISTS meta')
            cursor.execute('CREATE TABLE meta (key TEXT, value TEXT)')
            
            macro_info = summary.get("repo_macro_species", {})
            net_macro = summary.get("network_macro", {})
            cursor.executemany('INSERT INTO meta VALUES (?, ?)', [
                ("engine", session.get("engine")),
                ("project", session.get("target")),
                ("timestamp", session.get("timestamp")),
                ("branch", session.get("git_audit", {}).get("branch")),
                ("commit", session.get("git_audit", {}).get("commit_hash")),
                ("zero_dependency_mode", "True" if session.get("zero_dependency_mode") else "False"),
                ("repo_macro_species", macro_info.get("name", "Unclassified")),
                ("repo_z_score", str(macro_info.get("z_score", 0.0))),
                ("network_modularity", str(net_macro.get("modularity", 0.0))),
                ("network_assortativity", str(net_macro.get("assortativity", 0.0))),
                ("network_cyclic_density", str(net_macro.get("cyclic_density", 0.0))),
                ("network_avg_path_length", str(net_macro.get("avg_path_length", 0.0))),
                ("network_articulation_points", str(net_macro.get("articulation_points", 0)))
            ])

            cursor.execute('DROP TABLE IF EXISTS stars')
            risk_cols = ", ".join([f"{r} REAL" for r in self.RISK_SCHEMA])
            cursor.execute(f'''
                CREATE TABLE stars (
                    id INTEGER PRIMARY KEY,
                    path TEXT,
                    filename TEXT,
                    parent_entity TEXT,
                    constellation TEXT,
                    language TEXT,
                    lock_tier INTEGER,
                    total_loc INTEGER,
                    coding_loc INTEGER,
                    doc_loc INTEGER,
                    file_impact REAL,
                    control_flow_ratio REAL,
                    author_distribution REAL,
                    ownership_entropy REAL,
                    raw_churn_freq REAL,
                    cog_raw REAL,
                    ownership TEXT,
                    popularity INTEGER,
                    archetype TEXT,
                    global_drift REAL,
                    local_archetype TEXT,
                    local_drift REAL,
                    repo_macro_species TEXT,
                    repo_z_score REAL,
                    max_algorithmic_complexity TEXT,
                    max_db_complexity INTEGER,
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
                    avg_error_score REAL,
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
                    big_o_depth INTEGER,
                    is_recursive BOOLEAN,
                    db_complexity INTEGER,
                    docstring TEXT,
                    calls_out_to TEXT,
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

            const_meta = summary.get("directory_groups", {})

            for c_name, c_data in const_meta.items():
                exps = c_data.get("avg_exposures", {})
                cursor.execute('''
                    INSERT INTO constellations (name, file_count, total_mass, avg_cognitive_load, avg_error_score, avg_tech_debt, avg_verification)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    c_name, 
                    c_data.get("file_count", 0), 
                    c_data.get("total_mass", 0.0),
                    exps.get("cognitive_load", 0.0), 
                    exps.get("safety_score", 0.0), # Keep this as "safety_score" unless you've also renamed the internal dictionary keys upstream
                    exps.get("tech_debt", 0.0),
                    exps.get("verification", 0.0)
                ))

            for file_data in parsed_files:
                p = file_data.get("path")
                c_name = file_data.get("directory_group", "__monolith__")
                tel = file_data.get("telemetry", {})
                
                rv = file_data.get("risk_vector", [0.0] * len(self.RISK_SCHEMA))
                pop_count = len(inbound_map.get(p, []))
                
                # Extract repo-level metadata (can be injected via ML pass)
                repo_macro = tel.get("repo_macro_species", "Unknown")
                repo_z = tel.get("repo_z_score", 0.0)
                
                # --- INJECT ALL RAW DNA METRICS ---
                parent_entity = tel.get("domain_context", {}).get("parent_entity", "")
                
                cursor.execute(f'''
                    INSERT INTO stars (
                        path, filename, parent_entity, constellation, language, lock_tier, 
                        total_loc, coding_loc, doc_loc, file_impact,
                        control_flow_ratio, author_distribution, ownership_entropy,
                        raw_churn_freq, cog_raw, ownership, popularity, 
                        archetype, global_drift, local_archetype, local_drift,
                        repo_macro_species, repo_z_score, max_algorithmic_complexity, max_db_complexity,
                        {", ".join(self.RISK_SCHEMA)}
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, {", ".join(['?'] * len(self.RISK_SCHEMA))})
                ''', (
                    p, Path(p).name, parent_entity, c_name, file_data.get("lang_id"), file_data.get("lock_tier"), 
                    file_data.get("total_loc"), file_data.get("coding_loc"), file_data.get("doc_loc", 0), file_data.get("file_impact"),
                    tel.get("control_flow_ratio"), tel.get("author_distribution"), tel.get("ownership_entropy"),
                    tel.get("raw_churn_freq"), tel.get("densities", {}).get("cog_raw"), tel.get("ownership"), pop_count, 
                    tel.get("archetype", "Unknown"), tel.get("global_drift", 0.0), tel.get("local_archetype", "N/A"), tel.get("local_drift", 0.0),
                    str(repo_macro), repo_z, tel.get("max_algorithmic_complexity", "O(N)"), tel.get("max_db_complexity", 0),
                    *rv
                ))
                
                sid = cursor.lastrowid
                
                # Dynamic Hit Insertion (Automatically includes all sec_ signatures)
                hv = file_data.get("hit_vector", [])
                dna_data = [(sid, self.SIGNAL_SCHEMA[i], hv[i]) for i in range(len(hv)) if hv[i] > 0]
                cursor.executemany('INSERT INTO dna_hits VALUES (?, ?, ?)', dna_data)
                
                import json
                for func in file_data.get("functions", []):
                    calls_json = json.dumps(func.get("calls_out_to", []))
                    cursor.execute('INSERT INTO satellites (star_id, name, type_id, loc, impact, big_o_depth, is_recursive, db_complexity, docstring, calls_out_to) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
                        sid, func.get("name"), func.get("type_id"), func.get("loc"), func.get("impact"),
                        func.get("big_o_depth", 1), func.get("is_recursive", False), func.get("db_complexity", 0), func.get("docstring", ""), calls_json
                    ))

                raw_imports = file_data.get("raw_imports", [])

                raw_imports = file_data.get("raw_imports", [])
                if raw_imports:
                    out_data = [(sid, imp) for imp in raw_imports]
                    cursor.executemany('INSERT INTO outbound_dependencies VALUES (?, ?)', out_data)

                inbound = inbound_map.get(p, [])
                if inbound:
                    in_data = [(sid, imp_by) for imp_by in inbound]
                    cursor.executemany('INSERT INTO inbound_dependencies VALUES (?, ?)', in_data)

            conn.commit()
            conn.close()
        except Exception as e:
            self.logger.error(f"SQL Graph generation failed: {e}", exc_info=True)