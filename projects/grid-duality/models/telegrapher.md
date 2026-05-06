# Telegrapher

**One-line:** Bounded across (voltage-like) on nodes; unbounded through (current-like) on edges. Two-phase clock with signed-sum at nodes and principal-branch difference at edges.

## State

| Where | Symbol | Domain | Role |
|---|---|---|---|
| Node | v | [0, 2π) (U(1) compact) | across variable — "voltage" / "level" / "potential," bounded |
| Edge | i | ℝ (unbounded real) | through variable — "current" / "flow," unbounded |

## Clock

Two-phase. One full clock cycle is one node-phase followed by one edge-phase. Nodes and edges never update simultaneously.

## Update rules

**Phase 0 — node update.** For each node:

> v_node ← (v_node + Σ_e s_e · i_e) mod 2π

where the sum runs over edges incident at this node, i_e is the value of edge e, and s_e = +1 if this node is the *head* of edge e, −1 if this node is the *tail*. The sign reflects Kirchhoff-style continuity: incoming flow increases the node's level, outgoing flow decreases it.

**Phase 1 — edge update.** For each edge:

> i_edge ← i_edge + (v_tail − v_head)_pb

where (·)_pb denotes principal-branch reduction to (−π, π]. The reduction is necessary because both endpoints live in [0, 2π); without it, the literal difference can range over (−2π, 2π) and the integration becomes ambiguous near the wrap-around.

## Topology

Closed loops *through nodes* accumulate principal-branch differences that sum to 2π·k for integer k — the **node-loop winding number**. Topological invariants live on these node-loop windings.

This is matter-field-on-nodes flavor: the node hosts a U(1) compact phase analogous to a Higgs-style scalar field. The gauge structure is implicit in the edge values rather than stored as a U(1) link variable.

## Stability

- **1D linear array** (coord 2): marginally stable at unit time step. Eigenvalues on the unit circle.
- **2D hex** (coord 3): unstable at unit time step. CFL bound γ ≤ √(2/N) violated. Per-step changes at junctions are large; transient dynamics become erratic.
- **Higher coordination**: progressively worse without normalization.

## Notes

- This is the bond-graph telegrapher's-equations discretization with implicit L = C = 1 per primitive.
- Power conservation in steady state: at any node, Σ s_e · i_e = 0 implies Kirchhoff balance. For a sustained drive at a Y-junction with one input and two outputs, steady state has i_in = i_out_1 + i_out_2 (current splits equally if symmetric).
- Single-pulse 2D transients show amplification at junctions because the rule lets edges read the full v_node onto their integration, doubling apparent amplitude. This is the issue the comparison test bench will measure.
- Without 2D regularization, this model is expected to fail the 2D wavefront and 2D Y-junction tests. See the Normalized variant for one fix.

## Bounded vs unbounded phase

The default model carries v on the compact circle U(1) — every step applies (v + delta) mod 2π, discarding any winding accumulation. The implementation supports a `wrap_node = False` flag that drops the wrap (and the principal-branch reduction in the edge update), turning v into an unbounded ℝ variable. The test [scripts/test_unbounded_phase.py](../scripts/test_unbounded_phase.py) probes whether the wrap is doing thermodynamic-style work (allowing relaxation by discarding winding entropy) or whether it is purely representational.

Result for Telegrapher: 100-step 2D pulse on a 14×14 hex torus.

| Variant | Energy ratio after 100 steps |
|---|---|
| wrap_node=True (default) | 4.6 × 10⁴ |
| wrap_node=False | 6.3 × 10¹⁰⁵ (numerical overflow) |

The wrap *mitigates* but does not *fix* Telegrapher's CFL instability at coord 3. With the wrap, v stays in [0, 2π), which caps the magnitude of v's drift and slows the cross-coupling with i (which remains on ℝ in both modes). Without the wrap, both v and i grow without bound and the divergence accelerates dramatically. The wrap is a *symptom-suppressor*, not a stabilizer: the underlying CFL violation is unaffected.

The user's hypothesis going in was that the wrap enables cooling/relaxation by discarding winding accumulation. The data does not support this for Telegrapher: removing the wrap makes the divergence worse, not different in kind, and the relaxation probe (Dirichlet-pinned, damped, 800 steps) crashes outright in unbounded mode. Cooling, where it appears at all in the v-i family, comes from the *damping* term and the *static-limit-equals-Laplacian* property — not from phase wrapping. See the Normalized variant, which is bit-identical with and without the wrap (the wrap is "armed but never fires" in stable regimes).
