# The nature of local time

**Status:** Working note (hypothesis). Resolves what "time is local"
means for this project — Claim 1 of the [README](../README.md). This
note is *logically prior* to the update-rule feasibility gate: the gate
measures a distance-dependent delay field, and a delay field is
gravity only if delay equals proper time. That identification is settled
here, not there.

Each commitment is graded **[commitment]** (a modeling choice this
project adopts), **[rigorous]** (follows once the commitments are made),
or **[open]** (flagged, not resolved).

---

## The problem with Claim 1 as first written

The first phrasing said a node's clock rate is "how quickly it can clear
its traffic," with nodes advancing asynchronously rather than under a
master clock. Two things are ill-posed there:

- **What triggers a node to act?** An asynchronous "fire" needs a trigger
  — arrival of input, or a threshold crossing — and defining simultaneity
  and causal order across many independently-firing nodes, with no shared
  clock, is a genuinely hard and underspecified problem.
- **"Slower clock" is asserted, not derived.** Saying the clock runs slow
  under load skips the step that actually matters: *why* a slower signal
  is a slower clock, rather than merely slower light through an unchanged
  clock.

The fix is not to add detail about asynchronous firing. It is to relocate
where the delay lives and to make one identification explicit.

## Commitment 1 — delay lives in the edges; nodes are instantaneous [commitment]

Adopt the **transmission-line network** picture:

- **Edges** are delay lines with a finite transit time — the time for a
  signal to cross from one end to the other.
- **Nodes** redistribute continuously and instantaneously — they enforce a
  constraint among their incident edge values (a scattering / Kirchhoff
  relation) with no internal delay and no clock of their own.

