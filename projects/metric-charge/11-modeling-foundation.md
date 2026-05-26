# Chapter 11 (Appendix) — Foundation for downstream wave-equation-based modeling

The project's structural arc closes with [Chapter 10](10-closing-summary.md).
This appendix is a forward-looking hand-off rather than part of the
in-project derivation. It does not introduce any result that
chapters 1–10 use, and nothing here amends or revises what those
chapters established.

What the appendix does is gather, in chapter-grade form, the
foundation that downstream projects ([ma-domain](../ma-domain/),
[sheet-proton](../sheet-proton/), [metric-binding](../metric-binding/),
and others) will lean on when they model structure on metric-charge's
substrate. Several work files in [work/](work/) have developed this
foundation in detail; the appendix carries the chapter-level
statements so that downstream work has a stable citation target.

## Concepts introduced in this chapter

A short glossary for the sections below. Physics-trained readers
can skim. Entries are aimed at a college-level engineering reader
who may not have these as everyday vocabulary.

- **Canonical quantisation.** The standard procedure for promoting
  a classical wave field to a quantum field. Each independent
  Fourier mode of the classical field is treated as a separate
  quantum harmonic oscillator with its own creation and
  annihilation operators.

- **Ladder operators (creation / annihilation), a† and a.** For
  each mode, two operators that increase or decrease the number
  of quanta in that mode by one. "Quantum" here means one
  indivisible excitation of the field. The two operators satisfy
  [a, a†] = 1 (the standard quantum-mechanical relation;
  operators belonging to different modes commute).

- **Fock space.** The state space of the quantised field — every
  state the field can occupy. Built from a *vacuum* state |0⟩
  (no quanta anywhere) by acting with creation operators. A
  general basis state is labelled by occupation numbers, e.g.,
  "n₁ quanta in mode 1, n₂ in mode 2, …"; arbitrary superpositions
  are also allowed.

- **Noether's theorem / Noether-conserved charge.** Every
  continuous symmetry of a physical system corresponds to a
  conserved quantity. Time-translation symmetry → conservation
  of energy; spatial-translation symmetry → conservation of
  momentum; phase-rotation symmetry → conservation of charge.

- **U(1), SU(2), SU(N).** Group-theory notation for continuous
  symmetry groups. U(1) is the group of phase rotations
  (multiplication by e^{iθ}, one continuous parameter). SU(N) is
  the group of N × N complex matrices that are unitary and have
  determinant 1 — they describe how the components of an
  N-component complex vector can be mixed without changing its
  overall length. SU(2) is the group of spin-1/2 rotations;
  SU(3) is the gauge group of QCD's colour charge. (*Scope
  note:* this chapter's downstream targets that name "SU(2)" or
  "SU(3)" refer to the *structural* features of those algebras —
  fractional-charge inseparability, multi-component mixing — not
  necessarily to a full Yang–Mills gauge theory. §5 and §8
  flag the gap between "structural analog" and "gauge theory"
  where it matters.)

- **Dihedral group D_4.** The symmetry group of a square — 4
  rotations (by 0°, 90°, 180°, 270°) plus 4 reflections, 8
  elements total. In this appendix, D_4 acts on the integer
  (m, n) lattice in the natural way (swapping axes, flipping
  signs, rotating by 90°).

- **Hermite functions.** The eigenstates of the standard 1D
  quantum harmonic oscillator on the real line. A family of
  orthogonal functions of the form (polynomial of degree n) ×
  e^{−x²/2}. They are used as a reference vocabulary in §8
  (picture B) and need not be familiar in detail.

- **Coherent states.** Quantum states that approximate
  "classical" particles as closely as possible: minimum-
  uncertainty Gaussian wavepackets whose centres follow
  classical trajectories without spreading.

- **Geodesic curvature κ_g.** For a curve drawn on a surface, the
  rate at which the curve bends *within the surface* relative to
  the straightest-possible path (the geodesic) on that surface.
  A geodesic has κ_g = 0; any other curve has nonzero κ_g.

- **Gauss–Bonnet theorem.** A topological identity for a closed
  region on a surface, relating the total geodesic curvature
  along the boundary plus the total intrinsic curvature inside
  the region to the region's topology. For a simply-connected
  flat region with a smooth closed boundary, the identity
  reduces to ∮ κ_g ds = 2π — the tangent makes one full
  revolution as it traverses the boundary.

- **Holonomy / Berry phase.** A phase picked up by a quantum
  state (or wave) when parallel-transported around a closed
  loop on a curved geometry. Used briefly in §6 as a candidate
  promotion route for the per-arc charge bridge.

## Scope

The framework's actual physics — derived in chapters 1–10 — is the
**wave equation on a compact substrate**. The mass formula
(Ch 2 §3), closure condition (Ch 4), KK gauge identification
(Ch 5), σε product (Ch 8), and the (σ, ε) regime structure (Ch 9)
are all canonical-quantization results on this substrate. This
appendix calls that physics **picture A** and stays in it
throughout.

Two specific downstream questions motivate the appendix:

- **Per-arc fractional charge.** Modulated-clover constructions
  in the sheet-proton and ma-domain work folders read fractional
  charge as integrated geodesic curvature along arcs (Q_lobe = +2/3,
  Q_saddle = −1/3). Whether this per-arc reading is consistent
  with the framework's charge mechanism, and what its limits
  are, is settled in [work/per-arc-curvature-as-charge.md](work/per-arc-curvature-as-charge.md);
  §6 below carries the chapter-level summary.

- **Photon-on-shape vs HO-complex.** The framework's intuitive
  picture of a particle as a closed wave traversing a shaped
  substrate, and the alternative picture of the same particle as
  a multi-mode harmonic-oscillator complex (Hermite-style normal
  modes resonating at frequencies set by the substrate's shape),
  are two views of the same physics — both in picture A. §4
  develops the duality explicitly and makes the citable
  statement downstream projects need.

A third structural item — the angular-momentum reading of rest
mass — addresses the conservation-as-momentum direction in
ma-domain work; §7 carries it.

The chapter does *not* introduce a second physical model
alongside picture A. The earlier work-file framing entertained
a picture B (the bare 2D harmonic oscillator as a separate
physical system whose algebra could be borrowed); see §8 for
why that route was set aside and under what conditions it might
be revisited.

---

## 1. Picture A — the wave equation on the compact substrate

The framework's substrate is a manifold with one or more compact
directions: T² in this project ([Ch 1 §1](01-foundation.md)), with
extensions to more elaborate compact shapes (modulated tubes,
clover cross-sections, multi-sheet stacks) in downstream
projects. On any such substrate, the wave equation

<!-- □ φ + m² φ = 0 -->
$$
\Box\,\varphi \;+\; m^2\,\varphi \;=\; 0
$$

with periodicity around each compact direction admits a discrete
mode family labelled by integer winding numbers (m, n, …).
Canonical quantisation (see glossary) promotes each independent
mode of this classical field to its own quantum harmonic
oscillator, with creation and annihilation operators
(a†_{m,n,…}, a_{m,n,…}) — one pair per integer-labelled winding
mode. The full quantum state space — the **Fock space** — is
then built up by starting from the vacuum (no quanta anywhere)
and acting with creation operators to populate the modes.

This is **picture A**. It is the framework's actual physics.
Everything chapters 1–10 derive is in picture A: the Pythagorean
mass formula, the closure condition, the KK gauge identification,
the σε product, the (σ, ε) regimes. No alternative quantisation
is in play.

Two features of picture A worth keeping in view because they
matter for the sections below:

- **One ladder per mode.** Each integer-labelled winding mode
  (m, n) gets its own pair of creation/annihilation operators.
  A single quantum of mode (m, n) is the state
  a†_{m,n}|0⟩; a two-quantum state can have both quanta in the
  same mode or one quantum in each of two different modes.
- **Continuous symmetries are limited.** Picture A on T² with
  R_u = R_w carries U(1) × U(1) (Noether-conserved
  compact-direction momenta — the conservation laws coming
  from translation invariance around each compact direction)
  plus the discrete dihedral group D_4 on the integer (m, n)
  lattice (90° rotations and reflections of the integer mode
  labels). It does *not* carry continuous SU(2), SU(3), or any
  other continuous internal symmetry beyond the U(1)'s. §5
  develops this.

---

## 2. Citable foundation results

Concrete results downstream projects can cite from this appendix.
All are in picture A.

| # | Result | Source |
|---|---|---|
| F1 | The 2D rest mass is the Pythagorean sum of squares of two single-direction masses: m² = m_u² + m_w². | [Ch 2 §3](02-modes-on-a-sheet.md) |
| F2 | The Pythagorean answer is *also* obtainable by a sequential algebraic path: treat m_u as a 1D rest mass, then add a second compact direction's KK momentum p_w; the relativistic dispersion gives m² = m_u² + (p_w/c)². Sequential and joint approaches are two algebraic paths to the same dispersion within a single canonical quantisation of the substrate's wave equation — not two distinct quantisation procedures. | [work/ho-bridge-2d.md](work/ho-bridge-2d.md) "Hypothesis A" |
| F3 | "Charge requires non-trivial winding in both compact directions" is the **necessary** condition of the closure rule. The **sufficient** condition is the m \| n synchronisation that Ch 4 develops within the both-nonzero family. The "prior mass" reading of charge captures the necessary half only. | [work/ho-bridge-2d.md](work/ho-bridge-2d.md) "Hypothesis B"; [Ch 4](04-the-closure-condition.md) |
| F4 | U(1) × U(1) charge structure is **A-native**: each compact direction's phase rotation is a Noether symmetry; the two associated conserved charges are p_w and p_u (the KK identification of Ch 2 §5 and Ch 5). | [Ch 2 §5](02-modes-on-a-sheet.md), [Ch 5](05-metric-self-consistency.md) |
| F5 | The integer winding number n of a single-direction mode is the **quantized angular momentum** of the standing wave around the compact loop: J_u = ℏn. The rest-mass identification m_n = ℏ\|n\|/(R_u c) is equivalent to m·R·c = \|J\|. | [work/angular-momentum-as-mass.md](work/angular-momentum-as-mass.md) |
| F6 | Picture A's symmetry of the mode spectrum at R_u = R_w is the discrete dihedral group D_4 on the integer (m, n) lattice. Continuous SO(2) acting on (m, n) as real coordinates does *not* preserve the integer lattice and is not a symmetry of the actual spectrum. | [work/ho-bridge-2d.md](work/ho-bridge-2d.md) "Continuous internal symmetries" |
| F7 | Standard 2D-HO-style coherent states give wavepacket localisation on the substrate but follow elliptical classical orbits, not (m, n) torus knots. Knot-trajectory tracking requires a construction beyond standard coherent states. | [work/ho-bridge-2d.md](work/ho-bridge-2d.md) "Coherent-state localization" |

These are the foundation. Anything downstream uses from this
appendix should refer to F-numbers; the work-file derivations
back each one up.

---

## 3. Two further results carried under a named hypothesis

The following results are not derived from picture A alone;
each rests on an explicit, falsifiable hypothesis whose nature
is different in each case. The two are flagged here together
because both are appendix-citable foundations carried under
named hypotheses, but the hypotheses themselves sit at
*different rungs* on the assumption ladder (see "Hypothesis
status ladder" below).

| # | Result | Source | Hypothesis |
|---|---|---|---|
| H1 | The local EM charge density per unit arc length along a curve on the bent substrate is dQ/ds = (1/2π)·κ_g, where κ_g is the curve's geodesic curvature. Per-arc fractional charge follows: Q(γ) = (1/2π) ∫_γ κ_g ds; closed-track totals integrate to integer EM charge by Gauss–Bonnet. | [work/per-arc-curvature-as-charge.md](work/per-arc-curvature-as-charge.md) | **G1** (the local-leakage identification — see §6) |
| H2 | Continuous internal symmetries beyond U(1) × U(1) at radial isotropy points (continuous SU(2) at R_u = R_w on T²; continuous SU(N) at higher dimensions) are *available as a modelling tool* by borrowing the algebra of the bare-2D-HO-with-quadratic-potential as a *different* physical system whose one-quantum spectrum labels match. The borrowing does *not* upgrade picture A's discrete D_4 to continuous SU(2). | [work/ho-bridge-2d.md](work/ho-bridge-2d.md); [work/higher-order-charges.md](work/higher-order-charges.md) | **B1** (the picture-B borrowing premise — see §8) |

### Hypothesis status ladder

The framework carries several different *kinds* of "hypothesis"
across its chapters. They are not equivalent, and downstream
citations benefit from naming the kind:

1. **Free parameter, value forwarded to downstream mechanism.**
   Example: Ch 8 §7's k (the number of components in a
   multi-link). Linear theory does not fix k; structural
   consequences are derived "for any k" with the value-selection
   forwarded to inter-component dynamics. Carrying k as input
   asserts no specific physical claim — only the conditional
   "if k = N, then …" structure.
2. **Change of mathematical language (re-language).** Example:
   metric-mass Ch 9's HO translation. No new physics; the same
   canonical-quantisation spectrum reframed via operator
   algebra. The "hypothesis" is a choice of formalism, not a
   substantive physical claim.
3. **Substantive physical claim with specific functional form.**
   Example: **H1's G1** above. Asserts a specific local
   relationship (dQ/ds = (1/2π) κ_g) between a geometric
   quantity and a physical density. Falsifiable in a way the
   first two are not — a future companion derivation could
   yield a different functional form, in which case G1 is wrong
   and the per-arc chain breaks at Step 1.
4. **Borrowing the algebra of a different physical system as
   modelling vocabulary.** Example: **H2's B1** above. Adopts
   the algebra of bare 2D HO (a *different* physical system) as
   a tool for naming structures on picture A's spectrum. Not a
   physical claim about picture A's physics; a modelling-language
   premise with stated limits.

H1's G1 is the strongest claim (substantive physical, level 3);
H2's B1 is a modelling-vocabulary premise (level 4). Both are
falsifiable in their own terms — G1 by a different functional
form for the bend-to-charge identification; B1 by demonstration
that picture B's algebra fails to track picture A's structure
where it is being used to. Downstream citations should preserve
the level distinction.

---

## 4. Shape and HO-complex — dual views of picture A

A standing question the framework has been carrying: is a
particle better modelled as **a closed wave traversing a shaped
substrate** (the photon-on-shape view), or as **a multi-mode
harmonic-oscillator complex resonating at frequencies set by the
shape's parameters** (the HO-complex view)? For example: is the
proton better described as a photon on a torus whose tube is
shaped by several sinusoidal modulations, or as a complex of
HOs whose frequencies encode the tube's shape parameters?

These are **two dual views of the same physics** — both
picture A. The duality:

- **Photon-on-shape view.** The substrate has a definite shape
  (compact metric — torus, modulated tube, clover cross-section).
  A particle is a standing wave of the wave-equation field on
  that shape. The wave's mode structure and dispersion follow
  from the shape's geometry.
- **HO-complex view.** Decompose the wave equation in the basis
  of its own normal modes on the shape — each independent mode's
  amplitude evolves like a one-dimensional harmonic oscillator
  with its own frequency, set by the shape's parameters. A
  particle is a state in this multi-mode oscillator complex.
  The mode frequencies *encode* the shape.

**The two views are not competitors.** Picture A's wave
equation □φ + m²φ = 0 is already linear, so no "linearisation"
step is involved in the HO-complex view — it is simply the
mode-basis decomposition of the same wave equation. The shape
determines the normal-mode frequencies; the normal-mode
frequencies are what probes (scattering, decay spectroscopy)
actually measure as the resonance structure of the particle.
Either view is valid; each is useful in a different domain.

(If picture A is later extended with an interacting field —
e.g., the φ⁴ piece floated in
[Ch 8 §6](08-shear-and-fractional-charge.md) for k-selection
dynamics — then *that* interacting theory's small-oscillation
limit would be the natural setting for "small-oscillation"
language. For the free wave equation, what looks like a
small-oscillation step is really just normal-mode decomposition.)

| View | Domain | Calculational tool |
|---|---|---|
| Photon-on-shape (wave equation on substrate) | Substrate-level derivation; topology; closure; gauge identification | The wave equation itself, separation of variables, Gauss–Bonnet on the manifold |
| HO-complex (mode-basis decomposition) | Resonance spectrum; mode-by-mode analysis; probe-couplings; matrix elements | Normal-mode decomposition of the wave equation; canonical quantisation in the normal-mode basis; mode-by-mode amplitude operators |

For the proton specifically: a torus with a tube cross-section
shaped by several sinusoidal modulations (the modulated-clover
construction) admits both readings. In the photon-on-shape view
the proton is a standing wave on that shape; in the HO-complex
view the same proton is a multi-mode oscillator complex whose
mode frequencies depend on the modulation amplitudes and ratios.
A downstream calculation can use whichever view is more
convenient — usually the HO-complex view for spectroscopic
calculations, the photon-on-shape view for substrate-level
structural arguments.

**Both views live in picture A.** The HO-complex is *not* a
substitute physics; it is picture A in normal-mode coordinates.
The shape and the HO frequencies are dual representations of the
substrate's mode structure.

This duality is the citable statement: downstream projects
modelling particles as HO complexes are doing standard
small-oscillation analysis of picture A's wave equation on the
substrate's shape, not invoking a separate physical model.

---

## 5. Continuous internal symmetries in picture A

What continuous internal symmetries picture A *does* and
*does not* carry, in one place, for clean downstream reference.

**A-native (carried by picture A directly):**

- **U(1) × U(1).** Each compact direction's phase rotation is a
  Noether symmetry of the wave equation. The associated conserved
  charges are the compact-direction momenta p_w and p_u, which
  Ch 2 §5 and Ch 5 identify with the KK gauge charges. **This
  is the entire continuous-internal-symmetry content of picture A
  on T²** (more compact directions add more U(1)'s, one per
  direction).

**A-native discrete:**

- **Dihedral D_4 at R_u = R_w.** At equal radii the wave equation's
  mode spectrum m² ∝ m² + n² is invariant under the integer-
  lattice symmetries of the (m, n) plane: 90° rotations, axis
  reflections, and overall sign flip. This is a discrete, not
  continuous, enhancement of the symmetry at the isotropic point.
- **Z₂ overall sign flip.** Independent of isotropy.

**Not in picture A (regardless of radii):**

- **Continuous SU(2).** Continuous rotations of the (m, n) pair
  treated as real-valued coordinates do not preserve the integer
  lattice — an irrational rotation angle takes integer modes to
  non-existent intermediate values — and so are not symmetries
  of the actual mode spectrum. Continuous SU(2) does not appear
  in picture A on T² at any choice of radii.
- **Continuous SU(N) for N > 2.** Same reasoning, generalised to
  more compact directions: integer lattices have only discrete
  symmetries.

**Implication for downstream modelling targets.** Several
candidate identifications the framework has considered want
SU(N)-like structure: spin (SU(2)), weak isospin (SU(2)), color
(SU(3)). Picture A does not supply continuous SU(N) for any of
these. **Two distinct kinds of target should be separated**
before discussing routes:

- **Structural analog of an SU(N) target** — the
  fractional-charge inseparability and multi-component mixing
  phenomenology associated with the SU(N), without the
  gauge-theoretic dynamics. For color: 3-fold fractional charge
  with confinement-like inseparability of the fragments.
- **Full gauge SU(N)** — a Yang–Mills theory with N²−1 gauge
  bosons, covariant derivative, running coupling, asymptotic
  freedom (where applicable). The actual physics of QCD color
  or electroweak SU(2)_L.

The framework currently has A-native routes for *structural
analogs* of some targets, and no A-native route to *full gauge
SU(N)* for any of them. The borrowing route (§8) gets one
closer to continuous SU(N) algebra but does not by itself
deliver a Yang–Mills gauge theory either.

The available routes for *structural analogs* of SU(N) targets:

- **A-native topological route.** Construct the structural
  analog from picture A's available structure plus topology:
  - For *color's 3-fold confinement-like structure:* the k = N
    component-link mechanism of
    [Ch 8 §7](08-shear-and-fractional-charge.md) (already
    chapter-grade, gives k = 3 fractional charge with
    confinement-like inseparability of the components).
    **This is the structural analog of color, not gauge SU(3).**
  - For *spin-1/2's two-state structure:* half-twist windings,
    (1/2, 1)-style configurations from the modulated-clover work;
    or spin structures on the compact manifold (the standard
    differential-geometry construction that lets a manifold
    support half-integer-spin fields). Both are **candidate
    routes with known foundational gaps** — see §5.1 below.
- **Borrowing route.** Borrow the SU(N) algebra from a *different*
  physical system whose spectrum labels match (see §8). This
  route leaves picture A and brings the borrowing's status flags.
  It delivers continuous SU(N) algebra; it does not deliver
  gauge SU(N) without an additional gauging step.

The framework currently has at least one mature A-native route
for color's structural analog (Ch 8's k = 3 mechanism) and
candidate routes — with known gaps — for spin-1/2 (half-twist;
spin structure). Picture A is therefore not a dead end for SU(N)
*structural-analog* modelling; it just requires going
topological rather than continuous-symmetric at the geometric
level, and the gap between structural analog and full gauge
theory remains for any downstream work that wants the latter.

