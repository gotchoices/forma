# Chapter 6 — Handedness and pairs

**Status:** Sparse outline. Each section is one to three sentences describing the derivation step that section will perform. To be expanded into full prose once the outline is approved.

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

## Bare outline

### 1. What "handedness" means for knots

Two distinct kinds of sign-reflection are defined on knot space:

- **Sign reflection** (m, n) → (−m, −n) — reverses both windings simultaneously. Topologically the same unoriented closed curve traversed in the opposite direction; physically a different state in metric-charge per [Chapter 3 §3.2](03-knots-on-the-torus.md).
- **Mirror reflection** (m, n) → (m, −n) (or equivalently (−m, n)) — reverses one winding. Topologically a chirally distinct knot in 3-space (the mirror image); physically a different state.
<!--EC BTW, we gloss over mirror reflection as being equivalent.  But if we embed the sheet in such a way that ring and tube are distinct in their roles (is this possible?), then is mirror reflection still equivalent?  If this is not the right place to bring this up, fine.  But it might be worth knowing for sure.  -->

The chapter distinguishes these two operations carefully. They have different physical content and may correspond to different observables. Standard physics distinguishes parity from charge conjugation; the framework's two reflections may or may not align with that distinction.

### 2. The (m, n) → (−m, −n) reflection

This is the simplest discrete symmetry on knot space. Examine its content:

- **Topologically:** the same unoriented closed curve. Both signs trace out the same path on T², just in opposite direction.
- **In the (m, n) labeling:** different conserved sectors of the wave equation. The framework treats (1, 2) and (−1, −2) as distinct states because conservation operates on the integer pair, not on the unoriented curve.
- **Physically:** the (−1, −2) mode has opposite compact-direction momenta to (1, 2). Under the gauge-potential identification of [Chapter 5](05-metric-self-consistency.md), it sources off-diagonals of opposite sign — corresponding to opposite charge in the standard-physics sense.

Standard physics calls this the matter/antimatter axis: a particle and its antiparticle differ by sign of charge (and other internal quantum numbers). The framework's (m, n) → (−m, −n) reflection has the same structural property: opposite charge, same mass, same closure-eligibility. Whether the framework's reflection corresponds to standard physics' antimatter is a downstream MaSt-correspondence question; we treat it as a candidate identification.

### 3. The (m, n) → (m, −n) reflection (chirality)

A different operation: reverse only one winding. Examine its content:

- **Topologically:** mirror image of the original knot. Distinct from the unoriented original — chirally distinct in 3-space.
- **In the (m, n) labeling:** another distinct sector. (1, 2) and (1, −2) are different conserved sectors.
- **Physically:** the gauge-potential signs change for one direction but not the other. Net charge under the identifications of Chapter 5 may or may not be the same as the original.

Whether this corresponds to a standard-physics symmetry (parity? CP? something else?) is open. Possible interpretations:

- Parity (P): in standard physics, parity reverses spatial coordinates. Our reflection reverses one *compact* coordinate, which is structurally different. May or may not have a standard-physics analog.
- Chirality: in standard physics, chirality is a property of fermions distinguishing left- and right-handed states. The framework's mirror reflection may correspond to chirality if (m, n) ↔ (m, −n) corresponds to flipping spin direction relative to momentum.

Proceed with the analysis without committing to a specific standard-physics identification.

### 4. Pair configurations within a single field

A single field configuration φ can contain both (m, n) and (−m, −n) components simultaneously:

<!-- φ = α φ_(m,n) + β φ_(-m,-n) -->
$$
\varphi = \alpha\,\varphi_{(m,n)} + \beta\,\varphi_{(-m,-n)}
$$

with α, β complex coefficients. Under linear superposition, both modes are present at once.

Examine the resulting stress-energy and off-diagonal sourcing:

- **Diagonal entries (T_tt, T_uu, ...):** add as |α|² + |β|² — gravitational mass doubles when both modes are present at equal amplitude. (This is the metric-mass Ch 5 §7 result for ±n cancellation, extended to the 2D-compact case.)
- **Off-diagonal entries (T_tu, T_S₁u, ...):** each component sources off-diagonals of opposite sign. The combined off-diagonal scales as |α|² − |β|².

So when |α| = |β|, the off-diagonals **cancel exactly** — the configuration is gravitationally massive (2× a single mode) but produces zero net gauge potential. Net EM coupling is zero.

This is **cancellation neutrality**: a configuration that is massive but EM-neutral due to internal cancellation of opposite-handed components. It is structurally distinct from single-axis modes (which fail closure and are EM-neutral by *missing* one of the two gauge potentials). Both produce apparent neutrality but by different mechanisms.

### 5. Two distinct neutrality mechanisms

Compare the two mechanisms explicitly:

| Mechanism | Structural neutrality (Ch 4, 5) | Cancellation neutrality (this chapter) |
|---|---|---|
| Configuration | Single mode at (m, 0) or (0, n) | Single field with both (m, n) and (−m, −n) |
| Gauge structure | Partial — one U(1) only | Both U(1)s present, but fields cancel |
| Mass | Single mass m_(m, 0) | 2× mass: 2 m_(m, n) |
| Net charge | Zero (one U(1) missing for cross-coupling) | Zero (cancellation between opposite-sign sources) |
| Topological character | One winding zero | Both windings nonzero in each component |

