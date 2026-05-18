# Tube Lab — Spec

Interactive workbench for **smooth N-fold-symmetric tube cross-sections** swept
into a corrugated torus with adjustable twist. Generalizes the discrete-arc
clover of [proton-lab](proton-lab.html) to any lobe count and any valley
depth, using a C^∞ Fourier polar curve so curvature is continuous everywhere.

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

### 1.1 Cross-section profile (polar form)

The cross-section is a closed plane curve parameterised by

```
r(φ) = R_c · [ 1 + a₁ · cos(N · φ) + a₂ · cos(2 · N · φ) ]
P(φ) = ( r(φ) · cos φ , r(φ) · sin φ )
```

with three independent shape parameters:

| Parameter | Symbol | Role |
|---|---|---|
| Lobe count | `N` ∈ ℤ, 2 ≤ N ≤ 8 | Number of N-fold symmetric features around the cross-section |
| Fundamental amplitude | `a₁` ∈ [0, 0.9] | Sets the gross peak-to-trough swing |
| Second harmonic | `a₂` ∈ [−0.4, 0.4] | Sharpens or flattens valleys; introduces concave saddles when large |
| Mean radius | `R_c` | Sets the absolute size of the cross-section (mean r = R_c) |

The relationship between (a₁, a₂) and the named knobs *peak prominence* and
*valley depth* — measured at the symmetric extrema — is

- **Peak** at φ = 0: r(0) = R_c · (1 + a₁ + a₂) ⟹ peak − R_c = R_c · (a₁ + a₂)
- **Trough** at φ = π/N: r(π/N) = R_c · (1 − a₁ + a₂) ⟹ R_c − trough = R_c · (a₁ − a₂)

so if you want a peak prominence p and a valley depth v (both as fractions of R_c),
set **a₁ = (p + v) / 2**, **a₂ = (p − v) / 2**.

This identification is exact when (a₁, a₂) are small enough that the global
peak and trough actually sit at the symmetry points. For larger |a₂/a₁|,
additional extrema appear off-axis at cos(Nφ) = −a₁/(4a₂); the readout shows
the numerical `r_min`, `r_max`, `κ_min`, `κ_max` so the user always sees the
true bounds.

### 1.2 Curvature

The signed curvature of a polar curve r(φ) is

```
κ(φ) = ( r² + 2·r'² − r·r'' ) / ( r² + r'² )^{3/2}
```

with r' = dr/dφ, r'' = d²r/dφ². All three quantities are closed-form sums of
sin/cos for the Fourier form above, so curvature is computed analytically
with no discretisation artefacts. The 2D preview and 3D surface are coloured
by κ via a warm-to-cool ramp:

- κ > 0 → warm (red) — convex, lobe-like
- κ ≈ 0 → neutral grey
- κ < 0 → cool (blue) — concave, saddle-like

The colour scale auto-normalises against max |κ| on the profile.

### 1.3 Degenerate cases (presets)

| Case | Parameters | Geometry |
|---|---|---|
| Circle | a₁ = a₂ = 0 | Mean radius R_c |
| Bilobe (electron-tube limit) | N = 2, a₁ ≈ 0.3, a₂ ≈ 0 | Smooth ellipse-like, all convex |
| Rounded N-gon | small a₁, a₂ ≈ 0 | All-convex N-lobed shape (triangle/square/pentagon/hexagon as N varies) |
| Smooth clover | N = 3, a₁ ≈ 0.43, a₂ = 0, R_c ≈ 1.4 | Single-harmonic three-lobe with concave saddles. Matches the arc-clover's peak 2.0 / trough 0.8 at the symmetry points. (Use a₂ > 0 for fine-tuning the per-lobe turning A_lobe; see [tube-function.md §5.2.1](../projects/ma-domain/work/tube-function.md).) |
| Deep clover | N = 3, a₁ ≈ 0.55, a₂ ≈ 0.25 | Sharp narrow valleys, large lobes |

### 1.4 Surface embedding (corrugated torus)

Same construction as proton-lab. Sample P(φ), rotate by α = τ·θ in the
cross-section plane, then place at the ring at angle θ:

```
samp        = P(φ)
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
| a₂ | slider | 0.00 | Second-harmonic amplitude |
| R_major | slider | 3.0 | Ring radius |
| R_c | slider | 1.00 | Mean cross-section radius |
| τ | slider | 1/3 | Twist rate (continuous) |
| snap | button | — | Round τ to nearest k/N |
| shear `s` | slider | 0 | Overlay rotation offset |
| opacity | slider | 0.55 | Surface translucency |
| Reset | button | — | Restore defaults |

### 2.2 Left panel — Formula, presets, paths, toggles, profiles

- **Cross-section formula** — fixed reminder of `r(φ) = R_c · [1 + a₁ cos Nφ + a₂ cos 2Nφ]`.
- **Presets**:
  - Circle (degenerate)
  - Ellipse-like bilobe (N=2, τ=0)
  - **Electron tube** (N=2, τ=2, T(1,2) path on)
  - Rounded triangle (N=3, all convex)
  - **Smooth clover** (N=3, τ=1/3, three-fold symmetric paths on)
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
  - `r at lobe` = r(0) — symmetric peak.
  - `r at saddle` = r(π/N) — symmetric trough.
  - `r_max`, `r_min` — true numerical bounds (catches off-axis extrema).
  - `peak − R_c`, `R_c − trough` — the user's "foci separation" and "valley depth".
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

### 4.1 Why Fourier polar rather than Cartesian Fourier?

For lobed / star-shaped cross-sections, r(φ) > 0 single-valued in φ is the
natural representation. Polar form makes the symmetry group ℤ_N explicit
(harmonics are `cos(kNφ)`) and the curvature has a clean closed form. A
Cartesian (x(t), y(t)) Fourier series would also work but doubles the
parameter count and obscures the N-fold structure.

### 4.2 Why exactly two harmonics?

Two harmonics give independent control of *lobe prominence* and *valley
depth* at the symmetry points. One harmonic alone couples them (a single
amplitude `a` sets both peak height and valley depth simultaneously, via
the same N²-eigenvalue scaling). A third harmonic at 3Nφ would add control
over the curvature at the lobe peak (sharpening or flattening the lobe top)
but is not required for the user's stated knobs. The architecture supports
adding it (`a₃` in `rOf` / `rpOf` / `rppOf`) if a future need arises.

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

Profile cache (`cachedProfile`) is rebuilt only when N, a₁, a₂, or R_c
change. Other slider drags (R_major, τ, shear, opacity) reuse the cached
profile and only rebuild the surface mesh and overlays. All operations
should complete < 16 ms in modern browsers.

---

## 5. Keyboard shortcuts

- `r` — reset camera to default
- `g` — toggle grid lines
- `p` — toggle path overlay

---

## 6. Future extensions (out of scope for v1)

- **Third harmonic (a₃)** for independent lobe-peak sharpening.
- **Asymmetric profiles** with sin terms — chiral cross-sections.
- **True geodesics** on the corrugated tube (replace `(n_θ, n_φ)` straight
  lines in parameter space with geodesic integration).
- **Mass-formula overlay** — compute μ²(m_t, m_r) = (m_r − σ_eff m_t)² +
  (m_t / ε)² in real time and display the lowest few modes.
- **Modal density overlay** — solve the Laplacian on the corrugated surface
  and shade by |ψ|² for the selected mode.
- **Cross-link with proton-lab** — match the smooth clover to the arc clover
  visually (overlay both for comparison).
