# ==============================================================================
# GitGalaxy
# Copyright (c) 2026 Joe Esquibel
#
# This source code is licensed under the PolyForm Noncommercial License 1.0.0.
# You may not use this file except in compliance with the License.
# A copy of the license can be found in the LICENSE file in the root directory
# of this project, or at https://polyformproject.org/licenses/noncommercial/1.0.0/
# ==============================================================================
import re

"""
gitgalaxy_config.py
Phase 0 & 1: Repository Ingestion, Filtering, and Pre-Flight Context.

This file serves as the core configuration payload. It defines the global 
security exceptions and the lightweight ingestion rules used to filter 
out noise before the heavy physics engines are loaded into memory.
"""

# ------------------------------------------------------------------
# ZERO-TRUST IMPORT CONTROL (Supply Chain Firewall)
# Defines allowed and banned external dependencies (NPM, PyPI, Composer)
# ------------------------------------------------------------------
# True  = Strict Mode (Only allow packages explicitly in APPROVED_IMPORTS)
# False = Audit Mode (Allow unknown packages, but block BLACKLISTED_IMPORTS)
STRICT_IMPORT_MODE = False

APPROVED_IMPORTS = [
    # Examples (Add your approved dependencies here)
]

BLACKLISTED_IMPORTS = [
    # Known compromised, malicious, or troll packages
]


# ------------------------------------------------------------------
# GLOBAL DENYLIST
# String patterns for files that should NEVER exist in the repository.
# If a file matches these patterns, scanners will instantly block the commit.
# Supports standard Unix wildcards (* for everything, ? for single char).
# ------------------------------------------------------------------
DENYLIST_PATTERNS = [
    # "internal_*",         # Blocks internal_notes.txt, internal_architecture.md
    # "*.kdbx",             # Blocks all KeePass password databases
    # "*_backup.sql",       # Blocks database dumps ending in _backup.sql
    # "master_key.*",       # Blocks master_key.pem, master_key.txt, etc.
    # "*-secret-*.json"     # Blocks anything with '-secret-' in the middle
]


# ------------------------------------------------------------------
# GLOBAL ALLOWLIST 
# Add exact relative paths or partial string matches here to bypass security tools.
# If a scanner finds a threat here, it will log an "Allowlist Bypass" warning 
# rather than failing the build. Use this to mute mock data in test suites.
# ------------------------------------------------------------------
ALLOWLIST_PATHS = [
    # "tests/phpunit/integration/includes/Json/key1.pem",
    # "tests/phpunit/integration/includes/Json/key1.pem.pub",
    # "tests/phpunit/integration/includes/Json/key2.pem",
    # "tests/phpunit/integration/includes/Json/key2.pem.pub"
]

# ------------------------------------------------------------------
# X-RAY INSPECTOR BYPASSES
# X-Ray uses thermodynamic math (Shannon Entropy) which naturally flags
# compression, foreign languages, and hashes. Add extensions or paths here 
# to bypass the X-Ray engine without blinding the Vault Sentinel.
# ------------------------------------------------------------------
XRAY_BYPASS_EXTENSIONS = [
    '.json', '.gz', '.zip', '.tar', '.png', '.jpg', '.jpeg', '.ico', '.yml'
]

XRAY_BYPASS_PATHS = [
    "package-lock.json",
    "yarn.lock",
    "composer.lock"
]


