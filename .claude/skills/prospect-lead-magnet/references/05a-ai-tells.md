# AI-tells taxonomy (complete reference)

The full detector. Read this during any audit. Everything here is a Layer-2 default (voice may override, with evidence) **unless** it appears in the P0 list under Severity tiers or in Signal's house hard-bans, which are Layer-1 floor and come out regardless.

Match inflected forms. Each vocabulary entry covers the listed word and its variants (adverb, gerund, plural, comparative, verb conjugations) unless a variant has a distinct honest meaning. `leverage` also flags `leveraging`; `meticulous` covers `meticulously`; `real` meaning "factual" is not the intensifier in "a real improvement" — judge by context.

## Contents
1. Formatting
2. The X-not-Y family and the common AI phrases (start here)
3. Vocabulary — Tier 1 (always flag)
4. Vocabulary — Tier 2 (flag in clusters)
5. Vocabulary — Tier 3 (flag by density)
6. Tier 3 phrases (flag at density or in clusters)
7. Template phrases and transitions
8. Structural patterns
9. Rhythm and uniformity
10. Writer-side diagnostics
11. Severity tiers (P0 / P1 / P2)
12. Supplemental cliches and openers
13. Model first-word fingerprints
14. Era context (judgment, not bans)
15. Self-reference escape hatch

---

## 1. Formatting

