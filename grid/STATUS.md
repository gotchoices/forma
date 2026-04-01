# GRID Status

**Sub-project:** Geometric Relational Interaction Domain
**Parent:** [Project STATUS](../STATUS.md)
**Started:** 2026-03-31

---

## Roadmap

### Phase 1: Foundations ✅

Establish the axiom set, notation, and free parameters.

- [x] Define the constants: ζ (resolution, geometrically derived) and α (coupling, measured)
- [x] Write axioms A1–A6
- [x] Document what the axioms produce and what they don't
- [x] Identify open questions at the foundations level

**Deliverable:** [foundations.md](foundations.md)

### Phase 2: Maxwell from the lattice ✅

Derive all four of Maxwell's equations from axioms A1–A4 and A6,
cleanly and without importing any electrodynamics.

- [x] Continuum limit of phase field → gradient ∂_μθ
- [x] Gauge invariance demands compensating connection A_μ
- [x] Covariant derivative D_μθ = ∂_μθ − eA_μ
- [x] Field tensor F_μν = ∂_μA_ν − ∂_νA_μ from plaquette holonomy
- [x] Decompose F_μν into E and B using (1,3) signature
- [x] Electromagnetic action from coupling constant κ = 1/(4πα)
- [x] Euler-Lagrange → inhomogeneous Maxwell: ∂_μ F^μν = J^ν
  - [x] ν = 0 → Gauss's law: ∇·E = ρ
  - [x] ν = j → Ampère's law: ∇×B − ∂E/∂t = J
- [x] Bianchi identity → homogeneous Maxwell: ∂_{[μ} F_{νρ]} = 0
  - [x] One time index → Faraday's law: ∇×E + ∂B/∂t = 0
  - [x] Three spatial → No monopoles: ∇·B = 0
- [x] Charge quantization from phase periodicity (topological vortices)
- [x] Charge conservation ∂_μ J^μ = 0 as theorem
- [x] Axiom audit: which axioms did what
- [ ] SI restoration (deferred — working in natural units)

**Deliverable:** [maxwell.md](maxwell.md)

### Phase 3: Deriving G ✅

Derive Newton's gravitational constant from the resolution
parameter ζ via Jacobson's thermodynamic argument.

- [x] State axioms used (A1, A2, A5) and additional inputs
- [x] Local Rindler horizons from causal structure
- [x] Entropy bound from ζ: δS = ζ δA
- [x] Unruh temperature: T = κ/(2π) (flagged as additional input)
- [x] Energy flux through horizon: ∫ T_ab k^a k^b κλ dλ dA
- [x] Area change from Raychaudhuri equation (kinematic, not GR)
- [x] Clausius relation combines energy flux with entropy change
- [x] Null-vector identity → T_ab = −(ζ/2π) R_ab + f g_ab
- [x] Conservation + Bianchi identity → fixes f, gives Λ for free
- [x] Einstein equations emerge: G_ab + Λg_ab = (2π/ζ) T_ab
- [x] Read off G = 1/(4ζ) = 1 in natural units
- [x] Spacetime stiffness: c⁴/(8πG) = ζ/(2π) = 1/(8π)
- [x] SI restoration (note: G_SI consistent but not independently predicted)
- [x] Honesty check: circularity, Unruh, Raychaudhuri
- [ ] Connection to EM stiffness through shared lattice (deferred to stiffness.md)

**Deliverable:** [gravity.md](gravity.md)

### Phase 4: Synthesis ✅

Summarize what GRID establishes and what remains open.  Bridge to MaSt.

- [x] Both Maxwell and Einstein from one lattice, one geometric constant (ζ), one measured input (α)
- [x] EM = dynamics of phases; gravity = thermodynamics of configurations
- [x] Two knobs, two mechanisms: EM from dynamics, gravity from statistics
- [x] The hierarchy between EM and gravity: what ζ and α imply
- [x] Interface with MaSt: what GRID provides, what MaSt adds
- [x] Open questions and possible future work
- [x] Energy budget question
- [x] Honest accounting of what was NOT derived

