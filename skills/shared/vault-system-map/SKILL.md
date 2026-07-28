---
name: vault-system-map
description: Create, update, verify, or analyse the technical source of truth for domains, systems, services, components, APIs, data stores, infrastructure, environments, and UI surfaces. Use when the principal asks for a system map, architecture inventory, service catalogue, dependency or interface map, infrastructure topology, environment overview, ownership map, impact analysis, operational readiness view, or wants repositories, IaC, dashboards, runbooks, and design artefacts connected to projects.
---

# Map systems and infrastructure

Load `rules/shared/35-technical-project-management.md` and
`memory/technical-assets/_template.md`. The vault records relationships and
verified pointers; source code, live configuration, and whole design artefacts
remain in their authoritative systems.

## Build or update the map

1. Search for existing `AST-*` records, aliases, owners, projects, decisions,
   designs, and external authorities. Reuse stable IDs.
2. Establish asset boundaries before decomposition:
   - domain for a business capability boundary;
   - system for a cohesive product/solution;
   - service/component for independently owned technical parts;
   - API/data-store for explicit contracts and data responsibility;
   - infrastructure/environment for provisioned/runtime boundaries;
   - UI surface for a user-facing experience with its own ownership or
     lifecycle.
3. Record purpose, responsibilities and non-responsibilities, lifecycle,
   criticality, technical/product/operations owners, and last verification.
4. Link authoritative artefacts with immutable version/revision where
   possible: repositories, paths, IaC, cloud/platform inventory, API/schema,
   design frame, dashboard, runbook, incident or service-management record.
5. Map upstream/downstream dependencies and interfaces in both directions.
   Record owner, contract/version, protocol, data classification, failure
   behaviour, compatibility, and needed-by/review dates.
6. Map environments, accounts/regions, deployment/IaC, data, access controls,
   SLOs, capacity, RTO/RPO, observability, support, security evidence, and
   known exceptions.
7. For UI surfaces, connect users/journeys, states, responsive/input behaviour,
   accessibility evidence, design-system version, analytics, and support
   signals.

## Analyse and verify

8. Link active projects, requirements, designs, work, RAID, and releases
   bidirectionally. A project changes an asset; it does not own the asset's
   entire history.
9. Flag missing owners, undocumented interfaces, single points of failure,
   environment drift, unversioned authorities, stale verification, absent
   runbooks/observability, and project changes without design or release
   traceability.
10. When asked for impact, traverse both dependency directions and distinguish
    recorded links from inferred blast radius.
11. Update indexes/history, project hubs, `memory/log.md`, and search. Run
    project health and vault health.

## Return

Provide the changed asset IDs, boundary and ownership summary, critical
dependencies/interfaces, authority freshness, gaps, and affected projects or
release gates. Use a diagram only when it clarifies relationships; the record
links remain authoritative.
