# Torus Studio

A unified torus explorer that combines 3D shape morphing, arbitrary geodesic
winding, lattice shear, and an optional 2D flat-sheet view into a single tool.
Supersedes `torus-explorer.html`, `dual-torus.html`, and the shear overlay from
`shear-torus.html`.

---

## What this tool shows

A torus (donut shape) is the central geometric object in the WvM/MaSt electron
model.  The electron is modeled as a photon confined to a closed path — a
(1,2) torus knot — on a compact two-dimensional surface.  This tool lets you
explore that surface and the paths on it across three interrelated views:

1. **3D torus** — the embedded surface in three-dimensional space, with
   geodesic paths, a photon tracing the path, and optional overlay geometry
   (lattice lines, rotation horizon, symmetry axis).

2. **2D flat sheet** (optional side panel) — the same surface unrolled into a
   flat rectangle with periodic edges, showing the path as a straight diagonal
   line, and the effect of shear as a parallelogram grid.

3. **Info bar** — live numerical readouts of the physical quantities that come
   from the current shape: charge proxy, path length, volume ratio, lattice
   angle, and more.

---

## Physical background

### The torus shape: a/R

A torus is characterized by two radii:

- **R** — the major radius: distance from the center of the tube to the center
  of the whole ring.
- **a** — the minor radius: the radius of the tube itself.

Their ratio **a/R** controls the overall shape:

| a/R < 1 | a/R = 1 | a/R > 1 |
|---------|---------|---------|
| **Ring torus** — the tube doesn't reach the center | **Horn torus** — the inner equator touches itself | **Spindle torus** — the tube self-intersects at the center |

The WvM electron model places the electron near a/R ≈ 6.60, well into spindle
territory.  Several special values are available as presets:

| Preset | a/R | Meaning |
|--------|-----|---------|
| Ring 0.5 | 0.50 | A classic thin-tube torus |
| Horn | 1.00 | The singular boundary shape |
| Horizon | 5.28 | Outer equator = λ_C / (2π), the Compton rotation radius |
| q = e | 6.60 | Aspect ratio that yields charge ≈ e under the WvM energy balance |
| WvM sphere | 7.26 | The sphere-equivalent: V_torus = V_sphere at the Compton scale |

### Winding numbers (p, q)

A geodesic on a torus is specified by two integers: how many times the path
winds around the **tube** (minor circle, angle θ) and around the **ring** (major
circle, angle φ).  The electron's path is (p=1, q=2): once around the tube,
twice around the ring.

Any integer pair (p, q) with p,q ≥ 1 defines a valid closed path.  Higher
windings mean shorter wavelengths, and by the resonance condition (path length
= one Compton wavelength), higher mass.  The winding-number spinners let you
explore any mode, not just the electron's (1,2).

**Charge** depends on p: only p = 1 modes carry a net electric charge.
**Spin** depends on p: odd p → fermion (spin ½); even p → boson.

### Shear (s)

The flat material sheet is normally a rectangle — two periodic directions at
right angles (θ and φ).  Shear slightly tilts this lattice: the rectangle
becomes a parallelogram.

Physically, shear means: as you complete one full circuit around the **tube**
(θ: 0 → 2π), your position in the **ring** direction (φ) shifts by δ = s · 2π.
The tube lines in the flat picture lean; the ring lines stay horizontal.

```
Unsheared (s = 0):       Sheared (s > 0):
+----------+              +----------+
|          |             / ←δ→     /
|          |            /          /
+----------+           +----------+
```

Shear breaks a field-symmetry that otherwise cancels the net E-flux (charge)
to zero.  Any nonzero shear produces a nonzero charge.  The charge formula
involves `sin(2πs)`, so a tiny shear gives a tiny charge.  The fine structure
constant α ≈ 1/137 corresponds to a shear of about s ≈ 0.157 (an α preset is
provided).

The effective ring winding seen in 3D becomes qEff = q − p·s — the path
advances slightly less around the ring per tube circuit when the lattice tilts.
For the electron: qEff = 2 − s.

