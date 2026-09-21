# Working backwards — what GRID would need, and how many degrees of freedom

**Status:** Opening note of step 5 of the mechanism 3 validation plan
([STATUS.md](STATUS.md)). Steps 1–4 tested pieces of the mechanism with the loop
open. This note changes direction: instead of choosing *how* a node or edge
would do these things, it collects **what any implementation would have to
do** — the requirements the steps have produced — counts the degrees of freedom
that implies, and records the first result of scanning the remaining choices
against observation. Mechanisms can then be hypothesized against a fixed list.

Grades: **[rigorous]**, **[from the steps]**, **[from the repo]**,
**[reading]** (an interpretation, nothing computed), **[open]**.

---

## 0. What kind of claim this is

Everything here is a statement about **rules** — what happens on the lattice —
not about what nodes and edges are made of. The same rules could be realized by
many substrates, and an inhabitant of the lattice could only ever learn the
rules. By its own numbers the lattice hides well: every departure from
continuum physics found so far is of order (frequency × tick)², some forty
orders of magnitude below anything measurable. So the posits are constrained
almost entirely by whether they reproduce known physics economically, and by
any distinctive consequence they force (§8 lists the ones found so far).

## 1. Vocabulary at the lattice level

"Voltage" and "current" have settled meanings far above this level, and using
them here invites confusion. The circuit picture is kept as an *analogy* for
readers who think in it; the working terms are generalized mechanical ones,
which carry no electromagnetic meaning and fit the repo's existing picture of an
edge as a small elastic tube
([grid-primitive](../../grid-primitive/)).

| term used from here on | meaning | earlier notes | circuit analogy | rod-lattice analogy |
|---|---|---|---|---|
| **deflection** q | the stored scalar at a node; the carrier's *potential*. "Deflection" in a generalized sense — not a movement in space | "potential q" | flux (∫ voltage dt) | displacement |
| **deflection rate** | the value shared by everything meeting at a node; q's rate of change | "node value V" | node voltage | node velocity |
| **tension** | what a link carries; proportional to the difference of deflection between its ends | "link flux", "gradient" | link current | force in the rod |
| **node inertia** | what node storage raises (slows everything through the node) | ε, weight Y | shunt capacitance | node mass |
| **link compliance** | what edge storage raises (slows that link only) | μ, weight Z | series inductance | softness of the rod |
| **impedance** | √(inertia × stiffness); unchanged when both storages are loaded equally | impedance | impedance | impedance |

In the rod-lattice reading the mechanism says: *near energy, nodes gain inertia
and space-links lose stiffness, in equal proportion* — so waves slow, and
nothing reflects.

## 2. What a junction already does [rigorous]

If an edge is a lossless two-way line and a node is simply where N of them
meet, a pulse arriving on one line meets the other N − 1 in parallel. It is
partly reflected, with coefficient (2/N) − 1 — negative, i.e. *inverted* — and
partly transmitted, 2/N into each other line. Summing over arrivals gives
exactly GRID's scatter: shared value = (2/N)·Σ arrivals; each line sends back
the shared value minus what it brought.

