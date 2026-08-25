# grid-saturation

**Type:** Exploratory, computational-first project (see [../README.md](../README.md))
**Scope:** Whether the **bounded/saturating** GRID substrate — the same
discrete-max bound already posed for light-quantization — reproduces, as
*dynamics*, the quantum phenomena the *linear* grid (Maxwell) cannot:
the quantization threshold, **pair production** (energy moving S ↔ compact),
**single-quantum instantiation** (collapse/measurement), and the **Born
rule**. Tested on a minimal **1D-space + 1D-compact (x, c) cylinder**.
**Status:** Sim built ([scripts/cylinder.py](scripts/cylinder.py)). **M1
verified** — photons propagate in x, pass through each other, the compact
sector is decoupled (E(n≥1)=0), and the winding mode is massive/gapped, all as
KK predicts (first dynamical test of this in forma). **M2 negative-so-far, not
refuted, and it redirected the project.** Two results: (1) with a physical
**vacuum seed**, saturation (clip *or* spillover) pumps **no** persistent
compact mode above the linear control at any frequency (an earlier "+0.7%
signal" was a source-seed artifact — the seed is gapped and never reaches the
collision); (2) the **trap test** (excite a compact mode directly, at rest)
shows a saturating value-bound is a **defocusing** nonlinearity — it flattens
peaks, so retention *falls* with saturation depth, the opposite of a soliton.
**So the value-bound cannot bind a particle by self-focusing.** Two candidate
binding mechanisms remain, both untested: **(i) discreteness** — an indivisible
'1' can't leak fractionally, so a quantum is trapped until it escapes whole
(Peierls–Nabarro pinning; most GRID-native, needs no new field); and **(ii)
topology** — a particle as a **phase winding** of the ℵ-line (*charge =
winding*). A crude `--quantize` probe of (i) was inconclusive (it freezes the
whole lattice — a photon stops propagating too), showing the real construction
needed: an **integer, energy-conserving scatter** where photons still propagate
but fractional leakage is forbidden. Full account in
[work/results-m1-m2.md](work/results-m1-m2.md). Computational-first: build the
minimal sim and observe, then return to math.

---

## The through-line

Across the framework, almost every distinctively-quantum feature GRID does
*not* yet deliver — quantization, wavefunction collapse, the Born rule,
pair production — waits on the **same** missing ingredient: a **nonlinearity**.
The confirmed grid ([grid/sim-maxwell](../../grid/sim-maxwell/)) is *linear*
(exact superposition), which is exactly why it gives **Maxwell** and nothing
more.

**The key realization of this project:** the nonlinearity is not a separate
mystery. It is the **saturation** — the discrete-max / ±1 bound already posed
as the origin of quantization ([grid-quantization](../grid-quantization/),
`work/energy-and-coherence.md`). A bounded value that cannot scale
arbitrarily *is* a saturating nonlinearity. So the same bound that quantizes
light should also, in the right regime, produce the rest. One mechanism,
three regimes:

| Amplitude regime | Behaviour | Yields |
|---|---|---|
| **Below saturation** | effectively linear | Maxwell / free propagation |
| **Windowed (sigma-delta)** | many sub-quantum values per window | apparent large dynamic range |
| **At saturation** | genuinely nonlinear | quantization, pair production, instantiation |

"Firing two photons head-on" is simply a *deliberate* way to drive the field
into the saturation regime (amplitudes add at the collision) — the same
high-intensity condition under which real pair production occurs.

## The testbed: the (x, c) cylinder

The minimal setting: **1D space x** (S) × **1D compact c** (Ma), wrapped into
a **cylinder** — x along the axis, c periodic around the circumference. Every
x carries the *full* compact ring (fiber bundle); there is **no
high-coordination node** — "position x" *is* the column of c-nodes, each an
ordinary low-coordination lattice node (edges ±x and ±c). A photon is the
**c-uniform (n=0) mode** propagating in x; a particle is a **c-winding (n≥1)
standing wave** localized in x.

## Phenomena to test (each a milestone)

**M1 — KK decoupling (linear baseline).** Does a photon propagate cleanly
along x with the compact dimension present, and do two photons pass through
each other? Linear theory says yes (mode orthogonality); **forma has never
tested this dynamically** (all wave sims are 2D-flat). Cheap, and it
validates the baseline before any nonlinearity is added.

**M2 — Pair production (the saturation event).** Two counter-propagating
photons have **zero net S-momentum** (the CM frame) and total energy 2E.
Driven to saturation at the collision, the excess is **redirected into c**,
seeding a **standing wave circulating the tube** — a particle at rest.
Requirements, all GRID-native:
- *Momentum:* zero-net-momentum in → zero-momentum (rest) particle out. ✓
- *Threshold/resonance:* the energy must match a c-eigenmode (ℏω_c = rest
  mass); off-resonance the photons pass through. So it happens "in the right
  instance," like a real cross-section, not every collision.
