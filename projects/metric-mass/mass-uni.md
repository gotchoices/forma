# mass-uni — 3D Explorer for the Metric-Mass Project

**Status:** Specification only. To be implemented when the
project's derivational chapters call for an interactive
visualization.

This document specifies a future interactive 3D visualizer for
the [metric-mass project](README.md). When built, it lives in the
project's [viz/](../../viz/) folder under
`viz/mass-uni.html` and is linked from the relevant chapters of
this project. It follows the existing `viz/` conventions (single
HTML file, Three.js 0.163.0, shared `totu-viz.css` and
`totu-viz.js`; see [viz/README.md](../../viz/README.md) and
[viz/CLAUDE.md](../../viz/CLAUDE.md) for the API).

The name "mass-uni" is short for **Mass Universe** — the
three-coordinate (t, S, u) world this project lives in.

---

## Purpose

Provide a hands-on 3D environment for exploring how the wave
solutions of [Chapter 2](02-mass-from-u.md) live and interact on
the manifold M = (t, S, u) of [Chapter 1](01-foundation.md). The
emphasis is on building intuition that flat-page figures cannot —
specifically:

1. **What does the (t, S, u) manifold actually look like?**
   Render M as a 3D embedding (Cartesian x = S, y = u-circle,
   z = t) so the compact direction is a real circle around an
   axis, not an unrolled strip.
2. **What does a "particle" look like in this picture?**
   Render two distinct features for each massive mode: (a) the
   *worldline* of the wave packet's center, which is a straight
   line in (S, t) — the particle does not spiral; (b) the wave's
   *phase contour*, which threads helically through the (t, S,
   u) volume because the field winds n times around u at every
   position the packet occupies. The helix is a feature of the
   wave's phase structure, not of the particle's path.
3. **What does a "photon" look like?** Show light modes as
   straight worldlines, with optional decoration showing the
   wave's phase as it advances.
4. **How do geodesics respond to mass?** Place one or more
   masses at fixed S locations and draw geodesic test particles
   as curves through (S, t), showing how their paths bend in
   the presence of the masses.

The visualizer is *not* a derivation tool — it does not solve
field equations live. It uses the analytic results of the
project's chapters (or simple Newtonian approximations where the
project has not yet derived the gravitational behavior) and
renders them.

---

## Scope

**In scope (initial release):**

- 3D rendering of the manifold as an infinite cylinder, with t
  running vertically.
- A single user-set R_u (compact radius) controlling all the
  compact-direction geometry.
- One or more "particles" placed at user-chosen (S, n) — each
  carrying an integer winding number n that sets its rest mass
  m_n = ℏ|n|/(R_u c).
- Helical wavefronts for each particle, showing how its
  constant-phase surface winds around u as t advances and as it
  moves in S.
- Geodesic test particles emitted along S; each follows a
  computed path through (S, t) that bends in the presence of
  masses.
- Optional photon worldline (n = 0 mode) as a straight line in
  (S, t) at user-chosen S₀, t₀, with phase advancing in time.

**Out of scope (initial release):**

- Multiple compact dimensions (this project has only u; charge
  belongs to a future project with a separate compact direction
  w).
- Quantum-mechanical superposition or amplitude rendering. The
  visualizer shows classical mode shapes, not wave-packet
  amplitudes.
- Real-time field-theory simulation. All paths are precomputed
  from analytic formulas (or simple closed-form approximations).
- 4D or higher manifolds. (t, S, u) is exactly three.

**Open questions to be resolved before implementation:**

- *What gravitational profile do masses produce?* The project's
  derivational chapters have not yet committed to one
  ([Chapter 4](04-metric-self-consistency.md) addresses this).
  Until they do, the visualizer can either (a) use a
  qualitative bending profile chosen for pedagogical clarity,
  (b) borrow a Schwarzschild-style 1/|S − S_i| Newtonian
  profile as a placeholder, or (c) defer geodesic-response
  rendering until Chapter 4 settles the question. Decision to
  be made at implementation time.

---

## Coordinate mapping

The visualizer uses three orthogonal Cartesian display axes:

| Manifold coordinate | Display axis | Range / topology |
|---|---|---|
| Spatial extension S | x (horizontal, left-right) | unbounded, slider can pan |
| Compact direction u | wrapped around the y-axis as a circle of radius R_u | [0, L_u) with periodicity at L_u = 2π R_u |
| Time t | z (vertical, bottom-top) | unbounded, slider can scroll |

