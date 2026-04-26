# R64 Track 10 — Ring-S coupling: testing the mass-channel hypothesis

Track 10 tests whether the strong force originates in the **ring**
sector (mass-channel) rather than the **tube** sector (charge-channel)
of the p-sheet.  This reframes the strong-force search away from
σ_pS_tube (Tracks 7–9) toward σ_pS_ring as the primary direct
sheet-spacetime coupling.

The user's structural argument: gravity is always-attractive because
mass (= ring content) is always positive.  Coulomb is signed because
charge (= tube content) is signed.  The strong nuclear force is
gravity-like (always-attractive, charge-symmetric across pp/pn/nn),
suggesting its metric origin should be ring-related, not tube-related.

**Result: ring-S coupling is structurally α-inert (positive finding,
vindicates the mass-channel separation), but the deliverable σ_eff at
signature-permitted magnitudes is still too small for Phase 7c-class
strong force.  Outcome C: structural progress, magnitude unchanged.**

---

## Phase 10a — σ_pS_ring as primary direct coupling

Script:
[`scripts/track10_phase10a_ring_S_primary.py`](scripts/track10_phase10a_ring_S_primary.py) ·
Outputs:
[`outputs/track10_phase10a_universality_sweep.csv`](outputs/track10_phase10a_universality_sweep.csv) ·
[`outputs/track10_phase10a_potential_curves.csv`](outputs/track10_phase10a_potential_curves.csv) ·
[`outputs/track10_phase10a_potential_curves.png`](outputs/track10_phase10a_potential_curves.png)

### Method

Same machinery as Phase 7e + Phase 9b, with σ_pS_ring substituted for
σ_pS_tube as the primary direct sheet-S coupling:

1. Sweep σ_pS_ring alone across [−0.20, +0.20]; check signature
   (Lorentzian = one negative eigenvalue) and α universality across
   the 10 inventory modes.
2. Search for companion-entry prescriptions (R1: σ_aS = a·σ_pS_ring;
   R2: σ_pS_tube = b·σ_pS_ring; R3: both jointly).
3. At the best prescription, find the signature-OK band by
   incrementally extending σ_pS_ring with companion re-optimization.
4. Compute V(r) for pp, pn, nn channels using R64 Point B p-sheet
   parameters and the corrected two-body kinematic prefactor `4·(ℏc)²`
   (Phase 7c convention).

### F10a.1. σ_pS_ring alone preserves α universality structurally

The big positive finding: **σ_pS_ring requires no companion to preserve
α universality.**  Across all sweep values:

| σ_pS_ring | α-spread (no companion) |
|:---:|:---:|
| +0.001 | 5.4 × 10⁻¹⁵ |
| +0.005 | 5.4 × 10⁻¹⁵ |
| +0.010 | 5.4 × 10⁻¹⁵ |
| +0.025 | 5.4 × 10⁻¹⁵ |
| +0.050 | 1.0 × 10⁻¹⁴ |
| +0.10 | (signature still OK; spread tiny) |

This is qualitatively different from σ_pS_tube (Phase 7e), which broke
universality immediately at any non-zero value.

The companion searches (R1, R2, R3) all converged with companion
coefficients = 0 — confirming no companion is needed.  σ_pS_ring is
structurally α-inert.

### F10a.2. Why ring-S is α-inert and tube-S isn't

The structural reason: **charge lives in the tube sector**, not the
ring sector.

R62 D5 derives charge as the conserved Killing momentum P_4 in the
tube direction.  The α-extraction `α_Coulomb(G, n) = Q²/4π` depends
on the tube-row of the inverse metric (specifically G⁻¹[Ma, t]
projected on the tube components of the mode).

- σ_pS_tube directly modifies the tube-row of G⁻¹, perturbing α.
- σ_pS_ring modifies the ring-row, which doesn't enter the
  α-extraction calculation.

So **ring-S coupling is orthogonal to the charge sector by
construction.**  This is the user's mass/charge separation made
explicit at the metric level.

### F10a.3. Signature band under σ_pS_ring is wider

| Configuration | Signature-OK band |
|:---|:---:|
| σ_pS_tube alone (Phase 7e) | [−0.075, +0.075] |
| σ_pS_tube + companion H2 (Phase 9b) | [−0.0704, +0.0704] |
| σ_pS_tube + 2 companions H6 (Phase 9d) | [−0.102, +0.102] |
| **σ_pS_ring alone (Phase 10a)** | **[−0.122, +0.122]** |

Ring-S delivers the widest signature band of any tested coupling.
Combined with α-inertness, the ring channel is architecturally
"cleaner" than the tube channel.

### F10a.4. Schur-effective σ at the band boundary

At σ_pS_ring = ±0.109 (band boundary):

| Quantity | Value |
|:---|:---:|
| σ_eff_ring (Schur, full inverse) | ±1.133 |
| σ_eff_tube (Schur, induced) | ±0.557 |

The induced σ_eff_tube is a curiosity: σ_pS_ring at the metric level
generates a non-zero G⁻¹[p_t, S_x] entry through second-order Schur
mixing.  But its magnitude is small.

Both σ_eff_ring (~1.1) and σ_eff_tube (~0.5) at band boundary are
~100–200× too small for Phase 7c's σ_t = 116.

