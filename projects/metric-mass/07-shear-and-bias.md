# Chapter 7 — Off-diagonal shear and the breaking of ±n degeneracy

The ±n distinction has been examined repeatedly:

- [Chapter 3 §3](03-examining-the-modes.md) noted that ±n are
  linearly independent solutions of the wave equation but mass
  is symmetric in n (m = ℏ|n|/(R_u c)).
- [Chapter 4](04-mode-interactions.md) showed that for
  interactions in the bare diagonal metric, the ±n distinction
  is subtle: rest energies double in superposition, off-diagonal
  stress-energies cancel.
- [Chapter 5](05-metric-self-consistency.md) showed that mass
  *sources* off-diagonal metric entries when present, but the
  ±n superposition cancels the n-linear ones.
- [Chapter 6](06-gravitational-bending.md) showed that
  gravitational coupling is set by the (doubled) diagonal
  energy, so cancellation does not extend there.

What every previous chapter assumed is that the metric started
diagonal. This chapter asks the converse question: *given* an
off-diagonal entry in the metric, what does it do to the ±n
modes? In particular, can it lift the degeneracy and bias the
manifold toward one sign of n over the other?

The chapter is discovery-driven. We do not assert that the real
world has a shear; we compute what a shear would *do* and let
the implications follow. As will turn out, the answer is more
subtle than the outline of this question would suggest: shear
*does* lift the ±n degeneracy in a specific structural sense,
but pure thermal equilibrium does not produce net population
asymmetry. The chapter unpacks both halves of that result
carefully.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The setup: introduce a g_Su shear into the metric |
| 2 | The dispersion relation in the sheared metric |
| 3 | At rest: ±n unchanged |
| 4 | Moving: the dispersion splits |
| 5 | The Kaluza-Klein parallel: shear as a "vector potential" |
| 6 | Thermal ensembles and the (k_S, n) → (−k_S, −n) symmetry |
| 7 | The real-world matter/antimatter question |
| 8 | Where the shear could come from |
| 9 | What this chapter does and does not establish |
| 10 | End of Chapter 7 |

---

## 1. The setup

Modify Chapter 1's bare metric by adding a single off-diagonal
entry g_Su = γ. The modified metric, with coordinates ordered
(t, S, u):

<!-- g = | -c² 0 0 ; 0 1 γ ; 0 γ 1 | -->
$$
g_{\mu\nu}
= \begin{pmatrix}
   -c^2 & 0 & 0 \\
   0 & 1 & \gamma \\
   0 & \gamma & 1
  \end{pmatrix}
$$

The shear γ is a dimensionless parameter. Note carefully what is
*not* assumed here:

- We do not derive γ from anything. It is introduced as a
  parameter to study its consequences.
- We do not assert that γ ≠ 0 in any physical situation. The
  question of whether γ should be nonzero is deferred to §8,
  where we look at possible sources.
- We restrict to |γ| < 1 throughout, so that the metric remains
  Lorentzian (the (S, u) submatrix has positive determinant
  1 − γ² and the t-eigenvalue is the only negative one). At
  |γ| = 1 the metric becomes degenerate; at |γ| > 1 the
  signature changes and the construction loses its physical
  interpretation.

The inverse metric is needed for the wave equation. Inverting the
2×2 (S, u) submatrix:

<!-- (S, u) inverse = (1/(1-γ²)) | 1 -γ ; -γ 1 | -->
$$
\begin{pmatrix} 1 & \gamma \\ \gamma & 1 \end{pmatrix}^{-1}
= \frac{1}{1-\gamma^2}\begin{pmatrix} 1 & -\gamma \\ -\gamma & 1 \end{pmatrix}
$$

So the full inverse metric is:

<!-- g^μν entries -->
$$
g^{tt} = -\frac{1}{c^2},
\qquad
g^{SS} = g^{uu} = \frac{1}{1-\gamma^2},
\qquad
g^{Su} = g^{uS} = -\frac{\gamma}{1-\gamma^2}
$$

