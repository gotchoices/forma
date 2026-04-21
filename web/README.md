# Forma — Website

This directory contains the static marketing / entry-point website for the
Forma project (published at **formares.org**).  The goal is a quiet, readable
site that helps people *find* the project, understand what it is, and pick a
reading path into the open-source content on GitHub.

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
| `home.html`        | Landing page (hero + 3 tiles). |
| `idea.html`        | *The Idea* — plain-language core pitch. |
| `architecture.html`| *GRID & MaSt* — the two-layer architecture. |
| `results.html`     | *Results* — headline findings and open problems. |
| `read.html`        | *Read* — three reading paths (scientific / intuitive / reflective). |
| `about.html`       | *About* — who, why, AI disclosure, reliability, license. |
| `images/`          | Page imagery (`proton.png`, `grid-2D.png`, `grid-3D.png`, `electron.png`, …). |
| `server.sh`        | Simple local dev server (`python3 -m http.server`). |
| `publish.sh`       | Rsync deploy to formares.org. |

### Template pattern

`index.html` is the only "shell" file.  All other pages are content fragments
loaded by `script.js` via `fetch()` and injected into `#content`.  Navigation
uses URL hashes (`#home`, `#idea`, `#architecture`, `#results`, `#read`,
`#about`) so links are bookmarkable and browser back/forward works.

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

- **Tone.**  Quiet and technical rather than triumphalist.  The project
  proposes something ambitious ("finish what Einstein started") but the site
  deliberately softens that — it is a careful invitation, not a manifesto.
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

Draft 1 — initial site covering: home, idea, architecture, results, read,
about.  Ready for content review and local preview.
