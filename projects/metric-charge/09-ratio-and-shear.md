# Chapter 9 — Ratio and shear together: a general model of a particle sheet

This chapter brings ratio ε ([Chapter 7](07-aspect-ratio-and-character.md)) and shear σ_uw ([Chapter 8](08-shear-and-fractional-charge.md)) together into a unified treatment of the (σ_uw, ε) parameter space. So far the framework has analyzed each parameter alone; this chapter examines how they combine to produce qualitatively distinct sheet types.

The chapter's mission is to produce a **general model of a particle sheet** — characterizing how the two metric parameters jointly determine which closure-satisfying configurations dominate, what the sheet's structural character is, and how the framework's three qualitative sheet types (lepton-like, neutrino-like, hadronic-like) emerge as different regions of the combined landscape. This is the substrate for the eventual downstream exercise of *inverting* the structural map: given a sheet's measured properties, derive the metric parameter values for that sheet. metric-charge does not handle specific sheets; this chapter provides the general-sheet model from which sheet-specific downstream work can build.

**Framing convention.** Where standard-physics terminology appears — "lepton," "hadron," "neutrino" — it is used as **reference target** for what the framework's structural mechanisms could correspond to. The chapter is **qualitatively complete** for the structural shape of the (σ_uw, ε) landscape; quantitative predictions (specific σ_uw and ε values for each empirical sheet) require calculations flagged in [STATUS](STATUS.md) as the chapter's main pending dependencies.

**Inheritance.**

- *From [Chapter 1 §4](01-foundation.md):* the parametrization commitment — σ_uw (bare σ as shorthand) is the framework's primary parametrization, bounded by the binding constraint |σ_uw| < 1; the lattice-shear coefficient s = σ_uw/ε is the translation label for R-track-study correspondence.
- *From [Chapter 7](07-aspect-ratio-and-character.md):* the ε-alone analysis — three regimes (small ε, ε ≈ 1, large ε) and the finding that ε alone does not select multi-component-link structure.
- *From [Chapter 8](08-shear-and-fractional-charge.md):* the σ-alone analysis — the σε product as structural lever, m_opt = round(σε), single-Bloch-mode interpretation of the natural particle under shear, Configuration Y for multi-links, and the linear-theory non-derivability of k.

**Distinctive job.** Map the (σ_uw, ε) parameter space; identify the structural regimes; characterize each regime's qualitative sheet character; relate the framework's three sheet types to specific regions; and equip downstream work with the invertible structural map needed to derive a specific sheet's metric values from its observed properties.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The combined (σ_uw, ε) parameter space |
| 2 | The single-axis dominance puzzle |
| 3 | The σ → 1 principal-axis suppression mechanism |
| 4 | Three structural regimes |
| 5 | The three sheet types |
| 6 | Translation to s-form for empirical correspondence |
| 7 | Towards "metric from observables" |
| 8 | Summary — what this chapter establishes |
| 9 | What's next |

---

## 1. The combined (σ_uw, ε) parameter space

Chapters 7 and 8 treated ratio ε and shear σ_uw as independent parameters. The framework's three qualitative sheet types — lepton-like, neutrino-like, hadronic-like — each correspond to a *specific combination* of σ_uw and ε rather than to a single parameter alone. The chapter therefore unifies the two analyses.

### 1.1 Why a unified treatment is needed

Three structural observations motivate the combined treatment:

- The lepton-like sheet's character (single isolable charged primitive at moderate mass, substantial parity violation) needs **both** large ε *and* substantial σ_uw — neither alone suffices to produce both the parity violation and the single-particle dominance.
- The neutrino-like sheet's character (near-degenerate chirality-flipped pairs, oscillation behavior) needs **both** ε near 1 *and* σ_uw near zero — substantial σ_uw would destroy the near-degeneracy.
- The hadronic-like sheet's three-component structure (per production-study evidence that k = 3 minimizes energy at the proton sheet's parameters) needs **both** small ε *and* moderate σ_uw — neither alone produces the three-fold organization.

Neither [Chapter 7](07-aspect-ratio-and-character.md) (ratio alone) nor [Chapter 8](08-shear-and-fractional-charge.md) (shear alone) can derive these joint structural patterns. A combined treatment is therefore necessary.

### 1.2 The structural levers

The sheet metric has two free parameters: ε ≡ L_u/L_w (ratio) and σ ≡ σ_uw (shear, with |σ| < 1 binding per [Ch 1 §4](01-foundation.md)). Several combinations and individual parameters are useful structural levers:

| Combination | What it controls | Where developed |
|---|---|---|
| σε product | m_opt = round(σε) for the lightest closure-satisfying T(m, 1) primitive | [Ch 8 §2.3](08-shear-and-fractional-charge.md) |
| ε alone | Single-axis-vs-closure-satisfying mass competition | [Ch 7 §4](07-aspect-ratio-and-character.md), this chapter §2 |
| σ alone | R_w-conjugate chirality-bias amplitude (Δμ² = 4σmn/ε) | [Ch 8 §3](08-shear-and-fractional-charge.md) |
| (1 − σ²)⁻¹ | Global mass-scaling factor | [Ch 8 §2.1](08-shear-and-fractional-charge.md) |

The σε product appears most consequentially because it is what couples the two parameters at the linearized level (§1.3 below). The other levers — ε alone, σ alone, the global (1−σ²)⁻¹ factor — operate independently in their respective scopes but combine in regime-dependent ways developed in §4.

### 1.3 The σε product as the primary structural variable

The central derivable result tying σ_uw and ε together at the linearized level comes from completing the square in the dispersion of [Chapter 8 §2.3](08-shear-and-fractional-charge.md). For a closure-satisfying T(m, 1) primitive:

<!-- μ²(m, 1) = (m/ε − σ)² + (1 − σ²) -->
$$
\mu^2(m, 1;\,\sigma, \varepsilon) \;=\; \left(\frac{m}{\varepsilon} - \sigma\right)^{\!2} + (1 - \sigma^2)
$$

This is a parabola in m with minimum at m_opt = σε, where μ²_min = 1 − σ². Restoring the (1 − σ²)⁻¹ overall factor of the dispersion:

<!-- m²_phys(m_opt, 1) = M² -->
$$
m^2_\text{phys}\bigl(m_\text{opt}, 1\bigr) \;=\; M^2 \cdot \frac{1 - \sigma^2}{1 - \sigma^2} \;=\; M^2
$$

with M ≡ (ℏ/c)·(2π/L_w). **The lightest T(m, 1) primitive sits at exactly the natural mass scale M whenever σε is integer**, independent of the specific values of σ_uw and ε individually. The identity of "which integer m" shifts as σε varies, but the mass stays at M.

This cancellation is parametrization-specific: the (1 − σ²)⁻¹ factor exactly cancels the parabola's (1 − σ²) bottom value, which is structural to the metric-shear parametrization adopted in [Ch 1 §4](01-foundation.md). Predictions translated to lattice-shear (s) form for R-track-study correspondence acquire second-order corrections; §6 below develops the translation.

Two facts follow from the σε structural lever:

- **The σε product is the primary structural variable for closure-satisfying primitives**, not σ alone or ε alone. Different (σ, ε) values producing the same σε product give the same lightest closure-satisfying primitive identity (m_opt = round(σε)).
- **Level crossings between adjacent T(m, 1) primitives occur at half-integer σε** (σε = m + 1/2). Near these crossings, two closure-satisfying primitives are nearly degenerate at mass ≈ M.

The σε product appears again in §4's regime classification.

---

## 2. The single-axis dominance puzzle

A combined-parameter question that neither Ch 7 nor Ch 8 can resolve alone, but which the (σ_uw, ε) landscape sharpens: at any (σ, ε), the lightest single-axis modes are (1, 0) at μ² = 1/ε² and (0, 1) at μ² = 1. For ε > 1, single-axis (1, 0) is the unique lightest mode, with mass approaching zero as ε → ∞. Yet the framework wants charged sheets at extreme ε to be physically meaningful — the lepton-like sheet's empirical character (MaSt model-F) places its ε at very large values. This section states the puzzle precisely and considers its resolutions.

### 2.1 Statement of the puzzle

The mass landscape across ε regimes, comparing the lightest single-axis mode to the lightest closure-satisfying primitive:

| ε regime | Lightest single-axis | Lightest closure-satisfying | Which is lighter? |
|---|---|---|---|
| ε < 1 | (0, 1) at μ² = 1 | T(m_opt, 1) at μ² ≈ 1 − σ² | T(m_opt, 1) for σ > 0 |
| ε > 1 | (1, 0) at μ² = 1/ε² | T(m_opt, 1) at μ² ≈ 1 − σ² | (1, 0) unless σ > √(1 − 1/ε²) |
| ε ≫ 1 | (1, 0) at μ² ≈ 0 | T(m_opt, 1) at μ² ≈ 1 − σ² | (1, 0) *much* lighter |

For ε > 1, single-axis modes dominate the lowest-energy spectrum. By the structural-degeneracy mechanism of [Chapter 4 §1](04-the-closure-condition.md), single-axis modes are mass-only — one winding is zero, no chirality structure on the curve, no spacetime↔compact gauge potential. **The lowest-energy excitations of an extreme-ε sheet are therefore mass-only, not charged.**

This is the architectural question that [Chapter 7 §4.3](07-aspect-ratio-and-character.md) flags and leaves open: **why does an extreme-ε sheet host charged states as its physical particles when single-axis modes are lighter?** The framework needs an answer before any of the lepton-like sheet's structural picture is on firm ground.

### 2.2 Candidate resolutions

Four candidate resolutions are available:

**(a) Single-axis modes are not "particles" in the sheet-physical sense.** Under this reading, single-axis modes are the sheet's structural background — vacuum-like configurations that don't correspond to observed particles. Charged states are excitations *above* this background. The framework would need to specify what distinguishes a "particle" excitation from a "background" mode, and would inherit constraints from substrate-level analysis.

**(b) A substrate-level constraint projects out single-axis modes.** Grid-duality's wrap-promotion ladder may impose a structural requirement — for example, "both windings nonzero for sheet-physical-particle status" — that the framework inherits. Single-axis modes would exist in the mathematical inventory but be projected out as physical particles by the substrate.

**(c) The framework's prediction differs from observation.** Single-axis dominance at extreme ε is genuinely predicted; MaSt model-F's electron-sheet ε identification is wrong; the framework predicts something structurally different about large-ε sheets. Under this stance the chapter's claim is that large-ε sheets *should* be dominated by mass-only modes, and the lepton-like sheet's empirical identification must be re-examined.

**(d) σ → 1 principal-axis suppression.** As σ_uw approaches its positive-definiteness boundary, single-axis mode masses diverge as (1 − σ²)⁻¹, faster than the lightest closure-satisfying primitive's mass diverges (which can stay finite for integer ε). This **combined (σ, ε) mechanism** singles out closure-satisfying modes as the dominant low-energy excitations near the metric boundary. Developed rigorously in §3 below.

Of the four, only (d) is a structural-mechanism answer entirely within metric-charge's existing apparatus — neither (a) nor (b) commits to a specific projection rule, and (c) requires re-examining the MaSt identifications.

### 2.3 The chapter's stance

This chapter takes **mechanism (d) as the framework's primary candidate** for resolving the single-axis-dominance puzzle, on the grounds that:

- It uses the framework's existing parameters and structural mechanisms without adding new ingredients.
- It is a combined (σ, ε) mechanism — properly Ch 9's concern.
- It connects the lepton-like sheet's empirical character (large ε plus substantial shear) to a structural reason for the absence of single-axis dominance.

