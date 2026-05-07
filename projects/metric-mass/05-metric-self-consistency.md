# Chapter 5 — Self-consistency of the bare metric

[Chapter 1](01-foundation.md) posited a bare diagonal metric on M
as the *starting* condition, with the understanding (Chapter 1 §3)
that whether the metric stays diagonal is an open question. The
project's central question, stated then, was:

> When we put just light (no mass, no gravity, no charge) on the
> manifold M, do we expect off-diagonal entries of the metric to
> remain zero, or does something force them to develop?

The intervening chapters have produced the modes (Chapter 2),
examined them (Chapter 3), and characterized their behavior in
mode interactions (Chapter 4). This chapter turns to the metric
question. We compute the stress-energy of the wave field on the
bare metric, look at which entries are nonzero, and ask what that
implies for the metric.

The chapter does not predetermine the answer. We compute, report
what the math gives, and let the reader interpret. The
"must / can't / may / may not" question is answered by the math
case by case.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | Two senses of "self-consistent" |
| 2 | Stress-energy of a wave mode |
| 3 | Reading the cross-terms: what's nonzero, when |
| 4 | The chicken-and-egg problem |
| 5 | Back-reaction: what Einstein's equations would source |
| 6 | The Kaluza-Klein parallel |
| 7 | The ±n superposition: cross-term cancellation |
| 8 | Putting the chart together: must / can't / may / may not |
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

## 2. Stress-energy of a wave mode

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

## 5. Back-reaction: what Einstein's equations would source

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

The third point is the most novel. It says the bare metric of
Chapter 1 is consistent with no-field and with light, but is *not*
consistent with massive modes if Einstein's equations are
imposed: a g_tu cross-term must develop.

This answers the project's central question
([Chapter 1 §3](01-foundation.md)) for the case of mass on the
minimal manifold: **off-diagonals are forced** — specifically
g_tu, and additionally g_tS, g_Su when the mass is moving.

---

## 6. The Kaluza-Klein parallel

The structure of §5 lines up with standard Kaluza-Klein theory
in a specific and informative way.

In standard KK ([primers/kaluza-klein.md §5](../../primers/kaluza-klein.md)),
the off-diagonal metric component g_μ5 (mixing a 4D direction
with the compact 5th direction) is identified with the
electromagnetic potential A_μ. A particle with compact-direction
momentum p_w (interpreted in standard KK as electric charge)
sources A_μ via Einstein's equations, exactly as a charged
particle sources the electromagnetic field via Maxwell's
equations.

In our framework, compact-direction momentum is being
interpreted as **mass** (m = ℏ|n|/(R_u c)) rather than as
charge ([Chapter 2 §6](02-mass-from-u.md)). But the math of
§5 says that this compact-direction momentum *does* source the
analogous off-diagonal metric component g_tu (the "time"
component of the KK-style potential). The mechanism is the same;
only the interpretation has shifted.

This is one of those points where the project's choice of
interpretation has consequences worth flagging:

- *In standard KK*: ±n is charge sign, and ±n in superposition
  gives matter/antimatter cancellation of charge (g_t5 cancels
  for ±n superposition; Chapter 4 §3 noted the analog cross-
  check for our case).
- *In our framework*: ±n is read as a mass-direction handedness.
  The same cross-term g_tu cancels for ±n superposition (we
  compute this explicitly in §7 below). What standard KK would
  call "anti-matter cancels matter's charge" we are looking at
  as "anti-handed-mass cancels handed-mass's compact-direction
  flux."

Whether these are different framings of the same physics or
genuinely different physical readings is a question this
project cannot settle on its own. It is worth noting, though,
that the math doesn't distinguish: the same off-diagonal
sourcing mechanism is at play under both interpretations.

The project's choice to read compact-direction momentum as mass
(not charge) is a *framing* choice. If the framing turns out to
be incompatible with the off-diagonal structure that the math
requires — i.e., if the g_tu cross-term that mass sources is
*exactly* what standard physics calls electromagnetism — then
either (a) our framing is a notational rename of standard KK
with mass and charge swapped, or (b) the project's mass and
standard KK's charge are different concepts that happen to share
a sourcing mechanism. Distinguishing (a) from (b) is beyond this
chapter's scope.

