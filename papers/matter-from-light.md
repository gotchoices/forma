# Matter from Light and Geometry

**Status:** draft

**Paper 1 of 3.**  Paper 2: [Sub-Quantum Memory](sub-quantum-memory.md).
Paper 3: [The Nine-Dimensional Atom](atoms-from-geometry.md) (rough outline).

---

### Table of contents

| # | Section | Story beat | One-line summary |
|---|---------|------------|-----------------|
| 1 | The premise | Setup | Three axioms: energy, geometry, Maxwell. Everything else follows. |
| 2 | Why topology? | Setup | Gravity and nonlinear EM can't trap a photon. A closed surface can. |
| 3 | The flat torus | Setup | A material sheet as a resonant cavity. Standing waves, mode spectrum, the Asteroids analogy. |
| 4 | The electron | Payoff | The (1,2) mode gives spin ½, charge e, g ≈ 2 — with zero free parameters. |
| 5 | The energy gap | Payoff | A hard mass floor at 245 keV. Below it: classical EM. Above it: particles. |
| 6 | Heavier particles | Extension | Harmonics add mass without charge → proton, neutron, beta decay. |
| 7 | The neutrino crisis | Crisis | Lightest uncharged mode is 10⁵× too heavy. Charge-spin linkage blocks all fixes. |
| 8 | The MaSt architecture | Resolution | Each particle family gets its own material sheet. The crisis is resolved by architecture. |
| 9 | The neutrino resolved | Resolution | Mass-squared splittings from the neutrino sheet, matching experiment. |
| 10 | The emergent neutron | Surprise | A cross-sheet mode nobody looked for: charge 0, correct mass, natural decay. |
| 11 | The particle zoo | Payoff | Parameter-free predictions: kaon 1.2%, lambda 0.9%, eta-prime 0.3%. |
| 12 | What remains open | Honesty | The α problem, predictive horizon, ghost modes, and next steps. |

---


### Abstract

We explore a model — MaSt (Material-Space-time) — in which
all matter is electromagnetic radiation confined to material
extra dimensions.  The model begins with three axioms —
energy exists, material dimensions exist, and Maxwell's
equations govern propagation — and derives particle
properties from geometry alone.

On a single material sheet, the simplest nontrivial mode
reproduces the electron: spin ½ from the winding topology,
charge e from the shear of the lattice, and the g-factor
g ≈ 2 from the ratio of photon to fermion angular momentum.
The sheet imposes a hard mass floor at ~245 keV, below
which no material-dimension modes exist, providing a
geometric origin for the particle-creation threshold.

A structural crisis forces the architecture beyond one
sheet: the neutrino — uncharged, spin ½, and 10⁵ times
lighter than the mass floor — is impossible on any single
material sheet because a charge-spin linkage ties both
properties to the same quantum number.  The resolution is
Ma, the six-dimensional material space, composed of three
sheets (3Ma), one per stable particle family.  On this
geometry, the neutrino mass-squared splitting ratio
Δm²₃₁/Δm²₂₁ = 33.6 is reproduced exactly from a single
shear parameter.

Ma generates an emergent neutron as a cross-sheet mode
whose charge, mass, and decay products follow from the
geometry without adjustment.  With the proton aspect ratio
pinned by the neutron and muon (r_p = 8.906, σ_ep = −0.091),
the model has zero free parameters at the MeV scale and
produces parameter-free predictions for the kaon (1.2%
error), eta (0.6%), lambda (0.9%), sigma (0.3%),
eta-prime (0.3%), and phi (0.8%).

We present the model's successes, its specific failures
(tau at 5.6%, pion at 14%, Ω⁻ structurally forbidden),
and its central open problem: nothing yet selects the
electron's aspect ratio, and therefore nothing predicts the
fine-structure constant α from first principles.

---


## 1. The premise

The idea that particles are waves — not merely described by
waves, but *are* waves — is as old as quantum mechanics.

In 1924, Louis de Broglie proposed that every particle has
an associated wavelength, λ = h/p, and that the wave is not
a mathematical convenience but a physical reality.  Two years
later, Erwin Schrödinger built a wave equation to describe
these matter waves, and originally interpreted his
wavefunction as a real physical oscillation — not a
probability amplitude.  Born's statistical interpretation
prevailed, but Schrödinger spent the rest of his life
defending the physical reality of the wave.  His discovery
of *zitterbewegung* — a trembling motion at the Compton
scale, predicted by the Dirac equation — suggested that
something really is oscillating inside the electron, at a
frequency of ~10²¹ Hz and a radius of ~10⁻¹³ m.

In parallel, Theodor Kaluza (1921) and Oskar Klein (1926)
showed that adding a single compact extra dimension to
Einstein's spacetime produces electromagnetism from pure
geometry: the electromagnetic potential is the off-diagonal
component of the five-dimensional metric.  Momentum in the
compact direction appears as electric charge in four
dimensions.  The result was profound — charge and
magnetism emerged from geometry alone — but it had a gap:
KK still required pre-existing particles to carry the
momentum.  The geometry explained the *force* between
charged objects, but not the objects themselves.  And one
compact dimension gave electromagnetism but not the rest
of particle physics.

In 1997, J. G. Williamson and M. B. van der Mark united
these threads.  They proposed that the electron is a single
photon, trapped in a loop — specifically, a photon traveling
along a (1,2) torus knot, winding once around the tube for
every two circuits of the ring.  This is de Broglie's matter
wave made literal: the wave IS the particle, confined by
topology.  The zitterbewegung IS the photon circulating on
the torus.  The model reproduces spin ½ (exact, from the 1:2
winding ratio) and charge ≈ 0.91e (approximate, from the
field geometry).  It was not widely adopted, partly because
the paper left open what mechanism could confine a photon,
and partly because the charge prediction was 9% too low.

But the core claim — that spin ½ is topological, emerging
from the winding ratio — was exact.  And the idea that
matter might *be* light, shaped by geometry rather than
composed of point-like quarks, was radical enough to be
worth pushing as far as it would go.

The model described in this paper takes these ideas
seriously and extends them.  Where KK added one compact
dimension and still needed particles, MaSt goes a level
deeper: it uses a resonant *photon* as the circulating
entity — eliminating the need for pre-existing matter —
but requires two compact dimensions (a material sheet)
per particle family to support standing-wave modes.  Three
stable families (electron, neutrino, proton) on three
sheets gives 3 × 2 = 6 material dimensions, plus 3 spatial
+ 1 time = 10 total — the same dimensionality as string
theory, though at vastly larger scales (femtometers to
micrometers, not the Planck length).

