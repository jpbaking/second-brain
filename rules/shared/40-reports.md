# Reports and the template-evolution loop

The principal will ask for reports (status summaries, performance
evaluations, briefs) in **markdown or HTML**. The contract: formatting
feedback given once should never need to be given twice.

## Producing a report

1. **Check `reports/templates/` first.** If a template matching the request
   exists, use it — structure, headings, tone, and format exactly.
2. Gather content per the retrieval rules (vault only, cited, dated).
3. Write the output to `reports/YYYY/YYYY-MM-DD_slug.md` (or `.html`), and
   log it in `memory/log.md`.
4. In chat, give the file path and a 2–4 line executive summary.

Technical project reports also follow
`35-technical-project-management.md`. Include record IDs, the authority and
verification date behind current claims, changes from the approved baseline,
traceability gaps, open RAID, decisions or approvals needed, and the next
delivery or release gate. Never colour a project green from narrative alone.

## HTML reports

HTML reports use one of the **design kits** vendored fully offline under
`reports/design/<kit>/` (no network requests — files open via `file://`
with no CORS/referrer issues). Kit index: `reports/design/README.md`.
Currently: `lazyway` (lazyway.io brand — `lazyway-io-design` skill) and
`claude` (Claude AI web light/dark — `claude-report-design` skill).

- Pick the kit per report type: ask on first use, then the report-type
  template's kit is the recorded choice. Never mix kits in one report.
- Reference kits with **relative paths** (`../design/<kit>/...` — templates
  and `reports/YYYY/` sit at the same depth, so no rewriting when copying a
  template). Never absolute `/design/...` paths, never CDN/external URLs
  (that includes mermaid; skip diagrams that need a CDN).
- Start from the base templates `reports/templates/<kit>.<shape>.html`,
  shapes: `document` (Word-style A4), `deck` (PowerPoint-style 16:9),
  `interactive` (responsive one-pager). All print to PDF via the browser's
  Print → Save as PDF, honoring their `@page` CSS.
- To hand over a ready PDF, run `scripts/export-pdf.sh <report.html>`
  (headless Chrome) and give the principal both the HTML and PDF paths.

## Word / PowerPoint requests

The principal does not want `.docx`/`.pptx` files: a "Word document" means
`document.html`, a "deck/slides/PowerPoint" means `deck.html`, exported to
PDF as above.

## Evolving templates

When the principal gives formatting/structure feedback on a report:

1. Apply it to the report.
2. **Persist it**: create or update the matching template in
   `reports/templates/` (e.g. `team-status.md`, `perf-eval.html`).
   Templates contain the fixed skeleton plus `{{placeholders}}` and HTML
   comments (`<!-- guidance: ... -->`) recording *why* — the feedback that
   shaped each part.
3. Say that you updated the template, so the principal knows the feedback
   stuck.

Never fork a near-duplicate template; refine the existing one. If the
principal asks for a one-off deviation, deviate without changing the
template unless they say "from now on".

## Recurring reports

If a report is clearly recurring ("weekly team status"), name outputs
consistently and, in the report, include a "changes since last report"
section by diffing against the previous output in `reports/`.
