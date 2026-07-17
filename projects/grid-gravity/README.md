# grid-gravity

**Type:** Exploratory / speculative project (see [../README.md](../README.md))
**Scope:** Mechanical, substrate-level models in which mass — a standing
wave in a compact dimension — varies **local time** for resident and
passing waves, and that time-variation *is* gravity. Several candidate
mechanisms, **one shared evaluation framework**. Gravity only; the
electromagnetic force is a named stretch slot.
**Method:** Derivation and rule-design first; computation only at the
go/no-go gates.
**Status: parked — not yet solved, not refuted.** Two theses for a ground-up
GRID mechanism of gravity were explored; neither has *yet* produced one, and
each hit a specific obstruction *in the form tried*:
- **Mechanism 1 (congestion):** the passive "node eats waves" reading
  produces no vacuum field.
- **Mechanism 2 (detour/refractive):** the compact→spatial-transfer
  derivation forced by the review ([review.md](review.md)) comes out negative
  ([work/mode-coupling-derivation.md](work/mode-coupling-derivation.md)) — the
  boundedness (potential) coupling gives the photon a short-range, dispersive,
  gauge-breaking *mass* shift ∝ energy density, not the long-range,
  non-dispersive *metric* that gravity is.

These rule out the *specific forms*, **not the thesis** (mass → local-time
gradient → gravity), which stands open. The lesson is sharp — gravity is a
**metric (kinetic)** effect — and forma's **Jacobson route** (which produces
the metric thermodynamically) is the **fallback** until a deeper mechanism is
found. **Open to revival** if either thesis is seen from a new angle, or a
metric-producing mechanism appears. Working notes in [work/](work/).

---

## Why this project exists

GRID already derives gravity, but *statistically*.
[grid/gravity.md](../../grid/gravity.md) runs Jacobson's (1995)
thermodynamic argument to the Einstein equations, with G = 1/(4ζ). This
establishes *that* the lattice curves like general relativity. It does not
say, at the level of nodes and edges, *how* a specific lump of mass slows
clocks and bends paths. [grid/synthesis.md](../../grid/synthesis.md) states
the gap — *"gravity is thermodynamic, not mechanical"* — and
[grid/bounding-mechanisms.md](../../grid/bounding-mechanisms.md) and
[metric-mass](../metric-mass/) (Ch. 8, a reserved "gravity mechanism"
follow-up) flag the same hole. This project is that follow-up: a
substrate-level mechanism whose macroscopic limit is the curvature Jacobson
already reproduces — a story *beneath* general relativity, not a
replacement.

## Relationship to the statistical account

The mechanical and statistical (Jacobson) accounts are not rivals but two
levels of one stack, related as molecular motion is to thermodynamics.
Jacobson's derivation is the "equation of state" of the spacetime gas; this
project describes the molecules. The relationship is *upstream*: a working
mechanical theory should *derive* what the statistical one assumes (the
entropy law δS = ζ·δA and local equilibrium — the microscopic dS/dt that
[grid/bounding-mechanisms.md](../../grid/bounding-mechanisms.md) flags as
missing). Because the statistical result is substrate-independent (many
microscopic mechanisms coarse-grain to the same Einstein equations),
reproducing G = 1/(4ζ) is a **consistency check, not the payoff**; the
mechanism earns its keep by explaining the assumptions and reaching the
non-equilibrium regime the statistical account cannot. (On the graviton:
this project takes no position on quantizing the metric — it describes the
substrate of which the metric is an emergent collective mode.)

## The thesis (common to every mechanism)

1. **Mass is a compact standing wave** (per [metric-mass](../metric-mass/)).
2. It makes **local time run slower** for waves/particles at and near its
   location.
3. Because **every clock is confined light**, slowing the signal slows every
   clock uniformly ([work/local-time.md](work/local-time.md)) — so this is
   *time dilation*, not merely an optical medium, **provided the slowing is
   non-dispersive**.
4. The **gradient** of the local-time field bends worldlines: gravity (the
   weak-field fact that a gradient in the rate of proper time is Newtonian
   gravity).

Mechanisms differ only in *how* the compact standing wave slows local time.