---

## Layout

The page has three zones:

```
┌─────────────────────────────────────────────────────────────────┐
│  Top bar: all controls                                          │
├──────────────────────────────┬──────────────────────────────────┤
│                              │                                  │
│   3D view (always)           │   2D flat sheet (toggle)        │
│                              │                                  │
├──────────────────────────────┴──────────────────────────────────┤
│  Info bar: live readouts                                        │
└─────────────────────────────────────────────────────────────────┘
```

When the 2D pane is hidden, the 3D view fills the full width.  When it is
shown, the window splits 50/50.  Both views share the same animated photon
and respond to the same controls.

---

## Controls

### Shape

**a/R slider** (range 0.05–12, step 0.01) — sets the tube/ring ratio.  The
torus rebuilds immediately.  The auto-fit option keeps it centered in view as
the shape changes.

**Presets** — five buttons that jump to the physically significant values above.
Clicking a preset highlights it; dragging the slider clears the highlight.

**Opacity slider** — controls the transparency of the torus surface (0 =
invisible, 1 = fully opaque).  Useful for seeing the geodesic inside the
surface.

### Winding

**p spinner** and **q spinner** — integer inputs with ▲/▼ arrow buttons
(range 1–12).  These set the tube and ring winding numbers respectively.
Changing them rebuilds the geodesic path instantly.  Direct numeric entry is
also accepted.  There are no preset buttons for windings — any integer pair
works.

### Shear

**s slider** (range 0–0.50, step 0.001) — sets the fractional lattice shear.
At s = 0 the lattice is orthogonal and the ring and tube lines are independent
circles.  At s > 0 the tube lines lean and the path tilts.

**Shear presets** — four buttons: 0 (no shear), α (0.157, the fine-structure
value), ¼, and ½.

### Animation

**▶ Play / ⏸ Pause** — starts and stops the photon animation.

**Speed slider** (0.1–4×) — multiplies the animation rate.

### Toggles

These show or hide individual elements in the 3D view:

| Toggle | What it shows |
|--------|--------------|
| Surface | The translucent torus body |
| Wireframe | A low-opacity mesh overlay on the surface |
| Geodesic | The colored tube tracing the (p,q) path |
| Photon | The animated glowing sphere on the path |
| Ring lines | Toroidal lines (constant θ, φ varies) — red, flat circles |
| Tube lines | Poloidal lines (constant φ_flat, θ varies) — blue, lean when s > 0 |
| Horizon sphere | A faint wireframe sphere at r = λ_C/2 = 2πR, the Compton rotation radius |
| Axis | The Y symmetry axis |
| Auto-fit | Rescale the world so the torus always fits the viewport |
| 2D flat | Toggle the flat-sheet side panel |

Ring and tube lines are the shear visualization.  They default to **off** when
s = 0 (redundant with the wireframe) and automatically become visible when
s is changed from zero.

---

## 3D view details

The torus sits in the XZ plane with axis Y.  A point on the surface is:

    x = (R + a cos θ) cos φ
    y = a sin θ
    z = (R + a cos θ) sin φ

The geodesic path with shear traces:

    θ(t) = p · t
    φ(t) = (q − s·p) · t     ← ring winding reduced by shear

The photon follows this path continuously; its animation period is one full
q-circuit (t: 0 → 2π·q / speed).

**Ring lines** (red): each is a standard circle at a fixed θ — a horizontal
slice through the surface.  These are not affected by shear.

**Tube lines** (blue): each starts at a fixed φ_flat, but as θ increases the
embedding shifts in the ring direction: φ_emb = φ_flat − s·θ.  At s = 0 these
are the standard meridional circles.  At s > 0 they spiral, leaning in the
−φ direction — exactly the tilted vertical edges of the parallelogram in the
flat picture.

The **rotation horizon sphere** is a faint green wireframe sphere of radius
λ_C/2 = 2πR (in model units with R=1, radius = 2π ≈ 6.28).  It marks the
boundary beyond which the outer equator of a torus is moving at the speed of
light.  The q = e preset sits just inside this sphere.

