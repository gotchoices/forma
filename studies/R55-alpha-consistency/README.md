# R55: α consistency check — Ma-S coupling derivation

**Status:** Framed — not yet started
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

### Phase 1: Derive the α formula (theoretical)

Re-derive the R19 result in the 9×9 context:
1. Write the mode's electromagnetic field on the 9D manifold
2. The Ma-S entries determine how the field extends from Ma into S
3. Integrate the field energy in S → this is U_Coulomb
4. U_Coulomb / E_mode = α → formula for α in terms of Ma-S entries

### Phase 2: Solve for Ma-S entries (algebraic)

Given the formula from Phase 1:
1. Set α = 1/137 for the electron mode (1,2,0,0,0,0)
2. Solve for the Ma-S entries
3. Check universality: same entries → same α for proton (0,0,0,0,1,3)

### Phase 3: Consistency check (computational)

With the derived Ma-S entries:
1. Compute the Coulomb self-energy of the electron → should be αmc²
2. Compute the Coulomb self-energy of the proton → should be αMc²
3. Compute the hydrogen binding energy → should be 13.6 eV
4. Check the proton charge radius prediction

## Deliverables

- The α formula in terms of Ma-S metric entries
- Numerical Ma-S values for α = 1/137
- Universality check (electron, proton, muon)
- The complete 45-entry metric with no free parameters
