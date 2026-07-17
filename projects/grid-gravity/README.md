# grid-gravity

**Type:** Exploratory / speculative project (see [../README.md](../README.md))
**Scope:** Mechanical, substrate-level models in which mass — a standing
wave in a compact dimension — varies **local time** for resident and
passing waves, and that time-variation *is* gravity. Several candidate
mechanisms, **one shared evaluation framework**. Gravity only; the
electromagnetic force is a named stretch slot.
**Method:** Derivation and rule-design first; computation only at the
go/no-go gates.
**Status: parked — blocked on one crux, not refuted.** Two theses for a
ground-up GRID mechanism of gravity were explored; neither has *yet* produced
one, and each is blocked at a specific, identified point:
- **Mechanism 1 (congestion):** the passive "node eats waves" reading
  produces no vacuum field.
- **Mechanism 2 (detour/refractive):** blocked on **range** — does the local
  refractive perturbation extend as a 1/r field? An earlier note
  ([work/mode-coupling-derivation.md](work/mode-coupling-derivation.md)) read
  the coupling as a *refutation* (a gauge-breaking photon **mass** ∝ energy
  density), but that was a **gauge artifact** of coupling a bare *potential* to
  the photon (whose masslessness is established, A4). Redone gauge-invariantly
  ([work/gauge-invariant-coupling.md](work/gauge-invariant-coupling.md)), the
  coupling is a genuine **refractive index** — kinetic/metric-like,
  non-dispersive at ω ≪ ω₀, sourced by energy: the structure gravity needs. It
  is only **local (Planck-contact)**, so the make-or-break returns to **range**.
  Derived GRID-natively ([work/range-from-foundations.md](work/range-from-foundations.md)),
  the range is **blocked on a foundations gap**: a 1/r field needs a
  **massless, neutral, propagating** carrier, and GRID's specified spectrum has
  none — the photon is massless but **charge**-coupled (a neutral mass sources
  none), the KK modes are neutral but **Planck-massive** (short-range), and the
  ℵ-line size R_ℵ is specified as a per-particle **parameter**, not a
  propagating **field**. The scatter propagates signals, not the size.

Neither thesis is refuted, and the thesis itself (mass → local-time gradient →
gravity) stands open. But the mechanical route is **blocked at the range** on
structure GRID does not currently specify — and this is *why* forma's
**Jacobson route** is the natural home: the metric emerges as an *equation of
state*, never needing a massless neutral carrier in the spectrum. Jacobson is
the **fallback**. **Revival** would require a foundations-level result (in
grid-primitive / a substrate project, not here) making the ℵ-line size a
dynamical, massless, energy-sourced field. Working notes in [work/](work/).

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
*delayed*, not consumed. Its path is elongated by the excursion. The *aim* is a
discrete-lattice mechanism in the family of **optical-metric / polarizable-
vacuum gravity** (n(r) ≈ 1 + 2GM/rc²) — a known framework that reproduces the
weak-field GR tests including the factor-of-2 light bending. Whether *this*
mechanism actually reaches that form is **open**: the local index is
established (below), but its **1/r range** and the light-bending coefficient
are not.

> **Working premise (stated, not derived here).** The gauge-legitimate form of
> GRID boundedness is the finite-**bandwidth** bound — a bound on the *rate*
> (finite bits per tick, a bound on ∂θ; [local-time.md](work/local-time.md)
> Commitment 2), i.e. a **kinetic** nonlinearity — *not* a bound on the phase
> *value* (a potential, which would give the photon a mass and is forbidden by
> its established masslessness, A4). A rate-bound modifies the photon's
> **kinetic** term → a **refractive index** (metric/kinetic), which is the
> structure gravity needs. This is the project's *original* congestion premise
> (finite bandwidth), recovered after a first pass mistakenly reframed it as a
> value-bound. The bound's *origin* (node/edge mechanics) is handed to
> grid-primitive / a substrate project. See
> [work/gauge-invariant-coupling.md](work/gauge-invariant-coupling.md) §2 and
> [work/aleph-grounding.md](work/aleph-grounding.md).

Why it is a better fit to the gate than mechanism 1:
- **Lossless by construction** (detour, not absorption) — the linchpin behind
  conditions (0) and (2). *(Condition (1), range, is the open blocker — below.)*
- **Local index established, non-dispersively** — the coupling is a genuine
  refractive index (conditions 2 and 3, met from the rule; see below), *at* the
  mass. What is not yet met is extending it to range.
- **Resonance-gating** explains vacuum transparency: an off-resonant wave does
  not see the compact dimension; a resident standing wave enables the
  sub-quantum coupling of any passing wave.

