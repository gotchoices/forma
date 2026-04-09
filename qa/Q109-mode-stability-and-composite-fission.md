# Q109. Mode stability and composite fission: when does a torus mode survive as a free particle?

**Status:** Open — principled framework established
**Related:**
  [Q95](Q95-strong-force-as-internal-em.md) (strong force as internal Ma coupling),
  [Q107](Q107-wave-translation-of-atomic-physics.md) (Ma/S translation for atoms),
  [Q105](Q105-atoms-as-cross-sheet-modes.md) (atoms as cross-sheet modes),
  R33 Track 9 (Coulomb fission — computational verification),
  R47 review ((1,3) vs (3,6) proton — irreducibility argument),
  [`primers/charge-from-energy.md`](../primers/charge-from-energy.md) §3, §11 (2π charge rule)

---

## 1. The question

The Ma spectrum contains many modes (n₁, n₂) on each sheet.
Which of these can exist as **free particles** — stable,
observable, propagating modes in S?

Several filters are known:

- **Waveguide cutoff** (R46, R47): modes below cutoff are
  evanescent and don't propagate.  Kills (1,1) on Ma_e.
- **Spin-statistics** (R33 Track 6 / R49): fractional-spin
  modes are forbidden.  Kills most high-n₂ modes.
- **Charge integral** (R33 Track 1): determines coupling
  strength to the EM field.

This Q file addresses a fourth filter:

> **Composite fission.**  A mode whose winding numbers share
> a common factor can decompose into simpler modes.  Whether
> the composite is stable depends on whether the forces
> between the sub-modes are attractive (binding) or
> repulsive (fission).

This is the question of whether a given torus mode is a
**single particle** or an **unstable composite** that
splits apart in 3D space.


## 2. The gcd criterion

A mode (n₁, n₂) has a greatest common divisor g = gcd(n₁, n₂).

**If g = 1: the mode is irreducible.**

The standing wave traces an irreducible geodesic on the torus.
Its internal structure consists of **antinodes** — peaks of
one wave at evenly-spaced positions around the ring.  Antinodes
are features of the wave, not independent sub-modes.  You cannot
separate an antinode from its wave.

Examples: (1,2) electron, (1,3) proton.

**If g > 1: the mode is reducible.**

The standing wave decomposes into g copies of the reduced mode
(n₁/g, n₂/g), each at a different phase (evenly spaced around
the torus).  Each copy is called a **strand**.  Each strand is
a valid, independently-propagating mode on its own.

Examples: (2,4) = 2 × (1,2), (3,6) = 3 × (1,2).

The composite's stability then depends entirely on the forces
between strands.


## 3. Forces between strands

For a reducible mode (g·m, g·n) = g copies of (m, n):

**On the electron sheet (Ma_e):**

Each strand is a (1,2) electron.  By GRID's 2π charge rule,
each strand carries charge −e.  The inter-strand force
(between two electrons) is:

- **Coulomb repulsion** at strength α ≈ 1/137
- **No confining force** — the electron sheet has only
  electromagnetic internal coupling

