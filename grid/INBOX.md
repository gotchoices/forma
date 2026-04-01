# GRID Inbox

Raw ideas, hypotheses, and open threads not yet formalized
into study documents.  Items here may be promoted to their own
files or absorbed into existing documents as they mature.

---

## 2026-03-31: The cell as a processor on a string

### The computational picture

The GRID lattice looks like a **distributed processor on a
graph network**.  Each node and edge is an independent
computational unit:

- **Node register:** each cell holds an internal register
  storing a fractional bit (ζ = 1/4 for 2D triangular).
  This is the phase θ ∈ [0, 2π).

- **Edge registers:** each of the 3 edges (in the 2D
  triangular case) also stores state — the link phase /
  gauge connection A_μ.  These are the "wires" between
  processors.

- **Clock cycle:** every Planck time, each processor:
  1. Reads its own state and the state of its 3 edges
  2. Advances its own phase (node update)
  3. Advances the state of each of its edges (link update)
  4. The update rule is the lattice equation of motion —
     a "micro-coded instruction set" hardwired into the
     geometry

- **Phase periodicity and carries:** the state registers
  are periodic (θ wraps at 2π).  When a phase accumulates
  past 2π it wraps — analogous to a carry bit.  Where does
  the carry propagate?  Presumably to the edges (gauge
  connection absorbs the wrap, maintaining gauge
  invariance).  This might be the microscopic mechanism of
  charge quantization: a topological carry.

### Sub-state resolution

**Question:** is it "legal" for nodes/edges to do internal
bookkeeping at higher resolution than the ζ = 1/4 bit?

The 1/4 bit is the **externally accessible** information per
cell — what a horizon observer can extract.  Internally, the
phase θ is a continuous variable (or at least finer-grained
than 1/4 bit).  So yes — the cell's internal state can have
higher resolution than what it contributes to the collective
entropy.  Call this **sub-state resolution**: the precision
"right of the decimal place" in the fractional bit.

Analogy: a floating-point register has a fixed number of bits
visible to the bus, but internal pipeline stages may carry
extra guard bits for rounding.

The ζ = 1/4 bound is about the **entropy** (how many
distinguishable macrostates), not the internal state space.
The cell can have a rich internal life as long as the
*externally distinguishable* information per cell is ζ.

### The internal dimension as a string

What if the sub-state lives in an **internal 1D space** — a
tiny periodic dimension attached to each node?

- Each node is a **self-connected string** — a 1D periodic
  loop (a tiny torus) rendered at the lattice site.  It
  supports standing waves whose amplitudes encode the
  node's state.

- Each edge is a **linear string** connecting neighboring
  nodes.  It also supports standing waves that encode link
  state (the gauge connection).

- At the 3 connection points (where edge strings meet the
  node loop), there is a natural **additive junction** —
  the standing waves on the edge and node combine.  This
  is the microscopic version of the covariant derivative
  D_μθ = ∂_μθ − eA_μ: the phase gradient on the node
  (∂_μθ) plus the link contribution (A_μ) combine at the
  junction.

This picture looks like a **graphene sheet** — hexagonal
nodes connected by bonds, with vibrational modes on both.
Graphene could be a sympathetic macro-scale analog of the
fundamental lattice.

### Connection to string theory

This internal 1D dimension — a string-like degree of freedom
at each lattice site — is reminiscent of the **11th dimension**
in M-theory.  String theory says the fundamental objects are
1D strings; here, the "strings" are the internal state space
of nodes and edges.

If the node loop has a circumference related to the Planck
length, and the edge strings have a length of one lattice
spacing (also Planck), then the string tension and mode
spectrum would be set by the lattice geometry.  The standing
wave modes on the node loop would be quantized — giving
discrete internal states despite the continuous phase.

**Status:** purely conceptual.  May be functional (could
lead to a computational model) or may be just a useful
mental picture.

### Potential next step

Build a Python model of a small triangular lattice where:
- Each node has an internal 1D periodic register (mode
  amplitudes)
- Each edge has a 1D linear register
- Update rules propagate state per clock cycle
- Test whether the lattice can store a superposition of
  plane waves going in arbitrary directions (which is what
  is needed to host Maxwell's equations, and likely
  gravity via the thermodynamic route)

### Clifford embedding of Ma tori in S

The MaSt material sheets (Ma) are 2-tori embedded in the 3D
spatial lattice (S).  The current treatment may be too
abstract — the embedding might be more **literal** than
previously assumed.

