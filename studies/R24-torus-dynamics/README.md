# R24. Torus dynamics — T³ structure and nonlinear mode selection

**Questions:** Q18 (α), Q14 (neutrino), Q16 (proton spectrum), Q32 (energy-geometry)
**Type:** compute/analytical  **Depends on:** R15, R19, R20, R21, R22, R23

## Motivation

Twenty-one studies have mapped the *static* landscape of Ma_e (the electron sheet): eigenvalue spectra,
charge formulas, harmonic decompositions.  Two problems remain stubbornly open:

1. **r-selection:** α(r,s) gives a one-parameter family.  Nothing selects r.
2. **Neutrino:** No viable mechanism on a single sheet.  Beating works kinematically
   but isn't selective; phonon coupling is forbidden by θ₂ symmetry.

Both problems have the same root cause: the model is **linear on a fixed geometry**.
Every eigenmode is equally valid; nothing prefers one configuration over another.

This study attacks both problems with two new approaches:

- **T³ structure:** The electron uses two of three material dimensions.
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
- L₃ ~ 250–1020 μm, independent of all Ma_e parameters
- Predicted Σm = 65–72 meV (below cosmological bound)
- System is over-determined (3 free params, 4 mixing observables)
  → r is predicted, model is falsifiable

Critical open: spin of (0,0,n₃) modes, sterile neutrino suppression.

## Track 2 — Nonlinear wave equation on embedded Ma_e  ✓

Pseudo-spectral simulation (64×64 grid, RK4 time integration) of the
wave equation on the embedded torus with optional cubic nonlinearity.

Key results (F8–F12):
- Linear impulse = eigenmode decomposition (confirmed, as expected)
- Curvature mixes θ₁ Fourier modes within each θ₂ sector (F9)
- Pulse position matters: outer vs inner equator excite different modes (F10)
- Defocusing nonlinearity (−λψ³) does NOT select modes (F11)
- At physical coupling λ = α, effect is negligible phase shifts only

Conclusion: impulse dynamics with simple self-repulsion cannot solve
the r-selection problem.  Mode selection needs either a focusing
interaction, dissipation, or external constraints (→ Track 1's T³
parameter over-determination may be the right path).

## Track 3 — Aspect ratio selection  ✗ (pre-empted)

Track 2 found no mode selection (F12): defocusing self-interaction
disperses rather than concentrates energy.  Track 3's premise — sweep
r for dynamically stable configurations — does not hold.

The viable r-selection path is through Track 1's over-determination:
the PMNS mixing matrix provides 4 constraints on 3 parameters (r, s₁₃, s₂₃).
Deriving this mapping would predict r without needing dynamics.

## Critical path forward

R24 is complete (Tracks 1–3).  The next steps are sequential:

1. **Spin gate (Q1):** Do (0,0,n₃) modes carry spin-½?  Analytical,
   not computational.  If spin-0, the T³ neutrino model fails.
2. **PMNS derivation (Q3):** Map (r, s₁₃, s₂₃) → mixing angles.
   Requires understanding the weak-interaction analog on T³.
3. **r prediction:** Solve the PMNS equations → r is determined.

This is a natural scope for a new study (R25) rather than Track 4,
because it requires different tools (analytical topology, group theory)
rather than the numerical simulation methods used here.
