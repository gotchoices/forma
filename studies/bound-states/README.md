# R27. Bound states from T⁶ — atoms and nuclei as oscillation patterns  *(active)*

**Questions:** Q28 (photon absorption / energy levels), Q32 (energy-geometry)
**Type:** compute/analytical  **Depends on:** R26, R19, R15

## Motivation

R26 showed that the T⁶ produces an emergent neutron — a cross-
sheet mode with zero charge and mass near m_n.  But R27 Track 1
showed that the naive identification (mode (1,2,0,0,1,2)) does
not survive self-consistent treatment: when circumferences are
adjusted to keep m_e and m_p exact, the maximum achievable
m_n − m_p is only ~0.5 MeV (target: 1.293 MeV).

Before we can predict atoms, we need a self-consistent neutron.
And before we can predict anything complex, we need a general-
purpose **discovery engine** — a solver that takes target
properties (mass, charge, spin) and searches the full parameter
and quantum number space for T⁶ oscillation patterns that match.

The same engine that finds the neutron can then search for
hydrogen, the deuteron, and any other target.


## Core hypothesis

**The T⁶ supports oscillation patterns — single modes or
compound configurations — with the observed properties of
neutrons, atoms, and nuclei.  These patterns are discoverable
by systematic search over quantum numbers and metric parameters.**


## Approach

### Track 1 — Self-consistent neutron mass  ✔

**Status:** Complete.  See findings F1–F8.

Key results:
- The naive (1,2,0,0,1,2) mode with symmetric σ_ep is
  quantitatively insufficient (max m_n − m_p ≈ 0.50 MeV).
- Negative σ_ep gives the correct sign (m_n > m_p).
- Alternative modes (0, −3, n₃, n₄, 0, 2) achieve 0.93 MeV.
- The qualitative neutron picture is intact; the quantitative
  mode identification is open.


### Track 2 — T⁶ mode solver (discovery engine)

Build a solver library (`lib/t6_solver.py`) that sits on top of
`lib/t6.py` and provides:

**2a. Target-based mode search.**

Given target properties:
    target = {
        'mass_MeV': 939.565,
        'charge': 0,
        'spin_halves': 1,    # spin ½
    }

The solver searches over:
- All quantum numbers (n₁, ..., n₆) up to |n_i| ≤ n_max
- All cross-shear parameters (σ_ep, σ_eν, σ_νp) within
  positivity bounds
- Self-consistent circumferences at each parameter point

And returns the best-matching modes ranked by closeness to the
target mass, filtered by exact charge and spin constraints.

**2b. Self-consistent metric solver.**

Generalize the Track 1 self-consistent solver to handle ALL
cross-shears simultaneously.  At each point (σ_ep, σ_eν, σ_νp),
adjust L₂, L₄, and L₆ so that:

    E(1,2,0,0,0,0) = m_e        (electron exact)
    E(0,0,1,1,0,0) = m_ν₁       (neutrino₁ exact, or Δm²₂₁ exact)
    E(0,0,0,0,1,2) = m_p        (proton exact)

This ensures the three input particles are always correct,
regardless of cross-shear values.

**2c. Multi-target optimizer.**

Given MULTIPLE targets simultaneously (neutron + muon + tau, or
neutron + deuteron + ...), find parameter regions where all
targets are matched at once:

    targets = [
        {'mass_MeV': 939.565, 'charge': 0, 'spin_halves': 1},
        {'mass_MeV': 105.658, 'charge': -1, 'spin_halves': 1},
        ...
    ]

Minimize the total mass error across all targets.  This is the
tool that collapses the free parameter space.

**Deliverables:**
- `lib/t6_solver.py` — reusable solver module
- Validation: reproduce Track 1 results via the solver API
- Documentation and usage examples


### Track 3 — Neutron mode identification

Use the Track 2 solver to perform a comprehensive search for
the neutron:

**Target:**
    mass = 939.565 MeV
    charge = 0
    spin = ½
    additional: must be unstable when isolated but stabilizable
                in combination with a proton mode

**Search space:**
- Quantum numbers |n_i| ≤ 10 (not just ≤ 3 as in R26)
- All three cross-shears varied simultaneously
- Self-consistent circumferences at every point
- All three aspect ratios (outer sweep or optimization)

**Specific investigations:**
1. The (0, −3, n₃, n₄, 0, 2) family identified in F6 —
   self-consistent sweep, can it hit 1.293 MeV?
2. Modes with n₁ ≠ 0 and n₅ ≠ 0 (the original "electron+proton"
   type) at higher quantum numbers
