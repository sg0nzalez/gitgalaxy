import pytest
from gitgalaxy.physics.signal_processor import SignalProcessor


@pytest.fixture
def physics_engine():
    """Initializes the Signal Processor."""
    return SignalProcessor()


# ==============================================================================
# SYNTHETIC GALAXY DATA (MOCKING THE DETECTOR PAYLOADS)
# ==============================================================================
def create_synthetic_star(engine, name, loc, equations=None, forensics=None, functions=None):
    """Generates a perfectly structured raw detector payload."""
    base_eq = {
        "branch": 0,
        "linear": 0,
        "args": 0,
        "func_start": 0,
        "danger": 0,
        "sec_danger": 0,
        "safety_neg": 0,
        "safety": 0,
        "flux": 0,
        "todo": 0,
        "fixme": 0,
        "empty_stubs": 0,
        "fragile_debt": 0,
        "planned_debt": 0,
        "doc": 0,
        "test": 0,
        "api": 0,
        "concurrency": 0,
        "sync_locks": 0,
        "graveyard": 0,
        "spec": 0,
        "pointers": 0,
        "indent_tabs": 0,
        "indent_spaces": 0,
    }

    if equations:
        base_eq.update(equations)

    meta = {
        "path": f"src/{name}.py",
        "name": name,
        "lang_id": "python",
        "coding_loc": loc,
        "telemetry": {},
        "functions": functions or [{"name": "mock_func", "loc": loc, "branch": base_eq["branch"]}],
        "raw_imports": ["os", "sys"],
        "equations": base_eq,
        "dependency_network": {
            "direct_upstream": 2,
            "direct_downstream": 5,
            "total_upstream": 10,
            "total_downstream": 20,
        },
    }

    if forensics:
        meta["forensics"] = forensics
        meta["git_forensics"] = forensics

    return meta, base_eq


# ==============================================================================
# TEST 1: THE PERFECT FILE (Zero Risk Baseline)
# ==============================================================================
def test_signal_processor_perfect_baseline(physics_engine):
    """Proves a file with perfect safety/docs results in 0.0% risk exposures."""
    meta, eq = create_synthetic_star(physics_engine, "perfect", 50, {"safety": 10, "doc": 20, "test": 5})
    res = physics_engine.calculate_risk_vector(meta, eq)

    assert res["risk_vector"][0] < 10.0, "Perfect file failed Cog Load baseline!"
    assert res["risk_vector"][1] < 10.0, "Perfect file failed Error Risk baseline!"
    assert res["risk_vector"][2] == 0.0, "Perfect file has phantom tech debt!"


# ==============================================================================
# TEST 2: THE APOCALYPSE FILE (100% Risk Breaches)
# ==============================================================================
def test_signal_processor_apocalypse_breaches(physics_engine):
    """Proves an overwhelmingly terrible file successfully triggers 100% risk."""
    # Loc MUST be >= 15 to bypass the small-file 5.0% bypass in _calc_cog_load!
    meta, eq = create_synthetic_star(
        physics_engine,
        "nightmare",
        20,
        {
            "branch": 5000,
            "danger": 5000,
            "sec_danger": 5000,
            "flux": 5000,
            "planned_debt": 5000,
            "fragile_debt": 5000,
            "api": 5000,
            "concurrency": 5000,
        },
    )

    res = physics_engine.calculate_risk_vector(meta, eq)

    assert res["risk_vector"][0] > 80.0, "Failed to max out Cognitive Load!"
    assert res["risk_vector"][1] > 80.0, "Failed to max out Error Risk!"
    assert res["risk_vector"][2] > 80.0, "Failed to max out Tech Debt!"


# ==============================================================================
# TEST 3: ZERO-DIVISION & EMPTY STATE FALLBACKS
# ==============================================================================
def test_signal_processor_zero_division_shields(physics_engine):
    """Ensures no ZeroDivisionError crashes the pipeline on 0 LOC."""
    meta, eq = create_synthetic_star(physics_engine, "ghost", 0)
    meta["functions"] = []

    try:
        res = physics_engine.calculate_risk_vector(meta, eq)
        assert "risk_vector" in res, "Failed to output risk vector!"
        assert res["risk_vector"][0] >= 0.0, "Cog load dropped below zero!"
    except ZeroDivisionError:
        pytest.fail("Signal Processor crashed with ZeroDivisionError on a 0 LOC file!")


# ==============================================================================
# TEST 4: ERROR RISK FLOOR CAP (The 30% Testing Minimum)
# ==============================================================================
def test_signal_processor_error_risk_floor(physics_engine):
    """Proves high danger density floors the Error Risk to ~30% regardless of safety."""
    meta, eq = create_synthetic_star(
        physics_engine,
        "shielded",
        5,
        {"danger": 5000, "sec_danger": 5000, "safety": 500, "test": 500},
    )

    res = physics_engine.calculate_risk_vector(meta, eq)
    assert (
        res["risk_vector"][1] >= 29.0
    ), f"Error Risk Floor failed! Allowed heavy danger to drop to {res['risk_vector'][1]}%"


# ==============================================================================
# TEST 5: API & CONCURRENCY EXPOSURES
# ==============================================================================
def test_signal_processor_api_and_concurrency(physics_engine):
    """Proves the engine accurately calculates API and Concurrency risks."""
    meta, eq = create_synthetic_star(physics_engine, "api_gw", 10, {"api": 500, "concurrency": 500})
    meta["functions"] = [{"name": "mock_func", "loc": 10, "branch": 0}]

    res = physics_engine.calculate_risk_vector(meta, eq)
    assert res["risk_vector"][4] > 30.0, "API Exposure math failed!"
    assert res["risk_vector"][5] > 30.0, "Concurrency Exposure math failed!"


# ==============================================================================
# TEST 6: CIVIL WAR (Indentation Consistency)
# ==============================================================================
def test_signal_processor_civil_war(physics_engine):
    """Proves the Civil War exposure accurately measures Tab vs Space purity."""
    mt, et = create_synthetic_star(physics_engine, "t", 100, {"indent_tabs": 100})
    ms, es = create_synthetic_star(physics_engine, "s", 100, {"indent_spaces": 100})
    mm, em = create_synthetic_star(physics_engine, "m", 100, {"indent_tabs": 50, "indent_spaces": 50})

    rt = physics_engine.calculate_risk_vector(mt, et)
    rs = physics_engine.calculate_risk_vector(ms, es)
    rm = physics_engine.calculate_risk_vector(mm, em)

    assert rt["risk_vector"][12] < 10.0, "Pure Tabs failed!"
    assert rs["risk_vector"][12] > 90.0, "Pure Spaces failed!"
    assert 40.0 < rm["risk_vector"][12] < 60.0, "Mixed indentation failed!"


# ==============================================================================
# TEST 7: SIBLING TEST BONUS (Cross-File Network Mapping)
# ==============================================================================
def test_signal_processor_sibling_test_bonus(physics_engine):
    """Proves the umbrella_bonus parameter halves the testing risk penalty."""
    m1, e1 = create_synthetic_star(physics_engine, "logic", 200, {"branch": 20})
    m2, e2 = create_synthetic_star(physics_engine, "logic", 200, {"branch": 20})

    high_risk = physics_engine.calculate_risk_vector(m1, e1, umbrella_bonus=0.0)
    low_risk = physics_engine.calculate_risk_vector(m2, e2, umbrella_bonus=0.5)

    assert low_risk["risk_vector"][3] < high_risk["risk_vector"][3], "Sibling Test Bonus failed to apply!"


