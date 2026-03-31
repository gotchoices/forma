# sim-maxwell: Wave propagation on a triangular lattice

**Status:** Planned — not yet started.

**Question:** can a small triangular lattice support
directional wave propagation and superposition — the
minimum conditions for hosting Maxwell's equations?

This is the computational test of the "distributed processor"
picture from [INBOX.md](../INBOX.md).

---

## The core question

Maxwell's equations on a lattice require:
1. **Directional propagation** — a wave packet launched in
   one direction should travel in that direction, not
   diffuse isotropically
2. **Superposition** — two waves passing through each other
   should add linearly and emerge unchanged
3. **Correct speed** — waves propagate at c = 1 cell per
   tick (in lattice units)
4. **Polarization** — the wave should carry a vector
   character (E and B fields), not just a scalar amplitude

If the lattice can do all four, it hosts Maxwell.  If it
can do 1–3 but not 4, it hosts a scalar wave equation
(still useful, but not full EM).  If it can't even do 1,
the processor picture needs more structure.

---

## The tautology problem

A naive first attempt would be to use the **Wilson action**
from lattice gauge theory as the update rule.  The Wilson
action was specifically designed to discretize the Maxwell
action — running a simulation of it is confirming that the
discretization works numerically.  It would tell us nothing
about whether the lattice *naturally* hosts EM waves.  It
is circular: we'd be programming Maxwell in and observing
Maxwell out.

For this study to constitute a genuine result, the update
rule must emerge from the lattice itself — not be imported
from the answer we're trying to derive.

## Four levels of rigor

From most tautological to most ground-up:

### Level 1: Import the Wilson action (tautological)

Use Hamilton's equations from S = −κ Σ Re(U_plaquette).

This is what lattice QCD does.  It reproduces Maxwell by
construction.  Useful only as a **numerical reference** —
if we can't match this, we've made a coding error.

### Level 2: Derive the unique gauge-invariant action

Start from: nodes carry phase θ ∈ [0, 2π), edges carry
link variables U = exp(iA).  Impose:
- Locality (update depends only on immediate neighbors)
- Gauge invariance (physics unchanged under θ_x → θ_x + χ_x
  with compensating link transformation)
- At most second-order in derivatives (leading-order action)

Show that the Wilson action is the **unique** simplest
action satisfying these constraints.  Then the update rule
is forced, not chosen.

This is what [maxwell.md](../maxwell.md) already does on
paper.  The simulation would confirm it numerically.  Not
fully ground-up (we assumed gauge invariance as an axiom),
but not tautological — the action was derived, not imported.

### Level 3: Search the rule space (discovery)

Impose only: nodes have a periodic state, edges have a
periodic state, updates are local and gauge-invariant.

**Do not choose an action.**  Instead, enumerate or search
the space of possible local update rules that satisfy gauge
invariance.  For each candidate rule, run the simulation
and test whether it produces directional wave propagation.

Questions this would answer:
- Is the Wilson action the unique gauge-invariant rule that
  supports waves?  Or are there others?
- Is there a simpler rule that still works?
- What is the *minimal* gauge-invariant update that
  produces Maxwell-like behavior?

### Level 4: No assumptions (minimal model)

Don't assume gauge invariance.  Don't assume phases.
Just: nodes have state, edges have state, updates are local.

Explore what kinds of state and what update rules produce
directional wave propagation on a triangular lattice.

This is the string-register model from the INBOX: each node
holds a circular standing wave, each edge holds a linear
standing wave, and the update rule is local superposition at
junctions.

**State variables:**
- Node: mode amplitudes {a_n} for standing waves on a
  circular 1D space (a tiny periodic loop at the lattice
  site).  The fundamental mode (n=1) is the phase θ.
  Higher modes carry sub-state.
- Edge: mode amplitudes {b_n} for standing waves on a
  linear 1D space (a segment connecting two nodes).  The
  fundamental mode (n=1) is the gauge connection A_μ.

**Update rule (per clock cycle):**
1. At each junction (where edge meets node), the incoming
   wave amplitudes add: the edge's outgoing amplitude is
   set by the sum of the connected node's amplitude and
   the edge's current amplitude
2. The node's amplitude is updated by the sum of all
   connected edge amplitudes
3. Phase advanced by one tick (time always forward, but
   phase oscillates freely — see below)

**Key physics question:** what junction rule produces
directional propagation?

- **Naive sum (equal splitting):** energy distributes
  equally to all edges → isotropic diffusion → FAILS
- **Phase-sensitive sum:** the relative phase between node
  and edge determines the split → directional propagation
  possible if phases encode direction
- **Momentum-conserving rule:** the update preserves a
  lattice analog of momentum → directional propagation
  guaranteed

If Level 4 produces waves with the right behavior, it
validates the processor picture from first principles.  If
it fails (only diffusion), it tells us gauge invariance is
an essential ingredient — you can't get Maxwell without it.

## Phase dynamics: time advances, phase oscillates

A critical distinction for all approaches:

- **Time always moves forward** (Axiom A2).  The clock
  ticks monotonically: t → t+1.  There is no reversing the
  update cycle.

- **Phase oscillates freely.**  On each tick, the update
  rule can push θ in either direction.  The back-and-forth
  oscillation of phase IS the wave.  A phase that only
  advances monotonically would be a DC current (constant
  drift), not a wave.

- **θ̇ is the electric field.**  In the temporal gauge, the
  time derivative of the node phase is the electric field.
  Its oscillation between positive and negative values is
  what produces oscillating E and B.

