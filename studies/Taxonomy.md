# MaSt Taxonomy

A self-contained reference for the MaSt (Material-Space-time)
framework: dimensions, notation, geometry, particles, mechanisms,
and parameters.

For the naming rationale and migration guide, see
[`../qa/Q84-mast-terminology.md`](../qa/Q84-mast-terminology.md).

---

## 1. The ten dimensions

Einstein unified space and time into a four-dimensional
spacetime.  MaSt adds a lower layer: six compact **material**
dimensions where particles exist as standing electromagnetic
waves.  Energy flows through the full Ma-S-t continuum.

**MaSt** = **Ma**terial – **S**pace – **t**ime.

| Symbol | Name | Dim | Character | Scale |
|--------|------|:---:|-----------|-------|
| Ma | Material space | 6 | Compact, periodic | fm–mm |
| S | Space | 3 | Large, non-compact | cosmological |
| t | Time | 1 | Non-compact | — |

**Ma × S × t** = 6 + 3 + 1 = 10 dimensions.

Ordinary spacetime is S × t.  Ma is the new ingredient:
six material dimensions present at every point of S × t.
A particle is a standing wave on Ma.  Its position in S
and its evolution in t are secondary.

### Design principles (notation)

- **No superscript dimension counts.**  Ma is always 6D;
  S is always 3D.  Spell out counts in prose when needed.
- **Subscript = label.**  Always a letter or particle symbol
  (Ma_e, Ma_ν, Ma_p).
- **Leading numeral = structural count.**  3Ma = three sheets
  (not three dimensions).
- **ASCII:** Ma_nu (not Ma_v), sigma_ep, phi_e, theta_p.

---

## 2. The three material sheets (3Ma)

Ma decomposes into three independent periodic 2-planes:

| Symbol | Name | Size | Energy scale | Particle family |
|--------|------|------|-------------|-----------------|
| Ma_e | Electron sheet | ~pm | ~MeV | Electron, muon, tau |
| Ma_ν | Neutrino sheet | ~42–200 μm | ~meV (THz) | Neutrino mass eigenstates |
| Ma_p | Proton sheet | ~fm | ~GeV | Proton, hadrons, nuclei |

Arithmetic: 3Ma = Ma_e × Ma_ν × Ma_p = Ma (six dimensions).

Each sheet is a flat two-dimensional torus — a rectangle with
opposite edges identified.  Flatness means the photon propagating
inside sees Euclidean space.  The external embedding in S produces
the observable fields (charge, magnetic moment).

### 2.1 Within-sheet axes

Each sheet has two periodic axes: a **ring** (toroidal, major
circle) and a **tube** (poloidal, minor circle).

| Sheet | Ring axis | Tube axis |
|-------|-----------|-----------|
| Ma_e | φ_e | θ_e |
| Ma_ν | φ_ν | θ_ν |
| Ma_p | φ_p | θ_p |

The ring circumference L_φ ≥ tube circumference L_θ.  Their
ratio defines the **aspect ratio**:

    ε = a/R = L_θ / L_φ     (tube ÷ ring, always ≤ 1 for ring tori)

Per-particle values: ε_e, ε_p, ε_ν.

**Legacy notation:** Earlier studies and library code use `r_e`, `r_p`,
`r_ν` for the same quantity (ε).  A few studies (R21–R24) used
`r = 1/ε` (ring ÷ tube) alongside ε; those tables list both columns
for clarity.  New studies (R46+) use ε exclusively.

---

## 3. Geometric parameters

These numbers define the shape, size, and relationships of
the material dimensions.

### 3.1 Per-sheet parameters

| Parameter | Symbols | What it controls | Known values |
|-----------|---------|------------------|--------------|
| **Circumferences** | L_φ, L_θ per sheet | Physical size; sets energy scale | L_θe → m_e; L_θp → m_p |
| **Aspect ratio** | r_e, r_ν, r_p | Shape of each sheet | r_p = 8.906 (pinned by neutron + muon, R27 F18); r_e free; r_ν ≥ 3.2 |
| **Within-plane shear** | s_e, s_ν, s_p | Lattice skew; rectangle → parallelogram | All constrained: s_e by α (given r_e); s_ν = 0.022 by Δm²; s_p by α (given r_p) |
| **Energy scale** | E₀ | Fundamental mode energy ℏc/L | E₀(ν) ~ meV; E₀(e) ~ MeV; E₀(p) ~ GeV |

