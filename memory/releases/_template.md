---
type: release
id: REL-project-YYYYMMDD
title: Release or change title
date: YYYY-MM-DD
updated: YYYY-MM-DD
status: planned
owner: unassigned
project: PRJ-stable-slug
authority: vault
authority-ref: release plan or deployment authority
verified: YYYY-MM-DD
tags: []
kind: release
window: YYYY-MM-DDTHH:MMZ
review-by: YYYY-MM-DD
---

# Release: {{ID}} — {{Title}}

## Scope and outcome

- **Kind:** release | migration | infrastructure-change | experiment
- **Objective:** {{Outcome}}
- **Window / environments:** {{When and where}}
- **Included work:** {{WORK IDs}}
- **Requirements / designs:** {{REQ and DES IDs}}
- **Assets affected:** {{AST IDs}}
- **Explicitly excluded:** {{Scope not shipping}}

## Readiness gates

- [ ] Scope and baseline approved — {{evidence}}
- [ ] Included work done and acceptance evidence linked — {{evidence}}
- [ ] Design, security, data, infrastructure, and UI/UX gates complete as applicable — {{evidence}}
- [ ] Test and non-functional evidence accepted — {{evidence}}
- [ ] Deployment, migration, and rollback rehearsed or reviewed — {{evidence}}
- [ ] Observability, runbooks, support, and communications ready — {{evidence}}
- [ ] Open RAID disposition accepted — {{evidence}}
- [ ] Go/no-go authority approved — {{decision, actor, time}}

## Deployment and rollback

- **Runbook / automation:** {{Versioned authority}}
- **Sequence and owners:** {{Steps and hand-offs}}
- **Data migration / compatibility:** {{Plan and verification}}
- **Feature flags / exposure:** {{Plan}}
- **Rollback trigger:** {{Observable threshold}}
- **Rollback procedure and limit:** {{Authority and point of no return}}

## Verification and operations

- **Immediate checks:** {{Functional and technical signals}}
- **SLO / business measures:** {{Target, dashboard, observation window}}
- **UI/UX validation:** {{Journey, accessibility, analytics, support evidence}}
- **Security / compliance:** {{Evidence}}
- **Operational owner / support:** {{Acceptance and escalation}}

## Timeline

| Date/time | State | Actor | Evidence / observation |
|---|---|---|---|
| YYYY-MM-DD | planned | {{Actor}} | {{Source}} |

## Outcome and follow-up

- **Result:** {{Verified, rolled back, partial, cancelled}}
- **Evidence:** {{Metrics, tests, incidents, sign-off}}
- **Residual RAID / work:** {{IDs and owners}}
- **Post-release review:** {{Date and source}}
- **Closure authority:** {{Actor and date}}
