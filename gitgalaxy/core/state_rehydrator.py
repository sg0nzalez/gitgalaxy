# ==============================================================================
# state_rehydrator.py
# GitGalaxy: SQLite to RAM Memory Rehydration
# ==============================================================================
import sqlite3
from pathlib import Path
from typing import Dict, Any


class StateRehydrator:
    def __init__(self, db_path: str):
        self.db_path = Path(db_path)

    def load_latest_state(self, repo_name: str) -> Dict[str, Any]:
        """Pulls the most recent commit state from SQLite and rebuilds the RAM dictionary."""
        if not self.db_path.exists():
            print(f"⚠️ No master DB found at {self.db_path}. Cold start required.")
            return None

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # 1. Get the most recent commit hash for this repo
        cursor.execute(
            """
            SELECT commit_hash FROM repo_data 
            WHERE repo_name = ? 
            ORDER BY commit_date DESC LIMIT 1
        """,
            (repo_name,),
        )
        row = cursor.fetchone()

        if not row:
            print(f"⚠️ No scan history found for '{repo_name}'.")
            return None

        latest_hash = row["commit_hash"]
        print(f"🔄 Rehydrating RAM from commit: {latest_hash}")

        # 2. Extract the file physics
        cursor.execute(
            """
            SELECT * FROM file_data 
            WHERE repo_name = ? AND commit_hash = ?
        """,
            (repo_name, latest_hash),
        )

        file_rows = cursor.fetchall()

        # 3. Rebuild the `cryolink` dictionary format
        ram_state = {}
        for f in file_rows:
            rel_path = f["file_path"]

            # Reconstruct the basic RAM state the Delta Engine needs to run the Ripple Effect
            ram_state[rel_path] = {
                "path": rel_path,
                "lang_id": f["language"],
                "total_loc": f["total_loc"],
                "coding_loc": f["coding_loc"],
                "file_impact": f["structural_mass"],
                "control_flow_ratio": f["control_flow_ratio"],
                # Standard initialization for missing data that Delta Engine might need
                "raw_imports": set(),
                "hit_vector": [],
                "telemetry": {
                    "popularity": f["popularity"],
                    "ownership": f["author"],
                    "ai_threat_score": f["ai_threat_score"],
                },
                "dependency_network": {
                    "total_downstream": f["total_downstream"],
                    "total_upstream": f["total_upstream"],
                },
            }

        conn.close()
        return {"commit_hash": latest_hash, "cryolink": ram_state}
