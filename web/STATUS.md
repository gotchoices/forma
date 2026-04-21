# Forma website — STATUS

## Current state

**Draft 2** — simplified site published locally, not yet deployed.

### Pages

| Page               | File                 | Status |
|--------------------|----------------------|--------|
| Home               | `home.html`          | Draft — concise landing page focused on importance + repo handoff |
| Start Here         | `read.html`          | Draft — shortest route into the repository |
| About              | `about.html`         | Draft — scope, claims, AI use, and how to judge the work |

### Infrastructure

- `index.html` shell + `styles.css` + `script.js` hash-router — working.
- Primary nav reduced to `Home / Start Here / About`.
- `server.sh` — local dev server on :8080.
- `publish.sh` — rsync deploy to `/var/www/formares.org`.

## Open items

- [ ] User review pass on page content.
- [ ] Consider a favicon.
- [ ] Crop / downsize hero images if the current PNGs render too large on
      mobile.
- [ ] DNS pointing `formares.org` at the target host (infrastructure task).
- [ ] Smoke-test at `http://localhost:8080/` before first publish.

## Design decisions (fixed unless the user asks otherwise)

- Branding: **Forma** in header, *The Shape of Things* as italic tagline.
- Three-page nav: Home / Start Here / About.
- Template pattern: single `index.html` shell, content fragments loaded
  via hash routing (mirrors `devel/ser/sereus/docs/web/`).
- Tone: quiet, inviting, and non-technical.  The repo is treated as the real
  destination rather than duplicating its detail on the site.
