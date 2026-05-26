# Review — 11-modeling-foundation.md

Items I disagree with or find inaccurate in
[11-modeling-foundation.md](11-modeling-foundation.md). I do not
restate what the chapter gets right (the picture-A / picture-B
separation, the F/H citation framework, the §7 angular-momentum
treatment with embedding caveat, the corrected "one ladder per
mode" statement in §1, F6's discrete-D₄ result, F7's coherent-state
hedge). This list is only what should be fixed or qualified before
downstream projects cite this as a stable interface.

## 1. H1's per-arc charges are literal-arc-clover values, but the
downstream citation is "modulated-clover"

§6 carries the per-arc formula

  Q(γ) = (1/2π) ∫_γ κ_g ds

and immediately specialises it (lines 363–365) to

  Q_lobe = +2/3 for a 240° lobe arc;
  Q_saddle = −1/3 for a 120° saddle arc.

The 240° / 120° arc-extents are properties of the **literal
piecewise-arc clover** of
[sheet-proton/clover-quarks.md §11.7](../sheet-proton/work/clover-quarks.md);
they are *not* properties of the smooth tube-function
**modulated-clover**, which is the actual closure-satisfying
construction. The §6 step-4 example

  Q_proton = 2(+2/3) + (−1/3) = +1
  Q_neutron = 2(−1/3) + (+2/3) = 0

is the literal-arc reading.

The downstream-use paragraph then says (lines 427–430):

> Modulated-clover constructions in
> [sheet-proton/work/modulated-clover.md](../sheet-proton/work/modulated-clover.md)
> … should cite **H1 under G1**.

But [modulated-clover.md](../sheet-proton/work/modulated-clover.md)
§2.3 "Realizability" explicitly says:

> the smooth tube-function family **caps at Q_maj ≈ 0.63 < 2/3** —
> the +2/3 ideal lives at the κ → ∞ cusp limit of the arc-clover

so the modulated clover **cannot literally produce** Q_lobe = +2/3.
The integer (+1, 0) baryon charges are recovered there by *tuning
the modulation* (a 2-condition fit over the sin- and cos-harmonics),
not by per-piece arc-degree accounting.

Either:

(a) restrict §6's "per-arc fractional charge" derivation explicitly
    to the literal-arc clover, and supply a separate (or
    sub-section) treatment for how the modulated clover's
    *integrated* track charge under H1 produces the same integer
    totals via the modulation-tuning mechanism that
    modulated-clover.md §4.5 actually uses; or

(b) re-state H1 in terms of the *integrated track charge*
    (independent of arc-extent labelling) and have a separate
    paragraph note that the literal-arc 240°/120° split is an
    *idealised labelling* that the modulated clover only
    approximates.

As written, §6 conflates the two constructions and downstream
citations of "H1 under G1" for modulated-clover work will repeat
that conflation.

## 2. "A-native route to color SU(3)" via Ch 8's k = 3 mechanism
overstates what Ch 8 §7 delivers

§5 and §8's table both list:

| Color SU(3) | Ch 8 §7's k = 3 component-link mechanism … gives 1/3 fractional charge with confinement-like inseparability | SU(3) at 3D isotropy |

The glossary defines "SU(3) is the gauge group of QCD's colour
charge." The reader is primed to expect the Ch 8 mechanism to be
a substitute for, or geometric origin of, **gauge SU(3)** — a
Yang–Mills theory with 8 gluon fields, asymptotic freedom, and a
running coupling.

Ch 8 §7 actually delivers:

- A k-component multi-link as a single closure-satisfying winding
  pattern;
- Each component carries 1/k of the link's integer total charge;
- Components are not closure-satisfying alone, so they are not
  isolable as physical states — **structurally analogous** to QCD
  confinement.

This is a 3-fold structural decomposition with confinement-*like*
behaviour. It does **not** construct an SU(3) Lie algebra, gluon
fields, the Yang–Mills covariant derivative, or anything that
would produce a running coupling. Calling it "A-native route to
color SU(3)" elides the gap between "3-fold fractional charge with
inseparability" and "SU(3) gauge theory."

The fix is one of:

(a) Restate the mechanism as "A-native route to the structural
    analog of color confinement" or "A-native route to a 3-fold
    fractional-charge structure with confinement-like inseparability",
    and explicitly note that this is *not* the construction of
    gauge SU(3).

(b) Or, if the chapter wants to claim the Ch 8 mechanism *is*
    sufficient to model color, do so explicitly with a paragraph
    flagging that the framework's "color" target is the
    fractional-charge / confinement phenomenology only, not the
    gauge-theory dynamics.

As-is, the chapter inherits the conflation that
[work/higher-order-charges.md](work/higher-order-charges.md) made
between global SU(N) algebra structure and the gauge SU(N) of QCD.
(My prior review of that work file flagged the same point.)

## 3. "A-native route to spin-1/2" via half-twist + spin structure
papers over two known gaps

