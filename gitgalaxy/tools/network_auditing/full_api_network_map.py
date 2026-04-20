#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: Full API Network Map (Extended Frameworks & Auto-Discovery)
# Purpose: Hunts down undocumented "Shadow APIs" by comparing physical 
#          source code routers against official OpenAPI/Swagger documentation.
# ==============================================================================
import argparse
import sys
import re
import json
import yaml
from pathlib import Path
from collections import defaultdict

# ==============================================================================
# 1. THE ROUTER PHYSICS (EXPANDED FRAMEWORK REGEX TRAPS)
# ==============================================================================
FRAMEWORK_TRAPS = {
    "Python (FastAPI/Flask/Django)": {
        "ext": [".py"],
        "regex": re.compile(r'@(?:app|router|bp)\.(get|post|put|delete|patch)\s*\(\s*["\'](.*?)["\']', re.IGNORECASE)
    },
    "Node.js (Express/Fastify/Koa)": {
        "ext": [".js", ".ts"],
        "regex": re.compile(r'(?:app|router|server)\.(get|post|put|delete|patch)\s*\(\s*["\'](.*?)["\']', re.IGNORECASE)
    },
    "Java (Spring Boot)": {
        "ext": [".java"],
        "regex": re.compile(r'@(Get|Post|Put|Delete|Patch)Mapping\s*\(\s*(?:value\s*=\s*)?["\'](.*?)["\']\)', re.IGNORECASE)
    },
    "Golang (Gorilla/Mux/Gin/Fiber)": {
        "ext": [".go"],
        "regex": re.compile(r'\.(GET|POST|PUT|DELETE|PATCH)\s*\(\s*["\'](.*?)["\']', re.IGNORECASE)
    },
    "C# (.NET Controllers)": {
        "ext": [".cs"],
        "regex": re.compile(r'\[Http(Get|Post|Put|Delete|Patch)\s*\(\s*["\'](.*?)["\']\s*\)\]', re.IGNORECASE)
    },
    "C# (.NET Minimal APIs)": {
        "ext": [".cs"],
        "regex": re.compile(r'\.Map(Get|Post|Put|Delete|Patch)\s*\(\s*["\'](.*?)["\']', re.IGNORECASE)
    },
    "PHP (Laravel/Symfony)": {
        "ext": [".php"],
        "regex": re.compile(r'Route::(get|post|put|delete|patch)\s*\(\s*["\'](.*?)["\']', re.IGNORECASE)
    },
    "Rust (Actix/Rocket)": {
        "ext": [".rs"],
        "regex": re.compile(r'#\[(get|post|put|delete|patch)\s*\(\s*["\'](.*?)["\']\s*\)\]', re.IGNORECASE)
    },
    "Ruby (Rails/Sinatra)": {
        "ext": [".rb"],
        "regex": re.compile(r'^\s*(get|post|put|delete|patch)\s+["\'](.*?)["\']', re.IGNORECASE | re.MULTILINE)
    }
}

def auto_discover_swagger(target_dir: Path) -> list:
    """Hunts for OpenAPI/Swagger files by filename and internal content signatures."""
    candidates = set()
    common_names = {"swagger.json", "swagger.yaml", "swagger.yml", "openapi.json", "openapi.yaml", "openapi.yml"}

    for filepath in target_dir.rglob("*"):
        if not filepath.is_file() or filepath.suffix not in ['.json', '.yaml', '.yml']:
            continue

        # 1. Check filename first (Fast Path)
        if filepath.name.lower() in common_names:
            candidates.add(filepath)
            continue

        # 2. Deep Content Grep (Read first 1000 characters for speed)
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                head = f.read(1000)
                # Extra validation to ensure it's a real spec, not just a package.json mentioning swagger
                if re.search(r'("swagger"\s*:\s*"2\.\d"|"openapi"\s*:\s*"3\.\d\.\d"|swagger\s*:\s*["\']?2\.\d|openapi\s*:\s*["\']?3\.\d\.\d)', head):
                    candidates.add(filepath)
        except Exception:
            pass

    return list(candidates)

def parse_official_swagger(swagger_path: Path) -> set:
    """Parses the official security documentation to find 'Approved' APIs."""
    approved_apis = set()
    try:
        with open(swagger_path, 'r', encoding='utf-8') as f:
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

def map_physical_codebase(target_dir: Path) -> tuple:
    """Rips through the source code to find every API endpoint actually compiled."""
    physical_apis = defaultdict(list)
    frameworks_detected = set()
    
    for filepath in target_dir.rglob("*"):
        if not filepath.is_file():
            continue
            
        for framework, config in FRAMEWORK_TRAPS.items():
            if filepath.suffix in config["ext"]:
                try:
                    content = filepath.read_text(encoding='utf-8', errors='ignore')
                    hits = config["regex"].findall(content)
                    if hits:
                        frameworks_detected.add(framework)
                    
                    for method, api_path in hits:
                        # Normalize to "METHOD /path"
                        endpoint = f"{method.upper()} {api_path}"
                        physical_apis[endpoint].append(filepath.name)
                except Exception:
                    pass
                    
    return physical_apis, frameworks_detected

