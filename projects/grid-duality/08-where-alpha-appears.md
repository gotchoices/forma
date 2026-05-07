# Chapter 8: Where α appears — working outline

> **Status: working outline.** The chapter below is the section-by-section sketch produced during chapter-8 planning. The chapter's substantive claim is that α plausibly emerges at L3 for a structural reason parallel to mass emerging at L2 — both quantities require a particular kind of "progression space" before they have anywhere to live. The candidates for α's lattice origin are real but speculative. Resolving them likely requires lattice-gauge-theory machinery beyond what this project has built.

---

## §0. Working questions

These are the questions the chapter has identified. Each is unresolved at outline stage.

### W1. Does α appear at L3 for the same structural reason mass appears at L2?

Chapter 7 §4.1 established that mass is *not available at all* at L1 — the L1 substrate is 1D, has no band extrema, and so there is nothing for inertia to live in. Mass first becomes available at L2 because the substrate finally has the dimensional context for it.

The parallel question for α: is there a structural reason α first becomes available at L3 specifically? Candidates:

- *Cross-coupling.* α relates two physical quantities (charge and the EM field that couples to it). If charge is a topological winding (L3 first provides it), and the coupling field is a *second* topological structure that requires the second winding direction to be defined, then α — as the ratio between them — is undefined at L1, undefined at L2, first defined at L3 because L3 is where both ingredients exist simultaneously.
- *Cross-section / interaction strength.* α also has the reading "the probability that two charges interact via photon exchange." On a 1D ring there's no spatial scattering to compute a cross-section. On a 2D plaquette there's a region but no quantised charge. On a torus there's quantised charge AND a 2D region for the interaction to happen in, and the interaction strength can be computed as a ratio of topological invariants.

Both readings put α at L3 for parallel-to-mass-at-L2 reasons: the structure α requires (two-fold topology + bounded region + quantised invariant) first becomes available at the L3 rung. *Resolution at outline stage:* yes, the parallel is structurally apt, but specifying which ingredient α specifically depends on requires lattice-gauge-theory work not yet done.

### W2. Could α require even more structure — a third winding (L4)?

If α requires the cross-coupling of two U(1) factors, L3 is enough. If α requires three structures that interact pairwise (electric × magnetic × something else), then L3 has only two and L4 — the speculative third winding from chapter 7 §6 — would be needed.
<!--EC is the universe a 3-torus or a 4-torus?  i.e. time -->

Reasons to consider L4:
- *Renormalisation flow.* α(μ) runs with energy scale under the RG. The "scale" parameter μ might be the third winding's quantum number, with α(μ) being a function of where one is on the third axis.
- *Anomaly coefficients.* Some constants of nature (CKM angles, mass ratios) appear as ratios involving multiple gauge-group representations. If α is similarly a ratio of structures across multiple windings, three windings might be needed.
- *Cosmological selection.* If the universe is a 3-torus, the third winding's topology might fix α at the value 1/137 the way the lattice's overall geometry fixes other constants. This is the most speculative reading.

Reasons to think L3 is enough:
- *Continuum recovery.* In standard electromagnetism on T² (a 2D torus), α is well-defined without any third dimension. The continuum theory does not need a third winding.
- *Standard-Model parsimony.* The fine-structure constant exists in our 4D spacetime, where the "third winding" interpretation requires a specific cosmological topology that may or may not hold.

The chapter at outline stage flags both possibilities, picks neither.

### W3. What lattice observable gives α numerically?
<!--EC I've spent a lot of time searching for this kind of thing and so don't expect any simple answers like this section proposes.  If something falls out, great.  But I don't want to spend a lot of time searching for alpha in geometric ratios.  It appears to me that alpha appears on the material sheets because we are wrapping something that has already been wrapped once.  But it doesn't appear to be related to the actual dimensions of the thing being wrapped.  Not sure if that is correct or not.  -->
If α appears at L3, what specific lattice quantity equals 1/137 (or its dimensionless equivalent)?

Candidates worth investigating:

- *Ratio of topological invariants.* If charge is winding (w_α, w_β), then α might be a ratio like (winding density on a unit plaquette) / (winding density across the full torus). For specific torus dimensions, this evaluates to specific dimensionless numbers.
- *Combinatorial counts.* The number of distinct 6-cycles per unit cell on hex (2D), or per unit cell on diamond (3D), gives definite combinatorial constants. α might be expressible as a combinatorial ratio of paths on the lattice.
- *Spectral invariants.* The lattice's graph Laplacian has a spectrum; α might be a ratio of specific eigenvalue moments. Heat-kernel and ζ-function constructions on graphs (Verlinde-style) are the natural setting.
- *Geometric constants.* Hexagonal close packing has a packing density of π/(2√3) ≈ 0.907; diamond has structural constants. None of these obviously gives 1/137, but the right combination might.