- **Phase wrapping is charge.**  When θ accumulates past
  2π, it wraps.  This topological carry is the microscopic
  mechanism of charge quantization.  The wrap propagates
  to the edges (gauge connection absorbs it, maintaining
  gauge invariance).

## Recommended strategy

1. **Level 1 first** — implement the Wilson action as a
   reference baseline.  Quick to code, confirms the
   test infrastructure works.  Label it clearly as
   tautological.

2. **Level 2 next** — derive the action from axioms (as in
   maxwell.md) rather than importing it.  The simulation
   runs identically, but the writeup documents *why* this
   action is forced.  Partially ground-up.

3. **Level 4 in parallel** — build the string-register
   model with candidate junction rules.  Compare its
   behavior to the Level 1 reference.  This is the
   genuinely exploratory part.

4. **Level 3 if Level 4 fails** — if no simple rule
   produces waves, systematically search gauge-invariant
   rules to understand what structure is essential.

---

## Test protocol

### Test 1: Plane wave propagation

1. Initialize a plane wave: θ_x = A sin(k · x − ωt) at
   t = 0, with wavevector k pointing in one direction
2. Evolve for T time steps
3. Measure whether the wave packet moves in the k direction
4. Measure the propagation speed (should be c = 1)
5. Check for dispersion (wave spreading)

**Pass criterion:** wave packet center moves in the k
direction at speed ≈ 1, with modest dispersion.

### Test 2: Superposition

1. Initialize two plane waves with different wavevectors
   k₁ and k₂
2. Evolve until they overlap
3. Check that the field in the overlap region is the sum
   of the two individual waves
4. Evolve until they separate
5. Check that each wave emerges from the collision unchanged

**Pass criterion:** post-collision waves match pre-collision
waves to within numerical precision.

### Test 3: Point source

1. Drive a single node with oscillating phase: θ₀(t) =
   A sin(ωt)
2. Evolve for many periods
3. Measure the amplitude as a function of distance r from
   the source
4. Check for 1/√r falloff (2D cylindrical wave)

**Pass criterion:** amplitude ∝ 1/√r, with circular
wavefronts.

### Test 4: Polarization (if applicable)

1. On a 2D lattice, the "B field" is a scalar (B_z) and
   the "E field" has two components (E_x, E_y)
2. Initialize a wave with definite polarization
3. Check that E and B oscillate 90° out of phase
4. Check that E is perpendicular to the propagation
   direction

**Pass criterion:** correct E/B phase relationship and
transversality.

---

## Lattice geometry

For 2D tests, use a triangular lattice on a torus (periodic
boundary conditions in both directions) to avoid edge
reflections.

| Parameter | Minimum | Production |
|-----------|---------|------------|
| Lattice size | 30 × 30 | 100 × 100 |
| Vertices | ~900 | ~10,000 |
| Edges | ~2,700 | ~30,000 |
| Triangles | ~1,800 | ~20,000 |
| Time steps | 100 | 1,000 |

The wavelength of the test wave should be at least 10
lattice spacings (to stay well above the Nyquist limit and
avoid lattice dispersion artifacts).

---

## Files (planned)

| File | Purpose |
|------|---------|
| `README.md` | This design document |
| `lattice.py` | Triangular lattice topology (vertices, edges, plaquettes) |
| `wilson_ref.py` | Level 1: Wilson action reference (tautological baseline) |
| `derive_action.py` | Level 2: action derived from axioms |
| `string_model.py` | Level 4: string-register update rules |
| `rule_search.py` | Level 3: systematic search of gauge-invariant rules |
| `init.py` | Wave packet initialization (plane wave, point source) |
| `evolve.py` | Time stepping (shared by both approaches) |
| `measure.py` | Field snapshots, dispersion, superposition checks |
| `run_tests.py` | Automated test suite (tests 1–4) |
| `viz.py` | Visualization (animated wave propagation) |

---

## Dependencies

numpy, scipy, matplotlib.  Possibly a visualization library
for animated lattice plots (matplotlib.animation or similar).

---

## What success looks like

**Level 1 (baseline):** confirms test infrastructure works.
Not scientifically interesting — it is tautological by
design.  Value is purely as a reference.

**Level 2 (principled):** the action is derived from
axioms, not imported.  Waves propagate.  This confirms
maxwell.md computationally but doesn't go beyond it.

**Level 4 (discovery — the real prize):** a simple local
update rule, without importing the Wilson action or
assuming gauge invariance, produces directional wave
propagation and superposition on the triangular lattice.
This would mean the lattice geometry itself is sufficient
for Maxwell — gauge invariance would be a *consequence* of
the lattice structure, not an axiom.  This would reduce
GRID's axiom count.

**Level 3 (fallback discovery):** if Level 4 fails
(diffusion only), but a systematic search shows the Wilson
action is the *unique* gauge-invariant rule that produces
waves, that's also a genuine result.  It means gauge
invariance is the essential ingredient, and the Wilson
action is not a choice but a necessity.

**Informative failure:** Level 4 produces only diffusion
AND Level 3 finds multiple gauge-invariant rules that all
produce waves.  This would mean: (a) gauge invariance is
necessary, (b) it is not sufficient to uniquely fix the
dynamics, and (c) the Wilson action encodes additional
structure beyond gauge invariance.  An honest result that
would sharpen our understanding of what the axioms do and
don't determine.

All outcomes are useful.  The only wasted run is Level 1
alone with nothing else.
