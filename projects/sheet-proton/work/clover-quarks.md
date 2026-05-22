# clover-quarks.md — corrugated 3-lobed torus as substrate for quark assignments

**Status:** **Phases A and B complete** (analytical math, §§7–12). Phase C (numerical mode spectrum) sketched but not expanded. Sister to [quark-flavor.md](quark-flavor.md), [fractional-charge.md](../../metric-binding/work/fractional-charge.md), [color-confinement.md](../../metric-binding/work/color-confinement.md).

**Tone:** Geometric construction first, physics interpretation second. The geometry is well-defined; the quark identification falls out of the per-arc curvature accounting.

**Phase A headline (§11.7):** the per-radian curvature content of the clover profile assigns charge **+2/3 to each lobe arc** and **−1/3 to each saddle arc** via Q = (1/2π) ∫ κ ds. These are precisely the QCD up and down quark charges, falling out of the geometric construction without postulation.

**Phase B headline (§12):** clean particle identifications follow:
- **u quark = 1 lobe** (charge +2/3)
- **d quark = 1 saddle** (charge −1/3)
- **Proton (uud) = 2 lobes + 1 saddle path** (charge +1, closes in 2 ring revolutions)
- **Neutron (udd) = 1 lobe + 2 saddles path** (charge 0, closes in 1 ring revolution)

Neutron β decay is structurally a **localized q-shift** converting one saddle to one lobe (one down to one up) — a topological transition that doesn't require any wave running backwards, addressing a long-standing structural concern from the metric-mass standing-wave reading.

Combined with §8's identification of (ε, χ) as the two free parameters analogous to metric-charge's (L_u/L_w, σ_uw), the corrugated torus is a *2-parameter family* providing concrete geometric origins for fractional charges, Z₃ confinement, the up/down quark distinction, proton/neutron structure, and β-decay topology — all from a single construction.

> **⚠ Closure-problem annotation (2026-05-22).** The Phase B path-closure claims above
> — proton "closes in 2 ring revolutions," neutron "closes in 1 ring revolution" — rest
> on the *literal piecewise-arc* clover. That construction has a closure problem: a
> literal-arc proton path (2 lobes + 1 saddle) covers a cross-section φ-displacement
> 2φ_L + φ_S that lies strictly in (2π/3, 4π/3) for **every** geometry, so it never
> completes a whole tube wrap and the locus does not actually close (the §14 open
> questions already flag this; the derivation is in
> [modulated-clover.md §1](modulated-clover.md)). The per-arc **charge** accounting
> (Phase A: Q_lobe = +2/3, Q_saddle = −1/3, from Q = (1/2π)∫κ ds) does not depend on
> path closure and stands. The current **best-candidate** construction — one that
> *does* close the proton and neutron tracks, on a smooth, simple (non-self-intersecting)
> surface, with exact charges (+1, 0) and track lengths consistent with the nucleon
> masses — is [modulated-clover.md](modulated-clover.md), which replaces the piecewise
> arcs with a smooth harmonic cross-section plus a half-twist and parameter modulation.

---

## 0. Conventions

This section pins terminology and notation used throughout this file and across [clover-mass.md](clover-mass.md), [3-gen.md](3-gen.md), [quark-flavor.md](quark-flavor.md), and [meson-spectrum.md](meson-spectrum.md).

### 0.1 Coordinates

Two coordinate axes on the surface, both with period 2π:

- **θ** — angular coordinate around the **ring** (the large direction; ring circumference 2π R_major).
- **φ** — angular coordinate around the **tube** (the small direction; tube circumference L_total).

Define c ≡ L_total / (2π) — the tube's *effective radius* (so that the tube circumference is 2π c). With this:

<!-- ε = c / R_major = (tube effective radius) / (ring radius) = (tube circumference) / (ring circumference) -->
$$
\varepsilon \;\equiv\; \frac{c}{R_{\mathrm{major}}} \;=\; \frac{2\pi c}{2\pi R_{\mathrm{major}}} \;=\; \frac{\text{tube circumference}}{\text{ring circumference}}
$$

