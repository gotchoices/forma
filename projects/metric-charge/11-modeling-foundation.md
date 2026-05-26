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
  SU(3) is the gauge group of QCD's colour charge.

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
| F2 | The Pythagorean answer is *also* obtainable sequentially: treat m_u as a 1D rest mass, then add a second compact direction's KK momentum p_w; the relativistic dispersion gives m² = m_u² + (p_w/c)². The sequential and joint quantisations give identical results. | [work/ho-bridge-2d.md](work/ho-bridge-2d.md) "Hypothesis A" |
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
they are derived under one explicit, falsifiable hypothesis each,
in the same status pattern as Ch 8 §7 (which carries k as input)
and metric-mass Ch 9 (which carries the HO translation as
bridge).

| # | Result | Source | Hypothesis |
|---|---|---|---|
| H1 | The local EM charge density per unit arc length along a curve on the bent substrate is dQ/ds = (1/2π)·κ_g, where κ_g is the curve's geodesic curvature. Per-arc fractional charge follows: Q(γ) = (1/2π) ∫_γ κ_g ds, with Q_lobe = +2/3, Q_saddle = −1/3, summing to integer totals by Gauss–Bonnet. | [work/per-arc-curvature-as-charge.md](work/per-arc-curvature-as-charge.md) | **G1** (the local-leakage identification — see §6) |
| H2 | Continuous internal symmetries beyond U(1) × U(1) at radial isotropy points (continuous SU(2) at R_u = R_w on T²; continuous SU(N) at higher dimensions) are *available as a modelling tool* by borrowing the algebra of the bare-2D-HO-with-quadratic-potential as a *different* physical system whose one-quantum spectrum labels match. The borrowing does *not* upgrade picture A's discrete D_4 to continuous SU(2). | [work/ho-bridge-2d.md](work/ho-bridge-2d.md); [work/higher-order-charges.md](work/higher-order-charges.md) | **borrowing premise** (see §8) |

H1 and H2 are flagged with the hypothesis or premise they carry;
any downstream citation should preserve the flag.

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
- **HO-complex view.** Near equilibrium, the wave equation on
  any shape linearises into a set of normal modes, each behaving
  as a one-dimensional harmonic oscillator with a frequency set
  by the shape's parameters. A particle is a state in this
  multi-mode oscillator complex. The mode frequencies *encode*
  the shape.

**The two views are not competitors.** The HO-complex is the
small-oscillation limit of the wave-on-shape; the shape
determines the HO frequencies; the HO frequencies are what
probes (scattering, decay spectroscopy) actually measure as the
resonance structure of the particle. Either view is valid; each
is useful in a different domain.

| View | Domain | Calculational tool |
|---|---|---|
| Photon-on-shape (wave equation on substrate) | Substrate-level derivation; topology; closure; gauge identification | The wave equation itself, separation of variables, Gauss–Bonnet on the manifold |
| HO-complex (small-oscillation normal modes) | Resonance spectrum; mode-by-mode analysis; probe-couplings; matrix elements | Normal-mode decomposition of the linearised wave equation; Hermite-like expansions around the equilibrium configuration |

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
continuous SU(N) structure: spin (SU(2)), weak isospin (SU(2)),
color (SU(3)). Picture A does not supply continuous SU(N) for any
of these. Downstream work that wants SU(N) has two routes:

- **A-native topological route.** Construct the SU(N) target
  from picture A's available structure plus topology: half-twist
  windings on the substrate (as in the modulated-clover work),
  spin structures on the compact manifold (the standard
  differential-geometry construction that lets a manifold
  support half-integer-spin fields by allowing the wavefunction
  to flip sign around a closed loop), or the k = N
  component-link mechanism of
  [Ch 8 §7](08-shear-and-fractional-charge.md) (already
  chapter-grade, gives k = 3 fractional charge with
  confinement-like behaviour). This route stays in picture A.
- **Borrowing route.** Borrow the SU(N) algebra from a *different*
  physical system whose spectrum labels match (see §8). This
  route leaves picture A and brings the borrowing's status flags.

