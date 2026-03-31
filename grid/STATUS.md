# GRID Status

**Sub-project:** Geometric Relational Interaction Domain
**Parent:** [Project STATUS](../STATUS.md)
**Started:** 2026-03-31

---

## Roadmap

### Phase 1: Foundations ✅

Establish the axiom set, notation, and free parameters.

- [x] Define the two knobs: ζ (resolution) and α (coupling)
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

### Phase 3: Deriving G

Derive Newton's gravitational constant from the resolution
parameter ζ, in both natural and SI units.  No circular reasoning.

- [ ] Entropy bound from ζ: S = ζ · A (Planck units)
- [ ] Unruh temperature: T = ℏa/(2πck) for accelerating observers
- [ ] Jacobson's argument: δQ = TdS on local Rindler horizons
- [ ] Energy flux: ∫ T_μν ξ^μ dΣ^ν through the horizon
- [ ] Einstein equations emerge as thermodynamic equation of state
- [ ] Read off G = 1/(4ζ) = 1 in natural units
- [ ] Full SI restoration: G = ℏc³/(4ζk_B) → dimensional analysis
- [ ] Verify: G = 6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² from ζ = 1/4
- [ ] Spacetime stiffness: c⁴/(8πG) ≈ 4.8 × 10⁴² N
- [ ] Connection to EM stiffness (ε₀, μ₀) through shared lattice

**Deliverable:** [gravity.md](gravity.md)

### Phase 4: Stiffness analysis

Clean up the impedance/stiffness/bubble-radius material from the
original dialog into a rigorous treatment.

- [ ] EM stiffness: ε₀ and μ₀ as orthogonal spring constants
- [ ] Gravitational stiffness: c⁴/(8πG) as force
- [ ] Pressure analysis: gravitational vs stiffness pressure on a sphere
- [ ] Bubble radius and Schwarzschild connection
- [ ] Compton wavelength × bubble radius = Planck length² (crossover)
- [ ] Planck mass as the crossover scale
- [ ] Both stiffnesses from one lattice: EM (mechanical) vs gravity (statistical)

**Deliverable:** [stiffness.md](stiffness.md)

### Phase 5: Synthesis

Summarize what GRID establishes and what remains open.  Bridge to MaSt.

- [ ] Both Maxwell and Einstein from one lattice with two knobs
- [ ] EM = dynamics of phases; gravity = thermodynamics of configurations
- [ ] Two knobs, two mechanisms: EM from dynamics, gravity from statistics
- [ ] The hierarchy between EM and gravity: what ζ and α imply
- [ ] Interface with MaSt: what GRID provides, what MaSt adds
- [ ] Open questions and possible future work

**Deliverable:** [synthesis.md](synthesis.md)

---

## Current focus

**Phases 1–2 complete.**  Next: Phase 3 (deriving G).

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
