# Higher-order charges from multiple compact directions

**Status:** Exploratory and forward-looking. Not appendix-grade.
See [work/README.md](README.md) for context.

## Scope

Extend the U(1) / U(1)×U(1) charge story from the 1D
([metric-mass](../../metric-mass/)) and 2D ([metric-charge](../))
compact cases to N compact directions. Assess:

- whether SU(N) at full radial isotropy is the natural geometric
  candidate for QCD color (N = 3) and similar higher symmetries,
- whether baryon number fits the same ladder/U(1) mechanism or
  belongs to a separate (winding-count) story,
- what would have to be true of the framework before either reading
  can be made structural rather than speculative.

This file is aimed at later work in [ma-domain](../../ma-domain/)
extensions and [metric-binding](../../metric-binding/). Nothing here
is committed to be implemented in metric-charge itself.

## The N-direction extension

A manifold with N compact directions (radii R_1, ..., R_N) admits
free-wave modes labeled by N integer winding numbers
(n_1, ..., n_N). The dispersion gives

<!-- m² = (ℏ/c)² · Σ_i (n_i / R_i)² -->
$$
m^2 \;=\; \left(\frac{\hbar}{c}\right)^2 \sum_{i=1}^{N} \left(\frac{n_i}{R_i}\right)^2
$$

— Pythagorean combination of all N single-direction masses. Each
direction contributes one canonical momentum p_i = ℏn_i/R_i and one
ladder operator pair (a_i, a_i†) in the HO reading.

The associated symmetry depends on the radial pattern:

| Pattern | Symmetry | Notes |
|---|---|---|
| All R_i distinct (fully anisotropic) | U(1)^N | Each ladder has its own phase; N commuting charges |
| Two equal, rest distinct | U(1)^{N−2} × SU(2) | Pairwise mixing where radii match |
| All R_i equal (fully isotropic) | U(1) × SU(N) | Maximal symmetry; one overall phase + SU(N) ladder-mixing |

The SU(N) at isotropy is the *operator-algebra shadow* of an
isotropic radial pattern. It is invisible in the classical wave
reading.

## Specific case: N = 3 and color

Three compact directions with equal radii give SU(3) at full
isotropy — the gauge group of QCD color. The 8 SU(3) generators map
to 8 mode-mixing operations on the three ladder pairs
(a_1, a_2, a_3).

The candidate statement:

> Three compact directions with matched radii produce SU(3) as a
> structural symmetry. Color is the algebraic shadow of three-fold
> isotropy of the compact manifold.

Two factual checks against the framework's existing structure:

- **Three-sheet appearances.** Several [ma-domain](../../ma-domain/)
  candidates use three-sheet or three-phase structure (e.g.,
  three-phase wraps in [Ch 8 of metric-charge](../08-shear-and-fractional-charge.md)
  for fractional charge; three protons / three neutrons in recent
  ma-domain config work). Whether any of these correspond to "three
  compact directions with matched radii" in the strict sense
  required for SU(3), versus a different three-fold structure that
  only shadows SU(3), is open.

- **Confinement.** Full unbroken SU(3) is what produces QCD's
  confinement and asymptotic freedom phenomenology. A *broken*
  SU(3) (radii close but not equal) would give three approximately
  commuting U(1)'s with small off-diagonal interactions — *not* the
  QCD spectrum. So the color identification requires either
  enforced isotropy of three radii or an additional mechanism that
  produces the SU(3) phenomenology without requiring exact equal
  radii.

This is a constraint, not a refutation. The candidate stands as a
plausible direction; it is not derived.

## Why baryon number probably doesn't fit the ladder pattern

Baryon number in the Standard Model is **not a gauge symmetry**. It
is a global U(1) of the quark fields that is "accidental" — it is
preserved by the SM Lagrangian's renormalizable terms but is not
protected by any gauge structure. Anomalies (sphaleron processes)
can violate it.

