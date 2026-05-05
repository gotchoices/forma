# Chapter 6 — The Bridge to Maxwell

This chapter takes the cylinder primitive on a 2D hexagonal lattice (chapters 1–5) and shows how it supplies the inputs that [grid/maxwell.md](../../grid/maxwell.md) takes as given. The job is *not* to re-derive Maxwell's equations — grid/maxwell.md does that, starting from cell-level phase θ and link-level connection *A_μ*. The job is to show that the cylinder primitive *produces* (θ, *A_μ*) at the lattice scale, with the right structure for grid/maxwell.md to run on top.

This is a short bridge. Most of the work has been done in chapters 1–5: the matched-chirality matrix structure, the single propagation speed *c* for both polarizations, the 2D hexagonal lattice with wye junctions, the gauge-symmetric stress vector field. What remains is to identify which structures of the cylinder primitive correspond to which inputs of grid/maxwell.md, and to confirm that gauge invariance — central to Maxwell's derivation — is honored.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | What grid/maxwell.md takes as input |
| 2 | The cylinder primitive's stress vector as a complex matter field |
| 3 | Cell-level phase θ from values at nodes |
| 4 | Link-level connection *A_μ* from variation along edges |
| 5 | Gauge invariance and the cylinder primitive's symmetry |
| 6 | The two polarizations as Maxwell's photon |
| 7 | What this bridge establishes; what is deferred |
| 8 | Summary of givens |

---

## 1. What grid/maxwell.md takes as input

[grid/maxwell.md](../../grid/maxwell.md) derives all four of Maxwell's equations from a small set of GRID axioms (A1–A4 and A6). Its inputs at the lattice scale are:

- A **cell-level phase** θ ∈ [0, 2π) at each lattice cell (axiom A3). The phase is unobservable in absolute terms; only differences between neighboring cells matter.
- A **link-level gauge connection** *A_μ* on each link between cells (forced by axiom A4 — local gauge invariance). *A_μ* is "bookkeeping that lives on links, not cells, that compensates for arbitrary local relabelings of θ."
- The **wave equation** for *A_μ* in vacuum (which grid/maxwell.md derives from the gauge-invariant action) gives Maxwell's equations and the photon at speed *c*.

Both θ and *A_μ* are independent state variables of the lattice. Their dynamics at the lattice scale produce the electromagnetic field.

For our project: chapter 1 §1 set up the relationship — the cylinder primitive's azimuthal direction *φ* is what coarse-grains to *A_μ*. This chapter makes that identification concrete and adds a parallel story for θ.

---

## 2. The cylinder primitive's stress vector as a complex matter field

The cylinder primitive's state at each cross-section is a 2D stress vector ψ = (*e*, *φ*) — two real components, equivalently one complex scalar:

ψ(*x*, *t*) = *e*(*x*, *t*) · exp(*i φ*(*x*, *t*))

with magnitude *e* and phase *φ* (per chapter 1 §3). On a 2D lattice (chapter 5), this becomes ψ(*x*, *y*, *t*) — a complex-valued field defined at every spacetime point.

The complex-scalar structure is the same as the **charged matter field** of standard quantum electrodynamics, where ψ = (amplitude) × exp(*i* phase) couples to the electromagnetic gauge connection *A_μ* through a covariant derivative. The cylinder primitive's stress vector is — at the level of mathematical structure — the *matter field* that grid/maxwell.md's gauge connection *A_μ* will couple to.

This is more than an analogy. The complex-scalar field structure is what licenses the gauge-invariance argument that produces *A_μ* in the first place. Whatever the lattice's "matter" is, it has to be a complex-valued field for the gauge-symmetry story to apply. The cylinder primitive's two-component stress vector is exactly such a field.

A note on terminology. In grid/maxwell.md the "matter field" is identified with the cell phase θ. In the cylinder primitive's framing, the matter field is the full complex ψ — both its phase and its magnitude. The relationship between θ and ψ is the subject of §3.

---

## 3. Cell-level phase θ from values at nodes

In a hexagonal lattice with wye junctions (chapter 5 §1), each node has three incident edges. Node continuity (chapter 1 §5) requires the (*e*, *φ*) values at the meeting endpoints to agree — a single value of ψ at each node, shared by all incident edges.

At each lattice node, the cylinder primitive's azimuthal direction *φ* is the natural identification with grid/maxwell.md's cell phase θ:

θ(*x*) ↔ *φ*(*x*) at lattice nodes

This identification has the right structural properties:

- Both θ and *φ* are angles in [0, 2π) — the right type for a phase field.
- Both are continuous across the lattice — *φ* by node continuity, θ by smoothness in the long-wavelength limit.
- Both are unobservable in absolute terms (only differences matter physically).