We combine de Broglie's particle-as-wave with Kaluza-Klein's
geometry-as-force and WvM's topology-as-spin, and push the
synthesis from a single particle to the full spectrum.  We
state three axioms and attempt to derive everything else —
mass, charge, spin, the particle spectrum, nuclear binding —
from the geometry of material extra dimensions.


### 1.1 Three axioms

The axioms are:

1. **Energy exists** — in the form of electromagnetic
   radiation (photons).
2. **Material dimensions exist** — space has additional
   dimensions that are periodic: closed surfaces that wrap
   around on themselves.
3. **Maxwell's equations govern propagation** — the wave
   equation on these material surfaces is the starting point
   for all dynamics.

These are minimal.  No quantum mechanics is assumed (it will
emerge from the periodic boundary conditions).  No nuclear
or weak forces are assumed (they will emerge from the
geometry).  No particle masses are assumed (they will emerge
from the mode spectrum).  The axioms say only that photons
propagate on material surfaces according to Maxwell.

The framework they define is called **MaSt** —
**Ma**terial-**S**pace-**t**ime — after its three
ingredients.  Einstein fused space and time into spacetime;
MaSt adds a foundational layer beneath it.  Energy does not
merely move through spacetime — it moves through the full
Ma × S × t continuum, and what we call "matter" is energy
whose motion is confined to the material dimensions (Ma).


### 1.2 Natural units: everything reduces to energy and length

SI physics has seven independent base units: the meter,
kilogram, second, ampere, kelvin, mole, and candela.
Natural units (ℏ = c = 1) collapse them to just two:
**energy** and **length** — which are inverses of each other
(a photon's energy is inversely proportional to its
wavelength: E = ℏc/λ).

The collapse is revealing.  In SI, the vacuum's electric
permittivity ε₀ and magnetic permeability μ₀ look like
independent constants with different units and different
magnitudes.  They are not.  They are two springs of an LC
circuit.  ε₀ governs how much the vacuum resists an
electric field (electric energy density u_E = ½ε₀E²), while
1/μ₀ governs how readily it supports a magnetic field
(magnetic energy density u_B = B²/2μ₀).  In an
electromagnetic wave, energy sloshes between these two
springs — from electric to magnetic and back — just as
energy bounces between a capacitor and an inductor.

Maxwell showed that the resonant frequency of this vacuum
LC circuit is c = 1/√(ε₀μ₀): the speed of light.  Setting
c = ε₀ = 1 makes the two springs identical.  The electric
and magnetic fields acquire the same dimensions — which is
not an artifact of unit choice but a consequence of special
relativity, where E and B are already components of a
single electromagnetic field tensor F^μν.

The most dramatic casualty is **charge**.  In SI, charge is
an independent base dimension: coulombs cannot be expressed
in terms of meters, kilograms, and seconds without ε₀
doing the conversion.  Setting ε₀ = 1 eliminates that
conversion.  From Coulomb's law F = q²/r², force has
dimensions of energy/length and r² has dimensions of
length², so q² must have dimensions of energy.  Charge is
√energy.

This is not a mathematical trick.  It reflects something
physical: energy is always bilinear.  Coulomb energy
requires two charges meeting (q × q / r), just as kinetic
energy requires velocity meeting itself (½mv²).  A single
charge brings √energy to the table; two charges together
produce energy.

| SI quantity | Natural units |
|-------------|--------------|
| Time | Same dimension as length |
| Mass | Same dimension as energy |
| Charge | √energy |
| E field, B field | Same dimensions |

The three axioms take this reduction literally.  If all of
physics reduces to energy and length, and particles are
energy (photons) shaped by length (material geometry), then
the axioms — energy exists, geometry exists, Maxwell governs
— are not a subset of physics.  They may be all of it.


### 1.3 What this paper covers

Starting from the three axioms, we build a model of matter
in stages.  Each stage is motivated by what the previous
stage could not explain.  We begin with a single flat torus
and show that it produces an electron with the correct
spin, charge, and g-factor.  We then encounter a crisis —
the neutrino is structurally impossible on any single
material sheet — which forces the model into a six-
dimensional material geometry (Ma).  On this larger geometry, the neutrino is
accommodated, the neutron emerges unbidden as a cross-sheet
mode, and the model generates parameter-free predictions
for the masses of unstable particles.

At each stage we identify what works, what fails, and what
remains open.


## 2. Why topology?

A photon travels at the speed of light.  It cannot be
slowed, cannot be stopped, and cannot be turned around
without a force acting on it.  So the first question any
model of "matter from light" must answer is: what could
possibly confine a photon?

The confinement must be exact.  Protons have been stable
for at least 10³⁴ years.  Whatever traps the photon cannot
leak, cannot fluctuate, and cannot be disrupted by thermal
energy, collisions, or the passage of time.  An approximate
confinement mechanism would produce approximately stable
particles — and that is not what we observe.


### 2.1 Gravity is too weak

The most obvious candidate is gravity: a photon has energy,
energy gravitates, so perhaps a photon could form a
gravitational bound state with itself — a "geon."  The
calculation (R1) rules this out decisively.  The
gravitational self-energy of a photon with the electron's
rest energy, evaluated at the electron's Compton wavelength
(λ̄_C ≈ 3.86 × 10⁻¹³ m), is roughly 10²² times weaker than
would be needed for confinement.  Gravity is irrelevant at
the scale of particle physics.


### 2.2 Nonlinear self-trapping fails

Maxwell's equations are linear: electromagnetic waves pass
through each other without interacting.  There are no
stable lumps of electromagnetic energy in free space — no
solitons, no self-focusing, no self-trapping.  Nonlinear
extensions of electrodynamics (Born-Infeld theory, for
instance) can produce soliton-like solutions, but these
require modifying Maxwell's equations, which violates
axiom 3.


### 2.3 Topology: confinement without a force

The resolution is that the photon is not trapped *by*
anything.  It is trapped by the *shape of space itself*.

If space has compact dimensions — dimensions that wrap
around on themselves, like the surface of a cylinder or a
torus — then a photon propagating on that surface cannot
escape.  It is not confined by a force, a potential well, or
a boundary.  It simply has nowhere else to go.  The path is
closed because the space is closed.

This is exact confinement.  It requires no energy to
maintain.  It cannot leak because there is no edge to leak
through.  It is permanent because the topology of space does
not change with time (at least not at the energy scales of
particle physics).  And it is automatic: every photon on a
compact surface is confined, whether or not it "wants" to
be.

The question of confinement thus reduces to a question of
geometry: what compact surface, what shape, gives rise to
the particles we observe?


## 3. The flat torus

The simplest compact 2D surface is a flat torus — a
material sheet.  To build one, start with a rectangle and identify opposite
edges: the left edge is the same as the right edge, and the
top is the same as the bottom.  A photon traveling off the
right side reappears on the left.  One traveling off the
top reappears at the bottom.