# ------------------------------------------------------------------------------
# 1. THE APERTURE SHIELD (Ingestion & Exclusion Rules)
# Consumed by: aperture.py
# ------------------------------------------------------------------------------
APERTURE_CONFIG = {
    # --- 0. THE SECRETS SHUNT ---
    # Files caught here will bypass standard physics math and instantly 
    # register a 100.0 score on the Secrets Risk exposure vector.
    "SECRETS_EXTENSIONS": {
        '.pem', '.key', '.pub', '.crt', '.cer', '.p12', '.p7b', 
        '.asc', '.gpg', '.sig', '.keystore', '.ovpn', '.pfx', '.jks', '.kdbx'
    },
    "SECRETS_EXACT": {
        'id_rsa', 'id_dsa', 'id_ed25519', 'id_ecdsa', 
        'truststore.jks', 'keystore.jks', '.env', '.env.local', 
        '.env.production', '.npmrc', '.htpasswd', '.pypirc', 
        'credentials.json', 'client_secret.json', 'auth.json', 'shadow'
    },

    # --- 1. The "Solar Shield" Blocklist ---
    "BLACK_HOLES": {
        # 1. Version Control Ghosts
        '.git', '.svn', '.hg', 'CVS', '.bzr', '.gitignore', '.gitmodules',

        # 2. Package Managers, Dependencies & Third-Party Vendors
        'node_modules', 'vendor', 'bower_components', 'jspm_packages', 
        'Pods', 'Carthage', 'third_party', '.npm',

        # 3. Virtual Environments
        'venv', '.venv', 'env', '.env', 'virtualenv', '.tox', '.nox',

        # 4. Caches, Meta-Frameworks & Bytecode
        '__pycache__', '.pytest_cache', '.mypy_cache', '.ruff_cache', 
        '.next', '.nuxt', '.svelte-kit', '.expo', '.angular', 
        '.turbo', '.parcel-cache', '.cache', 'caches', '.serverless',

        # 5. Compiled Output & Native Build Targets
        'dist', 'build', '_build', 'target', 'obj', 'out', 'out-tsc',
        'Release', 'Debug', 'cmake-build-debug', 'CMakeFiles', 'classes',

        # 6. Testing Output & Coverage Reports
        'coverage', '.nyc_output', 'htmlcov', 'TestResults',

        # 7. IDE, OS Metadata, & Editor Blueprints
        '.idea', '.vscode', '.vs', '.settings', '.metadata', '.eclipse', 
        '.fleet', 'DerivedData', '__MACOSX', 

        # 8. Transitory Runtime Data & Temp Matter
        'tmp', 'temp', 'logs', 'log',
        
        # 9. Documentation & Licensing
        'LICENSES', 'licenses', 'LICENSE', 'license', 'DOCS', 'docs', 'LEGAL', 'legal'
    },

    # --- 2. Extension-Level Solar Shield ---
    "BLACK_HOLE_EXTENSIONS": {
        # 1. Vector & 3D Traps
        '.svg', '.eps', '.ai', '.gltf', '.dae', '.stl', '.obj', '.fbx',

        # 2. Raster Image Binaries
        '.png', '.jpg', '.jpeg', '.gif', '.ico', '.webp', '.tiff', '.bmp', '.heic',

        # 3. Typography & Fonts
        '.woff', '.woff2', '.ttf', '.eot', '.otf',

        # 4. Office & Print Documents
        '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp',

        # 5. UI/UX Design Project Files
        '.fig', '.sketch', '.psd', '.xd',

        # 6. Media (Audio/Video Data)
        '.mp4', '.mp3', '.wav', '.avi', '.mov', '.mkv', '.webm', '.flac', '.ogg', 

        # 7. Archives & Compression Binaries
        '.zip', '.tar', '.gz', '.tgz', '.bz2', '.xz', '.7z', '.rar', '.iso', '.cab',

        # 8. Core Compiled Binaries & Object Files
        '.exe', '.dll', '.so', '.dylib', '.class', '.jar', '.war', '.ear', '.o', '.a', '.lib', '.out', '.pyc', '.pyd',
        
        # 9. Cryptographic Binaries & Keystores (Lethal to text parsers)
        '.p12', '.pfx', '.p7b', '.jks', '.kdbx', '.der'
    },
    
    # --- 3. Contraband Patterns ---
    "CONTRABAND_PATTERNS": [
        "*.min.js", "*.min.css",          
        "jquery*.js", "bootstrap*.js",    
        "typeahead*.js", "vue.global.js", 
        "chunk-*.js", "*bundle.js",       
        "*_full.html",                    
        "ltmain.sh", "config.guess", "config.sub", "depcomp", "missing", "install-sh"
    ],
    
    # --- 4. Integrity Thresholds ---
    "MAX_LINE_LENGTH": 500,           
    "MINIFICATION_SCAN_LIMIT": 50,    
    "MAX_FILE_SIZE_MB": 50,           
    
    # --- 5. Spectral Band Definitions ---
    "BANDS": {
        "RADIO": "ignored_system_or_hidden_file",       
        "MICROWAVE": "unreadable_binary_or_media",  
        "DARK_MATTER": "unsupported_file_type", 
        "INFRARED": "minified_or_massive_data",      
        "VISIBLE": "valid_source_code",
        "QUARANTINE": "critical_contraband_leak",
        "RADIOACTIVE": "exposed_secret_or_key" 
    }
}