**BLOCKED ON RANGE (not refuted).** An independent critical review (since
incorporated) forced the compact→spatial-transfer derivation. A first pass
([work/mode-coupling-derivation.md](work/mode-coupling-derivation.md)) read it
as a refutation — the photon acquiring a gauge-breaking *mass* shift ∝ energy
density. But that was a **gauge artifact**: it coupled a bare phase *potential*
to the n=0 gauge mode, which the photon's **established** masslessness (A4)
forbids. Redone respecting gauge invariance
([work/gauge-invariant-coupling.md](work/gauge-invariant-coupling.md)), the
Ward identity forces the coupling **transverse** — a **refractive index**, not
a mass:
- a **metric/kinetic** coupling (a background-dependent photon kinetic term),
  **non-dispersive** for ω ≪ ω₀, **sourced by energy** — the structure gravity
  needs (conditions 2 and 3 met from the rule);
- **massless in vacuum** — gauge intact; the "photon mass" of the first pass is
  discarded as contradicting the confirmed Maxwell result;
- but the index is **local (Planck-contact)** — a dielectric sits *on* the
  matter. So the one surviving obstruction is **range**: getting a *local* index
  to extend as **1/r**.

Root cause of the first pass's error: it modeled boundedness as a bound on the
phase *value* (a potential → a mass), whereas the gauge-legitimate reading is
the finite-**bandwidth** bound on the *rate* (∂θ → a kinetic nonlinearity → an
index).

The surviving **range** question is **GRID-native** and does *not* require
importing anyone's scalar-tensor theory. The one hard *requirement* is math,
not borrowed physics: a **1/r** field needs a **massless** carrier (a massive
one falls off as short-range Yukawa), and the KK modes are Planck-massive — so
range cannot come from them. The GRID-native question is therefore whether the
substrate *has* a massless, neutral-energy-sourced mode that carries the local
index outward. The natural candidate is the **ℵ-line dilation** — the local
compact-size degree of freedom (whose zero-mode standard physics would call the
radion; [grid/photon-from-aleph.md](../../grid/photon-from-aleph.md)) — which a
resident mass shifts locally. Whether that shift propagates as a massless 1/r
field, is sourced ∝ energy, and slows passing light with the right strength, is
to be modeled **from GRID's own dynamics** (the update rule / lattice
propagation), *not* by adopting scalar-tensor formalism. Open — a live crux,
not a refutation.

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

The compact→spatial-transfer derivation (forced by the incorporated review)
was carried out in two passes. The first
([work/mode-coupling-derivation.md](work/mode-coupling-derivation.md))
read the coupling as a refutation (a gauge-breaking photon *mass*). The
gauge-invariant redo ([work/gauge-invariant-coupling.md](work/gauge-invariant-coupling.md))
shows that was an artifact: the physical coupling is a **refractive index** —
metric/kinetic, non-dispersive at ω ≪ ω₀, energy-sourced — so **mechanism 2 is
not refuted**. It is **blocked on range**: the index is local (Planck-contact),
and extending it to 1/r needs a massless, energy-sourced mediator. The chapter
arc above stays **on hold** — a chapter presenting mechanism 2 as a *settled*
gravity mechanism would still be premature — but it is not withdrawn.

That range crux was then **derived GRID-natively**
([work/range-from-foundations.md](work/range-from-foundations.md)), as the
foundations demand, and it is **blocked**: GRID's specified spectrum has **no
massless, neutral, propagating carrier** (photon = massless but charge-coupled;
KK = neutral but Planck-massive), and the ℵ-line size R_ℵ is specified as a
per-particle **parameter**, not a propagating **field** — the scatter moves
signals, not the size. So the local index has nothing to carry it to 1/r. This
is **not a refutation** (the index is real; the thesis stands) but it locates
the block precisely: a foundations gap. Standing options:

1. **Jacobson is the natural home.** Its metric emerges as an *equation of
   state*, so it never needs the massless neutral carrier the spectrum lacks —
   which is *why* the statistical route works where the mechanical one blocks. A
   mechanical contribution, if any, is the microscopic *dS/dt* that
   [grid/bounding-mechanisms.md](../../grid/bounding-mechanisms.md) flags,
   feeding that machinery — not a standalone force field.
2. **A foundations investigation, elsewhere.** Revival of mechanism 2 requires
   showing — in grid-primitive / a substrate project, *not* here — that GRID's
   ℵ-line size is a **dynamical, spatially-varying, massless** degree of freedom
   sourced by energy. Absent that, there is no carrier. (Even then, two hurdles
   remain: scalar-monopole sourcing and the light-bending coefficient,
   [work/gauge-invariant-coupling.md](work/gauge-invariant-coupling.md) §4.)
3. **Park the project, don't close it.** The block is recorded and precisely
   located (no massless neutral carrier in the foundations); **resurrect** if a
   substrate-level result supplies a massless ℵ-line-dilation field, or if a new
   angle appears. A block on a *foundations gap* is a legitimate, useful outcome
   — and honestly, this is the recommended state: the mechanical route can't
   proceed without foundations GRID doesn't yet have.

Coherence points that survive: the *odd* substrate deviation → charge
(grid-primitive/09). The **even → gravity** half is not refuted, but it is
**blocked** — it rests on a massless ℵ-line-dilation carrier that GRID does not
currently specify.
