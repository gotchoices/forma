# Tube Lab — Spec

Interactive workbench for **smooth N-fold-symmetric tube cross-sections** swept
into a corrugated torus with adjustable twist. Generalizes the discrete-arc
clover of [proton-lab](proton-lab.html) to any lobe count and any valley
depth, using a C^∞ harmonic curve so curvature is continuous everywhere. The
family contains — as exact members — the circle, rounded N-gons, the
three-lobe quark clover, and a **true ellipse**.

Single HTML file, no build step. Uses the standard `totu-viz.js` /
`totu-viz.css` infrastructure (Three.js 0.163.0).

Related references:
- [projects/ma-domain/work/electron-tube.md](../projects/ma-domain/work/electron-tube.md)
  — bilobe (N=2) tube with twist τ=2 as the natural T(1,2) electron host.
- [projects/sheet-proton/work/clover-quarks.md](../projects/sheet-proton/work/clover-quarks.md)
  — three-lobe arc clover; this lab supplies a smooth alternative whose
  Q = (1/2π) ∮ κ ds bookkeeping carries over.

---

## 1. Physics model

### 1.1 Cross-section profile (harmonic form)

The cross-section is a closed plane curve, written in complex coordinates
z = x + i·y and parameterised by a free parameter t:

```
z(t) = R_c · e^{i t} · w(t)
w(t) = [ 1 + a₁·cos(Nt) + a₂·cos(2Nt) ]  +  i·[ b₁·sin(Nt) + b₂·sin(2Nt) ]
```

with five independent shape parameters:

| Parameter | Symbol | Role |
|---|---|---|
| Lobe count | `N` ∈ ℤ, 2 ≤ N ≤ 8 | Number of N-fold symmetric features around the cross-section |
| Fundamental amplitude | `a₁` ∈ [0, 1.5] | Sets the gross peak-to-trough swing |
| First-harmonic split | `b₁` ∈ [−0.9, 0.9] | Asymmetry of the first harmonic; b₁ = −a₁ at N=2 gives a true ellipse |
| Second harmonic | `a₂` ∈ [−0.4, 0.4] | Sharpens or flattens valleys; introduces concave saddles when large |
| Second-harmonic split | `b₂` ∈ [−0.4, 0.4] | Asymmetry of the second harmonic (fine-tuning; usually 0) |
| Mean radius | `R_c` | Sets the absolute size of the cross-section |

**The polar slice.** With `b₁ = b₂ = 0` the shape function w(t) is real,
z = w(t)·R_c·e^{it}, and the parameter t coincides with the geometric polar
angle φ. The curve reduces to the familiar polar form
`r(φ) = R_c·[1 + a₁cos(Nφ) + a₂cos(2Nφ)]`. This slice covers the circle,
rounded N-gons, and the quark clover — leave the splits at 0 for those.

**The split parameters** b₁, b₂ let the inner/outer harmonic partners differ
(see [tube-function.md §2.3](../projects/ma-domain/work/tube-function.md)).
This is the freedom the polar form lacks: at N=2, a₂=b₂=0, **b₁ = −a₁**
produces an *exact ellipse* with semi-axes R_c(1±a₁) and foci separation
4·R_c·√a₁.

The named knobs *peak prominence* p and *valley depth* v are measured at the
symmetric extrema (which are split-independent — sin(Nt) vanishes there):

- **Peak** at t = 0: r = R_c·(1 + a₁ + a₂) ⟹ peak − R_c = R_c·(a₁ + a₂)
- **Trough** at t = π/N: r = R_c·(1 − a₁ + a₂) ⟹ R_c − trough = R_c·(a₁ − a₂)

so a₁ = (p + v)/2, a₂ = (p − v)/2. For larger amplitudes additional extrema
appear off-axis; the readout shows numerical `r_min`, `r_max`, `κ_min`,
`κ_max` so the true bounds are always visible.

### 1.2 Curvature

The signed curvature of the parametric curve z(t) is

```
κ(t) = Im( conj(z'(t)) · z''(t) ) / |z'(t)|³
```

with z′, z″ the first and second t-derivatives. Since z = R_c·e^{it}·w(t)
and w is a finite sum of sin/cos, z′ and z″ are closed-form and curvature is
computed analytically with no discretisation artefacts. (In the polar slice
b = 0 this reduces to the familiar κ = (r² + 2r′² − r·r″)/(r² + r′²)^{3/2}.)
The 2D preview and 3D surface are coloured by κ via a warm-to-cool ramp:

- κ > 0 → warm (red) — convex, lobe-like
- κ ≈ 0 → neutral grey
- κ < 0 → cool (blue) — concave, saddle-like

The colour scale auto-normalises against max |κ| on the profile.

### 1.3 Degenerate cases (presets)

| Case | Parameters | Geometry |
|---|---|---|
| Circle | a₁ = a₂ = b₁ = b₂ = 0 | Mean radius R_c |
| True ellipse | N = 2, b₁ = −a₁, a₂ = b₂ = 0 | Exact ellipse, semi-axes R_c(1±a₁), all convex |
| Rounded N-gon | small a₁, others ≈ 0 | All-convex N-lobed shape (triangle/square/pentagon/hexagon as N varies) |
| Smooth clover | N = 3, a₁ ≈ 0.43, others 0, R_c ≈ 1.4 | Single-harmonic three-lobe with concave saddles. Matches the arc-clover's peak 2.0 / trough 0.8 at the symmetry points. |
| Quark clover | N = 3, a₁ ≈ 0.707, b = 0 | Polar-slice three-lobe with A_lobe = 4π/3 (Q_lobe = +2/3). |
| Quark clover (fat lobe) | N = 3, a₁ ≈ 0.294, b₁ = 0.2 | Same A_lobe = 4π/3 charge, reached with much less radial swing; sharper valley. See [tube-function.md §5.2](../projects/ma-domain/work/tube-function.md). |
| Deep clover | N = 3, a₁ ≈ 0.85, b = 0 | Sharp narrow valleys, large lobes |

### 1.4 Surface embedding (corrugated torus)

Same construction as proton-lab. Sample the cross-section z(t), rotate by
α = τ·θ in the cross-section plane, then place at the ring at angle θ:

```
samp        = z(t)
(Pxr, Pyr)  = R_α · (samp.x, samp.y)        with α = τ · θ
r⃗(θ, φ)   = R_ring(θ) + Pxr · N̂(θ) + Pyr · B̂
R_ring(θ)   = R_major · (cos θ, sin θ, 0)
N̂(θ)       = (cos θ, sin θ, 0)              (outward radial)
B̂          = (0, 0, 1)                      (vertical)
```

**Closure condition.** The surface meets itself at θ = 2π iff the rotation
R_{2π·τ} maps the profile back to itself. With N-fold symmetry, that
requires `τ · N ∈ ℤ` (i.e., τ is a multiple of 1/N). The lab does **not**
enforce this — the slider is continuous, allowing the user to see the open
spiral surface that results from a non-closing τ. A "snap" button rounds
τ to the nearest closing value, and the `Closure` readout flags whether
the current τ closes.

**Notable τ values:**
- N = 2, τ = 2 — the electron-tube construction (one full extra turn per ring
  rev beyond τ = 1, giving σ_eff = 2 on the bilobe; see electron-tube.md §5).
- N = 3, τ = 1/3 — the proton clover construction.

### 1.5 Shear `s`

A second rotation rate parameter that affects **overlays only** (grid lines
and path tubes), not the surface mesh. Effective overlay rate is `(τ − s)`.
At `s = 0` the overlays follow the surface twist; at `s = τ` they cut across
it.

### 1.6 Path overlay

Closed curves on the surface parameterised by

```
θ(t) = 2π · n_θ · t          t ∈ [0, 1]
φ(t) = ph0 + 2π · n_φ · t
α(θ) = (τ − s) · θ
```

with (n_θ, n_φ) entered as integers. `copies` draws multiple paths at evenly
spaced ph0 ∈ {0, 2π/k, 4π/k, …}. Closure: `n_θ · (τ − s) − n_φ` should equal
an integer modulo 1/N for the path to close cleanly. The lab displays the
"path drift" = `n_θ · (τ − s)` as a diagnostic.

For the electron-tube preset, (n_θ, n_φ) = (2, 1) traces the T(1, 2)
double-loop with two ring winds and one tube wind, matching the WvM closure
on a bilobe with τ = 2.

---

## 2. UI layout

```
┌────────────────────────────────────────────────────────────┐
│  TOP BAR:  N  a₁  a₂  R_major  R_c  τ  snap  shear  opacity│
├──────────┬──────────────────────────────────────┬──────────┤
│  LEFT    │                                      │  RIGHT   │
│  PANEL   │       3D corrugated tube             │  PANEL   │
│  ~260px  │                                      │  ~260px  │
│          │  (κ-shaded; optional path overlay)   │          │
│ Formula  │                                      │ Profile  │
│ Presets  │                                      │ preview  │
│ Path     │                                      │ (2D)     │
│ Toggles  │                                      │ Geometry │
│ Profiles │                                      │ Closure  │
└──────────┴──────────────────────────────────────┴──────────┘
```

