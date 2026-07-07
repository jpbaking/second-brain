# Design kits

One folder per kit; every kit is **fully offline** (no CDN, no web fonts
fetched at view time — reports must open via `file://` with zero network
requests). Report templates live at `reports/templates/<kit>.<shape>.html`
and reference their kit as `../design/<kit>/…` — generated reports in
`reports/YYYY/` sit at the same depth, so templates copy over with no path
rewriting.

| Kit | Look | Themes | Rules / reference |
|---|---|---|---|
| [lazyway/](lazyway/) | lazyway.io brand: IBM Plex (self-hosted), brand blue `#12279E`, one amber accent | light only | `lazyway-io-design` skill; [lazyway/CHEATSHEET.md](lazyway/CHEATSHEET.md) |
| [claude/](claude/) | Claude AI web: warm ivory / warm charcoal, terracotta `#D97757`, serif display type | light + dark (toggle, persisted; OS default; print always light) | `claude-report-design` skill |

## Choosing a kit

Ask the principal on first use of a report type, then record the choice in
the report-type's template (the template's kit IS the choice). Don't mix
kits within one report.

## Adding a kit

1. `reports/design/<name>/` — self-contained: CSS (+ fonts if any, self-hosted),
   JS. Define the `--chart-1..5`, `--chart-grid/axis/label/value`, `--base`,
   `--chart-other`, `--chart-area-opacity` and `--font-sans` tokens and the
   shared `charts.js` engine works unchanged.
2. Keep the shared class vocabulary where semantics match (`.container`,
   `.card`, `.table`, `.data-list`, `.stat`, `.tab*`, `.alert`, `.badge`,
   `.btn`, `.prose`, `.chart`) so templates port between kits.
3. Add `reports/templates/<name>.{document,deck,interactive}.html`.
4. Add a skill under `.cline/skills/` with the kit's rules; update this table.
