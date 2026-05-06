# Chapter 6 — The Bridge to Maxwell

This chapter takes the cylinder primitive on a 2D hexagonal lattice (chapters 1–5) and shows that it is **compatible with** [grid/maxwell.md](../../grid/maxwell.md) — i.e., grid/maxwell.md's derivation runs on top of the lattice this project supplies. The job is *not* to re-derive Maxwell's equations; grid/maxwell.md does that, starting from a complex matter field with phase θ, a gauge connection A_μ on links (axiom A4), and local gauge invariance.

The headline result of this chapter is that the cylinder primitive supplies what the bridge needs:

1. **A substrate for the matter sector** — the complex field ψ = *e* · exp(*i φ*) at each node, with *φ* serving as the cell phase θ that grid/maxwell.md takes as input from axiom A3.
2. **The local U(1) gauge symmetry** that grid/maxwell.md requires from axiom A4 — the polar-frame freedom *φ* → *φ* + χ on the cylinder primitive's stress vector is exactly that symmetry.
3. **Lorentz-compatible matter dynamics** at the lattice scale — the wave equation of chapter 2 with both polarizations propagating at *c*.

With these in hand, grid/maxwell.md's derivation runs on top: it takes A_μ from axiom A4 directly (a link-level connection independent of the matter sector), and Maxwell's equations follow from the gauge-invariant Lagrangian.

A clarifying note on what this chapter does *not* claim: an earlier draft identified A_μ with ∂_μ *φ* — i.e., asserted that the cylinder primitive supplies both θ *and* A_μ from its own structure. That identification was over-reaching: A_μ ≡ ∂_μ *φ* gives F_μν = 0 (pure-gauge, no photon dynamics) and so could not have carried Maxwell's content. We retire it (§4), and the bridge does not depend on it. Independent A_μ on links is grid/maxwell.md's input from A4, not something the cylinder primitive needs to produce. This is also why grid/maxwell.md's *gauge sector* (the dynamics of A_μ itself, including F_μν F^μν) sits on top of the cylinder primitive rather than emerging from it; routes by which A_μ-like content could *emerge* from cylinder-primitive structure (topological winding, the 3D extension) are noted as future questions, not current requirements.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | What grid/maxwell.md takes as input |
| 2 | The cylinder primitive's stress vector as a complex matter field |
| 3 | The matter field at lattice nodes: ψ supplies θ |
| 4 | Where A_μ lives — a clarifying note on what the bridge does and does not require |
| 5 | Gauge invariance: the cylinder primitive's polar-frame freedom is the U(1) symmetry |
| 6 | The two polarizations and Maxwell's photon |
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

## 3. The matter field at lattice nodes: ψ supplies θ

The identification of grid/maxwell.md's cell-level phase θ with the cylinder primitive's azimuthal direction *φ* is not a structural analogy; it is a direct reading of what each thing *is*.

Grid/maxwell.md treats the matter field abstractly. In the standard QED-style derivation that grid/maxwell.md mirrors at the lattice level, the matter field is a complex scalar ψ_matter = ρ · exp(*i*Θ), where ρ is its amplitude and Θ its phase. Gauge invariance under Θ → Θ + χ(*x*) is what motivates the introduction of the gauge connection A_μ. The "cell-level phase θ" in grid/maxwell.md *is* the phase Θ of this matter field at each cell.

The cylinder primitive supplies a complex matter field directly. Its stress vector at each cross-section is ψ = *e* · exp(*i φ*), with magnitude *e* and phase *φ* (chapter 1 §3). Node continuity (chapter 1 §5) makes ψ single-valued at each node. So at each node:

ψ(node) = *e*(node) · exp(*i φ*(node))

is the cell-level matter field, with magnitude *e* and phase *φ*. The phase *φ* is therefore *exactly* what grid/maxwell.md calls θ — they are not two structurally similar quantities but the same thing in different notation:

θ(node) ≡ *φ*(node)

