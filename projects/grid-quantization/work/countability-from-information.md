# Countability (P3) from finite information — a derivation sketch

The one genuinely-imported piece of light-quantization
(work/tier2-design.md §4b) is **P3: that occupation is countable**
(integer number of quanta in a mode, rather than a continuous
amplitude). This document argues P3 follows from GRID's existing
axioms — **A3** (compact U(1) phase) plus **A5** (the substrate is
informational / finite-bit) — via one rigorous mathematical fact,
with the scale ℏ remaining a unit. It is a sketch: each step is
graded **[rigorous] / [interpretive] / [predicted]** so the load-
bearing assumption is visible.

This is foundational reasoning, not a simulation — the central fact
is a theorem (the dual of a circle is the integers), not something to
measure.

---

## 0. The earlier mistake this corrects

In §4a I objected: "winding quantizes **charge** (spatial vortices),
not photon number, so the loop story conflates them." That was half
right. There are **two different compact phases**, and the same
duality applies to each:

| compact phase (a circle) | its integer dual | physical meaning |
|---|---|---|
| matter phase θ wound around **space** | winding number | **charge** (maxwell.md) |
| a field mode's **oscillation phase** φ = ωt | occupation number | **photon number** |

These share one piece of *mathematics* — single-valuedness on a
compact U(1) forces an integer — but they are **not the same physical
fact**, and the difference is load-bearing (§3). Charge is a
**classical topological** winding of a classical field around a
*spatial* loop: an integer with no quantum content (a homotopy class,
maxwell.md). Occupation is a **quantum spectral** integer — the
eigenvalue of N̂ on a single-valued *complex amplitude* over the *time*
phase. Same circle→ℤ duality, different objects (classical homotopy vs
quantum spectrum). My earlier objection was right that they are
different; it was wrong only in concluding the oscillation-phase route
is closed off. (Conflating the two is what misled the first draft of
§3 below.)

---

## 1. The rigorous fact: dual of U(1) is ℤ  [rigorous]

The Pontryagin dual of the circle group U(1) = ℝ/2πℤ is the integers
ℤ. Concretely: any (square-integrable) function on a circle expands
in characters

<!-- f(φ) = Σ_{n∈ℤ} c_n e^{inφ} -->
$$
f(\varphi) \;=\; \sum_{n\in\mathbb{Z}} c_n\, e^{i n \varphi}
$$

with **integer** n, because e^{inφ} is single-valued on the circle
(f(φ+2π)=f(φ)) **iff** n ∈ ℤ. The operator conjugate to the angle,
N̂ = −i ∂/∂φ, has eigenfunctions e^{inφ} and therefore **integer
spectrum**. Countability of N̂ *is* the single-valuedness of a
function on a compact phase. No dynamics, no extra postulate.

(Known subtlety: the number–phase operator pair has technical
delicacies — the phase operator is not quite self-adjoint
[Carruthers–Nieto, Susskind–Glogower]. The robust part, which is all
we use, is that the spectrum forced by single-valuedness on the
compact angle is the integers.)

---

## 2. Why classical GRID does NOT trigger it  [rigorous]

A *classical* oscillator has a **definite** phase — a single point
φ₀ on the circle, not a function over it. A point has no Fourier
index; nothing is quantized. This is exactly why the classical
linear lattice (A1–A4) gives modes but not quanta (§4a), and why
"every classical oscillator would be quantized" is *not* a
consequence: §1 needs the state to be a *function/distribution over*
the phase circle, not a value of it.

So the trigger for P3 is precisely the step from "a definite phase"
to "an amplitude/distribution over phase." That step is what A5
supplies.

---

## 3. A5 supplies the missing structure  [interpretive]

A5 says the substrate is **informational**: a cell carries ζ = ¼ bit;
the state is specified by *information*, i.e. a distribution over
configurations, not a single sharp configuration. Read literally,
the state of a mode is therefore a **distribution (or amplitude)
over its compact phase φ** — exactly the object §1 needs.

Apply §1: a distribution over the compact φ has integer-indexed
Fourier content, and the conjugate quantity (the mode's
action/number) is integer-valued. **That integer is the occupation
number. P3 follows.**

This is the one interpretive step: treating A5's informational state
as "amplitude/distribution over the compact phase." It is natural
(A5 is an information axiom; information *is* distributions over
states) but it is an interpretation of A5, not a line of algebra —
hence graded [interpretive]. It is also the same move metric-mass
ch. 9 calls "promoting amplitudes to operators"; here A5 is what
licenses the promotion rather than it being imposed by fiat.

**Quantum vs merely stochastic — corrected.** An earlier draft claimed
a *real* probability distribution over φ suffices for countability.
That is **wrong** (and contradicts §8). A real P(φ) does have an
integer Fourier index, but those integers index the *angular shape of
the distribution*, not the occupation ladder. Occupation is the
spectrum of N̂ = −i∂/∂φ acting on the **complex amplitude** ψ(φ), and
that spectrum is integer **only because ψ is single-valued and
complex**; a real P carries no such ψ, and its conjugate action stays
**continuous**. So **integer occupation requires the complex amplitude
— the quantum structure itself.** Countability is therefore *not* a
cheaper, stochastic-only claim separable from QM: the single-valued
complex amplitude *is* the imported piece. (Interference and the Born
rule may be further still, but the complex amplitude is already
required for P3 — so "countability without the rest of QM" overstates;
the quantum *state* is already in.)

