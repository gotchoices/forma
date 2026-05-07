# Chapter 6 — Handedness and pairs

This chapter examines the **chirality / handedness** structure of the closure-satisfying inventory. The (m, n) labels carry sign as well as magnitude; this chapter asks what physical content the sign carries, and what happens when configurations contain both signs simultaneously.

The key distinction the chapter is structured around: **structural neutrality** (single-axis modes from chapters 4 and 5, where one winding is exactly zero) versus **cancellation neutrality** (single field configuration containing complementary pairs that cancel in net). These are different mechanisms producing apparent neutrality. Chapter 6 develops the second; chapters 4 and 5 already developed the first.

The two-distinct-knots version of pair behavior — when two separate closure-satisfying modes with opposite handedness collide in S — is **not** in this chapter. It is energetics on a multi-knot configuration and is forwarded to [metric-binding](../metric-binding/).

**Inheritance.**

- *From [Chapter 3 §3.2](03-knots-on-the-torus.md):* the topological equivalences (sign reflection, mirror reflection) and the framing that they are *not* generally physical equivalences.
- *From [Chapter 4](04-the-closure-condition.md):* the closure-satisfying inventory.
- *From [Chapter 5](05-metric-self-consistency.md):* the gauge-potential structure that distinguishes EM-observable from internal modes.
- *From [metric-mass Chapter 7](../metric-mass/07-shear-and-bias.md):* the analysis of ±n bias in a sheared metric — the Sakharov-CP-violation analog. metric-charge's chapter 6 carries this forward to 2D-compact configurations.

**Distinctive job.** Distinguish the two neutrality mechanisms (structural vs cancellation). Determine what physical content the (m, n) → (−m, −n) sign reflection carries. Cross-reference standard physics' matter/antimatter axis as a comparison target. Set up the multi-knot pair-behavior question for [metric-binding](../metric-binding/).

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | What "handedness" means for knots — two distinct reflections |
| 2 | The (m, n) → (−m, −n) reflection — content and standard-physics correspondence |
| 3 | The (m, n) → (m, −n) reflection — chirality and the ring/tube distinction |
| 4 | Pair configurations within a single field |
| 5 | Two distinct neutrality mechanisms — structural vs cancellation |
| 6 | Sign-bias and the asymmetric metric |
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

This is a sharp question worth addressing. The two operations agree at the topological-curve level — both produce the same mirror knot up to traversal reversal. But the metric-charge framework distinguishes ring (u) and tube (w) by the four conventions of [Chapter 3 §3.2](03-knots-on-the-torus.md): closure asymmetry, aspect-ratio labeling, shear, gauge convention. Once those conventions are stacked, are (m, −n) and (−m, n) still equivalent?

**Topologically: yes.** The bare knot type is the same.

**Physically in metric-charge: no.** The two configurations have different (m, n) integer labels, conserved in different sectors of the wave equation. They source different patterns of off-diagonals — (−m, n) reverses the u-direction's gauge potential A_μ while keeping B_μ; (m, −n) reverses B_μ while keeping A_μ. If both U(1)s in the framework's prediction are physical, the two operations correspond to different physical states with opposite charges in *different* gauge sectors. Even if only one U(1) is physical (open question per [Chapter 5 §8](05-metric-self-consistency.md)), the two operations would correspond to charge-conjugate states in different roles depending on which U(1) is identified as the physical EM.

This is consistent with the broader topology-vs-physics pattern of Chapter 3: topology is symmetric under (u, w) ↔ (w, u) and under their independent reflections; physics with conventions is not. The mirror reflection inherits the same asymmetry.

So when this chapter speaks of "the mirror reflection," it is referring to the topological operation. The two physical realizations (m, −n) and (−m, n) are distinct states; we treat them as two members of the mirror-reflection class rather than identifying them.

---

## 2. The (m, n) → (−m, −n) reflection

This is the simplest discrete symmetry on knot space — sign reflection of both windings simultaneously. Examine its content from three angles.

### 2.1 Topological content

The (−m, −n) curve traces the same path in 3-space as (m, n), just in the opposite direction. As an *unoriented* curve, the two are identical. As *oriented* curves, they are inverses — opposite traversal direction.

This is the simplest topological identification on knot space: forgetting orientation. For our framework, orientation matters at the wave-equation level (the (m, n) labels are conserved as an integer pair, including signs), so the topological identification does not reduce the physical state space.

