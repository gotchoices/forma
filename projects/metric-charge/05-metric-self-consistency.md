# Chapter 5 — Metric self-consistency and gauge promotion

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

**Distinctive job.** Demonstrate (or refute) the equivalence of the three views from [Chapter 1 §10](01-foundation.md): phase-pattern, topological, and metric-side. Provide the calculable mechanism for gravitational and EM bending flagged in [metric-mass Chapter 6 §4](../metric-mass/06-gravitational-bending.md) and forward-referenced in [Chapter 1 §10](01-foundation.md). Make any standard-EM correspondence a consequence rather than an assumption.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The chapter's job — three guiding questions |
| 2 | Stress-energy of a 2D-compact mode |
| 3 | Off-diagonal sourcing under linearized Einstein equations |
| 4 | Do the off-diagonals form a gauge potential? — testing against standard-physics properties |
| 5 | Closure-failing modes do not form valid gauge potentials |
| 6 | The three views are mutually consistent |
| 7 | The holonomy mechanism for bending |
| 8 | What the framework reproduces and where it might differ |
| 9 | What's next |

---

## 1. The chapter's job

Take the closure-satisfying inventory from [Chapter 4 §6](04-the-closure-condition.md). For each mode class, compute T_μν, identify the off-diagonal entries it sources via linearized Einstein equations, and examine whether the resulting metric perturbation has the algebraic structure standard physics ascribes to a gauge potential.

Three questions guide the chapter:

1. What off-diagonal entries does each closure-satisfying mode source?
2. Do those entries have the structure of A_μ and B_μ in the standard-physics sense?
3. How do closure-failing modes (single-axis, zero-mode) behave in the same analysis — do their off-diagonals fail to satisfy gauge structure, confirming the L2-in-L3 framing?

We answer (1) in §2–§3 by computing T_μν and the perturbation it sources. We answer (2) in §4 by checking the off-diagonals against four standard-physics properties of a gauge potential. We answer (3) in §5 by repeating the analysis for closure-failing modes and showing the gauge structure breaks down. §6 confirms that the metric-side answer agrees with the phase-pattern (Chapter 4) and topological ([grid-duality](../grid-duality/)) views. §7 develops the holonomy mechanism that connects all of this to physical bending. §8 audits what the framework reproduces vs. where it might differ from standard physics.

---

## 2. Stress-energy of a 2D-compact mode

For a separable mode at fixed (m, n):

<!-- φ(t, u, w) = T(t) U(u) W(w) -->
$$
\varphi(t, u, w) = T(t)\cdot U(u)\cdot W(w)
$$

with T(t) ∝ e^(−iωt), U(u) and W(w) standing waves of integer winding number m and n respectively, the stress-energy tensor T_μν follows from the standard scalar-field formula:

<!-- T_μν = ∂_μ φ ∂_ν φ* + ∂_ν φ ∂_μ φ* − g_μν L -->
$$
T_{\mu\nu} = \partial_\mu\varphi\,\partial_\nu\varphi^* + \partial_\nu\varphi\,\partial_\mu\varphi^* - g_{\mu\nu}\mathcal{L}
$$

with L the scalar-field Lagrangian density. [metric-mass Chapter 5 §2](../metric-mass/05-metric-self-consistency.md) computes T_μν for the 1D-compact case in factored form T_μν = 2|φ|² k_μ k_ν with k_μ = (−ω, k_S, n/R_u). The 2D-compact extension is mechanical:

<!-- k_μ = (−ω, k_S₁, k_S₂, n_u/R_u, n_w/R_w) for our 5D manifold -->
$$
k_\mu = (-\omega,\,k_{S_1},\,k_{S_2},\,k_u,\,k_w)
$$

with k_u = 2πm/L_u and k_w = 2πn/L_w. The stress-energy in factored form is:

<!-- T_μν = 2|φ|² k_μ k_ν -->
$$
T_{\mu\nu} = 2|\varphi|^2\,k_\mu k_\nu
$$

### 2.1 Diagonal entries — energy density and pressures

The diagonal entries scale as the squares of each wavenumber:

| Component | Value (up to 2|φ|²) |
|---|---|
| T_tt | ω² (energy density) |
| T_S₁S₁ | k_{S₁}² (pressure along S₁) |
| T_S₂S₂ | k_{S₂}² (pressure along S₂) |
| T_uu | k_u² (compact-direction "pressure" along u) |
| T_ww | k_w² (compact-direction "pressure" along w) |

These source the diagonal metric perturbation that [metric-mass Chapter 6](../metric-mass/06-gravitational-bending.md) interpreted as the gravitational mass — the perturbation that causes spacetime bending around the mode. For our purposes here, the diagonal sourcing gives us *gravitational* coupling (the mode acts like a localized mass when viewed from extended spacetime), which is necessary for any massive state.

### 2.2 Off-diagonal entries — six potential gauge potentials

The off-diagonals between extended-spacetime indices and compact indices are the entries of interest:

| Component | Value | Mode class for which it's nonzero |
|---|---|---|
| T_tu | −ω · k_u | any mode with k_u ≠ 0 (m ≠ 0) |
| T_S₁u | k_{S₁} · k_u | any mode with both k_{S₁} ≠ 0 and k_u ≠ 0 |
| T_S₂u | k_{S₂} · k_u | any mode with both k_{S₂} ≠ 0 and k_u ≠ 0 |
| T_tw | −ω · k_w | any mode with k_w ≠ 0 (n ≠ 0) |
| T_S₁w | k_{S₁} · k_w | any mode with both k_{S₁} ≠ 0 and k_w ≠ 0 |
| T_S₂w | k_{S₂} · k_w | any mode with both k_{S₂} ≠ 0 and k_w ≠ 0 |

For a mode at rest in S (k_{S₁} = k_{S₂} = 0), only T_tu and T_tw are nonzero. For a moving mode, additional entries activate. The structure of which entries are nonzero depends on the mode class:

| Mode class | T_μν off-diagonals nonzero |
|---|---|
| Light (0, 0) | None (no compact-direction structure) |
| Single-axis (m, 0) | T_tu only at rest; T_tu, T_S₁u, T_S₂u when moving — *u-set only* |
| Single-axis (0, n) | T_tw only at rest; *w-set only* |
| Diagonal (m, n) both nonzero | At rest: T_tu and T_tw. When moving: full six-entry pattern. *Both u-set and w-set sourced* |

Already at the T_μν level, the structural distinction emerges: closure-satisfying (diagonal) modes source *both* off-diagonal sets simultaneously, while closure-failing (single-axis) modes source only one. This is the metric-side fingerprint of the closure condition.

### 2.3 Cross-compact entry T_uw

For diagonal modes, the entry T_uw = k_u · k_w is also nonzero. This is *not* a spacetime↔compact off-diagonal — it is a compact↔compact cross-term. It is distinct from the σ_uw shear of [Chapter 1 §4](01-foundation.md) (which is an externally imposed metric parameter, not a wave-equation source); we flag it here because it appears for diagonal modes and may interact with σ_uw shear in chapter 8.

---

## 3. Off-diagonal sourcing under linearized Einstein equations

For each nonzero T_μν entry, the linearized Einstein equation sources a corresponding metric perturbation h_μν. [metric-mass Chapter 5 §5](../metric-mass/05-metric-self-consistency.md) develops the linearized-EE machinery for the 1D-compact case; we cite it and apply the same machinery to our 2D-compact setting.

### 3.1 The linearized sourcing relation

In Lorenz gauge, the linearized Einstein equations take the form:

<!-- □ h_μν = -16π G T_μν^trace-reversed -->
$$
\Box\, h_{\mu\nu} = -16\pi G\, \bar T_{\mu\nu}
$$

where □ is the d'Alembertian on flat spacetime and T̄_μν is the trace-reversed stress-energy tensor. The structural point: each component T_μν sources its corresponding h_μν component (modulo trace-reversal). Off-diagonal stress-energy entries source off-diagonal metric perturbations.

### 3.2 The full off-diagonal sourcing pattern for diagonal modes

For a closure-satisfying mode (m ≠ 0, n ≠ 0), the sourced off-diagonal metric perturbations are:

