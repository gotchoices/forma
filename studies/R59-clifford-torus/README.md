# R59: A self-consistent metric with time

**Status:** Framed
**Background:** [background.md](background.md)
**Type:** theoretical + compute + visualization
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
+1 ℵ).  Without time, the only coupling mechanism available was
the 3D bending of the torus surface (R19, sim-impedance) or
ℵ-mediation (R55).  Adding time opens the Kaluza-Klein coupling
mechanism: off-diagonal metric entries between Ma and t produce
the electromagnetic potential directly.

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
consistent metric.  If ℵ is needed, it adds one row/column.
If it's not needed, the metric is simpler.

## The coupling question (open)

Whether the coupling goes through ℵ (R55 approach), through
direct Ma-t entries (KK approach), or both, is an open question.
This study tests the time-based approach.  If it works without
ℵ, that's the simpler solution.  If ℵ is still needed, the
time dimension may still improve the 3.6% universality gap
from R55.

## EM as spacetime geometry (hypothesis)

A secondary question, tested in Tracks 2 and 5: if the Ma-t
coupling produces the electromagnetic field in St, does the
resulting force reproduce the Coulomb law via geodesic
deviation?  Specifically:

- Opposite Ma windings → fields cancel between charges →
  geodesics converge → **attraction**
- Same Ma windings → fields reinforce →
  geodesics diverge → **repulsion**

This would geometrize EM the same way Einstein geometrized
gravity.  It is a hypothesis, not an assertion.  Tracks 2
and 5 test it.

---

## Note on the flat metric (Clifford torus)

Model-E's particle spectrum uses a flat 2-torus metric for
each sheet.  This is intrinsically the Clifford torus — no
bending, no self-intersection, any aspect ratio valid.

Model-E's charge and α mechanisms (R19, R48, sim-impedance)
use 3D embedding with bending.  This study proposes to
replace those with the KK mechanism (Ma-t coupling), which
works on the flat metric directly.  If successful, the 3D
embedding becomes a visualization aid, not physics.

See [background.md](background.md) for detailed discussion
of the Clifford torus, the 3D embedding problems, and the
relationship to model-E.

---

## What changes from model-E's 3D embedding

Model-E's particle spectrum uses a flat metric, but its charge
and coupling mechanisms use 3D embedding.  R59 proposes to move
everything to the intrinsic flat geometry + KK coupling.
The table compares the two approaches.

| Feature | 3D visualization | Intrinsic (Clifford) | Type of change |
|---------|-----------------|---------------------|----------------|
| Extrinsic curvature | Nonzero (inner/outer) | Zero (flat) | Artifact removed |
| Self-intersection | Fails when a > R | Any aspect ratio valid | Artifact removed |
| Tube-ring mixing | cos(θ₁) factor | Zero | Artifact removed |
| Metric saturation | e-sheet at PD limit | No saturation | Artifact removed |
| EM from curvature | Not available | Hypothesis: Ma-St coupling → Coulomb | **New physics (R59)** |
| Time in metric | Absent | Included via KK | **New physics (R59)** |

---

## Open questions (not asserted)

1. **Does the Clifford embedding need ℵ?**  R55 Track 3 used
   ℵ to mediate Ma-S coupling (3.6% universality gap).  If
   the time dimension provides the coupling via KK reduction,
   ℵ may be redundant — or it may be the microscopic
   mechanism that the time-based coupling implements at the
   lattice scale.  To be determined.

2. **Which circle couples to time?**  If the torus embeds in
   spacetime, one circle is spatial and one involves time.
   Is it the tube (charge direction) or the ring (mass/frequency
   direction)?  The KK picture suggests the tube couples to t
   (producing the electric potential g₅₀).  But the ring might
   also couple (producing the magnetic potential).

3. **Where does α appear?**  In KK theory (compact momentum
   model), α comes from the ratio of the compact dimension's
   size to the Planck length.  Whether this carries over to
   MaSt (standing-wave model) is unknown.  α might come from
   a Ma-t off-diagonal entry, from the ℵ-t entry, or from a
   different mechanism entirely.  A single entry setting α
   would be the cleanest result.

---

## Tracks

### Track 1: Build the metric with time

The core track.  Extend the model-E 6D Ma metric to include
St (3+1 spacetime), optionally ℵ.

Full metric dimensions:
- 6 compact (Ma) — flat, internal, unchanged from model-E
- 3 spatial (S) — flat
- 1 time (t) — Lorentzian signature (−dt²)
- 1 ℵ (open — include if needed, omit if not)

Total: 10D (or 11D with ℵ).