The framework currently has at least one A-native route in hand
for color (Ch 8's k = 3 mechanism) and a candidate A-native route
for spin (half-twist windings; see [work/angular-momentum-as-mass.md](work/angular-momentum-as-mass.md)
Open Question 1, which records the two MaSt readings of spin-1/2).
Picture A is therefore not a dead end for SU(N) modelling; it
just requires going topological rather than continuous-symmetric
at the geometric level.

---

## 6. Per-arc fractional charge under G1

Sheet-proton and modulated-clover constructions in downstream
work read fractional charge along an arc as the integrated
geodesic curvature normalised by 2π:

<!-- Q(γ) = (1/2π) ∫_γ κ_g ds -->
$$
Q(\gamma) \;=\; \frac{1}{2\pi}\,\int_\gamma \kappa_g(s)\,ds
$$

A complete simple closed plane curve gives Q = 1 by Gauss–Bonnet
(the total turning is 2π). An incomplete arc gives a fractional
partial sum: Q_lobe = +2/3 for a 240° lobe arc; Q_saddle = −1/3
for a 120° saddle arc. **Per-arc fractional contributions with
sign tracking convex/concave geometry.**

The bridge from this per-arc reading to the framework's existing
charge mechanism is developed in
[work/per-arc-curvature-as-charge.md](work/per-arc-curvature-as-charge.md)
under one explicit working hypothesis:

> **G1 (local-leakage identification).** Bending the grid's
> hexagonal cylinder lattice into a 2D surface embedded in 3D
> produces, in the continuum limit, a local normal-E-field
> leakage density along any curve on the surface equal to
> (1/2π) κ_g(s).

G1 carries the load-bearing piece — extension of an already-
established uniform-circulation premise
([grid/charge-emergence.md](../grid/charge-emergence.md);
[grid/sim-impedance/F12](../grid/sim-impedance/F12-charge-per-radian.md),
[T12](../grid/sim-impedance/T12-charge-per-radian.md)) to
pointwise locality on curves with varying κ_g. Two promotion
routes are identified in the work file: locality from the
discrete lattice (grid-primitive-level addition), or a
lighter Berry-phase / holonomy route that may close locality
automatically.

**What follows under G1 (the chain summarised; full
derivation in the work file):**

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
  Q_proton = 2(+2/3) + (−1/3) = +1; Q_neutron = 2(−1/3) + (+2/3)
  = 0.
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

**Status.** The chain is complete under G1. The framework
already supplies G1's content for the **uniform-circulation
case** (charge per radian = e/(2π), per F12 §F3, T12 main
premise); G1 extends this to pointwise locality for varying κ_g.
That extension is currently flagged as a named hypothesis with
two identified promotion routes, not as derived.

**Downstream use.** Modulated-clover constructions in
[sheet-proton/work/modulated-clover.md](../sheet-proton/work/modulated-clover.md)
and any ma-domain-side modulated-clover analogue that read per-arc
fractional charge should cite **H1 under G1**. The status flag
ensures readers know the chain rests on G1 and that promotion
requires deriving G1 by one of the two routes.

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
target.** For every continuous-symmetry candidate the framework
has on the table, an A-native alternative exists:

| Target | A-native route | Picture B borrowing |
|---|---|---|
| Spin-1/2 | Half-twist windings, (1/2, 1)-style configurations (modulated-clover); spin structure on the compact manifold | SU(2) at ω_u = ω_w |
| Color SU(3) | Ch 8 §7's k = 3 component-link mechanism (chapter-grade, gives 1/3 fractional charge with confinement-like inseparability) | SU(3) at 3D isotropy |
| Weak isospin SU(2)_L | No committed mechanism (chirality structure required either way) | SU(2) at ω_u = ω_w plus chirality + gauging |

The A-native routes either are already chapter-grade (color) or
are the more developed candidates in current work (spin). Picture
B borrowing is therefore **available as a future option** but
**not load-bearing** for any current target.

**When picture B borrowing would become appropriate.** If a
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
**borrowing premise** (H2 in §3) should be cited explicitly so
that downstream readers see the status flag.

Until those conditions are met, the framework stays in picture A.

---

## 9. Hand-off to downstream projects

Citable anchors for downstream files that lean on this foundation:

| Downstream context | Cite |
|---|---|
| Modulated-clover constructions reading per-arc fractional charge ([sheet-proton/work/modulated-clover.md](../sheet-proton/work/modulated-clover.md); ma-domain analogues) | §6 (H1 under G1) |
| Conservation-as-momentum analyses (rest mass = compact-direction angular momentum) | §7 (F5 + 2D extension) |
| Spin-1/2 candidates via A-native half-twist routes | §5 ("A-native topological route"); [work/angular-momentum-as-mass.md](work/angular-momentum-as-mass.md) Open Question 1 |
| Spin-1/2 candidates via picture B borrowing | §8 (borrowing premise H2) |
| Color via Ch 8 §7's k = 3 mechanism | [Ch 8 §7](08-shear-and-fractional-charge.md) directly; §5 for the structural framing |
| Color via picture B borrowing at 3D isotropy | §8; [work/higher-order-charges.md](work/higher-order-charges.md) for the full development (not destined for metric-charge content) |
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
| Shape and HO-complex are dual views of picture A — the HO complex is the small-oscillation normal-mode decomposition of the wave equation on the shape | Established |
| Picture A on T² carries U(1) × U(1) (continuous, A-native) plus discrete D_4 at R_u = R_w; no continuous SU(2) | Established |
| Continuous-SU(N) targets for downstream modelling have two route options: A-native (topological/half-twist/Ch 8 k-mechanism) or picture B borrowing | Established |
| Picture B (the bare 2D harmonic oscillator) is available as a future borrowing option but is not currently used for any target; A-native routes cover the current candidates | Stated |

## What this appendix does *not* do

- It does not introduce a new derivation or alter any result of
  chapters 1–10.
- It does not commit the framework to picture B borrowing for
  any target. The borrowing is recorded as available, not as
  adopted.
- It does not derive G1. G1 remains a named hypothesis; the
  per-arc chain is complete *under* G1, not unconditionally.
- It does not identify any specific MaSt-correspondence target
  (electron, proton, neutrino, quark). Those are downstream
  comparison tasks, not appendix content.

## Hand-off

This appendix is a stable citation target for the downstream
projects listed in §9. Updates to the underlying work files do
not require updates to citations of F1–F7 or H1–H2; the appendix's
F- and H-numbers are the stable interface.
