# Q90: Quarks as emergent sub-modes on the material sheet

**Status:** Open — hypothesis (quantifiable)
**Related:**
  [Q26](Q26-hadrons-photon-knots.md) (earlier multi-photon attempt — failed),
  [Q85](Q85-harmonic-ladder-and-threshold.md) (energy storage and wavepackets),
  [Q95](Q95-strong-force-as-internal-em.md) (strong force as internal EM coupling),
  R14 F12 (three-photon linking fails),
  R19 F24 (single-photon KK charge always integer),
  S3 F1 (spin = ℏ/q for (1,q) knots),
  S3 F4 (fractional charges from different a/R),
  R24 T2 (wave dynamics on embedded torus),
  R17 (radiation pressure / centrifugal force),
  R18 (torus stiffness),
  R33 (ghost mode selection),
  R40 (dynamic torus — the computational route)

---


## 1. The problem with "we don't need quarks"

MaSt treats particles as standing-wave eigenmodes on compact
material sheets.  The proton is a (1,2) mode on Ma_p — a
single photon of energy m_p c² confined to one torus.  There
are no constituent particles inside it.

This is conceptually clean, but it fails to engage with fifty
years of experimental evidence:

- Deep inelastic scattering sees three point-like scattering
  centers inside the proton.
- Jets in e⁺e⁻ annihilation match quark fragmentation models.
- Baryon spectroscopy (Δ, Ω⁻, Λ, …) is organized by SU(3)
  flavor symmetry, which requires three-valued internal
  degrees of freedom.
- The entire Standard Model of strong interactions (QCD) is
  built on quarks and gluons as real dynamical fields.

Saying "quarks are not needed" is not an answer.  MaSt must
explain **what the experiments actually see** — and why the
quark model works so well — even if quarks are not
fundamental.


## 2. Earlier attempts and what failed

**Q26: Three-photon knots.**  The first attempt: three
separate photons topologically linked on the compact surface,
each contributing fractional charge and acting as one "quark."
R14 F12 found this fails — three-photon linking on a shared
geometry does not produce the required quantum numbers.

**R19 F24: Single-photon fractional KK charge.**  The
Kaluza-Klein charge formula Q = −n₁ + n₅ is always an
integer for any set of winding numbers.  A single photon on a
fixed torus geometry cannot carry 1/3 or 2/3 charge through
the topological (KK) mechanism.

These ruled out the two most obvious routes: quarks as
separate photons, and quarks as fixed-geometry modes with
fractional topological charge.


## 3. The hypothesis: quarks as transient sub-modes

The proton is a (1,2) eigenmode — one tube winding, two ring
windings.  This is the stable standing wave.  But the same
torus surface supports infinitely many resonances.  When
sufficient energy is deposited (via a hard collision, or when
the proton is probed faster than its internal timescale),
the standing wave can **momentarily redistribute into
sub-modes**.

Three (1,6) sub-modes tile the same topology as one (1,2):
the ring windings decompose as 3 × 2 = 6.  Each sub-mode
winds once around the tube and six times around the ring,
occupying roughly one-third of the ring circumference.

This is not a decomposition into separate objects.  The
proton's energy briefly redistributes across the same sheet,
creating three localized excitations that behave as
independent scattering centers for fast-enough probes.


### 3.1 Energy: the constituent quark mass

Each sub-mode carries ~m_p / 3 ≈ 313 MeV.  This is exactly
the **constituent quark mass** from nuclear physics — the
effective mass quarks carry inside a hadron.

In QCD, the 313 MeV comes from chiral symmetry breaking and
gluon field energy dressing a nearly massless "current quark."
In MaSt, it comes from dividing one mode's energy equally
among three sub-modes.  The agreement is not a coincidence to
be dismissed — it is the same physical energy partition seen
from two different frameworks.


### 3.2 Spin

S3 F1 found that spin scales as ℏ/q for a (1,q) torus knot:
a (1,2) knot gives spin ½, a (1,3) gives spin 1/3, a (1,6)
gives spin 1/6.

