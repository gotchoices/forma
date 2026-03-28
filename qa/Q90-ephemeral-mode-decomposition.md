# Q90: Can a mode temporarily decompose into quark-like sub-modes?

**Status:** Open — speculative
**Related:**
  [Q88](Q88-phase-dependent-nuclear-force.md) (phase-dependent forces),
  R19 F24 (single-photon quarks ruled out),
  R14 F12 (three-photon linking fails),
  S3 F1 (spin = ℏ/q for (1,q) knots),
  S3 F4 (fractional charges from different a/R),
  R24 T2 (wave dynamics on embedded torus),
  R17 (radiation pressure / centrifugal force),
  R18 (torus stiffness),
  R33 (ghost mode selection)


## The idea

All studies to date treat Ma modes as stationary eigenstates on a
fixed geometry.  Particles ARE modes — they don't decompose.

But a real physical surface has dynamics.  A drum tuned to middle C
still rings at overtones when struck hard enough.  Could a particle
mode, given sufficient energy, temporarily excite the torus surface
into a pattern that decomposes into sub-modes — and could those
sub-modes look like quarks?

### Mode decomposition (the "ringing" picture)

The proton is a (1,2) standing wave on the proton sheet.  The same
2D surface supports infinitely many resonances.  A (1,6) mode winds
once around the tube and 6 times around the ring.  Three (1,6)
modes tile the same topology as one (1,2) — the ring windings
decompose as 3 × 2 = 6.

Three (1,6) sub-modes:
- Energy: ~1/3 each (path ~3× longer → E = hc/λ ~1/3) → sums to E
- Spin: ℏ/6 each → 3 × ℏ/6 = ℏ/2 (aligned) → recovers proton spin

This bookkeeping works for energy and spin.  But quarks need
fractional charge (1/3, 2/3).  In the KK formula (Q = −n₁ + n₅),
charge is always integer.  However, the WvM surface integral —
which depends on geometry, not just topology — can produce
fractional values at different effective a/R (S3 F4).

If the torus surface deforms during the excitation, each sub-mode
could see a different effective curvature and carry a different
fraction of the charge.

### The Omega baryon test case

Ω⁻: charge −1, spin 3/2, mass 1672 MeV, lifetime 8.2 × 10⁻¹¹ s.
Standard Model: three strange quarks (sss), each charge −1/3,
spin 1/2, all spins aligned.

MaSt currently cannot produce Ω⁻ as a single mode (spin 3/2
requires 3 odd tube windings → even charge; charge −1 is odd).

But as a composite of three ephemeral (1,2)-like sub-modes, each
with charge −1/3 and spin 1/2:
- Total charge: 3 × (−1/3) = −1 ✓
- Total spin: 3 × 1/2 → 3/2 (aligned) ✓
- Unstable: decays when sub-modes recombine

This requires the WvM charge mechanism (geometry-dependent,
not topological) and a time-dependent mode formalism.

### What's needed

1. A wave equation on the torus with time evolution (R24 Track 2
   started this but didn't complete it)
2. A mechanism for mode splitting — how does external energy
   drive a (1,2) fundamental into sub-harmonics?
3. A charge calculation for the transient state — does the WvM
   surface integral give 1/3 for each sub-mode?
4. Stability analysis — how quickly do the sub-modes recombine?


## The dynamic torus

The studies above treat the torus as geometrically fixed.  R17
computed the centrifugal force of the confined photon pressing on
the torus surface.  R18 computed the stiffness.  Both found
self-consistent results but R17 concluded the force balance is a
consequence of confinement, not a separate dynamic.

But what if the dynamic is real?  What if space truly is rigid,
and the radiation pressure of the photon is what holds the torus
in its shape?

### Non-uniform radiation pressure → warped torus

The photon's wave function on the torus is not uniform — it has
a sinusoidal amplitude pattern (nodes and antinodes along the
geodesic).  At each surface element dA, the radiation pressure
differs.  The balance between outward photon pressure and inward
spatial rigidity is local, not global.

The result: the torus is NOT a perfect torus of revolution.  It is
warped.  The cross-section could be elliptical rather than circular,
and the ellipticity would vary around the ring (non-uniform, tracking
the mode amplitude).  The major cross-section could also deform.

### Consequences of a warped torus

**1. New dynamics.**  A warped surface has different geodesics than
a perfect torus.  The mode frequencies shift.  Modes that "almost
work" on the perfect torus might snap into exact resonance on the
warped surface.  The self-consistent shape is the one where the
mode and the geometry are mutually compatible — a nonlinear
eigenvalue problem.

**2. Ephemeral particles.**  A surface deformation that doesn't
match any stable eigenmode is a transient excitation.  It will
radiate or dissipate.  The lifetime depends on how far the
deformation is from a stable mode — this could naturally explain
the wide range of particle lifetimes (from 10⁻²⁴ s for the
delta baryon to stable for the electron).

**3. Ghost suppression.**  The ghost mode problem (R33) is that
the flat torus has ~14,000 charged modes below 10 GeV where
nature shows ~40 particles.  A dynamic torus may act as a
low-pass filter: only modes whose radiation pressure pattern is
compatible with a self-consistent surface deformation can exist
as stable particles.  High-harmonic modes (the ghosts) would
create surface patterns that destructively interfere with
themselves — the torus can't warp into a shape that supports them.
This is the geometric analog of a cavity that only supports certain
resonant frequencies.

**4. Fractional charge from deformation.**  If the warped torus has
regions of different effective curvature, the WvM surface integral
could produce charge values that differ from the integer KK
prediction.  Localized wavepackets on different parts of the
warped surface might carry fractional charge — and these would be
the ephemeral quarks.

**5. The moduli potential.**  R37 F7 found that energy minimization
prefers r ≈ 0.5 (fat torus), but the minimum is broad.  A dynamic
torus wouldn't sit at a single r — it would oscillate around the
minimum.  The shape of the energy landscape (the moduli potential)
determines the oscillation frequencies, which are new physical
predictions.  R31 and R37 both identified the moduli potential as
the critical unknown blocking progress.  The dynamic torus makes
computing it urgent.

### Connection to existing open problems

- **The α derivation (R15, R31, R32):** α = 1/137 might be selected
  by the self-consistent warped shape, not by a flat-torus formula.
- **The ghost problem (R33):** the dynamic filter might reduce
  14,000 modes to ~40.
- **Nuclear binding (R29, R39):** the warped torus changes the
  near-field structure, potentially creating the attractive short-
  range component missing from R39.
- **Particle lifetimes (R27 F30):** the lifetime-gap correlation
  (r = −0.84) might be explained by how far each particle's mode
  is from a self-consistent deformation.
- **Three generations (R38):** the cavity bandwidth idea (Q ≈ 30
  limits which modes can capture a photon) might emerge naturally
  from the dynamic torus's frequency response.