Result: repulsion wins.  The composite fissions into g
separate (1,2) electrons.  The fission energy (Coulomb
self-energy at the mode's Compton radius) grows as
~g²(g−1)/2 × α × m_e (R33 Track 9, F17).

**On the proton sheet (Ma_p) under the (1,3) hypothesis:**

The proton is (1,3), which has gcd(1,3) = 1 — irreducible.
The fission question does not arise.  Its three-fold
structure (three energy antinodes at 0°, 120°, 240°) is a
property of one standing wave, not three separable modes.
This is why quark confinement is automatic under (1,3):
there are no "quarks" to free (R47 review).

**Nuclear modes (A, 3A) on Ma_p:**

Nuclei modeled as (A, 3A) have gcd(A, 3A) = A.  Under the
gcd criterion, they are reducible into A strands of (1,3).
But nuclear modes ARE stable — held together by the internal
Ma field at full coupling strength (~1), not the
α-attenuated Coulomb (~1/137).  This is Q95's insight: the
"strong force" is the electromagnetic field seen from inside
Ma at torus-overlap distance, without Compton-window
attenuation.

| Sheet | Mode | gcd | Strands | Inter-strand force | Stable? |
|:---|:---:|:---:|:---|:---|:---:|
| Ma_e | (1,2) | 1 | irreducible | n/a | YES |
| Ma_e | (2,4) | 2 | 2 × (1,2) | Coulomb repulsion (α) | NO |
| Ma_e | (3,6) | 3 | 3 × (1,2) | Coulomb repulsion (α) | NO |
| Ma_p | (1,3) | 1 | irreducible | n/a | YES |
| Ma_p | (2,6) | 2 | 2 × (1,3) | Ma internal (~1), attractive | YES (He-4) |
| Ma_p | (6,18) | 6 | 6 × (1,3) | Ma internal (~1), attractive | YES (C-12) |


## 4. Why Ma_p supports composites but Ma_e does not

The difference is not about the sheets having different
physics.  Both sheets have the same internal electromagnetic
fields.  The difference is about what coupling pathway the
strands use to interact:

**Between Ma_e strands (free electrons at r >> λ_C):**

Two (1,2) electrons in the same spatial region interact
through S — the 3D lattice.  Their fields are α-projected
through the Compton window (Q94).  The interaction is:

    V(r) = α ℏc / r   (repulsive, Coulomb)

At the Compton scale (~400 fm), this is ~3.7 keV per pair.
No confining term.  The strands separate.

**Between Ma_p strands (nucleons at r ~ λ_C):**

Two (1,3) protons at nuclear distances (~1 fm) are within
each other's Compton wavelength.  Their Ma tori overlap.
The interaction goes **directly through Ma**, not through S:

    V(r) ~ ℏc / r   (full internal field, ~137× stronger)

Plus a confining linear term from the flux-tube topology.
The binding energy (~MeV per pair) vastly exceeds the
Coulomb repulsion (~keV).  The strands are locked together.

The key variable is **distance relative to the Compton
wavelength** (r/λ_C):

| r/λ_C | Coupling pathway | Strength | Regime |
|:---:|:---|:---:|:---|
| >> 1 | Through S (Compton window) | α ≈ 1/137 | Electromagnetic |
| ~ 1 | Direct on Ma (torus overlap) | ~1 | "Strong" |
| << 1 | Inside the mode | ~1 | Irreducible |

For free electrons, r/λ_C >> 1 (they are macroscopically
separated).  For nucleons in a nucleus, r/λ_C ~ 1 (they
overlap).  Same physics, different regime.


## 5. Multi-electron states in atoms

Atoms appear to violate the fission rule: Z electrons bound
to a nucleus form a stable configuration.  But they are NOT
a free (Z, 2Z) mode on Ma_e.  They are Z separate (1,2)
modes confined by an **external** potential — the nuclear
Coulomb attraction from Ma_p, transmitted through S.

Remove the nucleus and the electrons fly apart.  The
stability is S-physics (external confinement), not
Ma-physics (internal binding).

This is the two-tier picture applied to mode stability:

| | Ma contribution | S contribution |
|:---|:---|:---|
| **Free electron** | (1,2) mode identity | propagation in S |
| **Free multi-electron** | n × (1,2) strands | Coulomb fission — unstable |
| **Atomic electrons** | n × (1,2) strands | nuclear Coulomb confinement — stable |
| **Free proton** | (1,3) mode identity | propagation in S |
| **Nucleus** | A × (1,3) strands | Ma internal binding (Q95) |


## 6. Connection to the 2π charge rule

GRID's charge quantization (axiom A3) states: each 2π tube
winding contributes one unit of charge.  A mode with n₁
tube windings carries charge |Q| = n₁.

For a reducible mode (g·1, g·2) = g electrons on Ma_e:
- Total charge = −g·e (g tube windings, g charges)
- Total mass = g × m_e
- This is g electrons' worth of energy and charge

The 2π rule tells us these are g quanta of the same
fundamental excitation.  The gcd criterion tells us they
can separate because each quantum is independently valid.

For an irreducible mode like (1,3) on Ma_p:
- Total charge = +1·e (one tube winding, one charge)
- The three ring windings create three antinodes but only
  one charge — they are spatial structure of ONE quantum,
  not three separate quanta

This is the "3-phase" nature of the proton: three antinodes
locked in a single standing wave, like 3-phase AC power where
the three phases cannot desynchronize because they are features
of one rotating field, not three independent oscillators.


## 7. Implications

### For ghost selection (R33)

The gcd criterion adds a stability filter beyond charge and
spin: modes with gcd > 1 on Ma_e are unstable composites
that fission.  Only gcd = 1 modes survive as free particles.
On Ma_e with the waveguide cutoff, the only surviving free
charged fermion is (1,2) — the electron.

### For the proton hypothesis

The (1,3) proton has gcd = 1 — irreducible, automatically
confined.  The (3,6) proton has gcd = 3 — reducible into
three (1,2) strands that need an external mechanism (waveguide
cutoff) to prevent separation.  The irreducibility of (1,3)
is a structural advantage: confinement is guaranteed by
topology, not by a dynamical mechanism.

### For nuclear physics

Nuclei as (A, 3A) on Ma_p have gcd = A — they are A copies
of (1,3) protons.  Nuclear stability comes from direct Ma
coupling at torus-overlap distances (Q95).  Nuclear fission
and fusion are transitions between different A values on the
proton sheet, with the energy balance determined by the
competition between Ma binding and Coulomb repulsion.

### For atoms

Atomic electron configurations are S-physics: Z separate
(1,2) modes held by nuclear Coulomb attraction.  Shell
structure, angular momentum, and screening are properties
of the 3D arrangement (S + GRID), not of the Ma metric.
The Ma contribution to atoms is limited to particle identity:
mass, charge, spin, and the universal properties that make
all electrons identical.


## 8. Summary

A free torus mode is stable if and only if:

1. It passes the waveguide cutoff (can propagate)
2. It has valid spin (integer or half-integer)
3. It is either **irreducible** (gcd = 1) or **bound by
   internal Ma coupling** (nuclear scale, gcd > 1 with
   torus overlap)

Modes that are reducible AND lack internal binding fission
into their constituent strands.  On Ma_e, this kills all
(n, 2n) harmonics with n ≥ 2.  On Ma_p, internal Ma
coupling at the full field strength binds nuclear composites.

The pattern:
- **Ma_e free particles:** only (1,2) — the electron
- **Ma_p free particles:** (1,3) — the proton — plus
  nuclear composites (A, 3A) bound by Ma internal coupling
- **Atoms:** S-physics confinement of Ma_e modes by Ma_p
  modes through the GRID-derived Coulomb potential