The magnitude *e* at each node — the second component of ψ — does *not* correspond to grid/maxwell.md's θ directly. Instead, *e* coarse-grains to a separate quantity at the lattice scale: it is the **matter-field amplitude** that determines how strongly the lattice carries matter at each point. In grid/maxwell.md's framing, this is implicit in the combined matter-field structure ψ = (amplitude) · exp(*i* θ); we make it explicit by keeping *e* = |ψ| and *φ* = arg(ψ) as the two components.

Cell-level matter content at each lattice node is therefore:

(*e*, *φ*) = (|ψ|, arg ψ) at each node

This is what grid/maxwell.md takes as its θ-equivalent input, with the additional information of the matter-field amplitude included.

---

## 4. Link-level connection *A_μ* from variation along edges

The connection *A_μ* in grid/maxwell.md lives on links between cells. It records how the phase changes as you traverse the link — the "translation table" between adjacent cells' phases.

For the cylinder primitive, the cylinder *is* the link. The variation of *φ* along the cylinder's length is the natural identification with grid/maxwell.md's *A_μ*:

*A*(edge) = ∂_x *φ* along the edge (in natural units; with appropriate normalization)

More precisely: let *x* be a coordinate along an edge (cylinder), running from 0 at one node to *L* at the other. The connection *A* on this edge is *∂_x φ*(*x*) — the rate at which the azimuthal direction varies along the edge. In grid/maxwell.md's notation, this is the spatial component of *A_μ* in the direction of the edge.

For the time component *A_0* (corresponding to ∂_t *φ*), the cylinder primitive's time variation of *φ* gives the connection in the time direction. This is consistent with the wave-equation form derived in chapter 2 §2.