Three (1,6) sub-modes, spins aligned:

    3 × ℏ/6 = ℏ/2

This recovers the proton's spin ½.


### 3.3 Charge: the critical open calculation

The proton's charge (+1) must partition as +2/3, +2/3, −1/3
to match the standard uud assignment.

The KK route fails — topological charge is always integer
(§2).  But the **WvM surface integral**, which depends on
local curvature rather than global topology, can produce
non-integer values at different effective aspect ratios
(S3 F4).

If the torus surface deforms during the excitation (see §8),
each sub-mode would see a different local curvature.  The
WvM integral could yield a different fractional charge for
each.  Whether this actually produces the 2/3 and −1/3 values
is the most important open calculation in this hypothesis.

**The shear mechanism (R19) may change the picture.**  R19
showed that charge arises from a geometric shear deformation
of the sheet.  S3's null result (only (1,2) produces charge
via Frenet transport) used a different polarization transport
rule.  Whether shear on a (1,6) geodesic yields fractional
charge has not been computed.


## 4. The phase-offset interpretation

There is a simpler way to frame multi-traversal geodesics.
The electron's (1,2) mode is ½ phase-shifted after one tube
traversal — the wave function flips sign, requiring two full
traversals to return to its starting configuration.  This
half-integer topology is the origin of spin ½.

Extending the pattern: a geodesic that is 1/3 phase-shifted
per traversal needs three trips to close.  This is a (1,3)
torus knot.  S3 F1 found it gives spin 1/3 — not a known
free-particle spin, but quarks are never free.

| Phase offset | Trips to close | Knot  | Spin | Charge? |
|--------------|----------------|-------|------|---------|
| 1/2          | 2              | (1,2) | ½    | 1 (electron) |
| 1/3          | 3              | (1,3) | 1/3  | 1/3?    |

If the 1/3 phase offset → 1/3 charge connection holds, it
would link fractional charge to fractional spin through the
same geometric mechanism — the number of traversals needed
to close the path.

Confinement then has a topological explanation: a (1,3) mode
cannot propagate freely because its wave function never closes
in a single traversal.  It must always be bound with partners
whose phase offsets sum to an integer (e.g., three quarks with
offsets 1/3 + 1/3 + 1/3 = 1).


## 5. Timescales and the ephemeral quark

### 5.1 Traversal time

One traversal of the proton's (1,2) geodesic:

    T_proton = λ_C(proton) / c ≈ 1.32 fm / c ≈ 4.4 × 10⁻²⁴ s

The (1,6) sub-mode geodesic is ~3× longer:

    T_quark ≈ 1.3 × 10⁻²³ s

For comparison:

| Particle   | Lifetime           | Traversals |
|------------|--------------------|------------|
| Δ baryon   | 5.6 × 10⁻²⁴ s     | ~1–2       |
| ρ meson    | 4.5 × 10⁻²⁴ s     | ~1         |
| Proton     | stable             | ∞          |

The shortest-lived hadrons survive about one traversal.  They
are the broadest resonances in the particle zoo (Γ ~ 100–150
MeV width) — barely particles, more like lumps in scattering
cross-sections.


### 5.2 Quality factor and lifetime

A standing wave needs multiple traversals to establish itself
through constructive interference.  The number of traversals
is roughly the quality factor Q of the resonance:

    Q = mass / width = m / Γ

- Q = 1–2: broad resonance, barely a particle (the Δ)
- Q ≈ 10: recognizable resonance
- Q → ∞: stable particle (the proton, the electron)

A (1,6) sub-mode has the "wrong" winding numbers for a stable
eigenmode — the (1,2) geometry doesn't support it.  After one
traversal, the wave picks up a phase error (1/3 off from
closing, in the phase-offset picture).  After three traversals
it closes, but the torus geometry has been fighting it —
trying to re-establish the (1,2) eigenmode.

The sub-mode's lifetime is set by how quickly energy
redistributes back into the (1,2) standing wave: the
**ring-down time** of the cavity.  If the cavity strongly
favors (1,2), the sub-modes last only a few traversals before
the eigenmode reasserts itself.


