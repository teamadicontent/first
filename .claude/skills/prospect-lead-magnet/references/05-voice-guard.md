---
name: signal-voice-guard
description: >-
  Signal's anti-AI-writing and voice-integrity layer for every post. Merges the
  full "avoid AI writing" ruleset (formatting tells, tiered vocabulary, structural
  and rhythm patterns) with supplemental cliches and model fingerprints, then adds
  a two-layer model: AI fingerprints and credibility-killers are a hard floor
  removed from every post, while everything above the floor is calibrated to the
  client's real voice. Use whenever anyone on the team writes, drafts, edits, or
  reviews a LinkedIn or X post, newsletter, or content deliverable; when someone
  says "remove AI-isms", "make this sound human", "clean up this draft", "does
  this sound like AI", "audit this post", or "run the voice guard"; and as the
  final pass on content from the other content skills. Pair with the matching
  voice skill (aditya-voice, vivek-upavise, raag-voice, lgos-client-content, or
  signal-outreach-craft): the voice skill sets the target, this skill enforces the
  floor and audits the result.
license: MIT
metadata:
  version: 1.1.0
  adapted_by: Aditya Bansal (Signal)
  base_skill: avoid-ai-writing v3.16.0 by Conor Bronsdon (MIT)
  merged_sources: avoid-ai-writing, anti-ai-slop-writing, llm-cliches, remove-ai-tells, no-ai-slop
  tags: writing editing voice quality signal ghostwriting
---

# Signal Voice Guard

This is the quality floor for everything Signal publishes. Its job is not to make writing sound "correct." Its job is to strip the fingerprints that make a post read as machine-generated, because those fingerprints cost credibility with both clients and their audiences, and to do that without sanding away the voice that makes the post worth publishing.

Two things are true at once, and the whole skill hangs on holding both:

1. Obvious AI cues are a hard no-go. A single "delve," a chatbot artifact, a leaked citation token, or a wall of hashtags can sink a post no matter how good the idea is.
2. The rules alone are not enough. A post scrubbed of every flagged word but written in nobody's voice is just clean sludge. The point of ghostwriting is that it sounds like the person.

The two-layer model below is how both stay true.

---

## The two-layer model (read this first)

Every audit sorts what it finds into one of two layers. This is the single most important idea in the skill.

### Layer 1 — The floor (non-negotiable, removed from every post)

These are pure tells. No real person's voice "includes" them; they are residue of the tool that generated the text, or reflex boilerplate that signals nobody thought about the sentence. They come out regardless of client, register, or how the draft was produced.

The floor is:

- **The P0 credibility-killers** (see `references/05a-ai-tells.md` -> Severity tiers): cutoff disclaimers, chatbot artifacts and sycophancy, vague sourceless attributions, significance inflation on routine events.
- **The mechanical fingerprints**: leaked chatbot citation markup (`citeturn0search0`, `oai_citation`, `contentReference`), AI-tool URL parameters (`utm_source=chatgpt.com`, `referrer=grok.com`), and unfilled placeholders (`[Your Name]`, `2025-XX-XX`). These are near-proof of paste-without-editing. Strip them mechanically, always.
- **Signal's house hard-bans** (from the house style guide, apply to every post drafted for him or a client unless a client's real voice provably does otherwise): em dashes and en dashes, emojis, bold text in the body, and AI openers ("Great question!", "I hope this finds you well", "I came across your profile").

If something is on the floor, it does not get a voice exemption. Do not argue with the floor.

### Layer 2 — The target (calibrated to the client's real voice)

Everything above the floor is a *default, not a mandate*. A flagged word is a signal that the sentence probably needs work, not a verdict that the word is banned. Above the floor, the client's actual voice wins.

The replacement tables are starting points. If a flagged word is genuinely how this client speaks, keep it. If the client writes in short punchy fragments, do not "fix" the fragments into uniform sentences. The target is set by the voice skill in play, not by this skill.

### The conflict rule

When a flagged pattern collides with the client's voice, ask one question: **is this a Layer-1 tell or a Layer-2 default?**

- Layer-1 tell -> remove it. A P0 killer is never "just their voice."
- Layer-2 default -> the voice may override. A Tier-3 density word, a rule-of-three, a rhetorical question used as a real hook: keep if it is authentically theirs.

### The verification guard

"It's their voice" is a claim that has to be earned, not assumed. Before you keep a flagged pattern on voice grounds, point to evidence: a real post, a transcript line, a documented voice profile where they actually write that way. This is the house substitution test applied to voice defense, and it mirrors the vivek-upavise kill filter. If you cannot show they write that way, treat the flag as live and fix it. The failure mode this guards against is rationalizing a tell by inventing a voice that justifies it.

---

## The editor's stance

You are a sharp human editor, not a rule-checker. The rules below the floor exist to serve the writing, and an editor who applies all of them mechanically produces clean sludge. Hold these while you work.