3. Cross-block effects: does turning on σ_eν or σ_νp while
   σ_ep is active open new parameter space?
4. Modes that are unstable in isolation (energy > sum of decay
   products) but might be stabilized in a nucleus (energy
   landscape changes when a proton mode is also present)

**Deliverable:** The quantum numbers and parameter values for the
self-consistent neutron, or a clear diagnosis of what additional
mechanism is needed.


### Track 4 — Nuclear stability criterion

A neutron in a nucleus is stable.  A free neutron decays.  What
distinguishes these cases in the T⁶?

**Hypothesis:** The neutron mode's energy depends on what other
modes are simultaneously present.  In isolation, its energy
exceeds m_p + m_e (so decay is energetically allowed).  In the
presence of a proton mode, the combined pattern has lower total
energy than the separated modes — the neutron is "trapped."

**Method:** Using the Track 2 solver, compute:
1. E(neutron mode alone)
2. E(proton mode alone)
3. E(neutron + proton as compound pattern) — if multi-mode
   cross-energy exists (Track 2 formalism needed)

If E(compound) < E(neutron) + E(proton), the compound is bound
and the neutron is stabilized.

**Deliverable:** Whether the T⁶ produces different effective
neutron masses in isolation vs in a nuclear environment.


### Track 5 — Hydrogen-like patterns

Search for T⁶ oscillation patterns with hydrogen properties:
    charge = 0
    mass ≈ m_p + m_e − 13.6 eV
    discrete excited states at −13.6/n² eV

**Approach:** Use the Track 2 multi-target optimizer.  Search
for parameter regions where:
- A charge-0 pattern exists at m_p + m_e − 13.6 eV
- Related patterns exist at m_p + m_e − 3.4 eV, − 1.5 eV, ...
  (the Balmer series)

This is a harder search than the neutron because the binding
energy (13.6 eV) is tiny compared to the rest masses (~938 GeV),
requiring very precise mode matching.

**Deliverable:** A hydrogen-like T⁶ pattern, or identification
of what prevents it.


### Track 6 — Deuteron-like patterns

Search for a proton-neutron bound state:
    charge = +1e
    mass = m_p + m_n − 2.224 MeV
    spin = 1

**Deliverable:** A deuteron-like T⁶ pattern, or diagnosis of
why the simplest nucleus doesn't emerge.


## Infrastructure

### Existing: `lib/t6.py`

Low-level T⁶ model:
- Metric construction (`build_scaled_metric`)
- Mode energies (`mode_energy`)
- Charge and spin (`mode_charge`, `mode_spin`)
- Spectral scanning (`scan_modes`)

### New: `lib/t6_solver.py` (Track 2 deliverable)

High-level discovery engine:
- `find_modes(target, ...)` — search for modes matching target
  properties
- `self_consistent_metric(sigmas, ...)` — full self-consistent
  metric with all cross-shears
- `multi_target_optimize(targets, ...)` — find parameter regions
  matching multiple targets simultaneously
- `mode_stability(mode, environment_modes, ...)` — compute whether
  a mode is stable in the presence of other modes

Track-specific scripts go in `bound-states/scripts/`.


## What this study could determine

### Free parameters constrained

| Source | Constraint |
|--------|-----------|
| m_n − m_p = 1.293 MeV | Pins σ_ep (or combination) |
| Neutron mode identification | Constrains quantum numbers |
| Nuclear stability | Constrains cross-shear structure |
| Hydrogen binding 13.6 eV | Constrains cross-shear strength |
| α from binding energy | Relates r_e to shears |
| Deuteron binding 2.224 MeV | Further constrains parameters |

### Possible outcomes

**Best case:** The solver finds a self-consistent neutron,
hydrogen emerges as a compound pattern, and α is determined.

**Partial success:** The neutron is found with revised quantum
numbers but atoms require mechanisms beyond single-mode T⁶
physics (nonlinear coupling, backreaction).

**Null result (informative):** No single T⁶ mode matches the
neutron self-consistently.  This would mean the neutron is
genuinely a multi-body object (like the standard model's three
quarks) and single-mode T⁶ physics describes only fundamental
particles, not composites.


## Relation to prior studies

| Study | Relationship |
|-------|-------------|
| R26 | T⁶ framework, initial neutron discovery, metric infrastructure |
| R27 F1–F8 | Track 1 results that motivate the solver approach |
| R19 | Shear-charge mechanism |
| R15 | The α problem — hydrogen binding could solve it |
| R28 | Companion: unstable particle spectrum (shares solver) |
