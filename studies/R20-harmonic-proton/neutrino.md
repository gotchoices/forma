# The Neutrino Problem on the Material Sheet

R20 demonstrated that the electron, proton, neutron, muon, and tau can
all be built from modes on a single sheared material sheet: a charged (1,2)
fundamental carries spin ½ and charge ±e, while uncharged harmonics
(n, 2n) add mass without changing the charge.  Decay, stability, and
the lepton mass hierarchy all follow from charge conservation and the
mode spectrum.

The neutrino is the one particle that resists this construction.

This document collects what R20 proved about the neutrino, identifies
the precise obstacle, and lays out investigation directions for
producing the neutrino from the same material sheet — without invoking a separate
material geometry.


---

## 1. What R20 established (the hard constraints)

R20 ran five tracks that progressively closed off the simplest paths
to a neutrino on Ma_e.

| Constraint | Source | What it means |
|---|---|---|
| Lightest uncharged spin-½ mode is (2,4) at 2 m_e = 1.022 MeV | F14 | Six orders of magnitude too heavy |
| Lightest uncharged mode of *any* spin is (0,1) at 0.48 m_e = 245 keV | F7, F21 | Hard floor set by torus size (L ~ 5 pm) |
| No triplet of uncharged modes sums to 1.531 m_e (neutron excess) | F19 | Three-mode neutrino packet ruled out |
| Complex geodesics (high winding numbers) always give higher energy | F21 | No clever knot construction can get below 245 keV |
| Every uncharged mode has rest mass ≥ 245 keV; neutrino < 0.8 eV | F20 | F18c (neutrino as ejected harmonics) eliminated |

### The three options left after R20 (F18)

**(a) Separate material sheet.**  The neutrino is a (1,2) fundamental on its own
larger torus, with L_ν ~ 1.5 μm.  Experimentally allowed at the KATRIN
bound (F15).  This works mechanically but introduces a new material
geometry for each neutrino flavor — it is descriptive rather than
explanatory.

**(b) Geometry fluctuation.**  The neutrino is not a wave ON the material sheet but a
ripple OF it — a fluctuation of the torus shape parameters themselves.
Naturally uncharged and naturally light (suppressed by geometric
stiffness).  Conceptual only; never computed.

**(c) Created in decay as ejected harmonics.**  Ruled out by F20.  KK
mode rest masses (≥ 245 keV) are five orders of magnitude above the
neutrino mass.  No wave-packet construction closes the gap.

Option (a) is viable but unsatisfying: it amounts to creating a new
free parameter (L_ν) for each observation.  Option (c) is dead.
Option (b) was never developed.

The question is whether there is a **(d)** — a mechanism that keeps
the neutrino on the same material sheet as the electron, without requiring it to
be a standard Kaluza-Klein eigenmode.


---

## 2. The energy accounting problem

In beta decay the neutron has 1.531 m_e (0.782 MeV) more harmonic
energy than the proton (F9, F11).  When the electron fundamental
escapes, this excess energy must go somewhere.

On a **flat material sheet**, the available channels are exactly:

1. **Zero mode** (n₁ = 0, n₂ = 0): zero material momentum, zero rest
   mass.  This is a **photon**.  It propagates in 3D at speed c.  But
   if the decay energy goes entirely into photons and the electron, the
   decay is two-body (proton + electron), and the electron emerges
   monoenergetically at 0.782 MeV.  This contradicts the observed
   continuous beta spectrum, which requires a *third* particle sharing
   the energy.

2. **KK eigenmodes** (n₁, n₂ with non-trivial mode numbers): rest
   mass ≥ 245 keV.  Far too heavy to be a neutrino.

There is nothing in between.  On the flat material sheet, the mass spectrum has a
**gap** — from exactly 0 (photon) to 245 keV (lightest KK mode) —
with no states inside it.

The gap arises because the torus is small.  The electron mass sets the
torus size: L₁ ≈ L₂ ≈ 5.1 × 10⁻¹² m (at r = 1).  The lightest
standing wave on this torus has wavelength λ = L₂ ≈ 5 pm, which
corresponds to E = hc/λ ≈ 245 keV.  A neutrino-wavelength excitation
(λ_ν ~ 1.5 μm at the KATRIN bound) spans roughly 300,000 torus
periods.  It cannot fit as a standing wave on this material sheet.