§5 (lines 343–347) and §8's table list spin-1/2's A-native route
as "Half-twist windings, (1/2, 1)-style configurations
(modulated-clover); spin structure on the compact manifold."

Two gaps the chapter should flag inline:

(a) **The (1/2, 1) winding sits outside the standard closure-mode
    derivation.** [modulated-clover.md](../sheet-proton/work/modulated-clover.md)
    flags this explicitly:

    > The half-integer tube winding of the (1/2, 1) tracks sits
    > outside the standard closure-mode derivation — a real
    > foundational gap (open question 1 in §6).

    Citing the (1/2, 1) configurations as the A-native route
    without acknowledging this foundational-gap status overstates
    the route's maturity.

(b) **"Spin structure on the compact manifold" is the
    *prerequisite* for hosting spinor fields, not a derivation of
    spin-1/2 physics.** Having a spin structure means one *can
    write down* spinors; it doesn't produce the Dirac equation,
    the gamma-matrix algebra, or any specific spin-1/2
    dynamics from scalar wave-equation modes. The framework's
    wave equation is for a scalar field (□φ + m²φ = 0). Going
    from scalar modes to spin-1/2 requires extending the
    field-equation structure, not just acknowledging that the
    manifold admits spinors. Citing "spin structure" as a route
    obscures this.

The status of the spin-1/2 candidate is "exploratory and
foundationally incomplete." The chapter should label it as such
inline — "candidate route, with a known foundational gap on the
(1/2, 1) winding side" — rather than presenting it on equal
footing with the (much-more-mature) color k = 3 mechanism (which
has its own caveat per item 2).

## 4. §4 "small-oscillation limit" mis-frames the dual view

§4 (lines 242–245) writes:

> **HO-complex view.** Near equilibrium, the wave equation on any
> shape **linearises** into a set of normal modes, each behaving
> as a one-dimensional harmonic oscillator with a frequency set by
> the shape's parameters.

and then (line 249):

> **The two views are not competitors.** The HO-complex is the
> **small-oscillation limit** of the wave-on-shape.

The framework's wave equation as picture A is

  □φ + m²φ = 0

— **already linear**. Its normal modes are its Fourier modes on
the substrate; there is nothing to "linearise" because there is
no non-linear potential to expand around. Calling the HO-complex
the "small-oscillation limit" of the wave equation suggests a
linearisation step that is not present in picture A.

The correct framing is: the HO-complex view is the **mode-basis
decomposition** of the wave equation, or equivalently, **canonical
quantisation in the normal-mode basis**. Each independent Fourier
mode quantises to its own creation/annihilation pair; the
collection of modes is a "complex of HOs" in the sense that each
mode is an HO in its own oscillator-amplitude variable. No
small-oscillation step is involved.

If a future version of picture A *does* contain an interacting
(non-linear) field theory (e.g., a φ⁴ piece, per Ch 8 §6's
floated candidate), then "small-oscillation limit" *would* be the
correct framing for that interacting theory. But the chapter
should be explicit if that is what is meant. As written, §4 reads
as if a linearisation is being invoked for the *free* wave
equation, which is mathematically empty.

## 5. §3 lumps three structurally different hypothesis types into
"the same status pattern"

§3 (lines 209–211) says:

> they are derived under one explicit, falsifiable hypothesis
> each, in the same status pattern as Ch 8 §7 (which carries k as
> input) and metric-mass Ch 9 (which carries the HO translation
> as bridge).

The three named "status patterns" are structurally different
kinds of object:

- **Ch 8 §7's k** is a *free numerical parameter* — an integer
  whose value linear theory doesn't fix. Carrying k as input
  means "for any k, the structural consequences are as follows."
  The hypothesis content is "some mechanism (φ⁴ inter-component
  energetics or substrate Z_k) selects a specific k."

- **Ch 9's HO translation** is a *change of mathematical
  language* — the same canonical-quantisation spectrum reframed
  via operator algebra. There is no new physics; the bridge is
  pure re-language. The "hypothesis" is the choice of formalism,
  not a substantive claim.

- **H1's G1 (local-leakage identification)** is a *substantive
  physical claim* — that the discrete grid lattice's continuum
  limit produces a specific charge density formula
  (dQ/ds = (1/2π) κ_g) pointwise. This is neither a free parameter
  nor a re-language; it asserts a specific functional form for a
  physical quantity, and is falsifiable in a way the first two
  are not.

- **H2's borrowing premise** is yet a fourth kind — adopting the
  algebra of a *different* physical system as a modelling
  vocabulary for picture A's targets.

Calling all four "the same status pattern" obscures that they
sit at quite different rungs on the hypothesis ladder. The fix is
either to rank them explicitly (free parameter < re-language <
substantive functional claim < borrowing from another physics) or
to drop the "same pattern" framing and let each carry its own
description.

## 6. F2 frames a single quantisation as "two quantisations"

F2 in the §2 table:

> The Pythagorean answer is *also* obtainable sequentially: treat
> m_u as a 1D rest mass, then add a second compact direction's
> KK momentum p_w; the relativistic dispersion gives
> m² = m_u² + (p_w/c)². **The sequential and joint quantisations
> give identical results.**

