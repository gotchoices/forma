# Torus Modes — Spec

Visualize standing-wave eigenmodes on the curved (embedded) torus. Each mode ψ = f(θ₁)·e^{iq_eff θ₂} has a non-uniform |f(θ₁)|² that depends on curvature ε = a/R and effective winding q_eff = n₂ − s·n₁. Probability density renders as glowing lobes inside a translucent torus.

Context: R21 (curved-torus eigenmodes, localization), R20 (harmonic spectrum), R19 (shear, charge).

## Physics

### Sturm-Liouville equation

    d/dθ₁ [(1 + ε cos θ₁) df/dθ₁] + [λ(1 + ε cos θ₁) − ε²q²/(1 + ε cos θ₁)] f = 0

where q = q_eff = n₂ − s·n₁, periodic on [0, 2π].

Eigenfunctions have definite parity under θ₁ → 2π − θ₁:
- **Even** (cos-like): peaks at outer (θ₁=0) and/or inner (θ₁=π) equator
- **Odd** (sin-like): peaks at top/bottom of tube (θ₁=π/2, 3π/2)

On the curved torus (ε > 0), the potential well at the outer equator pulls even-mode amplitude outward (R21 F1–F2). The ±n₁ degeneracy lifts (R21 F3): cos-like and sin-like modes get different eigenvalues.

### Mode identification

A mode is (n₁, n₂, parity). Key modes:

| Mode | (n₁, n₂) | Parity | Identity |
|------|----------|--------|----------|
| Electron | (1, 2) | even | R19 fundamental |
| CPT conjugate | (−1, −2) | even | Anti-electron |
| Ground | (0, 2) | even | R21 F2: localizes outward |
| n₁=1 sin | (1, 2) | odd | R21 F3: peaks at top/bottom |
| Harmonic 2 | (2, 4) | even | R20 F1: uncharged |
| Harmonic 3 | (3, 6) | even | R20 F1: uncharged |
| Pure toroidal | (0, 1) | even | Lightweight uncharged mode |

The viewer supports **multiple simultaneous modes**, each with its own density cloud and color.

## Display

### Torus surface

Translucent shell via `buildTorusGeom`. Adjustable opacity, optional wireframe overlay. Torus in XZ plane, axis Y.

### Density cloud

For each active mode, a `THREE.Points` particle cloud fills the tube volume. Particle opacity/size ∝ |f(θ₁)|² at each particle's poloidal angle. High-density regions glow as visible **lobes**.

Particles are volumetric (distributed throughout the tube cross-section, not just on the surface). Multiple modes render as overlapping clouds in distinct colors.

### Info panel

Bottom: ε, s, selected mode's eigenvalue λ, number of active modes.

## Controls

### Global

| Control | Range | Default | Notes |
|---------|-------|---------|-------|
| ε (a/R) | 0.01–0.95 | 0.30 | Torus curvature |
| Shear s | 0–0.5 | 0.165 | Electron value from R19 |
| Shell α | 0–1 | 0.12 | Torus surface opacity |
| Wire | toggle | off | Wireframe overlay |

### Mode slots

A scrollable list of active modes. Each slot:

| Control | Type | Default | Notes |
|---------|------|---------|-------|
| n₁ | int spinner, −5…5 | 1 | Poloidal quantum number |
| n₂ | int spinner, −10…10 | 2 | Toroidal quantum number |
| Parity | even/odd toggle | even | cos-like or sin-like |
| Color | swatch | per-slot | Distinct default per slot |
| Brightness | slider, 0–1 | 0.8 | Cloud intensity multiplier |
| Visible | toggle | on | Show/hide cloud |
| ✕ | button | — | Remove slot |

**Add mode** button appends a new slot.

**Presets** dropdown for quick setup:
- *Electron* — single (1,2) even
- *R21 trio* — ground (0,2)even + (1,2)even + (1,2)odd, three colors
- *Harmonics 1–3* — (1,2), (2,4), (3,6) all even

### Mode eigenvalue readout

Each mode slot displays its computed λ. Optionally also shows the charge overlap C = ∫f cos θ₁ (1+ε cos θ₁) dθ₁.

## Eigensolver

Fourier-basis approach (small matrix, real-time):

1. Separate by parity: even modes use {1, cos θ, cos 2θ, …, cos Nθ}, odd modes use {sin θ, sin 2θ, …, sin Nθ}. N_max ≈ 16.
2. Compute matrix elements of the SL operator analytically using trig product identities (the metric factor 1+ε cos θ couples adjacent Fourier orders).
3. Solve the N_max × N_max real symmetric eigenproblem (Jacobi rotation method).
4. The k-th eigenvalue (sorted ascending) corresponds to the mode with k poloidal nodes.

Recompute when ε or s change. With N_max = 16, the matrix is tiny — instant in JS.

## Particle cloud

Per active mode:
- M ≈ 15 000 particles distributed in the tube volume
- Each particle: random (θ₁, θ₂, ρ) where ρ ∈ [0, a] is radial offset from tube center
- 3D position from standard torus embedding: x = (R + ρ cos θ₁) cos θ₂, etc.
- Vertex color = mode color, vertex alpha = |f(θ₁)|² × brightness × radial_fade(ρ/a)
- Radial fade: (1 − 0.6 × (ρ/a)²) — brighter at tube center, dimmer at edge
- `THREE.Points` with `size`, `sizeAttenuation`, `vertexColors`, `transparent`, `depthWrite: false`

Regenerate positions when ε changes (tube shape changes). When only f changes (mode parameters, s), update alpha buffer only. When brightness changes, scale alpha buffer without recompute.

## Camera

- OrbitControls, auto-fit on ε change
- Default position: angled view showing both outer and inner equator

## Persistence

`localStorage` key `torus-modes`. Save ε, s, shell settings, mode list. Reset button clears.

## Architecture notes (for extensibility)

- **Mode class/object**: each mode is a self-contained record {n1, n2, parity, color, brightness, visible, eigenvalue, f_coeffs, f_samples}. Adding new mode types (e.g., mixed-parity, superpositions) means adding fields, not restructuring.
- **Eigensolver is a pure function**: `solve(epsilon, q_eff, parity, N_max) → {eigenvalues[], eigenvectors[][]}`. Can be reused for future tools.
- **Particle system per mode**: each mode owns its own `THREE.Points`. Adding/removing modes = adding/removing point clouds. No coupling between modes.
- **Future: interference rendering**: a separate "superposition" cloud that computes |Σ c_k f_k(θ₁)|² would be a new particle system reading from all mode slots.

## Future features

- **Charge overlap display**: compute and show C(mode) per slot — enables reproducing R21 F7–F8 tables visually.
- **Eigenvalue spectrum inset**: small bar chart of λ values, highlighting active modes.
- **Harmonic composition**: load R20 proton model (fundamental + thermal harmonics) and display the composite density.
- **Animation**: slow rotation of density cloud phase (visual only), pulsing lobes.
- **Cross-section view**: slice the torus to show 2D density profile in the (ρ, y) plane.
- **Mode superposition**: toggle between independent clouds and coherent |Σψ|².
