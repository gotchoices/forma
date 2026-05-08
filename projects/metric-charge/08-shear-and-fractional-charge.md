# Chapter 8 — Shear and fractional charge

This chapter turns on the off-diagonal shear σ_uw and examines what it adds to the framework. So far the framework has worked with the bare diagonal metric (σ_uw = 0); this chapter introduces shear as a parameter and traces its consequences through the inventory.

The chapter has two main payloads. First, it quantifies the chirality-bias result from [Chapter 6 §6](06-handedness-and-pairs.md) — σ_uw breaks the (m, n) ↔ (m, −n) symmetry but preserves (m, n) ↔ (−m, −n) — computing the explicit mass split between chirality partners under shear. Second, it examines the **fractional-charge optimization**: closure-satisfying multi-component links of the form k × T(1, q) (per [Chapter 4 §4.3](04-the-closure-condition.md), where the synchronization rule restricts multi-links to those with T(1, q) primitives) carry 1/k of their primitive's charge per component; the chapter computes which k is energetically favored under shear and reports the result honestly. If k = 3 emerges, the framework matches the structural pattern that MaSt model-F associates with standard physics' quark inventory.

**Inheritance.**

- *From [Chapter 1 §4](01-foundation.md):* the σ_uw shear definition and its deferred status; the metric form with shear active.
- *From [Chapter 6 §6](06-handedness-and-pairs.md):* the chirality-bias result. σ_uw breaks (m, n) ↔ (m, −n) at the dispersion level; this chapter quantifies that bias.
- *From [Chapter 7 §6](07-aspect-ratio-and-character.md):* the finding that ε alone does not select multi-component-link character; chapter 8 examines whether σ_uw provides the missing mechanism.
- *From [metric-mass Chapter 7](../metric-mass/07-shear-and-bias.md):* the 1D-compact shear-bias analysis. **Note:** metric-mass's σ_Su shear is structurally distinct from metric-charge's σ_uw. The two shears couple different wavenumber pairs and break different symmetries. Chapter 6 §6.4 works through the comparison.

**Distinctive job.** Quantify σ_uw's chirality bias on the (m, n) inventory, and derive the framework's prediction for the energetically favored multi-component link structure under shear (the optimal k, and what fractional charge it produces).