**Problem:** embedding a flat 2-torus in 3D Euclidean space
necessarily introduces extrinsic curvature (you get a donut
shape, which stretches the surface).  A **Clifford torus**
embeds a flat torus in 4D (specifically in S³ ⊂ R⁴) with
zero extrinsic curvature — it sits "flat" in the higher-
dimensional space.

**Questions:**
- Can we embed the Ma 2-torus into 3D+1 (S × t) via a
  Clifford-like construction without warping?
- Does the (1,3) signature of spacetime help or hurt?  In
  Minkowski space, the extra dimension is timelike — this
  changes the geometry of the embedding.
- If the torus must embed in 3D (not 4D), is the extrinsic
  curvature physical?  Does it contribute to the particle's
  mass or energy?
- Does MaSt as currently formulated implicitly assume a flat
  embedding, and if so, does that need to be revisited?

**Status:** open question.  May need a focused study if the
embedding geometry affects the physics.

---

## 2026-03-31: Flat grid, warped embedding, dual-bubble law

**Promoted to** [dual-bubbles.md](dual-bubbles.md).

Core idea: the flat Ma torus forces the ambient S lattice to
deform (→ gravity), and the product λ_C × r_s = 2L_P² =
1/(2ζ) is a conservation law linking internal compactness to
external curvature.

---

## 2026-04-01: Model B — cell = its edges, no self

### The shift

The original "cell as processor" picture (Model A) placed a
circular string loop at each cell centre with linear strings
going out to neighbors.  **Model B** eliminates the loop:
the cell IS its boundary edges.  There is no separate
internal register.

Two ways to visualise the cell:
- **Triangle of strings** (2D): 3 edges forming the cell
  boundary, each shared with one neighbor.  The vertex is
  a coupling junction, not a state holder.
- **Node with strings out:** the cell centre sends 3 (half-)
  strings to neighbors.  Requires defining "half-string"
  boundary conditions.

The triangle is simpler — no half-strings, no extra objects.
Each edge is a whole string shared between two cells.

### Impact on ζ counting

Model A: self + D+1 neighbors = D+2 → ζ = 1/(D+2)
Model B: D+1 neighbors only (no self) → ζ = 1/(D+1)

| Dim | Simplex | Model A | Model B |
|-----|---------|---------|---------|
| 2D | Triangle | 1/4 | 1/3 |
| 3D | Tetrahedron | 1/5 | **1/4** |
| 4D | Pentachoron | 1/6 | 1/5 |

**Key result:** ζ = 1/4 (Bekenstein-Hawking) now comes from
the **3D tetrahedron** — the cell type adjacent to horizons.
A horizon is a 2D surface in 3D space; the cells that vote
on its entropy are 3D.  This is more physical than the
previous argument (which used 2D triangles with self-counting).

### Why Model B is preferred

1. No extra objects — the cell is its geometry
2. Edges carry standing-wave modes → entropy → entropic
   gravity (needed for sim-gravity-2)
3. Vertices are junctions (coupling rules), not state holders
4. BH factor from the right dimension (3D, not 2D)
5. Consistent with lattice gauge theory where the physical
   degrees of freedom live on links, not sites

### Status

Adopted as the leading model.  Updated in
[lattice-geometry.md](lattice-geometry.md) and
[foundations.md](foundations.md).  The sim-gravity-2 study
uses Model B's string-register structure.

---

## 2026-03-31: Two planned simulation studies

Both are substantial enough to warrant their own folders
inside `grid/`.  Design notes below; execution is future
work.

### Study A: Gravity from embedding (`sim-gravity/`)

**Question:** does embedding a rigid flat structure in a
relaxed lattice produce a deformation field that falls off
as 1/r?

See [dual-bubbles.md](dual-bubbles.md) for motivation.
Detailed design in [sim-gravity/README.md](sim-gravity/README.md).

### Study B: Wave propagation on the lattice (`sim-maxwell/`)

**Question:** can a small triangular lattice support
directional wave propagation and superposition — the
minimum conditions for hosting Maxwell's equations?

