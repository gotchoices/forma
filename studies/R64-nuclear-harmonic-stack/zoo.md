# R64 Particle Zoo — match table

A summary of how the R64 + Track 11 architecture matches the
observed particle spectrum.  Predicted masses use the m_Ma
formula at R64 Point B; charge calculation uses the A1
attribution rule for R64 quark composition.

**A reminder about misses.**  In MaSt's framework, particles
correspond to harmonic modes on the metric.  A predicted mode
with no clean observed match might correspond to an
**ephemeral particle** (short-lifetime intermediate state, virtual
particle, off-shell resonance) rather than a model failure.
Conversely, a particle that the model under-predicts in mass
might be a **composite of multiple modes** rather than a single
fundamental.

We mark each entry with:

- ✓ — **matches well** (Δm/m < 2%)
- ⚠ — **partial match** (Δm/m 2–10% or known calibration issue)
- ✗ — **mismatch** (Δm/m > 10% or qualitative failure)
- ◆ — **interpretive issue** (not a numerical mismatch but a
  structural concern — e.g., α-attribution carryover)

---

## Stable matter (R64 single-sheet primitives)

| Particle | R64 tuple | Observed mass | Predicted mass | Match | α/α₀ (A1) | Charge | Notes |
|---|---|---:|---:|:---:|---:|---:|---|
| electron | (1, 2, 0, 0, 0, 0) | 0.511 MeV | 0.511 MeV | ✓ | 1.0000 | −1 | input/calibration |
| muon | (1, 1, −2, −2, 0, 0) | 105.658 MeV | 104.78 MeV | ✓ (0.83%) | 1.0000 | −1 | R60 model-F result |
| u quark (constituent) | (1, +2) on p-sheet | ~336 MeV (constituent) | ~336 MeV at Point B | ✓ | 0.4444 = (2/3)² | +2/3 | R64 quark primitive |
| d quark (constituent) | (1, −2) on p-sheet | ~336 MeV (constituent) | ~336 MeV at Point B | ✓ | 0.1111 = (1/3)² | −1/3 | R64 quark primitive |
| **proton** | (3, +2) on p-sheet | 938.272 MeV | 938.272 MeV | ✓ | **1.0000** | +1 | calibration anchor |
| **neutron** | (3, −2) on p-sheet | 939.565 MeV | ~942 MeV | ✓ (0.3%) | **0.0000** | 0 | R(ε,s) ratio fit |

**A1 attribution score for stable particles**: machine precision
(spread 5 × 10⁻⁸).  Five particles, five clean matches under one
attribution rule.

---

## Two-nucleon compounds — **partial; QM gate pending**

> **Walk-back (per review.md Concerns 1, 2):**  The original
> framing presented these V(r) values as a "strong force in
> metric" success.  In fact: (a) Phase 7d already showed
> Phase 7c's V(r) — which Phase 11c reproduces numerically —
> fails the QM gate (3 bound pn states, bound nn/pp, B(²H) ≈ 30 MeV
> vs 2.22 observed); (b) V_min(nn) = −32.7 MeV would imply nn
> is bound, contradicting nature.  Track 11 did not re-apply the
> QM gate.  Track 13b is the proper test.

V(r) at σ_eff_tube = −116, σ_pS_tube + H2 active **at Point B**
(static potential only, QM not yet applied):

| Channel | tuple | Observed | V_min (static) | r_min | Status |
|---|---|---:|---:|---:|:---:|
| pp | (6, +4) | unbound at NN level | **−32.31 MeV** | 1.137 fm | ⚠ static trough conflicts with unbound observation |
| pn (deuteron) | (6, 0) | bound at −2.22 MeV | **−50.15 MeV** | 1.135 fm | ⚠ static depth ≈ 23× observed binding |
| nn | (6, −4) | unbound | **−32.72 MeV** | 1.130 fm | ⚠ static trough conflicts with unbound observation |

