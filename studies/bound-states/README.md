# R27. Bound states from T⁶ — atoms and nuclei as oscillation patterns  *(draft)*

**Questions:** Q28 (photon absorption / energy levels), Q32 (energy-geometry)
**Type:** compute/analytical  **Depends on:** R26, R19, R15

## Motivation

R26 showed that the T⁶ produces an emergent neutron — a single
cross-sheet mode (1,2,0,0,1,2) with the right mass, zero charge,
and natural instability.  The neutron was not found by computing
a force between an electron and a proton.  It was found as an
oscillation pattern of the geometry that *happens to have* the
properties of a neutron.

This study asks: **does the T⁶ support stable oscillation
patterns with the properties of atoms and nuclei?**

A hydrogen atom, in this picture, is not "an electron orbiting a
proton via a force."  It is a particular oscillation pattern of
the T⁶ — involving electron-sheet and proton-sheet quantum
numbers — that is stable and has the right total energy, charge,
and angular momentum.  The energy levels of hydrogen would be
a family of related patterns, not solutions to a Schrödinger
equation with an imposed potential.

This framing is consistent with the model's philosophy: everything
so far (mass, charge, spin, the neutron) has been a property of
oscillation patterns on compact geometry.  Atoms should be no
different.


## Core hypothesis

**Compound oscillation patterns on the T⁶ — multi-mode
configurations or higher-order modes spanning multiple T² sheets —
produce stable states with the observed properties of atoms and
simple nuclei.**

The key distinction from the neutron:
- The neutron is a *single mode* (1,2,0,0,1,2) — one standing
  wave with definite quantum numbers.
- An atom may be a *multi-mode configuration* — multiple standing
  waves coexisting on the T⁶, where the total pattern is stable
  because the cross-shear coupling locks them together.

Or it might be something else entirely: a single high-quantum-
number mode that happens to have the right energy, or a
nonlinear effect not captured by the single-mode approximation.
The study's job is to find out.


## What we want to know

1. **Is there a stable T⁶ pattern with the properties of
   hydrogen?**  Total charge +e − e = 0, total mass ≈ m_p + m_e
   minus 13.6 eV, discrete excited states at −13.6/n² eV.

2. **Is there a stable T⁶ pattern with the properties of a
   deuteron?**  Proton + neutron, binding energy 2.224 MeV,
   spin 1, charge +e.

3. **Does the T⁶ geometry naturally produce discrete energy
   levels?**  The periodic boundary conditions of the compact
   dimensions enforce quantization.  Do these quantization
   conditions, applied to compound patterns, reproduce the
   spacing of atomic energy levels?

4. **Does α emerge?**  The hydrogen ground state energy is
   −½ α² m_e c².  If the T⁶ produces −13.6 eV as output, the
   fine-structure constant is geometrically determined.


## Approach

### Track 1 — Self-consistent neutron mass

A prerequisite.  At each σ_ep, re-derive L₂ and L₆ so that the
electron and proton masses are exactly reproduced (inner 2D root-
find), then compute the self-consistent m_n − m_p.

This validates the cross-shear framework quantitatively and pins
σ_ep from the neutron mass difference (1.293 MeV).

**Deliverable:** The physically correct σ_ep and self-consistent
m_n − m_p, or a finding that no σ_ep achieves this.

**Infrastructure:** Uses `lib/t6.py` (shared T⁶ model).


### Track 2 — Multi-mode energy on T⁶

Develop the formalism for computing the total energy of a T⁶
configuration with multiple simultaneously active modes.

**Key question:** When two modes (e.g., electron (1,2,0,0,0,0)
and proton (0,0,0,0,1,2)) are both present on the T⁶, is the
total energy simply E_e + E_p (non-interacting), or does the
cross-shear metric produce cross-terms?

**Method:**

The energy density of a field on the T⁶ involves the metric:

    ℰ = ½ G^{ij} ∂_i ψ ∂_j ψ

If ψ = ψ_e + ψ_p, then:

    ℰ = ½ G^{ij} (∂_i ψ_e ∂_j ψ_e + ∂_i ψ_p ∂_j ψ_p
                    + 2 ∂_i ψ_e ∂_j ψ_p)

The first two terms give E_e + E_p.  The third (cross-term)
depends on the off-diagonal (cross-shear) entries of G^{ij}.
If this cross-term is nonzero and depends on the 3D separation
between the modes, it is the geometric mechanism for binding.

If the cross-term integrates to zero (because the compact modes
are orthogonal), there is no interaction and the atoms picture
requires a different mechanism.

**Deliverable:** Whether multi-mode cross-energy exists, and if
so, its magnitude and dependence on mode separation.