The commitment is **contingent on §6's translation analysis**: whether the σ → 1 mechanism's structural predictions survive translation from σ_uw-form (where the mechanism is defined) to s-form (where R-track studies report empirical parameter values) determines whether (d) is actually adequate. If §6's translation analysis fails to match empirical sheets, alternatives (a), (b), or (c) must be considered. The candidates are kept open as fallback positions.

---

## 3. The σ → 1 principal-axis suppression mechanism

This section derives mechanism (d) of §2.2 rigorously. The claim is precise: as σ_uw approaches 1 (the positive-definiteness boundary), single-axis mode masses diverge as (1 − σ²)⁻¹, while the lightest closure-satisfying T(m, 1) primitive's mass stays finite (at integer ε) or diverges more slowly (at non-integer ε). The mechanism therefore selects closure-satisfying modes as the dominant low-energy excitations near the metric boundary.

### 3.1 Setup

Take σ_uw approaching 1 from below: σ = 1 − δ with δ → 0⁺. The factor (1 − σ²) = δ(2 − δ) ≈ 2δ at leading order in small δ.

### 3.2 Single-axis modes diverge as 1/δ

For single-axis modes, the dispersion of [Ch 8 §2.1](08-shear-and-fractional-charge.md) gives physical mass-squared:

<!-- m²_phys(1, 0) ≈ M²/(2ε²δ) → ∞ -->
$$
m^2_\text{phys}(1, 0) \;\approx\; \frac{M^2}{2\varepsilon^2\,\delta} \;\to\; \infty,
\qquad
m^2_\text{phys}(0, 1) \;\approx\; \frac{M^2}{2\delta} \;\to\; \infty
$$

Both single-axis modes diverge as 1/δ as σ → 1. The (1 − σ²)⁻¹ factor is the only σ-dependence in their masses (per the σ-cross-term invariance of [Ch 8 §3](08-shear-and-fractional-charge.md)), and it pushes both modes' masses arbitrarily high as the metric approaches degeneracy.

### 3.3 Closure-satisfying primitive — two cases

The lightest closure-satisfying primitive sits at m̂ = round(σε). At σ = 1 − δ: m̂ ≈ round((1 − δ)·ε) = round(ε) for small δ. The residual Δ ≡ m̂/ε − σ controls the mass.

**Case A: ε is integer.** Then m̂ = ε exactly and m̂/ε = 1, so Δ = 1 − σ = δ. The residual squared (m̂/ε − σ)² = δ². Dividing by (1 − σ²) ≈ 2δ:

<!-- residual contribution = δ²/(2δ) = δ/2 → 0 -->
$$
\frac{\Delta^2}{1 - \sigma^2} \;\approx\; \frac{\delta^2}{2\delta} \;=\; \frac{\delta}{2} \;\to\; 0
$$

So m²_phys(m̂, 1) → M² as δ → 0. **At integer ε, the closure-satisfying primitive's mass stays at exactly M while single-axis modes diverge.** This is the σε product result of §1.3 evaluated at the σ → 1 limit: with integer ε and σ = 1 − δ, the product σε approaches the integer ε, putting the lightest primitive exactly at the parabola minimum, where the (1 − σ²) factors cancel.

**Case B: ε is not integer.** Let Δ_0 ≡ m̂/ε − 1, a fixed nonzero number with |Δ_0| ≤ 1/(2ε). At σ = 1 − δ: Δ ≈ Δ_0 for small δ. Residual squared: Δ_0². Dividing by (1 − σ²) ≈ 2δ:

<!-- m²_phys(m̂, 1) ≈ M²·Δ_0²/(2δ) for non-integer ε -->
$$
m^2_\text{phys}(\hat m, 1) \;\approx\; \frac{M^2\Delta_0^2}{2\delta}
$$

Both modes diverge as 1/δ. Compare the divergence rates of closure-satisfying to single-axis:

<!-- m²_phys(m̂, 1)/m²_phys(1, 0) = Δ_0²·ε² ≤ 1/4 -->
$$
\frac{m^2_\text{phys}(\hat m, 1)}{m^2_\text{phys}(1, 0)} \;=\; \Delta_0^2\cdot\varepsilon^2 \;\le\; \frac{1}{4}
$$

The closure-satisfying mass-squared is at most one-fourth of the (1, 0) single-axis mass-squared — equivalent to a factor of 2 lighter in mass — and is bounded below by 1/(4ε²) of the (1, 0) mass-squared. Closure-satisfying still wins, but the suppression is *partial* rather than *total*.

### 3.4 Summary of suppression

The mechanism's behavior across ε:

| ε | Closure-satisfying mass at σ → 1 | Single-axis (1, 0) mass | Suppression |
|---|---|---|---|
| Integer | Finite, equal to M | Diverges as 1/δ | **Total** |
| Non-integer, ε ≫ 1 | Diverges; bounded by ≈ M·Δ_0/√(2δ) | Diverges as M/(ε√(2δ)) | Strong (ε-suppressed) |
| Non-integer, ε ≈ 1 | Diverges; factor ~2 lighter than (1, 0) | Diverges as M/√(2δ) | Weak |
| Non-integer, ε ≪ 1 | Diverges; (0, 1) competitive | (0, 1) diverges as M/√(2δ) | Mode-specific |

**The mechanism works cleanly at integer ε** (total suppression) **and partially at large non-integer ε** (suppression by factor ~1/(2ε) in mass). It requires σ near 1 *and* ε near integer (or ε ≫ 1, where the residual Δ_0² is small in absolute terms).

### 3.5 Implication for the architectural question

At the conditions where mechanism (d) operates cleanly — large ε with σ near 1 — single-axis modes are pushed to high mass and closure-satisfying modes dominate the low-energy spectrum. This is precisely the structural picture the lepton-like sheet needs: a charged-mode tier at moderate mass, with single-axis modes scaled out.

