# Chapter 8 — Shear and fractional charge

**Status:** Sparse outline. Each section is one to three sentences describing the derivation step that section will perform. To be expanded into full prose once the outline is approved.

This chapter turns on the off-diagonal shear σ_uw and examines what it adds to the framework. So far the framework has worked with the bare diagonal metric (σ_uw = 0); this chapter introduces shear as a parameter and traces its consequences through the inventory.

The chapter has two main payloads. First, it carries the [Chapter 6 §6](06-handedness-and-pairs.md) shear-bias result through to the 2D-compact case explicitly, confirming the Sakharov-CP-violation analog for matter/antimatter asymmetry. Second, it derives the **fractional-charge mechanism**: N phased wraps distributed in w contribute 1/N charge each, with **shear specifically selecting k = 3** as the dominant multi-phase configuration. This is where the multi-component link structure of [Chapter 4 §4.3](04-the-closure-condition.md) connects to the three-phase organization that MaSt model-F (and standard physics' quark inventory) might correspond to.

**Inheritance.**

- *From [Chapter 1 §4](01-foundation.md):* the σ_uw shear definition and its deferred status; the metric form with shear active.
- *From [Chapter 6 §6](06-handedness-and-pairs.md):* the shear-bias / Sakharov-CP-violation analog; ±(m, n) symmetry breaking from off-diagonal coupling.
- *From [Chapter 7 §6](07-aspect-ratio-and-character.md):* the finding that ε alone does not select three-phase character; chapter 8 must provide the missing mechanism.
- *From [metric-mass Chapter 7](../metric-mass/07-shear-and-bias.md):* the 1D-compact shear-bias analysis. The 2D-compact extension is the immediate target.

**Distinctive job.** Derive the framework's prediction for **why three-phase fractional charge** is the structurally favored configuration when shear is on, and confirm the shear-bias symmetry-breaking from Chapter 6 quantitatively. These are the two key open mechanisms the framework needs to provide for the inventory to map onto standard physics' organization (matter/antimatter asymmetry; quark-like three-phase fractional charge).

The framework treats both predictions as **emergent results** of the framework's own machinery. Standard physics' three-phase quark organization and observed matter/antimatter asymmetry are reference targets to compare against, not inputs.

---

## Bare outline

### 1. Setting up the shear σ_uw

Restate the metric with shear active (from [Chapter 1 §4](01-foundation.md)):

<!-- ds² = -c² dt² + dS₁² + dS₂² + du² + 2 σ du dw + dw² -->
$$
ds^2 = -c^2\,dt^2 + dS_1^2 + dS_2^2 + du^2 + 2\,\sigma_{uw}\,du\,dw + dw^2
$$

The (u, w) sub-block is now:

<!-- (u, w) sub-block -->
$$
g^{(u,w)}_{ab} = \begin{pmatrix} 1 & \sigma_{uw} \\ \sigma_{uw} & 1 \end{pmatrix}
$$

The wave equation acquires cross-terms from the off-diagonal inverse metric. The compact-direction Laplacian becomes:

<!-- Laplacian with σ shear -->
$$
\nabla_{(u,w)}^2 \;\to\; \frac{1}{1-\sigma^2}\left(\partial_u^2 - 2\sigma\,\partial_u\partial_w + \partial_w^2\right)
$$

Periodicity boundary conditions need to be applied along sheared lattice vectors, not the rectangular (u, w) basis. Defer detailed treatment of the sheared lattice to §2.

### 2. Effects on the mass spectrum

With σ ≠ 0, the dispersion relation acquires σ-dependent cross-terms. For a (m, n) mode:

<!-- ω²/c² = k_S² + (k_u² - 2σ k_u k_w + k_w²)/(1-σ²) -->
$$
\frac{\omega^2}{c^2} = k_S^2 + \frac{k_u^2 - 2\sigma\,k_u\,k_w + k_w^2}{1 - \sigma^2}
$$

with k_u = 2πm/L_u, k_w = 2πn/L_w as before (modulo periodicity adjustments under shear).

Several structural observations:

- The cross-term −2σ k_u k_w breaks the (m, n) ↔ (−m, −n) symmetry: a mode with k_u and k_w of the same sign sees a different effective mass than one with opposite signs.
- This is the **shear-bias** mechanism — the 2D-compact extension of metric-mass's 1D-compact result ([metric-mass Chapter 7 §6](../metric-mass/07-shear-and-bias.md)).
- The (1, 1) mode and the (−1, −1) mode acquire different masses under shear, by an amount proportional to σ.
- Mode crossings: at specific σ values, the order of (1, 1) vs (1, −1) vs (−1, 1) vs (−1, −1) reorganizes, producing structurally interesting transition points.

### 3. Matter/antimatter bias from shear (the Sakharov-CP-violation analog)

Carry forward the [metric-mass Chapter 7](../metric-mass/07-shear-and-bias.md) analysis to 2D-compact:

- The ±(m, n) symmetry is broken by shear: m_(1, 1) ≠ m_(−1, −1) when σ ≠ 0.
- However, the (k_S, m, n) → (−k_S, −m, −n) symmetry of the *full* dispersion relation (including spacetime momenta) is exact.
- Pure thermal equilibrium gives direction-correlated asymmetry: at given (k_S₁, k_S₂), the (m, n) and (−m, −n) populations differ, but summed over all k_S directions they balance.

This is the framework's analog of one Sakharov ingredient (CP-violation) for what standard physics calls baryogenesis. The other two Sakharov ingredients (baryon-number-violation analog; non-equilibrium phase) are not provided by this chapter alone.

The chapter establishes the CP-violation analog *quantitatively* (computing the mass split, predicting the direction-correlated asymmetry coefficient) — going beyond Chapter 6 §6's structural statement that the bias exists.

### 4. The closure condition under shear

Does the closure condition itself change under σ ≠ 0?

The phase-pattern view of [Chapter 1 §10](01-foundation.md): "2π winding on w + standing wave on both u and w." This is stated in the bare-metric basis. Under shear, the natural "windings on u" and "windings on w" become entangled through the sheared lattice — a single closed traversal in the sheared-coordinate basis advances by mixed amounts in (u, w) directions.

Two ways to interpret:

- **Conservative:** the closure condition in the bare basis is unchanged; the wave equation's modes adjust their behavior under shear. (m, n) labels remain meaningful.
- **Sheared-basis:** the closure condition is naturally stated in the sheared basis, where the relevant labels are mass-eigenvalue pairs (m̃, ñ) related to (m, n) by σ-dependent linear combinations.

The chapter takes the conservative interpretation: closure operates on (m, n) labels in the bare basis; shear is a perturbation that affects masses and dispersion but not the closure condition itself. This is consistent with closure being a phase-pattern statement that doesn't depend on which basis is used to describe the wave.

### 5. Multi-component links under shear — energetics

Take a multi-component link T(km, kn) at gcd = k > 1. Under shear, the energetics of the k phased components changes:

- Each component is a phase-shifted copy of the primitive T(m, n).
- Phase-shifts within the (u, w) cycle interact with the shear cross-term −2σ k_u k_w in mode-dependent ways.
- The total energy of the k-component configuration depends on the *relative phases* of the components.

Specifically: if the k components are at phases 2π·j/k for j = 0, 1, ..., k−1, the total energy summed over components contains cross-terms between different j values. The cross-terms are sensitive to σ and to the specific phase distribution.

The chapter computes this sum and asks: at what k is the multi-component configuration most energetically favorable under shear?

### 6. Why k = 3 specifically — the three-phase mechanism

This is the chapter's key derivation. Argue (in the prose expansion) that shear σ_uw selects k = 3 cleanly via:

- The shear's cross-term has a structure that favors 2π/3 phase separations between components.
- Specifically, the energy of the k-component configuration as a function of σ has a minimum at k = 3 for nontrivial σ (in the small-shear limit, possibly extending to all σ in the framework's allowed range).
- The k = 3 configuration also satisfies a Z₃-symmetry constraint that simpler k = 2 or k = 4 configurations don't satisfy. (Connect to grid-duality's Z₃ confinement at L3 — possibly a topological reason for k = 3.)

The result: under shear, three-component links T(3m, 3n) are the energetically preferred multi-component configuration, with each component carrying 1/3 of the primitive's charge.

This derivation is the substantive new content of chapter 8; the outline only sketches the argument structure. The prose expansion will work through the calculation explicitly.

### 7. The fractional-charge prediction

Combine §5 and §6:

- Shear is what produces the multi-component link structure (without shear, ε alone doesn't favor multi-component).
- Shear specifically selects k = 3.
- Each component of the resulting T(3m, 3n) link carries 1/3 of the primitive T(m, n)'s charge.

So the framework predicts: **on a sheet with shear σ_uw ≠ 0, the dominant multi-component closure-satisfying configurations are 3-component links with fractional 1/3 charges per component.**

This matches the structural pattern of standard physics' quark organization: 3 quarks per baryon, each with 1/3 fractional charge (or 2/3 for up-type quarks). Whether the framework's specific predictions for fractional-charge values, mass ratios, and other observables match standard physics' quark properties is a downstream MaSt-correspondence question.

### 8. Summary — what shear adds to the inventory

The ε sweep of [Chapter 7](07-aspect-ratio-and-character.md) gave three regimes of sheet character (mass-only-dominated at extremes, charge-friendly at ε ≈ 1). Adding shear σ_uw to that inventory:

- **Breaks (m, n) ↔ (−m, −n) symmetry** — Sakharov-CP-violation analog, supporting matter/antimatter asymmetry.
- **Selects three-component link structure** — k = 3 via the shear's energetic preference.
- **Produces fractional 1/3 charges** — naturally, from the three-phase distribution.

Together with ε from chapter 7 and handedness from chapter 6, σ_uw gives the framework four parameters / structural choices that organize the closure-eligible inventory:

| Parameter | What it controls |
|---|---|
| (m, n) labels | Primary mode identity (chapters 2, 3) |
| Closure satisfaction | Charge vs no-charge (chapter 4) |
| Handedness sign | Matter/antimatter (chapter 6) |
| Aspect ratio ε | Sheet character / regime (chapter 7) |
| Shear σ_uw | Three-phase structure / fractional charge (this chapter) |

This is the framework's full structural inventory at the linearized level. Whether it corresponds to standard physics' particle inventory at the level of specific particle properties — masses, charges, decay rates, magnetic moments — is the downstream MaSt-correspondence work the framework leaves open.

### 9. What's next

[Chapter 9 — Closing summary](09-closing-summary.md). Consolidate what the project established, ruled out, and unexpectedly found across all eight chapters. Hand off to [metric-binding](../metric-binding/) for the multi-knot interaction story (multi-knot energetics, force laws, bound states, candidate strong-force mechanism).

---

## What this chapter does **not** do

- **Does not derive numerical α** or charge magnitudes. Cited from [grid-duality §8](../grid-duality/08-where-alpha-appears.md); structural location settled there, numerical values open.
- **Does not derive specific quark masses or mixing angles.** The framework predicts the structural pattern (three-phase links with 1/3 fractional charge) but not specific mass values; quantitative predictions are downstream MaSt-correspondence work.
- **Does not provide a complete baryogenesis mechanism.** The CP-violation analog from §3 is one of three Sakharov ingredients; the others are not provided.
- **Does not derive nonlinear shear effects.** Linear theory only. Whether large σ produces qualitatively different behavior (beyond the linear approximation breaking down) is downstream work.
- **Does not analyze interaction between distinct three-component links.** Multi-knot energetics is metric-binding territory.
- **Does not explain why σ_uw takes a specific value** on any given sheet. ε and σ are both treated as free parameters; whether they are dynamically determined is open.
- **Does not commit to MaSt-correspondence assignments.** The fractional-charge / three-phase prediction matches the structural pattern of standard physics' quarks; specific identifications (which (m, n) corresponds to which quark family, etc.) are downstream work.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Does the k = 3 selection follow from the local shear-cross-term structure alone, or does it require global topology (Z₃ from grid-duality) as an input? | Open; possibly resolved by grid-duality's substrate analysis |
| Does the shear-induced CP-violation analog quantitatively match observed CP-violation magnitudes? | Downstream MaSt-correspondence work + experimental data |
| Are there other multi-component links (k = 5, k = 7, ...) energetically favored at specific σ values, corresponding to potential exotic states? | Open follow-up; downstream investigation |
| Does the framework predict any deviation from standard quark mass / charge ratios that could be experimentally tested? | Open; depends on quantitative completion of the framework |
| What is the relationship between the framework's σ_uw and observed CP-violating phases (e.g., CKM matrix phases)? | Downstream MaSt-correspondence work |
| Does the choice of which compact direction is "tube" (closure-asymmetric) vs "ring" force a specific sign convention on σ_uw, or is the sign free? | Convention question; possibly settled by combination of Chapters 3 §3.2 and 5 §6.3 |
| At very large σ (approaching the |σ| < 1 boundary where the metric becomes degenerate), does the framework predict any structural transitions or singular behavior? | Out of scope; possibly relevant for nonlinear extensions |
