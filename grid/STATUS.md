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

**Phases 1–3 complete.**  Next: Phase 4 (stiffness analysis).

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
