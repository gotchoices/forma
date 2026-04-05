# Q102. Is neutrino neutrality a consequence of sheet size?

**Status:** Open — framing + candidate threshold calculation
**Related:**
  [Q78](Q78-neutrino-sheet-access.md) (neutrino sheet access),
  [Q99](Q99-fourth-neutrino-mode.md) (fourth neutrino mode),
  [`grid/foundations.md`](../grid/foundations.md) (axioms A3, A5, A6),
  [`grid/maxwell.md`](../grid/maxwell.md) (charge quantization),
  [`grid/sim-impedance/`](../grid/sim-impedance/) (defect cost analysis),
  [`primers/alpha-in-grid.md`](../primers/alpha-in-grid.md) (α as impedance mismatch)

---

## 1. The question

In MaSt, all three particle sheets (Ma_p, Ma_e, Ma_ν) are
2D triangular lattices wrapped into tori.  Standing waves on
these tori are particles.  On the proton and electron sheets,
the standing wave's phase winds through 2π around the tube,
producing a topological defect that the ambient 3D lattice
detects as electric charge.

Why doesn't the same thing happen on the neutrino sheet?

The neutrino has mass (it carries a standing wave), but no
charge.  In the Standard Model, neutrino neutrality is
postulated — it's built into the gauge group assignments.
Can GRID + MaSt do better and derive it from the lattice
structure?

## 2. The hypothesis

**Neutrino neutrality is a consequence of sheet size.**

The three sheets differ vastly in circumference:

| Sheet | Circumference | Compton energy mc² |
|-------|--------------|-------------------|
| Ma_p (proton) | ~10¹⁹ L | 938 MeV |
| Ma_e (electron) | ~10²² L | 0.511 MeV |
| Ma_ν (neutrino) | ~10²⁹ L | ~0.03 eV |

On all three sheets, the phase CAN wind through 2π around
the tube.  But on the neutrino sheet, that winding is spread
over ~10²⁹ cells — a phase step of ~10⁻²⁸ radians per cell.
If this gradient is below the lattice's resolution limit, the
ambient 3D lattice cannot detect the winding.  No detectable
winding → no topological defect → no charge.

The standing wave still circulates (the neutrino has mass).
But the phase twist is too gentle for the ambient lattice to
"see."  The neutrino's neutrality would be a resolution
failure — the lattice's finite information density ζ = 1/4
imposes a minimum detectable phase gradient, and the neutrino
sheet falls below it.

## 3. Why this matters

If correct, this would:

- **Derive neutrino neutrality** from α, ζ, and sheet sizes
  rather than postulating it
- **Predict a charge threshold** — a critical sheet
  circumference N_crit above which no particle can carry
  charge
- **Unify charge and mass** — both are properties of the
  same standing wave; whether you get charge depends on
  whether the lattice can resolve the associated phase
  gradient
- **Constrain neutrino masses** — the threshold would set a
  maximum mass for neutral particles, or equivalently a
  minimum mass for charged ones

## 4. The threshold calculation

### What we know

All ingredients are dimensionless and known:

- α ≈ 1/137.036 (coupling strength)
- ζ = 1/4 (information resolution)
- κ = 1/(4πα) ≈ 1722 (action coupling constant)
- Phase winding: 2π per tube circumference
- Phase step per cell: δθ = 2π / N (where N = circumference
  in Planck lengths)
- Sheet sizes: N_p ≈ 10¹⁹, N_e ≈ 10²², N_ν ≈ 10²⁹

### The problem: defining "resolvable"

The threshold depends on what "the lattice can't see the
winding" means precisely.  Three candidate criteria have been
considered, each using different physics:

**Criterion A: Phase gradient resolution.**

The lattice resolves ζ = 1/4 bit per cell.  This should
correspond to a minimum distinguishable phase step δθ_min.
The threshold is N_crit = 2π / δθ_min.

Problem: converting ζ (an entropy bound in bits) to δθ_min
(a phase resolution in radians) requires a model of how
information is encoded in the phase — specifically, how the
junction between the 2D sheet and the 3D lattice transmits
phase information.  The sim-impedance study (Track 1) showed
that a mechanical/geometric model of this junction gives the
wrong scale (~1/20 instead of ~1/137), and that the coupling
is thermodynamic rather than geometric.  The conversion from
ζ to δθ_min is not yet established.

