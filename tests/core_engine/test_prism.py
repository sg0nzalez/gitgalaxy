import pytest
import re
from unittest.mock import patch

# Adjust this import to match your project structure
from gitgalaxy.core.prism import Prism, RefractionError

# ==============================================================================
# MOCK HARDWARE CALIBRATION
# ==============================================================================
# We mock the language and comment definitions so the tests run deterministically
# regardless of what is inside your actual language_standards.py file.

MOCK_COMMENT_DEFS = {
    "mechanical_families": {
        "std_c": {"delimiters": ["//", "/*", "*/"]},
        "pure_hash": {"delimiters": ["#"]},
        "singular": {"delimiters": []},  # Relies on hardcoded regex in Prism
        "nested_c": {"delimiters": ["//", "/*", "*/"]},
        "positional": {"delimiters": []},
    }
}

MOCK_LANG_DEFS = {
    "c": {"lexical_family": "std_c"},
    "python": {"lexical_family": "pure_hash"},
    "rust": {"lexical_family": "nested_c"},
    "cobol": {"lexical_family": "positional"},
    "markdown": {"lexical_family": "prose"},
    "html": {"lexical_family": "xml"},
    "php": {"lexical_family": "std_c"},
}


@pytest.fixture
def prism_engine():
    """Initializes the Prism with a controlled, deterministic optical matrix."""
    # We patch the SHIELD_PATTERN just in case the standard library is missing it during test time
    with patch(
        "gitgalaxy.core.prism.PRISM_CONFIG",
        {
            "SHIELD_PATTERN": r'(?P<shield>"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|`(?:\\.|[^`\\])*`)',
            "PYTHON_DOC_PATTERN": r"(\"\"\"[\s\S]*?\"\"\"|\'\'\'[\s\S]*?\'\'\')",
            "PHP_HEREDOC_PATTERN": r"<<<EOT[\s\S]*?EOT;",
            "PHP_MULTILINE_STRING": r"'(?:\\'|[^'])*'",
        },
    ):
        return Prism(comment_definitions=MOCK_COMMENT_DEFS, language_definitions=MOCK_LANG_DEFS)


# ==============================================================================
# TEST 1: THE BYPASS PROTOCOLS
# ==============================================================================
@pytest.mark.smoke
def test_prism_prose_bypass(prism_engine):
    """Proves that Markdown and XML are routed entirely to the Ghost Mass (Doc) stream."""
    content = "# Title\n\nThis is a markdown file.\nIt has no active logic."
    result = prism_engine.refract(content, primary_lang="markdown")

    assert result["code_stream"] == ""
    assert result["comment_stream"] == content
    assert result["coding_loc"] == 0
    assert result["doc_loc"] == 3


def test_prism_metadata_guard(prism_engine):
    """Proves that Shebangs bypass the comment stripper and stay in the logic stream."""
    content = "#!/usr/bin/env python3\n# This is a comment\nprint('Hello')"
    result = prism_engine.refract(content, primary_lang="python")

    assert "#!/usr/bin/env python3" in result["code_stream"]
    assert "print('Hello')" in result["code_stream"]
    assert "# This is a comment" not in result["code_stream"]
    assert "This is a comment" in result["comment_stream"]


# ==============================================================================
# TEST 2: THE STRING SHIELD
# ==============================================================================
def test_prism_string_shield_protection(prism_engine):
    """Proves that string literals containing comment delimiters do not trigger the stripper."""
    content = (
        'let url = "https://github.com"; // Set the target URL\n'
        'let str_block = "/* DO NOT STRIP ME */";\n'
        "/* Real block comment */"
    )
    result = prism_engine.refract(content, primary_lang="c")

    code = result["code_stream"]
    docs = result["comment_stream"]

    assert "https://" + "github.com" in code
    assert "/* DO NOT STRIP ME */" in code
    assert "Set the target URL" in docs
    assert "Real block comment" in docs


