# work-ch9.md — Ratio and shear together: a general model of a particle sheet (Ch 9 scoping)

This file scopes a new **Chapter 9** that brings ratio ε ([Ch 7](07-aspect-ratio-and-character.md)) and shear σ_uw ([Ch 8](08-shear-and-fractional-charge.md)) together into a unified treatment of the (σ, ε) parameter space. The chapter's mission: produce a *general model of a particle sheet* — characterizing how the two metric parameters jointly determine which closure-satisfying configurations dominate, what the sheet's structural character is, and how the framework's three qualitative sheet types (lepton-like, neutrino-like, hadronic-like) emerge as different regions of the combined landscape.

Ch 9 is the substrate for the eventual downstream exercise: given a sheet's measured properties, derive the metric values (diagonals + cross-term) for that sheet. Metric-charge does not handle specific sheets; Ch 9 provides the structural model from which sheet-specific work can build.

The σ-alone analysis (what shear does to a single sheet's spectrum, gauge structure, multi-link inventory) is scoped in [work-m8a.md](work-m8a.md) and stays in Ch 8. The ε-alone analysis is in current [Ch 7](07-aspect-ratio-and-character.md). Ch 9 builds on both.

Conventions follow the rest of the project ([Ch 1](01-foundation.md): u = ring, w = tube; ε ≡ L_u/L_w). M ≡ (ℏ/c)·(2π/L_w) is the natural mass scale.

**Naming note.** This file uses σ as the working symbol for the metric off-diagonal throughout §§2–6, consistent with [Ch 1 §4](01-foundation.md)'s convention. Where §7 contrasts parametrizations using "View A vs View B" language, View A corresponds to Ch 1's σ_uw (metric-shear, the framework's primary parametrization) and View B corresponds to Ch 1's s (lattice-shear, used for R-track-study correspondence).

---

## Sections

| § | Topic |
|---|-------|
| 1 | The Ch 9 question |
| 2 | The combined (σ, ε) parameter space |
| 3 | The single-axis dominance puzzle |
| 4 | The σ → 1 principal-axis suppression mechanism |
| 5 | Three structural regimes by combined (σ, ε) |
| 6 | Three sheet types — qualitative correspondence |
| 7 | The σ → 1 mechanism and translation to s-form for empirical correspondence |
| 8 | Open questions for Ch 9 |
| 9 | Recommendations |

---

## 1. The Ch 9 question

Chapters 7 and 8 treat ratio and shear as independent parameters. But the framework's three qualitative sheet types — lepton-like, neutrino-like, hadronic-like — each correspond to a *specific combination* of σ and ε, not to a single parameter alone:

- The lepton-like sheet's character (single isolable charged primitive at mass M, substantial parity violation) needs **both** large ε *and* substantial σ — neither alone suffices.
- The neutrino-like sheet's character (near-degenerate chirality-flipped pairs, oscillation behavior) needs **both** ε near 1 *and* σ near zero — substantial σ would destroy the degeneracy.
- The hadronic-like sheet's 3-component structure needs **both** small ε *and* moderate σ — the empirical k = 3 finding (per production studies) is contingent on this combination.

Neither Ch 7 (ratio alone) nor Ch 8 (shear alone) can derive these joint structural patterns. A unified treatment is needed.

The Ch 9 question is therefore: **given the (σ, ε) parameter space and the structural mechanisms each parameter introduces, how does the combined landscape produce the qualitatively different sheet types?** The chapter's job is to map the parameter space, identify the regimes, characterize each regime's sheet character, and provide the substrate from which downstream "metric from observables" work can derive specific sheets.

---

## 2. The combined (σ, ε) parameter space

### 2.1 Two parameters, multiple combinations

The sheet metric has two free parameters: ε ≡ L_u/L_w (ratio) and σ ≡ σ_uw (shear). Useful combinations:

- **σε product** — selects the lightest closure-satisfying primitive's ring-winding (m_opt = round(σε); see [work-m8a.md §4](work-m8a.md)).
- **ε alone** — controls relative weight of single-axis modes (m, 0) vs (0, n).
- **σ alone** — controls chirality-bias amplitude (R_w-conjugate split between (m, n) and (m, −n)).
- **(1−σ²)⁻¹** — global mass-scaling factor in View A; replaced by no boundary in View B (§7).

The "structural levers" of the landscape:

| Combination | What it controls |
|---|---|
| σε | m_opt for closure-satisfying primitive |
| ε | single-axis-vs-closure-satisfying competition |
| σ | chirality-bias / matter-antimatter-pair-degeneracy |
| (1−σ²)⁻¹ | global mass scale (View A only) |

### 2.2 The σε product result, restated

From [work-m8a.md §4](work-m8a.md): the lightest closure-satisfying T(m, 1) primitive has μ²(m, 1) = (m/ε − σ)² + (1 − σ²), minimized at m = σε with μ²_min = 1 − σ². When σε is integer, this gives physical mass exactly M = (ℏ/c)·(2π/L_w), independent of σ.

This is the central derivable result tying σ and ε together at the linearized level. It says **the σε product is the primary structural variable for closure-satisfying primitives**, not σ alone or ε alone.

### 2.3 Where the σε result is parametrization-specific

The "mass exactly M at integer σε" cancellation arises because the (1−σ²)⁻¹ overall factor exactly cancels the parabola's (1−σ²) bottom value. This cancellation is specific to the metric-shear (View A) parametrization where the (1−σ²)⁻¹ factor appears — which is the framework's primary parametrization per [Ch 1 §4](01-foundation.md). When predictions are translated to s for R-track-study correspondence, the translation is non-trivial at large σ (see §7); the σε result and the cleanest σ → 1 statements live in View A.

---

## 3. The single-axis dominance puzzle

### 3.1 Statement of the puzzle

At any (σ, ε), the lightest single-axis modes are (1, 0) at μ² = 1/ε² and (0, 1) at μ² = 1.

| ε regime | Lightest single-axis | Lightest closure-satisfying | Which is lighter? |
|---|---|---|---|
| ε < 1 | (0, 1) at 1 | T(m_opt, 1) at 1−σ² | T(m_opt, 1) for σ > 0 |
| ε > 1 | (1, 0) at 1/ε² | T(m_opt, 1) at 1−σ² | (1, 0) unless σ > √(1 − 1/ε²) |
| ε ≫ 1 | (1, 0) at ≈ 0 | T(m_opt, 1) at 1−σ² | (1, 0) *much* lighter |

For ε > 1, single-axis (1, 0) is the unique lightest mode and becomes massless as ε → ∞. Single-axis modes are mass-only by the structural-degeneracy mechanism of [Ch 4](04-the-closure-condition.md) — no chirality structure on the curve, no spacetime↔compact gauge potential.

**Yet the framework wants charged sheets at extreme ε** (the lepton-like sheet's empirical large-ε identification, per MaSt model-F). Linear theory says single-axis modes are *much* lighter; the lowest-energy excitations are mass-only, not charged.

This is the architectural question that current [Ch 7 §4.3](07-aspect-ratio-and-character.md) flags but does not resolve. It is *the* core question Ch 9 has to engage: **why does an extreme-ε sheet host charged states as its physical particles when single-axis modes are lighter?**

### 3.2 Candidate resolutions

(a) **Single-axis modes are not "particles" in the sheet-physical sense.** They may be the sheet's "background" or "vacuum" structure rather than excitations corresponding to observed particles. Charged states are excitations *above* this background.

(b) **Substrate-level constraint projects out single-axis modes.** Grid-duality's wrap-promotion ladder may require both windings nonzero for a configuration to count as a sheet-physical particle. The framework would inherit this projection.

(c) **Framework prediction differs from observation.** Single-axis dominance at large ε is genuinely predicted; model-F's electron-sheet ε identification is wrong; the framework predicts something different about extreme-ε sheets.

(d) **σ → 1 principal-axis suppression.** As σ approaches 1 (in View A), single-axis masses diverge faster than closure-satisfying masses, suppressing single-axis as low-energy excitations. Developed rigorously in §4 below.

Mechanism (d) is the cleanest *structural* candidate the framework offers. It is a combined (σ, ε) mechanism — neither σ alone nor ε alone produces the suppression — and is therefore properly Ch 9's concern.

---

## 4. The σ → 1 principal-axis suppression mechanism

**The claim:** at σ → 1, the lightest closure-satisfying T(m, 1) primitive's mass approaches a finite limit while single-axis modes (1, 0), (0, 1) diverge as (1−σ²)⁻¹. This would single out closure-satisfying modes as the dominant low-energy excitations near the metric boundary.

**Setup.** Take σ → 1 with σ = 1 − δ, δ → 0⁺. Then (1−σ²) = δ(2−δ) ≈ 2δ.

### 4.1 Single-axis modes near the boundary

<!-- m²_phys(1, 0) ≈ M²/(2ε²δ) → ∞ -->
$$
m^2_\text{phys}(1, 0) \;\approx\; \frac{M^2}{2\varepsilon^2\,\delta} \;\to\; \infty,
\qquad
m^2_\text{phys}(0, 1) \;\approx\; \frac{M^2}{2\delta} \;\to\; \infty
$$

Both diverge as 1/δ.

### 4.2 Closure-satisfying primitive near the boundary

Optimum m at σ = 1 − δ: m_opt = σε = (1−δ)·ε ≈ ε. Take m̂ = round(ε). Residual Δ ≡ m̂/ε − σ.

**Case A: ε is integer.** m̂ = ε exactly, m̂/ε − 1 = 0, Δ = δ. Residual squared: δ². Divided by 1−σ² ≈ 2δ: δ/2 → 0.

<!-- m²_phys(m̂, 1) → M² as δ → 0 at integer ε -->
$$
m^2_\text{phys}(\hat m, 1) \;\to\; M^2 \quad\text{as}\quad \delta \to 0,\ \varepsilon\in\mathbb{Z}
$$

**Closure-satisfying primitive stays at exactly M while single-axis diverges.** Total suppression.

**Case B: ε is not integer.** Δ_0 = m̂/ε − 1, fixed nonzero with |Δ_0| ≤ 1/(2ε). Residual squared at small δ: ≈ Δ_0². Divided by 1−σ² ≈ 2δ: Δ_0²/(2δ) → ∞.

<!-- m²_phys(m̂, 1) ≈ M²·Δ_0²/(2δ) for non-integer ε -->
$$
m^2_\text{phys}(\hat m, 1) \;\approx\; \frac{M^2\Delta_0^2}{2\delta}
$$

Both modes diverge. Compare rates:

<!-- m²_phys(m̂, 1)/m²_phys(1, 0) = Δ_0²·ε² ≤ 1/4 -->
$$
\frac{m^2_\text{phys}(\hat m, 1)}{m^2_\text{phys}(1, 0)} \;=\; \Delta_0^2\cdot\varepsilon^2 \;\le\; \frac{1}{4}
$$

**Closure-satisfying mass-squared is at most 1/4 of (1, 0) mass-squared** — factor 2 lighter in mass, still divergent.

### 4.3 Summary of σ → 1 suppression

| ε | Closure-satisfying mass at σ → 1 | Single-axis mass | Suppression |
|---|---|---|---|
| Integer | M (finite) | ∞ | **Total** |
| Non-integer, ε ≫ 1 | Diverges; at most 1/(2ε) of (1, 0) mass | ∞ | Strong (ε-suppressed) |
| Non-integer, ε ≈ 1 | Diverges; factor 1/2 lighter than (1, 0) | ∞ | Weak |
| Non-integer, ε ≪ 1 | Diverges; (0, 1) competitive | ∞ | Mode-specific |

**The mechanism works cleanly at integer ε, partially at large ε.** It requires σ near 1 *and* ε near integer (or ε ≫ 1).

### 4.4 Translation to s-form for empirical correspondence

§4's derivation is entirely in metric-shear (View A) — and per [Ch 1 §4](01-foundation.md), View A is the framework's primary parametrization. The (1−σ²)⁻¹ factor that drives the suppression is structural to that choice.

For empirical correspondence with R-track studies (which work in s-form), structural predictions must be translated to s using the σ = s·ε transform documented in [Ch 1 §4](01-foundation.md). The translation is straightforward at small σ but **non-trivial at large σ near the |σ_uw| < 1 boundary** — the σ ↔ s relationship diverges at second order (see §7). Whether the σ → 1 suppression mechanism's quantitative predictions (suppression rates, mass ratios at non-integer ε) survive the translation cleanly enough to match the studies' lepton-like-sheet parameter region is an open quantitative question for Ch 9. §7 develops the transform.

---

## 5. Three structural regimes by combined (σ, ε)

Schematic partition of the (σ, ε) plane:

**Regime I — small σ, ε ≈ 1 (near-symmetric, near-bare).**
- Closure-satisfying T(1, 1) at μ² ≈ 2 − 2σ ≈ 2.
- Single-axis (1, 0) and (0, 1) both at μ² = 1.
- Chirality-bias (R_w-conjugate split between (m, n) and (m, −n)) small (∝ σ).
- m_opt = 1.

Sign-conjugate pairs (m, n) ↔ (−m, −n) mass-degenerate (R_J). R_w-conjugate pairs near-mass-degenerate at small σ. A configuration prepared as a chirality-eigenstate is near a mass-eigenstate; small σ drives oscillation between them. Sign-conjugate cancellation pairs of [Ch 6 §4](06-handedness-and-pairs.md) are cleanly mass-only with very small chirality field T_uw.

**Regime II — small σ, ε ≪ 1 (thin sheet, near-bare).**
- T(1, 1) heavy: μ² ≈ 1/ε² (dominated by 1/ε² for small ε).
- (0, 1) light: μ² = 1.
- (1, 0) very heavy: μ² = 1/ε².
- σε ≪ 1, m_opt = 1.

Single-axis (0, 1) dominates the lowest-energy spectrum. Closure-satisfying tier high-mass. The architectural question (§3) applies in its sharpest form.

**Regime III — σ near 1, large ε (wide sheet, sheared near boundary).**
- T(m_opt, 1) at mass ≈ M (m_opt = round(σε), large integer).
- Single-axis modes scaled out by (1−σ²)⁻¹ (the §4 mechanism).
- Substantial chirality bias.
- Many T(m, 1) primitives near m_opt have similar masses (residual ~ 1/ε² is small).

The σ → 1 principal-axis suppression activates; closure-satisfying becomes the dominant low-energy tier. This is the regime where charged-sheet character is structurally clean.

**Regime IV — σε ≈ k + 1/2 (level crossings).**
At half-integer σε, two adjacent T(m, 1) primitives are mass-degenerate. The sheet hosts a near-degenerate pair of closure-satisfying primitives, separated from the third-closest by residual ~ 1/ε². For ε ≫ 1, three primitives sit at nearly the same mass (no exact three-fold degeneracy per [work-m8a.md §4.4](work-m8a.md), but spread ~ 1/ε² which is small).

---

## 6. Three sheet types — qualitative correspondence

The framework needs to accommodate three structurally distinct sheet types. **The analysis below is qualitative.** Quantitative engagement requires the σ → 1 mechanism's translation to s-form for empirical correspondence (§7), carrying out the φ⁴ inter-component calculation ([work-m8a.md §6.5](work-m8a.md)), and computing the neutrino oscillation period explicitly. The parametrization itself is already settled at [Ch 1 §4](01-foundation.md); §7 below addresses the remaining quantitative-translation question.

### 6.1 Lepton-like sheet — "principal-axis-aligned charge"

A single isolable charged primitive at moderate mass, no fractional decomposition, well-defined chirality.

**Structural fit:** σ near 1, large ε (Regime III).

- T(m_opt, 1) at mass M, with m_opt = round(σε) — a specific large integer.
- Single-axis modes scaled out by (1−σ²)⁻¹ → ∞.
- Substantial chirality bias (R_w-conjugate split between (m_opt, 1) and (m_opt, −1)).
- Single-particle character (one lightest closure-satisfying primitive, others heavier).

**Why high ε?** Large ε lets σ approach 1 with σε large, giving m_opt = a specific large integer. Plus residual ~ 1/ε is small.

**Why σ near 1?** Activates the principal-axis suppression that pushes single-axis out of the relevant spectrum.

**Why single-particle?** At m_opt isolated as lightest, multi-link configurations cost k × M, Boltzmann-suppressed.

The architectural question of §3 is resolved here by mechanism (d). This is the cleanest structural picture metric-charge can offer for the lepton-like sheet. Given [Ch 1 §4](01-foundation.md)'s commitment to σ_uw (View A) as the framework's parametrization, the mechanism is well-defined; the open quantitative question is whether its predictions translate to s-form (used by R-track studies) cleanly enough at large σ to match empirical sheet character — see §7.

### 6.2 Hadronic-like sheet — "near-3-fold-degenerate charge tower"

Multiple closure-satisfying primitives at similar masses, with a 3-component structure that the framework needs to derive (the empirical finding is k = 3 at the proton sheet's (σ, ε), per the production studies).

**Structural fit:** ε ≪ 1, σ moderate (Regime II adjacent).

Linear theory at this regime:
- T(1, 1) at μ² ≈ 1/ε² — heavy because ε is small.
- (0, 1) at μ² = 1 — heavy in absolute terms but lighter than T(1, 1).
- m_opt = round(σε) ≈ 0 → 1. T(1, 1) is the lightest closure-satisfying primitive.
- Adjacent T(m, 1) primitives heavier (T(2, 1) at μ² ≈ 4/ε², etc.).

**Linear theory does not produce 3-component organization at this regime.** The hadronic-like 3-quark structure must come from a mechanism outside pure linear theory:

- **(a) Internal-mode dynamics with σ-induced coupling.** The φ⁴ self-interaction calculation per [work-m8a.md §6.5](work-m8a.md), evaluated at the proton sheet's (σ, ε). If k = 3 minimizes, the framework derives the structure.
- **(e) Lattice-shear basis rephrasing.** In View B (§7), the "shortest closure-satisfying curve" at the proton's (σ, ε) may *be* a 3-component configuration when expressed in lattice-shear-basis integer labels.

If neither (a) nor (e) yields k = 3, the framework forwards to substrate Z_3 from grid-duality.

This is the calculation Ch 9 (and the φ⁴ work) needs to attempt before committing to a forwarding stance.

### 6.3 Neutrino-like sheet — "near-degenerate chirality pairs"

Mass-without-charge behavior with paired structure that produces oscillation/cancellation.

**Structural fit:** σ very small, ε near 1 (Regime I).

**Mechanism α — chirality-pair mixing.** At σ very small, T(1, 1) and T(1, −1) are nearly mass-degenerate. The R_u-symmetrization basis differs from the mass-eigenstate basis; a chirality-eigenstate oscillates between mass-eigenstates with period ∝ 1/Δm ∝ 1/σ. As σ → 0, period diverges; as σ grows, oscillation accelerates. Structural pattern of neutrino oscillation.

**Mechanism β — sign-conjugate pair cancellation.** [Ch 6 §4](06-handedness-and-pairs.md)'s sign-conjugate pair (m, n) + (−m, −n) at equal amplitudes has gauge potentials canceling. This mechanism is σ-independent in its operation, but at small σ the chirality field T_uw is small (∝ σ) — so the cancellation pair is *more cleanly mass-only* than on a high-σ sheet.

Combined picture: small σ + ε near 1 gives sign-conjugate pairs (mass-only) plus chirality-pair near-degeneracy (oscillation). **Tiny σ is structurally necessary for the neutrino-like character.** Substantial σ would break the near-degeneracy and eliminate oscillation.

### 6.4 What's needed for quantitative engagement

The qualitative patterns are what linear theory + the §4 σ → 1 mechanism + the small-σ near-degeneracy supports. Quantitative engagement requires:

- **Lepton-like:** rigorous σ → 1 analysis at non-integer ε, plus translation of the σ → 1 predictions to s-form for empirical correspondence with R-track studies (§7). The σ_uw ↔ s transform diverges at second order, so verifying that the structural picture survives the translation at large σ is the substantive quantitative work.
- **Hadronic-like:** the φ⁴ inter-component coupling calculation at the proton sheet's (σ, ε), with the prediction "k = 3 minimizes" tested explicitly.
- **Neutrino-like:** oscillation period from σ computed explicitly and checked structurally against observed magnitudes.

Each of these is a concrete tractable calculation; together they constitute the work that converts Ch 9 from a structural map to a quantitative framework.

---

## 7. The σ → 1 mechanism and translation to s-form for empirical correspondence

The parametrization choice is settled at the framework level. [Ch 1 §4](01-foundation.md) commits to σ_uw (bare σ as shorthand) as the working parametrization, with the lattice-shear coefficient s = σ_uw/ε used as the translation label for R-track-study correspondence. The two are different numbers (not interchangeable; the transform is documented in Ch 1 §4) describing the same physical sheet. **|σ_uw| < 1 is a binding positive-definiteness requirement**, not a parametrization artifact.

This is effectively a "use both with translation rules, σ_uw primary" settlement, made at the Ch 1 framing level rather than at Ch 9. For Ch 9, the substantive remaining question is not which parametrization to adopt — that's settled — but rather **whether the §4 σ → 1 principal-axis suppression mechanism's quantitative predictions survive translation to s-form for empirical correspondence at large σ**, where the σ_uw ↔ s transform diverges at second order.

### 7.1 The two parametrizations

**Metric-shear (View A — framework primary):** sheared metric, rectangular periodicity. The dispersion (with the (1−σ²)⁻¹ overall factor):

<!-- μ²_A_phys = (1/(1-σ²))(m²/ε² - 2σmn/ε + n²) -->
$$
\mu^2_{A, \text{phys}}(m, n;\,\sigma, \varepsilon) \;=\; \frac{1}{1-\sigma^2}\Bigl[\tfrac{m^2}{\varepsilon^2} - \tfrac{2\sigma\,m n}{\varepsilon} + n^2\Bigr]
$$

**Lattice-shear (View B — used by R-track studies for correspondence):** flat metric, sheared periodicity. Basis vectors e_1 = (L_u, 0), e_2 = (sL_u, L_w). The studies' dispersion:

<!-- μ²_B = (n_t/ε)² + (n_r - s·n_t)² -->
$$
\mu^2_B(n_t, n_r;\,s, \varepsilon) \;=\; \tfrac{n_t^2}{\varepsilon^2} + (n_r - s\,n_t)^2 \;=\; \tfrac{n_t^2}{\varepsilon^2} + n_r^2 - 2s\,n_t n_r + s^2\,n_t^2
$$

### 7.2 First-order match, second-order divergence

Matching the linear-in-shear cross-term:

<!-- s = σ/ε at first order, with (n_t, n_r) = (m, n) -->
$$
-2s\,n_t\,n_r \;=\; -\tfrac{2\sigma\,m\,n}{\varepsilon} \;\implies\; s = \tfrac{\sigma}{\varepsilon}
$$

At first order: σ = s·ε.

At second order, expanding View A in σ²: + σ²·(m²/ε² + n²). View B at order s²: + s²·m² = + (σ/ε)²·m² = σ²·m²/ε².

**Difference at order σ²:** View A has extra σ²·ε²·n² that View B doesn't (after substituting s = σ/ε). For closure-satisfying primitives T(m, 1): n = 1, so the difference is σ²·ε² per mode — *substantial* at large ε and not small σ. The empirical lepton-like sheet (small ε, large s in studies' fit) sits in the regime where this divergence is non-trivial: studies fit "s" of order unity at large ε (s·ε of order hundreds), whereas σ_uw stays bounded by 1. The two parameters describe the same physical sheet but the numerical values differ substantially.

### 7.3 The open quantitative question — translation at large σ

The σ → 1 principal-axis suppression of §4 is the framework's main structural candidate for resolving the single-axis-dominance puzzle on extreme-ε sheets. It is in View A by construction — the (1−σ²)⁻¹ factor is what scales single-axis masses up faster than closure-satisfying masses near the metric boundary.

Translating this structural picture to s-form for empirical correspondence is mechanical at small σ (σ ≈ s·ε, second-order corrections small) but **substantively non-trivial at large σ** near the |σ_uw| < 1 boundary, where the σ²·ε²·n² discrepancy between the two parametrizations dominates. The open quantitative question for Ch 9 is:

- **Does the σ → 1 mechanism's predicted sheet character (single charged primitive at mass M, single-axis modes suppressed, substantial chirality bias) survive the σ → s translation at the large-σ regime where the lepton-like sheet's empirical s-values are reported?**
- **If yes:** the framework predicts the lepton-like sheet quantitatively. If no, either (i) the σ → 1 mechanism is the wrong candidate for the architectural question of §3 and another resolution (a)/(b)/(c) must be pursued, or (ii) the empirical s-values from studies require re-interpretation under the σ_uw parametrization.

The question is substantive because the σ → 1 mechanism is the load-bearing piece for the lepton-like sheet's character in §6.1. Without it, that sheet's structural picture rests on architectural-question resolutions (a)–(c) that the framework has not concretely worked out.

§7's payload for Ch 9: confirm the parametrization settlement from Ch 1 §4 (above), present the σ_uw ↔ s transform with its first-order match and second-order divergence (§7.1, §7.2), and frame the σ → 1 translation as the substantive quantitative work remaining (§7.3). The mathematical content of §§7.1–7.2 is needed because the translation analysis at large σ uses it.

---

## 8. Open questions for Ch 9

### 8.1 Single-axis dominance resolution (commit to mechanism)

§3.2's candidates (a)–(d). Mechanism (d) is the framework's cleanest *structural* option but depends on View A. The chapter must commit to one resolution or explicitly leave open with consequences spelled out.

### 8.2 Hadronic 3-component derivation

§6.2 identifies the φ⁴ inter-component coupling calculation ([work-m8a.md §6.5](work-m8a.md)) as the load-bearing piece. If the calculation yields k = 3 at the proton's (σ, ε), the framework derives the 3-quark structure. If not, forwarding to grid-duality.

### 8.3 σ → 1 mechanism's translation to s-form at large σ

The parametrization is settled at Ch 1 (σ_uw primary, s = σ_uw/ε for studies' correspondence). The open quantitative question is whether the §4 σ → 1 suppression mechanism's predictions translate cleanly to s-form at large σ — where the second-order divergence between σ_uw and s is non-trivial — to match empirical lepton-like-sheet parameter values from R-track studies (§7.3). This is the most consequential single open question for the lepton-like sheet's quantitative engagement.

### 8.4 Neutrino oscillation period

§6.3's mechanism α gives oscillation period ∝ 1/σ but needs explicit time-evolution calculation: chirality-eigenstate prepared as (cos θ)·(m,n) + (sin θ)·(m,−n), evolved under the sheared dispersion, period identified.

### 8.5 Towards "metric from observables"

Ch 9's end-state should equip downstream work to plug in a sheet's measured properties (mass, gauge structure, observable charge) and derive (σ_uw, ε) — i.e., invert the structural map. The inversion's invertibility depends on the framework's having committed to:

- The natural-particle definition under shear (single Bloch mode per [work-m8a.md §2.3](work-m8a.md), committed in [Ch 8 §2.2](08-shear-and-fractional-charge.md)).
- The multi-link interpretation (Configuration Y, committed in [Ch 8 §5.2](08-shear-and-fractional-charge.md)).
- The single-axis-dominance resolution mechanism (§3.2 candidates (a)–(d)).
- The k-selection mechanism (or its forwarding, per [Ch 8 §6.5](08-shear-and-fractional-charge.md)).
- The σ → 1 mechanism's translation behavior for s-form correspondence (§7.3).

The parametrization itself is already committed at Ch 1 (σ_uw primary, s for studies' correspondence). With the remaining commitments above, the map (σ_uw, ε) → sheet character becomes derivable and invertible. The actual "metric from observables" exercise is downstream of Ch 9 and may warrant its own chapter or follow-on project.

---

## 9. Recommendations

### 9.1 Carry out the φ⁴ inter-component coupling calculation

[work-m8a.md §6.5](work-m8a.md) outlines the calculation. The result determines whether Ch 9 derives the hadronic 3-component structure or forwards it. Most consequential single piece of work for the chapter.

### 9.2 Develop the σ → 1 suppression for non-integer ε, and its s-form translation

§4.3 has the integer-ε case clean and the non-integer case at "partial suppression with factor 1/(2ε)." For lepton-like sheets at non-integer ε near σ = 1, whether this partial suppression is sufficient for the empirical character is an open quantitative question. Then translate the suppression's predictions to s-form per §7.3 and check against R-track studies' lepton-like-sheet parameter region.

### 9.3 Compute the neutrino oscillation period

§8.4's calculation is straightforward at the linearized level. Carrying it out gives the framework a quantitative structural prediction (oscillation period as a function of σ).

### 9.4 Add Ch 9 to the project's chapter list

Update [README.md](README.md)'s chapter list. Update [Ch 7 §8](07-aspect-ratio-and-character.md) and [Ch 8 §9](08-shear-and-fractional-charge.md) "What's next" pointers to direct to Ch 9 before the closing summary.

### 9.5 Re-scope Ch 7 and Ch 8 to forward combined-parameter content to Ch 9

Ch 7 (ratio alone) and Ch 8 (shear alone) currently each gesture at combined-parameter character. With Ch 9 added, each chapter should keep its single-parameter analysis tight and forward the combined story to Ch 9. The Ch 8 refactor scope is in [work-m8a.md §8](work-m8a.md). A parallel scoping for Ch 7's tightening may be worth doing.
