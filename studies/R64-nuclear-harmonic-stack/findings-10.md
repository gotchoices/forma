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

---

## Phase 10c — Architecture test: σ_ra = 0 with direct sheet-S replacement

User-proposed simplification: aleph mediates **only** the tube
(charge) sector; the ring sector lives entirely in direct sheet-S
coupling.  This would zero out R60 T7's σ_ra = (s·ε)·σ_ta
prescription and replace its role with σ_pS_ring (or some
combination of sheet-S entries).  If it works, the aleph row
simplifies and the architecture cleanly separates: charge through
aleph, mass through direct S.

Script:
[`scripts/track10_phase10c_no_sigma_ra.py`](scripts/track10_phase10c_no_sigma_ra.py)
Output:
[`outputs/track10_phase10c_no_sigma_ra.csv`](outputs/track10_phase10c_no_sigma_ra.csv)

### F10c.1. σ_ra = 0 breaks signature, not just universality

Setting σ_ra = 0 (with no other modification) gives:

- **Signature is no longer Lorentzian** (multiple negative eigenvalues
  appear in the 11×11 metric).
- α universality spread: ~12.6 (catastrophic — modes vary by factor
  10× from each other).

Mode-by-mode α/α_expected with σ_ra = 0:

| Mode | α/α_expected |
|:---|:---:|
| electron | 12.50 |
| muon | 12.53 |
| proton | 0.00 (effectively no charge) |
| neutron | 0.00 (effectively no charge) |
| Λ | 12.63 |
| π⁰ | 0.00 |
| K± | 1.38 |
| ρ | 1.41 |

The proton's α going to zero is particularly striking — without σ_ra,
the ring sector's contribution to charge isn't routed correctly
through aleph, and the proton (which has mostly p-sheet ring content
n_pr = 3) loses its EM coupling.

### F10c.2. Direct sheet-S coupling cannot restore α universality

Three compensation hypotheses tested with σ_ra still set to zero:

- **C1**: σ_pS_tube + σ_pS_ring jointly free
- **C2**: + σ_aS (3-parameter)
- **C3**: 3-sheet symmetric extension (R60-T7-style ring companions
  on each sheet, with cross-sheet symmetric prescription)

All three searches failed to find a Lorentzian-signature
configuration that preserves α universality.  The optimizer was
never able to navigate out of the signature-broken region —
direct sheet-S entries do not couple in the right place to
fix the signature failure caused by removing σ_ra.

### F10c.3. σ_ra is structurally required, not a convenience

The architectural conclusion is decisive: **R60 T7's σ_ra
prescription is genuine and required**.  Three independent
observations confirm this:

1. **Signature**: σ_ra is needed to keep the 11×11 metric
   Lorentzian when σ_ta is active.  No combination of direct
   sheet-S entries restores signature.
2. **α universality**: Without σ_ra, charge extraction breaks for
   any mode with non-zero ring content.  The proton's charge
   becomes zero numerically.
3. **Substitution failure**: σ_pS_ring (or any direct sheet-S
   entry) does NOT play the same metric-structural role as σ_ra.
   Even though both involve the ring index, they sit in different
   inverse-metric paths and have different effects on α-extraction.

### F10c.4. Why the user's proposal can't work

The structural reason: **σ_ra and σ_pS_ring affect different
inverse-metric entries.**

- σ_ra connects ring → aleph → time, contributing to G⁻¹[Ma, t]
  (the column α-extraction reads).
- σ_pS_ring connects ring → S spatial directly, contributing to
  G⁻¹[Ma, S] (a different column entirely).

α-extraction projects onto G⁻¹[Ma, t].  σ_pS_ring doesn't enter
this projection at leading order, so it can't substitute for σ_ra's
role.

The architectural simplification "aleph mediates only tube" can't
be achieved by replacing σ_ra with sheet-S entries, because the
two metric structures occupy different functional roles.

### F10c.5. What this clarifies

Negative results have value.  Phase 10c clarifies that:

- **σ_ra is a structural feature of the 11D metric**, not a
  T7-specific convenience.  R60's architecture genuinely requires
  ring-aleph coupling.
- **Aleph mediates BOTH tube and ring**, with the σ_ra prescription
  ensuring α universality across the inventory.  This is the
  architecture; it can't be simplified by routing ring through S
  instead.
- **The user's "only tube couples to aleph" hypothesis** doesn't
  survive: the tube-only aleph row breaks both signature and
  universality.

This sharpens Q135's hub-and-spoke principle: aleph mediates the
full tube+ring sector, with σ_ra as the structural prescription
linking them.  Direct sheet-S couplings (as in Tracks 9 and 10a)
are *additional* channels on top of the aleph-mediated baseline,
not replacements for it.

The architectural picture is now:

| Channel | Status |
|:---|:---|
| Aleph-mediated EM (tube → aleph → time, ring → aleph derived) | structural baseline; cannot be reduced |
| σ_aS (aleph → S, α-magnitude) | completes EM with magnetic vector potential (Phase 8) |
| σ_pS_tube direct (with H2 prescription) | architecturally allowed at signature-permitted magnitudes (Phase 9) |
| σ_pS_ring direct (α-inert) | architecturally allowed without companion (Phase 10a) |
| σ_ra absent | structurally **forbidden** — breaks signature (Phase 10c) |

The strong-force-magnitude question stands: even with both
sheet-S channels available alongside the full aleph row, σ_eff is
capped at ~1 by signature constraints.  The metric route is
genuinely exhausted; propagator-based formalism (R64 pool item m)
remains the architectural next step for strong-force magnitude.

