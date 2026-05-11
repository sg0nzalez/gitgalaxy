import pytest
import sys
from pathlib import Path
from unittest.mock import patch

import gitgalaxy.tools.supply_chain_security.supply_chain_firewall as firewall_module

# ==============================================================================
# TEST 1: Zero-Trust Import Slicer (Regex & Bins)
# ==============================================================================
def test_zero_trust_import_slicer(tmp_path, monkeypatch):
    monkeypatch.setattr(firewall_module, "APPROVED_IMPORTS", ["react", "express"])
    monkeypatch.setattr(firewall_module, "BLACKLISTED_IMPORTS", ["event-stream-malware"])
    
    repo_dir = tmp_path / "imports_repo"
    repo_dir.mkdir()
    (repo_dir / "app.js").write_text("import 'react'; require('event-stream-malware');", encoding="utf-8")
    (repo_dir / "main.py").write_text("from 'django' import models", encoding="utf-8")
    
    result = firewall_module.run_firewall_audit(repo_dir)
    assert result["imports_blacklisted"] == 1, "Failed to identify blacklisted package!"
    assert result["imports_unknown"] == 1, "Failed to identify unknown package!"

# ==============================================================================
# TEST 2: Strict Mode Enforcement
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.supply_chain_firewall.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.supply_chain_firewall.ApertureFilter")
def test_strict_mode_enforcement(mock_aperture_class, mock_security_class, tmp_path, monkeypatch):
    monkeypatch.setattr(firewall_module, "APPROVED_IMPORTS", ["react"])
    monkeypatch.setattr(firewall_module, "BLACKLISTED_IMPORTS", [])
    monkeypatch.setattr(firewall_module, "STRICT_IMPORT_MODE", True)
    
    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_solar_shield.return_value = True
    mock_aperture.evaluate_path_integrity.return_value = (True, 100, "OK")
    
    mock_security = mock_security_class.return_value
    mock_security.scan_content.return_value = {"counts": {}, "snippets": {}}
    mock_security.evaluate_risk.return_value = {}

    repo_dir = tmp_path / "strict_repo"
    repo_dir.mkdir()
    (repo_dir / "server.js").write_text("import 'shadow-library';", encoding="utf-8")
    
    test_args = ["supply_chain_firewall.py", str(repo_dir)]
    with patch.object(sys, 'argv', test_args):
        with pytest.raises(SystemExit) as exc:
            firewall_module.main()
        assert exc.value.code == 1, "STRICT_IMPORT_MODE failed!"

# ==============================================================================
# TEST 3: The Inert Data Shield (Minified File Bypass)
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.supply_chain_firewall.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.supply_chain_firewall.ApertureFilter")
def test_inert_data_shield_minified_bypass(mock_aperture_class, mock_security_class, tmp_path, monkeypatch):
    monkeypatch.setattr(firewall_module, "STRICT_IMPORT_MODE", False)
    monkeypatch.setattr(firewall_module, "BLACKLISTED_IMPORTS", [])
    
    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_solar_shield.return_value = True
    mock_aperture.evaluate_path_integrity.return_value = (True, 100, "OK")
    
    mock_security = mock_security_class.return_value
    mock_security.scan_content.return_value = {"counts": {"homoglyphs": 500, "danger": 50}, "snippets": {}}
    
    def mock_eval_risk(counts, loc):
        if counts.get("homoglyphs", 0) > 10: return {"Hidden Malware Risk": 0.99}
        return {}
        
    mock_security.evaluate_risk.side_effect = mock_eval_risk

    repo_dir = tmp_path / "inert_repo"
    repo_dir.mkdir()
    test_args = ["supply_chain_firewall.py", str(repo_dir)]
    
    normal_file = repo_dir / "logic.js"
    normal_file.write_text("var a = 'fake malware';", encoding="utf-8")
    
    with patch.object(sys, 'argv', test_args):
        with pytest.raises(SystemExit) as exc:
            firewall_module.main()
        assert exc.value.code == 1
        
    normal_file.unlink()
    min_file = repo_dir / "logic.min.js"
    min_file.write_text("var a = 'fake malware';", encoding="utf-8")
    
    try:
        with patch.object(sys, 'argv', test_args):
            firewall_module.main()
    except SystemExit:
        pytest.fail("The Inert Data Shield failed!")