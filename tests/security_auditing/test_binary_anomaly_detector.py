import os
import sys
import pytest
import importlib
from unittest.mock import patch, MagicMock

import gitgalaxy.tools.supply_chain_security.binary_anomaly_detector as xray_module


# ==============================================================================
# TEST 1: The Routing Matrix (Denylist vs Allowlist vs Test Folders)
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.ApertureFilter")
def test_xray_routing_matrix(
    mock_aperture_class, mock_security_class, tmp_path, monkeypatch
):
    monkeypatch.setattr(xray_module, "DENYLIST_PATTERNS", ["*.key", "*.pem", "id_rsa*"])
    monkeypatch.setattr(xray_module, "XRAY_BYPASS_EXTENSIONS", [".gz", ".zip"])
    monkeypatch.setattr(xray_module, "ALLOWLIST_PATHS", ["approved_keys/"])

    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_solar_shield.return_value = True

    mock_security = mock_security_class.return_value
    mock_security.scan_content.return_value = {
        "counts": {"entropy": 6.5, "bitwise_hits": 0}
    }
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
    src_dir = repo_dir / "src"
    src_dir.mkdir()
    test_dir = src_dir / "tests"
    test_dir.mkdir()
    (test_dir / "mock_payload.dat").write_text(
        "FAKE_HIGH_ENTROPY_DATA", encoding="utf-8"
    )

    result = xray_module.run_xray_audit(repo_dir)
    assert (
        result["anomalies_found"] == 1
    ), "The routing matrix failed! Check Denylist/Allowlist math."


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
        if ext == ".jpg":
            return {
                "threat_snippet": "Magic Byte Mismatch: Expected JPEG, got PE32 Executable"
            }
        return {}

    def mock_scan_content(content, limit):
        if "MZ" in content:
            return {"counts": {"entropy": 6.8, "bitwise_hits": 2}}
        return {"counts": {"entropy": 1.2, "bitwise_hits": 0}}

    mock_security.scan_binary.side_effect = mock_scan_binary
    mock_security.scan_content.side_effect = mock_scan_content

    result = xray_module.run_xray_audit(repo_dir)
    assert (
        result["anomalies_found"] == 1
    ), "Failed to flag magic byte mismatch or high entropy!"


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
    mock_security.scan_content.return_value = {
        "counts": {"entropy": 0, "bitwise_hits": 0}
    }
    mock_security.scan_binary.return_value = {
        "threat_snippet": "Suspicious execution header: #!/bin/bash"
    }

    result = xray_module.run_xray_audit(repo_dir)
    assert result["anomalies_found"] == 0, "The Shebang Shield failed!"


# ==============================================================================
# TEST 4: I/O Exception Handling (Programmatic Entry)
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.ApertureFilter")
def test_xray_run_audit_exception(mock_aperture_class, mock_security_class, tmp_path):
    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_solar_shield.return_value = True

    repo_dir = tmp_path / "broken_audit"
    repo_dir.mkdir()
    (repo_dir / "locked.dat").write_text("data", encoding="utf-8")

    with patch("builtins.open", side_effect=PermissionError("Locked")):
        result = xray_module.run_xray_audit(repo_dir)

    assert (
        result["anomalies_found"] == 0
    ), "Failed to gracefully catch exception in run_xray_audit!"


# ==============================================================================
# TEST 5: CLI Main - Missing Target Trap
# ==============================================================================
def test_main_missing_target(capsys):
    """Proves the CLI catches invalid directories and exits safely."""
    with patch("sys.argv", ["xray", "non_existent_folder_path_12345"]):
        with pytest.raises(SystemExit) as exc_info:
            xray_module.main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Error: Target" in captured.out


