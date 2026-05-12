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
| 6 | The wave field φ — and the geometric meaning of signed (m, n) labels |
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

1. **Charge first appears at L3 of the wrap-promotion ladder.** Per [grid-duality §7.5](../grid-duality/07-wrap-promotion-modeling.md), the 2-torus closure T² = S¹ × S¹ has fundamental group π₁(T²) = ℤ² — supplying integer-valued conserved windings — and two independent U(1) isometries (one per compact direction), which under Kaluza-Klein dimensional reduction yield the **U(1) × U(1) gauge structure** that charge structurally requires. (The fundamental group is the topological invariant; the gauge group emerges from the metric's compact isometries under KK reduction. The two facts are parallel consequences of the 2-torus structure, not the same statement.) Below L3 there is at most one winding direction and one compact U(1) isometry; charge is undefined there. The 2D compact sheet of this project *is* the spacetime-embedded L3 substrate.

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

**Visualizing ε.** The 2-torus T² has a flat unrolled representation as a rectangle (the *fundamental domain*) in which opposite edges are identified — the left edge to the right edge, and the top edge to the bottom edge. Drawn this way, with **ring (u) as width** and **tube (w) as height**, the rectangle's shape directly displays the aspect ratio ε = width/height:

```
   ε ≪ 1 (thin sheet)       ε = 1 (Clifford torus)        ε ≫ 1 (fat sheet)
   ── small ring,           ── equal ring                 ── large ring,
      large tube               and tube                      small tube

         L_u                       L_u                              L_u
        ←──→                     ←────→                ←──────────────────→
        ┌──┐ ↑                   ┌────┐ ↑              ┌──────────────────┐ ↑
        │  │ │                   │    │ │              │                  │ │ L_w
        │  │ │                   │    │ │              └──────────────────┘ ↓
        │  │ │ L_w               │    │ │ L_w
        │  │ │                   │    │ │
        │  │ │                   └────┘ ↓
        │  │ ↓
        └──┘
```

Topology reminder: in each panel the left and right edges are the same circle (the ring, with u-coordinate identification u ~ u + L_u), and the top and bottom edges are the same circle (the tube, with w ~ w + L_w). A closed curve traversing T(m, n) — m wraps in ring, n wraps in tube — crosses the right edge m times (reappearing at the left) and the top edge n times (reappearing at the bottom). This unrolled flat view is the working diagram for chapters 2–9; it is distinct from the 3D-torus embedding of §5, which renders the same topology as a donut surface for spatial visualization purposes.

In the bare-metric form (§2), ε lives entirely in the periodicities (§9); it does not appear in the metric components themselves.

**Two homes for the same number.** ε has an equivalent alternate placement: under the rescaling u' = u/L_u, w' = w/L_w (both unit-period), the metric becomes g_u'u' = ε², g_w'w' = 1, and ε sits in the (u, u) diagonal entry instead of in the periodicity. The value is the same in both placements — the choice is whether ε lives in the boundary conditions (working convention) or in the metric matrix (metric-form display). The framework adopts the periodicity-form as its working convention to match MaSt's R-track, and uses the metric-form display only where showing all structural information inside the metric matrix is the cleaner object (relevant to the strategic stance of deriving each sheet's metric from species properties; see [metric-binding](../metric-binding/)). Either way, the symbol is bare ε; the home is identified by the surrounding equation, not by a subscript.

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

Geometric meaning: u and w are no longer orthogonal in the metric sense. σ_uw tilts the local (u, w) basis. The metric remains Lorentzian as long as |σ_uw| < 1 (otherwise the (u, w) sub-block becomes degenerate or signature-flipped). **|σ_uw| < 1 is a binding constraint** — a real positive-definiteness requirement, not a parametrization artifact.

**Equivalent form: lattice-shear s.** The same physical shear can be expressed in coordinates where the metric is flat (Euclidean) and the periodicity lattice is sheared instead. R-track studies (R60, R63, R64) work in this form and label the shear coefficient **s**. The two forms are related by

