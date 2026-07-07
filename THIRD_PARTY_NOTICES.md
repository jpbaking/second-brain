# Third-party notices

The vault template is licensed under 0BSD (see [LICENSE](LICENSE)).
The following vendored material is licensed separately.

## IBM Plex fonts — SIL Open Font License 1.1

`reports/design/lazyway/fonts/*.woff2` are the IBM Plex Sans and IBM Plex
Mono typefaces, © 2017 IBM Corp., self-hosted so reports open fully
offline. They are licensed under the **SIL Open Font License 1.1** — full
text at [reports/design/lazyway/fonts/OFL.txt](reports/design/lazyway/fonts/OFL.txt).
The OFL permits bundling, redistribution, and use, but the fonts remain
under the OFL (not 0BSD), and the license text must stay with the font
files.

## lazyway-io-design kit

`reports/design/lazyway/` is vendored from
<https://github.com/jpbaking/lazyway-io-design> (with the Google Fonts
`@import` replaced by the self-hosted fonts above). At the time of
vendoring, that repository declares no license; it is included here with
the owner's permission — treat it as **not covered by this project's
0BSD grant** unless/until the upstream repository declares its own
license. The logo and mesh assets in `reports/design/lazyway/assets/`
are brand assets of lazyway.io; reuse them as brand identifiers is not
granted by any code license.

`reports/design/claude/charts.js` is derived from the same kit's chart
engine and carries the same status. The rest of the `claude` kit
(styles, components, kit.js, templates) was authored for this project
and is covered by the 0BSD license.

## Favicon set

`reports/design/lazyway/assets/favicons/` ships with the lazyway kit —
same status as the kit itself. The kit's favicon-generation tooling
(`scripts/make-favicons.sh` upstream) is not vendored here.
