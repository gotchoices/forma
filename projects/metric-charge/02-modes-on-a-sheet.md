# Chapter 2 — Modes on a sheet

This chapter takes the givens of [Chapter 1](01-foundation.md) — the manifold M, the bare diagonal metric, the real scalar field φ, the massless wave equation □φ = 0, and the periodicity conditions on (u, w) — and works out which solutions the wave equation actually admits. The technical core is a Bloch decomposition on the 2-torus (u, w), which produces a discrete (m, n) mode family.

**Substantial inheritance.**

- *From [grid-duality §7](../grid-duality/07-wrap-promotion-modeling.md):* Bloch decomposition on a 2D periodic substrate, the band-extremum origin of mass, and the integer-quantization of winding numbers.
- *From [metric-mass Chapter 2](../metric-mass/02-mass-from-u.md):* the slow-motion inertial-mass argument carries over with one extra integer index.

This chapter does not re-derive any of those. It cites them and specializes their results to the metric-charge setting (continuum 2-torus rather than discrete lattice; spacetime embedding rather than abstract substrate).

The chapter's distinctive job is the spacetime-side framing: identifying the (0, 0) zero mode with massless propagation in (S₁, S₂), naming the single-axis (m, 0) and (0, n) modes as **L2-embedded-in-L3** candidates for closure-failure mass-only states (candidate structural origins of *non-charged massive states* — neutrinos, dark matter, certain neutral hadrons, etc., without commitment to which), and setting up the (m, n) labels for use in chapters 3–9.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | Setting up the problem: wave equation, separation, periodicity |
| 2 | The (m, n) mode family |
| 3 | The dispersion relation and the rest-mass formula |
| 4 | Three mode classes: light, single-axis, diagonal |
| 5 | Energy, momentum, and the topological-winding identification |
| 6 | What's next |

---

## 1. Setting up the problem: wave equation, separation, periodicity

We solve the wave equation on M. From [Chapter 1 §8](01-foundation.md):

<!-- (-1/c²)∂²φ/∂t² + ∂²φ/∂S₁² + ∂²φ/∂S₂² + ∂²φ/∂u² + ∂²φ/∂w² = 0 -->
$$
-\frac{1}{c^2}\frac{\partial^2\varphi}{\partial t^2}
+\frac{\partial^2\varphi}{\partial S_1^2}
+\frac{\partial^2\varphi}{\partial S_2^2}
+\frac{\partial^2\varphi}{\partial u^2}
+\frac{\partial^2\varphi}{\partial w^2}
= 0
$$

This is a partial differential equation in five variables. As in [metric-mass Chapter 2 §1](../metric-mass/02-mass-from-u.md), we attack it with **separation of variables**: assume φ factorizes as

<!-- φ(t, S₁, S₂, u, w) = T(t) X₁(S₁) X₂(S₂) U(u) W(w) -->
$$
\varphi(t, S_1, S_2, u, w) = T(t)\,X_1(S_1)\,X_2(S_2)\,U(u)\,W(w)
$$

substitute into the wave equation, divide through by the product, and ask each term to depend on only one variable. Five terms emerge:

<!-- -1/c² · T''/T + X₁''/X₁ + X₂''/X₂ + U''/U + W''/W = 0 -->
$$
-\frac{1}{c^2}\,\frac{T''(t)}{T(t)}
+\frac{X_1''(S_1)}{X_1(S_1)}
+\frac{X_2''(S_2)}{X_2(S_2)}
+\frac{U''(u)}{U(u)}
+\frac{W''(w)}{W(w)}
= 0
$$

Each ratio depends on only one variable, but their sum is zero everywhere. The standard separation-constant argument gives five ordinary differential equations linked by one algebraic constraint:

<!-- T''/T = -ω², X_i''/X_i = -k_{S_i}², U''/U = -k_u², W''/W = -k_w² -->
$$
\frac{T''}{T} = -\omega^2, \quad \frac{X_i''}{X_i} = -k_{S_i}^2, \quad \frac{U''}{U} = -k_u^2, \quad \frac{W''}{W} = -k_w^2
$$

with the **dispersion relation**

<!-- ω²/c² = k_{S₁}² + k_{S₂}² + k_u² + k_w² -->
$$
\frac{\omega^2}{c^2} = k_{S_1}^2 + k_{S_2}^2 + k_u^2 + k_w^2
$$

linking them.

