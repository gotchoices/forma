# R25. Neutrino spin and 3-torus topology

**Questions:** Q14 (neutrino), Q18 (α via r-prediction)
**Type:** analytical/compute  **Depends on:** R24 (T1 F1–F7), R19, R2

## Motivation

R24 Track 1 showed that modes (0,0,n₃) on the third material dimension
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
[`../R24-torus-dynamics/neutrinos.md`](../R24-torus-dynamics/neutrinos.md),
angular momentum conservation in beta decay demands a fermion — no
combination of photons can close the spin budget.  If (0,0,n₃) modes
cannot carry spin-½, the model must still produce a neutrino from
somewhere.  Failure here closes the 3-torus neutrino path *and* reopens
the neutrino mechanism as a fundamental open problem.

## The spin problem — three candidate mechanisms

### Mechanism A: Winding on the (θ₂, θ₃) subplane

A mode (0, p, q) with p/q half-integer (e.g., (0,1,2)) would give
spin-½ by the same WvM mechanism that gives the electron spin-½.
It is uncharged (n₁ = 0).

**Problem:** Mass ~ m_e/r ≈ 100 keV, set by the small Ma_e dimension.
Far too heavy for a neutrino (need meV).

Track 1 will test whether any geometric arrangement makes this work:
- Could the θ₂ and θ₃ energy contributions cancel to give meV mass?
- With shear, is there a winding whose effective momentum is dominated
  by the large (θ₃) dimension?

### Mechanism B: Spin structure on the 3-torus

A flat 3-torus admits 2³ = 8 distinct spin structures, differing in the
boundary conditions for spinor fields: periodic (P) or anti-periodic (A)
in each direction.  On a (P,P,A) structure, spinor modes in θ₃
have half-integer quantum numbers: n₃ = ½, 3/2, 5/2, ...

**Problem:** The photon is a vector field (spin-1), not a spinor
(spin-½).  Vector fields always have periodic boundary conditions.
The spin structure affects spinors, not vectors.

Track 1 will check: is there a formulation where the photon's
polarization components behave as spinors under 3-torus periodicity?
(Relevant if the (1,2) winding already makes the electron a spinor —
the "vector-to-spinor conversion" might extend to the third dimension.)

### Mechanism C: Curvature-induced spin-orbit coupling

The embedded Ma_e has position-dependent curvature that couples the
photon's polarization (helicity) to its orbital motion (R21).  This
is what gives the electron spin-½.  If the third dimension is coupled
to Ma_e through the embedding geometry, modes along θ₃ might
acquire an effective spin through polarization–geometry coupling.

**Problem:** The coupling scales as ε₃ = L₁/L₃ ~ 10⁻⁸.  Any spin
contribution would be negligibly small.

Track 1 will compute the actual magnitude of this coupling to confirm.

## Track 1 ✓ — Spin analysis  *(complete — negative result)*

All three mechanisms tested.  All fail.

- **A:** Wavevector of (0,0,n₃) is purely along θ₃ regardless of
  shear (reciprocal lattice is perpendicular to Ma_e).  No spin.
- **B:** Spin structures affect spinors, not vectors.  Inapplicable.
- **C:** Curvature mixing amplitude ~10⁻⁹.  Negligible.

**Central finding (F4):** The charge-spin linkage.  Both charge
(n₁ = ±1 required) and spin-½ (n₁ odd required) are controlled
by the tube winding number n₁.  "Uncharged" (n₁ = 0) and "fermion"
(n₁ odd) are mutually exclusive.  The WvM mechanism cannot produce
uncharged fermions.

See [`findings.md`](findings.md) for full analysis (F1–F7).

## Track 2 ✗ — PMNS matrix  *(cancelled)*

Depended on Track 1 producing a viable spin-½ mechanism.
Track 1 returned a structural negative: the charge-spin linkage
makes uncharged fermions impossible in the WvM framework.
PMNS derivation has no target.
