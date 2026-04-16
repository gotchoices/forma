# R55: α consistency check — Ma-S coupling derivation

**Status:** Track 1 complete — initial results
**Questions:** Q115 (metric structure), Q116 (T⁶ vs sheets)
**Type:** theoretical + compute
**Depends on:** R54 (particle inventory, metric terms), R19 (original α formula), R48 (charge mechanism)

---

## Motivation

R54 established a particle inventory (18/20 spin-correct modes)
and identified the 9×9 metric structure with four types of off-
diagonal entries serving distinct physical roles.  The Ma-S coupling
block (18 entries, reduced to ~4 effective by isotropy and inactive
dimensions) determines α = 1/137 — the fraction of a mode's
internal energy that appears as Coulomb field in 3D space.

The current state: we ASSUME the Ma-S entries are ~ O(α), but
we have no formula connecting them to α.  R19 derived such a
formula for the in-sheet shear, but that formula conflated charge
creation (topological, from GRID) with spatial coupling (geometric,
from Ma-S).  A new derivation is needed.

## Questions

1. **Can the R19 formula be re-derived for the Ma-S context?**
   R19 computed how a mode's energy, distributed across the torus
   by the in-sheet shear, projected into 3D space.  The same
   physics applies to the Ma-S block: the mode's energy on Ma
   projects into S through the Ma-S entries.  The derivation
   follows the same path but uses different metric entries.

2. **Is α universal?**  If we solve for Ma-S entries that give
   α = 1/137 for the electron, do the same entries give α = 1/137
   for the proton, muon, and all other charged modes?  Universality
   is required — α is the same for all charged particles in nature.

3. **Is the Coulomb self-energy correct?**  For a charged mode at
   the R54 geometry, does U_Coulomb = α × mc²?  This is the
   definitive test: one unit of energy in, 1/α units of Coulomb
   energy out.

4. **Can we model a hydrogen atom?**  With the complete 9×9 metric,
   the electron and proton have masses (from Ma block) and coupling
   (from Ma-S block).  The hydrogen energy levels should follow from
   standard QM.  More interestingly: does the Ma structure predict
   anything non-trivial (like the proton charge radius or the Lamb
   shift) that goes beyond what α and masses alone provide?

## Theory

The key insight from R54 Track 3 (F16–F21): charge is topological
(GRID tube winding), but α coupling is geometric (Ma-S projection).
R19 conflated them.  In the correct picture:

- A mode with n₁ = 1 has charge e regardless of shear
- The in-sheet shear s_e controls generation structure (R53)
- The Ma-S shear σ_MaS controls how much of the charge's
  energy reaches S

The internal shears can be arbitrarily large (s_e = 2.004) without
affecting α, because α depends on the Ma-S block, not the Ma block.
Any distortion created by internal shears can be compensated by the
right Ma-S entries.  The metric is symmetric — the coupling works
both directions through the same entries.

## Proposed approach

### Track 1: Numerical Ma-S transfer function (computational)

**Concept:** Build the full 9×9 metric (Ma + S), inject a mode
perturbation into Ma, and compute what fraction of the mode's
energy "makes it" into S.  The Ma-S shear entries are free
parameters; sweep them to find values where the effective
coupling equals α = 1/137.

**Why this works:** The 9×9 metric in block form is:

```
G = | A    B  |      A = 6×6 Ma metric (known)
    | Bᵀ   C  |      C = 3×3 S metric (identity, flat)
                      B = 6×3 Ma-S coupling (unknown)
```

A mode at rest in S has winding vector ñ = (n₁/L₁,...,n₆/L₆, 0, 0, 0).
Its energy in the full 9D metric is:

```
E² ∝ ñ_Maᵀ [G⁻¹]_Ma,Ma ñ_Ma
```

where [G⁻¹]_Ma,Ma = (A − B C⁻¹ Bᵀ)⁻¹ is the effective Ma
metric with S coupling included.  Without coupling (B = 0),
this reduces to A⁻¹.  The difference between the coupled and
uncoupled energies measures how much energy the Ma-S entries
divert into S — i.e., the Coulomb coupling.

**Method:**

1. Build the 6×6 Ma metric A from model-E parameters (known:
   ε_e, s_e, ε_p, s_p, ε_ν, s_ν, all cross-sheet σ)
2. Build the 6×3 Ma-S block B parameterized by 4 effective
   entries (e-ring→S, p-tube→S, p-ring→S, ν-ring→S = 0).
   Spatial isotropy means each Ma dimension has a single
   coupling to all three S directions.  Inactive dimensions
   (e-tube, ν-tube) are 0.  Sign convention: e-ring negative,
   p-tube and p-ring positive.
3. Compute E²_bare = ñᵀ A⁻¹ ñ (Ma only, no S coupling)
4. Compute E²_coupled = ñᵀ (A − B C⁻¹ Bᵀ)⁻¹ ñ (with S coupling)
5. Define α_eff(mode) from the energy fraction
6. Sweep the Ma-S parameters to find values where α_eff = 1/137

**Key constraint: universality.** The same Ma-S entries must
give α_eff = 1/137 for ALL charged modes simultaneously:
- Electron (1, 2, 0, 0, 0, 0) — e-sheet, ε = 397
- Proton (0, 0, −2, 2, 1, 3) — p-sheet, ε = 0.55
- Muon (1, 1, −2, −2, 0, 0) — e-sheet, different winding
- Neutrino (0, 0, 0, 0, 1, 1) — must give α_eff = 0

Universality with 4 unknowns and 4+ constraints leaves the
system nearly or over-determined.

**Possible outcomes:**

| Result | Meaning |
|--------|---------|
| One B solution with universal α = 1/137 | α is geometrically determined by Ma-S entries |
| No B works for all modes | Energy-fraction picture incomplete; Ma-S coupling is more subtle |
| Multiple B solutions | Need additional constraint to select the physical one |
| α_eff depends on mode regardless of B | Universality fails — model has a problem |

### Track 2: Analytical consistency (theoretical, follow-up)

If Track 1 finds a solution:
1. Examine the Ma-S values — do they have a pattern?
2. Check whether the Coulomb self-energy U = α_eff × mc² holds
3. Check the hydrogen binding energy (13.6 eV)
4. Compare the proton charge radius prediction

If Track 1 finds no solution:
1. Diagnose why — which modes break universality?
2. Consider whether the linear transfer-function picture needs
   nonlinear corrections (field profile in S, backreaction)
3. Revisit the KK analytical derivation for the specific failing case

## Deliverables

- The α_eff transfer function as a computable function of
  Ma-S entries and mode winding numbers
- Numerical Ma-S values for α = 1/137 (if they exist)
- Universality check (electron, proton, muon, neutrino)
- Assessment: is α determined by the geometry or still free?
