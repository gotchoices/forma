# Chapter outlines — the clean derivation

Outline scaffolding for the seven-chapter presentation arc (README
§"Presentation arc"). **Outlines only — no prose yet.** Each chapter
lists its role, a section skeleton, the raw-material sources, and a
*claim discipline* note fixing what it may and may not assert. Develop
one chapter at a time (project AGENTS.md): outline → prose → review →
check the next chapter still follows → iterate.

Grades: **[derived]** (axioms + computation) · **[reduced]** (standard
physics resting on one GRID ingredient) · **[conjecture]** (graded,
open) · **[scope]** (accounting).

---

## Ch. 1 — The substrate and the junction rule  [derived]

*Role:* establish the discrete medium and its local update — the stage.

- 1.1 The honeycomb lattice: edges as cells, nodes as 3-valent junctions.
- 1.2 The cell state: a periodic, bounded phase (A3) — point on a circle;
  only differences physical; magnitude pinned. *(Introduce compact phase
  before any use of it.)*
- 1.3 The clock (A2): discrete ticks; one update per tick; signal limit
  one edge per tick.
- 1.4 The junction rule `out_i = (2/3)·total − in_i` from energy
  conservation + equal impedance; the −1/3 reflection / 2/3 transmission.
- 1.5 No Maxwell input: geometry + impedance only.

*Sources:* [../../../grid/hexagonal.md](../../../grid/hexagonal.md),
[../../../grid/foundations.md](../../../grid/foundations.md) (A2, A3),
[../../../grid/sim-maxwell/](../../../grid/sim-maxwell/), `../scripts/lib.py`.
*Claim discipline:* inherited/standard — cite, don't re-derive; this is setup.

---

## Ch. 2 — Information becomes a wave  [derived]

*Role:* show an injected static perturbation becoming propagating light
(answers goal 1).

- 2.1 The restoring term: −1/3 reflection = sign-flipped residue = a
  "spring"; a static edge excitation cannot stay static.
- 2.2 Oscillation + propagation: the rule as the discrete wave equation.
- 2.3 Dispersion: measured linear ω ≈ 0.41·k; non-dispersive at long λ.
- 2.4 E, B, and spin: the helical Y-junction eigenmodes (1,ω,ω²),(1,ω²,ω)
  = E ± iB = the two photon helicities — spin/polarization for free.
- 2.5 *What "light" is here:* a propagating edge-wave excitation carrying
  coupled E,B with a definite helicity.

*Sources:* [../../../qa/Q140-light-quantization-from-recirculation.md](../../../qa/Q140-light-quantization-from-recirculation.md) §2,
[../../../grid/fields.md](../../../grid/fields.md), `../scripts/run_recirculation.py` (disp).
*Claim discipline:* wave mechanics is standard; the contribution is the
*identification* light = this excitation. No quantum content yet.

---

## Ch. 3 — The modes of light  [derived]

*Role:* map the spectrum — which excitations exist, each a clean oscillator.

- 3.1 The Bloch band structure: 2 flat bands (ω=0,π) + 4 dispersive bands
  (built empirically from `scatter_step`; cross-checked real-space).
- 3.2 Dispersive bands = free photons (P1: which ω exist); small-k slope
  = the 0.41 phase velocity.
- 3.3 Flat bands (ω = 0, π) = localized, non-propagating **bound modes**
  (the `bound` test; ~½ trapped; *not* the ZPE ½). **Not a massive
  particle:** ω=0 is zero-energy, and there is *no* localized mode at
  generic finite ω — so this is a bound/zero-mode, not "mass" (mass
  proper is MaSt, elsewhere).
- 3.4 Each mode an exact harmonic oscillator (P2): exact superposition.
- 3.5 Scale-invariance: linear dispersion as an IR fixed point; trapped
  fraction size-independent.

*Sources:* `../scripts/band_structure.py`, `run_recirculation.py` (bound,
circ), `loop_scaling.py`, `mode_projection.py`, `scale_invariance.py`;
[tier2-design.md](tier2-design.md) §1–§3.
*Claim discipline:* flat-band CLS are known network physics; the
contribution is the GRID reading (free photon vs mass-like limit).

---

## Ch. 4 — ℏ is a unit, not a target  [reduced]

*Role:* dissolve the "derive h" category error; locate ℏ as a substrate unit.

- 4.1 The category error: ℏ is dimensionful; ℏ = 1 by convention; a
  dimensionless prediction is the right target, not ℏ's scale.
- 4.2 The substrate grains: L (spacing), τ (tick), dW (transition cost).
- 4.3 Constants as grain-combinations: c = L/τ, ℏ = dW·τ; dimensional
  necessity (action = energy × time → only the product has the units).
- 4.4 Absolute scale: a third constant is needed; G = 1/(4ζ) closes it →
  grains = Planck units. *This is an identification (grid-is-fundamental),
  not a theorem; c = L/τ holds only up to an O(1) lattice factor.*
- 4.5 h not derivable from α: a pure number cannot fix a dimensionful
  quantity; e = √(4πα) is the α-definition with ℏ = 1, not a derivation.
- 4.6 What remains dimensionless: ζ and α.

