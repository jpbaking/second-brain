# Workflow: weekly (weekly review & sweep)

End-of-week (or start-of-week) housekeeping — deeper than `/brief.md`,
more judgmental than `/checkup.md`. Keeps the vault trustworthy.

Steps:

1. **Sweep the week** — read `memory/log.md` entries for the week; note
   anything captured but never followed up.
2. **Reminders & commitments** — move completed items to Done; re-date or
   escalate overdue ones (ask, don't guess); surface "waiting on" items
   that have aged past a week for a nudge list.
3. **People pulse** — reports with no interaction-log entry in 2+ weeks;
   attrition-risk entries that haven't been re-read in a month; goal
   checkpoints landing next week.
4. **Projects** — RAG changes this week, milestones landing next week,
   risks without owners, status logs stale 30+ days ("status unknown").
5. **Decisions** — decision pages whose `revisit by` date is near or past.
6. **Hygiene** — run `python3 scripts/health.py`; resolve mechanical
   issues; list `⚠` markers still unresolved and ask about the oldest.
7. **Look ahead** — next week's dated items across all areas.
8. Deliver as a chat brief: `Done this week / Slipped / Nudge list /
   Next week / Questions for you`. Offer to save as a written weekly
   report (template-evolvable). Append a `checkup` log entry.