- **Em dashes (— and --)**: Signal house hard-ban (Layer 1). Replace with commas, periods, parentheses, or two sentences. Applies to headings too. Catch both the Unicode em dash and the double-hyphen substitute.
- **Bold overuse**: Strip bold from most phrases. In body content for Signal, bold is a house hard-ban. If something is important enough to bold, restructure the sentence to lead with it.
- **Emoji in headers / body**: House hard-ban. Remove. (Social posts elsewhere may allow one or two end-of-line emoji; not for Signal's house style.)
- **Excessive bullet lists**: Convert bullet-heavy sections to prose. Bullets only for genuinely list-shaped content (steps, comparisons, parameters). On LinkedIn, lists are fine.
- **Curly quotes and apostrophes**: Weak paste-from-chat signal, meaningful mainly in plain-text or code contexts. Word, Docs, macOS, iOS all auto-curl, so most human prose has them. Corroborating only, never conclusive. Do not flag curly apostrophes alone.
- **Immaculate typography in casual registers**: Weak, register-scoped signal. Perfect spacing and capitalization in fast-typed contexts (chat, DMs, PR comments) is corroborating, not proof. Inverse: when editing a human's casual text, preserve their typos and idiosyncratic capitalization rather than smoothing away the fingerprint.

## 2. The X-not-Y family and the common AI phrases

The highest-frequency tells in short-form business writing. If you only read one section before an audit, read this one. Every pattern here shares one mechanism: the sentence performs insight instead of delivering it. The fix is almost always the same move, which is to delete the frame and state the claim.

### 2.1 The X-not-Y family (all forms)

The single most recognizable AI sentence shape. It manufactures contrast so the claim feels earned without any evidence being offered. **Max one per piece, and only when the X being negated is something the reader actually believes.** Negating a strawman is always a cut.

| Form | Example | Fix |
|---|---|---|
| Direct negation | "It's not a tool. It's a teammate." | State Y. "It works like a teammate: it picks up the ticket itself." |
| Split-sentence | "The headline isn't the speed. The real story is the cost." | "The cost is the real story." |
| Multi-negation countdown | "Not the price. Not the features. The trust." | "They bought it for the trust." |
| Not just / but | "This isn't just a redesign, it's a rethink." | "They rethought the whole flow." |
| Question negation | "The question isn't whether AI writes. It's who edits." | "Who edits matters more than whether AI writes." |
| Problem reframe | "The problem was never the model. It was the eval." | "The eval was the problem." |
| Less about / more about | "This is less about tooling and more about trust." | "This is about trust." |
| Not because / but because | "Not because it's cheap, but because it's fast." | "They picked it for the speed." |
| Everyone thinks X, actually Y | "Everyone thinks it's a distribution problem. It's a retention problem." | "It's a retention problem." |
| Doesn't mean X, means Y | "Hiring slower doesn't mean hiring less. It means hiring better." | "Hiring slower means hiring better." |
| More than X, it's Y | "It's more than a feature. It's a philosophy." | Cut entirely; the sentence has no content. |
| Stopped X, started Y | "We stopped selling features and started selling outcomes." | Keep only if both halves are literally true and specific. Otherwise state the change. |
| Not a bug, a feature | any variant | Cut. Exhausted. |

**The carve-out.** The shape is legitimate when the X is a real, widely-held belief that the piece then argues against, and the Y is specific. "Most founders think the bottleneck is lead volume. In every audit I have run, it was reply rate" is a real correction with evidence behind it. "It's not a tool, it's a teammate" is a slogan. Test: can you name who believes X? If not, cut.

### 2.2 Throat-clearing openers

Cut and state the point.

"Here's the thing." / "Here's what I mean." / "Let me be clear." / "I'll be honest." / "Let's be real." / "The uncomfortable truth is." / "Real talk." / "I'll say the quiet part out loud." / "Hot take:" / "Unpopular opinion:" / "Look," as a sentence opener. / "So." as a standalone paragraph.

### 2.3 Faux-insight setups

These flatter the writer as the lone expert who noticed. Cut the setup and let the claim stand alone.

"This is the part most people skip." / "What most people get wrong." / "Here's what nobody tells you." / "The part everyone misses." / "Nobody talks about this." / "What they don't tell you about X." / "Most people will never understand this." / "Here's what separates the top 1%."

"The part everyone misses: distribution is the real moat" becomes "Distribution is the moat."

### 2.4 Colon reveals

A noun phrase, a colon, then a lowercase dramatic reveal. Fake suspense in punctuation form.

"The detail that makes it work: a separate agent grades it." / "The best part: it learns." / "One catch: nobody reads them." / "My favorite part: it took nine minutes."

Rewrite as a plain sentence. "A separate agent does the grading, which is what makes it work." Use colons for lists, labels, and quotes, not for drama. Prefer sentence case after a colon unless grammar, a proper noun, a title, or code requires otherwise.

### 2.5 Rhetorical setups and self-answered questions

"What if I told you…" / "Think about it:" / "Plot twist:" / "Let that sink in." / "Read that again." / Question-then-answer pairs where the writer asks something only to answer it in the next line ("Why does this work? Because it removes a decision.").

Drop the setup and make the point. One earned rhetorical question per piece is fine on `linkedin`; a stack of them is a tell.

### 2.6 Fake-profound kickers

The final "deep" line that converts a concrete point into an aphorism, metaphor, or mic-drop. "And that's the real product." / "Turns out the moat was the process all along." / "The best systems are the ones you forget you built."

**Delete it. Do not rewrite it into a better metaphor and do not preserve the rhythm.** The rewrite instinct is what produces a worse kicker. End on the clearest concrete sentence already in the draft. If the ending genuinely needs closure, add a plain takeaway or a next action, in ordinary words.

### 2.7 Negative listing and dramatic fragmentation

- **Negative listing**: "Not a course. Not a cohort. Not a community." Just say what it is.
- **Dramatic fragmentation**: "X. And Y. And Z." or "That's it. That's the whole thing." or "Simple." as a one-word paragraph. Use complete sentences. Carve-out: if the client's documented voice uses fragments (evidence required, see the verification guard), keep them.

### 2.8 Quick-scan phrase list

The ctrl-F list. Every one of these is a default cut unless the writer's voice provably owns it.

**Empty framing:** it's worth noting, it's important to note, at the end of the day, when it comes to, at its core, in today's world, in the age of, in the world of, the reality is, the truth is, in terms of, with regard to, in order to, going forward, in this article, let's dive in, the bottom line is, here's the deal, in a nutshell, without further ado, it goes without saying, rest assured, buckle up.

**Empty verbs and inflation:** delve, foster, leverage, utilize, facilitate, empower, streamline, robust, cutting-edge, paradigm shift, game changer, this is huge, this changes everything, tapestry, realm, beacon, multifaceted, meticulous, intricate, paramount, transformative, elevate, embark, supercharge, harness, ever-evolving, move the needle, bridge the gap, take it to the next level, unlock the power of.

**Often-empty adverbs (judgment, not bans):** just, literally, honestly, simply, actually, truly, fundamentally, importantly, crucially, inherently, inevitably. Cut when they add nothing. Keep when they carry emphasis, uncertainty, contrast, or the writer's spoken rhythm.

**Weak verb phrases -> direct verbs:** made a decision -> decided; has the ability to -> can; provides support for -> supports; is responsible for -> runs, owns; conducted an analysis of -> analyzed; reached a conclusion -> concluded; gave consideration to -> considered; is in agreement with -> agrees.

### 2.9 Sentence-structure defaults

- **Hollow intensifiers**: Cut `genuine`/`genuinely`, `real` (as in "a real improvement"), `truly`, `quite frankly`, `to be honest`, `let's be clear`, `it's worth noting that`. State the fact.
- **Vague endorsement ("worth [verb]ing")**: Cut or replace `worth reading`, `worth paying attention to`, `worth a look`, `worth exploring`, `worth checking out`, `worth your time`. Say *why* it matters.
- **Hedging**: Cut `perhaps`, `could potentially`, `it's important to note that`, `to be clear`. Make the point.
- **Missing bridge sentences**: Each paragraph should connect to the last. If paragraphs could be rearranged unnoticed, add connective tissue.
- **Compulsive rule of three**: Vary groupings. Use two, four, or a full sentence. Max one "adjective, adjective, and adjective" per piece.

## 3. Vocabulary — Tier 1 (always replace)

Appear 5-20x more in AI text than human. Replace on sight.

| Replace | With |
|---|---|
| delve / delve into | explore, dig into, look at |
| landscape (metaphor) | field, space, industry, world |
| tapestry | (describe the actual complexity) |
| realm | area, field, domain |
| paradigm | model, approach, framework |
| embark | start, begin |
| beacon | (rewrite entirely) |
| testament to | shows, proves, demonstrates |
| robust | strong, reliable, solid |
| comprehensive | thorough, complete, full |
| cutting-edge | latest, newest, advanced |
| leverage (verb) | use |
| pivotal | important, key, critical |
| underscores | highlights, shows |
| meticulous / meticulously | careful, detailed, precise |
| seamless / seamlessly | smooth, easy, without friction |
| game-changer / game-changing | describe what specifically changed and why it matters |
| hit differently / hits different | (say what specifically changed, or cut) |
| utilize | use |
| watershed moment | turning point, shift |
| marking a pivotal moment | (state what happened) |
| the future looks bright | (cut) |
| only time will tell | (cut) |
| nestled | is located, sits, is in |
| vibrant | (describe what makes it active, or cut) |
| thriving | growing, active (or cite a number) |
| despite challenges… continues to thrive | (name the challenge and the response, or cut) |
| showcasing | showing, demonstrating (or cut) |
| deep dive / dive into | look at, examine, explore |
| unpack / unpacking | explain, break down, walk through |
| bustling | busy, active |
| intricate / intricacies | complex, detailed (or name the specific complexity) |
| complexities | (name the actual complexities) |
| ever-evolving | changing, growing |
| enduring | lasting, long-running |
| daunting | hard, difficult, challenging |
| holistic / holistically | complete, full, whole |
| actionable | practical, useful, concrete |
| impactful | effective, significant (or describe the impact) |
| learnings | lessons, findings, takeaways |
| thought leader / thought leadership | expert, authority (or describe their actual contribution) |
| best practices | what works, proven methods |
| at its core | (cut) |
| synergy / synergies | (describe the actual combined effect) |
| interplay | relationship, connection, interaction |
| in order to | to |
| due to the fact that | because |
| serves as | is |
| features (verb) | has, includes |
| boasts | has |
| presents (inflated) | is, shows, gives |
| commence | start, begin |
| ascertain | find out, determine, learn |
| endeavor | effort, attempt, try |
| keen (as intensifier) | interested, eager |
| genuinely / genuine (as intensifier) | (cut) |
| symphony (metaphor) | (describe the actual coordination) |
| embrace (metaphor) | adopt, accept, use, switch to |
| load-bearing (metaphor) | essential, critical — or say what breaks if you remove it |

**load-bearing carve-outs:** Only the hyphenated compound is a tell; "the load bearing down on the bridge" is fine. Before a literal structural noun (`wall`, `beam`, `column`, `joist`, `truss`, `footing`, `slab`, `stud`, `lintel`, `girder`, `capacity`, etc.), optionally with a material or position adjective between, it is standard building terminology — do not flag. Abstract nouns (`structure`, `element`, `frame`, `foundation`) are excluded, so "the load-bearing structure of his argument" still flags.

**Extended Tier 1 (merged from supplemental sources).** Promotional superlatives and inflated nouns/verbs that behave like Tier 1 — replace on sight with a plain description or a specific claim: captivating, distinguished, esteemed, exquisite, formidable, iconic, indomitable, irrefutable, omniscient, pioneering, trailblazing, unassailable, unblemished, unequaled, unmatched, unparalleled, unrivaled, unsurpassed, unwavering, unyielding, visionary, avant-garde; apogee, epitome, gusto, odyssey, pinnacle; usher, transcend, redefine (as empty inflation). Also treat these overused openers/phrases as always-cut: "in a nutshell", "without further ado", "buckle up", "take it to the next level", "unlock the power of", "supercharge your", "move the needle", "here's the deal", "the bottom line is", "it goes without saying", "rest assured".

## 4. Vocabulary — Tier 2 (flag when 2+ in the same paragraph)

Fine alone; a cluster signals a rewrite.

| Replace | With |
|---|---|
| harness | use, take advantage of |
| navigate / navigating | work through, handle, deal with |
| foster | encourage, support, build |
| elevate | improve, raise, strengthen |
| unleash | release, enable, unlock |
| streamline | simplify, speed up |
| empower | enable, let, allow |
| bolster | support, strengthen, back up |
| spearhead | lead, drive, run |
| resonate / resonates with | connect with, appeal to, matter to |
| revolutionize | change, transform, reshape |
| facilitate / facilitates | enable, help, allow, run |
| underpin | support, form the basis of |
| nuanced | specific, subtle, detailed |
| crucial | important, key, necessary |
| multifaceted | (describe the actual facets) |
| ecosystem (metaphor) | system, community, network, market |
| myriad | many, numerous (or give a number) |
| plethora | many, a lot of |
| encompass | include, cover, span |
| catalyze | start, trigger, accelerate |
| reimagine | rethink, redesign, rebuild |
| galvanize | motivate, rally, push |
| augment | add to, expand, supplement |
| cultivate | build, develop, grow |
| illuminate | clarify, explain, show |
| elucidate | explain, clarify, spell out |
| juxtapose | compare, contrast, set side by side |
| paradigm-shifting | (describe what actually shifted) |
| transformative / transformation | (describe what changed and how) |
| cornerstone | foundation, basis, key part |
| paramount | most important, top priority |
| poised (to) | ready, set, about to |
| burgeoning | growing, emerging |
| nascent | new, early-stage, emerging |
| quintessential | typical, classic, defining |
| overarching | main, central, broad |
| quietly | cut, or name the concrete contrast |
| deeply (significance collocations: "deeply integrated/committed/rooted"; literal "deeply nested" or "cares deeply" never count) | cut, or name what runs deep |
| underpinning / underpinnings | basis, foundation, what supports |

**Extended Tier 2 (merged):** predominant, prominent, ubiquitous; nexus, panorama, spectrum, trajectory, journey; brace, orchestrate, reinforce, envision, bridge the gap. Flag when two or more land in one paragraph.

## 5. Vocabulary — Tier 3 (flag only at high density)

Normal words; flag only when the text is saturated (roughly 3%+ of words), a sign AI filled space with vague praise.

significant / significantly (replace some with numbers), innovative / innovation (describe what is new), effective / effectively (say how or cite a metric), dynamic / dynamics (name the forces), scalable / scalability (describe what scales and to what), compelling (say why), unprecedented (name the precedent it breaks), exceptional / exceptionally (cite what makes it an exception), remarkable / remarkably (say what is worth remarking on), sophisticated (describe it), instrumental (say what role it played), world-class / state-of-the-art / best-in-class (cite a benchmark).

## 6. Tier 3 phrases (flag at 2+ uses of one phrase, or 3+ distinct phrases from this set in one piece)

Worst offenders in crypto, web3, DePIN, AI/infra content. The cluster rule: three or more distinct phrases from here in one piece is a strong signal even at one use each.

emerging sector / emerging space / emerging category (name the actual sector), the integration of (X with Y) (describe what changes for the user), the intersection of (X and Y) (pick the specific overlap or cut), community-driven (name what the community does), long-term sustainability (cite the horizon and constraint), user engagement (name the action), decentralized compute (specify the architecture), (sustainable) reward emissions (cite the schedule and sink), tokenized incentive structures (describe the mechanism), designed for long-term [X] (cut "designed for"; state the property).

## 7. Template phrases and transitions

**Slot-fill templates (avoid):**
- "a [adjective] step towards [adjective] AI infrastructure" / "a [adjective] step forward for [noun]" -> say what actually changed.
- "Whether you're [X] or [Y]" -> false breadth. Pick the real audience or cut.
- "I recently had the pleasure of [verb]-ing" -> just say what happened.

**Transitions to remove or rewrite:**
- "Moreover" / "Furthermore" / "Additionally" -> restructure, or use "and", "also", "on top of that".
- "In today's [X]" / "In an era where" -> cut or state specific context.
- "It's worth noting that" / "Notably" -> just state the fact.
- "Here's what's interesting" / "Here's what caught my eye" / "Here's what stood out" -> reader-steering. Let content signal its own importance.
- "In conclusion" / "In summary" / "To summarize" -> the conclusion should be obvious.
- "When it comes to" -> talk about the thing directly.
- "At the end of the day" -> cut.
- "That said" / "That being said" -> cut, or use "but", "yet", "however" (do not overuse any one).
- "Firstly / Secondly / Thirdly", "Overall," as a paragraph starter, "Indeed," -> cut or restructure.

## 8. Structural patterns

- **Formulaic openings**: If it opens with broad context ("In the rapidly evolving world of…"), rewrite to lead with the news or insight. Context comes second.
- **Uniform paragraph length**: Vary deliberately. Some one-sentence paragraphs, some longer.
- **Suspiciously clean grammar**: Do not sand away personality. Deliberate fragments, sentences starting with "And" or "But", comma splices for effect — keep if the voice uses them.
- **Significance inflation**: "marking a pivotal moment in the evolution of…", "a watershed moment for the industry". State what happened; let the reader judge. If the sentence works after deleting the inflation clause, delete it. (P0.)
- **Generic future-narrative closers**: modal (may/could/will/is poised to) + "become" + "one of the most [adjective]" + narrative/story/trend/chapter. Grammatically a prediction, no testable content. Pick the falsifiable version instead.
- **Hedge-stacked predictions**: "could potentially create", "may eventually unlock", "might ultimately transform". Each hedge cancels the next. Pick one.
- **"Real/actual" adjective inflation**: "real on-chain tokenomics", "genuine utility", "true product-market fit" — empty intensifier on an abstract noun implying the rest of the field is fake, without saying what makes this one real. Carve-out: if the sentence names the contrast ("real on-chain settlement, not bridged IOUs"), keep it. Otherwise drop the adjective and add the specific claim.
- **Hashtag stuffing**: 6+ hashtags on a short post is a hard flag; 5+ is a soft tell on `linkedin`/`investor-email`. The block usually mixes one specific tag with broad category tags (#AI #Web3 #Innovation #FutureTech). Cut to 2-3 specific tags or none. (P0 on social.)
- **Bullet lists of bare noun phrases**: 5+ consecutive bullets each a short (<=6 word) adjective+noun with no verb ("Stable mining efficiency / Reliable pool connectivity / …"). The tell is the symmetry. Convert to prose or rewrite items as full checkable claims. Does not apply to genuine list content (changelogs, parameters, ingredients).
- **Copula avoidance**: "serves as", "features", "boasts", "presents", "represents" substituting for "is"/"has". Default to "is" or "has" unless a specific verb adds meaning.
- **Synonym cycling**: rotating "developers… engineers… practitioners… builders" to avoid repetition. Repeat the clearest word instead.
- **Vague attributions**: "Experts believe", "Studies show", "Research suggests" without naming the source. Cite specifically or drop the attribution and state the claim. (P0.)
- **Filler phrases**: "It is important to note that", "In terms of", "The reality is that" -> cut or state directly.
- **Generic conclusions**: "The future looks bright", "Only time will tell", "One thing is certain", "As we move forward" -> cut or make specific.
- **Chatbot artifacts**: "I hope this helps!", "Certainly!", "Absolutely!", "Great question!", "Feel free to reach out", "Let me know if you need anything else", "In this article, we will explore…", "Let's dive in!" -> remove entirely. (P0.)
- **"Let's" constructions**: "Let's explore", "Let's take a look", "Let's break this down" as false-collaborative openers. Start with the point.
- **Notability name-dropping**: piling on prestigious citations ("cited in NYT, BBC, FT, and The Hindu") to manufacture credibility. One specific reference with context beats four name-drops. Related: **historical-analogy stacking** ("like the printing press, the telegraph, and the internet before it") — name the one parallel that does analytical work.
- **Vague third-party validation**: pointing at an *unnamed* authority with a superlative ("independent testing confirms", "analysts agree", "an outside party putting us on top"). Name the source, test, and result so a reader can check it, or cut. Carve-out: specifically attributed, checkable validation stays (named benchmark, linked report, dated audit).
- **Superficial -ing analyses**: a trailing participle clause that pretends to explain what something means. Trigger words: highlighting, underscoring, reflecting, showcasing, symbolizing, demonstrating, signaling, marking, cementing. "The launch adds file search, highlighting the team's commitment to better workflows." The clause asserts significance and delivers no information. **The fix is the mechanism, not a better verb**: "The launch adds file search, so users can find old drafts without leaving the editor." Also flag strings of them ("symbolizing the region's commitment, reflecting decades of investment, showcasing a new era") and the same move without the -ing: "this represents a broader shift", "symbolizes a commitment to excellence".
- **Importance puffery**: "stands as a testament to", "marks a pivotal moment", "plays a vital role in", "solidifies its position as", "underscores its significance", "cements its status". State the fact and let the reader judge. "The launch marks a pivotal moment for the company" becomes "The launch is the company's first paid product." (Overlaps significance inflation; same fix.)
- **Formatting slop**: emoji in headings, bold sprinkled mid-sentence for emphasis, bullet lists where two sentences of prose would read better, headers over two-sentence sections. Format follows content; it does not decorate it. (Signal's house bans on emoji and body bold are Layer 1 and come out regardless.)
- **Promotional language**: tourism-brochure prose ("nestled within the breathtaking foothills", "a vibrant hub of innovation"). Plain description instead. If you would not say it in conversation, cut it.
- **Formulaic challenges**: "Despite challenges, X continues to thrive", "While facing headwinds, the organization remains resilient". Name the actual challenge and response, or cut.
- **Speculative scenario openers**: "Imagine a world where…", "Picture a future in which…". The scenario does the persuading; no evidence offered. Cut and state the real claim. Carve-out: fiction, a thought experiment with a stated payoff, instructional "imagine you have a sorted array".
- **False ranges**: pairing unrelated extremes ("from the Big Bang to dark matter", "from ancient civilizations to modern startups"). List the actual topics or pick the one that matters.
- **Inline-header lists**: bullets that start with a bold header repeating itself ("**Performance:** Performance improved by…"). Strip the header and write the point.
- **List-label periods**: bullets leading with a short label terminated by a period, then a gloss ("**Intros.** Years of conferences…"). A human uses a colon. Fix the period to a colon and lowercase the gloss, or drop the label. Carve-outs: a full-sentence label keeps its period; only flag when the leading fragment is a 1-4 word noun phrase with no verb.
- **Title case headings**: "Strategic Negotiations And Key Partnerships" -> sentence case for subheadings. Title case only for the main title, if at all.
- **Hyphenated-pair overuse**: "a high-quality, well-architected, future-proof solution" — cut to the modifier that matters. Also the attributive/predicate error: hyphenate before the noun ("a high-quality report"), not after a linking verb ("the report is high quality").
- **Cutoff disclaimers**: "As of my last update", "I don't have access to real-time data", "while specific details are limited". Find the information or remove the hedge. Never publish a sentence admitting the writer did not look something up. (P0.)
- **Speculative gap-filling**: "maintains a relatively low public profile", "is believed to have", "likely began his career in". Guesses formatted as statements. Cut or replace with a sourced fact.
- **Unfilled placeholders**: `[Your Name]`, `[INSERT SOURCE URL]`, `2025-XX-XX`, `<!-- add citation -->`. Near-proof of paste-without-editing. Fill with real content or delete the sentence. (Floor / P0.)
- **Chatbot citation markup leaks**: `citeturn0search0`, `contentReference[oaicite:0]{index=0}`, `oai_citation`, `[attached_file:1]`, `grok_card`. Fingerprints, not patterns. Strip every token. (Floor / P0.)
- **AI-tool URL parameters**: `utm_source=chatgpt.com`, `utm_source=claude.ai`, `utm_source=perplexity.ai`, `referrer=grok.com`. Strip the parameter; keep the URL if the link is meaningful. (Floor / P0.)
- **Novelty inflation**: treating established concepts as invented ("he coined the phrase", "a failure mode nobody's naming", "what nobody tells you about"). Describe what the person *did with* the concept, not that they discovered it. Also flag invented labels coined mid-sentence and never defined ("the supervision paradox", "a coordination tax") — define on first use or describe the mechanism.
- **Infomercial engagement hooks**: "The catch?", "The kicker?", "Here's the thing.", "The best part?", "Plot twist:", "The result?". Delete the hook and state the thing.
- **Social endorsement closers**: "This one is worth your time:", "a must-read:", "Do yourself a favor and read this.", "Bookmark this.", "Don't sleep on this one.", "Thank me later." The LinkedIn/X share-post tell. Say what the thing is and who it is for, then drop the CTA.
- **Emotional flatline**: claiming emotion as a crutch ("What surprised me most", "I was fascinated to discover", "What struck me was", "Interesting part of the project:"). Tell-don't-show. If the thing is surprising, the content should convey it. Also "hit differently" as a shortcut to relatability.
- **False concession structure**: "While X is impressive, Y remains a challenge". Balance without weighing anything. Make the concession specific or pick a side.
- **Rhetorical question openers**: "But what does this mean for developers?", "So why should you care?" used to stall before the point. If you know the answer, say it. One earned hook is fine on `linkedin`.
- **Parenthetical hedging**: "(and, increasingly, Z)", "(or, more precisely, Y)". If the aside matters, give it a sentence; if not, cut.
- **Numbered list inflation**: "Three key takeaways", "Five things to know" padded to hit a number. Only use when the content genuinely has that many discrete parallel items.
- **Reasoning chain artifacts**: "Let me think step by step", "Breaking this down", "To approach this systematically", "Step 1:". Chain-of-thought scaffolding leaking into prose. State the conclusion, then the evidence.
- **Sycophantic tone**: "Great question!", "Excellent point!", "You're absolutely right!". Chat rewards, not writing. Remove. (P0.)
- **Acknowledgment loops**: "You're asking about", "To answer your question", restating the prompt or the prior section before answering. Just answer.
- **Confidence calibration phrases**: "It's worth noting that", "Interestingly", "Surprisingly", "Importantly", "Notably", "Certainly", "Undoubtedly". Let the fact speak. Flag by density (one "notably" in 2,000 words is fine; three in 500 is stacking). Related persuasive-authority tropes: "the real question is", "at its core", "fundamentally", "make no mistake", "the truth is".
- **Self-labeling significance**: after a list, pointing back and labeling one item ("That last move is the contrarian one", "Here's where it gets clever"). The label does the work the content should. Cut it and let the explanation carry the weight, or reposition the item so the label is redundant. Significance-adjectives that signal it: contrarian, clever, surprising, counterintuitive, interesting, key, unusual, smart, brilliant, real, actual.
- **Wall-of-text replies (missing line breaks)**: in conversational registers (issue/PR comments, chat, DMs, casual email), a reply-length text (under ~150 words) of 4+ sentences delivered as one unbroken block. Break at thought boundaries. Carve-out: a single dense paragraph is correct in formal long-form (blog intro, docs, a tight one-paragraph email) — never flag continuous long-form prose for lacking internal breaks.
- **Recap-flattery opener**: replying by summarizing the other person's own work back at them with praise before the point ("Thanks for all the legwork — the migration script and rollback plan you worked through are what made this possible"). Substance first; if thanks is warranted, one plain clause.
- **Excessive structure**: more than 3 headings in under 300 words; 8+ bullets in under 200 words; formulaic section headers ("Overview", "Key Points", "Summary", "Conclusion"). Merge, convert to prose, or use headers that say something specific.

## 9. Rhythm and uniformity

Structure is the #1 detection signal — weighted higher than vocabulary. Fix every flagged word but leave the rhythm metronomic and the text still reads as AI.

- **Sentence length uniformity**: if most sentences are 15-25 words, it sounds robotic. Mix short punchy (3-8 words) with longer flowing (20+). Fragments and questions break monotony.
- **Paragraph length uniformity**: vary deliberately; some one sentence, some longer.
- **Vocabulary repetition vs synonym cycling**: humans repeat when the word is right and vary when natural. No formula.
- **Read-aloud test**: if a TTS engine could read it without sounding weird, it is too uniform.
- **Missing first-person perspective**: where appropriate, the writer should have opinions and reactions. Relentless neutrality is itself a tell.
- **Over-polishing**: editing out every irregularity pushes human writing *toward* the AI profile. Natural disfluency and uneven pacing keep text human. Do not sand away all personality.
- **Vocabulary diversity (TTR)**: type-token ratio, distinct types over total tokens. Human prose 200+ words usually lands 0.50-0.65; AI trends flatter, sometimes under 0.40. Low TTR is not proof (narrow or technical topics compress legitimately), but on general prose over ~200 words, below 0.40 is worth a look. Fix by broadening the *what* — name specific things — not by thesaurusing.

## 10. Writer-side diagnostics

Not regexes; read-and-judge tests.

- **Paragraph-reshuffle immunity**: can you swap two body paragraphs without breaking the piece? If order does not matter, it is a list of points, not an argument that builds. Establish a through-line where each paragraph depends on the last, or make it an explicit list, or find the missing thesis.
- **Treadmill effect / low information density**: read each paragraph and ask "what's actually new here?" AI restates the premise in fresh words. If you can cut 40-60% with no information lost, do. For each paragraph name the one fact, claim, or turn it contributes; if there is none, cut it.

## 11. Severity tiers

Prioritize by tier on a quick pass. **P0 items are the Layer-1 floor: fix regardless of voice.**

### P0 — Credibility killers (fix immediately)
Cutoff disclaimers; chatbot artifacts and sycophancy ("I hope this helps!", "Great question!"); vague sourceless attributions ("Experts believe"); significance inflation on routine events; hashtag stuffing on `linkedin`/`investor-email`; citation-markup leaks; AI-tool URL parameters; unfilled placeholders.

### P1 — Obvious AI smell (fix before publishing)
Tier 1 word violations; the X-not-Y family in any form beyond one earned use; throat-clearing openers; faux-insight setups; colon reveals; fake-profound kickers; superficial -ing analyses; importance puffery; template and slot-fill phrases; "Let's" openers; synonym cycling; formulaic openings; bold overuse; em-dash frequency; future-narrative closers; social endorsement closers; hedge-stacked predictions; real/actual inflation; bullet lists of bare noun phrases; Tier 3 phrase clustering (3+ distinct).

### P2 — Stylistic polish (fix when time allows)
Generic conclusions; compulsive rule of three; uniform paragraph length; copula avoidance; transition phrases; rhetorical setups and self-answered questions; negative listing; dramatic fragmentation; weak verb phrases; formatting slop; hashtag stuffing on `blog`/`technical-blog`; Tier 3 phrase repetition (single phrase 2x).

Quick passes cover P0+P1. Full audits cover all three.

## 12. Supplemental cliches and openers (merged)

Add these to the always-cut set alongside Tier 1: "I hope this finds you well", "As per my last email", "Please don't hesitate to reach out", "That's a great point!", "I'd be happy to", "As an AI / As a language model", "here's the deal", "the bottom line is", "buckle up", "in a nutshell", "without further ado", "take it to the next level", "unlock the power of", "supercharge your", "bridge the gap", "move the needle", "it goes without saying", "rest assured".

## 13. Model first-word fingerprints

AI text disproportionately opens with these words. Do not open a post with them; if a draft does, rewrite the opener to lead with the news or insight.

- ChatGPT: as, yes, sure, here, in, to, creating, certainly, title, the
- Claude: in, from, this, how, yes, title, according, the, based, here
- Grok: step, introduction, yes, creating, to, title, in, certainly
- Gemini: my, creating, while, here, yes, this, the
- DeepSeek: based, yes, step, comprehensive, here, to, creating, title, certainly

## 14. Era context (judgment, not hard bans)

Why certain words spike, useful for calibration rather than mechanical banning. GPT-4 era: delve, tapestry, testament, vibrant, pivotal, meticulous, underscore, interplay, bolstered. GPT-4o era: emphasizing, enhance, showcasing, highlighting, fostering, "align with". GPT-5 era onward: emphasizing, enhance, highlighting, showcasing. Treat a cluster of same-era words as a stronger signal than any one alone.

## 15. Self-reference escape hatch

When writing *about* AI patterns (a post teaching this, documentation, a teardown), quoted examples are exempt. Text inside quotation marks, code blocks, or explicitly marked illustrative ("for example, AI might write…") is not rewritten. Only flag patterns in the author's own prose, not in cited examples of bad writing.
