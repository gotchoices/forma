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

<!-- L_u = R_u · p_u = R_u · (ℏ n / R_u) = ℏ n -->
$$
L_u \;=\; R_u \cdot p_u \;=\; R_u \cdot \frac{\hbar\,n}{R_u} \;=\; \hbar\,n
$$

— a quantized integer angular momentum in units of ℏ. Same form as
the orbital angular momentum spectrum of standard quantum mechanics,
but here arising from the *periodicity* of the compact direction
rather than from diagonalizing L̂² and L̂_z.

The metric-mass rest-mass identification

<!-- m_n = ℏ |n| / (R_u c) -->
$$
m_n \;=\; \frac{\hbar\,|n|}{R_u\,c}
$$

rearranged:

<!-- m_n · R_u · c = ℏ |n| = |L_u| -->
$$
m_n \cdot R_u \cdot c \;=\; \hbar\,|n| \;=\; |L_u|
$$

— **rest mass × compact radius × c = angular momentum about the
loop**.

Equivalently, defining ω_n = |n|c/R_u as the loop's rotational
angular frequency:

<!-- m_n c² = ω_n ℏ -->
$$
m_n\,c^2 \;=\; \omega_n\,\hbar
$$

— rest energy equals one quantum of angular-momentum × angular
frequency, the standard rotational energy of a quantum at angular
momentum L = ℏn rotating at angular frequency ω_n.

## Physical reading

From inside the loop: a wave wraps around the compact direction with
phase advancing by 2πn per circuit and angular momentum ℏn about the
loop's center.

From outside (in extended spacetime t, S): the loop is too small to
be resolved. The angular momentum is not observable as such — it
appears only as the *energy* of the rotation, which by relativistic
mass-energy equivalence appears as rest mass m_n = E_n / c².

The compact-direction angular momentum is **hidden from extended
spacetime, but its energy contribution is not**. That energy is
exactly the rest mass.

## Connection to the Compton scale

Metric-mass [Ch 2 §6](../../metric-mass/02-mass-from-u.md) already
notes that R_u = ℏ/(m_1 c) is the reduced Compton wavelength of the
n = 1 particle, and connects this to Schrödinger's *zitterbewegung*.
The angular-momentum reading sharpens the connection:

> **A particle's Compton wavelength is the radius at which one
> quantum of orbital angular momentum produces the particle's rest
> energy.**

This is a clean physically intuitive statement that metric-mass's
existing framing approaches but does not state directly.

## Extension to 2D

On a 2D compact sheet (metric-charge), each direction has its own
angular momentum:

<!-- L_u = ℏn,  L_w = ℏm -->
$$
L_u \;=\; \hbar\,n,
\qquad
L_w \;=\; \hbar\,m
$$

and the [Ch 2 §3](../02-modes-on-a-sheet.md) Pythagorean mass
formula reads as a vector-magnitude of angular momentum:

<!-- (m_(m,n) · c)² = (L_u · 2π/L_u)² + (L_w · 2π/L_w)² -->
$$
(m_{(m,n)}\,c)^2 \;=\;
\left(\frac{2\pi\,\hbar\,n}{L_u}\right)^2
+ \left(\frac{2\pi\,\hbar\,m}{L_w}\right)^2
$$

— a quadrature combination of two angular-momentum contributions,
each weighted by 2π/L_i, exactly as expected for two independent
rotations whose energies add in quadrature in the relativistic
combination. This generalizes cleanly to N compact directions and
makes the Pythagorean form of the mass formula intuitive rather than
formal.

## Where this reframing should live

The angular-momentum identification is a **re-reading** of existing
content, not new derivation. Options:

**(a) Back-edit to [metric-mass Ch 2](../../metric-mass/02-mass-from-u.md).**
Add a short paragraph (likely in §3 where the rest-mass formula is
derived, or §6 where the Compton-scale connection is drawn) noting
that n is the quantized angular-momentum quantum number around the
compact loop and that m·R·c = L is the resulting identification. The
change is small (~1 paragraph) and clarifying for any reader of
metric-mass.

**(b) Paragraph in
[metric-mass Ch 9 HO bridge](../../metric-mass/09-harmonic-oscillator-bridge.md).**
The HO formalism naturally hosts angular-momentum operators on the
loop (L̂ = −iℏ ∂/∂θ, eigenvalues ℏn on e^{inθ}). A short paragraph
there ties the angular-momentum reading directly to the HO framework
and makes the "L̂ has integer eigenvalues" → "rest mass quantized in
units of ℏ/(R_u c)" chain explicit.

**(c) Treatment in the prospective metric-charge HO bridge appendix.**
The 2D case has two angular momenta and the Pythagorean mass formula
is naturally read as a vector-magnitude of angular momentum (the
extension section above). Including the 2D angular-momentum framing
here would make Ch 2 of metric-charge feel more physically motivated
without disrupting the existing derivation.

**Tentative recommendation.** All three. The change is small enough
in each location that no one of them gets bloated:

- (a) is a one-paragraph back-edit that improves metric-mass on its
  own merits.
- (b) is a one-paragraph addition to the existing HO appendix.
- (c) is one section of the prospective metric-charge appendix and
  is the natural place to introduce the multi-direction extension.

Collectively the framing lands the physical interpretation cleanly
without any single chapter carrying the whole load.

## Open questions

1. **Direction of angular momentum.** The "angular momentum about
   the loop's center" reading assumes the compact direction is
   embedded with a natural rotation axis (perpendicular to the loop
   plane). For an abstract S¹ as a quotient of the real line, this
   axis is a *choice* — there is no embedding-independent direction.
   In a 2D sheet (S¹ × S¹) the two axes are mutually orthogonal in
   the natural embedding. Is the angular-momentum framing
   embedding-dependent in any way that matters? Probably not for
   the mass identification (which only uses the magnitude), but
   worth a one-line acknowledgment in whichever document carries
   it.

2. **Spin.** The framing identifies *orbital* angular momentum
   (around the loop) with rest mass. It says nothing about *spin*
   (intrinsic angular momentum of the field). Whether spin in this
   framework is a separate object (e.g., a polarization label on
   the wave field) or a different facet of the same compact-loop
   structure is open. Worth flagging as a sibling question for
   later projects, not for this back-edit.

3. **Reverse direction.** If rest mass = quantized angular momentum
   around a compact loop, does *any* observed rest mass imply a
   compact loop? The framework would say yes (mass requires winding
   on some compact direction). This is the framework's central
   claim; the angular-momentum reading just makes it physically
   transparent.

## Status

The identification is correct (algebra checked above) and physically
clarifying. The "where it lives" question is the only remaining
decision before edits. The recommendation above (back-edit metric-mass
Ch 2 + one paragraph in metric-mass Ch 9 + a section in the
prospective metric-charge appendix) is tentative; the user may
prefer to land it in fewer places.

No edits to existing chapters have been made; this file documents
the reframing and the placement options for review.
