# phase-0004 — Add deterministic project-health validation

- Status: done
- Depends on: phase-0002
- Goal: Make technical source-of-truth integrity mechanically testable instead of relying on agent judgement alone.
- Done when: Standard-library validation detects duplicate or malformed IDs, invalid states, missing required metadata, broken traceability, unowned or stale controls, and incomplete release or closure gates; automated tests cover valid and invalid fixtures.

## Sub-tasks
1. [done] Implement a reusable parser for the technical-record frontmatter and links — done when: it loads all seven record kinds, reports file-local parse errors, and has unit tests.
2. [done] Validate identity, allowed states, required fields, ownership, dates, and index membership — done when: fixtures prove each invalid class is detected and a complete fixture passes.
3. [done] Validate cross-record traceability and lifecycle gates from requirement through design, work, release, and evidence — done when: orphan, dangling, contradictory, and prematurely closed fixtures fail with actionable messages.
4. [done] Add staleness, overdue review, unmitigated RAID, and source-verification diagnostics — done when: date-controlled tests exercise fresh, warning, and overdue cases deterministically.
5. [done] Integrate project-health results into the main health and staged-commit validation paths — done when: the normal repository commands surface technical integrity failures without third-party dependencies.

## Log
- 2026-07-28: phase drafted to make “source of truth” a verifiable property rather than a documentation claim.
- 2026-07-28: phase began; sub-task 1 is implementing the technical-record parser.
- 2026-07-28: sub-task 1 completed with a standard-library frontmatter and technical-link parser for all seven record kinds.
- 2026-07-28: sub-tasks 2–4 completed with schema/path/state/ownership/date checks, project scope, reciprocal traceability, lifecycle gates, closure checks, and deterministic freshness diagnostics.
- 2026-07-28: sub-task 5 completed by integrating strict project health into `scripts/health.py` and technical-model changes into `scripts/validate_commit.py`.
- 2026-07-28: phase check passed with 19 unit tests, strict empty-vault project health, integrated vault health, and `git diff --check`.