### 5.1 Two known gaps on the spin-1/2 A-native route

The half-twist / spin-structure routes for spin-1/2 are
*candidate* routes, not established ones. Two specific gaps
should be carried into any downstream citation:

- **The (1/2, 1) half-integer-tube-winding configuration sits
  outside the standard closure-mode derivation.**
  [modulated-clover.md](../sheet-proton/work/modulated-clover.md)
  flags this explicitly as a foundational gap. Constructions
  that rely on (1/2, 1)-style windings inherit the gap.
- **A spin structure on the compact manifold is a
  *prerequisite* for hosting spinor fields, not a *derivation*
  of spin-1/2 physics from the scalar wave equation.** Having a
  spin structure means one *can* write down spinors on the
  manifold; it does not produce the Dirac equation, the
  gamma-matrix algebra, or any specific spin-1/2 dynamics from
  the framework's scalar field. Going from picture A's scalar
  modes to spin-1/2 dynamics requires extending the
  field-equation structure beyond □φ + m²φ = 0, not just
  acknowledging that the manifold admits spinors.

Status of the spin-1/2 A-native route: **candidate,
foundationally incomplete on both legs.** Downstream work
citing this route should preserve the gap status; presenting
the route on equal footing with the much-more-mature color
k = 3 mechanism overstates its maturity.

