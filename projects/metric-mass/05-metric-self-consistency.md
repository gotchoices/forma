# Chapter 5 — Self-consistency of the bare metric under standing-wave particles

[Chapter 1](01-foundation.md) posited a bare diagonal metric on M
as the *starting* condition, with the understanding (Chapter 1 §3)
that whether the metric stays diagonal is an open question. The
project's central question, stated then, was:

> When we put just light (no mass, no gravity, no charge) on the
> manifold M, do we expect off-diagonal entries of the metric to
> remain zero, or does something force them to develop?

The intervening chapters produced the modes (Chapter 2), examined
their phase structure (Chapter 3), and characterized their
behavior under linear superposition (Chapter 4). Those chapters
treated the wave equation generally — both ±n traveling-wave
solutions are mathematically valid, and the analysis was
agnostic about which combination corresponds to a physical
particle. This chapter takes the next step and identifies the
standing wave as the candidate particle, then asks the
metric-self-consistency question for it.

#### The standing-wave reading

The structural argument is short. A traveling wave around the
compact direction has a definite direction of propagation
around the loop — the sign of n labels which way the phase
rotates around u. A particle on M, however, should not carry a
built-in direction of propagation around a compact internal
coordinate; nothing about "being a particle" picks out one
direction around the loop over the other.

The natural construction without a preferred direction is the
**standing wave**: the equal-amplitude superposition of the +n
and −n traveling-wave components. The standing wave travels
"both ways or neither way" around the loop — equivalently, its
phase has fixed nodes and antinodes in u rather than rotating in
one direction. The ±n components are not separate physical
objects that occasionally meet; they are the *two solutions of
the same wave equation that, together, build the directionless
standing wave that is the particle*.

This reading aligns with the broader project arc. In
[metric-charge](../metric-charge/), particles are knots on a 2D
compact sheet — closed wavefronts of standing waves on T². The
1D analog that lives on metric-mass's compact circle is exactly
the ±n superposition: a standing wave on S¹.

#### What this chapter does

For the standing-wave particle, this chapter computes the
stress-energy and reads off what the metric must do. The
calculation proceeds in two stages:

- **Per-component (§§2–5).** Compute the stress-energy of a
  single +n traveling-wave component as an intermediate. This
  *would* source off-diagonal cross terms. The math here is
  textbook KK and reproduces the standard result.
- **Standing-wave particle (§§7–8).** Combine the +n and −n
  components into the standing wave. The n-linear cross-terms
  cancel exactly, and the standing-wave particle's stress-energy
  is purely diagonal (in the rest case). The bare diagonal metric
  is preserved.

Chapter 1's stance was to *not* impose Einstein's equations as
part of the project's setup ("Gravity. Einstein's equations are
not in play"). This chapter examines what would happen *if we
did*. The choice to look at this question is a deliberate
extension of scope: we keep the bare metric as Chapter 1 set it,
and ask what extra structure Einstein's equations would source on
top of it.

The headline result, in short: **the standing-wave particle is
consistent with the bare diagonal metric**. The single-component
analysis of §§2–5 *would* source off-diagonal cross terms, but
the standing wave is the sum of two oppositely-directed
components whose n-linear cross-term contributions cancel
exactly, leaving only the diagonal modifications (g_tt, g_uu)
that the rest energy naturally produces.

#### A note on chapter-3 / chapter-4 framing

Chapters 3 and 4 spoke loosely of ±n as a "matter/antimatter
analog," in line with how canonical Kaluza-Klein theory
identifies ±n traveling-wave components as charge sign (particle
and antiparticle). Under the standing-wave reading developed here,
that framing does not survive: ±n components are not separate
particles that occasionally meet — they are the two components
of a *single* standing-wave particle, always present together.
The framework on the minimal manifold (t, S, u) does not, on its
own, supply a clear antimatter analog; whether antimatter
corresponds to a standing wave of opposite polarity, requires
additional structure (e.g., the second compact direction in
metric-charge, or a substrate-level chirality asymmetry as in
grid-primitive chapter 9), or is simply not present at this
level, is left open. This chapter does not commit to an
antimatter interpretation.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | Two senses of "self-consistent" |
| 2 | Per-component stress-energy: a single ±n traveling wave |
| 3 | Reading the cross-terms: what's nonzero per component |
| 4 | The chicken-and-egg problem |
| 5 | Per-component back-reaction: what a single component would source |
| 6 | The Kaluza-Klein parallel |
| 7 | The standing-wave particle: cross-term cancellation |
| 8 | Putting the chart together: standing-wave vs single-component |
| 9 | What this chapter does not settle |
| 10 | End of Chapter 5 |

---

## 1. Two senses of "self-consistent"

The phrase "self-consistent metric" can mean two related but
distinct things, and it helps to separate them.

**Sense (a): the wave equation has solutions on the bare metric.**
This is the question Chapter 2 answered: given the bare metric of
Chapter 1, does □φ = 0 admit solutions? The answer was yes — a
discrete family of modes labeled by (n, k_S). In this sense, the
bare metric is already self-consistent: the equation has
solutions, no contradiction. Chapter 1's choice of metric was not
ruled out by anything that came after.

