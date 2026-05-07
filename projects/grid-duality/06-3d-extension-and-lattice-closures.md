# Chapter 6: 3D extension and lattice closures

## §1. The chapter's job

Chapter 4 selected Scattering as the lattice's dynamics on a 2D hex graph. The model uses a per-vertex matrix S = (2/N)·J − I during the inhale, followed by an exhale that swaps the two register values on each edge. Neither operation references position, edge direction, or the embedding space — they reference only the local register vector at each vertex (one entry per incident edge) and which two registers belong to each edge.

This chapter shows that all chapter-4 properties (energy conservation, matched-impedance scattering, stable propagation) carry over to higher-dimensional lattices and to any coordination N. The argument is mathematical, not empirical: unitarity and the matched-impedance coefficients are algebraic consequences of S's structure, independent of the lattice the registers live on. The chapter then defines four lattice closures — open chain, ring, plaquette, torus — that anchor the wrap-promotion ladder used in chapter 7.

The chapter is mathematical end to end. The key claims admit airtight algebraic proofs; no simulation is required.

## §2. The dimension-agnostic core of Scattering

The Scattering update has two ingredients:

1. **The vertex S-matrix** S = (2/N)·J − I, where J is the N×N all-ones matrix and I is the identity. N is the local coordination at the vertex.
2. **The edge swap**, which exchanges the two register values on each edge.

Neither operation references the lattice's spatial embedding. Both are operations on the abstract graph of nodes and edges.

### §2.1 S is involutory and orthogonal

Compute S · S directly. Note J² = N · J (J is rank 1 with rows summing to N):

<!-- S·S = ((2/N)·J − I)² = (4/N²)·J² − (4/N)·J + I = (4/N)·J − (4/N)·J + I = I -->
$$
S \cdot S \;=\; \left(\tfrac{2}{N}J - I\right)^2 \;=\; \tfrac{4}{N^2} J^2 - \tfrac{4}{N} J + I \;=\; \tfrac{4}{N} J - \tfrac{4}{N} J + I \;=\; I.
$$

So S² = I. Since J and I are symmetric, S is symmetric, and S² = I implies SᵀS = SS = I. So S is orthogonal — its action preserves the Euclidean norm of any register vector r:

<!-- ||S·r||² = (S·r)ᵀ(S·r) = rᵀ·Sᵀ·S·r = rᵀ·r = ||r||². -->
$$
\|S r\|^2 \;=\; (S r)^\top (S r) \;=\; r^\top S^\top S \, r \;=\; r^\top r \;=\; \|r\|^2.
$$

Energy is conserved exactly per inhale, at every vertex, at any coordination N. This holds for any N ≥ 1; the algebra does not depend on dimension or lattice geometry.

### §2.2 Matched-impedance coefficients at any N

Reading S = (2/N)·J − I element by element:

- Diagonal: (2/N) − 1 = (2 − N)/N. This is the **reflection coefficient** R for an inbound register on a single port.
- Off-diagonal: 2/N. This is the **transmission coefficient** T to each of the N − 1 other ports.

Energy partition for an inbound wave of unit amplitude:

<!-- R² + (N−1)·T² = ((2−N)/N)² + (N−1)·(2/N)² = ((2−N)² + 4(N−1)) / N² = (N² − 4N + 4 + 4N − 4) / N² = N²/N² = 1 -->
$$
R^2 + (N-1)\,T^2 \;=\; \frac{(2-N)^2 + 4(N-1)}{N^2} \;=\; \frac{N^2}{N^2} \;=\; 1.
$$

Energy is conserved exactly per scattering event at any N. The 2D hex result (N = 3: R = −1/3, T = +2/3, energy fractions 1/9 and 4/9 each) is a special case of this general identity. In 3D diamond (N = 4): R = −1/2, T = +1/2, energy fractions 1/4 and 1/4 each. Cubic (N = 6): R = −2/3, T = +1/3, energy fractions 4/9 and 1/9 each. FCC (N = 12): R = −5/6, T = +1/6, energy fractions 25/36 and 1/36 each. Every case satisfies energy conservation by the identity above.

### §2.3 The exhale is a relabeling

