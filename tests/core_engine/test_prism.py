import pytest
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
        "singular": {"delimiters": []}, # Relies on hardcoded regex in Prism
        "nested_c": {"delimiters": ["//", "/*", "*/"]},
        "positional": {"delimiters": []}
    }
}

MOCK_LANG_DEFS = {
    "c": {"lexical_family": "std_c"},
    "python": {"lexical_family": "pure_hash"},
    "rust": {"lexical_family": "nested_c"},
    "cobol": {"lexical_family": "positional"},
    "markdown": {"lexical_family": "prose"}
}

@pytest.fixture
def prism_engine():
    """Initializes the Prism with a controlled, deterministic optical matrix."""
    # We patch the SHIELD_PATTERN just in case the standard library is missing it during test time
    with patch('gitgalaxy.core.prism.PRISM_CONFIG', {
        "SHIELD_PATTERN": r'(?P<shield>"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|`(?:\\.|[^`\\])*`)',
        "PYTHON_DOC_PATTERN": r'(\"\"\"[\s\S]*?\"\"\"|\'\'\'[\s\S]*?\'\'\')'
    }):
        return Prism(comment_definitions=MOCK_COMMENT_DEFS, language_definitions=MOCK_LANG_DEFS)

# ==============================================================================
# TEST 1: THE BYPASS PROTOCOLS
# ==============================================================================
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
    
    # The shebang should be in the code stream, but the standard # comment should be stripped
    assert "#!/usr/bin/env python3" in result["code_stream"]
    assert "print('Hello')" in result["code_stream"]
    assert "# This is a comment" not in result["code_stream"]
    assert "This is a comment" in result["comment_stream"]

# ==============================================================================
# TEST 2: THE STRING SHIELD (Crucial for preventing ReDoS and Logic Erasure)
# ==============================================================================
def test_prism_string_shield_protection(prism_engine):
    """
    Proves that string literals containing comment delimiters (like http://) 
    do not trigger the stripper.
    """
    content = (
        'let url = "https://github.com"; // Set the target URL\n'
        'let str_block = "/* DO NOT STRIP ME */";\n'
        '/* Real block comment */'
    )
    result = prism_engine.refract(content, primary_lang="c")
    
    code = result["code_stream"]
    docs = result["comment_stream"]
    
    # Active Matter (Code) Verification
    assert "https://github.com" in code, "Shield failed! Stripped // inside a string."
    assert "/* DO NOT STRIP ME */" in code, "Shield failed! Stripped /* inside a string."
    
    # Ghost Mass (Comment) Verification
    assert "Set the target URL" in docs
    assert "Real block comment" in docs
    assert "DO NOT STRIP ME" not in docs

# ==============================================================================
# TEST 3: NESTED BLOCK PEELER (Rust/Swift/Scala)
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
    assert "Back to outer" in docs

# ==============================================================================
# TEST 4: POSITIONAL ANCHORS (COBOL / Fortran)
# ==============================================================================
def test_prism_positional_anchors(prism_engine):
    """Proves legacy column-anchored and inline comments are handled correctly."""
    content = (
        "      * This is a COBOL column 7 comment\n"
        "       MOVE A TO B. *> This is an inline comment\n"
        "C This is a Fortran column 1 comment\n"
        "       X = 1 ! This is a Fortran inline comment"
    )
    
    # Temporarily force the positional anchors for the test
    prism_engine.POSITIONAL_ANCHORS = {"*", "C", "c", "!"}
    
    result = prism_engine.refract(content, primary_lang="cobol")
    code = result["code_stream"]
    docs = result["comment_stream"]
    
    assert "MOVE A TO B." in code
    assert "X = 1" in code
    assert "This is a COBOL column 7 comment" not in code
    assert "This is an inline comment" in docs
    assert "This is a Fortran inline comment" in docs

# ==============================================================================
# TEST 5: HARDENED PYTHON DOCSTRINGS
# ==============================================================================
def test_prism_python_docstring_extraction(prism_engine):
    """Proves multi-line string literals acting as docstrings are extracted."""
    content = (
        "def compute_hash():\n"
        "    \"\"\"\n"
        "    This is a module docstring.\n"
        "    It spans multiple lines.\n"
        "    \"\"\"\n"
        "    x = '\"\"\"Not a docstring\"\"\"'\n"
        "    return True"
    )
    result = prism_engine.refract(content, primary_lang="python")
    
    code = result["code_stream"]
    docs = result["comment_stream"]
    
    assert "def compute_hash():" in code
    assert "return True" in code
    # The docstring should be moved to the docs stream
    assert "This is a module docstring." in docs