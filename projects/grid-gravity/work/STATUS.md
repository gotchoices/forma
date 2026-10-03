# STATUS — grid-gravity tracker

Living document. Tracks the active line of work (the mechanism 3 validation
plan), then indexes the work files. Update as steps complete.

**Project state (2026-10-02):** Mechanisms 1–2 parked on the range crux (record
in [../README.md](../README.md)). **Mechanism 3**
([sync-carrier-mechanism.md](sync-carrier-mechanism.md)) is validated for the
**static sector** — reproducing weak-field general relativity through second
order (γ = β = 1, 1/r² fall in 3D, mutual attraction, source ∝ energy) —
conditional on a listed ledger of posits. The **dynamic sector** (tensor waves,
frame-dragging) is open. The statistical (Jacobson) account is taken as the same
phenomenon at a coarser level (posit P8). A ten-chapter arc for the static sector
is drafted in the README. The statistical side is held in
[entropic-route.md](entropic-route.md); an EM slot in [em-slot.md](em-slot.md).

### At a glance — what is left

| Area | Item | Detail |
|---|---|---|
| **Dynamic sector** (main gap) | a local re-timing / re-labelling symmetry so only the two tensor polarizations radiate; frame-dragging (a universal non-reciprocal element); face-diagonal links for the second polarization | task 1 below; [tensor-extension.md](tensor-extension.md) |
| **Static sector** | **derived, conditional on the ledger** (P1–P9). Posits that would be strengthened by a derivation: P7 (rigid ring). The softening rule is now an explicit posit (P9); *why* a lattice softens is interpretive and optional | tasks 2, 2a; [mechanical-readings.md](mechanical-readings.md) §4 |
| **Smaller checks** | both photon polarizations slowed alike; strong field / horizons (5f); light-on-light and second-harmonic rate (5d); a direct 3D light-deflection run | tasks 3–6 |
| **Held open** | EM slot (E1–E3); area-entropy and stiffness ↔ ζ (bonus); free energy of two inclusions in 3D | tasks 7–9 |
| **Writing** | outline Chapters 1–3 from the README arc, then fill in one at a time | — |
| **Inputs to review** | new musings in [../../thoughts.md](../../thoughts.md) | — |

---

## Mechanism 3 — validation plan

Ordered so that the mechanism can fail early and cheaply. Each step states what
would count as a pass and what would end or redirect the line. A condition the
posits satisfy *by construction* (static 1/r, isotropy) is not on this list —
it is not evidence (README ground rule 9).

| # | Step | Kind | Pass looks like | Ends / redirects if | State |
|---|---|---|---|---|---|
| 1 | **Uniform-q theorem.** A concrete local lossless rule; exact spectrum with the carrier uniform; carrier speed. | derivation + exact numerics | light speed, rest frequency and inertia rescale by one factor; carrier speed = c untuned | no rule rescales them together (→ an optical medium, not time dilation) | **passed** — [uniform-q-theorem.md](uniform-q-theorem.md) |
| 2 | **Drop test.** Impose a static gradient of the storage weight on an (x, c) lattice; release packets of different k and compact mode n. | simulation (cross-check of step 1) | one acceleration for all, equal to −c²·∇(ln of the rate); small reflection | acceleration depends on k or n (equivalence fails); strong reflection at gentle gradients | **passed** — [drop-test-result.md](drop-test-result.md) |
| 3 | **Lattice action and the light-bending parameter γ.** One Lagrangian: wave field + carrier + coupling to energy density. Read off source ∝ energy, action–reaction, and γ. | derivation | source ∝ energy with one sign; a stated, natural spatial partner that gives γ = 1 | γ = 1 requires an unnatural or tuned partner | **passed at first order** (one new posit, two flags) — [action-and-gamma.md](action-and-gamma.md) |
| 4 | **Switch-on in 3D.** Constant source on the canonical scatter; watch the static pattern build. | simulation | static 1/r inside a front moving at c | the dynamics do not relax to the static field | **passed** — [switch-on-result.md](switch-on-result.md) |
| 5 | **Strong field.** Dead-band edge, slip, horizon radius versus M. | simulation (nonlinear) | horizon radius ∝ M; exterior field intact | radius ∝ √M, or exterior field screened | **mostly done** — run as a requirements search ([requirements-and-dof.md](requirements-and-dof.md)); sub-items below; open: 5d remainder, 5f |

