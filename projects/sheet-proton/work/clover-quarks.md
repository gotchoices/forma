# clover-quarks.md — corrugated 3-lobed torus as substrate for quark assignments

**Status:** Exploratory work file. Develops the user's hypothesis that quarks correspond to specific paths on a 3-lobed torus surface with a matching 1/3 chiral twist. The 120° rotational symmetry of the profile plus the 120° twist per ring revolution may align such that proton-like 3-quark configurations close consistently. Sister to [quark-flavor.md](quark-flavor.md), [fractional-charge.md](../../metric-binding/work/fractional-charge.md), [color-confinement.md](../../metric-binding/work/color-confinement.md).

**Tone:** Geometric construction first, physics interpretation second. The geometry is well-defined; the quark identification is the speculative payoff.

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

Sweep the profile around a major circular ring of radius R, with the cross-section rotating by a twist angle α·θ as the ring angle θ ∈ [0, 2π) advances.

**Surface parameterization:**

<!-- r(θ, φ) = R·(cos θ, sin θ, 0) + R_{α θ}·P(φ) embedded in plane perpendicular to ring tangent -->
$$
\vec{r}(\theta, \varphi) \;=\; \vec{R}(\theta) \;+\; M(\theta) \cdot P(\varphi + \alpha\,\theta)
$$

where:
- **R**(θ) = R · (cos θ, sin θ, 0) is the ring center at angle θ
- M(θ) is the 3D rotation taking the cross-section plane (at θ = 0) to the plane perpendicular to the ring tangent at angle θ
- α is the **twist rate** — how much the profile rotates relative to the ring's local Frenet frame as θ advances
- α θ enters as a rotation *inside* the profile parameter φ

**The 1/3 twist condition.** Choose α such that one full ring revolution gives a 120° = 2π/3 rotation of the profile:

<!-- α · 2π = 2π/3, so α = 1/3 -->
$$
\alpha \;=\; \frac{1}{3}
$$

With this choice, going around the ring once (θ: 0 → 2π) advances φ by 2π/3 — exactly the angular separation between lobes in the profile.

**Topology check.** The surface closes onto itself because the profile has 3-fold symmetry: the rotated profile at θ = 2π is identical to the profile at θ = 0 (just relabeled). So the surface is genuinely a closed 2-torus T², not an open spiral.

**Effective identification.** A point (θ, φ) on the surface is identified with (θ + 2π, φ + 2π/3) — the twist modifies the standard torus identification (θ, φ) ~ (θ + 2π, φ) by adding the 2π/3 shift in φ.

---

## 2. Paths and their windings

A closed path on the surface is parameterized by (θ(t), φ(t)) with periodic boundary conditions. The path's homotopy class is determined by:

- **n_θ**: the integer number of times it winds around the ring (θ-direction)
- **n_φ**: the integer winding around the cross-section (φ-direction)

For a closed path under the twisted identification, the total displacement must satisfy:

<!-- Δθ = 2π n_θ, Δφ = 2π n_φ + n_θ · 2π/3 -->
$$
\Delta\theta \;=\; 2\pi\, n_\theta, \qquad \Delta\varphi \;=\; 2\pi\, n_\varphi \;+\; n_\theta \cdot \frac{2\pi}{3}
$$

The extra n_θ · 2π/3 in Δφ is the **twist contribution**: each ring revolution adds 120° of cross-section angle. So a path that goes once around the ring (n_θ = 1) and once around the cross-section (n_φ = 1) traverses total cross-section angle of 2π + 2π/3 = 8π/3 = 480° — i.e., a full revolution plus one more lobe-saddle pair.

**Implication for closure.** A path with only one ring revolution (n_θ = 1, n_φ = 0) closes only if it traverses Δφ = 2π/3 in the cross-section — i.e., exactly one lobe-saddle pair (one fundamental domain of the profile). So *the simplest closed path on this surface is one revolution of the ring covering one-third of the cross-section*. Three such paths, offset by 2π/3 each, together cover the whole cross-section.

This is structurally suggestive: **three minimal closed paths together fill the surface, each occupying one-third of the cross-section.** It's the geometric realization of the Z₃ confinement pattern.

---

## 3. Quark identification — the user's hypothesis

