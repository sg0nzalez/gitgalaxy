import pytest
import math
from unittest.mock import patch

# Adjust this import to match your project structure
from gitgalaxy.physics.signal_processor import SignalProcessor

# ==============================================================================
# MOCK HARDWARE CALIBRATION
# ==============================================================================
# We mock the global schemas so the math engine runs deterministically without 
# requiring the actual standards files to be loaded.

MOCK_SIGNAL_SCHEMA = ["branch", "flux", "danger", "doc", "test"]
MOCK_RISK_SCHEMA = [
    "cognitive_load", "safety_score", "tech_debt", "verification", 
    "api_exposure", "concurrency", "state_flux", "graveyard", 
    "spec_match", "stability", "churn", "documentation", "civil_war",
    "obscured_payload", "logic_bomb", "injection_surface", "memory_corruption", "secrets_risk"
]

@pytest.fixture
def physics_engine():
    """Initializes the Signal Processor with a controlled mathematical environment."""
    with patch('gitgalaxy.physics.signal_processor.config') as mock_config:
        mock_config.RECORDING_SCHEMAS = {
            "SIGNAL_SCHEMA": MOCK_SIGNAL_SCHEMA,
            "RISK_SCHEMA": MOCK_RISK_SCHEMA
        }
        mock_config.PHYSICS_CONSTANTS = {
            "WEIGHT_RISK": 2.5, "WEIGHT_DEFENSE": 1.0,
            "TIER_VARS": {
                "tier1": {"fc": 1.0, "irc": 0}, 
                "tier2": {"fc": 0.85, "irc": 2}, 
                "tier3": {"fc": 0.60, "irc": 5}
            }
        }
        mock_config.RISK_EQUATION_TUNING = {}
        mock_config.PHYSICS_ASSET_MASKS = {
            "DOCUMENTATION_LANGUAGES": {"markdown", "plaintext", "rst", "text"}
        }
        
        # ---> THE FIX: Add these so they evaluate as empty dicts, not MagicMocks!
        mock_config.LANGUAGE_SECURITY_PROFILES = {}
        mock_config.PATH_MODIFIERS = {}
        mock_config.STATIC_ARCHETYPES = {}
        
        # Re-initialize so it picks up the patched config
        sp = SignalProcessor()
        # Force the schemas onto the instance
        sp.SIGNAL_SCHEMA = MOCK_SIGNAL_SCHEMA
        sp.RISK_SCHEMA = MOCK_RISK_SCHEMA
        return sp

# ==============================================================================
# TEST 1: ZERO-STATE RESILIENCY (Divide by Zero Protection)
# ==============================================================================
def test_processor_zero_state_resiliency(physics_engine):
    """
    Proves that an entirely empty file (0 LOC, 0 signals) does not crash the 
    engine with a ZeroDivisionError, and returns safe baseline metrics.
    """
    meta = {
        "coding_loc": 0, 
        "lang_id": "python",
        "path": "empty.py"
    }
    equations = {}
    
    # If it throws ZeroDivisionError, this will fail
    result = physics_engine.calculate_risk_vector(meta, equations)
    
    assert len(result["risk_vector"]) == len(MOCK_RISK_SCHEMA), "Failed to generate complete risk schema!"
    assert result["file_impact"] > 0, "Mass cannot be 0. Empty files still take up disk space."

# ==============================================================================
# TEST 2: SIGMOID OVERFLOW CLAMPING (The 100.0 Ceiling)
# ==============================================================================
def test_processor_sigmoid_overflow_clamping(physics_engine):
    """
    Proves that mathematically absurd densities (e.g. minified logic bombs) 
    trigger the OverflowError rescue block and clamp strictly to 100.0.
    """
    meta = {
        "coding_loc": 20,
        "lang_id": "javascript",
        "path": "malicious.min.js"
    }
    # 50,000 branches crammed onto 1 line of code
    equations = {
        "branch": 50000,
        "flux": 50000,
        "danger": 50000,
        "sec_danger": 50000
    }
    
    result = physics_engine.calculate_risk_vector(meta, equations)
    
    # Ensure no metric exceeded 100.0
    for idx, risk_score in enumerate(result["risk_vector"]):
        assert risk_score <= 100.0, f"Risk metric at index {idx} breached the 100.0 ceiling (Score: {risk_score})!"
        
    # Cognitive load should definitely be maxed out at 100.0
    cog_idx = MOCK_RISK_SCHEMA.index("cognitive_load")
    assert result["risk_vector"][cog_idx] == 100.0, "Failed to clamp extreme density to 100.0!"

# ==============================================================================
# TEST 3: THE INERT MASS BYPASS
# ==============================================================================
def test_processor_documentation_bypass(physics_engine):
    """
    Proves that Documentation files skip the logic engine, zeroing out their 
    logic/entropy risks while still preserving their physical mass.
    """
    meta = {
        "coding_loc": 500,
        "total_loc": 500,
        "lang_id": "markdown",
        "path": "README.md",
        "authors": {"joe": 10, "bob": 5}
    }
    
    result = physics_engine.calculate_risk_vector(meta, {})
    
    doc_idx = MOCK_RISK_SCHEMA.index("documentation")
    
    # 1. Logic risks must be 0
    assert result["risk_vector"][doc_idx] == 0.0, "Documentation file flagged with documentation risk!"
    
    # 2. Entropy must be 0 (Literature doesn't have execution entropy)
    assert result["telemetry"]["ownership_entropy"] == 0.0, "Literature flagged with execution entropy!"
    
    # 3. File Impact (Mass) must still exist
    assert result["file_impact"] >= 10.0, "Failed to calculate physical mass of the documentation file!"

# ==============================================================================
# TEST 4: LOGARITHMIC TEMPORAL NORMALIZATION (Pass 2)
# ==============================================================================
def test_processor_temporal_normalization(physics_engine):
    """
    Proves the 2nd Pass Normalization successfully maps the most volatile file 
    to 100.0 and logarithmically curves the rest.
    """
    # Create 3 mock files with varying raw churn
    files = [
        {"telemetry": {"raw_churn_freq": 0.0}, "risk_vector": [0.0] * len(MOCK_RISK_SCHEMA)},
        {"telemetry": {"raw_churn_freq": 10.0}, "risk_vector": [0.0] * len(MOCK_RISK_SCHEMA)},
        {"telemetry": {"raw_churn_freq": 1000.0}, "risk_vector": [0.0] * len(MOCK_RISK_SCHEMA)} # The Volcano
    ]
    
    physics_engine._normalize_temporal_metrics(files)
    churn_idx = MOCK_RISK_SCHEMA.index("churn")
    
    # File 3 is the global maximum, it must equal exactly 100.0
    assert files[2]["risk_vector"][churn_idx] == 100.0, "Global maximum churn failed to normalize to 100.0!"
    
    # File 1 is dead silent, it must equal 0.0
    assert files[0]["risk_vector"][churn_idx] == 0.0, "Zero churn failed to normalize to 0.0!"
    
    # File 2 is intermediate. It should be > 0 and < 100.
    assert 0.0 < files[1]["risk_vector"][churn_idx] < 100.0, "Logarithmic curve failed on intermediate file!"