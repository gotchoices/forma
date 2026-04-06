# Model: model-C (Generalized model — `ma_model.py`)

**Code / implementation:** [`studies/lib/ma_model.py`](../studies/lib/ma_model.py) (1,900-line Ma engine with four-level dynamic hierarchy; 125 unit tests), [`studies/lib/ma_solver.py`](../studies/lib/ma_solver.py)  
**Study range (approximate):** **R39 through R44** (see [`studies/STATUS.md`](../studies/STATUS.md)), plus all phenomena and infrastructure inherited from R26–R38.  
**Supersedes / superseded by:** Supersedes [model-B](model-B.md) (`ma.py`, R26–R38). Superseded by **model-D** ([`model-D.md`](model-D.md)) starting at R46, where waveguide filtering, finite-ε spin, (3,6) proton composite, and a new code stack (`ma_model_d.py`) replace this model's assumptions.

---

## Summary

Model-C is the **mature generalized version** of the three-sheet Ma framework. It refactors model-B's `ma.py` into `ma_model.py` — an immutable `Ma` class with static, elliptical, shortcut, and full iterative dynamic levels — and runs the model through several new domains: near-field nuclear EM (R39), self-consistent torus shape (R40), dynamic corrections and ghost census (R41), dark matter from ghost modes (R42), the Weinberg angle (R43), and the anomalous magnetic moment (R44). Model-C inherits and does not revise model-B's quantitative particle predictions (they depend on r_p and σ_ep, which are unchanged); its contribution is **conceptual deepening** (dynamic torus, dark matter mechanism, electroweak connections) and **honest negative results** (g−2 from shear ruled out, α still not derived, three generations not predicted, ghost modes not fully resolved).

This is the model described in the project's root-level files ([`README.md`](../README.md), [`STATUS.md`](../STATUS.md), [`studies/Taxonomy.md`](../studies/Taxonomy.md)) at the time of migration. The "current state of the project" up through approximately study R44 **is** model-C.

---

## Outcomes

*This section consolidates what model-C delivers. Inherited results from model-B are included because model-C is the version documented in root-level files.*

### The framework

- **MaSt** = Material – Space – time. Full arena: **Ma × S × t** = 6 + 3 + 1 = **10 dimensions**. Particles are standing EM waves on Ma. Mass = confined energy, spin = winding topology, charge = shear-induced symmetry breaking.
- Three flat periodic sheets (Ma_e, Ma_ν, Ma_p) are **required** — a single sheet cannot support both uncharged fermions and charged particles (R14, R25).
- **Energy and geometry are the only fundamentals.** Conservation laws are exact because they are topological: charge = winding number, spin = geodesic topology.
- The KK gauge field **emerges** from the wave equation on compact × non-compact space (R36 F8–F9); it is not imposed.

### Parameter accounting

| What | Count | Details |
|------|------:|---------|
| Ma metric components | 21 | Flat 6×6 symmetric metric |
| Set by experimental inputs | 6 | m_e, m_p, Δm²₂₁ → 3 ring scales; α → s_e(r_e), s_p(r_p); Δm² ratio → s_ν = 0.022 |
| Pinned by particle fits | 2 | r_p = 8.906 and σ_ep = −0.091 (neutron + muon, R27 F18) |
| Cross-shears (irrelevant) | 11 | All zero; shown insensitive to MeV-scale spectrum (R28 F1/F4) |
| **Effective free** | **2** | **r_e** (unconstrained), **r_ν** (≥ 3.2 from cosmological Σm_ν bound) |

MeV-scale hadron predictions are insensitive to both remaining free parameters.

### Electron properties (R2, R19)

| Property | Status |
|----------|--------|
| Spin ½ | Exact — topological, from (1,2) winding |
| Mass m_e | Input — Compton path-length fixes scale |
| Charge e | Emergent — shear mechanism; α still requires one input |
| g-factor ≈ 2.0023 | Derived — WvM energy-partition argument |
| Free parameters | Zero continuous — topology + e + m_e fully determines geometry |

### Particle spectrum (R27, R28 — inherited, parameter-free at MeV scale)

| Particle | Ma mode | Error | Source |
|----------|---------|------:|--------|
| Kaon K⁺ | (−4,−8,+1,0,−3,−1) | 1.2% | R27 F31 |
| Kaon K⁰ | (−3,−8, 0,0,−3,+1) | 1.2% | R27 F31 |
| Eta η | (−5,−8, 0,0,−5,+1) | 0.6% | R27 F31 |
| Eta prime η′ | (−3,−8, 0,0,−3,+2) | 0.3% | R27 F31 |
| Phi φ | (−7,−8, 0,0,−7,+2) | 0.8% | R27 F31 |
| Lambda Λ | (−12,−15,+1,0,−12,−2) | 0.9% | R28 F10 |
| Sigma⁺ Σ⁺ | (−14,−15, 0,0,−13,+2) | 0.3% | R28 F14 |

