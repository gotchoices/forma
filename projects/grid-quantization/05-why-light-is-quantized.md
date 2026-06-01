# Ch. 5 — Why light is quantized: periodicity, not discreteness

**Status:** Draft (prose, first pass). Part of the [presentation arc](README.md#presentation-arc).
**Grade:** [reduced] — standard math (U(1) ↔ ℤ, Fourier series) shown to rest on one GRID ingredient. The integer label rests on chapter 6's import; the grade is final only once that import is settled.
**Role:** the core. State what light-quantization *is* in the model — the mechanism that makes integer photon counts a fact about a periodic phase, not about discrete values.

## 5.0 The bounded-substrate thought experiment

The keystone of this chapter is best approached not from mathematics but
from the substrate itself. Imagine the lattice at its smallest scale:
time advances in clock ticks of length τ, and each cell stores one of a
small finite set of values. Two cases to keep in mind throughout:

- **Base 2** (binary): each cell is either −1 or +1.
- **Base n** (general bounded): each cell takes one of n equally-spaced
  values centred on zero, for example {−2, −1, 0, +1, +2} for n = 5.

The clock and the bounded dial together set a **maximum frequency**: a
cell can change at most once per tick — you cannot change faster than
your own clock — so the fastest possible oscillation has period 2τ.
This is the substrate's Nyquist limit; call it ω_max.

**The fastest photon.** A wave at ω_max is forced to alternate between
two values, one per tick. The natural choice — the one that puts
maximum energy into the wave — is to use the **extreme** values of the
dial: +A and −A, where A is the largest value available (A = 1 in base
2, A = (n−1)/2 in base n). Intermediate values like 0 in base 3 or
±1 in base 5 cannot enter at this frequency: there is no tick to spare
for them. **At ω_max, every bounded substrate behaves the same — like
a binary substrate operating on its outer values.** The intermediate
values are reserved for lower frequencies. The substrate's tightest
possible wave packet is one cycle at ω_max: two transitions of size 2A,
each costing some quantum of work. Call its total energy **E_max**.

**Half-frequency.** Now stretch the pattern in time: hold each value
for two ticks instead of one, giving …, −A, −A, +A, +A, …, with period
4τ. This is a wave at frequency ω_max / 2. The cycle still has two
transitions of size 2A — **the same E_max per cycle as before** — but
each cycle takes twice as long, so the power is **half**.

This is the central observation. In base 2 there is no other choice:
with only two values on the dial, the stretched square is the only
half-frequency option. **In base 3 the substrate gains a second
option** — the smoother staircase −1, 0, +1, 0, −1, …, taking the
same 4τ per cycle but with four small transitions instead of two
large ones. The shape differs; the scaling does not. Either pattern
still cuts the power by half when frequency is cut by half. The
intermediate value provides a *different shape* at lower frequency,
not a *different scaling*.

The pattern generalises directly. At ω_max / k, the stretched square
(using only the extremes) carries two transitions of size 2A per cycle
in period 2kτ, with power = E_max / (2kτ) ∝ ω. Smoother patterns
available in higher bases trade fewer large transitions for more small
ones; the precise per-cycle figure changes, but the power-vs-frequency
slope does not. **Lower frequency means proportionally fewer
transitions per unit time, which means proportionally lower power.
Power is proportional to ω.**

**Generalisation to any bounded base.** The argument turns on a single
feature: the substrate has **no amplitude knob**. Finitely many
discrete values on a fixed dial, nothing in between. Any finite n ≥ 2
has this property. A continuous-amplitude substrate would break the
argument — with a continuous amplitude knob, a low-frequency wave
could carry as much energy as a high-frequency one by simply being
*bigger*. The "no amplitude knob" property is what forces lower
frequency to mean lower power, and it requires *bounded*, not
specifically binary. The proportionality constant in "power = (const)
× ω" depends on n; the proportionality itself does not.

**ℏ falls out, in natural units.** The substrate's smallest action —
its smallest energy step times its smallest time step — is dW · τ. In
substrate-natural units (dW = τ = 1) this is **ℏ = 1**. The familiar
value 1.054 × 10⁻³⁴ J·s in SI is the conversion factor between
substrate units and lab units, not a prediction (chapter 4). What the
thought experiment *does* fix is the *structure*: ℏ is
energy-grain × time-grain.

**The stop point.** This delivers Planck's *scaling* — power ∝ ω,
equivalently *one cycle of squiggle at frequency ω carries an action
of order h*, derived from the substrate's grain bounds alone, without
invoking periodicity or any quantum-mechanical machinery. It does
**not** deliver the per-mode integer ladder: the further fact that a
mode at frequency ω carries exactly 0, 1, 2, … photons of ℏω each,
regardless of how the wave packet is shaped. That is a *per-mode*
statement, not a *per-cycle* one, and the bounded substrate alone
does not know what a "mode" is or that packets of any shape should
carry the same total energy. The rest of the chapter builds the
structure that closes that gap — and it is honest about the fact that
it has to *import* one piece (a complex amplitude on a compact phase)
from chapter 6 to do so.

What this chapter therefore delivers is a **reduction**, not a
from-scratch derivation: GRID's bounded substrate gives the Planck
*scaling* automatically; one well-localised import promotes that
scaling into the per-mode integer ladder. The bounded substrate is the
real GRID work here; the math that follows is the *structure of the
import's consequence*, not the substance of the derivation.

## 5.1 What is being explained — P3 and P4

Light is observed to come in integer numbers of quanta: a mode can hold
0, 1, 2, … photons, never 1.7. Each photon at frequency ω carries
energy ℏω, and the photons of a given mode are all identical, with the
same ℏω step from one rung of the ladder to the next.

P1 (which frequencies exist) and P2 (each mode is a classical harmonic
oscillator) were settled in Chapter 3. What remains is **P3** (the
integer ladder) and **P4** (the uniform ℏω step). This chapter handles
them together, because they collapse onto a single mechanism.

## 5.2 Periodicity ⇒ a discrete (integer) spectrum

Take a mode and look at it through its **phase**. A propagating sinusoid
e^{−iωt} has a temporal phase φ = ωt — an angle that advances steadily
with time. As time goes on the phase winds around the unit circle: φ
and φ + 2π denote the *same* point on that circle. The phase is
**compact** — a closed loop of circumference 2π.

Suppose the state of the mode is described by a function ψ(φ) over that
phase circle — a **complex amplitude** that has a value at every point
on the loop. (The role of this object, and what makes it complex rather
than a real probability, are the subject of chapter 6. Granted that it
is what it is, the following is purely mathematics.) For ψ to be
well-defined on the circle it must be **single-valued**: a full turn
through 2π must return ψ to itself, ψ(φ + 2π) = ψ(φ). Equivalently,
ψ may be expanded as a Fourier series

<!-- ψ(φ) = Σ_{n ∈ ℤ} c_n e^{i n φ} -->
$$
\psi(\varphi) \;=\; \sum_{n\in\mathbb{Z}} c_n\, e^{i\,n\,\varphi}
$$

with **integer** n. The integer is forced by the periodicity: a
non-integer exponent would fail to close on itself, so the expansion
drops it. *Periodicity of φ ⇔ integer-indexed spectrum of ψ.* This is
the Fourier-series fact from §5.0, applied to the phase rather than to
time.

## 5.3 That integer *is* the occupation number

The variable conjugate to the phase φ is the **occupation number**
operator N̂ = −i ∂/∂φ. Acting on the basis function e^{i n φ} it
returns the integer n:

> N̂ · e^{i n φ} = n · e^{i n φ}.

So the eigenvalues of N̂ are exactly the integers from §5.2. **The
integer label *n* of the Fourier mode is the number of quanta in the
state.** That is P3: occupation is integer because the phase is
compact, by Fourier-series. And because each unit of n corresponds to
the same step of action ∮ p dφ = h, the energy per quantum is the same
ℏω at every n — that is P4. The two collapse onto one mechanism.

Two clarifications are essential.

**The integer needs the complex ψ.** A *real* probability distribution
P(φ) over the phase circle also has an integer Fourier index, by the
same theorem — but those integers count the *angular harmonics of the
distribution's shape*, not the number of quanta. Without the complex
amplitude ψ, the operator N̂ has no well-defined spectrum on which to
act. So integer occupation does **not** follow from a merely
statistical state; it follows from a *complex amplitude* on a compact
phase. P3 rests on the import that chapter 6 names — that the
substrate's state is such a complex amplitude.

**Distinct from charge.** The same circle → ℤ duality also gives
charge — the integer winding of a *classical* matter phase around a
*spatial* loop ([maxwell.md](../../grid/maxwell.md)). Charge is a
classical topological integer (a homotopy class) needing no quantum
content. Occupation is a *quantum spectral* integer (an eigenvalue of
N̂ on ψ). The mathematics is shared; the physical objects are not.
Spin in Chapter 2 came from the *same* compact circle (the ℵ-line) and
yet again meant a different physical thing. That is GRID's economy —
one circle, several distinct consequences — not a confusion.

## 5.4 Two routes, one hinge

The same mechanism is reached from two different angles in the
project's working notes, and it is worth saying both — and being honest
about what their agreement does and does not buy:

- a **topological** route
  ([work/countability-from-information.md](work/countability-from-information.md))
  takes the duality U(1) ↔ ℤ as the central fact and reads occupation
  as the dual of the compact oscillation phase;
- an **energetic** route
  ([work/energy-and-coherence.md](work/energy-and-coherence.md)) takes
  a bounded, periodic cell and a fixed transition cost and reads
  E ∝ ω — Planck's *scaling* — from a pinned-magnitude argument on the
  substrate's transitions.

The two are **complementary, not independent**. The topological route
supplies the *integer label* — that occupation is integer at all — and
rests on the single-valued complex amplitude over the compact phase.
The energetic route supplies the *ω-scaling* — that energy goes as ω —
and rests on the *same* compact-phase structure plus the substrate's
grain bounds. The same chapter-6 reading underwrites both, so they
agree because they share their hinge; they are not independent
verifications. The agreement is meaningful — it shows the same
mechanism is recognisable from very different starting points — but it
is not corroboration of the kind two genuinely independent arguments
would provide.

## 5.5 Continuous vs finite phase: textbook QED vs a GRID deviation

The chapter has so far said "compact phase" without saying how *finely*
that phase is resolved. The two limits give different physics:

- a **continuous** compact phase — U(1) with infinite-precision values
  — has dual ℤ, the full set of integers. The occupation ladder is
  *unbounded*: a mode can hold arbitrarily many photons. This is
  textbook QED.
- a **finite** dial — ℤ_d of d equally-spaced positions on the circle,
  as A5's finite per-cell information would allow at the substrate
  scale — has dual ℤ_d. The occupation ladder is *bounded* at some
  large but finite d.

The bounded ladder is a GRID-specific deviation from the textbook
story: finite occupation per mode, with a cap set by the substrate's
information budget. The cap is astronomically high for any macroscopic
mode (because many cells participate), so the deviation is well below
any observational reach today, but it is in principle a sharp
signature. Both limits use the *same* compact phase and the *same*
periodicity-⇒-integer mechanism; they differ only in resolution.

## 5.6 Where the energy route stops

The §5.0 thought experiment *is* the energy route, stated in the
substrate's own terms. To recap its honest accounting: a bounded
substrate (any finite n ≥ 2) delivers the **scaling** rigorously —
power ∝ ω, with proportionality set by the substrate's grain bounds.
That much is GRID-derived, without reference to periodicity or quantum
amplitudes.

The step from this scaling to the per-mode quantum E = ℏω — the
integer ladder, every rung the same size — is the **import**.
"Action per cycle = h" (the Bohr–Sommerfeld / single-valuedness
postulate that §5.2 used to get an integer-spectrum N̂) is what
promotes the classical scaling into a quantised step, and it requires
the complex amplitude on the compact phase that chapter 6 supplies.
*Bounding the magnitude buys the scaling; getting the rungs themselves
takes the complex amplitude.*

## 5.7 What light-quantization *is*, in the model

Putting it together honestly: "light is quantized" in this model rests
on **two GRID-derived ingredients and one import**.

- The substrate is **bounded** (a finite dial — Chapter 1), so it has
  no amplitude knob. That alone, by the §5.0 thought experiment,
  delivers **Planck's scaling**: power ∝ ω. Discreteness does this
  work — no periodicity required.
- The substrate has a **compact phase** (the ℵ-line of A3). If the
  state on that phase is a single-valued **complex amplitude**, then
  the Fourier-series fact of §5.2 delivers the **per-mode integer
  ladder**: 0, 1, 2, … photons of ℏω each, every rung the same size.
  Periodicity does this work — discreteness is not required here.

Together these supply P1–P4. **The bounded substrate and the compact
phase are both GRID-derived; the *complex amplitude* on the phase is
the one import**, taken up next.

The full picture is therefore not "periodicity, not discreteness" —
both do work, in different roles. **Discreteness gives the scaling.
Periodicity gives the ladder.** And the project reduces
light-quantization to one precisely-located import: the substrate's
state being a complex amplitude over A3's compact phase. That is what
light-quantization *is*, in the model. The arc continues
([next](README.md#presentation-arc)).

---

## Sources

- [work/countability-from-information.md](work/countability-from-information.md) — U(1)↔ℤ, single-valuedness, the corrected real-vs-complex statement
- [work/energy-and-coherence.md](work/energy-and-coherence.md) §3 (E ∝ ω scaling), §5 (conservation + the dynamical gate), §6 (the topological lock)
- [foundations.md](../../grid/foundations.md) — A3 (the compact phase)

## Claim discipline

[reduced]. The math (U(1) ↔ ℤ, Fourier series; N̂ = −i∂/∂φ spectrum on
a single-valued complex ψ) is standard; the contribution is identifying
*this* mechanism as where GRID's "light is quantized" lives. **Do not
claim** the integer follows from a real / stochastic distribution
alone — it requires the *complex* amplitude, which is chapter 6's
imported piece. **Do not claim** the topological and energetic routes
are *independent* confirmation — they share the single hinge; the
agreement is meaningful but not double-corroboration. The chapter
delivers "what quantisation *is* in the model," not "we derived QM."
