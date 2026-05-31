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
    
    # 2. API DoS Bomb: O(N^3) + DB Complexity + Exposed to API & IO
    m_bomb, e_bomb = create_synthetic_star(physics_engine, "exposed_bomb", 100, {"api": 10})
    m_bomb["popularity"] = 5
    m_bomb["functions"] = [{"name": "dos_bomb", "loc": 50, "big_o_depth": 3, "db_complexity": 10, "hit_vector": {"api": 5, "io": 5, "flux": 5}}]
    
    # 3. Guarded DoS Bomb: Same as above but mitigated by safety bailouts
    m_guard, e_guard = create_synthetic_star(physics_engine, "guarded_bomb", 100, {"api": 10})
    m_guard["popularity"] = 5
    m_guard["functions"] = [{"name": "safe_bomb", "loc": 50, "big_o_depth": 3, "db_complexity": 10, "hit_vector": {"api": 5, "io": 5, "flux": 5, "safety": 1, "bailout_hits": 2}}]

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
