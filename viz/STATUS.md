# viz/ Shared Code Refactor

## Motivation

The four visualizers (`torus-explorer`, `dual-torus`, `multi-winding`,
`geodesic-curvature`) duplicate ~350 lines of identical code:

| Duplicated pattern | Lines × files | Total |
|--------------------|---------------|-------|
| `buildTorusGeom(a)` — manual BufferGeometry | 25 × 3 | 75 |
| Three.js scene setup (renderer, camera, OrbitControls, lights) | 20 × 4 | 80 |
| CSS (dark theme, slider thumb, button states, top-bar layout) | 40 × 4 | 160 |
| Torus geodesic point (`geodesicPoint3D` / `pt3d`) | 5 × 3 | 15 |
| Photon mesh + PointLight glow | 5 × 3 | 15 |
| Import map (Three.js 0.163.0 CDN) | 5 × 4 | 20 |
| Resize handler boilerplate | 5 × 4 | 20 |
| **Total** | | **~385** |

Practical consequences today:
- Updating the Three.js version requires editing 4 import maps.
- A torus geometry bug must be found and fixed in 3 places.
- Creating a new visualizer requires copy-pasting ~100 lines of boilerplate.
- UI styling drifts (geodesic-curvature already has slightly different slider
  widths, font sizes, and button classes from the other three).

## Architecture

Three layers, no build step. Everything works with `open viz/foo.html` or a
simple HTTP server.

```
viz/
  totu-viz.css          ← Layer 0: shared stylesheet
  totu-viz.js           ← Layer 1: shared JS module
  torus-explorer.html   ← Layer 2: individual visualizers
  dual-torus.html
  multi-winding.html
  geodesic-curvature.html
  index.html
```

### Layer 0 — `totu-viz.css`

Shared dark-theme stylesheet. Each HTML file adds
`<link rel="stylesheet" href="totu-viz.css">` and keeps only page-specific
overrides in an inline `<style>` block.

Provides:
- CSS custom properties for the palette (`--bg`, `--surface`, `--accent`,
  `--text`, `--muted`, etc.)
- Reset (`*`, `body`)
- Slider styling (range input, thumb)
- Button / toggle / preset-btn base classes
- Layout primitives: `.top-bar`, `.ctrl-group`, `.val`, `.sep`, `.toggle`
- Split-view and full-view containers
- Info panel, legend, and note overlays
- Badge variants (`.b-ring`, `.b-horn`, `.b-spindle`)

Estimated size: ~90 lines.

### Layer 1 — `totu-viz.js`

ES module exporting pure utility functions. Each HTML file imports what it
needs:

```js
import { createScene, buildTorusGeom, torusPt,
         createPhoton, PALETTE } from './totu-viz.js';
```

#### Exports

| Export | Signature | Notes |
|--------|-----------|-------|
| `PALETTE` | `{ bg, surface, path, photon, … }` | Hex color constants |
| `THREE_VERSION` | `'0.163.0'` | Single source of truth for CDN URL |
| `createScene` | `(container, opts?) → { scene, camera, renderer, controls, clock }` | Sets background, pixel ratio, OrbitControls with damping, standard lighting rig. `opts` can override FOV, near/far, damping, lights. |
| `autoResize` | `(renderer, camera, container) → unlisten` | Installs a resize observer; returns cleanup function. |
| `animLoop` | `(tick: (dt, elapsed) => void, deps: { renderer, scene, camera, controls }) → stop` | RAF loop with controls.update and render. Returns stop function. |
| `buildTorusGeom` | `(R, a, segU?, segV?) → BufferGeometry` | Torus in XZ plane, axis Y. Defaults segU=64, segV=128. |
| `torusPt` | `(t, R, a, p, q) → Vector3` | Point on (p,q) geodesic at parameter t. |
| `torusPathGeom` | `(R, a, p, q, opts?) → TubeGeometry` | Full (p,q) geodesic tube. `opts`: segments, tubeR, closed. |
| `createPhoton` | `(opts?) → { mesh, glow }` | SphereGeometry + PointLight child. |
| `torusMaterials` | `(opts?) → { surface, wireframe }` | Standard translucent torus materials. |

