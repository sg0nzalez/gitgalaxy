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
scanner_config.py
The "Universal Laws" of the GitGalaxy Physics Engine.
Contains:
# --- 0. APERTURE CONFIGURATION (Phase 0.1: Solar Shield) ---
# --- 1. How we assign a language to a file ---
# --- 2. THE FIDELITY MATRIX (Phase 1) ---
# --- 3. PATH MODIFIERS (Context Scaling) ---
# --- 4. PRIORITY WHITELIST (GuideStar Focus Overrides) ---

"""

class ThreatPolicy:
    """Defines the threshold at which a structural anomaly becomes a critical threat."""
    
    PROFILES = {
        # The Baseline: For standard, internal development where some low-level logic is expected.
        "baseline": {
            "secrets_risk_threshold": 0.001,      # 0.1% density
            "hidden_malware_threshold": 0.60,     # 60% density
            "logic_bomb_threshold": 0.50,         # 50% density
            "injection_surface_threshold": 0.65,  # 65% density
            "memory_corruption_threshold": 0.60   # 60% density
        },
        
        # The Hazmat Suit: For scanning unknown PyPI/npm packages in a quarantine sandbox.
        "paranoid": {
            "secrets_risk_threshold": 0.0001,     # Any trace is critical
            "hidden_malware_threshold": 0.15,     # 15% density trips the wire
            "logic_bomb_threshold": 0.20,         # 20% density
            "injection_surface_threshold": 0.25,  # 25% density
            "memory_corruption_threshold": 0.10   # 10% density
        }
    }

    @staticmethod
    def get_policy(mode="baseline"):
        """Returns the specific threat thresholds based on the deployment mode."""
        return ThreatPolicy.PROFILES.get(mode, ThreatPolicy.PROFILES["baseline"])

#


# ------------------------------------------------------------------------------
# 1. OPTICAL LAYER (Consumed by aperture.py & guidestar_lens.py)
# ------------------------------------------------------------------------------
APERTURE_CONFIG = {
    # The "Solar Shield" Blocklist: Directories that represent non-maintainable matter.
    "BLACK_HOLES": {
        # --- 1. Version Control Ghosts (Legacy & Modern) ---
        # (Fixes the DOOM CVS Super-Giant bug)
        '.git', '.svn', '.hg', 'CVS', '.bzr', '.gitignore', '.gitmodules',

        # --- 2. Package Managers & Third-Party Dependencies ---
        'node_modules', 'vendor', 'bower_components', 'jspm_packages', 
        'Pods', 'Carthage',

        # --- 3. Virtual Environments (Python/Ruby) ---
        'venv', '.venv', 'env', '.env', 'virtualenv', '.tox', '.nox',

        # --- 4. Caches, Meta-Frameworks & Bytecode ---
        '__pycache__', '.pytest_cache', '.mypy_cache', '.ruff_cache', 
        '.next', '.nuxt', '.svelte-kit', '.expo', '.angular', 
        '.turbo', '.parcel-cache', '.cache', 'caches', '.serverless',

        # --- 5. Compiled Output & Native Build Targets ---
        'dist', 'build', '_build', 'target', 'obj', 'out', 'out-tsc',
        'Release', 'Debug', 'cmake-build-debug', 'CMakeFiles', 'classes',

        # --- 6. Testing Output & Coverage Reports ---
        'coverage', '.nyc_output', 'htmlcov', 'TestResults',

        # --- 7. IDE, OS Metadata, & Editor Blueprints ---
        '.idea', '.vscode', '.vs', '.settings', '.metadata', '.eclipse', 
        '.fleet', 'DerivedData', '__MACOSX', 

        # --- 8. Transitory Runtime Data & Temp Matter ---
        'tmp', 'temp', 'logs', 'log',
        
        # --- 9. Documentation & Licensing ---
        'LICENSES', 'licenses', 'LICENSE', 'license', 'DOCS', 'docs', 'LEGAL', 'legal'
    },

    # --- 11. Extension-Level Solar Shield ---
    # Deflects mathematically dense data files, encoded binaries, and 
    # media assets that will hang the Prism or dilute the logic map.

    "BLACK_HOLE_EXTENSIONS": {
        # 1. Vector & 3D Traps (Massive XML coordinate arrays / JSON blobs)
        '.svg', '.eps', '.ai', '.gltf', '.dae', '.stl', '.obj', '.fbx',

        # 2. Raster Image Binaries
        '.png', '.jpg', '.jpeg', '.gif', '.ico', '.webp', '.tiff', '.bmp', '.heic',

        # 3. Typography & Fonts (Complex hex/binary tables)
        '.woff', '.woff2', '.ttf', '.eot', '.otf',

        # 4. Cryptographic Keys & Signatures (Dense Base64 / Hex blocks)
        # Prevents the engine from scanning thousands of lines of raw cryptographic hashes.
        '.crt', '.cer', '.p12', '.p7b', '.asc', '.gpg', '.sig', '.keystore',

        # 5. Office & Print Documents (Zipped XMLs that cause regex spirals)
        '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp',

        # 6. UI/UX Design Project Files
        '.fig', '.sketch', '.psd', '.xd',

        # 7. Media (Audio/Video Data)
        '.mp4', '.mp3', '.wav', '.avi', '.mov', '.mkv', '.webm', '.flac', '.ogg', 

        # 8. Archives & Compression Binaries
        '.zip', '.tar', '.gz', '.tgz', '.bz2', '.xz', '.7z', '.rar', '.iso', '.cab',

        # 9. Core Compiled Binaries & Object Files
        # (Catches things that might accidentally pass a simple UTF-8 sniff test)
        '.exe', '.dll', '.so', '.dylib', '.class', '.jar', '.war', '.ear', '.o', '.a', '.lib', '.out', '.pyc', '.pyd'
    },
    
    # --- 12. Contraband Patterns ---
    # Global glob patterns to natively deflect vendored, compiled, or machine-generated 
    # source code that bleeds outside of standard vendor/ directories.
    "CONTRABAND_PATTERNS": [
        "*.min.js", "*.min.css",          # Universal minification
        "jquery*.js", "bootstrap*.js",    # Legacy frontend monoliths
        "typeahead*.js", "vue.global.js", # Common UI plugins
        "chunk-*.js", "*bundle.js",       # Webpack/Vite compiled output
        "*_full.html",                    # Minified bundled HTML UIs
        
        # THE FIX: GNU Autotools & Libtool procedural monoliths
        "ltmain.sh", "config.guess", "config.sub", "depcomp", "missing", "install-sh"
    ],
    
    # Integrity Thresholds: Limits for minification and data-dump detection.
    "MAX_LINE_LENGTH": 500,           # Saturated Signal threshold (characters)
    "MINIFICATION_SCAN_LIMIT": 50,    # Performance Guard (lines to check)
    "MAX_FILE_SIZE_MB": 50,           # Resource Guard (Large Data Dump limit)
    
    # Spectral Band Definitions: Standardized terminology for the Orchestrator.
    # These strings are written directly to the galaxy.json manifest.
    "BANDS": {
        "RADIO": "ignored_system_or_hidden_file",       
        "MICROWAVE": "unreadable_binary_or_media",  
        "DARK_MATTER": "unsupported_file_type", 
        "INFRARED": "minified_or_massive_data",      
        "VISIBLE": "valid_source_code",
        "QUARANTINE": "critical_contraband_leak" 
    }
}

# These files are granted a high confidence score for importance by the GuideStar Lens.
# If found, their Bayesian confidence is boosted (+0.10) to ensure they
# remain visible in the 3D map as high-priority architectural anchors.
PRIORITY_WHITELIST = [
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
# 2. LEXICAL & SYNTACTIC LAYER (Consumed by language_lens.py & detector.py)
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

# Defines the tuning constants, anchors, and disqualifiers for the Linguistic Detector Chip
LENS_CONFIG = {
    "COLLISION_FREQUENCIES": {'.inc', '.h', '.py', '.cshtml', '.c', '.y', '.m'},
    "PROSE_ANCHORS": {
        'README', 'LICENSE', 'LICENCE', 'CONTRIBUTING', 'CHANGELOG', 'AUTHORS', 
        'INSTALL', 'NOTICE', 'COPYING', 'TODO', 'FAQ', 'NOTES', 
        'CREDITS', 'HISTORY', 'MANIFEST', 'FILES', 'FILES2', 'ACKNOWLEDGEMENTS',
        'AGREEMENT', 'CONTRIBUTORS', 'HACKING','HACKERS','AUTHOR',
        'CHANGES', 'NEWS', 'RELEASE_NOTES', 'RELEASENOTES', 
        'UPGRADE', 'UPGRADING', 'VERSION', 'BUGS', 'FEATURES',
        'ARCHITECTURE', 'DESIGN', 'GUIDE', 'USAGE', 'TUTORIAL', 'DOCS',
        'CODE_OF_CONDUCT', 'SECURITY', 'SUPPORT', 'COPYRIGHT', 
        'PATENTS', 'LEGAL', 'THANKS', 'OWNERS', 'CODEOWNERS', 'MAINTAINERS',
        'POSTAMBLE', 'README_BUFRLIB'
    },
    "DISQUALIFIERS": {
        'pure_hash': r'(?:^\s*using\s+namespace\b|^\s*public\s+(?:class|interface)\b|<\?php)',
        'positional': r'(?:^\s*(?:import|export)\s+\{|<html\b|<\?php|^\s*namespace\s+\w+)',
        'std_c': r'(?:<\?php|^\s*IDENTIFICATION\s+DIVISION\.)',
        'nested_c': r'(?:<\?php|<html\b|^\s*IDENTIFICATION\s+DIVISION\.)',
        'hybrid_dash': r'(?:^\s*public\s+class\b|<\?php|<html\b)',
        'hybrid_hash': r'(?:<\?php|^\s*IDENTIFICATION\s+DIVISION\.)',
        'singular': r'(?:<\?php|^\s*public\s+class\b|^\s*IDENTIFICATION\s+DIVISION\.)',
        'polyglot': r'^\s*IDENTIFICATION\s+DIVISION\.'
    },
    "HANDSHAKE_REGISTRY": [
        # Added strict line-start anchors to prevent matching generics like `List<script>`
        {"trigger": r'^[ \t]*<script\b', "end": r'</script>', "target": "javascript", "pair": None},
        {"trigger": r'^[ \t]*<style\b', "end": r'</style>', "target": "css", "pair": None},
        {"trigger": r'asm!\s*\(|__asm__', "end": r'\)', "target": "assembly", "pair": ("(", ")")},
    ],
    "THRESHOLDS": {
        "INTENSITY_FLOOR": 0.78,
        "FLOOR_TIER_4": 0.92,
        "PROSE_CONFIDENCE": 0.95,
        "MIN_OUTLIER_MARGIN": 1.15,
        "PROSE_BASELINE_SIGNAL": 3.0,
        "HANDSHAKE_LOOKAHEAD_LIMIT": 50000,
        "ECOSYSTEM_DOMINANCE_MIN": 0.70,
        "TIER_4_MIN_LINES": 100,
        "TIER_4_OUTLIER_MARGIN": 1.3
    }
}

PRISM_CONFIG = {
    "SHIELD_PATTERN": r'((?<!\\)"(?:\\.|[^"\\])*"|(?<!\\)\'(?:\\.|[^\'\\])*\'|(?<!\\)`(?:\\.|[^`\\])*`)',
    "PYTHON_DOC_PATTERN": r'(?m)^\s*(?:\"\"\"[\s\S]*?\"\"\"|\'\'\'[\s\S]*?\'\'\')\s*$',
    "PHP_HEREDOC_PATTERN": r'<<<[ \t]*([\'"]?)([a-zA-Z_]\w*)\1[ \t]*\r?\n[\s\S]*?\n[ \t]*\2;?',
    "PHP_MULTILINE_STRING": r'(?<!\\)"(?:\\.|[^"\\])*\n(?:\\.|[^"\\])*"|(?<!\\)\'(?:\\.|[^\'\\])*\n(?:\\.|[^\'\\])*\'',
    "POSITIONAL_ANCHORS": {"*", "C", "c", "/", "!"},
    "THRESHOLDS": {
        "NESTED_PEEL_LIMIT": 500
    }
}

LANGUAGE_DEFINITIONS = {
    "python": {
        "_meta": {
            "target_version": "Python 3.14",
            "last_updated": "2026-03-11",
            "blueprint_version": "6.30",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard modern suffixes, legacy formats, typed stubs, Cython, and build-tooling dialects.
        "extensions": [
            ".py",
            ".py3",
            ".py2",
            ".pyw",
            ".pyi",
            ".pyx",
            ".pxd",
            ".pxi",
            ".pyz",
            ".pyzw",
            ".bzl",
            ".gyp",
            ".gypi",
            ".vpython",
            ".vpython3",
            ".rpy",
            ".smk",
        ],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Extensionless build/config scripts and tooling configs that are secretly pure code.
        "exact_matches": [
            "setup.py",
            "SConstruct",
            "SConscript",
            "BUCK",
            "BUILD",
            "wscript",
            "Snakefile",
        ],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, package manifests, and lockfiles to resolve ambiguous files.
        "discriminators": [
            ".py",
            "requirements.txt",
            "pyproject.toml",
            "Pipfile",
            "Pipfile.lock",
            "tox.ini",
            "poetry.lock",
            "setup.cfg",
        ],
        "internal_discriminator": re.compile(r"^[ \t]*(?:import|from)\s+(?:subprocess|multiprocessing|threading|requests|pandas|numpy|django|flask|fastapi|sqlalchemy|boto3|httpx|matplotlib|scipy|tensorflow|torch)\b", re.M),
        # EXECUTION SIGNATURES: Interpreters found on Line 1.
        "shebangs": ["python", "python3", "python2", "pypy", "pypy3", "jython"],
        # UPGRADED: Maps to Family 3 (Pure Hash)
        # Rationale: Uses '#' for line-level literature; multi-line literature
        # (docstrings) is handled by the Section 2.3.C.3 Heuristic Pass.
        "lexical_family": "pure_hash",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Python uses '#' for standard line-level literature.
            "_line_anchor": re.compile(r"#"),
            # Inline comments are also triggered by the '#' token.
            "_inline_comment": re.compile(r"#"),
            # EXPLICIT: Python lacks native block comment delimiters (e.g. /* */).
            # Triple-quotes are Strings and protected by the Group 1 Shield.
            "_block_start": None,
            "_block_end": None,
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Includes match/case (3.10+) and logical short-circuits. EXCLUDES exceptions.
            "branch": re.compile(
                r"\b(if|elif|else|for|while|with|try|finally|match|case|and|or)\b"
            ),
            # 2. args (The Coupling Mass)
            # Signatures for def/lambda. Bounded generics [^\]]* and params [^)]*.
            "args": re.compile(
                r"(?:async[ \t]+)?def\s+\w+(?:\[[^\]]*\])?\s*\([^)]*\)|\blambda\s+[^:]+:",
                re.M,
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: _private (encapsulation) and Final (freeze_hits).
            "linear": re.compile(
                r"\b(def|class|return|import|from|as|pass|continue|break|yield|await|assert|del|global|nonlocal|type)\b"
            ),
            # 4. func_start (The Satellite Spawner)
            # Anchors executable logic. Steps safely over decorators.
            "func_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]+){0,5}(?:async[ \t]+)?def\s+\w+(?:\[[^\]]*\])?\s*\(",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            "class_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]+){0,5}class\s+\w+(?:\[[^\]]*\])?",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\b(try|except(?:\*)?|finally|assert|isinstance|issubclass|hasattr|getattr|dataclass|BaseModel|Field|TypeGuard|override)\b"
            ),
            # 7. safety_neg (The Fractures)
            # Swallowed errors, wildcard imports, and Any bypasses.
            "safety_neg": re.compile(
                r"\bpass\b[ \t]*$|except\s*[:(]|except\s+(?:Base)?Exception|from\s+[\w.]+\s+import\s+\*|#\s*type:\s*ignore|\b(Any|cast)\b|=\s*\[\s*\]|=[ \t]*\{\s*\}",
                re.M,
            ),
            # 8. danger (The Heavy Load)
            # Process killers and un-sanitized deserialization. EXCLUDES TODO/print.
            "danger": re.compile(
                r"\b(eval|exec|subprocess\.(?:call|Popen|run)|os\.system|pickle\.loads?|yaml\.unsafe_load|shell=True)\b"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(open|requests|httpx|aiohttp|boto3|os\.|sys\.|pathlib|socket|sqlalchemy|psycopg2?|asyncpg)\b"
            ),
            # 10. api (The Event Horizon)
            # Implicit public defaults (undercased root definitions) + explicit __all__.
            "api": re.compile(
                r"^[ \t]*(?:async[ \t]+)?def\s+[^_]\w+|^[ \t]*class\s+[^_]\w+|^__all__[ \t]*=|@(?:app|router|blueprint)\.(?:get|post|put|delete)",
                re.M,
            ),
            # 11. flux (The Boiling Plasma)
            # State mutation. Includes Walrus operator and collection mutators.
            "flux": re.compile(
                r"\bglobal\b|\bnonlocal\b|\b(?:self|cls)\.\w+[ \t]*=|:=|(?:\.\w+)?\.(?:append|extend|update|pop|remove|insert|clear)\s*\("
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"#[ \t]*(?:def|class|import|if|for|while|try|return)\b"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r'"""|\'\'\'|:param|:return|:raises|:type|\b(?:Args|Returns|Yields|Raises|Attributes):\b'
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r"\b(unittest|pytest|TestCase|fixture|patch)\b|def[ \t]+test_|\bassert\b|\bMock\b"
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Hidden Complexity) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(async|await|asyncio|threading|multiprocessing|ThreadPoolExecutor|TaskGroup|gather|create_task)\b"
            ),
            # 16. ui_framework (The View Layer)
            "ui_framework": re.compile(
                r"\b(streamlit|django\.shortcuts|flask\.render_template|gradio|dash|fasthtml|jinja2|render)\b"
            ),
            # 17. closures (The Functional Depth)
            "closures": re.compile(r"\blambda\b"),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\b(os\.environ|sys\.argv|sys\.path|globals\(\)|locals\(\))\b"
            ),
            # 19. decorators (The Metadata Hooks)
            "decorators": re.compile(r"^[ \t]*@[\w.]+", re.M),
            # 20. generics (The Type Abstractions)
            "generics": re.compile(
                r"\b(List|Dict|Set|Tuple|Optional|Union|TypeVar|Generic|Any|Callable|Mapping)\b\[[^\]]*\]|\b(list|dict|set|tuple|type)\[[^\]]*\]|->"
            ),
            # 21. comprehensions (The High-Density Loops)
            "comprehensions": re.compile(
                r"\[[^\]]*\bfor\b[^\]]*\]|\{[^}]*\bfor\b[^}]*\}|\([^)]*\bfor\b[^)]*\)"
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(math|numpy|pandas|polars|scipy|tensorflow|torch|jax|matplotlib|sklearn|keras|cv2|transformers)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Metaprogramming and class-level binding.
            "heat_triggers": re.compile(
                r"__(?:getattr|setattr|del|call|new|metaclass|dict|dir|import)__|@(?:staticmethod|classmethod|property)|\b(?:getattr|setattr|inspect\.)\b"
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(r"^[ \t]*(?:import|from)\b\s+[\w.]+", re.M),
            
            "_dependency_capture": re.compile(r"^[ \t]*(?:from|import)\s+([a-zA-Z0-9_.]+)", re.M),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"(?:__author__[ \t]*=|Author:|Created by:)\s*(.*)", re.I
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(
                r"\b(HACK|FIXME|XXX|BUG|KLUDGE|UGLY|WTF)\b", re.I
            ),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": re.compile(
                r"\b(render_template|HttpResponse|JSONResponse|TemplateResponse|WSGIApplication|ASGIApplication)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(Signal|receiver|post_save|pre_save|asyncio\.Event|EventDispatcher|emit|send|blinker)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\b(Depends|Provide|Inject|Container|dependency_injector|fastapi\.Depends)\b"
            ),
            # 34. macros
            "macros": None,  # Python lacks a C-style preprocessor.
            # 35. pointers (The Memory Map)
            "pointers": re.compile(r"\b(ctypes\.POINTER|c_void_p|byref)\b"),
            # 36. memory_alloc (Manual Memory Management)
            "memory_alloc": None,  # Managed by GC.
            # 37. inline_asm
            "inline_asm": None,
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(logging|logger|structlog|sentry_sdk|datadog|loguru)\.(?:info|error|warn|warning|debug|trace|log|exception|critical)\b"
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(r"\b(print|input)\s*\("),
            # 40. cast_hits (The Trust Me Tax)
            "cast_hits": re.compile(
                r"\b(int|str|float|list|dict|set|tuple|bool|bytes|cast)\b\s*\("
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(raise|quit|exit|sys\.exit|abort)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\b(time\.sleep|asyncio\.sleep|Thread\.join)\b"),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(r"<<|>>|\^|~"),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(Lock|RLock|Semaphore|BoundedSemaphore|Event|Condition|Barrier)\b"
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(r"\b(Final|frozenset|mappingproxy|immutable)\b"),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(r"\b(close|__exit__|del|shutdown|cleanup)\b\s*\("),
            # 47. encapsulation (The Vault)
            # Captures protected/private members via underscore convention.
            "encapsulation": re.compile(r"\b_[a-zA-Z_]\w*\b"),
            # 48. listeners (The Sinks)
            "listeners": re.compile(
                r"\b(on_event|add_listener|subscribe|callback|handler)\b"
            ),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(
                r"\b(pytest\.mark\.skip|unittest\.skip|mock\.|MagicMock)\b"
            ),
        },
    },
    "javascript": {
        "_meta": {
            "target_version": "ES2025 / React 19 / Node 22+",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard modern suffixes, legacy server-side formats, UI extensions, and embedded scripts.
        "extensions": [
            ".js",
            ".mjs",
            ".cjs",
            ".jsx",
            ".es6",
            ".es",
            ".pac",
            ".sjs",
            ".ssjs",
            ".xsjs",
            ".xsjslib",
            ".jsm",
            "._js",
            ".bones",
            ".gs",
        ],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Extensionless build/config scripts and tooling configs that are secretly pure code.
        "exact_matches": ["Jakefile"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, package manifests, and lockfiles to resolve ambiguous files.
        "discriminators": [
            ".js",
            "package.json",
            "package-lock.json",
            "yarn.lock",
            "pnpm-lock.yaml",
            "bower.json",
            ".eslintrc",
            ".prettierrc",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1.
        "shebangs": ["node", "nodejs", "deno", "bun", "zx", "phantomjs", "casperjs"],
        # UPGRADED: Maps to Family 1 (Standard C)
        # Rationale: Uses '//' for line-level literature; multi-line literature
        # (/* */) is handled by the Section 2.3.C.3 Heuristic Pass.
        "lexical_family": "std_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Standard C-family line comment token (Includes JSDoc // style)
            "_line_anchor": re.compile(r"//"),
            # Inline comments follow the standard '//' delimiter.
            "_inline_comment": re.compile(r"//"),
            # Block comment start: /* (Standard non-recursive delimiter)
            "_block_start": re.compile(r"/\*"),
            # Block comment end: */
            "_block_end": re.compile(r"\*/"),
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Decisions and logical jumps. EXCLUDES throw (bailout_hits).
            "branch": re.compile(
                r"\b(if|else|switch|case|default|for|while|do|catch|finally|continue|break|try)\b|&&|\|\||\?|\?\?"
            ),
            # 2. args (The Coupling Mass)
            # Parameter blocks. Bounded to prevent ReDoS on massive positional/destructured sets.
            "args": re.compile(
                r"function\s*\w*\s*\([^)]*\)|(?:\([^)]*\)|[a-zA-Z_$][\w$]*)[ \t]*=>|^[ \t]*(?:static[ \t]+)?(?:async[ \t]+)?(?:get\s+|set\s+)?(?:#?[a-zA-Z_$][\w$]*)\s*\([^)]*\)",
                re.M,
            ),
            # 3. linear (The Smooth Path)
            # Structural declaration boundaries. EXCLUDES: Access modifiers (encapsulation) and const (freeze_hits).
            "linear": re.compile(
                r"\b(let|var|import|export|return|class|extends|yield|super|await|delete)\b|=>"
            ),
            # 4. func_start (The Satellite Spawner)
            # Uses positive lookaheads (?=) to stop the match exactly at the identifier name.
            # Captures standard functions, namespace assignments (foo.bar = function),
            # object literal methods (foo: function), and ES6 methods.
            "func_start": re.compile(
                r"(?:"
                # 1. Standard: `function foo(`
                r"\b(?:async\s+)?function\s*\*?\s+[a-zA-Z_$][\w$]*(?=\s*\()|"
                # 2. Namespace/Variable Assignment: `foo.bar = function(` or `const foo = async () =>`
                r"\b[a-zA-Z_$][\w$]*(?=[ \t]*=[ \t]*(?:async\s*)?(?:function(?:\s*\*)?\b|\([^)]*\)[ \t]*=>|[a-zA-Z_$][\w$]*[ \t]*=>))|"
                # 3. Object Literal Property: `bar: function(` or `bar: () =>`
                r"^[ \t]*[a-zA-Z_$][\w$]*(?=[ \t]*:[ \t]*(?:async\s*)?(?:function(?:\s*\*)?\b|\([^)]*\)[ \t]*=>|[a-zA-Z_$][\w$]*[ \t]*=>))|"
                # 4. ES6 Class/Object Methods: `myMethod() {` (Explicitly blocks control flow keywords)
                r"^[ \t]*(?:static[ \t]+)?(?:async[ \t]+)?(?:get\s+|set\s+)?(?!(?:if|for|while|switch|catch|return|throw|new|typeof|jQuery|function)\b|\$)#?[a-zA-Z_$][\w$]*(?=\s*\()"
                r")",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            "class_start": re.compile(
                r"^[ \t]*(?:export[ \t]+)?(?:default[ \t]+)?class\s+[a-zA-Z_$][\w$]*",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\b(try|catch|finally|typeof|instanceof|Array\.isArray|Number\.(?:isFinite|isNaN)|Object\.hasOwn)\b|===|!==|\?\?|\?\."
            ),
            # 7. safety_neg (The Fractures)
            # Loose equality and bypasses.
            "safety_neg": re.compile(
                r"==(?!=)|!=(?!=)|\b(with|void)\b|eslint-disable|@ts-nocheck"
            ),
            # 8. danger (The Heavy Load)
            # Catastrophic vulnerabilities. EXCLUDES console.log (print_hits) and TODO (debt).
            "danger": re.compile(
                r"\b(eval|document\.write|innerHTML|outerHTML|dangerouslySetInnerHTML|debugger|alert|process\.exit)\b"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(fetch|axios|http|https|fs|path|database|sql|localStorage|sessionStorage|indexedDB|document\.cookie|XMLHttpRequest|child_process)\b"
            ),
            # 10. api (The Event Horizon)
            # Exposure surface. Explicit exports + implicit architectural defaults.
            "api": re.compile(
                r"\b(export|module\.exports|exports\.)\b|@(Controller|Resolver|Get|Post|Put|Delete)\b"
            ),
            # 11. flux (The Boiling Plasma)
            # Mutation of state. EXCLUDES const (freeze_hits).
            "flux": re.compile(
                r"\b(let|var|this\.|setState|mut|push|pop|shift|unshift|splice|sort|reverse|\.current[ \t]*=|\.set\(|\.delete\(|\.add\()\b"
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"//[ \t]*(?:if|for|while|function|class|return|var|const|let|import)\b"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r"/\*\*|@param|@return|@throws|@deprecated|@typedef|@type|@template"
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r"\b(describe|expect|assert|beforeEach|afterEach|jest|mocha|vitest|cy\.)\b|\b(?:it|test)\s*\("
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Domain) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(async|await|Promise|requestAnimationFrame|setImmediate|setTimeout|setInterval|queueMicrotask|Worker|postMessage)\b|\.then\(|\.catch\("
            ),
            # 16. ui_framework (The View Layer)
            "ui_framework": re.compile(
                r'<[A-Z]\w+|className=|use(?:State|Effect|Context|Reducer|Ref|Memo|Callback|Transition)|props\.|this\.state|document\.(?:getElementById|querySelector|addEventListener)|["\']use\s+(?:client|server)["\']'
            ),
            # 17. closures (The Functional Depth)
            "closures": re.compile(
                r"=>[ \t]*\{|\(\)[ \t]*=>|function\s*\([^)]*\)[ \t]*\{"
            ),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\b(window\.|global\.|process\.env|document\.|navigator\.|self\.|globalThis\.)\b"
            ),
            # 19. decorators (The Metadata Hooks)
            "decorators": re.compile(r"@\w+"),
            # 20. generics (The Type Abstractions)
            # Simulated/JSDoc generics in JS.
            "generics": re.compile(r"@template\s+\w+|/\*\*\s*@type\s*(?:\{|<\w+)"),
            # 21. comprehensions (The High-Density Loops)
            "comprehensions": re.compile(
                r"\.(?:map|filter|reduce|flatMap|some|every|find|forEach|groupBy)\s*\("
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(Math\.|tf\.|THREE\.|d3\.|gl-matrix|random)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            "heat_triggers": re.compile(
                r"\b(arguments\.|prototype|__proto__|Object\.assign|Reflect|Proxy|Object\.defineProperty|\.bind\(|\.call\(|\.apply\()\b"
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(
                r"^[ \t]*(?:import|export)\b[^;]*?\bfrom\b|\brequire\s*\(|import\s*\(",
                re.M,
            ),
            
            "_dependency_capture": re.compile(r"(?:import|export)\b[^;]*?\bfrom\s*['\"]([^'\"]+)['\"]|\b(?:require|import)\s*\(\s*['\"]([^'\"]+)['\"]", re.M),
            
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(r"(?:@author|Created by)\s+(.*)", re.I),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": re.compile(
                r"\b(getServerSideProps|getStaticProps|getInitialProps|renderToString|hydrateRoot)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(emit|on|once|off|dispatchEvent|EventEmitter|EventTarget)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\b(Inject|Injectable|Container|resolve|register|inversify)\b"
            ),
            # 34. macros
            "macros": None,
            # 35. pointers
            "pointers": None,
            # 36. memory_alloc (The Yin to cleanup)
            "memory_alloc": re.compile(r"\bnew\s+[A-Z]\w*"),
            # 37. inline_asm
            "inline_asm": None,
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(logger|winston|pino|morgan|datadog|prometheus|newrelic|sentry)\.(?:info|error|warn|debug|trace|log)\b"
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(
                r"\bconsole\.(?:log|warn|error|dir|trace|info|table|time)\b"
            ),
            # 40. cast_hits (The "Trust Me" Tax)
            "cast_hits": re.compile(
                r"\b(Number|String|Boolean|BigInt|Symbol|Array\.from)\b\s*\("
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(throw|abort|process\.exit)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(
                r"\b(sleep|delay|setTimeout|setInterval|Atomics\.wait)\b"
            ),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(r"<<|>>>?|\^|~"),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(mutex|lock|synchronized|Semaphore|Atomics\.lock|Atomics\.wait)\b",
                re.I,
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(
                r"\b(const|readonly|final|Object\.freeze|Object\.seal)\b"
            ),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r"\b(dispose|close|destroy|clearTimeout|clearInterval|removeEventListener|delete)\b"
            ),
            # 47. encapsulation (The Vault)
            # JS private fields and keywords.
            "encapsulation": re.compile(r"\b(private|protected|internal|#)\b"),
            # 48. listeners (The Sinks)
            "listeners": re.compile(
                r"\b(on|addEventListener|subscribe|watch|effect)\b"
            ),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(
                r"\b(test\.skip|it\.skip|describe\.skip|xit|xdescribe|mock|stub)\b"
            ),
        },
    },
    "typescript": {
        "_meta": {
            "target_version": "TypeScript 6.0 / ES2026",
            "last_updated": "2026-03-12",
            "blueprint_version": "v6.3.1",
            "status": "production",
        },
        "extensions": [
            ".ts",
            ".tsx",
            ".mts",
            ".cts",
            ".d.ts",
            ".d.mts",
            ".d.cts",  # Ambient declarations
        ],
        # COMPREHENSIVE SURFACE AREA: Standard modern suffixes, JSX variants, and ambient declaration boundaries.
        "extensions": [".ts", ".tsx", ".mts", ".cts", ".d.ts", ".d.mts", ".d.cts"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Extensionless build/config scripts and tooling configs that are secretly pure code.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, package manifests, and lockfiles to resolve ambiguous files.
        "discriminators": [
            ".ts",
            "tsconfig.json",
            "tslint.json",
            "package.json",
            "yarn.lock",
            "pnpm-lock.yaml",
            "deno.json",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1.
        "shebangs": ["ts-node", "deno", "bun", "tsx"],
        # UPGRADED: Maps to Family 1 (Standard C)
        # Rationale: Uses '//' for line-level literature; multi-line literature
        # (/* */) is handled by the Section 2.3.C.3 Heuristic Pass.
        "lexical_family": "std_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Standard C-family line comment token (Includes TSDoc /// references)
            "_line_anchor": re.compile(r"//"),
            # Inline comments follow the standard '//' delimiter.
            "_inline_comment": re.compile(r"//"),
            # Block comment start: /* (Standard non-recursive delimiter)
            "_block_start": re.compile(r"/\*"),
            # Block comment end: */
            "_block_end": re.compile(r"\*/"),
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # EXCLUDES: Exceptions (throw). Includes control flow and logical short-circuits.
            "branch": re.compile(
                r"\b(if|else|switch|case|default|for|while|do|catch|finally|continue|break|try)\b|&&|\|\||\?|\?\?"
            ),
            # 2. args (The Coupling Mass)
            # CRITICAL FIX: Added negative lookahead for control flow, and `[^=;{]*` to support TypeScript return types.
            "args": re.compile(
                r"function\s+\w*(?:<[^>]*>)?\s*\([^)]*\)|\([^)]*\)[^=;{]*=>|[a-zA-Z_$][\w$]*[ \t]*=>|^[ \t]*(?:(?:public|private|protected|static|override|abstract)[ \t]+){0,3}(?:async[ \t]+)?(?:get\s+|set[ \t]+)?(?!(?:if|for|while|switch|catch)\b)[a-zA-Z_$][\w$]*\s*\([^)]*\)",
                re.M,
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: Access modifiers (public/private) and Immutability (const).
            "linear": re.compile(
                r"\b(var|return|class|interface|type|enum|import|export|yield|await|satisfies|using|namespace|module|implements|extends|declare)\b|=>"
            ),
            # 4. func_start (The Satellite Spawner)
            # Captures standard functions, assignments, object properties, and class methods.
            # Safely steps over TypeScript Generics <T> and explicit return types in the lookaheads.
            "func_start": re.compile(
                r"(?:"
                # 1. Standard: `function foo<T>(`
                r"\b(?:async\s+)?function\s*\*?\s+[a-zA-Z_$][\w$]*(?=(?:<[^>]*>)?\s*\()|"
                # 2. Namespace/Variable Assignment: `foo.bar = function<T>(` or `const foo = async (req): Promise<Res> =>`
                # CRITICAL FIX: `[^=;{]*=>` allows the spawner to successfully step over TypeScript return types.
                r"\b[a-zA-Z_$][\w$]*(?=[ \t]*=[ \t]*(?:async\s*)?(?:<[^>]*>\s*)?(?:function(?:\s*\*)?\b|\([^)]*\)[^=;{]*=>|[a-zA-Z_$][\w$]*[ \t]*=>))|"
                # 3. Object Literal Property: `bar: function<T>(` or `bar: (req): Res =>`
                # CRITICAL FIX: `[^=;{]*=>` allows the spawner to successfully step over TypeScript return types.
                r"^[ \t]*[a-zA-Z_$][\w$]*(?=[ \t]*:[ \t]*(?:async\s*)?(?:<[^>]*>\s*)?(?:function(?:\s*\*)?\b|\([^)]*\)[^=;{]*=>|[a-zA-Z_$][\w$]*[ \t]*=>))|"
                # 4. Class/Object Methods: `public async myMethod<T>() {`
                r"^[ \t]*(?:(?:public|private|protected|static|override|abstract|readonly)[ \t]+){0,4}(?:async[ \t]+)?(?:get\s+|set\s+)?(?!(?:class|interface|type|enum|if|for|while|switch|catch|return|throw|new|typeof|jQuery|function)\b|\$)#?[a-zA-Z_$][\w$]*(?=(?:<[^>]*>)?\s*\()"
                r")",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            "class_start": re.compile(
                r"^[ \t]*(?:export[ \t]+)?(?:abstract[ \t]+)?(?:default[ \t]+)?(?:class|enum)\s+[a-zA-Z_$][\w$]*",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\b(try|catch|finally|satisfies|unknown|never|void|Object\.freeze|z\.(?:string|object|parse)|v\.(?:string|parse))\b|\?\?|\?\.|\b(?:is|asserts)\s+\w+\b"
            ),
            # 7. safety_neg (The Fractures)
            # Force unwrapping, any, and linter bypasses.
            "safety_neg": re.compile(
                r"\b(any)\b|as\s+any|!\s*[;,\n)\]\.]|!\.|@ts-ignore|@ts-expect-error|@ts-nocheck|eslint-disable|as\s+unknown\s+as|<any>"
            ),
            # 8. danger (The Heavy Load)
            # Process killers and catastrophic vulnerabilities. EXCLUDES TODO (debt) and console.log (print).
            "danger": re.compile(
                r"\b(eval|document\.write|innerHTML|outerHTML|dangerouslySetInnerHTML|debugger|alert|process\.exit)\b"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(fetch|axios|http|https|fs|path|database|sql|localStorage|sessionStorage|indexedDB|document\.cookie|XMLHttpRequest|child_process|fs/promises)\b"
            ),
            # 10. api (The Event Horizon)
            # Captures explicit exports and public visibility.
            "api": re.compile(
                r"\b(export|public|module\.exports|exports\.)\b|@(Controller|Resolver|Get|Post|Put|Delete)\b"
            ),
            # 11. flux (The Boiling Plasma)
            # Mutation of state. EXCLUDES const (freeze_hits).
            "flux": re.compile(
                r"\b(let|var|this\.|setState|push|pop|shift|unshift|splice|sort|reverse|\.current[ \t]*=|\.set\(|\.delete\(|\.add\()\b"
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"//[ \t]*(?:if|for|while|function|class|return|export|import)\b"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r"/\*\*|@param|@return|@throws|@deprecated|@typedef|@type|@template|@callback"
            ),
            # 14. test (The Verification)
            # CRITICAL FIX: Negative lookbehind (?<!\.) prevents matching 'regex.test()' as an assertion.
            "test": re.compile(
                r"\b(?:describe|expect|beforeEach|afterEach|jest|vitest|playwright)\s*\(|(?<!\.)\b(?:it|test|assert)\s*\("
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Hidden Complexity) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(async|await|Promise|requestAnimationFrame|setImmediate|setTimeout|setInterval|Worker|postMessage|Observable|Subject|Subscription)\b"
            ),
            # 16. ui_framework (The View Layer)
            "ui_framework": re.compile(
                r'<[A-Z]\w+|className=|use(?:State|Effect|Context|Reducer|Ref|Memo|Callback|Transition|Id)|props\.|this\.state|@Component|@Injectable|document\.(?:getElementById|querySelector)|["\']use\s+(?:client|server)["\']'
            ),
            # 17. closures (The Functional Depth)
            "closures": re.compile(
                r"=>[ \t]*\{|\(\)[ \t]*=>|function\s*\([^)]*\)[ \t]*\{"
            ),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\b(window\.|global\.|process\.env|document\.|navigator\.|self\.|globalThis\.)\b"
            ),
            # 19. decorators (The Metadata Hooks)
            "decorators": re.compile(r"@\w+(?:\([^)]*\))?"),
            # 20. generics (The Type Abstractions)
            "generics": re.compile(
                r"<\s*[A-Z][^>]*>|\b(?:keyof|infer|extends|Omit|Pick|Partial|Record|Required|Awaited|ReturnType|Parameters|NonNullable)\b"
            ),
            # 21. comprehensions (The High-Density Loops)
            "comprehensions": re.compile(
                r"\.(?:map|filter|reduce|flatMap|some|every|find|forEach|groupBy)\s*\("
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(Math\.|tf\.|THREE\.|d3\.|gl-matrix|random)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            "heat_triggers": re.compile(
                r"\b(arguments\.|prototype|__proto__|Object\.assign|Reflect|Proxy|Object\.defineProperty|\.bind\(|\.call\(|\.apply\()\b"
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(
                r"^[ \t]*(?:import(?:\s+type)?|export(?:\s+type)?)\b[^;]*?\bfrom\b|\brequire\s*\(|import\s*\(",
                re.M,
            ),
            
            "_dependency_capture": re.compile(r"(?:import(?:\s+type)?|export(?:\s+type)?)\b[^;]*?\bfrom\s*['\"]([^'\"]+)['\"]|\b(?:require|import)\s*\(\s*['\"]([^'\"]+)['\"]", re.M),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(r"(?:@author|Created by)\s+(.*)", re.I),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": re.compile(
                r"\b(getServerSideProps|getStaticProps|generateStaticParams|LoaderFunction|ActionFunction)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(emit|on|once|off|dispatchEvent|EventEmitter|EventTarget)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\b(Inject|Injectable|Container|resolve|register|tsyringe|inversify)\b"
            ),
            # 34. macros
            "macros": None,  # TypeScript uses transformer plugins/pre-processors, not standard inline macros.
            # 35. pointers
            "pointers": None,  # Managed memory environment.
            # 36. memory_alloc (The Yin to cleanup)
            "memory_alloc": re.compile(r"\bnew\s+[A-Z]\w*"),
            # 37. inline_asm
            "inline_asm": None,
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(logger|winston|pino|morgan|datadog|prometheus|newrelic|sentry)\.(?:info|error|warn|debug|trace|log)\b"
            ),
            # 39. print_hits (The Amateur)
            "print_hits": re.compile(
                r"\bconsole\.(?:log|warn|error|dir|trace|info|table|time)\b"
            ),
            # 40. cast_hits (The Trust Me Tax)
            "cast_hits": re.compile(r"\bas\s+[A-Z]\w*|<\s*[A-Z]\w*\s*>\s*[a-zA-Z_]"),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(throw|fatalError|abort|process\.exit)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(
                r"\b(sleep|delay|setTimeout|setInterval|Atomics\.wait)\b"
            ),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(r"<<|>>|\^|~"),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(mutex|lock|synchronized|Semaphore|Atomics\.lock|Atomics\.wait)\b",
                re.I,
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(
                r"\b(const|readonly|final|Object\.freeze|Object\.seal)\b"
            ),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r"\b(dispose|close|destroy|clearTimeout|clearInterval|removeEventListener|delete)\b"
            ),
            # 47. encapsulation (The Vault)
            "encapsulation": re.compile(r"\b(private|protected|internal|#)\b"),
            # 48. listeners (The Sinks)
            "listeners": re.compile(
                r"\b(on|addEventListener|subscribe|watch|effect)\b"
            ),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(
                r"\b(test\.skip|it\.skip|describe\.skip|xit|xdescribe|mock|stub)\b"
            ),
        },
    },
    "java": {
        "_meta": {
            "target_version": "Java 25 (Project Loom, Panama, Amber) / Spring Boot 3.4+",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard modern suffixes, server-side templates, and embedded scripting formats.
        "extensions": [".java", ".jav", ".jsp", ".jspf", ".jspx", ".jws", ".bsh"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Extensionless build/config scripts and tooling configs that are secretly pure code.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Sibling extensions, package manifests, and lockfiles to resolve ambiguous files.
        "discriminators": [
            ".java",
            "pom.xml",
            "build.gradle",
            "build.gradle.kts",
            "settings.gradle",
            "build.xml",
            "mvnw",
            "gradlew",
            ".classpath",
            ".project",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1.
        "shebangs": ["java", "jshell"],
        # UPGRADED: Maps to Family 1 (Standard C)
        # Rationale: Uses '//' for line-level literature; multi-line literature
        # (/* */) is handled by the Section 2.3.C.3 Heuristic Pass.
        "lexical_family": "std_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Standard C-family line comment token (Includes Javadoc /**)
            "_line_anchor": re.compile(r"//"),
            # Inline comments follow the standard '//' delimiter.
            "_inline_comment": re.compile(r"//"),
            # Block comment start: /* (Standard non-recursive delimiter)
            "_block_start": re.compile(r"/\*"),
            # Block comment end: */
            "_block_end": re.compile(r"\*/"),
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Includes modern switch expressions (yield) and pattern guards (when).
            # EXCLUDES: Exceptions (throw) - moved to bailout_hits.
            "branch": re.compile(
                r"\b(if|else|switch|case|default|for|while|do|catch|finally|continue|break|yield|try|when)\b|\?|:"
            ),
            # 2. args (The Coupling Mass)
            # Captures method/constructor params and lambdas. Bounded to prevent ReDoS.
            "args": re.compile(
                r"(?:(?:@[\w.]+(?:\([^)]*\))?[ \t]*)*(?:public|protected|private|static|final|abstract|synchronized|native|default|strictfp|<[^>]*>)[ \t]+){0,5}(?:[\w<>\[\]?]+[ \t]+)?\w+\s*\([^)]*\)|(?:\([^)]*\)|[a-zA-Z_$][\w_$]*)\s*->|::",
                re.M,
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: Access modifiers (encapsulation) and final (freeze_hits).
            "linear": re.compile(
                r"\b(void|return|import|package|class|interface|enum|record|extends|implements|var|sealed|non-sealed|permits|new|throws|module|requires|exports|opens|provides|uses)\b"
            ),
            # 4. func_start (The Satellite Spawner)
            # ONLY executable logic blocks. EXCLUDES classes/interfaces. Steps over annotations.
            "func_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]+){0,10}(?:(?:public|protected|private|static|final|abstract|synchronized|native|default|<[^>]*>)[ \t]+){0,5}(?:[a-zA-Z_$][\w<>$\[\]?,]*[ \t]+){0,5}(?!(?:if|for|while|switch|catch|new|return|class|interface|enum|record)\b)([A-Za-z_$][\w_$]*)\s*\(",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            "class_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]*){0,5}(?:(?:public|protected|private|static|final|sealed|non-sealed|abstract|strictfp)[ \t]+){0,5}(?:class|interface|enum|record)\s+[A-Za-z_$][\w_$]*",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\b(try|catch|finally|assert|Optional|Objects\.requireNonNull|instanceof)\b|@(Valid|Validated|NotNull|NonNull|NotBlank|Immutable|Transactional)\b"
            ),
            # 7. safety_neg (The Fractures)
            "safety_neg": re.compile(
                r"\b(null)\b|return\s+null|\([A-Z]\w+\)\s*(?!->)[a-zA-Z_$]|catch\s*\(\s*(?:Exception|Throwable)\b|@SuppressWarnings|@SneakyThrows|\.get\(\)"
            ),
            # 8. danger (The Heavy Load)
            # Process killers and raw memory/execution risks. EXCLUDES prints (Phase 5).
            "danger": re.compile(
                r"\b(Runtime\.getRuntime\(\)\.exec|ProcessBuilder|System\.exit|Thread\.stop|Unsafe)\b"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(File|InputStream|OutputStream|Reader|Writer|Scanner|Files\.|Path|Socket|RestTemplate|WebClient|RestClient|HttpClient|Connection|ResultSet|Statement|EntityManager|DataSource|Repository)\b"
            ),
            # 10. api (The Event Horizon)
            "api": re.compile(
                r"\b(public|protected)\b|@(RestController|Controller|Service|Component|Bean|Produces|Consumes|RequestMapping|GetMapping|PostMapping|PutMapping|DeleteMapping|PatchMapping|Endpoint|WebFilter)\b"
            ),
            # 11. flux (The Boiling Plasma)
            # Mutation of state. EXCLUDES final (freeze_hits).
            "flux": re.compile(
                r"\b(volatile|Atomic\w+)\b|^[ \t]*(?:this\.)?\w+[ \t]*=|@(?:Setter|Data)\b|(?:\w+\.)?(?:set[A-Z]\w+|add|put|remove|clear|addAll|replace|computeIfAbsent)\s*\("
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"//[ \t]*(?:public|private|protected|class|void|if|for|while|return|import)\b"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r"/\*\*|@param|@return|@throws|@deprecated|@see|@since|@apiNote|@implSpec|@Operation|@Schema"
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r"@(?:Test|ParameterizedTest|Before|After|BeforeEach|AfterEach|Mock|InjectMocks)|assert[A-Za-z0-9_]*\s*\(|\b(?:verify|expect|given|when)\s*\("
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Complexity) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(synchronized|Thread|Runnable|Future|CompletableFuture|ExecutorService|Semaphore|Atomic\w+|VirtualThread|StructuredTaskScope|ScopedValue|Mono|Flux|Publisher)\b|@(?:Async|Scheduled)"
            ),
            # 16. ui_framework (The View Layer)
            "ui_framework": re.compile(
                r"\b(SwingUtilities|JFrame|JPanel|javafx\.|ModelAndView|ModelMap|Model|@ModelAttribute|VaadinSession|FacesContext|UIComponent)\b"
            ),
            # 17. closures (The Functional Depth)
            "closures": re.compile(r"->|::"),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\b(System\.getProperty|System\.getenv|public\s+static\s+(?:final[ \t]+)?\w+\s+[A-Z_0-9]+[ \t]*=|ThreadLocal|ScopedValue)\b|@(?:Value|ConfigurationProperties)"
            ),
            # 19. decorators (The Metadata Hooks)
            "decorators": re.compile(r"^[ \t]*@[\w.]+(?:\([^)]*\))?", re.M),
            # 20. generics (The Type Abstractions)
            "generics": re.compile(r"<\s*[A-Z?][^>]*>"),
            # 21. comprehensions (The High-Density Loops)
            "comprehensions": re.compile(
                r"\.(?:stream|parallelStream|map|filter|reduce|collect|flatMap|forEach|anyMatch|noneMatch|gather)\("
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(Math\.|BigDecimal|BigInteger|Random|SecureRandom|StrictMath|VectorSpecies|FloatVector|IntVector)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Reflection and dynamic proxies.
            "heat_triggers": re.compile(
                r"\b(reflect\.|native|Class\.forName|Method\.invoke|Field\.setAccessible|Proxy\.newProxyInstance|ClassLoader|MethodHandles|VarHandle|Linker\.nativeLinker)\b|@SneakyThrows"
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(r"^[ \t]*import\s+(?:static[ \t]+)?[\w.]+;", re.M),
            
            "_dependency_capture": re.compile(r"^[ \t]*import\s+(?:static[ \t]+)?([\w.]+);", re.M),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(r"@author\s+(.*)", re.I),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": re.compile(
                r"\b(ModelAndView|FacesServlet|HttpServletRequest|HttpServletResponse|@ResponseBody|@ResponseStatus|JspWriter|ThymeleafViewResolver)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(ApplicationEvent|ApplicationEventPublisher|ApplicationListener|@EventListener|@KafkaListener|@RabbitListener|@JmsListener|EventObject|publishEvent)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\b(@Autowired|@Inject|@Qualifier|@Primary|@Component|@Service|@Repository|@Bean|@Configuration|ApplicationContext|BeanFactory|@Provides)\b"
            ),
            # 34. macros
            "macros": None,  # Java lacks preprocessor macros.
            # 35. pointers (The Memory Map)
            # Project Panama (Java 22+) bridging to native memory.
            "pointers": re.compile(
                r"\b(MemorySegment|MemoryLayout|ValueLayout|AddressLayout|SymbolLookup)\b"
            ),
            # 36. memory_alloc (The Yin to cleanup)
            "memory_alloc": re.compile(
                r"\b(Arena\.ofConfined|Arena\.ofShared|Arena\.ofAuto|Arena\.global|SegmentAllocator|allocateFrom|ByteBuffer\.allocateDirect)\b"
            ),
            # 37. inline_asm
            "inline_asm": None,
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(log|logger|LOGGER|LoggerFactory|LogManager|MDC|Tracer|Span)\.(?:info|error|warn|warning|debug|trace|log)\b|@Slf4j|@Log4j2"
            ),
            # 39. print_hits (The Amateur)
            "print_hits": re.compile(
                r"\b(System\.out\.(?:print|println|printf)|System\.err\.(?:print|println|printf)|\.printStackTrace\(\))\b"
            ),
            # 40. cast_hits (The Trust Me Tax)
            "cast_hits": re.compile(
                r"\(\s*(?:int|long|short|byte|char|float|double|boolean|[A-Z][A-Za-z0-9_]*)\s*\)\s*[a-zA-Z_$]"
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(throw|abort|System\.exit|halt)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(
                r"\b(Thread\.sleep|TimeUnit\.[A-Z_]+\.sleep|delay|CountDownLatch\.await)\b"
            ),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(r"<<|>>>?|\^|~"),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(mutex|lock|synchronized|Semaphore|ReentrantLock|ReadWriteLock|Condition)\b",
                re.I,
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(
                r"\b(final|immutable|unmodifiable[A-Z]\w*|Object\.freeze)\b"
            ),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r"\b(close|dispose|shutdown|free|release|cleaner\.register)\b\s*\("
            ),
            # 47. encapsulation (The Vault)
            "encapsulation": re.compile(r"\b(private|protected|internal)\b"),
            # 48. listeners (The Sinks)
            "listeners": re.compile(
                r"\b(on[A-Z]\w*|addEventListener|subscribe|@KafkaListener|@RabbitListener)\b"
            ),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(
                r"@(?:Ignore|Disabled)|test\.skip\(|mock\(|spy\(|verifyZeroInteractions"
            ),
        },
    },
    "csharp": {
        "_meta": {
            "target_version": "C# 14 / .NET 10 / Modern ASP.NET Core & Blazor",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard modern suffixes, legacy ASP.NET, and build-tooling formats.
        "extensions": [
            ".cs",
            ".csx",
            ".razor",
            ".cshtml",
            ".cake",
            ".linq",
            ".ashx",
            ".asmx",
            ".ascx",
            ".svc",
        ],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Extensionless build/config scripts and tooling configs that are secretly pure code.
        "exact_matches": ["build.cake"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Sibling extensions, package manifests, and lockfiles to resolve ambiguous files.
        "discriminators": [
            ".cs",
            ".csproj",
            ".sln",
            "packages.config",
            "nuget.config",
            "global.json",
            "App.config",
            "Web.config",
            "project.json",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1.
        "shebangs": ["dotnet-script", "csi"],
        # UPGRADED: Maps to Family 1 (Standard C)
        # Rationale: Uses '//' for line-level literature; multi-line literature
        # (/* */) is handled by the Section 2.3.C.3 Heuristic Pass.
        "lexical_family": "std_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Standard C-family line comment token (Includes XML Doc ///)
            "_line_anchor": re.compile(r"//"),
            # Inline comments follow the standard '//' delimiter.
            "_inline_comment": re.compile(r"//"),
            # Block comment start: /* (Standard non-recursive delimiter)
            "_block_start": re.compile(r"/\*"),
            # Block comment end: */
            "_block_end": re.compile(r"\*/"),
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Decisions and logical jumps. EXCLUDES throw (bailout_hits).
            # Includes pattern matching (and, or, not) and null-coalescing.
            "branch": re.compile(
                r"\b(if|else|switch|case|default|for|foreach|while|do|catch|finally|continue|break|goto|try|yield\s+return|yield\s+break|and|or|not)\b|\?\?|\?"
            ),
            # 2. args (The Coupling Mass)
            # Parameter blocks for methods, primary constructors, and lambdas.
            "args": re.compile(
                r"(?:(?:\[[^\]]*\][ \t]*)*(?:public|private|protected|internal|static|virtual|override|abstract|sealed|async|unsafe|partial|new|extern|file|ref|scoped|readonly)[ \t]+){0,5}(?:[\w<>\[\]?]+[ \t]+)?\w+\s*\([^)]*\)|(?:\([^)]*\)|[a-zA-Z_$][\w_$]*)[ \t]*=>",
                re.M,
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: Access modifiers (encapsulation) and const/readonly (freeze_hits).
            "linear": re.compile(
                r"\b(var|return|class|interface|struct|record|enum|using|namespace|yield|await|delegate|event|init|required|field|implements|extends|declare)\b|=>"
            ),
            # 4. func_start (The Satellite Spawner)
            # ONLY executable logic blocks. EXCLUDES types/classes. Steps over attributes.
            "func_start": re.compile(
                r"^[ \t]*(?:\[[^\]]*\][ \t]*){0,5}(?:(?:public|private|protected|internal|static|virtual|override|abstract|sealed|async|unsafe|partial|new|extern|file)[ \t]+){0,5}(?:[\w<>\[\]?,\s]+[ \t]+)?(?!(?:if|for|foreach|while|switch|catch|using|lock|new|return|class|interface|struct|record|enum)\b)([A-Za-z_$][\w_$]*)\s*\(",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            "class_start": re.compile(
                r"^[ \t]*(?:\[[^\]]*\][ \t]*){0,5}(?:(?:public|internal|private|protected|static|sealed|abstract|partial|file|unsafe|new)[ \t]+){0,5}(?:class|interface|struct|record|enum)\s+[A-Za-z_$][\w_$]*",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\b(try|catch|finally|checked|is|as|nameof|required|ArgumentNullException|ThrowIfNull|ThrowIfNullOrWhiteSpace)\b|\[(?:Required|NotNull|Authorize)\]|\?\?|\?\."
            ),
            # 7. safety_neg (The Fractures)
            # Null-forgiving operator, dynamic, and unsafe bypasses.
            "safety_neg": re.compile(
                r"!\.|\bnull!|#pragma\s+warning\s+disable|\.Result\b|\.Wait\(\)|\b(dynamic)\b"
            ),
            # 8. danger (The Heavy Load)
            # Extreme tech debt/vulnerabilities. EXCLUDES TODO (debt) and Console (print).
            "danger": re.compile(
                r"\b(Thread\.Abort|Process\.Start|Environment\.FailFast|Environment\.Exit|goto)\b"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(File|Directory|Stream|HttpClient|Path|SqlConnection|SqlCommand|DbContext|DbSet|HttpRequest|HttpResponse)\b\.|\[Table\("
            ),
            # 10. api (The Event Horizon)
            # Public exposure surface. Explicit visibility + Controller mapping.
            "api": re.compile(
                r"\b(public|internal)\b|\[(?:HttpGet|HttpPost|HttpPut|HttpDelete|Route|ApiController|HubMethodName)\]|\bapp\.Map(?:Get|Post|Put|Delete|Group)\b"
            ),
            # 11. flux (The Boiling Plasma)
            # Mutation of state. EXCLUDES const/readonly (freeze_hits).
            "flux": re.compile(
                r"\b(set|field)\s*[{;]|volatile|ref\s|out\s|^[ \t]*(?:this\.)?\w+[ \t]*=|(?:\w+\.)?(?:Add|Remove|Clear|Insert|Push|Pop|Update)\s*\("
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"//[ \t]*(?:public|private|protected|internal|class|void|if|for|foreach|while|return|using)\b"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r"///|///\s*<summary>|///\s*<param|///\s*<returns>|///\s*<remarks>"
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r"\[(?:Test|Fact|Theory|TestMethod|TestClass|SetUp|TearDown)\]|\b(?:Assert\.|Should\(\)|Mock\.|Substitute\.For)\b"
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Domain) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(async|await|Task|ValueTask|Thread|Parallel|SemaphoreSlim|Mutex|Channel|IAsyncEnumerable|Interlocked)\b"
            ),
            # 16. ui_framework (The View Layer)
            "ui_framework": re.compile(
                r"\b(ControllerBase|IActionResult|Binding|ObservableCollection|DependencyProperty|ComponentBase|RenderFragment|MonoBehaviour)\b"
            ),
            # 17. closures (The Functional Depth)
            "closures": re.compile(r"=>|delegate[ \t]*\{"),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\b(ConfigurationManager|Environment\.|public\s+static\s+(?:readonly[ \t]+)?[\w<>]+\s+[A-Z_0-9]+[ \t]*=|AsyncLocal)\b|\[ThreadStatic\]"
            ),
            # 19. decorators (The Metadata Hooks)
            "decorators": re.compile(r"^[ \t]*\[[A-Za-z_][^\]]*\]", re.M),
            # 20. generics (The Type Abstractions)
            "generics": re.compile(r"<\s*[A-Z][^>]*>|\bwhere\s+\w+\s*:"),
            # 21. comprehensions (The High-Density Loops)
            "comprehensions": re.compile(
                r"\.(?:Select|Where|OrderBy|GroupBy|Aggregate|Any|All|ToList|ToArray|SelectMany)\(|^[ \t]*from\s+\w+\s+in\s+",
                re.M,
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(Math\.|MathF\.|Vector[234]|Matrix4x4|Random|Complex|Tensor|TensorPrimitives)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Reflection and dynamic Emit.
            "heat_triggers": re.compile(
                r"\b(System\.Reflection|DllImport|LibraryImport|MethodInfo|Activator|Marshal\.|Emit|ILGenerator)\b"
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(
                r"^[ \t]*(?:global[ \t]+)?using\s+(?:static[ \t]+)?[\w.]+;", re.M
            ),
            
            "_dependency_capture": re.compile(r"^[ \t]*(?:global[ \t]+)?using\s+(?:static[ \t]+)?([\w.]+);", re.M),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(r"(?:<author>|Author:|Created by)\s*(.*)", re.I),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The Blazor/Razor Horizon)
            "ssr_boundaries": re.compile(
                r"@(?:page|rendermode|code|layout)|\[(?:Route|CascadingParameter)\]|\b(RenderFragment|ComponentBase|IViewComponentResult)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(event\s+[\w<>]+\s+\w+|EventHandler|\+=\s*|-=\s*|Invoke|Raise|MediatR|INotification|IRequest|Publish)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\b(IServiceCollection|AddTransient|AddScoped|AddSingleton|AddKeyed|\[Inject\]|FromServices|IServiceProvider)\b"
            ),
            # 34. macros (The Preprocessor Hooks)
            "macros": re.compile(
                r"^[ \t]*#(?:define|undef|if|elif|else|endif|region|endregion|pragma|warning|error)\b",
                re.M,
            ),
            # 35. pointers (The Memory Map)
            # Native pointers and modern memory structures (Span/Memory).
            "pointers": re.compile(
                r"\b(?:fixed|stackalloc|Unsafe\.AsPointer|IntPtr|UIntPtr|nint|nuint)\b|->"
            ),
            # 36. memory_alloc (Manual Memory Management)
            "memory_alloc": re.compile(
                r"\b(Marshal\.AllocHGlobal|GC\.AllocateArray|MemoryPool|ArrayPool<[^>]*>\.Shared\.Rent|ref\s+struct|scoped\s+ref)\b"
            ),
            # 37. inline_asm
            "inline_asm": None,
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(?:ILogger|_logger|Log|TelemetryClient|ActivitySource)\.(?:LogInformation|LogError|LogWarning|LogDebug|StartActivity|TrackEvent)\b|\[LoggerMessage"
            ),
            # 39. print_hits (The Amateur)
            "print_hits": re.compile(
                r"\b(Console\.(?:Write|WriteLine|Error)|Debug\.(?:Write|WriteLine|Print))\b"
            ),
            # 40. cast_hits (The Trust Me Tax)
            "cast_hits": re.compile(
                r"\bas\s+[A-Z]\w*|\(\s*(?:int|long|short|byte|char|float|double|decimal|bool|string|[A-Z][A-Za-z0-9_]*)\s*\)\s*[a-zA-Z_$]"
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(throw|abort|FailFast|Environment\.Exit)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(
                r"\b(sleep|delay|Wait\(\)|Task\.Delay|Thread\.Sleep)\b"
            ),
            # 43. bitwise_hits (The Sub-Atomic Math)
            # Low-level byte manipulation. Safely maps to C# bitwise operators without overlapping language-specific pipelines.
            "bitwise_hits": re.compile(r"<<|>>|\^|~"),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(mutex|lock|Monitor|Semaphore|Interlocked|SpinLock|ReaderWriterLockSlim)\b",
                re.I,
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(r"\b(const|readonly|init|Immutable[A-Z]\w*)\b"),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r"\b(dispose|close|free|delete|GC\.Collect|GC\.SuppressFinalize)\b\s*\("
            ),
            # 47. encapsulation (The Vault)
            "encapsulation": re.compile(r"\b(private|protected|internal|file)\b"),
            # 48. listeners (The Sinks)
            "listeners": re.compile(
                r"\b(on|addEventListener|subscribe|EventHandler)\b|\+="
            ),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(
                r"\[(?:Ignore|Skipped)\]|test\.skip\(|mock\(|stub\(|Substitute\.For"
            ),
        },
    },
    "go": {
        "_meta": {
            "target_version": "Go 1.22+ (Generics, Slog, Workspace paradigms)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        "extensions": [".go"],
        "exact_matches": [],
        "discriminators": [
            ".go",
            "go.mod",
            "go.sum",
            "go.work",
            "Gopkg.toml",
            "Gopkg.lock",
            "glide.yaml",
            "vendor/modules.txt",
        ],
        "shebangs": ["go", "gorun", "yaegi"],
        "lexical_family": "std_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Standard C-family line comment token.
            "_line_anchor": re.compile(r"//"),
            # Inline comments follow the standard '//' delimiter.
            "_inline_comment": re.compile(r"//"),
            # Block comment start: /* (Standard non-recursive delimiter).
            "_block_start": re.compile(r"/\*"),
            # Block comment end: */
            "_block_end": re.compile(r"\*/"),
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Includes select/case and range-based loops. EXCLUDES panic (bailout_hits).
            "branch": re.compile(
                r"\b(if|else|switch|case|default|for|range|select|goto|break|continue|fallthrough)\b|&&|\|\|"
            ),
            # 2. args (The Coupling Mass)
            # Parameter blocks for functions and methods. Bounded generics [^\]]* and params [^)]*.
            "args": re.compile(
                r"func\s+(?:\([^)]*\)[ \t]+)?\w*(?:\[[^\]]*\])?\s*\([^)]*\)", re.M
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: const/var (freeze_hits) and Capitalization (encapsulation).
            "linear": re.compile(
                r"\b(package|import|return|type|go|defer|chan|map|interface|struct)\b"
            ),
            # 4. func_start (The Satellite Spawner)
            # ONLY executable logic blocks.
            # Bypasses the 'func' keyword, skips optional method receivers (e.g. (s *Server)),
            # and strictly captures the actual identifier name. Ignores anonymous functions.
            "func_start": re.compile(
                r"^[ \t]*func(?:[ \t]+\([^)]+\))?[ \t]+([A-Za-z_$][\w_$]*)[ \t]*\(",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            # Go's equivalent to classes: struct/interface type definitions.
            "class_start": re.compile(
                r"^[ \t]*type\s+[a-zA-Z_]\w*(?:\[[^\]]*\])?\s+(?:struct|interface)",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"err\s*!=\s*nil|\b(errors\.(?:Is|As|New|Join)|sync\.(?:Once|WaitGroup)|context\.Context|recover\(\))\b"
            ),
            # 7. safety_neg (The Fractures)
            # Explicitly ignoring errors via blank identifier.
            "safety_neg": re.compile(
                r'_\s*,\s*err[ \t]*=|_[ \t]*=\s*\w+|\bimport\s+(?:\.[ \t]+)?"'
            ),
            # 8. danger (The Heavy Load)
            # Process-killing commands and direct syscalls. EXCLUDES TODO (debt) and fmt.Print (print_hits).
            "danger": re.compile(
                r"\b(os\.Exit|syscall\.Kill|syscall\.RawSyscall|log\.Fatal(?:f|ln)?)\b"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(os\.(?:Open|Create|ReadFile)|io\.(?:Reader|Writer|Copy)|net/http|database/sql|bufio\.|grpc\.|sqlx\.|pgx\.)\b"
            ),
            # 10. api (The Event Horizon)
            # Implicit Public Reality: Capitalized top-level identifiers in Go are public.
            "api": re.compile(
                r"^[ \t]*(?:func\s+(?:\([^)]*\)[ \t]+)?)?[A-Z]\w+|^[ \t]*(?:type|var|const)\s+[A-Z]\w+",
                re.M,
            ),
            # 11. flux (The Boiling Plasma)
            # Mutation of state. Reassignment and channel sends.
            "flux": re.compile(
                r":=|(?<![=!<>])=(?![=])|<-|\bappend\(|\batomic\.(?:Add|Store|Swap)"
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"//[ \t]*(?:func|type|var|const|import|if|for|switch|select|return)\b"
            ),
            # 13. doc (The Intent)
            # GoDoc standard: comments immediately preceding a declaration.
            "doc": re.compile(
                r"^[ \t]*//\s+[A-Z][a-zA-Z0-9_]+\s+.*|^[ \t]*//\s*Package\s+", re.M
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r"\b(?:Test|Benchmark|Fuzz)[A-Z]\w*\b|t\.Run\b|\b(?:assert|require|mock)\.\w+\("
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Complexity) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(go\s+func|go\s+\w+|chan\s+|select[ \t]*\{|context\.(?:WithTimeout|WithCancel)|errgroup\.Group)\b"
            ),
            # 16. ui_framework (The View Layer)
            # Go is primarily backend; targets templates and web handlers.
            "ui_framework": re.compile(
                r"\b(html/template|text/template|http\.HandleFunc|ServeHTTP|gin\.|echo\.|fiber\.)\b"
            ),
            # 17. closures (The Functional Depth)
            "closures": re.compile(
                r"func\s*\([^)]*\)\s*(?:\[[^\]]*\])?\s*(?:\([^)]*\))?[ \t]*\{"
            ),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"^[ \t]*var\s+[a-zA-Z_]\w*\s*(?:[a-zA-Z_]\w*\s*)?=|os\.Getenv|os\.Environ",
                re.M,
            ),
            # 19. decorators (The Metadata Hooks)
            # Go lacks @decorators; uses Struct Tags and Build Tags.
            "decorators": re.compile(
                r'`[^`]*?(?:json|xml|yaml|gorm|db|bson):"[^"]*"[^`]*?`|//go:build|//\s*\+build'
            ),
            # 20. generics (The Type Abstractions)
            "generics": re.compile(
                r"\[[^\]]*\b(?:any|comparable|~[a-zA-Z_]\w*)\b[^\]]*\]|\bany\b"
            ),
            # 21. comprehensions (The High-Density Loops)
            # Functional iteration helpers from the slices/maps packages.
            "comprehensions": re.compile(
                r"\b(slices\.(?:Delete|Filter|Sort|Compact)|maps\.(?:Keys|Values))\b"
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(math\.|math/cmplx\.|math/rand\.|crypto/rand\.|gonum\.)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Reflection, CGO, and Unsafe triggers.
            "heat_triggers": re.compile(
                r'import\s+"C"|\b(reflect\.|unsafe\.|cgo|go:linkname)\b'
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(r'^[ \t]*import\s*(?:\(|"[^"]+")', re.M),
            
            # ---> THE FIX: Strictly bounded to valid Go import path characters <---
            # Prevents raw HTTP string literals in test files from being hallucinated as packages.
            "_dependency_capture": re.compile(r'^[ \t]*(?:import\s+)?(?:\(\s*)?(?:[a-zA-Z0-9_.]+\s+)?["`]([a-zA-Z0-9_.\-/]+)["`]', re.M),
                        
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"(?://|#|/\*)\s*(?:Author|Maintainer|Created by|Owner):?\s+([a-zA-Z0-9_ -]+)",
                re.I,
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            # Gofmt mandates tabs; finding spaces at start signals structural friction.
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": re.compile(
                r"\b(html/template|ExecuteTemplate|http\.ResponseWriter|Render|gin\.Context)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(EventBus|Publish|Subscribe|kafka\.|rabbitmq\.|Emit|OnEvent)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\b(wire\.Build|wire\.NewSet|fx\.New|fx\.Provide|fx\.Invoke|dig\.Provide|do\.Provide)\b"
            ),
            # 34. macros (The Preprocessor Hooks)
            # Go lacks a preprocessor; //go: directives act as compile-time hooks.
            "macros": re.compile(
                r"^//go:(?:generate|build|noinline|nosplit|noescape|linkname)\b", re.M
            ),
            # 35. pointers (The Memory Map)
            # Explicit pointer addressing and dereferencing.
            "pointers": re.compile(
                r"\b(?:uintptr|unsafe\.Pointer)\b|&\w+|\*(?:[A-Z]\w*|int\d*|uint\d*|float\d*|byte|rune|string|bool)\b"
            ),
            # 36. memory_alloc (Manual Memory Management)
            "memory_alloc": re.compile(r"\b(make|new)\s*\(|sync\.Pool\b"),
            # 37. inline_asm
            "inline_asm": None,  # Go handles ASM in separate .s files.
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(slog|logrus|zap|zerolog|log)\.(?:Info|Warn|Error|Debug|Trace)(?:f|ln)?\b|\btrace\.Span\b"
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(
                r"\b(fmt\.Print|fmt\.Println|fmt\.Printf|println|print)\b"
            ),
            # 40. cast_hits (The "Trust Me" Tax)
            # Type assertions and conversions.
            "cast_hits": re.compile(
                r"\.\([a-zA-Z_]\w*\)|\b(?:int|int8|int16|int32|int64|uint|uint8|uint16|uint32|uint64|float32|float64|byte|rune|uintptr|string)\s*\("
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(panic|os\.Exit|log\.Fatal)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\b(time\.Sleep|time\.After|runtime\.Gosched)\b"),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(r"<<|>>|\^|&\^"),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(Mutex|RWMutex|Lock|Unlock|RLock|RUnlock|atomic\.|sync\.Map|sync\.Pool)\b"
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(r"\bconst\b"),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r"\b(defer|Close|Unlock|RUnlock|Stop|Cleanup)\b\s*\("
            ),
            # 47. encapsulation (The Vault)
            # Unexported identifiers (lowercase) in Go are private/internal.
            "encapsulation": re.compile(
                r"^[ \t]*(?:func\s+(?:\([^)]*\)[ \t]+)?)?[a-z]\w+|^[ \t]*(?:type|var|const)\s+[a-z]\w+",
                re.M,
            ),
            # 48. listeners (The Sinks)
            "listeners": re.compile(r"<-chan\b|\.On\(|\.Subscribe\("),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(r"\bt\.Skip(?:f|Now)?\(|mock\.|gomock\."),
        },
    },
    "rust": {
        "_meta": {
            "target_version": "Rust 1.93.1 / Edition 2024 / Modern Async & Macro Stacks",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard modern suffixes, libraries, and metadata formats.
        "extensions": [".rs", ".rlib", ".rmeta"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Extensionless build/config scripts and tooling configs that are secretly pure code.
        "exact_matches": ["build.rs"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Sibling extensions, package manifests, and lockfiles to resolve ambiguous files.
        "discriminators": [
            ".rs",
            "Cargo.toml",
            "Cargo.lock",
            "rust-toolchain",
            "rust-toolchain.toml",
            "rustfmt.toml",
            "clippy.toml",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1.
        "shebangs": ["rustc", "cargo", "rust-script", "cargo-script", "evcxr"],
        # UPGRADED: Maps to Family 2 (Nested C)
        # Rationale: Rust explicitly allows nested block comments (/* /* */ */),
        # unlike standard C/C++. Standard C parsing would prematurely terminate here.
        "lexical_family": "nested_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Standard C-family line comment token (Includes /// and //!)
            "_line_anchor": re.compile(r"//"),
            # Inline comments follow the same '//' delimiter.
            "_inline_comment": re.compile(r"//"),
            # REQUIRED for Family 2: Recursive logic markers
            "_block_start": re.compile(r"/\*"),
            # REQUIRED for Family 2: Recursive logic markers
            "_block_end": re.compile(r"\*/"),
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Decisions and logical jumps. EXCLUDES panic!/throw (bailout_hits).
            "branch": re.compile(
                r"\b(if|else|match|for|while|loop|break|continue)\b|\?|&&|\|\|"
            ),
            # 2. args (The Coupling Mass)
            # Parameter blocks of functions and closures. Bounded to prevent ReDoS on complex types.
            "args": re.compile(
                r"\bfn\s+[a-zA-Z_]\w*(?:<[^>]*>)?\s*\([^)]*\)|\|[^|]*\|", re.M
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: Access modifiers (pub) and Immutability (const/static).
            "linear": re.compile(
                r"\b(let|struct|enum|union|trait|impl|use|mod|type|yield|await|where|mut|ref|move|return)\b"
            ),
            # 4. func_start (The Satellite Spawner)
            # ONLY executable logic blocks. EXCLUDES structs/traits to prevent Ghost Satellites.
            "func_start": re.compile(
                r'^[ \t]*(?:pub(?:\([^)]*\))?[ \t]+){0,3}(?:(?:const|async|unsafe|extern(?:[ \t]+"[^"]*")?)[ \t]+){0,3}fn[ \t]+([a-zA-Z_]\w*)(?:<[^>]*>)?(?=\s*\()',
                re.M,
            ),
            # 5. class_start (The Entity Census)
            "class_start": re.compile(
                r"^[ \t]*(?:pub(?:\([^)]*\))?[ \t]+){0,3}(?:struct|enum|union|trait)\s+[a-zA-Z_]\w*",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\b(Option|Result|Mutex|RwLock|Arc|Rc|Box|RefCell|match|if\s+let|while\s+let|let\s+else|Ok|Err|Some|None)\b"
            ),
            # 7. safety_neg (The Fractures)
            # Actively bypasses type safety (unwraps and forced expectations).
            "safety_neg": re.compile(
                r"\b(unwrap|expect|unwrap_err|unwrap_unchecked)\b"
            ),
            # 8. danger (The Heavy Load)
            # Process-killing commands. EXCLUDES TODO (debt) and println! (print_hits).
            "danger": re.compile(
                r"\b(panic!|todo!|unimplemented!|process::exit|abort)\b"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(std::fs|File::|std::net|tokio::net|tokio::fs|reqwest|std::io|hyper::|sqlx::|diesel::|sea_orm::)\b"
            ),
            # 10. api (The Event Horizon)
            # Code exposed to the outside world.
            "api": re.compile(r"\bpub(?:\([^)]*\))?\b"),
            # 11. flux (The Boiling Plasma)
            # Mutation of state. EXCLUDES const (freeze_hits).
            "flux": re.compile(
                r"\bmut\b|\.borrow_mut\(\)|\.write\(\)|Cell::|RefCell::|Atomic[A-Za-z0-9]+"
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"//[ \t]*(?:fn|let|struct|impl|mod|use|match|for|while|loop|if|return)\b"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(r"///|//!|#!?\[doc\b[^\]]*\]"),
            # 14. test (The Verification)
            # Triggers indicating internal verification. Anchors standard testing macros and prevents prose collisions for BDD frameworks (rstest/spec).
            "test": re.compile(
                r"#\[(?:tokio::)?test\]|#\[cfg\(test\)\]|\b(?:assert!|assert_eq!|assert_ne!)\b|\b(?:describe|it|test)\s*\("
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Domain) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(async|await|std::thread|spawn|tokio::spawn|mpsc::|async_trait|Future|Stream|Send|Sync)\b"
            ),
            # 16. ui_framework (The View Layer)
            "ui_framework": re.compile(
                r"\b(yew::|dioxus::|iced::|html!|rsx!|view!|slint|leptos::|tauri::)\b"
            ),
            # 17. closures (The Functional Depth)
            "closures": re.compile(r"\|[^|]*\|[ \t]*\{"),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\b(static\s+mut|lazy_static!|OnceCell|OnceLock|LazyLock|std::env::var)\b"
            ),
            # 19. decorators (The Metadata Hooks)
            "decorators": re.compile(r"^[ \t]*#!?\[[^\]]*\]", re.M),
            # 20. generics (The Type Abstractions)
            "generics": re.compile(
                r"<\s*[A-Z\'][^>]*>|\bwhere\b|\'[a-z]+\b|\bimpl\s+[A-Z]\w+"
            ),
            # 21. comprehensions (The High-Density Loops)
            "comprehensions": re.compile(
                r"\.(?:map|filter|fold|collect|flat_map|any|all|reduce|for_each|find|zip)\s*\("
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(ndarray::|nalgebra::|num::|f32|f64|std::simd)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Metaprogramming and memory transmutation.
            "heat_triggers": re.compile(
                r"\b(macro_rules!|std::mem::transmute|Pin::|PhantomData|UnsafeCell)\b"
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(r"^[ \t]*(?:pub[ \t]+)?use\s+[^;]+;", re.M),
            
            "_dependency_capture": re.compile(r"^[ \t]*(?:pub[ \t]+)?use\s+([a-zA-Z0-9_:]+)", re.M),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"//\s*(?:Author|Maintainer|Copyright):\s+(.*)", re.I
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": re.compile(
                r"\b(actix_web|axum|rocket|HttpResponse|Responder|IntoResponse|Html|askama::|tera::)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(tokio::sync::broadcast|std::sync::mpsc|crossbeam_channel|Sender|Receiver)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\b(axum::extract::State|actix_web::web::Data|Extension|Provider|shaku::)\b"
            ),
            # 34. macros (The Preprocessor Hooks)
            "macros": re.compile(
                r"\b(macro_rules!|proc_macro|proc_macro_derive|proc_macro_attribute)\b"
            ),
            # 35. pointers (The Memory Map)
            # Raw memory addressing. Shielded from standard multiplication by explicitly mapping to native Rust unsafe pointer primitives and dereferencing.
            "pointers": re.compile(r"\*const\b|\*mut\b|\bNonNull\b|\bstd::ptr\b|->"),
            # 36. memory_alloc (Manual Memory Management)
            "memory_alloc": re.compile(
                r"\b(Box::new|Rc::new|Arc::new|Vec::with_capacity|String::with_capacity|alloc::|GlobalAlloc)\b"
            ),
            # 37. inline_asm (The Bare Metal)
            "inline_asm": re.compile(
                r"\b(?:core::arch::asm!|std::arch::asm!|asm!|global_asm!)\b"
            ),
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(?:log::|tracing::)?(?:info!|warn!|error!|debug!|trace!|span!|instrument)\b"
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(r"\b(println!|print!|eprintln!|eprint!|dbg!)\b"),
            # 40. cast_hits (The Trust Me Tax)
            # Forceful type coercion bypassing the safety engine. Enforces strict mapping to the `as` keyword followed by standard primitive types.
            "cast_hits": re.compile(
                r"\bas\s+(?:i8|i16|i32|i64|i128|isize|u8|u16|u32|u64|u128|usize|f32|f64|bool|char)\b"
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(panic!|abort|process::exit|fatalError)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(
                r"\b(std::thread::sleep|tokio::time::sleep|Duration::from)\b"
            ),
            # 43. bitwise_hits (The Sub-Atomic Math)
            # Low-level byte manipulation. CRITICAL: Removed the pipe '|' (used for closures `|x| x+1` and patterns), ampersand '&' (used for references), and exclamation '!' (used for macros and logical NOT).
            "bitwise_hits": re.compile(r"<<|>>|\^"),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(Mutex|RwLock|lock|barrier|atomic|Semaphore)\b", re.I
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(r"\b(const|static|immutable|readonly)\b"),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(r"\b(drop|free|delete|close|shutdown)\b\s*\("),
            # 47. encapsulation (The Vault)
            # Visibility variant tracking.
            "encapsulation": re.compile(r"\bpub(?:\(crate\)|\(super\)|\(self\))?\b"),
            # 48. listeners (The Sinks)
            "listeners": re.compile(r"\.subscribe\(|\.on\(|addEventListener"),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(r"#\[ignore\]|test\.skip\(|mock\(|fake\("),
        },
    },
    "cpp": {
        "_meta": {
            "target_version": "C++23 (Modules, Concepts, Coroutines, Ranges, std::print)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard sources, headers, template implementations, inline implementations, and legacy UNIX casing conventions.
        "extensions": [
            ".cpp",
            ".cc",
            ".cxx",
            ".c++",
            ".hpp",
            ".hh",
            ".hxx",
            ".h++",
            ".tpp",
            ".inc",
            ".inl",
            ".ipp",
            ".cp",
            ".C",
            ".H",
        ],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Extensionless build/config scripts and tooling configs that are secretly pure code.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, package manifests, and lockfiles to resolve ambiguous files (like .h or .inc).
        "discriminators": [
            ".cpp",
            ".cc",
            ".cxx",
            "CMakeLists.txt",
            "conanfile.txt",
            "vcpkg.json",
            "Makefile",
            "BUILD.bazel",
            "WORKSPACE",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1.
        "shebangs": ["cling", "cint"],
        # UPGRADED: Maps to Family 1 (Standard C)
        # Rationale: Uses '//' for line-level literature; multi-line literature
        # (/* */) is handled by the Section 2.3.C.3 Heuristic Pass.
        "lexical_family": "std_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # C++ uses '//' for standard line-level Literature (Ghost Mass).
            "_line_anchor": re.compile(r"//"),
            # Inline comments follow the standard '//' delimiter.
            "_inline_comment": re.compile(r"//"),
            # Block comment start: /* (Standard non-recursive delimiter).
            "_block_start": re.compile(r"/\*"),
            # Block comment end: */
            "_block_end": re.compile(r"\*/"),
            # 1. branch (The Forks in the Road)
            # Control flow jumps. Includes modern coroutine jumps (co_yield, co_await).
            # EXCLUDES exceptions (bailout_hits).
            "branch": re.compile(
                r"\b(if|else|switch|case|default|for|while|do|catch|break|continue|goto|co_yield|co_await)\b|&&|\|\||\?"
            ),
            # 2. args (The Coupling Mass)
            # Parameter blocks of functions and lambdas. Bounded to prevent ReDoS on massive signatures.
            "args": re.compile(
                r"\b[a-zA-Z_]\w*(?:::[a-zA-Z_]\w*)*(?:<[^>]*>)?\s*\(\s*(?:const\s+|volatile\s+)?(?:int|char|void|float|double|bool|long|short|unsigned|signed|struct|class|std::|[A-Z]\w*)\b[^)]*\)|\[[^\]]*\]\s*\([^)]*\)"
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: Access modifiers (encapsulation) and const (freeze_hits).
            "linear": re.compile(
                r"\b(namespace|using|class|struct|enum|union|template|typename|concept|requires|auto|return|void|inline|virtual|explicit|friend|module|export|import|typedef)\b"
            ),
            "func_start": re.compile(
                # =====================================================================
                # [LLM CONTEXT: C++ FUNCTION AST EXTRACTOR & REDOS SHIELD]
                # PURPOSE: Anchors executable logic blocks (methods/functions) in C++.
                # VULNERABILITY: C++ allows multi-line function signatures and complex 
                #   return types (e.g., `std::vector<int> \n myFunc()`). In files with 
                #   massive macro lists (like hardware register maps), the `[ \t\n]+` 
                #   allowances cause catastrophic backtracking (ReDoS).
                # THE "IRON WALL" FIX: `(?![ \t]*#)` is a negative lookahead injected at 
                #   high-risk multi-line boundaries. It explicitly forbids the regex engine 
                #   from crossing into preprocessor directives, capping the permutation tree.
                # =====================================================================

                # 1. THE HORIZONTAL ANCHOR (Stops O(N^2) vertical spirals)
                r"^[ \t]*"
                
                # 2. LINKAGE & STORAGE MODIFIERS (Now supports vertical formatting)
                r"(?:(?:static|inline|extern|virtual|_Noreturn|constexpr|consteval|constinit|__inline__|__forceinline)[ \t\n]+){0,5}"
                
                # 3. COMPILER ATTRIBUTES PRE-TYPE (Includes C23 [[...]])
                r"(?:(?:__attribute__[ \t]*\([^)]*\)|\[\[[^\]]*\]\]|__declspec[ \t]*\([^)]*\))[ \t\n]*){0,5}"
                
                # 4. THE RETURN TYPE (Pointers/references explicitly bound)
                # [IRON WALL]: Prevents the engine from reading a `#define` on the next line as a return type.
                r"(?:(?:struct|union|enum)[ \t\n]+)?"
                r"(?:(?![ \t]*#)[a-zA-Z_]\w*(?:::[a-zA-Z_]\w*)*(?:<[^>]*>)?(?:[ \t\n]+[*&]*[ \t\n]*|[*&]+[ \t\n]*)){0,5}"
                
                # 5. THE "NOT A FUNCTION" SHIELD
                # Prevents control flow (if, while) and primitive types from being captured as function names.
                r"(?!(?:if|for|while|switch|return|catch|else|elif|sizeof|new|delete|ARGS\d+|NOARGS|int|float|double|char|void|long|short|unsigned|signed|bool|INTEGER|LOGICAL|real|__attribute__|__declspec|__asm__)\b)"
                
                # 6. THE IDENTIFIER CAPTURE (SATELLITE NAME - GROUP 1)
                # [IRON WALL]: Ensures the actual function/operator name isn't hijacked by a macro definition.
                r"(?![ \t]*#)((?:[a-zA-Z_]\w*::)*[~a-zA-Z_]\w*|operator[ \t]*[^a-zA-Z_\s(]+|operator[ \t]+(?:new|delete)(?:\[\])?)"
                
                # 7. THE PARAMETER BLOCK (Supports vertical gap)
                r"[ \t\n]*(?:ARGS\d+\s*\([^)]*\)|\([^)]*\)|NOARGS)"
                
                # 8. POST-PARAMETER MODIFIERS & TRAILING RETURN TYPES
                r"(?:[ \t\n]+(?:const|volatile|noexcept|override|final|&{1,2}|__attribute__\s*\([^)]*\)|\[\[[^\]]*\]\])){0,10}"
                r"(?:[ \t\n]*->[ \t]*[a-zA-Z_:\w*<>]+)?"
                
                # 9. THE K&R C AND C++ CONSTRUCTOR GAP (ReDoS mitigated via Strict Bounding)
                # Handles C++ initializer lists (e.g., `MyClass() : a(1) {`) and legacy K&R declarations.
                # [IRON WALL - CATASTROPHIC BACKTRACKING FIX]: 
                # Previously, this used unbounded wildcards (`[^{;]+` and `[^(){};]*`). 
                # When parsing massive 50,000-line OS headers with complex macro arrays, 
                # the regex engine would attempt millions of permutations on failure, 
                # completely deadlocking the CPU (ReDoS) and causing starvation timeouts.
                # THE FIX: We enforce strict numeric bounds (`{0,500}` and `{0,100}`) 
                # instead of `+` or `*`. This caps the permutation tree instantly while 
                # perfectly accommodating valid constructor lists and K&R types.
                r"(?:[ \t\n]*(?![ \t]*#):[^{;]{0,500}|(?:[ \t\n]+(?![ \t]*#)[a-zA-Z_][^(){};]{0,100};){1,20})?"
                
                # 10. THE IGNITION (The opening brace confirming it is a definition, not a declaration)
                r"[ \t\n]*\{",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            "class_start": re.compile(
                r"^[ \t]*(?:export[ \t]+)?(?:template\s*<[^>]*>\s*)?(?:class|struct|union|enum\s+class|enum)\s+[a-zA-Z_]\w*",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\b(try|catch|finally|std::unique_ptr|std::shared_ptr|std::weak_ptr|override|final|noexcept|static_assert|assert|std::optional|std::expected|std::span|std::variant|std::lock_guard|std::atomic)\b"
            ),
            # 7. safety_neg (The Fractures)
            # Swallowing errors or bypassing types. EXCLUDES standard casting (Phase 5).
            "safety_neg": re.compile(
                r"\b(std::any|void\s*\*)\b|catch\s*\(\s*\.\.\.\s*\)"
            ),
            # 8. danger (The Heavy Load)
            # Process killers and low-level blits. EXCLUDES prints (Phase 5).
            "danger": re.compile(
                r"\b(system|memcpy|memset|abort|exit|std::terminate|longjmp|setjmp)\b"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(std::fstream|std::ifstream|std::ofstream|std::filesystem|fopen|fclose|fread|fwrite|socket|recv|send|asio::|curl_easy_perform|std::cin)\b"
            ),
            # 10. api (The Event Horizon)
            # Code exposed to the world. Explicit visibility and module exports.
            "api": re.compile(
                r'\b(public:|export\s+module|export\s+import|export\s+class|__declspec\(dllexport\)|__attribute__\(\(visibility\("default"\)\)\))\b|^[ \t]*export\b(?!\s*module)',
                re.M,
            ),
            # 11. flux (The Boiling Plasma)
            # Mutation of state. Includes moves and increments.
            "flux": re.compile(
                r"\b(mutable|std::move|std::exchange|std::swap|std::atomic)\b|(?<![=!<>])=(?![=])|&(?!\s*const)|\+\+|--|(?:\+=|-=|\*=|/=|%=|<<=|>>=|&=|\|=|\^=)"
            ),
            # 12. graveyard (The Necrosis)
            # Commented-out execution logic indicating dead features. MUST enforce that the structural keyword immediately follows the comment token.
            "graveyard": re.compile(
                r"//[ \t]*(?:if|for|while|auto|class|struct|std::cout|std::print|printf|void|int|return)\b"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r"///|/\*\*|@param|@return|@brief|@details|@tparam|\\param|\\return|\\brief|\\details|\\tparam"
            ),
            # 14. test (The Verification)
            # Triggers indicating internal verification. Anchors explicit GTest/Catch2 macros and prevents prose collisions.
            "test": re.compile(
                r"\b(?:TEST|TEST_F|TEST_CASE|SECTION|REQUIRE|CHECK|EXPECT_[A-Z_]+|ASSERT_[A-Z_]+|Catch::|GTest)\b"
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Domain) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(std::thread|std::jthread|std::mutex|std::future|std::promise|std::async|std::latch|std::barrier|std::condition_variable|std::semaphore|co_await|std::coroutine_handle)\b"
            ),
            # 16. ui_framework (The View Layer)
            "ui_framework": re.compile(
                r"\b(Q_OBJECT|slots:|signals:|QWidget|wxFrame|ImGui::|Fl_Window)\b"
            ),
            # 17. closures (The Functional Depth)
            "closures": re.compile(
                r"\[[^\]]*\]\s*(?:<[^>]*>\s*)?(?:\([^)]*\))?\s*(?:(?:mutable|constexpr|consteval|noexcept)\s+)*(?:mutable|constexpr|consteval|noexcept)?\s*(?:->\s*[\w:<>_]+)?[ \t]*\{"
            ),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\b(extern|static(?!\s*assert)|thread_local|inline\s+constexpr)\b|^[ \t]*(?:static|extern)\s+[\w:<>_]+\s+[a-zA-Z_]\w*[ \t]*=",
                re.M,
            ),
            # 19. decorators (The Metadata Hooks)
            "decorators": re.compile(r"\[\[\s*[a-zA-Z_:][^\]]*\]\]"),
            # 20. generics (The Type Abstractions)
            "generics": re.compile(r"\btemplate\s*<[^>]*>|\b(?:concept|requires)\b"),
            # 21. comprehensions (The High-Density Loops)
            # Range pipelines acting as functional mappers.
            "comprehensions": re.compile(
                r"\b(std::ranges::|std::views::|views::|std::transform|std::accumulate|std::reduce|std::for_each|std::filter)\b|\|\s*std::views::"
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(std::cmath|std::complex|std::linalg|std::mdspan|Eigen::|blaze::|std::simd|__m128|__m256|__m512|std::numbers::)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # SFINAE, compile-time reflection, and macros.
            "heat_triggers": re.compile(
                r"\b(if\s+constexpr|if\s+consteval|std::enable_if|std::is_same|std::any_cast|std::bit_cast|decltype|sizeof\.\.\.)\b|#define\s+[a-zA-Z_]"
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(
                r'^[ \t]*(?:#include\s*[<"][^>"]+[>"]|import\s+[a-zA-Z_][\w.:]*\s*;|export\s+import\s+[a-zA-Z_][\w.:]*\s*;)',
                re.M,
            ),
            
            "_dependency_capture": re.compile(r'^[ \t]*(?:#\s*include\s*[<"]([^>"]+)[>"]|(?:export\s+)?import\s+([a-zA-Z_][\w.:]*)\s*;)', re.M),
            
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"(?:@author|\\author|Author:|Created by:|Copyright)\s+(.*)", re.I
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": re.compile(
                r"\b(FCGI_Accept|render_template|Inja::|ctemplate::)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(emit|signal|slot|notify|publish|subscribe|boost::signals2)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\b(boost\.di|fruit::|[I]nject|IServiceCollection)\b"
            ),
            # 34. macros (The Preprocessor Hooks)
            "macros": re.compile(
                r"^[ \t]*#(?:define|undef|if|elif|else|endif|pragma|warning|error)\b",
                re.M,
            ),
            # 35. pointers (The Memory Map)
            # Raw memory addressing and pointer manipulation. CRITICAL: Uses lookbehinds `(?<=[=\s,(])` to strictly capture pointer dereferences `*ptr` and memory addresses `&var` without flagging standard multiplication `a * b` or logical AND `a & b`.
            "pointers": re.compile(
                r"->|\b(?:uintptr_t|intptr_t|ptrdiff_t|size_t)\b|(?<=[=\s,(])&\w+|(?<=[=\s,(])\*(?:\s*const\s*)?\w+"
            ),
            # 36. memory_alloc (Manual Memory Management)
            "memory_alloc": re.compile(
                r"\b(new|malloc|calloc|realloc|aligned_alloc|mmap|alloca)\b"
            ),
            # 37. inline_asm (The Bare Metal)
            "inline_asm": re.compile(
                r"\b(?:__asm__|asm|__asm)\b(?:\s+(?:volatile|__volatile__))?\s*\(|\b(?:__asm__|asm|__asm)\b[ \t]*\{"
            ),
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(log|logger|LOGGER|spdlog|glog|syslog)\.(?:info|error|warn|debug|trace)\b"
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(
                r"\b(std::cout|std::cerr|std::clog|printf|fprintf|vprintf|puts|putchar|std::print|std::println)\b"
            ),
            # 40. cast_hits (The "Trust Me" Tax)
            # Forceful type coercion bypassing the safety engine. Captures modern explicitly named casts and strict C-style groupings.
            "cast_hits": re.compile(
                r"\b(?:static_cast|dynamic_cast|reinterpret_cast|const_cast|bit_cast)\b|<\s*[A-Za-z_]\w*\s*>|\(\s*(?:int|float|double|char|bool|long|short|unsigned|signed)\s*\)\s*[a-zA-Z_]"
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(
                r"\b(throw|abort|exit|_Exit|quick_exit|std::terminate|longjmp)\b"
            ),
            # 42. halt_hits (Temporal Duct Tape)
            # Admission of race conditions or lazy polling.
            "halt_hits": re.compile(
                r"\b(sleep|delay|usleep|nanosleep|std::this_thread::sleep_for)\b"
            ),
            # 43. bitwise_hits (The Sub-Atomic Math)
            # Low-level byte manipulation. CRITICAL: Removed bare `<<` and `>>` to prevent catastrophic false positives on `std::cout` and `std::cin` streams. Explicit bitwise assignments (`<<=`, `&=`) are retained as they are unambiguous.
            "bitwise_hits": re.compile(r"\^|(?<![=!])~|<<=|>>=|&=|\|=|\^="),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(mutex|lock|synchronized|Semaphore|std::lock_guard|std::scoped_lock|std::unique_lock|mtx_lock)\b",
                re.I,
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(
                r"\b(const|constexpr|consteval|constinit|final|readonly|Immutable)\b"
            ),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r"\b(delete|free|close|fclose|dispose|shutdown|std::destroy|reset)\b\s*\("
            ),
            # 47. encapsulation (The Vault)
            "encapsulation": re.compile(r"\b(private:|protected:|internal:)\b"),
            # 48. listeners (The Sinks)
            "listeners": re.compile(
                r"\b(on|addEventListener|subscribe|connect|handler|callback)\b"
            ),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(
                r"\b(GTEST_SKIP|test\.skip|it\.skip|mock\(|fake\()\b"
            ),
        },
    },
    "c": {
        "_meta": {
            "target_version": "C23 (ISO/IEC 9899:2024 - constexpr, #embed, [[attributes]], nullptr, typeof)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard sources, headers, OpenCL kernels, Yacc grammars, and C-like scripting/ATS language files.
        # THE FIX: Added .dts and .dtsi (Device Tree Source) to parse hardware maps.
        "extensions": [".c", ".h", ".cl", ".inc", ".y", ".idc", ".cats", ".dts", ".dtsi"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Extensionless build/config scripts and tooling configs that are secretly pure code.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, package manifests, and lockfiles to resolve ambiguous files (like .h or .inc).
        "discriminators": [
            ".c",
            "Makefile",
            "configure.ac",
            "configure.in",
            "configure",
            "CMakeLists.txt",
            "Kconfig",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1.
        "shebangs": ["tcc", "picoc", "cscript"],
        # UPGRADED: Maps to Family 1 (Standard C)
        # Rationale: Uses '//' for line-level literature; multi-line literature
        # (/* */) is handled by the Section 2.3.C.3 Heuristic Pass.
        "lexical_family": "std_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Modern C (C99+) uses '//' for standard line-level Ghost Mass.
            "_line_anchor": re.compile(r"//"),
            # Inline comments follow the standard '//' delimiter.
            "_inline_comment": re.compile(r"//"),
            # Block comment start: /* (The primary literature delimiter for all C eras).
            "_block_start": re.compile(r"/\*"),
            # Block comment end: */
            "_block_end": re.compile(r"\*/"),
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Decisions and jumps. EXCLUDES exit/abort (bailout_hits).
            "branch": re.compile(
                r"\b(if|else|switch|case|default|for|while|do|break|continue|goto)\b|&&|\|\||\?"
            ),
            # 2. args (The Coupling Mass)
            # Parameter blocks. Bounded negation [^)]* to prevent ReDoS on massive param lists.
            "args": re.compile(
                r"(?!(?:if|for|while|switch|return)\b)\b[a-zA-Z_]\w*[ \t*]*\(\s*(?:const\s+|volatile\s+)?(?:int|char|void|float|double|long|short|unsigned|signed|struct|enum)\b[^)]*\)",
                re.M,
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: Access modifiers (encapsulation) and const (freeze_hits).
            "linear": re.compile(
                r"\b(struct|union|enum|typedef|return|void|restrict|auto|bool|true|false|_BitInt|alignas|alignof)\b"
            ),
            "func_start": re.compile(
                # =====================================================================
                # [LLM CONTEXT: C-FUNCTION AST EXTRACTOR & REDOS SHIELD]
                # PURPOSE: Anchors executable logic blocks (functions) in C.
                # VULNERABILITY: C allows multi-line function signatures. In files with 
                #   massive macro lists (e.g., 20k lines of `#define`), the `[ \t\n]+` 
                #   allowances caused catastrophic backtracking (ReDoS).
                # THE "IRON WALL" FIX 1 (Lookaheads): `(?![ \t]*#)` is a negative lookahead injected at 
                #   high-risk multi-line boundaries. It explicitly forbids the regex engine 
                #   from crossing into preprocessor directives, capping the permutation tree.
                # THE "IRON WALL" FIX 2 (Strict Bounding): Unbounded wildcards (`*` or `+`) 
                #   are STRICTLY FORBIDDEN inside the K&R parameter gap. They must use 
                #   numeric bounds (e.g., `{0,100}`) to starve ReDoS traps on massive files.
                # =====================================================================
                
                # 1. THE HORIZONTAL ANCHOR (Stops O(N^2) vertical spirals)
                r"^[ \t]*"
                
                # 2. LINKAGE & STORAGE MODIFIERS (Supports vertical formatting)
                r"(?:(?:static|inline|extern|_Noreturn|__inline__|__forceinline|constexpr)[ \t\n]+){0,5}"
                
                # 3. COMPILER ATTRIBUTES PRE-TYPE (Includes C23 [[...]] and GNU __attribute__)
                r"(?:(?:__attribute__[ \t]*\([^)]*\)|\[\[[^\]]*\]\]|__declspec[ \t]*\([^)]*\))[ \t\n]*){0,5}"
                
                # 4. THE RETURN TYPE (Pointers/references explicitly bound)
                # [IRON WALL]: Prevents the engine from reading a `#define` on the next line as a return type.
                r"(?:(?:struct|union|enum)[ \t\n]+)?"
                r"(?:(?![ \t]*#)[a-zA-Z_]\w*(?:[ \t\n]+[*&]*[ \t\n]*|[*&]+[ \t\n]*)){0,5}"
                
                # 5. THE "NOT A FUNCTION" SHIELD
                # Prevents control flow (if, while) and primitive types from being captured as function names.
                r"(?!(?:if|for|while|switch|return|sizeof|int|float|double|char|void|long|short|unsigned|signed|bool|__attribute__|__declspec|__asm__)\b)"
                
                # 6. THE IDENTIFIER CAPTURE (SATELLITE NAME - GROUP 1)
                # [IRON WALL]: Ensures the actual function name isn't hijacked by a macro definition.
                r"(?![ \t]*#)([a-zA-Z_]\w*)"
                
                # 7. THE PARAMETER BLOCK (Supports vertical gap)
                r"[ \t\n]*(?:ARGS\d+\s*\([^)]*\)|\([^)]*\)|NOARGS)"
                
                # 8. POST-PARAMETER MODIFIERS (GCC attributes safely handled)
                r"(?:[ \t\n]+(?:__attribute__\s*\([^)]*\)|\[\[[^\]]*\]\])){0,5}"
                
                # 9. THE K&R C PARAMETER GAP (Crucial for legacy codebases like DOOM/FreeBSD)
                # Legacy C allows type declarations between the closing ')' and opening '{'.
                # [IRON WALL - CATASTROPHIC BACKTRACKING FIX]: 
                # Previously used unbounded wildcards (`[^(){};]*`). On massive macro arrays,
                # this caused millions of permutations and 60+ second timeouts.
                # We enforce strict numeric bounds (`{0,100}`) to instantly cap the permutation tree.
                r"(?:(?:[ \t\n]+(?![ \t]*#)[a-zA-Z_][^(){};]{0,100};){1,20})?"
                
                # 10. THE IGNITION (The opening brace confirming it is a definition, not a declaration)
                r"[ \t\n]*\{",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            # C uses structs/unions/enums as the primary entity entities.
            "class_start": re.compile(
                r"^[ \t]*(?:typedef[ \t]+)?(?:struct|union|enum)\s+[a-zA-Z_]\w*", re.M
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\b(assert|static_assert|_Static_assert|size_t|snprintf|strncat|strncpy|calloc|nullptr|unreachable|ckd_add|ckd_sub|ckd_mul)\b"
            ),
            # 7. safety_neg (The Fractures)
            # Dangerous legacy functions and raw void manipulation.
            "safety_neg": re.compile(
                r"\b(strcpy|strcat|sprintf|gets|alloca)\b|\([a-zA-Z_]\w*\s*\*\)\s*[a-zA-Z_]\w*"
            ),
            # 8. danger (The Heavy Load)
            # Process killers and context switches. EXCLUDES prints (Phase 5).
            "danger": re.compile(r"\b(system|popen|execl|execv|fork|longjmp|setjmp)\b"),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(fopen|fclose|fread|fwrite|fscanf|sscanf|socket|recv|send|open|read|write|close|stat|fseek|remove|rename)\b"
            ),
            # 10. api (The Event Horizon)
            # Physical Reality: C functions are public by default.
            "api": re.compile(r'\b(extern|__declspec\(dllexport\)|__attribute__\(\(visibility\("default"\)\)\))\b|^[ \t]*(?!static\b)[a-zA-Z_]\w*[ \t*]+[a-zA-Z_]\w*(?:\[[^\]]*\])?\s*=?|^[ \t]*[a-zA-Z_]\w*[ \t*]+[a-zA-Z_]\w*\s*\([^)]*\)\s*;', re.M),
                        
            # 11. flux (The Boiling Plasma)
            # Mutation of state. EXCLUDES const/constexpr (freeze_hits).
            "flux": re.compile(
                r"(?<![=!<>])=(?![=])|\*(?!\s*const)\w+[ \t]*=|(?:\+\+|--)"
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(r"(?://|/\*)[ \t]*(?:if|for|while|struct|union|enum|void|int|return)\b"),
            
            # 13. doc (The Intent)
            "doc": re.compile(
                r"///|/\*\*|@param|@return|@brief|@details|\\param|\\return|\\brief|\\details"
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r"\b(?:TEST|TEST_F|TEST_CASE|CU_ASSERT|RUN_TEST|EXPECT_[A-Z_]+|ASSERT_[A-Z_]+)\b|\bassert\s*\("
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Complexity) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(thrd_create|thrd_join|mtx_lock|pthread_create|pthread_mutex_lock|atomic_int|_Atomic|memory_order_[a-z]+|thread_local)\b"
            ),
            # 16. ui_framework (The View Layer)
            "ui_framework": re.compile(
                r"\b(GtkWidget|CreateWindow|MessageBox|XOpenDisplay|gtk_window_new|Fl_Window|initscr|wprintw)\b"
            ),
            # 17. closures
            "closures": None,  # Strict C23 lacks native closures (blocks are non-standard).
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"^[ \t]*(?:static\s+|extern[ \t]+)?[a-zA-Z_]\w*[ \t*]+[a-zA-Z_]\w*(?:\[[^\]]*\])?\s*=(?![ \t]*==)",
                re.M,
            ),
            # 19. decorators (The Metadata Hooks)
            "decorators": re.compile(r"\[\[\s*[a-zA-Z_:][^\]]*\s*\]\]"),
            # 20. generics (The Type Abstractions)
            "generics": re.compile(r"\b_Generic\s*\([^)]*\)"),
            # 21. comprehensions
            "comprehensions": None,
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(math\.h|tgmath\.h|complex\.h|cblas_|dgemm|sin|cos|tan|exp|log|sqrt|complex|I|_Float\d+|__m\d+)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Macros with args and unstructured jumps.
            "heat_triggers": re.compile(
                r"^#\s*define\s+[a-zA-Z_]\w*\([^)]*\)|\bgoto\b", re.M
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(r'^[ \t]*#[ \t]*(?:include|embed)\s*[<"][^>"]+[>"]', re.M),
                        
            "_dependency_capture": re.compile(r'^[ \t]*#[ \t]*(?:include|embed)\s*[<"]([^>"]+)[>"]', re.M),
                                    
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"(?:@author|\\author|Author:|Created by:|Copyright)\s+(.*)", re.I
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": re.compile(
                r"\b(FCGI_Accept|khttp_parse|MHD_start_daemon|facil\.io)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(epoll_wait|epoll_ctl|kqueue|kevent|select|poll|libev|libuv)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\b(plugin_register|vtable|struct\s+[a-zA-Z_]\w*_ops)\b"
            ),
            # 34. macros (The Preprocessor Hooks)
            "macros": re.compile(r"^[ \t]*#[ \t]*(?:define|undef|if|elif|else|endif|pragma|warning|error)\b", re.M),
            # 35. pointers (The Memory Map)
            "pointers": re.compile(
                r"->|\b(?:uintptr_t|intptr_t|ptrdiff_t|size_t)\b|(?<=[=\s,(])&\w+|(?<=[=\s,(])\*(?:\s*const\s*)?\w+"
            ),
            # 36. memory_alloc (Manual Memory Management)
            "memory_alloc": re.compile(
                r"\b(malloc|calloc|realloc|free|aligned_alloc|mmap|alloca)\b"
            ),
            # 37. inline_asm (The Bare Metal)
            "inline_asm": re.compile(
                r"\b(?:__asm__|asm|__asm)\b(?:\s+(?:volatile|__volatile__))?\s*\(|\b(?:__asm__|asm|__asm)\b[ \t]*\{"
            ),
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(?:syslog|openlog|log_info|log_error|log_warn|log_debug|vsyslog)\b"
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(
                r"\b(printf|fprintf|vprintf|puts|putchar|perror)\b"
            ),
            # 40. cast_hits (The "Trust Me" Tax)
            "cast_hits": re.compile(
                r"\(\s*(?:int|float|double|char|bool|long|short|unsigned|signed|void)(?:\s*\*){0,5}\s*\)\s*[a-zA-Z_]"
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(
                r"\b(abort|exit|_Exit|quick_exit|return\s+-1)\b"
            ),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\b(sleep|usleep|nanosleep|thrd_sleep)\b"),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(r"<<|>>|\^|(?<![=!])~|<<=|>>=|&=|\|=|\^="),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(mtx_lock|mtx_unlock|pthread_mutex_lock|atomic_flag_test_and_set|atomic_store)\b"
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(r"\b(const|constexpr|alignas|restrict)\b"),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r"\b(free|fclose|close|munmap|destroy|shutdown)\b\s*\("
            ),
            # 47. encapsulation (The Vault)
            # Physical Reality: Static functions/variables are internal/private to the translation unit.
            "encapsulation": re.compile(r"^[ \t]*static\b", re.M),
            # 48. listeners (The Sinks)
            "listeners": re.compile(
                r"\b(on_event|handler|callback|signal\(|sigaction\()"
            ),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(r"\b(IGNORE_TEST|test\.skip|mock\(|fake\()\b"),
        },
    },
    "php": {
        "_meta": {
            "target_version": "PHP 8.5.x / Modern Laravel 11+, Symfony 7+, & PSR-12 Paradigms",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Merged standard suffixes, legacy formats, UI templates (.phtml, .ctp), and CMS "dark matter" (.module, .inc).
        "extensions": [
            ".php",
            ".phtml",
            ".php3",
            ".php4",
            ".php5",
            ".php7",
            ".php8",
            ".phps",
            ".ctp",
            ".module",
            ".inc",
            ".theme",
            ".install",
            ".profile",
            ".engine",
            ".aw",
        ],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Extensionless framework CLI entry points that are secretly pure PHP code.
        "exact_matches": ["artisan", "composer.phar", "drush", "wp-cli", "phpunit"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, package manifests, and lockfiles to resolve ambiguous files (like .inc).
        "discriminators": [
            ".php",
            "composer.json",
            "composer.lock",
            "phpunit.xml",
            "phpunit.xml.dist",
            "phpcs.xml",
            ".php_cs",
            ".php_cs.dist",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1.
        "shebangs": ["php", "php-cli", "php-cgi", "hhvm"],
        # UPGRADED: Maps to Family 6 (Polyglot)
        # Rationale: PHP fundamentally operates within an HTML context, requiring the parser
        # to explicitly hunt for <?php execution boundaries. It also supports multiple
        # comment styles (//, #, and /* */).
        "lexical_family": "polyglot",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # PHP supports both '//' and '#' for line-level Ghost Mass.
            "_line_anchor": re.compile(r"//|#"),
            # Inline comments follow the same dual-token logic.
            "_inline_comment": re.compile(r"//|#"),
            # Block comment start: /* '_block_start': re.compile(r'/\*'),
            # Block comment end: */
            "_block_end": re.compile(r"\*/"),
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Control flow. Includes modern match expression. EXCLUDES throw (bailout_hits).
            "branch": re.compile(
                r"\b(if|else|elseif|switch|case|default|foreach|for|while|do|try|catch|finally|break|continue|match|goto)\b|&&|\|\||\?\?|\?"
            ),
            # 2. args (The Coupling Mass)
            # Signatures for functions and arrow functions. Bounded to prevent ReDoS.
            "args": re.compile(
                r"\b(?:function|fn)\s*(?:&\s*)?[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*\s*\([^)]*\)|\bfunction\s*\([^)]*\)|fn\s*\([^)]*\)[ \t]*=>",
                re.M,
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: Access modifiers (encapsulation) and const/readonly (freeze_hits).
            "linear": re.compile(
                r"\b(namespace|use|class|interface|trait|enum|function|return|yield|declare|require|require_once|include|include_once|as|implements|extends|clone|new)\b"
            ),
            "func_start": re.compile(
                r"(?:^|[^a-zA-Z0-9_])(?:#\[[^\]]*\][ \t]*){0,5}"
                r"(?:(?:public(?:\s*\(\s*set\s*\))?|protected(?:\s*\(\s*set\s*\))?|private(?:\s*\(\s*set\s*\))?|static|final|abstract|readonly)[ \t]+){0,5}"
                r"function\s+(?:&\s*)?([a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*)(?=\s*\()",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            "class_start": re.compile(
                r"^[ \t]*(?:#\[[^\]]*\][ \t]*){0,5}(?:(?:abstract|final|readonly)[ \t]+){0,3}(?:class|interface|trait|enum)\s+[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\b(try|catch|finally|declare\s*\(\s*strict_types[ \t]*=\s*1\s*\)|readonly|Throwable|Exception|assert|isset|empty|is_null|instanceof)\b|\?\?|\?->|#\[Override\]"
            ),
            # 7. safety_neg (The Fractures)
            # Error suppression, dangerous eval, and loose equality.
            "safety_neg": re.compile(
                r"@(?:[a-zA-Z_\x80-\xff])|\b(unserialize|extract|parse_str|phpinfo)\b|error_reporting\s*\(\s*0\s*\)|==(?!=)|!=(?!=)"
            ),
            # 8. danger (The Heavy Load)
            # Shell execution and process killers. EXCLUDES prints (Phase 5).
            "danger": re.compile(
                r"\b(exec|shell_exec|system|passthru|proc_open|popen)\b|`[^`]+`"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(fopen|fread|fwrite|file_get_contents|file_put_contents|PDO|mysqli|curl_exec|socket|header|setcookie)\b|\$_(?:GET|POST|FILES|REQUEST|COOKIE)"
            ),
            # 10. api (The Event Horizon)
            # Exposed surface. Explicit public markers + attribute routes.
            "api": re.compile(
                r"\b(public)\b|#\[(?:ApiResource|Route|Get|Post|Put|Delete|Patch)[^\]]*\]"
            ),
            # 11. flux (The Boiling Plasma)
            # Mutation of state. Variable reassignments and array mutators.
            "flux": re.compile(
                r"\$[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*\s*(?:[-+*./%&|])?=|&\$|\bglobal\s+\$|(?:\w+)?(?:->|::)[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*[ \t]*=|array_(?:push|pop|shift|unshift|splice)\b|(?:\+\+|--)"
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"//\s*[;{}]|/\*\s*(?:function|class|namespace|use|if|foreach)\s|#\s*\$|//\s*(?:echo|print|\$|return|var_dump)"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r"/\*\*|@param|@return|@throws|@var|@deprecated|@property|@method"
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r"\b(PHPUnit|TestCase|assertSame|assertEquals|assertTrue|assertFalse|mock|spy|expects|toBe|test|it)\b|#\[Test\]"
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Complexity) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(Fiber|yield|Swoole|React\\|Amp\\|Coroutine|go\(|await|suspend|resume|pcntl_fork)\b"
            ),
            # 16. ui_framework (The View Layer)
            "ui_framework": re.compile(
                r'\b(view\s*\(|render\s*\(|renderView|extends\s+Controller|Blade::|Twig\\Environment)\b|@(?:if|foreach|yield|section|extends)\b|<\?=|echo\s+[\'"]<|\{\{[^}]*\}\}|\{%\s*[^%]*\s*%\}'
            ),
            # 17. closures (The Functional Depth)
            "closures": re.compile(
                r"\b(?:function\s*\([^)]*\)\s*(?:use\s*\([^)]*\)\s*)?\{|fn\s*\([^)]*\)[ \t]*=>)"
            ),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\b(\$_SERVER|\$_SESSION|\$_ENV|\$GLOBALS)\b|\bglobal\s+\$"
            ),
            # 19. decorators (The Metadata Hooks)
            "decorators": re.compile(r"#\[\s*[a-zA-Z0-9_:\\]+[^\]]*\]", re.M),
            # 20. generics (The Type Abstractions)
            # Simulated/Docblock generics.
            "generics": re.compile(
                r"@(?:template|implements|extends|use)\s+[a-zA-Z0-9_\\]+(?:<[^>]*>)?|\b(?:array|iterable|Collection)<[^>]*>"
            ),
            # 21. comprehensions (The High-Density Loops)
            "comprehensions": re.compile(
                r"\b(array_map|array_filter|array_reduce|array_walk|array_column|array_find|array_any|array_all)\b"
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(bcadd|bcsub|bcmul|bcdiv|gmp_add|gmp_mul|abs|cos|sin|tan|sqrt|log|exp|pow)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Magic methods, reflection, and variable variables.
            "heat_triggers": re.compile(
                r"\b(__(?:get|set|call|callStatic|invoke|destruct|clone)|Reflection(?:Class|Method|Property)|call_user_func(?:_array)?)\b|\$\$[a-zA-Z_\x80-\xff]"
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(
                r"^[ \t]*(?:use\s+(?:function|const[ \t]+)?[\w\\]+|require|include|require_once|include_once)\b",
                re.M,
            ),
            
            "_dependency_capture": re.compile(r"^[ \t]*use\s+(?:function\s+|const\s+)?([\w\\]+)|\b(?:require|require_once|include|include_once)\s*\(?\s*['\"]([^'\"]+)['\"]", re.M),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"@(?:author|copyright)\s+(.*)|(?:Created by|Maintainer):?\s+(.*)", re.I
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": re.compile(
                r"\b(Response|JsonResponse|HtmlResponse|RedirectResponse|Symfony\\Component\\HttpFoundation|Illuminate\\Http\\Response)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(EventDispatcher|dispatchEvent|Listener|dispatch|broadcast|notify|Event::|listen)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\b(ContainerInterface|Container|getContainer|inject|bind|singleton|app\(|make\()\b|#\[(?:Inject|Autowire)[^\]]*\]"
            ),
            # 34. macros (The Preprocessor Hooks)
            "macros": re.compile(r"\b(?:Macroable|macro\s*\(|mixin\s*\()\b"),
            # 35. pointers (The Memory Map)
            "pointers": re.compile(r"\b(FFI::cast|FFI::addr|FFI::scope|FFI::new)\b"),
            # 36. memory_alloc (The Yin to cleanup)
            "memory_alloc": re.compile(
                r"\bnew\s+[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*"
            ),
            # 37. inline_asm
            "inline_asm": None,
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(?:Log::|LoggerInterface|logger\(|Monolog\\|error_log|Psr\\Log)\b.*?(?:info|error|warning|debug|trace|notice|critical|alert|emergency)\b",
                re.I,
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(
                r"\b(echo|print|var_dump|print_r|printf|vprintf|var_export|die|exit|dd|dump)\b"
            ),
            # 40. cast_hits (The "Trust Me" Tax)
            "cast_hits": re.compile(
                r"\((?:int|integer|bool|boolean|float|double|string|array|object|unset)\)\s*|\bsettype\s*\("
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(throw|die|exit|abort)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(
                r"\b(sleep|usleep|time_nanosleep|time_sleep_until)\b"
            ),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(r"<<|>>|(?<!&)&(?!&)|(?<!\|)\|(?!\|)|\^|~"),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(mutex|lock|synchronized|Semaphore|flock|sem_acquire)\b", re.I
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(r"\b(const|readonly|final)\b"),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r"\b(unset|fclose|mysql_close|mysqli_close|PDO::null|dispose|cleanup)\b\s*\("
            ),
            # 47. encapsulation (The Vault)
            "encapsulation": re.compile(r"\b(private|protected|internal)\b"),
            # 48. listeners (The Sinks)
            "listeners": re.compile(
                r"\.on\(|addEventListener|subscribe|@KafkaListener|@RabbitListener"
            ),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(
                r"\b(markTestSkipped|test\.skip|it\.skip|mock\(|fake\()\b"
            ),
        },
    },
    "powershell": {
        "_meta": {
            "target_version": "PowerShell 7.5.4 (Core / Cross-Platform / PSClasses)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard scripts (.ps1), modules (.psm1), data files evaluated as AST (.psd1), and type formatting files.
        "extensions": [".ps1", ".psm1", ".psd1", ".ps1xml", ".psc1", ".pssc", ".cdxml"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: PowerShell rarely uses extensionless execution scripts; its conventions demand extensions.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions and analyzer settings to lock in context.
        "discriminators": [
            ".ps1",
            ".psm1",
            "PSScriptAnalyzerSettings.psd1",
            "psake.ps1",
        ],
        # EXECUTION SIGNATURES: Modern cross-platform and legacy Windows interpreters found on Line 1.
        "shebangs": ["pwsh", "powershell"],
        # UPGRADED: Maps to Family 4 (Hybrid Hash)
        # Rationale: PowerShell uses '#' for single-line comments but relies on
        # a unique '<# #>' syntax for multi-line block comments, requiring hybrid parsing logic.
        "lexical_family": "hybrid_hash",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # PowerShell uses '#' for standard line-level literature.
            "_line_anchor": re.compile(r"#"),
            # Inline comments are also triggered by the '#' token.
            "_inline_comment": re.compile(r"#"),
            # Block comment start: <#
            "_block_start": re.compile(r"<#"),
            # Block comment end: #>
            "_block_end": re.compile(r"#>"),
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # branch: decisions that split flow. Includes ternary operators (?) and null-coalescing (??).
            "branch": re.compile(
                r"\b(if|else|elseif|switch|for|foreach|while|do|until|try|catch|finally|throw|trap|break|continue|return)\b|-and|-or|-not|-xor|\?|\?\?",
                re.I,
            ),
            # args: Coupling Mass. Captures the param block mass of functions and script files.
            "args": re.compile(
                r"\bparam\s*\([^)]*\)|\bfunction\s+[a-zA-Z0-9_-]+\s*\([^)]*\)", re.I
            ),
            # linear: Smooth Path. Structural boundaries defining scope (process, begin, end).
            # EXCLUDES access modifiers (hidden, static) to prevent Geometry Inflation.
            "linear": re.compile(
                r"\b(function|filter|workflow|configuration|class|enum|process|begin|end|clean|return|exit|using|namespace)\b",
                re.I,
            ),
            # func_start: Satellite Spawner. Anchors executable logic blocks.
            # EXCLUDES class/enum to fix Ghost Satellites.
            "func_start": re.compile(
                r"^[ \t]*(?:function|filter|workflow)\s+([a-zA-Z0-9_-]+)|^[ \t]*\[[^\]]+\]\s+([a-zA-Z_]\w*)(?=\s*\()",
                re.I | re.M,
            ),
            # class_start: Entity Census. Defines OO boundaries (Classes and Enums).
            "class_start": re.compile(
                r"^[ \t]*(?:class|enum)\s+[a-zA-Z_]\w*", re.I | re.M
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # safety: Cyan Fortification. Strict mode, validation attributes, and null-conditional access (?.).
            "safety": re.compile(
                r"\b(try|catch|finally|trap|Set-StrictMode|ValidateNotNull|ValidateSet|ValidateRange|ValidatePattern)\b|-ErrorAction\s+Stop|\$\?|\?\.",
                re.I,
            ),
            # safety_neg: Fractures. Actively bypassing errors or type checks (Out-Null, SilentlyContinue).
            "safety_neg": re.compile(
                r"-ErrorAction\s+SilentlyContinue|-WarningAction\s+SilentlyContinue|Out-Null|\[void\]|ExecutionPolicy\s+Bypass|\bIgnore\b",
                re.I,
            ),
            # danger: Heavy Load. Dynamic code execution and process terminators.
            "danger": re.compile(
                r"\b(Invoke-Expression|iex|Stop-Process|kill|Exit)\b", re.I
            ),
            # io: Boundaries. Disk, Network, and URL fetching (Includes CERN/TBL legacy emulation triggers).
            "io": re.compile(
                r"\b(Get-Content|Set-Content|Out-File|Invoke-WebRequest|iwr|Invoke-RestMethod|irm|TcpClient|HttpListener|HTLoad|HTGet|ENQUIRE)\b",
                re.I,
            ),
            # api: Event Horizon. Exposed surface area (Module exports and non-hidden functions).
            "api": re.compile(
                r"\b(Export-ModuleMember|New-Alias|CmdletBinding)\b|^[ \t]*(?!hidden\s+)[a-zA-Z_]\w*\s*\(",
                re.I | re.M,
            ),
            # 11. flux (The Boiling Plasma)
            # Mutation of state. Captures assignments, scoped variables, array indexing, and anchored increments.
            "flux": re.compile(
                # PATH A: EXPLICIT CMDLET MUTATION
                r"\bSet-Variable\b|"
                # PATH B: STANDARD ASSIGNMENT (Variables, Scopes, Properties, and Arrays)
                # Safely captures $var, $global:var, $env:PATH
                r"\$(?:[a-zA-Z]+:)?[a-zA-Z_]\w*"
                # The Chain: Safely captures .Property OR ['Index'], clamped to {0,4} to prevent runaway depth
                r"(?:\.[a-zA-Z_]\w*|\[[^\]\n]+\]){0,4}"
                # The Operator: Uses [ \t]* instead of \s* to prevent O(N^2) vertical newline bleeding
                r"[ \t]*(?:\+|-|\*|/|%)?=|"
                # PATH C: PRE-INCREMENT / PRE-DECREMENT
                # Anchored to a variable to prevent matching "C++" in strings
                r"(?:\+\+|--)[ \t]*\$(?:[a-zA-Z]+:)?[a-zA-Z_]\w*|"
                # PATH D: POST-INCREMENT / POST-DECREMENT
                # Includes property/array chaining before the increment (e.g. $arr[0]++)
                r"\$(?:[a-zA-Z]+:)?[a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*|\[[^\]\n]+\]){0,4}[ \t]*(?:\+\+|--)",
                re.I,
            ),
            # 12. graveyard (The Necrosis)
            # Commented-out execution logic indicating dead features. Supports both `//` and `#` style comments.
            "graveyard": re.compile(
                r"(?:#|<#)[ \t]*(?:function|class|if|foreach|while|return)\b", re.I
            ),
            # doc: Intent. Get-Help comment-based documentation.
            "doc": re.compile(
                r"\.(?:SYNOPSIS|DESCRIPTION|PARAMETER|EXAMPLE|NOTES|LINK|INPUTS|OUTPUTS|ROLE)\b",
                re.I,
            ),
            # 14. test (The Verification)
            # Triggers indicating internal verification. MUST strictly anchor 'it', 'test', and 'toBe' with opening parentheses to prevent triggering on prose inside Pest/PHPUnit tests.
            "test": re.compile(
                r'\b(?:Mock|Assert-MockCalled|BeforeAll|AfterAll|BeforeEach|AfterEach|Should)\b|\b(?:Describe|Context|It)\s+[\'"]',
                re.I,
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # concurrency: Temporal Static. Jobs, Runspaces, and PS7 Parallel pipelines.
            "concurrency": re.compile(
                r"\b(Start-Job|Wait-Job|Receive-Job|Start-ThreadJob|-Parallel|RunspaceFactory|PowerShell\.Create)\b",
                re.I,
            ),
            # ui_framework: View Layer. WinForms/WPF bridges (Includes TBL WWW rendering emulation triggers).
            "ui_framework": re.compile(
                r"\[System\.Windows\.(?:Forms|Controls|Markup)\]|New-Object\s+System\.Windows\.|Out-GridView|HtmlDocument|WebBrowser|SGML|WorldWideWeb",
                re.I,
            ),
            # closures: Functional Depth. ScriptBlocks (The foundation of PS closures).
            "closures": re.compile(r"\{\s*(?:param\s*\([^)]*\))?[^}]*\}", re.I),
            # globals: Shared Void. Environment and global/script scope variables.
            "globals": re.compile(
                r"\$(?:global|env|script):[a-zA-Z_]\w*|\b(?:ErrorActionPreference|WarningPreference|ConfirmPreference)\b",
                re.I,
            ),
            # decorators: Metadata Hooks. Cmdlet and Parameter attributes.
            "decorators": re.compile(
                r"\[(?:CmdletBinding|Parameter|Alias|OutputType|AllowNull|AllowEmptyString)\s*\([^)]*\)\]",
                re.I,
            ),
            # generics: Type Abstractions. .NET generic type invocations.
            "generics": re.compile(r"\[[a-zA-Z_.]+(?:`\d+)?\[[^\]]*\]\]", re.I),
            # comprehensions: High-Density Loops. Pipeline filtering and projection.
            "comprehensions": re.compile(
                r"\|\s*(?:Where-Object|\?|Select-Object|select|ForEach-Object|%)[ \t]*\{",
                re.I,
            ),
            # scientific: Compute Core. .NET Math primitives.
            "scientific": re.compile(
                r"\[Math\]::(?:Abs|Acos|Asin|Atan|Ceiling|Cos|Exp|Floor|Log|Max|Min|Pow|Round|Sin|Sqrt|Tan|PI)\b",
                re.I,
            ),
            # heat_triggers: Thermal Radiation. Reflection and on-the-fly C# compilation via Add-Type.
            "heat_triggers": re.compile(
                r"\b(Add-Type|System\.Reflection|System\.Management\.Automation\.Language|Invoke-Expression|iex)\b|&\s*\$[a-zA-Z_]\w*",
                re.I,
            ),
            # import: Gravity Links. Module and assembly loading.
            "import": re.compile(
                r"\b(Import-Module|using\s+module|using\s+namespace|using\s+assembly|\.\s+[\w.\/\\]+\.ps1)\b",
                re.I,
            ),
            
            # --- UPDATED LINE FOR THE ORCHESTRATOR ---
            "_dependency_capture": re.compile(r"\b(?:Import-Module|using\s+(?:module|namespace|assembly))\s+['\"]?([^'\"\s;]+)['\"]?|(?:^|[ \t])\.\s+['\"]?([^'\"\s;]+\.ps1)['\"]?", re.I | re.M),
                        
            # ownership: Authorship indicators in comments or metadata.
            "ownership": re.compile(
                r"^[ \t]*#\s*(?:Author|Created by|Maintainer|Copyright):\s+([^\n]+)|\.AUTHOR\s+([^\n]+)",
                re.I | re.M,
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            "spec_exposure": re.compile(r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)\]", re.I),
            # 30. civil_war (The Indentation Tracker)
            # Structural formatting violating norms. Handled natively by the GitGalaxy Signal Processor.
            "civil_war": None,
            "ssr_boundaries": re.compile(
                r"\b(New-PodeServer|Add-PodeRoute|Write-PodeHtmlResponse|New-UDEndpoint|New-UDPage)\b",
                re.I,
            ),
            "events": re.compile(
                r"\b(Register-ObjectEvent|Register-EngineEvent|Register-WmiEvent|Unregister-Event|Wait-Event)\b",
                re.I,
            ),
            "dependency_injection": re.compile(
                r"\b(InversionOfControl|DependencyInjection|Register-Service|Get-Service|Resolve-Dependency)\b",
                re.I,
            ),
            "macros": None,  # PowerShell lacks a preprocessor
            # 35. pointers (The Memory Map)
            # PHP natively lacks pointers, but FFI (Foreign Function Interface) memory bounds are safely captured.
            "pointers": re.compile(
                r"\[(?:IntPtr|UIntPtr)\]|\[ref\]\s*\$[a-zA-Z_]\w*", re.I
            ),
            "memory_alloc": re.compile(
                r"\[System\.Runtime\.InteropServices\.Marshal\]::(?:AllocHGlobal|AllocCoTaskMem)",
                re.I,
            ),
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # telemetry: Professional observers. Structured pipeline logging.
            "telemetry": re.compile(
                r"\b(Write-Verbose|Write-Debug|Write-Information|Write-Warning|Start-Transcript|Write-Log)\b",
                re.I,
            ),
            # print_hits: Amateur space debris. Raw terminal pollution.
            "print_hits": re.compile(r"\b(Write-Host|echo)\b", re.I),
            # 40. cast_hits (The Trust Me Tax)
            # Forceful type coercion. PHP has a strict, built-in casting syntax which prevents false positives naturally.
            "cast_hits": re.compile(
                r"\[(?:int|long|string|char|byte|bool|double|float|decimal|array|hashtable)\]\s*[\$\(]",
                re.I,
            ),
            # bailout_hits: Detonators. Aborting execution context.
            "bailout_hits": re.compile(r"\b(throw|Exit)\b|-ErrorAction\s+Stop", re.I),
            # halt_hits: Temporal Duct Tape. Forcing threads to sleep.
            "halt_hits": re.compile(r"\b(Start-Sleep|sleep)\b", re.I),
            # 43. bitwise_hits (The Sub-Atomic Math)
            # Low-level byte manipulation. CRITICAL: Removed the pipe '|' (PHP 8 Union Types), ampersand '&' (Pass-by-reference `&$var`), and used lookarounds for `<<` to prevent triggering on Heredocs (`<<<EOF`).
            "bitwise_hits": re.compile(r"-(?:band|bor|bxor|bnot|shl|shr)\b", re.I),
            # sync_locks: Barricades. Coordinated threading logic.
            "sync_locks": re.compile(
                r"\b(lock|Monitor|Mutex|Semaphore|atomic|WaitOne)\b", re.I
            ),
            # freeze_hits: Data Cryogenics. Immutability via Constant variables.
            "freeze_hits": re.compile(
                r"New-Variable\s+[^;]*?-Option\s+Constant|readonly", re.I
            ),
            # cleanup: The Janitor. Resource release.
            "cleanup": re.compile(
                r"\b(dispose|Remove-Variable|Remove-Item|Remove-Module|Stop-Transcript)\b",
                re.I,
            ),
            # encapsulation: The Vault. Hiding logic from the application.
            "encapsulation": re.compile(r"\b(hidden|private)\b", re.I),
            # listeners: The Sinks. Waiting for external state broadcasts.
            "listeners": re.compile(r"\b(Register-ObjectEvent|on_|Connect-)\b", re.I),
            # test_skip: Safety Theater.
            "test_skip": re.compile(r"\b(pending|skip|Ignore)\b", re.I),
        },
    },
    "shell": {
        "_meta": {
            "target_version": "Bash 5.2 / Zsh 5.9 / Modern DevOps Scripts",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        "extensions": [
            ".sh",
            ".bash",
            ".zsh",
            ".ksh",
            ".dash",
            ".command",
            ".csh",
            ".tcsh",
            ".fish",
            ".bats",
        ],
        # Thorough Exact Match List: Captures hidden configuration and profile scripts.
        "exact_matches": [
            ".bashrc",
            ".zshrc",
            ".profile",
            ".bash_profile",
            ".bash_logout",
            ".inputrc",
            "bash_completion",
            "PKGBUILD",
        ],
        # Thorough Shebang mapping: Essential for identifying extensionless scripts.
        "shebangs": ["bash", "sh", "zsh", "ksh", "dash", "ash", "rbash"],
        # UPGRADED: Maps to Family 3 (Pure Hash)
        # Rationale: Relies strictly on '#' for line-level Ghost Mass; no native block delimiters.
        "lexical_family": "pure_hash",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Shell uses '#' for standard line-level literature.
            "_line_anchor": re.compile(r"#"),
            # Inline comments are also triggered by the '#' token.
            "_inline_comment": re.compile(r"#"),
            # EXPLICIT: Shell lacks native multi-line block comment delimiters.
            "_block_start": None,
            "_block_end": None,
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Decisions and logic jumps. Includes test constructs [[ ]] and [ ].
            # CRITICAL: Excluded bare '((' and '))' to prevent ReDoS on massive subshell nesting.
            "branch": re.compile(
                r"\b(if|then|else|elif|fi|case|esac|for|while|do|done|until|select|break|continue)\b|&&|\|\||\[\[|\]\]"
            ),
            # 2. args (The Coupling Mass)
            # Positional parameters and expansion markers.
            "args": re.compile(r'\$(?:[1-9]|\{[1-9]\w*\}|@|\*|#)|"\$@"|"\$\*"'),
            # 3. linear (The Smooth Path)
            # Structural boundaries and straight-line execution verbs.
            "linear": re.compile(
                r"\b(local|readonly|export|declare|typeset|return|exit|source|\.|read|cd|pwd|ls|cp|mv|rm|mkdir|touch)\b|\|(?!\s*\|)"
            ),
            # Anchors executable logic blocks. Captures `function foo` or `foo()`.
            # Handled by Mode D (Semantic Handshake) in detector.py.
            'func_start': re.compile(
            r'^[ \t]*(?:function[ \t]+([a-zA-Z_][a-zA-Z0-9_.-]*)|(?!(?:if|while|for|case|until)\b)([a-zA-Z_][a-zA-Z0-9_.-]*)[ \t]*\(\))',
            re.M
            ),
            # 5. class_start
            # Shell is strictly procedural.
            "class_start": None,
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            # Shell hardening: strict modes, traps, and robust quoting.
            "safety": re.compile(
                r'\b(set\s+-(?:[a-zA-Z]*e[a-zA-Z]*|u|o\s+pipefail)|trap\s+[^\n]*(?:ERR|EXIT|INT|TERM))\b|"\$[@*]"|"\$\{[^}]+\}"|\bcommand\s+-v\b|\$\{[a-zA-Z0-9_]+:[-=?][^}]*\}'
            ),
            # 7. safety_neg (The Fractures)
            # Unquoted variables, dynamic evaluation, and blind network-to-shell piping.
            # 7. safety_neg (The Fractures)
            # Unquoted variables, dynamic evaluation, and blind network-to-shell piping.
            "safety_neg": re.compile(
                r'\b(eval)\b(?!\s*\()|(?<!")\$(?![\(?])\w+(?!")|\|\|\s*true\b|>\s*/dev/null(?:\s*2>&1)?|\bcurl\s+[^|\n]{1,200}\|[ \t]*(?:bash|sh|zsh)\b'
            ),
            # 8. danger (The Heavy Load)
            # Destructive commands and privilege elevation. EXCLUDES echo (Phase 5).
            "danger": re.compile(
                r"\b(rm\s+-[rR]f|sudo|chmod\s+(?:-R[ \t]+)?777|chown\s+(?:-R[ \t]+)?root|mkfs|dd|kill(?:all)?)\b"
            ),
            # 9. io (The Boundaries)
            # Redirections, pipes, and network clients.
            "io": re.compile(
                r">|>>|<|\|(?:&)?|\b(curl|wget|nc|ssh|scp|ftp|rsync|cat|tail|grep|find|xargs|jq)\b"
            ),
            # 10. api (The Event Horizon)
            # Exported variables and identifiers modifying the global environment.
            "api": re.compile(r"^[ \t]*export\s+[a-zA-Z_]\w*", re.M),
            # 11. flux (The Boiling Plasma)
            # Mutation of state via assignment or arithmetic.
            "flux": re.compile(
                r"^[ \t]*[a-zA-Z_]\w*(?:\[[^\]]+\])?=(?![=~])|\b(?:let|declare)\s+[a-zA-Z_]\w*=|\[\+\]=|\(\([^)]*(?:\+\+|--|[-+*/%]=)[^)]*\)\)",
                re.M,
            ),
            # 12. graveyard (The Necrosis)
            # Commented-out execution logic indicating dead features.
            "graveyard": re.compile(
                r"#[ \t]*(?:if|for|while|function|export|echo|printf|cd|rm|sudo|ls)\b"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r"^[ \t]*#\s*(?:@param|@return|Usage:|Description:|Examples:|Options:)|#\s*shellcheck\s+disable",
                re.M | re.I,
            ),
            # 14. test (The Verification)
            # Triggers indicating internal verification. Anchored to shell-specific testing framework commands.
            "test": re.compile(
                r"\b(assert_?eq|assertTrue|assertFalse|assert_?match|bats|shunit2)\b|^@test\s+|\brun\s+[a-zA-Z0-9_-]+",
                re.M,
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Complexity) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"&[ \t]*$|\b(wait(?:\s+-n)?|coproc|nohup|parallel|jobs|fg|bg|disown|xargs\s+-P)\b|&\s*\|\||<\([^)]*\)|>\([^)]*\)",
                re.M,
            ),
            # 16. ui_framework (The View Layer)
            # Terminal UI builders and ANSI sequences.
            "ui_framework": re.compile(
                r"\b(dialog|whiptail|zenity|kdialog|notify-send|tput|gum|tmux)\b|\\033\[[0-9;]+m|\\e\[[0-9;]+m"
            ),
            # 17. closures
            "closures": None,  # Shell lacks native anonymous lambdas.
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\b(PATH|HOME|USER|SHELL|EDITOR|PWD|OLDPWD|TERM|LANG|OSTYPE|MACHTYPE|UID|EUID|GROUPS)\b"
            ),
            # 19. decorators
            "decorators": None,
            # 20. generics
            "generics": None,
            # 21. comprehensions (The High-Density Loops)
            # Brace expansions acting as inline loops.
            "comprehensions": re.compile(
                r"\{[0-9]+(?:\.\.|,)[0-9]+(?:\.\.[0-9]+)?\}|\{[a-zA-Z]\.\.[a-zA-Z]\}"
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(r"\b(bc|awk|dc|expr|jq|RANDOM|SRANDOM)\b|\$\(\("),
            # 23. heat_triggers (The Thermal Radiation)
            # Sub-languages and indirect expansion. (ReDoS Shielded)
            "heat_triggers": re.compile(
                r'\$\([^)]+\)|`[^`]+`|\b(?:awk|sed|perl|python[23]?|ruby)\s+[\'"][^\'"]{0,500}|\beval\s+\$|\$\{!?[a-zA-Z0-9_]+\}'
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(r"^[ \t]*(?:source|\.)\s+[^\s]+", re.M),
            
            "_dependency_capture": re.compile(r"^[ \t]*(?:source|\.)\s+['\"]?([^'\"\s]+)['\"]?", re.M),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"^[ \t]*#\s*(?:Author|Created by|Maintainer|Copyright):?\s+(.*)",
                re.M | re.I,
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"#\s*\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            # Legacy CGI shell environments.
            "ssr_boundaries": re.compile(
                r'\b(?:CONTENT_TYPE|QUERY_STRING|HTTP_USER_AGENT)\b|echo\s+"Content-type:\s*text/(?:html|plain|json)'
            ),
            # 32. events (The Pub/Sub Network)
            # Named pipes and OS signal handlers.
            "events": re.compile(
                r"\b(mkfifo|mknod|inotifywait|inotifywatch|fswatch|tail\s+-f|kill\s+-(?:SIG)?(?:USR1|USR2|HUP|TERM))\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\$\{1:-\w+\}|\$\{2:-\w+\}|\b(?:command\s+-v|type\s+-p)\b"
            ),
            # 34. macros (The Preprocessor Hooks)
            "macros": re.compile(r"^[ \t]*(?:alias|shopt)\b", re.M),
            # 35. pointers (The Memory Map)
            # Raw memory addressing. Shell uses namerefs and indirect expansion.
            "pointers": re.compile(r"\b(?:declare\s+-n|typeset\s+-n)\b|\$\{\!"),
            # 36. memory_alloc
            "memory_alloc": None,
            # 37. inline_asm
            "inline_asm": None,
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(?:logger|syslog|log_info|log_err|log_warn|log_debug)\b|>\s*/dev/(?:stderr|console)"
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(r"\b(echo|printf|print|read)\b"),
            # 40. cast_hits
            "cast_hits": None,
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(
                r"\b(exit|kill|abort|halt|return\s+[1-9][0-9]*)\b"
            ),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\b(sleep|read\s+-t)\b"),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": None,
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(r"\b(flock|mkdir|mkfifo|lockfile|sem)\b"),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(r"\b(readonly|declare\s+-r|typeset\s+-r)\b"),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(r"\b(rm\s+-f|trap\s+.*EXIT|unset|exit|logout)\b"),
            # 47. encapsulation (The Vault)
            # Physical Reality: local variables represent internal state scope.
            "encapsulation": re.compile(r"\b(local|typeset|declare)\b"),
            # 48. listeners (The Sinks)
            "listeners": re.compile(r"\b(read|inotifywait|nc\s+-l|while\s+read)\b"),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(r"\b(test\.skip|bats_skip|#\s*SKIP|mock|stub)\b"),
        },
    },
    "ruby": {
        "_meta": {
            "target_version": "Ruby 4.0 Paradigms (Ruby 3.4+ / Ractors / Sorbet / Pattern Matching)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard suffixes, rack configs (.ru), gem specs, and various templating/DSL extensions.
        "extensions": [
            ".rb",
            ".rbw",
            ".rake",
            ".rbi",
            ".gemspec",
            ".rbx",
            ".builder",
            ".ru",
            ".podspec",
            ".jbuilder",
            ".rabl",
        ],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Extensionless infrastructure-as-code and dependency configurations that are secretly pure Ruby.
        "exact_matches": [
            "Gemfile",
            "Rakefile",
            "Vagrantfile",
            "Guardfile",
            "Capfile",
            "Thorfile",
            "Berksfile",
            "Cheffile",
            "Podfile",
            "Fastfile",
            "Appraisals",
        ],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, lockfiles, and environment pins to lock in context.
        "discriminators": [
            ".rb",
            "Gemfile.lock",
            ".ruby-version",
            ".ruby-gemset",
            "config.ru",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1.
        "shebangs": ["ruby", "macruby", "jruby", "rbx"],
        # UPGRADED: Maps to Family 4 (Hybrid Hash)
        # Rationale: Uses '#' for single-line comments, but multi-line literature
        # utilizes the `=begin ... =end` block syntax, requiring hybrid parsing rules.
        "lexical_family": "hybrid_hash",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Ruby uses '#' for standard line-level literature (Ghost Mass).
            "_line_anchor": re.compile(r"#"),
            # Inline comments are also triggered by the '#' token.
            "_inline_comment": re.compile(r"#"),
            # Block comment start: =begin (Must be at the absolute start of the line).
            "_block_start": re.compile(r"^=begin", re.M),
            # Block comment end: =end (Must be at the absolute start of the line).
            "_block_end": re.compile(r"^=end", re.M),
            # 1. branch (The Forks in the Road)
            # Decisions and logical jumps. EXCLUDES raise/throw (bailout_hits).
            "branch": re.compile(
                r"\b(if|unless|elsif|else|case|when|in|for|while|until|begin|rescue|ensure|break|next|redo|retry)\b|&&|\|\||\?|=>"
            ),
            # 2. args (The Coupling Mass)
            # Parameter blocks of methods, lambdas, and blocks. Bounded to prevent ReDoS.
            "args": re.compile(
                r"\bdef\s+(?:self\.)?[a-zA-Z_]\w*[=!?]?\s*\([^)]*\)|\bdo\s*\|[^|]*\||\{\s*\|[^|]*\||->\s*\([^)]*\)",
                re.M,
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: Access modifiers (encapsulation) and const (freeze_hits).
            "linear": re.compile(
                r"\b(class|module|def|yield|return|super|alias|undef|require|require_relative|include|extend|prepend|attr_reader|attr_writer|attr_accessor|Data\.define)\b"
            ),
            # 4. func_start (The Satellite Spawner)
            # ONLY executable logic blocks. EXCLUDES class/module definitions.
            "func_start": re.compile(
                r'^[ \t]*(?:def\s+(?:self\.)?|define_method\s*\(?\s*[:\'"]?)([a-zA-Z_]\w*[=!?]?)(?=[ \t]*[)\(]|[\'"]?\s*(?:\{|do)|[ \t]*$|[ \t]+)',
                re.M,
            ),
            # 5. class_start (The Entity Census)
            "class_start": re.compile(
                r"^[ \t]*(?:class|module)\s+[A-Z]\w*(?:::[A-Z]\w*)*", re.M
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\&\.|\b(rescue|ensure|fetch|frozen_string_literal|freeze|catch|throw|safe_load|T\.must|T\.let|T\.cast|T\.bind)\b"
            ),
            # 7. safety_neg (The Fractures)
            # Dynamic logic bypasses and Sorbet escape hatches.
            "safety_neg": re.compile(
                r"\b(eval|class_eval|instance_eval|module_eval|send|__send__|public_send|binding|instance_variable_set|unsafe_load|T\.unsafe|T\.untyped)\b"
            ),
            # 8. danger (The Heavy Load)
            # Process killers and shell execution. EXCLUDES puts (Phase 5).
            "danger": re.compile(
                r"\b(abort|exit|exit!|system|exec|spawn|fork)\b|`[^`]+`|IO\.popen"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(File|Dir|IO|Net::HTTP|URI\.open|Socket|TCPSocket|FileUtils|ActiveRecord::Base|find|where|create|update|destroy)\b"
            ),
            # 10. api (The Event Horizon)
            # Implicit public defaults (undercased defs) + explicit module functions.
            "api": re.compile(
                r'\b(module_function)\b|^[ \t]*(?:get|post|put|patch|delete|resources?)\s+[:\'"]',
                re.M,
            ),
            # 11. flux (The Boiling Plasma)
            # Mutation of state. EXCLUDES const (freeze_hits).
            "flux": re.compile(
                r"@[a-zA-Z_]\w*\s*(?:\+|-|\*|/)?=|@@[a-zA-Z_]\w*\s*(?:\+|-|\*|/)?=|\b(?:push|pop|shift|unshift|delete|clear|merge!|update!|gsub!|map!|select!|reject!)\b|<<"
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"#[ \t]*(?:def|class|module|if|unless|while|puts|p)\b"
            ),
            # 13. doc (The Intent)
            # Captures YARD tags, Sorbet signatures, RDoc blocks/modifiers, and standard documentation headers.
            "doc": re.compile(
                r"^[ \t]*#\s*@(?:param|return|api|yield|raise|see|abstract|deprecated|note|example)|^[ \t]*sig[ \t]*\{|^=begin\s+(?:rdoc|pod)\b|^[ \t]*#\s*(?::nodoc:|:yields:|:args:|:return:)|^[ \t]*#\s*(?:Description|Usage|Example|Summary):\s+",
                re.M | re.I,
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r'\b(describe|context|expect|assert[a-zA-Z_]*|refute[a-zA-Z_]*|setup|teardown|before|after|let|subject)\b|\b(?:it|test)\s+[\'"]'
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Complexity) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(Thread|Mutex|Monitor|ConditionVariable|Ractor|Fiber|Async|await|Concurrent)\b"
            ),
            # 16. ui_framework (The View Layer)
            "ui_framework": re.compile(
                r"\b(ActionView|render|render_to_string|ViewComponent::Base|Phlex::HTML|form_with|form_for|link_to|stylesheet_link_tag|Turbo|Stimulus|Hotwire)\b|<%|%>"
            ),
            # 17. closures (The Functional Depth)
            "closures": re.compile(
                r"\b(?:do\s*\|[^|]*\||do\b|\{\s*\|[^|]*\||->\s*(?:\([^)]*\))?[ \t]*\{)"
            ),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\$[a-zA-Z_]\w*|\b(ENV|ARGV|ARGF|STDIN|STDOUT|STDERR|RUBY_VERSION)\b"
            ),
            # 19. decorators (The Metadata Hooks)
            # Rails class macros acting as metadata descriptors.
            "decorators": re.compile(
                r"^[ \t]*(?:before_action|after_action|around_action|before_save|after_commit|validates|has_many|belongs_to|has_one)\b",
                re.M,
            ),
            # 20. generics (The Type Abstractions)
            # Sorbet parameterized types.
            "generics": re.compile(
                r"\b(?:T::|::T::)?(?:Array|Hash|Set|Enumerable|Class)\[[^\]]*\]"
            ),
            # 21. comprehensions (The High-Density Loops)
            "comprehensions": re.compile(
                r"\.(?:map|collect|select|reject|reduce|inject|filter_map|flat_map|each_with_object|partition|group_by)\b(?:[ \t]*\{|\s*do)"
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(Math|Complex|Rational|Matrix|Vector|Numo::NArray|BigDecimal)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Metaprogramming and runtime object extensions.
            "heat_triggers": re.compile(
                r"\b(method_missing|define_method|const_missing|respond_to_missing\?|included|extended|prepended|class\s*<<\s*self)\b"
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(
                r"^[ \t]*(?:require|require_relative|load|autoload)\b", re.M
            ),
            
            "_dependency_capture": re.compile(r"^[ \t]*(?:require|require_relative|load|autoload)\b[^'\"]*['\"]([^'\"]+)['\"]", re.M),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"#\s*(?:Author|Created by|Maintainer|Copyright):\s+(.*)", re.I
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": re.compile(
                r"\b(ActionController::Base|ActionController::API|Sinatra::Base|Hanami::Action|respond_to|format\.html|format\.json)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(Wisper|broadcast|subscribe|ActiveSupport::Notifications\.instrument|publish)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\b(Dry::Container|Dry::AutoInject|include\s+Import|inject)\b"
            ),
            # 34. macros (The Preprocessor Hooks)
            # Ruby DSL macros.
            "macros": re.compile(
                r"^[ \t]*(?:attr_accessor|attr_reader|attr_writer|scope|delegate)\b",
                re.M,
            ),
            # 35. pointers (The Memory Map)
            "pointers": re.compile(
                r"\b(FFI::Pointer|Fiddle::Pointer|Fiddle::Function)\b"
            ),
            # 36. memory_alloc (Manual Memory Management)
            "memory_alloc": re.compile(
                r"\b(ObjectSpace|GC\.start|GC\.disable|GC\.enable|FFI::MemoryPointer)\b"
            ),
            # 37. inline_asm
            "inline_asm": None,
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(?:Rails\.logger|Logger\.new|SemanticLogger|[a-zA-Z_]\w*logger)\.(?:debug|info|warn|error|fatal|unknown)\b"
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(r"\b(puts|print|p|pp|warn)\b"),
            # 40. cast_hits (The Trust Me Tax)
            "cast_hits": re.compile(
                r"\b(Integer|Float|String|Array|Hash|Complex|Rational)\b\s*\("
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(raise|fail|abort|exit!)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\bsleep\b\s*[0-9.]+"),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(r"\^|(?<![=!])~"),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(mutex|lock|synchronized|Semaphore|Monitor|Atomic[A-Z]\w*)\b", re.I
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(r"\b(freeze|frozen_string_literal|immutable)\b"),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r"\b(close|GC\.start|dispose|shutdown|cleanup)\b\s*\("
            ),
            # 47. encapsulation (The Vault)
            # Visibility modifiers in Ruby.
            "encapsulation": re.compile(r"\b(private|protected)\b"),
            # 48. listeners (The Sinks)
            "listeners": re.compile(r"\.subscribe\(|\.on\(|addEventListener"),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(r"\b(skip|xit|xdescribe|mock|stub|double)\b"),
        },
    },
    "swift": {
        "_meta": {
            "target_version": "Swift 6.2 / iOS 18+ / Strict Concurrency, Macros & Swift Testing",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard sources and module interface declarations.
        "extensions": [".swift", ".swiftinterface"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Tooling configurations that are secretly pure Swift code.
        "exact_matches": ["Package.swift"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions and package manager lockfiles to resolve ambiguous files in mixed Apple environments.
        "discriminators": [".swift", "Package.resolved", "project.pbxproj"],
        # EXECUTION SIGNATURES: Interpreters found on Line 1 for Swift-based scripting and automation.
        "shebangs": ["swift", "swift-sh"],
        # UPGRADED: Maps to Family 2 (Nested C)
        # Rationale: Supports nested block comments (/* /* */ */), necessitating depth-aware stripping
        # rather than standard C-style early termination.
        "lexical_family": "nested_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Standard C-family line comment token
            "_line_anchor": re.compile(r"//"),
            # Inline comments follow the same '//' delimiter.
            "_inline_comment": re.compile(r"//"),
            # REQUIRED for Family 2: Recursive logic markers
            "_block_start": re.compile(r"/\*"),
            # REQUIRED for Family 2: Recursive logic markers
            "_block_end": re.compile(r"\*/"),
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Decisions and logical jumps. Includes modern typed throws (throws(Error)).
            # EXCLUDES throw/rethrows (bailout_hits).
            "branch": re.compile(
                r"\b(if|else|guard|switch|case|default|for|while|repeat|do|catch|break|continue|defer|try)\b|&&|\|\||\?|\?\?"
            ),
            # 2. args (The Coupling Mass)
            # Parameter blocks. Bounded negation [^)]* and <[^>]*> to prevent ReDoS.
            "args": re.compile(
                r"\b(?:func|init\??|subscript)\s*(?:[a-zA-Z_]\w*)?(?:<[^>]*>)?\s*\([^)]*\)|\{\s*(?:\[[^\]]*\]\s*)?(?:\([^)]*\)|[a-zA-Z_]\w*(?:\s*,\s*[a-zA-Z_]\w*){0,10})\s+in\b",
                re.M,
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: Access modifiers (encapsulation) and let (freeze_hits).
            "linear": re.compile(
                r"\b(var|struct|class|enum|protocol|extension|actor|macro|import|typealias|associatedtype|some|any|consume|borrow|discard|mutating|nonmutating|isolated|nonisolated|return|yield|await|inout)\b|~Copyable"
            ),
            # 4. func_start (The Satellite Spawner)
            # ONLY executable logic blocks. EXCLUDES types/classes. Steps over Concurrency modifiers.
            "func_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]*){0,5}"
                r"(?:(?:public|private|fileprivate|internal|open|package|override|final|static|class|mutating|nonmutating|isolated|nonisolated(?:\(unsafe\))?|distributed|required|convenience)[ \t]+){0,5}"
                r"(?:func\s+([a-zA-Z_]\w*)|(init\??)|(subscript))(?=\s*\()",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            "class_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]*){0,5}(?:(?:public|private|fileprivate|internal|open|package|final|distributed)[ \t]+){0,5}(?:class|struct|enum|protocol|actor|extension|macro)\s+[a-zA-Z_]\w*",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\b(guard\s+let|if\s+let|guard\s+var|if\s+var|try\?|as\?|catch|is|Sendable|Result|assert|precondition|Mutex)\b|@MainActor|\?\?"
            ),
            # 7. safety_neg (The Fractures)
            # Unsafe pointers and linter bypasses. EXCLUDES forced unwraps (moved to friction).
            "safety_neg": re.compile(
                r"\bunowned(?:\(unsafe\))?\b|\bnonisolated\(unsafe\)|\bunsafeDowncast\b|//\s*swiftlint:disable"
            ),
            # 8. danger (The Heavy Load)
            # Fatal traps and process killers. EXCLUDES TODO (debt) and print (print_hits).
            "danger": re.compile(
                r"\b(fatalError|preconditionFailure|assertionFailure|abort|exit)\b"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(URLSession|FileManager|FileHandle|Data\(contentsOf:|write\(to:|UserDefaults|CoreData|SwiftData|NWConnection)\b"
            ),
            # 10. api (The Event Horizon)
            # Exposed surface area. Explicit visibility and Objective-C bridges.
            "api": re.compile(
                r"\b(public|open|package|@usableFromInline|@objc|@objcMembers|@_exported|@IBAction|@IBOutlet|@Published)\b"
            ),
            # 11. flux (The Boiling Plasma)
            # Mutation of state. EXCLUDES let (freeze_hits).
            "flux": re.compile(
                r"\b(var|inout|mutating|didSet|willSet|_modify)\b|@(?:State|Binding|FocusState|Bindable|Observable)|^[ \t]*(?:self\.)?[a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*){0,5}\s*[-+*/]?=|\.(?:append|insert|remove|toggle|updateValue)\("
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"//[ \t]*(?:let|var|func|class|struct|actor|extension|if|guard|return)\b"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r"///|/\*\*|-\s*parameter|-\s*returns:|-\s*throws:|-\s*warning:"
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r"\b(?:XCTest|XCTestCase|XCTAssert[A-Za-z]*|setUp|tearDown)\b|@(?:Test|Suite)\b|#(?:expect|require)\b"
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Complexity) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(async|await|actor|Task|TaskGroup|DispatchQueue|OperationQueue|MainActor|Sendable|isolated|nonisolated|continuation)\b"
            ),
            # 16. ui_framework (The View Layer)
            "ui_framework": re.compile(
                r"\b(View|Body|ZStack|VStack|HStack|Text|Image|Button|SwiftUI|UIKit|AppKit|UIView|UIViewController|NSView|NSWindow|@State|@Binding|@Environment)\b"
            ),
            # 17. closures (The Functional Depth)
            "closures": re.compile(
                r"completion:[ \t]*\{|\{\s*(?:\[[^\]]*\]\s*)?(?:\([^)]*\)|[a-zA-Z_]\w*(?:\s*,\s*[a-zA-Z_]\w*)*)\s+in\b"
            ),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\b(?:static\s+let|static\s+var|shared|standard|default|NotificationCenter\.default|UserDefaults\.standard|FileManager\.default)\b|@Environment\b"
            ),
            # 19. decorators (The Metadata Hooks)
            "decorators": re.compile(r"@[a-zA-Z_]\w*(?:\([^)]*\))?"),
            # 20. generics (The Type Abstractions)
            "generics": re.compile(
                r"<\s*[A-Z][^>]*>|\bwhere\s+[a-zA-Z_]\w*\s*:|\b(?:some|any|each)\s+[A-Z]\w*"
            ),
            # 21. comprehensions (The High-Density Loops)
            "comprehensions": re.compile(
                r"\.(?:map|compactMap|flatMap|filter|reduce|forEach|allSatisfy|contains)\s*(?:\(|\{)"
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(simd|Accelerate|Double|Float|Float16|CGFloat|Decimal|CoreML|CreateML|vDSP|sqrt|pow|sin|cos|tan)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Reflection and Dynamic Dispatch.
            "heat_triggers": re.compile(
                r"\b(@objc|dynamic|Mirror\(|unsafeBitCast|withUnsafe\w+|KeyPath|WritableKeyPath)\b|\\\.[\w.]+"
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(
                r"^[ \t]*(?:@_exported[ \t]+)?import\s+[a-zA-Z_]\w*", re.M
            ),
            
            "_dependency_capture": re.compile(r"^[ \t]*(?:@_exported[ \t]+)?import\s+(?:(?:typealias|struct|class|enum|protocol|let|var|func)\s+)?([a-zA-Z_][\w.]+)", re.M),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"//\s*(?:Created by|Author:|Copyright):\s+(.*)", re.I
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": re.compile(
                r"\b(Vapor|Hummingbird|Request|Response|Route|app\.get|app\.post|EventLoopFuture)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(NotificationCenter|Combine|Publisher|Subscriber|CurrentValueSubject|PassthroughSubject|AnyCancellable|\.sink|\.assign|@Published|ObservableObject|Observation)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\b(@Environment|@EnvironmentObject|@Inject|@Dependency|Swinject|Container|Resolver|Factory)\b"
            ),
            # 34. macros (The Preprocessor Hooks)
            "macros": re.compile(
                r"#(?:Preview|Predicate|OptionSet|Rule|warning|error)\b|@(?:freestanding|attached)|#[A-Z]\w*"
            ),
            # 35. pointers (The Memory Map)
            "pointers": re.compile(
                r"\b(?:Unsafe(?:Mutable)?(?:Raw|Buffer)?Pointer|OpaquePointer|CVaListPointer|Unmanaged)\b|\.pointee\b|(?<=[=\s,(])&\w+"
            ),
            # 36. memory_alloc (Manual Memory Management)
            "memory_alloc": re.compile(
                r"\b(?:malloc|calloc|free|\.allocate\(capacity:|\.deallocate\(\)|ManagedBuffer)\b"
            ),
            # 37. inline_asm
            "inline_asm": None,  # Swift delegates ASM to C-headers.
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(?:Logger|OSLog|os_log)\b|\bLogger\([^)]*\)\.(?:info|error|warning|debug|trace|notice|critical|fault)\b",
                re.I,
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(r"\b(print|debugPrint|dump)\b"),
            # 40. cast_hits (The "Trust Me" Tax)
            "cast_hits": re.compile(
                r"\bas[!?]?\s+[A-Z]\w*|\bis\s+[A-Z]\w*|\b(?:Int|Double|Float|Float16|CGFloat|String|Bool)\s*\("
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(
                r"\b(throw|fatalError|abort|exit|preconditionFailure)\b"
            ),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\b(sleep|delay|Task\.sleep)\b"),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(r"<<|>>|\^|(?<![=!])~|<<=|>>=|\^="),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(mutex|lock|synchronized|Semaphore|OSAllocatedUnfairLock|MainActor|distributed)\b",
                re.I,
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(
                r"\b(let|final|static|readonly|Immutable|Sendable)\b"
            ),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r"\b(deinit|close|free|dispose|shutdown|removeAll)\b\s*\("
            ),
            # 47. encapsulation (The Vault)
            "encapsulation": re.compile(r"\b(private|fileprivate|internal)\b"),
            # 48. listeners (The Sinks)
            "listeners": re.compile(
                r"\.onAppear\(|\.onChange\(|\.sink\(|addObserver|subscribe"
            ),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(r"\b(XCTSkip|mock\(|stub\(|fake\(|double\()\b"),
        },
    },
    "kotlin": {
        "_meta": {
            "target_version": "Kotlin 2.3.10 (K2 Compiler / Wasm / Java 25 Support)",
            "last_updated": "2026-03-12",
            "blueprint_version": "v6.3.1",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard sources, Kotlin script files (heavily used in modern Gradle), and module declarations.
        "extensions": [".kt", ".kts", ".ktm"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Kotlin rarely uses extensionless execution scripts.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions and Kotlin-DSL Gradle build files to lock in context.
        "discriminators": [
            ".kt",
            "build.gradle.kts",
            "settings.gradle.kts",
            "gradle.properties",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1 for Kotlin scripting.
        "shebangs": ["kotlin", "kotlinc", "kscript"],
        # UPGRADED: Maps to Family 2 (Nested C)
        # Rationale: (CORRECTION) While Kotlin uses // and /* */, it officially allows nested
        # block comments (/* /* */ */). Using standard C parsing would cause early termination here.
        "lexical_family": "std_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Standard C-family line comment token
            "_line_anchor": re.compile(r"//"),
            # Inline comments follow the same '//' delimiter.
            "_inline_comment": re.compile(r"//"),
            # Block comment start: /*
            "_block_start": re.compile(r"/\*"),
            # Block comment end: */
            "_block_end": re.compile(r"\*/"),
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Decisions and logical jumps. Includes modern 'when' and Elvis operator.
            # EXCLUDES throw (bailout_hits).
            "branch": re.compile(
                r"\b(if|else|when|for|while|do|try|catch|finally|break|continue|return)\b|\?:|&&|\|\|"
            ),
            # 2. args (The Coupling Mass)
            # OPTIMIZED: Removed overlapping whitespace quantifiers to fix Regex Sludge.
            "args": re.compile(
                r"\b(?:fun|constructor)(?:<[^>\n]{0,100}>)?[ \t]*(?:[a-zA-Z_]\w*\.)?[a-zA-Z_]\w*[ \t]*\([^)\{]{0,500}\)|\{[ \t\n]*[a-zA-Z_][a-zA-Z0-9_ \t\n:<>,.?]{0,150}?->",
                re.M,
            ),

            # 4. func_start (The Satellite Spawner)
            # OPTIMIZED: Bound annotation parenthesis scanning to prevent multi-line bleeding.
            "func_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)\{]{0,300}\))?[ \t]+){0,10}(?:(?:public|private|protected|internal|open|override|abstract|final|suspend|inline|tailrec|infix|operator|external|expect|actual)[ \t]+){0,5}(?:context\s*\([^)]*\)\s*)?(?:fun\s+(?:<[^>\n]{0,100}>\s*)?(?:[a-zA-Z_]\w*\.)?([a-zA-Z_]\w*)|(init)|(constructor))(?=[ \t]*[\(\{])",
                re.M,
            ),
            
            # 5. class_start (The Entity Census)
            # OPTIMIZED: Applied the same 300-char bounds to class annotations.
            "class_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)\{]{0,300}\))?[ \t]*){0,10}(?:(?:public|private|protected|internal|open|abstract|final|sealed|data|value|annotation|expect|actual|inner)[ \t]+){0,5}(?:class|interface|object|enum\s+class)\s+[a-zA-Z_]\w*",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\?\.(?!.)|as\?|\b(require|requireNotNull|check|checkNotNull|error|sealed|is|!is|Result|onSuccess|onFailure|fold|runCatching)\b|\?:"
            ),
            # 7. safety_neg (The Fractures)
            # Force unwrapping, unsafe casts, and suppression.
            "safety_neg": re.compile(r"!!|as(?!\?)\b|\blateinit\s+var\b|@Suppress\b"),
            # 8. danger (The Heavy Load)
            # Process killers and raw system triggers. EXCLUDES println (Phase 5).
            "danger": re.compile(
                r"\b(System\.exit|exitProcess|Runtime\.getRuntime|Thread\.stop)\b"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(File|InputStream|OutputStream|Retrofit|OkHttpClient|Ktor|HttpClient|RoomDatabase|Dao|SharedPreferences|DataStore|java\.nio)\b"
            ),
            # 10. api (The Event Horizon)
            # Exposed surface. Implicit public/internal defaults + Ktor/Spring routes.
            "api": re.compile(
                r"\b(public|internal)\b|@(RestController|Controller|Service|Component|RequestMapping|GetMapping|PostMapping|Route)\b"
            ),
            # 11. flux (The Boiling Plasma)
            # CRITICAL FIX: Added re.M so it scans every line, not just the first line of the file!
            "flux": re.compile(
                r"\b(var|MutableList|MutableMap|MutableSet|MutableState|MutableStateFlow|Atomic[A-Za-z0-9]+)\b|^[ \t]*(?:this\.)?[a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*\s*[-+*/%]?=|\.(?:add|addAll|remove|put|set|update)\(",
                re.M,
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"//[ \t]*(?:val|var|fun|class|interface|object|if|when|for|return|import)\b"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r"/\*\*|@param|@return|@property|@receiver|@constructor|@throws|@see|@since"
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r"@(?:Test|ParameterizedTest|BeforeTest|AfterTest)|\b(?:assert[A-Za-z0-9_]*|mockk|spyk|test)\s*\(|\b(?:shouldBe|shouldNotBe)\b|\b(?:every|verify)\s*\{"
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Complexity) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(suspend|launch|async|CoroutineScope|GlobalScope|Dispatchers|Flow|StateFlow|SharedFlow|Channel|yield|runBlocking|withContext|Mutex)\b"
            ),
            # 16. ui_framework (The View Layer)
            "ui_framework": re.compile(
                r"@Composable|Modifier|\b(Column|Row|Box|Text|Image|Button|Scaffold|LazyColumn|LazyRow|Surface|remember|mutableStateOf|findViewById|View|Activity|Fragment)\b"
            ),
            # 17. closures (The Functional Depth)
            # OPTIMIZED: Removed overlapping whitespace quantifiers to fix ReDoS.
            "closures": re.compile(
                r"\{[ \t\n]*[a-zA-Z_][a-zA-Z0-9_ \t\n:<>,.?]{0,150}?->"
            ),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\b(object|companion\s+object)\b|^[ \t]*(?:const[ \t]+)?val\s+[A-Z_0-9]+[ \t]*=",
                re.M,
            ),
            # 19. decorators (The Metadata Hooks)
            # OPTIMIZED: Bounded arguments.
            "decorators": re.compile(r"@[a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*(?:\([^)\{]{0,300}\))?"),
                        # 20. generics (The Type Abstractions)
            # Prevented catastrophic backtracking across newlines.
            "generics": re.compile(
                r"<\s*(?:in|out)?\s*[A-Z][^>\n]{0,100}>|\breified\b|\bwhere\b"
            ),
            # 21. comprehensions (The High-Density Loops)
            # Functional collection transformations.
            "comprehensions": re.compile(
                r"\.(?:map|mapNotNull|filter|filterNot|reduce|fold|flatMap|zip|associate|groupBy|forEach|any|all|none|find)\b"
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(kotlin\.math\.|java\.lang\.Math\.|StrictMath\.|Random\.|sin|cos|tan|sqrt|exp|log|abs|BigDecimal|BigInteger)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Reflection and optimization hooks.
            "heat_triggers": re.compile(
                r"::class|javaClass|@JvmOverloads|@JvmStatic|@JvmField|@JvmName|\b(inline|crossinline|noinline|invoke|context|tailrec)\b"
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(r"^[ \t]*import\s+(?:static[ \t]+)?[\w.]+;?", re.M),
            
            "_dependency_capture": re.compile(r"^[ \t]*import\s+(?:static\s+)?([\w.]+)", re.M),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"@(?:author|since)\s+(.*)|//\s*(?:Created by|Maintainer|Copyright):\s+(.*)",
                re.I,
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": re.compile(
                r"\b(ApplicationCall|call\.respond|call\.respondText|call\.respondHtml|ServerResponse|ModelAndView)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\.(?:collect|collectLatest|observe|subscribe|onNext)\(|\b(LiveData|Observer|Observable|FlowCollector)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"@(?:Inject|Module|Provides|Binds|HiltViewModel|AndroidEntryPoint|Component|Autowired)|(?:koin|get|inject)\(\)"
            ),
            # 34. macros (The Preprocessor Hooks)
            "macros": re.compile(
                r"@(?:OptIn|RequiresOptIn|Suppress|SuppressWarnings)\b"
            ),
            # 35. pointers (The Memory Map)
            # Kotlin/Native FFI boundaries.
            "pointers": re.compile(
                r"\b(?:CPointer|COpaquePointer|CFunction|CValue|CPointed)\b"
            ),
            # 36. memory_alloc (Manual Memory Management)
            "memory_alloc": re.compile(
                r"\b(?:memScoped|alloc|allocArray|nativeHeap\.alloc|nativeHeap\.free)\b"
            ),
            # 37. inline_asm
            "inline_asm": None,  # Usually bridged via C-headers in Native.
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(?:Timber|Log|Logger|LoggerFactory)\.(?:i|e|w|d|v|info|error|warn|warning|debug|trace|verbose)\b|@Slf4j"
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(r"\b(println|print)\b\s*\("),
            # 40. cast_hits (The Trust Me Tax)
            "cast_hits": re.compile(
                r"\bas\??\s+[A-Z]\w*|\.to(?:Int|Long|Short|Byte|Double|Float|String|Boolean|UInt|ULong|UShort|UByte)\(\)"
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(throw|raise|exitProcess|return|panic)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\b(delay|Thread\.sleep|yield)\b"),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(
                r"\.(?:shl|shr|ushr|and|or|xor|inv)\(|\b(?:shl|shr|ushr|xor)\b"
            ),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(mutex|lock|synchronized|Semaphore|Atomic[A-Z]\w*)\b", re.I
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(r"\b(val|const|immutable|readonly)\b"),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(r"\b(close|dispose|shutdown|use|cleanup)\b\s*\("),
            # 47. encapsulation (The Vault)
            "encapsulation": re.compile(r"\b(private|protected|internal)\b"),
            # 48. listeners (The Sinks)
            "listeners": re.compile(
                r"\.(?:collect|observe|subscribe|on[A-Z]\w*|set[A-Z]\w*Listener)\("
            ),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(
                r"@(?:Ignore|Disabled)|test\.skip\(|mockk|spyK|fake\("
            ),
        },
    },
    "sqlite": {
        "_meta": {
            "target_version": "SQLite 3.51.2+ (STRICT Tables, JSONB, RETURNING, Math & CTEs)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard SQL scripts, data definition, and data manipulation files.
        "extensions": [".sql", ".ddl", ".dml"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Standard SQLite configuration and history files that consist of CLI commands/SQL.
        "exact_matches": [".sqliterc"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Binary database files acting as gravitational anchors to prove a .sql file is SQLite and not Postgres/MySQL.
        "discriminators": [
            ".sql",
            ".db",
            ".sqlite",
            ".sqlite3",
            ".db3",
            ".s3db",
            ".sl3",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1.
        "shebangs": ["sqlite3", "sqlite"],
        # UPGRADED: Maps to Family 5 (Hybrid Dash)
        # Rationale: Uses '--' for line-level and '/*' '*/' for block-level Ghost Mass.
        "lexical_family": "hybrid_dash",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # SQLite uses '--' for standard line-level literature.
            "_line_anchor": re.compile(r"--"),
            # Inline comments are also triggered by the '--' token.
            "_inline_comment": re.compile(r"--"),
            # Block comment start: /*
            "_block_start": re.compile(r"/\*"),
            # Block comment end: */
            "_block_end": re.compile(r"\*/"),
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Decisions and logical filters. Includes case logic and modern IIF().
            "branch": re.compile(
                r"\b(CASE|WHEN|THEN|ELSE|END|IFNULL|NULLIF|COALESCE|IIF|FILTER|WHERE|HAVING)\b",
                re.I,
            ),
            # 2. args (The Coupling Mass)
            # Parameter blocks and input coupling. Bounded to prevent ReDoS on massive IN clauses.
            "args": re.compile(
                r"\?[0-9]*|[:@$][a-zA-Z_]\w*|\b(?:VALUES|IN)\s*\([^)]*\)", re.I
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries defining query execution flow.
            "linear": re.compile(
                r"\b(SELECT|FROM|JOIN|INNER\s+JOIN|LEFT\s+JOIN|CROSS\s+JOIN|GROUP\s+BY|ORDER\s+BY|LIMIT|OFFSET|UNION|INTERSECT|EXCEPT|RETURNING|AS|INTO|WINDOW|STRICT|WITHOUT\s+ROWID|PARTITION\s+BY|PRECEDING|FOLLOWING|UNBOUNDED|CURRENT\s+ROW)\b",
                re.I,
            ),
            # 4. func_start (The Satellite Spawner)
            # Executable logic wrappers. EXCLUDES tables to avoid Ghost Satellites.
            "func_start": re.compile(
                r"^[ \t]*CREATE\s+(?:TEMP|TEMPORARY)?\s*(?:UNIQUE[ \t]+)?(?:TRIGGER|VIEW|INDEX)\s+"
                r"(?:IF\s+NOT\s+EXISTS[ \t]+)?([a-zA-Z_]\w*)(?=[ \t\(\n;])",
                re.I | re.M,
            ),
            # 5. class_start (The Entity Census)
            # Physical entity instantiation (Tables).
            "class_start": re.compile(
                r"^[ \t]*CREATE\s+(?:TEMP|TEMPORARY)?\s*(?:VIRTUAL[ \t]+)?TABLE\s+"
                r"(?:IF\s+NOT\s+EXISTS[ \t]+)?([a-zA-Z_]\w*)(?=[ \t\(\n;])",
                re.I | re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\b(TRANSACTION|COMMIT|ROLLBACK|SAVEPOINT|RELEASE|CONSTRAINT|CHECK|UNIQUE|PRIMARY\s+KEY|FOREIGN\s+KEY|STRICT|IF\s+NOT\s+EXISTS|ON\s+DELETE\s+CASCADE|PRAGMA\s+foreign_keys[ \t]*=\s*(?:1|ON))\b",
                re.I,
            ),
            # 7. safety_neg (The Fractures)
            # Bypassing safety checks and structural removals.
            "safety_neg": re.compile(
                r"\b(DROP\s+TABLE|DROP\s+VIEW|DROP\s+INDEX|PRAGMA\s+foreign_keys[ \t]*=\s*(?:0|OFF)|PRAGMA\s+writable_schema[ \t]*=\s*(?:1|ON)|PRAGMA\s+ignore_check_constraints[ \t]*=\s*(?:1|ON)|IF\s+EXISTS)\b",
                re.I,
            ),
            # 8. danger (The Heavy Load)
            # Destructive schema actions and system bypasses.
            "danger": re.compile(
                r"\b(PRAGMA\s+legacy_alter_table|DROP\s+DATABASE|\.shell|\.system|\.exit|\.quit)\b"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(SELECT|INSERT|UPDATE|DELETE|REPLACE|ATTACH\s+DATABASE|DETACH\s+DATABASE|\.import|\.output|\.dump|\.read|readfile|writefile)\b",
                re.I,
            ),
            # 10. api (The Event Horizon)
            # Exposed surface area (Views and Virtual Tables).
            "api": re.compile(
                r"^[ \t]*CREATE\s+(?:TEMP|TEMPORARY)?\s*(?:VIEW|VIRTUAL\s+TABLE)\s+",
                re.I | re.M,
            ),
            # 11. flux (The Boiling Plasma)
            # Mutation of state. Includes UPSERT.
            "flux": re.compile(
                r"\b(UPDATE|SET|ALTER\s+TABLE|ADD\s+COLUMN|DROP\s+COLUMN|RENAME\s+TO|UPSERT|ON\s+CONFLICT\s+DO\s+UPDATE|ON\s+CONFLICT\s+DO\s+NOTHING|REPLACE\s+INTO|EXCLUDED\.[a-zA-Z_]\w*|jsonb?_(?:insert|replace|set|remove|patch))\b",
                re.I,
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"--[ \t]*(?:SELECT|INSERT|UPDATE|DELETE|CREATE|DROP|ALTER|PRAGMA)\b",
                re.I,
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r"--\s*@(?:param|return|brief|table|column)|/\*\*|--\s*Description:"
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r"\b(?:EXPLAIN[ \t]+QUERY[ \t]+PLAN|PRAGMA[ \t]+integrity_check|PRAGMA[ \t]+foreign_key_check|\.testcase|\.lint)\b",
                re.I,
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Complexity) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(BEGIN\s+EXCLUSIVE|BEGIN\s+IMMEDIATE|PRAGMA\s+journal_mode[ \t]*=\s*WAL|PRAGMA\s+busy_timeout|PRAGMA\s+synchronous|PRAGMA\s+wal_checkpoint)\b",
                re.I,
            ),
            # 16. ui_framework
            "ui_framework": None,
            # 17. closures (The Functional Depth)
            # Common Table Expressions (CTEs).
            "closures": re.compile(
                r"\bWITH\s+(?:RECURSIVE[ \t]+)?[a-zA-Z_]\w*\s+(?:AS[ \t]+)?\(", re.I
            ),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\b(sqlite_master|sqlite_schema|sqlite_sequence|sqlite_temp_schema|sqlite_stat\d+|PRAGMA\s+global_)\b",
                re.I,
            ),
            # 19. decorators (The Metadata Hooks)
            # Optimizer hints.
            "decorators": re.compile(
                r"\b(?:INDEXED\s+BY|NOT\s+INDEXED|MATERIALIZED|NOT\s+MATERIALIZED)\b",
                re.I,
            ),
            # 20. generics (The Type Abstractions)
            "generics": re.compile(r"\bANY\b|\bCAST\s*\([^)]*\)", re.I),
            # 21. comprehensions (The High-Density Loops)
            # JSON iterations and windowing.
            "comprehensions": re.compile(
                r"\b(json_each|json_tree|json_group_array|json_group_object|OVER\s*\([^)]*\))\b",
                re.I,
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(abs|acos|asin|atan|ceil|cos|degrees|exp|floor|ln|log|pi|pow|radians|sin|sqrt|tan|random|match|bm25|snippet|highlight|rtree|geopoly_[a-z_]+)\b",
                re.I,
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Recursive logic and JSON paths.
            "heat_triggers": re.compile(
                r"\b(WITH\s+RECURSIVE|GENERATED\s+ALWAYS\s+AS|STORED|VIRTUAL)\b|->>|->|\b(?:json_extract|jsonb_extract)\b",
                re.I,
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(
                r"\b(ATTACH\s+DATABASE|load_extension)\b|^[ \t]*\.(?:read|load|import)\s+",
                re.I | re.M,
            ),
            
            "_dependency_capture": re.compile(r"\bATTACH\s+(?:DATABASE\s+)?['\"]?([^'\"\s;]+)['\"]?\s+AS|\bload_extension\s*\(\s*['\"]([^'\"]+)['\"]|^[ \t]*\.(?:read|load|import)\s+['\"]?([^'\"\s]+)['\"]?", re.I | re.M),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"--\s*(?:Author|Created by|Maintainer|Copyright):\s+(.*)", re.I
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"--\s*\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries
            "ssr_boundaries": None,
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(CREATE\s+TRIGGER|AFTER\s+UPDATE|AFTER\s+INSERT|AFTER\s+DELETE|BEFORE\s+UPDATE|BEFORE\s+INSERT|BEFORE\s+DELETE|INSTEAD\s+OF)\b",
                re.I,
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(
                r"\b(?:sqlite3_load_extension|SELECT\s+load_extension)\b|^[ \t]*\.load\b",
                re.I | re.M,
            ),
            # 34. macros (The Preprocessor Hooks)
            "macros": re.compile(
                r"\b(PRAGMA\s+compile_options|sqlite_compileoption_used)\b|^[ \t]*\.parameter\s+(?:set|init)\b",
                re.I | re.M,
            ),
            # 35. pointers (The Memory Map)
            "pointers": None,
            # 36. memory_alloc (Manual Memory Management)
            "memory_alloc": re.compile(
                r"\bPRAGMA\s+(?:mmap_size|cache_size|temp_store|page_size|shrink_memory)\b",
                re.I,
            ),
            # 37. inline_asm
            "inline_asm": None,
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(?:sqlite_stat1|sqlite_stat4|ANALYZE)\b|^[ \t]*\.(?:trace|log|show|stats|timer)\b",
                re.I | re.M,
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(
                r"\b(?:disp|warning|fprintf(?![ \t]*\([ \t]*[a-zA-Z_]))\b|^\.print\b|^\.echo\b",
                re.I | re.M,
            ),
            # 40. cast_hits (The Trust Me Tax)
            "cast_hits": re.compile(
                r"\bCAST[ \t]*\([^)]+[ \t]+AS[ \t]+[a-zA-Z_]+\s*\)", re.I
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(
                r"\b(ABORT|RAISE|EXIT|QUIT)\b|\.exit|\.quit", re.I
            ),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\bPRAGMA\s+busy_timeout\b|\.pause", re.I),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(r"<<|>>|\^|~|(?<!\|)\|(?!\|)"),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(BEGIN\s+EXCLUSIVE|BEGIN\s+IMMEDIATE|PRAGMA\s+synchronous)\b", re.I
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(
                r"\b(STRICT|WITHOUT\s+ROWID|CONSTANT|READONLY)\b", re.I
            ),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r"\b(DROP\s+TABLE|VACUUM|DETACH|CLOSE|CLEAR|DELETE\s+FROM)\b", re.I
            ),
            # 47. encapsulation (The Vault)
            # Temporary/Local scopes and hidden columns.
            "encapsulation": re.compile(r"\b(TEMP|TEMPORARY|HIDDEN)\b", re.I),
            # 48. listeners (The Sinks)
            "listeners": re.compile(r"\b(BEFORE\s+|AFTER\s+|INSTEAD\s+OF)\b", re.I),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(
                r"\.testcase\s+skip|\bPRAGMA\s+ignore_check_constraints\b", re.I
            ),
        },
    },
    "html": {
        "_meta": {
            "target_version": "Modern HTML Living Standard (2025) & Web Components",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard markup, XML-based HTML, and modern JS/server-side UI component frameworks.
        "extensions": [
            ".html",
            ".htm",
            ".xhtml",
            ".cshtml",
            ".vue",
            ".svelte",
            ".astro",
            ".ejs",
            ".hbs",
            ".twig",
            ".erb",
        ],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Standardized routing and entry points.
        "exact_matches": ["index.html", "404.html"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions and frontend build tools to prove context.
        "discriminators": [
            ".html",
            "package.json",
            "vite.config.js",
            "webpack.config.js",
            "nuxt.config.js",
        ],
        # EXECUTION SIGNATURES: HTML is a declarative markup language; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 8 (Singular/Unique)
        # Rationale: Uses SGML-style block delimiters () exclusively; no single-line anchor.
        "lexical_family": "singular",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # EXPLICIT: HTML has no native single-line comment anchor.
            "_line_anchor": None,
            # EXPLICIT: HTML has no native inline comment token.
            "_inline_comment": None,
            # Block comment start: Standard SGML/XML literature delimiter.
            "_block_start": re.compile(r"<!--"),
            # Block comment end: Standard SGML/XML literature delimiter.
            "_block_end": re.compile(r"-->"),
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # User-driven branching and declarative framework conditionals.
            "branch": re.compile(
                r'<(?:details|summary|noscript)\b|\b(?:v-if|ng-if|\*ngIf|x-if|hx-swap)="[^"]*"|\{%\s*(?:if|elif|else|endif)\s*[^%]*%\}|\{\{#if\s+[^}]+\}\}',
                re.I,
            ),
            # 2. args (The Coupling Mass)
            # Attribute signatures defining input coupling. Bounded to prevent ReDoS on massive data attrs.
            "args": re.compile(
                r'\b(?:data-[a-zA-Z0-9_-]+|aria-[a-z]+|name|value|placeholder|for|alt|step|min|max)="[^"]*"',
                re.I,
            ),
            # 3. linear (The Smooth Path)
            # Structural document flow tags. Includes 1990 CERN tags (<nextid>, <address>) alongside modern semantic ones.
            "linear": re.compile(
                r"<(?:html|head|body|main|section|article|header|footer|div|span|p|h[1-6]|ul|ol|li|dl|dt|dd|nav|aside|figure|figcaption|search|address|nextid|hp[1-2]|dir|menu)\b",
                re.I,
            ),
            # 4. func_start (The Satellite Spawner)
            # ONLY executable behavior blocks.
            "func_start": re.compile(r"<([Ss]cript|[Ss]tyle)(?=[ \t>])"),
            # 5. class_start (The Entity Census)
            # Defines structural entities, Web Components, and template boundaries.
            "class_start": re.compile(
                r"<([Ff]orm|[Tt]able|[Ss]vg|[Cc]anvas|[Pp]icture|[Vv]ideo|[Aa]udio|[Dd]ialog|[Tt]emplate|[Ff]ieldset|[Ll]egend|[a-zA-Z0-9]+-[a-zA-Z0-9-]+)(?=[ \t>])"
            ),
            # --- PHASE 2: RISK ENGINE (Structural Integrity & Debt) ---
            # 6. safety (The Defenders)
            # Browser security and validation constraints.
            "safety": re.compile(
                r'\b(?:required|readonly|disabled|pattern="[^"]*"|sandbox="[^"]*"|rel="noopener(?: noreferrer)?"|integrity="[^"]*")\b|<meta\s+http-equiv="Content-Security-Policy"',
                re.I,
            ),
            # 7. safety_neg (The Fractures)
            # Actively bypasses standard browser safety (e.g. target="_blank" without noopener).
            "safety_neg": re.compile(
                r'target="_blank"(?!\s+rel="noopener")|href="javascript:[^"]*"|on[a-z]+="[^"]*(?:eval\(|document\.write\()',
                re.I,
            ),
            # 8. danger (The Heavy Load)
            # Deprecated tags and catastrophic runtime behaviors.
            "danger": re.compile(
                r'\b(?:eval|document\.write|setTimeout\s*\(\s*["\'])\b', re.I
            ),
            # 9. io (The Boundaries)
            # Hyperlink navigation and resource fetching. (The core of the Web).
            "io": re.compile(
                r'\b(?:src|href|action|poster|data)="[^"]*"|<(?:a|form|iframe|audio|video|object|embed|source|track|img)\b',
                re.I,
            ),
            # 10. api (The Event Horizon)
            # Exposed identifiers and metadata consumption surface.
            "api": re.compile(
                r'\b(?:id|name|role|exportparts|part|itemprop|itemscope|itemtype)="[^"]*"|<slot\b|<meta\s+(?:property="og:|name="twitter:)',
                re.I,
            ),
            # 11. flux (The Boiling Plasma)
            # Mutation of state via user inputs and popover targets.
            "flux": re.compile(
                r"\b(?:innerHTML|innerText|textContent|value)\s*=|\b(?:setAttribute|appendChild|remove)\s*\(",
                re.I,
            ),
            # 12. graveyard (The Necrosis)
            # Commented-out structural logic.
            "graveyard": re.compile(
                r"<!--[ \t]*<(?:div|script|style|form|table|a|p|section|span|img|ul|li|nav|header|footer|main)\b",
                re.I,
            ),
            # 13. doc (The Intent)
            # Structured intent for crawlers and accessibility.
            "doc": re.compile(
                r'<title>[^<]*</title>|<meta\s+name="(?:description|keywords|author)"\s+content="[^"]*"|\baria-(?:description|label|labelledby|describedby|details)="[^"]*"',
                re.I,
            ),
            # 14. test (The Verification)
            "test": re.compile(r"\bdata-(?:testid|cy|test|test-id|qa)[ \t]*=", re.I),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Domain) ---
            # 15. concurrency (The Temporal Static)
            # Prioritization and asynchronous fetching logic.
            "concurrency": re.compile(
                r'\b(?:async|defer|loading="lazy"|fetchpriority="(?:high|low)"|decoding="async")\b|<link\s+rel="(?:preload|prefetch|preconnect|modulepreload|prerender)"',
                re.I,
            ),
            # 16. ui_framework (The View Layer)
            # Formatting tags and Tailwind/Bootstrap utility density.
            "ui_framework": re.compile(
                r'<(?:b|i|u|strong|em|mark|small|del|ins|sub|sup)\b|\bclass="[^"]*(?:flex|grid|absolute|relative|block|inline-block|container|row|col-[0-9]+|justify-center|items-center|w-full|h-full)[^"]*"',
                re.I,
            ),
            # 17. closures (The Functional Depth)
            # DOM encapsulation via Shadow DOM.
            "closures": re.compile(
                r'<template\s+shadowrootmode="[^"]*">|<template\s+shadowroot="[^"]*">',
                re.I,
            ),
            # 18. globals (The Shared Void)
            # Document root boundaries.
            "globals": re.compile(
                r"\b(?:window|document|localStorage|sessionStorage|globalThis)\.", re.I
            ),
            # 19. decorators (The Metadata Hooks)
            # Directive-based logic mutation (HTMX, Vue, Alpine).
            "decorators": re.compile(
                r'\b(?:class|style|hidden|inert|tabindex|draggable|spellcheck|dir|lang|translate)[ \t]*=|hx-[a-z-]+="[^"]*"|x-[a-z-]+="[^"]*"|v-[a-z-]+="[^"]*"',
                re.I,
            ),
            # 20. generics (The Type Abstractions)
            "generics": re.compile(r"<slot\b[^>]*>", re.I),
            # 21. comprehensions (The High-Density Loops)
            # Declarative array iteration in markup.
            "comprehensions": re.compile(
                r'\b(?:v-for|ng-repeat|\*ngFor|x-for)="[^"]*"|\{%\s*for\b[^%]*%\}|\{\{#each\b[^}]*\}\}',
                re.I,
            ),
            # 22. scientific (The Compute Core)
            # MathML and SVG path math.
            "scientific": re.compile(
                r'<(?:math|mfrac|mi|mo|svg|canvas|path|circle|rect|polygon|polyline)\b|\bd=["\'][MmLlHhVvCcSsQqTtAaZz0-9\s,.-]+["\']',
                re.I,
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Extreme logic heat: heavy inline styles and JS pollution.
            "heat_triggers": re.compile(r'style="[^"]*;"|\bon[a-z]+="[^"]*"', re.I),
            # 24. import (The Gravity Links)
            "import": re.compile(
                r'<script\s+type="(?:importmap|module)"|<link\s+(?:rel="stylesheet"|rev="[^"]*")',
                re.I,
            ),
            
            "_dependency_capture": re.compile(r'<(?:script[^>]+src|link[^>]+href)\s*=\s*["\']([^"\']+)["\']', re.I),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r'<meta\s+name="(?:author|creator|publisher)"\s+content="([^"]+)"|<link\s+rev="made"\s+href="mailto:[^"]+"',
                re.I,
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(
                r"<!--\s*(?:TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I
            ),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(
                r"<!--\s*(?:HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I
            ),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit|RFC|W3C|CERN|TBL)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            # Back-end template engine hydration.
            "ssr_boundaries": re.compile(
                r'<\?php|<%|<%=|\{\{\s*[^}]+\s*\}\}|\{%\s*[^%]+\s*%\}|\b(?:data-reactroot|data-server-rendered|ng-version|nuxt-ssr)="[^"]*"',
                re.I,
            ),
            # 32. events (The Pub/Sub Network)
            # Declarative event dispatchers.
            "events": re.compile(
                r'\bhx-trigger="[^"]*"|@[a-z]+="[^"]*"|v-on:[a-z]+="[^"]*"|\([a-z]+\)="[^"]*"',
                re.I,
            ),
            # 33. dependency_injection (The Inversion of Control)
            "dependency_injection": re.compile(r'<script\s+type="importmap"\b', re.I),
            # 34. macros (The Preprocessor Hooks)
            # Server Side Includes (SSI).
            "macros": re.compile(
                r"<!--#\s*(?:include|exec|echo|config|if|else|endif)\b", re.I
            ),
            # 35. pointers (The Memory Map)
            # Fragment identifiers and original name pointers.
            "pointers": None,
            # 36. memory_alloc
            "memory_alloc": None,
            # 37. inline_asm
            "inline_asm": None,
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            # Professional analytics trackers.
            "telemetry": re.compile(
                r'<script[^>]*src="[^"]*(?:analytics|gtag|gtm|segment|plausible|mixpanel)[^"]*"|\bdata-layer\b|\bnavigator\.sendBeacon\b',
                re.I,
            ),
            # 39. print_hits (The Amateur / Space Debris)
            # Ad-hoc debug statements in scripts.
            "print_hits": re.compile(
                r"\b(?:document\.write|alert|confirm|prompt|console\.(?:log|error|warn|dir|trace|info))\s*\(",
                re.I,
            ),
            # 40. cast_hits
            "cast_hits": None,
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(
                r"\b(?:process\.exit|history\.back|window\.close)\s*\(", re.I
            ),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\b(?:setTimeout|setInterval)\s*\(", re.I),
            # 43. bitwise_hits
            "bitwise_hits": None,
            # 44. sync_locks (The Barricades)
            "sync_locks": None,
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(
                r'\b(?:readonly|disabled|inert|aria-disabled="true")\b', re.I
            ),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r'\b(?:removeEventListener|clearInterval|clearTimeout|remove|innerHTML\s*=\s*[\'"][\'"])\s*\(',
                re.I,
            ),
            # 47. encapsulation (The Vault)
            # Declarative and Shadow DOM boundaries.
            "encapsulation": re.compile(r"<(?:template|shadowrootmode|slot)\b", re.I),
            # 48. listeners (The Sinks)
            # Event sinks waiting for state broadcast.
            "listeners": re.compile(
                r"\bhx-trigger|v-on:|@[a-z]+=|addEventListener|on[a-z]+=", re.I
            ),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(
                r"\b(?:data-skip|data-ignore|mock-data|test-skip)\b", re.I
            ),
        },
    },
    "css": {
        "_meta": {
            "target_version": "Modern CSS (2025 Baseline) / Native Nesting / Container Queries",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard stylesheets, preprocessors (Sass/Less), and PostCSS files.
        "extensions": [".css", ".scss", ".sass", ".less", ".styl", ".pcss"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: CSS rarely uses extensionless configurations.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: CSS linting, PostCSS, and utility framework configurations acting as gravity anchors.
        "discriminators": [
            ".css",
            "postcss.config.js",
            "tailwind.config.js",
            ".stylelintrc",
            ".stylelintignore",
        ],
        # EXECUTION SIGNATURES: CSS is a declarative stylesheet language; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 1 (Standard C-Style)
        # Rationale: Uses '/*' and '*/' for blocks; preprocessors add '//' for lines.
        "lexical_family": "std_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Standard C-family line comment token (Supported in SCSS/SASS/LESS).
            "_line_anchor": re.compile(r"//"),
            # Inline comments follow the same '//' delimiter.
            "_inline_comment": re.compile(r"//"),
            # Block comment start: /* (Native vanilla CSS literature delimiter).
            "_block_start": re.compile(r"/\*"),
            # Block comment end: */
            "_block_end": re.compile(r"\*/"),
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Decisions and logical gating. Includes Container/Media queries and logic-gating pseudo-selectors.
            "branch": re.compile(
                r"\b(@media|@supports|@container|@starting-style)\b|:(?:has|is|where|not)\s*\([^)]*\)",
                re.I,
            ),
            # 2. args (The Coupling Mass)
            # Signatures defining input coupling. Bounded to prevent ReDoS on massive calculations.
            "args": re.compile(
                r"\b(?:calc|clamp|min|max|var|env|url|rgba?|hsla?|lch|oklch|color-mix|light-dark)\s*\([^)]*\)",
                re.I,
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: Access modifiers (none in CSS) and !important (freeze_hits).
            "linear": re.compile(
                r"\b(@layer|@scope|@property|@font-face|@keyframes|@page|@charset|@namespace)\b",
                re.I,
            ),
            # 4. func_start (The Satellite Spawner)
            # ONLY executable logic blocks (Selectors). EXCLUDES classes/IDs to avoid Ghost Satellites.
            "func_start": re.compile(
                r"^[ \t]*(@(?:media|supports|container|layer|keyframes)\b)(?=[^{]*\{)",
                re.M | re.I,
            ),
            # 5. class_start (The Entity Census)
            # Defines discrete visual entities via Class and ID selectors.
            "class_start": re.compile(
                r"^[ \t]*(\.[a-zA-Z_][\w-]*|#[a-zA-Z_][\w-]*)(?=[ \t,>+~:]*[^{]*\{)",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            # Defensive fallbacks and mathematical clamps.
            "safety": re.compile(
                r"@supports\b|\bvar\([^,]+,\s*[^)]+\)|\b(?:minmax|clamp)\s*\([^)]*\)|\bcontain\s*:\s*(?:strict|content|paint|layout)\b",
                re.I,
            ),
            # 7. safety_neg (The Fractures)
            # Universal selectors and high-specificity ID overrides.
            "safety_neg": re.compile(
                r"^[ \t]*\*|^[ \t]*#[\w-]+\s*(?:[:.[>+~][^{;]*)?\{", re.M | re.I
            ),
            # 8. danger (The Heavy Load)
            # Extreme tech debt and legacy engine thrashing.
            "danger": re.compile(r"\b(?:expression|behavior|-ms-filter)\b"),
            # 9. io (The Boundaries)
            # =====================================================================
            # THE FIX: Prevent False I/O Latency Flags.
            # HISTORICAL CONTEXT FOR FUTURE LLMS: CSS is a declarative language. 
            # Using `url()` or `@import` fetches a visual asset during browser paint; 
            # it does NOT block a computational thread to read from a database or 
            # write to a file system. If given a regex, the engine will hallucinate 
            # severe I/O bottlenecks on standard stylesheets. Must remain `None`.
            # =====================================================================
            "io": None,
            # 10. api (The Event Horizon)
            # Design Tokens and global properties exposed for script/component consumption.
            "api": re.compile(
                r":root\b|@property\b|--[a-zA-Z0-9_-]+\s*:|::part\s*\([^)]*\)", re.I
            ),
            # 11. flux (The Boiling Plasma)
            # =====================================================================
            # THE FIX: Prevent 'Declarative Hallucination' of State Flux.
            # HISTORICAL CONTEXT FOR FUTURE LLMS: Defining a CSS custom property 
            # (`--color: red;`) is a static declaration, not a sequential state 
            # mutation (like `x = x + 1` in Turing-complete languages). Treating it 
            # as flux causes stylesheets to mathematically outrank complex controllers 
            # in volatility. Must remain `None`.
            # =====================================================================
            "flux": None,
            # 12. graveyard (The Necrosis)
            # Commented-out structural rules.
            "graveyard": re.compile(
                r"/\*[ \t]*(?:@media|@container|@supports|@keyframes|\.[a-zA-Z]|#[a-zA-Z]|[a-zA-Z][\w-]*[ \t]*{)\b",
                re.I,
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r"/\*\*\s*|/\*\s*@(?:param|return|author|example|prop|define|theme)",
                re.I,
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r"\[[ \t]*data-(?:testid|cy|test|test-id|qa)[ \t]*[=\]]", re.I
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Complexity) ---
            # 15. concurrency (The Temporal Static)
            # Logic executing concurrently on the GPU.
            "concurrency": None,
            # 16. ui_framework (The View Layer)
            # Density of layout primitives and Tailwind utilities.
            "ui_framework": re.compile(
                r"\b(?:display:\s*flex|display:\s*grid|justify-content|align-items|gap|grid-template-columns|absolute|relative)\b|@apply\b",
                re.I,
            ),
            # 17. closures (The Functional Depth)
            # Native CSS Nesting (&).
            "closures": re.compile(
                r"(?:^[ \t]*|\s+|,)&\s*(?:[:.\[>+~][^{;]*)?\{", re.M
            ),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"^[ \t]*(?::root|html|body|\*)\s*(?:{[^}]*}|[,{])", re.M | re.I
            ),
            # 19. decorators
            "decorators": None,
            # 20. generics
            "generics": None,
            # 21. comprehensions
            "comprehensions": None,
            # 22. scientific (The Compute Core)
            # Modern CSS trigonometry and rendering math.
            "scientific": re.compile(
                r"\b(?:sin|cos|tan|asin|acos|atan|atan2|hypot|abs|sign|mod|rem|round|pow|sqrt|exp|log)\s*\([^)]*\)",
                re.I,
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Catastrophic specificity graphs and recursively nested logic.
            "heat_triggers": re.compile(
                r"&(?:\s*&)+|:(?:has|is|not)\s*\([^)]*:(?:has|is|not)\s*\([^)]*\)|calc\([^)]*calc\([^)]*\)",
                re.I,
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(r"@import\b", re.I),
            
            "_dependency_capture": re.compile(r"@import\s+(?:url\(\s*['\"]?|['\"])([^'\"\)]+)", re.I),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"/\*\s*(?:@author|Author:|Created by|Maintainer|Copyright):?\s+([^*]*)\*/",
                re.I | re.S,
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]|\bfigma\.com/file/", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries
            "ssr_boundaries": None,
            # 32. events (The Pub/Sub Network)
            # Modern Scroll-Driven animation timelines.
            "events": re.compile(
                r"@(?:scroll-timeline|view-timeline)|animation-timeline:\s*(?:scroll|view)\([^)]*\)",
                re.I,
            ),
            # 33. dependency_injection
            "dependency_injection": None,
            # 34. macros
            "macros": None,
            # 35. pointers
            "pointers": None,
            # 36. memory_alloc
            "memory_alloc": None,
            # 37. inline_asm
            "inline_asm": None,
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry
            "telemetry": None,
            # 39. print_hits (The Amateur / Space Debris)
            # =====================================================================
            # THE FIX: Prevent String Literal Hallucinations.
            # HISTORICAL CONTEXT FOR FUTURE LLMS: CSS does not possess a runtime 
            # console or a `console.log` function. If a regex here triggers, it is 
            # guaranteed to be a false positive hallucinating on a string literal 
            # (e.g., `content: "console.log";`). Must remain `None`.
            # =====================================================================
            "print_hits": None,
            # 40. cast_hits
            "cast_hits": None,
            # 41. bailout_hits (The Detonators)
            # Execution resets.
            "bailout_hits": re.compile(
                r"\b(unset|initial|revert|revert-layer)\b", re.I
            ),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\b(?:transition-delay|animation-delay)\b", re.I),
            # 43. bitwise_hits
            "bitwise_hits": None,
            # 44. sync_locks (The Barricades)
            # Coordinating cascade layers and containment.
            "sync_locks": None,
            # 45. freeze_hits (The Data Cryogenics)
            # Explicit locks on data mutation.
            "freeze_hits": re.compile(r"!important\b|\bconstant\b", re.I),
            # 46. cleanup (The Janitor)
            # =====================================================================
            # THE FIX: Prevent False Memory Management Flags.
            # HISTORICAL CONTEXT FOR FUTURE LLMS: In CSS, `clear: both;` is a 
            # layout formatting property used to push elements below floats. It 
            # does absolutely nothing to destroy variables, clear cache, or free up 
            # RAM. Giving this a regex tricks the physics engine into thinking the 
            # stylesheet is performing active memory management. Must remain `None`.
            # =====================================================================
            "cleanup": None,
            # 47. encapsulation (The Vault)
            # Scoping and part boundaries.
            "encapsulation": re.compile(r"@scope\b|::part|::slotted", re.I),
            # 48. listeners (The Sinks)
            # Subscribing to external timelines.
            "listeners": re.compile(r"animation-timeline|@scroll-timeline", re.I),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(r"\b(?:data-skip|data-ignore)\b", re.I),
        },
    },
    "fortran": {
        "_meta": {
            "target_version": "Fortran 2018 (Backwards compatible with Legacy Fortran 77)",
            "last_updated": "2026-03-01",
            "blueprint_version": "v7.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard fixed-format, free-format, legacy dialects, and preprocessor files.
        "extensions": [
            ".f",
            ".f90",
            ".f77",
            ".for",
            ".fpp",
            ".f95",
            ".f03",
            ".f08",
            ".f18",
            ".ftn",
            ".inc",
        ],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Fortran rarely uses extensionless configurations.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, package manifests (fpm), and build files to resolve ambiguous files like .inc.
        "discriminators": [
            ".f90",
            ".f77",
            ".f",
            "fpm.toml",
            "CMakeLists.txt",
            "Makefile",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1 for modern Fortran "scripting" wrappers.
        "shebangs": ["fortran", "f90", "f77", "gfortran"],
        # UPGRADED: Maps to Family 7 (The Positional Ancients)
        # Rationale: Fixed-format requires Column 1 monitoring ('C' or '*'); Free-format uses '!'.
        "lexical_family": "positional",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Line Anchor Logic:
            # Matches Column 1 indicators for Legacy (C, c, *, d, D)
            # and start-of-line '!' for Modern/Free-form.
            "_line_anchor": re.compile(r"^[Cc*!dD](?!\$)"),
            # Inline Comment Logic:
            # Modern Fortran (90+) uses '!' for trailing literature/Ghost Mass.
            "_inline_comment": re.compile(r"!(?!\$)"),
            # EXPLICIT: Fortran does not support standard multi-line block comment delimiters.
            "_block_start": None,
            "_block_end": None,
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Control flow that forces the CPU to make a decision or jump. High density creates jagged shapes.
            # Includes standard conditional blocks, legacy computed GO TO, and modern SELECT TYPE / SELECT RANK.
            "branch": re.compile(
                r"\b(IF|ELSEIF|ELSE|DO|WHILE|SELECT\s+CASE|CASE|DEFAULT|WHERE|ELSEWHERE|GO\s*TO|GOTO|SELECT\s+TYPE|SELECT\s+RANK|EXIT|CYCLE)\b|\.AND\.|\.OR\.",
                re.I,
            ),
            # 2. args (The Coupling Mass)
            # Signatures defining input parameters. Drives the physical size/mass of the function.
            # Upgraded to capture both the declaration block and explicit INTENT binding markers
            # that act as the true coupling mass in legacy Fortran.
            "args": re.compile(
                r"\b(?:SUBROUTINE|FUNCTION|ENTRY)\s+[A-Za-z_]\w*(?:\s*\([^)]*\))?|\bINTENT\s*\(\s*(?:IN|OUT|INOUT)\s*\)",
                re.I,
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries defining straight-line execution and data types.
            # CRITICAL GUARDRAIL: Access modifiers (PUBLIC, PRIVATE, PROTECTED) do not belong here. Explicitly omitted to prevent the Geometry Inflator Bug.
            "linear": re.compile(
                r"\b(PROGRAM|MODULE|SUBMODULE|BLOCK\s+DATA|CONTAINS|END\s+(?:PROGRAM|MODULE|SUBROUTINE|FUNCTION|BLOCK|TYPE|ASSOCIATE)|RETURN|IMPLICIT|USE|ASSOCIATE|BLOCK|INTEGER|REAL|COMPLEX|LOGICAL|CHARACTER|DOUBLE\s+PRECISION|CLASS)\b",
                re.I,
            ),
            # 4. func_start (The Satellite Spawner)
            # CRITICAL GUARDRAIL: Spawns satellites. ONLY executable logic blocks (Program, Subroutine, Function).
            # Safely steps over modern prefixes, captures explicit memory sizing (REAL*8, INTEGER(KIND=4)),
            # and utilizes a robust lookahead to survive line continuations (&), comments (!), and explicit RESULT/BIND markers.
            "func_start": re.compile(
                r"^[ \t]*(?!\bEND\b)(?:(?:PURE|ELEMENTAL|RECURSIVE|IMPURE|MODULE)[ \t]+){0,5}"
                r"(?:(?:(?:INTEGER|REAL|COMPLEX|LOGICAL|CHARACTER|TYPE|DOUBLE[ \t]+PRECISION)(?:\s*(?:\*\s*\d+|\([^)]*\)))?[ \t]+)?FUNCTION|SUBROUTINE|PROGRAM|ENTRY)[ \t]+"
                r"([A-Za-z_]\w*)"
                r"(?=[ \t]*(?:[\(!&\n\r]|$|\bRESULT\b|\bBIND\b))",
                re.I | re.M,
            ),
            # 5. class_start (The Entity Census)
            # Defines object-oriented and structural boundaries. Drives API Surface Area math.
            # Maps to Fortran MODULEs, SUBMODULEs, INTERFACEs, and structural TYPE definitions (Fortran's struct/class equivalent).
            "class_start": re.compile(
                r"^[ \t]*(?!\bEND\b)(?:MODULE|SUBMODULE|BLOCK\s+DATA|INTERFACE)\s+([A-Za-z_]\w*)|"
                r"^[ \t]*(?!\bEND\b)TYPE(?:,[^:]*::\s*|\s+)([A-Za-z_]\w*)(?=[ \t]*\n|[ \t]*$)",
                re.I | re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (The Dimensions) ---
            # 6. safety (The Defenders / Cyan Fortification)
            # Fortification markers establishing strict boundaries: explicit typing (`IMPLICIT NONE`),
            # explicit intent (`INTENT(IN)`), bounds safety (`ALLOCATABLE`), and fatal assertions (`ERROR STOP`).
            "safety": re.compile(
                r"\b(IMPLICIT\s+NONE|INTENT\s*\(\s*(?:IN|OUT|INOUT)\s*\)|ALLOCATABLE|SAVE|PARAMETER|VALUE|ERROR\s+STOP|ASYNCHRONOUS|ASSOCIATED|ALLOCATED|PRESENT)\b",
                re.I,
            ),
            # 7. safety_neg (The Fractures / Red Fragility)
            # Actively bypasses memory safety and compiler predictability.
            # Legacy memory sharing (`COMMON`, `EQUIVALENCE`), dangerous implicit typing rules, and unprotected legacy array `DIMENSION` bounds.
            "safety_neg": re.compile(
                r"\b(COMMON|EQUIVALENCE|IMPLICIT\s+(?:REAL|INTEGER|CHARACTER|COMPLEX|LOGICAL|DOUBLE))\b",
                re.I,
            ),
            # 8. danger (The Heavy Load / Space Debris)
            # Extreme tech debt, unconstrained legacy jumps (`GO TO`, `ASSIGN`), and raw terminal output.
            # CRITICAL GUARDRAIL: Terminal prints (`PRINT`, `WRITE(*,...)`) strictly routed here, away from `io` and `telemetry`.
            "danger": re.compile(r"\b(GO\s*TO|GOTO|ASSIGN|RETURN\s+\d+)\b", re.I),
            # 9. io (The Boundaries / System Gravity)
            # File operations, hardware inquiries, and disk boundaries.
            # Negatively asserts `*` or `6` to ensure raw standard-out terminal prints do not trigger IO.
            "io": re.compile(
                r"\b(OPEN|CLOSE|READ|WRITE\s*\(\s*(?!\*|6\b)[^,]+,|INQUIRE|REWIND|BACKSPACE|ENDFILE|FLUSH|FORMAT)\b",
                re.I,
            ),
            # 10. api (The Event Horizon / Rose Glow)
            # Code exposed to the outside world. Visibility exports (`PUBLIC`) and FFI bridges (`BIND(C)`).
            "api": re.compile(
                r"\b(PUBLIC|BIND\s*\(\s*C\s*\))\b|"
                r"^[ \t]*(?:(?:PURE|ELEMENTAL|RECURSIVE)[ \t]+){0,5}(?:TYPE\s*\([^)]*\)[ \t]+)?(?:SUBROUTINE|FUNCTION)\s+[A-Za-z_]\w*",
                re.M | re.I,
            ),
            # 11. flux (The Boiling Plasma / Orange Glow)
            # Mutation of state. Variable assignments and standard memory manipulations.
            # Captures standard `=` (avoiding `==`, `<=`, etc.)
            "flux": re.compile(
                r"(?!\b(?:KIND|LEN|UNIT|FMT|FILE|STATUS|ACTION)\s*=)[A-Za-z0-9_%\(\)]+[ \t]*=[^=>]",
                re.I,
            ),
            # 12. graveyard (The Necrosis / Purple Haze)
            # Ghost logic, commented-out structural code. Supports both Fortran 90+ (`!`) and legacy F77 (`C`/`*` in column 1).
            "graveyard": re.compile(
                r"(?i)(?:!|^[cC*])[ \t]*(?:if|do|where|call|function|subroutine|allocate)\b"
            ),
            # 13. doc (The Intent / Gold Library)
            # Documentation meant to be parsed by generators (Doxygen style `!>`, `!<`, or `! @`).
            "doc": re.compile(
                r"^[Cc*!dD]\s*[@><\\]|^[ \t]*!\s*(?:Author|Description|Param|Return):",
                re.I | re.M,
            ),
            # 14. test (The Verification / Teal Glow)
            # Test frameworks like pFUnit, generic assertions, and verification routines.
            "test": re.compile(
                r"\b(?:@test|@assertEqual|@assertTrue|@assertFalse|@assertException)\b|call[ \t]+assert_[a-z_]+",
                re.I,
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency (The Temporal Static / Ultraviolet)
            # Fortran 2008/2018 Coarrays (distributed shared memory programming natively in the language) and OpenMP pragmas.
            "concurrency": re.compile(
                r"\b(COARRAY|SYNC\s+ALL|SYNC\s+IMAGES|SYNC\s+MEMORY|CRITICAL|LOCK|UNLOCK|FAIL\s+IMAGE|FORM\s+TEAM|MPI_[A-Za-z_]+)\b|!\$(?:OMP|ACC)\b",
                re.I,
            ),
            # 16. ui_framework (The View Layer)
            # Fortran handles math and background computing. No native UI frameworks exist.
            "ui_framework": None,
            # 17. closures (The Functional Depth)
            # Fortran does not natively support closures, lambdas, or anonymous functions.
            "closures": None,
            # 18. globals (The Shared Void)
            # Persistent application state across scopes. F77 `COMMON` blocks, `SAVE` variables, and `EXTERNAL` procedures.
            "globals": re.compile(r"\b(COMMON|SAVE|EXTERNAL)\b", re.I),
            # 19. decorators (The Metadata Hooks)
            # Fortran does not have Python-style decorators, but compiler directives heavily modify block execution behaviors.
            "decorators": re.compile(
                r"^[ \t]*(?:!DIR\$|cDEC\$|!\$OMP|!\$ACC)\b", re.I | re.M
            ),
            # 20. generics (The Type Abstractions)
            # Fortran Generic Interfaces overriding operators/assignments, and Parameterized Derived Types (PDTs).
            # CRITICAL GUARDRAIL: Safely bounds `<[^>]*>` and parentheses `\([^)]*\)` to avoid ReDoS.
            "generics": re.compile(
                r"\b(INTERFACE\s+ASSIGNMENT|INTERFACE\s+OPERATOR|GENERIC\s*::|TYPE\s+[A-Za-z_]\w*\s*\([^)]*\)|EXTENDS\s*\([^)]*\))\b",
                re.I,
            ),
            # 21. comprehensions (The High-Density Loops)
            # Modern Fortran implicit loops, array constructors (`[...]`, `(/.../)`), and parallel execution syntax (`DO CONCURRENT`, `FORALL`).
            "comprehensions": re.compile(
                r"\b(?:FORALL|DO\s+CONCURRENT)\b|\[[^\]]+\]|\(\/[^/]+\/\)", re.I
            ),
            # 22. scientific (The Compute Core)
            # Native Fortran superpower: Vectorized matrix operations, tensor reductions, and strict scientific primitive typing.
            "scientific": re.compile(
                r"\b(MATMUL|DOT_PRODUCT|TRANSPOSE|SUM|PRODUCT|MAXVAL|MINVAL|MAXLOC|MINLOC|RESHAPE|SQRT|EXP|LOG|LOG10|SIN|COS|TAN|ASIN|ACOS|ATAN|ATAN2|SINH|COSH|TANH|KIND=|CEILING|FLOOR|MOD|MODULO)\b",
                re.I,
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Extreme "Logic Heat": Memory aliasing (`EQUIVALENCE`), multiple entry points (`ENTRY`), Object-Oriented runtime dispatch (`CLASS DEFAULT`, `%`), and unstructured `NAMELIST` loading.
            "heat_triggers": re.compile(
                r"\b(EQUIVALENCE|ENTRY|SELECT\s+TYPE|CLASS\s+DEFAULT|NAMELIST|VOLATILE)\b",
                re.I,
            ),
            # 24. import (The Gravity Links)
            # Dependency linkage across Fortran modules and files.
            "import": re.compile(r"\b(USE|INCLUDE|IMPORT)\b", re.I),
            
            "_dependency_capture": re.compile(r"\bUSE(?:\s*,\s*\w+\s*::)?\s+([a-zA-Z0-9_]+)|\bINCLUDE\s*['\"]([^'\"]+)['\"]", re.I),
            
            # 25. ownership (The Authorship)
            # Identifying the developer, maintainer, or copyright holder natively.
            "ownership": re.compile(
                r"^[cCdD*!]\s*(?:Author|Created by|Maintainer|Developer):\s+(.*)",
                re.I | re.M,
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS ---
            # 26. planned_debt (The Promise / Good Debt)
            # Future work that doesn't necessarily imply current brokenness.
            "planned_debt": re.compile(
                r"\b(TODO|WIP|STUB|IMPLEMENT|PENDING|REFACTOR|CLEANUP|REVIEW|UPDATE|@todo)\b",
                re.I,
            ),
            # 27. fragile_debt (The Fracture / Bad Debt)
            # An explicit admission that the current logic is fragile, dangerous, or ugly.
            "fragile_debt": re.compile(
                r"\b(HACK|FIXME|XXX|BUG|WORKAROUND|KLUDGE|OPTIMIZE|HARDCODED|NOQA|IGNORED|WTF|BROKEN|FRAGILE|UGLY|MESSY|BAND-AID|PATCH)\b",
                re.I,
            ),

            # 29. spec_exposure (The Map vs. Territory)
            # Audit tags establishing traceability of intent back to physics papers or architectural specifications.
            # CRITICAL: Removed (?i) to enforce strict uppercase [SPEC-XYZ] tags and prevent prose collisions.
            "spec_exposure": re.compile(
                r"\[\s*(?:SPEC\s*-\s*\d+|AUDIT-[A-Z0-9_-]+)\s*\]"
            ),
            # 30. civil_war (The Indentation Tracker)
            # Identifies Tab indentation. In Legacy Fortran 77, columns strictly dictate syntax (1-5 label, 6 continuation, 7+ code).
            # Using tabs violates strict standard constraints, establishing heavy tech debt/formatter civil wars.
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            # Fortran does not perform Server-Side Rendering.
            "ssr_boundaries": None,
            # 32. events (The Pub/Sub Network)
            # Fortran 2018 natively introduced Event-Driven programming primitives for Coarray synchronization.
            "events": re.compile(r"\b(EVENT\s+POST|EVENT\s+WAIT|EVENT_QUERY)\b", re.I),
            # 33. dependency_injection (The Inversion of Control)
            # Fortran handles linkages procedurally or via modules. No native DI containers or decorators exist.
            "dependency_injection": None,
            # Low-level systems language concepts mapped to Fortran paradigms.
            # 34. macros (The Preprocessor Hooks)
            # Fortran utilizes the standard C Preprocessor (cpp) allowing for structural `#define`, `#ifdef` pathing (e.g., `#ifdef MPI`).
            "macros": re.compile(
                r"^[ \t]*#(?:define|undef|if|ifdef|ifndef|elif|else|endif|include|pragma)\b",
                re.M | re.I,
            ),
            # 35. pointers (The Memory Map)
            # Explicit memory mapping. Includes native Fortran `POINTER` logic, assignments `=>`, and C-FFI pointer bridges (`C_PTR`).
            "pointers": re.compile(r"(?i)\bpointer\b|[ \t]*=>[ \t]*"),
            # 36. memory_alloc (Manual Memory Management)
            # Dynamic memory allocation managed explicitly by the developer on the heap.
            "memory_alloc": re.compile(
                r"\b(ALLOCATE|DEALLOCATE|MOVE_ALLOC|MALLOC|FREE)\b", re.I
            ),
            # 37. inline_asm (The Bare Metal)
            # Fortran delegates assembly to standard C linkage. Inline ASM is explicitly not supported natively in Fortran code.
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Structured Observers)
            # CRITICAL GUARDRAIL: Isolates structured diagnostic output (custom Fortran loggers) away from raw terminal prints.
            "telemetry": re.compile(
                r"\b(?:call[ \t]+)?(?:log_info|log_error|log_warn|log_debug|logger%info|logger%error|logger%warn|logger%debug|flog)\b",
                re.I,
            ),
            # 39. print_hits (The Amateur / Space Debris)
            # Raw terminal output natively dumping to stdout.
            "print_hits": re.compile(
                r"\b(?:PRINT\b|WRITE\s*\(\s*(?:\*|6)\s*[,)])", re.I
            ),
            # 40. cast_hits (The Trust Me Tax)
            # Forceful type coercion bypassing the safety engine. Strictly defining known Fortran intrinsic type conversion functions.
            "cast_hits": re.compile(
                r"(?i)\b(?:int|real|cmplx|dble|achar|char|iachar|ichar)[ \t]*\([^)]*\)"
            ),
            # 41. bailout_hits (The Detonators)
            # Hard execution destruction and unrecoverable exceptions.
            "bailout_hits": re.compile(r"(?i)\b(?:stop|error[ \t]+stop|return)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            # Forcing threads to sleep.
            "halt_hits": re.compile(r"(?i)\bcall[ \t]+(?:sleep|usleep)\b"),
            # 43. bitwise_hits (The Sub-Atomic Math)
            # Low-level byte manipulation utilizing Fortran's explicit intrinsic bitwise functions.
            "bitwise_hits": re.compile(
                r"(?i)\b(?:iand|ior|ieor|not|ishft|ishftc|btest|ibset|ibclr|ibits)\b"
            ),
            # 44. sync_locks (The Barricades)
            # Explicit coordination to prevent race conditions (The Yang to Concurrency).
            "sync_locks": re.compile(
                r"(?i)\b(?:lock|unlock|critical|sync[ \t]+all|sync[ \t]+images|sync[ \t]+memory)\b"
            ),
            # 45. freeze_hits (The Data Cryogenics)
            # Explicit locking of data to prevent mutation (The Yang to Flux).
            "freeze_hits": re.compile(
                r"(?i)\b(?:parameter|intent[ \t]*\([ \t]*in[ \t]*\))\b"
            ),
            # 46. cleanup (The Janitor)
            # Explicit destruction of state or closing of streams (The Yang to IO/Memory).
            "cleanup": re.compile(r"(?i)\b(?:close|deallocate|nullify)\b"),
            # 47. encapsulation (The Vault)
            # Logic hidden from view via visibility modifiers (The Yang to API).
            "encapsulation": re.compile(r"(?i)\bprivate\b"),
            # 48. listeners (The Sinks)
            # Waiting to receive state from an external broadcast (The Yang to Events).
            "listeners": None,
            # 49. test_skip (Safety Theater)
            # Framework code that explicitly bypasses verification.
            "test_skip": None,
        },
    },
    "assembly": {
        "_meta": {
            "target_version": "x86-64 (NASM/GAS) & ARMv8 (AArch64) - Backwards Compatible",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard assembly, GNU Assembler, NASM, MASM, and architecture-specific extensions.
        "extensions": [
            ".asm",
            ".s",
            ".S",
            ".inc",
            ".nasm",
            ".s64",
            ".masm",
            ".arm",
            ".a51",
        ],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Assembly is assembled directly to machine code; no extensionless exact configurations exist.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, linker scripts (.ld), and build systems acting as gravity anchors to resolve .inc or .s files.
        "discriminators": [
            ".asm",
            ".s",
            ".S",
            ".c",
            ".cpp",
            ".ld",
            "Makefile",
            "CMakeLists.txt",
        ],
        # EXECUTION SIGNATURES: Assembly is compiled/assembled to binary; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 8 (Singular/Unique)
        # Rationale: Uses unique line delimiters ';' (NASM/Intel) and '#' (GAS/ARM).
        "lexical_family": "singular",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Assembly uses ';' or '#' for standard line-level literature.
            # (Note: '//' is occasionally used in modern GAS but ';' remains the anchor).
            "_line_anchor": re.compile(r"[;#]"),
            # Inline comments are triggered by the same ';' or '#' tokens.
            "_inline_comment": re.compile(r"[;#]"),
            # EXPLICIT: Standard Assembly does not support multi-line block comment delimiters.
            "_block_start": None,
            "_block_end": None,
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Decisions and logical jumps. EXCLUDES system exits/halts (bailout_hits).
            "branch": re.compile(
                r"\b(jmp|je|jne|jz|jnz|ja|jb|jl|jg|jge|jle|jae|jbe|call|ret|b|bl|bx|blr|cbz|cbnz|tbz|tbnz|beq|bne|loop)\b",
                re.I,
            ),
            # 2. args (The Coupling Mass)
            # Assembly uses ABI registers for parameter coupling.
            "args": re.compile(
                r"\b([er]di|[er]si|[er]dx|[er]cx|[er][89]|x[0-7]|w[0-7]|v[0-7]|xmm[0-7])\b",
                re.I,
            ),
            # 3. linear (The Smooth Path)
            # Data movement and arithmetic primitives. EXCLUDES: Linker visibility (api) and sections (globals).
            "linear": re.compile(
                r"\b(mov|mov[bwlq]|lea|ldr|str|push|pop|add|sub|inc|dec|mul|imul|div|idiv|nop|ldp|stp)\b",
                re.I,
            ),
            # 4. func_start (The Satellite Spawner)
            # Subroutine entry points. EXCLUDES data labels or local loop markers.
            "func_start": re.compile(
                r"^[ \t]*(?!\.L|\.LC|\d|\.text|\.data|\.bss)([a-zA-Z_][a-zA-Z0-9_.$]*)(?=\s*:)",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            # Maps to assembler structure definition macros.
            "class_start": re.compile(
                r"^[ \t]*(?:struc|STRUCT|\.struct)\s+[a-zA-Z_]\w*", re.M | re.I
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            # Stack preservation and defensive frame setups.
            "safety": re.compile(
                r"\b(enter|leave|endbr64|paciasp|autiasp|bti|retab|\.align|\.p2align)\b|\b(?:stp|ldp)\s+x29,\s*x30",
                re.I,
            ),
            # 7. safety_neg (The Fractures)
            # Indirect jumps and hardware interrupt disabling.
            "safety_neg": re.compile(
                r"\b(?:jmp|call)\s+(?:\*|\[|[er]?[abcd]x|r\d+)\b|\bbr\s+[xw]\d+\b|\b(cli|msr\s+daifclr)\b",
                re.I,
            ),
            # 8. danger (The Heavy Load)
            # CPU halts and debug traps. EXCLUDES prints (Phase 5).
            "danger": re.compile(r"\b(hlt|int\s+3|brk|ud2|sys_exit|sys_kill)\b", re.I),
            # 9. io (The Boundaries)
            # System calls and hardware I/O ports.
            "io": re.compile(
                r"\b(in|out|ins[bdw]|outs[bdw]|syscall|svc\b|int\s+0x80|sys_read|sys_open)\b",
                re.I,
            ),
            # 10. api (The Event Horizon)
            # Linker-visible global exports.
            "api": re.compile(
                r"^[ \t]*(?:\.global|\.globl|global|EXPORT|PUBLIC|EXTERN|IMPORT)\b",
                re.M | re.I,
            ),
            # 11. flux (The Boiling Plasma)
            # Explicit memory/register swaps and atomic increments.
            "flux": re.compile(r"\b(xchg|cmpxchg|inc|dec)\b", re.I),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"(?i)(?:;|#|//)[ \t]*(?:jmp|call|mov|push|pop|cmp|add|sub)\b"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r"^[;#@/|]+\s*@(?:param|return|brief|author|note)", re.M | re.I
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r"(?i)\b(?:describe|expect|assert|TestCase)\b|\bit[ \t]*\("
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Domain) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(lock|xadd|mfence|lfence|sfence|dmb|dsb|isb|ldxr|stxr|ldaxr|stlxr)\b",
                re.I,
            ),
            # 16. ui_framework
            "ui_framework": None,
            # 17. closures
            "closures": None,
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"^[ \t]*(?:\.data|\.bss|\.rodata|\.comm|section\s+\.data|section\s+\.bss)\b",
                re.M | re.I,
            ),
            # 19. decorators
            "decorators": None,
            # 20. generics
            "generics": None,
            # 21. comprehensions (The High-Density Loops)
            # Instruction repetition prefixes.
            "comprehensions": re.compile(
                r"^[ \t]*(?:%rep|\.rept|\.irp)\b|\b(?:rep|repe|repne|repz|repnz)\b",
                re.M | re.I,
            ),
            # 22. scientific (The Compute Core)
            # FPU, SSE, AVX, and NEON instructions.
            "scientific": re.compile(
                r"\b(fadd|fsub|fmul|fdiv|fsqrt|vadd[ps][sd]|vsub[ps][sd]|vmul[ps][sd]|fmla|fmov)\b",
                re.I,
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Complex SIB addressing and block replication.
            "heat_triggers": re.compile(
                r"\[\s*[a-zA-Z0-9_]+\s*\+\s*[a-zA-Z0-9_]+\s*\*\s*\d+", re.I
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(
                r"^[ \t]*(?:%include|\.include|\.incbin)\b", re.M | re.I
            ),
            
            "_dependency_capture": re.compile(r"^[ \t]*(?:%include|\.include|\.incbin)\s+(?:['\"]([^'\"]+)['\"]|([^'\"\s]+))", re.M | re.I),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"^[;#@/|]+\s*(?:Author|Created by|Maintainer|Copyright):\s+(.*)",
                re.M | re.I,
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit|rfc)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries
            "ssr_boundaries": None,
            # 32. events (The Pub/Sub Network)
            # Interrupt vectors and exception handlers.
            "events": re.compile(
                r"\b(int\s+(?:0x)?[0-9a-fA-F]+|iret[qd]?|reti|svc|hvc|smc)\b|^[ \t]*(?:vector|handler|isr)_[a-zA-Z0-9_]+:",
                re.M | re.I,
            ),
            # 33. dependency_injection
            "dependency_injection": None,
            # 34. macros (The Preprocessor Hooks)
            "macros": re.compile(
                r"^[ \t]*(?:%macro|\.macro|%endmacro|\.endm|%define|\.equ|\.set|#define)\b",
                re.M | re.I,
            ),
            # 35. pointers (The Memory Map)
            # Raw memory addressing and dereferencing.
            "pointers": re.compile(
                r"(?i)(?:byte|word|dword|qword)[ \t]+ptr[ \t]*\[[^\]]*\]|\[[^\]]+\]"
            ),
            # 36. memory_alloc (Manual Memory Management)
            "memory_alloc": re.compile(
                r"\b(?:call|bl)\s+(?:_?malloc|_?calloc)\b|\b(?:sys_mmap|sys_brk)\b",
                re.I,
            ),
            # 37. inline_asm
            "inline_asm": None,  # This is base assembly.
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(?:call|bl)\s+(?:log_info|log_error|log_warn|log_debug|syslog)\b",
                re.I,
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(
                r"\b(?:call|bl)\s+(?:printf|puts|sys_write)\b", re.I
            ),
            # 40. cast_hits (The Trust Me Tax)
            "cast_hits": re.compile(r"(?i)\b(?:byte|word|dword|qword)[ \t]+ptr\b"),
            # 41. bailout_hits (The Detonators)
            # Hard execution destruction and unrecoverable hardware exceptions. [cite: 780]
            "bailout_hits": re.compile(r"(?i)\b(?:hlt|ud2|brk|svc|int[ \t]+3)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            # Forcing hardware threads to sleep or pause execution. [cite: 781]
            "halt_hits": re.compile(r"(?i)\b(?:pause|hlt|wfi|wfe)\b"),
            # 43. bitwise_hits (The Sub-Atomic Math)
            # Low-level byte manipulation natively supported by the instruction set. [cite: 782]
            "bitwise_hits": re.compile(
                r"(?i)\b(?:and|or|xor|not|shl|shr|sal|sar|rol|ror|lsl|lsr|asr)\b"
            ),
            # 44. sync_locks (The Barricades)
            # Explicit hardware coordination to prevent race conditions (e.g., atomic instructions, memory barriers). [cite: 783]
            "sync_locks": re.compile(
                r"(?i)\b(?:lock|xchg|cmpxchg|stxr|ldxr|dmb|dsb|isb)\b"
            ),
            # 45. freeze_hits (The Data Cryogenics)
            # Explicit locking of data to prevent mutation (e.g., read-only data sections or constants). [cite: 784]
            "freeze_hits": re.compile(r"(?i)\b(?:equ|\.rodata|\.rdata)\b"),
            # 46. cleanup (The Janitor)
            # Assembly relies on manual memory management via standard instructions, lacking dedicated cleanup APIs. [cite: 785]
            "cleanup": re.compile(r"\b(?:call|bl)\s+_?free\b", re.I),
            # 47. encapsulation (The Vault)
            # Logic hidden from view via visibility directives. [cite: 786]
            "encapsulation": re.compile(r"(?i)\b(?:\.local|\.private)\b"),
            # 48. listeners (The Sinks)
            # Assembly relies on hardware interrupts rather than high-level listener subscriptions. [cite: 787]
            "listeners": None,
            # 49. test_skip (Safety Theater)
            # Framework code that explicitly bypasses verification. [cite: 788]
            "test_skip": None,
        },
    },
    "agc_assembly": {
        "_meta": {
            "target_version": "Apollo Guidance Computer (Luminary 099 / Comanche 055 - Apollo 11)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard Apollo Guidance Computer digitized source files.
        "extensions": [".agc"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: AGC code is hardware-level; no extensionless exact configurations exist.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions and emulator/assembler tools to lock in the historical context.
        "discriminators": [".agc", "yaYUL"],
        # EXECUTION SIGNATURES: AGC code is hardware-level or emulator-resident; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 3 (Pure Hash)
        # Rationale: Digitized source uses '#' for line-level Ghost Mass.
        "lexical_family": "pure_hash",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # AGC digitized source uses '#' for standard line-level literature.
            "_line_anchor": re.compile(r"#"),
            # Inline comments are also triggered by the '#' token.
            "_inline_comment": re.compile(r"#"),
            # EXPLICIT: AGC Assembly does not support multi-line block comment delimiters.
            "_block_start": None,
            "_block_end": None,
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Decisions and logical jumps. EXCLUDES fatal alarms (bailout_hits).
            "branch": re.compile(
                r"\b(TC|TCF|BZF|BZE|BMN|BPL|CCS|RESUME|RETURN|TCR|OVSK|BVBZ|CALL|GOTO)\b",
                re.I,
            ),
            # 2. args (The Coupling Mass)
            # Safely captures hardware registers (A, Q, L, Z) ONLY when they are
            # explicitly coupled to an AGC mathematical/memory opcode.
            # Also captures the Bank assignment declarations.
            "args": re.compile(
                r"\b(?:[EFB]BANK)="
                r"|"
                r"\b(?:CA|CS|TS|AD|SU|MULT|DV|MASK|DXCH|LXCH|QXCH|XCH|INDEX)[ \t]+(?:A|Q|L|Z)\b",
                re.I,
            ),
            # 3. linear (The Smooth Path)
            # Standard instruction flow and data markers.
            "linear": re.compile(
                r"\b(CA|CS|TS|DXCH|LXCH|QXCH|XCH|AD|SU|MULT|DV|MASK|SETLOC|BANK|COUNT|ADRES|OCTAL|2OCT|DEC|2DEC|BLOCK|ERASE)\b",
                re.I,
            ),
            # 4. func_start (The Satellite Spawner)
            # Subroutine entry points anchoring logic blocks.
            "func_start": re.compile(
                r"^([A-Z0-9_-]+)(?=\s+(?:TC|CA|CS|TS|DXCH|CCS|DLOAD|STORE|CALL|INDEX|EXTEND|INHINT|BZF|BZMF|BPL|BMI)\b)",
                re.M | re.I,
            ),
            # 5. class_start
            # AGC lacks native objects.
            "class_start": None,
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            # Real-time safety guards and interrupt control.
            "safety": re.compile(
                r"\b(INHINT|RELINT|TC\s+DOWNRUPT|CS\s+ERESTORE|MUST\s+RESTORE|EDRUPT)\b",
                re.I,
            ),
            # 7. safety_neg (The Fractures)
            # Bypassing predictable flow or task management risks.
            "safety_neg": re.compile(
                r"\b(TC\s+JOBSLEEP|TC\s+JOBWAKE|TCF\s+2|TASKOVER|TCF\s+ADRERR)\b", re.I
            ),
            # 8. danger (The Heavy Load)
            # High-risk failure states and alarms. EXCLUDES MOD history (Phase 2 debt).
            "danger": re.compile(
                r"\b(CURTAINS|SOFTWARE\s+RESTART|SYSTEM_FAILURE|WHIMPER|HALT)\b", re.I
            ),
            # 9. io (The Boundaries)
            # Hardware I/O bridging to the Command/Lunar Module.
            "io": re.compile(
                r"\b(DSKY|CHANNEL|READ|WRITE|V\d+N\d+|OUT\d+|IN\d+)\b", re.I
            ),
            # 10. api (The Event Horizon)
            # Global labels and externally visible entry points.
            "api": re.compile(
                r"^[A-Z0-9_-]+\s+EQUALS|^[ \t]*(?:SUBROUTINE|BEXT|EXTEND)\b",
                re.M | re.I,
            ),
            # 11. flux (The Boiling Plasma)
            # Direct state mutation and register storage.
            "flux": re.compile(
                r"\b(TS|DXCH|LXCH|QXCH|XCH|INCR|AUG|DIM|WRSUB|AUGMENT|DIMINISH|STORE|STQ|STCALL|DAS)\b",
                re.I,
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(r"(?i)#[ \t]*(?:TCF|CCS|INDEX|BZF|BZN|CA|CS)\b"),
            # 13. doc (The Intent)
            "doc": re.compile(
                r"^#\s*(?:Page|MOD\s+(?:BY|NO)|FUNCTIONAL\s+DESCRIPTION|SUBROUTINE|PURPOSE|CALLING\s+SEQUENCE|AUTHOR|PROGRAM|REVISION)",
                re.M | re.I,
            ),
            # 14. test (The Verification)
            # System integrity verifications and self-checks.
            "test": re.compile(
                r"\b(TC\s+ALARM2|SELFCHECK|ROPECHK|ERASCHK|CNTRCHK|CHECK|TC\s+BANKJUMP)\b",
                re.I,
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Domain) ---
            # 15. concurrency (The Temporal Static)
            # Priority multitasking scheduler and task management.
            "concurrency": re.compile(
                r"\b(PRIO[1-9]|EXEC|TC\s+NOVAC|TC\s+WAITLIST|TC\s+FINDVAC|ENDOFJOB|PHASCHNG|AWAKE|SLEEP|VARDELAY)\b",
                re.I,
            ),
            # 16. ui_framework (The View Layer)
            # DSKY (Display/Keyboard) UI verbs and nouns.
            "ui_framework": re.compile(
                r"\b(V\s+\d+|N\s+\d+|NOUN|VERB|ENTER|PROCEED)\b", re.I
            ),
            # 17. closures
            "closures": None,
            # 18. globals (The Shared Void)
            # Memory division markers.
            "globals": re.compile(
                r"\b(ERASABLE\s+MEMORY|FIXED\s+MEMORY|WORKING-STORAGE|COMMON|FLAGWRD\d+|BIT\d+)\b",
                re.I,
            ),
            # 19. decorators
            "decorators": None,
            # 20. generics
            "generics": None,
            # 21. comprehensions
            "comprehensions": None,
            # 22. scientific (The Compute Core)
            # Vector math and orbital navigation interpreter routines.
            "scientific": re.compile(
                r"\b(VAD|VSUB|BDSU|DDV|DMP|DSU|SQRT|NORM|SIGN|ABS|SIN|COS|ASIN|ACOS|SPCOS|SPSIN|DOT|CROSS|UNIT|ABVAL|VXV|VXM|MXV)\b",
                re.I,
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Self-modifying logic and VM entry.
            "heat_triggers": re.compile(
                r"\b(INDEX|TC\s+INTPRET|DXCH\s+0000|RVQ)\b", re.I
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(r"\b(BANK|SETLOC|EBANK=)\b", re.I),
            
            "_dependency_capture": re.compile(r"\b(?:BANK\s+|SETLOC\s+|EBANK=\s*)([A-Za-z0-9_]+)", re.I),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"^#\s*(?:MOD\s+BY|AUTHOR|CREATED\s+BY|MAINTAINER|Contact)\s*[:\-]\s*(.*)",
                re.M | re.I,
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(
                r"#\s*(TEMPORARY|WIP|STUB|IMPLEMENT|TODO)\b", re.I
            ),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(
                r"#\s*(HACK|FIXME|XXX|BOGUS|BUG|TRASH\s+POCKET)\b", re.I
            ),

            # 29. spec_exposure (The Map vs. Territory)
            # Linkage to MIT GSOP or mission versions.
            "spec_exposure": re.compile(
                r"\b(GSOP|LUMINARY|COMANCHE|COLOSSUS|SUNDISK|SUNBURST|PCR\s*\d+|PCN\s*\d+|SPEC\s*-\s*\d+|#\s*REF:)\b",
                re.I,
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries
            "ssr_boundaries": None,
            # 32. events (The Pub/Sub Network)
            # Hardware interrupt vectors (Rupts).
            "events": re.compile(
                r"\b(RUPT|TIME1|TIME2|KEYRUPT|UPRUPT|DOWNRUPT|RADAR|OPTIC|HANDRUPT|ERRUPT)\b",
                re.I,
            ),
            # 33. dependency_injection
            "dependency_injection": None,
            # 34. macros (The Preprocessor Hooks)
            "macros": re.compile(r"^[ \t]*(?:MACRO|ENDMAC|DEFINE)\b", re.M | re.I),
            # 35. pointers (The Memory Map)
            "pointers": re.compile(
                r"\b(?:INDEX|INDIRECT|POINTER|CADR|FCADR|ECADR)\b|\*[A-Z0-9_-]+", re.I
            ),
            # 36. memory_alloc (Manual Memory Management)
            "memory_alloc": re.compile(r"\b(?:ERASABLE|FIXED|EQUALS|SHARE)\b", re.I),
            # 37. inline_asm
            "inline_asm": None,
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            # Spacecraft downlink routines.
            "telemetry": re.compile(
                r"\b(DNTM|DOWNLINK|TELEM|TM|DUMPTEL|TM\s+WORD)\b", re.I
            ),
            # 39. print_hits
            "print_hits": re.compile(r"\b(?:FLASH|PINBALL|OUT\d+)\b", re.I),
            # 40. cast_hits
            "cast_hits": re.compile(r"\bEXTEND\b", re.I),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(POODOO|BAILOUT|TC\s+ALARM|ABORT)\b", re.I),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\b(TC\s+JOBSLEEP|VARDELAY)\b", re.I),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(r"\b(MASK|AD|SU|MULT|DV)\b", re.I),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(r"\b(INHINT|RELINT|LOCK|UNLOCK)\b", re.I),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(r"\bFIXED\s+MEMORY\b", re.I),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(r"\b(ENDOFJOB|RESUME|EXIT)\b", re.I),
            # 47. encapsulation (The Vault)
            # Internal task-local labels or non-global tags.
            "encapsulation": re.compile(r"^[ \t]*[a-z0-9_][a-zA-Z0-9_.]*", re.M),
            # 48. listeners (The Sinks)
            "listeners": re.compile(r"\b(EVENT\s+WAIT|TC\s+WAITLIST)\b", re.I),
            # 49. test_skip (Safety Theater)
            "test_skip": None,
        },
    },
    "lua": {
        "_meta": {
            "target_version": "Lua 5.5 / Luau / LuaLS Annotations / LuaJIT",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard scripts, Luau (Roblox), Nmap Scripting Engine (.nse), and LuaRocks package specs (.rockspec).
        "extensions": [".lua", ".luau", ".nse", ".pd_lua", ".wlua", ".rockspec"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Tooling and documentation configurations that are secretly pure Lua code.
        "exact_matches": ["config.ld"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, package manifests, and linting configs to resolve ambiguous files.
        "discriminators": [".lua", ".luacheckrc", "stylua.toml", ".rockspec"],
        # EXECUTION SIGNATURES: Interpreters found on Line 1 for CLI, Game-Engine, and embedded scripts.
        "shebangs": ["lua", "luajit", "luau", "texlua"],
        # UPGRADED: Maps to Family 5 (Hybrid Dash)
        # Rationale: Uses '--' for lines and '--[[ ... ]]' for blocks.
        "lexical_family": "hybrid_dash",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Lua uses '--' for standard line-level literature.
            "_line_anchor": re.compile(r"--"),
            # Inline comments are also triggered by the '--' token.
            "_inline_comment": re.compile(r"--"),
            # Block comment start: --[[
            # (Note: Lua supports long-brackets, but --[[ is the standard signature)
            "_block_start": re.compile(r"--\[=*\["),
            # Block comment end: Catches standard ]] and long-bracket ]=] styles
            "_block_end": re.compile(r"\]=*\]"),
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch: decisions that split flow. Includes standard loops and Lua 5.2+ goto.
            "branch": re.compile(
                r"\b(if|then|elseif|else|for|in|while|do|repeat|until|break|goto|and|or|not)\b"
            ),
            # 2. args: Coupling Mass. Captures parameters in named and anonymous function signatures.
            "args": re.compile(r"\bfunction\s*(?:[a-zA-Z_][\w.:]*\s*)?\([^)]*\)"),
            # 3. linear: Smooth Path. Structural boundaries defining scope and data definitions.
            "linear": re.compile(
                r"\b(local|end|require|module|return)\b|<\s*(?:const|close|toclose)\s*>"
            ),
            # 4. func_start: Satellite Spawner. Anchors executable logic blocks (named functions).
            "func_start": re.compile(
                r"^[ \t]*(?:local[ \t]+)?(?:export[ \t]+)?function\s+([a-zA-Z_][\w.:]*)(?=[ \t]*\()",
                re.M,
            ),
            # 5. class_start: Entity Census. Captures proto-tables or EmmyLua class definitions.
            "class_start": re.compile(
                r"^[ \t]*---@class\s+([a-zA-Z_]\w*)|^[ \t]*(?:local[ \t]+)?(?:export[ \t]+)?([A-Z][a-zA-Z0-9_]*)(?=[ \t]*=[ \t]*\{)",
                re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety: Cyan Fortification. Protected calls, assertions, and type checks.
            "safety": re.compile(
                r"\b(pcall|xpcall|assert|error|type|getmetatable|rawequal|ipairs|pairs|next)\b|<\s*(?:const|close|toclose)\s*>"
            ),
            # 7. safety_neg: Fractures. Actively bypassing safety (environment manipulation/raw access).
            "safety_neg": re.compile(
                r"\b(rawget|rawset|rawlen|debug\.[a-zA-Z0-9_]+|collectgarbage|_G|_ENV|getfenv|setfenv)\b"
            ),
            # 8. danger: Heavy Load. Dynamic evaluation and OS-level execution hooks.
            "danger": re.compile(
                r"\b(os\.execute|os\.exit|os\.remove|os\.rename|load|loadstring|loadfile)\b"
            ),
            # 9. io: Boundaries. Standard IO library and environment inquiries.
            "io": re.compile(
                r"\b(io\.open|io\.read|io\.lines|io\.close|io\.input|io\.output|io\.popen|os\.getenv)\b"
            ),
            # 10. api: Event Horizon. Functions NOT marked local or explicit module returns.
            "api": re.compile(
                r"^[ \t]*function\s+[^_][\w.:]*|^[ \t]*return\s+[a-zA-Z_]\w*[ \t]*$|---@public|\bexport\b",
                re.M,
            ),
            # 11. flux: Boiling Plasma. State mutation (assignments and table mutators).
            "flux": re.compile(
                r"\b[a-zA-Z_]\w*(?:\[[^\]]+\]|\.[a-zA-Z_]\w*)?\s*(?<![=<>~])=(?![=])|\btable\.(?:insert|remove|move|sort|concat)\b"
            ),
            # 12. graveyard: Necrosis. Commented out structural code trails.
            "graveyard": re.compile(
                r"(?:--|--\[=*\[)[ \t]*(?:if|local|function|for|while|print|return)\b",
                re.M,
            ),
            # 13. doc: Intent. LDoc/EmmyLua style documentation.
            "doc": re.compile(
                r"---@(?:param|return|field|see|alias|private|protected|diagnostic)|---\s*[A-Z]",
                re.M,
            ),
            # 14. test: Verification. Busted, LuaUnit, and custom verification markers.
            "test": re.compile(
                r'\b(?:setup|teardown|busted|luassert|assert|mock|stub|spy|luaunit|Test[A-Z]\w*)\b|\b(?:describe|it)\s*[\'"(]'
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency: Temporal Static. Lua coroutines and task schedulers.
            "concurrency": re.compile(
                r"\b(coroutine\.(?:create|resume|yield|wrap|status|isyieldable|close)|task\.(?:spawn|wait|defer|delay)|uv\.[a-zA-Z0-9_]+)\b"
            ),
            # 16. ui_framework: View Layer. Game engine hooks (LÖVE, Solar2D, Defold, Roblox).
            "ui_framework": re.compile(
                r"\b(love\.[a-zA-Z0-9_]+|display\.new[a-zA-Z0-9_]+|gui\.[a-zA-Z0-9_]+|Roact\.[a-zA-Z0-9_]+|Instance\.new)\b"
            ),
            # 17. closures: Functional Depth. Anonymous function depth.
            "closures": re.compile(r"(?:^|[(=,\s])function\s*\([^)]*\)", re.M),
            # 18. globals: Shared Void. Access to global registries.
            "globals": re.compile(
                r"\b(_G|_ENV|_VERSION|arg)\b|^[ \t]*[A-Z][A-Z0-9_]*[ \t]*=(?![=])", re.M
            ),
            # 19. decorators: Metadata Hooks. EmmyLua annotations.
            "decorators": re.compile(r"^[ \t]*---@[a-zA-Z_]\w*", re.M),
            # 20. generics: Type Abstractions. EmmyLua generic type annotations.
            "generics": re.compile(r"---@(?:generic|type)\s+[a-zA-Z_]\w*(?:<[^>]*>)?"),
            # 21. comprehensions: High-Density Loops. Functional iterator patterns.
            "comprehensions": re.compile(
                r"\b(?:pairs|ipairs|next|string\.gmatch)\b|\b(?:lume|moses|_\.)(?:map|filter|reduce|each|find|any|all)\b"
            ),
            # 22. scientific: Compute Core. Standard math library.
            "scientific": re.compile(
                r"\b(math\.[a-zA-Z0-9_]+|bit32\.[a-zA-Z0-9_]+)\b|<<|>>|//"
            ),
            # 23. heat_triggers: Thermal Radiation. Metatable overrides and Dunder methods.
            "heat_triggers": re.compile(
                r"\b(__index|__newindex|__call|__add|__sub|__mul|__div|__mod|__pow|__unm|__idiv|__band|__bor|__bxor|__bnot|__shl|__shr|__concat|__len|__eq|__lt|__le|__gc|__close|__mode)\b"
            ),
            # 24. import: Gravity Links. Dependency resolution.
            "import": re.compile(r"\b(require|dofile)\b"),
            
            "_dependency_capture": re.compile(r"\b(?:require|dofile)\s*\(?\s*['\"]([^'\"]+)['\"]", re.M),
            
            # 25. ownership: Authorship metadata in comments.
            "ownership": re.compile(
                r"--\s*(?:Author|Copyright|License|Maintainer):\s+([^\n]+)|---\s*@author\s+([^\n]+)",
                re.I | re.M,
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            # 26. planned_debt: The Promise. Future work markers.
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            # 27. fragile_debt: The Fracture. Admitted fragility or hacks.
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure: Map vs. Territory. Audit tags.
            "spec_exposure": re.compile(r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)\]", re.I),
            # 30. civil_war: Indentation Tracker. Tabs vs Spaces density.
            "civil_war": None,
            # 31. ssr_boundaries: View Horizon. Server-side rendering (Lapis/OpenResty).
            "ssr_boundaries": re.compile(
                r"\b(ngx\.say|ngx\.print|ngx\.exit|ngx\.req|lapis\.Serve|lapis\.Application)\b"
            ),
            # 32. events: Pub/Sub Network. Signal handlers and event brokers.
            "events": re.compile(
                r"\b(addEventListener|removeEventListener|dispatchEvent|on|emit|EventEmitter|Connect|FireServer|FireClient)\b"
            ),
            # 33. dependency_injection: Inversion of Control. Service locator patterns.
            "dependency_injection": re.compile(
                r"\b(inject|container:get|container:resolve|Locator)\b"
            ),
            # 34. macros: Preprocessor Hooks. (Lua lacks a native preprocessor).
            "macros": None,
            # 35. pointers: Memory Map. FFI raw memory interactions.
            "pointers": re.compile(
                r"\b(ffi\.cast|ffi\.new|ffi\.cdef|ffi\.typeof|ffi\.sizeof|ffi\.alignof|ffi\.offsetof|ffi\.string|ffi\.copy|ffi\.fill)\b"
            ),
            # 36. memory_alloc: Manual Memory Management. Garbage collection triggers and FFI malloc.
            "memory_alloc": re.compile(
                r"\b(ffi\.C\.malloc|ffi\.C\.free|ffi\.C\.calloc|ffi\.C\.realloc|collectgarbage)\b"
            ),
            # 37. inline_asm: Bare Metal.
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry: Professional diagnostics.
            "telemetry": re.compile(
                r"\b(?:log\.(?:info|warn|error|debug|trace)|ngx\.log|ngx\.ERR|ngx\.INFO)\b"
            ),
            # 39. print_hits: Amateur space debris.
            "print_hits": re.compile(r"\b(print|warn|io\.write)\b"),
            # 40. cast_hits: "Trust Me" Tax.
            "cast_hits": re.compile(r"\b(ffi\.cast|tonumber|tostring)\b"),
            # 41. bailout_hits: Detonators.
            "bailout_hits": re.compile(r"\b(error|assert|os\.exit)\b"),
            # 42. halt_hits: Temporal Duct Tape.
            "halt_hits": re.compile(r'\b(task\.wait|os\.execute\s*\(?[\'"]sleep)\b'),
            # 43. bitwise_hits: Sub-Atomic Math.
            "bitwise_hits": re.compile(r"<<|>>|&|\||\^|~(?!=)"),
            # 44. sync_locks: Barricades.
            "sync_locks": re.compile(
                r"\b(mutex|lock|semaphore|critical_section|uv\.mutex)\b", re.I
            ),
            # 45. freeze_hits: Data Cryogenics.
            "freeze_hits": re.compile(r"<\s*const\s*>"),
            # 46. cleanup: The Janitor.
            "cleanup": re.compile(
                r"\b(ffi\.C\.free|collectgarbage|io\.close|:[ \t]*close)\b|<\s*(?:close|toclose)\s*>"
            ),
            # 47. encapsulation: The Vault.
            "encapsulation": re.compile(r"\b(local|_ENV)\b|---@private", re.M),
            # 48. listeners: The Sinks.
            "listeners": re.compile(
                r"\b(on\s*\(|subscribe|Connect|addEventListener)\b"
            ),
            # 49. test_skip: Safety Theater.
            "test_skip": re.compile(r"\b(xdescribe|xit|skip)\b"),
        },
    },
    "perl": {
        "_meta": {
            "target_version": "Perl 5.42.0 (Corinna Native OOP, Signatures, Try/Catch, Defer)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard scripts, modules, tests, POD docs, and legacy CGI web scripts.
        "extensions": [".pl", ".pm", ".t", ".pod", ".plx", ".cgi", ".al", ".ph"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Core build scripts that are purely executed Perl code.
        "exact_matches": ["Makefile.PL", "Build.PL"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions and CPAN metadata to resolve .pl (Prolog collision) and .t.
        "discriminators": [
            ".pm",
            ".pod",
            ".pl",
            "cpanfile",
            "cpanfile.snapshot",
            "META.json",
            "META.yml",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1.
        "shebangs": ["perl", "perl5", "perl6"],
        # UPGRADED: Maps to Family 1 (Standard C-Style)
        # Rationale: FIXED: Changed from 'hybrid_hash' to 'std_c' so it correctly routes to the brace parser for structural mapping.
        "lexical_family": "std_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Perl uses '#' for standard line-level literature.
            "_line_anchor": re.compile(r"#"),
            # Inline comments are also triggered by the '#' token.
            "_inline_comment": re.compile(r"#"),
            # Block comment start: Perl uses POD (Plain Old Documentation) blocks.
            "_block_start": re.compile(r"^=\w+", re.M),
            # Block comment end: POD blocks are explicitly closed by '=cut'.
            "_block_end": re.compile(r"^=cut", re.M),
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch: Decisions that split the flow. Includes modern try/catch/finally and defer.
            "branch": re.compile(
                r"\b(if|unless|elsif|else|while|until|for|foreach|given|when|next|last|redo|try|catch|finally|defer|goto|continue|default)\b|&&|\|\||//|\?|:"
            ),
            # 2. args: Coupling Mass. Captures modern signatures, traditional @_ unpacking, and shift.
            "args": re.compile(
                r"\b(?:sub|method)\s+(?:[a-zA-Z_]\w*\s*)?\([^)]*\)|\bmy\s*\([^)]*\)[ \t]*=\s*@_|\bshift\b"
            ),
            # 3. linear: Smooth Path. Structural boundaries. EXCLUDES access modifiers and immutability.
            "linear": re.compile(
                r"\b(my|our|state|local|field|class|role|package|return|yield|use|require|undef|do|true|false|await)\b"
            ),
            # 4. func_start (The Satellite Spawner)
            # Anchors executable logic blocks. MUST HAVE EXACTLY ONE CAPTURE GROUP for the name.
            #
            # LLM/MAINTAINER CONTEXT & DOMAIN KNOWLEDGE:
            # 1. THE KEYWORDS: Captures standard `sub` and Perl 5.38+ Corinna OOP `method`.
            # 2. THE CAPTURE: `([a-zA-Z_]\w*)` isolates the exact function name.
            # 3. THE LOOKAHEAD GUARDRAILS `(?= ... )`: Perl allows a lot of junk between the name and the code block.
            #    - `\(` : Safely steps over legacy Prototypes `sub foo ($$)` and modern Signatures `sub foo ($a, $b)`.
            #    - `:`  : Safely steps over Subroutine Attributes `sub foo : lvalue : method {`.
            #    - `\{` : Matches standard immediate block openings `sub foo {`.
            #    - `\n|$`: Handles K&R style newline brace placements.
            "func_start": re.compile(
                r"^[ \t]*(?:sub|method)\s+" r"([a-zA-Z_]\w*)" r"(?=[ \t]*[:\(\{]|\n|$)",
                re.M,
            ),
            # 5. class_start: Entity Census. Defines object-oriented and structural boundaries.
            "class_start": re.compile(
                r"^[ \t]*(?:package|class|role)\s+([a-zA-Z_]\w*(?:::[a-zA-Z_]\w*)*)(?=[ \t]*[;\{]|\n|$)",
                re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety: Cyan Fortification. Defensive constructs (strict, warnings, safe exceptions).
            "safety": re.compile(
                r"\b(use\s+strict|use\s+warnings|use\s+v5\.\d+|croak|confess|try|catch|finally|eval[ \t]*\{|defer|isa|DOES)\b|->isa\b|->DOES\b"
            ),
            # 7. safety_neg: Fractures. Actively bypassing safety (no strict, string eval).
            "safety_neg": re.compile(
                r'\b(no\s+strict|no\s+warnings|eval\s*["\']|eval\s+(?!\w|{)|goto\s+\&)\b'
            ),
            # 8. danger: Heavy Load. Process killers and raw shell execution.
            "danger": re.compile(r"\b(system|exec|exit|qx|CORE::dump)\b|`[^`]+`"),
            # 9. io: Boundaries. Disk, Network, DBI, and standard handles.
            "io": re.compile(
                r"\b(open|close|sysopen|sysread|syswrite|opendir|closedir|DBI->connect|Mojo::UserAgent|HTTP::Tiny|LWP::UserAgent|socket|connect|bind)\b|<[A-Z_0-9]+>|<>"
            ),
            # 10. api: Event Horizon. Exposed surface area (Exports and modern routing).
            "api": re.compile(
                r'\b(?:get|post|put|del|any|patch)\s+[\'"]/[^\'"]*[\'"]|@(?:EXPORT|EXPORT_OK|EXPORT_TAGS|ISA)\b|use\s+(?:Exporter|parent|base)\b|:\s*(?:reader|writer|param)\b'
            ),
            # 11. flux: Boiling Plasma. State mutation (assignments, array mutators, substitutions).
            # UPDATED: Removed '.=' and '=~' / '!~' to prevent massive string-builder false positives.
            "flux": re.compile(
                r"\b(?:push|pop|shift|unshift|splice|delete)\b|[\$@%][a-zA-Z_]\w*(?:->|\[|\{){0,5}\s*(?:\+|-|\*|/|\||&|\^|%|x)?=(?!=)|(?:\+\+|--)|\bs/"
            ),
            # 12. graveyard: Necrosis. Commented out structural logic.
            "graveyard": re.compile(
                r"^[ \t]*#\s*(?:my|our|state|sub|method|class|package|if|unless|while|print|say)\b",
                re.M,
            ),
            # 13. doc: Intent. Structured POD documentation.
            "doc": re.compile(
                r"^=(?:pod|head[1-6]|item|over|back|cut|begin|end|encoding|for)\b", re.M
            ),
            # 14. test: Verification. Assertions and Test frameworks.
            "test": re.compile(
                r"\b(?:Test2::V0|Test::More|cmp_ok|is_deeply|subtest|done_testing|BAIL_OUT)\b|\b(?:ok|is|isnt|like|unlike|plan|diag|note)\s*\("
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency: Temporal Static. Async, forks, and threads.
            "concurrency": re.compile(
                r"\b(async|await|fork|waitpid|threads(?:->create)?|threads::shared|AnyEvent|Coro|Mojo::IOLoop|Mojo::Promise|Future|Parallel::ForkManager)\b"
            ),
            # 16. ui_framework: View Layer. GUI libraries and template engines.
            "ui_framework": re.compile(
                r"\b(Tk::|Wx::|Gtk2::|Gtk3::|Prima::|Template|HTML::Mason|Mojolicious::Plugin::TagHelpers)\b|\brender(?:_to_string)?\b|<%|%>|\[%|%\]"
            ),
            # 17. closures: Functional Depth. Anonymous subroutines.
            "closures": re.compile(r"\bsub\s*(?:\([^)]*\))?[ \t]*\{"),
            # 18. globals: Shared Void. Magic variables and system globals.
            "globals": re.compile(
                r"(?:\$a|\$b|\$_|\$\$|\$@|\$!|\$\?|\$0|%ENV|%SIG|@ARGV|@INC)\b|^[ \t]*our\s+[\$@%]",
                re.M,
            ),
            # 19. decorators: Metadata Hooks. Subroutine and variable attributes.
            "decorators": re.compile(r":\s*[a-zA-Z_]\w*(?:\([^)]*\))?"),
            # 20. generics: Type Abstractions. Parameterized types (via Type::Tiny/Moose).
            "generics": re.compile(
                r"\b(?:ArrayRef|HashRef|Map|Tuple|Dict|Maybe|InstanceOf|ConsumerOf|Enum)\[[^\]]*\]"
            ),
            # 21. comprehensions: High-Density Loops. Map and Grep.
            "comprehensions": re.compile(
                r"\b(?:map|grep|reduce|any|all|none|notall|first|List::Util)\b"
            ),
            # 22. scientific: Compute Core. PDL and Math::BigInt.
            "scientific": re.compile(
                r"\b(Math::Trig|Math::BigInt|Math::BigFloat|Math::Complex|PDL|sin|cos|exp|log|sqrt|atan2|abs|int|rand|srand)\b"
            ),
            # 23. heat_triggers: Thermal Radiation. Metaprogramming and Symbol table hacks.
            "heat_triggers": re.compile(
                r"\b(AUTOLOAD|DESTROY|BEGIN|UNITCHECK|CHECK|INIT|END|tie|untie|bless|overload)\b|\*[a-zA-Z_]\w*[ \t]*=\s*(?:\\|&)|goto\s+&"
            ),
            # 24. import: Gravity Links. Module loading.
            "import": re.compile(
                r"^[ \t]*(?:use|require|no)\s+[a-zA-Z_]\w*(?:::[a-zA-Z_]\w*)*", re.M
            ),
            
            "_dependency_capture": re.compile(r"^[ \t]*(?:use|require|no)\s+([a-zA-Z_]\w*(?:::[a-zA-Z_]\w*)*)", re.M),
            
            
            # 25. ownership: Authorship metadata.
            "ownership": re.compile(
                r"^=head1\s+(?:AUTHOR|COPYRIGHT|LICENSE)|#\s*(?:Author|Maintainer|Created by):\s+([^\n]+)",
                re.I | re.M,
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            # 26. planned_debt: The Promise. Future work markers.
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            # 27. fragile_debt: The Fracture. Admitted fragility or hacks.
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure: Map vs. Territory. Audit tags.
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war: Indentation Tracker. Tabs vs 4-Spaces density markers.
            "civil_war": None,
            # 31. ssr_boundaries: View Horizon. Server-Side Rendering computation boundaries.
            "ssr_boundaries": re.compile(
                r"\b(Mojolicious::Controller|Dancer2|Catalyst::Controller|render|template|reply->|to_app)\b"
            ),
            # 32. events: Pub/Sub Network. Event-driven architecture signatures and message brokers.
            "events": re.compile(
                r'\b(?:emit|once|unsubscribe|catch|Mojo::EventEmitter|AnyEvent->condvar)\b|\b(?:on|subscribe)\s+[\'"]'
            ),
            # 33. dependency_injection: Inversion of Control. Inversion of Control (IoC) injection markers.
            "dependency_injection": re.compile(
                r"\b(Bread::Board|Beam::Wire|IOC|container|resolve|inject|service)\b"
            ),
            # 34. macros: Preprocessor Hooks. Compiler pragmas or source filters.
            "macros": re.compile(
                r"\b(Filter::Simple|Filter::Util::Call|Devel::Declare|Keyword::Declare)\b|^[ \t]*BEGIN[ \t]*\{",
                re.M,
            ),
            # 35. pointers: Memory Map. Explicit tracking of memory addressing or references.
            # UPDATED: Removed '\\[$@%&*]\w+' to stop flagging standard pass-by-reference variables.
            "pointers": re.compile(r"->(?:\[[^\]]*\]|\{[^\}]*\})|@\$|%\$|\$\$|\&\$"),
            # 36. memory_alloc: Manual Memory Management. Explicit heap manipulations or reference count controls.
            "memory_alloc": re.compile(
                r"\b(Scalar::Util::weaken|Scalar::Util::isweak|Internals::SvREFCNT|Internals::SvREADONLY|undef|Devel::Peek)\b"
            ),
            # 37. inline_asm: Bare Metal. Direct architecture bridging via Inline modules.
            "inline_asm": re.compile(r'\buse\s+Inline\s+[\'"](?:C|CPP|ASM)[\'"]'),
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry: The Professional. Structured logging and observability frameworks.
            "telemetry": re.compile(
                r"\b(?:Log::Log4perl|Log::Any|Mojo::Log|log_(?:info|debug|warn|error|fatal))\b|->(?:debug|info|warn|error|fatal|trace)\b",
                re.I,
            ),
            # 39. print_hits: The Amateur / Space Debris. Ad-hoc debug statements.
            "print_hits": re.compile(r"\b(print|say|printf|sprintf|warn)\b"),
            # 40. cast_hits: The "Trust Me" Tax. Explicitly bypassing the type-checker or manual blessing.
            # UPDATED: Removed the pointer/reference overlap.
            "cast_hits": re.compile(r"\b(int|oct|hex|vec|ref|bless)\b"),
            # 41. bailout_hits: The Detonators. Forcefully destroying the current execution context.
            "bailout_hits": re.compile(r"\b(die|confess|croak|exit|BAIL_OUT)\b"),
            # 42. halt_hits: Temporal Duct Tape. Forcing a thread to sleep or blocking waits.
            "halt_hits": re.compile(r"\bsleep\b"),
            # 43. bitwise_hits: Sub-Atomic Math. Manipulating raw bytes and memory registers.
            # UPDATED: Added negative lookbehinds '(?<![=!])~' to ignore Perl regex operators.
            "bitwise_hits": re.compile(
                r"(?<!&)&(?!&)|(?<!\|)\|(?!\|)|<<|>>|\^|(?<![=!])~"
            ),
            # 44. sync_locks: The Barricades. Coordinating threaded logic to prevent race conditions.
            "sync_locks": re.compile(r"\b(lock|threads::shared|Thread::Semaphore)\b"),
            # 45. freeze_hits: Data Cryogenics. Explicitly locking data so it cannot be mutated.
            "freeze_hits": re.compile(
                r"\b(Readonly|Const::Fast|Internals::SvREADONLY)\b"
            ),
            # 46. cleanup: The Janitor. Explicitly destroying state or releasing resources.
            "cleanup": re.compile(
                r"\b(DESTROY|undef|close|closedir|finish)\b|^[ \t]*END[ \t]*\{", re.M
            ),
            # 47. encapsulation: The Vault. Explicitly hiding logic from the rest of the application.
            "encapsulation": re.compile(r"\b(my|state|local)\b|:private\b"),
            # 48. listeners: The Sinks. Waiting to receive state from an external broadcast.
            "listeners": re.compile(r"\b(on\s*\(|subscribe\s*\(|add_listener)\b"),
            # 49. test_skip: Safety Theater. Code that bypasses test verification.
            "test_skip": re.compile(r"\b(skip|todo_skip)\b"),
        },
    },
    "haskell": {
        "_meta": {
            "target_version": "GHC 9.14.1+ (Linear Types, cases, Type Abstractions, RecordDotSyntax)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard source, literate Haskell, and C-preprocessor Haskell.
        "extensions": [".hs", ".lhs", ".hsc", ".ghci"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Cabal custom setup scripts that evaluate as pure Haskell.
        "exact_matches": ["Setup.hs", "Setup.lhs"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, Stack configs, and Cabal manifests to anchor the ecosystem.
        "discriminators": [".hs", ".lhs", "stack.yaml", "cabal.project", ".cabal"],
        # EXECUTION SIGNATURES: Interpreters found on Line 1 for script-based Haskell execution.
        "shebangs": ["runhaskell", "runghc", "stack", "ghci"],
        # UPGRADED: Maps to Family 5 (Hybrid Dash)
        # Rationale: Uses '--' for lines and '{- -}' for blocks, which strictly supports recursive nesting.
        "lexical_family": "hybrid_dash",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Haskell uses '--' for line-level Ghost Mass.
            # CRITICAL GUARDRAIL: Negative lookahead ensures we don't accidentally split on custom operators like '-->'
            "_line_anchor": re.compile(r"--+(?![!#$%&*+./<=>?@\\^|~-])"),
            # Inline comments follow the same highly-specific symbol guard
            "_inline_comment": re.compile(r"--+(?![!#$%&*+./<=>?@\\^|~-])"),
            # Block comment start: {-
            "_block_start": re.compile(r"\{-"),
            # Block comment end: -}
            "_block_end": re.compile(r"-\}"),
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # branch: decisions that split flow. Includes guards (|) and modern \cases.
            "branch": re.compile(
                r"\b(if|then|else|case|of|MultiWayIf)\b|\\cases?|^[ \t]*\|", re.M
            ),
            # args: Coupling Mass. Captures type signatures, lambda bindings, and explicit @type apps.
            "args": re.compile(
                r"::\s*[^=\n]+(?:->|=>|⊸)|\\[a-zA-Z0-9_\'\s,()\[\]]+->|@[A-Z][a-zA-Z0-9_\']*"
            ),
            # linear: Smooth Path. Structural boundaries defining scope and data definitions.
            "linear": re.compile(
                r"\b(module|data|type|newtype|class|instance|let|in|where|do|mdo|deriving|family|pattern)\b|%1\s*->|⊸"
            ),
            # func_start: Satellite Spawner. Anchors executable logic (Type Signatures).
            # EXCLUDES data/type/class declarations to fix Ghost Satellites.
            "func_start": re.compile(
                r"^[ \t]*(?!(?:data|type|newtype|class|instance)\b)([a-z_][a-zA-Z0-9_\']*)(?=\s*::)",
                re.M,
            ),
            # class_start: Entity Census. Defines structural entities and typeclass boundaries.
            "class_start": re.compile(
                r"^[ \t]*(?:data|newtype|class|type(?:\s+family)?)\s+([A-Z][a-zA-Z0-9_\']*)(?=\s*[=|]|\n|$)",
                re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # safety: Cyan Fortification. Functional safety (Maybe/Either) and exception brackets.
            "safety": re.compile(
                r"\b(Maybe|Either|Just|Nothing|Right|Left|try|catch|bracket|finally|onException|SafeT|mask|pure|return)\b"
            ),
            # safety_neg: Fractures. Bypassing purity (unsafePerformIO) and partial functions.
            "safety_neg": re.compile(
                r"\b(unsafePerformIO|unsafeCoerce|error|undefined|fromJust|head|tail|init|last|throw|unsafeFixIO)\b"
            ),
            # danger: Heavy Load. Forceful aborts and Debug-trace leaks in production.
            "danger": re.compile(
                r"\b(die|exitWith|exitFailure|Debug\.Trace|trace|traceShow|traceIO|traceM)\b"
            ),
            # io: Boundaries. IO Monad and hardware interactions.
            "io": re.compile(
                r"\b(IO|readFile|writeFile|appendFile|hGetContents|hPutStr|openFile|withFile|getLine|getChar|Socket|Connection|runDB)\b"
            ),
            # api: Event Horizon. Captured via module headers. Captures both explicit lists and implicit "all" exports.
            "api": re.compile(
                r"^[ \t]*module\s+[A-Z][a-zA-Z0-9_.]*(?:\s*\([^)]*\))?\s*where|\bforeign\s+export\b",
                re.M,
            ),
            # flux: Boiling Plasma. State mutation (IORef/MVar) and monadic binds (<-).
            "flux": re.compile(
                r"\b(IORef|STRef|TVar|MVar|TMVar|modifyIORef\'?|writeIORef|putMVar|modify|put|StateT)\b|<-"
            ),
            # graveyard: Necrosis. Commented out structural code trails.
            "graveyard": re.compile(
                r"--\s*(?:data|type|newtype|class|instance|let|where|import|putStrLn)\b",
                re.M,
            ),
            # doc: Intent. Haddock documentation markers.
            "doc": re.compile(r"--\s*\||--\s*\^|\{-\||--\s*@(?:param|return|author)"),
            # test: Verification. Verification framework keywords (QuickCheck/Hspec).
            "test": re.compile(
                r'\b(?:hspec|QuickCheck|prop_[a-zA-Z0-9_\']+|assertEqual|shouldBe|testGroup|testCase)\b|\b(?:describe|it|property)\s+"'
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # concurrency: Temporal Static. STM, async, and thread forking.
            "concurrency": re.compile(
                r"\b(forkIO|forkOS|async|wait|cancel|MVar|TVar|STM|atomically|threadDelay)\b"
            ),
            # ui_framework: View Layer. Functional reactive GUI and web components.
            "ui_framework": re.compile(
                r"\b(Threepenny|Brick|Reflex|Miso|Gtk|widget|vBox|hBox|Lucid|Blaze|Monomer)\b"
            ),
            # closures: Functional Depth. Anonymous lambda depth.
            "closures": re.compile(r"\\[a-zA-Z0-9_\'\s(),\[\]]+\s*->|\\cases?"),
            # globals: Shared Void. Top-level state hacks (typically MVars using unsafePerformIO).
            "globals": re.compile(
                r"^[ \t]*[a-z_][a-zA-Z0-9_\']*\s*::\s*(?:IORef|TVar|MVar)[^=]*unsafePerformIO",
                re.M,
            ),
            # decorators: Metadata Hooks. GHC pragmas (INLINE, LANGUAGE).
            "decorators": re.compile(
                r"\{-#\s*(?:INLINE|NOINLINE|LANGUAGE|OPTIONS_GHC|RULES|MINIMAL)\s+[^#]*#-\}"
            ),
            # generics: Type Abstractions. forall quantification and constraints.
            "generics": re.compile(
                r"\bforall\s+[^.]+\.|\b(?:[A-Z][a-zA-Z0-9_\']*\s+[a-z][a-zA-Z0-9_\']*[ \t]*=>)|\([^)]+\)[ \t]*=>"
            ),
            # comprehensions: High-Density Loops. List comprehensions and dense monad applicatives.
            "comprehensions": re.compile(r"\[\s*[^|\]]+\s*\|[^\]]+\]|<\$>|<\*>|>>="),
            # scientific: Compute Core. Advanced Math and Linear Algebra.
            "scientific": re.compile(
                r"\b(Complex|RealFloat|Floating|Numeric\.LinearAlgebra|Matrix|Vector|ad|grad|jacobian|sin|cos|tan|exp|log|pi)\b"
            ),
            # heat_triggers: Thermal Radiation. QuasiQuotes and Template Haskell.
            "heat_triggers": re.compile(
                r"\b(TemplateHaskell|QuasiQuotes|TypeFamilies|GHC\.Generics|Generic)\b|\[[a-z_]+\||\$\([a-zA-Z0-9_\']+\)"
            ),
            # import: Gravity Links. Module resolution.
            "import": re.compile(
                r"^[ \t]*import\s+(?:qualified[ \t]+)?[A-Z][a-zA-Z0-9_.]*", re.M
            ),
            
            "_dependency_capture": re.compile(r"^[ \t]*import\s+(?:qualified\s+)?([A-Z][a-zA-Z0-9_.]*)", re.M),
            
            # ownership: Authorship indicators in comments.
            "ownership": re.compile(
                r"--\s*\|?\s*(?:Author|Maintainer|Copyright|License):\s+([^\n]+)", re.I
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            "spec_exposure": re.compile(r"\[(?:spec-[0-9]+|audit|rfc)\]", re.I),
            "civil_war": None,
            "ssr_boundaries": re.compile(
                r"\b(Yesod|Servant|ScottyM|ActionM|lucid|blaze-html|ToJSON|FromJSON|Handler|respond)\b"
            ),
            "events": re.compile(
                r"\b(Event|Behavior|Dynamic|reactive-banana|reflex|frp|stepper|accumE|conduit|Pipes|Stream)\b"
            ),
            "dependency_injection": re.compile(
                r"\b(ReaderT|MonadReader|Has[A-Z][a-zA-Z0-9_\']+|ask|asks|local)\b"
            ),
            "macros": re.compile(
                r"\{-#\s*LANGUAGE\s+[^#]*#-\}|\$[(a-z_A-Z0-9\']|^[ \t]*#(?:define|undef|if|ifdef|ifndef|elif|else|endif|include)\b",
                re.M,
            ),
            "pointers": re.compile(
                r"\b(Ptr|ForeignPtr|FunPtr|StablePtr|peek|poke|castPtr|plusPtr|nullPtr|Storable)\b"
            ),
            "memory_alloc": re.compile(
                r"\b(malloc|mallocBytes|alloca|allocaBytes|free|Foreign\.Marshal)\b"
            ),
            "inline_asm": re.compile(
                r"\bforeign\s+import\s+(?:ccall|cplusplus|prim|capi)\b"
            ),
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # telemetry: Professional structured logging.
            "telemetry": re.compile(
                r"\b(?:logDebug|logInfo|logWarn|logError|logOther|katip|MonadLogger|LoggerT)\b"
            ),
            # print_hits: Amateur space debris.
            "print_hits": re.compile(r"\b(putStr|putStrLn|print|putChar)\b"),
            # cast_hits: "Trust Me" Tax.
            "cast_hits": re.compile(
                r"\b(unsafeCoerce|coerce|fromIntegral|realToFrac|floor|ceiling|truncate|round)\b"
            ),
            # bailout_hits: The Detonators.
            "bailout_hits": re.compile(r"\b(throw|throwIO|panic|error)\b"),
            # halt_hits: Temporal Duct Tape.
            "halt_hits": re.compile(r"\b(threadDelay)\b"),
            # bitwise_hits: Sub-Atomic Math.
            "bitwise_hits": re.compile(
                r"\b(?:shift[LR]?|rotate[LR]?|xor|complement|testBit|setBit|clearBit|complementBit)\b|\.&&\.|\|\.\|\|\."
            ),
            # sync_locks: Barricades preventing races.
            "sync_locks": re.compile(
                r"\b(takeMVar|putMVar|readMVar|swapMVar|atomically|STM|Mutex|lock|unlock)\b"
            ),
            # freeze_hits: Data Cryogenics. Implicit in pure Haskell, but explicit in mutable contexts.
            "freeze_hits": re.compile(r"\b(pure|return|frozen|immutable|const)\b"),
            # cleanup: The Janitor.
            "cleanup": re.compile(
                r"\b(hClose|close|free|bracket|finally|onException)\b"
            ),
            # encapsulation: The Vault.
            "encapsulation": re.compile(
                r"^[ \t]*module\s+[A-Z][a-zA-Z0-9_.]*\s*\([^)]*\)\s*where", re.M
            ),  # Explicit export list = Encapsulated
            # listeners: The Sinks.
            "listeners": re.compile(r"\b(subscribe|onEvent|addEventListener|watch)\b"),
            # test_skip: Safety Theater.
            "test_skip": re.compile(r"\b(ignore|pending|skip|xit|xdescribe)\b"),
        },
    },
    "embedded_python": {
        "_meta": {
            "target_version": "Embedded Python (MicroPython / CircuitPython / Bare-Metal)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard Python suffixes and pre-compiled MicroPython bytecode (.mpy).
        "extensions": [".py", ".mpy"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: The strict execution entry points for microcontroller boot sequences.
        "exact_matches": ["boot.py"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, boot sequence files, and the MicroPython package installer (mip) configs.
        "discriminators": ["boot.py", "mip.json", "upip"],
        # EXECUTION SIGNATURES: Interpreters found on Line 1 for embedded discovery and cross-compilation.
        "shebangs": ["micropython", "mpy-cross"],
        
        # Instantly claims any .py file utilizing embedded electronics networking or GPIO libraries
        "internal_discriminator": re.compile(r"^[ \t]*(?:import|from)\s+(?:machine|board|microcontroller|busio|digitalio|analogio|usb_hid|neopixel|rp2|esp32|pyb|wifi|socketpool)\b", re.M),
        
        # UPGRADED: Maps to Family 3 (Pure Hash)
        # Rationale: Uses '#' for line-level literature; multi-line literature
        # (docstrings) is handled by the Section 2.3.C.3 Heuristic Pass.
        "lexical_family": "pure_hash",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # MicroPython uses '#' for line-level Ghost Mass.
            "_line_anchor": re.compile(r"#"),
            # Inline comments are also triggered by the '#' token.
            "_inline_comment": re.compile(r"#"),
            # EXPLICIT: MicroPython lacks native multi-line block comment delimiters.
            # (Note: Multi-line strings used as docs are handled by the 2.3.C Python Heuristic).
            "_block_start": None,
            "_block_end": None,
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Decisions and logical jumps. EXCLUDES raise (bailout_hits).
            "branch": re.compile(
                r"\b(if|elif|else|for|while|with|try|finally|match|case|and|or)\b"
            ),
            # 2. args (The Coupling Mass)
            # Parameter blocks of functions/lambdas. Bounded negation to prevent ReDoS.
            "args": re.compile(
                r"(?:async[ \t]+)?def\s+[a-zA-Z_]\w*\s*\([^)]*\)|\blambda\s+[^:]+:",
                re.M,
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: _private (encapsulation) and Final (freeze_hits).
            "linear": re.compile(
                r"\b(def|class|return|import|from|as|pass|continue|break|yield|await|assert|del|global|nonlocal|type)\b"
            ),
            # 4. func_start (The Satellite Spawner)
            # ONLY executable logic blocks. EXCLUDES classes. Steps safely over hardware decorators.
            "func_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]+){0,5}(?:async[ \t]+)?def\s+([a-zA-Z_]\w*)(?=\s*\()",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            "class_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]+){0,5}class\s+([a-zA-Z_]\w*)(?=[ \t]*[\(:]|\n|$)",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Cognitive Load & Tech Debt) ---
            # 6. safety (The Defenders)
            # Hardware watchdogs and standard Python safety checks.
            "safety": re.compile(
                r"\b(try|except|finally|assert|machine\.WDT|isinstance|issubclass|hasattr|getattr|alloc_emergency_exception_buf)\b"
            ),
            # 7. safety_neg (The Fractures)
            # Bare excepts and blocking the event loop (detrimental in embedded async).
            "safety_neg": re.compile(
                r"\bpass\b[ \t]*$|except\s*[:\n]|except\s+(?:Base)?Exception|from\s+[\w.]+\s+import\s+\*|\btime\.sleep(?:_ms|_us)?\b",
                re.M,
            ),
            # 8. danger (The Heavy Load)
            # Hardware resets and raw memory pokes. EXCLUDES TODO (debt) and print (print_hits).
            "danger": re.compile(
                r"\b(machine\.reset|machine\.deepsleep|machine\.bootloader|machine\.disable_irq|eval|exec|sys\.exit)\b"
            ),
            # 9. io (The Boundaries)
            # Hardware Peripherals (I2C, SPI, UART, Pin) and Networking.
            "io": re.compile(
                r"\b(open|Pin|I2C|SPI|UART|ADC|PWM|RTC|SDCard|I2S|WLAN|LAN|socket|usocket|uos\.mount|aiohttp)\b"
            ),
            # 10. api (The Event Horizon)
            # Implicit public defaults (undercased root defs) + explicit exports.
            "api": re.compile(
                r"^[ \t]*(?:async[ \t]+)?def\s+[^_]\w+|^[ \t]*class\s+[^_]\w+|^__all__[ \t]*=",
                re.M,
            ),
            # 11. flux (The Boiling Plasma)
            # State mutation including hardware value toggling.
            "flux": re.compile(
                r"\bglobal\b|\bnonlocal\b|\b(?:self|cls)\.\w+[ \t]*=|:=|(?:\.\w+)?\.(?:append|extend|update|pop|remove|insert|clear)\s*\(|\.(?:value|on|off|high|low|toggle)\s*\("
            ),
            # 12. graveyard (The Necrosis)
            "graveyard": re.compile(
                r"#[ \t]*(?:def|class|import|if|for|while|try|print|machine\.Pin)\b"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(
                r'"""|\'\'\'|:param|:return|:raises|:type|#\s*Pin[ \t]*=|#\s*GPIO'
            ),
            # 14. test (The Verification)
            "test": re.compile(
                r"\b(unittest|pytest|assert|test_|setUp|tearDown|Mock)\b"
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Domain) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(async|await|uasyncio|asyncio|Timer\.init|_thread|start_new_thread|allocate_lock|gather|create_task|Event|Lock)\b"
            ),
            # 16. ui_framework (The View Layer)
            # Framebuffers and embedded OLED/TFT drivers.
            "ui_framework": re.compile(
                r"\b(framebuf|ssd1306|st7789|ili9341|epaper|lvgl|display|text|fill|pixel|show|scroll)\b"
            ),
            # 17. closures (The Functional Depth)
            "closures": re.compile(r"\blambda\b"),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\bglobal\b|\bglobals\(\)|\blocals\(\)|\b(sys\.path|sys\.modules|os\.environ)\b"
            ),
            # 19. decorators (The Metadata Hooks)
            # Generic decorators. (Specific ASM/Viper optimizations moved to heat_triggers/inline_asm).
            "decorators": re.compile(
                r"^[ \t]*@(?!(?:micropython\.viper|micropython\.asm|micropython\.native))[\w.]+",
                re.M,
            ),
            # 20. generics (The Type Abstractions)
            "generics": re.compile(
                r"\b(?:List|Dict|Set|Tuple|Optional|Union|Any|Callable|Sequence|Iterable)\[[^\]]*\]|->"
            ),
            # 21. comprehensions (The High-Density Loops)
            "comprehensions": re.compile(
                r"\[[^\]]*\bfor\b[^\]]*\]|\{[^}]*\bfor\b[^}]*\}|\([^)]*\bfor\b[^)]*\)"
            ),
            # 22. scientific (The Compute Core)
            # Math, complex arrays, and ulab (MicroPython's NumPy).
            "scientific": re.compile(
                r"\b(math|cmath|ulab|numpy|ndarray|struct\.pack|struct\.unpack|bin|hex|oct|abs|sin|cos|tan)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Extreme "Logic Heat": Dunder methods and Viper/Native emitters.
            "heat_triggers": re.compile(
                r"__(?:getattr|setattr|new|call|dict|dir|import)__|@(?:staticmethod|classmethod|property)|@micropython\.(?:viper|native)\b|\b(?:getattr|setattr|hasattr)\b"
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(r"^[ \t]*(?:import|from)\b\s+[\w.]+", re.M),
            
            "_dependency_capture": re.compile(r"^[ \t]*(?:import|from)\b\s+([\w.]+)", re.M),
            
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"(?:__author__[ \t]*=|Author:|Created by:)\s*(.*)", re.I
            ),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(
                r"\b(HACK|FIXME|XXX|BUG|KLUDGE|UGLY|WTF)\b", re.I
            ),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            # Lightweight web servers (Microdot, Picoweb).
            "ssr_boundaries": re.compile(
                r"\b(microdot|picoweb|MicroWebSrv|tinyweb|render_template|Response|@app\.get|@app\.post)\b"
            ),
            # 32. events (The Pub/Sub Network)
            # Hardware interrupts and async event flags.
            "events": re.compile(
                r"\b(irq|Pin\.irq|Timer\.irq|machine\.enable_irq|trigger|set_callback|Event\.set|schedule)\b"
            ),
            # 33. dependency_injection
            "dependency_injection": None,  # MicroPython strictly follows imperative wiring due to RAM limits.
            # 34. macros
            # MicroPython's const() acts as a compile-time macro.
            "macros": re.compile(r"\bconst\s*\([^)]+\)"),
            # 35. pointers (The Memory Map)
            # Pointer manipulation enabled by Viper/uctypes.
            "pointers": re.compile(
                r"\b(uctypes\.addressof|uctypes\.bytearray_at|ptr8|ptr16|ptr32|machine\.mem8|machine\.mem16|machine\.mem32)\b"
            ),
            # 36. memory_alloc (The Yin to cleanup)
            "memory_alloc": re.compile(
                r"\b(bytearray|memoryview|alloc_emergency_exception_buf)\b"
            ),
            # 37. inline_asm (The Bare Metal)
            "inline_asm": re.compile(
                r"@(?:micropython\.asm_thumb|micropython\.asm_xtensa|rp2\.asm_pio)\b"
            ),
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(logging|logger|ulogging|syslog)\.(?:info|error|warn|warning|debug|trace|critical|exception)\b"
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(r"\b(print|input)\s*\("),
            # 40. cast_hits (The Trust Me Tax)
            "cast_hits": re.compile(
                r"\b(int|str|float|list|dict|set|tuple|bool|bytes|cast)\b\s*\("
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(raise|quit|exit|sys\.exit|abort)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\b(time\.sleep|asyncio\.sleep|Thread\.join)\b"),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(r"<<|>>|(?<!&)&(?!&)|(?<!\|)\|(?!\|)|\^|~"),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(Lock|RLock|Semaphore|Event|Condition|allocate_lock)\b"
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(r"\b(Final|frozenset|mappingproxy|immutable)\b"),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(r"\b(close|__exit__|del|gc\.collect|cleanup)\b\s*\("),
            # 47. encapsulation (The Vault)
            "encapsulation": re.compile(r"\b_[a-zA-Z_]\w*\b"),
            # 48. listeners (The Sinks)
            # Waiting for state broadcast via hardware IRQs or event listeners.
            "listeners": re.compile(r"\.irq\(|handler=|callback="),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(
                r"\b(pytest\.mark\.skip|unittest\.skip|mock\.|MagicMock)\b"
            ),
        },
    },
    "cobol": {
        "_meta": {
            "target_version": "Enterprise COBOL 6.4 (IBM) & GnuCOBOL 3.2",
            "last_updated": "2026-03-10",
            "blueprint_version": "v5.1",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard COBOL source files and copybooks (.cpy) which act as legacy header files.
        "extensions": [".cbl", ".cob", ".cpy", ".cobol", ".pco"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Mainframe environments do not typically use extensionless execution scripts.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions and Job Control Language (.jcl) files which orchestrated legacy COBOL execution.
        "discriminators": [".cbl", ".cob", ".cpy", ".jcl"],
        # EXECUTION SIGNATURES: Interpreters found on Line 1 (primarily for modern GnuCOBOL scripting).
        "shebangs": ["cobc"],
        # UPGRADED: Maps to Family 7 (The Positional Ancients)
        # Rationale: Strictly fixed-format. The engine must monitor Column 7 for an asterisk '*'
        # or slash '/' to identify line-level Ghost Mass.
        "lexical_family": "positional",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Fixed Format Logic: Column 7 is the 'Indicator Area'.
            # An asterisk '*' or forward-slash '/' in Col 7 marks the line as Literature (Ghost Mass).
            # Regex translates to: Start of line, skip 6 chars, match indicator.
            "_line_anchor": re.compile(r"^.{6}[*/dD]"),
            # Modern COBOL (GnuCOBOL/IBM 6+) supports floating inline comments via '*>'.
            "_inline_comment": re.compile(r"\*>"),
            # EXPLICIT: COBOL does not support multi-line block comment delimiters.
            "_block_start": None,
            "_block_end": None,
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch: Entscheidungslogik. Control flow that splits execution paths.
            "branch": re.compile(
                r"\b(IF|ELSE|EVALUATE|WHEN|PERFORM|UNTIL|VARYING|TIMES|DEPENDING\s+ON|ON\s+EXCEPTION|AT\s+END|INVALID\s+KEY|ON\s+SIZE\s+ERROR|ON\s+OVERFLOW)\b",
                re.I,
            ),
            # 2. args: Coupling Mass. Captures USING and RETURNING signatures in PROCEDURE division or CALLs.
            "args": re.compile(
                r"\b(?:USING|RETURNING)\s+((?:(?:BY\s+(?:REFERENCE|CONTENT|VALUE)[ \t]+)?[A-Z0-9_-]+[ \t]*,?){0,20})",
                re.I,
            ),
            # 3. linear: Smooth Path. Structural boundaries defining straight-line execution flow.
            # EXCLUDES access modifiers (GLOBAL, EXTERNAL) to prevent Geometry Inflation.
            "linear": re.compile(
                r"\b(DIVISION|SECTION|EXIT|CONTINUE|GOBACK|ACCEPT|XML\s+PARSE|JSON\s+GENERATE|DISPLAY|STOP\s+RUN)\b",
                re.I,
            ),
            # 4. func_start: Satellite Spawner. Anchors logic blocks (Paragraphs and Sections).
            # FIX 1: Explicitly ban `END-[A-Za-z0-9_-]+` scope terminators to prevent Area B indentation bleed.
            # FIX 2: Explicitly ban `[WORD] DIVISION` (e.g., ID DIVISION) to prevent massive structural ghosting.
            "func_start": re.compile(
                r"^(?:[0-9a-zA-Z \t]{6}[ \-]?)?[ \t]*"
                r"(?!(?:WORKING-STORAGE|DATA|ENVIRONMENT|IDENTIFICATION|ID|LINKAGE|FILE|DECLARATIVES|"
                r"INPUT-OUTPUT|CONFIGURATION|DISPLAY|CALL|MOVE|COMPUTE|PERFORM|ADD|SUBTRACT|MULTIPLY|"
                r"DIVIDE|INITIALIZE|SET|IF|ELSE|GOBACK|EXIT|STOP|EVALUATE|WHEN|READ|WRITE|REWRITE|"
                r"DELETE|OPEN|CLOSE|PROGRAM-ID|CLASS-ID|END-[A-Za-z0-9_-]+)\b)"
                r"(?![A-Za-z0-9_-]+\s+DIVISION\b)"
                r"([A-Za-z0-9_-]+)(?=(?:\s+SECTION)?[ \t]*\.)",
                re.I | re.M,
            ),
            # 5. class_start: Entity Census. Defines structural program and modern OO boundaries.
            "class_start": re.compile(
                r"^(?:[0-9a-zA-Z \t]{6}[ \-]?)?[ \t]*(?:PROGRAM-ID|CLASS-ID|INTERFACE-ID|FACTORY|OBJECT)\.\s+([A-Za-z0-9_-]+)(?=[ \t]*\.|\n|$)",
                re.I | re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety: Cyan Fortification. Defensive scope terminators and declarative blocks.
            "safety": re.compile(
                r"\b(END-IF|END-PERFORM|END-EVALUATE|END-READ|END-WRITE|END-COMPUTE|END-CALL|DECLARATIVES|VALIDATE|CHECK)\b",
                re.I,
            ),
            # 7. safety_neg: Fractures. Bypassing logic or unpredictable jumps.
            "safety_neg": re.compile(
                r"\b(NEXT\s+SENTENCE|GO\s+TO|CORRESPONDING|ANY\s+LENGTH|OMITTED)\b",
                re.I,
            ),
            # 8. danger: Heavy Load. Process-stopping commands and self-modifying code (ALTER).
            "danger": re.compile(r"\b(STOP\s+RUN|ALTER|CANCEL)\b", re.I),
            # 9. io: Boundaries. Disk, Database (SQL), and CICS communication.
            "io": re.compile(
                r"\b(READ|WRITE|REWRITE|OPEN|CLOSE|START|DELETE|EXEC\s+SQL|EXEC\s+CICS\s+(?:READ|WRITE|REWRITE|DELETE))\b",
                re.I,
            ),
            # 10. api: Event Horizon. Exposed linkage points and external entries.
            "api": re.compile(
                r"\b(ENTRY|LINKAGE\s+SECTION|CALL|INVOKE|EXPORT)\b", re.I
            ),
            # 11. flux: Boiling Plasma. State mutation (The core of COBOL data manipulation).
            "flux": re.compile(
                r"\b(MOVE|COMPUTE|ADD|SUBTRACT|MULTIPLY|DIVIDE|SET|INITIALIZE|REPLACE|STRING|UNSTRING)\b",
                re.I,
            ),
            # 12. graveyard: Necrosis. Commented out structural logic (Column 7 indicator).
            "graveyard": re.compile(
                r"^(?:.{6}\*|[ \t]*\*>)[ \t]*(?:MOVE|COMPUTE|IF|PERFORM|CALL|EXEC)\b",
                re.I | re.M,
            ),
            # 13. doc: Intent. Identification metadata and structured comments.
            "doc": re.compile(
                r"^(?:[0-9a-zA-Z \t]{6}[ \-]?)?[ \t]*(?:AUTHOR|DATE-WRITTEN|DATE-COMPILED|REMARKS|INSTALLATION)\.|\*>\s*@(?:param|return|author)",
                re.I | re.M,
            ),
            # 14. test: Verification. Unit testing framework markers (ZUnit).
            "test": re.compile(
                r"\b(ZUNIT|CBLUNIT|ASSERT|TEST-CASE|READY\s+TRACE)\b", re.I
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency: Temporal Static. CICS Task and resource coordination.
            "concurrency": re.compile(
                r"\bEXEC\s+CICS\s+(?:ENQ|DEQ|WAIT|START|DELAY)\b", re.I
            ),
            # 16. ui_framework: View Layer. Screen sections and CICS maps.
            "ui_framework": re.compile(
                r"\b(SCREEN\s+SECTION|EXEC\s+CICS\s+SEND\s+MAP|DFHMDF|DFHMDI|DFHMSD)\b",
                re.I,
            ),
            # 17. closures: Functional Depth. (COBOL lacks native lambdas).
            "closures": None,
            # 18. globals: Shared Void. Global storage and external linkages.
            "globals": re.compile(
                r"\b(WORKING-STORAGE\s+SECTION|COMMON|GLOBAL|EXTERNAL)\b", re.I
            ),
            # 19. decorators: Metadata Hooks. (COBOL uses compiler directives).
            "decorators": re.compile(
                r"^(?:[0-9a-zA-Z \t]{6}[ \-]?)?[ \t]*>>\s*(?:IF|ELSE|END-IF|DEFINE|CALL-CONVENTION)",
                re.I | re.M,
            ),
            # 20. generics: Type Abstractions. Parameterized classes (Modern COBOL).
            "generics": re.compile(
                r"\bCLASS-ID\.\s+[A-Za-z0-9_-]+\s+USING\s+[A-Za-z0-9_-]+", re.I
            ),
            # 21. comprehensions: High-Density Loops. (Not native to COBOL).
            "comprehensions": None,
            # 22. scientific: Compute Core. Intrinsic math functions.
            "scientific": re.compile(
                r"\bFUNCTION\s+(?:ACOS|ASIN|ATAN|COS|EXP|FACTORIAL|LOG|LOG10|MOD|RANDOM|SQRT|TAN|VARIANCE)\b",
                re.I,
            ),
            # 23. heat_triggers: Thermal Radiation. Metaprogramming and memory aliasing.
            "heat_triggers": re.compile(
                r"\b(REDEFINES|RENAMES|OCCURS\s+DEPENDING\s+ON|EVALUATE\s+TRUE|EXEC\s+CICS|EXEC\s+SQL)\b",
                re.I,
            ),
            # 24. import: Gravity Links. Copybooks and inclusions.
            "import": re.compile(r"\b(?:COPY|INCLUDE)\s+[A-Za-z0-9_-]+", re.I),
            
            "_dependency_capture": re.compile(r"\b(?:COPY|INCLUDE)\s+['\"]?([A-Za-z0-9_-]+)['\"]?", re.I),
            
            # 25. ownership: Authorship indicators.
            "ownership": re.compile(
                r"^(?:[0-9a-zA-Z \t]{6}[ \-]?)?[ \t]*AUTHOR\.\s+([^\n]+)", re.I | re.M
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            # 26. planned_debt: The Promise. Future work markers.
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            # 27. fragile_debt: The Fracture. Admitted fragility or hacks.
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure: Map vs. Territory. Audit tags.
            "spec_exposure": re.compile(r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)\]", re.I),
            # 30. civil_war: Indentation Tracker. Tabs vs spaces conflict.
            "civil_war": None,  # COBOL fixed format strictly forbids Tabs.
            # 31. ssr_boundaries: View Horizon. CICS web endpoints.
            "ssr_boundaries": re.compile(
                r"\bEXEC\s+CICS\s+(?:WEB\s+SEND|DOCUMENT|WEB\s+READ)\b", re.I
            ),
            # 32. events: Pub/Sub Network. Signal handlers and MQ bindings.
            "events": re.compile(
                r"\b(?:EXEC\s+CICS\s+(?:SIGNAL|HANDLE\s+CONDITION)|CALL\s+\'(?:MQPUT|MQGET)\')\b",
                re.I,
            ),
            # 33. dependency_injection: Inversion of Control.
            "dependency_injection": None,
            # 34. macros: Preprocessor Hooks. DEFINE directives.
            "macros": re.compile(
                r"^(?:[0-9a-zA-Z \t]{6}[ \-]?)?[ \t]*DEFINE\s+[A-Z0-9_-]+\.|>>DEFINE",
                re.I | re.M,
            ),
            # 35. pointers: Memory Map. Explicit pointer tracking.
            "pointers": re.compile(
                r"\b(?:POINTER|PROCEDURE-POINTER|FUNCTION-POINTER)\b|\bADDRESS\s+OF\b",
                re.I,
            ),
            # 36. memory_alloc: Manual Memory Management. Heap and CICS allocation.
            "memory_alloc": re.compile(
                r"\b(?:ALLOCATE|FREE|EXEC\s+CICS\s+(?:GETMAIN|FREEMAIN))\b", re.I
            ),
            # 37. inline_asm: Bare Metal.
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry: Professional diagnostics.
            "telemetry": re.compile(
                r"\b(?:EXEC\s+CICS\s+WRITEQ\s+TD|CEE3DMP|CEEMOUT|CEEDUMP)\b", re.I
            ),
            # 39. print_hits: Amateur space debris.
            "print_hits": re.compile(r"\b(DISPLAY)\b", re.I),
            # 40. cast_hits: Trust Me Tax. REDEFINES is the implicit COBOL cast.
            "cast_hits": re.compile(r"\b(REDEFINES)\b", re.I),
            # 41. bailout_hits: Detonators. Aborting execution.
            "bailout_hits": re.compile(r"\b(STOP\s+RUN|EXIT\s+PROGRAM|GOBACK)\b", re.I),
            # 42. halt_hits: Temporal Duct Tape. (Forced waits).
            "halt_hits": re.compile(r"\bEXEC\s+CICS\s+DELAY\b", re.I),
            # 43. bitwise_hits: Sub-Atomic Math. (Modern intrinsic bitwise).
            "bitwise_hits": re.compile(
                r"\bFUNCTION\s+(?:BIT-AND|BIT-OR|BIT-XOR|BIT-NOT)\b", re.I
            ),
            # 44. sync_locks: Barricades.
            "sync_locks": re.compile(r"\bEXEC\s+CICS\s+ENQ\b", re.I),
            # 45. freeze_hits: Data Cryogenics. Immutability.
            "freeze_hits": re.compile(r"\b(CONSTANT)\b", re.I),
            # 46. cleanup: The Janitor. Resource release.
            "cleanup": re.compile(r"\b(CLOSE|FREE|END-DECLARATIVES)\b", re.I),
            # 47. encapsulation: The Vault. Scope hiding.
            "encapsulation": re.compile(r"\b(LOCAL-STORAGE\s+SECTION|PRIVATE)\b", re.I),
            # 48. listeners: The Sinks.
            "listeners": re.compile(r"\b(?:MQGET|EXEC\s+CICS\s+RECEIVE)\b", re.I),
            # 49. test_skip: Safety Theater.
            "test_skip": re.compile(r"\b(IGNORE)\b", re.I),
        },
    },
    "zig": {
        "_meta": {
            "target_version": "Zig 0.15.2 (Modern Comptime, Explicit Allocators, Error Sets)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard sources and Zig Object Notation (ZON) files which are structurally Zig AST.
        "extensions": [".zig", ".zon"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: The pure-code build scripts that act as the architectural anchors of a Zig project.
        "exact_matches": ["build.zig", "build.zig.zon"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Zig's build system files ensure that ambiguous contexts are locked in perfectly.
        "discriminators": [".zig", "build.zig", "build.zig.zon"],
        # EXECUTION SIGNATURES: Zig is compiled, but `zig run` can be invoked via shebang in scripting scenarios.
        "shebangs": ["zig"],
        # UPGRADED: Maps to Family 8 (Singular/Unique)
        # Rationale: Zig intentionally omits multi-line block comments to keep parsing simple, exclusively using '//'.
        "lexical_family": "singular",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            "_line_anchor": re.compile(r"//"),
            "_inline_comment": re.compile(r"//"),
            "_block_start": None,
            "_block_end": None,
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch: decisions that split flow. Includes unique 'orelse' and 'catch' patterns.
            "branch": re.compile(
                r"\b(if|else|switch|while|for|try|catch|orelse|break|continue|return)\b|&&|\|\|"
            ),
            # 2. args: Coupling Mass. Captures parameters in function signatures.
            "args": re.compile(r"\bfn\s*(?:[a-zA-Z_]\w*\s*)?\([^)]*\)"),
            # 3. linear: Smooth Path. Structural boundaries. EXCLUDES access modifiers and const (freeze_hits).
            "linear": re.compile(
                r"\b(var|return|defer|errdefer|unreachable|resume|suspend|await|nosuspend|usingnamespace)\b"
            ),
            # 4. func_start: Satellite Spawner. Anchors logic blocks (fn). EXCLUDES struct/enum/union headers.
            "func_start": re.compile(
                r"^[ \t]*(?:(?:pub|export|extern|inline|noinline|callconv\([^)]*\))[ \t]+){0,5}fn\s+([a-zA-Z_]\w*)(?=\s*\()",
                re.M,
            ),
            # 5. class_start: Entity Census. Defines structural entities (struct, enum, union, error, opaque).
            "class_start": re.compile(
                r"^[ \t]*(?:pub[ \t]+)?const[ \t]+([a-zA-Z_]\w*)[ \t]*=[ \t]*(?:packed[ \t]+|extern[ \t]+)?(?:struct|enum|union|error|opaque)(?=[ \t]*[{(])",
                re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety: Cyan Fortification. Error handling, payload capturing (|val|), and debug assertions.
            "safety": re.compile(
                r"\b(try|catch|orelse|errdefer|std\.debug\.assert)\b|\|[ \t]*[a-zA-Z_]\w*[ \t]*\|"
            ),
            # 7. safety_neg: Fractures. Bypassing safety (undefined, unreachable, raw ptr casting).
            "safety_neg": re.compile(
                r"\b(undefined|unreachable|@ptrCast|@intCast|@alignCast|@bitCast|@truncate|@enumFromInt)\b"
            ),
            # 8. danger: Heavy Load. Forceful panics and process terminations.
            "danger": re.compile(r"\b(@panic|panic|std\.process\.exit)\b"),
            # 9. io: Boundaries. Standard library IO, Network, and Filesystem interactions.
            "io": re.compile(
                r"\b(std\.fs|std\.net|std\.io(?!\.getStdOut)|std\.ChildProcess|std\.posix|std\.os)\b"
            ),
            # 10. api: Event Horizon. Exposed boundaries via 'pub' and 'export' (C ABI).
            "api": re.compile(r"\b(pub|export)\b"),
            # 11. flux: Boiling Plasma. State mutation (var) and pointer dereference assignments (.* =).
            "flux": re.compile(r"\bvar\b|\.\*[ \t]*=[^=]"),
            # 12. graveyard: Necrosis. Commented out structural code.
            "graveyard": re.compile(
                r"//[ \t]*(?:fn|const|var|pub|if|for|while|try|catch)\b"
            ),
            # 13. doc: Intent. Structured documentation (/// and //!).
            "doc": re.compile(r"///|//!"),
            # 14. test: Verification. Native test framework blocks.
            "test": re.compile(
                r'\b(test\s+"[^"]*"|test\s+[a-zA-Z_]\w*|std\.testing\.expect|std\.testing\.expectEqual)\b'
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency: Temporal Static. Suspend/resume and thread primitives.
            "concurrency": re.compile(
                r"\b(std\.Thread|std\.Thread\.Mutex|std\.Thread\.RwLock|std\.atomic|@atomicLoad|@atomicStore|@atomicRmw|suspend|resume|await)\b"
            ),
            # 16. ui_framework: View Layer. (Zig lacks native UI; targets common bindings like Mach/zgui).
            "ui_framework": re.compile(
                r"\b(mach\.|zgui\.|zopengl\.|capy\.|vaxis\.|raylib\.)\b"
            ),
            # 17. closures: Functional Depth. (Zig lacks traditional anonymous closures).
            "closures": None,
            # 18. globals: Shared Void. Top-level file-scoped state.
            "globals": re.compile(
                r"^[ \t]*(?:pub[ \t]+)?(?:threadlocal[ \t]+)?(?:comptime[ \t]+)?(?:const|var)\s+[a-zA-Z_]\w*\s*(?::[^=]+)?=",
                re.M,
            ),
            # 19. decorators: Metadata Hooks. (Zig uses @builtins instead).
            "decorators": None,
            # 20. generics: Type Abstractions. Comptime parameters and 'anytype' duck typing.
            "generics": re.compile(
                r"\b(anytype|type)\b|\bcomptime\s+[a-zA-Z_]\w*\s*:\s*type\b"
            ),
            # 21. comprehensions: High-Density Loops. (Not native to Zig).
            "comprehensions": None,
            # 22. scientific: Compute Core. Math intrinsics and SIMD @Vector support.
            "scientific": re.compile(
                r"\b(std\.math|@Vector|f16|f32|f64|f80|f128|@sqrt|@sin|@cos|@splat|@reduce)\b"
            ),
            # 23. heat_triggers: Thermal Radiation. Comptime metaprogramming and reflection.
            "heat_triggers": re.compile(
                r"\b(comptime[ \t]*\{|inline\s+for|inline\s+while|@Type|@typeInfo|@compileLog|@hasDecl|@hasField)\b"
            ),
            # 24. import: Gravity Links. Module and C-header bridges.
            "import": re.compile(r"\b(@import|@cImport|@cInclude)\b"),
            
            "_dependency_capture": re.compile(r"\b(?:@import|@cInclude)\s*\(\s*['\"]([^'\"]+)['\"]", re.M),
            
            # 25. ownership: Authorship indicators in comments.
            "ownership": re.compile(
                r"//\s*(?:Author|Created by|Maintainer|Copyright):\s+([^\n]+)", re.I
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            # 26. planned_debt: The Promise. Future work markers.
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            # 27. fragile_debt: The Fracture. Admitted fragility or hacks.
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure: Map vs. Territory. Audit tags.
            "spec_exposure": re.compile(r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)\]", re.I),
            # 30. civil_war: Indentation Tracker. Tabs vs 4-space standardization.
            "civil_war": None,
            # 31. ssr_boundaries: View Horizon. Zap/httpz response handlers.
            "ssr_boundaries": re.compile(
                r"\b(zap\.Endpoint|zap\.Request|httpz\.Request|std\.http\.Server\.Request)\b"
            ),
            # 32. events: Pub/Sub Network. OS-level event loops.
            "events": re.compile(
                r"\b(std\.posix\.epoll_wait|std\.posix\.kevent|xev\.Loop)\b"
            ),
            # 33. dependency_injection: Inversion of Control.
            "dependency_injection": None,
            # 34. macros: Preprocessor Hooks. (Zig lacks macros).
            "macros": None,
            # 35. pointers: Memory Map. Explicit pointer tracking.
            "pointers": re.compile(
                r"(?<=[=\s,(])\*(?:const\s+|volatile\s+|allowzero[ \t]+)?[a-zA-Z_]\w*|\[\*c?\][a-zA-Z_]\w*|\.\*"
            ),
            # 36. memory_alloc: Manual Memory Management. Allocators bypassing the GC.
            "memory_alloc": re.compile(
                r"\b(std\.mem\.Allocator|allocator\.alloc|allocator\.free|allocator\.create|ArenaAllocator|c_allocator|page_allocator)\b"
            ),
            # 37. inline_asm: Bare Metal.
            "inline_asm": re.compile(r"\basm\b(?:\s+volatile)?\s*\([^)]+\)"),
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry: Professional diagnostics.
            "telemetry": re.compile(
                r"\b(?:std\.log\.(?:info|err|warn|debug)|std\.log\.scoped)\b"
            ),
            # 39. print_hits: Amateur space debris.
            "print_hits": re.compile(r"\b(std\.debug\.print)\b"),
            # 40. cast_hits: "Trust Me" Tax. Explicit casting.
            "cast_hits": re.compile(r"\b(@ptrCast|@intCast|@alignCast|@bitCast|@as)\b"),
            # 41. bailout_hits: Detonators. Aborting context.
            "bailout_hits": re.compile(r"\b(@panic|unreachable|return)\b"),
            # 42. halt_hits: Temporal Duct Tape. (Forced waits/sleep).
            "halt_hits": re.compile(r"\b(std\.time\.sleep)\b"),
            # 43. bitwise_hits: Sub-Atomic Math.
            "bitwise_hits": re.compile(r"(?<!&)&(?!&)|(?<!\|)\|(?!\|)|<<|>>|\^|~"),
            # 44. sync_locks: Barricades. Coordinated threading.
            "sync_locks": re.compile(r"\b(Mutex|RwLock|Semaphore|lock|unlock)\b"),
            # 45. freeze_hits: Data Cryogenics. Immutability.
            "freeze_hits": re.compile(r"\bconst\b"),
            # 46. cleanup: The Janitor. Resource release.
            "cleanup": re.compile(r"\b(deinit|free|destroy|allocator\.free)\b"),
            # 47. encapsulation: The Vault. Scope hiding (Lack of pub).
            "encapsulation": re.compile(
                r"^[ \t]*(?!(?:pub|export|extern)\b)(?:const|var|fn)\s+", re.M
            ),
            # 48. listeners: The Sinks.
            "listeners": None,
            # 49. test_skip: Safety Theater.
            "test_skip": re.compile(r"\b(std\.testing\.expect|assume|expectError)\b"),
        },
    },
    "apex": {
        "_meta": {
            "target_version": "Salesforce Apex 24.2 (API v62.0+)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard Salesforce classes and database triggers.
        "extensions": [".cls", ".trigger"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Apex code lives and executes on the Salesforce platform; no extensionless configurations exist.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: .cls is highly contested. Salesforce metadata XMLs and SFDX configs act as absolute gravity anchors.
        "discriminators": [
            ".cls-meta.xml",
            ".trigger-meta.xml",
            "sfdx-project.json",
            "package.xml",
        ],
        # EXECUTION SIGNATURES: Executed exclusively on the Salesforce platform; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 1 (Standard C-Style)
        # Rationale: Uses standard '//' for lines and '/*' '*/' for block-level Ghost Mass.
        "lexical_family": "std_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            "_line_anchor": re.compile(r"//"),
            "_inline_comment": re.compile(r"//"),
            "_block_start": re.compile(r"/\*"),
            "_block_end": re.compile(r"\*/"),
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch: decisions that split flow. Includes switch on/when and DML try-catch.
            "branch": re.compile(
                r"\b(if|else|switch\s+on|when|for|while|do|try|catch|finally|break|continue|return)\b|&&|\|\||\?|\?\?",
                re.I,
            ),
            # 2. args: Coupling Mass. Captures method parameters and trigger event signatures.
            "args": re.compile(
                r"\b[a-z_]\w*(?:<[^>]*>)?\s+[a-z_]\w*\s*\([^)]*\)|\btrigger\s+[a-z_]\w*\s+on\s+[a-z_]\w*\s*\([^)]*\)",
                re.I,
            ),
            # 3. linear: Smooth Path. Structural boundaries. EXCLUDES access modifiers and sharing keywords.
            "linear": re.compile(
                r"\b(class|interface|trigger|enum|final|transient|implements|extends|virtual|abstract|return)\b",
                re.I,
            ),
            # 4. func_start (The Satellite Spawner)
            # ReDoS clamped to {0,5}. Strict capture groups and lookaheads for both Methods and Triggers.
            "func_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]+){0,5}"
                r"(?:(?:public|private|global|protected|static|override|virtual|abstract|testMethod)[ \t]+){0,5}"
                r"(?:[\w<>\[\]?]+[ \t]+)?(?!(?:class|interface|enum|if|for|while|switch|catch)\b)([a-zA-Z_]\w*)(?=\s*\()|"
                r"^[ \t]*trigger\s+([a-zA-Z_]\w*)(?=\s+on\b)",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            # ReDoS clamped. Strict capture group and positive lookahead applied.
            "class_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]+){0,5}"
                r"(?:(?:public|private|global|virtual|abstract|with\s+sharing|without\s+sharing|inherited\s+sharing)[ \t]+){0,5}"
                r"(?:class|interface|enum)\s+([a-zA-Z_]\w*)(?=\s+implements|\s+extends|\s*\{|\n|$)",
                re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety: Cyan Fortification. Sharing rules, FLS checks, and null-safe navigation.
            "safety": re.compile(
                r"\b(with\s+sharing|inherited\s+sharing|isAccessible|isCreateable|isUpdateable|isDeletable|StripInaccessible|try|catch|finally|LIMIT\s+\d+|Security\.stripInaccessible)\b|\?\.",
                re.I,
            ),
            # 7. safety_neg: Fractures. Actively bypassing safety (without sharing, raw casting).
            "safety_neg": re.compile(
                r"\b(without\s+sharing|Database\.query(?!\s*\(.*?WITH\s+SECURITY_ENFORCED)|@SuppressWarnings)\b|\(\s*[A-Z_]\w*\s*\)\s*[a-z_]\w*",
                re.I,
            ),
            # 8. danger: Heavy Load. Dynamic SOQL, mass deletion, and hardcoded IDs.
            "danger": re.compile(
                r"\b(Database\.query|delete|undelete|emptyRecycleBin|purgeOldAsyncJobs)\b|\'[a-z0-9]{15,18}\'",
                re.I,
            ),
            # 9. io: Boundaries. SOQL/SOSL queries, HTTP callouts, and batch boundaries.
            "io": re.compile(
                r"\[\s*(?:SELECT|FIND)\b[^\]]*\]|\b(Http|HttpRequest|HttpResponse|Database\.executeBatch|HTLoad|HTGet|ENQUIRE)\b",
                re.I,
            ),
            # 10. api: Event Horizon. Exposed global interfaces, REST resources, and UI hooks.
            "api": re.compile(
                r"\b(global|webservice)\b|@(?:RestResource|HttpGet|HttpPost|HttpPut|HttpDelete|HttpPatch|AuraEnabled|InvocableMethod|RemoteAction)\b",
                re.I,
            ),
            # 11. flux: Boiling Plasma. State mutation (DML operations and standard assignments).
            "flux": re.compile(
                r"\b(insert|update|upsert|delete|merge)\b|^[ \t]*(?:this\.)?[a-z_]\w*\s*[-+*/%]?=|\.(?:add|addAll|remove|put|clear|set)\s*\(",
                re.I | re.M,
            ),
            # 12. graveyard: Necrosis. Commented out structural code or queries.
            "graveyard": re.compile(
                r"//[ \t]*(?:class|trigger|public|private|if|for|while|System\.debug|\[\s*SELECT|insert|update)\b|/\*[ \t]*(?:class|trigger|\[\s*SELECT)",
                re.I | re.M,
            ),
            # 13. doc: Intent. ApexDoc annotations and metadata blocks.
            "doc": re.compile(
                r"/\*\*|@description|@param|@return|@author|@date|@example", re.I
            ),
            # 14. test: Verification. Salesforce test execution and assertion markers.
            "test": re.compile(
                r"@isTest|@TestSetup|@TestVisible|\b(?:Test\.startTest|Test\.stopTest|System\.assert|Assert\.(?:isTrue|isNotNull|areEqual)|Test\.setMock)\b",
                re.I,
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency: Temporal Static. Asynchronous Apex (Future, Queueable, Batch).
            "concurrency": re.compile(
                r"@future|\b(Queueable|Schedulable|Batchable|System\.enqueueJob|Database\.executeBatch|System\.schedule)\b",
                re.I,
            ),
            # 16. ui_framework: View Layer. Visualforce and LWC bridge components.
            "ui_framework": re.compile(
                r"\b(ApexPages|PageReference|StandardController|Dom\.Document|SGML|HyperText|WorldWideWeb|BrowserView)\b",
                re.I,
            ),
            # 17. closures: Functional Depth. (Apex lacks true anonymous closures).
            "closures": None,
            # 18. globals: Shared Void. Custom Settings, Organization data, and User context.
            "globals": re.compile(
                r"\b(UserInfo|System\.Label|Organization|Cache\.Org|Cache\.Session)\b|\w+__c\.getInstance\b|\w+__mdt\.getInstance\b",
                re.I,
            ),
            # 19. decorators: Metadata Hooks. Execution context annotations.
            "decorators": re.compile(r"@[a-z_]\w*(?:\([^)]*\))?", re.I),
            # 20. generics: Type Abstractions. Parameterized collections (List, Map, Set).
            "generics": re.compile(
                r"\b(?:List|Set|Map|Iterable|Iterator)\s*<\s*[a-z_][^>]*>", re.I
            ),
            # 21. comprehensions: High-Density Loops. Inline SOQL for-loops act as mappers.
            "comprehensions": re.compile(
                r"\bfor\s*\([^)]+:\s*\[\s*SELECT[^\]]+\]\s*\)", re.I
            ),
            # 22. scientific: Compute Core. Standard numerical and currency math.
            "scientific": re.compile(
                r"\b(Math\.(?:abs|sin|cos|tan|exp|log|pow|sqrt)|Decimal|setScale|setRoundingMode)\b",
                re.I,
            ),
            # 23. heat_triggers: Thermal Radiation. Dynamic SOQL, Reflection, and Describe calls.
            "heat_triggers": re.compile(
                r"\b(Database\.query|Type\.forName|Schema\.getGlobalDescribe|Schema\.describeSObjects|SObject\.put|SObject\.get|JSON\.deserializeUntyped)\b",
                re.I,
            ),
            # 24. import: Gravity Links. (Apex classes occupy a global org namespace).
            "import": None,
            
            "_dependency_capture": None,
            
            # 25. ownership: Authorship indicators.
            "ownership": re.compile(
                r"(?:@author|Author|Created by|Maintainer|Copyright|Tim Berners-Lee):\s+([^\n]+)",
                re.I | re.M,
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            # 26. planned_debt: The Promise. Future work markers.
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            # 27. fragile_debt: The Fracture. Admitted fragility or hacks.
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure: Map vs. Territory. Audit tags and architecture specs.
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)\]|\b(?:WorldWideWeb|RFC|W3C|CERN|TBL|ENQUIRE)\b",
                re.I,
            ),
            # 30. civil_war: Indentation Tracker. Tabs vs 4-space standardization.
            "civil_war": None,
            # 31. ssr_boundaries: View Horizon. REST and Visualforce response handlers.
            "ssr_boundaries": re.compile(
                r"\b(RestContext\.request|RestContext\.response|RestRequest|RestResponse|renderAs)\b",
                re.I,
            ),
            # 32. events: Pub/Sub Network. Platform Events and Trigger context.
            "events": re.compile(
                r"\b(EventBus\.publish|PlatformEvent)\b|trigger\s+[A-z_]\w+\s+on\s+[A-z_]\w+Event__e",
                re.I,
            ),
            # 33. dependency_injection: Inversion of Control. Mocking and injection frameworks.
            "dependency_injection": re.compile(
                r"\b(fflib_ApexMocks|fflib_SObjectUnitOfWork|Injector|di_Injector|Application\.Service|Type\.newInstance)\b",
                re.I,
            ),
            # 34. macros: Preprocessor Hooks. (Apex lacks a preprocessor).
            "macros": None,
            # 35. pointers: Memory Map. (Apex is fully managed with no pointers).
            "pointers": None,
            # 36. memory_alloc: Manual Memory Management. Heap observations.
            "memory_alloc": re.compile(
                r"\b(Limits\.getHeapSize|Limits\.getLimitHeapSize|new\s+[a-z_]\w*)\b",
                re.I,
            ),
            # 37. inline_asm: Bare Metal.
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry: Professional diagnostics (Structured logs).
            "telemetry": re.compile(
                r"\b(Logger|Log|AppLog|NebulaLogger)\.(?:info|error|warn|debug|trace)\b|\binsert\s+new\s+Log__c\b",
                re.I,
            ),
            # 39. print_hits: Amateur space debris.
            "print_hits": re.compile(r"\b(System\.debug)\b", re.I),
            # 40. cast_hits: "Trust Me" Tax. Explicit type coercion.
            "cast_hits": re.compile(
                r"\(\s*(?:[A-Z]\w*|int|Id|String|Decimal|Boolean|Double|Long|Blob|Date|Datetime|Time)\s*\)\s*[a-zA-Z_$]"
            ),
            # 41. bailout_hits: Detonators. Aborting execution or rollback.
            "bailout_hits": re.compile(
                r"\b(throw|Database\.rollback|purgeOldAsyncJobs)\b", re.I
            ),
            # 42. halt_hits: Temporal Duct Tape. (Apex has no native sleep/delay).
            "halt_hits": None,
            # 43. bitwise_hits: Sub-Atomic Math.
            "bitwise_hits": re.compile(r"(?<!&)&(?!&)|(?<!\|)\|(?!\|)|<<|>>|\^|~"),
            # 44. sync_locks: Barricades. Row-level SOQL locking.
            "sync_locks": re.compile(r"\bFOR\s+UPDATE\b", re.I),
            # 45. freeze_hits: Data Cryogenics. Immutability (constants).
            "freeze_hits": re.compile(r"\b(static\s+final|final|const)\b", re.I),
            # 46. cleanup: The Janitor. Recycle bin management.
            "cleanup": re.compile(
                r"\b(emptyRecycleBin|Database\.rollback|clear)\s*\(", re.I
            ),
            # 47. encapsulation: The Vault. Scope hiding.
            "encapsulation": re.compile(r"\b(private|protected)\b", re.I),
            # 48. listeners: The Sinks. Triggers listening for events.
            "listeners": re.compile(r"^[ \t]*trigger\s+[a-z_]\w*\s+on\b", re.I | re.M),
            # 49. test_skip: Safety Theater.
            "test_skip": re.compile(
                r"\b(StubProvider|Test\.setMock|@SuppressWarnings)\b", re.I
            ),
        },
    },
    "dart": {
        "_meta": {
            "target_version": "Dart 3.11 (Records, Patterns, Class Modifiers, Macros, FFI)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard Dart sources.
        "extensions": [".dart"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Dart rarely uses extensionless configurations.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, pub package manifests, and analyzer configurations to anchor Flutter/Dart projects.
        "discriminators": [
            ".dart",
            "pubspec.yaml",
            "pubspec.lock",
            "analysis_options.yaml",
            ".metadata",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1 for standalone Dart scripting.
        "shebangs": ["dart"],
        # UPGRADED: Maps to Family 2 (Nested C)
        # Rationale: (CORRECTION) Like Swift and Rust, Dart officially supports nested multi-line
        # comments (/* /* */ */). Standard C parsing would prematurely terminate here causing geometry failure.
        "lexical_family": "std_c",
        "rules": {
            "_block_start": re.compile(r"/\*"),
            "_block_end": re.compile(r"\*/"),
            "_line_anchor": re.compile(r"//"),
            "_inline_comment": re.compile(r"//"),
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch: decisions that split flow. Includes modern pattern guards (when) and null-coalescing.
            "branch": re.compile(
                r"\b(if|else|switch|case|default|for|while|do|try|catch|finally|break|continue|when)\b|&&|\|\||\?|\?\?",
                re.I,
            ),
            # 2. args: Coupling Mass. Captures parameters in function, method, and lambda signatures.
            "args": re.compile(
                r"\b[A-Za-z_$][\w$]*(?:<[^>]*>)?\s*\([^)]*\)|\([^)]*\)\s*(?:=>|\{)",
                re.I,
            ),
            # 3. linear: Smooth Path. Structural boundaries. EXCLUDES access modifiers and const/final.
            "linear": re.compile(
                r"\b(var|late|return|yield|await|class|mixin|extension|enum|typedef|import|export|part|library|base|sealed|interface|macro)\b|=>",
                re.I,
            ),
            # 4. func_start (The Satellite Spawner)
            # ReDoS clamped to {0,5}. Strict capture group and positive lookahead applied.
            "func_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]+){0,5}"
                r"(?:(?:static|external|abstract|covariant|late)[ \t]+){0,5}"
                r"(?:[\w<>\[\]?]+[ \t]+)?(?!(?:class|mixin|enum|extension|typedef|if|for|while|switch|catch)\b)"
                r"(?:get\s+|set\s+|factory\s+|operator\s+\S+\s*)?([a-zA-Z_]\w*)(?=\s*\()",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            # ReDoS clamped. Strict capture group and positive lookahead applied.
            "class_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]+){0,5}"
                r"(?:abstract[ \t]+)?(?:sealed[ \t]+)?(?:base[ \t]+)?(?:interface[ \t]+)?(?:final[ \t]+)?(?:macro[ \t]+)?"
                r"(?:class|mixin|enum|extension\s+type|extension)\s+([A-Z]\w*)(?=[ \t]*[{<]|\n|$)",
                re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety: Cyan Fortification. Null safety boundaries, type assertions, and required parameters.
            "safety": re.compile(
                r"\b(try|catch|finally|on\s+[A-Z]\w*|assert|required|late|is|!is|SafeArea|@immutable|@mustCallSuper)\b|\?\?|\?.",
                re.I,
            ),
            # 7. safety_neg: Fractures. Actively bypassing sound null safety or static analysis.
            "safety_neg": re.compile(
                r"!\s*[;,\n)\.\]]|\bdynamic\b|//\s*ignore(?:_for_file)?:\s*\w+"
            ),
            # 8. danger: Heavy Load. Process killers and catastrophic exit commands.
            "danger": re.compile(r"\b(exit|exitCode|Process\.killPid)\b", re.I),
            # 9. io: Boundaries. Disk, Network, WebSockets, and Uri parsing (Includes legacy CERN triggers).
            "io": re.compile(
                r"\b(File|Directory|HttpClient|HttpServer|ServerSocket|WebSocket|Uri\.parse|HtmlDocument|HttpRequest|HttpResponse|HTRequest|Nexus|ENQUIRE)\b",
                re.I,
            ),
            # 10. api: Event Horizon. Exposed visibility (Lack of _ prefix) and routing decorators.
            "api": re.compile(
                r"\b(export|part\s+of)\b|@(Route|Get|Post|Mapping|visibleForTesting|pragma)\b|^[ \t]*(?:class|mixin|enum|extension|typedef)\s+(?![_])[A-Za-z]\w*",
                re.I | re.M,
            ),
            # 11. flux: Boiling Plasma. State mutation (setState and reactive collection mutators).
            "flux": re.compile(
                r"\b(setState|notifyListeners|markNeedsBuild|StreamController\.add)\b|[^!=<>\+\-\*\/%&\|\s]=\s*[^=]|(?:\+\+|--)|\.(?:add|addAll|remove|insert|clear|update)\s*\(",
                re.I,
            ),
            # 12. graveyard: Necrosis. Commented out structural code or dead widgets.
            "graveyard": re.compile(
                r"//[ \t]*(?:class|mixin|void|if|for|while|print|Widget|return)\b|/\*[ \t]*(?:class|mixin|void|Widget|if|for)"
            ),
            # 13. doc: Intent. dartdoc annotations and structured comments.
            "doc": re.compile(r"///|/\*\*|@param|@return"),
            # 14. test: Verification. Flutter test frameworks and standard expect/verify markers.
            "test": re.compile(
                r"\b(?:test|testWidgets|group|setUp|tearDown|pumpWidget|pumpAndSettle|find\.(?:byType|text|byKey))\b|\b(?:expect|verify|when)\s*\("
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency: Temporal Static. Event Loop primitives (Future, Stream, Isolate).
            "concurrency": re.compile(
                r"\b(async|async\*|sync\*|await|Future|Stream|Isolate|ReceivePort|SendPort|Completer|Timer|StreamSubscription)\b",
                re.I,
            ),
            # 16. ui_framework: View Layer. Flutter Component trees and DOM nodes (Includes TBL triggers).
            "ui_framework": re.compile(
                r"\b(Widget|BuildContext|StatefulWidget|Scaffold|Container|Text|HtmlElementView|RichText|Hyperlink|SGML|HyperText|Browser)\b",
                re.I,
            ),
            # 17. closures: Functional Depth. Fat-arrows and anonymous function blocks.
            "closures": re.compile(r"=>|\(\s*[^)]*\)\s*(?:async\*?|sync\*?)?[ \t]*\{"),
            # 18. globals: Shared Void. Static class fields and environmental bindings.
            "globals": re.compile(
                r"\b(static\s+final|static\s+const|Platform\.environment|window\.|Zone\.current)\b|^[ \t]*(?:final|const|var)\s+[A-Za-z_$][\w$]*[ \t]*=",
                re.I | re.M,
            ),
            # 19. decorators: Metadata Hooks. Annotations applied to methods/classes.
            "decorators": re.compile(r"@[A-Za-z_$][\w$]*(?:\([^)]*\))?"),
            # 20. generics: Type Abstractions. Parameterized collections and generic classes.
            "generics": re.compile(r"<\s*[A-Z][^>]*>"),
            # 21. comprehensions: High-Density Loops. Collection for/if and functional pipelines.
            "comprehensions": re.compile(
                r"\[\s*(?:for|if)\s*\([^)]*\)|\{\s*(?:for|if)\s*\([^)]*\)|\.(?:map|where|reduce|fold|expand|every|any)\s*\("
            ),
            # 22. scientific: Compute Core. math.pi, typed binary arrays, and Matrix4 vectors.
            "scientific": re.compile(
                r"\b(math\.sin|math\.cos|math\.sqrt|math\.pi|dart:math|Float64List|Float32List|Int32List|Uint8List|Vector2|Vector3|Matrix4)\b",
                re.I,
            ),
            # 23. heat_triggers: Thermal Radiation. Reflection, Native Bridges, and code generation markers.
            "heat_triggers": re.compile(
                r'\b(MethodChannel|EventChannel|dart:mirrors|reflect|reflectClass|noSuchMethod|dart:js_interop)\b|part\s+[\'"][^\'"]+\.(?:g|freezed)\.dart[\'"]',
                re.I,
            ),
            # 24. import: Gravity Links. Dependency resolution and library partitions.
            "import": re.compile(
                r'^[ \t]*(?:import|export|part|part\s+of)\b\s*[\'"][^\'"]+[\'"]', re.M
            ),
            
            "_dependency_capture": re.compile(r"^[ \t]*(?:import|export|part(?:[ \t]+of)?)\b[ \t]*['\"]([^'\"]+)['\"]", re.M),
            
            # 25. ownership: Authorship indicators.
            "ownership": re.compile(
                r"//\s*(?:Author|Created by|Maintainer|Copyright):\s+([^\n]+)", re.I
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            # 26. planned_debt: The Promise. Future work markers.
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            # 27. fragile_debt: The Fracture. Admitted fragility or hacks.
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure: Map vs. Territory. Audit tags and architecture specs.
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit|RFC|W3C|CERN|TBL|ENQUIRE)[^\]]*\]|\b(?:Tim\s+Berners-Lee|WorldWideWeb|HyperText\s+Proposal)\b",
                re.I,
            ),
            # 30. civil_war: Indentation Tracker. Tabs vs 2-space standardization.
            "civil_war": None,
            # 31. ssr_boundaries: View Horizon. shelf/Serverpod response handlers.
            "ssr_boundaries": re.compile(
                r"\b(shelf|dart_frog|Serverpod|Response\.(?:ok|internalServerError)|RequestContext|Router\(\)|Handler|Serve|renderHtml)\b",
                re.I,
            ),
            # 32. events: Pub/Sub Network. Stream subscriptions and broadcast observables.
            "events": re.compile(
                r"\b(StreamController|EventBus|Subject|BehaviorSubject|PublishSubject|EventEmitter|BlocProvider|notifyListeners)\b|\.listen\s*\(",
                re.I,
            ),
            # 33. dependency_injection: Inversion of Control. GetIt, Provider, and Injectable markers.
            "dependency_injection": re.compile(
                r"\b(GetIt\.I|GetIt\.instance|Provider\.of|ConsumerWidget|ref\.watch|ref\.read|Injector|@injectable)\b",
                re.I,
            ),
            # 34. macros: Preprocessor Hooks. Modern macros and JsonSerializable generators.
            "macros": re.compile(
                r"\bmacro\s+class\b|@(?!(?:override|deprecated|required|protected|visibleForTesting|pragma|immutable))[A-Z]\w*Macro\(\)|@JsonSerializable|@freezed",
                re.I,
            ),
            # 35. pointers: Memory Map. dart:ffi bridging to native memory space.
            "pointers": re.compile(
                r"\b(dart:ffi|Pointer<|NativeFunction<|Opaque|ffi\.cast|IntPtr|ffi\.Pointer)\b",
                re.I,
            ),
            # 36. memory_alloc: Manual Memory Management. Allocators bypassing the GC.
            "memory_alloc": re.compile(
                r"\b(ffi\.Allocator|malloc\.allocate|calloc\.allocate|malloc\.free|Arena|using\s*\(\s*\(Arena)\b",
                re.I,
            ),
            # 37. inline_asm: Bare Metal.
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry: Professional diagnostics (Structured logs).
            "telemetry": re.compile(
                r"\b(developer\.log|Logger|log|FirebaseCrashlytics|Sentry)\.(?:info|error|warn|severe|debug|trace|recordError)\b|\bdart:developer\b",
                re.I,
            ),
            # 39. print_hits: Amateur space debris.
            "print_hits": re.compile(r"\b(print|debugPrint)\s*\(", re.I),
            # 40. cast_hits: "Trust Me" Tax. Explicit casting.
            "cast_hits": re.compile(r"\bas\s+[A-Z]\w*|\(\s*[A-Z]\w*\s*\)\s*[a-zA-Z_$]"),
            # 41. bailout_hits: Detonators. Aborting context.
            "bailout_hits": re.compile(
                r"\b(throw|rethrow|exit|exitCode|Process\.killPid)\b", re.I
            ),
            # 42. halt_hits: Temporal Duct Tape. (Forced waits/delays).
            "halt_hits": re.compile(
                r"\b(sleep|delay|setTimeout|setInterval)\s*\(", re.I
            ),
            # 43. bitwise_hits: Sub-Atomic Math.
            "bitwise_hits": re.compile(
                r"(?<!&)&(?!&)|(?<!\|)\|(?!\|)|<<|>>|\^|~(?!=|/)"
            ),
            # 44. sync_locks: Barricades. Coordinated threading.
            "sync_locks": re.compile(
                r"\b(Mutex|Lock|synchronized|Semaphore|Completer)\b", re.I
            ),
            # 45. freeze_hits: Data Cryogenics. Immutability.
            "freeze_hits": re.compile(r"\b(const|final|readonly|@immutable)\b", re.I),
            # 46. cleanup: The Janitor. Resource release.
            "cleanup": re.compile(
                r"\b(dispose|close|cleanup|cancel|drop|free)\s*\(", re.I
            ),
            # 47. encapsulation: The Vault. Scope hiding (Underscore prefix).
            "encapsulation": re.compile(r"\b(_[a-zA-Z0-9_$]+)\b|@protected|@private"),
            # 48. listeners: The Sinks. Waiting for state broadcasts.
            "listeners": re.compile(
                r"\b(on\(|addEventListener|subscribe|watch|useEffect|listen)\b", re.I
            ),
            # 49. test_skip: Safety Theater.
            "test_skip": re.compile(r"\b(@Ignore|test\.skip|t\.Skip|xit|mock)\b", re.I),
        },
    },
    "scala": {
        "_meta": {
            "target_version": "Scala 3 (Dotty / Braceless Syntax / Contextual Abstractions)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard sources, worksheet files (.sc), and pure-Scala build tool configurations (.sbt).
        "extensions": [".scala", ".sc", ".sbt", ".kojo"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Scala build definitions are typically handled by .sbt extensions rather than extensionless files.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions, build files, and Play framework configurations to anchor the ecosystem.
        "discriminators": [
            ".scala",
            "build.sbt",
            "application.conf",
            "Dependencies.scala",
            "project/build.properties",
            "project/plugins.sbt",
        ],
        # EXECUTION SIGNATURES: Interpreters found on Line 1 for Scala scripting and the Ammonite REPL.
        "shebangs": ["scala", "amm", "scala-cli"],
        # UPGRADED: Maps to Family 2 (Nested C)
        # Rationale: Scala explicitly supports nested multi-line comments (/* /* */ */),
        # requiring depth-aware stripping to prevent premature termination.
        "lexical_family": "nested_c",
        "rules": {
            "_line_anchor": re.compile(r"//"),
            "_inline_comment": re.compile(r"//"),
            "_block_start": re.compile(r"/\*"),
            "_block_end": re.compile(r"\*/"),
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch: decisions that split flow. Includes Scala 3 if-then and match-case.
            "branch": re.compile(
                r"\b(if|then|else|match|case|try|catch|finally|for|while|do|throw|yield)\b|&&|\|\|",
                re.I,
            ),
            # 2. args: Coupling Mass. Captures parameters in method signatures and lambdas.
            "args": re.compile(
                r"\bdef\s+[a-zA-Z_]\w*(?:\[[^\]]*\])?\s*\([^)]*\)|\([^)]*\)[ \t]*=>|\b[a-zA-Z_]\w*[ \t]*=>"
            ),
            # 3. linear: Smooth Path. Structural boundaries. EXCLUDES access modifiers and val/var.
            "linear": re.compile(
                r"\b(lazy|type|opaque|class|trait|object|enum|extension|import|export|return|extends|with|derives|new|given|using)\b"
            ),
            # 4. func_start: Satellite Spawner. Anchors executable logic. EXCLUDES structural headers.
            "func_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]+){0,5}"
                r"(?:(?:override|private|protected|final|implicit|inline|transparent|open|lazy)[ \t]+){0,3}"
                r"def\s+([a-zA-Z_]\w*)(?=[ \t]*[\[(:=]|\n|$)",
                re.M,
            ),
            # 5. class_start: Entity Census. Defines structural entities and OO boundaries.
            "class_start": re.compile(
                r"^[ \t]*(?:@[\w.]+(?:\([^)]*\))?[ \t]+){0,5}"
                r"(?:(?:sealed|abstract|final|case|open|opaque|transparent)[ \t]+){0,3}"
                r"(?:class|trait|object|enum)\s+([A-Za-z_]\w*)(?=[ \t]*[\[({]|\s+extends|\n|$)",
                re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety: Cyan Fortification. Monadic error handling (Option/Try) and assertions.
            "safety": re.compile(
                r"\b(Option|Some|None|Try|Success|Failure|Either|Left|Right|sealed|require|assert|assume)\b|\|\s*Null\b"
            ),
            # 7. safety_neg: Fractures. Actively bypassing type safety (asInstanceOf, .get).
            "safety_neg": re.compile(
                r"\b(null|asInstanceOf|isInstanceOf|\.get\b(?!Class)|@unchecked|Any|AnyRef)\b"
            ),
            # 8. danger: Heavy Load. Process killers and catastrophic exit commands.
            "danger": re.compile(
                r"\b(System\.exit|sys\.exit|Thread\.stop|Runtime\.getRuntime\.exec)\b"
            ),
            # 9. io: Boundaries. Filesystem, Network, and Http Clients (Includes CERN triggers).
            "io": re.compile(
                r"\b(Source|java\.io|java\.nio|Files\.|Socket|ServerSocket|sttp|Http|WSClient|HTLoad|HTGet|ENQUIRE)\b"
            ),
            # 10. api: Event Horizon. Implicit public visibility and Scala 3 @main entry points.
            "api": re.compile(
                r"\b(export)\b|@(?:main|GetMapping|PostMapping|Endpoint|Path)\b|^[ \t]*(?:override\s+|inline\s+|transparent[ \t]+)?def\s+[^_]\w+",
                re.M,
            ),
            # 11. flux: Boiling Plasma. State mutation (var and mutable collection updates).
            "flux": re.compile(
                r"\b(var|scala\.collection\.mutable|AtomicReference|AtomicInteger)\b|^[ \t]*[a-zA-Z_]\w*[ \t]*=",
                re.M,
            ),
            # 12. graveyard: Necrosis. Commented out structural code or logic trails.
            "graveyard": re.compile(
                r"//[ \t]*(?:def|val|var|class|object|trait|if|match|println|import)\b|/\*[ \t]*(?:def|val|class|object)"
            ),
            # 13. doc: Intent. Scaladoc documentation (/**) and annotations.
            "doc": re.compile(r"/\*\*|@param|@return|@tparam|@throws|@see|@note"),
            # 14. test: Verification. ScalaTest, MUnit, and standard expect/verify markers.
            "test": re.compile(
                r"\b(test\s*\(|it\s+should|assertEquals|assertThrows|AnyFunSuite|WordSpec|munit|weaver)\b|\b(?:must|expect|assert)\s*[\(\{]"
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency: Temporal Static. Effect systems and Actor paradigms (ZIO, Cats Effect, Akka).
            "concurrency": re.compile(
                r"\b(Future|Promise|Await|Actor|Behavior|ZIO|UIO|Task|RIO|cats\.effect\.IO|Fiber|FiberRef|Ref|Deferred|Semaphore)\b"
            ),
            # 16. ui_framework: View Layer. Scala.js DOM and XML literals (Includes TBL triggers).
            "ui_framework": re.compile(
                r"\b(dom\.|Laminar|Tyrian|HtmlElement|Document|Node|SGML|HyperLink|scala\.xml|Elem|XML|WorldWideWeb|BrowserView)\b"
            ),
            # 17. closures: Functional Depth. Anonymous function fat-arrows and underscores.
            "closures": re.compile(r"=>|(?<=\()\s*_\s*(?=[\),])|(?<=\W)_\s*(?=\W)"),
            # 18. globals: Shared Void. Singletons (objects) and JVM environment bindings.
            "globals": re.compile(
                r"\b(object\s+[A-Z]\w*|sys\.env|sys\.props|System\.getProperty|scala\.util\.Properties)\b"
            ),
            # 19. decorators: Metadata Hooks. Method and class annotations.
            "decorators": re.compile(r"@[A-Za-z_]\w*(?:\([^)]*\))?"),
            # 20. generics: Type Abstractions. Type parameterization and HKT constraints.
            "generics": re.compile(
                r"\[\s*[+-]?[A-Z][^\]]*\]|\bF\[_\]|<:|>:|\[[ \t]*_\s*\]"
            ),
            # 21. comprehensions: High-Density Loops. For-comprehensions and monadic chains.
            "comprehensions": re.compile(
                r"\bfor\s*(?:\{[^}]*\}|\([^)]*\))\s*yield\b|\.(?:map|flatMap|filter|withFilter|foldLeft|reduce|collect)\s*[\(\{]"
            ),
            # 22. scientific: Compute Core. Math library and linear algebra wrappers.
            "scientific": re.compile(
                r"\b(scala\.math|breeze\.|spire\.|algebird|Math\.|StrictMath\.|DenseMatrix|DenseVector)\b"
            ),
            # 23. heat_triggers: Thermal Radiation. Contextual abstractions and implicit resolution.
            "heat_triggers": re.compile(
                r"\b(implicit|given|using|inline|extension|TypeTag|ClassTag|scala\.reflect|Typeable|Dynamic|summon|derives)\b"
            ),
            # 24. import: Gravity Links. Module dependency resolution and Scala 3 exports.
            "import": re.compile(r"^[ \t]*(?:import|export)\s+[\w.]+", re.M),
            
            "_dependency_capture": re.compile(r"^[ \t]*(?:import|export)\s+([\w.]+)", re.M),
            
            # 25. ownership: Authorship indicators.
            "ownership": re.compile(
                r"(?:@author|Created by|Maintainer|Copyright|Tim Berners-Lee):\s+([^\n]+)",
                re.I,
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            # 26. planned_debt: The Promise. Future work markers.
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            # 27. fragile_debt: The Fracture. Admitted fragility or hacks.
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure: Map vs. Territory. Audit tags and architecture specs.
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)\]|\b(?:WorldWideWeb|HyperText\s+Proposal|NeXTSTEP)\b",
                re.I,
            ),
            # 30. civil_war: Indentation Tracker. Tabs vs 2-space standardization.
            "civil_war": None,
            # 31. ssr_boundaries: View Horizon. Play Framework and twirl template endpoints.
            "ssr_boundaries": re.compile(
                r"\b(Action|Controller|HttpRoutes|ServerEndpoint|twirl|html\.[a-zA-Z_]\w*|Ok\(|BadRequest\()\b"
            ),
            # 32. events: Pub/Sub Network. Stream processing and event bus signatures.
            "events": re.compile(
                r"\b(Source|Flow|Sink|fs2\.Stream|ZStream|EventBus|system\.eventStream|Observable)\b"
            ),
            # 33. dependency_injection: Inversion of Control. ZLayer and ReaderT patterns.
            "dependency_injection": re.compile(
                r"\b(@Inject|wire\[|ZLayer|ZLayer\.from|provide|provideSome|ReaderT|Kleisli|requires)\b"
            ),
            # 34. macros: Preprocessor Hooks. Scala 3 inline and quoted metaprogramming.
            "macros": re.compile(
                r"\b(inline\s+def|transparent\s+inline|macro|scala\.quoted|Expr|Type|Quotes)\b|\$\{.*?\}|\'\{"
            ),
            # 35. pointers: Memory Map. Scala Native C-Interop pointers.
            "pointers": re.compile(
                r"\b(Ptr\[[^\]]+\]|scala\.scalanative\.unsafe|!ptr|ptr\.|CFuncPtr|CStruct\d+)\b"
            ),
            # 36. memory_alloc: Manual Memory Management. Heap and Native allocations.
            "memory_alloc": re.compile(
                r"\b(Zone|zone[ \t]*\{|alloc\[[^\]]+\]|malloc|calloc|free|scala\.scalanative\.libc\.stdlib)\b"
            ),
            # 37. inline_asm: Bare Metal.
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry: Professional diagnostics (Structured logs).
            "telemetry": re.compile(
                r"\b(?:logger|log|ZIO\.log|LoggerFactory|log4cats|slf4j)\.(?:info|error|warn|debug|trace)\b|@Slf4j"
            ),
            # 39. print_hits: Amateur space debris.
            "print_hits": re.compile(r"\b(println|print|Console\.println)\b"),
            # 40. cast_hits: "Trust Me" Tax. Explicit type coercion.
            "cast_hits": re.compile(
                r"\basInstanceOf\[[^\]]*\]|\.(?:toInt|toLong|toFloat|toDouble|toByte|toShort)\b"
            ),
            # 41. bailout_hits: Detonators. Aborting context.
            "bailout_hits": re.compile(r"\b(throw|panic|abort|sys\.error|exit)\b"),
            # 42. halt_hits: Temporal Duct Tape. (Forced waits/sleep).
            "halt_hits": re.compile(
                r"\b(Thread\.sleep|delay|setTimeout|setInterval)\s*\("
            ),
            # 43. bitwise_hits: Sub-Atomic Math.
            "bitwise_hits": re.compile(r"(?<!&)&(?!&)|(?<!\|)\|(?!\|)|<<|>>|\^|~"),
            # 44. sync_locks: Barricades. Coordinated threading.
            "sync_locks": re.compile(
                r"\b(synchronized|volatile|Semaphore|Mutex|lock|unlock)\b"
            ),
            # 45. freeze_hits: Data Cryogenics. Immutability.
            "freeze_hits": re.compile(
                r"\b(val|final|sealed|readonly|Object\.freeze|immutable)\b"
            ),
            # 46. cleanup: The Janitor. Resource release.
            "cleanup": re.compile(
                r"\b(dispose|close|cleanup|cancel|free|bracket|finally|onException)\b"
            ),
            # 47. encapsulation: The Vault. Scope hiding.
            "encapsulation": re.compile(r"\b(private|protected)\b|private\[[^\]]+\]"),
            # 48. listeners: The Sinks. Waiting for state broadcasts.
            "listeners": re.compile(
                r"\b(on\(|addEventListener|subscribe|watch|useEffect|listen)\b"
            ),
            # 49. test_skip: Safety Theater.
            "test_skip": re.compile(r"\b(ignore|pending|skip|xit|xdescribe)\b"),
        },
    },
    "dockerfile": {
        "_meta": {
            "target_version": "Dockerfile (BuildKit)",
            "last_updated": "2026-02-27",
            "blueprint_version": "v6.2.2",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard extensions for container definitions across Docker and Podman ecosystems.
        "extensions": [".dockerfile", ".containerfile"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: The universally recognized, extensionless architectural anchors of containerized environments.
        "exact_matches": [
            "Dockerfile",
            "Containerfile",
            "Dockerfile.prod",
            "Dockerfile.dev",
            "Dockerfile.build",
            "Dockerfile.test",
            "Dockerfile.local",
        ],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Compose files and ignore manifests acting as massive gravity anchors.
        "discriminators": [
            "docker-compose.yml",
            "docker-compose.yaml",
            ".dockerignore",
            "compose.yaml",
        ],
        # EXECUTION SIGNATURES: Docker natively uses BuildKit syntax directives instead of traditional shebangs.
        "shebangs": [],
        # UPGRADED: Maps to Family 3 (Pure Hash)
        # Rationale: Docker natively uses '#' exclusively for line-level comments and parser directives.
        "lexical_family": "pure_hash",
        "rules": {
            "_line_anchor": re.compile(r"#"),
            "_inline_comment": re.compile(r"#"),
            "_block_start": None,
            "_block_end": None,
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Control flow executing inside RUN shell blocks. High density indicates complex embedded shell scripts.
            "branch": re.compile(
                r"\b(?:if|elif|else|fi|case|esac|for|while|do|done|until)\b|&&|\|\|",
                re.I,
            ),
            # 2. args (The Coupling Mass)
            # Build arguments (`ARG`) passed into the container acting as input parameters to the satellite.
            "args": re.compile(r"^[ \t]*ARG[ \t]+[a-zA-Z0-9_-]+", re.M | re.I),
            # 3. linear (The Smooth Path)
            # Structural boundaries defining straight-line execution and environment contexts.
            # CRITICAL GUARDRAIL: EXCLUDES `FROM` and `RUN`/`CMD` to maintain geometric stability.
            "linear": re.compile(
                r"^[ \t]*(?:WORKDIR|USER|VOLUME|STOPSIGNAL|SHELL|LABEL)\b", re.M | re.I
            ),
            # 4. func_start (The Satellite Spawner)
            # CRITICAL GUARDRAIL: Spawns satellites. ONLY executable logic blocks.
            # In Docker, `RUN`, `CMD`, and `ENTRYPOINT` execute logic, generating discrete intermediate image layers.
            "func_start": re.compile(
                r"^[ \t]*(RUN|CMD|ENTRYPOINT|HEALTHCHECK)(?=[ \t])", re.M | re.I
            ),
            # 5. class_start (The Entity Census)
            # Defines object-oriented and structural boundaries. Drives API Surface Area math.
            # `FROM` instantiates a discrete build stage/image boundary, acting as a class wrapper.
            "class_start": re.compile(r"^[ \t]*(FROM)(?=[ \t])", re.M | re.I),
            # --- ⚠️ PHASE 2: RISK ENGINE (The Dimensions) ---
            # 6. safety (The Defenders / Cyan Fortification)
            # Hardening the container. Dropping root privileges (`USER nonroot`), explicit `HEALTHCHECK`,
            # setting explicit shell crash flags (`set -e`), and safe file ownership (`--chown`).
            "safety": re.compile(
                r"^[ \t]*HEALTHCHECK\b|--chown=|^[ \t]*USER[ \t]+(?!root\b|0\b)[a-zA-Z0-9_-]+|\bset[ \t]+-[exuo]\b",
                re.M | re.I,
            ),
            # 7. safety_neg (The Fractures / Red Fragility)
            # Actively bypassing isolation or safety logic.
            # Using `:latest`, running as root, setting permissions to 777, or blindly curling directly into bash.
            # CRITICAL GUARDRAIL: Safely bounds the curl/wget pipe `[^|\n]{1,200}` to prevent ReDoS on massive RUN chains.
            "safety_neg": re.compile(
                r":latest\b|^[ \t]*USER[ \t]+(?:root|0)\b|chmod[ \t]+777|--privileged|--allow-unauthenticated|\b(?:curl|wget)[ \t]+[^|\n]{1,200}\|[ \t]*(?:bash|sh|zsh)\b",
                re.M | re.I,
            ),
            # 8. danger (The Heavy Load / Space Debris)
            # Extreme space debris. Destructive recursive removes targeting root, and dangerous dynamic eval.
            # CRITICAL GUARDRAIL: Raw terminal prints (`echo`) strictly routed to print_hits.
            "danger": re.compile(
                r"\b(?:rm[ \t]+-rf[ \t]+/(?![A-Za-z])|eval|exec)\b", re.M | re.I
            ),
            # 9. io (The Boundaries / System Gravity)
            # Interaction with external networks, copying files from host, or executing package managers.
            "io": re.compile(
                r"^[ \t]*(?:COPY|ADD)[ \t]+|\b(?:wget|curl|apt-get|apk|yum|dnf|git[ \t]+clone|tar[ \t]+-[cx]f|unzip|pip[ \t]+install|npm[ \t]+install)\b",
                re.M | re.I,
            ),
            # 10. api (The Event Horizon / Rose Glow)
            # Code exposed to the outside world. Ports explicitly exposed to the host network (`EXPOSE`).
            "api": re.compile(r"^[ \t]*EXPOSE[ \t]+[0-9]+", re.M | re.I),
            # 11. flux (The Boiling Plasma / Orange Glow)
            # Mutation of state. Setting Environment variables that permanently alter the image layer state.
            "flux": re.compile(
                r"^[ \t]*ENV[ \t]+[a-zA-Z0-9_]+|export[ \t]+[a-zA-Z0-9_]+[ \t]*=",
                re.M | re.I,
            ),
            # 12. graveyard (The Necrosis / Purple Haze)
            # Ghost logic, commented-out structural Dockerfile commands.
            "graveyard": re.compile(
                r"^[ \t]*#[ \t]*(?:RUN|COPY|ADD|ENV|EXPOSE|FROM|CMD|ENTRYPOINT|WORKDIR)\b",
                re.M | re.I,
            ),
            # 13. doc (The Intent / Gold Library)
            # Intent documentation meant for developers or image registries.
            "doc": re.compile(
                r"^[ \t]*LABEL[ \t]+(?:maintainer|org\.opencontainers|version|description)=|^[ \t]*#[ \t]*(?:Description|Usage|Author|Maintainer):",
                re.M | re.I,
            ),
            # 14. test (The Verification / Teal Glow)
            # Explicit test runner executions inside the build layer (often used in CI multi-stage pipelines).
            "test": re.compile(
                r"\b(?:npm[ \t]+test|yarn[ \t]+test|pytest|go[ \t]+test|cargo[ \t]+test|make[ \t]+test)\b",
                re.M | re.I,
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency (The Temporal Static / Ultraviolet)
            # Parallelism executed inside the build shell (e.g. compiling with all cores).
            "concurrency": re.compile(
                r"&[ \t]*$|\b(?:nohup|parallel|make[ \t]+-j|xargs[ \t]+-P)\b", re.M
            ),
            # 16. ui_framework (The View Layer)
            # Containerizing GUI applications (X11, Wayland, GTK).
            "ui_framework": re.compile(
                r"\b(?:xvfb|x11|wayland|gtk|qt5?|libgl1-mesa)\b", re.I
            ),
            # 17. closures (The Functional Depth)
            # Dockerfiles are purely declarative structurally; closures do not exist.
            "closures": None,
            # 18. globals (The Shared Void)
            # Global environment variables mapping structurally.
            "globals": re.compile(r"^[ \t]*ENV[ \t]+[a-zA-Z0-9_]+", re.M | re.I),
            # 19. decorators (The Metadata Hooks)
            # Not natively applicable to Dockerfile architecture.
            "decorators": None,
            # 20. generics (The Type Abstractions)
            "generics": None,
            # 21. comprehensions (The High-Density Loops)
            "comprehensions": None,
            # 22. scientific (The Compute Core)
            # Installing data science, ML base dependencies, or GPU drivers natively into the image.
            "scientific": re.compile(
                r"\b(?:nvidia/cuda|pytorch/pytorch|tensorflow/tensorflow|jupyter/)\b",
                re.I,
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Extreme "Logic Heat": Advanced BuildKit logic. Mounting caches, secrets, cross-platform builds, or `ONBUILD` (which defers execution to downstream images).
            "heat_triggers": re.compile(
                r"^[ \t]*ONBUILD\b|--mount=type=(?:cache|secret|bind|ssh)|--platform=|<<EOF",
                re.M | re.I,
            ),
            # 24. import (The Gravity Links)
            # Base images or dependencies pulled from other build stages (`COPY --from=`).
            "import": re.compile(
                r"^[ \t]*FROM[ \t]+[a-zA-Z0-9_./:-]+|--from=[a-zA-Z0-9_-]+", re.M | re.I
            ),
            
            "_dependency_capture": re.compile(r"^[ \t]*FROM\s+(?:--[\w-]+=[^\s]+\s+)?([a-zA-Z0-9_./:-]+)|--from=([a-zA-Z0-9_-]+)", re.M | re.I),
            
            # 25. ownership (The Authorship)
            # Standard metadata tracing image ownership (legacy MAINTAINER or modern LABEL).
            "ownership": re.compile(
                r"^[ \t]*(?:MAINTAINER|LABEL[ \t]+maintainer=|LABEL[ \t]+org\.opencontainers\.image\.authors=)[ \t]*(.*)",
                re.M | re.I,
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(r"\b(?:TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(?:HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:[ \t]*SPEC[ \t]*-[ \t]*\d+|spec|audit|CVE-\d{4}-\d+)[^\]]*\]",
                re.I,
            ),
            # 30. civil_war (The Indentation Tracker)
            # Dockerfiles strictly use spaces for formatting continuations. Tabs indicate formatter disruption.
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": None,
            # 32. events (The Pub/Sub Network)
            # Container lifecycle events explicitly bound to the host OS.
            "events": re.compile(r"^[ \t]*STOPSIGNAL[ \t]+", re.M | re.I),
            # 33. dependency_injection (The Inversion of Control)
            # BuildKit secret and SSH mounts injecting external state at compile time securely.
            "dependency_injection": re.compile(r"--mount=type=(?:secret|ssh)", re.I),
            # 34. macros (The Preprocessor Hooks)
            # Docker BuildKit `# syntax=` directives which change the parser dynamically at compile-time (just like C-macros).
            "macros": re.compile(
                r"^[ \t]*#[ \t]*(?:syntax|escape)[ \t]*=", re.M | re.I
            ),
            # 35. pointers (The Memory Map)
            "pointers": None,
            # 36. memory_alloc (Manual Memory Management)
            # Explicit memory limits defined in ENV vars that configure Java/Node runtime heaps natively.
            "memory_alloc": re.compile(
                r"\b(?:--memory=|JAVA_OPTS|JAVA_TOOL_OPTIONS|NODE_OPTIONS|--max-old-space-size|-Xmx|-Xms)\b",
                re.I,
            ),
            # 37. inline_asm (The Bare Metal)
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            # Forcing specific logging outputs at the container level or symlinking to stdout for daemon parsing.
            "telemetry": re.compile(
                r"\b(?:LOG_LEVEL|--log-level[ \t]+(?:debug|info|warn|error)|ln[ \t]+-sf[ \t]+/dev/stdout)\b",
                re.I,
            ),
            # 39. print_hits (The Amateur / Space Debris)
            # Shell echos used for ad-hoc debugging in the build output log.
            "print_hits": re.compile(r"\b(?:echo|printf)\b", re.I),
            # 40. cast_hits (The "Trust Me" Tax)
            "cast_hits": None,
            # 41. bailout_hits (The Detonators)
            # Hard execution aborts forcing the build to fail dynamically.
            "bailout_hits": re.compile(
                r"\b(?:exit[ \t]+[1-9]|kill[ \t]+-[0-9]+)\b", re.I
            ),
            # 42. halt_hits (Temporal Duct Tape)
            # Forcing the build thread to sleep (often a hack to wait for a daemon/network).
            "halt_hits": re.compile(r"\bsleep[ \t]+[0-9]+\b", re.I),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": None,
            # 44. sync_locks (The Barricades)
            # Utilizing file locking to prevent parallel build collisions.
            "sync_locks": re.compile(r"\bflock\b", re.I),
            # 45. freeze_hits (The Data Cryogenics)
            # Pinning dependencies to immutable SHAs rather than mutable tags. (The Yang to `:latest`).
            "freeze_hits": re.compile(r"@[a-f0-9]{64}\b|--read-only|:ro\b", re.I),
            # 46. cleanup (The Janitor)
            # Explicitly purging apt/apk caches to reduce final container bloat. (The Yang to IO).
            "cleanup": re.compile(
                r"\b(?:apt-get[ \t]+clean|rm[ \t]+-rf[ \t]+/var/lib/apt/lists|apk[ \t]+(?:cache[ \t]+)?clean|yum[ \t]+clean[ \t]+all|npm[ \t]+cache[ \t]+clean)\b",
                re.I,
            ),
            # 47. encapsulation (The Vault)
            # Explicitly encapsulating logic in multi-stage builds (`AS builder`). Hides intermediate build layers.
            "encapsulation": re.compile(
                r"^[ \t]*FROM[ \t]+[^\n]+[ \t]+AS[ \t]+[a-zA-Z0-9_-]+", re.M | re.I
            ),
            # 48. listeners (The Sinks)
            # Exposing ports for network consumption. (The Yang to Events/IO).
            "listeners": re.compile(r"^[ \t]*EXPOSE[ \t]+[0-9]+", re.M | re.I),
            # 49. test_skip (Safety Theater)
            # Bypassing package manager tests/audits or using logical OR to ignore failures (`|| true`).
            "test_skip": re.compile(
                r"\|\|[ \t]*true\b|\b(?:--passWithNoTests|skipTests|Dmaven\.test\.skip=true|--no-audit)\b",
                re.I,
            ),
        },
    },
    "matlab": {
        "_meta": {
            "target_version": "MATLAB R2024b",
            "last_updated": "2026-02-27",
            "blueprint_version": "v6.2.2",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard scripts, functions, and modern Live Scripts (.mlx).
        "extensions": [".m", ".mlx"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: MATLAB and Octave rely strictly on extensions for execution.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Critical for resolving the massive .m collision with Objective-C. Binary workspace and figure files act as absolute anchors.
        "discriminators": [".m", ".mat", ".fig", ".mlx", "project.prj"],
        # Instantly claims any .m file that uses MATLAB's unique comment character (%) 
        # or the MATLAB function declaration syntax. Defeats Objective-C gravity theft.
        # Instantly claims any .m file via a definitive MATLAB section break (%%) 
        # or properly formatted comment. (Removed 'function' to prevent stealing extensionless shell scripts).
        "internal_discriminator": re.compile(r"^[ \t]*(?:%[ \t]+|%%)", re.M),
        # EXECUTION SIGNATURES: Interpreters found on Line 1 for GNU Octave or headless MATLAB CLI scripts.
        "shebangs": ["octave", "matlab"],
        # UPGRADED: Maps to Family 8 (Singular/Unique)
        # Rationale: (CORRECTION) Uses '%' for lines and '%{ %}' for blocks. Mapping this to
        # hybrid_dash would cause the engine to look for '--', missing the math entirely.
        "lexical_family": "singular",
        "rules": {
            "_line_anchor": re.compile(r"%"),
            "_inline_comment": re.compile(r"%"),
            "_block_start": re.compile(r"^[ \t]*%\{", re.M),
            "_block_end": re.compile(r"^[ \t]*%\}", re.M),
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # branch: MATLAB control flow. EXCLUDES 'error' and 'rethrow' (bailout_hits).
            "branch": re.compile(
                r"\b(?:if|elseif|else|switch|case|otherwise|for|while|try|catch)\b|&&|\|\||~="
            ),
            # args: Captures standard function inputs and return signatures `function [out1, out2] = myFun(in1, in2)`.
            # CRITICAL GUARDRAIL: Safely bounds `\([^)]*\)` and `\[[^\]]*\]`.
            "args": re.compile(
                r"\bfunction[ \t]+(?:\[[^\]]*\][ \t]*=[ \t]*|[a-zA-Z_]\w*[ \t]*=[ \t]*)?[a-zA-Z_]\w*[ \t]*\([^)]*\)|@[ \t]*\([^)]*\)"
            ),
            # linear: Structural boundaries defining straight-line execution.
            # CRITICAL GUARDRAIL: Access modifiers (private, protected) explicitly omitted.
            "linear": re.compile(
                r"\b(?:classdef|properties|methods|events|enumeration|return|global|persistent|continue|break|end)\b"
            ),
            # func_start: Spawns satellites. Exactly anchors executable blocks.
            # Negative lookahead explicitly prevents control flow or OOP structures from generating ghost satellites.
            "func_start": re.compile(
                r"^[ \t]*(?!(?:if|for|while|switch|catch|classdef)\b)function[ \t]+(?:\[[^\]]*\][ \t]*=[ \t]*|[a-zA-Z_]\w*[ \t]*=[ \t]*)?([a-zA-Z_]\w*)(?=[ \t]*\(|\n|$)",
                re.M,
            ),
            # class_start: Defines an object-oriented boundary.
            # Safely steps over optional class attributes like `classdef (ConstructOnLoad) MyClass`
            "class_start": re.compile(
                r"^[ \t]*classdef(?:[ \t]*\([^)]*\))?[ \t]+([a-zA-Z_]\w*)(?=[ \t\n]|$)",
                re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (The Dimensions) ---
            # safety: Defensive programming, modern argument validation (`arguments` block), and type/shape checks.
            "safety": re.compile(
                r"\b(?:try|catch|narginchk|nargoutchk|validateattributes|validatestring|mustBe[A-Za-z_]\w*|assert|isa|isempty|isnumeric|ischar|isstruct|isfield|iscell|islogical|arguments)\b"
            ),
            # safety_neg: Actively bypasses safety via dynamic strings or manipulating the caller workspace.
            "safety_neg": re.compile(
                r'\b(?:eval|evalin|assignin|evalc)\b|\bwarning[ \t]*\([ \t]*[\'"]off[\'"]'
            ),
            # danger: Destructive workspace actions and OS bypasses.
            # CRITICAL GUARDRAIL: Raw terminal prints (`disp`) strictly routed to print_hits.
            "danger": re.compile(
                r"\b(?:clear[ \t]+all|clc|system|dos|unix|exit|quit|keyboard)\b|^[ \t]*![ \t]*[a-zA-Z_]",
                re.M | re.I,
            ),
            # io: Interactions with disk, hardware, or web.
            "io": re.compile(
                r"\b(?:load|save|fopen|fclose|fread|fwrite|fscanf|webread|webwrite|urlread|urlwrite|readtable|writetable|readmatrix|writematrix|serialport|imread|imwrite|audioread)\b"
            ),
            # api: Public APIs. We track explicit Methods blocks that don't declare private access.
            "api": re.compile(
                r"^[ \t]*methods(?:[ \t]*\([ \t]*Access[ \t]*=[ \t]*public[ \t]*\))?",
                re.M | re.I,
            ),
            # flux: Mutation of state via assignment.
            # Safely clamped with `[ \t]*=[ \t]*` to avoid newline spirals. Bounded nested fields `{0,5}`.
            "flux": re.compile(
                r"^[ \t]*[a-zA-Z_]\w*(?:\([^)]*\)|\{[^}]*\}|\.[a-zA-Z_]\w*){0,5}[ \t]*=[ \t]*[^=]|\b(?:clear|clearvars)\b",
                re.M,
            ),
            # graveyard: Ghost logic, commented-out structural MATLAB code.
            "graveyard": re.compile(
                r"^[ \t]*%[ \t]*(?:if|for|while|function|classdef)\b", re.M
            ),
            # doc: Standard MATLAB Help text (`%%` sections) or typed annotations.
            "doc": re.compile(
                r"^[ \t]*%[ \t]*@(?:param|return|author)|^[ \t]*%%[ \t]*[A-Z][A-Z0-9_]*",
                re.M,
            ),
            # test: MATLAB unit testing framework keywords.
            "test": re.compile(
                r"\b(?:matlab\.unittest|TestCase|verifyEqual|assertEqual|assertGreaterThan|verifyTrue|verifyFalse|verifyError)\b"
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # concurrency: Parallel Computing Toolbox (parallel loops and batch jobs).
            "concurrency": re.compile(
                r"\b(?:parfor|parfeval|spmd|batch|createJob|createTask|BackgroundPool|parpool|fetchOutputs)\b"
            ),
            # ui_framework: MATLAB UI Figures and App Designer interfaces.
            "ui_framework": re.compile(
                r"\b(?:uifigure|uicontrol|uiaxes|uilabel|uibutton|appdesigner|guide|drawnow|msgbox|errordlg|warndlg|figure|plot|scatter|surf)\b"
            ),
            # closures: Anonymous functions (MATLAB's lambdas).
            "closures": re.compile(r"@[ \t]*\([^)]*\)"),
            # globals: Globals and persistent memory retaining state across calls.
            "globals": re.compile(r"\b(?:global|persistent|setenv|getenv)\b"),
            # decorators: MATLAB Property/Method attribute blocks (e.g., `methods (Access = private)`).
            # Safely bounded with `\([^)]*\)` to avoid ReDoS.
            "decorators": re.compile(
                r"^[ \t]*(?:properties|methods|events)[ \t]*\([^)]*\)", re.M
            ),
            # generics: MATLAB is dynamically typed. Generics do not exist natively.
            "generics": None,
            # comprehensions: MATLAB array mapping functions (the closest equivalent to list comprehensions).
            "comprehensions": re.compile(
                r"\b(?:arrayfun|cellfun|structfun|rowfun|varfun)\b"
            ),
            # scientific: The core of MATLAB. High-density built-in numerical solvers and DSP operations.
            "scientific": re.compile(
                r"\b(?:fft|ifft|svd|eig|inv|det|polyfit|ode45|ode15s|integral|cross|dot)\b|\.\*|\./|\.\^"
            ),
            # heat_triggers: Metaprogramming (feval), implicit expansion (bsxfun), and reflection.
            "heat_triggers": re.compile(
                r"\b(?:feval|bsxfun|cell2mat|mat2cell|num2cell|struct2cell|str2func|func2str|meta\.class|metaclass)\b|\?[a-zA-Z_]\w*"
            ),
            # import: Namespace/Class loading.
            "import": re.compile(r"^[ \t]*import[ \t]+[a-zA-Z0-9_.*]+", re.M),
            
            "_dependency_capture": re.compile(r"^[ \t]*import[ \t]+([a-zA-Z0-9_.*]+)", re.M),
            
            # ownership: Standard MATLAB comment authorship signatures.
            "ownership": re.compile(
                r"^[ \t]*%[ \t]*(?:Author|Created by|Copyright)[ \t]*:(.*)", re.M | re.I
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS ---
            "planned_debt": re.compile(r"\b(?:TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            "fragile_debt": re.compile(r"\b(?:HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            "spec_exposure": re.compile(
                r"\[(?:[ \t]*SPEC[ \t]*-[ \t]*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # civil_war: MATLAB default is 4 spaces. Raw tabs indicate formatter disruption.
            "civil_war": None,
            # ssr_boundaries: Web App compiler hooks.
            "ssr_boundaries": re.compile(r"\b(?:webwindow|htmlTree)\b"),
            # events: MATLAB Object-Oriented Event triggering.
            "events": re.compile(
                r"\b(?:notify|event\.EventData|event\.PropertyEvent)\b"
            ),
            "dependency_injection": None,
            "macros": None,
            # pointers: C/C++ FFI pointer manipulation via MATLAB's `libpointer` or `handle` class.
            "pointers": re.compile(r"\b(?:libpointer|calllib)\b|<[ \t]*handle\b"),
            # memory_alloc: Explicit pre-allocation (a critical MATLAB performance mechanism to avoid array resizing).
            "memory_alloc": re.compile(
                r"\b(?:zeros|ones|nan|NaN|false|true|cell|struct|prealloc)[ \t]*\([^)]*\)",
                re.I,
            ),
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # telemetry: Custom structured logging frameworks.
            "telemetry": re.compile(
                r"\b(?:log4m|logger\.(?:info|debug|warn|error)|logDebug|logInfo|logWarn|logError)\b",
                re.I,
            ),
            # print_hits: Ad-hoc console dumps. Excludes fprintf addressing file IDs `fprintf(fid, ...)`.
            "print_hits": re.compile(
                r"\b(?:disp|warning|fprintf(?![ \t]*\([ \t]*[a-zA-Z_]))\b"
            ),
            # cast_hits: Changing data types (vital for memory size control in big matrices).
            "cast_hits": re.compile(
                r"\b(?:cast|typecast|int8|uint8|int16|uint16|int32|uint32|int64|uint64|single|double|logical)\s*\("
            ),
            # bailout_hits: Hard execution aborts.
            "bailout_hits": re.compile(
                r"\b(?:error|throw|rethrow|MException|throwAsCaller)\b"
            ),
            # halt_hits: Forcing the thread to pause.
            "halt_hits": re.compile(r"\bpause[ \t]*\("),
            # bitwise_hits: Sub-atomic manipulations.
            "bitwise_hits": re.compile(
                r"\b(?:bitand|bitor|bitxor|bitcmp|bitshift|bitset|bitget)\b"
            ),
            # sync_locks: Managing parallel data queues and thread pooling barriers.
            "sync_locks": re.compile(
                r"\b(?:labBarrier|labSend|labReceive|labBroadcast)\b"
            ),
            # freeze_hits: Constant property assignments locking data.
            "freeze_hits": re.compile(r"\bConstant\b"),
            # cleanup: Garbage collection and explicit file/handle destruction.
            "cleanup": re.compile(
                r"\b(?:clear|clearvars|delete|close|fclose|onCleanup)\b"
            ),
            # encapsulation: Explicit scoping modifiers hiding logic.
            "encapsulation": re.compile(r"Access[ \t]*=[ \t]*(?:private|protected)"),
            # listeners: Event sinks waiting for state.
            "listeners": re.compile(
                r"\b(?:addlistener|event\.listener|event\.proplistener)\b"
            ),
            # test_skip: Safety Theater bypasses.
            "test_skip": re.compile(
                r"\b(?:assume|assumeFail|assumeTrue|assumeFalse)\b"
            ),
        },
    },
    "livecode": {
        "_meta": {
            "target_version": "LiveCode 9.6 / 10.0 (Current Stable/DP)",
            "last_updated": "2026-02-19",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Includes modern server scripts, builder files, binary stacks, and legacy Revolution stacks.
        "extensions": [".lc", ".livecodescript", ".lcb", ".livecode", ".stack", ".rev"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: LiveCode environments rarely use extensionless execution scripts.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions to anchor the LiveCode server/builder environment.
        "discriminators": [".lc", ".livecode", ".lcb", ".livecodescript"],
        # EXECUTION SIGNATURES: Interpreters found on Line 1 for LiveCode Server environments.
        "shebangs": ["livecode-server"],
        # UPGRADED: Maps to Family 6 (Polyglot)
        # Rationale: Accepts '--', '//', '#', and '/* */' to support both its legacy HyperTalk roots and modern C-style syntax.
        "lexical_family": "polyglot",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Handles all three line-comment styles found in the xTalk family.
            "_line_anchor": re.compile(r"--|//|#"),
            # Inline comments follow the same tri-token logic.
            "_inline_comment": re.compile(r"--|//|#"),
            # Block comment start: /* (Adopted in modern LiveCode)
            "_block_start": re.compile(r"/\*"),
            # Block comment end: */
            "_block_end": re.compile(r"\*/"),
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch: decisions that split flow. Includes English-like loops and try-catch.
            "branch": re.compile(
                r"\b(if|then|else|switch|case|default|repeat|while|until|times|try|catch|finally|throw|next\s+repeat|and|or|not)\b",
                re.I,
            ),
            # 2. args: Coupling Mass. Captures parameters in handlers (on, command, function).
            "args": re.compile(
                r"(?:on|command|function|getprop|setprop)\s+[a-zA-Z0-9_-]+\s+([^\n]+)",
                re.I,
            ),
            # 3. linear: Smooth Path. Structural boundaries and state transformation verbs.
            "linear": re.compile(
                r"\b(put|get|set|go|send|dispatch|pass|return|add|subtract|multiply|divide|constant|visual\s+effect|play|sort|find|replace)\b",
                re.I,
            ),
            # 4. func_start: Satellite Spawner. Anchors executable logic blocks (handlers).
            "func_start": re.compile(
                r"^[ \t]*(?:private\s+|public[ \t]+)?(?:on|command|function|getprop|setprop)\s+([a-zA-Z0-9_-]+)(?=[ \t\n]|$)",
                re.I | re.M,
            ),
            # 5. class_start: Entity Census. Defines structural entities (Stacks, Behaviors, Widgets).
            "class_start": re.compile(
                r'^[ \t]*(?:script|behavior|widget|module|library)\s+(["\'a-zA-Z_]\w*)(?=[ \t\n]|$)',
                re.I | re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety: Cyan Fortification. Defensive programming and screen/message locking.
            "safety": re.compile(
                r"\b(try|catch|finally|throw|lock\s+screen|lock\s+messages|lock\s+errordialogs|assert|strict\s+compilation|is\s+a|is\s+strictly)\b",
                re.I,
            ),
            # 7. safety_neg: Fractures. Actively bypassing safety (disabling messages, raw do).
            "safety_neg": re.compile(
                r"\b(disable\s+messages|unlock\s+(?:screen|messages)|global\s+|do\s+(?![a-zA-Z_]\w*\b))\b",
                re.I,
            ),
            # 8. danger: Heavy Load. Process killers and blocking UI alerts in execution flow.
            "danger": re.compile(
                r"\b(answer|ask|do(?!\s+(?:AppleScript|VBScript))|delete\s+(?:file|folder|url)|quit|exit\s+to\s+top)\b",
                re.I,
            ),
            # 9. io: Boundaries. Disk, Network, and URL fetching.
            "io": re.compile(
                r"\b(open\s+(?:file|socket|process)|read\s+from|write\s+to|close\s+(?:file|socket|process)|post\s+[^ \t\n]+?\s+to\s+url|get\s+url|put\s+url|load\s+url)\b",
                re.I,
            ),
            # 10. api: Event Horizon. Exposed surface area (Any non-private handler).
            "api": re.compile(
                r"^[ \t]*(?:public[ \t]+)?(?!(?:private)\s+)(?:on|command|function|getprop|setprop)\s+[a-zA-Z0-9_-]+",
                re.I | re.M,
            ),
            # 11. flux: Boiling Plasma. State mutation (The 'put into' core of xTalk).
            "flux": re.compile(
                r"\b(?:put\s+[^ \t\n]+?\s+(?:into|after|before)|set\s+(?:the[ \t]+)?[a-zA-Z0-9_.]+\s+to|add\s+[^ \t\n]+?\s+to|subtract\s+[^ \t\n]+?\s+from)\b",
                re.I,
            ),
            # 12. graveyard: Necrosis. Commented out structural code.
            "graveyard": re.compile(
                r"^[ \t]*(?:--|#|//)[ \t]*(?:on|command|function|put|get|set|if|repeat|try|end)\b",
                re.I | re.M,
            ),
            # 13. doc: Intent. Structured documentation (/** or --@ tags).
            "doc": re.compile(
                r"^[ \t]*(?:--\||--@|/\*\*|//!).*(?:@param|@return|@author)|\b(?:Description|Purpose|Author|Summary):\b",
                re.I | re.M,
            ),
            # 14. test: Verification. Unit testing framework markers.
            "test": re.compile(
                r"\b(command\s+test[a-zA-Z0-9_]*|pass\s+test|fail\s+test|Levure|LcU|runTests)\b",
                re.I,
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency: Temporal Static. Message scheduling and non-blocking waits.
            "concurrency": re.compile(
                r"\b(send\s+[^ \t\n]+?\s+in\s+[^ \t\n]+?\s+(?:seconds|milliseconds|ticks)|wait\s+(?:for[ \t]+)?\d+\s+[^ \t\n]+?\s+with\s+messages|dispatch|pendingMessages|cancel)\b",
                re.I,
            ),
            # 16. ui_framework: View Layer. HyperCard-descendant object hierarchy.
            "ui_framework": re.compile(
                r"\b(card|stack|background|bg|button|btn|field|fld|group|grp|graphic|grc|image|img|scrollbar|browser|data\s+grid|widget)\b",
                re.I,
            ),
            # 17. closures: Functional Depth. (LiveCode Script lacks native lambdas).
            "closures": None,
            # 18. globals: Shared Void. Global state and environmental bindings.
            "globals": re.compile(
                r"\b(global\s+|the\s+global|the\s+environment|the\s+platform|\$ENV|it)\b",
                re.I,
            ),
            # 19. decorators: Metadata Hooks. LCB attributes.
            "decorators": re.compile(
                r"^[ \t]*@(?:metadata|property|type|name|title)\b", re.M
            ),
            # 20. generics: Type Abstractions. (LCS is dynamically typed).
            "generics": None,
            # 21. comprehensions: High-Density Loops. Implicit list processing.
            "comprehensions": re.compile(
                r"\brepeat\s+for\s+each\s+(?:item|line|word|char|key|element)\b|\bfilter\s+[^ \t\n]+?\s+(?:with|without)\b",
                re.I,
            ),
            # 22. scientific: Compute Core. Native math commands.
            "scientific": re.compile(
                r"\b(sqrt|exp|ln|log2|log10|sin|cos|tan|asin|acos|atan|atan2|abs|round|trunc|random|any|average|max|min)\b",
                re.I,
            ),
            # 23. heat_triggers: Thermal Radiation. Dynamic execution and path hijacking.
            "heat_triggers": re.compile(
                r"\b(do\s+|value\(|the\s+params|the\s+paramcount|evaluate\(|frontscripts|backscripts|insert\s+script)\b",
                re.I,
            ),
            # 24. import: Gravity Links. Library and stack loading.
            "import": re.compile(
                r"\b(start\s+using\s+(?:stack|behavior)|require|include|module)\b", re.I
            ),
            
            "_dependency_capture": re.compile(r"\b(?:start\s+using\s+(?:stack\s+|behavior\s+)?|require\s+|include\s+|module\s+)(?:['\"]([^'\"]+)['\"]|([^'\"\s]+))", re.I),
            
            # 25. ownership: Authorship metadata in comments.
            "ownership": re.compile(
                r"^[ \t]*(?:--|//|#)\s*(?:Author|Created by|Maintainer|Copyright):\s+([^\n]+)",
                re.I | re.M,
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            # 26. planned_debt: The Promise. Future work markers.
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            # 27. fragile_debt: The Fracture. Admitted fragility or hacks.
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure: Map vs. Territory. Audit tags.
            "spec_exposure": re.compile(r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)\]", re.I),
            # 30. civil_war: Indentation Tracker. Tabs vs Spaces density.
            "civil_war": None,
            # 31. ssr_boundaries: View Horizon. Server-side rendering.
            "ssr_boundaries": re.compile(
                r"\b(<\?lc|\?>|\$_POST|\$_GET|\$_SERVER|\$_COOKIE|\$_SESSION|put\s+header)\b",
                re.I,
            ),
            # 32. events: Pub/Sub Network. Signal handlers and event brokers.
            "events": re.compile(
                r"^[ \t]*on\s+(?:mouseUp|mouseDown|openCard|closeCard|preOpenCard|openStack|closeStack|resizeStack|rawKeyDown|textChanged)\b",
                re.I | re.M,
            ),
            # 33. dependency_injection: Inversion of Control. Service locator patterns.
            "dependency_injection": re.compile(
                r"\b(?:set\s+the\s+behavior\s+of|start\s+using\s+(?:stack|behavior)|insert\s+script\s+into\s+(?:front|back))\b",
                re.I,
            ),
            # 34. macros: Preprocessor Hooks.
            "macros": None,
            # 35. pointers: Memory Map. Pass by reference in params.
            "pointers": re.compile(r"\b@[a-zA-Z_]\w*\b", re.I),
            # 36. memory_alloc: Manual Memory Management.
            "memory_alloc": None,
            # 37. inline_asm: Bare Metal.
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry: Professional diagnostics.
            "telemetry": re.compile(
                r"\b(revLog|syslog|logError|logInfo|logWarn|logDebug|mergLog|rreLog|lcLog)\b",
                re.I,
            ),
            # 39. print_hits: Amateur space debris (puts to message box without target).
            "print_hits": re.compile(
                r'^[ \t]*put\s+(?:"[^"]*"|[a-zA-Z0-9_]+)[ \t]*$', re.I | re.M
            ),
            # 40. cast_hits: English-style type checking.
            "cast_hits": re.compile(r"\bis\s+(?:not\s+)?a\b|\bis\s+strictly\b", re.I),
            # 41. bailout_hits: Hard detonations.
            "bailout_hits": re.compile(r"\b(exit\s+to\s+top|quit|throw|abort)\b", re.I),
            # 42. halt_hits: Temporal Duct Tape (Blocking wait).
            "halt_hits": re.compile(
                r"\bwait\s+(?:for[ \t]+)?\d+\s+[^ \t\n]+?(?!\s+with\s+messages)\b", re.I
            ),
            # 43. bitwise_hits: Sub-Atomic Math.
            "bitwise_hits": re.compile(
                r"\b(bitAnd|bitOr|bitXor|bitNot|bitShiftLeft|bitShiftRight)\b", re.I
            ),
            # 44. sync_locks: Barricades.
            "sync_locks": re.compile(
                r"\b(lock\s+screen|lock\s+messages|lock\s+errordialogs)\b", re.I
            ),
            # 45. freeze_hits: Data Cryogenics.
            "freeze_hits": re.compile(r"\b(constant\s+)\b", re.I),
            # 46. cleanup: The Janitor.
            "cleanup": re.compile(
                r"\b(delete\s+variable|close\s+file|stop\s+using|remove\s+script)\b",
                re.I,
            ),
            # 47. encapsulation: The Vault.
            "encapsulation": re.compile(r"\b(private\s+)\b", re.I),
            # 48. listeners: The Sinks.
            "listeners": re.compile(r"^[ \t]*on\s+[a-zA-Z0-9_-]+", re.I | re.M),
            # 49. test_skip: Safety Theater.
            "test_skip": re.compile(r"\b(skip\s+test)\b", re.I),
        },
    },
    "objective-c": {
        "_meta": {
            "target_version": "Objective-C 2.0 (ARC) & Modern Runtime",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard sources, Objective-C++ files (.mm), and shared C/C++ headers.
        "extensions": [".m", ".mm", ".h"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Objective-C executes natively on Apple platforms; no extensionless configurations exist.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: The ultimate defense against MATLAB. Apple UI components and Xcode project files act as massive gravity anchors.
        "discriminators": [
            ".m",
            ".mm",
            "project.pbxproj",
            ".storyboard",
            ".xib",
            ".xcworkspace",
            "Podfile",
            "Cartfile",
        ],
        # EXECUTION SIGNATURES: Compiled natively via LLVM/Clang; no shebangs exist.
        "shebangs": [],
        "internal_discriminator": re.compile(
            r'^[ \t]*#import\s+[<"][^>"]+\.h[>"]|'
            r'^[ \t]*@(?:interface|implementation|protocol|property|class)\b', 
            re.M
        ),
        # UPGRADED: Maps to Family 1 (Standard C-Style)
        # Rationale: Uses standard '//' for line-level literature and '/*' '*/' for blocks.
        "lexical_family": "std_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            "_line_anchor": re.compile(r"//"),
            "_inline_comment": re.compile(r"//"),
            "_block_start": re.compile(r"/\*"),
            "_block_end": re.compile(r"\*/"),
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch: Decisions that split flow. Includes Obj-C specific @try/@catch blocks.
            "branch": re.compile(
                r"\b(if|else|switch|case|default|for|while|do|break|continue|return|goto|@try|@catch|@finally)\b|&&|\|\||\?"
            ),
            # 2. args: Coupling Mass. Captures method parameters (colons), C-style args, and Blocks (^).
            "args": re.compile(
                r":\s*\([^)]+\)\s*[a-zA-Z_]\w*|\^[ \t]*(?:[a-zA-Z_]\w*\s*)?\([^)]*\)|\b[a-zA-Z_]\w*\s*\([^)]*\)\s*(?:\{|;)"
            ),
            # 3. linear: Smooth Path. Structural boundaries defining interface, implementation, and memory types.
            "linear": re.compile(
                r"\b(@interface|@implementation|@protocol|@end|@synthesize|@dynamic|@class|@import|typedef|struct|enum|union|__block|__weak|__strong)\b"
            ),
            # 4. func_start: Satellite Spawner. Anchors executable logic.
            # The Critical Fix: Compiled with re.M and optional return types for TBL / NeXTSTEP syntax
            "func_start": re.compile(
                r"^[ \t]*[-+]\s*(?:\([^)]+\))?\s*([a-zA-Z_]\w*)(?=[ \t]*[:\{;]|\n|$)|"
                r"^[ \t]*(?:static\s+|inline[ \t]+)?(?:[a-zA-Z_]\w*(?:\s*\*+)?\s+)+([a-zA-Z_]\w*)(?=\s*\()",
                re.M,
            ),
            # 5. class_start: Entity Census. Defines OO boundaries.
            "class_start": re.compile(
                r"^[ \t]*(?:@interface|@implementation|@protocol)\s+([a-zA-Z_]\w*)(?=[ \t]*[:(<{\n]|$)",
                re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety: Cyan Fortification. ARC memory qualifiers and Cocoa/NeXT Assertions.
            "safety": re.compile(
                r"\b(@try|@catch|@finally|__weak|__strong|__auto_type|NSAssert|NSParameterAssert|NSError|nil|Nil)\b"
            ),
            # 7. safety_neg: Fractures. Bypassing ARC, raw void pointers, and dangerous dynamic selectors.
            "safety_neg": re.compile(
                r"\b(__unsafe_unretained|unsafe_unretained|id|void\s*\*|performSelector:|performSelector:withObject:)\b|!\s*[;,\]\)\.]|#pragma\s+clang\s+diagnostic\s+ignored"
            ),
            # 8. danger: Heavy Load. Process killers.
            "danger": re.compile(r"\b(abort|exit)\b"),
            # 9. io: Boundaries. Disk, Network, and URL fetching (Includes NeXTSTEP NX prefixes & TBL WWW wrappers).
            "io": re.compile(
                r"\b(NSFileHandle|NSFileManager|NSURLSession|NSURLConnection|NSData|NXNetPath|NXSocket|NXStream|NXFile|HTLoad|HyperText|HTGet|socket|connect|send|recv)\b"
            ),
            # 10. api: Event Horizon. Exposed interface/C-level exports and Interface Builder hooks.
            "api": re.compile(
                r"\b(FOUNDATION_EXPORT|UIKIT_EXTERN|OBJC_EXPORT|extern)\b|@property|IBOutlet|IBAction"
            ),
            # 11. flux: Boiling Plasma. State mutation (Property setters and raw assignments).
            "flux": re.compile(
                r"\b(?:self\.)?[a-zA-Z_]\w*[ \t]*=|\[self\s+set[A-Z]\w*:|(?:\+\+|--)"
            ),
            # 12. graveyard: Necrosis. Commented out structural code.
            "graveyard": re.compile(
                r"//[ \t]*(?:@interface|@implementation|\[|if|NSLog|- \()|/\*[ \t]*(?:@interface|@implementation|\[|if|NSLog|- \()"
            ),
            # 13. doc: Intent. Structured documentation (Includes NeXT style).
            "doc": re.compile(r"/\*\*|///|/\*!|@param|@return|@brief|@discussion"),
            # 14. test: Verification. Unit testing framework markers (OCUnit/XCTest).
            "test": re.compile(
                r"\b(XCTest|XCTestCase|XCTAssert[A-Za-z]*|SenTestCase|STAssert[A-Za-z]*)\b|\b(?:setUp|tearDown)\s*\("
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency: Temporal Static. GCD (Grand Central Dispatch), NSOperation, and Locks.
            "concurrency": re.compile(
                r"\b(dispatch_async|dispatch_sync|dispatch_once|dispatch_queue_t|NSOperation|NSThread|@synchronized|NSLock|NXConditionLock)\b"
            ),
            # 16. ui_framework: View Layer. Cocoa, UIKit, and AppKit hierarchies (Includes legacy NX classes).
            "ui_framework": re.compile(
                r"\b(UIView|UIViewController|UIWindow|NSView|NSWindow|NXWindow|NXApp|NXBrowser|NXText|Text|ScrollView|HyperText|WorldWideWeb|SGML)\b"
            ),
            # 17. closures: Functional Depth. Objective-C Blocks.
            "closures": re.compile(r"\^[ \t]*(?:[a-zA-Z_]\w*\s*)?\s*\([^)]*\)[ \t]*\{"),
            # 18. globals: Shared Void. Singleton/Shared instance access.
            "globals": re.compile(
                r"\b(extern|NSUserDefaults|NXDefaults|\[UIApplication\s+sharedApplication\]|\[NSWorkspace\s+sharedWorkspace\]|NXApp)\b"
            ),
            # 19. decorators: Metadata Hooks. Attributes and Property decorators.
            "decorators": re.compile(
                r"\b__attribute__\s*\(\([^)]*\)\)|@property\s*\([^)]+\)"
            ),
            # 20. generics: Type Abstractions. Lightweight generics (introduced in Xcode 7).
            "generics": re.compile(r"<\s*[A-Z][^>]*\s*\*?\s*>"),
            # 21. comprehensions: High-Density Loops. Block-based array/set enumeration.
            "comprehensions": re.compile(
                r"\b(enumerateObjectsUsingBlock:|filteredArrayUsingPredicate:|makeObjectsPerformSelector:)\b"
            ),
            # 22. scientific: Compute Core. C-Math and CoreGraphics structs.
            "scientific": re.compile(
                r"\b(math\.h|sin|cos|tan|sqrt|exp|log|abs|NSDecimalNumber|CGVector|CGAffineTransform|CGPoint|CGRect|CGSize|NXRect|NXSize)\b"
            ),
            # 23. heat_triggers: Thermal Radiation. Objective-C Runtime Swizzling and dynamic messaging.
            "heat_triggers": re.compile(
                r"\b(objc_msgSend|performSelector|method_exchangeImplementations|class_addMethod|objc_allocateClassPair|isa|object_setClass)\b|<objc/runtime\.h>"
            ),
            # 24. import: Gravity Links. Module and header inclusion.
            "import": re.compile(r"^[ \t]*(?:#import|#include|@import)\b", re.M),
            
            "_dependency_capture": re.compile(r"^[ \t]*(?:#import|#include)\s*(?:<([^>]+)>|[\"']([^\"']+)[\"'])|^[ \t]*@import\s+([\w.]+)", re.M),
            
            # 25. ownership: Authorship metadata.
            "ownership": re.compile(
                r"\b(?:Created by|@author|Author:|Copyright|Tim Berners-Lee)\b", re.I
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit|RFC|W3C|CERN|TBL|ENQUIRE)[^\]]*\]|\b(?:WorldWideWeb|HyperText\s+Proposal|NeXTSTEP\s+Docs)\b",
                re.I,
            ),
            "civil_war": None,
            "ssr_boundaries": re.compile(
                r"\b(WOComponent|WOResponse|WOContext|WOApplication|WODirectAction|WebObjects)\b"
            ),
            "events": re.compile(
                r"\b(NSNotificationCenter|addObserver|postNotification|NXApp\s+run|sendEvent)\b"
            ),
            "dependency_injection": re.compile(
                r"\b(TyphoonComponentFactory|TyphoonDefinition|JSObjection|inject:|initWithDependency:)\b"
            ),
            "macros": re.compile(
                r"^[ \t]*#(?:define|undef|ifdef|ifndef|if|elif|else|endif|pragma)\b",
                re.M,
            ),
            "pointers": re.compile(
                r"->|&\w+|\b(?:id|Class|SEL|IMP)\b|(?<=[=(,])[ \t]*\*[a-zA-Z_]\w*"
            ),
            "memory_alloc": re.compile(
                r"\b(alloc|init|new|copy|mutableCopy|retain|malloc|calloc|NX_MALLOC|NX_ZONEMALLOC|NSZoneMalloc)\b"
            ),
            "inline_asm": re.compile(
                r"\b(?:__asm__|asm|__asm)\b(?:\s+volatile)?\s*\([^)]*\)"
            ),
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry: Professional diagnostics.
            "telemetry": re.compile(
                r"\b(os_log|OSLog|DDLogInfo|DDLogError|DDLogWarn|DDLogDebug|syslog)\b"
            ),
            # 39. print_hits: Amateur space debris.
            "print_hits": re.compile(r"\b(printf|fprintf|NXPrintf|NSLog)\b"),
            # 40. cast_hits: "Trust Me" Tax. Explicit type coercion.
            "cast_hits": re.compile(
                r"\(\s*[A-Za-z_]\w*\s*\*?\s*\)\s*[a-zA-Z_$]|typeof\b"
            ),
            # 41. bailout_hits: Detonators. Aborting execution context.
            "bailout_hits": re.compile(r"\b(@throw|abort|exit)\b"),
            # 42. halt_hits: Temporal Duct Tape. Forcing threads to sleep.
            "halt_hits": re.compile(r"\b(sleep|usleep|nanosleep)\s*\("),
            # 43. bitwise_hits: Sub-Atomic Math.
            "bitwise_hits": re.compile(r"(?<!&)&(?!&)|(?<!\|)\|(?!\|)|<<|>>|\^|~"),
            # 44. sync_locks: Barricades. Coordinated threading logic.
            "sync_locks": re.compile(
                r"\b(@synchronized|NSLock|NSRecursiveLock|NSConditionLock|dispatch_semaphore_wait)\b"
            ),
            # 45. freeze_hits: Data Cryogenics. Immutability.
            "freeze_hits": re.compile(r"\b(const|readonly|immutable)\b"),
            # 46. cleanup: The Janitor. Resource release (Crucial for MRC NeXT era).
            "cleanup": re.compile(r"\b(dealloc|release|autorelease|free|NX_FREE)\b"),
            # 47. encapsulation: The Vault. Hiding logic from the application.
            "encapsulation": re.compile(r"\b(@private|@protected|@package)\b"),
            # 48. listeners: The Sinks. Waiting for state broadcasts.
            "listeners": re.compile(
                r"\b(addObserver:|observeValueForKeyPath:|subscribeNext:)\b"
            ),
            # 49. test_skip: Safety Theater.
            "test_skip": re.compile(r"\b(XCTSkip|xit|xdescribe)\b"),
        },
    },
    "makefile": {
        "_meta": {
            "target_version": "GNU Make 4.4+",
            "last_updated": "2026-02-28",
            "blueprint_version": "v6.2.2",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard make extensions, definitions, and includes.
        "extensions": [".mk", ".mak", ".make", ".def"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: The universally recognized, extensionless build configurations that are executed as pure code.
        "exact_matches": [
            "Makefile",
            "makefile",
            "GNUmakefile",
            "Kbuild",
            "Makeconf",
            "Makevars",
        ],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Sibling configurations acting as gravity anchors to resolve ambiguous .mk includes.
        "discriminators": ["Makefile", "makefile", "configure.ac", "CMakeLists.txt"],
        # EXECUTION SIGNATURES: Interpreters found on Line 1 for executable make scripts.
        "shebangs": ["make", "gmake"],
        # UPGRADED: Maps to Family 3 (Pure Hash)
        # Rationale: Make natively uses '#' exclusively for line-level comments.
        "lexical_family": "pure_hash",
        "rules": {
            # Makefiles natively use '#' for both line and inline comments.
            "_line_anchor": re.compile(r"#"),
            "_inline_comment": re.compile(r"#"),
            # EXPLICIT: Makefiles lack native multi-line block comment delimiters.
            "_block_start": None,
            "_block_end": None,
            # --------------------------------------------------------------------------
            # 1. GEOMETRY & SHAPE (The Physical Stars)
            # --------------------------------------------------------------------------
            # Captures Make conditionals and typical inline shell conditional branches.
            "branch": re.compile(
                r"^[ \t]*(?:ifeq|ifneq|ifdef|ifndef|else|endif)\b|\b(?:if|elif|for|while|case)\b|&&|\|\|",
                re.M,
            ),
            # Make dynamically accesses arguments within $(call macro, args...) or positional $1, $2 inside recipes.
            "args": re.compile(r"\$\([0-9]+\)|\$[0-9]\b|\$\(call[ \t]+[a-zA-Z0-9_.-]+"),
            # Smooth structural boundaries: variable assignments (:=, =, ?=) and native structural controls like vpath.
            # Explicitly excludes the append operator `+=` which belongs in flux.
            "linear": re.compile(
                r"^[ \t]*[a-zA-Z0-9_.-]+[ \t]*(?::|\?|::)?=(?![ \t]*=)|^[ \t]*(?:vpath|undefine)\b",
                re.M,
            ),
            # 4. func_start (The Satellite Spawner)
            # Strict capture group and positive lookahead applied for both Obj-C methods and C-functions.
            "func_start": re.compile(
                r"^[ \t]*(?!\.(?:PHONY|POSIX|SECONDARY|PRECIOUS|DELETE_ON_ERROR|KEEP_STATE|NOTPARALLEL|WAIT|SILENT|EXPORT_ALL_VARIABLES|IGNORE|SUFFIXES|DEFAULT|PRECIOUS|INTERMEDIATE|SECONDARY|SECONDEXPANSION)\b)"
                r"([a-zA-Z0-9_./%-]+)(?=[ \t]*::?)",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            # Defines OO boundaries. Strict capture group and positive lookahead applied.
            "class_start": None,
            # --------------------------------------------------------------------------
            # 2. STRUCTURAL INTEGRITY & TECH DEBT (Cyan Fortifications & Red Fragility)
            # --------------------------------------------------------------------------
            # Defensive programming: Executing internal logic checks, asserting tool paths, or using safety system states.
            "safety": re.compile(
                r"^[ \t]*\.(?:POSIX|SECONDARY|PRECIOUS|DELETE_ON_ERROR|KEEP_STATE)\b|\bcommand[ \t]+-v\b|\$\((?:if|or|and)[ \t]+",
                re.M,
            ),
            # Bypassing safety: Prefixing recipes with `-` to swallow errors, or forcefully exiting true via shell logic.
            "safety_neg": re.compile(
                r"^\t[ \t]*-[a-zA-Z0-9_./$]|\|\|[ \t]*(?:true|exit[ \t]+0)\b", re.M
            ),
            # Heavily destructive sequence patterns or overriding permissions. (Eval is categorized under heat_triggers).
            "danger": re.compile(
                r"\bsudo[ \t]+|\brm[ \t]+-[rR]?[fF][ \t]+(?:/|\$[{(])|\bkill[ \t]+-9\b"
            ),
            # Interacting directly with outputs, networks, or the disk filesystem.
            "io": re.compile(
                r"\$\((?:file|wildcard)[ \t]+|\b(?:curl|wget|scp|rsync|tar|unzip|mkdir|cp|mv)\b|>>?[ \t]*[^ \t\n/]+"
            ),
            # Exposed architecture limits (Exporting variables globally or explicit lifecycle public endpoints).
            "api": re.compile(
                r"^[ \t]*(?:\.PHONY|export\b|(?:all|install|build|clean|test|run)[ \t]*::?)",
                re.M,
            ),
            # Mutating variable state by appending (+=) or shell assignment (!=). (The Yin to freeze_hits).
            "flux": re.compile(r"^[ \t]*[a-zA-Z0-9_.-]+[ \t]*(?:\+|!)=", re.M),
            # Ghost targets, commented out shell logic, or commented conditional Make directives.
            "graveyard": re.compile(
                r"^[ \t]*#[ \t]*(?:[a-zA-Z0-9_./%-]+[ \t]*::?|[a-zA-Z0-9_.-]+[ \t]*(?::|\?|::)?=|\b(?:ifeq|ifneq|ifdef|ifndef|include)\b)",
                re.M,
            ),
            # Structured self-documenting makefile comments typically utilizing a double hash block.
            "doc": re.compile(r"^[ \t]*##[ \t]+[^ \t\n]+", re.M),
            # Testing endpoints natively executing verifications or launching language-specific test suites.
            "test": re.compile(
                r"\b(?:npm[ \t]+test|yarn[ \t]+test|pytest|go[ \t]+test|cargo[ \t]+test|make[ \t]+test)\b",
                re.M | re.I,
            ),
            # --------------------------------------------------------------------------
            # 3. DOMAIN & ARCHITECTURE (Architectural Style and Abstractions)
            # --------------------------------------------------------------------------
            # Setting explicitly threaded job pipelines, detaching processes to background, or asserting waits.
            "concurrency": re.compile(
                r"\b(?:make[ \t]+-j|xargs[ \t]+-P|wait)\b|&[ \t]*$|\$\(MAKE\)[ \t]+-j",
                re.M,
            ),
            "ui_framework": None,
            "closures": None,
            # Core global state built-in environments spanning the build system.
            "globals": re.compile(
                r"\$\((?:MAKE|MAKEFLAGS|MAKECMDGOALS|CURDIR|SHELL|PATH|USER|HOME|PWD|\.VARIABLES)\)"
            ),
            "decorators": None,
            "generics": None,
            # High-density text manipulating algorithms native to GNU Make iterating through variable spaces.
            "comprehensions": re.compile(
                r"\$\((?:foreach|filter|filter-out|patsubst|subst|addprefix|addsuffix|words|firstword|lastword|sort|findstring|join)[ \t]+"
            ),
            # Launching explicit calculation boundaries outside the Make environment natively.
            "scientific": re.compile(r"\b(?:bc|expr|awk)\b|\$\(shell[ \t]+expr[ \t]+"),
            # Extremely dense meta-programming manipulations drastically raising cognitive load during debugging.
            "heat_triggers": re.compile(
                r"\$\((?:eval|call|value|origin|flavor|shell)[ \t]+|\.SECONDEXPANSION:"
            ),
            # Linking isolated segments of the graph execution via modular file resolution.
            "import": re.compile(r"^[ \t]*-?(?:include|sinclude)[ \t]+[^ \t\n]+", re.M),
            
            "_dependency_capture": re.compile(r"^[ \t]*-?(?:include|sinclude)[ \t]+([^\s#]+)", re.M),
            
            # Metadata anchoring authorship and structural domain owners.
            "ownership": re.compile(
                r"^[ \t]*#[ \t]*(?:@author\b|author:|maintainer:|created by:)",
                re.I | re.M,
            ),
            # --------------------------------------------------------------------------
            # 4. SPECIALIZED EXTRACTIONS (Sub-Equations and Low-Level/System)
            # --------------------------------------------------------------------------
            "planned_debt": re.compile(r"\b(?:todo|wip|stub|implement)\b", re.I),
            "fragile_debt": re.compile(r"\b(?:hack|fixme|xxx|kludge|ugly|wtf)\b", re.I),

            "spec_exposure": re.compile(r"\[(?:spec-[0-9]+|audit|spec)\]", re.I),
            # Strict tracking of Indentation structural boundaries. (Make strictly demands Tabs, mapping space usage catches severe fragmentation).
            "civil_war": None,
            "ssr_boundaries": None,
            "events": None,
            "dependency_injection": None,
            # Expanding structural blocks dynamically into recipes prior to runtime evaluation.
            "macros": re.compile(r"^[ \t]*define[ \t]+[a-zA-Z0-9_.-]+", re.M),
            "pointers": None,
            "memory_alloc": None,
            "inline_asm": None,
            # --------------------------------------------------------------------------
            # 5. THERMODYNAMIC BALANCE (Yin & Yang Forces)
            # --------------------------------------------------------------------------
            # Emitting pure, safe structural observability that does not risk halting or crashing the graph execution.
            "telemetry": re.compile(r"\$\(info[ \t]+[^)\n]*\)"),
            # Standard output commands echoing transient debris to the shell execution log.
            "print_hits": re.compile(
                r"^[ \t]*@?(?:echo|printf)[ \t]+|\$\(warning[ \t]+[^)\n]*\)", re.M
            ),
            "cast_hits": None,
            # System detonators specifically intended to abort the build flow if preconditions are failed natively or via shell.
            "bailout_hits": re.compile(
                r"\$\(error[ \t]+[^)\n]*\)|\bexit[ \t]+[1-9][0-9]*\b|\bfalse\b"
            ),
            # Temporal duct tape strictly applying forced pausing.
            "halt_hits": re.compile(r"\bsleep[ \t]+[0-9]+"),
            "bitwise_hits": None,  # Kept null as Bash pipe IPC limits logic math precision.
            # Explicit locks halting temporal thread races. (The Yang to concurrency).
            "sync_locks": re.compile(
                r"^[ \t]*\.(?:NOTPARALLEL|WAIT)[ \t]*::?|\bflock[ \t]+", re.M
            ),
            # Enforcing strict immutability bounds on state configuration. (The Yang to flux).
            "freeze_hits": re.compile(r"^[ \t]*override[ \t]+[a-zA-Z0-9_.-]+", re.M),
            # Janitor routines ripping apart build artifacts and cleanly tearing down output paths. (The Yang to io).
            "cleanup": re.compile(
                r"^[ \t]*(?:dist)?clean[ \t]*::?|\brm[ \t]+-[a-zA-Z]*f[a-zA-Z]*\b", re.M
            ),
            # The Vault explicitly hiding scope logic away from external API leakage boundaries. (The Yang to api).
            "encapsulation": re.compile(
                r"^[ \t]*(?:unexport[ \t]+[a-zA-Z0-9_.-]+|[a-zA-Z0-9_.-]+[ \t]*:[ \t]*private[ \t]+|\.SILENT[ \t]*:)",
                re.M,
            ),
            # Subscribing the file system to continuous native observation hooks.
            "listeners": re.compile(r"\b(?:inotifywait|watch)[ \t]+"),
            # Safety theater actively bypassing execution verifications during a test endpoint invocation.
            "test_skip": re.compile(
                r"\b(?:SKIP(?:_TESTS?)?|XFAIL)[ \t]*=[ \t]*[1TtYy]|\bpytest[ \t]+-k[ \t]+not\b|--skip",
                re.I,
            ),
        },
    },
    "abap": {
        "_meta": {
            "target_version": "ABAP 2025 (ABAP Cloud / RAP / Modern 7.5x+ Syntax)",
            "last_updated": "2026-02-18",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard Advanced Business Application Programming sources and modern Core Data Services.
        "extensions": [".abap", ".asddls"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: ABAP is executed within the SAP environment; no extensionless exact configurations exist.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: SAP deployment artifacts acting as gravity anchors.
        "discriminators": [".abap", "package.devc.xml", ".apc"],
        # EXECUTION SIGNATURES: Executed exclusively within the SAP NetWeaver/ABAP platform; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 7 (The Positional Ancients)
        # Rationale: Strictly fixed-format legacy constraints. The engine must monitor Column 1
        # for an asterisk '*' to identify line-level Ghost Mass, while allowing '"' for inline.
        "lexical_family": "positional",
        "rules": {
            "_line_anchor": re.compile(r"^\*"),
            "_inline_comment": re.compile(r"\""),
            "_block_start": None,  # ABAP has no standard multi-line block comments
            "_block_end": None,
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch: decisions that split flow. Includes modern COND/SWITCH expressions.
            "branch": re.compile(
                r"^[ \t]*(IF|ELSE|ELSEIF|CASE|WHEN|WHILE|DO|LOOP\s+AT|TRY|CATCH|CLEANUP|CHECK|EXIT|CONTINUE|RETURN|COND|SWITCH)\b",
                re.I | re.M,
            ),
            # 2. args: Coupling Mass. Captures explicit parameter binding keywords.
            "args": re.compile(
                r"\b(IMPORTING|EXPORTING|CHANGING|RETURNING|RECEIVING|EXCEPTIONS)\s+(?:VALUE\s*\([^)]*\)[ \t]+)?[a-zA-Z_][a-zA-Z0-9_-]*",
                re.I,
            ),
            # 3. linear: Smooth Path. Structural boundaries. EXCLUDES access modifiers and constants.
            "linear": re.compile(
                r"^[ \t]*(DATA|TYPES|FIELD-SYMBOLS|CLASS|INTERFACE|METHOD|FORM|FUNCTION|MODULE|REPORT|PROGRAM|IMPORT|EXPORT)\b",
                re.I | re.M,
            ),
            # 4. func_start: Satellite Spawner. Anchors executable logic. EXCLUDES structural headers.
            "func_start": re.compile(
                r"^[ \t]*(?!(?:CLASS|INTERFACE|DATA|TYPES|CONSTANTS)\b)(?:METHOD|FORM|FUNCTION|MODULE)\s+([a-zA-Z0-9_~-]+)(?=[ \t\n\.]|$)",
                re.I | re.M,
            ),
            # 5. class_start: Entity Census. Defines OO boundaries and RAP CDS Entities.
            "class_start": re.compile(
                r"^[ \t]*(?:CLASS|INTERFACE)\s+([a-zA-Z0-9_-]+)(?=[ \t]+DEFINITION|[ \t\n\.]|$)|^[ \t]*DEFINE\s+(?:ROOT[ \t]+)?(?:VIEW|ENTITY|PROJECTION\s+VIEW|BEHAVIOR)\s+([a-zA-Z0-9_-]+)",
                re.I | re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety: Cyan Fortification. Binding checks and authorization boundaries.
            "safety": re.compile(
                r"\b(TRY|CATCH|CLEANUP|ASSERT|AUTHORITY-CHECK|IS\s+BOUND|IS\s+ASSIGNED|IS\s+NOT\s+INITIAL|FINAL|READ-ONLY)\b",
                re.I,
            ),
            # 7. safety_neg: Fractures. Actively bypassing safety (casting/unchecked generics).
            "safety_neg": re.compile(
                r"\b(UNASSIGNED|TYPE\s+ANY|TYPE\s+REF\s+TO\s+DATA|IGNORE\s+ERRORS)\b|ASSIGN\s+[^\n;]+\s+TO\s+<[^>]+>\s+CASTING",
                re.I,
            ),
            # 8. danger: Heavy Load. Raw SQL/Kernel bypasses and mass deletion.
            "danger": re.compile(
                r"\b(SYSTEM-CALL|EXEC\s+SQL|DELETE\s+FROM|TRUNCATE|GENERATE\s+SUBROUTINE\s+POOL)\b",
                re.I,
            ),
            # 9. io: Boundaries. Database interaction and File datasets.
            "io": re.compile(
                r"^[ \t]*(SELECT|INSERT\s+(?:INTO\b)?|UPDATE\b|MODIFY\b|OPEN\s+DATASET|TRANSFER|READ\s+DATASET|CLOSE\s+DATASET|CL_HTTP_CLIENT|CL_WEB_HTTP_CLIENT)\b",
                re.I | re.M,
            ),
            # 10. api: Event Horizon. Exposed RFCs, OData publishing, and Public sections.
            "api": re.compile(
                r"\b(REMOTE\s+FUNCTION|@OData\.publish|DEFINE\s+VIEW|DEFINE\s+SERVICE|EXPOSED|PUBLIC\s+SECTION)\b",
                re.I,
            ),
            # 11. flux: Boiling Plasma. State mutation (The core of ABAP data manipulation).
            "flux": re.compile(
                r"^[ \t]*(MOVE|MOVE-CORRESPONDING|APPEND|MODIFY\s+TABLE|DELETE\s+TABLE)\b|^[ \t]*INSERT\s+[^\n;]+\s+INTO\s+TABLE",
                re.I | re.M,
            ),
            # 12. graveyard: Necrosis. Commented out structural logic (supports * and ").
            "graveyard": re.compile(
                r'^[ \t]*\*[ \t]*(?:DATA|METHOD|IF|SELECT|WRITE)\b|"[ \t]*(?:DATA|METHOD|IF|SELECT|WRITE)\b',
                re.I | re.M,
            ),
            # 13. doc: Intent. ABAP Doc annotations and metadata headers.
            "doc": re.compile(
                r'^"!\s*@(?:parameter|raising|return)|\b(?:AUTHOR|DESCRIPTION|PURPOSE|REMARKS):\b',
                re.I | re.M,
            ),
            # 14. test: Verification. ABAP Unit markers and test-injection.
            "test": re.compile(
                r"\b(FOR\s+TESTING|RISK\s+LEVEL|DURATION\s+SHORT|CL_ABAP_UNIT_ASSERT|ZCL_ABAP_UNIT)\b",
                re.I,
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency: Temporal Static. Async RFCs and background tasks.
            "concurrency": re.compile(
                r"\b(STARTING\s+NEW\s+TASK|ENQUEUE_|DEQUEUE_|WAIT\s+UP\s+TO)\b|CALL\s+FUNCTION\s+[^\n;]+\s+IN\s+BACKGROUND\s+TASK",
                re.I,
            ),
            # 16. ui_framework: View Layer. Screen programming and HTML viewers.
            "ui_framework": re.compile(
                r"\b(CALL\s+SCREEN|SELECTION-SCREEN|PARAMETERS|WDDOMODIFYVIEW|CL_GUI_HTML_VIEWER|CL_SALV_TABLE)\b",
                re.I,
            ),
            # 17. closures: Functional Depth. (ABAP lacks anonymous closures).
            "closures": None,
            # 18. globals: Shared Void. Global program data and the system registry.
            "globals": re.compile(
                r"\b(TABLES|STATICS|CLASS-DATA|SY-[A-Z0-9_]+)\b", re.I
            ),
            # 19. decorators: Metadata Hooks. CDS and class annotations.
            "decorators": re.compile(r"@[A-Za-z0-9_.]+(?:\([^)]*\))?", re.I),
            # 20. generics: Type Abstractions. Generic data references and field symbols.
            "generics": re.compile(
                r"\b(TYPE\s+ANY(?:\s+TABLE)?|TYPE\s+INDEX\s+TABLE|TYPE\s+STANDARD\s+TABLE|TYPE\s+REF\s+TO\s+DATA)\b",
                re.I,
            ),
            # 21. comprehensions: High-Density Loops. Modern constructor expressions.
            "comprehensions": re.compile(
                r"\b(?:VALUE|REDUCE|FILTER|CORRESPONDING|NEW)\s+#?\s*\(|\bFOR\s+[a-zA-Z_]\w*\s+IN\b",
                re.I,
            ),
            # 22. scientific: Compute Core. Standard numerical built-ins.
            "scientific": re.compile(
                r"\b(ABS|SQRT|LOG|EXP|SIN|COS|TAN|ROUND|CEIL|FLOOR|DECFLOAT16|DECFLOAT34)\b",
                re.I,
            ),
            # 23. heat_triggers: Thermal Radiation. RTTS and Dynamic assignment logic.
            "heat_triggers": re.compile(
                r"\b(CL_ABAP_TYPEDESCR|CL_ABAP_CLASSDESCR|ASSIGN\s+\([a-zA-Z0-9_-]+\)\s+TO|GENERATE\s+SUBROUTINE\s+POOL)\b",
                re.I,
            ),
            # 24. import: Gravity Links. Includes and type pools.
            "import": re.compile(r"\b(INCLUDE|TYPE-POOLS)\b", re.I),
            
            "_dependency_capture": re.compile(r"\b(?:INCLUDE|TYPE-POOLS)\s+([A-Za-z0-9_/]+)", re.I),
            
            # 25. ownership: Authorship indicators.
            "ownership": re.compile(
                r"(?:AUTHOR|CREATED\s+BY|MAINTAINER|Tim Berners-Lee):\s+([^\n]+)",
                re.I | re.M,
            ),
            # --- 🌌 PHASE 4: THE EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            # 26. planned_debt: The Promise. Future work markers.
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            # 27. fragile_debt: The Fracture. Admitted fragility or hacks.
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure: Map vs. Territory. Audit tags and architecture docs.
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)\]|\b(?:WorldWideWeb|RFC|W3C|CERN|TBL|ENQUIRE)\b",
                re.I,
            ),
            # 30. civil_war: Indentation Tracker. Tabs vs 2-space standardization.
            "civil_war": None,
            # 31. ssr_boundaries: View Horizon. ICF and BSP request handlers.
            "ssr_boundaries": re.compile(
                r"\b(IF_HTTP_EXTENSION~HANDLE_REQUEST|CL_BSP_CONTEXT|CL_BSP_RUNTIME|IF_HTTP_REQUEST|IF_HTTP_RESPONSE|HTML_STRING)\b",
                re.I,
            ),
            # 32. events: Pub/Sub Network. Native OO event architecture.
            "events": re.compile(
                r"\b(RAISE\s+EVENT|SET\s+HANDLER)\b|FOR\s+EVENT\s+[^\n;]+\s+OF", re.I
            ),
            # 33. dependency_injection: Inversion of Control. BAdIs and Test Doubles.
            "dependency_injection": re.compile(
                r"\b(GET\s+BADI|CALL\s+BADI|CL_BADI_BASE|CL_ABAP_TESTDOUBLE)\b", re.I
            ),
            # 34. macros: Preprocessor Hooks. ABAP macro definitions.
            "macros": re.compile(
                r"^[ \t]*DEFINE\s+[a-zA-Z0-9_-]+\.|^[ \t]*END-OF-DEFINITION\s*\.",
                re.I | re.M,
            ),
            # 35. pointers: Memory Map. Field-Symbols and data references.
            "pointers": re.compile(
                r"<[A-Za-z0-9_-]+>|->\*|\b(?:GET\s+REFERENCE\s+OF|REF\s+TO)\b", re.I
            ),
            # 36. memory_alloc: Manual Memory Management. Heap allocations.
            "memory_alloc": re.compile(
                r"\b(CREATE\s+OBJECT|CREATE\s+DATA|FREE|CLEAR)\b", re.I
            ),
            # 37. inline_asm: Bare Metal.
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry: Professional diagnostics.
            "telemetry": re.compile(
                r"\b(BAL_LOG_CREATE|BAL_DB_SAVE|CL_BALI_LOG|CL_BALI_MSG_SETTER)\b", re.I
            ),
            # 39. print_hits: Amateur space debris.
            "print_hits": re.compile(r"^[ \t]*(WRITE)\b", re.I | re.M),
            # 40. cast_hits: "Trust Me" Tax. Explicit casting and conversions.
            "cast_hits": re.compile(
                r"\b(?:CAST|CONV)\s*[a-zA-Z0-9_~-]*\s*#?\s*\(|ASSIGNING\s+<[^>]+>\s+CASTING",
                re.I,
            ),
            # 41. bailout_hits: Detonators. Aborting execution or error messages.
            "bailout_hits": re.compile(
                r'\b(RAISE\s+EXCEPTION|MESSAGE\s+[^\n;]+\s+TYPE\s+[\'"][EX][\'"]|LEAVE\s+PROGRAM)\b',
                re.I,
            ),
            # 42. halt_hits: Temporal Duct Tape. Thread sleep.
            "halt_hits": re.compile(r"\bWAIT\s+UP\s+TO\b", re.I),
            # 43. bitwise_hits: Sub-Atomic Math.
            "bitwise_hits": re.compile(r"\b(BIT-AND|BIT-OR|BIT-XOR|BIT-NOT)\b", re.I),
            # 44. sync_locks: Barricades.
            "sync_locks": re.compile(r"\b(ENQUEUE_|DEQUEUE_)\b", re.I),
            # 45. freeze_hits: Data Cryogenics. Immutability (constants).
            "freeze_hits": re.compile(r"\b(CONSTANTS|FINAL|READ-ONLY)\b", re.I),
            # 46. cleanup: The Janitor.
            "cleanup": re.compile(
                r"^[ \t]*(FREE|CLEAR|CLOSE\s+DATASET)\b", re.I | re.M
            ),
            # 47. encapsulation: The Vault. Scope hiding.
            "encapsulation": re.compile(
                r"\b(PRIVATE\s+SECTION|PROTECTED\s+SECTION)\b", re.I
            ),
            # 48. listeners: The Sinks.
            "listeners": re.compile(r"\bFOR\s+EVENT\s+[^\n;]+\s+OF\b", re.I),
            # 49. test_skip: Safety Theater.
            "test_skip": re.compile(r"\b(IGNORE)\b", re.I),
        },
    },
    "xml": {
        "_meta": {
            "target_version": "Standard XML 1.0 / UI Layouts",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard data, schemas, stylesheets, vector graphics, Apple UI, and config files.
        "extensions": [
            ".xml",
            ".xsd",
            ".xsl",
            ".xslt",
            ".svg",
            ".storyboard",
            ".xib",
            ".plist",
            ".wsdl",
            ".config",
            ".jelly",
        ],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Universally recognized XML architectural and build manifests.
        "exact_matches": ["pom.xml", "build.xml", "AndroidManifest.xml", "phpunit.xml"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Primary sibling extensions to anchor standard data serialization and frameworks.
        "discriminators": [".xml", ".xsd", ".xsl", "pom.xml", "build.xml"],
        # EXECUTION SIGNATURES: XML is declarative data/markup; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 8 (Singular/Unique)
        # Rationale: (CORRECTION) Consolidated 'xml_angle' into 'singular'. Like HTML, XML
        # exclusively uses SGML-style block delimiters () for its Ghost Mass.
        "lexical_family": "singular",
        "rules": {},
    },
    "markdown": {
        "_meta": {
            "target_version": "CommonMark / GitHub Flavored / AsciiDoc",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard modern suffixes, legacy extensions, MDX, and AsciiDoc formats.
        "extensions": [".md", ".markdown", ".mdown", ".mkd", ".mdx", ".adoc", ".asciidoc"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: The universally recognized, extensionless repository documentation anchors.
        "exact_matches": ["README", "LICENSE", "CHANGELOG", "CONTRIBUTING", "SECURITY"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Static site generators and documentation build configs acting as gravity anchors.
        "discriminators": [
            ".md",
            ".mdx",
            "mkdocs.yml",
            "_config.yml",
            "docusaurus.config.js",
        ],
        # EXECUTION SIGNATURES: Markdown is declarative text; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 8 (Singular/Unique)
        # Rationale: (CORRECTION) Markdown relies entirely on HTML's SGML-style block comments ().
        # Mapping this to 'hybrid_dash' would cause the engine to miss hidden documentation mass.
        "lexical_family": "singular",
        "rules": {},
    },
    "csv": {
        "_meta": {"target_version": "Comma Separated Values", "status": "production"},
        # COMPREHENSIVE SURFACE AREA: Comma, tab, and pipe-separated value formats.
        "extensions": [".csv", ".tsv", ".psv"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Delimited data relies strictly on extensions.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Sibling datasets and data-science logic files acting as gravity anchors.
        "discriminators": [".csv", ".tsv", ".py", ".ipynb", ".R", ".m"],
        # EXECUTION SIGNATURES: CSV is purely static data; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 3 (Pure Hash)
        # Rationale: While strictly data, when CSVs *do* contain comments (supported by
        # parsers like Pandas or DuckDB), they almost exclusively use the '#' symbol at the start of a line.
        "lexical_family": "pure_hash",
        "rules": {},
    },
    "yaml": {
        "_meta": {"target_version": "YAML", "status": "production"},
        "extensions": [".yml", ".yaml", ".yamllint"],
        "exact_matches": [
            ".prettierrc",
            ".stylelintrc",
            "clang-format",
            ".clang-format",
        ],
        "discriminators": [
            "docker-compose.yml",
            ".gitlab-ci.yml",
            "kubernetes.yaml",
            "openapi.yaml",
        ],
        "shebangs": [],
        "lexical_family": "pure_hash",
        "rules": {
            # Optical splits preserved for metadata extraction
            "_line_anchor": re.compile(r"#"),
            "_inline_comment": re.compile(r"#"),
            "_block_start": None,
            "_block_end": None,
            # ALL CUSTOM LOGIC REGEXES DELETED.
        },
    },
    "pbtxt": {
        "_meta": {
            "target_version": "Protobuf Text Format",
            "last_updated": "2026-03-11",
            "blueprint_version": "6.30",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard Protobuf text and binary message formats used heavily in Google/Bazel ecosystems.
        "extensions": [".pbtxt", ".textproto", ".textpb", ".pb"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: PBTXT strictly relies on its extensions.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Standard .proto schema definitions and Bazel build files acting as gravity anchors.
        "discriminators": [".proto", "WORKSPACE", "BUILD.bazel", "BUILD"],
        # EXECUTION SIGNATURES: PBTXT is purely serialized message data; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 3 (Pure Hash)
        # Rationale: While standard .proto schemas use C-style (//) comments, the instantiated
        # Text Format (.pbtxt) strictly uses '#' for comments.
        "lexical_family": "pure_hash",
        "rules": {},
    },
    "yacc": {
        "_meta": {
            "target_version": "GNU Bison / Yacc / Flex",
            "last_updated": "2026-03-11",
            "blueprint_version": "v5.1",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Yacc/Bison parser grammars (.y) and Lex/Flex tokenizers (.l), plus their C++ variants (.ypp, .lpp).
        "extensions": [".y", ".yy", ".ypp", ".l", ".ll", ".lpp"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Parser generators rely strictly on extensions.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: The generated C/C++ outputs and standard build systems acting as gravity anchors.
        "discriminators": [
            ".c",
            ".cpp",
            ".h",
            "Makefile",
            "CMakeLists.txt",
            "configure.ac",
        ],
        # EXECUTION SIGNATURES: Grammars are compiled into C/C++ state machines; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 1 (Standard C-Style)
        # Rationale: Yacc and Lex files interleave grammar definitions with pure C/C++ code
        # blocks (enclosed in %{ %}), relying entirely on standard '/* */' and '//' comments.
        "lexical_family": "std_c",
        "rules": {
            "_line_anchor": re.compile(r"//"),
            "_inline_comment": re.compile(r"//"),
            "_block_start": re.compile(r"/\*"),
            "_block_end": re.compile(r"\*/"),
            # --- 🪐 PHASE 1: PHYSICS ENGINE ---
            "branch": re.compile(r"\b(if|else|switch|case|for|while|do)\b|\|"),
            "args": re.compile(r"\$\d+|\$\$"),
            "linear": re.compile(
                r"\b(return|goto|break|continue|%token|%type|%left|%right|%nonassoc)\b"
            ),
            # The Satellite Spawner: Anchors specifically onto Grammar Rules
            # Matches "rule_name :" or "rule_name:" at the start of a line
            "func_start": re.compile(r"^[ \t]*([a-zA-Z_]\w*)(?=[ \t]*:)", re.M),
            "class_start": None,
            # --- ⚠️ PHASE 2: RISK ENGINE ---
            "safety": re.compile(r"\b(assert|YYABORT|YYACCEPT|YYERROR)\b"),
            "safety_neg": re.compile(r"\b(goto|void\s*\*)\b"),
            "danger": re.compile(r"\b(abort|exit|YYNOMEM)\b"),
            "io": re.compile(r"\b(fopen|fclose|fread|fwrite|yyin|yyout|fprintf)\b"),
            "api": re.compile(r"\b(%define|%code|%provides|%requires)\b"),
            "flux": re.compile(r"(?<![=!<>])=(?![=])|\+\+|--"),
            "graveyard": re.compile(
                r"//[ \t]*(?:if|for|while|return|%token)\b|/\*[ \t]*(?:if|for|while|%token)"
            ),
            "doc": re.compile(r"/\*\*|@param|@return"),
            "test": None,
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS ---
            "concurrency": None,
            "ui_framework": None,
            "closures": None,
            "globals": re.compile(r"\b(yylval|yylloc|yynerrs|yydebug)\b"),
            "decorators": None,
            "generics": re.compile(r"<[a-zA-Z_][a-zA-Z0-9_]*>"),  # Captures %type <val>
            "comprehensions": None,
            "scientific": None,
            "heat_triggers": re.compile(r"%\{|%\}|%%"),
            "import": re.compile(r'^[ \t]*#(?:include)\s*[<"][^>"]+[>"]', re.M),
            "ownership": re.compile(
                r"(?:@author|Author:|Created by:|Copyright)\s+(.*)", re.I
            ),
            # --- 🌌 PHASE 4: EXTENDED DIMENSIONS ---
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            "civil_war": None,
            "ssr_boundaries": None,
            "events": None,
            "dependency_injection": None,
            "macros": re.compile(
                r"^[ \t]*#(?:define|undef|if|elif|else|endif|pragma)\b", re.M
            ),
            "pointers": re.compile(
                r"->|&\w+|(?<=[=(,])[ \t]*\*(?:\s*const\s*)?[a-zA-Z_]\w*"
            ),
            "memory_alloc": re.compile(
                r"\b(malloc|calloc|realloc|free|YYMALLOC|YYFREE)\b"
            ),
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE ---
            "telemetry": re.compile(r"\b(?:syslog|openlog|log_info|YYDPRINTF)\b"),
            "print_hits": re.compile(r"\b(printf|fprintf|vprintf|puts|yyerror)\b"),
            "cast_hits": re.compile(
                r"\(\s*(?:int|char|short|long|float|double|void|unsigned|signed|[A-Z]\w*)\s*\*?\s*\)\s*[a-zA-Z_$]"
            ),
            "bailout_hits": re.compile(r"\b(abort|exit|YYABORT)\b"),
            "halt_hits": None,
            "bitwise_hits": re.compile(r"<<|>>|(?<!&)&(?!&)|(?<!\|)\|(?!\|)|\^|~"),
            "sync_locks": None,
            "freeze_hits": re.compile(r"\bconst\b"),
            "cleanup": re.compile(r"\b(free|YYFREE|fclose|destroy)\b\s*\("),
            "encapsulation": re.compile(r"^[ \t]*static\b", re.M),
            "listeners": None,
            "test_skip": None,
        },
    },
    "m4": {
        "_meta": {
            "target_version": "GNU M4 1.4+ / Autoconf 2.71+",
            "last_updated": "2026-03-11",
            "blueprint_version": "v5.1",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard macros, Autotest suites (.at), Autoconf logic (.ac), and template stubs (.in).
        "extensions": [".m4", ".at", ".ac", ".in"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: The undeniable structural anchors of the GNU build system.
        "exact_matches": ["configure.ac", "configure.in"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Automake configurations and standard Makefiles acting as massive gravity anchors for ambiguous .in templates.
        "discriminators": [
            ".m4",
            "Makefile.am",
            "Makefile.in",
            "aclocal.m4",
            "config.h.in",
        ],
        # EXECUTION SIGNATURES: M4 is a macro processor; no traditional shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 8 (Singular/Unique)
        # Rationale: M4 uniquely uses the `dnl` (Delete to NewLine) macro to act as its
        # line-level Ghost Mass.
        "lexical_family": "singular",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            "_line_anchor": re.compile(r"\bdnl\b"),
            "_inline_comment": re.compile(r"\bdnl\b"),
            "_block_start": None,
            "_block_end": None,
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # M4 branching logic and Autoconf shell-generation branches.
            "branch": re.compile(
                r"\b(?:ifelse|ifdef|AS_IF|AS_CASE|m4_if|m4_case|m4_cond|m4_ifval|m4_ifblank)\b"
            ),
            # 2. args (The Coupling Mass)
            # M4 positional arguments.
            "args": re.compile(r"\$[0-9]+|\$[@*#]"),
            # 3. linear (The Smooth Path)
            # Execution flow diversion and dependency signaling.
            "linear": re.compile(
                r"\b(?:divert|undivert|m4_divert|m4_undivert|m4_require|AC_REQUIRE)\b"
            ),
            # 4. func_start (The Satellite Spawner)
            # Defining a macro establishes an executable logic block in M4.
            "func_start": re.compile(
                r"^[ \t]*(m4_define|define|AC_DEFUN|AC_DEFUN_ONCE|AU_DEFUN|m4_defun)(?=\s*\()",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            "class_start": None,  # M4 is a macro processor, lacking objects.
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety (The Defenders)
            # Autoconf environment checks and M4 assertions.
            "safety": re.compile(
                r"\b(?:m4_assert|AS_VERSION_COMPARE|AC_CHECK_PROG|AC_CHECK_LIB|AC_CHECK_HEADER|AC_CHECK_FUNC|m4_warn)\b"
            ),
            # 7. safety_neg (The Fractures)
            # Dynamically altering the quote characters or comment strings breaks the parser context completely.
            "safety_neg": re.compile(
                r"\b(?:changequote|changecom|m4_changequote|m4_changecom|m4_ignore)\b"
            ),
            # 8. danger (The Heavy Load)
            # Executing raw shell commands during macro expansion (not generation).
            "danger": re.compile(r"\b(?:syscmd|esyscmd|m4_syscmd|m4_esyscmd)\b"),
            # 9. io (The Boundaries)
            # Reading system values, creating temp files, or emitting generated configurations.
            "io": re.compile(
                r"\b(?:sysval|mkstemp|maketemp|m4_mkstemp|m4_maketemp|AC_CONFIG_FILES|AC_OUTPUT)\b"
            ),
            # 10. api (The Event Horizon)
            # M4 macros are inherently public, but these explicitly export state into the generated Makefile/C headers.
            "api": re.compile(r"\b(?:AC_SUBST|AC_DEFINE|AC_PROVIDE|m4_provide)\b"),
            # 11. flux (The Boiling Plasma)
            # Stack-based macro overriding and list appending.
            "flux": re.compile(
                r"\b(?:pushdef|popdef|m4_pushdef|m4_popdef|m4_append|m4_append_uniq|m4_combine)\b"
            ),
            # 12. graveyard (The Necrosis)
            # Commented-out macro definitions.
            "graveyard": re.compile(
                r"^[ \t]*dnl[ \t]+(?:m4_define|define|AC_DEFUN|ifelse|AS_IF)\b", re.M
            ),
            # 13. doc (The Intent)
            # Documentation blocks or explicit copyright insertions into the output script.
            "doc": re.compile(
                r"^[ \t]*dnl[ \t]+@(?:param|return|brief)|AC_COPYRIGHT\b", re.M
            ),
            # 14. test (The Verification)
            # The GNU Autotest framework.
            "test": re.compile(r"\b(?:AT_SETUP|AT_CHECK|AT_CLEANUP|AT_INIT|AT_DATA)\b"),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Architecture & Complexity) ---
            # 15. concurrency
            "concurrency": None,
            # 16. ui_framework
            "ui_framework": None,
            # 17. closures
            "closures": None,
            # 18. globals (The Shared Void)
            # Environment variables mapped into the configure script.
            "globals": re.compile(r"\b(?:AC_ARG_VAR|AC_ENV_VAR|m4_divert_text)\b"),
            # 19. decorators
            "decorators": None,
            # 20. generics
            "generics": None,
            # 21. comprehensions (The High-Density Loops)
            # M4 map and foreach iterative constructs.
            "comprehensions": re.compile(
                r"\b(?:m4_foreach|m4_foreach_w|m4_map|m4_map_sep)\b"
            ),
            # 22. scientific (The Compute Core)
            # M4's native integer arithmetic evaluator.
            "scientific": re.compile(r"\b(?:eval|m4_eval)\b"),
            # 23. heat_triggers (The Thermal Radiation)
            # Advanced string metaprogramming and regex substitutions.
            "heat_triggers": re.compile(
                r"\b(?:translit|patsubst|regexp|m4_translit|m4_bpatsubst|m4_bregexp|m4_pattern_allow)\b"
            ),
            # 24. import (The Gravity Links)
            # File inclusions.
            "import": re.compile(
                r"^[ \t]*(?:include|sinclude|m4_include|m4_sinclude)\b", re.M
            ),
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"^[ \t]*dnl[ \t]+(?:Author|Maintainer|Copyright|License):|AC_COPYRIGHT",
                re.I | re.M,
            ),
            # --- 🌌 PHASE 4: EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            # 26. planned_debt
            "planned_debt": re.compile(r"\b(?:TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            # 27. fragile_debt
            "fragile_debt": re.compile(r"\b(?:HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure
            "spec_exposure": re.compile(
                r"\[(?:[ \t]*SPEC[ \t]*-[ \t]*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries
            "ssr_boundaries": None,
            # 32. events
            "events": None,
            # 33. dependency_injection
            # M4 dependency chaining to ensure macros execute in the correct order.
            "dependency_injection": re.compile(r"\b(?:AC_REQUIRE|m4_require)\b"),
            # 34. macros (The Preprocessor Hooks)
            # M4 is the macro engine, but this tracks configuring C-level preprocessor hooks.
            "macros": re.compile(r"\b(?:AC_DEFINE|AC_DEFINE_UNQUOTED|AH_TEMPLATE)\b"),
            # 35. pointers
            "pointers": None,
            # 36. memory_alloc
            "memory_alloc": None,
            # 37. inline_asm
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            # Logging configure progress securely to stdout and config.log.
            "telemetry": re.compile(
                r"\b(?:AC_MSG_CHECKING|AC_MSG_RESULT|AC_MSG_WARN|AC_MSG_NOTICE)\b"
            ),
            # 39. print_hits (The Amateur / Space Debris)
            # Raw M4 error printing.
            "print_hits": re.compile(r"\b(?:errprint|m4_errprint)\b"),
            # 40. cast_hits
            "cast_hits": None,
            # 41. bailout_hits (The Detonators)
            # Hard aborts.
            "bailout_hits": re.compile(
                r"\b(?:m4_fatal|AC_MSG_ERROR|AC_MSG_FAILURE|AS_EXIT)\b"
            ),
            # 42. halt_hits (Temporal Duct Tape)
            # Raw sleeps in generated scripts.
            "halt_hits": re.compile(r"\b(?:sleep)\b"),
            # 43. bitwise_hits
            "bitwise_hits": None,
            # 44. sync_locks
            "sync_locks": None,
            # 45. freeze_hits
            "freeze_hits": None,  # M4 macros are mutable by design.
            # 46. cleanup (The Janitor)
            # Macro unloading and Autotest tear-downs.
            "cleanup": re.compile(r"\b(?:m4_popdef|popdef|AT_CLEANUP)\b"),
            # 47. encapsulation (The Vault)
            # Forbidding specific patterns from reaching the output script.
            "encapsulation": re.compile(r"\b(?:m4_pattern_forbid)\b"),
            # 48. listeners
            "listeners": None,
            # 49. test_skip (Safety Theater)
            # Skipping tests in the Autotest framework.
            "test_skip": re.compile(r"\b(?:AT_SKIP_IF)\b"),
        },
    },
    "scheme": {
        "_meta": {
            "target_version": "R5RS / R6RS / Guile (GnuPG gpgscm)",
            "last_updated": "2026-03-11",
            "blueprint_version": "v6.2.2",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard Scheme, legacy PLT/Chez suffixes, and Racket sources.
        "extensions": [".scm", ".ss", ".rkt", ".sch", ".sld", ".sls", ".sps"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Scheme rarely uses extensionless configurations.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Guile build definitions, Racket manifests, and Lisp package formats.
        "discriminators": [".scm", ".rkt", "info.rkt", "guix.scm"],
        # EXECUTION SIGNATURES: Interpreters found on Line 1 for shell wrappers invoking Scheme/Guile/Racket.
        "shebangs": ["guile", "scheme", "csi", "racket", "racketsh"],
        # UPGRADED: Maps to Family 9 (Lisp_Semi) - *NEW FAMILY*
        # Rationale: Perfectly captures the Lisp ecosystem's reliance on ';' for line-level
        # comments and `#| |#` for nested block-level Ghost Mass.
        "lexical_family": "lisp_semi",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            # Scheme uses ';' for standard line-level literature.
            "_line_anchor": re.compile(r";"),
            "_inline_comment": re.compile(r";"),
            # Scheme block comments (SRFI 30) use #| and |#
            "_block_start": re.compile(r"#\|"),
            "_block_end": re.compile(r"\|#"),
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Lisp control flow branches. Uses custom S-expression boundaries.
            "branch": re.compile(
                r"(?<=[ \t(\[])(if|cond|case|and|or|when|unless)(?=[ \t)\]\n\r])"
            ),
            # 2. args (The Coupling Mass)
            # Captures the parameter list inside a standard function definition: (define (func arg1 arg2) ...)
            "args": re.compile(r"^[ \t]*\([ \t]*define\s+\([^ \t]+\s+([^)]*)\)", re.M),
            # 3. linear (The Smooth Path)
            # Structural boundaries defining scope and sequential execution.
            "linear": re.compile(
                r"(?<=[ \t(\[])(let|let\*|letrec|letrec\*|begin|do)(?=[ \t)\]\n\r])"
            ),
            # 4. func_start (The Satellite Spawner)
            # Anchors logic blocks. Captures the function name immediately following the parenthesis.
            "func_start": re.compile(
                r"^[ \t]*\([ \t]*define\s+\(\s*([a-zA-Z0-9_!?-]+)(?=[ \t)\]\n\r])", re.M
            ),
            # 5. class_start (The Entity Census)
            # Scheme lacks traditional objects; SRFI-9 Records serve as structural entities.
            "class_start": re.compile(
                r"^[ \t]*\([ \t]*define-record-type\s+([a-zA-Z0-9_!?-]+)(?=[ \t)\]\n\r])",
                re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety (The Defenders)
            # Continuations, exception guards, and dynamic-wind state protectors.
            "safety": re.compile(
                r"(?<=[ \t(\[])(guard|dynamic-wind|with-exception-handler|call-with-current-continuation|call/cc|assert|check)(?=[ \t)\]\n\r])"
            ),
            # 7. safety_neg (The Fractures)
            # Explicit, raw manipulation of cons cells or unrestricted environments.
            "safety_neg": re.compile(
                r"(?<=[ \t(\[])(set-car!|set-cdr!|interaction-environment)(?=[ \t)\]\n\r])"
            ),
            # 8. danger (The Heavy Load)
            # Dynamic code execution and emergency system exits.
            "danger": re.compile(
                r"(?<=[ \t(\[])(eval|exit|emergency-exit|quit)(?=[ \t)\]\n\r])"
            ),
            # 9. io (The Boundaries)
            # File operations and output ports.
            "io": re.compile(
                r"(?<=[ \t(\[])(open-input-file|open-output-file|read|read-char|write|display|newline|call-with-input-file|call-with-output-file|load|format)(?=[ \t)\]\n\r])"
            ),
            # 10. api (The Event Horizon)
            # Module exports defining the public surface.
            "api": re.compile(
                r"^[ \t]*\([ \t]*(?:export|define-public)(?=[ \t)\]\n\r])", re.M
            ),
            # 11. flux (The Boiling Plasma)
            # Mutation of state. In Scheme, all mutating functions end with a bang (!).
            "flux": re.compile(
                r"(?<=[ \t(\[])(set!|vector-set!|string-set!|hash-table-set!|bytevector-u8-set!)(?=[ \t)\]\n\r])"
            ),
            # 12. graveyard (The Necrosis)
            # Commented out S-expressions.
            "graveyard": re.compile(
                r"^[ \t]*;+[ \t]*\([ \t]*(?:define|let|if|cond|lambda)(?=[ \t)\]\n\r])",
                re.M,
            ),
            # 13. doc (The Intent)
            # Scheme documentation standards (triple semicolons or texinfo).
            "doc": re.compile(
                r"^[ \t]*;;;|^[ \t]*;[ \t]*@(?:param|return|author)", re.M
            ),
            # 14. test (The Verification)
            # SRFI-64 and Guile testing frameworks (essential for mapping gpgscm tests).
            "test": re.compile(
                r"(?<=\()(test-begin|test-end|test-assert|test-eqv|test-equal|test-eq|check-equal\?|check-true|test)(?=[ \t)\]\n\r])"
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency (The Temporal Static)
            # SRFI-18 Multithreading primitives.
            "concurrency": re.compile(
                r"(?<=[ \t(\[])(make-thread|thread-start!|thread-yield!|mutex-lock!|mutex-unlock!|condition-variable-signal!)(?=[ \t)\]\n\r])"
            ),
            # 16. ui_framework
            "ui_framework": None,
            # 17. closures (The Functional Depth)
            # Anonymous function depth.
            "closures": re.compile(r"(?<=[ \t(\[])lambda(?=[ \t)\]\n\r])"),
            # 18. globals (The Shared Void)
            # Top-level state bindings (defines that are NOT functions).
            "globals": re.compile(
                r"^[ \t]*\([ \t]*define\s+[a-zA-Z0-9_!?-]+\s+[^(\s]", re.M
            ),
            # 19. decorators
            "decorators": None,
            # 20. generics
            "generics": None,
            # 21. comprehensions (The High-Density Loops)
            # Functional list operations (SRFI-1).
            "comprehensions": re.compile(
                r"(?<=[ \t(\[])(map|for-each|filter|fold|reduce|fold-right|fold-left)(?=[ \t)\]\n\r])"
            ),
            # 22. scientific (The Compute Core)
            # Scheme's native mathematical tower.
            "scientific": re.compile(
                r"(?<=[ \t(\[])(sin|cos|tan|asin|acos|atan|exp|log|sqrt|expt|abs|gcd|lcm|numerator|denominator|floor|ceiling|truncate|round|exact->inexact)(?=[ \t)\]\n\r])"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Metaprogramming and syntactic abstractions.
            "heat_triggers": re.compile(
                r"(?<=[ \t(\[])(define-macro|define-syntax|syntax-rules|syntax-case|let-syntax|letrec-syntax)(?=[ \t)\]\n\r])"
            ),
            # 24. import (The Gravity Links)
            # Scheme module resolution dependencies.
            "import": re.compile(
                r"^[ \t]*\([ \t]*(?:import|use-modules|require)(?=[ \t)\]\n\r])", re.M
            ),
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"^[ \t]*;+\s*(?:Author|Created by|Maintainer|Copyright):\s+(.*)",
                re.I | re.M,
            ),
            # --- 🌌 PHASE 4: EXTENDED DIMENSIONS (Specialized Sub-Equations) ---
            # 26. planned_debt
            "planned_debt": re.compile(r"\b(TODO|WIP|STUB|IMPLEMENT)\b", re.I),
            # 27. fragile_debt
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            # 29. spec_exposure
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war
            # Lisp/Scheme relies entirely on uniform space alignment. Tabs are highly destructive here.
            "civil_war": None,
            # 31. ssr_boundaries
            "ssr_boundaries": None,
            # 32. events (The Pub/Sub Network)
            # Hook paradigms common in Guile/Emacs environments.
            "events": re.compile(
                r"(?<=[ \t(\[])(hook|add-hook!|run-hooks)(?=[ \t)\]\n\r])"
            ),
            # 33. dependency_injection
            "dependency_injection": None,
            # 34. macros (The Preprocessor Hooks)
            "macros": re.compile(
                r"(?<=[ \t(\[])(define-syntax|define-macro|syntax-rules|syntax-case)(?=[ \t)\]\n\r])"
            ),
            # 35. pointers
            "pointers": None,
            # 36. memory_alloc
            # Explicit heap instantiations.
            "memory_alloc": re.compile(
                r"(?<=[ \t(\[])(make-vector|make-string|make-bytevector|make-hash-table|cons|list)(?=[ \t)\]\n\r])"
            ),
            # 37. inline_asm
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"(?<=[ \t(\[])(log-info|log-error|log-warn|log-debug|syslog)(?=[ \t)\]\n\r])"
            ),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(
                r"(?<=[ \t(\[])(display|write|newline|format\s+#t)(?=[ \t)\]\n\r])"
            ),
            # 40. cast_hits (The "Trust Me" Tax)
            # Type coercions crossing memory boundaries.
            "cast_hits": re.compile(
                r"(?<=[ \t(\[])(number->string|string->number|symbol->string|string->symbol|list->vector|vector->list|char->integer|integer->char)(?=[ \t)\]\n\r])"
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(
                r"(?<=[ \t(\[])(error|abort|exit|emergency-exit)(?=[ \t)\]\n\r])"
            ),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(
                r"(?<=[ \t(\[])(sleep|usleep|thread-sleep!)(?=[ \t)\]\n\r])"
            ),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(
                r"(?<=[ \t(\[])(bitwise-and|bitwise-ior|bitwise-xor|bitwise-not|arithmetic-shift|ash)(?=[ \t)\]\n\r])"
            ),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"(?<=[ \t(\[])(mutex-lock!|make-mutex)(?=[ \t)\]\n\r])"
            ),
            # 45. freeze_hits (The Data Cryogenics)
            # Immutable strings and explicit quotations (meaning the list cannot be mutated safely).
            "freeze_hits": re.compile(
                r"(?<=[ \t(\[])(quote|string->immutable-string)(?=[ \t)\]\n\r])|\'(?=\()"
            ),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r"(?<=[ \t(\[])(close-input-port|close-output-port|close-port)(?=[ \t)\]\n\r])"
            ),
            # 47. encapsulation (The Vault)
            # Module-internal definitions.
            "encapsulation": re.compile(
                r"^[ \t]*\([ \t]*define-private(?=[ \t)\]\n\r])", re.M
            ),
            # 48. listeners (The Sinks)
            "listeners": re.compile(r"(?<=[ \t(\[])(add-hook!)(?=[ \t)\]\n\r])"),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(
                r"(?<=[ \t(\[])(test-skip|test-expect-fail)(?=[ \t)\]\n\r])"
            ),
        },
    },
    "mlir": {
        "_meta": {
            "target_version": "LLVM MLIR",
            "last_updated": "2026-03-11",
            "blueprint_version": "1.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: The standard dialect and transformation format for MLIR.
        "extensions": [".mlir"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: IR files strictly rely on their extensions.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: LLVM TableGen definitions, core LLVM IR, and CMake configs anchoring the compiler toolchain.
        "discriminators": [".mlir", ".td", ".ll", "CMakeLists.txt"],
        # EXECUTION SIGNATURES: MLIR is ingested by tools like mlir-opt; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 1 (Standard C-Style)
        # Rationale: MLIR intentionally adopts standard LLVM assembly syntax conventions,
        # using '//' exclusively for line comments to maintain C++ ecosystem familiarity.
        "lexical_family": "std_c",
        "rules": {
            "_line_anchor": re.compile(r"//"),
            "_inline_comment": re.compile(r"//"),
            "_block_start": None,
            "_block_end": None,
        },
    },
    "proto": {
        "_meta": {
            "target_version": "Protocol Buffers 3 (proto3)",
            "last_updated": "2026-03-11",
            "blueprint_version": "1.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard Protocol Buffer schema definition files.
        "extensions": [".proto"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Schemas strictly rely on their extensions.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Buf configuration files, Bazel build files, and generated code markers acting as anchors.
        "discriminators": [
            ".proto",
            "buf.yaml",
            "buf.gen.yaml",
            "WORKSPACE",
            "BUILD.bazel",
            "BUILD",
        ],
        # EXECUTION SIGNATURES: Protobuf is a declarative schema language; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 1 (Standard C-Style)
        # Rationale: Protobuf schemas strictly use standard '//' and '/* */' comments.
        "lexical_family": "std_c",
        "rules": {
            "_line_anchor": re.compile(r"//"),
            "_inline_comment": re.compile(r"//"),
            "_block_start": re.compile(r"/\*"),
            "_block_end": re.compile(r"\*/"),
        },
    },
    "hlo": {
        "_meta": {
            "target_version": "XLA High-Level Optimizer IR",
            "last_updated": "2026-03-11",
            "blueprint_version": "1.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard XLA HLO intermediate representation text formats.
        "extensions": [".hlo"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: IR text files strictly rely on their extensions.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: JAX, TensorFlow, and MLIR toolchain markers acting as gravity anchors for ML compilers.
        "discriminators": [".hlo", ".mlir", ".pbtxt", ".py", "BUILD.bazel", "BUILD"],
        # EXECUTION SIGNATURES: HLO is compiler intermediate representation; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 1 (Standard C-Style)
        # Rationale: HLO text format exclusively utilizes '//' for line-level comments, maintaining C++ ecosystem alignment.
        "lexical_family": "std_c",
        "rules": {
            "_line_anchor": re.compile(r"//"),
            "_inline_comment": re.compile(r"//"),
            "_block_start": None,
            "_block_end": None,
        },
    },
    "td": {
        "_meta": {
            "target_version": "LLVM TableGen",
            "last_updated": "2026-03-11",
            "blueprint_version": "1.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard LLVM TableGen record definition files.
        "extensions": [".td"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: TableGen relies entirely on its extensions.
        "exact_matches": [],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: LLVM/Clang core C++ source files, generated includes (.inc), and CMake configs anchoring the compiler backend.
        "discriminators": [
            ".td",
            ".cpp",
            ".h",
            ".inc",
            "CMakeLists.txt",
            "LLVMBuild.txt",
        ],
        # EXECUTION SIGNATURES: TableGen is processed by the llvm-tblgen backend during build time; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 1 (Standard C-Style)
        # Rationale: TableGen was built to integrate seamlessly into LLVM's C++ codebase, natively supporting '//' and '/* */' comments.
        "lexical_family": "std_c",
        "rules": {
            "_line_anchor": re.compile(r"//"),
            "_inline_comment": re.compile(r"//"),
            "_block_start": re.compile(r"/\*"),
            "_block_end": re.compile(r"\*/"),
        },
    },
    "plaintext": {
        "_meta": {
            "target_version": "Universal Plaintext",
            "last_updated": "2026-03-11",
            "blueprint_version": "1.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard text, log outputs, raw data dumps, and information files.
        # THE FIX: Added standard UNIX Man Page extensions (.1 through .9).
        "extensions": [
            ".txt", ".text", ".log", ".out", ".err", ".nfo", ".golden", ".properties",
            ".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9"
        ],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: The universally recognized, extensionless plaintext anchors of open-source repositories.
        "exact_matches": [
            "AUTHORS",
            "NOTICE",
            "COPYING",
            "INSTALL",
            "acknowledgements",
        ],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION: Plaintext is universal, but often orbits standard documentation.
        "discriminators": [".txt", ".md", "README", "LICENSE"],
        # EXECUTION SIGNATURES: Plaintext is uncompiled, unexecuted raw string data; no shebangs exist.
        "shebangs": [],
        # UPGRADED: Maps to Family 3 (Pure Hash) / Singularity Bypass
        # Rationale: As noted, Prism uses the 'Singularity Bypass' here. Because plaintext has
        # no structural syntax or comments to strip, it bypasses standard lexical parsing and
        # is treated entirely as raw literal mass.
        "lexical_family": "pure_hash",
        "rules": {
            "_line_anchor": None,
            "_inline_comment": None,
            "_block_start": None,
            "_block_end": None,
        },
    },
    "tcl": {
        "_meta": {
            "target_version": "Tcl 8.6 / SQLite Test Suite",
            "last_updated": "2026-03-11",
            "blueprint_version": "v6.3.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard scripts and Tcl modules.
        "extensions": [".tcl", ".itcl", ".tbc", ".tm"], # Removed .test
        # ABSOLUTE IDENTITY & EXACT FILENAMES:
        "exact_matches": ["tclIndex", "pkgIndex.tcl"],
        # ECOSYSTEM GRAVITY: Added .test here so it only anchors, but doesn't claim globally.
        "discriminators": [".tcl", "tclIndex", ".test", "Makefile"],
        # EXECUTION SIGNATURES: Standard interpreters found on Line 1.
        "shebangs": ["tclsh", "wish", "bin/expect", "jimsh"],
        # UPGRADED: Maps to Family 3 (Pure Hash)
        # Rationale: Tcl natively uses '#' exclusively for line-level comments. It does not
        # have native block comments (developers sometimes hack `if 0 { ... }`, but `#` is the standard).
        "lexical_family": "pure_hash",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            "_line_anchor": re.compile(r"#"),
            "_inline_comment": re.compile(r"#"),
            "_block_start": None,
            "_block_end": None,
            # --- 🪐 PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            # Tcl control flow keywords.
            "branch": re.compile(
                r"\b(?:if|elseif|else|switch|while|for|foreach|catch|try|trap|finally)\b"
            ),
            # 2. args (The Coupling Mass)
            # Safely captures the parameter list `{...}` immediately following a proc name.
            "args": re.compile(
                r"^[ \t]*proc[ \t]+[a-zA-Z0-9_:]+[ \t]+\{([^}]*)\}", re.M
            ),
            # 3. linear (The Smooth Path)
            # Structural boundaries. EXCLUDES: global/upvar (globals/heat).
            "linear": re.compile(
                r"\b(?:proc|return|break|continue|namespace|variable|yield)\b"
            ),
            # 4. func_start (The Satellite Spawner)
            # MUST HAVE EXACTLY ONE CAPTURE GROUP.
            # Captures standard procs and namespaced procs (e.g., `proc ::my::func`).
            "func_start": re.compile(
                r"^[ \t]*proc[ \t]+([a-zA-Z0-9_:]+)(?=[ \t]*\{|[ \t\n]|$)", re.M
            ),
            # 5. class_start (The Entity Census)
            # Captures TclOO, Snit, and Itcl class definitions.
            "class_start": re.compile(
                r"^[ \t]*(?:oo::class[ \t]+create|snit::type|itcl::class)[ \t]+([a-zA-Z0-9_:]+)(?=[ \t]*\{|[ \t\n]|$)",
                re.M,
            ),
            # --- ⚠️ PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety (The Defenders)
            # Safe evaluation and error catching.
            "safety": re.compile(
                r"\b(?:catch|try|trap|finally|info[ \t]+exists|assert)\b"
            ),
            # 7. safety_neg (The Fractures)
            # Unrestricted evaluation and context manipulation.
            "safety_neg": re.compile(r"\b(?:eval|uplevel|upvar)\b"),
            # 8. danger (The Heavy Load)
            # OS command execution and process termination.
            "danger": re.compile(r"\b(?:exec|exit)\b|file[ \t]+delete[ \t]+-force"),
            # 9. io (The Boundaries)
            # File system, sockets, and configuration. (Excludes puts which is mapped to print_hits).
            "io": re.compile(
                r"\b(?:open|close|read|gets|socket|fconfigure|file|source|vfs::)\b"
            ),
            # 10. api (The Event Horizon)
            # Exposing packages or namespace exports.
            "api": re.compile(
                r"^[ \t]*(?:package[ \t]+provide|namespace[ \t]+export)\b", re.M
            ),
            # 11. flux (The Boiling Plasma)
            # Variable state mutations.
            "flux": re.compile(
                r"\b(?:set|lappend|dict[ \t]+set|array[ \t]+set|incr|append)\b[ \t]+[a-zA-Z0-9_:]+"
            ),
            # 12. graveyard (The Necrosis)
            # Commented out structural code.
            "graveyard": re.compile(
                r"^[ \t]*#[ \t]*(?:proc|set|if|while|foreach|return)\b", re.M
            ),
            # 13. doc (The Intent)
            # Tcl doc blocks.
            "doc": re.compile(r"^[ \t]*#[ \t]*@(?:param|return|brief|author)", re.M),
            # 14. test (The Verification)
            # *THE SQLITE MEGA-SENSOR*: Accurately maps the SQLite custom test harnesses alongside standard tcltest.
            "test": re.compile(
                r"\b(?:do_test|do_execsql_test|do_catchsql_test|do_eqp_test|do_ioerr_test|do_faultsim_test|test\s+[a-zA-Z0-9_-]+|tcltest::|finish_test)\b"
            ),
            # --- 🔬 PHASE 3: SPECIALIZED SENSORS (Context Awareness) ---
            # 15. concurrency (The Temporal Static)
            # Event loops, delays, and threads.
            "concurrency": re.compile(r"\b(?:vwait|after|thread::|coroutine|yield)\b"),
            # 16. ui_framework (The View Layer)
            # Tkinter/Tk graphical elements.
            "ui_framework": re.compile(
                r"\b(?:button|pack|grid|place|canvas|frame|label|ttk::)\b"
            ),
            # 17. closures (The Functional Depth)
            # Tcl 8.6 anonymous functions.
            "closures": re.compile(r"\bapply[ \t]+\{"),
            # 18. globals (The Shared Void)
            # Tcl relies heavily on global imports and environment arrays.
            "globals": re.compile(r"\b(?:global|::env)\b|upvar[ \t]+#0"),
            # 19. decorators
            "decorators": None,
            # 20. generics
            "generics": None,
            # 21. comprehensions
            # Tcl 8.6 list map.
            "comprehensions": re.compile(r"\blmap\b"),
            # 22. scientific (The Compute Core)
            # Explicit math invocations via expr.
            "scientific": re.compile(
                r"\b(?:expr|math::)\b|\b(?:sin|cos|tan|sqrt|exp|log|pow)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Massive cognitive heat: Intercepting variables, tracking execution, and runtime aliasing.
            "heat_triggers": re.compile(
                r"\b(?:trace[ \t]+add|rename|interp[ \t]+create|interp[ \t]+alias)\b"
            ),
            # 24. import (The Gravity Links)
            # Package and module loading.
            "import": re.compile(
                r"^[ \t]*(?:package[ \t]+require|source|load)\b", re.M
            ),
            # 25. ownership (The Authorship)
            "ownership": re.compile(
                r"^[ \t]*#[ \t]*(?:Author|Created by|Maintainer|Copyright):\s+(.*)",
                re.I | re.M,
            ),
            # --- 🌌 PHASE 4: EXTENDED DIMENSIONS ---
            "planned_debt": re.compile(r"\b(?:TODO|WIP|STUB|IMPLEMENT|@todo)\b", re.I),
            "fragile_debt": re.compile(r"\b(?:HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),

            "spec_exposure": re.compile(
                r"\[(?:[ \t]*SPEC[ \t]*-[ \t]*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            # Tcl standardizes on spaces. Tabs indicate formatter friction.
            "civil_war": None,
            "ssr_boundaries": None,
            # 32. events (The Pub/Sub Network)
            # Tcl event bindings and file event handlers.
            "events": re.compile(r"\b(?:bind|fileevent|vwait|trace[ \t]+add)\b"),
            "dependency_injection": None,
            "macros": None,
            "pointers": None,
            "memory_alloc": None,
            "inline_asm": None,
            # --- ⚖️ PHASE 5: THERMODYNAMIC BALANCE ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(r"\b(?:log::log|logger::|syslog)\b"),
            # 39. print_hits (The Amateur / Space Debris)
            "print_hits": re.compile(r"\bputs\b"),
            # 40. cast_hits (The Trust Me Tax)
            "cast_hits": re.compile(r"\bexpr[ \t]+(?:int|double|wide)\("),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(?:error|exit)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\bafter[ \t]+[0-9]+\b"),
            # 43. bitwise_hits (The Sub-Atomic Math)
            "bitwise_hits": re.compile(r"(?<!&)&(?!&)|(?<!\|)\|(?!\|)|\^|~|<<|>>"),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(?:thread::mutex|thread::rwmutex|thread::cond)\b"
            ),
            # 45. freeze_hits (The Data Cryogenics)
            # Tcl lacks `const`, but setting a trace to prevent writes is the Tcl idiom for freezing.
            "freeze_hits": re.compile(
                r"\btrace[ \t]+add[ \t]+variable[ \t]+[a-zA-Z0-9_:]+[ \t]+write\b"
            ),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(
                r'\b(?:close|unset)\b|rename[ \t]+[a-zA-Z0-9_:]+[ \t]+""'
            ),
            # 47. encapsulation (The Vault)
            # Internal namespaces and private `_` prefixed procs.
            "encapsulation": re.compile(
                r"\bnamespace[ \t]+eval\b|^[ \t]*proc[ \t]+_[a-zA-Z0-9_:]+", re.M
            ),
            # 48. listeners (The Sinks)
            "listeners": re.compile(r"\b(?:bind|fileevent)\b"),
            # 49. test_skip (Safety Theater)
            # Using TclTest constraints to silently skip tests on certain OS environments.
            "test_skip": re.compile(
                r"-constraints[ \t]+[a-zA-Z0-9_]+\b|\btestConstraint\b"
            ),
        },
    },
    "groovy": {
        "_meta": {
            "target_version": "Groovy 4.0 / Gradle 8+",
            "last_updated": "2026-03-12",
            "blueprint_version": "v5.0",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA
        "extensions": [".groovy", ".gradle", ".gvy", ".gy", ".gsh"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES
        "exact_matches": ["Jenkinsfile"],
        # ECOSYSTEM GRAVITY & DISAMBIGUATION
        "discriminators": [
            "build.gradle",
            "settings.gradle",
            "gradle.properties",
            "pom.xml",
            ".java",
        ],
        # EXECUTION SIGNATURES
        "shebangs": ["groovy"],
        # LEXICAL FAMILY
        "lexical_family": "std_c",
        "rules": {
            # --- 2.3.C OPTICAL SPLIT CONTROLS ---
            "_line_anchor": re.compile(r"//"),
            "_inline_comment": re.compile(r"//"),
            "_block_start": re.compile(r"/\*"),
            "_block_end": re.compile(r"\*/"),
            # --- PHASE 1: PHYSICS ENGINE (Geometry & Structure) ---
            # 1. branch (The Forks in the Road)
            "branch": re.compile(
                r"\b(if|else|switch|case|default|for|while|in|try|catch|finally)\b|\?|:"
            ),
            # 2. args (The Coupling Mass)
            # Captures standard method arguments and Groovy closures (x, y ->)
            # CRITICAL FIX: Anchored the parenthesis capture to method signatures so it 
            # doesn't hallucinate every standard method call or if-statement in the file.
            "args": re.compile(
                r"^[ \t]*(?:(?:public|private|protected|static|final|def|abstract)[ \t]+){0,5}(?:[A-Z][a-zA-Z0-9_<>\[\]?]*[ \t]+){0,2}[A-Za-z_$][\w_$]*\s*\([^)]*\)|(?:\([^)]*\)|[a-zA-Z_$][\w_$]*)\s*->",
                re.M,
            ),
            # 3. linear (The Smooth Path)
            "linear": re.compile(
                r"\b(def|class|interface|trait|enum|record|import|package|extends|implements|return|yield)\b"
            ),
            # 4. func_start (The Satellite Spawner)
            # HIGHLY TUNED: Uses Negative Lookahead to explicitly ignore Gradle DSL keywords (implementation, api, task)
            # Uses Positive Lookahead (?=[ \t]*\() to stop exactly at the function name without consuming punctuation.
            "func_start": re.compile(
                r"^[ \t]*(?:(?:public|private|protected|static|final|def)[ \t]+){0,5}(?:[A-Z][a-zA-Z0-9_<>\[\]?]*[ \t]+){0,2}(?!(?:if|for|while|switch|catch|new|return|class|interface|enum|trait|implementation|testImplementation|api|compileOnly|runtimeOnly|classpath|dependency|from|file|mavenCentral|plugins|dependencies|repositories|task|project|allprojects|subprojects|ext)\b)([A-Za-z_$][\w_$]*)(?=[ \t]*\()",
                re.M,
            ),
            # 5. class_start (The Entity Census)
            "class_start": re.compile(
                r"^[ \t]*(?:(?:public|private|protected|static|final|abstract)[ \t]+){0,5}(?:class|interface|trait|enum|record)\s+[A-Za-z_$][\w_$]*",
                re.M,
            ),
            # --- PHASE 2: RISK ENGINE (Structural Integrity) ---
            # 6. safety (The Defenders)
            "safety": re.compile(
                r"\b(try|catch|finally|assert|instanceof|Optional)\b|@(?:Valid|Validated|NotNull|NonNull|Immutable)"
            ),
            # 7. safety_neg (The Fractures)
            "safety_neg": re.compile(
                r"\b(null)\b|return\s+null|catch\s*\(\s*(?:Exception|Throwable)\b|@SuppressWarnings|@SneakyThrows|\.get\(\)"
            ),
            # 8. danger (The Heavy Load)
            "danger": re.compile(
                r"\b(System\.exit|Runtime\.getRuntime\(\)\.exec|execute)\b"
            ),
            # 9. io (The Boundaries)
            "io": re.compile(
                r"\b(File|Files|Paths|FileReader|FileWriter|file|copy|sync|uri|url|Socket|Connection|ResultSet)\b"
            ),
            # 10. api (The Event Horizon)
            # Groovy classes/methods are implicitly public by default, making the whole file highly exposed.
            "api": re.compile(
                r"\b(public)\b|@(RestController|Controller|Service|Component|Bean|RequestMapping|GetMapping|PostMapping|PutMapping|DeleteMapping|PatchMapping)\b"
            ),
            # 11. flux (The Boiling Plasma)
            "flux": re.compile(r"^[ \t]*\w+(?:\.\w+)*[ \t]*=|@(?:Setter|Data)\b", re.M),
            # 12. graveyard (The Necrosis)
            # Tuned to catch dead Gradle definitions and Groovy logic.
            "graveyard": re.compile(
                r"//[ \t]*(?:def|class|void|if|for|while|import|implementation|compile|api|testImplementation)\b"
            ),
            # 13. doc (The Intent)
            "doc": re.compile(r"/\*\*|@param|@return|@throws|@deprecated|@see"),
            # 14. test (The Verification)
            # Integrates Spock Framework keywords (given:, when:, then:, expect:) alongside JUnit.
            "test": re.compile(
                r"@(?:Test|Before|After|BeforeEach|AfterEach|Mock)|assert\w*\s*\(|^\s*(?:given|when|then|expect|setup|cleanup|where):",
                re.M,
            ),
            # --- PHASE 3: SPECIALIZED SENSORS (Architecture & Domain) ---
            # 15. concurrency (The Temporal Static)
            "concurrency": re.compile(
                r"\b(synchronized|Thread|Runnable|Future|ExecutorService|Promise|Atomic\w+|task)\b|@(?:Async|Scheduled)"
            ),
            # 16. ui_framework (The View Layer)
            "ui_framework": re.compile(
                r"\b(SwingBuilder|JFrame|JPanel|ModelAndView|ModelMap|Model|UIComponent)\b"
            ),
            # 17. closures (The Functional Depth)
            "closures": re.compile(r"->|\{\s*(?:it|[\w\s,]+)\s*->"),
            # 18. globals (The Shared Void)
            "globals": re.compile(
                r"\b(System\.getProperty|System\.getenv|project\.ext)\b|@Value"
            ),
            # 19. decorators (The Metadata Hooks)
            "decorators": re.compile(r"^[ \t]*@[\w.]+(?:\([^)]*\))?", re.M),
            # 20. generics (The Type Abstractions)
            "generics": re.compile(r"<\s*[A-Z?][^>]*>"),
            # 21. comprehensions (The High-Density Loops)
            "comprehensions": re.compile(
                r"\.(?:collect|find|findAll|grep|inject|each|eachWithIndex|map|filter|reduce)\("
            ),
            # 22. scientific (The Compute Core)
            "scientific": re.compile(
                r"\b(Math\.|BigDecimal|BigInteger|Random|SecureRandom)\b"
            ),
            # 23. heat_triggers (The Thermal Radiation)
            # Groovy's highly dynamic Meta-Object Protocol (MOP).
            "heat_triggers": re.compile(
                r"\b(invokeMethod|getProperty|setProperty|methodMissing|propertyMissing|ExpandoMetaClass|metaClass)\b"
            ),
            # 24. import (The Gravity Links)
            "import": re.compile(r"^[ \t]*import\s+(?:static[ \t]+)?[\w.]+;?", re.M),
            # 25. ownership (The Authorship)
            "ownership": re.compile(r"@author\s+(.*)", re.I),
            # --- PHASE 4: EXTRACTED SUB-EQUATIONS (Specialized Systems) ---
            # 26. planned_debt (The Promise)
            "planned_debt": re.compile(
                r"\b(TODO|WIP|STUB|IMPLEMENT|PENDING|@todo)\b", re.I
            ),
            # 27. fragile_debt (The Fracture)
            "fragile_debt": re.compile(r"\b(HACK|FIXME|XXX|KLUDGE|UGLY|WTF)\b", re.I),
 
            # 29. spec_exposure (The Map vs. Territory)
            "spec_exposure": re.compile(
                r"\[(?:\s*SPEC\s*-\s*\d+|spec|audit)[^\]]*\]", re.I
            ),
            # 30. civil_war (The Indentation Tracker)
            "civil_war": None,
            # 31. ssr_boundaries (The View Horizon)
            "ssr_boundaries": re.compile(
                r"\b(MarkupBuilder|StreamingMarkupBuilder|TemplateEngine|HttpServletRequest|HttpServletResponse|@ResponseBody)\b"
            ),
            # 32. events (The Pub/Sub Network)
            "events": re.compile(
                r"\b(ApplicationEvent|ApplicationListener|@EventListener|publishEvent)\b"
            ),
            # 33. dependency_injection (The Inversion of Control)
            # Heavily captures Gradle plugin and dependency architecture.
            "dependency_injection": re.compile(
                r"\b(@Autowired|@Inject|@Component|@Service|@Repository|@Bean|@Configuration|apply\s+plugin|plugins\s*\{|dependencies\s*\{)\b"
            ),
            # 34. macros
            "macros": None,
            # 35. pointers (The Memory Map)
            "pointers": None,
            # 36. memory_alloc (The Yin to cleanup)
            "memory_alloc": None,
            # 37. inline_asm
            "inline_asm": None,
            # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
            # 38. telemetry (The Professional)
            "telemetry": re.compile(
                r"\b(log|logger|LOGGER|LoggerFactory)\.(?:info|error|warn|warning|debug|trace)\b|@Slf4j|@Log4j2|@Log"
            ),
            # 39. print_hits (The Amateur)
            "print_hits": re.compile(
                r"\b(println|print|printf|System\.out\.print|System\.err\.print|\.printStackTrace\(\))\b"
            ),
            # 40. cast_hits (The Trust Me Tax)
            "cast_hits": re.compile(
                r"\bas\s+[A-Z]\w*|\(\s*(?:int|long|short|byte|char|float|double|boolean|[A-Z][A-Za-z0-9_]*)\s*\)\s*[a-zA-Z_$]"
            ),
            # 41. bailout_hits (The Detonators)
            "bailout_hits": re.compile(r"\b(throw|System\.exit|GradleException)\b"),
            # 42. halt_hits (Temporal Duct Tape)
            "halt_hits": re.compile(r"\b(Thread\.sleep|sleep)\b"),
            # 43. bitwise_hits (The Sub-Atomic Math)
            # EXCLUDES `<<` and `>>` because Groovy heavily overloads `<<` for list/stream appending.
            "bitwise_hits": re.compile(r"\^|~"),
            # 44. sync_locks (The Barricades)
            "sync_locks": re.compile(
                r"\b(synchronized|ReentrantLock|ReadWriteLock|Semaphore|Lock|Mutex)\b"
            ),
            # 45. freeze_hits (The Data Cryogenics)
            "freeze_hits": re.compile(r"\b(final|@Immutable)\b"),
            # 46. cleanup (The Janitor)
            "cleanup": re.compile(r"\b(close|dispose|shutdown)\b\s*\("),
            # 47. encapsulation (The Vault)
            "encapsulation": re.compile(r"\b(private|protected)\b"),
            # 48. listeners (The Sinks)
            "listeners": re.compile(r"\b(addListener|on[A-Z]\w*|subscribe)\b"),
            # 49. test_skip (Safety Theater)
            "test_skip": re.compile(
                r"@(?:Ignore|Disabled|PendingFeature)\b|mock\s*\(|spy\s*\("
            ),
        },
    },
    "json": {
        "_meta": {
            "target_version": "JSON & ARB Localization",
            "status": "production",
        },
        # COMPREHENSIVE SURFACE AREA: Standard JSON and Flutter ARB files.
        "extensions": [".json", ".arb"],
        # ABSOLUTE IDENTITY & EXACT FILENAMES: Tooling configurations mapped as JSON.
        "exact_matches": [".prettierrc", ".eslintrc", ".babelrc", ".stylelintrc"],
        "discriminators": [".json", ".arb"],
        "shebangs": [],
        # Maps to Family 3 (Pure Hash) to trigger the Singularity Bypass for inert data.
        "lexical_family": "pure_hash",
        "rules": {
            "_line_anchor": None,
            "_inline_comment": None,
            "_block_start": None,
            "_block_end": None,
        },
    },
    "glsl": {
        "_meta": {"target_version": "OpenGL Shading Language", "status": "production"},
        "extensions": [".glsl", ".vert", ".frag", ".geom", ".comp"],
        "exact_matches": [],
        "discriminators": [".glsl", ".vert", ".frag"],
        "shebangs": [],
        "lexical_family": "std_c",
        "rules": {
            "_line_anchor": re.compile(r"//"),
            "_inline_comment": re.compile(r"//"),
            "_block_start": re.compile(r"/\*"),
            "_block_end": re.compile(r"\*/"),
        }
    },
    "nix": {
        "_meta": {"target_version": "Nix Expression Language", "status": "production"},
        "extensions": [".nix"],
        "exact_matches": [],
        "discriminators": ["flake.nix", "default.nix", "shell.nix"],
        "shebangs": [],
        "lexical_family": "pure_hash",
        "rules": {
            "_line_anchor": re.compile(r"#"),
            "_inline_comment": re.compile(r"#"),
            "_block_start": None,
            "_block_end": None,
        }
    },
    "blp": {
        "_meta": {"target_version": "Blueprint UI Markup", "status": "production"},
        "extensions": [".blp"],
        "exact_matches": [],
        "discriminators": [".blp", ".ui"],
        "shebangs": [],
        "lexical_family": "std_c",
        "rules": {
            "_line_anchor": re.compile(r"//"),
            "_inline_comment": re.compile(r"//"),
            "_block_start": re.compile(r"/\*"),
            "_block_end": re.compile(r"\*/"),
        }
    },
    "batch": {
        "_meta": {"target_version": "Windows CMD/Batch", "status": "production"},
        "extensions": [".bat", ".cmd"],
        "exact_matches": [],
        "discriminators": [],
        "shebangs": [],
        "lexical_family": "pure_hash",
        "rules": {
            # Uses REM or :: for comments. No active logic rules needed (Inert Matter Bypass).
            "_line_anchor": re.compile(r"^[ \t]*(?:REM|::)", re.I | re.M),
            "_inline_comment": None,
            "_block_start": None,
            "_block_end": None,
        }
    },
    
}

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
    "MANIFEST.in": "plaintext"
}
# ------------------------------------------------------------------------------
# 3. ORCHESTRATOR LAYER (Consumed by galaxyscope.py)
# ------------------------------------------------------------------------------

ORCHESTRATOR_RULES = {
    # Stems that are too common to count as relational popularity (The Hallucination Filter)
    "POPULARITY_STOP_STEMS": {
        # Your existing structural stems:
        "text", "type", "index", "main", "util", "config", "core", "base",
        
        # --- THE NEW SHADOW IMPORT SHIELD ---
        # Python Stdlib:
        "sys", "os", "time", "math", "re", "json", "collections", "datetime", "string", "pathlib",
        # C/C++ Stdlib (Often imported without extensions in modern C++):
        "stdio", "stdlib", "string", "math", "vector", "map", "iostream", "memory", "algorithm"
    },
    # ... [Keep your existing TEST_DIR_REGEX, etc.] ...
}

# ------------------------------------------------------------------------------
# 3.5 TEMPORAL SENSOR CONFIGURATION (Consumed by chronometer.py)
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
# 4. PHYSICS ENGINE (Consumed by signal_processor.py)
# ------------------------------------------------------------------------------
PHYSICS_CONSTANTS = {
    "WEIGHT_RISK": 2.5,
    "WEIGHT_DEFENSE": 1.0,
    
    # Trust Dampeners & Opacity Taxes
    "TIER_VARS": {
        "tier1": {"fc": 1.0,  "irc": 0}, # Explicit (Rust, Go, Java)
        "tier2": {"fc": 0.85, "irc": 2}, # Structured (Python, TS)
        "tier3": {"fc": 0.60, "irc": 5}  # Implicit (Shell, Groovy)
    },
    
    # Math constraints
    "TESTING_RISK_FLOOR": 15.0,
    "MASSIVE_FILE_THRESHOLD": 300, # Lines of code where tests lose efficacy
}

PHYSICS_ASSET_MASKS = {
    # Files strictly treated as literature (Bypasses active logic math)
    "DOCUMENTATION_LANGUAGES": {"plaintext", "markdown", "restructuredtext", "asciidoc", "org-mode", "tex", "latex"},

    
    # Files excluded from unit test exposure (Cannot be tested)
    "UNTESTABLE_EXTENSIONS": {
        "css", "html", "json", "yaml", "xml", "sql", "proto", "cmake",
        "scss", "sass", "less", "htm", "md", "mdx", "txt", "text", 
        "rst", "csv", "tsv", "log", "out", "err", "toml", "ini", 
        "cfg", "conf", "rc", "plist", "pbtxt", "graphql", "gql",
        "mk", "make", "in", "ac", "m4", "patch", "diff"
    },
    
    "UNTESTABLE_NAMES": {
        'readme', 'license', 'manifest', 'version', 'manifest.uuid', 
        'authors', 'notice', 'copying', 'changelog', 'contributing',
        'configure', 'cmake-configure', 'makefile', 'gnumakefile', 
        'cmakelists.txt', 'kbuild', 'makeconf', 'makevars',
        'build', 'install', 'setup', 'bootstrap', '__init__.py'
    },
    
    # Files invisible to the active logic rankings (e.g. JSON dumps)
    "STRUCTURAL_ASSETS": {
        "markdown", "plaintext", "rst", "text", 
        "html", "css", "scss", "sass", "less", "xml", "svg",
        "csv", "yaml", "yml", "json", "toml",
        "proto", "pbtxt", "mlir", "hlo", "td"
    }
}

FIDELITY_TIERS = {
    # Tier 1: Highly Explicit (0% Ambiguity Tax)
    'java': 1, 'csharp': 1, 'go': 1, 'rust': 1, 'kotlin': 1,
    'swift': 1, 'python': 1, 'sqlite': 1, 'micropython': 1, 'haskell': 1,
    'apex': 1, 'abap': 1, 'scala': 1, 'zig': 1, 'dart': 1, 'powershell': 1,
    'dockerfile': 1,
    
    # Tier 2: Explicit with some Implicit (15% Ambiguity Tax)
    'javascript': 2, 'typescript': 2, 'c': 2, 'cpp': 2, 'php': 2,
    'objective-c': 2, 'lua': 2, 'cobol': 2, 'fortran': 2,
    'matlab': 2,
    
    # Tier 3: Mostly Implicit (40% Ambiguity Tax)
    'shell': 3, 'ruby': 3, 'perl': 3, 'html': 3, 'css': 3,
    'assembly': 3, 'agc_assembly': 3, 'livecode': 3
}

PATH_MODIFIERS = {
    'Cognitive Load Exposure': [
        # 1. The Dictionary (Static Mapping)
        # Translation files, constants, and enums have massive line counts but almost 
        # zero logical complexity. Dampen them heavily so they don't look like giant risks.
        (re.compile(r'(?:^|/)(?:i18n|locales?|translations?|constants?|enums?)/', re.I), 0.80),

        # 2. The Abstraction (Declarations & Headers)
        # Expanded to catch C++ headers (.hpp, .hxx). These files outline structure 
        # without containing execution mass.
        (re.compile(r'\.(?:d\.ts|h|hpp|hxx)$', re.I), 0.85),

        # 3. The Config (Application Setup)
        # Expanded to catch environments and setup scripts. Usually highly declarative.
        (re.compile(r'(?:^|/)(?:configs?|settings|environments?|setup|makefile|\.env)\b', re.I), 0.70),
        
        # 4. The Junk Drawer (Low-Context Logic)
        # Utilities and helpers lack specific domain context. Developers have to guess 
        # what parts of the app use them, slightly increasing the cognitive tax.
        (re.compile(r'(?:^|/)(?:utils?|helpers?|common|shared)/', re.I), 1.05),

        # 5. The Deep Nest (Structural Complexity)
        # Files buried 5+ directories deep (e.g., src/app/modules/user/views/components/btn.js). 
        # High cognitive load just to mentally map where the file lives in the galaxy.
        (re.compile(r'(?:[^/]+/){5,}'), 1.10),

        # 6. The Brain (Global State Management)
        # Reducers, stores (Redux/Vuex/MobX), and global contexts. These files manipulate 
        # data that affects the entire application, requiring massive mental overhead to edit safely.
        (re.compile(r'(?:^|/)(?:stores?|states?|reducers?|contexts?)/', re.I), 1.15),
        # 7. The Verification Sieve
        # Test files are naturally dense with assertions and mocked data. 
        # Dampen their cognitive load so they don't outweigh actual application logic.
        (re.compile(r'(?:^|/)(?:tests?|specs?|testing)/|_spec\.[a-z]+$|\.test\.[a-z]+$', re.I), 0.50)
    ],
    'Error & Exception Exposure': [
        # 1. The Sentinel (Core Security & Auth)
        # Highly secure zones dedicated to authentication, authorization, and cryptography.
        # Massive reduction in risk exposure because this is explicit defensive mass.
        (re.compile(r'(?:^|/)(?:auth|security|policies|permissions|roles|crypto)/', re.I), 0.80),

        # 2. The Contract (Strong Typing, Models & Schemas)
        # Expanded to catch DTOs, Schemas, Contracts, TypeScript declaration files, 
        # and standard POJO/Entity bags (e.g., /data/, /models/). 
        # Shields simple data buckets from being penalized for lacking defensive logic.
        (re.compile(r'(?:^|/)(?:types|interfaces|schemas|dtos|contracts|data|models|entities|pojos)/|\.d\.ts$', re.I), 0.85),

        # 3. The Validator (Input & Boundary Defense)
        # Expanded to catch modern request pipelines like middleware and interceptors.
        (re.compile(r'(?:^|/)(?:validators?|sanitizers?|guards?|middlewares?|interceptors?)/', re.I), 0.90),

        # 4. The Unsafe Zone (Raw & Unchecked Data)
        # Areas where memory management or input sanitization is deliberately turned off.
        # Added 'danger' (e.g., dangerouslySetInnerHTML) and 'unverified'.
        (re.compile(r'(?:^|/)(?:unsafe|raw|danger|escape|unverified)/', re.I), 1.25),

        # 5. The Override (Explicit Safety Bypasses)
        # Distinct from Tech Debt. These are files specifically named to bypass 
        # security, typing, or linting rules (e.g., /force/, /ignore/).
        (re.compile(r'(?:^|/)(?:bypasses?|overrides?|ignores?|force)/', re.I), 1.20)
    ],
    'Tech Debt Exposure': [
        # 1. The Museum (Safely Retired / Ignored)
        # Amplifies slightly, but dampens overall execution risk because it's not active.
        # Added 'obsolete' and 'old'
        (re.compile(r'(?:^|/)(?:archive|legacy|deprecated|obsolete|old)s?/', re.I), 0.50), 

        # 2. The Scratchpad (Unfinished / Volatile)
        # High volatility. Added 'temp' and 'draft'.
        (re.compile(r'(?:^|/)(?:tmp|temp|scratch|wip|draft)s?/', re.I), 1.05),

        # 3. The Laboratory (Experimental Code)
        # Features that were tested but never fully merged or cleaned up. 
        # Extremely high risk if accidentally imported into core logic.
        (re.compile(r'(?:^|/)(?:experimental|experiments|sandbox|spikes?)/', re.I), 1.10),

        # 4. The Duct Tape (Hacks & Workarounds)
        # Code explicitly named as a patch, shim, or hack. This is the definition 
        # of structural tech debt and deserves a high exposure penalty.
        (re.compile(r'(?:^|/)(?:hacks?|patches|shims|polyfills|workarounds)/', re.I), 1.15),

        # 5. The Graveyard (Dead / Backup Files)
        # If files with these extensions bypassed the Aperture filter and made it 
        # to the pipeline, they are pure cognitive load and high debt.
        (re.compile(r'\.(?:bak|old|orig|conflict)$', re.I), 1.20),
        # The Build Config Exemption 
        # Gradle files often contain tooling TODOs that do not reflect architectural logic debt.
        (re.compile(r'\.gradle$', re.I), 0.0),

        # The Verification Exemption
        # Tests often contain mocked "TODO" strings to test parsers, or deliberate hacks 
        # for negative testing. They do not represent architectural debt.
        (re.compile(r'(?:^|/)(?:tests?|specs?|testing)/|_spec\.[a-z]+$|\.test\.[a-z]+$|.*IT\.java$', re.I), 0.0),

        # ---> NEW: The Documentation/Examples Exemption <---
        # Forgive example code for lacking production-grade tests/safety
        (re.compile(r'(?:^|/)examples?/', re.I), 0.0)
    ],
    'Documentation Exposure': [
        # 1. The Blueprint (Standard Directories)
        # Expanded to catch singular /doc/, /tutorials/, /guides/, and /wiki/
        (re.compile(r'(?:^|/)(?:docs?|examples?|tutorials?|guides?|wiki|man)/', re.I), 0.0),
        
        # 2. The Glossary (Core Repository Literature)
        # Catches standard root or nested community files (README, CHANGELOG, CONTRIBUTING, etc.)
        (re.compile(r'(?:^|/)(?:README|CHANGELOG|CONTRIBUTING|LICENSE|INSTALL|AUTHORS|SECURITY)\b', re.I), 0.0),        
        # 3. The Atlas (Standard Documentation Formats)
        # Captures Markdown, MDX (React Markdown), and reStructuredText (Python) anywhere in the repo
        (re.compile(r'\.(?:md|mdx|rst)$', re.I), 0.00),
        
        # 4. The Interactive Spec (API Docs & Notebooks)
        # Catches Swagger/OpenAPI schemas and Jupyter Notebooks (executable examples)
        (re.compile(r'(?:^|/)(?:swagger|openapi)\.(?:json|yaml|yml)$|\.ipynb$', re.I), 0.90),

        # 5. The Story (UI Component Documentation)
        # Expanded slightly to catch singular `.story.` formats just in case
        (re.compile(r'\.(?:stories|story|visual)\.', re.I), 0.90),
        # 6. The Verification Exemption
        # Unit tests rarely require formal JSDoc/RDoc blocks. Drop doc risk to 0.
        (re.compile(r'(?:^|/)(?:tests?|specs?|testing)/|_spec\.[a-z]+$|\.test\.[a-z]+$', re.I), 0.0)
    ],
    'Testing Exposure': [
        # 1. The Universal Standard: 'test' is safe across all languages
        (re.compile(r'(?:^|/)tests?/|(?:^|/)testing/|\.test\b|_test\b', re.I), 0.0), 
        
        # 2. The Spec Sieve (Ruby, JS/TS, Dart)
        # Only drops to 0 if the file inside /spec/ belongs to a spec-heavy language, 
        # OR if it explicitly has '.spec' or '_spec' in the filename.
        (re.compile(r'(?:^|/)specs?/.*\.(?:rb|js|jsx|ts|tsx|dart)$|\.spec\b|_spec\b', re.I), 0.0),
        
        # 3. The Perl Sieve
        # Strictly requires the file to be a .t file if it lives in a t/ folder
        (re.compile(r'(?:^|/)t/.*\.t$', re.I), 0.0),
        
        # 4. Standard E2E and Mock Blankets
        (re.compile(r'^e2e/|^cypress/|^playwright/', re.I), 0.00),
        (re.compile(r'/mocks/|/__mocks__/', re.I), 0.00),
        
        # 5. Build Orchestration Exemption (Do not punish build scripts for lacking unit tests)
        (re.compile(r'(?:^|/)tools?/|(?:^|/)build/|(?:^|/)scripts?/', re.I), 0.0),
        
        # 6. Specific Directory & File Exemptions
        # Forgive the autosetup directory for not having tests
        (re.compile(r'(?:^|/)autosetup/', re.I), 0.0),
        
        # Dampen the testing expectation for the WASM build tools
        (re.compile(r'(?:^|/)ext/wasm/mkdist\.sh$', re.I), 0.0),
        
        # Forgive global configure scripts
        (re.compile(r'(?:^|/)configure\.sh$', re.I), 0.0),
        
        # Forgive WordPress UI Pattern arrays for lacking PHPUnit tests
        (re.compile(r'(?:^|/)inc/patterns/', re.I), 0.0),

        # 7. The Legacy CGI Exemption
        # Root-level CGI scripts (common in 90s/00s Perl) are tested via E2E browser automation.
        (re.compile(r'^[^/]+\.cgi$', re.I), 0.0),

        # ---> NEW: The Documentation/Examples Exemption <---
        # Forgive example code for lacking production-grade tests/safety
        (re.compile(r'(?:^|/)examples?/', re.I), 0.0)
    ],
    'Dead Code Exposure': [
        # 1. The Template (Expected Dead Code)
        # Boilerplates, stubs, and generators intentionally contain commented-out 
        # "example" code. Dampen this heavily so the engine doesn't penalize it.
        (re.compile(r'(?:^|/)(?:templates?|stubs?|scaffolds?|fixtures?|examples?)/', re.I), 0.75),

        # 2. The Lab (Experimental Safe Zones)
        # Expanded to include sandboxes and drafts. Dead/commented code here is 
        # just part of the scientific process.
        (re.compile(r'(?:^|/)(?:experiments?|poc|spikes?|sandbox|playgrounds?|drafts?)/', re.I), 0.85),

        # 3. The Critical Path (Core Application Logic)
        # Expanded to include /src/, /lib/, and /services/. Leaving dead code in 
        # the main execution arteries creates structural friction and doubt.
        (re.compile(r'(?:^|/)(?:core|kernel|main|src|lib|services|providers)/', re.I), 1.15),

        # 4. The Brainstem (Application Entrypoints)
        # The absolute worst place for dead code. Files like index.js, main.go, or App.tsx 
        # are the first things a new developer reads. Commented-out garbage here 
        # sets a terrible precedent and deserves maximum penalty.
        (re.compile(r'(?:^|/)(?:index|main|app|server|bootstrap|init)\.(?:js|ts|jsx|tsx|go|py|c|cpp|rs|java)$', re.I), 1.25)
    ],
    'API Exposure': [
        # 1. The Event Hook (Inbound Triggers)
        # Webhooks and event subscribers that listen to third-party systems 
        # (like Stripe or GitHub). High exposure to external payload formats.
        (re.compile(r'(?:^|/)(?:webhooks?|listeners?|subscribers?|events?)/', re.I), 1.10),

        # 2. The Billboard (Standard HTTP/REST)
        # Expanded to catch routes, routers, handlers, and endpoints. 
        # This is the standard "front door" for client-to-server traffic.
        (re.compile(r'(?:^|/)(?:api|controllers?|routes?|routers?|handlers?|endpoints?)/', re.I), 1.15),

        # 3. The Graph (Complex Data Queries)
        # GraphQL and RPC (gRPC, tRPC) layers. These files expose massive, 
        # interconnected data graphs to the client. A mistake here can cause 
        # catastrophic N+1 database queries or data leaks.
        (re.compile(r'(?:^|/)(?:graphql|resolvers?|mutations?|queries|rpc|grpc|trpc)/', re.I), 1.20),

        # 4. The Distribution Contract (SDKs & Public Exports)
        # Expanded to catch packages and public-facing barrels. If a file lives in an 
        # SDK or /pkg/ directory, modifying it forces every consumer to update. 
        # This carries the absolute highest architectural risk penalty.
        (re.compile(r'(?:^|/)(?:sdk|public|pkg|packages?|exports?)/', re.I), 1.25)
    ],
    'Concurrency Exposure': [
        # 1. The Isolated Worker (Expected Async)
        # Dedicated background processors, thread pools, and task queues. 
        # Concurrency here is expected and architecturally isolated, so we dampen the risk.
        (re.compile(r'(?:^|/)(?:workers?|jobs?|queues?|tasks?|threads?|pools?|background)/', re.I), 0.85),

        # 2. The Stream (Continuous Temporal Flux)
        # Real-time data pipes like WebSockets or RxJS observables. Higher baseline 
        # risk because data is constantly in motion and state is volatile.
        (re.compile(r'(?:^|/)(?:streams?|sockets?|websockets?|pubsub|observables?|rx)/', re.I), 1.05),

        # 3. The UI Tangle (Client-Side Race Conditions)
        # Expanded to catch pages and screens. UI components that execute heavy asynchronous 
        # logic are the classic source of "unmounted-component" memory leaks and visual race conditions.
        (re.compile(r'(?:^|/)(?:ui|views?|components?|pages?|screens?)/', re.I), 1.15),

        # 4. The Global Mutator (State-Level Race Conditions)
        # Global state stores (Redux, Zustand, Vuex) managing concurrent operations. 
        # A race condition here doesn't just glitch a button; it corrupts the entire application state.
        (re.compile(r'(?:^|/)(?:stores?|states?|reducers?|contexts?)/', re.I), 1.20), 
        
        # 5. The Declarative Baseline (Material Science)
        # HTML/CSS/XML use declarative tags for resource fetching (lazy loading, async scripts).
        # This is handled by the browser engine, not the developer, carrying near-zero execution risk.
        (re.compile(r'\.(html|htm|css|scss|svg|xml)$', re.I), 00.0)
    ],
    'State Flux Exposure': [
        # 1. The Warehouse (Expected State Mutations)
        # Dedicated state managers, databases, and caches. Flux here is the 
        # primary purpose of the file, so we dampen the risk exposure.
        # Expanded to catch modern stores like Pinia, Zustand, and Vuex.
        (re.compile(r'(?:^|/)(?:stores?|states?|redux|vuex|pinia|zustand|mobx|contexts?|databases?|caches?)\b', re.I), 0.85),
        
        # 2. The Transaction (Local Volatility)
        # Dedicated mutation handlers, form controllers, and actions. 
        # Expected to have high variable turnover, but safely scoped.
        (re.compile(r'(?:^|/)(?:mutations?|actions?|forms?|inputs?)/', re.I), 0.95),

        # 3. The View Tangle (Component-Level Side Effects)
        # UI components should ideally consume state, not mutate it wildly. 
        # High state flux in a /components/ or /views/ directory indicates massive 
        # prop-drilling, "spaghetti" hooks, and a high risk of render loop bugs.
        (re.compile(r'(?:^|/)(?:components?|views?|pages?|screens?)/', re.I), 1.10),

        # 4. The Magic Side-Effect (Junk Drawer Mutations)
        # Utility and helper functions should strictly be "pure functions" (input -> output). 
        # If a file in /utils/ is heavily mutating variables or triggering state 
        # changes, it is a hidden side-effect and highly dangerous.
        (re.compile(r'(?:^|/)(?:utils?|helpers?|shared|common)/', re.I), 1.15),

        # 5. The Global Poison (Runtime Configuration Changes)
        # The absolute highest state flux risk. Files designated for environments, 
        # constants, or configs should be completely static after boot. If the 
        # engine detects state mutations here, the application is poisoning its own roots.
        (re.compile(r'(?:^|/)(?:configs?|envs?|globals?|constants?|settings?)/', re.I), 1.25),
        # The Migration Exemption (Database State Changes)
        # SQL and migration scripts are designed to mutate state. Dampen to 0.
        (re.compile(r'(?:^|/)migrations?/|\.sql$', re.I), 0.0),
        # The Migration Exemption (Database State Changes)
        # SQL, migration scripts, and Gradle configs are designed to mutate state. Dampen to 0.
        (re.compile(r'(?:^|/)migrations?/|\.sql$|\.gradle$', re.I), 0.0),

        # ---> NEW: The Verification Exemption (Integration Tests & Mocks) <---
        # Integration tests (*IT.java) are highly volatile by design to mock state changes.
        (re.compile(r'(?:^|/)(?:tests?|specs?|testing)/|.*IT\.java$', re.I), 0.0),

        # ---> NEW: The Documentation/Examples Exemption <---
        # Forgive example code for lacking production-grade tests/safety
        (re.compile(r'(?:^|/)examples?/', re.I), 0.0)
    ],
    'Structural Mass': [        
        # The Cryptographic & Test Vector Dampener
        # Auto-generated data arrays explode parser argument math. Extreme reduction 
        # prevents these static payloads from registering as massive logic hubs.
        (re.compile(r'(?:^|/)(?:wycheproof_tests|test_vectors|testdata|tests/data)/', re.I), 0.001),
        
        # The Code-Generation Dampener
        # Deeply dampens auto-generated files (e.g., Protobufs, boilerplate) 
        # so machine-written code doesn't mathematically outweigh human architecture.
        (re.compile(r'(?:^|/)(?:zz_generated.*|.*\.pb\.go|.*\.generated\.go)', re.I), 0.05), 

        # ---> NEW: The DB Migration & Schema Dampener <---
        # Dampens auto-generated database migrations and schema snapshots. These are 
        # declarative mappings of state, not complex, human-maintained execution paths.
        (re.compile(r'(?:^|/)(?:migrations?|schema)/.*\.(?:sql|ts|js|rb|py)$|(?:\d{10,}_[a-z0-9_]+\.(?:ts|js|rb|py|sql))$', re.I), 0.05),
        
        # The Vendored Directory Dampener
        # Neutralizes standard third-party ecosystem folders (vendor, node_modules) 
        # to prevent external dependencies from eclipsing the core repository.
        (re.compile(r'(?:^|/)(?:resources/lib|vendor|node_modules|third_party)/', re.I), 0.02),

        # The Global Frontend Vendor Dampener
        # Neutralizes massive JS bundles (jQuery, React, minified files) that hide 
        # outside standard vendor folders, preventing them from crushing the physics engine.
        (re.compile(r'(?:^|/)(?:jquery[^/]*\.js|bootstrap[^/]*\.js|typeahead[^/]*\.js|.*\.min\.js)$', re.I), 0.01),

        # ---> NEW: The Compiled Chunk & Bundle Dampener <---
        # Neutralizes Webpack/Vite production build outputs (e.g., main.a8b9.js, chunk-123.js)
        # that leak into public/ or static/ directories, mimicking massive logic hubs.
        (re.compile(r'(?:^|/)(?:chunk-[a-z0-9_.-]+|main\.[a-f0-9]{8,}\.(?:js|css)|[a-z0-9_.-]+\.bundle\.js)$', re.I), 0.01),

        # ---> NEW: The React SVG / Vector Graphics Dampener <---
        # Dampens UI components that are purely exported SVG path data (e.g., Icon.jsx).
        # Prevents raw vector math from artificially inflating UI framework density.
        (re.compile(r'(?:^|/)(?:icons?|illustrations?|logos?|assets?)/.*\.jsx?|tsx?$', re.I), 0.10),

        # ---> NEW: The Test Snapshot & Fixture Dampener <---
        # Neutralizes auto-generated UI snapshots and massive mock data payloads (like cryptographic keys)
        # so they do not artificially inflate the mass of the verification suite.
        (re.compile(r'(?:^|/)(?:__snapshots__|__mocks__|fixtures?)/|.*\.snap$', re.I), 0.001),

        # ---> NEW: The Academic Test Script Dampener <---
        # Heavily reduces the mass of massive procedural test/bug scripts in academic MATLAB/Python repos.
        (re.compile(r'(?:^|/)test/test_.*\.m$', re.I), 0.05),
        
        # The DevOps & Automation Dampener
        # Reduces the structural weight of CI/CD shell scripts and automation tooling 
        # so deployment pipelines don't mimic core application complexity.
        (re.compile(r'(?:^|/)(?:scripts?|ci|cd|docker|e2e)/.*\.(?:sh|bash|zsh)$', re.I), 0.10),
        
        # The Declarative & Type Definition Dampener
        # Dampens TS types and CSS files, as union types and variables artificially 
        # inflate branch/argument math without containing active execution logic.
        (re.compile(r'\.css$|\.scss$|\.d\.ts$|\.types\.ts$|/types\.ts$|params?\.ts$|schema\.ts$', re.I), 0.05),
        
        # The Parser & Lexer Tooling Dampener
        # C-based lexers and code generators explode mass calculations due to giant 
        # auto-generated switch statements. Neutralizes their structural gravity.
        (re.compile(r'(?:^|/)(?:tools|chem/KPP/kpp|var/da/makedepf90[^/]*)/', re.I), 0.001),
        
        # The External Modules Dampener
        # Heavily reduces the weight of external I/O or bundled communication libraries 
        # so they do not distort the physical footprint of the primary application.
        (re.compile(r'(?:^|/)external/', re.I), 0.001),   
        
        # The Upstream Ports Dampener
        # Reduces the mass of vendored upstream ecosystem ports (like contrib/crypto) 
        # ensuring the map focuses on the native system architecture.
        (re.compile(r'(?:^|/)(?:contrib|crypto)/', re.I), 0.01),
        # The Translation & Localization Dampener
        # Crushes massive i18n YAML/JSON dictionaries so they don't outweigh application logic.
        (re.compile(r'(?:^|/)locales?/', re.I), 0.001),

        # ---> NEW: The Generated HTML Docs Dampener <---
        # Prevents auto-generated HTML reference tables from mimicking web-app architecture mass.
        (re.compile(r'(?:^|/)html/.*\.html$', re.I), 0.001), 
        # ---> NEW: The Dart Code-Generation Dampener <---
        # Dampens auto-generated Dart files (.g.dart, .freezed.dart) so their massive 
        # static data arrays don't masquerade as thousands of logic functions.
        (re.compile(r'\.(?:g|freezed)\.dart$', re.I), 0.05), 
        # ---> NEW: The Go Compiler & CGO Auto-Gen Dampener <---
        # Crushes massive compiler-generated SSA rules and CGO-generated system 
        # bindings so they don't masquerade as dense human logic.
        (re.compile(r'(?:^|/)(?:rewrite[A-Za-z0-9_]+\.go|z[a-z0-9_]+\.go|opGen\.go|malloc_generated\.go)$', re.I), 0.001),
    ]
    }

# ------------------------------------------------------------------------------
# 4.5 RISK EQUATION TUNING (The Physics Engine Knobs)
# ------------------------------------------------------------------------------
# These constants control the sigmoid curves, thresholds, and hit-weights
# used to calculate 0-100% risk exposures.
RISK_EQUATION_TUNING = {
    "cognitive_load": {
        "branch_clamp": 0.5, "flux_clamp": 0.75, "flux_mult": 2.0,
        "async_mult": 3.0, "heat_mult": 5.0, "danger_mult": 5.0,
        "sigmoid_slope": 4.0, "sigmoid_offset": 0.75, "doc_mult": 10.0
    },
    "safety": {
        "danger_weight": 4.0, "safety_neg_weight": 1.5, "flux_weight": 0.5,
        "test_weight": 0.5, "doc_weight": 0.1,
        "laplace_smoothing": 20.0, "systems_buffer": 0.25,
        "sigmoid_slope": 12.0,
        "breach_density_min": 0.03, "breach_floor_mult": 500.0, "breach_floor_max": 80.0
    },
    "tech_debt": {
        "good_debt_weight": 1.0, "bad_debt_weight": 3.0, "stub_weight": 0.5, "irc_weight": 0.5,
        "threshold": 5.0, "sigmoid_slope": 0.5
    },
    "documentation": {
        "doc_weight": 1.0, "ownership_weight": 0.5, "doc_loc_weight": 0.33,
        "threshold_base": 10.0, "sigmoid_slope": 0.2
    },
    "verification": {
        "sibling_bonus": 30.0, "internal_test_mult": 5.0,
        "threshold_base": 15.0, "irc_mult": 3.0, "sigmoid_slope": 0.25,
        "mass_penalty_div": 20.0, "mass_penalty_max": 40.0,
        "risk_floor": 15.0
    },
    "graveyard": {
        "hit_mult": 3.0, "safe_mass_floor": 50.0,
        "threshold_base": 10.0, "sigmoid_slope": 0.3
    },
    "api_exposure": {
        "log_divisor": 1.5, "ratio_weight": 0.4, "volume_weight": 0.6
    },
    "concurrency": {
        "irc_mult": 0.1, "threshold_base": 4.0, "sigmoid_slope": 0.4
    },
    "state_flux": {
        "irc_mult": 0.15, "threshold_base": 15.0, "sigmoid_slope": 0.20
    }
}

# ------------------------------------------------------------------------------
# 4.6 LANGUAGE SECURITY PROFILES (The Context vs. Entity Matrix)
# Defines domain ontologies to cure the "Apollo Paradox" and detect Trojan Horses.
# ------------------------------------------------------------------------------
LANGUAGE_SECURITY_PROFILES = {
    "ECOSYSTEMS": {
        # Bare metal, embedded, and legacy mainframe. Pointer math and direct OS hooks are native.
        "systems": {
            "c", "cpp", "rust", "assembly", "agc_assembly", "zig", "cobol", 
            "fortran", "micropython", "objective-c"
        },
        # High DOM flux, UI components, and massive string manipulation. Highly vulnerable to XSS.
        "web": {
            "javascript", "typescript", "html", "css", "php", "ruby", 
            "dart", "livecode"
        },
        # Deployment, orchestration, and scripting. OS execution is the literal purpose.
        "infra": {
            "shell", "powershell", "dockerfile", "yaml", "makefile", "m4", 
            "xml", "json", "toml", "sqlite", "csv", "plaintext"
        },
        # Data processing, APIs, and strict-typed object orientation. 
        "backend": {
            "python", "java", "go", "csharp", "kotlin", "scala", "scheme", 
            "tcl", "matlab", "perl", "haskell", "lua", "apex", "swift"
        }
    },
    
    # Baseline multipliers applied when the file MATCHES its neighborhood's dominant ecosystem
    "NATIVE_WEIGHTS": {
        "systems": {"memory": 0.1, "logic_bomb": 0.2, "flux": 1.0, "injection": 1.0}, # Pointer math is normal
        "web":     {"memory": 1.0, "logic_bomb": 1.0, "flux": 0.3, "injection": 2.0}, # DOM flux is normal, XSS is deadly
        "infra":   {"memory": 1.0, "logic_bomb": 0.0, "flux": 1.0, "injection": 1.0}, # OS commands are literally the point
        "backend": {"memory": 1.5, "logic_bomb": 1.0, "flux": 1.5, "injection": 1.5}  # Standard aggressive baseline
    },
    
    # Aggressive penalties applied when the file is an ALIEN in its neighborhood
    "ALIEN_WEIGHTS": {
        "systems_in_web": {"memory": 5.0, "logic_bomb": 3.0}, # C code hiding in a JS app = Trojan
        "infra_in_web":   {"logic_bomb": 4.0},                # Shell script hiding in a JS app = Backdoor
        "web_in_systems": {"flux": 3.0}                       # JS embedded in C firmware = Bizarre architecture
    }
}

# ------------------------------------------------------------------------------
# 5. SCHEMA & EXPORT REGISTRY (Consumed by recorders & SQLite)
# ------------------------------------------------------------------------------
RECORDING_SCHEMAS = {
    "RISK_SCHEMA": [
        "cognitive_load", "safety_score", "tech_debt", "verification", 
        "api_exposure", "concurrency", "state_flux", "graveyard", 
        "spec_match", "stability", "churn", "documentation", "civil_war",
        # --- THE SECURITY & VULNERABILITY LENSES ---
        "obscured_payload", "logic_bomb", "injection_surface", 
        "memory_corruption", "secrets_risk"
    ],
    "SIGNAL_SCHEMA": [
        "branch", "linear", "args", "func_start", "class_start",
        "safety", "safety_neg", "danger", "io", "api", "flux", "graveyard", "doc", "test",
        "concurrency", "ui_framework", "closures", "globals", "decorators", "generics", 
        "comprehensions", "scientific", "heat_triggers", "import", "ownership",
        "planned_debt", "fragile_debt", "spec_exposure", "civil_war", 
        "ssr_boundaries", "events", "dependency_injection", "macros", "pointers", 
        "memory_alloc", "inline_asm", "telemetry", "print_hits", "cast_hits", 
        "bailout_hits", "halt_hits", "bitwise_hits", "sync_locks", "freeze_hits", 
        "cleanup", "encapsulation", "listeners", "test_skip",
        "indent_tabs", "indent_spaces",
        # --- NEW: PASSIVE SECURITY LENS OBSERVERS ---
        "sec_heat_triggers", "sec_safety_neg", "sec_io", "sec_danger", 
        "sec_flux", "sec_graveyard", "sec_bitwise_hits", "sec_shadow_imports",
        "sec_homoglyphs", "sec_private_info"
    ],
    "SAT_SCHEMA": [
        "name", "loc", "branch", "angle_x10", "args", "type_id", "control_flow_x1000", "mag_x10", "start_line", "end_line"
    ],
    "GPU_TEXTURE_LOOKUPS": [
        "standard", "crystalline", "plates", "digital", "metallic", 
        "necrosis", "io", "check", "verification", "mutation", 
        "event", "logic", "danger"
    ],
    "FRIENDLY_MAP": {
        "m_locs": "Coding Lines of Code (LOC)", "locs": "Total Lines of Code (LOC)",
        "lang_ids": "Detected Languages", "lang_id": "Primary Language",
        "mass": "Structural Complexity Mass", "author_distribution": "Author Distribution",
        "control_flow_ratio": "Control Flow Ratio",
        "verification": "Testing & Verification Exposure", "cognitive_load": "Cognitive Load Exposure",
        "safety_score": "Error & Exception Exposure", "tech_debt": "Technical Debt Exposure",
        "spec_match": "Specification Audit Alignment", "churn": "Code Volatility (Churn)",
        "documentation": "Documentation Risk Exposure", "api_exposure": "Public API Surface Area",
        "state_flux": "State Mutation Exposure", "branch": "Control Flow Branches",
        "linear": "Sequential Logic Declarations", "args": "Function Parameters",
        "func_start": "Function/Method Declarations", "class_start": "Class/Entity Declarations",
        "safety": "Defensive Programming Constructs", "safety_neg": "Type/Safety Bypasses",
        "danger": "High-Risk Execution Commands", "io": "I/O and Network Boundaries",
        "api": "Exposed API / Public Exports", "flux": "State Mutations / Variable Reassignments",
        "graveyard": "Commented-out Code (Dead Logic)", "doc": "Structured Documentation Blocks",
        "test": "Unit Test Assertions", "concurrency": "Asynchronous/Concurrent Execution",
        "ui_framework": "UI / View Layer Components", "closures": "Closures and Anonymous Functions",
        "globals": "Global State Dependencies", "decorators": "Decorators and Annotations",
        "generics": "Generic Type Abstractions", "comprehensions": "Collection Iterators / Comprehensions",
        "scientific": "Scientific & Mathematical Operations", "heat_triggers": "Metaprogramming & Reflection",
        "import": "Module Dependencies (Imports)", "ownership": "Authorship Metadata",
        "planned_debt": "Planned Work (TODOs)", "fragile_debt": "Acknowledged Tech Debt (FIXMEs)",
        "spec_exposure": "Specification Traceability Tags",
        "civil_war": "Indentation Faction", "ssr_boundaries": "Server-Side Rendering Contexts",
        "events": "Event Publishers / Emitters", "dependency_injection": "Dependency Injection Constructs",
        "macros": "Preprocessor Macros", "pointers": "Pointer Arithmetic & Addressing",
        "memory_alloc": "Manual Memory Allocation", "inline_asm": "Inline Assembly Blocks",
        "telemetry": "Structured Telemetry & Logging", "print_hits": "Ad-hoc Print / Debug Statements",
        "cast_hits": "Explicit Type Casts", "bailout_hits": "Fatal Aborts & Exceptions",
        "halt_hits": "Thread Sleeps & Blocking Waits", "bitwise_hits": "Bitwise Operations",
        "sync_locks": "Thread Synchronization Locks", "freeze_hits": "Immutable Data Declarations",
        "cleanup": "Resource Deallocation & Cleanup", "encapsulation": "Private / Encapsulated Scopes",
        "listeners": "Event Listeners & Subscribers", "test_skip": "Bypassed / Skipped Tests",
        "indent_tabs": "Structural Tab Indentations", "indent_spaces": "Structural Space Indentations",
        # --- SECURITY LENS UI MAPPINGS (Plain English) ---
        "sec_heat_triggers": "High-Entropy / Obfuscated Logic",
        "sec_safety_neg": "Safety & Constraint Bypasses",
        "sec_io": "External Network & I/O Hooks",
        "sec_danger": "Dynamic Code Execution (Eval/Exec)",
        "sec_flux": "Global Environment Mutation",
        "sec_graveyard": "Commented-Out Executable Logic",
        "sec_bitwise_hits": "Low-Level Bitwise / Cryptographic Math",
        "sec_shadow_imports": "Non-Standard / Steganographic Imports",
        "sec_homoglyphs": "Non-Standard Unicode / Homoglyphs",
        "sec_private_info": "Embedded Credentials & Keys",
        
        # --- VULNERABILITY EXPOSURE MAPPINGS (Plain English) ---
        "obscured_payload": "Obfuscation & Evasion Surface",
        "logic_bomb": "Exploit Generation Surface",
        "injection_surface": "Weaponized Injection Vectors",
        "memory_corruption": "Raw Memory Manipulation",
        "secrets_risk": "Hardcoded Payload Artifacts"
    },
    "EXPOSURE_LABELS": {
        "cognitive_load": "Cognitive Load Exposure", "safety_score": "Error & Exception Exposure",
        "tech_debt": "Tech Debt Exposure", "verification": "Testing Exposure",
        "api_exposure": "API Exposure", "concurrency": "Concurrency Exposure",
        "state_flux": "State Flux Exposure", "graveyard": "Graveyard Exposure",
        "spec_match": "Specification Exposure", "stability": "Instability Exposure",
        "churn": "Volatility Exposure", "documentation": "Documentation Exposure",
        "civil_war": "Civil War Exposure",
        
        # --- SECURITY LENS UI LABELS (Plain English) ---
        "obscured_payload": "Obfuscation & Evasion Surface",
        "logic_bomb": "Exploit Generation Surface",
        "injection_surface": "Weaponized Injection Vectors",
        "memory_corruption": "Raw Memory Manipulation",
        "secrets_risk": "Hardcoded Payload Artifacts"
    }
}
        
# ------------------------------------------------------------------------------
# 6. DIALECTS (Project-Specific Overrides)
# ------------------------------------------------------------------------------
PROJECT_OVERRIDES = {
    "freebsd-src": {
        # FreeBSD uses .m for KOBJ (Kernel Object) files which are pure C.
        # We must strip .m from Obj-C and map it to C to prevent engine hallucination.
        "objective-c": {
            "extensions": ['.mm', '.h'] # Removed .m
        },
        "c": {
            # THE FIX: Preserved the .m override, but synced with the new .dts/.dtsi baseline!
            "extensions": ['.c', '.h', '.cl', '.inc', '.y', '.idc', '.cats', '.m', '.dts', '.dtsi'] 
        }
    },
    
    "wrf-fortran": {
        # --- 1. SHIELD/APERTURE OVERRIDES ---
        "_shield_": {
            "unban_directories": ["var", "external", "test"]
        },
        # --- 2. LINGUISTIC OVERRIDES ---
        "fortran": {
            "concurrency": re.compile(r'\b(COARRAY|SYNC\s+ALL|CRITICAL|MPI_[A-Za-z_]+|wrf_dm[A-Za-z0-9_]*|RSL[A-Za-z0-9_]*)\b|!\$(?:OMP|ACC)\b', re.I)        
        }
    },
    
    "Apollo-11": {
        "agc_assembly": {
            # The multi-line block header (e.g., "FUNCTIONAL DESCRIPTION")
            '_meta_purpose_block': re.compile(r'^[ \t]*(?:FUNCTIONAL|PROGRAM)\s+DESCRIPTION\b', re.I),
            
            # The fallback single-line (or indented) description (e.g., "Purpose: Part of the source...")
            '_meta_purpose_line': re.compile(r'^[ \t]*Purpose[\s:\-]*(.*)', re.I),
            
            # The Escape Hatch. If the parser is reading the fallback Purpose line, hitting any of these headers tells it to stop.
            '_meta_boundary': re.compile(r'^[ \t]*(?:Assembler|Filename|Pages|Website|Mod history|Copyright|Reference|PROGRAM NAME)[\s:\-]+', re.I)
        }
    },

    "cpython": {
        # --- 1. SHIELD/APERTURE OVERRIDES ---
        "_shield_": {
            "exclude_paths": [
                "Lib/pydoc_data/topics.py", # The Supermassive Documentation Dictionary
                "configure",                # The 36,000-line generated autotools script
            ],
            "exclude_dirs": [
                "Modules/clinic",           # Auto-generated C-API boilerplate
            ]
        }
    },
    "AppFlowy": {
        # --- 1. SHIELD/APERTURE OVERRIDES ---
        "_shield_": {
            "exclude_dirs": [
                "scripts",           # Hard-blocks the shell script invasion (overrides VIP intent)
                "integration_test"   # Hard-blocks the massive test suites we saw earlier
            ],
            "exclude_paths": [
                "install.sh"         # Kills the specific root-level installer
            ]
        }
    },
    
    "ansible": {
        # --- 1. SHIELD/APERTURE OVERRIDES ---
        "_shield_": {
            "exclude_dirs": [
                ".azure-pipelines",  # Hard-blocks all Azure pipeline YAMLs and shell scripts
                ".github"            # Blocks GitHub Actions noise
            ]
        }
    },
    "bugzilla": {
        "html": {
            # Injects .tmpl into the standard HTML extension surface area
            "extensions": [
                ".html", ".htm", ".xhtml", ".cshtml", ".vue", ".svelte", 
                ".astro", ".ejs", ".hbs", ".twig", ".erb", ".tmpl"
            ]
        }
    },
    "bun": {
        # --- 1. SHIELD/APERTURE OVERRIDES ---
        "_shield_": {
            "exclude_dirs": [
                "scripts" # Hard-blocks the CI/CD shell scripts from grabbing a VIP pass
            ]
        },
    },
    "curl": {
        "plaintext": {
            # Injects man pages and text docs into the plaintext surface area
            "extensions": [
                ".txt", ".text", ".log", ".out", ".err", ".nfo", 
                ".1", ".3", ".d"
            ]
        }
    },
    "discourse": {
        # --- 1. SHIELD/APERTURE OVERRIDES ---
        "_shield_": {
            "exclude_paths": [
                "config/unicorn_launcher", # Hard-blocks the server boot script
                "pnpm-lock.yaml",          # Banishes the massive lockfile
                "yarn.lock"
            ]
        },
        # --- 2. LINGUISTIC OVERRIDES ---
        "javascript": {
            # Maps Ember Glimmer components (.gjs) so the frontend isn't invisible
            "extensions": [
                ".js", ".jsx", ".mjs", ".cjs", ".gjs"
            ]
        }
    },

    "elasticsearch": {
        # --- LINGUISTIC OVERRIDES ---
        "plaintext": {
            # Injects JSON REST API specs and YAML integration tests into the parsable surface area
            "extensions": [
                ".txt", ".text", ".log", ".json", ".yaml", ".yml"
            ]
        }
    },
    "exiftool": {
        "plaintext": {
            # Rescues ExifTool's gold-standard test outputs and config formats from Dark Matter
            "extensions": [
                ".txt", ".text", ".out", ".args", ".fmt", ".xmp"
            ]
        }
    },
    "express": {
        "html": {
            # Rescues Express view templates used in tests/examples
            "extensions": [
                ".html", ".htm", ".ejs", ".tmpl"
            ]
        }
    },
    "fieldtrip": {
        # --- 1. SHIELD/APERTURE OVERRIDES ---
        "_shield_": {
            "exclude_dirs": [
                "external" # Hard-blocks vendored third-party toolboxes (EEGLAB, SPM, etc.)
            ]
        }
    },
    "jenkins": {
        # --- 1. SHIELD/APERTURE OVERRIDES ---
        "_shield_": {
            # Banish the translation tooling scripts to Dark Matter so they 
            # don't falsely dominate the core Java architectural risk rankings.
            "exclude_paths": [
                "translation-tool.pl",
                "core/report-l10n.rb"
            ]
        }
    },
}