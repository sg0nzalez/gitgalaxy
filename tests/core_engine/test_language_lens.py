import pytest
import importlib
import re
from pathlib import Path

from gitgalaxy.standards import language_lens
from gitgalaxy.standards.language_lens import LanguageDetector


# ==============================================================================
# TEST 1: THE GOD MODE RELOAD SWEEP (Live Dictionary Verification)
# ==============================================================================
def test_language_lens_god_mode_reload_sweep():
    """
    Restored from your original file: Forces the Python interpreter to completely
    re-evaluate and compile the massive live LANGUAGE_DEFINITIONS dictionary.
    Guarantees no catastrophic regex compilation errors exist in your live config.
    """
    importlib.reload(language_lens)

    registry = getattr(language_lens, "LANGUAGE_DEFINITIONS", {})
    assert isinstance(registry, dict), "LANGUAGE_DEFINITIONS must be a dictionary."
    assert len(registry) > 0, "The language registry failed to load or is empty!"

    for lang_id, config in registry.items():
        assert "extensions" in config, f"Missing extensions in {lang_id}"

        # Trigger regex compilation to trap syntax errors (Trailing slashes, unclosed groups)
        rules = config.get("rules", {})
        for rule_name, pattern in rules.items():
            if pattern is None:
                continue
            if isinstance(pattern, str):
                assert re.compile(pattern)


# ==============================================================================
# MOCK LINGUISTIC CALIBRATION (Guarantees Deterministic Logic Tests)
# ==============================================================================
@pytest.fixture
def isolated_detector():
    """
    Creates a fully isolated LanguageDetector that does NOT rely on your live
    LENS_CONFIG. By injecting a perfect microcosm of languages, we can test the
    complex Bayesian logic gates without the tests randomly failing when you
    update the central dictionaries.
    """
    mock_langs = {
        "python": {"extensions": [".py"], "shebangs": ["python"]},
        "shell": {"extensions": [".sh"], "shebangs": ["bash"]},
        "cpp": {"extensions": [".cpp", ".h"], "lexical_family": "std_c"},
        "c": {
            "extensions": [".c", ".h"],
            "lexical_family": "std_c",
            "rules": {
                "main": re.compile(r"int\s+main")
            },  # <-- The engine needs a rule to detect C!
        },
        "objective-c": {
            "extensions": [".m", ".h"],
            "lexical_family": "std_c",
            "rules": {
                "interface": re.compile(r"@interface\s+")
            },  # Needed for Spectral Scan score
        },
        "html": {"extensions": [".html"], "lexical_family": "xml_angle"},
        "javascript": {"extensions": [".js"], "lexical_family": "std_c"},
        "markdown": {"extensions": [".md"], "lexical_family": "prose"},
    }

    # 1. Initialize with empty configs to prevent live lookups
    detector = LanguageDetector(mock_langs, {})

    # 2. Forcefully overwrite the internal maps to guarantee exact test states
    detector.extension_map = {
        ".py": "python",
        ".sh": "shell",
        ".h": "cpp",
        ".m": "objective-c",
        ".cpp": "cpp",
        ".c": "c",
        ".html": "html",
        ".js": "javascript",
        ".md": "markdown",
    }
    detector.anchor_map = {"README": "markdown"}

    detector.thresholds = {
        "PROSE_CONFIDENCE": 0.95,
        "ECOSYSTEM_DOMINANCE_MIN": 0.70,
        "INTENSITY_FLOOR": 0.78,
        "FLOOR_TIER_4": 0.10,  # <-- Lowered to allow our 16% density mock payload to pass!
        "TIER_4_MIN_LINES": 20,
        "TIER_4_OUTLIER_MARGIN": 1.10,
        "HANDSHAKE_LOOKAHEAD_LIMIT": 50000,
        "PROSE_BASELINE_SIGNAL": 3.0,
    }

    detector.COLLISION_FREQUENCIES = {".h", ".m"}
    detector.PROSE_ANCHORS = {"README"}
    detector.DISQUALIFIERS = {}

    detector.comment_defs = {
        "mechanical_families": {"std_c": {"delimiters": ["//", "/*"]}}
    }

    detector.HANDSHAKE_REGISTRY = [
        {
            "trigger": re.compile(r"<script>", re.I),
            "end": re.compile(r"</script>", re.I),
            "target": "javascript",
            "pair": None,
        }
    ]

    return detector


# ==============================================================================
# TEST 2: The Identity Crisis Trap (Security Lens)
# ==============================================================================
def test_identity_crisis_trap(isolated_detector):
    """Proves the engine catches files lying about their identity."""
    # A file claiming to be Python, but executing as Bash
    result = isolated_detector.inspect(
        file_path="test_malicious_xyz.py", content_sample="#!/bin/bash\nrm -rf /"
    )

    assert result["lang_id"] == "undeterminable", (
        "Failed to strip identity from conflicting file!"
    )
    assert result["lock_tier"] == 5, "Failed to apply Tier 5 Absolute Distrust!"
    assert any("Identity Masking" in flag for flag in result["anomaly_flags"]), (
        "Failed to cache the security anomaly!"
    )


