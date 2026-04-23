# Q124: Where does particle spin come from in MaSt?

**Status:** Answered — unified derivation established via
per-sheet Dirac–Kähler construction; architectural parallel
with the photon sector flagged.

**Related:**
  [Q07](Q07-flat-compact-dimensions.md) (flat 2-torus structure),
  [Q11](Q11-spin-statistics-filter.md) (earlier spin-statistics filter),
  [Q86](Q86-three-generations.md) (three-generation structure),
  [Q115](Q115-three-generations-and-metric-structure.md) (generations and metric),
  [Q116](Q116-three-sheets-vs-one-six-torus.md) (three sheets vs single T⁶),
  [Q122](Q122-why-torus-not-sphere.md) (torus vs sphere for compactification),
  [R60 Track 20](../studies/R60-metric-11/findings-20.md) (empirical compound-spin rule),
  [R62 derivation 7a](../studies/R62-derivations/derivation-7a.md) (metric alone — no spin),
  [R62 derivation 7b](../studies/R62-derivations/derivation-7b.md) (CP ratio rule),
  [R62 derivation 7c](../studies/R62-derivations/derivation-7c.md) (6D bulk Dirac),
  [R62 derivation 7d](../studies/R62-derivations/derivation-7d.md) (per-sheet Dirac–Kähler — the chosen derivation),
  [model-F](../models/model-F.md) (the working model).

---

## 1. The question

MaSt's matter modes are all observed to be spin-½ (electron,
muon, tau, neutrinos, quarks inside protons).  Where does this
spin come from in the compactified-geometry picture?  And how
do compound particles (mesons, baryons) get their spins (0, 1,
½, 3/2) given that they're built from multiple sheet
contributions?

This is not a small question.  It went through four distinct
proposals in derivation 7 (parts a, b, c, d) and a companion
empirical investigation (R60 Track 20) before landing on a
coherent answer.

## 2. The four derivation attempts

### 2a — Metric alone doesn't give spin (7a)

The first idea was: does the sheared-torus metric itself
produce spin-½ via Killing vectors or Levi-Civita holonomy?

**Answer (7a): no.**  On a flat 2-torus, the Levi-Civita
connection is identically zero, and the Killing algebra is
abelian u(1) ⊕ u(1).  Neither mechanism generates the (−1)
phase under 2π rotation that a spin-½ particle requires.
Spin-½ *fields* do live on T² (the 2-torus admits four spin
structures as ℤ₂ bundles), but the metric does NOT pick one
automatically — a spin structure must be chosen externally.

**Conclusion:** spin cannot come from the metric alone.  Some
additional structure (a field type, a spin bundle) has to be
posited.

### 2b — CP polarization ratio rule (7b)

The second attempt imagines a circularly-polarized photon
wrapping the 2-torus with winding (n_t, n_r).  Count how many
times the CP vector rotates per tube circuit: it rotates
n_r/n_t times.  By analogy with the standard
"fraction-of-a-rotation = spin" picture, assign

> **spin = n_t/n_r** (Williamson–van der Mark ratio rule)

**Under this rule:**
- (1, 2): spin ½ ✓ — electron
- (n, 2n) for any integer n: spin ½ ✓ — includes (3, 6)
- (1, 3): spin 1/3 ✗ — not a spin-½ candidate
- (1, 1): spin 1 — not spin-½

**Issues with 7b:**

1. It derives spin for a SINGLE MODE on a SINGLE SHEET.  It
   says nothing about compound modes spanning multiple sheets.
2. The ratio values 1/3, 1/5, etc. are non-physical — no
   observed particle has spin 1/3.  The rule implicitly assumes
   only ratios giving half-integer or integer results are
   "allowed" modes, but doesn't justify why.
3. For model-F's (1, 3) proton assignment, 7b rules out that
   mode as a valid spin-½ particle — creating the proton
   problem that motivated Tracks 15–19.

### 2c — 6D bulk Dirac spinor (7c)

The third attempt posits a single 6D Dirac spinor on the full
compactified M⁴ × T⁶ (or M⁴ × T² × T² × T²).  Standard
Kaluza–Klein reduction gives 4D Dirac fermions at every KK
mode, all spin-½ regardless of (n_t, n_r).

