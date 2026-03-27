# The T² Energy Gap and the Origin of Quantization

R20 established that the electron's T² has a hard energy floor: no
non-trivial compact mode exists below 245 keV.  Between zero (a free
photon in 3D) and 245 keV (the lightest KK eigenmode), the spectrum
is empty.  This gap is exact — forced by the periodic boundary
conditions of a finite compact geometry.

This document explores the implication: the T² gap may provide a
geometric mechanism for effects that quantum mechanics postulates
but does not explain.  Energy quantization, creation thresholds,
and the quantum-classical boundary all follow from the compact
cavity's cutoff.


---

## 1. The gap

The electron's T² (sheared, with r = 1, s₁₂ ≈ 0.165) has side
lengths L₁ ≈ L₂ ≈ 5.1 × 10⁻¹² m, set by the electron mass (R13,
R19).  Standing waves on this surface have quantized momenta, and
the dispersion relation E = ℏc|k| maps each mode to a definite
energy.

The lowest-energy modes are:

| Mode | Energy | Charge | Spin | Identity |
|------|--------|--------|------|----------|
| (0,0) | 0 | 0 | 1 | 3D photon (zero mode) |
| — | — | — | — | **GAP: nothing exists here** |
| (0,±1) | 0.48 m_e = 245 keV | 0 | 0 | lightest KK mode |
| (1,2) | 1.00 m_e = 511 keV | −e | ½ | electron |
| (−1,−2) | 1.00 m_e = 511 keV | +e | ½ | positron |

The gap from 0 to 245 keV is not approximate.  It is a geometric
fact: the torus is ~5 pm across, and no standing wave with wavelength
longer than ~5 pm fits.  The boundary conditions are periodic
(the space closes on itself), so there is no way to have "part of
a wavelength" — you fit integer numbers of wavelengths or nothing.

This is the same physics as a waveguide cutoff.  A waveguide of
width d has a lowest propagating mode at frequency f_c = c/(2d).
Below f_c, nothing propagates — waves are evanescent.  The T² gap
is the compact-dimension waveguide cutoff.


---

## 2. Getting in: why low-energy photons ignore compact dimensions

A 3D photon (the zero mode on T²) has no compact structure.  It
carries zero momentum in the θ₁ and θ₂ directions.  To create a
compact-dimension excitation — to "enter" T² — the photon must
deposit enough energy to populate at least one non-trivial eigenmode.

Below 245 keV: no T² mode is available.  The photon has nowhere
to put its energy in the compact dimensions.  It propagates freely
in 3D, obeying classical Maxwell's equations, as if the compact
dimensions do not exist.

At 245 keV: the (0,±1) channel opens.  A photon with this energy
can, in principle, excite the lightest compact mode.

At 1.022 MeV: the electron-positron channel opens.  A photon can
create two (1,2) winding modes with opposite charges.  This is pair
creation — and the threshold (1.022 MeV = 2 × 511 keV) is not a
quantum postulate but a cavity resonance condition: two standing
waves of the required type must fit simultaneously.

| Energy range | Available compact channels | Physics |
|---|---|---|
| E < 245 keV | none | Classical 3D electromagnetism |
| 245 keV ≤ E < 511 keV | (0,±1) uncharged modes | Compact excitations possible |
| 511 keV ≤ E < 1.022 MeV | above + single charged modes | Not enough for a pair |
| E ≥ 1.022 MeV | above + electron-positron pairs | Pair creation threshold |

The threshold behavior is geometric.  There is no axiom declaring
"energy must exceed 2mc² for pair creation."  Instead: two standing
waves of wavelength λ_e = L_e must fit on T², and each carries
energy m_e c².  The threshold is 2 × m_e c² because two modes must
be populated, each costing one unit of compact energy.

**Why visible light is classical.**  Visible photons have energy
~2 eV — five orders of magnitude below the T² gap.  They cannot
interact with compact dimensions at all.  To visible light, the
universe has exactly three spatial dimensions.  Classical
electromagnetism is not an approximation to some deeper quantum
theory; it is the exact physics of photons too weak to reach the
compact modes.


---

## 3. Getting out: why trapped energy stays trapped

Energy inside T² faces two distinct barriers to escape.

### Topological trapping (absolute)

The electron's (1,2) winding is a topological invariant.  You cannot
smoothly unwrap a path that winds once around the tube and twice
around the ring.  This energy is permanently confined — it can only
escape by meeting an opposite-winding mode (−1,−2) and annihilating.

Pair annihilation releases all the compact energy at once as 3D
photons.  It is all-or-nothing because topology is discrete: you
either have the winding or you don't.  There is no "half unwound"
state.  This discreteness is not a quantum postulate — it is a
mathematical property of closed curves on a torus.

### Gap trapping (threshold)

Even uncharged harmonics face the gap.  A harmonic with energy
n × m_e is a standing wave on T².  To escape as a 3D photon, it
must convert its compact momentum to zero — becoming the (0,0) zero
mode.  This is not a gradual process.  The mode must shed ALL its
compact momentum in one step, because there are no intermediate
states between its energy and zero.

