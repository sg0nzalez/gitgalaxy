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
analysis_lens.py
Phase 4+: The Laws of Physics, Threat Policies, and Mathematical Constants.

This file contains the immutable mathematical constants, security thresholds, 
and spatial modifiers used by the Signal Processor to calculate risk exposures 
and physical mass.
"""

# ------------------------------------------------------------------------------
# 1. SECURITY & THREAT POLICIES
# Consumed by: galaxyscope.py, security_lens.py, security_auditor.py
# ------------------------------------------------------------------------------

# The confidence threshold required to flag an artifact as Confirmed Malware.
# Tuned to 90.0% based on the 1.4M global probability distribution analysis.
AI_THREAT_THRESHOLD = 90.0

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


# ------------------------------------------------------------------------------
# 2. CORE PHYSICS CONSTANTS
# Consumed by: signal_processor.py
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


# ------------------------------------------------------------------------------
# 3. STRUCTURAL ASSET MASKS
# Consumed by: signal_processor.py
# ------------------------------------------------------------------------------
PHYSICS_ASSET_MASKS = {
    # Files strictly treated as literature (Bypasses active logic math)
    "DOCUMENTATION_LANGUAGES": {"plaintext", "markdown", "restructuredtext", "asciidoc", "org-mode", "tex", "latex"},

    # ==============================================================================
    # FILES EXCLUDED FROM UNIT TEST EXPOSURE (The "Cannot Be Tested" Mask)
    # RATIONALE: We do not penalize inert data, stylesheets, or documentation 
    # for lacking unit tests. Crucially, we also exclude test artifacts themselves 
    # (snapshots, mock data) to prevent the recursive trap of "testing the tester."
    # ==============================================================================
    "UNTESTABLE_EXTENSIONS": {
        # 1. UI, Styling & Markup (Declarative layout, no active logic)
        "css", "scss", "sass", "less", "html", "htm", "svg",
        
        # 2. Data & Configuration (Inert structures and environment settings)
        "json", "yaml", "yml", "toml", "ini", "cfg", "conf", "rc", "xml", "plist", "pbtxt",
        
        # 3. Documentation & Plaintext (Human-readable prose, tables, and logs)
        "md", "mdx", "txt", "text", "rst", "csv", "tsv", "log", "out", "err",
        
        # 4. Build, Infra & Schemas (Scaffolding and type definitions)
        "cmake", "mk", "make", "in", "ac", "m4", "patch", "diff", "sql", "proto", "graphql", "gql",
        
        # 5. Mainframe Inert Matter (Copybooks and Job Control definitions)
        "cpy", "jcl",
        
        # 6. TEST ARTIFACTS (The "Tester" Exclusions)
        # Prevents the engine from demanding test coverage on test outputs/snapshots.
        "snap", "tst", "cut"
    },
    
    "UNTESTABLE_NAMES": {
        'readme', 'license', 'manifest', 'version', 'manifest.uuid', 
        'authors', 'notice', 'copying', 'changelog', 'contributing',
        'configure', 'cmake-configure', 'makefile', 'gnumakefile', 
        'cmakelists.txt', 'kbuild', 'makeconf', 'makevars', 'gradlew',
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
# ------------------------------------------------------------------------------
# 4. ENVIRONMENTAL PHYSICS (Path Modifiers)
# Consumed by: signal_processor.py
# ------------------------------------------------------------------------------
PATH_MODIFIERS = {
    'Cognitive Load Exposure': [
        # 1. The Dictionary (Static Mapping)
        # Translation files, constants, and enums have massive line counts but almost 
        # zero logical complexity. Dampen them heavily so they don't look like giant risks.
        (re.compile(r'(?:^|/)(?:i18n|locales?|translations?|constants?|enums?)/', re.I), 0.80),

        # 2. The Abstraction (Declarations & Headers)
        # Expanded to catch C++ headers (.hpp, .hxx). These files outline structure 
        # without containing execution mass.
        (re.compile(r'\.(?:d\.ts|h|hpp|hxx|cpy)$', re.I), 0.85),

        # 3. The Config (Application Setup)
        # Expanded to catch environments and setup scripts. Usually highly declarative.
        (re.compile(r'(?:^|/)(?:configs?|settings|environments?|setup|makefile|\.env|cntl|jcl)\b', re.I), 0.70),
        
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
        (re.compile(r'(?:^|/)(?:types|interfaces|schemas|dtos|contracts|data|models|entities|pojos|copybooks?|cpy|copy)/|\.cpy$', re.I), 0.85),
        (re.compile(r'\.d\.ts$', re.I), 0.05), # Heavy dampen for pure type definitions
        
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
        (re.compile(r'(?:^|/)examples?/', re.I), 0.0),
        # Catch mainframe 8-char test prefixes (e.g., lgtestp1.cbl)
        (re.compile(r'(?:^|/)[a-z]{0,2}test[a-z0-9]*\.(?:cbl|cob)$', re.I), 0.0),
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
        (re.compile(r'\.css$|\.scss$|\.d\.ts$|\.types\.ts$|/types\.ts$|params?\.ts$|schema\.ts$|\.cpy$|\.bms$', re.I), 0.05),
        
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
# 5. RISK EQUATION TUNING (Sigmoid Curves & Scaling)
# Consumed by: signal_processor.py
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
        "loc_padding": 25,          # Override the massive 150 padding in the processor
        "irc_mult": 0.1, 
        "threshold_base": 2.5,      # Lowered from 4.0
        "sigmoid_slope": 0.8        # Steeper slope to accelerate the score once crossed
    },
    "state_flux": {
        "irc_mult": 0.15, 
        "threshold_base": 6.0,      # Lowered from 15.0 (6% mutation density is much more realistic)
        "sigmoid_slope": 0.40       # Increased from 0.20 to stretch the curve
    },
    # ---> DECOUPLED SECURITY EQUATION TUNING <---
    "obscured_payload": {
        "loc_padding": 500, # Raised from 150. Dilutes the density of massive framework files.
        "std_threshold": 35.0, "std_slope": 0.6, 
        "paranoid_threshold": 2.0, "paranoid_slope": 1.5
    },
    "logic_bomb": {
        "loc_padding": 500, # Raised from 150.
        "std_threshold": 90.0, "std_slope": 0.2,
        "paranoid_threshold": 10.0, "paranoid_slope": 0.5
    },
    "injection_surface": {
        "loc_padding": 500, # Raised from 150.
        "std_threshold": 60.0, "std_slope": 0.4,
        "paranoid_threshold": 3.0, "paranoid_slope": 1.2
    },
    "memory_corruption": {
        "loc_padding": 150,
        # Raised threshold from 25.0 -> 40.0 to forgive standard C/Rust pointer math
        "std_threshold": 40.0, "std_slope": 0.4,
        "paranoid_threshold": 4.0, "paranoid_slope": 0.8
    },
    "secrets_risk": {
        "loc_padding": 50,
        # Left extremely sensitive. Hardcoded secrets are never "noise."
        "std_threshold": 3.0, "std_slope": 1.0,
        "paranoid_threshold": 0.5, "paranoid_slope": 2.0
    }
}

# ------------------------------------------------------------------------------
# 6. DOMAIN ONTOLOGIES (Security Profiles & Alien Entity Rules)
# Consumed by: signal_processor.py
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
    },
    # Aggressive penalties applied when the file is an ALIEN in its neighborhood
    "ALIEN_WEIGHTS": {
        "systems_in_web": {"memory": 5.0, "logic_bomb": 3.0}, 
        "infra_in_web":   {"logic_bomb": 4.0},                
        "web_in_systems": {"flux": 3.0}                       
    },

    # ---> THE ARCHETYPE VIOLATION MATRIX (k=10 Edition) <---
    # Multiplies threat mass based on how anomalous the behavior is for the file's physical DNA.
    "ARCHETYPE_VIOLATION_MATRIX": {
        "Cluster 1: High-Dependency Config & Object Nodes": { 
            # The New Config/JSON/Typescript Interface nodes. 
            # These should NEVER execute logic, manage memory, or be obfuscated.
            "logic_bomb_multiplier": 25.0,        
            "injection_surface_multiplier": 20.0,
            "memory_corruption_multiplier": 20.0,
            "obscured_payload_multiplier": 10.0,
            "secrets_risk_multiplier": 2.0        
        },
        "Cluster 0: Native Memory & Systems Pointers": { 
            # Heavy C/C++. Memory manipulation is literally their job.
            "memory_corruption_multiplier": 0.1, 
            "logic_bomb_multiplier": 1.0,
            "injection_surface_multiplier": 1.5
        },
        "Cluster 3: Low-Level Bitwise Systems Core": { 
            # Rust/C Core. Bitwise operations are fine, but they shouldn't be dropping OS shells.
            "memory_corruption_multiplier": 0.05, 
            "logic_bomb_multiplier": 5.0,        
            "injection_surface_multiplier": 2.5
        },
        "Cluster 2: Asynchronous & Concurrent Orchestrators": { 
            # Python/TS Async logic. 
            "logic_bomb_multiplier": 8.0,
            "memory_corruption_multiplier": 5.0,
            "injection_surface_multiplier": 0.8   
        },
        "Cluster 6: Immutable State & Closure Logic": { 
            # UI Frameworks / React / View Layers. 
            # Frontend views shouldn't trigger OS/eval commands or touch memory.
            "memory_corruption_multiplier": 10.0, 
            "logic_bomb_multiplier": 10.0,       
            "injection_surface_multiplier": 1.5   
        },
        "Cluster 7: Exception Handling & Defensive Wrappers": { 
            # Try/Catch heavy logic. Malware loves to hide payloads in exception handlers.
            "logic_bomb_multiplier": 15.0,
            "obscured_payload_multiplier": 5.0,
            "memory_corruption_multiplier": 2.0
        },
        "Cluster 4: Complex Encapsulated OOP Logic": { 
            # Standard Object-Oriented Services.
            "memory_corruption_multiplier": 2.0,
            "injection_surface_multiplier": 1.0   
        },
        "Cluster 5: Async Closures & Memory Allocation": { 
            # JS/TS node allocating memory.
            "memory_corruption_multiplier": 0.5, # Expected behavior
            "logic_bomb_multiplier": 5.0,
            "injection_surface_multiplier": 1.0
        },
        "Cluster 8: Downstream Execution Triggers": { 
            # The New "God Nodes" (Extreme direct downstream). 
            # Massive blast radius if an injection surface or logic bomb is placed here.
            "logic_bomb_multiplier": 5.0,        
            "injection_surface_multiplier": 3.0,
            "obscured_payload_multiplier": 8.0
        }
    },
    
    # ---> THE BASELINE SPATIAL DISPERSIONS (Z-Score baselines) <---
    "ARCHETYPE_DISPERSIONS": {
        "Cluster 0: Native Core & Memory Management": 4.58,
        "Cluster 1: Object-Oriented Services & Typed Abstractions": 4.92,
        "Cluster 2: Declarative Definitions & Data Models": 2.87,
        "Cluster 3: C-Headers & Preprocessor Macros": 5.38,
        "Cluster 4: High-Complexity Closures & Orchestration": 4.86,
        "Cluster 5: Universal Dependencies (The God Nodes)": 4.99,
        "Cluster 6: UI Frameworks & View Layers": 4.61,
        "Cluster 7: Async Logic & Concurrency Orchestration": 6.25,
        "Cluster 8: Test Suites & Mock Environments": 6.53,
        "Cluster 9: I/O Boundaries & Scripting Automation": 4.50
    }
}




# ------------------------------------------------------------------------------
# 7. RECORDING SCHEMAS & UI MAPPINGS
# Consumed by: gpu_recorder.py, audit_recorder.py, llm_recorder.py, detector.py
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
        "indent_tabs", "indent_spaces", "hardware_bridge", "cryptography",
        
        # --- NEW: DOMAIN INTENT SENSORS ---
        "auth_middleware", "ipc_rpc_bridges", "feature_flags", "serialization_parsing", 
        "regex_execution", "time_date_logic",
        
        # --- NEW: LINGUISTIC & SLOP SENSORS ---
        "core_var_decl", "design_camel_case", "design_snake_case", "design_pascal_case", 
        "design_upper_case", "design_short_vars", "design_long_vars", 
        "design_slop_duplicates", "design_slop_orphans",

        # --- NEW: PASSIVE SECURITY LENS OBSERVERS ---
        "sec_heat_triggers", "sec_safety_neg", "sec_io", "sec_danger", 
        "sec_flux", "sec_graveyard", "sec_bitwise_hits", "sec_shadow_imports",
        "sec_homoglyphs", "sec_private_info", "sec_extension_mismatch", "sec_entropy",
        "sec_tainted_injection"
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
        "logic_bomb": "Destructive Execution Surface",
        "injection_surface": "Weaponizable Injection Vectors",
        "memory_corruption": "Weaponizable Memory Operations",
        "secrets_risk": "Hardcoded Credential Exposure"
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
        "injection_surface": "Weaponizable Injection Vectors",
        "memory_corruption": "Raw Memory Manipulation",
        "secrets_risk": "Hardcoded Payload Artifacts"
    }
}

# ------------------------------------------------------------------------------
# 8. Machine Learning Inference Models
# Consumed by: detector.py, signal_processor.py, security_auditor.py
# ------------------------------------------------------------------------------

# Function Archetypes (K-means Clusters) 
GENERAL_FUNCTION_INFERENCE_MODEL = {
    'SCALER_MEDIANS': [2.398, 0.693, 1.099, 1.5, 0.087, 2.272, 3.005, 2.603, 2.603, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.929, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.312, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    'SCALER_IQRS': [1.344, 1.609, 0.693, 0.895, 0.208, 3.082, 1.303, 2.037, 1.466, 1.0, 1.0, 1.0, 1.0, 1.0, 2.872, 3.172, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 3.387, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.792, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 3.045, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    'ARCHETYPES_K12': {
        'Cluster 0: Modern Systems & Typed Interfaces': [-0.151, -0.093, -0.153, 0.183, 0.055, -0.285, -0.179, -0.194, 0.081, 0.039, 0.003, 0.094, 0.014, 0.043, 0.296, -0.047, 0.0, 0.042, 0.066, 0.044, 0.077, 0.305, 0.051, 0.073, 0.038, 0.034, 0.03, 0.008, 0.004, 0.006, 0.0, 0.0, 0.001, 0.009, 0.014, 0.037, 0.539, 0.108, 0.001, 0.005, 0.027, 0.015, 0.117, 0.002, 0.084, 0.011, 3.067, 0.029, 0.293, 0.015, 0.003, 0.0, 0.0, 0.001, 0.001, 0.003, 0.019, 0.002, 0.005, -0.246, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'Cluster 1: I/O, UI & Scripting Automation': [0.435, 0.226, 0.253, 0.458, 0.111, -0.104, 0.27, -0.364, -0.447, 2.31, 0.098, 0.071, 0.003, 0.066, 1.02, 0.245, 0.0, 0.016, 0.015, 0.0, 0.006, 0.288, 0.016, 0.008, 0.001, 0.012, 0.112, 0.011, 0.003, 0.002, 0.0, 0.0, 0.0, 0.004, 0.012, 0.044, 1.09, 0.041, 0.001, 0.002, 0.021, 0.052, 0.027, 0.002, 0.26, 0.009, 0.269, 0.027, 0.781, 0.015, 0.0, 0.0, 0.0, 0.0, 0.0, 0.005, 0.001, -0.0, 0.0, 0.109, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'Cluster 2: Declarative Definitions & Data Structures': [1.096, 1.088, -0.019, -0.166, 0.845, 0.279, -0.596, -0.604, -0.909, 0.249, 0.215, 0.14, 0.028, 0.144, 0.524, 0.223, 0.001, 0.059, 0.028, 0.016, 0.058, 0.43, 0.02, 0.046, 0.04, 0.036, 0.228, 0.013, 0.004, 0.006, 0.0, 0.0, 0.002, 0.013, 0.005, 0.174, 0.667, 0.116, 0.004, 0.015, 0.102, 0.258, 0.138, 0.005, 0.398, 0.019, 0.358, 0.077, 0.382, 0.025, 0.001, 0.0, 0.0, 0.001, 0.001, 0.007, 0.017, 0.002, 0.006, 0.078, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'Cluster 3: Raw Pointer & Memory Manipulation': [-0.388, -0.261, 0.23, 0.109, -0.115, -0.455, 0.314, 0.313, 0.324, 0.01, 0.001, 0.003, 0.005, 0.061, 0.549, -0.272, 0.0, 0.064, 0.075, 0.014, 0.002, 0.088, 0.015, 0.003, 0.027, 0.019, 0.023, 0.016, 0.003, 0.002, 0.0, 0.0, 0.002, 0.007, 0.004, 0.017, 0.341, 0.055, 0.005, 0.006, 0.024, 0.002, 0.083, 0.003, 0.089, 0.021, 0.001, 0.043, 0.655, 0.02, 0.006, -0.0, 0.0, 0.001, 0.0, 0.005, 0.013, 0.001, 0.005, -0.397, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'Cluster 4: Object-Oriented Services & Testing': [0.472, 0.584, 0.125, 0.351, 0.747, 0.16, -0.494, -0.152, -0.309, 0.052, 2.387, 0.472, 0.028, 0.137, 0.266, -0.07, 0.0, 0.106, 0.348, 0.207, 0.496, 0.598, 0.063, 0.41, 0.237, 0.047, 0.086, 0.015, 0.009, 0.001, 0.0, 0.0, 0.002, 0.032, 0.044, 0.032, 0.324, 0.257, 0.001, 0.018, 0.051, 0.205, 0.567, 0.013, 0.369, 0.023, 2.645, 0.141, 0.477, 0.045, 0.005, -0.0, 0.0, 0.002, 0.004, 0.005, 0.059, 0.004, 0.009, 0.043, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'Cluster 5: High-Dependency C Headers': [0.005, -0.066, 0.072, 0.455, 0.077, -0.306, -0.148, 0.482, 0.296, 0.073, 0.285, 0.221, 0.021, 0.112, 0.134, -0.315, -0.0, 0.466, 0.398, 0.252, 2.898, 0.181, 0.08, 0.361, 0.421, 0.02, 0.099, 0.042, 0.007, 0.002, 0.0, 0.0, 0.005, 0.058, 0.045, 0.005, 0.026, 0.135, -0.0, 0.015, 0.07, 0.069, 0.127, 0.033, 0.063, 0.013, 0.584, 0.084, 0.331, 0.07, 0.014, -0.0, 0.0, 0.004, 0.003, 0.003, 0.045, 0.003, 0.012, -0.134, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'Cluster 6: Async Logic & Concurrency Orchestration': [0.034, 0.069, -0.048, 0.325, 0.164, -0.167, -0.197, -0.095, -0.103, 0.025, 0.353, 0.142, 0.023, 0.041, 0.145, 0.125, 0.0, 0.054, 0.015, 0.011, 0.077, 0.326, 0.036, 0.068, 0.024, 0.03, 0.053, 0.007, 0.003, 0.013, 0.0, 0.0, 0.001, 0.019, 0.003, 0.068, 0.592, 0.101, 0.001, 0.003, 0.064, 2.975, 0.054, 0.002, 0.1, 0.02, 1.336, 0.033, 0.206, 0.023, 0.0, -0.0, 0.0, 0.001, 0.001, 0.001, 0.011, 0.001, 0.004, -0.176, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'Cluster 7: Documented Core Interfaces': [-0.198, -0.149, 0.253, 0.438, 0.047, -0.338, -0.09, 0.294, 0.261, 0.109, 0.223, 0.343, 0.006, 0.079, 0.538, -0.366, 0.001, 0.134, 0.367, 0.283, 0.19, 0.03, 0.087, 3.159, 0.149, 0.018, 0.042, 0.03, 0.012, 0.003, 0.0, 0.0, 0.004, 0.012, 0.01, 0.005, 0.105, 0.044, -0.0, 0.008, 0.021, 0.13, 0.166, 0.004, 0.257, 0.024, 0.349, 0.014, 0.575, 0.036, 0.007, -0.0, 0.0, 0.003, 0.002, 0.003, 0.026, 0.002, 0.02, -0.254, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'Cluster 8: Universal Dependencies (The God Nodes)': [0.043, 0.281, 0.014, 0.5, 0.766, 0.072, -0.175, 0.14, -0.134, 0.022, 1.036, 2.958, 0.035, 0.361, 0.328, -0.233, 0.001, 0.126, 0.122, 0.056, 0.274, 0.131, 0.048, 0.238, 0.096, 0.05, 0.223, 0.02, 0.003, 0.001, 0.0, 0.0, 0.002, 0.025, 0.022, 0.017, 0.115, 0.09, 0.0, 0.032, 0.148, 0.358, 0.304, 0.025, 0.058, 0.029, 0.114, 0.141, 0.369, 0.051, 0.007, -0.0, 0.0, 0.002, 0.003, 0.004, 0.033, 0.003, 0.009, -0.114, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'Cluster 9: Functional OOP & Async Logic': [0.101, 0.006, -1.547, -0.346, 0.015, -0.251, -0.229, -1.224, -0.204, 0.07, 0.078, 0.112, 0.011, 0.057, 0.611, -0.025, 0.001, 0.038, 0.013, 0.002, 0.002, 0.603, 0.005, 0.003, 0.001, 0.026, 0.032, 0.002, 0.021, 0.045, 0.0, 0.0, 0.0, 0.005, 0.003, 0.081, 0.679, 0.062, 0.005, 0.003, 0.041, 0.083, 0.046, 0.004, 0.207, 0.019, 0.112, 0.059, 0.444, 0.013, 0.0, 0.0, 0.0, 0.0, 0.001, 0.002, 0.004, -0.0, 0.004, -0.202, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'Cluster 10: Object-Oriented Structures': [0.049, 0.218, 0.143, 0.173, 0.523, 0.019, -0.506, 0.008, -0.037, 0.031, 2.959, 0.106, 0.016, 0.112, 0.339, -0.188, 0.001, 0.16, 0.222, 0.042, 0.285, 0.087, 0.047, 0.563, 0.143, 0.019, 0.093, 0.036, 0.011, 0.002, 0.0, 0.0, 0.003, 0.018, 0.01, 0.018, 0.287, 0.119, 0.001, 0.021, 0.045, 0.157, 0.277, 0.008, 0.169, 0.053, 0.008, 0.115, 0.638, 0.021, 0.001, 0.0, 0.0, 0.003, 0.003, 0.004, 0.038, 0.001, 0.01, -0.275, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'Cluster 11: Algorithmic & Defensive Logic': [-0.246, -0.294, -0.292, -0.627, -0.183, -0.529, -2.22, -0.072, 0.161, 0.044, 0.035, 0.047, 0.016, 0.096, 0.227, -0.379, 0.0, 0.073, 0.038, 0.04, 0.036, 0.034, 0.043, 0.046, 0.022, 0.026, 0.064, 0.004, 0.011, 0.003, 0.0, 0.0, 0.004, 0.012, 0.013, 0.017, 0.167, 0.063, 0.002, 0.008, 0.061, 0.022, 0.152, 0.003, 0.127, 0.015, 0.056, 0.065, 0.261, 0.016, 0.001, -0.0, 0.0, 0.0, 0.001, 0.003, 0.015, 0.0, 0.004, -0.462, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    }
}

# General File Archetypes (K-means Clusters)
GENERAL_FILE_INFERENCE_MODEL = {
    'SCALER_MEDIANS': [4.127, 3.129, 2.139, 0.0, 0.0, 0.223, 2.14, 0.357, 0.693, 1.099, 0.0, 0.04, 0.109, 0.693, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.8, 0.328, 0.0, 0.0, 0.0, 1.52, 1.543, 0.2, 0.0, 3.078, 2.085, 0.0, 4.762, 2.889, 0.0, 0.0, 0.0, 5.106, 0.0, 0.0, 3.819, 4.503, 0.0, 0.0, 0.0, 0.0, 0.0, 2.151, 3.083, 2.082, 1.792, 0.2, 0.0, 0.0, 0.0, 0.0, 1.394, 1.466, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.501, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.603, 0.0, 0.452, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.751, 0.0, 0.0, 0.0, 0.0],
    'SCALER_IQRS': [1.889, 4.318, 3.103, 1.0, 1.0, 0.405, 3.045, 1.331, 2.079, 1.299, 0.446, 0.153, 0.569, 1.0, 1.0, 1.0, 1.0, 9.524, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.208, 0.719, 1.0, 1.0, 1.253, 2.354, 2.139, 1.441, 1.0, 1.811, 3.826, 1.29, 1.893, 4.494, 1.0, 2.028, 1.0, 1.908, 1.0, 1.0, 2.649, 5.572, 1.0, 1.0, 1.0, 1.0, 1.0, 2.949, 1.242, 2.272, 2.278, 1.441, 1.388, 0.432, 1.0, 1.0, 2.616, 2.978, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.778, 0.714, 1.0, 1.0, 1.0, 2.232, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.216, 2.086, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.008, 1.0, 1.558, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.821, 1.0, 1.52, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.231, 1.0, 1.0, 1.0, 1.0],
    'ARCHETYPES_K24': {
        'File Macro-Species 0: Java/JS Mixed Business Logic': [-0.01, 0.289, 0.315, 5.659, 0.0, 0.157, 0.163, 0.542, 0.44, -0.024, 0.648, 0.709, 0.443, -0.012, 0.558, 0.086, 1.317, 1.108, 0.656, 1.241, 0.549, 3.694, 70.293, 0.522, 1.594, 8.934, -0.211, 0.485, 0.178, 0.136, 0.494, 0.068, 0.224, 0.297, 0.0, 0.101, 0.69, 0.761, -0.023, -0.065, 0.361, 0.437, 0.179, 0.01, 0.272, 0.559, -0.297, -0.108, 0.002, 0.05, 0.007, 0.002, 0.004, 0.126, 0.176, 0.253, 0.192, 0.297, 0.758, 5.861, 0.05, 0.525, -0.035, -0.009, 0.066, 0.344, 0.353, 0.095, 0.44, 0.129, 0.96, 0.835, 0.161, 0.094, 0.413, 0.095, 0.086, 0.02, 0.001, 0.0, 0.009, 0.037, 0.04, 0.34, 0.091, 0.11, 0.002, 0.05, 0.189, 0.309, 0.325, 0.026, 0.129, 0.058, 0.31, 0.158, 0.666, 0.09, 0.022, 0.001, 0.002, 0.006, 0.044, 0.005, 0.074, 0.012, 0.034, -0.009, 0.0, 0.451, 0.022, 0.0, 0.03, 0.247, 0.007, 0.171, 0.0, 0.0, 0.053, 0.001, 0.0, 0.002, 0.001],
        'File Macro-Species 1: Modern Polyglot Backend': [0.103, 0.203, 0.148, 4.512, 0.0, 0.108, 0.052, 0.169, 0.237, -0.013, 0.767, 0.286, 0.433, -0.024, 5.838, 0.936, 2.583, 1.853, 2.03, 1.939, 2.119, 6.541, 2.678, 3.04, 6.648, 48.003, -0.339, 0.153, 0.302, 0.181, 0.438, -0.018, 0.289, 0.492, 0.0, -0.156, 0.117, 1.552, -0.125, -0.077, 0.347, 0.484, 0.198, -0.101, 0.306, 0.739, -0.152, -0.074, 0.005, 0.073, 0.004, 0.004, 0.001, -0.107, -0.314, 0.201, 0.266, 0.492, 0.548, 0.971, 0.03, 0.282, -0.046, -0.009, 0.084, 0.211, 0.312, 0.258, 0.386, 0.233, 1.022, 1.211, 0.167, 0.079, 0.26, 0.006, 0.082, 0.027, 0.001, 0.0, 0.009, 0.049, 0.073, 0.678, 0.298, 0.212, 0.003, 0.014, 0.114, 0.286, 0.288, 0.021, 0.257, 0.055, 0.574, 0.134, 0.655, 0.081, 0.006, 0.0, 0.0, 0.004, 0.019, 0.008, 0.071, 0.002, 0.025, -0.18, 0.0, 0.509, 0.066, 0.0, 0.023, 0.267, 0.005, 0.062, 0.0, 0.004, -0.092, 0.0, 0.0, 0.008, 0.0],
        'File Macro-Species 2: Frontend UI Components': [0.268, 0.382, 0.316, 9.998, 0.001, 0.058, 0.142, 0.385, 0.426, 0.046, 0.846, 0.496, 0.543, -0.026, 4.503, 0.291, 1.547, 1.446, 7.082, 46.056, 0.82, 6.37, 4.423, 0.291, 5.19, 9.658, -0.346, 0.107, 0.34, 0.199, 0.529, 0.107, 0.175, 0.233, 0.0, -0.223, 0.153, 0.998, -0.323, -0.058, 0.707, 0.306, 0.304, -0.259, 0.341, 0.873, -0.093, -0.089, 0.013, 0.091, 0.011, 0.001, 0.002, 0.013, 0.133, 0.481, 0.32, 0.233, 0.744, 1.503, 0.024, 0.273, -0.093, -0.056, 0.104, 0.475, 0.69, 0.633, 2.016, 0.316, 1.222, 1.386, 0.52, 0.056, 0.234, 0.137, 0.074, 0.015, 0.001, 0.0, 0.01, 0.097, 0.101, 0.141, 0.039, 0.231, 0.0, 0.035, 0.104, 0.228, 0.207, 0.043, 0.169, 0.037, 0.777, 0.152, 0.566, 0.155, 0.04, 0.0, 0.001, 0.007, 0.039, 0.009, 0.121, 0.008, 0.042, 0.022, 0.0, 0.303, 0.045, 0.0, 0.075, 0.251, 0.054, 0.021, -0.0, 0.0, 0.135, 0.0, 0.0, 0.002, 0.001],
        'File Macro-Species 3: Safe Systems & Infrastructure': [-0.088, 0.158, 0.299, 7.081, 0.0, 0.166, 0.193, 0.611, 0.373, 0.104, 0.382, 0.739, 0.4, -0.022, 0.093, 0.034, 0.518, 0.194, 0.41, 0.332, 0.134, 0.614, 0.234, 0.062, 94.841, 0.882, -0.246, 0.434, 0.343, 0.229, 0.443, 0.066, 0.107, 0.393, 0.0, 0.044, 0.034, 0.888, 0.062, -0.043, 0.445, 0.596, 0.371, 0.082, 0.389, 0.833, -0.096, -0.043, 0.002, 0.056, 0.003, 0.004, 0.002, 0.083, 0.002, 0.082, 0.102, 0.393, 1.881, 0.603, 0.002, 0.204, -0.001, -0.045, 0.146, 0.257, 0.41, 0.09, 0.416, 0.16, 0.827, 1.311, 0.214, 0.056, 0.152, 0.014, 0.097, 0.031, 0.001, 0.0, 0.01, 0.029, 0.041, 0.493, 0.385, 0.173, 0.001, 0.026, 0.107, 0.216, 0.269, 0.014, 0.233, 0.061, 0.218, 0.1, 0.858, 0.031, 0.012, 0.001, 0.001, 0.007, 0.016, 0.004, 0.103, 0.003, 0.023, -0.288, 0.0, 0.45, 0.07, 0.0, 0.029, 0.335, 0.002, 0.055, -0.0, 0.0, -0.25, 0.0, 0.0, 0.002, 0.001],
        'File Macro-Species 4: C/C++ Heavy Native Core': [0.79, 0.193, 0.158, 1.559, 0.0, 0.496, 0.344, 0.904, 0.959, -0.483, 0.976, 0.72, 0.039, -0.064, 5.044, 1.69, 24.412, 1.082, 1.336, 0.155, 3.722, 0.688, 1.221, 46.924, 1.351, 3.152, -0.118, -0.047, 0.143, 0.062, 0.184, -0.119, 0.041, 0.123, 0.0, -0.25, -0.033, 1.029, -0.636, -0.095, 0.059, 0.7, 0.229, -0.764, 0.147, 0.333, -0.352, -0.436, 0.001, 0.044, 0.001, 0.212, 0.0, 0.193, -0.413, -0.45, -0.062, 0.123, 0.305, 0.788, 0.048, 0.204, 0.224, 0.477, 0.089, 0.101, 0.065, 0.008, 0.04, 0.906, 0.047, 0.107, 0.018, 0.062, 0.426, -0.116, 0.069, 0.079, 0.002, 0.0, 0.002, 0.019, 0.014, 3.981, 1.356, 0.123, 0.013, 0.017, 0.156, 0.574, 0.135, 0.014, 0.555, 0.05, 0.374, 0.154, 0.529, 0.064, 0.003, 0.0, 0.0, 0.001, 0.003, 0.007, 0.014, 0.0, 0.008, 0.05, 0.0, 0.316, 0.011, 0.0, 0.003, 0.262, 0.0, 0.021, 0.0, 0.0, -0.113, 0.0, 0.0, 0.001, 0.0],
        'File Macro-Species 5: Async UI Controllers': [-0.19, 0.664, 0.891, 70.34, -0.0, 0.062, 0.059, 0.232, 0.124, 0.07, 0.446, 0.495, 0.815, -0.027, 2.511, 0.11, 0.511, 0.357, 3.803, 3.655, 0.522, 74.984, 1.837, 0.124, 4.358, 4.183, -0.601, 0.564, 0.318, 0.256, 0.716, 0.194, 0.207, 0.635, 0.0, 0.205, 0.106, 0.915, 0.092, 0.074, 1.082, 0.305, 0.192, 0.181, 0.422, 0.893, 0.016, 0.051, 0.008, 0.039, 0.01, 0.0, 0.001, -0.084, -0.26, 0.27, 0.301, 0.635, 0.659, 1.62, 0.017, 0.3, 0.058, -0.22, 0.079, 0.34, 0.974, 0.934, 0.772, 0.218, 1.32, 4.111, 0.355, 0.05, 0.364, 0.225, 0.147, 0.008, 0.001, 0.0, 0.025, 0.092, 0.202, 0.376, 0.11, 0.197, -0.0, 0.017, 0.085, 0.416, 0.521, 0.042, 0.541, 0.055, 0.819, 0.084, 0.616, 0.119, 0.035, 0.0, 0.002, 0.008, 0.08, 0.007, 0.116, 0.007, 0.046, -0.195, 0.0, 0.404, 0.065, -0.0, 0.065, 0.249, 0.002, 0.033, -0.0, 0.001, 0.142, 0.0, 0.0, 0.002, 0.003],
        'File Macro-Species 6: C/C++ Mixed Bindings': [0.747, 0.207, 0.2, 2.064, 0.003, 0.574, 0.436, 1.225, 1.136, 0.033, 0.953, 1.018, -0.05, -0.029, 3.624, 2.7, 46.586, 2.282, 1.935, 0.98, 5.575, 1.406, 2.209, 4.742, 2.131, 6.382, -0.064, -0.017, 0.259, 0.096, 0.177, -0.097, -0.035, 0.203, 0.0, -0.231, 0.021, 1.023, -0.646, -0.177, 0.133, 0.652, 0.316, -0.723, 0.168, 0.481, -0.371, -0.416, 0.002, 0.111, 0.002, 0.107, 0.002, 0.315, -0.307, -0.117, -0.089, 0.203, 0.377, 0.768, 0.069, 0.357, 0.032, 0.394, 0.133, 0.155, 0.129, 0.047, 0.183, 0.488, 0.223, 0.223, 0.129, 0.099, 0.331, -0.11, 0.082, 0.067, 0.001, 0.0, 0.009, 0.028, 0.021, 2.306, 0.906, 0.16, 0.008, 0.03, 0.262, 0.621, 0.27, 0.016, 0.479, 0.042, 0.331, 0.159, 0.718, 0.061, 0.005, 0.001, 0.002, 0.003, 0.008, 0.009, 0.064, 0.013, 0.025, 0.14, 0.0, 0.204, 0.031, 0.0, 0.014, 0.216, 0.001, 0.044, 0.0, 0.001, -0.098, 0.0, 0.0, 0.002, 0.0],
        'File Macro-Species 7: Strongly-Typed App Logic': [-0.239, -0.054, 0.041, 1.267, 0.0, -0.009, 0.032, -0.083, -0.153, -0.202, 0.211, -0.001, 0.497, -0.03, 0.229, 0.02, 0.234, 0.038, 0.131, 0.171, 0.073, 0.198, 0.12, 0.2, 0.255, 98.012, -0.763, 0.344, 0.165, 0.151, 0.518, -0.137, 0.19, 0.5, 0.0, -0.025, -0.062, 1.222, 0.191, -0.126, 0.155, 0.335, 0.278, 0.224, 0.302, 0.572, 0.088, 0.02, 0.004, 0.014, 0.001, 0.002, 0.001, -0.337, -0.981, 0.006, 0.148, 0.5, 0.254, 0.67, 0.028, 0.249, -0.121, -0.19, 0.11, 0.209, 0.117, 0.28, 0.267, 0.192, 0.908, 0.662, 0.067, 0.062, 0.263, -0.125, 0.056, 0.02, 0.001, 0.0, 0.005, 0.026, 0.079, 0.772, 0.132, 0.1, 0.002, 0.019, 0.135, 0.104, 0.235, 0.012, 0.121, 0.03, 0.36, 0.092, 0.35, 0.045, 0.005, 0.0, 0.0, 0.002, 0.012, 0.002, 0.053, 0.002, 0.019, -0.419, 0.0, 0.357, 0.072, -0.0, 0.015, 0.191, 0.003, 0.094, -0.0, 0.002, -0.195, 0.0, 0.0, 0.011, 0.0],
        'File Macro-Species 8: Scientific & Math Scripts': [0.235, 0.061, 0.307, 1.047, 0.001, 0.615, 0.665, 1.624, 0.972, 0.046, 0.201, 1.011, -0.042, -0.028, 0.198, 0.215, 97.558, 0.081, 0.085, 0.024, 0.191, 0.019, 0.072, 0.567, 0.132, 0.168, -0.172, 0.471, 0.153, 0.099, 0.19, -0.186, -0.225, 0.123, 0.0, 0.265, 0.177, 1.156, -0.142, -0.147, 0.102, 0.905, 0.509, -0.23, 0.171, 0.45, -0.199, -0.221, 0.005, 0.065, 0.001, 0.037, 0.002, 0.311, -0.456, -0.283, -0.203, 0.123, 0.398, 0.53, 0.059, 0.399, -0.068, 0.337, 0.209, 0.175, 0.095, 0.081, 0.239, 0.384, 0.232, 0.159, 0.13, 0.196, 0.244, -0.192, 0.054, 0.048, 0.001, 0.0, 0.014, 0.023, 0.016, 1.988, 0.554, 0.169, 0.005, 0.027, 0.272, 0.346, 0.279, 0.011, 0.401, 0.014, 0.218, 0.126, 0.374, 0.03, 0.007, 0.0, 0.001, 0.006, 0.007, 0.003, 0.076, 0.01, 0.014, 0.127, 0.0, 0.153, 0.025, 0.0, 0.016, 0.17, 0.001, 0.082, 0.0, 0.0, -0.133, 0.0, 0.0, 0.002, 0.0],
        'File Macro-Species 9: C++ Object-Oriented Systems': [0.503, 0.247, 0.149, 2.996, 0.001, 0.233, 0.135, 0.492, 0.632, -0.026, 0.975, 0.603, 0.3, -0.045, 44.482, 0.836, 9.717, 1.493, 4.197, 1.379, 8.972, 2.099, 1.436, 6.191, 1.978, 4.497, -0.249, 0.08, 0.239, 0.119, 0.521, 0.025, 0.229, 0.27, 0.0, -0.145, 0.106, 1.898, -0.43, -0.27, 0.189, 0.674, 0.267, -0.489, 0.212, 0.555, -0.271, -0.244, 0.003, 0.04, 0.002, 0.097, 0.0, 0.083, -0.099, 0.155, 0.167, 0.27, 0.435, 0.649, 0.041, 0.141, -0.16, 0.39, 0.105, 0.118, 0.201, 0.125, 0.258, 0.504, 0.368, 0.547, 0.107, 0.078, 0.268, 0.038, 0.099, 0.054, 0.003, 0.0, 0.001, 0.036, 0.035, 2.414, 0.908, 0.253, 0.005, 0.015, 0.084, 0.847, 0.154, 0.01, 0.353, 0.043, 1.191, 0.111, 0.33, 0.079, 0.006, 0.0, 0.0, 0.002, 0.03, 0.011, 0.066, 0.004, 0.022, -0.024, 0.0, 0.57, 0.015, 0.0, 0.022, 0.206, 0.003, 0.027, 0.0, 0.001, 0.045, 0.0, 0.0, 0.001, 0.0],
        'File Macro-Species 10: Universal Mixed Logic': [-0.141, -0.562, -0.548, 0.305, 0.0, -0.178, -0.478, -0.159, -0.197, -0.558, 0.164, -0.109, 0.688, -0.025, 0.231, 0.103, 0.388, 1.749, 0.113, 0.242, 0.282, 0.777, 0.814, 0.126, 0.343, 0.493, -0.244, 0.37, 0.142, 0.128, 0.918, -0.073, -0.377, 0.406, 0.0, -0.145, -0.066, 0.4, 0.149, -0.078, 0.158, 0.432, 0.208, 0.13, 0.248, 0.478, -0.02, -0.084, 0.004, 0.029, 0.002, 0.008, 0.002, -0.361, -0.539, -0.282, -0.361, 0.406, 0.298, 0.698, 0.015, 0.235, 0.019, -0.123, 0.084, 0.281, 0.139, 0.19, 0.185, 0.157, 0.66, 0.452, 0.062, 0.056, 0.356, -0.07, 0.044, 0.02, 0.001, 0.0, 0.011, 0.018, 0.029, 3.665, 0.308, 0.055, 0.003, 0.008, 0.061, 0.208, 0.078, 0.007, 0.197, 0.019, 0.342, 0.046, 0.339, 0.042, 0.019, 0.001, 0.001, 0.003, 0.017, 0.005, 0.074, 0.003, 0.025, -0.467, 0.0, 0.019, 0.037, 0.0, 0.01, 0.197, 0.002, 0.049, 0.0, 0.0, -0.081, 0.0, 0.0, 0.002, 0.0],
        'File Macro-Species 11: Frontend Testing & UI Frameworks': [-0.128, 0.181, 0.302, 2.074, 0.0, -0.197, 0.217, 0.167, 0.043, -0.027, 0.289, 0.119, 0.781, -0.031, 0.177, 0.012, 0.108, 0.037, 0.322, 97.938, 0.021, 0.138, 0.207, 0.002, 0.365, 0.352, -0.542, 0.316, 0.202, 0.201, 0.471, 0.007, 0.116, 0.197, 0.0, -0.043, -0.002, 0.778, 0.047, -0.146, 0.827, 0.228, 0.551, 0.121, 0.384, 0.783, 0.157, 0.03, 0.013, 0.027, 0.006, 0.0, 0.001, -0.264, 0.169, 0.479, 0.417, 0.197, 0.388, 0.751, 0.018, 0.196, -0.173, -0.198, 0.184, 0.847, 0.727, 0.528, 2.469, 0.306, 1.019, 0.763, 0.272, 0.024, 0.217, 0.024, 0.058, 0.006, 0.0, 0.0, 0.009, 0.084, 0.064, 0.051, 0.025, 0.185, 0.0, 0.008, 0.121, 0.098, 0.093, 0.021, 0.089, 0.018, 0.66, 0.072, 0.274, 0.095, 0.051, 0.0, 0.002, 0.006, 0.009, 0.005, 0.085, 0.003, 0.023, -0.166, 0.0, 0.34, 0.061, 0.0, 0.036, 0.219, 0.032, 0.024, -0.0, 0.0, 0.028, 0.0, 0.0, 0.002, 0.001],
        'File Macro-Species 12: High-Density Web Controllers': [0.503, 0.449, 0.392, 11.462, 0.004, 0.43, 0.257, 0.837, 0.83, 0.081, 0.931, 0.916, 0.131, -0.044, 12.466, 0.172, 3.143, 0.948, 43.11, 3.806, 1.927, 3.814, 3.163, 1.146, 8.67, 9.558, -0.357, 0.102, 0.648, 0.288, 0.565, 0.032, 0.09, 0.22, 0.0, -0.165, 0.11, 1.279, -0.505, -0.1, 0.762, 0.424, 0.249, -0.491, 0.372, 1.119, -0.201, -0.24, 0.002, 0.115, 0.008, 0.025, 0.001, 0.234, -0.262, 0.165, 0.137, 0.22, 1.42, 1.518, 0.016, 0.32, -0.099, 0.139, 0.092, 0.126, 0.912, 0.532, 0.794, 0.594, 0.718, 1.173, 0.44, 0.08, 0.237, 0.046, 0.114, 0.022, 0.002, 0.0, 0.007, 0.092, 0.15, 0.75, 0.289, 0.43, 0.002, 0.044, 0.087, 0.387, 0.578, 0.03, 0.429, 0.04, 1.247, 0.3, 0.639, 0.121, 0.014, 0.0, 0.001, 0.006, 0.021, 0.013, 0.152, 0.01, 0.029, 0.091, 0.0, 0.256, 0.029, 0.0, 0.086, 0.228, 0.009, 0.022, -0.0, 0.0, 0.153, 0.0, 0.0, 0.001, 0.001],
        'File Macro-Species 13: Pure C Core Libraries': [0.408, 0.014, 0.072, 0.821, -0.0, 0.035, 0.298, 0.609, 0.573, 0.135, 0.66, 0.454, 0.24, -0.017, 1.017, 87.76, 3.845, 0.641, 0.19, 0.041, 0.115, 0.029, 0.062, 0.599, 0.177, 0.064, 0.04, 0.197, 0.038, 0.048, 0.229, -0.061, 0.048, 1.419, 0.0, 0.042, 0.069, 0.481, -0.276, 0.135, 0.039, 0.787, 0.091, -0.397, 0.107, 0.278, -0.096, -0.586, 0.001, 0.013, 0.0, 0.097, 0.0, 0.014, 0.189, -0.11, 0.004, 1.419, 0.139, 0.282, 0.015, 0.233, 0.487, 0.44, 0.033, 0.068, 0.041, 0.012, 0.059, 0.398, 0.148, 0.052, 0.012, 0.026, 0.447, -0.05, 0.031, 0.024, 0.0, 0.0, 0.006, 0.015, 0.119, 3.211, 1.455, 0.052, 0.004, 0.004, 0.037, 0.09, 0.078, 0.006, 0.475, 0.011, 0.375, 0.033, 0.846, 0.034, 0.003, 0.0, 0.0, 0.002, 0.007, 0.024, 0.011, 0.001, 0.003, 0.124, 0.0, 0.159, 0.022, 0.0, 0.006, 0.098, 0.0, 0.064, -0.0, 0.0, -0.103, -0.0, 0.0, 0.0, 0.0],
        'File Macro-Species 14: C++ Systems with Memory Ops': [0.225, 0.211, 0.227, 5.345, 0.001, 0.139, 0.139, 0.421, 0.405, -0.016, 0.682, 0.492, 0.472, -0.052, 5.219, 0.138, 4.175, 0.726, 1.18, 0.392, 75.683, 0.84, 0.302, 2.229, 1.002, 1.928, -0.212, 0.359, 0.174, 0.109, 0.478, 0.108, 0.17, 0.294, 0.0, 0.129, 0.17, 2.228, -0.164, -0.392, 0.071, 0.902, 0.258, -0.221, 0.241, 0.5, -0.159, -0.112, 0.005, 0.027, 0.0, 0.095, 0.001, 0.006, -0.088, 0.136, 0.083, 0.294, 0.467, 0.435, 0.041, 0.121, -0.301, 0.426, 0.1, 0.199, 0.069, 0.033, 0.201, 0.49, 0.244, 0.627, 0.046, 0.093, 0.341, 0.122, 0.1, 0.095, 0.003, 0.0, 0.002, 0.032, 0.013, 3.021, 0.939, 0.176, 0.004, 0.009, 0.111, 2.467, 0.12, 0.011, 0.291, 0.046, 0.778, 0.086, 0.3, 0.075, 0.007, 0.0, 0.001, 0.001, 0.005, 0.002, 0.056, 0.004, 0.012, -0.091, 0.0, 0.506, 0.025, 0.001, 0.005, 0.214, 0.0, 0.044, 0.0, 0.0, 0.076, 0.0, 0.0, 0.001, 0.0],
        'File Macro-Species 15: C Native Embedded & Legacy': [0.147, 0.039, 0.151, 1.863, 0.0, 0.14, 0.211, 0.332, 0.272, -0.775, 0.492, 0.277, 0.286, -0.087, 1.111, 0.355, 2.53, 0.154, 0.295, 0.012, 0.451, 0.068, 0.286, 91.759, 0.461, 1.209, -0.328, 0.331, 0.095, 0.08, 0.347, -0.11, 0.107, 0.184, 0.0, -0.003, 0.05, 1.353, -0.023, 0.035, 0.028, 0.865, 0.215, -0.145, 0.183, 0.359, -0.156, -0.227, 0.001, 0.007, 0.0, 0.094, 0.0, -0.102, -0.351, -0.704, 0.012, 0.184, 0.185, 0.46, 0.045, 0.195, 0.225, 0.214, 0.081, 0.087, 0.029, 0.021, 0.022, 0.817, 0.071, 0.085, 0.015, 0.076, 0.293, -0.107, 0.062, 0.07, 0.001, 0.0, 0.001, 0.009, 0.014, 4.034, 1.0, 0.058, 0.014, 0.008, 0.106, 0.222, 0.128, 0.008, 0.467, 0.027, 0.237, 0.068, 0.391, 0.025, 0.003, 0.0, 0.0, 0.001, 0.002, 0.003, 0.026, 0.0, 0.008, -0.284, 0.0, 0.458, 0.008, 0.0, 0.002, 0.175, 0.0, 0.042, 0.0, 0.0, -0.066, 0.0, 0.0, 0.002, 0.0],
        'File Macro-Species 16: Safe Polyglot Services': [0.43, 0.308, 0.248, 5.149, 0.0, 0.188, 0.182, 0.589, 0.647, 0.136, 0.955, 0.68, 0.281, -0.014, 1.587, 0.37, 7.042, 2.043, 2.485, 2.145, 2.146, 10.616, 4.157, 1.139, 42.031, 6.826, -0.13, 0.053, 0.511, 0.215, 0.489, 0.084, 0.17, 0.363, 0.0, -0.329, 0.117, 1.145, -0.446, -0.035, 0.542, 0.651, 0.356, -0.418, 0.311, 0.899, -0.38, -0.212, 0.002, 0.208, 0.008, 0.012, 0.004, 0.146, 0.118, 0.17, 0.171, 0.363, 1.518, 1.199, 0.009, 0.278, 0.081, 0.091, 0.146, 0.277, 0.577, 0.145, 0.454, 0.156, 0.896, 1.664, 0.323, 0.093, 0.199, 0.035, 0.114, 0.041, 0.001, 0.0, 0.009, 0.052, 0.035, 0.446, 0.394, 0.202, 0.001, 0.046, 0.083, 0.414, 0.337, 0.019, 0.307, 0.106, 0.35, 0.168, 1.127, 0.071, 0.011, 0.003, 0.004, 0.009, 0.02, 0.009, 0.116, 0.009, 0.053, -0.048, 0.0, 0.423, 0.06, 0.0, 0.029, 0.425, 0.003, 0.059, 0.0, 0.001, -0.099, 0.001, 0.0, 0.003, 0.001],
        'File Macro-Species 17: Python/Java Data Services': [0.024, 0.215, 0.174, 3.024, 0.0, -0.129, 0.045, 0.134, 0.146, 0.079, 0.62, 0.257, 0.975, -0.005, 0.451, 0.082, 1.212, 0.907, 0.439, 0.95, 0.259, 81.56, 1.618, 0.469, 2.637, 1.684, -0.26, 0.12, 0.283, 0.207, 0.787, 0.212, 0.239, 0.57, 0.0, -0.211, 0.047, 0.663, -0.134, 0.122, 0.694, 0.405, 0.155, -0.026, 0.297, 0.772, -0.281, 0.051, 0.005, 0.108, 0.009, 0.0, 0.004, -0.121, 0.275, 0.273, 0.269, 0.57, 0.517, 1.458, 0.007, 0.15, 0.165, -0.164, 0.068, 0.445, 0.624, 0.281, 0.37, 0.047, 1.376, 3.646, 0.245, 0.039, 0.214, 0.241, 0.071, 0.019, 0.0, 0.0, 0.005, 0.018, 0.029, 0.115, 0.128, 0.039, 0.0, 0.029, 0.048, 0.278, 0.207, 0.01, 0.3, 0.05, 0.365, 0.037, 0.909, 0.107, 0.037, 0.006, 0.005, 0.009, 0.062, 0.005, 0.081, 0.007, 0.089, -0.072, 0.0, 0.545, 0.065, 0.0, 0.016, 0.399, 0.001, 0.045, 0.0, 0.001, 0.176, 0.001, 0.0, 0.003, 0.001],
        'File Macro-Species 18: Strictly Typed App Engines': [0.001, 0.21, 0.45, 1.515, -0.0, 0.352, 0.427, 1.103, 0.636, 0.063, 0.223, 0.857, 0.325, -0.047, 0.443, 0.034, 0.193, 0.049, 97.688, 0.227, 0.069, 0.082, 0.096, 0.15, 0.312, 0.243, -0.468, 0.453, 0.466, 0.31, 0.685, 0.139, -0.084, 0.168, 0.0, 0.165, 0.123, 0.756, -0.017, 0.009, 0.709, 0.391, 0.204, -0.002, 0.513, 1.118, 0.03, -0.108, 0.007, 0.063, 0.007, 0.009, 0.0, 0.177, -0.232, 0.104, 0.075, 0.168, 1.521, 1.249, 0.008, 0.268, -0.077, -0.043, 0.073, 0.147, 0.626, 0.557, 0.835, 0.562, 0.764, 0.942, 0.339, 0.045, 0.238, 0.16, 0.081, 0.015, 0.001, 0.0, 0.007, 0.054, 0.09, 0.905, 0.275, 0.325, 0.001, 0.029, 0.081, 0.274, 0.43, 0.018, 0.299, 0.025, 1.281, 0.159, 0.406, 0.086, 0.014, 0.0, 0.001, 0.011, 0.009, 0.008, 0.136, 0.008, 0.022, 0.035, 0.0, 0.232, 0.042, 0.0, 0.052, 0.227, 0.003, 0.025, -0.0, 0.002, 0.226, -0.0, 0.0, 0.001, 0.001],
        'File Macro-Species 19: Infrastructure & CI/CD Scripts': [-0.087, 0.841, 1.042, 71.486, 0.042, 0.434, 0.277, 0.887, 0.628, -0.338, 0.568, 1.139, 0.159, -0.033, 1.408, 0.124, 19.641, 0.915, 1.027, 1.212, 0.752, 0.778, 33.698, 2.382, 3.637, 26.625, -0.526, 1.24, 0.16, 0.116, 0.259, -0.193, 0.211, 0.119, 0.0, 0.582, 0.526, 1.439, 0.121, -0.334, 0.641, 0.62, 0.247, 0.081, 0.228, 0.441, -0.165, -0.22, 0.007, 0.053, 0.012, 0.002, 0.003, 0.291, -0.147, -0.187, -0.177, 0.119, 0.672, 4.95, 0.224, 1.752, -0.283, 0.133, 0.096, 0.317, 0.628, 0.149, 0.263, 0.359, 0.535, 0.358, 0.136, 0.338, 1.385, -0.18, 0.069, 0.041, 0.001, 0.0, 0.019, 0.072, 0.139, 0.56, 0.075, 0.104, 0.007, 0.025, 1.153, 0.18, 1.001, 0.18, 0.189, 0.196, 0.224, 0.829, 0.435, 0.156, 0.022, 0.001, 0.001, 0.009, 0.028, 0.005, 0.151, 0.009, 0.017, 0.0, 0.0, 0.449, 0.025, 0.0, 0.054, 0.207, 0.004, 0.441, -0.0, -0.0, -0.147, 0.001, 0.0, 0.019, 0.002],
        'File Macro-Species 20: Async UI Test Suites': [-0.028, 0.618, 1.003, 86.244, 0.013, -0.197, 0.396, 0.411, 0.182, -0.006, 0.25, 0.197, 0.755, -0.044, 1.1, 0.0, 0.178, 0.065, 0.856, 95.05, 0.152, 0.405, 0.243, 0.012, 1.011, 0.371, -0.585, 0.48, 0.308, 0.242, 0.419, 0.039, -0.016, 0.064, 0.0, 0.064, -0.034, 0.795, -0.024, -0.273, 1.617, 0.16, 0.429, 0.022, 0.453, 0.928, 0.156, -0.019, 0.037, 0.039, 0.033, -0.0, 0.002, -0.236, 0.222, 0.553, 0.497, 0.064, 0.525, 1.134, 0.071, 0.558, -0.266, -0.257, 0.149, 1.781, 1.616, 0.694, 2.641, 0.492, 0.988, 1.044, 0.366, 0.045, 0.243, 0.07, 0.084, 0.01, 0.0, 0.0, 0.023, 0.272, 0.246, 0.059, 0.009, 0.548, -0.0, 0.015, 0.213, 0.179, 0.256, 0.123, 0.175, 0.034, 0.974, 0.194, 0.228, 0.294, 0.161, 0.0, 0.001, 0.006, 0.015, 0.007, 0.298, 0.006, 0.079, -0.034, 0.0, 0.183, 0.039, 0.0, 0.174, 0.243, 0.012, 0.025, -0.0, 0.002, 0.136, 0.0, 0.0, 0.008, 0.007],
        'File Macro-Species 21: High-Safety Business Logic': [0.05, 0.676, 1.056, 86.686, 0.126, 0.441, 0.402, 1.143, 0.692, 0.082, 0.287, 1.281, 0.254, -0.076, 1.975, 0.039, 0.418, 0.051, 89.837, 2.232, 0.163, 0.883, 0.675, 0.034, 2.328, 0.927, -0.458, 0.696, 0.446, 0.293, 0.462, 0.054, -0.05, 0.239, 0.0, 0.278, 0.047, 0.858, -0.098, -0.164, 1.106, 0.216, 0.214, -0.052, 0.431, 1.033, 0.089, -0.085, 0.047, 0.128, 0.056, 0.002, 0.002, 0.23, -0.473, 0.17, 0.158, 0.239, 1.558, 1.592, 0.034, 0.574, -0.148, -0.136, 0.076, 0.551, 1.17, 0.56, 1.131, 0.976, 0.778, 1.513, 0.381, 0.143, 0.395, 0.07, 0.115, 0.013, 0.001, 0.0, 0.016, 0.159, 0.273, 0.448, 0.159, 0.426, 0.0, 0.052, 0.222, 0.424, 1.035, 0.053, 0.63, 0.051, 1.365, 0.306, 0.669, 0.183, 0.084, -0.0, -0.0, 0.003, 0.031, 0.009, 0.269, 0.008, 0.032, 0.143, 0.0, 0.168, 0.021, -0.0, 0.172, 0.385, 0.003, 0.021, 0.0, 0.0, 0.189, 0.0, 0.0, 0.001, 0.018],
        'File Macro-Species 22: Pure C Low-Level Kernels': [0.969, 0.125, 0.058, 0.419, 0.0, 0.286, 0.349, 0.908, 1.024, 0.126, 1.003, 0.72, 0.029, -0.026, 3.627, 47.193, 21.06, 2.265, 0.74, 0.075, 0.539, 0.283, 0.468, 3.505, 0.724, 0.215, 0.09, -0.132, 0.05, 0.026, 0.094, -0.101, 0.027, 1.1, 0.0, -0.324, -0.084, 0.27, -0.79, 0.067, 0.037, 0.602, 0.107, -0.933, 0.088, 0.221, -0.345, -0.752, 0.001, 0.021, -0.0, 0.183, -0.0, 0.191, 0.034, -0.157, -0.054, 1.1, 0.183, 0.375, 0.014, 0.269, 0.559, 0.544, 0.043, 0.05, 0.048, 0.002, 0.011, 0.606, 0.059, 0.036, 0.003, 0.04, 0.635, -0.096, 0.039, 0.052, 0.0, 0.0, 0.0, 0.019, 0.096, 4.036, 1.693, 0.059, 0.006, 0.008, 0.069, 0.154, 0.09, 0.008, 0.787, 0.022, 0.385, 0.078, 0.959, 0.047, 0.001, 0.0, 0.0, 0.0, 0.001, 0.029, 0.003, 0.0, 0.0, 0.192, 0.0, 0.04, 0.007, 0.0, 0.002, 0.107, 0.0, 0.005, 0.0, 0.0, -0.144, -0.0, 0.0, 0.0, 0.0],
        'File Macro-Species 23: C++/TS Hybrid Engines': [-0.157, 0.114, 0.25, 6.424, 0.0, -0.052, 0.071, 0.142, 0.049, -0.037, 0.336, 0.251, 0.778, -0.049, 95.757, 0.078, 0.583, 0.085, 0.51, 0.207, 0.627, 0.186, 0.12, 0.52, 0.091, 0.511, -0.597, 0.426, 0.13, 0.142, 0.734, 0.108, 0.183, 0.426, 0.0, 0.108, 0.075, 1.348, 0.14, -0.073, 0.304, 0.515, 0.185, 0.148, 0.301, 0.562, -0.004, -0.001, 0.004, 0.007, 0.002, 0.018, 0.001, -0.211, -0.233, 0.138, 0.17, 0.426, 0.225, 0.473, 0.022, 0.142, -0.037, 0.062, 0.074, 0.152, 0.23, 0.209, 0.249, 0.424, 0.758, 0.525, 0.084, 0.065, 0.307, 0.127, 0.071, 0.025, 0.001, 0.0, 0.004, 0.023, 0.1, 2.597, 0.517, 0.194, 0.002, 0.01, 0.074, 0.362, 0.164, 0.007, 0.257, 0.023, 1.414, 0.043, 0.306, 0.048, 0.007, 0.0, 0.001, 0.002, 0.021, 0.005, 0.078, 0.003, 0.02, -0.141, 0.0, 0.476, 0.027, 0.0, 0.029, 0.123, 0.001, 0.025, 0.0, 0.002, 0.128, 0.0, 0.0, 0.001, 0.0],
    }
}

# Language Specific File Archetypes (K-means Clusters)
SPECIFIC_FILE_INFERENCE_MODEL = {
    "python": {
    'SCALER_MEDIANS': [3.595, 4.47, 2.827, 2.796, 0.516, 1.271, 0.0, 0.0, 0.0, 2.849, 0.0, 0.0, 2.603, 0.0, 0.0, 0.0, 0.0, 0.0, 0.179, 0.0, 0.0, 0.0, 3.045, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.872, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.157, 2.398, 1.792, 0.0, 0.0, 0.0, 0.693, 1.099, 0.0],
    'SCALER_IQRS': [3.969, 1.514, 2.065, 2.078, 2.037, 3.028, 2.097, 1.0, 1.0, 1.846, 2.204, 1.0, 3.932, 1.963, 1.0, 1.0, 1.0, 2.234, 3.387, 0.825, 1.0, 0.804, 1.814, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.336, 0.642, 1.0, 1.0, 1.0, 1.0, 1.0, 3.66, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.085, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.355, 3.912, 1.299, 1.792, 1.099, 1.0, 1.792, 1.163, 1.0],
    'ARCHETYPES_K6': {
        'Cluster 0: Decorated Core & Metaprogramming': [-0.076, 0.432, 0.432, 0.42, 0.784, 0.052, 0.923, 0.014, 0.329, 0.41, 0.755, 0.082, 0.176, 0.183, 0.02, 0.302, 0.024, 1.043, 0.834, 0.56, 0.266, 4.164, 0.346, 0.009, 0.132, 0.034, 0.003, 0.014, 0.037, 0.012, 0.0, 0.007, 0.0, 0.051, 0.07, 0.485, 0.707, 0.011, 0.071, 0.053, 0.165, 0.08, 0.432, 0.164, 0.026, 0.012, 0.028, 0.012, 0.021, 0.005, 0.13, 0.019, 0.228, 0.0, 0.006, 0.2, 0.0, 0.896, 0.002, -0.0, 0.011, -0.0, 0.0, 0.186, 0.0, -0.038, -0.095, -0.064, 0.65, 0.627, 0.052, 0.086, -0.131, 0.097],
        'Cluster 1: Declarative Glue & Initialization': [-0.602, -0.493, -0.669, -0.663, 0.129, -0.247, 0.263, 0.016, 0.174, -0.501, 0.136, 0.044, -0.269, 0.215, 0.009, 0.063, 0.03, 0.186, 0.191, 0.113, 0.223, 0.072, -0.31, 0.017, 0.04, 0.019, 0.001, 0.006, 0.017, 0.012, 0.0, 0.002, 0.0, 0.014, 0.236, 0.166, 0.017, 0.006, 0.117, 0.021, 0.078, 0.015, -0.304, 0.027, 0.025, 0.007, 0.007, 0.009, 0.062, 0.005, 0.156, 0.012, 0.093, 0.0, 0.014, 0.196, 0.0, 0.225, 0.001, 0.0, 0.004, -0.0, 0.0, 0.012, 0.0, -0.071, -0.354, -0.498, 0.585, 0.341, 0.023, -0.239, -0.538, 0.08],
        'Cluster 2: Async & Concurrent Testing': [0.056, 1.023, 0.546, 0.548, 0.299, 0.686, 0.821, 0.006, 0.645, 0.565, 0.744, 0.041, 0.412, 1.479, 0.013, 0.17, 0.094, 0.846, 0.971, 0.706, 0.038, 0.43, 0.755, 0.002, 0.065, 0.021, 0.0, 0.019, 0.149, 0.031, 0.0, 0.0, 0.0, 0.059, 0.144, 0.56, 0.979, 0.128, 0.028, 0.18, 0.046, 0.169, -0.024, 0.492, 0.426, 0.081, 0.03, 0.063, 0.047, 0.005, 0.379, 0.013, 0.563, 0.0, 0.022, 2.262, 0.001, 4.939, 0.004, 0.02, 0.013, -0.0, 0.0, 1.19, 0.0, -0.072, 0.008, 0.391, 0.797, 0.951, 0.006, 0.12, -0.231, 0.097],
        'Cluster 3: Data Pipelines & I/O Operations': [0.058, -0.054, -0.008, -0.011, 0.279, 0.117, 0.649, 0.06, 1.071, -0.108, 0.74, 0.165, -0.047, 0.245, 0.03, 0.224, 0.255, 0.383, 0.365, 1.132, 0.419, 0.487, -0.109, 0.028, 0.194, 0.093, 0.004, 0.013, 0.06, 0.02, 0.0, 0.009, 0.0, 0.166, 0.533, 0.822, 2.023, 0.034, 0.291, 0.051, 0.048, 0.122, 0.001, 0.108, 0.026, 0.006, 0.036, 0.026, 0.043, 0.008, 0.354, 0.092, 0.192, 0.0, 0.014, 0.321, 0.0, 0.279, 0.003, 0.001, 0.039, 0.0, 0.0, 0.04, 0.0, 0.645, 0.356, 0.192, 0.519, 0.839, 0.078, 0.688, -0.021, 0.177],
        'Cluster 4: Procedural Verification & Mocks': [-0.078, 0.555, 0.42, 0.422, 0.397, 0.886, 0.497, 0.025, 0.914, 0.483, 0.423, 0.129, -0.202, 2.384, 0.041, 0.295, 0.244, 0.869, 0.319, 0.686, 0.41, 0.521, 0.163, 0.004, 0.239, 0.101, 0.001, 0.017, 0.051, 0.019, 0.0, 0.004, 0.0, 0.022, 0.126, 0.94, 0.25, 0.04, 0.186, 0.039, 0.04, 0.074, -0.117, 0.095, 0.83, 0.008, 0.034, 0.08, 0.172, 0.011, 0.715, 0.028, 0.443, 0.0, 0.027, 3.642, -0.0, 0.31, 0.011, 0.027, 0.104, -0.0, 0.0, 0.017, 0.0, 0.006, 0.144, 0.197, 0.06, 0.546, 0.006, 0.338, -0.018, 0.177],
        'Cluster 5: Universal Dependencies & Serialization': [-0.011, -0.059, 0.063, 0.076, 0.384, 0.194, 0.639, 0.002, 0.297, -0.204, 0.82, 0.058, 0.107, 0.121, 0.006, 0.114, 0.007, 1.038, 0.952, 1.344, 0.027, 2.984, -0.154, 0.001, 0.525, 0.014, 0.005, 0.004, 0.014, 0.004, 0.0, 0.001, 0.0, 0.027, 0.192, 0.779, 1.882, 0.004, 0.938, 0.022, 0.034, 0.467, 0.282, 0.077, 0.003, 0.008, 0.037, 0.007, 0.637, 0.009, 1.502, 0.044, 0.108, 0.0, 0.002, 0.08, 0.0, 0.628, 0.001, 0.0, 0.003, -0.0, 0.0, 0.053, 0.0, 0.468, 0.606, 0.728, 4.048, 1.249, 0.05, 0.391, -0.134, 0.171],
            }
        },
    "javascript": {
    'SCALER_MEDIANS': [3.621, 4.179, 2.529, 0.424, 0.0, 0.0, 0.0, 0.0, 0.0, 2.162, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.494, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 1.099, 0.693, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    'SCALER_IQRS': [3.932, 1.578, 3.781, 3.258, 1.0, 1.0, 2.487, 1.0, 2.872, 3.536, 3.853, 1.0, 1.0, 1.0, 2.872, 1.879, 1.0, 1.778, 1.0, 1.0, 1.0, 1.0, 3.932, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.558, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 2.197, 1.386, 0.693, 1.0, 1.0, 1.0, 1.099, 1.0],
    'ARCHETYPES_K10': {
        'Cluster 0: The God Nodes (Universal Dependencies)': [0.112, 0.003, -0.598, -0.06, 0.039, 0.004, 1.063, 0.001, 0.951, 0.342, 1.054, 0.002, 0.002, 0.001, 0.889, 0.071, 0.003, 1.502, 0.0, 0.008, 0.0, 2.868, 0.322, 0.0, 0.002, 0.0, 0.0, 0.001, 0.008, 0.001, 0.0, 0.0, 0.0, -0.0, 0.006, 0.002, 0.003, 0.0, 0.004, 0.0, 0.038, 0.005, 0.007, 0.006, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.007, 0.0, 0.001, 0.0, 0.0, 0.006, 0.022, 0.002, -0.0, 0.0, -0.0, 0.001, 0.0, 0.0, 0.0, 0.458, 0.397, 0.467, 0.958, 0.004, 0.0, 0.034, 0.053, 0.002],
        'Cluster 1: Async Testing & I/O Mocks': [-0.323, -0.024, 0.299, 0.91, 0.073, 0.574, 0.237, 0.442, 0.106, -0.203, 0.21, 0.017, 0.318, 4.339, 0.089, 1.201, 0.326, 0.214, 0.0, 0.224, -0.0, 0.289, -0.044, 0.0, 0.085, 0.013, 0.0, 0.005, 0.33, 0.164, 0.0, 0.0, 0.0, 0.0, 0.072, 0.06, 0.12, 0.046, 0.085, 0.002, 0.752, 0.091, 0.105, 0.207, 0.099, 0.003, 0.014, 0.004, 0.0, 0.0, 0.133, 0.005, 0.087, 0.0, 0.004, 1.563, 0.683, 0.846, 0.0, 0.003, 0.144, 0.037, 0.0, 0.06, 0.0, -0.123, 0.142, 0.058, 0.218, 0.055, 0.006, 0.357, 0.623, 0.06],
        'Cluster 2: Procedural Core & Safety Wrappers': [-0.005, -0.371, 0.219, 0.642, 0.467, 3.301, 0.961, 0.01, 0.096, -0.269, 0.602, 0.045, 0.167, 0.092, 0.129, 0.75, 0.356, 0.389, 0.0, 0.269, -0.0, 0.648, -0.284, 0.001, 0.032, 0.01, 0.001, 0.007, 0.106, 0.079, 0.0, 0.0, 0.0, 0.002, 0.549, 0.054, 0.33, 0.012, 0.136, 0.004, 0.556, 0.109, 0.105, 0.129, 0.003, 0.001, 0.006, 0.003, 0.001, 0.001, 0.156, 0.006, 0.022, 0.0, 0.001, 0.146, 0.38, 0.096, 0.0, -0.0, 0.066, 0.016, 0.0, 0.002, 0.0, 0.477, 0.615, -0.081, 0.313, 0.101, 0.003, 0.83, 0.692, 0.045],
        'Cluster 3: Pure View Layer Components (UI)': [-0.584, -0.067, 0.016, 0.514, 0.663, 0.015, 0.1, 0.028, 0.034, -0.269, 0.507, 0.027, 0.028, 0.031, 0.101, 0.557, 0.083, 0.334, 0.0, 0.063, 0.0, 0.16, -0.382, 0.0, 0.013, 0.004, 0.001, 0.017, 0.046, 0.044, 0.0, 0.0, 0.0, 0.001, 0.439, 0.026, 0.03, 0.009, 0.059, 0.001, 0.337, 0.039, 0.067, 0.062, 0.003, 0.001, 0.003, 0.001, 0.0, 0.001, 0.063, 0.003, 0.009, 0.0, 0.001, 0.051, 0.26, 0.115, 0.0, 0.0, -0.0, 0.007, 0.0, 0.002, 0.0, -0.275, -0.244, -0.271, 0.173, 0.037, 0.002, 0.122, 0.53, 0.043],
        'Cluster 4: Heavily Documented Core Functions': [-0.271, -0.076, 0.094, 0.643, 0.586, 0.568, 0.266, 0.029, 0.087, 0.145, 0.396, 0.037, 4.096, 0.124, 0.205, 0.549, 0.129, 0.452, 0.002, 0.176, -0.0, 0.334, -0.023, 0.008, 0.091, 0.01, 0.003, 0.002, 0.175, 0.058, 0.0, 0.0, 0.0, 0.002, 0.073, 0.042, 0.081, 0.01, 0.106, 0.023, 0.758, 0.128, 0.095, 0.091, 0.006, 0.002, 0.003, 0.001, 0.001, 0.006, 0.167, 0.006, 0.011, 0.0, 0.002, 0.12, 0.458, 0.213, 0.0, -0.0, 0.005, 0.042, 0.0, 0.005, 0.0, -0.07, 0.16, 0.142, 0.951, 0.049, 0.008, 0.415, 0.639, 0.078],
        'Cluster 5: I/O, UI & Routing Configuration': [0.063, 0.52, -0.633, -0.097, 0.002, 0.001, 0.008, 0.006, 1.256, 0.498, 0.011, 0.003, 0.004, 0.0, 1.228, 0.017, 0.011, 0.078, 0.0, 0.006, 0.0, 0.001, 0.517, 0.0, 0.002, 0.0, 0.0, 0.009, 0.011, 0.018, 0.0, 0.0, 0.0, -0.0, 0.0, 0.001, 0.0, 0.001, 0.007, 0.001, 0.051, 0.005, 0.008, 0.011, 0.0, 0.001, 0.0, 0.0, 0.0, 0.0, 0.011, 0.001, 0.002, 0.0, 0.0, 0.003, 0.007, 0.003, -0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.0, 0.003, 0.001, 0.292, 1.025, 0.012, 0.001, 0.004, 0.017, 0.055],
        'Cluster 6: Documented Native Core Logic': [-0.459, -0.227, 0.004, 0.555, 0.396, 0.514, 0.235, 0.036, 0.104, 0.009, 0.207, 0.031, 0.673, 0.303, 0.257, 0.535, 0.202, 0.398, -0.0, 0.2, 0.0, 0.183, -0.1, 0.0, 0.047, 0.007, 0.0, 0.025, 0.084, 0.094, 0.0, 0.0, 0.0, 0.002, 0.26, 0.036, 0.082, 0.022, 0.061, 0.049, 0.64, 0.057, 0.082, 0.11, 0.03, 0.005, 0.007, 0.007, 0.0, 0.004, 0.123, 0.021, 0.027, 0.0, 0.003, 0.057, 0.232, 0.306, 0.0, 0.0, 0.014, 0.014, 0.0, 0.022, 0.0, -0.135, 0.04, 0.08, 5.33, 0.044, 0.037, 0.388, 0.593, 0.083],
        'Cluster 7: Algorithmic Data Processing': [0.014, -0.48, 0.273, 0.697, 0.268, 2.446, 0.896, 0.036, 0.178, -0.323, 0.648, 0.131, 1.754, 0.187, 0.169, 0.809, 0.358, 0.259, 0.002, 0.657, 0.0, 0.609, -0.254, 0.013, 0.138, 0.025, 0.003, 0.003, 0.277, 0.14, 0.0, 0.0, 0.0, 0.006, 0.183, 0.201, 0.456, 0.07, 0.3, 0.021, 0.923, 0.373, 0.121, 0.31, 0.008, 0.002, 0.012, 0.007, 0.001, 0.006, 0.233, 0.042, 0.045, 0.0, 0.003, 0.2, 1.016, 0.528, 0.0, 0.001, 0.058, 0.17, 0.0, 0.137, 0.0, 0.62, 1.575, 0.508, 1.452, 0.164, 0.032, 2.782, 1.046, 0.217],
        'Cluster 8: Declarative Glue & Inert Types': [-0.72, -2.366, -0.391, 0.104, 0.008, 0.025, 0.098, 0.028, 0.077, -0.437, 0.051, 0.009, 0.143, 0.085, 0.034, 0.097, 0.106, 0.1, 0.0, 0.01, 0.0, 0.092, -0.504, 0.001, 0.013, 0.005, 0.001, 0.0, 0.041, 0.035, 0.0, 0.0, 0.0, 0.003, 0.477, 0.021, 0.05, 0.007, 0.128, 0.001, 0.289, 0.024, 0.035, 0.063, 0.006, 0.001, 0.003, 0.001, 0.002, 0.0, 0.358, 0.004, 0.006, 0.0, 0.002, 0.014, 0.138, 0.05, 0.001, 0.0, 0.001, 0.002, 0.0, 0.001, 0.0, -0.044, -0.057, -0.364, 0.282, 0.034, 0.004, 0.049, 0.168, 0.084],
        'Cluster 9: Highly Concurrent State Management': [-0.09, 0.194, 0.407, 0.897, 0.589, 1.668, 0.55, 0.084, 0.294, -0.216, 0.681, 0.085, 0.676, 0.411, 0.245, 1.202, 0.512, 0.538, 0.0, 0.526, 0.008, 0.467, -0.051, 0.004, 0.094, 0.019, 0.0, 0.054, 0.349, 0.69, 0.0, 0.0, 0.0, 0.01, 0.533, 0.102, 0.491, 0.303, 0.104, 0.024, 1.069, 0.398, 0.167, 0.394, 0.081, 0.002, 0.018, 0.029, 0.008, 0.005, 0.477, 0.008, 0.069, 0.0, 0.004, 0.234, 1.108, 4.379, 0.001, 0.004, 0.091, 0.203, 0.0, 1.951, 0.0, 0.089, 0.637, 0.308, 0.692, 0.139, 0.006, 1.248, 0.852, 0.119],
            }
        },
    "typescript": {
    'SCALER_MEDIANS': [3.504, 4.316, 2.898, 2.494, 0.0, 0.0, 0.0, 0.0, 0.0, 2.494, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.28, 0.0, 0.0, 0.0, 2.904, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.48, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.167, 1.609, 1.386, 0.693, 0.0, 0.0, 0.0, 0.742, 0.0],
    'SCALER_IQRS': [3.932, 1.206, 2.632, 3.536, 1.0, 2.527, 0.558, 1.0, 1.0, 2.366, 1.583, 1.0, 2.312, 1.0, 2.504, 2.398, 1.0, 2.185, 2.872, 1.0, 1.0, 1.0, 2.197, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 3.536, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.371, 3.178, 1.253, 1.609, 1.0, 1.0, 1.386, 1.154, 1.0],
    'ARCHETYPES_K9': {
        'Cluster 0: The God Nodes (Universal Dependencies)': [-0.373, 0.346, -0.576, -0.403, 0.224, 0.269, 0.089, 0.007, 0.284, 0.486, 0.232, 0.012, 0.636, 0.006, 0.225, 0.312, 0.027, 0.574, -0.097, 0.09, 0.034, 0.225, 0.2, 0.006, 0.029, 0.004, 0.0, 0.002, 0.017, 0.031, 0.0, 0.0, 0.0, 0.001, 0.006, 0.497, 0.051, 0.005, 0.098, 0.009, -0.22, 0.029, 0.15, 0.021, 0.005, 0.0, -0.0, 0.01, 0.007, 0.008, 0.082, 0.002, 0.018, 0.0, 0.002, 0.047, 0.233, 0.12, 0.0, 0.0, 0.002, 0.001, 0.0, 0.0, 0.0, -0.011, -0.136, -0.054, 2.874, 0.032, 0.016, 0.282, -0.304, 0.106],
        'Cluster 1: Async Scripting & I/O Automation': [-0.07, 0.192, 0.176, 0.15, 0.215, 0.793, 0.251, 0.026, 0.883, -0.14, 0.405, 0.054, 0.337, 0.078, 0.622, 0.726, 0.261, 0.554, 0.124, 0.416, 0.075, 0.077, 0.007, 0.003, 0.083, 0.011, 0.001, 0.016, 0.173, 0.375, 0.0, 0.0, 0.0, 0.081, 0.297, 0.392, 0.416, 0.168, 0.338, 0.014, 0.135, 0.27, 0.111, 0.2, 0.016, 0.0, -0.0, 0.055, 0.009, 0.012, 0.45, 0.008, 0.061, 0.0, 0.004, 0.133, 0.874, 3.454, 0.002, 0.002, 0.043, 0.091, 0.0, 0.351, 0.0, 0.306, 0.283, 0.129, 0.263, 0.126, 0.008, 0.932, 0.204, 0.15],
        'Cluster 2: Type Definitions & Bypasses': [-0.02, 0.448, 0.324, 0.26, 0.592, 0.841, 6.183, 0.021, 0.43, 0.022, 0.723, 0.064, 0.713, 0.124, 0.617, 0.621, 0.16, 0.341, 0.381, 0.357, 0.052, 0.163, -0.269, 0.022, 0.134, 0.017, 0.001, 0.003, 0.305, 0.14, 0.0, 0.0, 0.0, 0.011, 0.145, 0.504, 0.157, 0.052, 0.404, 0.012, -0.082, 0.26, 0.273, 0.289, 0.02, 0.0, 0.0, 0.03, 0.01, 0.01, 0.175, 0.007, 0.026, 0.0, 0.003, 0.154, 0.469, 0.879, 0.001, 0.0, 0.02, 0.058, 0.0, 0.063, 0.0, 0.242, 0.212, -0.275, 0.234, 0.092, 0.011, 0.675, 0.136, 0.114],
        'Cluster 3: UI Frameworks & View Layers': [0.063, 0.759, 0.311, 0.161, 0.308, 0.557, 0.036, 0.042, 0.301, 0.279, 0.202, 0.023, 0.395, 0.011, 1.239, 0.844, 0.104, 0.782, 0.639, 0.397, 0.047, 0.038, 0.481, 0.006, 0.057, 0.012, 0.0, 0.001, 0.102, 0.096, 0.0, 0.0, 0.0, 0.003, 0.076, 0.618, 0.046, 0.014, 0.431, 0.009, 0.166, 0.103, 0.105, 0.121, 0.011, 0.0, -0.0, 0.014, 0.002, 0.012, 0.131, 0.003, 0.03, 0.0, 0.006, 0.129, 0.182, 0.025, 0.001, 0.0, 0.018, 0.004, 0.0, -0.0, 0.0, 0.13, 0.12, 0.127, 0.165, 0.148, 0.002, 0.357, -0.029, 0.123],
        'Cluster 4: Heavily Documented Core Classes': [-0.843, -0.219, -0.542, -0.626, 1.014, 0.045, 4.18, 0.003, 0.022, -0.044, 0.075, 0.931, 1.256, 0.012, 0.161, 0.408, 0.014, 0.921, 0.346, 0.01, 0.002, 0.006, -0.04, 0.005, 0.013, 0.002, 0.0, 0.0, 0.01, 0.01, 0.0, 0.0, 0.0, 0.0, 0.01, 0.031, 0.003, 0.001, 0.017, 0.001, -0.578, 0.007, 0.94, 0.006, 0.002, 0.0, -0.0, 0.001, 0.004, 0.001, 0.011, 0.0, 0.003, 0.0, 0.016, 0.08, 0.022, 0.017, 0.002, -0.0, 0.001, 0.001, 0.0, 0.0, 0.0, -0.396, -0.458, 0.439, 0.663, 0.008, 0.001, 0.008, -0.566, 0.079],
        'Cluster 5: Declarative Glue & Inert Types': [-0.601, -0.498, -0.596, -0.368, 0.364, 0.13, 0.037, 0.013, 0.2, -0.164, 0.287, 0.194, 0.283, 0.087, 0.107, 0.135, 0.047, 0.163, -0.263, 0.03, 0.021, 0.037, -0.508, 0.006, 0.042, 0.006, 0.0, 0.0, 0.048, 0.037, 0.0, 0.0, 0.0, 0.002, 0.113, 0.203, 0.02, 0.005, 0.058, 0.004, -0.412, 0.045, 0.059, 0.047, 0.007, 0.0, -0.0, 0.012, 0.004, 0.002, 0.06, 0.002, 0.011, 0.0, 0.005, 0.046, 0.152, 0.036, 0.001, 0.0, 0.002, 0.004, 0.0, 0.0, 0.0, -0.113, -0.31, -0.625, -0.085, 0.03, 0.004, 0.038, -0.375, 0.058],
        'Cluster 6: Async Testing & Verification': [-0.13, 0.636, 0.788, 0.664, 0.114, 0.805, 1.641, 0.057, 1.095, -0.87, 0.725, 0.033, 0.225, 4.637, 0.337, 1.748, 0.336, 0.732, -0.097, 0.567, 0.089, 0.119, 0.113, 0.003, 0.176, 0.02, 0.003, 0.002, 0.639, 0.367, 0.0, 0.0, 0.0, 0.023, 0.102, 0.617, 0.336, 0.128, 0.35, 0.023, 0.388, 0.391, 0.222, 0.593, 0.789, 0.0, -0.0, 0.031, 0.005, 0.013, 0.622, 0.017, 0.106, 0.0, 0.021, 0.539, 1.416, 2.688, 0.007, 0.011, 0.035, 0.22, 0.0, 0.494, 0.0, -0.074, 0.282, 0.154, -0.361, 0.168, 0.003, 0.999, 0.274, 0.336],
        'Cluster 7: Highly Concurrent State Management': [0.04, 0.239, 0.265, 0.231, 1.098, 0.969, 1.455, 0.023, 0.796, -0.186, 2.301, 0.085, 0.503, 0.15, 0.659, 0.741, 0.274, 0.631, 0.27, 0.819, 0.119, 0.217, -0.007, 0.007, 0.138, 0.013, 0.006, 0.001, 0.363, 0.618, 0.0, 0.0, 0.0, 0.125, 0.212, 0.581, 0.694, 0.203, 0.444, 0.027, 0.234, 0.782, 1.568, 0.356, 0.04, 0.0, -0.0, 0.042, 0.029, 0.028, 0.395, 0.022, 0.094, 0.0, 0.002, 0.21, 1.701, 4.619, 0.001, 0.008, 0.032, 0.529, 0.0, 2.911, 0.0, 0.415, 0.583, 0.472, 0.355, 0.125, 0.011, 1.412, 0.397, 0.28],
        'Cluster 8: Algorithmic Data Processing': [0.062, -0.336, 0.068, 0.068, 0.438, 0.772, 0.668, 0.029, 0.513, -0.325, 1.257, 0.08, 0.443, 0.041, 0.521, 0.598, 0.247, 0.368, 0.066, 0.837, 0.209, 0.12, -0.328, 0.013, 0.102, 0.015, 0.001, 0.002, 0.17, 0.128, 0.0, 0.0, 0.0, 0.023, 0.143, 0.435, 0.257, 0.038, 0.306, 0.01, 0.122, 0.294, 0.531, 0.205, 0.008, 0.0, 0.0, 0.018, 0.005, 0.014, 0.223, 0.03, 0.063, 0.0, 0.002, 0.13, 0.96, 0.324, 0.001, 0.0, 0.025, 0.127, 0.0, 0.045, 0.0, 0.81, 0.754, 0.266, 0.307, 0.134, 0.012, 1.677, 0.384, 0.234],
            }
        },
     "c": {
    'SCALER_MEDIANS': [3.162, 3.158, 1.282, 1.41, 0.0, 0.0, 0.0, 0.0, 0.0, 3.434, 3.346, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.771, 0.892, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.97, 3.456, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.038, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.333, 3.219, 1.386, 0.0, 0.693, 0.0, 0.693, 0.0, 0.0],
    'SCALER_IQRS': [3.651, 2.068, 2.547, 2.388, 2.354, 0.325, 1.0, 1.0, 1.0, 1.491, 3.932, 1.0, 1.0, 1.0, 1.0, 1.0, 1.329, 1.0, 1.0, 1.0, 1.0, 1.109, 2.041, 1.928, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 3.536, 2.803, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.069, 1.0, 1.955, 1.0, 2.008, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.605, 4.92, 1.386, 1.386, 2.197, 1.0, 2.639, 1.099, 1.0],
    'ARCHETYPES_K5': {
        'Cluster 0: Defensive Downstream Logic & Immutable State': [-0.15, 0.229, 0.223, 0.138, 0.517, 7.832, 0.42, 0.01, 0.257, 0.319, -0.174, 0.115, 0.502, 0.34, 0.001, -0.0, 0.748, 0.011, 0.002, 0.0, 0.074, 0.593, 0.217, 0.234, 0.08, 0.058, 0.001, 0.0, 0.017, 0.058, 0.046, 0.206, 0.011, 0.011, 0.14, 0.468, 0.151, 0.01, 0.59, 0.021, 1.016, 0.18, 0.55, 0.051, 0.0, 0.0, 0.0, 0.001, 0.003, 0.016, 0.011, -0.0, 0.001, 0.0, 0.001, 0.551, 0.261, 0.052, 0.0, 0.0, 0.013, 0.182, 0.0, 0.021, 0.0, 0.002, -0.051, 0.124, 0.725, 0.339, 0.504, 0.242, 0.473, 0.053],
        'Cluster 1: Algorithmic Bitwise & Encapsulated Core': [0.067, 0.276, 0.278, 0.306, 0.699, 0.126, 0.314, 0.028, 0.303, 0.272, 0.044, 0.116, 0.439, 0.029, 0.002, 0.0, 0.772, 0.006, 0.002, 0.0, 0.1, 0.793, 0.18, 0.15, 0.084, 0.106, 0.001, 0.0, 0.02, 0.122, -0.035, 0.171, 0.023, 0.013, 0.171, 0.365, 0.148, 0.016, 0.942, 0.023, 0.607, 0.102, 0.824, 0.07, 0.0, 0.0, 0.0, 0.001, 0.001, 0.051, 0.004, -0.0, 0.001, 0.0, 0.001, 0.207, 0.132, 0.037, 0.0, 0.0, 0.0, 0.079, 0.0, 0.014, 0.0, 0.199, 0.194, 0.309, 0.293, 0.352, 0.158, 0.569, 0.728, 0.053],
        'Cluster 2: Inert Headers & Declarative Structures': [-0.706, -0.735, -0.219, -0.454, 0.278, 0.03, 0.022, 0.013, 0.043, -1.003, -0.555, 0.042, 0.252, 0.005, 0.0, 0.0, 0.068, 0.005, 0.006, 0.0, 0.05, 0.262, -0.21, 0.223, 0.03, 0.026, 0.0, 0.0, 0.006, 0.018, 0.132, -0.744, 0.01, 0.003, 0.019, 0.055, 0.01, 0.009, 0.21, 0.003, 0.223, 0.004, 0.079, 0.01, -0.0, 0.0, 0.0, 0.0, 0.001, 0.002, 0.003, -0.0, 0.0, 0.0, 0.0, 0.129, 0.008, 0.004, -0.0, 0.0, 0.0, 0.002, 0.0, 0.0, 0.0, -0.216, -0.443, -0.473, 0.943, -0.025, 0.657, -0.236, 0.078, 0.022],
        'Cluster 3: Complex Defensive Systems Logic': [0.062, 0.063, 0.102, 0.182, 0.537, 3.748, 0.507, 0.032, 0.503, 0.015, 0.042, 0.101, 0.272, 0.167, 0.001, 0.0, 0.938, 0.005, 0.001, 0.0, 0.092, 0.792, -0.02, -0.076, 0.071, 0.091, 0.001, 0.0, 0.032, 0.062, -0.147, 0.157, 0.012, 0.043, 0.324, 0.661, 0.261, 0.019, 0.677, 0.026, 0.672, 0.353, 0.758, 0.075, 0.0, 0.0, 0.0, 0.0, 0.003, 0.016, 0.01, 0.0, 0.001, 0.0, 0.001, 0.352, 0.41, 0.063, 0.0, -0.0, 0.017, 0.317, 0.0, 0.025, 0.0, 0.34, 0.358, 0.573, 0.207, 0.593, 0.138, 0.809, 0.7, 0.096],
        'Cluster 4: The God Headers (Documented & Defended APIs)': [0.076, 1.277, 1.013, 0.325, 1.312, 13.225, 0.381, 0.018, 0.385, 1.688, -0.18, 0.398, 1.298, 0.31, -0.0, -0.0, 0.546, 0.017, 0.007, 0.002, 0.113, 1.454, 0.744, 0.757, 0.193, 0.171, 0.003, 0.0, 0.044, 0.272, 0.679, 0.851, 0.029, 0.021, 0.121, 0.417, 0.103, 0.006, 1.018, 0.041, 1.895, 0.123, 0.893, 0.144, 0.0, 0.0, 0.0, 0.001, 0.004, 0.085, 0.01, -0.0, 0.001, 0.0, 0.0, 0.784, 0.278, 0.076, 0.0, -0.0, 0.017, 0.132, 0.0, 0.028, 0.0, -0.339, -0.218, -0.006, 1.603, 0.127, 1.119, -0.084, 0.386, 0.049],
        }
    },
    "cpp": {
    'SCALER_MEDIANS': [3.258, 3.536, 2.954, 2.179, 0.333, 0.0, 0.0, 0.0, 0.0, 0.0, 3.781, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.353, 2.565, 1.099, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.677, 2.894, 0.0, 0.0, 0.0, 1.921, 0.0, 0.0, 0.0, 0.0, 2.506, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 2.565, 1.609, 0.693, 1.792, 0.0, 0.693, 0.693, 0.0],
    'SCALER_IQRS': [3.651, 1.495, 1.611, 3.099, 2.097, 1.88, 1.0, 1.0, 1.0, 1.0, 1.766, 1.0, 0.721, 1.0, 1.0, 1.0, 1.477, 1.0, 1.0, 1.0, 1.0, 1.88, 1.674, 2.082, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.872, 3.867, 1.0, 1.0, 1.0, 3.045, 1.0, 1.0, 0.832, 1.0, 2.799, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 4.263, 1.204, 1.386, 3.664, 0.693, 2.197, 1.099, 1.0],
    'ARCHETYPES_K7': {
        'Cluster 0: Declarative Interfaces & Inert Headers': [-0.764, -0.508, -0.723, -0.456, 0.303, 0.311, 0.071, 0.012, 0.011, 0.006, -1.207, 0.065, 0.129, 0.008, 0.014, 0.019, 0.348, 0.024, 0.149, 0.002, 0.051, 0.523, -0.188, 0.145, 0.081, 0.025, 0.0, 0.0, 0.01, 0.0, 0.152, -0.501, 0.005, -0.0, 0.012, -0.328, 0.011, 0.003, 0.327, 0.041, -0.38, 0.014, 0.003, 0.03, 0.0, 0.0, 0.0, 0.001, 0.027, 0.003, 0.044, 0.0, 0.003, 0.0, 0.001, 0.061, 0.032, 0.009, 0.0, -0.0, 0.002, 0.003, 0.0, 0.003, 0.0, -0.233, -0.5, -0.376, 0.369, -0.071, 0.727, -0.29, -0.462, 0.033],
        'Cluster 1: Documented API Headers & Entity Definitions': [-0.387, -0.12, -0.128, -0.151, 0.396, 0.453, 0.161, 0.051, 0.022, 0.007, -0.379, 0.194, 5.313, 0.015, 0.014, 0.092, 0.451, 0.022, 0.236, 0.006, 0.01, 0.378, -0.224, 0.111, 0.127, 0.062, 0.0, 0.0, 0.021, 0.0, 0.025, -0.077, 0.002, 0.0, 0.053, -0.164, 0.061, 0.005, 0.502, 0.061, -0.116, 0.067, 0.003, 0.073, 0.0, 0.0, 0.0, 0.0, 0.02, 0.005, 0.028, 0.0, 0.006, 0.0, 0.001, 0.264, 0.225, 0.025, 0.0, 0.0, 0.011, 0.021, 0.0, 0.01, 0.0, 0.098, -0.094, -0.07, 0.232, -0.006, 0.543, 0.138, -0.095, 0.07],
        'Cluster 2: Verification & Unit Testing': [-0.306, 0.025, 0.33, 0.247, 0.195, 0.584, 0.057, 0.071, 0.049, 0.005, 0.221, 0.079, 0.199, 3.683, 0.018, 0.818, 0.4, 0.045, 0.309, 0.042, 0.014, -0.013, 0.159, 0.07, 0.135, 0.066, 0.0, 0.0, 0.052, -0.0, -0.374, 0.081, 0.0, 0.0, 0.052, 0.194, 0.041, 0.033, 0.235, 0.132, -0.13, 0.157, 0.001, 0.19, 0.074, 0.0, 0.0, 0.001, 0.02, 0.009, 0.115, 0.001, 0.035, 0.0, 0.006, 0.121, 0.208, 0.117, 0.002, -0.0, 0.022, 0.034, 0.0, 0.063, 0.0, 0.026, 0.039, 0.382, -0.439, -0.001, 0.032, 0.16, 0.26, 0.139],
        'Cluster 3: Algorithmic Execution Core': [0.043, -0.074, -0.002, 0.082, 0.013, 0.374, 0.097, 0.117, 0.054, 0.003, 0.099, 0.134, 0.25, 0.05, 0.022, 0.367, 0.427, 0.036, 0.166, 0.015, 0.032, -0.028, -0.134, -0.14, 0.195, 0.105, 0.0, 0.0, 0.041, 0.002, -0.331, 0.066, 0.007, 0.0, 0.109, 0.005, 0.08, 0.014, 0.469, 0.135, -0.098, 0.128, 0.003, 0.143, 0.0, 0.0, 0.0, 0.002, 0.032, 0.01, 0.09, 0.0, 0.009, 0.0, 0.001, 0.277, 0.331, 0.046, 0.0, 0.0, 0.02, 0.046, 0.0, 0.022, 0.0, 0.603, 0.423, 0.433, -0.404, 0.182, 0.056, 0.747, 0.316, 0.112],
        'Cluster 4: The God Headers (Universal Dependencies)': [-0.37, 0.214, -0.107, -0.098, 0.674, 0.436, 0.167, 0.06, 0.023, 0.0, -0.302, 0.212, 0.899, 0.031, 0.015, 0.101, 0.71, 0.096, 0.709, 0.007, 0.049, 0.691, -0.088, 0.171, 0.243, 0.11, 0.0, 0.0, 0.035, 0.0, 0.328, -0.221, 0.011, 0.0, 0.017, -0.062, 0.043, 0.006, 0.728, 0.155, 0.073, 0.07, 0.004, 0.106, 0.0, 0.0, 0.0, 0.001, 0.073, 0.01, 0.059, 0.0, 0.008, 0.0, 0.0, 0.174, 0.104, 0.028, 0.0, 0.0, 0.014, 0.023, 0.0, 0.012, 0.0, -0.07, -0.19, -0.149, 1.321, 0.198, 6.812, -0.058, -0.245, 0.098],
        'Cluster 5: Heavily Documented Complex Base Classes': [0.117, 1.624, 1.298, 0.569, 1.604, 1.468, 0.531, 0.055, 0.021, 0.003, 1.007, 0.736, 8.017, 0.015, 0.019, 0.208, 1.473, 0.104, 1.405, 0.007, 0.02, 1.098, 0.777, 0.403, 0.516, 0.201, 0.001, 0.0, 0.05, 0.0, 0.611, 0.41, 0.001, 0.0, 0.04, 0.503, 0.071, 0.01, 2.198, 0.164, 0.911, 0.209, 0.003, 0.171, 0.0, 0.0, 0.0, 0.0, 0.032, 0.011, 0.063, -0.0, 0.013, 0.0, 0.0, 0.92, 0.296, 0.082, 0.0, 0.0, 0.031, 0.051, 0.0, 0.045, 0.0, -0.166, -0.027, 0.161, 0.979, -0.088, 1.119, 0.024, -0.068, 0.095],
        'Cluster 6: Generic Templates & Metaprogramming Core': [0.1, 1.349, 0.93, 0.417, 1.251, 1.217, 0.141, 0.064, 0.037, 0.001, 0.716, 0.387, 0.106, 0.057, 0.028, 0.299, 1.274, 0.129, 1.672, 0.015, 0.112, 0.857, 0.765, 0.469, 0.381, 0.167, 0.001, 0.0, 0.068, 0.001, 0.509, 0.027, 0.008, 0.0, 0.026, 0.582, 0.052, 0.009, 1.707, 0.278, 0.631, 0.117, 0.011, 0.193, 0.001, 0.0, 0.0, 0.001, 0.053, 0.012, 0.154, 0.0, 0.027, 0.0, 0.0, 0.273, 0.262, 0.07, 0.0, 0.0, 0.029, 0.028, 0.0, 0.037, 0.0, -0.095, -0.022, 0.181, 0.593, 0.049, 0.729, 0.026, -0.063, 0.063],
                }
        },

}

GENERAL_REPO_INFERENCE_MODEL = {
    "k_clusters": 11,
    "cluster_names": [
        "Cluster 0: C-Core OS & Kernel Repositories",
        "Cluster 1: Heavy Polyglot Backend Infrastructure",
        "Cluster 2: C++/Web Native Hybrid Engines",
        "Cluster 3: Pure Backend Data Services",
        "Cluster 4: Mixed Systems & Application Logic",
        "Cluster 5: DevOps, CI/CD & Infrastructure Repositories",
        "Cluster 6: Memory-Safe Systems & Infrastructure",
        "Cluster 7: C++ Backed High-Performance Systems",
        "Cluster 8: Scientific Computing & Legacy Mainframes",
        "Cluster 9: C++ Object-Oriented & Embedded Systems",
        "Cluster 10: Full-Stack Web & Frontend Frameworks"
    ],
    "features": [
        "File-Archetype 0",
        "File-Archetype 1",
        "File-Archetype 10",
        "File-Archetype 11",
        "File-Archetype 12",
        "File-Archetype 13",
        "File-Archetype 14",
        "File-Archetype 15",
        "File-Archetype 16",
        "File-Archetype 17",
        "File-Archetype 18",
        "File-Archetype 19",
        "File-Archetype 2",
        "File-Archetype 20",
        "File-Archetype 21",
        "File-Archetype 22",
        "File-Archetype 23",
        "File-Archetype 3",
        "File-Archetype 4",
        "File-Archetype 5",
        "File-Archetype 6",
        "File-Archetype 7",
        "File-Archetype 8",
        "File-Archetype 9"
    ],
    "centroids": {
        "Cluster 0": [0.02767, 0.12062, 0.00646, 0.00118, -0.0, 0.21851, 0.05048, 0.01377, 0.00158, 0.02489, 0.00761, 0.01069, 0.00197, 0.00172, 0.00226, 0.27254, 0.01428, 0.07362, 0.00642, 0.00593, 0.00682, 0.05144, 0.04535, 0.03419],
        "Cluster 1": [0.03874, 0.51445, 0.05207, 0.04404, 0.00437, 0.00513, 0.0235, 0.02021, 0.00505, 0.00811, 0.01242, 0.0128, 0.06186, 0.0025, 0.00952, 0.0312, 0.03215, 0.02149, 0.0274, 0.01394, 0.01406, 0.0024, 0.00859, 0.03399],
        "Cluster 2": [0.04671, 0.20529, 0.02614, 0.0177, 0.00883, 0.00214, 0.03136, 0.02074, 0.04867, 0.00847, 0.00928, 0.0585, 0.01874, 0.01352, 0.04824, 0.03856, 0.09863, 0.04513, 0.12567, 0.04263, 0.04552, 0.00183, 0.00312, 0.03459],
        "Cluster 3": [0.01557, 0.72228, 0.01159, 0.00746, 0.00123, 0.0188, 0.05056, 0.00931, 0.00131, 0.00629, 0.0057, 0.00612, 0.00819, 0.0015, 0.00466, 0.0123, 0.00464, 0.03937, 0.00331, 0.00609, 0.00762, 0.00617, 0.01746, 0.03247],
        "Cluster 4": [0.05304, 0.34042, 0.01571, 0.02085, 0.01179, 0.01273, 0.03169, 0.02425, 0.01267, 0.03389, 0.01038, 0.04876, 0.03845, 0.0078, 0.03093, 0.06997, 0.02787, 0.02441, 0.03765, 0.05908, 0.02814, 0.00347, 0.01497, 0.0411],
        "Cluster 5": [0.04922, 0.15406, 0.0059, 0.00497, 0.00507, 0.01192, 0.0146, 0.02181, 0.00394, 0.01551, 0.01844, 0.23563, 0.01224, 0.07534, 0.04487, 0.06281, 0.01963, 0.01053, 0.00931, 0.09701, 0.07853, 0.0007, 0.00577, 0.04219],
        "Cluster 6": [0.05511, 0.0999, 0.00505, 0.0, 0.0, 0.00704, 0.08255, 0.08258, 0.0, 0.00131, 0.00328, 0.00102, 0.0, 0.0, 0.00196, 0.02983, 0.00077, 0.55684, 0.0, 0.0027, 0.00051, 0.0, 0.0088, 0.06075],
        "Cluster 7": [0.02086, 0.46424, 0.01397, 0.00265, 0.00012, 0.06694, 0.13305, 0.01594, 0.00013, 0.0137, 0.01548, 0.00471, 0.00778, 0.00027, 0.00673, 0.01677, 0.00173, 0.08008, 0.00057, 0.01709, 0.0022, 0.01896, 0.04566, 0.05035],
        "Cluster 8": [0.0, 0.08694, 0.00492, 0.0, 0.0, 0.13558, 0.00211, 0.01939, 0.0, 0.0, 0.0, 0.0007, 0.0007, 0.0, 0.0, 0.00141, 0.0007, 0.01569, 0.0, 0.0, 0.0, 0.0, 0.6818, 0.05005],
        "Cluster 9": [0.06158, 0.16117, 0.03079, 0.03523, 0.01134, 0.0026, 0.01782, 0.15699, 0.00236, 0.00759, 0.0231, 0.01559, 0.08732, 0.00128, 0.00636, 0.09935, 0.00832, 0.01982, 0.00665, 0.00494, 0.00771, 0.00315, 0.00429, 0.22465],
        "Cluster 10": [0.01464, 0.31817, 0.01683, 0.26361, 0.02936, 0.00639, 0.0207, 0.02486, 0.00222, 0.00963, 0.00371, 0.00398, 0.18729, 0.00022, 0.00454, 0.00804, 0.00562, 0.01991, 0.01289, 0.00471, 0.00388, 0.00018, 0.00317, 0.03545]
    },
    "z_score_params": {
        "Cluster 0": {
            "mean": 0.307,
            "std": 0.07531
        },
        "Cluster 1": {
            "mean": 0.14785,
            "std": 0.04182
        },
        "Cluster 2": {
            "mean": 0.19199,
            "std": 0.09002
        },
        "Cluster 3": {
            "mean": 0.12225,
            "std": 0.04613
        },
        "Cluster 4": {
            "mean": 0.17487,
            "std": 0.05283
        },
        "Cluster 5": {
            "mean": 0.20254,
            "std": 0.11519
        },
        "Cluster 6": {
            "mean": 0.10155,
            "std": 0.03625
        },
        "Cluster 7": {
            "mean": 0.15926,
            "std": 0.04733
        },
        "Cluster 8": {
            "mean": 0.22881,
            "std": 0.07316
        },
        "Cluster 9": {
            "mean": 0.1604,
            "std": 0.05625
        },
        "Cluster 10": {
            "mean": 0.20057,
            "std": 0.05956
        }
    }
}

