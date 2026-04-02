# R46 Findings: Electron filter — aperture effects on a toroidal cavity

Study: [`README.md`](README.md)

---

## Track 1. Baseline EM fields — vector model with circular polarization

Script: [`scripts/track1_baseline_fields.py`](scripts/track1_baseline_fields.py)

Uses the WvM circular polarization picture expressed as a vector
field on the full torus surface.  For a circularly polarized
photon with n₁ = 1, the E-field rotation matches the surface
normal rotation (one turn per tube circuit).  The θ₁ from the
mode phase cancels against the θ₁ from the geometric rotation,
giving fields that depend only on the ring angle θ₂:

    E_n(θ₁, θ₂) = E₀ cos(q_eff θ₂)    (normal to surface, outward)
    E_t(θ₁, θ₂) = E₀ sin(q_eff θ₂)    (tangent, ⊥ geodesic)
    B_t(θ₁, θ₂) = (E₀/c) sin(q_eff θ₂) (tangent, along geodesic)

where q_eff = n₂ − s.  This IS the n₁ = 1 selection rule
(R19 F17/F30) seen from the vector-field perspective.


### F1. The CP model produces a new α formula

Setting Q = e in the CP charge integral with KK normalization:

    α_CP  = μ sin²(2πs) / (4π q²)

where μ = √(1/r² + q²) and q = 2 − s.  Compare R19 scalar:

    α_R19 = r² μ sin²(2πs) / (4π q²)

The relationship is exact:  **α_CP = α_scalar / r²**.

At r = 1 (square torus), both formulas agree — the shear
required for Q = e is identical.  At larger r, the CP model
needs more shear because the circular-polarization charge
integral gives Q ∝ 1/r relative to the scalar integral
(the θ₁ cancellation removes a factor that helped the
scalar integral).


### F2. The CP shear converges to a fixed value at large r

| r    | s (scalar) | s (CP)    | s_CP / s_scalar | q_eff (CP) |
|------|------------|-----------|-----------------|------------|
| 1.00 | 0.064981   | 0.064981  | 1.000           | 1.935019   |
| 2.00 | 0.033515   | 0.067960  | 2.028           | 1.932040   |
| 4.00 | 0.016933   | 0.068823  | 4.065           | 1.931177   |
| 8.00 | 0.008497   | 0.069048  | 8.126           | 1.930952   |

The scalar shear goes to zero as r → ∞ (s_scalar ∝ 1/r).
The CP shear converges to **s ≈ 0.069**, independent of r.
This is because at large r, μ → q and α_CP → sin²(2πs)/(4πq),
which has a fixed solution s ≈ 0.069.

This is a strong prediction: in the CP model, the shear is
approximately the same for all aspect ratios.  The q_eff values
also converge (≈1.931), meaning the charge distribution pattern
is nearly r-independent.


### F3. Charge verified — Q = −e for all r

The analytical charge formula:

    Q = −ε₀ E₀ × 2πaR × sin(2πs) / q_eff

yields Q/e = −1.000000 at all tested r (by construction —
the shear was solved for this condition).  Numerical integration
on a 256×512 grid validates to 0.3%:

| r    | Q_analytic / e | Q_numerical / e | Error   |
|------|----------------|-----------------|---------|
| 1.00 | −1.000000      | −0.997495       | 0.25%   |
| 2.00 | −1.000000      | −0.997383       | 0.26%   |
| 4.00 | −1.000000      | −0.997350       | 0.27%   |
| 8.00 | −1.000000      | −0.997342       | 0.27%   |


### F4. Charge depends only on θ₂ — uniform around the tube

The most significant qualitative difference from the scalar
model: **σ has no θ₁ dependence**.  The charge density
σ = ε₀ E₀ cos(q_eff θ₂) is uniform around the tube
cross-section at each ring position.

On the unrolled sheet, the charge pattern is **horizontal
bands** (constant along the θ₁ axis), not the diagonal
stripes of the scalar model.  The charge is negative on the
half of the ring where cos(q_eff θ₂) < 0 and positive on
the other half, with ~2 oscillations per ring revolution
(q_eff ≈ 1.93).

This means:
- No north/south asymmetry (inner vs outer equator)
- Charge zeros are ring-direction features (specific θ₂ values)
- A slot at a given θ₂ affects ALL tube positions equally


### F5. Ghost (1,1) — same discrimination, different mechanism

The ghost also has n₁ = 1, so the same CP cancellation applies:

    E_n^ghost = E₀_ghost cos((1−s) θ₂)

| r    | q_eff (ghost) | Q_ghost / Q_electron | m_ghost / m_e |
|------|---------------|----------------------|---------------|
| 1.00 | 0.935         | 1.641                | 0.629         |
| 2.00 | 0.932         | 1.509                | 0.530         |
| 4.00 | 0.931         | 1.459                | 0.495         |
| 8.00 | 0.931         | 1.445                | 0.485         |

The ghost still produces 45–64% more charge per unit energy
than the electron (same conclusion as the scalar model, F5 in
the deleted findings).  But now the discrimination is purely a
θ₂ phenomenon:

- Electron: ~2 oscillations per ring revolution (q_eff ≈ 1.93)
- Ghost: ~1 oscillation per ring revolution (q_eff ≈ 0.93)

The zero crossings of electron and ghost are at **different
θ₂ positions**.  A slot at an electron zero will NOT be at a
ghost zero — this enables position-selective filtering.


### F6. B field is tangential, 90° out of phase with E_n

B_t = (E₀/c) sin(q_eff θ₂) is tangential to the surface
(along the geodesic direction) and spatially 90° out of phase
with E_n in the ring direction.  Where E_n is maximum (charge
peaks), B_t is zero, and vice versa.

The energy partition ⟨E_n²⟩ ≈ ⟨B_t²⟩c² ≈ 0.5 E₀² confirms
the equipartition expected for circular polarization.


### Track 1 outputs

| File | Contents |
|------|----------|
| `outputs/track1_data.npz` | E_n, E_t fields + geometry for both modes at r = 1, 2, 4, 8 |
| `outputs/track1_En_map_electron.svg` | E_normal heatmap (horizontal bands) |
| `outputs/track1_En_map_ghost.svg` | E_normal heatmap for ghost |
| `outputs/track1_charge_profile.svg` | σ vs θ₂ for both modes |
| `outputs/track1_alpha_comparison.svg` | s_CP vs s_scalar across r |


---

## Summary table

| # | Finding |
|---|---------|
| F1 | CP α formula: α = μ sin²(2πs)/(4πq²) — differs from scalar by 1/r² |
| F2 | CP shear converges to s ≈ 0.069 at large r (scalar shear → 0) |
| F3 | Charge Q = −e verified analytically and numerically at all r |
| F4 | E_n depends only on θ₂ — uniform around tube, horizontal bands on sheet |
| F5 | Ghost discrimination 45–64% persists; now purely a θ₂ pattern difference |
| F6 | B tangential, 90° out of phase with E_n; energy equipartition confirmed |
