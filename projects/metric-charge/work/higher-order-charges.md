# Higher-order charges from multiple compact directions

**Status:** Exploratory and forward-looking. Not appendix-grade.
**Not destined for metric-charge content.** The file lives in
`metric-charge/work/` because the analysis grew out of the 2D HO
bridge work, but the conclusions are aimed at later projects, not
at any metric-charge chapter or appendix. See
[work/README.md](README.md) for context. (Whether the file should
physically move to `metric-binding/work/` or a dedicated
forward-looking folder is an open organizational question; the
content does not change either way.)

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
| Two equal, rest distinct | U(1)^{N−1} × SU(2) | Two-ladder cluster gives U(2) = U(1) × SU(2); the other N−2 distinct radii give one U(1) each, for U(1)^{N−2}; total U(1)^{N−1} × SU(2) |
| k equal in one cluster, rest distinct | U(1)^{N−k+1} × SU(k) | General case: U(k) on the equal cluster plus one U(1) per distinct radius |
| All R_i equal (fully isotropic) | U(1) × SU(N) | Maximal symmetry; one overall phase + SU(N) ladder-mixing (k = N in the general row above) |

The SU(N) at isotropy is the *operator-algebra shadow* of an
isotropic radial pattern. It is invisible in the classical wave
reading.

## Specific case: N = 3 and color

Three compact directions with equal radii give SU(3) at full
isotropy. The 8 SU(3) generators map to 8 mode-mixing operations on
the three ladder pairs (a_1, a_2, a_3).

**Global vs gauge — important distinction.** The SU(3) that
emerges from radial isotropy is a **global** symmetry of the free-
mode algebra: it permutes/rotates the three ladders and preserves
the degenerate spectrum. QCD color, in contrast, is a **local
gauge symmetry**: confinement, asymptotic freedom, and the
three-jet structure are non-perturbative consequences of the
Yang–Mills dynamics that the local-gauge promotion produces. Those
phenomena do **not** follow from a global SU(3) symmetry of free
modes.

So at most the framework's three-radii isotropy provides the
*global-symmetry shadow* of color. Bridging from this to QCD-color
would require a **gauging mechanism** for SU(3) — analogous to how
[metric-charge Ch 5](../05-metric-self-consistency.md) gauges the
single-direction U(1) via off-diagonal metric components h_μw, but
non-abelian. No such mechanism is in scope anywhere in the project
as it stands.

The candidate statement, properly qualified:

> Three compact directions with matched radii produce **global**
> SU(3) as the structural symmetry of the free-mode spectrum.
> Whether this can be promoted to **gauge** SU(3) — and thereby to
> a QCD-color-like dynamics with gluons — is an open mechanism
> question; exact isotropy alone is not sufficient.

Two factual checks against the framework's existing structure:

- **Three-sheet appearances.** Several [ma-domain](../../ma-domain/)
  candidates use three-sheet or three-phase structure. Whether any
  of these correspond to "three compact directions with matched
  radii" in the strict sense required for global SU(3), versus a
  different three-fold structure that only shadows SU(3), is open.
  Note that a *separate*, existing geometric candidate for three-
  fold structure already lives at chapter grade in metric-charge
  itself — see the next section.

- **Approximate SU(3) is not QCD.** A *broken* SU(3) (radii close
  but not equal) would give three approximately commuting U(1)'s
  with small off-diagonal interactions — even further from QCD
  than the exact-isotropy global SU(3). The phenomenology of QCD
  has no obvious image at either end of the radial-pattern
  spectrum without an extra gauging step.

The candidate stands as a plausible direction; it is not derived.

## Two distinct geometric candidates for QCD-like 3-fold structure

The framework now carries two different, structurally distinct
geometric mechanisms that could underlie QCD-like 3-fold
phenomenology. They live in different geometries and predict
different physics, and contrasting them explicitly is necessary
before any single identification is pursued.

**(a) Three compact directions with matched radii** (the candidate
above). N = 3, all R_i equal, giving global SU(3) on the
three-ladder mode algebra. Lives on a 3D-compact substrate. To
reach QCD-color it requires a non-abelian gauging mechanism that
the framework does not currently have.

**(b) k = 3 component link on a 2D-compact sheet** (already
chapter-grade in [metric-charge Ch 8](../08-shear-and-fractional-charge.md)).
The closure-satisfying k-component link T(k, k·n′) with k_sel = 3
produces three fragments per configuration, each carrying 1/3 of
the link's integer charge, with confinement-like inseparability
because individual components fail the closure condition on their
own. Lives on the 2D-compact sheet that metric-charge already
treats; needs no new substrate.

The two are not the same mechanism:

| | (a) 3-isotropy | (b) k = 3 link |
|---|---|---|
| Substrate dimension | 3 compact directions | 2 compact directions (single sheet) |
| Source of 3-fold structure | Equal radii of 3 directions | Number of components in a multi-component link |
| Fractional charge | Not addressed at this level | 1/3 per component, automatic |
| Confinement-like behavior | Requires gauging procedure not in scope | Built in: components fail closure individually |
| Status in framework | Speculative (this file) | Chapter-grade (Ch 8) |
| Identification with QCD-color | Global SU(3) shadow only | Direct geometric origin of fractional/inseparable structure |

Which (if either) is the right geometric origin of QCD's 3-fold
structure is open. Candidate (b) currently has the stronger
grounding in the framework — it is already a chapter-grade
mechanism, it gives the right fractional charge without further
machinery, and its confinement-like behavior is structural rather
than dynamical. Candidate (a) offers a richer symmetry algebra but
sits behind a missing gauging step.

A serious attempt at color in this framework should probably start
by asking whether (a) and (b) are competing or complementary —
e.g., whether a k = 3 link on a sheet whose two compact directions
happen to satisfy some isotropy condition exhibits *both*
structures simultaneously.

## Why baryon number probably doesn't fit the ladder pattern

Baryon number in the Standard Model is **not a gauge symmetry**. It
is a global U(1) of the quark fields that is "accidental" — it is
preserved by the SM Lagrangian's renormalizable terms but is not
protected by any gauge structure. Anomalies (sphaleron processes)
can violate it.

In the framework as it stands, [metric-charge Ch 5](../05-metric-self-consistency.md)
gauges every closure-satisfying compact-direction U(1) via the
corresponding off-diagonal metric component h_μw. *Under that
specific gauging prescription*, any compact-direction U(1) ends up
as a gauge charge with an associated gauge boson — and baryon
number empirically has no such gauge boson, so it cannot be one of
the U(1)^N's of the ladder reading *as currently gauged*.

This is a prescription-specific argument, not a logical necessity
of the geometry. A compact direction could in principle carry a
**global** U(1) without becoming a Kaluza-Klein gauge boson — the
relevant h_μw component would have to be absent or projected out,
which the Ch 5 prescription does not currently provide for. So the
ruling-out is "ruled out under the current gauging prescription,"
not "ruled out by the geometry itself." A variant prescription that
permits ungauged compact-direction U(1)'s would re-open
ladder-based baryon-number candidates.