---

## 2D flat-sheet view

The 2D panel shows the flat torus T² as a rectangle (or parallelogram when
sheared) with its two periodic boundary directions labeled.

**Axes:**
- Horizontal → φ direction, labeled Lφ (ring circumference)
- Vertical → θ direction, labeled Lθ (tube circumference)
- The rectangle is scaled so the height-to-width ratio equals a/R

**Grid:**
- Horizontal grid lines: ring lines (constant θ) — flat, unaffected by shear
- Vertical grid lines: tube lines (constant φ_flat) — lean leftward when s > 0
- When s > 0, the grid becomes a parallelogram; the lean angle equals the
  lattice angle deviation from 90°

**Path:** the (p,q) geodesic appears as a straight orange diagonal crossing
the flat rectangle.  It wraps at the edges.  Slope = p·Lθ / (q−s·p)·Lφ.
For the (1,2) electron: two ring-crossings per tube-crossing.

**Photon:** a yellow dot moves along the diagonal, synchronized with the 3D
photon.

**Identification arrows:** arrows on each edge show which edges are glued
together, using red for the ring direction (Lφ) and blue for the tube direction
(Lθ).

---

## Info bar

A single strip at the bottom shows live values:

| Field | Description |
|-------|-------------|
| a/R | Current tube/ring ratio |
| Type | RING / HORN / SPINDLE badge |
| Knot (p,q) | Current winding numbers |
| Outer edge | The outermost circle of the torus in units of λ_C: (R+a)/(2π·R) |
| Vtor/Vsph | Ratio of torus volume to the volume of a sphere with r = λ_C/2 |
| q/e | Charge proxy from the WvM energy balance: 0.910 / √(Vtor/Vsph) |
| Path | Geodesic length in units of λ_C: √(q² + (p·a/R)²) |
| Slope | Ratio p·(a/R) / (q − s·p) — the path angle in the flat sheet |
| s | Fractional shear |
| δ/a | Shift per tube circuit: 2π·s |
| Lattice ∠ | Deviation from 90°: 90° − arctan(s · a/R) |
| qEff | Effective ring winding: q − p·s |

---

## Relationship to other visualizers

This tool replaces:

- **torus-explorer.html** — subsumed (all features present plus more)
- **dual-torus.html** — subsumed (2D pane is optional here)

It complements but does not replace:

- **shear-torus.html** — that tool remains useful for isolated study of the
  shear effect; this tool includes shear as one feature among many
- **torus-modes.html** — eigenmode probability densities (separate physics)
- **torus-slice.html**, **t3-slice.html** — slice geometry (separate use case)

---

## Implementation notes (for the developer)

- Single HTML file, shared `totu-viz.css` + `totu-viz.js`, Three.js 0.163.0.
- Use `animLoop()` from `totu-viz.js` (not an inline rAF loop).
- Use `torusMaterials()` from `totu-viz.js` for the surface and wire meshes.
- The 2D canvas lives in the right-hand flex pane; its resize handler fires
  on the same `window.resize` event as `autoResize`.
- The shear orientation is **tube-tilt**: tube lines use `φ_emb = φ₀ − s·θ`;
  ring lines use `θ = θ₀` (not the other way around, as in the current
  `shear-torus.html`).
- Geodesic: `θ = p·t`, `φ = (q − s·p)·t`.  Photon period: `2π` in t, which
  corresponds to one full tube circuit (and `q − s·p` ring circuits).
- The p and q spinners use `<input type="number">` with `appearance:textfield`
  and explicit ▼/▲ buttons styled to match the dark theme.
- Ring/tube line groups (THREE.Group) are rebuilt only when a/R or s changes.
- Auto-fit scales the world group: `gs = FIT / (R + a)`.  Photon sphere and
  path tube radius scale inversely so they stay visually constant size.
- Torus segment resolution: 96×192 for the surface (smooth at all a/R values),
  48×96 for the wireframe overlay.
