# sim-gravity-2: Entropic gravity from a string-register lattice

**Status:** Design phase.

**Question:** does the *entropic* force between two rigid
bodies on a fluctuating lattice fall off as 1/r (2D gravity),
rather than the 1/r² we got from mechanical springs
(sim-gravity)?

**Motivation:** sim-gravity showed that energy minimisation
on a spring lattice gives the elastic power law (1/r²), not
the gravitational one (1/r).  The GRID framework derives
gravity thermodynamically (Jacobson): F = T · dS/dr.  This
simulation tests that mechanism numerically.

---

## The key insight from sim-gravity

The spring lattice failed because the field variable was a
**2D position vector** at each vertex (satisfying Navier's
equation → 1/r² strain).  Gravity requires a **scalar** field
(satisfying Poisson's equation → 1/r force).

In the GRID picture, the gravitationally relevant quantity
is the **entropy** — the number of microstates per cell
(axiom A5, ζ = 1/4 bit per cell).  Entropy is scalar.  If a
rigid body creates a local entropy deficit, and that deficit
falls off as log(r), then the entropic force dS/dr ∝ 1/r.

The question is: what gives the lattice cells enough internal
structure to *have* entropy?

---

## The string-register model (Model B)

In Model B (see [lattice-geometry.md](../lattice-geometry.md)
and [INBOX.md](../INBOX.md)), the cell has **no separate
internal state**.  The cell IS its edges — vibrating strings
that carry all the information.  Vertices are coupling
junctions, not state holders.

### The cell as a triangle of strings (2D)

In the 2D simulation, each triangular cell is three strings
forming its boundary.  Each edge is a 1D linear string of
length 1 (one lattice spacing) with vertices as endpoints.

Each string supports standing-wave modes n = 1, 2, ..., n_max.
The energy on one edge is:

<!-- E_edge = Σ_n ω_n |a_n|² -->
$$
E_{\text{edge}} = \sum_{n=1}^{n_{\max}} \omega_n \,|a_n|^2
$$

where ω_n = nπ/L (fixed-endpoint modes) and a_n is the
complex amplitude of mode n.

- **Lowest mode (n = 1):** carries the gauge connection A_μ
  — the lattice version of the electromagnetic field.
- **Higher modes (n > 1):** sub-state structure — internal
  degrees of freedom that contribute to entropy but are not
  directly visible at the lattice scale.
- **Phase θ (axiom A3):** a collective property of the
  cell's three edge modes, not a separate variable.

### Vertex coupling

Each vertex is shared by 6 triangles (in a triangular
lattice) and 6 edges meet there.  The vertex is a **junction
rule**, not a state container.  At each clock cycle, the
vertex:

1. Receives the mode amplitudes from all connected edges
2. Applies a coupling rule (superposition / energy transfer)
3. Updates the outgoing mode amplitudes on each edge

This is the microscopic version of the covariant derivative:
D_μθ = ∂_μθ − eA_μ.  The phase gradient on one edge plus
the contribution from neighbouring edges combine at the
junction.

Energy transfers between edges at each vertex on each
clock cycle.  This is how information propagates through
the lattice.

### Entropy

The total number of **accessible microstates** for a cell
depends on how energy is distributed among the modes on its
3 edges.  With n_max modes per edge and 3 edges, the cell
has 3 × n_max oscillator modes.  For a system with fixed
total energy E and N_modes modes, the microstate count is:

<!-- Ω ~ E^(N_modes - 1) / Π ω_n -->
$$
\Omega \sim \frac{E^{N_{\text{modes}}-1}}{\prod_n \omega_n}
$$

(microcanonical density of states for harmonic oscillators).
The entropy is S = log Ω.

**A rigid body** (frozen edges) has its amplitudes fixed —
no fluctuations, no microstates, S = 0.  Near the rigid
body, the vertex coupling constrains the neighbouring edges'
modes, reducing their accessible microstates.  This creates
a **scalar entropy shadow** that spreads outward through the
lattice.

The correlation function of a scalar field on a 2D lattice
falls off as log(r).  If the entropy deficit follows the
same scaling, then:

- Entropy shadow: ΔS(r) ∝ log(r)
- Entropic force: F = T · dS/dr ∝ 1/r

This is the 2D gravitational force law.

### Connection to ζ

Under Model B, a 2D triangular cell has 3 face-sharing
neighbors (no self) → ζ = 1/3.  A 3D tetrahedral cell
has 4 face-sharing neighbors → ζ = 1/4 (Bekenstein-Hawking).
The 2D simulation uses ζ = 1/3; the physically relevant
value for horizons (3D cells) is ζ = 1/4.

---

## Standing waves and energy transfer

### Can a standing wave deliver energy at its endpoint?

A textbook standing wave on a rigid-endpoint string delivers
no net energy — the endpoints don't move, so no work is done.
But in our lattice the endpoints are *coupled junctions*
where multiple strings meet.  Each string's mode exerts a
force at the vertex; the vertex mediates energy transfer
between strings.  Energy arrives on one string's modes and
scatters into the other strings' modes.

This is how phonons propagate through a crystal lattice:
each bond has vibrational modes, and the atoms (vertices) are
coupling points.  The strings don't have rigid endpoints —
they have *coupled* endpoints.  The mode spectrum is still
discrete (standing-wave-like), but energy flows through the
junctions.

### Is the vertex stationary?

**Yes — in this simulation.**  The vertex is a massless,
stateless junction.  It has no inertia, no position to
update, and no state register.  It instantly mediates the
coupling between connected strings.

Why this choice matters: if we gave vertices mass and let
them move, we'd reintroduce the *vector displacement field*
that gave sim-gravity its 1/r² (elastic) result.  By keeping
vertices fixed and letting only the *mode amplitudes*
fluctuate, we isolate the **scalar entropy** from the
**vector elasticity**.  This separation is exactly what we
need to test whether the entropic force gives 1/r.

The Monte Carlo samples mode amplitudes on edges, not vertex
positions.  The vertex applies a coupling rule (how energy
redistributes among connected edges) but does not itself
contribute degrees of freedom.

---

## Why strings give entropy (and springs don't)

In sim-gravity, each vertex had a **single** degree of
freedom (its 2D position).  A single degree of freedom has
no internal microstates — it just sits at its energy minimum.
No entropy, no entropic force.

Edge strings are different because they have **many modes**.
A string with n_max modes has a high-dimensional state space.
At finite temperature, the string fluctuates among all
accessible states.  The number of accessible states (entropy)
depends on the constraints imposed by neighbours and rigid
bodies.

In Model B, the cell IS its edges.  A triangular cell has
3 edges × n_max modes = 3 × n_max oscillator degrees of
freedom.  Even with n_max = 3, that's 9 modes per cell — far
richer than the 2 degrees of freedom (x, y) in sim-gravity.

Analogy: a single spring has one state (its rest length).
A polymer chain with 1000 links has an astronomically large
configuration space — and the entropic force from constraining
that space is what makes rubber elastic.  Our edge strings are
the polymer; our vertices are the monomers.

Another analogy: graphene.  A graphene sheet is a 2D
triangular lattice of carbon atoms connected by bonds.  The
bonds vibrate (phonon modes).  The phonon spectrum gives
graphene a well-defined entropy, thermal conductivity, and
thermodynamic behaviour.  Our string-register lattice is
the Planck-scale version — and in Model B, the state lives
on the bonds (edges), not the atoms (vertices).

---

## Simulation design

### Approach: Monte Carlo at finite temperature

1. **Initialise:** triangular lattice, each node has n_max
   mode amplitudes (complex numbers), each edge has n_max
   mode amplitudes.  Total energy distributed thermally
   (Boltzmann distribution at temperature T).

2. **Embed rigid body:** freeze the mode amplitudes of a
   cluster of nodes (hexagon or triangle).  These nodes can
   no longer fluctuate.

3. **Monte Carlo sampling:** at each step:
   - Pick a random free node or edge
   - Propose a random perturbation to one of its mode
     amplitudes
   - Compute ΔE (energy change from junction coupling and
     self-energy)
   - Accept with probability min(1, exp(−ΔE/T))
   - Repeat for many sweeps until equilibrated

4. **Measure entropy:** for each node, estimate the local
   entropy from the variance of mode amplitudes across the
   Monte Carlo trajectory.  (High variance = many accessible
   states = high entropy.)

5. **Radial profile:** bin the local entropy by distance from
   the rigid body.  Fit to S(r) = A · log(r) + B.

6. **Entropic force:** compute the free-energy gradient
   between two rigid bodies at varying separations.

### Simplified version (scalar field)

If the full string-register model is too complex for a first
pass, a simpler version captures the essential physics:

- Each node carries a **single scalar** φ with a Gaussian
  energy: H = (K/2) Σ_edges (φ_i − φ_j)²
- Monte Carlo at temperature T samples the Boltzmann
  distribution exp(−H/T)
- Pinning φ at the rigid body creates a scalar entropy shadow
- The correlator ⟨φ(0)φ(r)⟩ ∝ log(r) for the 2D Gaussian
  model — this is well-known analytically
- This is less physically rich than the string model but
  should reproduce the 1/r force and validate the pipeline

The scalar version serves as a **baseline**, with the
full string-register model as the main event.

### Scalar baseline results ✅

The scalar baseline has been run (`run_scalar.py`).
Two methods:

**Part 1 — Direct solve (no MC):**  Solve ∇²φ = 0 with
φ = 1 at defect, φ = 0 at boundary.

| Lattice | φ fit R² | p (dφ/dr ∝ r⁻ᵖ) | R² |
|---------|---------|-----------------|-----|
| 100² | 1.000 | 0.979 | 0.983 |
| 200² | **1.000** | **1.012** | **0.999** |

The scalar field gives **φ ∝ log(r)** and **dφ/dr ∝ 1/r**
with p = 1.012, R² = 0.999.  This is the 2D gravitational
force law — compare with sim-gravity's vector field which
gave p = 2.0 (elastic).

**Part 2 — MC at T = 1.0 (40×40):**  Mean field tracks the
direct solution (R² = 0.988).  Variance (entropy proxy)
shows a log(r) trend (R² = 0.80) — positive but noisy due
to the small lattice.

**Conclusion:** the scalar field on the same triangular
lattice that gave 1/r² for springs gives **1/r for a scalar
potential**.  The field type (vector vs scalar) is the
decisive factor, confirming that gravity requires scalar
(entropic) degrees of freedom, not vector (elastic) ones.

Plots in `output/scalar_baseline.png`.

### What to measure (string-register model)

| Observable | Expected | Meaning |
|------------|----------|---------|
| Entropy profile S(r) | ∝ log(r) | Entropy shadow follows 2D Green's function |
| Entropic force dS/dr | ∝ 1/r | 2D gravitational force law |
| Free energy F(d) between two bodies | ∝ log(d) | Gravitational potential between masses |
| Force −dF/dd | ∝ 1/d | Newton's law in 2D |

---

## Connection to GRID axioms

| Element | GRID axiom | Model B version |
|---------|-----------|------------------------|
| Gauge connection A_μ | A4 | Lowest edge mode (n=1) |
| Phase θ | A3 | Collective property of cell's 3 edge lowest modes |
| Entropy density ζ | A5 | S/N per cell, from mode counting (ζ = 1/3 in 2D, 1/4 in 3D) |
| Clock cycle | A1 | One MC sweep = one Planck time |
| Coupling α | A6 | Vertex coupling strength |
| Vertex | — | Junction rule (covariant derivative), not a state holder |

The edge strings provide the **internal structure** that
makes axiom A5 physically concrete: the externally accessible
entropy per cell comes from the mode spectrum on its boundary
edges, not an abstract postulate.

---

## Why this should work (and what could go wrong)

**Why it should work:** the entropy shadow of a pinned scalar
field on a 2D lattice follows the 2D Green's function
(log r).  This is a known result from statistical mechanics.
The entropic force is the gradient: 1/r.  The string-register
model is a richer version of the same scalar field, with
additional modes that increase the entropy but shouldn't
change the power law (they add a multiplicative constant to
Ω, not a different r-dependence).

**What could go wrong:**
- The junction coupling between strings may create
  non-trivial correlations that change the power law
- Finite-size effects or equilibration problems in the MC
- The 1/r force might only appear at the critical temperature
  (where correlation length diverges), not at generic T
- The "entropy" we measure might be dominated by local
  self-energy rather than the spatial correlation with the
  rigid body

These are all testable.

---

## Files (planned)

| File | Purpose |
|------|---------|
| `README.md` | This document |
| `lattice.py` | Reuse from sim-gravity (triangular lattice generation) |
| `string_register.py` | Node and edge string-register model (modes, energy, coupling) |
| `monte_carlo.py` | Metropolis MC sampler with frozen vertices |
| `measure.py` | Local entropy estimation, radial profiling, free-energy measurement |
| `run_scalar.py` | Simplified scalar-field baseline |
| `run_strings.py` | Full string-register simulation |

---

## Running order

1. **Scalar baseline** (`run_scalar.py`): validate the
   pipeline, confirm log(r) entropy profile and 1/r force.
   Should take minutes.

2. **String-register model** (`run_strings.py`): the real
   test — does the richer internal structure change the
   power law?  If it still gives 1/r, we have evidence that
   gravity is robust to the details of the internal state
   space.  If it gives something else, we learn what the
   string structure does to the thermodynamics.

---

## Estimated scale

- **Lattice:** 50×50 to 150×150 (MC is cheaper per sweep
  than L-BFGS, but needs many sweeps)
- **Modes per string:** n_max = 3–8 (small enough for fast
  MC, large enough for meaningful entropy)
- **MC sweeps:** ~10⁴ for equilibration, ~10⁵ for
  measurement (standard for lattice models)
- **Dependencies:** numpy, matplotlib (no scipy needed for MC)
