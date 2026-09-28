# Fact-check protocol

A factual error under a client's name outranks every style fix. The target audience for the team's clients (CTOs, founders, VCs) includes people who know the real number. One wrong figure turns a peer-connect post into a peer-correction post, and that lands on the client, not on the team.

## Triggers

Verify before editing anything else if the draft contains:

- A number (valuation, users, revenue, growth multiple, token count, headcount, years).
- A named company, product, or deal.
- A named person and something attributed to them.
- A dated event or "recently" / "this week" / "just announced".
- A claim about a market ("fastest-growing", "largest", "first").
- A claim about the author's own history (years in a place, founding date) that the voice skill can check.

## How

1. One web search on the core entity and event. Add a second only if the first leaves the number unresolved.
2. Prefer the primary source (company newsroom, the founder's own post, a filing) over aggregators. Investor blog posts from the deal's own backers count as primary for deal-specific numbers.
3. Record: the figure, the unit, the period, the date of the source, and whether it is reported or confirmed.
4. If sources disagree, say so in the fix and recommend the most defensible figure (usually the company's own stated one, or a range).

## The traps

**Unit and period**
- "Token usage will cross 100T" means nothing without per-what. Per day, per week, per year, cumulative? Check the chart's axis before accepting the draft's reading of it.
- In the Stripe / OpenRouter example, the draft said "100T tokens" as a future milestone; the investor's own note put the platform at a 4.5+ quadrillion token annual run rate. The draft was 45x behind reality on the annual unit. The fix was not "wrong number" but "state the unit and period the chart actually shows."

**Stale figures**
- A number the author quoted in a podcast six months ago may have moved. Check the voice skill's number bank for the date of each figure. If the draft's number is newer than the bank's, verify the new one; if older, flag that the bank has a fresher figure.

**Reported vs. confirmed**
- "$7B" (Bloomberg, reported) vs. "terms not disclosed" (Stripe, confirmed) vs. "$7.5B" (NYT) vs. "$8B+" (Axios). The safe phrasing is "$7B+" or "reportedly $7B+". A draft that states a precise figure as fact should be softened unless the company confirmed it.

**Analyst opinion attributed to the author**
- If the draft's take ("this is really about the meter, not the model") matches a widely circulated analyst or VC framing, check whether the author has said it. If not, either attribute ("as Menlo's note put it") or remove. For Vivek this is a hard rule: his audience includes the people who wrote those notes.

**The author's own biography**
- "15 years in Silicon Valley" vs. the voice profile's "14 years, first years in Chennai/Bangalore." Small, but the author will notice, and it signals the ghostwriter was not paying attention.

## How it appears in the output

- The Call line in the scorecard names the factual fix first: "Revise. Fix the token number before anything else."
- Voice match is capped at 2/5 when a factual error is present, because the damage lands on the author.
- The fix block for the line quotes the verified figure with its source and date, in one clause, so the writer can check it themselves.
- Do not write a paragraph about the search. One clause on what was found, one clause on the unit, then the fix.