The diagonal entries g^SS and g^uu are rescaled by 1/(1−γ²);
the off-diagonal entry g^Su is sourced by the shear directly.
For γ → 0, the inverse metric reduces to diag(−1/c², 1, 1) — the
inverse of the bare diagonal metric of Chapter 1, as it should.

---

## 2. The dispersion relation in the sheared metric

The wave equation □φ = 0 in the modified metric is g^μν ∂_μ ∂_ν φ
= 0. For a single mode φ = exp(i(k_S S − ωt + nu/R_u)) with
covector k_μ = (−ω, k_S, n/R_u), the equation reduces to

<!-- g^μν k_μ k_ν = 0 -->
$$
g^{\mu\nu}\,k_\mu\,k_\nu = 0
$$

Substituting the inverse metric components:

<!-- expanded -->
$$
-\frac{\omega^2}{c^2}
\;+\; \frac{k_S^2}{1-\gamma^2}
\;+\; \frac{(n/R_u)^2}{1-\gamma^2}
\;-\; \frac{2\,\gamma\,k_S\,(n/R_u)}{1-\gamma^2}
= 0
$$

Solving for ω²:

<!-- ω²/c² = (k_S² + (n/R_u)² - 2γ k_S (n/R_u)) / (1 - γ²) -->
$$
\boxed{\;
\frac{\omega^2}{c^2}
\;=\; \frac{k_S^2 \;+\; (n/R_u)^2 \;-\; 2\,\gamma\,k_S\,(n/R_u)}{1 - \gamma^2}
\;}
$$

This is the dispersion relation in the sheared metric.

The cross-term `2γ k_S (n/R_u)` is **linear in n**. This is the
key structural fact: the dispersion is no longer n²-symmetric —
swapping n → −n no longer leaves ω unchanged at fixed k_S.

#### A useful rewriting: the shifted parabola

The dispersion relation can be cleaned up by completing the square
in k_S. Define a shifted wavenumber:

<!-- k'_S = k_S - γ n / R_u -->
$$
k'_S \;\equiv\; k_S \;-\; \frac{\gamma\,n}{R_u}
$$

Then the numerator of the dispersion relation becomes