There is one canonical quantisation of the wave equation on T²;
the "sequential" derivation is a different *algebraic path* to the
same Pythagorean dispersion, not a different quantisation. "Joint"
treats both compact directions on equal footing from the start;
"sequential" treats one first and adds the second's KK momentum
on top. Both arrive at the same dispersion because the
relativistic energy-momentum identity is structured that way.

Calling these "two quantisations" suggests two distinct
mathematical procedures both leading to the same answer. Re-word
to "two algebraic paths to the same Pythagorean dispersion, both
within a single canonical quantisation of the substrate's wave
equation." Otherwise downstream citations risk reading F2 as a
claim about quantisation procedures that the underlying material
does not actually make.

## 7. §9 hand-off table cites H2 for spin-1/2 without requiring
§8's own preconditions

§9's table includes the row:

| Spin-1/2 candidates via picture B borrowing | §8 (borrowing premise H2) |

But §8 (lines 562–575) lists two conditions for picture B
borrowing to be appropriate:

> 1. The modelling target needs continuous SU(N), not a discrete
>    approximation, and not a topological/half-twist alternative.
> 2. No A-native construction on picture A's substrate has been
>    found that produces the target — i.e., the A-native route has
>    been investigated and ruled out, not just bypassed.

§5 and §8's own table list a half-twist A-native candidate for
spin-1/2. By §8's own condition 2, picture B borrowing for spin
is not currently appropriate — the A-native route has not been
ruled out, only flagged as candidate (with the gaps from item 3
above).

The §9 hand-off table's row therefore invites downstream citations
of H2 for spin-1/2 in violation of §8's own preconditions. Either:

(a) Add a column to the §9 table indicating the precondition
    state of each H2 citation row; or

(b) Remove the spin-1/2-via-H2 row from §9 until the half-twist
    A-native route has either been ruled out or proved out.

The current table is internally inconsistent with §8.

## 8. Glossary primes the reader for gauge SU(3); §5 delivers a
structural analog — flag the mismatch

The glossary (lines 49–56) defines SU(N) and ends with:

> SU(3) is the gauge group of QCD's colour charge.

§5 then uses "color SU(3)" as a downstream modelling target and
lists Ch 8 §7's k = 3 mechanism as an "A-native route to color
SU(3)." A reader who took the glossary entry at face value
expects an SU(3) Yang–Mills construction; what they get from the
Ch 8 mechanism is a 3-fold fractional-charge confinement-*like*
structure (see item 2).

The mismatch is reader-facing: glossary primes one expectation;
§5 delivers another without flagging the difference. Either
add a line to the glossary entry of the form "the framework's
target for 'color' is the fractional-charge / confinement
phenomenology, not gauge SU(3) Yang–Mills" — making the chapter
honest about scope — or rewrite the §5 row to not name "color
SU(3)" as the target.

## 9. Minor: H1 / H2 labelling consistency

§3's table labels H1's hypothesis as **G1** (a named ID with a
mnemonic) and H2's hypothesis as **borrowing premise** (a
description, not a named ID). If downstream projects are expected
to cite the hypothesis names explicitly (per §3 line 218: "any
downstream citation should preserve the flag"), giving the
borrowing premise a parallel name (e.g., **B1**) would make the
citation interface uniform. The current asymmetry is a small
papercut, but the chapter has a stated "stable citation interface"
goal that the asymmetry undercuts.

## Summary of recommended fixes

1. Restrict H1's 240°/120° → 2/3/1/3 derivation explicitly to the
   literal-arc clover; supply a separate handling for the
   modulated clover's integrated track charge (which only
   approximates the per-piece ideal).
2. Restate Ch 8 §7's k = 3 mechanism as "structural analog of
   color confinement" or "3-fold fractional-charge structure with
   confinement-like inseparability", not as a route to "color
   SU(3)" tout court. Clarify that gauge SU(3) is not constructed.
3. Flag the spin-1/2 A-native route's two known gaps inline (the
   (1/2, 1) winding's foundational status; "spin structure" as
   prerequisite, not derivation).
4. Replace §4's "small-oscillation limit" framing with
   "mode-basis decomposition" or "canonical quantisation in the
   normal-mode basis." The wave equation is already linear.
5. Separate the H1 / Ch 8 k / Ch 9 HO bridge / H2 hypothesis
   types in §3; drop the "same status pattern" framing.
6. Re-word F2 so that "sequential" and "joint" are described as
   algebraic paths within a single quantisation, not as two
   quantisations.
7. Reconcile §9's hand-off table with §8's preconditions: either
   add a precondition-state column or remove the spin-1/2-via-H2
   row.
8. Reconcile the glossary's "SU(3) is the gauge group of QCD"
   with §5's "Ch 8's k = 3 is A-native route to color SU(3)" —
   either narrow the chapter's scope statement or qualify the §5
   claim.
9. Give H2's hypothesis a parallel ID (e.g., **B1**) to match G1.
