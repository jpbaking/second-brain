---
type: technical-asset
id: AST-stable-slug
title: Technical asset name
date: YYYY-MM-DD
updated: YYYY-MM-DD
status: planned
owner: unassigned
project: none
authority: external
authority-ref: durable system, repository, IaC, or design identifier
verified: YYYY-MM-DD
tags: []
kind: system
review-by: YYYY-MM-DD
---

# Technical asset: {{Name}}

## Identity and purpose

- **Kind:** domain | system | service | component | api | data-store |
  infrastructure | environment | ui-surface
- **Purpose:** {{Capability and users/consumers}}
- **Lifecycle:** planned | active | deprecated | retired
- **Business criticality:** low | medium | high | critical
- **Technical owner:** {{Team/person}}
- **Product/operations owner:** {{Team/person}}

## Authoritative artefacts

| Artefact | Authority | Version / revision | Verified | Owner |
|---|---|---|---|---|
| Source / configuration | {{Repository/path}} | {{Revision}} | YYYY-MM-DD | {{Owner}} |
| Infrastructure as code | {{Repository/path}} | {{Revision}} | YYYY-MM-DD | {{Owner}} |
| UI/UX source | {{Tool/frame or library}} | {{Version}} | YYYY-MM-DD | {{Owner}} |
| Runtime inventory | {{Platform/resource identifier}} | {{Version/state}} | YYYY-MM-DD | {{Owner}} |

## Architecture and boundaries

- **Responsibilities:** {{What it owns}}
- **Does not own:** {{Explicit boundaries}}
- **Upstream dependencies:** {{AST IDs, contracts, owners}}
- **Downstream consumers:** {{AST IDs, contracts, owners}}
- **Interfaces:** {{Protocol, API/event/schema, version, compatibility policy}}
- **Data:** {{Stores, classifications, residency, retention, lineage}}

## Environments and infrastructure

| Environment | Account / region | Deployment/IaC | Data | Access / controls | Verified |
|---|---|---|---|---|---|
| {{Environment}} | {{Location}} | {{Reference}} | {{Classification}} | {{Reference}} | YYYY-MM-DD |

## Reliability, security, and operations

- **SLO / availability:** {{Objective and measurement}}
- **Capacity / scaling:** {{Limits and triggers}}
- **RTO / RPO:** {{Targets or not applicable}}
- **Security / threat model:** {{DES/decision/evidence}}
- **Observability:** {{Dashboards, alerts, logs, traces}}
- **Runbook / support:** {{Runbook, on-call, escalation}}
- **Known debt / exceptions:** {{RAID or WORK IDs}}

## UI/UX surface

<!-- Complete for user-facing assets. -->

- **Users and journeys:** {{Personas, journeys, research evidence}}
- **States:** {{Loading, empty, error, success, permissions, offline}}
- **Responsive behaviour:** {{Breakpoints/input modes}}
- **Accessibility:** {{Target, audit evidence, known gaps}}
- **Design system:** {{Components/tokens and version}}

## Active traceability

- **Projects:** {{PRJ IDs}}
- **Requirements:** {{REQ IDs}}
- **Designs:** {{DES IDs}}
- **Work items:** {{WORK IDs}}
- **Open RAID:** {{RAID IDs}}
- **Releases:** {{REL IDs}}

## History

- YYYY-MM-DD: {{Dated lifecycle, ownership, interface, or verification change}}

## Sources

{{Vault evidence and durable external authority links.}}
