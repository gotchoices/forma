# Nested Torus — Spec

Visualize how periodic dimensions build on each other: a circle becomes a
torus, a torus becomes a torus-of-a-torus, and so on.  Each level sweeps the
previous structure around a new ring, producing a recursively nested surface
in 3D.

---

## Progressive sweep construction

The visualizer builds its geometry step by step.  Each level sweeps the
previous structure around a new ring whose axis is rotated 90° from the last.

The key constraint: **each level's ring passes through the previous level's
center.**  This means the new level's ring center is offset from the old
center, and the previous level's boundary tori sit naturally at the
cross-section position — no separate highlight copy is needed.

### Step by step

**Level 1 — Circle.**
A circle of radius r₁.  This is the innermost structure: one periodic
dimension.  Drawn as a thin tube so it is visible.

**Level 2 — Torus.**
Sweep the level-1 circle around a Y-axis ring of radius r₂.  Ring center
is at the origin.  The level-1 circle sits at (r₂, 0, 0) — the tube
center at φ₂ = 0 — and remains visible as a highlighted ring there.

  - L2 center: **(0, 0, 0)**
  - L1 circle at: **(r₂, 0, 0)** — the φ₂ = 0 cross-section

**Level 3 — Torus of torus.**
Sweep the level-2 torus around a Z-axis ring of radius r₃.  The ring
must pass through the L2 center (origin) AND thread through L2's hole
(which is along Y).  A Z-axis ring has tangent Y at φ = 0, so it
threads the Y-hole correctly.  The ring center is displaced in −X:

  - L3 center: **(−r₃, 0, 0)**
  - At φ₃ = 0: tube center = (−r₃ + r₃, 0, 0) = **(0, 0, 0)** = L2 center ✓
  - Tangent at φ₃ = 0: **(0, r₃, 0) = +Y** → through L2's Y-hole ✓

The L2 torus at origin sits exactly at the φ₃ = 0 cross-section of L3.
The L3 boundary envelopes the L2 torus there — no manufactured replica
needed.  The L2 torus itself IS the cross-section ghost.

In 3D, the L3 boundary consists of TWO standard tori (outer tube
r₂ + r₁, inner tube r₂ − r₁), both Z-axis with major radius r₃,
centered at (−r₃, 0, 0).

**Level 4 — and beyond.**
Each level adds another sweep.  The ring center is always offset in −X:

  - L4 center: L3 center − (r₄, 0, 0) = **(−r₃ − r₄, 0, 0)**
  - Tangent at φ₄ = 0: Z → through L3's Z-hole ✓

  - L5 center: L4 center − (r₅, 0, 0) = **(−r₃ − r₄ − r₅, 0, 0)**
  - Tangent at φ₅ = 0: Y → through L4's Y-hole ✓

The boundary tori double at each step (2^(k−2) tori at level k ≥ 2).
The previous level's tori always serve as the visible cross-section.

### Center-offset formula

The center of level k's ring, C_k:

    C_1 = (not applicable — L1 is a circle, not a ring)
    C_2 = (0, 0, 0)
    C_k = C_{k−1} − (r_k, 0, 0)    (k ≥ 3)

All centers lie along the −X axis:

| Level k | Axis  | Ring plane | Hole axis | C_k                          |
|---------|-------|------------|-----------|-------------------------------|
| 2       | Y     | XZ         | Y         | (0, 0, 0)                     |
| 3       | Z     | XY         | Z         | (−r₃, 0, 0)                   |
| 4       | Y     | XZ         | Y         | (−r₃ − r₄, 0, 0)              |
| 5       | Z     | XY         | Z         | (−r₃ − r₄ − r₅, 0, 0)         |

At φ_k = 0, the tube center is at C_k + (r_k, 0, 0) = C_{k−1}.  The
tangent there is:
- Y-axis ring (even k): tangent = Z → threads the Z-hole of level k−1
- Z-axis ring (odd k):  tangent = Y → threads the Y-hole of level k−1

This means each level's tube passes through the previous level's donut
hole, not just through its center.

### Axis rotation

Even levels (2, 4) use Y-axis (ring in XZ, hole along Y).
Odd levels ≥ 3 (3, 5) use Z-axis (ring in XY, hole along Z).

### Boundary formula

At level k (k ≥ 2), the boundary consists of 2^(k−2) standard tori.  All
share the same ring axis (from the table above) and major radius r_k,
**centered at C_k** (NOT at origin).  Tube radii are all sign combinations
of r_{k−1} ± r_{k−2} ± … ± r₁ (r_{k−1} always positive, remaining
signs vary).  Skip any combination where tube radius ≤ 0.

### Cross-section highlighting