So the flat-material-sheet model says the excess energy becomes photons.  That
contradicts three-body kinematics.  And it can't form a KK mode light
enough to be a neutrino.

**This is the contradiction.**  The energy can't leave as a photon
(beta decay requires a massive third particle), and it can't be a KK
mode (too heavy).  Something about the flat-material-sheet eigenmode picture is
incomplete.

### What the energy can't do

The energy cannot just disappear.  Conservation of energy and momentum
require the excess 0.782 MeV to be carried by something.  Conservation
of angular momentum requires that something to have spin ½ (the
neutron and proton are both spin ½; the emitted electron is spin ½;
a third spin-½ particle is needed to balance).  The continuous beta
spectrum requires the third particle to be very light — at most
~0.8 eV in rest mass.

These are exactly the neutrino's properties: spin ½, charge 0,
mass < 0.8 eV, produced in beta decay.  The material-sheet model must find a way
to produce this object.


---

## 3. What path would trapped sub-threshold energy take on the material sheet?

Suppose some energy from the decay is left behind on the material sheet — too little
to form any KK eigenmode, but carrying some imprint of the material
dimensions (so it isn't a photon).  What does it do?

### On the flat material sheet: the energy has nowhere to go

On a flat torus with periodic boundary conditions, the only
normalizable solutions are plane waves with quantized momenta.  A wave
function that is non-uniform on the material sheet but has energy below the first
eigenmode (245 keV) does not exist — the boundary conditions forbid it.
The energy is forced to be either a winding mode or the zero mode
(photon).  There is no intermediate option.

This is the fundamental limitation of the flat-material-sheet model.  The spectrum
is discrete and gapped, and no amount of cleverness within linear
theory on the flat material sheet can create a sub-eV massive state.

### On the embedded (curved) material sheet: new possibilities

The physical material sheet is not flat — it is embedded in 3D as a torus with
position-dependent Gaussian curvature (R12, R21):

    K(θ₁) = cos(θ₁) / (a(R + a cos(θ₁)))

At the outer equator (θ₁ = 0), K > 0 (positive, sphere-like
curvature).  At the inner equator (θ₁ = π), K < 0 (negative,
saddle-like curvature).  The curvature varies smoothly between these
extremes.

This curvature acts as an **effective potential** for waves on the material sheet.
A mode propagating on a flat torus sees uniform geometry everywhere.
A mode on the embedded torus sees hills and valleys — regions where
propagation is easier or harder.

On this curved surface, sub-threshold energy could be **localized in
a curvature potential well**: sitting near a specific θ₁ position,
not winding around either direction, oscillating in place while
propagating through 3D.

Its "path on the material sheet" would be: **stationary**.  A localized bump at a
fixed angular position, carried through 3D by its bulk momentum.
Fundamentally different from the electron's helical (1,2) winding.

However, there is a quantitative problem.  Curvature corrections to
eigenvalues are O(a/R) relative to the flat-material-sheet values.  With
a/R ≈ 1 (at r = 1), corrections can shift the 245 keV floor by
factors of order unity — perhaps to ~100 keV or ~50 keV.  Getting
to sub-eV requires a suppression of 10⁵, far beyond what curvature
perturbation theory can deliver.

Curvature alone almost certainly cannot bring a mode down to the
neutrino scale.  But it opens the door to qualitatively new types
of excitation that don't exist on the flat material sheet.


---

## 4. Beyond eigenmodes: what the flat material sheet is missing

The flat-material-sheet model treats the torus as a fixed background with
decoupled eigenmodes.  Every excitation decomposes into independent
plane waves; every plane wave has quantized energy ≥ 245 keV (for
uncharged modes).  There is no room for a neutrino.

But the physical torus is not a fixed background with decoupled modes.
Three features of the real system break the flat-material-sheet picture:

1. **Embedding curvature** breaks mode orthogonality.  On the embedded
   torus, eigenmodes are NOT the same as flat-material-sheet plane waves.  Modes
   couple to each other through the curvature.  R21 Track 4 is designed
   to compute these coupling coefficients.

2. **The proton is a many-body system.**  In the thermal model, the
   proton contains harmonics up to n ~ 154.  This is not a single mode
   — it is a condensate of many coupled modes.  Many-body systems have
   collective excitations (quasi-particles) whose properties can differ
   dramatically from those of their constituents.

3. **Decay is a dynamical process.**  When the neutron's electron
   fundamental escapes, the remaining harmonic energy must rearrange
   from the neutron's equilibrium to the proton's.  This rearrangement
   is not instantaneous — it proceeds through mode-mode coupling, which
   is weak (nearly flat material sheet).  Non-equilibrium configurations that arise
   during this process may have properties not captured by the
   equilibrium eigenmode picture.

Each of these features suggests a different mechanism for the neutrino.
The following sections develop five investigation directions.


---

## 5. Investigation directions

### Direction A: Harmonic condensate phonon

**Priority: high.  Most promising path.**

#### Concept

The proton is not one mode — it is a many-body system of ~154 occupied
harmonics (in the thermal picture with T' ≈ 34 m_e, F4).  A many-body
system has collective excitations — quasi-particles — whose energies
can be far below the energies of the individual constituents.

The canonical analogy is a crystal.  Individual atoms in a crystal have
binding energies of ~eV, but phonons (collective vibrations of the
lattice) can have energies of ~meV — a thousand times smaller.  The
phonon mass is not bounded by the atom mass.

Similarly, in a superconductor, individual electrons have rest mass
0.511 MeV, but Bogoliubov quasi-particles can have arbitrarily small
effective masses near the Fermi surface.

#### Application to the neutrino

The proton's harmonic occupancy spectrum {f(n)} defines a
configuration — how much energy sits in each harmonic.  A small
perturbation of this spectrum — shifting a tiny amount of energy from
harmonic n to harmonic n+1 — creates a "ripple" in the occupancy
profile.  If modes are coupled (through embedding curvature), this
ripple propagates through the composite and, when it escapes during
decay, travels through 3D as a quasi-particle.

The effective mass of this quasi-particle depends on:

- **Mode-mode coupling strength** (from embedding curvature —
  exactly what R21 Track 4 needs to compute).
- **Stiffness of the occupancy distribution** (how much energy it
  costs to redistribute energy among harmonics).
- **Dispersion relation** of the perturbation (how the ripple's
  energy depends on its wavelength).

If the coupling is weak — which we expect, because the modes are
*nearly* orthogonal on a *nearly* flat torus — the effective mass can
be naturally sub-eV.

#### Properties

- **Charge 0:** automatically, since it is a perturbation of uncharged
  harmonics.
- **Mass ~ sub-eV:** set by the coupling strength, not by KK
  quantization.  Weak coupling → small mass.
- **Created in decay:** the neutron's harmonic distribution differs
  from the proton's by 1.531 m_e (F11) — a 0.04% temperature shift.
  During decay, the spectrum rearranges.  The "leftover" ripple that
  doesn't settle into the proton's equilibrium IS the neutrino.
- **Spin ½:** each harmonic is individually spin-½.  A collective
  excitation of spin-½ constituents can carry half-integer spin
  (analogous to a spinon in condensed-matter spin chains), but this
  must be demonstrated rather than assumed.

#### Connection to existing work

This direction dovetails with R21 Track 4 (mode-mode coupling from
curvature).  The same coupling coefficients that determine the
proton's harmonic spectrum also determine the neutrino's effective
mass.  The phonon calculation is a natural extension of R21.

#### Concrete steps

1. Write down the Hamiltonian for N coupled harmonics on the curved
   torus, using the curvature coupling from R21 Track 1.
2. Compute the coupling matrix elements between adjacent harmonics.
3. Linearize around the proton's equilibrium spectrum to find the
   low-energy excitation spectrum (small oscillations = phonons).
4. Check whether the lowest collective mode has spin ½ and mass at
   the sub-eV scale.
5. Check whether three distinct phonon branches exist (which could
   map to three neutrino flavors).

#### What could go wrong

The spin-½ requirement is the main risk.  Phonons in ordinary
condensed matter are bosonic (integer spin).  Getting fermionic
collective excitations requires specific symmetry-breaking patterns
(as in fractional quantum Hall states or spin liquids).  The harmonic
condensate may or may not have the right structure.


---

### Direction B: Near-degeneracy oscillation modes

**Priority: high.  Natural connection to neutrino oscillations.**

#### Concept

F16 discovered that pairs of high-energy modes on Ma_e
are nearly degenerate, with energy splittings at the sub-eV scale:

| Mode range | Closest pair | ΔE (eV) |
|---|---|---|
| E < 20 m_e | (0,+6) – (−6,−1) | 1.7 |
| E < 100 m_e | (+3,−46) – (−46,−15) | 0.29 |

The irrational shear s₁₂ ≈ 0.165 guarantees that mode energies never
exactly coincide — there are always tiny residual splittings.  These
splittings are not fine-tuned; they emerge naturally from the geometry.

#### Application to the neutrino

During neutron decay, some of the excess harmonic energy may populate
a **superposition of two nearly-degenerate modes**.  These two modes
have slightly different energies E₁ and E₂, so their relative phase
oscillates at frequency (E₁ − E₂)/ℏ.

This is the same mathematical structure as **neutrino oscillations**.
In the Standard Model, neutrinos oscillate because flavor eigenstates
are superpositions of mass eigenstates with slightly different masses.
Here:

- The "mass eigenstates" are the individual KK modes (each at energy
  ~50 m_e, in the pair found at E < 100 m_e).
- The "flavor eigenstate" is the specific superposition produced in
  the decay process.
- The oscillation frequency is set by the mode splitting ΔE, which
  plays the role of Δm².

If the decay process preferentially populates specific superpositions,
and if these superpositions are what couple to other particles (through
mode-mode interactions), then the effective "mass" seen externally
could be related to ΔE rather than to the constituent mode masses.

#### Why this is attractive

- **Neutrino oscillations emerge naturally** from the geometry of
  the material sheet — no new physics needed beyond the existing mode spectrum.
- **Δm² values come from the torus parameters** (r, s₁₂, L₁).
  Different near-degeneracy pairs give different ΔE values, which
  could match the atmospheric and solar Δm² scales
  (Δm²_atm ≈ 2.5 × 10⁻³ eV², Δm²_sol ≈ 7.5 × 10⁻⁵ eV²).
- **Three flavors from three pairs.**  If three independent
  near-degeneracy classes exist on Ma_e, each
  corresponds to a neutrino flavor.

#### The challenge

The individual modes in each pair have energies ~50 m_e, not sub-eV.
In standard quantum mechanics, the invariant mass of a two-mode
superposition is not ΔE — it oscillates between E₁ and E₂.  The
"rest mass = ΔE" identification would require a non-standard
relationship between the beat pattern and the effective particle mass.

This distinction — the particle IS the beat, not the carrier waves —
is unusual but not unprecedented.  In optics, a beat frequency between
two sources has a well-defined energy ΔE even though the individual
photons have much higher energy.  Whether this analogy extends to
massive particles on the material sheet requires careful analysis of the invariant mass
of the propagating superposition.

#### Concrete steps

1. Systematically compute all near-degeneracy pairs on Ma_e
   up to E ~ 200 m_e.
2. Compute ΔE values and check against known Δm² ratios.
3. Determine whether the decay process preferentially populates
   specific superpositions (selection rules from mode-mode coupling).
4. Work out the invariant mass of the propagating interference
   pattern, as distinct from the constituent mode masses.
5. Check spin: does a beat between two spin-½ modes carry spin ½?


---

### Direction C: Trapped non-equilibrium configuration

**Priority: medium.**

#### Concept

During decay, harmonic energy is released rapidly.  The redistribution
of this energy among modes is not instantaneous — it requires
mode-mode coupling, which is weak (the torus is nearly flat).  Some
energy may get "stranded" in a configuration that is:

- Not an eigenmode of the material sheet (so it's not a stable KK state)
- Not the zero mode (so it's not a photon)
- Slowly decaying toward one or the other, but with a decay rate so
  slow that it propagates macroscopic distances before converting

#### Analogy

A metastable state in a double-well potential.  The energy sits in a
local minimum, not the global minimum (photon).  It slowly tunnels
toward the photon state, but the tunneling rate is exponentially
suppressed by the barrier height — which is set by the gap between
zero and the first KK mode (245 keV).

#### Application to the neutrino

The decay ejects some harmonic energy in a non-eigenmode configuration.
This configuration "wants" to become photons (zero mode) but can't
fully convert because:

- It originated from modes with specific material structure (winding
  numbers, angular momentum in the material dimensions).
- Topological conservation (winding number is a topological invariant)
  prevents clean conversion.
- The mismatch between its structure and the zero mode creates a
  tunneling barrier.

The effective mass of this trapped state is related to the curvature
of the potential barrier — small if the barrier is broad and shallow.
The state propagates through 3D carrying energy and momentum, slowly
leaking into photons over cosmological distances.

#### Why this is attractive

It explains why neutrinos are created in decays (they're a
non-equilibrium phenomenon, not a pre-existing particle) and why they
interact weakly (the coupling to other modes IS the same weak
mode-mode coupling that makes the configuration metastable).

#### Concrete steps

1. Model the decay process dynamically: how does energy redistribute
   among modes when a fundamental escapes?
2. Identify whether there are topological obstructions to full
   thermalization (i.e., are there selection rules that prevent
   complete redistribution to the zero mode?).
3. Compute the lifetime of non-eigenmode configurations on the curved
   torus.
4. Check whether the metastable state has spin ½ and charge 0.


---

### Direction D: Moduli (shape) oscillation

**Priority: medium-low.  Spin ½ is the main obstacle.**

#### Concept

The torus shape is defined by parameters: side lengths L₁ and L₂,
shear s₁₂, and aspect ratio r = L₂/L₁.  These are normally treated
as fixed constants.  But quantum mechanically, they can fluctuate.

A small oscillation of s₁₂ (the shear parameter) would propagate
through 3D as a scalar wave with mass set by the geometric stiffness.
R18 computed a stiffness value: κ = ε₀E₀²/(2R).  The mass of the
moduli fluctuation is m_mod ~ √(κ / kinetic_coefficient).

#### Why the neutrino?

- **Naturally uncharged:** a shape fluctuation doesn't change any
  winding number, so it carries no charge.
- **Naturally light:** if the stiffness is low (the torus shape is
  "floppy"), the fluctuation mass can be tiny.
- **On the same material sheet:** no new dimensions required — it's the geometry
  itself oscillating.

#### The spin problem

Scalar geometry fluctuations (changes to L₁, L₂, or r) have spin 0.
Tensor fluctuations have spin 2.  Getting spin ½ from a pure shape
fluctuation typically requires supersymmetry, which this model does
not invoke.

However, the material sheet has shear (s₁₂ ≈ 0.165), and a shear fluctuation
involves a cross-term between the two torus directions.  On the
embedded torus, this cross-term couples asymmetrically to the
tube-ring structure.  Whether this asymmetric coupling can produce an
effective spin-½ degree of freedom is an open question that may depend
on the details of the embedding.

#### Concrete steps

1. Write down the moduli action for the sheared material sheet — kinetic and
   potential energy terms for L₁, L₂, s₁₂.
2. Compute the mass eigenvalues of small oscillations around the
   equilibrium geometry.
3. Check whether any moduli mode has mass at the sub-eV scale.
4. Investigate whether shear fluctuations on the embedded torus can
   carry effective spin ½.


---

### Direction E: Topological defect from decay

**Priority: medium-low.  Speculative but geometrically motivated.**

#### Concept

When the electron's (1,2) winding mode escapes the neutron during beta
decay, the process of "unwinding" one fundamental from the composite
might not be clean.  The separation could leave a **topological
scar** — a phase defect in the remaining field configuration on the material sheet.

On the material sheet, topological defects include:
- **Vortices** (point-like phase singularities where the field phase
  winds by 2π around a point).
- **Dislocations** (mismatches in the periodic field structure).

Vortices are topologically stable — they cannot be smoothed out
without cutting the field.  They carry quantized topological charge
and a small amount of energy.

#### Application to the neutrino

In the neutron, the (+e) and (−e) fundamentals coexist as
opposite-winding modes: (1,2) and (−1,−2).  Their winding numbers
are topological invariants.  When the (1,2) mode escapes, it must
either:

- Depart cleanly, taking its winding with it (no remnant).
- Leave behind a topological remnant — a vortex or phase discontinuity
  in the field of the remaining modes.

If a remnant is left behind, it carries energy (from the field
configuration near the defect core) and propagates in 3D.

#### Properties

- **Topological protection** means the defect can't decay into
  photons — it is stable or very long-lived.
- **Low energy:** vortex energy on the material sheet is proportional to
  ln(L/ξ) where ξ is the core size.  If the core is not much
  smaller than the torus, the energy can be small.
- **Created in decay:** produced by the topological rearrangement
  during the fundamental's escape.
- **Spin ½:** a vortex with half-integer topological charge could
  carry spin ½, but this depends on the field structure.

#### Concrete steps

1. Analyze the field topology during decay: when a (1,2) mode
   separates from a (−1,−2) mode, what field configuration remains?
2. Can the separation produce vortices or dislocations on the material sheet?
3. Compute vortex energies on Ma_e.
4. Determine the spin of a vortex/anti-vortex pair on the material sheet.


---

## 6. Comparison of directions

| Direction | Stays on same Ma_e? | Natural mass scale | Spin ½? | Ties to existing work |
|---|---|---|---|---|
| **A. Condensate phonon** | yes | Sub-eV (weak coupling) | Plausible (spinon analog) | R21 Track 4 |
| **B. Near-degeneracy beats** | yes | Sub-eV (from F16) | Open | F16, extends R20 |
| **C. Non-equilibrium state** | yes | Model-dependent | Open | Decay dynamics |
| **D. Moduli fluctuation** | yes | Depends on stiffness | Difficult | R18 |
| **E. Topological defect** | yes | Model-dependent | Possible | Decay topology |

**Recommended starting points: A and B in parallel.**

Direction A is the most physically motivated.  The proton IS a
many-body system, and many-body systems always have collective
excitations lighter than their constituents.  The central question
is whether those excitations have the right quantum numbers (spin ½,
charge 0).  The calculation ties directly into R21.

Direction B has the most elegant connection to neutrino oscillations.
The beat-frequency structure maps naturally onto the flavor/mass
eigenstate formalism of the Standard Model.  The calculation can begin
immediately using the F16 mode catalog — no new infrastructure needed.


---

## 7. The deeper point

The project's guiding principle (from the top-level README) is:
**energy and geometry are the only fundamentals.**  The electron,
proton, neutron, muon, and tau all emerge from energy (photons)
confined in geometry (the material sheet).  The neutrino should too.

Creating a separate material sheet for the neutrino (F18a) is mechanically
viable but philosophically retrograde — it introduces a new free
parameter (L_ν) for each flavor, explaining nothing.  The neutrino
should be *emergent* from the dynamics of energy on the geometry
that already exists, not a fundamental field living on its own
private surface.

All five directions above share a common requirement: **mode-mode
coupling**.  On the flat material sheet, modes are independent, the spectrum is
gapped, and there is no room for a neutrino.  On the embedded torus,
curvature couples modes together, and new phenomena appear:
collective excitations, near-degeneracy beats, non-equilibrium
configurations, shape fluctuations, topological defects.

The key missing calculation — for the neutrino and for much else —
is R21 Track 1 (eigenmodes on the curved torus) and Track 4
(mode-mode coupling coefficients).  These results feed into every
neutrino direction, alongside the quark program and the binding
mechanism.

The neutrino problem and the binding problem may be the same problem.
Both require understanding how modes interact on the embedded torus.
Solving one likely solves both.


---

## References within this project

| Study | Relevant findings |
|---|---|
| R20 F14 | Neutrino cannot be a mode on Ma_e |
| R20 F15 | Separate material sheet at ~1.5 μm experimentally allowed |
| R20 F16 | Mode splittings reach sub-eV scale naturally |
| R20 F18 | Three options: separate material sheet, geometry fluctuation, decay product |
| R20 F19–F21 | Ejected harmonics and complex geodesics ruled out |
| R20 F9, F11 | Neutron excess = 1.531 m_e; decay endpoint 0.782 MeV |
| R20 F17 | Muon/tau decay as "harmonic evaporation" — also produces neutrinos |
| R21 | Embedding curvature → mode coupling → binding, spectrum, quarks |
| R12 | Two-domain picture: flat for mass/spin, embedded for charge |
| R18 | Material-sheet stiffness κ = ε₀E₀²/(2R) |
| Q14 (INBOX) | Neutrino topology — earliest note on the problem |
| Q11 | Spin-statistics filter: only q = 1 (bosons) and q = 2 (fermions) |
