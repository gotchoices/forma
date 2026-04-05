# Model: model-B (Three tori — `ma.py`)

**Code / implementation:** [`studies/lib/ma.py`](../studies/lib/ma.py), [`studies/lib/ma_solver.py`](../studies/lib/ma_solver.py)  
**Study range (approximate):** **R26 through R38** (see [`studies/STATUS.md`](../studies/STATUS.md) Done rows 24–34)  
**Supersedes / superseded by:** Supersedes [model-A](model-A.md) (single-sheet WvM). Superseded by **model-C** ([`model-C.md`](model-C.md), when drafted) at R39, where `ma_model.py` replaces `ma.py` and adds dynamic/elliptical corrections.

---

## Summary

Model-B is the **three-sheet Ma** architecture: three flat 2-tori (Ma_e, Ma_ν, Ma_p) for electron, neutrino, and proton respectively, embedded in a single **6-dimensional** material space (the "Ma"). Every physical mode is a six-tuple **n** = (n₁, …, n₆); mass comes from the 6×6 metric, charge from Q = −n₁ + n₅, spin from tube-winding parity. Cross-shears between sheets produce inter-particle states (neutron, muon, mesons, nuclei). The model achieves **zero effective free parameters** at MeV scale after pinning r_p and σ_ep from neutron + muon, and delivers five parameter-free particle predictions within 1.5%.

---

## Outcomes

*Skim here first for predictive strength.*

### Quantitative predictions (zero free parameters at MeV scale)

| Result | Study | Error / note |
|--------|-------|-------------|
| **Neutron** mass (939.565 MeV) | R27 F10 | Exact — pins σ_ep = −0.0906 |
| **Muon** mass (105.658 MeV) | R27 F17 | Exact — pins r_p = 8.906 |
| **Kaon** K⁺ (493.7 MeV) | R27 F27 | **−1.2%** parameter-free |
| **Kaon** K⁰ (497.6 MeV) | R27 F31 | **−1.2%** parameter-free |
| **Eta** η (547.9 MeV) | R27 F31 | **−0.6%** parameter-free |
| **Eta prime** η′ (957.8 MeV) | R27 F31 | **−0.3%** parameter-free |
| **Phi** φ (1019 MeV) | R27 F31 | **−0.8%** parameter-free |
| **Λ** baryon (1115.7 MeV) | R28 F10 | **0.9%** (n_max extended to 15) |
| **Σ⁺** baryon (1189.4 MeV) | R28 F14 | **0.3%** (n_max extended to 15) |
| **Deuteron** (1875.6 MeV) | R29 F18 | **0.02%** parameter-free; 86% of binding energy captured |
| **Nuclei** d → ⁵⁶Fe | R29 F16 | All **< 1%** via n₅ = A, n₆ = 2A scaling |

### Structural / qualitative successes

- **Neutrino mass-squared ratio** Δm²₃₁/Δm²₂₁ = 33.60 reproduced **exactly** from shear s₃₄ = 0.02199 (R26 F1). Assignment A passes all tests at ε ≥ 3.2 with **zero effective sterile neutrinos** (R26 F34, F39).
- **Σm_ν ≈ 117 meV** — testable prediction, falsifiable by CMB-S4 (R26 F38).
- **Charge, spin, g ≈ 2** from geometry on each sheet — structural, not fitted (inherited from model-A, now embedded in the 6D metric).
- **Lifetime-gap correlation** r = −0.84 (p = 0.009) for **weak decays** supports the off-resonance hypothesis: unstable particles are near-misses to eigenmodes (R27 F39).
- **Reaction energetics**: **21/21** decays pass energy-conservation sign test after R28 Track 3 extension (R27 F44 updated by R28 F11).
- **Ω⁻ structurally forbidden** as single mode: spin-3/2 + odd charge impossible (R27 F35).
- **Two-tier physics confirmed**: Ma → particles and nuclei (MeV); S → atoms and chemistry (eV). Hydrogen E₁ = −13.6 eV reproduced from Coulomb / KK zero-mode (R29 F2). Atoms are NOT Ma modes (R29 F24, R31 F2).
- **Free ≠ nuclear neutron**: different Ma modes; explains why n doesn't decay in a nucleus (R29 F20).
- **Six KK gauge fields** from the Ma geometry, including a proton-tube boson (52 MeV, 3.8 fm) as nuclear force candidate (R29 F5–F6).
- **Fat-torus preference**: constrained energy minimization on the α curve favors **r_e ≈ 0.50**, decisively ruling out the thin-torus r = 6.6 of model-A (R37 F7).

