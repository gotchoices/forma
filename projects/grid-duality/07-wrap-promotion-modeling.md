# Chapter 7: Wrap-promotion modeling — working outline

> **Status: working outline.** The chapter below is the section-by-section sketch produced during chapter-7 planning. It will be expanded into a full chapter once the working questions in §0 are settled and §2's three-pronged periodicity argument is fully developed.

## §0. Working questions

These are issues the chapter has identified but not yet resolved. Each will be addressed in the listed section once the chapter is written out.

### W1. Does L0 → L1 require periodicity?

The upper promotions clearly require periodicity by construction (rings, plaquettes, tori are inherently closed). The L0 → L1 transition (information → light) seems different — light is the extension of the substrate's local dynamics across space, and that extension can in principle work on an open or infinite lattice. But three independent self-consistency arguments (boundary effects, dispersion structure, finite information content) suggest periodicity is the natural shape even at L1. The chapter's honest answer in §2 is "structurally preferred, not strictly required" — but the alternatives have substantive costs.

A reading that may sharpen this: *there is nothing to wrap until information becomes light.* L0 is local dynamics on cells; nothing to extend, nothing to close. The act of extending the substrate across space *is* the L0 → L1 transition. For the extended substrate to be self-consistent, it must close upon itself — but this closure happens *as part of* the promotion, not before or after it. The wrap might live *between* levels rather than *on* them.

### W2. Do wraps live between levels or on them?

The current framing puts each closure (open chain, ring, plaquette, torus) *as* a level. An alternative framing: closures are operations that move you *between* levels. The ladder reads:

> L0 → [wrap: extend & close substrate] → L1 → [wrap: take 1D slice, embed in 2D & bound] → L2 → [wrap: close the second direction] → L3

Each wrap is the transformation, each level is the phenomenon resulting from the transformation. This is a noun/verb distinction: the wrap is the verb, the level is the noun. Worth deciding which framing the chapter commits to.

### W3. Is there a promotion higher than L3?

Following the wrap-promotion pattern, a 3-torus T³ = S¹ × S¹ × S¹ would be L4: three independent winding directions, π₁ = ℤ³. If 2-tori (L3) carry mass and charge, what would 3-tori carry as a third conserved quantity?

Speculative possibilities to consider in the chapter:

- A third gauge-like U(1) charge not yet identified at observable scales.
- Spin as a topological invariant on the third wrap direction.
- Generation number (e/μ/τ) as discrete topology of the third wrap.
- A cosmologically relevant invariant — if the universe is itself a 3-torus, the third winding might be an observable that lives at cosmic scale rather than particle scale.

This connects to the cosmological reading of W1: if the substrate must wrap for self-consistency, and the universe is the substrate at the largest scale, then the universe's apparent flatness is a local-tangent-space approximation of a globally compact 3-manifold. The simplest such manifold is the 3-torus. If that's right, L4 is a real rung — not a thought experiment but the actual cosmological scale.

The chapter's honest scope: note the L4 extension as a structural possibility, identify the candidates for the third invariant, and defer detailed development to a later project. Forcing a specific identification would be over-reach given current knowledge.

---

## §1. The chapter's job

Map each lattice closure (L0 → L1 → L2 → L3, with possible L4 extension) to a physical phenomenon (substrate, light, mass, charge, ?). For each rung, identify the mathematical observable on Scattering's dynamics that carries the phenomenon. Address the working questions of §0 as they bear on each rung.

## §2. The role of periodicity in the ladder

Three structural arguments to test, each independently real but none a hard theorem:

### §2.1 Boundary effects on open lattices

On an open lattice, boundary nodes have coord < N (the bulk coordination), so the S-matrix at the boundary differs from the bulk. Chapter 6 §7.1 showed: open chains have reflecting boundaries because S degenerates to identity at coord 1. Wavepackets reflect at the boundary; energy doesn't propagate freely off to infinity. The lattice has structurally distinguished "edge" cells that don't share the bulk dynamics.

### §2.2 Dispersion and Brillouin structure

The standard dispersion relation ω(k) is defined by Fourier-diagonalising the update operator. This requires translation invariance — which holds on a periodic lattice (giving a discrete set of k-modes) or on an idealized infinite lattice (a continuous Brillouin zone). On an open lattice with reflecting boundaries, modes are sin/cos standing waves rather than plane waves, and the standard dispersion machinery does not apply. Light's *familiar* mathematical description requires periodicity (or an unphysical idealization).

### §2.3 Bekenstein bound and finite information content

Chapter 5 established that the substrate's information capacity is M ≥ (amp_max/((N−1)ε))² cells per macroscopic window for any target precision ε. This presupposes a finite cell count. An infinite lattice has infinite information, which doesn't sit cleanly with the holographic-bound finiteness. A periodic finite lattice is the natural carrier of finite information.

### §2.4 Synthesis: structurally preferred, not strictly required

Each argument *individually* prefers a periodic substrate over an open or infinite one. Together they do not constitute a hard theorem that periodicity is required, but they do shift the burden of proof: an open or infinite substrate has to *justify* its choice against three independent self-consistency concerns. Periodicity is the natural shape.

The "nothing to wrap until information becomes light" reading from §0 W1 fits here: if the wrap lives at the L0 → L1 transition rather than as a property of L0 itself, then the periodicity question is *not* "is L0 periodic?" but "is the substrate's extension into space periodic?" — and the answer to that is yes, by all three arguments above.

