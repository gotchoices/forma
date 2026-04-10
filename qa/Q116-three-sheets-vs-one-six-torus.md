# Q116: Are three sheets the same thing as one six-torus?

**Status:** Open — structural insight with implications for
compound modes, string theory, and the role of cross-shears
**Related:**
  [Q115](Q115-three-generations-and-metric-structure.md) (three generations and metric),
  [Q111](Q111-neutrino-coupling-constant.md) (per-sheet coupling constants),
  [Q77](Q77-alpha-as-impedance.md) (α as impedance mismatch),
  [R53](../studies/R53-three-generations/findings.md) (ε = 330 geometry),
  [R50](../studies/R50-filtered-particle-search/findings.md) (compound modes, neutron),
  [`model-D.md`](../models/model-D.md) (6×6 metric structure)

---

## 1. The question

MaSt organises the six compact dimensions as three
material sheets — Ma_e, Ma_ν, Ma_p — each a 2D torus.
An alternative description treats the same six dimensions
as a single six-torus (T⁶) with a 6×6 metric.  **Is
there any mathematical difference between these two
descriptions?**

## 2. The metric is the same object

A 6×6 symmetric metric has 21 independent components.
In the "three sheets" language:

| Category | Count | Components |
|----------|-------|------------|
| Circumferences (diagonal) | 6 | L₁…L₆ |
| Within-plane shears | 3 | s₁₂, s₃₄, s₅₆ |
| Cross-plane shears | 12 | σ₁₃, σ₁₄, σ₂₃, σ₂₄, … |
| **Total** | **21** | |

In the "six strings" language:

| Category | Count | Components |
|----------|-------|------------|
| Circumferences (diagonal) | 6 | L₁…L₆ |
| Mutual shears (off-diagonal) | 15 | one per pair of dimensions |
| **Total** | **21** | |

And 3 + 12 = 15.  **It's the same 21-parameter object.**
The "sheet" decomposition is a basis choice — a way of
reading the matrix — not a property of the matrix itself.

## 3. When sheets are real: σ = 0

At zero cross-shear, the 6×6 metric is block-diagonal:

```
G = | G_ee   0      0    |
    | 0      G_νν   0    |
    | 0      0      G_pp |
```

The three 2×2 blocks are independent.  Mode energies
decompose as E² = E²_e + E²_ν + E²_p.  A mode on the
electron sheet has n₃ = n₄ = n₅ = n₆ = 0 and its
energy depends only on G_ee.  The sheets are cleanly
separated — "electron mode" and "proton mode" are
well-defined labels.

This factorized geometry (T⁶ = T² × T² × T²) is a
special point in the moduli space of the six-torus.

## 4. When sheets blur: σ ≠ 0

With nonzero cross-shears, the off-diagonal blocks
fill in.  Energy acquires cross-terms — the electron
quantum numbers interact with the proton quantum
numbers.  The eigenmodes of the full 6×6 system are
no longer localisable on any single sheet.

**The neutron is already an example.**  Its best match
in the unfiltered R50 search is (−2, −4, −2, −1, −2, 0)
— nonzero quantum numbers on all three sheets.  It is
not "on" any sheet.  It is an eigenmode of the full
6D metric.

## 5. Compound modes as 6D knots

On a single 2D sheet, a mode (n_t, n_r) is a torus knot:
a closed curve that winds n_t times around the tube and
n_r times around the ring.  One path, one object.

On the full T⁶, a compound mode like the neutron is the
same thing scaled up: **a single closed curve in 6D**
that winds the prescribed number of times around each
of the six dimensions before returning to its start.
Not three separate knots sharing energy — one knot
threading all six dimensions.

The integer quantum numbers are the closure condition:
the curve must return to its starting point in all six
dimensions simultaneously.

### The precession picture

