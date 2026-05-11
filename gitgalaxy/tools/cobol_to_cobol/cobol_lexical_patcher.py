#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: Lexical Patcher (Pre-Processor)
# Purpose: Neutralizes legacy COBOL structural traps by restructuring them into 
#          modern equivalents, protected by a Dialect Sensor to prevent 0C1 crashes.
# ==============================================================================
import re
from pathlib import Path

def detect_cobol_dialect(content: str) -> str:
    """
    Scans for post-1974 structural keywords to determine the compiler era.
    """
    # COBOL-85 introduced explicit scope terminators, EVALUATE, INITIALIZE, and inline comments (*>)
    modern_signatures = re.compile(
        r'\b(EVALUATE|INITIALIZE|END-IF|END-PERFORM|END-READ|END-EVALUATE|CONTINUE)\b|\*>', 
        re.IGNORECASE
    )
    
    if modern_signatures.search(content):
        return "COBOL-85"
    return "COBOL-74"

def patch_lexical_traps(filepath: Path) -> bool:
    """
    Scans the file for NEXT SENTENCE. If found, rewrites it safely based on the compiler dialect.
    Returns True if the file was modified, False otherwise.
    """
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        print(f"Error reading {filepath.name}: {e}")
        return False

    # Fast check before engaging heavy regex
    if not re.search(r'\bNEXT\s+SENTENCE\b', content, re.IGNORECASE):
        return False

    # 1. Sense the Environment
    dialect = detect_cobol_dialect(content)

    # 2. Apply Era-Appropriate Patches
    if dialect == "COBOL-85":
        # Safe to use modern block-scoped CONTINUE and inline comments
        patched_content = re.sub(
            r'\bNEXT\s+SENTENCE\b', 
            'CONTINUE *> GitGalaxy Patch: Neutralized Lexical Trap', 
            content, 
            flags=re.IGNORECASE
        )
        print(f"   ↳ [!] {dialect} Detected: Safely upgraded NEXT SENTENCE to CONTINUE.")
    else:
        # COBOL-74 Strict Mode: We must leave it as NEXT SENTENCE to prevent compiler strokes.
        # We rewrite it cleanly to ensure standard spacing for the AST slicer, but NO modern syntax.
        patched_content = re.sub(
            r'\bNEXT\s+SENTENCE\b', 
            'NEXT SENTENCE', 
            content, 
            flags=re.IGNORECASE
        )
        print(f"   ↳ [!] {dialect} Detected: Engaged ultra-conservative punch-card mode. Bypassing modern injection.")

    # Save the sanitized code back to the file if changes were made
    if content != patched_content:
        filepath.write_text(patched_content, encoding='utf-8')
        return True
        
    return False