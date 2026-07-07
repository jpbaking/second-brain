/* claude kit — theme toggle + tabs. Zero dependencies, offline.
   Theme: persisted in localStorage("claude-report-theme"); default follows
   the OS. Charts are SVG baked at render time, so pages that draw charts
   should expose them via  window.renderCharts = function () {…}  — the kit
   re-invokes it on every theme change and around printing. Printing always
   happens in light theme. */
(function () {
  "use strict";
  var KEY = "claude-report-theme";
  var root = document.documentElement;

  function current() {
    var forced = root.getAttribute("data-theme");
    if (forced) return forced;
    return matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function apply(theme, persist) {
    root.setAttribute("data-theme", theme);
    if (persist) { try { localStorage.setItem(KEY, theme); } catch (e) {} }
    document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
      btn.textContent = theme === "dark" ? "☀ light" : "☾ dark";
      btn.setAttribute("aria-pressed", theme === "dark");
    });
    if (typeof window.renderCharts === "function") window.renderCharts();
  }

  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);

  document.addEventListener("DOMContentLoaded", function () {
    apply(current(), false);
    document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        apply(current() === "dark" ? "light" : "dark", true);
      });
    });

    /* tabs — same markup API as the lazyway kit */
    document.querySelectorAll("[data-tabs]").forEach(function (group) {
      var tabs = group.querySelectorAll(".tab[data-tab-target]");
      tabs.forEach(function (tab) {
        tab.addEventListener("click", function () {
          tabs.forEach(function (t) { t.classList.remove("active"); });
          tab.classList.add("active");
          group.querySelectorAll(".tab-panel").forEach(function (p) { p.hidden = true; });
          var panel = group.querySelector(tab.getAttribute("data-tab-target"));
          if (panel) panel.hidden = false;
        });
      });
    });
  });

  /* print: force light + light charts, restore after */
  var before = null;
  addEventListener("beforeprint", function () {
    before = current();
    if (before === "dark") apply("light", false);
  });
  addEventListener("afterprint", function () {
    if (before === "dark") apply("dark", false);
    before = null;
  });
})();
