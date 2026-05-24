# Review — angular-momentum-as-mass.md

Items I disagree with or find inaccurate in
[angular-momentum-as-mass.md](angular-momentum-as-mass.md). I do not
restate the points the file gets right; this list is items to fix or
sharpen before any back-edits land in metric-mass or metric-charge.

## 1. Notation overload: `L_u` is used for two different quantities

The file introduces `L_u = R_u · p_u = ℏn` as the **angular momentum
about the loop's centre** (§"The identification", lines 36–39). The
"Extension to 2D" section then writes the Pythagorean mass formula

  (m c)² = (2π ℏ n / L_u)² + (2π ℏ m / L_w)²

where the `L_u` in the denominator is the **compact length**
L_u = 2π R_u — the metric-charge Ch 2 convention used throughout
[02-modes-on-a-sheet.md](../02-modes-on-a-sheet.md) and
[work/ho-bridge-2d.md](ho-bridge-2d.md). The Unicode comment

  `(m_(m,n) · c)² = (L_u · 2π/L_u)² + (L_w · 2π/L_w)²`

uses `L_u` to mean ℏn in the numerator *and* the compact length in
the denominator on the same line. It only makes sense if the reader
silently switches conventions mid-expression. Any back-edit that
inherits this clash will be a real source of confusion.

**Fix:** pick a single symbol for the angular momentum (e.g. `J_u`,
or simply keep "ℏn") and never overload `L_u`. The metric-charge
convention `L_u` = circumference is well-established and should not
be displaced.

## 2. "Standard rotational energy" mis-labels Planck–Einstein

The file writes (§"The identification", lines 67–73):

> m_n c² = ω_n ℏ
> — rest energy equals one quantum of angular-momentum × angular
> frequency, the standard rotational energy of a quantum at angular
> momentum L = ℏn rotating at angular frequency ω_n.

Two problems:

(a) E = ω_n ℏ is the **Planck–Einstein relation** E = ℏω applied to
the wave's temporal oscillation frequency ω_n = |n|c/R_u. It is not
"the standard rotational energy" of a rotor. The standard classical
rotational kinetic energy of a body with angular momentum L spinning
at angular frequency ω is **½ L ω** (= L²/2I), not L ω. Calling our
relation "the standard rotational energy" gives the reader the wrong
formula in their head.

(b) The ω_n in the formula is *not* the rotation rate of the
loop's phase pattern. The phase of U_n(u) e^{−iω_n t} = e^{i(n u/R_u
− ω_n t)} rotates around the loop at angular rate ω_n/|n| = c/R_u
(independent of n) — that is the genuine rotation rate of the
pattern. ω_n is the *temporal* oscillation frequency at a fixed
point on the loop, which scales linearly with n. If one wants the
honest rotor identity it is

  E = L · ω_rot = (n ℏ) · (c/R_u),

with ω_rot = c/R_u, not ω_n. The current wording conflates the two
frequencies and so makes a `L ω = E` claim that is right only for
|n| = 1.

**Fix:** either drop the "standard rotational energy" gloss in favour
of "Planck–Einstein E = ℏω for the wave's temporal oscillation" (the
cleanest reading), or restate it as "E = L · ω_rot with L = nℏ and
ω_rot = c/R_u (independent of n)". Don't mix the two.

## 3. The 2D Pythagorean form is not "two independent rotations whose
energies add in quadrature in the relativistic combination"

In §"Extension to 2D" the file says

> a quadrature combination of two angular-momentum contributions,
> each weighted by 2π/L_i, exactly as expected for two independent
> rotations whose energies add in quadrature in the relativistic
> combination.

This is the wrong physical reading.

(a) The quadrature (m c)² = (ℏ k_u)² + (ℏ k_w)² comes from
separation of variables of *one* wave equation on M; it is the
4-momentum identity for **one mode** with a two-component compact
momentum (p_u, p_w). It is not a relativistic combination of two
*separate* relativistic systems' energies — relativistic addition of
two particles' energies does **not** combine in such a Pythagorean
way (you need to choose a frame, account for momentum directions,
etc.).

(b) "Each weighted by 2π/L_i" is opaque: 2π/L_u is just 1/R_u, the
inverse compact radius. Stating it through the compact circumference
L_u rather than the radius hides the geometry of what the weight is.

(c) Calling the result a "vector-magnitude of angular momentum" only
holds when R_u = R_w. For R_u ≠ R_w (the generic anisotropic case
the work folder commits to in
[ho-bridge-2d.md](ho-bridge-2d.md), §"Symmetry payoffs"),

  (m c)² ∝ (n/R_u)² + (m/R_w)² ≠ n² + m²,

so the quantity in quadrature is **(L_i / R_i)** = **p_i**, not L_i
itself. The framing collapses to a clean "angular-momentum vector
magnitude" only at the isotropic point — exactly the point where
the U(1)×U(1) → SU(2) enlargement happens. Worth saying so
explicitly; the generic reading is "two-component **linear** momentum
on the compact sheet."

## 4. Embedding-dependent language used without inline caveat

The §"The identification" body treats "angular momentum about the
loop's centre" as a primary identification:

> p_u is the linear momentum tangent to the loop and the angular
> momentum about the loop's center is …

