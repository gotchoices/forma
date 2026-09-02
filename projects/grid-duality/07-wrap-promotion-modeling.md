# Chapter 7: Wrap-promotion modeling

## §1. The chapter's job

Each of the four lattice closures from chapter 6 (open chain, ring, plaquette, torus) is associated with a physical phenomenon (substrate, light, mass, charge). This chapter does the mathematical modeling: for each closure, identify the observable on Scattering's dynamics that carries the phenomenon, and show how the phenomenon emerges from the closure's topology.

The framing throughout is that **wraps live between levels, not on them**. Each level is a phenomenon (a noun); each wrap is a transformation (a verb) that produces the next phenomenon by changing the substrate's topology in a definite way. The ladder reads:

> L0 (substrate / information) → [wrap 1: extend & close] → L1 (light) → [wrap 2: bound 1D loop in 2D] → L2 (mass) → [wrap 3: close the second direction] → L3 (charge) → [wrap 4: close the third direction] → L4 (speculative).

This noun/verb separation is what lets the L0 → L1 transition introduce periodicity without requiring it of L0 itself. Periodicity is what wrap 1 does, not a property of the substrate sitting still. §2 develops this carefully, since whether the L0 → L1 wrap is forced or merely natural is a non-trivial question.

The chapter is mathematical end to end. Each phenomenon's modeling reduces to standard solid-state / lattice physics constructions (band structure, Bloch waves, effective mass, topological winding), now applied to the specific Scattering substrate of chapters 4–6. The Bloch / band-structure language is developed from scratch in [primers/bloch-band-structure.md](../../primers/bloch-band-structure.md); readers unfamiliar with these terms may want to skim that primer before §3 onward, since this chapter applies the primer's machinery rather than re-deriving it.

## §2. The role of periodicity in the ladder

The upper closures (ring, plaquette, torus) are inherently periodic by construction — periodicity is the closure. The structural question is whether the lower transition L0 → L1 also requires periodicity, or whether light can be a phenomenon on an open or infinite substrate.

Three independent self-consistency arguments each push toward periodicity. None is a hard theorem on its own, but their convergence is decisive.

### §2.1 Boundary effects on open lattices

On an open lattice, boundary nodes have coord N_b smaller than the bulk coord N. The S-matrix S_b = (2/N_b)·J_b − I_b at the boundary differs from the bulk S, so boundary cells follow a different dynamics. Chapter 6 §7.1 made this concrete for the open chain: at coord 1, S = (2/1)·1 − 1 = 1 (the identity), and the exhale at the boundary swaps the boundary register with the adjacent interior register. A wavepacket reaching the boundary is reflected, not transmitted away.

The reflection is a real change in the dynamics, not a measurement artifact. To have *uniform* matched-impedance dynamics throughout the lattice — every node the same N, every junction implementing the same S — the lattice must have no boundary. On a finite lattice, "no boundary" means periodic identification.

### §2.2 Dispersion and Brillouin structure

The standard description of waves on a lattice — a *dispersion relation* ω(k) giving the angular frequency of each plane wave as a function of its wavevector, and a *band structure* listing those dispersion curves across the Brillouin zone (the fundamental domain of allowed wavevectors) — relies on a single underlying theorem. **Bloch's theorem** says that any linear, translation-invariant update on a periodic lattice has plane-wave eigenstates labelled by a wavevector **k**, with the lattice's dynamics decomposing into one independent phase rotation per **k**. The theorem is generic: it requires only linearity of the update and discrete translation invariance, both of which Scattering satisfies on a periodic substrate. A self-contained development is in [primers/bloch-band-structure.md](../../primers/bloch-band-structure.md); the rest of this chapter applies it.

What matters here is the *converse*: if translation invariance is lost, Bloch's theorem does not apply, and the dispersion-relation language goes with it. On an open finite lattice, translation invariance fails near the boundary, and the natural mode basis becomes sin/cos standing waves rather than e^{ikx} plane waves. The dispersion relation used throughout chapters 4 and 6 — and on which the group velocity v_g = dω/dk and the speed of light c = 1 lattice unit per tick depend — is well-defined only with translation invariance. Without it, the familiar mathematical description of light does not apply.

