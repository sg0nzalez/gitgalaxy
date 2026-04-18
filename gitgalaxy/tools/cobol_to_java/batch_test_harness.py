#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: Prototyping Batch Test Harness
# Purpose: Stress-tests the entire V4 pipeline (Refractor -> Java -> Maven) 
#          across 'n' legacy repositories. Captures granular debugging logs.
# ==============================================================================
import argparse
import subprocess
import time
import os
from pathlib import Path

def run_command(command: list, cwd: Path) -> tuple[bool, str, str]:
    """Executes a shell command and returns success status + logs."""
    
    # Clone the current environment and force Java 17
    custom_env = os.environ.copy()
    custom_env["JAVA_HOME"] = "/usr/lib/jvm/java-17-openjdk-amd64"
    
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            env=custom_env,  # <--- Inject the environment here
            capture_output=True,
            text=True,
            timeout=300 # 5-minute timeout per command to prevent infinite hangs
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired as e:
        return False, e.stdout.decode('utf-8') if e.stdout else "", "TIMEOUT: Command exceeded 5 minutes."
    except Exception as e:
        return False, "", str(e)

def main():
    parser = argparse.ArgumentParser(description="GitGalaxy Batch Test Harness")
    parser.add_argument("corpus_dir", help="Path to the directory containing legacy COBOL repos")
    parser.add_argument("--n", type=int, default=0, help="Number of repositories to process (0 for all)")
    args = parser.parse_args()

    corpus_path = Path(args.corpus_dir).resolve()
    v6_dir = corpus_path.parents[1] / "v6" / "gitgalaxy" 
    
    reports_dir = corpus_path / "batch_test_reports"
    reports_dir.mkdir(exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    master_log_path = reports_dir / f"master_batch_run_{timestamp}.txt"

    all_dirs = [d for d in corpus_path.iterdir() if d.is_dir()]
    target_repos = [d for d in all_dirs if not ("_gitgalaxy_" in d.name or "batch_test" in d.name)]
    if args.n > 0:
        target_repos = target_repos[:args.n]

    print("\n" + "="*70)
    print(f" 🧪 GITGALAXY BATCH TEST HARNESS ENGAGED")
    print(f" Target Corpus : {corpus_path.name}")
    print(f" Sample Size   : n = {len(target_repos)}")
    print("="*70 + "\n")

    summary = {"passed": 0, "failed_refractor": 0, "failed_java_forge": 0, "failed_maven": 0}

    with open(master_log_path, "w", encoding="utf-8") as master_log:
        master_log.write(f"GITGALAXY BATCH RUN - {timestamp}\nSample Size: {len(target_repos)}\n\n")

        for repo in target_repos:
            print(f"⚙️  Processing: {repo.name} ... ", end="", flush=True)
            master_log.write(f"--- REPO: {repo.name} ---\n")
            repo_error_log = reports_dir / f"{repo.name}_error_{timestamp}.log"

            # STEP 1
            cmd1 = ["python", str(v6_dir / "cobol_refractor_controller.py"), repo.name]
            success1, out1, err1 = run_command(cmd1, cwd=corpus_path)
            if not success1:
                print("❌ FAILED (Refractor Phase)")
                print("\n" + "-"*40 + " LAST 15 LINES OF STDERR " + "-"*40)
                print("\n".join(err1.splitlines()[-15:]))
                print("-" * 105 + "\n")
                summary["failed_refractor"] += 1
                repo_error_log.write_text(f"--- REFRACTOR STDERR ---\n{err1}\n\n--- STDOUT ---\n{out1}")
                continue

            clean_dirs = sorted(corpus_path.glob(f"{repo.name}_gitgalaxy_clean_*"), key=lambda p: p.stat().st_mtime, reverse=True)
            if not clean_dirs: continue
            clean_room = clean_dirs[0]

            # STEP 2
            cmd2 = ["python", str(v6_dir / "cobol_to_java_controller.py"), clean_room.name]
            success2, out2, err2 = run_command(cmd2, cwd=corpus_path)
            if not success2:
                print("❌ FAILED (Java Forge Phase)")
                print("\n" + "-"*40 + " LAST 15 LINES OF STDERR " + "-"*40)
                print("\n".join(err2.splitlines()[-15:]))
                print("-" * 105 + "\n")
                summary["failed_java_forge"] += 1
                repo_error_log.write_text(f"--- JAVA FORGE STDERR ---\n{err2}\n\n--- STDOUT ---\n{out2}")
                continue

            java_dirs = sorted(corpus_path.glob(f"{repo.name}_gitgalaxy_java_spring_*"), key=lambda p: p.stat().st_mtime, reverse=True)
            if not java_dirs: continue
            java_dir = java_dirs[0]

            # STEP 3
            cmd3 = ["mvn", "clean", "compile"]
            success3, out3, err3 = run_command(cmd3, cwd=java_dir)
            if not success3:
                print("❌ FAILED (Maven Compilation)")
                print("\n" + "-"*40 + " LAST 15 LINES OF MAVEN LOG " + "-"*40)
                # Maven puts compilation errors in stdout, not stderr!
                print("\n".join(out3.splitlines()[-15:])) 
                print("-" * 105 + "\n")
                summary["failed_maven"] += 1
                repo_error_log.write_text(f"--- MAVEN STDERR/STDOUT ---\n{out3}\n{err3}")
                continue

            print("✅ SUCCESS (Fully Compiled)")
            summary["passed"] += 1

        print("\n" + "="*70)
        print(" 🏁 BATCH TEST COMPLETE")
        print("----------------------------------------------------------------------")
        print(f"  • Perfect Successes    : {summary['passed']}/{len(target_repos)}")
        print(f" 📁 Master Log  : {master_log_path}")
        print("======================================================================\n")

if __name__ == "__main__":
    main()