**Sense (b): the stress-energy of those solutions is consistent
with the metric, given Einstein's equations.** This is the
deeper question. Once we have the field φ on M, the field carries
energy, momentum, and pressure — together encoded in the
stress-energy tensor T_μν. Einstein's equations relate T_μν to
the curvature of g_μν. If we *demand* that the metric on M
satisfy Einstein's equations with the field's stress-energy as
source, would the bare diagonal metric still suffice? Or would
the field's stress-energy require curvature, off-diagonal entries,
or position dependence that the bare metric does not have?

Chapter 1 §9 declined to impose Einstein's equations as part of
the project's setup ("Gravity. Einstein's equations are not in
play"). This chapter examines what would happen *if we did*.
The choice to look at sense (b) is a deliberate extension of
scope: we keep the bare metric as Chapter 1 set it, and ask
what extra structure Einstein's equations would source on top
of it.

The remainder of the chapter computes this. The result is
informative regardless of whether one ultimately chooses to
impose Einstein's equations on M.

---

## 2. Per-component stress-energy: a single ±n traveling wave

We compute the stress-energy of a single traveling-wave component
of the form φ_n = e^{i(k_S S − ωt + nu/R_u)} for a fixed sign of
n. This is *not yet the particle* — under the standing-wave
reading the physical particle is the ±n superposition, computed
in §7. But the per-component stress-energy is the building block
the standing wave is constructed from, and the cross-term
structure that surfaces here is what §7 will show cancels in the
full superposition. Working through the per-component case first
gives the cross-term pattern that the standing-wave construction
will partially undo.

The stress-energy tensor of a complex scalar field with
Lagrangian L = g^μν ∂_μ φ* ∂_ν φ is

<!-- T_μν = ∂_μ φ* ∂_ν φ + ∂_ν φ* ∂_μ φ - g_μν L -->
$$
T_{\mu\nu}
\;=\; \partial_\mu \varphi^* \,\partial_\nu \varphi
\;+\; \partial_\nu \varphi^* \,\partial_\mu \varphi
\;-\; g_{\mu\nu}\,\mathcal{L}
$$

For a single mode

<!-- φ = exp(i(k_S S - ω t + n u/R_u)) -->
$$
\varphi(t, S, u) = \exp\!\bigl(i\,(k_S\,S - \omega\,t + n\,u/R_u)\bigr)
$$

each derivative pulls down a factor of i times the corresponding
"k-component":

<!-- ∂_t φ = -iω φ,  ∂_S φ = i k_S φ,  ∂_u φ = i (n/R_u) φ -->
$$
\partial_t \varphi = -i\omega\,\varphi,
\qquad
\partial_S \varphi = i\,k_S\,\varphi,
\qquad
\partial_u \varphi = i\,\frac{n}{R_u}\,\varphi
$$

Define a covector

<!-- k_μ = (-ω, k_S, n/R_u) -->
$$
k_\mu = \bigl(-\omega,\; k_S,\; n/R_u\bigr)
$$

so that ∂_μ φ = i k_μ φ and ∂_μ φ* = −i k_μ φ*. Then the
factored product is

<!-- ∂_μ φ* ∂_ν φ = k_μ k_ν |φ|² -->
$$
\partial_\mu \varphi^*\,\partial_\nu \varphi = k_\mu\,k_\nu\,|\varphi|^2
$$

Symmetrizing over (μ, ν) and using the on-shell value
L = 0 (which holds because g^μν k_μ k_ν = −ω²/c² + k_S² + (n/R_u)² = 0
by the dispersion relation), the stress-energy reduces to the
clean form

<!-- T_μν = 2 k_μ k_ν |φ|²  (on-shell) -->
$$
\boxed{\;T_{\mu\nu} = 2\,k_\mu\,k_\nu\,|\varphi|^2\;}
$$

For a normalized plane-wave mode, |φ|² = 1, so the stress-energy
is constant throughout space. (For a localized wave packet, |φ|²
is the envelope amplitude squared — peaked where the packet is,
falling off outside it.)

The factored form says: every entry of T_μν is the product of
two components of k_μ. The pattern of zeros and non-zeros in
T_μν is therefore controlled entirely by the pattern of zeros in
k_μ = (−ω, k_S, n/R_u).

---

## 3. Reading the cross-terms: what's nonzero, when

Write out the matrix. With coordinates ordered (t, S, u):

<!-- T_μν = 2|φ|² · k_μ k_ν matrix -->
$$
T_{\mu\nu}
= 2\,|\varphi|^2
  \begin{pmatrix}
   \omega^2 & -\omega\,k_S & -\omega\,n/R_u \\
   -\omega\,k_S & k_S^2 & k_S\,n/R_u \\
   -\omega\,n/R_u & k_S\,n/R_u & (n/R_u)^2
  \end{pmatrix}
$$

Reading off the diagonal entries:

| Entry | Value | Nonzero when |
|---|---|---|
| T_tt | 2ω² \|φ\|² | ω ≠ 0 (i.e., the field oscillates in time) |
| T_SS | 2 k_S² \|φ\|² | k_S ≠ 0 (the field has spatial structure) |
| T_uu | 2 (n/R_u)² \|φ\|² | n ≠ 0 (the field winds around u) |

And the off-diagonal entries (cross-terms in the stress-energy):

| Entry | Value | Nonzero when |
|---|---|---|
| T_tS | −2 ω k_S \|φ\|² | ω ≠ 0 AND k_S ≠ 0 |
| T_tu | −2 ω (n/R_u) \|φ\|² | ω ≠ 0 AND n ≠ 0 |
| T_Su | 2 k_S (n/R_u) \|φ\|² | k_S ≠ 0 AND n ≠ 0 |