This is the strongest of the three arguments. *Light's known mathematical description requires periodicity.*

### §2.3 Bekenstein bound and finite information content

Chapter 5 established that the substrate's information capacity satisfies a holographic-window scaling: M ≥ (amp_max/((N−1)·ε))² cells per macroscopic resolution ε. This presupposes a *finite* total cell count — without it, the substrate carries infinite information, which sits poorly with the Bekenstein bound and the holographic principle.

A finite homogeneous lattice has only one natural shape: periodic. Open finite lattices have boundaries (and so are not homogeneous); infinite lattices are not finite. The intersection is "finite + homogeneous = periodic."

### §2.4 Synthesis: structurally preferred, not strictly required

Each argument *individually* prefers periodicity. Together they shift the burden of proof: an open or infinite substrate has to justify itself against three independent self-consistency concerns, while a periodic substrate is the natural shape under all three. Periodicity is *what wrap 1 does* in the noun/verb framing — it is the structural transformation that makes the substrate's extension into space self-consistent. Light then propagates cleanly on the closed substrate, with a well-defined band structure, no boundary effects, and finite information.

The noun/verb framing also resolves an apparent tension: there is nothing to wrap until information becomes light, since L0 is local-cell dynamics with no spatial extension to wrap. The wrap is *coincident with* the L0 → L1 transition, not a property of L0 sitting still. Wrap 1 is the act of extending the substrate across space *and* closing it upon itself, both at once, because the closure is what makes the extension self-consistent.

### §2.5 The cosmological reading

Substrate self-consistency, holographic finiteness, and the wrap-promotion ladder all want compactness at the largest scale. If the universe is the substrate at the largest scale, and the substrate's natural shape is compact-with-wraps, then the universe is plausibly a 3-torus or some compact 3-manifold, with the apparent flatness at observational scales being the local-tangent-space approximation of a globally wrapped space.

The chapter does not commit to a specific cosmological topology. It notes the convergence and the simplest concrete realisation. §6 returns to the cosmological reading from a different direction (the L4 third-winding question).

## §3. L0 → L1: light as bulk wave propagation

The first wrap — extend the substrate across space and close it — yields a periodic graph on which Scattering propagates as a wave. Light is what Scattering does on this closed substrate.

The substrate now satisfies the conditions for Bloch's theorem (a linear, translation-invariant update on a periodic lattice — see [primers/bloch-band-structure.md §1](../../primers/bloch-band-structure.md)), so the per-substrate analysis that follows is one application of the same machinery: write the Bloch matrix at each wavevector **k**, diagonalise to get bands ω_n(**k**), and read off the dispersion. The 1D ring (§3.1) has the simplest possible Bloch matrix — 1 × 1 — and gives a single linear band; the 2D hex case (§3.2) has a 2 × 2 Bloch matrix and gives two bands; 3D diamond (§3.3) is the same with one more dimension. The conserved quantities in §3.4 are the universal ones the theorem produces on any periodic substrate.

### §3.1 Plane-wave solutions on a ring

The simplest non-trivial closure is the 1D ring of n cells, every node coord 2, S = J − I (the swap matrix). Scattering on the ring has a closed-form solution. Take a plane-wave ansatz on the forward register:

<!-- a_fwd_j(t) = A · exp(i(kj − ωt)) -->
$$
a^{\text{fwd}}_j(t) \;=\; A \, \exp\!\bigl[\, i\,(k\,j - \omega\, t) \,\bigr].
$$

After one full cycle, the wave has propagated by one site (the inhale-then-exhale cycle on a 1D chain reduces to "register at site j moves to site j+1" for the forward channel). So a^fwd_j(t+1) = a^fwd_{j-1}(t), giving:

<!-- ω(k) = k -->
$$
\omega(k) \;=\; k \qquad \text{(modulo 2π).}
$$

