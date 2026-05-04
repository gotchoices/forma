# Chapter 1 — Foundation

This chapter establishes the *primitive*, *fields*, and *connection rules* on which the rest of the project rests. It is the only chapter where things are **assumed**; every later chapter must derive its claims from what is stated here.

**Prerequisite:** familiarity with [grid/foundations.md](../../grid/foundations.md), which defines the GRID lattice axioms (A1–A6) at the cell level. This chapter assumes that material as background and concentrates on what sits *one layer below* the cell — the structure of an individual primitive that, when assembled into a lattice, supplies the inputs the GRID derivations require.

The chapter is paced deliberately slowly. Once a definition is set here it is used as-is throughout the rest of the project; revisions will be flagged explicitly when they happen.

---

## Concepts introduced in this chapter

| § | Concept |
|---|---------|
| 1 | The lattice, the primitive, and where this project sits |
| 2 | The cylinder's geometry (length, radius, transit time) |
| 3 | The two fields: strain *e(x, t)* and azimuthal phase *φ(x, t)* |
| 4 | Boundedness — why *φ* is compact and *e* is not |
| 5 | Nodes as passive continuity boundaries |
| 6 | The stiffness matrix M |
| 7 | The shear coupling *K_eφ* |
| 8 | Relationship to the earlier viz model |
| 9 | What is taken as input from GRID |
| 10 | Explicit non-assumptions |
| 11 | Summary of givens |

---

## 1. The lattice, the primitive, and where this project sits

The GRID lattice is a regular 4D causal array of cells (axiom A1 of [grid/foundations.md](../../grid/foundations.md)). Each cell carries an internal phase θ ∈ [0, 2π) (A3); each link between cells carries a gauge connection A_μ (A4). Maxwell's equations, charge quantization, and entropic gravity are all derived from the collective behavior of (θ, A_μ) on the lattice.

An intuition for what *gauge* and *A_μ* mean is worth carrying through the rest of the project. Each cell can be visualized as a small clock hand pointing in some direction on a circle — that is the phase θ. The physical content is *not* where any one clock hand points; it is the *difference* between the hands of neighboring clocks. Two configurations that look completely different at the cell level — every clock pointing in a different absolute direction — are physically the same as long as the differences between neighboring clocks agree.

The freedom to relabel each cell's clock by an arbitrary amount, without changing the physics, is **local gauge invariance**. For this invariance to be consistent, the lattice has to record an offset on each *link* between cells: how much the two clocks at the link's endpoints have been independently rotated relative to each other. That offset is the **gauge connection A_μ** — bookkeeping that lives on links, not cells, and that compensates for arbitrary local relabelings of θ. In the continuum limit, A_μ is the electromagnetic four-potential, and its dynamics produce the electromagnetic field. Inside this project, A_μ is one of the structures the cylinder primitive has to supply at the lattice scale; the cylinder's azimuthal phase *φ* is what coarse-grains to it.

This project sits one layer below. The question is: *what is the primitive substrate from which (θ, A_μ) emerge?* Concretely — when GRID writes "the lattice has cells and links," what *is* a cell or a link, and what supports its state?

The project commits to a specific picture: each link is a **2D cylindrical tube**, and each cell is a junction (a *node*) where multiple cylinders meet. The cylinder is the primitive. Cells, in this framing, are where cylinders connect — they are not state-bearing units in their own right.

This is a deliberate choice, not a derivation. Other primitive structures could have been considered (the dialog [grid-3.md](../../dialogs/grid-3.md) brainstormed several), and the cylinder is the candidate this project commits to. Whether it works is a hypothesis to be tested chapter by chapter; if it fails a check, the project either pivots or rescopes (see [README.md](README.md) ground rules 2 and 8).

---

## 2. The cylinder's geometry

A single cylindrical primitive is characterized by two geometric parameters:

| Symbol | Meaning |
|---|---|
| *L* | Length along the cylinder's long axis |
| *r* | Radius of the circular cross-section |

