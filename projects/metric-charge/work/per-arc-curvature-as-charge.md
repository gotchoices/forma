# Per-arc geodesic curvature as fractional charge contribution

**Status:** Exploratory. Not chapter-grade. See [work/README.md](README.md) for context.

## Scope

The sheet-proton clover constructions
([clover-quarks.md §11.7](../../sheet-proton/work/clover-quarks.md),
[modulated-clover.md §2.3, §4.3](../../sheet-proton/work/modulated-clover.md))
take charge along an arc to be the integrated geodesic curvature:

<!-- Q(γ) = (1/2π) ∫_γ κ_g ds -->
$$
Q(\gamma) \;=\; \frac{1}{2\pi}\,\int_\gamma \kappa_g\, ds
$$

A complete simple closed plane curve gives Q = 1 by Gauss–Bonnet. An incomplete arc
gives a fractional partial sum: Q_lobe = +2/3 for a 240° lobe arc, Q_saddle = −1/3
for a 120° saddle arc — **per-arc fractional charge contributions with sign tracking
convex/concave geometry**.

This file develops the bridge from the framework's existing charge mechanism (grid
charge-emergence) to this per-arc reading. The bridge requires **one substantive
working hypothesis** that is not derived from grid-primitive's substrate as of the
2026-05-24 survey. Once that hypothesis is explicitly carried, the rest of the
derivation chain proceeds cleanly to a *local-manifestation* claim — the sheet-proton
clovers become consistent with the framework, with the gap to a full derivation
collapsed into one named, falsifiable claim. This is the pattern established
elsewhere in the framework (ch. 8 carries k as input without deriving it; metric-mass
ch. 9 carries the HO bridge as translation without claiming derivation).

## The setup

Three readings of charge are in play:

| Source | Charge defined as |
|---|---|
| **grid charge-emergence** | Accumulated persistent normal-E-field leakage on a closed loop, quantized by 2π-periodicity. Integer. |
| **metric-charge ch. 4** | Integer winding number of a compact-direction wave mode (KK identification). Integer. |
| **sheet-proton clovers** | (1/2π) ∫_γ κ_g ds — integrand-level along arcs, integer only on closed-loop totals. |

The first two are equivalent in the framework. The third is the sheet-proton extension
under test here.

Two distinct fractional-charge readings already coexist in the framework, on different
structural axes:

- **Ch. 8 §7** — fractional *association* of an integer total across the k structural
  components of one multi-knot. Per-knot. Ch. 4 line 177 is explicit: "not a fractional
  value of a single quantity."
- **Sheet-proton clovers** — fractional *value* of an integrand-level quantity along
  one incomplete arc. Per-arc.

These are complementary, not competitors — they decompose the integer total along
different structural directions. The bridge below develops the per-arc axis to the
same structural level as ch. 8 §7's per-knot axis.

## Working hypothesis G1

> **G1 (local-leakage identification).** Bending the grid's hexagonal cylinder lattice
> into a 2D surface embedded in 3D produces, in the continuum limit, a local
> normal-E-field leakage density along any curve on the surface equal to (1/2π) κ_g(s),
> where κ_g is the curve's geodesic curvature in the embedded surface. Equivalently:
> the local EM charge density per unit arc length along a curve on the bent surface is
>
> $$ \frac{dQ}{ds} \;=\; \frac{1}{2\pi}\,\kappa_g(s) . $$

This is the single working hypothesis carried by this file. Everything below proceeds
from G1 as input.

**What G1 asserts.** A geometric quantity (geodesic curvature) IS a physical quantity
(local EM charge density along a curve on the bent surface). The sign of κ_g (convex
outward = +, concave inward = −, under standard orientation) is the sign of the local
charge density. So a small piece of a convex bend carries a small + charge, a small
piece of a concave bend carries a small − charge, and the closed-loop total integrates
to the framework's integer EM charge by Gauss–Bonnet (Step 3 below).

**Why G1 is plausible without being derived.**
[grid/charge-emergence.md](../../grid/charge-emergence.md) §2–5 establishes
qualitatively that bending the hexagonal lattice into 3D makes Y-junctions non-coplanar,
producing per-junction normal-field leakage that depends on the local bend direction.
G1 is the continuum-limit version of this discrete junction-level mechanism — the
discrete picture's per-vertex bend becomes a continuous κ_g(s) ds along a smooth curve,
and the per-vertex leakage becomes a local density. The qualitative agreement is good;
what is missing is the rigorous derivation that the continuum limit gives specifically
(1/2π) κ_g and not some other function of the bend field.

