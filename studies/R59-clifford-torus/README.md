# R59: A self-consistent metric with time

**Status:** Complete — see [findings.md](findings.md) for outcomes
**Background:** [background.md](background.md)
**Review:** [review.md](review.md)
**Type:** theoretical + compute
**Depends on:** R55 (ℵ-mediated coupling), R54 (particle inventory),
  R53 (generations),
  [sim-impedance](../../grid/sim-impedance/) (charge from bending, Tracks 8–12),
  GRID (lattice substrate)

---

## Goal

Find a single metric that simultaneously:

1. **Predicts the known particle spectrum** (model-E already
   does this with the flat 6D Ma metric + internal shears)
2. **Models the Ma-St coupling correctly** at strength α = 1/137
   (R55 partially achieved this with ℵ mediation, 3.6% gap)

The key new element: **add the time dimension to the metric.**
Model-E and R55 used a purely spatial metric (6 Ma + 3 S, or
+1 ℵ). Without time, the only coupling mechanism available was
the 3D bending of the torus surface (R19, sim-impedance) or
ℵ-mediation (R55). Adding time opens the Kaluza-Klein coupling
mechanism: off-diagonal metric entries between Ma and t produce
the electromagnetic potential directly — in principle.

## Strategy

1. Start with the model-E flat Ma metric (which gives the
   correct particle spectrum)
2. Add time to the metric, making it (6 Ma + 3 S + 1 t = 10D),
   or 11D if ℵ is included
3. Introduce Ma-t off-diagonal entries (the KK coupling)
4. Determine whether these entries can be set to produce
   α = 1/137 universally — for electron, proton, and all
   charged modes
5. Check that the particle spectrum is not disrupted

If a single Ma-t entry (or a small number of entries) sets α
without disturbing the particle spectrum, we have a self-
consistent metric. If ℵ is needed, it adds one row/column. If
it's not needed, the metric is simpler.

## The coupling question (open)

Whether the coupling goes through ℵ (R55 approach), through
direct Ma-t entries (KK approach), or both, is an open question
at framing time. This study tests the time-based approach. If
it works without ℵ, that's the simpler solution. If ℵ is still
needed, the time dimension may still improve the 3.6%
universality gap from R55.

## EM as spacetime geometry (hypothesis)

A secondary question: if the Ma-t coupling produces the
electromagnetic field in St, does the resulting force reproduce
the Coulomb law via geodesic deviation? Specifically:

- Opposite Ma windings → fields cancel between charges →
  geodesics converge → **attraction**
- Same Ma windings → fields reinforce →
  geodesics diverge → **repulsion**

This would geometrize EM the same way Einstein geometrized
gravity. It is a hypothesis to be tested, not an assertion.

---

## Note on the flat metric (Clifford torus)

Model-E's particle spectrum uses a flat 2-torus metric for
each sheet. This is intrinsically the Clifford torus — no
bending, no self-intersection, any aspect ratio valid.

Model-E's charge and α mechanisms (R19, R48, sim-impedance)
use 3D embedding with bending. This study proposes to
replace those with the KK mechanism (Ma-t coupling), which
works on the flat metric directly. If successful, the 3D
embedding becomes a visualization aid, not physics.

See [background.md](background.md) for detailed discussion
of the Clifford torus, the 3D embedding problems, and the
relationship to model-E.

---

## What changes from model-E's 3D embedding

Model-E's particle spectrum uses a flat metric, but its charge
and coupling mechanisms use 3D embedding. R59 proposes to move
everything to the intrinsic flat geometry + KK coupling. The
table compares the two approaches.

| Feature | 3D visualization | Intrinsic (Clifford) | Type of change |
|---------|-----------------|---------------------|----------------|
| Extrinsic curvature | Nonzero (inner/outer) | Zero (flat) | Artifact removed |
| Self-intersection | Fails when a > R | Any aspect ratio valid | Artifact removed |
| Tube-ring mixing | cos(θ₁) factor | Zero | Artifact removed |
| Metric saturation | e-sheet at PD limit | No saturation | Artifact removed |
| EM from curvature | Not available | Hypothesis: Ma-St coupling → Coulomb | **New physics (R59)** |
| Time in metric | Absent | Included via KK | **New physics (R59)** |

---

## Open questions

1. **Does the Clifford embedding need ℵ?** R55 Track 3 used ℵ
   to mediate Ma-S coupling (3.6% universality gap). If the
   time dimension provides the coupling via KK reduction, ℵ
   may be redundant — or it may be the microscopic mechanism
   that the time-based coupling implements at the lattice
   scale. To be determined.

