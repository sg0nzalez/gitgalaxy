#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: Java Spring Service Forge
# Purpose: Scaffolds the @Service class and auto-wires cross-service dependencies 
#          discovered via the global DAG (lineage).
# ==============================================================================
import argparse
import sys
import json
from pathlib import Path

def generate_service_skeleton(ir_state: dict, package_name: str) -> str:
    prog_id = ir_state.get("metadata", {}).get("file_name", "Unknown").split('.')[0]
    camel_prog = "".join(word.capitalize() for word in prog_id.split('-'))
    
    analysis = ir_state.get("analysis", {})
    lineage = analysis.get("lineage", {})
    unresolved_calls = lineage.get("unresolved_calls", [])
    
    java = []
    java.append(f"package {package_name}.service;\n")
    java.append("import org.springframework.stereotype.Service;")
    java.append("import lombok.RequiredArgsConstructor;")
    java.append("import org.slf4j.Logger;")
    java.append("import org.slf4j.LoggerFactory;\n")
    
    java.append("@Service")
    java.append("@RequiredArgsConstructor")
    java.append(f"public class {camel_prog}Service {{\n")
    
    java.append(f"    private static final Logger log = LoggerFactory.getLogger({camel_prog}Service.class);\n")
    
    # Cross-Service Dependency Injection (Commented out to prevent compile errors for missing modules)
    if unresolved_calls:
        java.append("    // \u26A0\uFE0F UNRESOLVED EXTERNAL DEPENDENCIES (FROM DAG)")
        for call in unresolved_calls:
            call_camel = "".join(word.capitalize() for word in call.split('-'))
            java.append(f"    // TODO: AI AGENT - Implement or mock call to: {call_camel}Service")
        java.append("")
        
    java.append(f"    public void execute{camel_prog}(/* Parameters mapped from Controller */) {{")
    java.append(f'        log.info("Executing legacy business logic for {prog_id}");')
    java.append("        // TODO: [AI AGENT] Implement extracted business rules here.")
    java.append("    }\n}")
    
    return "\n".join(java)

def main():
    parser = argparse.ArgumentParser(description="GitGalaxy Service Skeleton Forge")
    parser.add_argument("ir_file", help="Path to the GitGalaxy _ir.json state dump")
    parser.add_argument("--pkg", default="com.gitgalaxy.modernized", help="Base Java package name")
    args = parser.parse_args()

    ir_path = Path(args.ir_file).resolve()
    if not ir_path.exists():
        sys.exit(1)

    try:
        ir_state = json.loads(ir_path.read_text(encoding='utf-8'))
        java_code = generate_service_skeleton(ir_state, args.pkg)
        prog_id = ir_state.get("metadata", {}).get("file_name", "Unknown").split('.')[0].capitalize()
        out_path = ir_path.parent / f"{prog_id}Service.java"
        out_path.write_text(java_code, encoding='utf-8')
        print(f"⚙️ Service Skeleton Forged: {out_path.name}")
    except Exception as e:
        print(f"Error forging Service: {e}")

if __name__ == "__main__":
    main()
