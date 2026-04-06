# R51: Is the hydrogen atom a cross-sheet mode?

**Status:** Framing
**Questions:** [Q105](../../qa/Q105-atoms-as-cross-sheet-modes.md)
  (atoms as cross-sheet modes)
**Type:** compute
**Depends on:** R50 (model-D engine and parameters),
  R31 Track 1 (prior negative result, model-C)

---

## Motivation

R31 Track 1 concluded that "the hydrogen atom is NOT a Ma
mode" — no eigenmode near the hydrogen mass (938.783 MeV)
could be found with model-C parameters.  The finest Ma
energy step was ~38 keV, far coarser than the 13.6 eV
binding energy.

Q105 challenges this conclusion on two grounds:

1. **R31 searched for the wrong thing.** It looked for a
   mode AT the hydrogen total mass.  Q105 proposes that the
   binding energy is the DIFFERENCE between the coupled
   cross-sheet eigenvalue and the uncoupled sum — a
   perturbative splitting, not a new mode at a specific mass.

2. **Model-C parameters may not be representative.**
   Model-D has different geometry (proton as (3,6), different
   ε values, σ_ep = −0.13 vs −0.091).  The Schur complement
   mechanism (R50 Track 2 F14) produces energy shifts that
   are quadratic in σ and mode-dependent.  The eigenvalue
   landscape under model-D may have structure at scales that
   model-C could not resolve.

This study asks the question directly: at model-D
parameters, does the coupled cross-sheet eigenvalue of a
hydrogen-like mode differ from the uncoupled sum by ~13.6 eV?

## What we're computing

**NOT:** a search for a mode at 938.783 MeV (that's what
R31 did — wrong question).

**Instead:** the energy difference between:

- **Uncoupled:** E(electron alone) + E(proton alone)
  = E(1,2,0,0,0,0) + E(0,0,0,0,3,6)
  = 0.511 + 938.272 = 938.783 MeV

- **Coupled:** E(1,2,0,0,3,6) at nonzero σ_ep
  = the cross-sheet eigenvalue of a mode with electron
  AND proton windings simultaneously

The difference ΔE = E(coupled) − E(uncoupled sum) is what
we compare to the hydrogen binding energy (−13.6 eV).

If ΔE is negative and ~13.6 eV in magnitude, the atom IS
a cross-sheet mode whose binding energy comes from the
metric coupling.  If ΔE is positive, zero, or the wrong
magnitude (keV or MeV scale), the two-tier picture stands.

## Why this might work (where R31 failed)

### The Schur complement produces mode-dependent shifts

R50 Track 2 F14 established that σ_ep modifies the
effective metric through the Schur complement.  Different
modes shift by different amounts.  The neutron shifts by
~1.3 MeV relative to the proton (producing the mass
difference) — a ~0.14% relative shift on a ~938 MeV base.

The hydrogen binding energy is a ~0.0000014% shift on
the same base.  This is ~100× smaller than the neutron
shift.  Can the Schur complement produce a shift that
small?

The Schur complement correction is O(σ²) and
mode-dependent (F14 points 2, 4).  Different (n₁, n₂)
combinations couple differently to (n₅, n₆) through the
off-diagonal metric blocks.  The hydrogen mode
(1,2,0,0,3,6) has a specific coupling geometry that may
differ from the neutron mode (0,6,*,*,0,8) by exactly
the right factor to produce a 13.6 eV shift instead of
a 1.3 MeV shift.

### Different mode = different shift

The key insight: the hydrogen candidate has TUBE winding
on Ma_e (n₁ = 1), while the neutron candidate has only
RING winding (n₁ = 0, n₂ = 6).  Tube and ring windings
couple through different components of the metric's
off-diagonal block.  The tube-tube coupling (n₁ × n₅)
and tube-ring coupling (n₁ × n₆) have different
magnitudes, set by the aspect ratios and shears.

It is entirely possible that the specific combination
n₁ = 1 (electron tube) coupled to n₅ = 3, n₆ = 6
(proton composite) produces a much smaller shift than
n₂ = 6 (electron ring) coupled to n₆ = 8 (proton ring)
— because the tube-tube and tube-ring cross-terms in the
metric are different from the ring-ring cross-terms.

### Numerical precision is achievable

13.6 eV on a 938,783,000 eV base requires relative
precision of ~1.4 × 10⁻⁸.  Python's float64 has ~15
digits of precision.  The eigenvalue calculation
(E² = nᵢ G̃ⁱʲ nⱼ × scale²) is exact for a given metric
— no iterative approximation, no truncation.  The
precision limit is set by the input parameters (ε, s, σ),
which are specified to float64 precision.

So 10⁻⁸ relative precision is well within reach.  The
question is whether the physics produces a shift at this
scale, not whether we can detect it numerically.


## Tracks

### Track 1: Direct eigenvalue comparison

**Status:** Planned

**Goal:** Compute E(coupled) − E(uncoupled sum) for the
hydrogen candidate mode at model-D parameters.

**Method:**

1. Construct the model-D metric at default parameters
   (ε_e = 0.65, ε_p = 0.55, σ_ep = −0.13, others from
   R50 Track 1 F2/F9).

2. Compute E_uncoupled = E(1,2,0,0,0,0) + E(0,0,0,0,3,6).
   These are the reference masses — exact by construction.

3. Compute E_coupled = E(1,2,0,0,3,6) at the same
   parameters.  This is the cross-sheet eigenvalue.

4. Report ΔE = E_coupled − E_uncoupled in eV.

5. Compare ΔE to −13.6 eV (hydrogen ground state binding
   energy).

