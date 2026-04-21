# Forma — Website

This directory contains the static entry-point website for the Forma project
(published at **formares.org**).  The goal is deliberately narrow: give people
a general sense of the project, explain why it matters, and route them into
the open-source repository where the real work lives.

The actual research — papers, primers, studies, models, GRID and MaSt docs —
lives one directory up, in the parent project at
[`github.com/gotchoices/forma`](https://github.com/gotchoices/forma).  This
website links into that material rather than duplicating it.

---

## Files

| File | Role |
|------|------|
| `index.html`       | Page shell: header, nav, footer, empty `<main>` container. |
| `styles.css`       | All styling.  Single stylesheet, no build step. |
| `script.js`        | Hash-based router: loads `{page}.html` into `#content`. |
| `home.html`        | Main landing page: what Forma is, why it matters, and where to go next. |
| `read.html`        | *Start Here* — the shortest path into the GitHub repo. |
| `about.html`       | *About* — scope, claims, authorship, AI use, and how to judge the work. |
| `images/`          | Page imagery (`proton.png`, `grid-2D.png`, `grid-3D.png`, `electron.png`, …). |
| `server.sh`        | Simple local dev server (`python3 -m http.server`). |
| `publish.sh`       | Rsync deploy to formares.org. |

### Template pattern

`index.html` is the only "shell" file.  All other pages are content fragments
loaded by `script.js` via `fetch()` and injected into `#content`.  Primary
navigation uses URL hashes (`#home`, `#read`, `#about`) so links are
bookmarkable and browser back/forward works. Older hashes are still mapped
gracefully for compatibility.

To add a page:

1. Create `newpage.html` with a content fragment (no `<html>`, `<head>`, or
   `<body>` — just the inner content).
2. Add the page slug to the `PAGES` array in `script.js` and the `titleCase`
   map.
3. Add a nav entry in `index.html`.

---

## Local development

```bash
cd web
./server.sh          # serves on :8080
# or pick a port:
./server.sh 9000
```

Visit <http://localhost:8080/index.html#home>.

No build step.  Edit any file and reload.

---

## Publishing

```bash
cd web
./publish.sh                       # rsync to root@gotchoices.org:/var/www/formares.org
./publish.sh me@myhost /srv/site   # custom host and path
```

The deploy script excludes itself, the README, and the local-dev server
script so the production site stays clean.

DNS for `formares.org` should point at the same host serving the other
gotchoices.org sites.

---

## Design notes

- **Tone.**  Quiet, readable, and non-technical.  The project proposes
  something ambitious, but the site is intentionally brief and inviting rather
  than exhaustive.
- **Images.**  The site currently uses `proton.png`, `grid-3D.png`, and
  `electron.png` directly in the content pages, with `grid-2D.png` available
  as an alternate GRID render in `images/`.
- **Typography.**  `Fraunces` (serif) for display + pull-quotes; `Inter`
  (sans) for body text and UI.
- **Palette.**  Ink-blue primary (#1a2e4a), bronze accent (#b47a3c), warm
  ivory paper (#faf8f3) — intended to feel more like a printed essay than a
  landing page.
- **Math.**  `MathJax` is loaded lazily from a CDN so any TeX in future
  content pages renders automatically.  Present pages use very little math,
  by design.

---

## STATUS

Draft 2 — reduced site structure centered on three live pages: Home, Start
Here, and About.  The repo is now treated explicitly as the main destination.
