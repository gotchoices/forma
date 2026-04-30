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
- The node value is globally configurable to accumulate or not as it crosses the periodic boundary.  In accumlation mode, it goes from 360 to 361, for example, a value of 720 or -270 is possible.  In wrap mode, it goes from 359 to 0, there is no 360 or 2pi value as this is equivalent to zero.
- The simple node and edge lay flat in xz so the line is along x and the node circle is in the xz plane, centered on x.  The edge intersects the circle normal to the circle
- To build a linear array of primitives, we repeat the node-edge-node-edge-node along an axis
- Each node has an angular orientation where (for a 1D array) 0 points in the -x direction.  So each new node connected to the array connects to the previous edge at its own 0 point.  The 180 degree point (+x direction) will be where the next edge will connect to this node.
- Likewise, each edge has a directional orientation, a tail and a head.  In the 1D case, each edge has its tail in -x and its head in +x (connecting to each new node).
- A 1D linear array can be wrapped into a circle, making it periodic.  This is done by forming a circular array in xy.  A single node will be centered at the origin and flat in xz.  The nodes that connect to it will be rotated slightly in y to go to the next node.  This will form a circle of nodes and lines where the normals of the node circles point out radially from a cennter point.
- The controls allow one to build a linear array with a specified number of nodes.
- The controls also allow selectively to wrap the array into a circle.  The diameter/radious of the circle is derived by the number of primitives in the array.

## Clock
- There is a master clock that displays as 0 or 1
- It is controllable by single (half) stepping or with a run/stop button and a settable speed control
- There are two clock edges: 0-1 (inhale)
- There are two clock edges: 1-0 (exhale)

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

## Primitive scaling
To translate values between primitives (edges and nodes), including a global translation value that is settable.  Default = 1.  This translates magnitudes to angles and vice versa.  Node phase is derived by dividing the sum of its inputs by the translation factor.  Edges multiply to get their value.  This is uniform across update versions.

## Rendering
Each edge should be rendered as a heatmap or color.  A global setting can determine scaling, specifying the range of allowable values.  Values that overflow or underflow the heat mapping should saturate.  Zero should be mapped to a color in the middle of the spectrum, allowing positive and negative colors to map to hot and cold colors according to the selected scaling.  If the graph looks saturated, the scaling can be adjusted.  A checkbox should be available for auto scaling where the scaling method will adapt to values on the graph according to some slow update method.

Each node should be a uniform color but have a bright dot to indicate its current phase.  The dot is positioned over the correct location on the circle.  In cumulative mode, the base color of the node circle will change color according to scale (i.e. 0-360 is neutral, 361-720 is hotter, -360-0 is cooler).

## Initial Conditions
The user can click on a primitive to set its value.  A small popup box will accept the value and write it in.  There is also a global clear button to reset all values to zero.  In later iterations, we will have functions for injecting wave functions.

## MVP
For first iteration, we should be able to build the 1D array of specified length and optionall wrap it into y.  Further, higher degrees will be deferred for now.