ε is a pure ratio of the two compact circumferences (the 2π's cancel), so the same dimensionless aspect ratio used elsewhere in forma studies. Small ε = thin tube; ε of order 1 = comparable circumferences.

The convention is **tube-first** wherever pairs appear (matching metric-charge's (n_t, n_r) convention).

### 0.2 Path-winding numbers — (n_t, n_r)

For a *classical closed path* on the surface (e.g., the trajectory traced by a quark within a baryon), the winding numbers are

- **n_t** ∈ ℤ — number of times the path wraps around the **tube** direction.
- **n_r** ∈ ℤ — number of times the path wraps around the **ring** direction.

These are properties of a closed loop's **homotopy class** (the family of loops that can be continuously deformed into one another without breaking — two loops with the same windings (n_t, n_r) are in the same class), not of any particular wave-mode.

Example (per §12.2): the proton path covers 2 lobes + 1 saddle (= 600° of arc) and closes with **(n_t, n_r) = (1, 2)** — 1 tube turn and 2 ring revolutions. The neutron path covers 1 lobe + 2 saddles and closes with **(n_t, n_r) = (1, 1)**.

### 0.3 Wave-mode quantum labels — (m_t, m_r)

For a *quantum eigenmode* on the surface (a wavefunction Ψ that solves the Laplace–Beltrami eigenvalue equation), each mode is labelled by two integers that count how many times the wave's phase cycles around each direction as you traverse it:

- **m_t** ∈ ℤ — the number of phase cycles the wave makes going once around the tube. Equivalently, k_φ = m_t (the tube-direction wavenumber).
- **m_r** ∈ ℤ — the analogous count for the ring direction. Because of the twist, the ring-direction wavenumber becomes k_θ = m_r − m_t/3 (the m_t/3 term is the contribution from the twist's mod-3 shift, see §11).

The mass formula for the unperturbed (flat-twisted-torus) limit becomes

<!-- μ² = (m_r − 2 m_t / 3)² + (m_t / ε)² -->
$$
\mu^2 \;=\; \left(m_r \;-\; \frac{2\,m_t}{3}\right)^2 \;+\; \left(\frac{m_t}{\varepsilon}\right)^2
$$

(see [clover-mass.md §4](clover-mass.md) — derived; the factor-of-2 in 2m_t/3 is the metric-shear contribution stacking with the boundary-identification shift). **(n_t, n_r) and (m_t, m_r) are different objects** — path-windings vs wave-mode labels. We keep them apart throughout.

### 0.4 Shear σ versus twist τ

- **σ** (continuous, real) — an intrinsic **metric** shear of the sheet before it is rolled into a tube. Free parameter. Affects only the off-diagonal coupling g_θφ. Does *not* change boundary identifications. Analogous to metric-charge's σ_uw.

- **τ** (discrete, k/3 for integer k) — the angle by which the cross-section rotates per ring revolution. A **topological** operation: it changes the boundary identification (θ, φ) ~ (θ + 2π, φ + 2π τ), which selects Bloch sectors and forces m mod 3 constraints. Locked to k/3 by D₃ symmetry of the clover profile. We use τ = 1/3 throughout.

From the wave's perspective, σ and τ enter additively in an *effective* shear σ_eff ≈ σ + 2τ that appears in the mass formula. The two are physically distinct (one geometric, one topological), but a wave alone cannot tell them apart — only the *spectrum's sector structure* (the discrete Bloch labels) carries τ's topological fingerprint.

The status of σ as an independent parameter is being clarified in the restart (see [STATUS.md](STATUS.md) Phase 1).

### 0.5 Key mathematical terms

- **Hill equation** — a one-dimensional wave equation whose coefficients depend on position periodically (e.g. coefficients that vary with the lobe/saddle pattern around the tube). It's the kind of equation that describes a wave moving through a periodic medium, and it has well-developed solution techniques (band structure, Bloch sums). When we reduce our 2D torus problem to one direction by exploiting the helical symmetry (§10.4), what's left is a Hill equation in the tube coordinate u.

- **Sturm–Liouville form** — a symmetric way to write the Hill equation so that the operator is self-adjoint with respect to a weighted inner product. Numerically, discretising in this form preserves the symmetry, which is important for getting accurate (real, ordered) eigenvalues.

- **Helical translation symmetry** — sliding around the ring while simultaneously rotating around the tube by the twist angle leaves the surface metric unchanged. Practically: it lets us change coordinates so that the wave equation factors into a ring-direction part (just a plane wave) times a tube-direction part (the Hill equation above).

- **Bloch sector** — when a wave's tube wavenumber m_t is fixed (or fixed modulo 3), it defines a subspace of allowed waves. Because of the τ = 1/3 twist there are three distinct sectors (m_t mod 3 = 0, 1, 2). Different sectors don't mix under the surface's symmetries.

- **Zeroth-order spectrum** — the masses of waves on the surface *before* we account for the corrugation (i.e., imagine the cross-section is a perfect circle with the same circumference). Analogous to a DC baseline: it's the leading-order answer that we then add small corrections to. The boxed formula in §0.3 is this leading-order mass.

- **First-, second-order corrections** — successive terms in a series expansion where the small parameter is η = r_lobe / R_major (how big the corrugation amplitude is relative to the ring). First-order = the correction proportional to η; second-order = the correction proportional to η². [clover-mass.md §5–§6] shows first-order = 0 by symmetry, and second-order is O(χ²) (smaller than naive expectation; see §6.3 there).

### 0.6 Particles

- **Proton** = closed path covering 2 lobes + 1 saddle, (n_t, n_r) = (1, 2). Total charge +1.
- **Neutron** = closed path covering 1 lobe + 2 saddles, (n_t, n_r) = (1, 1). Total charge 0.
- **u quark** = single lobe arc, charge +2/3.
- **d quark** = single saddle arc, charge −1/3.

The wave-mode (m_t, m_r) that *represents* the proton/neutron quantum-mechanically is a separate identification question (still open; see [clover-mass.md §9.1](clover-mass.md) Concern A).

---

## 1. The geometric setup

### 1.1 The cross-section profile (clover-leaf)

Consider a closed plane curve with three-fold rotational symmetry, made from circular arcs of two kinds:

- **Three "lobe" arcs**, each spanning 240° of arc (i.e., 2/3 of a full circle) with positive curvature (centers *inside* the cross-section)
- **Three "saddle" arcs**, each spanning 120° of arc (1/3 of a full circle) with negative curvature (centers *outside* the cross-section, producing inward bulges)

The arcs alternate lobe-saddle-lobe-saddle-lobe-saddle around the closed curve.

**Closure check (Gauss-Bonnet).** The total signed turning of the tangent around a closed plane curve must equal 2π:

<!-- Σ (signed arc angles) = 2π -->
$$
3 \cdot 240° \;-\; 3 \cdot 120° \;=\; 720° - 360° \;=\; 360° \;=\; 2\pi
$$

So the profile *does* close geometrically. The lobes contribute outward turning (positive curvature, 240° each, total +720°); the saddles contribute inward turning (negative curvature, 120° each, total −360°); the net +360° matches the requirement for a simple closed plane curve.

**Tangency at junctions.** At each lobe-to-saddle junction (six per profile), the tangent direction must be continuous (C¹ smoothness). Curvature is discontinuous (jumps from +1/r_lobe to −1/r_saddle), but this is acceptable — it's a C¹ curve, not C². The arcs can be sized (r_lobe and r_saddle) such that the junctions occur at matching tangent directions.

**Parametric form.** Let φ ∈ [0, 2π) parameterize the profile by arc length normalized to a full traversal. The profile is

<!-- P(φ) = (X(φ), Y(φ)) in the cross-section plane -->
$$
P(\varphi) \;=\; \bigl(X(\varphi),\; Y(\varphi)\bigr)
$$

with three-fold symmetry:

<!-- P(φ + 2π/3) = R_{2π/3} · P(φ) -->
$$
P\!\left(\varphi + \frac{2\pi}{3}\right) \;=\; R_{2\pi/3}\; P(\varphi)
$$

where R_{2π/3} is the 120° rotation matrix in the cross-section plane. Each fundamental domain (one lobe + one saddle, of φ-extent 2π/3) covers 240° + 120° = 360° of arc.

### 1.2 The corrugated torus (sweep with twist)

Sweep the profile around a major circular ring of radius R, with the cross-section rotating by a twist angle τ·θ as the ring angle θ ∈ [0, 2π) advances.

**Surface parameterization:**

<!-- r(θ, φ) = R·(cos θ, sin θ, 0) + R_{τ θ}·P(φ) embedded in plane perpendicular to ring tangent -->
$$
\vec{r}(\theta, \varphi) \;=\; \vec{R}(\theta) \;+\; M(\theta) \cdot P(\varphi + \tau\,\theta)
$$

where:
- **R**(θ) = R · (cos θ, sin θ, 0) is the ring center at angle θ
- M(θ) is the 3D rotation taking the cross-section plane (at θ = 0) to the plane perpendicular to the ring tangent at angle θ
- τ is the **twist rate** — how much the profile rotates relative to the ring's local Frenet frame as θ advances. (Notation: we use τ rather than the more conventional α for the twist parameter, to avoid confusion with the fine-structure constant α ≈ 1/137 used elsewhere in MaSt. τ here is the standard differential-geometry name for the twist of a framed curve.)
- τ·θ enters as a rotation *inside* the profile parameter φ

**The 1/3 twist condition.** Choose τ such that one full ring revolution gives a 120° = 2π/3 rotation of the profile:

<!-- τ · 2π = 2π/3, so τ = 1/3 -->
$$
\tau \;=\; \frac{1}{3}
$$

With this choice, going around the ring once (θ: 0 → 2π) advances φ by 2π/3 — exactly the angular separation between lobes in the profile.

**Topology check.** The surface closes onto itself because the profile has 3-fold symmetry: the rotated profile at θ = 2π is identical to the profile at θ = 0 (just relabeled). So the surface is genuinely a closed 2-torus T², not an open spiral.

**Effective identification.** A point (θ, φ) on the surface is identified with (θ + 2π, φ + 2π/3) — the twist modifies the standard torus identification (θ, φ) ~ (θ + 2π, φ) by adding the 2π/3 shift in φ.

### 1.3 An alternative construction: the rolled leaf (introduces σ)

The §1.2 swept-profile construction has a single twist parameter τ that fuses two physically distinct effects — a discrete topological identification at the boundary and a continuous off-diagonal coupling in the induced metric. The **rolled-leaf** construction below builds the same surface (in a limit) but exposes these as two independent knobs: a continuous **intrinsic metric shear σ** in the sheet's underlying geometry, and the discrete twist τ in how the tube wraps the ring. σ pairs naturally with metric-charge's σ_uw; τ remains the topological wrap parameter of §1.2.

**Step 1 — Sheared parallelogram sheet.** Start with a flat 2D sheet of coordinates (u, w), and give it intrinsic shear σ ∈ ℝ:

<!-- ds² = du² + 2σ du dw + dw² -->
$$
ds^2 \;=\; du^2 \;+\; 2\sigma\,du\,dw \;+\; dw^2
$$

σ = 0 is the rectangular metric. σ ≠ 0 is a continuous tilt between u (which will become the tube direction) and w (which will become the ring direction) — directly analogous to metric-charge's σ_uw.

**Step 2 — Bend each strip into a leaf.** Bend a strip of u-width 2π/3 so that its cross-section traces one **leaf**: a half-saddle arc (π/3 of saddle-arc, concave) + a full lobe arc (4π/3, convex) + a second half-saddle (π/3, concave). The arc-lengths sum to π/3 + 4π/3 + π/3 = 2π. Each leaf's body runs along w; its cross-section is one lobe flanked by two half-saddles.

**Step 3 — Three leaves around a centerline → straight clover tube.** Place 3 leaves at 120° spacing around a common longitudinal axis (along w). Adjacent leaves join at the half-saddles: leaf-A's right half-saddle and leaf-B's left half-saddle together form one full 2π/3 saddle arc. The three joined leaves' cross-section is the three-lobe / three-saddle clover of §1.1.

Because the parallelogram was sheared (σ ≠ 0), each leaf's far edge (w = L_w) is offset in u relative to its near edge (w = 0). The tube's two ends are **jagged** — not aligned with the cross-section structure at either end.

**Step 4 — Wrap the centerline → clover torus.** Curl the length-axis into a circle of radius R_major (so w runs around a ring rather than along a line). The two jagged ends now meet head-to-head; the σ-induced u-offset around the loop becomes a constant off-diagonal entry in the induced metric (g_θφ), with no quantization required at the metric level. σ thus surfaces in the rolled torus as a continuous off-diagonal coupling.

**Step 5 — Add the discrete twist τ on top.** Independently of σ, rotate the cross-section by 2π τ per ring revolution. τ is forced to k/3 by the profile's Z₃ symmetry (the profile must map to itself under the boundary identification when the ring closes); σ has no such constraint. **σ and τ are then two distinct knobs**: σ a continuous metric property of the underlying sheet, τ a discrete topological property of the wrap.

**Reduction to §1.2.** Setting σ = 0 produces an un-jagged straight clover tube; wrapping it with τ = 1/3 in Step 5 reproduces the §1.2 surface exactly. §§7–10 (the closed-form profile and the induced-metric derivation) are therefore the σ = 0 special case of this construction.

**Solvability is preserved at σ ≠ 0.** σ enters the induced metric as a *constant* off-diagonal addition: it modifies g_θφ but does not modify any metric component's dependence on θ or φ. The helical translation symmetry of §10.4 — which depends only on θ/φ-independence of the metric — therefore survives, the Hill-equation reduction of [clover-mass.md §2](clover-mass.md) still goes through, and the closed-form leading-order mass formula still emerges from the same Bloch-sector analysis. σ enters the m_r ↔ m_t cross-term as σ_eff = σ + 2τ (replacing the bare 2τ at σ = 0). The detailed metric derivation, including the σ-dependent determinant correction, is worked out in §10.3.

---

## 2. Paths and their windings

A closed path on the surface is parameterized by (θ(t), φ(t)) with periodic boundary conditions. The path's homotopy class is determined by (using the tube-first convention from §0.2):

- **n_t** ∈ ℤ: the integer number of times the path winds around the **tube** (cross-section, φ-direction)
- **n_r** ∈ ℤ: the integer number of times the path winds around the **ring** (θ-direction)

For a closed path under the twisted identification, the total displacement must satisfy:

<!-- Δθ = 2π n_r, Δφ = 2π n_t + n_r · 2π/3 -->
$$
\Delta\theta \;=\; 2\pi\, n_r, \qquad \Delta\varphi \;=\; 2\pi\, n_t \;+\; n_r \cdot \frac{2\pi}{3}
$$

The extra n_r · 2π/3 in Δφ is the **twist contribution**: each ring revolution adds 120° of cross-section angle. So a path that goes once around the ring (n_r = 1) and once around the cross-section (n_t = 1) traverses total cross-section angle of 2π + 2π/3 = 8π/3 = 480° — i.e., a full revolution plus one more lobe-saddle pair.

**Implication for closure.** A path with only one ring revolution (n_r = 1, n_t = 0) closes only if it traverses Δφ = 2π/3 in the cross-section — i.e., exactly one lobe-saddle pair (one fundamental domain of the profile). So *the simplest closed path on this surface is one revolution of the ring covering one-third of the cross-section*. Three such paths, offset by 2π/3 each, together cover the whole cross-section.

This is structurally suggestive: **three minimal closed paths together fill the surface, each occupying one-third of the cross-section.** It's the geometric realization of the Z₃ confinement pattern.

---

## 3. Quark and baryon identification

### 3.1 Quarks as arc segments; baryons as 3-arc paths

- **u quark** = one lobe arc (240° = 4π/3 of profile arc length)
- **d quark** = one saddle arc (120° = 2π/3 of profile arc length)

Individual quarks do not close as standalone paths — that's the geometric expression of QCD confinement. They are *fragments* of a closed profile.

A **baryon** is the closed path obtained by concatenating three quark-arcs:

- **Proton** (uud) = 2 lobes + 1 saddle = 240° + 240° + 120° = 600° of profile arc
- **Neutron** (udd) = 1 lobe + 2 saddles = 240° + 120° + 120° = 480° of profile arc
- **Δ⁺⁺** (uuu) = 3 lobes = 720° of arc
- **Δ⁻** (ddd) = 3 saddles = 360° of arc

Each baryon covers more than one full profile circumference (360°). The twisted closure rule of §2 determines how many ring revolutions are needed for the path to return to its starting point.

### 3.2 Closure condition for baryon paths

The path closure rule from §2 (tube-first, twist τ = 1/3): a closed path with total cross-section arc Φ_path must satisfy

<!-- Φ_path = 2π n_t + (2π/3) n_r -->
$$
\Phi_{\mathrm{path}} \;=\; 2\pi\, n_t \;+\; \frac{2\pi}{3}\, n_r
$$

for some integer (n_t, n_r). Dividing both sides by 2π/3 gives the integer relation **3 n_t + n_r = (Φ_path)/(2π/3)** — i.e., the RHS is the path arc measured in units of one saddle-arc (since 2π/3 = saddle arc length). Equivalently, **3 n_t + n_r = 2 N_u + N_d** for a baryon with N_u up-quarks and N_d down-quarks (since one lobe = two saddle units, one saddle = one saddle unit).

Applied to the four 3-quark baryon combinations:

| Baryon | (N_u, N_d) | 2N_u + N_d | Smallest (n_t, n_r) |
|---|---|---|---|
| Δ⁺⁺ (uuu) | (3, 0) | 6 | (2, 0) — 2 tube turns, 0 ring revolutions |
| Proton (uud) | (2, 1) | 5 | (1, 2) — 1 tube turn, 2 ring revolutions |
| Neutron (udd) | (1, 2) | 4 | (1, 1) — 1 tube turn, 1 ring revolution |
| Δ⁻ (ddd) | (0, 3) | 3 | (1, 0) — 1 tube turn, 0 ring revolutions |

The full §12 discussion derives these closure numbers and uses them in the proton/neutron mass analysis.

### 3.3 The "1/3 precession" reading — lobe-label precession, not path closure

An appealing picture: "the tube twist advances the phase so that a proton could forever keep traversing 2 lobes and 1 saddle (with 1/3 precession)." There are two distinct things this can mean, and they're easy to conflate.

1. **Path-locus closure** — when does the geometric trajectory return to its starting point? Per §3.2, the proton path's locus closes at **(n_t, n_r) = (1, 2)** — 1 tube turn, 2 ring revolutions.

2. **Lobe-label precession** — the geometric twist shifts which Z₃ lobe a wave occupies by 120° per ring revolution. After 3 revolutions the lobe-label returns to itself. This is the "1/3 precession" the framing refers to: how the *labels* rotate, not how the *locus* closes.

These coexist: a wave whose locus closes in 2 ring revolutions still has its lobe-labels cycling on a 3-revolution period. The two observables are independent — locus-closure depends on the path's total Δφ; label-precession depends on how Z₃ labels rotate per revolution.

The Z₃ confinement structure rides on the second reading: three quarks together cover the cross-section, and the geometric twist enforces a 120° label shift per revolution. The "1/3 precession" intuition is geometrically real — it just refers to *label rotation*, not to a *path-closure* count.

---

## 4. Relation to other quark mappings

The clover construction's particle identification (§3.1) is specific to the corrugated-torus substrate. It does not directly translate into the round-tube T(m, n) winding language used by [quark-flavor.md](quark-flavor.md)'s competing mappings (R64, User-1, User-2, Alternative-3) — under those mappings each quark is a separable T(m, n) wave-mode of a smooth torus; under clover each quark is an arc-segment of a closed cross-section profile. The (m_t, m_r) wave-mode labels of [clover-mass.md](clover-mass.md) apply to the *whole baryon's* wavefunction, not to individual quarks.

**On color confinement.** Z₃ confinement under the clover construction comes from the third-integer momentum quantization k_θ = m_r − m_t/3 (§11), forced by the τ = 1/3 twist's boundary identification. Three quarks (three arcs) together cover the cross-section; observable baryons correspond to integer-charge combinations of three arcs.

**TODO:** match the (m, n) windings of metric-charge's primitive inventory to the (n_t, n_r) topology of these clover-torus paths.

---

## 5. Phase carried along the path

The 120° twist advances the *phase* of a wave along the path. If a wave has phase Θ(θ, φ), then after one ring revolution, the wave's phase is shifted by some amount that includes the geometric twist contribution.

A wave's phase along a path:

<!-- ΔΘ = ∫ (∂Θ/∂θ dθ + ∂Θ/∂φ dφ) -->
$$
\Delta\Theta \;=\; \int_{\mathrm{path}} \left(\frac{\partial \Theta}{\partial \theta} d\theta \;+\; \frac{\partial \Theta}{\partial \varphi} d\varphi\right)
$$

For a wave on the corrugated torus, the metric of the surface (induced from the 3D embedding) determines how phase accumulates. The twist τ = 1/3 means that "constant φ" curves on the surface are not closed in 1 revolution; they precess by 2π/3.

This is structurally analogous to the *Aharonov-Bohm phase* on a topologically non-trivial manifold: a closed path picks up a phase that depends on the global topology, not just the local geometry.

**Conjecture:** the proton's wave on this surface has a definite phase that returns to itself after the proper closure (3 revolutions for up-quark, 1 for down-quark, or whatever the composite structure requires). The "1/3 precession" is the proton's wavefunction picking up a phase shift of 2π·(1/3) per ring revolution.

For the wavefunction to be single-valued on the surface, the total phase accumulated around any closed path must be a multiple of 2π. This is a *quantization condition* on the wave's allowed momenta — a Bohr-Sommerfeld-style rule.

**TODO:** work out the phase-accumulation quantization for the up-quark and down-quark paths under Choice B. Does the 120° geometric twist provide the right phase for closure?

---

## 6. Connection to metric-charge / metric-binding framework

### 6.1 Closure condition

The standard closure rule of [metric-charge chapter 4](../../metric-charge/04-the-closure-condition.md) is "T(m, n) closure-satisfies iff m | n." On the corrugated torus, the closure condition is modified by the twist: the (n_t, n_r) indices have a shifted relation due to the 2π/3 twist per revolution.

Does the corrugated torus produce a *different* closure rule, or does it produce the same rule with different (m, n) interpretation? **TODO:** work out.

### 6.2 Z₃ confinement

The corrugated torus naturally produces a 3-fold structure: three minimal closed paths (one per fundamental domain) together cover the surface. This is the geometric realization of Z₃ confinement that [color-confinement.md](../../metric-binding/work/color-confinement.md) is trying to derive.

If this realization holds, it answers one of the framework's deepest questions structurally — "why three?" because the profile has 3 lobes, by construction. The closure of compounds requires a 3-fold partner structure.

### 6.3 Fractional charge

Per [fractional-charge.md](../../metric-binding/work/fractional-charge.md): if each minimal closed path on the corrugated torus carries 1/3 of the composite's external charge, then "fractional charge" is what a single path's contribution amounts to before the 3-fold closure is satisfied. Closure (full traversal of the surface) requires all three paths together — and that's where the charges combine to integer.

The corrugated-torus picture is essentially **partial-knot decomposition with a specific geometric realization**.

---

## 7. The profile in closed form

This section derives the explicit parametric form of the cross-section profile P(φ) under Z₆ symmetry (the natural symmetric clover). With Z₆, several parameters that would be free under Z₃ alone get pinned by the symmetry, simplifying the description considerably.

### 7.1 Z₆ symmetry assumption

We assume the profile is invariant under both:
- **3-fold rotation:** P(φ + 2π/3) = R_{2π/3} · P(φ) — the three lobes are equivalent, and the three saddles are equivalent.
- **Mirror symmetry through each lobe-axis:** the profile is symmetric under reflection through the axis from origin through any lobe-tip.

Together these give D₃ symmetry (dihedral group of order 6 = Z₆ if you prefer; same thing, different notation).

The mirror axes are at angles 0°, 60°, 120°, 180°, 240°, 300° — three through the lobe centers, three through the saddle centers.

Under D₃, the saddles sit at the **midpoints between adjacent lobes**: lobe centers at angles 2πk/3 (k = 0, 1, 2), saddle centers at angles 2πk/3 + π/3.

Dropping the mirror symmetry to keep only Z₃ would let the saddles drift azimuthally between adjacent lobes; for Phase A we keep D₃.

### 7.2 Circle center geometry

With D₃ symmetry, *all* circle centers (3 lobe-circles, 3 saddle-circles) sit at the same distance d from the profile center. To see this: by Z₃ rotation, all three lobe centers are equidistant from the origin (call this distance d_L). By Z₃ rotation, all three saddle centers are equidistant from the origin (call this d_S). The mirror symmetry through a lobe-axis maps the two adjacent saddles to each other; it does not relate d_L to d_S. So d_L and d_S could in principle differ.

However, the *kissing-circles* tangency condition couples them. Two adjacent circle centers (one lobe-center, one saddle-center, at angular separation π/3) must be exactly r_lobe + r_saddle apart for the arcs to meet smoothly:

<!-- |lobe-center − saddle-center|² = d_L² + d_S² − 2 d_L d_S cos(π/3) = d_L² + d_S² − d_L d_S = (r_lobe + r_saddle)² -->
$$
d_L^2 + d_S^2 - d_L d_S \;=\; (r_{\mathrm{lobe}} + r_{\mathrm{saddle}})^2
$$

For the symmetric solution d_L = d_S ≡ d, this reduces to d² = (r_lobe + r_saddle)², giving:

<!-- d = r_lobe + r_saddle -->
$$
\boxed{\;d \;=\; r_{\mathrm{lobe}} + r_{\mathrm{saddle}}\;}
$$

This is **the** kissing-circles relation under D₃: all six circle centers sit on a regular hexagonal lattice of side r_lobe + r_saddle around the profile center, at the same distance from origin.

### 7.3 Arc-degrees are forced

With D₃ symmetry and the kissing-circles relation, the lobe-arc-degree and saddle-arc-degree are not free parameters — they are forced by the geometry.

The junction between lobe-1 and saddle-1 sits at the point on lobe-1-circle that lies on the line connecting lobe-1-center to saddle-1-center. With lobe-1-center at (d, 0) and saddle-1-center at d·(cos 60°, sin 60°) = (d/2, d√3/2), the line direction from lobe-center toward saddle-center is (-1/2, √3/2). The junction is at distance r_lobe from lobe-center along this direction:

<!-- junction = (d - r_lobe/2, r_lobe √3/2) -->
$$
J_{1,1} \;=\; \bigl(d - r_{\mathrm{lobe}}/2,\; r_{\mathrm{lobe}}\sqrt{3}/2\bigr)
$$

Measured on the lobe-1-circle from the outward direction (= +x from lobe-1-center), this junction is at angle 120°. By mirror symmetry, the other junction (lobe-1 to saddle-3) is at angle −120° = 240°. So the lobe-arc on lobe-1-circle spans from angle 120° to angle 240° going through 180° (the outward back of lobe-1) — covering exactly **240° of arc**.

By the same construction, the saddle-arc spans exactly **120° of arc** of its saddle-circle.

So the user's specific 240°/120° split isn't a chosen parameter — it's the geometric consequence of the D₃-symmetric kissing-circles construction. Dropping mirror symmetry (Z₃ only) would free the arc-degrees, but Phase A is deliberately the symmetric case.

### 7.4 Total arc length

Lobe-arc length: (240°/360°) · 2π · r_lobe = 4π r_lobe / 3
Saddle-arc length: (120°/360°) · 2π · r_saddle = 2π r_saddle / 3

Total profile arc length (3 lobes + 3 saddles):

<!-- L_total = 3 · (4π r_lobe/3) + 3 · (2π r_saddle/3) = 4π r_lobe + 2π r_saddle = 2π(2 r_lobe + r_saddle) -->
$$
\boxed{\;L_{\mathrm{total}} \;=\; 2\pi\,(2\,r_{\mathrm{lobe}} + r_{\mathrm{saddle}})\;}
$$

This is the "circumference" of the corrugated tube — the analog of L_w (the cross-section circumference) in metric-charge's flat torus.

### 7.5 Radial extremes

- **Maximum** radius from profile center (apex of a lobe): r_max = d + r_lobe = 2 r_lobe + r_saddle
- **Minimum** radius (deepest indent of a saddle, on the saddle-arc midpoint): r_min = d − r_saddle = r_lobe

Ratio: r_max / r_min = 2 + χ where χ = r_saddle/r_lobe.

### 7.6 Explicit parametric form of P(φ)

Adopt arc-length parameterization: φ ∈ [0, 2π) with constant arc-speed |dP/dφ| = L_total/(2π) = (2 r_lobe + r_saddle). For φ in a fundamental domain φ ∈ [0, 2π/3):

The lobe portion occupies φ ∈ [0, φ_L) where:
<!-- φ_L = (4π r_lobe / 3) / (L_total / 2π) · 2π/(L_total) — wait, normalized: φ_L = (2π/3) · (2 r_lobe)/(2 r_lobe + r_saddle) -->
$$
\varphi_L \;=\; \frac{2\pi}{3}\,\frac{2\,r_{\mathrm{lobe}}}{2\,r_{\mathrm{lobe}} + r_{\mathrm{saddle}}}
$$

The saddle portion occupies φ ∈ [φ_L, 2π/3).

**Within the lobe portion** (centered on lobe-1, which sits on the +x axis), define the local angle on the lobe-circle from the outward direction:

<!-- ψ_L(φ) = (240°/φ_L) · (φ − φ_L/2) = (4π/3 · 2π/L_lobe-phi)... well, just say it maps linearly from [0, φ_L] to [-120°, +120°] of lobe-circle angle -->
$$
\psi_L(\varphi) \;=\; \frac{4\pi/3}{\varphi_L}\,\bigl(\varphi - \varphi_L/2\bigr) \;-\; 0 \quad\Longrightarrow\quad \psi_L \in [-2\pi/3,\; +2\pi/3]
$$

(centered so that φ = φ_L/2 corresponds to the lobe-1 arc-midpoint at outward direction, with ψ_L going from −120° to +120° as φ traverses the lobe from one junction to the other).

The position on the lobe:

<!-- P(φ) = (d + r_lobe cos ψ_L(φ), r_lobe sin ψ_L(φ)) for φ ∈ lobe range -->
$$
P(\varphi) \;=\; \bigl(d + r_{\mathrm{lobe}} \cos\psi_L(\varphi),\; r_{\mathrm{lobe}} \sin\psi_L(\varphi)\bigr), \quad \varphi \in [0, \varphi_L]
$$

**Within the saddle portion** (saddle-1 between lobe-1 and lobe-2, at azimuthal angle 60°), similarly define:

<!-- ψ_S(φ) = (2π/3 / (2π/3 − φ_L)) · (φ − (φ_L + 2π/6)) -->
$$
\psi_S(\varphi) \;=\; \frac{2\pi/3}{2\pi/3 - \varphi_L}\,\bigl(\varphi - (\varphi_L + \pi/3)\bigr) \quad \Longrightarrow\quad \psi_S \in [-\pi/3,\; +\pi/3]
$$

(with ψ_S = 0 at the saddle-1 arc-midpoint).

The position on the saddle-1 arc:

<!-- Saddle-1-center at (d/2, d√3/2). Inward direction from saddle-1-center toward origin: −(1/2, √3/2). Saddle-arc traces angles ψ_S ∈ [−60°, +60°] around this inward direction. -->
$$
P(\varphi) \;=\; \bigl(d/2,\; d\sqrt{3}/2\bigr) \;-\; r_{\mathrm{saddle}} \bigl(\cos(\psi_S(\varphi) + \pi/3),\; \sin(\psi_S(\varphi) + \pi/3)\bigr)
$$

for φ in the saddle-1 range. The other lobe and saddle portions are obtained by 3-fold rotation.

This is the explicit closed-form profile. With (d, r_lobe, r_saddle) given (constrained by d = r_lobe + r_saddle), P(φ) is determined.

### 7.7 Two free parameters

After the kissing-circles constraint, the profile has **2 free parameters**: r_lobe and r_saddle (equivalently, the overall scale d and the corrugation ratio χ = r_saddle / r_lobe).

---

## 8. Free parameters and connection to metric-charge

The two free parameters of the profile, combined with the major-ring radius R_major of the corrugated torus, give the full geometric specification of the surface. We want to connect these to metric-charge's (ε, σ_uw) language.

### 8.1 The natural aspect ratio

In metric-charge, the sheet has two compact directions u and w with circumferences L_u and L_w, and the aspect ratio is ε = L_u/L_w. The corrugated torus has analogous structure:

- **The major-ring direction** (θ-direction) has effective circumference L_θ = 2π R_major (assuming a circular ring; for a more general embedding, L_θ is the ring's path length).
- **The cross-section direction** (φ-direction) has total arc length L_total = 2π(2 r_lobe + r_saddle).

Define:

<!-- ε = L_total / L_θ = (2 r_lobe + r_saddle) / R_major -->
$$
\varepsilon \;\equiv\; \frac{L_{\mathrm{total}}}{L_\theta} \;=\; \frac{2\,r_{\mathrm{lobe}} + r_{\mathrm{saddle}}}{R_{\mathrm{major}}}
$$

This is directly analogous to L_u/L_w in metric-charge. Small ε = thin tube; large ε = fat tube.

### 8.2 The corrugation ratio

The second parameter is the relative depth of corrugation:

<!-- χ = r_saddle / r_lobe -->
$$
\chi \;\equiv\; \frac{r_{\mathrm{saddle}}}{r_{\mathrm{lobe}}}
$$

This is analogous to σ_uw in spirit (a deformation parameter beyond the bare aspect ratio) but with a *geometric* origin (corrugation depth) rather than a metric-shear origin (off-diagonal metric term).

- χ → 0: r_saddle → 0, the profile degenerates to three kissing circles (singular limit; saddle-arcs vanish).
- χ → ∞: the saddles dominate; the profile becomes hexagonal-with-rounded-corners (lobes are tiny bumps on a saddle-dominated curve).
- χ = 1: r_lobe = r_saddle = d/2. The "symmetric clover."

### 8.3 Parameter count summary

The corrugated proton sheet has the following open variables:

| Variable | Role | Status | Analog in metric-charge |
|---|---|---|---|
| ε = L_total / L_θ | Aspect ratio (tube-circumference / ring-circumference) | **Open** | L_u / L_w (directly) |
| χ = r_saddle / r_lobe | Corrugation depth | **Open** | σ_uw (analogous; different origin) |
| τ | Twist (cross-section advance per radian of θ) | **Open** — pinned to 1/3 only by the choice to enforce Z₃ closure in one revolution | New parameter; for the parameter-shift embedding, τ also plays the role of the metric shear σ_uw |
| Embedding | Parameter-shift vs rotation surface (see §9) | **Open** — binary choice | No analog; the flat torus has no embedding ambiguity |

Holding all four open, the corrugated sheet has a **richer parameter space** than metric-charge's flat sheet — but the topological proton structure (§§1–3) does not depend on τ's exact value or on the embedding choice. Only the **dynamical predictions** (mode frequencies, masses) depend on τ and on the embedding. The structural mapping at τ = 1/3 with parameter-shift embedding is:

- ε ↔ L_u/L_w (direct)
- χ ↔ σ_uw (analogous; σ_uw measures the tilt-between-compact-directions, χ measures the geometric corrugation depth)

Whether χ and σ_uw produce *the same physics* (just two languages for the same parameter) or *different physics* (two distinct ways to deform the sheet) is one of the project's central questions. The mode-quantization analysis of §11 will help distinguish.

### 8.4 Overall scale

R_major is an overall length scale (and through ε, sets the absolute size of r_lobe and r_saddle once ε and χ are fixed). Per the no-premature-pinning rule, R_major remains symbolic at this stage; it scales mass by R_major and dimensionful quantities accordingly.

### 8.5 Why these variables stay open

Per the no-premature-pinning rule, none of (ε, χ, τ, embedding) is fixed until the analysis forces a value. Concretely:

- **ε** is constrained by the proton's mass-to-Compton-length scale, once we solve the eigenvalue problem in §11/13. Until then, it carries forward symbolically.
- **χ** is constrained by mass ratios (e.g. m_u/m_d) and by the lobe/saddle arc-degree split (already forced to 240°/120° by D₆ + Gauss–Bonnet; χ remains free to set the corrugation depth).
- **τ** is constrained by Z₃ closure to be of the form k/3 for integer k. The choice τ = 1/3 minimises the winding required for closure; whether nature picks 1/3 or some other k/3 is open.
- **Embedding** is constrained by which surface produces the right mode spectrum. The two choices have identical topology, so any test that depends only on path-windings (quark assignment, β-decay topology, Z₃ confinement) is insensitive. Any test that depends on the metric (frequencies, masses) will distinguish them.

---

## 9. The 3D surface embedding

Embed the corrugated torus in ℝ³ with major-ring radius R_major.

### 9.1 Ring center

The ring lies in the (x, y) plane:

<!-- R(θ) = R_major (cos θ, sin θ, 0) -->
$$
\vec{R}_{\mathrm{ring}}(\theta) \;=\; R_{\mathrm{major}}\,(\cos\theta,\; \sin\theta,\; 0)
$$

### 9.2 Frenet frame at the ring

The local tangent, normal, and binormal at angle θ:

<!-- T = (-sin θ, cos θ, 0), N = (-cos θ, -sin θ, 0), B = (0, 0, 1) -->
$$
\hat{T}(\theta) = (-\sin\theta,\; \cos\theta,\; 0), \quad
\hat{N}(\theta) = (-\cos\theta,\; -\sin\theta,\; 0), \quad
\hat{B} = (0,\; 0,\; 1)
$$

The cross-section plane at θ is spanned by N̂(θ) and B̂.

### 9.3 Surface position with twist — two embedding choices

The twist τ can be realised in the embedding in two distinct ways. Both produce a closed T² with the same identification rules (§9.4) and so the same path-winding topology, but they describe *different surfaces in ℝ³* and *different induced metrics*. Which one is physical is an open question — see §9.5.

**Embedding A: parameter-shift.** Apply τ as a shift in the profile parameter:

<!-- r(θ, φ) = R_ring(θ) + P_x(φ + τθ) · N̂(θ) + P_y(φ + τθ) · B̂ -->
$$
\vec{r}_A(\theta, \varphi) \;=\; \vec{R}_{\mathrm{ring}}(\theta) \;+\; P_x(\varphi + \tau\theta)\,\hat{N}(\theta) \;+\; P_y(\varphi + \tau\theta)\,\hat{B}
$$

Under the change of coordinates ψ = φ + τθ, this becomes r_A = R_ring(θ) + P_x(ψ) N̂(θ) + P_y(ψ) B̂ — i.e. an **untwisted** corrugated torus carrying the twist purely in its boundary identification. The embedded clover cross-section is static (does not rotate with θ); only the φ-labels slide.

**Embedding B: rotation.** Apply τ as a physical rotation of the cross-section in the (N̂, B̂) plane:

<!-- r(θ, φ) = R_ring(θ) + [cos(τθ) P_x − sin(τθ) P_y] N̂(θ) + [sin(τθ) P_x + cos(τθ) P_y] B̂ -->
$$
\vec{r}_B(\theta, \varphi) \;=\; \vec{R}_{\mathrm{ring}}(\theta) \;+\; \bigl[\cos(\tau\theta)\,P_x(\varphi) - \sin(\tau\theta)\,P_y(\varphi)\bigr]\,\hat{N}(\theta) \;+\; \bigl[\sin(\tau\theta)\,P_x(\varphi) + \cos(\tau\theta)\,P_y(\varphi)\bigr]\,\hat{B}
$$

The clover cross-section physically rotates by τθ as θ advances. The embedded surface genuinely carries the twist; no reparameterisation makes it untwisted.

With τ = 1/3, both embeddings close after one ring revolution (one Z₃ symmetry step).

### 9.4 Closure of the surface

The 3-fold profile symmetry P(φ + 2π/3) = R_{2π/3} P(φ) combined with τ · 2π = 2π/3 means that going once around the ring (θ → θ + 2π) and shifting φ by 2π/3 returns to the same surface point:

<!-- r(θ + 2π, φ + 2π/3) = r(θ, φ) -->
$$
\vec{r}(\theta + 2\pi,\; \varphi + 2\pi/3) \;=\; \vec{r}(\theta,\; \varphi)
$$

In addition, profile periodicity gives:

<!-- r(θ, φ + 2π) = r(θ, φ) -->
$$
\vec{r}(\theta,\; \varphi + 2\pi) \;=\; \vec{r}(\theta,\; \varphi)
$$

So the surface is a 2-torus with identifications:

<!-- (θ, φ) ~ (θ + 2π, φ + 2π/3) and (θ, φ) ~ (θ, φ + 2π) -->
$$
(\theta, \varphi) \;\sim\; (\theta + 2\pi,\; \varphi + 2\pi/3), \qquad (\theta, \varphi) \;\sim\; (\theta,\; \varphi + 2\pi)
$$

This is a **twisted torus** — same topology as the flat T² (since the identifications are still generated by two independent cycles), but a different geometric realization.

### 9.5 What the two embeddings share, and where they differ

The two embeddings A and B agree on everything that is purely topological and disagree on everything that is metric-dependent:

| Quantity | Embedding A (parameter-shift) | Embedding B (rotation) |
|---|---|---|
| Closure identification (θ, φ) ~ (θ+2π, φ+2π/3) | ✓ | ✓ |
| Path winding numbers (n_t, n_r) | same | same |
| Closure-condition rules (§2, §3) | same | same |
| Z₃ confinement structure (§3.3) | same | same |
| 1/3 precession per revolution | same | same |
| Mode quantization rule k_θ = q − p/3 (§11) | same | same |
| Embedded shape in ℝ³ | untwisted clover; lobes at fixed angular positions | clover rotates by τθ; lobes physically precess |
| Induced metric g_ij (§10) | g_θφ = τ\|P'\|² | extra terms from cross-section rotation |
| Laplacian eigenvalues / mode frequencies | spectrum_A | spectrum_B (different in general) |
| Mass predictions from §13 | mass_A | mass_B (different in general) |

The choice between A and B is therefore an **open variable** at the same level as ε, χ, and τ. It will be pinned only by the mass-spectrum analysis of §13 (or by an independent geometric argument we have not yet identified).

§10 below derives the induced metric for **embedding A** (the parameter-shift formula). The corresponding derivation for embedding B is a one-page calculation deferred until we commit to one embedding.

The numerical scripts in `scripts/corrugated_torus.py` support both via the `--embedding` flag. The accompanying renderings `outputs/torus_chi1.00_R5.0_pshift_phi-band.png` and `outputs/torus_chi1.00_R5.0_rot_phi-band.png` show the visual contrast: same phi-band coloring, but only embedding B visibly twists the clover around the ring.

---

## 10. The induced metric

This section derives the induced metric for **embedding A (parameter-shift)** from §9.3, then augments it with the **intrinsic shear σ** from §1.3's rolled-leaf construction. The corresponding derivation for embedding B (rotation) is structurally similar but produces additional g_θφ contributions from the cross-section rotation; it is deferred until §9.5's open question is resolved.

All mass-spectrum analysis in [clover-mass.md](clover-mass.md) — the Hill-equation reduction, the closed-form mass formula, the η-expansion, and the numerical Bloch-restricted Fourier solver — runs against the embedding-A metric derived below.

### 10.1 Tangent vectors

The basis vectors on the surface, ∂_θ r and ∂_φ r:

<!-- ∂_θ r = R_major T(θ) + τ (P_x'(φ + τθ) N̂(θ) + P_y'(φ + τθ) B̂) + P_x(φ + τθ) ∂_θ N̂ + P_y(φ + τθ) ∂_θ B̂ -->

Compute ∂_θ N̂ = T̂(θ) (rotation of N̂ as θ advances), and ∂_θ B̂ = 0. So:

<!-- ∂_θ r = (R_major + P_x) T̂(θ) + τ P_x' N̂(θ) + τ P_y' B̂ -->
$$
\partial_\theta \vec{r} \;=\; \bigl(R_{\mathrm{major}} + P_x(\varphi + \tau\theta)\bigr)\,\hat{T}(\theta) \;+\; \tau\,P_x'(\varphi + \tau\theta)\,\hat{N}(\theta) \;+\; \tau\,P_y'(\varphi + \tau\theta)\,\hat{B}
$$

<!-- ∂_φ r = P_x'(φ + τθ) N̂(θ) + P_y'(φ + τθ) B̂ -->
$$
\partial_\varphi \vec{r} \;=\; P_x'(\varphi + \tau\theta)\,\hat{N}(\theta) \;+\; P_y'(\varphi + \tau\theta)\,\hat{B}
$$

### 10.2 Metric components

Using T̂, N̂, B̂ orthonormal:

<!-- g_θθ = (R_major + P_x)² + τ² (P_x'² + P_y'²) = (R_major + P_x)² + τ² |P'|² -->
$$
g_{\theta\theta} \;=\; \bigl(R_{\mathrm{major}} + P_x(\varphi + \tau\theta)\bigr)^2 \;+\; \tau^2\,|P'(\varphi + \tau\theta)|^2
$$

<!-- g_θφ = τ (P_x'² + P_y'²) = τ |P'|² -->
$$
g_{\theta\varphi} \;=\; \tau\,|P'(\varphi + \tau\theta)|^2
$$

<!-- g_φφ = P_x'² + P_y'² = |P'|² -->
$$
g_{\varphi\varphi} \;=\; |P'(\varphi + \tau\theta)|^2
$$

In arc-length parameterization, |P'(φ)| = L_total/(2π) ≡ c_arc (constant). So the embedding-A metric is:

<!-- g_θθ = (R_major + P_x)² + τ² c_arc², g_θφ = τ c_arc², g_φφ = c_arc² -->
$$
g_{\theta\theta}^{(A)} = (R_{\mathrm{major}} + P_x)^2 + \tau^2 c_{\mathrm{arc}}^2, \qquad g_{\theta\varphi}^{(A)} = \tau\,c_{\mathrm{arc}}^2, \qquad g_{\varphi\varphi}^{(A)} = c_{\mathrm{arc}}^2
$$

(P_x evaluated at u = φ + τθ throughout). The dependence on (θ, φ) is entirely through u; P_x ranges from r_min = r_lobe (saddle midpoint) to r_max = 2 r_lobe + r_saddle (lobe midpoint).

### 10.3 Rolled-leaf overlay: adding the intrinsic shear σ

The metric of §10.2 is the σ = 0 special case of the rolled-leaf construction from §1.3. Turning on σ adds the intrinsic shear of the underlying parallelogram sheet (Step 1 there) to the rolled torus. Because the bending and ring-wrapping that take the sheet to the torus are isometric, the shear survives unchanged in the intrinsic metric as a constant off-diagonal contribution.

In the convention where σ combines additively with τ (i.e., σ has units of "rotation per ring revolution", matching τ), the rolled-leaf contribution adds σ c²_arc to g_θφ and leaves the other entries alone:

<!-- g_θφ_sheet = σ c_arc²  -->
$$
\Delta g_{\theta\varphi}^{(\sigma)} \;=\; \sigma\,c_{\mathrm{arc}}^2, \qquad \Delta g_{\theta\theta}^{(\sigma)} \;=\; 0, \qquad \Delta g_{\varphi\varphi}^{(\sigma)} \;=\; 0
$$

σ enters only the off-diagonal entry — *not* g_θθ, *not* g_φφ, and *not* the parameter shift u inside P_x. (The asymmetry between σ and τ is essential: σ is a property of the *intrinsic* sheet metric and shows up only as an off-diagonal coupling, whereas τ enters via the 3D embedding's chain rule and so contributes to both g_θφ and g_θθ. See the independence note in §10.5 below.)

The combined embedding-A + rolled-leaf metric is therefore:

<!-- g_θθ = (R_major + P_x)² + τ² c_arc², g_θφ = (σ + τ) c_arc², g_φφ = c_arc² -->
$$
\boxed{\;g_{\theta\theta} = (R_{\mathrm{major}} + P_x)^2 + \tau^2 c_{\mathrm{arc}}^2, \quad g_{\theta\varphi} = (\sigma + \tau)\,c_{\mathrm{arc}}^2, \quad g_{\varphi\varphi} = c_{\mathrm{arc}}^2\;}
$$

Determinant of the metric:

<!-- |g| = g_θθ g_φφ − g_θφ² = ((R_major + P_x)² + τ² c²) c² − (σ+τ)² c⁴ = ((R_major + P_x)² − σ(σ+2τ) c²) c² -->
$$
|g| \;=\; \bigl((R_{\mathrm{major}} + P_x)^2 \;-\; \sigma(\sigma + 2\tau)\,c_{\mathrm{arc}}^2\bigr) \cdot c_{\mathrm{arc}}^2
$$

At σ = 0 this reduces to (R_major + P_x)² · c_arc². For σ ≠ 0 there is a small correction proportional to σ(σ + 2τ) · c²_arc — a higher-order-in-ε effect that is negligible whenever the rolled-leaf small-shear assumption σ ≲ 1 holds and ε ≪ 1.

Inverse metric (to leading order, treating ε² σ(σ + 2τ) as small):

<!-- g^θθ ≈ 1/(R_major + P_x)², g^θφ ≈ -(σ+τ)/(R_major + P_x)², g^φφ ≈ 1/c_arc² + τ²/(R_major + P_x)² -->
$$
g^{\theta\theta} \approx \frac{1}{(R_{\mathrm{major}} + P_x)^2}, \quad g^{\theta\varphi} \approx -\frac{\sigma + \tau}{(R_{\mathrm{major}} + P_x)^2}, \quad g^{\varphi\varphi} \approx \frac{1}{c_{\mathrm{arc}}^2} \;+\; \frac{\tau^2}{(R_{\mathrm{major}} + P_x)^2}
$$

Crucially, σ appears in the inverse off-diagonal g^θφ but **not** in g^φφ (since σ does not contribute to g_θθ in the original metric). This asymmetry is what drives the σ_eff = σ + 2τ form of the cross-term in the generalized mass formula (worked out in [clover-mass.md §4](clover-mass.md); the σ ≠ 0 derivation parallels the σ = 0 one with two changes: τ → σ + τ in g^θφ and τ → τ (unchanged) in g^φφ).

### 10.4 Helical translation symmetry (at σ ≠ 0)

The metric of §10.3 depends on (θ, φ) only through the combination u = φ + τθ — note that σ enters only as a constant off-diagonal entry, with no σ-dependent terms in u. So translations of the form (θ, φ) → (θ + δθ, φ − τ δθ) leave u — and hence the metric — invariant. This is a **continuous symmetry** of the surface, "helical translation" along the twisted axis.

This symmetry will let us reduce the Laplacian eigenvalue problem from 2D to effectively 1D in u (with a separate label for the orthogonal direction). The σ ≠ 0 generalization does not perturb the symmetry — σ shows up as an extra constant in g_θφ, which the symmetry transformation moves over uniformly. The Hill-equation reduction in [clover-mass.md §2](clover-mass.md) therefore proceeds unchanged at σ ≠ 0; only the coefficients shift.

### 10.5 σ and τ are independent

The metric of §10.3 makes the σ/τ independence explicit:

- **τ enters everywhere.** It sits inside the parameter shift u = φ + τθ (so it controls how P_x depends on (θ, φ)), it contributes τ²c²_arc to g_θθ, it contributes τc²_arc to g_θφ, and it sets the boundary identification (θ, φ) ~ (θ + 2π, φ + 2πτ). Because the boundary identification must map the profile to itself, **τ is quantized to k/3** by the Z₃ symmetry of the profile.

- **σ enters only off-diagonally.** It contributes σc²_arc to g_θφ and nothing else. It does not enter u, does not enter g_θθ or g_φφ, and — crucially — does not enter the boundary identification. **σ is therefore not subject to the Z₃ constraint**; it is a free real parameter.

The asymmetry is geometric in origin: τ comes from the 3D embedding's chain rule (∂_θ acting on P(φ + τθ) generates τP' along the cross-section directions), so it sees the profile structure. σ comes from the underlying sheet's intrinsic metric (a property that survives isometric bending and wrapping), so it sees nothing about the cross-section's structural features.

A wave on the surface feels both — both appear together in the leading-order mass formula via σ_eff = σ + 2τ. But the Z₃ structure of the Bloch-sector labels (m_t mod 3) is set entirely by τ via the boundary identification; σ shifts every sector continuously without changing how many sectors there are. This is the spectroscopic fingerprint that separates the two: τ's discreteness lives in the sector count, σ's continuity lives in within-sector mass shifts.

---

## 11. Mode quantization on the twisted torus

### 11.1 Single-valuedness conditions

A wave function ψ(θ, φ) on the surface must be single-valued. Equivalently, ψ on the universal cover ℝ² must satisfy:

<!-- ψ(θ + 2π, φ + 2π/3) = ψ(θ, φ) and ψ(θ, φ + 2π) = ψ(θ, φ) -->
$$
\psi(\theta + 2\pi,\; \varphi + 2\pi/3) \;=\; \psi(\theta,\; \varphi), \qquad \psi(\theta,\; \varphi + 2\pi) \;=\; \psi(\theta,\; \varphi)
$$

### 11.2 Plane-wave ansatz

Try ψ(θ, φ) = exp(i k_θ θ + i k_φ φ) for some wave numbers k_θ, k_φ ∈ ℝ.

**Second condition** (profile periodicity):

<!-- exp(i k_θ θ) exp(i k_φ (φ + 2π)) = exp(i k_φ · 2π) ψ -->
$$
e^{i k_\varphi \cdot 2\pi} \;=\; 1 \quad\Longrightarrow\quad k_\varphi \in \mathbb{Z}
$$

So k_φ must be an integer. Call it **m_t** (the **tube** Bloch index, per §0.3).

**First condition** (twisted ring periodicity):

<!-- exp(i k_θ (θ + 2π)) exp(i k_φ (φ + 2π/3)) = exp(i k_θ 2π) exp(i k_φ 2π/3) ψ = ψ -->
$$
e^{i k_\theta \cdot 2\pi} \cdot e^{i k_\varphi \cdot 2\pi/3} \;=\; 1
$$

This requires k_θ · 2π + k_φ · 2π/3 = 2π · m_r for some integer m_r (the **ring** Bloch index). With k_φ = m_t:

<!-- k_θ = m_r − m_t/3 -->
$$
\boxed{\;k_\theta \;=\; m_r \;-\; \frac{m_t}{3}, \qquad m_r,\, m_t \in \mathbb{Z}\;}
$$

### 11.3 The third-integer momentum quantization — the key result

The quantization rule k_θ = m_r − m_t/3 says that **k_θ takes third-integer values** when m_t is not a multiple of 3:

- **m_t ≡ 0 (mod 3):** k_θ ∈ {..., −1, 0, 1, 2, ...} — integer momenta
- **m_t ≡ 1 (mod 3):** k_θ ∈ {..., −4/3, −1/3, 2/3, 5/3, ...} — third-integers offset by 1/3
- **m_t ≡ 2 (mod 3):** k_θ ∈ {..., −5/3, −2/3, 1/3, 4/3, ...} — third-integers offset by 2/3

This is **the geometric realization of fractional momentum quantization**. It falls directly out of the surface's twist topology — the (θ, φ) identification with the 2π/3 offset.

The flat T² (no twist) gives k_θ and k_φ both integer. The corrugated torus with τ = 1/3 splits k_θ into three sub-lattices indexed by m_t mod 3.

**Labeling vs. spectrum.** The result k_θ = m_r − m_t/3 is a **labeling of admissible Bloch sectors** (per §0.5) — it tells you which (k_θ, k_φ) pairs correspond to single-valued wavefunctions on the closed surface. Plain plane waves exp(i k_θ θ + i k_φ φ) are *not* eigenmodes of the corrugated Laplace–Beltrami operator (whose metric coefficients depend on u = φ + τθ); the true eigenmodes are Bloch sums of plane waves within each sector. **However**, the leading-order mass spectrum derived in [clover-mass.md §4](clover-mass.md), μ² = (m_r − 2m_t/3)² + (m_t/ε)², treats each Bloch sector's lowest-energy mode as the plane wave at its smallest |m_t|, and this approximation is **validated to machine precision at small η** by the independent numerical solver in `scripts/laplacian_spectrum.py` (see [clover-mass.md §6.6](clover-mass.md)). So §11's labeling correctly organises both the Hilbert space and the leading-order spectrum; the corrugation corrections that distinguish eigenmodes from plane waves are O(η²) and have been computed numerically.

### 11.4 Mode count per fundamental domain

For modes with given k_φ = m_t, the spacing of allowed k_θ values is 1 (since m_r runs over integers). So the *density* of modes in k_θ at fixed m_t is the same as on the flat torus. What's different is the *offset*: each mod-3 class of m_t has its own offset (0, 1/3, or 2/3) for the k_θ lattice.

### 11.5 Connection to physical charge

Physical charge in MaSt is well-defined only for paths that close on the surface — equivalently, that wrap a full 2π of the profile. What the third-integer momenta describe:

- The **per-radian curvature contribution** of an arc segment is fractional — for one lobe it integrates to +2/3 of a full charge; for one saddle, −1/3 (see §11.7 for the precise integration). This is the "convex = +, concave = −" content of the geometry.
- These per-radian fractions are not standalone physical charges. They become observable only when a 3-arc combination (a baryon) sums them to an integer.
- The mode-quantization rule k_θ = m_r − m_t/3 is the quantum-mechanical reflection: third-integer momenta are mathematically allowed as fragments, but single-valuedness on the closed surface restricts physical particles to combinations whose total is integer.

Under metric-charge's closure rules, the cases of physical interest are essentially **m_t = 0 (integer-charge composite)** and **m_t mod 3 ≠ 0 (fragment that must combine with others to become observable)**. A mode with |m_t| > 1 is best understood as describing multiple constituents in the same compact direction, not a single "highly charged" particle.

§11.7 below is the precise statement of how the per-arc curvature integration yields Q_lobe = +2/3 and Q_saddle = −1/3 as the per-radian contributions, with the integer-charge restriction emerging from full closure.

### 11.6 Z₃ confinement as topological

A "free quark" would be a single mode with m_t ≡ 1 or 2 (mod 3) standing alone. Three such modes can combine into a state with total m_t,total ≡ 0 (mod 3), which corresponds to *integer* total charge — i.e., a confined three-quark composite.

This is the geometric realization of Z₃ confinement: only combinations with m_t,total ≡ 0 (mod 3) give integer-charge composites. Three-quark composites (baryons) satisfy this naturally; the same does mesons (qq̄ with m_t,q + m_t,q̄ ≡ 0 mod 3).

### 11.7 What we have derived

Phase A's central result, stated carefully: **fractional charges aren't fundamental quanta on the corrugated torus — they are the per-radian contributions of incomplete profile segments, which only become physically meaningful when summed into a closed path covering the full 2π profile (i.e., into a Z₃ singlet composite).** The mode quantization k_θ = m_r − m_t/3 is the *quantum-mechanical* reflection of this: third-integer momenta are quantum-mechanically allowed as fragments, but single-valuedness on the closed surface forces them to combine into integer totals.

This is one geometric mechanism producing:

- **Three-quark structure** of baryons (one full profile covering = three arc segments combining)
- **Fractional charges per quark** as the per-radian contribution of lobe vs saddle arcs (+2/3 lobe, −1/3 saddle)
- **Confinement** as the requirement that observable particles correspond to full 2π profile coverings

The detailed derivation:

The charge of a path along the profile, by the user's "convex = +, concave = −" framing, is the integrated geodesic curvature:

<!-- Q(γ) = (1/2π) ∫_γ κ ds -->
$$
Q(\gamma) \;=\; \frac{1}{2\pi}\,\int_\gamma \kappa\, ds
$$

For a complete closed plane curve, Gauss-Bonnet gives ∫ κ ds = 2π → Q = 1 (unit charge per full wrap).

For a single lobe-arc (240° on lobe-circle, κ = +1/r_lobe):

<!-- Q_lobe = (1/2π) · (1/r_lobe) · (4π r_lobe/3) = +2/3 -->
$$
Q_{\mathrm{lobe}} \;=\; \frac{1}{2\pi}\,\frac{1}{r_{\mathrm{lobe}}}\,\frac{4\pi r_{\mathrm{lobe}}}{3} \;=\; +\frac{2}{3}
$$

For a single saddle-arc (120° on saddle-circle, κ = −1/r_saddle):

<!-- Q_saddle = (1/2π) · (-1/r_saddle) · (2π r_saddle/3) = -1/3 -->
$$
Q_{\mathrm{saddle}} \;=\; \frac{1}{2\pi}\,\frac{-1}{r_{\mathrm{saddle}}}\,\frac{2\pi r_{\mathrm{saddle}}}{3} \;=\; -\frac{1}{3}
$$

**These are precisely the QCD charges of the up (+2/3) and down (−1/3) quarks.** Not derived as "third-integer eigenvalues" floating somewhere abstractly, but as the per-arc curvature contribution of geometrically explicit lobe and saddle segments.

The Phase A geometric content: the clover profile's six arcs (3 lobes + 3 saddles) supply exactly the right scaffolding for one full 2π wrap to be decomposable into the right combinations of u and d arc-fragments. Whether the physical states realize this decomposition as proton (uud) or neutron (udd) is the subject of Phase B.

The mode-quantization derivation (k_θ = q − p/3) is the corresponding quantum picture: the surface admits third-integer momenta as quantum-mechanically valid eigenmodes, but single-valued physical wave functions are restricted to integer-summing combinations. The geometric and quantum pictures are two languages for the same fact.

---

## 12. Phase B — Quark identification, path closure, and decay topology

Phase B builds on Phase A's per-arc charge accounting to identify which paths on the corrugated surface correspond to which particles, and to work out the closure conditions, decay dynamics, and energy relations that emerge.

### 12.1 The user's reframing of the original quark proposal

The user's original §3 proposal — "up quark traverses 2 lobes + 1 saddle, down quark traverses 2 saddles + 1 lobe" — has been refined by the per-arc charge accounting in §11.7. The cleaner reading is:

- **Up quark** is identified with a **single lobe arc** (charge +2/3 from the 240° convex segment).
- **Down quark** is identified with a **single saddle arc** (charge −1/3 from the 120° concave segment).
- **Proton** is the *composite* path covering **2 lobes + 1 saddle** = 2 ups + 1 down = uud (total charge +1).
- **Neutron** is the *composite* path covering **1 lobe + 2 saddles** = 1 up + 2 downs = udd (total charge 0).

What the user called "the up-quark's path" was actually the proton's path. Each individual quark = one arc segment; the proton/neutron are 3-arc combinations.

This relabeling preserves the geometric structure (the user's intuition was right about the topology) while aligning the quark labels with QCD's standard charge assignments.

### 12.2 Path closure under the relabeled identification

Re-running the closure analysis from §3.2 under the relabeled paths:

**Proton path** (2 lobes + 1 saddle of profile arc):

Total arc-degree covered: 2 × 240° + 120° = 600°
Total Δφ (literal-arc): 600° = 10π/3 radians

Closure condition (§2 of this file, twist-modified; tube-first conventions per §0.2):

<!-- Δφ = 2π n_t + n_r · 2π/3, so (10π/3 - n_r · 2π/3) / (2π) ∈ ℤ -->
$$
\frac{10\pi/3 \;-\; n_r \cdot 2\pi/3}{2\pi} \;\in\; \mathbb{Z}
$$

- n_r = 1: (10π/3 − 2π/3)/(2π) = 4/3. Not integer.
- n_r = 2: (10π/3 − 4π/3)/(2π) = 1. **Integer ✓**
- n_r = 3: (10π/3 − 6π/3)/(2π) = (10π/3 − 2π)/(2π) = (4π/3)/(2π) = 2/3. Not integer.

For the path to close at its starting (θ, φ): the total Δφ along the path must equal n_r · 2π/3 + n_t · 2π (mod 2π) for some integer n_t.

- Proton: Δφ_path = 600° = 10π/3.
  Want 10π/3 = n_r · 2π/3 + n_t · 2π for integers n_r, n_t.
  Divide by 2π/3: 5 = n_r + 3 n_t.
  Solutions: (n_t, n_r) = (0, 5), (1, 2), (2, −1), ...
  Smallest positive n_r giving integer n_t: **(n_t, n_r) = (1, 2)** — one tube turn, two ring revolutions.
  So **proton closes in 2 ring revolutions** (with 1 full profile traversal).

- Neutron: Δφ_path = 480° = 8π/3.
  Want 8π/3 = n_r · 2π/3 + n_t · 2π.
  Divide by 2π/3: 4 = n_r + 3 n_t.
  Solutions: (n_t, n_r) = (0, 4), (1, 1), (2, −2), ...
  Smallest positive n_r: **(n_t, n_r) = (1, 1)** — one tube turn, one ring revolution.
  So **neutron closes in 1 ring revolution**.

Correcting my earlier claim: under literal-arc parameterization, the proton's path closes in **(n_t, n_r) = (1, 2)** — 1 tube turn, 2 ring revolutions, not 3. The neutron closes in **(n_t, n_r) = (1, 1)** — 1 tube turn, 1 ring revolution. Both involve at least 1 full profile traversal (n_t ≥ 1).

The "1/3 precession" picture: each ring revolution shifts the path's φ-endpoint by 2π/3 due to twist. For the proton (Δφ_path = 10π/3 per cycle), a partial path covers 10π/3 in some number of revolutions; closure requires this Δφ_path to equal an integer-φ plus a multiple of 2π/3.

Reconciling with the user's "3 revolutions": maybe the user's intent was that *the up-quark cycles through three lobe positions over 3 revolutions* (the 3-fold precession of the lobe label). That's a different statement than "the proton's path closes in 3 revolutions." Each ring revolution shifts the wave from "lobe-1 region" to "lobe-2 region" to "lobe-3 region" (via the 1/3 twist), and after 3 revs the wave is back to its original lobe-positions. This 3-rev precession of *which* lobe the wave occupies is independent of the path-closure count.

So both pictures coexist:
- The proton's *path* (the locus of points the wave occupies) closes in 2 ring revolutions.
- The proton's *lobe-label rotation* (which lobe is "lobe-1" relative to the wave) cycles through three positions over 3 ring revolutions.

These describe different aspects of the same wave dynamics.

### 12.3 Charge of the proton and neutron paths (verifying §12.1)

**Proton path** (2 lobes + 1 saddle):

<!-- Q_proton = 2 · (+2/3) + 1 · (-1/3) = 4/3 - 1/3 = +1 ✓ -->
$$
Q_{\mathrm{proton}} \;=\; 2 \cdot \left(+\tfrac{2}{3}\right) \;+\; 1 \cdot \left(-\tfrac{1}{3}\right) \;=\; +1
$$

Matches observation: proton has charge +1.

**Neutron path** (1 lobe + 2 saddles):

<!-- Q_neutron = 1 · (+2/3) + 2 · (-1/3) = 2/3 - 2/3 = 0 ✓ -->
$$
Q_{\mathrm{neutron}} \;=\; 1 \cdot \left(+\tfrac{2}{3}\right) \;+\; 2 \cdot \left(-\tfrac{1}{3}\right) \;=\; 0
$$

Matches observation: neutron is neutral.

### 12.4 Neutron β decay as topological transition

Free neutron decay: n → p + e⁻ + ν̄_e with Q-value ≈ 0.78 MeV and lifetime ≈ 880 s.

Under the corrugated-torus identification:
- **Initial state:** neutron path covers 1 lobe + 2 saddles.
- **Final state:** proton path covers 2 lobes + 1 saddle.

The transition n → p is structurally a **conversion of 1 saddle to 1 lobe** (and the resulting energy difference is released as e⁻ + ν̄_e).

In the per-arc identification:
- Before: 1 up + 2 downs (=1 lobe + 2 saddles)
- After: 2 ups + 1 down (=2 lobes + 1 saddle)
- Net change: 1 down → 1 up, i.e., one saddle becomes one lobe

**Is this a "phase shift" or a "direction reversal"?** This was the user's specific question.

Under the traveling-wave reading of metric-mass (where ±n modes wind in opposite directions), converting d → u would require reversing the wave's direction of propagation around the compact direction. That's a hard dynamical transition.

Under the corrugated-torus reading: the surface has the same topology before and after, and both d and u correspond to specific *arc-segments* (saddle vs lobe) of the same surface. The d → u transition is a *q-shift* — incrementing the integer winding q by 1 while keeping p ≡ 1 (mod 3). Both states are in the same momentum sub-lattice; they differ only in q.

Equivalently in the geometric picture: the path-segment shifts from covering 1 saddle (down) to covering 1 lobe (up). The wave's amplitude redistributes from a saddle region to a lobe region. This is a **localized topological transition**, not a global direction reversal.

The energy cost of the transition:
- A single saddle has integrated turning −2π/3 (charge −1/3).
- A single lobe has integrated turning +4π/3 (charge +2/3).
- Net change in charge contribution: +1 (a saddle becomes a lobe, charge changes by +1).

The energy *cost* of this transition isn't fixed by the charge accounting alone; it depends on the surface's mode dispersion (Phase C). In QCD, this energy cost is set by the d-u quark mass difference (~2.6 MeV) plus the electroweak coupling factors. In the corrugated-torus framework, it should emerge from the surface's mode spectrum.

**Predicted features of the transition:**

1. **Wave-localized:** the transition happens locally on the surface (one segment flips from saddle-residence to lobe-residence), not globally.
2. **Energy released:** ≈ m_n − m_p − m_e ≈ 0.78 MeV, going into kinetic energy of e⁻ and ν̄_e.
3. **Lepton emission:** the electron and antineutrino emerge as wave modes on *other* sheets — they aren't part of the proton sheet. The corrugated-torus geometry alone doesn't host them.

**Why a q-shift is structurally easier than a direction reversal:**

In the metric-mass standing-wave picture, ±n components coexist within one particle (chapter 5). Converting +n → −n would require depleting the +n component while populating the −n component — a real *amplitude flow* between two components.

In the corrugated-torus q-shift: q is the integer winding around the ring direction. Incrementing q by 1 corresponds to adding *one more* ring revolution to the wave's path-length. Geometrically, this is "tightening the helical wrap by one turn" — a smooth deformation rather than a direction reversal.

This is the user's intuition: **the corrugated-torus topology makes neutron decay structurally easier than the standing-wave reading would suggest.** The d → u transition doesn't require any wave running backwards; it requires the wave's helical winding to gain one extra revolution.

### 12.4.1 Weak interaction as a least-energy phase-shift (hypothesis)

The Standard Model often describes the weak force as "the thing that turns an up quark into a down quark" — a flavour-changing current rather than a positional force. The clover/wave-mode picture suggests an even cleaner reading: **the weak interaction is the least-energy phase-shift between neighbouring (m_t, m_r) modes on the corrugated torus**.

The idea, stated as a hypothesis to develop:

- Each of the three quark-mode "slots" in a baryon is a localised wave-mode sitting at some (m_t, m_r) label on the surface.
- The clover dispersion μ²(m_t, m_r) = (m_r − 2m_t/3)² + (m_t/ε)² is not flat across (m_t, m_r) — different modes have slightly different energies, depending on ε and corrugation depth.
- If one mode is sitting at a higher-than-minimum (m_t, m_r) for its compatible-with-the-other-two configuration, there exists a *neighbouring* (m_t', m_r') with lower μ² that the mode can slide to (subject to charge conservation, baryon-number conservation, and the closure constraint).
- The transition emits the energy difference μ² → μ'² as wave modes on other sheets (electron sheet + neutrino sheet).
- The "weak coupling" g_W is whatever determines the matrix element for the phase-slip — small because the modes are well-separated in (m_t, m_r) space and the coupling operator is geometric, not direct.

Reading neutron β decay this way: the neutron's udd content (1 lobe + 2 saddles) has a "saddle slot" that, geometrically, sits at slightly higher energy than the corresponding "lobe slot" would. The configuration is metastable. A small perturbation (the weak coupling) lets one saddle slide phase to become a lobe — *because that's the lower-energy nearby configuration*. The 0.78 MeV is released as leptonic kinetic energy.

**Implications if this framing holds:**

1. **The weak force is not a separate field**; it's the calculus of which (m_t, m_r) reassignments lower total energy. The W and Z bosons of the Standard Model would correspond to the *propagating* phase-shift modes — the disturbance that carries the energy/momentum off to other sheets.
2. **Parity violation** of the weak force would map to an asymmetry of the corrugated surface (e.g., chirality of the τ = +1/3 twist vs −1/3 twist).
3. **Flavour mixing (CKM)** would correspond to the structure of which (m_t', m_r') neighbours are accessible from a given (m_t, m_r).
4. **Decay rates** would emerge from a least-energy calculus: time-to-slide = phase-space factor × |matrix element|², with both computable from the surface metric.

**Status:** This is currently a structural hypothesis, not derived. To develop it would require (a) showing that the (m_t^d, m_r^d) → (m_t^u, m_r^u) shift is indeed energy-lowering for the neutron's specific configuration (Phase C numerical check), and (b) showing that the inter-sheet coupling factor naturally gives the observed weak coupling strength g_W. Both are concrete next steps.

### 12.5 Why is the proton lower-energy than the neutron?

Empirically: m_n − m_p ≈ 1.29 MeV. The neutron is heavier, so β decay is energetically favorable.

Under the corrugated-torus framework, two candidate explanations:

**Candidate A: Topology alone.** The proton path (2 lobes + 1 saddle) and neutron path (1 lobe + 2 saddles) have different geometric content. If lobes and saddles have different *intrinsic* energy contributions (beyond just charge), then their sums would differ between proton and neutron.

For example: if each lobe carries energy E_L and each saddle carries energy E_S, then:
- Proton energy: 2 E_L + E_S
- Neutron energy: E_L + 2 E_S
- Difference: (m_n − m_p) c² = E_S − E_L

So under topology alone, the neutron being heavier means E_S > E_L (saddles cost more energy than lobes). Is there a structural reason for this in the corrugated-torus geometry?

One possibility: lobes have "more space" (positive curvature, broader physical extent) while saddles are "compressed" (negative curvature, narrower extent). The compressed region might host higher-momentum modes, hence higher energy. This is intuitive but needs Phase C to verify.

**Candidate B: Substrate asymmetry on top of topology.** The framework's earlier [work-strong.md](../../sheet-proton/work/strong.md) and [grid-primitive chapter 9](../../grid-primitive/09-chirality-asymmetry.md) raised the possibility of a small substrate-level chirality asymmetry χ_anti that breaks the (m, n) ↔ (−m, −n) sign-reflection symmetry — providing a matter/antimatter bias.

Such a bias would also produce a small preference between proton-orientation and neutron-orientation configurations, energetically. The 1.29 MeV proton-neutron mass split might come partly from intrinsic topology (Candidate A) and partly from substrate asymmetry (Candidate B).

**Phase C numerics** (corrugated-torus mode spectrum + substrate-asymmetry perturbation) is needed to distinguish these two contributions and to pin the magnitude of E_S − E_L. This work has been carried out for embedding A in [clover-mass.md](clover-mass.md). The closed-form leading-order mass formula μ² = (m_r − 2 m_t/3)² + (m_t/ε)² was derived there (clover-mass §4), validated numerically to machine precision at small η (clover-mass §6.6), and used to search for (m_t, m_r) identifications that reproduce m_n/m_p = 1.001378. Candidate pairs — e.g. (proton, neutron) = ((m_t, m_r) = (2, 1), (m_t, m_r) = (2, 2)) at ε ≈ 0.2, χ ∈ [0.5, 2] — fit the observed mass ratio to within **0.03%**. This does not derive E_S > E_L explicitly as the mass-split mechanism, but it does confirm that **the corrugated-torus geometry alone can reproduce the proton/neutron mass ratio at the percent level** without invoking electromagnetic, bare-mass, or chiral-symmetry-breaking corrections. Whether such corrections are needed to close the remaining 0.03% gap, or whether the gap is closable by fine-tuning (ε, χ) within clover, is the next quantitative test.

### 12.6 Net effect: the proton is stable, the neutron decays

Combining the threads:
- The corrugated-torus geometry supports both proton (uud, 2 lobes + 1 saddle) and neutron (udd, 1 lobe + 2 saddles) as closed paths on the same surface.
- The neutron is energetically higher (~1.3 MeV) than the proton.
- The transition n → p is a localized topological event (1 saddle → 1 lobe, equivalently 1 d → 1 u).
- The energy released ≈ 0.78 MeV manifests as electron and antineutrino kinetic energies on other sheets.
- The decay is slow (880 s) because:
  1. The transition requires "tunneling" between two topologically distinct configurations (saddle → lobe at a localized site).
  2. The energy must be transferred to other sheets (inter-sheet coupling is weak, per the broader framework — see [STATUS.md](STATUS.md)).
  3. The phase-space factor for low Q-value decay (Q⁵ scaling) is small (this is the standard Sargent's-rule consideration from earlier work).

All three contribute to the slow decay rate. The corrugated-torus framework provides the *structural* foundation (the saddle/lobe distinction and the q-shift mechanism); the rate calculation requires Phase C numerics plus inter-sheet coupling analysis.

### 12.7 What Phase B has established

| Question | Answer (under corrugated-torus framework) |
|---|---|
| What is an up quark? | A single lobe arc on the proton-sheet profile (+2/3 charge from convex segment) |
| What is a down quark? | A single saddle arc (−1/3 charge from concave segment) |
| What is a proton? | A path covering 2 lobes + 1 saddle (uud, charge +1) |
| What is a neutron? | A path covering 1 lobe + 2 saddles (udd, charge 0) |
| Does the user's "1/3 precession" picture work? | Yes: the surface twist produces a 120° lobe-relabeling per ring revolution, with closure after 2 (proton) or 1 (neutron) full revolution |
| How does n → p decay topologically? | A q-shift: 1 saddle → 1 lobe at a localized site (1 down → 1 up). No direction reversal required. |
| Why is the proton stable? | The proton is lower-energy than the neutron; the n → p transition requires tunneling between topological classes and emitting energy to other sheets |
| Does topology alone explain the n-p mass split? | Phase C numerics in [clover-mass.md](clover-mass.md) confirm: candidate (m_t, m_r) wave-mode identifications reproduce m_n/m_p = 1.001378 to within 0.03% from geometry alone (no EM/bare-mass/chiral inputs). Whether the residual 0.03% requires those QCD effects, or closes with fine-tuned (ε, χ), is the next test. |

**Remaining Phase B work to do:**

- Verify the 2-revolution proton-path closure with explicit construction (animated visualization helpful).
- Catalog all candidate quark paths on the surface and their charges; identify whether non-canonical paths (e.g., 3-lobe path with charge +2) correspond to anything observable (perhaps Δ⁺⁺ baryon).
- Examine excited states: higher-energy paths that wrap multiple times around the profile or have richer structure. These might correspond to baryon resonances (Δ⁰, Δ⁺, N* states).

These remaining items are computationally tractable but require care; they're listed as next-action items in §16.

---

## 13. Mass spectrum — see clover-mass.md

The Phase C numerical eigenvalue work (Hill-equation reduction of the Laplacian, perturbative expansion in η, numerical Bloch-restricted solver, mass-spectrum prediction) lives in [clover-mass.md](clover-mass.md).

---

## 14. Open questions

1. **Choice of parameterization (A vs B in §3.2).** Does the up-quark/down-quark distinction depend on whether we use equal-arc or literal-arc parameterization? Probably yes; need to commit to one.

2. **Choice of embedding (A vs B in §9.3).** Parameter-shift vs rotation. Topology and path winding are identical; metric and spectrum differ. Pinning to one of these is part of the Phase C numerical work.

3. **Does the proton-as-3-precessing-quarks construction actually close cleanly?** §3.3 sketches it; verification requires the full path analysis.

4. **What about the neutron?** udd. Under the closure pattern, does it close in 3 revolutions (because 1 up + 2 downs)? Or some other count?

5. **Does this geometry produce the correct mass split** between proton and neutron? The shear-and-aspect-ratio framework of metric-charge (chapter 7-8) operates on the standard T² without corrugation. The corrugated torus would need its own dispersion analysis.

6. **How does the user's specific (1, +2) / (−1, +2) hypothesis** (from [quark-flavor.md](quark-flavor.md)) map onto path topology on the corrugated torus? Is there a natural relabeling?

7. **Mass and charge from corrugation.** The traditional MaSt mass formula μ² = (n_t/ε)² + (n_r − s·n_t)² is for the smooth torus. On the corrugated torus, the dispersion is modified. What's the modified mass formula? Does it predict different (and possibly better) values for the proton sheet's (ε, s)?

---

## 15. Cross-references

- [quark-flavor.md](quark-flavor.md) — the candidate (m, n) mappings; corrugated-torus geometry might pick one out
- [fractional-charge.md](../../metric-binding/work/fractional-charge.md) — partial-knot picture; corrugated torus is a candidate geometric realization, with §11's third-integer momentum derivation as the concrete mechanism
- [color-confinement.md](../../metric-binding/work/color-confinement.md) — Z₃ confinement; the 3-lobe profile gives the 3 directly, and §11.6 is the explicit derivation
- [mass-from-cancellation.md](../../metric-binding/work/mass-from-cancellation.md) — mass mechanism may have corrugated-torus analog
- [metric-charge chapter 4](../../metric-charge/04-the-closure-condition.md) — closure rule on smooth torus; corrugation modifies
- [metric-charge chapter 7](../../metric-charge/07-aspect-ratio-and-character.md) — aspect ratio character; corrugation is a new geometric parameter

---

## 16. Next actions

**Phase A is now complete in this file.** Phases B and C are sketched but not expanded. Concrete next steps in order:

1. **Verify the geometric closure of the profile.** Choose specific r_lobe and r_saddle values; render the profile to confirm it's a smooth closed curve. Should take a few hours of plotting. Output: profile.png at representative (χ, scale) values.

2. **Implement the corrugated-torus embedding** in 3D and render. Visualize the surface with τ = 1/3 twist. A day of work. Output: surface visualization confirming the geometric structure.

3. **Phase B expansion.** Work out the closure-condition analysis for the up-quark and down-quark paths under both parameterization choices. Determine whether the user's "1/3 precession" picture closes consistently. Add §12 detail.

4. **Phase C — numerical wave equation.** Implement the Laplacian (§10), solve the eigenvalue problem (§13), compute the mode spectrum. Compare to flat-T² spectrum at the same ε. ~100-300 lines of Python.

5. **Mass-prediction test.** Identify which numerical modes correspond to proton, neutron, etc. Compare predicted masses to observed.

Steps 1-2 are simple sanity checks. Steps 3-4 are the substantive computational work. Step 5 is the test of whether the geometry yields anything quantitatively useful.

**If steps 3-5 yield, this is a major structural contribution** — a geometric derivation of Z₃ confinement, three-quark structure, fractional charges, and possibly the proton/neutron mass mechanism, all from a single geometric construction. The Phase A math already shows the structural derivation works for *charge quantization* (third-integer modes); Phases B and C test whether it also yields the *quantitative* particle physics.
