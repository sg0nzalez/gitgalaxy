import pytest
from unittest.mock import patch

# Adjust this import to match your project structure
from gitgalaxy.physics.spectral_auditor import SpectralAuditor

# ==============================================================================
# MOCK HARDWARE CALIBRATION
# ==============================================================================
# We provide mock language definitions so the auditor knows which languages 
# have active logic sensors (preventing them from passing through the Inert Gate).

MOCK_LANG_DEFS = {
    "cpp": {
        "rules": {"branch": 1, "args": 1, "linear": 1, "pointers": 1, "memory_alloc": 1}
    },
    "python": {
        "rules": {"branch": 1, "args": 1, "linear": 1}
    }
}

@pytest.fixture
def auditor():
    """Initializes the Spectral Auditor with controlled definitions."""
    return SpectralAuditor(lang_defs=MOCK_LANG_DEFS)

# ==============================================================================
# TEST 1: THE CONSENSUS ENGINE (Heuristic Loop-Back)
# ==============================================================================
def test_auditor_consensus_engine(auditor):
    """
    Proves that the engine uses the ecosystem's confident files to rescue 
    and reclassify ambiguous/unresolved files with the same extension.
    """
    files = [
        # 4 Confident Core files
        {"path": "a.cpp", "lang_id": "cpp", "telemetry": {"identity_lock_tier": 1}},
        {"path": "b.cpp", "lang_id": "cpp", "telemetry": {"identity_lock_tier": 1}},
        {"path": "c.cpp", "lang_id": "cpp", "telemetry": {"identity_lock_tier": 1}},
        {"path": "d.cpp", "lang_id": "cpp", "telemetry": {"identity_lock_tier": 1}},
        # 1 Ambiguous File (Tier 4 / Unknown)
        {"path": "mystery.cpp", "name": "mystery.cpp", "lang_id": "unknown", "telemetry": {"identity_lock_tier": 4}}
    ]
    
    # We must patch the 50/0 and Orphan guard so they don't interfere with this specific test
    with patch.object(SpectralAuditor, '_is_highly_blended', return_value=False):
        verified, unparsable = auditor.audit(files)
        
    assert len(verified) == 5, "Consensus Engine failed to rescue the ambiguous file!"
    
    mystery_file = next((f for f in verified if f["path"] == "mystery.cpp"), None)
    assert mystery_file is not None
    assert mystery_file["lang_id"] == "cpp", "Failed to inherit the ecosystem consensus!"
    assert mystery_file["telemetry"]["identity_lock_tier"] == 2, "Failed to elevate the lock tier!"

# ==============================================================================
# TEST 2: THE 50/0 LAW (Data Dump Guard)
# ==============================================================================
def test_auditor_50_zero_law(auditor):
    """Proves that a massive file with 0 structural logic is relegated to Dark Matter."""
    files = [
        # Give it a strong lock tier so it bypasses Consensus and hits the Audit phase
        {
            "path": "data_dump.cpp", "name": "data_dump.cpp", "lang_id": "cpp",
            "coding_loc": 150, # > 50
            "equations": {"branch": 0, "linear": 0}, # 0 signals
            "telemetry": {"identity_lock_tier": 1}
        }
    ]
    
    verified, unparsable = auditor.audit(files)
    
    assert len(verified) == 0
    assert len(unparsable) == 1
    assert "50/0 Law" in unparsable[0]["reason"], "Failed to trigger the 50/0 Law!"

# ==============================================================================
# TEST 2: THE 50/0 LAW (Data Dump Guard)
# ==============================================================================
def test_auditor_50_zero_law(auditor):
    """Proves that a massive file with 0 structural logic is relegated to Dark Matter."""
    files = [
        {
            "path": "data_dump.cpp", "name": "data_dump.cpp", "lang_id": "cpp",
            "coding_loc": 150,
            "equations": {"branch": 0, "linear": 0},
            "telemetry": {"identity_lock_tier": 0} # <--- CHANGE TO 0 (Bypass Orphan Guard)
        }
    ]
    
    verified, unparsable = auditor.audit(files)
    
    assert len(verified) == 0
    assert len(unparsable) == 1
    assert "50/0 Law" in unparsable[0]["reason"], "Failed to trigger the 50/0 Law!"

# ==============================================================================
# TEST 3: THE SUPERNOVA GUARD (Impossible Density)
# ==============================================================================
def test_auditor_supernova_guard(auditor):
    """Proves that a file with >3.0 signals per line is relegated as obscured debris."""
    files = [
        {
            "path": "packed_logic.cpp", "name": "packed_logic.cpp", "lang_id": "cpp",
            "coding_loc": 40,
            "equations": {"branch": 200, "linear": 100},
            "telemetry": {"identity_lock_tier": 0} # <--- CHANGE TO 0 (Bypass Orphan Guard)
        }
    ]
    
    verified, unparsable = auditor.audit(files)
    
    assert len(verified) == 0
    assert len(unparsable) == 1
    assert "Supernova Guard" in unparsable[0]["reason"], "Failed to trigger the Supernova Guard!"

# ==============================================================================
# TEST 4: THE QUARANTINE GUARD (Threat Override)
# ==============================================================================
def test_auditor_quarantine_guard(auditor):
    """
    Proves that a file failing the 50/0 Law is forcefully saved onto the map
    if it contains an active security signature.
    """
    files = [
        {
            "path": "malware.cpp", "name": "malware.cpp", "lang_id": "cpp",
            "coding_loc": 100, 
            "equations": {"sec_danger": 1}, 
            "telemetry": {"identity_lock_tier": 0} # <--- Bypasses the Orphan Guard
        }
    ]
    
    verified, unparsable = auditor.audit(files)
    
    assert len(verified) == 1, "Quarantine Guard failed to save the malicious file!"
    assert len(unparsable) == 0
    assert verified[0].get("is_quarantined") is True, "Failed to inject the quarantine flag!"

# ==============================================================================
# TEST 5: THE ORPHAN GUARD (Hallucination Stripping)
# ==============================================================================
def test_auditor_orphan_guard(auditor):
    """
    Proves that a tiny population (1 file) with a weak confidence tier gets 
    its hallucinated language stripped and reverted to plaintext.
    """
    files = [
        {
            "path": "weird_file.python", "name": "weird_file.python", "lang_id": "python",
            "coding_loc": 10,
            "equations": {"branch": 5},
            "telemetry": {"identity_lock_tier": 3} # <--- CHANGE TO 3 (Survives Gate 0, Dies to Orphan Guard)
        }
    ]
    
    with patch.object(auditor, '_is_highly_blended', return_value=False):
        verified, unparsable = auditor.audit(files)
        
    assert len(verified) == 1
    assert verified[0]["lang_id"] == "plaintext", "Orphan Guard failed to strip the hallucinated language!"
    assert "Orphan Guard Fallback" in verified[0]["telemetry"]["identity_source_proof"]