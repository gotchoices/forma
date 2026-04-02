# R46 Findings: Electron filter — aperture effects on a toroidal cavity

Study: [`README.md`](README.md)

---

## Track 1. Baseline EM fields — unipolar vector model with circular polarization

Script: [`scripts/track1_baseline_fields.py`](scripts/track1_baseline_fields.py)
Model:  [`scripts/torus_model.py`](scripts/torus_model.py)

### Model summary

The electron is a standing electromagnetic wave (eigenmode) on a
2D periodic sheet — a flat rectangle with opposite edges identified
(topologically a torus).  The two periodic coordinates are θ₁ (tube,
minor circle) and θ₂ (ring, major circle).  The electron is the
(1,2) mode: 1 winding around the tube, 2 around the ring.

The model is a 2D drum head, not a 3D hollow cavity.  The field
lives on the surface; there is no radial mode structure.  The
"thickness" a in the energy normalization is a scale factor for
the compact dimension, not a wall depth.

**Circular polarization (CP):** For a circularly polarized photon
with n₁ = 1, the E-field rotation rate matches the surface-normal
rotation (one turn per tube circuit).  The θ₁ phase cancels the
θ₁ geometry — the field depends only on θ₂.

**Unipolar field:** The radiation pressure always pushes outward
from the 2D sheet.  Field cannot pass backward through the sheet:

    P_out(θ₂) = E₀ (1 + cos(q_eff θ₂))    always ≥ 0

The DC component (E₀) maintains the cavity against the membrane's
confining force (R37 force balance).  The AC component
(E₀ cos(q_eff θ₂)) is the standing-wave modulation that leaks
through the Compton window as external field and produces charge.
The opposite knot chirality reverses the charge sign → positron.


### Current settings

| Parameter | Value | Source |
|-----------|-------|--------|
| Mode | (n₁, n₂) = (1, 2) | WvM electron topology |
| Aspect ratio r = a/R | free; tested at 1, 2, 4, 8 | R19/R44 convention |
| Shear s | solved per r to give α = 1/137.036 | CP α formula |
| Convention | KK (Kaluza-Klein) | R19 F39 |
| Field model | CP vector, unipolar | This study |
| Grid | 256 (θ₁) × 512 (θ₂) | Numerical validation |


---

### What the model produces for the electron

The table below shows the physical properties of the (1,2) electron
mode.  Mass is an input (sets the energy scale).  Spin is topological
(from the (1,2) winding numbers).  Charge is computed from the field
integral.  Magnetic moment is not yet computed in this track —
that is the goal of the aperture analysis.

| Property | Model value | Experiment | Status |
|----------|-------------|------------|--------|
| **Mass** | m_e c² (input) | 0.511 MeV | By construction — E₀ is set so total field energy = m_e c² |
| **Spin** | ℏ/2 | ℏ/2 | Topological: photon angular momentum ℏ divided by the double loop (ω_s = 2ω) gives L = ℏ/2 |
| **Charge** | Q = −e (exact) | −e | Shear s is solved to give α = 1/137.036, then Q = −e follows analytically |
| **Magnetic moment** | μ = g(e/2m_e)·(ℏ/2), g = 2 | g = 2.00232 | Topological g = 2 from R8; anomalous part (g−2) is the target of R46 |

**Mass** is not predicted — it is an input that sets the absolute
field amplitude E₀ = √(m_e c² / (4π²a²R ε₀)).  The mass *ratios*
between modes on the same sheet (e.g., ghost/electron) are predicted.

**Spin = ℏ/2** comes from the (1,2) topology: the confined photon
must traverse the double loop twice to return to its starting
orientation, so the internal frequency is ω_s = 2ω_C.  Angular
momentum L = E/ω_s = ℏω_C/(2ω_C) = ℏ/2.  This is purely
topological and does not depend on r, s, or the field model.

**Charge = −e** is the central result of this track.  It is achieved
by solving for the shear s that produces α = 1/137.036 in the CP
formula.  The charge integral is then exactly −e by construction.
Numerical validation confirms this to 0.3%.

**Magnetic moment:** The topological g-factor g = 2 is established
(R8 F9) independent of the charge distribution.  The anomalous
part (g − 2 ≈ α/2π ≈ 0.00116) has NOT been reproduced.  R44 ruled
out shear-induced charge distribution as the mechanism.  R46's
hypothesis is that a cavity aperture (slot) provides the anomalous
correction.  This is the subject of subsequent tracks.


---

### F1. The CP model produces a new α formula

Setting Q = e in the CP charge integral with KK normalization:

    α_CP  = μ sin²(2πs) / (4π q²)

where μ = √(1/r² + q²) and q = n₂ − s.  Compare R19 scalar:

    α_R19 = r² μ sin²(2πs) / (4π q²)

The relationship is exact:  **α_CP = α_scalar / r²**.

At r = 1 (square torus), both formulas agree.  At larger r, the
CP model needs more shear because the circular-polarization charge
integral removes the r² factor that the scalar model had.


### F2. The CP shear converges to a fixed value at large r

