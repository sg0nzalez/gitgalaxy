import os
from pathlib import Path
from unittest.mock import patch, MagicMock

import gitgalaxy.tools.supply_chain_security.binary_anomaly_detector as xray_module

# ==============================================================================
# TEST 1: The Routing Matrix (Denylist vs Allowlist vs Test Folders)
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.ApertureFilter")
def test_xray_routing_matrix(mock_aperture_class, mock_security_class, tmp_path, monkeypatch):
    monkeypatch.setattr(xray_module, "DENYLIST_PATTERNS", ["*.key", "*.pem", "id_rsa*"])
    monkeypatch.setattr(xray_module, "XRAY_BYPASS_EXTENSIONS", [".gz", ".zip"])
    monkeypatch.setattr(xray_module, "ALLOWLIST_PATHS", ["approved_keys/"])

    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_solar_shield.return_value = True

    mock_security = mock_security_class.return_value
    mock_security.scan_content.return_value = {"counts": {"entropy": 6.5, "bitwise_hits": 0}}
    mock_security.scan_binary.return_value = {}

    repo_dir = tmp_path / "routing_repo"
    repo_dir.mkdir()
    
    # File A (Anomaly)
    (repo_dir / "private.key").write_text("FAKE_PRIVATE_KEY", encoding="utf-8")
    
    # File B (Bypass Allowlist)
    approved_dir = repo_dir / "approved_keys"
    approved_dir.mkdir()
    (approved_dir / "service.pem").write_text("FAKE_CERT", encoding="utf-8")
    
    # File C (Bypass Extension)
    (repo_dir / "compressed.zip").write_text("FAKE_ZIP_DATA", encoding="utf-8")
    
    # File D (Bypass Test Folder) 
    # Nested inside 'src' so the string matching for "/tests/" perfectly aligns
    src_dir = repo_dir / "src"
    src_dir.mkdir()
    test_dir = src_dir / "tests"
    test_dir.mkdir()
    (test_dir / "mock_payload.dat").write_text("FAKE_HIGH_ENTROPY_DATA", encoding="utf-8")

    result = xray_module.run_xray_audit(repo_dir)
    assert result["anomalies_found"] == 1, "The routing matrix failed! Check Denylist/Allowlist math."

# ==============================================================================
# TEST 2: The Deep Scan Threat Identification
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.ApertureFilter")
def test_xray_deep_scan_threats(mock_aperture_class, mock_security_class, tmp_path):
    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_solar_shield.return_value = True
    
    repo_dir = tmp_path / "deep_scan_repo"
    repo_dir.mkdir()
    
    clean_file = repo_dir / "clean.txt"
    clean_file.write_text("Hello world", encoding="utf-8")
    
    spoofed_file = repo_dir / "hidden_exe.jpg"
    spoofed_file.write_text("MZ\x90\x00...", encoding="utf-8")

    mock_security = mock_security_class.return_value
    
    def mock_scan_binary(head_bytes, ext):
        if ext == ".jpg": return {"threat_snippet": "Magic Byte Mismatch: Expected JPEG, got PE32 Executable"}
        return {}
        
    def mock_scan_content(content, limit):
        if "MZ" in content: return {"counts": {"entropy": 6.8, "bitwise_hits": 2}}
        return {"counts": {"entropy": 1.2, "bitwise_hits": 0}}

    mock_security.scan_binary.side_effect = mock_scan_binary
    mock_security.scan_content.side_effect = mock_scan_content

    result = xray_module.run_xray_audit(repo_dir)
    assert result["anomalies_found"] == 1, "Failed to flag magic byte mismatch or high entropy!"

# ==============================================================================
# TEST 3: The Shebang Shield
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.ApertureFilter")
def test_xray_shebang_shield(mock_aperture_class, mock_security_class, tmp_path):
    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_solar_shield.return_value = True
    
    repo_dir = tmp_path / "shebang_repo"
    repo_dir.mkdir()
    
    sh_file = repo_dir / "deploy.sh"
    sh_file.write_text("#!/bin/bash\necho 'Deploying...'", encoding="utf-8")

    mock_security = mock_security_class.return_value
    mock_security.scan_content.return_value = {"counts": {"entropy": 0, "bitwise_hits": 0}}
    mock_security.scan_binary.return_value = {"threat_snippet": "Suspicious execution header: #!/bin/bash"}

    result = xray_module.run_xray_audit(repo_dir)
    assert result["anomalies_found"] == 0, "The Shebang Shield failed!"