<!-- s = σ_uw / ε,  L_w^B = √(1 − σ_uw²) · L_w -->
$$
s \;=\; \frac{\sigma_{uw}}{\varepsilon},\qquad L_w^B \;=\; \sqrt{1 - \sigma_{uw}^2}\;L_w
$$

(the lattice-form's "tube length" L_w^B differs from this chapter's L_w by the √(1 − σ_uw²) factor). The two values are **different numbers** describing the same physical sheet — same intrinsic geometry, different labels. They diverge non-trivially at second order in shear: a value reported as σ_uw cannot be plugged into a formula written for s, and vice versa. The two are **not interchangeable**, only translatable via the transform above.

The framework adopts σ_uw (with bare σ as shorthand) as the working parametrization, because σ_uw is the metric off-diagonal entry directly — same object that produces all of the framework's other structural results, including the gauge-potential identification of [Chapter 5 §4](05-metric-self-consistency.md). The lattice-shear s appears where the framework references R-track studies' parameter values or where the lattice-form is the cleaner display.

The σ_uw < 1 bound and the studies' s being unbounded are consistent: s → ∞ at fixed L_u corresponds to L_w^B → 0 (the second lattice basis vector flattens onto the first) — the same degenerate-torus limit that σ_uw → 1 approaches in the metric form. Same geometric wall, different labels.

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

### 6.1 Closed curves on the 2D compact sheet are oriented

A closed curve traversing the (u, w) torus has two distinct traversal directions. The same point set in 3-space can be visited in either order — call the two orderings the **two orientations** of the curve. Every closed curve on a 2D manifold admits two orientations; this is a topological fact about closed curves, independent of any field built on top of the manifold.

When chapter 2 derives the integer-pair labels (m, n) for wave modes on the 2-torus from the periodicity boundary conditions of §9, those integers will range over all of ℤ — positive and negative. On a real-valued φ, the sign pattern (sign m, sign n) does not encode anything about an internal field structure; it encodes which of the two orientations the wave packet traverses along T(m, n):

- The wave's energy density (and therefore the rest mass derived from it in chapter 2 §3) depends only on the magnitudes (|m|, |n|).
- The sign pattern is independent information — it tracks which way the wave's phase advances during traversal of the closed curve, equivalently the sign of the compact-direction momenta p_u, p_w that chapter 2 §5 introduces.

Two consequences flow from this geometric reading:

- **(m, n) and (−m, −n) are distinct configurations on a real field.** They trace the same closed curve in 3-space and have the same energy density (so the same gravitational mass), but their compact-direction momenta have opposite signs. Chapter 5 will show that the sign of compact momentum determines the sign of the off-diagonal metric perturbation each mode sources. Whether this sign distinction has further physical content — whether (m, n) and (−m, −n) correspond to what standard physics calls a particle and its antiparticle, for example — is a question chapters 5, 6, and 8 examine, with the answer left to fall out of the analysis rather than imposed here.

- **No complex-field structure is required.** The (m, n) ↔ (−m, −n) distinction is supported by the manifold's intrinsic orientation of closed curves on a real-valued φ. It does not require an internal U(1) symmetry of a complex scalar field, a Noether current, or any other field-theoretic apparatus from quantum field theory. (Standard quantum field theory's complex-scalar bookkeeping is one possible *summary* of the same geometric content; the framework keeps the geometry as primary and treats field-theoretic summaries as downstream translation targets, not as inputs.)

The convention for the rest of the project: **(m, n) labels are signed integer pairs in ℤ², and the sign pattern is a geometric label tracking traversal orientation of the closed curve T(m, n) on the 2-torus.** No additional structure on φ is invoked for this distinction.

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

### The wrap-order convention

The bare topology presents the two compact directions u and w symmetrically: nothing in §§1–9 distinguishes them. To make the framework's downstream derivations definite, we adopt a convention naming one direction the *ring* and the other the *tube*:

> **u = ring** — the multi-wrap direction where mass arises from standing-wave structure (the metric-mass-style compact direction extended to 2D).
>
> **w = tube** — the single-wrap direction (in primitives) where charge arises from KK-style traveling-wave structure.