| r    | s (scalar) | s (CP)    | s_CP / s_scalar | q_eff (CP) |
|------|------------|-----------|-----------------|------------|
| 1.00 | 0.064981   | 0.064981  | 1.000           | 1.935019   |
| 2.00 | 0.033515   | 0.067960  | 2.028           | 1.932040   |
| 4.00 | 0.016933   | 0.068823  | 4.065           | 1.931177   |
| 8.00 | 0.008497   | 0.069048  | 8.126           | 1.930952   |

The scalar shear goes to zero as r → ∞ (s_scalar ∝ 1/r).
The CP shear converges to **s ≈ 0.069**, independent of r.
At large r, μ → q and α_CP → sin²(2πs)/(4πq), which has a
fixed solution.


### F3. Charge verified — Q = −e for all r

The charge-producing AC modulation leaks through the Compton
window; the analytical charge integral is:

    Q = −ε₀ E₀ × 2πaR × sin(2πs) / q_eff

This yields Q/e = −1.000000 at all tested r (by construction).
Numerical integration on a 256×512 grid validates to 0.3%:

| r    | Q_analytic / e | Q_numerical / e | Error   | R (m)       | a (m)       |
|------|----------------|-----------------|---------|-------------|-------------|
| 1.00 | −1.000000      | −0.997495       | 0.25%   | 8.411×10⁻¹³ | 8.411×10⁻¹³ |
| 2.00 | −1.000000      | −0.997383       | 0.26%   | 7.707×10⁻¹³ | 1.541×10⁻¹² |
| 4.00 | −1.000000      | −0.997350       | 0.27%   | 7.520×10⁻¹³ | 3.008×10⁻¹² |
| 8.00 | −1.000000      | −0.997342       | 0.27%   | 7.472×10⁻¹³ | 5.978×10⁻¹² |


### F4. Radiation pressure is unipolar, charge pattern depends only on θ₂

The outward radiation pressure P ∝ E₀(1 + cos(q_eff θ₂)) is
always ≥ 0.  No field passes backward through the sheet.

The charge-producing part (the AC modulation) has **no θ₁
dependence**: σ = ε₀ E₀ cos(q_eff θ₂) is uniform around the
tube cross-section at each ring position.

On the unrolled sheet, the pressure pattern is **horizontal
bands** (constant along the θ₁ axis), not the diagonal
stripes of the scalar model.  There are ~2 oscillations per
ring revolution (q_eff ≈ 1.93).

This means:
- No north/south asymmetry (inner vs outer equator)
- Charge zeros are ring-direction features (specific θ₂ values)
- A slot at a given θ₂ affects ALL tube positions equally


### F5. Ghost (1,1) mode

The ghost also has n₁ = 1, so the same CP cancellation applies.
Its field is E₀_ghost (1 + cos((1−s) θ₂)) — same unipolar
structure but with q_eff ≈ 0.93 instead of ≈ 1.93.

| r    | q_eff (ghost) | Q_ghost / Q_electron | m_ghost / m_e |
|------|---------------|----------------------|---------------|
| 1.00 | 0.935         | 1.641                | 0.629         |
| 2.00 | 0.932         | 1.509                | 0.530         |
| 4.00 | 0.931         | 1.459                | 0.495         |
| 8.00 | 0.931         | 1.445                | 0.485         |

The ghost produces 45–64% more charge per unit energy than the
electron.  Discrimination is purely a θ₂ phenomenon:

- Electron: ~2 oscillations per ring revolution (q_eff ≈ 1.93)
- Ghost: ~1 oscillation per ring revolution (q_eff ≈ 0.93)

The zero crossings are at **different θ₂ positions**, enabling
position-selective filtering via a slot.


### F6. B field is tangential, 90° out of phase with E_n

B_t = (E₀/c) sin(q_eff θ₂) is tangential to the surface
(along the geodesic direction) and spatially 90° out of phase
with the AC component of E_n.  Where the charge modulation is
maximum, B is zero, and vice versa.

Energy partition confirms CP equipartition:

| r    | ⟨E_n²⟩/E₀² | ⟨B_t²⟩c²/E₀² |
|------|-------------|---------------|
| 1.00 | 0.4852      | 0.5148        |
| 2.00 | 0.4846      | 0.5154        |
| 4.00 | 0.4845      | 0.5155        |
| 8.00 | 0.4845      | 0.5155        |

Both are ≈ 0.5 (slight departure from exactly 0.5 because
q_eff is not exactly an integer).


---

### Track 1 outputs

| File | Contents |
|------|----------|
| `outputs/track1_data.npz` | Unipolar + AC field arrays, geometry, for all r |
| `outputs/track1_En_map_electron.svg` | Three-panel: heatmap + geodesic + resonant waveform |
| `outputs/track1_En_map_ghost.svg` | Same for (1,1) ghost mode |
| `outputs/track1_alpha_comparison.svg` | s_CP vs s_scalar across r |


---

## Summary table

| # | Finding |
|---|---------|
| F1 | CP α formula: α = μ sin²(2πs)/(4πq²) — differs from scalar by 1/r² |
| F2 | CP shear converges to s ≈ 0.069 at large r (scalar shear → 0) |
| F3 | Charge Q = −e verified analytically and numerically at all r |
| F4 | Unipolar pressure, no θ₁ dependence — horizontal bands on sheet |
| F5 | Ghost (1,1) discrimination persists; ~1 vs ~2 oscillations per revolution |
| F6 | B tangential, 90° out of phase with E_n; CP equipartition confirmed |
