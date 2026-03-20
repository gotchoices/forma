# Nested Torus — Spec

Visualize how periodic dimensions build on each other: a circle becomes a torus, a torus becomes a torus-of-a-torus, and so on. Each level wraps the previous structure around a new circle, producing a recursively nested surface in 3D.

## Levels

The visualizer supports 1 to 5 nesting levels, selectable at runtime. Adding a level does not destroy previous geometry — it wraps it.

| Level | Internal dim | What you see |
|-------|-------------|--------------|
| 1 | L₁ | A flat circle (line) of radius r₁ |
| 2 | L₁ × L₂ | Standard torus — major radius r₁, tube radius r₂ |
| 3 | L₁ × L₂ × L₃ | Two tori (outer/inner walls of a hollow tube). Major radius r₁, tubes r₂ ± r₃ |
| 4 | … | Four boundary tori. Major r₁, tubes r₂ ± r₃ ± r₄ |
| 5 | … | Eight boundary tori. Major r₁, tubes r₂ ± r₃ ± r₄ ± r₅ |

### Sweep rule

At each new level *k*, the tube of the previous torus gains internal structure by becoming a torus itself. The tube-torus has major radius r_{k−1} and tube radius r_k.

### Boundary formula

At depth d, each level k (k ≥ 2) renders 2^(k−2) standard tori. All share major radius r₁. Tube radii are all combinations of r₂ ± r₃ ± … ± r_k (r₂ always positive, remaining signs vary). Combinations with tube radius ≤ 0 are skipped.

### Radius convention

r₁ is the outermost (largest). Each deeper level is smaller: r_k = ratio_k × r_{k−1}. With default ratio = 0.3, a depth-2 torus has a/R ≈ 0.3 — a nice ring torus.

### Rendering by level

All levels 1 through d are rendered simultaneously as separate groups, each with its own color, opacity, render mode, and visibility. Inner levels are visible through translucent outer levels.

## Per-level controls

Each active level *k* (1 ≤ k ≤ depth) has its own control row that appears when the level is enabled:

| Control | Applies to | Range | Default | Notes |
|---------|-----------|-------|---------|-------|
| Ratio r_k/r_{k−1} | k ≥ 2 | slider, 0.05–0.95 | 0.3 | Changing a ratio cascades to all deeper levels. |
| Opacity α_k | all | slider, 0–1 | L1: 0.8, rest: 0.3 | Surface translucency |
| Render mode | k ≥ 2 | shell / wire toggle | shell | Wire makes it easy to see inside |
| Visible | all | toggle | on | Hides this level only. Children remain visible. |

Radius computation: `r₁` is set by the global slider. For k > 1, `r_k = ratio_k × r_{k−1}`. Changing r₁ or any ratio rescales all downstream levels automatically.

## Color palette

A persistent row of 5 swatches, always visible in the control bar. Click any swatch to open a color picker.

- Defaults: cyan, orange, green, purple, red.
- Inactive swatches (beyond current depth) are dimmed.

## Global controls

| Control | Range | Default | Notes |
|---------|-------|---------|-------|
| Depth | 1–5 (buttons) | 1 | Number of active nesting levels |
| r₁ | slider, 0.2–3.0 | 1.0 | Base radius — all others derive via ratios |
| Auto-fit | toggle | on | Camera zooms to fit when depth or radii change |
| Reset | button | — | Clears localStorage, restores all defaults |

## Persistence

All configuration saved to `localStorage` key `nested-torus`. Restored on page load. Reset button clears it.

## Geometry

Level 1: `THREE.Line` circle of radius r₁ in the XZ plane.

Level k ≥ 2: standard torus meshes via `buildTorusGeom(r₁, tubeR)` for each tube radius in the boundary set. Segment counts scale with tube radius (more segments for bigger tubes).

## Camera

- Auto-fit: bounding radius = r₁ + max(tube radii). Camera distance set to fit.
- OrbitControls for manual navigation.

## Info panel

Bottom center:
- Depth d
- Bounding radius
- r₁ through r_d values

## Future features

- **Wrap/unwrap animation:** when depth increases/decreases, animate the sweep (partial toroidal angle 0 → 2π) so you watch it wrap/unwrap. Code should be structured to support this.
- **Photon animation:** a glowing particle traveling through the nested space (first planned addition after wrap/unwrap).
- **Auto-rotate:** slow turntable spin.