The (T, X₁, X₂) equations are routine — same form as metric-mass §3, just with one extra spatial direction. The substantive new content lives in the joint (U, W) sub-problem, which is a Bloch decomposition on the 2-torus.

For the full Bloch machinery — plane-wave decomposition on a periodic substrate, band structure, conserved quantities under translation — we cite [grid-duality §7.3](../grid-duality/07-wrap-promotion-modeling.md). Here we work in the **continuum** 2-torus rather than a discrete lattice, which simplifies the mathematics: the dispersion is exact, not approximate, and the (m, n) labels (§2) range over all of ℤ² rather than a finite Brillouin set.

---

## 2. The (m, n) mode family

The (U, W) sub-problem is two ODEs with periodic boundary conditions:

<!-- U''(u) = -k_u² U(u), with U(u + L_u) = U(u) -->
$$
U''(u) = -k_u^2\,U(u), \qquad U(u + L_u) = U(u)
$$

<!-- W''(w) = -k_w² W(w), with W(w + L_w) = W(w) -->
$$
W''(w) = -k_w^2\,W(w), \qquad W(w + L_w) = W(w)
$$

For each direction independently, the periodicity condition picks out the discrete spectrum:

<!-- k_u = 2π m / L_u, m ∈ ℤ;  k_w = 2π n / L_w, n ∈ ℤ -->
$$
k_u = \frac{2\pi\,m}{L_u}, \quad m \in \mathbb{Z}; \qquad k_w = \frac{2\pi\,n}{L_w}, \quad n \in \mathbb{Z}
$$

The mode is labeled by an **integer pair (m, n)**. This is the same kind of integer quantization metric-mass derived for a single compact direction, doubled.

**Integers in ℤ, including negatives.** The integers m and n range over all of ℤ, including negative values. On a real-valued φ (per [Chapter 1 §6](01-foundation.md)), each (m, n) and its sign-reflected partner (−m, −n) corresponds to a distinct configuration: the standing-wave magnitude is the same (so the energy density and rest mass per §3 are the same), but the wave's traversal orientation along the closed curve T(m, n) is opposite. Per [Chapter 1 §6.1](01-foundation.md), this is the geometric origin of the sign — a topological property of oriented closed curves on the 2-torus, not an internal field-theoretic structure. Sign-of-(m, n) tracks which direction the wave packet's phase advances; magnitude-of-(m, n) tracks how often it wraps each cycle.

The integer pair (m, n) is the substrate for everything in chapters 3–9. The closure condition (chapter 4) is a rule about which (m, n) pairs satisfy it. The knot family (chapter 3) is the geometric picture of (m, n) as closed paths on the torus. The gauge-promotion question (chapter 5) asks which (m, n) modes source off-diagonals with the right structure.

### Identification with grid-duality's winding pair

In [grid-duality §7.5](../grid-duality/07-wrap-promotion-modeling.md), the topological invariants on a 2-torus are integer windings (w_α, w_β) ∈ ℤ², with each winding the line integral of the wavevector around its corresponding cycle:

<!-- w_α = (1/2π) ∮_α k · dx,  w_β = (1/2π) ∮_β k · dx -->
$$
w_\alpha = \frac{1}{2\pi}\oint_\alpha \mathbf{k}\cdot d\mathbf{x}, \qquad w_\beta = \frac{1}{2\pi}\oint_\beta \mathbf{k}\cdot d\mathbf{x}
$$

For our Bloch modes with k_u = 2πm/L_u and k_w = 2πn/L_w, these line integrals evaluate exactly to (m, n).

So the (m, n) labels of this chapter and the (w_α, w_β) windings of grid-duality are **the same integers**, viewed from two sides. The phase-pattern view (here) and the topological view (grid-duality) agree on the integer-quantization of winding by construction.

This is one of the equivalences flagged in Chapter 1 §10: integer winding numbers manifest as 2π phase wraps. We use either notation interchangeably depending on which side of the bridge we are working on.

---

## 3. The dispersion relation and the rest-mass formula

Substituting the quantized (k_u, k_w) into the dispersion relation gives

<!-- ω²/c² = k_S² + (2πm/L_u)² + (2πn/L_w)² -->
$$
\frac{\omega^2}{c^2} = k_S^2 + \left(\frac{2\pi\,m}{L_u}\right)^2 + \left(\frac{2\pi\,n}{L_w}\right)^2
$$