Lifetime-gap correlation r = −0.84 (p = 0.009) for weak decays. 21/21 tested decay reactions pass energy-conservation sign test.

### Emergent neutron (R26, R27)

Mode (0,−2,+1,0,0,+2) spanning Ma_e × Ma_ν × Ma_p. Q = 0 (exact, topological). Spin ½ from neutrino winding. Mass reproduced at σ_ep = −0.091. Not put in — found by the solver.

### Neutrino masses (R26)

Δm²₃₁/Δm²₂₁ = 33.60 reproduced exactly from integer mode numbers, independent of r_ν. Σm_ν ≈ 117 meV (testable prediction, falsifiable by CMB-S4). Normal ordering predicted.

### Nuclear scaling law (R29)

Nuclei are single Ma_p modes, not multi-particle bound states. n₅ = A, n₆ = 2A matches d → ⁵⁶Fe at < 1%. Deuteron: 0.02% error, 86% of binding energy. Nuclear spins: 9/11 correct. Free neutron ≠ nuclear neutron (explains nuclear stability).

### Charged lepton generations (R27, R41)

| Particle | Mode | Nearest mode (MeV) | Observed (MeV) | Gap | Lifetime |
|----------|------|-------------------:|---------------:|----:|----------|
| e⁻ | (1,2,0,0,0,0) | 0.511 | 0.511 | 0 | Stable |
| μ⁻ | (−1,5,0,0,−2,0) | ~105.9 | 105.7 | ~0.3% | 2.2 μs |
| τ⁻ | (−1,5,0,0,−2,−4) | 1876 | 1776.9 | 5.6% | 290 fs |

Filter-factor ordering FF(e) > FF(τ) > FF(μ) confirmed by R41 dynamic model.

### Dynamic torus model (R40, R41 — new in model-C)

The α-impedance model: the torus wall is the (1−α) energy contour, with 136/137 of the photon energy confined and 1/137 leaking as external field. The 3D embedding produces a 0.067% elliptical perturbation with an elastic 1/k² wall response acting as a **low-pass filter** in tube winding number (40× suppression per n₁ step). Dynamic corrections are O(α²) ≈ 5×10⁻⁵ — the static flat-torus model is the correct zeroth-order approximation. Force-balance iteration converges in 3–4 steps. Dynamic corrections **do not** improve mass predictions (shifts ~10⁻⁴ vs structural errors ~1–6%).

### Near-field nuclear EM (R39 — new in model-C)

Proton charge distribution on the (1,2) torus at r_p = 8.906 reduces the Coulomb barrier by ~74% at 1 fm. Phase modulation adds ~3–14%. Anti-phase cancellation falsified for (1,2). No EM attraction at any orientation. Nuclear binding requires a non-EM mechanism (or the direct-mode picture from R29 where nuclei are Ma modes, not force-bound composites).

### Dark matter from ghost modes (R42 — new in model-C)

Ghost modes are plausible dark matter candidates: exact charge symmetry, Compton window hypothesis (Q94) explains suppressed EM coupling, DM/visible mass ratio spans 2.4–12.4 under physical filters, with the Planck value 5.36 inside the range. Several filters give 4.4–4.8. Mechanism identified but the Compton window quality factor Q has not been computed from first principles.

### Weinberg angle (R43 — new in model-C)

sin²θ_W matches 3/13 to −0.19% of the MS-bar value. The ratio 2/9 predicts M_W = 80.420 GeV (+0.051%). However, 3/13 **cannot be derived** from the Ma metric trace (F10 — gets 3/15 at unified coupling). W and Z are transient cross-sheet reconfigurations, not eigenmodes.

### Charge mechanism (R15, R19)

Within-plane shear s ≠ 0 breaks azimuthal symmetry of mode wavefunctions, producing a net Coulomb monopole from a delocalized wave. The formula α(r, s) gives a one-parameter family of solutions — every aspect ratio r > ~2 has a self-consistent shear s. The electron is the lightest charged particle (R19 F31).

### Plausible explanations (geometrically motivated, not yet derived)

