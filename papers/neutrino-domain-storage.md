# The Neutrino-Domain Memory: Architecture, Capacity, and Mobility

**Status:** outline
**Companion to:** [Sub-Quantum Memory](storage-in-t6.md)

---

## Table of contents

| # | Section | Story beat |
|---|---------|------------|
| 1 | Geometry vs. particle | The neutrino T² is everywhere — you don't need a neutrino per cell |
| 2 | The address space | Each point in space has a frequency-indexed mode spectrum |
| 3 | Information capacity | How much can one cavity store, and how does it scale? |
| 4 | The mobility problem | Stored information must move with the organism |
| 5 | The wavepacket resolution | Compact-dimension excitations have spatial wavefunctions |
| 6 | Electromagnetic coupling as the anchor | The cell's field is the bowl; the excitation is the marble |
| 7 | Survival, mobility, and disruption | Three regimes: cell death, locomotion, trauma |
| 8 | Comparison to engineered memory | How the architecture maps to RAM, radio, and holography |
| 9 | Constraints and open calculations | What must be computed to make this quantitative |

---

## 1. Geometry vs. particle: the concert hall, not the violin

### 1.1 The compact dimensions exist everywhere

The neutrino T² is not located inside a neutrino.  It is a
structural feature of spacetime — two compact dimensions (θ₃,
θ₄) that exist at every point in ordinary 3D space.  A neutrino
particle is a specific standing-wave excitation on this geometry,
the way a specific note is a vibration of a guitar string.  The
string is there whether or not anyone is playing.

### 1.2 No neutrino particle per cell

The storage hypothesis does not require a neutrino particle to
be associated with each biological cell.  Neutrinos interact
only via the weak force (cross-section ~10⁻⁴⁴ cm²); there is no
known force that could confine one to a cell.  In the T⁶ model
specifically, the cross-plane coupling between the neutrino T²
and the electron/proton T²s is suppressed by (mᵥ/mₑ)² ~ 10⁻⁸.
Trapping a neutrino is neither necessary nor possible.

### 1.3 The concert hall analogy

The neutrino T² is the concert hall — a resonant space with
specific acoustic modes.  Neutrino particles are violins — one
type of excitation that can exist in the hall.  Cell membranes
are speakers — sources that inject energy at the hall's resonant
frequencies.  The storage is in the hall's mode pattern, not in
the violins.  The hall exists whether or not any violin is present.

### 1.4 What couples to what

The write mechanism is resonant frequency coupling: an
electromagnetic field oscillating at a mode's frequency, at a
given location in space, couples into that compact-dimension mode
via evanescent overlap.  The cell membrane's voltage oscillations
(10–90 meV) match the neutrino T² mode energies.  No particle
exchange is involved — the coupling is field-to-geometry, not
particle-to-particle.


## 2. The address space: frequency-indexed storage

### 2.1 Mode labeling

Each standing wave on the neutrino T² is labeled by an integer
pair (n₃, n₄) — the number of wavelengths around each compact
loop.  The pair is the mode's address.  Its energy (and therefore
frequency) is uniquely determined by the address and the geometry:

    E(n₃, n₄) = E₀ √((n₃/r)² + (n₄ − n₃s)²)

with E₀ = 29.26 meV, r ≈ 5, s = 0.022 (from R26 Assignment A).

### 2.2 Frequency as address

Unlike RAM (which addresses by physical location on a chip),
compact-dimension storage addresses by frequency.  Each mode is
a distinct frequency channel.  Writing to mode (1,0) does not
disturb mode (3,2), just as tuning a radio to one station does
not interfere with another.  All channels occupy the same
physical location simultaneously — wavelength-division
multiplexing in compact dimensions.

### 2.3 One cavity per ~(100 μm)³

The neutrino T² has circumferences L₃ ≈ 200 μm and L₄ ≈ 42 μm.
The evanescent coupling that connects 3+1D fields to compact
modes has a characteristic range set by these lengths.  Two
regions of space closer than ~100 μm share the same cavity and
cannot store independent information.  The spatial resolution is
one independent cavity per ~(100 μm)³ — the volume of a
biological cell.


## 3. Information capacity

### 3.1 Mode counting

The number of modes below energy E_max on a T² with aspect
ratio r is:

    N(E_max) ≈ π r (E_max / E₀)²

Verified against R26 F5 (r = 1, E_max = 1 eV: formula gives
3,668; simulation gives 3,670).

### 3.2 Modes per cavity at representative cutoffs

| Energy cutoff | Physical context | Mode count |
|---|---|---|
| 100 meV | Bio-relevant (membrane voltages) | ~180 |
| 300 meV | Sub-eV thermal regime | ~1,650 |
| 1 eV | Visible-light scale | ~18,000 |
| 10 eV | Deep UV | ~1.8 million |

### 3.3 Bits per mode

Each mode holds a continuously variable amplitude (under the
threshold model).  Precision is limited by noise — thermal
leakage, cross-shear coupling, and the unknown coupling
strength.  At ~1% noise floor: ~7 bits per mode (~100
distinguishable levels).  This is comparable to RAM's 8 bits
per address.