### Track 3 — Hydrogen-like patterns

Search for T⁶ configurations with the properties of hydrogen.

**Approach A — Mode family search:**

The hydrogen ground state has energy m_p + m_e − 13.6 eV.  Look
for T⁶ modes (single standing waves) with:
- Total charge 0 (electron + proton contributions cancel)
- Energy within ~14 eV of m_p + m_e
- Quantum numbers involving both electron and proton sheets

The neutron mode (1,2,0,0,1,2) has energy m_p + 1.293 MeV — far
too high (that's a different kind of electron-proton combination).
But modes with large ring windings and small tube windings might
have lower cross-sheet energy.

**Approach B — Multi-mode stability:**

If Track 2 shows that multi-mode cross-energy exists, compute the
total energy of electron + proton as a function of their relative
phase / separation.  Stable configurations (energy minima) are
bound states.  Excited states are higher local minima.

**Approach C — Nonlinear mode locking:**

If the T⁶ wave equation has nonlinear terms (from backreaction of
the field on the geometry), two modes can lock into a stable
compound pattern.  Investigate whether the effective nonlinearity
of the T⁶ supports hydrogen-like locking.

**Deliverable:** A T⁶ configuration with hydrogen-like properties,
or a clear identification of what prevents it.


### Track 4 — Deuteron-like patterns

Same approach as Track 3, but for the proton-neutron system.

The deuteron has:
- Charge +e (proton contributes +e, neutron contributes 0)
- Mass: m_p + m_n − 2.224 MeV
- Spin 1

Look for T⁶ configurations (single modes or multi-mode patterns)
with these properties.  The binding energy (2.224 MeV) is much
larger than hydrogen's (13.6 eV), so the cross-sheet coupling
would need to be stronger — or the mechanism is fundamentally
different (e.g., mode mixing rather than potential-well binding).

**Deliverable:** A deuteron-like T⁶ pattern, or a diagnosis of
why the simplest nucleus doesn't emerge.


### Track 5 — Energy level structure

If Tracks 3–4 succeed, investigate the spectrum of excited states.

For hydrogen: do the bound configurations come in a series with
energies approaching −13.6/n² eV?  If so, the model predicts
atomic spectroscopy from geometry.

For nuclei: does the proton-neutron system have excited states
matching known nuclear energy levels?

**Deliverable:** Energy level spectrum of the hydrogen-like and
deuteron-like patterns.


## Infrastructure

All tracks use the shared `lib/t6.py` module for:
- Metric construction (`build_scaled_metric`)
- Mode energies (`mode_energy`)
- Charge and spin (`mode_charge`, `mode_spin`)
- Spectral scanning (`scan_modes`)

Track-specific scripts go in `bound-states/scripts/`.


## What this study could determine

### Free parameters constrained

| Source | Constraint |
|--------|-----------|
| m_n − m_p = 1.293 MeV | Pins σ_ep |
| Hydrogen binding 13.6 eV | Constrains cross-shear mechanism strength |
| α from binding energy | Relates r_e to shears (solves the α problem) |
| Deuteron binding 2.224 MeV | Further constrains σ_ep |

### Possible outcomes

**Best case:** The T⁶ supports stable patterns with the right
energies for hydrogen and the deuteron.  The binding energies
emerge from the geometry without imposing a Coulomb potential.
α is determined.

**Partial success:** The self-consistent neutron works (Track 1)
and multi-mode cross-energy exists (Track 2), but the hydrogen
binding energy requires the still-free aspect ratios to be known
first.  Points to R28 (which constrains aspect ratios from the
particle spectrum) as a prerequisite.

**Null result:** Multi-mode cross-energy is zero — the T⁶
produces particles but not forces or bound states.  The model
describes the particle zoo but not chemistry or nuclear physics.
This would be an important finding: it would mean the T⁶ needs
additional structure (warping, nonlinearity, or a mechanism not
yet identified) to produce interactions.


## Relation to prior studies

| Study | Relationship |
|-------|-------------|
| R26 | T⁶ framework, neutron discovery, metric infrastructure |
| R19 | Shear-charge mechanism — origin of the EM field on T² |
| R15 | The α problem — this study could solve it |
| Q28 | Photon absorption / energy levels — addressed directly |
| R28 | Companion study: unstable particle spectrum (may constrain free parameters first) |


## What this study does NOT address

- **Unstable particle spectrum** (μ, τ, W, Z, mesons).  That is R28.
- **Quarks and confinement.**  Nuclear binding here is between
  protons and neutrons.
- **Many-body nuclear physics.**  Only hydrogen and the deuteron
  are attempted.
