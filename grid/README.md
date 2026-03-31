# GRID — Geometric Relational Interaction Domain

## What this is

GRID is the substrate layer beneath [MaSt](../README.md).

MaSt takes Maxwell's equations and the fine-structure constant α as
*inputs* and builds particles from confined photons on compact
geometry.  GRID asks: where do Maxwell's equations come from?  What
determines α?  And can gravity (G) emerge from the same foundation?

The approach: start from a minimal discrete lattice — cells, phases,
nearest-neighbor coupling — and derive the continuum physics that MaSt
assumes.  Two free parameters.  Everything else is emergent.

## The two knobs

| Symbol | Name | Value | What it controls |
|--------|------|-------|------------------|
| ζ | Resolution | 1/4 | Bits per Planck cell — the information density of the substrate.  Determines gravitational coupling G. |
| α | Coupling | ≈ 1/137.036 | Electromagnetic interaction strength — energy cost of a topological defect relative to the lattice scale.  Determines ε₀, μ₀, e. |

**ζ** (zeta) is the Bekenstein-Hawking factor: a horizon of area A
carries entropy S = ζ · A / L² (in Planck units).  It sets the
resolution of reality — how many lattice cells constitute one bit
of physical information.  With ζ = 1/4, four cells encode one bit.

**α** is a measured input — the single free coupling constant of
the lattice gauge theory.  MaSt also takes α as input (R15, R19,
R31–R36).  GRID does not attempt to derive it (at least for the moment).

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

### 3. The stiffness of spacetime

The quantity c⁴/(8πG) has units of force (newtons) and represents
the rigidity of spacetime against deformation.  Derive this from
ζ and show how it connects to the electromagnetic stiffness
(ε₀, μ₀) through the shared lattice origin.

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
| [foundations.md](foundations.md) | The six axioms, notation, the two knobs |
| [maxwell.md](maxwell.md) | Maxwell derivation from lattice *(planned)* |
| [gravity.md](gravity.md) | G derivation in natural + SI units *(planned)* |
| [stiffness.md](stiffness.md) | Spacetime stiffness and EM–gravity link *(planned)* |
| [lattice-geometry.md](lattice-geometry.md) | Open investigation: can ζ = 1/4 be derived from simplicial packing? |
| [synthesis.md](synthesis.md) | Unification summary, open questions *(planned)* |
