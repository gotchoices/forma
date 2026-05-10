# work-m8a.md — Preliminary exploration: shear's effect on a 2D particle sheet

This file is a working document, not a chapter. It carries out the kind of derivation [Chapter 8](08-shear-and-fractional-charge.md) should employ when [TODO-M8(a)](STATUS.md) is properly addressed: an open-minded analysis of how the shear σ_uw structurally affects a 2D-compact particle sheet, what it predicts at the linearized level, what it does *not* predict, and how shear and aspect ratio ε interact.

The exploration is intentionally not committed to "k_opt = 3 from optimization." It works through the math, reports what falls out, and flags where current Chapter 8's framing turns out to be unsupported by linear theory alone.

The primary goal: understand shear in a way that helps make sense of *all three* particle-sheet types the framework needs to accommodate (the qualitative shapes of the lepton-like, neutrino-like, and hadronic-like sheets), not just the proton/quark question. A secondary goal: assess whether Ch 8 should be reorganized — possibly merged with Ch 7 or supplemented by a new "ratio + shear together" chapter — once the linear analysis is honest.

Conventions follow the rest of the project ([Ch 1](01-foundation.md): u = ring, w = tube; ε ≡ L_u/L_w; closure rule n | m on (m, n) integer labels). Throughout, M ≡ (ℏ/c)·(2π/L_w) denotes the natural mass scale; μ²(m, n; σ, ε) is the dimensionless mass-squared coefficient before the (1−σ²) overall factor and the M² scaling.

---

## Sections

| § | Topic |
|---|-------|
| 1 | The question being asked |
| 2 | Setup — sheet with shear, dispersion, natural particle |
| 3 | Symmetries of the sheared spectrum |
| 4 | The σε product — structural lever for closure-satisfying primitives |
| 5 | Single-axis vs closure-satisfying competition under shear |
| 6 | Multi-component links — what does linear theory actually predict? |
| 7 | The combined (σ, ε) landscape — three structural regimes |
| 8 | What the three sheet types look like in this landscape |
| 9 | Architectural questions exposed by this analysis |
| 10 | Recommendations for Ch 8 (and possible new chapter) |

---

## 1. The question being asked

