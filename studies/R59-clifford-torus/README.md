# R59: A self-consistent metric with time

**Status:** Complete — negative result (Track 3b falsifies Ma-t = Coulomb)
**Background:** [background.md](background.md)
**Findings:** [findings.md](findings.md) — see §Track 3b and §R59 overall status
**Review:** [review.md](review.md)
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

### Track 3: Shear architecture test bed (complete)

Track 1 tuned σ so that ΔE/E = α.  But ΔE/E is a global
(integrated) quantity and the earlier Track 3 attempts did
not establish that this mass-shell shift IS the Coulomb
coupling.  The rebuilt Track 3 is a systematic **test bed**
over nine shear architectures.

**Approach:** For each architecture, build the full 10D (or
11D) metric from model-E's Ma block plus flat S, Lorentzian
t, and optional ℵ.  Overlay the architecture's shears at the
specified entries.  Then check:

1. **Metric signature** (exactly one negative eigenvalue for
   Lorentzian).  A broken signature disqualifies.
2. **Spectrum preservation** (electron and proton particle-
   root masses within 1% of model-E).
3. **α_eff extraction** via three complementary measures:
   - (a) mass-shell shift (E_particle − E_bare)/E_bare
   - (b) inverse-metric gauge extraction (KK-textbook)
   - (c) spatial coefficient of δg_{Ma,t}(r) at large r

No tuning — each architecture's α_eff is determined by its
input shears and model-E's geometry.

**Architectures tested:** internal cross shear, Ma-S, ℵ-
mediated to S, ℵ-mediated to t, direct Ma-tube ↔ t, direct
Ma-ring ↔ t (two magnitudes each).

**Key results:**
- Four of nine architectures break signature (F28).  The
  model-E metric is near the PD boundary; many cross-couplings
  push it over.
- Only Ma-ring ↔ t architectures preserve both signature and
  spectrum (F29).
- With σ = α at that slot, α_eff ≈ 0.87α for electron and
  0.85α for proton — universal to 1.8%, **without tuning**
  (F31).  This reproduces Track 1's result from a different
  angle.
- Measures (a) and (b) scale differently in σ (F30): (a) ~ σ,
  (b) ~ σ².  Cannot both be "the Coulomb α" — distinguishing
  them requires the spatial-field solve (Track 3b).

Track 3 thus narrows the mechanism to one surviving
architecture and defines the remaining ambiguity.

### Track 3b: Spatial field solve — the Coulomb test (complete)

The one test the test bed did not run: directly compute the
spatial field δg_{Ma,t}(r) in S sourced by a mode at origin,
and verify whether the coefficient of 1/r at r ≫ L_Ma
matches α × (source charge).

**Result: NEGATIVE.**  With Arch 7's σ = α plugged in, the
resulting α_Coulomb extracted from the 1/r coefficient is
~10⁻⁵ × α (electron) and ~10⁻⁴ × α (proton) — five to four
orders of magnitude too weak for observed Coulomb.  The 1/r
profile is confirmed at large r (F34), but the coefficient
is wrong (F35).  Universality also fails at the spatial level
(F36): α_e / α_p = 0.06 vs the mass-shell's 0.87.

To match observed α from the spatial solve requires σ ≈ 1.8
(F37), which breaks both signature and spectrum — the classical
KK hierarchy problem at Compton-scale compact dimensions.

**Implication for R59:** the mass-shell shift ΔE/E ≈ α from
Track 1 is not the Coulomb coupling.  It is a self-energy-like
mode shift that happens to equal α numerically when σ = α, but
does not produce Coulomb force at strength α in S.  R59's
central claim (Ma-t produces Coulomb α) is falsified (F38).

### Track 4: Closing and next steps

Given Track 3b's negative result, Track 4 does not proceed as
a "comparison and assessment" to build toward model-F.  Instead,
the study closes as a negative result with three possible
follow-on directions:

1. Accept the negative; move focus to other α mechanisms
   (extended R19, GRID-level, moduli potential).
2. Check whether a missed normalization factor in the spatial
   extraction could recover α (focused follow-up).
3. Treat Ma-t as providing sign structure only, with α strength
   from a different mechanism (hybrid, loose).

See findings.md §R59 overall status for the current state.

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
