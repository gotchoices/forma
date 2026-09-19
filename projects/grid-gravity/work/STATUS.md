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
| 2 | **Drop test.** Impose a static gradient of the storage weight on an (x, c) lattice; release packets of different k and compact mode n. | simulation (cross-check of step 1) | one acceleration for all, equal to −c²·∇(ln of the rate); small reflection | acceleration depends on k or n (equivalence fails); strong reflection at gentle gradients | next |
| 3 | **Lattice action and the light-bending parameter γ.** One Lagrangian: wave field + carrier + coupling to energy density. Read off source ∝ energy, action–reaction, and γ. | derivation | source ∝ energy with one sign; a stated, natural spatial partner that gives γ = 1 | γ = 1 requires an unnatural or tuned partner | queued |
| 4 | **Switch-on in 3D.** Constant source on the canonical scatter; watch the static pattern build. | simulation | static 1/r inside a front moving at c | the dynamics do not relax to the static field | queued |
| 5 | **Strong field.** Dead-band edge, slip, horizon radius versus M. | simulation (nonlinear) | horizon radius ∝ M; exterior field intact | radius ∝ √M, or exterior field screened | queued (only if 1–4 survive) |

**Pre-registered expectations** (written before the step is run):
- Step 2: acceleration −c²∇ln(1 − q), independent of k and n; reflection
  vanishing as the gradient length grows past a wavelength.
- Step 3: the node-level rule of step 1 alone gives **γ = 0** (half the observed
  bending); γ = 1 needs an equal, additional slowing on extended edges only.
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
  its 2-axis results).

---

## Work files

**Mechanism 3 (active)**
- [sync-carrier-mechanism.md](sync-carrier-mechanism.md) — the proposal: ledger
  of posits, roles of synchronization and carrier, conditions for range,
  horizon and charge readings, hurdles.
- [uniform-q-theorem.md](uniform-q-theorem.md) — step 1 result.

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
- `gate_falloff.py`, `gate_dispersion.py`, `hex_greens.py` — mechanism 1–2 gate
  sims.