### 3.2 Inter-sheet parameters

| Parameter | Symbols | What it controls | Known values |
|-----------|---------|------------------|--------------|
| **Cross-shear** | σ_ep, σ_eν, σ_νp | Coupling between different sheets; off-diagonal Ma metric | σ_ep = −0.091 → neutron mass |

Cross-shears enable **cross-plane modes** — standing waves
with quantum numbers on more than one sheet.  The neutron
(a mode spanning Ma_e × Ma_p) exists only because σ_ep ≠ 0.

Each cross-shear has four components (e.g., σ_φeφp, σ_φeθp,
σ_θeφp, σ_θeθp).  Only the aggregate σ_ep has been constrained.

### 3.2.1 Parameter census (R26 F59)

The flat Ma metric has 21 independent components.

| Category | Count | Status |
|----------|------:|--------|
| Ring scales (L_θe, L_θp, L_θν) | 3 | Set by m_e, m_p, Δm²₂₁ (inputs) |
| Within-plane shears (s_e, s_ν, s_p) | 3 | All constrained: s_e by α (given r_e), s_p by α (given r_p), s_ν by Δm² ratio |
| Aspect ratios (r_e, r_ν, r_p) | 3 | r_p and σ_ep jointly pinned by neutron + muon (R27 F18); **r_e free**; **r_ν ≥ 3.2** |
| Aggregate cross-shear σ_ep | 1 | Pinned jointly with r_p (R27 F18) |
| Other cross-shear components | 11 | All zero; shown irrelevant to MeV-scale observables (R28 F1/F4) |
| **Total constrained** | **8** | 6 from experimental data + 2 from particle fits |
| **Formally free** | **13** | r_e, r_ν, 11 cross-shear components |
| **Effective free** | **2** | **r_e** (unconstrained), **r_ν** (≥ 3.2) |

Note: s_e and s_p are each determined by the α formula once
their sheet's aspect ratio is known.  Since r_p is pinned
(R27 F18), s_p is fully determined.  Since r_e is free, the
(r_e, s_e) pair counts as one free parameter.  The 11
remaining cross-shear components are formally free but have
no measurable effect on any tested observable — the effective
free parameter count is 2.

### 3.3 Embedding parameters

| Parameter | Symbol | What it controls | Status |
|-----------|--------|------------------|--------|
| **S–Ma tilt** | ψ | Orientation of a sheet relative to S; how much S "sees" of compact modes | Free; produces no force if uniform (R36) |
| **Membrane stiffness** | K_n | Resistance of the Ma/S interface to deformation | Under study (R37) |

ψ (psi) avoids collision with the tube-axis angle θ.

### 3.4 The full metric

The 6×6 compact metric G̃ᵢⱼ (dimensionless, rescaled by
circumferences) encodes all per-sheet and inter-sheet
parameters.  Block-diagonal when σ = 0; off-diagonal blocks
appear when cross-shears are nonzero.

**Parameter census (R26):** 21 metric entries, 15 free after
symmetry.

---

## 4. Modes and quantum numbers

A **mode** is a standing electromagnetic wave on Ma, specified
by six integers — the winding numbers around each compact
axis.

**Tuple ordering:** (n_φe, n_θe, n_φν, n_θν, n_φp, n_θp)

Shorthand: (n₁, n₂, n₃, n₄, n₅, n₆).

### 4.1 Terminology