### 2.2 (m, n)-labeling content

The framework treats (m, n) and (−m, −n) as **distinct conserved sectors**. Their integer labels are different; the wave equation conserves them separately. A (1, 2) mode and a (−1, −2) mode are different physical states even though they trace the same unoriented curve.

### 2.3 Physical content under the gauge-potential identification of Chapter 5

The (−m, −n) mode has compact-direction momenta of opposite sign to (m, n):

<!-- p_u^(-m,-n) = -p_u^(m,n),  p_w^(-m,-n) = -p_w^(m,n) -->
$$
p_u^{(-m,-n)} = -p_u^{(m,n)},\qquad p_w^{(-m,-n)} = -p_w^{(m,n)}
$$

Under the linearized Einstein analysis of [Chapter 5](05-metric-self-consistency.md), the off-diagonal stress-energy is T_μu ∝ p_u and T_μw ∝ p_w. So the (−m, −n) mode sources off-diagonals of opposite sign — corresponding to opposite gauge-potential charge under the standard-physics identification.

In standard-physics terms: (m, n) and (−m, −n) are configurations of opposite charge but identical mass and identical closure-eligibility. This is the structural property of what standard physics calls a particle and its antiparticle — the matter/antimatter axis.

The framework's reflection has the same structural property. Whether the framework's (m, n) → (−m, −n) reflection corresponds to standard physics' antimatter is a downstream MaSt-correspondence question. We treat it as a candidate identification; the structural correspondence at the property level (opposite charge, same mass) holds, but identifying specific framework states with specific standard-physics particles requires quantitative work beyond this chapter's scope.

---

## 3. The (m, n) → (m, −n) reflection (chirality)

A different operation: reverse only one winding. Examine its content.

### 3.1 Topological content

The (m, −n) curve is the **mirror image** of (m, n) in 3-space. For genuine torus knots T(p, q) with both p, q ≥ 2 and gcd = 1, the mirror image is *chirally distinct* — a different knot type that cannot be deformed to the original without going through 4-space or breaking the curve. Trefoil T(2, 3) and its mirror T(2, −3) are the prototype: they are different (chiral) torus knots.

For "weak knot" diagonal modes (T(1, q) and T(p, 1)), both the original and mirror are unknots — chirally trivial — but the (m, n) labels are different and the modes are still physically distinct in metric-charge per Chapter 3.

### 3.2 (m, n)-labeling content

(m, n) and (m, −n) are different conserved sectors. The wave equation treats them as distinct integer pairs.

### 3.3 Physical content under the gauge-potential identification

The (m, −n) mode has p_u of the same sign as (m, n) but p_w of opposite sign:

<!-- p_u^(m,-n) = p_u^(m,n),  p_w^(m,-n) = -p_w^(m,n) -->
$$
p_u^{(m,-n)} = p_u^{(m,n)},\qquad p_w^{(m,-n)} = -p_w^{(m,n)}
$$

So the off-diagonal sourcing is mixed: A_μ (from h_μu) is unchanged, B_μ (from h_μw) is reversed. The configuration carries the same charge under one gauge potential but opposite charge under the other.

### 3.4 What standard-physics symmetry does this correspond to?

This is open. Several candidate identifications:

- **Parity (P).** In standard physics, parity reverses spatial coordinates and flips left-handed states to right-handed. The framework's mirror reflection reverses one *compact* coordinate, which is structurally different from reversing spatial coordinates. Whether there is an analog connection (compact-coordinate parity ↔ spatial parity in some appropriate limit) is open.
- **Charge conjugation (C).** In standard physics, charge conjugation reverses charge sign of a particle. The framework's mirror reflection reverses one of the two charge contributions but not the other — closer to "partial charge conjugation" than to full C. Doesn't cleanly correspond.
- **CP (combined C and P).** A composite operation in standard physics. The framework's mirror reflection does not obviously match either P alone or C alone, but might match a particular combination depending on identifications downstream.
- **Chirality (handedness of fermions).** In standard physics, chirality distinguishes left- and right-handed fermions by the relative orientation of spin and momentum. The framework's mirror reflection might correspond to chirality if (m, n) ↔ (m, −n) corresponds to flipping the spin direction relative to momentum — which it plausibly does, if spin in this framework is derived from the (m, n) winding ratio per matter-from-light §4.

Proceed with the analysis without committing to a specific standard-physics identification. The framework's mirror reflection is a real discrete operation on knot space; its standard-physics correspondence is downstream MaSt-correspondence work.