**Pre-registered expectations** (written before the step is run):
- Step 2: acceleration −c²∇ln(1 − q), independent of k and n; reflection
  vanishing as the gradient length grows past a wavelength.
- Step 3: the node-level rule of step 1 alone gives **γ = 0** (half the observed
  bending); γ = 1 needs an equal, additional slowing on extended edges only.
- Step 5 (added after step 3): a real standing wave with a dynamical carrier
  will radiate at twice its rest frequency; the nonlinear rule must realize the
  polarizable-vacuum form of the carrier's Lagrangian for β = 1.
- Step 4: unknown. grid-duality recorded that the scatter's dynamics did not
  relax to the static field under *pinning* in 2D; sourcing in 3D is untested.

**Scope note for step 5 (written after step 4).** Steps 1–4 tested the pieces
with the loop open: an imposed storage profile (1–3) and an imposed source (4).
Step 5 closes it — a standing wave sources q through the action; q sets the
storage weights; those slow the wave and everything near it — and then pushes it
to strong field. It carries three questions forward: (a) the breathing source of
a pure standing wave; (b) which nonlinear completion the lattice realizes, hence
β; (c) the dead-band edge, slip and the horizon radius. It is the first step
that is genuinely nonlinear, and the first where a design choice (how q sets Y
and Z, and how q's own propagation is loaded) has to be made rather than
derived.

**Step 5 is run backwards.** There is no mechanism to appeal to for *how* a node
or edge would carry the added degrees of freedom, so step 5 does not pick a
design. It collects what any implementation must satisfy, counts the degrees of
freedom, and scans the remaining choices against observation
([requirements-and-dof.md](requirements-and-dof.md)). Sub-items:

| # | Item | State |
|---|---|---|
| 5a | Requirements list (R1–R10), degrees-of-freedom ledger, lattice-level vocabulary | done |
| 5b | β: which loading gives β = 1 when the carrier propagates like light | **done** — each member's delay linear in the deflection; identical to the polarizable-vacuum form; resolves step 3's β flag at requirement level |
| 5c | Closed-loop simulation with that rule — separate-channel branch | **passed** — [closed-loop-result.md](closed-loop-result.md) |
| 5c′ | Same-channel branch: derive the exact conservative lattice rule from the action, *then* simulate | **passed** — [same-channel-result.md](same-channel-result.md) |
| 5d | Same-channel branch hazards: second harmonic, light-on-light | **partly done** — second harmonic found to be *resonant* (rate in matter not estimated); light-on-light not examined |
| 5e | Breathing source | **settled by argument, flag corrected** — a pulsing source radiates only through its form factor at half a Compton wavelength (step 3's lifetime assumed a point source); circulating source steady to machine precision; direct numerical check **inconclusive** |
| 5f | Strong field, with and without a largest delay (horizon only with one; radius ∝ M) | queued |
| 5g | **Direct 3D inverse-square check:** a massive body released in the 1/r deflection of a point source, at several distances | **passed** — [drop-3d-result.md](drop-3d-result.md) |

**Conceptual items (no computation yet):**
- One gravity, not two: *settled as a stance* — the mechanism and the Jacobson
  result ([grid/gravity.md](../../../grid/gravity.md)) are taken as two levels of
  one phenomenon (posit P8), judged by consistency where both speak. Open within
  it: the dynamic sector (see the audit below).
- Does one carrier rescale the clocks of every sheet alike?
- **EM slot (held open):** charge as a time *shear* — a signed clock offset per
  compact lap, seen only by circulating modes — beside gravity's time *stretch*.
  Reasoning, circuit picture and a three-rung test ladder (E1–E3) in
  [em-slot.md](em-slot.md). Nothing computed yet; to be taken up after the
  gravity plan.

**Statistical side — open computation:** free energy of two pinned inclusions
versus separation, in 3D ([entropic-route.md](entropic-route.md) §4).

## Objectives audit (after step 5c′; criteria revised)

**What success means** (README, "Relationship to the statistical account"). The
statistical (Jacobson) account and this mechanical one are taken to be two levels
of one phenomenon (posit P8). Validity does not require deriving one from the
other. Required: (1) reproduce observed gravity wherever the mechanism speaks;
(2) never contradict the statistical account where both speak. Bonus: illuminate
the statistical account's premises. *(Earlier the README made deriving Jacobson's
entropy law "the payoff"; that criterion has been relaxed to a bonus.)*

| Objective | State | Evidence / what is missing |
|---|---|---|
| Clear the gate: (0) vacuum field, (1) massless 1/r isotropic, (2) non-dispersive, (3) coupling a fixed constant ∝ mass-energy | **met**, conditional on the ledger | (0),(1) reached *dynamically* at light speed (step 4); (2) exact universal map (step 1); (3) derived from the action (step 3). The static 1/r is a property of the posit — labelled as such. |
| **Observed gravity, static sector:** time dilation, universal free fall, inverse square, light bending (γ), perihelion (β) | **met, on one premise** | Steps 1–5; γ = 1 from impedance-matched loading, β = 1 from delay linear in deflection. Rests on P7 (compact loop loaded once). |
| **Observed gravity, dynamic sector:** tensor gravitational waves (LIGO–Virgo polarization tests; binary-pulsar orbital decay), frame-dragging (Gravity Probe B, LAGEOS) | **not met — the mechanism is incomplete here** | One scalar deflection radiates as a scalar; reciprocal stores give no frame-dragging. Candidate extension: a memory on each link (its source, stress along the link, is already in the derived rule). Nothing computed. |
| Consistency with the statistical account where both speak | **holds in the static weak field through second order; open for radiation** | Same gap as the row above: the statistical account gives the tensor Einstein equations. |
| Non-dispersivity for full MaSt sheets (ground rule 7) | **met** | Step 1's closed form holds for any number of axes; with two compact directions every (m, n) sheet mode slows by the same factor to ~10⁻⁵. |
| Reconcile the local-clock premise with the confirmed Maxwell results (ground rule 5) | **met for a scalar wave; one check outstanding** | Stores vanish at zero deflection; the photon stays gapless under load; junctions need no clock. *Not shown:* both photon polarizations slowed alike in [grid-primitive](../../grid-primitive/)'s two-component wave. |
| Results come from the rule, prediction before run, not built into the setup | **met**, except the static 1/r (built in, and labelled) | Several first runs were wrong and are recorded as such. |
| *Bonus:* illuminate the statistical premises — area-entropy, dS/dt, stiffness ↔ ζ | **not attempted** | Hooks only: slipped edges lie on a surface; in the one-field branch the strength of gravity is not free, so stiffness ↔ ζ is in principle checkable (needs the quantum of action from grid-quantization). |
| EM force | **slot held open by design** | [em-slot.md](em-slot.md); nothing computed. |

**Verdict.** For the **static sector** the project's objective is met,
conditionally: a lattice mechanism that passes its gate and reproduces weak-field
general relativity through second order, posits listed. For the **dynamic
sector** it is incomplete, and that — not the entropy law — is the main open
task. The chapter arc can be written now for the static sector; the dynamic
sector is reported as open in Chapter 10.

### Tasks remaining for the work folder

In rough order of how much they would change what the project can claim:

1. **The dynamic sector.** *First pass done*
   ([tensor-extension.md](tensor-extension.md)): the loadings are the metric
   perturbation (node ↔ time–time, link ↔ space–space along it); P6 + P7 are
   general relativity's static solution transcribed; self-fed per-link memories
   **fail** (γ = 0); the feeding rule that reproduces the linearized field
   equations is found (each link: flow along it plus an equal share of the rest
   energy). **What remains is not a degree of freedom but a symmetry:** for only
   the two tensor polarizations to radiate, re-timing a node or re-labelling a
   neighbourhood must change nothing physical — the gravitational counterpart of
   what axiom A4 does for phases. Whether the lattice can carry that is the open
   question. Also open: the universal non-reciprocal element for frame-dragging;
   face-diagonal links for the second polarization.
2. **The compact-loop premise (P7).** Now read as "rigid ring, elastic space" —
   the compact circumference is held by the embedding, so the trapped light's
   outward push goes into S ([mechanical-readings.md](mechanical-readings.md)
   §3). Still to be derived from where the circulation lives (grid-primitive's
   tube). Full light bending depends on it.
2a. *(Optional — interpretive, not blocking; the behaviour is posit P9.)* **The node half of the response.** Why a junction's effective inertia rises
   under load (clocks slow) — the link half has a string-tension reading, the
   node half none. The one causal gap left in the static sector.
3. **Both polarizations.** Put the stores into grid-primitive's two-component
   wave and check that they slow both alike.
4. **Strong field (5f).** With and without a largest delay; horizon radius
   against M.
5. **Same-channel hazards (5d remainder).** Light-on-light scattering; the rate
   of the resonant second harmonic in dense matter.
6. **A direct 3D light-deflection run** with matched stores — the counterpart of
   the 3D drop.
7. **EM slot**, rungs E1–E3.
8. *Bonus:* the statistical premises — area-entropy of the lattice with these
   memories; stiffness ↔ ζ.
9. **Statistical side:** free energy of two pinned inclusions against
   separation, in 3D ([entropic-route.md](entropic-route.md) §4).

*Blocked elsewhere:* a closed loop in three dimensions needs a particle that
stays bound in 3D — [grid-matter](../../grid-matter/)'s open problem.

### Step log

- **Step 1 — passed.** Rule: one storage register of weight Y per node, its
  share returning to the same node next tick, on the canonical (end-register)
  scatter. Exact spectrum cos ω = (2Σcos k_a + Y)/(N+Y); universal map
  sin(ω_Y/2) = sin(ω_0/2)/√(1+Y/N); rate factor 1 − q = 1/√(1+Y/N). Failures
  identified: inverted return → photon mass; direction-labeled registers →
  anisotropic. Side finding: the direction-labeled scatter is anisotropic in
  three axes even unloaded (affects grid-matter's 3-axis two-slit numbers, not
  its 2-axis results; written up in
  [grid-matter/review.md](../../grid-matter/review.md)).
- **Step 2 — passed.** In a uniform gradient of Y, packets of three different
  masses fall together at a = g/(4+Y)² (sim/exact 0.996–0.999; the mass
  dependence is the predicted 1/cos²(ω₀/2), i.e. order (rest frequency ×
  tick)²). Moving massive packet and photon follow the ray equations to 0.02%;
  the photon is delayed. Reflection: 1% at an abrupt 18% speed step, < 10⁻⁴
  once the ramp exceeds ~1.5 wavelengths. Expectations met as pre-registered;
  the one addition is the speed-dependence a ∝ (1 − 2v²/c²), which is the γ = 0
  signature in one dimension.
- **Step 3 — passed at first order.** (a) The source is *derived* from the
  action: ∝ energy, one sign, always attractive; light sources twice as
  strongly per unit energy as matter at rest (as in GR); G = 1/(16πκ), a
  calibration. Posit P3 is retired. (b) γ = δμ_x/δε: node storage alone gives
  0 (as pre-registered); **equal loading of nodes and extended edges gives
  γ = 1, and that equality is the impedance-matching (reflectionless)
  condition** — exact spectrum 1.0000, time-domain 0.9997, matched abrupt step
  reflects 36× less than unmatched, rest-packet acceleration carries the GR
  factor (1 − 3v²/c²). Dual sign rule: node storage returns same-sign, edge
  storage returns inverted; the opposite in either place is a photon mass.
  (c) New posits: P6 (extended edges store too, loaded equally), P7 (the
  compact loop is loaded once — not by space-edge storage). (d) **Flags:** a
  purely standing wave is a breathing source and would radiate carrier waves
  (removed if the particle travels around a compact cycle, or by whole-quantum
  energetics); β is undetermined until the nonlinear completion is chosen —
  of three candidates only the polarizable-vacuum form gives β = 1. (e) The
  R_ℵ-stretch candidate cannot be the carrier's whole effect (it bends no
  light).