For k ≥ 3, no separate highlight mesh is needed.  The level-(k−1)
boundary tori, already rendered at C_{k−1}, sit at the φ_k = 0
cross-section of level k.  They ARE the highlight.

When depth = d, levels 1 through d−1 should switch to wireframe
rendering (they are now "ghosts" showing cross-sections of the
outermost level's sweep path).  Only level d renders as a solid shell.

The one exception is the **level 2 highlight for level 1**: the L1 circle
at (r₂, 0, 0) is still needed as a separate object since L1 is a circle,
not a torus.

### Radius convention

r₀ = 1 is an abstract reference unit (not rendered).  Each level has a ratio:

    r₁ = ratio₁ × r₀
    r_k = ratio_k × r_{k−1}    (k ≥ 2)

With ratio > 1, each successive radius grows.  For non-self-intersection at
all levels, ratio ≳ φ ≈ 1.618 (golden ratio), but self-intersecting
configurations are valid and interesting to explore.

### Opacity principle

Inner levels are more opaque; outer levels are more transparent.  Each
successive level should be visibly lighter so you can see the layers inside.
Default: level 1 at 0.8, each subsequent level ×0.5 (so 0.4, 0.2, 0.1, …).
The user can override per level.

## Per-level controls

Each active level *k* (1 ≤ k ≤ depth) has its own control row:

| Control | Applies to | Range | Default | Notes |
|---------|-----------|-------|---------|-------|
| Ratio r_k/r_{k−1} | all | slider, 0.1–10 | 2.5 | Values > 1 grow outward, < 1 shrink inward. Cascades to deeper levels. |
| Opacity α_k | all | slider, 0–1 | L1: 0.8, L2: 0.4, L3: 0.2, L4: 0.1, L5: 0.05 | Outer levels more transparent (see §Opacity principle) |
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

### Level 1 — circle

`TubeGeometry` circle of radius r₁.  Position: centered at the level-2
cross-section center (C₂ + (r₂, 0, 0) = (r₂, 0, 0)), lying in the XY
plane.  If depth = 1, center at origin in XZ plane instead.

### Level k ≥ 2 — boundary tori

Each boundary torus uses the level-k axis (Y for even k, X for odd k ≥ 3),
**centered at C_k** (see center-offset formula).

**Y-axis torus** (levels 2, 4, …) — ring in XZ plane, centered at C_k:

    x = C_k.x + (R + a cos θ) cos φ
    y = C_k.y + a sin θ
    z = C_k.z + (R + a cos θ) sin φ

**Z-axis torus** (levels 3, 5, …) — ring in XY plane, centered at C_k:

    x = C_k.x + (R + a cos θ) cos φ
    y = C_k.y + (R + a cos θ) sin φ
    z = C_k.z + a sin θ

where R = r_k (major radius), a = tube radius from the boundary formula,
θ = tube angle, φ = ring angle.

Verify: at φ = 0 on level k, the tube center is at C_k + offset_k = C_{k−1}.
The tube cross-section is a circle of radius `a` centered at C_{k−1}.
For the outermost boundary (a = r_{k−1} + r_{k−2} + … + r₁), this circle
envelopes the entire level-(k−1) structure.

Do NOT use `buildTorusGeom` for all levels — it only builds Y-axis tori.
Use `buildZTorusGeom` for odd levels (ring in XY).  Translate by setting
the group position to C_k.

Segment counts: scale with tube-to-major ratio.  Minimum 12 tube segments,
minimum 32 ring segments.

### Why no separate highlight geometry for k ≥ 3

The level-(k−1) boundary tori are already positioned at C_{k−1}.  At
φ_k = 0, the level-k tube center passes through C_{k−1}.  So the
level-(k−1) tori naturally appear at the cross-section — they ARE the
highlighted profile.

When depth increases, inner levels should switch to wireframe so they
read as "ghost" profiles.  This is controlled by the per-level render
mode (shell/wire toggle) and opacity.

The only separate highlight is the L1 circle at L2's cross-section
position.

## Camera

- Auto-fit: compute bounding box of all visible geometry (which now
  extends in different directions at each level).  Camera distance set
  to encompass the bounding box.
- OrbitControls for manual navigation.
- maxDistance large enough for depth-5 structures.

## Info panel

Bottom center:
- Depth d
- r₁ through r_d values
- C_d center coordinates
- Total torus count

## Future features

- **Wrap/unwrap animation:** when depth increases/decreases, animate the sweep (partial toroidal angle 0 → 2π) so you watch it wrap/unwrap.
- **Photon animation:** a glowing particle traveling through the nested space.
- **Auto-rotate:** slow turntable spin.