# ==============================================================================
# TEST 3: NESTED BLOCK PEELER
# ==============================================================================
def test_prism_nested_block_peeling(prism_engine):
    """Proves the while-peel loop correctly extracts recursive block comments."""
    content = (
        "fn main() {\n"
        "    /* Outer comment\n"
        "       /* Inner comment */\n"
        "       Back to outer */\n"
        "    println!('Done');\n"
        "}"
    )
    result = prism_engine.refract(content, primary_lang="rust")

    code = result["code_stream"]
    docs = result["comment_stream"]

    assert "fn main() {" in code
    assert "println!('Done');" in code
    assert "Outer comment" not in code
    assert "Inner comment" in docs


# ==============================================================================
# TEST 4: POSITIONAL ANCHORS
# ==============================================================================
def test_prism_positional_anchors(prism_engine):
    """Proves legacy column-anchored and inline comments are handled correctly."""
    content = (
        "      * This is a COBOL column 7 comment\n"
        "       MOVE A TO B. *> This is an inline comment\n"
        "C This is a Fortran column 1 comment\n"
        "       X = 1 ! This is a Fortran inline comment"
    )

    prism_engine.POSITIONAL_ANCHORS = {"*", "C", "c", "!"}
    result = prism_engine.refract(content, primary_lang="cobol")

    code = result["code_stream"]
    docs = result["comment_stream"]

    assert "MOVE A TO B." in code
    assert "This is a COBOL column 7 comment" not in code
    assert "This is an inline comment" in docs


# ==============================================================================
# TEST 5: HARDENED PYTHON DOCSTRINGS
# ==============================================================================
def test_prism_python_docstring_extraction(prism_engine):
    """Proves multi-line string literals acting as docstrings are extracted."""
    content = "def compute_hash():\n" '    """\n' "    This is a module docstring.\n" '    """\n' "    return True"
    result = prism_engine.refract(content, primary_lang="python")

    assert "def compute_hash():" in result["code_stream"]
    assert "This is a module docstring." in result["comment_stream"]


# ==============================================================================
# TEST 6: THE UNDETERMINABLE & METADATA BYPASSES
# ==============================================================================
def test_prism_undeterminable_and_xml_bypass(prism_engine):
    """Proves unknown and unparsable languages skip refraction entirely."""
    content = "some raw code // comment"
    res_unknown = prism_engine.refract(content, primary_lang="undeterminable")
    assert res_unknown["code_stream"] == content
    assert res_unknown["comment_stream"] == ""

    # We use chr() to prevent the HTML comment from vanishing when copying
    xml_content = "<?xml version='1.0'?>\n<data>" + chr(60) + "!-- comment --" + chr(62) + "</data>"
    res_xml = prism_engine.refract(xml_content, primary_lang="xml")
    assert res_xml["code_stream"] == ""
    assert chr(60) + "!-- comment --" + chr(62) in res_xml["comment_stream"]

    php_content = "<?php\n// This is a comment\n$x = 1;"
    res_php = prism_engine.refract(php_content, primary_lang="php")
    assert "<?php" in res_php["code_stream"]


# ==============================================================================
# TEST 7: PHP HEREDOC AND MULTILINE STRINGS
# ==============================================================================
def test_prism_php_string_extraction(prism_engine):
    """Proves PHP Heredoc and large strings are stripped to ghost mass."""
    prism_engine.languages["php"] = {"lexical_family": "std_c"}
    prism_engine.PHP_HEREDOC_PATTERN = re.compile(r"<<<EOT[\s\S]*?EOT;", re.M)
    prism_engine.PHP_MULTILINE_STRING = re.compile(r"'(?:\\'|[^'])*'", re.M)

    content = "<?php\n$a = <<<EOT\nMassive Text\nEOT;\n$b = 'Multi\nLine';\n// comment"
    res = prism_engine.refract(content, primary_lang="php")

    assert "<<<EOT" not in res["code_stream"]
    assert '""' in res["code_stream"]
    assert "Massive Text" in res["comment_stream"]


