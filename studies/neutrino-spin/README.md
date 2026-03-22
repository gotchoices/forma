# R25. Neutrino spin and T³ topology

**Questions:** Q14 (neutrino), Q18 (α via r-prediction)
**Type:** analytical/compute  **Depends on:** R24 (T1 F1–F7), R19, R2

## Motivation

R24 Track 1 showed that modes (0,0,n₃) on the third compact dimension
are kinematically viable neutrinos: automatically uncharged, with a
parameter-free mass-squared ratio matching experiment to 0.03σ, and an
over-determined system that would predict r.

But there is a critical gate: **spin.**

Neutrinos are spin-½ fermions.  In the WvM model, spin-½ arises from
the photon's helicity (±1) projected along a (1,2) geodesic — the
1:2 winding ratio yields the factor ½.  A pure (0,0,n₃) mode has
no winding in two dimensions.  It is a standing wave along a single
direction.  The WvM mechanism gives it spin-0, not spin-½.

The spin requirement is not optional.  As documented in
[`../torus-dynamics/neutrinos.md`](../torus-dynamics/neutrinos.md),
angular momentum conservation in beta decay demands a fermion — no
combination of photons can close the spin budget.  If (0,0,n₃) modes
cannot carry spin-½, the model must still produce a neutrino from
somewhere.  Failure here closes the T³ neutrino path *and* reopens
the neutrino mechanism as a fundamental open problem.

## The spin problem — three candidate mechanisms

### Mechanism A: Winding on the (θ₂, θ₃) subplane

A mode (0, p, q) with p/q half-integer (e.g., (0,1,2)) would give
spin-½ by the same WvM mechanism that gives the electron spin-½.
It is uncharged (n₁ = 0).

**Problem:** Mass ~ m_e/r ≈ 100 keV, set by the small T² dimension.
Far too heavy for a neutrino (need meV).

Track 1 will test whether any geometric arrangement makes this work:
- Could the θ₂ and θ₃ energy contributions cancel to give meV mass?
- With shear, is there a winding whose effective momentum is dominated
  by the large (θ₃) dimension?

### Mechanism B: Spin structure on T³

A flat T³ admits 2³ = 8 distinct spin structures, differing in the
boundary conditions for spinor fields: periodic (P) or anti-periodic (A)
in each direction.  On a (P,P,A) spin structure, spinor modes in θ₃
have half-integer quantum numbers: n₃ = ½, 3/2, 5/2, ...

**Problem:** The photon is a vector field (spin-1), not a spinor
(spin-½).  Vector fields always have periodic boundary conditions.
The spin structure affects spinors, not vectors.

Track 1 will check: is there a formulation where the photon's
polarization components behave as spinors under T³ periodicity?
(Relevant if the (1,2) winding already makes the electron a spinor —
the "vector-to-spinor conversion" might extend to the third dimension.)

### Mechanism C: Curvature-induced spin-orbit coupling

The embedded T² has position-dependent curvature that couples the
photon's polarization (helicity) to its orbital motion (R21).  This
is what gives the electron spin-½.  If the third dimension is coupled
to the T² through the embedding geometry, modes along θ₃ might
acquire an effective spin through polarization–geometry coupling.

**Problem:** The coupling scales as ε₃ = L₁/L₃ ~ 10⁻⁸.  Any spin
contribution would be negligibly small.

Track 1 will compute the actual magnitude of this coupling to confirm.

## Track 1 — Spin analysis

For each mechanism (A, B, C):
1. Formulate the angular momentum of the mode's electromagnetic field
   on T³ with the given topology / boundary conditions
2. Compute the spin projection along the external symmetry axis
3. Determine whether spin-½ is achievable

This is primarily analytical but can be supported with numerical
calculation of angular momentum integrals on the embedded torus.

**Possible outcomes:**
- One mechanism gives spin-½ → proceed to Track 2
- All mechanisms fail → T³ neutrino model is dead at the spin gate;
  neutrino mechanism remains open (requires fundamentally new idea)
- Mechanism A works if we abandon the "pure (0,0,n₃)" assignment
  and accept modes with winding → changes the mass predictions from
  R24 T1 (may or may not still match experiment)

## Track 2 — PMNS matrix from T³ geometry  *(contingent on Track 1)*

If a viable spin-½ mechanism is found:
1. Identify how the neutrino modes couple to the charged leptons
   (the "weak interaction" in compact-dimension language)
2. The coupling matrix between 3 neutrino modes and 3 charged leptons
   defines the PMNS mixing matrix
3. Map (r, s₁₃, s₂₃) → (θ₁₂, θ₂₃, θ₁₃, δ_CP)
4. Solve: does a unique (r, s₁₃, s₂₃) reproduce all 4 observables?
5. If yes → r is predicted → α is fully derived → model is falsifiable

## Risk assessment

- **Track 1:** High risk.  All three mechanisms have identified
  difficulties.  The most likely outcome is negative (spin-0 for all
  candidate modes).  But a negative result is clean and closes the
  T³ neutrino path definitively.

- **Track 2:** High value but speculative.  Requires understanding
  the weak interaction analog on T³, which is not yet formulated.
  Depends entirely on Track 1 succeeding.
