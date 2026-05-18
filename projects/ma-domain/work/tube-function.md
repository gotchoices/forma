# tube-function.md — a generalized cross-section function for the corrugated tube

**Status:** Working hypothesis / how-to. Documents a smooth two-parameter Fourier polar curve family that generalizes both the ellipse-like bilobe used as the electron tube and the three-lobe arc clover used for quarks. The function is C^∞ everywhere — no curvature jumps to manage — and a single parameter set lets one dial smoothly between the regimes. Records how to fit each particle-construction job with specific parameter choices.

**Cross-references:**
- [electron-tube.md](electron-tube.md) — bilobe tube with twist τ=2 as the T(1,2) electron host
- [sheet-proton clover-quarks §1.1, §3](../../sheet-proton/work/clover-quarks.md) — arc-clover three-lobe construction and the +2/3 / −1/3 charge accounting
- [viz/tube-lab](../../../viz/tube-lab.md) — interactive visualizer for this function family

---

## 1. Motivation

Two different tube cross-sections appear in the framework so far:

- **Bilobe** ([electron-tube §5](electron-tube.md)) — an ellipse with C₂ symmetry, smooth (C^∞) everywhere, all convex. Used as the substrate that makes T(1, 2) the lightest m_t = 1 mode under twist τ = 2.
- **Arc clover** ([clover-quarks §1.1](../../sheet-proton/work/clover-quarks.md)) — three convex 240° lobe arcs joined to three concave 120° saddle arcs by tangency. C¹ but not C² — curvature jumps at the six lobe-saddle junctions where the two arc radii meet.

Both shapes have non-trivial rotational symmetry (C₂ and D₃ respectively) and both serve as hosts for particle modes. The geometric distinction between them is qualitative: one is everywhere convex, the other has alternating convex / concave regions. But the underlying job is the same — to provide an N-fold symmetric, twist-bearing cross-section for the corrugated tube.

A single function family that includes both shapes — and that allows a continuous interpolation between them, with adjustable lobe count and adjustable valley depth — gives a unified picture and removes one ugly feature of the arc construction (the κ discontinuities at junctions).

---

## 2. The function

The proposed cross-section is the **truncated Fourier polar curve**:

<!-- r(φ) = R · [1 + a₁·cos(N·φ) + a₂·cos(2·N·φ)] -->
$$
r(\varphi) \;=\; R \cdot \bigl[\, 1 \,+\, a_1 \cos(N\varphi) \,+\, a_2 \cos(2N\varphi) \,\bigr]
$$

The cross-section curve in the (x, y) plane is then

<!-- P(φ) = (r(φ) cos φ, r(φ) sin φ) -->
$$
P(\varphi) \;=\; \bigl(\, r(\varphi)\cos\varphi,\; r(\varphi)\sin\varphi \,\bigr), \qquad \varphi \in [0, 2\pi)
$$

with four shape parameters:

| Parameter | Symbol | Role |
|---|---|---|
| Lobe count | N ∈ ℤ, N ≥ 2 | Number of N-fold symmetric features per revolution |
| Fundamental amplitude | a₁ | Sets the gross radial swing between lobe peaks and saddle valleys |
| Second-harmonic amplitude | a₂ | Sharpens or flattens valleys; controls how deeply κ goes negative |
| Mean radius | R | Sets the overall scale; the perimeter-averaged radius equals R |

The factor cos(Nφ) is N-periodic in φ, so the curve has rotational symmetry of order N: P(φ + 2π/N) is the same shape as P(φ), rotated by 2π/N. The second harmonic cos(2Nφ) has the same symmetry but oscillates twice as fast, giving an independent degree of freedom to shape each fundamental domain [0, 2π/N).

### 2.1 Derived quantities at the symmetry points

At the lobe-axis (φ = 0) and the saddle-midpoint (φ = π/N), the symmetry of the function forces cos(Nφ) = ±1 and cos(2Nφ) = +1. So:

<!-- r at lobe peak (φ = 0): r₀ = R(1 + a₁ + a₂) -->
$$
r_{\text{lobe}} \;\equiv\; r(0) \;=\; R\,(1 + a_1 + a_2)
$$

