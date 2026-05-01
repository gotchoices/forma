# Grid Laboratory Specifications

## Purpoose
This is for visualizing various versions of the grid lattice

## Viewer
The viewer is 3D and will build structures the user can zoom and pan around to see.
Use the standard visualizer componentry where possible.
User settings should be savable under a named profile and selectively restored by that name.
For purposes of this spec, x and z form the horizontal plane, y is up and down.

## Dimensions and primitives
We will build simple structures from scratch that can evolve from 1 to 2 to 3 dimensions.
- The simplest building block (primitive) consists of an edge or a node.  We'll call this 0 dimensional.
- To build structures, we connect nodes to edges in a graph network.
- Each edge holds a value that behaves like a magnitude, a real number, positive, negative, or zero
- Each node, a circle, holds a value that is periodic, settable in degrees or radians, also real.
- The length of nodes and the diameter of circles is set to a default value of 1 each.  But these values are independently settable, but global (applies to all edges and nodes in the graph).
- The node value is globally configurable to accumulate or not as it crosses the periodic boundary.  In accumulation mode, the value is unbounded — 360 → 361 is allowed, and values like 720 or -270 are valid.  In wrap mode, the value lives strictly in the half-open range [0, period): zero is valid, but the period itself (360° or 2π) is **not** — it is identical to zero and must fold back.  Implementations must enforce this so that floating-point noise near the period also snaps to zero; the user should never see a displayed 360 (or 2π) in wrap mode.  So the sequence is 358 → 359 → 0, never 358 → 359 → 360 → 0.
- The simple node and edge lay flat in xz so the line is along x and the node circle is in the xz plane, centered on x.  The edge intersects the circle normal to the circle
- To build a linear array of primitives, we repeat the (node, edge) unit cell N times along an axis: an array of N units has N nodes and N edges.  In an open chain (not periodic), the trailing edge has no head node — it is visualized as a stub for unit-cell symmetry but is inert (it does not participate in the update rules and is not seen by any node).  When the chain is periodic the trailing edge closes the loop, connecting node N-1 back to node 0.
- Each node has an angular orientation where (for a 1D array) 0 points in the -x direction.  So each new node connected to the array connects to the previous edge at its own 0 point.  The 180 degree point (+x direction) will be where the next edge will connect to this node.
- Likewise, each edge has a directional orientation, a tail and a head.  In the 1D case, each edge has its tail in -x and its head in +x (connecting to each new node).
- The chain has two independent boolean properties: *periodic* (logically closed, the trailing edge connects back to node 0) and *wrap* (visually rolled into a ring).  Periodic without wrap leaves the array drawn flat with the trailing edge as a stub, but the engine still treats it as connected to node 0.  Wrap rolls the chain into a vertical ring — picture a ferris wheel with its axle along z, the wrap circle in the xy plane, centered at the origin, with nodes spaced around its rim at the wheel's radius (derived from the array length).  Going from one node to the next is a small rotation about the z axis.  Each node circle reorients so its normal points radially outward from the axle, and edges curve along the rim, tangent to the wheel.  In wrap mode without periodic, the trailing edge is hidden and the visible chain forms an arc with one segment missing.
- The controls allow one to build a linear array with a specified number of unit cells (N), mark the array periodic, and toggle the visual wrap independently.  When wrapped, the diameter of the circle is derived from the number of unit cells.

## Clock
- There is a master clock that displays as 0 or 1
- It is controllable by single (half) stepping or with a run/stop button and a settable speed control
- There are two clock edges:
  - 0→1 (exhale, yang): information flows outward from nodes to edges
  - 1→0 (inhale, yin): nodes gather information from their edges

## Update rules
Each type of primitive has its own local update rule.  
The purpose of the update rule is to calculate the primitive's next value as a function of its inputs, the present values.

Update rules consider only:
- The current state of the primitive's value
- The current state of its neighbors' values
- A settable coupling value which will initially default to 1 (full coupling)
There can be multiple versions of the update rules.  A global setting decides which update rule version is in play.

## Version 1 Update rules
Node:
- On inhale, my next value is the sum of:
  - Each connected edge's value, times cos(phi) where phi is the angle where the edge connects to the node.  As an example, a node is connected by two edges, one to the left (-x) and one to the right (+x).  If the edge to the left has value 3 and the one to the right has value 2, the new node value will be 3 - 2 = 1.
- On exhale, do nothing.

Edge
- On inhale, do nothing.
- On exhale, my next value is the sum of the two nodes I am connected to

