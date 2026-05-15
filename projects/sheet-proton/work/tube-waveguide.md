# tube-waveguide.md — 3D wave-guide extension of the clover-torus picture

**Status:** Mathematical analysis of the simplest 3D-interior extension of the clover-torus picture, treating the tube as a 3D solid-torus wave guide with the clover-shaped 2D cross-section as the transverse boundary. Asks whether this extension produces the user's hoped-for hierarchy (whole-circumference < lobe-localized < saddle-localized) and whether the mass ratios reach observed quark inter-generation gaps.

**Companion to:** [clover-modes-analytical.md](clover-modes-analytical.md) (the 2D-surface analysis that established the hierarchy *cannot* emerge from the 2D Hill equation).

---

## 1. Setup — 3D solid torus with clover cross-section

The current metric-charge / clover-quarks / clover-mass framework treats the manifold as M = ℝ³ × T² with T² intrinsically 2-dimensional. There is no "interior" of the tube — the compact substrate *is* the 2-torus surface.

The user's proposed extension: M = ℝ³ × Ω where Ω is the 3D *solid torus* whose boundary is the clover-corrugated T². The compact part has:

- **1 longitudinal direction** (around the ring, θ ∈ [0, 2π) with twist identification)
- **2 transverse directions** (the 2D clover-shaped cross-section, with ∂Ω being the 1D clover profile)

This adds one effective compact dimension to the framework. The wave equation in the 3D interior is

<!-- (∂_t² − Δ_3D) ψ = 0 with Dirichlet ψ = 0 on ∂Ω -->
$$
(\partial_t^2 - \Delta_{3D})\,\psi \;=\; 0, \qquad \left.\psi\right|_{\partial\Omega} = 0
$$