### Looking ahead to Chapter 6 — this is more than a cross-check

What §5–§6 have constructed is more than a structural parallel
with KK. Compact-direction momentum sources off-diagonal metric
entries (§5); under the KK identification those entries are
gauge potentials A_μ (§6); a passing wave's worldline through
the perturbed metric picks up phase via the line integral
∮ A_μ dx^μ; that phase manifests as **trajectory deflection**
(gravitational lensing) and **coordinate-time slowdown**
(Shapiro delay) to a distant observer.

In other words: the chain compact momentum → off-diagonal
sourcing → KK gauge potential → phase holonomy on passing
worldlines is **a calculable mechanism for how mass bends
light**, internal to this framework. It is more granular than
standard GR's "mass curves spacetime; particles follow geodesics"
postulate, because each step admits an explicit calculation.
Chapter 6 §4 elevates this from cross-check to mechanism
candidate, alongside the entropic-gravity and GRID-substrate
mechanism programs.

---

## 7. The ±n superposition: cross-term cancellation

[Chapter 4](04-mode-interactions.md) examined the static
superposition of +n and −n at the same S. The energy was 2 m_n c²
(no cancellation at the diagonal level). Now we ask the
analogous question at the off-diagonal level.

For the superposition φ_+ + φ_-, where

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

Two cross-terms vanish in the superposition. The cancellation is
exact and is a direct consequence of T being bilinear in n: the
+n and −n contributions to entries linear in n have opposite
signs and cancel, while entries quadratic in n (like T_uu) have
the same sign and add.

So:

- **Diagonal entries (T_tt, T_SS, T_uu) double** in the
  superposition. Energy and pressure are additive, and the
  superposition has 2× the rest mass of a single component.
- **The "n-dependent" cross-terms (T_tu, T_Su) cancel** in the
  superposition. The off-diagonal entries that involve the
  compact-direction wavenumber linearly are exactly canceled
  when ±n are superposed.
- **The "n-independent" cross-term T_tS doubles**. The
  k_S-related cross-term has no n-dependence, so it is not
  affected by the ±n cancellation.

In particular, for a static ±n superposition (k_S = 0): all
off-diagonals cancel except none-that-survive (since T_tS = 0
when k_S = 0). The total stress-energy is purely diagonal:

<!-- For ±n at rest: T_μν = diag(4ω², 0, 4(n/R_u)²) -->
$$
T_{\mu\nu}^\text{static } \pm n = 2|\varphi|^2 \cdot \mathrm{diag}\bigl(2\omega^2,\; 0,\; 2(n/R_u)^2\bigr)
$$

(written here in matrix form with coordinate ordering (t, S, u);
the factor of 2 inside the diag comes from the doubled
contributions from ±n, and the prefactor 2|φ|² is the standard
stress-energy normalization).

#### Implication for the metric

Following §5: a static ±n superposition would source no
off-diagonal entries in g_μν. The metric modification it
produces, under linearized Einstein's equations, would be
*purely diagonal*. Specifically:

- g_tu cross-term: not sourced (cancelled by ±n).
- g_Su cross-term: not sourced.
- g_tS cross-term: not sourced (k_S = 0).
- Diagonal entries (g_tt, g_SS, g_uu) modified by 2× the rest
  energy density.

This is striking: the **static ±n superposition cancels
exactly the off-diagonals that a single mass mode would
source**. The diagonal energy density still doubles
([Chapter 4](04-mode-interactions.md) result), so total
gravitational coupling — measured by the diagonal stress-energy
trace — is doubled, not cancelled. But the off-diagonal
KK-style structures are cancelled cleanly.

The intuition that ±n superposition could "shield" something
([Chapter 4 §6](04-mode-interactions.md)) turns out to be
correct at the off-diagonal level: the cross-terms that
distinguish a mass-like configuration from a light-like one
(the "compact-direction couplings") *do* cancel in the
symmetric superposition. They do not cancel at the diagonal
level: the energy and rest mass still add.

---