- *Charge / angular momentum:* a 1D-compact standing wave has **no net
  circulation** — it is a **+winding and a −winding at once**. Splitting into
  the two opposite windings is exactly **particle + antiparticle**
  (matter/antimatter = opposite winding sign, [metric-charge](../metric-charge/)),
  with charge and angular momentum conserved (equal and opposite → the zero
  input). The "no direction" *is* the conservation backbone.

**M3 — Single-quantum instantiation (collapse).** If the total is one
quantum's worth of energy and instantiation needs a *full* bit locally, then
energy conservation guarantees **at most one full quantum at a time** → one
detection; once absorbed, it is gone from the field. The *fractional* field
still spreads and **interferes** (the loops/paths differ with one slit vs
two), so the click statistics carry interference while the click is single —
the pilot-wave / Bohm structure, GRID-native, and matching grid-quantization's
own "magnitude washes out / energy is a conserved integer" split.

**M4 — The Born rule (the prize).** The accumulated field *energy* density is
∝ **|field|²** (wave energy ∝ amplitude²). So "instantiate where enough
energy has accumulated to cross threshold" gives P(click at x) ∝ energy(x) ∝
**|field(x)|²** — the Born rule *out of* the dynamics, not assumed. For a
single photon this is the correct semiclassical "detection ∝ intensity." This
is the most distinctively-GRID result available; deriving Born from a realist
substrate (where Bohm/Everett/Barandes must posit or add equilibrium) would
be genuinely new. Multi-particle/entangled Born is a further, harder step.

## The saturation *mechanism* — storage vs spillover

*What* the node does with the excess at saturation is the crux, and it must
be **energy-conserving** to see a real S → c *transfer* rather than loss:

- **Naive clip [lossy — insufficient].** Discard the excess. Energy *vanishes*
  from S at the collision but does **not** reappear in c — it is just lost.
  Cheap to code, suggestive only.
- **Storage / sigma-delta [conserving; temporal redirect].** The node buffers
  the excess an edge can't take and releases it next cycle (grid-quantization's
  bit-conserving accumulator). Excess redirected in **time**.
- **Spillover [conserving; dimensional redirect — the preferred candidate].**
  The node has *no* storage, but when one edge saturates the excess **spills
  into the other edges**. When the *x*-channel saturates (head-on collision),
  the excess is forced into the orthogonal **c** edge — a "pressure-relief
  valve" that **redirects energy S → c precisely by geometry**. This is
  cleaner than storage for pair production: it needs no node memory and it
  routes the excess *into the compact dimension by construction*. Reversible:
  c saturating spills back into x = **annihilation**. Whether the spillover
  actually seeds a *stable* c-standing-wave (vs leaking back) is governed by
  the M2 threshold/resonance.

Both conserving behaviours are candidates; the spillover is the one to try
first for the S ↔ c transfer.

## Sim plan (computational-first)

1. **Linear cylinder** → M1 (pass-through, KK decoupling). Feasible now.
2. **Add a naive clip** → confirm head-on collisions reach saturation and
   something nonlinear happens (but lossy — energy disappears, not transfers).
3. **Add a *conserving* saturation (spillover first, then storage)** → test
   M2 (energy lands in a c-standing-wave at threshold, momentum conserved),
   then M3–M4 (single instantiation; is the click distribution ∝ |field|²?).

Step 3 is the real result; it is the same bit-conserving substrate that also
underwrites quantization — **build it once, it pays for M2, M3, M4, and
grid-quantization at once.**

## Why this is more than wishful — the connective threads

- **The grid-gravity lesson (a real consistency check).** The saturating
  *value*-bound is the **wrong** flavour for gravity — it gives a *mass*
  (potential/contact), not the *metric* (kinetic/long-range) gravity needs,
  which is why [grid-gravity](../grid-gravity/) blocked. But pair production
  **wants** a mass and **wants** energy to leave S into c — so the very
  mechanism that killed the gravity thread is the **right** one here.
  Different job, opposite verdict.
- **Reiter / threshold theory — pick the right one.** Reiter's *loading*
  theory predicts a single photon can trigger **multiple** detections — which
  single-photon **anticorrelation** experiments (Grangier–Aspect–Roger 1986+)
  contradict. GRID must use the **conserved-snap** (one quantum → one
  detection), *not* Reiter's loading. See
  [primers/threshold-theory.md](../../primers/threshold-theory.md) (which
  needs this distinction added).
- **Non-locality (Bell + collapse are the same fiber).** Instantiating one
  full quantum from a fractionally-spread field requires *collecting* the
  distant energy — which causal S cannot do instantly. The **compact fiber**
  is the candidate non-local channel, and it is the same non-locality a
  realist theory needs for **Bell**. One fiber may pay for both.
- **Barandes (QM = non-Markovian stochastic process).** For the fractional
  field to *interfere* (not just diffuse), the fork-weights must be
  **correlated / non-Markovian**, not independent local coin-flips — exactly
  Barandes's result. Interference lives in the correlation; single detection
  in the conserved quantum.

## Honest status and caveats

- The saturating substrate is **posed, not simulated**; its *dynamics* are the
  unbuilt object. This project's job is to build and observe them.
