# work-m8a.md — Shear's effect on a particle sheet (Ch 8 scoping)

This file scopes a Chapter 8 refactor focused on **what shear σ_uw does to a particle sheet in isolation** — the spectrum, the gauge structure, the multi-link inventory, and the natural-particle definition under shear. It is the σ-alone half of the broader (σ, ε) story; the combined-parameter content (regime map, three sheet types, σ → 1 principal-axis suppression, parametrization choice) lives in [work-ch9.md](work-ch9.md).

The file responds to [TODO-M8(a)](STATUS.md) and to the prior reviews [review.md](review.md) and [review-m8a.md](review-m8a.md). The central honest finding: **linear theory does not select a preferred k for multi-link configurations.** The σε product selects the lightest closure-satisfying primitive's ring-winding; nothing in pure linear theory selects k for multi-links. Identifying the next-most-tractable mechanism within metric-charge's scope (φ⁴ inter-component coupling) is the load-bearing open work.

Conventions follow the rest of the project ([Ch 1](01-foundation.md): u = ring, w = tube; ε ≡ L_u/L_w; closure rule n | m on (m, n) integer labels). M ≡ (ℏ/c)·(2π/L_w) is the natural mass scale.

---

## Sections

| § | Topic |
|---|-------|
| 1 | The Ch 8 question |
| 2 | Setup — sheet with shear; Bloch-mode-as-particle under shear |
| 3 | Symmetries of the sheared spectrum |
| 4 | The σε product — structural lever for closure-satisfying primitives |
| 5 | Single-axis vs closure-satisfying under shear |
| 6 | Multi-component links — Configuration X vs Y; k-selection |
| 7 | Open questions within Ch 8's scope |
| 8 | Recommendations for the Ch 8 refactor |

---

## 1. The Ch 8 question