**Preliminary step:** verify that the model-E 6D Ma metric
(flat, with internal shears) produces the correct particle
spectrum before any coupling is added.  This is a sanity
check, not a derivation — the flat metric is known to work.

**The new element:** Ma-t off-diagonal entries.

In standard KK theory (which uses compact MOMENTUM, not
standing waves), the off-diagonal entries between a compact
dimension and t produce the electromagnetic potential.
Whether the same mechanism applies to MaSt's standing-wave
picture is unknown and is what this track tests.

Approach:
1. Write the general 10D metric with Ma-t entries
2. Derive the effective St equations of motion for a mode
   on Ma (our standing-wave particle, not a KK point particle)
3. Identify which entries produce the EM potential — if any
4. Determine where α appears and whether it can be set by
   a single entry (or a small number of entries)

If KK applies directly: α comes from the off-diagonal
Ma-t normalization.  If it doesn't: we learn what's
different about standing waves vs compact momentum, and
adjust.

### Track 2: Particle spectrum with Ma-St coupling

Verify that adding the Ma-St coupling doesn't break the
particle spectrum.

Model-E's spectrum uses the flat 6D Ma metric — it is
already correct.  Adding Ma-t entries perturbs this.

Tests:
- How large are the spectrum shifts from the Ma-t entries?
- Can they be compensated by small adjustments to ε_e, ε_p
  (as in R55 Track 4)?
- Does the universality gap improve vs R55's 3.6%?
  (Different coupling mechanism — may give different gap.)
- What PD constraints do the Ma-t entries introduce?
  (The flat metric has no saturation; but Ma-t entries
  add new off-diagonal load.)

### Track 3: Spatial field from the coupling (computation)

Track 1 tuned σ so that ΔE/E = α.  But ΔE/E is a global
(integrated) quantity — it doesn't tell us about the spatial
field profile in S.  Track 3 computes the actual field.

**Approach:** Start with a single electron sheet (model-C
style).  Compute the spatial field in S from TWO mechanisms:

A. **R19 mechanism (internal shear):** the mode's energy on
   the 3D-embedded torus has a component that extends into S.
   The R19 formula computes this.  Measure the field at
   various distances r.  This is the mechanism we trusted in
   model-C.

B. **Ma-t mechanism (time coupling):** the off-diagonal Ma-t
   entry produces a perturbation in S through the mass-shell.
   Compute the field at various distances r using the
   linearized 10D Green's function.

**Compare A and B:** do they give the same spatial profile
(1/r) and the same coefficient (α)?  If yes, the two
mechanisms are equivalent and we understand the coupling.
If not, we learn which one produces the actual Coulomb field.

**Acceptance criteria:**
- Produce a number that plays the role of α (not tuned to α)
- Show 1/r spatial dependence with the correct coefficient
- Derive the charge sign from mode structure
- If it fails: diagnose which step gives the wrong number

### Track 4: Comparison and assessment

Compare results to R55 and model-E:

| Criterion | Model-E | R55 (ℵ) | R59 (time) |
|-----------|---------|---------|-----------|
| Particle spectrum | ✓ | ~1.3% shift | ? |
| α universality | N/A (assumed) | 3.6% gap | ? |
| ν coupling | not modeled | 1.07α | ? |
| Charge mechanism | 3D bending | ℵ mediation | Ma-t coupling? |
| Free parameters | 4 | 5 (+ σℵS) | ? |

Decision: does this become a model-E update, a model-F,
or a dead end?

---

## Visualization

The metric has 10+ dimensions.  Visualization requires
dimensional compression: reduce S from 3D to 2D, showing
the compact or time dimension as height, color, or animation.
Based on the approach in viz/geodesic-curvature.

Relevant for Track 3 (geodesic convergence/divergence).
Not needed for Tracks 1-2 (primarily mathematical/computational).

**Rule:** Derive analytically first.  Visualize to confirm
and communicate.

---

## Mathematical approach

New concepts needed (derived from scratch where used):

- **Lorentzian signature:** how time differs from space in the
  metric (−dt² vs +dx²) and what this means for geodesics
- **KK reduction:** how a higher-dimensional metric with compact
  dimensions produces gravity + gauge field in St.  Standard
  KK assumes compact momentum; we must check what changes for
  standing waves
- **Linearized gravity:** metric perturbations from a source →
  geodesic deviation → force (for Track 3)

---

## Files

| File | Purpose |
|------|---------|
| [background.md](background.md) | Detailed motivation and context |
| README.md | This framing document |
| scripts/ | Computation scripts (per track) |
| findings.md | Results (after computation) |
