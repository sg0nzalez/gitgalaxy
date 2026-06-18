import pytest
import json
from unittest.mock import patch

# Adjust this import to match your project structure
from gitgalaxy.core.guidestar_lens import GuideStarLens

# ==============================================================================
# MOCK HARDWARE CALIBRATION
# ==============================================================================
MOCK_GUIDESTAR_CONFIG = {
    "MANIFEST_MAP": {
        "package.json": "javascript",
        "Makefile": "unknown",
        "pyproject.toml": "python",
    },
    "INTENT_BIASED_SECTORS": ["src", "lib", "core", "api"],
    "EXEC_PREFIX_MAP": {"python": "python", "node": "javascript"},
}


@pytest.fixture
def guidestar(tmp_path):
    """Initializes the GuideStar Lens with a mocked configuration."""
    with patch(
        "gitgalaxy.core.guidestar_lens.GuideStarLens._gs_config", MOCK_GUIDESTAR_CONFIG
    ):
        with patch(
            "gitgalaxy.core.guidestar_lens.GuideStarLens.MANIFEST_MAP",
            MOCK_GUIDESTAR_CONFIG["MANIFEST_MAP"],
        ):
            with patch(
                "gitgalaxy.core.guidestar_lens.GuideStarLens.INTENT_BIASED_SECTORS",
                set(MOCK_GUIDESTAR_CONFIG["INTENT_BIASED_SECTORS"]),
            ):
                return GuideStarLens(root_path=tmp_path)


# ==============================================================================
# TEST 1: THE ROADMAP SCOUT (Manifest Parsing & AI Detection)
# ==============================================================================
def test_guidestar_manifest_and_ai_detection(guidestar, tmp_path):
    """
    Proves that package.json is parsed for entry points, and that AI
    dependencies trigger the synthetic ecosystem prior.
    """
    # Create a mock package.json
    pkg_path = tmp_path / "package.json"
    pkg_data = {
        "main": "src/server.js",
        "scripts": {"start": "node dist/index.js"},
        "dependencies": {"langchain": "^0.0.1"},  # The AI trigger keyword!
    }
    pkg_path.write_text(json.dumps(pkg_data), encoding="utf-8")

    # Run the alignment phase
    guidestar.scan_project_config()

    # 1. Test standard manifest extraction
    found, lock = guidestar.get_intent_status("src/server.js")
    assert found is True
    assert lock["lang_id"] == "javascript"
    assert lock["intensity"] == 0.95
    assert "Manifest Entry" in lock["source_proof"]

    # 2. Test script extraction
    found, lock = guidestar.get_intent_status("dist/index.js")
    assert found is True
    assert lock["intensity"] == 0.85

    # 3. Test AI Ecosystem Detection
    found, lock = guidestar.get_intent_status("__gitgalaxy_meta__.json")
    assert found is True
    assert lock["intensity"] == 1.0
    assert "AI Ecosystem Lock" in lock["source_proof"]


# ==============================================================================
# TEST 2: THE AUTHORITY SCOUT (.gitattributes)
# ==============================================================================
def test_guidestar_gitattributes_authority(guidestar, tmp_path):
    """
    Proves that .gitattributes pattern rules override normal logic with
    a 0.99 confidence lock.
    """
    attr_path = tmp_path / ".gitattributes"
    # Force all .h files to be classified as C++ instead of C
    attr_path.write_text("*.h linguist-language=C++\n", encoding="utf-8")

    guidestar.scan_project_config()

    # Test a file that matches the pattern
    found, lock = guidestar.get_intent_status("include/math_ops.h")

    assert found is True
    assert lock["lang_id"] == "cpp"  # Ensure it translated C++ to cpp
    assert lock["intensity"] == 0.99
    assert "Authoritative Override" in lock["source_proof"]


# ==============================================================================
# TEST 3: THE EVASION SCOUT (.gitignore)
# ==============================================================================
def test_guidestar_gitignore_evasion_tactics(guidestar, tmp_path):
    """
    Proves that force-including a compiled binary in .gitignore triggers
    a max-priority evasion alarm (1.0 confidence).
    """
    ignore_path = tmp_path / ".gitignore"
    ignore_path.write_text(
        "node_modules/\nbuild/\n!malicious_payload.so\n", encoding="utf-8"
    )

    guidestar.scan_project_config()

    found, lock = guidestar.get_intent_status("malicious_payload.so")

    assert found is True
    assert lock["intensity"] == 1.0
    assert "Hostile Gitignore Force-Include" in lock["source_proof"]


# ==============================================================================
# TEST 4: SECTOR BIAS (The Dynamic Priority Queue)
# ==============================================================================
def test_guidestar_sector_bias(guidestar, tmp_path):
    """
    Proves that files located in structurally important directories get a
    baseline priority boost, even if they aren't explicitly in a manifest.
    """
    # /src/ is in the mocked INTENT_BIASED_SECTORS
    found, lock = guidestar.get_intent_status("src/utils/helper.js")

    assert found is True
    assert lock["lang_id"] == "unknown"  # It doesn't know the lang yet
    assert lock["intensity"] == 0.75
    assert lock["source_proof"] == "Sector Bias"

    # /temp/ is not in the biased sectors
    found, lock = guidestar.get_intent_status("temp/cache.log")
    assert found is False