---
name: prospect-lead-magnet
description: Signal's end-to-end cold-outreach lead magnet. From a prospect's LinkedIn profile link, or an intake doc (name, headline, website, About, 10 posts), it researches the prospect, picks 5 to 10 fitting templates from the 250-template library, writes sourced posts in their voice, runs the Signal voice guard and editor, publishes a Google Doc in the fixed format, and writes a connection-request note of 300 characters or fewer (link included) for the 4th outreach touch. Use whenever someone sends a prospect's LinkedIn URL or prospect details and asks for the lead magnet, spec posts, sample posts, posts for outreach, the 4th DM, or says "run the process" or "do this prospect".
---

# Prospect Lead Magnet

**Goal:** the prospect opens the doc and thinks "that sounds like me, and I haven't written that yet." Getting the voice and the facts right matters more than being clever. A prospect spots a made-up story or a wrong number instantly, and then the outreach is dead.

**Deliverables** (every run):
1. A Google Doc with 5 to 10 ready-to-post LinkedIn posts, in the fixed format.
2. A LinkedIn connection-request note for the 4th touch: **300 characters or fewer, including the doc link.**
3. A short hand-off note: the editor scores, gaps the prospect would have to fill, and figures to double-check.

Claude never sends anything to the prospect. Souvik edits the note and adds it to the CRM, and Adi sends it.

## Hard rules