<!-- r at saddle midpoint (φ = π/N): r_π/N = R(1 − a₁ + a₂) -->
$$
r_{\text{saddle}} \;\equiv\; r(\pi/N) \;=\; R\,(1 - a_1 + a_2)
$$

If one prefers to specify a "peak prominence" p and a "valley depth" v as radial fractions:

p ≡ (r_lobe − R) / R = a₁ + a₂
v ≡ (R − r_saddle) / R = a₁ − a₂

solve for the harmonics:

<!-- a₁ = (p + v)/2 ; a₂ = (p − v)/2 -->
$$
a_1 \;=\; \tfrac{1}{2}(p + v), \qquad a_2 \;=\; \tfrac{1}{2}(p - v)
$$

This identification is exact only when the global extrema of r(φ) actually sit at the symmetry points. When |a₁/(4a₂)| < 1, additional extrema appear off-axis at cos(Nφ) = −a₁/(4a₂), and the numerical r_max, r_min may differ from r_lobe, r_saddle. The boundary case a₁ = 4|a₂| keeps the extrema co-located with the symmetry points.

### 2.2 Curvature

The signed curvature of a polar curve r(φ) is

<!-- κ(φ) = (r² + 2r'² − r·r'') / (r² + r'²)^{3/2} -->
$$
\kappa(\varphi) \;=\; \frac{r^2 + 2\,r'^2 - r\,r''}{(r^2 + r'^2)^{3/2}}
$$

where

r'(φ)  = −R·[a₁·N·sin(Nφ) + 2a₂·N·sin(2Nφ)]
r''(φ) = −R·[a₁·N²·cos(Nφ) + 4a₂·N²·cos(2Nφ)]

All three of r, r', r'' are sums of sines and cosines, so κ(φ) is a closed-form smooth function of φ with no piecewise stitching. Higher derivatives of κ are equally well-behaved.

This is the key geometric improvement over the arc clover: every derivative of the cross-section is continuous everywhere.

---

## 3. When does the curve develop concave saddles?

The total signed turning ∮ κ ds = 2π is fixed by Gauss-Bonnet for any simple closed plane curve. But the *sign* of κ at any specific point depends on the shape, so a smooth curve may be everywhere convex (κ > 0) or have alternating convex / concave regions.

For the Fourier polar curve, the saddle midpoint at φ = π/N has r' = 0 (by symmetry), so the curvature there simplifies:

<!-- κ at φ=π/N: κ = (r² − r r'') / r³ = (1 − a₁(1+N²) + (a higher-order a₂ term))/(r·denom) -->
$$
\kappa(\pi/N) \;=\; \frac{1}{r} \;-\; \frac{r''}{r^2}
$$

Substituting r(π/N) = R(1 − a₁ + a₂) and r''(π/N) = R·N²·(a₁ − 4a₂):

<!-- κ at saddle midpoint = [(1 − a₁ + a₂) − N²(a₁ − 4a₂)] / [R(1 − a₁ + a₂)²] -->
$$
\kappa(\pi/N) \;=\; \frac{\,1 - a_1(1 + N^2) + a_2(1 + 4N^2)\,}{R\,(1 - a_1 + a_2)^2}
$$

The denominator is positive (assuming r > 0, no self-intersection). So κ at the saddle midpoint is negative — i.e. the saddle is genuinely concave — iff the numerator is negative:

<!-- saddle is concave when 1 < a₁(1+N²) − a₂(1+4N²) -->
$$
a_1\,(1 + N^2) \;-\; a_2\,(1 + 4N^2) \;>\; 1
$$

Single-harmonic case (a₂ = 0): saddle is concave iff a₁ > 1/(1 + N²). Thresholds:

| N | a₁ threshold for concave saddle (a₂ = 0) |
|---:|---:|
| 2 | 1/5 = 0.200 |
| 3 | 1/10 = 0.100 |
| 4 | 1/17 ≈ 0.059 |
| 5 | 1/26 ≈ 0.038 |
| 6 | 1/37 ≈ 0.027 |

Higher N makes the saddles "give way" at lower a₁ — a small radial swing produces concave valleys for N = 4 or more. Conversely, on a bilobe (N = 2), the saddle remains convex up to a fairly large radial swing (a₁ = 0.2 corresponds to lobe peaks 20% larger than the saddle midpoint).

