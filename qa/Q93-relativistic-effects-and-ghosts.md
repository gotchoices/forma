# Q93: Unexplored relativistic effects — ghost suppression, accuracy, and dark matter

**Status:** Open
**Related:**
  R33 (ghost mode selection),
  R41 (dynamic model — O(α²) corrections don't solve ghosts),
  R38 (fourth generation / resonance capture),
  R19 (shear-induced charge),
  R32 (running of α),
  Q77 (ghost suppression),
  Q34 (what selects r?)

---

## Motivation

The static flat-torus model predicts ~900 modes with physical charges
below 2 GeV versus ~40 observed particles.  After the R33 charge
selection rule (|n₁| = 1) and the R41 dynamic low-pass filter, ~4
modes per charged sheet survive as unexplained ghosts — most
critically the (1,1) boson at half the electron mass.

R41 showed the dynamic model is a conceptual advance but does not
solve the ghost problem quantitatively (FF = 0.46 for the (1,1)
ghost).  Several relativistic effects remain unexplored that could
either suppress ghosts, improve mass accuracy, or reinterpret the
ghost modes as physical (dark matter).

---

## Path 1: Geometric phase (holonomy) from the 3D embedding

The photon's polarization vector undergoes parallel transport along
its geodesic on the embedded torus.  On a curved surface, a vector
transported around a closed loop rotates by an angle proportional to
the enclosed Gaussian curvature.  The torus has positive curvature
on the outer equator and negative on the inner — different geodesics
enclose different net curvature.

If the holonomy for a given (n₁, n₂) winding is not a multiple of
2π, the mode destructively interferes with itself and is forbidden.
This is a topological selection rule depending on winding numbers and
aspect ratio.

**Key question:** Does the (1,2) fundamental have trivial holonomy
(mode allowed) while the (1,1) ghost has non-trivial holonomy (mode
forbidden)?

**Approach:** Compute the Gauss-Bonnet integral along each geodesic
class on the embedded torus at r = 8.906.  Tabulate the holonomy
angle modulo 2π for all low modes.

**Risk:** The total Gaussian curvature of the torus is zero (Euler
characteristic = 0).  A geodesic that covers the full surface
symmetrically will see zero net rotation.  The question is whether
specific winding classes cover asymmetric patches.


## Path 2: Coupling asymmetry to S (geometric projection factor)

Not all Ma modes project into 3D space equally.  A particle's
observable properties — charge, magnetic moment, ability to be
created in collisions — depend on the overlap integral between the
mode's field pattern on Ma and the geometry that projects into S.
A mode that projects weakly is effectively dark: it exists as a valid
eigenmode but cannot be excited by any process accessible in S.

R33 Track 8 computed the radiation efficiency (ω⁴ Larmor factor).
The geometric projection factor — how much of the mode's field
pattern sticks out into 3D — has not been computed systematically.

**Key question:** Does the (1,1) ghost couple to S much more weakly
than the (1,2) electron?

**Approach:** For each mode (n₁, n₂), compute the far-field EM
multipole expansion as seen from S.  The charge integral (R19) gives
the monopole; higher multipoles determine the full coupling strength.
Compare the total radiated power (or cross-section for
photo-production) across modes.

**Connection to dark matter:** See Path 6.


## Path 3: One-loop self-energy from KK modes

Quantizing the field on Ma × S gives mass renormalization from
virtual excitation of other KK modes.  Each mode receives a
correction:

    δm² ∝ α × Σ (contributions from other modes)

This is O(α) ≈ 0.7% — comparable to the structural prediction
errors (0.1–6%).  Different modes receive different corrections
depending on their coupling matrix elements.

R32 found naive KK running is catastrophic (157,000× SM), but
that sums over all modes equally.  With ghost suppression applied
self-consistently, the sum might be finite and useful.

**Key question:** Do one-loop corrections improve the 1–6% mass
prediction errors?

**Approach:** Regularize the KK sum (zeta-function or dimensional
regularization).  Compute δm² for the 12 canonical mode assignments.
Compare with observed masses.


## Path 4: Decay channels within Ma

The free-EM Lagrangian has no interactions, so all modes are stable.
The quantized theory has interactions (photon-photon scattering at
one loop, graviton exchange).  Some ghost modes might have
kinematically allowed decay channels into lower-energy modes on Ma.

A mode that decays in < 10⁻²⁵ s would never register as a particle.
Even without computing rates, a selection rule (which modes have
allowed decay channels?) could thin the spectrum.

**Key question:** Is the (1,1) ghost kinematically allowed to decay
into lower modes?

**Approach:** For each ghost mode, enumerate all pairs/triples of
lower modes that conserve charge, spin, and total energy (within the
mode linewidth).  If no decay channel exists, the mode is stable and
requires a different suppression mechanism.


## Path 5: 10D polarization structure

Maxwell's equations in 10D have 8 transverse polarizations, not 2.
Upon compactification on Ma, these split into 2 ordinary photon
polarizations in S and 6 internal polarizations on Ma.  On a flat
torus, all polarizations are degenerate.  The 3D embedding breaks
this degeneracy: polarizations parallel vs. perpendicular to the
torus surface see different boundary conditions.

This introduces new quantum numbers (polarization state) that the
current model ignores entirely.  Physical modes might require
specific polarization states, providing another filter.

**Key question:** Does polarization splitting break the degeneracy
between the (1,2) electron and the (1,1) ghost?

**Approach:** Solve the 10D Maxwell equation on the embedded torus,
tracking all 8 polarizations.  Compute the spectrum for each
polarization sector separately.


## Path 6: Ghost modes as dark matter / energy reservoir

**Moved to [Q94](Q94-compton-window-and-dark-modes.md).**

Q94 develops the "Compton window" hypothesis: the Ma sheet dimensions
define a resonant aperture into S, and modes that don't fit the window
have mass but are invisible — dark matter candidates AND a threshold
energy reservoir (connecting to Q85 and R35).  Ghost modes may be a
feature, not a bug.

---

## Priority

1. **Path 6** (dark modes / dark matter) — reframes the ghost
   problem as a prediction; see [Q94](Q94-compton-window-and-dark-modes.md).
2. **Path 2** (projection factor) — most concrete computation;
   directly quantifies the Compton window for Q94.
3. **Path 1** (holonomy) — clean selection rule, computable now.
4. **Path 3** (self-energy) — needs QFT machinery not yet built.
5. **Path 4** (decay channels) — needs QFT but kinematics alone
   might be informative.
6. **Path 5** (polarization) — most technically demanding; likely
   needs a dedicated study.