---

## 4. Pair configurations within a single field

A single field configuration φ can contain both (m, n) and (−m, −n) components simultaneously:

<!-- φ = α φ_(m,n) + β φ_(-m,-n) -->
$$
\varphi = \alpha\,\varphi_{(m,n)} + \beta\,\varphi_{(-m,-n)}
$$

with α, β complex coefficients. Under linear superposition, both modes are present at once; the wave equation has no nonlinear coupling that would mix them, so both components evolve independently in their respective conserved sectors.

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

This is **cancellation neutrality**: a configuration that is massive but EM-neutral due to internal cancellation of opposite-handed components. Both U(1)s are present in the configuration, but their charges sum to zero.

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

## 5. Two distinct neutrality mechanisms

Compare the two mechanisms producing apparent EM-neutrality:

| Mechanism | Structural neutrality (Ch 4, 5) | Cancellation neutrality (this chapter) |
|---|---|---|
| Configuration | Single mode at (m, 0) or (0, n) | Single field with both (m, n) and (−m, −n) at equal amplitude |
| Gauge structure | Partial — one U(1) only; lacks U(1)×U(1) cross-coupling | Both U(1)s present, but net contributions cancel |
| Mass | Single mass m_(m, 0) or m_(0, n) | 2× mass: 2 m_(m, n) |
| Net charge | Zero (one gauge potential is missing entirely) | Zero (internal cancellation between opposite-sign sources) |
| Topological character | One winding zero; (m, n) → (m, 0) or (0, n) | Both windings nonzero in each component |
| Distinction from light | Has mass; no propagation at c | Has mass; no propagation at c |

Both mechanisms produce massive but EM-neutral states. The distinction matters for downstream identification:

- **Structural neutrality** is *fundamental* — it cannot be made to carry charge by adjusting amplitudes or phases. The mode structurally lacks one of the two gauge potentials.
- **Cancellation neutrality** is *contingent* — it depends on equal amplitudes between the two components. Adjusting α/β tunes the configuration between fully charged and fully neutral.

