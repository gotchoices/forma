# Chapter 8 — Shear and fractional charge

This chapter turns on the off-diagonal shear σ_uw and examines what it adds to the framework. So far the framework has worked with the bare diagonal metric (σ_uw = 0); this chapter introduces shear as a parameter and traces its consequences through the inventory.

The chapter has three main payloads. First, it derives shear's structural effect on the closure-satisfying primitive spectrum — the **σε product** selects which T(1, n) primitive is lightest, with the lightest mass sitting at exactly M = (ℏ/c)·(2π/L_w) for integer σε. Second, it quantifies the chirality-bias result of [Chapter 6 §6](06-handedness-and-pairs.md) — σ_uw breaks both single-axis chirality reflections (R_u and R_w) and preserves only joint reversal R_J, with the **R_w-conjugate split** between (m, n) and (−m, n) carrying the framework's chirality-bias content. Third, it examines the **fractional-charge structure** of multi-component links of the form k × T(1, n') — committing the framework to the Configuration-Y reading (k phased copies of a T(1, n') primitive, with k surviving gauge-potential cross-terms and 1/k charge associated per component) — and reports honestly that **linear theory does not by itself select a preferred k**.

The shear-alone analysis in this chapter is the σ-side of a broader (σ, ε) story. How σ and ε *together* produce the framework's three qualitative sheet types — and how the metric structure of a specific sheet can be derived from its measured properties — is the work of the planned [Chapter 9](#9-whats-next) (currently scoped in work-ch9.md). Ch 8 sets up shear's mechanisms; Ch 9 will bring them together with ratio.

**Framing convention.** Where standard-physics terminology appears — "quarks," "fractional charge," "P-violation" — it is used as **reference targets** for what the framework's structural mechanisms could correspond to. The framework's commitments are derived from its own machinery; correspondence is downstream comparison work.

**Inheritance.**

- *From [Chapter 1 §4](01-foundation.md):* the σ_uw shear definition, the metric form with shear active, the binding positive-definiteness bound |σ_uw| < 1, and the relationship to the lattice-shear coefficient s = σ_uw/ε used by R-track studies.
- *From [Chapter 5 §4](05-metric-self-consistency.md):* the wrap-order-asymmetric standing-wave construction defining the natural particle at σ = 0. The construction extends to σ ≠ 0 under the single-Bloch-mode interpretation developed in §2.2 below.
- *From [Chapter 6 §6](06-handedness-and-pairs.md):* the chirality-bias structure under shear. This chapter quantifies the bias and tracks its consequences for the gauge-potential analysis.
- *From [Chapter 7 §6](07-aspect-ratio-and-character.md):* the finding that ε alone does not select multi-component-link character; this chapter examines whether σ_uw provides the missing mechanism.
- *From [metric-mass Chapter 7](../metric-mass/07-shear-and-bias.md):* the 1D-compact shear-bias analysis. metric-mass's σ_Su shear is structurally distinct from metric-charge's σ_uw: they couple different wavenumber pairs and break different symmetries. See [Chapter 6 §6.5](06-handedness-and-pairs.md) for the comparison.

**Distinctive job.** Characterize how σ_uw modifies the closure-satisfying primitive spectrum, the chirality structure, and the multi-link inventory at the linearized level — and report honestly what linear theory does and does not derive about the fractional-charge value k.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | Setting up shear σ_uw |
| 2 | Effects on the mass spectrum — the σε product |
| 3 | Chirality bias from shear |
| 4 | The closure condition under shear |
| 5 | Multi-component links — Configuration X vs Configuration Y |
| 6 | k-selection — linear-theory degeneracy and the φ⁴ candidate |
| 7 | The fractional-charge prediction |
| 8 | Summary — what shear adds to the inventory |
| 9 | What's next |

---

## 1. Setting up shear σ_uw

Restate the metric with shear active (from [Chapter 1 §4](01-foundation.md)):

<!-- ds² = -c² dt² + dS₁² + dS₂² + du² + 2 σ du dw + dw² -->
$$
ds^2 = -c^2\,dt^2 + dS_1^2 + dS_2^2 + du^2 + 2\,\sigma_{uw}\,du\,dw + dw^2
$$

The (u, w) sub-block is:

<!-- (u, w) sub-block -->
$$
g^{(u,w)}_{ab} = \begin{pmatrix} 1 & \sigma_{uw} \\ \sigma_{uw} & 1 \end{pmatrix},
\qquad \det g^{(u,w)} = 1 - \sigma_{uw}^2
$$

Per [Ch 1 §4](01-foundation.md), **|σ_uw| < 1 is binding** — a positive-definiteness requirement of the (u, w) sub-block, not a parametrization artifact. We write σ ≡ σ_uw where context is unambiguous.

The wave equation acquires cross-terms from the off-diagonal inverse metric:

<!-- Laplacian with σ shear -->
$$
\nabla_{(u,w)}^2 \;=\; \frac{1}{1-\sigma^2}\left(\partial_u^2 - 2\sigma\,\partial_u\partial_w + \partial_w^2\right)
$$

Periodicity remains rectangular in (u, w) coordinates (per [Ch 1 §9](01-foundation.md)); the shear lives in the metric, not in the lattice. (R-track studies use the lattice-shear parametrization with shear coefficient s = σ_uw/ε on a flat metric with sheared periodicities; the two parametrizations describe the same physical sheet but use different numerical labels for the shear and diverge at second order — see [Ch 1 §4](01-foundation.md). This chapter uses σ_uw throughout, consistent with the rest of the framework.)

---

## 2. Effects on the mass spectrum — the σε product

### 2.1 Dispersion under shear

For a Bloch mode φ ∝ exp(i(k_u u + k_w w − ωt)) with k_u = 2πn/L_u (ring) and k_w = 2πm/L_w (tube):

<!-- ω²/c² = k_S² + (k_u² - 2σ k_u k_w + k_w²)/(1-σ²) -->
$$
\frac{\omega^2}{c^2} \;=\; k_S^2 \;+\; \frac{k_u^2 - 2\sigma\,k_u\,k_w + k_w^2}{1 - \sigma^2}
$$

