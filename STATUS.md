# Project Status

**Mission:** Build a geometric model of fundamental particles from pure EM
energy — no fundamental charges, no point particles. See [`README.md`](README.md).

**Current model:** [**model-D**](models/model-D.md) (active — waveguide
cutoff, (3,6) proton composite, GRID integration; particle census pending).
**Latest quantitative predictions:** [**model-C**](models/model-C.md)
(six hadron masses at 0.3–1.2%, emergent neutron, neutrino mass ratio).
**All models:** [`models/README.md`](models/README.md)

**Studies roadmap:** [`studies/STATUS.md`](studies/STATUS.md)
**GRID (substrate layer):** [`grid/STATUS.md`](grid/STATUS.md) — derives Maxwell + G from a discrete lattice
**Open questions:** [`qa/INBOX.md`](qa/INBOX.md) — [`qa/README.md`](qa/README.md) for index

---

## What has been established

For full details — particle tables, mode assignments, parameter
census, plausible explanations, and negative results — see
[`models/model-C.md`](models/model-C.md).  For the framework
reference (dimensions, geometry, mechanisms, particle catalog),
see [`studies/Taxonomy.md`](studies/Taxonomy.md).

**Key results (model-C):**

- **Material Space (Ma):** 6D compact manifold (three flat periodic
  sheets), particles as standing EM waves. 10 dimensions total
  (6+3+1). Two effective free parameters (r_e, r_ν).
- **Particle spectrum:** six hadrons at 0.3–1.2% error from geometry;
  lifetime-gap correlation r = −0.84 (p = 0.009).
- **Emergent neutron:** three-sheet mode found by the solver, not
  put in by hand.
- **Neutrino masses:** Δm²₃₁/Δm²₂₁ = 33.6 from integer winding numbers.
- **Nuclear scaling law:** nuclei as Ma_p modes, d → ⁵⁶Fe at < 1%.
- **Dynamic torus:** α-impedance model, corrections O(α²) ≈ 5×10⁻⁵.
- **Plausible mechanisms** for dark matter, strong force, and CP violation.

**What model-D adds** (see [`models/model-D.md`](models/model-D.md)):

- Waveguide cutoff eliminates (1,1) ghost mode (R46).
- Proton as (3,6) composite: SU(6) moments within ~7%, m_p/3 = 313 MeV,
  three-quark structure (R47).
- Charge derived as GRID topological winding (R48).
- Finite-ε spin replaces thin-torus formula (R49).
- Proton geometry retracted as premature; all parameters swept (R50).

### Deriving G from geometry (R37 → GRID) ✅

**Resolved by GRID:** the [GRID sub-project](grid/README.md)
derives both Maxwell's equations and Einstein's field equations
from a minimal discrete lattice with one geometric constant
(ζ = 1/4) and one measured input (α). See
[`grid/synthesis.md`](grid/synthesis.md) for the full summary.

---

## What remains open

For detailed discussion of each open problem, see
[model-C limitations](models/model-C.md#limitations) and
[model-D limitations](models/model-D.md#limitations).

- **The α problem:** what determines the electron sheet shear
  s ≈ 0.01? The single most important unsolved parameter.
- **Ghost mode suppression:** waveguide cutoff (model-D) eliminates
  the worst ghost, but the full census is pending.
- **The hierarchy:** why is gravity ~10⁴⁰× weaker than EM?
- **(3,6) composite mechanics:** how three (1,2) strands bind
  into the proton.
- **Flavor:** two quark flavors (u/d) not yet explained by geometry.
- **Model-D particle census (R50):** pending — will determine whether
  model-C's hadron predictions survive under the new assumptions.

---

## Possible future investigations

| Area | Key question | Status | Reference |
|------|-------------|--------|-----------|
| Geometric phase / holonomy | Parallel transport on embedded torus → ghost selection? | Open | Q93 Path 1 |
| Dark matter from ghost modes | Charge cancellation + Compton window → mass ratio 5.4? | **Plausible** | R42, Q94 |
| Strong force from internal EM | α_s ≈ 1 as full internal field? | **Plausible** | Q95 |
| Matter–antimatter asymmetry | Shear chirality → CP violation → baryogenesis? | **Plausible** | Q97, Q32 |
| Force carriers | W/Z as transient reconfigurations; sin²θ_W ≈ 3/13? | Partial | Q96, R43 |
| Fusion as mode transition | Geometry change on Ma rather than particle collision? | **Plausible** | Q89, viz/fusion |
| Moduli potential | What selects the Ma shape (r_e, r_ν)? | Open | Q34, R37 |
| Biological coupling | Can the neutrino sheet serve as an information substrate? | Open | Q78–Q83 |
| α from first principles | Dispersive or geometric derivation of s ≈ 0.01? | Open | Q18, R34 |
