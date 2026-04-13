# ==============================================================================
# GitGalaxy
# Copyright (c) 2026 Joe Esquibel
# ==============================================================================
import sqlite3
import json
import logging
import statistics
import math
from pathlib import Path
from typing import List, Dict, Any, Optional
from . import analysis_lens
from .analysis_lens import RECORDING_SCHEMAS

class RecordKeeper:
    """
    The GitGalaxy Record Keeper (Native SQLite Recorder).
    
    PURPOSE: Transforms the live RAM state directly into a highly relational 
    SQLite database. Bypasses the need for intermediate JSON parsing and creates 
    a time-series schema perfectly aligned for Master Database aggregation.
    """

    def __init__(self, parent_logger: Optional[logging.Logger] = None):
        self.logger = parent_logger.getChild("record_keeper") if parent_logger else logging.getLogger("record_keeper")
        
        schemas = RECORDING_SCHEMAS
        self.RISK_SCHEMA = schemas.get("RISK_SCHEMA", [])
        self.SIGNAL_SCHEMA = schemas.get("SIGNAL_SCHEMA", [])

        # The 5-Pillar Taxonomy Map (Enforces schema consistency)
        self.SHORT_KEY_MAP = {
            "branch": "struct_branch", "linear": "struct_linear", "args": "struct_args", "func_start": "struct_func_start", "class_start": "struct_class_start", "closures": "struct_closures", "comprehensions": "struct_comprehensions", "macros": "struct_macros", "decorators": "struct_decorators", "generics": "struct_generics", "core_var_decl": "struct_var_decl", "indent_tabs": "struct_tabs", "indent_spaces": "struct_spaces", "design_camel_case": "struct_camel_case", "design_snake_case": "struct_snake_case", "design_pascal_case": "struct_pascal_case", "design_upper_case": "struct_upper_case", "design_short_vars": "struct_short_vars", "design_long_vars": "struct_long_vars", "flux": "state_flux", "danger": "state_danger", "graveyard": "state_graveyard", "safety_neg": "state_safety_neg", "design_slop_orphans": "state_slop_orphans", "design_slop_duplicates": "state_slop_duplicates", "planned_debt": "state_planned_debt", "fragile_debt": "state_fragile_debt", "bailout_hits": "state_bailout_hits", "halt_hits": "state_halt_hits", "heat_triggers": "state_heat_triggers", "pointers": "state_pointers", "memory_alloc": "state_memory_alloc", "cast_hits": "state_cast_hits", "print_hits": "state_print_hits", "io": "arch_io", "api": "arch_api", "concurrency": "arch_concurrency", "import": "arch_import", "ui_framework": "arch_ui_framework", "globals": "arch_globals", "ipc_rpc_bridges": "arch_ipc", "ssr_boundaries": "arch_ssr_boundaries", "events": "arch_events", "scientific": "arch_scientific", "dependency_injection": "arch_dependency_injection", "hardware_bridge": "arch_hardware", "cryptography": "arch_crypto", "serialization_parsing": "arch_serialization", "regex_execution": "arch_regex", "time_date_logic": "arch_time", "feature_flags": "arch_feature_flags", "inline_asm": "arch_inline_asm", "safety": "def_safety", "freeze_hits": "def_freeze_hits", "cleanup": "def_cleanup", "sync_locks": "def_sync_locks", "test": "def_test", "test_skip": "def_test_skip", "doc": "def_doc", "listeners": "def_listeners", "encapsulation": "def_encapsulation", "auth_middleware": "def_auth", "telemetry": "def_telemetry", "ownership": "def_ownership", "spec_exposure": "def_spec_exposure", "sec_private_info": "threat_private_info", "sec_tainted_injection": "threat_tainted_injection", "sec_heat_triggers": "threat_obfuscated", "sec_bitwise_hits": "threat_crypto_math", "sec_extension_mismatch": "threat_extension_mismatch", "sec_entropy": "threat_entropy", "sec_danger": "threat_eval_exec", "sec_safety_neg": "threat_bypasses", "sec_io": "threat_network_hooks", "sec_flux": "threat_env_mutation", "sec_shadow_imports": "threat_stego_imports", "sec_homoglyphs": "threat_homoglyphs"
        }

    def record_mission(self, stars: List[Dict], singularity: List[Dict], summary: Dict, session_meta: Dict, output_path: str):
        """Builds the SQLite database directly from RAM."""
        repo_name = session_meta.get("target", "Unknown")
        git_audit = session_meta.get("git_audit", {})
        commit_date = git_audit.get("latest_commit_date", "Unknown").split("T")[0]
        commit_hash = git_audit.get("commit_hash", "Unknown")
        
        db_file = Path(output_path)
        self.logger.info(f"Record Keeper: Forging native SQLite database -> {db_file.name}")

        conn = sqlite3.connect(db_file)
        # Enforce foreign keys so cascading deletes work perfectly
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()

        # 1. DYNAMIC SCHEMA GENERATION
        risk_cols = [f"risk_{r.replace('-', '_')} REAL" for r in self.RISK_SCHEMA]
        hit_cols = [f"{self.SHORT_KEY_MAP.get(h, h)} INTEGER" for h in self.SIGNAL_SCHEMA]

        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS repo_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                repo_name TEXT,
                commit_date TEXT,
                commit_hash TEXT,
                total_files INTEGER,
                total_dark_matter INTEGER,
                total_loc INTEGER,
                total_coding_loc INTEGER,
                total_functions INTEGER,
                total_classes INTEGER,
                total_doc_files INTEGER,    -- <--- NEW: Markdown, Text, RST
                total_build_files INTEGER,  -- <--- NEW: Docker, Make, CMake, Shell
                total_config_files INTEGER, -- <--- NEW: JSON, YAML, TOML, XML
                total_test_files INTEGER,   -- <--- NEW: Test suites
                typosquat_hits INTEGER,
                macro_species TEXT,
                z_score REAL,
                avg_encapsulation_ratio REAL,
                avg_imports_per_file REAL,
                {", ".join(hit_cols)},
                file_composition TEXT,
                UNIQUE(repo_name, commit_hash)
            )
        ''')

        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS file_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                repo_name TEXT,
                commit_date TEXT,
                commit_hash TEXT,
                file_name TEXT,
                file_path TEXT,
                language TEXT,
                constellation TEXT,
                total_loc INTEGER,
                coding_loc INTEGER,
                structural_mass REAL,
                cog_raw REAL,
                ownership_entropy REAL,
                silo_risk REAL,
                raw_churn_freq REAL,
                popularity INTEGER,
                import_count INTEGER,
                total_downstream INTEGER, 
                total_upstream INTEGER,   
                downstream_ratio REAL,   
                upstream_ratio REAL,     
                control_flow_ratio REAL,
                function_count INTEGER,
                class_count INTEGER,
                func_complexity_vector TEXT,
                avg_func_loc REAL,
                avg_func_complexity REAL,
                max_func_complexity REAL,
                avg_func_args REAL,
                func_complexity_gini REAL,
                func_internal_density REAL,
                dependency_density REAL,
                encapsulation_ratio REAL,
                author TEXT,
                ai_threat_class TEXT,
                ai_threat_confidence REAL,
                func_z_max REAL DEFAULT 0.0, 
                func_z_mean REAL DEFAULT 0.0, 
                func_z_median REAL DEFAULT 0.0, 
                pct_z_above_5 REAL DEFAULT 0.0, 
                pct_z_above_15 REAL DEFAULT 0.0, 
                file_archetype TEXT, 
                file_fingerprint TEXT,
                ai_threat_score REAL,
                is_malware INTEGER,
                has_credentials INTEGER,
                binary_anomaly INTEGER,
                glassworm_flag INTEGER,
                {", ".join(risk_cols)},
                {", ".join(hit_cols)}
            )
        ''')

        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS function_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id INTEGER,
                func_name TEXT,
                complexity INTEGER,
                loc INTEGER,
                args INTEGER,
                usage_status INTEGER,
                keyword_density REAL,
                func_archetype TEXT DEFAULT 'Unclassified',
                func_z_score REAL DEFAULT 0.0,
                {", ".join(hit_cols)},
                FOREIGN KEY(file_id) REFERENCES file_data(id) ON DELETE CASCADE
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dark_matter_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                repo_name TEXT,
                commit_hash TEXT,
                file_path TEXT,
                extension TEXT,
                exclusion_reason TEXT,
                size_bytes INTEGER
            )
        ''')

        # ---> THE IDEMPOTENT WIPE <---
        cursor.execute("DELETE FROM file_data WHERE repo_name = ? AND commit_hash = ?", (repo_name, commit_hash))

        # 2. INSERTION LOOP
        agg_total_loc = 0
        agg_coding_loc = 0
        agg_func_count = 0
        agg_import_count = 0
        agg_encapsulation = 0.0
        agg_hits = [0] * len(self.SIGNAL_SCHEMA)
        
        # ---> NEW: INFRASTRUCTURE COUNTERS <---
        agg_doc_files = 0
        agg_build_files = 0
        agg_config_files = 0
        agg_test_files = 0

        for star in stars:
            tel = star.get("telemetry", {})
            sats = star.get("satellites", [])
            
            # Function Mathematics
            func_count = len(sats)
            complexities = [int(s.get("branch", 0)) for s in sats]
            locs = [int(s.get("loc", 0)) for s in sats]
            args_list = [int(s.get("args", 0)) for s in sats]
            
            avg_comp = float(sum(complexities) / func_count) if func_count > 0 else 0.0
            max_comp = float(max(complexities)) if func_count > 0 else 0.0
            avg_loc = float(sum(locs) / func_count) if func_count > 0 else 0.0
            avg_args = float(sum(args_list) / func_count) if func_count > 0 else 0.0
            func_comp_vector = json.dumps(complexities)
            
            # Z-SCORE CALCULATOR FOR "GOD FUNCTIONS"
            func_z_max = 0.0
            func_z_mean = 0.0
            func_z_median = 0.0
            pct_z_above_5 = 0.0
            pct_z_above_15 = 0.0
            z_scores = []
            
            if func_count > 0:
                mean_comp = statistics.mean(complexities)
                std_comp = statistics.pstdev(complexities) if func_count > 1 else 0.0
                
                for c in complexities:
                    z = (c - mean_comp) / std_comp if std_comp > 0 else 0.0
                    z_scores.append(round(z, 3))
                    
                if z_scores:
                    func_z_max = max(z_scores)
                    func_z_mean = statistics.mean(z_scores)
                    func_z_median = statistics.median(z_scores)
                    pct_z_above_5 = (sum(1 for z in z_scores if z > 5.0) / func_count) * 100.0
                    pct_z_above_15 = (sum(1 for z in z_scores if z > 15.0) / func_count) * 100.0

            func_internal_density = (avg_comp / avg_loc) if avg_loc > 0 else 0.0
            
            logic_loc_denom = max(int(star.get("coding_loc", 1) * tel.get("control_flow_ratio", 0.0)), 1)
            import_count = len(star.get("raw_imports", []))
            dependency_density = import_count / float(logic_loc_denom)

            ai_threat_conf_str = tel.get("domain_context", {}).get("AI Threat Confidence", tel.get("domain_context", {}).get("AI Threat Score", "0.0%"))
            ai_threat = float(str(ai_threat_conf_str).replace('%', '')) if ai_threat_conf_str else 0.0
            ai_threat_class = tel.get("domain_context", {}).get("AI Threat Class", "Safe")
            encapsulation_ratio = float(tel.get("encapsulation_ratio", 1.0))

            rv = star.get("risk_vector", [0.0] * len(self.RISK_SCHEMA))
            hv = star.get("hit_vector", [0] * len(self.SIGNAL_SCHEMA))

            file_archetype = tel.get("archetype", "Unknown")
            file_fingerprint_str = json.dumps(tel.get("archetype_fingerprint", {}))

            agg_total_loc += star.get("total_loc", 0)
            agg_coding_loc += star.get("coding_loc", 0)
            agg_func_count += func_count
            agg_import_count += import_count
            agg_encapsulation += encapsulation_ratio
            for i, val in enumerate(hv):
                if i < len(agg_hits):
                    agg_hits[i] += val

            # ---> NEW: TALLY THE INFRASTRUCTURE <---
            lang = star.get("lang_id", "unknown").lower()
            path_str = star.get("path", "").lower()
            
            if lang in ("markdown", "plaintext", "rst", "asciidoc"):
                agg_doc_files += 1
            elif lang in ("dockerfile", "makefile", "cmake", "shell", "batch", "powershell"):
                agg_build_files += 1
            elif lang in ("json", "yaml", "toml", "xml", "ini", "csv", "properties"):
                agg_config_files += 1
                
            if "/test" in path_str or "test_" in path_str or "_test" in path_str or ".test." in path_str:
                agg_test_files += 1

            # --- SECURITY EXTRACTIONS ---
            ai_score = float(star.get("ai_threat_score", 0.0))
            is_malware = 1 if star.get("is_malware", False) else 0
            has_creds = 1 if star.get("has_credentials", False) else 0
            bin_anomaly = 1 if star.get("binary_anomaly", False) else 0
            glassworm = 1 if star.get("glassworm_flag", False) else 0
            
            # --- N-TH DEGREE GRAPH EXTRACTION ---
            dep_net = star.get("dependency_network", {})
            tot_downstream = dep_net.get("total_downstream", 0)
            tot_upstream = dep_net.get("total_upstream", 0)
            
            total_repo_files = max(len(stars), 1) 
            down_ratio = round(tot_downstream / total_repo_files, 4)
            up_ratio = round(tot_upstream / total_repo_files, 4)

            # ---> FIXED: EXTRACT CLASS COUNT FOR THE FILE <---
            class_idx = self.SIGNAL_SCHEMA.index("class_start") if "class_start" in self.SIGNAL_SCHEMA else -1
            class_count = hv[class_idx] if class_idx >= 0 and class_idx < len(hv) else 0

            row_data = [
                repo_name, commit_date, commit_hash, Path(star.get("path", "")).name, star.get("path", ""),
                star.get("lang_id", "unknown"), star.get("constellation", "__monolith__"),
                star.get("total_loc", 0), star.get("coding_loc", 0),
                star.get("file_impact", 0.0), tel.get("densities", {}).get("cog_raw", 0.0),
                tel.get("ownership_entropy", 0.0), tel.get("author_distribution", 0.0),
                tel.get("raw_churn_freq", 0.0), tel.get("popularity", 0), import_count,
                tot_downstream, tot_upstream, down_ratio, up_ratio,
                tel.get("control_flow_ratio", 0.0), func_count, class_count, func_comp_vector,
                avg_loc, avg_comp, max_comp, avg_args, tel.get("func_complexity_gini", 0.0), 
                func_internal_density, dependency_density, encapsulation_ratio,
                tel.get("ownership", "Unknown"), ai_threat_class, ai_threat,
                func_z_max, func_z_mean, func_z_median, pct_z_above_5, pct_z_above_15,
                file_archetype, file_fingerprint_str,
                ai_score, is_malware, has_creds, bin_anomaly, glassworm
            ]
            
            row_data.extend(rv)
            row_data.extend(hv)

            placeholders = ",".join(["?"] * len(row_data))
            
            cursor.execute(f'''
                INSERT INTO file_data (
                    repo_name, commit_date, commit_hash, file_name, file_path, language, constellation, 
                    total_loc, coding_loc, structural_mass, cog_raw, ownership_entropy, silo_risk, 
                    raw_churn_freq, popularity, import_count, total_downstream, total_upstream, downstream_ratio, upstream_ratio,
                    control_flow_ratio, function_count, class_count,
                    func_complexity_vector, avg_func_loc, avg_func_complexity, max_func_complexity, 
                    avg_func_args, func_complexity_gini, func_internal_density, dependency_density, encapsulation_ratio,
                    author, ai_threat_class, ai_threat_confidence, 
                    func_z_max, func_z_mean, func_z_median, pct_z_above_5, pct_z_above_15, 
                    file_archetype, file_fingerprint,
                    ai_threat_score, is_malware, has_credentials, binary_anomaly, glassworm_flag,
                    {", ".join([f"risk_{r.replace('-', '_')}" for r in self.RISK_SCHEMA])},
                    {", ".join([self.SHORT_KEY_MAP.get(h, h) for h in self.SIGNAL_SCHEMA])}
                ) VALUES ({placeholders})
            ''', row_data)
            
            file_id = cursor.lastrowid

            # ---> FIXED: The Function Extraction Loop <---
            func_rows = []
            for s in sats:
                raw_hv = s.get("hit_vector", {})
                func_hits = [int(raw_hv.get(h, 0)) for h in self.SIGNAL_SCHEMA]
                
                func_row_data = [
                    file_id, 
                    str(s.get("name", "unknown_function"))[:255], 
                    int(s.get("branch", 0)), 
                    int(s.get("loc", 0)), 
                    int(s.get("args", 0)), 
                    int(s.get("usage_status", 0)),
                    float(s.get("keyword_density", 0.0)),
                    s.get("archetype", "Unclassified"), 
                    float(s.get("z_score", 0.0))        
                ] + func_hits
                
                func_rows.append(func_row_data)

            if func_rows:
                func_placeholders = ",".join(["?"] * len(func_rows[0]))
                cursor.executemany(f'''
                    INSERT INTO function_data 
                    (file_id, func_name, complexity, loc, args, usage_status, keyword_density, func_archetype, func_z_score, {", ".join([self.SHORT_KEY_MAP.get(h, h) for h in self.SIGNAL_SCHEMA])}) 
                    VALUES ({func_placeholders})
                ''', func_rows)

        # 3. REPO DATA INSERTION
        class_start_idx = self.SIGNAL_SCHEMA.index("class_start") if "class_start" in self.SIGNAL_SCHEMA else -1
        total_classes = agg_hits[class_start_idx] if class_start_idx >= 0 else 0
        
        macro_info = summary.get("repo_macro_species", {})
        repo_composition_str = json.dumps(summary.get("composition", {}))
        
        total_files = len(stars)
        total_dark_matter = len(singularity)
        
        avg_encapsulation = (agg_encapsulation / total_files) if total_files > 0 else 1.0
        avg_imports = (agg_import_count / total_files) if total_files > 0 else 0.0
        
        typosquat_count = summary.get("typosquat_hits", 0)
        
        repo_row_data = [
            repo_name,
            commit_date,
            commit_hash,
            total_files,
            total_dark_matter,  
            agg_total_loc,
            agg_coding_loc,
            agg_func_count,
            total_classes,
            agg_doc_files,      
            agg_build_files,    
            agg_config_files,   
            agg_test_files,     
            typosquat_count,    # <--- FIXED: Now matches the variable name above!
            macro_info.get("name", "Unclassified"),
            float(macro_info.get("z_score", 0.0)),
            round(avg_encapsulation, 3),
            round(avg_imports, 3)
        ] + agg_hits + [repo_composition_str]

        repo_placeholders = ",".join(["?"] * len(repo_row_data))
        cursor.execute(f'''
            INSERT OR REPLACE INTO repo_data (
                repo_name, commit_date, commit_hash, total_files, total_dark_matter, total_loc, total_coding_loc, 
                total_functions, total_classes, total_doc_files, total_build_files, total_config_files, total_test_files, 
                typosquat_hits, macro_species, z_score,
                avg_encapsulation_ratio, avg_imports_per_file,
                {", ".join([self.SHORT_KEY_MAP.get(h, h) for h in self.SIGNAL_SCHEMA])},
                file_composition
            ) VALUES ({repo_placeholders})
        ''', repo_row_data)
        
        # 4. DARK MATTER LEDGER INSERTION
        dark_rows = []
        for dark in singularity:
            path = dark.get("path", "")
            ext = Path(path).suffix.lower() if '.' in Path(path).name else "none"
            dark_rows.append([
                repo_name, commit_hash, path, ext,
                dark.get("reason", "Unknown"), dark.get("size_bytes", 0)
            ])
            
        if dark_rows:
            cursor.executemany('''
                INSERT INTO dark_matter_data 
                (repo_name, commit_hash, file_path, extension, exclusion_reason, size_bytes)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', dark_rows)

        conn.commit()
        conn.close()
        self.logger.info(f"Database sealed. Exported {len(stars)} files and functions to {db_file.name}")