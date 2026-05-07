# Grid Laboratory Specifications

## Purpose
This is for visualizing the GRID lattice as it is now understood: a network of nodes and edges that exchanges information through a *register / scattering* model.  The visualizer lets you build 1D, 2D, and 3D arrays, optionally make any axis periodic, optionally roll a periodic axis into a visible loop or torus, drive the lattice with the master clock, and watch waves propagate.

The model implemented here is the one selected by [grid-duality chapter 4](../projects/grid-duality/04-model-comparison.md): **Scattering**, specified in [grid-duality/models/scattering.md](../projects/grid-duality/models/scattering.md).  The Python implementation in [grid-duality/scripts/models.py](../projects/grid-duality/scripts/models.py) is the reference of record; this visualizer is a JavaScript port of the same algorithm.  Any divergence in observable behavior is a bug in the port.

## Viewer
The viewer is 3D and lets the user zoom and pan around the structure. Use the standard visualizer componentry where possible (`createScene`, `autoResize`, `animLoop`, `PALETTE` from [`totu-viz.js`](totu-viz.js)).

User settings save under a named profile and selectively restore by name.

For purposes of this spec, x and z form the horizontal plane, y is up and down.

## Substrate

Two structural primitive types:

- **Node** — a vertex in the lattice graph.  Renders as a flat circle (a torus mesh), normal aligned with the local viewing plane.
- **Edge** — a connection between two nodes.  Renders as a thin tube between the two nodes' rims.

The substrate **does not** distinguish "A-nodes" and "B-nodes" or any other functional sublattice.  Every node is the same kind of object; every edge is the same kind of object.  The geometric distinction in 2D — some wye-junctions point up, some point down — is purely a property of how the hex lattice tiles, not a difference in the dynamics of the nodes.

### Registers (where the state lives)

Each edge has two ends.  Each end *docks into* the node it connects to, forming a **register** — the meeting point between an edge end and a node.  A register holds a single real-valued number; that real number is the lattice's only stored state.

- An edge contributes **two registers** (one at each end).
- A node hosts **one register per incident edge**.  A node of coordination N has N registers.
- The register is owned jointly: the edge contributes the *end*, the node contributes the *socket*.  It is not a third primitive type — it is a derived structural element built from the two foundational ones.

This replaces the older "node carries a phase, edge carries a magnitude" framing: there is no longer a per-node phase or a per-edge scalar.  All state is in registers.

The total state count for any topology is exactly **2 · |edges|** real numbers, equivalently `Σ_node (coord of node)` since every edge contributes to two nodes.

### Edge polarity

Edges have a logical tail and head used as a layout convention (e.g., "the rightward edge in 1D").  The *Scattering dynamics does not use polarity* — both registers of an edge are unordered with respect to it.  Polarity is retained only as a labeling convenience for presets and rendering anchors.

## Dimensions

The visualizer supports three lattice dimensions, each with its own neighbor topology.  Higher dimensions are added in stages (1D first, then 2D, then 3D).

### 1D — linear chain

- N nodes spaced along the x axis.
- Open: N nodes, **N − 1 edges**.  No dangling stubs.  Boundary nodes have coordination 1.
- Periodic: N nodes, **N edges**.  Every node has coordination 2.  The wrap edge connects node N − 1 back to node 0.

The simple node and edge lay flat in xz so the chain runs along x and each node circle's plane is in xz, normal up (y).  The edge intersects the circle from outside.

When **periodic** but **not wrapped** visually, the chain is drawn flat and the wrap edge is rendered as **two short half-edge stubs**, one extending past each end of the chain, faded slightly so the eye reads them as "this connects around to the other side."  The two stubs together represent the single wrap edge logically.  When **periodic** *and* **wrapped**, the chain rolls into a vertical ring (ferris wheel: axle along z, ring in the xy plane, nodes spaced around the rim).  When **open** *and* **wrapped**, the chain is rolled into an arc with one rim segment missing.

### 2D — hex / wye sheet