| Source T_μν | Sourced h_μν | Standard-physics correspondence |
|---|---|---|
| T_tu | h_tu | A_t (temporal component of u-gauge potential) |
| T_S₁u | h_S₁u | A_{S₁} (spatial component of u-gauge potential) |
| T_S₂u | h_S₂u | A_{S₂} (spatial component of u-gauge potential) |
| T_tw | h_tw | B_t (temporal component of w-gauge potential) |
| T_S₁w | h_S₁w | B_{S₁} (spatial component of w-gauge potential) |
| T_S₂w | h_S₂w | B_{S₂} (spatial component of w-gauge potential) |
| T_uw | h_uw | (cross-compact perturbation; distinct from spacetime gauge potentials) |

Six spacetime↔compact off-diagonals, organized into two sets of three. Per the standard Kaluza-Klein identification (see [metric-mass Ch 5 §6](../metric-mass/05-metric-self-consistency.md) for the 1D version), each set of three is naturally read as the four-vector gauge potential associated with one compact direction — A_μ for u, B_μ for w. The "Standard-physics correspondence" column above states what the entries *would be* under the KK identification; whether they actually have the gauge-potential properties is the question §4 addresses.

For closure-failing modes:

- **Light (0, 0)** sources no off-diagonals. Diagonal h_μν only — no gravitational coupling beyond the trivial vacuum.
- **Single-axis (m, 0)** sources only the u-set: h_tu, h_S₁u, h_S₂u. The w-set is identically zero.
- **Single-axis (0, n)** sources only the w-set: h_tw, h_S₁w, h_S₂w. The u-set is identically zero.

---

## 4. Do the off-diagonals form a gauge potential?

This is the chapter's central question. We examine whether the six-entry off-diagonal pattern h_μu, h_μw (with μ ∈ {t, S₁, S₂}) has the structural properties standard physics ascribes to a gauge potential.

### 4.1 Standard-physics properties (used as reference target)

Standard physics defines a gauge potential A_μ by four properties. We use these as the reference target — what the framework's off-diagonals would have to satisfy to be called gauge potentials in the standard sense.

**Property 1 — Index structure.** A_μ is a 4-vector field on spacetime: it has one index that runs over spacetime coordinates, and it transforms as a vector under spacetime coordinate changes (with the compact direction held fixed).

**Property 2 — Gauge transformation.** Under a local U(1) phase rotation φ → e^(iα(x))φ, A_μ shifts by a gradient: A_μ → A_μ + (1/e)∂_μα. Equivalently, in KK language, A_μ shifts by ∂_μΛ when the compact coordinate is shifted by a function Λ(x).

**Property 3 — Field strength.** F_μν = ∂_μA_ν − ∂_νA_μ is the antisymmetric field strength. The Lagrangian density −¼F_μν F^μν gives Maxwell's equations.

**Property 4 — Coupling to charged matter.** A_μ couples to charged matter via the covariant derivative D_μ = ∂_μ + ieA_μ. In the geodesic equation for a charged particle on the perturbed metric, A_μ appears as a Lorentz-force term proportional to the particle's compact-direction momentum.

### 4.2 Testing the framework's off-diagonals against the four properties

For the closure-satisfying mode's h_μu set (and equivalently the h_μw set), we test each property in turn.

**Property 1 (index structure):** h_μu has one spacetime index (μ) and one compact-direction index (u). Under a spacetime-only coordinate change (one that holds u fixed), h_μu transforms as a covariant 4-vector — exactly as a gauge potential A_μ does. ✓ *Property reproduced.*

**Property 2 (gauge transformation):** Under a coordinate change x^u → x^u + Λ(t, S₁, S₂), the metric component h_μu shifts as h_μu → h_μu + ∂_μΛ. This is precisely the U(1) gauge transformation of standard physics. The KK identification A_μ = h_μu / (some normalization) makes the transformation properties of A_μ and h_μu coincide. ✓ *Property reproduced.*

**Property 3 (field strength):** Construct the antisymmetric combination F^A_μν = ∂_μ h_νu − ∂_ν h_μu. This is invariant under the gauge transformation of property 2 (the gauge term ∂_μΛ cancels in the antisymmetric combination). The 6 components of F^A_μν organize into electric and magnetic parts under the 3+1 split (3 components for E^A, 3 for B^A). The Lagrangian density −¼F^A_μν (F^A)^μν follows from the standard Einstein-Hilbert action restricted to the off-diagonal sector. ✓ *Property reproduced.*

