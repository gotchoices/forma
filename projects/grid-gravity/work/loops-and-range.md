# Loops and range: why the mass's effect spreads as 1/r

**Status:** Result note. Vets mechanism 2's make-or-break — the range /
falloff of the refractive well ([detour-refractive.md](detour-refractive.md)
§4) — via the loop-unification idea. Outcome: the range **resolves** for a
scalar source, and the open question refocuses onto source *character*.
Reproduce: `../scripts/hex_greens.py`.
Figure: [`../outputs/hex_greens.png`](../outputs/hex_greens.png).

---

## 1. The insight: the compact loop and the spatial hex loops are one kind of thing

A standing wave's self-consistency lives on the **compact-dimension loop**
(an S¹ cycle). Hexagonal loops in the spatial lattice — at every scale — are
**also closed 1-cycles**, each carrying a phase-closure constraint. There is
no difference *in kind*: both are closed loops with a single-valuedness
condition; they differ only in which cycle and at what scale.

The consequence: "the standing wave's constraint carried outward through the
shared loops at all scales" **is** the way a localized perturbation
propagates under the lattice operator — i.e. it is the lattice's own
**Green's function**. And the lattice operator is **confirmed massless**
(linear dispersion ω = ck; [grid/sim-maxwell](../../grid/sim-maxwell/),
[grid-duality §3](../grid-duality/07-wrap-promotion-modeling.md)). A massless
operator has **no length scale**, so its static response to a localized
source is a **scale-free power law** — 1/r (3D) / log r (2D) — not a Yukawa.

So the RG-fixed-point / scale-freeness worry ([foundations Q1](../../grid/foundations.md))
is answered *by the confirmed masslessness*: no preferred loop size ⇒ power
law. The make-or-break turns from "hope it is scale-free" into "it is
scale-free because the operator is massless, which is established."

## 2. The fork: scalar → gravity, winding → charge

A loop can carry two different "charges", and they give different forces:

- a **topological winding** (holonomy) around the loop sources a spatial
  field like a vortex → **charge** (the wrap-promotion L3 Coulomb field;
  signed, α);
- a **scalar** constraint (the standing wave's energy / occupancy at n₀)
  sources a spatial scalar field → **gravity** (unsigned, universal).

Both fall off as the same massless 1/r — but gravity must be seeded by the
**scalar energy**, not the winding, or the loop-generalization quietly
yields charge instead. So the range is common; the *source character* is what
separates the two forces.

## 3. The test (actual lattice operator, no free parameters)

The static response of the massless operator is the graph-Laplacian Green's
function. Built the triangular ("hex") lattice Laplacian L, solved L u = s
for a localized **scalar** source s (a point, and rings/"loops" of radius 6
and 20 — mimicking seed loops of different size), Dirichlet boundary,
radius-140 lattice (64k nodes). Measured falloff, scale-freeness, isotropy,
and loop-size dependence.

| Seed loop r | log-fit R² | scale-free (inner vs outer slope) | 6-fold anisotropy |
|---|---|---|---|
| 0 (point) | 1.00000 | 0.12% | 0.26% |
| 6 | 1.00000 | 0.10% | 0.26% |
| 20 | 1.00000 | 0.02% | 0.32% |

- **Scale-free power law.** Perfect log r (R² = 1.00000), slope constant
  across radial sub-decades (≤ 0.12%) — a genuine power law, **not Yukawa**.
- **Isotropic** — 0.26% residual 6-fold anisotropy.
- **Loop-size-independent** — far-field slopes −0.0920 / −0.0919 / −0.0919,
  **0.06% spread**. A point, a small loop, and a large loop seed the
  *identical* far-field.

## 4. What this establishes

- **The range make-or-break resolves — for a scalar source.** A localized
  scalar constraint, propagated by the *actual* lattice operator, spreads as
  a scale-free, isotropic 1/r-family field. The genuinely-tested parts
  (scale-freeness, isotropy, loop-size independence) all pass on the real
  operator; the log r itself follows from the operator's masslessness.
- **The loop-unification is validated.** The seed loop's scale is
  irrelevant to the far-field — the compact loop and the spatial hexagon
  loops (any size) are equivalent as sources. Your generalization holds:
  the mass's influence spreads as 1/r *because* it rides the lattice's own
  massless Green's function, seeded by any localized loop-constraint.

## 5. Honest limits — the residual open question

- **The scalar source was assumed.** The test *put in* a scalar and got
  gravity-like 1/r. It does **not** settle whether the detour effect
  actually presents a **scalar-energy** source (→ gravity) rather than a
  **winding** (→ charge) or a **mass-term-generating nonlinearity**
  (→ Yukawa). That is now the single remaining question for the range leg,
  and it is much sharper than "what is the falloff."
- **2D / graph-Laplacian.** The run is 2D (log r = the massless signature;
  1/r in 3D by the same masslessness). It uses the operator's static limit
  (the graph Laplacian), which is what the confirmed massless scatter
  reduces to.
- **Coefficient still open** (Objective 3): magnitude → G = 1/(4ζ) / the PV
  form n(r) = 1 + 2GM/rc².

## 6. Where mechanism 2 now stands

The range leg — the make-or-break flagged in
[detour-refractive.md](detour-refractive.md) §4 — is **resolved for a scalar
source**: scale-free, isotropic, 1/r, loop-size-independent, from the actual
operator. Combined with the earlier legs (vacuum field met; non-dispersivity
derived; losslessness structural), mechanism 2 clears the *shape* of the gate
on all fronts **conditional on one physical question**:

> Does the detour effect present the mass's **energy** to the lattice as a
> **scalar** source (→ gravity), rather than a winding (→ charge) or a
> mass-generating nonlinearity (→ Yukawa)?

That question — source character — plus the coefficient, are what remain.
Both are sharp, and both are the honest next targets before any chapter arc.