Each interior node has coordination 3, with three edges meeting at 120° angles.  The lattice tiles the plane in a hexagonal pattern: when viewed by its hex *openings*, the pattern reads as hexagons; when viewed by the wye-junction at each node, the pattern reads as alternating Y and inverted-Y junctions (some nodes have one edge pointing up and two pointing down, others one edge pointing down and two pointing up).  These up- and down-wyes are *geometric mirror images*, not functionally different objects.

Layout: nodes lie in the xz plane (y = 0); the lattice runs `nx` cells in one lattice direction and `ny` in the other.  Periodicity is per-axis: x can be periodic, z can be periodic, both, or neither.

When an axis is **periodic** but **not wrapped**, the wrap edges along that axis are rendered as short half-edge stubs at both ends of each affected row (1D treatment generalized).  When an axis is **wrapped** as well, that axis is rolled into a ring, and the sheet curves into a cylinder.  When *both* axes are periodic and wrapped, the sheet closes into a **torus**.  The torus geometry is computed so that the lattice tiles the surface cleanly — the major and minor radii are derived from `nx` and `ny` so that plaquettes close exactly when mapped onto the torus surface, no visible seam.

### 3D — diamond lattice

Every node has coordination 4, with four edges at the tetrahedral angle (~109.5°).  The lattice tiles 3D space in the same connectivity pattern as the carbon atoms in diamond.

Per-axis periodicity is independent (x, y, z each toggle).  Each periodic axis can independently be wrapped.  All three axes wrapped gives a 3-torus; visualizing this involves nesting three concentric loops and is sketched only after the 1D and 2D cases are working.  See [`nested-torus.html`](nested-torus.html) for the visual idiom.

## Clock

A master clock displays as `0` or `1`, controllable by half-stepping or run/stop with a settable speed.

Two clock edges:

- `0 → 1` (**exhale**, yang) — each edge transmits its two ends' values to one another.  The effect is a **swap** of the values in the edge's two registers.  Synchronous across the lattice.
- `1 → 0` (**inhale**, yin) — each node samples its registers, applies the **scattering matrix** S = (2/N)·J − I where N is the local coordination, and overwrites the registers with the result.

One full cycle (inhale + exhale) is one time tick.  An exhale is **one edge transit** — that is the **speed of light** on the lattice.

## Update rules

There is one update rule, derived from the two physical constraints any junction must enforce: voltage continuity (all incident lines see the same potential at the junction) and Kirchhoff current conservation.  The matrix S = (2/N)·J − I is the *unique* solution to these constraints at an N-port equal-impedance junction.

**Inhale (node).**  At each node of coordination N with registers r₁, …, r_N (in any local ordering):

> r_i ← (2/N) · (r₁ + r₂ + … + r_N) − r_i      for each i = 1, …, N

**Exhale (edge).**  For each edge with end-A register r_A and end-B register r_B:

> r_A, r_B ← r_B, r_A      (swap)

Both phases are *unitary* — exactly energy-preserving (Σ r_i² is conserved per cycle to machine precision).  Unit time step is stable for any coordination; no normalization or sub-stepping needed.

For interior 1D nodes (N = 2): inhale sends (r₁, r₂) → (r₂, r₁).  Combined with the exhale-swap on edges, one full cycle moves the value pattern by one cell (in either direction, depending on the channel).

For 2D hex / wye junctions (N = 3): the diagonal of S is −1/3 (reflection coefficient at a junction) and the off-diagonal is 2/3 (transmission to each of the two other ports).  This matches the matched-impedance scattering result that grid-duality verified to four decimals.

For 3D diamond (N = 4): diagonal is −1/2, off-diagonal is 1/2.

For a coordination-1 boundary node: S = 1 (identity).  A boundary register reflects perfectly back through the edge — equivalent to an open-circuit termination on a transmission line.

There is no separate "v1 / v2 / cos-weighted" rule selector.  The earlier candidates (v-i Telegrapher, normalized telegrapher, RelCos-both, cos-weighted) are documented in [grid-duality/02-candidate-models.md](../projects/grid-duality/02-candidate-models.md) but are not implemented here.

## Coupling factor

