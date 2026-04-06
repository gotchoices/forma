# Charge from Energy

How a packet of electromagnetic energy becomes a charged
particle — without introducing fundamental charge.
Starting from a photon, ending with an electron, using only
topology and geometry.

**Audience:** comfortable with E and B fields, waves, and
basic vector calculus.  No quantum field theory assumed.

---

## Contents

1. [The question](#1-the-question)
2. [The torus as waveguide and polarizer](#2-the-torus-as-waveguide-and-polarizer)
3. [Charge from winding](#3-charge-from-winding)
4. [Magnetic moment from the ring](#4-magnetic-moment-from-the-ring)
5. [The defect cost](#5-the-defect-cost)
6. [Why the moment isn't exact](#6-why-the-moment-isnt-exact)
7. [Which modes carry charge?](#7-which-modes-carry-charge)
8. [The mode spectrum](#8-the-mode-spectrum)
9. [The proton sheet](#9-the-proton-sheet)
10. [Shear as embedding angle](#10-shear-as-embedding-angle)
11. [Dark particles, antimatter, and the neutrino](#11-dark-particles-antimatter-and-the-neutrino)
12. [Summary](#12-summary)

---

## 1. The question

A photon has no charge.  An electron has charge −e.

In the MaSt (Material Space) framework, an electron IS a
photon — one that has been confined to a compact 2D surface
wrapped into a torus.  The photon's energy is the electron's
mass (E = mc²).  Its topology produces the electron's charge,
spin, and magnetic moment.

But how?  A photon's E field oscillates symmetrically —
positive and negative in equal measure.  Integrate the flux
over any closed surface surrounding a free photon and you get
zero.  Gauss's law: zero flux, zero charge.

So how does confinement turn zero into −e?

The answer involves three ingredients: the **geometry** of
the torus (which selects a special polarization), the
**topology** of the winding (which creates a net flux), and
the **impedance mismatch** between the 2D sheet and the 3D
ambient lattice (which determines how much of the wave's
energy appears externally as a Coulomb field).


## 2. The torus as waveguide and polarizer

Take a flat, 2D hexagonal lattice — a sheet of tiny
hexagons, like graphene at the Planck scale.  Wrap it into
a torus by matching up opposite edges.  The result is a
closed surface with two independent directions:

- **The tube** — the small circle (minor circumference)
- **The ring** — the large circle (major circumference)

A photon confined to this surface can form standing waves.
On the flat sheet, the wave propagates diagonally across the
rectangle.  On the torus, this diagonal path spirals around
both the tube and the ring simultaneously.  The electron's
mode is (1,2): one complete cycle around the tube for every
two around the ring.

The torus is a waveguide — it constrains the photon to the
surface.  But it is also a **polarizer**.

A photon has two transverse polarization states: linear and
circular.  On a flat sheet, both are equivalent.  On a torus,
they are not.

**Linear polarization** has E oscillating sinusoidally —
positive on one half-cycle, negative on the other.  On the
torus, as the photon wraps around the tube, the positive and
negative regions map to the outer and inner faces of the
surface.  The outward flux from one face cancels the inward
flux from the other.  Gauss's law: zero net flux, zero charge.
This is a **dark mode** — it exists, it has mass, but it
carries no charge.

**Circular polarization** is different.  The E vector rotates
helically along the propagation direction, tracing a corkscrew.
The magnitude |E| is constant — it never passes through zero.
Only the direction changes.

Now here is the key geometric fact: as the photon goes once
around the tube, the torus surface normal n̂ also rotates by
exactly 2π.  If the photon's helical E rotation matches this
geometric rotation in the opposite sense, the two rotations
cancel:

<!-- E · n̂ = E₀(cos²θ + sin²θ) = E₀ -->
$$
\mathbf{E} \cdot \hat{n} = E_0(\cos^2\theta + \sin^2\theta)
= E_0
\qquad\text{(constant, always outward)}
$$

The E field points outward everywhere, at all times.  There
is no cancellation.  The Gauss's law integral is nonzero.
**The torus has selected the polarization that produces
charge.**

The geometry doesn't create charge from nothing.  It acts as
a filter: both polarization states can exist on the torus,
but only the circularly polarized one couples to the outside
world as a charge.  The linearly polarized modes are dark —
they have mass but no electromagnetic signature.

This insight comes from the WvM (Williamson-van der Mark)
model and remains central to the MaSt picture.  What GRID
adds is the deeper reason: the synchronized polarization
rotation is the field-level manifestation of a **topological
phase winding** — and it is topology, not geometry, that
ultimately quantizes the charge.


## 3. Charge from winding

In the GRID framework, every cell of the lattice carries a
**phase** — a clock hand pointing somewhere on a circle
(axiom A3).  The physical content is in the phase differences
between neighbors, not in the absolute values.

When a photon is confined to a torus and its phase winds
through a full 2π as it traverses the tube once, that
winding is a **topological defect** — a twist that cannot be
smoothed away by any continuous deformation.  It is
permanent, discrete, and integer-valued.

The winding number IS the charge.  One 2π winding = one unit
of charge.  This is GRID's charge quantization theorem,
derived from the periodicity of the phase variable (axiom
A3): θ and θ + 2π are the same state, so the total phase
change around any closed loop must be an integer multiple of
2π.  You cannot have half a winding.

| Winding through tube | Charge | Particle |
|---------------------|--------|----------|
| +1 | +e | Positron |
| −1 | −e | Electron |
| 0 | 0 | Neutrino (no winding) |
| +2 | 0 (cancels — see §7) | Dark mode |

The direction of winding determines the sign of charge.
Clockwise and counterclockwise are the only options — there
is no in-between.  **Charge polarity is wrapping direction.**

This explains a fact that is otherwise mysterious: the
electron and the proton carry exactly the same magnitude of
charge (verified experimentally to 1 part in 10²¹), even
though they live on different sheets with vastly different
sizes.  In the topological picture, charge doesn't depend on
sheet size.  It depends on winding number.  Both have one 2π
winding.  Both carry charge e.  The universality of charge is
automatic.


## 4. Magnetic moment from the ring

The electron's mode is (1,2): one winding around the tube,
two around the ring.  The tube winding produces charge (§3).
What do the ring windings produce?

As the standing wave circulates around the ring, its B field
(tangent to the torus surface) has a component along the
torus symmetry axis — the axis perpendicular to the ring
plane.  This axial component accumulates coherently as the
wave goes around, producing a net **magnetic dipole moment**
along the axis.

The number of ring windings determines the magnitude: two
ring windings give a moment of approximately 2 Bohr
magnetons — the Dirac prediction for a spin-1/2 particle.

**Spin** emerges from the ratio:

> spin = n₁ / n₂ = 1/2

One tube winding, two ring windings.  The wave function
requires two complete trips around the ring to return to its
starting value — this half-integer topology is the origin of
spin 1/2.  The electron is a fermion because its winding
ratio is 1/2, not because spin is postulated.

**An open question (Q104):** does the photon's circular
polarization *force* n₂ = 2n₁?  The helical E field
rotating at one cycle per Compton wavelength, mapped onto
the (1,2) geodesic, may produce exactly two ring oscillations
as a geometric consequence of the helix.  If so, spin = 1/2
is not an independent quantum number — it follows from the
polarization structure.  The factor of 2 ring oscillations per
Compton cycle would be a property of helical waves on tori,
not a choice.


## 5. The defect cost

The standing wave on the torus carries the particle's full
rest energy mc².  But the 2π phase winding — the topological
defect — extends into the ambient 3D lattice, which must
accommodate the twist.  This accommodation costs energy.

The cost is the **Coulomb field** — the static electric field
radiating outward from the charge.  Its energy, evaluated at
the Compton scale, is:

> E_Coulomb = αmc²

where α ≈ 1/137 is the fine-structure constant.

The ratio is exact:

> E_Coulomb / E_wave = α

Only 1/137 of the wave's energy appears externally as
Coulomb field.  The remaining 136/137 stays on the sheet,
circulating as the standing wave that constitutes the
particle's mass.  The ambient 3D lattice sees only a small
fraction of what the particle actually carries.

In the GRID framework, α is the **impedance mismatch**
between the 2D material sheet and the 3D spatial lattice.
These are two different grid fabrics — different
dimensionality, different cell structure.  Energy crosses
from one to the other at a rate determined by the junction
geometry.  Alpha IS this transmission coefficient.

The defect cost is not a geometric coincidence rate — it is
a **thermodynamic energy partition**.  Simulations (grid/
sim-impedance) confirmed this: counting geometric node
coincidences between two lattices gives the wrong scale
(~1/20, not 1/137).  The correct picture is energetic: the
lattice action (axiom A6) sets the coupling κ = 1/(4πα) ≈
1722, and the vortex energy partitions accordingly.

Alpha is not a mysterious constant attached to the particle.
It is a property of the substrate — inherited from the
junction, not generated by the particle.


## 6. Why the moment isn't exact

The electron's magnetic moment is not exactly 2 Bohr
magnetons.  It is 2.00232 — slightly too large.  The excess
is the famous **anomalous magnetic moment**:

> (g − 2)/2 = α/(2π) ≈ 0.001162

This is α again — the same impedance mismatch that creates
the Coulomb field also distorts the circulating wave.

The standing wave on the torus doesn't circulate in a perfect
(1,2) pattern.  The coupling to the ambient lattice (strength
α) creates a Coulomb field, and that field back-reacts on the
current distribution.  The wave "overshoots" slightly —
the current loop is wider than the bare topology predicts.
The correction is proportional to α, with a geometric factor
of 1/(2π) from integrating the back-reaction around the tube.

This is one of the most precisely verified predictions in all
of physics: QED (quantum electrodynamics) computes (g−2)/2
as a power series in α and matches experiment to 12 decimal
places.  GRID does not add a new calculation here — the
standard QED series IS the lattice gauge theory calculation
in the continuum limit.  But GRID gives it a physical
picture: **the anomalous moment is the back-reaction of the
defect cost on the wave that created the defect.**

The **proton** tells the same story in a different regime.
Its magnetic moment is 2.793 nuclear magnetons — far from
any simple bare prediction.  The proton lives on a sheet
~1000× smaller than the electron's, with ~1000× steeper
phase gradients per cell.  At the proton's energy scale,
the internal coupling is strong and the corrections are no
longer small perturbations — they are order-1 distortions of
the wave pattern.  Same physics, different regime:
perturbative for the electron, non-perturbative for the
proton (Q103).


## 7. Which modes carry charge?

The torus supports many standing waves, not just (1,2).
Every pair of integers (n₁, n₂) labels a mode.  Which ones
carry charge?

The answer comes from two filters:

**Filter 1: tube winding parity.**  The tube winding n₁
determines whether the mode produces a net E-field flux:

- **Odd n₁** (1, 3, 5, ...): the circularly polarized field
  pattern produces a net outward flux.  The mode carries
  charge.
- **Even n₁** (0, 2, 4, ...): the field pattern has
  alternating outward/inward regions that cancel.  The
  Gauss's law integral is zero.  The mode is dark.

This eliminates half the modes immediately.

**Filter 2: ring resonance.**  The ring must sustain an
integer number of half-wavelengths for a standing wave to
persist.  The minimum is n₂ = 1 (one half-wavelength in the
ring).  But if the ring circumference is tuned so that the
lowest resonance requires n₂ = 2, then the (1,1) mode is
**below cutoff** — it cannot resonate and is dark.

This is critical.  The (1,1) mode — with n₁ = 1 (charged)
and n₂ = 1 — would be lighter than the electron and has
never been observed.  It is the most persistent **ghost mode**
in the MaSt program, surviving five independent attempts to
eliminate it.  Ring-circumference filtering offers a geometric
solution: the ring is simply too big for a single half-
wavelength to resonate.  The first charged mode is (1,2).

If the electron sheet's ring is tuned to first resonate at
n₂ = 2, this fixes the aspect ratio: ε = L_tube/L_ring ≈ 0.5.
This value has not been established from first principles
before — it was a free parameter in earlier MaSt studies
(R46 Track 5 tests this).

There may be a deeper explanation.  Q104 asks whether the
photon's helical polarization structure *forces* n₂ = 2n₁
for all charged modes.  If so, the ring filter is redundant
for charged particles — the helicity itself selects (1,2)
over (1,1).  The ring filter would still matter for dark
modes, which have different polarization structure.


## 8. The mode spectrum

Each material sheet is a torus with two periodic dimensions.
MaSt has **three** material sheets:

- **Ma_e** — the electron sheet (~1 pm circumference)
- **Ma_ν** — the neutrino sheet (~1 μm circumference)
- **Ma_p** — the proton sheet (~1 fm circumference)

A mode on the full material space is labeled by six integers:

> (n₁, n₂, n₃, n₄, n₅, n₆)

where (n₁, n₂) are windings on Ma_e, (n₃, n₄) on Ma_ν,
and (n₅, n₆) on Ma_p.

**Mass** comes from the eigenvalue of the wave equation on
the sheet.  Higher winding numbers → shorter wavelengths →
higher frequency → more energy → more mass:

<!-- m²c⁴ = (2πℏc)² [(n₁/L₁)² + (n₂/L₂)²] -->
$$
m^2 c^4 \propto \left(\frac{n_1}{L_1}\right)^2
+ \left(\frac{n_2}{L_2}\right)^2
$$

(simplified — the full formula includes shear corrections).

**Charge** across sheets follows the winding rule:

> Q = −n₁ + n₅

The electron sheet's tube winding contributes negative charge;
the proton sheet's contributes positive charge.  The neutrino
sheet contributes nothing to charge.

| Mode | Q | Identity |
|------|---|----------|
| (1, 2, 0, 0, 0, 0) | −1 | Electron |
| (0, 0, 0, 0, 1, 2) | +1 | Proton |
| (1, 2, 0, 0, 1, 2) | 0 | Neutron (cross-sheet) |
| (0, 0, 1, 1, 0, 0) | 0 | Neutrino |

The neutron is a **cross-sheet mode** — it has nonzero
windings on both the electron and proton sheets.  Its
charges cancel: −1 + 1 = 0.

### Charge and harmonics

GRID's charge quantization theorem (grid/maxwell.md) says
Q = ne for any integer n.  The phase is periodic (2π), so
vortex windings come in integer multiples.  On the bulk
lattice, a vortex with winding n = 2 carries charge 2e.
This is topological — no restriction to n = ±1.

**Harmonics as shorter wavelengths.**  The (1,2) geodesic
has a fixed path length — one Compton wavelength for the
electron.  The photon traverses this path at c, always.
A higher harmonic does not go around the path more times
— it fits more wave cycles into the same path.

Like a guitar string: the fundamental has one half-
wavelength fitting in the string length.  The second
harmonic has two half-wavelengths in the same string.
The string doesn't vibrate faster by "going around twice"
— the wavelength halves, the frequency doubles, and the
energy doubles.  Same path, shorter wave.

The (2,4) mode fits two complete wave cycles into the
same (1,2) geodesic.  Each cycle is one 2π phase winding.
Two cycles = two windings = charge 2e.

| Mode | Cycles on geodesic | Charge | Energy | Identity |
|------|--------------------|--------|--------|----------|
| (1,2) | 1 | −1e | m_e | Electron |
| (2,4) | 2 | −2e | ~2m_e | 2 electrons (He shell) |
| (3,6) | 3 | −3e | ~3m_e | 3 electrons (Li shell) |
| (Z,2Z) | Z | −Ze | ~Zm_e | Z electrons |

This assumption is consistent with GRID topology (Q = ne)
and with the observation that atoms with Z electrons carry
charge −Ze.  It means the (Z,2Z) harmonic on Ma_e IS the
Z-electron configuration — not Z separate particles, but
one mode with Z laps on the same geodesic.

**Status:** this is a working hypothesis.  The detailed
mechanism — how each lap's CP synchronization produces
one charge quantum on a torus — is not fully resolved
(the R48 computation gives ambiguous results for n > 1
due to the torus area weighting; see R48 review).  The
hypothesis will be tested by whether the harmonic model
correctly predicts nuclear charges and atomic binding
energies (R50, R51).

**Dark modes** still exist: modes that do NOT fit the
(n, kn) harmonic pattern of the fundamental knot — modes
with winding patterns that are not integer multiples of
the fundamental — may not produce charge.  The details of
which modes are dark and which are charged at higher
harmonics remains under investigation.


## 9. The proton sheet

The electron is the (1,2) mode on Ma_e — the first
surviving charged mode after the (1,1) ghost is killed by
the waveguide filter.

The proton is the **(1,3) mode on Ma_p** — the first
surviving charged mode on the proton sheet, after the (1,1)
and (1,2) ghosts are killed by the waveguide filter at
ε_p ≈ 0.33.

| Property | Electron | Proton |
|----------|----------|--------|
| Sheet | Ma_e | Ma_p |
| Mode | (1,2) | (1,3) |
| Ghost killed | (1,1) | (1,1) and (1,2) |
| Charge | −1 (from n₁ = 1) | +1 (from n₅ = 1) |
| Spin | ½ (n₁ odd) | ½ (n₅ odd) |
| Ring windings | 2 | 3 |
| Bare moment | ~2 Bohr magnetons | ~3 nuclear magnetons |
| Measured moment | 2.00232 | 2.793 μ_N |

The same pattern on both sheets: the waveguide kills the
lowest modes, and the first surviving mode with odd tube
winding (spin ½, charged) becomes the stable particle.
The electron sheet passes n₂ ≥ 2.  The proton sheet passes
n₆ ≥ 3.  Different cutoffs, same mechanism.

**Quarks from the standing wave.**  The (1,3) mode has three
ring windings, producing three energy antinodes at 0°, 120°,
and 240° around the ring.  A high-energy probe (DIS) with
wavelength shorter than the torus resolves these three peaks
as three separate scattering centers — quarks.

Each antinode carries ~m_p/3 ≈ 313 MeV (one-third of the
proton's mass) and ~1/3 of the charge (the charge density
has three-fold symmetry on the ring).  The total charge is
+1 from the fundamental formula Q = −n₁ + n₅ = 0 + 1 = +1.
No composite charge formula needed.

Confinement is automatic: the antinodes are features of one
standing wave, not independent sub-modes.  You cannot
separate an antinode from its wave.  There is no "free quark"
because there is no free antinode.


## 10. Shear as embedding angle

The material sheet does not float freely in 3D space.  It
is embedded in the ambient lattice at a specific angle —
and this angle has physical consequences.

On the unrolled flat sheet, **shear** is the tilt of the
lattice: the rectangle becomes a parallelogram when the top
edge is offset sideways relative to the bottom.  But this
internal tilt is not an abstract deformation — it IS the
angle at which the sheet sits in the 3D ambient lattice.
The internal (x, y) tilt and the embedding angle are the
same parameter viewed from two sides:

- **From inside the sheet:** "my axes are tilted by s"
- **From the ambient lattice:** "the sheet sits at angle s
  relative to my grid"

This embedding angle determines three things:

### Matter vs antimatter

The embedding breaks the symmetry between the two winding
directions.  On an unsheared sheet (s = 0), clockwise and
counterclockwise windings have identical energy — no
preference.  On a sheared sheet (s ≠ 0):

- Mode (1,2): effective coupling ∝ (2 − s)²
- Mode (−1,2): effective coupling ∝ (2 + s)²
- CPT conjugate (−1,−2): same energy as (1,2) — **exact**

One direction is energetically cheaper.  Photons entering
the torus from the ambient lattice preferentially wind in
the cheap direction.  The result: more matter than antimatter.

The shear sign is a **geometric chirality** — a handedness
frozen into the sheet when the lattice formed.  CPT symmetry
is exact (every particle has an antiparticle of identical
mass).  But C symmetry is broken (one winding direction is
kinetically favored).  The universe makes more matter than
antimatter because nature winds with the grain.

### The impedance mismatch

The embedding angle determines how efficiently the phase
winding on the sheet couples energy into the ambient lattice.
The α(r, s) formula from R19 expresses the coupling as a
function of the embedding geometry:

<!-- α = r² √(1/r² + (2−s)²) × sin²(2πs) / (4π(2−s)²) -->
$$
\alpha = r^2 \sqrt{\frac{1}{r^2} + (2-s)^2}
\cdot \frac{\sin^2(2\pi s)}{4\pi(2-s)^2}
$$

At s = 0: sin(0) = 0, so α = 0.  No shear, no coupling, no
charge.  Any nonzero shear produces nonzero coupling.

Whether this formula **computes** α from the embedding
geometry or merely provides a **consistency condition** between
the geometry and the substrate coupling α (GRID axiom A6) is
an open question.  GRID says α is a property of the substrate
junction; the α(r, s) formula may be expressing the same
quantity from the sheet's perspective.

### The mode spectrum

Shear changes the eigenvalues of the standing waves on the
torus.  Different embedding angles produce different mass
hierarchies.  The shear enters the mass formula through the
effective quantum number q_eff = n₂ − s · n₁, which shifts
the mode frequencies.


## 11. Dark particles, antimatter, and the neutrino

The torus supports far more modes than just the charged ones.
Most standing waves have even tube winding (n₁ = 0, 2, 4, ...)
or fall below the ring cutoff — they carry mass but no
charge.  These are **ghost modes** (also called dark modes).

Below 2 GeV, there are roughly 900 ghost modes on the three
material sheets, outnumbering known charged particles ~20 to 1.
They interact gravitationally (they have mass) but not
electromagnetically (they have no Coulomb field).  Their
predicted mass-weighted ratio brackets the observed dark-to-
visible ratio of 5.4.  Ghost modes are a leading candidate
for dark matter within the MaSt framework (R42, Q94).

**The neutrino** is a special case.  It lives on Ma_ν — the
largest sheet, with circumference ~10²⁹ Planck lengths.  It
has mass (a standing wave circulates) but no charge.  One
hypothesis (Q102): the neutrino sheet is too large for
charge.  The 2π phase winding, spread over 10²⁹ cells, has
a phase gradient per cell below the lattice's resolution
threshold.  The winding exists mathematically but is
physically undetectable.  If so, neutrino neutrality is a
consequence of sheet size, not a separate postulate.

**Antimatter** (§10) arises from the opposite winding
direction.  Every charged mode has a CPT conjugate with
the same mass and opposite charge.  The shear chirality
of the embedding makes one direction kinetically favored,
explaining the matter/antimatter asymmetry.  Annihilation
is topological cancellation: when opposite windings meet,
they unwind each other, releasing the trapped photon energy
back into free propagation.

**Compound particles** like the neutron are cross-sheet
modes — simultaneous windings on Ma_e and Ma_p whose charges
cancel.  Some observed particles may be compound resonances
involving multiple sheets rather than single-sheet modes.


## 12. Summary

### The recipe

How a confined photon produces each particle property:

| Property | What determines it | Rule | Example |
|----------|--------------------|------|---------|
| **Charge** | Wave cycles on geodesic | Q = ne: each 2π cycle on the knot path contributes ±e.  The (Z,2Z) harmonic has Z cycles → charge Ze. | 1 cycle = ±e.  4 cycles = ±4e (beryllium shell). |
| **Charge sign** | Winding direction | Clockwise vs counterclockwise on the tube | Direction set by shear chirality |
| **Charge magnitude** | α (impedance mismatch) | e = √(4πα); same for all charged particles on all sheets | α ≈ 1/137 → e ≈ 0.303 (natural units) |
| **Mass** | Mode eigenvalue | E² ∝ (n_tube/L_tube)² + (n_ring/L_ring)² | Electron (1,2): 0.511 MeV.  Proton (1,3): 938.3 MeV. |
| **Spin** | Tube winding parity | Odd n_tube → spin ½ (fermion).  Even → spin 0 or 1 (boson). | n₁=1 (odd) → ½.  n₁=2 (even) → 0. |
| **Magnetic moment** | Ring windings | Bare moment ∝ n_ring (number of ring windings) | Electron: n₂=2 → ~2μ_B.  Proton: n₆=3 → ~3μ_N. |
| **Anomalous moment** | Defect cost back-reaction | Leading correction = α/(2π) ≈ 0.00116 | Electron: 2.00232.  Proton: 2.793 (non-perturbative). |
| **Dark/charged** | Winding pattern | Harmonics of fundamental knot (n, kn) → charged.  Non-harmonic patterns → dark (under investigation). | (2,4) = 2 laps of (1,2) → charged.  Non-knot modes → dark. |
| **Mode selection** | Waveguide cutoff | Ring winding must exceed tube/ε for the mode to propagate | ε_e ≈ 0.65 kills (1,1), passes (1,2) |
| **Quarks** | Ring antinodes | n_ring = 3 → three antinodes at 120° = three quarks | Proton (1,3): 3 peaks, each ~313 MeV |
| **Confinement** | Antinodes ≠ modes | Peaks of one wave cannot separate — no free quarks | Automatic for (1,3); no extra mechanism |
| **Matter/antimatter** | Shear chirality | Embedding angle breaks CW/CCW symmetry; one direction is cheaper | CPT exact (equal masses); C broken (unequal rates) |
| **Neutrino neutrality** | Sheet size | Phase gradient too gentle for lattice to detect (Q102) | Ma_ν circumference ~10²⁹ L |

### The charge rule

**Each wave cycle on the geodesic contributes one quantum
of charge.**

GRID says Q = ne — charge is the winding number times the
elementary charge.  On a torus, the (1,2) or (1,3) knot is
the fundamental geodesic.  Higher harmonics fit more wave
cycles into the same path — shorter wavelength, higher
frequency, higher energy.  Each cycle is one complete 2π
phase winding, one unit of charge.

This is how atoms carry charge −Ze from a single mode on
the electron sheet, and how nuclei carry charge +Ze from
a single mode on the proton sheet.  The charge is additive
because the cycles are additive — and quantized because
each cycle is a complete 2π winding (no fractional cycles,
because the phase is periodic).

One photon.  One topology.  One α.

The photon carries zero charge in free space.  Confine it
to a torus, and the geometry selects a circular polarization
whose winding produces a net E-field flux — charge.  The
winding number quantizes the charge.  The impedance mismatch
between the sheet and the ambient lattice determines how
much energy appears externally as Coulomb field.  The same
mismatch back-reacts on the wave, producing the anomalous
magnetic moment.

There is no fundamental charge.  There is energy, there is
topology, and there is the junction between two grid fabrics.
What we call charge is how they combine to produce a net
E-field flux from a compact surface.

---

## References

- WvM paper: [`WvM.pdf`](WvM.pdf),
  summary: [`WvM-summary.md`](WvM-summary.md)
- GRID foundations: [`grid/foundations.md`](../grid/foundations.md)
- Maxwell derivation: [`grid/maxwell.md`](../grid/maxwell.md)
- Alpha primer: [`alpha-in-grid.md`](alpha-in-grid.md)
- Physics from fabric: [`physics-from-fabric.md`](physics-from-fabric.md)
- Defect cost analysis: [`grid/sim-impedance/`](../grid/sim-impedance/)
- Shear-induced charge: R19 findings
  ([`studies/R19-shear-charge/`](../studies/R19-shear-charge/))
- Electron filter: R46
  ([`studies/R46-electron-filter/`](../studies/R46-electron-filter/))
- Proton filter: R47
  ([`studies/R47-proton-filter/`](../studies/R47-proton-filter/))
- Open questions:
  [Q102](../qa/Q102-neutrino-neutrality-from-sheet-size.md) (neutrino neutrality),
  [Q103](../qa/Q103-anomalous-magnetic-moment-from-defect-cost.md) (anomalous moment),
  [Q104](../qa/Q104-helicity-forces-n2.md) (helicity → n₂)
