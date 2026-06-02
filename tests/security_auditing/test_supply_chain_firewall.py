import pytest
import sys
import json
from unittest.mock import patch

import gitgalaxy.tools.supply_chain_security.supply_chain_firewall as firewall_module


# ==============================================================================
# TEST 1: Zero-Trust Import Slicer (Regex & Bins)
# ==============================================================================
def test_zero_trust_import_slicer(monkeypatch):
    monkeypatch.setattr(firewall_module, "APPROVED_IMPORTS", ["react", "express"])
    monkeypatch.setattr(firewall_module, "BLACKLISTED_IMPORTS", ["event-stream-malware"])

    # Build the mock RAM graph (Pre-tokenized by Phase 1)
    mock_ram_graph = [
        {"path": "app.js", "raw_imports": ["react", "event-stream-malware"], "equations": {}, "coding_loc": 50},
        {"path": "main.py", "raw_imports": ["django"], "equations": {}, "coding_loc": 20},
    ]

    result = firewall_module.run_firewall_audit(mock_ram_graph)
    assert result["imports_blacklisted"] == 1, "Failed to identify blacklisted package!"
    assert result["imports_unknown"] == 1, "Failed to identify unknown package!"


# ==============================================================================
# TEST 2: Strict Mode Enforcement
# ==============================================================================
def test_strict_mode_enforcement(tmp_path, monkeypatch):
    monkeypatch.setattr(firewall_module, "APPROVED_IMPORTS", ["react"])
    monkeypatch.setattr(firewall_module, "BLACKLISTED_IMPORTS", [])
    monkeypatch.setattr(firewall_module, "STRICT_IMPORT_MODE", True)

    mock_ram_graph = {"stars": [{"path": "server.js", "raw_imports": ["shadow-library"], "equations": {}}]}

    # Test the main CLI interface by writing a fake RAM graph JSON
    graph_file = tmp_path / "results.json"
    graph_file.write_text(json.dumps(mock_ram_graph), encoding="utf-8")

    test_args = ["supply_chain_firewall.py", str(graph_file)]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as exc:
            firewall_module.main()
        assert exc.value.code == 1, "STRICT_IMPORT_MODE failed!"


# ==============================================================================
# TEST 3: The Inert Data Shield (Minified File Bypass)
# ==============================================================================
def test_inert_data_shield_minified_bypass(tmp_path, monkeypatch):
    monkeypatch.setattr(firewall_module, "STRICT_IMPORT_MODE", False)
    monkeypatch.setattr(firewall_module, "BLACKLISTED_IMPORTS", [])

    # The firewall evaluates behavioral hits based on Phase 1 equations.
    # We simulate a file that Phase 1 flagged with massive threats
    mock_ram_graph_threat = {
        "stars": [
            {"path": "logic.js", "raw_imports": [], "equations": {"homoglyphs": 500, "danger": 50}, "coding_loc": 50}
        ]
    }

    graph_file = tmp_path / "results.json"
    graph_file.write_text(json.dumps(mock_ram_graph_threat), encoding="utf-8")

    test_args = ["supply_chain_firewall.py", str(graph_file)]

    # It should exit with code 1 due to the high density of threats
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as exc:
            firewall_module.main()
        assert exc.value.code == 1