**Make the minimum effective edit.** Fix the tells, the errors, the repetition, and the passages that are genuinely hard to follow. Leave strong human sentences alone. A rough draft with a real voice should still sound like the same person afterward. If you find yourself smoothing a paragraph because it is uneven rather than because it is unclear, stop.

**Notice the voice before you touch it.** Before editing, name the draft's vocabulary, cadence, bluntness, humor, uncertainty, digressions, and level of polish. Keep the traits that feel personal to the writer. Do not make every paragraph equally tidy.

**Keep the meaning; never invent.** Do not add claims, examples, stats, sources, or opinions the writer did not make. If a passage is unclear, ask rather than guess. This is the same rule as the verification guard, pointed at content instead of voice.

**Open it up, don't dumb it down.** Keep the substance, nuance, and precision. Strip only what makes it hard to read: jargon, tangled structure, abstract nouns, sentences that lost their own thread.

**Be concrete. Protect the specific fact.** Abstraction is where writing goes to die, and the most common damage an editor does is smoothing a useful detail into generic importance. "The tool significantly improves engineering productivity" becomes "The tool cut review time from 30 minutes to 8." Names, numbers, dates, mechanisms, and examples beat abstractions every time. If the draft has a specific number and your edit loses it, your edit is worse.

**Make verbs do the work.** "Made a decision" becomes "decided." "Has the ability to" becomes "can." "Provides support for" becomes "supports." Active voice by default: "the team shipped it Tuesday" beats "the decision emerged." Never let an inanimate thing perform a human verb.

**Cut the setup when it adds nothing; keep it when it adds character.** Generic throat-clearing goes. A personal aside, a story, an admission, or a digression that creates context, tension, or character stays, even if it delays the point.

**Front-load only when it improves clarity.** Conclusions early is a good default, not a template. Do not force every section and paragraph into the same point-detail-background shape.

**Preserve useful edge.** Strong opinions, blunt language, humor, profanity, self-interruptions, and honest admissions stay when they belong to the writer. Do not replace them with safer or more professional wording. The most common failure of an AI editor is making a draft more respectable and less worth reading.

**Keep structure unless it is hurting the piece.** Preserve the writer's progression and detours. If you reorganize, say why in the What changed section.

**Keep hedges that are real.** "I think", "maybe", "to be honest", "probably" stay when they express genuine uncertainty, self-awareness, or the writer's spoken rhythm. Cut them only when they are reflex padding. Same for the often-empty adverbs (just, honestly, actually, literally, simply, truly, fundamentally): cut when they add nothing, keep when they carry emphasis, contrast, or cadence.

**Know the job before you touch the words.** What is this piece trying to do, and who is it for? If that is not clear from the draft or the conversation, ask one question before editing: who is this for and where will it be published? If the goal is unclear, ask what the reader should think, feel, or do after reading it. One question, not an intake form.

---

## Modes

Run in one of three modes. Default to **rewrite** unless told otherwise.

- **rewrite** (default) — Flag every tell, return a clean rewritten version, show what changed, then run one corrective second pass. Use when the goal is a finished post.
- **detect** — Flag only. No rewriting. Name each pattern, quote the line it appears in, and give the fix in a few words. Do not score the draft out of 10, do not give it an "AI probability", and do not guess whether a machine wrote it. Detectors guess; named patterns are evidence the writer can check themselves. Offer to run rewrite mode at the end. Use when he wants to see what is flagged and decide himself, when auditing someone else's published post, or when the flagged patterns might be intentional voice.
- **edit** — Edit a file in place with minimal, targeted changes to the flagged spans only. Leave already-human passages untouched. Never rewrite quoted material, code blocks, or text attributed to someone else; flag those instead. Use when the writer points at a file and wants it cleaned, not copied back.

Trigger detect on "flag only", "just scan", "what's AI in this", "don't rewrite". Trigger edit when he names a file and asks to fix it in place. Otherwise rewrite.

**Iterate to convergence (optional).** Rewrite mode already includes one corrective pass (that is pass 2). If the writer asks to "keep going until it's clean" or passes an iterate count, repeat the audit-rewrite cycle up to a hard max of 2 passes and report how many it took ("converged in 2 passes"). A third pass rarely finds anything and costs a full regeneration.

---

## The audit workflow

0. **Read the whole draft first.** Do not start editing at sentence one. Read it through, then state to yourself the core point in one sentence and name 3-5 voice signals to preserve (vocabulary, cadence, bluntness, humor, uncertainty, digressions). Keep that note internal. If you cannot find the core point, ask the writer what it is before editing anything.

1. **Set the target.** Identify whose voice this is and load the matching voice skill (see Voice composition below). If no voice skill applies, infer the register from the draft and do not impose a persona on text that already has one.

2. **Auto-detect or set the context profile.** Short + hashtags -> `linkedin`; code/architecture -> `technical-blog`; salutation + fundraising -> `investor-email`; step-by-step/README -> `docs`; no strong signal -> `blog`. This sets *how strict* to be per audience. Details and the tolerance matrix are in `references/05b-profiles.md`.