Both are positive real numbers and remain symbolic. The lattice spacing fixes *L* (one cylinder spans one lattice unit), but no numerical value is committed to until the algebra forces it.

A perturbation that enters the cylinder at one end takes time to reach the other end. This **transit time** is denoted *τ*:

τ = *L*/*c*

where *c* is the lattice signal speed defined by GRID axiom A1 (one cell per tick). The relation τ = *L*/*c* is a definition — *τ* is set by *L* and *c* together. The substantive question of how *τ* relates to the cylinder's *internal* dynamics is deferred.

Mechanical picture: the cylinder is a small, slightly elastic tube. Picture a rubber sleeve of length *L* and radius *r*, glued to its neighbors at each end. Under tension along its length the sleeve stretches; under torque around its long axis the sleeve twists. The combined picture is what hosts the wave dynamics.

---

## 3. The two fields: stress magnitude and azimuthal direction

The cylinder hosts a single physical object at each cross-section: an **internal stress vector** in the cross-sectional plane. This vector is described by two real-valued fields, each a function of position along the cylinder *x* ∈ [0, *L*] and time *t*:

- *e(x, t)* — **longitudinal stress magnitude**: the strength of the internal compression or tension at cross-section *x*. The sign convention is *e* > 0 for tension, *e* < 0 for compression, *e* = 0 for rest. *e* takes any real value.

- *φ(x, t)* — **azimuthal direction**: the angular location around the cross-section where the stress is concentrated — equivalently, the direction in which the cylinder is bowed by an off-center load. *φ* is an angle, periodic mod 2π.

The pair (*e*, *φ*) are polar coordinates of the stress vector; the underlying object is a 2D real vector with two independent real components in the cross-sectional plane. Either pair of coordinates would describe the same field — polar (*e*, *φ*) is convenient for the topological discussion in §4 and for matching the dialog's framing, while Cartesian (real and imaginary parts of the stress vector) is convenient for the linear wave equations in chapter 2.

There is no third state variable, no separate "twist" field, no body rotation of the cylinder. The cylinder body does not rotate around its long axis; *φ* is an angle in the cross-sectional plane (where the stress vector points), not a rotation angle of the cylinder mass.

The mechanical picture: a rubber cylinder reinforced with helical fibers, glued at the endpoints to its neighbors. Pushing on one endpoint *off-center* — at azimuthal location *φ* with longitudinal force *e* — exerts a directional load that the helical fibers couple to a transverse bow of the cylinder body. The bow propagates along the length and emerges at the far end as a perturbation in the next cylinder's (*e*, *φ*). The off-center loading at the end is what carries the directional information; the cylinder body itself does not rotate.

Two consequences worth marking now:

- **Distributed, not lumped.** The state at one end of the cylinder is not the same as the state at the other end at the same instant. A perturbation injected at *x* = 0 takes transit time *τ* to reach *x* = *L*. This is in deliberate contrast to the earlier viz model (§8), where each edge held a single lumped value with no spatial structure along the edge.

- **Polar singularity at *e* = 0 is a coordinate artifact.** When the stress magnitude vanishes, "where the stress is concentrated" has no unique answer — *φ* is undefined. This is the standard singularity of polar coordinates at the origin. The underlying stress vector is smoothly zero there; only the (*e*, *φ*) parameterization is singular. A separate physical interpretation introduced as an alternative in early drafts — treating *φ* as the direction of a transverse bow with *e* as bow magnitude — has the same singularity (and is in fact the same complex-scalar primitive in different language). It is not adopted here as a separate model.

---

## 4. Topology of the stress vector field — what makes entropy possible

The 2D stress vector field at each (*x*, *t*) takes values in a 2D plane (the cross-sectional plane). The target space is ℝ², or equivalently ℂ if we package the stress vector as a complex scalar ψ(*x*, *t*) = *e* · exp(*iφ*).

The compactness of *φ* in our polar parameterization is a property of the *coordinates*, not of the *target space*. Target-space topology is flat (ℝ²) — there is no intrinsic "wraparound" that loses information when the polar angle crosses 2π. The angle is just a coordinate label on a flat plane, and the underlying stress vector is smooth across the apparent wrap.

