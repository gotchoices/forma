# Per-arc geodesic curvature as fractional charge contribution

**Status:** Exploratory. Not chapter-grade. See
[work/README.md](README.md) for context.

## Scope

The sheet-proton clover constructions
([clover-quarks.md §11.7](../../sheet-proton/work/clover-quarks.md),
[modulated-clover.md §2.3, §4.3](../../sheet-proton/work/modulated-clover.md))
take charge along an arc to be the integrated geodesic curvature:

<!-- Q(γ) = (1/2π) ∫_γ κ ds -->
$$
Q(\gamma) \;=\; \frac{1}{2\pi}\,\int_\gamma \kappa_g\, ds
$$

A complete simple closed plane curve gives Q = 1 by Gauss–Bonnet. An incomplete arc
gives a fractional partial sum: Q_lobe = +2/3 for a 240° lobe arc, Q_saddle = −1/3 for
a 120° saddle arc. These are **per-arc fractional charge contributions**, treated as if
they were the per-arc analogue of the multi-knot fractional charges of
[ch. 8 §7](../08-shear-and-fractional-charge.md).

But the two readings are **structurally different objects**:

- **Ch. 8 §7 fractional charge** is the fractional *association* of an integer total
  across the k structural components of one closure-satisfying multi-knot. It is
  per-knot, not per-arc. Ch. 4 line 177 is explicit: "not a fractional value of a single
  quantity."
- **Sheet-proton clover fractional charge** is a fractional *value* of an integrand-
  level quantity (the geodesic curvature integral) along one incomplete arc of one
  curve. It is per-arc, with the total over a closed curve being integer by
  Gauss–Bonnet.

The sheet-proton reading is **imported into the clover constructions without derivation
from grid-primitive or metric-charge upstream** (verified by survey on 2026-05-24).
clover-quarks §11.7 introduces it as "the user's 'convex = +, concave = −' framing,"
which is intuition, not a derived consequence.

This file attempts to bridge the per-arc reading to the framework's existing
charge mechanism (grid charge-emergence + metric-charge KK identification). If the
bridge holds, the clovers' charge story becomes consistent with — and derivable from —
the rest of the framework. If it leaves gaps, those gaps become precise.

## The setup

Three readings of charge are in play:

| Source | Charge defined as |
|---|---|
| **grid charge-emergence** | Accumulated persistent normal-E-field leakage on a closed loop, quantized by 2π-periodicity. Integer. |
| **metric-charge ch. 4** | Integer winding number of compact-direction wave mode (KK identification). Integer. |
| **sheet-proton clovers** | (1/2π) ∫_γ κ_g ds — integrand-level along arcs, integer only on closed-loop totals. |

The first two are equivalent in the framework: grid's leakage *is* the KK winding around
the second compact direction when the wave is the photon-on-shape construction.
The third is the sheet-proton extension under test here.

## Attempted derivation

**Step 1 — grid lattice bend → continuum geodesic curvature.**

The grid is a discrete substrate. A "bend" of the lattice at a vertex stores a
quantum of normal-field leakage flux. The continuum limit replaces discrete bends by
a continuous geodesic curvature κ_g(s) along a smooth curve, with per-vertex bend →
κ_g ds. Accumulated normal-field flux on a closed loop in the grid:

  Φ_grid = Σ_{vertices on loop} (per-vertex bend)

Continuum limit (heuristic — see open question 1):

<!-- Φ_continuum = ∮_γ κ_g ds -->
$$
\Phi_{\text{continuum}} \;=\; \oint_\gamma \kappa_g\, ds
$$

**Step 2 — Gauss–Bonnet quantizes the closed-loop total.**

For a simple closed curve γ on a surface where the enclosed region D is topologically
trivial and intrinsically flat (or where the Gaussian curvature integral is itself
2π·integer), Gauss–Bonnet gives

<!-- ∮_γ κ_g ds + ∫∫_D K dA = 2π · χ_D -->
$$
\oint_\gamma \kappa_g\, ds \;+\; \iint_D K\, dA \;=\; 2\pi\,\chi_D ,
$$

and for the flat planar case χ_D = 1, K = 0:

  ∮ κ_g ds = 2π × (winding number of the tangent).

**Step 3 — identification with the framework's EM charge.**

The framework identifies this total accumulated normal-field flux with an integer EM
charge (this *is* what grid charge-emergence establishes for closed loops). So:

