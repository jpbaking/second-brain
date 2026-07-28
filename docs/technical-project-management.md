# Technical project management

Second Brain can operate as the control plane for a technical project from
charter through operational handover. It connects product intent, requirements,
systems and infrastructure, technical and UI/UX design, delivery work, risks,
decisions, releases, and evidence without copying live tools into Markdown.

## What is authoritative

The vault is authoritative for:

- project charter, scope, outcomes, governance, baselines, and milestones;
- approved requirements, designs, decisions, ownership, and risk acceptance;
- traceability between what was requested, designed, delivered, released, and
  verified;
- current delivery state when it is backed by a named authority and
  verification date.

Executable and live artefacts remain authoritative in their native systems:

- Git for source code and configuration;
- IaC repositories and platform inventory for infrastructure;
- design tools for detailed UI/UX source artefacts;
- delivery trackers when the team uses one as the work authority;
- observability, deployment, incident, and service-management systems for
  runtime state.

Vault records carry durable links, revisions, owners, and `verified` dates.
This makes Second Brain the place to understand what everything means and how
it connects without allowing a copied diagram or status paragraph to outrank
live evidence.

## The record graph

Every technical record has a stable ID and YAML frontmatter describing its
current state.

| Record | ID | Purpose |
|---|---|---|
| Project | `PRJ-<slug>` | Charter, outcomes, governance, baseline, roadmap, and delivery health |
| Technical asset | `AST-<slug>` | Systems, services, APIs, data stores, infrastructure, environments, and UI surfaces |
| Requirement | `REQ-<project>-NNN` | Need, rationale, acceptance, priority, and verification |
| Design | `DES-<project>-NNN` | Technical, infrastructure, data, security, UI, or UX intent and approval |
| Work item | `WORK-<project>-NNN` | Outcome, workstream, epic, feature, or task with delivery evidence |
| RAID | `RAID-<project>-NNN` | Risk, assumption, issue, or dependency with owner and review |
| Release | `REL-<project>-YYYYMMDD[-N]` | Readiness, rollout, rollback, verification, and outcome |

Links are bidirectional. A requirement points to its design and work; the
design and work point back. A release points to included work and affected
assets; those records point back to the release. The project hub links every
register.

## Start a project

Ask:

> Plan a new technical project for replacing the customer identity service.
> The outcome is zero-downtime migration by 30 November. Start with a proposed
> charter and tell me what is still unknown.

The `vault-project-plan` skill:

1. searches for existing projects, systems, decisions, and evidence;
2. creates a stable project hub;
3. captures outcomes, scope, governance, milestones, and definition of done;
4. creates only the requirements, assets, design work, delivery work, RAID,
   and releases supported by current evidence;
5. presents the proposed baseline and gaps;
6. waits for named approval before marking the project or baseline active.

The first plan may contain `unknown` and `unassigned` fields. Those are honest
gaps, not validation failures hidden by invented facts.

## Map systems and infrastructure

Ask:

> Map the current identity domain: services, APIs, data stores, environments,
> repositories, IaC, owners, interfaces, observability, and runbooks. Show
> what is inferred or stale.

`vault-system-map` creates or updates long-lived `AST-*` records. A technical
asset may outlive many changing projects.

Capture the level of detail needed to reason about ownership and change:

- responsibilities and explicit boundaries;
- upstream/downstream dependencies and interface contracts;
- environments, accounts, regions, IaC, and deployment authority;
- data classification, residency, retention, and lineage;
- SLOs, capacity, resilience, RTO/RPO, security, and operations;
- repositories, dashboards, alerts, runbooks, and support;
- UI surfaces, journeys, states, responsive behaviour, accessibility, design
  system, analytics, and user-support signals.

Use durable external identifiers and immutable revisions where possible.
Never paste credentials, whole configuration files, or copied source code into
the vault.

## Manage requirements

Ask:

> Turn this PRD and research summary into atomic requirements. Separate user,
> functional, security, operational, performance, UI, and UX needs. Flag
> ambiguity and do not approve anything yet.

`vault-requirements` separates needs from assumptions, design choices, tasks,
and desired dates. Each requirement carries:

- source, rationale, owner, kind, priority, and version;
- observable acceptance criteria or a measurable non-functional threshold;
- affected systems and designs;
- implementing work and release;
- accepted verification evidence.

After approval, changes create a new version and impact assessment. The old
baseline remains visible and the approving decision links the change.

`implemented` means the work exists. `verified` means the acceptance evidence
passed. The project-health validator enforces that distinction.

## Govern technical and UI/UX design

Ask:

> Create a design-review record for the new sign-in experience. Cover service
> boundaries, API and data changes, infrastructure, failure modes, migration,
> user journeys, all UI states, responsive behaviour, accessibility, design
> system impact, observability, and rollback.

`vault-design` records the design intent, alternatives, review, and approval.
Detailed diagrams, prototypes, schemas, and design frames remain in their
authoritative tools and are linked by version.

