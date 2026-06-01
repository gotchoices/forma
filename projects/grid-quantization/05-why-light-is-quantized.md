# Ch. 5 — Why light is quantized: periodicity, not discreteness

**Status:** Draft (prose, first pass). Part of the [presentation arc](README.md#presentation-arc).
**Grade:** [reduced] — standard math (U(1) ↔ ℤ, Fourier series) shown to rest on one GRID ingredient. The integer label rests on chapter 6's import; the grade is final only once that import is settled.
**Role:** the core. State what light-quantization *is* in the model — the mechanism that makes integer photon counts a fact about a periodic phase, not about discrete values.

## 5.0 A signals warm-up, before any math

A signal that is **periodic** in time has, in its frequency content, a
**line spectrum**: it carries energy only at integer multiples of one
fundamental frequency f₀ = 1/T. A sine wave at f₀ is a single line; a
square wave is f₀, 3f₀, 5f₀, …; a more complicated periodic shape adds
lines at 2f₀, 4f₀, and so on — but in every case only at *integer*
multiples. A signal that is *not* periodic — a single isolated pulse,
say — has instead a **continuous** spectrum: energy spread over a
continuum of frequencies, no lines.

That is the fact this chapter rests on. The math behind it is the
Fourier series: *periodic ⟺ discrete (integer-indexed)* in the
conjugate variable. It is well-known to any reader who has plotted a
square wave's spectrum on a scope.

The point of the chapter is that **the same fact applies to a phase.**
If a wave's phase lives on a compact circle — closes back on itself
after 2π — then the variable conjugate to it (the occupation number)
has a discrete, integer spectrum. **Not because anything is digital.
Not because the values are quantised. Because the phase is periodic.**
The lattice's job is to provide such a compact phase; the integer
ladder follows from the same Fourier-series fact that puts a line
spectrum on a square wave.

The rest of the chapter says this carefully, separates two converging
arguments for it, and marks the one piece that has to come in from
chapter 6.

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

## 5.6 What the energy route rigorously delivers, and what it does not

The energetic route deserves a careful accounting, because it is easy
to mistake what it does. On a bounded, periodic cell whose magnitude
is *pinned* (a value on a circle has no separate amplitude — Chapter 1
§1.2), the energy of a wave is carried by **transitions**, and the
number of transitions per unit time is proportional to frequency. The
result is the rigorous scaling

> power ∝ ω.

In concrete terms: on a binary ±1 substrate driven at the clock's
maximum frequency the cell flips every tick — maximum transition rate,
maximum power; halve the drive frequency and the flip rate halves and
so does the power. There is *no amplitude knob* on a pinned-magnitude
cell to hide energy in — frequency is the only variable that can carry
it. So far, so rigorous.

The step from this scaling to the *quantum* relation E = ℏω is
different. "Action per cycle = h" is the Bohr–Sommerfeld /
single-valuedness postulate that §5.2 used to get integer N̂ — it is
what *promotes* the classical scaling into a quantised step. The
energy route delivers Planck's *scaling* on its own; the *quantisation
of action* into integer-h units is the same import as P3's integer N̂,
brought in from chapter 6. So this route is rigorous on E ∝ ω, and
imports the rest. Stated otherwise: bounding the magnitude buys the
scaling; getting the rungs themselves takes the complex amplitude.

## 5.7 What light-quantization *is*, in the model

Putting it together: in this model, "light is quantized" is the
statement that a wave on the lattice has a phase that lives on a
compact circle (the ℵ-line of A3), and that the state on that circle
is a single-valued complex amplitude. From those two ingredients —
periodicity and a complex amplitude — the Fourier-series fact forces
the occupation ladder to be integer (P3), and action-per-cycle = h
forces the rung size to be ℏω (P4). The compact circle is grid-derived;
the complex amplitude is the imported piece. **Periodicity, not
discreteness, is what does the quantising.** That is what
light-quantization *is*, in the model — modulo the one import named in
the next entry of the [arc](README.md#presentation-arc).

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
