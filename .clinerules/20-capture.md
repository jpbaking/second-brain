# Capture: how information enters the vault

Two channels: files in `inbox/`, and things the principal says in chat.
Both end the same way — filed, indexed, logged.

## Processing an inbox item

For each file in `inbox/` (oldest first):

1. **Read it** (or as much as needed to understand what it is).
2. **Move it** to its year shard: `library/YYYY/YYYY-MM-DD_slug.ext`
   (shard year = filename year; create the folder and its `catalog.md` on
   first use). Move, don't copy — the inbox must end empty. NEVER alter
   the content, even to fix typos or formatting.
3. **Catalog it** — add a line to the shard's `library/YYYY/catalog.md`:
   `- [YYYY-MM-DD_slug.ext](YYYY-MM-DD_slug.ext) — what it is, received YYYY-MM-DD → notes: [page](../../memory/...)`
   Then update that year's count line in the root `library/catalog.md`
   (add the shard line if the year is new).
4. **Extract meaning** into `memory/`: update existing pages (a person's
   dossier, a project page) and/or create new ones. Summaries, dated facts,
   and links back to the library original.
5. **Index + log** per the structure rules.
6. **Tell the principal** what you filed and where, in 1–3 lines per item,
   and flag anything that surprised you (contradiction with existing memory,
   ambiguous ownership, unclear dates).

If a file is unintelligible (corrupt, unknown format), move it to its year
shard anyway (received date), catalog it as `unprocessed — needs principal
input`, and ask.

## Chat capture

When the principal shares substantive information in conversation —
about a person, meeting, decision, idea, deadline, anything worth
remembering — file it into `memory/` as part of handling their message,
even if they didn't explicitly say "remember this". Chat capture has no
library original; the log entry is the provenance (`chat-capture`).

Things that sound like reminders ("remind me to…", "I need to … by Friday")
go to `memory/notes/reminders.md` as:
`- [ ] YYYY-MM-DD due: task (captured YYYY-MM-DD)`

Promises **between people** go to `memory/notes/commitments.md` instead —
"I told Sam I'd review her doc" → *I owe*; "Bob will send the numbers by
Tue" → *Waiting on*. Same checkbox format, plus who and the source page.

Significant decisions (technical, organisational, professional) get a page
in `memory/decisions/` — see the `/decision.md` workflow. A decision
mentioned in passing still deserves at least a stub with status and date.

Project talk maps to the project page's sections: progress → **Status
log** (dated), new/changed risk → **Risks & issues** (with owner), date
movement → **Milestones** (append the new date, mark the old one
`⚠ slipped` + reason — never rewrite), "we're blocked on team X" →
**Dependencies** plus a *waiting-on* commitment. A slipped date or new
red risk mentioned in passing is still a capture, not just conversation.

## People facts — special care

Facts about people go in that person's dossier (`memory/people/`), created
from `_template.md` on first mention. Rules:

- Dated entries, principal's-eye view, neutral wording. Record what was
  said, not your editorializing: `- 2026-07-08: Principal noted X seemed
  disengaged in standups this week.`
- Attrition-risk and performance-concern entries additionally get the
  principal's stated reasoning, because evals will depend on it later.
- Accomplishments go in the accomplishments log **with date and scale**
  (small/medium/large as the principal frames it) — these are the raw
  material for performance evaluations.
- **The principal's own wins count too.** Anything they ship, present,
  file (patents), or get recognised for goes in the principal's OWN
  dossier in `people/` — it feeds `/cv-update.md`, promo cases, and
  self-reviews. They won't mention it twice; catch it the first time.

## Update, don't duplicate

Before creating a page, check the area's `index.md` (via the root
`memory/index.md`) for an existing one. New pages change the area's count
in the root index.
New information about an existing subject appends to its page. If new info
contradicts recorded info, keep both entries dated and add a
`⚠ superseded:` marker on the old line — never silently delete history.
