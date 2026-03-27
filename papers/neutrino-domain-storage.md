# The Neutrino-Domain Memory: Architecture, Capacity, and Mobility

**Status:** outline
**Companion to:** [Sub-Quantum Memory](sub-quantum-memory.md)

---

## Table of contents

| # | Section | Story beat |
|---|---------|------------|
| 1 | The neutrino sheet | Ma_ν is a feature of spacetime at every point; the concert-hall analogy |
| 2 | The address space | Each cavity has a frequency-indexed mode spectrum |
| 3 | Information capacity | How much can one cavity store, and how does it scale? |
| 4 | Neutrons as gateways | Every neutron is a cross-plane node that couples to Ma_ν |
| 5 | Mobility solved | Neutrons are bound to atoms; the gateway travels with the cell |
| 6 | Three regimes | Cell death, locomotion, and violent disruption |
| 7 | Comparison to engineered memory | How the architecture maps to RAM, radio, and holography |
| 8 | Constraints and open calculations | What must be computed to make this quantitative |

---

## 1. The neutrino sheet

### 1.1 The material dimensions exist everywhere

The neutrino sheet (Ma_ν, the six-dimensional material space's
neutrino subplane) is not located inside a neutrino particle.
It is a structural feature of spacetime — two material
dimensions (θ₃, θ₄) that exist at every point in ordinary
3D space.  A neutrino particle is a
specific standing-wave excitation on this geometry, the way a
specific note is a vibration of a guitar string.  The string is
there whether or not anyone is playing.

### 1.2 The concert hall analogy

The neutrino sheet is the concert hall — a resonant space with
specific acoustic modes determined by its geometry.  Neutrino
particles are violins — one type of excitation that can exist
in the hall.  Cell membranes are speakers — sources that inject
energy at the hall's resonant frequencies.  The storage is in
the hall's mode pattern, not in the violins.

### 1.3 Accessing the hall requires a door

The concert hall exists everywhere, but its modes are in material
dimensions — inaccessible to ordinary electromagnetic fields
except through cross-dimensional coupling.  To write energy into
the hall, or read it back, something must bridge the gap between
ordinary 3D space (S) and the neutrino sheet.  That bridge is the
neutron (section 4).


## 2. The address space: frequency-indexed storage

### 2.1 Mode labeling

Each standing wave on Ma_ν is labeled by an integer pair (n₃,
n₄) — the number of wavelengths around each material loop.  The
pair is the mode's address.  Its energy (and therefore frequency)
is uniquely determined by the address and the geometry:

    E(n₃, n₄) = E₀ √((n₃/r)² + (n₄ − n₃s)²)

with E₀ = 29.26 meV, r ≈ 5, s = 0.022 (from R26 Assignment A).

### 2.2 Frequency as address

Unlike RAM (which addresses by physical location on a chip),
material-dimension storage addresses by frequency.  Each mode is
a distinct frequency channel.  Writing to mode (1,0) does not
disturb mode (3,2), just as tuning a radio to one station does
not interfere with another.  All channels occupy the same
physical location simultaneously — wavelength-division
multiplexing in material dimensions.

### 2.3 One cavity per ~(100 μm)³

Ma_ν has circumferences L₃ ≈ 200 μm and L₄ ≈ 42 μm.  The
spatial resolution of material-mode excitations is set by the
Compton wavelength of the lightest neutrino mode (~42 μm).  Two
regions of space closer than ~42 μm share the same cavity and
cannot store independent information.  The spatial grain is one
independent cavity per roughly (100 μm)³ — the volume of a
biological cell.


## 3. Information capacity

### 3.1 Mode counting

The number of modes below energy E_max on a material sheet with
aspect ratio r is:

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
| Ma-dim. body (100 meV) | ~6 PB |
| Library of Congress (digitized) | ~15 PB |
| Ma-dim. body (1 eV) | ~555 PB |


## 4. Neutrons as gateways to the neutrino sheet

### 4.1 The neutron is a cross-plane mode

In the Ma model, the neutron is not a bag of quarks.  It is a
single cross-plane standing wave: mode (1,2,0,0,1,2), spanning
the electron sheet Ma_e (dimensions 1–2) and the proton sheet
Ma_p (dimensions 5–6).  Its charge neutrality follows from the
cancellation of the Ma_e and Ma_p charge contributions.  Its mass
exceeds the proton's because the cross-shear coupling σ_ep adds
energy.

### 4.2 Cross-shear couples all three sheets

