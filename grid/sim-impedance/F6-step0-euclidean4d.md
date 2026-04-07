# Track 6 Step 0 Findings: Euclidean 4D node coincidence

Script: `scripts/track6_step0_euclidean4d.py`

---

## Setup

**4D lattice:** bipartite simplex lattice — each node connects
to 5 neighbors along directions of a regular 4-simplex (all
pairwise angles 104.48° = arccos(−1/4)).  Built by BFS from
origin to depth 16, yielding 27,501 nodes (extent ≈ 18 in
each dimension).  All nearest-neighbor distances = 1.000,
coordination number = 5 (verified).

**2D lattice:** hexagonal, edge length 1, 767 nodes
(n_rings = 15).  Embedded in a random 2D plane in R⁴.  Core
trimmed to ~187 nodes for boundary avoidance.

**Method:** for each orientation of the 2D plane (random
sampling on the Grassmannian Gr(2,4)), count how many hex
nodes fall within distance δ of any lattice node.  Report the
coincidence fraction = n_hits / n_hex_core.

---

## F1. The exact-coincidence plateau: 1/187

For all tolerances δ ≤ 0.05, the coincidence fraction is
exactly 0.005348 = 1/187 at every orientation tested.  This
means **exactly 1 hex node** (the shared origin, placed by
construction) sits on a lattice node.

No additional hex nodes land on the 4D lattice at tight
tolerance.  This is expected: a generic 2D hexagonal lattice
embedded at a random orientation in a 4D simplex lattice is
**incommensurate** — the hex lattice spacing and simplex
lattice spacing produce no accidental coincidences at generic
angles.  Only at special "magic" orientations (where the
lattices are commensurate) would additional exact matches
appear — but these magic orientations form a measure-zero set
on Gr(2,4).

This confirms the Track 3 insight: exact node coincidence is
a discrete, angular-selective phenomenon (only at magic
angles), not a smooth average.

---

## F2. Tolerance scaling: 1/137 at δ ≈ 0.167

As δ increases beyond 0.05, additional hex nodes fall within
tolerance of lattice nodes, and the coincidence fraction rises:

| δ (tolerance) | Mean fraction | 1/fraction |
|:---:|:---:|:---:|
| 0.010 | 0.005348 | 187.0 |
| 0.050 | 0.005348 | 187.0 |
| 0.070 | 0.005508 | 181.6 |
| 0.100 | 0.005588 | 178.9 |
| **0.150** | **0.006471** | **154.5** |
| **0.200** | **0.009733** | **102.7** |
| 0.250 | 0.017861 | 56.0 |
| 0.300 | 0.027914 | 35.8 |
| 0.500 | 0.183529 | 5.4 |

**1/fraction = 137 occurs at δ ≈ 0.167** (interpolated
between δ = 0.15 and 0.20).

This tolerance is 1/6 of the edge length.  It is not derived
from the theory — it is a free parameter, just as the 2.2°
tolerance in Track 3 was free.  The result is the same in
structure: "1/137 appears at a specific tolerance, but we have
no reason to pick that tolerance over any other."

---

## F3. 4D is sparser than 3D

A direct comparison at matched tolerances shows that the 4D
simplex lattice has significantly lower coincidence rates than
the 3D diamond lattice:

| δ | 3D (1/frac) | 4D (1/frac) | 4D/3D ratio |
|:---:|:---:|:---:|:---:|
| 0.05 | 157 | 185 | 1.18× |
| 0.10 | 106 | 180 | 1.70× |
| 0.15 | 62 | 140 | 2.26× |
| 0.20 | 36 | 100 | 2.76× |
| 0.30 | 14 | 34 | 2.48× |

The 4D lattice produces 1.2–2.8× fewer coincidences than the
3D lattice at the same tolerance.  This is geometrically
expected: a 2D surface in 4D has two "extra" dimensions to
miss, versus one extra dimension in 3D.

**At δ = 0.15:** the 3D result is 1/62 (far from 137), while
the 4D result is 1/140 (close to 137).  The dimensional
effect alone moves the coincidence rate from the wrong ballpark
into the right one.

---

## F4. Orientation dependence exists

At δ = 0.15 over 1000 random orientations:

| Quantity | Value |
|:---:|:---:|
| Mean fraction | 0.006904 |
| Std deviation | 0.003367 |
| CV (std/mean) | 0.49 |
| Min fraction | 0.005348 (= 1/187, origin only) |
| Max fraction | 0.026738 (= 5/187) |
| 1/mean | 144.8 |

**The coupling IS orientation-dependent** (CV = 0.49 is large).
This is a crucial difference from Tracks 4–5, where the
per-junction coupling was exactly constant due to the 2-design
symmetry of the regular simplex.