| Term | Definition |
|------|-----------|
| **Winding number** | Integer count of wave cycles around a compact axis (nᵢ) |
| **Tube winding** | Winding on the smaller circumference (n₂, n₄, or n₆) |
| **Ring winding** | Winding on the larger circumference (n₁, n₃, or n₅) |
| **Fundamental mode** | Coprime winding pair — (1,2) is fundamental; (2,4) is not |
| **Harmonic** | Non-coprime pair: d × (p,q) where d > 1; same spin, d× energy |
| **Single-sheet mode** | Nonzero windings on only one sheet; zero on others |
| **Cross-plane mode** | Nonzero windings on more than one sheet; requires σ ≠ 0 |
| **Ghost mode** | Mode with valid quantum numbers but no observed particle |

### 4.2 Mode properties

| Property | How determined | Formula |
|----------|--------------|---------|
| **Mass** | Eigenvalue of Ma wave equation | m² = E₀² μ², where μ = √((n_φ·ε)² + (n_θ − n_φ·s)²) per sheet, plus cross-shear corrections |
| **Charge** | Ring windings on charged sheets | Q = −n₁ + n₅ (in units of e) |
| **Spin** | Tube winding number | s = ½ for odd n_θ (fermion); s = 0 or 1 for even n_θ (boson) |

### 4.3 Selection rules

| Rule | Effect | Source |
|------|--------|--------|
| **n₁ = ±1 for charge** | Only modes with \|n₁\| = 1 carry electric charge | R19 F17, F30 |
| **Spin-statistics** | Spin = n₁/n₂; only specific (n₁, n₂) give physical spin | R33 F3 |
| **s₁₃ = 0** | No shear between tube and 3rd direction → no charged particle lighter than the electron | R19 F31 |
| **Charge-spin linkage** | On a single sheet, charge and spin are both controlled by the tube winding n_θ; "uncharged fermion" is impossible on one sheet | R25 |

---

## 5. Particle catalog

### 5.1 Stable particles (inputs and anchors)

**Fitting principle:** Only stable particles should sit exactly
on Ma eigenmodes.  Unstable particles should be near-misses,
with the gap to the nearest eigenmode correlating with
lifetime (see §6, off-resonance hypothesis).

These stable particles pin the geometric parameters:

| Particle | Mode | Mass | Sheet(s) | What it pins |
|----------|------|------|----------|--------------|
| **Electron** | (1, 2, 0, 0, 0, 0) | 0.511 MeV | Ma_e | L_θe (input) |
| **Proton** | (0, 0, 0, 0, 1, 2) | 938.3 MeV | Ma_p | L_θp (input) |
| **Neutron** | (1, 2, 0, 0, 1, 2) | 939.6 MeV | Ma_e × Ma_p | σ_ep = −0.091 |

**Caveat on r_p:** R27 F18 used the muon (unstable, τ = 2.2 μs)
jointly with the neutron to pin r_p = 8.906 and σ_ep = −0.091.
This is inconsistent with the fitting principle above — the
muon should have a small off-resonance gap, not an exact match.
Because the muon is long-lived, the error is small (estimated
~0.3% from the lifetime-gap power law), and existing predictions
are unlikely to change significantly.  However, r_p and σ_ep
should eventually be re-derived from stable anchors only.

The model has **2 effective free parameters** (r_e and r_ν;
see §3) — the 11 remaining cross-shear components are formally
free but irrelevant.  The MeV-scale hadron predictions below
are insensitive to r_e and r_ν as well — they depend almost
entirely on r_p and σ_ep.  In this sense the predictions are
parameter-free.

### 5.2 Predictions insensitive to free parameters

| Particle | Mode | Predicted (MeV) | Observed (MeV) | Error |
|----------|------|----------------:|---------------:|------:|
| K⁺ | (−4,−8,+1,0,−3,−1) | 488.0 | 493.7 | 1.2% |
| K⁰ | (−3,−8, 0,0,−3,+1) | 503.7 | 497.6 | 1.2% |
| η | (−5,−8, 0,0,−5,+1) | 551.2 | 547.9 | 0.6% |
| η′ | (−3,−8, 0,0,−3,+2) | 961.1 | 957.8 | 0.3% |
| φ | (−7,−8, 0,0,−7,+2) | 1028.0 | 1019.5 | 0.8% |
| Λ | (−12,−15,+1,0,−12,−2) | 1105.9 | 1115.7 | 0.9% |
| Σ⁺ | (−14,−15, 0,0,−13,+2) | 1193.4 | 1189.4 | 0.3% |