## 6. Confinement as destructive interference

In QCD, confinement is enforced by the color force — the
potential energy between quarks grows linearly with distance,
making isolation impossible.  This works but does not explain
*why* the force has this property.

In MaSt, confinement has a geometric explanation.

At **short times** (shorter than one traversal), the sub-mode
hasn't tried to close.  It doesn't "know" its winding numbers
are wrong.  It looks like a localized excitation with definite
momentum and charge — a free particle.

At **longer times** (multiple traversals), destructive
interference kills the sub-mode.  The energy reorganizes back
into the stable (1,2) eigenmode.  Confinement is not a
force — it is the torus geometry rejecting modes that cannot
sustain constructive interference.

**This is asymptotic freedom.**  In QCD, quarks behave as
free particles at high energies (short distances) and become
confined at low energies (long distances).  In MaSt, this
maps directly onto the traversal timescale:

- **Probe faster than T_quark** → catches the sub-mode
  mid-traversal → sees a "free quark"
- **Probe slower than T_quark** → the sub-mode has already
  rung down → sees only the proton eigenmode

Deep inelastic scattering catches quarks mid-traversal,
before the geometry has a chance to reassert itself.  That is
why quarks are "seen" but never isolated.


## 7. The Omega baryon test case

Ω⁻: charge −1, spin 3/2, mass 1672 MeV, lifetime
8.2 × 10⁻¹¹ s.  Standard Model: three strange quarks (sss),
each charge −1/3, spin 1/2, all spins aligned.

MaSt currently cannot produce Ω⁻ as a single eigenmode
(spin 3/2 requires 3 odd tube windings → even charge;
charge −1 is odd).

But as a composite of three ephemeral sub-modes, each with
charge −1/3 and spin 1/2:

- Total charge: 3 × (−1/3) = −1  ✓
- Total spin: 3 × 1/2 → 3/2 (aligned)  ✓
- Unstable: decays when sub-modes recombine  ✓
  (lifetime ≫ T_quark → high Q → long-lived resonance)

This requires the WvM charge mechanism (geometry-dependent,
not topological) and a time-dependent mode formalism.  The
Omega is a strong test case because it is impossible as a
single MaSt eigenmode but natural as a three-sub-mode state.


## 8. The dynamic torus

The analysis above treats the torus as geometrically fixed.
A richer picture emerges if the torus surface itself responds
to the energy distribution — warping locally under radiation
pressure.

R17 computed the centrifugal force of the confined photon
pressing on the torus surface.  R18 computed the stiffness.
Both found self-consistent results but R17 concluded the
force balance is a consequence of confinement, not a separate
dynamic.  R40 is exploring whether the dynamic is real.


### 8.1 Warped geometry and fractional charge

The photon's wave function on the torus has a sinusoidal
amplitude pattern (nodes and antinodes along the geodesic).
Radiation pressure differs at each surface element dA.  The
balance between outward photon pressure and inward spatial
rigidity is local, not global.

The result: the torus is not a perfect torus of revolution.
It is **warped**.  The cross-section varies around the ring,
tracking the mode amplitude.  If sub-modes see different
local curvatures, the WvM charge integral could yield
fractional values — one route to the 2/3 and −1/3 charges.


### 8.2 Consequences for the particle spectrum

- **Ghost suppression (R33):**  The flat torus has ~14,000
  charged modes below 10 GeV where nature shows ~40 particles.
  A dynamic torus may act as a low-pass filter: only modes
  whose radiation pressure pattern is compatible with a
  self-consistent surface shape can exist as stable particles.
- **Particle lifetimes (R27 F30):**  The lifetime-gap
  correlation (r = −0.84) might be explained by how far each
  particle's mode is from a self-consistent deformation.
- **Three generations (R38):**  The cavity bandwidth idea
  (Q ≈ 30 limits which modes can capture a photon) might
  emerge naturally from the dynamic torus's frequency response.