### 3.4 Capacity per cavity

| Cutoff | Modes | Bits | Equivalent |
|---|---|---|---|
| 100 meV | 180 | ~1,260 | ~160 bytes |
| 300 meV | 1,650 | ~11,500 | ~1.4 KB |
| 1 eV | 18,000 | ~126,000 | ~15 KB |

At the biologically relevant cutoff (100 meV), each cell-sized
cavity holds about 160 bytes — less than a tweet.

### 3.5 Scaling to biological systems

| System | Cells | At 100 meV | At 1 eV |
|---|---|---|---|
| Planarian | ~10⁷ | ~1.6 GB | ~150 GB |
| Human brain | ~2.5 × 10¹¹ | ~40 TB | ~3.7 PB |
| Human body | ~3.7 × 10¹³ | ~5.9 PB | ~555 PB |

### 3.6 Comparison to familiar scales

| Storage system | Capacity |
|---|---|
| Laptop RAM | 16–64 GB |
| High-end server | 1–4 TB |
| Human brain (neural estimate) | ~2.5 PB |
| Compact-dim. body (100 meV) | ~6 PB |
| Library of Congress (digitized) | ~15 PB |
| Compact-dim. body (1 eV) | ~555 PB |


## 4. The mobility problem

### 4.1 The naive picture is fatal

If compact-dimension modes are properties of fixed locations in
spacetime, then walking across a room would separate an organism
from its stored information — like writing a message on the floor
and then leaving.  Every cell would arrive at a new location
containing someone else's (or no one's) stored state.

### 4.2 The problem applies to all particles

This concern is not unique to storage.  In the T⁶ model, the
electron IS a standing wave on compact dimensions.  When an
electron moves through space, its mass, charge, and spin do not
get left behind.  Whatever mechanism allows particles to carry
their compact-dimension properties through space applies equally
to sub-threshold storage excitations.

### 4.3 The problem is therefore already solved (in principle)

If the T⁶ model is viable at all — if it can describe moving
particles — then it already contains the mechanism for mobile
compact-dimension excitations.  The storage paper inherits this
mechanism; it does not need to invent a new one.


## 5. The wavepacket resolution

### 5.1 Two-part wavefunctions in Kaluza-Klein theory

In standard KK theory, every excitation of the compact
dimensions has both a compact part and a spatial part:

    ψ(x, θ) = φ(x, t) × χ(θ₃, θ₄)

The compact part χ determines the mode identity (which frequency
channel, what mass, what charge).  The spatial part φ is a
wavepacket in ordinary 3D space that determines where the
excitation is localized and how it moves.

### 5.2 Storage excitations are wavepackets, not fixed points

A sub-threshold energy deposit in mode (n₃, n₄) at position x₀
is not a permanent marking on spacetime at x₀.  It is a
wavepacket — a localized disturbance with both compact quantum
numbers and a spatial envelope.  The spatial envelope can
propagate, accelerate, and respond to forces, just like any
other field excitation.

### 5.3 Group velocity and dispersion

The dispersion relation for a compact-dimension mode with 3D
momentum k is E² = m²c⁴ + (ℏck)², where m is the mode mass
(set by the compact quantum numbers).  The group velocity is
v_g = ℏck/E — the same as any relativistic particle.  Storage
excitations can move at any speed up to c.


## 6. Electromagnetic coupling as the anchor

### 6.1 The potential well picture

The cell's electromagnetic field — generated by membrane
voltages, ion currents, and charge distributions — creates a
potential landscape in the compact-mode sector at the cell's
location.  A sub-threshold excitation sits in the potential well
created by this field.  The marble sits in the bowl.

### 6.2 The bowl moves with the cell

When the cell moves, its electromagnetic field moves.  The
potential well shifts in space.  The compact-dimension
excitation, coupled to the field, is dragged along — the way
a marble follows a bowl being carried across a room.

### 6.3 Coupling strength determines tracking fidelity

The excitation tracks the cell if the coupling can "refresh"
the compact-dimension state faster than the cell traverses one
cavity width.  At walking speed (~1 m/s), a cell crosses 100 μm
in ~100 μs.  THz-scale electromagnetic coupling operates on
picosecond timescales — about 10⁸ times faster than needed.
Even with severe evanescent suppression (factors of 10⁶), the
margin is comfortable.

### 6.4 The water-surface analogy

The compact dimensions are like a water surface that extends
everywhere.  A wave pattern on the surface is localized — a
disturbance at a specific place.  A boat (the cell) moving
across the lake drags wave patterns (the stored state) with it
through electromagnetic coupling.  The water is everywhere, but
the pattern follows the boat.


## 7. Three regimes: survival, mobility, and disruption

### 7.1 Cell death within intact tissue

When a single cell dies, its neighbors maintain the aggregate
electromagnetic field of the tissue region (connected via gap
junctions into isopotential fields).  The compact-mode
excitation at that location does not lose its anchor — the
surrounding cells' fields sustain the potential well.  The marble
stays in the bowl even if one stave is replaced.

This is why compact-dimension storage survives tissue turnover:
the excitation is coupled to the collective field, not to any
single cell.

### 7.2 Organism locomotion

