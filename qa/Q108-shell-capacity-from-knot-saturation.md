# Q108. Shell capacity from knot saturation on torus geodesics

**Status:** Open — observational hypothesis
**Related:**
  [Q107](Q107-wave-translation-of-atomic-physics.md) (Ma/S translation),
  [Q105](Q105-atoms-as-cross-sheet-modes.md) (atoms as modes),
  R51 (compound eigenmode tests),
  R46 Track 5 (waveguide cutoff and mode filtering),
  R50 Track 3 (particle spectrum)

---

## 1. The observation

The (1,2) standing wave on a torus, visualized in the
torus lab, shows **2 nodes** (zero-crossings) along the
geodesic, creating 2 antinodes (energy peaks).  Higher
modes show more nodes — up to 8 observed in the
visualizer.

The first electron shell holds exactly **2 electrons**.
The (1,2) knot has exactly **2 antinodes**.

This may not be a coincidence.


## 2. The hypothesis

**A torus geodesic knot has a maximum number of energy
quanta it can hold.**  Each quantum is one wavelength
fitted into the geodesic path.  When the knot is full,
the next quantum must go to the next available knot
(a different geodesic with a different winding pattern).
The maximum capacity of each knot IS the shell capacity.

### How quanta fill a knot

The (1,2) geodesic has a fixed path length (one Compton
wavelength at the fundamental frequency).  Adding energy
quanta to this knot means fitting more wavelengths into
the same path:

| Quanta | Mode | Wavelengths on path | Ring antinodes |
|--------|------|--------------------:|---------------:|
| 1 | (1,2) | 1 | 2 |
| 2 | (2,4) | 2 | 4 |
| 3 | (3,6) | 3 | 6 |
| Z | (Z,2Z) | Z | 2Z |

Each quantum adds one charge (from the 2π winding),
doubles the antinode count, and increases the mode energy
by ~m_e.

### When the knot is "full"

At some critical number of quanta N_max, the knot cannot
hold another wavelength.  Possible saturation mechanisms:

**Waveguide cutoff.**  The tube acts as a waveguide.  As
more wavelengths are packed in, the effective transverse
wavelength decreases.  When it drops below the tube's
cutoff, the mode becomes evanescent — it can't propagate.
The cutoff depends on the tube diameter (aspect ratio ε).

**Mode crowding.**  At high quantum numbers, the antinodes
are closely spaced.  Adjacent antinodes of opposite phase
begin to interfere destructively.  The mode becomes
unstable — the energy prefers to reorganize onto a
different geodesic.

**Energy crossing.**  A higher knot (different geodesic)
becomes energetically cheaper than adding another quantum
to the current knot.  The shell "closes" not because the
knot physically can't hold more, but because it's cheaper
to start a new knot.

**Lattice resolution (ζ = 1/4).**  The GRID lattice has a
minimum resolvable spatial frequency.  When the antinode
spacing drops below ~4 lattice spacings (the Nyquist
limit from ζ = 1/4), the lattice can't distinguish
adjacent antinodes.  The mode effectively saturates.


## 3. The knot sequence

If the first shell is the (1,2) knot with capacity 2,
what are the subsequent knots?  The electron sheet's
allowed geodesics are (1, n₂) modes (n₁ = 1 fixed for
charge).  The waveguide cutoff requires n₂ ≥ 2 (at
ε_e ≈ 0.65, the (1,1) ghost is killed).

The available charged knots on Ma_e:

| Knot | Ring windings | Fundamental antinodes | Path length ratio |
|------|-------------|----------------------|-------------------|
| (1,2) | 2 | 2 | 1.00 |
| (1,3) | 3 | 3 | ~1.12 |
| (1,4) | 4 | 4 | ~1.22 |
| (1,5) | 5 | 5 | ~1.30 |
| (1,6) | 6 | 6 | ~1.37 |

Each knot is a different geodesic on the torus with a
different path length and a different number of
fundamental antinodes.

### The key question

Can the knot sequence and saturation capacities reproduce
the electron shell filling:

| Shell | Electrons | Cumulative Z | Standard source |
|-------|----------|-------------|-----------------|
| 1 | 2 | 2 | 1s² |
| 2 | 8 | 10 | 2s² 2p⁶ |
| 3 | 8 | 18 | 3s² 3p⁶ |
| 4 | 18 | 36 | 4s² 3d¹⁰ 4p⁶ |
| 5 | 18 | 54 | 5s² 4d¹⁰ 5p⁶ |
| 6 | 32 | 86 | 6s² 4f¹⁴ 5d¹⁰ 6p⁶ |

The capacities are 2, 8, 8, 18, 18, 32 — following the
pattern 2n² for n = 1, 2, 2, 3, 3, 4.  The doubling
(each capacity appears twice) comes from the s+p filling
before d and f enter.


## 4. Learning the filter from the filling sequence

**Working backward:** if the shell capacities tell us
which knots are valid and how many quanta each holds,
the periodic table becomes a map of the torus geodesic
structure.

### What the capacities imply

**Shell 1 (capacity 2):** the (1,2) knot holds 2 quanta.
If the saturation mechanism is tied to the fundamental
antinode count (2 antinodes = 2 slots), this suggests
**one quantum per fundamental antinode** as the rule.

**Shell 2 (capacity 8):** if the rule is "one quantum per
fundamental antinode," the second knot must have 8
fundamental antinodes.  That would be the (1,8) geodesic —
8 ring windings.  Or: the capacity includes a degeneracy
factor.  If the second knot is (1,4) with 4 fundamental
antinodes, and each antinode holds 2 quanta (spin up +
spin down from the tube winding orientation), then
capacity = 4 × 2 = 8.