This removes the ill-posed trigger: nothing "fires." The dynamics are
continuous-time, with all timing carried by the edges. It is also the
*smaller* departure from GRID, which already treats nodes as instantaneous
stateless scatterers ("no extra ticks of delay through the node",
[grid-duality/09-node-decomposition.md](../../grid-duality/09-node-decomposition.md)).
A continuous-time transmission-line network still yields the wave equation
(telegrapher's equations → Maxwell) in the low-load limit, so this choice
supports Ground Rule 4 (reconcile with the confirmed Maxwell results)
rather than fighting it.

**"Local time" then has a concrete referent:** the local signal-transit
rate on the edges around a point.

## Commitment 2 — the edges are finite-bandwidth; latency grows with load [commitment]

A *linear* lossless transmission network has no congestion — signals
superpose exactly and pass without mutual delay (as
[grid/sim-maxwell](../../grid/sim-maxwell/) confirmed). Congestion
therefore requires the nonlinearity from the README's design trio, and it
is placed here: each edge carries only finite information per unit time,
so a backlog of in-flight signal raises the transit time. Transit time
τ_edge(load) increases with occupancy. This is the finite-bandwidth /
"edges carry limited bits" idea from earlier discussion, now given a
definite home (the edge, not a node buffer).

## Commitment 3 — slow light equals slow time, because every clock is confined light [commitment + rigorous consequence]

This is the keystone. Taken literally, congestion slows **light** — the
effective propagation speed c_eff(x) drops. By itself that is an *optical
medium*: glass slows light but does not slow time, and a clock outside the
glass is untouched.

The slowing becomes **time dilation** under one commitment: **every clock
is itself a pattern of the same signals being slowed.** In GRID/MaSt,
matter is confined light, and a particle's clock *is* its internal
circulation frequency — the Compton clock. So congestion that slows the
signal slows the circulation in the particle's cavity, and the particle's
proper time slows with it. Because atomic transitions, oscillators, and
every other process are likewise patterns of the same signal, they slow by
the same factor. All clocks agree — which is exactly the universality of
gravitational time dilation, inherited here from "one substrate."

The chain, stated plainly:

> slowed signal → slowed cavity circulation → slowed proper time,
> and it is *time* rather than *medium* only because every clock is
> made of the slowed signal.

Two conditions are required for this to hold, and they are real
constraints on the update rule — not decoration:

- **Non-dispersive [rigorous requirement].** Time dilation rescales *all*
  frequencies by the same factor. If congestion slowed high frequencies
  more than low (a dispersive medium), a Compton clock (high ω) and a slow
  oscillator (low ω) would dilate by different amounts — clocks would
  disagree, and the effect would not be time dilation. So the congestion
  delay must be **frequency-independent** — a uniform rescaling of the
  local rate. This is the cleanest single test that separates "time
  dilation" from "optical medium."
- **Universal [rigorous consequence].** It must slow everything, which
  follows for free from the one-substrate commitment, but must not fail:
  any process that escaped the slowing would break the equivalence
  principle.

## Commitment 4 — coordinate time is global and gauge; proper time is local and observable [commitment]

The worry behind "no master clock" is really a worry about *observable*
time. Resolve it as general relativity does:

- A global background bookkeeping parameter may remain (the substrate's
  update parameter) — this is **coordinate time**, unobservable and gauge,
  exactly like general relativity's coordinate time. Its presence is not a
  problematic "master clock."
- What any clock *reads* is **proper time**, set locally by the
  signal-propagation rate, which congestion reduces near mass. Proper time
  is the observable, and it is local.

So the sharp form of Claim 1 is not "there is no global clock." It is
**"proper time is local,"** with a global gauge coordinate-time permitted.
This maps directly onto general relativity's own time structure and
removes the squish without requiring true asynchrony.

## Scope of the slowing — compact and embedding directions [rigorous / open]

A node loaded by a compact-dimension standing wave is congested for
*every* edge it touches — compact and spatial alike. That is the whole
content of the shared-node premise. Two consequences, of different
maturity:

- **Compact directions → proper-time dilation of the particle** (the g₀₀ /
  clock sector). This is the clean part and what the mechanism most
  naturally delivers. **[rigorous, given Commitment 3]**
- **Spatial directions → Shapiro delay and bending of passing light** (the
  g_ij / space sector). Present in principle — same shared-node congestion
  — but reproducing the *full* general-relativistic light deflection is
  harder: the deflection takes equal contributions from the time and space
  sectors (the factor of 2), and whether the congestion distributes
  between compact and spatial directions to reproduce that is **[open]**.
  The README scopes full deflection out of the initial target for this
  reason.

## What this fixes for the gate

- The gate's distance-dependent field is to be read as a **proper-time**
  (clock-rate) field, not a light-transit-time field — that is what makes
  a 1/r result gravity rather than an optical halo.
- The update rule must produce a **non-dispersive** slowing. A rule that
  slowed frequencies differently would fail Commitment 3 even if it gave a
  clean 1/r falloff.

## Open questions

- **Reconciling continuous-time with the synchronous derivations.** GRID's
  Maxwell result is derived on a synchronous tick. The claim that a
  continuous-time, distributed-delay network reduces to the same Maxwell
  behaviour at low load is plausible (telegrapher → wave equation) but is
  asserted here, not shown.
- **Whether non-dispersivity is automatic or must be engineered.** Finite-
  bandwidth channels are generically dispersive. Whether the specific
  congestion mechanism can slow uniformly across frequencies, or whether
  non-dispersivity is an extra constraint that narrows the admissible
  rules, is unresolved and bears directly on the update-rule spec.
- **The space-sector / factor-of-2**, as above.

## Grades summary

| Item | Grade |
|---|---|
| Delay in edges, nodes instantaneous (transmission-line picture) | commitment |
| Finite-bandwidth edges, latency grows with load | commitment |
| Slow-light = slow-time *because clocks are confined light* | commitment |
| …therefore all clocks slow uniformly (universality) | rigorous, given the above |
| Non-dispersive slowing required | rigorous requirement |
| Coordinate-time (gauge, global) vs proper-time (observable, local) | commitment |
| Compact-direction slowing → proper-time dilation | rigorous, given Commitment 3 |
| Spatial-direction slowing → full GR light-bending (factor of 2) | open |
