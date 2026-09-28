---
name: prospect-lead-magnet
description: Signal's end-to-end cold-outreach lead magnet. From a prospect's LinkedIn profile link, or their name, headline, website, About section and about 10 posts, it researches the prospect, picks 5 to 10 fitting templates from the built-in template library, writes sourced posts in their voice, runs the Signal voice guard and editor, publishes a Google Doc in the fixed format, and writes a LinkedIn connection-request note of 300 characters or fewer (link included) for the 4th outreach touch. Use whenever someone sends a prospect's LinkedIn URL or prospect details and asks for the lead magnet, spec posts, sample posts, posts for outreach, the 4th DM, or says "run the process" or "do this prospect".
---

# Prospect Lead Magnet

**Goal:** the prospect opens the doc and thinks "that sounds like me, and I haven't written that yet." Getting the voice and the facts right matters more than being clever. A prospect spots a made-up story or a wrong number instantly, and then the outreach is dead.

**Deliverables** (every run):
1. A Google Doc with 5 to 10 ready-to-post LinkedIn posts, in the fixed format.
2. A LinkedIn connection-request note for the 4th touch: **300 characters or fewer, including the doc link.**
3. A short hand-off reply: the editor scores, gaps the prospect would have to fill, and figures to double-check.

Claude never sends anything to the prospect. Souvik edits the note and adds it to the CRM, and Adi sends it.

This file has everything the skill needs:
- **Part 1:** the process.
- **Part 2:** the voice guard, editor and outreach rules.
- **Part 3:** the template library, 224 templates with tags and skeletons.

Read Part 3's index lines to shortlist templates, then use only the skeletons you picked.

## Hard rules

1. **No invented stories.** Every story, quote, number, name and anecdote must trace to a source URL or to one of the prospect's own posts. If there's no source, the post doesn't get written. With no sourced story, write only educational, insight, contrarian and framework posts.
2. **No invented stances.** Don't put an opinion, prediction or piece of advice in their mouth that their sources don't support. If a template needs one, pick a different template.
3. **No placeholders inside a post.** A gap only the prospect can fill goes in the doc's "A note before you post" section. Better still, pick a template the facts already support.
4. **Signal house style:** no em dashes, en dashes or " -- ", and no bold in post bodies. Emojis and hashtags are allowed only when the prospect's own posts show them: match their choice and count, and use at most 3 hashtags.

# PART 1: THE PROCESS

## Inputs: two modes

- **Mode A: LinkedIn URL.** Research LinkedIn through Eden (costs 1 credit) plus web search.
- **Mode B: prospect details**: name, headline, website, About, about 10 posts, ideally with dates and reactions. They can arrive as pasted text, an uploaded file or a Google Doc link (read it with the Google Drive read tool). **Don't spend an Eden credit.** The posts supplied are the voice sample, so only run web searches for facts and stories.
- If the input is thinner than both modes, ask once for the Mode B fields. Otherwise go.

## Environment facts (learned the hard way)

- Cloud sessions often block direct page fetches of linkedin.com and many websites. **Web search works** and returns source URLs, so do all web research through it. If a fetch is blocked, don't retry it.
- **Eden credits are scarce** (about 250 a month, shared with other work). Use exactly one profile pull per Mode A prospect.
- **The Google Drive tools can create a doc but can't edit its text afterwards.** Get the posts right before uploading. A fix means uploading a new doc and renaming the old one "(old draft)". Never delete a doc the user may have edited: check its modified time against its created time first.

## Step 1: Research (budget: 1 Eden credit in Mode A, 5 to 9 web searches)