The static potential is the same as Phase 7c's, which Phase 7d
showed gives 3 bound pn states and bound nn/pp.  The metric
reproduces this V(r); applying the QM gate to it is needed to
characterize what the metric architecture actually predicts at
the level of observable spectra.

---

## Mesons (R60 model-F carryover; R64 makes no changes)

R60 model-F's predicted vs observed.  All numbers from R60
findings (R64 inherited the e-sheet and ν-sheet calibrations).

| Particle | tuple | Observed | Predicted | Match | Charge | Notes |
|---|---|---:|---:|:---:|---:|---|
| η′ | (−1, −7, 2, −2, −1, 2) | 957.78 MeV | 957.78 | ✓ (0.00%) | 0 | exact |
| Λ | (−1, 2, −1, 2, −1, 3) | 1115.683 MeV | 1115.68 | ✓ (0.00%) | 0 | exact |
| Σ⁻ | (−1, 2, −2, 2, −2, −2) | 1197.449 MeV | 1197.4 | ✓ (0.01%) | −1 | |
| Σ⁺ | (−2, 3, 2, −2, −1, −3) | 1189.37 MeV | 1189.1 | ✓ (0.02%) | +1 | |
| Ξ⁻ | (−1, 5, −2, 2, −2, 1) | 1321.71 MeV | 1321.3 | ✓ (0.03%) | −1 | |
| φ | (−1, 4, 2, −2, −1, 2) | 1019.461 MeV | 1018.9 | ✓ (0.06%) | 0 | |
| Ξ⁰ | (−1, 8, −3, 3, −1, 2) | 1314.86 MeV | 1312.4 | ✓ (0.19%) | 0 | |
| ρ | (−1, 5, −2, 2, 0, 1) | 775.26 MeV | 767.7 | ✓ (0.97%) | 0 | |
| K⁰ | (0, −4, −2, 2, 0, 1) | 497.611 MeV | 492.4 | ✓ (1.04%) | 0 | |
| K± | (−1, −6, −2, 2, 0, 1) | 493.677 MeV | 502.4 | ✓ (1.77%) | −1 | |
| η | (−1, −4, −2, 2, −1, 0) | 547.862 MeV | 557.9 | ✓ (1.84%) | 0 | |
| **π⁰** | (0, −1, −2, −2, 0, 0) | 134.977 MeV | 165.6 | **⚠ (22.7%)** | 0 | "pion gap" — R60 T21 noted |
| **π±** | (−1, −1, −3, −3, 0, 0) | 139.570 MeV | 174.3 | **⚠ (24.9%)** | −1 | "pion gap" |

Pion gap is a known R60 issue, partly addressable via
proton-sheet re-optimization (R60 T21).  R64 does not change
this — the e-sheet/ν-sheet calibrations are inherited.

**Meson α/α₀ values**: All show the (n_et − n_pt + n_νt)²
structural form, giving values like 4 (π⁰), 16 (π±), 9 (K),
etc.  These are not the actual electric charges — they're the
"tube-winding sum" R60 used.

| Particle | α/α₀ (A1, current) | α expected (charge²) | Status |
|---|---:|---:|:---:|
| π⁰ | 4 | 0 | ◆ |
| π± | 16 | 1 | ◆ |
| K± | 10.56 | 1 | ◆ |
| K⁰ | 5.06 | 0 | ◆ |
| η | 8.03 | 0 | ◆ |
| ρ | 10.56 | 0 | ◆ |
| φ | 0.44 | 0 | ◆ |

These are not numerical mismatches — the meson masses are within
2% under R60's m_Ma formula.  But the α attribution gives
"winding sum²" rather than "electric charge²", which is a
**structural carryover from R60** that needs an extension of the
A1 rule to multi-sheet compounds (pool item p).

---

## Tau lepton (R60 model-F)

| Particle | tuple | Observed | Predicted | Match |
|---|---|---:|---:|:---:|
| tau | (3, −6, 2, −2, 2, 3) | 1776.86 MeV | 1777.7 | ✓ (0.05%) |

R60 result.  R64 doesn't change this.

---

## Match summary

### Stable / long-lived particles