### 3.1 The proposal

- **Up quark** = a closed path traversing **2 lobes and 1 saddle** of the cross-section per ring revolution
- **Down quark** = a closed path traversing **2 saddles and 1 lobe** of the cross-section per ring revolution

In terms of arc-degree (lobe = 240°, saddle = 120°):
- Up-quark path covers 240° + 240° + 120° = 600° of profile arc
- Down-quark path covers 240° + 120° + 120° = 480° of profile arc

Both exceed one full cross-section traversal (360°). So neither closes in one ring revolution; both require multiple ring revolutions to close.

### 3.2 Closure condition for these paths

Using §2's identification: a path that wraps n_θ times around the ring with Δφ covering some total cross-section angle Φ_path must satisfy

<!-- Φ_path = 2π n_φ + n_θ · 2π/3 -->
$$
\Phi_{\mathrm{path}} \;=\; 2\pi\, n_\varphi \;+\; n_\theta \cdot \frac{2\pi}{3}
$$

for integer n_φ. Equivalently:

<!-- (Φ_path - n_θ · 2π/3) / (2π) ∈ ℤ -->
$$
\frac{\Phi_{\mathrm{path}} \;-\; n_\theta \cdot 2\pi/3}{2\pi} \;\in\; \mathbb{Z}
$$

Converting the user's arc-degree numbers to cross-section-angle: this requires committing to a parameterization relating arc-degree to φ-angle. Two natural choices:

**Choice A: equal-arc parameterization.** Treat each lobe as covering 240°/(240°+120°) = 2/3 of the φ between lobe-junction events; each saddle as 1/3. Then each fundamental domain (one lobe + one saddle) covers 2π/3 of φ regardless of arc-degree. In this case:
- Up-quark path (2 lobes + 1 saddle) covers... but what does "2 lobes + 1 saddle" mean in φ?
  - If the quark's wave is a localised pattern that *prefers* lobes over saddles (or vice versa), this is about the wave's amplitude distribution, not literally about path length on the profile.

**Choice B: literal arc-length parameterization.** Arc-degree directly = φ-angle. Then:
- Up-quark path: Φ = 600° = 10π/3
- Down-quark path: Φ = 480° = 8π/3

Apply the closure condition for n_θ = 1 (single ring revolution):
- Up: (10π/3 - 2π/3)/(2π) = 8π/3 / 2π = 4/3 — **not integer** — doesn't close in 1 revolution
- Down: (8π/3 - 2π/3)/(2π) = 6π/3 / 2π = 1 — **integer!** — closes in 1 revolution

For n_θ = 3:
- Up: (10π·3/3 - 3·2π/3)/(2π) = (10π - 2π)/(2π) = 4 — **integer** — closes after 3 revolutions
- Down: closes after 1 revolution already

So under literal arc-length: **down-quark path closes in 1 ring revolution, up-quark path closes in 3 ring revolutions.** This is a striking asymmetry — and it suggests the up and down quarks are *fundamentally different topological objects* on this surface, not just two species of similar paths.

### 3.3 The user's "1/3 precession" reading

The user's hope: "the tube twist would advance the phase such that a proton could forever keep traversing 2 lobes and 1 saddle (with 1/3 precession)."

Under Choice B: the up-quark path doesn't close in 1 revolution; instead, the path's "endpoint" is offset by 2π·4/3 − 2π = 2π/3 in the cross-section — exactly one fundamental domain shifted. So the up-quark path *precesses by 120° per ring revolution*, and closes only after 3 revolutions.

A proton (uud composite) has three constituents. If each is an up-quark-like path or a down-quark-like path, and their precessions are correlated, the composite can close in fewer revolutions than any individual.

**Specifically:** if the three constituents of a proton are mutually offset by 120° in their starting positions (so they together cover the surface), and each precesses by 120° per ring revolution, then *each revolution rotates the three constituents to the next-clockwise positions* — and after 3 revolutions, each has returned to its original spot. The proton as a whole closes in 3 revolutions; each constituent closes in 3 revolutions; but at any given revolution they collectively cover the full cross-section.

This is the "1/3 precession" the user is pointing at. It's structurally consistent with the proton-as-3-quark composite, with Z₃ confinement realized geometrically by the 120° twist.