**Relation to full MaSt (the simplification).** This project works in a
*simplified* setting — a 1D compact loop, a 2D spatial lattice — which is the
**mass-only** regime: charge needs circulation *synchronized between the two
dimensions of a sheet*, impossible in 1D, so 1D yields mass without charge,
exactly what gravity couples to. Because gravity is universal (it couples to
energy, not to which sheet or winding), the mechanism is expected to be
dimension-robust — the compact structure sets particle *identity*, not the
gravity *mechanism*. One check must be **re-derived** in the full 10/11D,
2D-sheet setting rather than assumed: **non-dispersivity** (a sheet has a
mode spectrum, not one resonance). The precise **coefficient** (ζ = 1/4 from
the sheet geometry) is an optional consistency bonus, not a validity
requirement — G's value is largely a unit. See
[work/simplified-model-and-mast.md](work/simplified-model-and-mast.md).

## The shared evaluation framework — the gate

Every candidate must produce a local-time field q(x) that clears the same
four conditions. This is the spine; each mechanism is run through it.

- **(0) Vacuum field [forced].** An isolated mass has a field with nothing
  else around. So the mechanism must produce q(x) in *vacuum* — this rules
  out purely *passive* mechanisms (which produce a field only when other
  traffic is present) and is the sharpest single filter
  ([work/micro-to-macro.md](work/micro-to-macro.md) Condition A).
- **(1) Falloff.** q massless → 1/r (3D) / log r (2D), **isotropic**.
- **(2) Non-dispersive.** the slowing uniform across frequency (a delay, not
  a low-pass filter) — else it is an optical medium, not time dilation
  ([work/local-time.md](work/local-time.md) Commitment 3).
- **(3) Coupling structure.** the coupling is a **fixed constant ∝
  mass-energy** — the same for every mass and location, giving a
  mass-independent Newtonian form — and *consistent in direction and order
  of magnitude* with G = 1/(4ζ). The **precise value of G is not a gate**: it
  is largely a *unit* (like c, ℏ — the SI value depends on the grain size in
  metres, itself defined through G), and the framework's own gravity
  derivation ([grid/gravity.md](../../grid/gravity.md)) does not predict it
  either (ζ = 1/4 is *calibrated*, not derived). Reproducing the exact
  1/(4ζ) factor is an **optional consistency bonus**, not a validity
  requirement — the principle (1/r, universal, coupling ∝ 1/ζ) is the
  dimensionless content; the scale is a unit.

**The linchpin.** Conditions 1 and 2 both trace to one property —
**losslessness**: *loss ⟺ shunt ⟺ Yukawa* (kills 1) **and** *loss ⟺
low-pass ⟺ dispersion* (kills 2). A lossless slowing gives a massless 1/r
field *and* a non-dispersive delay; a lossy one fails both
([work/shunt-check.md](work/shunt-check.md),
[work/dispersion-sim-result.md](work/dispersion-sim-result.md)). So a
mechanism that is *manifestly lossless* has the best shot.