Standard physics identifies several massive but EM-neutral particles: neutrinos, certain neutral mesons (like K⁰), the Higgs boson, etc. Some of these have intrinsic-property neutrality (neutrinos' lack of EM coupling is fundamental), while others have neutrality through structure (K⁰ is a quark-antiquark pair whose charges cancel).

The framework's two mechanisms map structurally:

- Structural neutrality might correspond to what standard physics calls neutrinos (intrinsic, fundamental neutrality).
- Cancellation neutrality might correspond to what standard physics calls neutral mesons or other composite-pair states (configuration-dependent neutrality).

Whether these candidate identifications hold depends on quantitative comparison and is downstream MaSt-correspondence work. The framework establishes that *both* mechanisms are structurally available and structurally distinct; which standard-physics particles correspond to which mechanism is open.

---

## 6. Sign-bias and the asymmetric metric

When σ_uw shear is on (chapter 8), or when an external bias is introduced through some other mechanism, the (m, n) ↔ (−m, −n) symmetry breaks. [metric-mass Chapter 7 §6](../metric-mass/07-shear-and-bias.md) examined this in the 1D-compact case: an off-diagonal shear g_Su lifted the ±n degeneracy via an n-linear cross-term in the dispersion relation. The framework's Sakharov-CP-violation analog lives there, and metric-charge inherits the same structural result on the 2D-compact substrate.

### 6.1 The shear-induced bias

With σ_uw ≠ 0, the dispersion relation acquires cross-terms that depend on the *signs* of m and n, not just their magnitudes. Consequently:

- (m, n) and (−m, −n) modes have slightly different dispersion ω(k_S; m, n) ≠ ω(k_S; −m, −n) when σ_uw ≠ 0.
- In thermal equilibrium, the populations of (m, n) and (−m, −n) are not exactly equal — the asymmetry is direction-correlated.
- The (k_S, m, n) ↔ (−k_S, −m, −n) symmetry of the sheared dispersion is exact, so pure thermal equilibrium gives direction-correlated asymmetry without net (m, n) → (−m, −n) population bias.

### 6.2 Standard physics correspondence

This is the framework's analog of one of the three Sakharov conditions for baryogenesis:

1. Baryon-number violation (or its analog): present.
2. C-violation and CP-violation (or their analogs): the shear provides this — different dispersion for (m, n) vs (−m, −n).
3. Departure from thermal equilibrium: not provided by the framework alone; requires cosmological inputs.

So the framework provides one Sakharov ingredient (the CP-analog from shear-induced bias). Full baryogenesis requires additional ingredients — particularly a non-equilibrium phase, which the framework does not derive. The CP-analog *prediction* is consistent with what standard physics calls CP-violation (a known feature of weak interactions); whether the framework's mechanism quantitatively reproduces observed CP-violation is downstream work.

---

## 7. The multi-knot pair-behavior question

This chapter's analysis is for **single field configurations** containing multiple (m, n) components — superpositions of opposite-handedness modes within one field. The two-distinct-knots case — where two independent modes at different (S₁, S₂) positions interact — is energetics on a multi-knot configuration and lies outside this chapter.

The same is true of **phase-offset configurations**: two distinct (m, n) modes at the same (S₁, S₂) but at different phase positions on the torus form a single field by linear superposition, with each mode evolving independently in its own conserved sector. Whether such a combined configuration is energetically stable, or whether it relaxes to one of its components, is a multi-knot energetics question — also forwarded to [metric-binding](../metric-binding/). Phase-offset configurations include both special cases already addressed (the multi-component link of [Chapter 4 §4.3](04-the-closure-condition.md), where k copies at 2π/k offsets share the same (m, n)) and the more general case of distinct (m, n) modes coexisting with arbitrary phase relationships, which is not addressed here.

Forward to [metric-binding](../metric-binding/) for:

- **Pass-through:** do two opposite-handedness modes pass through each other linearly, as the metric-mass Ch 4 result for 1D-compact pairs suggested? metric-binding Ch 2 examines.
- **Annihilation:** at zero spatial separation, do the modes annihilate (mass-energy released)? metric-binding Ch 2.
- **Bound states:** between pass-through and annihilation, is there a bound configuration where the modes orbit? metric-binding Chs 3–5.
- **Pair-creation thresholds:** under what energy conditions does the wave equation (or its appropriate extension) allow creation/annihilation of (m, n) ↔ (−m, −n) pairs from light? Out of scope for this project (linear theory only); deferred to nonlinear/quantum extensions.

This chapter's job is to establish the *single-field* pair structure (cancellation, sign-bias) that metric-binding's multi-knot energetics will operate on.

---

## 8. What's next

[Chapter 7 — Aspect ratio and character](07-aspect-ratio-and-character.md). Sweep ε = L_u / L_w and discover what knot families dominate at small ε (thin sheet), large ε (fat sheet), and ε ≈ 1. Look — without targeting it — for the conditions under which a sheet supports single-phase, three-phase, or dark behaviors. The "extreme aspect ratio" question (per MaSt model-F's electron-sheet identification) and the "diffuse charge" question (per model-F's neutrino-sheet identification) are examined there as reference targets, not as identifications this project pre-commits to.

Chapter 7 changes the parameter focus from sign labels (Chapter 6) to magnitude scales (the aspect ratio ε). Together, chapters 6 and 7 cover the two most important sub-(m, n) parameters: handedness and aspect ratio.

---

## What this chapter does **not** do

- **Does not derive the Sakharov mechanism for baryogenesis.** Cite [metric-mass Chapter 7](../metric-mass/07-shear-and-bias.md) for the shear-bias analog; full baryogenesis requires three Sakharov ingredients and is downstream work.
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
| What fraction of observed neutrinos correspond to structural-neutrality (Ch 4/5) vs cancellation-neutrality (this chapter) vs a hybrid? | MaSt-correspondence + experimental data |
| Does shear σ_uw produce a quantitatively meaningful matter/antimatter bias, or only a structural CP-violation analog? | Chapter 8 + downstream baryogenesis work |
| When a single field contains both (m, n) and (−m, −n) at unequal amplitudes, does the framework predict any observable consequence beyond standard EM? | Open; depends on the B_μ identification of Chapter 5 §8 |
| Is the (m, n) → (−m, −n) reflection a *physical* symmetry of the framework, or is it broken by some convention we have not yet identified? | Chapter 5 + grid alpha-derivation |
| If the conventions of Chapter 3 §3.2 distinguish u and w, do (m, −n) and (−m, n) correspond to physically distinguishable states or just to two presentations of the same mirror configuration? | Chapter 5 + grid alpha-derivation; the answer depends on whether one or both U(1)s are physical |
