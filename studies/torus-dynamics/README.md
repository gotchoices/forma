# R24. Torus dynamics — T³ structure and nonlinear mode selection

**Questions:** Q18 (α), Q14 (neutrino), Q16 (proton spectrum), Q32 (energy-geometry)
**Type:** compute/analytical  **Depends on:** R15, R19, R20, R21, R22, R23

## Motivation

Twenty-one studies have mapped the *static* landscape of T²: eigenvalue spectra,
charge formulas, harmonic decompositions.  Two problems remain stubbornly open:

1. **r-selection:** α(r,s) gives a one-parameter family.  Nothing selects r.
2. **Neutrino:** No viable mechanism on single T².  Beating works kinematically
   but isn't selective; phonon coupling is forbidden by θ₂ symmetry.

Both problems have the same root cause: the model is **linear on a fixed geometry**.
Every eigenmode is equally valid; nothing prefers one configuration over another.

This study attacks both problems with two new approaches:

- **T³ structure:** The electron uses two of three compact dimensions.
  Modes extending into the third dimension could be neutrinos.
  T³ has C(3,2) = 3 subplanes — matching three neutrino flavors.
  More parameters (5) but also more observables (α + neutrino sector ≥ 6),
  so the system may be over-determined → predictive.

- **Nonlinear dynamics:** Replace static eigenvalue analysis with time-domain
  simulation including the photon's self-interaction.  On a nonlinear system,
  an impulse selects specific stable configurations (attractors), potentially
  fixing r and the harmonic spectrum.

## Track 1 — T³ mode structure and neutrino flavors  ✓

Modes with n₁ = 0 are automatically uncharged (R19).  The lightest are
pure θ₃ modes (0,0,n₃) with m ∝ n₃/L₃.  The mass-squared ratio
(n_c²−n_a²)/(n_b²−n_a²) is determined by integers alone — parameter-free.

Key results (F1–F7):
- (7,10,42) matches the experimental ratio 33.60 to 0.03σ
- L₃ ~ 250–1020 μm, independent of all T² parameters
- Predicted Σm = 65–72 meV (below cosmological bound)
- System is over-determined (3 free params, 4 mixing observables)
  → r is predicted, model is falsifiable

Critical open: spin of (0,0,n₃) modes, sterile neutrino suppression.

## Track 2 — Nonlinear wave equation on embedded T²

Solve the time-dependent wave equation on the embedded torus:

    ∂²ψ/∂t² = c² Δ_T² ψ + V[ψ]

where V[ψ] includes self-interaction (Coulomb energy of the field).

Steps:
1. Spectral spatial discretization (Fourier basis on T²)
2. Time-stepping (RK4 or similar)
3. Start with localized impulse: Gaussian packet at (θ₁₀, θ₂₀)
4. Evolve and monitor: which modes grow, which decay, what survives

On the linear system (V=0), this reproduces eigenmode decomposition.
With V ≠ 0, mode coupling occurs and specific configurations may be
selected as attractors.

## Track 3 — Aspect ratio selection

If Track 2 shows mode selection, sweep over r to find which aspect
ratios produce stable configurations.  Compare with α constraint
from R19.  If a unique r emerges, the model becomes fully predictive.

## Risk assessment

- **Track 1:** Low risk, high value.  Straightforward mode enumeration.
  Main risk: T³ neutrino might not give correct mass splittings.
  Even a negative result narrows the landscape.

- **Track 2:** Medium risk.  The correct form of V[ψ] is not fully
  specified — is it electromagnetic self-energy, gravitational
  backreaction, or both?  Starting with the simplest (Coulomb) is
  defensible.  Risk: on a weakly nonlinear system (α << 1), mode
  selection may be too slow to observe numerically.

- **Track 3:** Depends on Track 2 succeeding.  Deferred.