Estimated size: ~130 lines.

### Layer 2 — individual visualizers

Each HTML file:
1. Links `totu-viz.css`.
2. Contains the same import map (or we extract it to a shared `<script>`).
3. Imports from `./totu-viz.js` plus Three.js.
4. Defines its own state object, model, rebuild functions, UI wiring, and any
   page-specific CSS overrides.
5. Remains fully self-contained in terms of physics / presentation logic.

No visualizer becomes a "thin wrapper" — each keeps its unique model code.
The shared layer only eliminates mechanical duplication.

---

## Implementation checklist

### Phase 1 — Create shared files (no existing file changes)

- [ ] **1.1** Write `totu-viz.css` with palette variables, reset, slider/button
      styles, layout primitives. Verify it renders correctly in isolation
      (import from a test page).
- [ ] **1.2** Write `totu-viz.js` exporting `createScene`, `autoResize`,
      `animLoop`, `buildTorusGeom`, `torusPt`, `torusPathGeom`,
      `createPhoton`, `torusMaterials`, `PALETTE`.
- [ ] **1.3** Write a minimal smoke-test HTML (`_test-shared.html`) that imports
      both files and renders a spinning torus with a photon. Verify all
      exports work. Delete after Phase 2.

### Phase 2 — Migrate visualizers (one at a time, test after each)

Migrate in order of increasing complexity so regressions are caught early.

- [ ] **2.1 torus-explorer.html** — simplest (single view, no 2D canvas).
      Replace inline CSS with `<link>` + page overrides. Replace scene setup,
      torus geom, geodesic path, photon, resize, and anim loop with shared
      imports. Verify all presets, sliders, checkboxes, and info panel still
      work.
- [ ] **2.2 dual-torus.html** — split view. Same as 2.1 plus verify 2D canvas
      still renders and photon syncs across both views.
- [ ] **2.3 multi-winding.html** — most complex torus viz. Same as 2.1 plus
      verify multi-loop paths, shear, and winding presets.
- [ ] **2.4 geodesic-curvature.html** — uses different scene model (no shared
      torus mesh in sphere mode; `genTorus()` for mass elements in torus
      mode). Only migrate CSS, `createScene`, `autoResize`, `animLoop`,
      and palette constants. The torus mass-element generation and
      Brill-Lindquist physics stay page-local.

### Phase 3 — Unify import map

- [ ] **3.1** Consider extracting the import map to a shared
      `<script src="totu-importmap.js">` or just keep it inline (it's only
      5 lines and ES import maps can't be loaded from external files in all
      browsers yet). If keeping inline, at least ensure all files reference
      the same version string via a comment pointing to `totu-viz.js`
      `THREE_VERSION`.

### Phase 4 — Polish

- [ ] **4.1** Delete `_test-shared.html`.
- [ ] **4.2** Update `README.md` to document the shared code convention.
- [ ] **4.3** Update `index.html` card descriptions if any wording changed.
- [ ] **4.4** Visual audit: open each visualizer side-by-side with a
      pre-refactor screenshot and confirm pixel-level consistency
      (no style regressions).

---

## Design constraints

1. **No build step.** Files must work from `open viz/foo.html` or
   `python3 -m http.server`.
2. **No framework.** The shared code is a utility library, not a
   component system.
3. **Self-contained visualizers.** Each HTML file owns its physics model,
   parameters, and interaction logic. Shared code only covers mechanical
   boilerplate.
4. **Backwards compatible.** After migration, every visualizer must behave
   identically to its pre-migration version.
5. **Import map stays inline.** ES import maps loaded from external scripts
   are not yet widely supported. Each file keeps its own inline import map,
   but all reference the same Three.js version.

## Decision log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-03-18 | Adopt 3-layer architecture | 385 lines of duplication across 4 files; project is growing |
| 2026-03-18 | Torus in XZ plane, axis Y | Matches existing `torus-explorer`, `dual-torus`, `multi-winding` convention and Three.js TorusGeometry after 90° X rotation |
| 2026-03-18 | No build step | Simplicity; all files must work with `open` or simple HTTP server |
