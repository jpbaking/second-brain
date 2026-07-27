---
name: vault-decision
description: Record a significant technical, organisational, or professional decision in the vault as an ADR-style page, including the rejected options and why. Use when the principal says they decided something, is weighing a decision, asks to write up or document a decision, or asks what was decided about a topic and whether it has been superseded.
---

# Record a decision

The principal made, is making, or is weighing a significant decision —
technical, organisational, or professional. Get it on the record.

## Steps

1. Create `memory/decisions/YYYY-MM-DD_decision-slug.md` from
   `memory/decisions/_template.md`. The date is the decision date; status is
   `proposed` if it is still open.
2. Capture the context, the options **including the rejected ones and why**
   (that is the part future-them needs), the decision, and the consequences.
   If the principal is still weighing it, fill Context and Options, stop at
   status `proposed`, and offer a structured pros-and-cons pass.
3. Fan out: follow-up actions go to `memory/notes/commitments.md` or
   `memory/notes/reminders.md` with owners and dates; link the decision from
   the related project, people, and meeting pages; set a `revisit by` date if
   the decision has an expiry condition.
4. If this supersedes an earlier decision page, mark that one
   `superseded by` with a link — never rewrite its history.
5. Update `memory/decisions/index.md` and the count in `memory/index.md`,
   then log it.
6. Confirm in chat with the decision in one sentence and the follow-ups.

A decision mentioned only in passing still deserves at least a stub with its
status and date.
