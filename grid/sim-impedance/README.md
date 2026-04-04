# sim-impedance: Lattice junction coincidences

**Status:** Track 1 complete.  See findings below.

**Question:** when two lattices of different orientation
intersect, how often can nodes from each lattice be
interconnected by an edge of exactly one lattice spacing?
Does the coincidence rate relate to the fine-structure
constant α ≈ 1/137?

**Motivation:** the [alpha-in-grid](../../primers/alpha-in-grid.md)
primer frames α as the impedance mismatch between the 2D
material sheet (Ma) and the 3D spatial lattice (S).  A
particle's Coulomb energy is α times its Compton (wave)
energy — only 1/137 of the internal standing-wave energy
couples through the junction into the ambient grid.  This
simulation asks whether that fraction has a geometric origin
in the lattice structures themselves.

The idea: two lattices at a relative angle will have occasional
**coincidence pairs** — nodes from lattice A that sit exactly
one edge-length from a node in lattice B.  If the coincidence
rate, compared to the fully-connected density of an intact
lattice, yields a ratio near α, that would give α a concrete
geometric meaning.

---

## Approach

### What we measure

For two lattices overlapping in the same region of space:

1. **Coincidence count** — the number of cross-lattice node
   pairs separated by distance L ± ε (where L is the lattice
   spacing and ε is a small tolerance).

2. **Coincidence rate** — coincidences per node of lattice A,
   normalized by the number of nearest neighbors in an intact
   lattice.  This gives a dimensionless ratio: "what fraction
   of a node's potential connections actually reach across to
   the other lattice?"

3. **Periodicity** — do the coincidences form a regular
   pattern (a superlattice)?  If so, what is the period
   relative to L?  This superlattice spacing, if it exists,
   is the characteristic scale of inter-grid coupling.

### The comparison baseline

In an intact 2D triangular lattice, every node has **6 nearest
neighbors**, all at distance exactly L.  The coincidence rate
is measured against this fully-connected baseline.  If a node
on lattice A finds, on average, 6/137 ≈ 0.044 valid cross-
connections to lattice B, that would be suggestive.

---

## Tracks

### Track 1: Two 2D triangular lattices, rotated

The simplest case.  Two triangular lattices in the same plane,
both with edge length L = 1, rotated by angle θ relative to
each other.  Sweep θ from 0° to 30° (the symmetry period of
the triangular lattice).

**What to look for:**
- Coincidence rate vs angle θ
- Whether specific angles produce sharp peaks (CSL angles)
- Whether any peak or characteristic rate lands near 1/137
- The spatial pattern of coincidences (superlattice structure)

Script: [`track1_planar_rotation.py`](track1_planar_rotation.py)

**Track 1 findings:** the coincidence rate settles into a flat
band around 1/20 to 1/25 of intact coordination for most angles,
well above 1/137.  The rate scales linearly with tolerance ε
(no exact coincidences at generic angles), meaning the result
is dominated by geometric probability (annular area × node
density), not lattice-specific commensurability.  The spatial
patterns DO show periodic superlattice structure (coincidence
site lattices), but the raw rate is too high by ~6× to match α.
Conclusion: a purely mechanical/geometric coincidence count in
2D-to-2D does not produce α.  See output/ for plots and data.

### Track 2: 2D sheet in 3D lattice (abandoned)

The physical geometry: a 2D triangular lattice (Ma sheet)
embedded in a 3D close-packed lattice (spatial S), with
two orientation angles (tilt and twist).  More expensive
but closer to the real MaSt architecture.

### Track 3: Rational-angle coincidence site lattices (abandoned)

For specific rational rotation angles, exact coincidences
form a periodic superlattice (the CSL).  Enumerate the CSL
angles for the triangular lattice and compute their Σ values
(the ratio of superlattice cell area to original cell area).
Check whether Σ = 137 or a related value appears.

---

## What we learned

### The mechanical picture doesn't work

Track 1 tested the most direct version of the hypothesis:
count how often two lattices can physically interconnect, and
see if the rate is 1/137.  The answer is no — the coincidence
rate is ~1/20 of intact coordination, dominated by simple
geometric probability (how much annular area at distance L
contains nodes of the other lattice).  The rate scales linearly
with tolerance ε, has no special angle dependence, and carries
no lattice-specific signature beyond the node density.

A mechanical linkage — counting which nodes CAN connect — asks
the wrong question.  It measures geometric opportunity, not
physical cost.

### The right question is thermodynamic, not geometric

The phrase "defect cost" is thermodynamics language.  In
condensed matter physics, a defect cost is the **free energy
penalty** for introducing a topological defect (a vortex, a
dislocation) into an ordered medium.  It is not about how many
sites could geometrically hold a defect — it is about how much
energy the medium must store to accommodate one.

GRID already answers this question.  The Maxwell derivation
([maxwell.md](../maxwell.md), Step 5) gives the lattice action
with coupling constant κ = 1/(4πα) ≈ 1722.  The energy stored
in a minimal vortex — one 2π phase winding — is proportional
to κ, i.e. proportional to **1/α**.  This is the defect cost,
derived directly from the axioms.

### Alpha as energy partition

Consider a particle: a standing wave of energy mc² on the 2D
material sheet, whose phase winds through 2π (a topological
defect in the ambient 3D lattice).  The energy partitions
between two locations:

| Where | Energy | What it is |
|-------|--------|------------|
| On the sheet | mc² | The standing wave — the particle's mass |
| In the ambient lattice | αmc² | The Coulomb field — the energy cost of maintaining the 2π winding in the surrounding medium |

The fraction of total energy that radiates into the ambient
lattice as Coulomb field is:

<!-- α / (1 + α) ≈ α -->
$$
\frac{\alpha}{1 + \alpha} \approx \alpha
$$

This is exact.  The Coulomb self-energy of a charge e at the
Compton radius ƛ_C is e²/(4πε₀ƛ_C) = αmc².  The ratio
E_Coulomb / E_wave = α.

### What α is, physically

Alpha is not a geometric coincidence rate.  It is a
**thermodynamic partition ratio** — the fraction of a
topological defect's total energy that the ambient medium
must store to accommodate the twist.

In the GRID + MaSt picture:

- A particle is a 2π phase winding on a 2D sheet
- The winding is a topological defect in the ambient 3D lattice
- The lattice action (axiom A6) sets the energy cost of such
  a defect at κ = 1/(4πα) per unit of field strength squared
- The resulting Coulomb field carries energy αmc², while the
  wave itself carries mc²
- Alpha is the ratio: **how much energy does the defect leak
  into the surrounding medium, relative to the energy of the
  wave that created it?**

This reframes α from a mysterious measured constant to a
physically interpretable quantity: the energy tax that the
ambient lattice levies on a topological defect.  The value
1/137 is a free parameter — it is likely not derived from the lattice
geometry (as the compact-dimensions study and this simulation
both confirm).  But its *meaning* is clear: it is the coupling
efficiency between the 2D material sheet and the 3D spatial
lattice, expressed as an energy fraction.

The mechanical simulation was worth running because it ruled
out the simplest geometric explanation and pointed toward the
thermodynamic one.  The answer was already in the action
principle — we just needed to read it as a defect cost rather
than a coupling constant.

---

## Files

| File | Contents |
|------|----------|
| [track1_planar_rotation.py](track1_planar_rotation.py) | Track 1: sweep rotation angle, measure coincidence rate |
| [output/](output/) | Plots and data |
