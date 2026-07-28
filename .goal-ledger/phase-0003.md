# phase-0003 — Create technical project-management skills

- Status: done
- Depends on: phase-0002
- Goal: Give agents concise, reusable procedures for planning and maintaining the technical source of truth across the full project lifecycle.
- Done when: New canonical skills for project planning, project updates, requirements, system mapping, design, release, and closure pass skill validation and correctly fan changes across all linked registers.

## Sub-tasks
1. [done] Initialise new canonical skill folders with the skill-creator tooling and portable metadata — done when: every planned skill has a valid generated skeleton under `skills/shared/` with no placeholder content.
2. [done] Implement `vault-project-plan` and `vault-project-update` for chartering, baselining, delivery capture, milestone movement, RAID, dependencies, and register fan-out — done when: both skills specify complete workflows, stop conditions, provenance, and observable completion checks.
3. [done] Implement `vault-requirements`, `vault-system-map`, and `vault-design` for requirement/change control, system/infra mapping, and technical or UI/UX design governance — done when: each skill enforces IDs, authority links, approval states, and bidirectional traceability.
4. [done] Implement `vault-release` and `vault-project-close` for readiness, cutover, rollback, post-release verification, operational handover, lessons, and residual obligations — done when: both skills distinguish planned, approved, executed, verified, and closed states.
5. [done] Validate all new and changed canonical skills using the skill validator and realistic synthetic scenarios — done when: validation passes and scenario results contain no untraced requirement, design, delivery item, RAID entry, or release claim.

## Log
- 2026-07-28: phase drafted for seven focused lifecycle skills rather than one context-heavy all-purpose project-manager skill.
- 2026-07-28: phase began; sub-task 1 is initialising canonical skill folders.
- 2026-07-28: sub-task 1 completed with seven skill-creator initialisations and generated `agents/openai.yaml` metadata.
- 2026-07-28: sub-tasks 2–4 completed with concise workflows covering charter through closure and shared technical-contract enforcement.
- 2026-07-28: sub-task 5 completed; all new skills pass `quick_validate.py`, contain no TODOs, and pass a charter-to-closure scenario contract matrix for IDs, authority, traceability, gates, and evidence.