So the manifold M is rendered as a vertical infinite cylinder of
radius R_u, with S running along the cylinder axis and t running
up the page. Inside this cylinder, particles, photons, and
geodesics are drawn as curves.

(The Cartesian display axes carry no metric meaning — they are
just where on the screen each coordinate goes. The metric
geometry is encoded in the curve shapes themselves.)

---

## Features

### 1. Manifold rendering

The cylinder is rendered as a translucent surface so curves
inside it are visible. Optional grid lines mark integer values
of S (in some user-chosen unit) and integer fractions of L_u
along u.

### 2. Particles

Each particle is specified by:

- An S₀ — its position along the extended direction
- An n — its integer winding number (sets rest mass m_n)
- An optional initial spatial momentum k_S (for moving particles)

Rendering uses **two distinct visual elements** per particle, to
keep clear what is a path and what is wave structure:

- **Worldline** — a straight line through (S, t) at slope v_g
  (the group velocity). This is the path the wave packet's
  center takes through extended spacetime. For a particle at
  rest, the worldline is vertical (constant S, advancing t);
  for a moving particle, it tilts.
- **Phase contour** — a helical curve through the (t, S, u)
  volume, computed from the particle's mode

  <!-- φ_n,k_S(t, S, u) = exp(i (k_S S - ω t + n u / R_u)) -->
  $$
  \varphi_{n, k_S}(t, S, u) = \exp\!\bigl(i\,(k_S\,S - \omega\,t + n\,u/R_u)\bigr)
  $$

  with ω = c·√(k_S² + (n/R_u)²) (from the dispersion relation in
  [Chapter 2 §4](02-mass-from-u.md#4-the-dispersion-relation)).
  This curve is the locus of constant phase, parameterized by t.
  For a particle at rest (k_S = 0), it is a *vertical helix*
  winding around u as t advances; for a moving particle it
  tilts.

The visual point: *the particle moves in a straight line; the
wave's phase winds through u along the way*. The straight
worldline plus the helical phase contour together represent the
mass mode honestly. Drawing only the helix would suggest the
particle is on a spiral path, which is wrong (and would imply
charge, not mass).

Multiple particles can be placed at different S₀ values, each
with its own n and k_S.

### 3. Photons

A "photon" is an n = 0 mode. Its constant-phase line in (S, t)
is a straight line at slope c (or −c). The photon is rendered
as a straight worldline through the cylinder, optionally
decorated with a colored phase indicator that advances along
the line.

(n = 0 has no u-dependence, so the photon's worldline is *not*
helical — it lies in a plane parallel to the cylinder axis.
This is the visual distinction between light and matter on M:
light goes straight, mass spirals.)

### 4. Geodesic test particles

A geodesic test particle is a "tracer" — a free-falling test
mass that responds to whatever spacetime curvature the user-
specified masses produce. It is rendered as a curve through
(S, t) showing how its path bends near the masses.

User specifies:

- An emission point (S₀, t₀)
- An initial direction (initial dS/dt, in units of c)

The visualizer computes its geodesic forward in t and renders
the resulting curve.

In the absence of masses, geodesics are straight lines (free
fall in flat spacetime). With masses present, geodesics bend
toward each mass according to the chosen gravitational profile
(see "Open questions" above).

### 5. Phase-decorated photon trajectory (optional)

If implementation budget allows: render the photon's wave phase
as it travels — for example, color the photon's worldline with
a sinusoidal pattern that advances along the line at the wave's
frequency. This shows the photon as a literal *wave* moving
through space, not just a worldline.

Note for the user-supplied "spiral path of the photon" idea: a
photon (n = 0) does not spiral around u — it has no u-dependence
by construction. The thing that spirals around u is a *massive*
mode (n ≠ 0). The visualizer may want to make this visual
distinction explicit: light goes straight, mass spirals. If the
intent is instead to show the *internal* phase of the photon as
it travels, that lives along the photon's worldline (not around
u) and is rendered as the phase decoration above.

---

## UI controls

Following the [viz/](../../viz/) project conventions:

- **R_u slider.** Sets the compact radius. Affects rest-mass
  spectrum (m_n = ℏ|n|/(R_u c)) and visible cylinder radius.
- **Particle list.** Add/remove/edit each particle. For each:
  S₀, n, k_S, color.
- **Photon list.** Add/remove/edit each photon. For each: S₀,
  t₀, direction.
- **Geodesic list.** Add/remove/edit each geodesic test
  particle. For each: emission (S₀, t₀), initial direction.
- **Time slider / animation.** Advance t to see the system
  evolve. Pause, rewind, scrub.
- **View controls.** Standard orbit / zoom / pan from
  `totu-viz.js`.
- **Visibility toggles.** Show/hide cylinder surface, grid,
  individual particle helices, individual photon lines,
  individual geodesic curves.
- **Phase decoration toggle** (optional): show wave phase along
  worldlines.

---

## Implementation notes

The visualizer is a single `viz/mass-uni.html` file using the
shared `totu-viz.css` (styling) and `totu-viz.js` (Three.js
utilities, control patterns, coordinate conventions).

### Three.js scene structure

- **Cylinder mesh.** Translucent surface representing the
  manifold M. Rendered with `MeshStandardMaterial` and low alpha.
- **Particle helices.** Each particle is a `BufferGeometry` of
  vertices traced by parameterizing the mode's constant-phase
  curve in t.
- **Photon worldlines.** Straight `LineSegments` in (x = S, z = t)
  with optional phase-decoration via `ShaderMaterial`.
- **Geodesic curves.** Computed numerically (forward-Euler or
  RK4 from a chosen gravitational profile) and rendered as
  `BufferGeometry` line strips.
- **Grid lines.** Integer-tick reference lines on the cylinder
  surface.

### Performance

For a few particles + photons + geodesics (say ≤ 20 of each),
the scene should render at 60 fps on commodity hardware. If
geodesic computation becomes expensive at high counts,
precompute and cache.

### State management

Use the same control-panel pattern as `viz/torus-studio.html` and
`viz/torus-lab.html`. Each entity (particle, photon, geodesic)
is a row in a list with its own controls; entities can be added,
removed, or edited interactively.

---

## Future extensions

These are *not* in scope for the initial release but are
plausible follow-ups:

- **Two compact dimensions.** Once the charge project introduces
  w, extend the visualizer to (t, S, u, w) by treating w as a
  second nested wrap or as a color/texture dimension on the u
  cylinder.
- **Multiple R_u values.** Allow each particle to have its own
  effective R_u (relevant if [Chapter 5](README.md#tentative-downstream-arc)
  introduces position-dependent g_uu and the compact radius
  varies in space).
- **Off-diagonal metric visualization.** If
  [Chapter 6](README.md#tentative-downstream-arc) finds that
  off-diagonal terms get sourced, render the resulting
  worldline tilts (the "tilted conveyor belt" of Kaluza-Klein,
  but for mass instead of charge).
- **Many-particle dynamics.** Real time evolution under mutual
  gravitational attraction. Useful for n-body intuition on the
  cylinder.
- **Cross-link to the production R-track.** If the project's
  results connect to [studies/R60](../../studies/R60-metric-11/)
  or beyond, render specific particle configurations from those
  studies.

---

## Limitations / honesty

The visualizer renders configurations the chapters have derived,
plus pedagogical decoration. It does not:

- Solve field equations live. All curves are pre-computed from
  analytic formulas.
- Include quantum-mechanical fluctuations, second quantization,
  or anything beyond classical wave mechanics.
- Make claims about *physical particles* in nature. The modes
  rendered are the modes of the wave equation on M, with the
  rest masses derived in Chapter 2. Whether nature populates
  any of them is outside the project's scope.

The "open question" of which gravitational profile to use for
geodesic bending should be treated honestly in the visualizer's
UI: when a placeholder profile is in use, label it as such.

---

## Building checklist

When the time comes to implement:

1. Confirm Chapter 4's findings on gravitational behavior; pick
   the rendering profile accordingly.
2. Create `viz/mass-uni.html` and `viz/mass-uni.md` (the
   user-facing spec for the visualizer's UI; this file moves to
   that location and is updated to reflect actual UI).
3. Add a card to `viz/index.html` and an entry in
   `viz/README.md`'s tools table.
4. Link from the relevant project chapters
   ([03-examining-the-modes.md §4](03-examining-the-modes.md#4-visualization-on-the-cylinder)
   in particular).
5. Test interactively before declaring done.
