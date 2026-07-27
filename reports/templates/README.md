# Report templates

Templates grow out of feedback: when the principal shapes a report's
format, the agent persists that shape here (`{{placeholders}}` +
`<!-- guidance -->` comments recording the why). Next request of the same
kind uses the template automatically.

## Base HTML templates (fully offline)

Named `<kit>.<shape>.html` — kits live in [../design/](../design/) (see its
README for the kit index) and are referenced via relative paths, so files
open straight from disk (`file://`) with zero network requests and export
to PDF via the browser's Print → Save as PDF or `scripts/export-pdf.sh`.
Generated reports in `reports/YYYY/` are at the same depth as this folder,
so templates copy over with no path rewriting.

Three shapes per kit:

- `*.document.html` — "Word document": A4 portrait pages, paper look on
  screen, `@page` print CSS, `.page-break` helper.
- `*.deck.html` — "PowerPoint": 16:9 slides (13.333in × 7.5in),
  scroll-snap + arrow-key navigation on screen, one slide per PDF page.
- `*.interactive.html` — responsive single-page report: stats, tabs,
  charts, filterable table; printing flattens the tabs so the PDF captures
  every panel.

Kits: `lazyway.*` (lazyway.io brand — one amber element, tokens only, no
gradients; see the `lazyway-io-design` skill) and `claude.*` (Claude AI web
light/dark, terracotta accent, persisted theme toggle, print always light;
see the `claude-report-design` skill).

Derive report-type templates (e.g. `team-status.html`) from these rather
than from scratch, keeping each kit's rules.

## Markdown

Starter template for performance evaluations lives with its skill at
`skills/shared/performance-evaluation/templates/`; once evolved,
its copy here takes precedence.
