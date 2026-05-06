# Chapter 5 — 2D Lattice Assembly

Chapters 1–3 established the cylinder primitive on a single edge: its energy (with matched-chirality matrices *M* and *D*), its wave dynamics (single propagation speed *c* under matched chirality + bare-speed equality), and the constraints that the lattice signal speed places on its parameters. Chapter 4 already used a 2D lattice's static and thermal behavior to derive 1/r force scaling, but it did so without formally constructing the lattice from the single-primitive equations.

This chapter does the formal construction. We pick a specific 2D lattice geometry — the **hexagonal** (honeycomb) lattice with **wye junctions** at each node — assemble many cylinder primitives into it, derive the wave equation, and check the band structure for any surprises.

The chapter is much simpler than its earlier draft. The "slow-mode tension" that an earlier draft had to address was a consequence of using a diagonal inertia matrix *D*; chapter 1 §8's matched-chirality commitment removed the tension at the foundation level. Both polarizations propagate at *c*. The lattice analysis here is just a routine assembly with no surprises.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The hexagonal lattice — wye junctions and hexagonal faces |
| 2 | The wave equation on the 2D lattice |
| 3 | The long-wavelength continuum: single propagation speed *c* |
| 4 | Brillouin-zone modes and the photon at the lattice scale |
| 5 | Summary of givens |

---

## 1. The hexagonal lattice — wye junctions and hexagonal faces

The 2D periodic lattice we work with is the **hexagonal (honeycomb) lattice** — the geometry familiar from graphene, carbon nanotubes, and benzene rings. The relevant features:

- **Vertices** (nodes) are points where three edges meet at 120° — a *wye junction*. Each node has exactly 3 incident edges.
- **Faces** are hexagons.
- **Edges** are the line segments between adjacent nodes; each edge is one cylinder primitive.

The two "sublattices" of the honeycomb (the A-sublattice and the B-sublattice, where each A-node connects to three B-nodes and vice versa) form a 2-site unit cell. Each unit cell has 1 A-node, 1 B-node, and 3 edges — and each edge has 2 cylinder DoF (*e*, *φ*) — giving 6 DoF per unit cell.

### Continuity at a wye junction

Chapter 1 §5 stated that nodes impose continuity of the stress vector at endpoints of meeting cylinders. At a wye junction, three cylinders meet at 120°, so the continuity rule needs a moment of attention.

The cylinder's azimuthal direction *φ* is defined relative to a *local cross-section frame* — a choice of "where φ = 0 points" specific to that cylinder's geometry. Three cylinders meeting at 120° each carry their own local frame, and those frames are not the same. The polar coordinates (*e*, *φ*) of cylinder A's stress vector at the junction therefore do *not* equal the (*e*, *φ*) of cylinder B's stress vector at the same junction in numerical value, even when the two stress vectors agree as physical objects.

So the continuity rule is on the **underlying stress vector ψ** — the 2D real vector in the cross-sectional plane, expressed in some shared lab frame:

> At each node, the three incident cylinders' endpoint stress vectors all coincide as elements of the same 2D vector space.

Equivalently: pick a lab frame at the node; convert each cylinder's local (*e*, *φ*) into the lab-frame (ψ_R, ψ_I); require those (ψ_R, ψ_I) values to match. Each cylinder's local-frame (*e*, *φ*) is then determined by the shared lab-frame ψ via the standard rotation between local frame and lab frame.

This rule reduces to "(*e*_A, *φ*_A) = (*e*_B, *φ*_B)" only when adjacent cylinders share a common cross-section frame (e.g., in the chapter-2 single-edge analysis where two cylinders meet end-to-end along the same axis). At a general wye junction the rule must be expressed in lab-frame components.

### Why hexagonal

Per [grid/hexagonal.md](../../grid/hexagonal.md):

