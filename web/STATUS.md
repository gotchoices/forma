# Forma website — STATUS

## Current state

**Draft 1** — initial site published locally, not yet deployed.

### Pages

| Page               | File                 | Status |
|--------------------|----------------------|--------|
| Home               | `home.html`          | Draft — hero + tiles + pull-quote |
| The Idea           | `idea.html`          | Draft — condensed *whatif.md* + *gut.md* |
| GRID & MaSt        | `architecture.html`  | Draft — two-layer explainer, split sections |
| Results            | `results.html`       | Draft — stat row, spectrum table, open-problems list |
| Read               | `read.html`          | Draft — three reading paths linking to GitHub |
| About              | `about.html`         | Draft — disclaimers, reliability table, license |

### Infrastructure

- `index.html` shell + `styles.css` + `script.js` hash-router — working.
- `server.sh` — local dev server on :8080.
- `publish.sh` — rsync deploy to `/var/www/formares.org`.

## Open items

- [ ] User review pass on page content.
- [ ] Consider a favicon.
- [ ] Consider adding a News or Updates page once the project has a
      cadence of visible milestones.
- [ ] Crop / downsize hero images if the current PNGs render too large on
      mobile.
- [ ] DNS pointing `formares.org` at the target host (infrastructure task).
- [ ] Smoke-test at `http://localhost:8080/` before first publish.

## Design decisions (fixed unless the user asks otherwise)

- Branding: **Forma** in header, *The Shape of Things* as italic tagline.
- Six-page nav: Home / The Idea / GRID & MaSt / Results / Read / About.
- Template pattern: single `index.html` shell, content fragments loaded
  via hash routing (mirrors `devel/ser/sereus/docs/web/`).
- Tone: quiet and technical, not triumphalist.  The *finish-what-Einstein-
  started* angle is present but softened.