---

## 6. Per-arc fractional charge under G1

Sheet-proton and clover constructions in downstream work read
fractional charge along an arc as the integrated geodesic
curvature normalised by 2π:

<!-- Q(γ) = (1/2π) ∫_γ κ_g ds -->
$$
Q(\gamma) \;=\; \frac{1}{2\pi}\,\int_\gamma \kappa_g(s)\,ds
$$

A complete simple closed plane curve gives Q = 1 by Gauss–Bonnet
(the total turning is 2π). An incomplete arc gives a fractional
partial sum.

The bridge from this reading to the framework's existing charge
mechanism is developed in
[work/per-arc-curvature-as-charge.md](work/per-arc-curvature-as-charge.md)
under one explicit working hypothesis:

> **G1 (local-leakage identification).** Bending the grid's
> hexagonal cylinder lattice into a 2D surface embedded in 3D
> produces, in the continuum limit, a local normal-E-field
> leakage density along any curve on the surface equal to
> (1/2π) κ_g(s).

G1 carries the load-bearing piece — extension of an
already-established uniform-circulation premise
([grid/charge-emergence.md](../grid/charge-emergence.md);
[grid/sim-impedance/F12](../grid/sim-impedance/F12-charge-per-radian.md),
[T12](../grid/sim-impedance/T12-charge-per-radian.md)) to
pointwise locality on curves with varying κ_g. Two promotion
routes are identified in the work file: locality from the
discrete lattice (grid-primitive-level addition), or a
lighter holonomy route that may close locality automatically.

