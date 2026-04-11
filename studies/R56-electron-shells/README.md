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


## Track 6 (framed): Mode capacity of a torus — Ma overflow into S

### The question

How many orthogonal standing-wave modes can coexist on a
single Ma torus?  When that capacity is exceeded, where does
the next mode go — and at what energy cost?

### Why this is different from Tracks 1–5

Tracks 1–5 asked about packing physical objects in S.  This
track asks about **mode capacity in Ma** with overflow into S.
The electrons don't pack spatially — they fill up the available
orthogonal modes on a torus.  When the torus is "full" (no
unoccupied orthogonal modes remain), the next electron must
create its own torus at a different S location.

### Physical picture

A torus with geometry (ε, s, L_ring) supports standing-wave
modes labeled by (n_t, n_r).  Each mode is orthogonal to the
others (different winding numbers → linearly independent
standing waves).  Two electrons with opposite tube winding
(±n_t) occupy the same mode — that's the factor of 2.

At a given energy ceiling (set by the Coulomb binding at
radius r), only a finite number of modes have energy below
the ceiling.  This count IS the shell capacity.

When all modes below the ceiling are occupied, the next
electron has two options:

1. **Promote to a higher harmonic on the same torus** —
   costs the energy difference to the next mode above the
   ceiling.

2. **Slide apart in S** — create a new torus at a different
   location (larger radius, next shell), at a cost set by the
   Coulomb potential difference between shells.

The system chooses whichever costs less energy.  This is a
**lowest-energy routing problem** between Ma excitation and
S separation.

### Implications

**For electron shells:** at the Bohr radius r_n, the torus
has an energy ceiling from the Coulomb binding.  The mode
count below this ceiling should be n² (giving shell capacity
2n²).  When full, the next electron slides to r_{n+1}
because that costs less than promoting to the next Ma
harmonic.

**For charged ghost modes:** high harmonics on the e-sheet
(the "ghosts" from R53 Track 6) might not be populated
because it's cheaper to separate spatially than to excite
a higher mode.  This provides a PHYSICAL reason why only a
few charged modes are observed — the rest are energetically
uncompetitive with spatial separation.

**For nuclear structure:** the proton torus has its own mode
capacity.  Nuclear stability limits (iron-56 being the most
stable nucleus) might correspond to the p-sheet torus filling
its modes.  Beyond that capacity, adding nucleons costs more
than the nuclear binding provides.

### Method

1. At the Bohr radius r_n for shell n, compute the Coulomb
   binding energy: E_bind = Z²α² m_e / (2n²)

2. On the electron torus at geometry (ε_e, s_e), count all
   modes (n_t, n_r) with mode energy μ below the ceiling
   set by E_bind at that shell.

3. For each shell n: does the mode count equal n²?

4. Compute the energy cost of two alternatives for the
   (capacity+1)th electron:
   - Promote: energy of the next mode above the ceiling
   - Separate: Coulomb energy difference to the next shell
   Which is cheaper?  Does the cheaper option match what
   nature does (filling shells in the observed order)?

### What success looks like

If the mode count at each Bohr radius matches n², the shell
capacities 2n² = 2, 8, 18, 32 are DERIVED from the torus
geometry.  The Pauli exclusion principle becomes: "a torus
has finite mode capacity."  The shell structure becomes:
"overflow goes to the next shell because it's cheaper."

If the mode count doesn't match n² but does show a finite
capacity that increases with radius, the qualitative picture
(Ma overflow → S separation) is right even if the exact
numbers need refinement.

### Connection to ghost modes

The charged ghosts from R53 Track 6 (78 Q = ±1 spin-½ modes
below 2 GeV) are higher harmonics on the e-sheet torus.
If promoting to these harmonics costs more energy than spatial
separation, they're never populated in nature — the electron
prefers to slide apart rather than excite mode (1, 4) or
(1, 5).  This would resolve the ghost problem: the modes
EXIST on the torus but are EMPTY because spatial separation
is cheaper.

### Connection to nuclear limits

The p-sheet torus at L_ring_p = 4.45 fm has its own mode
capacity.  The nuclear scaling law n₅ = A fills proton-sheet
modes with increasing A.  At some A, the modes are full and
adding another nucleon costs more than it gains from nuclear
binding.  This should correspond to the iron peak (A ≈ 56)
— the most stable nucleus.