**Why G1 is not derived in grid-primitive (2026-05-24 substrate survey).** grid-primitive
ch. 1–8 has no local-bend continuum field, no constitutive relation between bend and
the cylinder primitive's (e, φ) wave-fields under deformation, no continuum limit
producing κ_g, and no leakage-rate identification. The closest existing structure —
ch. 8's polygonal-kink picture — is discrete and explicitly marked as having an
uncontrolled (Δθ)² expansion at N = 6. The coupling magnitude α is explicitly not
derived from the bending mechanism even at the junction level. Making G1 rigorous
requires a multi-chapter structural addition to grid-primitive — see "Path to
promotion" and "Open question 1" below.

**Why naming G1 is honest rather than cheating.** G1 is a single, definite,
falsifiable claim that bundles the load-bearing missing identification into one named
hypothesis. It can be tested: if a future grid-primitive companion derives the
bend → κ_g identification with a different functional form, G1 is wrong and this
file's chain breaks at Step 1. If it derives the form G1 asserts, this file's chain
is promoted to a derivation. The pattern (carry a named hypothesis, complete the
downstream work, identify the promotion path) is established framework practice —
ch. 8 §5 explicitly forwards k-selection to downstream work while developing the
structural consequences in §7; metric-mass ch. 9 carries the HO translation as a
bridge without claiming derivation.

## Derivation under G1

**Step 1 — local charge density along a curve.** Given G1, the local EM charge density
per unit arc length at point P on a curve γ on the bent surface is

<!-- dQ/ds(P) = (1/2π) κ_g(P) -->
$$
\frac{dQ}{ds}\bigl(P\bigr) \;=\; \frac{1}{2\pi}\,\kappa_g(P) .
$$

This identifies κ_g(P) directly with a physical local quantity. Its sign at P tracks
convex/concave geometry at P.

**Step 2 — per-arc charge from integration.** For any sub-arc γ_i ⊂ γ,

<!-- Q_i = (1/2π) ∫_{γ_i} κ_g ds -->
$$
Q_i \;=\; \frac{1}{2\pi}\,\int_{\gamma_i} \kappa_g\, ds
$$

is the integrated local charge density along γ_i. Under G1 this is the *real, physical*
per-arc charge contribution — not just integrand bookkeeping. The sign of Q_i is the
sum of the local signs of κ_g along γ_i: for a purely convex arc Q_i > 0, for a purely
concave arc Q_i < 0, for a mixed arc the sign depends on which dominates.

**Step 3 — closed-loop total via Gauss–Bonnet.** For a closed curve γ on a surface
where the enclosed region D is topologically trivial and intrinsically flat,

<!-- ∮_γ κ_g ds + ∫∫_D K dA = 2π · χ_D -->
$$
\oint_\gamma \kappa_g\, ds \;+\; \iint_D K\, dA \;=\; 2\pi\,\chi_D ,
$$

and in the flat planar case (χ_D = 1, K = 0): ∮ κ_g ds = 2π × (winding number of the
tangent). Combined with G1:

<!-- Q = (1/2π) ∮ κ_g ds = integer EM charge -->
$$
Q \;=\; \frac{1}{2\pi}\oint_\gamma \kappa_g\, ds \;=\; \text{integer EM charge} .
$$

This recovers grid charge-emergence's "closed loop = integer charge" result at the
continuum level. Non-trivial topology (loops on a torus, modulated-clover tracks)
modifies χ_D — see open question 2.

**Step 4 — per-arc fractions sum to the integer.** For a closed loop decomposed into
N arcs γ = γ_1 ∪ … ∪ γ_N,

<!-- Q = Σ Q_i -->
$$
Q \;=\; \sum_{i=1}^{N} Q_i ,
$$

where each Q_i is per-arc real-valued and the sum is integer. This is the per-arc
fractional structure: real per-arc local charges, sign-varying, summing to an integer
at closure. The standard worked examples drop out:

  Q_lobe (240° arc, κ = +1/r) = (1/2π)(1/r)(4πr/3) = **+2/3**;
  Q_saddle (120° arc, κ = −1/r) = (1/2π)(−1/r)(2πr/3) = **−1/3**.

The clover proton sums 2 lobes + 1 saddle = 2(+2/3) + (−1/3) = **+1**; the neutron
2 saddles + 1 lobe = 2(−1/3) + (+2/3) = **0**. Modulated-clover §4.5's tuned
Q_p ≈ +1, Q_n ≈ 0 are these integer totals.