Resolving this requires actual lattice-gauge-theory or graph-spectral computation; it is outside the chapter's scope at outline stage.

---

## §1. The chapter's job
<!--EC If leakage is universal in wrapping, one potential question: is entropy the lead at the mass wrap level?  (and charge is the leak at the next level?) -->
Locate α on the wrap-promotion ladder. Identify the structural candidates for α's lattice origin. Be honest about what the chapter can and cannot deliver: it identifies *where* α plausibly first appears (L3, possibly with L4 contributions) and *what kind of object* α plausibly is (a ratio of topological invariants), but it does not derive α = 1/137 from lattice geometry. That derivation is open work requiring machinery beyond this project's scope.

The argument runs parallel to chapter 7's mass-at-L2 argument: mass is unavailable at L1 because L1 lacks the dimensional context; α is plausibly unavailable below L3 because the lower rungs lack the topological context. The structural pattern of the wrap-promotion ladder is "each rung makes available the simplest new conserved quantity that the new topology supports"; α fits this pattern as the natural L3-or-above quantity that requires multiple winding directions.

## §2. The mass-at-L2 parallel

A short subsection that recapitulates chapter 7 §4.1's argument for mass needing 2D context, and articulates the parallel claim for α needing L3-or-above context. The structural argument has the same shape:

- *Mass requires v_g = 0 at a band extremum.* Band extrema require coord ≥ 3, which requires ≥2D embedding. Mass first becomes available at L2.
- *α requires cross-coupling between (at least) two topological invariants.* Two independent winding directions require T² (or higher torus). α first becomes available at L3.

Both statements have the form: the quantity is unavailable below the rung where its required structure first appears. This is not a coincidence; it is what the wrap-promotion ladder is.

## §3. Why α plausibly first appears at L3

Three independent structural arguments, paralleling chapter 7 §2's three-pronged periodicity argument:

### §3.1 Cross-coupling needs two topological invariants

α relates charge (a quantised topological invariant) to the gauge field that mediates EM interactions (a second structure that lives on cycles). Both must exist simultaneously and independently for α — the *ratio between them* — to be defined. Below L3 there is at most one topological invariant (the L1 / L2 winding around a single direction), so α cannot be defined as a ratio because the numerator and denominator collapse into the same object.

### §3.2 The U(1) × U(1) structure at L3

L3's torus has π₁ = ℤ², giving two independent U(1) factors. The two are dual: electric and magnetic (in the standard EM reading). α is the natural coupling constant *between* these two U(1)s — the strength with which one's quantum couples to the other's quantum. This is exactly the situation where α has a structural meaning; L1 and L2 don't have the second U(1) for the coupling to be defined against.

### §3.3 Quantised charge as the substrate of α

α has the reading "α e² = the strength of EM coupling at the natural scale." For α to be dimensionless and finite, e (charge) must be quantised — otherwise the coupling rescales arbitrarily with charge convention. L3 is the first rung where charge is quantised by topology (winding numbers are integers); below L3, "charge" is at most a continuous-valued plaquette flux. Without quantised charge, α has no dimensionless meaning. With quantised charge — as L3 first provides — α becomes definite.

## §4. Candidate structural origins of α

The chapter would survey candidate lattice observables that might equal 1/137 (or a dimensionless equivalent). Each is a hypothesis; none is yet derived.

### §4.1 Ratio of winding densities

If charge is winding (w_α, w_β), the natural ratio is (w_α / total area) ÷ (w_β / total area) for some specific geometric configuration. On specific torus dimensions and lattice types, these ratios evaluate to specific dimensionless numbers. The hypothesis is that α is one such ratio for a canonical configuration (e.g., the unit cell of the dual lattice).

### §4.2 Combinatorial path counts

Each lattice has a definite count of distinct closed paths of given length per unit cell. Hex has 1 hexagon per cell (in the right counting convention); diamond has counts that include both 6-cycles and longer paths. α might be expressible as a combinatorial ratio of paths — e.g., (number of hexagons) / (number of 12-cycles) per unit cell — that evaluates to ≈ 1/137 for the right lattice topology.

### §4.3 Spectral invariants on the graph Laplacian

Verlinde's entropic-gravity construction (chapter 5 §4.4) used the graph Laplacian's spectrum to define gravitational behaviour. The same spectrum has higher-moment invariants: Σ 1/λ², Σ λ², log det(L), etc. These produce specific numbers for specific lattices. α might be one such moment ratio.

### §4.4 Heat-kernel / ζ-function constants