From any single sheet's perspective, the compound mode
looks like a **precessing orbit**.  Project the 6D
trajectory onto the electron sheet's two dimensions:
you see a path that winds around the electron tube and
ring but doesn't quite close.  It drifts — precesses —
by an amount set by the neutrino and proton windings.
The orbit only closes when all six dimensions have been
traversed.

The cross-shears control this precession.  They tilt
the 6D trajectory so that motion along one sheet's
tube has a component along another sheet's ring.  At
σ = 0, there is no tilt and no precession — the
three sheet projections close independently.  At
σ ≠ 0, each sheet sees a slowly-varying pattern that
precesses through configurations until the full 6D
figure closes.

### The Lissajous analogy

A Lissajous figure on an oscilloscope traces a closed
curve from two frequencies at a rational ratio.  At
1:1 it's an ellipse; at 2:3 it's a more complex loop.
A compound mode is a **6D Lissajous figure** — six
frequencies (one per dimension) whose ratios are set
by the quantum numbers and metric.  The figure closes
because the quantum numbers are integers.  Each sheet's
2D projection shows a recognisable but incomplete piece
of the full pattern.

## 6. The R53 geometry: sheets become strings

R53 found that the electron sheet at (ε = 330, s = 3)
reproduces the three charged lepton masses from three
low-order modes.  At ε = 330:

- The tube circumference is 330× the ring circumference
- The fundamental domain (a rectangle L_tube × L_ring)
  is an elongated ribbon — effectively 1D
- The torus is almost a sphere (the ring hole has
  shrunk to a pinprick)
- Charge distribution is nearly perfectly spherical
  (~0.3% asymmetry)

**Each sheet is effectively a string** — one dominant
dimension with a tiny compact transverse width.  The
three "sheets" become three "strings."  And the full
T⁶ with cross-shears becomes **three coupled strings**
— which is precisely the setup of string theory
compactified on T⁶ in the large complex-structure
limit.

## 7. Structural parallels with string theory

The mathematical framework shared between MaSt and
string theory on T⁶:

| Feature | MaSt | String theory on T⁶ |
|---------|------|---------------------|
| Compact space | 6D torus (T⁶) | 6D torus (T⁶) |
| Metric parameters | 21 (circumferences + shears) | 21 (metric moduli) |
| Mode quantum numbers | (n₁,…,n₆) integer windings | Winding + momentum numbers |
| Factorised limit | T² × T² × T² (3 sheets at σ=0) | Factorised T⁶ (special moduli point) |
| Modular parameter | τ = s + iε per sheet | τ per T² factor |
| Large ε limit | Sheets → strings (R53: ε = 330) | Large complex-structure / thin-torus limit |
| τ → τ+1 symmetry | Shear shift s → s+1 | Modular T-transformation |

**What MaSt adds that string theory hasn't achieved:**
- Three generations from shear resonance (R53)
- Specific mode assignments for known particles
- A mechanism connecting the modular parameter to
  measured masses (shear resonance → mass hierarchy)

**What string theory has that MaSt hasn't used:**
- The antisymmetric B-field (15 additional components
  on T⁶, alongside the 21 symmetric metric components).
  If MaSt's compact sector is truly a T⁶, these 15
  degrees of freedom may encode physics not yet explored
- T-duality: the symmetry R ↔ 1/R between large and
  small compact dimensions.  MaSt's shift from ε = 0.65
  (model-D) to ε = 330 (R53) could be a T-duality
  transformation — dual descriptions of the same physics
- Modular invariance constraints that restrict which
  (ε, s) values give consistent theories

## 8. Is MaSt a version of string theory?

The shared mathematics (T⁶ moduli, winding modes, modular
parameters) invites the question.  The honest assessment:

**What justifies the comparison:**
- Both frameworks identify particles as vibrational modes
  of extended objects in compact dimensions
- Both live on the same mathematical arena (T⁶ with a
  21-parameter metric)
- At R53 geometry (ε = 330), each MaSt sheet is
  effectively a 1D string with a tiny compact transverse
  direction — literally a compactified string
