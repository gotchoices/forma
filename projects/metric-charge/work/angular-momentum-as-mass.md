# Standing-wave angular momentum as the source of rest mass

**Status:** Exploratory. Not chapter-grade. See
[work/README.md](README.md) for context.

## Scope

Test the framing:

> Rest mass is, physically, the quantized angular momentum of a
> standing wave around a compact loop, viewed from extended
> spacetime as inertia.

If the identification is correct and useful, decide where it should
be stated explicitly: as a back-edit to metric-mass, as part of the
existing metric-mass Ch 9 HO bridge, as part of the prospective
metric-charge HO bridge, or in more than one of those places.

This is a *reframing* of existing derivations, not new physics.

## The identification

The Ch 2 mode profile around the compact direction u is
U_n(u) = e^{i n u / R_u}, with quantized wavenumber k_u = n/R_u.
Associated linear momentum (tangent to the loop):

<!-- p_u = ℏ k_u = ℏ n / R_u -->
$$
p_u \;=\; \hbar\,k_u \;=\; \hbar\,\frac{n}{R_u}
$$

If u is read as an angle around the compact loop (u = R_u θ with
θ ∈ [0, 2π)), then p_u is the linear momentum tangent to the loop
and the **angular momentum about the loop's center** is:

<!-- J_u = R_u · p_u = R_u · (ℏ n / R_u) = ℏ n -->
$$
J_u \;=\; R_u \cdot p_u \;=\; R_u \cdot \frac{\hbar\,n}{R_u} \;=\; \hbar\,n
$$

— a quantized integer angular momentum in units of ℏ. Same form as
the orbital angular momentum spectrum of standard quantum mechanics,
but here arising from the *periodicity* of the compact direction
rather than from the angular-momentum eigenvalue problem in 3D
extended space.

**Symbol convention.** **J_u** is used for the angular momentum
about the loop, distinct from **L_u** = 2π R_u, which is the
compact circumference (a metric parameter used throughout
metric-charge). Where confusion is possible, J denotes angular
momentum and L denotes a length.

**Embedding caveat.** The phrase "angular momentum about the loop's
center" requires the compact direction to be embedded in a plane
with a definite rotation axis. The abstract S¹ (the quotient of ℝ
by L_u) does not by itself supply such a center. What *is*
embedding-independent is that n is the eigenvalue of the translation
generator P̂_u = −iℏ ∂/∂u acting on e^{i n u / R_u}, and that the
mass identification m_n = ℏ|n|/(R_u c) uses only |n|. The
"angular momentum" *labelling* of n adds physical intuition under a
natural embedding (the standard rolled-up cylinder picture) but is
not load-bearing for the mass identification.

The metric-mass rest-mass identification

<!-- m_n = ℏ |n| / (R_u c) -->
$$
m_n \;=\; \frac{\hbar\,|n|}{R_u\,c}
$$

rearranged:

<!-- m_n · R_u · c = ℏ |n| = |J_u| -->
$$
m_n \cdot R_u \cdot c \;=\; \hbar\,|n| \;=\; |J_u|
$$

— **rest mass × compact radius × c = angular momentum about the
loop**.

Two frequencies show up in the wave on the loop. They give the
same rest energy but mean different things, and conflating them is
easy:

| Frequency | Formula | Meaning |
|---|---|---|
| ω_rot | c / R_u (independent of n) | The angular rate at which a massless wave goes once around the loop |
| ω_n | \|n\| c / R_u (scales with n) | The temporal oscillation rate at a fixed point on the loop |

The two are related by ω_n = |n| · ω_rot.

Each gives the rest energy through its own identity:

- **Rotor identity (E = J · ω_rot).** The massless-on-a-ring
  result E = pc, applied around the loop with p = J/R, gives

<!-- m_n c² = |J_u| · ω_rot = |n| ℏ · (c / R_u) -->
$$
m_n\,c^2 \;=\; |J_u| \cdot \omega_{\text{rot}}
\;=\; |n|\,\hbar \cdot \frac{c}{R_u}
$$

  *Not* the non-relativistic rotor identity E = ½Jω, which the
  form E = J·ω might otherwise suggest — the factor of ½ does not
  appear here because the wave is massless and relativistic.

- **Planck–Einstein identity (E = ℏω_n).** The standard
  identification of energy with temporal oscillation frequency
  gives

<!-- m_n c² = ℏ ω_n -->
$$
m_n\,c^2 \;=\; \hbar\,\omega_n
$$

Both are correct and equivalent; they just emphasize different
features of the same wave (geometric rotation vs. temporal
oscillation).

