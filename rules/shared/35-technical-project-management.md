# Technical project management: source-of-truth contract

Use this contract whenever work concerns a product, project, system,
infrastructure, API, data store, environment, technical or UI/UX design,
requirement, delivery item, RAID entry, or release.

The vault is a **technical delivery control plane**. It is authoritative for
what is intended, approved, owned, connected, at risk, and reported. It does
not pretend that copied prose is more current than executable or live systems.

## Authority hierarchy

Record both `authority` and `verified` in technical-record frontmatter.
`verified` is the last date the record was checked against its authority, not
merely the date the page was edited.

| Information | Authoritative source | What the vault stores |
|---|---|---|
| Project charter, scope, baseline, governance, milestone commitments | Approved vault project and decision records | Current approved state plus append-only change history |
| Requirements and acceptance criteria | Approved vault requirement record, or a named external requirements system | Stable ID, current baseline/version, source, approval, traceability |
| Architecture and design intent | Approved vault design and decision records, or a named external design system | Design status, versioned artefact link, requirements, affected assets, reviewers |
| Source code and configuration | Git repository and immutable revision | Repository/path, revision or release, owner, last verification |
| Provisioned infrastructure | IaC repository plus cloud/platform inventory | IaC path/revision, account/region/environment, drift or exception evidence |
| UI/UX source artefacts | Named design tool and immutable version/frame | Artefact link/version, approved design record, research and accessibility evidence |
| Work execution | Vault work item or a named external tracker | Stable cross-reference, owner, state, dates, blocked reason, linked evidence |
| Runtime behaviour and reliability | Observability, incident, deployment, and service-management systems | Dashboard/runbook/incident links, SLOs, last verification, interpreted status |
| Raw evidence | `library/` original | Immutable original plus links to derived records |

When an external system is authoritative, write `authority: external` and
record its durable URL or identifier in `authority-ref`. When the vault is
authoritative, write `authority: vault` and link the approving decision or
meeting. Never copy secrets, credentials, source code, live configuration, or
whole design files into `memory/`.

If authorities disagree, do not silently choose. Preserve both dated claims,
mark the vault record `⚠ authority conflict`, identify the owning human or
system, and make reconciliation an open work item or RAID entry.

## Common record metadata

Every technical record begins with YAML frontmatter containing:

```yaml
---
type: project | technical-asset | requirement | design | work-item | raid | release
id: STABLE-ID
title: Plain title
date: YYYY-MM-DD
updated: YYYY-MM-DD
status: allowed-status
owner: person, team, or "unassigned"
project: PRJ-stable-slug | none
authority: vault | external
authority-ref: relative link, durable external identifier, or "chat YYYY-MM-DD"
verified: YYYY-MM-DD
tags: []
---
```

- `id` never changes, even if the title or filename changes.
- `updated` is the latest dated material change.
- `verified` advances only when checked against the authoritative source.
- Use `unassigned`, `unknown`, or `none` explicitly; never invent a value to
  satisfy a field.
- Frontmatter is current machine-readable state. Preserve prior state in the
  dated history section of the page.

## Stable IDs and locations

| Record | ID | Canonical location |
|---|---|---|
| Project or programme | `PRJ-<stable-slug>` | `memory/projects/prj-<stable-slug>.md` |
| Technical asset | `AST-<stable-slug>` | `memory/technical-assets/ast-<stable-slug>.md` |
| Requirement | `REQ-<project-slug>-NNN` | `memory/requirements/prj-<project-slug>/req-<project-slug>-NNN_<slug>.md` |
| Design | `DES-<project-slug>-NNN` | `memory/designs/prj-<project-slug>/des-<project-slug>-NNN_<slug>.md` |
| Work item | `WORK-<project-slug>-NNN` | `memory/work-items/prj-<project-slug>/work-<project-slug>-NNN_<slug>.md` |
| RAID entry | `RAID-<project-slug>-NNN` | `memory/raid/prj-<project-slug>/raid-<project-slug>-NNN_<slug>.md` |
| Release | `REL-<project-slug>-YYYYMMDD[-N]` | `memory/releases/prj-<project-slug>/rel-<project-slug>-YYYYMMDD[-N].md` |

Choose the next unused project-scoped sequence by inspecting both the area
index and files. Never reuse an ID from a deleted, rejected, or superseded
record. Technical assets are long-lived and may link to many projects.

## Record kinds and lifecycle