Rest mass-squared (k_S = 0):

<!-- m²_(m,n) = M²·(1/(1-σ²))·(n²/ε² - 2σmn/ε + m²) -->
$$
m_{(m,n)}^2 \;=\; \frac{M^2}{1-\sigma^2}\left[\frac{n^2}{\varepsilon^2} - \frac{2\sigma\,mn}{\varepsilon} + m^2\right]
$$

with M ≡ (ℏ/c)·(2π/L_w). Define the dimensionless coefficient:

<!-- μ²(m, n; σ, ε) = n²/ε² - 2σmn/ε + m² -->
$$
\mu^2(m, n;\,\sigma, \varepsilon) \;\equiv\; \frac{n^2}{\varepsilon^2} - \frac{2\sigma\,mn}{\varepsilon} + m^2
$$

so m²_{(m,n)} = M²·μ²/(1−σ²). The (1−σ²)⁻¹ factor is a global rescaling that affects every (m, n) uniformly; the σ-dependent *structure* of the spectrum lives in μ². Several structural observations follow directly from the bilinearity of the cross-term −2σmn/ε:

- **The cross-term is invariant under (m, n) ↔ (−m, −n)** (joint sign flip, which leaves mn unchanged). Sign-conjugate partners remain mass-degenerate under shear; the R_J reflection of [Chapter 6](06-handedness-and-pairs.md) is preserved.
- **The cross-term flips sign under (m, n) ↔ (m, −n)** (R_u: ring-chirality reflection — n, the ring winding, flips → k_u flips). R_u-conjugate Bloch modes acquire mass splits proportional to σmn/ε.
- **The cross-term flips sign under (m, n) ↔ (−m, n)** (R_w: tube-chirality reflection — m, the tube winding, flips → k_w flips). R_w-conjugate Bloch modes also split.
- σ_uw thus breaks *both* single-axis chirality reflections (R_u and R_w) by the same algebraic amount (μ² split of 4σmn/ε) and preserves only R_J.

§3 develops the R_u/R_w/R_J distinction's physical consequences. First, we address what "the particle" means under shear.

### 2.2 The natural particle under shear

[Chapter 5 §4](05-metric-self-consistency.md) defines the natural particle for a closure-satisfying mode as the **R_u-symmetrized** combination (m, n) + (m, −n) at equal amplitude — enforcing the wrap-order's ring-direction reflection as a particle symmetry (n is the ring winding under the new tuple convention; R_u flips n). At σ = 0, R_u is exact: the two R_u-conjugate Bloch modes have identical mass, and the equal-amplitude combination is a stationary state of the wave equation.

Under σ ≠ 0, R_u is broken (per §2.1). The two Bloch modes (m, n) and (m, −n) acquire different masses:

<!-- μ²(m, n) - μ²(m, -n) = -4σmn/ε -->
$$
\mu^2(m, n) - \mu^2(m, -n) \;=\; -\frac{4\sigma\,mn}{\varepsilon}
$$

The equal-amplitude R_u-symmetrized combination is no longer stationary; it oscillates between the two mass eigenstates with period proportional to 1/Δm. Chapter 5 §4's σ = 0 natural-particle construction does not strictly transfer.

**This chapter commits to the single-Bloch-mode interpretation of the natural particle under shear.** The particle at the (m, n) sector is the single Bloch mode itself, with mass μ²(m, n; σ, ε) as in §2.1. The wrap-order selects which chirality sector — by convention, the sign of n (the ring winding) for which μ² is lower at the operating σ. For mn > 0 with σ > 0: μ²(m, n) < μ²(m, −n), so positive-mn is the picked sector. Flipping σ flips the pick. This is the structural locus of the chapter's intra-particle chirality bias (§3).

The σ = 0 R_u-symmetrized construction recovers as a small-σ limit: the chirality-eigenstate basis and the mass-eigenstate basis coincide at σ = 0 and rotate together as σ grows. At any σ > 0, the single Bloch mode is what the framework counts as "the particle." Sign-conjugate pairs (m, n) ↔ (−m, −n) remain mass-degenerate under shear (R_J preserved); the [Chapter 6 §4](06-handedness-and-pairs.md) sign-conjugate cancellation construction operates the same at σ ≠ 0 as at σ = 0.

