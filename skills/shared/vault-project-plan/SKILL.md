---
name: vault-project-plan
description: Create, initialise, charter, plan, baseline, or rebaseline a technical project or programme in the vault. Use when the principal starts an initiative, asks for a project plan, charter, roadmap, delivery plan, work breakdown, governance model, milestone plan, technical programme setup, or wants scope and requirements turned into an approved source-of-truth baseline.
---

# Plan a technical project

Build a traceable control plane, not a speculative plan. Load
`rules/shared/35-technical-project-management.md`,
`memory/projects/_template.md`, and the templates for any registers the
project actually needs.

## Establish the project

1. Search the vault for an existing project, aliases, predecessor work, active
   systems, decisions, commitments, and source material. Update an existing
   hub instead of creating a duplicate.
2. Establish the minimum charter: problem, intended users or customers,
   measurable outcomes, explicit in/out scope, constraints, sponsor, project
   lead, decision rights, target date, and definition of done. Mark missing
   facts `unknown`; ask only for choices that materially change the plan.
3. Create `memory/projects/prj-<stable-slug>.md` from the template with a
   permanent `PRJ-<stable-slug>` ID. Keep `status: proposed` until an
   authorised person approves the charter.
   When upgrading a legacy project page with no technical frontmatter,
   preserve its dated history, assign the stable ID, move its existing
   content into the new hub sections, update inbound links/indexes, and fan
   distinct records into the technical registers. Never create a duplicate
   hub or discard the earlier RAID-lite history.
4. Identify affected `AST-*` technical assets. Create asset stubs only when
   their identity and owner or authority are known; otherwise open a discovery
   work item or RAID gap.

## Build the delivery baseline

5. Decompose the outcome into milestones and `WORK-*` outcomes, workstreams,
   or epics. Each has an owner, observable done and verification gates,
   dependencies, and a milestone or release destination.
6. Capture known `REQ-*` requirements with sources and acceptance criteria.
   Separate business, user, functional, non-functional, technical, security,
   operational, UI, and UX requirements. Use the `vault-requirements` skill
   for substantial elicitation or change control.
7. Create or link `DES-*` design work for architecture, infrastructure, data,
   security, UI, or UX decisions that are not yet approved. Do not turn an
   assumption into an approved design.
8. Create `RAID-*` entries for uncertain assumptions, delivery risks, active
   issues, and dependencies. Every open entry has an owner, next action, and
   review or due date.
9. Define release or migration increments, readiness gates, operational
   ownership, and feedback loops. Create `REL-*` records only when a release
   boundary is meaningful.

## Review and approve

10. Check traceability in both directions: project ↔ assets, requirements,
    designs, work, RAID, releases, decisions, and evidence. Surface unowned
    records, missing acceptance, circular dependencies, infeasible dates, and
    authority conflicts.
11. Present the proposed baseline: outcomes, scope, milestones, critical path,
    top RAID, affected systems/infra/UI, release strategy, decisions needed,
    and explicit unknowns.
12. Obtain approval before setting the project `active` or requirements and
    designs `approved`. Append a baseline entry with the exact IDs/versions,
    approving evidence, and date. Rebaselining preserves the old baseline and
    links an impact assessment and decision.
13. Update all area indexes, root counts, project links, and
    `memory/log.md`; reindex search and run project health plus
    `python3 scripts/health.py`.

## Return

Lead with the project ID, proposed or approved outcome, next gate, top three
risks, and the decisions or missing authorities that require the principal.
