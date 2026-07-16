# grid-gravity

**Type:** Exploratory / speculative project (see [../README.md](../README.md))
**Scope:** A *mechanical* substrate account of how mass produces
gravitational time dilation and geodesic bending — the "how" beneath
the "that." Gravity only; the electromagnetic force is a named stretch
slot, not a deliverable (see Objectives).
**Method:** Derivation and rule-design first; computation only at the
explicit go/no-go gates.
**Status:** Framed; **feasibility-gated**. No chapter arc is committed
until the gate below (Objective 1) clears. Working hypotheses live in
[work/](work/) until then.

---

## Why this project exists

GRID already derives gravity, but *statistically*. [grid/gravity.md](../../grid/gravity.md)
runs Jacobson's (1995) thermodynamic argument: horizon entropy (axiom
A5) + the Clausius relation + the Unruh effect ⇒ the Einstein field
equations, with G = 1/(4ζ). This establishes *that* the lattice curves
like general relativity. It does not say, at the level of nodes and
edges, *how* a specific lump of mass slows clocks and bends the paths
near it. [grid/synthesis.md](../../grid/synthesis.md) states the gap
outright — *"gravity is thermodynamic, not mechanical"* and *"the
graviton is not derived"* — and two other places flag the same hole:

- [grid/bounding-mechanisms.md](../../grid/bounding-mechanisms.md)
  lists as open *"a microscopic derivation of dS/dt from the rate of
  phase wraps in the lattice… not currently in the GRID files."*
- [metric-mass](../metric-mass/) (Chapter 8) reserves a follow-up
  "gravity mechanism" project. This is that project.

The aim is a substrate-level mechanism whose macroscopic limit is the
curvature that Jacobson's argument already reproduces — a story that
sits *beneath* general relativity, not a replacement for it. General
relativity explains the downstream "how" (curvature → geodesics) well;
what is missing is a substrate origin for the curvature itself.

## Relationship to the statistical account

The mechanical and statistical (Jacobson) accounts are not rivals but two
levels of one stack, related as molecular motion is to thermodynamics: a
gas has a temperature (statistical) and its molecules have velocities
(mechanical), and the temperature *is* the mean kinetic energy at coarse
resolution. Jacobson's derivation is, by his own framing, the "equation of
state" of the spacetime gas; this project describes the molecules.

The relationship is *upstream*. The statistical derivation does not build
gravity from nothing — it assumes the entropy law δS = ζ·δA (axiom A5) and
local equilibrium, then hands them to the Clausius argument. A working
mechanical theory should *derive* those assumptions from the node/edge
dynamics — the microscopic dS/dt that
[grid/bounding-mechanisms.md](../../grid/bounding-mechanisms.md) flags as
missing. This fixes what counts as success: because the statistical result
is substrate-independent (many microscopic mechanisms coarse-grain to the
same Einstein equations), reproducing G = 1/(4ζ) is a necessary
**consistency check, not the payoff**. The mechanism earns its keep by
explaining *why* the entropy is area-scaling and equilibrium holds, and by
reaching the regime the statistical account cannot — far from equilibrium,
[grid/gravity.md](../../grid/gravity.md) notes, the Clausius relation fails
and the Einstein equations may hold only as an approximation.

Compatibility is thus a testable constraint, not an assumption: the levels
lock together only if the mechanism reproduces the area-law entropy and
G = 1/(4ζ) (Objective 2) without a preferred frame that breaks Lorentz
invariance (Ground rule 4). Fail either and the mechanical story is wrong;
the statistical one stands regardless. (On the graviton: this project takes
no position on quantizing the metric — it describes the substrate of which
the metric is an emergent collective mode, the natural stance beneath an
emergent-gravity result.)

## The core hypothesis

Four claims, each a hypothesis to test, not a result:

1. **Proper time is local.** All timing lives in the edges
   (finite-bandwidth transmission lines with load-dependent transit
   times); nodes redistribute continuously, with no clock of their own. A
   global bookkeeping parameter may remain — an unobservable *coordinate*
   time, as in general relativity — but the time any clock *reads* is
   *proper* time, set locally by the signal-propagation rate, which
   congestion reduces near mass. The step from "slowed light" to "slowed
   time" holds only because every clock is itself confined light, so
   slowing the signal slows every clock uniformly. This claim, its
   non-dispersive requirement, and its reconciliation with GRID's
   synchronous-lattice model are developed in
   [work/local-time.md](work/local-time.md).