If this sounds familiar, it is the geometry of the classic
video game *Asteroids* — a flat, unbounded space that
nevertheless wraps around on itself.


### 3.1 The geometry

The torus has three parameters:

- **L₁** — the circumference of the first loop (the
  "tube").  A photon traveling in the θ₁ direction returns
  to its starting point after traveling a distance L₁.

- **L₂** — the circumference of the second loop (the
  "ring").  Similarly for the θ₂ direction.

- **s** — the shear.  If s = 0, the two loops are
  perpendicular.  If s ≠ 0, they are tilted: the tube
  direction is no longer exactly orthogonal to the ring.
  Geometrically, the rectangle that defines the torus has
  been skewed into a parallelogram.

The aspect ratio r = L₁/L₂ is the ratio of tube to ring
circumference.  Together with the shear, it completely
specifies the shape of the torus.  The scale (how big the
torus is) is set by the particle mass, as we will see.

Crucially, the torus is **flat**: it has zero intrinsic
curvature.  A photon inside the torus travels in a straight
line through Euclidean space.  The "donut" shape is just
how we visualize the torus when we embed it in 3D — the
photon does not experience any curvature.  This matters
because it means Maxwell's equations on the torus are
exactly the same as in flat space, with periodic boundary
conditions.


### 3.2 Standing waves and the mode spectrum

A wave on the torus must satisfy a constraint: after
traveling around either loop, it must return to its starting
value.  This is the periodic boundary condition.  It means
the wave must fit a whole number of wavelengths around each
circumference.

A guitar string vibrates at discrete frequencies —
fundamental, second harmonic, third harmonic — because the
string has fixed endpoints.  The torus imposes the same
kind of discreteness, but in two dimensions simultaneously.
Each allowed vibration is labeled by two integers (n₁, n₂):
the number of wavelengths around the tube and the number
around the ring.  The pair (n₁, n₂) is called a **mode**.

The set of all allowed modes — and their corresponding
energies — is the torus's **mode spectrum**.  It is entirely
determined by the geometry (L₁, L₂, s).  Different torus
shapes produce different spectra, just as different guitar
strings produce different sets of harmonics.


### 3.3 Mode energy and mass

Einstein's E = mc² says that energy and mass are the same
thing, measured in different units.  The energy of a
standing wave on the torus is therefore the mass of the
corresponding particle.

The mode energy formula on a sheared torus is:

    E(n₁, n₂) = (ℏc/L₂) × √((n₁/r)² + (n₂ − n₁ s)²)

Each mode (n₁, n₂) has a definite energy, which is a
definite mass.  Higher mode numbers mean shorter
wavelengths, higher frequencies, and more energy — hence
heavier particles.

The geometry determines the particle spectrum.  If the torus
has the right shape, its mode energies will match the masses
of observed particles.  This is the central hypothesis:
**particles are standing waves on material extra dimensions,
and their masses are the eigenfrequencies of that geometry.**


## 4. The electron

The electron is the lightest charged particle.  It has mass
0.511 MeV, spin ½, charge −e, and a magnetic moment that
corresponds to g ≈ 2.002.  These four properties must all
emerge from the geometry.


### 4.1 The (1,2) mode

The electron corresponds to the (1,2) mode: one cycle around
the tube, two around the ring.  This is the simplest mode
with both n₁ and n₂ nonzero (modes with n₁ = 0 or n₂ = 0
are qualitatively different, as we will see in section 7).

When L₂ is set so that E(1,2) = 0.511 MeV, the torus size
is fixed at the electron's Compton wavelength — the quantum
length scale of the electron.  This is the Kaluza-Klein
Compton constraint: the mode energy equals the particle mass,
which sets the material geometry's scale.


### 4.2 Spin ½ from topology

Spin is intrinsic angular momentum.  In the standard model,
it is an abstract quantum number assigned to particles.  In
the torus model, it has a geometric origin.

A photon has spin 1: its electromagnetic field completes one
full rotation per oscillation cycle.  The (1,2) mode on the
torus winds once around the tube for every two times around
the ring.  This 1:2 ratio means the field completes only
half a rotation per ring traversal.

More precisely: the angular frequency of the photon's field
rotation is set by the tube winding (ω_tube = 2π/T_tube),
while the orbital period is set by the ring (T_ring =
2T_tube for the (1,2) path).  The angular momentum is:

    L = E / ω_orbital = E × T_ring / (2π) = E / (2 × ω_tube/(2π) × 2π) = ℏ/2

The spin-1 photon becomes a spin-½ fermion because of the
1:2 winding topology.  The result is exact — not a
perturbative approximation, not an artifact of a particular
limit.  It is a topological invariant: any continuous
deformation of the torus that preserves the 1:2 winding
ratio preserves the spin.

More generally, a (p, q) mode has spin q/(2p).  Only when
q/(2p) is a half-integer (1/2, 3/2, ...) does the mode
represent a fermion.  The simplest case is p = 1, q = 2:
spin ½.


### 4.3 Charge from shear

On an unsheared torus (s = 0), the two loops are exactly
perpendicular.  A photon's electric field oscillates
symmetrically as it winds around the surface: the positive
and negative half-cycles cancel exactly when integrated over
a full orbit.  The net far-field flux is zero.  The particle
is electrically neutral.

Shear breaks this symmetry.  When the tube is tilted
relative to the ring (s ≠ 0), the cancellation is
imperfect.  The photon's electric field no longer integrates
to zero — there is a net flux, and the mode acquires
electric charge.

The charge depends on the shear through a specific integral
over the torus surface.  The result (R19) is a clean,
dimensionless formula relating the fine-structure constant α
to the aspect ratio r and shear s:

    α = r² sin²(2πs) / (4π(2−s)² √(1/r² + (2−s)²))

For any aspect ratio r above a critical value (~0.26),
there exists a unique shear s that produces Q = e exactly.
The charge is not approximate — it is the exact solution of
a transcendental equation.  The ~9% deficit in WvM's
original calculation was an artifact of their
uniform-sphere field approximation, not a problem with the
mechanism.

Shear is energetically favorable: tilting the torus
lengthens the (1,2) geodesic, which lowers the photon's
energy, saving about 6.6% of the rest mass.  The Coulomb
self-energy of the resulting charge costs only ~0.8% of the
rest mass.  The system does not resist acquiring charge — it
welcomes it.


### 4.4 The g-factor

The g-factor measures the ratio of a particle's magnetic
moment to its spin, in units of the appropriate magneton.
For a classical spinning charged sphere, g = 1.  For the
electron, g ≈ 2.002.

