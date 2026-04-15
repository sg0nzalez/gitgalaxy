#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy: COBOL Refractor Controller
# Purpose: Wraps the Universal Translator suite, executing JCL Forge, DAG Architect,
#          Graveyard Finder, and Schema Forge, outputting to a clean artifact folder.
# ==============================================================================
import argparse
import sys
import subprocess
from pathlib import Path
from datetime import datetime

# Map the paths to the tools in your /tools directory
TOOL_DIR = Path(__file__).parent / "tools"
JCL_FORGE = TOOL_DIR / "jcl_forge.py"
DAG_ARCHITECT = TOOL_DIR / "dag_architect.py"
GRAVEYARD_FINDER = TOOL_DIR / "cobol_graveyard_finder.py"
SCHEMA_FORGE = TOOL_DIR / "cobol_schema_forge.py"

def run_engine(command: list, output_file: Path = None):
    """Executes a GitGalaxy tool and optionally routes its output to a file."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        if output_file:
            output_file.write_text(result.stdout, encoding='utf-8')
        return True
    except subprocess.CalledProcessError as e:
        print(f" ❌ Error running {' '.join(command[:2])}:")
        print(e.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="GitGalaxy COBOL Refractor Controller")
    parser.add_argument("target", help="The legacy repository or directory to scan")
    args = parser.parse_args()

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print(f"Error: Target {target_path} does not exist.")
        sys.exit(1)

    # Create the Clean-Room parallel directory right next to the target
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    clean_dir = target_path.parent / f"{target_path.name}_gitgalaxy_clean_{timestamp}"
    
    # Define the sub-architecture
    jcl_dir = clean_dir / "01_zero_trust_jcls"
    dag_dir = clean_dir / "02_execution_dags"
    schema_dir = clean_dir / "03_cloud_schemas"
    report_dir = clean_dir / "04_audit_reports"

    # Build the folder tree
    for d in [jcl_dir, dag_dir, schema_dir, report_dir]:
        d.mkdir(parents=True, exist_ok=True)

    print("\n" + "="*70)
    print(" 🚀 COBOL REFRACTOR CONTROLLER ENGAGED")
    print(f" Target: {target_path.name}")
    print(f" Forging Clean-Room Artifacts at: {clean_dir.name}")
    print("="*70 + "\n")

    # ---------------------------------------------------------
    # Phase 1: JCL Forge (Zero-Trust Boundaries)
    # ---------------------------------------------------------
    print(" [1/4] Minting Zero-Trust JCL Sandboxes...")
    run_engine([sys.executable, str(JCL_FORGE), str(target_path), "--out", str(jcl_dir)])
    print(f"       ✅ Saved to {jcl_dir.name}/\n")

    # ---------------------------------------------------------
    # Phase 2: DAG Architect (Pipeline Generation)
    # ---------------------------------------------------------
    print(" [2/4] Mapping Data Lineage and Execution DAGs...")
    dag_report = dag_dir / "master_execution_pipeline.txt"
    run_engine([sys.executable, str(DAG_ARCHITECT), str(target_path)], output_file=dag_report)
    print(f"       ✅ Saved pipeline to {dag_report.name}\n")

    # ---------------------------------------------------------
    # Phase 3: Graveyard Finder (Dead Code Isolation)
    # ---------------------------------------------------------
    print(" [3/4] Reaping Dead Code and Orphaned Memory...")
    reaper_report = report_dir / "dead_code_elimination_report.txt"
    run_engine([sys.executable, str(GRAVEYARD_FINDER), str(target_path)], output_file=reaper_report)
    print(f"       ✅ Saved report to {reaper_report.name}\n")

    # ---------------------------------------------------------
    # Phase 4: Schema Forge (Cloud DDL Generation)
    # ---------------------------------------------------------
    print(" [4/4] Forging Cloud Database Schemas (PostgreSQL & JSON)...")
    cobol_files = list(target_path.rglob("*.cbl")) + list(target_path.rglob("*.cpy")) + list(target_path.rglob("*.cob"))
    schemas_generated = 0
    
    for file_path in cobol_files:
        schema_output = schema_dir / f"{file_path.stem}_schema.txt"
        
        # We capture the output. If it's mostly empty (no schemas), we don't save the text file
        result = subprocess.run([sys.executable, str(SCHEMA_FORGE), str(file_path)], capture_output=True, text=True)
        if "🐘 POSTGRESQL DDL" in result.stdout:
            schema_output.write_text(result.stdout, encoding='utf-8')
            schemas_generated += 1

    print(f"       ✅ Forged {schemas_generated} database schemas into {schema_dir.name}/\n")

    # ---------------------------------------------------------
    # Final Output
    # ---------------------------------------------------------
    print("="*70)
    print(" 🏁 REFRACTION COMPLETE: GitGalaxy Clean-Room successfully generated.")
    print(f" 📁 Location: {clean_dir}")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()