*Sources:* [energy-and-coherence.md](energy-and-coherence.md) §3–§4,
[tier2-design.md](tier2-design.md) §4b, foundations A5/A6.
*Claim discipline:* dimensional analysis + principle-vs-scale; the
Planck-units result is a *consistency*, not a proof the cell is Planck-sized.

---

## Ch. 5 — Why light is quantized: periodicity, not discreteness  [reduced]

*Role:* the core — what light-quantization *is* in the model.

- 5.1 The target: P3 (integer occupation, the one import) + P4 (uniform ℏω).
- 5.2 The key fact: single-valuedness of a **complex amplitude** ψ on the
  compact phase ⇒ discrete (integer) spectrum (Fourier *series*).
  *Periodicity* (not discreteness of values) is the quantizer. (Signals
  analogy: periodic ⇒ line spectrum at integer harmonics.)
- 5.3 The integer *is* the occupation number — the spectrum of
  N̂ = −i∂/∂φ on ψ. **It requires the complex ψ:** a *real* distribution's
  integer index is its *shape*, not occupation. *Distinct from* charge
  (a classical topological winding, no QM) — same circle→ℤ math, different
  objects. ⇒ P3 rests on the ch. 6 import (the complex amplitude).
- 5.4 Two **complementary** routes — topological (the integer label) and
  energetic (the ω-scaling) — both rest on the *same* A5 hinge:
  co-dependent, *not* independent confirmation.
- 5.5 Continuous vs finite: continuous phase → unbounded ladder (QED);
  finite dial (A5) → bounded ladder (GRID deviation). Same circle, two
  resolutions.
- 5.6 Energy scaling: pinned magnitude ⇒ E ∝ ω; fixed quantum is action;
  energy quantum = ℏω = h/period.

*Sources:* [countability-from-information.md](countability-from-information.md),
[energy-and-coherence.md](energy-and-coherence.md) §3, §5, §6.
*Claim discipline:* the math (U(1)↔ℤ, Fourier series) is standard; the
contribution is identifying it as the GRID mechanism. Do **not** claim
the integer comes from a real/stochastic state (it needs the complex
amplitude — ch. 6), nor that the two routes are *independent*
confirmation (they share the hinge). Resolve real-vs-complex before
grading this [reduced]; "what quantization *is*," never "we derived QM."

---

## Ch. 6 — The one imported piece, and the shared root  [conjecture]

*Role:* state the lone hinge honestly and the gravity connection.

- 6.1 The hinge: the state must be a single-valued **complex amplitude**
  over the phase (A5's informational reading) — the quantum state itself,
  not a sharp classical value *and not a mere real distribution* (neither
  triggers §5).
- 6.2 Grade [interpretive]: the one load-bearing assumption — natural
  (A5 is an information axiom), but an interpretation, not algebra.
- 6.3 Shared root with gravity: A5 also gives G (entropy → Jacobson), but
  the two *uses* differ — gravity reads A5 as a **real/statistical**
  entropy count, quantization needs a **complex amplitude**. So "shared
  root" is **unproven** and *harder* than it first looked: bridging
  real-statistical to complex-amplitude is the open task (countability §8).
- 6.4 Stochastic vs quantum (resolved): a real distribution does **not**
  give countability — the complex amplitude is required for P3. Open: can
  A5 supply a complex amplitude at all? (Interference / Born rule further still.)
- 6.5 GRID-specific signatures (graded): bounded occupation ladder
  [predicted]; α-scale leakage coupling 1/129.7 [suggestive; value is input].
- 6.6 The dynamical gate: the substrate rule must be a bit-conserving
  discrete CA — the continuous 2/3 rule has no finite closure (1/3
  obstruction). Candidate: a sigma-delta / error-feedback node (exact
  conservation; fractions statistical).

*Sources:* [countability-from-information.md](countability-from-information.md)
§3,§5,§7,§8; [energy-and-coherence.md](energy-and-coherence.md) §5,§6,§8;
[../../../qa/Q140-light-quantization-from-recirculation.md](../../../qa/Q140-light-quantization-from-recirculation.md) §5,§7.
*Claim discipline:* everything here is conjecture/interpretive/input —
grade each line; never present the shared root as established.

---

## Ch. 7 — The honest ledger  [scope]

*Role:* the full accounting — done, imported, out of scope, open.

- 7.1 The "what each phenomenon is" table (README), in full, with status.
- 7.2 Derived: info → light; P1, P2, P4; ℏ a unit; P3 reduced to one hinge.
- 7.3 Imported / conjectured: the A5 reading; α's value; the shared root.
- 7.4 Out of scope: full QM (complex amplitudes, interference, Born rule)
  — that is all of quantum foundations, not "why light is quantized."
- 7.5 Open computational probes: the bit-conserving sigma-delta rule
  (grounds the energy route); loop-closure / emergent-photon (quantum
  spin ice) sectors (needs quantum dynamics).
- 7.6 Place in GRID: the promotion ladder (substrate → light → mass →
  charge); gravity shares A5.

*Sources:* README §"What this project does NOT show",
[energy-and-coherence.md](energy-and-coherence.md) §8,
[countability-from-information.md](countability-from-information.md) §8,
[../../grid-duality/grid-quantizing.md](../../grid-duality/grid-quantizing.md).
*Claim discipline:* this chapter *is* the honesty layer — under-claim
before over-claim.
