# R54: Compound modes on the full T⁶

**Status:** Framed — waiting for R53 Tracks 5–7
**Questions:** Q115 (metric structure), Q116 (T⁶ vs three sheets)
**Type:** compute / theoretical
**Depends on:** R53 (single-sheet precision values), R50 (particle
inventory), R49 (neutrino sheet)

---

## Motivation

R53 established that in-sheet shear resonance produces three
generations on each sheet independently:

| Sheet | Family | Modes | ε | s |
|-------|--------|-------|---|---|
| Ma_e | leptons (e, μ, τ) | (1,3), (3,8), (3,−8) | 330 | 3.004 |
| Ma_p | up quarks (u, c, t) | (1,3), (−1,3), (3,9) | 0.5 | 2.000 |
| Ma_p | down quarks (d, s, b) | (5,4), (1,1), (5,5) | 570 | 0.799 |
| Ma_ν | neutrinos (ν₁, ν₂, ν₃) | (1,1), (−1,1), (1,2) | 5.0 | 0.022 |

But many particles are NOT single-sheet modes.  The neutron spans
all three sheets.  The muon and tau need charge compensation from
the proton sheet.  The down-type quarks may be compound e+p modes
(Q116 §4) rather than pure p-sheet modes.  Hadrons (proton,
neutron, mesons, baryons) are bound states of quarks — compound
modes on the full T⁶.

R54 takes the single-sheet foundations from R53 and builds the
compound-mode picture on the full 6D torus.  The key new
ingredient is the **cross-sheet coupling** (the 12 off-diagonal
entries of the 6×6 metric that R53 did not use).


## What R53 provides (prerequisites)

From R53 Track 7 (compatibility assessment):
- Precision values for (ε_e, s_e, ε_p, s_p, ε_ν, s_ν)
- L_ring values for each sheet
- Mode assignments for all single-sheet particles
- Ghost inventories at each geometry

R54 inherits these as inputs and adds the cross-sheet structure.


## Key questions

1. **Can the e-p cross-shear σ_ep differentiate up-type from
   down-type quarks?**  If up quarks are pure p-sheet modes and
   down quarks are compound e+p modes (per Q116 §4), then σ_ep
   provides the second degree of freedom that eliminates the need
   for two p-sheet shears.  This is the most important structural
   question.

2. **What are the proton and neutron as compound modes?**  The
   proton (uud) and neutron (udd) are three-quark bound states.
   In the T⁶ picture, they are 6D knots threading multiple
   dimensions.  R54 should find their 6-tuples and compute their
   masses from the full metric.  The proton mass (938 MeV) becomes
   a prediction, not an input.

3. **Do the 4 entries of each cross-block matter, or is 1 scalar
   per block sufficient?**  R50 collapsed each 2×2 cross-block
   to one scalar.  R54 should test whether the structured 2×2
   block (tube-tube, tube-ring, ring-tube, ring-ring couplings)
   provides the physics that the scalar missed.

4. **What is α = 1/137 in the full T⁶?**  R53 showed that α
   cannot come from in-sheet shear.  R54 should determine whether
   α comes from a Ma-S cross term or from a specific combination
   of the 6×6 metric entries.


## Priority

**The proton and neutron are the proof.  Everything else is
supporting structure.**

Finding quarks, generations, and shear resonances is valuable
for understanding the geometry.  But the model succeeds or fails
on whether a compound 6-tuple exists at 938.272 MeV (Q = +1,
spin ½, stable eigenmode) and another near 939.565 MeV (Q = 0,
spin ½, near-miss).  If we find those, the framework works.
If we don't, nothing else matters.

Track 3 (hadron masses) is therefore the PRIMARY deliverable.
Tracks 1–2 are setup; Track 4 (α) is secondary.


## Tracks (preliminary)

### Track 1: Structured cross-block — σ_ep as a 2×2 matrix

Test whether the 4 independent entries of the e-p cross-block
can simultaneously:
- Set the neutron mass (currently σ_ep ≈ −0.13 from R50)
- Differentiate up-type from down-type quarks
- Preserve the R53 single-sheet generation structure

### Track 2: Down quarks as compound e+p modes

Enumerate compound modes (n₁, n₂, 0, 0, n₅, n₆) with both
e-sheet and p-sheet content.  Score against d, s, b masses.
Test whether the e-p cross-coupling naturally produces the
down-type mass hierarchy without a separate p-sheet shear.