Setting that prescription-dependent argument aside, a more likely
structural origin is baryon number as a **winding-count of a
specific knot type** — the number of copies of a primitive knot
T(1, n') in a multi-component link. This makes baryon number a
*topological* count rather than a *spectral* (ladder-occupation)
quantity.

The structural distinction:

- **SU(N) / U(1) gauge charges** are local generators acting on the
  compact-direction ladders. They are continuous symmetries with
  associated gauge bosons (under the Ch 5 prescription).
- **Baryon number** would be a discrete count of how many primitive
  knots are stacked on the same sheet (or how many copies of a
  primitive winding pattern appear). Discrete, global, no gauge
  boson, violated by topology-changing processes.

### Two issues the winding-count proposal has to address

The proposal needs to be checked against two SM facts before it can
be called a candidate, not just a direction:

- **Anti-baryons have B = −1.** A naive "number of copies of a
  primitive knot" is a non-negative integer count. The proposal
  therefore needs an orientation / sign structure on the knot
  contribution to deliver ±B. Charge conjugation in the existing
  framework ([metric-charge Ch 6](../06-handedness-and-pairs.md))
  maps (m, n) ↔ (−m, −n); whether stacking T(1, n') and T(1, −n')
  copies cleanly produces B ↔ −B (rather than, say, B + |B| = 2|B|)
  is the first thing the formal development has to settle.

- **Per-quark B = 1/3, per-baryon B = 1.** In the SM each quark
  carries B = 1/3 and a baryon is three quarks. If baryon number
  is "the number of copies of a primitive knot," the natural unit
  is 1 per copy, not 1/3. Reconciling per-quark B = 1/3 with
  per-knot-copy B = +1 requires either redefining the
  identification (e.g., B = (number of copies) / 3) or identifying
  "a copy" with something other than a single quark. The
  [Ch 8 k = 3 component-link mechanism](../08-shear-and-fractional-charge.md)
  already gives 1/3 fractional EM charge per component, so it is
  plausible that the same mechanism delivers 1/3 baryon number per
  component, which would *match* per-knot-copy B = 1/3 cleanly —
  but this needs to be worked out explicitly.

This is forward-looking; the formal development belongs in
[metric-binding](../../metric-binding/) once multi-knot structure
is in scope, and the two issues above should be carried into that
work as constraints.

## What would have to be true before any of this becomes structural

For the SU(3) → color identification to graduate from speculative
to structural, **both** of the following have to be established
(not just one):

1. **A non-abelian gauging mechanism for SU(3).** Enforcing radial
   isotropy alone gives only **global** SU(3); QCD-color requires
   the symmetry to be **gauged** (local, with Yang–Mills dynamics
   and gluon-like off-diagonal degrees of freedom). The metric-charge
   Ch 5 gauging procedure handles the abelian U(1) case via h_μw;
   a non-abelian analog for three compact directions does not exist
   in the framework as it stands and would have to be constructed.
2. **An identification of the eight SU(3) generators** with
   specific geometric operations on the three-direction substrate,
   such that "a gluon" has a concrete geometric description and
   confinement / asymptotic freedom can be read off the geometry.

(Approximate SU(3) from near-equal radii is *not* a sufficient
alternative path: it gives three approximately commuting U(1)'s
with small off-diagonal corrections, which is qualitatively wrong
for QCD's confining, non-perturbative behavior.)

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

   **The deeper problem is mass scaling, not count.** The ladder
   spectrum is m_n ∝ |n|, so a 3-level cut-off would give mass
   ratios m_2/m_1 = 2 and m_3/m_1 = 3. Observed SM ratios:

   - m_charm / m_up ≈ 580
   - m_top / m_up ≈ 10⁵
   - m_τ / m_e ≈ 3500

   These differ from the naive ladder-level ratios by factors of
   10²–10⁴. The "generation = ladder excitation" reading is
   observationally falsified by the mass spectrum, not just
   count-bounded — any cut-off mechanism would have to spread the
   levels in a wildly non-linear way, not just stop at three. This
   is the question that decides whether the identification is
   viable at all, not a detail.

4. **Electroweak SU(2) from the metric-charge ε = 1 case?** The
   metric-charge HO bridge work
   ([ho-bridge-2d.md](ho-bridge-2d.md)) identifies SU(2) at ε = 1
   as a structural symmetry of the 2D case. Whether this SU(2)
   could be a candidate for electroweak SU(2)_L is an open
   identification question. Two compact dirs with matched radii
   would have to be physically realized for the symmetry to hold.

   **There is an unflagged chirality gap.** Electroweak SU(2)_L is
   a **chiral gauge symmetry**: it acts on left-handed fermions
   and is invisible to right-handed ones. The HO SU(2) at ε = 1
   is a **global, achiral** symmetry mixing the two ladders
   (a_u, a_w) with no intrinsic handedness. For the identification
   to land, the framework would need at minimum:

   - Gauge promotion of the global SU(2) to a local gauge symmetry
     (covariant derivative, gauge bosons).
   - A chirality structure so that the SU(2) acts on one chirality
     only — the bare HO SU(2) is achiral and supplies no such
     structure.
   - Spontaneous breaking to U(1)_EM via something Higgs-like.

   Item 2 (the achirality of the bare HO SU(2)) is the largest gap
   and is currently missing from both this file and
   [ho-bridge-2d.md](ho-bridge-2d.md).

## Status

Exploratory. None of this is appendix-grade. Items adjusted per
[higher-order-charges-review.md](higher-order-charges-review.md):

- Symmetry table middle row corrected to U(1)^{N−1} × SU(2); the
  general k-equal cluster formula added (item 1).
- Global vs gauge SU(N) distinction made explicit; the "color =
  algebraic shadow of isotropy" candidate now properly qualified
  as the *global-symmetry shadow only*, with the gauging
  requirement called out as a separate, unsolved step (item 2).
- New section contrasting (a) 3-isotropy and (b) Ch 8's k = 3
  component-link mechanism as two distinct geometric candidates
  for QCD's 3-fold structure (item 7).
- Generations OQ augmented with the mass-scaling falsification
  (10²–10⁴ deviation from the linear ladder ratios), not just the
  count problem (item 3).
- Electroweak SU(2)_L OQ augmented with the chirality gap (HO
  SU(2) at ε = 1 is achiral; SU(2)_L is chiral) (item 4).
- Baryon-number-as-winding-count section augmented with the
  anti-baryon sign issue and the per-quark-1/3 vs per-knot-copy-1
  reconciliation (item 5).
- "Compact U(1) ⇒ gauge boson" argument tightened: now noted as
  prescription-specific to the Ch 5 KK gauging, not a logical
  necessity of the geometry (item 6).
- Forward-looking flag at top sharpened to make clear the file is
  not destined for metric-charge content (item 8 partial; file
  location decision deferred).

The N = 3 isotropy → SU(3) identification is now properly
qualified as a *global-symmetry shadow* only, with the gauging
step explicitly named as missing. Ch 8's k = 3 component-link
mechanism is identified as a structurally distinct, already
chapter-grade alternative for the same QCD-like 3-fold structure;
serious color work should contrast the two before committing to
either.

Baryon number as winding-count is plausible but undeveloped; the
sign and 1/3-per-component issues are now flagged for the
metric-binding work that would carry it forward.

Forward direction: develop in parallel with multi-direction
extensions in ma-domain, and return to make appendix-level claims
only after the mechanism questions above are settled.