The honest standard for "clearing the gate": these must come out of the
mechanism's **rule**, cross-checked between derivation and a micro-rule sim
with **no free parameters** — not built into the setup (the trap the first
round's sims fell into; see [work/micro-to-macro.md](work/micro-to-macro.md) §6).

## Candidate mechanisms

### Mechanism 1 — Congestion / finite-capacity  *(largely superseded)*

The shared node's finite processing capacity, consumed by the standing
wave, delays spatial signals; congestion spreads via the surrounding loops.

- **The passive "node eats passing waves" reading is dead.** It is lossy
  (→ Yukawa), a *dipole* scatterer (wrong falloff), and produces **no vacuum
  field** — failing gate condition 0
  ([work/micro-to-macro.md](work/micro-to-macro.md) Condition A).
- **The lossless-delay reading survives** but requires the mass to be an
  *active* source of consistency-traffic — a possible but awkward demand.
- **What the investigation established:** the *phenomenological* layer is
  consistent — given a lossless, conserved, diffusive congestion field, the
  result is a massless (1/r), isotropic, non-dispersive slowing, and both
  gate legs reduce to losslessness. But the sims *assumed* the conserved /
  lossless / diffusive properties rather than deriving them, so the premise
  itself was not validated. Notes:
  [local-time](work/local-time.md), [congestion-falloff](work/congestion-falloff.md),
  [shunt-check](work/shunt-check.md), [update-rule](work/update-rule.md),
  [falloff sim](work/falloff-sim-result.md),
  [dispersion sim](work/dispersion-sim-result.md),
  [micro-to-macro](work/micro-to-macro.md).

### Mechanism 2 — Detour / refractive  *(current focus)*

The resident standing wave makes the local vacuum a **slower medium**. A
passing wave briefly **detours into the compact dimension** — a sub-quantum
phase-nudge of the standing wave, ejected within one cycle — and re-emerges
*delayed*, not consumed. Its path is elongated by the excursion. This is a
discrete-lattice mechanism for **optical-metric / polarizable-vacuum
gravity** (n(r) ≈ 1 + 2GM/rc²), a known framework that reproduces the
weak-field GR tests, *including* the light-bending factor of 2.

> **Working premise (stated, not derived here).** The ℵ-line value is bounded
> by a **symmetric, smooth, lossless (reactive)** saturation. This is the
> generic form of any bounded Hamiltonian nonlinearity and is the flavor the
> derivation needs (even ⇒ universal attraction; smooth ⇒ weak-field;
> lossless ⇒ no Yukawa/dispersion). It **differs from forma's default A3
> wrap** (which is lossy) — so this project derives gravity *given* a reactive
> bound, and hands the bound's *origin* (node/edge mechanics) to
> grid-primitive / a substrate project. It may emerge from the hard 1-bit
> bound via grid-quantization's sigma-delta coarse-graining. See
> [work/aleph-grounding.md](work/aleph-grounding.md).

Why it is a better fit to the gate than mechanism 1:
- **Lossless by construction** (detour, not absorption) → condition (0)/(1)/(2)
  linchpin met naturally.
- **Vacuum field via the refractive index** — n(x) is defined at every
  point whether or not a wave is present, so condition (0) is met *without*
  the mass having to actively broadcast (the awkward demand mechanism 1 hit).
- **Resonance-gating** explains vacuum transparency and universality: an
  exact quantum is needed to *initiate* a standing wave, but once one exists
  it enables *sub-quantum* linear coupling of any passing wave.

**REFUTED.** The critical review ([review.md](review.md)) forced the
compact→spatial-transfer derivation (review §2), and the mode-coupling
calculation ([work/mode-coupling-derivation.md](work/mode-coupling-derivation.md))
comes out **negative**. The photon (n=0) coupling to the compact modes via
the boundedness (potential) nonlinearity gives the photon an **effective mass
shift ∝ local energy density** — which is:
- a **mass/potential** coupling (dispersive), not the **metric/kinetic**
  coupling (non-dispersive index) that gravity is — confirming review §1/§2;
- ∝ **local** energy density (contact) — short-range, not 1/r — so the
  loops-and-range 1/r *assumed* a spreading source the mechanism doesn't
  produce (review §5);
- a potential on the U(1) phase, which **breaks gauge invariance** (gives the
  photon a mass) — while the gauge-invariant version (mere compactness) is
  linear and has no detour at all.

Root cause: **gravity is a metric (kinetic) modification** — universal,
non-dispersive, long-range — whereas **boundedness is potential-like**, giving
a mass/contact coupling. Wrong tensor character, wrong range, wrong frequency
behaviour. The earlier "softening → refractive index" step hid this by never
distinguishing a *compact-stiffness* change (a mass) from a *spatial-speed*
change (a metric). So the detour route to gravity is dead in this form.

### (open to further mechanisms)

New mechanisms are welcome provided they are run through the same gate.

## What would kill it (any mechanism)

- The field is Yukawa or anisotropic (fails 1); or dispersive (fails 2); or
  has no vacuum field (fails 0); or the coupling is not a fixed constant ∝
  mass-energy, or is off from 1/(4ζ) by orders of magnitude (fails 3). (A
  *precise* mismatch in the O(1) factor does **not** kill it — that value is
  a unit / calibration, not a gate.)
- **The magnitude graveyard** — earlier "variable-c near mass" ideas in the
  repo (e.g. [dialogs/grid-2.md](../../dialogs/grid-2.md)) foundered on the
  scaling and coefficient, not the picture. Measure the power law and
  prefactor; don't admire the analogy.

## Fail-fast options

A failed gate is not the death of the thesis (mass-induced local-time
variation → gravity). Preserving it, in descending order of salvage:

1. **Mechanical → entropy → Jacobson.** If no mechanism produces a direct
   1/r *force* field but one produces microscopic entropy at Jacobson's rate
   (the dS/dt [grid/bounding-mechanisms.md](../../grid/bounding-mechanisms.md)
   wants), the mechanical picture *feeds* the statistical machinery instead
   of replacing it — dropping the risky direct-field claim, filling the
   flagged gap.
2. **Long-range Yukawa** (ξ beyond tested scales — massive-gravity territory).
3. **Redshift-only** — deliver the time-dilation sector even if lensing is
   deferred.
4. **Re-source or coarse-grain** — reconsider the source, or restore isotropy
   via the continuum / block-spin limit
   ([grid/foundations.md](../../grid/foundations.md) Q1).

A clean *negative* is itself a result: it rules out a hypothesis cheaply.

## Relationship to existing work

| Existing | This project |
|---|---|
| [grid/gravity.md](../../grid/gravity.md) — gravity as horizon thermodynamics (statistical) | the *mechanical* counterpart whose limit is that curvature |
| [metric-mass](../metric-mass/) — mass as a compact standing wave | the source every mechanism acts on; the "gravity mechanism" hand-off metric-mass reserves |
| [grid-quantization](../grid-quantization/) — lossless buffering node; [grid-duality](../grid-duality/) — wrap-promotion ladder | supply the substrate rules and the mass/charge objects the mechanisms act on |
| optical-metric / polarizable-vacuum gravity (Eddington, Puthoff) | mechanism 2 is a discrete-lattice microscopic mechanism for it |

## Scope boundaries

- Not re-deriving the Einstein equations or G — [grid/gravity.md](../../grid/gravity.md)
  does that thermodynamically; this supplies a microscopic mechanism.
- Not deriving α; not delivering the EM force (a stretch slot); not replacing
  general relativity (it sits beneath GR as a substrate origin for curvature).

## Ground rules

1. **One shared gate.** Every mechanism faces the same four conditions;
   results must come from the rule, cross-checked with no free parameters.
2. **Losslessness is the linchpin** — favour manifestly-lossless mechanisms;
   don't develop lossy variants known to give Yukawa / dispersion.
3. **Derivation and rule-design first**; simulate only at the gates.
4. **Variables stay symbolic** — no numerical pinning until forced.
5. **Reconcile with the synchronous lattice** — the local-clock premise
   departs from GRID's global clock; showing it does not break the confirmed
   Maxwell results is part of the work.
6. **Reader-neutral narrative.**
7. **Keep the simplification in context.** The model is 1D-compact
   (mass-only); real MaSt has 2D sheets (mass + charge). Results are the
   mechanism's *skeleton*; non-dispersivity needs full-D re-derivation (the
   precise coefficient is an optional bonus, not a gate)
   ([work/simplified-model-and-mast.md](work/simplified-model-and-mast.md)).
