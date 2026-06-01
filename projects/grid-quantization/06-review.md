# Review: Ch. 6 — The one imported piece, and the shared root

Checked against
[work/countability-from-information.md](work/countability-from-information.md),
[work/energy-and-coherence.md](work/energy-and-coherence.md),
[foundations.md](../../grid/foundations.md) (A5),
[gravity.md](../../grid/gravity.md), and chs. 1, 5.

This is the most carefully graded chapter in the arc. The
three-readings setup in §6.1, the explicit [interpretive] label in
§6.2, the §6.3 restatement of complex-vs-stochastic, and the §6.4
honest list of *real-statistical-spatial* vs
*complex-quantum-temporal* differences in the two A5 uses are all good
work. The five tags in §6.7 — [interpretive], [conjecture],
[predicted given import], [suggestive not predicted], [conjecture] —
are accurately assigned. Items below are residual gaps, not structural
failures.

## Material omissions

**1. The intra-quantization bridge from A5 (per-cell, spatial) to ψ(φ)
(per-mode, temporal) is not described.** A5 allocates **ζ bits per
spatial cell**. The chapter's import — "ψ(φ) carries the information ζ
allocates as a Hilbert-space state" (§6.1) — places the complex
amplitude on a **per-mode temporal** phase circle (φ = ωt of ch. 5
§5.2). Per-cell spatial bits → per-mode temporal amplitude is itself a
non-trivial bridge: a mode spans many cells, and aggregating ζ bits
across those cells into a single per-mode ψ(φ) is *exactly* the step
the import has to perform. §6.4 honestly lists "spatial vs temporal"
as a difference between gravity-A5 and quantization-A5, but the
*quantization-A5* use itself crosses that divide internally — and the
chapter elides it. The "import" is doing more work than the chapter
admits: not just *"informational state = amplitude"* but also
*"per-cell spatial information encoded as a complex amplitude on a
per-mode temporal phase circle."*

**2. Inherits the unresolved state-model conflation from chs. 1 and 5.**
§6.6 motivates the sigma-delta candidate by *"if cells start at
integer values, one tick later they sit on multiples of 1/3"* — i.e.
the 1/3 obstruction *assumes* the cell state is on a finite alphabet.
Ch. 1 §1.2 introduced the per-edge state as a **continuous** compact
phase θ ∈ S¹, not a finite alphabet. The finite-alphabet reading is
energy-and-coherence's, and ch. 5 §5.0 used it too without flagging
the substitution ([05-review.md §9](05-review.md), [01-review.md
§5–6](01-review.md)). §6.6's motivation only holds in the
finite-alphabet reading, which has not been canonically adopted. The
chapter needs the project to settle which substrate it is *actually*
running on; either is defensible, but they are not the same model.

## Imprecisions

**3. §6.3 "N̂ = −i ∂/∂φ has no well-defined spectrum on a classical
probability distribution."** Strictly false. The operator
−i ∂/∂φ has the same mathematical spectrum (all of ℤ) acting on any
L² function on the circle — distributions included. The correct
distinction is that the spectrum corresponds to **occupation** as a
physical observable only when the state is a quantum amplitude; for a
classical distribution, the integer Fourier index just labels the
harmonics of the distribution's shape and carries no
measurement-eigenvalue interpretation. The next sentence — *"the
integer Fourier index of P(φ) and the integer spectrum of N̂ on ψ(φ)
are different mathematical facts about different objects"* — is right;
the lead sentence is over-strong and could be softened to "no
*physical* spectrum" or "no spectrum that corresponds to occupation."

**4. §6.5's "α-scale leakage" is more hedged in the loop-recirculation
work than the citation suggests.** The Q140 §5 cite carries the
exponent/running caveats, but
[work/loop-recirculation-attempt.md](work/loop-recirculation-attempt.md)
§5 adds a sharper one inherited from `run_recirculation.py --test
circ`: (2/3)¹² is a *forced single-pulse around an isolated loop*,
whereas a clean propagating wave's net induced circulation **cancels**
(the zigzag-cancellation finding) — so the number is a property of a
forced, artificial setup, not of what a free photon actually does.
Adding the loop-recirculation-attempt aside as a second citation would
make the "[suggestive]" tag honest about the right object.

**5. §6.4's "shared root" framing may overstate even granting the
unification.** Even if A5's two readings turn out the same, A5 is then
a *shared input* to two different mechanisms (Jacobson thermodynamics
for gravity, Fourier U(1)↔ℤ for quantization). Calling it the
**root** of both treats it as a generating principle, when it is
really the supplier of a quantitative ingredient (entropy density;
amplitude/distribution interpretation) that two separate machineries
turn into their respective results. The chapter does hedge with the
fallback ("A5 is *used* in both places, by separate readings"), but
the strong-claim framing still leans on "root" doing more work than
"shared input."

## Smaller note

**6. §6.1's three readings (sharp value / real distribution / complex
amplitude) omit a fourth obvious one: a density matrix / mixed quantum
state.** Probably not load-bearing for the chapter's argument (the
complex-vs-stochastic distinction is the load-bearing axis), but a
careful reader will notice the gap. One clause acknowledging it as a
finer-grained option within the quantum reading would close it.

---

## Author response

Integrated all six items.

- **Item 1 (per-cell spatial → per-mode temporal bridge).** Genuine
  omission, fixed. §6.1 now ends with an explicit paragraph naming
  the bridge: the import is not just "informational state = amplitude"
  but more fully "per-cell spatial information, aggregated across a
  mode, encoded as a single complex amplitude on the per-mode temporal
  phase circle." Honest about how much the import actually carries.
- **Item 2 (state-model conflation).** Accepted. §6.6 now opens with
  a preliminary note explicitly flagging that the 1/3-obstruction
  motivation presupposes the A5-finite-alphabet reading (not chapter
  1's continuous compact phase), and that the substrate-model layering
  is itself an open question.
- **Item 3 ("no well-defined spectrum" too strong).** Accepted. §6.3
  rephrased: the operator −i∂/∂φ has the same mathematical all-of-ℤ
  spectrum on L² functions of either kind; the distinction is
  *physical* — only on a quantum amplitude does the spectrum
  correspond to occupation as a measurement-eigenvalue observable.
- **Item 4 (α-scale zigzag-cancellation caveat).** Accepted and
  added. §6.5 now cites loop-recirculation-attempt.md §5 alongside
  Q140 §5 and names the zigzag-cancellation finding explicitly:
  (2/3)¹² is a property of a forced single pulse around an isolated
  loop, not of what a free propagating photon actually does. Makes
  the *[suggestive]* tag honest about the right object.
- **Item 5 ("shared root" overstates).** Accepted. §6.4 now includes
  an explicit "a word on the word 'root'" paragraph: even granting
  unification, A5 is a *shared input* to two different machineries
  (Jacobson for gravity; Fourier U(1)↔ℤ for quantization). The strong
  "root" reading is named, and the more accurate weaker reading
  "shared input" is given as the qualifier.
- **Item 6 (density matrix as fourth reading).** Accepted as a brief
  acknowledgement. §6.1 now has a parenthetical noting that the
  density matrix / mixed state is the natural finer-grained
  generalisation within the complex-amplitude category; the
  load-bearing distinction remains *complex vs real distribution*.