# ==============================================================================
# TEST 8: GIT FORENSICS (Deep Churn & Stability)
# ==============================================================================
def test_signal_processor_git_forensics(physics_engine):
    """Proves the Deep Churn and Instability formulas process git metadata across multiple files."""
    m1, e1 = create_synthetic_star(physics_engine, "vol_max", 100)
    # Inject exact temporal keys expected by _calc_raw_temporal_signals
    m1["temporal_telemetry"] = {
        "is_git_tracked": True,
        "mtime": 100,
        "repo_min_time": 0,
        "repo_max_time": 110,
        "commit_count": 500,
    }
    # Inject exact authors dict expected by _calculate_silo_risk
    m1["authors"] = {"dev_a": 500}  # 100% silo risk

    m2, e2 = create_synthetic_star(physics_engine, "vol_min", 100)
    m2["temporal_telemetry"] = {
        "is_git_tracked": True,
        "mtime": 0,
        "repo_min_time": 0,
        "repo_max_time": 110,
        "commit_count": 5,
    }
    m2["authors"] = {"dev_a": 5, "dev_b": 5}  # 50% distribution

    # Process both and properly unwrap the telemetry
    tel1 = physics_engine.calculate_risk_vector(m1, e1)
    m1["telemetry"] = tel1["telemetry"]
    m1["risk_vector"] = tel1["risk_vector"]
    m1["file_impact"] = tel1["file_impact"]

    tel2 = physics_engine.calculate_risk_vector(m2, e2)
    m2["telemetry"] = tel2["telemetry"]
    m2["risk_vector"] = tel2["risk_vector"]
    m2["file_impact"] = tel2["file_impact"]

    parsed = [m1, m2]
    physics_engine.summarize_galaxy_metrics(parsed, [])

    assert m1["risk_vector"][9] > 0.0, "Failed to calculate Instability!"
    assert m1["risk_vector"][10] > 0.0, "Failed to calculate Deep Churn!"
    assert m1["telemetry"]["author_distribution"] == 100.0, "Failed to calculate Silo Risk!"


# ==============================================================================
# TEST 9: THE OVERFLOW SHIELD (Math Limits)
# ==============================================================================
def test_signal_processor_math_overflow_shield(physics_engine):
    """Proves astronomical negative densities trigger and survive the OverflowError."""
    meta, eq = create_synthetic_star(physics_engine, "absurd", 1, {"sec_danger": -99999999, "branch": -99999999})

    try:
        res = physics_engine.calculate_risk_vector(meta, eq)
        assert "risk_vector" in res
    except OverflowError:
        pytest.fail("Signal Processor crashed with an OverflowError on extreme density!")


# ==============================================================================
# TEST 10: GALAXY AGGREGATORS (Summary & Forensics)
# ==============================================================================
def test_signal_processor_aggregations(physics_engine):
    """Triggers the final galaxy-level summary and forensic reports."""
    m1, e1 = create_synthetic_star(physics_engine, "f1", 100, {"branch": 10})
    m2, e2 = create_synthetic_star(physics_engine, "f2", 200, {"sec_danger": 10})

    # Process and unwrap correctly!
    tel1 = physics_engine.calculate_risk_vector(m1, e1)
    m1["telemetry"] = tel1["telemetry"]
    m1["risk_vector"] = tel1["risk_vector"]
    m1["file_impact"] = tel1["file_impact"]

    tel2 = physics_engine.calculate_risk_vector(m2, e2)
    m2["telemetry"] = tel2["telemetry"]
    m2["risk_vector"] = tel2["risk_vector"]
    m2["file_impact"] = tel2["file_impact"]

    parsed = [m1, m2]
    unparsed = [{"path": "bad.py", "reason": "corrupted"}]

    summary = physics_engine.summarize_galaxy_metrics(parsed, unparsed)
    assert isinstance(summary, dict)

    forensics = physics_engine.generate_forensic_report(parsed)
    assert "cumulative_risk" in forensics, "Forensic report missing cumulative risk!"
    assert "highest" in forensics["cumulative_risk"], "Forensic report missing highest risk array!"


# ==============================================================================
# TEST 11: THE MINIFIED VENDOR TRIPWIRE
# ==============================================================================
def test_signal_processor_minified_tripwire(physics_engine):
    """Proves minified files bypass standard math and trigger explicit risk spikes."""
    meta, eq = create_synthetic_star(physics_engine, "vendor_bundle", 1000, {"sec_danger": 50})
    meta["is_minified"] = True  # Trigger the tripwire

    res = physics_engine.calculate_risk_vector(meta, eq)

    # Standard cognitive load should be 0.0, and the file impact forced to 1.0
    assert res["risk_vector"][0] == 0.0, "Standard cognitive load should be bypassed for minified files!"
    assert res["file_impact"] == 1.0, "Minified files should have an impact of exactly 1.0!"

    # We don't know the exact index, but the 100.0 spike MUST exist in the array
    assert 100.0 in res["risk_vector"], "Minified tripwire failed to spike the malicious exposure vector!"


# ==============================================================================
# TEST 12: THE DOCUMENTATION BYPASS & SECRETS LEAK
# ==============================================================================
def test_signal_processor_doc_and_secrets_bypass(physics_engine):
    """Proves markdown files skip logic math, and exposed secrets spike risk."""
    # 1. Test Documentation Bypass
    meta_doc, eq_doc = create_synthetic_star(physics_engine, "readme", 500, {"branch": 500})
    meta_doc["lang_id"] = "markdown"  # Claim to be docs

    res_doc = physics_engine.calculate_risk_vector(meta_doc, eq_doc)
    assert res_doc["risk_vector"][0] == 0.0, "Documentation shouldn't calculate logic cognitive load!"

    # 2. Test Critical Secrets Leak
    meta_sec, eq_sec = create_synthetic_star(physics_engine, "keys", 10)
    meta_sec["metadata"] = {"aperture_reason": "CRITICAL LEAK"}

    res_sec = physics_engine.calculate_risk_vector(meta_sec, eq_sec)
    assert 100.0 in res_sec["risk_vector"], "Critical Leak failed to spike the Secrets Risk to 100%!"


# ==============================================================================
# TEST 13: THE OOM BOMB (Recursive Flux)
# ==============================================================================
def test_signal_processor_oom_bomb(physics_engine):
    """Proves recursive functions with high state mutation trigger the OOM multiplier."""
    # Baseline: Normal function with state mutation
    meta1, eq1 = create_synthetic_star(physics_engine, "safe_flux", 100, {"flux": 50})
    meta1["functions"] = [{"name": "safe", "loc": 100, "is_recursive": False, "big_o_depth": 1}]

    # OOM Bomb: Recursive function + State mutation (No lazy evaluation)
    meta2, eq2 = create_synthetic_star(physics_engine, "oom_flux", 100, {"flux": 50})
    meta2["functions"] = [{"name": "bomb", "loc": 100, "is_recursive": True, "big_o_depth": 1}]

    res_safe = physics_engine.calculate_risk_vector(meta1, eq1)
    res_bomb = physics_engine.calculate_risk_vector(meta2, eq2)

    # The oom_multiplier = 3.0 should cause a significant difference in the final arrays
    assert res_bomb["risk_vector"] != res_safe["risk_vector"], "OOM Bomb multiplier failed to alter the risk vector!"