The mechanism is in σ_uw-form by construction. The (1 − σ²)⁻¹ factor that drives the suppression is structural to that parametrization, not present in the lattice-shear (s) form. Translating the mechanism's predictions to s-form for empirical correspondence with R-track studies is non-trivial at large σ; §6 below develops the translation.

---

## 4. Three structural regimes

The (σ_uw, ε) plane partitions into structurally distinct regions based on which mode classes dominate the low-energy spectrum and which mechanisms are active. The partition is qualitative; the regimes overlap and shade into each other at boundaries, but each has a characteristic structural signature useful for thinking about sheet character.

### 4.1 Regime I — near-symmetric, near-bare (small σ, ε ≈ 1)

- Closure-satisfying T(1, 1) at μ² = 1/ε² − 2σ/ε + 1 ≈ 2 − 2σ ≈ 2 (for ε ≈ 1, σ ≪ 1).
- Single-axis (1, 0) and (0, 1) both at μ² ≈ 1.
- Chirality-bias R_w-conjugate split between (m, n) and (m, −n) small, scaling as σ.
- m_opt = round(σ·1) = 1; T(1, 1) is the lightest closure-satisfying primitive.

Two structural features of this regime matter for sheet character:

- **Sign-conjugate pairs** (m, n) and (−m, −n) are mass-degenerate by R_J preservation under shear ([Ch 8 §2.1](08-shear-and-fractional-charge.md)). [Chapter 6 §4](06-handedness-and-pairs.md)'s sign-conjugate cancellation construction operates cleanly here: pair configurations are mass-only with very small chirality field T_uw (∝ σ).
- **R_w-conjugate pairs** (m, n) and (m, −n) are near-mass-degenerate at small σ. A configuration prepared as a chirality-eigenstate is close to a mass-eigenstate; small σ produces a small mismatch that drives oscillation between them with period ∝ 1/σ.

### 4.2 Regime II — thin sheet, near-bare (small σ, ε ≪ 1)

- T(1, 1) at μ² ≈ 1/ε² + 1 ≈ 1/ε², dominated by the 1/ε² term for small ε.
- Single-axis (0, 1) at μ² = 1.
- Single-axis (1, 0) at μ² = 1/ε² — heavy, comparable to T(1, 1).
- σε ≪ 1; m_opt = 1.

Single-axis (0, 1) is by far the lightest mode and dominates the low-energy spectrum. The closure-satisfying tier sits at mass ≈ M/ε — substantially heavier. The architectural question of §2 applies in its sharpest form: the lowest-energy excitations are mass-only, not charged.

This regime is where mechanism (d) of §2.3 does *not* operate cleanly (σ is small, not near 1). Whether the framework supports charged-sheet character here depends on substrate-level input or on the φ⁴ inter-component mechanism flagged in §5.2.

### 4.3 Regime III — wide sheet, sheared near boundary (σ near 1, large ε)

- T(m_opt, 1) at mass ≈ M, with m_opt = round(σε) — a specific large integer.
- Single-axis modes scaled out by (1 − σ²)⁻¹ (the §3 mechanism).
- Substantial chirality bias from σ near unity.
- Many T(m, 1) primitives near m_opt have similar masses, with residual splitting ~ 1/ε² per step in m.

The σ → 1 principal-axis suppression activates in this regime: single-axis modes diverge, closure-satisfying modes stay at moderate mass, and the spectrum's low-energy tier is dominated by T(m_opt, 1) and its nearby neighbors. This is **the regime where charged-sheet character is structurally clean** within metric-charge's existing apparatus.

### 4.4 Regime IV — level crossings (σε ≈ k + 1/2)

At half-integer values of the σε product, two adjacent T(m, 1) primitives are mass-degenerate (per [Ch 8 §2.3](08-shear-and-fractional-charge.md)). The sheet hosts a near-degenerate pair of closure-satisfying primitives, separated from the third-closest by residual ~ 1/ε². For ε ≫ 1, three primitives can sit at nearly the same mass (no exact three-fold degeneracy — [Ch 8 §2.3](08-shear-and-fractional-charge.md) shows this is impossible at any single σε — but the spread is small).

Regime IV is a feature within Regimes II and III (at the σε values that produce level crossings); it is called out separately because the level-crossing structure is itself a structural mechanism worth noting.

---

## 5. The three sheet types

The framework needs to accommodate three qualitatively distinct sheet types: lepton-like, hadronic-like, and neutrino-like. Each maps onto a specific region of the (σ_uw, ε) landscape, with the regime's structural mechanisms producing the sheet's qualitative character. The analysis below is **qualitative**; §5.4 lists what each sheet requires for quantitative engagement.

### 5.1 Lepton-like sheet — "principal-axis-aligned charge"

A single isolable charged primitive at moderate mass, no fractional decomposition, well-defined chirality.

**Structural fit:** Regime III (σ near 1, large ε).

Under Regime III:

- The lightest closure-satisfying primitive T(m_opt, 1) sits at mass M, with m_opt = round(σε) — a specific large integer determined by the sheet's σ and ε together.
- Single-axis modes are scaled out by (1 − σ²)⁻¹ → ∞ via the §3 mechanism.
- The R_w-conjugate split between (m_opt, 1) and (m_opt, −1) is substantial, producing the parity-violation-like asymmetry observed for the empirical lepton.
- Single-particle character: at m_opt isolated as the unique lightest, multi-link configurations cost k × M and are Boltzmann-suppressed at any modest temperature.

Three structural-mechanism observations support this fit:

- **Why large ε?** Large ε permits σ to approach 1 while keeping the σε product large enough that m_opt is a specific large integer rather than 1. Additionally, the residual ~ 1/ε is small, keeping T(m_opt, 1) close to M even at non-integer ε.
- **Why σ near 1?** The §3 mechanism's suppression of single-axis modes is the framework's primary structural-mechanism candidate for resolving the §2 architectural question. σ near 1 is what activates the suppression.
- **Why single-particle?** When m_opt is isolated as the unique lightest closure-satisfying primitive (away from level-crossings), only one closure-satisfying mass tier is populated at low energy. Multi-link configurations and other primitives sit at higher mass.

The architectural question of §2 is resolved here by mechanism (d). This is the cleanest structural picture metric-charge can offer for the lepton-like sheet, contingent on the §6 translation analysis confirming that the σ → 1 mechanism's predictions survive to the s-form used by R-track studies.

**Gauge structure at σ near 1.** The wrap-order convention of [Ch 1 §10](01-foundation.md) keeps the gauge-potential identification clean across σ regimes: h_μw is the single U(1) gauge potential, and h_μu's contribution under shear is the mass-direction metric perturbation rather than a second gauge field (see [Ch 5 §4.6.5](05-metric-self-consistency.md)). The lepton-like sheet's "single isolable charged primitive" framing is preserved at σ near 1 — the strong shear that activates the §3 suppression mechanism does not introduce additional gauge structure.

### 5.2 Hadronic-like sheet — "three-component charge tower"

Multiple closure-satisfying primitives in a three-component structural organization, with each component carrying 1/3 of the link's integer total charge.

**Structural fit:** ε ≪ 1, σ moderate (Regime II adjacent).

Linear theory at this regime:

- T(1, 1) sits at μ² ≈ 1/ε² — heavy because ε is small.
- Single-axis (0, 1) at μ² = 1 — heavy in absolute terms but much lighter than T(1, 1).
- m_opt = round(σε) ≈ 0, rounded to 1. T(1, 1) is the lightest closure-satisfying primitive.
- Adjacent T(m, 1) primitives are even heavier (T(2, 1) at μ² ≈ 4/ε², etc.).

**Linear theory does not, by itself, produce three-component organization at this regime.** The empirical evidence for k = 3 at the proton sheet's parameters (from production studies that fit multi-observable target sets) requires a mechanism outside pure linear scalar-field theory. Per [Chapter 1 §11](01-foundation.md)'s deferral of nonlinear backreaction, metric-charge does not derive k itself — k-selection is forwarded.

Three candidate mechanisms with their downstream destinations:

- **Internal-mode dynamics with σ-induced coupling.** Per [Chapter 8 §6.3](08-shear-and-fractional-charge.md), adding a small inter-component coupling (a φ⁴-style quadratic-in-amplitude term) introduces dynamics among the relative phases of components. The calculation — write the φ⁴ self-interaction energy of a k-component link at the hadronic-like (σ, ε), minimize over k — is a nonlinear self-interaction calculation, forwarded to [metric-binding](../metric-binding/) along with the rest of multi-knot energetics.
- **Lattice-shear basis rephrasing.** In the lattice-shear (s) form used by R-track studies (§6), the "shortest closure-satisfying curve" at the hadronic parameters may *be* a 3-component configuration in lattice-shear integer labels. This is a basis-rephrasing question that may settle within metric-charge once the §6 translation analysis is done.
- **Substrate Z_3 from grid-duality.** k = 3 selection from substrate Z_k input at L3 (per [grid-duality §7.5](../grid-duality/07-wrap-promotion-modeling.md)).

metric-charge's contribution to this sheet is the structural framing: the inventory of closure-satisfying configurations, what a k-component multi-link looks like under Configuration Y, and how the fractional-charge structure emerges once a k has been selected. The k-selection itself comes from downstream — whichever of the three candidate mechanisms above turns out to apply.

### 5.3 Neutrino-like sheet — "near-degenerate chirality pairs"

Mass-without-charge behavior with paired structure that produces oscillation and cancellation.

**Structural fit:** Regime I (σ very small, ε near 1).

Two structural mechanisms operate together in this regime:

**Mechanism α — chirality-pair mixing.** At small σ_uw, the R_w-conjugate Bloch modes T(1, 1) and T(1, −1) are nearly mass-degenerate (μ² split ≈ 4σ/ε, small). The chirality-eigenstate basis (under the framework's wrap-order) differs from the mass-eigenstate basis (under the sheared dispersion); a configuration prepared as a chirality-eigenstate oscillates between mass-eigenstates with period proportional to 1/Δm ∝ 1/σ. As σ → 0, the period diverges and the chirality-eigenstate becomes stationary; as σ grows, oscillation accelerates and the chirality-eigenstate spreads quickly. This is the structural pattern of neutrino oscillation.

**Mechanism β — sign-conjugate pair cancellation.** Per [Chapter 6 §4](06-handedness-and-pairs.md), a sign-conjugate pair (m, n) + (−m, −n) at equal amplitudes has its gauge potentials cancel under R_J-symmetrization — yielding mass-only configurations with a chirality field T_uw. This mechanism operates independently of σ (the R_J reflection is preserved under shear; [Ch 8 §3](08-shear-and-fractional-charge.md)), but at small σ the chirality field T_uw is correspondingly small (proportional to σ). The cancellation pair is therefore *more cleanly mass-only* on a small-σ sheet than on a high-σ sheet.

Combined picture: small σ + ε near 1 gives sign-conjugate pairs (mass-only by mechanism β, very small T_uw chirality field) plus chirality-pair near-degeneracy (oscillation by mechanism α). **Tiny σ is structurally necessary for the neutrino-like character.** Substantial σ would break the near-degeneracy (eliminating oscillation) and produce a non-negligible T_uw (compromising the clean mass-only behavior of cancellation pairs).

The chapter's structural prediction for this sheet: the framework's small-σ, ε-near-1 regime produces mass-without-charge configurations organized as oscillating chirality-eigenstate pairs — matching the qualitative shape of neutrino phenomenology.

### 5.4 What quantitative engagement requires

The three-sheet correspondence above is qualitative. Converting it to quantitative predictions — specific σ_uw and ε values per sheet, specific oscillation periods, specific multi-link masses — requires the following pending calculations:

- **Lepton-like:** Rigorous σ → 1 analysis at non-integer ε, plus translation of the predictions to s-form for empirical correspondence with R-track studies (§6). The σ_uw ↔ s transform diverges at second order, so the substantive quantitative work is verifying that the structural picture survives the translation at large σ.
- **Hadronic-like:** The φ⁴ inter-component coupling calculation lives in [metric-binding](../metric-binding/) (per §5.2 — it is a nonlinear self-interaction outside metric-charge's scope); the substrate Z_k input lives in grid-duality. metric-charge's contribution is the structural framing (Configuration Y consequences, sign audit per [TODO-L5](STATUS.md)), independent of k-selection.
- **Neutrino-like:** Oscillation period from σ computed explicitly via the time-evolution of a chirality-eigenstate prepared as (cos θ)·(m, n) + (sin θ)·(m, −n) under the sheared dispersion, then checked structurally against observed oscillation magnitudes.

Each is a concrete tractable calculation; together they convert this chapter from a structural map to a quantitative framework. [STATUS](STATUS.md) tracks these as the chapter's main pending dependencies.

---

## 6. Translation to s-form for empirical correspondence

The framework's σ_uw is bounded by the binding constraint |σ_uw| < 1 (per [Ch 1 §4](01-foundation.md)). R-track studies use the lattice-shear coefficient s with no such bound, related to σ_uw by the transform s = σ_uw/ε at first order. The two parametrizations describe the same physical sheet but **diverge at second order in shear**, which makes translation non-trivial at large σ — precisely the regime where the §3 σ → 1 mechanism operates.

### 6.1 The parametrization is settled at the framework level

[Chapter 1 §4](01-foundation.md) commits the framework to σ_uw (bare σ as shorthand) as the working parametrization, with s = σ_uw/ε used as the translation label for R-track-study correspondence. The two are different numbers describing the same physical sheet via the documented transform; they are not interchangeable. **|σ_uw| < 1 is a binding positive-definiteness requirement of the (u, w) metric sub-block**, not a parametrization artifact.

This chapter therefore does not relitigate the parametrization choice. The remaining question is purely about translation behavior: does the σ → 1 mechanism's structural predictions translate cleanly enough to s-form to match the parameter values reported by R-track studies?

### 6.2 The two parametrizations

**Metric-shear (σ_uw form, framework primary):** sheared metric, rectangular periodicity. The dispersion includes the (1 − σ²)⁻¹ overall factor that makes the σ → 1 mechanism possible:

<!-- μ²_phys = (1/(1-σ²))(m²/ε² - 2σmn/ε + n²) -->
$$
\mu^2_\text{phys}(m, n;\,\sigma, \varepsilon) \;=\; \frac{1}{1-\sigma^2}\Bigl[\frac{m^2}{\varepsilon^2} - \frac{2\sigma\,m n}{\varepsilon} + n^2\Bigr]
$$

**Lattice-shear (s form, used by R-track studies):** flat metric, sheared periodicity with basis vectors e_1 = (L_u, 0), e_2 = (s·L_u, L_w). The studies' dispersion (relating wavenumber labels n_t, n_r to integers m, n by n_t = m, n_r = n):

<!-- μ²_B = (n_t/ε)² + (n_r - s·n_t)² -->
$$
\mu^2_B(n_t, n_r;\,s, \varepsilon) \;=\; \frac{n_t^2}{\varepsilon^2} + (n_r - s\,n_t)^2 \;=\; \frac{n_t^2}{\varepsilon^2} + n_r^2 - 2s\,n_t n_r + s^2\,n_t^2
$$

The two parametrizations describe the same physical sheet under a coordinate change documented in [Ch 1 §4](01-foundation.md). The translation between them — for sheet parameters and for predictions — is the subject of this section.

### 6.3 First-order match, second-order divergence

Matching the linear-in-shear cross-term −2s·n_t·n_r between the two dispersions to the σ_uw-form's −2σ·mn/ε:

<!-- s = σ_uw/ε at first order -->
$$
s = \frac{\sigma_{uw}}{\varepsilon}
$$

This is the first-order transform. At second order, expanding the (1 − σ²)⁻¹ factor of σ_uw-form in σ²:

<!-- (1 − σ²)⁻¹ ≈ 1 + σ² + O(σ⁴) -->
$$
\frac{1}{1 - \sigma^2} \;\approx\; 1 + \sigma^2 + O(\sigma^4)
$$

The σ² correction contributes + σ²·(m²/ε² + n²) to μ²_phys. The s-form (which has no overall (1 − s²)⁻¹ factor) contributes only + s²·m² = + (σ/ε)²·m² = σ²·m²/ε² at order s².

**Difference at order σ²:** σ_uw-form has an extra + σ²·n² term that s-form does not. For closure-satisfying primitives T(m, 1) where n = 1, this difference is σ² — substantial at large σ. The two parametrizations describe the same physical sheet, but the specific numerical values of σ_uw and s diverge at second order: the empirical lepton-like sheet fits to "s of order unity" in R-track studies' s-form gives "σ_uw·ε of order ε" via the first-order transform, but the second-order correction means the same sheet's σ_uw is bounded by 1 by the positive-definiteness wall.

### 6.4 The open quantitative question

The σ → 1 principal-axis suppression of §3 is the framework's main structural candidate for resolving the §2 architectural question on extreme-ε sheets. The mechanism is defined in σ_uw-form: the (1 − σ²)⁻¹ factor is what scales single-axis masses up faster than closure-satisfying masses near the metric boundary.

Translating this structural picture to s-form for empirical correspondence is **mechanical at small σ** (the first-order σ = s·ε transform works, second-order corrections small) but **substantively non-trivial at large σ** near the |σ_uw| < 1 boundary — where the §3 mechanism operates and where the σ_uw ↔ s second-order divergence is non-trivial.

The open question for this chapter and its downstream work:

**Does the σ → 1 mechanism's predicted sheet character (single charged primitive at mass M, single-axis modes suppressed, substantial chirality bias) survive translation to s-form at the large-σ regime where R-track studies' empirical lepton-like-sheet s-values are reported?**

Two outcomes are possible:

- **If yes:** The framework predicts the lepton-like sheet's character quantitatively. The σ_uw value in framework-form, when translated to s-form, matches the studies' empirical fits — and the §3 mechanism is the structural answer to the §2 puzzle for this sheet.
- **If no:** Either the σ → 1 mechanism is the wrong candidate for the architectural question (forcing reconsideration of resolutions (a), (b), or (c) from §2.2), or the empirical s-values from studies require re-interpretation under σ_uw parametrization rules — implying that the studies' identification of "the lepton sheet's shear" may not be what the framework's σ_uw represents.

The question is substantive because mechanism (d) is the load-bearing piece for the lepton-like sheet's structural picture in §5.1. Without it confirmed, that sheet's character rests on architectural-question resolutions (a)–(c) that the framework has not yet concretely worked out. The translation analysis is therefore the most consequential single quantitative work for the lepton-like sheet's empirical correspondence.

---

## 7. Towards "metric from observables"

The chapter's end-state equips downstream work with the substrate for the eventual exercise of **inverting** the structural map: given a sheet's measured properties (mass, gauge structure, observable charge, chirality bias, multi-component organization), derive the sheet's metric parameter values (σ_uw, ε, plus the diagonal-normalization convention of [Ch 1 §11](01-foundation.md)). This section spells out what the inversion requires and what remains downstream of this chapter.

### 7.1 The inversion exercise

The forward map established in §§1–5 reads (σ_uw, ε) → sheet character, where "sheet character" includes:

- The lightest closure-satisfying primitive's identity (m_opt = round(σε)) and mass (≈ M at integer σε).
- The single-axis-vs-closure-satisfying competition (which mode tier dominates).
- The R_w-conjugate chirality-bias magnitude (∝ σ).
- The regime classification (I, II, III, IV) and corresponding qualitative pattern.
- The sheet type identification (lepton-like, hadronic-like, neutrino-like) based on regime fit.

The inversion runs in the opposite direction: a sheet's observed mass scale, gauge structure, parity-violation magnitude, and (if hadronic) multi-component organization determine (σ_uw, ε) — by reading off the regime, matching to one of the three sheet types, and refining numerically against the structural-map relations.

### 7.2 Prerequisites for invertibility

The map (σ_uw, ε) → sheet character is well-defined and structurally invertible when the framework has committed to several upstream choices. Most are already settled:

| Commitment | Where settled |
|---|---|
| Parametrization: σ_uw primary, s for translation | [Ch 1 §4](01-foundation.md) |
| Binding bound: \|σ_uw\| < 1 | [Ch 1 §4](01-foundation.md) |
| Natural particle under shear: single Bloch mode | [Ch 8 §2.2](08-shear-and-fractional-charge.md) |
| Multi-link interpretation: Configuration Y | [Ch 8 §5.2](08-shear-and-fractional-charge.md) |
| Single-axis-dominance resolution: mechanism (d), contingent | §2.3 of this chapter |
| k-selection mechanism (or forwarding) | [Ch 8 §6.5](08-shear-and-fractional-charge.md) + §5.2 of this chapter |
| σ → 1 mechanism's translation behavior | §6.4 of this chapter, contingent |

With these commitments in place, the structural map is operationally complete. The two contingent items — §2.3's commitment to mechanism (d) and §6.4's translation-survival question — are flagged as the load-bearing dependencies; if either falls, alternate routes are spelled out in their respective sections.

### 7.3 Multi-sheet composition forwarded to metric-binding

The "metric from observables" exercise as described above operates at the **single-sheet level**: one sheet, one (σ_uw, ε) pair, one metric. [Chapter 1 §11](01-foundation.md) flags multi-sheet composition as a non-assumption for this project — how multiple sheets share extended spacetime, how their diagonal normalizations compose, how their shears interact in multi-species settings — and forwards the architectural commitments to [metric-binding](../metric-binding/).

The actual "metric from observables" inversion exercise is **downstream of this chapter** and may warrant its own follow-on chapter or a separate sheet-specific project. metric-charge's job is to provide the general-sheet structural map; the inversion's specific application to electron, proton, neutrino sheets, including the multi-sheet composition rules needed when several species share extended spacetime, lives in downstream work.

---

## 8. Summary — what this chapter establishes

The chapter's structural payoff for the framework:

- **The σε product** is the framework's primary structural lever for closure-satisfying primitive selection. Neither σ_uw nor ε alone is sufficient; the product σε determines which integer m is m_opt and produces the "mass exactly M at integer σε" cancellation that anchors the closure-satisfying tier near the natural mass scale.
- **The single-axis dominance puzzle** is a sharp architectural question at large ε: linear theory says single-axis modes are lighter than closure-satisfying modes, yet the framework wants charged-sheet character at large ε. The chapter commits to mechanism (d) — σ → 1 principal-axis suppression — as the primary candidate resolution, contingent on §6's translation analysis.
- **Four structural regimes** partition the (σ_uw, ε) plane: near-symmetric near-bare (I), thin sheet near-bare (II), wide sheet sheared near boundary (III), and level crossings (IV). Each regime has a characteristic structural signature and a characteristic candidate sheet-type correspondence.
- **The three sheet types** map onto specific regions of the landscape: lepton-like in Regime III (with mechanism (d) supplying the single-axis suppression), hadronic-like in Regime II (with the φ⁴ inter-component or substrate Z_3 supplying the three-component organization), neutrino-like in Regime I (with chirality-pair near-degeneracy supplying the oscillation pattern). Each correspondence is qualitative; quantitative engagement requires pending calculations.
- **Translation to s-form** is mechanical at small σ but non-trivial at large σ. The σ_uw ↔ s transform diverges at second order, with the substantive quantitative work for the lepton-like sheet's empirical correspondence localized to the §6.4 translation question.
- **The invertible structural map** (σ_uw, ε) → sheet character is the substrate for downstream "metric from observables" work. The inversion's prerequisites are mostly already committed; the load-bearing dependencies — mechanism (d) and the §6 translation — are flagged for ongoing work.

The framework's structural inventory at the single-sheet level is now complete:

| Parameter / structural choice | What it controls |
|---|---|
| (m, n) labels | Primary mode identity (Chapters 2, 3) |
| Closure satisfaction (n | m) | Charge vs no-charge (Chapter 4) |
| Handedness sign | Matter/antimatter (Chapter 6) |
| Aspect ratio ε | Single-axis-vs-closure-satisfying competition (Chapter 7, this chapter) |
| Shear σ_uw | Chirality bias; σε primitive selection; σ → 1 suppression (Chapter 8, this chapter) |
| Combined (σ_uw, ε) regime | Sheet-type character; structural map for "metric from observables" (this chapter) |

This is metric-charge's contribution to the framework's particle-sheet model. Multi-sheet composition and the specific application to empirical sheet inventories are forwarded to [metric-binding](../metric-binding/) and downstream MaSt-correspondence work.

---

## 9. What's next

[**Chapter 10 — Closing summary**](10-closing-summary.md). Consolidates what the project established across all nine chapters, what was ruled out, what was unexpectedly found, and what remains open. Hands off to [metric-binding](../metric-binding/) for the multi-knot interaction story — multi-knot energetics, force laws, bound states, multi-sheet composition rules, and the candidate strong-force mechanism.

---

## What this chapter does **not** do

- **Does not carry out the φ⁴ inter-component coupling calculation.** Scoped in [Ch 8 §6.3](08-shear-and-fractional-charge.md); identified in §5.2 as load-bearing for the hadronic-like sheet's three-component derivation. Tracked in [STATUS](STATUS.md) as TODO-M8(a)'s redirected open work.
- **Does not predict specific (σ_uw, ε) values** for the three empirical sheets. The chapter provides the qualitative structural map and the regime classification; quantitative predictions per sheet require the §5.4 pending calculations and §6.4's translation analysis.
- **Does not carry out the "metric from observables" inversion exercise.** §7 establishes the substrate and prerequisites; the actual inversion application to specific sheets is downstream of this chapter and may warrant its own follow-on chapter or project.
- **Does not handle multi-sheet composition.** Per [Ch 1 §11](01-foundation.md), the framework treats one sheet at a time. How multiple sheets share extended spacetime, how their diagonal normalizations compose, how their shears interact — forwarded to [metric-binding](../metric-binding/).
- **Does not commit to MaSt-correspondence assignments.** The three-sheet structural correspondence (lepton-like in Regime III, hadronic-like in Regime II, neutrino-like in Regime I) matches MaSt model-F's qualitative identifications; specific quantitative identifications are downstream MaSt-correspondence work.
- **Does not derive a matter/antimatter bias mechanism.** σ_uw provides P-flavor chirality bias only. The C-flavor side (matter/antimatter populations) is not derived; forwarded to substrate-level work per [Ch 8 §3.3](08-shear-and-fractional-charge.md).
- **Does not derive nonlinear shear effects beyond the linear-adjacent φ⁴ candidate.** Linear theory only, with the φ⁴ self-interaction term as the smallest departure considered. Larger nonlinear corrections are deferred.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Does the σ → 1 mechanism's predicted sheet character survive translation to s-form at large σ, matching R-track-study lepton-like-sheet values? | §6.4 of this chapter. The most consequential single quantitative question. |
| Does the φ⁴ inter-component coupling calculation (forwarded to [metric-binding](../metric-binding/) per [Ch 1 §11](01-foundation.md)) yield k = 3 at the hadronic-like regime, or does k-selection come from substrate Z_k (grid-duality §8) or another mechanism? | [metric-binding](../metric-binding/) (nonlinear multi-knot energetics) or [grid-duality §8](../grid-duality/08-where-alpha-appears.md) (substrate Z_k). |
| If mechanism (d) fails the §6 translation, which of resolutions (a)/(b)/(c) does the framework commit to for the §2 architectural question? | §2.2 / §6.4 of this chapter, contingent. |
| What is the explicit neutrino-oscillation period derived from σ_uw, and does it structurally match observed magnitudes? | §5.3 / §5.4 of this chapter; calculation pending. |
| What does the "metric from observables" inversion exercise look like in detail for each of the three empirical sheets? | §7 of this chapter, then downstream of the chapter (sheet-specific follow-on work). |
| What additional structure (multi-sheet composition rules) does the inversion require for cases where multiple species share extended spacetime? | Forwarded to [metric-binding](../metric-binding/) per [Ch 1 §11](01-foundation.md). |
| Are there sheet types beyond the three considered — combinations of (σ_uw, ε) that produce qualitatively new structural character not covered by Regimes I–IV? | Open follow-up; the chapter's regime map is exhaustive in coarse terms but finer structure may emerge from quantitative analysis. |
| Does the (σ_uw, ε) landscape's structural-map predictions hold at higher orders, beyond the linearized regime that this chapter operates in? | Open; nonlinear backreaction work deferred per [Ch 1 §11](01-foundation.md). |
