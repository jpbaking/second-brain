---
name: vault-release
description: Plan, assess, approve, record, or review a software release, migration, infrastructure change, experiment, cutover, rollback, or post-release verification. Use for release plans, readiness reviews, go/no-go decisions, change windows, deployment coordination, rollback planning, operational handover, launch checks, release status, post-implementation review, or questions about whether a technical change is ready and proven.
---

# Govern a release or technical change

Load `rules/shared/35-technical-project-management.md`,
`memory/releases/_template.md`, the project baseline, included work,
requirements, designs, assets, and open RAID.

This procedure manages the source-of-truth record and readiness assessment. It
does not deploy, change infrastructure, send communications, or approve
production actions unless the principal separately requests and authorises
those actions.

## Plan

1. Search for an existing `REL-*` record. Define outcome, kind, scope,
   exclusions, environments, window, owner, change authority, affected assets,
   user impact, and point of no return.
2. Assign a stable release ID. Link included `WORK-*`, `REQ-*`, `DES-*`,
   `AST-*`, decisions, and RAID in both directions.
3. Record versioned deployment/migration automation, sequencing and owners,
   compatibility, data handling, flags/exposure, communications, support,
   observability, and rollback triggers/procedure.
4. Define measurable immediate, observation-window, business, technical,
   security, operational, UI/UX, and accessibility verification.

## Assess readiness and decide

5. Evaluate every applicable readiness gate from evidence. Unknown, stale,
   partial, or verbal-only evidence does not pass a gate.
6. Surface incomplete work, unverified requirements, unapproved designs,
   unowned steps, open critical RAID, missing rollback/observability/support,
   unresolved authority conflicts, and environment drift.
7. Recommend `go`, `conditional go`, or `no-go` with reasons and accepted
   residual risk. Only the named authority sets `approved`; record actor,
   decision, time, conditions, and evidence.

## Record execution and outcome

8. Append the actual timeline; never replace the plan. Record deviations,
   observations, incidents, rollback decisions, communications, and owners.
9. `deployed` means the change reached the target. Move to `verified` only
   after all mandatory checks and the observation window pass. A rollback or
   partial result preserves what happened and opens residual work/RAID.
10. Update asset versions and verification dates from authoritative evidence.
    Do not infer runtime health from deployment success.
11. Complete the post-release review: outcome versus target, incidents,
    feedback, metrics, lessons, residual obligations, operational acceptance,
    and closure authority.

## Finish

12. Update indexes, project hub, linked records, `memory/log.md`, and search.
    Run project health and vault health.
13. Return readiness, blockers, decision owner, timeline state, verification
    evidence, residual RAID, and next gate.