### 5.3 Neutrino mass eigenstates

Three modes on Ma_ν with shear s₃₄ = 0.02199:

| Mode | Mass (meV) | Status |
|------|------------|--------|
| ν₁ = (1, 1) | 29.2 | Identified (R26) |
| ν₂ = (−1, 1) | 30.5 | Identified (R26) |
| ν₃ = (1, 2) | 58.2 | Identified (R26) |

Mass-squared ratio: Δm²₃₁/Δm²₂₁ = 33.6 — matches experiment
(33.6 ± 0.9), independent of r_ν.

Sum: Σm_ν ≈ 117 meV (below cosmological bound ~120 meV).

### 5.4 Nuclear scaling law

Nuclei are single Ma_p modes, not multi-particle bound states.

| Property | Formula |
|----------|---------|
| Ring winding | n₅ = A (mass number) |
| Tube winding | n₆ = 2A |
| Mass | m ≈ A × 938 MeV (< 1% error, d → ⁵⁶Fe) |

Nuclear spins predicted correctly for 9 of 11 tested nuclei.
Deuteron: 0.02% mass error, 86% of binding energy captured.

### 5.5 Charged lepton generations

| Particle | Mode | Nearest mode (MeV) | Observed (MeV) | Gap | Lifetime |
|----------|------|-------------------:|---------------:|----:|----------|
| e⁻ | (1, 2, 0, 0, 0, 0) | 0.511 | 0.511 | 0 | Stable |
| μ⁻ | (−1, 5, 0, 0, −2, 0) | ~105.9 | 105.7 | ~0.3% | 2.2 μs |
| τ⁻ | (−1, 5, 0, 0, −2, −4) | 1876 | 1776.9 | 5.6% | 290 fs |

All three have |n₁| = 1 → charge −1, spin ½.  They differ
only in quantum numbers on Ma_p.  The electron sits exactly
on its eigenmode (stable).  The muon and tau are near-misses
whose gaps correlate with their lifetimes — the tau's larger
gap explains its shorter lifetime (off-resonance hypothesis,
§6).  The tau's 5.6% gap is a prediction, not a failure.

"Three generations" is not a design constraint but the three
lowest-energy solutions to the charge/spin constraints.  The
Ma spectrum contains ~14,000 charge −1, spin ½ levels below
10 GeV — the ghost mode problem determines why only 3 are
occupied (R33, R38).

### 5.6 Known failures

| Particle | Error | Nature of failure |
|----------|-------|-------------------|
| Pion π | 14% | Nearest mode too heavy; lightest uncharged spin-0 (R27) |
| Omega⁻ Ω⁻ | — | Structurally forbidden: spin 3/2 + odd charge incompatible (R27) |

Note: the tau's 5.6% gap was previously listed here.  Under
the off-resonance hypothesis (§6), this gap is expected — it
explains the tau's short lifetime (290 fs).  See §5.5.

### 5.7 Predictive horizon

Above ~2 GeV, the Ma mode spectrum becomes so dense (band
spacing < 5 MeV) that matching particles to modes ceases to
be discriminating.  W, Z, and Higgs match trivially at high
energy — these are not meaningful tests (R28).

---

## 6. Key mechanisms