The pattern is clean: every cross-term in T_μν is the product of
two k-components, and is therefore nonzero exactly when *both*
factors are nonzero.

By configuration:

| Mode configuration | Nonzero T entries |
|---|---|
| No field (φ = 0 everywhere) | none — T_μν = 0 |
| Light at rest (n = 0, k_S = 0): degenerate, ω = 0 | T_μν = 0 |
| Light moving (n = 0, k_S ≠ 0): ω = c\|k_S\| | T_tt, T_SS, T_tS only |
| Mass at rest (n ≠ 0, k_S = 0): ω = ω_rest | T_tt, T_uu, **T_tu** only |
| Mass moving (n ≠ 0, k_S ≠ 0) | T_tt, T_SS, T_uu, **T_tS, T_tu, T_Su** all nonzero |

Two observations stand out:

1. **A massive mode at rest carries a nonzero T_tu.** Even at
   k_S = 0 (no spatial momentum), the cross-term between time
   and the compact direction is nonzero. This is sourced by the
   product ω·(n/R_u): the rest frequency times the
   compact-direction wavenumber. Both of these are nonzero for
   any massive mode, so T_tu is present whenever mass is
   present.
2. **A light mode at rest carries no stress-energy.** With
   n = 0, k_S = 0, the dispersion relation gives ω = 0, and
   every component of T_μν vanishes. There is, in this
   limit, no field to speak of; this is the trivial case of
   §1's no-field configuration.

The pattern is structural: T_μν cross-terms appear when the
corresponding pair of k-components are both nonzero, full stop.

#### Sanity check: the trace

The on-shell trace of T_μν is

<!-- T^μ_μ = g^μν T_μν -->
$$
T^\mu_{\;\mu} = g^{\mu\nu}\,T_{\mu\nu}
\;=\; 2|\varphi|^2 \cdot g^{\mu\nu}\,k_\mu\,k_\nu
$$

For our diagonal bare metric (g^tt = −1/c², g^SS = g^uu = 1):

<!-- T^μ_μ = 2|φ|² · (-ω²/c² + k_S² + (n/R_u)²) -->
$$
T^\mu_{\;\mu} = 2|\varphi|^2 \cdot \left(-\frac{\omega^2}{c^2} + k_S^2 + \frac{n^2}{R_u^2}\right) \;=\; 0
$$

The bracket vanishes by the dispersion relation. So T_μν is
*traceless on-shell* — a standard property of a massless scalar
field's stress-energy. Useful as a check on the algebra.

---

## 4. The chicken-and-egg problem

Before proceeding, an honest acknowledgment.

The wave equation we used in Chapter 2 was □φ = 0 with the
d'Alembertian computed on the bare diagonal metric. The
stress-energy of §2 was computed using *those* solutions and
*that* metric.

If we now demand that Einstein's equations be satisfied — and
they require the metric to be modified by the stress-energy —
then the metric is no longer the bare flat one. But changing the
metric changes the wave equation, which changes the solutions,
which changes the stress-energy, which changes the required
metric modification, and so on.

This is a self-consistency loop, and it is non-trivial in
general. There are two standard ways to handle it:

- **The test-field approximation.** Treat the field as
  propagating on a fixed background (the bare metric), and
  ignore back-reaction. This is justified when the field's
  energy density is small compared to whatever scale sets the
  metric's curvature — for example, when G·T/c⁴ is small.
- **Self-consistent solution.** Demand simultaneous solution of
  the wave equation and Einstein's equations. This is what
  full general relativity does. It is technically harder, and
  in 1+1+1D = 3D requires solving the coupled system explicitly.

In linearized gravity, the two are reconciled at leading order:
g_μν = η_μν + h_μν with h small, T_μν computed on the
unperturbed background, h sourced by T to leading order. The
back-reaction is *consistent* with the test-field calculation
to first order in h.

For this chapter, we use the test-field calculation as the
primary tool. It gives the right pattern of source contributions
(which off-diagonals would be sourced) and lets us read off the
direction of metric modification without solving the full
coupled system. We note where the linearized story would
require corrections and where the full nonlinear system might
differ.

---

## 5. Per-component back-reaction: what a single component would source

This section reads off the metric implications of the
single-component stress-energy from §3. A +n traveling-wave
component, treated as if it were itself the particle, would
source g_tu (and additionally g_tS, g_Su when moving). §7 then
combines the +n and −n components into the standing wave that
*is* the particle and shows that the n-linear cross-term
sourcings cancel.

A note on the relationship to Kaluza-Klein theory before
proceeding. The cross-term pattern that emerges in this section
is *similar in form* to what KK produces — both involve
off-diagonal entries between a 4D direction and the compact
direction sourced by compact-direction wavenumber — but the
underlying physical setups are different. Standard KK
([primers/kaluza-klein.md](../../primers/kaluza-klein.md))
posits a 4D theory of gravity *plus a massive* (or charged)
particle on a manifold with one compact extra direction; the
off-diagonal cross-term that emerges is identified with the
electromagnetic potential and is *real and lingering* — it does
not cancel, because KK takes definite-charge particles as input
(particles and antiparticles are separate states, not coherent
superpositions). This project, by contrast, posits *light only*
(no mass, no charge) on a manifold with one compact direction;
mass emerges from the wave's compact-direction structure
(Chapter 2), and the per-component cross-term that surfaces
here is then a candidate for cancellation when the per-component
intermediates are assembled into the directionless standing-wave
particle that the project commits to as the physical state.
The two frameworks share mathematical machinery at the
per-component level but differ in starting point and in what
the cross-term ultimately does. §7 shows that ours, hopefully,
vanishes.

