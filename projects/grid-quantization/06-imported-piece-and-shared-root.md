# Ch. 6 — The one imported piece, and the shared root

**Status:** Draft (prose, first pass). Part of the [presentation arc](README.md#presentation-arc).
**Grade:** [conjecture] — every claim below is conjecture, interpretive, or import. Nothing in this chapter is presented as derived. Under-claim before over-claim.
**Role:** state the lone hinge of the arc honestly, and propose the conjectural unification with gravity that would close it.

Chapters 1 through 5 established what GRID derives from its axioms.
This chapter names what it does *not* derive, and identifies the
conjectural payoff the missing import would deliver if it held. Every
claim below is graded explicitly.

## 6.1 The hinge: a complex amplitude on the compact phase

What chapter 5 reduced to a single missing piece — and what this
chapter takes up — is the question of *what the state of a mode is on
the compact phase*. Three candidates are mathematically distinct:

- **A sharp classical value.** A definite point on the phase circle.
  This is the classical oscillator: one position, no Fourier-series
  structure. *Does not deliver the integer ladder.*
- **A real probability distribution.** A density over the phase circle,
  specifying probabilities of finding the phase at each value. This has
  integer Fourier modes, but those integers index the *shape* of the
  distribution, not the *occupation* of the mode. *Does not deliver the
  ladder either.*
- **A single-valued complex amplitude.** A wavefunction ψ(φ) over the
  phase circle. This makes N̂ = −i ∂/∂φ a well-defined operator with
  integer spectrum. *This delivers the ladder.*

(A finer-grained quantum option — a *density matrix / mixed state* —
sits inside the third category as the natural generalisation to
statistically mixed quantum states. The load-bearing distinction here
is *complex amplitude vs real distribution*, so the chapter discusses
"the complex amplitude reading" as the import; the mixed-state
refinement is part of it.)

**The import GRID must make is the third reading.** The state on the
compact phase is a single-valued complex amplitude. This is what makes
the substrate's state *quantum* rather than classical or merely
stochastic. It is the load-bearing piece of the entire arc.

The reading is an *interpretation* of GRID's information axiom A5. A5
says each cell carries a finite quantity of information — ζ = ¼ bit per
cell. *How* that information is encoded as a state on the phase circle
admits the three readings above. The third is the one GRID's
quantization story requires — but stating it requires unpacking what
the per-cell information actually has to support. A5 allocates
information **per cell, in space**; the import places a complex
amplitude on the **per-mode oscillation phase, in time** (chapter 5
§5.2's φ). A mode spans many cells, and aggregating ζ bits across
those cells into a single per-mode ψ(φ) is itself part of what the
import has to perform: the chapter's import is not just *"informational
state = amplitude"* but more fully *"per-cell spatial information,
aggregated across a mode, encoded as a single complex amplitude on the
per-mode temporal phase circle."* That extra clause is honest about
how much the import has to do.

## 6.2 Grade: [interpretive], not [derived]

This reading of A5 is graded **[interpretive]** for a specific reason:
it is a choice among three mathematically distinct objects (sharp
value, real distribution, complex amplitude), and GRID's axioms do not
— on their own — single out the third. A real distribution is just as
compatible with "ζ bits of information per cell" as a complex amplitude
is. The third reading is *natural* — quantum information theory
routinely models information-bearing states as Hilbert-space vectors —
but naturalness is not derivation.

So the grade is honest: this is one interpretive reading of A5 among
the available ones, load-bearing for the arc, and it deserves the
*interpretive* tag rather than the *derived* one. If a future step in
the project succeeds in *proving* this reading from prior structure
rather than positing it, that proof is the work that would upgrade
chapter 6 from a conjecture into a derivation.

## 6.3 Why merely stochastic does not suffice

Chapter 5 §5.3 settled this in its own context; the conclusion bears
restating here because it is what *makes* the complex-amplitude reading
the load-bearing one rather than the cheaper real-distribution reading.

A real probability distribution P(φ) over the phase circle has an
integer Fourier index, by the same Fourier-series fact §5.2 used. But
those integers count the *angular harmonics of the distribution's
shape*, not the *occupation of a mode*. The conjugate operator
N̂ = −i ∂/∂φ has, mathematically, the same all-of-ℤ spectrum acting
on any L² function on the circle — distributions included. The
relevant distinction is *physical*: the spectrum corresponds to
**occupation as a measurement-eigenvalue observable** only when the
state is a quantum amplitude; for a classical distribution, the integer
Fourier index just labels the harmonics of the distribution's shape and
carries no measurement-eigenvalue interpretation. So the "integer
Fourier index of P(φ)" and the "integer spectrum of N̂ on ψ(φ)" are
different *physical* facts about different objects, and only the second
is the occupation ladder.

The consequence: GRID needs the complex amplitude *specifically*.
Reading A5 as merely supplying a stochastic / informational distribution
would leave countability — and hence the per-mode integer ladder —
underived. The import has to be the genuinely quantum reading.

## 6.4 The shared-root conjecture — and why it is *harder* than it looks

Here is the chapter's most ambitious claim, and its most carefully
graded one:

**A5 is the same axiom that GRID uses for gravity**
([gravity.md](../../grid/gravity.md)). In the gravity derivation, A5
supplies the horizon entropy density: the entropy on a causal horizon
of area A is ζ · A, and this entropy density is what Jacobson's
thermodynamic argument feeds into Einstein's equations to recover the
gravitational coupling G = 1 / (4ζ). The chain is *A5 ⇒ horizon
entropy ⇒ Jacobson ⇒ Einstein's equations*.

The chain GRID would use for *quantization*, on this chapter's
reading, is *A5 ⇒ complex amplitude on the compact phase ⇒
Fourier-series ⇒ integer ladder*.

Both chains start at A5. *If* the two uses of A5 — the horizon entropy
density for gravity, and the complex amplitude on a temporal phase for
quantization — turn out to be the *same* reading of A5, then finite
information would be a single root underwriting *both* gravity and
quantum discreteness. That would be a striking unification, and it is
the conjecture this chapter names.

A word on the word "root." Even granting the unification, A5 is then a
shared *input* to two different machineries: Jacobson's thermodynamic
construction for gravity, and the Fourier U(1) ↔ ℤ structure for
quantization. Calling it the *root* of both treats it as a generating
principle, when it is more accurately the *supplier of a quantitative
ingredient* (entropy density on one side, amplitude / distribution
interpretation on the other) that two distinct machineries turn into
their respective results. The stronger reading — "shared root" —
should be heard with that qualifier; the weaker but more accurate
reading is "shared input."

**But the two uses look different on inspection**, and this difference
must be flagged honestly:

- **Gravity uses A5 statistically.** The horizon entropy ζ · A counts
  microstates on a spatial 2-surface. The mathematics is real-valued,
  statistical, and lives on a horizon in space.
- **Quantization uses A5 quantum-mechanically.** The complex amplitude
  ψ(φ) carries the information ζ allocates as a Hilbert-space state.
  The mathematics is complex-valued, quantum, and lives on a temporal
  compact phase.

Bridging these — showing that *the same reading* of A5 generates both
the spatial statistical entropy of gravity *and* the temporal complex
amplitude of quantization — is the **open task**. The two readings
might be unified by a deeper principle yet to be articulated (one
finite-information axiom expressed both ways), or they might prove
genuinely distinct, in which case the "shared root" claim collapses to
the weaker "A5 is *used* in both places, by separate readings." The
chapter does not adjudicate; it names the gap and grades it
**[conjecture]**.

It is worth being explicit about which way the inspection currently
leans: gravity reads A5 as a *real, statistical, spatial* quantity;
quantization needs A5 to give a *complex, quantum, temporal* quantity.
These are different in object type (real vs complex), interpretation
(statistical vs quantum), and locus (spatial 2-surface vs temporal
circle). The conjecture asks for a principle that unifies all three
differences in one stroke. That is a *lot* of unification, and the
chapter is honest that this is therefore a substantial and unproven
ambition.

## 6.5 GRID-specific signatures

Granted the complex-amplitude reading of §6.1, GRID makes two specific
predictions that distinguish it from textbook QED, plus one suggestive
numerical observation that is *not* a prediction.

**The integer ladder per mode [predicted, given the import].** Given
§6.1, the ladder is integer and uniform — P3 and P4. This is the
chapter-5 keystone result. It is predicted by the arc as a whole,
*given* this chapter's import.

**The bounded occupation ladder [predicted].** A5's per-cell
information is *finite*, so the effective dial of §5.5 has finite size
d (depending on how many cells contribute to a mode), and the dual
ℤ_d is also finite. A mode's occupation ladder is therefore *bounded*
at some integer cap, not unbounded as in textbook QED. The cap is
astronomical for any macroscopic mode (it scales with the cell count
the mode spans), so the deviation is unobservable in any conceivable
experiment today — but it is, in principle, a sharp distinguishing
prediction. Textbook QED says any mode can hold arbitrarily many
photons; GRID says there is a hard cap.

**The α-scale leakage coupling [suggestive, but α is input].** The
single-hexagon energy-return fraction (2/3)¹² = 1/129.75 sits inside
α's running range (1/137 at low energy, 1/128 at the Z mass).
[Q140 §5](../../qa/Q140-light-quantization-from-recirculation.md) has
the bookkeeping and its caveats (exponent ambiguity, coherent vs
incoherent summation, bare vs running). One further caveat is added by
[work/loop-recirculation-attempt.md](work/loop-recirculation-attempt.md)
§5 from `run_recirculation.py --test circ`: the (2/3)¹² figure is a
property of a *forced single pulse around an isolated loop*, whereas a
clean propagating wave's net induced circulation **cancels** (the
zigzag-cancellation finding). So the number is a property of a forced,
artificial setup, not of what a free photon actually does — which makes
the *[suggestive]* tag honest about the right object. This number is
*not* a prediction of α — α is an A6 input — but it is a suggestive
numerical observation consistent with the broad picture that α at the
substrate scale relates to a loop-leakage coupling. Marked
**[suggestive, not predicted]**.

## 6.6 The dynamical gate

A second strand of conjecture concerns the *dynamics* the substrate
must support to make the bounded-substrate story of chapter 5
self-consistent.

A preliminary note on which substrate this discussion presupposes.
Chapter 1 §1.2 introduced the per-edge state as a *continuous* compact
phase θ ∈ S¹. Chapter 5 §5.0 (and the energy-and-coherence working
notes) use a *finite-alphabet* reading at the substrate scale, derived
from A5. The 1/3 obstruction below requires the finite-alphabet
reading: the obstruction *is* the assertion that a literal continuous
rule cannot preserve a finite alphabet. So §6.6's conjecture is honest
about which substrate model it concerns, and the model it concerns is
the A5-finite-alphabet reading, not chapter 1's continuous phase. The
substrate-model layering is itself an open question the project must
eventually settle.

The continuous junction rule of chapter 1, `out = (2/3)·total −
incoming`, has a factor of 1/3 in it. That factor takes a discrete
starting state off any finite alphabet: if cells start at integer
values, one tick later they sit on multiples of 1/3, the next tick on
multiples of 1/9, and so on (the *1/3 obstruction*). So a strictly
*bounded* substrate — the substrate the §5.0 thought experiment leans
on — cannot at the cell level run the literal continuous rule. It
must run a discrete *bit-conserving* rule whose coarse-graining
reproduces the continuous one on average.

The candidate sketched in
[work/energy-and-coherence.md](work/energy-and-coherence.md) §8 is a
**sigma-delta node**: the junction computes the exact fractional scatter
result, sends out only the integer part on each edge, and *carries the
remainder forward in a small bounded accumulator at the node*. Total
bit count is conserved exactly; the fractional 1/3 is tracked rather
than discarded; and the long-time average reproduces the continuous
rule. The construction is well-known in signal processing — sigma-delta
modulators in audio DACs do exactly this — and it is a plausible
candidate for what a bit-conserving GRID rule could look like.

This candidate is **graded [conjecture]** for two reasons. First, it is
unbuilt: no GRID simulation has been written that runs it. Second, even
granting the construction, the node carries a small bounded *memory*
(the accumulator), introducing structure at the junction that the
chapter-1 substrate did not explicitly include. How that fits A5's
per-cell information budget is itself part of what an explicit
construction would have to settle. The construction is honest about
these openings; it is not a solved problem, it is a candidate.

## 6.7 What the chapter claims, in one paragraph

The role of this chapter is to *name* what is left open and to grade
it. Summarising:

- **[interpretive] import**: the substrate's state on the compact phase
  is a single-valued *complex* amplitude (not classical, not merely
  stochastic). Load-bearing for the arc; deserves the interpretive tag.
- **[conjecture]**: that A5's two uses — statistical horizon entropy
  for gravity, complex amplitude for quantization — are the *same*
  reading. Unproven; bridging real-statistical-spatial to
  complex-quantum-temporal is the open task.
- **[predicted]**: the per-mode integer ladder (given the import), and
  the bounded ladder (given finite information).
- **[suggestive]**: the α-scale leakage coupling, *not* a prediction of α.
- **[conjecture]**: a sigma-delta-style bit-conserving substrate rule,
  unbuilt.

The honest summary: GRID **reduces** light-quantization to one
well-localised import (a complex amplitude over A3's compact phase),
and *gestures at* — but does not prove — that this import is the
*same* finite-information principle GRID uses for gravity. That is the
chapter's claim, fully graded. The arc continues
([next](README.md#presentation-arc)).

---

## Sources

- [work/countability-from-information.md](work/countability-from-information.md) §3, §5, §7, §8 — the import; the bounded-ladder prediction; the open A5-reading task
- [work/energy-and-coherence.md](work/energy-and-coherence.md) §5, §6, §8 — the dynamical gate; the sigma-delta candidate; the open construction
- [Q140](../../qa/Q140-light-quantization-from-recirculation.md) §5, §7 — the α-scale leakage bookkeeping with full caveats
- [foundations.md](../../grid/foundations.md) — A5 (finite information per cell; the source for both gravity and quantization)
- [gravity.md](../../grid/gravity.md) — Jacobson's entropy → Einstein's equations derivation, given A5

## Claim discipline

[conjecture] throughout. Every claim is graded; nothing here is presented
as derived. The shared root with gravity is named as a conjectural
unification and explicitly distinguished from the weaker fact that A5
is *used* in both places. The bounded occupation ladder is a prediction
*given* the import; the α-scale leakage is **suggestive, not predicted**
(α is an A6 input). The sigma-delta dynamical candidate is unbuilt.
Under-claim before over-claim.
