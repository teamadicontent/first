#!/usr/bin/env python3
"""Scan finished posts for Signal voice-guard tells before they go in the doc.

Usage: python3 guard_scan.py posts.json
posts.json: {"posts": [{"title": "...", "body": "..."}, ...]} (same file build_doc.py reads)

Prints hits per post. Any hit must be fixed or consciously kept with evidence
from the prospect's own posts (emoji, hashtags). Exit code 1 if any floor hit.
"""
import json, re, sys

FLOOR = {  # Layer 1: never allowed
    "em/en dash": r"[—–]| -- ",
    "bold markdown": r"\*\*",
    "placeholder": r"\[[^\]]*\]|XX|TODO|DETAIL NEEDED",
    "chatbot phrase": r"(?i)i hope this|great question|certainly!|feel free to|let me know if|as an ai",
    "vague attribution": r"(?i)\b(experts (say|believe)|studies show|research suggests)\b",
}
P1 = {  # obvious AI smell: fix unless there is a clear reason
    "tier-1 word": r"(?i)\b(delve|landscape|tapestry|realm|paradigm|embark|beacon|testament|robust|comprehensive|cutting-edge|pivotal|underscores?|meticulous\w*|seamless\w*|game.chang\w*|utiliz\w*|vibrant|thriving|showcas\w*|deep dive|dive into|unpack\w*|holistic\w*|actionable|impactful|learnings|synerg\w*|journey|elevate|supercharge|unlock\w*|empower\w*|streamline\w*|foster\w*|resonat\w*|navigat\w*|crucial)\b",
    "leverage as verb": r"(?i)\bleverag(e|es|ed|ing) (the|your|our|their|ai|it|this)\b",
    "x-not-y": r"(?i)(isn't about|is not about|not just\b|it's not (a|the)\b|you don't need .{0,40}\. you need|less about .{0,30} more about|doesn't mean .{0,30}\. it means)",
    "infomercial hook": r"(?i)\b(the good news\?|the catch\?|the kicker\?|the result\?|the best part\?|plot twist|here's the thing|here's what (i'm noticing|stood out|caught|nobody)|what nobody tells you|let that sink in|read that again)",
    "endorsement closer": r"(?i)(this one's for you|worth (a look|reading|your time|checking|exploring)|must-read|bookmark this|don't sleep on|thank me later|and a lot more|and so much more)",
    "empty framing": r"(?i)(it's worth noting|at the end of the day|in today's|in the age of|at its core|the reality is|the truth is|let's dive|in a nutshell|buckle up|here's the deal|the bottom line)",
    "intensifier": r"(?i)\b(genuinely|truly|quite frankly|to be honest)\b",
}
FINGERPRINT_FIRST = {"the","how","in","this","here","as","yes","sure","to","creating","certainly","from","according","based","my","while","step","introduction","comprehensive","title"}

def scan(body):
    hits = []
    for k, p in FLOOR.items():
        for m in re.finditer(p, body):
            hits.append(("FLOOR", k, m.group(0)))
    for k, p in P1.items():
        for m in re.finditer(p, body):
            hits.append(("P1", k, m.group(0)))
    first = re.sub(r"^[\"'“]+", "", body.strip()).split()[0].lower().strip(",.:;!?\"'")
    if first in FINGERPRINT_FIRST:
        hits.append(("P1", "AI first word", first))
    tags = re.findall(r"#\w+", body)
    if len(tags) > 3:
        hits.append(("FLOOR" if len(tags) >= 6 else "P1", "hashtags", str(len(tags))))
    q = body.count("?")
    if q > 2:
        hits.append(("P2", "question count", str(q)))
    emoji = re.findall(r"[\U0001F000-\U0001FAFF☀-➿]", body)
    if emoji:
        hits.append(("CHECK", "emoji (allowed only if prospect uses them)", "".join(emoji)))
    return hits

data = json.load(open(sys.argv[1]))
floor = False
for i, p in enumerate(data["posts"], 1):
    hits = scan(p["body"])
    words = len(p["body"].split())
    print(f"Post {i}: {p['title']} ({words} words)")
    for sev, k, s in hits:
        floor |= sev == "FLOOR"
        print(f"   {sev:5} {k}: {s!r}")
    if not hits:
        print("   clean")
sys.exit(1 if floor else 0)