def main():
    parser = argparse.ArgumentParser(description="GitGalaxy Full API Network Map")
    parser.add_argument("source", help="Directory containing the application source code")
    parser.add_argument("--swagger", required=False, help="Optional: Path to a specific official swagger.json/yaml file")
    parser.add_argument("--merge-all", action="store_true", help="Merge all discovered Swagger files together (useful for Microservice Monorepos)")
    args = parser.parse_args()

    source_path = Path(args.source).resolve()

    if not source_path.exists():
        print(f"Error: Target source directory '{source_path}' does not exist.")
        sys.exit(1)

    print(f"🗺️  GitGalaxy Network Mapper analyzing physical endpoints in: {source_path.name}...\n")

# ==============================================================================
    # AUTO-DISCOVERY HANDSHAKE & THE AUDIT
    # ==============================================================================
    approved_apis = set()

    if not args.swagger:
        print(" 🔍 No --swagger file provided. Initiating auto-discovery...")
        candidates = auto_discover_swagger(source_path)
        
        if not candidates:
            print(" ❌ [ABORT] No OpenAPI/Swagger specifications found in the repository.")
            print("    Please provide one manually using the --swagger flag.")
            sys.exit(1)
            
        # Segregate testing schemas from primary production schemas
        primary_cands = []
        test_cands = []
        for c in candidates:
            parts = [p.lower() for p in c.relative_to(source_path).parts]
            if "test" in parts or "tests" in parts or "__tests__" in parts or "testing" in parts:
                test_cands.append(c)
            else:
                primary_cands.append(c)

        if len(primary_cands) == 1 and not args.merge_all:
            swagger_path = primary_cands[0]
            print(f" 🎯 Auto-discovered Primary Swagger: {swagger_path.relative_to(source_path)}")
            if test_cands:
                print(f" 🛡️  Safely bypassed {len(test_cands)} schemas detected in test directories:")
                for tc in test_cands:
                    print(f"    - [Assumed Test] {tc.relative_to(source_path)}")
            print("")
            approved_apis = parse_official_swagger(swagger_path)
            
        elif len(candidates) > 1 and not args.merge_all:
            print(f" ⚠️  [AMBIGUITY] Multiple OpenAPI/Swagger specifications found ({len(candidates)}).")
            print("    To prevent test-file pollution, automatic merging is disabled.")
            print("\n    Discovered Files (By Endpoint Count):")
            
            # Calculate telemetry (route counts) to help the user choose
            preview_stats = []
            for c in candidates:
                try:
                    routes = parse_official_swagger(c)
                    preview_stats.append((c, len(routes), c in test_cands))
                except:
                    preview_stats.append((c, 0, c in test_cands))
            
            # Sort by largest endpoint count first
            preview_stats.sort(key=lambda x: x[1], reverse=True)
            
            for c, count, is_test in preview_stats:
                badge = "[TEST DIR]" if is_test else "[PRIMARY]"
                print(f"    - {badge.ljust(11)} [{count} routes] {c.relative_to(source_path)}")
                
            print("\n    Please specify the correct schema using the --swagger flag,")
            print("    OR use the --merge-all flag to union all of them together.")
            sys.exit(1)
            
        elif len(candidates) > 1 and args.merge_all:
            print(f" 🎯 --merge-all active. Unioning {len(candidates)} discovered specifications...\n")
            for c in candidates:
                try:
                    approved_apis.update(parse_official_swagger(c))
                except Exception: pass
        else:
            swagger_path = candidates[0]
            print(f" 🎯 Auto-discovered Swagger specification: {swagger_path.relative_to(source_path)}\n")
            approved_apis = parse_official_swagger(swagger_path)
    else:
        swagger_path = Path(args.swagger).resolve()
        if not swagger_path.exists():
            print(f" ❌ Error: Provided Swagger file '{swagger_path}' does not exist.")
            sys.exit(1)
        approved_apis = parse_official_swagger(swagger_path)
    physical_apis_map, frameworks_detected = map_physical_codebase(source_path)
    physical_endpoints = set(physical_apis_map.keys())

    shadow_apis = physical_endpoints - approved_apis
    ghost_apis = approved_apis - physical_endpoints

    # ==============================================================================
    # PRESENTATION DASHBOARD
    # ==============================================================================
    print("==========================================================")
    print(" 📡 SHADOW API SECURITY AUDIT")
    print("==========================================================")
    framework_str = ", ".join(frameworks_detected) if frameworks_detected else "None Detected"
    print(f" Physical Frameworks Tracked    : {framework_str}")
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

def run_api_audit(source_path: Path) -> dict:
    """Programmatic entry point for GalaxyScope."""
    candidates = auto_discover_swagger(source_path)
    if not candidates: 
        return {"status": "no_swagger", "shadow_count": 0, "ghost_count": 0}
        
    primary_cands = [c for c in candidates if "test" not in [p.lower() for p in c.relative_to(source_path).parts]]
    if len(primary_cands) != 1: 
        return {"status": "ambiguous", "shadow_count": 0, "ghost_count": 0}
        
    approved_apis = parse_official_swagger(primary_cands[0])
    physical_apis_map, frameworks = map_physical_codebase(source_path)
    physical_endpoints = set(physical_apis_map.keys())
    
    return {
        "status": "success",
        "frameworks": list(frameworks),
        "shadow_count": len(physical_endpoints - approved_apis),
        "ghost_count": len(approved_apis - physical_endpoints),
        "shadow_apis": list(physical_endpoints - approved_apis)
    }
    
if __name__ == "__main__":
    main()