#!/usr/bin/env python3
"""Build the lead-magnet Google Doc HTML from posts.json (fixed doc format).

Usage: python3 build_doc.py posts.json out.html

posts.json:
{
  "name": "Ron Schmelzer",
  "built_from": "your podcast, newsletter, Forbes column and posts",
  "how_made": ["paragraph 1", "paragraph 2"],
  "posts": [
    {"title": "...", "format": "...", "why": "...", "body": "post text, \\n between lines",
     "image": "optional image idea", "source": "url(s)"}
  ],
  "note": "figures they should double-check (optional)",
  "signoff": "Put together by Adi, Signal."
}
Upload the output with Google Drive create_file, contentMimeType text/html (converts to a Google Doc).
"""
import html, json, sys
d = json.load(open(sys.argv[1])); e = html.escape; P = d["posts"]
h = ['<html><body style="font-family:Arial">',
     f'<h1>{len(P)} LinkedIn posts for {e(d["name"])}</h1>',
     f'<p><i>Written in your voice, built from {e(d["built_from"])}. Free to use, edit or ignore.</i></p>',
     '<h2>How these were made</h2>'] + [f'<p>{e(x)}</p>' for x in d["how_made"]]
h += ['<h2>At a glance</h2><ol>'] + [f'<li>{e(p["title"])} ({e(p["format"])})</li>' for p in P] + ['</ol>']
for i, p in enumerate(P, 1):
    h += [f'<h2>Post {i}: {e(p["title"])}</h2>',
          f'<p><b>Format:</b> {e(p["format"])}<br><b>Why this one:</b> {e(p["why"])}</p>', '<hr>']
    h += [f'<p>{e(l) if l.strip() else "&nbsp;"}</p>' for l in p["body"].split("\n")]
    h += ['<hr>']
    if p.get("image"):
        h.append(f'<p><b>Image idea:</b> {e(p["image"])}</p>')
    h.append(f'<p style="color:#666"><small>Source: {e(p["source"])}</small></p>')
if d.get("note"):
    h += ['<h2>A note before you post</h2>', f'<p>{e(d["note"])}</p>']
h += [f'<p>{e(d.get("signoff", "Put together by Adi, Signal."))}</p>', '</body></html>']
open(sys.argv[2], "w").write("\n".join(h))
print(f"wrote {sys.argv[2]} ({len(P)} posts)")
