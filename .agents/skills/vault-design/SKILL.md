---
name: vault-design
description: Create, capture, review, approve, change, trace, or assess a product, solution, software, API, data, infrastructure, security, UI, or UX design in the vault. Use for architecture proposals, RFCs, technical designs, infrastructure plans, API/data contracts, threat-model decisions, UI flows, UX research-to-design work, design reviews, accessibility reviews, alternatives, implementation hand-off, or design impact analysis.
---

# Manage technical and UI/UX design

Load `rules/shared/35-technical-project-management.md`,
`memory/designs/_template.md`, the project hub, requirements, and affected
technical assets.

The vault design page is the approval and traceability record. Keep detailed
source diagrams, prototypes, code, schemas, and design files in their
authoritative repository/tool and record an immutable version.

## Create or change a design

1. Establish the problem, constraints, users, affected assets, requirements,
   success measures, and authority. Search existing `DES-*` records and
   decisions before creating one.
2. Assign the next unused `DES-<project>-NNN` ID and correct kind. Keep it
   `draft` until evidence is ready for review.
3. Describe boundaries, structure, behaviour, interfaces, data, failure modes,
   environments, deployment, migration, rollback, observability, operations,
   cost, security, and compatibility to the degree relevant.
4. Record alternatives, trade-offs, rejected options, assumptions, and RAID.
   Significant choices link to decision records.
5. For UI/UX design, include:
   - users, jobs, journeys, and research evidence;
   - information architecture and end-to-end flows;
   - loading, empty, error, success, validation, permission, and offline
     states;
   - content, interaction, input modes, and responsive behaviour;
   - accessibility targets and verification;
   - design-system components/tokens, prototype version, analytics and
     usability evidence, and engineering hand-off.

## Review and approve

6. Trace requirements and assets in both directions. Link implementation work,
   release/migration, validation evidence, decisions, and RAID.
7. Review against requirement coverage, failure behaviour, operability,
   security/privacy, data, performance/capacity, resilience, testability,
   migration/rollback, UI/UX consistency, accessibility, and ownership.
8. Record each review finding, owner, disposition, evidence, and date. Open
   work or RAID for unresolved material concerns.
9. Only named authority moves a design to `approved`. `implemented` requires
   delivery evidence; `verified` requires accepted technical and user evidence
   as applicable.
10. A change to an approved design creates a new version and impact analysis.
    Preserve the prior version, update the project baseline if needed, and link
    an approving decision.

## Finish

11. Update linked records, indexes, project hub, `memory/log.md`, and search.
    Run project health and vault health.
12. Return the design ID/version, recommendation, requirements covered,
    affected assets, review findings, RAID, and approval or evidence still
    required.
