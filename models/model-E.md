# Model: model-E (Full T⁶ with generation structure) ⟵ ACTIVE

**Status:** Active — R53/R54 complete, R55 framed
**Code:** [`studies/lib/ma_model_d.py`](../studies/lib/ma_model_d.py) (engine shared with model-D; metric extensions in R54 scripts)
**Study range:** R53 (generations), R54 (compound modes, nuclei, α), R55 (Ma-S derivation, framed)
**Supersedes:** [model-D](model-D.md)

---

## Assumptions

1. **GRID** — a discrete causal lattice with internal phase.
   Gives Maxwell's equations, gravity, charge quantization, and α.
   Charge is topological: one tube winding = one unit of charge
   (GRID axiom A3).

2. **One flat six-torus (T⁶)** in six compact material
   dimensions.  The three "sheets" (Ma_e, Ma_ν, Ma_p) are a
   basis choice for reading the 6×6 metric, not separate
   physical entities (Q116).  At zero cross-coupling the sheets
   decouple; at nonzero coupling they blur into one 6D space.

3. **Particles are standing electromagnetic waves on T⁶.**
   Each mode is labeled by six integers (n₁,...,n₆).  Mass
   is the eigenfrequency.  Charge and spin are topological.

4. **The 9×9 metric** on T⁶ × S has four types of off-diagonal
   entries serving distinct roles:
   - In-sheet shears → generation structure and mode energies
   - Cross-sheet entries → compound modes (neutron, hadrons)
   - Ma-S entries → α coupling (charge → Coulomb field)
   - Within-S → flat space (zero)

5. **Charge sign comes from Ma-S coupling sign.** The charge
   formula Q = −n₁ + n₅ encodes that the e-sheet couples to S
   with NEGATIVE sign and the p-sheet with POSITIVE sign.  The
   magnitudes are equal (|σ_eS| = |σ_pS| ∝ α), giving equal
   coupling strength; the signs are opposite, giving opposite
   charge.  The ν-sheet has zero Ma-S coupling (neutrinos are
   electrically neutral).  Matter vs antimatter is the sign of
   the tube winding; positive vs negative charge is which sheet
   the winding lives on.

## Parameter count

| Category | Count | Examples |
|----------|------:|---------|
| **Measured inputs** | **7** | α, m_e, m_p, Δm²₂₁, m_μ/m_e, m_τ/m_e, Δm² ratio |
| — of which dimensional (scales) | 3 | m_e, m_p, Δm²₂₁ |
| — of which dimensionless | 4 | α, m_μ/m_e, m_τ/m_e, Δm² ratio |
| **Derived from inputs** | 10+ | s_e, ε_e, s_p, s_ν, L₁–L₆, Ma-S signs |
| **Constrained by physics** | 2 | ε_p (waveguide), ε_ν (Family A) |
| **Soft (neutron neighborhood)** | 2 | σ₄₅, σ₄₆ |
| **Open cross-sheet** | 4 | σ₂₃, σ₂₄, σ₂₅, σ₂₆ |

The Standard Model has ~19 dimensionless free parameters.
Model-E has **4** (or 3 if GRID derives α).

## Results

### Predictions

- **20 of 20 surveyed particles have credible modes** — stable
  particles match exactly, unstable particles are near-misses
  with gaps consistent with their instability
- The proton is an exact eigenmode at 938.272 MeV
- The neutron is a 6D knot (electron + neutrino + proton fused)
  at 0.07% off — a near-miss predicting its 880 s decay
- **Three charged lepton generations** from in-sheet shear
  resonance: electron (1,2), muon (3,8)/(−3,−5), tau (3,−8)/(−7,3).
  Mass ratios exact from two geometric parameters (ε_e, s_e)
- Nuclear masses from deuterium to iron at ≤ 1.1% via the
  R29 scaling law (n₅ = A, n₆ = 3A), with universal charge
  formula Q = −n₁ + n₅ = Z
- Neutrino oscillation: Δm²₃₁/Δm²₂₁ = 33.6 exact, normal
  ordering, Majorana nature (R26/R49, unchanged from model-D)