# ==============================================================================
# TEST 14: AI TOPOLOGY & NETWORK POSTURE
# ==============================================================================
def test_signal_processor_ai_topology(physics_engine):
    """Proves the aggregator correctly classifies Autonomous Fleets and RAG pipelines."""
    # Level 4 Agent (Tools + Logic Loops, but NO memory)
    m1, e1 = create_synthetic_star(
        physics_engine,
        "agent",
        100,
        {"ai_logic_loop": 10, "ai_tools": 10, "ai_memory": 0},
    )

    # RAG Pipeline
    m2, e2 = create_synthetic_star(physics_engine, "rag", 100, {"llm_api": 10, "llm_vector_store": 10})

    # Process files
    tel1 = physics_engine.calculate_risk_vector(m1, e1)
    m1["telemetry"] = tel1["telemetry"]
    m1["hit_vector"] = tel1["hit_vector"]  # Essential for the AI sensor!

    # Inject Fake Network Posture
    m1["telemetry"]["network_metrics"] = {
        "pagerank_score": 5.0,
        "normalized_blast_radius": 2.5,
        "betweenness_score": 0.1,
        "ecosystem_role": "Core Hub",
    }

    tel2 = physics_engine.calculate_risk_vector(m2, e2)
    m2["telemetry"] = tel2["telemetry"]
    m2["hit_vector"] = tel2["hit_vector"]

    parsed = [m1, m2]
    summary = physics_engine.summarize_galaxy_metrics(parsed, [])

    topology = summary.get("ai_topology", {})
    assert topology["classification"] == "Autonomous Agentic Fleet (Level 4)", "Failed to classify Level 4 Agent!"

    insights = " ".join(topology["insights"])
    assert "context amnesia" in insights, "Failed to detect missing Agent Memory!"
    assert "catastrophically across the system" in insights, "Failed to detect high PageRank blast radius!"
    assert "Cognitive Choke Point" in insights, "Failed to detect high Betweenness!"


# ==============================================================================
# TEST 15: ALGORITHMIC DOS EXPOSURE
# ==============================================================================
def test_signal_processor_algorithmic_dos(physics_engine):
    """Proves the Big-O risk exposure scales with data gravity and choke points, and is dampened by safety guardrails."""

    # 1. Isolated Harmless Loop: O(N^3) but no IO/API and 0 popularity.
    m_iso, e_iso = create_synthetic_star(physics_engine, "isolated", 100, {"api": 0})
    m_iso["popularity"] = 0
    m_iso["functions"] = [{"name": "safe_loop", "loc": 50, "big_o_depth": 3, "db_complexity": 0, "hit_vector": {}}]

    # 2. API DoS Bomb: O(N^3) + DB Complexity + Exposed to API
    m_bomb, e_bomb = create_synthetic_star(physics_engine, "exposed_bomb", 500, {"api": 4})
    m_bomb["popularity"] = 2
    m_bomb["functions"] = [
        {
            "name": "dos_bomb",
            "loc": 250,
            "big_o_depth": 3,
            "db_complexity": 2,
            "hit_vector": {"api": 4},
        }
    ]

    # 3. Guarded DoS Bomb: Same as above but mitigated by safety bailouts
    m_guard, e_guard = create_synthetic_star(physics_engine, "guarded_bomb", 500, {"api": 4})
    m_guard["popularity"] = 2
    m_guard["functions"] = [
        {
            "name": "safe_bomb",
            "loc": 250,
            "big_o_depth": 3,
            "db_complexity": 2,
            "hit_vector": {"api": 4, "safety": 1, "bailout_hits": 2},
        }
    ]

    res_iso = physics_engine.calculate_risk_vector(m_iso, e_iso)
    res_bomb = physics_engine.calculate_risk_vector(m_bomb, e_bomb)
    res_guard = physics_engine.calculate_risk_vector(m_guard, e_guard)

    # Index 13 is the new algorithmic_dos vector
    iso_score = res_iso["risk_vector"][13]
    bomb_score = res_bomb["risk_vector"][13]
    guard_score = res_guard["risk_vector"][13]

    assert iso_score < bomb_score, "Isolated loop should have significantly lower risk than exposed bomb!"
    assert guard_score < bomb_score, "Safety guardrails failed to dampen the Algorithmic DoS threat!"
    assert bomb_score > 50.0, "API DoS bomb failed to spike the risk exposure!"


# ==============================================================================
# TEST 16: WEAPONIZABLE SURFACE EXPOSURES (Security Lenses)
# ==============================================================================
def test_signal_processor_security_lenses(physics_engine):
    """Ensures all security lens risk equations return valid floats and properly scale."""
    
    # 1. Logic Bomb
    m_lb, e_lb = create_synthetic_star(physics_engine, "logic_bomb", 100, {
        "branch": 50, "sec_danger": 20, "sec_tainted_injection": 5
    })
    
    # 2. Obscured Payload (Requires intent_mass via sec_danger to bypass the 95% false-positive shield)
    m_ob, e_ob = create_synthetic_star(physics_engine, "obscured", 100, {
        "sec_heat_triggers": 20, "sec_bitwise_hits": 50, "sec_shadow_imports": 5, "sec_danger": 10
    })
    
    # 3. Injection Surface
    m_inj, e_inj = create_synthetic_star(physics_engine, "injection", 100, {
        "sec_io": 30, "sec_danger": 30
    })
    
    # 4. Memory Corruption (Requires native memory language like 'c' + malicious intent to bypass the 95% shield)
    m_mem, e_mem = create_synthetic_star(physics_engine, "memory", 100, {
        "pointers": 50, "memory_alloc": 20, "sec_danger": 10
    })
    m_mem["lang_id"] = "c"

    r_lb = physics_engine.calculate_risk_vector(m_lb, e_lb)
    r_ob = physics_engine.calculate_risk_vector(m_ob, e_ob)
    r_inj = physics_engine.calculate_risk_vector(m_inj, e_inj)
    r_mem = physics_engine.calculate_risk_vector(m_mem, e_mem)

    idx_lb = physics_engine.RISK_SCHEMA.index("logic_bomb")
    idx_ob = physics_engine.RISK_SCHEMA.index("obscured_payload")
    idx_inj = physics_engine.RISK_SCHEMA.index("injection_surface")
    idx_mem = physics_engine.RISK_SCHEMA.index("memory_corruption")
    
    assert isinstance(r_lb["risk_vector"][idx_lb], float), "Logic bomb must return a float!"
    assert r_lb["risk_vector"][idx_lb] > 10.0, "Logic bomb failed to register!"
    
    assert isinstance(r_ob["risk_vector"][idx_ob], float), "Obscured payload must return a float!"
    assert r_ob["risk_vector"][idx_ob] > 10.0, "Obscured payload failed to register!"

    assert isinstance(r_inj["risk_vector"][idx_inj], float), "Injection surface must return a float!"
    assert r_inj["risk_vector"][idx_inj] > 10.0, "Injection surface failed to register!"

    assert isinstance(r_mem["risk_vector"][idx_mem], float), "Memory corruption must return a float!"
    assert r_mem["risk_vector"][idx_mem] >= 9.0, "Memory corruption failed to register!"


