# A Model For a GRID Primitive
Brainstorming

## Project Objectives
- Derive a mathematical model for the grid and its primitives
- Verify that the derivation still produces Maxwell's equations correctly
- Verify that the derivation still produces entropic gravity (Jacobson)
- Explain, in this interpretive model, what role alpha plays/explains at the most primitive level possible

## Summary
- forma/dialogs/grid-3.md contains a dialog exploring possible models for the grid lattice
- Grid contemplates a 2D sheet or a 3D space of interconnected grid edges and nodes
- Various models have been explored
- Of particular interest is how alpha might be either derived or at least explained in terms of grid geometry
- The dialog explores several specific areas of interest:
  - How to properly encode wave information, magnitude, phase in a lattice?
  - How this might be done on a discrete, digital model (2-phase clock with separate update rules for edges, nodes)
  - How this might be done with a continuous, mechanical model (each edge is a cylindrical edge with 2 DoF, linear compression, radial angle in 2pi of force/deflection, nodes are passive connectors)
  - In each of these models, how might alpha manifest itself as some ratio or characteristic of the geometry
- The model I like the best is the continuous, flexible cylinder.  I like that it can be modeled as another layer of 2D grid lattice wrapped into a cylinder.
- Each edge is both a linear edges and a circular cross-section, incorporating both magnitude type and phase type information in a single primitive.
- It turns out that shear in the wrap of the edge cylinder is needed in order to make a continuous system behave like the discrete clock-driven model.  The edge has two characters, compression and radial direction (phase) but they are intertwined such that each one drives the other.
- In the dialog, it sounds like ideal shear is 1/sqrt(2)?  However, this also degenerates somehow?  We need to understand that better.  The idea that magnitude and phase (yang and yin) both hold an equal share of the job, is appealing.  Not sure if non-precise (not exactly 45 degrees) also implies that B and H don't have exactly equal roles.
- Grid has shown that a wrap of 2pi results in charge.  In the original grid derivation, this seems a little mysterious.  We have made several efforts to explain this in a more fundamental way.  Some sub-objectives:
  - Interpret alpha showing that wrapping the surface creates a small efficiency so that the standing wave can be maintained in the compact dimension with only 136/137 of the original energy and 1/137 of the energy is available to produce the emergent static electric field.
  - Show that any bend produces a "leak" of energy that is a function only of the bend angle (rate/radian)
  - Show that the leak rate (alpha) does not depend on the size of the wrap, only the fact that there _is_ a wrap.
  - One possible interpretation: The wrap occurs in discrete steps.  At each step, there is a discontinuity that causes a small amount of energy to _escape_.  This leak constitutes _excess_ energy due to efficiencies related to the wrap.
  - Another interpretation: The wrap is a continuous bend.  Since the edge has non-zero thickness (it is a nanotube structure), this puts inner sub-edges in compression and outer sub-edges in tension.  This results in a calculable concentration of energy toward the inside of the wrap and some type of emission outward.
  - In both interpretations, it is theorized that the _escape_ component results in some type of DC eddy light currents in hexagonal loops on the larger 2D wrap.  This results in some type of emergent E field (the static charge).
  - Even in the _continuous_ interpretation, the phenomenon is still quantum at the sub-edge level because the edge is made up of a discrete set of sub-edges.

- Two derivations/solutions:
  - Grid is a lattice of edges (in 2D or 3D) where each edge is itself a grid lattice cylinder (like a carbon nanotube in structure).  Two qualities need to be kept, related to E and B.  We have a model where both can be different qualities of a single edge.  We can solve for a shear value that makes the system work.
  - Alpha (energy leak) is a result of bending a lattice sheet and is a result of the thickness of the edges themselves or the discrete bending points.  We can compute alpha as a function of shear and tube circumference.

- Using these two derivations, can we arrive at a tube thickness based on an optimal selection of shear?

## Gravity concern
- In another context (see viz/grid-lab), it was determined that the _entropy_ required for the grid to produce gravity, comes from the fact that the phase variable is bounded at 2pi.  It was my intuition (possibly wrong) that the entropy comes from the phase "throwing away" information about any wrapping (probably a Q file on this).  The file dialog/grid-3 does not support this notion.
- The "throw away" concept may be wrong.  That's fine.  But the grid _must_ produce gravity according to grid's original derivation (sim-gravity).  Otherwise, our mechanical model is of no use.


## Style
- This project should follow the style of metric-mass
- IOW, the goal is not to assert a theory
- Rather, we should start from a set of fundamentals and proceed with a derivation that _discovers_ or _yields_ the desired output.
- This is a bit of a cheat because we already know where we are headed
- But we want the narrative to feel interesting and like a discovery process.
