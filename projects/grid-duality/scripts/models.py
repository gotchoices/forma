"""Candidate models for grid-duality.

Each model implements:
- init_state(lattice) — returns initial state (zeros).
- update(state, lattice) — one full clock cycle, returns new state.
- perturb_node(state, idx, value) / perturb_edge(state, idx, value) — apply a delta.
- node_observable(state) — paradigm-neutral per-node scalar in a comparable range.
- edge_observable(state) — paradigm-neutral per-edge scalar.
- total_energy(state) — model-natural scalar tracking conservation.

Reference specs live under projects/grid-duality/models/<name>.md.
"""

import numpy as np

TWO_PI = 2.0 * np.pi


def _principal_branch(x):
    """Reduce a real-valued array to (−π, π]."""
    return ((x + np.pi) % TWO_PI) - np.pi


def _phase_distance(v):
    """Map U(1) phase v ∈ [0, 2π) to its signed distance from 0 in (−π, π]."""
    return _principal_branch(v)


# ---------- Base ----------

class Model:
    """Abstract base for candidate models. See models/<name>.md for full specs."""

    name = "base"

    def init_state(self, lattice):
        raise NotImplementedError

    def update(self, state, lattice):
        raise NotImplementedError

    def perturb_node(self, state, idx, value):
        raise NotImplementedError

    def perturb_edge(self, state, idx, value):
        raise NotImplementedError

    def node_observable(self, state):
        raise NotImplementedError

    def edge_observable(self, state):
        raise NotImplementedError

    def total_energy(self, state):
        raise NotImplementedError


# ---------- Telegrapher ----------

class Telegrapher(Model):
    """v on nodes ∈ U(1); i on edges ∈ ℝ. Signed sum at nodes (mod 2π);
    principal-branch difference at edges. Two-phase clock (node first).
    """

    name = "telegrapher"

    def init_state(self, lattice):
        return {
            "v": np.zeros(lattice.n_nodes),
            "i": np.zeros(lattice.n_edges),
        }

    def update(self, state, lattice):
        v = state["v"]
        i = state["i"]
        # Phase 0 — node update: v_new = (v + Σ s · i) mod 2π
        delta = lattice.M @ i
        v_new = (v + delta) % TWO_PI
        # Phase 1 — edge update: i_new = i + (v_tail − v_head)_pb
        diff_pb = _principal_branch(v_new[lattice.tails] - v_new[lattice.heads])
        i_new = i + diff_pb
        return {"v": v_new, "i": i_new}

    def perturb_node(self, state, idx, value):
        new_v = state["v"].copy()
        new_v[idx] = (new_v[idx] + value) % TWO_PI
        return {"v": new_v, "i": state["i"]}

    def perturb_edge(self, state, idx, value):
        new_i = state["i"].copy()
        new_i[idx] = new_i[idx] + value
        return {"v": state["v"], "i": new_i}

    def node_observable(self, state):
        # Phase distance from 0 in (−π, π], for symmetric plotting around zero.
        return _phase_distance(state["v"])

    def edge_observable(self, state):
        return state["i"].copy()

    def total_energy(self, state):
        v_obs = self.node_observable(state)
        i = state["i"]
        return 0.5 * (np.sum(v_obs ** 2) + np.sum(i ** 2))


# ---------- Normalized Telegrapher ----------

class NormalizedTelegrapher(Telegrapher):
    """Like Telegrapher but with a 1/N factor on the node update,
    where N is the local coordination at each node. This handles CFL
    stability at any coordination at unit time step."""

    name = "normalized"

    def update(self, state, lattice):
        v = state["v"]
        i = state["i"]
        # Phase 0 — node update: averaged signed sum of incident edges
        # (1/N factor where N = local coordination)
        delta = (lattice.M @ i) / lattice.coord
        v_new = (v + delta) % TWO_PI
        # Phase 1 — edge update: same as Telegrapher
        diff_pb = _principal_branch(v_new[lattice.tails] - v_new[lattice.heads])
        i_new = i + diff_pb
        return {"v": v_new, "i": i_new}
