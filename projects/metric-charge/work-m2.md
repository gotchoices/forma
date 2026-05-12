# work-m2.md — TODO-M2: Four-property gauge-potential test

This file evaluates [TODO-M2](STATUS.md) by working through the four-property gauge-potential test of [Ch 5 §4.6](05-metric-self-consistency.md) at both σ = 0 (the original scope) and σ ≠ 0 (the extension added by the Ch 8 refactor's single-Bloch-mode commitment in [Ch 8 §2.2](08-shear-and-fractional-charge.md)).

The framework's wrap-order convention ([Ch 1 §10](01-foundation.md): u = ring/mass, w = tube/charge) selects h_μw as the gauge candidate at both regimes; the four-property test serves to *confirm* h_μw satisfies standard-physics gauge-potential requirements, not to *select* among competing candidates. Under this framing, σ = 0 and σ ≠ 0 are a single derivation rather than two cases with different mechanisms.

- **σ = 0:** Properties 1–3 are bookkeeping; Property 4 is one Christoffel calculation yielding the Lorentz-force structure m d²x^μ/dτ² = F^B^μ_ν v^ν p^w. Confirms h_μw as gauge potential.
- **σ ≠ 0:** The single-Bloch-mode interpretation makes T_tu nonzero in addition to T_tw, so h_μu also gets sourced. Per the wrap-order convention, h_μu is the **mass-direction metric perturbation**, not a second gauge potential. The Lorentz-force structure for h_μw is unchanged; the h_μu contribution to the geodesic equation is a metric-distortion effect from the particle's ring-direction (mass-direction) structure.

Both regimes integrate cleanly into Ch 5 §4.6 as one unified derivation. No architectural decision required.

Conventions follow the rest of the project. M ≡ (ℏ/c)·(2π/L_w). σ ≡ σ_uw.

---

## Sections

| § | Topic |
|---|-------|
| 1 | The four properties (recap) |
| 2 | σ = 0: confirming h_μw as the gauge potential |
| 3 | σ ≠ 0: same convention, same gauge potential |
| 4 | Alternative framings considered (superseded) |
| 5 | Recommendation — unified integration |

---

## 1. The four properties (recap)

[Ch 5 §4.6](05-metric-self-consistency.md) states the four-property test for h_μw to qualify as a standard-physics gauge potential:

**Property 1 — Index structure.** h_μw has one extended-spacetime index μ ∈ {t, S₁, S₂} and one compact index w. It transforms as a covariant 4-vector under spacetime coordinate changes that hold w fixed.

**Property 2 — Gauge transformation.** Under a coordinate shift x^w → x^w + Λ(t, S₁, S₂), the metric component shifts as h_μw → h_μw + ∂_μ Λ.

**Property 3 — Field strength.** F^B_μν ≡ ∂_μ h_νw − ∂_ν h_μw is antisymmetric and gauge-invariant.

**Property 4 — Coupling to charged matter.** A particle on the perturbed metric h_μw follows a geodesic equation that, in the slow-motion limit, picks up a force term proportional to p^w (the tube-direction momentum) with the structure of the Lorentz force.

Properties 1–3 are bookkeeping that follows from the framework's existing symmetries; Property 4 is the substantive one — it tests whether the framework's wrap-order-selected gauge candidate satisfies standard-physics gauge-potential requirements.

**Framing note.** The test is a *confirmation* that h_μw — the gauge candidate selected by the wrap-order convention of [Ch 1 §10](01-foundation.md) — satisfies these properties. It is not a *selection mechanism* between competing candidates. The wrap-order axiom (u = ring/mass direction, w = tube/charge direction) does the structural selection; the four-property test confirms the selected candidate behaves as standard-physics requires.

---

## 2. σ = 0: confirming h_μw as the gauge potential

Per [Ch 5 §4](05-metric-self-consistency.md), the natural particle at σ = 0 is the R_u-symmetrized combination φ_natural = 2A·cos(k_u u)·cos(k_w w − ωt) with k_u = 2πm/L_u, k_w = 2πn/L_w. The surviving spacetime↔compact cross-term is h_μw, sourced by T_tw = −A²·ω·k_w (and its moving-particle extensions T_S₁w, T_S₂w when k_S ≠ 0).

The R_u-symmetrization at σ = 0 is one realization of the wrap-order convention: it mechanically cancels the cross-term h_μu (R_u-symmetrization makes the sign of m unobservable, ⟨p^u⟩ = 0 under the symmetrized state), in addition to the structural assignment of u as the mass direction. The two mechanisms — R_u-symmetrization at the particle level, wrap-order at the gauge-identification level — are consistent at σ = 0, with R_u-symmetrization providing additional mechanical cancellation that the convention alone does not require.

### 2.1 Property 1 — Index structure

Under a spacetime coordinate change x^μ → x'^μ(x^ν) that holds the compact coordinates fixed (x^u → x^u, x^w → x^w), the linearized metric component transforms as a tensor:

<!-- h_μw → (∂x^ν/∂x'^μ) h_νw -->
$$
h'_{\mu w} \;=\; \frac{\partial x^\nu}{\partial x'^\mu}\, h_{\nu w}
$$

Since x^w is held fixed (∂x^w/∂x'^μ = 0 for μ extended-spacetime), no cross-mixing into compact components occurs. h_μw transforms as a covariant 4-vector indexed by μ. ✓

### 2.2 Property 2 — Gauge transformation

Consider a coordinate shift acting only on the compact w-coordinate:

<!-- x^w → x^w + Λ(t, S₁, S₂), other coords fixed -->
$$
x^w \;\to\; x^w + \Lambda(t, S_1, S_2),
\qquad x^u, x^t, x^{S_1}, x^{S_2} \text{ fixed}
$$

The metric transforms as g'_αβ = (∂x^μ/∂x'^α)(∂x^ν/∂x'^β) g_μν. For the (μ, w) component with μ extended-spacetime, the Jacobian contributions are:
- ∂x^μ/∂x'^μ = δ^μ_μ (identity on extended-spacetime indices)
- ∂x^w/∂x'^μ = −∂_μ Λ (from x'^w = x^w + Λ)
- ∂x^w/∂x'^w = 1

To linear order in h and Λ:

<!-- h'_μw = h_μw + ∂_μΛ -->
$$
h'_{\mu w} \;=\; h_{\mu w} + \partial_\mu \Lambda
$$

Standard KK gauge transformation. ✓

### 2.3 Property 3 — Field strength

Define F^B_μν ≡ ∂_μ h_νw − ∂_ν h_μw. Under the gauge transformation of Property 2:

<!-- F^B_μν → ∂_μ (h_νw + ∂_νΛ) − ∂_ν (h_μw + ∂_μΛ) = F^B_μν -->
$$
F^B_{\mu\nu} \;\to\; \partial_\mu(h_{\nu w} + \partial_\nu \Lambda) - \partial_\nu(h_{\mu w} + \partial_\mu \Lambda) \;=\; F^B_{\mu\nu} + \partial_\mu \partial_\nu \Lambda - \partial_\nu \partial_\mu \Lambda \;=\; F^B_{\mu\nu}
$$

The Λ-terms cancel because partial derivatives commute. Antisymmetry follows by construction. ✓

### 2.4 Property 4 — Lorentz-force coupling

The substantive calculation. The geodesic equation for a test particle on the perturbed metric g_μν = η_μν + h_μν:

<!-- d²x^α/dτ² + Γ^α_βγ (dx^β/dτ)(dx^γ/dτ) = 0 -->
$$
\frac{d^2 x^\alpha}{d\tau^2} + \Gamma^\alpha_{\beta\gamma}\,\frac{dx^\beta}{d\tau}\,\frac{dx^\gamma}{d\tau} \;=\; 0
$$

For h_μν with only h_μw nonzero (and depending on extended-spacetime coordinates, not on u or w — the dimensional-reduction limit), the linearized Christoffel symbols:

<!-- Γ^α_βγ = (1/2) η^ασ (∂_β h_σγ + ∂_γ h_σβ − ∂_σ h_βγ) -->
$$
\Gamma^\alpha_{\beta\gamma} \;\approx\; \tfrac{1}{2}\,\eta^{\alpha\sigma}\bigl(\partial_\beta h_{\sigma\gamma} + \partial_\gamma h_{\sigma\beta} - \partial_\sigma h_{\beta\gamma}\bigr)
$$

Focus on Γ^μ_νw with μ, ν extended-spacetime indices:

<!-- Γ^μ_νw = (1/2) η^μσ (∂_ν h_σw + ∂_w h_σν − ∂_σ h_νw) -->
$$
\Gamma^\mu_{\nu w} \;=\; \tfrac{1}{2}\,\eta^{\mu\sigma}\bigl(\partial_\nu h_{\sigma w} + \partial_w h_{\sigma\nu} - \partial_\sigma h_{\nu w}\bigr)
$$

The middle term vanishes (∂_w h = 0 by dimensional reduction). The remaining two terms, with indices raised using the flat metric:

<!-- Γ^μ_νw = (1/2)(∂_ν h^μ_w − ∂^μ h_νw) = -(1/2) F^B^μ_ν -->
$$
\Gamma^\mu_{\nu w} \;=\; \tfrac{1}{2}\bigl(\partial_\nu h^\mu{}_w - \partial^\mu h_{\nu w}\bigr) \;=\; -\tfrac{1}{2}\,F^{B\,\mu}{}_\nu
$$

where F^B^μ_ν ≡ η^μα F^B_αν = ∂^μ h_νw − ∂_ν h^μ_w.

The geodesic equation's spacetime↔compact contribution:

<!-- d²x^μ/dτ² = -2 Γ^μ_νw (dx^ν/dτ)(dx^w/dτ) = F^B^μ_ν (dx^ν/dτ)(dx^w/dτ) -->
$$
\frac{d^2 x^\mu}{d\tau^2} \;=\; -2\,\Gamma^\mu_{\nu w}\,\frac{dx^\nu}{d\tau}\,\frac{dx^w}{d\tau} \;=\; F^{B\,\mu}{}_\nu\,\frac{dx^\nu}{d\tau}\,\frac{dx^w}{d\tau}
$$

(Factor of 2 from Γ^μ_νw and Γ^μ_wν being equal — Christoffel symmetric in lower indices.)

In the slow-motion limit, dx^ν/dτ ≈ v^ν and dx^w/dτ = p^w/m. Multiplying by m:

<!-- m d²x^μ/dτ² = F^B^μ_ν v^ν p^w -->
$$
\boxed{m\,\frac{d^2 x^\mu}{d\tau^2} \;=\; F^{B\,\mu}{}_\nu\, v^\nu\, p^w}
$$

**Lorentz-force structure** with p^w playing the role of charge q. The framework's wrap-order-selected h_μw satisfies the standard-physics gauge-potential coupling. ✓

All four properties confirmed at σ = 0.

---

## 3. σ ≠ 0: same convention, same gauge potential

Per [Ch 8 §2.2](08-shear-and-fractional-charge.md), the framework commits to the **single-Bloch-mode interpretation** of the natural particle under shear: at σ ≠ 0, the particle is one specific Bloch mode (m, n), with the wrap-order selecting the sign of m for which mass is lower. The σ = 0 R_u-symmetrization does not transfer (R_u is broken by the cross-term −2σmn/ε in the dispersion).

### 3.1 What changes under shear

For a single Bloch mode φ = A·e^{i(k_u u + k_w w − ωt)}, the stress-energy time-averages are (per [Ch 5 §2](05-metric-self-consistency.md) factored form T_μν = 2|φ|²·k_μ·k_ν with k_μ = (−ω, k_S₁, k_S₂, k_u, k_w)):

| Component | Time-averaged value |
|---|---|
| T_tt | 2A²·ω² |
| T_uu | 2A²·k_u² |
| T_ww | 2A²·k_w² |
| T_tu | −2A²·ω·k_u |
| T_tw | −2A²·ω·k_w |
| T_uw | 2A²·k_u·k_w |

Compared to the σ = 0 R_u-symmetrized natural particle (which had T_tu = T_uw = 0 by R_u-cancellation), the single-Bloch-mode construction has all three off-diagonals nonzero. The linearized Einstein equations source corresponding metric perturbations: h_μu (from T_tu, plus T_S₁u, T_S₂u when moving), h_μw (from T_tw, plus T_S₁w, T_S₂w), and h_uw (from T_uw).

**Per the wrap-order convention of [Ch 1 §10](01-foundation.md), the gauge-identification step is unchanged from σ = 0:**

- **h_μw** is the gauge potential — the wrap-order assigns w as the tube/charge direction. The four-property test confirms h_μw still satisfies standard-physics gauge-potential requirements at σ ≠ 0 (§3.2 below).
- **h_μu** is the mass-direction metric perturbation — the wrap-order assigns u as the ring/mass direction. Its nonzero source at σ ≠ 0 is a real metric effect (it appears in the geodesic equation), but it is not a gauge potential by convention. §3.3 characterizes its physical role.
- **h_uw** is the compact-compact cross-term encoding chirality, per [Ch 5 §5.2](05-metric-self-consistency.md) — not a gauge potential (no extended-spacetime index).

The σ = 0 R_u-symmetrization provided an additional mechanical cancellation of h_μu, on top of the wrap-order's structural assignment. At σ ≠ 0 the mechanical cancellation fails, but the structural assignment remains. The framework's "single gauge potential per closure-satisfying particle" claim is *grounded in the wrap-order axiom*, not in R_u-symmetrization. R_u-symmetrization was sufficient at σ = 0; under shear the framework relies on the axiom alone.

### 3.2 Four-property test on h_μw under shear

Each of Properties 1–4 runs identically to the σ = 0 derivation in §2:

- **Property 1** (index structure): h_μw still transforms as a covariant 4-vector under spacetime coordinate changes holding w fixed. The Jacobian argument is independent of σ. ✓
- **Property 2** (gauge transformation): The coordinate shift x^w → x^w + Λ_w(t, S₁, S₂) still gives h_μw → h_μw + ∂_μ Λ_w. ✓
- **Property 3** (field strength F^B_μν gauge-invariant): Follows from Property 2; partial derivatives commute. ✓
- **Property 4** (Lorentz-force coupling): The Christoffel calculation Γ^μ_νw = −(1/2) F^B^μ_ν is unchanged; the slow-motion limit yields:

<!-- m d²x^μ/dτ² (from h_μw) = F^B^μ_ν v^ν p^w -->
$$
\Bigl(m\,\frac{d^2 x^\mu}{d\tau^2}\Bigr)_{\!h_{\mu w}} \;=\; F^{B\,\mu}{}_\nu\, v^\nu\, p^w
$$

Same Lorentz-force structure as at σ = 0. p^w is the charge. ✓

The framework's gauge-potential claim h_μw → B_μ survives the shear-induced symmetry-breaking of R_u, because it was always grounded in the wrap-order convention rather than in R_u-symmetrization specifically.

### 3.3 The h_μu contribution: metric distortion, not gauge force

The single-Bloch-mode construction at σ ≠ 0 sources h_μu in addition to h_μw. Its contribution to the geodesic equation appears via the Christoffel term Γ^μ_νu, which by the symmetric calculation of §2.4 (with w → u substitution) equals −(1/2)·(∂^μ h_νu − ∂_ν h^μ_u). The geodesic equation acquires:

<!-- (m d²x^μ/dτ²)_h_μu = -2 Γ^μ_νu v^ν p^u -->
$$
\Bigl(m\,\frac{d^2 x^\mu}{d\tau^2}\Bigr)_{\!h_{\mu u}} \;=\; -2\,\Gamma^\mu_{\nu u}\, v^\nu\, p^u \;=\; (\partial^\mu h_{\nu u} - \partial_\nu h^\mu{}_u)\, v^\nu\, p^u
$$

with p^u the particle's ring-direction (mass-direction) momentum. The full geodesic equation under shear is the sum of the h_μw piece (§3.2) and this h_μu piece:

<!-- Full geodesic equation: m d²x^μ/dτ² = F^B^μ_ν v^ν p^w + (∂^μ h_νu − ∂_ν h^μ_u) v^ν p^u -->
$$
m\,\frac{d^2 x^\mu}{d\tau^2} \;=\; F^{B\,\mu}{}_\nu\, v^\nu\, p^w \;+\; (\partial^\mu h_{\nu u} - \partial_\nu h^\mu{}_u)\, v^\nu\, p^u
$$

The first term is the Lorentz force from the gauge potential B_μ ≡ h_μw, with p^w as charge. The second term is **a metric-distortion effect** from the mass-direction perturbation h_μu, coupling to the particle's ring-direction momentum p^u.

**Why this is not a second gauge force.** Mathematically, the second term has the same algebraic structure as the first (∂^μ h_νu − ∂_ν h^μ_u looks like an antisymmetric "field strength" of h_μu, and v^ν p^u looks like a "current"). But the framework's wrap-order convention says u is the mass direction, not a charge direction. The h_μu metric perturbation is not what the framework calls a gauge potential.

Physical reading: at σ ≠ 0, a closure-satisfying particle has definite p^u (the wrap-order picks one sign of m for the natural particle). This ring-direction momentum is part of the particle's mass structure (per Ch 1 §10's identification of u as the mass direction). The particle's mass structure creates a metric perturbation h_μu in extended spacetime, and another particle moving through this perturbation experiences a velocity-dependent metric distortion — structurally analogous to gravitational frame-dragging from a rotating mass, not to a Lorentz force from a separate gauge field. It is part of the gravitational interaction, not part of the electromagnetic interaction.

