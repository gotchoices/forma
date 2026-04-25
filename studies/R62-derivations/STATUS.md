# R62 STATUS — derivation roadmap

This file tracks the derivation program's **givens** (accepted as
inputs without derivation), **what's already derived**, and **what
remains to prove**.  The remaining-to-prove list defines the
follow-on study scope.

---

## Givens (assumed without derivation)

These are the inputs we accept as starting points.  They are not
empirical fits; they are structural assumptions that any future
"deeper" derivation would have to reach as outputs.

1. **α = 1/137.036** — input.  GRID-level derivation deferred (R59).
2. **Three sheets** — postulated from three stable particles
   (electron, proton, neutrino).  Topology choice: T² × T² × T².
3. **Each sheet is 2D (T²)** — postulated from the promotion
   principle.  A 2π closure on one cycle promotes light → mass; a
   second 2π closure on the orthogonal cycle promotes mass →
   charge.  Two cycles per sheet are the minimum to reach charge.
4. **One mass-scale anchor per sheet** — calibration from observed
   masses (m_e, m_p, m_ν₁).  Three independent K's for now;
   reducing to one is a derivation target (see remaining list).
5. **ν-sheet `(ε_ν, s_ν)` admit a few free variables** — pending
   experimental tightening of neutrino observables.  Not a target
   for derivation in the near term.

The aleph dimension's necessity is *not* on this list — it's a
math-driven decision, an open obstacle below.

---

## Already derived (current state)

### Particle-level kinematics (R62 Program 1, complete)

Given the metric structure and the givens above:

- Mass formula `μ² = h^{ab} P_a P_b` on T⁶ (D2, D4, D8, D10).
- Charge as tube Killing momentum (D5).
- Bright/dark dichotomy from phase-lock — `Q132 v2` (D5b).
- Universal charge formula `Q = e(−n_1 + n_5)` on T⁶ (D10, D10b).
- Spin-½ on every KK mode via per-sheet Dirac–Kähler (D7d).
- Tree-level g_e = 2, g_p = 6 (D11).
- Lorentz force from minimal coupling (D6).
- Dark conservation laws from ring momenta (F16).
- Scale-invariance of the construction (D9).

### Sheet-level structural derivations

- **e-sheet `(ε_e, s_e)` derived algebraically** from observed
  lepton mass ratios `m_μ/m_e` and `m_τ/m_e` (R53 Solution D,
  validated under Q132 v2 by R63 Track 5).
- **p-sheet `(ε_p, s_p)` located** by R64 Points A/B against
  proton mass and nuclear chain.  *Not yet R53-style algebraic*
  — this is a parity gap with the e-sheet, listed below.

### Metric-entry derivations

- `σ_ra = (s · ε) · σ_ta` per sheet (R60 T7).
- `σ_ta = √α`, `σ_at = 4π·α`, `g_aa = 1` (R60 T7, given α).
- Diagonal entries in (ε, s, K) per sheet given calibration.

This is roughly half the 21-parameter metric structure derived,
half remaining — see open obstacles.

---

## Open obstacles — the derivation TODO list

Remaining work, ordered by structural priority.

### Obstacle 1 — Cross-sheet σ structural prescription

