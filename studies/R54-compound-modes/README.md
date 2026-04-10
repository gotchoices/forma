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

### Track 4: α from the full metric

Identify which metric component produces α = 1/137.  Candidates:
- A Ma-S cross term (g(e-tube, S-x))
- A specific combination of the 6×6 entries
- A derived quantity from the modular parameter τ = s + iε


## Philosophy

R54 treats the 6 compact dimensions as **one T⁶** (per Q116),
not three independent sheets.  The "sheet" labels are approximate
— useful for classifying single-sheet modes but inadequate for
compound particles.  The eigenmodes of the full metric are the
physical particles.  Cross-shears are not corrections; they are
part of the fundamental geometry.