2. **Mass is a persistent load.** A massive particle is a standing wave
   on a compact dimension (per [metric-mass](../metric-mass/)). Its
   self-consistency (single-valued around the 2π loop) continuously
   cycles information through the lattice node(s) it occupies, imposing
   a persistent load there.

3. **Finite bandwidth ⇒ congestion ⇒ slowed clocks.** GRID edges carry
   finite information per tick. When a node's incoming traffic exceeds
   what it can clear, the surplus is buffered and released as fast as the
   edges allow. Under load, this buffering delays throughput — the local
   clock runs slow. The delay spreads to nearby nodes through the spatial
   loops the loaded node participates in, producing a **congestion field**.

4. **The congestion field is the potential.** Where clocks run slower,
   worldlines lean — the standard weak-field fact that a gradient in the
   rate of proper time is Newtonian gravity. If the congestion field
   falls off correctly (see Objective 1), its gradient reproduces
   gravitational attraction and light-bending.

### The design constraints (a trio, not a single knob)

The mechanism only works if the node/edge rule is simultaneously:

- **Lossless (no shunt loss)** — it leaks none of the sourcing quantity
  (energy) to a bath. *Shunt* loss would add a mass term, giving a
  short-range Yukawa field e^(−r/ξ)/r; with none, the field is massless and
  falls off as a power law (1/r in 3D, log r in 2D). Crucially this means
  *no shunt loss*, **not** *no dissipation at all* — an irreversible
  *series* impedance is not only allowed but required (see the
  Irreversible constraint below and
  [work/congestion-falloff.md](work/congestion-falloff.md) §3). Long-range
  gravity requires masslessness, so no-shunt-loss is a prerequisite,
  assumed throughout (its necessity is settled; see [work/](work/)).
- **Nonlinear** — a linear lossless rule has no load-dependent delay
  (it superposes exactly, as [grid/sim-maxwell](../../grid/sim-maxwell/)
  confirmed). Congestion *requires* nonlinearity: a node's delay must
  depend on how much other traffic is present.
- **Irreversible** — the buffering carries an arrow (the delay/ordering),
  and this is the *series* impedance that lets a static congestion field
  form at all: a purely reversible (reactive) delay passes the steady
  component unchanged and forms no static field
  ([work/congestion-falloff.md](work/congestion-falloff.md) §3).
  Irreversibility is also consistent with GRID's A3 (energy-conserving but
  information-discarding) and would supply the microscopic entropy
  production that [grid/bounding-mechanisms.md](../../grid/bounding-mechanisms.md)
  flags as missing.

## Mission

Produce a mechanical, substrate-level account of how mass generates
gravitational time dilation and geodesic bending — reducing, in the
continuum limit, to the curvature that GRID's thermodynamic derivation
already establishes.

## Objectives

1. **The gate (go/no-go).** Construct a concrete lossless,
   finite-bandwidth node/edge update rule that (a) reduces to the known
   junction behaviour (the 2/3 scatter → Maxwell) at low load, and (b)
   produces a delay that grows with local load. Then test whether a
   persistent localized load produces a congestion field that falls off
   as a **1/r potential (3D) / log (2D), isotropically**. If it comes out
   Yukawa (short-range) or anisotropic, the mechanism fails here and the
   project pivots or closes.
2. **The coefficient.** Given a passing gate, check whether the
   congestion field's strength reproduces G = 1/(4ζ) — i.e. that
   gravity's coupling comes out as the lattice information resolution ζ,
   not as some unrelated constant.
3. **Stretch: the electromagnetic channel.** Gravity is the *scalar*
   (pressure/congestion) response of the traffic. A charged particle is
   the *signed circulation* (helical winding) of the same standing wave,
   whose lattice response is a *directional drift* — a vector channel that
   could carry a signed force (like-repels, unlike-attracts). Attempted
   only if Objectives 1–2 hold; the architecture should leave a named slot
   for it without depending on it.

## Strategy

- **Paper first.** Derive and specify the update rule symbolically;
  reason about the congestion field's operator (does it reduce to a
  massless Laplacian?) before simulating.