In the torus model, the magnetic moment comes from the
photon's circulating current (a charged photon orbiting on
a torus is a current loop), and the spin is ℏ/2 from the
1:2 winding.  Because the photon has spin 1 but produces a
spin-½ fermion, the g-factor is:

    g = 2 × (photon spin) / (fermion spin) = 2 × 1 / (½) = 2

The leading-order result g = 2 is exact.  The anomalous
magnetic moment (g − 2 ≈ 0.002) arises in QED from
radiative corrections — loop diagrams involving virtual
photons.  These corrections have not yet been computed in
the torus framework, but the zeroth-order result matches.


### 4.5 The lightest charged fermion

An important structural result: no charged fermion lighter
than the electron can exist on the torus.

Charge requires n₁ ≠ 0 (the shear mechanism produces zero
net flux when n₁ = 0).  Spin ½ requires the winding ratio
n₁/n₂ to be an odd integer over an even integer in lowest
terms — the simplest case is 1/2.  Among all modes
satisfying both constraints, the (1,2) mode has the lowest
energy for any torus with r > 0.26.

This is a prediction, not an assumption: the electron is
the lightest charged fermion because no lighter mode on the
torus satisfies the joint requirements of nonzero charge
and half-integer spin.  The topological constraint forbids
it.


## 5. The energy gap

### 5.1 The Kaluza-Klein mass floor

The lightest nontrivial mode on Ma_e — the
(0, 1) mode, a single wavelength around the ring with no
tube winding — has energy approximately 245 keV (about half
the electron mass).  Below this energy, the mode spectrum is
empty.  There are no material-dimension excitations between
zero energy and 245 keV.

This gap is not put in by hand.  It follows directly from
the periodic boundary conditions: the shortest wavelength
that fits around the torus determines the minimum
excitation energy, and that wavelength is set by the torus
circumference, which is set by the electron mass.

The gap is called the **Kaluza-Klein mass floor**, after
Theodor Kaluza and Oskar Klein, who first studied physics
in compact extra dimensions in the 1920s.


### 5.2 Below the gap: classical electromagnetism

Below 245 keV, no material-dimension modes can be excited.
The material dimensions are invisible — there is nothing to
observe about them, no experiment that can detect them.
Photons propagate in the three ordinary spatial dimensions
according to Maxwell's equations, exactly as if the material
dimensions did not exist.

This is not an approximation.  It is a rigorous consequence
of the gap: if the material modes require a minimum energy
of 245 keV to excite, then any process occurring at lower
energies simply cannot access them.  Classical
electromagnetism — Maxwell's equations in 3D — is the exact
low-energy limit of the material-dimension theory.


### 5.3 Above the gap: the quantum world

Above 245 keV, material modes can be excited.  Energy is no
longer continuous: only specific mode energies are allowed,
and the energy of any excitation is an integer combination
of mode quanta.  Pair creation becomes possible (a photon
with enough energy can excite a charged mode and its
antimode).  The stability of matter follows from the
discreteness of the spectrum: a particle sitting at a mode
energy has no lower-energy state to decay into unless one
exists in the spectrum.

The hallmarks of quantum mechanics — discrete energy levels,
pair creation thresholds, stable ground states — all appear
as consequences of the geometry.


### 5.4 The particle-creation threshold

The energy gap provides a physical, geometric origin for the
threshold of particle creation.  Below 245 keV, the material
dimensions are inert: no modes can be excited, no particles
can be created, and physics is purely electromagnetic.
Above 245 keV, the discrete mode spectrum activates: pair
creation becomes possible, energy is quantized, and the
material dimensions become observable.

This threshold is not imposed by hand.  It is derived from
the periodic boundary conditions of a finite compact
surface — the smallest wavelength that fits around the
material sheet sets the minimum excitation energy.

Note that this is the threshold for *particle creation*, not
for quantum mechanics in general.  Quantum effects at atomic
scales (eV) — discrete spectra, entanglement,
superconductivity — arise from the spatial dimensions and
the Coulomb potential, not from material-dimension modes.
The gap separates material-mode physics (MeV) from ordinary
electromagnetism (eV and below).


## 6. Heavier particles: harmonics on the torus

The electron is the (1,2) mode.  But the torus supports an
infinite tower of higher modes — (2,4), (3,6), (4,8), and
so on — each with the same 1:2 winding ratio but higher
frequency.  These are the **harmonics** of the electron,
analogous to the overtones of a guitar string.

Like a guitar string's harmonics, which vibrate at 2×, 3×,
4× the fundamental frequency, the torus harmonics have
energies that are integer multiples of the electron mass:
E(n, 2n) = n × m_e.  The (2,4) mode has energy 2m_e, the
(3,6) mode 3m_e, and so on.


### 6.1 Harmonics are uncharged

A crucial property: the harmonics (n, 2n) with n ≥ 2 carry
**exactly zero charge**.  This follows from the same shear
integral that gives the electron its charge.  The integral
contains a factor that selects |n₁| = 1; for any higher tube
winding, the electromagnetic field oscillates too rapidly
and the positive and negative half-cycles cancel exactly
over the surface.

This means you can add harmonic energy to a particle
without changing its charge.  A composite of the (1,2)
fundamental plus any number of uncharged harmonics has
charge e (from the fundamental) and mass greater than m_e
(from the added energy).


### 6.2 The proton

The proton has the same quantum numbers as the electron —
spin ½, charge +e — but is 1836 times heavier.  In the
harmonic model, the proton is the same (1,2) fundamental
mode (providing the charge and spin) plus a tower of
uncharged harmonics whose total energy sums to m_p.

Multiple convergent harmonic series reproduce this mass.
A corrected thermal distribution with temperature T ≈ 34 m_e
(about 17 MeV) gives the right total.  A geometric series
with ratio x ≈ 0.977 also works.  The proton is, in this
picture, a "fat electron" — the same topological object
carrying a large amount of uncharged harmonic energy.

This is descriptive rather than predictive: multiple
harmonic combinations can reach 1836 m_e, and nothing in
the single-torus model selects one over another.  The model
explains the proton's quantum numbers but does not predict
its mass from first principles.  That requires the more
rigid architecture introduced in section 8, where the
proton gets its own material sheet (Ma_p) and becomes a single
fundamental mode (0,0,0,0,1,2) — not an electron dressed
in harmonics, but an independent standing wave on a
separate material surface.


### 6.3 The neutron (first pass)

The neutron is electrically neutral but otherwise resembles
the proton.  In the harmonic model, it is two opposite-
charge fundamentals — a (1,2) mode with charge +e and a
(−1,−2) mode with charge −e — plus uncharged harmonics.
The charges cancel exactly (CPT symmetry guarantees that
the conjugate mode carries exactly opposite charge).  The
total mass is slightly above m_p because the pairing adds
energy.