---

## Phase 10b — Aleph-redundancy audit (full removal test)

User-proposed simplification beyond Phase 10c: remove the aleph
dimension entirely, replacing the aleph row with direct
sheet-spacetime entries (σ_xt_t, σ_xr_t for each sheet).  If
the 11×11 metric can simplify to effectively 10×10 with direct
sheet-time couplings preserving α universality and the right α
magnitude, aleph is removable.

Script:
[`scripts/track10_phase10b_aleph_redundancy.py`](scripts/track10_phase10b_aleph_redundancy.py)
Output:
[`outputs/track10_phase10b_aleph_audit.csv`](outputs/track10_phase10b_aleph_audit.csv)

### F10b.1. Zeroing aleph collapses all charges to zero

Setting all aleph row entries to zero (σ_ta, σ_at, σ_ra, σ_aS = 0)
gives:

- Signature OK ✓
- α-spread = 0 (trivially)
- **α(proton) = 0** (and α(electron), α(every charged mode) = 0)

The proton's charge collapses because there's no metric path from
`p_tube` to `time` once aleph is removed.  Charge generation is
literally absent without the aleph mediation.  Universality holds
trivially (zero = zero everywhere).

### F10b.2. Direct sheet-time entries cannot recover α magnitude

Three hypotheses tested with α-magnitude penalty included in the
cost function (to filter out degenerate "all α = 0" solutions):

| Hypothesis | n_params | best α(proton) | target α |
|:---|:---:|:---:|:---:|
| H_T1: only σ_pt_t | 1 | 1.5 × 10⁻³⁴ | 7.3 × 10⁻³ |
| H_T2: σ_xt_t for all 3 sheets | 3 | 5.9 × 10⁻³² | 7.3 × 10⁻³ |
| H_T3: σ_xt_t + σ_xr_t for all 3 sheets | 6 | 1.2 × 10⁻³⁴ | 7.3 × 10⁻³ |

All three optimizations stuck at the magnitude-penalty floor
(cost ≈ 0.10).  The optimizer could not find direct-coupling
configurations that produce α(proton) at any meaningful fraction
of 1/137 — values are 30+ orders of magnitude too small.

### F10b.3. Why direct sheet-time can't replace aleph

The structural reason: aleph's α-architecture has a specific
Schur path that produces α at the right magnitude:

`α ∝ σ_ta · σ_at / g_aa = √α · 4πα / 1 ≈ α`

This is a *product* of two off-diagonals (σ_ta and σ_at) divided
by a diagonal (g_aa = 1).  The product structure naturally
produces α-magnitude coupling.

Direct σ_pt_t entries enter the inverse metric as:

`G⁻¹[p_t, t] ≈ -σ_pt_t / (g_pp · g_tt)`

This is a single off-diagonal divided by two diagonals.  At
R64 Point B with g_pp = ε_p² ≈ 0.04 and g_tt ≈ −1, the scaling
behaves differently, and the optimizer cannot find a stable
basin where α(proton) ≈ 1/137 with universality across the
inventory.

### F10b.4. Verdict

**Aleph is structurally required for charge generation.**  Three
independent pieces of evidence:

1. **Without aleph, charge collapses** (F10b.1).  No metric path
   from sheet-tube to time means no Coulomb coupling.
2. **Direct sheet-time entries cannot replace aleph** at meaningful
   α magnitudes (F10b.2).  Optimization stuck at 30+ orders below
   target.
3. **Phase 10c showed even partial aleph removal** (just σ_ra = 0)
   breaks signature catastrophically.  Aleph is not a
   convenience layer; it's structural.

The user's "10D aleph-removal" simplification does not survive
the test.  R60's 11D architecture is the minimum required for
the EM sector.

### F10b.5. What this finalizes for Track 10

Combined results across Phase 10a, 10b, 10c:

| Test | Result | Architectural conclusion |
|:---|:---|:---|
| 10a: σ_pS_ring as primary direct coupling | α-inert; σ_eff still capped ~1 | Ring channel is structurally clean (mass-channel) but magnitude-limited |
| 10c: σ_ra = 0 (just remove ring-aleph) | Signature breaks, charge collapses | σ_ra is structural, not a convenience |
| **10b: full aleph removal** | **No direct replacement found** | **Aleph itself is structurally required** |

The architectural floor:
- **11D is the minimum metric for MaSt's EM sector.**  Aleph
  cannot be removed; σ_ra cannot be removed.
- **Both tube and ring couple to aleph** — that's the structure.
- **Direct sheet-S couplings are allowed** as additional channels
  on top of the aleph baseline (Phases 9b, 10a), but capped at
  σ_eff ~ 1 by signature constraints.
- **Strong force magnitude (Phase 7c required σ_eff ≈ 116) cannot
  fit in the metric**, regardless of which channels are activated.

The architectural picture is now closed:

| Sector | Mechanism |
|:---|:---|
| Coulomb (tube → aleph → t) | σ_at, σ_ta — derived in R62 D5 |
| Magnetic (aleph → S) | σ_aS at α-magnitude — completes EM (Phase 8) |
| Ring sector universality preservation | σ_ra = (s·ε)·σ_ta — required (Phase 10c) |
| Direct sheet-S couplings | allowed with prescriptions, capped at σ_eff ~1 |
| Strong force at full magnitude | **outside the metric** — propagator route |

Track 10 (a, b, c) plus Track 9 (a, b, c, d) together exhaust the
metric architecture for the strong sector.  Pool item m
(Yukawa propagator extension) becomes the architecturally
unavoidable next path.