**Criterion B: Vortex energy from the action.**

The lattice action has coupling κ = 1/(4πα).  A vortex
(2π phase winding) on the sheet has an energy cost
proportional to κ.  On a discrete lattice of N cells, the
vortex energy is approximately:

> E_vortex ~ κ × (2π)² / N = 4π² κ / N = π/(αN)

(This is the harmonic energy ½κ(δθ)² summed over N cells,
each contributing (2π/N)².)

For the vortex to be sustainable, this energy must be
available from the standing wave.  The standing wave energy
is mc² = 2π/N (in natural units where the lowest mode has
wavelength = circumference).  The condition E_vortex ≤ mc²
gives:

> π/(αN) ≤ 2π/N

which simplifies to:

> 1/(2α) ≤ 1

This is satisfied for α ≥ 1/2, which is NOT satisfied for
α ≈ 1/137.  This suggests the vortex is always too expensive
for the standing wave to sustain — which would mean NO
particles are charged, contradicting observation.

This means the simple harmonic estimate is wrong, or the
vortex energy is not paid by the standing wave alone but by
the lattice vacuum.  The vortex may be topologically stable
once formed (the winding number can't change continuously),
with its energy stored in the ambient lattice's Coulomb
field (αmc²) rather than deducted from the wave energy mc².

**Criterion C: Coupling energy per cell at the junction.**

The energy that couples into the ambient lattice is αmc²
total.  Spread over ~N cells at the junction (the torus
surface), the coupled energy per cell is αmc²/N.  If this
drops below the lattice's minimum registrable energy per
cell (set by ζ), the coupling fails.

In natural units, mc² ≈ 1/N for the lowest mode, so:

> Coupled energy per cell ≈ α/N²

For the electron: α/(10²²)² ≈ 10⁻⁴⁸
For the neutrino: α/(10²⁹)² ≈ 10⁻⁶² 

Both are absurdly small in Planck units.  Unless the
minimum registrable energy per cell is similarly tiny
(which is plausible — the lattice routinely carries
sub-Planck-energy fields), this criterion doesn't cleanly
separate charged from neutral.

### Assessment

None of the three criteria produces a clean threshold that
falls between the electron and neutrino sheet sizes.  The
calculation is not blocked by free variables — all the
numbers are known.  It is blocked by the **junction model**:
we need to understand how phase information on the 2D sheet
couples through to the 3D lattice at the point of contact.

The sim-impedance study established that this coupling is
thermodynamic (an energy partition) rather than geometric
(a coincidence rate).  The defect cost picture (α as the
fraction of energy that leaks into the Coulomb field) works
for explaining what α IS, but doesn't obviously provide a
threshold below which the leakage stops entirely.

## 5. Possible paths forward

**Path A: Topological stability analysis.**  A vortex on
a lattice has a core and a far field.  The core has a
minimum size (a few lattice spacings).  If the torus tube
circumference is smaller than the vortex core, the winding
can't form — there isn't room for the phase to ramp from
0 to 2π smoothly.  This would give a MINIMUM circumference
for charge, not a maximum.  That's backwards for the
neutrino (which has the largest sheet), but it could
constrain other aspects of the model.

**Path B: Mode analysis on the torus.**  The standing wave
modes on a torus have quantized frequencies.  The charged
modes (those with net winding) may have different energy
spectra than the neutral modes (those without).  If the
lowest charged mode on the neutrino sheet has energy above
the neutrino mass scale, charged neutrinos can't exist as
stable particles — the charged mode would be too heavy to
be the ground state.

**Path C: Junction bandwidth.**  The junction between the
2D sheet and the 3D lattice may have a finite bandwidth —
a maximum spatial frequency it can transmit.  A winding
spread over 10²⁹ cells has spatial frequency 1/10²⁹ in
Planck units.  If the junction acts as a high-pass filter
(only coupling gradients above some cutoff), then very
gentle windings would not couple through.  This is
essentially Criterion A above, but framed as a filter
property of the junction rather than a resolution limit
of the bulk lattice.

**Path D: Different lattice structure on Ma_ν.**  The
three sheets may not have identical lattice types.  If
Ma_ν has a different cell geometry (e.g., hexagonal instead
of triangular, or a different edge-length-to-circumference
ratio), the phase topology may differ in a way that
prevents winding.  This is less elegant (it requires
postulating a structural difference) but worth noting.

## 6. Connection to existing work

- **Charge quantization** (maxwell.md): established that
  charge = integer winding number × e.  Does not address
  when winding is possible vs impossible.

- **Defect cost** (sim-impedance/README.md): established
  α as the energy fraction leaking through the junction.
  Does not provide a threshold.

- **Compact dimensions** (grid/compact-dimensions.md):
  showed that the triangular lattice wrapping discretizes
  α but doesn't select its value.  Does not address
  whether the wrapping supports or prevents winding on
  different sheets.

- **Ghost modes / dark matter** (Q94, R42): the ~860
  Ma eigenstates without EM coupling are neutral by
  geometric symmetry, not by a resolution threshold.
  This is a different mechanism from what Q100 proposes
  for neutrinos.

## 7. Experimental status: is neutrino charge exactly zero?

Science has not measured neutrino charge to be exactly zero.
It has placed an upper bound that is very small:

| Method | Bound on |q_ν| | Source |
|--------|---------|--------|
| Charge neutrality of matter | < ~10⁻²¹ e | If q_ν ≠ 0, neutron decay (n → p + e⁻ + ν̄) violates charge conservation unless q_p − q_e − q_ν = 0 exactly.  Tested to ~10⁻²¹ e. |
| Stellar cooling | < ~10⁻¹⁵ e | A charged neutrino would couple to stellar magnetic fields, altering energy loss rates.  Stellar models constrain this. |
| Laboratory (reactor) | < ~10⁻¹² e | Direct scattering measurements. |

The Standard Model predicts exactly zero from gauge group
assignments and anomaly cancellation.  But this is a
structural assumption, not a derived result — physics beyond
the Standard Model could allow tiny nonzero charge.

### What the two MaSt mechanisms predict

The two candidate explanations for neutrino neutrality make
different predictions about whether the charge is exactly
zero or merely extremely small:

**Mechanism (a): Sheet too large (resolution threshold).**
The phase gradient is below the lattice's ability to detect.
The winding exists mathematically but is physically
invisible.  Prediction: **charge is exactly zero**.  The
coupling doesn't happen at all — there is no residual.

**Mechanism (b): Zero or near-zero shear.**  No circulation
symmetry breaking, so no net traveling wave, so no charge.
But if the shear is extremely small rather than exactly zero,
there would be a tiny net circulation and a correspondingly
tiny charge.  Prediction: **charge could be nonzero at an
extremely small level**, proportional to the shear.  For a
shear of ~10⁻²⁰ (compared to ~0.01 for the electron sheet),
the charge might be ~10⁻²⁰ e — consistent with experimental
bounds.

This is a testable distinction in principle:
- If neutrino charge is measured at any nonzero level
  (even ~10⁻²¹ e), mechanism (a) is excluded and
  mechanism (b) is favored.
- If neutrino charge is pushed below ~10⁻²⁵ e (far below
  current sensitivity), mechanism (b) with naturally small
  shear becomes strained, favoring mechanism (a).

Current experiments cannot distinguish "exactly zero" from
"10⁻²¹ e."  But the two mechanisms make structurally
different predictions — one gives a hard zero, the other
gives a soft zero — and future precision measurements could
in principle separate them.

A nonzero neutrino charge would also imply nonzero shear
on Ma_ν, which would produce matter/antimatter asymmetry
in neutrino production — a form of CP violation.  Current
hints of CP violation in neutrino oscillation (δ_CP ≈ −π/2
from T2K, 2–3σ) could be related, though the connection
between oscillation CP violation and sheet shear has not
been derived.


## 8. Summary

Neutrino neutrality MAY follow from the combination of
large sheet size and finite lattice resolution, but a clean
derivation requires a junction model that doesn't yet exist.
The hypothesis is physically motivated (large N → gentle
phase gradient → undetectable winding) and uses only known
ingredients (α, ζ, sheet sizes).  The main obstacle is
defining "resolvable" in a way that produces a threshold
between the electron and neutrino scales.

This question is worth returning to when the junction
physics (how 2D sheet states couple to 3D ambient lattice
states) is better understood.  A successful threshold
calculation would derive neutrino neutrality from first
principles and predict a maximum neutral-particle mass.