Current Ch 8 (in outline form) frames the central derivation as: *given fixed (σ, ε), what value of k minimizes the total energy of a k × T(m', 1) multi-link configuration?* It hopes the answer is k = 3, matching the structural pattern that MaSt model-F associates with quark organization.

Two problems with this framing as it stands.

**First, the calculation hasn't been done.** [STATUS](STATUS.md) records this honestly as TODO-M8(a). Until carried out, the "k_opt from optimization" claim is asserted rather than derived.

**Second, when the calculation *is* attempted in pure linear theory, the answer is degenerate.** Linear theory treats each (m, n) mode as an independent excitation with mass set by the dispersion. A k-link T(km', k) has mass k × mass(T(m', 1)) — exactly the same total energy as k separate T(m', 1) primitives. There is no preferred k at the linearized level. (§6 below works through this carefully.)

So a real derivation — open-mindedly carried out — has to acknowledge that:

- Linear theory gives a clean answer about *which T(m, 1) primitive is lightest* under shear (§4 below: m_opt depends on the σε product).
- Linear theory gives a clean answer about *what shear does to the spectrum's symmetry structure* (§3: σ_uw breaks chirality reflections, preserves joint reversal).
- Linear theory does *not* give a preferred k for multi-link organization — that selection requires structural input from outside linear scalar-field analysis (substrate, nonlinearity, exclusion-like constraints).

What this exploration does: work through all of the above honestly, and use the cleanly-derivable parts to reason about how the (σ, ε) landscape maps onto the qualitative shapes of the three sheet types. The open-mindedness is principled — the framework's value depends on identifying what it actually predicts vs what it merely structurally allows.

---

## 2. Setup — sheet with shear, dispersion, natural particle

### 2.1 Sheet metric and inverse

The (u, w) block of the sheet metric with shear active ([Ch 1 §4](01-foundation.md), [Ch 8 §1](08-shear-and-fractional-charge.md)):

<!-- g_uw block = ((1, σ),(σ, 1)) -->
$$
g^{(u,w)}_{ab} \;=\; \begin{pmatrix} 1 & \sigma_{uw} \\ \sigma_{uw} & 1 \end{pmatrix}
\qquad\det g^{(u,w)} = 1 - \sigma_{uw}^2
$$

For brevity we write σ ≡ σ_uw throughout this file. Positive-definiteness requires |σ| < 1; we treat this as a binding metric-side constraint (whether it is a *physical* constraint on real sheets is a separate question — see §9.3).

The inverse is

<!-- g^(u,w) inv = (1/(1-σ²)) ((1,-σ),(-σ,1)) -->
$$
g^{ab}_{(u,w)} \;=\; \frac{1}{1-\sigma^2}\begin{pmatrix} 1 & -\sigma \\ -\sigma & 1 \end{pmatrix}
$$

### 2.2 Dispersion of a separable mode

For a separable mode φ ∝ exp(i(k_u u + k_w w − ωt)) with rectangular periodicity k_u = 2πm/L_u, k_w = 2πn/L_w, the wave equation gives

<!-- (ω/c)² = k_S² + (k_u² - 2σ k_u k_w + k_w²)/(1 - σ²) -->
$$
\frac{\omega^2}{c^2} \;=\; k_S^2 + \frac{k_u^2 - 2\sigma\,k_u k_w + k_w^2}{1-\sigma^2}
$$

The rest mass-squared (k_S = 0):

<!-- m²_(m,n) = M² · (1/(1-σ²)) · (m²/ε² - 2σmn/ε + n²) -->
$$
m_{(m,n)}^2 \;=\; \frac{M^2}{1-\sigma^2}\Bigl[\tfrac{m^2}{\varepsilon^2} - \tfrac{2\sigma\,m n}{\varepsilon} + n^2\Bigr]
$$

with M ≡ (ℏ/c)·(2π/L_w). Define the **dimensionless mass-squared coefficient**:

<!-- μ²(m, n; σ, ε) = m²/ε² - 2σmn/ε + n² -->
$$
\mu^2(m, n;\,\sigma,\varepsilon) \;\equiv\; \frac{m^2}{\varepsilon^2} - \frac{2\sigma\,m n}{\varepsilon} + n^2
$$

so that m²_{(m,n)} = M² · μ²/(1−σ²). The (1−σ²) factor is a global rescaling that affects every (m, n) the same way; the σ-dependent *structure* of the spectrum lives in μ².

### 2.3 The natural particle under shear

Per [Ch 5 §4](05-metric-self-consistency.md), the natural particle for a closure-satisfying mode is the R_u-symmetrized standing-wave construction:

<!-- φ_natural = 2A · cos(k_u u) · cos(k_w w - ωt) -->
$$
\varphi_\text{natural} \;=\; 2A \cdot \cos(k_u u) \cdot \cos(k_w w - \omega t)
$$

— standing in the ring direction u, traveling in the tube direction w. Under bare metric (σ = 0), the rest mass-squared is m² c² = (ℏ k_u)² + (ℏ k_w)². Under sheared metric, the rest mass-squared picks up the cross-term:

<!-- m²_natural c² = (M²ℏ²/(1-σ²)) · μ²(m, n; σ, ε) -->
$$
m_\text{natural}^2 c^2 \;=\; \frac{M^2 \hbar^2}{1-\sigma^2}\,\mu^2(m, n;\,\sigma, \varepsilon)
$$

The natural-particle construction does not change the form of the rest-mass coefficient — it determines which off-diagonal cross-terms survive in the sourced metric (Ch 5 §4.4) but the rest mass is set by the sum of squared compact-direction wavenumbers under the sheared inverse metric. So the dispersion of §2.2 is what the natural particle inherits.

### 2.4 The σ-spectrum on the integer lattice

For each (m, n) ∈ ℤ², μ²(m, n; σ, ε) is a quadratic form. We can write it as

<!-- μ² = (m, n) · Q · (m, n)^T -->
$$
\mu^2 \;=\; \begin{pmatrix} m & n \end{pmatrix} \cdot Q(\sigma, \varepsilon) \cdot \begin{pmatrix} m \\ n \end{pmatrix},
\qquad Q \;=\; \begin{pmatrix} 1/\varepsilon^2 & -\sigma/\varepsilon \\ -\sigma/\varepsilon & 1 \end{pmatrix}
$$

Eigenvalues of Q are

<!-- λ_± = (1/2)[(1 + 1/ε²) ± √((1 - 1/ε²)² + 4σ²/ε²)] -->
$$
\lambda_\pm \;=\; \tfrac{1}{2}\Bigl[(1 + \tfrac{1}{\varepsilon^2}) \pm \sqrt{(1 - \tfrac{1}{\varepsilon^2})^2 + \tfrac{4\sigma^2}{\varepsilon^2}}\Bigr]
$$

Trace and determinant identities (useful below):

<!-- λ_+ + λ_- = 1 + 1/ε²;  λ_+ λ_- = (1 - σ²)/ε² -->
$$
\lambda_+ + \lambda_- = 1 + \tfrac{1}{\varepsilon^2},\qquad \lambda_+\,\lambda_- = \tfrac{1 - \sigma^2}{\varepsilon^2}
$$

These are the principal-axis eigenvalues of the dispersion quadratic form. Their physical significance: a continuous mode along the principal axis has dimensionless mass-squared per unit (m, n)-vector-norm-squared equal to λ_+ or λ_−; the actual integer modes pick out specific points on the lattice that are closer to one principal axis or the other.

---

## 3. Symmetries of the sheared spectrum

The cross-term −2σ mn/ε in μ² is *bilinear* in (m, n). This single algebraic fact controls all the symmetry structure under shear.

### 3.1 The three sign-flip operations

For (m, n) → (m', n') with sign flips:

| Operation | Action | Effect on μ² |
|---|---|---|
| **R_J** (joint reversal) | (m, n) → (−m, −n) | mn unchanged; m², n² unchanged → **μ² unchanged** |
| **R_u** (ring chirality) | (m, n) → (−m, n) | mn → −mn; m², n² unchanged → cross-term flips sign |
| **R_w** (tube chirality) | (m, n) → (m, −n) | mn → −mn; m², n² unchanged → cross-term flips sign |

So **σ_uw breaks both chirality reflections (R_u and R_w independently) and preserves only joint reversal R_J**. This matches what Ch 6 §6 and Ch 8 §3 already establish; we restate it here as the foundation for everything that follows.

Concretely, mode masses under shear:

| Mode | μ² |
|---|---|
| (m, n) | m²/ε² − 2σ mn/ε + n² |
| (−m, −n) | m²/ε² − 2σ mn/ε + n² (same; R_J-invariant) |
| (m, −n) | m²/ε² + 2σ mn/ε + n² (different; R_w broken) |
| (−m, n) | m²/ε² + 2σ mn/ε + n² (different; R_u broken — but same as (m, −n)) |

The two "sign-conjugate-pair" modes (m, n) and (−m, −n) are mass-degenerate; the two "chirality-conjugate-pair" modes (m, n) and (m, −n) are split. The shear-induced split is the chirality bias of [Ch 6 §6](06-handedness-and-pairs.md).

### 3.2 What R_J preservation implies for the natural particle

The natural-particle construction of [Ch 5 §4](05-metric-self-consistency.md) under wrap-order R_u-symmetrization combines (++) + (−+) — *not* (++) + (−−). So shear's preservation of R_J doesn't directly stabilize the natural particle; rather, it preserves the equivalence between (m, n) and (−m, −n) sectors.

The natural particle at (m, n) and the natural particle at (−m, −n) are the same particle (they would be combined as a sign-conjugate pair under the cancellation-pair construction of [Ch 6 §4](06-handedness-and-pairs.md)). Under shear, this remains true — the σ-cross-term doesn't lift the (m, n) ↔ (−m, −n) degeneracy.

The chirality-flipped natural particle (R_u acts internally to combine (++) + (−+)) sees shear at the level of *which (m, n) sector it lives in*. The (m, n) and (m, −n) sectors are now mass-distinct under shear; the natural particle in one sector is heavier/lighter than its chirality-conjugate. This is the intra-particle chirality bias.

---

## 4. The σε product — structural lever for closure-satisfying primitives

### 4.1 The optimum ring-winding

Take a closure-satisfying T(m, 1) primitive. Its dimensionless mass-squared:

<!-- μ²(m, 1; σ, ε) = m²/ε² - 2σm/ε + 1 -->
$$
\mu^2(m, 1;\,\sigma, \varepsilon) \;=\; \tfrac{m^2}{\varepsilon^2} - \tfrac{2\sigma m}{\varepsilon} + 1
$$

Complete the square in m:

<!-- μ²(m, 1) = (m/ε - σ)² + (1 - σ²) -->
$$
\mu^2(m, 1;\,\sigma, \varepsilon) \;=\; \Bigl(\tfrac{m}{\varepsilon} - \sigma\Bigr)^{\!2} + (1 - \sigma^2)
$$

This is a parabola in m with minimum at **m_opt = σε**, where μ²_min = 1 − σ². Restoring the (1−σ²) overall factor of §2.2:

<!-- m²_(m_opt, 1) = M² · (1 - σ²)/(1 - σ²) = M² -->
$$
m^2_\text{phys}\bigl(m_\text{opt}, 1\bigr) \;=\; M^2 \cdot \frac{1 - \sigma^2}{1 - \sigma^2} \;=\; M^2
$$

**The minimum mass of the lightest T(m, 1) primitive is exactly M, independent of σ.** The σ-dependence cancels between μ²_min = 1 − σ² and the global (1−σ²)⁻¹ rescaling.

This is striking. The lightest closure-satisfying primitive sits at exactly the natural mass scale M = (ℏ/c)·(2π/L_w) — *for any (σ, ε) such that σε is integer*. Its identity (which integer m ≥ 1 it is) shifts with σε, but its mass doesn't.

### 4.2 Quantization residual

m must be a positive integer, but σε generally is not. Let m̂ = round(σε) (the nearest positive integer to σε; if σε < 1, m̂ = 1). The actual minimum:

<!-- μ²_min^integer = (m̂/ε - σ)² + (1 - σ²) -->
$$
\mu^2_\text{min, integer} \;=\; \Bigl(\tfrac{\hat m}{\varepsilon} - \sigma\Bigr)^{\!2} + (1 - \sigma^2)
$$

The quantization residual (m̂/ε − σ)² is at most (1/(2ε))² = 1/(4ε²). So:

<!-- m²_phys = M²·[1 + Δ²/(1-σ²)],  Δ ≤ 1/(2ε) -->
$$
m^2_\text{phys} \;=\; M^2\cdot\Bigl[1 + \tfrac{\Delta^2}{1-\sigma^2}\Bigr],\qquad \Delta \;\equiv\; \tfrac{\hat m}{\varepsilon} - \sigma,\;\; |\Delta| \le \tfrac{1}{2\varepsilon}
$$

For ε ≫ 1, the residual is tiny — the quantization is fine compared to the parabola's curvature, and the lightest closure-satisfying primitive is essentially at mass M for any σ.

For ε ≲ 1, the residual is order-unity — quantization is coarse, and the lightest closure-satisfying primitive sits noticeably above M except at special σε values where m_opt happens to land near an integer.

### 4.3 Level crossings between adjacent T(m, 1) primitives

Two adjacent integer T(m, 1) primitives have equal mass when σε = m + 1/2:

<!-- μ²(m, 1) = μ²(m+1, 1) iff m + 1/2 = σε -->
$$
\mu^2(m, 1) = \mu^2(m+1, 1) \iff (m/\varepsilon - \sigma)^2 = ((m+1)/\varepsilon - \sigma)^2 \iff \sigma\varepsilon = m + \tfrac{1}{2}
$$

So the spectrum of lightest closure-satisfying primitives undergoes successive level-crossings at σε = 1.5, 2.5, 3.5, …, with T(1, 1) being lightest for σε < 1.5, T(2, 1) lightest for 1.5 < σε < 2.5, and so on.

At the crossing σε = m + 1/2, both T(m, 1) and T(m+1, 1) have

<!-- μ²(m, 1) = μ²(m+1, 1) = (1/(2ε))² + (1 - σ²) at σε = m + 1/2 -->
$$
\mu^2 \;=\; \tfrac{1}{4\varepsilon^2} + (1 - \sigma^2)
$$

so they sit slightly above the M-mass minimum (by the residual term). The "two-fold degeneracy" at level crossings is a real spectrum feature of the integer T(m, 1) family.

### 4.4 No three-fold degeneracy among adjacent primitives at any single σε

The natural follow-up question: is there any σε at which *three* closure-satisfying primitives are degenerate? This would matter for "three-phase" interpretations.

For T(m−1, 1), T(m, 1), T(m+1, 1) all degenerate, both pairwise crossings need to coincide:

- T(m−1, 1) = T(m, 1) at σε = m − 1/2.
- T(m, 1) = T(m+1, 1) at σε = m + 1/2.

These can never coincide (they differ by 1). So **no three closure-satisfying T(m, 1) primitives are simultaneously degenerate at any (σ, ε).**

A weaker question: at what σε do three primitives have *similar* masses? At σε = m + 1/2 (a 2-fold crossing), the third-closest primitive sits at residual (1.5/ε)² above the crossing pair — small for large ε, substantial for small ε.

A different weaker question: at what σε is the mass-spread of the three closest T(m, 1) primitives smallest? Since the function (m/ε − σ)² is parabolic, the symmetric configuration about σε = m_center gives equal residuals 1/ε² for both flanking primitives. So at σε = m_center (integer), three primitives have masses

- T(m_center, 1): μ² = 1 − σ².
- T(m_center ± 1, 1): μ² = 1/ε² + 1 − σ².

The split between center and flanks is 1/ε² · M² /(1−σ²). For ε = 2 this is M²/4 — substantial. For ε = 5 it's M²/25 — small. For ε ≪ 1 the flanks are much heavier than the center; for ε ≫ 1 they're nearly degenerate.

So *near-three-fold degeneracy* among adjacent T(m, 1) primitives is an ε ≫ 1 phenomenon, not a special σε.

This is one of the cleanest things linear theory says about the inventory under shear. It does *not* say "k = 3 is preferred"; it says "many T(m, 1) primitives sit at nearly the same mass when ε is large."

### 4.5 Summary of what σε does

The σε product is the structural lever for the closure-satisfying primitive inventory. Its effects:

- Selects which integer m maximizes μ² minimization (m_opt ≈ σε, rounded to integer ≥ 1).
- Sets the residual (m̂/ε − σ)² that controls how close the lightest T(m, 1) is to the M-mass minimum.
- Generates level-crossings at half-integer σε (within the closure-satisfying primitive tower).
- For large ε, gives near-degeneracy among many adjacent T(m, 1) primitives even at generic σε.

What σε does *not* do (linear theory):

- Select a preferred multi-link k (§6).
- Push closure-satisfying primitives lighter than single-axis modes (§5).
- Force a three-phase character on the sheet's inventory.

---

## 5. Single-axis vs closure-satisfying competition under shear

### 5.1 Single-axis modes are σ-cross-term-invariant

For (m, 0): μ² = m²/ε², no cross-term (mn = 0).
For (0, n): μ² = n², no cross-term.

Both are σ-independent in their μ². The only σ-dependence comes through the global (1−σ²)⁻¹ factor:

<!-- m²_phys(m, 0) = M² · m²/(ε²(1-σ²))  ;  m²_phys(0, n) = M² · n²/(1-σ²) -->
$$
m^2_\text{phys}(m, 0) = \frac{M^2}{1-\sigma^2}\cdot\frac{m^2}{\varepsilon^2},\qquad
m^2_\text{phys}(0, n) = \frac{M^2}{1-\sigma^2}\cdot n^2
$$

So shear scales single-axis masses up uniformly as σ → 1, but doesn't change the *relative* ordering of single-axis modes among themselves.

### 5.2 Comparing the lightest single-axis mode to the lightest closure-satisfying mode

The lightest single-axis modes are (1, 0) and (0, 1):

<!-- μ²(1, 0) = 1/ε²  ;  μ²(0, 1) = 1 -->
$$
\mu^2(1, 0) = \tfrac{1}{\varepsilon^2},\qquad \mu^2(0, 1) = 1
$$

The lightest closure-satisfying primitive at integer m_opt has μ²(m_opt, 1) ≥ 1 − σ² (with equality at integer σε).

Compare:

| Mode | μ² | m²_phys (× (1−σ²)/M²) |
|---|---|---|
| (1, 0) | 1/ε² | 1/ε² |
| (0, 1) | 1 | 1 |
| T(m_opt, 1) | ≥ 1−σ² | ≥ 1−σ² |

Whether the closure-satisfying T(m_opt, 1) is lighter than (0, 1) requires 1 − σ² < 1, which is always true for σ > 0. So **T(m_opt, 1) is lighter than (0, 1) at any σ > 0** (assuming σε is integer or close to it).

But T(m_opt, 1) vs (1, 0): need 1 − σ² < 1/ε², i.e., 1 − 1/ε² < σ², or σ > √(1 − 1/ε²). For ε > 1, this requires substantial σ (close to 1). For ε < 1, the inequality 1 − 1/ε² < 0 is automatic — T(m_opt, 1) is *always* lighter than (1, 0).

**Reorganizing into regime claims:**

| ε regime | Lightest single-axis | Lightest closure-satisfying | Which is lighter? |
|---|---|---|---|
| ε < 1 | (0, 1) at μ² = 1 | T(m_opt, 1) at μ² ≈ 1 − σ² | T(m_opt, 1) lighter for σ > 0 |
| ε > 1 | (1, 0) at μ² = 1/ε² | T(m_opt, 1) at μ² ≈ 1 − σ² | (1, 0) lighter unless σ > √(1 − 1/ε²) |
| ε ≫ 1 | (1, 0) at μ² ≈ 0 | T(m_opt, 1) at μ² ≈ 1 − σ² | (1, 0) much lighter |
| ε = 1 | (1, 0) = (0, 1) at μ² = 1 | T(m_opt, 1) at μ² ≈ 1 − σ² | T(m_opt, 1) lighter for σ > 0 |

### 5.3 The ε > 1 architectural question

For ε > 1, the (1, 0) single-axis mode is the unique lightest mode, with mass approaching 0 as ε → ∞. This is mass-only by the structural-degeneracy mechanism of [Ch 4 §1.1 / §6.2](04-the-closure-condition.md) — no chirality structure on the curve, so the natural particle reduces to metric-mass's standing wave on a single direction with no spacetime↔compact gauge potential.

The closure-satisfying T(m_opt, 1) sits at mass M (or slightly above), much heavier than (1, 0).

**Yet the framework wants charged sheets to be physically meaningful at large ε.** MaSt model-F's electron-sheet identification places the electron at very large ε; the framework must accommodate a charged-particle interpretation in this regime. But linear theory says single-axis modes are *much* lighter — the lowest-energy excitations on a large-ε sheet are mass-only, not charged.

This is an **architectural question that the current Ch 7 partially flags but doesn't resolve** ([Ch 7 §4.3](07-aspect-ratio-and-character.md) calls it a "structural discrepancy" between framework and model-F). It needs explicit engagement, with three plausible resolutions:

(a) **Single-axis modes are not "particles" in the sheet-physical sense** — they may be the sheet's "background" or "vacuum" structure rather than excitations corresponding to observed particles. Charged states are excitations *above* this background. Under this reading, "the electron sits at the sheet's *closure-satisfying tier* at mass M" is what the framework means by saying the electron is on a large-ε sheet, while the (1, 0) modes are part of the sheet's intrinsic structure rather than its particle inventory.

(b) **Some non-linear or substrate-level constraint projects out single-axis modes** — possibly from grid-duality's wrap-promotion ladder, where single-axis modes don't satisfy some L3 wrap constraint. The framework would predict their absence as physical particles even though linear theory allows them.

(c) **The framework's prediction differs from observation here** — and the discrepancy is real. Single-axis dominance at large ε is genuinely predicted; the model-F identification is wrong; the framework predicts something different about what large-ε sheets look like.

Resolving among (a), (b), (c) is outside this exploration's scope but is a substantive open architectural question. **Any clean Ch 8 (or Ch 7+8 unification) needs to commit to one of these or explicitly leave the question open.**

### 5.4 The ε < 1 case is similar by mirror

For ε < 1, the (0, 1) single-axis mode at μ² = 1 is comparable to T(m_opt, 1) at μ² ≈ 1 − σ² — the closure-satisfying primitive is slightly lighter for any σ > 0. So the ε < 1 regime has *closure-satisfying lightness* over (0, 1), which is what we'd want for a charge-friendly sheet.

But for ε very small (ε ≪ 1), the picture changes again. The closure-satisfying T(1, 1) (the only T(m, 1) with reasonable m_opt ≈ σε ≈ 0 → 1) sits at μ² ≈ 1/ε² + 1 − 2σ/ε, dominated by 1/ε² for small ε. Heavy.

The hadron-like sheet (ε ≪ 1, modest σ) has the T(1, 1) primitive at very high mass relative to (0, 1). So *charged-mode lightness* in the ε ≪ 1 regime requires either substantial σ (so σε product approaches 1), or admitting that the sheet's character is not "lightest mode is charged."

This is the same architectural question as §5.3 in mirror: at ε ≪ 1, single-axis dominates the low-energy spectrum unless something projects them out.

---

## 6. Multi-component links — what does linear theory actually predict?

### 6.1 Mass of a k × T(m', 1) multi-link

The k-component multi-link with primitive T(m', 1) has total winding (km', k). Its dispersion-derived mass (treated as a single (m, n) mode at (km', k)):

<!-- m²(km', k) = (M²/(1-σ²)) · ((km')²/ε² - 2σ(km')(k)/ε + k²) = k² · m²(m', 1) -->
$$
m^2(km', k) \;=\; k^2 \cdot m^2(m', 1)
$$

Mass scales linearly with k:

<!-- m_phys(km', k) = k · m_phys(m', 1) -->
$$
m_\text{phys}(km', k) \;=\; k \cdot m_\text{phys}(m', 1)
$$

This is the bare-dispersion result. It's exactly what we'd expect from the (m, n)-quadratic structure — the cross-term scales with km' · k, the diagonal terms with k², the whole expression is a perfect square in k.

### 6.2 The non-derivability of k_opt in linear theory

Now compare two configurations carrying the same total physical content:

- **Configuration A**: a single k × T(m', 1) link with total integer charge k (in some appropriate normalization), total mass k · m(m', 1).
- **Configuration B**: k separate T(m', 1) primitives, each with charge 1, total mass k · m(m', 1).

**Both configurations have identical total mass at the linearized level.** The total winding decomposes into k primitives in either case; the dispersion sees only the integer (m, n) it's evaluated at, and the energy of the k components in either case is the same.

Linear scalar-field theory does *not* distinguish:

- "1 instance of the k-link as a single connected curve" from
- "k disjoint instances of the primitive curve."

Both contribute the same total energy density and the same gauge-potential structure (k surviving h_μw cross-terms in either case, by the natural-particle construction of [Ch 5 §4](05-metric-self-consistency.md) applied per-component).

So the question "what k is optimum?" — asked of a pure linearized scalar-field analysis on a sheared 2D-compact substrate — has the answer: **all k are degenerate at the energy level. No preferred k emerges from energetic minimization.**

This is an honest finding. The current Ch 8 §6's framing — "compute E(k; σ, ε, m'), minimize over k, report what k_opt emerges" — implicitly assumes some additional ingredient that distinguishes A from B. That ingredient is *not in linear theory*.

### 6.3 What ingredients could select k

Five candidate mechanisms that would distinguish multi-link from k separate primitives:

**(a) Nonlinear self-interaction.** A φ⁴ (or higher-order) term in the field action introduces couplings between modes. Two primitives at (m', 1) interact differently than one (km', k)-link at fixed total amplitude. The interaction's specific form determines which is energetically favored. Outside linear theory; outside this project's scope.

**(b) Topological / substrate input.** Grid-duality's wrap-promotion ladder may impose a Z_k constraint that forces specific k for closure-satisfying multi-component configurations — analogous to the way a Z_3 confinement constraint in standard physics (color confinement) forces baryons to have 3 quarks. The framework might inherit such a constraint from its substrate. The candidate "Z_3 from grid-duality at L3" is mentioned in current Ch 8 §6 as a candidate; whether it actually does this is a grid-duality question.

**(c) Phase-coherence under sheared metric.** Going around the multi-link curve in a sheared geometry picks up holonomy phases that depend on σ. For the k components to phase-cohere into a topologically valid k-link, the σ-dependent holonomies must satisfy a Z_k commensurability condition. At specific (σ, ε) values, specific k may be selected by this commensurability. Worth a careful analysis but speculative without it.

**(d) Pauli-like exclusion.** If the framework's primitives are subject to an exclusion principle (the framework hasn't committed to spin/statistics), then k separate primitives cannot occupy the same (m, n) state — they must populate distinct states. The total energy of k distinct primitives Σ_{i=1}^k m(m_i, 1) generally exceeds k · m(m_opt, 1), making the k-link (which can occupy one state) energetically favored. The selection of k could then come from how many distinct (m, n) primitives are accessible. This requires a commitment on statistics that the framework hasn't made.

**(e) Confinement-like interaction not present at linear level.** A binding energy between components that scales with separation distance (analogous to QCD string tension) would energetically favor multi-link bound states over separated primitives. The strength of the binding could depend on k via some structural-symmetry argument. Outside linear scalar-field theory.

**Linear theory gives no preferred k.** This is the honest answer. Whether the framework predicts a specific k requires committing to additional structure: grid-duality input (b), spin/statistics (d), nonlinear interactions (a), or confinement (e). Or commensurability (c), if a careful derivation supports it.

### 6.4 What current Ch 8 should say (honestly)

The "k_opt = 3 from energy minimization" framing is not derivable in linear theory. Current Ch 8 §6 should be reorganized to:

- Acknowledge the linear-theory degeneracy (this section's finding).
- Identify the candidate mechanisms (a)–(e) above that *could* select k.
- Note which mechanism the framework would naturally lean on. Given the project's explicit substrate-foundation in [grid-duality](../grid-duality/) and the existing reference to "Z_3 from grid-duality at L3," (b) is the natural candidate.
- Forward the actual k-selection derivation to grid-duality's substrate-level analysis.
- Report what *can* be derived in linear theory: the σε-driven m_opt structure of §4 above, and the chirality-bias structure of [Ch 6 §6](06-handedness-and-pairs.md).

This honest reframing is more in line with the project's "discovery mode" stance ([README](README.md) rule 3) than the current "optimization will yield k = 3" formulation.

---

## 7. The combined (σ, ε) landscape — three structural regimes

§§4–5 examined σε and ε separately. The full picture is a 2D landscape in (σ, ε) with multiple structurally distinct regimes. We can map them by the qualitative behavior of the closure-satisfying inventory and the single-axis competition.

### 7.1 Defining axes of the landscape

Two natural-feeling combinations:

- **σε product** — controls m_opt for the lightest closure-satisfying primitive.
- **ε itself** — controls the relative weight of single-axis modes (m, 0) vs (0, n), and the spacing of T(m, 1) primitives in mass.

Plus σ appears in the global (1−σ²)⁻¹ scaling and in the chirality-bias splits between (m, n) and (m, −n).

The (σ, ε) plane has three or four useful axes for understanding regimes: σ (chirality bias amplitude), ε (axis asymmetry), σε (m_opt selector), and possibly σ/ε.

### 7.2 Three structural regimes

A coarse partition of the (σ, ε) plane:

**Regime I — small σ, ε ≈ 1 (near-symmetric, near-bare).**

- Closure-satisfying T(1, 1) at μ² ≈ 1 + 1 − 2σ ≈ 2 − 2σ.
- Single-axis (1, 0) and (0, 1) at μ² = 1 — both light, close in mass.
- Chirality bias (between (m, n) and (m, −n)) is small (proportional to σ).
- m_opt = round(σ·1) = 1 (since σ ≪ 1).
- Three primitive sectors (charged T(1, 1) and two single-axis) all have masses within order-unity ratios.

In this regime, sign-conjugate pairs (m, n) and (−m, −n) are mass-degenerate (always, by R_J). Chirality-conjugate pairs (m, n) and (m, −n) are *nearly* mass-degenerate (small σ). At σ → 0, chirality pairs are exactly degenerate.

A configuration prepared as a sum of (m, n) and (m, −n) at equal amplitudes has gauge potentials that don't simply add or cancel — they're at slightly different masses, so the pair is not a stationary state. Mass-eigenstates are the individual (m, n) and (m, −n) modes; the equal-amplitude sum is a *flavor-eigenstate-like* construction that oscillates between mass eigenstates with frequency proportional to the mass split.

This is the structural pattern of mass-eigenstate-vs-flavor-eigenstate distinction familiar from neutrino oscillation. Whether this structural pattern matches observed neutrino oscillation quantitatively is downstream; structurally, the regime supports an oscillating pair-organization picture.

**Regime II — small σ, ε ≪ 1 (thin sheet, near-bare).**

- Closure-satisfying T(1, 1) heavy: μ² ≈ 1/ε² + 1 ≈ 1/ε² (for ε ≪ 1).
- Single-axis (0, 1) light: μ² = 1.
- Single-axis (1, 0) very heavy: μ² = 1/ε² ≈ T(1, 1).
- m_opt ≈ 1.
- σε ≪ 1 → minimum mass of T(m_opt, 1) is much higher than (0, 1).

The single-axis (0, 1) modes are by far the lightest. The closure-satisfying tier is high-mass. The chirality-bias split is small (σ small).

This is a "single-axis-dominated" regime in [Ch 7](07-aspect-ratio-and-character.md)'s terminology: low-energy excitations are mass-only single-axis (0, n) modes, with charged states accessible only at higher energy. The architectural question of §5.3 applies: how is this regime relevant to a charged sheet's character?

**Regime III — moderate σ, very large ε (wide sheet, sheared).**

- Single-axis (1, 0) very light: μ² = 1/ε² ≈ 0.
- Single-axis (0, 1) at μ² = 1.
- Closure-satisfying T(m_opt, 1) at mass M (μ² ≈ 1 − σ²).
- m_opt = round(σε) — could be large if σ is moderate.
- Many T(m, 1) primitives near m_opt have similar masses (residual ~ 1/ε² is small).

In this regime, the single-axis (m, 0) modes dominate at lowest energy. The closure-satisfying tier sits at M with many near-degenerate T(m, 1) primitives. The chirality-bias split is substantial (σ moderate, large σε in cross-term).

If the "physical sheet" in this regime is interpreted as living at the closure-satisfying tier (architectural resolution (a) of §5.3), then a sheet here has many near-degenerate charged primitives at mass M, with a finely-resolved chirality structure (σ-induced splits).

### 7.3 The σ → 1 boundary

At σ → 1, the (1−σ²)⁻¹ factor diverges. But along the principal axis of the dispersion quadratic form, the eigenvalue λ_− also approaches zero, and the ratio λ_−/(1−σ²) → 1/(ε²+1) (computed from the eigenvalue identity λ_+ λ_− = (1−σ²)/ε² with λ_+ → 1 + 1/ε²).

The principal-axis direction at σ → 1 is the eigenvector (ε, 1) (normalized). For ε integer, this is exactly the closure-satisfying primitive T(ε, 1) — and its mass is exactly M at σ = 1, by §4.1's calculation.

So the σ → 1 limit has a clean structural interpretation: **the lightest closure-satisfying primitive aligns exactly with the dispersion's principal axis when σε equals an integer, and its mass is M**. Off-principal-axis modes have mass diverging as 1/(1−σ²) — they become very heavy near the boundary.

This is a kind of "selection" effect — at σ → 1, only the principal-axis closure-satisfying primitive remains at moderate mass; everything else (single-axis, off-axis closure-satisfying, multi-link) has its mass scaled up by the (1−σ²)⁻¹ factor without being on the principal axis to compensate.

If the framework interprets "physical sheet near σ = 1" as a regime where only the principal-axis closure-satisfying primitive is the dominant low-energy mode, then large-ε sheets approach this regime, and the architectural question of §5.3 may have a partial resolution: at extreme ε with σ approaching 1, single-axis modes become heavy (1−σ²)⁻¹ scaling, and the closure-satisfying primitive is the unique "cheap" mode.

This is speculative but worth flagging — it's a structural mechanism that the linear theory could itself provide for charge-friendly behavior at extreme ε under the right σ.

---

## 8. What the three sheet types look like in this landscape

The framework needs to accommodate three structurally distinct sheet types, each with its own qualitative character. Without committing to specific (ε, σ) values from external sources, we can describe what each *looks like* under the framework's own analysis.

### 8.1 Lepton-like sheet — "principal-axis-aligned charge"

A single isolable charged primitive at mass M, no fractional decomposition, well-defined chirality.

The framework's structural fit for this sheet is the σ → 1, ε large regime (Regime III). Under that regime:

- Single closure-satisfying primitive T(m_opt, 1) sits at mass M. m_opt = round(σε) — a specific large integer when ε is large and σ is moderate.
- Single-axis modes are scaled up to high mass by the (1−σ²)⁻¹ factor (σ → 1 limit) — possibly out of the relevant low-energy spectrum.
- Chirality-bias (σ-induced split between (m_opt, 1) and (m_opt, −1)) is substantial. The sheet has a definite chirality preference; the natural particle is a chirality-eigenstate.

What this picture says about the lepton-like sheet:

- **Why high ε?** Large ε is what allows σ to approach 1 with σε large — i.e., what allows the m_opt to be a specific large integer rather than just 1.
- **Why substantial σ?** Substantial σ does two things: (i) drives the chirality bias (parity violation); (ii) raises the (1−σ²)⁻¹ factor, scaling single-axis modes up and out of the relevant spectrum. Combined, σ provides both the chirality structure and the single-axis suppression that makes the sheet charge-dominated.
- **Why single-particle character?** At Regime III with the principal axis aligned with a specific T(m_opt, 1), the natural lowest-energy state is a single primitive, not a multi-link. Multi-link configurations exist but at higher mass (k × M).

A possible candidate identification of m_opt for the lepton-like sheet would emerge from σ and ε together. The framework here doesn't commit; it observes that "σε determines which integer T(m_opt, 1) is the lightest charged primitive."

### 8.2 Hadronic-like sheet — "near-3-fold-degenerate charge tower"

Multiple closure-satisfying primitives at similar masses, with a 3-component structure (under appropriate substrate input). The framework's three-quark organization candidate.

The structural fit: ε ≪ 1, σ moderate. Under this:

- Closure-satisfying T(1, 1) sits at μ² ≈ 1/ε² + 1 — heavy (because ε is small).
- Single-axis (0, 1) sits at μ² = 1 — also heavy in absolute terms but lighter than T(1, 1) by factor 1/(1 + 1/ε²) ≈ ε² for ε small.
- m_opt = round(σε) ≈ 0 → rounded to 1. T(1, 1) is the unique lightest closure-satisfying primitive — no level-crossings nearby in the σε landscape since σε ≪ 1.
- Adjacent T(m, 1) primitives (T(2, 1), T(3, 1)) are heavy: μ²(2, 1) ≈ 4/ε² + 1, μ²(3, 1) ≈ 9/ε² + 1. *Not* near-degenerate with T(1, 1).

So the linear-theory analysis at small ε, small σ does *not* provide a near-three-fold-degenerate charged primitive tower. The hadronic-like 3-quark structure does not emerge from linear theory in this regime.

What *could* yield three-fold structure for this sheet:

- Substrate Z_3 input (per §6.3(b)) — the multi-link selection k = 3 from grid-duality, applied to multi-link configurations of T(1, 1). Under this, the hadronic sheet hosts 3 × T(1, 1) = T(3, 3) configurations at mass 3M_(1,1) per link.
- Confinement-like binding (§6.3(e)) — three primitives bound by an interaction that's not in linear theory.
- Some other mechanism not derivable here.

What's clean from linear theory:

- The hadronic-like sheet has a single charged primitive T(1, 1) at mass m_(1,1) = M·√(1/ε² + 1 − 2σ/ε)/(√(1−σ²)) — a specific number per (σ, ε).
- Multi-link configurations of this primitive (k × T(1, 1)) all have mass k × m_(1,1) at the linearized level — no preferred k.
- Single-axis (0, 1) is at mass M/√(1−σ²) — lighter than T(1, 1) at small ε. The architectural question (§5.3) applies: why does this sheet host T(1, 1) configurations as its physical particles when (0, 1) is lighter?

The "3-quark structure" would have to come from substrate or non-linear input. *Linear ratio + linear shear together does not produce the 3-component organization*. This is a clear honest finding for the chapter to report.

### 8.3 Neutrino-like sheet — "near-degenerate chirality pairs"

Mass-without-charge behavior, with paired structure that produces oscillation/cancellation behavior.

The structural fit: σ very small, ε near 1 (Regime I). Under this:

- Closure-satisfying T(1, 1) at μ² ≈ 2 − 2σ ≈ 2 (since σ very small).
- Single-axis (1, 0) and (0, 1) both at μ² = 1.
- Chirality-bias split between T(1, 1) and T(1, −1) is very small (∝ σ).

Two structural mechanisms relevant to neutrino-like behavior:

**Mechanism α — chirality-pair mixing.** At σ very small, T(1, 1) and T(1, −1) are nearly mass-degenerate. The mass-eigenstates are the individual (m, n) and (m, −n) modes; the *chirality-eigenstates* (which are the natural particles under R_u-symmetrization) differ from the mass-eigenstates. A configuration prepared as a chirality-eigenstate oscillates between mass-eigenstates with period ∝ 1/Δm ∝ 1/σ. As σ → 0, the oscillation period diverges; as σ grows, oscillation accelerates. This is the structural pattern of neutrino oscillation.

**Mechanism β — sign-conjugate pair cancellation.** [Ch 6 §4](06-handedness-and-pairs.md) identifies that a sign-conjugate pair (m, n) + (−m, −n) at equal amplitudes (R_J-symmetrized) has gauge potentials canceling — yielding mass + chirality field but no observable EM. This mechanism operates *independently of σ*; it's available on any sheet. But on the neutrino-like sheet (small σ), the chirality field T_uw is small (proportional to σ) — so the cancellation pair is *more cleanly mass-only* than on a high-σ sheet. The neutrino-like sheet is structurally well-suited to host cancellation pairs as its dominant configurations.

Combined picture: neutrino-like sheet at small σ, ε ≈ 1 hosts:

- Sign-conjugate pairs of T(1, 1) configurations (mass-only by R_J cancellation, very small chirality field).
- Chirality-pair near-degeneracy between T(1, 1) and T(1, −1) (mass-eigenstate-vs-flavor-eigenstate organization, oscillation behavior).
- No single isolable charged particle (sign-conjugate pairs always come in two; they cancel observable EM).

This structural picture matches several qualitative properties of the neutrino sector: oscillation between flavor-like and mass-like eigenstates, near-mass-degeneracy of chirality partners, dominance of cancellation-pair-like neutral configurations.

The "tiny shear matters" question is now answered: small σ produces *small chirality bias* (so chirality-flipped partners are near-degenerate, enabling oscillation) and *small chirality field* (so sign-conjugate cancellation pairs are cleanly EM-neutral). Both structural roles for σ on this sheet are realized at small σ. *Substantial σ* would break the near-degeneracy and re-establish chirality-eigenstates as mass-eigenstates, eliminating oscillation behavior.

This is a clean structural prediction the linear theory makes.

### 8.4 What this picture says about the three sheets together

The three sheets occupy distinct regions of the (σ, ε) landscape, each producing qualitatively different behavior at the linearized level:

| Sheet type | Region | Dominant structural feature |
|---|---|---|
| Lepton-like | Large ε, σ moderate-to-large | Principal-axis-aligned T(m_opt, 1) at mass M; substantial chirality bias; single-particle character |
| Neutrino-like | ε ≈ 1, σ very small | Sign-conjugate cancellation pairs; near-degenerate chirality pairs; oscillation behavior |
| Hadronic-like | Small ε, σ moderate | T(1, 1) at high mass; substrate input needed for 3-component organization |

For the lepton-like sheet, **the combination of large ε and large σ together** provides charge-friendly behavior (via the principal-axis alignment near the σ → 1 boundary). Neither alone would suffice — large ε alone would put single-axis modes at low energy; large σ alone with small ε wouldn't give the m_opt structure.

For the neutrino-like sheet, **σ very small** is what enables the near-degenerate chirality pairs and the clean cancellation-pair structure. Larger σ would break this; the neutrino-like behavior is *structurally specific to the small-σ regime*.

For the hadronic-like sheet, the 3-component organization requires substrate input not in linear theory. **Ratio and shear together at small ε do not produce a three-quark structure** at the linearized level.

This is the framework's honest report, given the linear analysis as carried out here.

---

## 9. Architectural questions exposed by this analysis

### 9.1 Multi-link selection mechanism

What selects k for multi-link configurations? Linear theory says nothing; the candidates of §6.3 — substrate input, nonlinearity, exclusion, confinement, commensurability — are all outside linear-theory scope. The framework's claim to predict three-component organization for hadrons depends on resolving this. The natural forwarding target is grid-duality (substrate Z_k input) and metric-binding (multi-link energetics).

### 9.2 Single-axis dominance puzzle

At extreme ε (either ε ≪ 1 or ε ≫ 1), single-axis modes are much lighter than the closure-satisfying tier. Yet the framework wants charged sheets at extreme ε. The architectural question (§5.3) needs explicit engagement: what makes the single-axis modes irrelevant or absent? Possibilities (a)–(c) of §5.3 are open. Until resolved, the framework's claim to support charged sheets at extreme ε is conditional.

### 9.3 σ-bound and the parametrization choice

The framework's metric-shear σ_uw is bounded by |σ| < 1 (positive-definiteness of the sheet metric). If the empirical sheets need shear values that exceed this bound under one parametrization (lattice-shear vs metric-shear are non-equivalent under a coordinate change that scales lengths), the framework needs to commit to which parametrization is physical.

Two options:
- Metric-shear σ_uw with |σ| < 1 — current framework choice. Bounded shear; some empirical estimates of "shear" may not directly apply if their parametrization is different.
- Lattice-shear s with no bound — equivalent under coordinate change for σ < 1, but extends beyond. Used by some studies.

These are related by a coordinate change with |σ| < 1, but for |σ| ≥ 1 the metric becomes Lorentzian — physically pathological for a Riemannian sheet. Either the framework adopts the metric-shear bound and accepts that empirical "shear" estimates may be in a different parametrization, or it generalizes to admit lattice-shear without metric bound.

This needs explicit discussion in Ch 8 — currently it's elided.

### 9.4 Three-phase structure for hadronic sheets

The hadronic-like sheet's 3-quark structure is a genuine structural prediction the framework wants to make, but linear theory at small ε does not produce it. Three candidate sources:

- Substrate Z_3 from grid-duality.
- Non-linear / confinement-like binding among k = 3 primitives.
- A different structural location for "3 components" (e.g., the three near-degenerate chirality-projected components at small σ near ε = 1, forming a triplet under some flavor-like symmetry).

The framework's commitment to "k = 3 from optimization" should be reframed as "k = 3 from substrate / confinement / flavor-structure" — depending on which mechanism survives scrutiny.

### 9.5 Chirality bias and parity violation

σ_uw provides intra-particle chirality bias ([Ch 6 §6](06-handedness-and-pairs.md), [Ch 8 §3](08-shear-and-fractional-charge.md)) — a P-flavor ingredient toward Sakharov-style CP-violation-like structure. The C-flavor side (matter-antimatter bias) is *not* provided by σ_uw under the framework's wrap-order. This is forwarded outside metric-charge to substrate-level work.

### 9.6 Neutrino oscillation period

The chirality-pair near-degeneracy at σ → 0 provides an oscillation mechanism with period ∝ 1/Δm ∝ 1/(σ · K_u K_w / mass-scale). Whether the empirical neutrino oscillation periods match this structural prediction quantitatively is downstream MaSt-correspondence work; structurally, the prediction exists.

---

## 10. Recommendations for Ch 8 (and possible new chapter)

### 10.1 Reframe Ch 8's central derivation

Replace the current §6 framing ("k_opt from energy minimization") with the honest finding: **linear theory selects m_opt for the lightest T(m, 1) primitive (m_opt = round(σε) at fixed (σ, ε)), but does not select k_opt for multi-link organization**.

The §4 chirality-bias derivation can stay; it's clean linear-theory output. The §5 multi-link energetics discussion needs to be reframed around the ingredient question (§6.3 of this file): what would distinguish a k-link from k separate primitives? Linear theory doesn't; substrate or nonlinearity might.

The §6 "k = 3 emerges" expectation should be replaced with: "k = 3 (or any specific k) requires substrate input, forwarded to grid-duality."

### 10.2 Add §4-style m_opt-under-shear analysis

Sections 4 and 7 of this file are good candidate content for a new Ch 8 §4 or §5. The σε product as the structural lever for closure-satisfying primitive selection is a clean, novel, derivable result. It belongs in the chapter prominently.

### 10.3 Engage the architectural question (single-axis dominance)

§5.3 above identifies an architectural tension that current Ch 7 partially flags but doesn't resolve. Ch 8 should commit to one of the resolutions (a)–(c) or explicitly leave the question open with a clear restatement of what's at stake. Not committing leaves the framework's claim to support charged sheets at extreme ε in an underspecified state.

### 10.4 Consider unifying Ch 7 and Ch 8 — or adding a "ratio + shear together" chapter

The σε product, the regime structure of §7 above, the shear-driven mechanisms for the three sheet types in §8 above — all of these are *combined* effects of ratio and shear. Ch 7 alone (ratio) and Ch 8 alone (shear) miss them. Two restructuring options:

**Option A**: Merge Ch 7 and Ch 8 into a single Ch 7 "Ratio and shear together," structured around the combined (σ, ε) landscape and three-regime analysis. Pros: single coherent treatment of the parameter space. Cons: Ch 7's pure-ε analysis becomes harder to find; size becomes large.

**Option B**: Keep Ch 7 (ratio alone) and Ch 8 (shear alone) as setups, then add a new Ch 9 "The (σ, ε) landscape" or "Ratio and shear together" that brings them together. Pros: preserves the pedagogical "one parameter at a time" build. Cons: pushes the unified picture into a third chapter.

Recommendation: **Option B if the project's chapter-by-chapter pedagogy is important to preserve** (consistent with Ch 7 and Ch 8 being substantial in their own right). **Option A if the unified picture is structurally more important than the per-chapter pedagogy**. The user should decide; the math goes the same way either way.

### 10.5 Forwardings

The k-selection question (§9.1) forwards naturally to grid-duality (substrate Z_k input) and metric-binding (multi-link energetics). The matter-antimatter mechanism (§9.5) forwards similarly. The single-axis-dominance question (§9.2) is internal to the metric-charge/metric-mass framework — requires architectural commitment within this project's scope, not just forwarding.

### 10.6 Honest scope statement

Ch 8's "What this chapter does NOT do" list should add:

- Does not predict a specific multi-link k value from linear theory. The k-selection mechanism is forwarded to grid-duality (Z_k substrate) and/or metric-binding (multi-link energetics). The candidate k = 3 is structurally suggested (Z_3 in grid-duality at L3), not derived here.
- Does not resolve the single-axis-dominance question at extreme ε. Three candidate resolutions are noted (§5.3 of work-m8a.md); the chapter does not commit.
- Does not commit to a metric-shear vs lattice-shear parametrization choice for empirical correspondence. The σ_uw of the framework is metric-shear with |σ| < 1; empirical "shear" parameters may not directly correspond.

These are honest restrictions that strengthen rather than weaken the chapter.

---

## Notes on what remains open

This exploration is intentionally preliminary and not committal. Key remaining work before refactor:

- Carefully verify the §4 "m_opt minimum at mass exactly M" result — particularly the cancellation of (1−σ²) factors. This file argues it; the chapter would want the calculation written out cleanly with checks at edge cases (σ → 0, σ → 1, ε integer vs ε non-integer).
- Work through §6.3(c) (phase-coherence under sheared metric) with a real holonomy calculation to determine whether commensurability conditions actually select specific k. If they do, that would be a real linear-theory mechanism for k-selection that we shouldn't dismiss too quickly.
- Examine whether the §7.3 "principal-axis alignment at σ → 1" interpretation actually works to suppress single-axis modes in the sense §5.3(a) wants. The mass-scaling argument is suggestive but not rigorous.
- For the neutrino-like sheet (§8.3), compute the oscillation period from σ explicitly and check whether the small-σ near-degeneracy structurally matches observed neutrino-oscillation magnitudes — at the level of "right order of magnitude under reasonable parameters." If not, the structural picture needs revision.
- Decide whether the σ-bound (|σ| < 1) is binding for the framework, or whether nonlinear / lattice-shear extension is needed.

If these checks come out clean, the §10 recommendations can be carried out as a Ch 8 refactor. If some come out negatively (e.g., principal-axis suppression doesn't actually work), the architectural questions of §9 reopen and the framework needs more substantial rethinking before the chapter can be solid.