<!-- Q = (1/2π) ∮ κ_g ds = integer charge -->
$$
Q \;=\; \frac{1}{2\pi}\oint_\gamma \kappa_g\, ds \;=\; \text{integer EM charge.}
$$

For a closed planar curve traversed once: Q = 1, the unit charge the user's question
already takes as given.

**Step 4 — per-arc partial contribution is well-defined.**

For a closed loop decomposed into N arcs γ = γ_1 ∪ … ∪ γ_N,

<!-- Q = Σ_i Q_i,  Q_i = (1/2π) ∫_{γ_i} κ_g ds -->
$$
Q \;=\; \sum_{i=1}^{N} Q_i ,
\qquad
Q_i \;=\; \frac{1}{2\pi}\int_{\gamma_i} \kappa_g\, ds .
$$

The Q_i are real-valued (in general fractional, either sign). Their sum is the closed-
loop integer. In the grid's discrete language, Q_i is the partial sum of per-vertex
bends along arc γ_i — a real, additive, integrand-level quantity.

This **is** the per-arc fractional charge contribution used in clover-quarks §11.7 and
modulated-clover §4.3. The 240° lobe with κ = +1/r gives Q_lobe = (1/2π)(1/r)(4πr/3) =
+2/3; the 120° saddle with κ = −1/r gives Q_saddle = −1/3; etc.

## Confinement — per-arc fractions are not standalone

The Q_i are real numbers. Only the closed-loop sum Σ Q_i is forced to be integer (by
2π-periodicity in Step 2). The framework's commitment, inheriting grid charge-emergence:
**observable persistent EM charges are integer closed-loop totals**, not per-arc
fractions. A standalone fractional charge would require an arc that does not close —
which by the leakage mechanism cannot sustain a persistent charged state (only an
ephemeral one during photon passage).

So per-arc fractional contributions exist as integrand-level quantities but are not
standalone observable particles. They are only observable as part of an integer-summing
closed loop. **This is the geometric realization of confinement.** Quarks
(Q = +2/3, −1/3 per arc-fragment) cannot be isolated; baryons (3 arcs summing to integer
Q) can.

This puts the per-arc reading on the same structural footing as the ch. 8 §7 multi-knot
reading: in both, fractional values exist only inside a configuration whose total is
integer-quantized, and individual fractional pieces are non-isolable. The two readings
differ in *what* is being decomposed:

| | What carries the integer total | What carries the fraction |
|---|---|---|
| **Ch. 8 §7** | A k-component multi-knot | Each of the k closure-satisfying primitives (1/k per component) |
| **This file** | A single closed arc-loop with N pieces | Each arc piece (real value from integrating κ_g over that piece) |

Both are "fractional structurally exists; integer total quantized; pieces non-isolable."
They are complementary axes of the same confinement principle.

## What this bridge establishes — and what it doesn't

