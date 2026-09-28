#!/usr/bin/env python3
"""Count a LinkedIn connection-request note. Hard limit 300 characters, including the link.

Usage: python3 count_note.py "note text with docs.google.com/document/d/<id>"
"""
import sys
note = " ".join(sys.argv[1:]).strip()
n = len(note)
banned = [c for c in ("—", "–", "!") if c in note]
print(f"{n}/300 characters" + ("  OVER LIMIT" if n > 300 else "  (target 280 or less)" if n > 280 else "  OK"))
if banned:
    print("Contains banned characters:", banned)
sys.exit(1 if n > 300 else 0)