This gives the rule:

> **Shell capacity = 2 × (fundamental antinodes of the
> knot)**

For (1,2): 2 × 2 = 4?  But shell 1 holds 2, not 4.

Unless: the (1,2) knot has only 1 independent antinode
(the two antinodes are related by the torus symmetry —
they are the same standing wave sampled at two points,
not two independent slots).  Then capacity = 2 × 1 = 2. ✓

For (1,4): 4 ring antinodes, but how many are independent?
If the (1,4) mode has 4-fold ring symmetry, the
independent antinodes might be 4/1 = 4 (all independent
because they have different angular positions in 3D).
Capacity = 2 × 4 = 8. ✓

For (1,6) or whatever the third-shell knot is:
need 2 × N = 18, so N = 9 independent antinodes.  A
(1,9) knot?  Or (1,6) with some multiplicity?

The numbers don't yet produce a clean rule.  But the
approach — reading the knot structure FROM the shell
capacities — could work if the right counting scheme is
found.

### What the knot sequence implies for the filter

If the allowed knots on Ma_e are (1,2), (1,4), (1,6),
(1,9), ... (determined by which geodesics the torus
supports as stable standing waves), then:

- The waveguide cutoff determines the LOWEST knot (kills
  (1,1), passes (1,2))
- The knot saturation determines the CAPACITY per shell
- The knot sequence determines WHICH shells exist
- The torus geometry (ε_e, s_e) determines all of the
  above

**The periodic table would be a direct readout of the
electron torus geometry.**


## 5. How to test this

### Computational

1. **Visualize the antinodes.**  Use the torus lab to map
   the standing wave patterns for (1,2), (1,3), (1,4),
   (1,5), (1,6), ... on Ma_e.  Count the independent
   antinodes at each mode.  Compare to shell capacities.

2. **Compute the energy crossings.**  At what quantum
   number does adding to the (1,2) knot become more
   expensive than starting the (1,4) knot (or whatever
   the next knot is)?  This crossing point defines the
   shell closure.  Compare to the observed shell closures
   at Z = 2, 10, 18, 36, 54, 86.

3. **Sweep ε_e.**  The knot energies and saturation
   capacities depend on the aspect ratio.  Is there a
   specific ε_e where the crossings match the observed
   shell closures?  If so, ε_e is DETERMINED by the
   periodic table — not a free parameter.

4. **Check the proton sheet.**  The proton sheet (Ma_p)
   has its own knot structure.  Nuclear magic numbers
   (2, 8, 20, 28, 50, 82, 126) might correspond to
   knot saturation on the proton torus, the same way
   electron shells correspond to knot saturation on the
   electron torus.  If the same mechanism produces BOTH
   sets of magic numbers on their respective sheets, the
   case is very strong.

### Observational

5. **Does the filling order match the knot energy order?**
   The Aufbau principle (1s, 2s, 2p, 3s, 3p, 4s, 3d, ...)
   has a specific ordering that depends on screening.  If
   the knot energies on the torus produce the same
   ordering WITHOUT invoking screening, the torus geometry
   explains the Aufbau principle directly.

6. **Transition elements.**  The 3d shell fills AFTER 4s
   (not before, despite having lower principal quantum
   number).  In the knot picture, this means the (1, n₂)
   knot corresponding to 3d is slightly MORE expensive
   than the 4s knot at the relevant Z.  This inversion
   is a stringent test of the knot energy spectrum.


## 6. Connection to the proton mode question

The proton is the (1,3) mode on Ma_p (leading hypothesis).
The proton sheet's knot structure determines nuclear
shell closures.  If:

- Electron sheet: (1,2) → (1,4) → (1,6) → ... gives
  electron shells at 2, 8, 18, 32
- Proton sheet: (1,3) → (1,?) → (1,?) → ... gives
  nuclear shells at 2, 8, 20, 28, 50, 82, 126

Then the proton's (1,3) fundamental (with 3 ring windings
= 3 fundamental antinodes) and the electron's (1,2)
fundamental (with 2 ring windings = 2 fundamental
antinodes) would explain why the nuclear and electron
shell sequences are DIFFERENT — they live on tori with
different fundamental knots.


## 7. Why this could pin the geometry

Currently, ε_e and ε_p are free or weakly constrained
parameters.  If the knot saturation capacities depend on
ε, and the correct shell capacities (2, 8, 18, 32 for
electrons; 2, 8, 20, 28, 50, 82, 126 for nuclei) emerge
at SPECIFIC ε values, then:

- ε_e is determined by the electron shell sequence
- ε_p is determined by the nuclear shell sequence
- Both free parameters become PREDICTIONS of the periodic
  table and the nuclear chart

This would reduce model-D's effective free parameters
from 2 to 0 — the geometry is fully determined by
observed shell structure.


## 8. Caution

This is a hypothesis based on a visual observation
(antinodes in the torus lab) and a numerical coincidence
(2 antinodes ↔ 2-electron first shell).  No computation
has been performed.  The knot-saturation mechanism is
not specified (waveguide cutoff? crowding? energy
crossing?).  The connection between antinode count and
shell capacity is suggestive but not derived.

The hypothesis is falsifiable: if the torus mode spectrum
at any ε_e produces shell capacities that don't match
[2, 8, 18, 32], it's wrong.  If it matches, it's a
strong geometric prediction.

**Priority:** the computational tests in §5 (especially
items 1-3) are straightforward using existing tools
(torus lab, ma_model_d.py) and would quickly validate or
falsify the core claim.