- **Step 4 — passed.** A steady source switched on in a 241³ canonical-scatter
  lattice builds q = 6s/(4πr) behind a front at the lattice light speed:
  q·r = 0.4775 against 0.4775 predicted (ratio 1.0000), anisotropy < 0.2% beyond
  r ≈ 16, front speed 0.575–0.581 (1/√3 = 0.577) in three directions, no drift;
  V → 0 behind the front; link flux ∝ 1/r². Switched off, the potential leaves
  as a wave (residue ≤ 0.3%). **Structural result:** the carrier's potential q is
  the *running sum* of the node value — a stored accumulator — while the
  registers carry its rate and gradient (refines P2). grid-duality's earlier 2D
  negative is likely a property of two dimensions (the potential of a
  switched-on source grows logarithmically there), not of the scatter.
- **Step 5a–b — done.** The scatter's "sum minus own value" is reflection at a
  junction of N equal lines (coefficient 2/N − 1): the edge negates, the node
  only joins; equal transit times replace a clock; storage is the only way to
  slow without breaking timing. Requirements R1–R10 and a degrees-of-freedom
  ledger recorded. Vocabulary fixed at lattice level (deflection, deflection
  rate, tension, node inertia, link compliance). Fork opened: carrier as a
  second channel, or as the rectified zero-frequency part of the one channel
  (no free stiffness). **β = 1 ⇔ each member's delay is linear in the
  deflection** (static solution 1 + q/2 = e^(GM/r), verified symbolically);
  this is the polarizable-vacuum form in another variable. It has no horizon
  unless the lattice has a largest delay, in which case the radius ∝ M.