## Physical reading

From inside the loop: a wave wraps around the compact direction with
phase advancing by 2πn per circuit and angular momentum J_u = ℏn
about the loop's center (under the natural embedding).

From outside (in extended spacetime t, S): the loop is too small to
be resolved. The angular momentum is not observable as such — it
appears only as the *energy* of the rotation, which by relativistic
mass-energy equivalence appears as rest mass m_n = E_n / c².

The compact-direction angular momentum is **hidden from extended
spacetime, but its energy contribution is not**. That energy is
exactly the rest mass.

## Connection to the Compton scale

Metric-mass [Ch 2 §6](../../metric-mass/02-mass-from-u.md) already
notes that R_u = ℏ/(m_1 c) is the **reduced** Compton wavelength
λ̄ = ℏ/(mc) of the n = 1 particle (distinct from the full Compton
wavelength λ = h/(mc) = 2π λ̄), and connects this to Schrödinger's
*zitterbewegung*. The angular-momentum reading **re-states** the
connection:

> **A particle's reduced Compton wavelength is the radius at which
> one quantum of orbital angular momentum produces the particle's
> rest energy.**

This is tautologically equivalent to the n = 1 mass formula
m_1 = ℏ/(R_u c) — it adds no derivational content. Its value is
purely interpretive: the Compton scale gets a one-line physical
reading instead of appearing only as the algebraic relation between
R_u and m_1.

## Extension to 2D

On a 2D compact sheet (metric-charge), each direction carries its
own linear compact momentum (and a corresponding angular momentum
under the natural embedding, with the same caveat as in the 1D
case):

<!-- p_u = ℏn / R_u,  p_w = ℏm / R_w;  J_u = ℏn,  J_w = ℏm -->
$$
p_u \;=\; \frac{\hbar\,n}{R_u},
\quad
p_w \;=\; \frac{\hbar\,m}{R_w};
\qquad
J_u \;=\; \hbar\,n,
\quad
J_w \;=\; \hbar\,m
$$

The [Ch 2 §3](../02-modes-on-a-sheet.md) Pythagorean mass formula
combines the two **compact linear momenta** in quadrature:

<!-- (m · c)² = p_u² + p_w² = (ℏn/R_u)² + (ℏm/R_w)² -->
$$
(m_{(m,n)}\,c)^2
\;=\; p_u^2 + p_w^2
\;=\; \left(\frac{\hbar\,n}{R_u}\right)^2
   + \left(\frac{\hbar\,m}{R_w}\right)^2
$$

— this is the standard relativistic E² = (**p** c)² + (m c²)²
applied at p_S = 0 with a 2-component compact momentum (p_u, p_w).
It is **not** a relativistic combination of two separate systems'
energies (which does not combine Pythagoreanly).