This convention is inherited from [grid-duality](../grid-duality/)'s wrap-promotion ladder, where L0→L1 (which produces the ring direction) and L1→L2 (which produces the tube direction) are *structurally distinct* substrate operations. The alternative convention (u as tube, w as ring) is isomorphic up to (u, w) ↔ (w, u) swap with ε → 1/ε; we adopt the convention above and proceed.

The closure condition stated below forces closure-satisfying primitives into T(m', 1) form (ring winding any integer m', tube winding ±1). The wrap-order convention names that structural asymmetry — its u/w role assignment tracks the closure condition's content rather than being arbitrary labeling.

### The closure condition (chirality form)

> **Closure condition.** A configuration T(m, n) is closure-satisfying — i.e., a (massive) mode also carries observable EM charge — if and only if:
>
> (i) the closed curve T(m, n) is **achiral** in 3-space — its chirality reflections are topological symmetries of the curve up to ambient isotopy — *and*
>
> (ii) the wrap-order's ring-direction reflection R_u (m ↔ −m) is among those topological symmetries.
>
> Within the torus-knot family realizable on T², (i) is the condition that the gcd-reduced primitive has tube winding ±1 (the curve is the unknot in 3-space, or a multi-link of unknots), and (ii) is automatic given (i).

This is **stated, not derived**. The deeper "why" — the α-coupling-strength derivation that explains the magnitude of the resulting charge — lives in [grid/](../../grid/), to be developed there. The chirality criterion above is what *selects* closure-satisfying configurations; the strength of the resulting coupling is a separate question.

The criterion is not fundamentally about "unknot status" — it is a chirality-symmetry condition that, applied to any T(m, n), produces a definite yes/no answer. For the torus knots that T² admits, the criterion happens to select unknots and their multi-links. The criterion itself is general (it would extend naturally to other manifolds where non-torus closed curves could be embedded — for example, an amphicheiral knot like the figure-eight would qualify on (i) grounds if it could be embedded).

### Equivalent operational test (synchronization)

The chirality criterion has a clean operational test in terms of phase synchronization during traversal:

> **Synchronization test.** Parametrize the traversal of T(m, n) by s ∈ [0, 1] with u(s) = m·s·L_u and w(s) = n·s·L_w. The tube phase crosses zero (modulo L_w) at s = j/n for j = 0, 1, ..., n. At each such s, the ring is at u(s) = (m·j/n)·L_u. For the ring to also cross zero (modulo L_u) at every such s, we need m·j/n to be an integer for every j ∈ {0, 1, ..., n}.
>
> **This holds if and only if n divides m (n | m), with both m and n nonzero.**