What survives, and is genuinely topological, is the *non-trivial homotopy structure*:

π₁(ℝ² \ {0}) = ℤ

That is: closed loops in the plane *with the origin removed* are classified by an integer — the winding number around the origin. This is what makes **vortex defects** possible.

A vortex defect is a point in (*x*, *t*) space where the stress vector vanishes (*e* = 0) and where the surrounding stress vector field circulates with nonzero winding number as one traces a small loop around the point. Each vortex is labeled by an integer winding *n* ∈ ℤ. Vortices of opposite sign can annihilate; vortices of the same sign repel. In thermal equilibrium on a 2D field theory of this type, vortex–antivortex pairs proliferate.

This is the **2D XY model** universality class. The Berezinskii–Kosterlitz–Thouless (BKT) transition separates a low-temperature regime (vortices bound in pairs) from a high-temperature regime (vortices unbound and free). In either regime, defects carry entropy.

A note on what the cylinder primitive makes available for the entropy story. Three structures coexist on the primitive, any of which could in principle source entropy; chapter 4 will sort through them:

1. **Topological vortex defects in the 2D stress vector field** — points in (*x*, *t*) where *e* = 0 with nonzero winding number around them. This is the primary candidate, and the one chapter 4 examines first.

2. **Non-trivial winding sectors of *φ(x)* along the cylinder** — for a fixed time, *φ(x)* can wrap the 2π circle some integer number of times as *x* ranges over [0, *L*]. The winding number is a discrete invariant per cylinder, complementary to defects in (*x*, *t*).

3. **Longitudinal Fourier modes of *e* and *φ*** — Fourier-decomposing the fields along *x* gives a tower of mode amplitudes, each an oscillator. This is the mathematical structure that supplied [grid/sim-gravity-2/](../../grid/sim-gravity-2/)'s entropy reservoir on the ℵ-line; it remains available as a backup if the topological-defect mechanism does not suffice.

All three are present. Which (if any) actually sources the entropy required for Jacobson's argument is the substantive question of chapter 4. The topological-defect mechanism (1) is the load-bearing bet of theory 7 in [README.md](README.md); a negative result triggers fallback to a discrete primitive (ground rule 8).

---

## 5. Nodes as passive continuity boundaries

Where multiple cylinders meet — a node, the primitive's analog of a GRID cell — there is no state of its own. Nodes are not data structures; they are geometric points where adjacent cylinder endpoints coincide.

The role of a node is to impose **continuity of the stress vector**:

> At the junction where two cylinders meet, the 2D stress vectors at the meeting endpoints agree as vectors.

Concretely: if cylinder A's right end (at *x_A* = *L*) meets cylinder B's left end (at *x_B* = 0), then for all *t* the stress vector matches across the junction. In polar coordinates this is *e_A*(*L*, *t*) = *e_B*(0, *t*) and *φ_A*(*L*, *t*) = *φ_B*(0, *t*); in Cartesian coordinates it is the equality of the underlying 2D vectors directly. (The Cartesian statement is well-defined even when *e* = 0, where the polar one is not — another reason to think of the stress vector as the underlying object.)

When more than two cylinders meet at a node, the same continuity holds across all of them — every cylinder's endpoint at the node carries the same stress vector at every instant.

This is a boundary condition, not an update rule. Nodes do not compute, average, advance time, or maintain state. They are passive in the strongest sense — like the corners of the original Yee cell, which carry no field components and have no update. Newton's third law (force balance across the junction) is automatically satisfied by the continuity of the stress vector; no further constraint is needed.

Mechanical picture: the cylinders are glued at their endpoints. The glue is rigid in position — meeting endpoints are co-located — but transmits the off-center longitudinal load (the stress vector) intact across the junction. No body rotation is required at endpoints; the junction simply transmits the directional information of the stress.

---

## 6. The stiffness matrix M

The cylinder's two fields couple through a 2 × 2 symmetric stiffness matrix *M*:

<!-- M = (Kₑₑ K_(eφ); K_(eφ) K_(φφ)) -->
$$
M = \begin{pmatrix} K_{ee} & K_{e\phi} \\ K_{e\phi} & K_{\phi\phi} \end{pmatrix}
$$

Each entry has a physical meaning:

- *K_ee* — diagonal stiffness for strain alone. The cylinder's resistance to longitudinal compression or extension. Real and positive.
- *K_φφ* — diagonal stiffness for phase alone. The cylinder's resistance to azimuthal twist. Real and positive.
- *K_eφ* — off-diagonal coupling between strain and phase. Real, no sign constraint at this stage.

All three entries remain symbolic; nothing in this chapter pins their numerical values. The dynamics that *M* governs — how *e(x, t)* and *φ(x, t)* evolve in time — is the subject of the next chapter.

Two formal properties of *M* will be used later:

**Stability.** *M* must be positive-definite for the cylinder's energy to be bounded below. This requires:

K_ee > 0,  K_φφ > 0,  K_eφ² < K_ee · K_φφ

The strict inequality on the off-diagonal is what keeps wave dynamics nontrivial; equality (K_eφ² = K_ee · K_φφ) is the degenerate boundary at which the wave speed collapses to zero.

**Dimensionless shear.** The natural parameterization of the off-diagonal coupling, scale-invariant by construction:

χ̃ = K_eφ / √(K_ee · K_φφ),  with χ̃ ∈ (0, 1) in the stable range.

χ̃ = 0 means strain and phase are decoupled; χ̃ = 1 is the degenerate stability boundary; χ̃ ∈ (0, 1) is where wave propagation lives.

---

## 7. The shear coupling *K_eφ*

Among the three entries of *M*, the off-diagonal *K_eφ* deserves a separate paragraph because it is what makes the cylinder a *wave-supporting* medium rather than two independent decoupled springs.

If *K_eφ* = 0, the cylinder's strain and phase evolve independently. A longitudinal perturbation produces only longitudinal oscillation; an azimuthal perturbation produces only azimuthal oscillation. There is no exchange between the two channels and no propagating wave along the cylinder.

If *K_eφ* ≠ 0, strain and phase drive each other. A stretch at one position induces a twist; a twist induces a stretch elsewhere. The wave that propagates along the cylinder is a coupled stretch-and-twist motion in which neither field carries the wave alone.

Mechanical picture: imagine the rubber cylinder of §2 reinforced with helical fibers wrapped around the wall at a non-trivial angle. When the cylinder is pulled along its length, the fibers refuse to lengthen along the helix without also rotating, so a stretch forces a twist. *K_eφ* is the strength of that coupling — geometrically, it is set by the helix angle of the fibers (achiral fibers give *K_eφ* = 0; maximally chiral fibers give the largest *K_eφ*).

This is the substantive structural commitment of the primitive. The cylinder is not a chiral mathematical curiosity — by hypothesis, it is what supports wave propagation in the lattice at all.

---

## 8. Relationship to the earlier viz model

The earlier viz model ([viz/grid-lab.md](../../viz/grid-lab.md)) treated edges and nodes as separate primitives:

- Each edge carried one real-valued magnitude (lumped — no internal spatial structure along the edge).
- Each node carried one periodic phase (also lumped).
- A discrete two-phase clock alternated edge updates and node updates (Yee-style).

The cylinder primitive supersedes this in three ways:

1. The edge's magnitude and the node's phase are folded into a *single* primitive — the cylinder — which carries both.
2. Lumped values are replaced by distributed fields *e(x, t)* and *φ(x, t)* along the cylinder's length.
3. The node becomes passive (no clock, no update) and the cylinder becomes active (the wave propagates *along* it, with internal transit time *τ*).

The viz remains a useful intuition tool for direct propagation (left-going pulses, right-going pulses, superposition), but it is not the foundational model for this project.

---

## 9. What is taken as input from GRID

The project assumes — and does not re-derive — the following from [grid/foundations.md](../../grid/foundations.md):

