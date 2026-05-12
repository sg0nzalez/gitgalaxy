# IMPORTANT: Adjust this path to match exactly where your file is located
from gitgalaxy.tools.ai_guardrails.dev_agent_firewall import DevAgentFirewall

# ==============================================================================
# TEST 1: The Context Window Shredder (Black Hole Detection)
# ==============================================================================
def test_black_hole_detection():
    """
    Proves that files exceeding 8k tokens with O(N^3) or worse complexity
    are correctly flagged as Context Window Shredders.
    """
    firewall = DevAgentFirewall()
    
    mock_files = [{
        "token_mass": 8500,     # ☢️ Exceeds 8k limit
        "max_big_o": 3,         # ☢️ High algorithmic complexity
        "telemetry": {},
        "risk_vector": []
    }]
    
    result = firewall.evaluate_ecosystem(mock_files)
    guardrails = result[0]["telemetry"]["ai_guardrails"]
    
    assert guardrails["is_agentic_black_hole"] is True, "Failed to detect the Agentic Black Hole!"
    assert any("Black Hole detected" in warning for warning in guardrails["warnings"])

# ==============================================================================
# TEST 2: The HITL Mandate (Blast Radius + Risk Debt)
# ==============================================================================
def test_hitl_mandate_detection():
    """
    Proves that high PageRank (blast radius) combined with severe risk debt 
    mandates a Human-in-the-Loop constraint.
    """
    firewall = DevAgentFirewall()
    
    mock_files = [{
        "token_mass": 1000,
        "max_big_o": 1,
        "risk_vector": [100, 50, 60], # ☢️ Sum = 210 (> 200 threshold)
        "telemetry": {
            "network_metrics": {
                "normalized_blast_radius": 1.5 # ☢️ > 1.0 threshold
            }
        }
    }]
    
    result = firewall.evaluate_ecosystem(mock_files)
    guardrails = result[0]["telemetry"]["ai_guardrails"]
    
    assert guardrails["requires_hitl"] is True, "Failed to enforce the HITL Mandate!"
    assert any("Human-in-the-Loop required" in warning for warning in guardrails["warnings"])

# ==============================================================================
# TEST 3: The Hallucination Zone (Metaprogramming + Low Docs)
# ==============================================================================
def test_hallucination_zone_detection():
    """
    Proves that high dynamic execution (heat triggers) and poor documentation
    triggers the Hallucination Zone warning.
    """
    firewall = DevAgentFirewall()
    
    mock_files = [{
        "telemetry": {
            "heat_triggers": 3,   # ☢️ > 2 dynamic execution triggers
            "doc_density": 0.15   # ☢️ < 0.20 density
        }
    }]
    
    result = firewall.evaluate_ecosystem(mock_files)
    guardrails = result[0]["telemetry"]["ai_guardrails"]
    
    assert guardrails["hallucination_zone"] is True, "Failed to detect the Hallucination Zone!"
    assert any("Hallucination Zone" in warning for warning in guardrails["warnings"])

# ==============================================================================
# TEST 4: The Silent Mutation Risk (Flux + Blast + No Tests)
# ==============================================================================
def test_silent_mutation_risk_detection():
    """
    Proves that files with high state flux, high inbound dependencies, and 
    zero test coverage are flagged as a Silent Mutation Risk.
    """
    firewall = DevAgentFirewall()
    
    mock_files = [{
        "telemetry": {
            "state_flux": 55,     # ☢️ > 50 flux
            "has_tests": False,   # ☢️ Zero test coverage
            "network_metrics": {
                "in_degree": 6    # ☢️ > 5 dependencies rely on this
            }
        }
    }]
    
    result = firewall.evaluate_ecosystem(mock_files)
    guardrails = result[0]["telemetry"]["ai_guardrails"]
    
    assert guardrails.get("silent_mutation_risk") is True, "Failed to detect Silent Mutation Risk!"
    assert any("Silent Mutation Risk" in warning for warning in guardrails["warnings"])

# ==============================================================================
# TEST 5: The Clean Baseline (False-Positive Guard)
# ==============================================================================
def test_safe_agentic_baseline():
    """
    Proves that a well-documented, well-tested, simple file passes the firewall
    without triggering any agentic guardrails.
    """
    firewall = DevAgentFirewall()
    
    mock_files = [{
        "token_mass": 2000,       # ✅ Safe size
        "max_big_o": 1,           # ✅ Simple O(N) logic
        "risk_vector": [10, 5],   # ✅ Low risk debt (15)
        "telemetry": {
            "heat_triggers": 0,   # ✅ No dynamic execution
            "doc_density": 0.85,  # ✅ Highly documented
            "state_flux": 10,     # ✅ Low flux
            "has_tests": True,    # ✅ Safely tested
            "network_metrics": {
                "normalized_blast_radius": 0.5, # ✅ Low blast radius
                "in_degree": 1                  # ✅ Low dependencies
            }
        }
    }]
    
    result = firewall.evaluate_ecosystem(mock_files)
    guardrails = result[0]["telemetry"]["ai_guardrails"]
    
    # Assert absolutely NO flags were triggered
    assert guardrails["is_agentic_black_hole"] is False
    assert guardrails["requires_hitl"] is False
    assert guardrails["hallucination_zone"] is False
    assert guardrails.get("silent_mutation_risk", False) is False
    assert len(guardrails["warnings"]) == 0, "False positive triggered on a safe file!"