**This works mathematically** — the derivation is rigorous
and follows Witten 1981 / Duff–Nilsson–Pope 1986.  Every mode
is spin-½ because the field type (Dirac spinor) is spin-½ in
4D regardless of compactification.

**Why 7c was set aside:**

1. **GRID incompatibility.**  GRID's axioms (A1–A6) describe
   a lattice of U(1) phases — entirely bosonic.  A 6D Dirac
   spinor is a Grassmann field with no direct realization in
   GRID.
2. The derivation *did* suggest a bridge — the Dirac–Kähler
   correspondence on flat manifolds — but did not construct
   it explicitly for the MaSt/GRID case.  The "reconciliation
   debt" was flagged and deferred.
3. Bulk Dirac spinors on generic KK manifolds suffer from
   well-known problems (chirality doubling, generation
   counting, non-propagating components) that don't arise
   automatically — they have to be imposed through geometric
   constraints.

7c remained as an open-but-unused alternative for a while.
Then R60's Track 19/20 work on the (3, 6) proton and the
compound-spin question exposed a new problem: **the working
particle inventory was using the R50-era parity rule for spin
selection, but claiming 7b as the derivation**.  These don't
match.

### 2d — Per-sheet Dirac–Kähler (7d — the answer)

The fourth attempt, motivated by R60 Track 20's empirical
findings and the "scary correlation" with GRID's photon
sector, gives the cleanest derivation yet:

> **Each Ma sheet is a flat 2-torus, which admits a
> Dirac–Kähler field as its privileged fermion content.
> Kaluza–Klein reducing this field gives a tower of 4D
> Dirac spinors labeled by winding (n_t, n_r), each of spin ½
> regardless of (n_t, n_r).  Compound particles spanning
> multiple sheets have total spin given by SU(2) angular-
> momentum composition of per-sheet spin-½ contributions.**

