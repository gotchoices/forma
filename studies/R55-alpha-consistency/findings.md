# R55: α consistency — Findings

## Track 1: Schur complement transfer function

### F1. Per-mode energy fractions are NOT universal

The Schur complement approach — computing how much of a mode's
energy is diverted into S by the Ma-S coupling — gives
mode-dependent coupling.  Different modes on the same sheet get
different α_eff values for the same Ma-S entries.

Specifically: modes proportional to the reference mode get
exact α_eff = 1/137, but all other modes deviate.

| Sheet | ε | s | off-diag ratio | Universality |
|-------|---|---|----------------|-------------|
| p-sheet | 0.55 | 0.162 | 0.089 | Good — proton, deuteron, iron exact |
| ν-sheet | 5.0 | 0.022 | 0.109 | Fair — ν₁ exact, ν₂ 0.3% off |
| e-sheet | 397 | 2.004 | 0.894 | Poor — only (n, 2n) modes match |


### F2. The off-diagonal ratio depends only on shear, not ε

The anisotropy of the 2×2 sheet metric is:

> off-diag ratio = |s| / √(1 + s²)

This depends ONLY on the shear s, not on the aspect ratio ε.
Reducing ε (making the torus less elongated) does not improve
universality.  Only reducing s helps.


### F3. Low-ε solutions exist but don't help

A systematic search found solutions with ε as low as 19
(electron mode (1,14), s = 14) that produce three lepton
generations within 3%.  However, these have HIGHER shear and
WORSE universality (off-diag ratio = 0.998).

There is a fundamental tension:
- Three generations require shear resonance at s ≥ 1
- Universal coupling (in the Schur picture) requires s << 1
- These constraints are incompatible on the e-sheet


### F4. The Schur complement is the wrong coupling model

The universality condition requires BBᵀ ∝ A (the Ma-S
correction must be proportional to the full metric).  Since
BBᵀ is rank-1 and A is rank-2, this is mathematically
impossible except when A is degenerate (s → 0 or ε → ∞).

This means the per-mode energy fraction is NOT the physical
definition of α.  In real physics, α is the same for all
charged particles — it's a property of the electromagnetic
field, not of the source.  The Schur complement computes a
mode-specific quantity that happens to equal the physical α
only for modes aligned with the reference direction.


### F5. Ma-S numerical values found

Despite the universality failure, Track 1a solved for Ma-S
entries that give α for the reference modes:

| Strategy | σ(e-ring→S) | σ(p-tube→S) | σ(p-ring→S) | σ(ν-ring→S) |
|----------|------------|------------|------------|------------|
| Proportional | 0.095 | 0.038 | 0.038 | 0.046 |
| Ring-only | 0.057 | — | 0.058 | 0.050 |
| Uniform | 7.2×10⁻⁵ | 0.038 | 0.038 | 0.046 |

All values are O(0.03–0.06), which is O(√α) not O(α).
The Ma-S entries are larger than previously assumed.


### F6. Internal shears DO affect Ma-S coupling

The effective coupling through the Schur complement depends
on both the internal metric A (which contains shears) and
the Ma-S entries B.  Internal shears tilt the mode energy
distribution, changing how the Ma-S entries project that
energy into S.

However, this is a property of the Schur complement
approach, not necessarily of the physical coupling.  If α
is a field-level property (F4), then internal shears may
not affect the gauge coupling at all.


### F7. Neutrino sheet coupling is nonzero and well-behaved

When the ν-sheet is allowed to couple to S at α (not assumed
zero), the Ma-S solution is well-behaved and the universality
across neutrino modes is the best of all three sheets
(off-diag ratio = 0.02).

There is no experimental or theoretical reason to force
ν-sheet Ma-S coupling to zero.  Standard physics assigns
zero electromagnetic coupling to neutrinos, but MaSt predicts
modes on the ν-sheet still couple to S through the metric.
This coupling is what L05 proposes to detect.


## Track 1a status

**Complete.** The Schur complement approach is understood and
its limitations are characterized.  The per-mode energy
fraction is not the physical α — it is a mode-dependent
quantity that only equals α for modes aligned with the
reference direction.  The physical α must be computed as a
field-level (gauge) property of the geometry.

## What was learned

1. Ma-S entries are O(√α) ≈ 0.03–0.06, not O(α) ≈ 0.007
2. Internal shears affect the Schur complement but may not
   affect the gauge coupling
3. The off-diagonal ratio = |s|/√(1+s²) controls universality
   in the Schur picture and depends only on shear, not ε
4. No alternative e-sheet geometry avoids the tension between
   generations (needs s ≥ 1) and Schur universality (needs s << 1)
5. The resolution is likely that α is a field-level property
   (KK gauge coupling) that is automatically mode-independent

## Proposed Track 2 direction

The charge formula Q = −n₁ + n₅ assigns charge to tube
winding numbers: n₁ (e-tube, dimension 0) and n₅ (p-tube,
dimension 4).  In standard Kaluza-Klein theory, the gauge
coupling for a charge associated with compact dimension i is:

> α_i ∝ (σ_i / L_i)²

where σ_i is the Ma-S entry and L_i is the circumference.
This coupling is a property of the GEOMETRY (σ_i and L_i),
not of the MODE.  It is automatically universal.

The internal shear s does not appear in this formula because
it mixes compact dimensions with each other, not with S.
The gauge coupling only involves the Ma-S entries.

For α_electron = α_proton:
> σ_eT / L_eT = σ_pT / L_pT

This determines the ratio of Ma-S entries from the known
circumferences.  A single normalization then sets both
to give α = 1/137.