<!-- (k_S - γ n/R_u)² + (n/R_u)²(1-γ²) -->
$$
k_S^2 + (n/R_u)^2 - 2\gamma k_S (n/R_u)
\;=\; (k'_S)^2 \;+\; (n/R_u)^2\,(1-\gamma^2)
$$

(an algebraic identity), and the dispersion relation simplifies
to:

<!-- ω² = c² (k'_S)² / (1-γ²) + c² (n/R_u)² -->
$$
\omega^2
\;=\; \frac{c^2\,(k'_S)^2}{1-\gamma^2}
\;+\; c^2\,(n/R_u)^2
$$

Reading the simplified form:

- For each fixed n, the dispersion is a parabola in k_S, just as
  in the unsheared case — but the parabola's *minimum* sits at
  k_S = γn/R_u, not at k_S = 0.
- For +n the minimum is shifted to *positive* k_S; for −n the
  minimum is shifted to *negative* k_S. The two parabolas have
  their minima *oppositely shifted*.
- At the minimum, ω² = c²(n/R_u)², so ω_min = c|n|/R_u,
  independent of γ. The lowest energy a mode of given n can
  have is unchanged by the shear; only its *location in k_S* is
  shifted.

This shifted-parabola form makes the rest of the chapter's
analysis cleaner.

---

## 3. At rest: ±n unchanged

The "rest" condition in the lab frame is k_S = 0. Substituting
into the dispersion relation:

<!-- at k_S = 0 -->
$$
\frac{\omega^2}{c^2}
\;=\; \frac{(n/R_u)^2}{1-\gamma^2}
\qquad\Longrightarrow\qquad
\omega_\text{rest}
\;=\; \frac{c\,|n|}{R_u\,\sqrt{1-\gamma^2}}
$$

The rest frequency is the same for +n and −n; it depends only on
|n|. So the rest-mass formula picks up a γ-dependent factor but
remains symmetric in the sign of n:

<!-- m_n = ℏ |n| / (R_u c √(1-γ²)) -->
$$
m_n \;=\; \frac{\hbar\,|n|}{R_u\,c\,\sqrt{1-\gamma^2}}
$$

The conclusion is direct: **shear does not break the ±n
rest-mass degeneracy**. A particle at rest in the lab frame
sees no asymmetric energy from γ. The 1/√(1−γ²) factor is
present, but it acts on +n and −n identically.

A subtle observation worth noting: rest in the lab frame
(k_S = 0) is *not* the same as the minimum-energy state of the
mode for γ ≠ 0. The minimum-energy state, per §2, sits at the
shifted wavenumber k_S = γn/R_u, where ω = c|n|/R_u. So a +n
mode has its minimum-energy state at k_S > 0, and a −n mode has
its minimum-energy state at k_S < 0 (assuming γ > 0). At the
lab-frame rest position k_S = 0, the mode is *above* its
minimum energy by the factor 1/√(1−γ²) − 1; it is not the
ground state of the n-th branch in the shifted-parabola sense.

This will matter in §6 when we consider thermal occupations.

---

## 4. Moving: the dispersion splits

For k_S ≠ 0, the n-linear cross-term in the dispersion produces
different ω values for +n and −n at the same k_S. Write out
both:

<!-- ω_+² and ω_-² -->
$$
\frac{\omega_+^2}{c^2}
\;=\; \frac{k_S^2 + (n/R_u)^2 - 2\gamma\,k_S\,(n/R_u)}{1-\gamma^2}
$$

$$
\frac{\omega_-^2}{c^2}
\;=\; \frac{k_S^2 + (n/R_u)^2 + 2\gamma\,k_S\,(n/R_u)}{1-\gamma^2}
$$

(The −n branch has the cross-term sign flipped relative to +n
because the cross-term is linear in n.) Subtracting:

<!-- ω_+² - ω_-² = -4γ c² k_S (n/R_u) / (1-γ²) -->
$$
\omega_+^2 - \omega_-^2
\;=\; \frac{-4\,\gamma\,c^2\,k_S\,(n/R_u)}{1-\gamma^2}
$$

The two branches have different ω at the same k_S — a moving +n
and a moving −n with the same lab-frame momentum no longer have
the same energy.

The splitting has three structural features worth recording:

1. **It vanishes at k_S = 0.** The rest case is symmetric (§3);
   the splitting only appears for moving modes.
2. **It is direction-dependent.** The sign of ω_+² − ω_-²
   depends on sign(γ k_S n). Reversing the direction of motion
   (k_S → −k_S) flips the sign of the splitting. There is no
   absolute statement that "+n is always lower energy than −n"
   — the asymmetry depends on direction.
3. **It scales linearly with γ at small γ.** For small shear,
   the splitting is proportional to γ; for γ → 0 the dispersion
   collapses to the ±n-symmetric form of Chapter 2.

The (k_S, ω) plot of the n=±1 branches in the sheared metric
shows two parabolas with minima oppositely shifted in k_S: the
+n parabola has its bottom at k_S = +γ/R_u; the −n parabola
has its bottom at k_S = −γ/R_u. The two parabolas are
*reflections of each other* across the k_S = 0 axis. They cross
at k_S = 0, where they meet at the common rest energy
c|n|/(R_u √(1−γ²)).

This crossing is geometrically meaningful: the ±n branches are
related by a *symmetry* — reflection across k_S = 0 combined
with sign flip of n. We make this symmetry explicit in §6.

---

## 5. The Kaluza-Klein parallel

The structural similarity to standard Kaluza-Klein
([primers/kaluza-klein.md §5](../../primers/kaluza-klein.md))
is exact: in standard KK, off-diagonal g_μ5 = A_μ couples to
compact-direction momentum (interpreted there as charge) to
produce the Lorentz force. The dispersion of a charged particle
in an electromagnetic potential is split by exactly the
mechanism we have computed: a cross-term linear in the charge
sign that shifts the parabola's minimum oppositely for ±q
modes.

In our framework, the off-diagonal g_Su plays the role that
g_μ5 plays in standard KK. The compact-direction momentum that
in standard KK is charge is in this project being read as
mass-handedness ([Chapter 2 §6](02-mass-from-u.md)). The
shear-induced dispersion splitting is *the Lorentz-force
mechanism, recast in mass-mode language*.

This sharpens the framing tension the project has been carrying.
Standard KK reads:

- Off-diagonal g_μ5 ↔ EM potential A_μ
- Compact momentum ↔ charge
- Lorentz force on charge in EM field ↔ shear-induced dispersion
  shift on compact-momentum modes

This project's mass-only reading reframes this as:

- Off-diagonal g_Su ↔ a "mass-handedness coupling" (no
  conventional name)
- Compact momentum ↔ mass-handedness sign
- Shear-induced dispersion shift on ±n modes ↔ dynamical
  signature of mass-handedness

Whether these are different framings of the same physics, or
different physics with the same mathematical skeleton, is a
question the present project cannot settle. It is, however,
explicitly the question the future
[charge project](../metric-charge/) will need to engage:
once both compact directions are present, the mass-vs-charge
framing of compact momentum becomes a real choice with
testable consequences (or, alternatively, a relabeling with no
content). For Chapter 7's purposes, we observe the parallel and
record it.

---

## 6. Thermal ensembles and the (k_S, n) → (−k_S, −n) symmetry

A single mode moving through a sheared region experiences a
direction-dependent dispersion shift (§4). The natural
follow-up question — *can shear bias an ensemble of modes
toward one sign of n over the other?* — turns out to have a
more subtle answer than the §4 result alone suggests.

#### The exact symmetry

Look at how the dispersion transforms under the simultaneous
flip (k_S, n) → (−k_S, −n):

<!-- under (k_S → -k_S, n → -n): -->
$$
\omega^2(-k_S, -n)
\;=\; \frac{c^2 \bigl[k_S^2 + (n/R_u)^2 - 2\gamma\,(-k_S)(-n/R_u)\bigr]}{1-\gamma^2}
\;=\; \omega^2(k_S, n)
$$

The cross-term picks up two minus signs (one from each flip)
and is unchanged. So:

<!-- ω(k_S, n) = ω(-k_S, -n) -->
$$
\omega(k_S, n) \;=\; \omega(-k_S, -n)
$$

This is an **exact symmetry of the sheared dispersion**. For
every (+n, +k_S) mode there is a (−n, −k_S) mode at the same
energy. The (k_S, n) → (−k_S, −n) symmetry is preserved by the
shear; the cross-term `2γ k_S (n/R_u)` is invariant under it.

#### What thermal equilibrium gives

In thermal equilibrium, mode populations are weighted by
exp(−ω/kT) (or its quantum analog; the symmetry argument is
the same in either case). Compute the total population of +n
modes by integrating over all k_S:

<!-- N_{+n}(T) = ∫ dk_S exp(-ω(k_S, +n)/kT) -->
$$
N_{+n}(T) \;=\; \int dk_S \;\exp\!\bigl(-\omega(k_S, +n)/kT\bigr)
$$

And the analogous total for −n. By the symmetry just derived,

<!-- N_{-n} = N_{+n} -->
$$
N_{-n}(T)
\;=\; \int dk_S \;\exp\!\bigl(-\omega(k_S, -n)/kT\bigr)
\;=\; \int dk_S \;\exp\!\bigl(-\omega(-k_S, +n)/kT\bigr)
\;=\; \int dk'_S \;\exp\!\bigl(-\omega(k'_S, +n)/kT\bigr)
\;=\; N_{+n}(T)
$$

(the change of integration variable k'_S = −k_S leaves the
limits invariant since both run over all of ℝ). So:

<!-- result: total +n population equals total -n population -->
$$
N_{+n}(T) \;=\; N_{-n}(T)
$$

**Pure thermal equilibrium with shear does not bias the total
±n populations.** The (k_S, n) → (−k_S, −n) symmetry pairs
+n modes at +k_S with −n modes at −k_S, and the thermal
weighting respects this pairing.

#### What thermal equilibrium does give

Although total counts are equal, momentum-resolved counts are
not. At a fixed lab-frame momentum k_S = k₀ (with k₀ ≠ 0):

<!-- relative density at fixed k_S -->
$$
\frac{n_{+n}(k_0, T)}{n_{-n}(k_0, T)}
\;=\; \exp\!\bigl((\omega_- - \omega_+)/kT\bigr) \neq 1
$$

For γ > 0 and k₀ > 0, n > 0: ω_+ < ω_- so the ratio is greater
than 1 — more +n than −n at that momentum. At k_S = −k₀ the
ratio inverts: more −n than +n. The two effects exactly cancel
in the integral over all k_S.

So thermal equilibrium with shear produces a **correlation**
between the sign of n and the direction of motion, but no net
imbalance in particle counts. The framework, viewed through the
lens of thermal statistics alone, has the property: for every
+n mode moving in +S there is a −n mode moving in −S; both are
equally populated; the total counts of ±n are equal.

#### The deeper structural fact

The (k_S, n) → (−k_S, −n) symmetry is the framework's analog
of CPT — a discrete symmetry that pairs particles with
antiparticles. CPT is exact in standard quantum field theory
under very general assumptions. In our framework, the symmetry
of the sheared dispersion under the combined flip is the
classical wave-mechanical version of the same statement.

Pure CPT-respecting dynamics cannot produce net particle/
antiparticle asymmetry from a CPT-symmetric initial state.
This is the well-known reason that real-world baryogenesis
requires *more* than just a thermal soup with some
CP-violation:

- A pure CP-symmetric, thermally equilibrated system stays at
  zero net baryon number forever.
- CP-violation alone does not break CPT; it reduces CPT to a
  weaker symmetry but still excludes net asymmetry from
  equilibrium.
- The Sakharov conditions specifically include
  *out-of-equilibrium dynamics* to break the symmetry-protected
  zero-asymmetry result.

So our framework, with shear γ alone, gives CPT-respecting
dynamics. Shear lifts the ±n degeneracy in a *direction-
dependent* sense (different energies at the same lab-frame
k_S), but the underlying symmetry forbids net population
asymmetry in equilibrium.

The chapter's central observation, corrected:

> Shear alone is **necessary** for ±n distinguishability in
> dynamics — it makes ±n modes locally distinguishable through
> their dispersion. Shear alone is **not sufficient** for net
> ±n biasing; producing that requires breaking the (k_S, n) →
> (−k_S, −n) symmetry through additional structure, most
> naturally via out-of-equilibrium dynamics.

---

## 7. The real-world matter/antimatter question

Standard physics treats matter/antimatter asymmetry
("baryogenesis") as an open problem. A small primordial
asymmetry (~10⁻⁹, the baryon-to-photon ratio) developed in the
early universe and produced today's matter-dominated cosmos.
Mechanisms in the literature (Sakharov conditions, GUT
baryogenesis, electroweak baryogenesis, leptogenesis) all
combine three ingredients identified by Sakharov in 1967:

1. Baryon-number violation (some process that creates baryons
   without creating antibaryons in equal number).
2. C and CP violation (dynamics that distinguishes between
   matter and antimatter).
3. Out-of-equilibrium evolution (departure from thermal
   equilibrium during the relevant epoch).

All three are required because, as §6 reminded us, equilibrium
dynamics that respects the underlying symmetries cannot generate
net asymmetry from a symmetric initial state.

In our framework, off-diagonal shear γ contributes to the
*second* Sakharov condition: it provides a CP-violation analog
(distinct dynamics for ±n modes at the same momentum). It does
*not* on its own provide the third condition (out-of-equilibrium
evolution); for that, the framework would need either a
dynamical γ that evolves with cosmic time, an expanding
manifold, or some other source of equilibrium-breaking.

What this project's framework therefore offers, to the
real-world matter-antimatter question, is **a candidate
mechanism for the CP-violation ingredient**, not a complete
account of baryogenesis. A primordial g_Su shear in the early
universe's geometry would establish the local
distinguishability of ±n modes; combined with an
out-of-equilibrium epoch (cosmic expansion, phase transitions,
or other), it would in principle produce a small net imbalance
that becomes today's matter dominance.

The status of this contribution is narrow but real:

- *It is not a complete baryogenesis mechanism.* The framework
  alone does not produce net asymmetry; it provides one of
  three required ingredients.
- *It is also not nothing.* Identifying a geometric source
  for CP-violation analogs is a non-trivial finding from the
  framework's own machinery.
- *It does not assert that γ ≠ 0 in the real world.* The
  empirical question of whether the universe carries such a
  shear is not addressed here.

Settling whether shear is the actually-realized CP-violation
ingredient (vs Sakharov-style mechanisms in the standard
model) would require empirical signatures this project is not
in a position to identify.

---

## 8. Where the shear could come from

Within the framework, the question of *why* γ takes whatever
value it does cannot be answered: γ is a parameter, not a
derived quantity. But it is worth cataloging the kinds of
explanations that could be available.

#### Physics-internal candidate sources

- **Primordial geometric structure.** The manifold M might
  have inherited a small g_Su term from its initial conditions
  — i.e., the early universe started with this off-diagonal
  geometric component already present. This is the simplest
  hypothesis but it pushes the explanation onto initial
  conditions.
- **Sourced by an early matter-imbalanced state.** Per
  [Chapter 5](05-metric-self-consistency.md), mass-moving
  modes source g_Su via T_Su = 2 k_S (n/R_u) |φ|². An early
  universe with a small momentum or n imbalance could have
  sourced its own asymmetric shear, which then biased
  subsequent equilibration. This is a self-consistent
  bootstrapping picture but still requires the original
  imbalance to come from somewhere.
- **Coupling to other fields.** If the framework later admits
  additional fields (charge, second compact direction), shear
  might be sourced or stabilized by those fields. The future
  charge project might provide a natural mechanism.

#### Meta-level explanations

The above are physics-internal candidate mechanisms — sources
within the manifold's own dynamics or initial-condition
specification. There is also a meta-level layer of explanation
worth flagging: any specific value of γ has to come from
*somewhere*, and the question of why the universe's geometry
takes the values it does spans a wider explanatory range than
physics-internal mechanisms alone.

- **Anthropic / multiverse selection.** If many manifolds with
  different γ exist, observers necessarily find themselves in
  ones whose γ supports their existence. The selection effect
  picks values without identifying a generating mechanism.
- **Fundamental "just is."** Some parameters of nature may
  simply be brute facts with no deeper explanation —
  fundamental constants in the same sense that the speed of
  light is a fundamental constant. A primordial γ would, on
  this reading, be a similar irreducible parameter of the
  universe.
- **Designer-set / intelligent design.** The geometry of the
  manifold could be specified by a non-physical first cause —
  an intelligence, a deity, or any other agency standing
  outside the physics-internal causal chain. This explanation
  lies outside the scope of empirical physics and therefore
  outside the methods this project uses, but it is a
  consistent meta-level position about *why* the geometry is
  what it is. Including it here is acknowledging the
  explanatory spectrum, not endorsing any particular position.

The chapter does not commit to any of these — physics-internal
or meta-level. It notes them as the range of possibilities
follow-up work or independent inquiry might engage. The
project's contribution is identifying the *mechanism* by which
shear, once present (from any source), produces the
direction-dependent ±n distinguishability of §§4–6. Whether
the source is ultimately a physical process, a selection
effect, a brute fact, or an external act of specification is a
question different methods are needed to address.

---

## 9. What this chapter does and does not establish

#### Established

- Adding a g_Su shear γ to the bare metric modifies the wave
  equation and the dispersion relation in a specific way:
  the n-linear cross-term `2γ k_S (n/R_u)` enters, breaking
  the n²-symmetry that the bare diagonal metric had.
- At rest (k_S = 0), the ±n modes are unchanged in the sense
  that their rest energies are equal: rest mass picks up a
  γ-dependent factor of 1/√(1−γ²) but remains symmetric in n.
- For moving modes (k_S ≠ 0), the dispersion of +n and −n
  splits: at the same lab-frame k_S, ±n have different
  energies. The splitting is direction-dependent (it flips
  sign with k_S → −k_S).
- The (k_S, n) → (−k_S, −n) symmetry is *exact* in the
  sheared dispersion. This is the framework's analog of CPT
  and protects total ±n populations against bias in
  equilibrium.
- Pure thermal equilibrium with shear produces a
  *direction-correlated* asymmetry (more +n than −n at given
  +k_S; the reverse at −k_S) but **zero net asymmetry in
  total ±n counts**.
- The framework therefore provides one of the three Sakharov
  ingredients (CP-violation analog) but not the others
  (baryon-number violation, out-of-equilibrium dynamics).

#### Not established

- That γ ≠ 0 in the real world.
- That this mechanism is sufficient on its own to produce the
  observed real-world matter/antimatter asymmetry.
- The numerical magnitude of γ that would be required to play
  the CP-violation role in any concrete baryogenesis scenario.
- Whether γ is itself a dynamical field or a fixed background
  parameter.

#### What this leaves open

- The dynamics of γ. If γ has its own equation of motion
  rather than being a fixed parameter, the cosmological story
  of how shear evolves over time, dissipates, or persists to
  today becomes a follow-on question. The
  [cosmological project](README.md#what-this-project-leaves-to-follow-up-projects)
  is the natural home for it.
- Whether the bias is observable independently of mass — for
  example, effects on light propagating through sheared
  regions. The current chapter has focused on massive modes;
  whether n = 0 modes (light) experience any γ-induced
  effects is a separate question.
- The relationship between this CP-violation analog and the
  Standard Model's CP-violating sector. Whether the framework
  can host a quantitative match to observed CP-violation
  parameters is unsettled.

---

## 10. End of Chapter 7

The chapter examined what happens when a single off-diagonal
metric entry, g_Su = γ, is introduced to the bare manifold. The
math gave a clean and somewhat-corrective answer.

What shear *does*: lifts the ±n degeneracy in a
direction-dependent way. At fixed lab-frame momentum, +n and
−n modes have different energies. At rest, they don't. The
mechanism is the n-linear cross-term in the dispersion relation,
which shifts the +n and −n parabolas oppositely in k_S. This is
the standard KK Lorentz-force coupling, recast for our
mass-only framing.

What shear *does not* do: produce net population asymmetry of
±n in thermal equilibrium. The (k_S, n) → (−k_S, −n) symmetry
of the sheared dispersion is exact, and this protects total
±n counts from being biased by thermal weights. The
direction-correlated asymmetry exists at fixed momentum but
cancels under integration over all k_S.

The implication for the real-world matter/antimatter question
is correspondingly narrow: the framework supplies *one* of the
three Sakharov conditions (a CP-violation analog) when γ ≠ 0,
but does not supply the others (baryon-number violation,
out-of-equilibrium dynamics). A complete baryogenesis story
in this framework would require a dynamical γ or another
source of out-of-equilibrium evolution.

The closing summary [Chapter 8](08-closing-summary.md)
consolidates this and the rest of the project's findings.

---

## What's next

For the next chapter and the rest of the project arc, see the
project [README's table of contents](README.md#chapters).
