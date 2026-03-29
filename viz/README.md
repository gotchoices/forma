# Visualizations

Interactive browser-based tools for exploring the geometry of the photon-knot
electron model. Each file is self-contained — open directly in any modern
browser, no server required.

## Tools

| File | Tag | Description |
|------|-----|-------------|
| [`dual-torus.html`](dual-torus.html) | R3 | Side-by-side 3D torus and 2D flat rectangle with a synchronized photon on a (1,2) geodesic. |
| [`torus-explorer.html`](torus-explorer.html) | S2 | Interactive 3D torus with a/R slider. Morph from thin ring through horn torus to sphere-like blob. |
| [`R8-multi-winding.html`](R8-multi-winding.html) | R8 | Multi-winding electron geometry. Many-orbit photon paths, winding number vs torus size. |
| [`geodesic-curvature.html`](geodesic-curvature.html) | GR | Geodesic/field-line grid around a spherical or toroidal Compton zone. 3D spatial and 2D+T modes. |
| [`shear-torus.html`](shear-torus.html) | R19 | Shear deformation on the flat material sheet. Ring lines twist into helices; geodesic follows q_eff = m − ns. |
| [`torus-slice.html`](torus-slice.html) | 4D | Sweeps a cutting plane through the 3D torus, showing the annular cross-section over time. |
| [`t3-slice.html`](t3-slice.html) | T³ | 3D hyperplane slices of a T³ = T² × S¹ in R⁴. Two tori split and merge as the slice sweeps. Tube-sweep and ring-sweep modes. |
| [`nested-torus.html`](nested-torus.html) | T^d | Recursive nesting of periodic dimensions (1–5 levels). Each level wraps the previous around a new circle, producing concentric boundary tori. Per-level colour, opacity, wireframe/shell, and visibility. |
| [`fusion.html`](fusion.html) | Q95 | Proton-proton fusion: nuclear potential (Coulomb + MaSt strong), fusion rate vs temperature, WKB tunneling, B-field alignment, scenario analysis. |
| [`torus-modes.html`](torus-modes.html) | R21 | Standing-wave eigenmodes on the curved embedded torus. Probability density |f(θ₁)|² rendered as glowing particle clouds inside a translucent shell. Multiple simultaneous modes, presets (electron, R21 trio, harmonics). Adjustable ε, shear. |

## Launch

    cd viz && python3 -m http.server 8765
    open http://localhost:8765/index.html

---

## Building New Visualizers

### Architecture

```
totu-viz.css        Shared dark-theme stylesheet (CSS variables, layout classes)
totu-viz.js         Shared Three.js utilities (ES module)
*.html              Individual visualizers (one per file, no build step)
index.html          Card gallery linking every visualizer
```

### Three.js version

Always **0.163.0**. Use this importmap exactly:

```html
<script type="importmap">
{"imports":{
  "three":"https://cdn.jsdelivr.net/npm/three@0.163.0/build/three.module.js",
  "three/addons/":"https://cdn.jsdelivr.net/npm/three@0.163.0/examples/jsm/"
}}
</script>
```

### HTML skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>My Viz — totu viz</title>
<link rel="stylesheet" href="totu-viz.css">
<style>/* page-specific styles only */</style>
</head>
<body>

<div class="top-bar">
  <h1>My Viz</h1><div class="sep"></div>
  <!-- controls -->
</div>

<div class="view-full" id="view">
  <!-- optional overlays -->
</div>

<script type="importmap">
{"imports":{
  "three":"https://cdn.jsdelivr.net/npm/three@0.163.0/build/three.module.js",
  "three/addons/":"https://cdn.jsdelivr.net/npm/three@0.163.0/examples/jsm/"
}}
</script>
<script type="module">
import {
  THREE, createScene, autoResize, animLoop,
  buildTorusGeom, torusPt, torusPathGeom,
  createPhoton, torusMaterials, PALETTE
} from './totu-viz.js';

const $ = id => document.getElementById(id);

const S = { /* mutable state */ };

const { scene, camera, renderer, controls, clock } = createScene($('view'), {
  camPos: [2.5, 1.8, 3.5],
});
autoResize(renderer, camera, $('view'));

