# R63 Track 10: Pauli-saturated multi-strand coherence

Track 10 takes up the last Ma-internal candidate for nuclear binding,
reframed by the reviewer from the original Phase 9d "Z₃ multi-strand
phase coherence" wording into a deterministic Pauli-saturation picture.

**Premise.**  Each (1, 2) p-sheet primitive strand carries a Z₃ color
(3 values) and a Dirac–Kähler spin (2 values).  Pauli antisymmetry gives
a per-tuple capacity of 3 × 2 = 6 strands.  The proton (k = 3) fills
half the slots; the deuteron (k = 6) fills all six and is *Pauli-
saturated*.  The hypothesis: the Pauli-saturated configuration's mass
differs from "two independent k = 3 triplets" by the deuteron binding
2.22 MeV, with no free parameters.

Phase 10a tests two structural questions before any mass-correction
ansatz is computed:

1. **Geometric.**  Does the (1, 2) eigenmode at the g-candidate
   p-sheet baseline have a localization profile that even *permits*
   six strands to coexist on the torus?
2. **Mechanistic.**  Does R60 T16's back-reaction selection rule (the
   2ω density-cancellation argument that fixed Z₃ in the first place)
   distinguish between candidate N = 6 phase arrangements
   (Z₆ hexagon vs. 2 × Z₃ at various inter-triplet angles)?

Both questions are computable directly without an ansatz.  Findings
below.

Scripts:
[`scripts/track10_phase10a_eigenmode_fit.py`](scripts/track10_phase10a_eigenmode_fit.py) ·
[`scripts/track10_phase10a_back_reaction_U.py`](scripts/track10_phase10a_back_reaction_U.py)
Outputs:
[`outputs/track10_phase10a_density_profile.png`](outputs/track10_phase10a_density_profile.png) ·
[`outputs/track10_phase10a_fit_summary.csv`](outputs/track10_phase10a_fit_summary.csv) ·
[`outputs/track10_phase10a_back_reaction_U.csv`](outputs/track10_phase10a_back_reaction_U.csv)

---

## Phase 10a — Eigenmode geometry and back-reaction capacity at k ≤ 6

### F10a.1. The (1, 2) eigenmode is computable on the curved p-sheet

The Sturm-Liouville eigenvalue problem for a mode
ψ(θ₁, θ₂) = f(θ₁) · exp(i q_eff θ₂) on the curved torus

