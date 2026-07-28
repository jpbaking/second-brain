---
name: report-builder
description: Build a markdown or HTML report from the vault and run the template-evolution loop, so formatting feedback is given once and then lives in reports/templates/ forever. Trigger when the principal asks for a report, summary document, status update, one-pager, brief, pre-read, dashboard page, or an "updated" version of a previous report, or gives formatting or structure feedback on one.
---

# Report builder

Companion to `rules/shared/40-reports.md` — that file is the contract; this
skill is the procedure. The core promise: **formatting feedback is given
once**, then lives in `reports/templates/` forever.

## Steps

1. **Clarify only what is essential and unstated** — the subject, and the
   format (markdown or HTML) if it is not inferable. Decide everything else
   yourself and note your assumptions in the reply.
2. **Identify the report type.** Is this a repeat of something in
   `reports/templates/` or `reports/YYYY/`? "The usual team status" or
   "update the June report" means: find the previous one, reuse its template,
   and include a *changes since last report* section.
3. **Template resolution order:** an exact template in `reports/templates/` →
   the previous report of the same type in `reports/` (derive the structure,
   then save it as a template) → design fresh. A fresh design becomes a
   template candidate the moment the principal gives feedback.
4. **Gather** via the retrieval rules in `rules/shared/30-retrieval.md`.
   Every claim must trace to memory pages — include a discreet Sources
   section or footnotes. Note gaps in the report itself rather than smoothing
   over them.
   For technical project, system, infrastructure, design/UI/UX, delivery, or
   release reports, also load
   `rules/shared/35-technical-project-management.md` and include stable IDs,
   authority, verification dates, baseline movement, traceability, RAID, and
   evidence gates.
5. **Format:**
   - Markdown: clean headings, tables for enumerable facts, and links to
     memory pages as sources.
   - HTML: build on one of the vendored design kits under `reports/design/`
     per `rules/shared/40-reports.md`, referenced with relative paths. No
     external assets or CDN requests, and print-friendly.
6. **Deliver:** write to `reports/YYYY/YYYY-MM-DD_slug.md` or `.html`, append
   a `report` entry to `memory/log.md`, and reply with the path, a two- to
   four-line executive summary, and any data gaps that weakened the report
   ("no entries for X since May").
7. **On feedback:** apply it to the output **and** persist it to the template
   with `{{placeholders}}` and `<!-- guidance: why -->` comments capturing the
   feedback. Confirm: "Template updated — next time this is automatic."
