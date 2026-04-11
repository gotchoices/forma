# R56: Electron shell structure from geometric packing

**Status:** Active — Tracks 1–5 complete
**Questions:** Can MaSt explain WHY electron shells have the
capacities they do (2, 8, 18, 32)?
**Type:** compute + theoretical
**Depends on:** R53 (electron Compton scale), model-E

---

## Motivation

Standard quantum mechanics derives shell capacities from
spherical harmonics and the Pauli exclusion principle.  Both
are axiomatic — the QM formalism says WHAT the numbers are
but not WHY.  MaSt provides a physical electron (a Compton-
scale torus, not a point) and topological quantum numbers
(tube winding = spin).  Can these produce shell structure
from geometry?

## Prior work

**LaFave (2014)** showed that the Thomson problem (minimizing
energy of N point charges on a fixed sphere) produces energy
irregularities matching the periodic table's shell-filling
pattern.  The key: discrete symmetry changes when going from
N to N+1 charges produce energy jumps at noble gas
configurations.  See [arXiv:1403.2591](https://arxiv.org/abs/1403.2591).

**Knot Physics** (knotphysics.net) derives Pauli exclusion from
the topology of fermion knots — same-winding knots
geometrically prevent co-occupation.  Structurally parallel
to MaSt's tube-winding picture.

LaFave takes shell radii as given from QM and has no
explanation for the factor of 2 (spin degeneracy).  Neither
framework derives shell structure from particle geometry.


## Tracks

### Track 1: Classical packing of distributed-charge electrons

**Status:** Complete — negative

Model each electron as a uniform spherical shell of charge −e
at the Compton radius.  Place N around a nucleus and minimize
total energy.  Two electron sizes tested (R = 751 fm from
model-E; R = 386 fm from reduced Compton).

**Result:** smooth energy landscape, no shell closure at 2, 8,
or 18.  Classical packing of distributed-charge electrons does
not produce shells.

### Track 2: Couplet packing

**Status:** Complete — weak positive, not definitive

An electron couplet = two electrons with opposite tube winding
(+1 and −1) at the same S coordinate.  Properties: charge −2e,
spin 0, magnetic moment 0 (a boson).  Pack couplets around a
nucleus with one couplet fixed at the origin as a core.

**Result:** weak structure in the energy progression; the
computation was noisy (optimizer issues).  The core+ring
geometry was later invalidated by Track 3b.

### Track 3: Diameter sweep

**Status:** Complete — clean data, false premise

Fix 1 core couplet at origin, place N ring couplets around it.
Use analytic equal-spaced ring (no optimizer noise).  Sweep
electron effective radius R_eff from 10 fm to 15,000 fm.

**Result:** the ratio ΔE_5/ΔE_4 = 0.50 at EVERY R_eff — a
geometric identity independent of electron size.  Shell closure
(6th couplet costs energy) occurs at 5 ring couplets = 10 ring
electrons.  But the core+ring assumption was shown to be wrong
by a 5-couplet configuration comparison: all couplets prefer
the same radius (triangular bipyramid), not a 1+4 layered
structure.

### Track 4: Free 3D couplet packing

**Status:** Complete — shells do not emerge

Free 3D basin-hopping optimization of N couplets around a
+2Ne nucleus (neutral atoms).  No assumed geometry.

**Result:** all couplets collapse to the same radius (~R_eff)
in polyhedral arrangements.  No two-shell structure.  The
uniform-sphere charge model has constant interior potential
(shell theorem), which erases radial differentiation.

### Track 5: Torus standing waves and orientation packing

**Status:** Complete — partial success

Reframe the question: instead of packing physical objects,
analyze standing waves of a torus orbiting a nucleus.

**Part A:** the Bohr quantization condition (2πr = nλ_dB)
gives the shell radii.  This is the same formula as standard
QM but reinterpreted: the electron is a physical torus fitting
integer wavelengths around the nucleus.

**Part B:** solid-angle packing of torus orientations at the
Bohr radius gives ~20,000 possible orientations at n=1 (vs
QM count of 1).  The torus is too small relative to the orbit
for physical packing to constrain the angular count.

**Part C:** the angular count n² comes from standing-wave
closure on a sphere — the constraint l < n (angular nodes
cannot exceed radial wavelengths).  This is the SAME closure
condition that quantizes modes on the Ma torus.

**Result — what MaSt adds:**
1. The factor of 2: derived from tube winding topology (±1)
2. The Bohr radii: physical torus fitting, not abstract wave
3. Unified closure condition: Ma quantization and S shell
   quantization are the same mechanism in different domains

**Result — what MaSt does not yet add:**
1. The n² angular count (spherical harmonics on S)
2. The Madelung filling order (4s before 3d)


## Other directions not yet pursued

**Thin-ring charge model:** A thin ring or torus of charge has
non-constant interior potential (unlike the uniform sphere)
and might produce radial differentiation in packing.  Deferred.

**Interference exclusion (Pauli from wave physics):** Two
co-located electron tori with the same tube winding might
destructively interfere on Ma, preventing co-occupation.
This would derive Pauli exclusion from standing-wave physics
rather than postulating it.  Theoretical, not yet attempted.

**Torus orientation quantization:** The electron torus at the
Bohr radius might have discrete stable orientations (like a
gyroscope in a gravitational field) that give the 1, 3, 5, 7
orbital counts.  Not yet modeled.