- The (1,1) ghost is eliminated by shear ordering — the electron
  is naturally the lightest charged mode.  No waveguide filter needed
- Charged pion spin-charge barrier broken: two odd tube windings
  on different sheets (e + ν) give spin 0 with Q = ±1
- **Electron shell structure** explained as a lowest-energy
  routing problem: the Ma torus at each Bohr radius has finite
  mode capacity (n² angular modes from the closure condition
  l(l+1) < n²); when full, the next electron routes to S
  (next shell) because spatial separation costs ~2.5× less
  than promoting to the next angular harmonic.  Shell
  capacities 2n² = 2, 8, 18, 32 reproduced exactly, with
  the factor of 2 derived from tube winding topology (R56)
- **Ghost mode suppression** follows from the same routing:
  higher Ma harmonics exist but are never populated because
  spatial separation is energetically cheaper (R56 F23)
- Strong force, quark confinement, dark matter candidates — all
  inherited from model-D

### Working assumptions

- **α = 1/137 from Ma-S coupling.** Charge is topological (GRID).
  The fraction of a mode's energy appearing as Coulomb field is
  controlled by the Ma-S block of the 9×9 metric, not by in-sheet
  shears.  The quantitative formula connecting Ma-S entries to α
  is the subject of R55 (framed, not yet computed).  The R19
  formula applies at the p-sheet (ε ~ O(1)) as a consistency
  condition; it does not apply at the e-sheet (ε >> 1).
  See [R54 Track 3](../studies/R54-compound-modes/findings_track3.md).

### Unresolved

- **α derivation from the 9×9 metric** — conceptual framework
  established (Ma-S coupling), quantitative formula pending (R55)
- **Off-resonance correlation** — correct qualitatively (stable =
  exact, unstable = near-miss) but weak as a single-variable
  predictor (Spearman ρ = +0.14).  Stratified by decay mechanism,
  as in model-D

## Particle inventory

Geometry: ε_e = 397.07, s_e = 2.00420 (R53 Solution D);
ε_p = 0.55, s_p = 0.16204 (from α); ε_ν = 5.0, s_ν = 0.02199.
Cross-shears: σ₄₅ = −0.18, σ₄₆ = +0.10 (soft, neutron region).

| Particle | Obs (MeV) | Mode | Δm/m | Stable? |
|----------|----------|------|------|---------|
| electron | 0.511 | (1, 2, −2, −2, 0, 0) | input | stable ✓ |
| proton | 938.3 | (0, 0, −2, 2, 1, 3) | input | stable ✓ |
| neutron | 939.6 | (0, −4, −1, 2, 0, −3) | 0.07% | near-miss ✓ |
| muon | 105.7 | (1, 1, −2, −2, 0, 0) | 0.83% | near-miss ✓ |
| tau | 1776.9 | (3, −6, 2, −2, 2, 3) | 0.05% | near-miss ✓ |
| Λ | 1115.7 | (−1, 2, −1, 2, −1, 3) | 0.00% | near-miss ✓ |
| η′ | 957.8 | (−1, −7, 2, −2, −1, 2) | 0.00% | near-miss ✓ |
| Σ⁻ | 1197.4 | (−1, 2, −2, 2, −2, −2) | 0.01% | near-miss ✓ |
| Σ⁺ | 1189.4 | (−2, 3, 2, −2, −1, −3) | 0.02% | near-miss ✓ |
| Ξ⁻ | 1321.7 | (−1, 5, −2, 2, −2, 1) | 0.03% | near-miss ✓ |
| φ | 1019.5 | (−1, 4, 2, −2, −1, 2) | 0.06% | near-miss ✓ |
| Ω⁻ | 1672.5 | (−2, 2, −2, 2, −3, 0) | 0.13% | near-miss ✓ |
| Δ⁺ | 1232.0 | (−3, −6, 2, −2, −2, 2) | 0.17% | near-miss ✓ |
| Ξ⁰ | 1314.9 | (−1, 8, −1, 2, −1, 2) | 0.19% | near-miss ✓ |
| ρ | 775.3 | (−1, 5, −2, 2, 0, 1) | 0.97% | near-miss ✓ |
| K⁰ | 497.6 | (0, −4, −2, 2, 0, 1) | 1.04% | near-miss ✓ |
| K± | 493.7 | (−1, −6, −2, 2, 0, 1) | 1.77% | near-miss ✓ |
| η | 547.9 | (−1, −4, −2, 2, −1, 0) | 1.84% | near-miss ✓ |
| π⁰ | 135.0 | (0, −1, −2, −2, 0, 0) | 22.7% | near-miss ✓ |
| π± | 139.6 | (−1, −1, −2, −2, 0, 0) | 24.9% | near-miss ✓ |