A lattice graph has a heat-kernel trace tr(e^{-tL}) whose t → 0 expansion gives the lattice's spectral dimension and other constants. Some of these constants have universal values; α might be expressible in terms of one. This is closely related to §4.3 but uses analytic-continuation machinery.

### §4.5 Renormalisation-flow fixed points

α runs with energy scale: α(μ_low) ≈ 1/137 at atomic scales but increases at higher μ (≈ 1/127 at the Z mass). If the lattice has a natural energy scale set by its cell spacing (Planck), then α at any μ is α(Planck) flowed down to μ. The fixed-point structure of this RG flow on the lattice might fix α at a specific value at the IR fixed point. This is the most speculative candidate but also the most physically motivated.

## §5. The L4 connection (speculative)

A subsection that takes seriously the possibility α requires L4's third winding. Two specific scenarios:

- *α as cross-coupling among three windings.* If electromagnetism is one U(1) of an underlying U(1) × U(1) × U(1) structure (or something embedding it), α might be the cross-coupling between the EM U(1) and a third structure. The third U(1) might be cosmologically scaled (the universe-as-3-torus reading) or particle-scale (some not-yet-identified gauge structure).
- *α as a function of cosmological topology.* If the universe's specific 3-torus dimensions fix the value of α, then α is a topological constant of the universe's overall shape. This would explain why α has the specific value it does: it would be a property of *our* cosmological topology, varying in different topologies.

Both scenarios are honest speculation. The chapter would identify them and leave them open.

## §6. Honest scope and what would be needed for a derivation

The chapter would close with explicit statements about its limits:

- It identifies where α plausibly first appears: L3 (with possible L4 contributions).
- It identifies what kind of object α plausibly is: a ratio of topological invariants on the lattice.
- It does not derive α = 1/137. That derivation requires:
  - Explicit lattice-gauge-theory construction on the diamond lattice.
  - Calculation of specific topological / spectral invariants.
  - RG flow analysis if α is an IR fixed point.
- These are open work programs, each a separate project.

## §7. Closing pointer

α's structural location is L3; its specific lattice value is open. The wrap-promotion ladder ends here in this project's scope. Pointer to chapter 9 (closing summary).

---

## Appendix A: Notes for full chapter writing

- §2 (the mass-at-L2 parallel) is the chapter's structural backbone — it justifies why we expect α at L3 in the first place. Develop carefully.
- §3's three-pronged argument should be made concrete with specific examples: where, on a 1D ring, would α "fail to exist" as a definite ratio? Where, on a plaquette, similarly? Where on a torus does it suddenly cohere? Worked examples make the structural claim sharp.
- §4 candidate observables can each get its own subsection with explicit construction. None of these has been computed, so the chapter at outline stage just lists them; full chapter would compute at least one and report whether it lands near 1/137.
- §5 (L4 speculation) should be honest about scope — same care as chapter 7 §6 took with the speculative third invariant.
- §6 (scope statement) is essential. Without it, the chapter risks reading as if it's claiming to derive α when it's actually flagging where to look. The honest scope is: "we know roughly where to look, we don't yet have the answer."
- The chapter should *not* attempt any of the lattice-gauge-theory derivations in §4 unless preliminary calculations show one of them lands near 1/137. The default is "this is the program; future work fills it in."

## Evaluation: is there anything useful to explore here?

A short note for the project author. **Yes, structurally.** The mass-at-L2 → α-at-L3 parallel is the chapter's substantive contribution — it gives a structural reason α has the *lattice level* it has, and identifies what kind of quantity α plausibly is. That is genuine progress over "α is a free parameter we don't understand."

**No, computationally.** The chapter does not derive α = 1/137 and probably cannot without substantially more machinery. The candidate observables in §4 are honest hypotheses, not results. Anyone reading the chapter should leave understanding *where to look* (L3 topological invariants on a hex / diamond lattice) and *what to look for* (a dimensionless ratio that evaluates to 1/137), not feeling that the question is solved.

**The honest verdict for this project's chapter 8.** Useful as a structural-locator chapter that closes the wrap-promotion ladder cleanly: substrate (L0) → light (L1) → mass (L2) → charge (L3) → α (L3, structurally) → ? (L4, speculative). It identifies α's natural home and connects it to the rest of the project's framing. It does not solve α; that is acknowledged as open work for a separate effort.

If the project wants to attempt at least one §4 candidate computation before closing, the most tractable target is §4.1 (winding-density ratios on standard lattices) — small Python computation, definite answer, falsifiable hypothesis. That would either land near 1/137 (in which case the chapter has a real result) or rule out that specific candidate (in which case the chapter has a real exclusion). Either is a clean outcome; the speculation in §4.2–§4.5 can be left as future work in either case.