1. **No invented stories.** Every story, quote, number, name and anecdote must trace to a source URL (or to one of the prospect's own posts). If there's no source, the post doesn't get written. With no sourced story, write only educational, insight, contrarian and framework posts.
2. **No invented stances.** Don't put an opinion, prediction or piece of advice in their mouth that their sources don't support. If a template needs one, pick a different template.
3. **No placeholders inside a post.** A gap only the prospect can fill goes in the doc's "A note before you post" section. Better still, pick a template the facts already support.
4. **Signal house style:** no em dashes, en dashes or " -- ", no bold in post bodies. Emojis and hashtags are allowed only when the prospect's own posts show them (match their choice and count, at most 3 hashtags).

## Inputs: two modes

- **Mode A: LinkedIn URL.** Research LinkedIn through Eden (costs 1 credit) plus web search.
- **Mode B: intake doc** (name, headline, website, About, 10 posts, ideally with dates and reactions). Pasted text, an uploaded file or a Google Doc link (read it with Google Drive `read_file_content`). **Don't spend an Eden credit.** The posts supplied are the voice sample, so only run web searches for facts and stories.
- If the input is thinner than both modes, show `assets/intake-template.md` and ask once. Otherwise go.

## Environment facts (learned the hard way)

- Cloud sessions usually block direct fetches of linkedin.com and most websites, including the browser. **WebSearch works** and returns source URLs, so do all web research through it. If a fetch is blocked, don't retry it.
- **Eden credits are scarce** (about 250 a month, shared with other work). Use exactly one profile pull per Mode A prospect.
- **Google Drive tools can create a doc but can't edit its text afterwards.** Get the posts right before uploading. A fix means uploading a new doc, then renaming the old one "(old draft)". Never delete a doc the user may have edited: check `modifiedTime` against `createdTime` first.

## Step 1: Research (budget: 1 Eden credit in Mode A, 5 to 9 web searches)

**Mode A, Eden:** load the Eden tools with ToolSearch, then:
- Call `eden_analyze_creator` with `query` set to the URL, `creatorRef {platform: "linkedin", username: <slug from the URL>}`, `since: "year"` and `topPostLimit: 8`.
- If Eden returns `indexing` (it's pulling this creator for the first time), wait about 15 seconds and call it once more. A `not-found` timeout is temporary, so retry once.
- Creator-scoped `eden_search_social_content` reads the posts Eden already pulled. Use `eden_read_social_post` only when a post body was cut off and you need it.
- From Eden, take: the bio, follower count, the posts that did best against their own average, what their typical post gets, hashtags, formats, and 3 to 5 sample posts for voice.

**Web search (both modes)** covers the company or website, podcasts, newsletter, interviews, articles and press, talks, career history, the frameworks they've named and recent news. Record every fact with its URL.

**Write the research brief** using `assets/brief-template.md`. The parts that matter:
- **Voice notes**, each with a quoted line from their posts as evidence: opening move, length, register, recurring phrases, emoji, hashtags, lists and close. See `references/02-voice-archetypes.md` if the voice is unclear.
- **Audit:** 2 to 3 observations using `references/01-outreach-audit.md` Part 1 (recency, the substitution test, a voice check, the "buried asset", engagement vs audience). They must be specific enough that only someone who looked could write them, because they feed the note.
- **Sourced facts table** and **sourced stories table**. Write "None found" if there are none; that's normal.
- **Covered list:** what they've already posted, so you don't repeat it.

If you're working inside a repository that has `lead-magnet/prospects/`, save the brief as `lead-magnet/prospects/<yyyy-mm-dd>-<name-slug>.md`, then commit and push.

## Step 2: Pick templates

1. Read `references/template-index.md`, not the full library. Its tags:
   - **spec**
     - `go`: can be written from public research.
     - `found`: usable only if your sourced tables cover that row's "Needs".
     - `skip`: promotional (launches, events, giveaways, testimonials). Never used.
   - **type:** story, proof, case, about, contrarian, insight, educational, news, curation, promo.
   - **tone:** warm, analytical, bold, punchy, playful.
2. Choose 5 to 10 templates:
   - At most 2 of any one type.
   - Match their tone.
   - At least one connected to where they're heading next.
   - Built from their buried asset, not general industry knowledge.
   - Not on the covered list.
   - Not two templates the library's **Note:** line marks as echoes of each other.
3. Open only the chosen skeletons in `references/template-library.md` (search for `## <ID> —`).

A good default mix: one post that turns their own numbers into a contrarian take, one satire or meme post if they're funny, one list of examples from their own material, one post built around a guest quote from their podcast or interview, one framework post if they've named a framework, and one news or prediction post built from their own recent article.

## Step 3: Write

- Follow each skeleton's **mechanic**, not its wording. Their rhythm wins on sentence length, lists and the close.
- **Length:** match their typical post. Most land at 80 to 160 words, and some prospects write 1 to 3 lines.
- **Hook:** make the first ~140 characters work before LinkedIn's "See more" cut-off.
- **Numbers:** use past tense for historical figures, e.g. "reached 900M users", never a present-tense stale number.
- If their bio claims something the sources don't cover (for example "triple exit" with only two found), don't fill the gap. Note it for the prospect.

## Step 4: Voice guard (mandatory)

Read `references/05-voice-guard.md` and `references/05a-ai-tells.md`, and use the `linkedin` profile in `references/05b-profiles.md`. The prospect's real voice is what you're matching, and the guard's hard rules apply on top of it. Fix every P0 and P1 item. These are the ones that slipped through before:

- **Slogan or aphorism endings** ("Small team. Big scale.", "You don't need to predict the future. You need to..."). Delete them and end on the last concrete line or a plain question.
- **Stock hooks:** "The good news?", "Here's what I'm noticing:", "this one's for you", "And a lot more."
- **AI first words:** don't open with The, How, In, This, Here or As.
- **Self-answered questions, X-not-Y lines** (more than one, or aimed at a strawman), and lists that always come in threes.

Then run the scanner:

```
python3 scripts/guard_scan.py posts.json
```

Fix every FLOOR and P1 hit. A CHECK hit (emoji) stays only if their posts show that habit. Re-read every post once more after fixing: tells creep back in during rewrites.

## Step 5: Editor pass

Run `references/06-editor.md` on every post internally. Load `06-what-survives-filler.md` and `06-loops.md`, check facts with `06-fact-check.md`, and calibrate with `06-worked-example.md`.

- Score each post 1 to 5 on Loops (every hook or question the post opens gets answered), Structure, Readability and Voice match, then make the call: Publish, Revise or Kill.
- Apply the fixes. A post with Voice match or Structure below 4, or a Kill call, gets rewritten or swapped for a different template. Re-run steps 4 and 5 on it.
- Only publish posts called **Publish**, or **Revise** when the only open item is a gap the prospect has to fill (noted in the doc).
- The usual problems: pre-announcing the evidence, restating a list after it, sentences that change grammar partway through a list, "Most founders..." claims with nothing specific in them, and prescriptions the prospect never made.

## Step 6: Build the Google Doc (fixed format)

Write `posts.json` in the structure shown at the top of `scripts/build_doc.py`, then build and upload:

```
python3 scripts/build_doc.py posts.json doc.html
```

Upload with Google Drive `create_file`, `title: "<N> LinkedIn Posts for <Full Name>"`, `contentMimeType: "text/html"`, and the HTML as `textContent`. Confirm with `get_file_metadata` that `fileSize` is not 1 and the snippet shows the title.

Doc format, v1 (Adi will restyle it later; follow the latest version recorded in the repo's `lead-magnet/PLAYBOOK.md` if one exists):
1. **Title:** `<N> LinkedIn posts for <Name>`, then an italic line: "Written in your voice, built from <their sources>. Free to use, edit or ignore."
2. **How these were made:** 2 short paragraphs covering what was read, the one-line audit insight, and that every fact comes from something they published.
3. **At a glance:** a numbered list of `<post title> (<format>)`.
4. **Each post:**
   - `Post N: <title>`
   - "Format:" and "Why this one:" (1 to 2 lines tied to their own data)
   - a rule, the post itself, a rule
   - an optional "Image idea:" line, outside the post
   - a grey `Source: <url>` line
5. **A note before you post:** figures to double-check and gaps only they can fill. Never use "worth a check".
6. **Sign-off:** "Put together by Adi, Signal."

If Google Drive isn't connected, save `doc.html`, send it with SendUserFile, and say that Drive needs connecting.

## Step 7: Connection-request note (300 characters or fewer, link included)

Follow the rules in `references/01-outreach-audit.md` Parts 2, 3 and 5:
- Line one proves you looked: one specific number or detail from their posts. The best one contrasts their top post with the post type that holds their buried asset.
- One idea only: the doc, framed as a free gift built from their own material.
- A soft close, e.g. "Free, no strings:" followed by the link.
- No em dashes, emojis, exclamation marks, flattery, "I came across your profile" or "loved your post".
- **Link format:** `docs.google.com/document/d/<id>`, with no https:// and no /edit. That's about 72 characters, which leaves about 210 for the text.

Count it every time:

```
python3 scripts/count_note.py "<note>"
```

Aim for 280 or fewer so Souvik has room to edit. Report the count.

Example (Ron Schmelzer, 267 characters):
> Ron, your Stick joke got 24 comments, the MacPaw episode got 1. Your hiring math and 5 Laws of Scalemaxxing mostly show up as links, so I turned them into 7 posts in your voice. Free, no strings: docs.google.com/document/d/<id>

## Step 8: Hand-off reply

Keep the reply short and in this order:
1. The doc link, plus the reminder: set sharing to "Anyone with the link can view" before sending.
2. The note text and its character count.
3. A table with one row per post: title, the four editor scores, and the call.
4. **Fill in:** gaps only the prospect can close.
5. **Check:** figures that are old or come from a single mention.
6. **Cost:** Eden credits used and the number of web searches.

Never paste the full post texts into the chat; they're in the doc.

## Cost guidance

Run each prospect in a fresh session so context doesn't pile up. For daily runs, Sonnet at medium effort is enough. Mode B saves an Eden credit per prospect.
