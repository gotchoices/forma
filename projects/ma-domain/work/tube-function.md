# tube-function.md — a generalized cross-section function for the corrugated tube

**Status:** Working hypothesis / how-to. Documents a smooth harmonic curve family for the corrugated-tube cross-section. The family is built from sinusoids, is C^∞ everywhere (no curvature jumps), and contains — as exact members — the circle, the **true ellipse** used as the electron tube, rounded N-gons, and the three-lobe clover used for quarks. A single parameter set dials smoothly between all of them. Records how to fit each particle-construction job with specific parameter choices.

**Cross-references:**
- [electron-tube.md](electron-tube.md) — bilobe tube with twist τ=2 as the T(1,2) electron host
- [sheet-proton clover-quarks.md §1.1, §3](../../sheet-proton/work/clover-quarks.md) — arc-clover three-lobe construction and the +2/3 / −1/3 charge accounting
- [viz/tube-lab](../../../viz/tube-lab.md) — interactive visualizer for this function family
- [scripts/harmonic_tube.py](../scripts/harmonic_tube.py) — verification script (ellipse exactness, A_lobe loci); output in [outputs/harmonic_tube.txt](../outputs/harmonic_tube.txt)

---

## 1. Motivation

Several different tube cross-sections appear in the framework:

- **Circle** — the featureless degenerate case.
- **Ellipse** ([electron-tube.md §5](electron-tube.md)) — a C₂-symmetric convex profile. Under twist τ=2 it makes T(1, 2) the lightest m_t = 1 mode (the WvM electron).
- **Arc clover** ([clover-quarks.md §1.1](../../sheet-proton/work/clover-quarks.md)) — three convex 240° lobe arcs joined to three concave 120° saddle arcs by tangency. C¹ but not C² — curvature jumps at the six lobe–saddle junctions.

All are N-fold symmetric, twist-bearing cross-sections for the corrugated tube. We want **one function family** that:

1. produces shapes with a chosen number N of lobes,
2. keeps each lobe convex by construction,
3. lets the lobe prominence be dialed,
4. optionally develops concave valleys between lobes, with the valley depth dialed independently,
5. is built only from sinusoids and is continuous (C^∞) with closed-form curvature,
6. can reproduce the 240°/120° turning split that gives quarks their +2/3 / −1/3 charges,
7. degenerates cleanly to circle, rounded square, rounded triangle, **and a true ellipse**.

An earlier version of this document used a *polar* curve r(φ). That form meets goals 1–6 but **fails goal 7's ellipse case**: a true ellipse is not a finite cosine series in its own polar angle. This version uses a harmonic curve parameterized by a free parameter t. It contains the polar curve as a special slice and the true ellipse as another, so every goal above is met at once.

---

## 2. The function

### 2.1 The harmonic form

Write a point of the cross-section as a complex number z = x + i·y. The curve is

<!-- z(t) = R · e^{i t} · [ 1 + a1 cos(Nt) + a2 cos(2Nt) + i ( b1 sin(Nt) + b2 sin(2Nt) ) ] -->
$$
z(t) \;=\; R\,e^{i t}\,\Bigl[\, 1 + a_1\cos(Nt) + a_2\cos(2Nt) \;+\; i\bigl(\, b_1\sin(Nt) + b_2\sin(2Nt) \,\bigr) \,\Bigr],
\qquad t \in [0, 2\pi)
$$

The bracket is a **complex shape function** w(t):

<!-- w(t) = [1 + a1 cos(Nt) + a2 cos(2Nt)]  +  i[b1 sin(Nt) + b2 sin(2Nt)] -->
$$
w(t) \;=\; \underbrace{1 + a_1\cos(Nt) + a_2\cos(2Nt)}_{\text{real part} \;=\; \text{radius profile}} \;+\; i\,\underbrace{\bigl(b_1\sin(Nt) + b_2\sin(2Nt)\bigr)}_{\text{imag. part} \;=\; \text{angular drift}}
$$

so z(t) = R·e^{it}·w(t). The factor e^{it} carries the point around once; w(t) modulates both its distance from the origin and its angular position.

Five parameters:

| Parameter | Symbol | Role |
|---|---|---|
| Lobe count | N ∈ ℤ, N ≥ 2 | Number of N-fold symmetric features per revolution |
| Mean radius | R | Overall scale |
| First-harmonic amplitude | a₁ | Gross radial swing between lobe peaks and saddle valleys |
| Second-harmonic amplitude | a₂ | Sharpens or flattens valleys |
| First-harmonic **split** | b₁ | Asymmetry of the first harmonic — the new knob (see §2.3) |
| Second-harmonic **split** | b₂ | Asymmetry of the second harmonic |

Because cos(Nt), sin(Nt) and the 2N terms are all 2π/N-periodic, w(t + 2π/N) = w(t), and

z(t + 2π/N) = e^{i·2π/N}·z(t)

— the curve has exact N-fold rotational symmetry. With real coefficients it is also mirror-symmetric, so the full symmetry group is the dihedral group D_N (a mirror line through every lobe and every valley).

### 2.2 The polar slice — the shortcut for goals 1–6

Set **b₁ = b₂ = 0**. Then w(t) is real, w(t) = 1 + a₁cos(Nt) + a₂cos(2Nt), and

z(t) = R·[1 + a₁cos(Nt) + a₂cos(2Nt)]·e^{it}

This is exactly the polar curve r(φ)·e^{iφ} with the parameter t playing the role of the geometric polar angle φ:

<!-- r(φ) = R[1 + a1 cos(Nφ) + a2 cos(2Nφ)]   (the b1 = b2 = 0 slice) -->
$$
r(\varphi) \;=\; R\,\bigl[\, 1 + a_1\cos(N\varphi) + a_2\cos(2N\varphi) \,\bigr]
\qquad\text{(the } b_1 = b_2 = 0 \text{ slice)}
$$

So the old polar tube-function is **not a different family** — it is the harmonic family restricted to b = 0. Whenever the splits vanish, t and the geometric angle φ coincide, and all the convenient polar readouts (radius at the lobe peak, radius at the saddle) are exact. This slice is the natural input mode for any shape that does *not* need an ellipse: circle, rounded N-gon, smooth clover, the quark tube. Treat it as the **polar shortcut** — specify (N, R, a₁, a₂), leave b at zero.

### 2.3 What the split parameter does

Expand z(t) into pure harmonics using cos x = (e^{ix}+e^{−ix})/2 and sin x = (e^{ix}−e^{−ix})/2i:

<!-- z/R = e^{it} + ((a1+b1)/2) e^{i(1+N)t} + ((a1-b1)/2) e^{i(1-N)t} + ((a2+b2)/2) e^{i(1+2N)t} + ((a2-b2)/2) e^{i(1-2N)t} -->
$$
\frac{z(t)}{R} \;=\; e^{it} \;+\; \tfrac{a_1+b_1}{2}\,e^{i(1+N)t} \;+\; \tfrac{a_1-b_1}{2}\,e^{i(1-N)t} \;+\; \tfrac{a_2+b_2}{2}\,e^{i(1+2N)t} \;+\; \tfrac{a_2-b_2}{2}\,e^{i(1-2N)t}
$$

Each harmonic level (1±N, and 1±2N) has an **inner** partner e^{i(1−mN)t} and an **outer** partner e^{i(1+mN)t}. The amplitude aₘ is their average; the split bₘ is their difference:

- **bₘ = 0** → inner and outer partners equal → the polar slice. This is the constraint a polar curve always satisfies.
- **bₘ ≠ 0** → the partners differ. The curve is still smooth, sinusoidal, and D_N-symmetric, but t no longer equals the geometric angle.

The split is the one degree of freedom the polar form cannot express — and it is exactly what is needed for the ellipse (see §5.1). Compared to the old polar tube-function the family has gained **two parameters**, b₁ and b₂ — one split per harmonic level. In practice b₁ is the one that matters; b₂ is a fine-tuning knob and can be left at zero for every shape currently in use.

### 2.4 Derived quantities at the symmetry points

At the lobe axis (t = 0) and the saddle midpoint (t = π/N), every sin(Nt) and sin(2Nt) vanishes, so the imaginary part of w is zero and w is real there. Two consequences:

1. The lobe peak sits at geometric angle 0 and the saddle midpoint at π/N regardless of b — the splits do not move the symmetry points.
2. The **radii at the symmetry points are unchanged from the polar form**:

<!-- r_lobe = R(1 + a1 + a2);  r_saddle = R(1 - a1 + a2) -->
$$
r_{\text{lobe}} \;\equiv\; |z(0)| \;=\; R\,(1 + a_1 + a_2),
\qquad
r_{\text{saddle}} \;\equiv\; |z(\pi/N)| \;=\; R\,(1 - a_1 + a_2)
$$

The split parameters reshape the curve *between* the symmetry points (and redistribute curvature); they leave the peak and trough radii alone. As before, with peak prominence p and valley depth v as radial fractions,

p = (r_lobe − R)/R = a₁ + a₂,  v = (R − r_saddle)/R = a₁ − a₂,  ⟹  a₁ = ½(p + v),  a₂ = ½(p − v)

(exact when the global extrema sit at the symmetry points — see §3).

### 2.5 Curvature

For a parametric plane curve z(t), the signed curvature is

<!-- κ(t) = Im( conj(z') · z'' ) / |z'|^3 -->
$$
\kappa(t) \;=\; \frac{\operatorname{Im}\!\bigl(\overline{z'(t)}\;z''(t)\bigr)}{\lvert z'(t)\rvert^{3}}
$$

with arc-length element ds = |z′(t)| dt. From z = R·e^{it}·w,

z′ = R·e^{it}·(i·w + w′),  z″ = R·e^{it}·(−w + 2i·w′ + w″)

and w, w′, w″ are finite sums of sin/cos, so κ(t) is a closed-form smooth function with no piecewise stitching. This is the geometric improvement over the arc clover: every derivative of the cross-section is continuous everywhere. In the polar slice (b = 0, w real, t = φ) the formula reduces to the familiar κ = (r² + 2r′² − r·r″)/(r² + r′²)^{3/2}.

---

## 3. When does the curve develop concave saddles?

Total signed turning ∮ κ ds = 2π is fixed by Gauss–Bonnet for any simple closed plane curve. The *sign* of κ at a point depends on the shape, so a smooth curve may be everywhere convex (κ > 0) or have alternating convex / concave regions.

At the saddle midpoint t = π/N the derivatives of w take the values w = w₀, w′ = i·w₁, w″ = w₂ with

w₀ = 1 − a₁ + a₂,  w₁ = N(2b₂ − b₁),  w₂ = N²(a₁ − 4a₂)

Substituting into the curvature formula (with w₀ + w₁ > 0):

<!-- κ(π/N) = (w0 + 2 w1 - w2) / [ R (w0 + w1)^2 ] -->
$$
\kappa(\pi/N) \;=\; \frac{w_0 + 2w_1 - w_2}{R\,(w_0 + w_1)^2}
$$

The denominator is positive, so the saddle is genuinely concave (κ < 0) iff the numerator is negative. Writing it out:

<!-- saddle concave  ⟺  a1(1+N^2) - a2(1+4N^2) + 2N(b1 - 2 b2) > 1 -->
$$
a_1\,(1 + N^2) \;-\; a_2\,(1 + 4N^2) \;+\; 2N\,(b_1 - 2b_2) \;>\; 1
$$

Setting b = 0 recovers the polar threshold a₁(1+N²) − a₂(1+4N²) > 1. The split contributes the extra term 2N(b₁ − 2b₂): **a positive b₁ lowers the threshold** — the saddle goes concave at smaller radial swing. This is the analytic counterpart of the numerical finding in §5.2.

Single-harmonic polar case (a₂ = b₁ = b₂ = 0): saddle concave iff a₁ > 1/(1 + N²). Thresholds:

| N | a₁ threshold for concave saddle |
|---:|---:|
| 2 | 1/5 = 0.200 |
| 3 | 1/10 = 0.100 |
| 4 | 1/17 ≈ 0.059 |
| 5 | 1/26 ≈ 0.038 |
| 6 | 1/37 ≈ 0.027 |

The lobe peak t = 0 carries the same formula with w₀ → 1+a₁+a₂, w₁ → N(b₁+2b₂), w₂ → −N²(a₁+4a₂); for the amplitudes in use it stays positive (convex lobe). So with four shape knobs (a₁, a₂, b₁, b₂) the curvature at the lobe peak and at the saddle midpoint can be set **independently** — i.e. the osculating-circle radius of the lobe centre and of the valley centre are separately dialable, meeting goals 3 and 4.

---

## 4. The 240°/120° question

A natural question from the arc clover: does the smooth three-lobe curve always present a 240° convex / 120° concave split?

**Answer:** No. The arc clover's 240°/120° split is specific to the piecewise-circular construction. The smooth curve has a parameter-dependent split. What is rigid is the *turning content*, and that is **parameterization-independent** — it depends only on the curve, not on whether we describe it polar or harmonic. So this section is unchanged by the move to the harmonic basis.

### 4.1 The rigid sum rule

For any simple closed smooth plane curve with N-fold symmetry and N convex regions alternating with N concave regions, total turning ∮ κ ds = 2π plus the symmetry give, per fundamental domain,

<!-- A_lobe + A_saddle = 2π / N -->
$$
A_{\text{lobe}} \;+\; A_{\text{saddle}} \;=\; \frac{2\pi}{N},
\qquad
A_{\text{lobe}} = \!\!\int_{\kappa > 0}\!\! \kappa\,ds,
\quad
A_{\text{saddle}} = \!\!\int_{\kappa < 0}\!\! \kappa\,ds
$$

The arc clover happens to pick A_lobe = +4π/3 and A_saddle = −2π/3 (summing to 2π/3 for N = 3). A smooth curve picks different individual values; only the sum is fixed.

### 4.2 Why this matters — quark charge

The +2/3 / −1/3 charge assignment in [clover-quarks.md §3](../../sheet-proton/work/clover-quarks.md) reads charge as per-radian curvature content, Q_region = (1/2π) ∫_region κ ds. So

Q_lobe = A_lobe/(2π),  Q_saddle = A_saddle/(2π),  with  Q_lobe + Q_saddle = 1/N.

For N = 3 the up/down quark charges Q_lobe = +2/3, Q_saddle = −1/3 require **A_lobe = 4π/3**. That is a real constraint on the shape parameters, addressed in §5.2.

---

## 5. Parameterization recipes for specific jobs

### 5.1 Electron tube — now a true ellipse

**Job:** provide a convex-only C₂ cross-section that, under twist τ = 2, puts the T(1, 2) closure mode at the energetic floor (per [electron-tube.md §3](electron-tube.md)). [electron-tube.md §5](electron-tube.md) names the ideal profile an **ellipse**.

The harmonic family delivers a *literal* ellipse. Take N = 2, a₂ = b₂ = 0, and set the first-harmonic split to cancel the outer partner:

<!-- ellipse:  N = 2,  a2 = b2 = 0,  b1 = -a1 -->
$$
b_1 \;=\; -\,a_1
\quad\Longrightarrow\quad
\frac{z(t)}{R} \;=\; e^{it} + a_1\,e^{-it}
\;=\; (1+a_1)\cos t \;+\; i\,(1-a_1)\sin t
$$

This is an exact ellipse with semi-axes

A = R(1 + a₁) (major),  B = R(1 − a₁) (minor),  foci separation = 2√(A² − B²) = **4R√a₁**.

So a₁ directly controls the eccentricity, and the foci separation is 4R√a₁ — a single tunable geometric parameter. [harmonic_tube.py](../scripts/harmonic_tube.py) confirms the curve satisfies (x/A)² + (y/B)² = 1 to ~10⁻¹⁵ (machine precision) across a₁ ∈ [0.1, 0.7]. An ellipse is convex for every a₁ ∈ (0, 1), so the convex-only requirement is met automatically with no threshold to watch.

| Parameter | Value | Reason |
|---|---|---|
| N | 2 | Bilobe; C₂ symmetry needed to make τ physical |
| a₁ | (0, 1) free | Sets eccentricity; foci separation = 4R√a₁ |
| b₁ | −a₁ | Cancels the outer harmonic → exact ellipse |
| a₂, b₂ | 0 | Not needed |
| R | free | Cross-section scale; electron mass μ_e = 1/ε |
| τ | 2 | Smallest twist with trivial monodromy on C₂ giving σ_eff = 2 |
| σ (shear) | 0 | None needed |

The ellipse named in [electron-tube.md §5](electron-tube.md) is therefore not an approximation forced by a truncated series — it is an exact, single-parameter member of the same family that produces the quark clover.

(The polar slice b₁ = 0 at N = 2 still gives the *ellipse-like bilobe* r = R(1 + a₁cos 2φ). It agrees with the true ellipse to a few percent for small a₁ but is a genuinely different curve — it goes concave for a₁ > 1/5, whereas the true ellipse never does. Use b₁ = −a₁ for the literal ellipse.)

### 5.2 Quark / proton tube — reproducing +2/3 / −1/3 charges

**Job:** a three-lobe cross-section with concave saddles that satisfies A_lobe = 4π/3, hence Q_u = +2/3, Q_d = −1/3.

**Polar slice (b = 0) — the baseline.** With b₁ = b₂ = 0 the constraint A_lobe = 4π/3 carves a one-parameter locus in (a₁, a₂). Numerical integration ([harmonic_tube.py](../scripts/harmonic_tube.py), N = 3):

| a₂ | a₁ solving A_lobe = 4π/3 | κ_min (valley) |
|---:|---:|---:|
| −0.10 | 0.534 | −59.9 |
| −0.05 | 0.621 | −65.0 |
| **0.00** | **0.7071** | **−70.8** |
| +0.05 | 0.793 | −76.8 |
| +0.10 | 0.877 | −81.9 |

For the single-harmonic polar case (a₂ = 0) the constraint is met at **a₁ ≈ 1/√2 ≈ 0.7071** — a large radial swing (lobe peak 71% above the mean).

**Unlocking b₁ — the new freedom.** With a₂ = b₂ = 0 and b₁ free, A_lobe = 4π/3 is solved at ([harmonic_tube.py](../scripts/harmonic_tube.py), N = 3):

| b₁ | a₁ solving A_lobe = 4π/3 | r_peak / r_mean | κ_min (valley) |
|---:|---:|---:|---:|
| −0.30 | 1.291 | 2.29 | −27.3 |
| −0.20 | 1.100 | 2.10 | −35.1 |
| −0.10 | 0.905 | 1.91 | −47.8 |
| **0.00** | **0.707** | **1.71** | **−70.8** |
| +0.10 | 0.504 | 1.50 | −121 |
| +0.20 | 0.294 | 1.29 | −281 |
| +0.30 | 0.070 | 1.07 | −1620 |

**What this shows.** The quark clover is no longer a single fine-tuned point — A_lobe = 4π/3 becomes a one-parameter *family* of valid shapes indexed by b₁. The split lets the lobe carry the +2/3 charge with **far less radial swing**: at b₁ = +0.2 the lobe reaches 4π/3 with a₁ ≈ 0.29 instead of 0.71, and the peak is only 29% above the mean instead of 71%. The lobes are rounder and fatter relative to their prominence — the lobe charge no longer demands an extreme bulge.

The trade is valley sharpness. As b₁ increases, κ_min plunges (the valley curves toward a cusp — the curve heads for the deltoid/hypocycloid limit). Conversely, negative b₁ buys a *gentler* valley (κ_min = −27 at b₁ = −0.3 versus −71 in the polar slice) at the cost of a larger radial swing. So b₁ is a knob that, at fixed quark charge, trades radial swing against valley curvature. Pick the member of the family whose valley sharpness is acceptable for the construction at hand; b₁ ≈ 0 (the old polar a₁ ≈ 0.707) remains a reasonable middle choice.

| Parameter | Value | Reason |
|---|---|---|
| N | 3 | Three lobes |
| a₁, b₁ | on the A_lobe = 4π/3 locus above | Fixes Q_lobe = +2/3 |
| a₂, b₂ | 0 (or used to fine-tune the locus) | Extra freedom |
| R | free | Cross-section scale (charge is scale-invariant) |
| τ | 1/3 | Smallest twist with D₃ closure (τ·N = 1) → Z₃ monodromy |
| σ | from rolled-leaf | Metric only, not boundary identification |

**Validity checks.** Keep the curve simple (no self-intersection) and the saddle genuinely concave: large combined amplitudes can drive the tangent to wind more than once. [harmonic_tube.py](../scripts/harmonic_tube.py) flags this — every entry in the tables above is a verified simple closed curve.

**Position in the family.** The arc clover sits at a *limiting* point of the broader family: the limit of piecewise-constant κ (constant on each lobe arc, constant on each saddle arc, with curvature jumps at the six junctions). The smooth harmonic versions populate the rest of the A_lobe = 4π/3 surface with continuous κ.

### 5.3 Higher-N cross-sections

The family extends to N ≥ 4 (rounded square / quad clover, rounded pentagon, etc.). None is currently identified with a particle. The Gauss–Bonnet sum rule A_lobe + A_saddle = 2π/N gives Q_lobe + Q_saddle = 1/N — a rigid prediction any future N-lobe identification must respect.

---

## 6. Twist closure

The tube is the cross-section swept around a ring of radius R_major, with the cross-section rotating by α = τ·θ as the ring angle θ advances. The surface closes at θ = 2π iff the rotation R_{2πτ} maps the cross-section to itself — i.e. 2πτ is a multiple of the symmetry angle 2π/N:

<!-- τ · N ∈ ℤ -->
$$
\tau \cdot N \;\in\; \mathbb{Z}
$$

So the admissible twists are τ ∈ {k/N : k ∈ ℤ}. This depends only on the N-fold symmetry, which the harmonic family preserves for any (a, b) — closure is unaffected by the split parameters.

The two main constructions land at:

- **Proton clover:** N = 3, τ = 1/3 (τ·N = 1). Rotation by 2π/3 per ring rev → Z₃ monodromy → fractional k_θ ∈ {0, 1/3, 2/3} → fractional quark charges.
- **Electron ellipse:** N = 2, τ = 2 (τ·N = 4). Rotation by 4π per ring rev = two full identities on C₂ → trivial monodromy → k_θ ∈ ℤ → integer charge.

---

## 7. Summary

A single smooth harmonic family

<!-- z(t) = R e^{it} [ 1 + a1 cos(Nt) + a2 cos(2Nt) + i(b1 sin(Nt) + b2 sin(2Nt)) ] -->
$$
z(t) \;=\; R\,e^{it}\,\Bigl[\, 1 + a_1\cos(Nt) + a_2\cos(2Nt) + i\bigl(b_1\sin(Nt) + b_2\sin(2Nt)\bigr) \,\Bigr]
$$

generates cross-sections from circle (a = b = 0) through rounded polygons up to lobed clover shapes — and, uniquely among the forms tried, the **exact ellipse**. It is C^∞ everywhere with closed-form curvature κ = Im(z̄′z″)/|z′|³.

- **Polar shortcut** — set b₁ = b₂ = 0. Then t equals the geometric angle and z reduces to the polar curve r(φ) = R[1 + a₁cos Nφ + a₂cos 2Nφ]. This is the input mode for circle, rounded N-gon, smooth clover.
- **Electron T(1, 2):** N = 2, a₂ = b₂ = 0, b₁ = −a₁, τ = 2 — an exact ellipse, semi-axes R(1±a₁), foci separation 4R√a₁, convex for every a₁ ∈ (0, 1).
- **Proton / quark:** N = 3, (a₁, b₁) on the A_lobe = 4π/3 locus, τ = 1/3 — three lobes, concave saddles, Q_u = +2/3, Q_d = −1/3. The split b₁ turns the old single fine-tuned point into a one-parameter family and lets the lobe carry its charge with much less radial swing.

The 240°/120° split is *not* automatic; the Gauss–Bonnet sum A_lobe + A_saddle = 2π/N is rigid and parameterization-independent, with a family of (a₁, a₂, b₁, b₂) values reproducing the arc clover's charge assignment. The family is open for future-identified particles at higher N, each carrying a rigid Q_lobe + Q_saddle = 1/N constraint.
