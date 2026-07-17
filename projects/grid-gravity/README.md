# grid-gravity

**Type:** Exploratory / speculative project (see [../README.md](../README.md))
**Scope:** Mechanical, substrate-level models in which mass — a standing
wave in a compact dimension — varies **local time** for resident and
passing waves, and that time-variation *is* gravity. Several candidate
mechanisms, **one shared evaluation framework**. Gravity only; the
electromagnetic force is a named stretch slot.
**Method:** Derivation and rule-design first; computation only at the
go/no-go gates.
**Status:** Two candidate mechanisms under a common gate. Congestion
(mechanism 1) is largely superseded; detour/refractive (mechanism 2) is the
current focus. No mission chapter arc until a mechanism clears the full gate
(falloff + dispersion + coefficient) from its rule, not by construction.
Working notes in [work/](work/).

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
- **(3) Coefficient.** magnitude reproducing **G = 1/(4ζ)**.

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

Why it is a better fit to the gate than mechanism 1:
- **Lossless by construction** (detour, not absorption) → condition (0)/(1)/(2)
  linchpin met naturally.
- **Vacuum field via the refractive index** — n(x) is defined at every
  point whether or not a wave is present, so condition (0) is met *without*
  the mass having to actively broadcast (the awkward demand mechanism 1 hit).
- **Resonance-gating** explains vacuum transparency and universality: an
  exact quantum is needed to *initiate* a standing wave, but once one exists
  it enables *sub-quantum* linear coupling of any passing wave.

Open (the gate conditions, for this mechanism):
- **Non-dispersive?** Is the detour delay *fixed* (≈ one compact-dimension
  cycle → non-dispersive) or *resonant* (frequency-dependent → dispersive)?
- **Range?** Does the refractive well *extend* (n(r) → 1/r potential) via the
  loop-coupling carrying the standing wave's constraint outward?

Foundation + derivation attempt: [work/detour-refractive.md](work/detour-refractive.md).

### (open to further mechanisms)

New mechanisms are welcome provided they are run through the same gate.

## What would kill it (any mechanism)

- The field is Yukawa or anisotropic (fails 1); or dispersive (fails 2); or
  has no vacuum field (fails 0); or the coefficient is not ~1/(4ζ) (fails 3).
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

## Next step

Vet mechanism 2 (detour/refractive) against the gate from its rule:
[work/detour-refractive.md](work/detour-refractive.md) — foundation and
micro→macro derivation attempt, settling first whether the detour delay is
non-dispersive (fixed ≈ one compact cycle) or dispersive (resonant), then
whether the refractive well has 1/r range. If it fails early, the fail-fast
options and further mechanisms remain.
