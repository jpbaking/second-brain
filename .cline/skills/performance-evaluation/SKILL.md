---
name: performance-evaluation
description: Draft or guide a performance evaluation for a team member using their dossier, accomplishment log, goals, and meeting history in the vault. Trigger when the principal asks for a performance review, eval, appraisal, promo case, self-review input, or goal-setting/check-in prep for a person on their team.
---

# Performance evaluation

Produce an evidence-based evaluation draft the principal can stand behind.
Every claim must trace to dated vault entries — an eval built on vibes is
worse than no eval.

## Steps

1. **Scope**: confirm the person, the review period, and the artifact
   wanted (full written eval, talking points, promo case, goal check-in).
   If the principal's org has a rating scale or form recorded in the vault
   or `templates/`, use it; otherwise ask once and record the answer in
   `memory/topics/` for next time.
2. **Gather** (retrieval rules apply):
   - `memory/people/<person>.md` — full dossier: role, goals, dated
     accomplishments, concerns, growth notes, attrition signals.
   - `memory/meetings/` — entries mentioning the person in the period.
   - `memory/projects/` — their contributions on project pages.
   - Previous evals in `reports/` for trajectory and consistency.
3. **Assess against their recorded goals**, not generic criteria: for each
   goal, cite the dated evidence for/against. Then strengths (with the 2–3
   strongest dated examples), growth areas (recorded concerns, framed
   constructively), and trajectory vs last eval.
4. **Flag evidence gaps loudly**: "No entries on goal #2 since March —
   either it's been quiet or we haven't been capturing it." Never pad a
   thin record with invented specifics.
5. **Draft** using `reports/templates/performance-evaluation.md` (or the
   principal's evolved template if one exists in `reports/templates/`).
   Output to `reports/YYYY/YYYY-MM-DD_perf-eval-<person>.md`. Log it.
6. **Handle with discretion**: this document is about one person; don't
   pull in comparative details about teammates unless explicitly asked
   for calibration, and say so if asked to compare.
7. Formatting feedback → evolve the template per `.clinerules/40-reports.md`.

## Template

Starter skeleton: [templates/performance-evaluation.md](templates/performance-evaluation.md).
Once the principal gives feedback, the evolved copy in `reports/templates/`
supersedes it.
