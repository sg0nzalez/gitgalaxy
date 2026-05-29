import pytest
import sys
from pathlib import Path
from unittest.mock import patch

import gitgalaxy.tools.supply_chain_security.vault_sentinel as sentinel_module


# ==============================================================================
# TEST 1: The Denylist Wall (Immediate Path Blocking)
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.ApertureFilter")
def test_sentinel_denylist_blocking(mock_aperture_class, mock_security_class, tmp_path, monkeypatch):
    """
    Proves that files matching the DENYLIST_PATTERNS are instantly blocked
    and trigger a fatal exit without needing a deep content scan.
    """
    monkeypatch.setattr(sentinel_module, "DENYLIST_PATTERNS", ["*.pem", "id_rsa*"])
    monkeypatch.setattr(sentinel_module, "ALLOWLIST_PATHS", [])

    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_solar_shield.return_value = True

    repo_dir = tmp_path / "denylist_repo"
    repo_dir.mkdir()
    (repo_dir / "production.pem").write_text("FAKE_CERT_DATA", encoding="utf-8")

    test_args = ["vault_sentinel.py", str(repo_dir)]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as exc:
            sentinel_module.main()
        assert exc.value.code == 1, "Sentinel failed to block a DENYLIST file pattern!"


# ==============================================================================
# TEST 2: The Deep Scan Trap (Hardcoded Content Leaks)
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.ApertureFilter")
def test_sentinel_content_breach(mock_aperture_class, mock_security_class, tmp_path, monkeypatch):
    """
    Proves that seemingly benign files are deeply scanned, and if the SecurityLens
    detects private_info, it successfully crashes the build.
    """
    monkeypatch.setattr(sentinel_module, "DENYLIST_PATTERNS", [])
    monkeypatch.setattr(sentinel_module, "ALLOWLIST_PATHS", [])

    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_solar_shield.return_value = True
    mock_aperture.evaluate_path_integrity.return_value = (True, 100, None)

    mock_security = mock_security_class.return_value
    mock_security.scan_content.return_value = {
        "counts": {"private_info": 1},
        "snippets": {"private_info": ["AKIAIOSFODNN7EXAMPLE"]},
    }

    repo_dir = tmp_path / "deepscan_repo"
    repo_dir.mkdir()
    (repo_dir / "database_config.py").write_text("AWS_KEY = 'AKIAIOSFODNN7EXAMPLE'", encoding="utf-8")

    test_args = ["vault_sentinel.py", str(repo_dir)]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as exc:
            sentinel_module.main()

        assert exc.value.code == 1, "Sentinel failed to crash the build on a hardcoded secret!"


# ==============================================================================
# TEST 3: The Allowlist Bypass (Mock/Test Key Suppression)
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.ApertureFilter")
def test_sentinel_allowlist_bypass(mock_aperture_class, mock_security_class, tmp_path, monkeypatch):
    """
    Proves that if a file is explicitly inside an ALLOWLIST_PATH, it completely
    bypasses both Denylist crashes and Content Scan crashes.
    """
    monkeypatch.setattr(sentinel_module, "DENYLIST_PATTERNS", ["*.pem"])
    monkeypatch.setattr(sentinel_module, "ALLOWLIST_PATHS", ["mock_keys/"])

    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_solar_shield.return_value = True
    mock_aperture.evaluate_path_integrity.return_value = (
        False,
        100,
        "CRITICAL LEAK: Private Key",
    )

    mock_security = mock_security_class.return_value
    mock_security.scan_content.return_value = {"counts": {"private_info": 5}}

    repo_dir = tmp_path / "allowlist_repo"
    repo_dir.mkdir()

    mock_dir = repo_dir / "mock_keys"
    mock_dir.mkdir()
    (mock_dir / "dummy_test.pem").write_text("FAKE_KEY_DATA", encoding="utf-8")

    test_args = ["vault_sentinel.py", str(repo_dir)]

    try:
        with patch.object(sys, "argv", test_args):
            sentinel_module.main()
    except SystemExit:
        pytest.fail("The Allowlist Bypass failed! A whitelisted test key crashed the build.")