**What follows under G1 (the chain summarised; full derivation
in the work file):**

- **Step 1.** Local charge density along a curve is
  dQ/ds = (1/2π) κ_g, with sign tracking convex/concave geometry.
- **Step 2.** Per-arc charge from integration: Q_i = (1/2π) ∫_{γ_i}
  κ_g ds. Each Q_i is a real local quantity, not just integrand
  bookkeeping.
- **Step 3.** Closed-loop total via Gauss–Bonnet on a
  topologically trivial enclosed region recovers integer EM
  charge: Q = (1/2π) ∮_γ κ_g ds = winding number of the tangent.
- **Step 4.** Per-arc fractions sum to the integer total:
  Q = Σ Q_i, with each Q_i fractional and the sum integer.
- **Step 5.** Local manifestation: short-wavelength probes
  couple to per-arc Q_i with sign tracking convex/concave
  geometry; long-wavelength probes couple to the integer total.
  Per-arc fractional charges exist locally but are confined to
  their host closed-loop integer totals — a structural realisation
  of confinement under G1.

This is **complementary** to Ch 8 §7's k-component-link
mechanism: Ch 8 decomposes the integer total **per-knot** across
k components of a multi-knot; the per-arc reading decomposes
along a *different* axis, **per-arc** of integrated geodesic
curvature on a single closed track. Both are valid; they
describe the integer total's decomposition along different
structural directions.