# ------------------------------------------------------------------------------
# 2. PRIORITY ALLOWLIST (Architectural Anchors)
# Consumed by: guidestar_lens.py
# ------------------------------------------------------------------------------
# These files are granted a high confidence score for importance by the GuideStar Lens.
# If found, their Bayesian confidence is boosted (+0.10) to ensure they
# remain visible in the 3D map as high-priority architectural anchors.
PRIORITY_WHITELIST = [
    # --- AI Ecosystem Anchor ---
    "__galaxy_brain__.ai",

    # --- Universal Entry Points ---
    "main.py", "app.py", "index.js", "server.js", "main.go", "main.rs",
    "index.ts", "app.ts", "main.cpp", "main.c", "Main.java", "program.cs",
    
    # --- Framework Specific Anchors ---
    "manage.py", "wsgi.py", "asgi.py", "settings.py", # Django/Flask
    "App.js", "App.tsx", "index.tsx",                 # React/Native
    "routes.php", "api.php",                          # Laravel
    "application.rb", "routes.rb",                    # Rails
    "Startup.cs", "Program.cs",                       # .NET Core
    
    # --- Critical Path Assets ---
    "docker-compose.yml", "Dockerfile", "Jenkinsfile"
]


# ------------------------------------------------------------------------------
# 3. GUIDESTAR INTELLIGENCE (Manifests & Sector Biases)
# Consumed by: guidestar_lens.py
# ------------------------------------------------------------------------------
# Defines the rules for Bayesian Intent inference used by the GuideStar Lens
GUIDESTAR_CONFIG = {
    "MANIFEST_MAP": {
        'package.json': 'javascript',
        'Makefile': 'makefile',
        'CMakeLists.txt': 'cmake',
        'pyproject.toml': 'python',
        'setup.py': 'python',
        'Cargo.toml': 'rust',
        'go.mod': 'go',
        'Gemfile': 'ruby',
        'Rakefile': 'ruby',
        'pom.xml': 'java'
    },
    "INTENT_BIASED_SECTORS": {
        "bin", "scripts", "tools", "utils", "src", "libexec", "hooks"
    },
    "EXEC_PREFIX_MAP": {
        'python3': 'python',
        'python': 'python',
        'node': 'javascript',
        'npm': 'javascript',
        'sh': 'shell',
        'bash': 'shell',
        'cargo': 'rust',
        'go': 'go'
    }
}


# ------------------------------------------------------------------------------
# 4. PRISM OPTICS (Comment Delimiters by Family)
# Consumed by: prism.py, language_lens.py
# ------------------------------------------------------------------------------
# Defines the structural delimiters for extracting literature (comment_stream)
COMMENT_DEFINITIONS = {
  "mechanical_families": {
    "std_c": { "delimiters": ["//", "/*", "*/"] },
    "nested_c": { "delimiters": ["//", "/*", "*/"] },
    "pure_hash": { "delimiters": ["#"] },
    "hybrid_hash": { "delimiters": ["#", "<#", "#>", "=begin", "=end", "=pod", "=cut"] },
    "hybrid_dash": { "delimiters": ["--", "--[[", "]]", "{-", "-}"] },
    "polyglot": { "delimiters": ["//", "/*", "*/", "#"] },
    "positional": { "delimiters": ["*>", "!", "C", "*", "D"] },
    "singular": { "delimiters": ["", ";", "//", "dnl", "%", "%{", "%}"] },
    "lisp_semi": { "delimiters": [";", "#|", "|#"] }
  }
}