**Step 5 — local manifestation.** Because G1 makes (1/2π) κ_g(P) a real local charge
density (not merely an integrand piece), a probe coupling to EM charge at point P
couples to that local density. By standard form-factor / multipole-expansion arguments
from EM scattering:

- A probe with wavelength λ ≫ L_loop (long-wavelength) integrates over the whole loop
  and couples only to the monopole = integer total. The surface looks like an integer
  point charge.
- A probe with wavelength λ ≲ L_arc (short-wavelength) resolves individual arcs and
  couples to per-arc Q_i directly, *with sign tracking convex/concave geometry*. The
  surface's per-arc fractional structure is visible up close.

This step is what answers the user's "stacking jacks" question: up close, two surfaces
probing each other at scales below the loop size resolve each other's per-arc
fractional charge structure with the correct signs from local convex/concave geometry;
at a distance, they see only each other's integer totals. The Coulomb-style
interaction between resolved fractional charges of one surface and resolved fractional
charges of another is a calculable consequence and a natural starting point for any
downstream nucleon–nucleon binding work, though that calculation is downstream of
this file.

## Confinement — per-arc fractions exist locally but not as standalone persistent charges

Per-arc Q_i is a real local quantity under G1 — observable by short-wavelength probes
at the point along the arc. But **it is not a standalone persistent charge**: only
closed-loop integer totals are persistent under the grid leakage mechanism (an open
arc cannot sustain a persistent charge state, only an ephemeral one during photon
passage, per grid charge-emergence).

So per-arc fractional charges exist locally but are confined to their host closed-loop
integer configurations. Quarks (Q = +2/3, −1/3 per arc-fragment) are *locally
probable* inside baryons (3 arcs summing to integer Q) but cannot be ripped out as
standalone particles. This is the geometric realization of confinement under G1.

This puts the per-arc reading on the same structural footing as ch. 8 §7's per-knot
reading:

| | Carries the integer total | Carries the fraction | Decomposition axis |
|---|---|---|---|
| **Ch. 8 §7** | A k-component multi-knot | Each closure-satisfying primitive | Per-knot |
| **This file (under G1)** | A closed arc-loop with N pieces | Each arc piece (real per-arc Q_i) | Per-arc of κ_g |

Both are "fractional structurally exists; integer total quantized; pieces non-isolable
as standalone but locally probable inside the configuration." They are complementary
axes of the same confinement principle.

## What this bridge establishes — under G1

**Established (mathematically, given G1).**

- Per-arc Q_i = (1/2π) ∫_{γ_i} κ_g ds is a real local charge contribution with sign
  tracking convex/concave geometry.
- Per-arc fractions sum to the closed-loop integer EM charge by Gauss–Bonnet (modulo
  the non-trivial-topology caveat in open question 2).
- Confinement is structural: standalone persistent fractional charges are excluded by
  the grid leakage mechanism, but per-arc fractions are locally probable inside their
  host closed-loop configurations.
- Local manifestation: a short-wavelength probe at point P couples to (1/2π) κ_g(P)
  with the right sign; a long-wavelength probe couples to the integer total. The
  "stacking jacks" intuition is recovered as the short-wavelength regime of this
  picture.

**Sheet-proton clover constructions become consistent with the framework under G1.**
clover-quarks.md §11.7's Q = (1/2π) ∫_γ κ_g ds is recovered. Modulated-clover.md §4.3's
Q_track is the per-track integral of the experienced curvature, which under G1 is the
per-track charge. Modulated-clover.md §4.5's tuned Q_p ≈ +1, Q_n ≈ 0 are the
closed-track integer totals.

**Conditional on G1.** Without G1, the chain has no physical content beyond
differential-geometric bookkeeping (per-arc Q_i is a mathematical integrand piece of
an integer total, not a local physical quantity). With G1, the chain produces the
per-arc fractional reading with local manifestation, confinement, and consistent
recovery of all sheet-proton clover quantities.

## Path to promotion

To promote this file from "complete under G1" to "complete unconditionally," **G1 must
be derived from grid-primitive**. That requires a multi-chapter structural addition:

1. **Define local lattice bend as a continuum field** — θ_bend(x, y) or κ_ij on the
   lattice surface — with a clean continuum limit.