Both mechanisms produce massive but EM-neutral states. The chapter's claim: **standard physics' "neutrino" property (mass, no EM) might correspond to either mechanism, or to a combination, or to one specific mechanism per neutrino species.** Which mechanism actually realizes observed neutrinos is a downstream MaSt-correspondence question and is not determined here.

[matter-from-light §4](../../papers/matter-from-light.md) and other MaSt model-F discussions have specific identifications; the framework here treats those as reference targets, not inputs. Both candidate mechanisms are made structurally available; which one (or both) corresponds to physical neutrinos is open.

### 6. Sign-bias and the asymmetric metric

When σ_uw shear is on (chapter 8), or when an external bias is introduced, the (m, n) ↔ (−m, −n) symmetry breaks. Connect to [metric-mass Chapter 7 §6](../metric-mass/07-shear-and-bias.md): in that chapter, an off-diagonal shear g_Su lifted ±n degeneracy via an n-linear cross-term in the dispersion relation. The 2D-compact analog: σ_uw shear (or a hypothetical σ_St shear) produces analogous bias on (±m, ±n) pairs.

Whether this bias corresponds to **what standard physics calls baryogenesis / matter-antimatter asymmetry** is the same question raised in metric-mass Chapter 7. The framework's view: shear-induced bias is one of the three Sakharov ingredients (CP-violation analog), not a complete baryogenesis mechanism. The mechanism for converting symmetric initial conditions into observed matter dominance requires additional ingredients beyond what this chapter establishes.

### 7. The multi-knot pair-behavior question

This chapter's analysis is for **single field configurations** containing multiple (m, n) components. The two-distinct-knots case — where two independent modes at different (S₁, S₂) positions interact — is energetics on a multi-knot configuration.

Forward to [metric-binding](../metric-binding/) for:

- **Pass-through:** do two opposite-handedness modes pass through each other linearly, as the metric-mass Ch 4 result for 1D-compact pairs suggested?
- **Annihilation:** at zero spatial separation, do the modes annihilate (mass-energy released)? metric-binding Ch 2 examines.
- **Bound states:** between pass-through and annihilation, is there a bound configuration where the modes orbit? metric-binding Chs 3–5.

This chapter's job is to establish the *single-field* pair structure (cancellation, sign-bias) that metric-binding's multi-knot energetics will operate on.

### 8. What's next

[Chapter 7 — Aspect ratio and character](07-aspect-ratio-and-character.md). Sweep ε = L_u / L_w and discover what knot families dominate at small ε (thin sheet), large ε (fat sheet), and ε ≈ 1. Look — without targeting it — for the conditions under which a sheet supports single-phase, three-phase, or dark behaviors. The "extreme aspect ratio" question (per MaSt model-F's electron-sheet identification) and the "diffuse charge" question (per model-F's neutrino-sheet identification) are examined there as reference targets.

---

## What this chapter does **not** do

- **Does not derive the Sakharov mechanism for baryogenesis.** Cite [metric-mass Chapter 7](../metric-mass/07-shear-and-bias.md) for the shear-bias analog; full baryogenesis requires three Sakharov ingredients and is downstream work.
- **Does not assign "matter" vs "antimatter" labels.** The framework treats (m, n) and (−m, −n) as distinct sectors but does not pre-commit to which corresponds to what standard physics calls matter.
- **Does not commit to whether parity (P) corresponds to mirror reflection or sign reflection.** Open question; downstream comparison with standard physics' P, C, CP symmetries.
- **Does not analyze multi-knot pair behavior** (pass-through, annihilation, bound states). [metric-binding](../metric-binding/).
- **Does not derive specific mass/charge ratios** for matter vs antimatter species. The framework predicts the same mass for (m, n) and (−m, −n) at the linearized level; full quantitative work is downstream.
- **Does not derive nonlinear pair-creation processes.** Linear theory only; pair creation/annihilation is a nonlinear / quantum phenomenon, deferred.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Does the framework's (m, n) → (−m, −n) reflection correspond to what standard physics calls antimatter, or to something else? | Downstream MaSt-correspondence work |
| Does the (m, n) → (m, −n) mirror reflection correspond to parity, chirality, or neither? | Open; downstream comparison with standard P/C/CP symmetries |
| What fraction of observed neutrinos correspond to structural-neutrality (Ch 4/5) vs cancellation-neutrality (this chapter) vs a hybrid? | MaSt-correspondence + experimental data |
| Does shear σ_uw produce a quantitatively meaningful matter/antimatter bias, or only a structural CP-violation analog? | Chapter 8 + downstream baryogenesis work |
| When a single field contains both (m, n) and (−m, −n) at unequal amplitudes, does the framework predict any observable consequence beyond standard EM? | Open; depends on the B_μ identification of Chapter 5 §8 |
| Is the (m, n) → (−m, −n) reflection a *physical* symmetry of the framework, or is it broken by some convention we have not yet identified? | Chapter 5 + grid alpha-derivation |