(Dirichlet BCs taken for the simplest version; radiation/absorbing BCs are more physical given grid's "α-strength leakage" mechanism but produce finite-lifetime resonances instead of true bound states — same mass scale.)

For a thin tube R_major ≫ r_max, the cross-section problem decouples from the ring direction at leading order. The mode structure is

$$
\psi(\theta, x_\perp) \;=\; e^{i n_\theta \theta}\,\chi_\alpha(x_\perp)
$$

with χ_α(x_⊥) satisfying the 2D cross-section Helmholtz equation

<!-- -∇²_⊥ χ = λ_α χ on the clover-shaped disc, with χ = 0 on the boundary -->
$$
-\,\nabla^2_\perp\,\chi_\alpha \;=\; \lambda_\alpha\,\chi_\alpha, \qquad \chi_\alpha|_{\partial\Omega} = 0
$$

The mass formula in R_major = 1 units:

<!-- μ² = n_θ² + λ_α -->
$$
\mu^2 \;=\; n_\theta^2 \;+\; \lambda_\alpha
$$

The 2D-only analysis (clover-modes-analytical) corresponds to λ_α = 0 plus the 2D-surface Hill spectrum. The 3D extension adds the full cross-section eigenvalue spectrum λ_α.

(The torus curvature correction from R_major ~ r_max — relevant for the fat-tube regime where the proton sheet sits — modifies λ_α by O(r_max/R_major)² factors. Ignored in this leading-order analysis.)

---

## 2. Cross-section eigenvalue spectrum

For a 2D domain with Dirichlet BCs, the lowest eigenvalues are well-studied. For a *disc of radius a*:

$$
\lambda_{nm}^{\mathrm{disc}} \;=\; (z_{nm}/a)^2
$$

with z_nm the m-th positive zero of the Bessel function J_n. Low values:

| (n, m) | z_nm | (z_nm)² | Degeneracy |
|---|---|---|---|
| (0, 1) | 2.405 | 5.78 | 1 |
| (1, 1) | 3.832 | 14.68 | 2 |
| (2, 1) | 5.135 | 26.37 | 2 |
| (0, 2) | 5.520 | 30.47 | 1 |
| (3, 1) | 6.380 | 40.71 | 2 |
| (1, 2) | 7.016 | 49.22 | 2 |

The ratios (λ_α / λ_(0,1)): 1, 2.54, 4.56, 5.27, 7.04, 8.51. Bessel-zero ratios grow linearly with sqrt: z_nm ~ (m + n/2)π for large m + n. So mode ratios are O(few) for low modes, growing slowly.

For a *clover-shaped domain* (3-fold-symmetric with 3 convex lobes and 3 concave saddles), the spectrum differs from the disc. Key qualitative features:

- **3-fold symmetry** → most eigenvalues come in triplets (one per Z₃ rep). Some non-degenerate (trivial rep), some 2-fold degenerate (E rep).
- **Local geometry varies**: at lobe bumps, the domain is locally a disc of radius ~ r_lobe; at saddle indents, the domain narrows to width ~ r_saddle.
- **Modes can be classified** as: (a) spread across the whole cross-section ("whole-cross-section" modes), (b) concentrated in lobes ("lobe-localized"), or (c) concentrated at saddle constrictions ("saddle-localized"), with the localization regime requiring large geometric asymmetry between lobe and saddle scales.

For the **symmetric clover (χ ≡ r_saddle/r_lobe = 1)**, the cross-section is a smooth 3-fold-symmetric region with no dramatic asymmetry. The spectrum is qualitatively similar to a disc of effective radius ~ r_max = ε:

$$
\lambda_\alpha \;\approx\; \frac{(z_{nm}^{\mathrm{disc}})^2}{r_{\max}^2} \;=\; \frac{(z_{nm})^2}{\varepsilon^2}
$$

with order-unity corrections from the clover shape.

For the **asymmetric clover (χ ≠ 1)**, two limits are interesting:

**χ ≪ 1 (thin saddles, near-disconnected lobes):** the cross-section becomes three near-disconnected discs of radius r_lobe connected by thin saddle channels.
- Lowest band: 3 nearly-degenerate lobe-disc ground states at λ ≈ z_{01}²/r_lobe² = 5.78/r_lobe² = 5.78 (2+χ)²/ε².
- Higher bands: similarly 3-fold degenerate, at λ_{nm}/r_lobe².
- Inter-band ratios: (z_{nm}/z_{01})² — same as disc, of order 2.5–8 for low modes.
- *Saddle-localized modes* (modes whose amplitude concentrates in the narrow saddle necks) exist as gap states with λ_saddle ~ π²/r_saddle² = π² (2+χ)²/(εχ)². For very thin saddles (small χ), these are *very* high — λ_saddle ~ 1/χ² × (factors).

**χ ≫ 1 (saddles dominate, lobes are bumps on a hexagonal-like baseline):** the cross-section is approximately hexagonal-with-rounded-bumps. Lobe modes (bound to bumps) require the bump curvature to support trapping; for χ ≫ 1, the bumps are mild and don't strongly localize.

---

## 3. Mass spectrum and mass ratios — numerical evaluation

For each (ε, χ), compute the cross-section spectrum. I'll evaluate three regimes.

### 3.1 Symmetric clover (ε = 3, χ = 1) — clover-mass §8 Identification II operating point

In R_major = 1 units, r_max = 3, r_lobe = r_saddle = 1.

Cross-section λ_α ≈ (z_{nm})²/r_max² = (z_{nm})²/9. Low modes:

| Cross-section mode | λ_α | μ² = n_θ² + λ_α (at n_θ = 0) | μ |
|---|---|---|---|
| (0, 1) ground | 0.64 | 0.64 | 0.80 |
| (1, 1) | 1.63 | 1.63 | 1.28 |
| (2, 1) | 2.93 | 2.93 | 1.71 |
| (0, 2) | 3.39 | 3.39 | 1.84 |
| (3, 1) | 4.52 | 4.52 | 2.13 |
| (1, 2) | 5.47 | 5.47 | 2.34 |

Mass ratios from the ground state: 1.59, 2.13, 2.30, 2.65, 2.91. Up to a factor of ~3 across the lowest six modes.

**Compared to observed quark mass ratios:** 580 (m_c/m_u), 78000 (m_t/m_u). Way short.

### 3.2 Mildly asymmetric clover (ε = 3, χ = 0.1)

r_lobe = ε/(2+χ) = 1.43, r_saddle = 0.143.

In the χ ≪ 1 limit, the cross-section is three near-disconnected discs. Lobe-disc lowest mode: λ ≈ 5.78/r_lobe² = 2.83 (in R = 1 units).

Saddle-localized modes (if they exist as gap states): λ ~ π²/r_saddle² = 9.87/0.0204 ≈ 484.

Mass ratios:
- m_saddle / m_lobe = √(484/2.83) ≈ 13.

Better than the symmetric case (ratio 13 vs 3), but still not 580.

### 3.3 Highly asymmetric clover (ε = 3, χ = 0.01)

r_lobe ≈ 1.49, r_saddle = 0.0149.

λ_saddle ~ π²/r_saddle² = 9.87/0.000222 ≈ 44400.

m_saddle / m_lobe = √(44400/2.6) ≈ 130.

Closer to m_b/m_d ≈ 188, but still not reaching m_c/m_u ≈ 580 or m_t/m_u ≈ 78000.

### 3.4 Extreme asymmetry (ε = 3, χ = 0.001)

r_saddle = 0.0015. λ_saddle ~ 9.87/(0.0015)² ≈ 4.4 × 10⁶.

m_saddle / m_lobe ≈ √(1.6 × 10⁶) ≈ 1300.

Now in the right range for m_b/m_d ≈ 880 but overshoots. And still short of m_t/m_u ≈ 78000.

### 3.5 Summary of mass ratios

| χ | m_lobe (= μ at lobe-disc ground state) | m_saddle (= μ at saddle-localized mode) | Ratio |
|---|---|---|---|
| 1.0 | 0.80 | 0.80 (no separate saddle band) | 1 |
| 0.1 | 1.68 | 22 | 13 |
| 0.01 | 1.62 | 211 | 130 |
| 0.001 | 1.62 | 2105 | 1300 |
| 0.0001 | 1.62 | 21100 | 13000 |

Achieving m_t/m_u ≈ 78000 requires χ ≈ 10⁻⁵ (saddle thickness ~ 10⁻⁵ × lobe radius). This is an extreme structural asymmetry — far beyond what the clover-quarks kissing-circles geometry suggests as physically natural.

---

## 4. Where the picture works and where it fails

**The qualitative hierarchy emerges naturally.** Unlike the 2D-surface picture (where lobes are wells in the Hill equation's effective potential and localized states are *lighter* than plane-wave states), the 3D wave-guide picture treats the lobes as wider regions of the cross-section domain and saddles as narrower constrictions. The user's intuition "smaller cavity → higher frequency" applies correctly to the 3D wave-guide cross-section problem:

$$
\omega_{\mathrm{wc}} \;\sim\; \frac{1}{r_{\max}}
\;<\;
\omega_{\mathrm{lobe}} \;\sim\; \frac{1}{r_{\mathrm{lobe}}}
\;<\;
\omega_{\mathrm{saddle}} \;\sim\; \frac{1}{r_{\mathrm{saddle}}}
$$

For χ < 1, all three are distinct mass scales with the user's expected ordering. The picture *structurally* admits the hoped-for hierarchy.

**Quantitatively, the picture comes up short.** The cross-section mode ratios within one geometric family (e.g., the lobe-mode-band) are bounded by Bessel-zero ratios (~ 1.6, 2.1, 2.5, ...) — at most factors of ~10 across the lowest dozen modes. The saddle-vs-lobe ratio scales as 1/χ — which can be made arbitrarily large by making saddles arbitrarily thin, but at extreme asymmetry (χ ≪ 10⁻³) the geometric picture becomes questionable.

Reaching the observed m_t/m_u ≈ 78000 in a single sheet's 3D wave-guide spectrum requires χ ≈ 10⁻⁵ — structurally implausible for a "natural" clover-corrugated profile. The simplest 3D extension produces qualitative success but quantitative shortfall for the heaviest generations.

**Modes per generation.** In the 3D wave-guide picture, each cross-section mode α is itself 3-fold degenerate (from Z₃ symmetry of the clover). The 3-fold degeneracy could be interpreted as the 3 colors of QCD (per [color-confinement.md](color-confinement.md) framing). The "up vs down" distinction within a generation would come from a different mechanism — possibly the +2/3 / −1/3 per-arc curvature accounting of [clover-quarks §11](clover-quarks.md), which is independent of the 3D mode structure.

---

## 5. Comparison with grid's framework

Grid is *natively* 3D: the wave lives on a 3D lattice; the 2D torus is an emergent curvature feature. The "tube interior" is a region of 3D lattice space enclosed by the torus surface; waves there propagate according to the lattice action. Grid's "charge from bending" mechanism is the surface effect of this 3D structure — what gets out into observable 3D space.

The 3D wave-guide extension here is the closest metric-charge analog of grid's natural 3D structure. The boundary conditions on the surface (Dirichlet here for the simplest analysis) correspond to grid's perfect-reflection limit; the more physical case (radiation BCs at coupling strength α) gives finite-lifetime resonances rather than true bound states — same mass scale, but with a width Γ ∼ α ω.

The "internal leakage creates extra efficiencies" intuition (user's phrasing) corresponds to: the 3D-interior modes can self-interact through coupling at the surface (where bending mediates the energy flow). Modes with the same surface footprint (same n_θ, similar cross-section localization) can mix; this is a candidate amplification mechanism beyond the simple Helmholtz analysis here, and would require nonlinear coupling work (forwarded to metric-binding's territory).

---

## 6. Verdict

**The user's structural intuition is correct.** The 3D wave-guide extension of the clover picture admits the qualitative mass hierarchy whole-circumference < lobe-localized < saddle-localized, with mass scales 1/r_max < 1/r_lobe < 1/r_saddle. The 2D-surface analysis (which gave the *opposite* hierarchy with lobe-localized modes lighter than plane-waves) was an artifact of the 2D-thin-shell limit — the simplest 3D extension reverses this and produces the user's expected ordering.

**However, quantitative reach is limited.** Reaching observed inter-generation ratios (580, 78000) requires extreme cross-section asymmetry (χ ≈ 10⁻⁵ for the top quark), which is structurally implausible for a clover with kissing-circle geometry. The factor 1/χ from saddle-vs-lobe geometric asymmetry can deliver ratios up to ~10²–10³ in plausible regimes, sufficient for m_s/m_d, m_b/m_d, and potentially m_c/m_u, but not for m_t/m_u.

**What this means for the framework:**

1. **The single-sheet single-cross-section picture is insufficient for the full quark spectrum.** Even the 3D wave-guide extension can't span the full inter-generation gaps with one clover profile.

2. **For light generations (gen 1 ↔ gen 2 separation in the m_d ↔ m_s sense, factor ~20), the 3D picture in a moderately asymmetric clover (χ ~ 0.05–0.1) is workable.** This is encouraging structurally — it shows the framework can support multi-generation structure in a principled way, just not the full observed range from one sheet.

3. **Heavier generations (top, bottom) probably do require separate sheets.** Consistent with the [metric-binding](../../metric-binding/) framework's natural reading: each generation lives on a sheet with its own (ε, χ, geometric scale). The clover sheet supports the *light* generation plus possibly the second (with mild asymmetry χ ~ 0.1); the third generation is off-sheet.

4. **The Phase 3 negative verdict in [3-gen.md §12](3-gen.md) needs updating.** The 2D-surface analysis ruled out the user's picture under the surface-only idealization; this 3D extension shows the picture is *structurally compatible* in the 3D wave-guide interpretation. The two analyses are complementary — they apply to different mathematical setups. 3-gen.md §12 should reflect this: the 2D analysis ruled out the picture *in 2D*, but the 3D extension is qualitatively viable and quantitatively partial.

---

## 7. Open follow-ons

1. **Numerical eigenvalue computation for the clover cross-section.** Estimates here use disc-approximation Bessel zeros plus saddle-width arguments. A direct numerical solver for the 2D Helmholtz equation on the clover-shaped domain (with proper Dirichlet BCs) would replace these estimates with accurate eigenvalues, including the proper degeneracy structure and the lobe/saddle/whole-cross-section classification of eigenmodes.

2. **Torus-curvature correction.** The R_major / r_max correction (a factor of order 1 when the tube is fat) modifies cross-section eigenvalues. Worth including for any quantitative fit to a specific operating point.

3. **Radiation BCs and α-dependence.** Replace Dirichlet with absorbing/radiation BCs at the surface, parameterized by α (grid's coupling). Modes become resonances with finite width Γ ~ α ω. The mass scale is unchanged but the framework gains a natural width → decay-rate prediction.

4. **Connection to clover-mass §6.6's mass ratio survey.** The 3D-extension formula μ² = n_θ² + λ_α gives a richer parameter space than the 2D Hill equation. The compound-inventory picture of [clover-quarks §3](clover-quarks.md) (proton-as-2-lobe-1-saddle path) sits *on top of* this mode structure — each "arc" of the closure path is now a cross-section mode rather than a literal arc segment.

5. **What it would take to reach m_t/m_u ≈ 78000.** Either (a) extreme corrugation (χ ~ 10⁻⁵, structurally implausible), (b) a different cross-section geometry with intrinsically larger eigenvalue spread, (c) multi-sheet generations (per [metric-binding](../../metric-binding/) natural reading), (d) higher mode quantum numbers (gen 3 = high cross-section excitation, not gen 1's ground state). Option (c) is the most natural under the framework's broader architecture.

---

## 8. Cross-references

- [clover-modes-analytical.md](clover-modes-analytical.md) — the 2D-surface analysis (Hill equation on the corrugated surface), which showed the user's hoped-for hierarchy *cannot* emerge from the 2D-only idealization.
- [clover-quarks.md §11](clover-quarks.md) — per-arc curvature charge accounting (Q_lobe = +2/3, Q_saddle = −1/3); independent of mode structure (works in both 2D and 3D pictures).
- [clover-mass.md §4](clover-mass.md) — 2D-surface mass formula μ² = (n − 2m/3)² + (m/ε)²; this is the n_r = 0 (2D-mode) limit of the present 3D framework.
- [3-gen.md §12](3-gen.md) — Phase 3 negative numerical result; consistent with the 2D analysis but not informative about the 3D extension.
- [grid/charge-emergence.md](../../../grid/charge-emergence.md) — grid's natively-3D framework; the natural home for the wave-guide picture as a structural extension.
- [metric-charge Ch 10 §7](../../metric-charge/10-closing-summary.md) — the closing-summary section that flagged structural extensions outside scope, including "non-trivial T² fibration" and "higher-genus compact substrate"; the 3D-interior extension here is in the same family.
