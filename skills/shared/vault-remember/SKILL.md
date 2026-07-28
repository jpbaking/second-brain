---
name: vault-remember
description: Capture something the principal just said in chat into the vault's memory/ layer — a person fact, reminder, commitment, project or technical-asset update, requirement, design fact, work progress, RAID change, release evidence, or decision — dated, indexed, traced, and logged. Use when the principal shares substantive information, says to remember or note something, or mentions a fact worth keeping even in passing.
---

# Capture a fact from chat

The principal has just told you something worth keeping, or invoked this with
new information in the same message. File it.

## Steps

1. Identify the discrete facts in what was said. One message may carry
   several — a person fact plus a reminder plus a project update.
2. For each fact, find its home via the indexes: an existing person dossier,
   project page, meeting file, `memory/notes/reminders.md`, and so on. Create
   pages from `_template.md` files only when no home exists.
3. Write dated entries, converting relative dates to absolute. For facts
   about people, follow the special-care rules in
   `rules/shared/20-capture.md`.
   For technical delivery facts, load
   `rules/shared/35-technical-project-management.md`; preserve the distinction
   between discussed/approved, implemented/verified, and deployed/healthy.
   Update the authoritative record, project hub, and reciprocal links. If the
   project or authority is ambiguous, mark the gap instead of assigning one.
4. Update the indexes and append a `chat-capture` entry to `memory/log.md`.
5. Confirm in one or two lines: what was filed and where. If something was
   ambiguous (which "Alex"? which project?), file your best guess, mark it
   `⚠ unconfirmed`, and ask.

Reminders ("remind me to…", "I need to … by Friday") go to
`memory/notes/reminders.md`. Promises **between people** go to
`memory/notes/commitments.md` instead, split into *I owe* and *Waiting on*.
Significant decisions deserve at least a stub page — use the `vault-decision`
skill.