- The hexagonal lattice has cleaner wave propagation than triangular (89% transmitted per junction vs 56%; each junction is a 3-port wye instead of a 6-port crossing).
- It is flexible: hexagons can deform with fixed edge lengths, supporting curvature through pentagonal defects.
- It naturally analogizes to the carbon-nanotube structure that the cylinder primitive's microstructure is meant to evoke.
- Under Model B counting from [grid/lattice-geometry.md](../../grid/lattice-geometry.md) — "the cell IS its edges" — the wye junction has 3 incident edges, giving ζ_2D = 1/3 (the 2D analog of GRID's 3D ζ = 1/4).

Periodic boundary conditions close the lattice into a torus, eliminating boundary effects.

---

## 2. The wave equation on the 2D lattice

Each edge carries a cylinder primitive whose dynamics are chapter 2's wave equation. Each node enforces continuity of the stress vector across all incident edges (chapter 1 §5). Together, these give the lattice equations of motion.

For wavelengths much larger than the lattice spacing *a*, the lattice "looks" continuous and the wave equation is the 2D version of chapter 2's master equation:

<!-- D ∂_t² u = M (∂_x² + ∂_y²) u = M ∇² u -->
$$
D\, \partial_t^2\, \mathbf{u} \;=\; M\, (\partial_x^2 + \partial_y^2)\, \mathbf{u} \;=\; M\, \nabla^2\, \mathbf{u}
$$

where **u**(*x*, *y*, *t*) = (*e*, *φ*)ᵀ is the stress vector field at every spatial point. The 2D Laplacian ∇² replaces the 1D ∂_x²; *D* and *M* are unchanged from chapter 1's matched-chirality matrices.

This is the same equation chapter 4 §4 used (and confirmed numerically in [scripts/](scripts/)); we are now deriving it formally as the long-wavelength limit of a hexagonal lattice with cylinder primitives on edges and wye-junction continuity at nodes.

---

## 3. The long-wavelength continuum: single propagation speed *c*

Look for plane-wave solutions in 2D:

<!-- u(x, y, t) = A exp(i(k·r - ωt)) -->
$$
\mathbf{u}(x, y, t) \;=\; \mathbf{A}\, e^{i(\mathbf{k}\cdot\mathbf{r} - \omega t)}
$$

with **k** = (*k_x*, *k_y*) the 2D wavevector. The Laplacian applied to this brings down −|**k**|² where |**k**|² = *k_x*² + *k_y*².

Substituting:

<!-- ω² D A = |k|² M A -->
$$
\omega^2\, D\, \mathbf{A} \;=\; |\mathbf{k}|^2\, M\, \mathbf{A}
$$

Under matched chirality, *M* = *c*² *D* (chapter 2 §4). Substituting:

ω² *D* **A** = |**k**|² · *c*² *D* **A**

so

<!-- ω² = c² |k|² -->
$$
\omega^2 \;=\; c^2\, |\mathbf{k}|^2
$$

— for any amplitude vector **A**. There is no eigenvalue selection; every direction in (*A_e*, *A_φ*)-space is an eigenvector with the same eigenvalue *c*². The dispersion relation is single-branch:

ω(**k**) = *c* |**k**|

Both polarizations propagate at *c*, isotropically in any direction in the 2D plane. This matches vacuum Maxwell exactly: two photon polarizations both at *c*.

The 2D lattice does not modify the long-wavelength continuum result. Both polarizations propagate cleanly at *c*; there is no slow-mode tension.

---

## 4. Brillouin-zone modes and the photon at the lattice scale

At wavelengths comparable to the lattice spacing *a*, we leave the long-wavelength continuum and enter the Bloch-wave regime: each Bloch wavevector **k** in the Brillouin zone (a hexagonal region of **k**-space) has a discrete spectrum of frequencies — the *bands*. The number of bands per **k**-point equals the number of independent DoF per unit cell.

For the honeycomb lattice with cylinder primitives on edges, the unit cell has 3 edges × 2 DoF = 6 bands per **k**-point.

Under matched chirality with *M* = *c*² *D* on every edge (the same matched-chirality structure that gave the long-wavelength single-speed result), all 6 bands are zone-folded copies of the single dispersion ω = *c* |**k**|. There is no band splitting between different polarizations or between sublattice A and B configurations — every Bloch state propagates at *c*.

The photon at the lattice scale is therefore clean: the cylinder primitive's two polarizations on a 2D hexagonal lattice produce exactly two photon polarizations at *c*, with no extra modes, no birefringence, and no Planck-scale anomalies.

This is what we wanted to confirm before proceeding to the Maxwell-bridge chapter: at the level of single-primitive lattice assembly, the cylinder primitive is consistent with vacuum Maxwell's photon.

A subtlety worth flagging: the matched-chirality structure assumed identical cylinders on every edge. If the lattice had asymmetries between sublattices, or different cylinders on different edges, band gaps and other features could emerge. Those are richer structures than this chapter develops; for the bare hexagonal lattice with identical matched-chirality cylinders, no surprises arise.

---

## 5. Summary of givens

What this chapter establishes:

- The 2D *hexagonal* lattice with cylinder primitives on edges and wye-junction node continuity is the natural assembly: matches grid-docs preferences ([grid/hexagonal.md](../../grid/hexagonal.md), [grid/lattice-geometry.md](../../grid/lattice-geometry.md)), gives ζ_2D = 1/3 from the wye-junction count, and supports natural curvature through pentagonal defects.
- The wave equation on the 2D lattice is *D* ∂_t² **u** = *M* ∇² **u**, with **u** = (*e*, *φ*)ᵀ at every spatial point.
- Under matched chirality (*M* = *c*² *D*, from chapter 1 §8 plus chapter 3's bare-speed condition), the long-wavelength continuum gives a single dispersion ω = *c* |**k**|. Both polarizations propagate at *c*. There is no slow-mode split.
- At lattice scale, the Bloch-wave analysis gives 6 bands per Brillouin-zone point, all of which are zone-folded copies of the single ω = *c* |**k**| dispersion. No Planck-scale anomalies for the bare hexagonal lattice with identical cylinders.
- The cylinder primitive on a 2D hexagonal lattice produces a clean photon at *c* with two polarizations — exactly what vacuum Maxwell expects.

The next chapter takes up the Maxwell bridge: how the cylinder lattice's (*e*, *φ*) coarse-grain to the cell-level phase θ and link-level connection *A_μ* that grid/maxwell.md takes as input.