Linearized Einstein equations around the bare metric η_μν take
the form

<!-- (linear operator on h_μν) ∝ T_μν -->
$$
\mathcal{D}_{\mu\nu}[h] \;\propto\; T_{\mu\nu}
$$

where D is a linear differential operator (in Lorenz gauge,
proportional to □ acting on the trace-reversed h̄_μν). The
proportionality constant is 8πG/c⁴.

Without solving the operator equation, we can read off the
*pattern* of metric corrections directly from T_μν: each entry
T_μν that is nonzero will source a corresponding nonzero h_μν
(modulo the operator's structure, which preserves the index
pattern in our setting). The amplitudes are tiny (proportional to
G), but the pattern is what matters here.

So the metric modification sourced by each mode configuration
follows the same chart as §3:

| Mode configuration | Cross-terms sourced in g_μν |
|---|---|
| No field | none — bare diagonal metric is fully consistent |
| Light moving (n = 0, k_S ≠ 0) | g_tS only |
| Mass at rest (n ≠ 0, k_S = 0) | g_tu only |
| Mass moving (n ≠ 0, k_S ≠ 0) | g_tu, g_tS, g_Su all |

Three things follow:

1. **In vacuum (no field), the bare diagonal metric is fully
   self-consistent.** No cross-terms are sourced. The metric
   we set in Chapter 1 is what it is.
2. **Light moving sources g_tS.** This is the conventional
   cross-term between time and the spatial direction it is
   moving in — the same structure that appears in any "moving
   energy density" source in GR (Poynting-like flux). It is
   not specific to our compact dimension.
3. **Mass at rest sources g_tu, but NOT g_tS or g_Su.** The
   only off-diagonal sourced is the time-compact entry. This is
   a striking observation: the presence of mass at rest forces
   *exactly one* off-diagonal entry to develop, and it is the
   one that mixes time with the compact direction.

The third point is the most novel for the per-component picture.
A single +n (or single −n) traveling-wave component, treated as
if it were a particle, would force the bare metric to develop a
g_tu cross-term — the same form of off-diagonal that KK's
external-mass calculation produces.

This is **not** yet the answer to the project's central question.
Under the standing-wave reading developed in this chapter's
intro, the physical particle is the ±n superposition, not a
single component. §7 carries out the standing-wave calculation
and shows that the n-linear cross-term sourcings (g_tu, and at
non-zero k_S also g_Su) cancel exactly — the directionless
standing-wave particle has no compact-direction current to
source those off-diagonals. Only the n-independent cross-term
(g_tS, present only for moving particles, sourced by the
conventional Poynting-like flux of the moving energy density)
survives. This is where our framework diverges from KK's
"lingering cross term" picture: KK's particle is the per-component
object and its cross term is real; our particle is the standing
wave and its corresponding cross term cancels.

The summary at the end of §8 brings the per-component (this
section) and standing-wave (§7) results together side by side.

---

## 6. The Kaluza-Klein parallel

This project is a Kaluza-Klein-style construction
([primers/kaluza-klein.md](../../primers/kaluza-klein.md)) — a
manifold with one compact extra dimension, with off-diagonal
metric components arising from compact-direction wave structure.
The math at the per-component level is recognisably the
KK calculation. But the project's setup and the resulting
fate of the cross-term differ from canonical KK in two
specific ways worth flagging.

#### Different starting points

Canonical KK begins with 4D gravity plus a *massive* (or
charged) particle on a 5D manifold with one compact direction.
The starting object is a particle that already carries mass and
charge; the off-diagonal cross-term g_μ5 then appears in
Einstein's equations and is identified with the electromagnetic
potential A_μ. The KK punchline is that adding one compact
extra dimension to gravity (plus an external particle) produces
electromagnetism.

This project begins with **light only** (no mass, no charge) on
the (t, S, u) manifold with u compact. There is no externally
postulated particle; mass *emerges* from the compact-direction
wave structure (Chapter 2). The per-component cross-term that
arises in §§2–5 has the same off-diagonal index structure as
KK's g_μ5, but its origin is sourced by the wave's
compact-direction wavenumber n rather than by an externally-given
charge. The KK machinery applies; the input differs.

#### Different fates of the cross-term

The more substantive difference is what happens to the
cross-term. Canonical KK's g_μ5 *lingers*: a definite-charge
particle and its antiparticle are treated as separate states
(not coherent superpositions), each sources its own cross-term,
and the cross-term does not cancel. The lingering g_μ5 *is* the
EM potential — it is the entire point of canonical KK.

This project's per-component cross-term, by contrast, is hoped
(and §7 will confirm) to *vanish* for the directionless
standing-wave particle. The standing wave is the equal-amplitude
superposition of +n and −n components; its compact-direction
"current" is zero by construction; its per-component
cross-terms cancel structurally. There is no lingering EM
potential — and therefore no electromagnetism — produced by
this framework's mass particle on the minimal manifold.

That asymmetry between canonical KK and this project is what the
standing-wave reading is doing. KK produces a lingering cross
term and gets EM out of it; this project produces a cross term
that cancels and gets a clean diagonal metric for rest mass.
The shared KK machinery (off-diagonal sourcing by
compact-direction wavenumber) does not force a shared physical
outcome — what survives the construction depends on what kind of
particle is taken as the physical state.