Two candidate approaches:
1. **Standard lattice gauge theory** — use the Wilson
   action equations of motion as the update rule.  This is
   proven to work (it's how lattice QCD is done), but it
   imports formalism rather than testing the "processor"
   picture from scratch.
2. **String-register model** — each node holds a circular
   standing wave (phase state), each edge holds a linear
   standing wave (link state), and the update rule is local
   superposition at junctions.  This tests whether the
   processor/string picture from the INBOX entry above is
   *functional* or merely *conceptual*.

Approach 2 is riskier but more informative.  If it works
(supports directional propagation, not just diffusion), it
validates the micro-instruction picture.  If it fails
(energy sloshes isotropically), it tells us the string
picture needs more structure.

Detailed design in [sim-maxwell/README.md](sim-maxwell/README.md).

---

## 2026-03-31: Transverse vs longitudinal — what vibrates?

### The question

The sim-maxwell and sim-gravity-2 models use scalar
amplitudes on edges (a_fwd, a_bwd).  These are treated as
"waves on strings," but we never specified in what
direction the string vibrates.  Is the model secretly
assuming a transverse wave in a direction normal to the
lattice sheet — a direction that doesn't exist?

### The answer: the amplitude is internal, not spatial

The scattering rule is:

    outgoing_i = (2/N) × total_incoming − incoming_i

This operates on scalar numbers.  It doesn't know or care
whether those numbers represent:
- Transverse displacement (vibration normal to edge)
- Longitudinal displacement (compression along edge)
- An abstract internal quantity (phase, field amplitude)

The rule is derived from energy conservation + equal
impedance.  It's **agnostic about the physical nature of
the amplitude.**  Longitudinal waves would give identical
simulation results.

### What the amplitude actually IS

In the theoretical framework (maxwell.md), the relevant
quantity is the **gauge connection A_μ** — the phase offset
between adjacent cells.  This is not a displacement in any
spatial direction.  It is a scalar value associated with
each link, living in the **internal phase space** of the
cell (Axiom A3: each cell has a periodic phase θ ∈ [0, 2π)).

This internal phase space is:
- **Compact** (periodic, like a circle)
- **1-dimensional** (a single angle)
- **Not a spatial direction** — it's an independent degree
  of freedom, inaccessible to observers living on the sheet

This is exactly the Kaluza-Klein picture: the "extra
dimension" is the internal phase, and gauge fields are the
connection between phases at neighboring sites.

### Why this is not a cheat

1. **The simulations are correct as-is.**  The scattering
   rule is scalar and doesn't reference any spatial
   direction.  No fictitious perpendicular axis is used.

2. **Transverse vs longitudinal is irrelevant.**  Both
   give the same scattering, propagation, and superposition.
   The distinction only matters if you model the amplitude as
   a physical displacement — which we don't need to do.

3. **The "vibration" is in the internal phase space.**  Each
   edge carries a state value (phase/amplitude) that evolves
   according to the scattering rule.  This state lives in a
   compact 1D space — the gauge circle — not in any direction
   normal to the sheet.

4. **The graphene analogy holds.**  In real graphene, the
   electronic properties (Dirac equation, conduction) are
   described by abstract spinor amplitudes, not by physical
   displacements.  The electron wavefunction on the lattice
   doesn't vibrate in a direction — its state evolves.
   Similarly, the GRID lattice edge state evolves; it doesn't
   deflect.

### Implication for MaSt

The compact dimensions in MaSt (the Ma tori) are made from
this same lattice.  The "perpendicular" direction that Ma
occupies relative to Space is not a spatial direction where
strings vibrate — it's the internal gauge degree of freedom
of the lattice edges.  The "rolling up" of a hexagonal sheet
into a Ma torus is a topological identification (periodicity)
of the internal phase space, not a physical bending into an
extra spatial dimension.

This means compactification is genuinely "free" (as noted in
hexagonal.md): the lattice doesn't need to bend in a higher
dimension; it just identifies phases periodically.  The
internal state space IS the compact dimension.

---

## 2026-03-31: Lattice scales — spatial vs internal

### c and the lattice

c is not derived from GRID — it's 1 in natural units by
construction (Axiom A1+A2: Lorentzian causal structure sets
the speed limit at 1 edge per tick).  The SI value of c
reflects the arbitrary ratio of human meters to Planck
lengths.

What IS derived from geometry: the ratio of the EM wave
propagation speed to the causal limit.  On the triangular
lattice, waves propagate at ≈ 0.70 edges/tick; on the
hexagonal, ≈ 0.73.  This geometric factor comes from
junction scattering (energy reflected at each vertex slows
the wave below the causal limit).  In the continuum limit,
this factor is absorbed into the definition of physical
distance.

### Two independent length scales

The spatial lattice spacing is constrained to L_P by the
gravity derivation: Bekenstein-Hawking entropy S = A/4
requires ζ × (A/L_edge²) = A/4, so L_edge = 1 in natural
units = L_P.  This is not a choice — it's pinned by G.

But the internal string length — the extent of each edge's
compact dimension — is a separate, free parameter.  It
determines how many standing-wave modes the edge supports.
This is the size of the compact Ma dimension.

| | Spatial lattice | Internal string |
|---|---|---|
| **What it is** | Distance between nodes in 3D | Extent of compact dimension along edge |
| **Length** | L_P (fixed by gravity) | L_compact (free, = Compton wavelength) |
| **Determines** | G, entropy density | Particle mass spectrum |
| **Constrained by** | Bekenstein-Hawking entropy | Particle masses (empirical) |

The ratio L_compact / L_P = M_Planck / m_particle:
- Electron: ~10²²
- Proton: ~10¹⁹
- Neutrino: ~10²⁸

This naturally explains the hierarchy between the Planck
scale (gravity) and the Compton scale (particles).

### The internal string length doesn't change c

The internal dimension is orthogonal to space.  Traversing
it doesn't move you between nodes.  Spatial propagation
(node to node) takes 1 tick regardless of internal string
length — like rooms connected by doors where the ceiling
height doesn't affect walking speed.

What the internal string length DOES affect: the mass of
particles (nonzero modes).  A massive particle has energy
bouncing in the compact direction instead of moving forward
in space.  The spatial speed is:

v = c × √(1 − m²/E²)

This IS special-relativistic kinematics, now understood as
a geometric effect: part of the energy goes sideways (in
the compact dimension) instead of forward (in space).

### Why massive particles are slower than light

In this picture, the KK mass mechanism and SR kinematics
are the same thing seen from different angles:

- A photon (zero mode): all energy goes forward → speed = c
- An electron (nonzero mode on Ma_e): some energy bounces
  in the compact direction → speed < c
- A heavier particle: more energy in compact modes → even
  slower

This is why E = γmc² — the total energy is the sum of
rest energy (compact-dimension oscillation) and kinetic
energy (spatial propagation).

---

## 2026-03-31: The aether question — inertia as lattice reconfiguration

### Is GRID an aether?

Structurally, yes.  GRID is a fixed substrate through
which EM waves propagate.  That is what "aether" means.

But GRID avoids the problems that killed the classical
aether:

1. **No preferred frame.**  The GRID lattice has Lorentzian
   structure (A2).  In the continuum limit, the dynamics
   are Lorentz-invariant.  There is no "aether wind" — the
   lattice looks the same in every inertial frame.
   Michelson-Morley would see nothing.

2. **Not a substance in space.**  GRID is not embedded in a
   pre-existing space.  It IS space.  You can't move
   "through" it because there's no outside.  Particles,
   fields, and observers are all lattice excitations.

3. **No drag at constant velocity.**  Lorentz invariance
   guarantees that uniform motion costs no energy.  A
   moving object's lattice configuration is just a Lorentz
   boost of the stationary configuration — same entropy,
   same energy (in the comoving frame).

### But there IS a cost to acceleration

When a mass accelerates, its gravitational field (the
pentagonal defect distribution in the lattice) must
rearrange.  The curvature pattern — the distribution of
pentagons and heptagons — must sweep through the lattice,
redistributing defects to accommodate the mass at each
new position and velocity.

This rearrangement has a cost.  As v → c:
- The gravitational field Lorentz-contracts
- Pentagon defects concentrate into a narrower region
- The lattice must reconfigure faster and faster
- At v = c, the reconfiguration must happen at the causal
  speed limit — which it can't, because you'd need to
  move defects faster than information travels

**This is why mass can't reach c:** the lattice has a
finite causal speed for reconfiguration.  The c limit is
not an imposed rule — it's a consequence of the lattice's
causal structure.  The energy cost of maintaining the
contracted curvature pattern diverges as v → c because the
lattice literally can't rearrange fast enough.

### Inertia = lattice reconfiguration cost

The relativistic kinetic energy E_kin = (γ − 1)mc² can
be reinterpreted as the energy stored in the lattice
reconfiguration:

- At rest: the pentagonal defect pattern is symmetric
  (Schwarzschild curvature, spread over 4π steradians)
- In motion: the pattern is Lorentz-contracted (concentrated
  perpendicular to motion, compressed along motion)
- The energy difference between these configurations is
  the kinetic energy

Inertia — the resistance to acceleration — is the lattice's
resistance to having its defect pattern rearranged.  A
heavier mass (more defects, deeper gravity well) requires
more rearrangement → more inertia.  This is not metaphor;
it is the mechanical content of the Jacobson derivation
applied to moving objects.

### The Unruh connection

An accelerating observer sees thermal radiation at
temperature T = a/(2π) (Unruh effect).  In the lattice
picture, this is the thermodynamic signature of forced
lattice reconfiguration.  The "heat" of the Unruh bath IS
the entropy production from pushing pentagonal defects
through the lattice faster than they would naturally
rearrange.

- Constant velocity: no Unruh radiation, no entropy
  production, no "friction" (Lorentz symmetry)
- Acceleration: Unruh radiation, entropy production,
  energy cost (lattice reconfiguration)
- The Unruh temperature is the "temperature of the aether
  friction"

### Is this calculable?

Potentially.  The entropy cost of redistributing
pentagonal defects around a moving mass could be
computed from the pentagon density formulas in
sim-schwarzschild, combined with the Lorentz contraction
of the Schwarzschild geometry.  The integral would be:

    ΔS = ∫ [S_defect(r, v) − S_defect(r, 0)] dV

where S_defect is the entropy associated with the
pentagonal defect density at radius r.  If this integral
reproduces (γ − 1)mc² / T_Unruh, it would provide an
independent lattice-level derivation of relativistic
kinetic energy.

This is a potentially significant calculation — it would
connect the lattice's geometric structure (pentagons) to
the kinematic structure (Lorentz factor γ) through
thermodynamics.  Framed as a possible future study:
**sim-inertia**.

### What's new vs what's restating GR

| Statement | New? |
|-----------|------|
| Speed limit c from lattice causality | Gives a mechanical reason for SR; the content is equivalent |
| Acceleration costs energy | Restates relativistic mechanics; identifies mechanism as lattice reconfiguration |
| Unruh radiation as aether friction | Known in QFT; lattice interpretation (pentagon redistribution) is new |
| Inertia from defect rearrangement cost | Potentially calculable and new; connects geometry to kinematics via thermodynamics |
| γ divergence from causal reconfiguration limit | New framing — the speed limit is the lattice's finite processing speed |

---

## 2026-03-31: One grid or many? Particles and frames

### The question

Do particles move *through* the grid, or does each particle
have its own grid?

### Current GRID picture (one grid)

As formulated, there is one lattice.  Particles are wave
patterns propagating across it — like ripples on a pond.
The ripple doesn't carry water; it propagates through the
water.  A particle "moving" is just the pattern shifting
from one set of edges to the next.

### The "private grid" hypothesis (speculative)

An alternative framing: each particle's internal state
space (its compact-dimension string, its standing-wave
modes) constitutes its own "quantum address space."  The
particle doesn't see the grid directly — it sees its own
internal state evolving.  The grid is the substrate, but
the particle's experience is mediated entirely by its
internal modes.

If each particle has its own internal frame defined by its
compact-dimension state, then:
- c is constant for every particle because each particle's
  internal dynamics run at the same rate (one mode update
  per tick) — the grid's causal speed is the same for all
- Lorentz invariance doesn't need to be "proven" on the
  grid as a whole; it follows from each particle's internal
  state being unable to detect absolute motion through the
  grid (the internal modes are scalar — they don't know
  which direction the pattern is moving in space)
- This connects to MaSt: each particle IS a standing wave
  on its own compact geometry, and the compact geometry is
  the particle's "private grid"

### Open questions about this framing

1. **Lorentz invariance is assumed (A2), not derived.**
   GRID has not proven that the lattice looks the same in
   every frame.  In lattice gauge theory, Lorentz invariance
   is recovered in the continuum limit — but exact Lorentz
   invariance on a discrete lattice is impossible (the
   lattice picks out preferred directions at the Planck
   scale).  This is a known issue with all discrete models.

2. **One grid vs many grids is a question about QM
   foundations.**  In standard QM, all particles share one
   Hilbert space (one wavefunction for the universe).  In
   relational QM (Rovelli), each observer has their own
   perspective.  The "private grid" idea aligns more with
   the relational view.

3. **Testability:** if the grid has preferred directions
   at the Planck scale, there could be tiny Lorentz-
   violating effects.  Gamma-ray astronomy places extremely
   tight bounds on such effects — no violation detected
   to date.  This is consistent with GRID (Lorentz
   invariance recovered in the continuum limit) but does
   not confirm it.

### Status

Speculative.  The "one grid, particles are patterns on it"
picture is more conservative and sufficient for all current
GRID results.  The "private grid" picture is an interesting
alternative framing that might connect to the measurement
problem and relational QM, but has no computational
consequences yet.
