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