The quadrature uses **p_i = J_i / R_i**, not J_i itself. When the
two radii differ (R_u ≠ R_w, the generic anisotropic case the work
folder commits to in [ho-bridge-2d.md](ho-bridge-2d.md) §"Symmetry
payoffs"), angular momenta on different-radius loops carry
different "weight" per unit J — the combination is not (J_u, J_w)
read as a 2-vector. Only at the **isotropic point R_u = R_w** does
the formula collapse to (m c)² ∝ J_u² + J_w², and only there can
one read the right-hand side as the magnitude-squared of an
angular-momentum 2-vector. This isotropic point is precisely where
the U(1) × U(1) ladder symmetry enlarges to SU(2) — see
[ho-bridge-2d.md §"Symmetry payoffs"](ho-bridge-2d.md). The
"vector angular momentum" reading and the SU(2) enlargement are
two faces of the same symmetry.

For N compact directions the same picture extends:
(m c)² = Σ p_i² = Σ (J_i / R_i)², with the angular-momentum-vector
reading available only for fully isotropic radial patterns.

## Where this reframing should live

The angular-momentum identification is a **re-reading** of existing
content, not new derivation. Further, the n ↔ orbital-angular-
momentum identification is itself the standard "particle on a ring"
interpretation from undergraduate QM — periodicity ⇒ integer n ⇒
L_z = n ℏ — and metric-mass Ch 2 §2 already brushes against it
explicitly ("the same logic that quantizes notes on a guitar
string, **quantizes angular momentum**, and quantizes electron
orbitals"). The placement should therefore be light, not duplicated.

**(a) One-sentence inline addition in
[metric-mass Ch 2 §6](../../metric-mass/02-mass-from-u.md).** §6 is
where the Compton-scale connection is already drawn. A single
sentence there — noting that n is the quantized
angular-momentum quantum number around the compact loop, and that
the rest-mass identity reads m·R·c = J — sits naturally next to
the existing Compton paragraph without disrupting §6's flow.

**(b) Section in the prospective metric-charge HO bridge
appendix.** The 2D case is what genuinely adds new content here:
two compact linear momenta in quadrature, the J-reading available
only at the isotropic point, and the connection to the SU(2)
enlargement. This belongs in the appendix that introduces the 2D
HO translation, since the multi-direction extension is what the
appendix already needs to cover.

**Considered and rejected: a separate paragraph in
[metric-mass Ch 9](../../metric-mass/09-harmonic-oscillator-bridge.md).**
Ch 9's translation table already covers the 1D mode ↔ ladder
correspondence. Adding "and also it is an angular momentum" as a
separate paragraph there would be redundant with the inline
sentence in Ch 2 §6.

The two places (a) and (b) collectively land the framing without
duplication.

## Open questions

(Embedding-dependence of the "loop's center" reading is addressed
inline in §"The identification" above; not a separate open question.)

1. **Spin.** The framing identifies *orbital* angular momentum
   (around the loop) with rest mass. It says nothing about *spin*
   (intrinsic angular momentum of the field). Whether spin in this
   framework is a separate object (e.g., a polarization label on
   the wave field) or a different facet of the same compact-loop
   structure is open. Worth flagging as a sibling question for
   later projects, not for this back-edit.

   MaSt currently carries two distinct candidate readings for why
   the fundamental fermion spin is 1/2, alluded to elsewhere in the
   repo and not adjudicated here:

   - **Two-dimension reading.** Spin 1/2 because the compact
     substrate for matter sheets is 2D — two compact directions
     produce a half-integer spectrum naturally when the closure
     condition mixes the two windings.
   - **Winding-ratio reading.** Spin 1/2 because of the specific
     ratio of windings on the sheet — configurations of type
     (1, 2) or (1/2, 1) and their relatives carry an effective
     "half" through the way the two windings synchronize, not
     through the dimensionality of the substrate per se.

   The two readings are not equivalent (one is about the *number*
   of compact directions, the other about *how* a given pair of
   windings combines), and which one — or whether some combination
   — is correct is open. Both should be tracked when the spin
   question is taken up systematically.

2. **Reverse direction (framework hypothesis, not a derived
   consequence).** If rest mass = quantized angular momentum around
   a compact loop, does any observed rest mass imply a compact
   loop? The framework's working hypothesis is yes: mass requires
   winding on some compact direction. But this is **assumed** — the
   manifold has a compact direction by construction
   ([metric-mass Ch 1](../../metric-mass/01-foundation.md)) and
   mass arises from winding on it (Ch 2). The angular-momentum
   reading restates this hypothesis in different vocabulary; it
   does not strengthen the implication or convert the hypothesis
   into a derivation. The reverse direction (mass ⇒ compact loop)
   remains a framework hypothesis to be tested against alternative
   mass-generation mechanisms, not something this reframing
   establishes.

## Status

The identification is correct (algebra checked above) and physically
clarifying within its limits. Items adjusted per
[angular-momentum-as-mass-review.md](angular-momentum-as-mass-review.md):

- Symbol J_u introduced to disambiguate the angular momentum from
  the compact circumference L_u (item 1).
- Rest-energy rewrite uses ω_rot = c/R_u (n-independent) for the
  rotor identity, and Planck–Einstein separately for ω_n; the
  conflation has been removed (item 2).
- 2D extension now combines compact **linear** momenta in
  quadrature; the J-vector reading is restricted to the isotropic
  case and tied to the SU(2) point at ε = 1 (item 3).
- Inline embedding caveat added in §"The identification"; original
  Open Question 1 dropped as redundant (item 4).
- "Reduced Compton wavelength" used throughout (item 5).
- "Sharpens" softened to "re-states" and the tautology
  acknowledged explicitly (item 6).
- Placement narrowed to (a) one inline sentence in metric-mass
  Ch 2 §6 + (b) a section in the prospective metric-charge HO
  appendix; the metric-mass Ch 9 paragraph dropped as redundant
  (item 7).
- Reverse-direction Open Question 2 marked explicitly as framework
  hypothesis, not a derived consequence of this reframing (item 8).

The "where it lives" decision is the only remaining step before
edits to existing chapters. The current recommendation (a)+(b)
above is tentative; the user may prefer to land it in fewer places.

No edits to existing chapters have been made; this file documents
the reframing and placement options for review.
