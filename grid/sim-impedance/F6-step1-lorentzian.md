# Track 6 Step 1 Findings: Lorentzian per-junction coupling

Script: `scripts/track6_step1_lorentzian.py`

---

## Setup

Three candidate lattice geometries tested:

- **Option A:** Euclidean regular 4-simplex (5 directions in R⁴,
  all pairwise Euclidean angles 104.48°), with coordinate 0
  reinterpreted as time under metric η = diag(−1,+1,+1,+1).

- **Option B:** 4 tetrahedral spatial edges (in coords 1,2,3,
  pairwise angles 109.47°) plus 1 purely timelike edge (coord 0,
  orthogonal to all spatial edges).  This is the "3D diamond +
  time axis" picture.

- **Option C:** Euclidean 4-simplex with a Lorentz boost applied
  (rapidity ξ = 0.5 in the t-x plane).  Intended to test
  whether a boost produces useful asymmetry.

For each option, the computation measures:
1. Whether Σ (ê · d_j)² is constant or varies (2-design test)
2. The projection matrix M, transfer efficiency T, and SVD
   as functions of wye orientation and timelike tilt
3. What fraction of energy couples into the timelike edge

---

## F1. Option A: Lorentzian reinterpretation preserves the 2-design

| Metric | Σ (ê · d_j)² | Constant? |
|:---:|:---:|:---:|
| Euclidean | 5/4 = 1.2500 | Yes (std = 0, CV = 0) |
| Minkowski | 5/4 = 1.2500 | Yes (std = 0, CV = 0) |

**Both sums are exactly constant at 1.25.**

This is a theorem, not a numerical accident.  The Minkowski
coupling sum is:

> Σ_j η(ê, d_j)² = ê^T η (Σ_j d_j d_j^T) η ê

For the Euclidean 2-design: Σ d_j d_j^T = (5/4) I.  Therefore:

> = (5/4) ê^T η² ê = (5/4) ê^T I ê = 5/4

since **η² = I** (the Minkowski metric is its own inverse).

**This means: ANY Euclidean spherical 2-design remains a
2-design under Lorentzian reinterpretation.**  The η² = I
identity guarantees it.  The Lorentzian signature does not
break the 2-design symmetry of the regular simplex.

Option A is dead — the per-junction coupling is constant at
ALL orientations, in both Euclidean and Minkowski metrics.

---

## F2. Option B: Spatial wye decouples from time

For a purely spatial wye (tilt = 0, the Ma sheet at fixed time):

| Quantity | Value | Varies? |
|:---:|:---:|:---:|
| Tr(MᵀM) | 4.0000 | No (std = 0) |
| T (transfer efficiency) | 2.0000 | No (std = 0) |
| SVD singular values | (√2, √2, 0) | No |
| Energy to 4 spatial edges | 100% | No |
| Energy to timelike edge | 0% | No |

**The spatial wye is completely orthogonal to the timelike
edge.**  All coupling goes to the 4 tetrahedral spatial edges,
reproducing exactly the Track 5 result (3D case).  The 3D
tetrahedron IS a 2-design, so the coupling is constant.

The timelike edge is invisible to a spatial wye.

### Effect of timelike tilt

When the wye plane tilts into the time direction (representing
a worldsheet — the Ma surface extending in time):

| Tilt | Tr(MᵀM) Eucl | Tr(MᵀM) Mink |
|:---:|:---:|:---:|
| 0° (spatial) | 4.00 | 4.00 |
| 15° | 4.39 | 4.31 |
| 30° | 5.37 | 5.21 |
| 45° | 7.31 | 7.11 |
| 60° | 10.56 | 10.70 |
| 75° | 15.00 | 15.30 |
| 90° (worldsheet) | 23.73 | 23.73 |

The coupling **increases** with tilt — the timelike edge adds
to the total projection power.  There is no dip to 1/137.
Tilting into time makes the coupling STRONGER, not weaker.

---

## F3. Option C: boost is ill-conditioned

The Lorentz boost creates vectors with wildly different
Euclidean norms (up to 6×), making the coupling sums
meaninglessly large and noisy (mean ≈ 12, range 1–39).
This option is not useful because the boost doesn't preserve
Euclidean lengths, and the resulting "simplex" is grossly
non-regular.

---

## F4. Why ALL per-junction approaches fail

Three independent symmetry arguments now close the door:

1. **Euclidean n-simplex is a 2-design** (theorem, all n):
   Σ (ê · d_j)² = (n+1)/n for any unit ê.  This kills all
   quadratic coupling measures for regular simplex lattices in
   any Euclidean dimension.

2. **η² = I preserves the 2-design** (F1 above):
   Lorentzian reinterpretation of the Euclidean simplex does
   not break the symmetry.  The Minkowski coupling sum is also
   constant.

3. **Spatial wye ⊥ timelike edge** (F2 above):
   If the physical lattice is "3D diamond + time axis"
   (Option B), a spatial Ma sheet sees only the 4 tetrahedral
   edges.  The 3D tetrahedron is a 2-design.  The timelike
   edge contributes nothing.

**No per-junction quantity — Euclidean or Lorentzian,
quadratic in the projection — can depend on the orientation
of a 2D sheet relative to a simplex lattice in any dimension.**

---

## F5. What survives

The per-junction coupling is constant.  But Step 0 showed that
the **multi-node lattice coincidence rate** DOES vary with
orientation (CV = 0.49 in 4D).  This is a lattice property,
not a junction property.  It involves the PERIODICITY and
COMMENSURABILITY of the two lattices — a many-body effect
that the 2-design theorem does not constrain.

Step 0 found the 4D coincidence fraction ≈ 1/145 at δ = 0.15,
close to 1/137.  The per-junction coupling is a constant
multiplier (T = 2) that scales every orientation equally.
The orientation-dependent part comes ONLY from the lattice
coincidence geometry.

**The path to α goes through the lattice, not through the
junction.**

---

## F6. Revised picture

The coupling between a 2D sheet and the 4D lattice factors as:

> α = (per-junction efficiency) × (lattice coincidence fraction)

- Per-junction efficiency: **constant** (= 2, or some
  normalization thereof).  Does not depend on orientation,
  dimension, or metric signature.

- Lattice coincidence fraction: **orientation-dependent**.
  Determined by the commensurability of the hexagonal lattice
  with the ambient lattice at each orientation.  The torus
  surface sweeps through orientations; the integral over the
  torus gives α.

Step 0 showed the lattice coincidence fraction is ~1/145 in
Euclidean 4D.  The remaining factor to reach 1/137 may come
from:
- The torus geometry (ε, specific orientation path)
- The Lorentzian metric's effect on lattice periodicity
  (not on per-junction coupling, but on which orientations
  are physically accessible)
- The lattice structure itself (A4 vs D4 vs other 4D lattices)