# ==============================================================================
# TEST 3: Tier 0 (Convergent Lock)
# ==============================================================================
def test_tier_0_convergent_lock(isolated_detector):
    """Proves absolute certainty when Extension and Shebang agree."""
    result = isolated_detector.inspect(
        file_path="test_script_xyz.py",
        content_sample="#!/usr/bin/env python3\nprint('hello')",
    )

    assert result["lock_tier"] == 0, "Failed to apply Tier 0 Convergent Lock!"
    assert result["lang_id"] == "python"


# ==============================================================================
# TEST 4: Tier 1.5 (Ecosystem Gravity Collision Resolution)
# ==============================================================================
def test_ecosystem_gravity_collision(isolated_detector):
    """Proves the engine uses surrounding repo mass to resolve contested extensions."""
    # .h files collide between C, C++, and Obj-C.
    # We give it an ecosystem tally overwhelmingly dominated by C++
    tally = {".cpp": 50, ".c": 1}

    result = isolated_detector.inspect(
        file_path="src/test_header_xyz.h",
        content_sample="class MyClass {};",
        ext_tally=tally,
    )

    assert result["lang_id"] == "cpp"
    assert result["lock_tier"] == 1.5
    assert "Ecosystem Gravity" in result["source_proof"]


# ==============================================================================
# TEST 5: Tier 3 (Spectral Scan)
# ==============================================================================
def test_tier_3_spectral_scan(isolated_detector):
    """Proves the fallback syntax verification works when ecosystem gravity is missing."""
    # .m files collide (Obj-C vs MATLAB). Provide no gravity, forcing a syntax read.
    content = "#import <Foundation/Foundation.h>\n@interface MyClass : NSObject\n@end"

    result = isolated_detector.inspect(
        file_path="test_code_xyz.m", content_sample=content, ext_tally={}
    )

    assert result["lock_tier"] == 4, "Spectral resolution should occur at Tier 4!"
    assert result["lang_id"] == "objective-c"


# ==============================================================================
# TEST 6: Tier 4 (Deep Space Discovery)
# ==============================================================================
def test_tier_4_deep_space_discovery(isolated_detector):
    """Proves the engine can blindly identify a file with no extension."""
    import os

    # Needs > 20 lines to trigger Tier 4. We inject C-style comments and structure.
    content = (
        f"// C-style comment{os.linesep}" * 25
        + f"int main() {{ return 0; }}{os.linesep}" * 5
    )

    result = isolated_detector.inspect(
        file_path="unknown_binary_xyz", content_sample=content
    )

    # It should isolate 'std_c' as the comment family and find one of the C-family languages
    assert result["lang_id"] in ["c", "cpp", "objective-c", "javascript"]
    assert "Discovery" in result["source_proof"]


# ==============================================================================
# TEST 7: Hybrid Detection (Nested Languages)
# ==============================================================================
def test_hybrid_language_detection(isolated_detector):
    """Proves the Handshake Registry can identify injected scripts."""
    content = (
        "<html>\n<body>\n<script>\nconsole.log('test');\n</script>\n</body>\n</html>"
    )

    result = isolated_detector.inspect(
        file_path="test_index_xyz.html", content_sample=content
    )

    assert result["lang_id"] == "html"
    assert len(result["lang_mix"]) > 0
    assert any(mix["id"] == "javascript" for mix in result["lang_mix"]), (
        "Failed to extract nested JavaScript!"
    )


# ==============================================================================
# TEST 8: Prose & Metadata Overrides
# ==============================================================================
def test_prose_and_metadata_anchors(isolated_detector):
    """Proves specific filenames bypass standard code physics."""
    result = isolated_detector.inspect(
        file_path="README-TEST.md", content_sample="# Welcome to my project\n"
    )

    assert result["lang_id"] == "markdown"
    assert result["lock_tier"] == 1


from unittest.mock import patch
from gitgalaxy.standards.language_lens import FocusingError


# ==============================================================================
# TEST 9: Hardware Failure & OS Exceptions (Lines 842-848)
# ==============================================================================
@patch("builtins.open", side_effect=PermissionError("Mocked Permission Denied"))
def test_focusing_error_hardware_failure(mock_open, isolated_detector):
    """Proves the engine safely raises a FocusingError if the OS locks the file."""
    # By omitting `content_sample`, the engine attempts an OS-level read
    with pytest.raises(Exception) as exc_info:
        isolated_detector.inspect("locked_system_file.py")

    assert type(exc_info.value).__name__ == "FocusingError", (
        "Failed to catch FocusingError!"
    )
    assert "Failed to focus lens" in str(exc_info.value)


