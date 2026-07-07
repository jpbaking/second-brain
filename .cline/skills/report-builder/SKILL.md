---
name: report-builder
description: Build a markdown or HTML report from the vault and run the template-evolution loop. Trigger when the principal asks for a report, summary document, status update, one-pager, dashboard page, or an "updated" version of a previous report, or gives formatting feedback on one.
---

# Report builder

Companion to `.clinerules/40-reports.md` — that file is the contract; this
skill is the procedure. The core promise: **formatting feedback is given
once**, then lives in `reports/templates/` forever.

## Steps

1. **Identify the report type.** Is this a repeat of something in
   `reports/templates/` or `reports/YYYY/`? "The usual team status" or
   "update the June report" means: find the previous one, reuse its
   template, and include a *changes since last report* section.
2. **Template resolution order:** exact template in `reports/templates/`
   → previous report of the same type in `reports/` (derive the structure,
   then save it as a template) → design fresh.
3. **Gather** via retrieval rules; claims trace to memory pages. Note gaps
   in the report itself rather than smoothing over them.
4. **Format:**
   - Markdown: clean headings, tables for enumerable facts, links to
     memory pages as sources.
   - HTML: one self-contained file, inline CSS, no external assets,
     print-friendly, restrained professional styling.
5. **Deliver:** write to `reports/YYYY/YYYY-MM-DD_slug.md|.html`, log in
   `memory/log.md`, reply with path + executive summary.
6. **On feedback:** apply to the output AND persist to the template with
   `{{placeholders}}` and `<!-- guidance: why -->` comments capturing the
   feedback. Confirm: "Template updated — next time this is automatic."
