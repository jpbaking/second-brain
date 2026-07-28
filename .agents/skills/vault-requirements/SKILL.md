---
name: vault-requirements
description: Elicit, capture, refine, approve, baseline, change, trace, audit, or assess coverage of technical and product requirements in the vault. Use for PRDs, specifications, user needs, acceptance criteria, non-functional requirements, security or operational constraints, UI/UX requirements, change requests, scope impact, traceability matrices, or questions about what is required and whether it is implemented and verified.
---

# Manage requirements

Load `rules/shared/35-technical-project-management.md`, the project hub, and
`memory/requirements/_template.md`.

## Choose the operation

- **Capture/refine:** turn evidence into atomic, unambiguous requirements.
- **Baseline/change:** propose or approve a versioned scope change.
- **Impact:** find designs, assets, work, releases, RAID, and tests affected.
- **Coverage:** identify missing implementation or verification traceability.

## Capture and refine

1. Search existing `REQ-*` records and sources before creating anything.
2. Split compound statements. Each requirement identifies an actor or system,
   observable behaviour or quality, conditions, rationale, and measurable
   acceptance or threshold.
3. Preserve source wording and provenance. Separate requirements from
   assumptions, design choices, work tasks, and desired dates.
4. Assign the next unused `REQ-<project>-NNN` ID. Record kind, owner,
   priority, authority, source, version, and review date.
5. For non-functional requirements, record conditions and a measurable target:
   performance, availability, capacity, resilience, RTO/RPO, security,
   privacy, compliance, observability, operability, cost, maintainability, or
   accessibility.
6. For UI/UX requirements, cover users and journeys, content, loading/empty/
   error/success/permission states, input modes, responsive behaviour,
   accessibility acceptance, research evidence, and analytics or usability
   success where relevant.

## Trace, baseline, and change

7. Link each requirement bidirectionally to project, affected assets, designs,
   implementing work, release, decisions/RAID, related requirements, and
   verification evidence. Unknown downstream links remain explicit gaps.
8. Detect duplicates, conflicts, infeasible combinations, hidden assumptions,
   missing owners, and acceptance criteria that cannot be tested.
9. Approval requires named authority and evidence. On baseline, append the
   exact ID/version to the project baseline.
10. After approval, never overwrite meaning. Create a new version/change
    entry, assess impact across linked records, obtain a decision, and mark
    replaced requirements `superseded` with links.
11. `implemented` requires delivery evidence; `verified` requires accepted
    evidence against every mandatory criterion. Partial evidence stays
    implemented or explicitly partial, never verified.

## Finish

12. Update requirement and linked-record indexes/history, the project hub,
    `memory/log.md`, and search. Run project health and vault health.
13. Return the created/changed IDs, baseline impact, coverage gaps, conflicts,
    and approvals or evidence still required.