**Sweep:** Repeat for σ_ep from 0 to −0.3 in fine steps.
At σ_ep = 0, ΔE should be exactly 0 (no coupling → no
binding).  Track how ΔE varies with σ_ep.

**Extended candidates:** Also compute ΔE for:

| System | Mode candidate | Binding energy |
|--------|---------------|---------------|
| Hydrogen | (1,2,0,0,3,6) | −13.6 eV |
| Helium (Z=2) | (2,4,0,0,*,*) + nuclear | −79.0 eV |
| Deuterium (n+p) | (0,n₂,n₃,n₄,0,n₆) | −2.224 MeV |

The deuterium case is a cross-check: R50 Track 2 already
found modes near the neutron mass with ~MeV shifts.  The
deuteron should be a similar-scale cross-sheet mode.

**Success criteria:**
- If ΔE ≈ −13.6 eV for hydrogen: Q105 is strongly
  supported.  The atom IS a cross-sheet mode.
- If ΔE ≈ 0 or ΔE ≫ 13.6 eV: the two-tier picture
  stands.  Binding energy comes from 3D Coulomb, not
  from the Ma metric.
- If ΔE is negative but the wrong magnitude (e.g.,
  −1 keV or −1 MeV): partial support — the metric
  produces binding, but at the wrong scale.  Interesting
  but not a match.


### Track 2: Mode anatomy — which metric components matter

**Status:** Planned

**Goal:** Decompose the cross-sheet eigenvalue shift into
contributions from specific metric components.  Identify
which off-diagonal terms drive the binding and whether the
eV scale emerges naturally or requires fine-tuning.

**Method:**

1. At the σ_ep value where Track 1 finds ΔE closest to
   −13.6 eV (if any), decompose the metric G̃ into:
   - Diagonal blocks (single-sheet contributions)
   - Off-diagonal blocks (cross-sheet coupling)
   - Schur complement correction to each block

2. Compute the eigenvalue shift contribution from each
   term separately.

3. Identify: is the eV-scale shift a cancellation between
   large terms (fine-tuned) or a naturally small term
   (robust)?  If it's a cancellation of MeV-scale terms
   to get eV, the result is fragile and probably wrong.
   If it's a naturally small coupling term, it's robust.


### Track 3: Helium and the Z-scaling test

**Status:** Planned

**Goal:** If Track 1 finds a hydrogen binding energy, test
whether the scaling with Z matches known atomic physics.

**Method:**

1. Compute ΔE for helium: mode (2,4,0,0,*,*) coupled to
   the He-4 nuclear mode.  Target: −79.0 eV (total
   ionization energy of helium).

2. Compute ΔE for lithium: mode (3,6,0,0,*,*) coupled to
   the Li-7 nuclear mode.  Target: −203.5 eV.

3. Check whether ΔE(Z) scales as ~Z^(7/3) (Thomas-Fermi
   scaling for heavy atoms) or linearly in Z, or something
   else.

**Success criteria:**
- Correct Z-scaling would be strong evidence that the
  cross-sheet coupling captures atomic binding.
- Wrong scaling (e.g., linear when it should be Z^(7/3))
  would suggest the metric produces binding at the wrong
  rate — possibly requiring additional physics (the 3D
  Coulomb picture from Paper 3).


### Track 4: Harmonic mass scaling check

**Status:** Planned

**Goal:** Verify that E(Z, 2Z) = Z × E(1, 2) on the
electron sheet (linear harmonic scaling), and determine
whether the binding energy breaks this linearity in the
right way.

**Method:**

1. Compute E(Z, 2Z, 0, 0, 0, 0) for Z = 1 to 30 on
   the uncoupled electron sheet.  Verify linearity.

2. Compute E(Z, 2Z, 0, 0, n₅, n₆) for the same Z
   values, coupled to the appropriate nuclear modes.

3. The difference E(coupled) − Z × m_e should be the
   binding energy at each Z.  Plot against the measured
   total ionization energies.

**The test:** if the harmonic mass IS linear (step 1) but
the coupled eigenvalue deviates from linearity (step 2) in
a way that matches measured binding energies (step 3), then
the binding energy is genuinely coming from the cross-sheet
coupling and not from the electron-sheet geometry alone.


---

## Design notes

### Precision requirements

| Quantity | Scale | Relative precision needed |
|----------|-------|-------------------------|
| Proton mass | 938,272,000 eV | 10⁻⁸ for 13.6 eV |
| Electron mass | 511,000 eV | 10⁻⁵ for 13.6 eV |
| Binding energy | 13.6 eV | absolute |
| Mode energies | MeV | 10⁻⁸ relative |
| Python float64 | — | 10⁻¹⁵ | ample |

The computation is well within numerical precision.  The
question is physics, not numerics.

### What we expect

Honest expectations before running:

- **Most likely:** ΔE is zero to float64 precision (the
  cross-sheet coupling is too weak at the eV scale, the
  Schur complement correction doesn't reach down to 10⁻⁸
  relative shifts).  This would confirm R31 and the
  two-tier picture.

- **Interesting:** ΔE is nonzero but the wrong magnitude
  (keV or MeV).  This would mean the cross-sheet coupling
  produces binding, but at the nuclear scale, not the
  atomic scale.  Consistent with the neutron being a
  cross-sheet mode but atoms being spatial.

- **Remarkable:** ΔE ≈ −13.6 eV.  This would overturn
  the two-tier picture and validate Q105.  Given that no
  one has proposed this test before (R31 asked the wrong
  question), this is genuinely unknown territory.

We do not bias toward any outcome.  We compute and report.


---

## Files

| File | Contents |
|------|----------|
| [findings.md](findings.md) | Results and interpretation |
