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


# ---------- Relative-cos variants ---------------------------------------------
#
# Experimental candidates exploring the user's "compass dial" intuition:
# the node has a dial direction v ∈ [0, 2π); each edge has a fixed geometric
# direction θ (the line direction in space, pointing tail → head); the cos
# of (θ − v) acts as a directional weight.
#
# Polarity factor s_e (+1 head-here, −1 tail-here) is included so that at a
# head node the contribution flips sign relative to the tail node — this is
# necessary because θ is a property of the edge as a line in space (same at
# both endpoints), not a per-endpoint angle.

def _node_signed_sum_cos_relative(v, i, lattice):
    """Σ_k s_k · i_k · cos(θ_k − v_node) per node, vectorised."""
    # Broadcasting: cos has shape (n_nodes, n_edges); M (signs) has same shape.
    cos_mat = np.cos(lattice.theta[None, :] - v[:, None])
    return ((lattice.M * cos_mat) @ i)


class RelativeCosNode(Telegrapher):
    """Variant A: cos on node update only (relative to v); plain edge update."""

    name = "relcos-node"

    def update(self, state, lattice):
        v = state["v"]
        i = state["i"]
        delta = _node_signed_sum_cos_relative(v, i, lattice)
        v_new = (v + delta) % TWO_PI
        diff_pb = _principal_branch(v_new[lattice.tails] - v_new[lattice.heads])
        i_new = i + diff_pb
        return {"v": v_new, "i": i_new}


class RelativeCosEdge(Telegrapher):
    """Variant B: plain node update; cos on edge update (relative to v at each endpoint).

    Edge update reads each endpoint's phase-distance scaled by cos(θ − v_end):
        e_new = e + (φ(v_tail) · cos(θ − v_tail) − φ(v_head) · cos(θ − v_head))
    where φ(v) is the principal-branch reading of v in (−π, π], so that v
    is treated as a phase amplitude, not a raw [0, 2π) value.
    """

    name = "relcos-edge"

    def update(self, state, lattice):
        v = state["v"]
        i = state["i"]
        delta = lattice.M @ i
        v_new = (v + delta) % TWO_PI
        v_tail = v_new[lattice.tails]
        v_head = v_new[lattice.heads]
        amp_tail = _phase_distance(v_tail) * np.cos(lattice.theta - v_tail)
        amp_head = _phase_distance(v_head) * np.cos(lattice.theta - v_head)
        i_new = i + (amp_tail - amp_head)
        return {"v": v_new, "i": i_new}


class RelativeCosBoth(Telegrapher):
    """Variant C: cos relative to v on both phases."""

    name = "relcos-both"

    def update(self, state, lattice):
        v = state["v"]
        i = state["i"]
        # Node update with cos weighting
        delta = _node_signed_sum_cos_relative(v, i, lattice)
        v_new = (v + delta) % TWO_PI
        # Edge update with cos weighting
        v_tail = v_new[lattice.tails]
        v_head = v_new[lattice.heads]
        amp_tail = _phase_distance(v_tail) * np.cos(lattice.theta - v_tail)
        amp_head = _phase_distance(v_head) * np.cos(lattice.theta - v_head)
        i_new = i + (amp_tail - amp_head)
        return {"v": v_new, "i": i_new}
