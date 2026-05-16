# Convex Integration and the Corrugation Process — A Ground-Up Introduction

A walkthrough of the mathematics behind the **Hévéa project**'s visualizations of corrugated flat tori, focused on the technical contribution of Mélanie Theillière's 2019 thesis *Intégration convexe effective*: the **Corrugation Process** formula.

**Audience.** Engineers and developers comfortable with basic calculus, linear algebra, and signal-processing intuition (frequency, amplitude, Fourier). No differential geometry assumed. Every Greek letter, every operator, and every piece of jargon is defined the first time it appears.

**Why this primer exists.** The Hévéa visualizations look striking, but the original papers are written for differential topologists. This primer translates the machinery for engineers: explicit recipes, signal-processing language, plain-English versions of every formal definition, and step-by-step intuition for what each formula is doing and why.

---

## Concepts introduced

| § | Concept |
|---|---------|
| 1 | The flat torus and what "isometric embedding" means |
| 2 | Why an ordinary donut fails — and Nash-Kuiper's surprising fix |
| 3 | Corrugations: how wiggles absorb extra length |
| 4 | The h-principle: turning wishful objects into real solutions |
| 5 | Gromov's convex integration formula |
| 6 | Theillière's local Corrugation Process formula |
| 7 | Choosing the corrugation shape (patterns and Kuiper relations) |
| 8 | Building a C¹ embedding layer by layer |
| 9 | The C¹-fractal limit |
| 10 | The Maslov phase and the Weierstrass fractal |
| 11 | Where else the technique applies |
| 12 | Practical takeaways |

---

## 1. The flat torus and isometric embedding

### A flat torus, in plain English

Picture a rectangular piece of paper. Now add two rules:

- Walk off the **right edge**, reappear on the **left edge**.
- Walk off the **top edge**, reappear on the **bottom edge**.

This rectangle-with-edge-identifications is called a **flat torus**. It has the same connectivity as the surface of a donut (start anywhere, loop around in either direction, come back to where you started), but it is geometrically a piece of *flat paper*. Distances measured on the rectangle stay valid: if two points are 3 cm apart on the rectangle, they are 3 cm apart on the flat torus. The word "flat" means it has the ordinary geometry of a sheet of paper — no curvature anywhere.

Mathematicians sometimes write this construction as `T² = ℝ²/(ℤe₁ + ℤe₂)`, which is shorthand for "the plane, with every point identified to all the points shifted by integer steps in two basis directions." But the picture is just **rectangle + edge-glue rules**.

### Isometric embedding, in plain English

Now we want to **draw** this flat torus in 3D space — to lay out an actual surface in space that has the same shape and the same distances.

The word **embedding** means a function that takes each point on the flat torus and assigns it a position in 3D space, producing an actual surface. The word **isometric** means *distance-preserving*: any curve drawn on the flat torus has the same length as its image on the 3D surface, measured along that surface.

A useful mental model: the flat torus is a piece of paper with glue rules. An isometric embedding is a way of folding that paper into 3D space, with the glue rules respected, **without stretching or compressing it anywhere**.

The question the Hévéa team addresses: **does such a distance-preserving 3D embedding exist, and can it be drawn explicitly?**

---

## 2. Why an ordinary donut isn't an isometric embedding

The first attempt: roll the paper into a tube (gluing top to bottom), then bend the tube into a ring (gluing the two open ends). The result is an ordinary donut shape.

A donut has the right connectivity. But it does **not** have the right distances.

### The length mismatch

Walk along the **outer equator** of a donut — the circle traced by the outermost points. Its length is 2π(R + r), where R is the distance from the donut's center to the tube's center, and r is the tube radius.

Walk along the **inner equator** — the circle traced by the innermost points. Its length is 2π(R − r).

These are different. But on the original flat rectangle, before we glued anything, the two horizontal lines that became these two equators **had the same length**. The donut has stretched the outer one and compressed the inner one. Distances are not preserved.

### What "curvature" means here

Underneath the length mismatch is a more fundamental obstruction: the donut is **curved**, while the flat torus is **flat**.