- **Step 5a addendum.** Clocking: a junction is linear and scatters each arrival
  on its own, so no clock and no synchronization are needed; the tick is the
  unloaded transit time. Slowing can be storage (needed if strictly
  tick-synchronous; what the sims use) *or* longer transit at unchanged
  impedance (exactly reflectionless) — equivalent at long wavelength; an earlier
  "storage is forced" statement was corrected. Branch B′ recorded: light/matter
  = the oscillating part of grid-primitive's two tube degrees of freedom,
  gravity = the steady part of the stretch-like one, charge = the steady part of
  the twist-like one — no new wave degrees of freedom, only the node memory.
- **Step 5c — passed (separate-channel branch).** Loop closed: waves source q, q
  sets the stores by the linear-delay rule, waves respond. Two lumps (masses 1
  and 3) released at rest fall toward each other; each follows the ray law in
  the jointly produced field (sim/ray 0.998, 1.011); acceleration ratio 3.22 →
  3.06 and momentum imbalance 0.8% → 0.4% as the field weakens (mass ratio 3);
  equal masses symmetric; norm conserved to 10⁻¹³. One extended dimension (a
  constant pull, not 1/r²). Trap recorded: a light narrow packet spreads across
  the midpoint and corrupts the centroids.
- **Step 5g — passed.** Asked directly: does a body fall as 1/r² in three
  dimensions? Yes — a ∝ r^−1.96 over r = 24–64 (r^−1.98 beyond 32); a/a_ray =
  0.996–0.999 for r ≥ 32; identical on a body diagonal and an axis; a·r² → 0.0379
  against 0.0383 predicted. Departures at small r are extended-body effects (the
  packet is half as wide as its distance at r = 24). Why 5c showed no falloff: one
  extended dimension gives a node one edge in and one out, so nothing is shared;
  in 3D the scatter divides a steady tension among a node's edges, flux through a
  shell is conserved, and each edge carries 1/r².
