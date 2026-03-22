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

## Track 1 — T³ mode structure and neutrino flavors

Enumerate modes on flat T³ with general lattice (3 radii, 3 shears).
Identify the electron's T² subplane.  Classify remaining modes by:
- Which subplane(s) they occupy
- Charge (only modes winding in θ₁ carry charge via R19 mechanism)
- Spin (winding topology → spin-½ requires (1, n₂) or equivalent)
- Energy scale

Key questions:
- Do modes on the (θ₁, θ₃) and (θ₂, θ₃) planes have zero charge?
- Can they carry spin-½?
- Does the mass spectrum depend on the third radius c in a way that
  could reproduce Δm²₃₁/Δm²₂₁ ≈ 33.6?
- How many free parameters remain after fitting α + neutrino masses?
  If mixing angles are predicted, the model is falsifiable.

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