### 2.1 Top bar (geometry)

| Control | Type | Default | Notes |
|---|---|---|---|
| N | slider (int) | 3 | Lobe count, 2–8 |
| a₁ | slider | 0.43 | Fundamental amplitude |
| b₁ | slider | 0.00 | First-harmonic split (b₁ = −a₁ at N=2 → true ellipse) |
| a₂ | slider | 0.00 | Second-harmonic amplitude |
| b₂ | slider | 0.00 | Second-harmonic split |
| R_major | slider | 3.0 | Ring radius |
| R_c | slider | 1.00 | Mean cross-section radius |
| τ | slider | 1/3 | Twist rate (continuous) |
| snap | button | — | Round τ to nearest k/N |
| shear `s` | slider | 0 | Overlay rotation offset |
| opacity | slider | 0.55 | Surface translucency |
| Reset | button | — | Restore defaults |

### 2.2 Left panel — Formula, presets, paths, toggles, profiles

- **Cross-section formula** — fixed reminder of the harmonic form
  `z(t) = R_c·e^{it}·[1 + a₁cos Nt + a₂cos 2Nt + i(b₁sin Nt + b₂sin 2Nt)]`.
- **Presets**:
  - Circle (degenerate)
  - **True ellipse** (N=2, b₁ = −a₁, τ=0)
  - **Electron tube** (N=2 ellipse, τ=2, T(1,2) path on)
  - Rounded triangle (N=3, all convex)
  - **Smooth clover** (N=3, τ=1/3, three-fold symmetric paths on)
  - **Quark clover** (N=3, A_lobe = 4π/3, polar slice)
  - **Quark clover (fat lobe)** (N=3, b₁ = 0.2 — same charge, less swing)
  - Deep clover (N=3, sharp valleys)
  - Rounded square / Quad clover (N=4)
  - Rounded pentagon (N=5)
  - Rounded hexagon (N=6)
- **Path overlay**: n_θ, n_φ, copies (multiple symmetric paths at offsets ph0 = 2πk/copies).
- **Toggles**: Surface, Wireframe, κ-shaded color, Grid lines, Path overlay, Ring spine, XYZ axes.
- **Profiles**: save/load named profiles to localStorage (`tubeLab.profiles`).

### 2.3 Right panel — Cross-section preview & info

- **Cross-section preview** (2D canvas): the curve at the current (N, a₁, a₂, R_c),
  coloured by signed curvature, with markers at the N lobe-axis points (red dots)
  and the N saddle midpoints (blue dots), and a faint dashed circle at r = R_c.