---

## 4. The scale stays a unit  [rigorous, by §4b]

§1 fixes that the action comes in **integer** steps; it does not fix
the **size** of a step. One unit of N̂ corresponds to one quantum of
action ∮ p dφ = h — and the value of h is the area of one phase-space
cell, a unit (like c), not a prediction (work/tier2-design.md §4b).
So: integer-ness from compactness (A3+A5), step-size ℏ as the unit.

---

## 5. Lattice-concrete version + a prediction  [predicted]

A5's per-cell budget is finite (ζ = ¼ bit *externally*; cells may
carry more internal sub-state, INBOX "sub-state resolution"). A mode
spanning N cells carries ~Nζ bits, so its phase circle is resolved
into ~2^{Nζ} distinguishable values. By §1 the occupation index n
then ranges over a **bounded** set of size ~2^{Nζ}, not all of ℤ.

**Prediction:** GRID gives each mode a *finite* occupation ladder
(a maximum photon number per mode ~2^{Nζ}), whereas standard QFT's
ladder is unbounded. For any macroscopic mode N is astronomical, so
the cutoff is unobservably high — but it is a definite, in-principle
GRID deviation from QFT, and it is *why* the ladder looks infinite
without being so. (This is the qudit-vs-oscillator distinction:
finite information ⇒ finite-dimensional per-mode Hilbert space.)

---

## 6. The payoff: one root for gravity and quantization

A5 is not invented for this. It is the **holographic/Bekenstein
information bound**, and gravity.md already derives Newton's G from
it (entropy density → Jacobson → Einstein equations). The present
sketch says the **same** axiom — finite information, the substrate
being informational rather than sharply classical — is what makes
occupation countable. So:

> A5 (finite information) ⇒ **gravity** (via entropy/Jacobson) **and**
> ⇒ **quantization** (via amplitude-over-compact-phase + U(1)↔ℤ).

If this holds up, gravity and quantum discreteness share a single
root in GRID — the lattice's finiteness of information — which is a
much stronger and more economical claim than deriving either alone.

---

## 7. Honest status

| Step | Grade |
|---|---|
| Dual of U(1) is ℤ ⇒ integer conjugate to a compact phase | **rigorous** |
| Occupation = integer spectrum of N̂ on a single-valued **complex amplitude** over the oscillation phase (a *quantum* fact; *distinct* from charge's classical winding) | **rigorous** |
| Classical (definite phase) does not trigger it | **rigorous** |
| A5's informational state = a single-valued **complex amplitude** over the compact phase | **interpretive** (the one load-bearing assumption) |
| ⇒ occupation countable (P3) | follows — but only *given the complex amplitude* |
| a *real* distribution alone gives countability | **FALSE** (corrected §3) — its integer index is the distribution's shape, not occupation |
| ℏ is the unit, not derived | rigorous (§4b) |
| Finite info ⇒ bounded occupation ladder per mode | **predicted** (testable in principle) |
| Interference / Born rule (beyond the complex amplitude) | **NOT established** |

**Bottom line.** P3 is reduced to one interpretive reading of A5 — that
the substrate's state is a single-valued **complex amplitude** over the
compact phase — after which integer occupation is forced by the
dual-of-a-circle theorem. The import is therefore **the quantum state
itself** (the complex amplitude), *not* a cheaper stochastic
distribution: "countability without the rest of QM" overstates, since
the complex amplitude is already the quantum structure. Combined with
the already-derived pieces (P1, P2, P4 + scale-invariant universality,
α, spin, bound modes), the genuinely-open question is whether A5
supplies that *complex-amplitude* structure. The "same reading as
gravity" claim is now **harder, not easier**: gravity reads A5 as a
*real/statistical* entropy count (configuration counting on a spatial
horizon), whereas P3 needs a *complex amplitude* over a temporal phase
— so the two readings are, if anything, further apart, and showing them
the same is the open task (§8). The scale ℏ is, and should be, a unit.

---

## 8. What would harden this

- **Pin the A5 reading.** Is "informational state = distribution over
  compact phase" derivable from how A5 is used in gravity.md (the
  entropy counting), so the two uses of A5 are demonstrably the same
  reading? If yes, the [interpretive] step upgrades toward [rigorous].
- **Stochastic vs quantum — now resolved (§3).** Integer occupation
  requires a single-valued *complex* amplitude; a real distribution
  does **not** suffice. So the open question is not "real or complex?"
  but the sharper one: **can A5 supply a complex amplitude at all?** A5
  as used for gravity is a real/statistical entropy count — so this is
  the same gap as "pin the A5 reading," now seen to require bridging
  *real-statistical* (gravity) to *complex-amplitude* (quantization).
- **The bounded-ladder prediction.** Work out ~2^{Nζ} for a concrete
  mode and confirm the cutoff is unobservably high (consistency), and
  whether any regime (very small N, near the Planck scale) could make
  it matter.