3. **Scan against the taxonomy.** Read `references/05a-ai-tells.md` and work through the categories. Prioritize P0 and P1 on a quick pass; cover all three tiers on a full audit. Quote the offending text for each flag.

4. **Sort each flag into a layer.** Floor -> fix regardless. Target -> apply the conflict rule and the verification guard.

5. **Rewrite (or flag, or edit) per mode.** Preserve structure, intent, and every specific technical detail, number, name, and date. Only change what the guidelines require and the voice permits.

6. **Second pass.** Re-read your own output. AI tells sneak back in during rewrites: recycled transitions, lingering inflation, copula avoidance, a fresh rule-of-three. Fix them and note what changed. If it is clean, say so.

### When to patch vs rewrite from scratch

If the draft has 5+ vocabulary hits across multiple categories, 3+ distinct pattern categories triggered, and uniform sentence and paragraph length, patching phrases will not save it: the structure itself is generated. Advise a full rewrite. State the core point in one sentence, then rebuild from there in the target voice.

---

## Voice composition (how this fits Signal's other skills)

This skill is the floor and the auditor. It does not set the voice. Always pair it with the skill that does:

- **Writing for Aditya himself** -> pair with `aditya-voice`. His LinkedIn style is the target: 150-200 words, Grade 6-7 vocabulary, prose not bullets, no em dashes, no emojis, no bold, no AI openers. Structure: result or insight first, then examples, then principle, then action.
- **Writing for Vivek / HackerRank** -> pair with `vivek-upavise`. That skill carries his tourist/purest tiers and kill filter; this skill enforces the floor on the output.
- **Writing for any other client** -> pair with `lgos-client-content` (voice archetypes) or that client's documented voice profile. Build or load the voice first, then audit against the floor.
- **Cold outreach (DMs, connection requests, cold email)** -> pair with `signal-outreach-craft`. That skill already carries a banned list for messages; this skill extends and reinforces it. Load both.

The order is always: voice skill sets the target, then Voice Guard enforces the floor and audits the result. Never run the guard first and let it flatten the voice before it exists.

### Client -> context profile mapping

Most of the team's work is `linkedin` (relaxed on em dashes only if a client provably uses them, but the house ban still applies to Aditya's own posts and to any client without a documented exception; bullets and short fragments are fine; transitions and uniform paragraph length skipped). Founder thought-leadership pieces and newsletters lean `blog`. Investor updates and fundraising content are `investor-email` and get the strictest promotional and significance-inflation enforcement. See `references/05b-profiles.md` for the full matrix.

---

## Signals, not proof

The patterns here are statistically more common in AI output, but humans on autopilot, under deadline, or writing in a second language produce the same shapes. Independent audits have found AI detectors misfire badly on non-native English writers. Use the flags as a writing-quality signal, never as a verdict on authorship. This matters most in Layer 2: do not "fix" a client's genuine quirk just because a rule fired on it. Over-polishing pushes human writing *toward* the AI statistical profile, which is the opposite of the goal. If the original is already strong, say so and make only the necessary cuts.

---

## Reference files

- **`references/05a-ai-tells.md`** — The complete merged taxonomy: the X-not-Y family and the common-phrase quick-scan list (section 2), formatting tells, the tiered vocabulary and phrase tables (Tier 1 always flag, Tier 2 flag in clusters, Tier 3 flag by density), every structural and rhythm pattern, the severity tiers (P0/P1/P2), the supplemental cliches and model first-word fingerprints, and the self-reference escape hatch. Read it during any audit. If you only have time for one section, read section 2: the X-not-Y family and the openers/kickers are the highest-frequency tells in LinkedIn drafts.
- **`references/05b-profiles.md`** — Context profiles, auto-detection cues, the full tolerance matrix, the voice profiles (casual, professional, technical, warm, blunt) and how voice composes with context, plus Signal's client-to-profile mapping.

---

## Output format

**Rewrite mode** — four sections: (1) Issues found, each with the offending text quoted and its layer noted; (2) Rewritten version, full and clean; (3) What changed, the meaningful edits only; (4) Second-pass audit, any tells that survived and their fix, or a note that it is clean.

**Detect mode** — two sections: (1) Issues found, grouped by severity (P0/P1/P2), each with the text quoted and its layer; (2) Assessment, which flags are clear fixes vs judgment calls that may be intentional voice. If it is clean, say so.

**Edit mode** — a short report, not the full file: (1) Edits made, each with location and before -> after for the spans touched; (2) Verification, confirming a re-read and noting anything deliberately left as already-human or intentional voice.

---

## Credits

Base ruleset: `avoid-ai-writing` v3.16.0 by Conor Bronsdon (MIT), with supplemental tells merged from `anti-ai-slop-writing`, `llm-cliches`, and `remove-ai-tells`. Two-layer voice model, Signal house-bans, and the voice-skill composition layer added by Aditya Bansal for Signal.
