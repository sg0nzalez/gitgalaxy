import pytest
import logging
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

from gitgalaxy.physics.chronometer import Chronometer


# ==============================================================================
# TEST 1: NO GIT FALLBACK & OS WALK (Lines 45-46, 74-95, 295-296)
# ==============================================================================
@patch("gitgalaxy.physics.chronometer.subprocess.run")
@patch("gitgalaxy.physics.chronometer.os.walk")
@patch("gitgalaxy.physics.chronometer.os.path.getmtime")
def test_chronometer_no_git_fallback(mock_getmtime, mock_walk, mock_run, tmp_path):
    """Proves the chronometer gracefully falls back to OS Walk if Git is missing."""
    # Simulate Git binary not found
    mock_run.side_effect = FileNotFoundError()

    # Simulate an OS walk returning some files
    mock_walk.return_value = [(str(tmp_path), ["dir1"], ["file1.txt", "file2.txt"])]
    # Provide fake modification times to establish boundaries
    mock_getmtime.side_effect = [1000.0, 2000.0, 1000.0, 2000.0]

    # Initialize without a parent logger to trigger the root logger fallback (Lines 45-46)
    chrono = Chronometer(tmp_path)

    assert not chrono.is_resilient, "Failed to degrade to non-resilient OS mode!"
    assert chrono.repo_min_time == 1000.0, "Failed to set min boundary from OS walk!"
    assert chrono.repo_max_time == 2000.0, "Failed to set max boundary from OS walk!"
    assert "file1.txt" in chrono.mtime_map, "Failed to map files via OS fallback!"


# ==============================================================================
# TEST 2: GIT BOUNDARY SURVEY (Lines 106-146)
# ==============================================================================
@patch("gitgalaxy.physics.chronometer.subprocess.run")
def test_chronometer_git_boundaries(mock_run, tmp_path):
    """Proves the boundary scanner correctly extracts min/max times from git logs."""

    # Simulate the .git directory existing so the hardware check fires
    (tmp_path / ".git").mkdir()

    def git_side_effect(cmd, **kwargs):
        m = MagicMock()
        m.stdout = ""
        if "--version" in cmd:
            m.stdout = "git version 2.40.0\n"
        elif "log" in cmd and "-1" in cmd and "HEAD" not in cmd and len(cmd) == 4:
            m.stdout = "5000\n"  # Max Time
        elif "rev-list" in cmd:
            m.stdout = "abc123hash\n"  # First Commit Hash
        elif "log" in cmd and "abc123hash" in cmd:
            m.stdout = "1000\n"  # Min Time
        elif "ls-files" in cmd:
            m.stdout = "src/main.py\n"  # Fake tracking
        return m

    mock_run.side_effect = git_side_effect

    # Block the actual Popen log streaming so we just test the boundaries
    with patch("gitgalaxy.physics.chronometer.subprocess.Popen"):
        chrono = Chronometer(tmp_path, parent_logger=logging.getLogger("test"))

    assert chrono.is_resilient, "Failed to verify Git hardware!"
    assert chrono.repo_max_time == 5000.0, "Failed to extract Max Time!"
    assert chrono.repo_min_time == 1000.0, "Failed to extract Min Time via rev-list!"


# ==============================================================================
# TEST 3: IGNORED REVS LOADING (Lines 150-164)
# ==============================================================================
def test_load_ignored_revs(tmp_path):
    """Proves the sensor strips cosmetic commits from the churn math."""
    ignore_file = tmp_path / ".git-blame-ignore-revs"
    ignore_file.write_text("# This is a cosmetic styling commit\nabc123\ndef456\n")

    # Bypass the initialization sequence so we can test the specific method
    with patch.object(Chronometer, "_calibrate_temporal_field"):
        chrono = Chronometer(tmp_path)
        ignored = chrono._load_ignored_revs()

        assert "abc123" in ignored
        assert "def456" in ignored
        assert "# This is a cosmetic styling commit" not in ignored


# ==============================================================================
# TEST 4: LOG ESCALATOR EDGE CASES (Lines 172-217, 248-249, 261-262, 270, 273)
# ==============================================================================
@patch("gitgalaxy.physics.chronometer.subprocess.run")
@patch("gitgalaxy.physics.chronometer.subprocess.Popen")
def test_hybrid_log_scan_and_escalator(mock_popen, mock_run, tmp_path):
    """Proves the Popen stream handles quoted paths, skipped hashes, and empty lines."""
    # 1. Mock ls-files
    mock_run.return_value = MagicMock(stdout="src/main.py\nsrc/utils.py\n")

    # 2. Mock Popen stream output with hostile edge cases
    mock_process = MagicMock()
    mock_stdout = MagicMock()
    mock_stdout.__iter__.return_value = [
        "hash1|1000|Alice\n",
        '"src/main.py"\n',  # Quoted path trap
        "\n",  # Empty line trap
        "hash_ignored|2000|Bob\n",
        "src/utils.py\n",  # Should be skipped entirely because the hash is ignored!
    ]
    mock_process.stdout = mock_stdout
    mock_popen.return_value = mock_process

    with patch.object(Chronometer, "_calibrate_temporal_field"):
        chrono = Chronometer(tmp_path)
        chrono.is_resilient = True
        chrono.repo_max_time = 5000

        # Inject our ignored hash
        with patch.object(chrono, "_load_ignored_revs", return_value={"hash_ignored"}):
            chrono._ignite_hybrid_log_scan()

        # Verify the quoted path was stripped and mapped
        assert "src/main.py" in chrono.entropy_map, "Failed to strip quotes from path!"
        assert chrono.entropy_map["src/main.py"] == 1
        assert chrono.author_map["src/main.py"]["Alice"] == 1

        # Verify the ignored hash skipped the subsequent file
        assert "src/utils.py" not in chrono.entropy_map, "Failed to skip ignored commit hash!"


# ==============================================================================
# TEST 5: TEMPORAL SIGNAL HANDOVER (Lines 311-317, 324-337)
# ==============================================================================
@patch("gitgalaxy.physics.chronometer.os.path.getmtime")
def test_get_temporal_signals(mock_getmtime, tmp_path):
    """Proves the Handover method returns cache hits and falls back cleanly."""
    with patch.object(Chronometer, "_calibrate_temporal_field"):
        chrono = Chronometer(tmp_path)
        chrono.repo_min_time = 100
        chrono.repo_max_time = 500
        chrono.is_resilient = True

        # Pre-mapped file (Cache Hit)
        chrono.mtime_map["mapped.py"] = 300.0
        chrono.entropy_map["mapped.py"] = 5
        chrono.author_map["mapped.py"] = {"Alice": 5}

        sig1 = chrono.get_temporal_signals("mapped.py")
        assert sig1["commit_count"] == 5
        assert sig1["mtime"] == 300.0

        # Unmapped file -> Falls back to live OS check
        mock_getmtime.return_value = 400.0
        sig2 = chrono.get_temporal_signals("unmapped.py")
        assert sig2["commit_count"] == 0
        assert sig2["mtime"] == 400.0
        mock_getmtime.assert_called_once()

        # Unmapped ghost file -> Falls back to repo_max_time if OS throws OSError
        mock_getmtime.side_effect = OSError()
        sig3 = chrono.get_temporal_signals("ghost.py")
        assert sig3["mtime"] == 500