"Curved" here means the surface bends in space in a way that an ant walking on it can detect intrinsically — by drawing triangles and checking whether their angles sum to 180°, or by trying to keep walking in a "straight line" and seeing whether the path closes up. On the outside of a donut, triangle angles add up to more than 180° (positive curvature, like a ball). On the inside of the donut (the hole region), triangle angles add up to less than 180° (negative curvature, like a saddle). On the flat torus, triangle angles add up to exactly 180° everywhere — like on a normal flat sheet.

The mathematical name for this curvature measure is **Gaussian curvature**, written K. Flat surfaces have K = 0 everywhere. The donut has K positive on the outside, negative on the inside, zero only on the topmost and bottommost circles.

A donut and a flat torus, having different Gaussian curvature, **cannot be isometric**. Any genuine isometric embedding would have to bend somehow yet still be flat — which sounds like a contradiction.

### Nash-Kuiper: the unexpected escape

In 1954-55, John Nash and Nicolaas Kuiper proved a surprising result:

> Despite the curvature mismatch, an isometric embedding of the flat torus into 3D **does** exist — as long as the surface is allowed to be **C¹** but not **C²**.

What do C¹ and C² mean?

- **C¹** = the surface has well-defined **tangent planes** everywhere. At any point you can lay a flat sheet of paper that just barely touches the surface there, oriented uniquely.
- **C²** = the surface has well-defined tangent planes **and** well-defined curvature everywhere. You can not only orient a tangent plane, you can also measure how fast it tilts as you move along the surface.

A C¹ surface is smooth enough to be drawn, smooth enough to have well-defined directions at every point. But its second derivatives — the things that would tell you "how curved is it here?" — may misbehave. The surface might bend wildly at every scale without having a well-defined curvature at any single point.

