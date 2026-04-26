# R64 Track 11 — Quark-counting structural audit

Track 11 audits whether R64's u/d quark decomposition introduced a
hidden factor-of-3 (or factor-of-9) error in the α-Coulomb formula
or the strong-force cross term, before declaring the metric route
exhausted (Track 10's verdict).

**Phase 11a result: two separate findings, both substantial.**

1. **Attribution fix is real.**  A charge-function projection
   `f(n_pt, n_pr) = n_pt/6 + n_pr/4` gives α universality at
   machine precision across the full R64 inventory (single
   quarks, baryons, two-nucleon compounds, leptons).  The
   factor-of-9 anomaly at the R64 proton is resolved.  Pool
   item g is closed.
2. **σ_eff_ring is NOT capped at ~1.**  The Schur-effective
   coupling diverges as σ_pS_ring approaches the signature
   boundary.  At σ_pS_ring ≈ 0.1251 (within the signature-OK
   band) σ_eff_ring crosses Phase 7c's target of 116.  The
   "metric capped at σ_eff ~1" finding from Phase 10a was a
   measurement choice, not a structural ceiling.

**However**, even at σ_eff_ring = 116, V(r) does not deliver
charge-symmetric strong-force binding.  The ring channel is
structurally tied to **signed** n_pr, so pp gets repulsion, nn
gets attraction (charge-asymmetric), and pn gets nothing
(n_pr = 0).  The magnitude limit was a misdiagnosis — the real
limit is **channel structure**, which Phase 11b will address.

---

## Phase 11a — α-attribution audit

Script:
[`scripts/track11_phase11a_attribution_audit.py`](scripts/track11_phase11a_attribution_audit.py) ·
Outputs:
[`outputs/track11_phase11a_attribution_audit.csv`](outputs/track11_phase11a_attribution_audit.csv) ·
[`outputs/track11_phase11a_alpha_ratios.png`](outputs/track11_phase11a_alpha_ratios.png)

### Method

1. Compute α/α₀ across R64 inventory (single u, single d, R64
   proton, R64 neutron, R64 deuteron, R64 pp, R64 nn, electron,
   muon, ν_e) under three rules:
   - **R0** (status quo): current `n_Ma · G⁻¹[Ma, t]` formula at
     R60 model-F + R64 Point B metric.
   - **A1** (charge-function projection): replace p-sheet
     contribution with `n_eff_p = f(n_pt, n_pr) = n_pt/6 + n_pr/4`.
   - **A2** (σ_ta_p recalibration): scale the p-sheet σ_ta entry
     by 1/3 to absorb the factor of 3.
2. Compute σ_eff_ring at signature boundary under each rule
   (Phase 10a's Schur formula), checking how close to the actual
   metric edge the Schur quantity remains finite.
3. At σ_eff_ring = 116, compute V(r) for pp, pn, nn channels and
   compare to Phase 7c's reference depth (−50 MeV at 1.135 fm).

### F11a.1. R64 inventory under current attribution (R0)

The α-Coulomb formula at the R60 model-F + R64 Point B metric,
applied to R64 quark-decomposed inventory:

| Mode | Tuple | q_expected (e) | α/α₀ | Expected | Ratio |
|:---|:---:|:---:|:---:|:---:|:---:|
| u (R64 prim) | (0,0,0,0,1,+2) | +2/3 | 1.0000 | 0.4444 | **2.25** |
| d (R64 prim) | (0,0,0,0,1,−2) | −1/3 | 1.0000 | 0.1111 | **9.00** |
| R64 proton | (0,0,0,0,3,+2) | +1.0 | 9.0000 | 1.0000 | **9.00** |
| R64 neutron | (0,0,0,0,3,−2) | 0.0 | 9.0000 | 0.0000 | (catastrophic) |
| R64 deuteron | (0,0,0,0,6,0) | +1.0 | 36.0000 | 1.0000 | **36.00** |
| R64 pp | (0,0,0,0,6,+4) | +2.0 | 36.0000 | 4.0000 | **9.00** |
| R64 nn | (0,0,0,0,6,−4) | 0.0 | 36.0000 | 0.0000 | (catastrophic) |
| electron | (1,2,0,0,0,0) | −1.0 | 1.0000 | 1.0000 | 1.00 ✓ |
| muon | (1,1,−2,−2,0,0) | −1.0 | 1.0000 | 1.0000 | 1.00 ✓ |

**Universality spread: 35.0** (catastrophic).

Two structural failures of R0:

- **R0 cannot distinguish u from d.**  Both give α/α₀ = 1
  because the σ_ra prescription suppresses G⁻¹[p_r, t] to
  numerical noise (~10⁻¹⁹), so Q ∝ n_pt only.  The n_pr
  difference between u (+2) and d (−2) drops out.
- **R0 gives wrong charges for neutron and nn.**  Both should
  be neutral (α = 0), but R0 gives α/α₀ = 9 and 36 respectively
  because Q² ∝ n_pt² is always positive.

The bare α factor of 9 at R64 proton (acknowledged silently
since Phase 7g) propagates linearly through the entire inventory.

### F11a.2. A1 (charge-function projection) restores universality

Replacing the p-sheet contribution with `n_eff_p = n_pt/6 + n_pr/4`:

| Mode | n_eff_p | α/α₀ | Expected | Ratio |
|:---|:---:|:---:|:---:|:---:|
| u | +2/3 | 0.4444 | 0.4444 | **1.0000** ✓ |
| d | −1/3 | 0.1111 | 0.1111 | **1.0000** ✓ |
| R64 proton | +1 | 1.0000 | 1.0000 | **1.0000** ✓ |
| R64 neutron | 0 | 0.0000 | 0.0000 | ✓ |
| R64 deuteron | +1 | 1.0000 | 1.0000 | **1.0000** ✓ |
| R64 pp | +2 | 4.0000 | 4.0000 | **1.0000** ✓ |
| R64 nn | 0 | 0.0000 | 0.0000 | ✓ |
| electron | n_et=1 | 1.0000 | 1.0000 | **1.0000** ✓ |
| muon | n_et=1 | 1.0000 | 1.0000 | **1.0000** ✓ |

**Universality spread: 4.8 × 10⁻⁸** (machine precision).

The charge function `f(n_pt, n_pr) = n_pt/6 + n_pr/4` has a clean
derivation: it is the unique linear combination that maps the u
quark primitive (1, +2) to charge +2/3 and the d quark primitive
(1, −2) to charge −1/3.  All composite charges (proton +1,
neutron 0, deuteron +1, etc.) follow from additive composition
of the quark-level charges.

This is **pool item g resolved**.  The R64 frame's α-attribution
extends model-F's by treating the p-sheet (n_pt, n_pr) as a 2D
charge-tuple and projecting via the linear functional f — rather
than reading n_pt directly as the charge winding.

### F11a.3. A2 (σ_ta_p recalibration) does not work

Scaling the p-sheet σ_ta by 1/3 (intended to absorb the n_pt = 3
factor in the proton):

- R64 proton α/α₀ = 0.6393 (overshoots 1.0)
- u and d still give the same α (cannot distinguish)
- Universality spread: 1.56 (still broken)

A2 reduces the magnitude error but doesn't address the structural
issue (u/d indistinguishability).  A1 is strictly better.

### F11a.4. σ_eff_ring at the signature boundary

Phase 10a reported σ_eff_ring = 1.13 at "band boundary" σ_pS_ring
= 0.109.  But the actual signature-OK band extends to σ_pS_ring =
**0.1251** (numerical edge), and σ_eff_ring grows divergently as
σ_pS_ring approaches that edge:

| σ_pS_ring | Signature OK | σ_eff_ring |
|:---:|:---:|:---:|
| 0.000 | ✓ | 0.000 |
| 0.100 | ✓ | 0.277 |
| 0.115 | ✓ | 0.741 |
| 0.120 | ✓ | 1.497 |
| 0.122 | ✓ | 2.478 |
| 0.124 | ✓ | 6.963 |
| 0.1245 | ✓ | 12.611 |
| 0.1248 | ✓ | 24.494 |
| **0.1250** | ✓ | **65.65** |
| 0.12505 | ✓ | **116.00** (Phase 7c target) |
| 0.125110 | ✓ | 853.59 |

Crucially, **A1 universality holds at machine precision (5 × 10⁻⁸)
across the entire band**, including at the boundary.  Operating
near the signature edge does not break α physics.

This contradicts the Track 10 verdict that "σ_eff caps at ~1."
The cap was a measurement choice (taking σ_eff at "safe distance"
from the boundary).  The Schur-effective coupling has full range
[0, ∞] within the signature-OK band.

### F11a.5. V(r) at σ_eff_ring = 116 — the channel-structure problem

At σ_pS_ring ≈ 0.1251 (giving σ_eff_ring = 116), V(r) for the
three NN channels:

| Channel | n_pt | n_pr | r_min (fm) | V_min (MeV) | V(5 fm) |
|:---|:---:|:---:|:---:|:---:|:---:|
| pp | 6 | +4 | 5.0 (boundary) | **+11.32 (repulsive!)** | +11.32 |
| pn | 6 | 0 | 5.0 (boundary) | −15.72 (Ma offset only) | −15.72 |
| nn | 6 | −4 | 1.685 | −14.59 | −8.17 |

This is qualitatively wrong for the strong force:

1. **pp repulsive, nn attractive** — strong force should be
   charge-symmetric.  The asymmetry comes from the cross term
   `2·k_S·σ_eff_ring·n_pr·ℏc`: for pp (n_pr = +4) it adds
   positive m², repelling; for nn (n_pr = −4) it subtracts,
   attracting.
2. **pn channel gets zero contribution from σ_pS_ring** because
   n_pr(pn) = 0 (R64's u/d primitives sum: u + u + d + u + d + d
   has total n_pr = +6 − 6 = 0).
3. **nn trough at 1.69 fm with depth −14.6 MeV** — much shallower
   than Phase 7c's −50 MeV at 1.135 fm.  Even where the magnitude
   is right, the kinematic shape doesn't match.

The ring channel cannot deliver charge-symmetric strong force
**by construction** — it's tied to the signed n_pr value.  Phase
10a's "deuteron problem" generalizes here: the issue is not
σ_eff magnitude, it's that σ_eff multiplies a quantity (n_pr)
that's signed and doesn't reflect quark-pairwise structure.

### F11a.6. What Phase 11a establishes

1. **Pool item g (α-attribution) is resolved.**  The charge-function
   projection `f(n_pt, n_pr) = n_pt/6 + n_pr/4` gives α universality
   at machine precision across all R64 inventory tuples.  The
   silent factor of 9 at the R64 proton is corrected.
2. **The Track 10 "σ_eff caps at 1" verdict was wrong.**  The
   metric supports σ_eff_ring values from 0 to ∞ within the
   signature-OK band; magnitude is freely tunable.
3. **The strong force's true obstruction is channel structure,
   not metric magnitude.**  Ring channel ties to signed n_pr and
   cannot give charge-symmetric, deuteron-binding strong force.
4. **Phase 11b (pairwise quark-quark cross term) is the
   architecturally indicated next test.**  A pairwise mass-content
   product `σ·Σᵢⱼ |n_pr,i|·|n_pr,j|` (or similar always-positive
   form) would naturally give charge symmetry and non-zero pn
   binding because each quark contributes |n_pr| = 2 regardless
   of sign.

### F11a.7. Implications for Track 10's architectural verdict

Track 10 concluded: "11D is the minimum metric for MaSt's EM
sector; aleph cannot be removed; σ_ra cannot be removed; **strong
force at full magnitude cannot fit in the metric**."

Phase 11a partially **reverses** the third point: the metric
*can* deliver σ_eff_ring = 116 within the signature band; the
magnitude is fine.  What the metric *cannot* deliver via the
ring channel alone is charge-symmetric strong force — and that's
because of channel structure (signed n_pr), not signature
constraints.

The architectural picture revised:

| Sector | Mechanism | Status |
|:---|:---|:---|
| Coulomb (tube → aleph → t) | σ_at, σ_ta — derived in R62 D5 | ✓ structural baseline |
| Magnetic (aleph → S) | σ_aS at α-magnitude | ✓ Phase 8 confirmed |
| α-attribution at R64 quark inventory | f(n_pt, n_pr) = n_pt/6 + n_pr/4 | ✓ Phase 11a F11a.2 |
| σ_ra prescription | (s·ε)·σ_ta — required (Phase 10c) | ✓ structural |
| Direct sheet-S couplings | tunable to any σ_eff at signature edge | ✓ Phase 11a F11a.4 |
| Charge-symmetric strong force | requires non-signed-n_pr coupling form | ✗ open (Phase 11b) |

The metric formalism is **not exhausted**; it has architectural
room for the strong force at the right magnitude.  The remaining
question is which projection of (n_pt, n_pr) (or which pairwise
quark-quark structure) gives the charge-symmetric phenomenology.

---

## Status

**Phase 11a complete.**

**Track 11 net result:**

- Pool item g resolved: f(n_pt, n_pr) = n_pt/6 + n_pr/4 gives
  α universality across the full R64 quark inventory at
  machine precision.
- Phase 10a's σ_eff cap of ~1 was a measurement artifact, not a
  structural ceiling.  σ_eff_ring is freely tunable up to ∞
  within the signature-OK band.
- The strong force's real architectural challenge is finding a
  cross-term form that's **charge-symmetric** and gives non-zero
  contribution at n_pr = 0 (the deuteron) — not finding magnitude.
- Track 10's "metric exhausted" conclusion is partially reversed:
  metric magnitude is sufficient; channel structure is the open
  question.
- **Phase 11b (pairwise vs linear cross term)** becomes the
  natural next test.  Replacing `σ·n_pr` with a pairwise
  quark-mass-content product would naturally give charge symmetry
  and non-zero pn binding.

**Pool item m (Yukawa propagator) is no longer architecturally
forced** — there's room in the metric for the strong force, given
the right cross-term structure.  Phase 11b will determine whether
pairwise quark-quark counting closes the channel-structure gap.