Per [Ch 1 §10](01-foundation.md)'s classification, only T(1, n') primitives and their k-component repetitions k × T(1, n') are closure-satisfying. Bloch modes at (m, n) with the gcd-reduced primitive having tube winding |m'| > 1 are off the closure-satisfying lattice — read as harmonic content, composite states, or spatially separated multi-primitive configurations rather than as new fundamental sectors. The single-Bloch-mode commitment above applies to the closure-satisfying inventory; downstream development assumes the primitive (1, n) form.

(A consequence: under shear, the surviving cross-term pattern (T_tu, T_tw, T_uw) under the single-Bloch-mode construction differs from the σ = 0 R_u-symmetrized version — h_μu and h_uw are sourced in addition to h_μw. The wrap-order convention of [Ch 1 §10](01-foundation.md) selects h_μw as the gauge potential regardless of regime; h_μu's nonzero contribution at σ ≠ 0 is the **mass-direction metric perturbation** — structurally analogous to gravitational frame-dragging rather than to a second gauge potential. See [Ch 5 §4.6.5](05-metric-self-consistency.md) for the explicit treatment.)

### 2.3 The σε product — the structural lever for closure-satisfying primitives

For a closure-satisfying T(1, n) primitive (tube winding m = 1, ring winding n):

<!-- μ²(1, n; σ, ε) = n²/ε² - 2σn/ε + 1 -->
$$
\mu^2(1, n;\,\sigma, \varepsilon) \;=\; \frac{n^2}{\varepsilon^2} - \frac{2\sigma\,n}{\varepsilon} + 1
$$

Complete the square in n:

<!-- μ²(1, n) = (n/ε - σ)² + (1 - σ²) -->
$$
\mu^2(1, n) \;=\; \left(\frac{n}{\varepsilon} - \sigma\right)^{\!2} + (1 - \sigma^2)
$$

A parabola in n with minimum at **n_opt = σε**, where μ²_min = 1 − σ². Restoring the (1−σ²)⁻¹ factor:

<!-- m²_phys(1, n_opt) = M² -->
$$
m^2_\text{phys}\bigl(1, n_\text{opt}\bigr) \;=\; M^2 \cdot \frac{1 - \sigma^2}{1 - \sigma^2} \;=\; M^2
$$

**The minimum mass of the lightest T(1, n) primitive is exactly M, independent of σ — for any (σ, ε) such that σε is integer.** The σ-dependence cancels between μ²_min = 1 − σ² and the global (1−σ²)⁻¹ rescaling. The lightest closure-satisfying primitive sits at exactly the natural mass scale M = (ℏ/c)·(2π/L_w); its identity (which integer n) shifts with σε, but its mass does not.

n must be a positive integer; σε generally is not. Let n̂ = round(σε) (the nearest positive integer ≥ 1). The actual minimum is

<!-- m²_phys = M²·[1 + Δ²/(1-σ²)],  |Δ| ≤ 1/(2ε) -->
$$
m^2_\text{phys} \;=\; M^2\left[1 + \frac{\Delta^2}{1 - \sigma^2}\right],
\qquad \Delta \;\equiv\; \frac{\hat n}{\varepsilon} - \sigma,\quad |\Delta| \le \frac{1}{2\varepsilon}
$$

For ε ≫ 1, the residual Δ²/(1−σ²) is small and the lightest closure-satisfying primitive sits at ≈ M for any σ. For ε ≲ 1, the residual is order unity and the mass sits noticeably above M except at special σε values that put n_opt exactly on an integer.

**Level crossings.** Two adjacent T(1, n) primitives are mass-degenerate at σε = n + 1/2:

<!-- σε = n + 1/2 → T(1, n) and T(1, n+1) degenerate -->
$$
\sigma\varepsilon \;=\; n + \tfrac{1}{2} \;\implies\; \mu^2(1, n) = \mu^2(1, n+1)
$$

So T(1, 1) is the lightest closure-satisfying primitive for σε < 1.5, T(1, 2) for 1.5 < σε < 2.5, and so on. At a crossing, both primitives sit at μ² = 1/(4ε²) + (1−σ²) — slightly above the M-mass minimum.

**No simultaneous three-fold degeneracy.** For T(1, n−1), T(1, n), T(1, n+1) to be all three degenerate, two pairwise crossings would have to coincide: σε = n − 1/2 *and* σε = n + 1/2. Impossible. Near-three-fold-degeneracy (three primitives separated only by residuals of order 1/ε²) is an ε ≫ 1 phenomenon, not a special σε value.

The σε product is therefore the structural lever for closure-satisfying primitive selection under shear: it picks out n_opt = round(σε), drives the spacing of nearby primitives, and locates the level crossings. The σ-alone or ε-alone view of these effects is partial; **the combined σε product is what controls them**.

The σε result depends on the metric-shear parametrization where the (1−σ²)⁻¹ factor exactly cancels the parabola minimum's (1−σ²) value. This cancellation is structural to the framework's choice in [Ch 1 §4](01-foundation.md). The combined (σ, ε) regime structure — including what happens near the σ → 1 boundary and how the three sheet types map onto regions of the (σ, ε) plane — is the planned [Ch 9](#9-whats-next)'s work.

---

## 3. Chirality bias from shear

Per §2.1, σ_uw breaks both single-axis chirality reflections (R_u and R_w) and preserves only joint reversal R_J. The R_u-broken split is between (m, n) and (m, −n) — what would have been the natural particle's two components at σ = 0 (R_u flips n, the ring winding). The R_w-broken split is between (m, n) and (−m, n) — the chirality-conjugate pair under tube-direction reflection (R_w flips m, the tube winding). The two splits are equal in magnitude (4σmn/ε in μ²) but play distinct physical roles:

| Pair | Δμ² under shear | Physical role |
|---|---|---|
| (m, n) ↔ (m, −n) — **R_u-conjugate** | 4σmn/ε | Ring-chirality split — natural-particle symmetrization axis at σ = 0 (now broken; particle is single Bloch mode) |
| (m, n) ↔ (−m, n) — **R_w-conjugate** | 4σmn/ε | Tube-chirality split — the framework's chirality-bias variable |
| (m, n) ↔ (−m, −n) — **R_J-conjugate** | 0 | Sign-conjugate pair — mass-degenerate under shear |

### 3.1 Mass splits, explicit

From the dispersion of §2.1, the four sign combinations of (m, n) at fixed magnitudes (|m|, |n|) have mass-squared values:

| Mode | k_u·k_w | μ² |
|---|---|---|
| (m, n) and (−m, −n) | +K_u K_w | n²/ε² − 2σ|mn|/ε + m² |
| (m, −n) and (−m, n) | −K_u K_w | n²/ε² + 2σ|mn|/ε + m² |

The two R_J-conjugate partners (m, n) and (−m, −n) sit at the same mass; the two R_w-conjugate partners (m, n) and (−m, n) sit at masses that differ by 4σ|mn|/ε. For small σ, the leading split is:

<!-- Δm²/m² ≈ 4σ K_u K_w / (K_u² + K_w²) -->
$$
\frac{\Delta m^2}{m^2_{\sigma = 0}} \;\approx\; \frac{4\sigma\,K_u K_w}{K_u^2 + K_w^2} \;+\; \mathcal{O}(\sigma^2)
$$

(σ² corrections come from the (1−σ²)⁻¹ denominator and are set aside at the linearized level.)

### 3.2 What the chirality bias means dynamically

Under thermal equilibrium with σ ≠ 0, the populations of (m, n) and (−m, n) Bloch modes are unequal — Boltzmann-suppressed by Δm². A configuration prepared with equal amplitudes of the two R_w-conjugate components is not in thermal equilibrium and would redistribute toward the lower-energy chirality unless prevented by a conservation law. This is the dynamical chirality bias that σ_uw produces.

Under the single-Bloch-mode interpretation of §2.2, the wrap-order selects which Bloch mode is "the particle" — the one with lower mass under the operating σ. The R_u-conjugate partner sits at higher mass; the R_w-conjugate partner sits at higher mass and represents a chirality-flipped configuration. Both are physically distinct states from "the particle," with different (m, n) labels and different observable consequences.

### 3.3 What σ_uw does not do — the matter/antimatter question

σ_uw provides **chirality bias**, not sign-reflection bias. The R_J pair (m, n) ↔ (−m, −n) — the framework's candidate matter/antimatter labeling per [Chapter 6 §3](06-handedness-and-pairs.md) — is mass-degenerate under shear. **σ_uw therefore biases chirality within a particle, not matter/antimatter populations.**

This is structurally distinct from [metric-mass Chapter 7 §6](../metric-mass/07-shear-and-bias.md)'s σ_Su shear, whose cross-term k_S·k_u flips sign under single-axis flip alone (metric-mass's 1D-compact index) and breaks the sign-reflection symmetry. The two shears couple different wavenumber pairs and break different symmetries; σ_uw is *not* the 2D-compact extension of σ_Su.

The framework's σ_uw shear does not provide a Sakharov-CP-violation analog in the matter/antimatter sense. Standard Sakharov requires both C and P violation; σ_uw provides P-flavor (chirality) bias only. The C-flavor (sign-reflection) side has no derived mechanism here. Earlier framings (pre-refactor) conflated the two; the math distinguishes them clearly.

**Whether the framework derives a matter/antimatter bias from any mechanism is left open.** Candidates the framework's broader stack might supply such a mechanism are summarized in [Chapter 6 §6.7](06-handedness-and-pairs.md): a different shear (σ_Su or σ_Sw, not currently in the metric), substrate-level chirality from grid-primitive / grid-duality, or a structural mechanism not yet identified. None is committed to here; the math is honest about what σ_uw alone does and does not do.

---

## 4. The closure condition under shear

Does the closure condition itself change under σ ≠ 0?

The chirality criterion of [Chapter 1 §10](01-foundation.md), with the operational synchronization condition m | n on (m, n) integer labels, is stated in the bare-metric basis. Under shear, the geometric relationship between "winding on u" and "winding on w" becomes entangled through the sheared metric — a single closed traversal in the rectangular (u, w) basis advances along a curve whose geometric length and orientation depend on σ.

Two ways to interpret:

- **Conservative:** the closure condition operates on (m, n) labels in the bare basis. Shear is a perturbation that affects masses and dispersion but not the closure condition itself. (m, n) labels remain meaningful.
- **Sheared-basis:** the closure condition is naturally stated in coordinates aligned with the sheared metric, where the relevant labels are linear combinations of (m, n) involving σ.

The chapter takes the **conservative interpretation**: closure operates on (m, n) labels in the bare basis; shear modifies dispersion but not the closure rule. This is consistent with closure being a chirality criterion on the closed curve in 3-space, which depends on the curve's topology rather than on the metric in which the wave propagates. The downstream consequence — which (m, n) configurations carry observable EM under shear — is identical to the bare-metric inventory of [Chapter 4](04-the-closure-condition.md).

---

## 5. Multi-component links — Configuration X vs Configuration Y

[Chapter 4 §4.3a](04-the-closure-condition.md) describes a closure-satisfying multi-component link of the form T(k, k·n') = k × T(1, n') as "k phased copies of a T(1, n') primitive, with each component carrying 1/k of the link's total charge." Under linear theory, this phrase admits two physically distinct interpretations that must be distinguished before the link's energetics and gauge structure can be analyzed.

### 5.1 Two interpretations

**Configuration X — single Bloch mode at (k, k·n').** A single excitation with wavevector (k_u, k_w) = (2πk·n'/L_u, 2πk/L_w). The wave function has k·n'-fold ring structure and k-fold tube structure. Mass read directly off the dispersion at (k, k·n'):

<!-- m²_X(k, k·n') = (M²/(1-σ²))·k²·μ²(1, n'; σ, ε) -->
$$
m^2_\text{X}(k, k\cdot n') \;=\; \frac{M^2}{1-\sigma^2}\cdot k^2\,\mu^2(1, n')
$$

so m_X = k · m(1, n'). The [Chapter 5 §4](05-metric-self-consistency.md) gauge-potential derivation, applied to this mode, gives *one* surviving cross-term h_μw — one gauge potential per such Bloch mode.

**Configuration Y — k phased copies of T(1, n').** A superposition of k Bloch modes at the same wavevector (2πn'/L_u, 2π/L_w) but at distinct phase positions:

<!-- ψ_Y = Σ_j A·exp(i(k_u u + k_w w + 2πj/k - ωt)) -->
$$
\psi_\text{Y} \;=\; \sum_{j=0}^{k-1} A\cdot e^{i(k_u u + k_w w + 2\pi j/k - \omega t)}
$$

Each component contributes its own primitive mass; total mass is k · m(1, n') by additivity. Each component sources its own h_μw — **k surviving cross-terms total**, organized as k phased copies of the primitive's gauge structure.

The two configurations have *identical total mass* at the linearized level (both equal to k · m(1, n')). They differ in their *gauge-potential structure*: Configuration X has one gauge potential per multi-link instance, Configuration Y has k.

### 5.2 The framework commits to Configuration Y

[Chapter 4 §4.3a](04-the-closure-condition.md)'s phrasing — "k phased copies" — and the framework's "1/k charge per component" structural claim are both natural under Configuration Y. Under X, the per-component charge interpretation is not available; the link carries integer charge k·n' as a single mode.

This chapter therefore reads "k × T(1, n') multi-link" as **Configuration Y throughout**. Consequences:

- **Total mass:** k · m(1, n') — same as k separate independent primitives at the same wavevector.
- **Gauge structure:** k surviving h_μw cross-terms per multi-link.
- **Charge per component:** 1/k of the link's integer total charge.
- **Closure:** the link satisfies closure iff each component does (each is T(1, n'), m=1 trivially divides any n').

(A propagation note: [Chapter 4 §4.3](04-the-closure-condition.md) and [Chapter 5 §4](05-metric-self-consistency.md) have been tacitly using the Configuration-Y reading without making the choice explicit. The commitment here should be propagated to those chapters in a coordinated pass. [STATUS](STATUS.md) flags this as a follow-on.)

### 5.3 Energetics under shear, per-component

Under Configuration Y, each component of a k × T(1, n') multi-link is a phase-shifted copy of the primitive T(1, n') at the same wavevector. Each component's individual mass is m(1, n') — the σε analysis of §2.3 applies to the primitive directly. The total link mass scales linearly with k.

Phase-shifts within the (u, w) cycle do interact with the shear cross-term −2σ k_u k_w in mode-dependent ways. Specifically: with the k components at phases 2π·j/k for j = 0, ..., k−1, the total energy summed over components contains cross-terms between different j values that depend on σ and on the specific phase distribution. The chapter computes this sum in §6 and asks: at what k is the configuration most energetically favorable under shear?

---

## 6. k-selection — linear-theory degeneracy and the φ⁴ candidate

§5 established that a Configuration-Y multi-link has total mass k · m(m', 1) at the linearized level. This section examines whether shear selects a preferred k. The honest finding: **linear scalar-field theory does not.** The chapter identifies the linear-adjacent mechanism (φ⁴ inter-component coupling) as the candidate within the framework's scope, and forwards the open calculation.

### 6.1 Linear-theory non-derivability of k_opt

Under Configuration Y, two configurations of total integer charge k carry identical total energy at the linearized level:

- **One instance of a k × T(1, n') multi-link:** total mass k · m(1, n'), gauge structure k-fold (k surviving h_μw cross-terms).
- **k separate independent T(1, n') primitives:** total mass k · m(1, n'), gauge structure k-fold (one cross-term per primitive, k total).

Linear theory does not distinguish "1 instance of the k-link as a single bound configuration" from "k separate primitives." They have identical total energy density and identical gauge-potential structure. Any optimization over k is therefore degenerate.

So the question "what k minimizes E(k; σ, ε, n')?" — asked of pure linearized scalar-field analysis — has the answer: **all k are degenerate at the energy level. No preferred k emerges from energetic minimization.**

This is a substantive negative finding. A real k-selection requires a structural ingredient distinguishing the bound k-link from k independent primitives. That ingredient is not in linear theory.

### 6.2 Phase coherence — a negative finding

The most promising *linear-theory* candidate for distinguishing the k-link from k independent primitives is phase coherence around the link's closed curve. The hope: in a sheared metric, going around a multi-link curve picks up holonomy phases that depend on σ, and Z_k commensurability of these phases selects specific k.

Compute phase advance around a T(1, n') primitive once: traversal Δu = n'·L_u (ring), Δw = L_w (tube); the Bloch mode at wavevector (2πn'/L_u, 2π/L_w) accumulates phase:

<!-- Δφ = k_u · n' L_u + k_w · L_w = 2π(n'² + 1) -->
$$
\Delta\varphi \;=\; k_u\,n' L_u + k_w\,L_w \;=\; 2\pi(n'^2 + 1)
$$

This is 2π × integer regardless of σ. Phase coherence is automatic for integer-winding modes; **no σ-dependence enters the phase advance**.

Per Configuration Y, each component of the multi-link traces its own primitive curve with the same phase advance 2π(n'² + 1). The relative phases {2π·j/k} between components are *imposed by the configuration* (they define which Y-configuration is meant), not *derived from σ*.

**Pure linear scalar-field theory therefore does not produce σ-dependent phase-coherence constraints that select specific k.** Shear enters the energy via the dispersion's cross-term, but not the phase coherence of going around integer-winding closed curves. Phase coherence is *not* the linear-theory mechanism for k-selection.

### 6.3 Internal-mode dynamics — the linear-adjacent φ⁴ candidate

What is *almost* linear theory but actually does give k-selection: **internal-mode dynamics of the multi-link with shear-induced inter-component coupling.**

A multi-link with k components has internal degrees of freedom — relative phases (and amplitudes) of the components. In pure linear scalar-field theory these are free parameters; the components do not interact. Adding the smallest departure from pure linear theory — a quadratic-in-amplitude inter-component coupling of the form

<!-- L_coupling = -λ · Σ_{j ≠ j'} φ_j² φ_{j'}² -->
$$
\mathcal{L}_\text{coupling} \;=\; -\lambda \sum_{j \ne j'} \varphi_j^2\,\varphi_{j'}^2
$$

— introduces dynamics among the relative phases. Under shear, this coupling acquires σ-dependent modulation through the cross-term in each component's kinetic energy. The internal modes (relative-phase oscillations between the k components) form a k-dimensional system with a σ-dependent coupling matrix. Stability and energy ordering depend on k. For specific (σ, ε), specific k may have the lowest-energy stable internal-mode configuration.

This mechanism is **outside metric-charge's declared scope** per [Chapter 1 §11](01-foundation.md)'s explicit deferral of nonlinear backreaction: the φ⁴ self-coupling is a nonlinear self-interaction term, and the framework does not undertake its analysis. The calculation — write the φ⁴ self-interaction energy of a k-component link on a sheared sheet, minimize over k, report which k wins — is therefore forwarded to [metric-binding](../metric-binding/), which is the project specifically charged with multi-knot energetics (binding, separation, inter-component dynamics).

metric-charge identifies the mechanism as the closest linear-adjacent candidate so that downstream work has a concrete target; the actual calculation lives in metric-binding's territory. If k = 3 emerges at the regime where production studies' empirical optimization (R60, R63, R64) finds k = 3 numerically, the framework has the candidate first-principles derivation. If not, k-selection comes from substrate Z_k via grid-duality (§6.4(b)) or another route.

### 6.4 Other candidate mechanisms

Ordered by closeness to the framework's existing apparatus:

| Mechanism | Status |
|---|---|
| **(a) Internal-mode dynamics with σ-induced coupling (§6.3).** | Nonlinear self-interaction; forwarded to [metric-binding](../metric-binding/) per [Ch 1 §11](01-foundation.md). |
| **(b) Substrate Z_k from grid-duality.** Z_k constraint at L3 forces specific k. | Forwarded to [grid-duality §8](../grid-duality/08-where-alpha-appears.md). |
| **(c) Confinement-like binding.** k components bound by interaction with separation cost. | Forwarded to [metric-binding](../metric-binding/). |
| **(d) Pauli-like exclusion.** Requires spin/statistics commitment not yet made. | Out of scope. |
| **(e) Topological commensurability under shear.** Basis-rephrasing in lattice-shear coordinates. | Open (may resolve within metric-charge once σ ↔ s translation is worked out — see [Ch 9 §6](09-ratio-and-shear.md)). |

### 6.5 The framework's commitment

Linear scalar-field theory on a sheared 2D-compact substrate gives no preferred k. The σε product of §2.3 selects n_opt for primitives; it does not select k for multi-links.

The framework's commitment: **k-selection is forwarded.** Per [Chapter 1 §11](01-foundation.md)'s deferral of nonlinear backreaction, mechanisms (a) and (c) of §6.4 are forwarded to [metric-binding](../metric-binding/) as multi-knot energetics; mechanism (b) is forwarded to [grid-duality §8](../grid-duality/08-where-alpha-appears.md) as substrate input. metric-charge does not derive k.

What metric-charge *does* deliver: §7 below works through the *structural* consequences of a k-component multi-link configuration — what fractional-charge structure it produces and how that's consistent with grid-duality's integer quantization — assuming a k has been selected by some downstream mechanism. The structural analysis is independent of which mechanism selects k.

---

## 7. The fractional-charge prediction

### 7.1 The combined picture

Combine §§5 and §6:

- Under shear, multi-component closure-satisfying links of the form k × T(1, n') are structurally available (per the closure rule of [Chapter 4 §4.3](04-the-closure-condition.md), with Configuration-Y reading per §5).
- Some mechanism — internal-mode dynamics (§6.3), substrate Z_k (§6.4(b)), or other — selects a specific k (call it k_sel; for present purposes its value is left open per §6.5).
- For a k_sel-component multi-link, each component is associated with 1/k_sel of the link's total integer charge.

### 7.2 Consistency with grid-duality's integer quantization

Per [grid-duality §7.5.4](../grid-duality/07-wrap-promotion-modeling.md), winding numbers are integer-valued and conserved. At first glance this conflicts with the per-component "1/k_sel fractional charges" above. The conflict is only apparent.

Grid-duality's integer quantization applies at the level of *complete closure-satisfying configurations*. A k-component link T(k, k·n') is a single topological object — one winding pattern with definite integer (k, k·n'). The link as a whole carries integer charge under the quantization rule. The "1/k_sel charge per component" is not a *fractional charge of an individual closure-satisfying mode* — it is the *fractional association* of the link's integer total charge with each of its k structural components.

Three points clarify the consistency:

- **Components are not closure-satisfying on their own.** A single component of a multi-link, considered in isolation, is just a single (m, n) mode at primitive winding. Whether that single (m, n) satisfies closure depends on the chirality-criterion alignment requirement (per [Ch 4 §1](04-the-closure-condition.md)). For the multi-link case, it is the *collective configuration* (all k components together in the proper phase distribution) that satisfies closure as a single integer-winding object. Individual components are *fragments* of the configuration, not closure-satisfying configurations themselves.

- **Integer total charge is preserved.** The full multi-link has charge proportional to its winding (k, k·n') — integer-valued in the grid-duality sense. Distributing the link's integer total across k components gives 1/k per component, but the total integer is unchanged. No quantization rule is violated.

- **Confinement-like consequence.** Because individual components are not closure-satisfying alone, they are not isolable as physical states — they only exist as parts of the collective k-link. This is structurally analogous to what standard physics calls quark confinement: individual quarks carry fractional charge and are not observable in isolation; only color-neutral composite states are.

So the framework's fractional-charge structure is consistent with grid-duality's integer winding quantization, and predicts confinement-like behavior as a structural consequence: per-component fractional values exist only inside the collective configuration, with integer total preserved.

### 7.3 What is and is not yet proven

Three distinct claims about fractional charge sit in this chapter; separating what the framework derives from what it leaves open:

**Proven (structurally):**

- *Fractional-charge configurations exist as closure-satisfying states.* Multi-component links of the form k × T(1, n') satisfy the closure rule ([Ch 4 §4.3](04-the-closure-condition.md)); each component carries 1/k of the link's integer total charge as a structural fact of the multi-link decomposition under Configuration Y (§5). The 1/k per component is not a separate physical postulate — it falls out of the link's geometry plus integer total quantization.
- *Components are not closure-satisfying alone.* A single T(1, n') primitive at a phase position within a k × T(1, n') link does not satisfy the closure rule in isolation; only the collective configuration closes.

**Open at the linear-theory level:**

- *Which k is selected.* §6 establishes that linear theory does not pick a specific k. The framework's specific prediction (e.g., k_sel = 3 for the hadronic regime) depends on the φ⁴ inter-component calculation or substrate Z_k input. Until carried out, the framework predicts that *some* k-component structure exists, not that k = 3.

**Not proven — and forwarded to [metric-binding](../metric-binding/):**

- *Whether fractional-charge states are stable in time.* The structural prediction is that components cannot exist in isolation as closure-satisfying configurations — consistent with confinement-like behavior. But "cannot exist in isolation as closure-satisfying" is weaker than "cannot exist in isolation at all": a component without closure would be a mass-only mode (single-axis or non-synchronizing diagonal), which is a permitted state in the framework, just not a charged one. Whether the energetic cost of separating one component from a multi-link is finite-but-large (giving long-lived but separable states) or genuinely infinite-in-the-limit (true confinement) requires an explicit energetics calculation across the separation.
- *The energy cost of separation as a function of distance.* For two parts of a multi-link pulled apart in (S₁, S₂), what does E(separation) look like? Standard physics' quark confinement comes from a linear potential at large distances (string tension); whether the framework reproduces that, or some other functional form, is a multi-knot energetics calculation.
- *Whether fractional-charge components can be created/destroyed independently.* Linear theory (this project) conserves (m, n) labels exactly; pair creation/annihilation is a nonlinear/quantum phenomenon outside scope here.

The "is fractional charge stable / can it be observed in isolation?" question is fundamentally a multi-knot energetics question — it requires comparing the energy of a multi-link configuration to the energy of its separated components as a function of separation. That calculation is the subject of [metric-binding](../metric-binding/), the follow-up project specifically focused on multi-knot configurations and binding energetics.

This chapter's claim is therefore: **fractional charge structurally exists** (as the per-component association inside closure-satisfying multi-links) **and structurally requires the collective configuration** (since components alone fail closure). **The value of k is not derived in linear theory** and is forwarded to either an internal φ⁴ calculation or substrate Z_k input. **The dynamical stability of components — whether they can be ripped apart, with what energy cost — is forwarded to metric-binding.**

### 7.4 Mixed-orientation compounds — structural inventory

§§7.1–7.3 work with uniform-phase Configuration Y: all k components of a k × T(1, n') multi-link share the same primitive (e.g., all T(+1, n')), so per-component charge sign is uniform and the link's external integer charge is ±k. This is what the framework's structural derivation gives for a single coherent k × T(1, n') multi-link.

A broader class of configurations sits in the framework's mode-language inventory by construction: **mixed-orientation compounds**, where different components of a multi-mode configuration carry different orientations of the primitive. A field configuration containing three independent Bloch modes at, say, (+1, n'), (+1, n'), and (−1, n') is a superposition of three Bloch modes — each evolving in its own conserved (m, n) sector under the linearized wave equation — admissible by linear superposition without new mechanism. Its external integer charge follows the same tube-winding-sum rule (per [Ch 6 §2.4](06-handedness-and-pairs.md), charge sign tracks the sign of p^w = ℏ·(2π/L_w)·m) that governs the uniform case:

| Compound | Per-component charges | External integer charge (tube-winding sum) |
|---|---|---|
| 3 × T(+1, n') (uniform) | +1, +1, +1 | +3 |
| 2 × T(+1, n') + 1 × T(−1, n') | +1, +1, −1 | +1 |
| 1 × T(+1, n') + 2 × T(−1, n') | +1, −1, −1 | −1 |
| 3 × T(−1, n') (uniform) | −1, −1, −1 | −3 |

R_J-conjugates (e.g., replacing T(+1, n') by T(−1, −n') throughout) give the antiparticle direction of each row at identical mass per [Ch 6 §2.4](06-handedness-and-pairs.md).

**Metric-charge's structural commitment:** mixed-orientation compounds *exist* in the inventory with the charge arithmetic above. The mode-language is rich enough to describe configurations whose external integer charge is, e.g., +1 with three internal components of mixed sign — a structural building block for the candidate proton-like state.

**Forwarded — binding-mechanism work outside metric-charge's linear scope:**

- **Stability.** Whether a mixed-orientation compound is stable as a bound multi-component object, versus relaxing to its uniform counterpart or separating into independent primitives, is a multi-knot binding-energetics question. Forwarded to [metric-binding](../metric-binding/).
- **Empirical identification.** Whether the 2:1 mixed compound corresponds to standard physics' proton — and what the neutron analog is — is a downstream phenomenology question. The compounds tabulated above all have odd external integer charge for any 3-component configuration of T(±1, n') primitives; a neutral 3-component baryon therefore requires either a different mode-content reading (zero-sum mix involving components that fail closure) or a different framework reading entirely.
- **Integer vs fractional charge reading.** Whether per-component charges read as integer ±1 in framework units or as fractional ±1/3 in standard-model units — a units convention, a deep-inelastic-averaging artifact, or a genuine structural mechanism — is downstream phenomenology, not metric-charge's structural derivation.
- **Alternative readings.** The R-track studies after R60 — [R53-three-generations](../../studies/R53-three-generations/), [R54-compound-modes](../../studies/R54-compound-modes/), [R63-proton-tuning](../../studies/R63-proton-tuning/), [R64-nuclear-harmonic-stack](../../studies/R64-nuclear-harmonic-stack/) — take a structurally different approach: each quark is its own (m, n) mode on the proton sheet, with mass hierarchies from shear-resonance numerics and per-mode charge from a separate phase-locking rule. The proton in that picture is a compound of three independent mode-assignments, not a single 3-component Configuration Y multi-link. R53's unresolved two-shear puzzle (R53 F16, ≈ 19 for up-types vs ≈ 0.8 for down-types on the same physical sheet) is the active barrier to a closed downstream picture. Reconciling the compound-inventory reading with the R-track mode-by-mode reading is downstream binding-side work.

---

## 8. Summary — what shear adds to the inventory

Adding shear σ_uw to the ε-swept inventory of [Chapter 7](07-aspect-ratio-and-character.md):

- **Selects the lightest closure-satisfying primitive via the σε product** (§2.3). n_opt = round(σε) is the integer ring-winding for the lightest T(1, n); at integer σε, the lightest primitive sits at mass exactly M. Level crossings at half-integer σε; no simultaneous three-fold degeneracy.
- **Redefines the natural particle as the single Bloch mode** under shear (§2.2). The σ = 0 R_u-symmetrization breaks at σ ≠ 0; the wrap-order selects a chirality sector by picking the lower-mass Bloch mode.
- **Breaks chirality reflections R_u and R_w independently** (§3). The R_w-conjugate split between (m, n) and (−m, n) is the framework's chirality-bias variable. σ_uw provides P-flavor (chirality) bias only; C-flavor (matter/antimatter) bias is not derived from σ_uw.
- **Commits to Configuration Y for multi-component links** (§5). k × T(1, n') is k phased copies of the primitive, with k surviving h_μw cross-terms and 1/k charge associated per component.
- **Does not by itself select a preferred k** (§6). Linear theory is degenerate. The φ⁴ inter-component candidate (§6.3) is the framework's most-tractable open calculation for first-principles k-selection.
- **Predicts confinement-like behavior for individual components** (§7). Components are not closure-satisfying alone and so are not isolable; integer total charge is preserved as 1/k per component within the collective configuration.
- **Admits mixed-orientation compounds in the mode-language inventory** (§7.4). Configurations such as 2 × T(+1, n') + 1 × T(−1, n') exist as superpositions of independent Bloch modes; external integer charge is the tube-winding sum. Stability and empirical identification are forwarded.

Together with ε from [Chapter 7](07-aspect-ratio-and-character.md) and handedness from [Chapter 6](06-handedness-and-pairs.md), σ_uw gives the framework five structural parameters that organize the closure-eligible inventory:

| Parameter | What it controls |
|---|---|
| (m, n) labels | Primary mode identity (chapters 2, 3) |
| Closure satisfaction | Charge vs no-charge (chapter 4) |
| Handedness sign | Matter/antimatter (chapter 6) |
| Aspect ratio ε | Sheet character / regime (chapter 7) |
| Shear σ_uw | Primitive selection via σε (n_opt = round(σε)); chirality bias; multi-link structure (this chapter) |

This is the framework's structural inventory at the linearized level for a single sheet under given (ε, σ_uw). How σ and ε *together* select sheet character — and how that combined structure can be inverted to recover (ε, σ_uw) from observed sheet properties — is the planned [Chapter 9](#9-whats-next) work.

---

## 9. What's next

[Chapter 9 — Ratio and shear together](09-ratio-and-shear.md).

---

## What this chapter does **not** do

- **Does not derive numerical α** or charge magnitudes. Cited from [grid-duality §8](../grid-duality/08-where-alpha-appears.md); structural location settled there, numerical values open.
- **Does not derive specific quark masses or mixing angles.** The framework predicts the structural pattern (multi-component links with 1/k fractional charge under Configuration Y); specific mass and charge values are downstream MaSt-correspondence work.
- **Does not derive the value of k.** §6 shows linear theory is degenerate. The φ⁴ inter-component calculation that *could* select k is flagged as the open follow-on.
- **Does not derive a matter/antimatter bias mechanism.** §3 shows σ_uw cannot do it. σ_uw provides intra-particle chirality bias only — at most a P-flavor ingredient toward a Sakharov-CP construction; the C-flavor side is not derived. Forwarded to [Chapter 6 §6.7](06-handedness-and-pairs.md) for candidate alternatives.
- **Does not engage the combined (σ, ε) landscape.** The σε product analysis of §2.3 is a per-parameter result; how σ and ε *together* produce the three sheet types, including the σ → 1 single-axis-suppression mechanism that's central to charged-sheet character at large ε, is forwarded to Chapter 9 (planned).
- **Does not redo the four-property gauge-potential test at σ ≠ 0.** [Ch 5 §4.6](05-metric-self-consistency.md)'s test was derived for the σ = 0 R_u-symmetrized particle; the single-Bloch-mode interpretation under shear (§2.2) requires the test to be redone, with potentially different surviving cross-term structure. Flagged as an extension of [TODO-M2](STATUS.md).
- **Does not derive nonlinear shear effects.** Linear theory only. Whether large σ produces qualitatively different behavior beyond linear-approximation breakdown is downstream work.
- **Does not analyze interaction between distinct multi-component links.** Multi-knot energetics is metric-binding territory.
- **Does not derive the dynamical stability of fractional-charge components.** §7.3 establishes structural non-isolability; energetics of separation forwards to [metric-binding](../metric-binding/).
- **Does not explain why σ_uw takes a specific value** on any given sheet. ε and σ are both treated as free parameters; whether they are dynamically determined is open.
- **Does not commit to MaSt-correspondence assignments.** The fractional-charge / multi-component prediction matches the structural pattern of standard physics' quark inventory under k = 3; specific identifications are downstream work.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Does the φ⁴ inter-component coupling calculation (§6.3) yield a specific k_sel at relevant (σ, ε)? Specifically, does k = 3 fall out at the regime where production studies find it numerically? | Follow-on to [TODO-M8(a)](STATUS.md). Within metric-charge's scope if pursued. |
| Are fractional-charge components dynamically stable, or only structurally non-isolable? What is E(separation) for pulling one component out of a k × T(1, n') multi-link? | [metric-binding](../metric-binding/) — multi-knot energetics. |
| Does k-selection ultimately come from local internal-mode dynamics (§6.3), substrate Z_k input from grid-duality (§6.4(b)), or some combination? | Open; needs both candidates pursued. |
| Does the σ_uw chirality bias quantitatively match observed P-violation magnitudes (e.g., parity-violation in weak interactions)? | Downstream MaSt-correspondence work + experimental data. |
| Does the framework derive a matter/antimatter bias from any mechanism? §3 shows σ_uw cannot. Candidates: σ_Su or σ_Sw (different shear, not in current metric); substrate-level chirality from grid-primitive / grid-duality; other unidentified mechanisms. | Project-direction question (see [Chapter 6 §6.7](06-handedness-and-pairs.md)). |
| Under the single-Bloch-mode interpretation of §2.2, does the [Ch 5 §4.6](05-metric-self-consistency.md) four-property gauge-potential test still hold? What is the surviving cross-term pattern (T_tu, T_tw, T_uw)? | Extension of [TODO-M2](STATUS.md). |
| Are there other multi-component links (k = 5, k = 7, ...) energetically favored at specific σ values, corresponding to potential exotic states? | Open follow-up; downstream investigation after §6.3's calculation. |
| Does the framework predict any deviation from standard quark mass / charge ratios that could be experimentally tested? | Open; depends on quantitative completion of the framework. |
| Does the choice of which compact direction is "tube" (closure-asymmetric) vs "ring" force a specific sign convention on σ_uw, or is the sign free? | Convention question; possibly settled by combination of [Chapter 3 §3.2](03-knots-on-the-torus.md) and [Chapter 5 §6.3](05-metric-self-consistency.md). |