| Input | Source |
|---|---|
| 4D causal lattice | Axiom A1 |
| Lorentzian (1, 3) signature | Axiom A2 |
| Lattice signal speed *c* (one cell per tick) | Axiom A1 |
| Cell-level periodic phase θ ∈ [0, 2π) | Axiom A3 |
| Local gauge invariance and connection A_μ on links | Axiom A4 |
| Information-resolution parameter ζ = 1/4 per cell | Axiom A5 |
| Coupling α ≈ 1/137 | Axiom A6 |

The "4D causal lattice" entry in the table refers to the GRID lattice as a whole — the spacetime structure on which Maxwell and gravity are derived. This project's primitive (the cylinder) is *dimensionally agnostic*: the same primitive can be assembled into 1D chains, 2D sheets, or 3D lattices, with only the connection topology of the nodes changing. The 1D chain is an intuition aid; the 2D sheet is what MaSt-style compact dimensions wrap into; the 3D lattice is what the spatial extent S is built from. Ground rule 7 commits the project to working in 2D periodic configurations as the minimum sufficient setting; lower dimensions are toys, and 3D is a natural extension once 2D is established.

The project's job is not to derive the GRID inputs. Its job is to show how a primitive substrate (the cylinder) is consistent with them and supplies their inputs at a more granular level, in whichever dimensionality the assembled lattice requires.

---

## 10. Explicit non-assumptions

To prevent confusion later, things this chapter does *not* assume:

- **No assumption that the cylinder is a real carbon nanotube.** The cylinder is a pictorial primitive; the stiffness-matrix entries are symbolic, not derived from atomic-scale physics. The dialog's nanotube analogy is for intuition, not quantitative use.
- **No assumption that the cylinder wall has internal structure.** The "wrapped microgrid" recursion mentioned in [README.md](README.md) is acknowledged but not pursued. The cylinder is the bottom of this description.
- **No assumption that nodes have hidden state.** Nodes are exactly continuity boundaries — nothing more.
- **No assumption that *e* and *φ* are independent in their dynamics.** They are independent *fields* (independent state at any instant), but their *evolution* is coupled by *K_eφ*. The independence is at the level of state; the coupling is at the level of dynamics.
- **No commitment to a numerical value of χ̃.** Equipartition arguments and lattice-speed constraints will be examined in later chapters; neither pins χ̃ at the foundation level.
- **No assumption that the entropy account works.** That the bounded *φ* (or one of the structures listed in §4) supplies sufficient entropy for Jacobson's argument is a downstream hypothesis, not a foundation-level commitment.

---

## 11. Summary of givens

The full setup, in one place:

- A 2D cylindrical primitive of length *L* and cross-section radius *r*, deemed continuous along its length.
- A 2D internal stress vector at each cross-section, parameterized in polar coordinates as magnitude *e(x, t)* ∈ ℝ and azimuthal direction *φ(x, t)* ∈ ℝ (mod 2π), with *x* ∈ [0, *L*]. The underlying vector is in ℝ² ≅ ℂ; the polar parameterization has a coordinate singularity at *e* = 0 that is not a feature of the underlying field.
- A symmetric stiffness matrix *M* with entries *K_ee* > 0, *K_φφ* > 0, and off-diagonal *K_eφ* satisfying K_eφ² < K_ee · K_φφ.
- A dimensionless shear ratio χ̃ = K_eφ / √(K_ee · K_φφ) ∈ (0, 1).
- Nodes that impose continuity of the stress vector at endpoints of meeting cylinders, with no state and no update rule.
- Transit time τ = *L*/*c* across a cylinder, with *c* the lattice signal speed inherited from GRID axiom A1.
- Three latent entropy structures available on the primitive (§4) — vortex defects in the 2D stress field, longitudinal winding sectors of *φ*, and longitudinal Fourier modes — of which at least one is hoped to source entropy in chapter 4.

The next chapter takes this setup and derives the dynamics — the equations of motion for *e(x, t)* and *φ(x, t)*, the dispersion relation, the propagating modes, and the bidirectional propagation symmetry that the lattice signal speed requires.
