# R23. Neutrino from Harmonic Beating

Can the neutrino emerge as a collective excitation (phonon) of
three nearly-degenerate harmonics on the electron's T², with
the mass-squared splitting ratio constraining the aspect ratio r?

## Background

### The neutrino problem (R20 F14–F21, neutrino.md)

The neutrino cannot be a KK eigenmode on the electron's T².
The lightest uncharged mode is (0,±1) at 245 keV — five orders
of magnitude above the neutrino mass (< 0.8 eV).  No wave-packet
or geodesic construction closes the gap (F20, F21).

Three options survived R20:
- (a) Separate T² for neutrinos (viable but unsatisfying)
- (b) Geometry fluctuation (never computed)
- (c) Decay product from harmonic rearrangement (ruled out if
  "harmonics" means KK eigenmodes — but NOT if it means a
  collective excitation)

### Near-degeneracies exist (R20 F16)

Mode splittings on the electron's T² reach the sub-eV scale
naturally.  At E < 100 m_e, splittings as small as 0.29 eV
were found.  These arise from the irrational shear s₁₂ making
mode energies incommensurate — near-degeneracies are Diophantine
approximations, not fine-tuning.

### Parity selection rule (R21 F12, F15)

All harmonics in charged composites (proton, muon) must be
sin-like (odd parity) to preserve the muon charge constraint.
This constrains which modes participate in the harmonic condensate.

## Core idea

### The phonon mechanism

The proton's harmonic condensate is a many-body system of ~154
coupled modes (R20 F4).  In beta decay, the neutron's harmonic
spectrum rearranges from neutron-equilibrium to proton-equilibrium,
releasing 1.531 m_e of excess energy.

Among the occupied harmonics, three nearly-degenerate modes
(E₁ ≈ E₂ ≈ E₃) exist with sub-eV pairwise splittings.
During the rearrangement, the occupation shifts in these three
modes don't fully thermalize — they propagate away from the
proton as a collective excitation: a **phonon** of the harmonic
condensate.

Key distinction from R20 F20: the neutrino is NOT three full
quanta (which would have mass ~75 MeV).  It is a PERTURBATION
of occupation numbers — a ripple.  Its mass is set by the
mode-mode coupling strength (sub-eV for weak curvature coupling),
not by the individual mode energies.

### Three flavors from three splittings

Three nearly-degenerate modes produce three pairwise beat
frequencies.  Only two are independent:

    ΔE₂₁ = E₂ − E₁     ΔE₃₁ = E₃ − E₁

These map to two independent neutrino mass-squared differences:

    Δm²₂₁ = 7.53 × 10⁻⁵ eV²    (solar)
    Δm²₃₁ = 2.53 × 10⁻³ eV²    (atmospheric)

The ratio Δm²₃₁/Δm²₂₁ ≈ 33.6 is a dimensionless experimental
number.  In the model, this ratio depends on the mode quantum
numbers and the torus parameters (r, s).

### Geometry constraint

Given m_e (fixes the scale) and α = 1/137 (fixes s at each r),
the mode spectrum is a function of r alone.  Finding a triplet
of near-degenerate modes whose splitting ratio matches 33.6
would **pin down r** — the central free parameter of the model.

This would be the first physical fix for r, resolving Q67.

### Spin and entanglement

The phonon inherits angular momentum from the modes it involves.
Each sin-like harmonic has well-defined angular momentum from its
winding structure.  Angular momentum conservation in decay
(neutron → proton + electron + neutrino, all spin ½) REQUIRES
the neutrino to carry spin ½.

The phonon is born from modes shared with the proton.  The
proton's remaining occupation is correlated with the escaping
phonon — a geometric entanglement.  The proton "knows" which
modes shifted; the neutrino "knows" it came from those modes.
This mirrors the flavor/mass eigenstate structure of standard
neutrino physics.

### Oscillations

The three phonon branches have slightly different dispersion
relations (from the three slightly different mode energies).
A neutrino produced in a specific decay process populates a
specific superposition of these branches — a "flavor eigenstate."
As it propagates, the relative phases of the three branches
evolve at rates set by their mass differences, producing
oscillations between flavors.

