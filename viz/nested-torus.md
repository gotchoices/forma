# Nested Torus — Spec

Visualize how periodic dimensions build on each other: a circle becomes a torus, a torus becomes a torus-of-a-torus, and so on. Each level wraps the previous structure around a new circle, producing a recursively nested surface in 3D.

This visualizer is broken--not yet working.

## Levels

The visualizer supports 1 to 4 nesting levels, selectable at runtime. Adding a level wraps the existing structure — it does not destroy previous geometry.

| Level | Internal dim | What you see |
|-------|-------------|--------------|
| 1 | L₁ | Circle of radius r₁ |
| 2 | L₁ × L₂ | Standard torus — tube r₁, major r₂ |
| 3 | L₁ × L₂ × L₃ | Major r₃, tube boundaries at r₂ ± r₁ (2 tori, hollow tube) |
| 4 | … | Major r₄, tubes r₃ ± r₂ ± r₁ (4 boundary tori) |

### Sweep rule

At each new level *k*, the ring (major circle) of the previous torus becomes part of the tube cross-section of the new torus. The new torus sweeps the entire previous structure around a new circle of radius r_k, with the rotation axis shifted 90° from the previous sweep.

Concretely: the level-k torus has major radius r_k. Its tube contains the level-(k−1) structure as a cross-section.

Example:
- Ring for level 1 (circle) is in xz axis
- Ring for level 2 is in xy axis
- Ring for level 3 is in yz axis
- Ring for level 4 is in xz axis

### Boundary formula

At depth d, level k (k ≥ 2) renders 2^(k−2) standard tori. Each has major radius r_k. Tube radii are all combinations of r_{k−1} ± r_{k−2} ± … ± r₁ (r_{k−1} always positive, remaining signs vary). Combinations yielding tube ≤ 0 are skipped.

### Radius convention

r₀ = 1 is an abstract reference unit (not rendered). Each level has a ratio factor:

    r₁ = ratio₁ × r₀
    r_k = ratio_k × r_{k−1}    (k ≥ 2)

With ratio > 1, each successive radius grows — the level-k torus is a bigger ring than level-(k−1). With ratio < 1, the structure shrinks inward. For non-self-intersection at all levels, ratio ≳ φ ≈ 1.618 (golden ratio), but self-intersecting configurations are valid and interesting to explore.

### Rendering by level

All levels 1 through d are rendered simultaneously as separate groups, each with its own color, opacity, render mode, and visibility. With ratio > 1, inner levels appear as smaller rings nested concentrically. With translucency you can see all layers.

## Per-level controls

Each active level *k* (1 ≤ k ≤ depth) has its own control row:

| Control | Applies to | Range | Default | Notes |
|---------|-----------|-------|---------|-------|
| Ratio r_k/r_{k−1} | all | slider, 0.1–10 | 2.5 | Values > 1 grow outward, < 1 shrink inward. Cascades to deeper levels. |
| Opacity α_k | all | slider, 0–1 | L1: 0.8, rest: 0.25 | Surface translucency |
| Render mode | k ≥ 2 | shell / wire toggle | shell | Wire makes it easy to see inside |
| Visible | all | toggle | on | Hides this level only. Other levels unaffected. |

Radius computation: `r₀ = 1` (implicit). `r₁ = ratio₁ × r₀`. For k > 1, `r_k = ratio_k × r_{k−1}`. Changing any ratio rescales all downstream levels.

## Color palette

A persistent row of 5 swatches, always visible in the control bar. Click any swatch to open a color picker.

- Defaults: cyan, orange, green, purple, red.
- Inactive swatches (beyond current depth) are dimmed.

## Global controls

| Control | Range | Default | Notes |
|---------|-------|---------|-------|
| Depth | 1–5 (buttons) | 2 | Number of active nesting levels |
| Auto-fit | toggle | on | Camera zooms to fit when depth or radii change |
| Reset | button | — | Clears localStorage, restores all defaults |

## Persistence

All configuration saved to `localStorage` key `nested-torus`. Restored on page load. Reset button clears it.

## Geometry

Level 1: `TubeGeometry` circle of radius r₁ in the XZ plane (thin tube so it's visible).

Level k ≥ 2: standard torus meshes via `buildTorusGeom(r_k, tubeR)` for each tube radius in the boundary set. Each level k has its own major radius r_k. Segment counts scale with tube-to-major ratio.

## Camera

- Auto-fit: bounding radius = r_d + max(tube radii at depth d), where d is current depth. Camera distance set to fit.
- OrbitControls for manual navigation.
- maxDistance large enough for depth-5 structures.

## Info panel

Bottom center:
- Depth d
- r₁ through r_d values
- Bounding radius
- Total torus count

## Future features

- **Wrap/unwrap animation:** when depth increases/decreases, animate the sweep (partial toroidal angle 0 → 2π) so you watch it wrap/unwrap.
- **Photon animation:** a glowing particle traveling through the nested space.
- **Auto-rotate:** slow turntable spin.
