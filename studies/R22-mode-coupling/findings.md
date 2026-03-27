# R22 Findings

## Track 1: Curvature-corrected harmonic energies

**Script:** [`scripts/track1_curvature_corrected_proton.py`](scripts/track1_curvature_corrected_proton.py)


### F1. Curvature makes harmonics heavier relative to the electron

On the embedded torus, the cos/sin parity splitting lifts the
±n₁ degeneracy.  The electron (cos-like, lower energy) and the
uncharged harmonics (sin-like, higher energy per R21 F12) sit
on opposite sides of the split.  Since the splitting grows with
n₂_eff = n(2−s), harmonics have a larger fractional upshift than
the electron:

| r  | ε      | δ∞/n (ppm) | δ(n=10)    | δ(n=60)    |
|----|--------|------------|------------|------------|
| 3  | 0.333  | 29,100     | +0.292 m_e | +1.746 m_e |
| 4.29 | 0.233 | 7,480    | +0.075 m_e | +0.449 m_e |
| 6  | 0.167  | 2,467      | +0.025 m_e | +0.148 m_e |
| 10 | 0.100  | 583        | +0.006 m_e | +0.035 m_e |
| 20 | 0.050  | 115        | +0.001 m_e | +0.007 m_e |

δ(n) = E_curved(n,2n)/E_curved(1,2) − n.  All deviations are
positive: harmonics are heavier on the curved torus.


### F2. The deviation δ/n converges for large n

The fractional correction δ(n)/n approaches a constant δ∞/n
that depends only on ε (and weakly on s).  This convergence is
fast: δ/n is within 2% of its asymptotic value by n = 15.

The asymptotic correction scales approximately as ε²:

    δ∞/n ≈ 0.26 × ε²  (fit to data)

This is the cos/sin splitting divided by the total eigenvalue,
which is dominated by the kinetic term n² at large n.


### F3. The proton mass decreases with curvature

Heavier harmonics → lower Bose-Einstein occupation → the thermal
sum converges faster → the proton is lighter on the curved torus.

| r    | ε      | M_curved (m_e) | ΔM (m_e) | ΔM/M (%)  |
|------|--------|----------------|----------|-----------|
| 3.00 | 0.333  | 1783.1         | −53.0    | −2.89     |
| 4.29 | 0.233  | ~1821          | ~−15     | ~−0.8     |
| 6.00 | 0.167  | 1831.5         | −4.6     | −0.25     |
| 10.0 | 0.100  | 1835.1         | −1.1     | −0.06     |
| 20.0 | 0.050  | 1835.9         | −0.2     | −0.01     |

Using the flat-torus temperature T' = 33.87 m_e throughout.
The correction is smooth, monotonic, and scales as ~ε².


### F4. The curvature correction does not select a specific r

M(r) increases monotonically toward the flat value M_flat = 1836.15
as r → ∞.  There is no zero-crossing, extremum, or resonance.
At any r, the experimental proton mass can be recovered by a
small adjustment to T' (the thermal temperature).

The correction can be absorbed into a redefined T'(r):

    T'(r) > T'(∞) = 33.87 m_e

with T'(r) → T'(∞) as r → ∞.  This means the curvature
does NOT predict the proton mass.  The temperature T' remains
a free parameter (now r-dependent).


### F5. Backreaction preserves θ₂ symmetry — phonon rescue ruled out

Every mode on the embedded torus has wavefunction
ψ(θ₁,θ₂) = f(θ₁) exp(i n₂_eff θ₂), so the energy density
|ψ|² = |f(θ₁)|² is θ₂-independent.

For any statistical ensemble (thermal, BEC, or general mixture):

    ⟨ρ(θ₁,θ₂)⟩ = Σ_n f_occ(n) |f_n(θ₁)|²

which is purely a function of θ₁.  Therefore:

1. The proton's stress-energy is θ₂-independent.
2. Any elastic/gravitational backreaction preserves axisymmetry.
3. The n₂ quantum number remains exactly conserved.
4. Modes with different n₂ still cannot couple.

**This rules out the R23 F13 rescue path** (proton backreaction
breaking θ₂ to enable inter-n₂ coupling).  The phonon model
for the neutrino is dead at the mean-field level.


### F6. Remaining neutrino paths

With the phonon mechanism ruled out (R23 F8–F12, R22 F5),
the T² model's neutrino options are:

| Path | Mechanism | Status |
|------|-----------|--------|
| (a) Separate T² per flavor | Each neutrino on its own torus | Not yet explored |
| (b) Quantum fluctuations | Beyond-mean-field θ₂ breaking | Exponentially suppressed |
| (c) Multi-torus / T³ | Higher-dimensional topology | Not yet explored |
| (d) Moduli oscillation | Shape fluctuation + spin mechanism | Needs spin-½ construction |


## Summary table

| ID | Finding |
|----|---------|
| F1 | Curvature makes harmonics heavier: δ/n ≈ 29000 ppm (r=3), 583 ppm (r=10) |
| F2 | δ/n converges fast; scales as ~0.26 ε² |
| F3 | Proton mass decreases: ΔM ≈ −53 m_e (r=3), −1 m_e (r=10) |
| F4 | Correction monotonic in r; does not select geometry |
| F5 | θ₂ symmetry preserved by backreaction → phonon neutrino ruled out |
| F6 | Remaining neutrino paths: separate T², multi-torus, moduli oscillation |


## Scripts

| Script | Purpose |
|--------|---------|
| `track1_curvature_corrected_proton.py` | Spectral S-L solver, energy ratios, proton mass, θ₂ proof |