A loop's *centre* is not part of the data of an abstract S¹ (the
quotient of ℝ by L_u). It requires the loop to be embedded in a
plane with a definite rotation axis. The file flags this in Open
Question 1 but the main identification reads as if "angular momentum
about the loop's centre" is a derived fact rather than an
embedding-dependent reading.

A cleaner derivation: n is the eigenvalue of the translation
generator P̂_u = −iℏ ∂/∂u on e^{i n u/R_u}, well-defined on any
compact direction without an embedding. The "angular momentum"
*labelling* of n (and the scale ℏn = R_u · p_u) requires the
embedding; the **mass identification** uses only |n|, so it is robust
to the choice. Stating this inline (one sentence) would prevent a
careful reader from objecting.

## 5. "Reduced" Compton wavelength is dropped

§"Connection to the Compton scale" promotes the statement

> A particle's Compton wavelength is the radius at which one quantum
> of orbital angular momentum produces the particle's rest energy.

R_u = ℏ/(m_1 c) is the **reduced** Compton wavelength λ̄ = ℏ/(mc),
not the (full) Compton wavelength λ = h/(mc) = 2π λ̄. Metric-mass
Ch 2 §6 is careful to say "reduced Compton wavelength"
([02-mass-from-u.md](../../metric-mass/02-mass-from-u.md) line 1532).
The proposed back-edit drops the qualifier; if it lands as written
it will conflict with Ch 2 §6 and mislead any reader who knows the
factor-of-2π difference between λ and λ̄.

**Fix:** "reduced Compton wavelength" throughout.

## 6. The Compton "sharpening" claim is mostly tautology

The file argues that the angular-momentum reading

> sharpens the connection [to the Compton scale].

But R_u = ℏ/(m_1 c) at n=1 is, under the metric-mass derivation,
*the definition* of the mass scale m_1 — equivalently, R_u is
forced to be the reduced Compton wavelength of the n=1 mode by the
mass formula itself. Restating "R = ℏ/(mc) at n=1" as "the radius
at which one quantum of orbital angular momentum produces the rest
energy" is a clean *re-wording* but adds no derivational content;
the result is tautologically equivalent to the mass formula at
n = 1. "Sharpens" overstates what is happening. "A useful
re-statement of the n = 1 mass formula" would be honest.

## 7. The reframing is mostly textbook vocabulary

The file presents the n ↔ orbital-angular-momentum identification
as a fresh re-reading. But this is the standard "particle on a
ring" interpretation in undergraduate QM — periodicity ⇒ integer
n ⇒ L_z = n ℏ. Metric-mass Ch 2 itself already brushes this:

> This is the same logic that quantizes notes on a guitar string,
> **quantizes angular momentum**, and quantizes electron orbitals
> ([02-mass-from-u.md](../../metric-mass/02-mass-from-u.md), line ~407).

So the identification is already implicit in Ch 2 and is not novel.
This affects placement: the file's tentative recommendation —
back-edits in metric-mass Ch 2, metric-mass Ch 9, *and* the
prospective metric-charge HO appendix — is heavy for a vocabulary
remark. A single one-sentence inline note in metric-mass Ch 2 §6
(where the Compton tie-in already lives) plus the 2D extension in
the prospective metric-charge appendix would carry the load without
duplication. I would drop the metric-mass Ch 9 paragraph; Ch 9's
existing classical-wave ↔ HO translation table already implicitly
covers what the angular-momentum reading adds at the 1D level, and
adding a separate "and also it's an angular momentum" paragraph
risks repetition.

## 8. Open Question 3's "reverse direction" is not made transparent
by this reading

The file says:

> If rest mass = quantized angular momentum around a compact loop,
> does *any* observed rest mass imply a compact loop? The framework
> would say yes (mass requires winding on some compact direction).
> This is the framework's central claim; the angular-momentum
> reading just makes it physically transparent.

The framework's central claim is **assumed** — the manifold has a
compact direction by construction (Ch 1), and mass arises from
winding on it (Ch 2). The reverse direction (mass ⇒ compact loop)
is not a derived statement; it is the framework's working
hypothesis. Calling it "the framework's central claim" is fine, but
the wording "the angular-momentum reading just makes it physically
transparent" suggests the reading *strengthens* the implication.
It does not — it restates the same assumption in different
vocabulary. Worth being explicit that this is hypothesis, not
derivation.

## Summary of recommended fixes before back-edit

1. Choose a non-overloaded symbol for "angular momentum about the
   loop", e.g. J_u, and leave L_u for the compact length.
2. Drop or restate the "standard rotational energy" gloss; clarify
   ω_n vs ω_rot.
3. Re-frame the 2D Pythagorean form as a two-component **linear**
   compact momentum (not "two independent rotations"); reserve the
   "angular-momentum vector magnitude" reading for the isotropic
   case.
4. Add an inline one-sentence acknowledgment of embedding
   dependence in §"The identification".
5. Use "reduced Compton wavelength" consistently.
6. Soften "sharpens" to "re-states" (or similar).
7. Narrow the placement recommendation: one inline sentence in
   metric-mass Ch 2 §6 + the 2D extension in the prospective
   metric-charge appendix. Drop the metric-mass Ch 9 paragraph as
   redundant.
8. Mark the reverse-direction claim of Open Question 3 explicitly
   as a framework hypothesis, not a derived consequence of the
   angular-momentum reading.