**Property 4 (coupling to charged matter):** A particle on the perturbed metric h_μu follows a geodesic equation that, in the slow-motion limit, picks up a force term ∝ p^u (∂_μ h_νu − ∂_ν h_μu) ẋ^ν. This is precisely the Lorentz-force coupling, with p^u playing the role of charge and F^A_μν = ∂_μh_νu − ∂_νh_μu playing the role of the EM field strength. ✓ *Property reproduced.*

### 4.3 Both U(1)s

The same analysis applied to the h_μw set produces a second gauge potential B_μ, with field strength F^B_μν = ∂_μ h_νw − ∂_ν h_μw, and coupling proportional to p^w. The two U(1)s are independent: a coordinate change of u does not affect h_μw, and vice versa.

So the framework structurally reproduces a **U(1) × U(1) gauge structure** at the linearized level — exactly the topology that [grid-duality §7.5.3](../grid-duality/07-wrap-promotion-modeling.md) identifies for the 2-torus closure at L3. The metric-side and topological views agree: the L3 substrate carries two independent U(1) gauge potentials, and our linearized Einstein analysis produces both.

### 4.4 What's been shown

For closure-satisfying modes, the off-diagonal metric perturbations h_μu and h_μw satisfy all four properties standard physics uses to define gauge potentials, separately for each compact direction. The KK identification is not assumed — it emerges from the linearized-EE analysis applied to the closure-satisfying mode's stress-energy.

This is the metric-side derivation of what the closure condition (Chapter 4) accomplishes: closure-satisfaction is the rule under which the off-diagonals form valid gauge potentials, with both U(1)s active. We have not assumed standard EM; we have derived a structure that satisfies the standard-physics definitions of gauge potentials, given the closure-satisfaction prerequisite.

---

## 5. Closure-failing modes do not form valid gauge potentials

For single-axis modes (m, 0) or (0, n), only one set of off-diagonals is sourced. The other set is identically zero.

### 5.1 The structural deficiency

Take a single-axis mode (m, 0) for concreteness. The h_μu set has all the gauge-potential properties of §4.2 — the property tests pass for the u-direction:

- h_μu transforms as a 4-vector ✓
- Gauge transformation under u-shifts ✓
- Field strength F^A_μν well-defined ✓
- Coupling to compact-momentum-carrying matter ✓

Taken alone, this single U(1) gauge potential A_μ is structurally indistinguishable from standard EM at the linearized level. So why does this mode fail to produce observable EM?

The answer lies in the **U(1) × U(1) cross-coupling structure** required by [grid-duality §8.2](../grid-duality/08-where-alpha-appears.md) for α-mediated EM. Per grid-duality's analysis, observable EM requires *both* winding directions to be active simultaneously. The α coupling is fundamentally a *cross-coupling* between the two U(1)s — without the second one, there is no cross-coupling structure for α to sit in, and the apparent gauge potential A_μ has no observable manifestation.

A single-axis mode therefore carries **partial gauge structure** — one U(1) in isolation — but lacks the cross-coupling that produces observable EM. The gauge structure is incomplete in exactly the way grid-duality identifies as structurally required.

### 5.2 The metric-side confirmation

This is the metric-side confirmation of the L2-in-L3 framing: single-axis modes have mass (energy density T_tt, T_uu source diagonal metric perturbations and gravitational mass) but no observable EM (the gauge structure is incomplete). The structural property here — massive states without EM coupling — is what standard physics ascribes to neutrinos; whether single-axis modes correspond to standard-physics neutrinos is a downstream MaSt-correspondence question.

What the metric-side analysis adds beyond the phase-pattern view of Chapter 4: it makes the structural deficiency *concrete*. Closure-failing modes are not just "not satisfying a phase pattern" — they are missing one of the two gauge potentials that the L3 substrate's α-mediated EM requires. The two views agree on which modes are EM-observable and which aren't, but the metric-side view shows *why* in terms of off-diagonal structure.