This is the SAME mathematical structure as standard neutrino
oscillations, with the mass eigenstates identified as phonon
branches and the flavor eigenstates as decay-specific
superpositions.

## Planned approach

### Track 1: Near-degenerate triplet search  ✓ (complete)

Systematically search for triplets of uncharged modes on the
sheared T² whose pairwise energy splittings have ratio ≈ 33.6.

**Result:** At E_max = 100 m_e (~68k modes at r = 1), the ratio 33.6
is trivially achieved at keV-scale inner splittings — mode density
is so high (~686/m_e) that ANY ratio matches to 4+ decimal places.
The test becomes non-trivial only at sub-eV inner splittings, where
pair counts drop to ~85 (r = 1) through ~753 (r = 10).  Best sub-eV
match: r = 10, ratio = 33.82 (0.75% off).  The ratio alone does not
uniquely fix r.  See findings F1–F7.

### Track 2: Phonon dispersion and effective mass

Given a candidate triplet, compute the phonon dispersion
relation for collective excitations involving these three modes.

Steps:
1. Write the Hamiltonian for coupled modes on the curved torus.
2. Linearize around the proton's equilibrium occupation.
3. Compute the phonon spectrum (small oscillations).
4. Extract effective masses for the three phonon branches.
5. Compare to neutrino mass bounds (< 0.8 eV).

### Track 3: Spin and quantum numbers

Verify that the phonon carries the correct quantum numbers.

Steps:
1. Compute the angular momentum of each sin-like mode.
2. Show that the occupation-shift ripple carries spin ½.
3. Verify charge = 0 (trivially satisfied for uncharged modes).
4. Check lepton number conservation (if applicable).

### Track 4: Decay dynamics and flavor production

Model the decay process to determine which phonon superposition
is produced.

Steps:
1. Describe the neutron → proton occupation shift.
2. Determine which modes' occupations change during decay.
3. Compute the overlap with the three phonon branches.
4. Show that different decay channels (beta, muon capture)
   produce different superpositions (i.e., different flavors).

## Dependencies

- **R20 (complete):** Mode catalog, neutrino constraints F14–F21,
  neutron-proton spectrum difference.
- **R21 (complete):** Eigenmodes on curved torus (F1–F5),
  parity selection rule (F12, F15), shear doesn't break parity.
- **R19 (complete):** α formula, shear s(r), mode energies.
- **neutrino.md:** Comprehensive problem analysis, Directions A+B.

## Relation to other questions

- Q14: neutrino topology (this proposes a specific mechanism)
- Q67: what fixes r (triplet ratio could provide the constraint)
- Q70: neutrino from beating harmonics (this is the full study)

## Risk assessment

**Track 1 (triplet search): resolved — not a sharp test.**
Triplets matching ratio 33.6 exist at all r values, but only at
splittings above the sub-eV regime.  At sub-eV scale, match quality
(0.75%–2.8% off) is limited by counting statistics, not geometry.
The ratio test does not falsify the model but does not fix r either.
Higher E_max or analytical Diophantine methods could sharpen the test.

**Track 2 (phonon mass): high risk.**
Getting a sub-eV effective mass requires weak mode-mode coupling.
The coupling strength hasn't been computed (this is also R22's
domain).  If the coupling is too strong, the phonon is too heavy.

**Track 3 (spin): medium risk.**
Angular momentum conservation requires spin ½.  Whether the
phonon naturally carries half-integer spin is the deepest
theoretical question.  Fermionic collective excitations exist
(spinons) but are rare and require specific symmetry conditions.

**Track 4 (flavor): lower risk.**
If Tracks 1–3 succeed, the flavor structure follows from the
decay kinematics and mode coupling.  This is an extension, not
a new obstacle.

**Overall: the study is worth continuing.**  Track 1 showed the
ratio test is not sharp at E_max = 100 — triplets exist everywhere
at keV scale, while sub-eV statistics are too sparse.  But the
model is NOT falsified: good matches exist at every r.  The next
discriminating test is Track 2 (phonon mass), which provides an
absolute scale constraint independent of mode-counting statistics.