The framework's mass/charge distinction at σ ≠ 0 is therefore: charge (from p^w via h_μw) gives Lorentz force via B_μ; mass-direction structure (from p^u via h_μu) gives a velocity-dependent metric-distortion contribution to the gravitational interaction. Both are real effects on particle motion; they are categorized differently by the wrap-order convention.

(This distinction parallels how standard general relativity categorizes geodesic-equation terms by their physical origin — diagonal metric perturbations from mass-energy density give gravitational attraction, while certain off-diagonal terms from mass-energy current give frame-dragging. The framework's wrap-order convention is what assigns h_μu to the gravity side rather than to the EM side.)

---

## 4. Alternative framings considered (superseded)

Before settling on the wrap-order-enforcement framing of §3, two alternative readings of the σ ≠ 0 situation were considered. They are recorded here briefly because the symmetric reading is the natural one to arrive at first, and seeing why it is superseded helps clarify what the wrap-order axiom is doing.

**Symmetric reading — U(1) × U(1) at σ ≠ 0.** Apply the four-property test symmetrically to both h_μu and h_μw. Both pass (by the bare-metric symmetry of the σ = 0 framework in (u, w)). Conclude that the σ ≠ 0 framework predicts a richer gauge structure than σ = 0 — two independent U(1) gauge potentials per closure-satisfying particle, with the particle carrying separate "charges" p^u and p^w. **Superseded** because this reading treats the four-property test as a *selection mechanism* applied symmetrically, ignoring the wrap-order convention's structural assignment. With the convention enforced at the gauge-identification level, only h_μw is a gauge potential by definition.

**Interpretation-(b) workaround — R_u-symmetrized as a small-σ perturbation.** Maintain the σ = 0 R_u-symmetrization construction at σ ≠ 0, accepting that it is no longer a stationary state. Compute T_tu for the time-averaged construction; it does not vanish at σ ≠ 0 but is σ-suppressed (proportional to Δω/ω·k_u). h_μu would then be a σ-suppressed second gauge potential rather than a full-strength one. **Superseded** because it (a) is well-defined only at small σ (the construction breaks down at large σ where the [Ch 9 §3](09-ratio-and-shear.md) σ → 1 mechanism operates), (b) contradicts the [Ch 8 §2.2](08-shear-and-fractional-charge.md) commitment to single-Bloch-mode interpretation, and (c) still treats h_μu as a (suppressed) gauge potential candidate rather than as a mass-direction metric perturbation — the underlying framing issue is unresolved.

Both alternatives illustrate the same point: without wrap-order enforcement at the gauge-identification level, the σ ≠ 0 framework would face a hard structural choice. With wrap-order enforcement, no choice is needed. The convention does the work the alternatives were trying to do via mechanism.

---

## 5. Recommendation — unified integration

The math is settled. Both σ = 0 (§2) and σ ≠ 0 (§3) derivations now run under one unified framing: the wrap-order convention selects h_μw as the gauge candidate, and the four-property test confirms h_μw satisfies standard-physics gauge-potential requirements in both regimes. No architectural decision is required.

### 5.1 Integrate into Ch 5 §4.6

The §2 derivation (Properties 1–4 at σ = 0) converts Ch 5 §4.6's *asserted* four-property claim into *derived* — the original TODO-M2 scope. Add a framing note at the start of Ch 5 §4.6 stating that h_μw is the gauge candidate by wrap-order convention (Ch 1 §10), and the test confirms it satisfies standard-physics gauge-potential requirements. Position the test as confirmation, not selection.

The §3 derivation extends Ch 5 §4.6 to σ ≠ 0. Three additions:

- The test on h_μw runs identically to σ = 0 — same Christoffel calculation, same Lorentz-force structure. h_μw is the gauge potential B_μ at both regimes.
- A new sub-subsection characterizing the h_μu contribution at σ ≠ 0 as a metric-distortion effect (frame-dragging-like, from the mass-direction structure), not a gauge force.
- Cross-reference Ch 8 §2.2's single-Bloch-mode commitment as the regime in which the h_μu contribution becomes nonzero.

Estimated work: half-day editing pass on Ch 5 §4.6. The Christoffel calculation goes in once; the σ ≠ 0 extension is a short addition characterizing the h_μu contribution.

### 5.2 Note in Ch 8 §2.2

Ch 8 §2.2's parenthetical that flagged TODO-M2 extension can be tightened: the surviving cross-term pattern (T_tu, T_tw, T_uw) at σ ≠ 0 under single-Bloch-mode does require the four-property test to be redone, but the wrap-order convention resolves the gauge-identification step cleanly. h_μw remains the single gauge potential; h_μu's contribution is characterized as a metric-distortion effect in Ch 5 §4.6's extended treatment.

This is a single sentence's worth of edit — replace the "the surviving cross-term pattern differs from the σ = 0 R_u-symmetrized version" sentence with a brief cross-reference to Ch 5 §4.6's σ ≠ 0 treatment.

### 5.3 Update STATUS

Mark TODO-M2 as **resolved** by the unified wrap-order-enforcement framing. The σ = 0 + σ ≠ 0 derivations integrate into Ch 5 §4.6 as a single derivation; no TODO-M2b is needed for the σ ≠ 0 extension as a separate item.

The cross-cutting observations table can drop the σ ≠ 0 extension as a separate concern; the unified derivation handles both regimes.

### 5.4 Why keep this file post-rework

work-m2.md remains valuable as the document that *surfaced* the framing question. The original symmetric reading (Properties 1–4 applied to both h_μu and h_μw, leading to U(1) × U(1)) was the natural first reading and was worth working through to see that the asymmetry has to be imported explicitly at the gauge-identification step. Future readers wondering "why doesn't σ ≠ 0 predict two gauge potentials?" will find this file's §4 the cleanest articulation of why the question dissolves under wrap-order enforcement.

---

## Notes on the math

The derivations in §§2–3 assume:
- The dimensional-reduction limit: h_μν depends only on extended-spacetime coordinates, not on u or w. Standard KK assumption.
- Linearized Einstein equations: T_μν sources h_μν via □ h_μν = −16π G T̄_μν per [Ch 5 §3](05-metric-self-consistency.md).
- Slow-motion limit for the geodesic equation: dx^ν/dτ ≈ v^ν, with v^ν the spacetime velocity.

These match the framework's existing scope. No additional assumptions are introduced.

The σ ≠ 0 calculation assumes that the single-Bloch-mode's stress-energy time-average correctly captures the perturbation's source. This is the standard reading consistent with [Ch 8 §2.2](08-shear-and-fractional-charge.md)'s commitment.