If every charge in the geometric framework were a compact-direction
ladder, baryon number would have to be one of the U(1)^N's — but
then it would be a gauge charge with a gauge boson, which it is not
in observed physics.

A more likely structural origin: baryon number as a **winding-count
of a specific knot type** — the number of copies of a primitive knot
T(1, n') in a multi-component link. This makes baryon number a
*topological* count rather than a *spectral* (ladder-occupation)
quantity.

The structural distinction:

- **SU(N) / U(1) gauge charges** are local generators acting on the
  compact-direction ladders. They are continuous symmetries with
  associated gauge bosons.
- **Baryon number** would be a discrete count of how many primitive
  knots are stacked on the same sheet (or how many copies of a
  primitive winding pattern appear). Discrete, global, no gauge
  boson, violated by topology-changing processes.

This is forward-looking; the formal development belongs in
[metric-binding](../../metric-binding/) once multi-knot structure is
in scope.

## What would have to be true before any of this becomes structural

For the SU(3) → color identification to graduate from speculative to
structural, at least one of the following has to be established:

1. **A mechanism that enforces radial isotropy** for three compact
   directions, producing exact SU(3) as a geometric necessity.
2. **A demonstration that approximate SU(3)** (radii close but not
   equal) reproduces the *phenomenological* features of QCD
   (confinement, asymptotic freedom, three-jet events) without
   requiring exact symmetry.
3. **An identification of the eight SU(3) generators** with
   specific geometric operations on the three-direction substrate,
   such that "a gluon" has a concrete geometric description.

For baryon number as winding-count to graduate, the framework needs:

1. **A definition of multi-knot configurations** on a single sheet
   or across multiple sheets (this is metric-binding's job).
2. **Demonstration that the winding count is conserved** by the
   framework's interaction rules.
3. **A treatment of why the conservation is approximate** (i.e.,
   what the geometric analog of sphaleron processes looks like).

## Open questions

1. **Does the wrap-promotion ladder (grid-duality §7) extend cleanly
   to L4, L5, ...?** Each higher rung would correspond to an
   additional compact direction in the metric-charge ↔ ma-domain
   correspondence. The 2D L3 is well established. L4 has not been
   characterized.

2. **What does the lepton/quark split look like geometrically if
   color is N = 3 isotropy?** Quarks transform as the
   SU(3)-fundamental (3 copies); leptons are SU(3)-singlet (1
   copy). Geometrically, this would mean quark configurations
   occupy the three ladders as a non-trivial multiplet while lepton
   configurations occupy a singlet combination. Worth working out
   what "singlet combination" of three compact-direction excitations
   looks like in mode terms.

3. **Generation count = number of ladder copies?** SM has three
   generations of fermions; if each generation is "the same SU(N)
   structure with a different excitation level on one ladder," the
   framework would need a natural argument for why exactly three
   levels are accessible (rather than two or four or infinitely
   many). The HO ladder is infinite in occupation number; some
   additional energetic or stability cut-off would be needed to
   limit it to three.

4. **Electroweak SU(2) from the metric-charge ε = 1 case?** The
   metric-charge HO bridge work
   ([ho-bridge-2d.md](ho-bridge-2d.md)) identifies SU(2) at ε = 1
   as a structural symmetry of the 2D case. Whether this SU(2)
   could be a candidate for electroweak SU(2)_L is an open
   identification question. Two compact dirs with matched radii
   would have to be physically realized for the symmetry to hold.

## Status

Exploratory. None of this is appendix-grade. The N = 3 isotropy → SU(3)
identification is structurally compelling but requires either an
enforced-isotropy mechanism or a treatment of approximate SU(3) before
it can be presented as a derived consequence rather than a candidate.

Baryon number as winding-count is plausible but undeveloped; the
necessary multi-knot machinery lives in metric-binding.

Forward direction: develop in parallel with multi-direction extensions
in ma-domain, and return to make appendix-level claims only after the
mechanism questions above are settled.