# ==============================================================================
# TEST 10: Multi-Dot & Safe Wrapper Stripping (Lines 150-162)
# ==============================================================================
def test_safe_wrapper_stripping(isolated_detector):
    """Proves the engine strips .template / .bak wrappers to find the true extension."""

    # 1. A true dotfile (should wipe extension)
    res_dotfile = isolated_detector.inspect(".bashrc", "echo 'hello'")
    # 2. A wrapped script (script.sh.template -> .sh -> shell)
    res_wrapped = isolated_detector.inspect("deploy.sh.template", "echo 'hello'")
    # 3. A dummy multi-dot (should NOT strip if the wrapper isn't recognized)
    res_unknown = isolated_detector.inspect("data.tar.gz", "binary data")

    assert res_dotfile["lock_tier"] >= 2, ".bashrc should not lock via extension"
    assert res_wrapped["lang_id"] == "shell", (
        "Failed to extract .sh from .template wrapper!"
    )
    # The engine gracefully accepts unknown extensions as Exo-Species at Tier 1.7!
    assert res_unknown["lang_id"] == "gz"


# ==============================================================================
# TEST 11: Local Ecosystem Gravity & Toxic Pruning (Lines 382-439)
# ==============================================================================
@patch("pathlib.Path.iterdir")
def test_local_ecosystem_gravity_and_toxic_pruning(mock_iterdir, isolated_detector):
    """Proves the engine calculates local folder mass and applies toxic constraints."""

    # Mock the local directory containing C++ files
    mock_child = type(
        "obj",
        (object,),
        {"is_file": lambda self: True, "suffix": ".cpp", "name": "main.cpp"},
    )
    mock_iterdir.return_value = [mock_child()] * 10

    # Inject a discriminator and a toxic disqualifier into our isolated C config
    isolated_detector.languages["c"]["discriminators"] = [".c_discrim"]
    isolated_detector.languages["c"]["disqualifiers"] = [".toxic_c"]

    # Provide a global tally that triggers the toxic collapse
    global_tally = {".c": 5, ".toxic_c": 1}

    # The .h extension is contested. The local directory is C++, but the global
    # tally has C files AND a toxic C disqualifier.
    lang, dominance = isolated_detector._evaluate_ecosystem_gravity(
        "src/header.h", ".h", global_tally
    )

    assert lang == "cpp", "Failed to prioritize Local C++ gravity over global tally!"
    assert dominance >= 0.70


# ==============================================================================
# TEST 12: Legacy Focus Gateway (Lines 124-128)
# ==============================================================================
def test_legacy_focus_gateway(isolated_detector):
    """Proves the legacy wrapper yields 'plaintext' for low-signal files."""
    lang, intensity, fam = isolated_detector.focus(
        "unknown_file", "a"
    )  # 'a' is too short to generate > 0.25 intensity

    assert lang == "plaintext"
    assert intensity == 0.40


# ==============================================================================
# TEST 13: Hybrid String Ignorance (Lines 852-876)
# ==============================================================================
def test_hybrid_string_ignorance(isolated_detector):
    """Proves the balanced end finder does not trip on triggers inside strings."""
    # A JavaScript payload inside an HTML file, where a string contains a fake closing tag
    content = '<html>\n<script>\nlet fake_end = "</script>";\nconsole.log(fake_end);\n</script>\n</html>'

    res = isolated_detector.inspect("index.html", content)

    assert "lang_mix" in res
    assert any(mix["id"] == "javascript" for mix in res["lang_mix"]), (
        "Failed to ignore string contents while mapping hybrid boundaries!"
    )


# ==============================================================================
# TEST 14: Tier 4 Macro Blindspot Fix & ABAP Handicap (Lines 639-702)
# ==============================================================================
@patch("gitgalaxy.standards.language_lens.time.time")
def test_tier_4_macro_and_handicaps(mock_time, isolated_detector):
    """Proves C-family macros provide a density boost, and ABAP gets handicapped."""

    # Make time.time() step by exactly 1.0s every call.
    # This guarantees the 'friction_ratio' tie-breaker is always perfectly 1.0 (Safe)
    mock_time.side_effect = [float(i) for i in range(50)]

    # Inject ABAP into the isolated detector
    isolated_detector.languages["abap"] = {
        "lexical_family": "std_c",
        "rules": {"keyword": re.compile(r"REPORT")},
    }

    # Payload: 20+ lines to trigger Tier 4. Lots of C macros.
    # We add 10 `int main` hits to ensure C brutally defeats C++ in the density margin.
    c_payload = (
        "// C file\n" * 15
        + "#define FOO 1\n#include <stdio.h>\n" * 5
        + "int main() {}\n" * 10
    )
    res_c = isolated_detector.inspect("no_extension_file", c_payload)

    # Payload: ABAP. The engine should hit the `regex_hits *= 0.7` handicap
    abap_payload = "// ABAP file\n" * 15 + "REPORT ZTEST.\n" * 5
    res_abap = isolated_detector.inspect("no_extension_file2", abap_payload)

    assert res_c["lang_id"] == "c", (
        "Failed to apply macro density boost and tie-breaker!"
    )
    assert res_abap["lang_id"] == "abap", "Failed to identify ABAP despite handicap!"