- **Steps 5c′, 5d, 5e.** *Rule derived:* in Hamiltonian form the state is node
  momentum P and link extension e; when a store's weight changes, P and e carry
  through (not the stored energies), and the back-reaction ½M′v² + ¼ΣC′T² on the
  deflection appears unasked — always positive, ∝ energy. *Same channel works:*
  one real field, no coupling constant; two circulating lumps (energies 1 : 3)
  rectify a steady deflection 30× their own amplitude and fall into it — ray law
  0.998 / 0.999, acceleration ratio 3.13, momenta balanced to 0.2%, energy drift
  7×10⁻⁴ halving with the time-step (integrator). *Hazard found:* the compact
  tower is harmonic, so second-harmonic generation (two n = 1 quanta → one
  n = 2) is resonant; 4% amplitude in the run; rate in real matter not
  estimated. *Flag corrected:* step 3's "2 million years" for a standing proton
  assumed a point source; with the wave packet's form factor the radiation is
  suppressed by ~10⁻²⁰ or more. *Inconclusive:* a direct numerical check of that
  suppression (narrow lumps spread too fast; test mode removed).
- **Dynamic sector, first pass.** Dictionary (checked symbolically): with the
  compact loop unloaded, node loading = h₀₀ and the loading of a link along a =
  hₐₐ. GR in lattice words — rest mass: node 2U, every space link 2U, compact
  untouched (= P6 + P7 exactly); light beam along x: node and x-links 4U,
  transverse links 0; gravitational wave: links only, opposite signs on two
  perpendicular directions. So one scalar matches GR for sources at rest, departs
  in the space–space part for anisotropic sources, and cannot carry a tensor wave.
  Self-fed independent link memories give γ = 0 (a rest mass has no tension along
  space links). The rule that works feeds each link by the energy flowing along
  it plus an equal share of the rest (compact-circulation) energy, and the node
  by its rate energy less that share — reading: trapped radiation presses equally
  on all the links that confine it. Remaining obstacle: with every memory an
  independent positive-energy wave the node's loading would radiate too; only a
  local re-timing / re-labelling symmetry removes that (and then the dynamics are
  Einstein's, by the standard uniqueness result).
- **Mechanical readings recorded.** Memory dissolves into static deflection (the
  register scatter tracks rates; a lattice node simply is where it is); the dead
  band is an unanchored lattice; P7 is a rigid ring held by elastic space; the
  source is the back-pressure of trapped light — found independently from GR's
  feeding rule; the response (softening under load) is the one physical posit
  left, with a string-tension sign argument for links and nothing yet for nodes.
  Graviton: a scalar carrier candidate exists (massless, at c, energy-sourced);
  spin-2 is latent in the link-loading tensor (elastic shear waves) but the
  compressional mode would also radiate — the local-symmetry gap.

---

## Work files

**Mechanism 3 (active)**
- [sync-carrier-mechanism.md](sync-carrier-mechanism.md) — the proposal: ledger
  of posits, roles of synchronization and carrier, conditions for range,
  horizon and charge readings, hurdles.
- [uniform-q-theorem.md](uniform-q-theorem.md) — step 1 result.
- [drop-test-result.md](drop-test-result.md) — step 2 result.
- [action-and-gamma.md](action-and-gamma.md) — step 3 result: the action, the
  derived source, γ and impedance matching, the two flags.
- [switch-on-result.md](switch-on-result.md) — step 4 result: dynamic
  relaxation to 1/r at light speed; the potential as an accumulator.
- [mechanical-readings.md](mechanical-readings.md) — the requirements re-read as a
  mechanical lattice: no memory (static deflection), unanchored nodes (massless),
  rigid ring in elastic space (P7), back-pressure of trapped light (the source),
  softening under load (the one remaining physical posit).
- [tensor-extension.md](tensor-extension.md) — the dynamic sector, first pass:
  the loading ↔ metric dictionary; P6 + P7 as GR's static solution; the negative
  for self-fed link memories; the feeding rule; the missing local symmetry.
- [same-channel-result.md](same-channel-result.md) — steps 5c′/5d/5e: the
  conservative rule derived; one field with no coupling constant rectifies its
  own gravity; the resonant second harmonic; the breathing flag corrected.
- [drop-3d-result.md](drop-3d-result.md) — step 5g result: a body falls toward a
  point source as 1/r², in three dimensions, isotropically.
- [closed-loop-result.md](closed-loop-result.md) — step 5c result: two lumps
  make a field and fall into it; third law and momentum conservation emerge.
- [requirements-and-dof.md](requirements-and-dof.md) — step 5 opening: the
  lattice-level vocabulary, what a junction already does, requirements R1–R10,
  the degrees-of-freedom ledger, the stretch/twist reading, the channel fork,
  and the β result.

**EM slot (open)**
- [em-slot.md](em-slot.md) — where an electromagnetic effect fits; why the
  gravity carrier cannot supply it; how it would be tested.

**Statistical side**
- [entropic-route.md](entropic-route.md) — what "entropic" means; parked
  two-body and charge hypotheses with their obstructions.

**Shared foundations**
- [local-time.md](local-time.md) — the four commitments (delay in edges; finite
  bandwidth; slow light = slow time; coordinate vs proper time).
- [simplified-model-and-mast.md](simplified-model-and-mast.md) — the mass-only
  simplification and what must be re-derived in full MaSt.
- [micro-to-macro.md](micro-to-macro.md) — the vacuum-field condition; the
  built-into-the-setup trap.

**Mechanism 1 (congestion) — record**
- [congestion-falloff.md](congestion-falloff.md),
  [update-rule.md](update-rule.md), [shunt-check.md](shunt-check.md) (loss ⟺
  Yukawa), [falloff-sim-result.md](falloff-sim-result.md),
  [dispersion-sim-result.md](dispersion-sim-result.md).

**Mechanism 2 (detour / refractive) — record**
- [detour-refractive.md](detour-refractive.md),
  [energy-coupling.md](energy-coupling.md),
  [aleph-grounding.md](aleph-grounding.md) (even → gravity, odd → charge),
  [mode-coupling-derivation.md](mode-coupling-derivation.md) (first pass; gauge
  artifact), [gauge-invariant-coupling.md](gauge-invariant-coupling.md) (the
  coupling is an index), [loops-and-range.md](loops-and-range.md),
  [range-from-foundations.md](range-from-foundations.md) (the carrier
  requirement).

**Scripts** ([../scripts/](../scripts/))
- `carrier_dispersion.py` — exact Bloch spectrum with a node storage register
  (step 1).
- `drop_test.py` — packets in a gradient of the storage weight; reflection
  from a ramp (step 2).
- `gamma_test.py` — node + edge storage: anisotropic spectrum, γ, reflection
  at a matched step, matched-gradient drop (step 3).
- `switch_on.py` — steady source switched on (and off) in 3D (step 4).
- `drop_3d.py` — a massive packet released in a 1/r deflection in 3D (step 5g).
- `same_channel.py` — one real field with the derived conservative rule; lumps
  rectify their own deflection and fall into it (steps 5c′, 5d).
- `closed_loop.py` — two lumps source the deflection, the deflection loads the
  lattice, the lumps respond (step 5c).
- `gate_falloff.py`, `gate_dispersion.py`, `hex_greens.py` — mechanism 1–2 gate
  sims.
