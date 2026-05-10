# Chapter 6 — Handedness and pairs

This chapter examines the **chirality / handedness** structure of the closure-satisfying inventory. The (m, n) labels carry sign as well as magnitude; this chapter asks what physical content the sign carries, and what happens when configurations contain both signs simultaneously.

The key distinction the chapter is structured around: **structural neutrality** (single-axis modes from chapters 4 and 5, where one winding is exactly zero) versus **cancellation neutrality** (single field configuration containing complementary pairs that cancel in net). These are different mechanisms producing apparent neutrality. Chapter 6 develops the second; chapters 4 and 5 already developed the first.

The two-distinct-knots version of pair behavior — when two separate closure-satisfying modes with opposite handedness collide in S — is **not** in this chapter. It is energetics on a multi-knot configuration and is forwarded to [metric-binding](../metric-binding/).

**Inheritance.**

- *From [Chapter 3 §3.2](03-knots-on-the-torus.md):* the topological equivalences (sign reflection, mirror reflection) and the framing that they are *not* generally physical equivalences.
- *From [Chapter 4](04-the-closure-condition.md):* the closure-satisfying inventory.
- *From [Chapter 5](05-metric-self-consistency.md):* the gauge-potential structure that distinguishes EM-observable from internal modes.
- *From [metric-mass Chapter 7](../metric-mass/07-shear-and-bias.md):* the analysis of ±n bias in a sheared metric (under shear σ_Su, between extended and compact). metric-charge's σ_uw shear is structurally different (between two compacts) — see §6 for the explicit comparison.

**Distinctive job.** Distinguish the structural-neutrality and cancellation-neutrality mechanisms. Determine what physical content the (m, n) → (−m, −n) sign reflection carries. Derive what σ_uw shear actually breaks at the dispersion level. Set up the multi-knot pair-behavior question for [metric-binding](../metric-binding/).

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | What "handedness" means for knots — two distinct reflections |
| 2 | The (m, n) → (−m, −n) reflection — content and standard-physics correspondence |
| 3 | The (m, n) → (m, −n) reflection — chirality and the ring/tube distinction |
| 4 | Pair configurations within a single field |
| 5 | Three distinct neutrality mechanisms |
| 6 | What σ_uw shear breaks: chirality within particles, not matter/antimatter populations |
| 7 | The multi-knot pair-behavior question |
| 8 | What's next |

---

## 1. What "handedness" means for knots

Two distinct kinds of sign-reflection are defined on knot space, and they have different physical content. The chapter distinguishes them carefully.

**Sign reflection** (m, n) → (−m, −n) reverses *both* windings simultaneously. Topologically, this is the same unoriented closed curve traversed in the opposite direction — same knot type, same shape in 3-space, just reverse traversal direction. Physically in metric-charge, per [Chapter 3 §3.2](03-knots-on-the-torus.md), it is a different state (different conserved sector with different (m, n) integer labels).

**Mirror reflection** reverses *one* winding only:

<!-- (m, n) → (m, -n) or (-m, n) -->
$$
(m, n) \to (m, -n) \quad\text{or}\quad (-m, n)
$$

Topologically these two operations both produce the **mirror image** of the original knot — chirally distinct from the original in 3-space. As unoriented closed curves in 3-space, the two operations produce the same mirror knot (one is just the other's traversal reversed).

### 1.1 Are (m, −n) and (−m, n) equivalent in metric-charge?

This is a sharp question worth addressing. The two operations agree at the topological-curve level — both produce the same mirror knot up to traversal reversal. But the metric-charge framework distinguishes ring (u) and tube (w) via the wrap-order convention of [Chapter 1 §10](01-foundation.md). Once the wrap-order is fixed, are (m, −n) and (−m, n) still equivalent?

**Topologically: yes.** The bare knot type is the same.

**Physically in metric-charge: no.** The two configurations have different (m, n) integer labels, conserved in different sectors of the wave equation. Under the natural-particle construction of [Chapter 5 §4](05-metric-self-consistency.md), they relate differently to the wrap-order's R_u-symmetrization: (−m, n) is the R_u-conjugate of (m, n) (combining them gives the natural particle's R_u-symmetrized form, with cross-term in h_μw); (m, −n) is the R_w-conjugate (combining them would standing-wave the tube direction, which the wrap-order rules out as a particle symmetry — see Ch 5 §4.3). So the two operations play structurally different roles in the natural-particle construction.

