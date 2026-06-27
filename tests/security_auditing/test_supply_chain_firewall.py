import pytest
import sys
import json
from unittest.mock import patch

import gitgalaxy.tools.supply_chain_security.supply_chain_firewall as firewall_module

# ==============================================================================
# TEST 1: Dependency Graph Import Verification
# ==============================================================================
def test_zero_trust_import_verification(monkeypatch):
    """
    Validates that the firewall correctly segregates imports into approved,
    unknown, and blacklisted categories based on enterprise policy constraints.
    """
    monkeypatch.setattr(firewall_module, "APPROVED_IMPORTS", ["react", "express"])
    monkeypatch.setattr(
        firewall_module, "BLACKLISTED_IMPORTS", ["event-stream-malware"]
    )

    mock_ram_graph = [
        {
            "path": "app.js",
            "raw_imports": ["react", "event-stream-malware"],
            "equations": {},
            "coding_loc": 50,
        },
        {
            "path": "main.py",
            "raw_imports": ["django"],
            "equations": {},
            "coding_loc": 20,
        },
    ]

    result = firewall_module.run_firewall_audit(mock_ram_graph)
    assert result["imports_whitelisted"] == 1, "Failed to identify approved package."
    assert result["imports_blacklisted"] == 1, "Failed to identify blacklisted package."
    assert result["imports_unknown"] == 1, "Failed to identify unknown package."
    assert result["threats_found"] == 1, "Blacklisted package did not increment threat counter."

# ==============================================================================
# TEST 2: Local Path and Sub-Module Truncation Shield
# ==============================================================================
def test_import_truncation_and_local_shield(monkeypatch):
    """
    Ensures that local relative imports are ignored, and deeply nested
    scoped packages (@org/pkg/module) are properly truncated for evaluation.
    """
    monkeypatch.setattr(firewall_module, "APPROVED_IMPORTS", ["@angular/core", "lodash"])
    monkeypatch.setattr(firewall_module, "BLACKLISTED_IMPORTS", [])

    mock_ram_graph = [
        {
            "path": "component.ts",
            # .local should be ignored. @angular/core/testing should truncate to @angular/core
            "raw_imports": ["./local-service", "@angular/core/testing", "lodash/fp"],
            "equations": {},
            "coding_loc": 50,
        }
    ]

    result = firewall_module.run_firewall_audit(mock_ram_graph)
    assert result["imports_whitelisted"] == 2, "Failed to truncate and match scoped/nested dependencies."
    assert result["imports_unknown"] == 0, "Local relative import was erroneously evaluated."

# ==============================================================================
# TEST 3: Alias Spoofing Detection
# ==============================================================================
def test_alias_spoofing_detection(monkeypatch, capsys):
    """
    Validates that the firewall correctly detects when a safe alias is mapped
    to a blacklisted upstream package via the alias_map.
    """
    monkeypatch.setattr(firewall_module, "APPROVED_IMPORTS", [])
    monkeypatch.setattr(firewall_module, "BLACKLISTED_IMPORTS", ["malicious-core"])

    mock_ram_graph = [
        {
            "path": "package.json",
            "raw_imports": ["safe-utils"],
            "equations": {},
            "coding_loc": 10,
        }
    ]
    
    # Simulate an npm alias: "safe-utils": "npm:malicious-core@1.0"
    mock_alias_map = {"safe-utils": "malicious-core"}

    result = firewall_module.run_firewall_audit(mock_ram_graph, alias_map=mock_alias_map)
    captured = capsys.readouterr()
    
    assert result["imports_blacklisted"] == 1, "Failed to dereference spoofed alias."
    assert result["threats_found"] == 1, "Spoofed alias did not increment threat counter."
    assert "Spoofed alias blocked" in captured.out, "Missing spoofed alias log output."

