# GRID — Geometric Relational Interaction Domain

## What this is

GRID is the substrate layer beneath [MaSt](../README.md).

MaSt takes Maxwell's equations and the fine-structure constant α as
*inputs* and builds particles from confined photons on compact
geometry.  GRID asks: where do Maxwell's equations come from?  What
determines α?  And can gravity (G) emerge from the same foundation?

The approach: start from a minimal discrete lattice — cells, phases,
nearest-neighbor coupling — and derive the continuum physics that MaSt
assumes.  One geometric constant, one measured input.
Everything else is emergent.

## The two constants

| Symbol | Name | Value | Status | What it controls |
|--------|------|-------|--------|------------------|
| ζ | Resolution | 1/4 | Derived from geometry | Bits per Planck cell — the information density of the substrate.  Determines gravitational coupling G. |
| α | Coupling | ≈ 1/137.036 | Measured input | Electromagnetic interaction strength — energy cost of a topological defect relative to the lattice scale.  Determines ε₀, μ₀, e. |

**ζ** (zeta) follows from the geometry of the cells adjacent
to causal horizons.  A horizon is a 2D surface in 3D space.
The 3D cells touching the horizon are tetrahedra (3-simplices).
Under Model B — where the cell IS its edges, with no separate
internal state — each tetrahedron has 4 face-sharing neighbors
and no "self" to count, giving ζ = 1/4.  This is the
Bekenstein-Hawking factor: a horizon of area A carries entropy
S = ζ · A = A/4.  The value is not imported from black hole
physics — it is derived from the dimensionality (3D) and
packing (simplicial) of the cells adjacent to the horizon.
See [lattice-geometry.md](lattice-geometry.md) for details.

**α** is the sole measured input — the single free coupling
constant of the lattice gauge theory.  MaSt also takes α as
input (R15, R19, R31–R36).  GRID does not attempt to derive it.

## Relationship to MaSt

```
GRID (this sub-project)
    Axioms: 4D causal lattice + ζ + α
        │
        ├── Derives: Maxwell's equations (ε₀, μ₀, charge quantization)
        ├── Derives: G from entropy density
        └── Derives: spacetime stiffness c⁴/(8πG)
              │
              ▼
MaSt (the existing framework)
    Takes as input: Maxwell + α
        │
        ├── Particles as confined photons on Ma
        ├── Mass spectrum, spin, charge
        └── Nuclear structure
```

GRID is upstream.  It provides the foundations that MaSt stands on.

## Derivation goals

### 1. Maxwell's equations from the lattice

Starting from six axioms (see [foundations.md](foundations.md)),
derive all four Maxwell equations without importing any
electrodynamics.  The electromagnetic field emerges as the
gauge connection of phase differences between lattice cells.

**Target:** a clean, step-by-step derivation from axioms to
∂_μ F^μν = J^ν and ∂_{[μ} F_{νρ]} = 0, with explicit identification
of E, B, ε₀, μ₀.

### 2. Newton's gravitational constant G

From the resolution parameter ζ, derive G in both natural units
(where G = 1) and SI units.  The path goes through entropy:
ζ sets the entropy density → Jacobson's thermodynamic argument
yields Einstein's equations → G is read off as G = 1/(4ζ)
in natural units.

**Target:** G expressed in terms of ζ, ℏ, c, k with full
dimensional analysis.  No circular reasoning.

## Origin

This sub-project grew from the dialog in
[`dialogs/the-grid.md`](../dialogs/the-grid.md) — an exploration
starting from electromagnetic impedance and arriving at a two-knob
lattice model.  That dialog contains the intuition; these files
contain the clean formulation.

## Status

See [STATUS.md](STATUS.md) for the roadmap and progress.

## Files

| File | Contents |
|------|----------|
| [foundations.md](foundations.md) | The six axioms, notation, ζ and α |
| [maxwell.md](maxwell.md) | Full derivation: lattice → Maxwell's equations |
| [gravity.md](gravity.md) | Full derivation: lattice → Einstein's equations + G |
| [lattice-geometry.md](lattice-geometry.md) | Open investigation: can ζ be derived from simplicial packing? |
| [compact-dimensions.md](compact-dimensions.md) | Hypothesis: MaSt sheets as wrapped 2D triangular lattices; can wrapping constrain α? |
| [synthesis.md](synthesis.md) | What GRID proves, what it doesn't, and where it leads |
| [dual-bubbles.md](dual-bubbles.md) | The Compton-Schwarzschild conservation law and the embedding mechanism (framing) |
| [sim-gravity/](sim-gravity/) | Complete: spring-lattice elasticity gives ε ∝ 1/r² (elastic), not 1/r (gravitational) |
| [sim-gravity-2/](sim-gravity-2/) | Design phase: entropic force via string-register Monte Carlo — testing for 1/r |
| [sim-maxwell/](sim-maxwell/) | Planned simulation: can the lattice propagate directional waves? |
| [INBOX.md](INBOX.md) | Raw ideas and open threads not yet formalized |
