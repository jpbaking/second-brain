---
name: vault-project-status
description: Report evidence-backed technical project or portfolio status from the vault — outcomes, baseline movement, milestones, requirements, systems/infrastructure, design and UI/UX, delivery, RAID, dependencies, release readiness, decisions, and asks. Use when the principal asks where a project stands, for a status update, portfolio or programme view, steering review, delivery health, readiness, risks, blockers, movement, or what needs attention.
---

# Report technical project status

This is read-only unless the principal also asks to record or reconcile the
status. Load `rules/shared/35-technical-project-management.md`.

## Single project

1. Search for the `PRJ-*` hub, then traverse linked requirements, assets,
   designs, work, RAID, releases, decisions, meetings, commitments, and
   evidence. Check authority and verification dates.
2. Compare current evidence with the previous status and approved baseline:
   outcomes/KPIs, scope, milestone/date movement, and added/removed IDs.
3. Assess each dimension separately:
   - scope and requirement coverage;
   - architecture/design and UI/UX approval/verification;
   - build, integration, and delivery flow;
   - systems, infrastructure, data, security, operations, and ownership;
   - open RAID, dependencies, critical path, and ageing blockers;
   - release readiness, rollout/rollback, and observed outcomes.
4. Derive overall RAG from the worst material evidence, not an average or the
   old colour. Stale or conflicting authority becomes `unknown` or a named
   caveat.
5. Deliver: overall RAG and reason; movement; milestone forecast; top RAID and
   owners; traceability/authority gaps; next gate; and decisions, escalations,
   or nudges required.

## Portfolio

6. One row per active/on-hold/closing project: RAG, phase, next gate/date,
   baseline movement, top RAID, release state, evidence age, and ask. Order
   red, amber, unknown, then green.
7. Include cross-project asset, interface, environment, team, vendor, and
   release dependencies. Flag conflicting dates or ownership across hubs.
8. A project with no verified delivery evidence in 30 days is `status
   unknown — evidence stale`, regardless of its stored colour.

## Persist only when asked

9. If the principal asks to record/reconcile the result, use
   `vault-project-update`: update authoritative records, append dated status,
   preserve baseline history, run project health, and log it. A report alone
   does not mutate the vault.
10. Chat by default. For a document or deck, use
    `reports/templates/technical-project-status.md` and the report rules.