A positive a₂ raises the threshold (saddles harder to make concave); a negative a₂ lowers it.

---

## 4. The 240°/120° question

A natural question, posed in the context of the arc clover: does the smooth three-lobe curve always present a 240° convex / 120° concave split?

**Answer:** No. The arc clover's 240°/120° split is specific to the piecewise-circular construction. The smooth Fourier curve has a (a₁, a₂)-dependent split, and even *what one means* by "240°" needs to be made precise.

### 4.1 Three different "angle spans" to keep separate

The arc clover's 240°/120° refers to three geometric quantities that all happen to equal each other because the curve is built from circular arcs of constant per-piece curvature:

1. **Angular span of the arc on its own center-circle.** Each lobe arc covers 240° = 4π/3 of its lobe-circle. Each saddle arc covers 120° = 2π/3 of its saddle-circle.

2. **Signed tangent turning along the arc.** ∫_arc κ ds for a circular arc of radius r over angular extent θ equals (1/r) · (r·θ) = θ. So lobe-arc turning = +240° = +4π/3, saddle-arc turning = −120° = −2π/3.

3. **φ-extent of the lobe vs saddle in a constant-arc-speed parameterization.** When [clover-quarks §1.1](../../sheet-proton/work/clover-quarks.md) parameterizes the closed curve by φ ∈ [0, 2π) at constant arc-speed, the lobe occupies φ-extent (2π/3)·(2r_L)/(2r_L + r_S) and the saddle occupies the rest. For the canonical r_L = 2·r_S, this gives lobe-φ-extent 4π/9 and saddle-φ-extent 2π/9 — already not 240°/120° in φ, despite the arc spans being 240°/120°.

So even on the arc clover, "240°" is unambiguous only in the first two senses, not the third. The total *turning* per lobe is 4π/3, and the total *arc-span* per lobe on its center-circle is 4π/3 — those coincide for a constant-curvature arc.

### 4.2 What the smooth curve guarantees

For any simple closed smooth plane curve with three-fold symmetry and three convex regions alternating with three concave regions:

<!-- A_lobe + A_saddle = 2π/3 (per fundamental domain), where A_lobe = ∫_{one lobe region} κ ds > 0 and A_saddle = ∫_{one saddle region} κ ds < 0 -->
$$
A_{\text{lobe}} \;+\; A_{\text{saddle}} \;=\; \frac{2\pi}{3}
$$

where A_lobe = ∫_{one-lobe region of κ > 0} κ ds and A_saddle = ∫_{one-saddle region of κ < 0} κ ds. The relation follows from total turning ∮ κ ds = 2π and the 3-fold symmetry (three lobes plus three saddles cover the curve).

The arc clover happens to pick A_lobe = +4π/3 and A_saddle = −2π/3, which together give 2π/3 per fundamental domain. The smooth Fourier curve picks different values of A_lobe and A_saddle depending on (a₁, a₂); only the sum is fixed.

### 4.3 Why this matters

The +2/3 / −1/3 charge assignment in [clover-quarks §3](../../sheet-proton/work/clover-quarks.md) reads charge as the per-radian curvature content:

<!-- Q_region = (1/2π) ∫_{region} κ ds -->
$$
Q_{\text{region}} \;=\; \frac{1}{2\pi} \int_{\text{region}} \kappa \, ds
$$

So:

Q_lobe = A_lobe / (2π)
Q_saddle = A_saddle / (2π)

with A_lobe + A_saddle = 2π/3 forcing **Q_lobe + Q_saddle = 1/3** (a rigid consequence of three-fold symmetry).

For the arc clover, (A_lobe, A_saddle) = (4π/3, −2π/3) gives (Q_lobe, Q_saddle) = (+2/3, −1/3) — the up- and down-quark charges. For a smooth Fourier curve, the same charge formula yields different numbers in general, anywhere along the locus Q_lobe + Q_saddle = 1/3.

The next section discusses how to keep the +2/3 / −1/3 assignment when using the smooth curve as a quark substrate.

---

## 5. Parameterization recipes for specific jobs

### 5.1 Electron tube (selecting the T(1, 2) mode)