- **Compute only at the gates.** The go/no-go halo test (Objective 1) and
  the coefficient check (Objective 2) are where simulation earns its
  place. A lattice Green's-function calculation is confirmatory, not
  decision-driving, and is deferred until the update rule exists.
- **Feasibility gate before arc.** Working hypotheses in [work/](work/)
  until the gate clears; a chapter arc is written only afterward.

## What would kill it

Kept visible so the project stays honest:

- **The rule may not be constructible** — lossless *and* nonlinear *and*
  reducing to Maxwell at low load may not be simultaneously satisfiable.
- **The halo may be Yukawa or anisotropic** — any per-hop dissipation
  makes it short-range; lattice discreteness may make it
  direction-dependent (a direction-dependent gravity is a failure, not a
  cosmetic flaw).
- **Scalar reach only** — a clock-rate (scalar) field gives the universal
  attractive channel but cannot by itself produce the signed EM force
  (the scalar/vector sign theorem, and the universality of time dilation).
  Objective 3 is a genuinely harder, separate build.
- **Dispersive slowing** — if congestion slows different frequencies by
  different amounts (a low-pass filter rather than a pure delay), a
  Compton clock and a slow oscillator dilate differently, clocks disagree,
  and the effect is an optical medium, not time dilation. Decidable from
  the loaded dispersion relation
  (see [work/congestion-falloff.md](work/congestion-falloff.md) §6).
- **The light-bending factor of 2** — a pure time-dilation field
  reproduces Newtonian gravity and gravitational redshift but underbends
  light unless the spatial-metric part is also produced. This project
  targets the dominant time sector; full agreement with general
  relativity's deflection is out of initial scope.
- **The magnitude graveyard** — earlier "variable-c near mass" ideas in
  the repo (e.g. the hexagon-distortion refractive picture in
  [dialogs/grid-2.md](../../dialogs/grid-2.md)) foundered on getting the
  scaling and coefficient right, not the picture. The discipline is to
  measure the power law and prefactor, not to admire the analogy.

## Fail-fast options

A failed gate is not the death of the general hypothesis (gravity from
substrate congestion / local time). If a gate fails, these preserve it, in
descending order of how much they salvage:

1. **Mechanical → entropy → Jacobson (the robust retreat).** If congestion
   cannot be shown to produce a direct 1/r *force* field but *can* be shown
   to produce microscopic entropy at the rate Jacobson's argument needs —
   the dS/dt from phase-wraps/congestion that
   [grid/bounding-mechanisms.md](../../grid/bounding-mechanisms.md) flags as
   missing — then the mechanical picture *feeds* the existing statistical
   machinery instead of replacing it. This drops the risky direct-field
   claim, keeps "gravity from congestion," and fills the exact gap the repo
   already names. A retreat from "mechanical force" to "mechanical entropy
   source."
2. **Long-range Yukawa.** If the field is e^(−r/ξ)/r with ξ beyond tested
   scales, it mimics gravity at accessible ranges — massive-gravity
   territory: weaker, with known issues, but not immediately dead.
3. **Redshift-only.** Even if the spatial/lensing sector is intractable,
   clean gravitational time dilation (the Compton-clock slowing) for
   particles is a real, testable prediction the mechanism may deliver on
   its own.
4. **Re-source or coarse-grain.** Reconsider what sources the field (energy
   flux or winding vs local standing-wave amplitude), or restore isotropy
   via the continuum / block-spin limit
   ([grid/foundations.md](../../grid/foundations.md) Q1) if the lattice
   result is anisotropic.

A clean *negative* — proving congestion gives a Yukawa or a dispersive
slowing — is itself a result: it rules out a hypothesis at low cost, which
is the point of gating.

## Relationship to existing work

| Existing | This project |
|---|---|
| [grid/gravity.md](../../grid/gravity.md) — gravity as horizon thermodynamics (Jacobson), statistical | the *mechanical* counterpart: the substrate dynamics whose limit is that curvature |
| [metric-mass](../metric-mass/) — mass as a compact standing wave (the source of the load) | consumes that source; is the "gravity mechanism" hand-off metric-mass reserves |
| [grid-quantization](../grid-quantization/) — the lossless "sigma-delta / error-feedback node" (buffers, leaks, conserves) proposed for light-quantization | repurposes the same buffering node as the *congestion* element, for gravity |
| [grid-duality](../grid-duality/) — the wrap-promotion ladder (substrate → light → mass → charge) | supplies the mass (L2) and charge (L3) objects the load and the stretch channel act on |