## 9. How this differs from "we don't need quarks"

The old MaSt stance said quarks are an artifact of applying
the wrong model (point particles) to what is actually a
single-mode system.  This was logically consistent but
dismissive of powerful experimental evidence.

The new hypothesis says **quarks are real but emergent**:

| Question | Old answer | New answer |
|----------|-----------|------------|
| Are quarks real? | No — artifacts | Yes — transient sub-modes |
| Why three? | N/A | (1,2) → 3 × (1,6) tiling of the ring |
| Why 1/3, 2/3 charge? | N/A | WvM on locally deformed geometry (open calc) |
| Why confined? | N/A | Destructive interference for non-closing paths |
| Why free at high E? | N/A | Probe faster than traversal timescale |
| What is 313 MeV? | N/A | m_p / 3 energy partition per sub-mode |
| What about the Ω⁻? | Can't model it | Three sub-modes with aligned spin |

The shift is from "quarks are unnecessary" to "quarks are
what eigenmode decomposition looks like from the inside."
This is a stronger position: it accounts for the experimental
evidence rather than denying it, while maintaining MaSt's
core claim that all particles are electromagnetic energy
confined to compact geometry.


## 10. The baryon spectrum as decomposition spectrum

The Standard Model catalogs hundreds of baryons — the Δ, Σ,
Λ, Ξ, Ω families and their excited resonances (Δ(1232),
Δ(1600), Δ(1620), …).  These arise from combinatorics: 6
quark flavors taken 3 at a time, with different spin
alignments and orbital angular momentum states.

In MaSt, this richness comes from the fact that a standing
wave on a 2D surface does not have a unique decomposition —
it has many.  Every valid way of redistributing the energy
among sub-modes is a candidate baryon state.


### 10.1 Multiple decomposition channels

The proton's (1,2) mode on Ma_p can redistribute in many
ways.  Each decomposition defines a different transient
particle:

**Equal sub-modes (the simplest baryons):**
Three (1,6) sub-modes — the ground-state decomposition
analyzed in §3.  Energy splits equally (~313 MeV each),
spins are ℏ/6 each.  This is the proton/neutron internal
structure seen in deep inelastic scattering.

**Unequal winding numbers (quark "flavors"):**
The ring windings can be partitioned unevenly.  Instead of
6 = 2+2+2 (three identical sub-modes), consider 6 = 1+2+3:
sub-modes with windings (1,3), (1,4), and (1,5).  Each has a
different path length, therefore a different energy.  A
heavier sub-mode plays the role of a strange or charm quark —
"flavor" is not a fundamental label but a statement about how
the energy was partitioned.

This reframes the quark mass hierarchy.  The current quark
masses (u ≈ 2 MeV, d ≈ 5 MeV, s ≈ 95 MeV, c ≈ 1.3 GeV,
b ≈ 4.2 GeV, t ≈ 173 GeV) would correspond to sub-modes
with progressively higher winding numbers on progressively
stiffer sheets — each winding number selecting a different
fraction of the parent mode's energy.

**Different spin configurations:**
The same three sub-modes can have their spins aligned or
anti-aligned.  This is the distinction between the proton
(mixed alignment, spin ½) and the Δ baryon (all aligned,
spin 3/2) — same "quarks," different spin arrangement.  In
MaSt, these are the same sub-mode set with different phase
relationships between their oscillating fields.

**Cross-sheet sub-modes:**
Energy can redistribute across multiple material sheets
simultaneously.  The neutron already works this way (R27
F15–F18: a three-sheet mode spanning Ma_e, Ma_ν, and Ma_p).
Sub-modes that involve different sheets see different torus
geometries, giving them different effective masses and
charges — a natural origin for the flavor structure that QCD
must postulate.

**Higher-order decompositions:**
Nothing restricts the tiling to three sub-modes.  Four
sub-modes would be a tetraquark; five would be a pentaquark.
Both have been observed experimentally (LHCb, 2015 onward).
In the Standard Model these "exotic hadrons" are surprising
and their internal structure is debated.  In MaSt they are
simply higher-multiplicity decompositions of the same
standing wave — less probable (the energy must split more
ways) but not fundamentally different.


