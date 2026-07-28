---
name: vault-project-close
description: Close, cancel, or hand over a technical project or programme with evidence and preserved history. Use when the principal says a project is finished, shipped, cancelled, transitioning to operations, needs a closure review, lessons learned, benefits review, final status, archive, ownership transfer, or wants to verify that requirements, releases, systems, infrastructure, UI/UX, risks, and follow-ups are complete.
---

# Close a technical project

Load `rules/shared/35-technical-project-management.md`, the full project hub,
all linked registers, decisions, commitments, and release evidence. Start with
`status: closing`; closing is an audit, not a wording change.

## Audit closure

1. Compare actual outcomes and KPIs with the charter and current approved
   baseline. Record met, missed, superseded, waived, and not-yet-measurable
   outcomes separately.
2. Check every approved requirement. It must be verified, explicitly
   superseded/rejected, or accepted as residual scope with an owner and
   decision.
3. Check designs, work items, releases, migrations, data, security,
   infrastructure, and UI/UX acceptance. Done or deployed without evidence is
   not verified.
4. Verify each affected technical asset has current ownership, authority
   links/revisions, environment state, dependencies/interfaces, operational
   documentation, observability, support, and review date.
5. Reconcile open RAID, reminders, commitments, incidents, debt, exceptions,
   licences/contracts, and follow-up benefits measurement. Resolve, transfer,
   accept, or retain each with owner and date; never drop it at closure.

## Handover and decide

6. Record operational and product acceptance, support/escalation, runbooks,
   dashboards, access/control ownership, capacity/cost responsibility, known
   failure modes, and the first post-handover review.
7. Capture lessons with evidence: what changed the outcome, what to repeat,
   what to avoid, and concrete improvements with owners. Do not convert
   personal blame into a project fact.
8. Present the closure pack: outcomes, baseline variance, requirement and
   release evidence, asset handover, residual RAID/work, benefits review,
   lessons, and explicit closure gaps.
9. Only the named authority moves the project to `closed` or `cancelled`.
   Record the decision/date and reason. If mandatory evidence or ownership is
   missing, keep `closing` and name the gate.

## Preserve and finish

10. Keep all project and linked records indexed and searchable. Do not delete
    or move them merely because the project closed; long-lived technical
    assets remain active under their operational owners.
11. Update project/record histories, indexes, `memory/log.md`, and search. Run
    project health and vault health.
12. Return the closure state, outcome evidence, accepted variance, operational
    owner, residual obligations, review dates, and missing approval if any.