**Job:** provide a convex-only bilobe cross-section that supports σ_eff = 2 under a chosen twist, so the T(1, 2) closure mode sits at the energetic floor (per [electron-tube §3](electron-tube.md)).

**Why convex-only.** Concave (κ < 0) regions induce fractional Z_n sectors in the boundary identification, giving fractional charge modes. The electron is integer-charged, so the cross-section must have κ ≥ 0 everywhere.

**Parameter choices:**

| Parameter | Value | Reason |
|---|---|---|
| N | 2 | Bilobe; lowest non-trivial symmetry (C₂) needed to make τ physical |
| a₁ | (0, 1/5) | Below 1/(1 + N²) = 1/5 to keep saddle midpoint convex |
| a₂ | 0 | No second harmonic needed; introduces an unwanted shape complication |
| R | free | Sets the cross-section scale; the electron mass becomes μ_e = 1/ε with ε = R/R_major |
| τ | 2 | Smallest twist with trivial monodromy on C₂ that gives σ_eff = 2 |
| σ (shear) | 0 | None needed |

**What the choices buy.**

- a₂ = 0, a₁ < 1/5 keeps κ > 0 around the whole cross-section. The bilobe is smooth and convex everywhere.
- N = 2 gives C₂ symmetry, sufficient to break the rotational degeneracy (so τ is a meaningful physical parameter rather than gauge) per [electron-tube §4](electron-tube.md).
- τ = 2 means the cross-section rotates twice as θ traverses the ring once. Since R_{2·2π} = R_{4π} = identity on any cross-section (it's a full 720° rotation that returns to start), the boundary identification has trivial monodromy → k_θ integer → integer charge.
- The combination τ = 2, σ = 0 yields σ_eff = σ + τ = 2 (in the trivial-monodromy regime — see [electron-tube §2 table](electron-tube.md)), placing T(1, 2) at the cross-section-only mass floor μ² = (m_t/ε)².

**Note on relation to the true ellipse.** The Fourier-2 curve r(φ) = R(1 + a₁·cos 2φ) is not literally an ellipse — a true ellipse has infinitely many Fourier coefficients in this polar form. For small a₁ the two agree to within a few percent. For physics that depends only on C₂ symmetry and the existence of "a face" on the cross-section (per [electron-tube §4](electron-tube.md)'s WvM-twisted-strip picture), either profile suffices. The Fourier-2 has the practical advantage of being directly comparable to the N = 3 and higher-N cases in the same function family.

### 5.2 Quark / proton tube (reproducing +2/3 / −1/3 charges)

**Job:** provide a three-lobe cross-section with concave saddles, supporting the Q_u = +2/3 / Q_d = −1/3 charge assignment of [clover-quarks §3](../../sheet-proton/work/clover-quarks.md) via the per-region turning integral.

**Why three lobes with concave saddles.** The fractional charges +2/3 and −1/3 are integer fractions of total turning (1/2π · 4π/3 = 2/3 and 1/2π · 2π/3 = 1/3 of a turn). Three convex regions alternating with three concave regions is the smallest shape that splits the 2π total turning into three pieces summing to the fractional values needed.

**Parameter choices:**

| Parameter | Value | Reason |
|---|---|---|
| N | 3 | Three lobes |
| a₁ | > 1/10, tuned by (5.2.1) | Above the concave-saddle threshold; specific value picked to fix A_lobe |
| a₂ | tuned by (5.2.1) | Independent degree of freedom; together with a₁ determines (A_lobe, A_saddle) |
| R | free | Sets the cross-section scale |
| τ | 1/3 | Smallest twist with D₃ closure (τ · N = 1 integer); produces Z_3 monodromy |
| σ | from rolled-leaf | Continuous; affects metric only, not boundary identification (see [clover-quarks §1.3](../../sheet-proton/work/clover-quarks.md)) |

#### 5.2.1 The charge constraint

For the smooth curve to reproduce Q_u = +2/3, the per-lobe turning must equal A_lobe = 4π/3. By the rigid sum-rule of §4.2, this also fixes A_saddle = −2π/3 and hence Q_d = −1/3.

A_lobe is a function of (a₁, a₂):

<!-- A_lobe(a₁, a₂) = ∫_{φ : κ > 0, |φ| < π/3} κ(φ) · sqrt(r² + r'²) dφ -->
$$
A_{\text{lobe}}(a_1, a_2) \;=\; \int_{\varphi : \kappa > 0,\;|\varphi| < \pi/3}\!\! \kappa(\varphi) \,\sqrt{r^2 + r'^2}\, d\varphi
$$

This integral is one equation in two unknowns. Setting it equal to 4π/3 carves out a 1-parameter curve in (a₁, a₂) space — the locus of admissible quark substrates. Every point on this curve is a different shape (different ratio of lobe-prominence to valley-depth) but all satisfy Q_u = +2/3, Q_d = −1/3.

**Quantitative answer: where on (a₁, a₂) space does A_lobe = 4π/3?**

A_lobe is *not* automatically 4π/3 for an arbitrary three-fold-symmetric Fourier curve — the equation A_lobe = 4π/3 is a real constraint that selects a specific 1-parameter family of (a₁, a₂) values out of the full 2D parameter space. Numerical integration of the line integral gives the following:

| a₂ | a₁ that solves A_lobe = 4π/3 | Q_lobe |
|---:|---:|---:|
| −0.10 | 0.534 | +2/3 |
| −0.05 | 0.621 | +2/3 |
| **0.00** | **0.7071** | **+2/3** |
| +0.05 | 0.793 | +2/3 |
| +0.10 | 0.877 | +2/3 |
| +0.15 | (no valid solution; off-axis extrema dominate) | — |

For the single-harmonic case (a₂ = 0), the constraint is satisfied at **a₁ ≈ 1/√2 ≈ 0.7071** (to the precision of the numerical integration). This is the cleanest smooth-clover choice that reproduces the +2/3 / −1/3 quark charges exactly. Adding a positive a₂ requires a correspondingly larger a₁; adding a negative a₂ allows a smaller a₁ (but pushes toward the convexity threshold).

**Caution: matching the symmetry-point peak/trough is not enough.** The "arc-matching" preset (R = 1.4, a₁ = 3/7 ≈ 0.429, a₂ = 0) reproduces the arc-clover's peak r = 2.0 and trough r = 0.8 at the symmetry points, but gives A_lobe ≈ 3.41 (rather than 4π/3 ≈ 4.19) and hence Q_lobe ≈ 0.54 (rather than +2/3). Matching radial extrema is a weaker condition than matching per-region turning. To reproduce the quark charges, tune to the (a₁, a₂) locus above, not to the extrema-matching preset.

**Practical procedure.**

1. Pick a desired a₂ (start with 0).
2. Adjust a₁ so that A_lobe (numerically integrated) equals 4π/3. For a₂ = 0 the answer is a₁ ≈ 0.7071.
3. Pick R to set the absolute size of the cross-section (e.g., to fit a target peak radius). R does not enter the charge calculation (Q is scale-invariant).
4. Verify a₁ > 4·|a₂| (no off-axis extrema) and a₁(N² + 1) − a₂(4N² + 1) > 1 (saddle midpoint concave). The locus above satisfies both inside the table range.

**Caution — two thresholds to clear, not one.** Two distinct conditions need to hold simultaneously for a clean three-lobe-three-saddle clover:

1. **No off-axis extrema:** a₁ > 4·|a₂| keeps the radial peaks at the lobe-axes (φ = 2πk/N) and the radial troughs at the saddle midpoints (φ = (2k+1)π/N). If a₁ ≤ 4·|a₂|, additional extrema appear at cos(Nφ) = −a₁/(4a₂) — the curve develops bulges between the lobe and saddle.

2. **Concave saddle midpoint:** a₁(N² + 1) − a₂(4N² + 1) > 1 (derived in §3). If this fails, the saddle midpoint has κ ≥ 0 (convex).

For (a₁, a₂) = (0.48, 0.12) at N = 3, condition (1) is at the boundary (a₁ = 4·a₂ exactly) but condition (2) fails (10·0.48 − 37·0.12 = 0.36 < 1). The result is a peculiar shape: a small convex nub at the saddle midpoint (κ = 1/r > 0) surrounded by concave wings on either side. Not a clean clover. To enter the clean regime while keeping a₂ = 0.12, increase a₁ past ≈ 0.544 (so condition (2) is satisfied).

**Position in the family.** The arc clover sits at a *limiting* point of the broader 1-parameter family A_lobe = 4π/3: the limit where κ is piecewise constant (κ = +1/r_L on lobes, κ = −1/r_S on saddles, with curvature discontinuities at the six junctions). The smooth Fourier versions populate the rest of the constraint curve with continuous κ.

### 5.3 Higher-N cross-sections

The function family extends naturally to N ≥ 4. None of these are currently identified with any specific particle:

| N | Shape (small a₁, a₂ = 0) | Shape (with concave saddles) |
|---|---|---|
| 4 | rounded square | quad-clover (four lobes, four saddles) |
| 5 | rounded pentagon | penta-clover |
| 6 | rounded hexagon | hexa-clover |

The same Gauss-Bonnet sum rule applies with the 3 replaced by N:

<!-- per fundamental domain at N-fold symmetry: A_lobe + A_saddle = 2π/N -->
$$
A_{\text{lobe}} \;+\; A_{\text{saddle}} \;=\; \frac{2\pi}{N}
$$

so Q_lobe + Q_saddle = 1/N for the per-region charge. This is a rigid prediction of the framework — any future-identified particle hosted on an N-lobe cross-section has its per-region charges constrained by 1/N.

---

## 6. Twist closure

The tube is the cross-section swept around a ring of radius R_major, with the cross-section rotating by an angle α = τ·θ as the ring angle θ advances. The surface closes onto itself at θ = 2π iff the rotation R_{2π·τ} maps the cross-section to itself — i.e., 2π·τ is a multiple of the cross-section's rotational symmetry angle 2π/N:

<!-- τ · N ∈ ℤ -->
$$
\tau \cdot N \;\in\; \mathbb{Z}
$$

So the admissible twists are τ ∈ {k/N : k ∈ ℤ}.

The two main constructions land at:

- **Proton clover:** N = 3, τ = 1/3 (so τ·N = 1, satisfied). The rotation by 2π/3 per ring rev is the source of the Z_3 monodromy that produces fractional k_θ ∈ {0, 1/3, 2/3} and the fractional quark charges.

- **Electron bilobe:** N = 2, τ = 2 (so τ·N = 4, satisfied). The rotation by 2·2π = 4π per ring rev is a full 720° = two full identities on C₂. Monodromy is trivial, k_θ ∈ ℤ, charge integer.

Other admissible values for each N produce variants (e.g., N = 2 with τ = 1/2 gives the Z_2 case discussed in [electron-tube §5.1](electron-tube.md) — same C₂ profile but with half-integer monodromy, yielding fractional charge).

---

## 7. Summary

A single smooth function family

<!-- r(φ) = R · [1 + a₁·cos(N·φ) + a₂·cos(2·N·φ)] -->
$$
r(\varphi) \;=\; R \cdot \bigl[\, 1 + a_1 \cos(N\varphi) + a_2 \cos(2N\varphi) \,\bigr]
$$

generates cross-sections from circle (a₁ = a₂ = 0) through rounded polygons (small a₁) up to lobed-and-cuspy clover shapes (large a₁, a₂). The function is C^∞ everywhere with a closed-form analytic curvature κ(φ).

Two physical constructions land on specific parameter choices in this family:

- **Electron T(1, 2):** N = 2, a₁ ∈ (0, 1/5), a₂ = 0, τ = 2 — bilobe, all convex, integer-charge, T(1, 2) at the floor.
- **Proton / quark:** N = 3, (a₁, a₂) tuned so A_lobe = 4π/3, τ = 1/3 — three-lobe-three-saddle, fractional Z_3 charge with Q_u = +2/3, Q_d = −1/3.

The 240° / 120° split observed in the arc clover is *not* automatic in the smooth case. The Gauss-Bonnet sum A_lobe + A_saddle = 2π/N is rigid; the individual values depend on the smooth shape's parameters, with a one-parameter family of (a₁, a₂) values reproducing the arc clover's charge assignment.

The same function family is open for future-identified particles at higher N — each carries a rigid Q_lobe + Q_saddle = 1/N constraint that a candidate identification must respect.