### Decisive negative results

| Result | Study |
|--------|-------|
| **Tau** structural gap: no single mode at 1777 MeV; nearest at 1876 MeV (+5.6%) | R27 F20–F25 |
| **Pion** 13.5% off; structural, not parametric | R27 F29 |
| **α not derived**: Casimir has no interior minimum; Casimir prefers *larger* α | R31 F5–F6 |
| **Naive KK Yukawa** 10⁴× too large for Lamb shift; massive KK couplings must be suppressed ≳ 10⁵ | R29 F11, R31 |
| **Ghost modes**: ~900 charged modes below 2 GeV vs ~40 observed; 20× overprediction | R28 F6 |
| **Naive α running** catastrophic; ghost modes as independent fields ruled out | R32 |
| **Geometric tilt** does not replicate shear's charge mechanism | R36 |
| **Model does NOT predict three generations**: ~14,000 charge-−1 spin-½ levels below 10 GeV | R38 |
| **Predictive horizon** at ~2 GeV; above that, Ma spectrum too dense to discriminate | R28 F21 |
| **g − 2 from charge-mass separation** ruled out (wrong sign, 1400× too large) | R44 |

---

## Goals

- Extend the electron-on-a-torus picture to a **joint** material space hosting electron, neutrino, and proton on **three coupled sheets** — solving the neutrino spin problem that killed model-A.
- Build a **shared code library** (`ma.py`) for the 6×6 metric, mode energies, charges, spins, and scanning.
- **Pin free parameters** from particle masses: use cross-shears and aspect ratios as handles, fit to neutron, muon, and as many other particles as possible.
- Derive **Coulomb / α from geometry** (partially achieved via KK zero-mode; α as input not yet broken).
- Model **nuclei** as Ma modes, not force-bound composites.
- Quantify the **off-resonance hypothesis**: unstable particles as near-misses, lifetime ∝ gap.

---

## Assumptions

- **Three flat 2-tori** (Ma_e, Ma_ν, Ma_p) with within-plane shears s₁₂, s₃₄, s₅₆ and up to 12 cross-shears σ_ij connecting the sheets.
- **Charge** from tube windings: Q = −n₁ + n₅ (from the R19 shear mechanism on each sheet).
- **Spin** from tube-winding parity (odd tube winding → spin-½ contribution); finite-ε corrections computed via geodesic path integral (R26 Track 1d).
- **α = 1/137** as input → fixes within-plane shears s₁₂(r_e) and s₅₆(r_p).
- **m_e, m_p** as inputs → fix circumferences L₂, L₆ (given aspect ratios).
- **Δm²₂₁ = 7.53 × 10⁻⁵ eV²** → fixes neutrino scale L₄ (given r_ν).
- **Proton as (1,2)** mode on Ma_p (later reconsidered in model-C/D as (3,6) composite).
- **Linearized, single-mode KK picture**: each physical state is one six-tuple; multi-mode composites are not yet in scope (except descriptively for nuclei).

---

## Strategies / approach

### Core library

[`studies/lib/ma.py`](../studies/lib/ma.py) — extracted from R26 Track 4a. Builds the dimensionless 6×6 metric G̃, computes mode energy E(n), charge Q(n), spin. Condition number ~1.25 (vs ~10²¹ for the physical metric). [`studies/lib/ma_solver.py`](../studies/lib/ma_solver.py) — self-consistent circumference solver, brute-force mode scanner, multi-target optimizer.

### Study arc

| Study | Focus | Key method |
|-------|-------|-----------|
| **R26** | Establish the 3-sheet framework; neutrino assignments; neutron candidate; parameter census | Analytical + numerical metric construction |
| **R27** | Discovery engine; pin r_p, σ_ep from neutron + muon; particle catalog; lifetime-gap law; reaction energetics | `ma_solver.py` systematic search |
| **R28** | σ_eν / σ_νp exploration; mode census; strange baryon refinement; high-energy horizon | Extended n_max scans |
| **R29** | KK → Coulomb; hydrogen; **nuclei as Ma modes** (n₅ = A, n₆ = 2A); two-tier physics | Analytical KK + nuclear mode search |
| **R30** | Is a torus topologically required? Klein bottle, circle, hierarchical compactification | Structural / analytical |
| **R31** | Can α be derived? Casimir, Lamb shift, merger barrier | Casimir zeta function; perturbative Lamb shift |
| **R32** | α running from ghost modes; volume dilution | QFT-style loop counting on Ma spectrum |
| **R33** | Ghost-mode selection rules (charge integral, spin filter, dipole suppression) | WvM charge integral numerics |
| **R34** | Midpoint coupling (137 → 80.5 → 24); Kramers-Kronig | Dispersion-relation fits |
| **R35** | Threshold / biological coupling; Cd-109 / Na-22 detector model; elastic torus I/O | Monte Carlo + SCA |
| **R36** | Geometric tilt vs within-plane shear | Analytical KK comparison |
| **R37** | Membrane mechanics: elastic constants, energy minimization → **r ≈ 0.50** | Constrained optimization along α curve |
| **R38** | Fourth generation census; resonance capture | Brute-force level counting |