## Scope boundaries — what this project is *not*

- Not re-deriving the Einstein equations or G — [grid/gravity.md](../../grid/gravity.md)
  does that thermodynamically; this supplies a microscopic mechanism, not
  a second macroscopic derivation.
- Not deriving α (that is [studies/R31](../../studies/R31-alpha-derivation/)
  and the grid α work).
- Not delivering the electromagnetic force — that is a stretch slot
  (Objective 3), attempted only if the gravity leg stands.
- Not replacing general relativity — it sits beneath GR as a substrate
  origin for curvature.

## Background reading

- [grid/gravity.md](../../grid/gravity.md) — the statistical derivation
  this project complements
- [grid/foundations.md](../../grid/foundations.md) — the axioms (A3
  compact phase; A5 resolution ζ; the ℵ-line)
- [grid/bounding-mechanisms.md](../../grid/bounding-mechanisms.md) — the
  local-vs-global wrap picture and the flagged missing microscopic dS/dt
- [metric-mass](../metric-mass/) — mass as a compact standing wave
- [grid-quantization/work/energy-and-coherence.md](../grid-quantization/work/energy-and-coherence.md)
  — the lossless buffering (sigma-delta) node
- [grid/sim-gravity/](../../grid/sim-gravity/) and
  [grid/sim-gravity-2/](../../grid/sim-gravity-2/) — the precedent for
  adjudicating a mechanism by its power law (1/r² elastic fails; scalar
  1/r passes)

## Ground rules

1. **Losslessness is assumed**, as a settled prerequisite — no effort is
   spent on dissipative variants known to give short-range fields.
2. **Derivation and rule-design first**; simulate only at the two gates.
3. **Variables stay symbolic** — no numerical pinning until the algebra
   forces it.
4. **Reconcile with the synchronous lattice.** The local-clock premise
   departs from GRID's global-clock model; showing the departure does not
   break the confirmed Maxwell results is part of the work, not an aside.
5. **One topic per chapter**, once the arc begins.
6. **Reader-neutral narrative** — written for any reader, not addressed to
   a particular one.

## Next step

Three work notes are in place, in order:

1. [work/local-time.md](work/local-time.md) — what "proper time is local"
   means (Claim 1): delay in the edges, nodes instantaneous, slowed-light
   = slowed-time via confined-light clocks, coordinate vs proper time.
2. [work/congestion-falloff.md](work/congestion-falloff.md) — the gate
   derivation: reduces the 1/r question to two rule-level conditions
   (no-shunt → massless → 1/r; non-dispersive → time dilation), both read
   off one linearization.
3. [work/update-rule.md](work/update-rule.md) — a concrete candidate
   (finite-bandwidth FIFO edge, instantaneous node) that plausibly passes
   both conditions in the weak-field regime at leading order.

The remaining go/no-go:

- **Next-order linearization** — *done*
  ([work/shunt-check.md](work/shunt-check.md)). The shunt check passes
  analytically: losslessness forbids the bulk loss a shunt requires (shunt
  ⟺ local loss), and the nonlinear back-reactions renormalize coefficients
  without generating a mass term, so the 1/r far-field survives. Two
  contingencies remain, both settled by the simulation below.
- **Falloff + isotropy simulation** — *done, PASSES*
  ([work/falloff-sim-result.md](work/falloff-sim-result.md),
  [scripts/gate_falloff.py](scripts/gate_falloff.py)). A lossless
  finite-bandwidth conservative transport on a hex lattice gives a
  **massless** (log r / 1-over-r, R² = 1.00000), **isotropic** (0.2%
  hexagonal) field, and the bandwidth nonlinearity **does not screen** —
  confirming the shunt-check at full nonlinearity.
- **Dispersion simulation** — *remaining.* Is the load-dependent slowing
  uniform across frequency (a delay, not a low-pass filter)? Needs wave
  propagation, not diffusion — measure ω_loaded(k)/ω_unloaded(k) for
  constancy.

Clearing the dispersion leg clears the gate and opens Objective 2 (the
coefficient, → G = 1/(4ζ)); failing it routes to Fail-fast options.