This approach bypasses the Schur complement entirely and
uses the KK gauge coupling directly.  It is clean,
computable, and resolves the universality problem by
construction.

**Caveat:** the standard KK formula may need correction
for a sheared compact space.  The shear mixes compact
dimensions, which could modify the gauge field normalization.
Track 2 would compute this correction.


## Track 3: ℵ-mediated coupling (10×10 metric)

### F8. The e-tube is at PD saturation — no room for Ma-S coupling

The e-tube ↔ e-ring off-diagonal ratio in the 6×6 metric is
0.999999 — exactly at the positive-definiteness boundary.
The e-sheet's large internal shear (s_e = 2.004) has consumed
ALL of the e-tube's off-diagonal budget.  Any additional
coupling on dimension 0 (e-tube) makes the metric invalid.

This is why hypotheses A and C (which couple tube dimensions
to ℵ) fail positive-definiteness: the e-tube can't support
any additional off-diagonal entries.


### F9. Hypothesis F (ring-only coupling) works

Coupling through the RING dimensions (not tubes) avoids the
PD saturation.  The e-ring diagonal is 633,324 — a coupling
of 0.16 is negligible relative to it.

Ma-ℵ entries: [0, −1/(2π), 0, +1/(2π), 0, +1/(2π)]
(ring dimensions only, at ±1/(2π) = ±0.1592)

This is physically motivated: ℵ as an angular coordinate
(radians), with the Ma-ℵ coupling converting between length
and angle at the rate of 1/(2π) per full rotation.


### F10. σℵS = 0.2902 gives exact α for the electron

Binary search finds σℵS = 0.29019 such that α_eff(electron)
= α = 1/137.036 to 6 decimal places.

The effective product (1/2π) × σℵS = 0.0462, which is
0.541 × √α.  This is NOT exactly √α — the Schur complement
introduces corrections from the internal Ma metric structure.


### F11. Near-universal α across e-sheet and p-sheet

At the optimal σℵS:
- Electron: α_eff = 1.000α (exact, by tuning)
- Proton: α_eff = 0.964α (3.6% low)
- All nuclei (d, He, C, Fe): α_eff = 0.964α (identical to proton)
- Σ⁻: α_eff = 0.955α (4.5% low)

The 3.6% gap between e-sheet and p-sheet is the residual
non-universality.  It comes from the different internal
shears on each sheet affecting the Schur complement when ℵ
is integrated out.

This is the FIRST approach that achieves near-universal
coupling across both sheets.  Track 1's best result had 30%+
spread.


### F12. Neutrino couples at 1.07α — nonzero

The ν-ring couples to ℵ at +1/(2π), giving the ν-sheet a
nonzero coupling to S of 1.07α.  This is close to the
charged-particle coupling, supporting the L05 premise that
neutrino Compton frequencies can be excited by electromagnetic
energy.


### F13. Spectrum shifts are ~1.3% — manageable

The ℵ-mediated coupling shifts mode energies:
- Proton: 938.3 → 950.6 MeV (+1.3%)
- Electron: 0.511 → 0.518 MeV (+1.4%)

These shifts are small enough to be compensated by re-tuning
ε_p and ε_e by ~1%.  The particle ZOO structure (which modes
match which particles) is unchanged.


### F14. Compound particles show wider α spread

Multi-sheet modes (with complex winding numbers) show α_eff
values from 0.26α (Ξ⁻) to 2.30α (K±).  This reflects the
non-trivial interaction of cross-sheet shears with the
ℵ-mediated coupling.  The universality holds for fundamental
single-sheet modes and their nuclear composites, but not for
all compound baryons and mesons.


### F15. Charge and coupling are now fully separated

| Phenomenon | Mechanism | Where in metric |
|------------|-----------|-----------------|
| Charge sign | Tube winding (n₁, n₅) | Topology (winding numbers) |
| Charge quantization | 2π periodicity on tube | Compactness |
| Charge magnitude | ℵ-S coupling × Ma-ℵ | Off-diagonal: ℵ row/column |
| Generation structure | Internal shear (s_e, s_p) | Ma-Ma off-diagonal |
| Compound modes | Cross-sheet shears (σ₄₅...) | Ma-Ma off-diagonal |
| ν neutrality | ν-tube resolution below threshold | Size argument (Q102) |
| ν coupling | ν-ring → ℵ → S | Same Ma-ℵ mechanism as charged sheets |

The ℵ dimension cleanly separates all five types of
off-diagonal physics.  No entry serves double duty.


## Track 3 status

**Complete.**  The ℵ-mediated coupling (hypothesis F) achieves
near-universal α (3.6% spread vs Track 1's 30%+), preserves
the particle spectrum to ~1.3%, and provides nonzero ν coupling
consistent with L05.

## Open for future work

1. **Close the 3.6% gap:**  The e-p universality gap may close
   with a more sophisticated Ma-ℵ coupling (not exactly 1/2π
   for all rings) or with corrections from the cross-sheet
   entries.

2. **Re-tune ε_p, ε_e** to compensate the ~1.3% spectrum shift.
   This is a parameter adjustment, not a structural change.

3. **Derive σℵS from GRID.**  Currently tuned to give α.  If
   the sim-impedance junction leakage mechanism determines σℵS,
   it would derive α from geometry.

4. **Time dimension.**  The 10×10 metric is spatial.  Adding
   time would give 11×11 and might be needed for dynamic
   processes (decay, scattering).

See [metric-terms.md](metric-terms.md) for the full 10×10
reference table.