This is the **per-sheet restriction of 7c**.  Instead of a
single global 6D Dirac spinor on T⁶ (7c's approach), 7d uses
three independent 2D Dirac–Kähler fields — one per sheet.
Advantages:

1. **Standard mathematics.**  Dirac–Kähler on flat T² is
   well-established (Ivanenko–Landau 1928, Kähler 1962,
   Becher–Joos 1982, Kogut–Susskind staggered fermions
   1975).  No novel field-theory construction required.
2. **Generation count automatic.**  Three sheets → three
   fermion families.  No need for index theorems or curvature
   conditions.
3. **Sidesteps bulk-spinor problems.**  Each sheet is treated
   independently; chirality and anomaly issues from global
   bulk spinors don't arise.
4. **Compatible with GRID substrates.**  The lattice
   realization of Dirac–Kähler is the Kogut–Susskind
   staggered-fermion construction — standard in lattice gauge
   theory.  The reconciliation debt 7c flagged has a concrete
   resolution path here.

See R62 [derivation-7d.md](../studies/R62-derivations/derivation-7d.md)
for the full derivation.

## 3. The R60 Track 20 empirical correlation

The derivation 7d path was not pulled from thin air.  It was
triggered by an empirical investigation that ran ahead of the
derivation.

**R60 Track 20** audited 12 candidate compound-spin rules
against the model-F particle inventory.  Each rule was a
different proposal for how per-sheet spin contributions compose
into an observable total.  Rules tested included:

- Strict 7b per-sheet (n_r = 2·n_t on every active sheet)
- Sum-all ratios
- e+p additive with ν paired off
- Parity rule (the current implementation)
- Vector magnitude √(s_e² + s_p² + s_ν²)
- L-∞ max
- **Unit-per-sheet AM addition** (each sheet contributes ½;
  compose via SU(2) angular-momentum)
- Others (total-winding, tensor-product, etc.)

**The winner** was unit-per-sheet AM:

- 14 of 16 non-input particles matched within 2%
- No pathological misses (unlike the parity rule, which
  admitted a π± tuple at 896% off)
- Only the pions (10–13%) exceeded 2%, and that's now known
  to be a proton-sheet parameterization artifact (R60 T21),
  independent of the spin rule

But the striking finding was the **taxonomic structure** that
fell out:

| Active sheets | Allowed spins (AM) | Observed particle class |
|:-:|:-:|:---|
| 1 | ½ | **Leptons** (electron, muon) |
| 2 | 0 or 1 | **Mesons** (π, K, η, η′ = spin 0; ρ, φ = spin 1) |
| 3 | ½ or 3/2 | **Baryons** (tau, neutron, Λ, Σ, Ξ = spin ½) |

This is **exactly the Standard Model taxonomy** — without
being put in by hand.  The search just asked "which rule best
fits the inventory?" and the winner turned out to encode
leptons/mesons/baryons as 1-/2-/3-sheet objects.

See R60 [findings-20.md](../studies/R60-metric-11/findings-20.md)
for the full analysis.

## 4. The "scary correlation" with the photon

A structural observation reinforces the derivation: **the same
principle that gives matter spin-½ on a 2-torus gives the
photon spin-1 on a single compact dimension.**

GRID's architecture places a U(1) phase field on its sub-
Planck compact dimension (aleph ≈ S¹, one compact direction).
Standard Kaluza–Klein reduction of a 1-form on M⁴ × S¹ gives:

- A_μ (4D 1-form, spin 1) — the photon
- A_5 (4D scalar from compact index)

The photon's spin-1 comes from the vector index structure,
preserved through KK reduction.  No winding-dependent spin
assignment, no ratio rule.

**The pattern:**

| Compact geometry | Privileged field | 4D spin after reduction |
|---|---|:-:|
| M⁴ (no compact) | Scalar / tensor as needed | 0, 2, … |
| M⁴ × S¹ (aleph) | U(1) 1-form (gauge) | **1** (photon) |
| M⁴ × T² (each sheet) | Dirac–Kähler → Dirac spinor | **½** (matter) |

The principle is **compact topology determines privileged
field type determines 4D spin**.  Each compact geometry has
a natural minimal field, and that field's Lorentz
representation gives the 4D spin.  No additional rules needed.

This is why 7d's derivation is compelling: it's the matter-
sector analogue of the standard KK photon construction,
applied to the per-sheet 2-torus topology.  The photon and
matter pieces of MaSt share a common architectural principle.

A rigorous GRID-level derivation of the photon (showing that
GRID's U(1) phase axiom gives 4D Maxwell theory via lattice
KK) is a separate project — flagged as a future R62
derivation but not blocking model-F's update.

## 5. The cross-product intuition

A natural intuition for compound-spin composition, raised
during the Track 20 discussions: "each sheet is orthogonal to
the others, so spins should combine like a non-scaling cross
product across orthogonal directions."

This instinct is correct — and its mathematical realization is
**SU(2) angular-momentum composition**, which IS a quantum
cross-product structure.  The SU(2) commutators

$$
[J_x, J_y] \;=\; i\,J_z
$$

with cyclic permutations have structure constants equal to
the Levi-Civita symbol ε_{ijk} — which is the cross-product
tensor.

**The non-scaling character** the intuition pointed at is
exactly captured by SU(2):

- Each sheet contributes a UNIT spin (½), not a magnitude that
  scales with (n_t, n_r) ratio.
- Composition is algebraic (tensor product of representations),
  not arithmetic (sum of magnitudes).
- Two spin-½'s combine to spin 0 OR spin 1 (a SET of allowed
  values), not to a scaled magnitude.

Under this picture:

- The "cross-product idea" was geometrically correct — sheets
  are orthogonal, composition is non-abelian.
- The magnitudes that compose are NOT the 7b ratios; they're
  fixed spin-½ per active sheet.
- The composition rule IS SU(2)'s quantum cross-product.

7b's ratio rule remains useful, but in a demoted role: it
identifies single-sheet modes whose CP polarization closes
cleanly on the torus without external imposition.  Those are
the "magic shear" (n, 2n) modes.  But spin-½ is a *topological*
property of the Dirac–Kähler field, not a dynamical property
of the CP rotation rate.

## 6. Path traversal intuition — why 2 compact dimensions
give spin ½

Another intuition raised: "what if 1/2 is derived from the
fact that half the path traverses the tube and half the ring,
rather than from a turns ratio?"

This is also correct at a deeper level.  A 2-torus has two
independent 1-cycles (tube and ring).  The Dirac spinor on T²
has two components, one naturally associated with each cycle's
ℤ₂ spin structure.  Their combination into a 4D Dirac spinor
under KK reduction gives spin ½ as a **topological**
consequence of the 2-torus structure.