#### What this means for the project

The metric-mass project does not produce electromagnetism. It
produces mass, via the compact-direction wave structure of
Chapter 2 and the diagonal stress-energy of §7. Whether *charge*
exists in this framework — and if so, where — is the question
[metric-charge](../metric-charge/) takes up. There the answer
involves a *second* compact direction (a 2D compact sheet
rather than a single compact circle), and the topological
structure of T² supplies the gauge structure that one compact
direction alone does not.

One way to read the relationship: canonical KK's "compact
dimension produces EM" works because it puts mass in by hand
and gets EM out via the lingering cross-term. This project puts
light in only, and the same KK machinery produces *just mass* —
the cross-term cancels for the directionless standing-wave
particle, leaving rest mass as the sole macroscopic signature.
EM (or its analog) requires the second compact direction. The
metric-mass result that the bare diagonal metric is preserved
by the rest standing-wave particle is therefore consistent with
"no EM at this level," not in conflict with the KK parallel.

#### Looking ahead to Chapter 6

Chapter 6 picks up the gravitational consequences. Under the
standing-wave reading, the rest-mass particle is purely diagonal
in stress-energy, so its leading gravitational signature is the
diagonal modification of the metric (g_tt and g_uu). Off-diagonal
contributions appear only when the particle is *moving* (g_tS
from the conventional Poynting-like flux). The relevant
perturbations for the standing-wave particle are the diagonal
ones — rest-energy density curving spacetime in the conventional
GR way — not the off-diagonal g_tu of the per-component
intermediate.

---

## 7. The standing-wave particle: cross-term cancellation

This is the central calculation of the chapter. The
per-component analysis of §§2–5 was the intermediate; this
section assembles the standing-wave particle from its ±n
components and reads off what its stress-energy actually
requires of the metric.

The standing-wave particle is by construction the equal-amplitude
superposition φ = φ_+ + φ_-, where

<!-- φ_+ = exp(i(k_S S - ω t + n u/R_u)),  φ_- = exp(i(k_S S - ω t - n u/R_u)) -->
$$
\varphi_+ = e^{i(k_S S - \omega t + n u/R_u)},
\qquad
\varphi_- = e^{i(k_S S - \omega t - n u/R_u)}
$$

(both with the same k_S and ω, since |n| determines ω
identically for ±n), the stress-energy is bilinear in φ. So
T_μν^{total} = T_μν[φ_+] + T_μν[φ_-] + (cross-terms in
φ_+ φ_-*).

The cross-terms involve products like φ_+* · φ_- ∝ exp(−2inu/R_u),
which is rapidly oscillating in u and integrates to zero over the
compact circle. So the *integrated* (over u) cross-terms vanish:

<!-- ∫ du (cross-terms) = 0 -->
$$
\int_0^{L_u} du \;(\text{cross-terms in } \varphi_+ \varphi_-^*) \;=\; 0
$$

Thus the (u-integrated) total stress-energy is just the sum of
the individual contributions:

<!-- T_μν^{total} = T_μν^{+} + T_μν^{-}  (after u-averaging) -->
$$
T_{\mu\nu}^\text{total} = T_{\mu\nu}^{+} + T_{\mu\nu}^{-}
$$

Here T_μν^{+} uses k^+_μ = (−ω, k_S, +n/R_u) and T_μν^{-} uses
k^-_μ = (−ω, k_S, −n/R_u). Adding:

| Entry | T^+ + T^- | Result |
|---|---|---|
| T_tt | 2ω² + 2ω² | 4ω² (doubles) |
| T_SS | 2k_S² + 2k_S² | 4k_S² (doubles) |
| T_uu | 2(n/R_u)² + 2(n/R_u)² | 4(n/R_u)² (doubles) |
| T_tS | −2ωk_S − 2ωk_S | −4ωk_S (doubles) |
| T_tu | −2ω(n/R_u) − 2ω(−n/R_u) | **0 (cancels)** |
| T_Su | 2k_S(n/R_u) + 2k_S(−n/R_u) | **0 (cancels)** |

The two n-linear cross-terms vanish identically. The
cancellation is exact and follows from the per-component T being
linear in n for those entries: the +n and −n contributions to
T_tu and T_Su have opposite signs and cancel, while entries that
involve n quadratically (T_uu) or not at all (T_tt, T_SS, T_tS)
have matching signs and add.

So for the standing-wave particle:

- **Diagonal entries (T_tt, T_SS, T_uu) double** relative to a
  single component. Energy and pressure are additive across the
  two components, and the integrated rest energy of the
  standing wave is twice that of either component alone.
- **The n-linear cross-terms (T_tu, T_Su) cancel structurally**.
  These are the off-diagonal entries that involve the
  compact-direction wavenumber linearly; they are exactly absent
  in the standing-wave configuration by virtue of the
  directionless construction.
- **The n-independent cross-term T_tS survives, doubled**. This
  cross-term is non-zero only when k_S ≠ 0 (the standing-wave
  particle is moving in S). It has no n-dependence, so the
  ±n cancellation does not touch it; it is the conventional
  Poynting-like flux of moving energy density, present for any
  moving mass.

In particular, for a **standing-wave particle at rest**
(k_S = 0): T_tS also vanishes, and the total stress-energy is
purely diagonal:

