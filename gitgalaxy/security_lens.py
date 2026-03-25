import re

class SecurityLens:
    """
    The GitGalaxy Physics Engine for Threat Detection.
    Measures raw structural realities (Regex Hits) and compares them 
    against dynamically injected Policy Thresholds.
    """
    
    def __init__(self, policy=None):
        # ------------------------------------------------------------------
        # DYNAMIC POLICY INJECTION
        # The lens no longer makes the rules. It receives its thresholds 
        # from gitgalaxy_standards.ThreatPolicy. If none is provided, it 
        # defaults to a safe baseline.
        # ------------------------------------------------------------------
        self.policy = policy or {
            "secrets_risk_threshold": 0.001,
            "hidden_malware_threshold": 0.60,
            "logic_bomb_threshold": 0.50,
            "injection_surface_threshold": 0.65,
            "memory_corruption_threshold": 0.60
        }

        # ------------------------------------------------------------------
        # RAW SENSORS (The Physics Engine)
        # These remain untouched. They strictly measure structural reality.
        # ------------------------------------------------------------------
        self.THREAT_SIGNATURES = {
            # 1. THE GLASSWORM (Obfuscation & Heat Signatures)
            "heat_triggers": re.compile(
                r'\b(?:atob|btoa|base64_decode|base64_encode|gzuncompress|str_rot13)\b|'
                r'\\x[0-9a-fA-F]{2}|\\u[0-9a-fA-F]{4}|'
                r'(?:\w{15,}[ \t]*=[ \t]*["\'][A-Za-z0-9+/]{40,}={0,2}["\'])|'
                r'[\u200B-\u200D\uFEFF\u200E\u200F\u202A-\u202E]', # Invisible Unicode
                re.I
            ),

            # 2. THE TROJAN (Identity Masking & Safety Bypasses)
            "safety_neg": re.compile(
                r'\b(?:atob|btoa|base64_decode|gzinflate|gzuncompress|str_rot13|urldecode)[ \t]*\([ \t]*(?:atob|btoa|base64_decode|gzinflate|gzuncompress|str_rot13|urldecode)\b|'
                r'\b(?:auto_prepend_file|auto_append_file)\b|'
                r'\b(?:ini_set|ini_restore|putenv)[ \t]*\([ \t]*["\'](?:disable_functions|safe_mode|open_basedir|allow_url_fopen)["\'][ \t]*,[ \t]*["\']?(?:0|off|false|)["\']?\)|'
                r'\b(?:disable_functions|safe_mode|open_basedir)\b[ \t]*=[ \t]*(?:off|0|false|""|\'\')|'
                r'process\.env\.NODE_TLS_REJECT_UNAUTHORIZED[ \t]*=[ \t]*["\']?0["\']?|'
                r'\b(?:verify|strictSSL|rejectUnauthorized|CURLOPT_SSL_VERIFYPEER)[ \t]*[=:,][ \t]*(?:False|false|0)\b',
                re.I
            ),

            # 3. EXFILTRATION VECTORS (System Gravity)
            "io": re.compile(
                r'\b(?:fetch|XMLHttpRequest|WebSocket|http\.request|https\.request|requests\.(?:post|put|get)|urllib\.request\.urlopen)\b\s*\(|'
                r'\b(?:curl_exec|fsockopen|pfsockopen|stream_socket_client|file_get_contents)\b\s*\(|'
                r'\b(?:dns_get_record|gethostbyname|socket\.gethostbyname|resolve(?:4|6|Cname|Txt)?)\b\s*\(|'
                r'(?:https?|ftp|tcp|udp|wss?):\/\/(?:(?:\d{1,3}\.){3}\d{1,3}|\[[0-9a-fA-F:]+\]|.*?\.(?:ngrok\.io|ngrok-free\.app|localtunnel\.me|pastebin\.com|workers\.dev|s3\.amazonaws\.com|requestbin\.net|pipedream\.net))',
                re.I | re.X
            ),

            # 4. THE EXECUTIONER (Dynamic Payloads)
            "danger": re.compile(
                r'\b(?:eval|Function|setTimeout|setInterval)\b\s*\(\s*(?:atob|base64|["\']|`)|'
                r'\b(?:document\.write|location\.replace|assert|create_function|passthru|shell_exec|system)\b|'
                r'child_process\.(?:exec|spawn|fork)|'
                r'(?:window|global|this|globalThis)\[[ \t]*(?:["\'][a-zA-Z]["\'][ \t]*\+[ \t]*){1,15}["\'][a-zA-Z]["\'][ \t]*\][ \t]*\(|'
                r'\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*\s*\(\s*\$_(?:POST|GET|COOKIE|REQUEST|HEADERS)|'
                r'getattr\s*\(\s*__import__\s*\(|__builtins__\[|Assembly\.Load\s*\(',
                re.I | re.X
            ),

            # 5. ENVIRONMENT POISONING (State Flux)
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

            # 6. SHADOW LOGIC (Necrosis / Graveyard)
            "graveyard": re.compile(
                r'(?://|#|--)[^\n]*?\b(?:http|bash|curl|wget|eval|base64|nc\s+-e|/dev/tcp)\b|'
                r'/\*(?:(?!\*/).){0,500}?\b(?:http|bash|curl|wget|eval|base64|nc\s+-e|/dev/tcp)\b',
                re.I
            ),
            
            # 7. SUB-ATOMIC DECRYPTION (Bitwise Hits)
            "bitwise_hits": re.compile(
                r'\b\w+[ \t]*=[ \t]*(?:\w+[ \t]*\^[ \t]*\w+[ \t]*){2,20}|'
                r'(?:\w+\[[^\]\n]{1,50}\][ \t]*\^[ \t]*=?[ \t]*(?:0x[0-9a-fA-F]+|\d+|\w+)[ \t]*;[ \t]*){3,20}', 
                re.I
            ),
            
            # 8. SHADOW IMPORTS (The Switcharoo / Steganography)
            "shadow_imports": re.compile(
                r'\b(?:require|include|import|require_once|include_once|source|load|dofile)\b\s*\(?\s*'
                r'["\'][^"\']+\.(?:png|jpg|jpeg|gif|ico|pdf|zip|tar|dat|tmp|log|txt|csv|wav|mp3)["\']',
                re.I
            ),
            
            # 9. UNICODE SMUGGLING (Homoglyphs & Typosquatting)
            "homoglyphs": re.compile(
                r'\b(?:import|from|require|include|require_once|fetch|XMLHttpRequest)\b'
                r'[^\n]*?(?:[\u0400-\u04FF]|'       
                r'[\u0370-\u03FF]|'                 
                r'[\u1D400-\u1D7FF]|'               
                r'\u3164)',                         
                re.I
            ), 
            
            # 10. THE VAULT DOOR (Credential & Secret Leaks)
            "private_info": re.compile(
                r"\b(password|secret|token|api[_-]?key|client[_-]?secret|credentials|private[_-]?key|auth[_-]?token)\b[ \t]*(?:[:=]|=>)[ \t]*[\"'][A-Za-z0-9\-_+/=]{16,}[\"']",
                re.I
            ),
            
            # 11. RAW MEMORY OVERRIDES (From previous context)
            "memory_corruption": re.compile(
                r'\b(?:malloc|calloc|realloc|free|memcpy|memset|memmove|strcpy|strcat|sprintf)\b\s*\(|'
                r'\b(?:asm|__asm__|__asm)\b\s*[\(\{]',
                re.I
            )
        }

    def scan_content(self, file_content, total_loc):
        """
        Scans raw text and returns the raw hits for the engine to aggregate.
        """
        hits = {key: len(pattern.findall(file_content)) for key, pattern in self.THREAT_SIGNATURES.items()}
        return hits

    def evaluate_risk(self, aggregated_hits, total_loc):
        """
        Takes the raw physics hits, calculates the density, and checks 
        if it breaches the dynamically injected policy thresholds.
        """
        # Prevent division by zero
        loc_safe = total_loc if total_loc > 0 else 1
        
        exposures = {}
        
        # 1. Hidden Malware Risk (Combines heat, bitwise math, and shadow imports)
        malware_hits = aggregated_hits.get("heat_triggers", 0) + aggregated_hits.get("bitwise_hits", 0) + aggregated_hits.get("shadow_imports", 0) + aggregated_hits.get("homoglyphs", 0)
        malware_density = malware_hits / loc_safe
        if malware_density >= self.policy["hidden_malware_threshold"]:
            exposures["Hidden Malware Risk"] = malware_density

        # 2. Logic Bomb / Sabotage Risk
        sabotage_hits = aggregated_hits.get("graveyard", 0) + (aggregated_hits.get("danger", 0) * 1.5)
        sabotage_density = sabotage_hits / loc_safe
        if sabotage_density >= self.policy["logic_bomb_threshold"]:
            exposures["Logic Bomb Risk"] = sabotage_density

        # 3. Data Injection Risk
        injection_hits = aggregated_hits.get("io", 0) + aggregated_hits.get("danger", 0) + aggregated_hits.get("flux", 0)
        injection_density = injection_hits / loc_safe
        if injection_density >= self.policy["injection_surface_threshold"]:
            exposures["Data Injection Risk"] = injection_density

        # 4. Memory Corruption Risk
        memory_hits = aggregated_hits.get("memory_corruption", 0)
        memory_density = memory_hits / loc_safe
        if memory_density >= self.policy["memory_corruption_threshold"]:
            exposures["Memory Corruption Risk"] = memory_density

        # 5. Secrets Risk (Highly sensitive)
        secrets_hits = aggregated_hits.get("private_info", 0)
        secrets_density = secrets_hits / loc_safe
        if secrets_density >= self.policy["secrets_risk_threshold"]:
            exposures["Secrets Leak Risk"] = secrets_density

        return exposures