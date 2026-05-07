# Chapter 1 — Foundation

This chapter establishes the *manifold*, *metric*, *field*, *periodicities*, and *closure rule* on which the rest of the project rests. It is the only chapter where we **assume** things; every later chapter must derive its claims from what is stated here.

**Prerequisites:**

- [primers/metric.md](../../primers/metric.md) — the metric primer (covers metric machinery, signature, off-diagonals, light cones, the d'Alembertian, compact dimensions). We assume it as a reference.
- [metric-mass/01-foundation.md](../metric-mass/01-foundation.md) — the predecessor chapter. Where metric-mass already established something (mass-from-compactification, the inertial proof, off-diagonal sourcing from massive modes), we cite it rather than re-derive.

The chapter is paced deliberately slowly. Once a concept is defined here, it is used as-is throughout the rest of the project. If you are fluent with differential geometry or with metric-mass, parts will feel basic. That is intentional.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | Our coordinates: t, S₁, S₂, u, w and their domains |
| 2 | The bare metric on the 2D sheet |
| 3 | Aspect ratio ε ≡ L_u / L_w |
| 4 | Off-diagonal shear σ_uw |
| 5 | Visualization disposition (45° rendering) |
| 6 | The wave field φ |
| 7 | Why a scalar field is enough — and what we choose not to track |
| 8 | The wave equation on M |
| 9 | Periodicity in (u, w) |
| 10 | The closure condition (axiomatic) |
| 11 | Explicit non-assumptions |
| 12 | Summary of givens |

---

## 1. Our coordinates

We work with five coordinates: **t**, **S₁**, **S₂**, **u**, and **w**. Each one's domain (the set of values it can take) is given below.

| Coordinate | Symbol | Domain | What this means |
|---|---|---|---|
| Time | t | All real numbers | t can be any real value, no wraparound |
| First spatial extension | S₁ | All real numbers | S₁ can be any real value, no wraparound |
| Second spatial extension | S₂ | All real numbers | S₂ can be any real value, no wraparound |
| Compact, "u-direction" of the sheet | u | u ∈ [0, L_u), wraps | u runs from 0 up to L_u, then wraps back to 0 |
| Compact, "w-direction" of the sheet | w | w ∈ [0, L_w), wraps | w runs from 0 up to L_w, then wraps back to 0 |

The lengths L_u and L_w are the circumferences of the two compact directions. Both have units of length. We leave their numerical values symbolic for now.

**Manifold notation.** In differential-geometry shorthand, the combined domain is

<!-- M = ℝ × ℝ × ℝ × S¹ × S¹ -->
$$
M = \mathbb{R} \times \mathbb{R} \times \mathbb{R} \times S^1 \times S^1
$$

— ℝ for each of t, S₁, S₂, and S¹ ("the 1-sphere," math-speak for an ordinary circle) for each of u and w. The two compact factors form a **2-torus** T² = S¹ × S¹. We will call the manifold **M**, but the formal product notation is just shorthand for the table above.

(Heads-up on a notation clash, same one as metric-mass: **S₁** is our coordinate for the first spatial extension; **S¹** is the math symbol for "circle." The subscript 1 vs. superscript 1 is the only thing distinguishing them in print. They are different things.)

**Why two extended dimensions** (whereas metric-mass had one). Most single-knot derivations in this project don't strictly need S₂ — the closure condition, knot topology, mode spectrum, aspect-ratio sweep, and shear-induced fractional charge all work in S₁ alone. S₂ is carried in the coordinate set as forward-looking infrastructure for the follow-up project [metric-binding](../metric-binding/), where two knots at different (S₁, S₂) positions become essential. Keeping the coordinate set consistent across the two projects avoids a notational reset at the boundary.

**Why two compact dimensions** (whereas metric-mass had one). Four converging reasons:

1. **Charge first appears at L3 of the wrap-promotion ladder.** Per [grid-duality §7.5](../grid-duality/07-wrap-promotion-modeling.md), the 2-torus closure T² = S¹ × S¹ has fundamental group π₁(T²) = ℤ², providing the U(1) × U(1) gauge structure that charge structurally requires. Below L3 there is at most one winding direction; charge is undefined there. The 2D compact sheet of this project *is* the spacetime-embedded L3 substrate.

2. **Knot families.** A 1D compact direction admits only a single winding number — no knot topology. The 2-torus admits a discrete family of knots labeled by winding pairs (m, n) with non-trivial topological invariants (crossing number, genus, linking number). The geometric picture of charge as a closed curve traversing the sheet (chapter 3) requires the 2D substrate.

3. **The closure condition** (§10) requires winding in *both* u and w simultaneously. A single compact direction cannot host the rule.

4. **Polarization.** A real EM photon has E and B fields perpendicular to its propagation direction. A photon traveling along u with only u as a compact direction has nowhere internal for its polarization — it would have to point into S, which would put oscillating fields throughout observable spacetime. The 2D sheet gives polarization an internal home. We expand on this in §7.

These reasons converge: L3 is the structural reason, and (2)–(4) are particular manifestations of what the L3 substrate makes available.

**Note on visualization.** When we render M to a screen later, we embed the compact (u, w) sheet at a tilted disposition relative to (t, S₁, S₂); the details are in §5. The Cartesian display axes (x, y, z) carry no metric meaning — they are just where on the screen each coordinate goes.

---

## 2. The bare metric

The starting metric for this project is the simplest Lorentzian metric on M:

<!-- ds² = -c² dt² + dS₁² + dS₂² + du² + dw² -->
$$
ds^2 = -c^2\,dt^2 + dS_1^2 + dS_2^2 + du^2 + dw^2
$$

In matrix form, with coordinate ordering (t, S₁, S₂, u, w):

<!-- g = diag(-c², 1, 1, 1, 1) -->
$$
g_{\mu\nu} = \begin{pmatrix}
-c^2 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 1
\end{pmatrix}
$$

(For what a metric is and why we write it this way, see [metric.md §1–§4](../../primers/metric.md). The 5D extension is mechanical — every spacelike direction gets the same +1 entry.)

Reading the matrix:

- **g_tt = −c².** The diagonal entry for time. The negative sign is what distinguishes time from space (Lorentzian signature). The c² is the unit-conversion factor that makes ds² come out as length² when t is in seconds and the spatial coordinates are in meters.
- **g_S₁S₁ = g_S₂S₂ = 1.** Ordinary Euclidean weight for the two extended spatial directions.
- **g_uu = g_ww = 1.** Same Euclidean weight for the two compact directions. The only thing distinguishing u and w from S₁ and S₂ in the metric is the topology of the underlying coordinate (compact vs. extended), not the metric weight.

Three properties of this metric to keep in mind:

- **Lorentzian.** One negative eigenvalue (the time entry) → light cone exists at every point.
- **Flat.** g_μν does not depend on any of the coordinates → no curvature anywhere.
- **Diagonal — as a starting condition.** No cross terms between coordinates. As in metric-mass, we treat this as an *initial* form to be revisited. metric-mass Chapter 5 already established that off-diagonals develop in the presence of mass; this project takes that result as given and asks what additional structure the closure condition imposes (see §10 and chapter 5 of this project).

The diagonal-and-constant bare metric is the simplest possible setting in which to start the analysis. Whenever a later chapter requires off-diagonals — either the externally introduced shear σ_uw (§4, chapter 8) or the dynamically sourced cross terms from a mass mode (chapter 5) — that chapter will say so explicitly.

---

## 3. Aspect ratio ε ≡ L_u / L_w

The 2-torus has two independent compact lengths, L_u and L_w. We define the **aspect ratio**:

<!-- ε ≡ L_u / L_w -->
$$
\varepsilon \;\equiv\; \frac{L_u}{L_w}
$$

It is a free, dimensionless parameter of the sheet.

- **ε = 1** is the symmetric **Clifford torus**: equal compact lengths in u and w.
- **ε ≪ 1** is a "thin" sheet — small u-circumference, large w-circumference.
- **ε ≫ 1** is a "fat" sheet — large u-circumference, small w-circumference.

In the bare-metric form (§2), ε lives entirely in the periodicities (§9); it does not appear in the metric components themselves. (One could absorb ε into the metric coefficients by rescaling u or w; we do not, because keeping ε in the periodicities matches the convention used in MaSt's R-track.)

ε is left symbolic throughout this chapter and chapter 2. It will be **swept** as a parameter in chapter 7, where varying ε is the mechanism by which different knot families dominate, including the candidate single-phase, three-phase, and dark behaviors.

---

## 4. Off-diagonal shear σ_uw

In the bare metric (§2), all off-diagonals are zero. We introduce one optional off-diagonal entry: a coupling between u and w, denoted σ_uw (also written σ when context is unambiguous).

With shear, the metric becomes:

<!-- ds² = -c²dt² + dS₁² + dS₂² + du² + 2 σ du dw + dw² -->
$$
ds^2 = -c^2\,dt^2 + dS_1^2 + dS_2^2 + du^2 + 2\,\sigma_{uw}\,du\,dw + dw^2
$$

In matrix form, the change is in the (u, w) sub-block:

<!-- (u, w) sub-block becomes ((1, σ), (σ, 1)) -->
$$
g^{\text{(u,w)}}_{\mu\nu} = \begin{pmatrix} 1 & \sigma_{uw} \\ \sigma_{uw} & 1 \end{pmatrix}
$$

Geometric meaning: u and w are no longer orthogonal in the metric sense. σ_uw tilts the local (u, w) basis. The metric remains Lorentzian as long as |σ_uw| < 1 (otherwise the (u, w) sub-block becomes degenerate or signature-flipped).

For most of the project (chapters 2–7) we keep **σ_uw = 0**. Shear is turned on in chapter 8, where it becomes the parameter that biases matter over antimatter, aligns complementary nodes (proton-vs-neutron analog), and drives the quark-like fractional-charge mechanism.

This σ_uw is a **deliberate, externally imposed** off-diagonal — it is not the off-diagonal that mass dynamically sources via Einstein's equations. The latter is treated in chapter 5. Both kinds of off-diagonals coexist in the framework; they have different origins and play different roles.

---

## 5. Visualization disposition

When we render M to a screen, we use a fixed convention so that pictures across chapters refer to the same arrangement.

**Display axes.** The Cartesian rendering axes are (x, y, z), where:

- **x** displays S₁
- **y** displays S₂
- **z** displays t

These are display assignments only; they carry no metric meaning. (S₁ and S₂ are spacelike with metric weight 1; t is timelike with metric weight −c². The renderer ignores those distinctions and just plots them as Cartesian axes.)

**The compact sheet.** The (u, w) torus is rendered as a small 2-torus embedded in 3D space at each (x, y, z) point, with the compact dimensions exaggerated for visibility. The sheet is drawn at a **45° disposition** relative to the display axes:

- u's normal points toward (+y, +z) — i.e., into the upper-back region of the rendering frame.
- w's normal points toward (−y, +z) — i.e., into the upper-front region.

The two normals are 90° apart in the bare (σ_uw = 0) case and visibly distinct from any of the (x, y, z) display directions.

**Effect of shear.** When σ_uw ≠ 0, the rendered angle between u and w narrows from 90° (viewed from above, looking down the +z axis). This is the visual analog of the metric-side tilt described in §4.

**Knot trajectories.** A knot — a closed curve traversing the (u, w) sheet — appears in the visualization as a 3D spiral. When the knot also has a worldline through (S, t), the spiral threads through space and time. This will be the main visual object in chapter 3 (knots on the torus) and onward.

The visualization is intended for intuition, not derivation. None of the project's mathematical results depend on the rendering choice.

---

## 6. The wave field

We assume the existence of a single **real scalar field** on M, which we call φ.

The notation:

<!-- φ : M → ℝ -->
$$
\varphi : M \to \mathbb{R}
$$

— shorthand for "for each point (t, S₁, S₂, u, w) of M, there is a real number φ(t, S₁, S₂, u, w)." Same kind of object as the φ of metric-mass, just on a larger manifold.

The choice to use a *scalar* (rather than a vector or tensor field) deserves its own discussion, since it elides a real piece of physics and we want to be explicit about what we are choosing not to track. That discussion is §7.

---

## 7. Why a scalar field is enough — and what we choose not to track

This section is the seam between metric-mass and metric-charge on the polarization question. It is deliberately structural and short. The full vector-field story is parallel to our work, not part of it; the quantitative part of it lives downstream in [grid/](../../grid/).

### 7.1 The scalar abstraction is sufficient for our derivation chain

Everything chapters 2–9 will derive operates on the **phase pattern** of φ:

- Winding numbers (m, n) on the 2-torus
- Knot topology and its invariants
- The closure condition (§10) — a statement about how phase wraps and standing-waves
- Fractional charge from multi-phase wraps (chapter 8)
- Mass-only modes from closure failure (chapter 4)
- Off-diagonal sourcing of the metric by these modes (chapter 5)

None of these requires a polarization vector. A scalar field is the right level of abstraction for this project's derivation chain, and we use it throughout.

### 7.2 What metric-mass quietly elided

A real electromagnetic photon is a **vector potential** A_μ with E and B fields perpendicular to its propagation direction k. metric-mass's scalar abstraction collapsed this away — the mass-from-u derivation didn't need polarization, so it didn't include it.

If we naively promote metric-mass's setup to a real photon and ask where polarization would live, we run into a problem. A photon traveling along u has its polarization perpendicular to u. With only u as a compact direction, "perpendicular to u" inside the manifold means **only S or t** — observable spacetime. A bound photon on u, taken seriously as a vector field, would put an oscillating E into S at every massive object's Compton frequency. We do not observe this.

So the scalar abstraction in metric-mass is not just a pedagogical simplification — it is a way of avoiding a structural deficiency: **one compact dimension is too few to host the photon's polarization internally.**

### 7.3 What the 2D sheet buys for polarization

With both u and w compact, a photon traveling along u has w as a perpendicular direction *within the sheet*. E along w is internal to the compact structure — a polarization component that does not leak into observable spacetime.

This is the minimum compact geometry on which one of the photon's polarization components has an internal home, independent of the (already sufficient) topological reasons for the 2D-sheet jump.

### 7.4 What still leaks

Even on the 2D sheet, the *full* polarization story does not close. B = k × E. With k along u and E along w, B is perpendicular to both — out of the sheet plane. Within the manifold M, "out of the (u, w) plane" means into S or t.

So at most *one* of {E, B} fits inside the sheet at any moment, depending on the polarization choice. The other one wants to live outside.

This residual leakage is plausibly the structural opening through which bound photons couple to S — the mechanism by which compact-sheet modes become observable as electromagnetic phenomena in 4D spacetime. It is a candidate quantity for what α measures in geometric terms (cf. [Q137](../../qa/Q137-alpha-as-aleph-aspect-ratio.md), the alpha-derivation work in [grid/](../../grid/)). The quantitative answer is grid's job, not this project's.

### 7.5 What this chapter commits to

We use a scalar φ throughout. Wherever later chapters say "the wave winds 2π on w," "the wave forms a knot," or "the closure condition is satisfied," we mean *the phase pattern of φ*. The polarization-leakage question is parallel to our work, deferred to grid, and flagged as an open structural question — not a derivation step.

If a later chapter forces the issue (say, a closure-condition prediction that depends quantitatively on polarization structure), we will revisit. So far we do not expect that.

---

## 8. The wave equation

φ obeys the **massless wave equation**:

<!-- □φ = 0 -->
$$
\Box\varphi = 0
$$

This says, in the language of the metric primer ([metric.md §11](../../primers/metric.md)), that φ is a light-like field — its disturbances propagate on light-like paths (ds² = 0).

Plugging the bare metric (§2) into the general form g^μν ∂_μ ∂_ν φ = 0 gives the explicit wave equation we will work with in chapter 2:

<!-- (-1/c²)∂²φ/∂t² + ∂²φ/∂S₁² + ∂²φ/∂S₂² + ∂²φ/∂u² + ∂²φ/∂w² = 0 -->
$$
-\frac{1}{c^2}\frac{\partial^2\varphi}{\partial t^2}
+\frac{\partial^2\varphi}{\partial S_1^2}
+\frac{\partial^2\varphi}{\partial S_2^2}
+\frac{\partial^2\varphi}{\partial u^2}
+\frac{\partial^2\varphi}{\partial w^2}
= 0
$$

The structure is a routine extension of metric-mass's wave equation: each Cartesian-orthogonal coordinate contributes a second derivative with sign matching its metric signature. The substantive new piece, coming in chapter 2, is the **Laplacian on the (u, w) torus** — the last two terms together. That Laplacian is what the periodicity boundary conditions of §9 act on, and its eigenvalue structure is what produces the discrete (m, n) mode family.

When σ_uw ≠ 0 (chapter 8), the wave equation acquires a cross-term from the off-diagonal inverse metric. We defer that case until needed.

---

## 9. Periodicity in (u, w)

Because both u and w are compact, the field φ must be **single-valued** on each compact direction. Going around by L_u (and coming back to "where you started") must give the same field value; same for L_w.

Two boundary conditions, both required:

<!-- φ(t, S₁, S₂, u + L_u, w) = φ(t, S₁, S₂, u, w) -->
$$
\varphi(t, S_1, S_2, u + L_u, w) = \varphi(t, S_1, S_2, u, w)
$$

<!-- φ(t, S₁, S₂, u, w + L_w) = φ(t, S₁, S₂, u, w) -->
$$
\varphi(t, S_1, S_2, u, w + L_w) = \varphi(t, S_1, S_2, u, w)
$$

These are not separate equations but **boundary conditions** on the wave equation of §8. They restrict which solutions are allowed: a candidate solution that increased or decreased after one trip around either compact direction would be multi-valued and is therefore disqualified.

These two periodicities together produce the **discrete 2D mode family** (m, n) that chapter 2 will derive — the analog of metric-mass's 1D winding spectrum, now indexed by a pair of integers rather than one.

**Note for chapter 8 (when σ_uw ≠ 0).** With shear, the natural periodicity lattice on (u, w) is no longer rectangular — it is sheared to match the metric. The boundary conditions must be applied along the sheared lattice vectors, not along independent u and w. We flag this here and defer the full treatment to chapter 8.

---

## 10. The closure condition (axiomatic)

This is the centerpiece of the project. We state it now and explore its consequences in chapters 4 and 5.

> **Closure condition.** A wave configuration on the 2D sheet promotes its mass mode to a charge mode when, during a single closed traversal of its phase pattern, **both** of the following are satisfied:
>
> 1. The phase completes a full **2π winding on w**.
> 2. The phase completes a **complete standing wave** (full period — node-to-antinode-to-node) on **both u and w**.
>
> Mini-step traversals are allowed; what matters is that the closure pattern locks during one full traversal of the knot.

This is **stated, not derived**. The "why" — the α-coupling-strength derivation that explains the *strength* of the resulting charge — lives in [grid/](../../grid/), to be developed there. This project takes the rule as given and explores its consequences.

### Three views, one rule

The phase-pattern statement above is one of three equivalent formulations of the same condition.

**Topological view** (lattice-substrate side). Per [grid-duality §7.5](../grid-duality/07-wrap-promotion-modeling.md) and [§8](../grid-duality/08-where-alpha-appears.md), the L3 2-torus has fundamental group π₁(T²) = ℤ², giving each closed wave configuration two independent integer winding numbers (w_α, w_β). The U(1) × U(1) cross-coupling structure that supports α and observable EM requires both winding directions to be active simultaneously. Closure-failed configurations have at most one active winding direction and reduce to L2 (mass without charge) embedded in an L3 substrate. The closure condition is the rule that **both** winding numbers are nonzero.

**Metric-side view** (spacetime-embedding side; developed in chapter 5). metric-mass Chapter 5 established that under linearized Einstein equations, a mass mode in a compact direction sources off-diagonal metric entries (g_tu in metric-mass's case). On the 2D sheet, the analogous calculation produces a richer set: in principle, all of g_tu, g_S₁u, g_S₂u, g_tw, g_S₁w, g_S₂w can be sourced. In the standard Kaluza-Klein identification, these off-diagonals are physical electromagnetic gauge potentials A_μ and B_μ, one per compact direction. The closure condition, in this formulation, is the rule under which the sourced off-diagonals actually form a valid gauge-potential pattern — consistent with the gauge structure that makes them observable as EM in 4D. The same off-diagonal-sourcing chain is also the framework's calculable mechanism for how mass mechanically bends light (gravitational lensing, Shapiro delay) — see [metric-mass Chapter 6 §4](../metric-mass/06-gravitational-bending.md) for the elevation from cross-check to mechanism claim.

**Phase-pattern view** (the box above). The wave's phase completes a full 2π winding on w *and* a complete standing wave on both u and w during a single closed traversal.

The three formulations agree where they overlap. The topological ↔ phase-pattern equivalence is essentially the assertion that integer winding numbers manifest as 2π phase wraps. **Chapter 5 develops the metric-side view and shows its equivalence to the other two.** Chapter 1 only states all three. Closure failure under any one formulation corresponds to mass-only modes in all three: a candidate structural origin of neutrino-class neutrality, distinct from any pair-cancellation mechanism.

### Variants to keep open

The closure condition stated above is one specific rule. Several variants are conceivable and will be examined in chapter 4:

- 2π winding on **u** instead of w — does this give a different particle class?
- A standing wave on only one of u or w (rather than both)
- A configuration where multiple knots collectively satisfy closure but no single one does individually

Whether these variants describe additional particle classes, redundant labelings of the same class, or unphysical configurations is a chapter-4 question.

---

## 11. Explicit non-assumptions

The following are *not* given. They are to be derived, observed to arise from the givens, or kept out of scope for this project.

- **Distinct sheet species.** No claim that electron, proton, or neutrino sheets exist as separate species. This project has *one sheet* and characterizes what kinds of particles it can host under varying (ε, σ_uw, knot quantum numbers, multi-phase populations). The multi-sheet structure of full MaSt is downstream.

- **Numerical α.** We do not commit to a numerical value of the fine-structure constant. Where α appears in interpretations or comparisons, it is taken as given; its derivation is [grid/](../../grid/)'s territory.

- **Closure-condition uniqueness.** No claim that the closure condition of §10 is the unique rule that promotes mass to charge. Alternatives are examined in chapter 4.

- **Vector polarization.** We do not track full vector polarization for the EM field. The scalar field φ carries phase but not polarization. See §7.

- **Lossless scalar abstraction.** No claim that the scalar abstraction loses *no* information beyond polarization. We leave room for surprises and will revisit if any later chapter encounters a result that depends on polarization in an unexpected way.

- **Quantum field theory.** The wave equation is classical. We invoke quantization-of-momentum at the periodicity boundary conditions (§9) but otherwise treat φ classically. ℏ enters only at the step of identifying p = ℏk for a wave of wavenumber k.

- **Nonlinear backreaction.** We use linearized Einstein equations to compute mass-mode-sourced off-diagonals (chapter 5). Full nonlinear self-consistency of the field-and-metric system is deferred — the linearized regime is sufficient for everything this project sets out to establish.

---

## 12. Summary of givens

We have, in total:

1. A manifold M with coordinates (t, S₁, S₂, u, w) — t, S₁, S₂ are extended (real-line); u and w are compact (circles of circumferences L_u and L_w respectively).
2. A starting metric ds² = −c²dt² + dS₁² + dS₂² + du² + dw², diagonal and constant. Subject to revision in chapter 5 (mass-induced off-diagonals) and chapter 8 (externally imposed shear σ_uw).
3. The aspect-ratio parameter ε ≡ L_u/L_w, free and symbolic; swept in chapter 7.
4. The shear parameter σ_uw, equal to zero in chapters 2–7; turned on in chapter 8.
5. A real scalar field φ : M → ℝ.
6. The massless wave equation □φ = 0.
7. Two periodicity boundary conditions: φ(u + L_u) = φ(u) and φ(w + L_w) = φ(w) (with all other arguments held fixed).
8. **The closure condition** of §10, as a statement about phase patterns, with equivalent topological (inherited from grid-duality) and metric-side (developed in chapter 5) formulations.
9. **Inherited from [grid-duality](../grid-duality/) (chapters 7–8):** the L3 location of charge in the wrap-promotion ladder, the U(1) × U(1) gauge structure of the 2-torus closure, and the integer-quantization of winding numbers (w_α, w_β) ∈ ℤ². Used throughout but not re-derived.

Methodological commitments:

- Units are kept SI-like: c and ℏ remain explicit symbols.
- φ is a scalar; full vector polarization is acknowledged but not tracked (§7).
- Off-diagonals of the metric start at zero and are introduced where the project requires them (mass-sourced in chapter 5; shear-imposed in chapter 8).

That is the entire content of this chapter. Everything else in the project must be derived from these eight items and the methodological commitments.

---

## What's next

[Chapter 2 — Modes on a sheet](02-modes-on-a-sheet.md). Solve the wave equation on M. Derive the mode family (m, n) labeled by winding pairs in (u, w), the dispersion relation, and the discrete mass spectrum. Confirm the (0, 0) zero mode behaves as ordinary light. Establish the (m, 0) and (0, n) "single-axis" modes as candidate closure-failure mass-only states for chapter 4 to interrogate.