The multi-node lattice coincidence rate DOES vary with the
orientation of the 2D plane in 4D, even in Euclidean geometry.
This is because lattice coincidence involves the PERIODICITY
of both lattices (a many-node property), not just the local
junction geometry (a single-node property).

Most orientations give the minimum (only the origin matches).
A minority of orientations give additional coincidences,
pulling the mean above the minimum.

---

## F5. What this means

### The good news

1. **The dimensional effect is significant.**  Going from 3D
   to 4D moves the coincidence rate from ~1/60 toward ~1/145
   at moderate tolerance — into the range of 1/137.

2. **Orientation dependence exists.**  Unlike the per-junction
   deadlock (Tracks 4–5), the multi-node coincidence rate
   varies with orientation.  This means the torus integral
   (averaging over the torus surface's orientation sweep)
   would give a specific, geometry-dependent value.

3. **1/mean ≈ 145 at δ = 0.15 is provocatively close.**  The
   Euclidean 4D result is in the right order of magnitude
   without any Lorentzian corrections.

### The bad news

4. **The tolerance is still a free parameter.**  1/137 appears
   at δ ≈ 0.167, but there is no theoretical reason to select
   this value.  This is the same problem as Track 3 (where
   1/137 appeared at 2.2° tolerance).

5. **Exact coincidence gives only the trivial hit.**  At δ → 0,
   the only coincidence is the shared origin — which exists by
   construction, not by geometry.  The coincidence fraction at
   exact matching scales as 1/N (system-size dependent), not
   as a geometric constant.

6. **The lattice may still be too small.**  With ~187 hex nodes
   in the core and ~16,500 lattice nodes, statistical
   resolution is limited.  Larger systems would improve the
   statistics but not change the structural conclusion: at
   generic orientations, exact coincidences beyond the origin
   are absent.

### Assessment

The coincidence counting approach — in both 3D and 4D —
produces 1/137 at a tunable tolerance but does not DERIVE
the tolerance.  The tolerance is analogous to the coupling
bandwidth in a waveguide junction: it determines what counts
as "close enough" to couple.

**Possible resolution:** in GRID, the lattice is discrete
and all edges are exactly L.  Two nodes either coincide
(distance = 0) or they don't.  The "tolerance" in this
computation proxies for the coupling range of the defect
cost — how far a phase twist can extend its influence.  If
the defect's influence range is ~L/6 (≈ 0.167 L), the
coincidence fraction is 1/137.

This connects back to the impedance mismatch framing:
α = 1/137 is the fraction of defect energy that the ambient
lattice absorbs.  The "coupling range" δ/L ≈ 1/6 may be
derivable from the lattice action (the ζ = 1/4 scattering
rule and the defect structure).

---

## F6. Next steps

1. **Lorentzian 4D (Steps 1–5):** The Lorentzian signature
   breaks the Euclidean 4-simplex symmetry.  The timelike
   direction distinguishes some planes from others.  This
   could shift the mean from 1/145 to 1/137 at the same
   tolerance, or it could introduce a NATURAL tolerance scale
   (from the metric signature).

2. **Larger system test:** Increase depth to 20+ and n_rings
   to 30+ to verify the δ = 0.15 result is stable.  Check
   whether the fraction stabilizes or drifts with system size.

3. **Magic orientation search:** Instead of random orientations,
   systematically search for orientations where the hex lattice
   IS commensurate with the 4D lattice (exact coincidence
   beyond the origin).  Count how many such orientations exist
   in Gr(2,4) and compute their measure.

4. **Derive δ from lattice physics:** Compute the defect's
   influence range from the lattice action with κ = 1/(4πα).
   If it gives δ/L ≈ 0.167, the circle is closed.

---

## F7. Comparison across all tracks

| Track | Dimension | Method | Result | 1/137? |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 2D→2D | Rotation coincidence | ~1/20 | No |
| 3 | 2D→3D | Edge alignment | 1/137 at 2.2° tol | Free parameter |
| 4 | 2D→3D | cos² projection | Constant 4/3 | Dead (2-design) |
| 5 | 2D→3D | Coherent transfer | Constant T=2 | Dead (2-design) |
| **6.0** | **2D→4D** | **Node coincidence** | **1/137 at δ≈0.17** | **Free parameter (but close at δ=0.15)** |

The progression: 2D→3D gives ~1/60 (too low), 2D→4D gives
~1/145 (in range).  The dimensional effect accounts for about
half the needed reduction.  Whether the remaining factor comes
from the Lorentzian signature or from the lattice action
coupling constant is the open question for Steps 1–5.