The Nash-Kuiper theorem escapes the curvature contradiction by **going through this loophole**: the embedding can bend (so it closes up into a torus) without having well-defined curvature anywhere (so it doesn't violate flatness). The proof, however, was non-constructive — it showed the embedding exists without showing how to draw one.

The Hévéa project's achievement was to construct one explicitly, by adding wiggles.

---

## 3. Corrugations: how wiggles absorb extra length

### The corrugated-sheet analogy

A flat metal sheet of horizontal width W covers exactly W of horizontal extent. A **corrugated** metal sheet of the same horizontal width uses *more material* — the wiggles add length you couldn't see if the sheet were flat. Press a corrugated sheet flat and you'd find the metal is longer than W.

This is the core idea Nash-Kuiper exploits: corrugations on a donut can hold the extra length that the flat torus needs, even though the smooth donut couldn't.

### The math of a single wiggle

Imagine a sinusoidal curve y = A · sin(2π N x), where:

- A is the **amplitude** — how tall the wiggles are.
- N is the **frequency** — how many wiggles fit in one unit of x.

The total arc length of this curve over 0 ≤ x ≤ 1 is approximately

  arc length ≈ 1 + π² A² N²   (when A is small but A·N is large)

So short-amplitude high-frequency wiggles can absorb arbitrary amounts of extra length. A wiggle of amplitude 0.01 and frequency 100 has the same length-absorption as a wiggle of amplitude 1 and frequency 1, but is far less visible.

### Why a single layer isn't enough

A single layer of corrugations adds length in **one direction** (perpendicular to the corrugation ridges). The flat torus, however, has length deficits in multiple directions on the original rectangle. One layer cannot fix all directions at once.

Hévéa's solution: **multiple layers**. Each layer's corrugations point in different directions, and each successive layer is smaller (lower amplitude) but wigglier (higher frequency) than the previous. The hierarchy converges to a genuine isometric embedding in the infinite-layer limit.

The published Hévéa visualizations show four layers because the fifth would be too small to see. Mathematically, there are infinitely many.

---

## 4. The h-principle: from wishful objects to real solutions

Before the corrugation formula itself, we need one piece of mathematical machinery — the **h-principle**. The name is opaque, but the idea is simple.

### Wishful objects vs real solutions

Think of a geometric embedding as carrying three pieces of information at each point:

- **A** — Where you are on the flat torus (a point on the rectangle).
- **B** — Where the embedding sends you (a point in 3D space).
- **C** — The "stretch direction" at that point: a linear map that says, "if I move slightly in such-and-such direction on the rectangle, the embedded surface moves slightly in such-and-such direction in 3D."

For a genuine geometric embedding, **C is required to be the derivative of B as a function of A**. The three pieces are consistent with each other: B varies smoothly, and C records exactly how fast it varies.

Now imagine we are allowed to **lie** about C. We invent A, B, and C at each point, **without requiring C to actually be the derivative of B**. We just write down "at this point, here's where you are, here's where I'd put you in 3D, and here's what the derivative would be if I had one."

This is a **wishful object**: pointwise consistent (each point has its own A, B, C) but not globally consistent (C doesn't have to be the actual derivative of B).

Mathematicians call wishful objects **formal solutions** and real ones **holonomic solutions**. The word "holonomic" just means "C is genuinely the derivative of B."

### The h-principle

The **h-principle** is the question: if I have a wishful object that satisfies some property — say, "C is always an isometry" — can I deform it into a real, consistent solution that satisfies the same property?

For the flat-torus isometric embedding problem, the property is "C preserves lengths locally." A wishful object satisfies this if every point's made-up C is an isometry; a real solution satisfies it if its actual derivative is an isometry everywhere. The h-principle asks whether one can always be deformed into the other.

For C¹ isometric embeddings of the flat torus, **the answer is yes** — this is what Nash-Kuiper proves. The technique developed by Mikhail Gromov in the 1970s, called **convex integration**, gives a recipe for the deformation. Theillière's Corrugation Process improves the recipe.

---

## 5. Gromov's convex integration formula

The recipe: take a wishful object whose derivative is "too short" along some direction, then modify it by **adding high-frequency oscillations** that, on average, equal the missing piece.

### Setting up the problem

Suppose we have a current embedding f₀ taking points on the rectangle to points in 3D. Pick a direction on the rectangle — call it the x-direction. The current derivative of f₀ in this direction is some 3D vector that varies from point to point. We will write this as ∂₁f₀(x), meaning "the partial derivative of f₀ with respect to the first coordinate, evaluated at x."

We want to **replace** this derivative with a target vector γ̄(x) — what the wishful object says it should be. The gap between ∂₁f₀(x) and γ̄(x) is the "missing length" we need to absorb.

### The loop family

The trick is to introduce a **loop family**: a function γ(x, t) where, for each fixed x, the function t ↦ γ(x, t) is a closed loop in 3D (it comes back to its start as t completes one cycle). The loop is chosen so that its **average value equals the target**:

  (average of γ(x, t) over one period of t) = γ̄(x)

This is just like a Fourier-series construction: γ̄(x) is the DC component (the average), and the rest of γ wiggles around that average.

### The formula

Gromov's convex integration recipe defines a new map F₁ by integrating γ along the x-direction with a high oscillation frequency N:

<!-- F_1(x_1, x_2, ...) = f_0(0, x_2, ...) + ∫_0^{x_1} γ(s, x_2, ..., Ns) ds -->
$$
F_1(x_1, x_2, \ldots) \;=\; f_0(0, x_2, \ldots) \;+\; \int_0^{x_1} \gamma(s, x_2, \ldots,\; Ns)\, ds
$$

Reading this aloud: "start from f₀ at x₁ = 0, then accumulate contributions from γ, where the spatial position s sweeps from 0 to x₁ and at each s we sample γ at the oscillation phase Ns."

Because the loop's average equals the target, after a large number of oscillations (large N), the new map's derivative in the x-direction tracks the target γ̄.

In signal-processing language: we've **frequency-modulated** the embedding's derivative to follow a desired waveform.

### What this achieves, and its cost

For large N, the new map F₁ has three nice properties:

1. **F₁ is close to f₀ everywhere**: the difference shrinks as 1/N. At high frequency, the wiggles average out and the new map is uniformly near the old.
2. **Partial derivatives in directions other than x are nearly unchanged**: the oscillation acts only along x.
3. **The x-derivative tracks the target**: ∂₁F₁(x) is approximately γ̄(x), with a small superimposed oscillation.

So the wishful derivative is realized as the new map's actual derivative.

The **cost**: the formula contains an integral from 0 to x₁ along a spatial direction. The value of F₁ at one point depends on f₀ and γ along the **entire path** from 0 to that point. Two problems follow:

- **Implementation**: computing F₁(x) requires an integral, not a local formula.
- **Stitching artifacts**: when the construction is applied piece-by-piece to a complex surface (broken into multiple coordinate regions), the integration constants don't match across region boundaries, producing discontinuities that need a separate repair step.

Theillière's contribution fixes both of these costs.

---

## 6. Theillière's local Corrugation Process

The new idea: rewrite the formula so the integration is **only over the oscillation parameter**, with no path integral in space.

### The Corrugation Process formula

<!-- f_1(x) = f_0(x) + (1/N) ∫_0^{N x_1} [γ(x, s) − γ̄(x)] ds -->
$$
f_1(x) \;=\; f_0(x) \;+\; \frac{1}{N}\int_0^{N x_1} \bigl[\gamma(x, s) \;-\; \overline\gamma(x)\bigr]\, ds
$$

The structural difference from Gromov's formula: **x appears only as a parameter inside γ**. The integration variable s runs over the oscillation phase, not over space. The position x is fixed during the integration.

### Why this is "local"

Computing f₁(x) at a single point only requires:

- The value of f₀ at that same point x.
- The values of γ(x, s) for s = 0 to N·x₁.
- A 1D integral over s.

There is **no path integration in space**. Two neighboring spatial points don't need to know about each other's history; each computes its own integral independently.

The integral over s can also be **precomputed once** for each shape of loop and tabulated as a lookup, since γ's t-dependence is just whatever loop shape you chose.

### Practical consequences

- **Parallelizable**: each output point can be computed independently. Perfect for GPU shaders, distributed solvers, or any embarrassingly-parallel framework.
- **No stitching artifacts**: applying the formula on multiple regions of a complex surface produces no discontinuities at region boundaries.
- **Coordinate-system-independent**: a slightly more general form of the formula works on curved target spaces, replacing the addition "+" with an **exponential map** (a standard differential-geometry tool for moving along a manifold from a base point in a tangent direction).

The new map f₁ has the same three good properties as Gromov's F₁ (close to f₀, unchanged in transverse directions, target derivative along the chosen direction). But it's produced by a local formula instead of an integral over a spatial path.

This is the central technical contribution of Theillière's thesis.

---

## 7. Choosing the corrugation shape

The Corrugation Process needs a loop family γ(x, t) to be specified. Different choices produce different surfaces. To make the construction efficient and theoretically tractable, Theillière proposes that all loops in the family share a common **shape**, called a **pattern**.

### Patterns

A **pattern** is a template loop, written c(α, t), with two arguments:

- α is a **shape parameter** — a small set of numbers that adjust the template's amplitude or specific form at each point.
- t is the **oscillation phase** — a number in [0, 1) that indexes points along the loop.

Then a loop family is built as

  γ(x, t) = c₁(α(x), t) · e₁(x) + c₂(α(x), t) · e₂(x) + ...

where c₁, c₂, ... are the coordinate components of the template, α(x) tells the template how to be shaped at this point, and e₁(x), e₂(x), ... are a few local direction vectors. The intuition: every loop in the family is the **same template c**, just rotated and parameter-adjusted at each spatial location.

This is reminiscent of programming with a single shader function (the template) parameterized by per-pixel uniforms (α(x)) and orientation vectors (e_i(x)).

### The pattern for isometric embeddings

For the isometric embedding problem, Theillière proves that the right template is

<!-- c(α, t) = (cos(α cos 2πt) − J₀(α), sin(α cos 2πt), 1) -->
$$
c(\alpha, t) \;=\; \bigl(\cos(\alpha \cos 2\pi t) \;-\; J_0(\alpha),\;\; \sin(\alpha \cos 2\pi t),\;\; 1\bigr)
$$

A few notes:

- **J₀(α) is a Bessel function** — a standard special function that comes up in problems with cylindrical symmetry. For this primer, treat J₀ as a fixed numerical function whose values can be looked up in tables or computed by standard library calls. The point is just that it's a specific, computable function of α.
- The template is **smooth and sinusoidal** in t, with a Bessel-function offset.
- The −J₀(α) offset is essential: it ensures the average of the first coordinate over one period equals zero, which is the technical condition that keeps the lower-order properties of the construction intact.

### Kuiper relations

Some differential constraints are *easier* to solve with the Corrugation Process than others. Theillière names the class for which the formula simplifies most cleanly **Kuiper relations**. The formal condition involves convex hulls and surrounding loop families; the operational consequence is that for a Kuiper relation, the integral over s can be replaced by an explicit local sum, with no remaining integration. Specifically:

Define the running average of the template (with its mean removed):

  C_i(α, t) = ∫₀ᵗ [c_i(α, s) − c̄_i(α)] ds

where c̄_i(α) is the t-average of c_i(α, t). The functions C_i are **1-periodic in t**, so they can be tabulated once.

Then the Corrugation Process becomes an **explicit, local, integral-free formula**:

<!-- f_1(x) = f_0(x) + (1/N) Σ_i C_i(α(x), N · h(x)) · e_i(x) -->
$$
f_1(x) \;=\; f_0(x) \;+\; \frac{1}{N}\,\sum_i C_i\!\bigl(\alpha(x),\;\; N\cdot h(x)\bigr)\, e_i(x)
$$

Here h(x) is a smooth scalar function on the rectangle that specifies the corrugation direction (it's called a "submersion" in the thesis; think of it as a "phase coordinate" along which the corrugations oscillate). In simple cases, h(x) is just one of the rectangle's coordinates.

Reading the formula: at each point x, take the local pattern primitives C_i (looked up in a table), evaluate them at the shape parameter α(x) and the local phase N·h(x), scale them by 1/N, and add them along the local frame e_i(x). That's the new map's value at x.

This is a clean, fast, GPU-friendly local operation. No integrals at runtime.

---

## 8. Building a C¹ embedding layer by layer

One application of the Corrugation Process closes only part of the gap between a short embedding and a true isometric one. To close the rest, iterate.

### The iteration

Step 1. **Start with a short embedding f₀** — a smooth map whose distances are everywhere shorter than the target flat-torus distances. (The ordinary smooth donut is one such starting point.)

Step 2. **Measure the defect**: how much extra length is needed at each point and in each direction? The defect is a smooth tensor field on the rectangle that records the gap between current distances and target distances.

Step 3. **Choose a path of intermediate metrics**, gradually closing the gap. Call the fraction of the gap closed at step k a number δ_k between 0 and 1, with δ_k → 1 as k grows.

Step 4. **Decompose each step's gap-closure into simple direction-square pieces**. Each piece is "add length in this one direction."

Step 5. **Apply the Corrugation Process once per piece**, with a frequency N_k chosen large enough to absorb that direction's length.

Step 6. **Update** to the new f_k, repeat.

After many iterations, the maps f_k converge to a limit f_∞ whose distances exactly match the target. The limit is the C¹ isometric embedding promised by Nash-Kuiper.

### How fast do frequencies grow?

For the iteration to converge to a C¹ limit (rather than diverge), the corrugation frequencies must grow **fast enough**. The technical convergence condition is

  Σ_k √(δ_{k+1} − δ_k) < ∞

This says the steps δ_{k+1} − δ_k must shrink fast enough for their square roots to sum to a finite number. In plain terms: **each successive intermediate metric must close the remaining gap aggressively**.

In practice, frequencies grow **geometrically** — each layer's frequency is roughly 10 times (or more) the previous layer's. Correspondingly, each layer's amplitude shrinks geometrically. Each new layer is **much smaller and much wigglier** than the previous one.

This is exactly what the Hévéa visualizations show: the first layer's corrugations dominate visually, the second layer adds finer ripples, the third adds finer still, the fourth is at the edge of visibility, and the fifth is too small to see.

---

## 9. The C¹-fractal limit

Each layer of corrugation adds finer structure on top of the previous. In the infinite limit, the surface has structure at all scales: large bumps host smaller bumps, which host smaller bumps, all the way down.

This self-similar layering is what motivates the name **C¹-fractal**:

- **C¹** = tangent planes exist everywhere. At any point you can lay a small flat sheet that touches the surface at that point with a unique orientation.
- **Fractal** = the structure repeats at every scale. Zooming into any patch reveals new corrugations that weren't visible at coarser resolution.

The fractal is **deterministic**, not random — it is rigidly produced by the corrugation process given a particular starting short embedding and a particular sequence of frequency/amplitude choices. But it is genuinely infinite-detail.

### Why classical curvature can't survive

The classical **Gauss-Bonnet theorem** says: for a smooth, closed surface in 3D, the total Gaussian curvature integrated over the whole surface equals 2π × (Euler characteristic). For a torus, the Euler characteristic is 0, so the total curvature integrates to zero. A smooth donut achieves this with some positive curvature on the outside and some negative on the inside, balancing to zero overall.

But the flat torus has curvature **zero everywhere**. A C² (twice-differentiable) embedding would need to bend in 3D space, producing some non-zero curvature somewhere — contradicting "zero everywhere." So no C² isometric embedding exists.

The C¹ corrugated embedding sidesteps this by **having no curvature at all** in the classical sense. The second derivatives that would define curvature don't exist in the limit; they oscillate at higher and higher frequencies as the corrugation layers accumulate, and lose any well-defined value. The Gauss-Bonnet integral is not classically defined for a C¹ surface.

Nash-Kuiper's loophole is exactly the gap between **having tangent planes** (C¹) and **having curvature** (C²). The corrugation construction lives in this gap.

---

## 10. The Maslov phase and the Weierstrass fractal

The fractal nature of the limit can be made mathematically explicit through an object called the **Maslov phase**. This section requires a bit more setup than the others.

### The Gauss map (warm-up)

For a smooth surface in 3D, the **Gauss map** is the function that sends each point to the unit normal vector at that point — the direction perpendicular to the surface, pointing outward. The Gauss map gives a way of measuring the surface's orientation at every point.

### The generalization: a Maslov phase

In Theillière's more general setting (higher-dimensional manifolds embedded in target spaces with a complex structure), the analog of "the normal vector" is more complicated. But it turns out that one can always extract a single **phase angle** — a number in [0, 2π) — from the embedding at each point. This phase angle is called the **Maslov phase**, and the function from the surface to the unit circle is the **Maslov map**.

For a reader who hasn't seen Grassmannians or complex structures, the operational picture is enough:

- The Maslov map records **a single phase angle** at each point of the embedded surface.
- The phase rotates as you move across the surface.
- Theillière proves the rotation has an **explicit, computable form** for corrugated embeddings.

### The Weierstrass form

Theillière's central result on self-similarity is the following: for the limit embedding f_∞ built by iterated corrugation, the Maslov phase argument (the function from the rectangle to the real line that, when exponentiated as e^{iW}, gives the Maslov phase) is **asymptotically a sum of cosines** at exponentially growing frequencies:

<!-- W_∞(x) ≈ Σ_k α_k cos(2π N_k h_k(x)) -->
$$
\mathcal{W}_\infty(x) \;\approx\; \sum_{k=1}^\infty \alpha_k \cos\bigl(2\pi N_k\, h_k(x)\bigr)
$$

Here α_k → 0 as k grows (decreasing amplitudes), N_k → ∞ rapidly (increasing frequencies), and h_k are the corrugation-direction coordinate functions chosen at each iteration step.

This is precisely the form of the classical **Weierstrass function**:

<!-- W(x) = Σ a^n cos(b^n π x) -->
$$
W(x) \;=\; \sum_{n=0}^\infty a^n \cos\bigl(b^n \pi x\bigr), \qquad 0 < a < 1,\; b \text{ a positive odd integer},\; ab > 1 + \tfrac{3\pi}{2}
$$

The Weierstrass function is the classic textbook example of a "wild but continuous" function:

- **Continuous everywhere**: no jumps.
- **Differentiable nowhere**: the derivative doesn't exist at a single point.
- **Self-similar graph**: zooming into any portion of the graph reveals copies of the whole pattern at smaller scales.
- **Hausdorff dimension > 1**: the graph is "more than a curve" in a precise fractal sense.

### Why this matters

Before Theillière's result, the C¹-fractal nature of the corrugated torus was a **qualitative observation** — "this looks fractal." After her result, there is a **concrete scalar function** (the Maslov phase argument) with an **explicit Weierstrass decomposition**, computable directly from the corrugation parameters. Self-similarity stops being a vibe and starts being an explicit Fourier-like sum.

This gives a mathematical handle for any future analysis that wants to talk precisely about the fractal: it tells you what to compute.

---

## 11. Where else the technique applies

The Corrugation Process is not specific to flat tori. Theillière's thesis proves it applies to three categories of differential constraints:

1. **Immersions** — smooth maps whose derivative is everywhere injective (never collapsing dimensions). Useful for surfaces that may self-intersect but never degenerate.
2. **Approximate isometries (ε-isometric maps)** — maps whose pullback metric differs from a target by at most a small amount ε. A useful intermediate constraint on the way to exact isometric embeddings.
3. **Totally real maps** — a constraint in complex geometry requiring the embedded surface's tangent planes to avoid complex directions. This is a refinement of isometric embedding for complex-geometric target spaces.

### A new visualization: corrugated RP²

As a by-product, the thesis produces a new explicit immersion of the **real projective plane RP²** into 3D, obtained by applying the Corrugation Process to a starting surface called a Plücker conoid (a classical ruled surface in differential geometry). This is a one-shot application — no iteration needed.

### Connections to other constructions

The Corrugation Process recovers several existing constructions when the pattern is chosen specifically:

- **Thurston's corrugation theory** (1970s, used in Smale's sphere eversion): emerges as a special case.
- **Conti-De Lellis-Székelyhidi ansatz** (2012, used in regularity studies of C^{1,α} isometric immersions): another special case.

This positioning suggests the Corrugation Process is the natural unifying formula for explicit corrugation-based constructions in differential geometry.

---

## 12. Practical takeaways

### What the Corrugation Process provides

- **An explicit, local formula** for adding length-absorbing oscillations to a smooth map.
- **A hierarchical algorithm**: iterate at successively higher frequencies and smaller amplitudes to converge to a C¹ isometric embedding.
- **A principled corrugation shape** (the pattern), with a specific sinusoidal-with-Bessel-offset form for isometric embeddings.
- **A convergence guarantee** when frequencies grow fast enough.
- **An analytical handle on the fractal limit**: the Maslov phase is a Weierstrass-like sum.

### What it does not provide

- **Smoothness beyond C¹**. The limit has tangent planes but no curvature. Applications needing smoother geometry must look elsewhere.
- **Uniqueness or optimality**. Different choices (of starting short embedding, metric-defect decomposition, frequency sequence, pattern) give different limits. No single one is privileged.
- **Minimum-corrugation results**. The smooth construction uses infinitely many corrugations. Discrete or piecewise-linear versions need different techniques entirely.
- **Physical interpretation**. The corrugations are mathematical objects with no built-in connection to physics. Borrowing the architecture for physics applications requires separately motivating what plays each role.

### Implementation hints

- **Tabulate the pattern primitives** C_i(α, t) once. They're 1-periodic in t, smooth in α — a small 2D lookup table.
- **Each iteration is pure parallel compute**: every output value depends only on local inputs. Map naturally to GPU shaders or distributed solvers.
- **Frequency choice is the most sensitive parameter**. Too low fails to converge; too high causes numerical instability. Geometric progression by factors of ~10 per layer is the typical regime.
- **The "decompose the metric defect into squares of linear forms" step** is the algorithmic non-trivial part. For specific targets (flat torus, sphere) it's known explicitly; for arbitrary target metrics, a Cholesky-like decomposition does the job.

---

## References

Mélanie Theillière, *Intégration convexe effective* (PhD thesis, Université Lyon 1, 2019). The thesis this primer summarizes; especially Chapter 1 (h-principles and convex integration), Chapter 2 (the Corrugation Process and Kuiper relations), and Chapter 4 (Maslov-Weierstrass self-similarity).

V. Borrelli, S. Jabrane, F. Lazarus, B. Thibert, "Flat tori in three-dimensional space and convex integration," PNAS 2012 — the original Hévéa flat-torus construction.

The Hévéa Project website ([hevea-project.fr](https://hevea-project.fr)) — visualizations and accessible writeups, in French and English.

M. Gromov, *Partial Differential Relations* (Springer 1986) — the foundational reference on convex integration and h-principles.

J. Nash, "C¹ isometric imbeddings" (1954); N. Kuiper, "On C¹ isometric imbeddings" (1955) — the original existence proofs that Hévéa makes explicit.