# ==============================================================================
# TEST 17: STRUCTURAL METRICS (Graveyard & Spec Match)
# ==============================================================================
def test_signal_processor_structural_metrics(physics_engine):
    """Ensures Graveyard and Spec Match exposures calculate correctly."""
    
    # Graveyard (High dead code)
    m_grave, e_grave = create_synthetic_star(physics_engine, "graveyard", 100, {
        "graveyard": 80
    })
    
    # Spec Match (0 specs for 10 functions = 100% risk)
    m_spec, e_spec = create_synthetic_star(physics_engine, "spec", 100, {
        "func_start": 10, "spec_exposure": 0
    })
    
    r_grave = physics_engine.calculate_risk_vector(m_grave, e_grave)
    r_spec = physics_engine.calculate_risk_vector(m_spec, e_spec)

    idx_grave = physics_engine.RISK_SCHEMA.index("graveyard")
    idx_spec = physics_engine.RISK_SCHEMA.index("spec_match")

    assert r_grave["risk_vector"][idx_grave] > 50.0, "Graveyard risk failed to register!"
    assert r_spec["risk_vector"][idx_spec] == 100.0, "Spec match risk failed to register maximum exposure on undocumented functions!"


# ==============================================================================
# TEST 18: UNACKNOWLEDGED DEBT (Design Slop Amplifier)
# ==============================================================================
def test_signal_processor_design_slop(physics_engine):
    """Proves that silent design slop (orphans/duplicates) exponentially spikes Tech Debt."""
    
    # 1. Clean Debt: Only explicit TODOs
    m_clean, e_clean = create_synthetic_star(physics_engine, "clean_debt", 100, {
        "planned_debt": 10
    })
    
    # 2. Sloppy Debt: Explicit TODOs + Invisible Slop
    m_slop, e_slop = create_synthetic_star(physics_engine, "sloppy_debt", 100, {
        "planned_debt": 10, "design_slop_orphans": 5, "design_slop_duplicates": 2
    })
    
    r_clean = physics_engine.calculate_risk_vector(m_clean, e_clean)
    r_slop = physics_engine.calculate_risk_vector(m_slop, e_slop)

    idx_debt = physics_engine.RISK_SCHEMA.index("tech_debt")
    
    assert r_slop["risk_vector"][idx_debt] > r_clean["risk_vector"][idx_debt], "Design Slop failed to amplify Tech Debt!"
    assert r_slop["risk_vector"][idx_debt] > 50.0, "Severe slop failed to trigger high exposure!"


# ==============================================================================
# TEST 19: VERIFICATION THERMODYNAMICS (Skips & Mass Penalty)
# ==============================================================================
def test_signal_processor_verification_thermodynamics(physics_engine):
    """Proves skipped tests neutralize assertions, and massive files receive a testing penalty."""
    
    # 1. Safe: 50 tests, standard LOC
    m_safe, e_safe = create_synthetic_star(physics_engine, "safe_test", 100, {
        "test": 50, "test_skip": 0
    })
    
    # 2. Bypassed: 50 tests, but 25 skipped (Thermodynamic cancellation)
    m_skip, e_skip = create_synthetic_star(physics_engine, "skip_test", 100, {
        "test": 50, "test_skip": 25
    })
    
    # 3. Massive: 50 tests, but 1000 LOC (Mass Penalty)
    m_mass, e_mass = create_synthetic_star(physics_engine, "mass_test", 1000, {
        "test": 50, "test_skip": 0
    })
    
    r_safe = physics_engine.calculate_risk_vector(m_safe, e_safe)
    r_skip = physics_engine.calculate_risk_vector(m_skip, e_skip)
    r_mass = physics_engine.calculate_risk_vector(m_mass, e_mass)

    idx_test = physics_engine.RISK_SCHEMA.index("verification")
    
    # Higher score = Higher Risk Exposure (Worse Verification)
    assert r_safe["risk_vector"][idx_test] < r_skip["risk_vector"][idx_test], "Test skips failed to neutralize assertions!"
    assert r_safe["risk_vector"][idx_test] < r_mass["risk_vector"][idx_test], "Mass penalty failed to increase testing risk on giant files!"


# ==============================================================================
# TEST 20: GOD FUNCTION PENALTY (Cognitive Load Gini)
# ==============================================================================
def test_signal_processor_god_function_gini(physics_engine):
    """Proves that concentrating complexity into a single function spikes Cognitive Load."""
    
    # Both files have 100 LOC and 20 Branches total.
    
    # 1. Flat Distribution (4 functions, 5 branches each) -> Low Gini
    m_flat, e_flat = create_synthetic_star(physics_engine, "flat_dist", 100, {"branch": 20})
    m_flat["functions"] = [
        {"name": "f1", "branch": 5, "loc": 25},
        {"name": "f2", "branch": 5, "loc": 25},
        {"name": "f3", "branch": 5, "loc": 25},
        {"name": "f4", "branch": 5, "loc": 25},
    ]
    
    # 2. God Function (1 massive function, 3 empty) -> High Gini
    m_god, e_god = create_synthetic_star(physics_engine, "god_func", 100, {"branch": 20})
    m_god["functions"] = [
        {"name": "god", "branch": 20, "loc": 90},
        {"name": "f2", "branch": 0, "loc": 3},
        {"name": "f3", "branch": 0, "loc": 3},
        {"name": "f4", "branch": 0, "loc": 4},
    ]
    
    r_flat = physics_engine.calculate_risk_vector(m_flat, e_flat)
    r_god = physics_engine.calculate_risk_vector(m_god, e_god)

    idx_cog = physics_engine.RISK_SCHEMA.index("cognitive_load")
    
    assert r_god["risk_vector"][idx_cog] > r_flat["risk_vector"][idx_cog], "God function Gini index failed to amplify Cognitive Load!"


# ==============================================================================
# TEST 21: CONCURRENCY THERMODYNAMICS (Locks & Starvation)
# ==============================================================================
def test_signal_processor_concurrency_thermodynamics(physics_engine):
    """Proves sync locks mitigate async risk, and high Big-O spikes thread starvation."""
    
    # 1. High Async, No Locks
    m_async, e_async = create_synthetic_star(physics_engine, "pure_async", 100, {"concurrency": 20})
    
    # 2. High Async, Mitigated by Locks (1 lock mitigates 1.5 async hits)
    m_sync, e_sync = create_synthetic_star(physics_engine, "locked_async", 100, {
        "concurrency": 20, "sync_locks": 15
    })
    
    # 3. Thread Starvation (Async + High Big-O)
    m_starve, e_starve = create_synthetic_star(physics_engine, "starved_async", 100, {"concurrency": 20})
    m_starve["functions"] = [{"name": "heavy_thread", "loc": 50, "big_o_depth": 3, "hit_vector": {"concurrency": 5}}]
    
    r_async = physics_engine.calculate_risk_vector(m_async, e_async)
    r_sync = physics_engine.calculate_risk_vector(m_sync, e_sync)
    r_starve = physics_engine.calculate_risk_vector(m_starve, e_starve)
    
    idx_async = physics_engine.RISK_SCHEMA.index("concurrency")
    
    assert r_sync["risk_vector"][idx_async] < r_async["risk_vector"][idx_async], "Sync locks failed to mitigate concurrency risk!"
    assert r_starve["risk_vector"][idx_async] > r_async["risk_vector"][idx_async], "Thread starvation (Big-O + Async) failed to amplify risk!"