2. **Derive the constitutive relation** between the bend field and the cylinder
   primitive's (e, φ) wave-fields under deformation. (How the wave equation D ∂_t² u =
   M ∂_x² u is modified when the underlying lattice is bent.)
3. **Take the continuum limit** and identify the resulting bend field with κ_g, the
   standard geodesic curvature in the differential-geometric sense.
4. **Derive the leakage rate** per arc length, identify it with (1/2π) κ_g, and show
   that this is the local EM charge density that G1 posits.

These four items are the same work the original "Step 1" demanded, now bundled and
named as a single deliverable: **derive G1**. They are real chapter-grade additions to
grid-primitive, not work-file extensions.

Once G1 is derived, this file's chain (Steps 1–5 under G1) becomes a metric-charge
chapter, structurally parallel to metric-mass ch. 9 — a translation/bridge layer that
downstream projects (sheet-proton, ma-domain) can cite when using the per-arc
fractional reading.

## Open questions

1. **Derive G1.** Multi-chapter addition to grid-primitive as outlined above. The
   single major prerequisite for promotion to chapter-grade. Until done, sheet-proton's
   per-arc constructions are "consistent under G1" rather than "derived from the
   framework."

2. **Non-trivial loop topology.** Step 3 assumes a topologically trivial closed loop
   (χ_D = 1, K = 0 in the enclosed region). For loops on a torus or modulated-clover
   that are not contractible plane curves, the Gauss–Bonnet integer-charge
   identification needs to be redone with the correct χ. Working out the calculation
   explicitly on the modulated-clover surface would settle this — and might be a
   useful sanity check on modulated-clover §4.5's Q_p ≈ +1, Q_n ≈ 0 numbers.

3. **Half-integer windings.** Modulated-clover's (1/2, 1) tracks close only via the
   half-twist gluing. Does Gauss–Bonnet on a half-twisted surface give an integer
   total via this file's chain, or does the half-twist topology re-route the integer
   count? This intersects modulated-clover §6 open question 1 directly. Likely
   resolvable once question 2 is in hand.

4. **Z_N origin of thirds.** The per-arc bridge here grounds *fractional contributions
   in general*; it does not derive *thirds specifically*. Q_lobe = 2/3 vs 1/6 or 1/2
   depends on the cross-section's Z_N symmetry; the clover construction posits Z_3 to
   match QCD color. Connects to [higher-order-charges.md](higher-order-charges.md)
   on Z_N → SU(N).

5. **Berry-phase / holonomy alternative.** A geometric-phase framework gives the same
   Q = (1/2π) ∮ κ_g ds expression. Whether this could supply a *different proof of
   G1* — bypassing the discrete-limit argument in grid-primitive — is worth a separate
   look. If it works, G1 might promote without needing grid-primitive's structural
   chapters.

## Status

**Complete under G1.** The per-arc fractional charge reading used in sheet-proton's
clover constructions is consistent with the framework's existing charge mechanism,
conditional on the one explicit working hypothesis G1 (local-leakage density =
(1/2π) κ_g). Per-arc Q_i is a real local charge contribution, sign-tracks
convex/concave geometry, confines into integer closed-loop totals, and is locally
probable to short-wavelength probes — exactly the picture sheet-proton's clovers
actually rely on, and the "stacking jacks" intuition is recovered as the short-
wavelength regime.

**G1 is not derived from grid-primitive.** The 2026-05-24 substrate survey identified
what would need to be added to derive G1 (open question 1) — a multi-chapter
structural addition. Until that work is done, this file's chain is
complete-conditional-on-G1, not unconditionally derived.

**This file's contribution.**

- A precise statement of G1 as the *one* load-bearing hypothesis that bridges the
  per-arc reading to the framework's existing charge mechanism.
- A clean Steps 1–5 chain showing what follows from G1, including the
  local-manifestation step (Step 5) that answers what sheet-proton's clovers actually
  rely on — fractional charges visible up close with sign tracking convex/concave.
- A specific path to promotion (derive G1 in grid-primitive) so the open work is
  named and bounded.
- A demarcation between what is mathematically rigorous (Steps 2–4 differential
  geometry plus algebra; Step 5 standard EM under G1) and what depends on G1
  (Step 1 — the load-bearing identification).

The file is now in the same status pattern as metric-charge ch. 8 (carries k as input,
develops the structural consequences in §7) and metric-mass ch. 9 (carries the HO
translation as a bridge, not derivation). Promotion to chapter-grade requires G1
derived; until then, the file is a structural-completion under a named, falsifiable
hypothesis.