### 10.2 Why most baryons are broad resonances

Most entries in the baryon catalog are not sharp particles.
They are broad resonances — poorly defined masses with widths
Γ of 100–300 MeV, lifetimes of 10⁻²³ to 10⁻²⁴ s.  Only
the proton, neutron, and a few hyperons are long-lived.

This follows directly from the sub-mode picture.  A
decomposition that is far from any stable eigenmode of the
torus surface has a low quality factor (Q = m/Γ ≈ 1–10).
The cavity reasserts the parent eigenmode after only a few
traversals.  Only decompositions that happen to match a
near-eigenmode of the (possibly warped) surface can persist —
and these are rare, which is why the stable hadrons are few
while the resonances are many.

The **density of baryon resonances increases with mass**:
there are more Δ and N* states above 2 GeV than below it.
This is the expected behavior if each mass range corresponds
to a larger combinatorial space of sub-mode winding-number
partitions.  More energy allows more ways to divide it.


### 10.3 Mesons as two-body decompositions

If baryons are three sub-modes, mesons should be two.  A
quark-antiquark pair in the Standard Model maps to a (1,q)
sub-mode and its conjugate (1,−q), or equivalently two
sub-modes whose phase offsets sum to an integer.

For example, the pion (mass ~140 MeV, spin 0) could be a
(1,4) + (1,4) decomposition with anti-aligned spins.  The
low mass relative to the proton would reflect the fact that
the pion is a partial decomposition — most of the parent
mode's energy is not involved.  (In QCD, the pion's
anomalously low mass comes from being a Goldstone boson of
chiral symmetry breaking.  Whether MaSt's geometry produces
a corresponding suppression is an open question.)


### 10.4 The pattern

| SM concept | MaSt decomposition |
|------------|-------------------|
| Quark flavor (u, d, s, c, b, t) | Sub-mode winding numbers |
| Baryon (3 quarks) | Three-sub-mode tiling |
| Meson (quark + antiquark) | Two-sub-mode tiling |
| Exotic hadron (4q, 5q) | Higher-multiplicity tiling |
| Spin excitations (Δ vs p) | Phase alignment of sub-modes |
| Orbital excitations (L > 0) | Spatial beating patterns between sub-modes |
| Resonance width (Γ) | Inverse ring-down time |
| Resonance density vs mass | Combinatorial growth of winding partitions |

The hundreds of baryons are not hundreds of fundamental
things.  They are hundreds of ways to ring the same bell.


## 11. What's needed

1. **Shear on a (1,3) geodesic (R19 extension):**  Does the
   shear mechanism produce 1/3 charge for a mode that takes
   three traversals to close?  This is the decisive
   calculation.

2. **Time-dependent mode formalism (R24 T2):**  The current
   eigenmode framework is static.  Sub-mode decomposition
   requires evolving a perturbed standing wave on the torus
   surface and tracking how it redistributes.

3. **WvM charge on a warped surface (R40):**  If the torus
   deforms, does each sub-mode's local curvature yield the
   correct fractional charge?

4. **Ring-down time (R40):**  How quickly do sub-modes
   recombine into the eigenmode?  This determines the
   effective quark lifetime and sets the confinement scale.

5. **Meson states:**  Can a (1,2) mode decompose into two
   sub-modes with the right quantum numbers for pions, kaons,
   etc.?  Does the geometry suppress the meson mass the way
   chiral symmetry breaking does in QCD?

6. **Winding-number partition counting:**  Enumerate the
   allowed sub-mode tilings of a (1,2) mode on Ma_p as a
   function of total energy.  Compare the count vs. energy
   to the observed density of baryon resonances in the
   Particle Data Group tables.

7. **Pentaquark geometry:**  The LHCb pentaquark states
   (Pc(4312), Pc(4440), Pc(4457)) have specific masses and
   widths.  Can five-sub-mode decompositions reproduce these?