The synchronization test selects the same set of (m, n) as the chirality criterion: configurations for which the gcd-reduced primitive has tube winding 1 (T(m', 1) form). Within the torus-knot family on T², the chirality view (criterion (i)+(ii) above) and the synchronization view (operational test n | m) agree by construction.

### Topological characterization

> **Topological form.** T(m, n) closure-satisfies iff its gcd-reduced primitive is **T(m', 1)** for some integer m' ≥ 1. Equivalently: n | m with both nonzero. The closure-satisfying inventory is exactly **T(m', 1) primitives** and their **k-component repetitions** k × T(m', 1) (where k = n and m = k·m').

This is the same rule, viewed three ways:

- **Chirality view (the box above).** The closed curve is achiral and the wrap-order's R_u is among its topological symmetries.
- **Synchronization view.** The wave's tube-zero crossings coincide with ring-zero crossings during one closed traversal.
- **Topological view.** The closure-satisfying configurations are exactly the T(m', 1) primitives and their k-component repetitions.

Within the torus-knot family on T², the three views are mathematically equivalent — they all select the same partition of (m, n) ∈ ℤ² with both nonzero into closure-satisfying and closure-failing.

### Metric-side derivation — chapter 5

Chapter 5 develops a *metric-side* derivation: under the wrap-order-asymmetric standing-wave construction, closure-satisfying modes source one off-diagonal metric entry that forms a single Kaluza-Klein gauge potential pattern under linearized Einstein equations, while closure-failing modes source no EM gauge potential. The metric-side derivation is exactly equivalent to the chirality criterion (i)+(ii) — both are descriptions of the same underlying fact: the curve's chirality status, which controls which wrap-order-aligned symmetries the natural particle inherits.

The same off-diagonal-sourcing machinery is also the framework's calculable mechanism for how mass mechanically bends light (gravitational lensing, Shapiro delay) — see [metric-mass Chapter 6 §4](../metric-mass/06-gravitational-bending.md) and Chapter 5 below.

### Genuine torus knots: closure-failing

A genuine torus knot T(p, q) with both p, q ≥ 2 and gcd(p, q) = 1 is *chirally distinct* from its mirror in 3-space — T(p, q) and T(p, −q) (or T(−p, q)) are different knots, not isotopic to each other. Neither chirality reflection is a topological symmetry of the curve, so criterion (i) fails. **All genuine torus knots are closure-failing.** T(2, 3), T(2, 5), T(3, 4), T(3, 5), T(2, 7), ... are all closure-failing.

These modes source diagonal stress-energy (mass) and a chirality-encoded compact-compact cross-term that records which chirality of knot is present, but they source no EM gauge potential. Chapter 4 develops the resulting mass-only inventory; chapter 5 derives the metric-side picture.

### Why this convention? — open

The choice of which direction is the ring and which is the tube is a *convention* the framework adopts. Whether something physical eventually *forces* this choice — handedness or chirality of the embedding spacetime, substrate constraints from grid-primitive, or other — is a downstream question, not a determination of this chapter. If a structural mechanism eventually forces it, the convention becomes a derived result; if it remains adopted-by-stipulation, that is also defensible. [grid-duality §8](../grid-duality/08-where-alpha-appears.md) and alpha-derivation work may settle this.

This project takes the convention as adopted and explores its consequences.

### Variants to keep open

The closure condition stated above adopts a specific wrap-order. Several variants are conceivable and are examined in chapter 4:

- The opposite wrap-order (u as tube, w as ring) — gives an isomorphic framework with labels swapped per (u, w) ↔ (w, u).
- A configuration where one of the two windings is zero (single-axis modes) — closure-failing because there is no chirality structure to test.
- A configuration where multiple knots collectively satisfy closure but no single one does individually.

Whether these variants describe additional particle classes, redundant labelings of the same class, or unphysical configurations is a chapter-4 question.

---

## 11. Explicit non-assumptions

The following are *not* given. They are to be derived, observed to arise from the givens, or kept out of scope for this project.

- **Distinct sheet species.** No claim that electron, proton, or neutrino sheets exist as separate species. This project has *one sheet* and characterizes what kinds of particles it can host under varying (ε, σ_uw, knot quantum numbers, multi-phase populations). The multi-sheet structure of full MaSt is downstream.

- **Numerical α.** We do not commit to a numerical value of the fine-structure constant. Where α appears in interpretations or comparisons, it is taken as given; its derivation is [grid/](../../grid/)'s territory.

- **Closure-condition uniqueness.** No claim that the chirality-based closure condition of §10 is the unique rule under which a (massive) mode also carries observable EM charge. Alternatives (different wrap-orders, alternative particle-symmetry choices) are examined in chapter 4.

- **Vector polarization.** We do not track full vector polarization for the EM field. The scalar field φ carries phase but not polarization. See §7.

- **Lossless scalar abstraction.** No claim that the scalar abstraction loses *no* information beyond polarization. We leave room for surprises and will revisit if any later chapter encounters a result that depends on polarization in an unexpected way.

- **Quantum field theory.** The wave equation is classical. We invoke quantization-of-momentum at the periodicity boundary conditions (§9) but otherwise treat φ classically. ℏ enters only at the step of identifying p = ℏk for a wave of wavenumber k.

- **Complex-field structure for matter/antimatter labeling.** φ is real-valued (§6). The (m, n) ↔ (−m, −n) distinction the framework uses downstream (chapters 5, 6) is grounded in the geometric orientation of closed curves on T² (§6.1), not in an internal U(1) Noether structure of a complex scalar field. Standard quantum field theory's complex-scalar bookkeeping is a parallel summary of the same geometric content; whether that bookkeeping is the eventual most-natural description is left open, but the project's derivations operate on the real field with traversal orientation, not on a complex field with internal U(1).

- **Nonlinear backreaction.** We use linearized Einstein equations to compute mass-mode-sourced off-diagonals (chapter 5). Full nonlinear self-consistency of the field-and-metric system is deferred — the linearized regime is sufficient for everything this project sets out to establish.

- **Multi-sheet composition.** This project treats one compact sheet at a time. How two or more sheets share an extended-spacetime metric — whether they inhabit a common compact bundle or separate ones, whether their diagonal normalizations match across species, how their shears compose — is forwarded to [metric-binding](../metric-binding/).

- **Diagonal normalization choice.** The metric is written with g_uu = g_ww = 1 in the periodicity-form coordinates of §2. An equivalent parametrization moves ε into the (u, u) diagonal (g_uu = ε², g_ww = 1) and uses unit periodicities. The two are the same sheet — same ε in two homes (§3). The choice between them does not affect single-particle predictions and is left to downstream work to commit on for multi-species settings.

---

## 12. Summary of givens

We have, in total:

1. A manifold M with coordinates (t, S₁, S₂, u, w) — t, S₁, S₂ are extended (real-line); u and w are compact (circles of circumferences L_u and L_w respectively).
2. A starting metric ds² = −c²dt² + dS₁² + dS₂² + du² + dw², diagonal and constant. Subject to revision in chapter 5 (mass-induced off-diagonals) and chapter 8 (externally imposed shear σ_uw).
3. The aspect-ratio parameter ε ≡ L_u/L_w, free and symbolic; swept in chapter 7.
4. The shear parameter σ_uw (working symbol σ; equivalent lattice-shear label s = σ/ε used for R-track-study correspondence, see §4), equal to zero in chapters 2–7; turned on in chapter 8. The bound |σ_uw| < 1 is a binding positive-definiteness requirement.
5. A real scalar field φ : M → ℝ.
6. The massless wave equation □φ = 0.
7. Two periodicity boundary conditions: φ(u + L_u) = φ(u) and φ(w + L_w) = φ(w) (with all other arguments held fixed).
8. **The closure condition** of §10, as a chirality-symmetry criterion on the closed curve T(m, n), with equivalent operational (synchronization), topological (gcd-reduced primitive form), and metric-side (chapter 5) formulations.
9. **Inherited from [grid-duality](../grid-duality/) (chapters 7–8):** the L3 location of charge in the wrap-promotion ladder, the U(1) × U(1) gauge structure of the 2-torus closure, and the integer-quantization of winding numbers (w_α, w_β) ∈ ℤ². The integer-quantization is also derived independently in Chapter 2 §2 from the periodicity boundary conditions of §9; the two derivations agree, and we use grid-duality's result and our own as mutually consistent.

Methodological commitments:

- Units are kept SI-like: c and ℏ remain explicit symbols.
- φ is a scalar; full vector polarization is acknowledged but not tracked (§7).
- Off-diagonals of the metric start at zero and are introduced where the project requires them (mass-sourced in chapter 5; shear-imposed in chapter 8).

That is the entire content of this chapter. Everything else in the project must be derived from these eight items and the methodological commitments.

---

## What's next

[Chapter 2 — Modes on a sheet](02-modes-on-a-sheet.md). Solve the wave equation on M. Derive the mode family (m, n) labeled by winding pairs in (u, w), the dispersion relation, and the discrete mass spectrum. Confirm the (0, 0) zero mode behaves as ordinary light. Establish the (m, 0) and (0, n) "single-axis" modes as candidate closure-failure mass-only states for chapter 4 to interrogate.
