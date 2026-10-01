# RIAAK search

The site's search box. It is a copy of the template's own `dg-search` plugin
with one change: a search first asks RIAAK's meaning-based search service
(`/api/search`, which Netlify forwards to `riaak.vercel.app`) and only falls
back to the offline keyword index if that fails. Searches that start with `#`
(tag searches) still use the offline index.

## Why it is a separate plugin

Until template 1.91.0 this code lived in
`src/site/_includes/components/searchScript.njk`. The template update on
1 October 2026 replaced that file with the stock search, which quietly turned
the smart search off. The template updater only rewrites the `dg-*` plugin
folders, so code kept here survives future updates.
`src/plugins/plugins.json` switches `dg-search` off so the two don't both draw a
search box.

## After a template update

`templates/searchButton.njk` and `templates/search-index.njk` are unchanged
copies of `dg-search`'s. `index.js` differs in two places: the name of its
index template, and how it writes hashtags into `searchIndex.json`. `dg-search`
writes them raw, so a single hashtag containing a backslash or a quote mark
makes the whole index invalid and the search box stops responding (this
happened on 1 October 2026). This copy encodes them properly. `templates/searchContainer.njk` is `dg-search`'s plus the changes
marked "Semantic search". If an update improves `dg-search`, compare it with
these files and copy the improvements across:

```bash
diff -r src/plugins/dg-search src/plugins/riaak-search
```
