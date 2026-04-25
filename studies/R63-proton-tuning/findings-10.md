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
   candidate N = 6 arrangements** — Z₆, 2×Z₃ at any inter-triplet
   angle, and Pauli-spin-saturated all give U₂ = −3.  The framework's
   actual binding-selection mechanism therefore yields *no* mass
   difference between "deuteron Pauli-saturated compound" and "two
   free protons + neutron".
4. **Higher harmonics (m = 3, 4, 6) distinguish configurations but
   give inconsistent orderings and have no framework-level reason
   to dominate.**  Selecting one as the binding mechanism would be
   an added postulate, not a derivation.

### F10a.6. Reading on the Track 10 hypothesis

Track 10's framing ("Pauli-saturated coherence has lower mass than
two independent triplets, deriving the deuteron binding without free
parameters") **does not survive Phase 10a as posed**.  The framework's
ω-cancellation rule treats Z₆ and 2×Z₃ identically, and Pauli-
saturation maps onto Z₆ structurally.

Three readings of this result are available; choosing among them is
the user-and-reviewer call:

**Reading A (honest closure).**  The strong-force-in-Ma hypothesis
is falsified at the level the framework currently supports.
R60 T16's 2ω cancellation is rigid enough to select N = 3 (the
proton) but degenerate at N = 6 (cannot select a unique deuteron
configuration).  If the framework's existing rigidity is taken as
authoritative, Track 10 closes the candidate-mechanism list, and
"binding requires framework extension" (F9a.6) is now earned.

**Reading B (extend the cancellation rule).**  Promote the
density-cancellation argument from "cancel 2ω" to "cancel an
infinite tower".  Define an effective coherence energy

<!-- U_eff = Σ_m w_m U_m -->
$$
U_{\text{eff}}(\{\phi_i\}) = \sum_{m \geq 2} w_m U_m(\{\phi_i\})
$$

with weights `w_m` to be derived from a higher-order analysis of
ρ_Q at multi-mode interaction.  This is *not* a free-parameter fit —
the weights would come from a re-derivation of R60 T16 carried to
higher orders in φ.  It is a framework extension within Ma but
beyond what currently exists.

**Reading C (different physics).**  Nuclear binding is not in the
phase-coherence channel of Ma at all.  The 2ω rule is exhausted at
N = 3, and additional structure at N = 6 belongs to S-space (spatial
configuration energy of nucleon centers) or to a yet-unidentified
sheet-coupling term.  Track 9's framework-extension note in F9a.6
is what's earned.

### F10a.7. What still wants computing

If Reading B is pursued, the natural Phase 10b would derive `w_m`
from a higher-order treatment of `ρ_Q = (Σ_i φ_i)²` for k coherent
strands — the cross-terms produce harmonics beyond 2ω whose
back-reaction *is* in principle computable from the same framework
that produced R60 T16, just at higher order in the φ expansion.

If Reading A or C is accepted, Track 10 closes here with the
finding that *no Ma-internal mechanism currently in the framework
supplies a binding-energy distinction at k = 6 strands*.

**Phase 10a status: complete.**  Decision on Reading A vs. B vs. C
is the next conversation step, not a unilateral closure.

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
