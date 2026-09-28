# Profiles reference

Two independent axes. **Context profiles** set *how strict* to be for an audience. **Voice profiles** set *how the prose should sound*. You can write blunt for a blog or warm for docs. Neither axis overrides the Layer-1 floor: Signal's house hard-bans (em dashes, emoji, bold body, AI openers) and the P0 credibility-killers apply at every profile.

---

## Context profiles

Pass a context hint or auto-detect it. Rules not listed in the tolerance matrix apply at full strength everywhere.

- **`linkedin`** — Short-form social. Punchy fragments and visual formatting matter.
- **`blog`** — Default. Standard long-form prose. All rules at full strength.
- **`technical-blog`** — Long-form with code, architecture, APIs. Some technical terms get a pass.
- **`investor-email`** — High-trust audience. Tighten everything; promotional language is the biggest risk.
- **`docs`** — Documentation, READMEs, guides. Clarity over voice.
- **`casual`** — Slack, internal notes, quick replies. Only the worst offenders.

### Auto-detection cues

| Signal | Inferred context |
|---|---|
| Under 300 words + hashtags or mentions | `linkedin` |
| Code blocks, API references, technical architecture | `technical-blog` |
| Salutation ("Hi [name]", "Dear") + investor/fundraising language | `investor-email` |
| Step-by-step instructions, parameter docs, README structure | `docs` |
| No strong signals | `blog` (safest default) |

If auto-detection feels wrong, state which profile you are using and why. The writer can override.

### Tolerance matrix

Rules not listed apply at full strength across all profiles.

| Rule | linkedin | blog | technical-blog | investor-email | docs | casual |
|---|---|---|---|---|---|---|
| Em dashes | Signal house-ban still applies; relaxed only for a client who provably uses them | strict | strict | strict | relaxed | skip |
| Bold overuse | house-ban on body; bold hooks tolerated only outside Signal style | strict | strict | strict | relaxed | skip |
| Emoji in headers | house-ban for Signal; 1-2 end-of-line only for non-Signal social | strict | strict | strict | skip | skip |
| Excessive bullets | skip (lists work on LinkedIn) | strict | relaxed (technical lists OK) | strict | skip (lists are docs) | skip |
| Hedging | strict | strict | relaxed ("may" is accurate in technical) | strict | relaxed | skip |
| Word tables (full) | strict | strict | partial (see below) | strict | relaxed | P0 only |
| Promotional language | relaxed (some sell expected) | strict | strict | extra strict | strict | skip |
| Significance inflation | strict | strict | strict | extra strict | relaxed | skip |
| Copula avoidance | skip | strict | relaxed | strict | skip | skip |
| Uniform paragraph length | skip (short-form) | strict | strict | strict | relaxed | skip |
| Numbered list inflation | relaxed | strict | relaxed | strict | skip | skip |
| Rhetorical questions | relaxed (1 as hook OK) | strict | strict | strict | strict | skip |
| Transition phrases | skip (short-form) | strict | strict | strict | relaxed | skip |
| Generic conclusions | skip | strict | strict | extra strict | skip | skip |
| Hashtag stuffing | strict | strict | strict | extra strict | skip | skip |
| Bullet-NP lists | strict | strict | relaxed (option lists OK) | strict | relaxed (parameter lists OK) | skip |
| Tier 3 phrase clustering | strict | strict | strict | extra strict | relaxed | skip |
| Future-narrative closers | strict | strict | strict | extra strict | skip | skip |
| Social endorsement closers | strict (the share-post tell) | strict | strict | strict | skip | relaxed (1 OK in a DM) |
| Hedge-stacked predictions | strict | strict | relaxed | extra strict | relaxed | skip |
| Real/actual inflation | strict | strict | strict | extra strict | relaxed | skip |

**Technical-blog word-table exceptions.** These have legitimate technical meaning and are not flagged in technical context: `robust`, `comprehensive`, `seamless`, `ecosystem`, `leverage` (actual platform leverage/APIs), `facilitate`, `underpin`, `streamline`. Still flag: `delve`, `tapestry`, `beacon`, `embark`, `testament to`, `game-changer`, `harness`.

**"Extra strict"** means flag even borderline instances. In an investor update, one "thriving ecosystem" can undermine the whole message. **"Skip"** means do not audit that category for that profile.

---

## Voice profiles

Voice is optional. If the writer does not name one, infer it from the draft's existing register and do not impose a persona on text that already has one. Each profile is concrete targets, not a vibe.

- **`casual`** — Contractions throughout. Short sentences (aim <=14 words average); fragments allowed. At least one first-person or concrete-anecdote touch. Near-zero jargon. Keep warm hedges ("honestly", "I think"); cut corporate ones ("it's worth noting"). *Blog, social, community.*
- **`professional`** — Active voice for most sentences. Vary sentence length. One concrete claim per paragraph (a number, name, date), never "experts say". Make the ask explicit. Low tolerance for hedging. *LinkedIn, investor email, pitches.*
- **`technical`** — Prefer plain copulatives ("X is Y") over inflated substitutes. One idea per sentence; imperative mood for instructions. Jargon fine, but define on first use. Tables and lists only where content is genuinely list-shaped. *Docs, technical blog.*
- **`warm`** — Address the reader directly ("you") and acknowledge them at least once. Cut intensifiers ("very", "truly", "incredibly") for stronger verbs. No performative-empathy openers. Medium sentences (15-20 words). *Mentorship, onboarding, thank-yous.*
- **`blunt`** — Lead with the claim; cut "It's important to note that" windups. Periods for emphasis, not em dashes. No padding to hit a rule of three. Near-zero hedging. Short declaratives with the occasional long sentence for contrast. *Decision memos, thought leadership, hard feedback.*

**Calibrate to a sample (preferred for client work).** If the writer gives a sample of the client's real writing, analyze its sentence-length pattern, contraction rate, paragraph openings, and recurring word choices, and match those instead of a named profile. Do not "upgrade" their vocabulary: if they write "stuff" and "things", keep that register. This is the Layer-2 target in practice — the sample *is* the evidence the verification guard asks for.

**How voice composes with context.** Voice sets the target; context sets how hard to enforce it. A voice target always applies, even where a context profile would skip that category (technical voice still prefers plain copulatives in a casual context). Where both agree, they reinforce. Where they disagree, resolve toward the **stricter** of the two (a warm voice on docs still gets no decorative tables). Sensible pairings: casual with casual, professional with linkedin/investor-email, technical with docs/technical-blog.

---

## Signal client-to-profile mapping

Defaults for the team's actual work. Always confirm against the specific deliverable.

- **Aditya's own LinkedIn** -> context `linkedin`, voice calibrated to his documented style via `aditya-voice`: 150-200 words, Grade 6-7 vocabulary, prose, result/insight first then examples then principle then action. House hard-bans in full force.
- **Vivek / HackerRank** -> context `linkedin` or `blog` depending on the piece, voice via `vivek-upavise` (tourist/purest tiers, kill filter). Guard enforces the floor on the output.
- **Founder thought-leadership / newsletters** -> usually `blog`, voice calibrated to that founder's sample via `lgos-client-content` or their voice profile.
- **Investor updates / fundraising content** -> `investor-email`, professional voice, strictest promotional and significance-inflation enforcement.
- **Cold outreach (DMs, connection requests, cold email)** -> pair with `signal-outreach-craft`, which carries its own banned list; this guard extends and reinforces it. Load both.

The rule that never changes: the voice skill sets the target first, then the guard enforces the floor and audits the result.
