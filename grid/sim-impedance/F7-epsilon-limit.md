# Track 7 Findings: The ε → 0 limit

Script: `scripts/verify_epsilon_to_zero.py`

---

## F1. Edge coincidence (2D-in-2D) goes to zero

Two triangular lattices rotated by 13.2°, counting cross-
lattice node pairs separated by 1 ± ε.

| ε | per node | rate/6 | 1/rate |
|:---:|:---:|:---:|:---:|
| 0.2000 | 2.8296 | 0.47160 | 2.1 |
| 0.1000 | 1.4444 | 0.24073 | 4.2 |
| 0.0500 | 0.6246 | 0.10411 | 9.6 |
| 0.0200 | 0.3148 | 0.05246 | 19.1 |
| 0.0100 | 0.1014 | 0.01690 | 59.2 |
| **0.0050** | **0.0430** | **0.00716** | **139.7** |
| 0.0020 | 0.0169 | 0.00282 | 355.0 |
| 0.0010 | 0.0092 | 0.00153 | 655.4 |
| 0.0005 | 0.0042 | 0.00070 | 1420 |
| 0.0002 | 0.0000 | 0.00000 | ∞ |
| 0.0001 | 0.0000 | 0.00000 | ∞ |

The rate decreases monotonically with ε.  At ε = 0.005, the
inverse rate happens to pass through ~140 (near 1/137), but
this is a point on a smooth curve, not a plateau or step.
Below ε = 0.0002, zero pairs survive — there are no exact
edge coincidences.

---

## F2. Node coincidence (2D-in-2D) is essentially zero

Same lattice pair, counting nodes within ε of each other.

| ε | hits | fraction |
|:---:|:---:|:---:|
| 0.2000 | 464 | 0.16338 |
| 0.1000 | 0 | 0.00000 |
| ≤ 0.05 | 0 | 0.00000 |

Below ε = 0.1, **zero** nodes from the rotated lattice
coincide with nodes from the original.  The two lattices are
completely incommensurate for node-to-node overlap at this
angle.  There is no regime where the rate plateaus — it drops
from 16% directly to zero.

---

## F3. Angular alignment (wye-jack) goes to zero

Fraction of orientations where at least one wye edge aligns
within tol° of a jack edge.

| tol (°) | fraction | 1/frac |
|:---:|:---:|:---:|
| 5.00 | 0.03648 | 27 |
| 2.00 | 0.00540 | 185 |
| 1.00 | 0.00145 | 690 |
| 0.50 | 0.00026 | 3797 |
| 0.20 | 0.00013 | 7594 |
| 0.10 | 0.00000 | ∞ |
| 0.05 | 0.00000 | ∞ |