**Status**: Open.  R60 T7c showed most cross-sheet activations
break α universality.  The structural prescription that survives
(R63 pool item **h**'s triangular pattern) hasn't been derived
from a constraint.

**What's needed**: Take "preserve α universality across all
inventory modes" as an algebraic constraint on the cross-sheet
σ block of the 11×11 metric.  Solve for admissible patterns.

**Expected outcome**: Either a unique structural prescription
(analogous to σ_ra = (s·ε)·σ_ta), a small family of allowed
forms, or "must be zero."  The R64 Phase 7e finding (sectors
algebraically couple) is a piece of evidence: cross-sheet σ
entries DO mix into α extraction; the constraint solver would
identify which patterns leave α invariant.

**Scope**: Bounded.  Single algebraic study, weeks of work.

### Obstacle 2 — Strong-force coupling derivation

**Status**: Open.  R64 has σ_pS_tube ≈ −116 as an empirical fit
that delivers the NN trough at intermediate r.

**Two candidate routes**:

- **Route A (R64 pool j)** — derive σ_pS_tube as a structural
  metric entry, with companion entries that preserve α.
  Quadratic-in-σ deviation pattern from R64 F7e.3 is the
  starting clue.
- **Route B (R64 pool m)** — propagator-based formulation.
  The strong force lives in a vertex factor + meson-analog
  propagator integral, leaving R60's metric algebraically
  untouched.  Yukawa form falls out structurally.

These are alternative architectural choices, not both true.
Route A keeps the 7-tensor metric coupling and adds structure
to make it consistent.  Route B abandons the metric coupling
for a propagator picture.  R64 Phase 7d's clean negative
result on the polynomial form (multi-bound-state Rydberg
ladder, wrong-sign a_s) is evidence for Route B; the
unit-translation gap in 7e is evidence that Route A may not
be as broken as it appears.

**Scope**: Substantial.  Either route is multi-week to
multi-month depending on depth.

### Obstacle 3 — Aleph existence / role decision

**Status**: Open.  R62 D5 derives EM via aleph mediation.  But
the *necessity* of aleph (vs constructing EM in a 10D metric
without it) hasn't been ruled out.

**What's needed**: Try to construct α universality in a 10D
metric (T⁶ + spacetime, no aleph row).  If it works, aleph is
convenience and the metric reduces to 10D.  If it fails (any
attempted construction breaks α universality across modes),
aleph is structurally required.

**Expected outcome**: Decisive.  Either aleph is required (in
which case R62 D5's mediation is the right structural story
and σ_ta = √α is fundamental) or aleph is removable (in which
case σ_ta needs reformulation as a direct Ma↔S coupling).

**Scope**: Bounded.  Single algebraic study, weeks of work.

### Obstacle 4 — p-sheet (ε_p, s_p) algebraic derivation

**Status**: Partial.  R64 located Points A and B by fitting
nuclear chain mass ratios; not yet R53-style algebraic.

**What's needed**: Pick three p-sheet mass-ratio constraints
(e.g., m_p, m_π⁰, m_n − m_p, or some other independent
triple) and solve algebraically for `(ε_p, s_p, K_p)` the way
R53 did for the e-sheet.

**Expected outcome**: Either Point B emerges as the unique
algebraic solution, or a different point does (in which case
R64's chain fit needs reinterpretation), or the system is
under-constrained (in which case more p-sheet observables are
needed to close the algebra).

**Scope**: Small.  Days to weeks, parallel R53 infrastructure.

### Obstacle 5 — Mass-scale ratio derivation (`L_ring_e : L_ring_p : L_ring_ν`)

**Status**: Open.  Currently three independent calibration
scales.  Their ratios `L_ring_p/L_ring_e ≈ 12` and
`L_ring_ν/L_ring_e ≈ 10¹⁰` are not derived.

**What's needed**: Either an inter-sheet relationship from
cross-sheet σ structure (corollary of Obstacle 1), or a deeper
hierarchy argument from R49/R59.  This is a *corollary* —
solving Obstacles 1 and 3 may collapse this to one anchoring
scale automatically.

**Expected outcome**: Best case, three K's reduce to one (only
m_p remains as a calibration anchor; m_e and m_ν₁ follow from
sheet-ratio structure).  Worst case, three K's stay
independent and the hierarchy ratio question goes to R49.

**Scope**: Depends on Obstacles 1, 3.  Itself bounded after
those.

---

## Why this is a TODO list

After Obstacles 1–5 close, the 11D (or 10D) metric has
**every entry expressible** in terms of:

- α (input)
- One mass scale (input, e.g., m_p)
- Sheet topology (3 × T², given)
- Standing-wave quantization (givens 2–4)

That's a substantively predictive theory.  R62 Program 1 has
already established the kinematic backbone (mass, charge,
spin, Lorentz force, magnetic moment).  Obstacles 1–5 close
the metric-structure backbone.

The remaining empirical inputs (α, m_p) are then the SAME
two empirical inputs used in any precision SM calculation —
α and a mass scale.  MaSt would have reduced ~19 SM
parameters to 2.

## Suggested study breakdown

Each obstacle is a candidate for its own study (with appropriate
R-number):

| Study | Obstacle | Scope |
|:--|:--|:--|
| **R65** *(suggested)* | Obstacle 1 — cross-sheet σ structural prescription via α-universality solver | weeks |
| **R66** *(suggested)* | Obstacle 3 — aleph existence test (10D vs 11D EM construction) | weeks |
| **R67** *(suggested)* | Obstacle 4 — p-sheet algebraic derivation (R53 parity) | days–weeks |
| **R68** *(suggested)* | Obstacle 2 — strong-force coupling, Route A or Route B | months |
| **R69** *(suggested)* | Obstacle 5 — mass-scale ratio derivation (likely corollary of R65) | days–weeks |

R67 and R66 are the smallest and least dependent on others; they
make natural near-term targets.  R65 and R66 together resolve the
metric-structure question.  R68 closes the strong-force sector.
R69 falls out as a corollary.

When all five close, R62 Program 1's "Electron from light" arc
extends to a full **MaSt-from-givens** derivation: every metric
term has a mathematical expression in terms of α and one mass
scale, plus the structural givens above.

---

## What stays open after all five close

For honest scope-setting, the items NOT covered by closing
Obstacles 1–5:

- **α-from-geometry** (R59 program, deferred per user direction).
- **Why these specific given values** — why three sheets
  specifically?  Why 2D each?  Why this particular topology?  These
  are taken as givens but their *uniqueness* (vs alternative
  structures) isn't proven.
- **Higgs / electroweak structure** — out of R62's current scope.
- **QFT loop machinery** — radiative corrections, running couplings.
- **Cosmological observables** — BBN, CMB, dark matter density.
- **Gravity at Planck scale** — quantum gravity sector.

These are real scope limits, but none of them blocks the metric-
structure derivation.  They're the next program after R62's
metric program closes.

---

## Possible architectural simplification — hub-and-spoke metric

A structural principle that would collapse Obstacles 1, 2, and 5
simultaneously: **aleph is the unique common mediator; every
off-diagonal in the 11D metric routes through the aleph row, and
direct non-aleph off-diagonals are structurally zero.**

Captured in [Q135](../../qa/Q135-aleph-as-common-mediator.md).
The pattern is consistent with:

- R60's existing structure (cross-sheet σ already zero by default).
- R60 T7c's finding (most direct cross-sheet activations break α).
- R64 Phase 7e's finding (direct σ_pS_tube perturbs α).
- R62 D5's derivation (EM lives entirely in the aleph row).

If the principle is correct, the obstacle list reorganizes:

| Obstacle (original) | Status under hub-and-spoke |
|:---|:---|
| 1 — cross-sheet σ prescription | **Resolved**: all cross-sheet σ = 0 by structure |
| 2 — strong-force coupling | **Reframed**: derive σ_aS (aleph ↔ S-spatial), not σ_pS_tube |
| 3 — aleph existence | **Resolved**: aleph is structurally required as the mediator |
| 4 — p-sheet algebraic derivation | Unchanged |
| 5 — mass-scale ratio | Likely **resolved as corollary**: hub-and-spoke fixes inter-sheet coupling structure, which determines L_ring ratios |

Net: **obstacles 1, 3, and 5 close trivially; obstacle 2 reframes
to a single new entry (σ_aS); obstacle 4 unchanged**.  The
remaining derivation work shrinks substantially.

### Falsification

The principle is testable via **R64 Track 8** (suggested): activate
σ_aS numerically at R64 Point B, check whether α universality is
preserved AND whether a strong-force trough emerges.  Two outcomes:

- **Hub-and-spoke supported**: σ_aS preserves α (as σ_ta/σ_ra do)
  AND produces a strong-force trough comparable to σ_pS_tube's
  Phase 7c result.  Architectural simplification confirmed.
- **Hub-and-spoke fails**: σ_aS either perturbs α (then it's a
  metric entry that needs structural prescription, mirroring 7e's
  σ_pS_tube finding) or fails to produce strong-force phenomena
  (then aleph mediation can't carry the strong sector and we're
  back to a direct sheet-S entry of some kind).

Either outcome is informative.  The test is concrete and bounded
in scope.

### Suggested study revision

If hub-and-spoke is adopted as the working principle, the suggested
study list compresses:

| Study | Obstacle | Status under hub-and-spoke |
|:---|:---|:---|
| R65 | cross-sheet σ universality solver | possibly **redundant** (answer is "all zero") |
| R66 | aleph existence test | possibly **redundant** (answer is "required") |
| R67 | p-sheet algebraic derivation | unchanged |
| R68 | strong-force coupling | **becomes "derive σ_aS"**, simpler scope |
| R69 | mass-scale ratio | likely **corollary** of hub-and-spoke |
| **R64 Track 8** *(new)* | hub-and-spoke numerical test | **runs first**, gates the others |

Recommended sequence: **run R64 Track 8 first** (small, decisive on
the architectural choice), then R67 (independent, small), then
either the much-simplified R68 (if hub-and-spoke confirmed) or the
original R65/R66/R68 (if hub-and-spoke falsified).