| Phenomenon | SM status | MaSt explanation | Reference |
|------------|-----------|-----------------|-----------|
| Dark matter | Unknown particle(s); no detection after decades of search | Ghost modes on Ma: exact charge symmetry, Compton window suppresses EM coupling, mass ratio brackets 5.4 | R42, Q94 |
| Strong force | Separate force with fitted coupling α_s | Internal EM between overlapping Ma tori at r ~ λ_C, unattenuated by Compton window; range, coupling ~1, attraction emerge | Q95 |
| Matter–antimatter asymmetry | Requires CP violation beyond SM (CKM phase too small by ~10¹⁰) | Shear chirality of Ma breaks C and CP geometrically; all three Sakharov conditions met | Q97, Q32 |
| Nuclear binding | QCD confinement (non-perturbative, lattice-computed) | Nuclei are Ma_p modes, not multi-particle bound states; binding = mode transition on Ma | R29, Q89, Q95 |
| Force carriers (W, Z, gluon) | Fundamental gauge bosons mediating forces | Not fundamental: gluons unnecessary (Q95), W/Z are transient cross-sheet reconfigurations; sin²θ_W matches 3/13 to −0.19% (unexplained match) | Q96, R43 |
| Three generations | Unexplained; SM accommodates but does not predict | Three charge −1 spin ½ modes found: e (exact), μ (near-miss, ~0.3% gap), τ (near-miss, 5.6% gap); gaps correlate with lifetimes | R27, R41, Q86 |

### Decisive negative results (new in model-C era)

| Result | Study |
|--------|-------|
| **g−2 from shear-charge** ruled out: wrong sign, ~1400× too large | R44 |
| **Dynamic corrections** do not improve mass accuracy: O(10⁻⁴) vs O(1–6%) structural errors | R41 |
| **(1,1) ghost** not suppressed by dynamic filter: FF ≈ 0.46 | R41 |
| **Phase-dependent nuclear attraction** not found in classical EM | R39 |
| **sin²θ_W = 3/13** cannot be derived from Ma metric | R43 F10 |

### Predictive horizon (R28)

Above ~2 GeV the Ma mode spectrum is too dense (spacing < 5 MeV) for mass-matching to be discriminating. W/Z/Higgs match trivially — not a test.

### Computational infrastructure

- `lib/ma_model.py` — 1,900-line Ma model engine, immutable `Ma` class, four-level dynamic hierarchy (flat / elliptical / shortcut / full iterative). 125 unit tests.
- `lib/ma_solver.py` — mode discovery engine (self-consistent circumferences, brute-force scan, multi-target optimizer).
- 41+ completed studies (S1–S3, R1–R44), ~500 findings.
- White paper draft ([`papers/white-paper.md`](../papers/white-paper.md)).
- Taxonomy reference ([`studies/Taxonomy.md`](../studies/Taxonomy.md)).

---

## Goals

- **Refactor** `ma.py` into a production-quality engine (`ma_model.py`) with dynamic corrections and immutable state.
- **Test dynamic torus**: does the self-consistent shape improve mass predictions or resolve ghost modes?
- **Characterize near-field EM** at nuclear distances: can classical EM on the torus explain nuclear binding?
- **Dark matter**: can ghost modes account for the observed DM/baryon ratio?
- **Electroweak**: does the Ma geometry encode sin²θ_W or the W mass?
- **Anomalous magnetic moment**: can g−2 be derived from shear-induced charge distribution?
- **Consolidate** all model results into root-level documentation (README, STATUS, Taxonomy).

---

## Assumptions

All assumptions from model-B, plus:

- **Proton as (1,2)** mode on Ma_p (unchanged from model-B; reconsidered in model-D).
- **α-impedance wall**: the torus boundary is the (1−α) energy contour; field outside is the leaking 1/137 fraction.
- **Elastic 1/k² response**: the wall deforms under radiation pressure as a low-pass function of tube winding.
- **r_p = 8.906**, **σ_ep = −0.091** (pinned from R27, carried forward without revision).

---

## Strategies / approach

| Study | Focus | Key method |
|-------|-------|-----------|
| **R39** | Near-field phase-dependent proton EM at nuclear distances | Numerical charge distribution + orientation-averaged Coulomb on the (1,2) torus |
| **R40** | Self-consistent torus shape: radiation pressure, Clairaut geodesics, α-impedance model | Phase 1: GR stiffness (δ ~ 10⁻⁴⁰). Phase 2: α-impedance (δ ~ α²), low-pass filter |
| **R41** | Full dynamic model engine (`ma_model.py`); ghost census; generation hierarchy | Refactored library + brute-force 6D scan; filter-factor ordering |
| **R42** | Dark matter: ghost-mode charge symmetry, mass ratio, Compton window | Mode census + ad hoc filters; Lorentzian Q toy model |
| **R43** | Weinberg angle: sin²θ_W from sheet counting; W/Z as reconfigurations | Structural ratio 3/13; metric trace attempt (failed) |
| **R44** | Anomalous magnetic moment from R19 shear-charge distribution | Classical current-loop g-factor on the sheared torus |

---

## Limitations

All model-B limitations that were not resolved, plus:

- **α still circular**: input via s(r) from R19; no first-principles derivation. The dynamic model does not help.
- **r_e still unconstrained** at MeV scale. R37's fat-torus r ≈ 0.5 preference is the only internal signal.
- **Ghost modes**: dynamic filter suppresses high tube winding but **not (1,1)** — the most problematic ghost (half electron mass, charged boson). Ghost problem remains ~20× overprediction.
- **Tau gap** (5.6%) and **pion** (14%) unchanged — structural, not improved by dynamic corrections.
- **g−2** from shear-charge ruled out (R44) — wrong sign and order of magnitude. No alternative mechanism in this model.
- **Three generations accommodated, not predicted**: ~14,000 charge −1 spin ½ levels below 10 GeV (R38, R41).
- **sin²θ_W ≈ 3/13** is a striking numerology but **not derivable** from the Ma metric (R43 F10).
- **Nuclear binding**: R39 showed classical EM on the torus does not provide attraction; the direct-mode picture (R29) works for masses but the binding energy residual (~8 MeV/A for heavy nuclei) is not explained.
- **Proton as (1,2)**: later work (R47) prefers **(3,6)** composite with geometric confinement and SU(6) quark structure. Model-C does not address internal proton structure.
- **No waveguide filtering**: the cutoff mechanism discovered in R46 (model-D era) is absent; all modes above zero-point survive the catalog.
- **Naive KK massive-mode coupling** fails for Lamb shift by ~10⁵ (inherited from R29/R31).
- **Compton window Q factor** not computed from first principles — dark matter ratio is order-of-magnitude, not a prediction.
- **The hierarchy problem**: why is gravity ~10⁴⁰× weaker than EM? GRID explains the mechanism (EM is local phase dynamics, gravity is collective thermodynamics) but the precise ratio depends on ζ and α, whose relationship (if any) is unknown.

### Supersession

Model-D begins at **R46** (electron filter). The key developments that force a new model:

1. **Waveguide cutoff** (R46): a hard mode selection rule on Ma_e and Ma_p that model-C lacks entirely. Eliminates ghost modes below cutoff.
2. **Finite-ε spin** (R49): spin deviates significantly from ½ at large ε; the thin-torus spin formula used throughout model-C is qualitatively wrong for Assignment B and large-ε regimes.
3. **Proton as (3,6) composite** (R47): wins 8 of 11 criteria vs (1,2); SU(6) moments, constituent mass m_p/3 = 313 MeV, and geometric confinement all follow. This overturns model-C's single-mode (1,2) proton.
4. **No premature pinning philosophy** (R50): model-D treats the neutron as a prediction, not a calibration target. r_p and σ_ep are **swept**, not fixed from R27.
5. **New code stack**: `ma_model_d.py` replaces `ma_model.py` with joint-metric APIs and per-sheet waveguide filters.

See [`model-D.md`](model-D.md).

---

## References

- **Studies (model-C era):**
  [R39](../studies/R39-near-field-phase/README.md),
  [R40](../studies/R40-dynamic-torus/README.md),
  [R41](../studies/R41-dynamic-model/README.md),
  [R42](../studies/R42-dark-matter/README.md),
  [R43](../studies/R43-weinberg-angle/README.md),
  [R44](../studies/R44-g-minus-2/README.md)

- **Inherited studies (model-B, fully incorporated):**
  R26–R38 (see [model-B.md](model-B.md))

- **Root-level documentation (describes model-C state):**
  [`README.md`](../README.md),
  [`STATUS.md`](../STATUS.md),
  [`studies/Taxonomy.md`](../studies/Taxonomy.md)

- **Code:**
  [`studies/lib/ma_model.py`](../studies/lib/ma_model.py),
  [`studies/lib/ma_solver.py`](../studies/lib/ma_solver.py),
  [`studies/lib/constants.py`](../studies/lib/constants.py)

- **Papers:**
  [`papers/matter-from-light.md`](../papers/matter-from-light.md),
  [`papers/white-paper.md`](../papers/white-paper.md),
  [`papers/atoms-from-geometry.md`](../papers/atoms-from-geometry.md),
  [`papers/dark-matter.md`](../papers/dark-matter.md)

- **Key QA:**
  [Q94 (Compton window)](../qa/Q94-compton-window-and-dark-modes.md),
  [Q95 (strong force)](../qa/Q95-strong-force-as-internal-em.md),
  [Q96 (force carriers)](../qa/Q96-force-carriers-in-mast.md),
  [Q97 (CP violation)](../qa/Q97-shear-chirality-and-cp-violation.md),
  [Q86 (three generations)](../qa/Q86-three-generations.md),
  [Q84 (MaSt terminology)](../qa/Q84-mast-terminology.md)
