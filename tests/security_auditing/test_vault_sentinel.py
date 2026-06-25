import pytest
import sys
from unittest.mock import patch

import gitgalaxy.tools.supply_chain_security.vault_sentinel as sentinel_module

# ==============================================================================
# TEST 1: Denylist Path Evaluation (Immediate Blocking)
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.ApertureFilter")
def test_sentinel_denylist_blocking(
    mock_aperture_class, mock_security_class, tmp_path, monkeypatch
):
    """
    Proves that files matching the DENYLIST_PATTERNS are instantly blocked
    and trigger a pipeline failure without requiring a deep content scan.
    """
    monkeypatch.setattr(sentinel_module, "DENYLIST_PATTERNS", ["*.pem", "id_rsa*"])
    monkeypatch.setattr(sentinel_module, "ALLOWLIST_PATHS", [])

    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_ignore_rules.return_value = True

    repo_dir = tmp_path / "denylist_repo"
    repo_dir.mkdir()
    (repo_dir / "production.pem").write_text("FAKE_CERT_DATA", encoding="utf-8")

    test_args = ["vault_sentinel.py", str(repo_dir)]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as exc:
            sentinel_module.main()
        assert exc.value.code == 1, "Sentinel failed to block a denylisted file pattern."

# ==============================================================================
# TEST 2: Deep Content Inspection (Hardcoded Credential Leaks)
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.ApertureFilter")
def test_sentinel_content_breach(
    mock_aperture_class, mock_security_class, tmp_path, monkeypatch
):
    """
    Proves that seemingly benign files are deeply scanned, and if the SAST engine
    detects private_info signatures, it successfully halts the pipeline.
    """
    monkeypatch.setattr(sentinel_module, "DENYLIST_PATTERNS", [])
    monkeypatch.setattr(sentinel_module, "ALLOWLIST_PATHS", [])

    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_ignore_rules.return_value = True
    mock_aperture.evaluate_path_integrity.return_value = (True, 100, None)

    mock_security = mock_security_class.return_value
    mock_security.scan_content.return_value = {
        "counts": {"hardcoded_secrets": 1},
        "snippets": {"hardcoded_secrets": ["AKIAIOSFODNN7EXAMPLE"]},
    }

    repo_dir = tmp_path / "deepscan_repo"
    repo_dir.mkdir()
    (repo_dir / "database_config.py").write_text(
        "AWS_KEY = 'AKIAIOSFODNN7EXAMPLE'", encoding="utf-8"
    )

    test_args = ["vault_sentinel.py", str(repo_dir)]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as exc:
            sentinel_module.main()

        assert exc.value.code == 1, (
            "Sentinel failed to halt the pipeline on a hardcoded credential detection."
        )

# ==============================================================================
# TEST 3: Allowlist Path Exclusions (Test Key Suppression)
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.ApertureFilter")
def test_sentinel_allowlist_bypass(
    mock_aperture_class, mock_security_class, tmp_path, monkeypatch, capsys
):
    """
    Proves that if a file resides explicitly inside an ALLOWLIST_PATH, it completely
    bypasses both Denylist path checks and Deep Content scanning triggers.
    """
    monkeypatch.setattr(sentinel_module, "DENYLIST_PATTERNS", ["*.pem"])
    monkeypatch.setattr(sentinel_module, "ALLOWLIST_PATHS", ["mock_keys/"])

    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_ignore_rules.return_value = True
    mock_aperture.evaluate_path_integrity.return_value = (
        False,
        100,
        "CRITICAL LEAK: Private Key",
    )

    mock_security = mock_security_class.return_value
    mock_security.scan_content.return_value = {"counts": {"hardcoded_secrets": 5}}

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
        pytest.fail(
            "The Allowlist evaluation failed. A designated test credential triggered a pipeline failure."
        )
        
    captured = capsys.readouterr()
    assert "[ALLOWLIST BYPASS]" in captured.out
    assert "[SUCCESS] No unauthorized secrets detected." in captured.out

# ==============================================================================
# TEST 4: Root Traversal Ignore Rules (Skipping .git / node_modules)
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.ApertureFilter")
def test_ignore_rules_traversal(
    mock_aperture_class, mock_security_class, tmp_path, monkeypatch, capsys
):
    """
    Ensures that os.walk is properly mutated to completely skip directories
    like .git or node_modules that fail the ApertureFilter check.
    """
    monkeypatch.setattr(sentinel_module, "DENYLIST_PATTERNS", [])
    monkeypatch.setattr(sentinel_module, "ALLOWLIST_PATHS", [])

    mock_aperture = mock_aperture_class.return_value
    
    # Configure the mock to reject any directory named '.git'
    def mock_check_ignore(rel_path):
        if ".git" in str(rel_path):
            return False
        return True
        
    mock_aperture._check_ignore_rules.side_effect = mock_check_ignore
    mock_aperture.evaluate_path_integrity.return_value = (True, 100, None)
    
    mock_security = mock_security_class.return_value
    mock_security.scan_content.return_value = {"counts": {"hardcoded_secrets": 0}}

    repo_dir = tmp_path / "ignore_repo"
    repo_dir.mkdir()
    
    # Create a blocked directory with a file that would normally be scanned
    git_dir = repo_dir / ".git"
    git_dir.mkdir()
    (git_dir / "config").write_text("dummy", encoding="utf-8")
    
    # Create an approved directory
    src_dir = repo_dir / "src"
    src_dir.mkdir()
    (src_dir / "main.py").write_text("dummy", encoding="utf-8")

    test_args = ["vault_sentinel.py", str(repo_dir)]
    with patch.object(sys, "argv", test_args):
        sentinel_module.main()

    captured = capsys.readouterr()
    assert "Files Evaluated    : 1" in captured.out, "Failed to skip the .git directory contents during traversal."

# ==============================================================================
# TEST 5: Exception Handling (Unreadable Files)
# ==============================================================================
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.SecurityLens")
@patch("gitgalaxy.tools.supply_chain_security.vault_sentinel.ApertureFilter")
def test_unreadable_file_handling(
    mock_aperture_class, mock_security_class, tmp_path, monkeypatch
):
    """
    Validates that a file generating an I/O or Permission error during reading
    is gracefully skipped without crashing the Sentinel.
    """
    monkeypatch.setattr(sentinel_module, "DENYLIST_PATTERNS", [])
    monkeypatch.setattr(sentinel_module, "ALLOWLIST_PATHS", [])

    mock_aperture = mock_aperture_class.return_value
    mock_aperture._check_ignore_rules.return_value = True
    mock_aperture.evaluate_path_integrity.return_value = (True, 100, None)

    repo_dir = tmp_path / "broken_repo"
    repo_dir.mkdir()
    (repo_dir / "locked.dat").write_text("data", encoding="utf-8")

    test_args = ["vault_sentinel.py", str(repo_dir)]
    
    try:
        with patch.object(sys, "argv", test_args):
            with patch("builtins.open", side_effect=PermissionError("Locked")):
                sentinel_module.main()
    except SystemExit as exc:
        pytest.fail(f"Sentinel failed to gracefully handle file read exception. Exited with {exc.code}")

# ==============================================================================
# TEST 6: CLI Main - Missing Target Validation
# ==============================================================================
def test_main_missing_target(capsys):
    """Proves the CLI catches invalid directories and exits safely."""
    with patch("sys.argv", ["vault_sentinel.py", "non_existent_folder_path_12345"]):
        with pytest.raises(SystemExit) as exc_info:
            sentinel_module.main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Error: Target" in captured.out