Current Ch 8 (in outline form) frames its central derivation as: *given fixed (σ, ε), what value of k minimizes the total energy of a k × T(m', 1) multi-link configuration?* It hopes k = 3 emerges, matching MaSt model-F's three-quark organization.

Two problems with this framing.

**First, the calculation hasn't been done.** [STATUS](STATUS.md) records this as TODO-M8(a).

**Second, when the calculation *is* attempted in pure linear theory, the answer is degenerate.** A k-link's total mass is k × mass(primitive), exactly equal to k separate primitives. There is no preferred k at the linearized level (§6 below).

What this scoping file does: work through what shear *does* derive at the linearized level (§§2–4: symmetry structure, m_opt = σε), what it *does not* derive (§6: k-selection), and what mechanism within metric-charge's scope could complete the picture (§6.5: φ⁴ inter-component coupling). The combined-parameter content — how σ and ε *together* produce different sheet characters — belongs in the new Ch 9 and is scoped in [work-ch9.md](work-ch9.md).

---

## 2. Setup — sheet with shear, Bloch-mode-as-particle under shear

### 2.1 Sheet metric and inverse

The (u, w) block of the sheet metric with shear active ([Ch 1 §4](01-foundation.md)):

<!-- g_uw block = ((1, σ),(σ, 1)) -->
$$
g^{(u,w)}_{ab} \;=\; \begin{pmatrix} 1 & \sigma_{uw} \\ \sigma_{uw} & 1 \end{pmatrix}
\qquad\det g^{(u,w)} = 1 - \sigma_{uw}^2
$$

We write σ ≡ σ_uw. Positive-definiteness requires |σ| < 1 within this (View A / metric-shear) parametrization. The parametrization choice itself — whether to keep metric-shear or adopt the lattice-shear View B — is a framework-wide decision scoped in [work-ch9.md §7](work-ch9.md).

The inverse:

<!-- g^(u,w) inv = (1/(1-σ²)) ((1,-σ),(-σ,1)) -->
$$
g^{ab}_{(u,w)} \;=\; \frac{1}{1-\sigma^2}\begin{pmatrix} 1 & -\sigma \\ -\sigma & 1 \end{pmatrix}
$$

### 2.2 Dispersion of a Bloch mode

For a Bloch mode φ ∝ exp(i(k_u u + k_w w − ωt)) with rectangular periodicity k_u = 2πm/L_u, k_w = 2πn/L_w:

<!-- (ω/c)² = k_S² + (k_u² - 2σ k_u k_w + k_w²)/(1 - σ²) -->
$$
\frac{\omega^2}{c^2} \;=\; k_S^2 + \frac{k_u^2 - 2\sigma\,k_u k_w + k_w^2}{1-\sigma^2}
$$

Rest mass-squared:

<!-- m²_(m,n) = M² · (1/(1-σ²)) · (m²/ε² - 2σmn/ε + n²) -->
$$
m_{(m,n)}^2 \;=\; \frac{M^2}{1-\sigma^2}\Bigl[\tfrac{m^2}{\varepsilon^2} - \tfrac{2\sigma\,m n}{\varepsilon} + n^2\Bigr]
$$

Define the dimensionless coefficient:

<!-- μ²(m, n; σ, ε) = m²/ε² - 2σmn/ε + n² -->
$$
\mu^2(m, n;\,\sigma,\varepsilon) \;\equiv\; \frac{m^2}{\varepsilon^2} - \frac{2\sigma\,m n}{\varepsilon} + n^2
$$

so m²_{(m,n)} = M²·μ²/(1−σ²). The (1−σ²)⁻¹ factor is a global rescaling; the σ-dependent structure of the spectrum lives in μ².

### 2.3 Bloch-mode-as-particle under shear

[Ch 5 §4](05-metric-self-consistency.md) defines the "natural particle" for a closure-satisfying mode as the R_u-symmetrized combination (m, n) + (−m, n) at equal amplitude — enforcing the wrap-order's ring-direction reflection R_u as a particle symmetry. At σ = 0, R_u is exact and the equal-amplitude combination is a stationary state.

**Under σ ≠ 0, R_u is broken.** The two Bloch modes (m, n) and (−m, n) acquire different masses:

<!-- μ²(m, n; σ, ε) - μ²(-m, n; σ, ε) = -4σmn/ε (R_u-conjugate split) -->
$$
\mu^2(m, n) - \mu^2(-m, n) \;=\; -\tfrac{4\sigma\,m n}{\varepsilon}
$$

The equal-amplitude combination is no longer stationary; it oscillates between mass eigenstates. The σ = 0 natural-particle construction does not strictly transfer.

Three options for what "the particle" means at σ ≠ 0:

(a) **Single-Bloch-mode interpretation.** The particle is the single Bloch mode at (m, n), with mass μ² from §2.2. The wrap-order selects which chirality sector — the sign of m that gives the lower-mass mode for sign(σ) and the (m, n) sector.

(b) **R_u-symmetrized as small-σ perturbation.** Approximate at small σ; chirality eigenstates and mass eigenstates rotate with σ.

(c) **Sheared natural particle.** Redefine as the lowest-energy state with appropriate wrap-order properties. Reduces to (a) since both R_u and R_w are broken.

**This file commits to interpretation (a).** Consequence: [Ch 5 §4.6](05-metric-self-consistency.md)'s four-property gauge-potential test (derived for the σ = 0 R_u-symmetrized particle) must be redone for the single Bloch mode at σ ≠ 0. This extends TODO-M2. The structural conclusions of §§4–6 below use μ²(m, n; σ, ε) directly, valid under interpretation (a).

### 2.4 The σ-spectrum on the integer lattice

μ²(m, n; σ, ε) is a quadratic form on integer (m, n):

<!-- μ² = (m, n) · Q · (m, n)^T -->
$$
\mu^2 \;=\; \begin{pmatrix} m & n \end{pmatrix} Q \begin{pmatrix} m \\ n \end{pmatrix},
\qquad Q \;=\; \begin{pmatrix} 1/\varepsilon^2 & -\sigma/\varepsilon \\ -\sigma/\varepsilon & 1 \end{pmatrix}
$$

Eigenvalues:

<!-- λ_± = (1/2)[(1 + 1/ε²) ± √((1 - 1/ε²)² + 4σ²/ε²)] -->
$$
\lambda_\pm \;=\; \tfrac{1}{2}\Bigl[(1 + \tfrac{1}{\varepsilon^2}) \pm \sqrt{(1 - \tfrac{1}{\varepsilon^2})^2 + \tfrac{4\sigma^2}{\varepsilon^2}}\Bigr]
$$

with λ_+ + λ_− = 1 + 1/ε² and λ_+λ_− = (1−σ²)/ε². Integer modes pick out points closer to one principal axis or the other; the analysis of which principal axis dominates at extreme parameters is taken up in [work-ch9.md §4](work-ch9.md).

---

## 3. Symmetries of the sheared spectrum

The cross-term −2σmn/ε is bilinear in (m, n). This controls all the symmetry structure.

### 3.1 The three sign-flip operations

| Operation | Action | Effect on μ² |
|---|---|---|
| **R_J** (joint reversal) | (m, n) → (−m, −n) | mn unchanged → **μ² unchanged** |
| **R_u** (ring chirality) | (m, n) → (−m, n) | mn → −mn → cross-term flips sign |
| **R_w** (tube chirality) | (m, n) → (m, −n) | mn → −mn → cross-term flips sign |

**σ_uw breaks both chirality reflections (R_u and R_w independently) and preserves only joint reversal R_J.** The R_u-broken split between (m, n) and (−m, n) is structurally identical in size (4σmn/ε in μ²) to the R_w-broken split between (m, n) and (m, −n). But they are *different physical pairs* and play *different roles*.

### 3.2 Two distinct chirality-conjugate pairs

| Pair | Δμ² under shear | Role |
|---|---|---|
| (m, n) ↔ (−m, n) — **R_u-conjugate** | 4σmn/ε | Ring-chirality split; these were the natural particle's two components at σ = 0 |
| (m, n) ↔ (m, −n) — **R_w-conjugate** | 4σmn/ε | Tube-chirality split; the chirality-bias variable of [Ch 6 §6](06-handedness-and-pairs.md) |
| (m, n) ↔ (−m, −n) — **R_J-conjugate** | 0 | Sign-conjugate pair; mass-degenerate |

The prior version of [Ch 6 §6](06-handedness-and-pairs.md) (and the first pass of this file) conflated R_u and R_w splits. They are physically distinct: R_u is the natural-particle's symmetrization axis; R_w is the framework's chirality-bias variable.

### 3.3 Implications for the natural particle

Under interpretation (a) of §2.3, the natural particle at "the (m, n) sector" is one of the two R_u-conjugate Bloch modes — by the wrap-order, the sign of m that gives the lower mass under σ ≠ 0. For mn > 0 with σ > 0: μ²(m, n) < μ²(−m, n), so positive-mn is the picked sector. Flipping σ flips the pick. This is the structural locus of intra-particle chirality bias.

The sign-conjugate pair (m, n) ↔ (−m, −n) remains mass-degenerate under shear (R_J preserved). [Ch 6 §4](06-handedness-and-pairs.md) sign-conjugate cancellation operates the same at σ ≠ 0 as at σ = 0.

---

## 4. The σε product — structural lever for closure-satisfying primitives

### 4.1 The optimum ring-winding

For a closure-satisfying T(m, 1) primitive:

<!-- μ²(m, 1; σ, ε) = m²/ε² - 2σm/ε + 1 -->
$$
\mu^2(m, 1) \;=\; \tfrac{m^2}{\varepsilon^2} - \tfrac{2\sigma m}{\varepsilon} + 1
$$

Complete the square in m:

<!-- μ²(m, 1) = (m/ε - σ)² + (1 - σ²) -->
$$
\mu^2(m, 1) \;=\; \Bigl(\tfrac{m}{\varepsilon} - \sigma\Bigr)^{\!2} + (1 - \sigma^2)
$$

Parabola in m with minimum at **m_opt = σε**, where μ²_min = 1 − σ². Restoring the (1−σ²)⁻¹ factor:

<!-- m²_(m_opt, 1) = M² · (1 - σ²)/(1 - σ²) = M² -->
$$
m^2_\text{phys}(m_\text{opt}, 1) \;=\; M^2 \cdot \frac{1 - \sigma^2}{1 - \sigma^2} \;=\; M^2
$$

**The minimum mass of the lightest T(m, 1) primitive is exactly M, independent of σ — for any (σ, ε) such that σε is integer.** The σ-dependence cancels between μ²_min = 1 − σ² and the global (1−σ²)⁻¹ rescaling. The lightest closure-satisfying primitive sits at exactly the natural mass scale M = (ℏ/c)·(2π/L_w); its identity (which integer m) shifts with σε, but its mass doesn't.

This cancellation is specific to the metric-shear (View A) parametrization. Whether the result survives in the lattice-shear (View B) reformulation is examined in [work-ch9.md §7](work-ch9.md).

### 4.2 Quantization residual

m must be a positive integer; σε generally is not. Let m̂ = round(σε). The actual minimum:

<!-- m²_phys = M²·[1 + Δ²/(1-σ²)],  Δ ≤ 1/(2ε) -->
$$
m^2_\text{phys} \;=\; M^2\cdot\Bigl[1 + \tfrac{\Delta^2}{1-\sigma^2}\Bigr],\qquad \Delta \;\equiv\; \tfrac{\hat m}{\varepsilon} - \sigma,\;\; |\Delta| \le \tfrac{1}{2\varepsilon}
$$

For ε ≫ 1: residual tiny, lightest closure-satisfying ≈ M for any σ. For ε ≲ 1: residual is order unity; mass sits noticeably above M except at special σε values.

### 4.3 Level crossings

Two adjacent T(m, 1) primitives are degenerate at σε = m + 1/2:

<!-- σε = m + 1/2 for crossing between T(m, 1) and T(m+1, 1) -->
$$
\sigma\varepsilon = m + \tfrac{1}{2}
$$

So T(1, 1) is lightest for σε < 1.5, T(2, 1) for 1.5 < σε < 2.5, and so on. At the crossing, both primitives sit at μ² = 1/(4ε²) + (1−σ²), slightly above the M-mass minimum.

### 4.4 No three-fold degeneracy

For T(m−1, 1), T(m, 1), T(m+1, 1) all degenerate, the pairwise crossings would have to coincide: σε = m − 1/2 *and* σε = m + 1/2. Impossible.

**No three closure-satisfying T(m, 1) primitives are simultaneously degenerate at any (σ, ε).** Near-three-fold degeneracy (residual ~ 1/ε² split among three primitives) is an ε ≫ 1 phenomenon, not a special σε value.

### 4.5 Summary of σε

The σε product is the structural lever for closure-satisfying primitive selection. It:

- Selects m_opt = round(σε).
- Sets the residual (m̂/ε − σ)² controlling how close the lightest T(m, 1) is to M.
- Generates level crossings at half-integer σε.
- For large ε, gives near-degeneracy among many adjacent T(m, 1) primitives.

What σε does *not* do: select a preferred multi-link k (§6).

---

## 5. Single-axis vs closure-satisfying under shear

### 5.1 Single-axis modes are σ-cross-term-invariant

For (m, 0): μ² = m²/ε². For (0, n): μ² = n². Both have no σ in μ²; σ enters only through the global (1−σ²)⁻¹ factor:

<!-- m²_phys(m, 0) = M² · m²/(ε²(1-σ²))  ;  m²_phys(0, n) = M² · n²/(1-σ²) -->
$$
m^2_\text{phys}(m, 0) = \frac{M^2 m^2}{\varepsilon^2(1-\sigma^2)},\qquad
m^2_\text{phys}(0, n) = \frac{M^2 n^2}{1-\sigma^2}
$$

Shear scales single-axis masses up uniformly as σ → 1 but doesn't change relative ordering among single-axis modes.

### 5.2 Comparison with the lightest closure-satisfying primitive

| Mode | μ² |
|---|---|
| (1, 0) | 1/ε² |
| (0, 1) | 1 |
| T(m_opt, 1) | ≥ 1−σ² |

For ε < 1: T(m_opt, 1) is lighter than (0, 1) at any σ > 0 (since 1−σ² < 1).
For ε > 1: (1, 0) is lighter than T(m_opt, 1) unless σ > √(1 − 1/ε²) — i.e., σ close to 1 with ε close to 1.
For ε ≫ 1: (1, 0) is *much* lighter — the architectural single-axis-dominance puzzle (scoped in [work-ch9.md §3](work-ch9.md)).

What this section covers is **how shear scales the spectrum**. What it does *not* resolve is whether sheets at extreme ε are physically charged despite single-axis modes being lighter — that resolution requires the combined (σ, ε) analysis of the next chapter.

---

## 6. Multi-component links — Configuration X vs Y; k-selection

### 6.1 Two interpretations of "k × T(m', 1)"

The phrase admits two physically distinct readings under linear theory:

**Configuration X — single Bloch mode at (km', k).** Wavefunction has km'-fold ring structure and k-fold tube structure. Mass read directly off the dispersion at (km', k):

<!-- m²_X(km', k) = (M²/(1-σ²))·k²·μ²(m', 1; σ, ε) -->
$$
m^2_\text{X}(km', k) \;=\; \frac{M^2}{1-\sigma^2}\cdot k^2\,\mu^2(m', 1)
$$

so m_X = k · m(m', 1). Ch 5 §4 derivation gives *one* surviving cross-term h_μw.

**Configuration Y — k phased copies of T(m', 1).** Superposition:

<!-- ψ_Y = Σ_j A·exp(i(k_u u + k_w w + 2πj/k - ωt)) -->
$$
\psi_\text{Y} \;=\; \sum_{j=0}^{k-1} A\cdot e^{i(k_u u + k_w w + 2\pi j/k - \omega t)}
$$

Each component at the same wavevector and dispersion; total mass k·m(m', 1) by additivity. Each component sources its own h_μw → *k* surviving cross-terms.

[Ch 4 §4.3a](04-the-closure-condition.md) describes the multi-link as "k phased copies of a T(m', 1) primitive, with each component carrying 1/k of the link's total charge" — the **Configuration Y** interpretation.

### 6.2 The framework's commitment — Configuration Y

Under Y:
- Total mass: k · m(m', 1) — same as k separate primitives.
- Gauge structure: k surviving cross-terms (k-fold).
- Charge per component: 1/k of the link's integer total.
- Closure: link satisfies closure iff each component does.

This file commits Ch 8 to interpretation Y throughout. X is a different physical configuration the framework does not identify with multi-links.

### 6.3 Non-derivability of k_opt in linear theory

Under Y:
- 1 instance of k-link: total mass k·m(m', 1), gauge structure k-fold.
- k separate primitives: total mass k·m(m', 1), gauge structure k-fold.

**Linear theory does not distinguish these.** Any optimization over k is degenerate.

So the question "what k is optimum?" — asked of pure linearized scalar-field analysis — has the answer: **all k are degenerate; no preferred k emerges from energetic minimization.**

The current Ch 8 §6 framing ("k_opt from energy minimization") implicitly assumes some additional ingredient that distinguishes a k-link from k separate primitives. That ingredient is not in linear theory.

### 6.4 Phase-coherence under sheared metric — a negative finding

The most promising linear-theory candidate would be phase-coherence around the multi-link curve.

**Phase advance around T(m', 1) primitive.** Going once around: Δu = m'·L_u, Δw = L_w. Phase from Bloch mode at (k_u, k_w) = (2πm'/L_u, 2π/L_w):

<!-- Δφ = k_u · m' L_u + k_w · L_w = 2π(m'² + 1) -->
$$
\Delta\varphi \;=\; 2\pi(m'^2 + 1)
$$

This is 2π × integer regardless of σ. Phase coherence is automatic; no σ-dependence enters.

**Phase advance around k × T(m', 1) multi-link.** Per Configuration Y, each component traces its own primitive curve with the same phase advance 2π(m'² + 1). The relative phases {2π j/k} are imposed by the configuration, not derived from σ.

**Conclusion: pure linear scalar-field theory does not produce σ-dependent phase-coherence constraints that select specific k.** σ enters the energy via the cross-term in dispersion, but not the phase coherence of going around integer-winding closed curves. This is a sharp negative finding — phase-coherence is *not* the linear-theory mechanism for k-selection.

### 6.5 Internal-mode dynamics — the linear-adjacent mechanism

What is *almost* linear-theory but actually does give k-selection: **internal-mode dynamics of the multi-link with shear-induced inter-component coupling.**

A multi-link with k components has internal degrees of freedom — relative phases (and amplitudes) of the components. In pure linear theory these are free parameters; adding a quadratic-in-amplitude inter-component coupling (the smallest departure from pure linear theory) introduces dynamics:

<!-- L_coupling = -λ · Σ_{j ≠ j'} φ_j² φ_{j'}² -->
$$
\mathcal{L}_\text{coupling} \;=\; -\lambda \sum_{j \ne j'} \varphi_j^2\,\varphi_{j'}^2
$$

Under shear, this coupling acquires σ-dependent modulation through the cross-term in each component's kinetic energy. Internal modes (relative-phase oscillations between components) form a k-dimensional system with a σ-dependent coupling matrix. Stability and energy ordering depend on k. For specific (σ, ε), specific k may have the lowest-energy stable internal-mode configuration.

This is **not pure linear-theory** — it requires the φ⁴ self-coupling outside [Ch 5 §4](05-metric-self-consistency.md)'s linearized scope. But it is the *linear-adjacent* mechanism that comes closest to derivable within metric-charge's existing apparatus, and it is the most concrete candidate for a k = 3 derivation.

**The candidate calculation** — write the φ⁴ self-interaction energy of a k-component link on a sheared sheet, minimize over k, report which k wins at the hadronic sheet's (σ, ε) — is the natural follow-on to TODO-M8(a) at this stage. It is the work the framework most plausibly *can* do to settle k-selection without forwarding to grid-duality or metric-binding.

If k = 3 emerges, the framework has derived the structure. If not, the framework forwards k-selection to grid-duality (substrate Z_k) or metric-binding (multi-knot energetics).

### 6.6 Other candidate mechanisms (ordered by closeness to framework's apparatus)

- **(a) Internal-mode dynamics with σ-induced coupling (§6.5).** Most promising within metric-charge's scope.
- **(b) Substrate Z_k from grid-duality.** Z_k constraint at L3 forces specific k. Forwards to [grid-duality](../grid-duality/).
- **(c) Confinement-like binding.** k components bound by interaction. Forwards to metric-binding.
- **(d) Pauli-like exclusion.** Requires spin/statistics commitment not yet made.
- **(e) Topological commensurability under shear.** Basis-rephrasing in lattice-shear (View B); scoped in [work-ch9.md §7](work-ch9.md).

### 6.7 Honest finding

Linear scalar-field theory on a sheared 2D-compact substrate gives no preferred k. The σε product selects m_opt for primitives; it does not select k for multi-links.

If the framework commits to "metric-charge should derive k from shear (and ratio) together," the chapter must pursue mechanism (a) and carry out the φ⁴ calculation explicitly, or commit to (e) and reformulate in lattice-shear basis.

If the framework commits to "metric-charge sets up the inventory; substrate selects k," forwarding (b) to grid-duality is the principled stance — the chapter documents the linear-theory degeneracy and passes k-selection downstream.

The choice is a project-direction call. Either way, this scoping makes the linear-theory finding clear.

---

## 7. Open questions within Ch 8's scope

### 7.1 Natural particle under shear

Interpretation (a) of §2.3 (single Bloch mode is the particle) needs the [Ch 5 §4.6](05-metric-self-consistency.md) four-property gauge-potential test redone at σ ≠ 0. The surviving cross-term pattern (T_tu, T_tw, T_uw) under the single-Bloch-mode construction differs from the σ = 0 R_u-symmetrized version. **This extends TODO-M2.**

### 7.2 Multi-link interpretation choice

§6.1's Configuration X vs Configuration Y distinction needs to be made explicit in [Ch 4 §4.3](04-the-closure-condition.md) and [Ch 5 §4](05-metric-self-consistency.md). The framework has been tacitly using Y but has not committed. Ch 8 should commit and propagate.

### 7.3 The φ⁴ inter-component calculation

§6.5's calculation is the load-bearing piece for the "shear (with ratio) derives k = 3 at the hadronic regime" claim. It is the most consequential single piece of work the chapter could carry out before publication.

### 7.4 Chirality bias and parity violation

σ_uw provides intra-particle chirality bias ([Ch 6 §6](06-handedness-and-pairs.md), [Ch 8 §3](08-shear-and-fractional-charge.md)) — a P-flavor ingredient. The C-flavor side (matter-antimatter bias) is not provided by σ_uw. Forwarded outside metric-charge per [STATUS](STATUS.md).

### 7.5 Neutrino oscillation period

The R_w-conjugate near-degeneracy at σ → 0 provides an oscillation mechanism with period ∝ 1/Δm ∝ 1/(σ·K_u K_w / mass-scale). The explicit time-evolution calculation — chirality-eigenstate prepared as (cos θ)·(m,n) + (sin θ)·(m,−n), evolved under the sheared dispersion, with the oscillation period identified — has not been done. Straightforward at the linearized level; worth carrying out.

---

## 8. Recommendations for the Ch 8 refactor

### 8.1 Reframe the central derivation honestly

Replace current §6's "k_opt from energy minimization" framing with:

- **Linear theory:** no preferred k (§6.3, §6.4). σε selects m_opt for primitives but doesn't select k for multi-links.
- **Linear-adjacent (φ⁴ inter-component coupling):** the candidate calculation that *can* select k. Carry it out at the hadronic sheet's (σ, ε); report the result.
- **If yields specific k:** framework derives the multi-link structure.
- **If yields no preference or wrong k:** forward k-selection to grid-duality / metric-binding.

### 8.2 Add the σε analysis prominently

§4 of this file is the cleanest derivable result and belongs in Ch 8 as a substantive new section. The "lightest T(m, 1) primitive at mass exactly M" result is novel.

### 8.3 Resolve the natural particle definition under shear

Commit to interpretation (a) of §2.3. Update Ch 5 §4 to extend the gauge-potential analysis to σ ≠ 0 single-Bloch-mode particles. Update TODO-M2 in [STATUS](STATUS.md).

### 8.4 Resolve the multi-link interpretation

Commit to Configuration Y. Update [Ch 4 §4.3](04-the-closure-condition.md) to make this explicit. Update [Ch 5 §4](05-metric-self-consistency.md) gauge-potential analysis to handle k-component configurations cleanly.

### 8.5 Forwardings

Forward (with cross-references):

- Combined (σ, ε) landscape, three-sheet correspondence, σ → 1 principal-axis suppression, parametrization choice — to the new Ch 9 (scoped in [work-ch9.md](work-ch9.md)).
- Matter/antimatter (C-flavor) bias — outside metric-charge.
- Multi-knot energetics — to metric-binding.
- Substrate Z_k input — to grid-duality.

Do *not* forward without first attempting: the φ⁴ inter-component calculation (§6.5) and the natural-particle gauge-potential test extension (§7.1).