<!-- For standing wave at rest: T_μν = 2|φ|² · diag(2ω², 0, 2(n/R_u)²) -->
$$
T_{\mu\nu}^\text{rest standing-wave particle} = 2|\varphi|^2 \cdot \mathrm{diag}\bigl(2\omega^2,\; 0,\; 2(n/R_u)^2\bigr)
$$

(written here in matrix form with coordinate ordering (t, S, u);
the factor of 2 inside the diag comes from the doubled
contributions from the ±n components, and the prefactor 2|φ|²
is the standard stress-energy normalization).

#### Implication for the metric

Following §5: a rest standing-wave particle sources *no*
off-diagonal entries in g_μν. The metric modification it
produces, under linearized Einstein's equations, is
**purely diagonal**:

- g_tu cross-term: not sourced (cancelled by the standing-wave
  construction).
- g_Su cross-term: not sourced (k_S = 0; would also cancel for
  k_S ≠ 0).
- g_tS cross-term: not sourced (k_S = 0).
- Diagonal entries (g_tt, g_uu) modified by the rest-energy
  density.

This is the chapter's central result: **the bare diagonal metric
of Chapter 1 is preserved by the rest standing-wave particle**.
What appeared at the per-component level (§5) as a mandatory
off-diagonal sourcing — the KK-style single-mode g_tu — vanishes
when the per-component intermediate is assembled into the actual
physical particle. The off-diagonal cross-terms
do not "dangle"; they cancel structurally.

The non-zero diagonal stress-energy still curves spacetime in the
ordinary way: a localised standing-wave particle's rest energy
modifies g_tt and g_uu in its vicinity, producing the
gravitational signature of mass. Chapter 6 takes up the
gravitational consequences in detail. What this section
establishes is the *off-diagonal* result: the standing-wave
particle does not source the KK-style off-diagonal gauge
potential that a single traveling-wave component would.

#### Why the cancellation is structural, not coincidental

A useful way to see why the cancellation is forced rather than
fortunate: the n-linear cross-terms T_tu and T_Su exist only
because a per-component configuration carries a *direction*
around the compact loop. T_tu = −2ω(n/R_u) is, physically, a
flux of the compact-direction wavenumber n in the time
direction — a "current" of compact-direction winding. T_Su is
the analogous spatial component of that current.

A traveling wave with definite n carries this current; the sign
of the current is set by the sign of n (the direction of the
phase rotation around u). A directionless standing wave does
not carry a current of n in any direction — it has no preferred
direction around the loop, so no flux of n to flow. The
cancellation in the summed stress-energy is the algebraic
expression of this physical fact: the per-component T_tu and
T_Su flip sign under n → −n, so the standing-wave sum (which is
symmetric in ±n by construction) annihilates them.

The n-independent cross-term T_tS, by contrast, expresses
ordinary Poynting flux that has nothing to do with the loop
direction; it survives because the standing wave can still move
bodily in S even though it has no internal direction around u.

---

## 8. Putting the chart together: standing-wave vs single-component

The chapter's analysis splits cleanly into two readings of "the
particle" — the per-component intermediate and the standing
wave that the project commits to. The chart below records what
each reading would source under Einstein's equations.