We will revisit the neutron more rigorously in section 10,
where the Ma geometry produces it as a single mode rather
than a composite.  But the qualitative picture — charge
cancellation from opposite-winding fundamentals, instability
from the possibility of the pair separating — carries over.


### 6.4 Beta decay

In this picture, neutron decay (n → p + e⁻ + ν̄_e) is the
escape of one of the two fundamentals.  The −e fundamental
departs as the emitted electron.  The remaining +e
fundamental, still dressed in its harmonic tower, is the
proton.  The excess harmonic energy (the neutron had
slightly more than the proton needs) is released as
kinetic energy of the decay products.

The energy budget works: m_n − m_p − m_e = 0.782 MeV, and
this is exactly the kinetic energy shared between the
electron and antineutrino.  The endpoint energy matches the
experimentally measured value.


### 6.5 Proton stability

The proton contains a single charged fundamental.  There is
nothing to annihilate, no opposite-charge partner to
separate from.  To decay, the proton would need to shed its
(1,2) fundamental — but the fundamental IS the charge, and
the charge is conserved.  No lighter particle with charge +e
and spin ½ exists on the torus (section 4.5 proved that the
electron is the lightest charged fermion).  So the proton
cannot decay: it is the ground state of the charged sector.

This explains both proton stability and neutron instability
from the same geometric principle: the topology of the
torus determines which configurations are energetically
terminal.


### 6.6 What this gets right, and what it doesn't

The harmonic model successfully explains:
- Why the proton has the same charge and spin as the
  electron despite being 1836× heavier
- Why the neutron is slightly heavier than the proton
- Why the neutron decays into exactly p + e⁻ + ν̄
- Why the proton is stable
- Why the muon and tau (which have the same charge and
  spin as the electron but higher mass) are unstable —
  they are the same fundamental carrying excess harmonic
  energy that radiates away, like a hot object cooling

What it does NOT do is predict the proton mass, select a
unique harmonic spectrum, or account for the neutrino.
Multiple harmonic combinations reach 1836 m_e, and the
model provides no principle to choose among them.  The
neutrino — uncharged, spin ½, and absurdly light — is an
even deeper problem.  The next section shows why.


## 7. The neutrino crisis

The neutrino is the ghost of the particle zoo: nearly
massless (< 0.1 eV), electrically neutral, and barely
interacting with anything.  It has spin ½, so it is a
fermion.  These three properties — light, uncharged, spin ½
— turn out to be mutually incompatible on any single
material sheet.

This is not a minor technical issue.  It is a structural
impossibility that forces the model into a fundamentally
different architecture.


### 7.1 The mass floor

The lightest uncharged mode on Ma_e is the
(0,1) mode at approximately 245 keV.  The neutrino's mass
is below 0.1 eV — a factor of more than two million too
light.

The mass floor is a direct consequence of the torus size.
The electron mass sets the torus circumference at the
Compton wavelength (~3.86 × 10⁻¹³ m).  Any mode on this
torus has energy at least ℏc/L₂ ≈ 245 keV.  There is no
way around this: making the neutrino lighter requires
making the torus larger, but the torus size is already
fixed by the electron.


### 7.2 Three failed approaches

Three increasingly creative approaches were tried over the
course of studies R23–R25.  All failed.

**Beating between high modes (R23).**  On Ma_e,
near-degenerate mode pairs exist with energy differences in
the sub-eV range — tantalizingly close to neutrino mass
splittings.  The ratio Δm²₃₁/Δm²₂₁ = 33.6 can be
reproduced by many triplets.  But a beat between two modes
is an oscillation frequency, not a rest mass.  The neutrino
is a particle with invariant mass < 0.1 eV, not a
fluctuation at the eV scale.  The beating mechanism
gives the right oscillation rate but the wrong physical
interpretation.

**Third compact dimension (R24).**  Adding a third compact
axis (extending one sheet to three dimensions) introduces
modes (0, 0, n₃) that propagate purely along the new axis.
With n₁ = n₂ = 0, these modes are automatically uncharged.
The mass-squared ratio Δm²₃₁/Δm²₂₁ depends only on integer
mode numbers, and the triplet (7, 10, 42) matches the
experimental value 33.6 to 0.03σ — a remarkable result.

But these modes have spin 0.  Modes with n₁ = n₂ = 0 have
no tube winding and therefore no angular momentum.  They
are bosons, not fermions.  The neutrino must be spin ½.

**The charge-spin linkage (R25).**  The root cause of the
failure is a structural constraint on the WvM spin
mechanism.  Both charge and spin ½ are controlled by the
same quantum number: n₁, the tube winding.

| n₁ | Charge (from shear) | Spin |
|----|---------------------|------|
| 0 | zero | integer (boson) |
| odd | nonzero | half-integer (fermion) |
| even ≥ 2 | zero | integer (boson) |

An uncharged particle requires n₁ = 0 (or even n₁, but even
n₁ ≥ 2 are also uncharged bosons).  A spin-½ fermion
requires n₁ to be odd.  These two requirements are **mutually
exclusive**.  They demand contradictory values of the same
quantum number.


### 7.3 The crisis

This is not a technical failure that might be fixed by a
cleverer calculation, a different mode assignment, or a
modest extension of the model.  The charge-spin linkage is
a mathematical fact about the sheet geometry: on any single
material sheet, the WvM spin mechanism ties fermionic spin
to tube winding, and tube winding is the same quantum
number that produces charge.  The neutrino — uncharged,
fermionic — falls in a category that the mechanism
structurally cannot produce.

Either the model is wrong, or the neutrino lives somewhere
else entirely.


## 8. The MaSt architecture

The neutrino crisis has an architectural resolution.

Instead of trying to fit all particles onto a single
material sheet, we give each stable particle family its own
sheet within a shared six-dimensional material space.  The
result is **Ma** — the material space of the MaSt framework,
composed of three material sheets (3Ma).

| Particle | Dimensions | Material sheet |
|----------|-----------|-------------|
| Electron | θ₁, θ₂ | Ma_e |
| Neutrino | θ₃, θ₄ | Ma_ν |
| Proton | θ₅, θ₆ | Ma_p |

Each mode on Ma is labeled by six integers:
(n₁, n₂, n₃, n₄, n₅, n₆).  The electron is
(1, 2, 0, 0, 0, 0) — it winds on its own sheet and is
inert on the other two.  The proton is (0, 0, 0, 0, 1, 2).
The neutrino is a mode on (θ₃, θ₄) with n₃ odd (for spin
½) and n₁ = n₅ = 0 (for zero charge).


### 8.1 How 3Ma resolves the crisis

The charge-spin linkage depended on charge and spin being
tied to the same quantum number on the same sheet.  On Ma,
they are decoupled:

- **Charge** comes from the electron sheet: Q = −n₁ + n₅.
  A mode with n₁ = 0 and n₅ = 0 is uncharged, regardless
  of what happens on the neutrino sheet.

- **Spin** on the neutrino sheet comes from n₃ (the
  neutrino tube winding).  An odd n₃ gives spin ½.  This
  has nothing to do with n₁.

The neutrino (n₁ = 0, n₃ = odd) is simultaneously uncharged
(because n₁ = n₅ = 0) and spin ½ (because n₃ is odd).  The
crisis is resolved because charge and spin now operate on
different dimensions of the material space.


### 8.2 The three scales

The three sheets of 3Ma have vastly different sizes, set by
the masses of their resident particles:

| Particle | Material sheet | Circumferences | Energy scale |
|----------|------------|----------------|-------------|
| Electron | Ma_e (θ₁, θ₂) | ~5000 fm, ~32000 fm | ~0.5 MeV |
| Neutrino | Ma_ν (θ₃, θ₄) | ~42 μm, ~200 μm | ~30 meV |
| Proton | Ma_p (θ₅, θ₆) | ~2.7 fm, ~24 fm | ~938 MeV |

The neutrino sheet is roughly a billion times larger than
Ma_p, because neutrinos are roughly a billion times
lighter.  This enormous scale separation is not a choice or
a fine-tuning — it is a direct consequence of the
energy-geometry relationship E ∝ ℏc/L.  Lighter particles
live on bigger tori.

The Ma_ν circumferences (~42–200 μm) are
macroscopic by particle physics standards.  If gravity
propagates in these material dimensions, deviations from
Newton's inverse-square law should appear at distances below
~50 μm.  Current experiments have tested gravity down to
about 50 μm without finding deviations — the Ma prediction
sits right at the edge of experimental sensitivity.


### 8.3 Cross-shear coupling

The three sheets are not perfectly independent.  The full Ma
metric can include off-diagonal terms that tilt one sheet
relative to another.  These tilts are parameterized
by **cross-shears** (σ_ep, σ_eν, σ_νp) — small angles
between the subplanes.

Cross-shears are weak (a few degrees from perpendicular),
but they have observable consequences.  The most dramatic is
the subject of section 10: a cross-shear between the
electron and proton sheets produces a new mode — the
neutron — that nobody put in and nobody expected.

With three sheets, three within-sheet shears (s₁₂, s₃₄,
s₅₆), three aspect ratios (r_e, r_ν, r_p), three
circumferences (L₂, L₄, L₆), and three cross-shears
(σ_ep, σ_eν, σ_νp), the Ma geometry has 12 parameters in
total.  How many are determined by observation is the
subject of section 12.


## 9. The neutrino resolved

With the neutrino living on its own material sheet, its properties are
determined by the geometry of that sheet.


### 9.1 Neutrino modes

Ma_ν supports a mode spectrum just like the
electron's, but at a vastly lower energy scale (meV instead
of MeV).  Three modes form the triplet that corresponds to
the three observed neutrino mass eigenstates (ν₁, ν₂, ν₃).
All three have spin ½ (from odd n₃) and zero charge (from
n₁ = n₅ = 0).


### 9.2 Mass-squared splittings

Neutrino oscillation experiments do not measure individual
masses directly.  They measure differences in the squares
of masses: Δm²₂₁ = m₂² − m₁² and Δm²₃₁ = m₃² − m₁².
The ratio R = Δm²₃₁/Δm²₂₁ is one of the best-measured
quantities in neutrino physics: R = 33.60 ± 0.90.

On Ma_ν, this ratio depends on a single
parameter: the within-sheet shear s₃₄.  The aspect ratio
r_ν cancels completely from the formula — a remarkable
algebraic simplification.  The ratio is:

    R = (3 − 2s₃₄) / (4s₃₄)

Setting R = 33.60 gives s₃₄ = 0.02199.  This is one
equation with one unknown, yielding an exact solution.  The
match to experiment is to 0.03σ.


### 9.3 Absolute masses

The individual neutrino masses depend on both s₃₄ and the
aspect ratio r_ν.  At large r_ν (≳ 5), the three masses
converge to:

    m₁ ≈ 29 meV,  m₂ ≈ 30 meV,  m₃ ≈ 58 meV

The sum Σm_ν ≈ 117 meV sits just below the current
cosmological upper bound of ~120 meV — a testable
prediction.  If the cosmological bound tightens below
~115 meV, this prediction is falsified.

The mass hierarchy is "normal ordering" (m₃ > m₂ > m₁),
consistent with the current experimental preference but not
yet definitively established.  The Ma model predicts normal
ordering as a structural consequence of the mode spectrum.


## 10. The emergent neutron

The neutron is the most remarkable output of the Ma model.
It was not designed to produce a neutron.  Ma was built
to accommodate three particles — the electron, the
neutrino, and the proton — on three separate material sheets.
The neutron appeared uninvited.


### 10.1 A mode nobody looked for

When Ma_e and Ma_p are tilted by a small
cross-shear (σ_ep ≈ −0.09), the Ma spectrum contains a
mode that lives on all three sheets simultaneously:
(0, −2, n₃_odd, n₄, 0, +2).  This mode has quantum
numbers from the electron sheet (n₂ = −2), the neutrino
sheet (n₃ odd, providing spin ½), and the proton sheet
(n₆ = +2, providing the bulk of the mass).

Its charge is Q = −n₁ + n₅ = 0 + 0 = 0.  Its spin is ½
(from the odd neutrino tube winding).  Its mass is very
close to the proton mass but slightly higher, because the
cross-sheet coupling adds energy.


### 10.2 The neutron mass pins the cross-shear

At any proton aspect ratio r_p, exactly one value of the
cross-shear σ_ep produces a neutron mode at the observed
mass difference m_n − m_p = 1.293 MeV.  This eliminates
σ_ep as a free parameter: the neutron mass determines it.

The muon provides a second constraint.  A charge −1, spin ½
mode appears at the muon mass (105.658 MeV) when r_p ≈ 8.9.
The simultaneous requirement of the correct neutron AND muon
masses pins both parameters:

    r_p = 8.906
    σ_ep = −0.0906


### 10.3 Why m_n > m_p is geometric

The neutron is heavier than the proton because a mode
spanning two tilted sheets has higher energy than a mode on
a single sheet.  This is a geometric theorem, not a
contingent fact.

In the standard model, m_n > m_p is an unexplained fact
with enormous consequences.  If the neutron were lighter
than the proton, protons would decay instead of neutrons.
Hydrogen would be unstable.  Nuclear physics — and therefore
chemistry, biology, and the universe as we know it — would
not exist.  The standard model traces the mass difference
to m_d − m_u (a free parameter) partially offset by
electromagnetic self-energy, but provides no explanation
for why the sign and magnitude come out as they do.