### Two distinct downstream constructions use H1 differently

Two clover-style constructions in [sheet-proton](../sheet-proton/)
and ma-domain work apply H1 in structurally different ways. The
distinction matters for how H1 should be cited:

**The literal-arc clover** ([sheet-proton/work/clover-quarks.md](../sheet-proton/work/clover-quarks.md))
takes a closed curve composed of three lobe arcs and three
saddle arcs with definite angular extents — 240° per convex
lobe arc, 120° per concave saddle arc. Each arc has constant
geodesic curvature κ_g = ±1/r over its extent. Step 2 then
gives clean per-piece values:

- Q_lobe (240° arc, κ_g = +1/r): (1/2π)(1/r)(4πr/3) = **+2/3**
- Q_saddle (120° arc, κ_g = −1/r): (1/2π)(−1/r)(2πr/3) = **−1/3**

Closed-track totals follow by Step 4: Q_proton = 2(+2/3) +
(−1/3) = +1; Q_neutron = 2(−1/3) + (+2/3) = 0. These are
real, well-defined per-arc fractional contributions on the
literal-arc curve.

**The smooth modulated clover** ([sheet-proton/work/modulated-clover.md](../sheet-proton/work/modulated-clover.md))
replaces the piecewise-arc curve with a smooth tube-function
cross-section. The smooth family **cannot literally reach the
+2/3, −1/3 per-piece ideals** — modulated-clover.md §2.3 records
that the smooth family caps at Q_maj ≈ 0.63 < 2/3, with the
+2/3 ideal living only at the κ → ∞ cusp limit of the
literal-arc clover. The integer baryon-charge totals (+1, 0)
are recovered on the modulated clover by **tuning the
modulation amplitudes** (a 2-condition fit over the sin- and
cos-harmonics, per modulated-clover.md §4.5) so that the
closed-track integrals come out correct, not by per-piece arc
accounting.

So the chain Steps 1–5 applies uniformly *as the framework for
integrated track charge* — the closed-track totals via
Gauss–Bonnet are robust on both constructions. The *per-piece
fractional decomposition* with the specific values ±2/3, ±1/3
belongs specifically to the literal-arc clover; the smooth
modulated clover approximates these per-piece ideals (with
known cap below 2/3) while recovering the integer totals by
modulation tuning.

**Citation guidance.** Downstream projects citing H1 should
make the underlying construction explicit:

- **Literal-arc clover** — cite H1 with the per-arc 240°/120°
  → ±2/3, ±1/3 decomposition.
- **Smooth modulated clover** — cite H1 for the *integrated
  track charge* (Steps 1, 2, 5 as the local density picture;
  Steps 3, 4 for the closed-track integer total via
  Gauss–Bonnet); the per-piece ±2/3, ±1/3 values are an
  approximated ideal, not a literal calculation result.

**Status.** The chain is complete under G1. The framework
already supplies G1's content for the **uniform-circulation
case** (charge per radian = e/(2π), per F12 §F3, T12 main
premise); G1 extends this to pointwise locality for varying κ_g.
That extension is currently flagged as a named hypothesis with
two identified promotion routes, not as derived.

---

## 7. Angular-momentum reading of rest mass

The integer winding number n of a single-direction mode on a
compact loop of radius R_u is the **quantized angular momentum**
of the standing wave around the loop:

<!-- J_u = R_u · p_u = ℏn -->
$$
J_u \;=\; R_u \cdot p_u \;=\; \hbar\,n
$$

Same form as the orbital angular momentum spectrum of standard
quantum mechanics, here arising from periodicity rather than
from the angular-momentum eigenvalue problem in 3D space.

The metric-mass rest-mass identification m_n = ℏ|n|/(R_u c)
rearranges to:

<!-- m_n · R_u · c = ℏ |n| = |J_u| -->
$$
m_n \cdot R_u \cdot c \;=\; \hbar\,|n| \;=\; |J_u|
$$

— **rest mass × compact radius × c = angular momentum about the
loop**. Equivalently, the rest energy m_n c² equals the angular
momentum |J_u| times the loop circumnavigation rate ω_rot = c/R_u
(massless-on-a-ring identity E = pc, applied around the loop).

**Embedding caveat.** "Angular momentum about the loop's centre"
requires the compact direction to be embedded in a plane with a
definite rotation axis. What is embedding-independent is that n
labels how rapidly the wave's phase changes as u advances along
the loop — mathematically, n is the eigenvalue of the momentum
operator −iℏ ∂/∂u acting on the mode functions. The
angular-momentum *labelling* of n adds physical intuition under
the natural embedding (rolled-up cylinder) but is not
load-bearing for the mass identification, which uses only |n|.

**2D extension.** On a 2D compact sheet each direction carries
its own linear compact momentum and corresponding angular
momentum:

<!-- p_w = ℏm/R_w, p_u = ℏn/R_u;  J_w = ℏm, J_u = ℏn -->
$$
p_w = \frac{\hbar\,m}{R_w},\;
p_u = \frac{\hbar\,n}{R_u};
\qquad
J_w = \hbar\,m,\; J_u = \hbar\,n
$$