The "½" doesn't come from literal arithmetic of "half path
tube + half path ring."  It comes from the projective nature
of Spin(3) = SU(2) vs SO(3): a 2π rotation in SO(3) corresponds
to 4π in Spin(3), and Dirac spinors on T² transform in this
projective representation.  The 2-torus's two cycles provide
exactly the right ℤ₂ structure for the Dirac–Kähler field to
project to a single Dirac spinor.

**So:**

- 1 compact dimension (S¹) → U(1) structure → 1-form field →
  spin 1 photon via vector-index preservation.
- 2 compact dimensions (T²) → ℤ₂ ⊕ ℤ₂ spin structure →
  Dirac–Kähler field → spin ½ fermion via projective
  representation.
- Higher compact structures would need their own analysis, but
  MaSt doesn't use them (sheets are 2-tori, aleph is S¹).

## 7. Summary — the coherent spin story

Putting it all together, MaSt has a unified, derivation-backed
spin story for the first time:

1. **Single-sheet modes (leptons, free quark constituents)
   are spin ½** because each sheet is a flat 2-torus admitting
   a Dirac–Kähler field whose KK reduction gives 4D Dirac
   fermions of spin ½ regardless of (n_t, n_r).  This is R62
   derivation 7d, leveraging standard results from Becher–Joos
   1982 and Kogut–Susskind 1975.

2. **Compound modes have total spin from SU(2) composition**
   across active sheets:
   - 1 active sheet → spin ½ (leptons)
   - 2 active sheets → spin 0 or 1 (mesons)
   - 3 active sheets → spin ½ or 3/2 (baryons)

   This is the empirically-derived unit-per-sheet AM rule
   from R60 Track 20, now with a theoretical underpinning in
   7d.

3. **The Standard Model taxonomy** (leptons, mesons, baryons
   as 1/2/3-sheet objects) emerges structurally from the
   sheet architecture + SU(2) composition.  Not postulated.

4. **The photon's spin 1** arises from the same principle
   applied to GRID's 1-compact-dimension substrate (aleph =
   S¹).  This is a structural parallel, not part of 7d's
   derivation, but architecturally coherent.

5. **7b's ratio rule** is demoted to a mode-structure rule:
   (n, 2n) modes have special CP-polarization closure
   properties relevant to some computations, but don't by
   themselves set spin — all KK modes are spin ½.

6. **7a's negative result** (metric alone doesn't give spin)
   is preserved and consistent: the spin comes from the FIELD
   TYPE (Dirac–Kähler), not from the metric.

7. **7c's bulk Dirac spinor** is recognized as a more
   ambitious global version of 7d's per-sheet construction.
   7d is the cleaner, GRID-tractable, three-generation-ready
   restriction.

## 8. Open derivation items

The spin story is now cohesive but two items remain for
further derivation work:

1. **Axiomatize per-sheet Dirac–Kähler from deeper
   principles.**  Why does each sheet carry a Dirac–Kähler
   field?  In principle, this could be derived from GRID's
   lattice structure via the staggered-fermion formulation.
   Pool-item derivation target.

2. **Pick the specific spin within SU(2)-allowed sets.**  2-
   sheet compounds are spin 0 OR 1 (SU(2) allows both); which
   is realized depends on internal structure (symmetry of the
   two-spinor combination).  3-sheet compounds are spin ½ OR
   3/2; the octet vs decuplet distinction has a known group-
   theoretic basis that needs to be made explicit in the MaSt
   context.

These are conventional physics extensions, not obstructions
to the working model.

## 9. Model-F implications

Model-F's current documentation still references the parity
rule or 7b as the spin derivation.  The in-place update
should:

- Adopt 7d as the single-sheet spin derivation.
- Adopt SU(2) AM composition (per R60 Track 20) as the
  compound-spin rule.
- Reference this Q and R62 derivation 7d as the derivation
  chain.
- Note the photon-parallel observation as architectural
  elegance but not part of the matter derivation.
- Flag the two open items (deeper per-sheet axiom, specific-
  spin selection) as pool items.

This update closes the spin-derivation gap that has existed
since the early R-study era.