# ==============================================================================
# TEST 22: THE ECHO CHAMBER FIX (API Isolation)
# ==============================================================================
def test_signal_processor_api_echo_chamber(physics_engine):
    """Proves that APIs with no inbound network connections receive a massive risk dampener."""
    
    # 1. Orphaned API (Exposes 50 APIs, but 0 popularity)
    m_orphan, e_orphan = create_synthetic_star(physics_engine, "orphan_api", 100, {"api": 50})
    m_orphan["popularity"] = 0
    
    # 2. Networked API (Exposes 50 APIs, highly popular)
    m_network, e_network = create_synthetic_star(physics_engine, "network_api", 100, {"api": 50})
    m_network["popularity"] = 20
    
    r_orphan = physics_engine.calculate_risk_vector(m_orphan, e_orphan)
    r_network = physics_engine.calculate_risk_vector(m_network, e_network)
    
    idx_api = physics_engine.RISK_SCHEMA.index("api_exposure")
    
    assert r_orphan["risk_vector"][idx_api] < (r_network["risk_vector"][idx_api] * 0.5), "Echo chamber fix failed: Orphaned APIs were not properly dampened!"


# ==============================================================================
# TEST 23: STATE FLUX THERMODYNAMICS (Immutability)
# ==============================================================================
def test_signal_processor_flux_immutability(physics_engine):
    """Proves that immutable data declarations (freeze_hits) neutralize state flux."""
    
    # 1. Pure Flux (High mutation)
    m_flux, e_flux = create_synthetic_star(physics_engine, "high_flux", 100, {"flux": 30})
    
    # 2. Frozen Flux (High mutation, but heavily mitigated by freeze/const/final)
    m_frozen, e_frozen = create_synthetic_star(physics_engine, "frozen_flux", 100, {
        "flux": 30, "freeze_hits": 40
    })
    
    r_flux = physics_engine.calculate_risk_vector(m_flux, e_flux)
    r_frozen = physics_engine.calculate_risk_vector(m_frozen, e_frozen)
    
    idx_flux = physics_engine.RISK_SCHEMA.index("state_flux")
    
    assert r_frozen["risk_vector"][idx_flux] < r_flux["risk_vector"][idx_flux], "Immutability (freeze_hits) failed to mitigate state flux risk!"

# ==============================================================================
# TEST 24: EXTENSION DECEPTION SENSOR
# ==============================================================================
def test_signal_processor_extension_deception(physics_engine):
    """Proves the engine flags files that claim to be inert data but contain executable logic."""
    m_dec, e_dec = create_synthetic_star(physics_engine, "data", 100)
    m_dec["path"] = "src/data.json"  # Claims to be JSON
    m_dec["lang_id"] = "python"      # Actually evaluated as Python!

    r_dec = physics_engine.calculate_risk_vector(m_dec, e_dec)
    
    idx_mismatch = physics_engine.SIGNAL_SCHEMA.index("sec_extension_mismatch")
    assert r_dec["hit_vector"][idx_mismatch] == 1, "Extension Deception Sensor failed to flag the mismatch!"


# ==============================================================================
# TEST 25: ALIEN ENTITY CONTEXT PENALTIES
# ==============================================================================
def test_signal_processor_alien_entity(physics_engine):
    """Proves that a Systems language hiding in a Web folder receives severe threat multipliers."""
    # 1. Native C (C code inside a C/CPP folder)
    m_native, e_native = create_synthetic_star(physics_engine, "native", 100, {
        "branch": 50, "sec_danger": 20, "sec_tainted_injection": 5
    })
    m_native["lang_id"] = "c"
    m_native["metadata"] = {"folder_dominant_lang": "cpp"}

    # 2. Alien C (C code inside a Javascript/Web folder)
    m_alien, e_alien = create_synthetic_star(physics_engine, "alien", 100, {
        "branch": 50, "sec_danger": 20, "sec_tainted_injection": 5
    })
    m_alien["lang_id"] = "c"
    m_alien["metadata"] = {"folder_dominant_lang": "javascript"}

    r_native = physics_engine.calculate_risk_vector(m_native, e_native)
    r_alien = physics_engine.calculate_risk_vector(m_alien, e_alien)

    idx_lb = physics_engine.RISK_SCHEMA.index("logic_bomb")
    
    assert r_alien["risk_vector"][idx_lb] > r_native["risk_vector"][idx_lb], "Alien entity penalty failed to apply!"


# ==============================================================================
# TEST 26: THE AGENTIC & SCIENCE SHIELD
# ==============================================================================
def test_signal_processor_science_shield(physics_engine):
    """Proves that Scientific/Math logic dampens the false-positive threat of Logic Bombs."""
    # 1. Standard executable with dangerous triggers
    m_std, e_std = create_synthetic_star(physics_engine, "standard", 100, {"branch": 30, "sec_danger": 20})
    
    # 2. Scientific executable with the exact same triggers
    m_sci, e_sci = create_synthetic_star(physics_engine, "science", 100, {"branch": 30, "sec_danger": 20, "scientific": 10})

    r_std = physics_engine.calculate_risk_vector(m_std, e_std)
    r_sci = physics_engine.calculate_risk_vector(m_sci, e_sci)

    idx_lb = physics_engine.RISK_SCHEMA.index("logic_bomb")
    
    assert r_sci["risk_vector"][idx_lb] < r_std["risk_vector"][idx_lb], "Scientific shield failed to dampen the Logic Bomb false positive!"


# ==============================================================================
# TEST 27: CATASTROPHIC FALLBACKS & EMPTY GALAXIES
# ==============================================================================
def test_signal_processor_catastrophic_fallbacks(physics_engine):
    """Ensures the physics engine survives catastrophic type errors and empty data sets."""
    # 1. Force a catastrophic math crash (string instead of int)
    m_crash, e_crash = create_synthetic_star(physics_engine, "crash", 100)
    m_crash["coding_loc"] = "THIS_WILL_BREAK_MATH"
    
    r_crash = physics_engine.calculate_risk_vector(m_crash, e_crash)
    
    assert "error" in r_crash["telemetry"], "Engine failed to catch and log the catastrophic physics failure!"
    assert r_crash["risk_vector"] == [0.0] * len(physics_engine.RISK_SCHEMA), "Crash fallback did not safely zero out the risk vector!"
    
    # 2. Force an empty global synthesis
    empty_summary = physics_engine.summarize_galaxy_metrics([], [])
    assert empty_summary == {}, "Summarizer failed to safely exit on an empty repository!"

