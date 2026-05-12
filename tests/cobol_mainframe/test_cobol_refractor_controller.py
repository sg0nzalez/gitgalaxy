import pytest
from pathlib import Path
import sqlite3

# IMPORTANT: Adjust this path to match exactly where your file is located
import gitgalaxy.cobol_refractor_controller as controller_module

# ==============================================================================
# TEST 1: The Scale Sensor (OOM Protection)
# ==============================================================================
def test_scale_sensor_calibration(tmp_path):
    """
    Proves the orchestrator accurately calculates repository mass and dynamically 
    toggles the storage medium to prevent Out-Of-Memory (OOM) crashes.
    """
    repo_dir = tmp_path / "legacy_repo"
    repo_dir.mkdir()
    
    # Create 3 small mock COBOL files
    for i in range(3):
        (repo_dir / f"PGM{i}.cbl").write_text("IDENTIFICATION DIVISION.", encoding="utf-8")
        
    # 1. Test RAM Mode (Thresholds are higher than the payload)
    mode, files = controller_module.calibrate_ir_medium(repo_dir, max_files=5, max_mb=10)
    assert mode == "RAM", "Failed to default to high-speed RAM!"
    assert len(files) == 3
    
    # 2. Test SQLite Mode (Threshold tripped by file count)
    mode, files = controller_module.calibrate_ir_medium(repo_dir, max_files=2, max_mb=10)
    assert mode == "SQLITE", "Scale sensor failed to trip the SQLite safety switch!"

# ==============================================================================
# TEST 2: Hybrid State Manager Parity
# ==============================================================================
def test_ir_state_manager_parity(tmp_path):
    """
    Proves that the IR abstraction layer perfectly mirrors data retrieval 
    whether backed by temporary RAM or a physical SQLite disk database.
    """
    # 1. Initialize RAM Manager
    ram_mgr = controller_module.IRStateManager("RAM", tmp_path)
    ram_mgr.record_dead_code("PGM-ALPHA", dead_paras={"GHOST-PARA"}, orphaned_vars={"DEAD-VAR"})
    
    # 2. Initialize SQLite Manager
    sql_mgr = controller_module.IRStateManager("SQLITE", tmp_path)
    sql_mgr.record_dead_code("PGM-ALPHA", dead_paras={"GHOST-PARA"}, orphaned_vars={"DEAD-VAR"})
    
    # 3. Assert Parity
    assert ram_mgr.get_dead_paras("PGM-ALPHA") == sql_mgr.get_dead_paras("PGM-ALPHA")
    assert ram_mgr.get_orphaned_vars("PGM-ALPHA") == sql_mgr.get_orphaned_vars("PGM-ALPHA")
    
    # 4. Verify SQLite strictly wrote to disk
    assert (tmp_path / "gitgalaxy_ir.db").exists()
    sql_mgr.close()

# ==============================================================================
# TEST 3: Payload Integration Orchestrator
# ==============================================================================
def test_process_payload_integration(tmp_path):
    """
    Proves the orchestrator successfully routes a file through the sub-tools
    (Graveyard Reaper, Lineage Architect, Schema Forge) and aggregates the state.
    """
    cbl_file = tmp_path / "MAINPGM.cbl"
    cbl_file.write_text(
        "       PROGRAM-ID. MAINPGM.\n"
        "       DATA DIVISION.\n"
        "       01 DEAD-VAR PIC X.\n"    # Will trigger Graveyard Reaper
        "       PROCEDURE DIVISION.\n"
        "       MAIN.\n"
        "           DISPLAY 'HELLO'.\n",
        encoding="utf-8"
    )
    
    mgr = controller_module.IRStateManager("RAM", tmp_path)
    ir_state = controller_module.process_payload(cbl_file, mgr)
    
    # 1. Verify Metadata Extraction
    assert ir_state["metadata"]["file_name"] == "MAINPGM.cbl"
    
    # 2. Verify Graveyard Sub-Tool Integration
    assert "DEAD-VAR" in ir_state["analysis"]["graveyard"]["orphaned_vars"], "Orchestrator failed to invoke Graveyard Reaper!"
    
    # 3. Verify Schema Sub-Tool Integration
    assert "schemas" in ir_state["generation"]
    
    # 4. Verify IR State Manager persistence
    assert mgr.get_orphaned_vars("MAINPGM") == {"DEAD-VAR"}, "Orchestrator failed to sync with global IR State Manager!"