The dispersion relation is *linear and dispersionless*: every wavevector k propagates at v_g = dω/dk = 1 lattice unit per tick. This is the empirical L1a result of test_1d_dispersion.py: at coord 2, every k gave v_g = 1.000.

The ring's periodicity quantises k:

<!-- k_m = 2π·m/n,  m ∈ {0, 1, ..., n−1} -->
$$
k_m \;=\; \frac{2\pi\, m}{n}, \qquad m \in \{0, 1, \ldots, n-1\}.
$$

These n discrete modes form a complete basis for any state on the ring; any Scattering evolution is a phase rotation in this basis, e^{−iω(k_m)t} = e^{−ik_m t}. Energy is conserved per mode (unitary by chapter 6 §2). Crystal momentum k is conserved per mode (no scattering between k-modes, since the dynamics is translation-invariant).

### §3.2 Bloch decomposition on 2D hex

In 2D hex (coord 3, two-atom basis A and B), the same Bloch-decomposition machinery applies. The Fourier-transformed update operator at wavevector **k** is a 2×2 matrix mixing the A-sublattice and B-sublattice register amplitudes; diagonalising it gives two bands ω_±(**k**). The maximum group velocity is bounded by 1 lattice unit per tick (from the exhale's "one edge per tick" structural property), but mild dispersion appears at coord 3 because the matrix has direction-dependent off-diagonal entries.

The 2D dispersion test (L1b) measured this empirically: v_g ≈ 0.35 ± 0.06 across k ∈ [0.2, 2.6]. The bound v_g ≤ 1 came out structurally; the *actual* v_g(**k**) curve is set by the band structure, which is mildly direction-dependent.

### §3.3 Bloch decomposition on 3D diamond

Same construction in 3D diamond: 2-atom basis (A, B), 4 edges per A vertex, gives a 2×2 matrix at each **k** and two bands ω_±(**k**). Group velocity bounded by 1 along edge directions, ≥ 1/√3 along non-edge directions (chapter 6 §6.2). The structural bound v_g ≤ 1 is the same; the band structure's specific shape is the direction-dependent piece.

### §3.4 What's conserved

Per cycle, on any periodic substrate of any dimension:

- *Energy* E = ½ Σ r² (chapter 6 §2 unitarity).
- *Crystal momentum* **k** per Bloch mode (translation invariance under periodic identifications).
- *Phase* φ within each mode (unitary phase rotation).

These are the conservation laws of light. They follow directly from Scattering's structural properties applied to a periodic substrate. Light is L1.

## §4. L1 → L2: mass as a circulating standing wave

The second wrap takes the 1D loop of L1 and embeds it in a 2D substrate, simultaneously raising the lattice's coordination from 2 to 3 (or higher) and giving the loop an *interior* — a bounded 2D region. Mass appears at L2 as a *circulating wavepacket trapped on the now-bounded loop, with effective rest mass set by the band curvature that the higher coordination unlocks*.

The next subsection makes the structural point sharp: mass is not a phenomenon that exists at L1 and merely picks up extra observables at L2. Mass is *not available at all* on a 1D substrate — it requires the higher-dimensional context that L2 introduces. The L1 → L2 wrap is the first rung where the substrate has anywhere for inertia to live.

### §4.1 Why mass needs a higher-dimensional context

A massive excitation on a lattice is a wavepacket that is *spatially localised* and *does not propagate*. From the dispersion analysis, "does not propagate" means v_g = dω/dk = 0 — the wavepacket sits at a band extremum. From the wavepacket-envelope expansion (the standard solid-state effective-mass result; see §4.2 below and [primers/bloch-band-structure.md §10](../../primers/bloch-band-structure.md)), the rest mass is finite when the band has curvature at that extremum.

Three structural facts chain together to lock this to L2:

1. **Mass requires v_g = 0 at some k_0**, i.e. an extremum of the dispersion. Without an extremum, every wavepacket has non-zero v_g and propagates; nothing localised and stationary is available.
2. **Band extrema require coord ≥ 3.** On a 1D coord-2 chain, the dispersion is *linear and dispersionless*: §3.1 derived ω(k) = k by direct calculation, with v_g = 1 everywhere and no extremum to be found. Light is structurally massless on coord-2 lattices. As soon as coord ≥ 3, the Bloch matrix at each **k** has multiple sublattices and direction-dependent off-diagonal entries, the band structure has interior extrema, and effective mass becomes finite.
3. **Coord ≥ 3 requires ≥ 2D embedding.** On a 1D substrate every interior node has exactly two neighbours (one on each side), so coord = 2 is forced. To raise coord to 3 or more, the substrate must branch out of 1D into at least 2D. Hex gives coord 3, diamond gives coord 4.

Linking the three: mass → extremum → coord ≥ 3 → ≥ 2D substrate. L1's coord-2 ring has no extrema and therefore hosts no mass; the L1 → L2 wrap raises the coord while bounding the loop in the new dimension, and *both* effects are required for mass to manifest. Mass is not an L1 phenomenon awaiting an L2 dressing; it is a phenomenon that *first becomes available* at L2.

The two observables L2 brings are then both consequences of the same dimensional extension: the rest-mass observable m_eff comes from the band curvature that coord ≥ 3 unlocks, and the plaquette flux observable φ comes from the bounded 2D region that the embedding produces. They are not two independent additions; they are two faces of the L1 → L2 wrap.

### §4.2 The mass eigenstate at a band extremum

The substrate-level picture combines two standard facts of band theory: a wavepacket centred near a band extremum **k**_0 (a point where v_g = ∇_**k** ω vanishes) does not translate, and the second derivatives of ω at that extremum set an effective mass m_eff = ℏ² / (d²ω/dk²)|_{**k**_0} for the wavepacket's response to small perturbations (see [primers/bloch-band-structure.md §10](../../primers/bloch-band-structure.md) for the derivation). A mass eigenstate is therefore a stationary wavepacket with rest energy E_0 = ℏ·ω(**k**_0), effective mass m_eff set by the band's local curvature, a spatial extent set by its envelope, and persistent existence in time under the non-interacting Scattering dynamics. Different band extrema give different m_eff. On the L1 coord-2 ring (linear dispersion, v_g = 1 everywhere, no extremum to evaluate) no such state exists; on 2D hex or 3D diamond at coord ≥ 3 the band structure has interior extrema (typically at the Brillouin-zone centre or zone edges), and mass eigenstates live there. This is the substrate-level reading of §4.1's chain of structural facts.

The *continuum-level* statement of mass — what the lattice's effective-mass parameter looks like at the metric level, viewed as a quantised standing-wave momentum on a compact dimension — is the subject of [metric-mass](../metric-mass/), which derives mass from a single compact extra coordinate via the standard Kaluza-Klein machinery. metric-mass is logically prior to this chapter: it establishes the continuum-side mass derivation that grid-duality presupposes when it identifies band-extremum eigenstates as massive. The substrate / continuum split is the natural one to keep in mind: this chapter's job is to show that the lattice produces band curvature exactly at the right rung; metric-mass's job is to say what that curvature *is* when viewed through a metric.

### §4.3 The plaquette and the bounded region

The L1 → L2 wrap is, geometrically, the embedding of the 1D loop into a higher-dimensional region. On 2D hex this means the loop bounds a hexagonal plaquette; on 3D diamond, the loop bounds a chair-conformation 6-membered ring with a 2D plane of definite orientation in 3-space.

The dimensional extension simultaneously raises the lattice coord (to 3 in hex, 4 in diamond) and gives the loop an interior. From the §4.1 chain, the coord increase is what unlocks the band-extremum mass eigenstate; the bounded interior is what produces a second observable, the *plaquette flux*:

<!-- φ = ∮(k − ω/v_g) dx -->
$$
\varphi \;=\; \oint \! \bigl(k - \omega/v_g\bigr) \, dx.
$$

For non-dispersive media (v_g constant, ω = k·v_g) this vanishes identically. For dispersive media (v_g(k) ≠ const) it can be non-zero. The plaquette flux is the discrete-lattice analog of the line integral ∮ A·dl in continuum gauge theory; it lives on the bounded region the loop encloses, which only L2 has.

Together with φ comes the *orientation* of the bounded region: the loop's normal vector picks out a specific 2D plane in 3D, or a specific orientation in 2D. The mass eigenstate at L2 carries this orientation as part of its physical identity — it is not just a scalar mass but a localised structure with a preferred direction.

Mass at L2 is therefore a wavepacket carrying:

- *Localised energy* E_0 (the rest energy).
- *Effective mass* m_eff (from band curvature unlocked at coord ≥ 3).
- *Plaquette flux* φ (geometric phase observable on the bounded region).
- *Orientation* (the normal to the bounded region).

This is structurally close to a charged-particle eigenstate in lattice gauge theory; what's missing for a full charged-particle picture is the *quantisation of φ in integer units of 2π*. That quantisation arises only at L3, when the second direction wraps.

## §5. L2 → L3: charge as topological winding

The third wrap closes the second direction. The plaquette becomes a torus T² = S¹ × S¹. Two independent π₁-generators emerge, and topological invariants of the wave dynamics now take values in ℤ² rather than ℤ. The substrate-level claim of this chapter is that *charge* — quantised, integer-valued, conserved under unitary dynamics — is the topological winding number that lives on these closed cycles, and that the L3 rung is the first rung where it becomes available.

This is presented as a structural hypothesis here. The substrate produces exactly the right object (a pair of integer-valued conserved windings on T²); the *formal continuum derivation* — taking T² as a 2D compact sheet attached to extended spacetime, applying the standard Kaluza-Klein dimensional reduction, and showing that the resulting quantities transform and couple as electromagnetic charge — is the work of [metric-charge](../metric-charge/), which picks the L3 substrate up directly from this chapter and does the metric-level construction. The substrate / continuum split in §4 (band curvature here, KK mass derivation in metric-mass) carries over to charge: the lattice's job is to produce the right topological skeleton, and the continuum project's job is to dress that skeleton in metric-level language.

### §5.1 Topology of the 2-torus

A torus has two independent first-homotopy generators α (going around the first periodic direction once) and β (around the second). Any closed loop on the torus is homotopic to a unique combination w_α α + w_β β with (w_α, w_β) ∈ ℤ². The pair (w_α, w_β) is the loop's *winding number* in the two directions.

The fundamental group π₁(T²) = ℤ² is abelian (in contrast to the higher-genus cases where π₁ is non-abelian). The torus also has two continuous translation symmetries — rotating each S¹ factor independently — which together form a U(1) × U(1) isometry group. The two facts are conceptually distinct (π₁ is a topological invariant; U(1) × U(1) is a Lie group of continuous symmetries), but on T² they share a common origin: each S¹ factor contributes one ℤ generator to π₁ *and* one U(1) factor to the isometry group. The substrate-level winding numbers (w_α, w_β) are π₁ invariants of trajectories on the torus; the U(1) × U(1) gauge structure that appears in metric-charge after Kaluza-Klein reduction is built on the isometry side. They are linked because the same two S¹ factors produce both.

### §5.2 Conservation of winding under unitary dynamics

The winding number of a *wavepacket* on a torus is the integer associated to the trajectory of its phase. As the wavepacket evolves under Scattering, this winding is preserved: there is no continuous unitary path between winding (1, 0) and (0, 0) that keeps the wavepacket localised in real space, because such a path would require the wavefront to "unwind" through a configuration that crosses itself.

Concretely, the conserved invariants are the line integrals of the wavevector:

<!-- w_α = (1/2π) ∮_α k · dx,    w_β = (1/2π) ∮_β k · dx -->
$$
w_\alpha \;=\; \frac{1}{2\pi}\oint_\alpha \mathbf{k}\cdot d\mathbf{x}, \qquad
w_\beta \;=\; \frac{1}{2\pi}\oint_\beta \mathbf{k}\cdot d\mathbf{x}.
$$

For a Bloch state with wavevector **k** = (k_x, k_y) on a torus of size (L_x, L_y), these reduce to (k_x L_x / 2π, k_y L_y / 2π), and the periodic-identification quantisation k_x = 2π m_x / L_x forces both windings to take integer values m_x, m_y.

So *w_α and w_β are integers*. They are conserved exactly under unitary Scattering. There is no continuous deformation between distinct integer pairs; transitions between charge sectors require non-unitary processes (e.g. emission of a particle with the requisite winding).

### §5.3 The U(1) × U(1) structure at the lattice level

The two independent windings classify wavepackets on the torus up to homotopy: each (w_α, w_β) ∈ ℤ² is a topological sector, and unitary dynamics cannot connect different sectors. The two ℤ factors are the lattice-level shadow of a U(1) × U(1) structure — the same U(1) × U(1) that appears as the isometry group in §5.1. Identifying this structure with the U(1) × U(1) gauge theory of electromagnetism (in the (2+1)D continuum limit, with the two factors related by Hodge duality and assigned to electric and magnetic charge) is the metric-level move; this chapter does not perform that identification, but the natural reading of the substrate is that L3 produces exactly the topological skeleton on which such a continuum gauge theory rests. The formal reduction is in [metric-charge §1](../metric-charge/01-foundation.md).

The lattice does, however, make one feature of the gauge picture geometrically transparent: the two periodic directions of the torus are *interchangeable*, so the two windings (w_α, w_β) play symmetric roles. Which one is later labelled "electric" and which "magnetic" is a convention fixed by orientation choices in the metric-level construction, not by anything intrinsic to the substrate. This symmetry is part of why the L3 substrate is structurally well-suited to host an electromagnetic-style gauge theory: the duality between electric and magnetic charge that takes work to produce in continuum is already present in the topology of the wrap.

### §5.4 Charge quantisation

The most striking consequence of the L2 → L3 wrap is *charge quantisation*: physical charge is integer-valued because winding numbers are integer-valued, with no continuous-deformation path between distinct integers. Dirac's argument for charge quantisation (the existence of a single magnetic monopole anywhere in the universe forces all electric charges to be integer multiples of a unit) finds its discrete-lattice counterpart here: charge is integer because topology is integer.

The single unit of charge — the basic quantum (1, 0) or (0, 1) — corresponds to a wavepacket that wraps exactly once around one direction. Higher integer charges (n, 0) are wavepackets with winding n in one direction, with energy and effective mass scaling appropriately with n. Bound states with mixed windings (n, m) are also allowed.

### §5.5 What's conserved at L3

Per cycle, on a 2-torus closure:

- All conservation laws of L1 (energy, crystal momentum, phase per mode).
- All conservation laws of L2 (rest mass, plaquette flux on a bounded region).
- *Topological winding* (w_α, w_β) ∈ ℤ², the two-component U(1) × U(1) charge.

Each new conservation law corresponds to a new conserved observable. The wrap-promotion ladder is, structurally, the accretion of conserved observables as the substrate's topology grows non-trivial in successive directions.

## §6. L3 → L4: a third winding direction (speculative)

The natural extension closes the third direction. A 3-torus T³ = S¹ × S¹ × S¹ has π₁ = ℤ³ — three independent winding directions. Following the wrap-promotion pattern, the L4 closure would carry a *third conserved invariant* beyond mass and charge.

This section identifies candidates without committing. The structural pattern (each wrap adds one conserved invariant) implies that L4 exists; what physical phenomenon it carries is an open question requiring data this chapter does not have.

### §6.1 Candidate observables for the third winding

- *A third gauge charge.* If the lattice supports three independent U(1) windings, the gauge group of the substrate is U(1)³ (or a non-abelian extension of it). At observable scales, electromagnetism uses one U(1); two more might correspond to forces not yet identified, or to a discrete-lattice substrate of the Standard Model's larger gauge group SU(3) × SU(2) × U(1).

- *Spin.* Spin is a topological quantum number with a 4π-periodicity that distinguishes it from rotational symmetry. A third winding direction — if the third S¹ factor is intrinsic rather than spatial — could carry the spin invariant directly.

- *Generation number.* The three observed lepton/quark generations (e/μ/τ; u/c/t; d/s/b) form a three-fold structure not explained by current Standard Model gauge group. If the third winding direction has a discrete index that takes three distinct values, it could be the lattice substrate of generation.

- *A cosmologically scaled invariant.* If the universe is itself a 3-torus (the §2.5 cosmological reading), the third winding lives at cosmic scale rather than particle scale. Its observable signature would be at the level of cosmic structure (matched-pair correlations in CMB, repeating cosmic structure).

### §6.2 Why this remains speculative

Each candidate fits the L4 slot structurally but commits to a specific physical identification that the wrap-promotion mathematics does not by itself force. The L1 → L2 → L3 ladder maps cleanly to substrate → light → mass → charge because each phenomenon was already known and the topology matches the conserved-observable structure. At L4 there is no agreed-upon "third Standard-Model phenomenon" with the right topological signature, so the candidates are placeholders for future work.

The chapter notes the L4 thread, identifies candidates, and leaves the identification open. The structural result is robust (the third wrap creates a third conserved observable); the physical identification is not.

## §7. The phenomena ladder

A summary of what each rung adds:

| Rung | Wrap producing it | Closure | New conserved observable | Phenomenon |
|---|---|---|---|---|
| L0 | — | bulk substrate (cell + dynamics) | local energy per inhale | substrate / information |
| L1 | extend & close substrate | ring or any periodic identification | dispersion ω(k); energy + crystal momentum | light |
| L2 | bound the 1D loop in 2D | plaquette in 2D or 3D | rest mass m_eff; plaquette flux φ | mass |
| L3 | close the second direction | 2-torus T² | winding pair (w_α, w_β) ∈ ℤ² | charge (U(1) × U(1)) |
| L4 | close the third direction | 3-torus T³ | third winding w_γ ∈ ℤ | speculative — see §6 |

Each row adds one new conserved observable to the row above. The wrap-promotion process is the accretion of conserved observables as the substrate's topology grows non-trivial in successive directions; the phenomena are how those observables manifest physically.

A pattern worth flagging: each level beyond L1 has a *band-structure* observable from L1 that becomes *quantised* at the level above. At L1, ω(k) is continuous in **k** (up to the periodic mode discretisation, which becomes continuous in the large-system limit). At L2, the plaquette flux φ becomes a real-valued geometric phase. At L3, the windings (w_α, w_β) become *integer-valued* — discrete by topology. The promotion from continuous to discrete invariants is what makes L3 charges quantised and L2 masses (which are still continuous-valued) distinct from L3 charges (which are integer-valued). The L4 third winding, if it exists, would also be integer-valued.

## §8. Closing pointer

The wrap-promotion ladder presented here is the structural skeleton of the substrate's phenomenology. Light, mass, and charge each arise as conserved observables on closures of increasing topological complexity. Chapter 8 takes the L3 winding-pair structure and asks where the fine-structure constant α appears — whether on the L3 rung itself or in the relationships among the rungs.

The L4 thread (§6) is left open. Resolving it requires data and identification work outside this chapter's scope.

**Dynamical confirmation (cross-reference).** The L1→L2→L3 structure this chapter derives from band topology has since been checked *dynamically* on the Scattering substrate in [grid-matter](../grid-matter/): the exact dispersion (eigenvalues of the scatter+propagate operator) gives a **massless L1 photon** and **relativistic L2 massive modes** (ω² = c²k² + ω₀²) with the KK mass tower ω₀(n) ∝ 1/R and de Broglie phase harmony, and the **L2 mass (breather) / L3 charge (winding-kink)** both fall out of the compact-*phase* potential U = m²(1−cos φ). The stability side of the ladder (a conserved winding protects a mode; unprotected modes radiate = "ephemeral") is shown by the Q-ball-vs-oscillon contrast. See [grid-matter/work/promotion-hierarchy.md](../grid-matter/work/promotion-hierarchy.md).

The chapter sequence is summarized in the project [README](README.md).