The Pythagorean mass formula combines the two **compact linear
momenta** in quadrature: (m_{(m,n)} c)² = p_w² + p_u². The
J-as-2-vector reading collapses to "angular-momentum vector
magnitude" only at the isotropic point R_u = R_w; for generic
R_u ≠ R_w, the quadrature uses p_i = J_i/R_i (linear momenta,
weighted by inverse radius), not J_i itself.

The full development with the rotor-vs-Planck-Einstein
distinction is in [work/angular-momentum-as-mass.md](work/angular-momentum-as-mass.md).

**Downstream use.** The conservation-as-momentum direction in
ma-domain work, which is testing whether several SM conserved
quantities are some form of compact-direction momentum, should
cite F5 and the 2D extension above as the per-direction
angular-momentum reading. The reading is a vocabulary
restatement of the rest-mass identification (it produces no new
formula) but provides the physical intuition that compact-
direction momentum = angular momentum about the loop, and
externally appears as inertia.

---

## 8. Picture B (the bare 2D harmonic oscillator) — a noted-but-not-used alternative

The earlier work-file analysis entertained a separate physical
model, called **picture B**, as a source of continuous internal
symmetries beyond what picture A carries. Picture B is the bare
2D harmonic oscillator with quadratic confining potential:

- **Hamiltonian (the energy operator):**
  H = (p_w² + ω_w² w²)/2 + (p_u² + ω_u² u²)/2 — two oscillators
  side by side, each one a "mass on a spring" with its own
  frequency.
- **Mode functions:** Hermite functions on ℝ² (the standard
  harmonic-oscillator wavefunctions; they decay at infinity and
  are *not* periodic in any direction).
- **Spectrum:** E = ℏω_w(m + 1/2) + ℏω_u(n + 1/2) — energy adds
  linearly across the two oscillators.
- **State space structure:** *two* ladders of creation/annihilation
  operators, (a_w, a_u), one per oscillator — not one ladder per
  mode as in picture A.
- **Continuous symmetries at ω_u = ω_w:** U(1) × SU(2). The SU(2)
  is the continuous mixing of the two ladder operators that
  shows up because the two oscillators have the same frequency.

Picture B and picture A share the same integer-pair labels (m, n)
at the one-quantum level — both have one basis state per (m, n) —
but they differ in essentially everything else:

- Hamiltonian (confining potential vs wave equation on a
  compact substrate),
- mode-function geometry (Hermite functions on the real line vs
  plane waves on the compact substrate),
- multi-quantum state-space structure (two ladders vs one ladder
  per mode),
- energy formula (linear additive vs Pythagorean), and
- continuous-symmetry algebra (SU(2) vs discrete D_4 at
  isotropy).

They are **different physical systems**, not different readings
of the same system.

**The framework does not currently borrow from picture B for any
target.** For each candidate target, the table below records the
A-native route status (per §5) and what picture B borrowing
would deliver. "Structural analog" rather than "gauge theory" is
the target type for every entry; promoting to a full gauge
theory requires a separate gauging step neither A-native nor
borrowing routes supply on their own.

| Target | A-native route (status) | Picture B borrowing (would deliver) |
|---|---|---|
| Spin-1/2 (two-state) | Half-twist windings / spin structure (candidate; foundationally incomplete on both legs — see §5.1) | Continuous SU(2) algebra at ω_u = ω_w, *not* spin-1/2 dynamics |
| Color (3-fold confinement-like fractional charge) | Ch 8 §7's k = 3 component-link mechanism (chapter-grade, structural analog only — *not* gauge SU(3)) | Continuous SU(3) algebra at 3D isotropy, *not* gauge SU(3) |
| Weak isospin SU(2)_L (chiral gauge) | No committed mechanism (chirality structure required either way) | Continuous SU(2) algebra at ω_u = ω_w; *not* chiral, *not* gauged |

The A-native routes are either chapter-grade (color, as
structural analog) or candidate with known gaps (spin-1/2).
Picture B borrowing is therefore **available as a future
option** but **not load-bearing** for any current target. In no
case does the borrowing alone construct gauge SU(N) — promotion
to a Yang–Mills theory is a separate step the framework does
not have a mechanism for.

**When picture B borrowing (B1) would become appropriate.** If a
downstream candidate target genuinely requires continuous SU(N)
structure and no A-native route covers it after honest
investigation, the borrowing route is available. Two conditions
have to be met:

1. The modelling target needs continuous SU(N), not a discrete
   approximation, and not a topological/half-twist alternative.
2. No A-native construction on picture A's substrate has been
   found that produces the target — i.e., the A-native route has
   been investigated and ruled out, not just bypassed.

If both are met, [work/ho-bridge-2d.md](work/ho-bridge-2d.md)
records what the borrowing involves and its limits; the
**B1 borrowing premise** (named in §3) should be cited
explicitly so that downstream readers see the status flag.

