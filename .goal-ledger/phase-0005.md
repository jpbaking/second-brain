# phase-0005 — Integrate governance and reporting workflows

- Status: done
- Depends on: phase-0003, phase-0004
- Goal: Make existing capture, meeting, recall, review, status, and report procedures maintain and consume the expanded project truth consistently.
- Done when: Cross-cutting skills update the right technical records, status and governance views use traceable evidence and freshness, and reusable report shapes cover delivery, architecture, and release decisions.

## Sub-tasks
1. [done] Update inbox, remember, meeting, decision, and reindex procedures to classify and fan out technical delivery facts — done when: each procedure routes requirements, assets, designs, work, RAID, and releases without duplicating the authoritative record.
2. [done] Upgrade project status, briefs, meeting prep, weekly review, recall, and check-up procedures to traverse the full traceability graph — done when: outputs distinguish baseline, current evidence, change, staleness, risk, and required decisions.
3. [done] Add reusable report templates for technical project status, system overview, design review, and release readiness — done when: each template cites authority, last verification, traceability gaps, decisions, and asks.
4. [done] Exercise an end-to-end synthetic project from charter through requirement, system/design, delivery risk, release, and closure — done when: every record is reachable from the project hub and every status assertion resolves to dated evidence.

## Log
- 2026-07-28: phase drafted to prevent the new registers from becoming isolated documentation silos.
- 2026-07-28: phase began; sub-task 1 is integrating technical classification and fan-out into capture workflows.
- 2026-07-28: sub-task 1 completed across inbox, chat capture, meetings, decisions, and reindexing with authority-aware technical record classification and reciprocal fan-out.
- 2026-07-28: sub-task 2 completed across project status, briefs, preparation, weekly review, recall, check-up, handoff, and report building.
- 2026-07-28: sub-task 3 completed with technical-project-status, system-overview, design-review, and release-readiness report templates.
- 2026-07-28: sub-task 4 completed with a reciprocal end-to-end synthetic closure graph; corrected closure validation so operational assets may remain active after the changing project closes.
- 2026-07-28: phase check passed with all skill validators, 20 unit tests, strict project health, integrated vault health, and whitespace checks.
- 2026-07-28: phase-close staging later exposed trailing spaces used as Markdown hard breaks in four new report templates; the commit succeeded because the shell sequence did not stop on `git diff --cached --check`. The content checks remained green; whitespace correction moved immediately to phase-0006.