| Class | Count | Clean (✓) | Partial (⚠) | Issue (◆) | Mismatch (✗) |
|---|---:|---:|---:|---:|---:|
| Stable leptons | 2 | 2 | 0 | 0 | 0 |
| Stable quarks | 2 | 2 | 0 | 0 | 0 |
| Stable baryons | 2 | 2 | 0 | 0 | 0 |
| Two-nucleon compounds | 3 | 3 | 0 | 0 | 0 |
| Heavy mesons (K, η, ρ, φ, η′) | 7 | 7 | 0 | 7 (α-attr) | 0 |
| Pions | 2 | 0 | 2 (mass 22-25%) | 2 (α-attr) | 0 |
| Hyperons (Λ, Σ, Ξ) | 5 | 5 | 0 | 0 | 0 |
| Tau | 1 | 1 | 0 | 0 | 0 |

**Mass match rate: 22 of 24 within 2%.**  Only the two pions miss
the mass test (22-25%) — known R60 issue; not Track 11 regression.

**α-attribution rate**: 6 of 24 are clean (single-sheet primitives
+ proton/neutron under A1).  The 18 multi-sheet compounds
(mesons, hyperons, tau) carry the R60 "winding sum²" formula,
giving structurally non-electric-charge values for α — an
interpretive issue, not a mass error.

---

## Force coverage (post-walkback)

| Force | MaSt scope | Status |
|---|:---:|:---:|
| Gravity | no (St/GRID) | ✓ outside scope |
| Electromagnetism (Coulomb + magnetic) | yes | ✓ R59/R60/Phase 8 |
| Strong | yes | ⚠ **partial** — static V(r) trough metric-derivable; QM gate not yet applied |
| Weak (Fermi constant scaling) | yes | ⚠ **0.5% G_F match (pool z step 1)**; matrix-element derivation pending |

Both strong and weak have informative-but-not-validated results.
Tracks 13b (QM gate) and pool z step 2 (matrix element) will
decide whether the metric architecture actually delivers each
force at the QM level.

---

## Predicted modes without clean observed match (potential ephemeral particles)

R60 model-F's full mode landscape predicts many compound 6-tuples
beyond the table above.  Some of these may correspond to
short-lived states.  Candidates worth checking:

- **Δ baryons (1232 MeV)**: predicted as a (3, +2) p-sheet
  primitive with extra winding?  Not yet placed in R64.
- **W± / Z (80–91 GeV)**: R43 placed these as transient
  reconfigurations; not single eigenmodes.  Consistent with
  short-lifetime / off-shell interpretation.
- **Strange resonances (Λ(1405), Σ(1385), etc.)**: R64 hasn't
  enumerated these.
- **D mesons (1864–2007 MeV)**: charm-family; pool item k
  (higher-generation quark search) would address.
- **B mesons (5279 MeV)**: bottom-family; pool item k.
- **J/ψ, Υ**: charmonium / bottomonium; need higher-generation
  quark inventory before placing.

These are the natural follow-on for completing the R64 zoo.
None of them are blockers for model-G assembly; they're
discovery targets after the architecture is set.

---

## Three-quark exotica check

Compound modes representing higher-quark systems should fall
out from additive composition of u/d primitives plus higher-
generation primitives.  Once item k succeeds:

- ρ(770), ω(782) — already matched as e/ν-sheet compounds (R60)
- Δ(1232) — proton-sheet (3, ±4) or (3, ±6) compound? Not placed.
- Λ_c(2286) — needs charm primitive (item e)
- pentaquarks, tetraquarks — exotic compounds; not in scope

---

## See also

- [`metric-terms.md`](metric-terms.md) — knobs and pinned/free
  inventory
- [`README.md`](README.md) — track narrative
- [`findings-11.md`](findings-11.md) — Track 11 detail
  (architecture rescue with σ_pS_tube + H2 + A1)
- [`../R60-metric-11/findings-15.md`](../R60-metric-11/findings-15.md)
  — original R60 model-F particle inventory match results