So the scatter's "new sum, minus the edge's own previous value" needs no
computation. The sum is the value shared at the junction; the negation is the
reflection. **The edge does the negating; the node only holds the lines
together.** This is how grid-primitive already describes it ("nodes are passive
junctions … there is no node update rule"), and it is the register picture of
[grid-duality](../../grid-duality/models/scattering.md) read physically.

Two consequences for clocking and for what "slowing" means:

- **No clock is needed, and nothing needs to get synchronized.** A junction is
  linear: it scatters each arriving pulse on its own and never waits for a
  coincidence. Signals launched at different sub-tick offsets simply travel as
  independent interleaved copies of the same lattice; for any wave much longer
  than an edge they all carry nearly the same values — one smooth field. The
  "tick" is just the unloaded transit time of an edge, a bookkeeping unit. (This
  is posit P1 with neither scheduler nor synchronization step.)
- **Two equivalent ways to slow a wave.** (a) *Storage:* a store returns its
  share one tick later; transit times stay fixed. This is the only option if the
  lattice is strictly tick-synchronous, and it is what the simulations use,
  since a discrete-tick code cannot represent a fractional delay. (b) *Longer
  transit:* the wave simply takes longer to cross a loaded edge. With passive
  junctions this is allowed, and a line whose transit time lengthens at
  **unchanged impedance** is *exactly* reflectionless — cleaner than storage,
  which leaves a residue of order (spacing/wavelength)². The two agree at long
  wavelength and carry the same requirement (R5, R6, R9): a hop through space is
  delayed by (1 + q/2)², a clock's compact lap by (1 + q/2).

**What time dilation means in either picture.** Coordinate time is what distant,
unloaded clocks read. Proper time at a place is the phase accumulated there by
circulating waves, which is what every clock is made of. Near energy that
accumulation is slower — because more of each wave is parked, or because each
lap takes longer — by the same factor for every clock.

## 3. The requirements so far [from the steps]

| # | Requirement | From |
|---|---|---|
| R1 | Lossless throughout — no local leak of anything stored | mechanisms 1–2; step 1 |
| R2 | Equal transit time on every line (every channel) | §2 |
| R3 | Slowing is lossless and does not change impedance: by storage returning one tick later, or by longer transit at fixed impedance (§2) | §2, step 1 |
| R4 | A node store returns its share with the **same** sign; a link store returns it **inverted** (the opposite, in either place, gives the photon a mass) | steps 1, 3 |
| R5 | Node stores and space-link stores are loaded **equally** (impedance unchanged → no reflection → full light bending) | step 3 |
| R6 | A clock's compact circulation is loaded by **one** of the two stores, not both | step 3 (P7) |
| R7 | Each node keeps a **memory**: the running sum of its deflection rate (the deflection q). Links carry only differences of q, so a node cannot learn q from its links | step 4 |
| R8 | The stores' weights are set by the local q (potential, not tension) | P5; step 2 |
| R9 | Each member's delay is **linear** in q (§7) | this note |
| R10 | A single particle's source must not oscillate (§8) | step 3 |

R7 with R8 is the one genuinely new kind of element: a store whose weight
depends on the *history* of what has passed through it. Lossless elements of
that kind are known in circuit theory (memory-capacitors and memory-inductors);
in the rod reading it is an inertia that depends on how far the node has been
deflected.

## 4. Degrees of freedom

| where | what | status |
|---|---|---|
| each link | two amplitudes, one travelling each way, per wave channel | GRID has it |
| each node | nothing of its own (a junction) | GRID has it |
| each node | one store amplitude | new (step 1) |
| each space link | one store amplitude | new (step 3) |
| each node | one memory, the deflection q, which sets the two store weights around it | new (step 4) |
| carrier channel | either a second wave channel on the links (two more amplitudes per link) — or none (§6) | **open** |
| each link | the link phase and its conjugate | GRID has it (axiom A4) |
| compact loop | a non-reciprocal element (the [EM slot](em-slot.md)) | open |

Per node in a 3D lattice the gravity additions come to one store amplitude, one
memory, and one store amplitude on each of its three links — plus, in the
costlier branch of §6, a second channel.

## 5. A mechanical reading: stretch and twist [reading]

A literal-stress picture fits this list better than might be expected, and much
of it is already in the repo.

- **The edge as a small elastic tube** is grid-primitive's primitive: a
  nanotube-like cylinder carrying a longitudinal strain and an azimuthal phase,
  with nodes as passive junctions.
  [grid-duality's tube sketch](../../grid-duality/grid-quantizing.md) adds
  counter-propagating torsional waves that pass through each other linearly,
  and a radial breathing mode whose period is the tick.
- **Scalar ↔ stretch (or breathing).** A change of length or radius has no
  direction. It is even under reversing anything — the right character for the
  gravity carrier (even, universal, one sign).
- **Signed ↔ twist.** A twist is left- or right-handed. That is the signed
  quantity the charge slot needs. One caution, to be checked rather than
  assumed: the handedness of a twist does *not* flip when the edge is traversed
  the other way (a left-handed helix is left-handed from both ends), whereas a
  link phase does flip. So a twist is naturally a *chirality*, and
  [grid-primitive ch. 9](../../grid-primitive/09-chirality-asymmetry.md) already
  shows that an antisymmetric chirality acts as a background gauge field and
  produces signed phase shifts on compact wraps. Whether that supplies the
  vector character needed for like charges to *repel* is rung E3 of the EM
  ladder.
- **A finer layer.** grid-primitive notes that the tube wall could itself be a
  finer lattice and stops there by rule. At requirement level the idea costs
  one thing: **R2**. A real elastic tube carries stretch and twist at different
  speeds; here every channel in use must share one transit time.
  grid-primitive's "bare-speed equality" postulate is the same requirement,
  already stated.

## 6. The fork: is the carrier a separate channel? [open]

**Branch A — a second channel.** The carrier is its own wave amplitude on the
same lines, sourced by the matter wave through the action of step 3, with a free
stiffness κ that sets Newton's constant.

**Branch B — the same channel.** If a store's weight depends on the accumulated
deflection of the *one* wave that is there, that wave feeds itself: the source
term of step 3, ½K′·(rate)², is always positive, so an oscillating wave leaves
behind a slow, one-signed deflection — a rectified component — proportional to
its energy, which spreads as 1/r. Gravity would then be the zero-frequency part
of the same field whose oscillating part is light and matter. Nothing is added
beyond the memory of R7, and there is **no free stiffness**: the coupling is of
order one in lattice units, which is what a Planck-scale grain means (consistent
rather than predictive).

Branch B is cheaper and has more ways to fail: the same nonlinearity produces
light-on-light scattering and a second harmonic at twice a particle's rest
frequency, both at gravitational strength. Those have to be shown harmless.

**Branch B′ — the same two degrees of freedom for everything.** A refinement
that costs nothing further: grid-primitive's tube already has exactly two
internal degrees of freedom (a longitudinal strain and an azimuthal phase), and
its photon is their coupled oscillation, with two polarizations. Let light and
matter be the *oscillating* part of those two, gravity the *steady* part of the
stretch-like one, and charge the steady part of the twist-like one. Then the
ledger of §4 needs **no new wave degrees of freedom at all** — only the node
memory of R7 (and the non-reciprocal compact element of the EM slot). This is
the cheapest ledger found so far. Its open points are Branch B's, plus the
twist's vector character (§5).

## 7. First scan result: β requires delay linear in deflection [rigorous]

Step 3 left the second-order parameter β open
([action-and-gamma.md](action-and-gamma.md) §7), comparing three candidate
dynamics at a *fixed* form of the loading, K = e^q. Asked the other way round —
given that the carrier propagates on the loaded lattice exactly as light does
(which both branches require, and which keeps gravitational and light signals in
step), *what form of loading gives β = 1?* — the answer is unique:

<!-- √K = 1 + q/2  : each member's delay factor is linear in the deflection -->
$$
\sqrt{K} \;=\; 1 + \tfrac{q}{2}
\qquad\text{i.e. each member's delay factor is linear in the deflection.}
$$

A node delays by (1 + q/2); a space link delays by (1 + q/2); light, crossing
both, by (1 + q/2)²; a clock, sitting in one, by (1 + q/2). With U = GM/r the
static solution is 1 + q/2 = e^U exactly (checked symbolically: the static field
equation is satisfied identically), so the clock rate is e^(−U) and the light
speed c₀·e^(−2U):

- clock rate² = 1 − 2U + 2U² − … → **β = 1**;
- light speed = c₀(1 − 2U + …) → **γ = 1**.

This is not a new model: under the change of variable σ = 2·ln(1 + q/2) it is
*identical* to the polarizable-vacuum form that step 3 found to be the one
survivor. So step 3's flag is resolved at requirement level (R9): one completion
is viable, and in the lattice's own variable it is the simplest rule available —
**delay proportional to deflection.**

**Consequence for the strong field.** The clock rate e^(−GM/r) reaches zero only
at r = 0: this completion has **no horizon** of its own. A horizon appears only
if the lattice has a largest delay factor D_max a member can supply — the "edge
of the dead band" — and then the surface where the lattice loses lock sits at
r = GM / ln D_max, **proportional to M**, as the scaling test of
[sync-carrier-mechanism.md](sync-carrier-mechanism.md) §10 demands. Whether such
a limit exists is a property of the substrate, not derivable here.

## 8. Distinctive consequences so far [from the steps]

Places where the mechanism says something that is not simply built in:

- A purely **standing** neutral wave is a breathing source and would radiate
  (step 3). Hence R10: real particles must be of the travelling kind, or
  protected by whole-quantum energetics.
- Departures from universality of free fall of order (rest frequency × tick)²
  (step 2).
- No horizon without a largest delay (§7).
- In Branch B: light-on-light scattering and a second-harmonic response at
  gravitational strength.

## 9. What remains for step 5

1. **Close the loop in simulation** with R9's rule: a wave sources q; q sets the
   stores. *Branch A done* ([closed-loop-result.md](closed-loop-result.md)): two
   lumps fall toward each other on the ray law, with the third law and momentum
   conservation emerging. *Branch B next* — but first its exact conservative
   lattice rule must be derived from the action (what is held fixed when a
   store's weight changes), since an ad hoc rule would not conserve energy.
2. **Branch B's hazards** (§6): size of the second-harmonic and light-on-light
   effects.
3. **R10**: confirm that a wave travelling around the compact loop has a steady
   source, and a standing one radiates at the predicted rate.
4. **The strong field**, with and without a largest delay.

## Grades summary

- **[rigorous]** The junction derivation of the scatter (§2); the linear-delay
  result, its static solution, β = γ = 1, and its identity with the
  polarizable-vacuum form (§7).
- **[from the steps]** R1–R8, R10; the consequences of §8.
- **[from the repo]** The tube primitive, passive nodes, the acknowledged finer
  layer, bare-speed equality, chirality as a background gauge field.
- **[reading]** Stretch ↔ scalar, twist ↔ signed (§5).
- **[open]** The fork (§6); the twist's vector character; a largest delay;
  everything in §9.