8. **Upstream substrate properties are stated premises, not smuggled.** The
   *reactive-bound premise* (a symmetric, smooth, lossless ℵ-line saturation)
   is stated explicitly and flagged as differing from forma's default wrap;
   its origin (node/edge mechanics) is another project's job. Derive gravity
   *given* it; do not pretend it is established.

## Background reading

- [grid/gravity.md](../../grid/gravity.md) — the statistical derivation this
  complements
- [grid/foundations.md](../../grid/foundations.md) — axioms (A3 compact
  phase; A5 resolution ζ; the ℵ-line)
- [metric-mass](../metric-mass/) — mass as a compact standing wave
- [work/local-time.md](work/local-time.md) — the shared time thesis (slowed
  light = slowed time; coordinate vs proper time)
- [grid/sim-gravity/](../../grid/sim-gravity/),
  [grid/sim-gravity-2/](../../grid/sim-gravity-2/) — the precedent for
  adjudicating a mechanism by its power law

## Chapter arc (draft)

**Objective.** Present how GRID's substrate *mechanically* realizes the
optical-metric / polarizable-vacuum form of gravity — the "how" beneath
forma's statistical "that" — as an **emergence / coherence result at skeleton
rigor**, conditional on the reactive-bound premise. Not a new theory of
gravity: a substrate mechanism for a known one. Its value is framework
coherence (a mechanical gravity to sit beside the statistical one) and the two
structural insights below, not a new prediction.

The arc is a sketch — early chapters firmer, later ones a pool; developed one
at a time and submitted to review (per [../AGENTS.md](../AGENTS.md)).