- **Geometry readouts**:
  - `r at lobe` = |z(0)| — symmetric peak.
  - `r at saddle` = |z(π/N)| — symmetric trough.
  - `r_max`, `r_min` — true numerical bounds (catches off-axis extrema).
  - `peak − R_c`, `R_c − trough` — radial prominence and valley depth.
  - `ellipse foci sep` — focal distance, shown for N = 2. Exact for the
    true ellipse (b₁ = −a₁, a₂ = b₂ = 0); approximate for other N = 2 curves
    (focal distance of the ellipse with the same numeric r_max, r_min).
  - `κ_min`, `κ_max` — signed curvature extremes.
  - `ε = R_c / R_major` — aspect parameter (matches metric-charge's L_u/L_w analog).
  - `L` — numeric perimeter of the cross-section.
- **Closure**:
  - `τ · N` — the integer-target value for closure.
  - `closure` — ✓ if `τ · N` is integer (within ±0.001), ✗ otherwise.
  - `path drift` = `n_θ · (τ − s)` for the path-overlay closure check.

---

## 3. Rendering

### 3.1 Surface mesh

`N_θ = 240` × `N_φ = 180` (~ 43 k triangles). Profile is pre-sampled at 720
densely-spaced φ values into typed arrays. Curvature is sampled at the same
points and used to interpolate per-vertex colour.

### 3.2 Surface coloring (κ-shaded)

For each vertex, look up κ(φ) on the profile, normalise against max |κ|, then
lerp between neutral grey and red (positive κ, lobes) or neutral grey and
blue (negative κ, saddles). When `κ-shaded color` is toggled off, all
vertices render in neutral grey.

### 3.3 Path overlay

Up to `copies` paths drawn as glowing `TubeGeometry`, each at a different ph0
offset, distinguishable by color.

### 3.4 Camera

Default `(2.5·R_major, 1.5·R_major, 3.0·R_major)` looking at the origin.
OrbitControls + camera persistence to localStorage (`tubeLab.camera`).

---

## 4. Implementation notes

### 4.1 Why the harmonic form rather than a polar curve?

An earlier version used a polar curve r(φ). It is the b₁ = b₂ = 0 slice of
the present family — convenient, but it cannot express a true ellipse: an
ellipse is not a finite cosine series in its own polar angle. The harmonic
form z(t) = R_c·e^{it}·w(t) parameterises the curve by a free parameter t,
keeps the N-fold symmetry explicit (every term is N-periodic in t), still has
a clean closed-form curvature, and *does* contain the exact ellipse (and
exact rounded N-gons, circle, etc.). It is strictly more general than the
polar form at the cost of two extra parameters. See
[tube-function.md §2](../projects/ma-domain/work/tube-function.md).

### 4.2 Why two harmonic levels, each with an amplitude and a split?

Two harmonic levels (Nt and 2Nt) give independent control of *lobe
prominence* and *valley depth* at the symmetry points — one level alone
couples them. Each level carries an amplitude aₘ (the symmetric, polar
part) and a split bₘ (the asymmetric part that lets the inner/outer harmonic
partners differ). The split is what unlocks the ellipse and the
fat-lobe quark family. b₂ is rarely needed; it is exposed for completeness.
A third level at 3Nt would add lobe-peak sharpening but is not required for
the stated knobs.

### 4.3 Relationship to the arc-clover (proton-lab)

The discrete-arc clover at (r_lobe, r_saddle) = (0.8, 0.4) has

- peak = 2.0, trough = 0.8 (so peak/trough = 2.5)
- C¹ everywhere, but **curvature jumps** at the six junction points
  (κ = +1/r_lobe = +1.25 inside lobes, κ = −1/r_saddle = −2.5 inside saddles).

The single-harmonic smooth-clover preset in this lab (N=3, a₁=0.43, a₂=0,
R_c=1.4) has the same peak/trough at the symmetry points (2.0 / 0.8) **and**
is C^∞ everywhere. (a₂ = 0 keeps all extrema at the symmetry points, so the
named peak/trough are the true global extrema. The saddle midpoint is
genuinely concave with κ ≈ −10 — well past the threshold a₁ > 1/(N²+1) =
1/10 for N=3.) The two curves coincide at the six tangency points but differ
in the middle of each arc — the smooth version's curvature varies
continuously instead of being piecewise constant.

The "lobe charge +2/3 and saddle charge −1/3" assignment of clover-quarks.md
depends only on the signed turning ∮ κ ds = 2π and the fraction of that
turning carried by each lobe-or-saddle region. For any closed simple curve,
the lobe vs. saddle fractions can be defined by integrating κ over the
positive-κ vs. negative-κ regions of φ — and that integral is independent
of whether the curve is piecewise circular or sinusoidal. So the smooth
clover supports the same quark identifications, with a more physical
continuous-curvature substrate.

### 4.4 Performance

Profile cache (`cachedProfile`) is rebuilt only when a shape parameter
(N, a₁, b₁, a₂, b₂, R_c) changes. Other slider drags (R_major, τ, shear,
opacity) reuse the cached profile and only rebuild the surface mesh and
overlays. All operations should complete < 16 ms in modern browsers.

---

## 5. Keyboard shortcuts

- `r` — reset camera to default
- `g` — toggle grid lines
- `p` — toggle path overlay

---

## 6. Future extensions (out of scope for v1)

- **Third harmonic level (a₃, b₃)** for independent lobe-peak sharpening.
- **Chiral cross-sections** — a relative phase between the inner and outer
  harmonic partners (complex coefficients) breaks the mirror symmetry that
  the real a/b coefficients preserve.
- **True geodesics** on the corrugated tube (replace `(n_θ, n_φ)` straight
  lines in parameter space with geodesic integration).
- **Mass-formula overlay** — compute μ²(m_t, m_r) = (m_r − σ_eff m_t)² +
  (m_t / ε)² in real time and display the lowest few modes.
- **Modal density overlay** — solve the Laplacian on the corrugated surface
  and shade by |ψ|² for the selected mode.
- **Cross-link with proton-lab** — match the smooth clover to the arc clover
  visually (overlay both for comparison).
