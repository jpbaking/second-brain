---
name: vault-weekly
description: Run the vault's weekly review and sweep — what was captured but never followed up, reminders and commitments to re-date or escalate, people and project pulse, decisions due for revisit, hygiene, and the week ahead. Use when the principal asks for a weekly review, end-of-week or start-of-week sweep, or a look back at the week and ahead to the next.
---

# Weekly review and sweep

End-of-week or start-of-week housekeeping — deeper than the `vault-brief`
skill, more judgmental than the `vault-checkup` skill. This is what keeps the
vault trustworthy.

## Steps

1. **Sweep the week.** Read `memory/log.md` entries for the week and note
   anything captured but never followed up.
2. **Reminders and commitments.** Move completed items to Done; re-date or
   escalate overdue ones — ask, do not guess. Surface *waiting on* items that
   have aged past a week as a nudge list.
3. **People pulse.** Reports with no interaction-log entry in 2 or more
   weeks; attrition-risk entries not re-read in a month; goal checkpoints
   landing next week.
4. **Projects.** RAG changes this week, milestones landing next week, risks
   without owners, and status logs stale 30 days or more ("status unknown").
5. **Decisions.** Decision pages whose `revisit by` date is near or past.
6. **Hygiene.** Run `python3 scripts/health.py`, resolve the mechanical
   issues, then list the `⚠` markers still unresolved and ask about the
   oldest.
7. **Look ahead.** Next week's dated items across all areas.
8. Deliver as a chat brief under `Done this week / Slipped / Nudge list /
   Next week / Questions for you`. Offer to save it as a written weekly
   report, which is template-evolvable. Append a `checkup` entry to
   `memory/log.md`.
