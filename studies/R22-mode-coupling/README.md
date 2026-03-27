# R22. Mode coupling and proton mass

**Questions:** Q16, Q26, Q32
**Type:** compute
**Depends on:** R21, R20, R19

## Background

On flat Ma_e (the electron sheet), each harmonic (n, 2n) has energy exactly n × m_e.  The
proton mass M = m_e + Σ n f(n) is determined entirely by the thermal
temperature T' ≈ 34 m_e, independent of the torus geometry (r, s).

On the embedded torus, position-dependent curvature modifies mode
energies.  The Sturm-Liouville eigenvalue for harmonic (n, 2n) with
n₂_eff = n(2−s) shifts from its flat value, breaking the exact
E(n)/E(1) = n scaling.  This makes the proton mass r-dependent —
potentially selecting a specific geometry.

Additionally, R23 identified θ₂-momentum conservation as a structural
obstacle for the phonon neutrino model.  The proposed rescue (proton
backreaction breaking θ₂ symmetry) requires checking whether the
energy density of harmonics on the curved torus is θ₂-dependent.


## Tracks

### Track 1: Curvature-corrected harmonic energies  ✓

Fourier-Galerkin spectral S-L solver (exact, no FD discretization error).
6 findings (F1–F6):

- Harmonics heavier: δ/n ≈ 0.26 ε² (F1–F2).
- Proton mass lighter: ΔM ≈ −53 m_e (r=3), −1 m_e (r=10) (F3).
- Correction monotonic, does not select r (F4).
- **θ₂ backreaction preserves symmetry → phonon neutrino ruled out (F5).**


### Track 2: Mode-mode coupling matrix  *(planned)*

Compute inter-mode coupling on the curved torus:
- Within each n₂ sector: curvature mixing (R21 basis change)
- Between sectors: electromagnetic? gravitational?
- Does coupling select a preferred harmonic spectrum?


### Track 3: Energy minimization and spectrum prediction  *(planned)*

Given the coupling matrix and curvature-corrected energies:
1. Find the energy-minimizing harmonic occupation at fixed total mass.
2. Does it predict m_p/m_e = 1836?
3. Is the spectrum unique or degenerate?


## Risk assessment

**Track 1: low risk.** Well-defined computation using R21 machinery.
The curvature correction is computable; the question is only its
magnitude and r-dependence.

**Track 2–3: medium risk.** The coupling mechanisms available
(within n₂ sectors only, per R23 F8) may be too limited to select
a unique spectrum.