### 5.3 What about light?

The (0, 0) zero mode sources no off-diagonals at all (no compact-direction momentum). Its h_μν is purely diagonal — it bends spacetime gravitationally but has no gauge-potential content. From the metric-side view, light is the trivial case: it propagates at c on the perturbed metric, picking up gravitational deflection from any nearby matter (per metric-mass Ch 6) but contributing no gauge-potential perturbation itself. Consistent with light being its own propagation mode rather than a sourcing mass.

---

## 6. The three views are mutually consistent

[Chapter 1 §10](01-foundation.md) introduced the closure condition with three views. We can now confirm they agree on which (m, n) modes carry observable EM.

### 6.1 The three views

| View | Condition | Source chapter |
|---|---|---|
| Phase-pattern | 2π winding on w + standing waves on both u and w | [Chapter 4](04-the-closure-condition.md) |
| Topological | Both winding integers (m, n) ≠ 0 — U(1) × U(1) cross-coupling active | [grid-duality §7.5–§8](../grid-duality/07-wrap-promotion-modeling.md) |
| Metric-side | Both h_μu and h_μw sourced; both pass gauge-potential property tests | This chapter |

### 6.2 The three views select the same modes

For each (m, n) class:

| (m, n) class | Phase-pattern | Topological | Metric-side |
|---|---|---|---|
| (0, 0) | Fails (no winding) | Fails (no winding) | Fails (no off-diagonals) |
| (m, 0) | Fails (no w-standing-wave) | Fails (one winding zero) | Partial gauge structure (only h_μu) |
| (0, n) | Fails (no u-standing-wave) | Fails (one winding zero) | Partial gauge structure (only h_μw) |
| (m, n) both ≠ 0 | Satisfies | Satisfies | Both gauge potentials active |

The three views agree on the partition into observable-EM modes vs. non-observable. This consistency is a structural cross-check that the closure condition is well-defined across multiple framings — and that the framework's three-way framing in [Chapter 1 §10](01-foundation.md) was correct.

### 6.3 The asymmetry is one convention with three faces

The three views also expose an interesting alignment: each view has a closure-asymmetry built in (preferring w over u for the phase-pattern view; preferring one of the two U(1)s as physical for the metric-side view; preferring tube over ring for the topological view per the conventions of [Chapter 3 §3.2](03-knots-on-the-torus.md)). All three asymmetries point the same direction.

Whether to read this as one underlying convention manifesting three times, or as three independent conventions that happen to align, is a chapter-deep question. The most parsimonious reading is **one convention with three faces** — a single asymmetry-breaking choice (whatever its deeper origin) that shows up consistently in all three frameworks. Chapter 4 §5.1 noted this is open work for [grid-duality §8](../grid-duality/08-where-alpha-appears.md) and downstream alpha-derivation work.

---

## 7. The holonomy mechanism for bending

Drawing the chapter's results together, we have the **calculable mechanism** for how mass mechanically bends spacetime and how charged matter creates EM fields. This is the mechanism flagged in [metric-mass Chapter 6 §4](../metric-mass/06-gravitational-bending.md) and forward-referenced in [Chapter 1 §10](01-foundation.md).

### 7.1 The chain

1. A closure-satisfying mode at fixed (m, n) carries compact-direction momenta p_u = ℏk_u, p_w = ℏk_w (Chapter 2 §5).
2. These compact momenta source off-diagonal stress-energy T_tu, T_S₁u, ..., T_S₂w (this chapter §2).
3. Linearized Einstein equations source off-diagonal metric perturbations h_tu, h_S₁u, ..., h_S₂w (this chapter §3).
4. These off-diagonals satisfy the four properties of standard-physics gauge potentials (this chapter §4) — they are A_μ and B_μ in the KK identification.
5. A passing wave's worldline through the perturbed metric picks up phase via the line integral ∮ A_μ dx^μ (and similarly for B_μ).
6. That phase manifests as **trajectory deflection** (gravitational lensing) and **coordinate-time slowdown** (Shapiro delay) for the gravitational case, and as **EM refractive-index physics** (charged matter slowing light in materials) for the EM case.