**20 of 20 particles matched.** Stable particles are exact
eigenmodes.  Unstable particles are near-misses with gaps
consistent with their decay rates (stratified by decay mechanism).

## Nuclear scaling

| Nucleus | A | Z | Δm/m |
|---------|---|---|------|
| d | 2 | 1 | 0.05% |
| ⁴He | 4 | 2 | 0.69% |
| ¹²C | 12 | 6 | 0.76% |
| ⁵⁶Fe | 56 | 26 | 1.05% |

Scaling law: n₅ = A, n₆ = 3A.  Charge: Q = −n₁ + n₅ = Z.
Universal for all tested nuclei from deuterium to iron.

## Three generations (R53)

| Gen | Lepton | Mode | Mechanism |
|-----|--------|------|-----------|
| 1st | electron | (1, 2) | shear resonance (n₂ ≈ s_e) |
| 2nd | muon | (3, 8) or (−3, −5) | off-resonance |
| 3rd | tau | (3, −8) or (−7, 3) | chirality partner / far off-resonance |

At ε_e ≈ 330–397 and s_e ≈ 2–3, the electron sits at the
shear cancellation point (n₂ − n₁·s ≈ 0), making it anomalously
light.  The muon and tau are off-resonance modes with larger
ring detuning.  The mass ratios are algebraically exact:
m_μ/m_e and m_τ/m_e determined by (ε_e, s_e) with zero free
parameters beyond the two geometric inputs.

## Metric structure

See [R54/metric-terms.md](../studies/R54-compound-modes/metric-terms.md)
for the complete 45-entry reference table.

The 9×9 metric has 45 independent entries: 29 determined,
12 from α (working assumption, pending R55), 4 active
cross-sheet entries open.

## Key advances over model-D

| Feature | Model-D | Model-E |
|---------|---------|---------|
| Particle credible modes | 16 of 20 | **20 of 20** |
| Muon | 10.9% (mass desert) | **0.83%** |
| Pion spin | impossible | **solved** (e+ν dual tube) |
| Ghost (1,1) | waveguide filter | **shear ordering** (natural) |
| Three generations | unexplained | **shear resonance** |
| Metric structure | 6×6, 3 scalar σ | **9×9, 45 entries, 4 roles** |
| α mechanism | R19 (conflated) | **Ma-S coupling** (separated) |
| T⁶ interpretation | three sheets | **one T⁶** (Q116) |
| Nuclear scaling | ≤ 1% | **≤ 1.1%** (comparable) |

## Studies

| Study | Focus | Status |
|-------|-------|--------|
| R53 | Three generations from in-sheet shear | Tracks 1, 4, 5, 6 complete |
| R54 | Compound modes on the full T⁶ | Tracks 1–3 complete |
| R55 | α consistency — Ma-S coupling derivation | Framed |
| R56 | Electron shell structure from geometric packing | Tracks 1–6 complete |

## References

- [R53 findings](../studies/R53-three-generations/findings.md)
- [R54 findings](../studies/R54-compound-modes/findings.md)
- [R54 metric terms](../studies/R54-compound-modes/metric-terms.md)
- [R54 STATUS](../studies/R54-compound-modes/STATUS.md)
- [Q115 (generations + metric)](../qa/Q115-three-generations-and-metric-structure.md)
- [Q116 (T⁶ vs sheets)](../qa/Q116-three-sheets-vs-one-six-torus.md)
- Predecessor: [model-D](model-D.md)
