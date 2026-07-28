# phase-0001 — Define the technical delivery contract

- Status: done
- Depends on: none
- Goal: Define what the vault owns, how technical delivery records relate, and how truth changes without erasing history.
- Done when: The canonical rules and root routing specify the authority hierarchy, record identities and lifecycle states, minimum traceability, baseline/change-control behaviour, and staleness/conflict handling for every planned technical record type.

## Sub-tasks
1. [done] Define the federated authority hierarchy for vault records versus Git, IaC, design tools, ticketing systems, and runtime platforms — done when: a canonical rule names the authoritative source and required last-verified evidence for each class of information.
2. [done] Define stable IDs, metadata, lifecycle states, and allowed transitions for projects, technical assets, requirements, designs, work items, RAID entries, and releases — done when: the canonical rule contains a complete schema and transition table for all seven record types.
3. [done] Define bidirectional traceability, baseline, change-control, contradiction, supersession, and append-only history rules — done when: the rule states required links and preservation behaviour from requirement through design, delivery, release, and evidence.
4. [done] Route technical-project work through the root, structure, capture, retrieval, and report contracts — done when: every affected root or shared rule links to the new contract and a local Markdown-link check passes.

## Log
- 2026-07-28: phase drafted from the gap between the current RAID-lite project page and the requested full technical source of truth.
- 2026-07-28: phase began; sub-task 1 is defining the federated authority hierarchy.
- 2026-07-28: sub-tasks 1–3 completed in `rules/shared/35-technical-project-management.md`; the rule defines the authority matrix, common metadata, stable IDs, states, traceability, baselines, and freshness.
- 2026-07-28: sub-task 4 completed by routing the contract from `AGENTS.md` and shared structure, capture, retrieval, and report rules; all added links resolve.
- 2026-07-28: phase check passed with `python3 scripts/health.py` and `git diff --check`.
