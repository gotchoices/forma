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

## The string-register model

Each node and edge in the lattice carries a **1D internal
register** — a short periodic or linear "string" that
supports standing-wave modes.  This idea originates from
[INBOX.md](../INBOX.md) ("The cell as a processor on a
string").

### Node register

Each node has a tiny 1D periodic loop (circumference L_node).
It supports standing waves with mode numbers n = 1, 2, ...,
n_max.  Each mode has an amplitude and phase.  The total
energy on the node is:

<!-- E_node = Σ_n ω_n |a_n|² -->
$$
E_{\text{node}} = \sum_{n=1}^{n_{\max}} \omega_n \,|a_n|^2
$$

where ω_n = 2πn/L_node is the mode frequency and a_n is
the complex amplitude of mode n.

The **phase** θ (axiom A3) is the lowest mode (n = 1).
Higher modes are sub-state structure — internal degrees of
freedom that contribute to entropy but are not directly
visible at the lattice scale.

### Edge register

Each edge has a 1D linear string of length 1 (one lattice
spacing) with fixed endpoints.  Standing-wave modes:
n = 1, 2, ..., n_max.  The lowest mode carries the gauge
connection A_μ.  Higher modes are sub-state.

### Junction coupling

Where an edge string meets a node loop, the amplitudes
couple additively — the wave on the edge and the wave on the
loop superpose at the junction point.  This is the
microscopic version of the covariant derivative:
D_μθ = ∂_μθ − eA_μ.

Energy can transfer between modes at each junction on each
clock cycle.  This is how information propagates through the
lattice.

### Entropy

The total number of **accessible microstates** for a node
depends on how many modes are excited and how energy is
distributed among them.  For a system with fixed total energy
E and n_max modes, the number of microstates scales roughly
as:

<!-- Ω ~ E^(n_max - 1) / Π ω_n -->
$$
\Omega \sim \frac{E^{n_{\max}-1}}{\prod_n \omega_n}
$$

(the microcanonical density of states for a collection of
harmonic oscillators).  The entropy is S = log Ω.

**A rigid body** (frozen node) has its amplitudes fixed —
no fluctuations, no microstates, S = 0.  Near the rigid
body, the junction coupling constrains the neighbouring
nodes' modes, reducing their accessible microstates.  This
creates a **scalar entropy shadow** that spreads outward
through the lattice.

The correlation function of a scalar field on a 2D lattice
falls off as log(r).  If the entropy deficit follows the
same scaling, then:

- Entropy shadow: ΔS(r) ∝ log(r)
- Entropic force: F = T · dS/dr ∝ 1/r

This is the 2D gravitational force law.

---

## Why strings give entropy (and springs don't)

In sim-gravity, each vertex had a **single** degree of
freedom (its 2D position).  A single degree of freedom has
no internal microstates — it just sits at its energy minimum.
No entropy, no entropic force.

Strings are different because they have **many modes**.  A
string with n_max modes has a high-dimensional state space.
At finite temperature, the string fluctuates among all
accessible states.  The number of accessible states (entropy)
depends on the constraints imposed by neighbours and rigid
bodies.

Analogy: a single spring has one state (its rest length).
A polymer chain with 1000 links has an astronomically large
configuration space — and the entropic force from constraining
that space is what makes rubber elastic.  Our strings are the
polymer; our nodes are the monomers.

Another analogy: graphene.  A graphene sheet is a 2D
triangular lattice of carbon atoms connected by bonds.  The
bonds vibrate (phonon modes).  The phonon spectrum gives
graphene a well-defined entropy, thermal conductivity, and
thermodynamic behaviour.  Our string-register lattice is
the Planck-scale version.

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

The scalar version can serve as a **baseline**, with the
full string-register model as the main event.

### What to measure

| Observable | Expected | Meaning |
|------------|----------|---------|
| Entropy profile S(r) | ∝ log(r) | Entropy shadow follows 2D Green's function |
| Entropic force dS/dr | ∝ 1/r | 2D gravitational force law |
| Free energy F(d) between two bodies | ∝ log(d) | Gravitational potential between masses |
| Force −dF/dd | ∝ 1/d | Newton's law in 2D |

---

## Connection to GRID axioms

| Element | GRID axiom | String-register version |
|---------|-----------|------------------------|
| Phase θ | A3 | Lowest node mode (n=1) |
| Gauge connection A_μ | A4 | Lowest edge mode (n=1) |
| Entropy density ζ | A5 | S/N per cell, from mode counting |
| Clock cycle | A1 | One MC sweep = one Planck time |
| Coupling α | A6 | Junction coupling strength |

The string registers provide the **internal structure** that
makes axiom A5 (ζ = 1/4 bit per cell) physically concrete:
the 1/4 bit is the externally accessible entropy from the
mode spectrum, not an abstract postulate.

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
