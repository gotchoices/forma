# Grid Couplet
Brainstorming

## Observations
- Before running grid-primitive, we experimented with several types of primitive structures.
- For example viz/grid-lab analyzed the relationship between edges and nodes.  This had a two-phase master clock.  On alternate clock phases, edges and nodes respectively would recalculate their value based on the values of their neighbors.
- grid-primitive took a different approach: A single edge took on both edge (linear, magnitude) and node (circular, phase) characteristics.  As a further allusion, it is noted that a cylinder looks like a segment from the side and a circle from the end.  It has dual character (not sure if this should be added somewhere into the grid-primitive project itself).
- grid-primitive was fairly successful but may have gone to a lot of effort in modeling a continuous, mechanical behavior which may actually be the result of a fractal stack of discrete properties.
- The grid-primitive approach feels like an "analog-first" model where we try to understand the system based on the individual actions of edges that are connected in a coherent grid, but otherwise fairly independent to compute values internally in a pseudo-mechanical way, based on their neighbors.
- This project will take on more of a "digital-first" model where the primitive components will obey a "master clock" with two clock-phases, edges acting on one clock-phase and nodes acting on the other clock-phase.

## Hypotheses to Test and Properties to Derive
- There are two primitives we will call edge and node.
- Edges are linear, nodes are periodic (circular or at least logically circular).
- Edges are unbounded and have a sense of their polarity, indicated by a head and a tail.
- Nodes are bounded in the range of 0 - 2pi.
- A node can be modeled as and even number of 2 or more edges (presumably, at the next lower/smaller level of fractal recursion) aligned in a linear array head-to-tail in a periodic (2pi) wrap or loop.  As an example, 2 edges might be joined head to tail in the smallest configuration possible.  Three edges could form a square.  Six edges could form a hexagon.
- This wrapping limits the set of internal node states to those that are self-consistent around the circle.  In general, the last half of the circle will have to hold complementary values to what the first half holds.  In this way, the values will return to the starting point as 2pi is reached.
- This wrap is likely analogous to wrapping a 2D sheet but it is a linear array of edges 1D, wrapping into a logical circle.
- It is unclear whether a functional edge can be analogously created from some sort of array of nodes.
- If it is possible, I would like to identify that configuration and compare it to the node-from-edges configuration.
- If it is not possible, I would like to prove _why not_.  I have a hunch that it is possible to limit an unbounded system to a bounded one, but that there is some entropy that occurs in the bounding that prevents the creation of an unbounded system solely from bounded components.  But I'm open minded on this.  I'd like to discover the true answer.
- Having characterized the edge and the emergent node, I'd like to posit a couplet consisting of the two as the functional primitive for the grid.
- It is intuitive (as in viz/grid-lab) to create a 1D linear array of couplets.  It is also intuitive that the end can always couple to the beginning as they will be opposite in nature (node to edge).
- It is less intuitive whether a 2D sheet can _always_ be created from couplets exactly.  Specifically, does this work:
  - Start with a single couplet, edge on the left, node on the right
  - The location on the node where it meets the edge is zero by definition
  - Imagine each node as a hexagon
  - At orientations 2pi/3 (120) and -2pi/3 (240), we position two more couplets to form a split
  - These split again, and so forth
  - Is it _always_ the case that I can wrap the sheet (first, assuming no shear) periodically in both directions and that there will always be room for full couplets to be added until the sheet is fully continuous?  IOW, there is never a case where two edges come together without an intervening node or vice versa?  The sheet always can be described as a discrete number of couplets whose constituent edge and node can be said to belong exclusively to that couplet?
- We have a routine already in viz somewhere for computing minimal tori in this configuration.  It may be of some help.
- Does any special insight into alpha come from the wrapping process when we build a node from (6) edges?
- Is there a phenomenon analogous to "leakage" that is observable/computable in this minimal 2pi wrap?
- This is not charge emergence (which happens with a 2D sheet wrap).  It could arguably be construed as mass emergence but likely at the next level down.  Perhaps alpha comes into play only when one wrap becomes two?  I don't think that is what the original grid derivations claimed explicitly, but maybe it is buried in the math somewhere.  Is there an alpha phenomenon when light is promoted to mass or only when mass is promoted to charge?
- Perhaps our first 1D wrap is literally the wrap that promotes information to light (information with a direction).
- If wrapping is what brings about _promotion_ (information -> light -> mass -> charge), then is there a _leakage_ analog at each level or is it unique to the mass -> charge level and why?

## Other Thoughts
- It is probably trivial to extend this structure to the regular derivations in grid/*.md.  However, we should provide the bridge if/where it is not obvious.
- I think grid explicitly assumes the phases (clock faces) and sort of implicitly computes the edges (the differences).  We should confirm if this is correct.
- We should derive the simplest set of update rules for edges and nodes.  I like the convention that on a (negative, reflective, inhalative) clock-phase, the nodes gather information in and on the (positive, assertive, exhalative) clock-phase, the edges assert their new values.  Does this match what is in viz/grid-lab?
- If this project is successful, a natural outgrowth would be to finish the visualizer grid-lab so it can selectively render 2D arrays wrapped as tori.
- The word primitive will likely refer to an edge, but a node would be some sort of emergent structure, and the couplet would become another emergent structure.  Then, the goal would be to build every larger structure from exactly couplets, rather than calling upon any lower structures (edges or nodes).
- I think a couplet can contain a fully characterized, directional perturbance (likely in either direction).