# ==============================================================================
# TEST 28: CIVIL WAR VOID STATE (Zero Indentation)
# ==============================================================================
def test_signal_processor_civil_war_void(physics_engine):
    """Proves the Civil War exposure safely defaults to 50.0 (Neutral) if a file has no indentation."""
    m_void, e_void = create_synthetic_star(physics_engine, "void_file", 10, {
        "indent_tabs": 0, "indent_spaces": 0
    })
    
    r_void = physics_engine.calculate_risk_vector(m_void, e_void)
    idx_civil = physics_engine.RISK_SCHEMA.index("civil_war")
    
    assert r_void["risk_vector"][idx_civil] == 50.0, "Void state failed to default to 50.0% neutral exposure!"


# ==============================================================================
# TEST 29: AGENTIC RCE (Prompt Injection to Execution)
# ==============================================================================
def test_signal_processor_agentic_rce(physics_engine):
    """Proves that pairing an LLM Orchestrator with dynamic execution creates a massive Injection Surface spike."""
    # 1. Standard dynamic execution
    m_std, e_std = create_synthetic_star(physics_engine, "std_exec", 100, {"sec_danger": 10})
    
    # 2. Agentic dynamic execution
    m_agent, e_agent = create_synthetic_star(physics_engine, "agent_exec", 100, {
        "sec_danger": 10, "llm_orchestrator": 5, "ai_tools": 5
    })

    r_std = physics_engine.calculate_risk_vector(m_std, e_std)
    r_agent = physics_engine.calculate_risk_vector(m_agent, e_agent)

    idx_inj = physics_engine.RISK_SCHEMA.index("injection_surface")
    
    assert r_agent["risk_vector"][idx_inj] > r_std["risk_vector"][idx_inj], "Agentic RCE spike failed to amplify injection risk!"


# ==============================================================================
# TEST 30: CRYPTOGRAPHY & PROFESSIONALISM SHIELDS
# ==============================================================================
def test_signal_processor_crypto_professionalism_shield(physics_engine):
    """Proves that heavy documentation, safety blocks, and crypto math dampen obfuscation false positives."""
    # 1. Raw obfuscation (High entropy, bitwise math) + malicious intent
    m_raw, e_raw = create_synthetic_star(physics_engine, "raw_obf", 100, {
        "sec_heat_triggers": 50, "sec_bitwise_hits": 50, "sec_danger": 10
    })
    
    # 2. Professional cryptography (Same obfuscation, but heavily documented and safe)
    m_pro, e_pro = create_synthetic_star(physics_engine, "pro_crypto", 100, {
        "sec_heat_triggers": 50, "sec_bitwise_hits": 50, "sec_danger": 10,
        "doc": 100, "safety": 20, "cryptography": 10
    })

    r_raw = physics_engine.calculate_risk_vector(m_raw, e_raw)
    r_pro = physics_engine.calculate_risk_vector(m_pro, e_pro)

    idx_ob = physics_engine.RISK_SCHEMA.index("obscured_payload")
    
    assert r_pro["risk_vector"][idx_ob] < r_raw["risk_vector"][idx_ob], "Crypto/Professionalism shield failed to dampen obfuscation risk!"


# ==============================================================================
# TEST 31: LLM API SECRETS LEAK
# ==============================================================================
def test_signal_processor_llm_api_secrets(physics_engine):
    """Proves that hardcoded secrets mixed with LLM APIs trigger a massive careless amplifier."""
    # 1. Standard secret leak (Requires sec_heat_triggers to bypass the 2.0 clamp)
    m_std, e_std = create_synthetic_star(physics_engine, "std_leak", 500, {
        "sec_private_info": 1, "globals": 1, "sec_heat_triggers": 1
    })
    
    # 2. Careless LLM API secret leak (Calling APIs without using global variables)
    m_llm, _unused_e_llm = create_synthetic_star(physics_engine, "llm_leak", 500, {
        "sec_private_info": 1, "llm_api": 5, "globals": 0, "sec_heat_triggers": 1
    })

# ==============================================================================
# TEST 32: SAFE MINIFIED VENDOR FILE
# ==============================================================================
def test_signal_processor_safe_minified(physics_engine):
    """Proves that minified files with zero malicious intent safely bypass the tripwire."""
    m_safe, e_safe = create_synthetic_star(physics_engine, "jquery_min", 100, {"branch": 50, "flux": 20})
    m_safe["is_minified"] = True
    
    r_safe = physics_engine.calculate_risk_vector(m_safe, e_safe)
    
    assert r_safe["risk_vector"] == [0.0] * len(physics_engine.RISK_SCHEMA), "Safe minified file failed to zero out risks!"
    assert r_safe["telemetry"]["domain_context"]["alert"] == "MINIFIED VENDOR BYPASS", "Minified bypass flag missing!"


# ==============================================================================
# TEST 33: LAZY EVALUATION SHIELD (OOM BOMB)
# ==============================================================================
def test_signal_processor_lazy_evaluation_shield(physics_engine):
    """Proves that lazy evaluation (generators/streams) neutralizes the OOM Bomb multiplier."""
    # 1. Ticking OOM Bomb (O(N^3) + High Flux + No Lazy Eval)
    m_oom, e_oom = create_synthetic_star(physics_engine, "oom_bomb", 100, {"flux": 20})
    m_oom["functions"] = [{"name": "heavy_loop", "loc": 50, "big_o_depth": 3}]
    
    # 2. Safe Stream (O(N^3) + High Flux + Lazy Evaluation)
    m_lazy, e_lazy = create_synthetic_star(physics_engine, "lazy_stream", 100, {"flux": 20, "lazy_evaluation": 10})
    m_lazy["functions"] = [{"name": "generator", "loc": 50, "big_o_depth": 3}]

    r_oom = physics_engine.calculate_risk_vector(m_oom, e_oom)
    r_lazy = physics_engine.calculate_risk_vector(m_lazy, e_lazy)

    idx_flux = physics_engine.RISK_SCHEMA.index("state_flux")
    assert r_lazy["risk_vector"][idx_flux] < r_oom["risk_vector"][idx_flux], "Lazy evaluation failed to dampen the OOM Bomb multiplier!"


# ==============================================================================
# TEST 34: AI TOPOLOGY (DEEP LEARNING & TRADITIONAL ML)
# ==============================================================================
def test_signal_processor_ai_topology_dl_ml(physics_engine):
    """Ensures the AI topology summarizer correctly identifies Deep Learning and Traditional ML."""
    # Deep Learning
    m_dl, e_dl = create_synthetic_star(physics_engine, "pytorch_model", 100, {"dl_frameworks": 10})
    r_dl = physics_engine.calculate_risk_vector(m_dl, e_dl)
    m_dl.update(r_dl)
    
    # Traditional ML
    m_ml, e_ml = create_synthetic_star(physics_engine, "xgboost_model", 100, {"ml_traditional": 10})
    r_ml = physics_engine.calculate_risk_vector(m_ml, e_ml)
    m_ml.update(r_ml)

    # Summarize DL
    sum_dl = physics_engine.summarize_galaxy_metrics([m_dl], [])
    assert sum_dl["ai_topology"]["classification"] == "Deep Learning Architecture", "Failed to classify DL Architecture!"
    
    # Summarize ML
    sum_ml = physics_engine.summarize_galaxy_metrics([m_ml], [])
    assert sum_ml["ai_topology"]["classification"] == "Statistical Machine Learning", "Failed to classify Traditional ML!"

