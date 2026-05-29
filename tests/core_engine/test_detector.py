import pytest
import re
import math
from unittest.mock import patch

from gitgalaxy.core.detector import LogicSplicer, Cartographer

# ==============================================================================
# MOCK HARDWARE CALIBRATION
# ==============================================================================
# We mock the definitions so the pipeline operates deterministically without
# relying on external standards files.

MOCK_LANG_DEFS = {
    "python": {
        "lexical_family": "pure_hash",
        "rules": {
            "func_start": re.compile(r"^[ \t]*def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(", re.M),
            "branch": re.compile(r"\b(if|elif|for|while)\b"),
            "linear": re.compile(r"\b(print|return|assign)\b"),
            "ownership": re.compile(r"#\s*Architect:\s*(.*)"),
            "_meta_purpose_line": re.compile(r"^Purpose:\s*(.*)"),
        },
    },
    "assembly": {
        "lexical_family": "singular",
        "rules": {
            "func_start": re.compile(r"^([a-zA-Z0-9_]+):", re.M),
            "branch": re.compile(r"\b(JNE|JEQ|CALL)\b"),
            "linear": re.compile(r"\b(MOV|PUSH|POP)\b"),
        },
    },
    "c": {
        "lexical_family": "std_c",
        "rules": {
            "func_start": re.compile(r"^[ \t]*\w+\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^)]*\)\s*\{", re.M),
            "memory_scraping": re.compile(r"\b(memcpy|VirtualRead)\b"),
            "exfiltration_camouflage": re.compile(r"\b(send|socket)\b"),
            "danger": re.compile(r"\b(strcpy|gets)\b"),
            "safety": re.compile(r"\b(strncpy|fgets)\b"),
            "sec_danger": re.compile(r"system"),
            "sec_io": re.compile(r"request_get"),
            "concurrency": re.compile(r"std::thread"),
            "flux": re.compile(r"shared_state"),
            "sync_locks": re.compile(r"mutex_lock"),
            "memory_alloc": re.compile(r"malloc"),
            "cleanup": re.compile(r"free"),
        },
    },
    "sql": {
        "lexical_family": "singular",
        "rules": {"io": re.compile(r"\b(SELECT|INSERT|UPDATE|DELETE)\b", re.I)},
    },
    "shell": {
        "lexical_family": "singular",
        "rules": {
            "branch": re.compile(r"\b(if|case|for|while)\b"),
            "linear": re.compile(r"\b(echo|export|source)\b"),
        },
    },
    "ruby": {
        "lexical_family": "pure_hash",
        "rules": {
            "branch": re.compile(r"(?<![:.])\b(if|unless|case|while|until)\b(?!:)"),
            "linear": re.compile(r"(?<![:.])\b(puts|require|include)\b(?!:)"),
        },
    },
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
        "    for i in range(10):\n"  # Indent Level 1
        "        if i == 5:\n"  # Indent Level 2
        "            print(i)\n"  # Indent Level 3 (Deepest)
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
    code = "def parse_blob():\n" f"    payload = '{massive_blob}'\n" "    return payload\n"

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
    code = "SELECT * FROM users\n" "WHERE active = 1;\n" "\n" "UPDATE audit_log\n" "SET viewed = 1\n" "WHERE id = 55;\n"

    # Mode E requires specific handshake routing inside the engine
    with patch("gitgalaxy.core.detector.SemanticScopeRegistry.get_mode", return_value="mode_e"):
        result = splicer.splice(code, "")

        assert len(result["functions"]) >= 2, "Mode E failed to cleave the file into distinct blocks!"

        func_names = [f["name"] for f in result["functions"]]
        assert any("SELECT" in name for name in func_names), "Failed to ignite the SELECT block!"
        assert any("UPDATE" in name for name in func_names), "Failed to ignite the UPDATE block!"


def test_detector_class_extraction_and_lcom():
    """
    Proves the engine accurately bounds OOP entities, links internal methods,
    and calculates LCOM/State Entanglement without full AST parsing.
    """
    splicer = LogicSplicer("python", MOCK_LANG_DEFS)
    code = (
        "class UserManager:\n"
        "    def __init__(self):\n"
        "        self.users = []\n"  # Hits 'flux' (mutation)
        "    def add_user(self, user, role):\n"  # 2 args
        "        self.users.append(user)\n"  # Hits 'flux'
        "        print(role)\n"
    )

    # Mocking a flux rule for testing state entanglement
    MOCK_LANG_DEFS["python"]["rules"]["flux"] = re.compile(r"\b(append|users\s*=)\b")

    result = splicer.splice(code, "")

    assert len(result["classes"]) == 1, "Failed to extract the class boundary!"

    cls = result["classes"][0]
    assert cls["name"] == "UserManager"
    assert cls["method_count"] == 2, "Failed to spatially link methods to the parent class!"
    assert cls["lcom_score"] < 100.0, "LCOM calculation failed or defaulted to 100!"
    assert cls["state_entanglement"] > 0.0, "State entanglement failed to register mutations!"


def test_detector_atomic_literal_shield():
    """
    Proves the _apply_literal_shield safely blanks complex strings and heredocs
    without destroying physical line geometries.
    """
    splicer = LogicSplicer("ruby", MOCK_LANG_DEFS)
    code = (
        "def query_database\n"
        "  sql = <<-SQL\n"
        "    SELECT * FROM users\n"
        "    WHERE active = true;\n"
        "    def fake_function_inside_string\n"
        "  SQL\n"
        "end\n"
    )

    # Access the shield directly
    safe_code = splicer._apply_literal_shield(code, "ruby")

    assert "def fake_function_inside_string" not in safe_code, "Shield failed to mask heredoc contents!"
    assert safe_code.count("\n") == code.count("\n"), "Shield altered the physical line count!"


def test_detector_orphan_and_duplicate_logic():
    """
    Proves the engine accurately identifies uncalled (orphan) functions
    and duplicated function definitions within a single file.
    """
    splicer = LogicSplicer("python", MOCK_LANG_DEFS)
    code = (
        "def active_helper():\n"
        "    return True\n"
        "\n"
        "def forgotten_orphan():\n"
        "    pass\n"
        "\n"
        "def main_process():\n"
        "    if active_helper():\n"
        "        print('Running')\n"
    )

    result = splicer.splice(code, "")

    # active_helper is used, forgotten_orphan is not, main_process is the entry point
    orphans = [f["name"] for f in result["functions"] if f.get("usage_status") == 1]

    assert "forgotten_orphan" in orphans, "Failed to flag the unused function as an orphan!"
    assert "active_helper" not in orphans, "Falsely flagged an active function as an orphan!"


def test_detector_c_macro_dead_branch_shield():
    """
    Proves the Mode B Preprocessor Shield successfully blanks out dead
    #ifdef branches and multi-line macro continuations.
    """
    splicer = LogicSplicer("c", MOCK_LANG_DEFS)
    code = (
        "void system_init() {\n"
        "#if defined(DEBUG_MODE)\n"
        "    int fake_danger = strcpy(dest, src);\n"
        "#else\n"
        "    int safe_ops = strncpy(dest, src, 10);\n"
        "#endif\n"
        "}\n"
    )

    result = splicer.splice(code, "")

    # Because 'danger' is in the dead branch, it should be scrubbed by the preprocessor shield
    # before the regex engine even sees it.
    assert result["equations"]["danger"] == 0, "Failed to scrub dead preprocessor branches!"


# ==============================================================================
# TEST 5: MODE D (SEMANTIC HANDSHAKE STACK)
# ==============================================================================
def test_detector_mode_d_shell_handshake():
    """
    Proves Mode D correctly identifies scope boundaries using semantic keywords
    (if/fi, for/done) instead of braces, and prevents scope bleeding.
    """
    splicer = LogicSplicer("shell", MOCK_LANG_DEFS)
    code = (
        "function backup_db() {\n"
        "    if [ -f $FILE ]; then\n"
        "        echo 'File exists.'\n"
        "    fi\n"
        "    for i in 1 2 3; do\n"
        "        echo $i\n"
        "    done\n"
        "}\n"
    )

    result = splicer.splice(code, "")

    assert len(result["functions"]) == 1, "Failed to extract the shell function as a single block!"

    func = result["functions"][0]
    assert func["name"] == "backup_db"
    assert func["coding_loc"] >= 6, "Line counting failed inside the semantic block!"
    assert func["branch_count"] == 2, "Failed to register internal structural branches!"


def test_detector_mode_d_ruby_inline_modifier():
    """
    Proves the engine's Ruby inline modifier guard prevents trailing conditionals
    from artificially inflating the scope stack and swallowing the file.
    """
    splicer = LogicSplicer("ruby", MOCK_LANG_DEFS)
    code = (
        "def calculate_risk()\n"
        "    risk_exposure = 100 if user.is_admin?\n"
        "    return risk_exposure unless risk_exposure > 50\n"
        "end\n"
        "\n"
        "def secondary_process()\n"
        "    puts 'Processing'\n"
        "end\n"
    )

    result = splicer.splice(code, "")

    assert len(result["functions"]) == 2, "Inline modifiers corrupted the stack depth and swallowed the file!"

    names = [f["name"] for f in result["functions"]]
    assert "calculate_risk" in names
    assert "secondary_process" in names


# ==============================================================================
# TEST 6: MODE C (INDENTATION STRATIFICATION)
# ==============================================================================
def test_detector_mode_c_indentation():
    """
    Proves Mode C correctly tracks Python indentation to close scopes,
    preventing nested functions or trailing text from bleeding into the parent.
    """
    splicer = LogicSplicer("python", MOCK_LANG_DEFS)
    code = (
        "def parent_process():\n"
        "    print('Starting')\n"
        "    if True:\n"
        "        assign_val = 1\n"
        "\n"  # Blank lines should not break the scope
        "def adjacent_process():\n"
        "    return False\n"
    )

    result = splicer.splice(code, "")

    assert len(result["functions"]) == 2, "Mode C failed to separate Python functions by indentation!"

    parent = result["functions"][0]
    assert parent["name"] == "parent_process"
    assert parent["loc"] == 4, "Mode C failed to accurately count lines inside the indentation block!"


# ==============================================================================
# TEST 7: MODE A (GREEDY LABELS)
# ==============================================================================
def test_detector_mode_a_labels():
    """
    Proves Mode A correctly cleaves Assembly and COBOL blocks using greedy
    label matching until the next label or termination instruction.
    """
    splicer = LogicSplicer("assembly", MOCK_LANG_DEFS)
    code = (
        "INIT_SYSTEM:\n"
        "    MOV EAX, 1\n"
        "    PUSH EAX\n"
        "    CALL SETUP\n"
        "ERROR_HANDLER:\n"
        "    POP EAX\n"
        "    RET\n"
    )

    result = splicer.splice(code, "")

    assert len(result["functions"]) >= 2, "Mode A failed to slice Assembly labels!"

    func_names = [f["name"] for f in result["functions"]]
    assert "INIT_SYSTEM" in func_names
    assert "ERROR_HANDLER" in func_names


# ==============================================================================
# TEST 8: LEVEL 3 WIRING & FUNCTION CLASSIFICATION
# ==============================================================================
def test_detector_classification_and_wiring():
    """
    Proves the engine extracts outbound function calls (calls_out_to) for Level 3
    topology wiring and accurately classifies function types based on naming heuristics.
    """
    splicer = LogicSplicer("python", MOCK_LANG_DEFS)
    code = "def save_user_data(user_id):\n" "    validate_id(user_id)\n" "    db_insert(user_id)\n" "    return True\n"

    result = splicer.splice(code, "")
    func = result["functions"][0]

    assert "validate_id" in func["calls_out_to"], "Failed to extract Level 3 outbound calls!"
    assert "db_insert" in func["calls_out_to"], "Failed to extract Level 3 outbound calls!"
    assert func["type_id"] == "mutation", "Failed to classify 'save_user_data' as a mutation!"


# ==============================================================================
# TEST 9: GHOST TETHER & METADATA EXTRACTION
# ==============================================================================
def test_detector_ghost_tether_and_metadata():
    """
    Proves the engine correctly parses the decoupled comment stream to extract
    ownership/purpose, and successfully maps docstrings back to their physical functions.
    """
    splicer = LogicSplicer("python", MOCK_LANG_DEFS)
    code = (
        "def compute_hash():\n"
        "    '''\n"
        "    This is the internal docstring tethered to compute_hash.\n"
        "    '''\n"
        "    return True\n"
    )

    comment_stream = "# Architect: Ada Lovelace\n" "# Purpose: Handles core cryptographic operations.\n"

    # We must pass raw_content to allow the Ghost Tether to search coordinates
    result = splicer.splice(code, comment_stream, raw_content=code)

    # Check File Metadata
    assert result["metadata"]["ownership"] == "Ada Lovelace", "Failed to decode ownership from comment stream!"
    assert "cryptographic operations" in result["metadata"]["purpose"], "Failed to decode purpose from comment stream!"

    # Check Ghost Tether (Function-level docstring)
    func = result["functions"][0]
    assert (
        "internal docstring tethered" in func["docstring"]
    ), "Failed to tether the docstring to the physical function bounds!"


# ==============================================================================
# TEST 10: OOP & MACRO NAME EXTRACTOR SHIELDS
# ==============================================================================
def test_detector_cpp_objc_name_extraction():
    """
    Proves the _extract_name logic safely isolates overloaded C++ operators,
    C++ testing macros, and Objective-C method signatures without destroying them.
    """
    splicer = LogicSplicer("cpp", MOCK_LANG_DEFS)

    # Objective-C
    assert splicer._extract_name("- (void)initWithObjects:(NSArray *)objects {") == "initWithObjects"
    assert splicer._extract_name("+ (instancetype)sharedInstance;") == "sharedInstance"

    # C++ Operators
    assert splicer._extract_name("MyClass::operator<<(std::ostream& os)") == "operator<<"
    assert splicer._extract_name("operator bool() const") == "operator bool"
    assert splicer._extract_name("operator()()") == "operator()"

    # C++ Macros
    assert splicer._extract_name("BOOST_AUTO_TEST_CASE(MyTestName)") == "MyTestName"
    assert splicer._extract_name("TEST_F(MySuite, MyGTestName)") == "MySuite"


# ==============================================================================
# TEST 11: ADVANCED APPSEC SENSORS (PHASE 4)
# ==============================================================================
def test_detector_advanced_appsec_sensors():
    """
    Proves the Phase 4 spatial correlation matrix correctly calculates metrics
    for unmitigated Memory Leaks, Tainted RCE Injection, and Race Conditions.
    """
    splicer = LogicSplicer("c", MOCK_LANG_DEFS)
    code = (
        "void vulnerable_rce() { system(request_get()); }\n"
        "void race_condition() { std::thread t(worker); shared_state = 1; }\n"
        "void memory_leak() { malloc(100); }\n"
    )

    result = splicer.splice(code, "")
    eqs = result["equations"]
    mits = result["mitigation_telemetry"]

    # 1. RCE Weaponization: sec_danger spatially overlapping with sec_io
    assert eqs.get("sec_tainted_injection", 0) >= 1, "Failed to spatially correlate Tainted RCE Injection!"

    # 2. Race Conditions: concurrency overlapping with unlocked flux (multiplies by 5)
    assert eqs.get("concurrency", 0) >= 5, "Failed to detect and amplify the Race Condition penalty!"
    assert mits.get("amplified_race_conditions", 0) >= 1, "Failed to log the Race Condition telemetry!"

    # 3. Memory Leaks: unmitigated alloc
    assert eqs.get("memory_alloc", 0) >= 1, "Failed to flag the unmitigated Memory Leak!"


# ==============================================================================
# TEST 12: CATASTROPHIC FALLBACKS (HARDWARE GUILLOTINES)
# ==============================================================================
def test_detector_catastrophic_fallbacks():
    """
    Proves the engine gracefully zeroes out payloads on standard exceptions to prevent
    pool crashes, but explicitly raises TimeoutError to allow the Worker to kill the thread.
    """
    import pytest

    splicer = LogicSplicer("python", MOCK_LANG_DEFS)

    # 1. Standard Exception -> Returns zeroed Ghost Mass payload
    with patch.object(
        splicer,
        "_partition_segments",
        side_effect=ValueError("Catastrophic parsing failure"),
    ):
        result = splicer.splice("def foo(): pass", "# Architect: Joe")
        assert result["equations"] == {}, "Fallback did not return an empty equations dict!"
        assert result["logic_density"] == 0.0, "Fallback did not zero out logic density!"
        assert result["metadata"]["ownership"] == "Joe", "Fallback destroyed the Ghost Mass metadata!"

    # 2. TimeoutError -> Hardware Guillotine drops cleanly
    with patch.object(
        splicer,
        "_partition_segments",
        side_effect=TimeoutError("Hardware thread timeout exceeded"),
    ):
        with pytest.raises(TimeoutError):
            splicer.splice("def foo(): pass", "")


# ==============================================================================
# CARTOGRAPHER: 3D SPATIAL GEOMETRY & MAPPING
# ==============================================================================


@pytest.fixture
def cartographer():
    """Initializes the 3D mapping engine."""
    return Cartographer()


def test_cartographer_mass_extraction(cartographer):
    """Proves the engine extracts gravitational mass natively or via fallback telemetry."""
    # 1. Primary: Forensics Dictionary
    assert cartographer._get_mass({"forensics": {"structural_mass": 42.0}}) == 42.0

    # 2. Secondary: Processed File Impact
    assert cartographer._get_mass({"file_impact": 15.5}) == 15.5

    # 3. Fallback: Raw Function Impact
    assert cartographer._get_mass({"sum_fxn_impact": 7.0}) == 7.0


def test_cartographer_deterministic_jitter(cartographer):
    """
    Proves the pseudo-random jitter is perfectly deterministic based on the MD5 hash
    of the filename. This ensures the WebGPU map doesn't mutate on refresh.
    """
    val1 = cartographer._hash_jitter("auth_service", 100.0)
    val2 = cartographer._hash_jitter("auth_service", 100.0)
    val3 = cartographer._hash_jitter("database_service", 100.0)

    assert val1 == val2, "Jitter is not deterministic! The map will warp on reload."
    assert val1 != val3, "Jitter failed to differentiate distinct files!"
    assert -100.0 <= val1 <= 100.0, "Jitter violated its amplitude constraints!"


def test_cartographer_sectorization_and_monolith(cartographer):
    """
    Proves the engine correctly groups files into sector constellations by their
    parent directories, and traps root files in the __monolith__.
    """
    files = [
        {"path": "main.py", "file_impact": 10.0},
        {"path": "src/api.py", "file_impact": 20.0},
        {"path": "src/db.py", "file_impact": 30.0},
        {"path": "tests/e2e/test_auth.py", "file_impact": 5.0},
    ]

    mapped = cartographer.map_repository(files)

    # 1. Verify 3D coordinates were injected into every file
    assert all("pos_x" in f for f in mapped), "Missing X coordinates!"
    assert all("pos_y" in f for f in mapped), "Missing Y coordinates!"
    assert all("pos_z" in f for f in mapped), "Missing Z coordinates!"

    # 2. Verify Sector Assignments
    monolith = [f for f in mapped if f.get("directory_group") == "__monolith__"]
    src_group = [f for f in mapped if f.get("directory_group") == "src"]
    test_group = [f for f in mapped if f.get("directory_group") == "tests/e2e"]

    assert len(monolith) == 1, "Root file evaded the monolith!"
    assert len(src_group) == 2, "Failed to group sibling files into the same sector!"
    assert len(test_group) == 1, "Failed to handle nested directory sectors!"


def test_cartographer_ray_casting_collision_avoidance(cartographer):
    """
    Proves the angular spatial hashing engine prevents massive constellations
    from spawning inside each other (overlapping geometry).
    """
    # Create two astronomically massive stars in different sectors
    files = [
        {"path": "alpha_quadrant/core.py", "file_impact": 10000.0},
        {"path": "beta_quadrant/core.py", "file_impact": 10000.0},
    ]

    mapped = cartographer.map_repository(files)
    f1, f2 = mapped[0], mapped[1]

    # Calculate Euclidean distance between the two supermassive stars (X and Z plane)
    distance = math.hypot(f1["pos_x"] - f2["pos_x"], f1["pos_z"] - f2["pos_z"])

    # Calculate their physical radius footprints
    footprint = cartographer._calculate_orbit_footprint(10000.0)

    # Because of the step_factor (1.5x) in the math engine, the distance between them
    # MUST be significantly larger than a single footprint to prevent a visual crash.
    assert distance > footprint * 1.5, "Ray-Caster failed! Massive constellations are overlapping in 3D space."


# ==============================================================================
# TEST 13: THE PROSE & SINGULARITY BYPASS
# ==============================================================================
@pytest.mark.smoke
def test_detector_prose_and_empty_bypass():
    """Proves the engine gracefully aborts on Markdown, low confidence, or empty streams."""
    splicer = LogicSplicer("markdown", MOCK_LANG_DEFS)

    # 1. Prose/Confidence Bypass
    res_prose = splicer.splice("## Header", "comment", confidence=0.40)
    assert res_prose["logic_density"] == 0.0, "Prose bypass failed to abort on low confidence!"

    # 2. Empty Code Stream Bypass
    splicer_py = LogicSplicer("python", MOCK_LANG_DEFS)
    res_empty = splicer_py.splice("", "comment")
    assert res_empty["logic_density"] == 0.0, "Empty stream bypass failed to abort!"


# ==============================================================================
# TEST 14: FUNCTION TAXONOMY CLASSIFICATION
# ==============================================================================
def test_detector_function_classification():
    """Proves the engine accurately classifies function textures based on naming heuristics."""
    splicer = LogicSplicer("python", MOCK_LANG_DEFS)
    code = (
        "def handle_click_event():\n    pass\n"
        "def parse_raw_text():\n    pass\n"
        "def is_valid_user():\n    pass\n"
        "def test_identity():\n    pass\n"
        "def generate_uuid():\n    pass\n"
    )
    res = splicer.splice(code, "")

    types = {f["name"]: f["type_id"] for f in res["functions"]}
    assert types.get("handle_click_event") == "event", "Failed to classify 'handle' as event!"
    assert types.get("parse_raw_text") == "logic", "Failed to classify 'parse' as logic!"
    assert types.get("is_valid_user") == "check", "Failed to classify 'is_' as check!"
    assert types.get("test_identity") == "verification", "Failed to classify 'test' as verification!"
    assert types.get("generate_uuid") == "standard", "Failed to fallback to standard taxonomy!"


# ==============================================================================
# TEST 15: RUBY SHIELDS & MAKEFILE NAME EXTRACTION
# ==============================================================================
def test_detector_ruby_literals_and_makefile_extraction():
    """Proves Ruby % literals are shielded and Makefile variables are extracted correctly."""
    # 1. Ruby % literals
    splicer_rb = LogicSplicer("ruby", MOCK_LANG_DEFS)
    ruby_code = "def foo\n  x = %q{this is a string}\n  y = %W[a b c]\nend"
    safe_ruby = splicer_rb._apply_literal_shield(ruby_code, "ruby")
    assert "%q{" not in safe_ruby, "Failed to shield Ruby %q literal!"

    # 2. Makefile Name Extraction
    splicer_make = LogicSplicer("makefile", MOCK_LANG_DEFS)
    name = splicer_make._extract_name("$(TARGET):")
    assert name == "$(TARGET)", "Makefile shield failed to preserve $(...) syntax!"

    # 3. C-Style ARGS Shield
    splicer_c = LogicSplicer("c", MOCK_LANG_DEFS)
    c_name = splicer_c._extract_name("void my_func ARGS1(int x) {")
    assert c_name == "my_func", "C-Style ARGS macro shield failed!"


# ==============================================================================
# TEST 16: MISSING DEPENDENCY FALLBACKS
# ==============================================================================
@patch("gitgalaxy.core.detector.HAS_TIKTOKEN", False)
def test_detector_missing_tiktoken_fallback():
    """Proves the engine won't crash or poison datasets if tiktoken is missing."""
    splicer = LogicSplicer("python", MOCK_LANG_DEFS)
    res = splicer.splice("def foo(): pass", "")

    assert res["token_mass"] is None, "Fallback failed to return None for token mass!"
    assert res["financial_read_cost"] is None, "Fallback failed to neutralize financial cost!"