Putting both together: at every spacetime point along an edge, the cylinder primitive has (e, φ) and their derivatives. The combination ∂_μ *φ* (μ running over time and the edge's spatial direction) is the local connection *A_μ* that grid/maxwell.md's machinery uses.

A note on the edge-vs-cell geometry. In grid/maxwell.md, *A_μ* is a 4-vector at each link; it has 4 components corresponding to the 4 spacetime directions. In our 2+1D project (a 2D spatial lattice + time), *A_μ* has 3 components. On a hexagonal lattice, each link goes in one of three directions in the 2D plane; the spatial component of *A_μ* on each link is whichever spatial direction that link runs along, plus the time component *A_0* common to all links.

Coarse-graining to the continuum: as the lattice spacing shrinks, the discrete link variables on different-direction edges combine into a smooth 3-vector *A_μ*(*x*, *y*, *t*) at every spacetime point. This is the input that grid/maxwell.md's continuum derivation works with.

---

## 5. Gauge invariance and the cylinder primitive's symmetry

For grid/maxwell.md's derivation to run, *local gauge invariance* (axiom A4) is required: the physics must be unchanged under local relabelings θ(*x*) → θ(*x*) + χ(*x*) at any spacetime point.

The cylinder primitive has exactly this symmetry, by construction. The stress vector ψ in the (*e*, *φ*) plane is the physical object; the polar coordinates (*e*, *φ*) are *one parameterization* of that vector. A different choice of where φ = 0 points — a different polar frame at any point — gives different (*e*, *φ*) values for the same physical ψ. This is a U(1) gauge symmetry built into the cylinder primitive.

Under a local relabeling *φ*(*x*) → *φ*(*x*) + χ(*x*), the gradient ∂_μ *φ* shifts by ∂_μ χ. This is exactly the transformation rule for a gauge connection. Defining *A_μ* via §4 (*A_μ* = ∂_μ *φ* / *e*, in the standard normalization), we get:

*A_μ* → *A_μ* + (1/*e*) ∂_μ χ

— exactly grid/maxwell.md's gauge-transformation rule (where *e* is the elementary charge from axiom A6, not our *e* field — the notation collision is unfortunate but standard).

The cylinder primitive's chirality structure (matched chirality between *M* and *D*) is preserved under this transformation: a local rotation of the polar coordinate frame doesn't change the underlying stress vector field's structure, so the matched-chirality condition that the cylinder primitive's wave dynamics rely on is gauge-invariant.

This means the cylinder primitive *automatically* has the local gauge symmetry that grid/maxwell.md's derivation requires. We do not need to impose it as an additional axiom — it is built into the polar-coordinate structure of the stress vector field at the foundation level (chapter 1 §3).

---

## 6. The two polarizations as Maxwell's photon

Chapter 5 §3 established that on the 2D hexagonal lattice, with matched chirality giving *M* = *c*² *D*, the dispersion relation is single-branch: ω(**k**) = *c* |**k**| for any amplitude vector. Both polarizations propagate at *c*.

In Maxwell's framing on a 2D space:
- A photon has 1 transverse polarization (perpendicular to its propagation direction in the 2D plane).
- The longitudinal/Coulomb component of the gauge field is non-radiative (gauge-fixable, no propagation).

The cylinder primitive's two-polarization structure on the 2D lattice has two propagating modes both at *c*. Mapped to Maxwell:
- One polarization corresponds to the transverse photon (the radiative degree of freedom).
- The other polarization corresponds to the longitudinal/scalar gauge component (the non-radiative Coulomb potential).

In Coulomb gauge (∇ · **A** = 0), the longitudinal component is fixed by sources and does not propagate as a wave. The cylinder primitive's two modes both propagate at *c*, but at the level of *physical* (gauge-fixed) propagating degrees of freedom, only the transverse mode is the photon. The longitudinal mode is the static Coulomb potential, also propagating at *c* in the ungauged formulation but reduced to its gauge-fixed equivalent (a non-radiative source-determined field) in the physical theory.

This identification is consistent with chapter 4's static result: the 2D Laplacian Green's function (1/r force in 2D) is exactly the Coulomb potential of 2+1D Maxwell. The cylinder primitive at static equilibrium is producing the Coulomb component; at dynamic equilibrium it produces the transverse photon. Both are in the same wave equation, and both propagate at *c* in our model — consistent with vacuum Maxwell.

For higher-dimensional generalizations: in 3+1D Maxwell, the photon has 2 transverse polarizations (both radiative), and the longitudinal/scalar potential is non-radiative. A 3D extension of the cylinder primitive lattice (cylinders along edges of a 3D lattice) would supply 3 photon modes per cell, of which 2 are transverse and 1 is longitudinal — the standard Maxwell structure. This extension is outside chapter 6's scope but is the natural next step.

---

## 7. What this bridge establishes; what is deferred

### Established by this chapter

- The cylinder primitive's stress vector ψ = *e* exp(*i φ*) on a 2D lattice has the complex-scalar structure that grid/maxwell.md's matter field requires.
- At each lattice node, the value of ψ is the cell-level state; the phase *φ* is the cell phase θ that grid/maxwell.md uses.
- Along each edge, the variation of *φ* is the link-level gauge connection *A_μ* that grid/maxwell.md uses.
- The cylinder primitive automatically has local U(1) gauge invariance from the polar-coordinate structure of the stress vector.
- The two polarizations propagate at *c*, matching Maxwell's photon (with the longitudinal component being non-radiative under gauge fixing).
- The wave equation of chapter 2 (with matched chirality giving single propagation speed *c*) reduces in the long-wavelength limit to Maxwell's wave equation in vacuum.

### What grid/maxwell.md takes from here

With (*e*, *φ*) on edges providing both the matter field ψ and the gauge connection *A_μ*, grid/maxwell.md's derivation runs unchanged on top. The four Maxwell equations follow from the gauge-invariant Lagrangian, the field tensor *F_μν* = ∂_μ *A_ν* − ∂_ν *A_μ*, and the equations of motion derived from the action.

We do not re-derive grid/maxwell.md's content here. We supply its inputs.

### Deferred to chapter 7

The coefficient question — whether the cylinder primitive's parameters give the correct value of α (the electromagnetic coupling) — is taken up alongside the gravity-coefficient question in chapter 7 and the α-derivation in chapter 8. grid/maxwell.md takes α as an input (axiom A6); the question of how α emerges from the cylinder primitive's geometry is a separate downstream question.

### Deferred to a 3D extension

Generalizing from 2D to 3D extends the photon to two transverse polarizations and re-introduces the standard 3+1D electromagnetic structure. This is the natural next step but is outside this project's scope (the project commits to 2D per ground rule 7).

---

## 8. Summary of givens

What this chapter establishes:

- The cylinder primitive's stress vector ψ = *e* exp(*i φ*) is the matter field of grid/maxwell.md, with magnitude *e* and phase *φ* taking the natural complex-scalar form.
- At lattice nodes, *φ* is the cell phase θ that grid/maxwell.md takes as input.
- Along lattice edges, ∂_μ *φ* is the gauge connection *A_μ* that grid/maxwell.md takes as input.
- Local U(1) gauge invariance is built into the cylinder primitive at the foundation level (the polar-coordinate freedom on the stress vector field).
- The matched-chirality condition (chapter 1 §8) makes both polarizations propagate at *c*; in Maxwell, this corresponds to the transverse photon (radiative) and the longitudinal/Coulomb component (non-radiative under gauge fixing) both propagating at *c* in the ungauged formulation.
- grid/maxwell.md's derivation runs unchanged on top of this lattice setup. The cylinder primitive supplies its inputs; Maxwell's equations follow.

The next chapter takes up the gravity-coefficient calculation: matching the cylinder primitive's continuum Green's-function coefficient to GRID's geometrically-derived ζ.
