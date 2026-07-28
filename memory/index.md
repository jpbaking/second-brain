# Master index — root

DOX-style root: navigation only, one line per **area**, never per page.
Per-page lines live in each area's own `index.md`. Counts are verified by
`scripts/health.py`; refresh them (and this file) with the `vault-reindex` skill.

Area line format:
`- [Area](area/index.md) — N page(s): what lives there`

## Areas

- [People](people/index.md) — 0 page(s): one dossier per person (incl. the principal's own brag doc)
- [Meetings](meetings/index.md) — 0 page(s): minutes, filed by year
- [Projects](projects/index.md) — 0 page(s): ongoing initiatives
- [Technical assets](technical-assets/index.md) — 0 page(s): systems, services, APIs, data, infrastructure, environments, UI surfaces
- [Requirements](requirements/index.md) — 0 page(s): project-scoped needs and acceptance criteria
- [Designs](designs/index.md) — 0 page(s): technical, infrastructure, security, UI and UX designs
- [Work items](work-items/index.md) — 0 page(s): outcomes, workstreams, epics, features and tasks
- [RAID](raid/index.md) — 0 page(s): risks, assumptions, issues and dependencies
- [Releases](releases/index.md) — 0 page(s): release, migration and infrastructure-change records
- [Decisions](decisions/index.md) — 0 page(s): significant decisions, ADR-style
- [Notes](notes/index.md) — 2 page(s): mental notes, reminders, commitments
- [Ideas](ideas/index.md) — 0 page(s): brainstorms
- [Topics](topics/index.md) — 0 page(s): everything without a better home
