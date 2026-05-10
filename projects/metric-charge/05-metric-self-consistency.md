# Chapter 5 — Metric self-consistency and gauge promotion

This chapter takes the closure-satisfying modes identified in [Chapter 4](04-the-closure-condition.md) and asks the **metric-side** question: under linearized Einstein equations, what off-diagonal metric entries do these modes source, and do those entries have the structure that standard physics calls a *gauge potential*?

The chapter's structural parallel is [metric-mass Chapter 5](../metric-mass/05-metric-self-consistency.md), but on a 2D-compact substrate. metric-mass found that a 1D-compact mass mode's per-component (single traveling-wave) stress-energy sources g_tu under linearized Einstein equations; the metric-mass standing-wave principle then *cancelled* that cross-term in the directionless ±n superposition, leaving only diagonal modifications — pure mass, no gauge structure. The 2D-compact extension introduces a second compact direction, with two per-component cross-terms (g_tu and g_tw) instead of one, and the chapter's central question is what the standing-wave principle does to them under the framework's wrap-order convention.

The answer this chapter derives: under the wrap-order convention of [Chapter 1 §10](01-foundation.md), one cross-term cancels (the ring direction's, by the metric-mass mechanism) and the other survives (the tube direction's, as the standard Kaluza-Klein gauge potential). Closure-satisfying particles produce **a single gauge field B_μ from h_μw**, matching standard EM at the structural level.

