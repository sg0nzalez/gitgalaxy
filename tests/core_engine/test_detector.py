import re
from unittest.mock import patch

# Adjust this import to match your project structure
from gitgalaxy.core.detector import LogicSplicer

# ==============================================================================
# MOCK HARDWARE CALIBRATION
# ==============================================================================
# We mock the definitions so the pipeline operates deterministically without 
# relying on external standards files.

MOCK_LANG_DEFS = {
    "python": {
        "lexical_family": "pure_hash",
        "rules": {
            "func_start": re.compile(r'^[ \t]*def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', re.M),
            "branch": re.compile(r'\b(if|elif|for|while)\b'),
            "linear": re.compile(r'\b(print|return|assign)\b')
        }
    },
    "c": {
        "lexical_family": "std_c",
        "rules": {
            "func_start": re.compile(r'^[ \t]*\w+\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^)]*\)\s*\{', re.M),
            "memory_scraping": re.compile(r'\b(memcpy|VirtualRead)\b'),
            "exfiltration_camouflage": re.compile(r'\b(send|socket)\b'),
            "danger": re.compile(r'\b(strcpy|gets)\b'),
            "safety": re.compile(r'\b(strncpy|fgets)\b')
        }
    },
    "sql": {
        "lexical_family": "singular",
        "rules": {
            "io": re.compile(r'\b(SELECT|INSERT|UPDATE|DELETE)\b', re.I)
        }
    }
}

# ==============================================================================
# TEST 1: ALGORITHMIC PHYSICS (Big-O & Recursion)
# ==============================================================================
def test_detector_big_o_and_recursion():
    """
    Proves the engine accurately calculates nesting depth based on indentation,
    and flags exponential O(2^N) recursion without building an AST.
    """
    splicer = LogicSplicer("python", MOCK_LANG_DEFS)
    code = (
        "def calculate_fibonacci(n):\n"
        "    if n <= 1:\n"
        "        return n\n"
        "    for i in range(10):\n"      # Indent Level 1
        "        if i == 5:\n"           # Indent Level 2
        "            print(i)\n"         # Indent Level 3 (Deepest)
        "    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)\n"
    )
    
    result = splicer.splice(code, "")
    assert len(result["functions"]) == 1
    
    func = result["functions"][0]
    assert func["name"] == "calculate_fibonacci"
    assert func["is_recursive"] is True, "Failed to flag recursive execution!"
    assert func["big_o_depth"] >= 3, "Failed to calculate Big-O nesting depth!"

# ==============================================================================
# TEST 2: SPATIAL THREAT CORRELATION (The AppSec Sensor)
# ==============================================================================
def test_detector_spatial_appsec_correlation():
    """
    Proves the Spatial Map correctly amplifies penalties when an attacker reads
    memory and sends it out to a socket within a 200-character blast radius.
    """
    splicer = LogicSplicer("c", MOCK_LANG_DEFS)
    code = (
        "void malicious_exfiltration_func() {\n"
        "    char buffer[100];\n"
        "    memcpy(buffer, secret_key, 100);  // Trigger: memory_scraping\n"
        "    send(socket, buffer, 100, 0);     // Trigger: exfiltration_camouflage\n"
        "}\n"
    )
    
    result = splicer.splice(code, "")
    
    # A single memory_scraping hit normally = 1.
    # The AppSec multiplier adds 100 if correlated. Total should be >= 100.
    assert result["equations"]["memory_scraping"] >= 100, "Spatial correlation failed to multiply the threat penalty!"
    assert result["mitigation_telemetry"]["amplified_leaks"] == 1, "Failed to log the active leak mitigation stat!"

def test_detector_silencer_region():
    """
    Proves the Spatial Map correctly neutralizes danger signals if a safety wrapper
    exists within the 500-character silencer radius.
    """
    splicer = LogicSplicer("c", MOCK_LANG_DEFS)
    code = (
        "void safe_wrapper() {\n"
        "    // Using strncpy for safety instead of strcpy\n"
        "    strncpy(dest, src, sizeof(dest));\n" 
        "}\n"
    )
    
    result = splicer.splice(code, "")
    # The raw string "strcpy" is inside "strncpy", so both trigger in a naive regex.
    # The spatial math should subtract the danger hit.
    assert result["equations"]["danger"] == 0, "Silencer region failed to dampen the danger signal!"
    assert result["mitigation_telemetry"]["mitigated_danger"] >= 1

# ==============================================================================
# TEST 3: THE ANTI-REDOS SHIELD
# ==============================================================================
def test_detector_anti_redos_line_limiter():
    """
    Proves that a catastrophic 2000+ character line (e.g., base64 blob) is safely
    blanked out to protect the multiprocessing pool, while preserving the LOC count.
    """
    splicer = LogicSplicer("python", MOCK_LANG_DEFS)
    
    # Generate a 2500 character string
    massive_blob = "A" * 2500 
    code = (
        "def parse_blob():\n"
        f"    payload = '{massive_blob}'\n"
        "    return payload\n"
    )
    
    # If the shield fails, the regex engine might hang. If it succeeds, it finishes instantly.
    result = splicer.splice(code, "")
    
    assert len(result["functions"]) == 1
    assert result["functions"][0]["name"] == "parse_blob"
    assert result["functions"][0]["coding_loc"] == 3, "Anti-ReDoS shield destroyed the physical line count!"

# ==============================================================================
# TEST 4: MODE E (TERMINATOR CLEAVING)
# ==============================================================================
def test_detector_terminator_cleaving():
    """
    Proves Mode E correctly chops SQL payloads by terminators (;) rather than 
    braces or indentation scopes.
    """
    splicer = LogicSplicer("sql", MOCK_LANG_DEFS)
    code = (
        "SELECT * FROM users\n"
        "WHERE active = 1;\n"
        "\n"
        "UPDATE audit_log\n"
        "SET viewed = 1\n"
        "WHERE id = 55;\n"
    )
    
    # Mode E requires specific handshake routing inside the engine
    with patch('gitgalaxy.core.detector.SemanticScopeRegistry.get_mode', return_value="mode_e"):
        result = splicer.splice(code, "")
        
        assert len(result["functions"]) >= 2, "Mode E failed to cleave the file into distinct blocks!"
        
        func_names = [f["name"] for f in result["functions"]]
        assert any("SELECT" in name for name in func_names), "Failed to ignite the SELECT block!"
        assert any("UPDATE" in name for name in func_names), "Failed to ignite the UPDATE block!"