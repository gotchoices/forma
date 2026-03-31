# Torus Modes — Spec

Visualize standing-wave eigenmodes on the material sheet (torus surface).
Each mode ψ = f(θ₁)·e^{iq_eff θ₂} has a non-uniform |f(θ₁)|² that depends
on curvature ε = a/R and effective winding q_eff = n₂ − s·n₁.  Energy
density is shown as brightness variation on the torus surface itself, with
an optional geodesic path overlay showing the mode's winding.

Context: R21 (curved-torus eigenmodes, localization), R20 (harmonic spectrum),
R19 (shear, charge), torus-studio (geodesic path reference).

---

## Physics

### Sturm-Liouville equation

    d/dθ₁ [(1 + ε cos θ₁) df/dθ₁] + [λ(1 + ε cos θ₁) − ε²q²/(1 + ε cos θ₁)] f = 0

where q = q_eff = n₂ − s·n₁, periodic on [0, 2π].

Eigenfunctions have definite parity under θ₁ → 2π − θ₁:
- **Even** (cos-like): peaks at outer (θ₁=0) and/or inner (θ₁=π) equator
- **Odd** (sin-like): peaks at top/bottom of tube (θ₁=π/2, 3π/2)

On the curved torus (ε > 0), the potential well at the outer equator pulls
even-mode amplitude outward (R21 F1–F2).  The ±n₁ degeneracy lifts (R21 F3):
cos-like and sin-like modes get different eigenvalues.

### Why the surface, not the volume

The mode is a standing wave on the 2D material sheet — the torus surface T².
Energy density is |ψ(θ₁, θ₂)|² evaluated on the surface.  The material
sheet has no interior; it is a 2-dimensional manifold.  Fields extend into
3D space (producing the Coulomb field), but the mode itself lives on the
surface.

Since |e^{iq_eff θ₂}|² = 1, the density depends ONLY on the tube angle θ₁.
The surface brightness is constant around the ring (in φ) and varies only
around the tube cross-section (in θ₁).

### Mode identification

A mode is (n₁, n₂, parity).  Key modes:

| Mode | (n₁, n₂) | Parity | Identity |
|------|----------|--------|----------|
| Electron | (1, 2) | even | R19 fundamental |
| CPT conjugate | (−1, −2) | even | Anti-electron |
| Ground | (0, 2) | even | R21 F2: localizes outward |
| n₁=1 sin | (1, 2) | odd | R21 F3: peaks at top/bottom |
| Harmonic 2 | (2, 4) | even | R20 F1: uncharged |
| Harmonic 3 | (3, 6) | even | R20 F1: uncharged |
| Pure toroidal | (0, 1) | even | Lightweight uncharged mode |
| Ghost (1,1) | (1, 1) | even | Spin-1, lighter than electron |

---

## Display

### Primary: surface brightness modulation

Each active mode modulates the brightness/emissive color of the torus
surface.  Every vertex on the torus mesh is at a specific θ₁.  The vertex
color intensity is set to |f(θ₁)|² × mode brightness.

For a single mode: the torus glows in the mode's color where |f(θ₁)|² is
large, and is dark where it is small.

For multiple modes: each mode contributes its own color weighted by its
density at that θ₁.  Colors blend additively — regions where two modes
overlap show a mixed hue.

The torus mesh should use MeshPhongMaterial (or MeshStandardMaterial) with
per-vertex colors set via the `color` buffer attribute.  The emissive
channel should carry the mode color so the bright regions glow even without
direct light.

### Geodesic path overlay

Each active mode can optionally show its (n₁, n₂) geodesic path on the
torus surface — the same winding path from torus-studio.  The path is drawn
as a thin tube on the surface in the mode's color, showing which trajectory
the standing wave wraps around.

Path formula (from torus-studio):

    θ(t) = n₁ · t
    φ(t) = n₂ · t       (always n₂, not q_eff — see torus-studio spec)

This lets the user see both WHERE the energy concentrates (surface
brightness) and WHAT PATH the wave follows (geodesic).

### Tube reference lines (optional)

When shear is nonzero, optionally show the tube reference lines from
torus-studio (φ_emb = φ₀ − s·θ) to visualize the lattice tilt.

### Info panel

Bottom: ε, s, active mode eigenvalue λ, q_eff, charge overlap C.

---

## Controls

### Shape (shared with torus-studio concepts)

| Control | Range | Default | Notes |
|---------|-------|---------|-------|
| a/R (= ε) | slider, 0.01–12 | 6.60 | Torus shape — same range as torus-studio |
| Shear s | slider, 0–0.50 | 0.157 | Electron value; α preset button |
| Shell α | slider, 0–1 | 0.5 | Surface base opacity (modulated by density) |
| Wire | toggle | off | Wireframe overlay |

**a/R presets**: same as torus-studio (Ring 0.5, Horn, Horizon, q=e, WvM
sphere).  The physically relevant electron shape is a/R ≈ 6.60, well into
spindle territory.

**Shear presets**: 0, α (0.157), ¼, ½.

### Mode slots

A scrollable list of active modes.  Each slot:

| Control | Type | Default | Notes |
|---------|------|---------|-------|
| n₁ | int spinner, −5…5 | 1 | Tube winding (poloidal) |
| n₂ | int spinner, −10…10 | 2 | Ring winding (toroidal) |
| Parity | even/odd toggle | even | cos-like or sin-like |
| Color | swatch | per-slot | Distinct default per slot |
| Brightness | slider, 0–1 | 0.8 | Surface intensity multiplier |
| Geodesic | toggle | on | Show/hide the (n₁,n₂) path |
| Visible | toggle | on | Show/hide this mode's contribution |
| ✕ | button | — | Remove slot |

**Add mode** button appends a new slot with next unused color.

**Presets** dropdown:
- *Electron (1,2)* — single mode, even
- *Ghost (1,1)* — the stubborn ghost mode
- *R21 trio* — ground (0,2)even + (1,2)even + (1,2)odd
- *Harmonics 1–3* — (1,2), (2,4), (3,6) all even
- *Charge family* — (1,1), (1,2), (1,3) even — shows how density shifts
  with n₂

### Mode eigenvalue readout

Each mode slot displays:
- q_eff = n₂ − s·n₁
- λ (eigenvalue from eigensolver)
- C = ∫ f(θ₁) cos θ₁ (1+ε cos θ₁) dθ₁ (charge overlap integral)

---

## Eigensolver

Fourier-basis approach (small matrix, real-time):

1. Separate by parity: even modes use {1, cos θ, cos 2θ, …, cos Nθ},
   odd modes use {sin θ, sin 2θ, …, sin Nθ}.  N_max ≈ 16.
2. Compute matrix elements of the SL operator via numerical quadrature
   (the metric factor 1+ε cos θ couples adjacent Fourier orders).
3. Solve the generalized eigenproblem H v = λ M v via Cholesky + Jacobi.
4. The k-th eigenvalue (sorted ascending) corresponds to the mode with
   k poloidal nodes.

Recompute when ε or s change.  With N_max = 16, the matrix is tiny —
instant in JS.

---

## Surface color computation

For each active mode m with density array density_m[θ₁] and color
(r_m, g_m, b_m):

1. Compute |f(θ₁)|² on a fine grid (256 samples over [0, 2π]).
2. Normalize so max = 1.
3. For each vertex on the torus mesh, look up θ₁ from the vertex position
   (θ₁ = atan2(y, x − R_major·cos φ)... or more simply, store θ₁ per
   vertex during mesh construction).
4. Set vertex color:
   R = Σ_m (r_m × density_m[θ₁] × brightness_m)
   G = Σ_m (g_m × density_m[θ₁] × brightness_m)
   B = Σ_m (b_m × density_m[θ₁] × brightness_m)
5. Clamp to [0, 1].

The torus mesh needs to be built with θ₁ stored per vertex (either as a
separate attribute or reconstructed from position).  Since `buildTorusGeom`
constructs vertices in a (θ₁, θ₂) grid, the θ₁ for each vertex is known
at construction time.

When mode parameters change, only the color buffer needs updating — no
geometry rebuild.  When ε changes, rebuild the mesh and recompute
eigenvalues.

---

## Geodesic path rendering

Per active mode with geodesic enabled:

- Path: θ(t) = n₁·t, φ(t) = n₂·t, t ∈ [0, 2π]
- Rendered as a thin TubeGeometry on the torus surface (same approach
  as torus-studio)
- Color: the mode's color, fully opaque
- Tube radius: small (0.02 / world scale), so it reads as a line on
  the surface

When shear or winding changes, rebuild the path geometry.

---

## Camera

- OrbitControls, auto-fit on ε change
- Default position: angled view showing both outer and inner equator

## Persistence

`localStorage` key `torus-modes`.  Save ε, s, shell settings, mode list.
Reset button clears.

---

## Architecture notes

- **Mode object**: {n1, n2, parity, color, brightness, visible,
  showGeodesic, eigenvalue, chargeOverlap, f_coeffs, densitySamples}.
- **Eigensolver is a pure function**: `solve(epsilon, q_eff, parity,
  N_max) → {eigenvalues[], eigenvectors[][]}`.  Reusable.
- **Single shared torus mesh** with vertex color buffer.  All modes
  contribute to the same color buffer (additive).  Updating modes =
  recomputing colors, not rebuilding meshes.
- **Separate geodesic meshes** per mode.  Adding/removing modes =
  adding/removing tube meshes.

---

## Future features

- **Animation**: slow phase rotation of the wave (visual only — rotate
  the brightness pattern around the ring at a rate proportional to the
  mode's energy).
- **Cross-section inset**: a small 2D panel showing the tube
  cross-section with |f(θ₁)|² as a polar plot.
- **Eigenvalue spectrum inset**: small bar chart of λ values, highlighting
  active modes.
- **Mode superposition**: toggle between independent mode colors and
  coherent |Σ c_k ψ_k|² interference pattern.
- **Charge overlap display**: per-slot C value already in the spec;
  visually mark the charge-producing region on the surface.
