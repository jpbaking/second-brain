# Master index — root

DOX-style root: navigation only, one line per **area**, never per page.
Per-page lines live in each area's own `index.md`. Counts are verified by
`scripts/health.py`; refresh them (and this file) via `/reindex.md`.

Area line format:
`- [Area](area/index.md) — N page(s): what lives there`

## Areas

- [People](people/index.md) — 0 page(s): one dossier per person (incl. the principal's own brag doc)
- [Meetings](meetings/index.md) — 0 page(s): minutes, filed by year
- [Projects](projects/index.md) — 0 page(s): ongoing initiatives
- [Decisions](decisions/index.md) — 0 page(s): significant decisions, ADR-style
- [Notes](notes/index.md) — 2 page(s): mental notes, reminders, commitments
- [Ideas](ideas/index.md) — 0 page(s): brainstorms
- [Topics](topics/index.md) — 0 page(s): everything without a better home