---

## Limitations

- **α is circular**: input via s(r) from R19; no first-principles derivation. Casimir provides no minimum (R31). The "why α = 1/137?" question reduces to "why s ≈ 0.01?" (R32).
- **r_e unconstrained** at MeV scale (invisible to particle masses). R37's fat-torus preference (r ≈ 0.5) is the only internal selection; R29 Yukawa bounds give r_e ≲ 2–5 from hydrogen.
- **r_ν weakly constrained** (ε ≥ 3.2 from cosmology).
- **Tau structural gap** (5.6%): no single mode at 1777 MeV. The proton energy ladder has a ~470 MeV gap there.
- **Pion** 13.5% off — structural, not tunable.
- **Ghost modes**: 20× more charged modes than observed particles below 2 GeV. The off-resonance hypothesis is qualitatively supported but a quantitative selection rule (which modes are observable?) is missing.
- **Three generations accommodated, not predicted**: ~14,000 charged lepton levels below 10 GeV; nothing selects exactly three.
- **Naive KK massive-mode coupling** fails for Lamb shift by ~10⁵. Resolution requires non-uniform coupling or a different intermediate theory; unresolved.
- **Proton as (1,2)**: later work (R47, model-D) prefers **(3,6)** composite — model-B does not address internal proton structure or anomalous moments.
- **No waveguide filtering**: the cutoff mechanism discovered in R46 (model-D era) is absent; all modes above the zero-point survive the catalog.
- **No dynamic torus corrections**: elliptical cross-section, radiation pressure, and self-consistent shape are deferred to model-C (`ma_model.py`).

### Supersession

Model-B's `ma.py` is **refactored** into [`studies/lib/ma_model.py`](../studies/lib/ma_model.py) starting at **R39** (near-field phase). The refactor adds an immutable `Ma` class, dynamic corrections (elliptical cross-section, pressure harmonics), and a broader parameter-sweep API. Studies R39–R43 form the **model-C** era. The key motivations for moving on:

1. **Ghost mode problem** unresolved — R33's partial filters are not integrated into the library.
2. **Tau and pion gaps** are structural under single-mode KK; dynamic corrections might shift mode energies.
3. **Proton structure** (anomalous moment, quark phenomenology) needs revisiting — R44/R47 undertake this in the model-C/D era.
4. **Waveguide filtering** (R46) and **finite-ε spin** (R49) are discovered *after* model-B and require a new code stack.

See [`model-C.md`](model-C.md) *(draft when added)*.

---

## References

- **Studies:**
  [R26](../studies/R26-neutrino-t4/README.md),
  [R27](../studies/R27-bound-states/README.md),
  [R28](../studies/R28-particle-spectrum/README.md),
  [R29](../studies/R29-atoms-and-nuclei/README.md),
  [R30](../studies/R30-minimal-geometry/README.md),
  [R31](../studies/R31-alpha-derivation/README.md),
  [R32](../studies/R32-alpha-running/README.md),
  [R33](../studies/R33-ghost-selection/README.md),
  [R34](../studies/R34-midpoint-coupling/README.md),
  [R35](../studies/R35-threshold-coupling/README.md),
  [R36](../studies/R36-geometric-tilt/README.md),
  [R37](../studies/R37-membrane-mechanics/README.md),
  [R38](../studies/R38-fourth-generation/README.md)

- **Code:**
  [`studies/lib/ma.py`](../studies/lib/ma.py),
  [`studies/lib/ma_solver.py`](../studies/lib/ma_solver.py),
  [`studies/lib/constants.py`](../studies/lib/constants.py)

- **Key QA / primers:**
  [`qa/Q18-deriving-alpha.md`](../qa/Q18-deriving-alpha.md),
  [`qa/Q16-proton-mass.md`](../qa/Q16-proton-mass.md),
  [`qa/Q34`](../qa/) (α selection paths),
  [`primers/neutrino.md`](../primers/neutrino.md)