In the Ma model, m_n > m_p follows from the geometry:
a cross-sheet mode always has more energy than a single-
sheet mode, because the tilt adds strain.  The sign is not
accidental; it is a consequence of the cross-shear coupling
between sheets.


### 10.4 What the neutron tells us

The neutron is the first particle Ma produces that was
not put in by hand.  The model was built around three
particles (electron, neutrino, proton); the neutron emerged
as the simplest cross-sheet vibration the geometry could
support.  Its decay products (p + e⁻ + ν̄) are exactly the
three particles Ma was built around — the mode
unraveling into its constituent sheets.

That the geometry's most natural cross-sheet excitation
reproduces a known particle — with the correct charge,
spin, mass, decay products, and instability — is suggestive
evidence that Ma is not merely a bookkeeping device.
It appears to be generating physics.


## 11. The particle zoo

With r_p = 8.906 and σ_ep = −0.0906 determined by the
neutron and muon, Ma has **zero free parameters at the
MeV scale**.  The three input masses (m_e, m_ν, m_p) set
the three circumferences.  The neutron mass and muon mass
pin the remaining two parameters.  Every other mode energy
in the Ma spectrum is now a definite number — a prediction.

The question becomes: do these predicted modes correspond to
known particles?


### 11.1 Parameter-free predictions

A systematic search (R27, R28) across the Ma mode
spectrum identifies the nearest mode to each known particle,
matching by mass, charge, and spin.  The results for the
closest matches:

| Particle | Observed (MeV) | Ma mode (MeV) | Error |
|----------|---------------|---------------|-------|
| Kaon K⁺ | 493.7 | 488.0 | 1.2% |
| Kaon K⁰ | 497.6 | 503.7 | 1.2% |
| Eta η | 547.9 | 551.2 | 0.6% |
| Lambda Λ | 1115.7 | 1105.6 | 0.9% |
| Sigma Σ⁺ | 1189.4 | 1185.5 | 0.3% |
| Eta-prime η′ | 957.8 | 961.1 | 0.3% |
| Phi φ | 1019.5 | 1028.0 | 0.8% |

Seven particles, each matched to within 1.2% of their
observed mass, with zero adjustable parameters.  The
geometry is fully determined by the stable particles; the
unstable particle masses are outputs, not inputs.


### 11.2 Why most particles are ephemeral

In the Ma picture, only three particles are absolutely
stable:

- **The electron**: the lightest charged fermion.  No
  lighter mode with charge e and spin ½ exists on any material
  sheet.  It has nowhere to decay to.

- **The proton**: the lightest positively charged state on
  Ma_p.  Its charge is topologically protected.

- **The neutrino**: the lightest fermion on Ma_ν.

Every other particle is a higher mode — a more energetic
vibration of the material geometry — that can shed energy by
decaying into one of these endpoints.  The muon and tau are
"hot electrons": the same (1,2) fundamental carrying excess
energy that radiates away (muon decay is harmonic
evaporation — the extra energy escapes as neutrinos).
Pions, kaons, and other mesons are unstable harmonic
excitations: they are modes on Ma that can relax to
lower-energy configurations.

The particle zoo is not a zoo of fundamentally different
objects.  It is a **spectrum of excitations** on a single
material geometry — the same geometry that produces the
stable particles.


### 11.3 The lifetime–gap correlation

A striking pattern emerges from the data.  Among particles
that decay via the weak interaction, those whose Ma mode
energy is close to their observed mass (small "gap") tend to
live longer, while those with larger gaps decay faster.

The correlation for the 8 weakly-decaying particles is
r = −0.84, with p = 0.009 — statistically significant.

The physical interpretation: a particle whose mass happens
to sit near a natural Ma resonance is well-described by
that mode and has a long lifetime.  A particle far from any
resonance is poorly described by a single mode — it is "off
resonance" — and decays quickly because the geometry offers
no stable resting place near its mass.

This is not a complete theory of lifetimes (it does not
account for the strong/electromagnetic/weak hierarchy), but
within the weak-decay class, the gap-lifetime correlation
is robust and makes a testable prediction.


### 11.4 What doesn't work

Not every particle finds a close match.  The failures are
as informative as the successes:

- **Tau (5.6% off):** The closest mode is at 1876 MeV —
  almost exactly 2 × m_p.  The proton energy ladder has a
  structural gap at the tau mass; no single Ma mode can
  reach 1777 MeV.  This is the boundary of the single-mode
  framework.

- **Pion (14% off):** The pion is rougher than the kaon,
  possibly because it is sensitive to within-plane shear
  details or nonlinear corrections not yet included.

- **Ω⁻ baryon (no match):** Spin 3/2 requires all three
  tube windings (n₁, n₃, n₅) to be odd.  But charge
  Q = −n₁ + n₅ with both n₁ and n₅ odd is always even.
  Charge −1 with spin 3/2 is **structurally forbidden** in
  the Ma mode spectrum.  The Ω⁻ cannot be a single Ma
  mode; it must be a multi-mode composite or involve physics
  beyond the single-mode picture.

These failures are specific, informative, and falsifiable.
They are not "the model doesn't work well enough" — they
are "the model says this particular thing is impossible for
this particular geometric reason."


### 11.5 The predictive horizon

Above approximately 2 GeV, the Ma mode spectrum becomes
too dense to be discriminating.  The band spacing drops
below 5 MeV, meaning that any mass in this range can be
matched to within ~0.001% by some Ma mode — including
fictional particles.  The W boson (80.4 GeV), Z boson
(91.2 GeV), and Higgs (125 GeV) all find modes at sub-
0.001% accuracy, but so would any invented mass.

This is not a failure of the model — it is a structural
boundary.  Below ~2 GeV, the spectrum is sparse enough
that a close match is meaningful (a random mass has only
a ~5% chance of landing within 1% of a mode).  Above
~2 GeV, matches are trivially guaranteed.  Ma has a
**predictive horizon**: it makes sharp predictions in the
hadron mass range but loses discriminating power at higher
energies, where physics may require dynamics beyond the
single-mode framework.


## 12. What remains open

### 12.1 The parameter census

The Ma geometry has 12 parameters.  Here is the honest
balance sheet:

| Parameter | Description | Status |
|-----------|------------|--------|
| L₂ | Electron ring circumference | **Pinned** by m_e |
| L₄ | Neutrino ring circumference | **Pinned** by m_ν |
| L₆ | Proton ring circumference | **Pinned** by m_p |
| r_p | Proton aspect ratio (L₅/L₆) | **Pinned** at 8.906 (neutron + muon) |
| s₃₄ | Neutrino within-sheet shear | **Pinned** at 0.022 (Δm² ratio) |
| σ_ep | Electron-proton cross-shear | **Pinned** at −0.0906 (m_n − m_p) |
| s₁₂ | Electron within-sheet shear | **Constrained** by α formula (not uniquely — see 12.2) |
| s₅₆ | Proton within-sheet shear | **Constrained** by α formula (same family as s₁₂) |
| r_ν | Neutrino aspect ratio | **Weakly constrained** (r_ν ≳ 5 from mass convergence) |
| r_e | Electron aspect ratio | **Unconstrained** (invisible to MeV-scale observables) |
| σ_eν | Electron-neutrino cross-shear | **Irrelevant** (no measurable effect) |
| σ_νp | Neutrino-proton cross-shear | **Irrelevant** (no measurable effect) |

**Score:** 6 pinned, 2 constrained, 1 weakly constrained,
1 unconstrained, 2 irrelevant.

The three circumferences are not free parameters in the
usual sense — they are fixed by the three input masses
(m_e, m_ν, m_p), just as the length of a guitar string is
fixed by the pitch you want it to play.  The particle
spectrum predictions (section 11) use zero additional
parameters beyond these inputs.


### 12.2 The α problem

The R19-shear-charge formula produces a one-parameter family of
solutions: for every aspect ratio r_e above ~0.26, there is
a unique shear s₁₂ that gives α = 1/137.  The formula is
self-consistent at every point on this family — the
electron's mass, spin, charge, and g-factor are all correct
simultaneously.

The aspect ratio r_e is invisible to all MeV-scale
observables: it enters no mode energy at any precision we
can currently probe.

A partial result narrows the range.  Treating the material
sheet as an elastic membrane with isotropic surface tension,
the total energy (photon mode plus boundary) has a minimum
along the α curve at r_e ≈ 0.50 — a "fat torus" where the
ring circumference is about half the tube.  The minimum is
broad (r = 0.4 to 0.6 within 0.5% of optimal), but the
historical value r = 6.6 is 91% higher in energy and
decisively ruled out.

The remaining uncertainty is the anisotropic correction:
the actual boundary energy depends on the **moduli
potential** — the vacuum energy of the material sheet as a
function of its shape — which is not yet derivable within
the framework.  This is the same deep unknown that blocks
computing the neutrino sheet's stiffness.

The α problem is thus partially resolved (regime selected,
thin torus excluded) but not closed (precise r_e awaits the
moduli potential).  A full solution would complete the
model: if r_e is determined, then s₁₂ follows from the
charge formula, and the entire Ma geometry is fully
specified.


### 12.3 Ghost modes

A census of the Ma mode spectrum below 2 GeV (R28)
reveals approximately 900 distinct modes — roughly 20×
more than the ~40 known particles in this mass range.
These "ghost modes" are predicted vibrations of the
material geometry with definite mass, charge, and spin
that have no observed counterpart.

The ghost modes are consistent with the off-resonance
hypothesis from section 11.2.  Most observed particles
sit slightly off an Ma eigenfrequency �� they are transient
excitations, not exact modes.  The ghosts are the
eigenfrequencies themselves: most are not directly
realized as particles because producing a mode requires
a reaction that delivers exactly the right energy and
quantum numbers.  In collider experiments, most of
these modes would appear as extremely short-lived
resonances — too brief to register as distinct particles.

The mode spectrum is dominated by a rigid energy ladder
set by the proton sheet, with steps of ~52 MeV (proton
tube) and ~467 MeV (proton ring).  Every observed
particle's mass is explained by where it falls on this
ladder, not by any internal quark structure.


### 12.4 Beyond single particles

The Ma model as presented describes single-particle
properties: mass, charge, spin.  But nature is not isolated
particles — atoms exist, nuclei are stable, electrons
occupy discrete energy levels.

Extending the model to multi-body systems requires adding
the three ordinary spatial dimensions, making the full
framework Ma × S — nine dimensions.  Results (R29) are
striking: nuclei turn out to be Ma modes themselves (not
bound multi-particle states), following the scaling law
n₅ = A, n₆ = 2A (mass number A), and matching all tested
nuclei from the deuteron to iron-56 to within 1%.

Atoms, by contrast, live below the Ma energy resolution
floor (~38 keV, vs atomic binding at ~13.6 eV) and require
the spatial dimensions for their description.  Hydrogen's
ground state energy emerges from the Kaluza-Klein Coulomb
potential — the same Ma geometry that defines the
particles also generates the force between them.

The naive Kaluza-Klein boson-exchange picture initially
produced a crisis: Yukawa corrections to the hydrogen Lamb
shift exceeded observations by a factor of 10⁵.  This was
resolved not by abandoning the geometry but by recognizing
that the boson-mediation picture was the wrong intermediate
theory — nuclei are modes, not force-bound composites,
and the massive KK tower couples far more weakly than the
zero-mode (photon) channel.

These results establish a two-tier architecture: Ma
determines particle identity and nuclear composition (MeV
scale), while S (the three spatial dimensions) determines atomic binding and nuclear
stability (eV scale).  They are the subject of a companion
paper.


### 12.5 The path forward

The model's value lies in its falsifiability.  It makes
specific numerical predictions that can be compared to
experiment:

- **Neutrino mass sum:** Σm_ν ≈ 117 meV (testable by
  next-generation cosmological surveys)
- **Normal mass ordering:** m₃ > m₂ > m₁ (testable by
  JUNO, DUNE, and other oscillation experiments)
- **Particle masses:** kaon at 488 MeV, eta at 551 MeV,
  lambda at 1106 MeV, sigma at 1186 MeV, eta-prime at
  961 MeV, phi at 1028 MeV
- **Structural constraints:** no single-mode Ω⁻; tau
  cannot be a single mode at 1777 MeV
- **Predictive horizon:** the Ma spectrum becomes too
  dense above ~2 GeV to distinguish real particles from
  noise — electroweak-scale physics is outside the
  model's current reach
- **Sub-mm gravity:** deviations from Newton's law below
  ~50 μm if gravity propagates in Ma_ν

Where the model fails — tau, pion, Ω⁻ — the failures are
specific and informative, pointing to the boundary between
single-mode physics and multi-mode or nonlinear effects.
Where it succeeds — kaon, eta, lambda, sigma, eta-prime,
phi, neutron — the successes are parameter-free.

The fine-structure constant remains underived.  The ghost
mode census is incomplete.  The connection to quantum field
theory is unexplored.  But a model that begins with three
axioms and arrives at percent-level predictions for particle
masses — without adjustable parameters — has, at minimum,
earned the right to be taken seriously as a framework worth
investigating further.