- Whether saturation traps into **c specifically** (vs merely distorting the
  wave / making x-harmonics) is **untested** — M2 decides it.
- The **energy-conserving** saturation (storage/spillover) is the delicate
  construction; the naive clip is lossy and only suggestive.
- The **Born rule** (M4) and the **non-local collection** (M3) are the hard
  cores; GRID has candidate *ingredients* (energy ∝ |field|²; the fiber), not
  proofs.
- Given a repeated pattern of over- and under-claiming in adjacent threads,
  results here must come from the **sim**, graded honestly, not asserted.

## Relation to other projects

- [grid-quantization](../grid-quantization/) — proposed the bounded /
  sigma-delta substrate for *occupation* quantization; this project builds its
  *dynamics* and extends it to pair production and measurement.
- [ma-domain](../ma-domain/) — its parked
  [threshold-dynamics.md](../ma-domain/work/threshold-dynamics.md) names
  γ → e⁺e⁻ pair production as a load-bearing test; M2 here is the concrete
  testbed for it. (ma-domain's own arc is the fermion *spectrum*, a distinct
  scope.)
- [grid-gravity](../grid-gravity/) — parked; the metric-vs-mass /
  wrong-flavour-for-gravity lesson is the consistency check above.
- [metric-mass](../metric-mass/), [metric-charge](../metric-charge/) — mass =
  compact standing wave; charge = winding; matter/antimatter = winding sign —
  the objects M2 creates.

## Roadmap — what to prove next, ordered by decisiveness

The milestones above (M1–M4) are the *phenomena*; this is the **order to attack
them in**, by how sharply each can confirm or kill the thesis. It reflects what
experiment A taught: the compact sector is a *stable place a particle could
live*, but no *pump* into it has been found yet.

**Tier 1 — make-or-break (do next).** *(Trap test done: a value-bound is
defocusing, so it cannot self-focus a soliton — [work/results-m1-m2.md](work/results-m1-m2.md)
§M2·A. Two binding candidates remain; test the GRID-native one first.)*
- **A. Discreteness as containment (the integer-conserving scatter).** Build a
  **whole-unit, energy-conserving** discrete scatter (lattice-gas-style, *not*
  `(2/N)J−I` + rounding) and run the **selective-containment control**: does a
  **photon still propagate** while a **compact mode stays trapped**? If yes,
  discreteness binds the particle *and* unifies with grid-quantization. (Crude
  `--quantize` was inconclusive — it freezes everything; see §M2·B.) **Fallback
  if it fails:** give the compact dimension a **phase** (U(1) ℵ-line) and test a
  **topologically stable unit winding** (§M2·A route).
- **B. Does the bound actually *quantize*?** Inject sub-quantum energy (stays
  diffuse, no click?) vs a full quantum (snaps coherently?). The foundational
  "is this substrate even quantum" check; validates the premise behind M2–M4.
  Best done *with* the conserving discrete scatter from A (the crude round is
  non-conserving).

**Tier 2 — the prizes (downstream of Tier 1).**
- **C. Single-quantum instantiation / collapse (M3)** — does energy
  conservation + the bound enforce one detection at a time?
- **D. The Born rule (M4)** — is instantiation ∝ |field|²? The standout result;
  needs C working.

**Tier 3 — enabling / calibration.**
- **E. Is the S→c transfer fraction robust or geometric?** (The honest version
  of "0.7% ≈ α?" — sweep the knobs; a fitting artifact wanders, a real coupling
  converges or is geometric, cf. grid-quantization's (2/3)¹² ≈ 1/130.)
- **F. Widen the resonance search** — sweep nc and amplitude jointly, and try
  `--quantize` as the trap, not just ω.

## Next step

Rather than guess among the three binding candidates (instantiation split,
lattice-gas, topological winding), a **gate** was set — criteria any mechanism
must satisfy — and the candidates scored against it:
[work/binding-evaluation.md](work/binding-evaluation.md). The gate's verdict:
the options are **complementary, not rivals** — **topological winding (III)
binds** the persistent, interfering, charged, massive particle, and the
**instantiation split (I) supplies whole-quantum detection** on top; together
they cover the whole gate. The **lattice-gas (II) is dominated** (it fails
Maxwell + single-particle interference) and is set aside as a fallback.

The I+III path rested on **one unverified, GRID-specific assumption** — that a
**topological winding is stable on the impedance-scatter lattice** — so a minimal
**2-component (phase) field** ([scripts/phase_cylinder.py](scripts/phase_cylinder.py))
was built and the winding tested
([work/phase-winding-results.md](work/phase-winding-results.md)). Outcome: the
winding **is** topologically protected and localized, **but immobile** — a
flat-band state (speed 0 at every momentum kick), so **not yet a genuine
particle**. Likely cause: the **1D-ring compact dimension is too simple** (a flat
massive band = infinite mass). **Next step: a 2D-toroidal Ma-sheet compact
dimension** — does a winding there acquire a finite mass and *move* (a real
particle) while photons still propagate and the winding stays protected? If not,
the lattice-gas (II) returns as fallback. The gate, not a guess, decides.