**Current status of the two conditions for each candidate
target** (per §5's table):

| Target | Condition 1 (target needs continuous SU(N))? | Condition 2 (A-native ruled out)? | B1 currently appropriate? |
|---|---|---|---|
| Spin-1/2 | Open — depends on which MaSt reading | A-native candidates exist with known gaps; not ruled out | **No** |
| Color (structural analog) | Structural analog does not require continuous SU(3); Ch 8 k = 3 mechanism is chapter-grade | Ch 8 k = 3 covers the structural analog | **No** |
| Weak isospin SU(2)_L | Would require continuous SU(2) plus chirality plus gauging | No A-native committed yet; A-native not investigated enough to be ruled out | **No** |

Until both conditions are met for some specific target, the
framework stays in picture A and does not cite B1.

---

## 9. Hand-off to downstream projects

Citable anchors for downstream files that lean on this foundation:

| Downstream context | Cite |
|---|---|
| Modulated-clover constructions reading per-arc fractional charge ([sheet-proton/work/modulated-clover.md](../sheet-proton/work/modulated-clover.md); ma-domain analogues) | §6 (H1 under G1) |
| Conservation-as-momentum analyses (rest mass = compact-direction angular momentum) | §7 (F5 + 2D extension) |
| Spin-1/2 candidates via A-native half-twist routes (candidate; foundational gaps per §5.1) | §5 + §5.1; [work/angular-momentum-as-mass.md](work/angular-momentum-as-mass.md) Open Question 1 |
| Color's structural analog (3-fold fractional charge with confinement-like inseparability) via Ch 8 §7's k = 3 | [Ch 8 §7](08-shear-and-fractional-charge.md) directly; §5 for the structural-analog framing |
| Color via picture B borrowing at 3D isotropy (B1; *not currently appropriate* per §8 — A-native covers the structural analog) | §8; [work/higher-order-charges.md](work/higher-order-charges.md) for the full development (not destined for metric-charge content) |
| Modelling particles as HO complexes (resonance-spectrum view of the wave on a shaped substrate) | §4 (the shape ↔ HO-complex duality, both in picture A) |
| Wavepacket-localisation arguments | F7 in §2 (coherent states give localisation but not knot-trajectory tracking automatically) |

Higher-order extensions (N compact directions, SU(N) candidate
for color) are developed in
[work/higher-order-charges.md](work/higher-order-charges.md),
which is explicitly forward-looking and aimed at ma-domain and
metric-binding. That file is not chapter-grade for metric-charge
and is not cited as such here; downstream projects that want the
full N-direction structural picture should cite the work file
directly.

---

## What this appendix establishes

| Claim | Status |
|---|---|
| Picture A (the wave equation on the compact substrate) is the framework's actual physics; chapters 1–10 are entirely in picture A | Recap |
| Seven citable foundation results (F1–F7), all in picture A | Established in chapters 1–10 and corresponding work files |
| Per-arc fractional charge (H1) follows from picture A under one named hypothesis G1 (local-leakage identification) | Established under G1; G1 partially supported (uniform-circulation case in grid/) with locality the remaining gap; two promotion routes identified |
| H1's per-piece ±2/3, ±1/3 decomposition is *literal* on the literal-arc clover and an *approximated ideal* on the smooth modulated clover (which caps at Q_maj ≈ 0.63); both constructions recover the integer closed-track totals | Established under G1 (per §6) |
| Shape and HO-complex are dual views of picture A — the HO complex is the mode-basis decomposition (not a small-oscillation step, since the wave equation is already linear) | Established |
| Picture A on T² carries U(1) × U(1) (continuous, A-native) plus discrete D_4 at R_u = R_w; no continuous SU(2) | Established |
| SU(N)-like *structural analog* targets for downstream modelling have two route options: A-native (topological/half-twist/Ch 8 k-mechanism) or picture B borrowing (B1). Neither route constructs gauge SU(N) on its own — promoting to a Yang–Mills theory is a separate step the framework lacks a mechanism for | Established |
| Picture B (the bare 2D harmonic oscillator) is available as a future borrowing option (B1) but is not currently used for any target; A-native routes cover the *structural-analog* version of color (Ch 8 k = 3, mature) and are candidate-with-gaps for spin-1/2 (per §5.1) | Stated |
| Hypothesis ladder: G1 is a substantive physical claim (specific functional form for a physical density); B1 is a modelling-vocabulary premise (borrowing the algebra of a different physical system). They sit at different rungs and should be cited at the right level | Stated (per §3 ladder) |

## What this appendix does *not* do

- It does not introduce a new derivation or alter any result of
  chapters 1–10.
- It does not commit the framework to picture B borrowing (B1)
  for any target. B1 is recorded as available, not as adopted.
- It does not derive G1. G1 remains a named hypothesis; the
  per-arc chain is complete *under* G1, not unconditionally.
- It does not construct gauge SU(N) (Yang–Mills theory with
  gauge bosons, covariant derivative, running coupling) for any
  target. The framework's color and weak-isospin targets are
  treated as *structural analogs* (fractional-charge
  inseparability, multi-component mixing); the gap to a full
  gauge theory remains outside scope.
- It does not identify any specific MaSt-correspondence target
  (electron, proton, neutrino, quark). Those are downstream
  comparison tasks, not appendix content.

## Hand-off

This appendix is a stable citation target for the downstream
projects listed in §9. Updates to the underlying work files do
not require updates to citations of F1–F7 or H1–H2; the appendix's
F- and H-numbers are the stable interface.
