# R51: Atoms as compound tori modes

**Status:** Framing
**Questions:** [Q105](../../qa/Q105-atoms-as-cross-sheet-modes.md)
  (atoms as cross-sheet modes)
**Type:** compute
**Depends on:** R50 (model-D engine and parameters),
  R31 Track 1 (prior negative result, model-C)

---

## Premise

This study takes the position that **electrons in atoms are
not spatially related to nuclei.**  There are no orbitals, no
Bohr radii, no 3D Coulomb potential.  Instead:

- **Atoms are compound eigenmodes** of the three coupled tori
  (Ma_e, Ma_ν, Ma_p).  A "hydrogen atom" is a single eigenmode
  whose quantum numbers span both the electron sheet and the
  proton sheet.

- **"Adding an electron"** means adding a quantum of energy to
  the electron sheet — incrementing (n₁, n₂) on Ma_e while
  keeping the proton-sheet quantum numbers fixed.

- **Shell filling** is mode saturation: when the electron sheet
  absorbs enough quanta, adding one more pushes accumulated
  energy into a dark mode (e.g. on Ma_ν), producing the
  screening effect observed as closed shells.

- **Nuclei grow** by adding energy to proton-sheet modes in
  quantum amounts (the R29 scaling law: n₅ = A, n₆ = 2A or
  3A depending on proton hypothesis).

We make no appeal to the Bohr model, the Standard Model, or
any 3D spatial electron-nucleus picture.  The goal is to find
**any** set of assumptions under which atoms and elements can
be modeled entirely as compound tori modes.  We start with
hydrogen.


## Why revisit this

R31 Track 1 concluded that "the hydrogen atom is NOT a Ma
mode" — the finest Ma energy step was ~38 keV, far coarser
than the 13.6 eV ionization energy.

But R31 may have been premature:

1. **R31 asked the wrong question.** It searched for a mode
   AT the hydrogen total mass (m_e + m_p = 938.783 MeV).
   In the compound-mode picture, the hydrogen mass is NOT
   m_e + m_p — it is the eigenvalue E(1,2,0,0,n₅,n₆) of
   the coupled metric, which differs from m_e + m_p by
   the binding structure.

2. **R31 used model-C parameters.** Model-D has different
   geometry (dual proton hypotheses, different ε values,
   different σ_ep).  The Schur complement mechanism (R50
   Track 2 F14) produces mode-dependent energy shifts.
   The eigenvalue landscape under model-D may differ from
   model-C at scales R31 could not resolve.


## The energy of "adding an electron"

### Zero-coupling baseline

The compound hydrogen mode is (1,2,0,0,n₅,n₆) — the
electron mode (1,2) combined with the proton mode (n₅,n₆)
into a single 6-tuple.

At σ_ep = 0 (no cross-sheet coupling), the metric is
block-diagonal.  The eigenvalue satisfies:

<!-- E²(compound) = E²(electron) + E²(proton) = m_e² + m_p² -->
$$
E^2(1,2,0,0,n_5,n_6)\big|_{\sigma=0}
\;=\; E^2(1,2,0,0,0,0) + E^2(0,0,0,0,n_5,n_6)
\;=\; m_e^2 + m_p^2
$$

Because the eigenvalue equation is a quadratic form (E² not
E), the energies add **in quadrature**, not linearly.  This
gives:

<!-- E(compound) = √(m_e² + m_p²) ≈ m_p + m_e²/(2m_p) ≈ m_p + 139 eV -->
$$
E = \sqrt{m_e^2 + m_p^2}
\;\approx\; m_p + \frac{m_e^2}{2\,m_p}
\;\approx\; m_p + 139\;\text{eV}
$$

So the energy cost of "adding one electron quantum" to a
bare proton at zero coupling is:

<!-- ΔE_add = √(m_e² + m_p²) − m_p ≈ m_e²/(2m_p) ≈ 139 eV -->
$$
\Delta E_{\text{add}}\big|_{\sigma=0}
\;=\; \sqrt{m_e^2 + m_p^2} - m_p
\;\approx\; \frac{m_e^2}{2\,m_p}
\;\approx\; 139\;\text{eV}
$$

**This is only ~10× the hydrogen ionization energy (13.6 eV).**
R31 found the spectrum was 2,830× too coarse — but that was
because it compared to m_e (511 keV), not to the quadrature
cost m_e²/(2m_p) (139 eV).  The reframing dramatically
narrows the gap.

### With cross-sheet coupling

At σ_ep ≠ 0, off-diagonal metric terms mix the electron and
proton sectors.  Both the compound mode and the bare proton
shift:

- E(1,2,0,0,n₅,n₆; σ) shifts due to electron-proton coupling
- E(0,0,0,0,n₅,n₆; σ) also shifts (Schur complement modifies
  the proton block even for pure proton modes)

