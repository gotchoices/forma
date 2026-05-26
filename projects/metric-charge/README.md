# metric-charge

**Type:** Educational project (see [../README.md](../README.md))
**Scope:** Charge generation on a 2D compact sheet. Mass is covered in [metric-mass](../metric-mass/); multi-knot interactions are deferred to [metric-binding](../metric-binding/).
**Method:** Mathematical derivation as discovery; minimal computation.
**Status:** Chapters 1–7 in full prose; Chapter 8 in outline form (energy-minimization computation pending); Ch 11 appendix in place as a stable foundation for downstream wave-equation-based modeling. See [review.md](review.md) for the project's open-issues log.

## Why this project exists

[metric-mass](../metric-mass/) established how a single compact dimension produces mass: standing-wave momentum along u, quantized by periodicity, behaves operationally as inertial mass. This project picks up the analogous question for charge.

The naive next step would be to add a second independent compact dimension w and treat it the way Kaluza-Klein treats charge — momentum on w → quantized as charge. That step is well covered in [`primers/kaluza-klein.md`](../../primers/kaluza-klein.md), and metric-mass deliberately did not take it. Repeating it here would just rehearse the standard KK story.

We jump instead to a **2D compact sheet** — one continuous 2D torus with coordinates u and w. The structural reason comes from [grid-duality §7](../grid-duality/07-wrap-promotion-modeling.md): charge first appears at **L3** of the wrap-promotion ladder, where the substrate has been wrapped twice and the closure produces a 2-torus T² = S¹ × S¹ with π₁(T²) = ℤ². Below L3 there is at most one winding direction; L3 is the *first* rung where the substrate has the wrap-order asymmetry (one direction as ring, the other as tube) that charge structurally requires. metric-charge takes this L3 substrate and asks what additional structure emerges when it is embedded in extended spacetime. Charge becomes something the **geometry of the sheet** produces — not something a second independent CD provides.

The central question:

> *What does light alone on a manifold with one **2D compact sheet** produce, and under what conditions does the sheet's geometry cause a (massive) standing-wave mode to also carry something that behaves like charge?*

### Underlying targets

The framework should illuminate, without explicitly hunting for any of them:

- **Quark-like three-phase structure** on a single sheet — how does the geometry produce three repeating phases? Where does fractional charge come from?
- **Aspect-ratio extremes** — what does a very fat or very thin sheet correspond to physically? Can the framework predict why one species would land at extreme ε while another sits near unity?
- **Apparent neutrality** — can a sheet produce mass with no observable charge? Is "no charge" structural (the wrap simply doesn't satisfy the closure condition), a diffuseness limit (charge is real but spread over a vast L_w), or a complementary-pair cancellation?

(Multi-knot interactions, force laws, and bound-state regimes are the subject of the follow-up project [metric-binding](../metric-binding/), not this one.)

The framework is not **on the hunt** for the proton, electron, or neutrino sheets specifically. It is in **discovery mode** — exploring how sheet shape (aspect ratio ε), shear (σ_uw), and multi-phase wrap population sort modes into qualitatively different particle classes, including possible single-phase, three-phase, and dark behaviors.

## Coordinates and notation

| Symbol | Role | Type |
|---|---|---|
| **t** | Time | Extended, real (rendered along z) |
| **S₁** | First spatial extension | Extended, real (rendered along x) |
| **S₂** | Second spatial extension | Extended, real (rendered along y) |
| **u** | First compact coordinate on the 2D sheet | Compact: u ~ u + L_u |
| **w** | Second compact coordinate on the 2D sheet | Compact: w ~ w + L_w |

x, y, z are Cartesian *visualization* axes — not metric coordinates.

- **Aspect ratio:** ε ≡ L_u / L_w. Free parameter of each sheet.
- **Shear:** σ_uw is the off-diagonal metric entry coupling u and w. Tilts the compact directions away from orthogonality and breaks several symmetries we'll see come into play.

**Visualization disposition.** When rendered, the compact sheet sits in 3D space at roughly 45° to the (x, y, z) axes — u's normal points roughly (+y, +z), w's normal roughly (−y, +z). The intent is to keep the compact directions visibly distinct from S₁, S₂, and t while still inhabiting the same 3D space. Shear narrows the (otherwise 90°) angle between u and w as seen from above. With the compact dimensions exaggerated for visualization, knots through (S, t) can be drawn as spirals through space and time.

**Why two S dimensions** (whereas metric-mass had one): single-knot derivations in this project largely don't require S₂ — most results work in S₁ alone. S₂ is carried in the coordinate set as forward-looking infrastructure for [metric-binding](../metric-binding/), where the second spatial dimension is essential for placing two knots at different (S₁, S₂) positions. Keeping the coordinate set consistent across the two projects avoids a notational reset at the boundary.

## Strategic stance

The metric is the framework's primary structural object. For each closure-satisfying particle species, the framework should ultimately provide a metric prescription — specific values of the diagonals, ε, σ_uw (with the equivalent lattice-shear label s where helpful) — derived from the species' structural properties (mass, charge, generation, chirality). This project sets up the single-particle case and characterizes what charge looks like given a sheet; deriving the parameter values from species identity is downstream work, in [metric-binding](../metric-binding/) and beyond.

## Ground rules

1. **Discovery, not proof.** Where possible, do mathematics that *discovers* a result rather than confirms a prior one. We may know roughly what to expect from MaSt, but the chapter arc should let the math reveal it. (Acknowledged: this is not strictly possible when the result is already known — but the arc should still feel like discovery, not appeal-to-authority.)

2. **Don't re-derive metric-mass.** If a result was established there, cite it. Re-deriving content from `papers/derivations.md`, R62, etc. is fine where it serves the narrative.

3. **Inherit from grid-duality.** The wrap-promotion ladder, the structural location of charge at L3, and the integer-quantization of winding numbers are all established in [grid-duality](../grid-duality/) (chapters 7–8). We use them; we don't re-derive them. metric-charge's distinctive job is to render this L3 substrate in spacetime-metric terms and to do parameter sweeps (ε, σ_uw) that grid-duality's fixed-substrate construction does not.

4. **MaSt identifications are reference targets, not inputs.** MaSt's existing model-versions (model-A through model-F) propose specific correspondences between geometric modes and standard-physics particles — for example, model-F proposes T(1, 2) as a candidate identification with what standard physics calls the electron. **The framework here treats those proposals as reference targets to compare derivation results against, not as axiomatic inputs.** The project's job is to derive structural properties (mode labels, masses, charges, gauge structure) from the closure-condition machinery — and then, separately, to ask whether those properties match MaSt's model-F proposals or standard physics' inventory. Identification is a downstream comparison task, not a prior commitment. Standard Model terminology (electron, proton, neutrino, quark, gauge potential) appears as a reference vocabulary, not as something the framework imports.

5. **The closure condition is axiomatic, not derived.** This project takes "wraps satisfying condition X produce charge" as an *input* to be explored. The α-coupling-strength derivation belongs in [grid/](../../grid/) — we use the result here, we do not re-derive it.

6. **One topic per chapter.** Bundling defeats the discovery arc.

7. **Variables stay symbolic.** Don't pin numerical values until the algebra forces it (per the no-premature-pinning rule).

8. **Computation only when forced.** Paper math first; scripts only when algebra becomes intractable or visualization is the only way to see the geometry.

## Goals

### Theories to test

Claims to examine — derived where possible, stated explicitly when taken as input, and falsified explicitly if the math doesn't support them.

1. **Mass from a 2D standing wave.** A standing wave on a compact 2D surface of any shape produces mass — direct generalization of metric-mass.

2. **Knots as massive modes.** A *knot* — a closed curve that traverses the 2D surface — produces mass when its total path length equals the Compton wavelength of the relevant energy level.

3. **Knot families.** A 2D surface supports a *family* of knots labeled by winding pair (m, n) and possibly higher topological invariants. Goal: characterize the family — series, generations, exclusions.

4. **Topological invariants as quantum numbers.** Crossing number, genus, and linking number map to physical labels: lighter particles correspond to lower-crossing knots; generations to higher-crossing knots in the same isotopy class. Worth checking whether this organizes the spectrum cleanly.

5. **The closure condition (centerpiece) — chirality criterion.** A configuration T(m, n) carries observable EM charge iff (i) the closed curve is achiral in 3-space — its chirality reflections are topological symmetries — *and* (ii) the wrap-order's ring-direction reflection R_u is among those topological symmetries. Within the torus-knot family on T², (i) reduces to "the gcd-reduced primitive has tube winding 1" (the unknot), and (ii) is automatic. Operationally: **m divides n (m | n) with both nonzero** under the tuple convention m = tube, n = ring. The closure-satisfying inventory is exactly the **T(1, n') primitives and their k-component repetitions k × T(1, n')**.

6. **Closure failure → mass without observable charge — three mechanisms.** A wave configuration that does *not* satisfy the closure rule carries mass but no observable EM:
   - **Single-axis** (one winding zero) — fails by structural degeneracy: no chirality structure on the curve to test
   - **Chirality-non-degenerate** (genuine torus knots T(p, q) with p, q ≥ 2 and gcd = 1 — e.g., T(3, 2), T(5, 2), T(4, 3), ...) — fails by chirality non-degeneracy: the curve is chirally distinct from its mirror in 3-space
   - **Sign-conjugate cancellation pair** (single field with both (m, n) and (−m, −n) at equal amplitude — see Chapter 6 §4) — closure-satisfying mode in R_J-symmetrized form (instead of the natural R_u-symmetrization); the gauge potential cancels, mass and chirality field T_uw remain
   
   Three structurally distinct mass-only mechanisms, each producing massive but EM-neutral states by a different route. Candidate identifications with what standard physics calls neutrinos, neutral mesons, the Higgs, and other neutral massive states are downstream MaSt-correspondence work.

7. **Knot handedness as a candidate matter/antimatter axis.** A knot has two traversal directions. The (m, n) ↔ (−m, −n) sign reflection is the framework's candidate axis for what standard physics calls matter/antimatter. Whether the framework derives any *bias* on this axis (a population preference for one over the other) is open — Chapter 6 §6 demonstrates that σ_uw shear cannot provide such a bias (σ_uw biases chirality *within* particles, not matter/antimatter populations); candidate mechanisms (different shear, substrate-level chirality from grid-primitive/grid-duality) are forwarded for project-direction work.

8. **Shear biases chirality within particles, not matter/antimatter populations.** σ_uw between u and w produces:
   - **Intra-particle chirality bias** — within a natural particle (R_u-symmetrized configuration), σ_uw splits the energies of the (++) and (−+) components, biasing the internal amplitude balance (Chapter 6 §6, Chapter 8 §3)
   - **Selection of multi-component link structure** — the energetics of k × T(1, n') configurations under shear pick out a favored k_opt(σ, ε) (Chapter 8 §6)
   - **No matter/antimatter bias.** σ_uw is *invariant* under (m, n) ↔ (−m, −n); the joint-sign-flip symmetry is preserved (Chapter 6 §6, derivation explicit)

9. **Multi-phase knots on w produce fractional charge (the quark mechanism).** N knots distributed evenly in w-phase, all sharing the same closure pattern, contribute fractional 1/N charge each. Three-phase populations give thirds-of-a-charge — the structural origin of quark-like behavior on a single sheet. The closure condition still applies per knot, but the *embedding pattern* of multiple knots around the w-cycle is what produces fractional contributions.

10. **Sheet character emerges from (ε, σ, multi-phase population).** Varying sheet shape, shear, and how many phased wrap copies populate the sheet sorts the admissible mode family into qualitatively different particle classes — single-phase, three-phase, and dark — without explicitly hunting for any of them. Single-sheet mini-universe: we cannot have a "proton" or "electron" by name (those require multi-sheet structure in MaSt), but we can characterize *what kinds of particles a single sheet supports* under varying conditions.

(Multi-knot superposition, finite-separation interaction energies, and the strong-force-candidate bound-state regimes are theories tested in [metric-binding](../metric-binding/), not here.)

### Open questions

To answer or sharpen along the way:

1. **What distinguishes matter from antimatter?** An energy-comparison regimen is needed: when does a knot's energy stay bound in Ma (mass) and when does it leak to S (radiation)?

2. **What does ε = L_u / L_w do?** Predict effects forward from the metric, not retroactively. Specifically: which ε regimes admit which knot families, and is there a structural reason for extreme aspect ratios (very fat / very thin) to appear?

3. **What does σ_uw select?** Which behaviors does shear pick out, and how cleanly? Three-phase population and proton/neutron-style splitting both should be examined here.

4. **What sets the particle inventory?** Is it the full enumeration of admissible knots up to some crossing number, or are there structural exclusions (Pauli-like) that forbid specific (m, n) pairs?

5. **Is the closure condition unique?** Does 2π-on-w + full-SW-on-both have alternatives that select different particle classes? Enumerating the variants would tell us whether all observable distinctions trace to one rule or several.

6. **What does S₂ actually buy *for single-knot derivations*?** Most single-knot results work in S₁ alone; flag the ones that genuinely need S₂. (The full payoff of S₂ — separation between knots — lives in [metric-binding](../metric-binding/).)

7. **What carries momentum through S when a knot moves?** Rigid translation, internal deformation, or precession?

## Background reading

- [metric-mass/](../metric-mass/) — the dimensional-laddering predecessor; mass-from-u
- [grid-duality/](../grid-duality/) — the substrate-level predecessor; charge as L3 phenomenon, wrap-promotion ladder, integer winding quantization. Especially [chapter 7](../grid-duality/07-wrap-promotion-modeling.md) (wrap-promotion ladder) and [chapter 8](../grid-duality/08-where-alpha-appears.md) (α at L3).
- [primers/kaluza-klein.md](../../primers/kaluza-klein.md) — standard KK (and why this project deliberately skips repeating it)
- [studies/R63-proton-tuning/](../../studies/R63-proton-tuning/) — proton sheet, three-phase structure
- [studies/R64-nuclear-harmonic-stack/](../../studies/R64-nuclear-harmonic-stack/) — quarks on the p-sheet
- [studies/R46-electron-filter/](../../studies/R46-electron-filter/) — electron sheet, fat aspect ratio
- [studies/R49-neutrino-filter/](../../studies/R49-neutrino-filter/) — neutrino sheet mode spectrum
- [grid/](../../grid/) — where the α numerical-value derivation will eventually live (structural location is settled in grid-duality)

## Chapters

The arc below is a *sketch*. Early chapters are framed in detail; later chapters are framed as questions to examine. The project may redirect when a chapter's math reveals something unexpected.

1. **`01-foundation.md`** — Axioms and givens. The (t, S₁, S₂, u, w) manifold, the metric (with ε and σ_uw as parameters), the wave field, and the closure condition stated axiomatically. Visualization disposition (45° rendering) included.

2. **`02-modes-on-a-sheet.md`** — Solve the wave equation on the 2D compact sheet. Derive the mode family labeled by winding pairs (m, n), the dispersion relation, and the discrete mass spectrum. Confirm the (0, 0) zero mode behaves as light; non-trivial (m, n) modes carry rest mass. Establish the (m, 0) and (0, n) "single-axis" modes as candidates for closure-failure mass-only states.

### Tentative downstream arc

The chapters below are plausible follow-ups, not commitments.

3. **`03-knots-on-the-torus.md`** — Reframe non-trivial modes geometrically as knots traversing the sheet. Characterize the knot family: which (m, n) pairs admit non-self-intersecting closures? Establish the topological invariants (crossing number, genus, linking) and how they index the family.

4. **`04-the-closure-condition.md`** — When does a (massive) mode also carry observable EM charge? Work through the chirality criterion (with synchronization m | n as the operational test) explicitly. Identify which (m, n) modes satisfy it (charged-state modes) and which don't (mass-only modes — single-axis, chirality-non-degenerate, and cancellation-pair candidates for non-charged massive states).

5. **`05-metric-self-consistency.md`** — *Metric self-consistency and gauge promotion.* Compute T_μν for the per-component intermediate (single traveling-wave mode), then apply the wrap-order-asymmetric standing-wave construction: R_u-symmetrization of the natural particle (standing in the ring direction, traveling in the tube direction) cancels the ring's would-be cross-term and preserves the tube's, producing **a single gauge potential B_μ from h_μw** per closure-satisfying particle. Closure-failing modes — single-axis and chirality-non-degenerate genuine torus knots — yield mass-only outcomes via R_u-only or R_J-fallback symmetrizations under the same construction. Establishes closure as the *metric-side* rule under which mass-induced off-diagonals become observable EM, parallel to metric-mass Chapter 5 but applied asymmetrically per the wrap-order convention.

6. **`06-handedness-and-pairs.md`** — Knot orientation as the (candidate) matter/antimatter axis. Examine when complementary pairs *within a single field configuration* cancel net charge (R_J-symmetrization replacing the natural R_u), giving apparent neutrality through internal cancellation, distinct from the structural neutrality of chapters 4 and 5. Derive what σ_uw shear actually breaks at the dispersion level — the chapter shows σ_uw biases chirality (m, n) ↔ (m, −n) *within particles* (not between matter and antimatter populations), with a structural reason: σ_uw is invariant under joint sign flip. The two-distinct-knots version of pair behavior — pass-through vs. annihilation — is taken up in [metric-binding](../metric-binding/).

7. **`07-aspect-ratio-and-character.md`** — Sweep ε = L_u / L_w. Discover what knot families dominate at small ε (thin sheet), large ε (fat sheet), and ε ≈ 1. Look — without targeting it — for the conditions under which a sheet supports single-phase, three-phase, or dark behaviors. The "extreme aspect ratio" question (per MaSt model-F's electron-sheet identification) and the "diffuse charge" question (per model-F's neutrino-sheet identification) are examined here as reference targets, not as identifications this project pre-commits to.

8. **`08-shear-and-fractional-charge.md`** — Turn on σ_uw. Quantify the chirality bias derived in Chapter 6 §6 (the explicit mass split between chirality partners within a natural particle under shear). Then examine the fractional-charge optimization: closure-satisfying multi-component links of the form k × T(1, n') have 1/k charge per component; the chapter computes which k is energetically favored under shear and reports the result honestly. If k = 3 emerges, the framework matches the structural pattern that MaSt model-F associates with quark organization.

9. **`09-ratio-and-shear.md`** — Bring ε and σ_uw together into a unified treatment of the (σ_uw, ε) parameter space. Identify three structural regimes mapping to three qualitative sheet types (lepton-like, neutrino-like, hadronic-like). Develop the σ → 1 principal-axis suppression mechanism and set up the substrate for the downstream inversion exercise of deriving (ε, σ_uw) from a sheet's observed properties.

10. **`10-closing-summary.md`** — Consolidate what the project established, ruled out, and unexpectedly found. Hand off to [metric-binding](../metric-binding/) for the multi-knot interaction story.

11. **`11-modeling-foundation.md`** — *Appendix.* Foundation for downstream wave-equation-based modeling on metric-charge's substrate. Gathers (in chapter-grade form) the foundation that downstream projects ([ma-domain](../ma-domain/), [sheet-proton](../sheet-proton/), [metric-binding](../metric-binding/)) will lean on. Picture A (the wave equation on the substrate) throughout; seven citable foundation results (F1–F7) plus two carried-under-named-hypothesis results (H1 under G1 for per-arc fractional charge; H2 for picture B borrowing if needed). Addresses the shape-vs-HO-complex duality (both views of picture A) and the angular-momentum reading of rest mass. Picture B (the bare 2D HO as a separate physical system) noted as a future borrowing option, not currently used. Stable citation target via F- and H-numbers.

Each chapter is added one at a time. The arc is a sketch, not a contract.