**Deliverable:** [synthesis.md](synthesis.md)

### Phase 5: Hexagonal lattice & simulations

The hexagonal (honeycomb / wye) lattice has emerged as a
potentially better substrate than the triangular (delta)
lattice: flexible with fixed edges, lower reflection at
junctions, curvature from pentagonal defects.

- [x] **sim-maxwell on hexagonal lattice (N=3)** — single
  edge pulses propagate forward (dir=0.53 vs 0.24 tri).
  Speed comparable (0.73 vs 0.71).  Hexagonal is better
  for single quanta; triangular better for coherent fronts.
- [x] **sim-schwarzschild** — horizon is NOT a lattice
  failure (consistent with GR: coordinate singularity).
  Pentagon density saturates at r_crit = (1.24 r_s)^(1/3).
  Minimum BH mass ≈ 0.56 Planck masses.  Physical
  singularity (r=0) IS a lattice failure (K → ∞).
- [x] sim-maxwell follow-up: superposition (two crossing
  wavefronts) — **perfect** on both lattices (residual
  ~10⁻¹⁵, machine epsilon).  Waves pass through each
  other with zero distortion.
- [ ] sim-maxwell follow-up: plaquette circulation
  measurement (test zigzag-circulation cancellation).
  *Polish — tests the mechanism behind an already-confirmed
  result.  Would deepen understanding but doesn't answer
  any open question.*
- [ ] sim-maxwell follow-up: E/B field identification in
  propagating wave.  *Polish — would show the wave IS an
  EM wave (transverse, with B = plaquette circulation).
  Satisfying but the theoretical derivation in maxwell.md
  already establishes this.*
- [ ] sim-maxwell follow-up: dispersion relation (speed vs
  wavelength).  *Low priority — characterizes Planck-scale
  corrections.  Only matters if we ever make sub-Planck
  predictions.*
- [ ] Update lattice-geometry.md for hexagonal perspective.
  *Documentation — no new results.*
- [ ] Re-run compact-dimensions wrapping with hexagonal
  lattice (different α spectrum?).  *Low priority — we
  already concluded α is a designer's choice.  Hexagonal
  wrapping would change the discrete steps but not the
  conclusion.*
- [ ] Evaluate whether hexagonal makes A4 (gauge invariance)
  derivable rather than axiomatic.  *HIGH VALUE if it works
  — this is the only remaining item that could reduce the
  axiom count.  But it is a theoretical argument, not a
  simulation, and the path is unclear.*
- [ ] **sim-torus-limits** — is there a min/max radius for
  rolling a hexagonal sheet into a torus without shearing?
  *Probably low value after sim-schwarzschild showed the
  hexagonal lattice flexes freely without shearing.  The
  same flexibility that makes the horizon non-special also
  means torus bending is free.  Only topology (periodicity)
  would constrain sizes, and that's already covered by
  compact-dimensions.md.*
- [ ] **sim-alpha-chord** — can a specific initial excitation
  pattern on the grid launch a proton+electron pair?
  *Highly ambitious, long-term.  Requires solving the
  inverse problem: MaSt particle → lattice excitation.
  Not tractable until GRID ↔ MaSt interface is much better
  understood.  Aspirational.*

**Deliverables:** [hexagonal.md](hexagonal.md),
[sim-schwarzschild/](sim-schwarzschild/), updated sim-maxwell

### Backlog: Stiffness analysis (optional)

Repackage the impedance/stiffness/bubble-radius material from
the original dialog.  This reinterprets existing results — it
does not derive anything new.

*Low priority — repackaging, not discovery.  Might be useful
if writing a paper, but adds no new capability.*

- [ ] EM stiffness: ε₀ and μ₀ as orthogonal spring constants
- [ ] Gravitational stiffness: c⁴/(8πG) as force
- [ ] Bubble radius and Schwarzschild connection
- [ ] Both stiffnesses from one lattice: EM (mechanical) vs gravity (statistical)