# ==============================================================================
# TEST 6: CLI Main - Clean Run & Allowlist Bypasses
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.ApertureFilter")
def test_main_clean_run(
    mock_aperture_class, mock_security_class, tmp_path, monkeypatch, capsys
):
    """Proves a clean repository successfully logs completion without raising SystemExit."""
    monkeypatch.setattr(xray_module, "ALLOWLIST_PATHS", ["approved/"])
    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_solar_shield.return_value = True

    mock_security = mock_security_class.return_value
    mock_security.scan_binary.return_value = {}

    # We must trigger an anomaly in the bypassed file so the engine logs it as 'allowed'
    def mock_scan_content(content, limit):
        if "bypassed" in content:
            return {"counts": {"entropy": 6.0, "bitwise_hits": 0}}
        return {"counts": {"entropy": 0, "bitwise_hits": 0}}

    mock_security.scan_content.side_effect = mock_scan_content

    repo_dir = tmp_path / "clean_repo_cli"
    repo_dir.mkdir()

    (repo_dir / "safe.txt").write_text("safe", encoding="utf-8")

    approved_dir = repo_dir / "approved"
    approved_dir.mkdir()
    (approved_dir / "bypassed.key").write_text("bypassed", encoding="utf-8")

    with patch("sys.argv", ["xray", str(repo_dir)]):
        xray_module.main()

    captured = capsys.readouterr()
    assert (
        "ALL CLEAR: No encrypted payloads or binary anomalies detected." in captured.out
    )
    assert "known mock/safe files were bypassed via configuration." in captured.out


# ==============================================================================
# TEST 7: CLI Main - Anomaly Detected (System Exit 1)
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.ApertureFilter")
def test_main_anomaly_detected(
    mock_aperture_class, mock_security_class, tmp_path, monkeypatch, capsys
):
    """Proves the CLI detects active anomalies, blocks the commit, and logs the triage alert."""
    monkeypatch.setattr(xray_module, "DENYLIST_PATTERNS", ["*.forbidden"])
    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_solar_shield.return_value = True

    repo_dir = tmp_path / "threat_repo_cli"
    repo_dir.mkdir()

    (repo_dir / "bad.forbidden").write_text("bad", encoding="utf-8")
    (repo_dir / "encrypted.dat").write_text("HIGH ENTROPY", encoding="utf-8")

    mock_security = mock_security_class.return_value
    mock_security.scan_binary.return_value = {}
    mock_security.scan_content.side_effect = lambda content, limit: (
        {"counts": {"entropy": 5.0, "bitwise_hits": 1}}
        if "HIGH ENTROPY" in content
        else {"counts": {}}
    )

    with patch("sys.argv", ["xray", str(repo_dir)]):
        with pytest.raises(SystemExit) as exc_info:
            xray_module.main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "TRIAGE ALERT" in captured.out
    assert "[FORBIDDEN FILE BREACH]" in captured.out
    assert "[ANOMALY DETECTED]" in captured.out


# ==============================================================================
# TEST 8: CLI Main - Exception Catch
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.binary_anomaly_detector.ApertureFilter")
def test_main_file_read_exception(mock_aperture_class, mock_security_class, tmp_path):
    """Triggers the generic 'except Exception: pass' inside the deep scan loop of main()."""
    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_solar_shield.return_value = True

    repo_dir = tmp_path / "broken_main"
    repo_dir.mkdir()
    (repo_dir / "unreadable.dat").write_text("data", encoding="utf-8")

    with patch("sys.argv", ["xray", str(repo_dir)]):
        with patch("builtins.open", side_effect=PermissionError("Locked")):
            xray_module.main()


# ==============================================================================
# TEST 9: Module Import Fallback Configuration
# ==============================================================================
def test_xray_import_fallback():
    """Proves the module gracefully degrades if custom bypass arrays are missing from config."""
    # Stash the original module
    original_config = sys.modules.get("gitgalaxy.standards.gitgalaxy_config")

    # Create a mock module that ONLY has APERTURE_CONFIG (simulating a fresh install)
    mock_config = type(sys)("gitgalaxy.standards.gitgalaxy_config")
    mock_config.APERTURE_CONFIG = {}
    sys.modules["gitgalaxy.standards.gitgalaxy_config"] = mock_config

    # Force a reload to trigger the ImportError bypass block (Lines 24-29)
    importlib.reload(xray_module)

    assert (
        xray_module.ALLOWLIST_PATHS == []
    ), "Fallback failed to initialize empty Allowlist!"
    assert (
        xray_module.DENYLIST_PATTERNS == []
    ), "Fallback failed to initialize empty Denylist!"

    # Restore reality
    if original_config:
        sys.modules["gitgalaxy.standards.gitgalaxy_config"] = original_config
    importlib.reload(xray_module)