- GRID's ℵ-line (the 1D internal dimension of each
  lattice edge) is structurally a string at the Planck
  scale; the Ma sheets are collective modes of many
  such strings at the Compton scale

**What separates them:**
- String theory strings are 1D objects that *propagate
  through* spacetime.  MaSt sheets *are* the particle
  — they don't move through the compact space, they are
  standing waves on it
- String theory requires supersymmetry and critical
  dimensionality (10D or 26D).  MaSt uses 9+1 without
  SUSY
- String theory compactifies at the Planck scale
  (~10⁻³⁵ m).  MaSt's compact dimensions are at the
  Compton scale (~10⁻¹³ m) — 22 orders of magnitude
  apart
- String theory produces ~10⁵⁰⁰ vacua and cannot
  select among them.  MaSt has specific parameters
  fixed by measured particle masses

**Assessment:** MaSt is a cousin framework — the same
conceptual programme (particles = modes of compact
geometry) built from different axioms (lattice physics
rather than perturbative quantum gravity) and operating
at a different scale (Compton rather than Planck).  It
solves problems string theory has not (three generations,
specific particle masses) but lacks the formal
mathematical infrastructure (worldsheet CFT, dualities,
anomaly cancellation) that gives string theory its
internal consistency checks.

The relationship may eventually be made precise: T-duality
maps large compact dimensions to small ones, so MaSt's
Compton-scale tori could be the T-dual of Planck-scale
strings.  If so, MaSt and string theory would be dual
descriptions of the same underlying physics — not a
"wing" of string theory, but its long-wavelength mirror.

## 9. Implications

1. **The "sheet" label is approximate.**  At σ = 0,
   sheets are real entities.  At σ ≠ 0, they are a
   basis choice.  Physical particles — especially
   compound modes like the neutron — are eigenstates
   of the full T⁶ metric, not of any individual sheet.

2. **Per-sheet coupling constants (Q111) become
   basis-dependent.**  The α_ν ≈ 1/52 computed from
   the neutrino sheet's (ε, s) is meaningful at σ = 0
   (where the sheet is a well-defined subsystem) but
   approximate at σ ≠ 0 (where sheet identity blurs).

3. **The compound mode is one object, not three.**
   There is no "electron part" and "proton part" of
   the neutron that can be separated.  The 6D knot is
   irreducible once cross-shears couple the dimensions.

4. **String theory's mathematical tools apply.**  The
   moduli space, duality symmetries, and modular
   constraints of T⁶ compactifications are directly
   applicable to MaSt's compact sector.  This is a
   large and well-developed mathematical toolkit that
   has not yet been brought to bear on MaSt.

## 10. Open questions

1. Does MaSt have an analogue of the antisymmetric
   B-field?  If so, what are its 15 components and
   what physics do they encode?

2. Is the model-D geometry (ε ~ 0.5–0.65) T-dual to
   the R53 geometry (ε ~ 330)?  If so, they describe
   the same physics in different coordinates, and the
   "correct" ε is a gauge choice rather than a physical
   parameter.

3. Do modular invariance constraints (τ → τ+1 and
   τ → −1/τ) restrict the allowed (ε, s) values?  If
   the electron sheet must sit at a modular-invariant
   point, this could derive the generation structure
   rather than fitting it.

4. At what cross-shear magnitude does the "sheet"
   decomposition break down entirely?  The working
   value σ_ep ≈ −0.28 is substantial — are the sheets
   already thoroughly mixed at this coupling?

5. Can the 6D Lissajous / precession picture be
   visualised computationally?  Projecting compound
   mode trajectories onto each sheet pair could build
   intuition about how cross-shears shape the internal
   circulation of compound particles.

---

*Connects to: Q115 (R53 generations), Q111 (per-sheet
coupling), Q77 (α as impedance), R53 (ε = 330 geometry),
R50 (compound modes / neutron), model-D (6×6 metric)*