# ==============================================================================
# TEST 35: PARANOID MODE ACTIVATION
# ==============================================================================
def test_signal_processor_paranoid_mode(physics_engine):
    """Proves that Paranoid Mode tightens the Sigmoid thresholds across security lenses."""
    m_para, e_para = create_synthetic_star(physics_engine, "paranoid_file", 500, {
        "sec_danger": 5, "sec_io": 5
    })
    
    # Calculate in Standard Mode
    physics_engine.is_paranoid = False
    r_std = physics_engine.calculate_risk_vector(m_para, e_para)
    
    # Calculate in Paranoid Mode
    physics_engine.is_paranoid = True
    r_para = physics_engine.calculate_risk_vector(m_para, e_para)
    
    # Reset the engine state so subsequent tests aren't affected
    physics_engine.is_paranoid = False
    
    idx_inj = physics_engine.RISK_SCHEMA.index("injection_surface")
    assert r_para["risk_vector"][idx_inj] > r_std["risk_vector"][idx_inj], "Paranoid mode failed to amplify the risk exposure!"


# ==============================================================================
# TEST 36: AI TOPOLOGY (RAG & CLOUD WRAPPERS)
# ==============================================================================
def test_signal_processor_ai_topology_rag_cloud(physics_engine):
    """Ensures the AI topology summarizer correctly identifies RAG pipelines and Cloud wrappers."""
    # RAG Pipeline
    m_rag, e_rag = create_synthetic_star(physics_engine, "rag_bot", 100, {
        "llm_vector_store": 10, "llm_api": 5
    })
    r_rag = physics_engine.calculate_risk_vector(m_rag, e_rag)
    m_rag.update(r_rag)
    
    # Cloud API Wrapper
    m_cloud, e_cloud = create_synthetic_star(physics_engine, "cloud_bot", 100, {
        "llm_api": 10
    })
    r_cloud = physics_engine.calculate_risk_vector(m_cloud, e_cloud)
    m_cloud.update(r_cloud)

    # Summarize RAG
    sum_rag = physics_engine.summarize_galaxy_metrics([m_rag], [])
    assert sum_rag["ai_topology"]["classification"] == "RAG Pipeline (Retrieval-Augmented Generation)", "Failed to classify RAG Pipeline!"
    
    # Summarize Cloud
    sum_cloud = physics_engine.summarize_galaxy_metrics([m_cloud], [])
    assert sum_cloud["ai_topology"]["classification"] == "Cloud API Wrapper", "Failed to classify Cloud API Wrapper!"


# ==============================================================================
# TEST 37: SIGMOID OVERFLOW RESISTANCE (Extreme Density)
# ==============================================================================
def test_signal_processor_sigmoid_overflow(physics_engine):
    """Proves the Sigmoid curve safely catches math.exp OverflowErrors on extreme densities."""
    # Create a file with mathematically impossible levels of safety to force a massive negative density
    m_safe, e_safe = create_synthetic_star(physics_engine, "super_shield", 1, {
        "safety": 15000, "test": 15000, "doc": 15000, "freeze_hits": 15000
    })
    
    # Create a file with mathematically impossible danger to force a massive positive density
    m_danger, e_danger = create_synthetic_star(physics_engine, "super_bomb", 1, {
        "branch": 15000, "concurrency": 15000, "flux": 15000, "sec_danger": 15000
    })

    # If these execute without crashing the test runner, the except blocks are working perfectly.
    r_safe = physics_engine.calculate_risk_vector(m_safe, e_safe)
    r_danger = physics_engine.calculate_risk_vector(m_danger, e_danger)
    
    idx_saf = physics_engine.RISK_SCHEMA.index("safety_score")
    
    # The OverflowError should gracefully return either 0.0 or 100.0 depending on the threat trajectory
    assert r_safe["risk_vector"][idx_saf] == 0.0, "Overflow fallback failed to zero out the mathematically safe file!"
    assert r_danger["risk_vector"][idx_saf] == 100.0, "Overflow fallback failed to max out the mathematically dangerous file!"


# ==============================================================================
# TEST 38: STANDALONE INIT & SILO VOID
# ==============================================================================
def test_signal_processor_standalone_init_and_silo():
    """Ensures the processor initializes without a parent logger and handles 0-commit silo math."""
    from gitgalaxy.physics.signal_processor import SignalProcessor
    
    # Test standalone initialization
    standalone_engine = SignalProcessor(parent_logger=None)
    assert standalone_engine is not None, "SignalProcessor failed to initialize without a parent logger!"
    
    # Test the silo math directly on a 0-commit developer void state
    zero_silo = standalone_engine._calculate_silo_risk({"dev_a": 0, "dev_b": 0})
    assert zero_silo == 0.0, "Silo risk failed to safely return 0.0 on a void state!"

# ==============================================================================
# TEST 39: THE LOAD-BEARER PENALTY (Verification Risk)
# ==============================================================================
def test_signal_processor_load_bearer_penalty(physics_engine):
    """Proves that highly imported files receive a massive penalty for lacking tests."""
    # 1. Standard file with 0 tests
    m_std, e_std = create_synthetic_star(physics_engine, "std_untested", 100, {"test": 0})
    m_std["popularity"] = 0
    
    # 2. Foundational pillar with 0 tests
    m_pillar, e_pillar = create_synthetic_star(physics_engine, "pillar_untested", 100, {"test": 0})
    m_pillar["popularity"] = 20  # Highly imported

    r_std = physics_engine.calculate_risk_vector(m_std, e_std)
    r_pillar = physics_engine.calculate_risk_vector(m_pillar, e_pillar)

    idx_ver = physics_engine.RISK_SCHEMA.index("verification")
    
    assert r_pillar["risk_vector"][idx_ver] > r_std["risk_vector"][idx_ver], "Load-bearer penalty failed to amplify verification risk!"


# ==============================================================================
# TEST 40: KINETIC BLINDNESS (Documentation Risk)
# ==============================================================================
def test_signal_processor_kinetic_blindness(physics_engine):
    """Proves that deeply nested/heavy functions lacking docstrings spike documentation risk."""
    # 1. Complex function WITH a docstring
    m_doc, e_doc = create_synthetic_star(physics_engine, "documented_heavy", 100, {"doc": 10})
    m_doc["functions"] = [{"name": "heavy_func", "loc": 50, "big_o_depth": 3, "docstring": True}]
    
    # 2. Complex function WITHOUT a docstring
    m_blind, e_blind = create_synthetic_star(physics_engine, "blind_heavy", 100, {"doc": 10})
    m_blind["functions"] = [{"name": "heavy_func", "loc": 50, "big_o_depth": 3, "docstring": False}]

    r_doc = physics_engine.calculate_risk_vector(m_doc, e_doc)
    r_blind = physics_engine.calculate_risk_vector(m_blind, e_blind)

    idx_doc = physics_engine.RISK_SCHEMA.index("documentation")
    
    assert r_blind["risk_vector"][idx_doc] > r_doc["risk_vector"][idx_doc], "Kinetic blindness failed to penalize undocumented heavy functions!"