---

## 4. Quark mappings to compare

Connect to [quark-flavor.md](quark-flavor.md): the corrugated-torus picture suggests specific (m, n) identifications for u and d.

| Particle | Path topology | n_θ to close | Conjectured (m, n) mapping |
|---|---|---|---|
| u (up) | 2 lobes + 1 saddle per revolution | 3 | T(1, ?) — needs literal-arc analysis |
| d (down) | 2 saddles + 1 lobe per revolution | 1 | T(1, ?) — closes faster |
| proton uud | 3 constituents at 120° offsets, collectively cover surface | 3 | (3, ?) composite via path superposition |

**Note the n_θ = 3 closure for the up-quark path** is interesting: it might be the "color confinement" pattern realized geometrically. A free up-quark (single path) doesn't close in 1 revolution; it requires the 3-fold structure (three offset paths) for closure within one round.

**TODO:** match the (m, n) windings of metric-charge's primitive inventory to the (n_θ, n_φ) topology of these clover-torus paths.

---

## 5. Phase carried along the path

The user's deeper point: the 120° twist advances the *phase* of a wave along the path. If a wave has phase Θ(θ, φ), then after one ring revolution, the wave's phase is shifted by some amount that includes the geometric twist contribution.

A wave's phase along a path:

<!-- ΔΘ = ∫ (∂Θ/∂θ dθ + ∂Θ/∂φ dφ) -->
$$
\Delta\Theta \;=\; \int_{\mathrm{path}} \left(\frac{\partial \Theta}{\partial \theta} d\theta \;+\; \frac{\partial \Theta}{\partial \varphi} d\varphi\right)
$$

For a wave on the corrugated torus, the metric of the surface (induced from the 3D embedding) determines how phase accumulates. The twist α = 1/3 means that "constant φ" curves on the surface are not closed in 1 revolution; they precess by 2π/3.

This is structurally analogous to the *Aharonov-Bohm phase* on a topologically non-trivial manifold: a closed path picks up a phase that depends on the global topology, not just the local geometry.

**Conjecture:** the proton's wave on this surface has a definite phase that returns to itself after the proper closure (3 revolutions for up-quark, 1 for down-quark, or whatever the composite structure requires). The "1/3 precession" is the proton's wavefunction picking up a phase shift of 2π·(1/3) per ring revolution.

For the wavefunction to be single-valued on the surface, the total phase accumulated around any closed path must be a multiple of 2π. This is a *quantization condition* on the wave's allowed momenta — a Bohr-Sommerfeld-style rule.

**TODO:** work out the phase-accumulation quantization for the up-quark and down-quark paths under Choice B. Does the 120° geometric twist provide the right phase for closure?

---

## 6. Connection to metric-charge / metric-binding framework

### 6.1 Closure condition

The standard closure rule of [metric-charge chapter 4](../../metric-charge/04-the-closure-condition.md) is "T(m, n) closure-satisfies iff m | n." On the corrugated torus, the closure condition is modified by the twist: the (n_θ, n_φ) indices have a shifted relation due to the 2π/3 twist per revolution.

Does the corrugated torus produce a *different* closure rule, or does it produce the same rule with different (m, n) interpretation? **TODO:** work out.

### 6.2 Z₃ confinement

The corrugated torus naturally produces a 3-fold structure: three minimal closed paths (one per fundamental domain) together cover the surface. This is the geometric realization of Z₃ confinement that [color-confinement.md](../../metric-binding/work/color-confinement.md) is trying to derive.

If this realization holds, it answers one of the framework's deepest questions structurally — "why three?" because the profile has 3 lobes, by construction. The closure of compounds requires a 3-fold partner structure.

### 6.3 Fractional charge

Per [fractional-charge.md](../../metric-binding/work/fractional-charge.md): if each minimal closed path on the corrugated torus carries 1/3 of the composite's external charge, then "fractional charge" is what a single path's contribution amounts to before the 3-fold closure is satisfied. Closure (full traversal of the surface) requires all three paths together — and that's where the charges combine to integer.

The corrugated-torus picture is essentially **partial-knot decomposition with a specific geometric realization**.

---