A review traces the design to requirements and affected assets, then checks
the applicable concerns:

- architecture, dependencies, interfaces, and compatibility;
- infrastructure, environments, capacity, resilience, cost, and operations;
- data, privacy, threat/security, and compliance;
- migration, failure behaviour, rollback, testability, and observability;
- user research, journeys, content, states, input modes, responsive behaviour,
  accessibility, analytics, usability, and engineering hand-off.

Approval is a named state transition. Implementation and verification remain
separate later gates.

## Capture delivery updates

Ask:

> Update PRJ-identity from these notes. Reconcile milestone movement, changed
> requirements, design findings, blocked work, RAID, and release readiness.
> Show every old-to-new state and any authority conflict.

`vault-project-update` classifies each fact and updates the record that owns
it. It preserves prior baselines and status history, updates reciprocal links,
and distinguishes:

- discussed from approved;
- implemented from verified;
- deployed from healthy;
- closed work from achieved outcomes.

Inbox processing, chat capture, meetings, and decisions use the same fan-out
model. A meeting decision can update a requirement, design, work item, RAID,
release, project hub, reminder, and commitment in one traceable transaction.

## Review status and governance

Ask:

> Give me the evidence-backed status of PRJ-identity. Compare it with the
> approved baseline and cover requirements, systems, infrastructure, design,
> UI/UX, delivery, RAID, and release. Do not modify the vault.

`vault-project-status` is read-only unless you also ask it to record or
reconcile the result. It derives RAG from evidence and reports stale or
conflicting state as `unknown`.

For a portfolio:

> Show every active project ordered red, amber, unknown, then green. Include
> next gate, baseline movement, top RAID, release state, evidence age, shared
> system dependencies, and the decision needed from me.

Daily briefs, meeting preparation, weekly reviews, check-ups, handoffs, and
recall also traverse the technical record graph.

## Plan and assess a release

Ask:

> Assess REL-identity-20261130 for go/no-go. Check every readiness gate against
> evidence, including rollback, observability, support, security, data,
> infrastructure, UI/UX, and unresolved RAID.

`vault-release` records scope, environment/window, sequencing, owners,
deployment authority, compatibility, data migration, flags/exposure,
communications, support, observability, rollback, and verification.

It recommends `go`, `conditional go`, or `no-go`; only the named authority
sets the approved state. Unknown, stale, partial, or verbal-only evidence does
not pass a gate.

The procedure manages the release record. It does not deploy or change
infrastructure unless you separately request and authorise that action.

## Close and hand over

Ask:

> Audit PRJ-identity for closure. Verify outcomes, requirements, designs, work,
> releases, system ownership, operations, residual RAID, and benefits review.
> Keep it closing if any mandatory gate is missing.

`vault-project-close` confirms:

- outcomes against the approved charter and baseline;
- disposition of every approved requirement;
- design, work, release, infrastructure, security, and UI/UX evidence;
- operational ownership, runbooks, dashboards, support, and review dates;
- resolution, transfer, or explicit acceptance of every residual obligation;
- lessons and follow-up improvements with owners.

Closing a project does not retire its systems. Long-lived assets transfer to
their operational owners and continue to be verified independently.

## Mechanical integrity

Run:

```bash
python3 scripts/project_health.py --strict
python3 scripts/health.py
```

Project health checks:

- record frontmatter, stable IDs, canonical paths, kinds, and allowed states;
- project scope and required metadata;
- duplicate, dangling, and one-way traceability;
- missing project hubs and prematurely closed records;
- requirement, work, design, release, and closure evidence gates;
- unassigned ownership, stale authority, and overdue review;
- release readiness and unresolved obligations.

Warnings surface work that needs attention. Issues fail strict validation and
the staged commit check.

## Report templates

Reusable Markdown templates are available for:

- `technical-project-status.md`;
- `system-overview.md`;
- `design-review.md`;
- `release-readiness.md`.

The `report-builder` skill can turn them into recurring Markdown or offline
HTML/PDF reports while preserving your later formatting feedback.

## Migrating existing project pages

The technical model is stricter than the earlier RAID-lite project template.
An existing project page without the new frontmatter will be reported by
`project_health.py`.

Ask:

> Upgrade the existing identity project to the technical project-management
> model. Preserve every dated status, milestone, risk, and source. Assign
> stable IDs, create only records supported by evidence, update inbound links,
> and show me the proposed baseline before approving it.

The `vault-project-plan` procedure migrates the page in place:

1. preserve the existing dated history;
2. assign the stable `PRJ-*` ID and canonical filename;
3. move existing content into the project hub sections;
4. fan distinct requirements, assets, designs, work, RAID, and releases into
   their registers without inventing approval;
5. update links, indexes, and counts;
6. run project and vault health;
7. present unknowns and the proposed baseline for approval.

Do not bulk-convert existing prose into verified records. Migration preserves
what was recorded and makes missing authority or evidence visible.