| Configuration | Off-diagonals that would be sourced |
|---|---|
| No field (vacuum) | none — bare diagonal metric is fully consistent |
| Light moving (n = 0, k_S ≠ 0) | g_tS only (n-independent Poynting flux) |
| Single ±n component at rest (per-component intermediate) | g_tu only |
| Single ±n component moving (per-component intermediate) | g_tu, g_tS, g_Su all |
| **Standing-wave particle at rest** (this project's reading) | **none — bare metric preserved** |
| **Standing-wave particle moving** (this project's reading) | **g_tS only** (n-independent Poynting flux) |

The two single-component rows are the canonical KK result for
a definite-charge particle, included for comparison and as the
per-component intermediates the standing-wave particle is
built from. The two
boldface rows are the project's primary results: under the
standing-wave reading, the n-linear cross-terms (g_tu and g_Su)
cancel structurally, and what survives is exactly the
n-independent Poynting cross-term (g_tS) that any moving energy
density produces.

The bare diagonal metric of Chapter 1 is therefore:

- **Self-consistent in vacuum.** No cross-terms forced.
- **Self-consistent for light only.** g_tS appears for moving
  light, but rest light is degenerate (no field).
- **Self-consistent for the rest standing-wave particle.** The
  particle's stress-energy is purely diagonal; the
  per-component g_tu cancels by the standing-wave construction.
- **Sources g_tS for moving particles.** This is the
  conventional flux-of-energy cross-term, present for any
  moving mass; it does not depend on the compact-direction
  structure.

The diagonal entries (g_tt, g_uu) are still modified by the
particle's rest-energy density — that is the gravitational
signature of mass, taken up in Chapter 6.

This is the structural answer the math gives under the
standing-wave reading: **the bare diagonal metric is preserved
by rest mass, and only the conventional Poynting-flux
cross-term g_tS appears for moving mass**. There is no g_tu
"frame-dragging in u" of the kind that appeared for the
single-component intermediate.

#### Reading the result: the metric *is* the gravitational field

The metric *is* the gravitational field, in the standard
general-relativistic sense — the gravitational field is the
deviation of the metric from a flat reference
([primers/metric.md §9](../../primers/metric.md)). For the
standing-wave particle on M, this deviation is purely diagonal
in the rest case: the rest-energy density modifies g_tt and
g_uu, and those modifications constitute the particle's
gravitational signature.

This is qualitatively the same picture as a localised energy
density in standard 1+3D general relativity (Schwarzschild-style
diagonal-only metric for a static mass); the off-diagonal
"frame-dragging" entries that appear in Kerr require actual
rotation, and they appear here only for a moving particle (and
then only as the conventional Poynting cross-term g_tS, not as
a compact-direction g_tu). The standing-wave reading therefore
brings the project's gravitational picture back into agreement
with the standard GR intuition for a static mass: a localised
diagonal modification of the metric, no off-diagonal mystery.

#### Two masses: superposition of contributions

For two masses on M, there is **one** metric that satisfies
Einstein's equations sourced by both stress-energies together,
not two separate metrics. In the linearized regime
(g_μν = η_μν + h_μν with h small), the equation
□ h_μν ∝ T_μν is linear, so contributions add:

<!-- h_μν^total = h_μν^[mass 1] + h_μν^[mass 2]  (linearized) -->
$$
h_{\mu\nu}^\text{total} = h_{\mu\nu}^{[\text{mass 1}]} + h_{\mu\nu}^{[\text{mass 2}]}
$$

Each mass independently sources its own diagonal modifications
(g_tt and g_uu, plus g_tS if moving), and the total at any
spacetime point is the sum of the contributions from each
source. This linear superposition of metric perturbations is
the standard formalism by which "two masses each warp
spacetime" produces an interference pattern of warps —
exactly the picture observers expect from two gravitating
bodies.

Outside the linearized regime, this superposition is only
approximate: at higher orders, the contributions interact via
the nonlinearity of the Einstein tensor. But for any
physically realistic field amplitude on M, the linearized
picture is exact to extraordinary precision.

So the reading is: the chapter has effectively *shown the
mechanism* for how mass on M produces gravitational warping.
Multiple masses produce multiple linearly-superposed
contributions, and the total diagonal metric deformation at
any point is the gravitational field there. This is the
spacetime warping we expect from masses, derived inside the
framework's own machinery rather than imposed from outside.

#### Two masses: superposition of contributions

For two masses on M, there is **one** metric that satisfies
Einstein's equations sourced by both stress-energies together,
not two separate metrics. In the linearized regime
(g_μν = η_μν + h_μν with h small), the equation
□ h_μν ∝ T_μν is linear, so contributions add:

<!-- h_μν^total = h_μν^[mass 1] + h_μν^[mass 2]  (linearized) -->
$$
h_{\mu\nu}^\text{total} = h_{\mu\nu}^{[\text{mass 1}]} + h_{\mu\nu}^{[\text{mass 2}]}
$$

Each mass independently sources its own g_tu (and other
modifications), and the total off-diagonal entries at any
spacetime point are the sum of the contributions from each
source. This linear superposition of metric perturbations is
the standard formalism by which "two masses each warp
spacetime" produces an interference pattern of warps —
exactly the picture observers expect from two gravitating
bodies.

Outside the linearized regime, this superposition is only
approximate: at higher orders, the contributions interact via
the nonlinearity of the Einstein tensor. But for any
physically realistic field amplitude on M, the linearized
picture is exact to extraordinary precision.

So the reading is: yes, the chapter has effectively *shown
the mechanism* for how mass on M produces gravitational
warping. Multiple masses produce multiple linearly-superposed
contributions, and the total off-diagonal-and-diagonal metric
deformation at any point is the gravitational field there.
This is the spacetime warping we expect from masses, derived
inside the framework's own machinery rather than imposed from
outside.

#### Comparison with Schwarzschild and Kerr

The standing-wave reading aligns the project's static-mass
result with the standard general-relativistic picture:

- The **Schwarzschild** metric (a static, non-rotating spherical
  mass in vacuum) is *purely diagonal*. A particle at rest
  produces no off-diagonal entries; gravity manifests as
  diagonal modifications of g_tt and g_rr (gravitational time
  dilation and radial-ruler stretching). Orbits emerge from
  the diagonal curvature via the geodesic equation; no
  off-diagonal cross-term is needed for orbital mechanics.
- The **Kerr** metric (a rotating mass) does have an
  off-diagonal: g_tφ ≠ 0, called *frame-dragging*. Spacetime
  near a spinning mass is dragged around in the direction of
  the rotation, mixing time with the azimuthal direction. This
  off-diagonal vanishes when the mass stops spinning.

In our framework, the rest standing-wave particle on M sources
a *purely diagonal* metric perturbation — the same qualitative
structure as Schwarzschild's static mass. There is no g_tu
"frame-dragging in u" when the particle is at rest; the
n-linear cross-term that would have given a Kerr-like signature
under the per-component intermediate is precisely the term that
the standing-wave construction cancels.

This is an alignment, not a coincidence. The Kerr g_tφ
off-diagonal in standard GR requires the mass to actually
rotate — the rotation breaks time-reversal symmetry by
selecting a definite rotational direction, and that breaking is
what sources the off-diagonal entry. Under the standing-wave
reading, a particle on M *also* has no rotational direction
(both ±n components are present), so by the same physical
argument it sources no analogous cross-term. The
Schwarzschild-like diagonal-only result for the rest particle
on M is the natural outcome of having no preferred direction
around the compact loop.

A moving standing-wave particle does source g_tS, the
n-independent Poynting-flux cross-term. This is the analog of
the off-diagonal piece a moving mass produces in any GR
calculation; it has no compact-direction-specific structure and
is not Kerr-like.

#### Orbits and extended dimensions

The diagonal modifications of g_tt and g_uu produced by the
rest standing-wave particle are the gravitational signature
that bends nearby trajectories. If the framework were extended
to multiple S dimensions (S_1, S_2, ... — beyond the scope of
this project), localised masses would source position-dependent
diagonal modifications g_tt(S), g_S_iS_i(S), and orbital
trajectories would emerge from those diagonal pieces in the
standard GR way — exactly as in Schwarzschild.

The standing-wave reading therefore makes the project's
gravity story qualitatively continuous with standard GR's
diagonal-only picture for static masses. There is no extra
compact-direction-specific off-diagonal signature for the rest
particle on M; the only place compact-direction structure
shows up gravitationally is via the modification of g_uu (the
"size" of the compact direction near the mass), which is a
diagonal effect, not an off-diagonal one.

---

## 9. What this chapter does not settle

The computation above is at the level of leading-order
linearized gravity, treating the wave field as a source on a
fixed background. Several things this chapter does not address:

- **The full nonlinear Einstein-Klein-Gordon system.** A
  self-consistent solution where the metric and field
  back-react on each other to all orders has not been
  attempted here. The leading-order pattern of cross-term
  sourcing is robust, but the magnitudes (and possibly the
  precise structure at higher orders) require a full
  calculation.
- **Whether Chapter 1's choice to *not* impose Einstein's
  equations is mandatory or optional.** This chapter has
  examined the consequences of imposing them. Whether the
  project should commit to imposing them as a permanent rule
  is a separate decision, not made here.
- **Magnitudes.** The cross-terms sourced by Einstein's
  equations are proportional to G·T/c⁴, which is extraordinarily
  small for any realistic field amplitude. The qualitative
  pattern (which cross-terms appear) is what this chapter
  reports; the actual numerical strength of the metric
  modifications would require a more detailed calculation.
- **Whether the off-diagonal cross-terms, once sourced, would
  in turn modify the wave equation enough to change the mode
  structure.** This is the chicken-and-egg problem of §4. At
  first order it does not, but at higher orders the
  back-reaction would feed into the wave equation and could
  shift dispersion or generate new effects.
- **Quantum mechanics.** This chapter is classical throughout.
  Quantum corrections to T_μν (the expectation value in some
  state of the quantized field) could change the answer. They
  are outside scope.

---

## 10. End of Chapter 5

#### What was computed

- Per-component stress-energy in the factored form
  T_μν = 2|φ|² k_μ k_ν, with k_μ = (−ω, k_S, n/R_u).
- Pattern of nonzero cross-terms in the per-component T_μν, by
  configuration: vacuum (none), light moving (T_tS only),
  single-component mass at rest (T_tu only), single-component
  mass moving (all three of T_tS, T_tu, T_Su).
- Pattern of off-diagonal entries that linearized Einstein's
  equations would source for the per-component intermediate.
- The standing-wave construction: ±n components combined into
  one particle. T_tu and T_Su cancel exactly; T_tt, T_SS, T_uu
  double; T_tS doubles when k_S ≠ 0 (n-independent).

#### What this chapter establishes

- The standing wave (±n superposition) is the candidate
  physical particle on M; the per-component traveling-wave
  pieces are intermediates the standing wave is built from.
- The bare diagonal metric of Chapter 1 is self-consistent in
  vacuum.
- **Under Einstein's equations, the bare diagonal metric is
  preserved by the rest standing-wave particle.** The particle
  sources purely diagonal stress-energy; no off-diagonals are
  forced.
- A *moving* standing-wave particle additionally sources
  g_tS (the conventional Poynting-flux cross-term, present for
  any moving mass), but no compact-direction-specific
  off-diagonal.
- The off-diagonal cross-terms that the per-component
  intermediate appears to require (g_tu, g_Su) cancel
  structurally in the standing-wave construction.
- The cancellation is the algebraic expression of the physical
  fact that a directionless standing wave has no preferred
  direction around the compact loop; there is no compact-direction
  current to source the corresponding cross-terms.

#### What this chapter does not establish

- Whether the project should commit to imposing Einstein's
  equations on M.
- The numerical magnitudes of the diagonal metric modifications
  (qualitative pattern only is given).
- The behavior of the system under full nonlinear GR or under
  quantization.
- Whether the per-component intermediate has any independent
  physical interpretation in this framework, or is purely a
  mathematical building block of the standing-wave particle.
- Whether the framework's "mass" reading and canonical KK's
  "charge" reading are different framings of the same physics
  — a separate framing question that the standing-wave reading
  does not resolve.
- Whether antimatter has any analog in this framework (the
  ±n distinction does not survive as a particle/antiparticle
  distinction under the standing-wave reading; what, if
  anything, plays the role of antimatter on this manifold is
  left open).

#### What this chapter leaves open for downstream chapters

- The standing-wave particle's *diagonal* metric modifications
  (g_tt, g_uu) are the gravitational signature taken up in
  Chapter 6.
- Chapter 7 examines the converse question: what a separately
  introduced metric shear γ would do to the ±n modes — useful
  as a "what if a sheared metric is given" study, independent
  of whether the particles themselves source it.

---

## What's next

For the next chapter and the rest of the project arc, see the
project [README's table of contents](README.md#chapters).
