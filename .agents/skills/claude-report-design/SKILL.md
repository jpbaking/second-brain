---
name: claude-report-design
description: Build HTML reports in the "claude" design kit — Claude AI web look, warm ivory light theme and warm charcoal dark theme, terracotta #D97757 accent, serif display type, persisted light/dark toggle. Use when the principal asks for a report in the claude kit/style/theme, mentions Claude-style or light/dark reports, or a report template based on reports/design/claude.
---

# claude-report-design — how to build report pages

Kit location (vendored, fully offline): `reports/design/claude/` —
`styles.css` (themed tokens) + `components.css` + `kit.js` (theme toggle,
tabs, print-light) + `charts.js` (token-driven SVG charts).

## Rules

1. No custom CSS when a documented class does the job; unavoidable custom
   CSS uses `var(--…)` tokens only — never hardcode colors, sizes, shadows.
2. **Never style for one theme.** Every color must come from a token so both
   themes work. Check anything custom in light AND dark before finishing.
3. Terracotta (`--accent`) is for emphasis, not decoration: eyebrows, the
   active tab, key actions. Semantic states use `--success/--warn/--danger`
   and their washes.
4. Serif display faces (`--font-display`, via `h1–h3`/`.display`/
   `.stat-value`) are for headings and hero numbers only — body text stays
   `--font-sans`. Uppercase mono (`.eyebrow`, `.label`, `.mono-label`,
   `.stat-label`) is for short labels only.
5. Reference the kit with relative `../design/claude/…` paths; zero external
   URLs (no CDNs, no web fonts — the kit uses system font stacks).
6. Include the theme toggle (`<button class="theme-toggle" data-theme-toggle>`)
   on interactive pages; `kit.js` wires it, persists the choice, and forces
   light for printing.
7. Charts: init inside `window.renderCharts = function () {…}` and call it
   once — `kit.js` re-renders on theme change and around printing. Never pass
   colors (auto from `--chart-1..5`, themed per mode); ≤5 series.

## Start from a template (copy, then edit text only)

- `reports/templates/claude.document.html` — Word-style A4 document
- `reports/templates/claude.deck.html` — 16:9 slide deck (cover slide is
  fixed charcoal regardless of theme)
- `reports/templates/claude.interactive.html` — responsive one-pager
  (stats, tabs, charts, filterable table)

All print to PDF via Print → Save as PDF or `scripts/export-pdf.sh`.

## Class vocabulary

- Layout: `.container` (1080px) / `.container-narrow` (720px) / `.section` /
  `.grid-2` `.grid-3` `.grid-stats`
- Header: `.bar` > `.bar-brand` (with `.brand-dot`) + `.bar-actions`;
  `.theme-toggle`
- Headings: `.eyebrow` (mono uppercase, terracotta) · `.display` · `.lead` ·
  `.section-title` · `.muted` · `.mono-label`
- Buttons: `.btn btn-primary / btn-secondary / btn-quiet`, size `btn-sm`
- Cards: `.card` > `.card-title` + `.card-desc`
- Stats: `.stat` > `.stat-value` + `.stat-label`; one `.stat-highlight` max
- Badges: `.badge badge-info / -ok / -warn / -danger / -accent`
- Table: `.table-wrap` > `table.table`, numeric cells `.num`
- Key/value: `.data-list` > `.data-row` > `.data-key` + `.data-value`
- Alerts: `.alert alert-success / -warn / -danger` > `.alert-title` + text
- Tabs (kit.js): `[data-tabs]` > `.tab-list` > `.tab` with
  `data-tab-target="#panel"` (+`.active` on first) + `.tab-panel` divs
  (`hidden` on all but first)
- Forms: `.field` > `.label` + `.input`; `.search-input`
- Charts: `.chart` > `.chart-title` + `.chart-sub` + target div;
  `lwCharts.bar/line/donut/sparkline`
- Long-form: `.prose`; footer: `.footer`

## Checklist before finishing

- [ ] Both stylesheets + `kit.js` linked with relative `../design/claude/` paths
- [ ] Looks right in light AND dark (toggle it); print preview is light
- [ ] No hardcoded colors outside tokens; no external URLs
- [ ] Charts inside `window.renderCharts`; no custom chart colors
