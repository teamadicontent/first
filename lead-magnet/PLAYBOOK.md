# Prospect Lead Magnet Playbook

A free lead magnet of 5–10 ready-to-post LinkedIn posts, written for one prospect and sent with the **4th cold DM**. The same process runs for every prospect.

## Hard rules

1. **No invented stories.** Every story, quote, number, client name and anecdote in a post must trace to a source URL in the prospect's research brief. If there's no source, the post doesn't get written. With no sourced story, write only educational and informative posts.
2. **Nothing gets sent to the prospect by Claude.** The output is the doc plus a DM draft. Souvik edits the DM and adds it to the CRM, and Adi sends it.
3. **One fresh session per prospect** to keep token use low.

## Per-prospect run (input: prospect name + LinkedIn URL)

### 1. Research (budget: 1 Eden credit + ~5–9 web searches)
- **Network note:** this cloud environment blocks direct fetches of linkedin.com and most sites (the browser too). `WebSearch` works and returns source URLs; use it for all web research. Eden is the only way to read LinkedIn posts.
- **Eden credits (~250/month, shared with post writing):** call `eden_analyze_creator` once with `creatorRef {platform: linkedin, username: <slug from URL>}` and `since: year`. A first-time creator returns `indexing`; wait ~15s and call again (the retry didn't appear to cost a second pull). Skip `eden_resolve_creator` when the URL gives the slug.
- **What Eden returns:** `eden_analyze_creator` gives recent posts, standout posts vs. their own baseline, topic and format mix. If the resolution is ambiguous, stop and ask. Use `eden_read_social_post` for full text of 2–3 posts to learn their voice.
- **Web:** company site, podcasts, interviews, articles, press, talks. Record each finding with its URL.
- Write `lead-magnet/prospects/<yyyy-mm-dd>-<name-slug>.md`, containing:
  - Who they are, what they sell, who they sell to
  - Voice notes: length, line breaks, emoji, hooks, formality, recurring phrases
  - Topics they already post about, and gaps
  - **Sourced facts table:** fact, source URL
  - **Sourced stories table:** story summary, source URL. Write "none found" if empty.
  - Tone tag (warm / analytical / bold / punchy / playful)

### 2. Pick templates
- Read `templates/index.md` (not the full library).
- Choose 5–10 templates: all `go` rows are eligible. `found` rows are eligible only when the brief's sourced tables cover that row's "Needs". Never use `skip` rows.
- Mix types (at most 2 of one type), match tone, avoid picking two templates that echo each other.
- Open only the chosen skeletons in `templates/template-library.md`.

### 3. Write and check
- Write each post in the prospect's voice, following the skeleton's mechanic, not its wording.
- Voice pass: does it sound like their posts, not like a template?
- Fact pass: every specific claim in every post maps to a row in the brief. Cut or generalise anything that doesn't. This includes opinions: don't put a take in their mouth that their sources don't support.
- **Voice-guard pass (mandatory, before the doc).** Read the full `05-voice-guard.md` and `05a-ai-tells.md` in the prospect-spec-posts skill references. Fix all P0 and P1 items in every post:
  - Floor: em/en dashes, bold, chatbot phrases, vague attributions, hashtag stuffing, `[placeholders]` inside a post body. Emojis and hashtags are allowed only when the prospect provably uses them (cite the post).
  - Endings: delete slogan/aphorism endings ("X. Y. That's the game.", "You don't need X. You need Y."). End on the last concrete line or a plain question.
  - Hooks: no "The good news?", "The catch?", "Here's what I'm noticing/what stood out", "this one's for you", "And a lot more". Don't start with the first words the guard lists as AI fingerprints (The, How, In, This, Here, As...).
  - At most one X-not-Y line, and only when a real belief is being negated. No self-answered questions. Vary list lengths (not everything in threes).
  - Then run a regex scan for the banned words and patterns, and re-read each post once more (second pass).

### 4. Lead magnet doc
- Build it in the **fixed format** (see "Doc format" below).
- Destination: Google Drive (Google Doc). The Drive tools can't edit a doc's text after creation, so get it right before uploading; a fix means a new doc.

### 5. 4th-touch message (LinkedIn connection request note)
- **Hard limit: 300 characters, including the doc link.** Count with a script every time and state the count. Aim for ≤280 so Souvik has room to edit.
- Link: `docs.google.com/document/d/<id>` (no https://, no /edit), which is about 72 characters, so the text itself gets ~200–220.
- Signal outreach craft rules: line one proves you looked (one specific number or detail from their posts), one idea, the doc as a free gift, soft close. No em dashes, emojis, flattery or "I came across your profile".
- Output it as plain text for Souvik to edit.

### 6. Hand-off and record
- Commit the research brief and a copy of the posts to `lead-magnet/prospects/`.
- Reply with the doc link and the DM text.

## Doc format

_v0 (first used for Ron Schmelzer, 2026-09-28). Adi to edit; the final layout gets recorded here._

Created with `mcp__Google_Drive__create_file`, `contentMimeType: text/html` (converts to a Google Doc). Title: `N LinkedIn Posts for <Full Name>`.

1. H1 `N LinkedIn posts for <Name>` + italic line: written in your voice, built from <their sources>, free to use, edit or ignore.
2. H2 `How these were made`: 2 short paragraphs (what was read, the one-line audit insight; every fact comes from something they published).
3. H2 `At a glance`: numbered list, `<post title> (<format>)`.
4. Per post: H2 `Post N: <title>` · `Format:` + `Why this one:` (1–2 lines tied to their data) · rule · the post, one paragraph per line with blank-line spacers · rule · optional `Image idea:` line (outside the post) · grey small `Source: <source URL>` (label changed by Adi).
5. H2 `A note before you post`: any figures they should double-check.
6. Sign-off: `Put together by Adi, Signal.`
7. Share the doc as "anyone with the link can view" before the DM goes out.

## Files

- `templates/template-library.md`: the full 250-template library (source of truth for skeletons)
- `templates/index.md`: tagged compact index (spec / type / tone / tier / needs)
- `templates/templates.json`: the same data, machine-readable
- `templates/tags.txt`: hand-assigned `type tone spec` per template. To re-tag, edit this, then re-run `parse.py` and the merge step
- `prospects/`: one research brief and post set per prospect