The energy cost of adding an electron becomes:

ΔE_add(σ) = E(1,2,0,0,n₅,n₆; σ) − E(0,0,0,0,n₅,n₆; σ)

At σ = 0: ΔE_add = 139 eV (baseline).
Target: ΔE_add = 13.6 eV at the physically correct σ_ep.

If σ_ep can reduce the addition cost from 139 eV to 13.6 eV,
the compound tori model reproduces the hydrogen ionization
energy with no spatial physics.

### Alternative comparison: ionization as separation

There is a second way to define ionization energy.  If a
"free electron" (not bound to any nucleus) has energy m_e,
and a "free proton" has energy m_p, then the ionization
energy is the cost to separate the compound into free parts:

I.E. = (m_e + m_p) − E(compound)

At σ = 0: I.E. = (m_e + m_p) − √(m_e² + m_p²)
  ≈ m_e − m_e²/(2m_p) ≈ 511 keV

This is much larger — essentially m_e.  It says the compound
mode is ~511 keV lighter than the separated particles, purely
from the quadrature combination.  This "tori binding" is
kinematic, not from any coupling.

With σ ≠ 0, the compound mode energy shifts, and I.E.
changes.  If σ_ep pushes the compound energy upward (toward
m_e + m_p), the ionization energy decreases.  If it can push
it to within 13.6 eV of m_e + m_p, we match hydrogen.

**Both definitions must be computed.**  They ask different
questions: ΔE_add asks what the proton "sees" when an
electron quantum is added; I.E. asks the total energy
balance of separation.


## What we're computing

For each proton hypothesis ((1,3) and (3,6)) and each
σ_ep value:

1. **Bare proton energy:** E_p(σ) = E(0,0,0,0,n₅,n₆; σ)
2. **Free electron energy:** E_e(σ) = E(1,2,0,0,0,0; σ)
3. **Compound hydrogen energy:** E_H(σ) = E(1,2,0,0,n₅,n₆; σ)

Derived quantities:
- ΔE_add(σ) = E_H(σ) − E_p(σ)  (cost of adding electron)
- I.E.(σ) = E_e(σ) + E_p(σ) − E_H(σ)  (separation energy)
- Both reported in eV with full float64 precision


## Tracks

### Track 1: Energy cost of adding an electron to a proton

**Status:** Complete

**Goal:** Map ΔE_add(σ) and I.E.(σ) as functions of σ_ep
for both proton hypotheses.  Determine whether either
quantity can match 13.6 eV.

**Method:**

1. Construct the model-D metric at default parameters
   (ε_e = 0.65, ε_p = 0.55, others from R50).

2. For each proton hypothesis (n_p = (1,3) and (3,6)):
   a. Sweep σ_ep from 0 to −0.3 in fine steps (≥ 100 points)
   b. At each σ, compute E_p, E_e, E_H
   c. Report ΔE_add and I.E. in eV

3. At σ = 0, verify:
   - ΔE_add = m_e²/(2m_p) ≈ 139.1 eV  (quadrature baseline)
   - I.E. = m_e − m_e²/(2m_p) ≈ 510,861 eV  (full separation)

4. Identify: does either curve cross 13.6 eV?  If so, at
   what σ_ep?  Is that σ_ep consistent with R50 particle
   fitting (σ_ep ≈ −0.28)?

**Success criteria:**
- ΔE_add(σ) = 13.6 eV at some σ_ep: the "addition cost"
  interpretation works.  Strong if σ_ep matches R50.
- I.E.(σ) = 13.6 eV at some σ_ep: the "separation cost"
  interpretation works.  Strong if σ_ep matches R50.
- Both give ~13.6 eV at the SAME σ: remarkable — the model
  is internally consistent.
- Neither reaches 13.6 eV: the tori model cannot reproduce
  hydrogen binding.  Record the closest approach and the
  scale of ΔE_add at R50 σ values.


### Track 2: Adding a second electron — helium

**Status:** Planned (contingent on Track 1)

**Goal:** Model helium as a compound mode by adding a second
electron quantum to a Z=2 nucleus.

**Method:**

1. The ⁴He nucleus (Z=2, N=2, A=4) in the (1,3) proton
   hypothesis: nuclear mode (N, *, *, *, A, 3A) = (2, *, *, *, 4, 12)
   The electron-sheet n₁ = N = 2 comes from neutron content.

2. Neutral ⁴He: add Z=2 electron quanta.  The electron
   contribution is (Z, 2Z) = (2, 4) on Ma_e.  Combined with
   nuclear n₁ = N = 2: total n₁ = N + Z = 4, n₂ = n₂_nuc + 4.