The Ma metric contains cross-shear parameters that couple every
pair of material-sheet subplanes.  The neutron's mode directly involves the
electron–proton coupling (σ_ep ≈ 0.038).  But the metric also
contains electron–neutrino coupling (σ_eν) and proton–neutrino
coupling (σ_νp).  A neutron — a physical excitation that already
bridges two material-sheet subplanes — provides a local coupling
node where energy in ordinary EM fields can reach the neutrino
sheet via the chain:

    EM field → Ma_e → σ_eν → Ma_ν
    EM field → Ma_p → σ_νp → Ma_ν

### 4.3 Every cell has many gateways

Nearly every atom heavier than hydrogen contains neutrons.  A
typical human cell contains ~10¹⁴ atoms, most with one or more
neutrons.  Each neutron is a cross-plane coupling node — a
gateway to Ma_ν at its location in S.  The cell does not need
to create or capture a special particle to access the neutrino
sheet; the gateways are already embedded in its ordinary matter.

### 4.4 Redundancy

The sheer number of neutron gateways per cell (~10¹⁴) provides
massive redundancy.  No single atom is critical.  Atoms are
continuously replaced by metabolism (the average atom in a human
body is replaced every few months to years), but as long as
replacement atoms also contain neutrons — which they do, because
chemistry requires them — the gateway population is maintained.

### 4.5 Coupling strength scales with neutron density

More neutrons per unit volume means stronger aggregate coupling
to Ma_ν.  Neutron-rich tissue (bone: calcium, phosphorus;
enzymes: zinc, iron, copper) would couple more strongly than
hydrogen-rich tissue (fat, water).  This is a testable
prediction: mineral-dense structures might serve as preferential
coupling sites.

### 4.6 All gateways share one cavity

The spatial resolution of Ma_ν is ~42 μm (set by the Compton
wavelength of the lightest neutrino mode).  All neutrons within
a cell (~10–100 μm diameter) are within one cavity.  They do
not create separate address spaces — they are multiple faucets
flowing into the same tub.  More gateways means stronger
coupling, not more storage.

Between cells (separated by ≳42 μm), neutrons couple to
different cavities — independent address spaces.  The one-cavity-
per-cell picture holds.


## 5. Mobility: the gateway travels with the cell

### 5.1 The mobility problem

If material-dimension storage is tied to fixed locations in
spacetime, then an organism walking across a room would leave its
stored information behind — like writing on the floor and then
walking away.

### 5.2 The neutron gateway resolves this

Neutrons are bound to atomic nuclei.  Atomic nuclei are bound
into molecules.  Molecules are bound into cells.  When a cell
moves through S, its atoms — and their neutrons — move with it.
The gateways are physically part of the matter.

The coupling chain (section 4.2) is local: each neutron couples
to Ma_ν at the neutron's own position in S.  As the neutron
moves, it couples to the neutrino sheet at its new position.  The
stored state is continuously refreshed and dragged along by the
moving gateway population, the way a magnet drags its field
pattern through a ferrofluid.

### 5.3 The coupling timescale is fast enough

The material-mode excitation must track the cell faster than the
cell crosses one cavity width.  At walking speed (~1 m/s), a cell
traverses ~100 μm in ~100 μs.  The gateway coupling operates at
THz-scale frequencies (picosecond timescales) — about 10⁸ times
faster than needed.  Even with severe evanescent suppression
(factors of 10⁶), a comfortable margin remains.

### 5.4 The stored state is an attribute of the matter

In this picture, the material-dimension state is not "information
stored at a location in spacetime."  It is "information stored
in the matter at that location" — carried by the matter's
neutron population and refreshed continuously through the
gateway coupling.  The matter carries its neutrino-sheet state
the same way it carries its mass, charge, and spin: as an
attribute of the particles, not of the coordinates.


## 6. Three regimes: survival, mobility, and disruption

### 6.1 Cell death within intact tissue

When a single cell dies, the surrounding tissue retains its
atoms (and their neutrons).  The gateway population in the
region is temporarily reduced but not eliminated.  More
importantly, the neighboring cells' gap-junction-connected
isopotential fields maintain the aggregate electromagnetic
environment that sustains the material-mode state.  The stored
information survives because the tissue-level field and the
gateway population persist.

### 6.2 Organism locomotion

When the organism moves, all cells move together.  Every neutron
in every atom moves with the body.  The entire gateway
population translates as a rigid body.  There is no relative
displacement between the stored state and the biology.

### 6.3 Violent disruption

Severe trauma destroys tissue structure, scatters atoms, and
disrupts the electromagnetic field.  The gateway population is
dispersed and the coupling environment is destroyed.  Stored
information in the affected region degrades or is lost.