There is no way to "slowly bleed" energy from T² to 3D in amounts
smaller than one eigenmode.  The transfer is quantized by the cavity
spectrum.

This means emission from T² is inherently discrete:

- A mode can radiate its entire energy as a photon (if coupling
  allows and selection rules permit) — one quantum.
- Or it stays.  There is no fractional emission.

This is the geometric origin of the photon: electromagnetic energy
comes in lumps because the compact cavity has discrete eigenmodes.
A "photon" in the T² framework is what happens when one eigenmode
decays to the zero mode — releasing exactly one quantum of compact
energy into 3D.


---

## 4. What this explains that QM postulates

Standard quantum mechanics takes certain principles as axioms —
things declared true without derivation.  Several of these follow
from the T² gap as geometric consequences.

### Energy quantization

**QM postulate:** Energy is quantized.  E = nhf (Planck, 1900).

**T² derivation:** Compact dimensions are finite and periodic.
Standing waves on a finite periodic surface have discrete allowed
wavelengths.  Each allowed wavelength maps to a definite energy
via E = ℏc|k|.  The energy spectrum is discrete because the
geometry is finite.  Planck's constant ℏ enters through the
dispersion relation — its value is set by the torus scale.

### Pair creation threshold

**QM postulate:** Creating a particle-antiparticle pair requires
energy ≥ 2mc² (Dirac, 1928).

**T² derivation:** Creating a pair means populating two compact
modes — one (1,2), one (−1,−2).  Each mode requires energy m_e c²
to excite.  The threshold is 2 m_e c² because two standing waves
must fit.  This is a cavity resonance condition, not a decree.

### Discrete emission and absorption

**QM postulate:** Atoms emit and absorb photons of specific energies
(Bohr, 1913).

**T² derivation (partial):** The compact cavity has discrete
eigenmodes.  When a mode decays or is excited, the energy change
is the difference between two eigenvalues — a specific, discrete
amount.  The "photon" is the packet of energy transferred between
compact modes and 3D, and its energy is quantized by the mode
spacing.

(Caveat: atomic energy levels involve the electron's 3D spatial
wavefunction, not just the compact modes.  The T² gap sets the
particle properties — mass, charge — which then determine the
atomic spectrum through the 3D Schrödinger equation.  The compact
quantization underlies the spatial quantization but does not
replace it.  See Section 6.)

### Stability of matter

**QM postulate:** Electrons don't spiral into nuclei because
energy levels are discrete (Bohr model) or because the uncertainty
principle prevents localization (Heisenberg).

**T² derivation (partial):** The electron is a topological winding
mode.  Its energy is m_e c² — the energy of one (1,2) standing wave.
You cannot take energy away from this mode without unwinding it,
and unwinding requires an antiparticle.  The electron doesn't
radiate and collapse because it IS a standing wave, and standing
waves on compact dimensions are intrinsically stable.  There is no
lower-energy state to decay into (the electron is already the
lightest charged spin-½ mode on T²; R14 F10, R19 F31).


---

## 5. The quantum-classical boundary as the KK gap

A longstanding puzzle in physics is: where does quantum behavior end
and classical behavior begin?  The Copenhagen interpretation says
the boundary is the "measurement" — but what counts as a measurement
is never defined precisely.  Decoherence theory says classicality
emerges from environmental entanglement — but doesn't explain why
some systems resist decoherence.

The T² model offers a concrete alternative: the quantum-classical
boundary is the KK energy gap.

**Below the gap (E < 245 keV):**
- Photons propagate as classical waves in 3D
- No compact-dimension channel is available
- Maxwell's equations are purely 3D and continuous
- Physics is genuinely classical — not "approximately" classical,
  but exactly classical, because the extra dimensions are dark

**Above the gap (E ≥ 245 keV):**
- Compact modes can be excited
- Interactions become discrete (quantized by the mode spectrum)
- Energy comes in lumps (each lump = one compact eigenmode)
- Physics looks "quantum"