1. **The mechanical-gravity question.** The gap: GRID's gravity is
   *statistical* (Jacobson) — *that* spacetime curves, not *how*. The thesis:
   mass slows local time, and a gradient in the rate of proper time is
   Newtonian gravity. Clock = confined light, so slowing the signal slows
   every clock (time dilation, not merely slow light). States the simplified
   (1D-compact, mass-only) frame and the **reactive-bound premise** up front,
   and the honest scope (coherence, skeleton rigor).

2. **The players: mass and light on the ℵ-line.** Mass as a compact standing
   wave (KK; [metric-mass](../metric-mass/)); the ℵ-line with the photon as
   its n=0 mode and mass as an n≥1 mode; vacuum transparency (linear KK modes
   are orthogonal — an off-resonant wave doesn't see the compact dimension).

3. **The detour: a resident mass slows the local medium.** Under the reactive
   bound, a large-amplitude standing wave *softens* the local ℵ-line stiffness
   (effective-potential / Kapitza averaging); a passing photon sees a slower
   medium — a refractive perturbation δn — where a mass sits. The core
   mechanism, from the premise.

4. **Why it couples to energy (and always attracts).** A symmetric bound is
   *even*, so the softening is ∝ A² = energy — the coupling gravity needs
   (universal: neutral matter gravitates), always positive (every mass
   attracts). The Lorentz-dielectric identity: the vacuum near mass *is* a
   Lorentz medium with the mass as the resonant oscillator.

5. **Why it is time dilation, not an optical medium.** The slowing is
   non-dispersive (a static effective-medium change; the Lorentz index is flat
   below the mass frequency), so it rescales all clocks uniformly. With clock =
   confined light, the refractive slowing *is* gravitational time dilation.

6. **Why it reaches: the 1/r field.** A localized softening spreads by the
   lattice's own *massless* Green's function; with no length scale, the field
   is scale-free 1/r, isotropic. The loop-unification — the compact loop and
   the spatial hexagon loops are the same kind of cycle — and the assembly
   into the Newtonian potential and light-bending.

7. **Relationships and the honest ledger.** To the statistical gravity: both
   from boundedness (reactive → this mechanical/PV account; dissipative →
   Jacobson). To charge: the *even* substrate deviation gives gravity, the
   *odd* (chirality) gives charge. To full MaSt: what re-derives in 2D sheets
   (non-dispersivity with a spectrum; the coefficient). Honest positioning (a
   re-derivation of the optical-metric/PV picture with a GRID mechanical
   origin — coherence, not novelty), and what is established / premised /
   deferred.

Each chapter maps to work notes already in [work/](work/); the arc is their
pedagogical presentation, not new content.

## Next step

The compact→spatial-transfer derivation (review §2) was carried out
([work/mode-coupling-derivation.md](work/mode-coupling-derivation.md)) and
obstructed mechanism 2 *in the form tried*: the boundedness (potential)
coupling gives the photon a short-range, dispersive, gauge-breaking *mass*
shift, not the long-range, non-dispersive *metric* that gravity is. The
chapter arc above is **withdrawn for now** — a chapter presenting mechanism 2
as a settled gravity mechanism would be wrong.

The **thesis is not refuted** — we simply have **not yet** found a ground-up
GRID mechanism, after two theses. The lesson is sharp and useful: **gravity is
a metric (kinetic) modification**, so any mechanical mechanism must produce
*that*, not a potential/mass or contact/short-range effect. Until one is found:

1. **Jacobson is the fallback.** Forma's existing gravity already produces the
   *metric* (thermodynamically) — the right structure. A mechanical
   contribution, if any, is the microscopic *dS/dt* that
   [grid/bounding-mechanisms.md](../../grid/bounding-mechanisms.md) flags,
   feeding that machinery — not a standalone force field.
2. **Stay open to a metric-producing mechanism** — an emergent field-dependent
   *kinetic* term (effective metric) sourced by energy. Not pursued now (it is
   the hard problem of emergent gravity), but the target is now clear.
3. **Park the project, don't close it.** The two specific obstructions are
   recorded; **resurrect** if either thesis is seen from a new perspective, or
   a deeper mechanism appears. A negative result on the *forms tried* is a
   legitimate, useful outcome — not a conclusion that the thesis fails.

Coherence points that survive independently: the *odd* substrate deviation →
charge (grid-primitive/09). The even→gravity half awaits a viable mechanism.