When the entire organism moves, all cells move together.  The
aggregate electromagnetic field moves rigidly.  Every compact-
mode excitation is dragged along simultaneously.  There is no
relative displacement between the stored state and the biology
— the entire system translates as a unit.

### 7.3 Violent disruption

Severe trauma (crush injury, burns, radiation damage) destroys
the electromagnetic field structure over a region.  The potential
wells that anchor compact-mode excitations are disrupted.
Information in the affected region degrades or is lost.

This is consistent with biology: severe trauma causes
morphogenetic errors, developmental defects, and loss of
regenerative fidelity.  The prediction is that the boundary
between "recoverable" and "lost" information correlates with
the boundary between "intact field structure" and "disrupted
field structure" — not with the boundary between "living cells"
and "dead cells."

### 7.4 The Goldilocks coupling

The coupling must be:
- **Strong enough** to drag excitations along during movement
  and to write/read via membrane voltages
- **Weak enough** to preserve stored states against thermal
  noise and casual electromagnetic interference

This is the same tension identified in the parent paper
(storage-in-t6, section 14.2).  The margin analysis (6.3)
suggests both conditions can be met simultaneously, but the
definitive answer requires computing the evanescent coupling
strength from the T⁶ metric.


## 8. Comparison to engineered memory architectures

### 8.1 RAM analogy: address space and word size

RAM addresses memory by physical location (row, column on a
chip); each address holds 8 bits.  Compact-dimension memory
addresses by frequency (mode quantum numbers); each address
holds ~7 bits.  The per-address capacity is comparable.  The
total address space (~180 modes at bio-relevant cutoff) is tiny
by RAM standards — but there are 37 trillion "chips" in a human
body.

### 8.2 Radio analogy: frequency-division multiplexing

The architecture is closer to a radio spectrum than to a memory
chip.  Each cavity has ~180 independent frequency channels, all
occupying the same physical location.  This is wavelength-
division multiplexing — the same principle used in fiber-optic
communications, where a single fiber carries hundreds of
independent data streams separated by wavelength.

### 8.3 Holographic analogy: distributed, analog, interference-based

Holographic memory stores information as interference patterns
in an optical medium.  Compact-dimension memory stores energy
distributions across standing-wave modes.  Both are analog,
distributed, and frequency-addressed.  Both degrade gracefully
(losing detail before losing structure).  The key difference:
holographic media wear out; compact-dimension geometry does not.

### 8.4 DNA analogy: capacity and addressing

The human genome stores ~750 MB (3 billion base pairs × 2 bits).
One cell's compact-dimension cavity stores ~160 bytes (at
100 meV cutoff) — about 5,000× less than the genome.  But the
genome is the same in every cell; the compact-dimension state
could be different in every cell.  The total unique information
across 37 trillion cells is ~6 PB compact-dimension vs. ~750 MB
genomic — the compact-dimension system wins by a factor of
~10⁷ in aggregate unique information.


## 9. Constraints and open calculations

### 9.1 The coupling strength (critical)

The evanescent coupling between 3+1D electromagnetic fields and
compact-dimension modes has not been computed.  This single
number determines whether the entire architecture is physically
viable.  It must satisfy the Goldilocks constraint (section 7.4):
strong enough for write/read and mobility, weak enough for
retention and noise immunity.

### 9.2 The noise floor (determines bits per mode)

The 7-bits-per-mode estimate assumes a ~1% noise floor.  The
actual noise floor depends on thermal coupling (kT ≈ 25 meV at
room temperature), cross-shear leakage rates, and environmental
electromagnetic interference.  A 10% noise floor halves the
capacity; a 0.1% floor increases it by ~50%.

### 9.3 Mode–mode coupling (determines information lifetime)

On a perfectly flat T² with linear dynamics, modes are exactly
independent and information persists forever.  Real corrections
— cross-shear coupling, nonlinear wave interactions — transfer
energy between modes, blurring the stored state.  The rate of
this transfer sets the information lifetime.  This calculation
requires the full T⁶ metric with realistic cross-shear
parameters.

### 9.4 Spatial resolution (determines cavity independence)

The estimate of one independent cavity per ~(100 μm)³ assumes
the evanescent coupling range matches the compact dimension
size.  The actual spatial resolution could be finer (if the
coupling is more localized) or coarser (if field configurations
create larger coherent regions, as suggested by Levin's
isopotential cell fields).

### 9.5 Tracking speed limit (determines mobility constraint)

The maximum organism speed at which compact-mode excitations
can track the biology.  Estimated at ≫ 1 m/s (section 6.3),
but the actual limit depends on the coupling strength.  If
the limit is below biological speeds (cheetah: 30 m/s; nerve
impulse: 100 m/s), the hypothesis faces a constraint.

### 9.6 Relationship to the parent paper

This paper develops the information-theoretic and engineering
implications of the storage hypothesis presented in
[Sub-Quantum Memory](storage-in-t6.md).  It takes the physics
of that paper as given (T⁶ geometry, threshold absorption,
evanescent coupling) and works through three questions that
paper leaves open: how much can the system store, how is it
addressed, and how does the stored state move with the organism.
