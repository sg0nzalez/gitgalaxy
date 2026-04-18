#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: Full API Network Map
# Purpose: Hunts down undocumented "Shadow APIs" by comparing physical 
#          source code routers against official OpenAPI/Swagger documentation.
# ==============================================================================
import argparse
import sys
import re
import json
import yaml  # Added to support .yaml Swagger files
from pathlib import Path
from collections import defaultdict

# ==============================================================================
# 1. THE ROUTER PHYSICS (FRAMEWORK REGEX TRAPS)
# ==============================================================================
FRAMEWORK_TRAPS = {
    "Python (FastAPI/Flask)": {
        "ext": [".py"],
        "regex": re.compile(r'@(?:app|router)\.(get|post|put|delete|patch)\s*\(\s*["\'](.*?)["\']', re.IGNORECASE)
    },
    "Node.js (Express)": {
        "ext": [".js", ".ts"],
        "regex": re.compile(r'(?:app|router)\.(get|post|put|delete|patch)\s*\(\s*["\'](.*?)["\']', re.IGNORECASE)
    },
    "Java (Spring Boot)": {
        "ext": [".java"],
        "regex": re.compile(r'@(Get|Post|Put|Delete|Patch)Mapping\s*\(\s*(?:value\s*=\s*)?["\'](.*?)["\']\)', re.IGNORECASE)
    },
    "Golang (Gorilla/Mux/Gin)": {
        "ext": [".go"],
        "regex": re.compile(r'\.(?:GET|POST|PUT|DELETE|PATCH|HandleFunc)\s*\(\s*["\'](.*?)["\']', re.IGNORECASE)
    }
}

def parse_official_swagger(swagger_path: Path) -> set:
    """Parses the official security documentation to find 'Approved' APIs."""
    approved_apis = set()
    try:
        with open(swagger_path, 'r', encoding='utf-8') as f:
            # Universally handle both JSON and YAML blueprints
            if swagger_path.suffix.lower() in ['.yaml', '.yml']:
                swagger_data = yaml.safe_load(f)
            else:
                swagger_data = json.load(f)
            
        paths = swagger_data.get('paths', {})
        for api_path, methods in paths.items():
            for method in methods.keys():
                # Normalize to "METHOD /path" (e.g., "GET /api/users")
                approved_apis.add(f"{method.upper()} {api_path}")
    except Exception as e:
        print(f" ❌ Error reading Swagger file: {e}")
        sys.exit(1)
        
    return approved_apis

def map_physical_codebase(target_dir: Path) -> dict:
    """Rips through the source code to find every API endpoint actually compiled."""
    physical_apis = defaultdict(list)
    
    for filepath in target_dir.rglob("*"):
        if not filepath.is_file():
            continue
            
        for framework, config in FRAMEWORK_TRAPS.items():
            if filepath.suffix in config["ext"]:
                try:
                    content = filepath.read_text(encoding='utf-8', errors='ignore')
                    hits = config["regex"].findall(content)
                    for method, api_path in hits:
                        # Normalize to "METHOD /path"
                        endpoint = f"{method.upper()} {api_path}"
                        physical_apis[endpoint].append(filepath.name)
                except Exception:
                    pass
                    
    return physical_apis

def main():
    parser = argparse.ArgumentParser(description="GitGalaxy Full API Network Map")
    parser.add_argument("source", help="Directory containing the application source code")
    parser.add_argument("--swagger", required=True, help="Path to the official swagger.json file")
    args = parser.parse_args()

    source_path = Path(args.source).resolve()
    swagger_path = Path(args.swagger).resolve()

    if not source_path.exists() or not swagger_path.exists():
        print("Error: Target source directory or Swagger file does not exist.")
        sys.exit(1)

    print(f"🗺️ GitGalaxy Network Mapper analyzing physical endpoints in: {source_path.name}...\n")

    # 1. Extract the Truth
    approved_apis = parse_official_swagger(swagger_path)
    physical_apis_map = map_physical_codebase(source_path)
    physical_endpoints = set(physical_apis_map.keys())

    # 2. The Math (Set Theory)
    shadow_apis = physical_endpoints - approved_apis
    ghost_apis = approved_apis - physical_endpoints # Documented, but don't exist in code

    # 3. Presentation Dashboard
    print("==========================================================")
    print(" 📡 SHADOW API SECURITY AUDIT")
    print("==========================================================")
    print(f" Documented Endpoints (Swagger) : {len(approved_apis)}")
    print(f" Physical Endpoints (Source)    : {len(physical_endpoints)}")
    print("-" * 58)

    if shadow_apis:
        print(f" 🚨 SHADOW APIS DETECTED: {len(shadow_apis)} (Critical Risk)")
        for api in sorted(shadow_apis):
            files = ", ".join(set(physical_apis_map[api]))
            print(f"    ↳ {api.ljust(25)} [Found in: {files}]")
    else:
        print(" ✅ No Shadow APIs detected. Codebase matches documentation.")

    print("\n----------------------------------------------------------")
    if ghost_apis:
        print(f" 👻 GHOST APIS DETECTED: {len(ghost_apis)} (Documentation Bloat)")
        for api in sorted(ghost_apis):
            print(f"    ↳ {api.ljust(25)} [Missing from source code]")
    else:
        print(" ✅ No Ghost APIs detected.")
        
    print("==========================================================\n")

if __name__ == "__main__":
    main()