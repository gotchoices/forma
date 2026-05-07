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

### 6. Optimizing k under shear — what value emerges?

This is the chapter's central derivation, framed as a real optimization rather than a proof of a presupposed answer.

Set up the optimization problem: given fixed (σ, ε), what value of k minimizes the total energy of a k-component multi-link configuration T(km, kn) at primitive (m, n) = (1, 1) (the lightest closure-eligible primitive at any ε per chapter 7)? Compute E(k; σ, ε), minimize over k, and report what optimal k(σ, ε) emerges.

The framework's *prediction* about k is the result of this optimization, not an input. The prose expansion works through the calculation; here we sketch the argument structure.

Candidate mechanisms for what k might be favored under shear (to be tested in the optimization):

- The shear's cross-term structure may favor specific phase separations between components on energetic grounds. If the structure is 2π/k-symmetric for some k, that k is a natural optimization candidate.
- A Z_k-symmetry constraint may make some k values satisfy a structural property that others don't. (Connect to grid-duality's Z₃ confinement at L3 — *if* the optimization confirms k = 3, this may be the topological reason for it.)
- Pure energetic minimization may pick out a k that doesn't correspond to any standard-physics analog, or k may vary non-trivially with (σ, ε).

The result of the optimization is reported as the framework's prediction. If k = 3 emerges as the optimum across the natural range of (σ, ε) values, the framework's structural match to what standard physics ascribes to quark organization is genuine. If a different k emerges, or if k varies substantially with (σ, ε) in ways that do not match observation, the framework's prediction differs from standard physics' quark structure — and that should be reported honestly.

This derivation is the substantive new content of chapter 8; the outline only sketches the argument structure. The prose expansion will work through the explicit energy minimization and report the answer.

### 7. The fractional-charge prediction — and consistency with grid-duality's quantization

Combine §5 and §6:

- Shear is what produces the multi-component link structure (without shear, ε alone doesn't favor multi-component, per chapter 7).
- The optimization in §6 identifies the favored k under shear; call this k_opt(σ, ε).
- For a multi-link configuration with k_opt components, each component is *associated with* 1/k_opt of the link's total charge.

**Consistency with grid-duality's integer charge quantization.** Per [grid-duality §7.5.4](../grid-duality/07-wrap-promotion-modeling.md), winding numbers are integer-valued and conserved. At first glance this conflicts with the per-component "fractional charges" above. The conflict is only apparent.

Grid-duality's integer quantization applies at the level of *complete closure-satisfying configurations*. A k-component link T(km, kn) is a single topological object — one winding pattern with definite integer (km, kn). The link as a whole carries integer charge under the quantization rule. The "1/k_opt charge per component" is not a *fractional charge of an individual closure-satisfying mode* — it is the *fractional association* of the link's integer total charge with each of its k structural components.

Three points clarify the consistency:

- **Components are not closure-satisfying on their own.** A single component of a multi-link, considered in isolation, is just a single (m, n) mode at primitive winding. Whether that single (m, n) satisfies closure depends on the standing-wave alignment requirement. For the multi-link case, it is the *collective configuration* (all k components together with their specific phase distribution) that satisfies closure. Individual components do not satisfy closure in isolation.

- **Integer total charge is preserved.** The full multi-link has charge proportional to its winding (km, kn) — integer-valued in the grid-duality sense. Distributing across k components gives 1/k per component, but the total integer charge is unchanged. No quantization rule is violated.

- **Confinement-like consequence.** Because individual components are not closure-satisfying alone, they are not isolable as physical states — they only exist as parts of the collective k-link. This is structurally analogous to what standard physics calls quark confinement: individual quarks carry fractional charge and are not observable in isolation; only color-neutral composite states are.

So the framework's fractional-charge prediction is consistent with grid-duality's integer winding quantization, and predicts confinement-like behavior as a structural consequence: per-component fractional values exist only inside the collective configuration, with integer total preserved.

**The framework's prediction:** on a sheet with shear σ_uw ≠ 0, the dominant multi-component closure-satisfying configurations are k_opt-component links with 1/k_opt charge associated per component, and individual components are not isolable. If §6's optimization yields k_opt = 3, this matches the structural pattern of standard physics' quark organization (3 components per baryon, each with 1/3 fractional charge under confinement). If §6 yields a different k_opt, or yields k_opt varying with (σ, ε), the framework's prediction differs from observed quark structure and should be reported honestly.

Whether the framework's specific predictions (k_opt, charge magnitudes, mass ratios, link-stability conditions) match standard physics' quark properties under detailed comparison is downstream MaSt-correspondence work.

### 8. Summary — what shear adds to the inventory

The ε sweep of [Chapter 7](07-aspect-ratio-and-character.md) gave three regimes of sheet character (mass-only-dominated at extremes, charge-friendly at ε ≈ 1). Adding shear σ_uw to that inventory:

- **Breaks (m, n) ↔ (−m, −n) symmetry** — Sakharov-CP-violation analog, supporting matter/antimatter asymmetry.
- **Selects a k_opt-component link structure** — the optimization in §6 picks out which k minimizes link energy under shear; the framework reports what k_opt(σ, ε) emerges.
- **Produces 1/k_opt fractional charges per component** — distributed across the link's structural components, with integer total charge preserved (consistent with grid-duality §7.5.4).
- **Predicts confinement-like behavior for individual components** — per §7, individual components of a multi-link are not closure-satisfying in isolation and therefore not isolable.

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
