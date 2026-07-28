---
name: vault-project-update
description: Capture and reconcile technical project delivery updates across the project hub, milestones, systems, infrastructure, requirements, designs, work items, RAID, releases, decisions, reminders, and commitments. Use when the principal reports progress, blockers, scope or date changes, completed work, technical discoveries, design changes, delivery status, tracker updates, or asks to bring a project's source of truth up to date.
---

# Update a technical project

Treat an update as a source-of-truth transaction. Load
`rules/shared/35-technical-project-management.md` and the named project hub.

## Reconcile the evidence

1. Search the vault and identify the exact `PRJ-*` and affected record IDs. If
   the update arrived as a file, process its immutable original with
   `vault-inbox` first.
2. Classify each claim: project status, milestone, asset, requirement, design,
   work item, RAID, release, decision, reminder, or commitment.
3. Check the named authority and its last verification. Preserve the source's
   actual state: discussed is not approved; implemented is not verified;
   deployed is not healthy; closed is not outcome achieved.
4. If an external tracker, repository, IaC source, design tool, or runtime
   view conflicts with the vault, retain both dated claims and open an
   authority-conflict gap. Do not silently resolve it.

## Apply the update and traceability

5. Update current frontmatter and append a dated history entry on each
   authoritative vault record. Preserve prior dates, baselines, status, and
   rejected or superseded content.
6. Update both sides of every affected link so the traceability graph remains
   complete. Typical fan-out:
   - scope or acceptance → requirements, designs, work, baseline impact;
   - system/interface/infra/UI change → assets, designs, requirements, release;
   - progress or blocker → work, milestone, RAID, commitments;
   - risk realised → RAID kind/status plus impacted records and project RAG;
   - deployment → release timeline and asset verification, never automatic
     release verification.
7. A baseline change requires an impact statement across outcome, scope,
   schedule, technical assets, UI/UX, security, operations, cost, and risk,
   followed by an approving decision. Leave it proposed until approved.
8. Recompute delivery health from evidence. Record movement since the previous
   update, not a rewritten snapshot. Mark unknown or stale dimensions
   explicitly.

## Verify and report

9. Run project-health validation. Resolve mechanical gaps; report authority,
   approval, ownership, and evidence gaps that need a human.
10. Update indexes, `memory/log.md`, and search. Run `scripts/health.py`.
11. Reply with:
    - IDs changed and their old → new states;
    - milestone or baseline movement;
    - new/resolved RAID and blockers;
    - evidence supporting done or verified;
    - decisions, escalations, and next gates.