A global coupling constant `c` (default 1) is stubbed into engine config for future use.  At c = 1 the dynamics is exactly the Scattering model above.  Future extensions may modulate the per-edge swap by a coupling that depends on the bending angle between adjacent edges; this is not active in MVP.

## Rendering

### Edges

Each edge renders as a tube between two nodes (or two stubs in periodic-but-not-wrapped mode).  The tube is **split into two halves**, one for each register.  Each half is colored by a heat map of its register's value:

- Zero is mid-spectrum (neutral).
- Positive values warm toward red/orange.
- Negative values cool toward blue.
- Out-of-range values saturate.

The split point is at the midpoint of the edge, so each half visually attaches to the node it docks into.  An optional refinement is a smooth gradient interpolation across the midpoint instead of a hard split; the engine treats the two registers as independent values, so the visual choice is purely cosmetic.

A global heat range slider sets the saturation thresholds.  An auto-scale checkbox slowly adapts the range to the current maximum register magnitude on the lattice.

### Nodes

Each node renders as a circular ring (torus mesh) in its local plane.  The ring is divided into **angular sectors**, one per incident edge, each sector spanning the arc nearest its register.  Each sector is colored by the same heat map applied to the corresponding register.  This makes the value continuous across the node-edge boundary — the edge half and the node sector that share a register show the same color.

For nodes of coordination 1 (1D boundary), the sector spans the side of the ring facing the connected edge; the rest of the ring is neutral.

If sector subdivision proves visually fussy, the fallback is a single uniform color per node ring with sector colors deferred to a future iteration.

### Numeric labels

Each register can display a numeric value, positioned near the edge end that hosts it (i.e., near the corresponding node, not at the edge midpoint).  Labels render at a constant font size in screen space, always upright regardless of camera orientation.  Numeric display toggles globally.

### Half-edge stubs (periodic, not wrapped)

When an axis is periodic but not visually wrapped, the wrap edges render as short half-stubs extending past the boundary nodes.  Each stub is a single-tube half-edge in the boundary node's outward direction, faded slightly (e.g., dashed or 60% opacity) and labeled with an arrow or short text indicating which node it logically connects to.  Two stubs per wrap edge — one at each end — together represent the single logical edge.  Their two register values are still part of the engine's state and can be read off the stubs.

## Initial Conditions

Click any primitive — a register on a node or an edge half — to open a popup that sets its value.  A global Clear button zeros every register.

A pulldown menu offers preloaded presets.  Each preset clears the lattice and overwrites register values:

- **Delta L** — single rightward-traveling unit pulse seeded at the left end of the chain.  Sets the rightward-channel register at node 0 (the head-end register of the wrap edge, if periodic, or of the leftmost edge in open mode) to a unit amplitude.
- **Delta R** — symmetric to Delta L, leftward-traveling, seeded at the right end.
- **Delta 2** — both Delta L and Delta R simultaneously, so the two pulses meet and pass through each other.
- **Sin** — a smooth right-going sinusoidal traveling wave: registers along the rightward channel carry a sine pattern around the chain, leftward-channel registers are zero.  On a periodic ring this is an exact eigenmode and propagates without distortion.

In later iterations, additional presets (Gaussian wavepackets, multi-mode mixes, Y-junction probes for 2D) will be added.

## MVP and refactor plan

Per the user's intent, the refactor proceeds in three steps:

1. **1D only** — port engine, tests, and visualization to the register / Scattering model on the existing 1D chain.  Drop v1/v2 selector, per-node phase, per-edge magnitude, accumulate-mode, units, and k.  Validate energy conservation and pulse propagation.  *(This MVP step.)*
2. **2D** — add a `build2D(nx, ny, { periodic_x, periodic_y })` builder, hex/wye geometry, optional torus wrap, half-edge stubs for unwrapped periodic axes.
3. **3D** — add a `build3D(nx, ny, nz, …)` builder for the diamond lattice, with per-axis periodicity and wrap; nested-torus visualization for fully wrapped 3D.

After each step the visualizer should remain usable end-to-end; later steps don't break earlier ones.
