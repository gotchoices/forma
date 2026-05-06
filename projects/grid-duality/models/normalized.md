# Normalized telegrapher

**One-line:** Telegrapher with 1/N factor on the node update, where N is the local coordination. CFL-stable at any coord; propagation speed varies with coordination.

## State

| Where | Symbol | Domain | Role |
|---|---|---|---|
| Node | v | [0, 2π) (U(1) compact) | across variable, bounded |
| Edge | i | ℝ (unbounded real) | through variable, unbounded |

Same as [Telegrapher](telegrapher.md).

## Clock

Two-phase. Same as Telegrapher.

## Update rules

**Phase 0 — node update.** For each node:

> v_node ← (v_node + (1/N) · Σ_e s_e · i_e) mod 2π

where N is this node's coordination (number of incident edges), s_e is +1 (head here) or −1 (tail here). The 1/N factor is the only difference from Telegrapher.

**Phase 1 — edge update.** Same as Telegrapher:

> i_edge ← i_edge + (v_tail − v_head)_pb

## Topology

Same as Telegrapher: node-loop windings.

## Stability

**Stable at unit time step for any coordination.** The 1/N factor in the node update reduces the effective leapfrog gain. With local coord N at each node, the per-step amplification is bounded; CFL is satisfied implicitly by the rule.

Trade-off: propagation speed in lattice units depends on coordination. A wave at coord 3 propagates more slowly per cycle than a wave at coord 2, because the node averages contributions rather than summing them. This is physically reasonable — higher-coordination lattices distribute energy across more channels — but should be verified by simulation.

## Notes

- Interpret the 1/N as *averaging over incident edges* rather than *summing*. The node treats its update as a mean of incoming flow contributions, which is a natural choice for a 0D scalar accumulator on a graph with arbitrary coordination.
- Inspired by sim-maxwell's (2/N)·J factor in the scattering matrix; the normalization plays the same CFL-stabilizing role here.
- For coord 2 (1D linear): 1/N = 1/2. Propagation speed is reduced relative to Telegrapher (which is at unit speed in 1D).
- For irregular lattices (varying coord per node), the 1/N factor is local — each node uses its own coord. This keeps the rule local without needing global lattice information.
- This is the most pragmatic of the bond-graph candidates. If it passes the comparison tests, it's a strong contender for the winning model.