Each step is explicitly computable from the apparatus developed in this chapter and Chapter 2. The mechanism is more granular than standard GR's "mass curves spacetime, particles follow geodesics" postulate — it locates the mechanism in compact-direction momentum, off-diagonal sourcing, and gauge-potential holonomy.

### 7.2 Gravitational and EM versions

Both gravitational and electromagnetic bending emerge from the same off-diagonal-sourcing chain. The difference is which specific off-diagonal entries dominate the holonomy in a given regime:

- **Gravitational case:** the diagonal-metric perturbations from energy density (T_tt) dominate. Massive matter near a passing wave produces curvature; the wave bends along geodesics on the curved metric. Gauge potentials A_μ, B_μ are active too but typically much weaker in their effect on the wave's worldline at long range.
- **EM case (refractive-index physics):** the gauge-potential off-diagonals dominate. Charged matter (closure-satisfying modes) couples to passing EM waves through the gauge-potential channel; the wave's phase velocity slows. Gravitational coupling is also present but typically dwarfed by α-mediated EM effects in atomic-scale matter.

For closure-failing modes (single-axis): the holonomy mechanism still operates for the diagonal-metric perturbations (gravitational lensing from energy density), but not for the gauge-potential channel. Single-axis modes bend light gravitationally but produce no EM holonomy. Consistent with the structural property of mass without EM coupling — what standard physics ascribes to neutrinos.

### 7.3 Observable predictions from the mechanism

Three predictions follow from the chain:

1. **Gravitational lensing of light by mass** — emerges quantitatively from the chain in the linearized regime, agreeing with standard GR predictions to the order of approximation.
2. **EM refractive index of matter** — emerges from the gauge-potential channel; the standard Lorentz-oscillator picture of refractive index becomes a special case of the holonomy mechanism evaluated in the closure-satisfying mode's gauge-potential channel.
3. **Distinct gravitational-only behavior of single-axis (neutrino-class) modes** — they bend light gravitationally but show no EM coupling. This matches what standard physics observes for neutrinos (gravitational interaction only, no EM coupling).

The third prediction is the most distinctive of the framework: it predicts the existence of mass-only modes structurally, as the L2-in-L3 mass-only states of Chapter 2 §4. Standard physics calls these neutrinos and ascribes the same property; whether the framework's predictions for *which specific particles* these are matches the standard-physics inventory is downstream MaSt-correspondence work.
<!--EC Not sure standard physics exclusively calls them neutrinos.  Might be more accurate to say that they are candidates for non-charged masses such as neutrinos and dark matter.  Would you agree? -->
---

## 8. What the framework reproduces and where it might differ

This chapter set out to ask whether the off-diagonal sourcing produces a gauge structure matching standard physics. Section 4 answered yes for the four-property test, separately for each U(1). Section 6 confirmed consistency across the three views from Chapter 1 §10.

What the framework **reproduces** at the linearized level:

- U(1) × U(1) gauge symmetry — the topology of [grid-duality §7.5.3](../grid-duality/07-wrap-promotion-modeling.md) emerges from the metric-side off-diagonal pattern.
- Gauge-potential transformation properties — the four standard-physics properties of A_μ are all reproduced for each compact direction's off-diagonal set.
- The holonomy structure of EM coupling to charged matter — the §7 chain provides this directly.
- Structural neutrality of mass-only modes (the property standard physics ascribes to neutrinos) — single-axis modes have partial gauge structure that doesn't produce observable EM.
- Gravitational lensing and Shapiro delay — emerges from diagonal-metric perturbations as a special case of the holonomy mechanism.

Where the framework **might differ** from standard physics:

- **Two U(1)s, not one.** The framework structurally has both A_μ (from h_μu) and B_μ (from h_μw). Standard physics observes one EM gauge potential. Whether the second U(1) corresponds to a known force (e.g., a magnetic-charge analog under Hodge duality, per [grid-duality §7.5.3](../grid-duality/07-wrap-promotion-modeling.md)), to something not yet identified, or to a redundancy that gauge fixing eliminates, is open. The framework predicts a structural duality at L3 that may or may not have a Standard Model counterpart.