Coupling value
In the version 1, the individual coupling constant will not be used.  Later, it will become a function of the bending angle between primitives.  Keep it stubbed in, but do not consider it yet in the calculation.

## Version 2 Update rules

Yee-style additive coupling.  Each update *adds* a contribution from neighbors to the primitive's current value rather than replacing it.  Combined with the staggered geometry — nodes at integer positions, edges between them — this yields stable, linear wave propagation: a perturbation travels along the array in a definite direction, and two perturbations launched from opposite ends pass through each other without disrupting each other.

Node:
- On inhale, my next value is my current value plus the sum of:
  - Each connected edge's value, times cos(phi) where phi is the angle where the edge connects to the node, divided by the translation factor k.  As an example, a node currently at phase 10, connected by two edges (left at -x, phi=0, value 3; right at +x, phi=180°, value 2), becomes 10 + (3 − 2)/k.
- On exhale, do nothing.

Edge
- On inhale, do nothing.
- On exhale, my next value is my current value plus k times (the value of my tail node − the value of my head node).  The sign convention follows from stability: the edge stores a flux/gradient pointing from high-phase tail to low-phase head, so a positive tail-minus-head difference grows the edge value.  As an example, an edge currently at value 4, running from node A (tail, phase 30) to node B (head, phase 50), becomes 4 + k·(30 − 50) = 4 − 20·k.

Coupling value
Same stub as v1 — present in state, defaulting to 1, not yet used in the calculation.  When activated it will modulate the per-edge contribution as a function of the bending angle between primitives.

## Primitive scaling
To translate values between primitives (edges and nodes), including a global translation value that is settable.  Default = 1.  This translates magnitudes to angles and vice versa.  Node phase is derived by dividing the sum of its inputs by the translation factor.  Edges multiply to get their value.  This is uniform across update versions.

## Rendering
Each edge should be rendered as a heatmap or color.  A global setting can determine scaling, specifying the range of allowable values.  Values that overflow or underflow the heat mapping should saturate.  Zero should be mapped to a color in the middle of the spectrum, allowing positive and negative colors to map to hot and cold colors according to the selected scaling.  If the graph looks saturated, the scaling can be adjusted.  A checkbox should be available for auto scaling where the scaling method will adapt to values on the graph according to some slow update method.

Each node should be a uniform color but have a bright dot to indicate its current phase.  The dot is positioned over the correct location on the circle.  In cumulative mode, the base color of the node circle will change color according to scale (i.e. 0-360 is neutral, 361-720 is hotter, -360-0 is cooler).

In addition to graphical rendering, each primitive shall be able to display a numeric value.  These should be legible at a single font regardless of zoom value and display in proximity, to the primitive and always right-side-up regardless of the primitive's rotation.  Near center of mass for each primitive is a good place for the numeric display, slightly elevated in y for edges (so it isn't buried in the edge thickness).  Numeric display may be turned on/off globally.

## Initial Conditions
The user can click on a primitive to set its value.  A small popup box will accept the value and write it in.  There is also a global clear button to reset all values to zero.

A pulldown menu offers preloaded initial states for common test cases.  Selecting a preset clears the chain and overwrites all values.  In each delta-style preset, both a node phase and an edge value are set: in periodic mode the edge value is needed to cancel the would-be opposite-direction branch and yield a clean directional pulse, and in an open chain the boundary already breaks symmetry so the edge seed is cosmetic but kept for consistency.

- **Delta L** — single impulse at the left end set up to propagate right.  Sets node 0's phase and the trailing edge's value (positive sign).
- **Delta R** — single impulse at the right end set up to propagate left.  Sets node N-1's phase and the trailing edge's value (negative sign — opposite to Delta L).
- **Delta 2** — both Delta L and Delta R simultaneously, so the two pulses meet and pass through each other in the middle.  Both endpoint nodes are set; the trailing-edge contributions cancel and it remains zero.
- **Sin** — a smooth sinusoidal traveling-wave initial condition: nodes carry a cosine pattern around the chain, and edges carry the matching half-cell-shifted sine pattern (so on a periodic ring at k=1 it propagates right at one cell per cycle without distortion).

In later iterations, we will add additional injection presets (Gaussian wavepackets, multi-mode mixes, etc.).

## MVP
For first iteration, we should be able to build the 1D array of specified length and optionally wrap it into a ring (ferris-wheel orientation).  Further, higher degrees will be deferred for now.