This is consistent with the broader topology-vs-physics pattern of Chapter 3: topology is symmetric under (u, w) ↔ (w, u) and under their independent reflections; physics with the wrap-order convention is not. The mirror reflection inherits the same asymmetry.

So when this chapter speaks of "the mirror reflection," it is referring to the topological operation. The two physical realizations (m, −n) and (−m, n) are distinct states; we treat them as two members of the mirror-reflection class rather than identifying them.

---

## 2. The (m, n) → (−m, −n) reflection

This is the simplest discrete symmetry on knot space — sign reflection of both windings simultaneously. Examine its content from three angles.

### 2.1 Geometric content — traversal orientation

The (−m, −n) curve traces the same point set in 3-space as (m, n), just visited in the opposite order. Per [Chapter 1 §6.1](01-foundation.md), every closed curve on the 2-torus admits two orientations; the (m, n) → (−m, −n) operation is exactly the operation that switches between them. As an *unoriented* curve, the two configurations are identical; as *oriented* curves, they are inverses.

The framework's primary label is the signed integer pair (m, n), and the sign tracks traversal orientation as a geometric property of the closed curve — not as an internal field-theoretic label. The orientation distinction is therefore *not* eliminated by working with a real-valued φ; it lives in the manifold's topology, not in the field's value space.

### 2.2 (m, n)-labeling content

The framework treats (m, n) and (−m, −n) as **distinct conserved sectors**. Their integer labels are different; the wave equation conserves them separately. A (2, 1) mode and a (−2, −1) mode are different physical states — they trace the same unoriented curve but with opposite traversal direction, and they carry opposite-sign compact-direction momenta.

### 2.3 Physical content under the gauge-potential analysis of Chapter 5

The (−m, −n) mode has compact-direction momenta of opposite sign to (m, n):

<!-- p_u^(-m,-n) = -p_u^(m,n),  p_w^(-m,-n) = -p_w^(m,n) -->
$$
p_u^{(-m,-n)} = -p_u^{(m,n)},\qquad p_w^{(-m,-n)} = -p_w^{(m,n)}
$$

This is a kinematic statement: a wave packet traveling around the closed curve in the opposite direction carries opposite-sign compact momentum. No internal field-theoretic structure is invoked.

Under the linearized Einstein analysis of [Chapter 5](05-metric-self-consistency.md), the per-component off-diagonal stress-energy is T_μu ∝ p_u and T_μw ∝ p_w. The natural particle's surviving cross-term h_μw scales with p_w, so the (−m, −n) mode sources h_μw of opposite sign — opposite-sign coupling under the framework's single gauge potential B_μ. (The would-be h_μu cross-term cancels in the natural particle by R_u-symmetrization, regardless of mode labels.)

### 2.4 What does this opposite-sign property correspond to physically?

Open at this stage. The framework establishes that:

- (m, n) and (−m, −n) are configurations of identical mass (energy density depends on |m|, |n| only) and identical closure-eligibility (the closure rule depends only on magnitudes via n | m or equivalently the chirality criterion).
- They source opposite-sign h_μw — under the natural-particle construction of [Ch 5 §4](05-metric-self-consistency.md), opposite-sign coupling under the single gauge potential B_μ.
- They correspond to opposite traversal directions on the same closed curve.

These structural properties are what standard physics ascribes to a particle and its antiparticle (same mass, opposite charges, complementary conservation labels). Whether the framework's (m, n) → (−m, −n) reflection actually corresponds to what standard physics calls antimatter — versus to some other physical distinction (or to no physical distinction beyond a redundant labeling) — is left open. The chapter's stance:

- **The opposite-sign-momentum property is geometric and unambiguous.** It falls out of the orientation of closed curves on T² (per Ch 1 §6.1) and the kinematics of wave packets on those curves.
- **The matter/antimatter identification is a candidate, not a commitment.** Whether (m, n) ↔ (−m, −n) corresponds to particle ↔ antiparticle requires that something physically distinguish the two beyond their structural opposite-charge property — i.e., something that breaks the (m, n) ↔ (−m, −n) symmetry of the dispersion. **σ_uw shear cannot do this** ([§6](#6-what-σ_uw-shear-breaks-chirality-reflection-not-sign-reflection) demonstrates: the σ_uw cross-term k_u·k_w is invariant under joint sign flip). The framework currently has no derived mechanism that breaks (m, n) ↔ (−m, −n); whether one exists at the substrate level (grid-primitive / grid-duality) or via a different shear in the metric is open ([§6.7](#67-matterantimatter-bias--open)).
- **If some mechanism does break (m, n) ↔ (−m, −n), the matter/antimatter analog acquires physical content; if no mechanism breaks it, the two labels may be redundant presentations of the same physical state.** The framework does not pre-commit; the math is what determines this, and the math currently leaves it open.

---

## 3. The (m, n) → (m, −n) reflection (chirality)

A different operation: reverse only one winding. Examine its content.

### 3.1 Topological content

The (m, −n) curve is the **mirror image** of (m, n) in 3-space. For genuine torus knots T(p, q) with both p, q ≥ 2 and gcd = 1, the mirror image is *chirally distinct* — a different knot type that cannot be deformed to the original without going through 4-space or breaking the curve. Trefoil T(2, 3) and its mirror T(2, −3) are the prototype: they are different (chiral) torus knots.

For "weak knot" diagonal modes (T(m, 1) primitives — and equivalently T(1, q) under cycle swap, which is *not* a closure-satisfying form in the framework's wrap-order), both the original and mirror are unknots — chirally trivial — but the (m, n) labels are different and the modes are still physically distinct in metric-charge per Chapter 3.

### 3.2 (m, n)-labeling content

(m, n) and (m, −n) are different conserved sectors. The wave equation treats them as distinct integer pairs.

### 3.3 Physical content under the gauge-potential identification

The (m, −n) mode has p_u of the same sign as (m, n) but p_w of opposite sign:

<!-- p_u^(m,-n) = p_u^(m,n),  p_w^(m,-n) = -p_w^(m,n) -->
$$
p_u^{(m,-n)} = p_u^{(m,n)},\qquad p_w^{(m,-n)} = -p_w^{(m,n)}
$$

So under the natural-particle construction, the surviving cross-term h_μw is *reversed* under the mirror reflection — the gauge potential B_μ flips sign. (The would-be h_μu cross-term cancels in the natural particle anyway, so the per-component-level reversal of its sign has no consequence in the natural particle.) The configuration carries opposite charge under B_μ.

### 3.4 What standard-physics symmetry does this correspond to?

This is open. Several candidate identifications:

- **Parity (P).** In standard physics, parity reverses spatial coordinates and flips left-handed states to right-handed. The framework's mirror reflection reverses one *compact* coordinate, which is structurally different from reversing spatial coordinates. Whether there is an analog connection (compact-coordinate parity ↔ spatial parity in some appropriate limit) is open.
- **Charge conjugation (C).** In standard physics, charge conjugation reverses charge sign of a particle. The framework's mirror reflection reverses one of the two charge contributions but not the other — closer to "partial charge conjugation" than to full C. Doesn't cleanly correspond.
- **CP (combined C and P).** A composite operation in standard physics. The framework's mirror reflection does not obviously match either P alone or C alone, but might match a particular combination depending on identifications downstream.
- **Chirality (handedness of fermions).** In standard physics, chirality distinguishes left- and right-handed fermions by the relative orientation of spin and momentum. The framework's mirror reflection might correspond to chirality if (m, n) ↔ (m, −n) corresponds to flipping the spin direction relative to momentum — which is plausible if spin in this framework derives geometrically from the substrate's torus structure (open work, per [Chapter 3 §5](03-knots-on-the-torus.md)).

Proceed with the analysis without committing to a specific standard-physics identification. The framework's mirror reflection is a real discrete operation on knot space; its standard-physics correspondence is downstream MaSt-correspondence work.

---

## 4. Pair configurations within a single field — the sign-conjugate case

This section examines configurations of the form (m, n) + (−m, −n) — *sign-conjugate* pair configurations. Under the natural-particle construction of [Chapter 5 §4](05-metric-self-consistency.md), this is R_J-symmetrization (joint reversal). For closure-satisfying modes, R_u was the natural choice (giving one gauge potential); choosing R_J instead is a *voluntary* construction that cancels the gauge potential and gives a mass-only configuration with chirality field T_uw — what this section calls cancellation-pair neutrality.

A single field configuration φ can contain both (m, n) and (−m, −n) components simultaneously:

<!-- φ = α φ_(m,n) + β φ_(-m,-n) + c.c. -->
$$
\varphi = \alpha\,\varphi_{(m,n)} + \beta\,\varphi_{(-m,-n)} + \text{c.c.}
$$

with α, β complex amplitudes that set the magnitude (|α|, |β|) and phase of each traveling-wave component. The "+ c.c." (complex conjugate) makes the resulting field real-valued, consistent with [Chapter 1 §6](01-foundation.md); the complex-amplitude notation is calculational shorthand for two independent real-valued traveling waves on the same closed curve, traversing it in opposite directions per [Chapter 1 §6.1](01-foundation.md). Under linear superposition, both components are present at once; the wave equation has no nonlinear coupling that would mix them, so they evolve independently in their respective conserved sectors.

### 4.1 The stress-energy of the pair configuration

Compute T_μν for this superposition. The diagonal entries:

<!-- T_diagonal ∝ |α|² + |β|² -->
$$
T_{\mu\mu} \;\propto\; |\alpha|^2 + |\beta|^2
$$

Both components contribute additively. When |α| = |β|, the total energy density (and gravitational mass) is **doubled** compared to a single mode.

The off-diagonal entries:

<!-- T_off-diagonal ∝ |α|² - |β|² -->
$$
T_{\mu\nu}^{\text{off-diag}} \;\propto\; |\alpha|^2 - |\beta|^2
$$

The opposite-handedness components source off-diagonals of opposite sign (per §2.3), so the contributions subtract. This generalizes the [metric-mass Chapter 5 §7](../metric-mass/05-metric-self-consistency.md) ±n cancellation result to the 2D-compact setting; the same structural cancellation operates in both projects.

### 4.2 The cancellation case |α| = |β|

When both components have equal amplitude, the off-diagonals cancel exactly. The configuration is:

- **Gravitationally massive** with mass 2 m_(m, n) (twice a single mode).
- **EM-neutral** at the linearized level — no net gauge potential, no observable EM coupling.

This is **cancellation neutrality**: a configuration that is massive but EM-neutral due to internal cancellation of opposite-handed components. The natural-particle construction (R_u-symmetrization) is replaced by R_J-symmetrization, which cancels the spacetime↔compact gauge potential and leaves only diagonal mass plus the chirality-encoded compact-compact cross-term T_uw.

### 4.3 The unequal case |α| ≠ |β|

When the two components have unequal amplitudes, the off-diagonals do not cancel completely. The configuration has:

- **Total gravitational mass** ∝ |α|² + |β|² (still 2× a single mode if both nonzero).
- **Net charge** ∝ |α|² − |β|² (intermediate between full charge and zero).

A configuration with |α| ≠ |β| has a continuously-tunable net charge, going from full positive at α=1, β=0 through neutral at α=β to full negative at α=0, β=1.

### 4.4 Are unequal configurations stable?

The wave equation does not constrain the relative amplitudes α, β — both are set by the field's preparation (initial conditions). At the linearized level, any (α, β) pair is an equally valid solution.

Whether unequal configurations are *physically realized* in nature is an energetics question, not a wave-equation question. The framework predicts the *space of possible configurations*; which configurations are actually populated requires energy minimization, thermal equilibration, or other dynamical considerations beyond chapter 6's scope.

For comparison: standard physics treats matter and antimatter as distinct species with conservation laws governing their populations. The framework's view is similar — (m, n) and (−m, −n) are conserved sectors — but allows superpositions in principle. Whether superpositions occur in observed physics is a downstream question.

---

## 5. Three distinct neutrality mechanisms

The framework has *three* structurally distinct mechanisms producing apparent EM-neutrality. Chapters 4 and 5 developed the first two (single-axis structural neutrality and chirality-non-degenerate neutrality of genuine torus knots); this section develops the third (sign-conjugate cancellation pair).

| Mechanism | Single-axis (Ch 4, 5) | Chirality-non-degenerate (Ch 4, 5) | Cancellation pair (this chapter) |
|---|---|---|---|
| Configuration | Single mode at (m, 0) or (0, n) | Single mode at T(p, q), p, q ≥ 2, gcd = 1 (genuine torus knot) | Single field with both (m, n) and (−m, −n) at equal amplitude (closure-satisfying mode in R_J-symmetrized form) |
| Particle symmetry enforced | R_u or R_w (only one available; no chirality structure to test) | R_J only (R_u and R_w not topological symmetries; chirality is non-degenerate) | R_J chosen voluntarily over the available R_u (closure-satisfying mode would be charged under R_u; R_J cancels the gauge potential instead) |
| Mass | Single mass m_(m, 0) or m_(0, n) | Single mass m_(p, q) | 2× mass: 2 m_(m, n) |
| Net cross-terms | T_tu, T_tw, T_uw all zero | T_tu, T_tw zero; T_uw nonzero (chirality field) | T_tu, T_tw zero; T_uw nonzero (chirality field) |
| Tunable? | No — fundamental (curve admits no chirality structure) | No — fundamental for the (m, n) sector (chirality is topologically non-degenerate) | Yes — cancellation depends on equal amplitudes; adjusting α/β tunes the configuration between fully charged (R_u-symmetrized natural particle) and fully cancelled (R_J pair) |

Each mechanism produces a massive but EM-neutral state by a structurally distinct route. The distinction matters for downstream identification:

- **Single-axis neutrality** is fundamental and structural — the curve admits no chirality structure (one winding is zero), so the natural-particle construction reduces to metric-mass's standing wave on a single direction.
- **Chirality-non-degenerate neutrality** is fundamental for genuine torus knots — the curve is chirally distinct from its mirror, so R_u is not a topological symmetry, and the natural particle falls back to R_J-symmetrization, sourcing T_uw (chirality field) but no spacetime↔compact gauge potential.
- **Cancellation-pair neutrality** is contingent — it operates on a closure-satisfying mode that *could* be charged (R_u was available) but is configured as an R_J-symmetrized pair instead. Adjusting α/β tunes the configuration between fully charged and fully cancelled.

Standard physics identifies several massive but EM-neutral particles: neutrinos (three flavors), neutral mesons (K⁰, B⁰, etc.), the Higgs boson, dark matter candidates, etc. Some have *intrinsic-property* neutrality (neutrinos' lack of EM coupling is fundamental); others have *structural-pair* neutrality (K⁰ is a quark-antiquark pair); still others have other origins.

The framework's three mechanisms map structurally onto multiple standard-physics neutral-mass categories:

- **Single-axis neutrality** might correspond to neutrinos or to one specific category of fundamental neutral states.
- **Chirality-non-degenerate neutrality** might correspond to a different category — possibly neutral hadrons-in-isolation, the Higgs, or some standard-physics state with chirality structure but no observable EM.
- **Cancellation-pair neutrality** might correspond to what standard physics calls neutral mesons or other composite-pair states with configuration-dependent neutrality (matter-antimatter bound state of a closure-satisfying mode).

Whether these candidate identifications hold depends on quantitative comparison and is downstream MaSt-correspondence work. The framework establishes that *three* structurally distinct neutrality mechanisms are available; which standard-physics particles correspond to which mechanism is open. The richness of the framework's neutral inventory — three structurally distinct categories — is suggestive of standard physics' multiple neutral categories, but the specific mapping is not determined here.

---

## 6. What σ_uw shear breaks: chirality reflection, not sign reflection

This section works through the dispersion relation under σ_uw shear and asks which symmetries σ_uw breaks. The answer is precise and constraining: σ_uw breaks the **chirality reflection** (m, n) ↔ (m, −n) (and equivalently (m, n) ↔ (−m, n)), and it leaves the **sign reflection** (m, n) ↔ (−m, −n) invariant. Under work1's natural-particle construction (Ch 5 §4), this means σ_uw biases the *internal amplitude balance of a particle* (its R_u-symmetrized (++) vs (−+) components) rather than its matter/antimatter populations.

The derivation is short and forced; we walk through it explicitly.

### 6.1 The dispersion relation under σ_uw shear

From [Chapter 8 §1–§2](08-shear-and-fractional-charge.md), the wave equation on the sheared metric gives the Bloch-mode dispersion:

<!-- ω²/c² = k_S² + (k_u² - 2σ k_u k_w + k_w²) / (1 - σ²) -->
$$
\frac{\omega^2}{c^2} = k_S^2 + \frac{k_u^2 - 2\sigma\,k_u\,k_w + k_w^2}{1 - \sigma^2}
$$

with k_u = 2πm/L_u and k_w = 2πn/L_w. The σ-dependence enters entirely through the **cross-term** −2σ·k_u·k_w. This is the only piece of the dispersion that distinguishes σ ≠ 0 from σ = 0 in a sign-sensitive way: k_u² and k_w² are even in (m, n) and unchanged by any sign flip.

### 6.2 Symmetry test on the cross-term

Apply each candidate sign-flip symmetry to the cross-term k_u·k_w:

| Symmetry | Maps (k_u, k_w) → | Cross-term k_u·k_w → | Dispersion invariant? |
|---|---|---|---|
| **(m, n) ↔ (−m, −n)** (sign reflection) | (−k_u, −k_w) | (−k_u)(−k_w) = +k_u k_w | **Yes — invariant** |
| **(m, n) ↔ (m, −n)** (chirality, n flips) | (k_u, −k_w) | k_u·(−k_w) = −k_u k_w | **No — flips sign** |
| **(m, n) ↔ (−m, n)** (chirality, m flips) | (−k_u, k_w) | (−k_u)·k_w = −k_u k_w | **No — flips sign** |
| **Full sign flip** (k_S, m, n) ↔ (−k_S, −m, −n) | all flip | invariant | **Yes — invariant** |

The math is forced: a bilinear cross-term is invariant under joint sign flip of both factors and flips under one-sided sign flip. This is purely algebra; nothing more sophisticated than that.

**Concrete example.** Take k_u = k_w = K > 0 (so the magnitudes match). Compute the cross-term contribution for each pair:

- Mode (1, 1) and mode (−1, −1): both have k_u·k_w = +K². *Identical contribution. Same dispersion. Same effective mass.*
- Mode (1, 1) and mode (1, −1): one has +K², the other has −K². *Opposite contributions. Different dispersion.*

For σ > 0, the explicit mass split between the chirality-conjugate pair is:

<!-- m²(1, 1) ∝ 2K²(1 - σ),  m²(1, -1) ∝ 2K²(1 + σ) -->
$$
m^2_{(1, 1)} \;\propto\; 2K^2(1 - \sigma), \qquad m^2_{(1, -1)} \;\propto\; 2K^2(1 + \sigma)
$$

Mass split between the **chirality** partners; **no split** between the sign partners.

### 6.3 What this means structurally

The σ_uw entry is symmetric in (u, w) (g_uw = g_wu) and represents a non-orthogonal slant between the two compact directions. Geometrically: a wave going "along the slant" (k_u, k_w of like sign) experiences a different effective length than one going "against the slant" (opposite signs). Chirality is the natural axis a slant distinguishes; joint sign flip rotates the wave 180° in the (u, w) plane and leaves its alignment with the slant unchanged.

This means σ_uw is, *purely from the geometry*, a chirality-bias mechanism. The framework's machinery does not allow it to be otherwise.

### 6.4 Comparison with metric-mass's σ_Su shear

[metric-mass Chapter 7](../metric-mass/07-shear-and-bias.md) introduces shear σ_Su between *extended S* and *compact u*. The cross-term in that case is k_S·k_u — bilinear in *one extended and one compact* wavenumber. Under (n) → (−n) (so k_u → −k_u), this cross-term flips sign — correctly breaking the (n) ↔ (−n) symmetry in the 1D-compact setting.

metric-charge's σ_uw is a different shear: between two compact directions. The cross-term is k_u·k_w — bilinear in two compacts. The two shears break different symmetries:

| Shear | Cross-term | Symmetry broken |
|---|---|---|
| σ_Su (metric-mass, 1D-compact) | k_S · k_u | (n) ↔ (−n) — sign reflection |
| σ_uw (metric-charge, 2D-compact) | k_u · k_w | (m, n) ↔ (m, −n) — chirality reflection |

Earlier framings in this chapter and Chapter 8 conflated the two and presented σ_uw as the "2D-compact extension" of metric-mass's mechanism. They are structurally distinct mechanisms operating on different symmetries. The 2D-compact extension of metric-mass's σ_Su would be σ_S₁u or σ_S₁w — extended-versus-compact shear — which metric-charge's [Chapter 1 §4](01-foundation.md) does not introduce.

### 6.5 Consequences for the framework

The chirality-bias result has consequences that follow directly from the math, made sharper under work1's natural-particle construction:

- **σ_uw biases chirality *within particles*, not matter/antimatter populations.** Whatever asymmetry σ_uw introduces operates on the (m, n) ↔ (m, −n) axis (and equivalently (m, n) ↔ (−m, n) — the R_u and R_w reflections, which σ_uw breaks). For a natural particle (R_u-symmetrized configuration of (++) and (−+) per Ch 5 §4), σ_uw shifts the energies of the (++) and (−+) components in opposite directions, producing an internal amplitude bias within the particle. This is *intra-particle chirality bias*.

- **σ_uw does not bias matter vs antimatter.** The (m, n) ↔ (−m, −n) sign reflection — which the framework treats as the matter/antimatter axis (§2) — is invariant under σ_uw (the cross-term k_u·k_w is unchanged under joint sign flip). σ_uw shifts matter and antimatter rest energies *equally*; it cannot bias their populations at the dispersion level. **Whatever produces the universe's matter/antimatter asymmetry, it is not σ_uw.**

- **Sign-conjugate cancellation pairs (§4) remain neutral under shear.** A configuration with (m, n) + (−m, −n) at equal amplitude has identical dispersion for both components even at σ ≠ 0; the cancellation neutrality of §4 is robust under σ_uw shear.

- **The R_w-symmetrized configuration is energetically disfavored under shear.** A configuration of the form (m, n) + (m, −n) — combining chirality-conjugates in the *tube* direction — is not a natural particle under the wrap-order convention (Ch 5 §4.3 rules out R_w as a particle symmetry). Under σ_uw ≠ 0, the two components sit at different energies (per §6.2), so this configuration is also not in thermal equilibrium. It would tend to redistribute toward whichever component the σ_uw shear favors energetically — settling into either (m, n) alone or (m, −n) alone, neither of which is by itself a natural particle. The configuration is structurally and energetically marginal.

### 6.6 Matter/antimatter bias — open

The framework derives chirality bias *within particles* from σ_uw. It does **not** derive matter/antimatter bias on populations from any mechanism in this chapter or [Chapter 8](08-shear-and-fractional-charge.md). If matter/antimatter asymmetry is a structural prediction of the framework, it must come from some other mechanism. Candidate locations the framework's broader stack might supply such a mechanism:

- **A different shear in the metric.** Shear between an extended direction and a compact direction (σ_Su or σ_Sw) would break (m) ↔ (−m) or (n) ↔ (−n) by the metric-mass mechanism. metric-charge's [Chapter 1 §4](01-foundation.md) introduces only σ_uw; introducing a second shear would be a structural change the project does not currently take.
- **Substrate-level chirality from the underlying lattice.** Inherited from [grid-primitive](../grid-primitive/) or [grid-duality](../grid-duality/), the substrate may carry a built-in preferred direction at the edge level (chiral edge twist, asymmetric edge orientation) that propagates upward and biases (m, n) ↔ (−m, −n) at the mode level. This would be a substrate boundary condition, not a metric-charge derivation.
- **Some structural mechanism not yet identified.**

The chapter does not commit to any of these. The math is honest: σ_uw alone cannot do it. The matter/antimatter bias question is forwarded to project-direction work and to the substrate-level projects.

---

## 7. The multi-knot pair-behavior question

This chapter's analysis is for **single field configurations** containing multiple (m, n) components — superpositions of opposite-handedness modes within one field. The two-distinct-knots case — where two independent modes at different (S₁, S₂) positions interact — is energetics on a multi-knot configuration and lies outside this chapter.

The same is true of **phase-offset configurations**: two distinct (m, n) modes at the same (S₁, S₂) but at different phase positions on the torus form a single field by linear superposition, with each mode evolving independently in its own conserved sector. Whether such a combined configuration is energetically stable, or whether it relaxes to one of its components, is a multi-knot energetics question — also forwarded to [metric-binding](../metric-binding/). Phase-offset configurations include both special cases already addressed (the multi-component link of [Chapter 4 §4.3](04-the-closure-condition.md), where k copies at 2π/k offsets share the same (m, n)) and the more general case of distinct (m, n) modes coexisting with arbitrary phase relationships, which is not addressed here.

Forward to [metric-binding](../metric-binding/) for:

- **Pass-through:** do two opposite-handedness modes pass through each other linearly, as the metric-mass Ch 4 result for 1D-compact pairs suggested? metric-binding Ch 2 examines.
- **Annihilation:** at zero spatial separation, do the modes annihilate (mass-energy released)? metric-binding Ch 2.
- **Bound states:** between pass-through and annihilation, is there a bound configuration where the modes orbit? metric-binding Chs 3–5.
- **Pair-creation thresholds:** under what energy conditions does the wave equation (or its appropriate extension) allow creation/annihilation of (m, n) ↔ (−m, −n) pairs from light? Out of scope for this project (linear theory only); deferred to nonlinear/quantum extensions.

This chapter's job is to establish the *single-field* pair structure (sign-conjugate and chirality-conjugate cancellation, plus σ_uw's chirality bias) that metric-binding's multi-knot energetics will operate on.

---

## 8. What's next

[Chapter 7 — Aspect ratio and character](07-aspect-ratio-and-character.md). Sweep ε = L_u / L_w and discover what knot families dominate at small ε (thin sheet), large ε (fat sheet), and ε ≈ 1. Look — without targeting it — for the conditions under which a sheet supports single-phase, three-phase, or dark behaviors. The "extreme aspect ratio" question (per MaSt model-F's electron-sheet identification) and the "diffuse charge" question (per model-F's neutrino-sheet identification) are examined there as reference targets, not as identifications this project pre-commits to.

Chapter 7 changes the parameter focus from sign labels (Chapter 6) to magnitude scales (the aspect ratio ε). Together, chapters 6 and 7 cover the two most important sub-(m, n) parameters: handedness and aspect ratio.

---

## What this chapter does **not** do

- **Does not derive a matter/antimatter bias mechanism.** §6 demonstrates that σ_uw shear biases chirality *within particles* (the R_u-symmetrized (++) vs (−+) amplitude balance), not matter/antimatter populations — σ_uw is invariant under (m, n) ↔ (−m, −n) joint sign flip. Whether the framework derives matter/antimatter bias from any other mechanism is left open at this chapter (see §6.6).
- **Does not derive the Sakharov mechanism for baryogenesis.** σ_uw provides intra-particle chirality bias only; the C-flavor (sign reflection) bias on populations has no derived mechanism in this chapter or [Chapter 8](08-shear-and-fractional-charge.md). Full Sakharov baryogenesis would require both C and CP violation plus a non-equilibrium phase; the framework currently provides at most a P-flavor intra-particle ingredient.
- **Does not assign "matter" vs "antimatter" labels** to specific (m, n) sectors. The framework treats (m, n) and (−m, −n) as distinct sectors but does not pre-commit to which corresponds to what standard physics calls matter.
- **Does not commit to whether parity (P) corresponds to mirror reflection or sign reflection** or some other operation. Open question; downstream comparison with standard physics' P, C, CP symmetries.
- **Does not analyze multi-knot pair behavior** (pass-through, annihilation, bound states). [metric-binding](../metric-binding/).
- **Does not derive specific mass/charge ratios** for matter vs antimatter species. The framework predicts the same mass for (m, n) and (−m, −n) at the linearized level; full quantitative work is downstream.
- **Does not derive nonlinear pair-creation processes.** Linear theory only; pair creation/annihilation is a nonlinear/quantum phenomenon, deferred.
- **Does not commit to whether (m, −n) and (−m, n) are physically equivalent** — they are topologically equivalent but the conventions of [Chapter 3 §3.2](03-knots-on-the-torus.md) break the equivalence physically. Both treated as distinct states in the framework.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Does the framework's (m, n) → (−m, −n) reflection correspond to what standard physics calls antimatter, or to something else? | Downstream MaSt-correspondence work |
| Does the (m, n) → (m, −n) mirror reflection correspond to parity, chirality, charge conjugation, or none of these? | Open; downstream comparison with standard P/C/CP symmetries |
| What fraction of observed neutrinos correspond to single-axis (Ch 4/5), chirality-non-degenerate (Ch 4/5), or sign-conjugate cancellation (§4)? | MaSt-correspondence + experimental data |
| **Does the framework derive a matter/antimatter bias from any mechanism?** §6 shows σ_uw cannot do it (σ_uw biases chirality within particles, not matter/antimatter populations). Candidate alternatives include extended-compact shear (σ_Su), substrate-level chirality from grid-primitive/grid-duality, or other unidentified mechanisms. | Project-direction question; possibly resolved at substrate level |
| When a single field contains both (m, n) and (−m, −n) at unequal amplitudes, does the framework predict any observable consequence? | Open; couples to the substrate-level matter/antimatter origin question |
| Is the (m, n) → (−m, −n) reflection a *physical* symmetry of the framework, or is it broken by some convention we have not yet identified? | Substrate-level work; possibly grid-primitive's chirality |
| If the wrap-order convention distinguishes u and w, do (m, −n) and (−m, n) correspond to physically distinguishable states or just to two presentations of the same mirror configuration? | Chapter 5 §4.3 (R_w-symmetrization is wrap-order-ruled-out as a particle symmetry; the configurations are distinct from natural particles) |