Per cycle, after the per-vertex inhale, each edge's two registers swap. A swap is a permutation operation; it preserves the energy norm trivially. Like the inhale, it depends only on which two registers belong to each edge — not on edge direction, position, or dimension.

### §2.4 Conclusion

The full clock cycle (inhale + exhale) is unitary on any lattice graph at any coordination in any dimension. Energy is conserved exactly per step. Matched-impedance scattering at every junction follows from the algebraic structure of S. The chapter-4 verdict generalizes to higher-dimensional lattices without modification.

What *does* depend on dimension and lattice: the dispersion relation v_g(k) (depends on the geometric arrangement of edges), and the topological structure of closures (depends on the lattice's connectivity). These are addressed in §3–§7.

### §2.5 How to think about a junction tick

The algebra above proves S = (2/N)·J − I has the right properties. The intuition for *why* the formula is what it is — and how each part contributes — is worth stating directly, since the rest of the project leans on this picture.

A node's inhale is a three-step ritual:

1. *I gather all my register values as inputs.* I have N registers, one per incident edge; each holds whatever value the previous exhale just delivered to me from the far end of that edge.
2. *I compute the junction potential* V = 2 × (the average of my inputs) = (2/N) · Σ inputs. This is the single shared value that all my edges agree the local junction must be at, by **potential continuity** — the substrate-level statement that all incident lines meeting at a junction see the same value there. (At the higher emergent level of electromagnetism this becomes voltage continuity; at the substrate level we have not yet committed to charge or current density, so "potential" is the more accurate word.)
3. *I write back, register by register,* output_i = V − input_i. The output equals the shared junction potential minus what *that register itself* contributed.

The two terms of S correspond to the two parts of step 3, and they do different physical jobs.

The (2/N)·J part is the **share** — every register receives the same junction potential V. If S were *only* this term, every register's new value would equal V on every step. After the exhale swap, every cell would hold the local junction potential of its neighbor, and the dynamics would become *averaging your neighborhood* — i.e., the discrete heat equation. Information would spread symmetrically out from any source, with no propagation direction, no wavefronts, and gradual energy loss (the share-only operator is rank 1, not invertible).

The −I part is the **subtract-your-own** correction, and it is the entire reason waves propagate instead of diffusing. By subtracting input_i from output_i, the rule guarantees that a value coming *in* through register i is not sent *back out* through register i — it is actively cancelled. That value's energy flows out the other N−1 registers, with each one carrying T = 2/N of it; the small reflection R = (2−N)/N back through register i is what's left after the cancellation. The asymmetry between input direction and output direction is the directional structure of a wavefront. Drop the −I term, and the wavefront flattens into a diffusion blob. Keep it, and the wavefront keeps moving.

These two roles are really two views of the same property. The −I term simultaneously enables directional propagation (the physical reading) and makes the update orthogonal — S² = I (the mathematical reading). Light propagates *because* the rule is unitary, and the rule is unitary *because* it cancels each input through its own port. The (2/N)·J part on its own is junction physics; the −I part is what turns junction physics into a wave equation.

This three-step picture — gather, compute V, write back V − input — is the entire local action of a node, on any lattice, at any coordination. The rest of the project's modeling (closures, wrap-promotion, mass and charge observables) reasons about what happens when many such junctions are wired together into specific topologies. Knowing what one junction does is enough to follow the rest.

## §3. Choosing a 3D lattice

The substrate framework allows any graph, but for explicit 3D wrap-promotion-ladder analysis a specific 3D lattice is needed. The crystallographic candidates with regular coordination:

| Lattice | Coord N | S-matrix | R | T per branch | Sublattice structure |
|---|---|---|---|---|---|
| Diamond | 4 | (1/2)·J − I | −1/2 | +1/2 | bipartite (A, B) |
| Simple cubic | 6 | (1/3)·J − I | −2/3 | +1/3 | none (single sublattice) |
| BCC | 8 | (1/4)·J − I | −3/4 | +1/4 | bipartite (A at corners, B at body) |
| FCC | 12 | (1/6)·J − I | −5/6 | +1/6 | none |

All are valid carriers of Scattering as a dynamics — unitarity holds at every N. The choice matters for how cleanly the substrate's structure carries forward from 2D.

The 2D hex lattice has two key features that propagate cleanly to higher dimensions: (i) it is *bipartite* (two sublattices A and B), and (ii) it is *vertex-transitive* (all vertices look the same locally). The 3D analog with both properties is the **diamond** lattice — each A-vertex has 4 B-neighbors at the tetrahedral angles, and vice versa. This is the structure of carbon's sp³ bonding (and of silicon's crystal lattice). Subsequent sections work on diamond.