### Track 3: Hadron mass predictions

Build the proton (uud) and neutron (udd) as composite 6-tuples.
Compute their masses from the full 6×6 metric.  Compare to 938
and 939.6 MeV.  This is the ultimate test of the compound
picture: can the proton mass emerge from quark modes + binding?

### Track 3: α from the Ma-S coupling

**Status:** Pending

**Goal:** Derive the Ma-S cross terms (the 6×3 block of the
9×9 metric) such that α = 1/137 emerges as the impedance
mismatch between Ma modes and 3D space.

**Physical picture:** α is the fraction of a mode's internal
energy (on Ma) that leaks into the spatial lattice (S) as
Coulomb field.  The leakage depends on how the mode's energy
distribution in Ma projects onto the S directions through the
Ma-S cross terms.  The internal Ma shears (s_e, s_p, σ's)
affect this projection by changing how energy is distributed
across the Ma dimensions.

**Method:**
1. Compute the electron mode's energy distribution across
   the 6 Ma dimensions at the R54 geometry.
2. Impose isotropy in S (coupling to S_x = S_y = S_z)
   and zero coupling for inactive dimensions (e-tube, ν-tube).
3. Solve for the remaining Ma-S entries such that the total
   coupling² / E² = α for the electron.
4. Verify: does the same set of Ma-S entries give α = 1/137
   for the proton and other charged particles?

**Key question:** Is α universal — one set of Ma-S entries
gives the same coupling for all charged modes?  If yes, the
framework is self-consistent.  If different particles need
different Ma-S values, the coupling mechanism is more complex.

**Deliverable:** The 6×3 Ma-S block values, or a formula
relating them to α and the internal Ma metric.

**Script:** `scripts/track3_alpha.py`


## Design decision: all 15 off-diagonal entries, not 6

The 6×6 symmetric metric has 21 independent components — 6
diagonal (circumferences) and 15 off-diagonal (shears).  Model-D
collapsed the 15 into 6: three within-sheet shears (s_e, s_ν, s_p)
and three scalars (σ_ep, σ_eν, σ_νp), each scalar controlling a
2×2 cross-block uniformly.

**R54 works with all 15 individually.**  The consolidation was an
artifact of the three-sheet view (Q116 §2).  There is no physical
reason for σ₁₅ (e-tube ↔ p-tube) to equal σ₂₆ (e-ring ↔ p-ring).
The directional selectivity of individual entries is likely what
differentiates compound modes (e.g., up vs down quarks).

The full metric structure:

```
         e_tube  e_ring  ν_tube  ν_ring  p_tube  p_ring
e_tube  [ L₁²     s_e     σ₁₃     σ₁₄     σ₁₅     σ₁₆  ]
e_ring  [  ·      L₂²     σ₂₃     σ₂₄     σ₂₅     σ₂₆  ]
ν_tube  [  ·       ·      L₃²     s_ν     σ₃₅     σ₃₆  ]
ν_ring  [  ·       ·       ·      L₄²     σ₄₅     σ₄₆  ]
p_tube  [  ·       ·       ·       ·      L₅²     s_p   ]
p_ring  [  ·       ·       ·       ·       ·      L₆²   ]
```

Lower-left is symmetric (G_ij = G_ji).  The dots represent the
mirror of the upper-right entries.

| Category | Count | Entries |
|----------|-------|---------|
| Diagonal (circumferences) | 6 | L₁²…L₆² |
| Within-sheet shears | 3 | s_e, s_ν, s_p |
| e↔ν cross entries | 4 | σ₁₃, σ₁₄, σ₂₃, σ₂₄ |
| e↔p cross entries | 4 | σ₁₅, σ₁₆, σ₂₅, σ₂₆ |
| ν↔p cross entries | 4 | σ₃₅, σ₃₆, σ₄₅, σ₄₆ |
| **Total independent** | **21** | |


## Philosophy

R54 treats the 6 compact dimensions as **one T⁶** (per Q116),
not three independent sheets.  The "sheet" labels are approximate
— useful for classifying single-sheet modes but inadequate for
compound particles.  The eigenmodes of the full metric are the
physical particles.  Cross-shears are not corrections; they are
part of the fundamental geometry.