**Mode A, Eden:**
- Call `eden_analyze_creator` with `query` set to the URL, `creatorRef {platform: "linkedin", username: <slug from the URL>}`, `since: "year"` and `topPostLimit: 8`.
- If Eden returns `indexing` (it's pulling this creator for the first time), wait about 15 seconds and call it once more. A `not-found` timeout is temporary, so retry once.
- Creator-scoped `eden_search_social_content` reads the posts Eden already pulled. Use `eden_read_social_post` only when a post body was cut off and you need it.
- From Eden, take: the bio, follower count, the posts that did best against their own average, what their typical post gets, hashtags, formats, and 3 to 5 sample posts for voice.

**Web search (both modes)** covers the company or website, podcasts, newsletter, interviews, articles and press, talks, career history, the frameworks they've named and recent news. Record every fact with its URL.

**Research brief** (write it for yourself before writing any posts):
- **Who they are:** what they sell, who to, and where they're heading next.
- **Voice notes**, each with a quoted line from their posts as evidence: opening move, length, register, recurring phrases, emoji, hashtags, lists and close. Tag the tone as warm, analytical, bold, punchy or playful.
- **Audit:** 2 to 3 observations specific enough that only someone who looked could write them. Use the audit questions in Part 2C. These feed the note.
- **Sourced facts table** (fact, URL) and **sourced stories table** (story, URL). Write "None found" if empty; that's normal.
- **Covered list:** what they've already posted, so you don't repeat it.
- **Gaps only the prospect can fill.**

If you're working in a repository that has `lead-magnet/prospects/`, save the brief there as `<yyyy-mm-dd>-<name-slug>.md`, then commit and push.

## Step 2: Pick templates (from Part 3)

Each template's index line carries:
- **ID**
- **spec**
  - `go`: can be written from public research.
  - `found`: usable only if your sourced tables cover its "Needs".
- **type:** story, proof, case, about, contrarian, insight, educational, news or curation.
- **tone**
- **tier:** A = needs a personal narrative, B = needs verified specifics, C = expertise only.
- **Needs**

Choose 5 to 10 templates:
- At most 2 of any one type.
- Match their tone.
- At least one connected to where they're heading next.
- Built from their buried asset, not general industry knowledge.
- Not on the covered list.
- Not two templates marked as echoes of each other.

A good default mix: one post that turns their own numbers into a contrarian take, one satire or meme post if they're funny, one list of examples from their own material, one post built around a guest quote from their podcast or interview, one framework post if they've named a framework, and one news or prediction post built from their own recent article.

## Step 3: Write

- Follow each skeleton's **mechanic**, not its wording. Their rhythm wins on sentence length, lists and the close.
- **Length:** match their typical post. Most land at 80 to 160 words, and some prospects write 1 to 3 lines.
- **Hook:** make the first ~140 characters work before LinkedIn's "See more" cut-off.
- **Numbers:** use past tense for historical figures, e.g. "reached 900M users", never a present-tense stale number.
- If their bio claims something the sources don't cover (for example "triple exit" with only two found), don't fill the gap. Note it for the prospect.

## Step 4: Voice guard (mandatory, see Part 2A)

Fix every floor and P1 item. The prospect's real voice is what you're matching, and the floor applies on top of it.

Then run the scan in Part 2A:
- Use code execution if it's available (a regex pass over each post).
- If it isn't, check every item by hand.

Re-read every post once more after fixing, because tells creep back in during rewrites.

## Step 5: Editor pass (see Part 2B)

- Score every post 1 to 5 on Loops (every hook or question the post opens gets answered), Structure, Readability and Voice match, then make the call: Publish, Revise or Kill.
- Apply the fixes. Any post with Voice match or Structure below 4, or a Kill call, gets rewritten or swapped for a different template. Re-run steps 4 and 5 on it.
- Only publish posts called **Publish**, or **Revise** when the only open item is a gap the prospect has to fill (noted in the doc).
- Fact-check every number, name, date and market claim against the sources (see the traps in Part 2B).

## Step 6: Build the Google Doc (fixed format)

Build HTML in this exact structure, then upload it with the Google Drive create-file tool:
- `title: "<N> LinkedIn Posts for <Full Name>"`
- `contentMimeType: "text/html"`
- the HTML as `textContent`

This converts to a Google Doc. Confirm with the metadata tool that it has content.

Escape `&`, `<`, `>` and quotes in the text. Each line of a post is its own `<p>`, and a blank line is `<p>&nbsp;</p>`.

```
<html><body style="font-family:Arial">
<h1>N LinkedIn posts for NAME</h1>
<p><i>Written in your voice, built from THEIR SOURCES (e.g. your podcast, newsletter and posts). Free to use, edit or ignore.</i></p>
<h2>How these were made</h2>
<p>What was read, and the one-line audit insight.</p>
<p>Every number, name and quote comes from something you published. Each post lists its source so you can check it.</p>
<h2>At a glance</h2><ol><li>POST TITLE (FORMAT)</li>...</ol>
<h2>Post 1: TITLE</h2>
<p><b>Format:</b> FORMAT<br><b>Why this one:</b> 1 to 2 lines tied to their own data.</p>
<hr>
<p>post line</p>
<p>&nbsp;</p>
<p>post line</p>
<hr>
<p><b>Image idea:</b> optional, outside the post</p>
<p style="color:#666"><small>Source: URL(s)</small></p>
... repeat per post ...
<h2>A note before you post</h2>
<p>Figures to double-check and gaps only they can fill. Never write "worth a check".</p>
<p>Put together by Adi, Signal.</p>
</body></html>
```

If Google Drive isn't connected, give the HTML as a file and say that Drive needs connecting.

## Step 7: Connection-request note (300 characters or fewer, link included)

- **Line one proves you looked:** one specific number or detail from their posts. The best one contrasts their top-performing post with the post type that holds their buried asset.
- **One idea only:** the doc, framed as a free gift built from their own material.
- **A soft close**, e.g. "Free, no strings:" followed by the link.
- **Never:** em dashes, emojis, exclamation marks, flattery, "I came across your profile", "loved your post", "I hope this finds you well".
- **Link format:** `docs.google.com/document/d/<id>`, with no https:// and no /edit. That's about 72 characters, which leaves about 210 for the text.
- **Count the characters exactly** (use code execution if available) and aim for 280 or fewer so Souvik has room to edit. Report the count.

Example (Ron Schmelzer, 267 characters):
> Ron, your Stick joke got 24 comments, the MacPaw episode got 1. Your hiring math and 5 Laws of Scalemaxxing mostly show up as links, so I turned them into 7 posts in your voice. Free, no strings: docs.google.com/document/d/<id>

## Step 8: Hand-off reply

Keep it short and in this order:
1. The doc link, plus the reminder: set sharing to "Anyone with the link can view" before sending.
2. The note text and its character count.
3. A table with one row per post: title, Loops, Structure, Readability, Voice, and the call.
4. **Fill in:** gaps only the prospect can close.
5. **Check:** figures that are old or come from a single mention.
6. **Cost:** Eden credits used and the number of web searches.

Don't paste the full post texts into the chat; they're in the doc.

**Cost tip:** run each prospect in a fresh conversation. Mode B saves an Eden credit.

# PART 2: RULES

## 2A. Voice guard (Signal)

There are two layers:
- **Layer 1, the floor.** Always removed, whatever the voice.
- **Layer 2.** Fixed by default, but the prospect's real voice can override it. Only claim "it's their voice" if you can quote a post of theirs that does it.

**Floor (P0 and house bans):**
- Em dashes, en dashes and " -- ".
- Bold in the body.
- Emojis, unless the prospect provably uses them.
- Chatbot phrases: "Great question", "I hope this helps", "Certainly!", "Feel free to reach out".
- Vague attributions: "Experts say", "Studies show", "Research suggests".
- Significance inflation: "marks a pivotal moment", "a watershed moment".
- Hashtag stuffing: 5 or more is a tell, 6 or more is a hard fail.
- Unfilled placeholders, like `[Your Name]` or `[Image: ...]` inside a post.
- Cutoff disclaimers.

**P1, fix before publishing:**
- **The X-not-Y family:** "It's not X. It's Y.", "not just X but Y", "isn't about X, it's about Y", "You don't need X. You need Y.", "less about X, more about Y", "doesn't mean X, it means Y". At most one per post, and only when X is something readers really believe.
- **Throat-clearing openers:** "Here's the thing", "Let me be clear", "The truth is", "Hot take:", "Unpopular opinion:".
- **Faux-insight setups:** "What nobody tells you", "The part everyone misses", "Here's what separates the top 1%".
- **Infomercial hooks:** "The good news?", "The catch?", "The kicker?", "The result?", "The best part?", "Plot twist:".
- **Colon reveals:** "The best part: it learns."
- **Reader-steering lines:** "Here's what I'm noticing", "Here's what stood out".
- **Social endorsement closers:** "this one's for you", "worth a look / worth your time / worth reading", "must-read", "Bookmark this", "And a lot more".
- **Fake-profound kickers:** a slogan or aphorism as the last line, e.g. "Small team. Big scale.", "And that changes everything.", "Turns out the moat was the process all along." Delete it, don't polish it, and end on the last concrete line or a plain question.
- **Tier 1 words:** delve, landscape, tapestry, realm, paradigm, embark, beacon, testament to, robust, comprehensive, cutting-edge, leverage (as a verb), pivotal, underscores, meticulous, seamless, game-changer, utilize, vibrant, thriving, showcasing, deep dive, unpack, holistic, actionable, impactful, learnings, synergy, journey, supercharge, unlock, elevate.
- **Tier 2 words** (flag when 2 or more appear in one paragraph): harness, navigate, foster, streamline, empower, resonate, revolutionize, facilitate, crucial, ecosystem, transformative, cornerstone, paramount, poised.
- **Superficial -ing clauses:** "...highlighting the team's commitment". Replace them with the actual mechanism.
- **Empty framing:** "it's worth noting", "at the end of the day", "in today's world", "at its core", "let's dive in", "in a nutshell", "here's the deal".
- **Hollow intensifiers:** genuinely, truly, "to be honest".
- **Real/actual inflation:** "real product-market fit".

**P2, style polish:**
- Self-answered questions, like "Why does this work? Because...". One earned rhetorical hook per post is fine on LinkedIn.
- Every list coming in threes. Vary list lengths.
- Negative listing: "Not a course. Not a cohort."
- Dramatic one-word fragments, unless their voice does it.
- Uniform sentence length. Mix 3 to 8 word sentences with 20+ word ones.
- Generic closers like "The future looks bright".

**First words:** don't open a post with The, How, In, This, Here, As, Yes, Sure, According, Based or Certainly. Open on the news, the number or the scene.

**Editor's stance:** make the minimum effective edit. Keep specifics (names, numbers, dates). Keep the edge (humour, bluntness, their real hedges). Never add claims, stats or opinions.

## 2B. Editor (Signal)

Score 1 to 5, where 5 means publish as is.

**Loops** (promises the reader expects to be paid: a question, a tease, a number, a story, a framework):
- 5 = every loop opened is paid, in the order the reader's trust allows.
- 3 = paid, but late, or one minor loop left hanging.
- 1 = several open loops early, most never closed.
- An unpaid loop at the end is worse than none.

**Structure:**
- 5 = the spine (the best section) arrives fast and the close lands on its energy.
- 3 = the spine is right but the approach is backwards or the ending drifts.
- 1 = no spine.

**Readability:**
- 5 = no sentence exists only to reach the next one, the rhythm varies, and nothing needs a re-read.
- 3 = filler at the edges.

**Voice match:**
- 5 = passes the substitution test and has their habits, with nothing assigned to them they haven't said.
- 3 = the tone is right but their habits are missing.
- 1 = any stance or claim they haven't made, or any factual error. A factual error caps Voice at 2.

**Call:**
- **Publish:** no fix above word choice.
- **Revise:** the spine is right and the fixes are small. Name the first fix.
- **Kill:** no spine, or it fails the substitution test and no single addition rescues it.

**Faults that survive filler removal:**
- A credential stapled to a drumroll ("After 15 years, I've realized something:").
- A corrective opener ("While everyone obsesses over X, the real question is Y").
- A promise with no delivery window.
- Pre-announcing the evidence ("And everything they do is in line with that.").
- Restating a list right after it.
- Doing the reader's thinking for them ("X fits that template.").
- Sentences that change grammar partway through a list. Use one shape per item, with the last item hitting hardest.
- A one-word paragraph carrying an abstraction ("Mission.").
- A claim with nothing specific in it ("Most founders...", "The best teams...").
- A rhetorical question the author then answers.
- The writer's flourish in the last line.
- A bolted-on engagement question ("Agree?"). Use a question only a peer could answer.
- A close that just restates the hook.
- Commentary with nothing from the author's own life or company.
- A stance assigned to the author that they never stated.

**Substitution test:** could anyone else in their category publish this as written? If yes, add the one line only they could write, from the sources, or name the gap.

**Fact-check traps:**
- Unit and period: per day, per year, or cumulative?
- Stale figures: date every number.
- Reported vs confirmed: soften reported figures ("reportedly $7B+").
- Analyst opinion attributed to the author.
- The author's own biography (years, places) must match the sources exactly.

**Fix format** (when reporting to Adi):
- Quote the line.
- Name the fault's mechanism.
- Give the cost to the reader or the author's credibility.
- Give the fix line, or "cut".
- If a fix needs information only the author has, name it instead of inventing it.

## 2C. Outreach audit and message craft (Signal)

**Audit questions**, over their last 10 to 15 posts:
1. **Frequency and recency.**
2. **The substitution test:** name their most generic recent post.
3. **Voice check:** first person and opinionated, or press-release voice?
4. **The buried asset:** what they uniquely know but aren't writing about.
5. **Engagement vs audience:** e.g. 20K followers but posts averaging 10 likes, or one post hugely above their own average.

The output is 2 to 3 observations only someone who looked could write.

**Message rules:**
- Lead with the specific observation, not who you are.
- One idea per message, and give something usable even if they never reply.
- Soft close, and no calendar links.
- Simple words, with short sentences mixed with a longer one.
- Credibility at most as one parenthetical.
- Banned words: delve, leverage, unlock, elevate, supercharge, seamless, game-changer, landscape, journey, resonate, empower, streamline.
- Banned openers: "I hope this finds you well", "I came across your profile", "I couldn't help but notice", "I was impressed by".
- No flattery before the point.

**Final check:** does line one prove you looked? Is there something useful even without a reply? Would it sound normal read aloud? Is it 300 characters or fewer, counted?

# PART 3: TEMPLATE LIBRARY

224 skeletons. The 26 promotional templates (launches, events, giveaways, testimonials, hiring, ads) are left out because they're never used for spec posts.

- **Index line:** `ID · spec · type · tone · tier · title`, then Needs, then an Echoes line when another template is structurally similar.
- **Placeholders:** the [brackets] inside skeletons are slots to fill from sourced facts. They must never survive into a finished post.

## STORY (61)

### T18.4 · found · story · bold · A · Deliberate alienation
Needs: the exact dismissive question an old acquaintance asked and the turning point since
```
I caught up with an old [acquaintance] recently and they asked me "[Dismissive question]?"
These days I don't get offended or try to prove anything when people from my past life think [pursuit] is just some side hobby.
If they want to [choose a less desirable path], be my guest. That's less competition for us [identity/role].
Since [turning point] [time period] ago, I've [unlocked results] all thanks to my [self-deprecating description] [pursuit].
But go on about how "[dismissive label]" it is.
For the people who ARE hip to [opportunity/trend] and are tired of sitting on the sidelines, that's exactly what [offer name] is for. How to [core action] that gets you:
- [Desirable outcome #1]
- [Desirable outcome #2]
- [Desirable outcome #3]
[Call to action].
[Question for audience].
[Image that matches the post]
```
### T17.2 · found · story · warm · A · "The jobs that made us"
Needs: a specific first job and a memorable detail or lesson from it
```
The jobs that made us… [time period] ago, I was a [past role/job]. Things I learned that stick with me today:
This pic is from [reference to the image or artifact tied to the story]. I had [lack of skill/experience], no professional clue what I was doing, and a [dream/goal].
A vague dream to [describe long-term aspiration].
Through the experience, I learned:
- [Lesson / realization / observation / preference 1]
- [Lesson / realization / observation / preference 2]
- [Lesson / realization / observation / preference 3]
- [Lesson / realization / observation / preference 4]
[Question for audience or call to action].
[Image that matches the post]
```
### T17.5 · found · story · warm · A · Micro-moment, macro-lesson
Needs: a real quoted exchange/moment that cannot be invented, plus their actual reply
```
I [describe scene where someone says or does something that triggers a reaction in you]:
"[Quote the exact phrase that triggered it]"
[Your initial thought/reaction].
"[Quote your reply]."
[Break down the significance of that brief interaction].
[State what was wrong/right about it and why you reacted the way you did].
[Relate prior scenario to a niche-specific scenario].
[Give an illustrative example].
[Reveal the hidden question or meaning sitting underneath those examples]
There's another way.
[State your core philosophy or solution in one line]
[Give some practical advice/tactics].
Imagine [person in your opening scene] said:
"[The alternate, low-pressure version of the triggering line]"
I would've [positive reaction].
"[Your honest, unguarded response in that alternate version]"
[Briefly summarise why this interaction is better].
[Name the concept or framework behind this technique]
[Key takeaway(s)].
```
### T15.1 · found · story · playful · A · Turn life's calamities into business lessons
Needs: a specific real chaotic situation happening in their business right now
```
[Common cliché phrase/joke from your industry]:
[your honest reaction to that phrase]
[2-3 sentences explaining the chaotic situation you're dealing with].
The business lesson?
[Your one-line actionable advice].
[Briefly expand on advice].
[Photo showing the reality behind your reaction]
```
### T14.4 · found · story · warm · A · The secret to creating content that resonates
Needs: a specific real presentation moment and the audience's actual live reaction
```
I [briefly describe showing or presenting something - set the scene, don't reveal] and [describe surprising/positive feedback].
It was a simple comparison:
[Briefly summarize what you shared].
[Expand with key fact/data point/context].
[Describe how you noticed the surprising/positive feedback that followed].
That's when I knew [what you realised].
We're so used to hearing "[common belief or industry cliché]" that we forget to [the simple thing most people overlook].
[A short list of low-effort beneficial actions]. These things [compound/grow/build] in ways [the conventional alternative] simply can't.
Because [conventional alternative] [buys/gets you] [surface-level outcome].
[The approach you're advocating] [builds/creates] [deeper outcome].
And [that deeper outcome] turns into [chain of increasingly valuable results] you never saw coming.
[The audience you're speaking to] didn't need [more of what they thought they needed] - they just needed to [reframe of what they actually need].
That's what I've been saying for years, but seeing [describe the moment of realisation] in real time was something else.
If you're spending [too much time/money/energy on conventional approach], try this first:
- [Action step 1]
- [Action step 2]
- [Action step 3]
Do this for [time period]. Then tell me if you still think you need [the thing you're challenging].
[Question for audience or call to action].
[Image that matches the post]
```
### T13.2 · found · story · warm · A · The key to emotional storytelling
Needs: a specific decision/moment and the writer's raw first-thought vs corrected-thought reaction
```
I [made a decision that signals self-awareness].
First thing [that happened challenged your existing approach].
I'd [made that choice], on purpose, because I knew [it would lead to desirable outcome].
[Give more context about the initial inciting incident].
[They/It] made me feel [vulnerable emotion].
First thought, "[raw reactive response]."
Second thought, about [short timeframe] later:
"[Correcting word/phrase]. This is the exact reason you [made that decision]."
You wanted [the thing that came with the discomfort]. Now you have to actually sit in that feeling instead of running from it.
If [decision] never makes you feel a bit [vulnerable emotion], you've [made the wrong choice].
[Key takeaway].
[Image that matches the post]
```
### T12.2 · found · story · warm · A · Failure-first vulnerability post
Needs: a specific personal failure streak, the pivot made, and the measurable result after
```
I [vulnerable admission that highlights common pain point].
[X years of relevant credentials/actions]. [Y credential/actions]. But [0 result].
The consistent [failures] made me feel [negative self-label].
So, I started [unconventional action].
If you're not seeing any luck either:
[Actionable suggestion 1].
[Actionable suggestion 2].
[Actionable suggestion 3].
[Time period] of [unconventional action] → [specific measurable result].
Lesson? [Counterintuitive reframe of your negative label].
[One-line philosophical close].
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T11.2 · found · story · warm · A · Generic-lessons authority listicle
Needs: a specific achievement built plus personal anecdotes/mistakes behind each numbered lesson
Echoes: T13.4
```
How I built a [specific achievement] in [timeframe].
(And [X] lessons I learnt along the way)
1. [Lesson header]
[Personal anecdote / challenges overcome / commentary / observations / mistakes you made / advice for reader].
2. [Lesson header]
[Personal anecdote / challenges overcome / commentary / observations / mistakes you made / advice for reader].
3. [Lesson header]
[Personal anecdote / challenges overcome / commentary / observations / mistakes you made / advice for reader].
[Question for audience or call to action].
[Image that matches the post]
```
### T10.3 · found · story · warm · A · Transformation story as case study
Needs: a specific dated life/business decision and the concrete milestones since
Echoes: T18.2
```
In [specific month and year], I [made a significant life or business decision] with [humanising personal detail].
It's [current year]. Here's where we are now:
- [Life or business win/milestone 1]
- [Life or business win/milestone 2]
- [Life or business win/milestone 3]
- [Life or business win/milestone 4]
- [Life or business win/milestone 5]
None of this was handed to me.
[Difficulty/obstacle you faced 1].
[Difficulty/obstacle you faced 2].
[Difficulty/obstacle you faced 3].
But I made one decision that changed everything.
[The decision]
[Expand on the actions you took/the persistence you showed].
And slowly, then all at once - everything changed.
[One sentence naming the thing that made it possible].
[Question for audience or call to action].
[Image that matches the post]
```
### T9.1 · found · story · warm · A · All scroll-stopping images do THIS
Needs: a specific judged personal identity/choice and how it changed the writer's life
```
Just because you [fit/qualify/check the boxes], doesn't mean you [belong/should stay/are in the right place].
I'm a proud [identity that others might judge].
[That choice] changed my life:
- [Positive outcome 1]
- [Positive outcome 2]
- [Positive outcome 3]
I'm walking proof of what happens when you [make relevant choice].
But let me be clear: [briefly acknowledge objection].
[Handle objection by empathising with the difficulty of making said choice].
But you know what's worse?
[Sum up the risk of inaction].
I always fall back on this quote when I'm [struggling with trade-off of making said choice].
"[Pithy quote that has practical value]."
[Ask initial reflective question]?
I hope you choose [growth trajectory].
-
[X] questions to ask if you're [considering choice]:
1/ [Self-assessment question]?
2/ [Self-assessment question]?
3/ [Self-assessment question]?
[Motivating sign-off line].
[Image that matches the post]
```
### T9.5 · found · story · bold · A · The No.1 rule when making predictions
Needs: a specific dollar figure once offered and the writer's year-by-year skepticism-to-belief story
Echoes: T15.5, T9.5
```
I remember being shocked that [people/brands] used to offer me [dollar figure] for [thing]. Now I charge a LOT more than that. Here's the full story:
[Year] was when I first saw [peers/others] [doing the new thing]. I told myself [dismissive rationalisation]. This would pass. That I didn't need to chase it.
I completely dismissed [trend/opportunity].
But [evidence kept coming]. I was being [offered/approached/shown results] every single week. I started [engaging with it] (still convinced it wouldn't last).
Then [next year] happened. That was the first year [the industry/market] really started [the shift].
I also [hit personal milestone] that year. [Briefly expand on impact that had on your life/business].
So yeah, I was wrong.
I firmly believe [industry shift] will only continue to gain traction.
[One or two sentences of market logic that explains why the trend has legs].
Being early gave me an advantage. I had [specific asset] and [specific positioning] when [the market] started looking.
Now in [year], I'm [current status with specific numbers].
I strongly believe that [the thing] is here to stay.
[Question for audience or call to action].
[Image that matches the post]
```
### T6.1 · found · story · warm · A · Not your typical LinkedIn "Glow-Up" story
Needs: a specific real memory of holding two contrasting roles/experiences at the same time
```
[X] years ago, I had 2 very different [roles/experiences]: one [impressive metric], the other [humble metric].
[Role #1] - [brief description of what it involved].
[Role #2] - [brief description of what it involved].
[Briefly describe the daily routine that connected the two].
I used to [humorous thought or scenario about the contrast between your two lives - something that highlights the absurdity].
I loved [what you genuinely enjoyed about holding both experiences at once].
[One of the roles] had [a meaningful detail or mission].
What [surprised/shocked] me most was [the unexpected observation that connects both experiences].
In [context #1], [describe a surprising, contrasting difference].
In [context #2], [describe how that contrasting difference applied in the other context].
It made me realise [the core lesson].
So please, [direct appeal to the reader - short, punchy, informal].
[One-line universal principle that reinforces the lesson].
[Image that matches the post]
```
### T6.2 · found · story · warm · A · Your client conversations are rich with content ideas
Needs: the exact real question a client or prospect asked them
Echoes: T14.1
```
A [senior person you advise/work with] who's struggling with [specific challenge] just asked me: "[The exact question they asked]"
I've been [doing this thing] since my days [at credible company/role]. And I've [impressive result/metric that demonstrates your expertise].
So I've seen what works and what [fails/wastes resources] fast.
My answer: [Short answer with a condition attached].
What I tell every [client/founder/colleague] before they [commit/start/invest]:
* [Tip 1 - concise, specific directive]
* [Tip 2 - concise, specific directive]
* [Tip 3 - concise, specific directive]
The [channel/strategy/approach] works. But only when [the key conditions] work together.
Otherwise, you [vivid image of what failure looks like].
```
### T6.3 · found · story · warm · A · How to inject believability into your stories
Needs: the specific blunt feedback a real friend/colleague/mentor gave them, verbatim
```
One of my [closest friends/colleagues/mentors] told me my [work/output] sucked.
"[Direct quote - the blunt feedback they gave you]."
They were right...
I've been [complacent/coasting/distracted] with [your craft/work] recently.
Distracted with:
- [Relatable commitment/excuse 1]
- [Relatable commitment/excuse 2]
- [Relatable commitment/excuse 3]
Because [past results gave me a false sense of security], I let my standards slip.
But that is such a bad attitude to have.
[Briefly list 2-3 negative consequences].
I feel [genuinely grateful] for [people like this], who tell me what they really think, even when I don't want to hear it.
[Key realisation/reminder/lesson].
So, this is my plan to [improve/fix/raise the bar]:
1. [Action/step 1]
2. [Action/step 2]
3. [Action/step 3]
From now on there will be no more [bad habit].
We're [levelling up / raising the bar / getting serious] around here.
[Question that invites the reader to join you]
[Image that matches the post]
```
### T6.4 · found · story · warm · A · Not sure what to write about? Try this…
Needs: a specific past struggle story including one concrete detail like a tracking ritual/tool used
Echoes: T17.1
```
When I was getting started as a [role/creator/professional], I was [doing early version of what you do now and explain key thing you did differently].
I needed [specific number] of [clients/customers/sales] [key reason why].
It was hard. Almost every [sale/win/deal] was [the scrappy, manual way you had to do it].
I literally had [a physical tool or system you used to track progress]. [Describe exactly how it worked - the specific ritual or routine].
It was hard, but [explain what kept you going].
And it worked.
Over time, [describe how the flywheel started turning and things got easier].
Today, [describe where you are now - specific number or rate that shows the contrast].
If you're getting started, just know, it gets easier. [Brief insight about why the economics or dynamics shift over time].
But it's all on the other side of [the difficult phase].
[Punchy sign-off].
```
### T6.5 · found · story · warm · A · Peer conversations as content
Needs: a specific real conversation with a named person including their actual quoted answers
```
Some of the best [topic] conversations happen over...
[unexpected casual setting].
Recently, I met [expert's name], a [their role/title] I connected with [on [platform/during scenario].
They were visiting [your city/location] so I brought them to [local spot], [brief description of what makes it special].
Beyond the [surface activity], what I really enjoyed was the conversation.
We share the same mission.
[Briefly explain shared mission].
I asked [name] a few quick questions.
Q: [Question relevant to your shared field]?
A: [The helpful advice they gave].
Q: [Question relevant to your shared field]?
A: [The helpful advice they gave].
Q: [Light, personal question that humanises the conversation]?
A: [Short, fun answer].
It was such a pleasure meeting you [name]. [Warm closing line + hint at future meetup or continuation.]
[Image that matches the post]
```
### T5.1 · found · story · punchy · A · How to write a viral origin story
Needs: a full personal career timeline with specific ages, wins, losses, and results
```
Age [X]: [Origin story / starting point].
Age [X]: [Early attempt]. [Result].
Age [X]: [Failure or setback with a memorable detail].
Age [X]: [First meaningful win]. [Specific result].
Age [X]: [Loss or humbling moment]. [Why it happened].
Age [X]: [Win/Loss/Obstacle].
Age [X]: [Win/Loss/Obstacle].
Age [X]: [Win/Loss/Obstacle].
Age [X]: [Win/Loss/Obstacle].
Age [X]: [Win/Loss/Obstacle].
Age [X]: [Peak outcome - the big result].
Age [X]: [Where you are now & current metric].
Age [X]: [Recent win].
[Summarise key takeaway].
[Practical lesson].
[Brief motivational close].
[Image that matches the post]
```
### T4.2 · found · story · warm · A · The boring (but effective) truth about posting on LinkedIn
Needs: a specific piece of advice they personally dismissed early on and the mistakes that resulted
```
I [dismissive reaction] at so much [your field/niche] advice.
(And now I wish I'd listened)
When I started, everyone kept saying:
"[Common advice #1]."
"[Common advice #2]."
"[Common advice #3]."
And I thought: yeah, yeah. I'll figure it out my own way.
So I did. [What you actually did - list 2-3 wrong choices/mistakes you made].
It cost me.
The advice I ignored the most: "[The one piece of advice you wish you'd taken, in quote format]."
I thought [why you dismissed it]. That [second reason you dismissed it].
That I needed to [third reason, framed as what you believed instead].
I was wrong.
The [clients/businesses/individuals you now see succeeding]? [Brief description of what they're doing]. They've been [doing the thing you dismissed] for [timeframe]. And it's working.
Because [relatable human truth that explains why the advice works].
[Summarise core lesson].
I just had to learn it the hard way.
[Question for audience or call to action].
[Image that matches the post]
```
### T4.3 · found · story · warm · A · Justin Welsh's favourite 6-step persuasive post writing framework (PASTOR)
Needs: a specific personal struggle they experienced, with real numbers and feelings
```
There's nothing worse than [relatable pain point].
But a lot of [people/group] are in that situation. It sucks.
I can remember [when you experienced this yourself].
[Specific details of your struggle: financial, emotional, professional - give concrete numbers and feelings if possible].
Back then, [explain why things were different].
But today? [Explain how the landscape has changed for the better].
- [Opportunity/option]
- [Opportunity/option]
- [Opportunity/option]
[Optimistic one-liner about the opportunity available].
[Briefly acknowledge any difficulties or roadblocks honestly].
But [restate the core benefit of taking action].
If you don't know how to start, [give one simple first step].
I'll show you exactly how [mention your resource/offer/lead magnet].
[Outline the value prop].
[Simple next step - CTA].
[Relatable text image to act as a 'billboard' for your post]
```
### T4.4 · found · story · punchy · A · The "timestamp" hook
Needs: a specific turning-point story including who said what to change their mind
Echoes: T18.2, T10.3
```
[Year]: [Where you struggled or almost gave up]
[Year]: [Where you are now - e.g. same domain, elevated position]
I almost quit [role/pursuit] [timeframe] in. I remember [specific moment of doubt - what you were looking at, thinking, feeling].
I [complained about/struggled with] [specific frustration]. [Another frustration]. [Another frustration].
[Optional: Self-deprecating joke or aside that lightens the weight of the story].
[What you tried: effort you put in that still didn't work, 2-3 short lines].
Still [briefly explain where you were at mentally].
So before [pivotal moment], I made [decision you'd come to].
[Briefly expand on what happened: who was there, their relationship to you, where you were, what you said/did].
What [they said/happened] next [impactful statement]:
"[Question/advice/moment that changed your perspective]."
[Share what you realised].
[The initial change you made/action you took].
[Short timeframe later], [the first result - specific number or milestone]. I still remember the feeling of [what that felt like].
[X years/months] later, I've [stacked accomplishments - numbers, programs, milestones], and I'm [doing the elevated thing from your hook].
So.. before you [quit/give up on] something this year, [ask yourself/remember this]:
[Repeat/reinforce core quote/lesson].
[Key takeaway].
[Image that matches the post]
```
### T2.2 · found · story · warm · A · Terrifying (present-tense) vulnerability
Needs: a specific real present-tense moment, physical location, and vulnerable internal question
```
[Time period ago] I watched [vivid image of someone else doing something noteworthy]. Meanwhile, I couldn't shake the [thing pulling me back to my own world
[Briefly share a relevant detail that brings this moment to life].
I [achieved specific result] in [short timeframe].
I initially aimed for [modest goal].
Instead I'm [describe where you physically were], and all I can think is:
"[Vulnerable internal question]?"
I realised:
[Core emotional truth/realisation].
[Reframe the result in a humorous or self-deprecating way].
[Pivot to relevant offer or key takeaway].
[Question for audience or call to action].
[Image that matches the post]
```
### T2.4 · found · story · punchy · A · Flat, unemotional hook for gut-punch stories
Needs: a real injustice/setback story and the exact dismissive quote received
```
[Someone else] got the [thing you deserved] over me.
[Their weakness]. [Their one advantage].
I [proof of your merit]. [More proof]. [More proof].
[He/She] was 10x better than me at [the thing that actually got rewarded].
[He/She] got [reward]. I got "[dismissive quote]."
It took [time frame] for me to click that most [key realisation].
[Brief description of what you built instead].
Now I [the positive outcomes since]. No [negative thing you escaped]
[Key takeaway(s)].
[Inspirational sign-off].
[Question for audience or call to action].
[Image that matches the post]
```
### T1.1 · found · story · warm · A · Withheld-information story (mystery hook)
Needs: a specific real turned-down opportunity and the true reason for hesitating
```
[Timeframe] ago, I walked away from a career-making opportunity.
And I've never felt more at peace with a decision.
[Briefly set the scene & describe why it was such a great opportunity].
When it first came up, I couldn't believe it was even an option.
[Initial action(s) you took].
Then I hesitated.
Not because [reason A].
Not because [reason B].
But because [real reason].
It would've been easy to say, "This is too good to pass up. I'll figure it out."
But it didn't feel right.
And I realised [share what you realised at the time].
[State the decision you made].
Because deep down, I knew [reason for making decision].
Instead, I chose to focus on [another direction / priority / area of commitment].
Past me would've said yes immediately.
But this version didn't.
[Final takeaway(s)].
```
### T1.3 · found · story · warm · A · "You know that feeling when..." sensory device
Needs: a specific real break from work and the pivotal moment ending it
```
I stepped away from [activity / project / responsibility] for [time period].
No [related task A], [related task B], or [related task C].
It felt great… until [pivotal moment].
You know that feeling when [describe relatable feeling]?
Here's what I did instead of [doing what most people do]:
[List steps or actions you took].
By [time period], I had [unlocked desirable outcome].
Because I [reason for choosing this approach].
If you're struggling with [relevant pain point], try it.
I call it the [Name & Claim the framework/rule]: [sum up core idea].
This applies to almost anything.
Want to [achieve specific goal] but [obstacle that stands in your way]?
[List steps or actions you could take].
Within [short time period], you're [operating at or achieving a desirable output].
Most people try to [common mistake(s) people make].
[Key takeaway(s)]
[Image that matches the post]
```
### T-LC1.4 · found · story · warm · A · "LinkedIn loves stories"
Needs: a specific real origin story, hometown, hardship, and how you escaped it
Echoes: T18.2, T10.3, T4.4
```
I grew up here.
[Share 1-2 details of living circumstances and/or location]
X years ago, I decided to [pursue a goal].
I/We didn't have [an advantage].
I/We didn't even know what a [common means to achieve goal] was.
I/We [took specific actions] and [achieved goal].
[Short timeframe] ago, I/we [reached a significant achievement].
This post isn't to brag.
It's to show that regardless of where you start, you can [empowering message].
I didn't choose to live in [humble starting point].
I didn't choose to [put up with specific adversity].
I did choose to get out of that.
Truth is you can/have [universal truth or insight].
You may not be in control of where you start.
But you are in control of where you finish.
```
### T-LC1.5 · found · story · playful · A · Warning: this post may get you worked up!
Needs: a specific real workplace dysfunction situation with concrete issues experienced
Echoes: T13.1
```
Once upon a time.
I [experienced a challenging and slightly unusual situation]:
- [Issue/behaviour and its impact]
- [Issue/behaviour and its impact]
- [Issue/behaviour and its impact]
Sure, [type of situation] happens in [given context].
Sometimes we have to [reasonable response].
But here's what I could never understand:
Why does [specific issue] become [consequence of the issue]?
```
### T-LC2.4 · found · story · warm · A · How to lead with vulnerability and inspire others
Needs: a specific real business failure/comeback story with concrete repercussions
```
[X years] ago, my [type of venture] failed.
Despite not having [type of support], I was determined to succeed.
I [methods of funding and effort] for the first [X month/years].
Eventually I tried [alternative method of funding and effort], but I knew [related risks/challenges] so I had to [make specific sacrifice].
I [related struggle]. [Negative consequence].
That [venture] failed, and I faced [severe consequences].
For [X month/years], I dealt with [specific repercussions].
I worried about whether I could even [carry out a relatively normal task].
However, [X weeks/months] ago… 
[Positive turn or resolution].
Why am I telling you this?
Because what you see online isn't the whole story.
People only show you what they want you to see.
So if you're experiencing [specific type of hardship] right now, I assure you it won't last forever.
[Wise parting advice/quote]
[Personal image that matches the post]
```
### T-LC3.3 · found · story · warm · A · What promise are you making to the reader?
Needs: a specific person met at a real event and the real chain of events that followed
```
I [achieved remarkable outcome] [through unexpected means].
[X years/months] ago, I [met/supported someone] at [event/scenario].
They're also [role/accomplishment/recognition].
[Short time period ago], I reached out to them because:
* I [related struggle]
* I [related struggle]
* I [related struggle]
This led to:
* [Positive individual/shared outcome]
* [Positive individual/shared outcome]
* [Positive individual/shared outcome]
Which later led to [remarkable outcome].
And it all stems from [relevant details from initial encounter].
All this has taught me [valuable lesson] in [specific context].
[Sum up core message/lesson].
[Image that matches the post]
```
### T-LC5.4 · found · story · warm · A · How to boost your authority by association
Needs: a specific named collaborator, how they met, and a real shared anecdote/turning point
```
[Short time period ago], I [met/achieved significant milestone with] [description of the person - e.g. a rising star in the tech industry]
We first connected in [initial meeting context] in [year].
Both of us [description of initial common ground - e.g. aspiring entrepreneurs].
[Share an amusing anecdote or notable interaction during the early stages].
[Give any further context]
We reconnected and [what happened next].
Then, [describe a turning point or notable event/interaction].
To date, we [list shared accomplishments].
And [short time period ago] we [met/achieved significant milestone].
I admire [Person's Name] for their [three personal qualities].
They're the real deal and are destined for great things.
In fact, they [list some of their notable solo accomplishments/things they're working on].
I'm proud to call them a friend.
[Show gratitude for/endorse person]
Definitely check them out and follow their work.
[Personal sign-off]
[Image that matches the post]
```
### T-LC7.1 · found · story · warm · A · Remember to document your journey
Needs: three specific real personal achievement-vs-struggle contrasts from their own journey
Echoes: T1.2, T6.4
```
[Contrast a personal achievement with a prior struggle 1]
[Contrast a personal achievement with a prior struggle 2]
[Contrast a personal achievement with a prior struggle 3]
[Share a key takeaway or motivational insight based on your experiences]
P.S. [Call to action]
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC7.4 · found · story · warm · A · Why being vulnerable is relatable
Needs: a specific vulnerable admission, real turning point, and ongoing struggle from their own life
Echoes: T2.2
```
I've been in [engaging in new action] for [time period] and I [vulnerable admission].
[Briefly describe the struggle/challenge faced].
But recently I realised:
[Share a realisation or turning point].
[Acknowledge you still struggle].
Here's what I do when I [encounter struggle]:
* [Action 1]
* [Action 2]
* [Action 3]
[Share a final thought or reflection]
[End with an encouraging message]
[Image that matches the post]
```
### T-LC10.2 · found · story · warm · A · A good twist keeps 'em reading
Needs: a specific personal anecdote with an unexpected positive twist or reframe
```
Some truths about [your field or role].
[Brief personal anecdote and/or list of relatable challenges].
But this isn't a bad thing.
Because on [this occasion], I also [engaged in positive action or experience].
Which means, I [tie back to personal anecdote/challenges].
[End story with a positive outcome, action, or insight]
[Briefly expand on how you _think_ about facing such challenges]
[Share an inspiring takeaway]
Here's a tip: [Practical tip]
[Include relevant image/image hook]
```
### T-LC10.4 · found · story · warm · A · Here's another attention-getting tool… (surprising facts)
Needs: a specific personal setback-to-success turnaround story
```
[Surprising Fact or Misconception 1]
[Surprising Fact or Misconception 2]
[Surprising Fact or Misconception 3]
I [experienced relevant setback] before I [achieved relevant success].
[Motivational insight and/or practical takeaway]
```
### T-LC11.3 · found · story · playful · A · Catching your reader off-guard
Needs: a specific personal story of trying an unconventional method, from first steps to results
```
My secret for [achieving goal]?
[Unconventional solution].
[Anticipate the reader's scepticism or confusion].
But hear me out.
I [describe what you did initially - first steps].
[Key reason(s) for decision].
[Describe what happened next].
The results have been amazing!
* [Impressive result/benefit gained]
* [Impressive result/benefit gained]
* [Impressive result/benefit gained]
[Summarise key benefit].
[Give a brief anecdote that relates to your experience engaging with the solution/authority].
When I [did relevant activity], I [experienced/gained]:
* [Desirable outcome/positive feedback].
* [Desirable outcome/positive feedback].
* [Desirable outcome/positive feedback].
Here's the lesson:
[Key takeaway(s)].
PS. [Personal sign-off or call to action]
[Image that matches the post]
```
### T-LC12.5 · found · story · warm · A · The nightmare behind a shiny facade
Needs: a specific anonymized conversation with someone, including a direct quote from them
Echoes: T13.4, T12.5
```
Ever wondered what lies behind the glittering façade of [industry/profession/role]? 
Let me take you behind the scenes.
[Short time ago], I spoke with [describe person and their impressive credentials]. 
From the outside, [brief description of their success and lifestyle]. 
But here's what you don't see:
[Share a vulnerable admission/predicament they're in]. 
Despite [brief description of achievements], they're facing [key challenges]. 
Here's what they said:
"[Direct quote from the conversation]"
This story isn't unique. 
It's the untold reality many face in [industry/profession], where [brief description of common misconceptions].
I've [walked this path myself/seen it unfold like this before]. 
Sometimes, [positive outcomes]. 
But often, [common negative outcomes].
Then one day, you realise [reflective thought or decision].
For those feeling the same, looking for [what the reader might be seeking], I've created something for you. Check out this [resource/tool/link]: [Link]
```
### T-LC13.3 · found · story · warm · A · The power of emotionally-charged phrases
Needs: a specific personal anecdote tied to the shared painful experience described
```
"[Common negative feedback/phrase]."
If you've been [related activity], you will have heard this.
It [causes specific negative impact/emotion].
It [causes specific negative impact/emotion] when [specific situation].
It [causes specific negative impact/emotion] more when [more detailed situation].
[Relevant harsh truth].
But it [causes specific negative impact/emotion] less when you realise:
- [Reassuring point/new perspective 1]
- [Reassuring point/new perspective 2]
- [Reassuring point/new perspective 3]
[Personal anecdote related to narrative].
If you've faced [specific negative impact/emotion] lately, please know [reassuring statement].
[Briefly expand on the reassuring statement from above].
Keep [taking positive action 1].
Keep [taking positive action 2].
Keep [taking positive action 3].
[Powerful concluding statement].
[Image hook that reinforces core message]
```
### T-LC14.2 · found · story · warm · A · No one can argue with your personal experiences
Needs: a real personal struggle-to-realization story with specific early tasks and turning point
```
If you're a [target audience], your main task is to [core responsibility].
It took me [significant time period] to learn this.
When I first started [relevant activity], I was:
* [Task 1]
* [Task 2] 
* [Task 3] 
I worked X hours a day.
But [undesirable outcome].
It was [emotional response].
[Briefly expand on the problem].
And then I realised…
[Key realisation].
[Rhetorical question that relates to problem]?
So, I [changed my approach or took decisive action]
[Briefly explain new approach/action taken].
And that's how I [unlocked desirable outcome].
Because the truth is:
[Harsh truth].
[Key takeaway].
[Question to foster engagement and/or Call to action].
[Include relevant image/image hook]
```
### T-LC14.3 · found · story · warm · A · One of the greatest gifts you can give the reader
Needs: their own limiting belief and how long it personally held them back
Echoes: T5.2
```
This is a terrible mindset for [target audience]:
(It held me back for [time period])
[Briefly explain/list limiting belief(s)].
Because here's the thing…
In [current year], [motivating statement].
Zoom out:
[Include one or more supporting facts or statistics].
[Inspiring takeaway].
[Include relevant image/image hook]
```
### T-LC14.4 · found · story · warm · A · How to imply you're an expert
Needs: a specific real anecdote about someone they remember whose approach changed over time
```
I remember a [person/scenario] who/that used to [supportive/beneficial action].
[Person/Scenario] used to [key action].
But then [things stopped or resulted in a negative outcome].
It's because [prior action/event that initiated this change].
[Briefly expand on what happened to conclude the story].
See a lot of [target audience] subscribe to the [common strategy/action]. 
But here's the thing…
[Give your unique perspective/challenge how this strategy/action is implemented].
[Statement that ties your perspective back to the initial story].
[Key takeaway].
```
### T-LC14.5 · found · story · warm · A · How to write posts that sound like music
Needs: a real personal anecdote about how they came to resist a popular tool or strategy
```
Why [specific tool/strategy] has/was NOT [used to perform key action]:
Under pressure to [achieve challenging goal]?  
You're not alone.
Everyone's talking about [alternative solution]:
But I resist.  
[Briefly give your unique perspective].
[List reasons why you choose to resist].
[Tell a brief anecdote/story that explains how you came to adopt your unique perspective].
[List key actions that help you maintain this mindset].
As [Authority Figure] said:  
"[Relevant quote]."
[Key takeaway].
[Question to foster engagement and/or Call to action].
[Include relevant image/image hook]
```
### T-LC15.3 · found · story · warm · A · Stoke the fire of your reader's imagination
Needs: a real anecdote of personally witnessing the named eminent individual in action
```
The greatest [profession] I've ever seen is [eminent individual].
[Brief anecdote that involves you witnessing said individual conducting relevant activity].
And it got me thinking.
What if [eminent individual] was [conducting relevant activity in a hypothetical scenario]?
Here's how I think it would play out:
[Describe hypothetical scenario from start to finish - consider including dialogue if appropriate]
[Final outcome achieved].
The lesson?
[Summarise key takeaway(s)].
[Call to action or question to foster engagement].
[Image that matches the post]
```
### T-LC15.4 · found · story · punchy · A · The key to casting a wide net (for maximum reach)
Needs: three real struggle-to-milestone pairs from their own career history
Echoes: T4.1, T-LC1.4
```
[Early struggle or humble beginning].
[Related later success or milestone].
[Early struggle or humble beginning].
[Related later success or milestone].
[Early struggle or humble beginning].
[Related later success or milestone].
[Motivational takeaway].
[Call to action or question to foster engagement].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC17.5 · found · story · warm · A · How to Write on LinkedIn
Needs: a real personal surprising-experience story with a turning point and resolution
```
[Statement related to a surprising experience you had].
[Share where it started - give brief details on any significant events that led up to your surprising experience].
[Give a play-by-play of key events].
[The turning point and/or any key realisations you had].
[Share where you're at now - give key details that round out the transformational journey you went on, resolve the story].
[Key takeaway or lesson(s) you learned].
[Call to action or question for audience].
[Image that matches the post]
```
### T-LC18.1 · found · story · warm · A · How to Get People to (Actually) See Your Long-Form Content
Needs: a specific personal struggle-to-achievement story, real lessons, and a genuine content link
Echoes: T-LC1.2
```
[Timeframe] ago, I was struggling with [a challenge, frustration, or dissatisfaction].
Today, I've achieved [current success or milestone], and I'm [positive transformation or new state of life].
Lessons learned along the way: 
* [Key lesson 1]
* [Key lesson 2]
* [Key lesson 3]
* [Key lesson 4]
* [Key lesson 5]
* [Key lesson 6]
I recently shared my experience in a [content medium - e.g. speech, article, podcast].
You can [watch/read/listen] here: [Content link]
[Image that matches the post]
```
### T-LC18.4 · found · story · warm · A · Most Great Stories Have a Turning Point
Needs: a specific personal turnaround story with dated photo and a real turning-point moment
Echoes: T18.2, T4.4, T-LC1.4
```
This is me at [age/time period ago - note: this should coincide with the photo you include with the post] going through [challenging situation].
The [challenges] I faced were no joke:
[Briefly describe specific issues going on at the time].
And that's not all.
[Briefly describe 1 or 2 more specific issues going on at the time].
My [life/business/career] was spiralling out of control.
[List some of the negative repercussions].
[Reflect on how you were and what you thought at the time].
But you know what?
Sometimes you just need [briefly describe the moment that changed everything].
[Give some more details that relate to what happened - e.g. include events, quotes, realisations].
I decided [describe what you did next - e.g. how your mindset or trajectory changed].
And the rest is history.
Looking back, [reflect on the key thing you learned].
It's easy to [let the above challenges affect you in a negative way].
But what I failed to realise was [key realisation that seeded a more positive mindset].
[Key takeaway(s)].
[Call to action or question for audience].
[Image that matches the post - e.g. an image of you at the start of the story]
```
### T-LC19.2 · found · story · warm · A · Boost The Persuasiveness Of Any Idea
Needs: a specific real story with characters, dialogue, and a rising-stakes moment
```
Why [key theme/topic] matters.
[Briefly set the scene and/or introduce the story's characters].
[Share a relatable moment that occurred in the story - include dialogue if applicable].
[Raise the stakes by sharing another key emotional moment].
[Resolve the story in a way that illustrates why the key theme/topic matters].
[Image that matches the post]
```
### T-LC19.4 · found · story · warm · A · The Inverted Pyramid Technique
Needs: a specific origin story with a real turning point and named pivotal characters
Echoes: T7.5
```
[Person or Entity] [achieves remarkable feat] and is regarded as "[relevant moniker]".
[Notable fact or stat that has broad appeal].
This is the [adjective] story of [Person or Entity's Name].
[Describe their humble beginnings and/or prior struggles they faced].
[Mention the turning point - i.e. a key event, achievement or realisation].
[Include the relevant events that happened next to advance the story - e.g. did they meet any pivotal characters or do anything of note?]
Except [their venture or approach] was different.
[Break down the facts and figures behind the remarkable feat described in the hook, giving brief explanations where necessary].
[Conclude with a statement that describes the wider impacts of feat].
[Positive or inspiring takeaway].
[Question to foster engagement from audience]?
[Image that matches the post]
```
### T-LC20.2 · found · story · warm · A · Struggling With Something? Ask Your Audience
Needs: a specific current personal struggle and a specific past-success anecdote to contrast
```
I've been struggling to [recent struggle you're facing].
[Expand on the challenge, using inner monologue or self-reflection to build emotional depth].
Back when [reference to past success or easier times].
[Personal anecdote of prior success or ease].
Back then, [reflect on how things were easier].
Today, [describe how things have changed/become tougher].
So yeah, I'm [describe your emotional state or mindset].
Here's what I'm going to do:
1. [Actionable step 1]
2. [Actionable step 2]
3. [Actionable step 3]
4. [Actionable step 4]
What do you do when you face [specific challenge]? Drop your tips below!
```
### T-LC20.5 · found · story · bold · A · Grab Attention With The Unexpected
Needs: a specific surprising personal experience or habit with a genuine emotional twist
```
[Bold, unexpected statement related to a surprising personal experience].
It was [describe setting/event in brief, vivid detail].
[Describe a surprising detail or emotion related to the event.]
But [twist or unexpected realisation].
[Segway into personal reflection].
It made me think about how [describe a personal challenge or common societal pressure].
But as I [describe a pivotal moment or decision], I learned to [embrace/change] myself.
[Share a personal characteristic or behaviour you once tried to hide].
[Mention a quirky or unconventional habit].
[Open up about a struggle or challenge].
And guess what? 
[Describe the positive outcome or lesson learned].
[Key takeaway].
[Relevant question to foster engagement from reader]?
```
### T-LC21.3 · found · story · warm · A · How To Keep People Reading (A Storytelling Trick)
Needs: a specific multi-beat origin story with a real turning point and outcomes
```
[Time period] ago, I [describe unexpected outcome].
And it all started with [simple action/decision/discovery]. 
Here's the story:
I began [mention the activity or initiative] back in [relevant time period].
[Briefly reflect on that time, your circumstances, your mindset].
[Mention one or more relatable struggles or challenges you faced].
But I've always been drawn to [mention intrinsic motivation or passion].
So I [took specific action].
Around that time, [introduce character or key realisation you had].
[Briefly expand on why this event was significant and how it aligned with your goal].
[Expand how a simple interaction/moment/discovery/decision led to unexpected events or successes - give brief context where necessary].
That's how I [key turning point - e.g. a moment where things changed for the better].
[List any results/accomplishments/positive outcomes that followed].
But here's the thing…
[Key takeaway that's clearer now with hindsight].
Here are a few tactical takeaways I'd suggest for anyone considering a similar path:
* [Practical lesson 1]
* [Practical lesson 2]
* [Practical lesson 3]
[Image that matches the post]
```
### T-LC24.3 · found · story · warm · A · The Hidden Curiosity-Drivers Behind Engaging Hooks
Needs: a specific personal turning-point story (setback, loss, failure) and its consequences
```
[Impactful personal event].
[Briefly give context - describe the struggle, regret, or unfulfilled dream related to the story].
[State the goal(s) of the story's protagonist].
[Describe the story's turning point].
[List the following consequences].
This underscores that [principle or universal truth].
[List actionable steps related to the message in short, impactful sentences]:
* [Action 1]
* [Action 2]
* [Action 3]
[Key takeaway(s)].
```
### T-LC25.1 · found · story · warm · A · If You're Not (Yet) Posting, Read This
Needs: a specific real conversation, exact quote, and the reply/reaction that followed
```
I [briefly describe an interaction you had - i.e. who it was with and what it was about].
They told me:
"[Direct quote/dialogue to set up tension - eg. it may reflect a relatable challenge your audience faces]." 
"[Your response - eg. it may be counterintuitive advice]."
[Their reply/reaction].
Here's what worked for me:
* [Practical step/tip/advice]
* [Practical step/tip/advice]
* [Practical step/tip/advice]
* [Practical step/tip/advice]
In other words, [sum up your philosophy].
[Key takeaway/friendly reminder].
```
### T-LC25.2 · found · story · warm · A · Why Feeling Like An Imposter Is A Good Thing
Needs: a specific personal fear-to-realization story and the actions that triggered it
```
I was afraid to [relevant action].
In fact, I [detail showing initial hesitation or fear].
When I [took specific action], I realised [unexpected truth].
When I [took another action], I again realised [unexpected truth].
[Explain key concept. Give the reader a new way to think about it].
Fear of [common fear] goes away when you realise [counterintuitive truth/fact/stat]."
[List practical actions that illustrate key idea in action].
[Key takeaway].
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC25.4 · found · story · warm · A · "I Don't Have Any Stories To Share"
Needs: a specific real person met, the question asked, and their exact quoted response
Echoes: T7.5, T-LC7.3
```
A few months ago, I met [unique or intriguing person].
[Briefly tease what makes them and the interaction you had interesting]. 
Here's what they said:
I asked them [question], and they said "[interesting response that sums up or relates to key lesson]."
[Briefly give your take on their response].
[Expand on the lesson further: set up the situation/problem, add relevant context, reveal resulting actions].
[Highlight the key lesson].
In many areas of life, [core idea] applies too:
* [Example 1: Relatable scenario].
* [Example 2: Relatable scenario].
* [Example 3: Relatable scenario].
[Empowering conclusion or actionable takeaway].
```
### T-LC25.5 · found · story · warm · A · 2 Hooks Are Better Than 1
Needs: a specific real phrase/insight actually heard and the transformation it caused
```
I heard a [phrase/insight] that [describe transformation]:
"[Memorable phrase or insight]."
If you're [example activity], [briefly explain how phrase/insight applies in a real-world context]."
Here are X [content type - e.g. "lessons"] on [topic] I've learned recently:
1. [Principle/lesson/realisation 1].
2. [Principle/lesson/realisation 2].
3. [Principle/lesson/realisation 3].
4. [Principle/lesson/realisation 4].
5. [Principle/lesson/realisation 5].
"It's tough to [acknowledge related challenge]. 
But these truths can help you [unlock benefit(s)]."
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC26.1 · found · story · warm · A · How To NOT Come Across Like An Insufferable Know-It-All
Needs: a specific personal confusion/struggle and the moment it was resolved
```
Let's clear something up: [Common misconception or confusion].
Whether you're [target audience] or [secondary audience], understanding this is critical.
Without it, [describe negative outcome that may occur].
I remember when I [personal struggle related to the topic]. It wasn't until I [took action to resolve confusion] that I realized [insight].
In simple terms: [Concise explanation of key distinction].
[Further expand on concise explanation above, giving any relevant details or examples].
[Briefly explain what this means for each of the audiences - how does knowing this impact any relevant actions they may take?].
[Question for audience or call to action].
```
### T-LC28.5 · found · story · warm · A · 3 Things (Almost) All Great Stories Have
Needs: a specific personal or client origin/turnaround story mapped to intention-obstacle-resolution
```
[Specific action/strategy/task] is hard.
You [expand on what people typically go through].
Most people don't understand that [goal/process] is like [short analogy]:
* [Challenge 1].
* [Challenge 2].
* [Challenge 3].
Until you [make this realisation/reach this milestone].
After [gaining this experience/share result(s) you've driven], I've found there's one thing that [strategy/habit/tool/mindset] does:
* It [unlocks benefit 1].
* It [unlocks benefit 2].
* It [unlocks benefit 3].
When you [take related action], you [unlock core desirable outcome].
[Question for audience or call to action].
[Image that matches the post]
```
### T-LC29.2 · found · story · warm · A · Not An Expert? Try This…
Needs: a specific real conversation, event, or interaction the person actually had
```
[Time period ago], I had the privilege to [describe the event, conversation, or interaction].  
[Briefly share some context that gives the reader a window into something surprising and/or relatable about the scenario].
Here's the key thing I took away:  
[Thought-provoking observation or principle].  
Many people [describe a shared or relatable behavior or experience]. 
But [highlight how it's different for a specific group, skill set, or approach].  
[Summarise the main insight in a different way].  
[Suggest how the reader can implement the insight - e.g. describe a personal habit, tip, or tool you use to support this practice].  
If you want to [achieve result], [encouraging takeaway].
[Question for audience or call to action].
[Image that matches the post]
```
### T-LC30.4 · found · story · warm · A · All Top 1% Creators Understand This
Needs: a specific story about a mentor/parent/client, including an actual quote they said
```
A story [from someone significant or memorable].
If you're [a relevant audience], this might resonate with you as it did with me.
They said, [insert a quote or a poignant statement that introduces the theme of the story].
They've always [share a notable quality or value of the person].
But they remember this…
It was [describe a situation or challenge they faced, focusing on the tension or stakes].
They could just picture [describe the impact of the situation, using relatable or emotional imagery].
[Detail an action they took to resolve the situation, emphasising the decision-making process or sacrifice].
At the time, [introduce a contrasting perspective or person to heighten the significance of the actions].
[Describe the contrasting perspective's outcomes, underscoring the lesson or takeaway].
And in all these years, [highlight the enduring positive outcomes of the initial decision].
They often attribute their [success/happiness/lasting result] to [specific value/principle/action].
[Key takeaway - eg. general reflection or universal truth derived from the story].
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC32.3 · found · story · warm · A · Unsure What To Write? Try This
Needs: a specific real anecdote plus the exact quote of feedback that triggered it
Echoes: T6.3
```
Had a bit of a wake up call.
[Brief anecdote or situation that led to the realisation].  
[Direct quote of feedback or insight that triggered the change].
[State how it made you feel].
My first thought: [Your initial reaction/thought process].
[List any other realisations you had].
So I adopted X strategies to [improve/adopt new mindset]:
1. [Strategy 1]  
↳ [Short explanation or actionable step].
2. [Strategy 2]  
↳ [Short explanation or actionable step].
3. [Strategy 3]  
↳ [Short explanation or actionable step].
[Expand on how your perspective has changed].
The more I embraced this shift...  
The more [positive outcome] I created.  
And the more [measurable impact] I saw.
[Key takeaway].
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T14.1 · found · story · warm · B · The "recently someone asked me" post
Needs: a real recurring question a client actually asked them
```
I've [brief proof point establishing years of experience]. Now I [desirable lifestyle outcome].
But recently someone asked me "[relatable question about achieving that outcome]?"
My answer:
[Short, counterintuitive core advice].
Because unless you want to [specific future pain of not acting], you don't get a do over. You don't get [what gets lost] back.
This is what [your solution] buys you:
- it [benefit 1 - business or lifestyle]
- it [benefit 2 - business or lifestyle]
- it [benefit 3 - business or lifestyle]
- it [benefit 4 - business or lifestyle]
- it [benefit 5 - business or lifestyle]
Get it wrong and it's not just that [surface-level failure]…it's that [deeper failure], so [ultimate downstream consequence].
It's important.
So [core action]. And keep it simple!
Make sure you've got:
- [essential component 1]
- [essential component 2]
- [essential component 3]
Because if it's not simple, it'll [negative consequence].
[Question for audience or call to action].
[Image that matches the post]
```

## PROOF (22)

### T-LC3.1 · found · proof · warm · A · How to celebrate a win (without bragging)
Needs: a specific start date, real early struggles, and a named org/person who recognized the work
```
I [started engaging with specific action] on [date]. 
At first, I [briefly list common experiences/initial failures/struggles].
[X years/months] later, I've [sustained a specific level of effort].
This has led to [positive impacts/results].
I'm grateful to know my work offers [specific value] to others.
Special thanks to [Organization/Individual] for [Specific Recognition].
If you're just getting going or on a similar path, remember: 
[Motivational advice].
You won't regret [engaging in specific action] and [impacting others].
Here's a [resource/tip] to help you get started: [Link]
[Image that matches the post]
```
### T18.2 · found · proof · analytical · B · Before/after, "here's what I actually changed"
Needs: their own specific starting/improved metrics and the exact changes they made
```
I went from [starting metric] to [improved metric].
Here's what I actually changed:
For months I was [describe what you were doing].
[Consistent effort] over [time period].
Hoping [desired outcome] would happen on its own.
It was working. Just not fast enough.
So I made [X] moves:
1. [Change 1].
[Brief rationale].
2. [Change 2].
[Brief rationale].
3. [Change 3].
[Brief rationale].
No [ruled-out approach].
Just [actual approach].
I do this for [clients/others] every day.
I just never did it for myself.
Things were working. So I coasted.
But when I stopped coasting?
[Improved metric]. That's the difference.
[Question for audience or call to action].
[Image that matches the post]
```
### T17.1 · found · proof · playful · B · Build-in-public / document don't create
Needs: the specific tools used, product shipped, and an earlier simpler version built
```
I made this [type of output] using only [tool 1] & [tool 2].
(this isn't a "[category] is dead" [asset]).
But this technology is improving.
Also, [briefly give a necessary caveat].
But it is compounding.
And now I can [produce desirable output] and it will:
1. [Step 1 name] - [what it fixes or does]
2. [Step 2 name] - [what it fixes or does]
3. [Step 3 name] - [what it fixes or does]
[time period] ago, I built my first [earlier, simpler version of this system].
It simply [did one narrow function].
But now I'm out to solve [bigger underlying problem] for good.
[Question for audience or call to action].
[Image that matches the post]
```
### T17.3 · found · proof · punchy · B · One habit, one outcome
Needs: a specific achieved outcome/metric and the exact single habit that produced it
```
I [achieved impressive outcome].
From ONE simple habit:
[Name the single habit in one line].
You don't have to be [a traditional skill/talent] to [unlock desired outcome].
Instead, use this simple [time commitment] habit:
(It's how I consistently [related action] every single day.)
[Briefly break down your method - step by step].
This makes the next [time period]'s [task] effortless for [X] reasons:
1. [Reason why method helps 1].
[Explain reason 1 in 2-3 short lines].
2. [Reason why method helps 2].
[Explain reason 2 in 2-3 short lines].
3. [Reason why method helps 3].
[Explain reason 3 in 2-3 short lines].
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T17.4 · found · proof · analytical · B · A vs B comparison
Needs: two specific tools/methods compared with real prices, observations, and a stated verdict
```
I [made surprising product choice - e.g. downgrade].
Here's what happened:
[time period] ago I was [outline relatable problem you had with tool(s)].
I experienced [negative emotion/state].
So I ran an actual test to put some data behind my [instinct/hunch].
I [outline solution/test you implemented] to both [tool/method A] and [tool/method B]:
[Option A] ([price]):
- [Observation 1]
- [Observation 2]
- [Observation 3]
[Option B] ([price]):
- [Observation 1]
- [Observation 2]
- [Observation 3]
Before you say "[anticipated objection]" No. [Your counterpoint in 1-2 lines].
Anyway, the winner was [give your verdict].
It's been [time period] now and [outcome/result]. I'm still [current status].
Other than [secondary benefit], the biggest thing I learned is that [reframe the real lesson].
[Punchy closing line that restates the lesson memorably].
```
### T15.4 · found · proof · analytical · B · Why you should give more examples
Needs: a specific transparent public activity/event they ran and real observations from it
```
I've [done a specific, high-volume action] in [timeframe].
But on [day/date], [X] people watched me [do an unusual, transparent activity] for [duration] so they know exactly what I [look for/do/think] when I [related everyday action].
Here's the [X] biggest takeaways on what I was looking for (+ what I'd change):
1. [Observation/practical tip]
2. [Observation/practical tip]
3. [Observation/practical tip]
4. [Observation/practical tip]
5. [Observation/practical tip]
[Question for audience or call to action].
[Image that matches the post]
```
### T14.5 · found · proof · analytical · B · Struggling to book calls?
Needs: a specific historical result/metric and the exact outreach system steps used
```
Back in [year], [my business / I] [achieved a specific, concrete result] consistently. We never [common assumption about how that result happens], but [the actual system] worked like crazy:
Every [time period], we'd [first step you took]. Then we'd [second step that involves examples]:
1. [Approach name]
[Description/template/prompt/example].
2. [Approach name]
[Description/template/prompt/example].
3. [Approach name]
[Description/template/prompt/example].
Yes, this all takes [time / effort / work].
So few people do this and that's exactly why it works.
If I had to start over, this is exactly what I'd do.
[Question for audience or call to action].
[Image that matches the post]
```
### T8.3 · found · proof · analytical · B · How to breathe life into dead hooks
Needs: past attempts/tools tried, the specific tool/method used, and comparative results vs an incumbent
```
If you've ever [experienced a specific painful consequence of a known problem], you know the feeling.
[Thing that was supposed to prevent it] said everything was fine.
Why? Because [root cause of the problem].
I've been obsessed with [solving this problem] for years.
[Proof of obsession - past attempts, companies built, methods tried].
Tried to close the gap. Got [partial result].
Last week I tried something different.
I tried [tool/method]. 
[Step(s) you took].
Got [specific result with concrete detail].
Tried the same thing with [incumbent/alternative]. Got [inferior result]. Useless.
The difference?
[New tool/method] was [briefly explain underlying mechanism].
Here's what clicked for me:
[Handle any obvious objection that arises - _optional_].
[Summarise the main benefit of new approach].
If you're a [target reader] still [living with the old problem], there's a better way now.
[Question for audience or call to action].
[Image that matches the post]
```
### T7.2 · found · proof · analytical · B · Get outsized reach with this simple post type
Needs: three specific real AI systems/processes they've built and the business metric achieved
Echoes: T7.1, T18.3
```
How I'm using AI to run a [impressive metric] [business type] with [team size - _optional_]:
> [First system/process/initiative you've built - briefly explain how it works and how it's impacting your business].
> [Second system/process/initiative you've built - briefly explain how it works and how it's impacting your business].
> [Third system/process/initiative you've built - briefly explain how it works and how it's impacting your business].
[Briefly sum up how you feel about how it's going].
But we're pushing VERY hard on [this priority] because [reason(s)].
[Key takeaway].
[Image that matches the post]
```
### T1.2 · found · proof · analytical · B · Building-in-public value prop reminder
Needs: a real project milestone/metric and the specific build-in-public strategy used
Echoes: T17.1
```
My brand new [project / channel / initiative] just hit [early milestone].
But [metric] isn't the interesting part…
[I/We've] been [sum up what your service does] for clients for years. It's what [I/we] do at [Company Name] - [expand on company value prop].
But doing it for yourself is a different ball game.
When you're both the [role] and the [role], you [list common struggles].
So we stopped planning and just… started.
Brand new [project]. Starting from [zero / starting point].
And now we're watching the system work on our own terms.
[Briefly share some early wins / metrics].
[Break down your strategy, your thinking behind it, and the benefits].
[My old system] used to feel like a heavy lift. Now everything is easier because the system is compounding.
We do this for clients all the time. Now we're proving it works for ourselves.
[Key takeaway(s)].
I'll keep you updated with how things progress.
[Image that matches the post]
```
### T-LC3.2 · found · proof · punchy · B · "Pssst… wanna know a secret?"
Needs: a specific daily habit and the achieved outcome it actually produced
```
People ask me how I [achieved desirable outcome] so quickly.
My secret? 
I [daily action].
People ask me how I [achieved desirable outcome].
My secret? 
I [daily action].
People ask me how I [achieved desirable outcome].
My secret? 
I [daily action].
But the truth is…
There is no secret, just [core principle].
To [achieve key desirable outcome], you have to [high-level advice].
Here are [X steps/tips/strategies/questions] to get you started:
1. [Step/Tip/Strategy/Question]
2. [Step/Tip/Strategy/Question]
3. [Step/Tip/Strategy/Question]
4. [Step/Tip/Strategy/Question]
5. [Step/Tip/Strategy/Question]
Want to [Attain desirable role/outcome]?
[Conduct specific daily action]
Remember, showing up daily is what separates [desirable group] from the rest.
Start today.
```
### T-LC6.5 · found · proof · punchy · B · The power of repeating yourself over and over and over again
Needs: a specific real achievement and the prerequisites actually skipped to reach it
Echoes: T9.4, T8.1
```
I [achieved goal Y] without [common pre-requisite 1].  
I [achieved goal Y] without [common pre-requisite 2].  
I [achieved goal Y] without [common pre-requisite 3].  
I [achieved goal Y] without [common pre-requisite 4].  
I [achieved goal Y] without [common pre-requisite 5].  
To [achieve goal Y], all you really need to do is:
1. [Core action 1 for achieving goal].  
2. [Core action 2 for achieving goal].  
3. Rinse and repeat (many times).
Everything else is just a distraction.
[Image that matches the post]
```
### T-LC8.3 · found · proof · analytical · B · Share your wins, then tease future value…
Needs: a specific achievement with real dates, numbers, names, and the marketing strategy used
```
We/I [achieved something significant].
Here are the details:
[Give relevant details - e.g. dates, numbers, names, significant events]
This [project/achievement] was [the result of a unique factor]. 
Marketing consisted of [strategy]. 
And it involved [team description/anecdote].
[Provide a key takeaway/lesson]
We/I can't wait to share more lessons with you soon.
[Express some words of gratitude for team/audience].
```
### T-LC8.4 · found · proof · analytical · B · How to give an honest, unbiased review
Needs: a specific tool/technique tried, the timeframe, and the actual metrics reached
```
[Time/date], [notable event].
[Short time/date later], [impressive outcome].
This [tool/technique] helped me [achieve result] in [short time frame].
Here's how I did it:
1. [Step 1]
2. [Step 2]
3. [Step 3]
And here's the result:
[Impressive outcome + details of any relevant features/benefits]
These [outputs] reached [impressive metrics].
[Thought-provoking question that aligns with common objection]?
[Explain the broader implications]
[Share your opinions]
[Personal sign-off/call to action]
[Image that adds interest to the post]
```
### T-LC10.3 · found · proof · analytical · B · What does your hook imply?
Needs: specific real achievements over a stated timeframe plus the specific strategies used
Echoes: T7.2, T18.3
```
I've [engaged in action/role/platform/context] for [timeframe].
In which time, I've:
* [Achievement 1]
* [Achievement 2]
* [Achievement 3]
Here's what I didn't do:
* [Common tactic 1]
* [Common tactic 2]
* [Common tactic 3]
Instead, I did this:
* [Effective strategy 1]
* [Effective strategy 2]
* [Effective strategy 3]
* [Effective strategy 4]
* [Effective strategy 5]
So don't just [follow the common advice].
[Briefly summarise your overall effective strategy from above]
PS. [Relevant thought-provoking question for audience]?
[Include relevant image/image hook]
```
### T-LC20.4 · found · proof · punchy · B · Creative Reframing
Needs: a specific real milestone number (time, revenue, followers) to reframe vividly
```
[A past struggle you faced].
That's [statement that emphasises implications of struggle].
But then things finally changed.
This isn't a post about [specific challenge/topic]. It's about [topic]. 
[Key takeaway].
Perhaps you're:
* [Chasing goal/pursuit]
* [Chasing goal/pursuit]
* [Chasing goal/pursuit]
And perhaps you're:
* [Experiencing pain point]
* [Experiencing pain point]
* [Experiencing pain point]
[Reinforce key takeaway].
[Call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC22.4 · found · proof · punchy · B · The Progressive Timeline Technique
Needs: three specific dated milestones (quotes, results, or events) showing real progress
Echoes: T5.1, T-LC16.3
```
[Year/month/date]: [Quote/result/circumstance/event]  
[Next year/month/date]: [Quote/result/circumstance/event]  
[Following year/month/date]: [Quote/result/circumstance/event]  
[Summarise the key takeaway(s)].
It can help you [unlock these benefits].  
[Call to action or question for audience].
```
### T-LC27.1 · found · proof · analytical · B · Creating Content Can Be A Massive Waste Of Time (Unless You Can Answer This…)
Needs: a specific strategic change made plus before/after results achieved
Echoes: T-LC9.1, T27.1, T-LC19.1
```
[Timeframe] ago, I stopped [strategic action].
Now, I [new strategic action] because:
[Main reason for making change].
And despite what people say, you don't need [misconception] to achieve [desired outcome].
Here's what I did:
[List key steps you took to implement change].
Before, [outline key outcomes/results you were getting before change].
And now, [key outcomes/results since making change].
[Key takeaway(s)].
[Question for audience and/or call to action].
```
### T-LC27.5 · found · proof · warm · B · A Massively Underrated Marketing Play
Needs: a specific real event's title, location, audience, and key themes shared
Echoes: T-LC8.3
```
I did it!
I just finished my [presentation/event/keynote]:
"[Title or Topic]"
[Give some quick context - e.g. location, event name, audience].
It was amazing to see [a notable observation about the setting, audience, or event].
A few key themes:
* [Insight or takeaway 1]
* [Insight or takeaway 2]
* [Insight or takeaway 3]
* [Insight or takeaway 4]
[Reflect on a moment that stuck with you].
At one point, I shared that [key idea or bold statement].
[Briefly explain significance of key idea].
[Question for audience or call to action].
[Image that matches the post]
```
### T-LC28.2 · found · proof · analytical · B · Avoid This Mistake When Marketing Your Business
Needs: a specific small tweak they made and the surprising outcome/results it achieved
```
This 1 [small change or tweak] [achieved surprising outcome].
[Key element 1] is the same.
[Key element 2] is the same.
So why does it work better?
The answer is [core principle/strategy].
While [core principle/strategy] seems simple, it's [explain what people miss/why it's harder than it seems].
It requires [specific skill/mindset/resource].
Most [role/profession/group] [encounter common related frustration/challenge].
Instead of [pain point], you could:
[Expand on how your alternative solution is delivered in a way that's faster, easier, more efficient, or more cost-effective].
The result?
* [Key benefit 1].
* [Key benefit 2].
* [Key benefit 3].
[Question for audience or call to action].
[Image that matches the post]
```
### T-LC29.1 · found · proof · punchy · B · An Age-Old Copywriting Trick
Needs: a specific milestone they achieved and the unconventional method used to reach it
Echoes: T-LC6.5
```
I [achieved noteworthy milestone] without [relying on traditional expectation].
Because here's the thing:
[Short belief or principle that contradicts expectation or objection from above].
[Briefly explain belief or principle].
So, how do you [relevant question]?
* [Practical action/tip 1]
* [Practical action/tip 2]
* [Practical action/tip 3]
[Key takeaway that helps the reader see how your advice can benefit them].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC30.5 · found · proof · analytical · B · Reframing Negative Perspectives
Needs: a specific personal or client example with a starting metric and improved result
Echoes: T-LC15.2, T16.5
```
[Year/Timeframe 1]: [Something common or traditional people did]
[Year/Timeframe 2]: [How the practice has shifted or evolved]
[Introduce the central idea or insight].
And if your next question is:
* [Common doubt or fear posed as a question 1]?
* [Common doubt or fear posed as a question 2]?
* [Common doubt or fear posed as a question 3]?
I challenge you to change this to:
* [Reframed positive perspective 1]
* [Reframed positive perspective 2]
* [Reframed positive perspective 3]
[Share a personal or client example of progress or success, starting from a low point and leading to a high point].
[Empowering takeaway that fosters optimism].
[Question for audience or call to action].
```

## CASE (8)

### T-LC4.5 · go · case · analytical · B · How to champion a hero in a brand's success story
Needs: a named brand's real strategy, specific industry shift, and turnaround metrics
Echoes: T13.4
```
[Brand's success story] is a testament to [key strategy]. [Impressive metric].
Let's dive into the journey:
During [time period], [Brand] was at the peak of its game. 
[Mention specific achievement].
Their strategy was simple: [Original strategy].
This approach worked great… 
Until [specific industry shift] led to [bad outcome].
By [date], [low point occurred].
[Brand] decided to pivot.
[Team/Business unit] doubled down on [alternative strategy] after they realised [key realisation].
They implemented:
1. [Solution 1]
2. [Solution 2]
3. [Solution 3]
The outcome? [Brand]'s renaissance is a story of [relevant lesson]
Many companies face [common challenge] because of [industry shift].
[Brand]'s story shows the importance of [summarise solution].
Now, [Brand] stands as a beacon of [achieved goal], with [success metric].
[Image that matches the post]
```
### T13.4 · found · case · warm · A · One of the most powerful (but underused) tactics in personal branding
Needs: a specific named-concept client transformation story with real quotes and dialogue
```
My client [dramatic before situation]. [Timeframe] later, [dramatic after situation].
[They were a person from a specific background] who [context that sets up the challenge].
[Specific injustice or wound that created the problem]. [Clarification that deepens the injustice] - but [they] still [consequence] for the [surprisingly small triggering action].
When I met [them], [they were]:
- [Impressive credential]
- [Impressive credential]
- [Impressive credential (with humour)]
On paper, [they] had no business hiring [a professional like me].
My first thought was, "[surface-level reactive question]?"
My second thought was that [their] problems were real. Experiencing [X years of Y] probably [led to negative consequence].
[One day/night], we [did something]. All we did was [deliberately simple method].
[They achieved the specific result].
Afterwards [they] turned to me and said, "[payoff question]?"
"[Loaded reply that implies the full story without stating it]."
That's the strange thing about [Named Concept] - you can have [objective quality], [objective quality], [objective quality] - and still [the false belief they carry].
My client was living a [diminished version of life] because [they were] carrying [a false story] about [themselves] for over [timeframe].
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T18.1 · found · case · analytical · B · Named case study, minimalist verdict
Needs: a named client and their specific starting requirements plus the outcome achieved
```
Some [group/clients] don't need [expected element].
[Person's name] is one of them.
[Introduce person / give context / give proof].
We skipped [expected addition 1].
We skipped [expected addition 2].
[Briefly list key elements that make up your approach].
Because [person] already had what mattered:
- [Key requirement 1]
- [Key requirement 2]
- [Key requirement 3]
When those [X] are solid, you don't need to add anything else.
Most people think [common practice] means more.
More [thing]. More [thing]. More [thing].
But often the strongest move is [counterintuitive quality].
Let [element] breathe.
Let [element] do the work.
Let [element] land without competing.
A [minimal version] says "[confident statement]."
A [cluttered version] says "[insecure statement]."
Good [skill/craftspeople] knows when to stop.
Most people don't.
[Question for audience or call to action].
[Image that matches the post]
```
### T11.5 · found · case · analytical · B · Free-strategy case study to sell a service
Needs: a client's specific starting problem, the process used, and the specific result achieved
Echoes: T18.1
```
When I [do service] for [client type], here's how I make sure [I achieve desirable outcome].
A [client type - e.g. "founder"] reached out to me [time period ago] because they'd been [doing the thing] for [timeframe], had [positive quality], but [state problem] - and couldn't figure out why.
[Their output/set-up] looked fine, but it wasn't actually doing anything for [their goal].
So I walked them through my process, and it starts way before I [do the obvious part of the service]:
1. [Explain step 1 - the key actions and give a brief explanation as to why they're important].
2. [Explain step 2 - the key actions and give a brief explanation as to why they're important].
3. [Explain step 3 - the key actions and give a brief explanation as to why they're important].
Within [short timeframe], [client] had [specific, concrete result] - no [effort-intensive alternative], no [cost-intensive alternative].
[One-sentence philosophy about what the service should do at its best].
If [you have the symptom described in the opening], that's exactly the gap I fill.
[Question for audience or call to action].
[Image that matches the post]
```
### T2.1 · found · case · analytical · B · Borrowed credibility hook
Needs: a named client's exact question plus specific trends found in your results
```
[Time period ago], [individual/company] told me:
[Briefly explain their question/goal/problem].
I looked back at all the [content/work/actions] that ever [drove the result they wanted] for me from [early milestone] to [current milestone].
There were [X] clear trends:
* [Finding 1]
* [Finding 2]
* [Finding 3]
[Distil a common thread between the findings].
It wasn't [common assumption 1] or [common assumption 2] driving [the result].
It was [the real driver].
This might sound [anticipated objection]. But it's not.
It's actually the [reframe how it's easier/simpler/cheaper than expected]. 
Because you're just:
[List or state relevant actions/steps/tips].
(+ here's the system I use to [get result] fast: [resource link])
[Question to prompt reflection]?
PS. [Question for audience or call to action].
```
### T-LC9.2 · found · case · analytical · B · How to write a post that sells
Needs: a client's starting point, a direct quote from them, and their specific results
Echoes: T11.5
```
How my client [achieved desirable outcome] in [timeframe] 
(with [specific method])
[Briefly explain client's starting point]
But they [encountered problem]
They said:
"[Direct quote from client expressing their struggle]"
I suggested they [solution offered].
* Reason why/benefit
* Reason why/benefit
* Reason why/benefit
Here's what we/they did next:
* Strategic step 1
* Strategic step 2
* Strategic step 3
The result?
[Mention key positive results/outcomes].
[Give inspiring takeaway].
PS. If you're interested in achieving the same in [timeframe], [relevant call to action]
```
### T-LC22.5 · found · case · warm · B · The No.1 Way To Boost Your Authority, Land More Clients & Start Charging More
Needs: a named client, their starting state, specific results, and an actual testimonial quote
Echoes: T5.4, T-LC9.2
```
I met [Client Name/Person] [time period] ago.  
They were [starting state - e.g. struggling with..., at a specific level, etc.].  
[Timeline list of specific engagements or interactions showing incremental coaching, training, or consulting sessions].  
Today, they [current success level or recent milestone].  
By [next year/future date], they'll [future goal or ambitious projection].  
[Give a key reason(s) for success].
To [reach desirable outcome A] 
To [overcome specific obstacle] 
To [reach desirable outcome B] 
Over [time span], I've helped them:
* [Unlock skill/technique/benefit]
* [Unlock skill/technique/benefit]
* [Unlock skill/technique/benefit]
They've mastered [key progression].
And recently, they left me this [video/message/testimonial].
[Outline relevant offer and current availability].
My [product/service] can help you:
* [Unlock desirable outcome 1] 
* [Unlock desirable outcome 2] 
* [Unlock desirable outcome 3] 
[Inspiring sign-off].
[Call to action].
[Include image or video testimonial]
```
### T-LC24.2 · found · case · warm · B · How To Write A (Valuable) Case Study
Needs: a named client, their starting situation, and the specific results achieved
Echoes: T13.4, T-LC9.2, T-LC22.5
```
This is my [relation/friend/client], [Person's Name].
I helped them [achieve specific, impressive result].
If you want to [achieve goal], read this:
I met [Name] in [timeframe].
At the time, they were [describe the initial situation].
Fast forward to today, they're [describe the transformation].
The problem with most [profession/role/group] is [specific issue].
So, we focused on fixing [specific areas or challenges].
We implemented [framework/strategy/method] to help them [unlock benefit].
Here's how it works:
[List and briefly explain each step involved - consider including issues overcome, questions to aid reader reflection, any unique frameworks you used, and any desirable outcomes or impressive results they achieved along the way].
With these changes, [Name] went from [before state] to [after state].
Now, they [describe current success].
If you want to [pursue goal/unlock key desirable outcome], [relevant call to action].
[Image that matches the post]
```

## ABOUT (5)

### T2.5 · found · about · warm · A · 90-day re-introduction post
Needs: a personal origin story, prior identity and how the journey started
Echoes: T16.1
```
I'm [age], [nationality], [personality trait/fact], and run a [brief business descriptor].
Last [time period ago], [specific metric/accolade achieved].
What [we/I] sell:
[List products/services you offer + prices (optional)].
How we [market/sell]:
* [Channel/method] [cadence]
* [Channel/method] [cadence]
* [Channel/method] [cadence]
Tools [we/I] use:
* [Tool 1] ([what it does])
* [Tool 2] ([what it does])
* [Tool 3] ([what it does])
Where I started:
[X] years ago, I was [previous identity] who knew nothing about [relevant skill set]. I just wanted [modest original desire]. Today, I [brief description of where you're at now].
If you do a fraction of this, you can [scaled-down version of the result]. You just need [three simple ingredients].
[Warm sign-off].
[Image that matches the post]
```
### T-LC12.2 · found · about · warm · A · Is your account growing? If so, do this intermittently…
Needs: a specific personal origin story, hometown, background, and journey timeline
Echoes: T2.5, T1.5
```
I began my journey in [field/industry] [time period] ago.
Hi, I'm [Your Name].
Originally from [Original Location], I now live in [Current Location].
My background includes [time period] in [industry or field] - specialising in [specific skills or areas].
I had no prior knowledge of [new skill or field] when I started.
But after [time period], things began to pick up:
- [Key achievement/benefit unlocked]
- [Key achievement/benefit unlocked]
- [Key achievement/benefit unlocked]
Now, I'm focused on [current goal or business focus].
Along the way, I offer [type of advice or service you provide].
[Additional interesting personal fact]
[A quirky or engaging question to engage reader]
[Call to action]
[Image that matches the post]
```
### T16.1 · found · about · warm · B · What a post written by an actual human looks like…
Needs: real age, birthplace, quirky personal facts, and named client results
```
I'm [age]. Born in [place]. Raised in [place]. Now live in [place]. I [profession/role in one line] and I run a business with [person OR include another interesting fact about your business].
- [quirky personal fact 1]
- [quirky personal fact 2]
- [quirky personal fact 3]
- [quirky personal fact 4]
- [quirky personal fact 5]
- [quirky personal fact 6]
[Time period 1] ago, I started [initial venture/offering].
[Time period 2] ago, I [realized/did/achieved X].
[Time period 3] ago, I [realized/did/achieved Y].
Now [I/we] run a business that:
- [State what you do in one line]
- [State second thing you do / outcome you drive]
- and [State third thing you do / outcome you drive]
And it's working. Some recent client results:
- [Client result 1]
- [Client result 2]
- [Client result 3]
[Image that matches the post]
```
### T15.3 · found · about · playful · B · The case for getting personal on LinkedIn
Needs: five real personal facts/hobbies not previously shared on their LinkedIn
```
[X] things you probably wouldn't know about me from my LinkedIn:
1. [Personal interest/hobby/fact/realization 1]
2. [Personal interest/hobby/fact/realization 2]
3. [Personal interest/hobby/fact/realization 3]
4. [Personal interest/hobby/fact/realization 4]
5. [Personal interest/hobby/fact/realization 5]
I don't feel like talking about work today, so tell me something I wouldn't know about you!
[Image that matches the post]
```
### T14.3 · found · about · warm · B · A cheeky way to maximize reach once (or twice) a year
Needs: real personal achievements and honest missed goals from a specific year
```
I'm [age or milestone marker]. Here's some highlights from being [previous age or stage]:
- [Achievement/milestone/remarkable event 1]
- [Achievement/milestone/remarkable event 2]
- [Achievement/milestone/remarkable event 3]
- [Achievement/milestone/remarkable event 4]
- [Achievement/milestone/remarkable event 5]
Some things I didn't do as much as I'd have liked:
- [Missed goal + brief context/reason 1]
- [Missed goal + brief context/reason 2]
- [Missed goal + brief context/reason 3]
[Previous period(s)] was [brief, honest assessment].
[Current period] [brief forward-looking statement].
[Image that matches the post]
```

## CONTRARIAN (30)

### T16.2 · go · contrarian · analytical · B · Apply this "everyone wants X, nobody wants Y" thesis hook to almost any domain
Needs: a named study/authority and its specific data findings that contradict an assumption
```
Everyone wants [desirable outcome].
Nobody wants to do what it actually takes.
And I have bad news, because it takes...a LOT.
[Authority/source] finally confirmed that [common assumption] is [wrong/misguided]. [Briefly explain why].
So if [precondition], you likely won't [desired result].
Then there's the question of [related unresolved issue].
[Data source] data shows [surprising finding that contradicts assumption]. Not [expected answer]. [One-line explanation of why].
The logic:
[Core mechanism, stated plainly, first cause].
[Second cause explained]. [Include second data point - if applicable].
You heard that correctly: [punchy restatement of the insight].
And finally, dear [target audience], [common goal] might not be the [desirable thing] you think it is. Another study by [source] found [briefly explain surprising finding].
The rest [alternative reason for the outcome], not because [original assumption].
So stop chasing [false goal].
Build [the real, sustainable goal].
[Image that matches the post]
```
### T1.4 · go · contrarian · analytical · B · The Qualification Sandwich
Needs: a stated industry opinion and a real benefit from the alternative approach
```
I'm seeing [platform / craft / industry shift].
(and [share quick opinion])
It's okay to [take a break from / stop common practice].
I have nothing against it. I've done it too.
But there's real value in [alternative approach].
[Expand on why this alternative approach is effective and/or beneficial].
[Briefly share how it's helped you].
So [reinforce key directive - eg. take a break from common practice]
[Key takeaway(s)].
```
### T13.1 · go · contrarian · bold · C · Your content needs an enemy
Needs: only a contrarian positioning stance and decision criteria, no personal facts
```
I've [verb] [negative quality] [subject/role] from [specific context].
I've [verb] [positive quality] [subject/role] from [specific context].
You can be a [relevant metaphor] and claim that [success/result] your entire [career/life].
You can also be a [positive quality] [subject/role] who made the best of [unfavourable circumstances].
Don't [make decisions] based on [the superficial signal everyone defaults to].
[Make decisions] based on [criterion 1], [criterion 2], and [criterion 3].
```
### T10.5 · go · contrarian · bold · C · Permission-giving contrarian post
Needs: only a contrarian mindset stance, no personal facts or client specifics
```
Oddly unpopular take:
[Core contrarian stance].
If you are [the behaviour being defended]… don't apologize for it.
You don't have to [social expectation 1].
You don't have to [social expectation 2].
You don't need to [expected behaviour].
It's okay if you're in your [name the season or phase].
It's okay to be [word society uses as criticism].
[One or two sentence justification that reframes the behaviour as rational or necessary.]
[Key takeaway].
[Relatable text image to act as a 'billboard' for your post]
```
### T9.2 · go · contrarian · playful · C · The Midwit Razor is (still) undefeated
Needs: only an industry-trend critique and the writer's own take, no personal facts
```
[Familiar concept] has been getting a rebrand for months.
[New name 1], [New name 2], [New name 3], ...
Then every week I read [content type] pushing new '[rebrand name]' tactics.
"[Recycled advice 1]"
"[Recycled advice 2]"
"[Recycled advice 3]"
"[Recycled advice 4]"
The Midwit Razor kicks in:
Looking at these [rebrand name] tactics, what would the "idiot" and the "genius" both agree on?
Answer: "It's just [the original concept]"
That's 90% of the [rebrand name] advice out there.
These are [decades/years]-old [original discipline] tactics repackaged as revolutionary findings.
[Briefly share your take].
[Question for audience or call to action].
[Image that matches the post - e.g. Midwit meme with relevant annotations]
```
### T8.1 · go · contrarian · bold · C · Why this viral post is so damn satisfying
Needs: researched examples of past failed "industry is dying" predictions, including one dated named-figure quote
```
[Industry/concept] has been dying since [year].
Some notable "deaths" include:
- [Failed prediction 1]
- [Failed prediction 2]
- [Failed prediction 3]
- [Failed prediction 4]
- [Failed prediction 5]
- [Failed prediction 6]
- [Failed prediction 7]
- [Failed prediction 8]
So now... [current narrative/new threat]?
Here's the reality:
- [Data/observation that counters above narrative]
- [Data/observation that counters above narrative]
- [Data/observation that counters above narrative]
[Define thing people claim is dead].
[Reason why definition supports counter-narrative].
The "[threat]" narrative is wrong. [New thing] won't kill [industry/concept]. [New thing becomes a component/enabler of it].
In [specific date], [named figure] declared [bold prediction about the industry's collapse].
Don't be [him/her] in [this year].
[Industry/concept] is very much alive.
It's just evolving.
[Image that matches the post]
```
### T-LC4.3 · go · contrarian · analytical · C · How to fix BROKEN thinking
Needs: only domain expertise on the common misconception and a general reframe strategy
```
Why does [specific audience] face [common problem]?
Because they believe [common misconception].
Here's my [unique strategy] to help you [unlock desirable outcome]:
The reality is, [summarise why the problem exists].
The secret lies in [specific solution].
Benefits of this approach include:
1. [Benefit 1]
2. [Benefit 2]
By adopting [specific strategy], you eliminate [specific problem] and [unlock desirable outcome].
Here's how to think about it:
* [Mental reframe/tip]
* [Mental reframe/tip]
* [Mental reframe/tip]
So when you [plan your strategy], here are [X] things to consider:
* [Strategic component 1]
* [Strategic component 2]
* [Strategic component 3]
* [Strategic component 4]
* [Strategic component 5]
Here's an example:
Instead of [common approach], try this:
* [Strategic component 1 - example]
* [Strategic component 2 - example]
* [Strategic component 3 - example]
* [Strategic component 4 - example]
* [Strategic component 5 - example]
[Expand on why this method unlocks desirable outcomes].
[Image that matches the post]
```
### T-LC4.4 · go · contrarian · punchy · C · Here's a reality check for ya!
Needs: only domain expertise on realistic limits of the role/industry, no client specifics
```
"[Industry/Role], [unrealistic request]."
X things [Industry/Role] can't fix:
1. [Common misunderstanding 1] - [Harsh truth].
2. [Common misunderstanding 2] - [Harsh truth].
3. [Common misunderstanding 3] - [Harsh truth].
[Industry/Role] can achieve [positive outcome].
But it can't [meet unrealistic expectations].
Please remember this.
```
### T-LC5.2 · go · contrarian · bold · C · "You've been lied to. Here's the truth…"
Needs: only a contrarian industry opinion and general reasoning, no personal specifics needed
```
[Specific harsh truth].
[Necessary action/belief] is essential to [achieve desirable outcome].
Whether that's [example 1 of action to take], or [example 2 of action to take].
If you don't [take recommended action], [negative consequence].
"[Common but misguided belief]"
[Statement that rejects belief].
The truth is [impact of maintaining misguided belief].
```
### T-LC6.1 · go · contrarian · punchy · C · Can you tell WHY this post went viral?
Needs: only a general strategy-comparison framework, no personal or client specifics needed
```
The difference between [strategy A] and [strategy B] is: 
[Key negative outcome associated with strategy B that's often overlooked].
For [strategy A], you get [summarise key advantage].
[Share practical takeaway].
```
### T-LC6.2 · go · contrarian · playful · C · How to use analogies to make your point
Needs: only an analogy and domain reasoning about an unfair industry norm
```
"[Common but controversial business practice posed as a statement by uninformed culprit]"
Wait a minute.
You would never [example of unfair practice occurring in another domain where it's not the norm].
You would [list usual, fair behaviours].
Why then do we see this as acceptable in [industry/field]? 
Instead of [unfair practice], let's focus on:
- [Alternative method/step 1]
- [Alternative method/step 2]
- [Alternative method/step 3]
- [Alternative method/step 4]
[Highlight how the culprit may justify unfair practice] [then briefly dispute this justification].
[Concluding statement/takeaway]
```
### T-LC6.4 · go · contrarian · analytical · C · The problem with attention-grabbing phrases
Needs: only domain commentary on overused content tactics and a named alternative approach
```
[Pose a common concern as a question]?
- [Problematic trend 1]
- [Problematic trend 2]
- [Problematic trend 3]
[Briefly give your point of view]
So rather than [conduct misguided behaviour], [list recommended behaviours/strategies].
Doing so will [unlock these benefits].
This approach is [name or define approach/strategy].
For a step-by-step breakdown, check out my latest [content medium - e.g. newsletter].
Link in the comments.
```
### T-LC10.5 · go · contrarian · bold · C · The dark side of LinkedIn
Needs: only general industry/platform observations about deceptive norms, no names needed
```
[Hint at deceptive behaviour on platform/industry/context].
Don't get me wrong, I enjoy [platform/industry/context].
But there is a dark side.
For example, sometimes I see:
* [Negative/deceptive behaviour 1]
* [Negative/deceptive behaviour 2]
* [Negative/deceptive behaviour 3]
So if you [engage on platform/industry/context], and you're [negatively impacted]...
Remember, [positive/inspiring takeaway].
[Include relevant image/image hook]
```
### T-LC13.1 · go · contrarian · bold · C · The secret to writing content that hits the dopamine button
Needs: domain expertise to reframe a common belief with supporting examples, no personal facts
```
"[Provocative statement that challenges a common belief]."
[Truth that contradicts the common belief].
[Briefly elaborate on core idea].
- [Example of action related to truth 1]
- [Example of action related to truth 2]
- [Example of action related to truth 3]
- [Example of action related to truth 4]
- [Example of action related to truth 5]
[Personal observation or insight - e.g. about people who have embraced the truth and succeeded].
[Key takeaway].
[Call to action or question for the audience].
[Video or image that matches the post]
```
### T-LC15.1 · go · contrarian · bold · C · You've been lied to (here's the truth…)
Needs: domain expertise to identify five common industry myths and their blunt realities
Echoes: T-LC5.2
```
X [industry/field] lies:
"[Common falsehood people/companies say]"
↳ [The blunt reality - consider using sarcasm to heighten the discrepancy]
"[Common falsehood people/companies say]"
↳ [The blunt reality - consider using sarcasm to heighten the discrepancy]
"[Common falsehood people/companies say]"
↳ [The blunt reality - consider using sarcasm to heighten the discrepancy]
"[Common falsehood people/companies say]"
↳ [The blunt reality - consider using sarcasm to heighten the discrepancy]
"[Common falsehood people/companies say]"
↳ [The blunt reality - consider using sarcasm to heighten the discrepancy]
[Impactful closing statement or question to foster engagement].
```
### T-LC15.2 · go · contrarian · analytical · C · How to dispel false beliefs (that stop people from buying)
Needs: general facts or stats debunking a common prospect misconception, not client-specific
```
What [specific group] say:
"[Common misconception framed as a quote]."
What's true:
- [Fact, stat, or benefit that supports the contrary].
- [Fact, stat, or benefit that supports the contrary].
- [Fact, stat, or benefit that supports the contrary].
- [Fact, stat, or benefit that supports the contrary].
[Bold claim that reinforces core message].
[Empowering takeaway].
```
### T-LC16.1 · go · contrarian · bold · C · Where's My Tribe At?
Needs: domain knowledge of commonly criticized industry practices to rally the audience around
Echoes: T13.5
```
Don't [common industry practice that's often criticised 1].
Don't [common industry practice that's often criticised 2].
Don't [common industry practice that's often criticised 3].
... [Dismissive phrase implying the repetition of similar advice - e.g. "blah, blah, blah"]
Being a [profession/role] is already hard enough.
Those who can, [positive action or result].
And those who can't, [negative action].
```
### T-LC16.4 · go · contrarian · bold · C · How to Win Trust by Being (Too) Honest
Needs: domain expertise to challenge a common belief and offer alternative steps
Echoes: T-LC4.4
```
This may lose me some business, but it has to be said:
[Present a core principle or insight that challenges common thinking].
In other words, [insert a metaphor or common saying to reinforce your point].
Try this instead:
* [Strategic step or actionable tip]
* [Strategic step or actionable tip]
* [Strategic step or actionable tip]
* [Strategic step or actionable tip]
[Key takeaway].
```
### T-LC28.3 · go · contrarian · bold · C · "Don't Play The Engagement Game" - Ryan Musselman
Needs: only a contrarian niche opinion and an illustrative example of the right approach
```
[Platform/context/product] isn't for [outdated goal/focus] anymore - it's for [new goal/focus].
(But only for those who [take specific approach]).
Here's what most people do wrong:
[List common mistakes].
The truth is, [restate/reinforce key idea].
Don't play the [ineffective strategy] game.
If you're a [target audience] and you [describe area of focus], don't [take ineffective actions]. 
Focus on [action(s)/approach/strategy].
[Briefly expand].
Let's take an example:
[Describe an example of what to do instead].
Do you see the strategy here?
[Key takeaway(s)].
[Question for audience or call to action].
```
### T-LC29.5 · go · contrarian · bold · C · A Great Way To Dramatise Your Writing
Needs: only a contrarian opinion and generic illustrative examples, no personal facts
Echoes: T-LC13.2
```
[Bold, contrarian statement that challenges conventional thinking].  
[Use short, rhythmic sentences to highlight the problems with this mindset or system].  
[Common misconception that's related to the core idea].  
[Define the core idea or concept that underpins your argument].  
* [Relatable example 1]
* [Relatable example 2]
* [Relatable example 3]
Most people [state common flawed action(s)].
Then [state negative consequence(s)].  
Try this instead:
* [Practical action/step 1]
* [Practical action/step 2] 
* [Practical action/step 3]
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC30.3 · go · contrarian · bold · C · How To Work Smarter, Not Harder
Needs: only a contrarian opinion about an outdated common practice and its smarter alternative
Echoes: T-LC28.3, T-LC19.1
```
Please STOP [doing common and/or ineffective practice].
I see too many [examples of people/businesses doing this] that [describe the negative outcome], yet they're still [repeating the ineffective practice].
If you're already [doing related action], try this instead:
* [Actionable step 1]
* [Actionable step 2]
* [Actionable step 3]
* [Actionable step 4]
[Expand where needed AND/OR clarify what needs clarifying AND/OR include some relatable examples]
You'll achieve [positive outcome] much faster by [restating the new focus] rather than [repeating the ineffective practice].
Try it for the next [time frame] and see what happens.
[Question for audience or call to action].
```
### T-LC31.3 · go · contrarian · bold · C · How To Stand Out (Without Ruining Your Rep)
Needs: only a contrarian opinion rejecting common advice with bolder alternative actions
```
Most [field or industry] advice is [adjective 1].
And [adjective 2].
* "[Common advice 1]."
* "[Common advice 2]."
* "[Common advice 3]."
Ok, but that's not enough.
In [current or upcoming year], [professionals/group] need to do more.
For example:
1. [Bold action 1]
[Expand on why this action is important, and give actionable advice].
2. [Bold action 2]
[Expand on why this action is important, and give actionable advice].
3. [Bold action 3]
[Expand on why this action is important, and give actionable advice].
4. [Bold action 4]
[Expand on why this action is important, and give actionable advice].
[Key takeaway].
```
### T11.4 · found · contrarian · bold · A · Polarizing belief / permission-to-be-bold post
Needs: a specific years-long false belief the writer held and the moment it was disproven
```
[Bold universal claim about what's possible or what's true].
That's the uncomfortable truth most people never figure out.
[Personal admission of the mistake or false belief you held for years]. [What that looked like in practice, what you were waiting for or avoiding].
[The moment that revealed nothing happened / nobody cared / the fear was unfounded].
But [surprising and beneficial thing you noticed].
[Describe the specific fears or obstacles you anticipated - name 2-4 concretely].
[Single-line deflation: None of that happened / It never came / The response was silence].
[Give each feared obstacle a specific, mundane reason it never materialised].
I've watched this play out with [clients / people I coach / groups I've observed]. [Explain the pattern you observed, describe the behaviour - eg. the over-preparing, the polishing, the delay].
[Describe what actually happens when they finally take beneficial action].
[Name the realisation that hits. What did the fear actually cost them, and what was it protecting them from?]
[Reframe the broader system or environment - what's actually going on?]
But if you decide to [take specific action]? If you decide to [take the hard route]? [Summarise what will actually happen].
[Reinforce with a second personal proof point - a specific decision you made, the judgment you expected, and the reality of what followed].
The people who [achieve desirable outcome] aren't [positive trait] than everyone else. They just figured out that [sum up key realisation].
You don't need [perceived requisite 1]. You don't need [perceived requisite 2]. You don't need [perceived requisite 3].
You just need to start [key next action(s)].
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T16.3 · found · contrarian · bold · B · The Contrarian Spotlight
Needs: specific low-cost alternatives used with actual costs and outcomes achieved
```
[Contrarian claim about what's not required to succeed].
I think we use that as a crutch - oh yeah sure, I'd do that too if I had [common excuse/resource].
No. [Restate the contrarian claim].
Some of my favorite [examples/plays/tactics]:
Instead of [expensive/conventional option], we [creative low-cost alternative] for [fraction of cost].
Result: [surprising or impressive outcome]
Instead of [expensive/conventional option], we [creative low-cost alternative].
Cost: [specific low number]
Result: [surprising or impressive outcome]
Instead of [expensive/conventional option], we [creative low-cost alternative].
Cost: [specific low number]
Result: [surprising or impressive outcome, plus a personal detail]
[Core philosophy in one line].
You can find creative ways to [achieve the goal] without [common assumption about what's required].
[Practical instruction 1]. [Practical instruction 2].
That's the fun part of [field] to me. Give me [scenario A], give me [scenario B]. We're going to [desired outcome] either way.
"[Relevant quote]" - [Attribution]
[Image that matches the post]
```
### T15.2 · found · contrarian · bold · B · How to HAMMER an idea into people's heads
Needs: the specific thing built in public and specific actions/topics deliberately skipped
```
Most people are [common, watered-down behavior in your field].
They [example 1].
They [example 2].
[Example 3].
They think [the false belief behind the behavior].
But it just [the real cost of that belief].
When you [the bold alternative behavior], you [immediate, uncomfortable consequence].
[Briefly expand on that consequence].
[Expand on how some positive consequences].
That's how you find [desirable outcome].
I built my whole [thing you built] in public, [doing this bold behavior].
No [action you didn't take] on [specific topic 1], [specific topic 2], or [specific topic 3].
I'm sure it's cost me [what you lost], but it's also built [what you gained that actually matters].
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T13.3 · found · contrarian · bold · B · Different is better than Better
Needs: a specific recent achievement and the concrete result number it reached
```
Sorry to tell you this BUT...
You're [provocative quality].
And so is the rest of the world.
There's a trend going around right now saying [cultural observation].
And at [Brand/name] we've fully leaned into it.
To bring some [quality/value] back. And the [result area] genuinely shows.
Because in a world of [status quo], the only way to actually get [desired outcome] is to [required action]. It's exactly why our [first/recent achievement] reached [specific result].
The [system] isn't trying to [feared assumption]. It's trying to [positive reframe]. 
So when you [follow the crowd], you're working against the [system]. 
[Briefly expand - if necessary].
We chose [value 1]. We chose [value 2]. We chose to [distinctive decision]. And the [briefly describe outcome].
So if your [work/output] feels [safe/generic] right now... that's probably exactly why it's not working.
[Key takeaway].
[Question for audience or call to action].
[Image that matches the post]
```
### T7.3 · found · contrarian · bold · B · Using AI to create content is not the real problem
Needs: a specific stated controversial opinion and how it applies to each client type served
```
Unpopular opinion:
I don't care if [controversial thing].
I work with [type of person/project].
[Tool/approach] lets [them/me] do that.
I work with [type of person/project].
[Tool/approach] helps [them/me] out.
I work with [type of person/project].
[Tool/approach] closes that gap.
So I don't care that [controversial thing].
I care that [what actually matters].
We can't just say all [thing] is bad.
[Give people a helpful reframe to help shift their perspective from negative to positive].
-[Tangible example/Practical next step 1]
-[Tangible example/Practical next step 2]
-[Tangible example/Practical next step 3]
[Key takeaway].
Disagree with me?
```
### T-LC9.1 · found · contrarian · punchy · B · What's the goal of your post?
Needs: a specific success metric achieved without the common practice, in a stated timeframe
```
Don't [common practice/action].
[Do these alternative action(s) instead].
[Give an underlying reason for doing so].
[Key benefit the alternative action unlocks].
[Take action on related strategy] to [reach desirable outcome].
We/I have [specific success metric] in [timeframe] without [undesired methods].
And [related strategy] is what made it possible.
```
### T-LC19.1 · found · contrarian · punchy · B · Why People Ignore Your Content
Needs: specific results the writer or their clients achieved using the recommended strategy
Echoes: T-LC9.1
```
Don't [insert common practice].
Start [alternative action(s)].
[Briefly list reasons why alternative action(s) are beneficial to the reader].
[Summarise the name and key desirable outcome of the strategy outlined above].
[Share results you or your customers have achieved using this strategy].
Without [strategy], none of this would have been possible.
```
### T-LC21.2 · found · contrarian · bold · B · Is It All Just BS?
Needs: five specific, genuinely-held contrarian opinions on common industry metrics or approaches
Echoes: T13.5, T-LC15.1
```
I've done a 180 and now hold to X [topic] beliefs:
1. I don't care about [common metric/approach/goal/mindset]; I do care about [alternative metric/approach/goal/mindset].
2. I don't care about [common metric/approach/goal/mindset]; I do care about [alternative metric/approach/goal/mindset].
3. I don't care about [common metric/approach/goal/mindset]; I do care about [alternative metric/approach/goal/mindset].
4. I don't care about [common metric/approach/goal/mindset]; I do care about [alternative metric/approach/goal/mindset].
5. I don't care about [common metric/approach/goal/mindset]; I do care about [alternative metric/approach/goal/mindset].
[Call to action or question for audience].
```

## INSIGHT (35)

### T-LC5.1 · go · insight · warm · B · Empower your reader to think differently
Needs: a specific statistic on how few people/initiatives hit the typical success bar
```
Only [a small fraction] of [specific initiatives/individuals] [achieve desirable outcome].
You don't have to follow [typical definition of success].
Define what success looks like for you.
Something you can look back on in [time period] from now with pride.
Perhaps that's [typical definition of success].
Or [alternative definition of success A].
Or even [alternative definition of success B].
Whichever path you choose, you're the one who decides.
[Personal sign-off/Call to action]
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC18.5 · go · insight · analytical · B · How to Make Obvious Insights Compelling
Needs: specific researched facts, names, stats and quotes about a real historic/news event
```
[Bold statement that sums up core lesson from historic event].
After [time period], [describe key recent event]. [Briefly describe how things were before this event in a way that illustrates the transformation].
But due to [key detail relating to this recent event], [share supporting facts or stats that demonstrate the overall outcome].
What happened?
[List reasons for what happened - include specific names, facts, and examples where possible].
The result was [Include another key fact, stat, or expert quote].
[Give your take on what happened - consider using a comparison or analogy to illustrate your point].
[Briefly describe a key event that's happened since the main event described above].
The lesson?
[Key takeaway].
[Image that matches the post]
```
### T-LC26.3 · go · insight · analytical · B · Validate Your Claims - Here's How
Needs: specific industry stats or facts that back up a bold claim
```
[Target audience] don't realise [briefly state hidden opportunity that exists].
[Compelling stats or facts that back up claim from above].
[Industry/field/role] is often seen as [negative stereotype].
But that's exactly why [target audience] should [take positive action]. 
[Benefits or reasons to pursue this course of action].
[Question for audience or call to action].
```
### T14.2 · go · insight · bold · C · It's your job as a creator to do THIS…
Needs: general industry insight into what evaluators actually prioritize now, no personal facts
```
[Role/group] won't tell you this.
But it's real. [Common belief] does not matter... as much as it used to [timeframe].
The first thing [role/individual] looks at when you [action] is not [assumed priority] anymore.
[Name what has actually moved into first position, with 2-3 examples segmented by situation, audience type, or use case].
Think of it this way. When you [relatable everyday scenario]. What do you do first? You [behaviour the reader already performs] to understand if [what they're actually checking for].
The same thing applies here.
If [role/individual] likes what they see with [the real priority], they are going to [take/have positive action/reaction].
As [relevant role you play], I don't [old behaviour] anymore, I [new behaviour].
[Question for audience or call to action].
[Image that matches the post]
```
### T13.5 · go · insight · bold · C · Your POV doesn't just attract customers
Needs: only a stated values/hiring philosophy, no personal facts or client specifics
```
I don't care [about the conventional metric everyone defaults to].
[Scenario 1]? [Short neutral acceptance].
[Scenario 2]? [Short neutral acceptance].
[Scenario 3]? [Slightly warmer acceptance].
[Scenario 4]? [Active encouragement].
I don't [hire/work with/choose] [people/things] to [control the conventional metric].
I [hire/work with/choose] [people/things] to [deliver the real outcome].
And if [the result] is there, I couldn't care less [about the conventional metric].
P.S. It's called [the underlying principle or value].
[Image that matches the post]
```
### T10.1 · go · insight · warm · C · Future pacing transformation post
Needs: only an imagined future-state narrative, no personal facts or client specifics
```
This will blow your mind...
It's [time frame] from now and you're:
[Everyday mundane action setting the scene.]
- [Specific desirable outcome #1]
- [Specific desirable outcome #2]
- [Specific desirable outcome #3]
[One sentence expanding the aspirational picture - contrast with current reality].
Here's what made the difference:
[Core behaviour or decision].
Because [short supporting truth borrowed or stated plainly].
No matter how:
- [Quality or effort that didn't save them]
- [Quality or effort that didn't save them]
- [Quality or effort that didn't save them]
[Absolute negative consequence of not doing the thing].
But [reframe - address the most common misconception].
It starts with one thing:
[The single pivotal insight].
[Briefly expand on what that enables or the broader strategy at play].
[Cost of inaction 1].
[Cost of inaction 2].
[Cost of inaction 3 - most painful].
[Reframe the outcome as logic, not luck].
[Reduce it to simple arithmetic].
That's how [identity before] become [identity after].
That's how [underdog description] become [aspirational description].
[Short motivating directive 1].
[Short motivating directive 2].
[Short motivating directive 3].
Because [time frame] from now, you'll either be exactly where you are today or exactly where you want to be.
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T9.4 · go · insight · warm · C · Only ONE person reads your content
Needs: only a values-driven reframe about human connection, no personal facts
```
Stop [doing the common thing]. Start [doing alternative thing].
We've become obsessed with [behaviour].
[Parallel phrase - e.g. "Chasing X instead of Y. Optimising for Z, not W"].
But [system] doesn't [work according to the story you're telling yourself].
It doesn't [feel/see/value] your [human quality].
[Group/method] [do/does].
And here's what most people forget:
[Core reframe - a counterintuitive way of seeing the audience or the task].
[One sentence that makes the reframe concrete and visceral].
When you [do the wrong thing]:
- [Negative outcome 1]
- [Negative outcome 2]
- [Negative outcome 3]
When you [do the right thing]:
- [Positive outcome 1]
- [Positive outcome 2]
- [Positive outcome 3]
[System] will change tomorrow.
[The platforms/tools/rules] will change next quarter.
But [the human constant] remains constant.
And the best part?
When you stop [chasing the system] and start [doing alternative], [system] often rewards you anyway.
Because [platforms/markets/audiences] ultimately want: [simple thing].
[Key takeaway].
[Image that matches the post]
```
### T8.5 · go · insight · punchy · C · Quick tip to hold your reader's attention
Needs: only a general industry principle/metaphor about over-optimization, no personal or client specifics
```
You [over-optimised] [thing] so much it [negative metaphor].
Now it [negative consequence 1].
There's this quiet assumption in [industry/niche] that if it's [desirable quality], it's probably not [legitimising quality] enough.
So everything [negative consequence 2]. [Descriptor]. [Descriptor]. [Descriptor]. And technically... fine. But also [negative consequence 3].
The thing is, the [outcome you're looking to unlock won't come from this flawed approach]. It comes from [desirable alternative]. 
That's where the opportunity is.
The [brands/people/teams] that [unlock desirable outcome] aren't [louder/bigger/more expensive]. They're just [quality 1], a little more [quality 2], and a lot more [quality 3] about how they [do the thing]. They [achieve the goal others want]... just without [unnecessary obstacle].
And that difference adds up quickly.
Because when something is [easier to X], it's [easier to Y].
And when it's [easier to Y], it's a lot easier to [desired action].
So no, [category] doesn't have to be [the negative trait]. It just has to stop [with flawed approach].
[Image that matches the post]
```
### T4.1 · go · insight · warm · C · What your prospective customers actually want
Needs: only general knowledge of audience identity types/behavior patterns, no personal facts
```
Many [people/group] want [desirable change/outcome].
But most of them never [identify invisible barrier that holds them back].
[Identity A] [default behaviour pattern].
[Identity B] [upgraded behaviour pattern].
If you're interested in [achieving the desirable outcome], [introduce your offer/resource and how to access it].
[Post image - e.g. A two-column comparison graphic. Example title: "[Identity A] vs [Identity B]"]
```
### T3.4 · go · insight · analytical · C · POV-driven strategy post (content people are starving for in the Age of AI)
Needs: domain expertise, a general strategy framework for a client type
```
Your [team/department/strategy] is [driving impressive metric] this year. But your [key person/strategy] is [driving low metric].
The solution isn't to [obvious but wrong approach] because that just [briefly example why it's a mistake].
Instead, [briefly sum up your alternative solution].
A few strategies that I use with [client type]:
1. [Step/Strategy 1]
[Tips/Sub-steps/Questions].
2. [Step/Strategy 2]
[Tips/Sub-steps/Questions].
3. [Step/Strategy 3]
[Tips/Sub-steps/Questions]
Outcomes:
[List benefits or state key desirable outcome].
[Key takeaway that reframes this core distinction].
[Question for audience or call to action].
```
### T1.5 · go · insight · analytical · C · Be remembered, not just seen
Needs: domain expertise, a general industry-shift observation and positioning stance
```
[Target audience/peer group] never [challenge common belief].
It was just easier to believe we did when [explain old dynamic].
Today, [describe how things have changed].
Recently, I've been reflecting on one core shift:
[long time period] ago, the goal was [surface-level objective].
[shorter time period] ago, the goal was [surface-level objective].
Now, the goal is [deeper, more strategic objective].
Here's what most people will take away from this: [common but ineffective practices].
Please don't do that.
Instead, [list alternative, effective practices].
[Key takeaway(s)].
[Image that matches the post]
```
### T-LC1.3 · go · insight · playful · C · The Slippery Slide Effect
Needs: domain expertise, general conceptual musing and a future-content tease
```
[Concept 1] = [Outcome 1]. [Concept 2] = [Outcome 2].
It's not the [concept 1/desire] we want. It's the [deeper desire].
Yet...
We all know the cliche, [common saying or belief]. Despite the [deeper desire], many let [concept 1/desire] shackle them in a new way.
The new [ideal goal] is to be [desirable state]. How do you achieve this?
I got obsessed with this idea as I began [hitting my goals]. I've spent [considerable timeframe] getting to know [relevant individuals/topic], and studying those who [reached desirable state].
What do you think the answer is?
It's an idea I've been organising my thoughts on for a while. Sometime in [timeframe], I'll have a [content asset] out on it.
Feel free to [subscribe/follow/sign up] if that's something you'd want to see: [Link]
```
### T-LC3.4 · go · insight · warm · C · Pair your advice with credibility elements
Needs: only a named principle/rule and generic supporting advice, no personal specifics needed
Echoes: T11.1, T7.4
```
[Name of Rule/Wisdom]:
[Context] is tough. [Setbacks] happen. 
Ensure your next action aligns with your goals.
* [Experienced specific setback]? [Respond with positive related action].
* [Experienced specific setback]? [Respond with positive related action].
* [Experienced specific setback]? [Respond with positive related action].
[Share relevant quote/wise advice]
[Reiterate Rule/Wisdom as practical takeaway]
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC7.2 · go · insight · warm · C · Why 3 is the magic number
Needs: only a generic trait list describing an ideal boss/client type, no specific person needed
```
Ever had a [role A] who felt more like a [role B]?
For them, it's not just about [expected value]. It's also about:
* [Additional value 1]
* [Additional value 2]
* [Additional value 3]
Here's how they do it:
1. They [positive trait or action with explanation 1]
2. They [positive trait or action with explanation 2]
3. They [positive trait or action with explanation 3]
4. They [positive trait or action with explanation 4]
5. They [positive trait or action with explanation 5]
[Summarise their positive actions on you or the business]
P.S. Does this remind you of any [role A]s?
Mention them in the comments.
[Call to action]
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC7.5 · go · insight · analytical · C · Reinforce what people already believe
Needs: only a generic list of the most valued traits in an asset/team/tool
```
The most important [specific asset/trait/quality] any [target audience] can have is an [asset/person/team/strategy/tool] who/that [prioritises desirable trait/quality].
* [Key quality or action 1]
* [Key quality or action 2]
* [Key quality or action 3]
* [Key quality or action 4]
* [Key quality or action 5]
[Summarise the advantage or importance of having such an asset/person/team/strategy/tool].
```
### T-LC9.3 · go · insight · analytical · C · How do you get the reader to remember you?
Needs: only domain knowledge of common audience behaviour and why it happens
```
Why do [target audience] [perform action] on/in [platform/tool/scenario]?
You may have seen:
* Example of related behaviour
* Example of related behaviour
* Example of related behaviour
Why do this?
[Briefly explain the reasoning].
Next time you [encounter relevant scenario], ask yourself:
[Question that prompts observation from reader]?
[Fact to reinforce key point]
Here are X tips to [unlock key benefit]:
* Actionable tip/advice
* Actionable tip/advice
* Actionable tip/advice
[Question to foster engagement]?
```
### T-LC11.4 · go · insight · analytical · C · Why "going viral" shouldn't be the goal
Needs: only a reframing metaphor and general steps to achieve the outcome
```
[Target audience]: you don't want your [asset/output] to "[common misconception]."
Instead, you want it to [vivid metaphor that describes what asset/output should be like].
In other words:
* [Specific characteristic that describes what asset/output should be like]
* [Specific characteristic that describes what asset/output should be like]
* [Specific characteristic that describes what asset/output should be like]
Or you risk [negative consequence(s) occuring].
Here are X ways/steps to [achieve desirable outcome]:
* [Actionable insight/step]
* [Actionable insight/step]
* [Actionable insight/step]
* [Actionable insight/step]
[Key takeaway].
```
### T-LC12.1 · go · insight · bold · C · This is one of the hardest hooks to nail
Needs: only a single sharp insight about readiness preceding tactics, no personal facts
```
If your [organisation/department/team] isn't ready to [desired change or action], all the [common practice or resource] in the world won't matter.
```
### T-LC14.1 · go · insight · bold · C · Tapping into the human desire to belong
Needs: domain expertise to frame a skill or habit as an elite-group essential
```
Quick reminder: [Skill/Habit/Routine] isn't JUST for [expected group].
[Aspirational group] all know that [skill/habit/routine] is [relevant descriptor]. 
They use it [list/briefly explain key benefit(s)].
It takes [relevant investment] to [learn/implement/benefit from] [skill/habit/routine].
But if you [understand/follow these steps]:
* [Fundamental/Step 1]
* [Fundamental/Step 2]
* [Fundamental/Step 3]
Then you can [unlock desirable outcome(s)].
[Personal sign-off].
[Call to action].
[Include relevant image/image hook]
```
### T-LC16.5 · go · insight · warm · C · Want Your Idea to Really Resonate? Try This…
Needs: domain expertise to build a vivid negative future-state scenario and remedy steps
Echoes: T10.1
```
Imagine waking up [years from now] and [briefly sum up negative future state].
* [Downside 1]
* [Downside 2]
* [Downside 3]
* [Downside 4]
* [Downside 5]
And to top it off, [key negative outcome].
You'd probably find this [negative emotion].
It would mean [explain the core message-why this scenario is undesirable].
To [achieve a desirable future state], [key concept] is crucial. But it doesn't happen by accident.
[Brief analogy or metaphor that helps reader better grasp key concept].
How is this made possible?
[Key actionable takeaway].
[Expand on why adopting this advice is beneficial].
[List specific actions/steps necessary for achieving relevant goal].
Here's a bonus: as you [take key action] you'll [unlock unexpected benefit(s)].
You'll no longer be happy settling for less. You'll keep [relevant progression].
[End with an inspiring note on progress and/or a key takeaway].
[Call to action and/or question for audience].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC18.3 · go · insight · warm · C · Ever Feel Like You Have Nothing of Value to Share?
Needs: only expertise-based framing of a common misconception in their field
```
You are [unexpected insight that holds many of your audience back].
You think [relatable misconception] because [briefly explain why people believe this].
[Key takeaway that frames a new, better way to think].
[Practical advice].
```
### T-LC20.3 · go · insight · warm · C · "What's The Benefit Of The Benefit?"
Needs: only domain knowledge of the audience's common problems, excuses, and offer fit
```
This [week/month/year] has been tough for me.
* [Specific problem faced]
* [Specific problem faced]
* [Specific problem faced]
[Briefly reflect on struggle].
Sure, I could make excuses, like:
* [Current obstacle faced/common excuse people give]
* [Current obstacle faced/common excuse people give]
* [Current obstacle faced/common excuse people give]
But such is life. No one gets out alive.
[Sum up key reason why for challenges faced].
And for most [target audience], when things go wrong:
* [Typical misguided action]
* [Typical misguided action]
* [Typical misguided action]
But I'm not worried.
Because I [have the specific solution needed to unlock desirable outcome].
And that's the problem I'm here to solve.
So if you're [target audience], and you're tired of [pain point], and want to [unlock benefits]...
[Relevant call-to-action]
And [unlock key desired outcomes].
PS. [Question to prompt reflection or engagement]?
[Image that matches the post]
```
### T-LC21.5 · go · insight · analytical · C · The Old Way vs. The New Way
Needs: only domain knowledge of the old convention's origin and the proposed new approach
```
The traditional approach to [mention conventional system or model] originated in [mention historical time frame].
But it's no longer suitable for today's [mention area of focus].
If you want to [achieve specific goal], you need to [adopt new approach].
Go and [expand on alternative/new approach]
This way, you can [unlock these desirable outcomes].
[Call to action or question for audience].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC22.3 · go · insight · punchy · C · "Why Good Design Is Important"
Needs: only a domain concept paired with a supporting image, no personal facts
```
Quick reminder that [key concept/topic] is important:
[Image that demonstrates the importance of key concept/topic]
```
### T-LC23.4 · go · insight · warm · C · There's More Than One Way To Win
Needs: only their stated general approach/philosophy contrasted with alternative methods
```
The pressure to [growing pressure or trend in your industry or field].
"[Relevant question/doubt/frustration target audience may have]."
"[Relevant question/doubt/frustration target audience may have]."
"[Relevant question/doubt/frustration target audience may have]."
[Briefly explain where you encounter people talking about these issues].
I hear this all the time.
People want [achieve X], but they're unsure about:
[Key fear/uncertainty/doubt].
[Key fear/uncertainty/doubt].
[Key fear/uncertainty/doubt].
Here's how I see it:
[Suggest your core approach or solution].
[Briefly expand on this approach and its benefits].
* [Practical tip/step/example]
* [Practical tip/step/example]
* [Practical tip/step/example]
Personally, I [give your unique perspective or opinion].
But I don't tend to [do alternative approach]. I [approach it this way].
And yet I [unlock desirable outcome] because I [sum up specific approach].
[Call to action].
[Question for audience]?
```
### T-LC24.4 · go · insight · analytical · C · How To Make More $$$ With Content
Needs: only a domain content formula/principle and general supporting examples
```
If you're [relevant audience or interest group], read this:
You're obsessing over the wrong [metric/idea/habit].
There's only one thing you should obsess over: 
[Core formula or principle].
It's because of this [formula/principle] that:
* [Example related success]
* [Example related success]
* [Example related success]
[Briefly explain why formula/principle works].
So when you [take action] [you/they can unlock benefit].
"In contrast, [contrasting habit or idea] fails because: 
[List relevant reasons and examples that support point].
The solution: 
Focus on [specific action/concept].
Remember: [Reiterate core formula/principle].
```
### T-LC24.5 · go · insight · analytical · C · How To Argue Your Case (Steal These 11 Post Elements)
Needs: only domain expertise to build a persuasive argument with generic examples
```
[Main topic or concept] may be [commonly repeated saying], but [complementary but often overlooked factor] is [related statement to repeated saying].
Imagine [relatable scenario that highlights key problem or concept]:
* [Problem/flaw that illustrates key problem]
* [Problem/flaw that illustrates key problem]
* [Problem/flaw that illustrates key problem]
It's no different for [main topic/niche/target audience].
* [Common flaw/mistake that relates to topic]
* [Common flaw/mistake that relates to topic]
* [Common flaw/mistake that relates to topic]
[Summarise key takeaway].
Here are some [considerations/tips/strategies]:
1. [Consideration/tip/strategy]
[Briefly explain why this is important and give some actionable advice].
2. [Consideration/tip/strategy]
[Briefly explain why this is important and give some actionable advice].
3. [Consideration/tip/strategy]
[Briefly explain why this is important and give some actionable advice].
Your goal is to [summarise overall goal].
Remember:
[State or list key lessons or phrases].
[Optional: Give real-world example/reference example in image].
[Image that matches the post]
```
### T-LC26.2 · go · insight · warm · C · Teasing What's Up Ahead
Needs: only domain expertise to challenge a misconception and reassure the reader
```
Important reminder for [target audience]:
[Common misconception]. 
[Alternative perspective].
[Common action] is not [negative assumption]. But if you avoid it, you'll risk [undesirable consequence(s)].
I get it - some of you might [briefly qualify who this may not apply to]. But for most of us, this is essential.
Don't be [negative emotion]. 
Don't be [another negative emotion]. 
Remember, [positive affirmation about the reader's value or skill].
[Question for audience or call to action].
```
### T-LC27.2 · go · insight · analytical · C · How To Establish A Strong Visual Brand (Even If You Know Nothing About Design)
Needs: only domain expertise plus general reasons and relatable examples
```
[An unexpected comparison of concepts/practices/professions that challenges assumptions].
[Briefly explain what you mean using a relatable example, analogy, or personal experience].
[Key implication of this in the broader context of business/your field/industry].
Here's why [core concept] matters:
* [Reason 1]: [Brief explanation that outlines key benefit]
* [Reason 2]: [Brief explanation that outlines key benefit] 
* [Reason 3]: [Brief explanation that outlines key benefit] 
* [Reason 4]: [Brief explanation that outlines key benefit] 
Take [relatable examples].
Their [core concept] [brief explanation].
[Key takeaway].
[Question for audience or call to action].
[Image that matches the post]
```
### T-LC28.4 · go · insight · warm · C · Which Fears Are You Leaving Unaddressed?
Needs: only general coaching knowledge of common fears and how to address them
Echoes: T-LC5.5, T17.4
```
1 reason [specific struggle or pain point]:
[Sum up specific cause].
I see this often:
* [Inferior approach/mistake]
* [Inferior approach/mistake]
* [Inferior approach/mistake]
None of these [highlight specific issue].
The moment you [specific actionable step], [positive result begins].
* [Example of what to do instead]
* [Example of what to do instead]
* [Example of what to do instead]
The biggest obstacle is [fear/limiting belief/roadblock].
Here's how to overcome it:
* [Actionable tip 1]
* [Actionable tip 2]
* [Actionable tip 3]
Start with [simple step]. Over time, you'll [unlock long-term benefit/insight].
[Key takeaway(s)].
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC31.1 · go · insight · analytical · C · Wanna Make (More) Money On LinkedIn? Read This
Needs: only domain knowledge of the ICP's common characteristics and challenges
```
Over the past [timeframe], I've talked to [group of people] that [share common characteristic or achievement] but struggle with [specific issue].
They genuinely want to [unlock desirable outcome].
But they face a few key challenges:
1. [First challenge]:
[Explain the challenge - e.g. break a misconception and/or highlight what people miss]. [Expand on how to overcome challenge].
2. [Second challenge]:
[Explain the challenge - e.g. break a misconception and/or highlight what people miss]. [Expand on how to overcome challenge].
3. [Third challenge]:
[Explain the challenge - e.g. break a misconception and/or highlight what people miss]. [Expand on how to overcome challenge].
Here's the reality:
[Share a counterintuitive or surprising insight].
[Explain how this insight relates to the core message or theme].
"[Prempt common excuse/objection - optional]."
[Key takeaway].
[Image that matches the post]
```
### T-LC31.2 · go · insight · bold · C · How To Twist The Knife (Making A Problem Hurt)
Needs: only domain expertise naming a problem's symptoms and a reframe with advice
Echoes: T-LC16.2
```
If you're [target audience/aspiring group], you've probably felt this:
[Common pain point].
* [Specific symptom of problem 1]
* [Specific symptom of problem 2]
* [Specific symptom of problem 3]
But here's the thing: [Reframe the problem or introduce a counterintuitive insight about the issue]. 
[Give a fresh perspective].
[Introduce a comparison or framework to explain the new perspective].
[Expand on concept - consider using relatable examples and vivid descriptions].
Here's how you can [achieve this new perspective]:
1. [A specific, actionable recommendation].
[Explain on recommendation - what do people need to know, avoid, do? Keep advice concise and actionable].
2. [A specific, actionable recommendation].
[Explain on recommendation - what do people need to know, avoid, do? Keep advice concise and actionable].
3. [A specific, actionable recommendation].
[Explain on recommendation - what do people need to know, avoid, do? Keep advice concise and actionable].
So, ask yourself: [question encouraging reflection and action].
[Key takeaway and/or call to action].
[Image that matches the post]
```
### T-LC32.2 · go · insight · warm · C · A Trick To Fire Up Your Reader's Brain
Needs: only general coaching knowledge to write reflective diagnostic questions
```
[Common frustration or challenge].
And as a [target audience], [briefly state why this issue is especially relevant].
Here's how I [approach this problem]:
[Key principle/mindset shift].
There are only X good reasons [why frustration persists/to take a certain action]:
[Reason 1]  
[Reason 2]  
[Reason 3]  
Take [specific action].
Ask yourself:
[Key question to aid reflection 1]?  
- [Brief explanation of why it matters].
[Key question to aid reflection 2]? 
- [Brief explanation of why it matters].
[Key question to aid reflection 3]? 
- [Brief explanation of why it matters].
[Briefly explain consequence(s) of not applying this advice].
[Final thought reinforcing why this matters].
[Question for audience or call to action].
```
### T10.2 · found · insight · bold · A · Reactive "scroll with intention" opinion post
Needs: a specific real piece of content or interaction the writer recently observed
```
I might get crucified for this, but oh well.
I saw [a piece of content / interaction / moment] recently and it got me thinking.
A lot of us who [shared background or identity] experienced [difficult or formative situation]. [Briefly expand].
A lot of us [second shared experience]. A lot of us [third shared experience - escalates the weight of the circumstances].
Some of us take those experiences and say because of that [negative outcome in life, career, or relationships]. We blame [external cause] for [current result].
Then there are some of us who say [same external cause] happened, but so what. We are going to [declaration of intent] anyway.
I find this genuinely fascinating. How can two people go through the exact same situation and one of them decides it is [outcome A] whilst the other decides it is [outcome B]?
[One or two sentence core belief - what separates the two camps].
[Key takeaway].
[Question for audience or call to action].
[Image that matches the post]
```
### T-LC29.3 · found · insight · analytical · B · Nothing Is "Original"
Needs: three specific real examples of how they've applied or learned from the idea
Echoes: T11.2
```
[State a bold or attention-grabbing observation].  
And [state why it doesn't affect you in the way people may expect]:  
I [share how you've applied or learned from this behavior/situation 1].  
I [share how you've applied or learned from this behavior/situation 2].  
I [share how you've applied or learned from this behavior/situation 3].  
Here's how I see it:  
* [State principle/insight 1]  
* [State principle/insight 2]  
* [State principle/insight 3]  
[Elaborate on why this behavior/situation is important, particularly for a specific group or context].  
Now, [clarify a potential misunderstanding or objection].  
[Provide a contrasting perspective or reframe the concept in a positive light].  
[Explain the consequences of misunderstanding or misusing this behavior/situation].  
The truth is, [highlight a counterintuitive or universal insight].  
[Introduce actionable suggestions]: 
* [Actionable tip 1]  
* [Actionable tip 2]  
* [Actionable tip 3]  
[Key takeaway/caveat].  
[The key benefit the reader stands to gain if they take action].
[Image that matches the post]
```

## EDUCATIONAL (43)

### T-LC3.5 · go · educational · analytical · B · Are you making this mistake?
Needs: a specific statistic on how many people make the named mistake
Echoes: T3.3
```
[High number]% of [digital asset/group] make this mistake:
Did you know by [following common practice], you are actually [eliciting negative outcome]?
Try/Think about it like this instead:
* [Step/tip/intended use]
* [Step/tip/intended use]
* [Step/tip/intended use]
(but this won't happen if [negative outcome])
The goal is [desired outcome], not [undesirable outcome].
```
### T-LC4.2 · go · educational · analytical · B · Why you should give more examples
Needs: a specific research finding or study backing the named psychological concept
Echoes: T15.4
```
[Startling fact or statistic]
But why [relevant question/problem]?
Introducing [concept or phenomenon].
Research shows:
[Summarize key findings and/or expert opinions].
The main reason for this is [explain reason in simple terms]. 
It's like when [relatable example].
So, what can we do? 
[Introduce specific solution].
[Briefly explain why it works and the expected outcome].
So next time you find yourself in [common situation], remember [concept or phenomenon] and the importance of [actions related to solution].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC17.1 · go · educational · analytical · B · How to Explain an Abstract Idea
Needs: real well-known company examples of the concept plus a stated personal differentiator
```
[Compare two products or ideas from a well-known domain that demonstrate an abstract concept].
[Briefly explain the abstract concept].
[Name the abstract concept].
The same goes for [target audience/industry].
[Statement that sums up why abstract concept relates to target audience/industry].
The reason I can [take related action] vs. [other entities that take another related action]:
[Name the abstract concept again].
[List what other entities lack].
[Explain why abstract concept is beneficial to consider/implement for target audience].
[Give an example of other well-known individuals or companies that apply the same abstract concept in their businesses].
[Call to action or question for audience].
[Relatable text image to act as a 'billboard' for your post]
```
### T12.1 · go · educational · punchy · C · Tweet-style hook opener
Needs: only a domain method/tactic explanation, no personal or client specifics
```
My favorite way to do this:
(By far)
[One-word or short-phrase answer].
But not just any [answer].
[Common version of the answer] doesn't work.
[Worst version of the answer] is worst of all.
[Answer] works when it makes people:
1. [Outcome 1]
2. [Outcome 2]
3. [Outcome 3]
Which generally means you're [doing]:
- [Tactic 1]
- [Tactic 2]
[Secondary recommendation] helps a lot too.
I definitely recommend doing it.
But [primary recommendation] into a habit too.
[Key takeaway].
[Relatable text image with stats/facts that support key reframe/recommendation].
```
### T3.3 · go · educational · punchy · C · Common Mistakes format
Needs: domain expertise, five common niche mistakes and fixes, no personal facts
```
I see the same [platform/area] [mistakes/problems] every single day:
- [Mistake 1].
[Why it fails/Good or bad example]. [Practical advice].
- [Mistake 2].
[Why it fails/Good or bad example]. [Practical advice].
- [Mistake 3].
[Why it fails/Good or bad example]. [Practical advice].
- [Mistake 4].
[Why it fails/Good or bad example]. [Practical advice].
- [Mistake 5].
[Why it fails/Good or bad example]. [Practical advice].
Your [the thing you've been critiquing] is your [what's really at stake].
[One sentence elevating why it matters more than they think].
[Direct prompt asking the reader to evaluate their current approach]. 
Be honest... [Closing question that makes them self-reflect]?
[Image that matches the post]
```
### T-LC1.1 · go · educational · punchy · C · The AIDA copywriting formula
Needs: domain expertise, generic platform actions and outcomes, no personal facts
```
It's impossible to [achieve a common goal] on/in [platform/tool/group] today.
Instead, here's what's achievable today:
- You can [specific action] to [achieve specific goal].
- You can [specific action] to [achieve specific goal].
- You can [specific action] to [achieve specific goal].
- You can [specific action] to [achieve specific goal].
It'll only take you [realistic time investment].
However, in [relatively short time frame], you'll have:
- [Desirable outcome]
- [Desirable outcome]
- [Desirable outcome]
Don't say:
"I want to [achieve common goal] on/in [platform/tool/group] today"
Instead, say:
"I want to [engage in specific daily action] today"
Pick [new strategy for success] over [common but less effective strategy].
P.S. [Foster follower engagement with a personal sign-off]
```
### T-LC2.1 · go · educational · analytical · C · The PAS copywriting formula
Needs: domain expertise, generic facts, consequence, and tips for a pain point
```
[Give an impressive, relatable fact].
[Give another fact that builds on the first].
This explains why [you/we] can [perform specific action OR reach specific goal].
But because of [these facts], [a negative consequence can occur].
[Name a negative consequence].
[Briefly explain the relevance of the consequence].
So, how do [you/we] [resolve this issue]?
[Name a solution].
[Briefly explain the relevance of the solution].
Here are [X actionable tips/questions/steps] to help get you started:
- [Tip/Question/Step 1]
- [Tip/Question/Step 2]
- [Tip/Question/Step 3]
- [Tip/Question/Step 4]
Take [timeframe] to [follow this advice] and you'll [unlock key benefit].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC2.5 · go · educational · punchy · C · Good strategy → great strategy
Needs: domain expertise, generic amateur-to-expert framework, no personal facts
```
Amateur: "I [basic activity] [on/with] [Platform/Product/Strategy]."
Intermediate:
"I [basic activity] and [additional activity]."
Advanced:
"I [basic activity], [additional activity], and [another activity]."
Expert:
"I [basic activity], [additional activity], [another activity], [further activity], and [final activity]."
The reality:
[Achieving specific goal] requires more than just [basic activity].
```
### T-LC8.1 · go · educational · analytical · C · The pain of losing > the pleasure of gaining
Needs: only domain knowledge of threats/risks facing the audience and how to mitigate them
```
[Potential threat/negative action 1]
[Related potential threat/negative action 2]
[Related potential threat/negative action 3]
But here's the thing:
[Eye-opening way to avoid/mitigate these negative outcomes]
[Actionable tip/takeaway]
```
### T-LC8.5 · go · educational · warm · C · Ever get stuck writing content? Try this…
Needs: only domain knowledge of audience's common reasons for inaction and a solution
```
X reasons [people/audience] don't [take desired action].
1. [Reason/problem 1]
2. [Reason/problem 2]
3. [Reason/problem 3]
Here's the solution:
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Step 4]
[Summarise the benefits this solution unlocks]
[Personal sign-off/call to action]
PS. [Personal insight or future content tease]
```
### T-LC9.4 · go · educational · punchy · C · "The best LinkedIn copywriting lesson you'll get today"
Needs: only a teachable lesson/concept and a few named approaches to apply it
```
The best [topic] lesson you'll see today.
[Lesson/directive/concept].
X ways to do this:
1. Approach A
2. Approach B
3. Approach C
[Takeaway to reinforce lesson's importance].
[Call to action/personal sign-off].
[Provide example of lesson in action - either include in text post or as an image]
```
### T-LC9.5 · go · educational · punchy · C · Don't _just_ edit for readability!
Needs: only a repeatable framework of steps/laws packaged as domain expertise
```
How to [achieve desirable outcome] - X [laws/tips/steps]:
(if you [struggle with specific challenge], read on)
1. Law/Tip/Step A
* Give more practical advice/context as a short list…
2. Law/Tip/Step B
* Give more practical advice/context as a short list…
3. Law/Tip/Step C
* Give more practical advice/context as a short list…
[Clarify the ultimate goal of following strategy above].
[Summarise key takeaway]. 
Do this for [timeframe] and [unlock specific benefit].
[Question to foster engagement]?
[Image that matches the post]
```
### T-LC11.5 · go · educational · punchy · C · Unsure how to structure your next LinkedIn post? Try this…
Needs: only domain expertise on common mistakes and correct steps for the activity
Echoes: T-LC2.1
```
Most [common activity/assets] I see are [negative descriptor].
[Target audience], you must keep this in mind: 
[Key insight].
The [activity/asset] is NOT for [incorrect assumption].
It's for [correct assumption].
These are the common mistakes I often see:
* [Mistake]
* [Mistake]
* [Mistake]
Here's how to [achieve goal]:
* [Actionable insight/step]
* [Actionable insight/step]
* [Actionable insight/step]
* [Actionable insight/step]
And always remember to [crucial step/action].
This way, you can [achieve desirable outcome] [easier/faster/cheaper].
```
### T-LC13.4 · go · educational · analytical · C · How to switch the reader from passive skimmer to active thinker
Needs: domain expertise to construct a hypothetical scenario illustrating the advice
```
If [target audience] want to [achieve desirable outcome], then they need to do this:
They need to [main action or principle].
How?
By [Distill main action or principle into a short concept].
For example:
[Give a hypothetical scenario that puts the prescriptive advice from above into context].
[Question to encourage reader to internalise core message]?
[Image hook or relevant quote from an authority figure]
```
### T-LC15.5 · go · educational · punchy · C · Going mega-viral (8 tips)
Needs: domain expertise to produce actionable tips and pitfalls plus a real authority quote
```
[Short statement that challenges a common belief].
[State the value or benefit of the alternative behaviour/strategy you're recommending].
[Transitional sentence that introduces actionable advice]:
- [Actionable tip/step]
↳ [Briefly expand on tip/step with some specific practical advice].
- [Actionable tip/step]
↳ [Briefly expand on tip/step with some specific practical advice].
- [Actionable tip/step]
↳ [Briefly expand on tip/step with some specific practical advice].
Here's what to avoid:
- [Common pitfall]
↳ [Briefly expand on specific action(s) to avoid].
- [Common pitfall]
↳ [Briefly expand on specific action(s) to avoid].
- [Common pitfall]
↳ [Briefly expand on specific action(s) to avoid].
[Inspiring takeaway].
[Call to action or question to foster engagement].
[Relevant quote from eminent individual to act as a 'billboard' for your post]
```
### T-LC16.2 · go · educational · bold · C · What Are the Costs of Inaction? (FOMO)
Needs: domain expertise to frame a strategy with do/don't lists and urgency
```
The ultimate [topic/field] hack: 
[Strategy/Habit/Desired attribute].
Don't:
→ [Negative action/experience negative consequence 1]
→ [Negative action/experience negative consequence 2]
→ [Negative action/experience negative consequence 3]
Instead:
→ [Positive action/unlock desirable outcome 1]
→ [Positive action/unlock desirable outcome 2]
→ [Positive action/unlock desirable outcome 3]
Every day you put off [key positive action] is another day selling yourself short.
Your future [goal/outcome] depends on it.
[Call to action and/or question for audience].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC19.5 · go · educational · playful · C · Gamify Your Educational Content
Needs: only a domain concept and an illustrative example/image to build the game
```
[Follow on from image with a relevant statement or question that piques curiosity - e.g. "You probably won't guess it."].
[Introduce and explain key concept from image].
For example, [explain how the key concept informs what's going on in the image or the choice the reader makes]. (Source: [Credit source(s) if applicable].
[Describe the key benefit(s) of applying key concept].
[Suggest how key concept can be used in other contexts - if this applies to your context].
[Revelant call to action - eg. an event invite or link to an additional content resource].
[Image of thought experiment, challenge or guessing game that relates to key concept from post].
```
### T-LC21.1 · go · educational · punchy · C · Beautify Your Lists
Needs: only domain knowledge of common ineffective versus proven tactics in the field
Echoes: T3.3, T-LC10.3
```
I've been in [field/profession] for [time period]. Here's what's NEVER worked:
* [Common ineffective tactic 1]
* [Common ineffective tactic 2]
* [Common ineffective tactic 3]
* [Common ineffective tactic 4]
Here's what always works:
* [Proven tactic 1]
* [Proven tactic 2]
* [Proven tactic 3]
* [Proven tactic 4]
What would you add?
```
### T-LC22.1 · go · educational · playful · C · Speaking The LinkedIn Lingo
Needs: only a novel domain analogy explaining the main topic
```
[Main Topic] Explained.  
Think of [main topic] as [give a novel way to think about it].
[Briefly explain the significance of this and/or the actions it necessitates].
[Key takeaway].
[Relevant question for audience].
[Call to action].
[Relevant image that demonstrates concept or acts like a billboard for your post]
```
### T-LC23.1 · go · educational · analytical · C · How To Make Common Insights Yours!
Needs: only expertise to craft an illustrative anecdote/example demonstrating a common insight
```
Sick and tired of [common frustration/problem]?
[Our/My approach] [led to specific benefit] thanks to an unexpected trick: 
[One-sentence overview of the trick or technique].
[Handle an obvious objection that arises].
Instead, focus on [core principle - like personalization, relevance, etc.].
For example: [an illustrative anecdote from well-known or hypothetical figure/company].
[Briefly explain why trick or technique works in this circumstance].
So, why not apply this to [professional context]:
[Question that aids practical thought]?
[Question that aids practical thought]?
[Question that aids practical thought]?
[Summarise one specific way to apply this trick or technique].
[Key takeaway that emphasises why trick or technique is important].
Bonus Tip: You can also apply this [trick or technique] when you [secondary application] to [unlock benefit] too!
```
### T-LC24.1 · go · educational · analytical · C · The Key To Making An Idea Uniquely Yours
Needs: only domain expertise to break down and critique a real or illustrative example
Echoes: T-LC22.3
```
[Platform/tool/topic] breakdown.
Here's the takeaway:
[Core principle/tip].
[Optional critique/suggestion/explanation].
[Image that demonstrates principle/trip]
```
### T-LC25.3 · go · educational · punchy · C · What PROMISE Are You Making The Reader?
Needs: only domain expertise to state an underrated insight and practical tips
Echoes: T-LC3.3
```
Underrated [industry/field] advice:
[Core insight framed as a call to reflection or action].
Let your [work/content/product]:
* [Practical advice/shift mindset]
* [Practical advice/shift mindset]
* [Practical advice/shift mindset]
* [Practical advice/shift mindset]
[Key takeaway/desirable outcome].
```
### T-LC26.5 · go · educational · playful · C · The 2nd Most Engaging Word In The English Language
Needs: only copywriting expertise to construct a progressive rewrite example
```
[Common approach] is ok. But [better approach] achieves [desired outcome]."
Watch how [describe example] evolves:
[Baseline example].
Let's improve it:
[Improved version].
We can do better:
[More improved version].
We can do better still:
[Ultimate version]
[List practical takeaways or state lesson].
[Question for audience or call to action].
```
### T-LC30.1 · go · educational · analytical · C · Is Your Advice Actually Actionable, Though?
Needs: only domain knowledge of a framework/book translated into practical audience-specific steps
```
I've [explored] many [ideas/resources/approaches], but this one [unlocked benefit]:
(And it's not [commonly spoken about idea/resource/approach])
→ [Introduce the unexpected idea/resource/approach].
Here's how to apply this to [specific context]:
* [Key idea/principle 1]: [Practical application tailored to the audience/context]
* [Key idea/principle 2]: [Practical application tailored to the audience/context]
* [Key idea/principle 3]: [Practical application tailored to the audience/context]
* [Key idea/principle 4]: [Practical application tailored to the audience/context]
* [Key idea/principle 5]: [Practical application tailored to the audience/context]
This [idea/resource/approach] taught me more than [conventional alternative].
Master these [ideas/principles], and you'll become [desirable state].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC31.5 · go · educational · punchy · C · A Hook Tactic For 2025 (And Beyond)
Needs: only a general listicle of habits to stop, no personal specifics needed
```
X [negative habits/practices] to eliminate in [timeframe].
([Motivational statement about the benefit of change]).
Here's how to [achieve result] in [short timeframe]:
1. Stop [habit/practice 1].
→ Signals: "[Underlying belief or message conveyed by this behavior]."
How to eliminate:
[State or list practical actions or techniques].
2. Stop [habit/practice 2].
→ Signals: "[Underlying belief or message conveyed by this behavior]."
How to eliminate:
[State or list practical actions or techniques].
3. Stop [habit/practice 3].
→ Signals: "[Underlying belief or message conveyed by this behavior]."
How to eliminate:
[State or list practical actions or techniques].
4. Stop [habit/practice 4].
→ Signals: "[Underlying belief or message conveyed by this behavior]."
How to eliminate:
[State or list practical actions or techniques].
[Key takeaway].
[Question for audience or call to action].
[Image that matches the post]
```
### T-LC32.1 · go · educational · analytical · C · A Surefire Way To Improve Your Writing
Needs: only a common mistake observed and a named framework with generic example
```
[Opening line that establishes credibility or introduces an insight].
[Concise, impactful statement reinforcing the main idea].
Works for:  
[Relevant context where insight applies 1]  
[Relevant context where insight applies 2]  
[Relevant context where insight applies 3]  
[Statement that draws from your experience in the area].  
Here's a common mistake I often see:
[Explain common mistake you've observed].
I know it's costing them [specific negative consequence(s)].  
This simple  framework can help:  
[Framework Name]  
[List steps involved].
Here's an example:
[Give a relatable example of framework being applied].
[Reinforce or reiterate core insight].  
Use this [framework] to [achieve desired outcome(s)].  
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T5.2 · found · educational · warm · A · Surface-level vs basement-level problems (The Generic Content Trap)
Needs: a specific personal turning point when their skill/results accelerated fastest
Echoes: T18.5, T7.1
```
I can't stop thinking about a [piece of content] I saw the other day.
It said:
"[Quoted insight]."
This is so true.
But even after we [take the first step], we [run into obstacle]:
- [Step 1 of relatable cycle].
- [Step 2 of relatable cycle].
- [Step 3 of relatable cycle].
[Summarise reframe - link this obstacle to quoted insight].
But realize this:
[Redefine obstacle in simple terms].
[Expand on why it's actually achievable].
The problem?
[Name the hidden obstacle that makes people give up].
So... you [expand on negative consequences].
The skill to build is being able to [action] despite being surrounded by:
- [Obstacle 1]
- [Obstacle 2]
- [Obstacle 3]
If you can build this skill, you can [achieve the desirable outcome].
So [take logical next step] now.
And realise [key thing to bear in mind].
For me, I've [pull from your own personal experience].
And my skill as a [role] accelerated the fastest when I [specific turning point].
I [brief list of relevant social proof points or results you've achieved].
But if I was just starting over, I'd [take specific path].
So I created [lead magnet name].
It has everything you need to [become/achieve something specific]:
- [Feature 1 with benefit]
- [Feature 2 with benefit]
- [Feature 3 with benefit]
And more.
Want access so you can [desirable outcome]?
Comment "[keyword]" and I'll DM it to you for free.
(And if we're not connected, send me a connection request with the word "[keyword]" and I'll send it over.)
[Relatable text image to act as a 'billboard' for your post]
```
### T11.1 · found · educational · analytical · B · The "boring truth" framework reveal
Needs: a named recurring framework and the specific impressive result it generates
```
The following advice is boring.
But it [generates impressive result for me] every [time period].
If you really want to [achieve desired outcome], focus on what I call the '[named framework].'
Work out what you need to do every single [time period] to experience [result 1] and [result 2].
Depending on the [context], every [time period] we do [example action 1], [example action 2], etc.
[Briefly explain how to apply framework].
Because here's the thing...
When you're [at specific stage], it's all about [activity]. And it's [positive emotion] because you're [experiencing positive thing].
But at some point, you [engage in beneficial action].
So, you've got to embrace a little bit of [reframed negative feeling].
All it means is that [high-level positive outcome] and you have a [named framework] that is guaranteed to [drive specific desirable outcome] as long as you want it to.
[Question for audience or call to action].
```
### T7.4 · found · educational · playful · B · An underrated hook that turns your post into a puzzle
Needs: a named proprietary framework, its illustrative examples, and a specific client result number
```
What do these [X] [objects in image] have in common?
They each are ideas built around [briefly explain concept].
I call them "[Named Concept]."
All [X] [objects in image] signal [expand on concept].
[Explain why adopting this concept is important in today's world].
[Object A]: [brief label]
[Object B]: [brief label]
[Object C]: [brief label]
[Key principle at play].
Many [group/role] [get stuck] because [they make this common mistake].
Our clients have probably got [impressive result] in the last year using this [concept].
[Key takeaway].
Try [Named Concept idea].
[Image that matches the post]
```
### T5.5 · found · educational · analytical · B · Let's be blunt about LinkedIn for a sec
Needs: a specific real result they recently achieved and the framework's actual stages
```
Last week I had a big realisation after [achieving impressive result] (without [conventional constraint/method]):
1. [First stage of framework]
[Briefly expand on what stage entails].
Check: [Key consideration].
2. [Second stage of framework]
[Briefly expand on what stage entails].
Check: [Key consideration].
3. [Third stage of framework]
[Briefly expand on what stage entails].
Check: [Key consideration].
TLDR:
[Summarise core idea behind framework].
[Pithy takeaway].
[Image that matches the post]
```
### T-LC2.2 · found · educational · punchy · B · Don't do this… instead, do this…
Needs: a specific real recent unusual event plus concrete alternative strategies
```
This week, I [experienced a remarkable/unusual event].
Here are [X] ways I wouldn't recommend to [related activity]:
1. [Common ineffective approach 1]
[Explain why it's ineffective]
2. [Common ineffective approach 2]
[Explain why it's ineffective]
3. [Common ineffective approach 3]
[Explain why it's ineffective]
This is how I'd do it instead:
1. [Effective strategy 1]. [Brief explanation].
2. [Effective strategy 2]. [Brief explanation].
3. [Effective strategy 3]. [Brief explanation].
Remember: 
[Takeaway that summarises why this advice is important]
```
### T-LC4.1 · found · educational · analytical · B · How to create "valuable" content
Needs: a specific quantifiable goal, a named strategy, and the real results it produced
```
[Specific quantifiable goal]/[short timeframe] = [Specific quantifiable goal] in [long timeframe]
That's the goal. 
To get there, you can either:  
* [Method A]
* [Method B]
Just carry out these daily tasks:
* [Daily strategic task 1]
* [Daily strategic task 2]
* [Daily strategic task 3]
Here's an example of what that looks like:
1. [Specific example of "daily strategic task 1"]
2. [Specific example of "daily strategic task 2"]
3. [Specific example of "daily strategic task 3"]
Now all you have to do is [additional action] and you [achieve desirable outcome]. 
As you progress, incorporate:  
* [Less frequent action 1]
* [Less frequent action 2]
* [Less frequent action 3]
Following this exact [Strategy Name] for [time period] has helped me [unlock benefit] and [unlock additional benefit].
It's more effective than [alternative strategy].
```
### T-LC5.5 · found · educational · analytical · B · To sell more, acknowledge and resolve objections
Needs: a specific product name plus two named people/companies actually using it
```
"I don't want [common fear or misconception]."
[Reassure reader]
Many [target audience] think [new development in technology/method] will [lead to negative outcome]. 
But don't worry.
Because [provide a new way to think about it].
- [Briefly explain relevant feature]
- [Briefly explain relevant feature]
- [Briefly explain relevant feature]
And it [unlocks benefit].
[List more relevant benefits]
[State high-level desirable outcome(s)]
Smart [professionals/role] like [Name 1] and [Name 2] are getting involved.
They're using [Product Name] to [carry out action/achieve desirable outcome].
[Relevant thought-provoking question/Call to action]
[Image that matches the post]
```
### T-LC6.3 · found · educational · warm · B · Boost your credibility and relatability with shared experiences
Needs: a specific real-life example of someone applying the proposed solution
```
Many [target audience] start [at common starting point]. 
And that makes sense. 
But [outline common growth challenge].
This happens because [reason for challenge]. 
You may find yourself [engaging in problematic actions], which [result in negative outcome].
But there's a better way: [proposed solution]. 
[Briefly define the solution].
For example, take [share a real-life example].
[Thought-provoking question for audience]?
[Related text image to act as a 'billboard' for your post]
```
### T-LC8.2 · found · educational · analytical · B · How to get people to take action!
Needs: a specific number of clients/professionals worked with plus the repeatable steps used
```
I've worked with [impressive number] of [relevant professionals/clients].
Here's how they [achieve desirable outcome]:
[Summarise key principle or rule].
1. [Actionable step]
2. [Actionable step]
3. [Actionable step]
4. [Actionable step]
This is how you [reach specific goal] without [common pre-requisite].
* If you want [benefit A], then [take action A]
* If you want [benefit B], then [take action B]
* If you want [benefit C], then [take action C]
Simple, effective, repeatable.
Apply these steps for [time period], and watch what happens.
[Personal anecdote/sign-off]
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC11.1 · found · educational · analytical · B · What to say when your reader's heard it all before…
Needs: a specific start date/endeavour and named eminent figures/companies as proof examples
Echoes: T7.4, T3.4
```
I [started endeavour] in [time period]. 
(Steal my method for [achieving desirable outcome])
It's not just about [common assumption]. 
It's about using "[unique strategy name]" to [achieve goal].
After [doing a significant amount of research/analysis], here's how [eminent figures/companies get desirable results]:
- [Mission/Aim 1]
- [Mission/Aim 2]
- [Mission/Aim 3]
[Briefly reinforce/explain points from above].
[Statement that transitions to actionable advice]:
- [Strategy/Tactic 1]
- [Strategy/Tactic 2]
- [Strategy/Tactic 3]
For example:
[Give example(s) - if appropriate]
[Additional insight/tip]
[Key takeaway]
PS. [Call to action or question for audience]
[Image that matches the post]
```
### T-LC11.2 · found · educational · analytical · B · Every post is a seed
Needs: specific real tasks/actions the person has been doing over a stated recent period
```
Your [topic/idea/owned asset] is a [valuable asset] you can [exploit/benefit from].
Over the last [short time period], I've been [doing a lot of key action].
* [Specific task relevant to key action]
* [Specific task relevant to key action]
* [Specific task relevant to key action]
It's all I do every [time of day/week].
My [topic/idea/owned asset] has been a lifesaver.
And the best thing about [doing key action] is that it:
* [Unlocks short-term benefit]
* [Unlocks short-term benefit]
* [Unlocks short-term benefit]
[Bold statement that reinforces the positive impact of doing key action].
Plus if you [take this additional key action] you can:
* [Unlock this longer-term benefit]
* [Unlock this longer-term benefit]
* [Unlock this longer-term benefit]
So remember to [summarise your perspective/reiterate key message].
PS. [Call to action or question for audience]
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC12.3 · found · educational · warm · B · How to put yourself into your reader's shoes
Needs: the writer's own specific experience and benefits derived from using the tactic
Echoes: T18.1, T5.3
```
The secret to [taking specific action] that [unlocks desirable outcome]: 
[Counterintuitive tip/strategy].
"[Common objection posed as a question]?"
[Yes or No].
Here's why:
[List reasons that clearly alleviate the objection from above].
[Briefly explain your experience using counterintuitive tip/strategy, and the benefits you (or others) have derived].
"[Guiding question that helps ascertain whether counterintuitive tip/strategy is working]?"
[Key takeaway].
[Image that matches the post]
```
### T-LC17.3 · found · educational · warm · B · Let's Talk Brackets (aka. Parentheses)
Needs: their own specific practice that replaced traditional advice which didn't work for them
```
When I [face specific challenging situation], it's often because [underlying reason]. 
Here's what helps me [resolve it]: [specific action you take].
The traditional advice of [list common, ineffective advice].
… has not worked for me.
Here's what has worked for me:
* [Action/step you take 1]
* [Action/step you take 2]
* [Action/step you take 3]
[Explain why this process works and benefits you derive].
[Respected authority] said, "[Insert quote]."
[Statement that relates quote to your topic or key takeaway].
[Call to action or question for audience].
```
### T-LC27.3 · found · educational · punchy · B · The 'Frustration - Promise - Exclusivity' Hook Framework
Needs: a named proprietary technique, a specific success metric, and the steps used
Echoes: T-LC11.1, T7.4
```
If you're [experiencing challenge/frustration], here's a [hack/tip/strategy] for you (that no one else is talking about).
It's a very specific [approach/strategy] I use every time I [describe application]. 
And it's helped me [specific success metric or outcome].
It's called '[Name of Technique or Framework]'.
Let me explain…
[Briefly describe the technique and how it works. Focus on what makes it unique or effective.]
When I [took specific action], I realised I needed to do more than just [describe an outdated or ineffective approach]. 
So I started [explain how you used the technique, step by step].
[State the critical element that made this strategy work.] [Describe specific desirable outcomes/results gained].
Why am I sharing this now?
Because [mention resource, timing, and/or why it's relevant today].
[Key takeaway(s)].
[Question for audience or call to action].
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC27.4 · found · educational · analytical · B · How To Share Steps In A Memorable Way
Needs: specific outcomes/results achieved and a named step-by-step framework
```
How to [achieve a specific goal] (even if you're [facing a challenge]).
[Briefly explain why you're qualified to give this advice - e.g. the outcomes/results you've achieved since taking these steps].
Here's the exact [method/framework] I used:
I call it '[Name of Method/Framework].'
* [Step 1 Title]
[Briefly explain what to do first and why it matters].
* [Step 2 Title]
[Describe the next action to take].
* [Step 3 Title]
Now I [sum up what you've achieved so far] - [Relevant question]?
[Explain what to do now in a way that answers the question from above].
* [Step 4 Title]
[Explain what to do for the final step].
With just [manageable time investment] you can [unlock main benefit/key desirable outcome].
So try [Name of Method/Framework] for [time period] and see what happens.
[Motivational takeaway].
[Question for audience or call to action].
[Image or video that matches the post]
```
### T-LC29.4 · found · educational · analytical · B · The Power Of The Post Scriptum
Needs: five specific examples with real actions, metrics, facts, or anecdotes attached
```
[Ask a thought-provoking question or present a common challenge].  
[Briefly explain or imply why you're qualified to answer this question].
[Highlight a relatable pain point or obstacle related to the topic].  
But the good news is [reassure the reader with a positive counterpoint, introducing your main idea].  
Here are X examples of how [specific approach, strategy, or concept can work]:  
1. [Approach/strategy/concept 1]
[Briefly explain how this example works, including specific actions, metrics, facts, and/or anecdotes].  
2. [Approach/strategy/concept 2] 
[Briefly explain how this example works, including specific actions, metrics, facts, and/or anecdotes].  
3. [Approach/strategy/concept 3] 
[Briefly explain how this example works, including specific actions, metrics, facts, and/or anecdotes].  
4. [Approach/strategy/concept 4] 
[Briefly explain how this example works, including specific actions, metrics, facts, and/or anecdotes].  
5. [Approach/strategy/concept 5] 
[Briefly explain how this example works, including specific actions, metrics, facts, and/or anecdotes].   
While [commonly used method or approach] is often one of the [easiest/fastest/most affordable or more popular] ways to [achieve desired outcome], it's not the only way.  
[Key takeaway that ties back to points discussed].
[Question for audience or call to action].
```
### T-LC32.4 · found · educational · analytical · B · A Timeless Copywriting Technique
Needs: a specific framework they discovered and the concrete transformation/result it produced
Echoes: T-LC1.3
```
Most [people/group] [make common mistake].
They think they need:
* [Common but unnecessary approach/mindset 1]  
* [Common but unnecessary approach/mindset 2]  
* [Common but unnecessary approach/mindset 3]  
I followed this path for a long time.  
Until I discovered a simple [framework/method] that changed everything.  
Here's how it works:  
Start by defining [core principle or guiding statement]:  
[List steps, give practical tips and/or examples].
The result?  
[Transformation or impact achieved by following the framework/method].  
[Key takeaway].
Give it a try.
[Image that matches the post]
```

## NEWS (7)

### T15.5 · go · news · bold · B · The news hook (steal urgency & borrow authority)
Needs: real recent news events/company names and the specific consequences to cite
```
[Fact 1: a negative event, stated plainly].
[Fact 2: a contrasting event soon after].
That's how it works in [year/context].
[The group who did the real work] get [a specific negative consequence].
[The group who caused/benefited from the situation] get [a specific positive outcome].
[Core belief, stated bluntly].
[One-line reinforcement of that belief].
Meanwhile, [a group who took a different, proactive approach earlier] aren't [doing the anxious, reactive thing right now].
They have [the advantage they've built].
[List 2-3 specific forms that advantage takes].
(And [an additional intangible asset].)
They have [a specific safety net] the day [a negative event] happens.
That's the difference [the underlying principle] makes.
The safest [career/business] move you can make in [year] is [the core recommendation].
If you're starting from 0, here's where to begin:
1. [Practical step]
[Elaboration with specific guidance].
2. [Practical step]
[Elaboration with specific guidance].
3. [Practical step]
[Elaboration with specific guidance].
[Question for audience or call to action].
[Image that matches the post]
```
### T-LC5.3 · go · news · analytical · B · "Hot off the press! Here's what you need to know…"
Needs: a real, specific news event or product launch from a named company
```
BREAKING: [Short time period ago], [High-profile person/company/collaboration] revealed [new product/service/news]
Here's what you need to know:
1. [New feature/development] 
[Brief explanation/benefits/comparisons/opinion]
2. [New feature/development] 
[Brief explanation/benefits/comparisons/opinion]
3. [New feature/development] 
[Brief explanation/benefits/comparisons/opinion]
My thoughts: [share opinions/additional insider insights]
More updates to come.
[Relevant call to action - e.g. Subscribe, follow, sign-up]
[Image that matches the post]
```
### T-LC20.1 · go · news · analytical · B · How To Craft A Prediction Post
Needs: real cited industry trends or stats from a named expert or publication
```
I'm interested to see if [industry prediction].
Here's what I'm noticing:
* [Highlight trend/share observation]
* [Highlight trend/share observation]
* [Highlight trend/share observation]
According to [industry expert/publication]:
* [Relevant trend/stat/fact/observation]
* [Relevant trend/stat/fact/observation]
* [Relevant trend/stat/fact/observation]
A big part of [pursuing relevant goal] will come from:
* [Practical advice based on prediction]
* [Practical advice based on prediction]
* [Practical advice based on prediction]
[Key takeaway and/or call to action].
```
### T-LC28.1 · go · news · analytical · B · The Treasure You Seek Isn't (Necessarily) On LinkedIn
Needs: a specific real product/tool launch with its actual steps, features, and market impact
Echoes: T-LC5.3, T18.3
```
BREAKING: [New product/service/feature] is live.
(You may no longer need [alternative solutions])
Here's how to try it out:
* [Step 1].
* [Step 2].
* [Step 3].
Here's what makes it powerful:
* [Feature/benefit 1].
* [Feature/benefit 2].
* [Feature/benefit 3].
* [Feature/benefit 4].
[Briefly share how you think this will change the overall market/field].
* [Another recent development in wider industry].
* [Another recent development in wider industry].
* [Another recent development in wider industry].
And now [product/service/company] is stepping up.
In just [short timeframe], [tool/company/solution]:
[List any other recent developments made by tool/company/solution].
[Tool/company/solution] is showing us [key insight/big idea/future prediction].
[Question for audience or call to action].
[Image or video that matches the post]
```
### T4.5 · go · news · bold · C · "If you're seeing this right now, you're ahead of 99% of people"
Needs: only domain expertise/prediction about a trend, no personal or client facts
```
We are staring at the BIGGEST opportunity since [recent reference point] and [historical reference point]. If you're seeing this right now, you're ahead of [large percentage] of [people/group].
This isn't just another [category] post.
For context:
[Name of tool/trend] is [briefly explain what it does/what's going on].
If you [take relevant action], then [bold claim about what becomes possible].
I can see a future where [vivid, specific prediction].
[Briefly explain how the reader should think about this].
[Audience segment 1]: you need to [specific action].
[Audience segment 2 - if relevant]: [specific action].
Here's how you should get started:
- [Step 1]
- [Step 2]
- [Step 3]
[Sum up opportunity/share key takeaway].
[Image that matches the post]
```
### T18.3 · found · news · bold · B · The Escalating Proof Ladder
Needs: five specific real numbers, actions, or events proving the trend/prediction
```
I couldn't possibly be any more bullish on [industry/trend] right now:
> [Example 1: include specific numbers/actions/key events]
> [Example 2: include specific numbers/actions/key events]
> [Example 3: include specific numbers/actions/key events]
> [Example 4: include specific numbers/actions/key events]
> [Example 5: include specific numbers/actions/key events]
And people are still only just waking up to how big of an opportunity this is.
```
### T-LC32.5 · found · news · analytical · B · 7 Reasons Why This Post Went Viral
Needs: specific facts about a real breaking event/product and their direct hands-on experience with it
Echoes: T-LC5.3, T-LC28.1
```
BREAKING: [Industry update/product launch/significant event].
[Briefly state what qualifies you to speak on the subject - e.g. refer to the time spent testing a new product; perhaps you attended an event, or met and obtained insights from noteworthy people].
Let's break down what it is, my take, why it matters, and what you should do next:
WHAT: [Brief explanation of the topic/tool/concept]. 
MY THOUGHTS: [Share thoughts, realisations, limitations, applications, considerations, etc.].
WHY IT MATTERS: [Tie what you've discussed to over-arching trends or challenges within the field].
WHAT TO DO: [Give steps and/or practical insights that the reader can apply].
[Question for audience or call to action].
[Image that matches the post]
```

## CURATION (13)

### T7.5 · go · curation · warm · A · A personal branding lesson that's NOT about you
Needs: a real named individual's biography with a direct quote and specific career turning points
```
She/He [made unconventional decision] at [age]. By [later age], [impressive outcome].
Meet [Full Name], [role/title].
[Name] grew up in [place]. [Brief family/background context].
[Humanising origin detail - how they first got interested in their field, the more unexpected the better].
By [early age], [early sign of hustle or talent].
[He/She] enrolled at [institution] to study [subject]. But [conventional path] didn't hold [their] attention.
At [age], [he/she] [made pivotal decision]. [Brief explanation of what that meant].
[Loved ones/stakeholders] were [emotional reaction]. [Why it mattered to them - the stakes].
But [Name] had a different plan.
[Rapid-fire career highlight progression - 2-3 lines].
That's where [he/she] met [key person].
In [year], at [age], they [founded/launched/built] [venture] - [one-line description].
[He/She] [made pivotal decision] [brief reason]. But [he/she] kept [the thing others overlooked].
That decision [changed everything / made them wealthy / proved them right].
By [year], [venture] [impressive milestone]. 
[He/She] became [record or title], unseating [recognisable reference point].
Today, [he/she] [current chapter]. [He/She]'s [raised/built/grown] [metric].
When asked about [topic], [Name] said:
"[Short, punchy direct quote]"
[One action they now take that supports quote].
What makes [Name] remarkable is [core character trait - what they kept doing when others wouldn't].
Every unconventional decision paid off.
Yet this post might be the first time you've ever heard of [him/her].
[Question for audience or call to action].
[Image that matches the post]
```
### T3.5 · go · curation · warm · B · Curation post
Needs: three named real LinkedIn creators and a summary of what each does
Echoes: T4.1
```
You don't need an [intimidating credential] to [learn/do desirable thing].
These [X] LinkedIn creators make it easy for you:
1. [Name]: [Brief summary of what they do].
2. [Name]: [Brief summary of what they do].
3. [Name]: [Brief summary of what they do].
Tag someone who deserves to be on this list. Who should be #[next number]? Comment below.
[Relatable text image to act as a 'billboard' for your post]
```
### T-LC7.3 · go · curation · analytical · B · Borrow credibility to get attention
Needs: an actual quote or lesson from a specific named authority figure
Echoes: T7.5
```
[Topic] advice from [Authoritative figure]:
[Direct quote or lesson]
This also applies to [field/industry/group/context].
[Share a problematic practice from that field/industry/group/context to illustrate the point]
* [Example 1]
* [Example 2]
* [Example 3]
* [Example 4]
[Offer an actionable takeaway]
```
### T-LC16.3 · go · curation · warm · B · Storytelling That Grips the Reader
Needs: a real named person or company and their specific unconventional practice with outcome
```
The [role/title] of [well-known person/company] used to [surprising or unconventional practice].
Highly unusual but [explain the purpose or effect of the practice].
[They] would also [describe another unique aspect of the process].
[Describe how the person/group experienced this process and what it involved].
After the [process/event], [explain an unexpected consequence or result].
[Briefly expand on the surprising nature of the consequence].
[Person/organisation] believed that [behaviour/attitude/action] was [explain the reasoning or belief behind the process].
[They] were right.
[Person/company] became known for [positive outcome related to the original, surprising action].
Takeaways:
* [Key takeaway 1]
* [Key takeaway 2]
* [Key takeaway 3]
[Call to action and/or question for audience].
```
### T-LC17.2 · go · curation · warm · B · What Can Creators Learn From 'David and Goliath'?
Needs: a real named underdog company or individual with specific milestones and how achieved
```
In [year], this [professional(s) or company type] [describe risks taken] to take on [name or list giant competitor(s)].
And today, they [hit milestone].
Introducing [give name(s) of key individuals or company].
[Briefly explain a bit about the product or process and what makes it unique].
In just [short timeframe], they've:
* [Achievement/milestone]
* [Achievement/milestone]
* [Achievement/milestone]
* [Achievement/milestone]
[Briefly explain how they did it and what they got right - e.g. reveal the gap in the market they spotted].
[State one or two key desirable outcomes they unlocked].
[Show support for their future endeavours].
Huge congrats, guys!
[Image that matches the post - e.g. photo of the people involved and/or the product]
```
### T12.4 · go · curation · warm · C · Curated book-lesson listicle
Needs: book titles/authors and quotes, no personal facts about the writer needed
```
I've read [X]+ books on [topic]. Here are [X] of the most important lessons I have learned and applied to my [life/business/scenario]:
1. "[Quote/Lesson 1]."
([Author] - [Book title])
2. "[Quote/Lesson 2]."
([Author] - [Book title])
3. "[Quote/Lesson 3]."
([Author] - [Book title])
I have [X] more. Should I do a part 2?
[Question for audience or call to action].
[Image that matches the post]
```
### T-LC13.2 · go · curation · warm · C · How to add emphasis with anaphora
Needs: a real quote from an authority figure plus generic "before you X" advice
```
[Expert or Influential Person] said, "[Relevant Quote]."
In other words: [Paraphrase the quote for clarity].
Before you [common negative response/action], [alternative positive action].
Before you [common negative response/action], [alternative positive action].
Before you [common negative response/action], [alternative positive action].
Before you [common negative response/action], [alternative positive action].
When I [feel/encounter negative emotion or situation], I [ask myself: "Question to encourage positive action?" OR conduct key positive action]
```
### T-LC13.5 · go · curation · warm · C · Nobody cares about your content? Try this…
Needs: domain knowledge of real resources and creators worth recommending in the niche
Echoes: T3.5, T-LC1.2
```
X [valuable resources] to [unlock specific desirable outcome]:
1. [Resource 1] by [Creator/Author/Authority]
[Brief description of resource, why it's recommended, and an interesting insight].
2. [Resource 2] by [Creator/Author/Authority]
[Brief description of resource, why it's recommended, and an interesting insight].
3. [Resource 3] by [Creator/Author/Authority]
[Brief description of resource, why it's recommended, and an interesting insight].
4. [Resource 4] by [Creator/Author/Authority]
[Brief description of resource, why it's recommended, and an interesting insight].
5. [Resource 5] by [Creator/Author/Authority]
[Brief description of resource, why it's recommended, and an interesting insight].
[Tease upcoming content or call to action to engage readers further].
[Image that matches the post]
```
### T12.3 · found · curation · analytical · B · Non-sponsored tool/method recommendation
Needs: a specific tool/resource name, the exact reusable prompt, and specific results gotten
```
I really think "[tool/resource]" is the most underrated [category] right now. And it's completely [free/accessible].
Here's my favorite [prompt/method] for [desired outcome]:
"[Exact reusable prompt/method]."
[Short timeframe] later, I get [specific result 1], [specific result 2], and [specific result 3].
Check it out at: [link]
Not sponsored or anything. I just really like it. Especially because I can then [next step / deeper use case].
In the photo: [Give context about image]
[Image that matches the post]
```
### T-LC1.2 · found · curation · analytical · B · How to get eyeballs on your long-form content
Needs: a named guest and their real specific tips from an actual asset
```
[Person's name] [has done a remarkable thing] with [topic/product]. Here's how they [approach specific skill]:
1. [Practical tip shared in long-form content]
2. [Practical tip shared in long-form content]
3. [Practical tip shared in long-form content]
4. [Practical tip shared in long-form content]
Here's the full [resource]: [Link]
```
### T-LC23.2 · found · curation · playful · B · Be The Guinea Pig (Your Audience Will Love You For It)
Needs: a specific tool/resource they tried and its concrete features/benefits
Echoes: T12.3
```
"If [generating specific output] were as simple as [simplified approach], we'd all be [experiencing desirable outcome].
But nowadays, [describe current expectations or requirements in the field].
It's about [key elements of a successful approach].
And to be honest?
That kind of [skill/knowledge/approach] [requires specific sacrifice].
Recently, I found myself [struggling with task or challenge].
[Negative consequence(s) of struggle].
That's when I tried [tool/resource/strategy]-and it was game-changing.
Here's how:
* [Feature or benefit 1]: [Briefly describe how it makes things easier/quicker/cheaper]
* [Feature or benefit 2]: [Briefly describe how it makes things easier/quicker/cheaper]
* [Feature or benefit 3]: [Briefly describe how it makes things easier/quicker/cheaper]
And here's the best part…
I [sum up how tool/resource/strategy helped you achieve desirable outcome].
If you're like me and want to [achieve X], I recommend giving [tool/resource/strategy] a try.
[Provide link or direct reader to link in the comments].
[Image that matches the post]
```
### T-LC23.3 · found · curation · punchy · B · A Dead-Simple Way To Recommend A Tool
Needs: a specific tool or process switched to and the old inefficient method it replaced
Echoes: T-LC23.2
```
Can't believe I used to [describe outdated, inefficient process or method].
[Briefly cover details about the previous, ineffective approach].
This led to [negative outcome].
That was until [time period] ago. Now I [approach task in a new way].
[Briefly describe the key features and benefits of new approach].
And the best part? 
[Highlight a significant, unique benefit of the new approach].
[Name of new approach/tool/resource] is my personal favorite. 
[Provide link or direct reader to link in the comments].
```
### T-LC26.4 · found · curation · analytical · B · "Don't State. Quote" (Jasmin Alić)
Needs: a named interview guest, their credentials, and the specific topics discussed
```
"[Attention-grabbing statement about a pressing topic posed as a relatable quote]."
It was a pleasure speaking with [Expert's Name] on [media/podcast]. 
[Briefly list some of their notable credentials and/or interesting facts about them].
We spoke about:
* [Key topic of interest 1]
* [Key topic of interest 2]
* [Key topic of interest 3]
* [Key topic of interest 4]
And so much more.
If you're [specific audience], you don't want to miss this episode.
[Acknowledge or thank guest/co-host/associate].
[Question for audience or call to action].
[Image or video that matches the post]
```