# ==============================================================================
# TEST 4: Strict Policy Enforcement Mode
# ==============================================================================
def test_strict_mode_enforcement(tmp_path, monkeypatch):
    """
    Ensures that when STRICT_IMPORT_MODE is enabled, any unknown dependency
    causes the pipeline to fail with a SystemExit.
    """
    monkeypatch.setattr(firewall_module, "APPROVED_IMPORTS", ["react"])
    monkeypatch.setattr(firewall_module, "BLACKLISTED_IMPORTS", [])
    monkeypatch.setattr(firewall_module, "STRICT_IMPORT_MODE", True)

    mock_ram_graph = {
        "artifacts": [
            {"path": "server.js", "raw_imports": ["shadow-library"], "equations": {}}
        ]
    }

    graph_file = tmp_path / "results.json"
    graph_file.write_text(json.dumps(mock_ram_graph), encoding="utf-8")

    test_args = ["supply_chain_firewall.py", str(graph_file)]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as exc:
            firewall_module.main()
        assert exc.value.code == 1, "Strict import policy enforcement failed to block an unknown package."

# ==============================================================================
# TEST 5: Behavioral Threat Density Evaluation
# ==============================================================================
def test_behavioral_threat_evaluation(tmp_path, monkeypatch):
    """
    Validates that artifacts exhibiting high-density threat indicators
    (calculated during Phase 1) trigger a firewall block.
    """
    monkeypatch.setattr(firewall_module, "STRICT_IMPORT_MODE", False)
    monkeypatch.setattr(firewall_module, "BLACKLISTED_IMPORTS", [])

    mock_ram_graph_threat = {
        "artifacts": [
            {
                "path": "logic.js",
                "raw_imports": [],
                "equations": {"homoglyphs": 500, "high_risk_execution": 50},
                "coding_loc": 50,
            }
        ]
    }

    graph_file = tmp_path / "results.json"
    graph_file.write_text(json.dumps(mock_ram_graph_threat), encoding="utf-8")

    test_args = ["supply_chain_firewall.py", str(graph_file)]

    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as exc:
            firewall_module.main()
        assert exc.value.code == 1, "Behavioral threat density evaluation failed to trigger pipeline failure."

# ==============================================================================
# TEST 6: Build-Time Execution Multiplier (Static Sandbox)
# ==============================================================================
def test_build_time_execution_multiplier(monkeypatch):
    """
    Ensures that critical build files (like setup.py) have their risk equations
    artificially multiplied to make them hyper-sensitive to anomalous logic.
    """
    monkeypatch.setattr(firewall_module, "STRICT_IMPORT_MODE", False)
    
    # MATHEMATICS FIX: 
    # A file with 1000 LOC gets a safe_loc of 1150.
    # To breach the 20% 'paranoid' Logic Bomb threshold, the file needs 
    # a sabotage density of >= 0.20 (230 effective hits).
    #
    # standard_app.py: 20 danger hits * 1.5 = 30 hits (2.6% density) -> Safely Passes
    # setup.py: (20 danger hits * 10x multiplier) * 1.5 = 300 hits (26.0% density) -> Blocks!
    mock_ram_graph = [
        {
            "path": "setup.py",
            "raw_imports": [],
            "equations": {"high_risk_execution": 20},
            "coding_loc": 1000,
        },
        {
            "path": "standard_app.py",
            "raw_imports": [],
            "equations": {"high_risk_execution": 20},
            "coding_loc": 1000,
        }
    ]

    result = firewall_module.run_firewall_audit(mock_ram_graph)
    assert result["threats_found"] == 1, "Build-time multiplier failed to amplify threat in setup.py."

# ==============================================================================
# TEST 7: CLI Main - Missing Target Validation
# ==============================================================================
def test_main_missing_target(capsys):
    """Proves the CLI catches invalid directories and exits safely."""
    with patch("sys.argv", ["supply_chain_firewall.py", "non_existent_graph.json"]):
        with pytest.raises(SystemExit) as exc_info:
            firewall_module.main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Error: RAM graph" in captured.out

# ==============================================================================
# TEST 8: CLI Main - Corrupted JSON Handling
# ==============================================================================
def test_main_corrupted_json(tmp_path, capsys):
    """Ensures the firewall gracefully exits if the input graph is malformed."""
    broken_graph = tmp_path / "broken.json"
    broken_graph.write_text("{ broken_json: ", encoding="utf-8")

    with patch("sys.argv", ["supply_chain_firewall.py", str(broken_graph)]):
        with pytest.raises(SystemExit) as exc_info:
            firewall_module.main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Failed to parse RAM graph JSON" in captured.out