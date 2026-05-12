# work-ch9.md — Ratio and shear together: a general model of a particle sheet (Ch 9 scoping)

This file scopes a new **Chapter 9** that brings ratio ε ([Ch 7](07-aspect-ratio-and-character.md)) and shear σ_uw ([Ch 8](08-shear-and-fractional-charge.md)) together into a unified treatment of the (σ, ε) parameter space. The chapter's mission: produce a *general model of a particle sheet* — characterizing how the two metric parameters jointly determine which closure-satisfying configurations dominate, what the sheet's structural character is, and how the framework's three qualitative sheet types (lepton-like, neutrino-like, hadronic-like) emerge as different regions of the combined landscape.

Ch 9 is the substrate for the eventual downstream exercise: given a sheet's measured properties, derive the metric values (diagonals + cross-term) for that sheet. Metric-charge does not handle specific sheets; Ch 9 provides the structural model from which sheet-specific work can build.

The σ-alone analysis (what shear does to a single sheet's spectrum, gauge structure, multi-link inventory) is scoped in [work-m8a.md](work-m8a.md) and stays in Ch 8. The ε-alone analysis is in current [Ch 7](07-aspect-ratio-and-character.md). Ch 9 builds on both.

Conventions follow the rest of the project ([Ch 1](01-foundation.md): u = ring, w = tube; ε ≡ L_u/L_w). M ≡ (ℏ/c)·(2π/L_w) is the natural mass scale.

**Naming note.** This file predates [work-discipline.md](work-discipline.md). Where it discusses parametrization in "View A vs View B" terms (§7), View A's shear corresponds to work-discipline's bare σ and View B's shear corresponds to work-discipline's s. The structural content is unchanged; only the labels differ. When this file is consumed by the eventual Ch 9 writing, View A's σ → bare σ and View B's s → s (already aligned with studies' usage).

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
| 7 | Parametrization choice — View A vs View B |
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

The "mass exactly M at integer σε" cancellation arises because the (1−σ²)⁻¹ overall factor exactly cancels the parabola's (1−σ²) bottom value. This cancellation is specific to the metric-shear (View A) parametrization where the (1−σ²)⁻¹ factor appears. In the lattice-shear (View B) parametrization scoped in §7, the cancellation does not arise the same way; the σε analog needs to be redone in View B if View B is adopted.

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

### 4.4 The View B caveat

§4's derivation is entirely in metric-shear (View A). View B has no σ → 1 boundary — the (1−σ²)⁻¹ divergence does not exist. The principal-axis suppression mechanism *as formulated here* does not transfer to View B.

Whether an analogous "large-s" suppression mechanism exists in View B is an **open question that Ch 9 must address before the parametrization commitment of §7 is final.** If §7 adopts View B and the suppression mechanism evaporates, the single-axis-dominance puzzle (§3) loses its main candidate resolution; another resolution mechanism must be identified or the puzzle accepted as open.

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

The framework needs to accommodate three structurally distinct sheet types. **The analysis below is qualitative.** Quantitative engagement requires resolving the parametrization issue (§7), carrying out the φ⁴ inter-component calculation ([work-m8a.md §6.5](work-m8a.md)), and computing the neutrino oscillation period explicitly.

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

The architectural question of §3 is resolved here by mechanism (d). This is the cleanest structural picture metric-charge can offer for the lepton-like sheet — *if* View A is the framework's parametrization (§7).

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

- **Lepton-like:** rigorous σ → 1 analysis at non-integer ε, plus resolution of the parametrization issue (§7). The empirical "shear" parameter from studies may not directly correspond to σ_uw.
- **Hadronic-like:** the φ⁴ inter-component coupling calculation at the proton sheet's (σ, ε), with the prediction "k = 3 minimizes" tested explicitly.
- **Neutrino-like:** oscillation period from σ computed explicitly and checked structurally against observed magnitudes.

Each of these is a concrete tractable calculation; together they constitute the work that converts Ch 9 from a structural map to a quantitative framework.

---

## 7. Parametrization choice — View A vs View B

The framework's σ_uw is bounded by |σ| < 1 (positive-definiteness of the (u, w) block). Production studies (R60, R63, R64) use a shear parameter s with no such bound. The two are related but **non-equivalent at second order in shear**.

### 7.1 The two views

**Metric-shear (View A): sheared metric, rectangular periodicity.** The framework's current choice.

<!-- μ²_A_phys = (1/(1-σ²))(m²/ε² - 2σmn/ε + n²) -->
$$
\mu^2_{A, \text{phys}}(m, n;\,\sigma, \varepsilon) \;=\; \frac{1}{1-\sigma^2}\Bigl[\tfrac{m^2}{\varepsilon^2} - \tfrac{2\sigma\,m n}{\varepsilon} + n^2\Bigr]
$$

**Lattice-shear (View B): flat metric, sheared periodicity.** The studies' choice. Basis vectors e_1 = (L_u, 0), e_2 = (sL_u, L_w).

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

**Difference at order σ²:** View A has extra σ²·ε²·n² that View B doesn't (after substituting s = σ/ε).

For closure-satisfying primitives T(m, 1): n = 1, so the difference is σ²·ε² per mode — *substantial* at large ε. This is the parametrization mismatch the empirical sheets sit in: studies fit "s" of order unity at large ε (sε of order hundreds in View A units), well outside the σ_uw < 1 bound.

### 7.3 Implications and commitment

The σ_uw < 1 bound is a *parametrization artifact* of metric-shear: View B has no such bound. The lepton-like sheet's empirical "shear" approaching unity in studies' parametrization is **not** the same as metric-charge's σ_uw approaching 1; they diverge at second order.

**Commitment options:**

(I) **Adopt View B as primary.** Replaces σ_uw with s, removes the |σ| < 1 bound, aligns with the studies' parametrization. Requires reformulating §§4 of [work-m8a.md](work-m8a.md), §§4–6 of this file, and Ch 1 §4 (where σ_uw is defined). The σε product result and the σ → 1 suppression mechanism need to be redone — and as §4.4 notes, the suppression mechanism does *not* trivially transfer.

(II) **Keep View A and accept the parametrization gap.** σ_uw < 1 is the framework's parameter; studies' s is a different parametrization, only first-order equivalent. For quantitative correspondence, downstream work translates from one to the other.

(III) **Use both, with translation rules.** View A for derivations involving the σ → 1 mechanism; View B for empirical correspondence and large-shear regimes. The framework documents both and the translation between them.

Each option has costs:

- (I): the cleanest result of [work-m8a.md §4](work-m8a.md) (mass exactly M at integer σε) is View-A-specific. May not survive in View B. And the σ → 1 suppression mechanism evaporates.
- (II): the framework cannot directly predict empirical sheet parameters; "why does each sheet land at its specific (ε, σ)" is structurally untestable.
- (III): more complex and risks the framework looking incoherent.

The decision is consequential and not derivable from math alone. **Ch 9 should commit explicitly.** A recommended ordering: first work out what the §4 σ → 1 mechanism looks like in View B (or whether it has any analog there) — if there is no equivalent, then View A has structural value the framework cannot give up, and option (II) or (III) is forced.

---

## 8. Open questions for Ch 9

### 8.1 Single-axis dominance resolution (commit to mechanism)

§3.2's candidates (a)–(d). Mechanism (d) is the framework's cleanest *structural* option but depends on View A. The chapter must commit to one resolution or explicitly leave open with consequences spelled out.

### 8.2 Hadronic 3-component derivation

§6.2 identifies the φ⁴ inter-component coupling calculation ([work-m8a.md §6.5](work-m8a.md)) as the load-bearing piece. If the calculation yields k = 3 at the proton's (σ, ε), the framework derives the 3-quark structure. If not, forwarding to grid-duality.

### 8.3 Parametrization commitment

§7's three options. Resolution affects all chapters using shear. The decision needs to be made before Ch 9 can be written; this is the most consequential single open question.

### 8.4 σ → 1 analog in View B

If §7 commits to View B (option I), §4's σ → 1 suppression mechanism needs reformulation. Whether an analog exists at "large s" in View B is an open calculation.

### 8.5 Neutrino oscillation period

§6.3's mechanism α gives oscillation period ∝ 1/σ but needs explicit time-evolution calculation: chirality-eigenstate prepared as (cos θ)·(m,n) + (sin θ)·(m,−n), evolved under the sheared dispersion, period identified.

### 8.6 Towards "metric from observables"

Ch 9's end-state should equip downstream work to plug in a sheet's measured properties (mass, gauge structure, observable charge) and derive (σ, ε) — i.e., invert the structural map. The inversion's invertibility depends on the framework's having committed to:

- The parametrization (View A or B).
- The natural-particle definition under shear (single Bloch mode per [work-m8a.md §2.3](work-m8a.md)).
- The multi-link interpretation (Configuration Y).
- The single-axis-dominance resolution mechanism.
- The k-selection mechanism (or its forwarding).

With those commitments, the map (σ, ε) → sheet character becomes derivable and invertible. The actual "metric from observables" exercise is downstream of Ch 9 and may warrant its own chapter or follow-on project.

---

## 9. Recommendations

### 9.1 Commit to the parametrization first

Before any further analytic work, decide View A vs View B (or both with translation rules). This decision affects every downstream derivation. The recommended sequence: work out the §4 mechanism's View B analog (or lack thereof) explicitly, then commit.

### 9.2 Carry out the φ⁴ inter-component coupling calculation

[work-m8a.md §6.5](work-m8a.md) outlines the calculation. The result determines whether Ch 9 derives the hadronic 3-component structure or forwards it. Most consequential single piece of work for the chapter.

### 9.3 Develop the σ → 1 suppression (or its View B equivalent) for non-integer ε

§4.3 has the integer-ε case clean and the non-integer case at "partial suppression with factor 1/(2ε)." For lepton-like sheets at non-integer ε near σ = 1, whether this suppression is sufficient for the empirical character is an open quantitative question. The Ch 9 chapter should commit to whether the partial suppression suffices or whether integer ε is structurally required.

### 9.4 Compute the neutrino oscillation period

§8.5's calculation is straightforward at the linearized level. Carrying it out gives the framework a quantitative structural prediction (oscillation period as a function of σ).

### 9.5 Add Ch 9 to the project's chapter list

Update [README.md](README.md)'s chapter list. Update [Ch 7 §8](07-aspect-ratio-and-character.md) and [Ch 8 §9](08-shear-and-fractional-charge.md) "What's next" pointers to direct to Ch 9 before Ch 10 / closing summary.

### 9.6 Re-scope Ch 7 and Ch 8 to forward combined-parameter content to Ch 9

Ch 7 (ratio alone) and Ch 8 (shear alone) currently each gesture at combined-parameter character. With Ch 9 added, each chapter should keep its single-parameter analysis tight and forward the combined story to Ch 9. The Ch 8 refactor scope is in [work-m8a.md §8](work-m8a.md). A parallel scoping for Ch 7's tightening may be worth doing.