The other 3D lattices remain available — Scattering's machinery applies to each — but diamond is the natural inheritance from 2D hex. Choosing diamond is a design decision, not a forced one.

## §4. The 3D diamond lattice

Diamond consists of two interpenetrating FCC sublattices, A and B. Each A-vertex has 4 B-neighbors at the four tetrahedral directions:

<!-- n̂_1 = (+1, +1, +1)/√3, n̂_2 = (+1, −1, −1)/√3, n̂_3 = (−1, +1, −1)/√3, n̂_4 = (−1, −1, +1)/√3 -->
$$
\hat{n}_1 = \tfrac{1}{\sqrt{3}}(+1, +1, +1), \quad
\hat{n}_2 = \tfrac{1}{\sqrt{3}}(+1, -1, -1), \quad
\hat{n}_3 = \tfrac{1}{\sqrt{3}}(-1, +1, -1), \quad
\hat{n}_4 = \tfrac{1}{\sqrt{3}}(-1, -1, +1).
$$

These vectors form a tetrahedron centered at the origin; their pairwise dot products are all −1/3 (the tetrahedral angle, ≈ 109.5°). Each B-vertex has 4 A-neighbors at the negated directions: −n̂₁, …, −n̂₄.

By the bipartite convention from chapter 1 §3, all edges point A → B, so each edge's polarity is fixed by which sublattice its endpoints belong to. (Polarity is a labeling convention only — Scattering's dynamics does not read it; the registers at the two ends of an edge are unordered. This is the same situation as in 2D hex.)

Periodic boundary conditions identify a finite (n_x, n_y, n_z) slab of cells into a 3-torus T³, the natural 3D analog of the 2D hex torus.

## §5. Scattering on diamond

At every vertex (A or B), four registers are present (one per incident edge). The inhale applies S = (1/2)·J − I to the register vector; by the general result of §2:

- R = −1/2 (reflection from any one port).
- T = +1/2 (transmission to each of the other 3 ports).
- Energy: R² + 3·T² = 1/4 + 3·(1/4) = 1, conserved exactly per inhale.

Per cycle, the inhale runs at every A-vertex and every B-vertex; then each edge swaps its two registers. Both phases preserve the energy norm; the full cycle is unitary, identically to the 2D hex case.

This establishes the structural part of the chapter's claim: **Scattering on 3D diamond is well-defined, energy-conserving, and matched-impedance at every junction**, as a direct algebraic consequence of S = (1/2)·J − I and the unitarity argument of §2.

## §6. Dispersion on diamond