### §2.5 The cosmological consequence

If the substrate's natural shape is compact-with-wraps, the universe at the largest scale is plausibly a 3-torus or some compact 3-manifold, with the apparent flatness at observational scales being the local-tangent-space approximation. The chapter does not commit to a specific cosmological topology, but it notes the convergence: substrate self-consistency, holographic finiteness, and the wrap-promotion ladder all want compactness at the largest scale.

This connects directly to W3 in §0: the 3-torus reading of the universe's shape *is* the L4 rung of the ladder, taken seriously.

## §3. L0 → L1: light as bulk wave propagation

Light is what Scattering does on the bulk lattice. Mathematical observables: dispersion relation ω(k), group velocity v_g(k). Conservation laws: energy (per chapter-2 unitarity) and crystal momentum k (per translation invariance, requires periodicity).

The lattice's "speed of light" is one edge per exhale, set by the clock — a structural property, not a parameter. Bands are bounded; v_g(k) ≤ 1.

What changes between L0 (substrate baseline) and L1 (any periodic identification): on L0 there are boundary problems (per §2); on L1 the dispersion is clean. The promotion is essentially "close the substrate." Light *exists* on L0 in the sense that bulk wave propagation works; it *behaves like classical light* on L1 because that's where the math is well-defined.

## §4. L1 → L2: mass as a circulating standing wave

A ring (L1) supports persistent circulating wavepackets. Standing-wave modes are quantized: k_m = 2πm/n on a ring of n cells. Each mode has a definite frequency ω(k_m) and an effective mass given by the dispersion curvature:

> m_eff ∝ 1 / (d²ω/dk²) |_{k = k_m}

This is the "rest mass" of an excitation that *cannot* propagate away — the ring's topology traps it. The promotion to L2 (plaquette) adds spatial embedding: the ring acquires a bounded 2D region, and *plaquette flux* (the phase accumulated per circumnavigation) becomes a new observable. Mass at L2 is localized energy plus a flux signature — closer to charged particles than to free standing waves.

A working question: is the L2 plaquette flux already a "proto-charge," or does charge specifically require the second winding direction at L3? Answered in §5.

## §5. L2 → L3: charge as topological winding

A torus (L3) has two independent π₁ generators, so a wavepacket has two independent winding numbers (w_x, w_y) ∈ ℤ². These are conserved exactly under unitary dynamics — they cannot continuously deform to zero. Charge quantization in this picture is the discreteness of the winding spectrum: charge is integer-valued because winding numbers are integer-valued.

The two windings give a U(1) × U(1) structure on the torus, the natural setting for electric–magnetic duality. Whether this exhausts charge or only its topological skeleton is an open question for chapter 8 (where α is mapped onto the L3 structure).

## §6. L3 → L4: a third winding direction (speculative)

If the substrate is itself a 3-torus, π₁ = ℤ³ — three independent winding directions. The third winding number would be a third conserved invariant beyond mass and charge.

Candidates:

- *A third gauge-like U(1) charge* not yet identified at observable scales.
- *Spin* as a topological invariant — possibly tied to a third winding direction that is intrinsic rather than spatial.
- *Generation number* — the discrete (e, μ, τ) family structure as a third winding.
- *A cosmologically scaled invariant* observable only at the largest scales — connected to the cosmic-3-torus reading of §2.5.

The chapter does not commit to a specific identification. It notes L4 as the structural extension implied by the wrap-promotion pattern and identifies the candidates worth investigating.

## §7. The phenomena ladder

Summary table (provisional — to be filled in once the chapter develops fully):

| Rung | Closure | New observable | Conservation | Phenomenon |
|---|---|---|---|---|
| L0 | bulk substrate | local update | energy per inhale | substrate / information |
| L1 | ring or any periodic | dispersion ω(k) | energy + crystal momentum | light |
| L2 | plaquette in 2D | + plaquette flux | + flux | mass |
| L3 | 2-torus | (w_x, w_y) ∈ ℤ² | + winding pair | charge |
| L4 | 3-torus (speculative) | (w_x, w_y, w_z) ∈ ℤ³ | + third winding | ? (see §6) |

Each rung adds one new conserved observable. The promotion is the appearance of that new observable as the closure topology becomes nontrivial in a new direction.

## §8. Closing pointer

Pointer to chapter 8 where α is mapped onto the L3 winding structure. The L4 thread is left open; further work on it would be a separate project.

---

## Appendix A: Notes for full chapter writing

- The §2 three-pronged argument is the chapter's structural backbone — it justifies why periodicity matters. It needs full development with examples and concrete counterfactuals.
- The §3–§5 modeling sections need explicit Fourier-decomposition / band-structure / winding-number derivations (math-heavy, no simulation needed if the chapter-6 §2 generalization is invoked).
- §6 (L4 speculation) needs to be honest about its scope — it's a thought experiment that the wrap-promotion pattern *suggests*, not a derived consequence.
- The "wraps between levels" framing (W2) should probably be the working framework throughout, even if it's not formally argued for. It reads cleaner than "wraps as levels," and it absorbs the L0 → L1 question naturally.
- Chapter 8 will need the L3 winding-pair structure to be sharply defined here. Particularly: how (w_x, w_y) on a torus relates to U(1) gauge structure, and what continuum limit recovers Maxwell's electromagnetism.