| Mechanism | Description | Reference |
|-----------|-------------|-----------|
| **Shear-induced charge** | Within-plane shear s ≠ 0 breaks φ-symmetry of mode wavefunctions; net E-flux asymmetry = electric charge; α = f(ε, s) | R19 |
| **Axial B-field projection** | B tangent to T² surface → net axial component along spin axis → magnetic dipole moment; g ≈ 2 from (1,2) topology | R2, primer |
| **Cross-shear coupling** | Inter-sheet shear σ ≠ 0 allows modes spanning multiple sheets; neutron, muon, and hadrons are cross-plane modes | R26 |
| **KK gauge field emergence** | Off-diagonal metric between Ma and S; fluctuations in S propagate as EM field; emerges from the wave equation, not imposed | R36 F8–F9 |
| **Charge-spin linkage** | On a single sheet, both charge and spin depend on the tube winding n_θ → uncharged fermion impossible → forced the move to 3Ma | R25 |
| **Off-resonance hypothesis** | Unstable particles sit between Ma eigenmodes; gap to nearest mode correlates with lifetime (r = −0.84, p = 0.009) | R27 |
| **Ghost mode suppression** | Most Ma modes are unobserved; n₁ = ±1 rule + spin filter kill ~99%; residual ~4 per sheet still open | R33 |
| **Nuclear mode identity** | Nuclei are Ma_p modes (n₅ = A, n₆ = 2A), not collections of bound nucleons | R29 |
| **Predictive horizon** | Above ~2 GeV, mode density prevents discriminating predictions | R28 |
| **Membrane mechanics** | Photon radiation pressure on the Ma/S interface; elastic response → gravity (normal) and charge (shear) | R37 (draft) |

---

## 7. Coupling asymmetry: E vs B

The two halves of the photon's energy couple to S with
strikingly different efficiency:

| Field | Direction on Ma | Projection into S | Coupling | Character |
|-------|----------------|--------------------|----------|-----------|
| E | Perpendicular to sheet (radial) | Electric monopole (charge) | O(α) ≈ 0.7% of E energy | Requires shear to avoid cancellation |
| B | Tangent to sheet (axial) | Magnetic dipole (moment) | O(1) — topological | Axial symmetry adds coherently |

α is the geometric penalty for extracting a monopole (radial)
field from a rotating surface normal, compared to the
efficient axial projection of B.

---

## 8. Open problems

| Problem | Status | Studies |
|---------|--------|---------|
| **Under-determination** | 21 metric components, 8 constrained → 13 formally free, but 11 are irrelevant cross-shears → **2 effective free** (r_e, r_ν). r_e is completely unconstrained; r_ν only lower-bounded (≥ 3.2). | R26 F59–F62, R27 F18, R28 F1/F4 |
| **The α problem** | What sets shear s_e ≈ 0.01? Multiple mechanisms tested, none successful. Coupled to r_e: s_e is not unique until r_e is fixed. | R15, R19, R31, R32, R34 |
| **Ghost modes** | ~900 valid modes below 2 GeV vs ~40 known particles; ~10⁵ suppression needed | R33 |
| **Aspect ratio r_e** | Free parameter; not pinned by any data | R19, R31 |
| **Three generations** | Accommodated but not predicted; reduces to ghost problem | R38, Q86 |
| **Membrane stiffness** | Does the Ma/S interface have computable elastic constants? | R37 |
| **α–G relationship** | Both from membrane mechanics? Hierarchy = Poisson ratio? | R37 |
| **Tau gap** | 5.6% off-resonance gap; consistent with τ lifetime but not yet derived from first principles | R27 |
| **Pion mass** | 14% off; lightest meson poorly matched | R27 |

---

## 9. Study registry

For the full study-by-study listing (active, backlog, done),
see [`STATUS.md`](STATUS.md).

---

## 10. Papers

| File | Title | Status |
|------|-------|--------|
| [`matter-from-light.md`](../papers/matter-from-light.md) | Matter from Light and Geometry | Draft (paper 1/3) |
| [`sub-quantum-memory.md`](../papers/sub-quantum-memory.md) | Sub-Quantum Memory | Part I draft, Part II outline (paper 2/3) |
| [`atoms-from-geometry.md`](../papers/atoms-from-geometry.md) | The Nine-Dimensional Atom | Rough outline (paper 3/3) |
| [`neutrino-domain-storage.md`](../papers/neutrino-domain-storage.md) | Neutrino-Domain Memory | Outline (companion) |
| [`universe-as-mode.md`](../papers/universe-as-mode.md) | The Universe as a Mode | Outline (thought piece) |