# ==============================================================================
# TEST 8: HYBRID PARTITIONING & BALANCED END ESCAPING
# ==============================================================================
def test_prism_hybrid_partitioning_and_escaping(prism_engine):
    """Proves the Handshake Registry accurately isolates embedded languages."""
    prism_engine.HANDSHAKES = [
        {
            "trigger": re.compile(r"<script>", re.I),
            "end": re.compile(r"</script>", re.I),
            "target": "javascript",
            "pair": None,
        },
        {
            "trigger": re.compile(r"\{", re.I),
            "end": None,
            "target": "css",
            "pair": ("{", "}"),
        },
    ]

    prism_engine.HANDSHAKE_LOOKAHEAD_LIMIT = 20
    html_content = "<html><script>let x = 1; // js"
    res1 = prism_engine.refract(html_content, primary_lang="html")
    assert "let x = 1;" in res1["code_stream"]

    prism_engine.HANDSHAKE_LOOKAHEAD_LIMIT = 50000
    css_content = r"body { content: 'escaped \}'; /* comment */ }"
    idx = prism_engine._find_balanced_end(css_content, 5, "{", "}")

    assert css_content[idx - 1] == "}"


# ==============================================================================
# TEST 9: DYNAMIC OPTICAL MATRIX CALIBRATION
# ==============================================================================
def test_prism_matrix_calibration_edge_cases():
    """Proves all complex and fallback regex families compile correctly."""

    # We construct HTML comments dynamically to completely bypass UI clipboard erasing
    html_open = chr(60) + "!--"
    html_close = "--" + chr(62)

    # 1. Primary Branches (Full Delimiter Sets)
    primary_families = {
        "hybrid_hash": {"delimiters": ["#", "<#", "#>"]},
        "hybrid_dash": {"delimiters": ["--", html_open, html_close, "{-", "-}"]},
        "polyglot": {"delimiters": ["//", "/*", "*/", "#"]},
        "empty_delim": {"delimiters": []},
    }

    engine_primary = Prism(
        comment_definitions={"mechanical_families": primary_families},
        language_definitions={},
    )

    assert "hybrid_hash" in engine_primary.PRISM_MATRIX
    assert "hybrid_dash" in engine_primary.PRISM_MATRIX
    assert re.escape("{-") in engine_primary.PRISM_MATRIX["hybrid_dash"].pattern
    assert "polyglot" in engine_primary.PRISM_MATRIX

    # 2. Fallback Branches (Partial Delimiter Sets)
    fallback_families = {
        "hybrid_dash": {"delimiters": ["--", html_open, html_close]},
        "polyglot": {"delimiters": ["//", "/*", "*/"]},
    }

    engine_fallback = Prism(
        comment_definitions={"mechanical_families": fallback_families},
        language_definitions={},
    )

    assert "hybrid_dash" in engine_fallback.PRISM_MATRIX

    # We check if the safely escaped version of '<!--' is in the compiled pattern
    assert re.escape(html_open) in engine_fallback.PRISM_MATRIX["hybrid_dash"].pattern
    assert "polyglot" in engine_fallback.PRISM_MATRIX


# ==============================================================================
# TEST 10: SAFETY LIMITS AND CATASTROPHIC ERRORS
# ==============================================================================
def test_prism_safety_limits_and_errors(prism_engine):
    """Proves nested peel limits and catastrophic exception handlers fire."""

    prism_engine.NESTED_PEEL_LIMIT = 1
    content = "/* level 1 /* level 2 */ */"
    code, lits = prism_engine._refract_nested(content)
    assert "level 2" in " ".join(lits)

    with patch.object(prism_engine, "_partition_segments", side_effect=ValueError("Simulated Fault")):
        with pytest.raises(RefractionError) as exc:
            prism_engine.refract("print(1)", primary_lang="python")
        assert "Prism failure: Simulated Fault" in str(exc.value)
