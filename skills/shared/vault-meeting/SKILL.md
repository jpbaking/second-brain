---
name: vault-meeting
description: File meeting minutes into the vault and fan out the consequences to reminders, people dossiers, project hubs, requirements, technical assets, designs, work items, RAID, releases, and decisions. Use when the principal gives you a meeting to record — pasted notes, a file in the inbox, or a verbal recap — or asks to write up, file, or capture what happened in a meeting.
---

# File meeting minutes

The principal is giving you a meeting to record, as pasted notes, a file in
the inbox, or a verbal recap.

## Steps

1. If it arrived as a file, first handle the original with the `vault-inbox`
   procedure so it lands in `library/` and its year catalog. The memory page
   below then links to it.
2. Create `memory/meetings/YYYY/YYYY-MM-DD_topic-slug.md` from
   `memory/meetings/_template.md`, capturing attendees, agenda and context,
   discussion summary, **decisions**, **action items** with owner and due
   date, and open questions.
3. Fan out the consequences, linking each entry back to the meeting page:
   - Action items owned by the principal → `memory/notes/reminders.md`.
   - Facts about attendees (commitments, accomplishments, concerns) → their
     dossiers in `memory/people/`.
   - Project decisions and status → the project page in `memory/projects/`.
   - Scope, acceptance, or user need → the matching `REQ-*` record; use
     `vault-requirements` when it needs refinement or approval.
   - System, interface, environment, infrastructure, or UI-surface facts →
     `AST-*`, checked against their named authority.
   - Architecture, infrastructure, security, UI, or UX direction → `DES-*`
     plus a decision when approved.
   - Delivery progress/blockers → `WORK-*`, project milestone, and `RAID-*`
     as applicable.
   - Readiness, go/no-go, deployment, rollback, or observed outcome →
     `REL-*`; never promote meeting confidence into verification.
   Apply `rules/shared/35-technical-project-management.md` and update both
   sides of each technical link.
4. Update `memory/meetings/index.md` and the counts in `memory/index.md`,
   then append a `meeting` entry to `memory/log.md`.
5. Reply with the decisions and action-item list, plus where it was filed.