where we have collected the spatial momentum into a single magnitude k_S² = k_{S₁}² + k_{S₂}².

This is the 2D-compact extension of metric-mass's ω²/c² = k_S² + (n/R_u)² dispersion. The new structure is the *joint* contribution from m and n.

### The rest-mass formula

Set k_S = 0 (rest frame). The rest energy is

<!-- E_rest = ℏω = ℏc · √((2πm/L_u)² + (2πn/L_w)²) -->
$$
E_{\text{rest}} = \hbar\omega = \hbar c \,\sqrt{\left(\frac{2\pi\,m}{L_u}\right)^2 + \left(\frac{2\pi\,n}{L_w}\right)^2}
$$

and the corresponding rest mass m_(m,n) = E_rest / c²:

<!-- m_(m,n) = (ℏ/c) · √((2πm/L_u)² + (2πn/L_w)²) -->
$$
m_{(m,n)} = \frac{\hbar}{c}\,\sqrt{\left(\frac{2\pi\,m}{L_u}\right)^2 + \left(\frac{2\pi\,n}{L_w}\right)^2}
$$

The mass is parametrized by the integer pair (m, n) — a 2D discrete spectrum, where metric-mass had a 1D spectrum.

### Connection to the band-extremum picture

The closed-form rest-mass formula above is the spacetime-side rendering of a structurally deeper result. In [grid-duality §7.4.3](../grid-duality/07-wrap-promotion-modeling.md), mass arises from band curvature at extrema of the dispersion ω(**k**):

<!-- m_eff = ℏ² / (d²ω/dk²)|_{k_0} -->
$$
m_{\text{eff}} = \frac{\hbar^2}{(d^2\omega/dk^2)\big|_{k_0}}
$$

where k_0 is a point in the Brillouin zone with v_g = dω/dk = 0.

For our continuum dispersion, fix (m, n) and treat ω as a function of k_S alone:

<!-- ω(k_S) = c · √(k_S² + (2πm/L_u)² + (2πn/L_w)²) -->
$$
\omega(k_S) = c\,\sqrt{k_S^2 + \left(\frac{2\pi\,m}{L_u}\right)^2 + \left(\frac{2\pi\,n}{L_w}\right)^2}
$$

This has v_g = dω/dk_S = 0 at k_S = 0 — the rest frame is the band extremum for that (m, n) sector. Expanding to second order around k_S = 0:

<!-- ω(k_S) ≈ ω_0 + (c²/2ω_0) k_S² -->
$$
\omega(k_S) \approx \omega_0 + \frac{c^2}{2\omega_0}\,k_S^2
$$

with ω_0 = c · √((2πm/L_u)² + (2πn/L_w)²). Reading off m_eff = ℏ²/(d²ω/dk_S²) gives

<!-- m_eff = ℏω_0 / c² = ℏ/c · √((2πm/L_u)² + (2πn/L_w)²) -->
$$
m_{\text{eff}} = \frac{\hbar\omega_0}{c^2} = \frac{\hbar}{c}\sqrt{\left(\frac{2\pi\,m}{L_u}\right)^2 + \left(\frac{2\pi\,n}{L_w}\right)^2}
$$

— exactly m_(m,n). The two pictures agree: spacetime-closed-form (here) and lattice-band-extremum (grid-duality §7.4) yield the same rest mass for the bare-metric case treated in this chapter.

The grid-duality framing is the deeper one: rest mass is *the curvature of a band at a stationary point*. In our continuum setting this happens to admit a closed-form expression; in more general setups (curved metrics, modified dispersion) the band-extremum interpretation continues to apply when the closed form does not.

### Inertial behavior

The proof that m_(m,n) acts operationally as inertial mass — that p_S = m_(m,n) · v_g in the slow-motion limit, and that this matches Newton's second law — is identical in form to [metric-mass Chapter 2 §6](../metric-mass/02-mass-from-u.md), with one extra integer index. The argument depends only on the dispersion relation's structure near k_S = 0, not on the dimensionality of the compact part. We cite metric-mass and do not re-derive.

---

## 4. Three mode classes

The (m, n) mode family naturally partitions into three classes, each playing a distinct role in chapters 4–9.

| Class | (m, n) | Mass | Role |
|---|---|---|---|
| Light | (0, 0) | 0 | Massless propagation in (S₁, S₂); ordinary EM in spacetime |
| Single-axis | (m, 0) or (0, n) | m_(m,n) per §3 | L2-in-L3 candidates; mass without observable charge |
| Diagonal | both nonzero | m_(m,n) per §3 | L3 charged-state candidates; closure-eligible |