This predicts that the boundary between "recoverable" and "lost"
morphogenetic information correlates with the boundary between
"intact matter + field structure" and "dispersed matter" — not
simply with cell viability.

### 6.4 The Goldilocks coupling

The coupling must be:
- **Strong enough** to drag the stored state during locomotion
  and to write/read via membrane voltages
- **Weak enough** to preserve stored states against thermal
  noise and casual electromagnetic interference

The neutron-gateway model helps with the "strong enough" side:
~10¹⁴ gateways per cell provide an aggregate coupling much
larger than a single evanescent tail.  The definitive answer
still requires computing the per-gateway coupling strength from
the Ma metric.


## 7. Comparison to engineered memory architectures

### 7.1 RAM analogy: address space and word size

RAM addresses memory by physical location (row, column on a
chip); each address holds 8 bits.  Material-dimension memory
addresses by frequency (mode quantum numbers); each address
holds ~7 bits.  The per-address capacity is comparable.  The
total address space (~180 modes at bio-relevant cutoff) is tiny
by RAM standards — but there are 37 trillion "chips" in a human
body.

### 7.2 Radio analogy: frequency-division multiplexing

The architecture is closer to a radio spectrum than to a memory
chip.  Each cavity has ~180 independent frequency channels, all
occupying the same physical location.  This is wavelength-
division multiplexing — the same principle used in fiber-optic
communications, where a single fiber carries hundreds of
independent data streams separated by wavelength.

### 7.3 Holographic analogy: distributed, analog, interference-based

Holographic memory stores information as interference patterns
in an optical medium.  Material-dimension memory stores energy
distributions across standing-wave modes.  Both are analog,
distributed, and frequency-addressed.  Both degrade gracefully
(losing detail before losing structure).  The key difference:
holographic media wear out; material-dimension geometry does not.

### 7.4 DNA analogy: capacity and addressing

The human genome stores ~750 MB (3 billion base pairs × 2 bits).
One cell's material-dimension cavity stores ~160 bytes (at
100 meV cutoff) — about 5,000× less than the genome.  But the
genome is the same in every cell; the material-dimension state
could be different in every cell.  The total unique information
across 37 trillion cells is ~6 PB material-dimension vs. ~750 MB
genomic — the material-dimension system wins by a factor of
~10⁷ in aggregate unique information.


## 8. Constraints and open calculations

### 8.1 Per-gateway coupling strength (critical)

The cross-shear–mediated coupling from a single neutron into
Ma_ν modes has not been computed.  This determines the
effective coupling per cell (single-neutron strength × ~10¹⁴
gateways), which in turn determines write/read speed, noise
immunity, and whether the Goldilocks condition (6.4) is met.

### 8.2 The noise floor (determines bits per mode)

The 7-bits-per-mode estimate assumes a ~1% noise floor.  The
actual noise floor depends on thermal coupling (kT ≈ 25 meV at
room temperature), cross-shear leakage rates, and environmental
electromagnetic interference.  A 10% noise floor halves the
capacity; a 0.1% floor increases it by ~50%.

### 8.3 Mode–mode coupling (determines information lifetime)

On a perfectly flat material sheet with linear dynamics, modes are exactly
independent and information persists forever.  Real corrections
— cross-shear coupling, nonlinear wave interactions — transfer
energy between modes, blurring the stored state.  The rate of
this transfer sets the information lifetime.

### 8.4 Spatial resolution (determines cavity independence)

The one-cavity-per-cell estimate assumes the resolution is set
by the Compton wavelength of the lightest neutrino mode (~42 μm).
The actual resolution could be finer (if gateway coupling is
more localized) or coarser (if Levin's isopotential cell fields
create larger coherent regions).

### 8.5 Neutron density variation across tissue types

If coupling scales with neutron count, different tissues have
different coupling strengths.  Mapping neutron density across
tissue types (bone vs. fat vs. nerve vs. muscle) could predict
which tissues are most sensitive to material-dimension storage —
and which are most vulnerable to disruption.

### 8.6 Relationship to the parent paper

This paper develops the information-theoretic and engineering
implications of the storage hypothesis presented in
[Sub-Quantum Memory](sub-quantum-memory.md).  It takes the physics
of that paper as given (Ma geometry, threshold absorption,
evanescent coupling) and works through three questions that
paper leaves open: how much can the system store, how is it
addressed, and how does the stored state move with the organism.
The neutron-gateway mechanism (section 4) provides a concrete
physical answer to the mobility question that the parent paper
identifies but does not resolve.