# ------------------------------------------------------------------------------
# 5. EXACT FILE ROUTING (Extensionless Identifiers)
# Consumed by: language_lens.py
# ------------------------------------------------------------------------------
EXACT_FILE_MATCH = {
    # --- 1. Build Systems & Manifests ---
    "Makefile": "makefile",
    "makefile": "makefile",
    "Dockerfile": "dockerfile",
    
    # Safely mapped to plaintext to prevent unsupported format crashes
    "CMakeLists.txt": "plaintext",
    "package.json": "plaintext",
    "BUILD": "plaintext",
    "BUILD.bazel": "plaintext",
    "WORKSPACE": "plaintext",
    "WORKSPACE.bazel": "plaintext",

    # --- 2. Environment-Specific Text / Config Bypasses ---
    "noopt_exceptions": "plaintext",
    "noopt_exceptions_f": "plaintext",
    "configure": "shell",
    "config.status": "shell",

    # --- 3. Dependency Manifests (Text Bypasses) ---
    "requirements.txt": "plaintext",
    "pyproject.toml": "plaintext",
    "Pipfile": "plaintext",
    "tox.ini": "plaintext",
    "MANIFEST.in": "plaintext",

    # --- 4. Secrets Bypass ---
    "id_rsa": "plaintext",
    "id_dsa": "plaintext",
    "id_ed25519": "plaintext",
    "id_ecdsa": "plaintext",
    "truststore.jks": "plaintext",
    "keystore.jks": "plaintext",
    ".env": "plaintext",
    ".env.local": "plaintext",
    ".env.production": "plaintext",
    ".npmrc": "plaintext",
    ".htpasswd": "plaintext",
    ".pypirc": "plaintext",
    "credentials.json": "plaintext",
    "client_secret.json": "plaintext",
    "auth.json": "plaintext",
    "shadow": "plaintext"
}


# ------------------------------------------------------------------------------
# 6. ORCHESTRATOR RULES (Global Pipeline Constraints)
# Consumed by: galaxyscope.py
# ------------------------------------------------------------------------------
ORCHESTRATOR_RULES = {
    # Stems that are too common to count as relational popularity (The Hallucination Filter)
    "POPULARITY_STOP_STEMS": {
        # Structural stems:
        "text", "type", "index", "main", "util", "config", "core", "base",
        
        # --- THE SHADOW IMPORT SHIELD ---
        # Python Stdlib:
        "sys", "os", "time", "math", "re", "json", "collections", "datetime", "string", "pathlib",
        # C/C++ Stdlib (Often imported without extensions in modern C++):
        "stdio", "stdlib", "string", "math", "vector", "map", "iostream", "memory", "algorithm"
    },
}


# ------------------------------------------------------------------------------
# 7. CHRONOMETER CONFIGURATION (Temporal Scanning Limits)
# Consumed by: chronometer.py
# ------------------------------------------------------------------------------
CHRONOMETER_CONFIG = {
    # The absolute ceiling for OS-level fallback scanning
    "FALLBACK_SCAN_LIMIT": 25000, 
    
    # Process management
    "STREAM_TIMEOUT_SECONDS": 60.0,
    
    # Dynamic Windowing Constraints (in seconds)
    # 10% of the project's lifespan will be used, bounded by these limits:
    "DYNAMIC_WINDOW_MIN_DAYS": 30,   # Never look at less than 1 month
    "DYNAMIC_WINDOW_MAX_DAYS": 365,  # Never look at more than 1 year
    
    # If the dynamic window yields zero commits, fallback to this raw volume
    "DORMANT_FALLBACK_COMMITS": 500 
}


# ------------------------------------------------------------------------------
# 8. STATIC ARCHETYPES (Inert Matter Labels)
# Consumed by: signal_processor.py
# ------------------------------------------------------------------------------
# Single Source of Truth for files that bypass active ML logic processing.
STATIC_ARCHETYPES = {
    "literature": "Static: Literature & Documentation",
    "data": "Static: Declarative Data & Configurations",
    "minified": "Static: Minified & Vendor Opaque Mass",
    "unknown": "Static: Unmapped Dark Matter"
}

# ------------------------------------------------------------------------------
# 9. PROJECT STORIES (Dynamic Lore Injection)
# Consumed by: gpu_recorder.py
# ------------------------------------------------------------------------------
PROJECT_STORIES = {
    # You can add your repository-specific lore and UI story payloads here later.
}