The magnitude *e* is the matter-field amplitude (often suppressed in grid/maxwell.md's discussion when only the phase sector is in play). Cell-level matter content at each lattice node is the full ψ = *e* · exp(*i φ*).

The dynamics of φ — and hence of θ — is what chapter 2's wave equation supplies. The gauge symmetry under *φ* → *φ* + χ(*x*) (next sections) is what grid/maxwell.md's derivation requires for A_μ to enter as a connection.

---

## 4. Where A_μ lives — a clarifying note on what the bridge does and does not require

Grid/maxwell.md's gauge connection *A_μ* lives on links between cells. It is an *independent dynamical field*, taken as input from axiom A4 alongside the cell-level phase θ from axiom A3. Maxwell's equations are equations *for A_μ*, with field strength F_μν = ∂_μ A_ν − ∂_ν A_μ encoding the photon's content.

For the bridge from the cylinder primitive to grid/maxwell.md to work, A_μ does *not* need to be supplied by the cylinder primitive's own structure. It is supplied by axiom A4 directly. What the cylinder primitive must do is *be consistent with* A4 — i.e., have the local U(1) gauge symmetry that A4's connection structure requires, and supply a matter substrate that A_μ couples to. Both are established in this chapter. With both in hand, grid/maxwell.md's derivation runs.

A clarifying note on an earlier-draft over-reach. Some early versions of this chapter went further and *identified* A_μ with ∂_μ *φ* — i.e., asserted that the cylinder primitive supplies the gauge field from its own internal structure. That identification was tempting because ∂_μ *φ* transforms the right way under *φ* → *φ* + χ, but it is not consistent with A_μ's role as an independent dynamical field:

- ∂_μ *φ* is the gradient of a single-valued scalar, not an independent field.
- The would-be field strength F_μν = ∂_μ(∂_ν *φ*) − ∂_ν(∂_μ *φ*) = 0 for single-valued, smooth *φ*.
- F_μν ≡ 0 is a pure-gauge configuration — no photon, no Coulomb interaction.

So A_μ ≡ ∂_μ *φ* would have identified the gauge field with a configuration that carries no electromagnetism. We therefore retire that identification. **The bridge to Maxwell does not depend on it**: A_μ is grid/maxwell.md's input from A4, not something the cylinder primitive is asked to produce.

A subsequent question worth noting (but outside this chapter's scope): could the cylinder primitive, suitably extended, supply A_μ-like content from below as well — i.e., could a richer cylinder-primitive structure also produce a connection field with non-trivial F_μν, in addition to the matter sector? Two routes by which this could happen are:

- **Topological winding of *φ*.** If *φ* is allowed to be multi-valued — picking up integer multiples of 2π around closed loops in the lattice — the holonomy around closed loops becomes non-zero, and a corresponding F_μν acquires support concentrated on the loop. This is exactly the wrap/winding picture chapter 8 explores for the α question.
- **The 3D extension.** This project's 2D restriction misses degrees of freedom that the natural 3D extension would supply. The gauge-field sector is most cleanly introduced when the lattice has the higher-dimensional structure that supports it.

These are interesting follow-up directions for *deepening* the bridge — for asking whether the cylinder primitive can supply A_μ from below in addition to supplying the matter sector. The bridge as established in this chapter does not depend on either; grid/maxwell.md's derivation runs on the matter substrate and gauge symmetry already in hand.

---

## 5. Gauge invariance: the cylinder primitive's polar-frame freedom is the U(1) symmetry

For grid/maxwell.md's derivation to run, *local gauge invariance* (axiom A4) is required: the physics must be unchanged under local relabelings of the matter-field phase, *φ*(*x*) → *φ*(*x*) + χ(*x*) at each spacetime point.

The cylinder primitive has exactly this symmetry, by construction. The stress vector ψ in the cross-sectional plane is the physical object; the polar coordinates (*e*, *φ*) are *one parameterization* of that vector — a *choice of where φ = 0 points*. A different choice of polar frame at each spatial point gives different (*e*, *φ*) values for the same physical ψ. This polar-frame freedom is a U(1) gauge symmetry built into the cylinder primitive at the foundation level (chapter 1 §3).

Under a local relabeling *φ*(*x*) → *φ*(*x*) + χ(*x*), the matter field transforms as

ψ(*x*) → exp(*i* χ(*x*)) · ψ(*x*)

— the standard U(1) transformation of a complex matter field. The cylinder primitive's chirality structure (matched chirality between *M* and *D*) and bare-speed equality are both preserved: a local rotation of the polar frame doesn't change the underlying stress vector field's structure, so the cylinder primitive's wave dynamics are invariant under the gauge transformation.

What grid/maxwell.md needs from this is the *existence* of the symmetry — that the matter sector ψ has a local U(1) phase invariance — not a specific construction of A_μ. The standard derivation then proceeds: gauge invariance under χ(*x*) requires introducing a connection field A_μ on links that transforms as A_μ → A_μ + (1/*q*) ∂_μ χ (with *q* the elementary charge from axiom A6, written *q* to avoid colliding with the cylinder primitive's *e* field), and the gauge-covariant derivative D_μ ψ = (∂_μ − *i q A_μ*) ψ replaces the ordinary derivative in the matter Lagrangian. Maxwell's equations for A_μ then follow from the gauge-invariant Lagrangian (1/4) F_μν F^μν.

The cylinder primitive's contribution at this stage is to *demonstrate* that the U(1) gauge symmetry is present in the matter sector. It does not, by itself, supply the gauge field A_μ as an independent dynamical degree of freedom — see §4. The A_μ field is an additional structure that grid/maxwell.md's derivation introduces; the cylinder primitive's job is to show that the matter sector has the symmetry that demands it.

---

## 6. The two polarizations and Maxwell's photon

Chapter 5 §3 established that on the 2D hexagonal lattice, with matched chirality and bare-speed equality giving *M* = *c*² *D*, the dispersion relation is single-branch: ω(**k**) = *c* |**k**| for any amplitude vector. Both polarizations propagate at *c*.

This is *not* directly the structure of 2+1D Maxwell. In 2+1D Maxwell, a photon propagating in a given direction has only **one** transverse polarization (perpendicular to its propagation direction in the 2D plane), plus a non-radiative longitudinal/Coulomb mode that is fixed by sources rather than propagating. So 2+1D Maxwell expects 1 propagating mode, while the cylinder primitive's 2D lattice has 2.

The cleanest reading of this mismatch is that the cylinder primitive's two propagating modes are best understood as the analogs of the *two transverse photon polarizations* of 3+1D Maxwell — not as "1 transverse + 1 Coulomb in 2+1D." The 2D restriction of this project misses the third (Coulomb) channel rather than splitting the photon's polarization budget across the existing two.

This reading is consistent with the structural arc of the project:

- In 3+1D Maxwell, a photon has 2 transverse polarizations (both radiative at *c*) plus 1 non-radiative Coulomb mode.
- The cylinder primitive on a 3D lattice (the natural extension of this project, deferred to follow-up per ground rule 7) would supply 3 modes per cell: 2 carrying the transverse polarizations and 1 carrying a separate Coulomb-channel role.
- This project's 2D restriction supplies 2 of those 3 modes — the two transverse polarizations — without yet supplying the Coulomb channel. The two cylinder modes propagating at *c* are the lattice-scale realization of the two photon polarizations; the Coulomb channel emerges only when the spatial lattice is extended to 3D.

Chapter 4's static result fits this reading. The 2D Laplacian Green's function (1/r force in 2D) is the static-limit response of the cylinder primitive's two transverse fields. In standard Maxwell the static 1/r law would come from the Coulomb channel, but in this project's 2D restriction the same 1/r structure is produced by the same wave equation that supplies the transverse polarizations — there is no separate Coulomb sector to maintain the distinction. When the project extends to 3D, the static and dynamic responses will sit in different sectors (Coulomb vs transverse) and the standard Maxwell structure recovers.

So the §3 and §4 identifications (φ ↔ θ at nodes; ∂_μ φ ↔ A_μ along edges) supply the inputs for the *transverse* sector of grid/maxwell.md cleanly, and grid/maxwell.md's transverse-photon derivation runs unchanged on top. The Coulomb sector of grid/maxwell.md is not directly supplied by this project's 2D primitive lattice; that supply requires the 3D extension.

---

## 7. What this bridge establishes; what is deferred

### Established by this chapter

- The cylinder primitive's stress vector ψ = *e* exp(*i φ*) on a 2D lattice *is* the complex-scalar matter field that grid/maxwell.md treats abstractly as ψ_matter = ρ exp(*i*Θ).
- At each lattice node, the phase *φ* is exactly grid/maxwell.md's cell phase θ — same quantity, different notation.
- The cylinder primitive's polar-frame freedom (*φ* → *φ* + χ at each node) is the local U(1) gauge symmetry that grid/maxwell.md's derivation requires from axiom A4.
- The two propagating polarizations both at *c* match the *two transverse polarizations* of a 3+1D photon (the project's 2D restriction does not yet supply the Coulomb sector — see §6).
- The wave equation of chapter 2 (with matched chirality + bare-speed equality giving single propagation speed *c*) reduces in the long-wavelength limit to the matter-sector wave equation that grid/maxwell.md couples to A_μ via the covariant derivative.

**Net result: the cylinder primitive lattice is compatible with grid/maxwell.md.** Grid/maxwell.md's derivation runs unchanged on top: the matter substrate is supplied by the cylinder primitive, the gauge symmetry it requires is built in, and A_μ enters from axiom A4 as in any standard gauge-theory construction.

### What grid/maxwell.md takes from here

- **Matter Lagrangian.** Whatever form it takes (Klein-Gordon, Dirac, etc.), it acts on the ψ this chapter supplies. The gauge-covariant derivative D_μ ψ = (∂_μ − *iqA_μ*)ψ runs as standard.
- **Gauge Lagrangian.** The (1/4)F_μν F^μν Lagrangian gives Maxwell's equations for A_μ as in standard QED, with A_μ supplied directly from axiom A4.
- **Gauge invariance.** Built into the cylinder primitive at the foundation level (§3, §5).

The bridge as a whole: the cylinder primitive supplies the matter sector and the gauge symmetry; A_μ comes from A4; grid/maxwell.md derives Maxwell's equations from these inputs. The case for compatibility is made.

A separate, future-direction question — *can the cylinder primitive be extended so that A_μ also arises from below?* — is flagged in §4 (topological winding, 3D extension). This would deepen the bridge but is not required for it to be made.

### Deferred to chapter 7

The coefficient question — whether the cylinder primitive's parameters give the correct value of α (the electromagnetic coupling) — is taken up alongside the gravity-coefficient question in chapter 7 and the α-derivation in chapter 8. grid/maxwell.md takes α as an input (axiom A6); the question of how α emerges from the cylinder primitive's geometry is a separate downstream question.

### Deferred to a 3D extension

Generalizing from 2D to 3D extends the photon to two transverse polarizations and re-introduces the standard 3+1D electromagnetic structure. This is the natural next step but is outside this project's scope (the project commits to 2D per ground rule 7).

---

## 8. Summary of givens

What this chapter establishes:

- The cylinder primitive's stress vector ψ = *e* exp(*i φ*) *is* the matter field of grid/maxwell.md — same quantity, different notation. The phase *φ* is exactly the cell phase θ; the magnitude *e* is the matter-field amplitude.
- The cylinder primitive's polar-frame freedom (*φ* → *φ* + χ) is the local U(1) gauge symmetry that grid/maxwell.md requires from axiom A4.
- Matched chirality + bare-speed equality (chapters 1 §8 and 2 §4) make both polarizations propagate at *c*. The cleanest reading of the two cylinder modes is as the lattice-scale analogs of the *two transverse photon polarizations* of 3+1D Maxwell. (2+1D Maxwell expects only 1 propagating mode per direction; the Coulomb channel is missing from this project's 2D restriction and would emerge from the 3D extension — ground rule 7, deferred.)
- **The cylinder primitive lattice is compatible with grid/maxwell.md.** grid/maxwell.md's derivation runs unchanged on top: matter substrate from the cylinder primitive, gauge symmetry built in, A_μ from axiom A4 in the standard gauge-theory way. Maxwell's equations follow.
- An over-reaching subclaim from earlier drafts — that A_μ could be identified with ∂_μ *φ* directly (i.e., that the cylinder primitive supplies A_μ from below as well as θ) — gives F_μν ≡ 0 and has been retired (§4). The bridge does not depend on it. Whether a deeper extension of the cylinder primitive could also supply A_μ from below is a future-direction question (topological winding, 3D extension) noted in §4.

The next chapter takes up the gravity-coefficient calculation: matching the cylinder primitive's continuum Green's-function coefficient to GRID's geometrically-derived ζ.