The framework treats both as **emergent results** of the framework's own machinery. Standard physics' three-phase quark organization is a reference target to compare against, not an input. Matter/antimatter asymmetry is *not* derived from σ_uw — see [§3](#3-chirality-bias-from-shear) and [Chapter 6 §6.7](06-handedness-and-pairs.md) for the open question.

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

Several structural observations follow directly from the bilinearity of the cross-term in (k_u, k_w):

- **The cross-term −2σ k_u k_w is invariant under (m, n) ↔ (−m, −n)** (joint sign flip of both windings, which leaves the product k_u·k_w unchanged). The (1, 1) and (−1, −1) modes have *identical* dispersion under shear.
- **The cross-term flips sign under (m, n) ↔ (m, −n)** (chirality reflection — flipping only one winding). The (1, 1) and (1, −1) modes acquire *different* masses under shear: m²_(1, 1) ∝ 2K²(1−σ) and m²_(1, −1) ∝ 2K²(1+σ) with K = 2π/L (taking L_u = L_w = L for illustration).
- **σ_uw is therefore a chirality-bias mechanism, not a sign-bias mechanism.** This is structurally distinct from [metric-mass Chapter 7 §6](../metric-mass/07-shear-and-bias.md)'s σ_Su shear, whose cross-term k_S·k_u flips sign under (n) → (−n) and so breaks the sign-reflection symmetry. The two shears couple different wavenumber pairs and break different symmetries; σ_uw is *not* the 2D-compact extension of metric-mass's σ_Su.
- Mode crossings: at specific σ values the order of (1, 1) vs (1, −1) — chirality partners — reorganizes, but the (1, 1) and (−1, −1) ordering is preserved. The σ-induced reorganization acts on the chirality axis only.

The full symmetry analysis and its consequences are worked through in [Chapter 6 §6](06-handedness-and-pairs.md), which also surfaces a fourth structural neutrality mechanism (chirality-conjugate cancellation pairs) that follows from the same math.

### 3. Chirality bias from shear

Per [Chapter 6 §6](06-handedness-and-pairs.md), the σ_uw cross-term in the dispersion breaks the (m, n) ↔ (m, −n) **chirality** reflection while preserving the (m, n) ↔ (−m, −n) **sign** reflection. The framework's σ_uw shear therefore provides a chirality-bias mechanism, not a matter/antimatter-bias mechanism. This section quantifies the chirality bias and notes its consequences.

**Mass split between chirality partners.** From the dispersion of §2, with k_u = K_u and k_w = K_w (positive magnitudes), the mass-squared values for the four sign combinations are:

| Mode | k_u·k_w | m² (proportional) |
|---|---|---|
| (m, n) and (−m, −n) | +K_u K_w | (K_u² − 2σ K_u K_w + K_w²)/(1−σ²) |
| (m, −n) and (−m, n) | −K_u K_w | (K_u² + 2σ K_u K_w + K_w²)/(1−σ²) |

The two **sign-reflection partners** ((m, n) and (−m, −n)) sit at the same mass; the two **chirality-reflection partners** ((m, n) and (m, −n)) sit at masses that differ by an amount proportional to σ. For small σ, the leading split is

<!-- Δm²/m² ≈ 4σ K_u K_w / (K_u² + K_w²) -->
$$
\frac{\Delta m^2}{m^2_{\sigma = 0}} \;\approx\; \frac{4\sigma\,K_u K_w}{K_u^2 + K_w^2} \;+\; \mathcal{O}(\sigma^2)
$$

(The exact value also acquires σ²-corrections from the (1−σ²) denominator, which we set aside at the linearized level.)

**(k_S, m, n) → (−k_S, −m, −n) symmetry of the full dispersion is exact.** Adding spatial momentum k_S does not change the analysis: k_S² is invariant under any of the sign-flip operations considered, and there is no σ-dependent cross-term involving k_S in the sheared dispersion of §2 (the framework introduces only σ_uw, not σ_Su or σ_Sw). The full sign flip is therefore exactly preserved.

**What the chirality bias means dynamically.** Under thermal equilibrium with σ ≠ 0, the populations of (m, n) and (m, −n) are unequal — mass-Boltzmann-suppressed by the Δm² above. A configuration prepared with equal amplitudes of the two chirality components is not in thermal equilibrium and would tend to redistribute toward the lower-energy chirality unless prevented by another conservation law. This is the dynamical chirality bias σ_uw produces.

**What it does not do.** The framework's σ_uw shear does *not* provide a Sakharov-CP-violation analog in the matter/antimatter sense. Standard-physics Sakharov requires both C and P violation; σ_uw provides P-flavor (chirality) bias only. The C-flavor (sign-reflection) side has no derived mechanism in this chapter or [Chapter 6](06-handedness-and-pairs.md). Earlier framings of this chapter and Chapter 6 conflated the two and presented σ_uw as a Sakharov-CP analog; the math shows this is incorrect — the two shears (metric-mass's σ_Su and metric-charge's σ_uw) break different symmetries.

**Open: matter/antimatter bias.** Whether the framework derives a matter/antimatter bias from any mechanism is left open. Candidate locations the framework's broader stack might supply such a mechanism are summarized in [Chapter 6 §6.7](06-handedness-and-pairs.md): a different shear (σ_Su or σ_Sw, not currently in the metric), substrate-level chirality from grid-primitive/grid-duality, or a structural mechanism not yet identified. None of these is committed to here; the math is honest about what σ_uw alone can and cannot do.

### 4. The closure condition under shear

Does the closure condition itself change under σ ≠ 0?

The phase-pattern view of [Chapter 1 §10](01-foundation.md): "2π winding on w + standing wave on both u and w." This is stated in the bare-metric basis. Under shear, the natural "windings on u" and "windings on w" become entangled through the sheared lattice — a single closed traversal in the sheared-coordinate basis advances by mixed amounts in (u, w) directions.

Two ways to interpret:

- **Conservative:** the closure condition in the bare basis is unchanged; the wave equation's modes adjust their behavior under shear. (m, n) labels remain meaningful.
- **Sheared-basis:** the closure condition is naturally stated in the sheared basis, where the relevant labels are mass-eigenvalue pairs (m̃, ñ) related to (m, n) by σ-dependent linear combinations.

The chapter takes the conservative interpretation: closure operates on (m, n) labels in the bare basis; shear is a perturbation that affects masses and dispersion but not the closure condition itself. This is consistent with closure being a phase-pattern statement that doesn't depend on which basis is used to describe the wave.

### 5. Multi-component links under shear — energetics

Take a closure-satisfying multi-component link of the form T(k, k·q) = k × T(1, q), with k ≥ 2 and q ≥ 1. (Per the synchronization rule of [Chapter 4](04-the-closure-condition.md), only multi-links with T(1, q) primitives satisfy closure; multi-links with genuine-torus-knot primitives fail synchronization and are mass-only.) Under shear, the energetics of the k phased components changes:

- Each component is a phase-shifted copy of the primitive T(1, q).
- Phase-shifts within the (u, w) cycle interact with the shear cross-term −2σ k_u k_w in mode-dependent ways.
- The total energy of the k-component configuration depends on the *relative phases* of the components.

Specifically: if the k components are at phases 2π·j/k for j = 0, 1, ..., k−1, the total energy summed over components contains cross-terms between different j values. The cross-terms are sensitive to σ and to the specific phase distribution.

The chapter computes this sum and asks: at what k is the k × T(1, q) multi-link configuration most energetically favorable under shear?

### 6. Optimizing k under shear — what value emerges?

This is the chapter's central derivation, framed as a real optimization rather than a proof of a presupposed answer.

Set up the optimization problem: given fixed (σ, ε), what value of k minimizes the total energy of a k × T(1, q) multi-link configuration? (The synchronization rule restricts multi-links to those with T(1, q) primitives — these are the only closure-satisfying multi-link configurations.) Compute E(k; σ, ε, q), minimize over k for the lightest q (q = 1 at most ε), and report what optimal k(σ, ε) emerges.

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

### 7.4 What is and is not yet proven about fractional charge

Three distinct claims about fractional charge sit in this chapter; it is worth separating what the framework derives from what it leaves open.

**Proven (structurally):**

- *Fractional-charge configurations exist as closure-satisfying states.* Multi-component links of the form k × T(1, q) satisfy synchronization (Chapter 4 §4.3); each component carries 1/k of the link's integer total charge as a structural fact of the multi-link decomposition (this section, §7.1–§7.3). The 1/k per component is not a separate physical postulate — it falls out of the link's geometry plus integer total quantization.
- *Components are not closure-satisfying alone.* A single (1, q) primitive at a phase position within a k × T(1, q) link does not satisfy the synchronization rule on its own (Chapter 4 §4.3). Only the collective configuration with all k components in proper phase distribution closes.

**Not proven — and forwarded to [metric-binding](../metric-binding/):**

- *Whether fractional-charge states are stable in time.* The structural prediction is that components cannot exist in isolation as closure-satisfying configurations — this is consistent with confinement-like behavior. But "cannot exist in isolation as closure-satisfying" is weaker than "cannot exist in isolation at all": a component without closure would be a mass-only mode (single-axis or non-synchronizing diagonal), which is a permitted state in the framework, just not a charged one. Whether the energetic cost of separating one component from a multi-link is finite-but-large (giving long-lived but separable states) or genuinely infinite-in-the-limit (true confinement) requires an explicit energetics calculation across the separation.
- *The energy cost of separation as a function of distance.* For two parts of a multi-link pulled apart in (S₁, S₂), what does E(separation) look like? Standard-physics' quark confinement comes from a linear potential at large distances (string tension); whether the framework reproduces that, or some other functional form, is a multi-knot-energetics calculation.
- *Whether fractional-charge components can be created/destroyed independently.* Linear theory (this project) conserves (m, n) labels exactly; pair creation/annihilation is a nonlinear/quantum phenomenon outside scope here.

**Where the stability question lives.** The "is fractional charge stable / can it be observed in isolation?" question is fundamentally a *multi-knot energetics* question — it requires comparing the energy of a multi-link configuration to the energy of its separated components as a function of separation. That calculation is the subject of [metric-binding](../metric-binding/), which is the follow-up project specifically focused on multi-knot configurations and binding energetics. metric-binding's chapters on binding/unbinding energetics are where the quark-stability question gets resolved within the framework.

This chapter's claim is therefore: **fractional charge structurally exists** (as the per-component association inside closure-satisfying multi-links) **and structurally requires the collective configuration** (since components alone fail closure), **but the question of dynamical stability — whether components can be ripped apart, with what energy cost, and at what timescales — is forwarded to metric-binding.**

### 8. Summary — what shear adds to the inventory

The ε sweep of [Chapter 7](07-aspect-ratio-and-character.md) gave three regimes of sheet character (mass-only-dominated at extremes, charge-friendly at ε ≈ 1). Adding shear σ_uw to that inventory:

- **Breaks (m, n) ↔ (m, −n) chirality symmetry** (per §3 derivation; preserves (m, n) ↔ (−m, −n) sign reflection). σ_uw provides chirality bias only; matter/antimatter bias is not derived here.
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
- **Does not derive a matter/antimatter bias mechanism.** §3 shows σ_uw cannot do it (σ_uw breaks chirality, not sign reflection). What σ_uw provides is a chirality bias only — at most a P-flavor ingredient toward a Sakharov-CP construction; the C-flavor side is not derived. Forwarded to [Chapter 6 §6.7](06-handedness-and-pairs.md) for candidate alternatives.
- **Does not derive nonlinear shear effects.** Linear theory only. Whether large σ produces qualitatively different behavior (beyond the linear approximation breaking down) is downstream work.
- **Does not analyze interaction between distinct three-component links.** Multi-knot energetics is metric-binding territory.
- **Does not derive the dynamical stability of fractional-charge components.** §7.4 establishes that components are *structurally* non-isolable (they are not closure-satisfying alone), but the *energetics* of separating components — whether the energy cost grows linearly with distance (true confinement), saturates at finite value (separable but bound), or some other functional form — is a multi-knot energetics calculation forwarded to [metric-binding](../metric-binding/).
- **Does not explain why σ_uw takes a specific value** on any given sheet. ε and σ are both treated as free parameters; whether they are dynamically determined is open.
- **Does not commit to MaSt-correspondence assignments.** The fractional-charge / three-phase prediction matches the structural pattern of standard physics' quarks; specific identifications (which (m, n) corresponds to which quark family, etc.) are downstream work.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Are fractional-charge components dynamically stable, or only structurally non-isolable? What is E(separation) for pulling one component out of a k × T(1, q) multi-link? | [metric-binding](../metric-binding/) — multi-knot energetics. The framework structurally predicts components are not closure-satisfying alone (per §7.4), but the energetics of separation (string-tension-like vs finite barrier) is a multi-knot calculation. |
| Does the k = 3 selection follow from the local shear-cross-term structure alone, or does it require global topology (Z₃ from grid-duality) as an input? | Open; possibly resolved by grid-duality's substrate analysis |
| Does the σ_uw chirality bias quantitatively match observed P-violation magnitudes (e.g., parity-violation in weak interactions)? | Downstream MaSt-correspondence work + experimental data |
| Does the framework derive a matter/antimatter bias from any mechanism? §3 shows σ_uw cannot. Candidates: σ_Su or σ_Sw (different shear, not in current metric); substrate-level chirality from grid-primitive/grid-duality; other unidentified mechanisms. | Project-direction question (see [Chapter 6 §6.7](06-handedness-and-pairs.md)) |
| Are there other multi-component links (k = 5, k = 7, ...) energetically favored at specific σ values, corresponding to potential exotic states? | Open follow-up; downstream investigation |
| Does the framework predict any deviation from standard quark mass / charge ratios that could be experimentally tested? | Open; depends on quantitative completion of the framework |
| If observed CP-violation has a chirality (P-flavor) component, can σ_uw's chirality bias quantitatively match its magnitude? (The framework does not derive the C-flavor component from σ_uw.) | Downstream MaSt-correspondence work |
| Does the choice of which compact direction is "tube" (closure-asymmetric) vs "ring" force a specific sign convention on σ_uw, or is the sign free? | Convention question; possibly settled by combination of Chapters 3 §3.2 and 5 §6.3 |
| At very large σ (approaching the |σ| < 1 boundary where the metric becomes degenerate), does the framework predict any structural transitions or singular behavior? | Out of scope; possibly relevant for nonlinear extensions |
