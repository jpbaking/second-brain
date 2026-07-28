# phase-0006 — Document, synchronise, and acceptance-test

- Status: done
- Depends on: phase-0005
- Goal: Ship the technical project-management capability coherently across every supported agent harness and user-facing guide.
- Done when: Documentation explains the model and workflows, generated adapters exactly match canonical skills, all tests and health checks pass, staged validation passes, and the goal is ready for user acceptance.

## Sub-tasks
1. [done] Add a technical project-management guide and update the README, user guide, and architecture documentation — done when: a new user can initialise, operate, review, release, and close a technical project from the documented plain-language prompts.
2. [done] Update the root skill inventory and repository maps for all new rules, areas, scripts, and skills — done when: no documented path or skill name is stale and all local Markdown links resolve.
3. [done] Regenerate every harness adapter from `skills/shared/` — done when: `./scripts/sync-agent-adapters.sh --check` reports exact synchronisation.
4. [done] Run skill validation, unit tests, vault health, project health, whitespace checks, and staged commit validation — done when: every required command passes with no unresolved warning that undermines source-of-truth integrity.
5. [done] Review the complete diff for confidentiality, generated artefacts, portability, and backwards compatibility — done when: the worktree contains only goal-owned changes and the final handoff names any intentional migration impact.

## Log
- 2026-07-28: phase drafted as the release-quality integration and acceptance gate.
- 2026-07-28: phase began; sub-task 1 includes immediate correction of report-template trailing whitespace surfaced during phase-0005 closeout.
- 2026-07-28: sub-task 1 completed with a full lifecycle guide, migration procedure, README positioning, user guide, architecture, and report-template documentation.
- 2026-07-28: sub-task 2 completed with updated root skill inventory, memory/script maps, and validated user-documentation links.
- 2026-07-28: sub-task 3 completed with 25 canonical skills copied exactly into both generated adapter trees; final resync follows the migration note.
- 2026-07-28: sub-task 4 began after pre-acceptance skill, unit, project-health, vault-health, adapter, link, whitespace, and secret checks passed.
- 2026-07-28: sub-task 4 completed after the final canonical change was resynchronised and all 75 canonical/adapter skill validations, 20 unit tests, strict project health, integrated vault health, local links, whitespace, and secret scans passed.
- 2026-07-28: sub-task 5 completed; protected library/log history is untouched, generated trees match canonical skills byte-for-byte, only goal-owned paths changed, and the documented migration impact is that legacy RAID-lite project pages require stable IDs/frontmatter and register fan-out before strict project health passes.
- 2026-07-28: phase complete; goal is ready for user acceptance.