## 7. Mathematical specification — formal write-up

For computational work, the surface is specified by:

1. **Profile function** P(φ) — a closed C¹ curve in ℝ² with 3-fold rotational symmetry, built from alternating arcs of curvature ±κ_lobe, ±κ_saddle.

2. **Twist parameter** α = 1/3.

3. **Surface embedding** $\vec{r}(\theta, \varphi) = \vec{R}(\theta) + M(\theta)\, P(\varphi + \alpha\theta)$ in ℝ³.

4. **Induced metric** g_ij on the surface from the embedding.

5. **Wave equation** (∂_t² − c² Δ_g) ψ = 0 on the surface, with periodic boundary conditions under the twisted identification (θ, φ) ~ (θ + 2π, φ + 2π/3).

6. **Closed paths** classified by (n_θ, n_φ) homotopy indices satisfying the twist-modified identification.

**Computable quantities:**
- Spectrum of the wave equation on the surface
- Mode decomposition into (n_θ, n_φ) families
- Identification of "up-quark-like" and "down-quark-like" modes
- Composite-mode masses for 3-mode bound states

---

## 8. Open questions

1. **Choice of parameterization (A vs B in §3.2).** Does the up-quark/down-quark distinction depend on whether we use equal-arc or literal-arc parameterization? Probably yes; need to commit to one.

2. **Does the proton-as-3-precessing-quarks construction actually close cleanly?** §3.3 sketches it; verification requires the full path analysis.

3. **What about the neutron?** udd. Under the closure pattern, does it close in 3 revolutions (because 1 up + 2 downs)? Or some other count?

4. **Does this geometry produce the correct mass split** between proton and neutron? The shear-and-aspect-ratio framework of metric-charge (chapter 7-8) operates on the standard T² without corrugation. The corrugated torus would need its own dispersion analysis.

5. **How does the user's specific (1, +2) / (−1, +2) hypothesis** (from [quark-flavor.md](quark-flavor.md)) map onto path topology on the corrugated torus? Is there a natural relabeling?

6. **Mass and charge from corrugation.** The traditional MaSt mass formula μ² = (n_t/ε)² + (n_r − s·n_t)² is for the smooth torus. On the corrugated torus, the dispersion is modified. What's the modified mass formula? Does it predict different (and possibly better) values for the proton sheet's (ε, s)?

---

## 9. Cross-references

- [quark-flavor.md](quark-flavor.md) — the candidate (m, n) mappings; corrugated-torus geometry might pick one out
- [fractional-charge.md](../../metric-binding/work/fractional-charge.md) — partial-knot picture; corrugated torus is a candidate geometric realization
- [color-confinement.md](../../metric-binding/work/color-confinement.md) — Z₃ confinement; the 3-lobe profile gives the 3 directly
- [mass-from-cancellation.md](../../metric-binding/work/mass-from-cancellation.md) — mass mechanism may have corrugated-torus analog
- [metric-charge chapter 4](../../metric-charge/04-the-closure-condition.md) — closure rule on smooth torus; corrugation modifies
- [metric-charge chapter 7](../../metric-charge/07-aspect-ratio-and-character.md) — aspect ratio character; corrugation is a new geometric parameter

---

## 10. Next actions

1. **Verify the geometric closure of the profile.** Choose specific r_lobe and r_saddle values; render the profile to confirm it's a smooth closed curve. (A few hours of plotting.)

2. **Implement the corrugated-torus embedding** in 3D and render. Visualize what the surface looks like with α = 1/3 twist. (A day of work.)

3. **Work out the closure-condition analysis** for the up-quark and down-quark paths under both parameterizations (A and B). Determine whether the user's "1/3 precession" picture closes consistently.

4. **Develop the wave equation on the corrugated torus.** Compute the induced metric, write the Laplacian, identify the mode spectrum. Compare to flat-T² spectrum at the same (ε, s).

5. **Test against proton/neutron mass predictions.** Does the corrugated-torus mass formula give better fits than R64's flat-torus mass formula?

If steps 3 and 4 yield, this is a major structural contribution — a geometric derivation of Z₃ confinement, three-quark structure, and possibly the proton/neutron mass mechanism, all from a single geometric construction.