The transition is not fuzzy.  It is set by a definite energy scale
(245 keV on the electron's T²), which is determined by the torus
size, which is determined by the electron mass.

This does NOT mean that all physics below 245 keV is classical.
Existing particles (electrons, protons) are already compact
excitations.  Their interactions with low-energy photons are
mediated by their compact structure, which introduces discrete
behavior even at eV scales.  But the discrete behavior comes from
the particles (which are above the gap), not from the photons
(which are below it).

A universe with no compact excitations — no electrons, no protons,
just photons below 245 keV — would be perfectly classical.  Quantum
behavior enters when photons interact with compact-dimension
structures.  The "quantum world" is the compact-dimension world.


---

## 6. Two layers of quantization

The T² model has two distinct mechanisms that produce discrete
behavior, operating at different scales.

### Layer 1: Compact quantization (the T² gap)

**Scale:** 245 keV to MeV
**Mechanism:** Periodic boundary conditions on T² discretize
the allowed momenta and energies.
**What it determines:**
- Particle masses (m_e, m_p, m_n, ...)
- Particle charges (±e, 0)
- Creation/annihilation thresholds (pair production at 1.022 MeV)
- Stability (topological winding conservation)

This layer is fundamental.  It comes from the geometry of the
compact dimensions and cannot be derived from anything simpler
within the model.

### Layer 2: Spatial quantization (atomic/orbital structure)

**Scale:** eV
**Mechanism:** An electron (already a T² excitation) is bound to
a nucleus by the Coulomb force.  The electron's 3D wavefunction
must satisfy boundary conditions imposed by the potential well.
These boundary conditions discretize the allowed energies (atomic
energy levels).

**What it determines:**
- Atomic spectra (Rydberg, Balmer, Lyman series)
- Chemical bonds
- Solid-state band structure

This layer is derived.  Given a particle with mass m_e and charge e
(both set by Layer 1), the Schrödinger equation in a Coulomb
potential produces discrete energy levels.  The quantization of
atomic physics is a CONSEQUENCE of the particle properties, which
are themselves consequences of compact geometry.

### How they connect

A photon absorbed by an atom changes the electron's 3D orbital
(Layer 2) without changing its compact mode — the electron remains
(1,2) on T².  The photon is a zero mode (no compact structure) that
couples to the electron's 3D wavefunction through the electron's
charge, which is a compact property.

This is why atomic transitions involve eV-scale photons even though
the compact gap is at 245 keV.  The photon doesn't need to cross
the compact gap — it interacts with the electron's 3D state, not
its compact state.  But the reason the electron HAS a charge for
the photon to couple to is Layer 1 (the (1,2) winding number on
T²).

The hierarchy is:

    Compact geometry (T²)
        → particle properties (mass, charge, spin)
            → 3D dynamics (Schrödinger/Dirac equation)
                → atomic energy levels
                    → discrete photon emission/absorption

Each level of quantization is derived from the one above it.  At
the top is geometry.


---

## 7. Implications for the neutrino problem

The gap is directly responsible for the neutrino problem described
in [`neutrino.md`](neutrino.md).  The neutrino needs mass < 0.8 eV,
but the lightest non-trivial T² mode is 245 keV.  The gap that
makes classical electromagnetism work (by hiding compact dimensions
from low-energy photons) is the same gap that makes the neutrino
hard to accommodate.

This connects the two problems: **the quantum-classical boundary
and the neutrino are two faces of the same geometric fact** — the
T² cavity has a cutoff.

If the neutrino is a standard eigenmode, it must live on a T² large
enough for sub-eV modes — which means a separate, much larger T²
(F18a).  If the neutrino is NOT a standard eigenmode — if it is a
collective excitation, a beat, or a geometry fluctuation (Directions
A–E of the neutrino analysis) — then it exists BELOW the gap by
being a qualitatively different kind of excitation.

The neutrino would then be the one known particle that lives in the
gap.  Not a compact standing wave, but something else: a ripple in
the occupancy spectrum, a phase beat, a topological scar.  It would
be "quantum" (massive, spin-½) without being a cavity eigenmode.
It occupies the space between classical and quantum — which might
explain why it is so elusive.


---

## 8. Testable consequences

If the T² gap is the origin of quantization, several predictions
follow:

**1. No particles with mass between 0 and ~245 keV (except neutrinos).**
The gap predicts a mass desert between zero (photon) and the
lightest KK mode.  The only known particles in this range are
neutrinos (< 0.8 eV) — which, per the neutrino analysis, are
likely a different type of excitation.  If a particle with mass
in the 1 eV to 100 keV range were discovered, it would challenge
the single-T² model.

**2. Pair creation thresholds are exact.**
The e⁺e⁻ threshold at 1.022 MeV is a geometric resonance, not an
approximate rule.  The T² model predicts no pair creation below
this energy, no matter how intense the field.  (In QED, virtual
pairs can be produced below threshold via the Schwinger mechanism
in extreme fields.  Whether the T² model reproduces this effect
depends on how nonlinear mode coupling works on the curved torus.)

**3. Classical electromagnetism is exact below the gap.**
Not approximate — exact.  Maxwell's equations in 3D are the
complete description of photon physics below 245 keV.  Quantum
corrections (vacuum polarization, light-by-light scattering) arise
only through coupling to compact excitations (virtual pairs), and
their strength is set by how far below the gap the photon is.
This predicts that quantum corrections scale as powers of
E/E_gap — which is consistent with their known scaling as
powers of α = e²/(4πε₀ℏc) ≈ 1/137.


---

## References within this project

| Study | Connection |
|---|---|
| R20 F7, F21 | The 245 keV floor and proof that no lighter uncharged mode exists |
| R20 F14 | Neutrino excluded from electron's T² by the gap |
| R14 F10 | Spin quantization: only q = 1 (bosons) and q = 2 (fermions) allowed |
| R19 F31 | No charged particle lighter than the electron on T³ |
| R13 | Electron as winding mode; torus size set by m_e c² |
| R12 F14 | Two-domain picture: flat for mass/spin, embedded for charge |
| Q28 | Photon absorption and excited electrons |
| Q32 | Energy and geometry as only fundamentals |
| [`neutrino.md`](neutrino.md) | The neutrino lives in the gap — see Directions A–E |