**Framing convention.** Standard Model terminology (gauge potential, Maxwell's equations) is used in this chapter as a **reference target** — a structure the framework's derivations may or may not reproduce. We do not adopt the Standard Model as axiomatic. The questions are:

- Do the off-diagonal entries our closure-satisfying modes source have the algebraic and geometric properties standard physics uses to define a gauge potential?
- If yes, the framework *reproduces* the standard gauge structure — emergent, not postulated.
- If partially, the framework *predicts* deviations from standard EM that may or may not match observation.

This is the discovery-not-proof philosophy of [metric-charge](README.md) applied to the gauge structure: let the math reveal what emerges, with standard physics as the comparison target rather than the starting point.

**Inheritance.**

- *From [metric-mass Chapter 5](../metric-mass/05-metric-self-consistency.md):* the standing-wave-as-particle reading, the per-component stress-energy machinery, and the off-diagonal cancellation that produces mass-only configurations from the equal-amplitude ±n superposition. The 2D-compact extension uses the same machinery, applied asymmetrically per the wrap-order.
- *From [Chapter 1 §10](01-foundation.md):* the wrap-order convention (u = ring, w = tube) and the chirality form of the closure rule.
- *From [Chapter 4](04-the-closure-condition.md):* the closure-satisfying inventory (T(m, 1) primitives and their k × T(m, 1) multi-link repetitions).
- *From [grid-duality §7.5–§8](../grid-duality/07-wrap-promotion-modeling.md):* the L3 location of charge in the wrap-promotion ladder.

**Distinctive job.** Derive the single gauge potential per closure-satisfying particle via the wrap-order-asymmetric standing-wave construction. Confirm the metric-side derivation is exactly equivalent to the chirality criterion of Chapter 1 §10 (i.e., the four views — chirality, synchronization, topological, metric-side — all agree on which (m, n) carry observable EM). Provide the calculable mechanism for gravitational and EM bending flagged in [metric-mass Chapter 6 §4](../metric-mass/06-gravitational-bending.md). Make any standard-EM correspondence a consequence rather than an assumption.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The chapter's job — three guiding questions |
| 2 | Per-component stress-energy of a 2D-compact mode |
| 3 | Per-component off-diagonal sourcing under linearized Einstein equations |
| 4 | The wrap-order-asymmetric standing-wave construction — one gauge field |
| 5 | Closure-failing modes — mass-only outcomes via the same construction |
| 6 | Equivalence of the four views (chirality, synchronization, topological, metric-side) |
| 7 | The holonomy mechanism for bending |
| 8 | What the framework reproduces |
| 9 | What's next |

---

## 1. The chapter's job

Take the closure-satisfying inventory from [Chapter 4 §6](04-the-closure-condition.md). For each mode class, compute T_μν, identify the off-diagonal entries it sources via linearized Einstein equations, and apply the standing-wave-as-particle principle inherited from [metric-mass Chapter 5](../metric-mass/05-metric-self-consistency.md) — applied asymmetrically per the wrap-order convention to determine which cross-terms survive in the natural particle.

Three questions guide the chapter:

1. What off-diagonal entries does each closure-satisfying mode source *per-component* (i.e., for a single traveling-wave component before the standing-wave construction)?
2. Under the wrap-order-asymmetric standing-wave construction, which cross-terms survive in the natural particle, and do they form a valid gauge potential in the standard-physics sense?
3. How do closure-failing modes (single-axis, genuine torus knots) behave under the same construction — do their natural particles source EM cross-terms?

§§2–3 establish the per-component intermediate (the single traveling-wave stress-energy and what it would source). §4 introduces the wrap-order-asymmetric standing-wave construction and derives that exactly *one* gauge potential survives per closure-satisfying particle. §5 confirms closure-failing modes produce no EM cross-term under the same construction (mass-only outcomes). §6 confirms the metric-side derivation is exactly equivalent to the chirality criterion of Chapter 1 §10. §7 develops the holonomy mechanism that connects all of this to physical bending. §8 audits what the framework reproduces.

---

## 2. Per-component stress-energy of a 2D-compact mode

This section computes the stress-energy of a *single traveling-wave component* at fixed (m, n). Per [metric-mass Chapter 5](../metric-mass/05-metric-self-consistency.md), the single traveling-wave is a **per-component intermediate**, not a particle: it has a definite direction of phase advance around the compact loops, and the physical particle is the equal-amplitude superposition that enforces the appropriate topological symmetries (§4 develops which superposition is appropriate under the wrap-order). The per-component stress-energy is the building block the standing-wave construction operates on.

For a separable mode at fixed (m, n):

<!-- φ(t, u, w) = T(t) U(u) W(w) -->
$$
\varphi(t, u, w) = T(t)\cdot U(u)\cdot W(w)
$$

we use the standard complex-exponential notation T(t) ∝ e^(−iωt), U(u) ∝ e^(i k_u u), W(w) ∝ e^(i k_w w) as **calculational shorthand** for real-valued sinusoidal traveling waves. Per [Chapter 1 §6](01-foundation.md), φ is real-valued; the physical field is the real part of the complex form, and the imaginary part is bookkeeping for sinusoidal evolution. The signed integers (m, n) ∈ ℤ² label traveling-wave configurations on the closed curve T(m, n) per [Chapter 1 §6.1](01-foundation.md); the sign of (m, n) tracks which traversal direction the wave packet propagates. This is standard classical-wave-mechanics shorthand, not a commitment to a complex-valued field.

The stress-energy tensor T_μν follows from the standard scalar-field formula:

<!-- T_μν = ∂_μ φ ∂_ν φ* + ∂_ν φ ∂_μ φ* − g_μν L -->
$$
T_{\mu\nu} = \partial_\mu\varphi\,\partial_\nu\varphi^* + \partial_\nu\varphi\,\partial_\mu\varphi^* - g_{\mu\nu}\mathcal{L}
$$

with L the scalar-field Lagrangian density. (For a real-valued physical field this evaluates to the mode-averaged result; the complex notation simplifies the algebra. See [metric-mass Chapter 5 §2](../metric-mass/05-metric-self-consistency.md) for the explicit calculation.) That chapter computes T_μν for the 1D-compact case in factored form T_μν = 2|φ|² k_μ k_ν with k_μ = (−ω, k_S, n/R_u). The 2D-compact extension is mechanical:

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

| Mode class | T_μν off-diagonals nonzero (per-component) |
|---|---|
| Light (0, 0) | None (no compact-direction structure) |
| Single-axis (m, 0) | T_tu only at rest; T_tu, T_S₁u, T_S₂u when moving — *u-set only* |
| Single-axis (0, n) | T_tw only at rest; *w-set only* |
| Diagonal (m, n) both nonzero | At rest: T_tu *and* T_tw. When moving: full six-entry pattern. *Both u-set and w-set sourced* |

The diagonal-mode entry has *two* spacetime↔compact off-diagonals at the per-component level — one too many relative to standard EM's single U(1) gauge potential. **Resolving this two-cross-term apparent over-prediction is what §4's standing-wave construction does.**

### 2.3 Cross-compact entry T_uw

For diagonal modes, the entry T_uw = k_u · k_w is also nonzero. This is *not* a spacetime↔compact off-diagonal — it is a compact↔compact cross-term. It is distinct from the σ_uw shear of [Chapter 1 §4](01-foundation.md) (which is an externally imposed metric parameter, not a wave-equation source); we flag it here because it appears for diagonal modes and may interact with σ_uw shear in chapter 8.

---

## 3. Per-component off-diagonal sourcing under linearized Einstein equations

For each nonzero T_μν entry of §2, the linearized Einstein equation sources a corresponding metric perturbation h_μν. [metric-mass Chapter 5 §5](../metric-mass/05-metric-self-consistency.md) develops the linearized-EE machinery for the 1D-compact case; we apply the same machinery here. As in §2, this is the per-component intermediate sourcing — what §4's standing-wave construction will operate on.

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

Six spacetime↔compact off-diagonals at the per-component level, organized into two sets of three. The "Standard-physics correspondence" column states what the entries *would be* under the standard Kaluza-Klein identification — A_μ for the ring direction's set, B_μ for the tube direction's set. **At the per-component level, the framework over-predicts: standard EM has one gauge potential, the framework's per-component analysis has two.** §4's standing-wave construction resolves this by cancelling one of them.

For closure-failing modes (per-component):

- **Light (0, 0)** sources no off-diagonals. Diagonal h_μν only — no gravitational coupling beyond the trivial vacuum.
- **Single-axis (m, 0)** sources only the u-set: h_tu, h_S₁u, h_S₂u. The w-set is identically zero.
- **Single-axis (0, n)** sources only the w-set: h_tw, h_S₁w, h_S₂w. The u-set is identically zero.

---

## 4. The wrap-order-asymmetric standing-wave construction

This is the chapter's central derivation. The per-component analysis of §§2–3 produces two spacetime↔compact cross-terms (h_μu and h_μw) for closure-satisfying modes. The metric-mass standing-wave principle (single Bloch mode = per-component intermediate, particle = directionless ±n superposition) cancels n-linear cross-terms in 1D; this section applies the same principle to 2D-compact, with the asymmetry sourced from the wrap-order convention. The result is that exactly *one* cross-term survives in the natural particle.

### 4.1 The principle restated

Per [metric-mass Chapter 5 §7](../metric-mass/05-metric-self-consistency.md), the metric-mass standing-wave principle is **not** "uniformly standing-wave every compact direction." It is the more careful statement:

> Symmetrize the field over each topological symmetry the configuration *actually has*; enforce only the symmetries the substrate makes available.

In 1D-compact, u → −u is a topological symmetry of the unoriented circle; the particle inherits it as a particle symmetry, and combining ±n at equal amplitude is what enforces the symmetry. The cross-term cancellation is the algebraic consequence.

In 2D-compact, three sign-flip operations on the (m, n) labels are available, and each generates a candidate symmetrization. The wrap-order convention selects which of these is actually a *particle* symmetry of the natural particle.

### 4.2 The three candidate symmetrizations

The four traveling-wave components at fixed (|m|, |n|) — call them (++), (+−), (−+), (−−) by sign pattern — admit three independent equal-amplitude pair superpositions, each enforcing a different sign-flip symmetry:

| Symmetry enforced | Modes combined | Resulting wave |
|---|---|---|
| **R_J: (m, n) ↔ (−m, −n)** (joint sign reversal) | (++) + (−−) | 2A·cos(k_u u + k_w w)·cos(ωt) — directionless standing wave on T(m, n) |
| **R_u: m ↔ −m** (chirality of ring) | (++) + (−+) | 2A·cos(k_u u)·cos(k_w w − ωt) — *standing in u, traveling in w* |
| **R_w: n ↔ −n** (chirality of tube) | (++) + (+−) | 2A·cos(k_w w)·cos(k_u u − ωt) — standing in w, traveling in u |

For each, compute the surviving stress-energy entries (using ⟨cos²⟩ = ⟨sin²⟩ = 1/2 and ⟨sin·cos⟩ = 0 over a full period):

| Symmetry enforced | T_tu | T_tw | T_uw |
|---|---|---|---|
| R_J (joint reversal) | 0 | 0 | nonzero |
| **R_u (ring chirality)** | **0** | **nonzero** | **0** |
| R_w (tube chirality) | nonzero | 0 | 0 |

Three constructions, three different cross-term inventories. The math is unambiguous; what differs is *which symmetry to enforce*.

### 4.3 The wrap-order asymmetry selects R_u

The bare manifold T² is symmetric in (u, w): the metric is diagonal with no preferred direction, and the wave equation treats u and w identically. *On the bare manifold alone*, all three reflections are equally available. The wrap-order convention of [Chapter 1 §10](01-foundation.md) — u = ring, w = tube — distinguishes them.

We need to distinguish two notions of symmetry:

- **Topological symmetry of the curve.** Whether R takes T(m, n) to itself as a knot in 3-space.
- **Particle symmetry of the construction.** Whether R is enforced as a symmetrization in the natural-particle definition (modes combined in equal amplitude under R).

For closure-satisfying T(m, 1) — the unknot — both R_u and R_w are *topological* symmetries of the curve in 3-space (the unknot is achiral; reflecting it in either compact direction takes it to itself up to ambient isotopy). Topology alone does not distinguish them. The wrap-order's role is to single out which of the two chirality reflections gets enforced as a *particle* symmetry:

- **R_u (chirality reflection of the ring) — particle symmetry.** The wrap-order assigns the ring direction the metric-mass-style symmetric role: standing-wave construction in the ring, with the ring's chirality treated as a particle symmetry. Ring-direction wavenumber sign carries no observable.
- **R_w (chirality reflection of the tube) — *not* a particle symmetry.** The wrap-order assigns the tube direction the KK-style charge-bearing role: the sign of compact-direction wavenumber is a physical observable (charge sign). R_w would flip that sign and so cannot be enforced as a symmetrization, even though it remains a topological symmetry of the unknot.
- **R_J = R_u · R_w — *not* a particle symmetry.** Since R_w is not a particle symmetry, R_J is also not. Enforcing R_J overshoots — it cancels both cross-terms, including the one the wrap-order says should survive.

The distinction is sourced from the wrap-order, not from topology alone. The natural-particle construction enforces **R_u alone**: standing in the ring (u), traveling in the tube (w). One spacetime↔compact cross-term survives — the tube-direction's, h_μw — and is identified with the EM gauge potential B_μ.

### 4.4 Stress-energy of the natural particle, explicitly

Compute T_μν for φ_natural = 2A·cos(k_u u)·cos(k_w w − ωt) at rest in 4D. Derivatives:

- ∂_t φ = +2A·ω·cos(k_u u)·sin(k_w w − ωt)
- ∂_u φ = −2A·k_u·sin(k_u u)·cos(k_w w − ωt)
- ∂_w φ = −2A·k_w·cos(k_u u)·sin(k_w w − ωt)

Spatial-temporal averages:

| Entry | Average | Note |
|---|---|---|
| T_tt | A²·ω² | Doubled (relative to single component); rest-energy density |
| T_uu | A²·k_u² | Doubled; ring compact pressure |
| T_ww | A²·k_w² | Doubled; tube compact pressure |
| T_tu | **0** | cos·sin in u → 0; ring cross-term cancels by R_u-symmetrization |
| T_tw | **−A²·ω·k_w** | Doubled and surviving; tube cross-term sources gauge potential B_μ |
| T_uw | **0** | cos·sin in u → 0; cross-compact cancels |

The three off-diagonals reduce to one nonzero entry: **T_tw = −A²·ω·k_w**, doubled relative to a single traveling-wave component (which would give −A²·ω·k_w/2). Diagonal entries are also doubled, giving the rest-mass contribution

<!-- m² c² = (ℏk_u)² + (ℏk_w)² -->
$$
m_\text{rest}^2 c^2 \;=\; (\hbar k_u)^2 + (\hbar k_w)^2
$$

— the metric-mass mass formula extended to two compact directions, with both ring and tube contributing to rest energy. The natural particle has **rest mass plus exactly one gauge potential B_μ from h_μw**.

### 4.5 KK consistency

Standard 5D Kaluza-Klein theory ([primers/kaluza-klein.md](../../primers/kaluza-klein.md)) has 4D extended spacetime + 1 compact direction, treats a particle with definite compact-direction wavenumber, and identifies the cross-term g_μ5 = A_μ as the gauge potential. KK does *not* standing-wave the compact direction — the particle has definite charge, and the cross-term survives precisely because it does.

In this chapter's 2D-compact construction:

- The **tube direction (w) plays the role of standard KK's single compact direction.** The natural particle has definite n in the tube, the wave is traveling in w, and h_μw = B_μ survives — standard KK applied to the tube.
- The **ring direction (u) plays the role of metric-mass's single compact direction.** The natural particle has the standing-wave structure cos(k_u u), the wave is *not* traveling in u, and the per-component cross-term h_μu cancels — metric-mass applied to the ring.

The 2D-compact T² is decomposed by the wrap-order into "1D-compact for KK + 1D-compact for mass-only." Neither mechanism contradicts the other because they apply to different directions. The choice of which direction is which is forced by the wrap-order, which is fixed once for the framework as a whole and applies the same way to all modes. No new principles, no per-particle interpretive moves — standard KK on the tube, metric-mass on the ring.

### 4.6 Gauge-potential properties of the surviving B_μ

The single surviving cross-term h_μw satisfies the four standard-physics properties of a gauge potential, separately for each entry in the spacetime index μ:

**Property 1 — Index structure.** h_μw has one spacetime index (μ ∈ {t, S₁, S₂}) and transforms as a covariant 4-vector under spacetime coordinate changes that hold w fixed. ✓

**Property 2 — Gauge transformation.** Under a coordinate shift x^w → x^w + Λ(t, S₁, S₂), the metric component shifts as h_μw → h_μw + ∂_μΛ — the standard KK gauge transformation. ✓

**Property 3 — Field strength.** F^B_μν = ∂_μ h_νw − ∂_ν h_μw is antisymmetric and gauge-invariant (the gauge term ∂_μΛ cancels in the antisymmetric combination). The 6 components of F^B_μν organize into electric and magnetic parts under the standard 3+1 split. ✓

**Property 4 — Coupling to charged matter.** A particle on the perturbed metric h_μw follows a geodesic equation that, in the slow-motion limit, picks up a force term proportional to p^w (∂_μ h_νw − ∂_ν h_μw) ẋ^ν — the Lorentz-force coupling, with p^w playing the role of charge. ✓

The four properties are reproduced for the single surviving gauge potential. No second U(1) is left over; the framework's prediction matches standard physics' single observed EM gauge potential at the structural level.

---

## 5. Closure-failing modes — mass-only outcomes via the same construction

For closure-failing configurations, the topological status of R_u and R_w changes, and the natural-particle construction follows the same principle as §4: enforce only the topological symmetries the configuration actually has. Both closure-failing categories yield mass-only outcomes, confirming the construction is not ad hoc — the wrap-order-asymmetric standing-wave principle handles charged and neutral particles uniformly.

### 5.1 Single-axis modes

Modes (m, 0) or (0, n) — one winding zero. Take (m, 0):

- The wave has no w-dependence; reflections in w act trivially.
- R_u (sign of m) is the only nontrivial reflection. There is no chirality structure on the closed curve to test.
- Natural particle: (++) + (−+) → 2A·cos(k_u u)·cos(ωt). This is metric-mass's standing wave restricted to the u-direction, with no w-structure at all.
- T_tu = 0 (R_u cancellation, by the metric-mass mechanism). T_tw = 0 (no k_w to source it). T_uw = 0. **Mass only — no spacetime↔compact gauge potential.**

The (0, n) case gives mass-only by the symmetric calculation in w.

### 5.2 Genuine torus knots

For T(p, q) with p, q ≥ 2 and gcd(p, q) = 1, the curve is a *genuine* torus knot — chirally distinct from its mirror in 3-space.

- **R_u changes the knot type.** T(p, q) and T(−p, q) are mirror-chirality torus knots, distinct in 3-space. R_u is *not* a topological symmetry.
- **R_w changes the knot type.** Similarly distinct. R_w is *not* a topological symmetry.
- **R_J = R_u · R_w preserves the knot type.** T(p, q) and T(−p, −q) are the same unoriented curve (just opposite traversal). R_J *is* a topological symmetry.

The only available symmetry is R_J. Natural particle: (++) + (−−) → 2A·cos(k_u u + k_w w)·cos(ωt). By §4.2's table:

- T_tu = 0 (R_J cancels both spacetime↔compact cross-terms — including the one R_u alone would have preserved).
- T_tw = 0 (same).
- T_uw ≠ 0 (the compact↔compact cross-term is even under R_J, so it doubles rather than cancels — chirality-encoded T_uw, distinct from σ_uw shear).

**Mass + chirality field (in T_uw), no EM gauge potential.** Genuine torus knots are mass-only at the spacetime↔compact level, with a chirality signature in the compact↔compact cross-term that records which chirality of knot is present.

### 5.3 Why closure-satisfying and closure-failing diverge under the same construction

For closure-satisfying T(m, 1), the underlying curve is achiral in 3-space, so its chirality reflections (both R_u and R_w) are topological symmetries; R_u in particular is among them, and the wrap-order's selection of R_u as the particle symmetry is consistent with topology. For genuine torus knots, the underlying curve is chiral, so neither R_u nor R_w is a topological symmetry; R_u cannot be enforced as a particle symmetry without combining topologically distinct configurations. The construction falls back to R_J (the only remaining topological symmetry — joint reversal preserves the unoriented curve), yielding the mass-only configuration.

The closure rule of [Chapter 1 §10](01-foundation.md), expressed as a chirality criterion on the closed curve in 3-space, is **exactly equivalent** to the metric-side criterion "the wrap-order's R_u is enforceable as a particle symmetry, hence the natural particle sources a single gauge potential B_μ from h_μw." Both are descriptions of the same underlying fact: the curve's chirality status, which controls which wrap-order-aligned symmetries the natural particle inherits.

### 5.4 The closure-failing inventory at the metric-side level

| Category | Particle symmetry | T_tu | T_tw | T_uw | Outcome |
|---|---|---|---|---|---|
| Light (0, 0) | — (no compact structure) | 0 | 0 | 0 | Light, no EM |
| Single-axis (m, 0) | R_u (only available) | 0 | 0 (k_w = 0) | 0 | Mass only |
| Single-axis (0, n) | R_w (only available) | 0 (k_u = 0) | 0 | 0 | Mass only |
| Genuine torus knot T(p, q), gcd = 1 | R_J (only available) | 0 | 0 | nonzero | Mass + chirality field |

All closure-failing categories produce massive but EM-neutral states under the natural-particle construction. The *mechanism* differs: single-axis modes fail by structural degeneracy (no chirality structure to test); genuine torus knots fail by chirality non-degeneracy (R_u not a topological symmetry, fall back to R_J). The framework distinguishes them by which particle symmetry the natural-particle construction can enforce.

Standard physics has multiple categories of neutral massive states (neutrinos in three flavors, neutral mesons, neutral baryons, dark matter, the Higgs); how the framework's structural categories map to standard physics' inventory is downstream MaSt-correspondence work. Plus a separate cancellation-pair mechanism from [Chapter 6 §4](06-handedness-and-pairs.md) operates on top of these.

### 5.5 What about light?

The (0, 0) zero mode sources no off-diagonals at all (no compact-direction momentum). Its h_μν is purely diagonal — it bends spacetime gravitationally but has no gauge-potential content. From the metric-side view, light is the trivial case: it propagates at c on the perturbed metric, picking up gravitational deflection from any nearby matter (per metric-mass Ch 6) but contributing no gauge-potential perturbation itself. Consistent with light being its own propagation mode rather than a sourcing mass.

---

## 6. Equivalence of the four views

[Chapter 1 §10](01-foundation.md) introduced the closure condition in three equivalent forms (chirality, synchronization, topological) and announced a metric-side derivation in this chapter. We can now confirm that the four views agree on which (m, n) carry observable EM.

### 6.1 The four views

| View | Condition | Source |
|---|---|---|
| Chirality (primary) | The closed curve T(m, n) is achiral in 3-space *and* the wrap-order's R_u is a topological symmetry | [Ch 1 §10](01-foundation.md) |
| Synchronization (operational test) | n \| m with both nonzero | [Ch 1 §10](01-foundation.md), [Ch 4 §1](04-the-closure-condition.md) |
| Topological | gcd-reduced primitive of T(m, n) is T(m', 1) | [Ch 4 §1](04-the-closure-condition.md) |
| Metric-side | The wrap-order's R_u-symmetrization of the natural particle preserves a single spacetime↔compact cross-term h_μw | This chapter §4 |

### 6.2 The four views all agree

| (m, n) class | Chirality | Synchronization | Topological | Metric-side |
|---|---|---|---|---|
| (0, 0) | N/A (no curve) | Fails (no winding) | Fails (no winding) | No off-diagonals (light) |
| Single-axis (m, 0), (0, n) | Vacuous (no chirality structure) | Fails (one winding zero) | Fails | R_u or R_w-only symmetrization gives mass only |
| T(m, 1) primitives | Achiral; R_u is a symmetry → satisfies | n=1 \| m → satisfies | Primitive is T(m, 1) → satisfies | R_u-symmetrization yields one gauge potential h_μw |
| Genuine torus knot T(p, q), p,q ≥ 2, gcd = 1 | Chirally distinct from mirror → criterion (i) fails | n ∤ m → fails | Primitive is genuine torus knot → fails | R_u not a topological symmetry → fall back to R_J → mass only with chirality field T_uw |
| Multi-link k × T(m', 1) | Achiral per component → satisfies | n = k \| m = k·m' → satisfies | Primitive is T(m', 1) → satisfies | R_u-symmetrization per component yields k-fold gauge potential structure |
| Multi-link with genuine-knot primitive | Chirally non-degenerate per component → fails | Fails | Fails | R_J fallback per component → mass only |

All four views agree on every row. The closure rule's partition of (m, n) into charged-vs-neutral is the same regardless of which view we use to derive it.

### 6.3 Why all four agree

The four views are descriptions of the same underlying fact: the curve's chirality status in 3-space, which controls (a) whether the synchronization test n | m holds, (b) whether the gcd-reduced primitive is the unknot T(m', 1), and (c) whether the wrap-order's R_u can be enforced as a particle symmetry under the standing-wave construction. All three downstream consequences are equivalent because the wrap-order's selection of R_u as the particle symmetry is exactly the condition under which the natural particle sources a single gauge potential.

The chirality view is the most fundamental — it ties directly to the topological character of the curve in 3-space and explains *why* the closure rule selects the (m, n) it does. The synchronization view is operationally cleanest (just check n | m). The topological view is structurally cleanest (the gcd-reduced primitive form). The metric-side view is the derivation that produces the gauge field. Each is useful in its own context; all four select the same set of (m, n) configurations as charged.

### 6.4 The wrap-order convention's three faces

The wrap-order convention of [Chapter 1 §10](01-foundation.md) has three distinct projections — each of them a consequence of the single choice "u = ring, w = tube":

- **Closure rule.** The closure condition selects the chirality reflection R_u of the ring direction as the particle symmetry. (Equivalently, the synchronization test reads n | m, picking the direction-pair where the tube divides the ring.)
- **Aspect-ratio labels.** ε ≡ L_u/L_w; "thin sheet" = small ε labels the ring as the small direction, the tube as the large direction (or the reverse, depending on the regime).
- **Gauge identification.** The single surviving cross-term h_μw is identified with the EM gauge potential B_μ — chosen by the wrap-order's selection of w as the tube direction whose KK-style traveling-wave structure produces the gauge potential.

These three faces flip together under the bare-framework swap S: (u, w) ↔ (w, u) with L_u ↔ L_w and (m, n) ↔ (n, m). A consistent framework requires all three to align with a single wrap-order choice; flipping one without the others would invert the framework's labels. The wrap-order's three faces are not three independent stipulations — they are projections of a single substrate-level convention inherited from [grid-duality](../grid-duality/)'s wrap-promotion ladder.

(σ_uw shear is a *separate* asymmetry-introducing mechanism, structurally distinct from the wrap-order convention. The σ_uw entry is symmetric in (u, w) — invariant under S — and what it breaks is a chirality reflection on the (m, n) labels (R_u or R_w) rather than the wrap-order swap. σ_uw operates *within* the natural particle to bias chirality balance, not at the wrap-order level. See [Chapter 6 §6](06-handedness-and-pairs.md) and [Chapter 8 §3](08-shear-and-fractional-charge.md).)

### 6.5 What this demonstration leaves open

The wrap-order convention is *adopted by stipulation* in [Chapter 1 §10](01-foundation.md). This chapter's derivation assumes the wrap-order is already fixed and reads off the consequences. Whether something physical (handedness of the embedding spacetime, substrate constraint from grid-primitive, or other) *forces* one wrap-order over the other is downstream work for [grid-duality §8](../grid-duality/08-where-alpha-appears.md) and the alpha-derivation track. The σ_uw shear's sign is similarly left open here; it is examined in [Chapter 8](08-shear-and-fractional-charge.md).

---

## 7. The holonomy mechanism for bending

Drawing the chapter's results together, we have the **calculable mechanism** for how mass mechanically bends spacetime and how charged matter creates EM fields. This is the mechanism flagged in [metric-mass Chapter 6 §4](../metric-mass/06-gravitational-bending.md) and forward-referenced in [Chapter 1 §10](01-foundation.md).

### 7.1 The chain

1. A closure-satisfying mode at fixed (m, n) carries compact-direction momenta p_u = ℏk_u, p_w = ℏk_w (Chapter 2 §5).
2. The natural particle (R_u-symmetrized per §4) sources diagonal stress-energy (T_tt, T_uu, T_ww) and a single off-diagonal stress-energy entry T_tw (and its moving-particle extensions T_S₁w, T_S₂w when k_S ≠ 0).
3. Linearized Einstein equations source the diagonal metric perturbation (gravitational mass) and the single off-diagonal metric perturbation h_μw (the surviving gauge potential).
4. The off-diagonal h_μw satisfies the four properties of standard-physics gauge potentials (this chapter §4.6) — it is B_μ in the KK identification.
5. A passing wave's worldline through the perturbed metric picks up phase via the line integral ∮ B_μ dx^μ.
6. That phase manifests as **trajectory deflection** (gravitational lensing) and **coordinate-time slowdown** (Shapiro delay) for the gravitational case, and as **EM refractive-index physics** (charged matter slowing light in materials) for the EM case.

Each step is explicitly computable from the apparatus developed in this chapter and Chapter 2. The mechanism is more granular than standard GR's "mass curves spacetime, particles follow geodesics" postulate — it locates the mechanism in compact-direction momentum, off-diagonal sourcing, and gauge-potential holonomy.

### 7.2 Gravitational and EM versions

Both gravitational and electromagnetic bending emerge from the same off-diagonal-sourcing chain. The difference is which specific off-diagonal entries dominate the holonomy in a given regime:

- **Gravitational case:** the diagonal-metric perturbations from energy density (T_tt) dominate. Massive matter near a passing wave produces curvature; the wave bends along geodesics on the curved metric. The gauge potential B_μ is active too but typically much weaker in its effect on the wave's worldline at long range.
- **EM case (refractive-index physics):** the gauge-potential off-diagonal h_μw dominates. Charged matter (closure-satisfying modes) couples to passing EM waves through the gauge-potential channel; the wave's phase velocity slows. Gravitational coupling is also present but typically dwarfed by α-mediated EM effects in atomic-scale matter.

For closure-failing modes (single-axis or genuine torus knots): the holonomy mechanism still operates for the diagonal-metric perturbations (gravitational lensing from energy density), but not for the gauge-potential channel — neither configuration sources h_μw under the natural-particle construction. Closure-failing modes bend light gravitationally but produce no EM holonomy. Consistent with the structural property of mass without EM coupling — a property standard physics ascribes to multiple non-charged massive categories (neutrinos, dark matter candidates, certain neutral hadrons, the Higgs).

### 7.3 Observable predictions from the mechanism

Three predictions follow from the chain:

1. **Gravitational lensing of light by mass** — emerges quantitatively from the chain in the linearized regime, agreeing with standard GR predictions to the order of approximation.
2. **EM refractive index of matter** — emerges from the gauge-potential channel; the standard Lorentz-oscillator picture of refractive index becomes a special case of the holonomy mechanism evaluated in the closure-satisfying mode's gauge-potential channel.
3. **Distinct gravitational-only behavior of closure-failing modes** — they bend light gravitationally but show no EM coupling. This matches structural properties standard physics ascribes to non-charged massive states (neutrinos, dark matter candidates, the Higgs, certain neutral hadrons-in-isolation): gravitational interaction only, no EM coupling.

The third prediction is the most distinctive of the framework: it predicts the existence of mass-only modes structurally, as the closure-failing states of Chapter 4. Standard physics has multiple categories of non-charged massive states (neutrinos in three flavors, dark matter candidates, neutral mesons, the Higgs boson, neutral baryons); the framework's structural mass-only modes are candidates for any of these. Which framework state corresponds to which standard-physics category — or whether some categories are absent or duplicated under the framework's three-mechanism partition (single-axis, chirality-non-degenerate, cancellation-pair) — is downstream MaSt-correspondence work.
---

## 8. What the framework reproduces

This chapter set out to ask whether the off-diagonal sourcing produces a gauge structure matching standard physics. The wrap-order-asymmetric standing-wave construction of §4 answers yes — exactly one gauge potential B_μ from h_μw per closure-satisfying particle, with the four standard-physics gauge-potential properties reproduced (§4.6).

What the framework **reproduces** at the linearized level:

- **A single U(1) gauge potential per charged particle** — matching standard EM's single observed U(1)_em. The natural particle (R_u-symmetrized per §4) sources h_μw alone; the would-be h_μu cross-term cancels by the metric-mass mechanism applied to the ring direction.
- **Gauge-potential transformation properties** — the four standard-physics properties of an EM gauge potential are reproduced for h_μw (§4.6).
- **The holonomy structure of EM coupling to charged matter** — the §7 chain provides this directly.
- **Structural neutrality of mass-only modes** (the property standard physics ascribes to non-charged massive states such as neutrinos and dark matter) — single-axis and genuine-torus-knot modes source no spacetime↔compact gauge potential under the natural-particle construction.
- **Gravitational lensing and Shapiro delay** — emerge from diagonal-metric perturbations as a special case of the holonomy mechanism.

Where the framework's results are **conditional on downstream work**:

- **The wrap-order convention's origin is adopted, not derived.** The choice of "u = ring, w = tube" is fixed once for the framework as a whole and applies the same way to all modes ([Ch 1 §10](01-foundation.md)). Whether something physical (handedness of the embedding spacetime, substrate constraint from grid-primitive, or other) eventually forces this choice is downstream work for [grid-duality §8](../grid-duality/08-where-alpha-appears.md) and the alpha-derivation track.

- **α coupling strength is not derived here.** The structural location of α at L3 is settled by [grid-duality §8](../grid-duality/08-where-alpha-appears.md); the numerical value is open work for grid alpha-derivation. This chapter's analysis is at the linearized level where the coupling strength's specific value does not affect structural conclusions.

- **Nonlinear backreaction is deferred.** Linearized Einstein equations only. Whether the gauge-potential properties survive at higher orders, and whether full nonlinear self-consistency is achievable, is downstream work (cf. [Chapter 1 §11](01-foundation.md) non-assumptions).

The framework reproduces standard EM at the structural level: a single gauge potential per charged particle, with the standard-physics gauge-potential properties and the holonomic mechanism for both gravitational and EM bending. Whether it reproduces standard EM *quantitatively* — exact mass and charge values, exact magnetic moments, full higher-order corrections — depends on the α derivation and nonlinear analysis downstream. At the level this chapter operates (linearized, structural), the correspondence holds.

---

## 9. What's next

[Chapter 6 — Handedness and pairs](06-handedness-and-pairs.md). Take the closure-satisfying inventory from Chapter 4 and the single-gauge-potential structure from this chapter, and examine the **chirality / handedness** structure: when do (m, n) and (−m, −n) correspond to physically distinguishable particles (in the sense of what standard physics calls matter vs antimatter), and when do they represent the same particle viewed two different ways? Examine when complementary pairs *within a single field configuration* cancel net charge (apparent neutrality through internal cancellation, distinct from the structural neutrality of closure-failing modes from this chapter). Sharpen σ_uw shear's role: under work1's framing, σ_uw biases chirality *within particles* (the (++) vs (−+) amplitude balance), not matter/antimatter populations.

The closure-condition structure that was settled in chapters 4 and 5 — which (m, n) modes carry observable EM and which don't, and how the natural particle is constructed — is the substrate. Chapter 6 adds handedness as a sub-(m, n) label and asks what physical content the sign-reflection symmetry carries.

---

## What this chapter does **not** do

- **Does not postulate gauge symmetry.** The Standard Model gauge structure appears as a target the chapter examines, not an input. The four-property test in §4.6 was applied to determine whether the surviving cross-term satisfies standard-physics gauge-potential properties — a positive test, not an assumption.
- **Does not derive numerical α.** Cited from [grid-duality §8](../grid-duality/08-where-alpha-appears.md); structural location is settled there, numerical value is grid alpha-derivation work.
- **Does not derive Maxwell's equations.** Standard EM is a reference target. Whether Maxwell's equations follow from the off-diagonal sourcing in some appropriate limit is downstream work.
- **Does not assign handedness or matter/antimatter.** Chapter 6.
- **Does not derive the wrap-order convention itself.** The convention is adopted in [Chapter 1 §10](01-foundation.md); whether something physical forces it is open work for [grid-duality §8](../grid-duality/08-where-alpha-appears.md) and the alpha-derivation track.
- **Does not analyze nonlinear backreaction.** Linearized Einstein equations only; nonlinear self-consistency is deferred (per [Chapter 1 §11](01-foundation.md)).
- **Does not analyze multi-knot energetics.** [metric-binding](../metric-binding/) territory.

---

## Open questions flagged in this chapter

| Q | Where it goes |
|---|---|
| What forces the wrap-order convention's specific direction (u = ring rather than u = tube)? Is it adopted-by-stipulation or substrate-derived? | [grid-duality §8](../grid-duality/08-where-alpha-appears.md) + alpha-derivation track |
| Does the holonomy mechanism (§7) reproduce standard gravitational lensing predictions quantitatively? | Cross-check with metric-mass Chapter 6 + standard GR |
| Does the framework's single-U(1) gauge structure quantitatively match standard EM at every order, or only at linearized order? | Nonlinear backreaction work, deferred |
| Does T_uw (the chirality-encoded compact-compact cross-term sourced by genuine torus knots) interact with σ_uw shear in chapter 8 in a structurally meaningful way? | Chapter 8 |
| Does the framework predict any deviation from standard EM that could be experimentally tested? | Open; depends on nonlinear corrections and the alpha-derivation track |