The fraction decreases monotonically.  The 1/frac value
passes through 137 between tol = 2° and 5° (consistent with
Track 3's finding of ~2.2°).  Below 0.1°, zero orientations
show any alignment on the finite grid.  No exact alignment
exists at generic orientations because the fundamental angular
mismatch (120° vs 109.47°, the 19.47° barrier from Track 3)
prevents any wye edge from exactly matching a jack edge except
at isolated special orientations.

---

## F4. The tolerance problem

All three tests show the same pattern:

1. **The coincidence rate is a smooth, monotonically increasing
   function of ε.**  There are no plateaus, steps, or fixed
   points.

2. **At ε = 0, the rate is zero** (or effectively zero on a
   finite grid).

3. **Any target value — including 1/137 — can be obtained by
   choosing the appropriate ε.**  The tolerance at which
   1/frac ≈ 137 is different for each test:

   | Test | ε for 1/137 |
   |:---|:---:|
   | Edge coincidence | ε ≈ 0.005 (dimensionless) |
   | Angular alignment | tol ≈ 2.2° |
   | 4D node coincidence (Track 6.0) | δ ≈ 0.167 |

   Three different numbers, three different units, no common
   geometric origin.

This means the tolerance is not encoding a physical property
of the lattice junction — it is an arbitrary parameter.  The
"1/137" results from earlier tracks were not measurements of
a geometric constant; they were artifacts of the chosen
proximity threshold.

---

## F5. What this rules out

Track 7 seems to close the door on **coincidence-counting** as a
mechanism for deriving α:

- **Node coincidence** (Tracks 1, 6.0): the 2D hexagonal and
  3D/4D simplex lattices are incommensurate.  At generic
  orientations, no nodes coincide exactly.  The coincidence
  rate is proportional to the tolerance volume, with no
  geometric structure.

- **Edge/angular alignment** (Track 3): the 19.47° angular
  barrier between hexagonal (120°) and tetrahedral (109.47°)
  angles prevents exact alignment at most orientations.
  Single-edge alignments occur at isolated special
  orientations, but these do not propagate into lattice-wide
  patterns.

Combined with the per-junction results:

- **Per-junction quadratic coupling** (Tracks 4, 5, 6.1):
  killed by the spherical 2-design theorem.  The coupling
  sum is exactly constant at all orientations, in any
  Euclidean dimension, and under Lorentzian reinterpretation
  (η² = I).

**No static geometric property of the 2D/3D (or 2D/4D)
lattice junction produces a non-trivial, tolerance-
independent coupling fraction.**

---

## F6. What remains viable

The sim-impedance study has tested static junction geometry
exhaustively.  The following approaches remain **untested**
and could still provide a derivation of α:

### 1. Internal sheet geometry (wrapping/shear)

The material sheet is a triangular lattice wrapped into a
torus.  The wrapping is specified by four integers
(n₁, m₁, n₂, m₂) that determine:
- The aspect ratio ε (= R₁/R₂)
- The shear angle (relative twist of the two wrapping
  directions)

MaSt (R15, R19) already establishes a formula α(r, s)
relating the aspect ratio and shear to α.  If the shear
is determined by discrete wrapping integers, α would be a
number-theoretic constant of the sheet geometry — not a
continuous free parameter.

This is a property of the **sheet itself**, not the junction
between lattices.  sim-impedance did not test it.

### 2. Topological defect energy

GRID (A6, foundations.md) describes α as "the energy cost of
a minimal topological defect (vortex) relative to the natural
lattice energy scale."  This is a thermodynamic/action-based
quantity involving the lattice coupling constant κ = 1/(4πα).

A vortex is a region where the phase winds through 2π.  The
energy stored in the vortex field depends on how the phase
gradient distributes across the lattice — a question about
the lattice action, not static node positions.  This has not
been tested computationally in sim-impedance.

### 3. Dynamic wave propagation / scattering

A wave propagating on the 2D sheet hits a junction node where
the sheet meets the 3D lattice.  The scattering amplitude —
how much wave energy reflects, transmits into the sheet, or
radiates into the 3D lattice — depends on the wave equation
on both lattices and the boundary conditions at the junction.

This is a dynamic quantity that depends on wave frequency,
propagation direction, and the discrete structure of both
lattices.  It cannot be captured by static coincidence
counting or projection sums.  sim-impedance did not test it.

### 4. Multi-junction / collective effects

The 2-design theorem (Tracks 4, 5, 6.1) proves that
**single-junction** quadratic coupling is constant.  But
coupling measured over **many junctions** (an extended
interface between the sheet and the lattice) could show
interference, coherence, or cancellation effects that break
the single-junction symmetry.

Track 6.0's multi-node coincidence rate DID show orientation
dependence (CV = 0.49 in 4D), unlike the per-junction
measures.  However, Track 7 shows this orientation dependence
is still tolerance-dependent and goes to zero as ε → 0.

---

## F7. Summary

| Approach | Status | Outcome |
|:---|:---:|:---|
| Node/edge coincidence (Tracks 1, 3, 6.0, **7**) | Closed | Rate → 0 as ε → 0; any target value obtainable by choosing ε |
| Per-junction coupling (Tracks 4, 5, 6.1) | Closed | Constant at all orientations (2-design theorem + η² = I) |
| Internal sheet geometry (shear/wrapping) | **Open** | Untested by sim-impedance; existing MaSt connection (R15, R19) |
| Topological defect energy | **Open** | Untested; described in GRID A6 but not computed |
| Dynamic scattering at junctions | **Open** | Untested; requires wave equation, not static geometry |
| Multi-junction collective coupling | **Open** | Partially tested (6.0 shows orientation dependence but still ε-dependent) |

The central lesson of sim-impedance is: **the tolerance
parameter ε has no geometric justification.**  With no exact
coincidences between incommensurate lattices, any coincidence-
based measure requires defining "how close is close enough,"
and that definition is arbitrary.  The value 1/137 is not
privileged — it is one point on a smooth curve that passes
through every positive number as ε varies.

The viable pathways for deriving α involve mechanisms that
do not depend on a proximity threshold: the discrete
geometry of the sheet wrapping, the energy of topological
defects in the lattice action, or the scattering dynamics
of waves at lattice junctions.