Only use these states. Moving backwards requires a dated reason and, after
approval or baseline, a linked decision.

| Record | Kinds | Normal lifecycle |
|---|---|---|
| Project | project, programme, initiative | `proposed → active ↔ on-hold → closing → closed`; terminal `cancelled` |
| Technical asset | domain, system, service, component, api, data-store, infrastructure, environment, ui-surface | `planned → active → deprecated → retired` |
| Requirement | business, user, functional, non-functional, technical, security, operational, ui, ux | `draft → proposed → approved → implemented → verified → retired`; terminal `rejected`, `superseded` |
| Design | product, solution, software, api, data, infrastructure, security, ui, ux | `draft → in-review → approved → implemented → verified`; terminal `rejected`, `superseded`, `retired` |
| Work item | outcome, workstream, epic, feature, task | `backlog → ready → in-progress ↔ blocked → done → verified`; terminal `cancelled` |
| RAID | risk, assumption, issue, dependency | `open → monitoring | mitigating → resolved | accepted | closed` |
| Release | release, migration, infrastructure-change, experiment | `planned → ready → approved → deploying → deployed → verified → closed`; terminal `rolled-back`, `cancelled` |

Do not infer a transition from optimistic prose. Record the approving evidence,
effective date, and actor. `done` means work was performed; `verified` means
acceptance evidence passed.

## Minimum traceability

Links are bidirectional. When adding or changing one side, update the linked
record in the same task.

- A **project** links its current baseline, milestones, requirements, designs,
  technical assets, work items, open RAID, releases, decisions, and sources.
- A **technical asset** links owners, dependent assets, interfaces,
  environments, repositories/IaC, operational evidence, active projects, and
  designs that define it.
- A **requirement** links its source and rationale, project, acceptance
  criteria, affected assets, implementing designs and work items, and
  verification evidence. Approved requirements without implementation or
  planned disposition are gaps.
- A **design** links the requirements it satisfies, assets it changes,
  decisions, versioned source artefacts, reviewers, work items, and validation
  evidence. UI/UX designs additionally link user evidence, states, responsive
  behaviour, accessibility criteria, and design-system impact where relevant.
- A **work item** links its parent/outcome, requirements, designs, assets,
  milestone or release, dependencies, owner, and completion evidence.
- A **RAID entry** links every impacted project, requirement, asset, design,
  work item, milestone, or release, plus owner, next action, and review date.
- A **release** links included work items and requirements, affected assets and
  environments, approved designs/decisions, readiness evidence, deployment and
  rollback plans, observability, sign-offs, and post-release verification.

Do not mark a requirement, design, work item, release, or project verified or
closed while its mandatory downstream evidence or residual obligations are
missing. Use `unknown` and open a gap rather than manufacturing traceability.

## Baselines and change control

A baseline is a dated, approved set of requirement, design, milestone, and
release references recorded on the project page.

1. Before approval, edit draft content normally while keeping dated source
   references.
2. On approval, append a baseline entry with the approving evidence and the
   exact record IDs and versions.
3. After approval, never rewrite the earlier baseline. Propose the change,
   record impact across scope, schedule, risk, systems, infrastructure, UI/UX,
   operations, and release, then link the approving decision.
4. Update current frontmatter and append a dated change entry. Mark replaced
   records `superseded by` with a link; do not delete them.
5. For rejected or cancelled work, preserve the reason and any accepted
   residual risk or obligation.

## Status and freshness

Every status assertion answers:

- **As of when?**
- **According to which authority?**
- **What changed since the previous status?**
- **What evidence supports done, verified, green, ready, or closed?**
- **What is unknown, stale, blocked, or in conflict?**

Project status becomes unreliable after 30 days without verified delivery
evidence. Technical assets and approved designs become review-due after 90
days unless they declare a shorter `review-by` date. Requirements, RAID
entries, and releases use their explicit review or due dates. A stale record
is not automatically wrong, but it cannot support an unqualified current
claim.

## Source-of-truth update transaction

For any technical delivery update:

1. Read the project hub and all directly affected records.
2. Check the named authority before changing current state.
3. Update the authoritative vault records and their dated histories.
4. Update both sides of every traceability link.
5. Fan out actions to work items, reminders, commitments, or RAID as
   appropriate.
6. Update area indexes, root counts when pages were created, and
   `memory/log.md`.
7. Run the technical project-health check and `scripts/health.py`.
8. Report the changed IDs, evidence, unresolved conflicts, and next gates.