3. Compute:
   - E(nucleus alone) at given σ_ep
   - E(nucleus + 1 electron) — singly ionized He⁺
   - E(nucleus + 2 electrons) — neutral He
   - First ionization: E(He) − E(He⁺)
   - Second ionization: E(He⁺) − E(He²⁺)

4. Compare to measured ionization energies:
   - He first: 24.587 eV
   - He second: 54.418 eV

**The test:** does adding successive electron quanta cost
different amounts?  In the tori model at zero coupling,
adding the Z-th electron costs (2Z−1) × m_e²/(2m_p),
which scales linearly in Z.  Real ionization energies do
NOT scale linearly — they have shell structure.  If σ_ep
introduces non-linearity that matches observed ionization
energies, the compound mode picture gains support.


### Track 3: Z-scaling across the periodic table

**Status:** Planned (contingent on Track 2)

**Goal:** Compute the energy cost of adding electrons for
Z = 1 through 30 and compare to measured total ionization
energies.  Look for shell structure.

**Method:**

1. For each element Z:
   - Construct the nuclear mode from R29 scaling
   - Add Z electron quanta sequentially
   - Compute each successive ionization energy

2. Plot ΔE_add(Z) against measured first ionization
   energies.  Look for:
   - Periodic structure (noble gas peaks)
   - Correct ordering of shells (2, 8, 18, ...)
   - Approximate magnitude match

3. Does the tori model produce ANY periodic structure
   from pure metric coupling, without 3D orbitals?


### Track 4: Shell saturation — dark mode overflow

**Status:** Planned (contingent on Track 3)

**Goal:** Investigate whether there is a maximum electron
quantum number before energy "overflows" into a dark mode.

**Premise:** Shell filling in the tori model means that
at some critical Z, adding another electron quantum to
Ma_e becomes energetically unfavorable — the energy would
prefer to couple into Ma_ν (neutrino sheet) via σ_eν.
This would manifest as a dark (neutral, undetectable)
excitation, producing the screening effect observed as
closed shells.

**Method:**

1. For a given nuclear mode, compute ΔE_add(Z) as Z
   increases from 1 to Z_max.

2. At each Z, also compute the energy of the ALTERNATIVE:
   coupling the extra quantum into Ma_ν instead of Ma_e.

3. If at some Z_crit, the Ma_ν coupling becomes lower
   energy than the Ma_e addition, that Z_crit defines
   a shell closure.

4. Does Z_crit match 2 (helium), 10 (neon), 18 (argon)?


### Track 5: Mode anatomy — what drives the binding

**Status:** Planned

**Goal:** Decompose the cross-sheet eigenvalue shift into
contributions from specific metric components.  Identify
whether the eV-scale physics emerges naturally or requires
fine-tuning.

**Method:**

1. At the σ_ep value closest to matching 13.6 eV (from
   Track 1), decompose the metric G̃ into:
   - Diagonal blocks (single-sheet contributions)
   - Off-diagonal blocks (cross-sheet coupling)
   - Schur complement correction to each block

2. Compute the eigenvalue shift contribution from each
   term separately.

3. Identify: is the eV-scale shift a cancellation between
   large terms (fine-tuned) or a naturally small term
   (robust)?


---

## Design notes

### Precision requirements

| Quantity | Scale | Relative precision needed |
|----------|-------|--------------------------|
| Proton mass | 938,272,000 eV | 10⁻⁸ for 13.6 eV |
| Electron mass | 511,000 eV | 10⁻⁵ for 13.6 eV |
| Zero-coupling ΔE_add | ~139 eV | 10⁻¹ for 13.6 eV |
| Target binding | 13.6 eV | absolute |
| Python float64 | — | 10⁻¹⁵ | ample |

The computation is well within numerical precision.  The
question is physics, not numerics.

### Why this might work

The zero-coupling energy cost of adding an electron
(m_e²/(2m_p) ≈ 139 eV) is already within an order of
magnitude of the ionization energy (13.6 eV).  We need
σ_ep to reduce it by a factor of ~10.  For comparison:

- The neutron mass shift from σ_ep is ~1.3 MeV (~0.14%
  of m_p) — a large effect.
- We need a ~125 eV shift on a ~139 eV quantity — a large
  fractional effect, but tiny in absolute terms (10⁻⁷ of m_p).
- The hydrogen mode (n₁=1, n₂=2) has very small electron
  quantum numbers, so it couples weakly to the proton sheet.
  Whether this weak coupling produces a shift at exactly
  the right scale is the open question.

### Proton hypothesis dependence

Both (1,3) and (3,6) proton modes are tested.  They produce
different L_ring_p values, different mode spacings, and
different coupling geometries.  The zero-coupling ΔE_add is
the same for both (~139 eV, since it depends only on m_e and
m_p), but the σ-dependence will differ.


---

## Files

| File | Contents |
|------|----------|
| [findings.md](findings.md) | Results and interpretation |