The dispersion relation ω(k) and group velocity v_g(k) on a periodic lattice are determined by Fourier-diagonalizing the update operator over one Bravais cell. For diamond, the Bravais cell contains 2 vertices (one A, one B) and 4 edges, giving an 8-register basis at each k. The full band structure is well-known in solid-state physics (the same band structure that determines silicon's electronic dispersion at low energies, with the wave equation replacing the Schrödinger equation).

The chapter does not derive the full band structure. The qualitative facts that matter for chapter 7's modeling are short and provable without solving the eigenvalue problem:

### §6.1 Maximum group velocity is 1 lattice unit per tick

By construction, each exhale moves a register one edge length. This sets the lattice's **speed of light** c = 1 edge per tick. Any wavepacket's group velocity must satisfy v_g ≤ c, since information cannot move faster than the exhale-step:

<!-- v_g(k) ≤ c = 1 (lattice unit per clock tick) -->
$$
v_g(k) \;\le\; c \;=\; 1.
$$

This generalizes the 2D hex bound (where v_g(k) ≤ 1 was confirmed empirically) to 3D as a structural property: it cannot be otherwise.

### §6.2 Mild anisotropy along symmetry directions

A wavepacket propagating along an edge direction (e.g., n̂₁ = (1, 1, 1)/√3) moves at v_g = 1 along that direction — one register per tick along the edge.

A wavepacket propagating along a non-edge direction (e.g., (1, 0, 0)) projects onto the edge directions with cosines |cos θ| = 1/√3 ≈ 0.577. The effective group velocity along (1, 0, 0) is bounded by this projection:

<!-- v_g((1,0,0)) ≤ 1/√3 ≈ 0.577 -->
$$
v_g\bigl((1,0,0)\bigr) \;\le\; \tfrac{1}{\sqrt{3}} \;\approx\; 0.577.
$$

The anisotropy ratio between fastest and slowest directions on diamond is therefore at most √3 ≈ 1.73. The 2D hex test L1b measured an anisotropy ratio of about 1.4 across coord-3 directions; diamond's coord-4 with tetrahedral symmetry gives a comparable but slightly larger range.

### §6.3 Dispersion is bounded but not flat

At each k, ω(k) is determined by the band structure. The mild dispersion observed in 2D coord-3 (test L1b) generalizes — it is the same structural feature: junction scattering at coord N introduces frequency-dependent phase shifts of order 1/N, integrating to a small group-velocity dispersion across k. Quantitative numbers per direction can be extracted by Fourier analysis or simulation if a specific dispersion claim is needed in chapter 7; the structural fact for chapter 6 is that dispersion is bounded and v_g ∈ [1/√3, 1] across symmetry directions.

## §7. Lattice closures

The wrap-promotion ladder L0 → L1 → L2 → L3 corresponds to specific topological structures on the lattice. Each is a *closure* — a finite, periodic identification — of a portion of the lattice graph. The closures are listed in increasing topological complexity:

### §7.1 L0 — Open chain

The simplest substrate: a 1D chain of n nodes connected by n − 1 edges, no periodic identification. Topology: a connected interval, π₁ = 0 (simply connected, no winding).

Each interior node has coord 2; each end node has coord 1. The S-matrix at coord 2 is (2/2)·J − I = J − I, which on a 2×2 all-ones J is

<!-- S_{coord 2} = J − I = [[0,1],[1,0]] -->
$$
S_{N=2} \;=\; J - I \;=\; \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$

— the swap matrix. So at every interior node, "scattering" is just a swap of the two registers, and the cycle (inhale + exhale) propagates the wave by one site. A wavepacket on an open chain moves at v_g = 1 without dispersion.

At the chain's ends (coord 1), S = (2/1)·J − I = 1 (the 1×1 identity), and the exhale swaps the boundary register with the adjacent interior register. The result is **reflecting boundary conditions** — a wavepacket reaching an end is reflected back. Energy is conserved at the boundaries by S's identity action and the swap's permutation.

The open chain is the L0 substrate of the wrap-promotion ladder: information flows but does not topologically loop.

### §7.2 L1 — Ring

A 1D ring of n nodes with periodic identification: edge n connects node n − 1 to node 0. Topology: S¹, π₁ = ℤ (one winding direction).

Every node has coord 2; the S-matrix is the swap matrix everywhere; the cycle propagates wavepackets by one site per tick. A right-moving wavepacket circulates indefinitely — there is no boundary to reflect off.

The ring's persistent modes have wavevectors quantized by the periodicity:

<!-- k_m = 2π m / n,   m ∈ {0, 1, …, n−1} -->
$$
k_m = \frac{2\pi m}{n}, \qquad m \in \{0, 1, \ldots, n-1\}.
$$

These are the standing-wave eigenmodes of the ring. The integer **winding number** w of a wavepacket counts how many times its phase circumnavigates the ring per cycle:

<!-- w = ∮ (dk / 2π) = k · n / (2π) -->
$$
w \;=\; \oint \frac{dk}{2\pi} \;=\; \frac{k \cdot n}{2\pi}.
$$

Under unitary evolution, w is conserved exactly. This is the simplest topological invariant the lattice supports, and it sits at the L1 rung of the ladder.

### §7.3 L2 — Plaquette

A plaquette is the smallest closed loop in a 2D or 3D lattice graph. In 2D hex, the plaquette is a hexagon: six A and six B vertices alternating around a six-cycle, joined by twelve edges (two between each adjacent A–B pair, by the bipartite orientation). On 3D diamond, the smallest cycle is also a six-membered ring (the chair conformation of cyclohexane sp³ carbons), with three A and three B vertices alternating.

Topology: a single plaquette is a 1D loop (S¹) embedded in 2D or 3D, so its π₁ is again ℤ — same as the ring's. What's new at L2 is the *embedding*: the plaquette has a definite orientation in the embedding space and bounds a 2D region. The geometric object is no longer the loop alone but the loop-plus-its-bounded-region.

The new physics this enables: **plaquette flux**. A wavepacket circulating once around a plaquette accumulates a phase determined by the plaquette's geometry and the wave's wavevector. Under Scattering, this phase is computable from the unitary update; it is the discrete analog of the line integral ∮ A·dl in continuum gauge theory. Plaquette-flux is the foundational topological observable in lattice gauge theory and will be the chapter-7 modeling's natural carrier of mass-like and charge-like phenomena.

### §7.4 L3 — 2-sheet wrap / torus

A torus T² is a 2D sheet with both directions periodically identified. On the 2D hex lattice, this is exactly what `make_2d_hex_torus(n_x, n_y)` produces: an (n_x × n_y) cell region with both lattice-vector directions identified. On 3D diamond, an analogous 2-sheet wrap takes a 2D layer of the diamond lattice (e.g., a (111) plane) and identifies both periodic directions.

Topology: T², π₁ = ℤ² (two independent winding numbers, one per periodic direction). Two homotopy generators: a loop wrapping once around the first periodic direction, and a loop wrapping once around the second.

Persistent modes on a torus are quantized by both periodicities:

<!-- k_{m_x, m_y} = (2π m_x / n_x,  2π m_y / n_y),  (m_x, m_y) ∈ ℤ² -->
$$
\mathbf{k}_{m_x, m_y} \;=\; \left(\frac{2\pi m_x}{n_x}, \; \frac{2\pi m_y}{n_y}\right), \qquad (m_x, m_y) \in \mathbb{Z}^2.
$$

A wavepacket localized on the torus may have nontrivial winding in either or both directions; the winding pair (w_x, w_y) ∈ ℤ² is conserved exactly under the unitary dynamics. Two independent topological invariants live on the L3 closure.

This double winding is what lifts the topology from "ring-plus-area" (L2) to "two-direction wrap" (L3), and is what chapter 7's modeling of charge will identify as the discrete substrate of charge quantization.

### §7.5 The increasing-complexity ladder

The four closures form an increasing sequence:

| | embedding dim | π₁ rank | new topological feature |
|---|---|---|---|
| L0: open chain | 1 | 0 | none — bare propagation |
| L1: ring | 1 | 1 | one winding number, w ∈ ℤ |
| L2: plaquette | ≥ 2 | 1 | bounded region → plaquette flux |
| L3: 2-sheet wrap | 2 | 2 | two independent windings, (w_x, w_y) ∈ ℤ² |

L0 → L1 closes the chain into a loop, introducing the first winding number. L1 → L2 increases the embedding dimension without changing π₁, introducing the bounded-region flux as a new observable. L2 → L3 adds a second wrap, doubling π₁'s rank from 1 to 2.

Three ingredients accumulate: winding (at L1), flux (at L2), and second winding (at L3). Chapter 7 uses these as the structural carriers of light, mass, and charge.

## §8. Closing pointer

Scattering generalizes from 2D hex to higher-dimensional lattices and to any coordination by the algebraic properties of S = (2/N)·J − I and the structure of the inhale/exhale clock. On 3D diamond, R = −1/2 and T = +1/2 per branch, with energy conserved exactly per step. The maximum group velocity is 1 lattice unit per tick, with bounded dispersion across symmetry directions.

The four lattice closures (open chain, ring, plaquette, torus) form a topological ladder of increasing complexity, accumulating winding, flux, and second-winding as the closure is promoted. This is the structural ladder chapter 7 maps to physical phenomena.

The chapter sequence is summarized in the project [README](README.md).
