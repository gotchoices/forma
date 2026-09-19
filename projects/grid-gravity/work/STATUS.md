# STATUS — grid-gravity tracker

Living document. Tracks the active line of work (the mechanism 3 validation
plan), then indexes the work files. Update as steps complete.

**Project state:** Mechanisms 1–2 parked on the range crux (record in
[../README.md](../README.md)). **Mechanism 3**
([sync-carrier-mechanism.md](sync-carrier-mechanism.md)) is under validation.
The statistical side is held in [entropic-route.md](entropic-route.md).

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
| 4 | **Switch-on in 3D.** Constant source on the canonical scatter; watch the static pattern build. | simulation | static 1/r inside a front moving at c | the dynamics do not relax to the static field | next |
| 5 | **Strong field.** Dead-band edge, slip, horizon radius versus M. | simulation (nonlinear) | horizon radius ∝ M; exterior field intact | radius ∝ √M, or exterior field screened | queued (only if 1–4 survive) |

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

**Conceptual items (no computation yet):**
- One gravity, not two: is the mechanism the microscopic form of the Jacobson
  result ([grid/gravity.md](../../../grid/gravity.md)) — ideally supplying its
  entropy law — rather than a second force?
- Does one carrier rescale the clocks of every sheet alike?
- A signed, winding-selective carrier for charge
  ([sync-carrier-mechanism.md](sync-carrier-mechanism.md) §12).

**Statistical side — open computation:** free energy of two pinned inclusions
versus separation, in 3D ([entropic-route.md](entropic-route.md) §4).

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
- `gate_falloff.py`, `gate_dispersion.py`, `hex_greens.py` — mechanism 1–2 gate
  sims.