<!-- d/dθ₁[(1+ε cos θ₁) f'] + [λ(1+ε cos θ₁) − ε² q²/(1+ε cos θ₁)] f = 0 -->
$$
\frac{d}{d\theta_1}\left[(1+\varepsilon\cos\theta_1)\,f'\right]
\;+\;\left[\lambda(1+\varepsilon\cos\theta_1)
- \frac{\varepsilon^2 q_{\text{eff}}^2}{1+\varepsilon\cos\theta_1}\right] f = 0
$$

with `q_eff = n_r − s · n_t = 2 − 0.162037 ≈ 1.838` and the periodic
boundary `f(0) = f(2π)`, was discretized on N = 512 points and solved
as a generalized eigenvalue problem.

Lowest eight eigenvalues at the g-candidate baseline (`ε_p = 0.55`,
`s_p = 0.162037`):

| Index | λ | Identification |
|:-:|:-:|:-:|
| 0 | 0.78 | n_t = 0 ground state |
| **1** | **2.07** | **n_t = 1 (cos-like) — selected** |
| 2 | 3.41 | n_t = 1 (sin-like) |
| 3 | 5.70 | n_t = 2 (cos-like) |
| 4 | 6.39 | n_t = 2 (sin-like) |

The selected n_t = 1 eigenvalue λ = 2.07 matches the flat-torus value
n_t² + ε² q² ≈ 2.02 to within the curvature-induced shift expected at
ε = 0.55.  The mode is solved correctly.

**Density profile** |f(θ₁)|² of the n_t = 1 cos-like mode:

- Peak at **θ₁ = 80°** — the strand sits in the outer-equator quadrant,
  not strictly at θ₁ = 0 as a flat-torus calculation would give, but
  shifted by the metric's `(1 + ε cos θ₁)` weight.
- **FWHM in θ₁ ≈ 83°** — substantial localization in the tube
  direction.

This is informative regardless of what 10a concludes about Pauli
capacity: the (1, 2) primitive is no longer "uniformly spread" on the
sheet; it occupies a localized ribbon that wraps the torus once
poloidally and twice toroidally.

See `track10_phase10a_density_profile.png`.

### F10a.2. The "ribbon overlap" geometric criterion is wrong

The first natural fit criterion — "N parallel ribbons of θ₂-width
2 · FWHM_θ₁ fit if 2π/N ≥ ribbon width" — gives N_max = π/FWHM ≈ 2.17
at the measured FWHM.

This would forbid the proton (N = 3 strands at 120° offsets) at the
g-candidate baseline, which contradicts observation.  The criterion
must therefore be wrong: parallel geodesics on a torus never intersect
in the geometric sense, and "density overlap" alone does not preclude
multiple modes from sharing space when distinguished by quantum
numbers (as in Pauli antisymmetry).

The right capacity question for MaSt is not geometric; it is the
back-reaction selection rule that gave Z₃ confinement in the first
place.

### F10a.3. R60 T16's 2ω back-reaction does not distinguish Z₆ from 2×Z₃

R60 T16 derived Z₃ confinement from a density-cancellation argument:
a single (1, 2) mode has charge density ρ_Q = φ² with a 2ω time-
varying harmonic.  N copies at internal phases {φᵢ} produce a coherent
back-reaction proportional to

<!-- U_2 = Σ_{i<j} cos(2(φᵢ − φⱼ)) = ½(|Σ_i exp(2iφᵢ)|² − N) -->
$$
U_2 \;=\; \sum_{i<j} \cos\bigl(2(\phi_i - \phi_j)\bigr)
\;=\; \tfrac{1}{2}\bigl(|\textstyle\sum_i e^{2i\phi_i}|^2 - N\bigr).
$$

Configurations with U₂ < 0 cancel the 2ω harmonic.  R60 T16 selected
N = 3 at Z₃ phases `(0, 2π/3, 4π/3)` as the minimum stable composite
(U₂ = −1.5).

For N = 6, the candidate arrangements give:

| Arrangement | Phases | U₂ |
|:---|:---|:---:|
| Z₆ hexagon | `(0, π/3, 2π/3, π, 4π/3, 5π/3)` | **−3.00** |
| 2 × Z₃, inter-triplet angle 60° | (= Z₆ structurally) | **−3.00** |
| 2 × Z₃, inter-triplet angle 0° (coincident) | doubled triplet | **−3.00** |
| 2 × Z₃, inter-triplet angle 30° | misaligned | **−3.00** |
| Pauli {color × spin-π} | `(0, 2π/3, 4π/3) ∪ (π, 5π/3, π/3)` (= Z₆) | **−3.00** |
| All aligned | `(0, 0, 0, 0, 0, 0)` | +15.00 |

Every Z₃-respecting arrangement gives the same U₂ = −3 at N = 6.  The
2ω back-reaction sees only the "is each Z₃ triplet internally singlet"
property, which all the candidates share.  **R60 T16's mechanism, as
formulated, cannot supply a binding energy that distinguishes N = 6
from "two independent N = 3"** because both have U₂ = −3 = 2 × (−1.5).

The deuteron remains additive at this level.

### F10a.4. Higher harmonics distinguish, but inconsistently and without a framework selection rule

Beyond m = 2, the harmonic sums separate the configurations:

| Arrangement | U₂ | U₃ | U₄ | U₆ |
|:---|:-:|:-:|:-:|:-:|
| Z₆ hexagon | −3 | **−3** | −3 | **+15** |
| 2 × Z₃ inter = 60° | −3 | −3 | −3 | +15 |
| 2 × Z₃ inter = 0° | −3 | **+15** | −3 | +15 |
| 2 × Z₃ inter = 30° | −3 | **+6** | −3 | **−3** |
| Pauli spin-π Z₃×{0, π} (= Z₆) | −3 | −3 | −3 | +15 |

m = 3 prefers `2×Z₃ at 60° = Z₆` (U₃ = −3) over `2×Z₃ at 0°`
(U₃ = +15) or `at 30°` (U₃ = +6).  m = 6 prefers `2×Z₃ at 30°`
(U₆ = −3) over the Z₆ hexagon (U₆ = +15).  The orderings disagree.

**Two problems with using these harmonics for binding:**

1. **No framework selection.**  R60 T16 specifically derived m = 2
   from `ρ_Q = φ²`; higher m would correspond to higher field-power
   contributions to the density (φ³, φ⁴) that the framework currently
   has no rigorous accounting for.  Picking which harmonic dominates
   would be an *added postulate*.
2. **Inconsistent orderings.**  Even if a particular m were selected,
   m = 3 and m = 6 favor different N = 6 arrangements.  The
   Pauli-saturated configuration (which structurally is Z₆) wins at
   m = 2, 3, 4 but loses at m = 6.  No single-harmonic selection rule
   gives Pauli a clean structural advantage.

The Pauli labelling (color × spin-π) maps the six strands onto
*exactly* the Z₆ hexagon phases.  This is structurally elegant but
does not break the U₂ tie because R60 T16's U₂ already saturates at
−3 for any Z₃-coherent N = 6 arrangement.

### F10a.4b. Modeling correction — spin does not enter the back-reaction phase

The "Pauli spin-π Z₃×{0,π}" mapping in F10a.4 assumes the spin
label enters R60 T16's back-reaction phase as a π shift, sending
the Pauli-saturated 6 strands onto the Z₆ hexagon.  This
assumption is not justified by R60 T16's derivation.

R60 T16 uses charge density `ρ_Q = φ²`.  In Dirac–Kähler (and in
standard QED), `|ψ|²` sums over spinor components and is
**independent of m_s**.  Spin is an orthogonal quantum-number
label to the spatial phase; it does not appear in `ρ_Q`'s
harmonic decomposition.  The Pauli-saturated 6 strands occupy
six distinct `(color, spin)` labels but only **three distinct
color phases**, each with multiplicity 2.  The correct phase
profile is **"doubled Z₃"** — the same as row `2×Z₃ inter=0°`
in F10a.4's table — not the Z₆ hexagon.

Re-reading F10a.4's table with corrected labels:

| Arrangement | U₂ | U₃ | U₄ | U₆ |
|:---|:-:|:-:|:-:|:-:|
| **Pauli-saturated (= doubled Z₃)** | −3 | **+15** | −3 | **+15** |
| Two independent Z₃ triplets (free baryons) | −3 | +6 | −3 | +6 |
| Z₆ hexagon (geometric, no Pauli motivation) | −3 | −3 | −3 | +15 |

The Pauli row matches what was previously labeled `2×Z₃ inter=0°`;
the Z₆ row matches what was previously labeled "Pauli spin-π."

At m = 2 the Pauli configuration is degenerate with two free
triplets (both U₂ = −3), so F10a.3's leading-order conclusion is
unchanged.  At m = 3, 6, 9, … the Pauli configuration has U_m =
+15 versus the two-free-triplet sum of +6 — the Pauli phase
profile is **more positive** by 9 units at every m = 3k harmonic,
i.e. **less stable**, not more.  Higher-order corrections to
R60 T16's `ρ_Q`-coherence mechanism therefore push Pauli-saturation
in the **wrong direction** for binding.

This corrects the F10a.4 narrative: m = 3 does not "prefer Z₆,"
because Z₆ is not the Pauli configuration under R60 T16's actual
operator.  The genuine Pauli configuration loses to two free
triplets at every higher harmonic.

### F10a.5. What Phase 10a establishes

1. **The (1, 2) eigenmode on the curved p-sheet is computable and
   has a well-defined FWHM ≈ 83°**, peaked at θ₁ ≈ 80°.  This is
   the first quantitative localization measurement of the proton's
   primitive on the g-candidate geometry.
2. **The natural geometric capacity criterion ("ribbons overlap →
   forbidden") is the wrong question** — it would forbid the proton
   itself.  Multiple modes can occupy the same spatial region when
   distinguished by quantum numbers.
3. **R60 T16's 2ω back-reaction U₂ does NOT distinguish the
   Pauli-saturated configuration from two free Z₃ triplets** —
   both give U₂ = −3.  The framework's leading-order binding-
   selection mechanism yields *no* mass difference between
   "deuteron Pauli-saturated compound" and "two free nucleons."
4. **Under the corrected spin-orthogonal modeling (F10a.4b),
   higher harmonics push Pauli-saturation in the wrong
   direction.**  At m = 3, 6, 9, … the Pauli phase profile
   (= doubled Z₃) gives U_m = +15 versus +6 for two free
   triplets, making it less stable rather than more.
   Reading B as originally framed (higher-harmonic completion
   of R60 T16's `ρ_Q`-coherence mechanism) cannot supply
   binding — it makes the problem worse.
5. **The phase-coherence channel of `ρ_Q` is exhausted.**  Any
   Ma-internal binding mechanism must come from a different
   operator — one that sees the spin labels directly, which
   `ρ_Q` does not.

### F10a.6. Reading on the Track 10 hypothesis (corrected)

Track 10's framing ("Pauli-saturated coherence has lower mass than
two independent triplets") is degenerate at the leading order of
R60 T16's `ρ_Q`-coherence mechanism (m = 2) and is anti-binding
at higher orders of the same mechanism (m = 3k).  The
phase-coherence channel of `ρ_Q` is closed for binding under the
corrected spin-orthogonal modeling.

The Track 10 framing is not falsified, however — it is redirected.
Pauli-saturation is real (six distinct color-spin labels exist on
a single tuple); R60 T16's `ρ_Q`-coherence operator simply does
not see the spin labels and cannot reward Pauli structure.  A
different operator that *does* see them is the natural next test.

Three readings remain:

**Reading A — honest closure.**  All Ma-internal mechanisms in
the framework's current operator inventory have been exhausted
for binding.  R63 closes with "binding requires framework
extension or a different physics channel."

**Reading B (revised) — exchange-interaction channel.**  D7d's
per-sheet Dirac–Kähler structure provides an antisymmetric Slater
determinant for N strand fermions on a single tuple.  The
expectation value of the same `ρ_Q` operator on the
antisymmetrized 6-fermion wavefunction (Pauli-saturated)
contains exchange terms that the classical phase-coherence sum
U_m does not capture — the U_m sum treats strands as classical
phases, while the Slater determinant carries fermion sign
factors that depend on color-and-spin label overlap.  These
exchange contributions are computable from D7d's existing
machinery without framework extension.  This is the natural
Phase 10b in the corrected picture.

**Reading C — different physics.**  Nuclear binding belongs to
S-space configuration energy or a yet-unidentified sheet-coupling
term.  Same as before; deferred to a successor study.

### F10a.7. What still wants computing

Under Reading B (revised), Phase 10b evaluates `ρ_Q` (or another
appropriate operator) on the antisymmetrized 6-fermion Slater
determinant of (color, spin) labels and compares to the
two-disjoint-3-fermion-Slater configuration.  The mechanical
steps:

1. Construct the 6-fermion Slater determinant from labels
   `(c, s) ∈ {R, G, B} × {↑, ↓}` on the single (1, 2) primitive
   spatial wavefunction.
2. Compute `⟨Ψ_6 | Ô | Ψ_6⟩` for the relevant operator(s); the
   exchange terms (with fermion sign factors from
   antisymmetrization) appear here but not in the classical
   U_m sum.
3. Compute the same expectation value on two disjoint
   3-fermion Slater determinants (each of which is the
   proton's Z₃ singlet structure).
4. Difference is the candidate binding contribution.  Compare
   to deuteron 2.22 MeV.

This stays inside the existing framework (D7d for spinors,
R60 T16 for the operator).  No new postulates.

If Reading B (revised) also returns degenerate or wrong-sign,
Reading A is earned: no Ma-internal mechanism currently in the
framework distinguishes Pauli-saturated 6-fermion compounds
from disjoint 3-fermion compounds, and binding requires either
S-space machinery (Reading C) or a structural extension
(F9a.6's open-question status).

**Phase 10a status: complete (with F10a.4b correction).**
Decision on Reading A vs. B-revised vs. C is the next
conversation step.

---

## Phase 10b — Slater-determinant exchange-interaction verification

**Hypothesis (Reading B-revised).**  D7d's per-sheet Dirac–Kähler
construction provides an antisymmetric Slater determinant for the
Pauli-saturated 6-fermion state on a single (1, 2) p-sheet
primitive.  The expectation value of R60 T16's U_m operator on
this antisymmetrized state may include exchange contributions
that the classical phase-coherence sum F10a.4 doesn't capture.

Script:
[`scripts/track10_phase10b_slater_exchange.py`](scripts/track10_phase10b_slater_exchange.py) ·
Outputs:
[`outputs/track10_phase10b_slater_exchange.csv`](outputs/track10_phase10b_slater_exchange.csv) ·
[`outputs/track10_phase10b_spin_color.csv`](outputs/track10_phase10b_spin_color.csv)

### F10b.1. Slater-determinant U_m equals the classical doubled-Z₃ sum

Computing `⟨Ψ_6 | U_m | Ψ_6⟩` via the Slater-Condon two-body rule
on the Pauli-saturated 6-fermion state with labels
`{R↑, R↓, G↑, G↓, B↑, B↓}` (all sharing the (1, 2) spatial mode):

| m | Slater (quantum) | classical doubled-Z₃ | two free Z₃ triplets | Pauli − two free |
|:-:|:-:|:-:|:-:|:-:|
| 2 | −3.0000 | −3.0000 | −3.0000 | +0.0000 |
| 3 | +15.0000 | +15.0000 | +6.0000 | +9.0000 |
| 4 | −3.0000 | −3.0000 | −3.0000 | +0.0000 |
| 6 | +15.0000 | +15.0000 | +6.0000 | +9.0000 |

The quantum Slater value matches the classical doubled-Z₃ sum at
every harmonic.  **The exchange contribution is identically zero**
for label-diagonal operators like U_m.  This is a direct
consequence of Slater-Condon: a two-body operator V that doesn't
change labels under action gives ⟨ij|V|ji⟩ matrix elements that
cancel the direct contribution's swap-sign, leaving only the
direct sum.

F10a.4b's analysis is now confirmed quantum-mechanically: the
Pauli-saturated configuration is degenerate with two free
triplets at m=2 and **less stable** by 9 units at m=3k harmonics.

### F10b.2. The exchange-interaction channel does not supply binding

Reading B-revised's hypothesis — that antisymmetrization gives
exchange contributions beyond the classical U_m sum — is
falsified for R60 T16's ρ_Q-coherence operator.  The reason is
structural: R60 T16's operator is label-diagonal (depends on
color phases, not on label identity), and label-diagonal
operators have zero Slater-Condon exchange.

The Pauli structure does set the *occupied label set* (forces
six distinct color-spin labels at k=6 saturation), but does not
re-weight the energy expectation value of operators that only
see the color phase — including R60 T16's existing operator.

### F10b.3. Spin-dependent operators distinguish, but lie outside R60 T16

A side calculation tested the mixed spin-color operator
`Σ_{i<j} σ_z(i) σ_z(j) cos(m(c_i − c_j))` on three reference
configurations:

| m | Pauli-saturated | aligned spins | separated spins |
|:-:|:-:|:-:|:-:|
| 2 | −3 | −3 | −3 |
| 3 | −3 | +15 | −3 |
| 4 | −3 | −3 | −3 |
| 6 | −3 | +15 | −3 |

This operator distinguishes Pauli-saturated/separated (both at −3)
from aligned-spin (at +15) at the higher harmonics.  Spin-coupled
operators have non-trivial expectation values on different label
arrangements.  But none of these operators appears in R60 T16's
derivation, which uses only `ρ_Q = |ψ|²` — spin-blind by
construction.  Promoting R60 T16 to a spin-coupled operator
would be a framework extension (a new term in the Lagrangian),
not a completion of the existing one.

### F10b.4. What Phase 10b establishes

1. **The exchange-interaction channel via R60 T16's operator is
   exhausted.**  Slater-Condon gives no exchange contribution
   for label-diagonal V, and U_m is label-diagonal.  The
   Pauli-saturated state's expectation value equals the
   classical doubled-Z₃ result identically.
2. **Reading A is earned within the framework's existing
   operator set.**  No Ma-internal mechanism currently in MaSt
   distinguishes Pauli-saturated 6 strands from two free Z₃
   triplets in the binding direction; in the higher-harmonic
   direction the distinction has the wrong sign.
3. **Spin-coupled operators COULD distinguish, but require
   framework extension.**  The closest in-framework option
   (Reading B-extended) is to add a spin-coupled term to R60
   T16's back-reaction.  This is a structural extension of
   the Lagrangian, not a re-evaluation of an existing
   calculation.
4. **The deuteron-binding question is now decisively outside
   R63's refinement scope.**  The "g-candidate" model — Q132
   v2 + ingredient-sum charge + additive nuclear composition +
   β-decay-consistent neutron — refines model-F's discipline
   but does not derive nuclear binding.  Binding is a separate
   research target.

### F10b.5. Successor-study directions

Three concrete directions for future work, all outside R63:

**Reading B-extended** — add a spin-coupled back-reaction
operator to R60 T16.  Would derive the operator from the same
Dirac–Kähler structure that gives D7d's spin (so it's not a
free-postulate addition), and re-run the Pauli-saturation
calculation with the extended operator.  Sits in Ma; framework
extension required.

**Reading C** — model the S-space configuration energy of
spatially-separated nucleons.  Would import standard nuclear-
force phenomenology (Yukawa pion exchange, etc.) into the
spacetime side of MaSt; aligns with how SM treats binding.
Larger scope; reinvents some SM machinery.

**Reading D (new)** — vacuum polarization of the p-sheet by
multi-baryon compound modes.  Multi-strand compounds polarize
the p-sheet's other modes (mesonic excitations); the
back-reaction is a one-loop / many-mode effect, not a tree-
level KK mass.  Conceptually a closer analog of pion-exchange
binding in nuclei.  Substantial framework extension.

R63 closes here with respect to nuclear binding.  The
g-candidate model is the deliverable; the binding mechanism
remains an open Ma-extension target for a successor study.

---

## Status

**Phase 10b complete.**  Slater-determinant exchange-interaction
channel verified to give zero contribution beyond the classical
sum for R60 T16's existing operator.  Reading A is earned within
the framework's current operator inventory.

Track 10 closes; R63 closes with respect to nuclear binding.
The three successor-study directions (B-extended, C, D) are
all framework extensions that fall outside R63's scope.

---

## Antimatter vs "complementary" — clarification before any 10b

The user asked, before approving Phase 10b, how a Pauli-saturated
"complementary" 6-strand configuration is different from antimatter.
Brief answer:

- **Antimatter on the p-sheet** flips the *signs* of the windings
  `(n_pt, n_pr) → (−n_pt, −n_pr)` and the e-sheet charge.  Mass is
  identical because `μ²` depends on `n²`.  An antiproton has
  `(n_pt, n_pr) = (−3, −6)` on the p-sheet, opposite Z₃ phase
  cycling.
- **Pauli-saturating spin label** keeps the windings unchanged but
  flips the *internal spin phase*: φ_total = θ_color + π · m_s.
  Same `(n_pt, n_pr)`, same energy contribution from the mass
  formula directly; only the back-reaction phase differs.

So the proton's spin-↑ and spin-↓ strands are not antiparticles —
they have the same windings (matter, not antimatter) — but their
internal back-reaction phases are π-shifted.  The Pauli capacity
of 6 = (3 colors × 2 spins) is matter-only; antimatter doubles it
again to 12 conceptually, though that's irrelevant to deuteron
binding.

The "shear/ratio still free in bounds" point is also correct: the
g-candidate baseline (ε_p, s_p) = (0.55, 0.162037) is the working
choice, but Track 5/6 confirmed a wider region is viable.  Phase
10a was run at the baseline; if Reading B is pursued, sweeping
within bounds is permitted as long as the inventory fit is
maintained.

---

## Status

**Phase 10a complete; Track 10 pending decision.**

- Eigenmode geometry on p-sheet: characterized (FWHM 83° at
  baseline).
- Back-reaction U₂ for N = 6 candidate arrangements: all tied at
  −3.  R60 T16's mechanism does not derive deuteron binding.
- Higher-harmonic sums distinguish but lack framework selection.

**Next step is a decision call**: Reading A (close R63 with
"binding requires framework extension"), Reading B (extend R60
T16 to higher harmonics), or Reading C (move binding to S-space
or a different sheet-coupling).
