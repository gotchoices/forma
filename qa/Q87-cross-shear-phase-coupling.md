# Q87. Can cross-shear couple energy between material sheets and modify mode phase?

**Status:** open — conceptual; no computation yet
**Source:** user question (atoms-from-geometry review session)
**Connects to:** R26 F66–F74 (cross-shear landscape), R27 F14
(σ_eν and σ_νp shift neutron mass), R28 F1 (neutrino cross-shears
irrelevant at MeV scale), R36 F8 (inter-sheet shear vs tilt),
R29 F22 (electron-sheet energy negligible at nuclear scale)

---

## Background

The 6×6 Ma metric has 12 cross-shear components — 4 per pair
of material sheets:

| Sheet pair | Components | Status |
|---|---|---|
| e–p | σ_φeφp, σ_φeθp, σ_θeφp, σ_θeθp | Aggregate σ_ep = −0.091 pinned (R27 F18). Individual components untested. |
| e–ν | σ_φeφν, σ_φeθν, σ_θeφν, σ_θeθν | All set to zero. |σ_eν| > 0.05 would break the neutrino mass ratio (R26 F72). |
| ν–p | σ_φνφp, σ_φνθp, σ_θνφp, σ_θνθp | All set to zero. No measurable effect on MeV-scale observables (R28 F1). |

Of the 12 components, only 1 aggregate (σ_ep) is constrained.
The remaining 11 are formally free (Taxonomy §3.2.1).  All
existing studies treat cross-shears as static geometric
constants.

Cross-shear is distinct from tilt (ψ):

- **Cross-shear (σ):** Couples the *intrinsic* wave equations of
  two material sheets.  An off-diagonal metric entry between
  material dimensions on different sheets.  Enables cross-plane
  modes (e.g., the neutron spans Ma_e × Ma_p because σ_ep ≠ 0).

- **Tilt (ψ):** Orientation of a material sheet relative to S.
  An *embedding* parameter.  Uniform tilt produces no force
  (R36 F4).

## The question

### Part 1: energy transfer

Non-zero cross-shear couples the wave equations of two sheets.
The neutron is proof: its mode spans Ma_e × Ma_p, drawing
energy from both.  At zero cross-shear, each sheet's modes are
independent (E² = E²_e + E²_p, simply additive).  At nonzero
σ_ep, the effective metric mixes the sheets, redistributing
energy.

**Does this coupling allow dynamical energy transfer?**  If
σ_ep (or its individual components) were time-dependent —
fluctuating, driven by some excitation on one sheet — could
energy flow from Ma_e into Ma_p modes, or vice versa?  The
static metric gives a fixed energy distribution.  A dynamical
metric (σ(t)) would modulate the distribution.

### Part 2: phase perturbation

A standing wave on the proton sheet has a well-defined phase
(the configuration of the oscillation at a given moment).  If
the electron sheet is excited — say, an electron mode changes
its quantum state — the effective metric seen by the proton-
sheet mode changes slightly (through σ_ep).

The energy perturbation from electron-sheet activity on
proton-sheet modes is small: the electron dimensions contribute
~keV to nuclear modes that are ~MeV–GeV, a ratio of 10⁻⁴ to
10⁻⁵ (R29 F22).  But phase perturbation is a different
question.  In wave physics, a small perturbation to the
potential can advance or retard the phase of a standing wave
without disrupting its resonance — the amplitude stays the
same, only the timing shifts.

**Could electron-sheet activity modify the phase of proton-
sheet modes without disrupting the resonance?**  The proton
mode would still be the proton — same mass, charge, spin —
but its oscillation would be slightly advanced or retarded by
whatever is happening on the electron sheet.

### Part 3: individual cross-shear components

The 4 components within each σ block (e.g., σ_φeφp, σ_φeθp,
σ_θeφp, σ_θeθp) couple specific axes: ring-to-ring,
ring-to-tube, tube-to-ring, tube-to-tube.  If these have
different values (R26 N3 proposed this for PMNS mixing), a
specific mode on one sheet would couple preferentially to
specific modes on another sheet — not to all modes equally.

This axis-specific coupling could mean that *which* electron-
sheet mode is excited determines *how* the proton-sheet mode
is phase-perturbed.  Different electron states would imprint
different phase signatures on the proton.

## What's needed

1. **Dynamical cross-shear formalism.**  Promote σ from a
   static metric entry to a time-dependent field σ(t).  Write
   the coupled wave equations.  Compute the energy transfer
   rate between sheets.

2. **Phase perturbation calculation.**  For a proton-sheet
   mode at fixed energy, compute the phase shift induced by a
   small σ perturbation.  How large is it?  Is it detectable?

3. **Individual component effects.**  Break the σ_ep block
   into its 4 components and compute mode-specific coupling
   strengths.

## Why it matters

If cross-shear phase coupling exists, it would mean:

- Material sheets are not independent oscillators — they form
  a coupled system where activity on one sheet is "felt" by
  the others as phase modulation.

- The proton's internal clock (its oscillation phase) would
  carry an imprint of electron-sheet activity — a form of
  inter-sheet information transfer.

- The 11 "irrelevant" cross-shear components might not be
  irrelevant at all — they might control the *coupling
  structure* between sheets, even if they don't affect mode
  energies at the MeV scale.
