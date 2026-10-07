# Junction geometry — what a node may do with edges that belong to different sheets

**Status:** Revised 2026-10-07. **An earlier version of this file was wrong**, and the correction matters: it claimed the choice of junction rule was pinned to four discrete options, which closed off weak coupling and forced an unsound patch elsewhere. The constraint it leaned on was not a real one. What follows is the corrected account.

---

## 1. The error, stated plainly

The earlier version argued that a junction rule must conserve **momentum at the node**, and derived from that a discrete set of exactly four admissible rules. Two things were wrong.

**The momentum measure was wrong.** A wave's momentum goes with its **energy flux**, as amplitude *squared* — not as amplitude. Under the correct measure:

| rule | Σ S·d (amplitude-weighted, what was used) | Σ \|S\|²·d (energy flux, physical) |
|---|---|---|
| uniform (2/N)·J − I | (−1, 0) ✓ | **(0, 0)** ✗ |
| straight-through | (−1, 0) ✓ | (−1, 0) ✓ |

So the uniform scatter does not conserve momentum at a node at all. It isotropises, which is what a diffusive scatter does.

**And the constraint was not required in the first place.** The nodes are fixed. A fixed lattice can absorb momentum — that is what crystal momentum means, conserved globally modulo reciprocal-lattice vectors rather than node by node. The only genuine per-node constraint is **unitarity**: energy in equals energy out.

## 2. What follows once the false constraint is dropped

The four-solution result goes with it. Requiring only unitarity leaves a **continuous family**. Taking S = exp(θA) with A an antisymmetric circulant gives an exactly unitary rule at every θ, with cross-coupling between the groups that rises smoothly from zero:

| θ | 0.0 | 0.1 | 0.3 | 0.6 |
|---|---|---|---|---|
| cross-coupling | 0.000 | 0.099 | 0.282 | 0.466 |

So **weak always-on coupling is available**, and the two rules that had looked like rivals are the ends of one dial: θ = 0 is the ideal node that never crosses below the ceiling, small θ the physical one that leaks a little. That is exactly the distinction already drawn in the project's own framing — the ideal node, with a real system expected to approximate it and leak slightly.

## 3. What this fixes

**Motion.** A shared coupling, however weak, gives one wave operator spanning both directions, hence the joint relation ω² = c²k² + ω₀² — which is what makes compact momentum behave as inertia and lets a massive mode travel. This is the standard Kaluza–Klein result and [grid-matter ch. 4](../../grid-matter/04-matter-waves-and-de-broglie.md) already measures it for the pooled scatter.

**It also retires a patch.** A previous version of this file argued that a moving particle must be a soliton held together by saturation at its core. **That claim is withdrawn.** It was introduced to supply motion when weak coupling looked unavailable, and it fails on its own terms: the project calibrates the ceiling so that ordinary light passes below it, and an electron has roughly a threshold photon's energy in roughly a threshold photon's volume, so its core sits *below* the ceiling too — the opposite of what the argument needed. With weak coupling restored, nothing needs the soliton.

Saturation returns to the job it was proposed for: **bulk** transfer across the boundary, which is creation and decay. Ordinary propagation of an already-made particle is carried by the weak linear coupling.

## 4. Why Maxwell is not at risk

The partition is **space against a sheet**, not dimension against dimension. Within space the ordinary scatter applies and nodes mix their spatial edges exactly as before, so the spatial sector is unchanged and Maxwell is untouched. Only the space↔sheet channel is weak. A hazard raised earlier — that a permutation rule is ballistic transport and loses interference — applies only to the dimension-by-dimension reading, which is not the proposal.

## 5. What is still open

- **How small is θ?** The ideal node is θ = 0; a physical one leaks. Whether that residue is required, and whether it is what α measures, is unsettled. It is also now a *measurable* parameter rather than a posit.
- **Does the joint dispersion actually form on this lattice?** §3 is an inference from the shared operator, not a measurement. The test is to sweep a mode's winding and x-momentum and fit ω² = c²k² + ω₀².
- **Does saturation still do its job at θ > 0?** All the overflow measurements so far are at θ = 0.