### F10a.5. V(r) decomposition by channel — the deuteron problem

V(r) computed at σ_pS_ring = ±0.109 (band boundary) for three
two-body compound modes:

| Channel | n_pt | n_pr | V_min (MeV) | r_min (fm) | V(∞) (Ma offset) |
|:---|:---:|:---:|:---:|:---:|:---:|
| pp (R64) | 6 | +4 | +0.03 | 49.2 (boundary) | +0.02 |
| **pn (R64)** | **6** | **0** | **−17.3** | **49.2 (boundary)** | **−17.31** |
| nn (R64) | 6 | −4 | +0.03 | 49.2 (boundary) | +0.02 |

The deuteron problem under ring-S coupling: **`n_pr(pn) = 0`** because
R64 has p = (3, +2) and n = (3, −2), summing to (6, 0).  So the
σ_pS_ring·n_pr cross-coupling is **identically zero for the
deuteron**.  pn's binding (−17.3 MeV) is purely the Ma-side
asymptotic offset (F7a.2 finding) — the (6, 0) compound mass formula
already gives this.

For pp (n_pr = +4) and nn (n_pr = −4), σ_pS_ring contributes
equal-magnitude opposite-sign cross-couplings.  But at signature-
permitted magnitudes, the cross-coupling contributions to V(r) are
tiny: pp and nn V_min ≈ +0.03 MeV vs the kinetic-dominated value of
~+0.05 MeV at sigma=0.  Negligible attraction.

So the channel-decomposition under σ_pS_ring direct coupling:

- **pp, nn**: V(r) almost purely kinetic; cross-coupling at
  signature-OK σ adds ~0.02 MeV — within noise.
- **pn**: V(r) ≈ −17 MeV asymptote (Ma side); σ_pS_ring contributes
  exactly zero because n_pr(pn) = 0.

### F10a.6. Charge symmetry holds, but trivially

The script's charge-symmetry check (V_min(pp) ≈ V_min(nn)) passes
at +0.03 MeV each.  But this isn't the charge-symmetric strong force
of nature — it's just kinetic dominance for both channels with
σ_pS_ring contributing too little to differentiate them.

### F10a.7. What Phase 10a establishes

1. **The ring channel is α-inert.**  σ_pS_ring can be activated
   directly in the metric without disturbing α universality, no
   companion entry required.  This is qualitatively different from
   σ_pS_tube (Phase 7e) and confirms the user's mass-channel /
   charge-channel structural separation at the metric level.

2. **Signature band under σ_pS_ring is widest of any tested coupling**
   (±0.122).  But σ_eff at the boundary (~1.1) is still ~100× too
   small for Phase 7c-class strong-force depth.

3. **The deuteron's pn n_pr = 0 means σ_pS_ring contributes
   identically zero to deuteron binding.**  The −17 MeV pn binding
   in the calculation is Ma-side offset only.  Pure ring-S coupling
   cannot be the source of the deuteron's strong-force binding.

4. **The architectural picture sharpens**: the metric supports a
   ring-S "gravity-like" channel (always-attractive in the sense
   of n_pr² type contributions, σ-symmetric under sign flip, α-inert)
   in parallel to the tube-S "Coulomb-like" channel.  Both channels
   exist; neither delivers strong-force *magnitude* at signature-OK
   values.

### F10a.8. Implications

The user's two-channel hypothesis is validated *structurally*:
- Tube channel (charge-related) carries Coulomb
- Ring channel (mass-related) is genuinely orthogonal — α-inert,
  wider signature band, charge-symmetric phenomenology

But neither channel delivers strong-force *strength*.  The signature
constraint caps σ_eff at ~1 across all tested couplings — Phase 7c's
116 magnitude is unreachable in the metric formalism.

The deuteron-specific issue (n_pr = 0 → σ_pS_ring contributes
zero) is structural under R64's u/d primitive assignment.  Either:

- The deuteron's binding is purely Ma-side offset (consistent with
  Phase 8c/9c findings; explains why metric routes can't reach
  Phase 7c depth — there isn't supposed to be any cross-coupling
  contribution).
- Or R64's u/d assignment isn't quite right, and a different
  primitive structure would give n_pr ≠ 0 for the deuteron.

The first reading is consistent with everything Phase 7–10 has
shown.  The second is a genuine architectural question that
Track 10 has surfaced but not resolved.

---

## Status

**Phase 10a complete.**

**Net Track 10 result:**

- σ_pS_ring direct coupling preserves α universality with no
  companion needed (positive structural finding; vindicates the
  user's mass-channel/charge-channel separation).
- Signature band under σ_pS_ring is the widest of any tested
  coupling (±0.122), but Schur σ_eff at boundary still too small
  (~1) for Phase 7c-class strong force (~116).
- The deuteron-specific result: σ_pS_ring contributes identically
  zero to the pn channel because n_pr(pn) = 0 under R64's u/d
  assignment.  pn binding in the calculation is purely the
  Ma-side asymptotic offset.
- Combined with Track 9: both metric channels (tube and ring) are
  exhausted; the strong force at full strength does not live in
  the 11D metric.

The structurally-clean two-channel architecture (Coulomb in tube,
gravity-like in ring) is validated.  The strong force's magnitude
question remains open and points outside the metric — propagator-
based formalism (R64 pool item m) or some other extension.
