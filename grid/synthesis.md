# GRID Synthesis

What the Geometric Relational Interaction Domain establishes,
what it does not, and where it leads.

---

## The claim

Electromagnetism and general relativity share a common geometric
origin: both emerge from a minimal discrete lattice defined by
six axioms and two free parameters.

This is not a Grand Unified Theory (GUT) in the traditional
sense — GRID does not touch the weak or strong forces.  It is
something more specific: **a common substrate for the two
long-range forces**, derived from first principles without
importing either Maxwell's equations or Einstein's equations.

---

## What was derived

### From axioms A1–A4 and A6: Maxwell's equations

Starting from a 4D causal lattice (A1) with Lorentzian
signature (A2), periodic phase per cell (A3), local gauge
invariance (A4), and coupling strength α (A6):

- Gauge invariance forces the lattice to carry **link variables**
  (A_μ) in addition to cell phases (θ)
- The field tensor F_μν emerges from plaquette holonomies
- The (1,3) signature splits F_μν into electric (E) and
  magnetic (B) fields
- The principle of least action yields the inhomogeneous
  Maxwell equations (Gauss's law, Ampère's law)
- The Bianchi identity yields the homogeneous Maxwell equations
  (Faraday's law, no monopoles)
- Charge quantization follows from phase periodicity
- Charge conservation follows as a theorem

**Full derivation:** [maxwell.md](maxwell.md)

### From axioms A1, A2, and A5: Einstein's field equations

Starting from the same lattice (A1) with the same signature
(A2), plus the information resolution ζ (A5):

- Any causal horizon on the lattice has entropy S = ζ · A
- Energy flowing through a local Rindler horizon deposits
  heat (Clausius relation: δQ = TδS)
- The Unruh effect sets the horizon temperature
- The Raychaudhuri equation converts curvature into area change
- Combining these yields the Einstein field equations:
  G_ab + Λg_ab = (2π/ζ) T_ab
- Newton's constant reads off as G = 1/(4ζ)
- The cosmological constant Λ appears for free as an
  integration constant
- **Spacetime bends around mass because energy flow through
  causal horizons forces geometric change**

**Full derivation:** [gravity.md](gravity.md)

---

## One lattice, two forces, two mechanisms

| | Electromagnetism | Gravity |
|--|------------------|---------|
| **What emerges** | Maxwell's equations, E, B, charge | Einstein's equations, G, Λ |
| **Axioms used** | A1, A2, A3, A4, A6 | A1, A2, A5 |
| **Free parameter** | α (coupling strength) | ζ (information resolution) |
| **Mechanism** | Dynamics — gauge symmetry of phases | Thermodynamics — entropy of horizons |
| **Nature of the force** | Mechanical — propagating disturbances in link states | Statistical — emergent from information flow |
| **Carrier** | Photon (link-state wave) | Graviton (not explicitly derived) |

The two forces share the lattice (A1) and the causal structure
(A2), but draw on different features:

- **EM** uses the internal structure of the lattice: phases on
  cells, connections on links, gauge symmetry.
- **Gravity** uses the information-theoretic structure: how
  many bits the lattice encodes per unit area.

This explains the hierarchy: α ≈ 1/137 is a moderate coupling
(link phases interact at every tick), while G in everyday units
is fantastically weak (you need ~10⁶⁰ cells' worth of area to
encode enough entropy for gravity to matter).  EM is a local
phase interaction; gravity is a collective statistical effect.

---

## What was NOT derived

Honesty about the boundaries is essential.

**The value of α.**  The fine-structure constant is a measured
input (axiom A6), not derived.  GRID takes α ≈ 1/137.036 as
given.  MaSt also takes α as input.  Whether α can be derived
from deeper structure (perhaps from ζ via a consistency
condition) is an open question
(see [foundations.md](foundations.md), Q2).

**The value of ζ.**  The information resolution is a free
parameter (axiom A5).  The lattice geometry investigation
([lattice-geometry.md](lattice-geometry.md)) proposes that ζ
may follow from the cell packing — the leading candidate is
ζ = 1/6 from a 4D simplicial lattice — but this is
exploratory, not proven.

**The weak and strong forces.**  GRID produces only U(1) gauge
theory (electromagnetism).  The SU(2) × SU(3) structure of the
weak and strong forces would require richer internal degrees of
freedom beyond a single phase per cell.  Within the MaSt
framework, the strong force may be the full internal EM
interaction at short range (Q95), but this is not derived from
GRID axioms.

**Quantum mechanics.**  The Maxwell derivation is classical.
The gravity derivation uses the Unruh effect, which assumes
quantum field theory.  GRID does not derive QM from the
lattice — it assumes that the lattice, when quantized, produces
standard QFT.  This is the well-established claim of lattice
gauge theory, but GRID has not proven it independently.

**Particle masses and spectrum.**  These are MaSt's domain.
GRID provides the field equations; MaSt provides the compact
geometry (Material Space) that confines photons into massive
particles.

**The graviton.**  The Einstein equations emerge as an equation
of state (thermodynamic).  A propagating graviton (quantized
spin-2 excitation) is not derived.  Whether the lattice supports
graviton-like excitations is an open question.

---

## Constants inventory

What has GRID derived, what is input, and what remains?

### Derived from the lattice

| Constant / relation | How it emerges | Derivation |
|---------------------|----------------|------------|
| Maxwell's equations (all 4) | Gauge invariance + least action | [maxwell.md](maxwell.md) |
| Einstein field equations | Thermodynamics of information | [gravity.md](gravity.md) |
| G = 1/(4ζ) | Coefficient in Einstein equations | [gravity.md](gravity.md) |
| Λ (cosmological constant) | Integration constant from Bianchi identity | [gravity.md](gravity.md) |
| Spacetime stiffness c⁴/(8πG) = ζ/(2π) | Rearrangement of G | [gravity.md](gravity.md) |
| e = √(4πα) | Charge from coupling constant | [maxwell.md](maxwell.md) |
| Charge quantization | Phase periodicity → topological winding | [maxwell.md](maxwell.md) |
| Charge conservation (∂_μJ^μ = 0) | Antisymmetry of F^μν | [maxwell.md](maxwell.md) |
| E = ℏω (energy ∝ frequency) | Quadratic action → wave equation | Implicit in [maxwell.md](maxwell.md) |
| λ = h/p (de Broglie) | Fourier relation on the lattice | Implicit in wave mechanics |
| ε₀ = μ₀ = 1 (natural units) | Single coupling α unifies them | [foundations.md](foundations.md) |

### Input parameters (not derived)

| Constant | Role in GRID | Status |
|----------|-------------|--------|
| α ≈ 1/137 | Coupling strength (A6) | Measured input — the single unsolved number |
| ζ | Information resolution (A5) | Free parameter; may follow from packing geometry ([lattice-geometry.md](lattice-geometry.md)) |

### Unit-system constants (definitional, not physical)

| Constant | What it means in the lattice |
|----------|------------------------------|
| c | One cell per tick — defines the relationship between length and time units |
| ℏ | One phase cycle per Planck energy — defines energy units in terms of frequency |
| k_B | One bit per Planck temperature — defines temperature units |
| L (Planck length) | Grain size = 1 by definition |

These are not "derived" or "unexplained" — they are unit
conversions between human-scale SI and the lattice's natural
scales.  Their SI values (c = 3×10⁸ m/s, etc.) reflect the
ratio between human units and Planck units.

### What remains unexplained

| Mystery | Status |
|---------|--------|
| Why α ≈ 1/137 | Open — the single most important unsolved parameter |
| Why ζ = 1/4 (or 1/6) | Exploratory — may follow from packing geometry |
| Why 4 dimensions | Assumed (A1) |
| Why (1,3) signature | Assumed (A2) |
| Value of Λ | Appears as free integration constant — not predicted |

---

## The energy budget question

If every cell computes a new state every Planck tick, what
powers the computation?

Three observations suggest this may not be a real problem:

1. **Zero-energy universe.**  The total energy of the universe
   may be exactly zero: positive matter/radiation energy
   cancelled by negative gravitational potential energy
   (Tryon 1973).  The lattice doesn't consume energy — it IS
   the energy.

2. **Reversible computation.**  Quantum mechanics is unitary —
   evolution preserves information.  By Landauer's principle,
   only irreversible (information-destroying) computation has a
   thermodynamic cost.  A reversible cellular automaton runs
   for free.

3. **No external substrate.**  The lattice is not running on a
   computer.  It is not a simulation.  The cells and their
   update rules ARE reality.  Asking "what powers the lattice?"
   is like asking "what powers the laws of physics?" — it may
   be a category error.

This is not settled, but the question may dissolve rather than
require an answer.

---

## GRID + MaSt: the full stack

GRID alone covers the two long-range forces.  But MaSt extends
the picture to particles, masses, and potentially the short-
range forces — all from the same electromagnetic substrate.

```
GRID (substrate layer)
    Inputs:  ζ, α
    Outputs: Maxwell's equations, G, Λ
                │
                ▼
MaSt (architecture layer)
    Inputs:  Maxwell + α (provided by GRID)
    Outputs: particle spectrum, masses, charges,
             nuclear structure, dark matter candidates,
             strong force mechanism, weak force (open)
```

Together, the two layers attempt a complete account of
fundamental physics from two free parameters:

| Force | Layer | Mechanism | Status |
|-------|-------|-----------|--------|
| Electromagnetism | GRID | Phase dynamics + gauge invariance | **Derived** |
| Gravity | GRID | Thermodynamics of information | **Derived** |
| Strong | MaSt | Full internal EM at overlap range (Q95) | **Plausible** — qualitative features match |
| Weak | MaSt | Collective Ma excitations? (Q96) | **Open** |

**What GRID provides to MaSt:**
- Maxwell's equations — previously assumed, now derived
- The gravitational constant G — previously unaddressed
- A physical picture: particles (confined photons on Ma) live
  on a discrete lattice whose phase dynamics produce EM and
  whose information density produces gravity

**What MaSt provides that GRID cannot:**
- Particle masses (from compact geometry)
- The charge mechanism (from sheet shear)
- Nuclear structure (from Ma_p modes)
- The predictive spectrum below 2 GeV
- The strong force as unscreened internal EM (Q95)

**Shared open question:** what determines α?

The compact-dimensions investigation
([compact-dimensions.md](compact-dimensions.md)) showed that
wrapping 2D triangular sheets into tori discretizes α but does
not uniquely determine it — the lattice spectrum is dense
enough that essentially any coupling constant is achievable.
Conclusion: **α is a designer's choice within the available
discrete steps.**  A selection principle (energy minimization,
topological constraint, or something else) remains unknown.

If the strong force mechanism (Q95) is confirmed quantitatively
and the weak force finds a geometric explanation within MaSt,
then GRID + MaSt would constitute a complete geometric account
of all four fundamental forces, the particle spectrum, and
gravity — from two numbers and a lattice.

---

## Open questions

### Foundational

| Question | Status | Reference |
|----------|--------|-----------|
| Can ζ be derived from packing geometry? | Leading candidate: ζ = 1/6 from 4D simplex | [lattice-geometry.md](lattice-geometry.md) |
| Are ζ and α related? | Unknown — treated as independent | [foundations.md](foundations.md), Q2 |
| Why 4 dimensions? | Assumed (A1), not derived | [foundations.md](foundations.md), Q3 |
| Why (1,3) signature? | Assumed (A2), not derived | [foundations.md](foundations.md), Q4 |

### Physical

| Question | Status | Reference |
|----------|--------|-----------|
| Can the lattice support non-abelian gauge symmetry? | Open — would need richer cell structure | — |
| Does lattice quantization reproduce standard QFT? | Expected from lattice gauge theory, not proven within GRID | — |
| What is the graviton in this picture? | Not derived — gravity is thermodynamic, not mechanical | — |
| How does the lattice handle topology change? | Open — relevant for black hole evaporation | — |

### Philosophical

| Question | Status | Reference |
|----------|--------|-----------|
| What powers the computation? | Likely a category error (see above) | — |
| Is the lattice deterministic or probabilistic? | Open — QM suggests probabilistic, but 't Hooft argues deterministic substrate is possible | — |
| Does the lattice have a boundary? | Open — related to cosmological horizon and Λ | — |

---

## Summary

Six axioms.  Two free parameters.  Two forces from the lattice,
potentially four from the full stack.

GRID demonstrates that electromagnetism and general relativity
share a common origin in a minimal discrete lattice —
without importing either one.  The electromagnetic field is the
dynamics of phase connections between cells.  Gravity is the
thermodynamics of information encoded in those cells.  Both live
on the same substrate; they emerge through different mechanisms
from the same small set of rules.

MaSt builds on this substrate: confining photons on compact
geometry to produce particles, masses, and charges — with a
plausible mechanism for the strong force (Q95) and open work
on the weak force (Q96).  Together, GRID + MaSt attempt a
geometric account of fundamental physics from two numbers
and a lattice.

What remains: fixing the two free parameters (ζ from geometry,
α from a selection principle or measurement), confirming the
strong force mechanism quantitatively, finding a weak force
mechanism, and connecting to quantum mechanics.  The lattice
geometry investigation offers a path to reducing ζ from a free
parameter to a geometric consequence.  The compact-dimensions
study showed that α, while discretized by the lattice, is
not uniquely constrained — it remains a free parameter whose
value must be set by additional physics or taken from
experiment.
