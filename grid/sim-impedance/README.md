# sim-impedance: Lattice junction coupling

**Status:** Track 1 complete.  Tracks 2-3 framing.

**Question:** when two lattices of different structure or
orientation interface, what determines the coupling between
them?  Can the fine-structure constant α ≈ 1/137 emerge
from the geometry of this interface?

**Motivation:** the [alpha-in-grid](../../primers/alpha-in-grid.md)
primer frames α as the impedance mismatch between the 2D
material sheet (Ma) and the 3D spatial lattice (S).  A
particle's Coulomb energy is α times its Compton (wave)
energy — only 1/137 of the internal standing-wave energy
couples through the junction into the ambient grid.  This
folder investigates whether that fraction has a geometric
origin in the lattice structures themselves.

---

## Tracks

| Track | Premise | Status | Files |
|-------|---------|--------|-------|
| **1** | 2D-in-2D: two triangular lattices rotated in the same plane | Complete — negative (rate ~1/20, not 1/137) | [T1](T1-planar-rotation.md), [F1](F1-planar-rotation.md) |
| **2** | 2D-in-3D continuum: hexagonal sheet in truncated-octahedral lattice, sweeping orientation | Framing | [T2](T2-3d-lattice.md) |
| **3** | 2D-in-3D discrete: hexagonal rings on a Planck-scale 3D lattice, exact edge matching | Framing | [T3](T3-discrete-embedding.md) |
| **4** | Projection coupling: what fraction of 2D signal projects onto 3D edges? | Framing | [T4](T4-projection-coupling.md) |
| **5** | Wavefront transfer: coherent signal coupling through a shared 2D/3D node (projection matrix, SVD, directional efficiency) | Framing | [T5](T5-wavefront-transfer.md) |
| ~~6~~ | Rational-angle coincidence site lattices (CSL) | Abandoned | — |

**Track 1** established that 2D-in-2D coincidence counting
gives a smooth, featureless coupling rate dominated by
geometric probability — no structure near 1/137.

**Track 2** introduces the 3D truncated-octahedral lattice,
which has discrete "magic angles" (4 hexagonal face families
along ⟨111⟩ directions).  The coupling function C(θ,φ) is
zero except at these magic angles.  A torus embedded in the
lattice sweeps through the magic angles in proportion to its
surface area — the integral may give α at a specific ε.

**Track 3** goes to the Planck-discrete foundation.  All
edges are exactly L (no tolerance).  The question becomes:
at how many DISCRETE angles can a hexagonal ring share nodes
with a 3D lattice?  A staircase of partial coupling levels
(0 to 6 shared edges) emerges, and the ratio of coupled to
uncoupled angles may converge to 1/137 as the torus size
grows.  If so, α is a pure integer-geometry ratio.

---

## What we learned (from Track 1)

### The mechanical picture doesn't work (in 2D)

Track 1 tested the most direct version of the hypothesis:
count how often two lattices can physically interconnect, and
see if the rate is 1/137.  The answer is no — the coincidence
rate is ~1/20 of intact coordination, dominated by simple
geometric probability.  A mechanical linkage — counting which
nodes CAN connect — asks the wrong question in 2D.

### The right question may be thermodynamic

The phrase "defect cost" is thermodynamics language.  GRID
derives the defect cost from the lattice action with coupling
constant κ = 1/(4πα) ≈ 1722.  The energy stored in a minimal
vortex (one 2π phase winding) is proportional to 1/α.

Alpha is a **thermodynamic partition ratio** — the fraction of
a topological defect's total energy that the ambient medium
must store to accommodate the twist.  The Coulomb field
carries energy αmc², while the wave itself carries mc².

### But geometry may underlie the thermodynamics

Tracks 2 and 3 ask whether the REASON α has the value 1/137
is geometric: the fraction of orientations at which a 2D
hexagonal lattice couples to a 3D lattice with tetrahedral
coordination.  If the coupling fraction (from magic-angle
counting on the discrete lattice) converges to 1/137, the
thermodynamic partition ratio has a geometric origin.

---

## Files

| File | Contents |
|------|----------|
| [T1-planar-rotation.md](T1-planar-rotation.md) | Track 1 framing |
| [F1-planar-rotation.md](F1-planar-rotation.md) | Track 1 findings |
| [T2-3d-lattice.md](T2-3d-lattice.md) | Track 2 framing (continuum 3D) |
| [T3-discrete-embedding.md](T3-discrete-embedding.md) | Track 3 framing (discrete 3D) |
| [F3-step1-single-node.md](F3-step1-single-node.md) | Track 3 Step 1 findings |
| [scripts/track1_planar_rotation.py](scripts/track1_planar_rotation.py) | Track 1 script |
| [scripts/track3_step1_single_node.py](scripts/track3_step1_single_node.py) | Track 3 Step 1 (coarse) script |
| [scripts/track3_step1_fine.py](scripts/track3_step1_fine.py) | Track 3 Step 1 (fine resolution) script |
| [output/](output/) | Plots and data |