**Deliverable:** [stiffness.md](stiffness.md) *(if needed)*

### Backlog: SI restoration (optional)

*Bookkeeping — no physics content.  Only needed if presenting
to an SI-focused audience.*

- [ ] SI units for Maxwell derivation (maxwell.md)

---

## Current status

**Phases 1–5 substantially complete.**  Core GRID work is done.
All major derivations and simulations are finished.  Remaining
Phase 5 items are polish, confirmation, or speculative
extensions — none are critical to the framework.

### Completed studies

| Study | Key result |
|-------|-----------|
| [lattice-geometry.md](lattice-geometry.md) | ζ = 1/4 from 3D tetrahedral packing (Model B) |
| [compact-dimensions.md](compact-dimensions.md) | α is a designer's choice within dense discrete steps |
| [sim-gravity/](sim-gravity/) | Elastic lattice gives 1/r² (elastic, not gravitational) — confirms Jacobson route is necessary |
| [sim-gravity-2/](sim-gravity-2/) | Scalar + string-register: both give 1/r force (p ≈ 1.01) — entropic gravity confirmed |
| [sim-maxwell/](sim-maxwell/) | Directional propagation from geometry alone (speed ≈ 0.70, no Maxwell input) |
| sim-maxwell (hexagonal) | Single-edge forward propagation (hex dir=0.53 vs tri=0.24) |
| sim-maxwell (superposition) | Perfect superposition on both lattices (residual ~10⁻¹⁵) |
| [sim-schwarzschild/](sim-schwarzschild/) | Horizon is NOT a lattice failure; min BH mass ≈ 0.56 m_P; singularity IS |
| [hexagonal.md](hexagonal.md) | Hexagonal lattice: flexible, lower reflection, curvature from defects |

### What the framework establishes

- **Maxwell's equations** from lattice gauge theory (A1–A4, A6)
- **Einstein's equations + G** from lattice thermodynamics (A1, A2, A5)
- **Directional wave propagation** from geometry alone (no Maxwell input)
- **Linear superposition** exact on both triangular and hexagonal lattices
- **1/r entropic gravity** on the lattice (2D confirmed)
- **Event horizon** = coordinate singularity (lattice accommodates it)
- **Physical singularity** = lattice failure (curvature exceeds pentagon capacity)
- **Minimum BH mass** ≈ 0.56 Planck masses (geometric prediction)

### Remaining mysteries

| Mystery | Importance | Notes |
|---------|-----------|-------|
| Why α ≈ 1/137 | The one unsolved parameter | Not a framework deficiency — α is a measured input, like the speed of light in SI |
| Value of Λ | Open | Appears as integration constant; the famous "cosmological constant problem" |
| Particle masses | MaSt's territory | GRID provides the substrate; MaSt provides the compact geometry |
| Gauge invariance from hex geometry? | High if achievable | Could reduce axiom count — theoretical, not simulation |

---

## Dependencies

| GRID needs from MaSt | MaSt needs from GRID |
|----------------------|----------------------|
| Nothing — GRID is upstream | Maxwell's equations (derived, not assumed) |
| (α is a shared input, not exchanged) | The value and meaning of G |
| | Connection between EM and gravity |

---

## Decision log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-03-31 | Created as `grid/`, not a study | GRID is foundational — upstream of MaSt, not a focused investigation within it |
| 2026-03-31 | Variable ζ for resolution (not q) | q is overloaded in MaSt studies (charge, winding number) |
| 2026-03-31 | Two free parameters: ζ and α | Minimal set.  Whether they reduce to one is an open question, not an assumption |
| 2026-03-31 | 4D simplicial as leading packing candidate | Pentachoron is the minimal 4D polytope; geometry may determine ζ.  (1,3)-split simplicial kept as alternative (matches BH factor 1/4) |