## 8. Putting the chart together: must / can't / may / may not

The framing question — under what conditions must cross-terms
exist, can't exist, may exist, may not exist? — can now be
answered case by case from the math.

**Must cross-terms exist?**

The answer depends on the field configuration:

| Configuration | Cross-terms forced |
|---|---|
| No field (vacuum) | None must exist. Bare metric is consistent. |
| Light at rest | Degenerate (no field). None must exist. |
| Light moving | g_tS must exist (sourced by T_tS = −2ωk_S). |
| Mass at rest (single mode) | g_tu must exist (sourced by T_tu). g_tS and g_Su do not. |
| Mass at rest (±n superposition) | None must exist. ±n cancellation eliminates g_tu. |
| Mass moving (single mode) | g_tu, g_tS, g_Su all must exist. |
| Mass moving (±n superposition) | g_tS only must exist. g_tu and g_Su cancel. |

**Can't cross-terms exist?**

In vacuum, all cross-terms must be zero (no source for them).
The bare metric is uniquely consistent with vacuum.

For specific configurations, certain cross-terms cannot be
sourced. For instance, a single light mode (n = 0) cannot
source g_tu or g_Su, because both of those require n ≠ 0.

**May or may not?**

Beyond what the math of §§3, 5, 7 has settled, the residual
freedom is in the choice of:

- *Whether to impose Einstein's equations.* If Chapter 1's
  stance is maintained (no Einstein's equations), no
  cross-terms are forced regardless of T_μν — the metric is
  whatever we say. Cross-terms *may* exist by stipulation but
  are not forced.
- *What field configuration to consider.* The chart shows
  cross-term presence for various configurations; "may not"
  configurations (e.g., light only) keep the metric diagonal
  by construction.

So the answer to "must, can't, may, may not" is **all of
the above, depending on configuration**. Mass at rest (single
mode) forces g_tu. ±n superposition cancels it. Light alone
keeps the metric diagonal (with possibly g_tS for light
moving). Vacuum forces nothing.

The bare diagonal metric of Chapter 1 is therefore:

- **Self-consistent in vacuum and for light only.** No
  cross-terms forced.
- **Inconsistent under Einstein's equations whenever a single
  massive mode is present.** g_tu (at minimum) must develop.
- **Self-consistent again** for a static ±n superposition,
  where the ±n cancellation eliminates the g_tu source.

This is the structural answer the math gives.

#### Reading the result: the metric *is* the gravitational field

A natural interpretation worth making explicit: what the
chapter has shown is that **mass on M sources off-diagonal
metric components, and the off-diagonals (together with the
modifications to the diagonal entries) are the gravitational
field**. The g_tu component, in particular, is one piece of
the gravitational field that a mass at rest produces.

This lines up with how gravity works in standard general
relativity: the gravitational field *is* the metric, or more
precisely the deviation of the metric from a flat reference
([primers/metric.md §9](../../primers/metric.md)). A particle
of mass M sources a metric perturbation h_μν whose
non-trivial entries (in suitable coordinates) include both
diagonal modifications (the g_tt = −(1−2GM/(r c²)) factor
familiar from Schwarzschild) and, when motion or angular
momentum is involved, off-diagonals like the frame-dragging
g_tφ in Kerr. The "field" is the full deformation of g_μν
away from flat. There isn't a separate "gravitational field"
distinct from the metric — they are the same object.

In our framework, the g_tu component is the off-diagonal
piece of that deformation associated specifically with mass
at rest on a manifold with a compact dimension. Together with
the modifications to T_tt and T_uu (which would source g_tt
and g_uu modifications), it is the project's full
gravitational signature of mass on the minimal manifold.

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

A specific point of comparison with standard general relativity
is worth flagging. In standard 1+3D GR:

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

In our framework, the g_tu off-diagonal sourced by a *static*
mass at rest is structurally analogous to **Kerr's
frame-dragging g_tφ**, with two important wrinkles:

1. The compact direction u plays the role that φ plays in Kerr —
   it is the direction "around" which the dragging happens.
2. The mass is producing the off-diagonal even though it is
   *not rotating in the usual sense*. The role that φ-rotation
   plays in Kerr is played here by the wave's compact-direction
   *winding*, which is non-zero for any massive mode (n ≠ 0)
   at any state of motion, including rest. The winding is a
   kind of "intrinsic compact-direction angular momentum" that
   the wave carries by virtue of being massive.

So our minimal-manifold framework produces a *Kerr-like*
gravitational signature even for a non-rotating rest mass.
This is a non-trivial qualitative difference from standard
1+3D GR's static-mass result. Whether it is a deep feature of
the wave-realist mass picture, or a peculiarity of the 1+1+1D
manifold, is a question this project does not settle. It is
worth flagging for the future charge project (where standard
KK identifies the same g_μ5 entries as the EM potential, not
as gravitational frame-dragging — yet another instance of the
mass-vs-charge framing tension noted in §6 of this chapter).

#### Orbits and extended dimensions

The g_tu off-diagonal does not directly produce orbits. Orbits
in standard GR are extended-space trajectories driven by the
geodesic equation applied to the *diagonal* curvature of
spacetime; Schwarzschild gives orbits with no off-diagonals.

If the framework were extended to multiple S dimensions
(S_1, S_2, ... — beyond the scope of this project), localized
masses would source position-dependent diagonal modifications
g_tt(S), g_S_iS_i(S), and orbital trajectories would emerge
from those diagonal pieces in the standard GR way. The g_tu
off-diagonal is a compact-direction-specific feature
("frame-dragging in u") with no direct extended-space orbital
analog. It would coexist with the diagonal modifications that
produce orbits, but it would not contribute to them.

In other words: gravity on a multi-S manifold would still
produce orbits via the standard mechanism (diagonal curvature),
*and* would carry an additional compact-direction
off-diagonal (g_tu) signature for any masses present. The two
features live in independent components of the metric.

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

- Stress-energy of a single mode in the factored form
  T_μν = 2|φ|² k_μ k_ν, with k_μ = (−ω, k_S, n/R_u).
- Pattern of nonzero cross-terms in T_μν, by configuration:
  vacuum (none), light moving (T_tS only), mass at rest (T_tu
  only), mass moving (all three of T_tS, T_tu, T_Su).
- Pattern of off-diagonal entries that linearized Einstein's
  equations would source in the metric, mirroring T_μν.
- The ±n superposition: T_tu and T_Su cancel exactly; T_tt,
  T_SS, T_uu, T_tS double.

#### What this chapter establishes

- The bare diagonal metric of Chapter 1 is self-consistent in
  vacuum.
- Under Einstein's equations, the bare metric is *not*
  self-consistent in the presence of a single massive mode:
  g_tu must develop.
- The static ±n superposition cancels the g_tu source: under
  this configuration, the bare diagonal metric remains
  self-consistent at the off-diagonal level (though its
  diagonal entries would still be modified by the doubled
  energy density).
- The off-diagonal sourcing parallels standard Kaluza-Klein
  theory, where compact-direction momentum sources off-diagonal
  metric entries.

#### What this chapter does not establish

- Whether the project should commit to imposing Einstein's
  equations on M.
- The numerical magnitudes of the metric modifications
  (qualitative pattern only is given).
- The behavior of the system under full nonlinear GR or under
  quantization.
- Whether our project's "mass" interpretation and standard KK's
  "charge" interpretation are different framings of the same
  physics.

#### What this chapter leaves open for downstream chapters

- *If the diagonal metric is to remain*: the project would
  need to either decline to impose Einstein's equations, or
  restrict to ±n-symmetric field configurations where the
  off-diagonals cancel.
- *If the metric is to develop g_tu in response to mass*: the
  consequences for the mode structure (does the wave equation
  on the corrected metric still have the same mode spectrum?
  do new effects appear?) are downstream questions for
  chapters 7 and beyond.
- *The Kaluza-Klein parallel*: whether to engage seriously
  with the question of whether our "mass" framing is a
  rename of standard KK's "charge" framing is a project-level
  question worth flagging for follow-up work.

---

## What's next

For the next chapter and the rest of the project arc, see the
project [README's table of contents](README.md#chapters).