// Build geometry, control handlers, animation loop
</script>
</body>
</html>
```

### totu-viz.css classes

| Class | Purpose |
|-------|---------|
| `.top-bar` | Horizontal control strip (flex, wraps) |
| `.top-bar h1` | Title (14px, muted) |
| `.cg` | Control group: label + slider + `.val` readout |
| `.sep` | Vertical divider |
| `.btn` / `.btn.on` | Button / active state |
| `.tog` | Checkbox toggle wrapper |
| `.view-full` | 3D viewport (fills remaining height) |
| `.info-line` | Bottom-left overlay text |
| `.hide` | `display: none !important` |

CSS variables: `--bg`, `--accent`, `--text`, `--muted`, `--btn-bg`, `--btn-border`, etc.

### totu-viz.js exports

**Scene & rendering:**

| Export | Signature | Notes |
|--------|-----------|-------|
| `THREE` | — | Re-exported Three.js namespace |
| `OrbitControls` | — | Re-exported from three/addons |
| `PALETTE` | `{ bg, surface, path, photon, green, blue, red, purple }` | Hex color constants |
| `createScene` | `(container, opts?) → { scene, camera, renderer, controls, clock }` | Full scene setup. Appends canvas to container. opts: `bg`, `fov`(45), `camPos`([2.5,1.8,3.5]), `damping`, `maxDistance`, `fillLight`(true) |
| `autoResize` | `(renderer, camera, container) → cleanup` | Window resize handler. Call once after createScene. |
| `animLoop` | `(tick, { renderer, scene, camera, controls }) → stop` | rAF loop: controls.update → tick → render |

**Torus geometry:**

| Export | Signature | Notes |
|--------|-----------|-------|
| `buildTorusGeom` | `(R, a, segU?, segV?) → BufferGeometry` | R = major, a = tube radius |
| `torusPt` | `(t, R, a, p, q) → Vector3` | Point on (p,q) geodesic at parameter t |
| `torusPathGeom` | `(R, a, p, q, opts?) → TubeGeometry` | Tube along geodesic. opts: `segments`, `periods`, `tubeR`, `closed` |
| `torusMaterials` | `(opts?) → { surface, wire }` | Translucent Phong + wireframe. opts: `color`, `opacity`, `wireOpacity` |
| `createPhoton` | `(opts?) → { mesh, glow }` | Glowing sphere + point light. opts: `r`, `color` |

**Coordinate convention:** torus in XZ plane, axis Y.
`x = (R + a cos θ) cos φ`, `y = a sin θ`, `z = (R + a cos θ) sin φ`

### Control HTML patterns

```html
<!-- Slider -->
<div class="cg">
  <label>a/R</label>
  <input type="range" id="sl-ar" min="0.1" max="3.0" step="0.01" value="0.34">
  <span class="val" id="v-ar">0.34</span>
</div>

<!-- Preset buttons (toggle .on, sync slider from dataset) -->
<div class="cg" style="gap:3px">
  <button class="btn on" data-ar="0.34">R8</button>
  <button class="btn" data-ar="1.00">Horn</button>
</div>

<!-- Toggle -->
<div class="tog"><label><input type="checkbox" id="t-surf" checked> Surface</label></div>

<!-- Play/Pause (toggle ▶ Play / ⏸ Pause, toggle .on) -->
<button class="btn on" id="btn-play">▶ Play</button>
```

**Info panel** (centered bottom overlay):

```html
<div id="info-panel">
  <div><span class="lbl">a/R = </span><span class="v" id="i-ar">0.34</span></div>
</div>
```

```css
#info-panel {
  position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%);
  background: rgba(10,10,18,0.9); padding: 8px 18px; border-radius: 8px;
  backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.06);
  font-size: 11px; display: flex; gap: 18px; white-space: nowrap;
  pointer-events: none; z-index: 10;
}
```

### Checklist

1. `<title>` and `<h1>` match.
2. importmap uses Three.js 0.163.0.
3. `autoResize` called after `createScene`.
4. No console errors.
5. Card added to `index.html`.
6. Entry added to tools table above.