2. **Which circle couples to time?** If the torus embeds in
   spacetime, one circle is spatial and one involves time. Is
   it the tube (charge direction) or the ring (mass/frequency
   direction)? The KK picture suggests the tube couples to t
   (producing the electric potential g₅₀). But the ring might
   also couple (producing the magnetic potential).

3. **Where does α appear?** In KK theory (compact momentum
   model), α comes from the ratio of the compact dimension's
   size to the Planck length. Whether this carries over to
   MaSt (standing-wave model) is unknown. α might come from
   a Ma-t off-diagonal entry, from the ℵ-t entry, or from a
   different mechanism entirely. A single entry setting α
   would be the cleanest result.

---

## Tracks

### Track 1: Direct Ma-t coupling on model-E

Extend the model-E 6D Ma metric to 10D (6 Ma + 3 S + 1 t).
Introduce Ma-t off-diagonal entries. Tune σ so that a
mass-shell "α_eff" matches observed α. Check universality
across electron, proton, and other modes. Verify the particle
spectrum is not disrupted.

**Preliminary step:** verify that the model-E 6D Ma metric
(flat, with internal shears) produces the correct particle
spectrum before any coupling is added. This is a sanity
check, not a derivation — the flat metric is known to work.

### Track 1b: ℵ-mediated time coupling (11D)

Route the coupling through ℵ instead of directly: Ma ↔ ℵ ↔ t
chain on an 11D metric. Compare to Track 1's direct Ma-t
architecture. Test whether ℵ mediation improves the
universality gap or the mass-direction physics.

### Track 1c: Minimal single sheet

Strip the metric to a single electron sheet + ℵ + S + t. Test
both coupling architectures (D1 = direct ring-t, D2 =
ℵ-mediated) on this minimal system. Check whether the coupling
entries conflict with the particle-spectrum entries (tubes and
internal shear). Verify that generation structure is preserved.

### Track 1d: Two sheets (electron + proton)

Add the proton sheet to the minimal system. Test whether
cross-sheet coupling interferes or whether the two sheets
operate independently. Measure universality on the two-sheet
system and compare to single-sheet and full model-E results.

### Track 1e: Root-selection diagnostics

Investigate the sign-direction concern raised during Track 1
(apparent mass decrease under coupling). Three diagnostics:
(a) which quadratic root is "the particle" under a consistent
charge-sign definition, (b) whether the standard Coulomb
self-energy matches the mass-shell shift in magnitude, and
(c) whether flipping the metric signature convention changes
the sign.

### Track 3: Shear architecture test bed

Systematic test bed over a catalog of shear architectures. For
each, build the full N×N metric, check signature + spectrum
preservation, and extract α_eff via three complementary
measures: (a) mass-shell shift, (b) inverse-metric gauge, (c)
spatial coefficient.

Architectures: internal cross shear, Ma-S direct, ℵ-mediated
to S, ℵ-mediated to t, direct Ma-tube ↔ t, direct Ma-ring ↔ t
(at σ = α and σ = √α each).

No tuning — each architecture's α_eff is determined by its
input shears and model-E's geometry.

### Track 3b: Spatial field solve — the Coulomb test

Compute the spatial field δg_{Ma,t}(r) directly by solving
Poisson's equation in S for a localized source. Extract the
1/r coefficient at r ≫ L_Ma and compare to α × (source charge).
This is the definitive test that distinguishes mass-shell
α_eff from the Coulomb coupling.

Covers multiple architectures: direct Ma-t, ring-based
ℵ-mediation, tube-based ℵ-mediation on model-E, and
tube-based ℵ-mediation on a shearless clean metric.

---

## Visualization

The metric has 10+ dimensions. Visualization requires
dimensional compression: reduce S from 3D to 2D, showing
the compact or time dimension as height, color, or animation.
Based on the approach in viz/geodesic-curvature.

Relevant for illustrating geodesic convergence/divergence
if R59 reaches that point. Not needed for the core
mathematical/computational work.

**Rule:** derive analytically or compute numerically first;
visualize to confirm and communicate.

---

## Mathematical approach

New concepts needed (derived from scratch where used):

- **Lorentzian signature:** how time differs from space in the
  metric (−dt² vs +dx²) and what this means for geodesics
- **KK reduction:** how a higher-dimensional metric with compact
  dimensions produces gravity + gauge field in St. Standard
  KK assumes compact momentum; we must check what changes for
  standing waves
- **Linearized gravity:** metric perturbations from a source
  → geodesic deviation → force

---

## Files

| File | Purpose |
|------|---------|
| [background.md](background.md) | Detailed motivation and context |
| README.md | This framing document |
| [findings.md](findings.md) | Results, summary, and interpretations |
| [review.md](review.md) | Review notes on framing and execution |
| [scripts/](scripts/) | Computation scripts (per track) |
