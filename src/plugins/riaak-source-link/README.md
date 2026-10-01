# RIAAK source link

Shows each note's original source just under its title and tags:
"Original source: frontiersin.org · 2021 · Academic Paper", or "Listen to the
episode · 2019" on podcast pages.

The link comes from the note's `Url` property (or `source_url`, or `source`).
The Digital Garden plugin passes a note's properties to the site as
`dg-note-properties`, and the template exposes them as `noteProps`. Notes
without a stored http(s) link show nothing.

It lives in its own plugin folder so template updates, which rewrite the
template's own `dg-*` plugins and files, leave it alone. `src/plugins/plugins.json`
gives it `"order": -1` so it sits above the created/updated dates.