The three classes are distinguished not just by mass but by their **topological winding profile** — and that profile is what determines whether a given mode can satisfy the closure condition.

### 4.1 The (0, 0) zero mode — ordinary light

The (m, n) = (0, 0) mode has no winding in either compact direction. The dispersion reduces to

<!-- ω²/c² = k_S²  →  ω = c · k_S -->
$$
\frac{\omega^2}{c^2} = k_S^2 \quad \Longrightarrow \quad \omega = c\,k_S
$$

— the dispersion of a massless wave propagating at speed c through (S₁, S₂). The field configuration is independent of u and w; the wave does not "know about" the compact structure at all.

This is the analog of metric-mass's n = 0 zero mode and is structurally what we call **ordinary light** in spacetime. It does *not* satisfy the closure condition of [Chapter 1 §10](01-foundation.md): the closure condition requires nonzero windings, and (0, 0) has both equal to zero on all three views (topological: w_α = w_β = 0; phase-pattern: no winding to wrap; metric-side: no compact-direction momentum to source off-diagonals). Confirmed against [metric-mass Chapter 5](../metric-mass/05-metric-self-consistency.md): vacuum and pure-light configurations leave the bare metric self-consistent. The zero mode produces no mass and no charge.

### 4.2 Single-axis modes — (m, 0) and (0, n)

These modes wind in *one* compact direction only:

- **(m, 0):** winds m times around u, zero times around w. Carries mass m · 2πℏ/(L_u c). In topological terms, w_α = m, w_β = 0.
- **(0, n):** winds zero times around u, n times around w. Carries mass n · 2πℏ/(L_w c). In topological terms, w_α = 0, w_β = n.

These are the **L2-embedded-in-L3** modes. They have the topology of an L2 phenomenon (a single winding direction; per [grid-duality §7.4](../grid-duality/07-wrap-promotion-modeling.md), L2 supports mass via band curvature) but live on an L3 substrate (the 2-torus, with both directions geometrically available).

Per Chapter 1 §10's three-view formulation, single-axis modes **fail the closure condition under all three formulations**:

- *Topological:* one of (w_α, w_β) is zero. The U(1) × U(1) cross-coupling structure that supports α and observable EM (per [grid-duality §8.2](../grid-duality/08-where-alpha-appears.md)) requires both windings to be active simultaneously.
- *Phase-pattern:* one of u or w lacks a complete standing wave (because the wave doesn't wind through that direction at all).
- *Metric-side (chapter 5):* the off-diagonal metric entries sourced by these modes don't form a valid gauge-potential pattern.

Single-axis modes therefore produce **mass without observable charge**. They are candidate structural origins of *non-charged massive states* on a single sheet — a geometric, not pair-cancellation, mechanism for "massive but neutral." Standard physics has multiple non-charged massive categories (neutrinos, dark matter, certain neutral hadrons, the Higgs); which (if any) of these correspond to the framework's single-axis modes is open MaSt-correspondence work. Chapter 4 will interrogate the closure-failing modes further.

This distinction — between mass that arises from a single winding (L2-in-L3) and charge that requires both (full L3) — is a clean structural separation that grid-duality's wrap-promotion ladder makes available. The metric-charge framework imports the distinction directly.

### 4.3 Diagonal modes — (m, n) with both nonzero

These modes wind in *both* compact directions. They have both topological windings nonzero, so the U(1) × U(1) cross-coupling structure is active. Per Chapter 1 §10, this is the *necessary* condition for charge promotion under all three views.

It is not sufficient. The closure condition requires the winding to be accompanied by a complete standing-wave pattern on both u and w. Whether a given (m, n) actually satisfies that requirement depends on the standing-wave alignment — a phase-pattern question we defer to chapter 4. Our task in this chapter is only to identify which modes are *eligible* for charge under the necessary topological condition.

The diagonal modes are the eligible candidates. Chapter 4 will examine which (m, n) values survive the additional standing-wave alignment constraint — and what variants of the closure condition (Chapter 1 §10) might select different sub-families.

---

## 5. Energy, momentum, and the topological-winding identification

The four-momentum components of a generic (m, n) mode in motion follow directly from the dispersion relation. We define each component, then derive the energy-momentum relation and identify the compact-direction momenta with grid-duality's topological windings.

### 5.1 Components

The standard quantum-mechanical identification p = ℏk gives:

| Component | Value | Type |
|---|---|---|
| Energy | E = ℏω | continuous |
| Spatial momentum | p_S = ℏ k_S (in the (S₁, S₂) plane) | continuous |
| u-direction momentum | p_u = (2π ℏ/L_u) m | discrete, signed |
| w-direction momentum | p_w = (2π ℏ/L_w) n | discrete, signed |

The compact-direction momenta p_u and p_w carry the sign of (m, n). Per [Chapter 1 §6.1](01-foundation.md), this sign reflects the *traversal orientation* of the wave packet along the closed curve T(m, n) — a geometric label, not an internal field structure. The compact momenta are *internal* in the sense that they do not correspond to motion in observable (S₁, S₂, t) spacetime: the wave packet is going "around" the compact direction, not propagating along S.

These compact momenta are what shows up as off-diagonal sourcing in chapter 5's analysis. The identification of compact-direction momentum with electric-charge-like coupling comes from the geometric Kaluza-Klein mechanism: translations along a compact direction become a U(1) gauge symmetry of the effective theory under dimensional reduction, and the conserved Noether charge for that symmetry — which is just compact-direction momentum p_u or p_w — couples to the off-diagonal metric perturbation g_μu or g_μw (the KK gauge potential). [Chapter 5](05-metric-self-consistency.md) develops this explicitly. The mechanism is geometric (it lives in metric structure under dimensional reduction); standard-physics' identification of charge with KK compact-momentum is a translation target the framework's derivations may or may not match in detail.

### 5.2 The energy-momentum relation

Multiplying the dispersion relation through by ℏ²c² gives

<!-- E² = (p_S c)² + (p_u c)² + (p_w c)² -->
$$
E^2 = (p_S c)^2 + (p_u c)^2 + (p_w c)^2
$$

Equivalently, using the rest-mass formula of §3 to absorb the compact-direction momenta:

<!-- E² = (p_S c)² + (m_(m,n) c²)² -->
$$
E^2 = (p_S\,c)^2 + (m_{(m,n)}\,c^2)^2
$$

This is the standard relativistic E² = (pc)² + (mc²)² once we identify m_(m,n) as rest mass. The compact-direction structure is hidden inside m_(m,n) when viewed from extended spacetime alone — an observer in (t, S₁, S₂) cannot distinguish a (m, n) mode at rest from a textbook particle of mass m_(m,n).

### 5.3 Compact-direction momenta as topological windings

The compact-direction momenta have a deeper identity. From [grid-duality §7.5.2](../grid-duality/07-wrap-promotion-modeling.md), the conserved invariants on a 2-torus are line integrals of the wavevector around each cycle:

<!-- w_α = (1/2π) ∮_α k · dx,  w_β = (1/2π) ∮_β k · dx -->
$$
w_\alpha = \frac{1}{2\pi}\oint_\alpha \mathbf{k}\cdot d\mathbf{x}, \qquad w_\beta = \frac{1}{2\pi}\oint_\beta \mathbf{k}\cdot d\mathbf{x}
$$

For our Bloch modes the integrand is constant along each cycle (k is uniform in the planar separation we have used), and the integrals evaluate to (m, n) directly.

Translating between the two notations:

<!-- p_u = ℏ · k_u = ℏ · (2π/L_u) · w_α -->
$$
p_u = \hbar\,k_u = \hbar\cdot\frac{2\pi}{L_u}\cdot w_\alpha, \qquad p_w = \hbar\,k_w = \hbar\cdot\frac{2\pi}{L_w}\cdot w_\beta
$$

The compact-direction momenta in spacetime units (this chapter) and the topological winding numbers (grid-duality) are the same quantity, expressed two different ways.

This identification is the bridge between this chapter's spacetime-momentum view and chapter 5's metric-side picture. In chapter 5 we will see that p_u and p_w are the source terms that drive the off-diagonal metric entries g_μu and g_μw; under the Kaluza-Klein identification, those off-diagonals are the EM gauge potentials A_μ and B_μ. The chain reads:

> topological windings (grid-duality) ↔ compact-direction momenta (this chapter) ↔ off-diagonal metric sourcing (chapter 5) ↔ KK gauge potentials A_μ, B_μ

Each step is an identification, not a derivation. The math agrees on all four sides; we are just reading the same physical content through four different lenses.

**The chain is also a calculable mechanism for bending.** A passing wave traversing the perturbed metric near a bound mass picks up phase via the line integral ∮ A_μ dx^μ along its worldline. In the gravitational case (mass-sourced gauge potentials, no closure required), the holonomy manifests as gravitational lensing and Shapiro delay; in the electromagnetic case (closure-promoted charge with full A_μ, B_μ), the holonomy manifests as the EM refractive-index physics that slows light through matter. Both are quantitatively computable from this chapter's mode structure plus chapter 5's off-diagonal sourcing. See [metric-mass Chapter 6 §4](../metric-mass/06-gravitational-bending.md) for the gravitational version named explicitly as a mechanism candidate; chapter 5 of this project extends it to the EM case.

### 5.4 Conservation

The compact-direction momenta are conserved exactly under the wave equation on M with the bare metric — no source can change p_u or p_w during evolution because the wave equation does not couple modes with different (m, n). This is the wave-equation-side statement of the topological-winding conservation that grid-duality §7.5.2 derives from unitarity on the lattice.

The spacetime view and the topological view make the same statement: a mode's (m, n) is fixed at preparation and persists indefinitely under free evolution. Transitions between (m, n) sectors require a process that explicitly couples them, and no such process is available from the bare diagonal metric and free wave equation alone. Chapter 5's introduction of mass-sourced off-diagonals does *not* by itself open such a coupling — the off-diagonals are sourced by the mode but do not feed back to mix sectors at linear order.

---

## 6. What's next

[Chapter 3 — Knots on the torus](03-knots-on-the-torus.md). Take the (m, n) mode family derived here and reframe it geometrically as **closed curves traversing the (u, w) sheet**. The topological setup — that closed loops on T² fall into homotopy classes labeled by (m, n) ∈ ℤ² — is established in [grid-duality §7.5.1](../grid-duality/07-wrap-promotion-modeling.md). Chapter 3's distinctive job is the *geometric visualization* of these topological classes as actual torus knots, the mapping between (m, n) labels and standard torus-knot terminology, and any non-self-intersection or self-consistency constraints that pick out a sub-family of the full ℤ² label set.

The diagonal modes (m, n) of §4.3 will be the geometrically interesting cases in chapter 3: each gives a non-trivial torus knot. The single-axis modes (m, 0) and (0, n) of §4.2 reduce to trivial wrappings around one cycle — closed curves but not properly *knotted* in the topological sense. The (0, 0) zero mode is a point (no curve at all). This three-class partition will reappear at the topological level in chapter 3 just as it appeared at the dispersion-relation level here.

---

## What this chapter does **not** do (deliberately)

Six things are cited rather than re-derived:

- **Bloch decomposition on a 2D periodic substrate.** Cite [grid-duality §7.3](../grid-duality/07-wrap-promotion-modeling.md). We use the result; the derivation is there.
- **Band-extremum origin of mass.** Cite [grid-duality §7.4.3](../grid-duality/07-wrap-promotion-modeling.md). We confirm it agrees with our closed-form result (§3) but do not re-derive the general framework.
- **Integer-quantization of topological winding.** Cite [grid-duality §7.5.4](../grid-duality/07-wrap-promotion-modeling.md). The identification with our (m, n) is explicit (§2).
- **The slow-motion inertial-mass proof.** Cite [metric-mass Chapter 2 §6](../metric-mass/02-mass-from-u.md). It carries over with one extra integer index.
- **The metric-side picture of charge promotion.** Deferred to chapter 5. This chapter establishes only the mode family; chapter 5 does the off-diagonal sourcing analysis.
- **The classification of which (m, n) survive the closure condition.** Deferred to chapter 4. This chapter establishes only which modes are *eligible* (the diagonal modes of §4.3); chapter 4 examines whether they actually satisfy the standing-wave alignment requirement.

Six things are also *not* in scope at all, in this project:

- Quantum field theory of φ on M.
- Nonlinear self-interaction of φ.
- Multi-knot configurations on the same sheet (deferred to [metric-binding](../metric-binding/)).
- Vector polarization (the scalar abstraction is sufficient — see Chapter 1 §7).
- The numerical value of α (open work; structural location is settled in [grid-duality §8](../grid-duality/08-where-alpha-appears.md)).
- Direction-dependence of k_S in the (S₁, S₂) plane (this becomes important only when two knots sit at different (S₁, S₂) — i.e., in metric-binding).