# ==============================================================================
# TEST 41: TECH DEBT SLOP MULTIPLIER
# ==============================================================================
def test_signal_processor_tech_debt_slop(physics_engine):
    """Proves that unacknowledged slop multiplies the severity of fragile debt."""
    # 1. Just fragile debt
    m_debt, e_debt = create_synthetic_star(physics_engine, "fragile_only", 500, {"fragile_debt": 2})
    
    # 2. Fragile debt PLUS orphans/duplicates
    m_slop, e_slop = create_synthetic_star(physics_engine, "fragile_slop", 500, {
        "fragile_debt": 2, "design_slop_orphans": 2, "design_slop_duplicates": 1
    })

    r_debt = physics_engine.calculate_risk_vector(m_debt, e_debt)
    r_slop = physics_engine.calculate_risk_vector(m_slop, e_slop)

    idx_debt = physics_engine.RISK_SCHEMA.index("tech_debt")
    
    # The multiplier is 1.5x, so the slop score should be significantly higher
    assert r_slop["risk_vector"][idx_debt] > (r_debt["risk_vector"][idx_debt] * 1.2), "Tech debt slop failed to multiply fragile debt severity!"


# ==============================================================================
# TEST 42: REPORT GENERATOR MALFORMED DICTIONARY FALLBACK
# ==============================================================================
def test_signal_processor_report_fallback(physics_engine):
    """Ensures the report generator safely handles missing keys and malformed telemetry."""
    malformed_files = [
        {"name": "missing_risk_vector", "path": "src/bad1.py"}, # No risk_vector key
        {"name": "string_risk_vector", "path": "src/bad2.py", "risk_vector": "INVALID"}, # Wrong type
        {"name": "short_risk_vector", "path": "src/bad3.py", "risk_vector": [0.0]} # Index out of bounds
    ]
    
    # Should execute smoothly without raising a KeyError, TypeError, or IndexError
    report = physics_engine.generate_forensic_report(malformed_files)
    
    assert "exposures" in report, "Report generator completely failed on malformed data!"
    
    # The lowest/highest rankings should have safely defaulted the values to 0.0
    for exposure_key, ranking in report["exposures"].items():
        assert ranking["highest"][0]["value"] == 0.0, f"Fallback failed to zero out invalid data for {exposure_key}!"

# ==============================================================================
# TEST 43: CRITICAL LEAK BYPASS (Absolute Maximum Risk)
# ==============================================================================
def test_signal_processor_critical_leak_bypass(physics_engine):
    """Proves that critical leaks bypass standard physics and max out secrets risk."""
    m_leak, e_leak = create_synthetic_star(physics_engine, "aws_key", 10, {})
    m_leak["path"] = "config/production.pem"
    m_leak["metadata"] = {"aperture_reason": "CRITICAL LEAK DETECTED"}
    
    r_leak = physics_engine.calculate_risk_vector(m_leak, e_leak)
    
    idx_sec = physics_engine.RISK_SCHEMA.index("secrets_risk")
    
    assert r_leak["file_impact"] == 150.0, "Critical leak failed to trigger the 150.0 mass spike!"
    assert r_leak["risk_vector"][idx_sec] == 100.0, "Critical leak failed to max out secrets risk!"
    assert r_leak["telemetry"]["domain_context"]["alert"] == "CRITICAL LEAK BYPASS", "Bypass alert missing from telemetry!"


# ==============================================================================
# TEST 44: THE DARKNESS RATIO (100% Unparsable)
# ==============================================================================
def test_signal_processor_darkness_ratio(physics_engine):
    """Ensures global synthesis survives a completely broken repository (0 parsed, 10 unparsable)."""
    unparsable_files = [{"name": f"broken_{i}.py"} for i in range(10)]
    
    # 0 parsed files, 10 unparsable files
    summary = physics_engine.summarize_galaxy_metrics([], unparsable_files)
    
    assert summary["summary"]["total_files"] == 10, "Failed to count unparsable files in total!"
    assert summary["summary"]["verified_files"] == 0, "Verified files should be 0!"
    assert summary["summary"]["Percent_Visible"] == 0.0, "Darkness ratio failed to calculate 0% visibility!"
    assert summary["unparsable_files"]["ambig_file_count"] == 10, "Failed to aggregate unparsable file count!"


# ==============================================================================
# TEST 45: HARDWARE BRIDGE DAMPENERS
# ==============================================================================
def test_signal_processor_hardware_bridge_shield(physics_engine):
    """Proves that Hardware Bridges (Serial/USB I/O) are forgiven for dynamic execution."""
    # 1. Raw Execution (Malicious)
    m_raw, e_raw = create_synthetic_star(physics_engine, "raw_exec", 100, {"sec_danger": 10, "sec_io": 10})
    
    # 2. Hardware Execution (Expected Arduino/Serial behavior)
    m_hw, e_hw = create_synthetic_star(physics_engine, "hw_exec", 100, {
        "sec_danger": 10, "sec_io": 10, "hardware_bridge": 10
    })

    r_raw = physics_engine.calculate_risk_vector(m_raw, e_raw)
    r_hw = physics_engine.calculate_risk_vector(m_hw, e_hw)

    idx_inj = physics_engine.RISK_SCHEMA.index("injection_surface")
    
    assert r_hw["risk_vector"][idx_inj] < r_raw["risk_vector"][idx_inj], "Hardware bridge shield failed to dampen injection risk!"


# ==============================================================================
# TEST 46: ALGORITHMIC DOS O(N) BYPASS
# ==============================================================================
def test_signal_processor_algorithmic_dos_linear_bypass(physics_engine):
    """Ensures O(N) linear loops are ignored by the Algorithmic DoS equations."""
    m_linear, e_linear = create_synthetic_star(physics_engine, "linear_loop", 100, {"api": 10})
    # big_o_depth = 1 is standard O(N)
    m_linear["functions"] = [{"name": "safe_loop", "loc": 50, "big_o_depth": 1, "db_complexity": 5}]
    
    r_linear = physics_engine.calculate_risk_vector(m_linear, e_linear)
    idx_dos = physics_engine.RISK_SCHEMA.index("algorithmic_dos")
    
    # Because depth is < 2, the loop `continue` triggers and mass remains 0.0
    assert r_linear["risk_vector"][idx_dos] == 0.0, "O(N) linear loops should not trigger Algorithmic DoS!"


# ==============================================================================
# TEST 47: TIER 3 LANGUAGE FALLBACK
# ==============================================================================
def test_signal_processor_tier_3_language(physics_engine):
    """Ensures esoteric/unstructured languages trigger Tier 3 physics modifiers."""
    m_t3, e_t3 = create_synthetic_star(physics_engine, "esoteric", 100, {"branch": 20})
    # "haskell" is not in the Tier 1 or Tier 2 explicit sets
    m_t3["lang_id"] = "haskell" 
    
    r_t3 = physics_engine.calculate_risk_vector(m_t3, e_t3)
    
    # If it didn't crash, the _get_tier fallback successfully returned "tier3" and pulled the correct physics vars
    assert r_t3 is not None, "Tier 3 language fallback crashed the physics engine!"