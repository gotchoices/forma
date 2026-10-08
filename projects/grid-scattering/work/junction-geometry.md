# Junction geometry — what a node may do with edges that belong to different sheets

**Status:** Cut back 2026-10-07. This file has been wrong twice, in opposite
directions, and what survives is small. Numbers:
[measurements.md](measurements.md).

1. The first version claimed the junction rule was pinned to **four discrete
   options**, which closed off weak coupling and forced an unsound patch
   elsewhere. The constraint it leaned on was not real.
2. The second version then argued that *any* shared coupling, however weak,
   would give a joint wave operator and hence Kaluza–Klein motion. That was an
   inference, not a measurement, and the couplings built on it all failed.

---

## 1. The false constraint

The first version argued that a junction rule must conserve **momentum at the
node**, and derived from that exactly four admissible rules. Two things were
wrong.

**The momentum measure was wrong.** A wave's momentum goes with its **energy
flux**, as amplitude *squared* — not as amplitude:

| rule | Σ S·d (amplitude-weighted, what was used) | Σ \|S\|²·d (energy flux, physical) |
|---|---|---|
| pooled (2/N)·J − I | (−1, 0) ✓ | **(0, 0)** ✗ |
| straight-through | (−1, 0) ✓ | (−1, 0) ✓ |

So the pooled scatter does not conserve momentum at a node at all. It
isotropises, which is what a diffusive scatter does.

**And the constraint was not required in the first place.** The nodes are fixed,
and a fixed lattice absorbs momentum — that is what crystal momentum means,
conserved globally modulo reciprocal-lattice vectors rather than node by node.
The only genuine per-node constraint is **unitarity**: energy in equals energy
out.

## 2. What that leaves

Requiring only unitarity leaves a **continuous family**. Taking S = exp(θA) with
A an antisymmetric circulant gives an exactly unitary rule at every θ, with
cross-coupling between the groups rising smoothly from zero:

| θ | 0.0 | 0.1 | 0.3 | 0.6 |
|---|---|---|---|---|
| cross-coupling | 0.000 | 0.099 | 0.282 | 0.466 |

So weak always-on coupling is *available*. What this file previously inferred
from that — that it would therefore supply motion — is withdrawn (§3).

## 3. The inference that failed

The second version argued: a shared coupling, however weak, gives one wave
operator spanning both directions, hence ω² = c²k² + ω₀², hence a massive mode
that travels. Each step is standard Kaluza–Klein and the conclusion is true of
the *right* coupling. It is not true of an arbitrary one, and the three tried
all failed:

- a **constant** rotation is algebraically a mass term, so it gives light a gap
  equal to the rotation angle;
- a **gradient** coupling g·(1 − cos k_c) keeps light massless but pairs `+x`
  with `+c` and `−x` with `−c`, so each compact direction hybridises with only
  one x direction: the band is not even in k_x and a mode at rest drifts at
  +0.107;
- a **saturation-bound soliton** contradicts the project's own ceiling
  calibration, since by "light must pass" an electron's core sits below the
  ceiling.

All three are recorded in [§M7](measurements.md).

**The reason none was needed.** The motivation for building a bespoke rule was
to keep the compact sectors from mixing below the ceiling. That needs no rule:
on a translation-invariant lattice the compact wavenumber is a Bloch label, so
no linear rule mixes wound with unwound content, the pooled scatter included
([§M2](measurements.md), exactly zero at every amplitude). And the pooled
scatter supplies the motion to 0.1%, even in k_x exactly, with group velocity
exactly zero at rest — while being node-local and reciprocal, which none of the
bespoke rules were ([§M3](measurements.md)).

So the project's linear sector is the **ordinary pooled scatter**, and this file
contributes nothing to it. What remains distinctive is the **nonlinear**
overflow channel.

## 4. Why Maxwell is not at risk

The partition is **space against a sheet**, not dimension against dimension.
Within space the ordinary scatter applies and nodes mix their spatial edges
exactly as before, so the spatial sector is unchanged and Maxwell is untouched.
A hazard raised earlier — that a permutation rule is ballistic transport and
loses interference — applies only to the dimension-by-dimension reading, which
is not the proposal.

## 5. What is still open

- **Is θ > 0 required?** The ideal node is θ = 0; a physical one might leak.
  Whether that residue is required, and whether it is what α measures, is
  unsettled. It is a measurable parameter rather than a posit, but nothing in
  this project now needs it to be nonzero.
- **Is the overflow rule reciprocal enough?** It carries the same `+x↔+c` /
  `−x↔−c` pairing that broke the gradient coupling. It does no harm in the
  window where motion survives (even in k_x to 5 × 10⁻⁵) but leaks asymmetry in
  the pinned regime. This is the project's cheapest open experiment
  ([STATUS.md](STATUS.md) E1).
