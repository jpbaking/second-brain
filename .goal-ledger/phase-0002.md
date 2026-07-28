# phase-0002 — Build the source-of-truth record model

- Status: done
- Depends on: phase-0001
- Goal: Add durable, indexed templates and registers for technical delivery without turning the vault into a copy of executable artefacts.
- Done when: Empty-template memory areas and project hubs support systems/infrastructure, requirements, designs including UI/UX, work items, RAID, and releases; all indexes resolve; and `python3 scripts/health.py` reports a healthy empty vault.

## Sub-tasks
1. [done] Expand the project template into a control-plane hub for charter, outcomes, scope, stakeholders, governance, roadmap, milestones, baselines, linked registers, and dated status — done when: the template covers initiation through closure and each register has an explicit link target.
2. [done] Add a technical-assets area for domains, systems, services, components, APIs, data stores, infrastructure, environments, and UI surfaces — done when: its template captures ownership, lifecycle, dependencies, interfaces, repositories/IaC, environments, reliability, security, operations, and last verification.
3. [done] Add requirements and designs areas with project-scoped stable IDs and end-to-end traceability — done when: templates cover acceptance criteria, non-functional requirements, technical/infra/data/security/UI/UX design kinds, approvals, decisions, artefact versions, and verification evidence.
4. [done] Add work-item, RAID, and release areas for delivery execution and operational handover — done when: templates cover hierarchy, owners, dependencies, mitigations, gates, rollout, observability, rollback, sign-off, and post-release outcome.
5. [done] Add each area index and update root navigation, structure rules, and reindex behaviour — done when: all new areas are counted correctly and the empty template passes the existing navigation and link checks.

## Log
- 2026-07-28: phase drafted with cross-project registries so long-lived systems and infrastructure can outlive individual projects.
- 2026-07-28: phase began; sub-task 1 is expanding the project control-plane template.
- 2026-07-28: sub-task 1 completed with a lifecycle-spanning project control-plane template.
- 2026-07-28: sub-tasks 2–4 completed with technical-asset, requirement, design, work-item, RAID, and release templates carrying common metadata and traceability.
- 2026-07-28: sub-task 5 completed with six area indexes, accurate root counts, and nested technical-record handling in `vault-reindex`.
- 2026-07-28: phase check passed; the empty template is healthy and the diff has no whitespace errors.
