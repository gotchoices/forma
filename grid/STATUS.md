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

### Backlog: Stiffness analysis (optional)

Repackage the impedance/stiffness/bubble-radius material from
the original dialog.  This reinterprets existing results — it
does not derive anything new.

- [ ] EM stiffness: ε₀ and μ₀ as orthogonal spring constants
- [ ] Gravitational stiffness: c⁴/(8πG) as force
- [ ] Bubble radius and Schwarzschild connection
- [ ] Both stiffnesses from one lattice: EM (mechanical) vs gravity (statistical)

**Deliverable:** [stiffness.md](stiffness.md) *(if needed)*

### Backlog: SI restoration (optional)

- [ ] SI units for Maxwell derivation (maxwell.md)

---

## Current focus

**Phases 1–4 complete.**  Core GRID work is done.

**Parallel tracks:**
- [lattice-geometry.md](lattice-geometry.md) — can ζ follow
  from packing geometry?  Leading candidate: 4D simplicial
  (pentachoron, ζ = 1/6), or 2D sheets give ζ = 1/4.
- [compact-dimensions.md](compact-dimensions.md) — **complete** —
  2D triangular lattices wrapped into tori produce a discrete
  but dense α spectrum.  Conclusion: α is a designer's choice
  within available discrete steps; the lattice geometry does
  not uniquely determine it.  Noteworthy: weak coupling
  (1/α > 100) requires a minimum of 3 cells (6 triangles).
- [sim-gravity/](sim-gravity/) — **complete** — embedded
  rigid body in spring lattice gives edge strain ε ∝ 1/r²
  (R² = 0.9999).  This is the 2D *elastic* power law
  (Eshelby), not the 2D *gravitational* power law (1/r).
  Key finding: mechanical elasticity ≠ gravity; the
  thermodynamic route (Jacobson) is genuinely necessary.
  See [sim-gravity/README.md](sim-gravity/README.md).
- [sim-gravity-2/](sim-gravity-2/) — **scalar baseline
  complete** — scalar field on the same lattice gives
  dφ/dr ∝ 1/r (p = 1.012, R² = 0.999) vs sim-gravity's
  vector 1/r² (p = 2.0).  Confirms: scalar (entropic) field
  → gravitational power law.  String-register model next.

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