**Established (modulo Step 1's continuum-limit heuristic).**

- Per-arc Q_i is a well-defined integrand-level quantity that sums to the closed-loop
  integer charge.
- Confinement of the per-arc fractions follows from the framework's commitment that
  only closed-loop integer totals are persistent.
- The per-arc reading is structurally consistent with ch. 8 §7's per-knot reading
  (different decompositions of the same integer-quantization rule).

**Not established (open).**

- **Step 1 is heuristic.** Discrete grid bend → continuum geodesic curvature is
  intuitive but not derived from grid-primitive's link-level structure. A clean
  derivation would start from the lattice action and show κ_g emerges as the
  appropriate continuum object. Belongs in grid-primitive (see open question 1).
- **Step 2 needs care for non-trivial topology.** For non-contractible loops on a
  torus (e.g., a baryon path around the tube on the modulated-clover surface), the
  enclosed-region argument doesn't apply the same way. Gauss–Bonnet's relative form
  (∮ κ_g ds + ∫∫ K dA = 2π χ) still holds, but χ is not simply 1 for non-trivial
  loops. The framework's "closed loop = integer charge" needs to be verified to hold
  in the cases sheet-proton actually uses (where the loop is a sweep on a torus,
  not a simple plane curve).
- **The choice of 3-fold symmetry.** This bridge grounds *fractional contributions*
  but not *thirds specifically*. Q_lobe = 2/3 vs 1/6 or 1/2 depends on the
  cross-section's Z_N symmetry; the clover construction posits Z_3 to match QCD
  color, without deriving it. This intersects [higher-order-charges.md](higher-order-charges.md)
  open question on N-fold isotropy.
- **Half-integer windings.** The bridge as stated assumes closed-loop integer total.
  modulated-clover's (1/2, 1) tracks close only via the half-twist gluing; whether
  Gauss–Bonnet on a half-twisted surface gives integer-or-half-integer totals is the
  same open question raised in modulated-clover §6 open question 1.

## Where this should live, if it cleans up

If the bridge survives scrutiny — particularly if Step 1 gets a rigorous derivation
in grid-primitive and Step 2's non-trivial-topology cases check out — the natural home
is a metric-charge chapter or appendix on **per-arc curvature as a charge ledger**.
Structurally parallel to [metric-mass ch. 9](../../metric-mass/09-harmonic-oscillator-bridge.md)
(HO bridge): a translation chapter that downstream projects (sheet-proton, ma-domain)
can cite when using the per-arc fractional reading. It would not introduce new physics
into metric-charge's main arc; it would expose a per-arc reading of the closure rule
that is implicit in the existing chapters.

A clean version of the bridge needs three things:

1. **A grid-primitive companion** deriving κ_g as the continuum limit of discrete
   lattice bend, replacing the Step 1 heuristic with a rigorous identification.
2. **A metric-charge chapter** (this work file, hardened) stating the per-arc
   ledger reading with Gauss–Bonnet on the closed loop and the confinement statement.
   Includes the relation to ch. 8 §7 as the complementary fractional axis.
3. **Back-references in sheet-proton modulated-clover §4.3 and clover-quarks §11.7**
   replacing the current "by the user's framing" with citations to the metric-charge
   chapter.

## Open questions

1. **Continuum limit of grid bend → κ_g.** What is the rigorous derivation from a
   discrete lattice action? Does it require the link Hamiltonian (a grid-primitive
   question)? Likely the load-bearing piece for any chapter-grade promotion.

2. **Non-trivial loop topology.** For loops on a torus or modulated-clover that are
   not simple contractible plane curves, does the closed-loop integer-charge
   identification still hold? Working out the Gauss–Bonnet calculation explicitly on
   the modulated-clover surface would settle this — and might be a useful sanity
   check on the §4.5 Q = +1, 0 numbers.

3. **Half-integer windings.** Does the per-arc reading extend to (1/2, 1) tracks? The
   half-twist gluing means a track closes in half a tube revolution; does
   Gauss–Bonnet on such a track give an integer total, or does the half-twist
   topology re-route the integer count? This intersects modulated-clover §6 open
   question 1 directly.

4. **Z_N origin of thirds.** What forces 3-fold cross-section symmetry rather than
   2-fold, 6-fold, etc.? The clover construction posits it to match QCD; a
   foundational derivation would be a major step. Connects to
   [higher-order-charges.md](higher-order-charges.md) on whether matched compact-
   direction radii give a Z_N → SU(N) story.

5. **Berry-phase / holonomy alternative.** A different formal route — geometric
   phase accumulated by a wave parallel-transported around a loop — gives the same
   Q = (1/2π) ∮ κ_g ds expression directly. Is this an alternative derivation, or
   the *same* derivation in different language? If a holonomy framework can be
   imported, it might supply the rigorous version of Step 1 that grid currently
   lacks, bypassing the discrete-limit argument.

## Status

A **partial bridge**. Steps 2–4 are clean modulo non-trivial-topology cases (open
question 2); Step 1 (grid bend → κ_g) is heuristic and needs a foundational
companion in grid-primitive. The per-arc fractional reading is well-defined
geometrically *given* Step 1 holds, and the confinement story aligns it structurally
with ch. 8 §7's per-knot reading.

The bridge is **good enough to ground the sheet-proton clovers as consistent with
the framework** under the heuristic Step 1 reading; it is **not yet good enough to
present them as derived consequences** without grid-primitive's companion work.

Recommended next steps before any chapter-grade promotion: settle open question 1
(grid bend → κ_g) and open question 3 (half-integer winding compatibility), in
that order. Open question 4 (Z_N origin) is sheet-proton's domain and can be
addressed separately — the per-arc framework here is Z_N-agnostic.
