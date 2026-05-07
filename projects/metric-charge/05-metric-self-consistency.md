# Chapter 5 — Metric self-consistency and gauge promotion

**Status:** Sparse outline. Each section is one to three sentences describing the derivation step that section will perform. To be expanded into full prose once the outline is approved.

This chapter takes the closure-satisfying modes identified in [Chapter 4](04-the-closure-condition.md) and asks the **metric-side** question: under linearized Einstein equations, what off-diagonal metric entries do these modes source, and do those entries have the structure that standard physics calls a *gauge potential*?

The chapter's job is structurally parallel to [metric-mass Chapter 5](../metric-mass/05-metric-self-consistency.md), but on a 2D-compact substrate where the off-diagonal sourcing has more places to go. metric-mass found that a 1D-compact mass mode sources g_tu under linearized Einstein equations; the 2D-compact extension produces a richer set of off-diagonals (g_tu, g_S₁u, g_S₂u, g_tw, g_S₁w, g_S₂w), and the question of whether these collectively form a "gauge potential" — in the sense standard physics uses the term — becomes substantive.

**Framing convention.** Standard Model terminology (gauge potential, U(1) × U(1) symmetry, Maxwell's equations) is used in this chapter as a **reference target** — a structure the framework's derivations may or may not reproduce. We do not adopt the Standard Model as axiomatic. The questions are:

- Do the off-diagonal entries our closure-satisfying modes source have the algebraic and geometric properties standard physics uses to define a gauge potential?
- If yes, the framework *reproduces* the standard gauge structure — emergent, not postulated.
- If partially, the framework *predicts* deviations from standard EM that may or may not match observation.
- If no, the framework's "charge" concept is structurally different from standard EM and the correspondence breaks down.

This is the discovery-not-proof philosophy of [metric-charge](README.md) applied to the gauge structure: let the math reveal what emerges, with standard physics as the comparison target rather than the starting point.

**Inheritance.**

- *From [metric-mass Chapter 5](../metric-mass/05-metric-self-consistency.md):* the 1D-compact stress-energy and off-diagonal sourcing analysis. The 2D-compact extension follows the same machinery with one more index.
- *From [Chapter 4](04-the-closure-condition.md):* the closure-satisfying inventory and the centered-alignment phase requirement.
- *From [grid-duality §7.5–§8](../grid-duality/07-wrap-promotion-modeling.md):* the topological U(1) × U(1) cross-coupling structure at L3, which is what we want to see emerge from the metric-side analysis.

**Distinctive job.** Demonstrate (or refute) the equivalence of the three views from [Chapter 1 §10](01-foundation.md): phase-pattern, topological, and metric-side. Provide the calculable mechanism for gravitational and EM bending flagged in [metric-mass Chapter 6 §4](../metric-mass/06-gravitational-bending.md) and forward-referenced in [Chapter 1 §10](01-foundation.md). Make the standard-EM correspondence a consequence rather than an assumption.

---

## Bare outline

### 1. The chapter's job

Take the closure-satisfying inventory from [Chapter 4 §6](04-the-closure-condition.md). For each mode class, compute T_μν, identify the off-diagonal entries it sources via linearized Einstein equations, and examine whether the resulting metric perturbation has the algebraic structure standard physics ascribes to a gauge potential.

Three questions guide the chapter:

1. What off-diagonal entries does each closure-satisfying mode source?
2. Do those entries have the structure of A_μ and B_μ in the standard-physics sense?
3. How do closure-failing modes (single-axis, zero-mode) behave in the same analysis — do their off-diagonals fail to satisfy gauge structure, confirming the L2-in-L3 framing?

### 2. Stress-energy of a 2D-compact mode

For a mode φ ∝ exp(−iωt) U(u) W(w) at fixed (m, n), compute T_μν. Cite [metric-mass Chapter 5 §2](../metric-mass/05-metric-self-consistency.md) for the 1D-compact case; the 2D extension is mechanical but produces more off-diagonals.

The relevant entries:

- **Diagonal:** T_tt, T_S₁S₁, T_S₂S₂, T_uu, T_ww (energy density and pressures).
- **Spacetime ↔ compact off-diagonals:** T_tu, T_tw, T_S₁u, T_S₁w, T_S₂u, T_S₂w. These are the entries that source the off-diagonal metric perturbations of interest in §3.
- **Compact ↔ compact:** T_uw. Distinct from the spacetime-compact off-diagonals; flagged here as it appears for diagonal (m, n) modes and may interact with the σ_uw shear of chapter 8.

The pattern of which entries are nonzero depends on the mode class:

| Mode class | T_μν off-diagonals nonzero |
|---|---|
| Light (0, 0) | None (no compact-direction structure) |
| Single-axis (m, 0) | T_tu, T_S₁u, T_S₂u only (u-set) |
| Single-axis (0, n) | T_tw, T_S₁w, T_S₂w only (w-set) |
| Diagonal (m, n) both nonzero | Both u-set and w-set; possibly T_uw |

Already at the T_μν level, the structural distinction emerges: closure-satisfying (diagonal) modes source *both* off-diagonal sets simultaneously, while closure-failing (single-axis) modes source only one.

### 3. Off-diagonal sourcing under linearized Einstein equations

For each nonzero T_μν entry, the linearized Einstein equation sources a corresponding metric perturbation h_μν. Cite [metric-mass Chapter 5 §5](../metric-mass/05-metric-self-consistency.md) for the linearized-EE machinery.

The sourcing pattern:

- T_tu → h_tu (the 1D-compact case from metric-mass).
- T_S₁u → h_S₁u, T_S₂u → h_S₂u.
- T_tw → h_tw, T_S₁w → h_S₁w, T_S₂w → h_S₂w.
- T_uw → h_uw (cross-compact perturbation; distinct from σ_uw shear of [Chapter 1 §4](01-foundation.md)).

For diagonal (m, n) modes, all six spacetime↔compact off-diagonals are sourced — three for u, three for w. For single-axis modes, only one set (three entries) is sourced.

### 4. Do the off-diagonals form a gauge potential?

This is the chapter's central question. We examine whether the six-entry off-diagonal pattern h_μu, h_μw (where μ ∈ {t, S₁, S₂}) has the structural properties standard physics ascribes to a gauge potential A_μ.

Standard-physics properties of a gauge potential (used as reference target, not axiom):

- **Index structure:** A_μ is a 4-vector field on spacetime. Our h_μu transforms as a spacetime vector (under a spacetime-only coordinate change) once u is treated as a compact-direction label. Same for h_μw.
- **Gauge transformation:** under change of coordinates that mixes spacetime with the compact direction, A_μ shifts by a gradient: A_μ → A_μ + ∂_μ Λ. Our h_μu has the analogous transformation under (u → u + Λ) shifts.
- **Field strength:** F_μν = ∂_μ A_ν − ∂_ν A_μ should follow from h_μu by the same construction.
- **Coupling to charged matter:** A_μ couples to charges via the geodesic equation's Lorentz-force term. This should emerge from the off-diagonal h_μu in the geodesic on the perturbed metric.

For closure-satisfying modes, the chapter shows:

- The h_μu set does form a gauge potential A_μ in the structural sense above. The KK identification A_μ = h_μu / (some normalization) is what makes this work.
- The h_μw set forms a *second* gauge potential B_μ — a U(1) × U(1) structure consistent with [grid-duality §7.5.3](../grid-duality/07-wrap-promotion-modeling.md).
- Whether both U(1)s are physical or only one is a convention question — see §6.

### 5. Closure-failing modes do not form valid gauge potentials

For single-axis modes (m, 0) or (0, n), only one set of off-diagonals is sourced. The other set is identically zero.

Under standard-physics gauge-potential structure, having only h_μu (and zero h_μw) does not by itself fail any of the property tests — the h_μu set on its own can still be a single U(1) gauge potential.

But the closure condition specifically requires *both* directions to be active simultaneously. Single-axis modes have a structural deficiency: they source what *would* be a gauge potential in one direction, but they don't have the second one.

The interpretation: single-axis modes carry a partial gauge structure that doesn't couple into observable EM in 4D. The U(1) × U(1) cross-coupling that [grid-duality §8.2](../grid-duality/08-where-alpha-appears.md) shows is required for α-mediated EM is absent.

This is the metric-side confirmation of the L2-in-L3 framing: single-axis modes have mass (energy density T_tt, T_uu source diagonal metric perturbations and gravitational mass) but no observable EM (the gauge structure is incomplete). The structural property here — massive states without EM coupling — is what standard physics ascribes to neutrinos; whether single-axis modes correspond to standard-physics neutrinos is a downstream MaSt-correspondence question.

### 6. The three views are mutually consistent

Show that [Chapter 1 §10](01-foundation.md)'s three views agree on which (m, n) modes carry observable charge:

- **Phase-pattern view** (Chapter 4): closure-satisfied at centered alignment for diagonal modes.
- **Topological view** (grid-duality): both windings nonzero, U(1) × U(1) cross-coupling active.
- **Metric-side view** (this chapter): both h_μu and h_μw sourced, forming a valid gauge-potential pattern.

The three classifications produce the same partition of modes into charged vs neutral. This consistency is a structural cross-check that the closure condition is well-defined across multiple framings.

The cross-check also exposes the symmetry-breaking conventions noted in [Chapter 3 §3.2](03-knots-on-the-torus.md):

- The closure rule's preference for w-winding (phase-pattern view) is the same convention as the gauge-coupling preference for one of the two U(1)s (metric-side view) and as grid-duality's tube/ring asymmetry (topological view).
- Whether to read these as one convention adopted three times, or as three independent conventions that happen to align, is a chapter-deep question. Probably one convention with three faces.

### 7. The holonomy mechanism for bending

Drawing the chapter's results together, the **calculable mechanism** for how mass mechanically bends spacetime and how charged matter creates EM fields:

1. Closure-satisfying mode sources off-diagonal h_μu, h_μw.
2. h_μu and h_μw are the gauge potentials A_μ, B_μ.
3. A passing wave's worldline through the perturbed metric picks up phase via ∮ A_μ dx^μ (and similarly for B_μ).
4. That phase manifests as gravitational lensing + Shapiro delay (gravity case) or refractive-index slowdown (EM case).

This is the mechanism flagged in [metric-mass Chapter 6 §4](../metric-mass/06-gravitational-bending.md). On the 2D-compact substrate, both gravitational and EM versions emerge from the same off-diagonal-sourcing chain — the difference is only which specific off-diagonal entries dominate the holonomy in a given regime.

For closure-failing modes (single-axis): the holonomy mechanism still operates for the diagonal-metric perturbations (gravitational lensing from energy density), but not for the gauge-potential channel. Single-axis modes bend light gravitationally but produce no EM holonomy. Consistent with the structural property of mass without EM coupling — what standard physics ascribes to neutrinos.

### 8. What the framework reproduces and where it might differ

Compare what emerges from §§2–7 against the standard-physics gauge structure:

- Reproduces: U(1) × U(1) gauge symmetry at the linearized level.
- Reproduces: gauge-potential transformation properties.
- Reproduces: the holonomy structure of EM coupling to charged matter.
- Reproduces: the structural neutrality of mass-only modes (the property standard physics ascribes to neutrinos).

Where the framework might differ:

- The two U(1)s are intrinsically symmetric (by the bare topology) and the asymmetry that selects one as "physical EM" comes from the conventions of [Chapter 3 §3.2](03-knots-on-the-torus.md) rather than from an a priori principle. Standard physics treats the choice of EM gauge as observed; the framework treats it as conventional.
- The framework predicts a *second* gauge potential B_μ that may or may not have a Standard Model counterpart. Whether B_μ corresponds to a known force (e.g., the analog of magnetic-charge / Hodge-dual of EM, per grid-duality §7.5.3) or to something not yet identified is open.
- The α coupling strength is not derived here; it is the structural quantity grid-duality §8 forwards to grid alpha-derivation work.

The framework reproduces standard EM at the structural level. Whether it reproduces standard EM *quantitatively* depends on the α derivation downstream.

### 9. What's next

[Chapter 6 — Handedness and pairs](06-handedness-and-pairs.md). Take the closure-satisfying inventory from chapter 4 and the gauge-potential structure from this chapter, and examine the **chirality / handedness** structure: when do (m, n) and (−m, −n) correspond to physically distinguishable particles (matter vs antimatter), and when do they represent the same particle viewed two different ways? Examine when complementary pairs *within a single field configuration* cancel net charge (apparent neutrality through internal cancellation, distinct from the structural neutrality of single-axis modes from this chapter).

---

## What this chapter does **not** do

- **Does not postulate gauge symmetry.** The Standard Model gauge structure appears as a target the chapter examines, not an input.
- **Does not derive numerical α.** Cited from [grid-duality §8](../grid-duality/08-where-alpha-appears.md); structural location is settled there, numerical value is grid alpha-derivation work.
- **Does not derive Maxwell's equations.** Standard EM is a reference target. Whether Maxwell's equations follow from the off-diagonal sourcing in some appropriate limit is downstream work.
- **Does not assign handedness or matter/antimatter.** Chapter 6.
- **Does not commit to whether B_μ is a known Standard Model force or new physics.** Open question forwarded to grid alpha-derivation and downstream MaSt-correspondence work.
- **Does not analyze nonlinear backreaction.** Linearized Einstein equations only; nonlinear self-consistency is deferred (per [Chapter 1 §11](01-foundation.md)).
- **Does not analyze multi-knot energetics.** metric-binding territory.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Are the two U(1) gauge potentials (A_μ from h_μu, B_μ from h_μw) both physical, or is only one observed? | Convention question; possibly settled by grid alpha-derivation |
| Does B_μ correspond to a known force (Hodge-dual of EM, magnetic charge, etc.) or to new physics? | Downstream grid + MaSt-correspondence work |
| Does the holonomy mechanism (§7) reproduce standard gravitational lensing predictions quantitatively? | Cross-check with metric-mass Chapter 6 + standard GR |
| Why are the closure-rule, aspect-ratio, and gauge conventions all aligned (one convention, three faces)? | Structural question; possibly forced by deeper symmetry |
| Does the framework's prediction of a U(1) × U(1) gauge structure quantitatively match standard EM at every order, or only at linearized order? | Nonlinear backreaction work, deferred |
| Does T_uw (cross-compact stress-energy) interact with σ_uw shear in chapter 8 in a structurally meaningful way? | Chapter 8 |