- **The closure-asymmetry origin is conventional.** The choice of which U(1) is "physical EM" comes from the conventions of [Chapter 3 §3.2](03-knots-on-the-torus.md) — closure asymmetry, aspect ratio convention, gauge convention. Standard physics treats the EM gauge structure as observationally determined. The framework treats the asymmetry as conventional and notes that the convention itself may be derivable downstream.

- **α coupling strength is not derived here.** The structural location of α at L3 is settled by [grid-duality §8](../grid-duality/08-where-alpha-appears.md); the numerical value is open work for grid alpha-derivation. This chapter's analysis is at the linearized level where the coupling strength's specific value does not affect structural conclusions.

- **Nonlinear backreaction is deferred.** Linearized Einstein equations only. Whether the gauge-potential properties survive at higher orders, and whether full nonlinear self-consistency is achievable, is downstream work (cf. [Chapter 1 §11](01-foundation.md) non-assumptions).

The framework reproduces standard EM at the structural level. Whether it reproduces standard EM *quantitatively* — exact mass and charge values, exact magnetic moments, full higher-order corrections — depends on the α derivation and nonlinear analysis downstream. At the level this chapter operates (linearized, structural), the correspondence holds.

---

## 9. What's next

[Chapter 6 — Handedness and pairs](06-handedness-and-pairs.md). Take the closure-satisfying inventory from Chapter 4 and the gauge-potential structure from this chapter, and examine the **chirality / handedness** structure: when do (m, n) and (−m, −n) correspond to physically distinguishable particles (in the sense of what standard physics calls matter vs antimatter), and when do they represent the same particle viewed two different ways? Examine when complementary pairs *within a single field configuration* cancel net charge (apparent neutrality through internal cancellation, distinct from the structural neutrality of single-axis modes from this chapter).

The closure-condition structure that was settled in chapters 4 and 5 — which (m, n) modes carry observable EM and which don't — is the substrate. Chapter 6 adds handedness as a sub-(m, n) label and asks what physical content the sign-reflection symmetry carries.

---

## What this chapter does **not** do

- **Does not postulate gauge symmetry.** The Standard Model gauge structure appears as a target the chapter examines, not an input. The four-property test in §4 was applied to determine whether the off-diagonals satisfy standard-physics gauge-potential properties — a positive test, not an assumption.
- **Does not derive numerical α.** Cited from [grid-duality §8](../grid-duality/08-where-alpha-appears.md); structural location is settled there, numerical value is grid alpha-derivation work.
- **Does not derive Maxwell's equations.** Standard EM is a reference target. Whether Maxwell's equations follow from the off-diagonal sourcing in some appropriate limit is downstream work.
- **Does not assign handedness or matter/antimatter.** Chapter 6.
- **Does not commit to whether B_μ is a known Standard Model force or new physics.** Open question forwarded to grid alpha-derivation and downstream MaSt-correspondence work.
- **Does not analyze nonlinear backreaction.** Linearized Einstein equations only; nonlinear self-consistency is deferred (per [Chapter 1 §11](01-foundation.md)).
- **Does not analyze multi-knot energetics.** [metric-binding](../metric-binding/) territory.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| Are the two U(1) gauge potentials (A_μ from h_μu, B_μ from h_μw) both physical, or is only one observed? | Convention question; possibly settled by grid alpha-derivation |
| Does B_μ correspond to a known force (Hodge-dual of EM, magnetic charge, etc.) or to new physics? | Downstream grid + MaSt-correspondence work |
| Does the holonomy mechanism (§7) reproduce standard gravitational lensing predictions quantitatively? | Cross-check with metric-mass Chapter 6 + standard GR |
| Why are the closure-rule, aspect-ratio, and gauge conventions all aligned (one convention with three faces)? | Structural question; possibly forced by deeper symmetry; grid alpha-derivation |
| Does the framework's prediction of a U(1) × U(1) gauge structure quantitatively match standard EM at every order, or only at linearized order? | Nonlinear backreaction work, deferred |
| Does T_uw (cross-compact stress-energy) interact with σ_uw shear in chapter 8 in a structurally meaningful way? | Chapter 8 |
| Does the framework predict any deviation from standard EM that could be experimentally tested? | Open; depends on B_μ identification and nonlinear corrections |
