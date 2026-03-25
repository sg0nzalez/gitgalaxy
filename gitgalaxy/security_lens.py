import re
import copy
import logging
from typing import Dict, Any

# ==============================================================================
# GitGalaxy Security Lens (Passive Threat Observer)
# Protocol: Glassworm, Trojan, and Exfiltration Hunting
# ==============================================================================

class SecurityLens:
    """
    PURPOSE: 
    Acts as a Passive Observer within the GitGalaxy Physics Engine. 
    It runs alongside the standard architectural audit, silently collecting 
    malicious intent, obfuscation, and exfiltration metrics into RAM.
    
    MECHANISM:
    Injects high-priority threat signatures into the primary language rulesets
    using a 'sec_' prefix. This ensures standard metrics (like tech debt) are 
    calculated normally, while security anomalies are passively cached for later extraction.
    """

    def __init__(self, parent_logger: logging.Logger = None):
        self.logger = parent_logger.getChild("security_lens") if parent_logger else logging.getLogger("security_lens")
        self.logger.setLevel(logging.INFO)

        # ======================================================================
        # THE THREAT REGISTRY (Security Overlay V2 - O(N) Safe)
        # ======================================================================
        self.THREAT_SIGNATURES = {
            # ------------------------------------------------------------------
            # 1. THE GLASSWORM (Obfuscation & Heat Signatures)
            # Targets decoding functions, massive blobs, and invisible steganography.
            # ------------------------------------------------------------------
            "heat_triggers": re.compile(
                r'\b(?:atob|btoa|base64_decode|base64_encode|gzuncompress|str_rot13)\b|'
                r'\\x[0-9a-fA-F]{2}|\\u[0-9a-fA-F]{4}|'
                r'(?:\w{15,}[ \t]*=[ \t]*["\'][A-Za-z0-9+/]{40,}={0,2}["\'])|'
                r'[\u200B-\u200D\uFEFF\u200E\u200F\u202A-\u202E]', # Invisible Unicode
                re.I
            ),

            # ------------------------------------------------------------------
            # 2. THE TROJAN (Identity Masking & Safety Bypasses)
            # Targets cross-algorithm double-decoding and runtime security downgrades.
            # ------------------------------------------------------------------
            "safety_neg": re.compile(
                r'\b(?:atob|btoa|base64_decode|gzinflate|gzuncompress|str_rot13|urldecode)[ \t]*\([ \t]*(?:atob|btoa|base64_decode|gzinflate|gzuncompress|str_rot13|urldecode)\b|'
                r'\b(?:auto_prepend_file|auto_append_file)\b|'
                r'\b(?:ini_set|ini_restore|putenv)[ \t]*\([ \t]*["\'](?:disable_functions|safe_mode|open_basedir|allow_url_fopen)["\'][ \t]*,[ \t]*["\']?(?:0|off|false|)["\']?\)|'
                r'\b(?:disable_functions|safe_mode|open_basedir)\b[ \t]*=[ \t]*(?:off|0|false|""|\'\')|'
                r'process\.env\.NODE_TLS_REJECT_UNAUTHORIZED[ \t]*=[ \t]*["\']?0["\']?|'
                r'\b(?:verify|strictSSL|rejectUnauthorized|CURLOPT_SSL_VERIFYPEER)[ \t]*[=:,][ \t]*(?:False|false|0)\b',
                re.I
            ),

            # ------------------------------------------------------------------
            # 3. EXFILTRATION VECTORS (System Gravity)
            # Targets dynamic outbound connections, tunneling proxies, and DNS exfiltration.
            # ------------------------------------------------------------------
            "io": re.compile(
                r'\b(?:fetch|XMLHttpRequest|WebSocket|http\.request|https\.request|requests\.(?:post|put|get)|urllib\.request\.urlopen)\b\s*\(|'
                r'\b(?:curl_exec|fsockopen|pfsockopen|stream_socket_client|file_get_contents)\b\s*\(|'
                r'\b(?:dns_get_record|gethostbyname|socket\.gethostbyname|resolve(?:4|6|Cname|Txt)?)\b\s*\(|'
                r'(?:https?|ftp|tcp|udp|wss?):\/\/(?:(?:\d{1,3}\.){3}\d{1,3}|\[[0-9a-fA-F:]+\]|.*?\.(?:ngrok\.io|ngrok-free\.app|localtunnel\.me|pastebin\.com|workers\.dev|s3\.amazonaws\.com|requestbin\.net|pipedream\.net))',
                re.I | re.X
            ),

            # ------------------------------------------------------------------
            # 4. THE EXECUTIONER (Dynamic Payloads)
            # HARDENED: Unbounded repetitions clamped to prevent ReDoS on minified code.
            # ------------------------------------------------------------------
            "danger": re.compile(
                r'\b(?:eval|Function|setTimeout|setInterval)\b\s*\(\s*(?:atob|base64|["\']|`)|'
                r'\b(?:document\.write|location\.replace|assert|create_function|passthru|shell_exec|system)\b|'
                r'child_process\.(?:exec|spawn|fork)|'
                # Clamped string concatenation to {1,15} to kill exponential backtracking
                r'(?:window|global|this|globalThis)\[[ \t]*(?:["\'][a-zA-Z]["\'][ \t]*\+[ \t]*){1,15}["\'][a-zA-Z]["\'][ \t]*\][ \t]*\(|'
                r'\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*\s*\(\s*\$_(?:POST|GET|COOKIE|REQUEST|HEADERS)|'
                r'getattr\s*\(\s*__import__\s*\(|__builtins__\[|Assembly\.Load\s*\(',
                re.I | re.X
            ),

            # ------------------------------------------------------------------
            # 5. ENVIRONMENT POISONING (State Flux)
            # Targets prototype pollution, native function hooking, and global overrides.
            # ------------------------------------------------------------------
            "flux": re.compile(
                r'\b[A-Za-z0-9_]+\.prototype\.[A-Za-z0-9_]+[ \t]*=|'
                r'\.__proto__[ \t]*=[ \t]*[{a-zA-Z]|'
                r'\b(?:window|global|globalThis|document)\.(?:fetch|eval|setTimeout|setInterval|Promise|console|JSON)[ \t]*=|'
                r'\$(?:GLOBALS|_(?:SERVER|GET|POST|COOKIE|REQUEST|ENV|SESSION))\[[^\]]+\][ \t]*=[ \t]*[^=]|'
                r'\bextract[ \t]*\([ \t]*\$(?:_(?:GET|POST|REQUEST|COOKIE)|GLOBALS)\b|'
                r'\b__builtins__\[[^\]]+\][ \t]*=|'
                r'\bsys\.modules\[[^\]]+\][ \t]*=',
                re.I
            ),

            # ------------------------------------------------------------------
            # 6. SHADOW LOGIC (Necrosis / Graveyard)
            # O(N) SAFE: Fast block scanning bounded to 500 chars to prevent ReDoS.
            # ------------------------------------------------------------------
            "graveyard": re.compile(
                r'(?://|#|--)[^\n]*?\b(?:http|bash|curl|wget|eval|base64|nc\s+-e|/dev/tcp)\b|'
                r'/\*(?:(?!\*/).){0,500}?\b(?:http|bash|curl|wget|eval|base64|nc\s+-e|/dev/tcp)\b',
                re.I
            ),
            
            # ------------------------------------------------------------------
            # 7. SUB-ATOMIC DECRYPTION (Bitwise Hits)
            # HARDENED: Replaced .*? with bounded character exclusions. 
            # ------------------------------------------------------------------
            "bitwise_hits": re.compile(
                # Clamped to {2,20} and {3,20} to prevent infinite runaway loops on data arrays
                r'\b\w+[ \t]*=[ \t]*(?:\w+[ \t]*\^[ \t]*\w+[ \t]*){2,20}|'
                r'(?:\w+\[[^\]\n]{1,50}\][ \t]*\^[ \t]*=?[ \t]*(?:0x[0-9a-fA-F]+|\d+|\w+)[ \t]*;[ \t]*){3,20}', 
                re.I
            ),
            # ------------------------------------------------------------------
            # 8. SHADOW IMPORTS (The Switcharoo / Steganography)
            # Targets legitimate code attempting to import, require, or execute
            # payloads hidden inside non-executable media or data files.
            # ------------------------------------------------------------------
            "shadow_imports": re.compile(
                r'\b(?:require|include|import|require_once|include_once|source|load|dofile)\b\s*\(?\s*'
                r'["\'][^"\']+\.(?:png|jpg|jpeg|gif|ico|pdf|zip|tar|dat|tmp|log|txt|csv|wav|mp3)["\']',
                re.I
            ),
            # ------------------------------------------------------------------
            # 9. UNICODE SMUGGLING (Homoglyphs & Typosquatting)
            # Targets look-alike characters (Cyrillic, Greek, Hangul Filler) 
            # used to hijack legitimate imports or disguise network requests.
            # ------------------------------------------------------------------
            "homoglyphs": re.compile(
                r'\b(?:import|from|require|include|require_once|fetch|XMLHttpRequest)\b'
                r'[^\n]*?(?:[\u0400-\u04FF]|'       # Cyrillic (e.g., false 'a', 'e', 'o')
                r'[\u0370-\u03FF]|'                 # Greek
                r'[\u1D400-\u1D7FF]|'               # Math Alphanumerics
                r'\u3164)',                         # Hangul Filler (Invisible whitespace)
                re.I
            ), 
            # ------------------------------------------------------------------
            # 10. THE VAULT DOOR (Credential & Secret Leaks)
            # Universal RHS-aware secret detection. Demands string literals 
            # of at least 16 characters to prevent false positives on booleans/ints.
            # ------------------------------------------------------------------
            "private_info": re.compile(
                r"\b(password|secret|token|api[_-]?key|client[_-]?secret|credentials|private[_-]?key|auth[_-]?token)\b[ \t]*(?:[:=]|=>)[ \t]*[\"'][A-Za-z0-9\-_+/=]{16,}[\"']",
                re.I
            ),
        }
        
    def arm_lens(self, base_registry: Dict[str, Any], target_languages: list = None) -> Dict[str, Any]:
        """
        Injects the threat signatures as PASSIVE OBSERVERS into the registry.
        They will be scanned by the Splicer and cached in RAM, but will NOT destroy 
        the standard architectural calculations.
        """
        self.logger.info("Arming Security Lens: Injecting Passive Observers into Registry...")
        
        secure_registry = copy.deepcopy(base_registry)
        
        if not target_languages:
            target_languages = ['javascript', 'typescript', 'php', 'python', 'ruby', 'shell', 'powershell']

        for lang in target_languages:
            if lang in secure_registry and 'rules' in secure_registry[lang]:
                rules = secure_registry[lang]['rules']
                
                # --- PASSIVE OBSERVER INJECTION ---
                for dimension, threat_regex in self.THREAT_SIGNATURES.items():
                    # By prefixing with "sec_", we preserve the original "io" or "danger" rules
                    # The Splicer automatically scans any key in this dictionary, meaning
                    # these hits will quietly accumulate in the file's 'equations' output in RAM.
                    rules[f"sec_{dimension}"] = threat_regex
                    
                self.logger.debug(f"Passive Security Sensors attached to '{lang}'.")

        self.logger.info(f"Passive Security Lens active across {len(target_languages)} ecosystems.")
        return secure_registry