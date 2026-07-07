# CHEATSHEET — build a page in this design system

Self-contained instructions. Follow them literally. When unsure, copy a demo page from `demos/` and edit the text.

## Rules (absolute)

1. NEVER write custom CSS if a class below does the job. If you must write CSS, use ONLY `var(--…)` tokens. NEVER hardcode a color, px size, or shadow.
2. ONE amber element per page: a `.kicker`, OR one `.nav-link.active`, OR one `.stat-highlight`, OR one `.alert-warn`. Pick one. (Badges and chart colors don't count.)
3. Backgrounds: white or solid brand blue only. NO gradients.
4. UPPERCASE mono (`.mono-label`, `.kicker`, `.tag`, `.label`…) is for labels only — never body text.
5. Every page MUST have the three favicon `<link>` lines. If favicon files don't exist, generate them: `./scripts/make-favicons.sh logo.svg webroot/ "Site Name"`.
6. Logos: rounded blue tile `#12279E`, white linework, exactly ONE amber `#D9821F` dot.
7. Copy tone: plain and understated; British spelling (organise, centre); no exclamation marks.

## Page skeleton (start every page like this)

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page — Site</title>
  <meta name="description" content="One plain sentence.">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="stylesheet" href="/design/styles.css">
  <link rel="stylesheet" href="/design/components.css">
</head>
<body>
  ...content...
  <script src="/design/components.js"></script>  <!-- only if using modal/tabs/pickers -->
  <script src="/design/charts.js"></script>      <!-- only if using charts -->
</body>
</html>
```

## Page shapes — copy the matching demo

- Single-function app (one form does one job) → copy `demos/tool.html`
- Product/landing page → copy `demos/landing.html`
- Dashboard → copy `demos/dashboard.html`
- Blog → copy `demos/blog.html`
- Docs → copy `demos/docs.html`

## Components (copy-paste)

**Nav** (top of `<body>`):
```html
<header class="nav-wrap"><nav class="nav container">
  <a href="/" class="brand"><img src="/design/assets/logo-mark.svg" alt=""><span class="brand-name">Site</span></a>
  <ul class="nav-links" role="list">
    <li><a href="/x" class="nav-link active">X</a></li>
    <li><a href="/y" class="nav-link">Y</a></li>
  </ul>
</nav></header>
```

**Hero** (white; `.hero-invert` for blue):
```html
<section class="hero">
  <img class="hero-mesh" src="/design/assets/mesh-blue.svg" alt="" aria-hidden="true">
  <div class="hero-inner container">
    <div class="kicker">// Eyebrow text</div>
    <h1 class="headline">Calm, confident headline.</h1>
    <p class="lead">One or two muted sentences.</p>
    <div class="hero-actions">
      <a href="#" class="btn btn-primary">Primary</a>
      <a href="#" class="btn btn-secondary">Secondary</a>
    </div>
  </div>
</section>
```

**Section with head row**:
```html
<section class="section container">
  <div class="section-head">
    <div class="section-kicker">// Label</div>
    <h2 class="section-title">Title</h2>
    <a href="#" class="section-all">All →</a>
  </div>
  ...content...
</section>
```

**Cards** (grid of 3): `<div class="grid-3">` containing:
```html
<div class="card">
  <div class="card-meta"><span class="tag">tag</span> <span class="badge badge-live">Live</span></div>
  <h3 class="card-title">Title</h3>
  <p class="card-desc">Muted description.</p>
</div>
```
Clickable card: `<a class="card tile" href="#">…</a>`.

**Stats** (`<div class="grid-stats">`; at most ONE `.stat-highlight`):
```html
<div class="stat"><div class="stat-value">99.98%</div><div class="stat-label">Uptime</div></div>
```

**Buttons:** `.btn btn-primary` (solid blue) / `btn-secondary` (outline) / `btn-quiet` / `btn-danger` / add `btn-sm`. On blue backgrounds: `btn-on-blue` / `btn-outline-on-blue`. Small copy button: `.copy-btn`.

**Badges:** `<span class="badge badge-live">Live</span>` (`-pilot -shipped -planned -danger`). **Tags:** `<span class="tag">name</span>`.

**Table:**
```html
<div class="table-wrap"><table class="table">
  <thead><tr><th>Name</th><th class="num">Count</th></tr></thead>
  <tbody><tr><td>api</td><td class="num">24,910</td></tr></tbody>
</table></div>
```

**Key/value list:**
```html
<div class="data-list">
  <div class="data-row"><span class="data-key">IP</span><span class="data-value">203.0.113.7</span></div>
</div>
```

**Form field:**
```html
<div class="field">
  <label class="label" for="e">Email</label>
  <input class="input" id="e" placeholder="you@example.com">
  <span class="field-hint">Optional hint.</span>
</div>
```
Also: `.select`, `.textarea`, `.search-input`, `.checkbox`, `.radio`, `.switch` (input + `<span class="switch-track">`), error state `.input-error` + `.field-error`.

**Alert:** `<div class="alert alert-info"><span class="alert-title">Note</span><span>Text.</span></div>` (`-success -warn -danger`).

**Modal** (needs components.js):
```html
<button class="btn btn-secondary" data-modal-open="#m1">Open</button>
<dialog id="m1" class="modal">
  <div class="modal-head"><h3 class="modal-title">Title</h3><button class="modal-close" data-modal-close>Close ✕</button></div>
  <div class="modal-body"><p>Body.</p></div>
  <div class="modal-foot"><button class="btn btn-quiet" data-modal-close>Cancel</button><button class="btn btn-primary" data-modal-close>OK</button></div>
</dialog>
```

**Tabs** (needs components.js):
```html
<div data-tabs>
  <div class="tab-list"><button class="tab active" data-tab-target="#t1">One</button><button class="tab" data-tab-target="#t2">Two</button></div>
  <div class="tab-panel" id="t1">…</div>
  <div class="tab-panel" id="t2" hidden>…</div>
</div>
```

**Date / time pickers** (needs components.js): `<input class="input" data-datepicker>` (→ `2026-07-02`), `<input class="input" data-timepicker="15">` (→ `14:30`).

**Progress:** `<div class="progress"><div class="progress-fill" style="width: 42%;"></div></div>` (add `.warn`/`.danger` to the fill).

**Long-form text:** wrap rendered markdown/article HTML in `<div class="prose">…</div>` — headings, lists, quotes, code, tables are styled.

**Footer:**
```html
<footer class="footer"><div class="footer-inner container">
  <div class="foot-brand"><img src="/design/assets/logo-mark-invert.svg" alt=""><span class="foot-name">Site</span></div>
  <div class="foot-links"><a class="foot-link" href="#">GitHub</a></div>
  <div class="foot-copy">&copy; 2026 Site</div>
</div></footer>
```

**Single-function app page** (the url-shortener shape — see `demos/tool.html` for the full working example):
```html
<body class="app-page">
  <section class="app-hero">
    <a class="app-brand" href="/"><img src="/design/assets/logo-mark.svg" alt=""><span class="app-wordmark">tool.example</span></a>
    <p class="app-kicker">What this tool is</p>
    <h1 class="app-title">The one question it answers.</h1>
    <p class="app-tagline">One sentence of instructions.</p>
  </section>
  <section class="action-card">
    <form class="input-row"><input class="input" placeholder="…"><button class="btn btn-primary">Go</button></form>
    <div class="result-block">
      <span class="mono-label">Result</span>
      <div class="result-row"><a class="result-link" href="#">the-answer</a><button class="copy-btn">Copy</button></div>
    </div>
  </section>
  <footer class="app-foot">One quiet footer line.</footer>
</body>
```

## Charts (needs charts.js; container: `<div class="chart">` + title + a target div)

```js
lwCharts.bar("#el",  { labels: ["Q1","Q2"], series: [{ name: "Plan", values: [40,55] }] });
lwCharts.line("#el", { labels: [...], series: [{ name, values }], area: true }); // area: 1 series only
lwCharts.donut("#el",{ slices: [{ label: "API", value: 41 }], totalLabel: "total" });
lwCharts.sparkline("#el", { values: [3,5,4,7] }); // inside a .stat
```
Never pass colors (they're assigned from `--chart-1..5` in order). Max 5 series. Never two y-axes.

## Diagrams (mermaid) — copy the init from `demos/docs.html` (theme "base" + token hexes), put the diagram in a `.card`.

## React — start a new app from `starter/react/` (README §7 has the 5 copy steps). Components live in `components/react/`: `Modal`, `Tabs`, `DatePicker`, `TimePicker`, `DataTable`, `StatTile`, `Chart`. Same two stylesheets required; `Chart` also needs `/design/charts.js`; never load `/design/components.js` in a React app.
