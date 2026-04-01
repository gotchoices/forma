"""Energy minimization of the spring lattice with frozen vertices.

Uses scipy.optimize.minimize (L-BFGS-B) to find the equilibrium
configuration that minimises the total elastic energy:

    E = (k/2) Σ_edges (|r_i − r_j| − L₀)²

Frozen vertices are excluded from the optimisation variables.
All inner loops are vectorised with numpy for performance.
"""

import numpy as np
from scipy.optimize import minimize


def _build_free_map(n_verts, frozen):
    """Map from vertex index to free-variable index (or -1 if frozen)."""
    free_map = np.full(n_verts, -1, dtype=int)
    count = 0
    for i in range(n_verts):
        if i not in frozen:
            free_map[i] = count
            count += 1
    free_idx = np.where(free_map >= 0)[0]
    return free_idx, free_map


def _energy_and_grad(x_free, free_idx, pos_template, edges,
                     rest_lengths, k):
    """Vectorised elastic energy and gradient."""
    pos = pos_template.copy()
    pos[free_idx] = x_free.reshape(-1, 2)

    a_idx = edges[:, 0]
    b_idx = edges[:, 1]

    d = pos[a_idx] - pos[b_idx]                    # (E, 2)
    lengths = np.sqrt(np.sum(d * d, axis=1))        # (E,)
    lengths = np.maximum(lengths, 1e-15)

    dl = lengths - rest_lengths                     # (E,)
    energy = 0.5 * k * np.sum(dl * dl)

    scale = (k * dl / lengths)[:, None]             # (E, 1)
    force = scale * d                               # (E, 2)

    grad = np.zeros_like(pos)
    np.add.at(grad, a_idx, force)
    np.subtract.at(grad, b_idx, force)

    return energy, grad[free_idx].ravel()


def relax(pos: np.ndarray, edges: np.ndarray,
          rest_lengths: np.ndarray, frozen: frozenset,
          k: float = 1.0, tol: float = 1e-10,
          maxiter: int = 5000) -> tuple[np.ndarray, float]:
    """Minimise spring energy, holding *frozen* vertices fixed.

    Parameters
    ----------
    pos : (N, 2) initial positions (not modified)
    edges : (E, 2) edge list
    rest_lengths : (E,) rest lengths
    frozen : set of vertex indices that don't move
    k : spring constant
    tol : convergence tolerance for L-BFGS-B
    maxiter : max iterations

    Returns
    -------
    pos_relaxed : (N, 2) relaxed positions
    final_energy : total elastic energy at equilibrium
    """
    free_idx, _ = _build_free_map(len(pos), frozen)

    if len(free_idx) == 0:
        return pos.copy(), 0.0

    x0 = pos[free_idx].ravel().copy()

    result = minimize(
        _energy_and_grad,
        x0,
        args=(free_idx, pos, edges, rest_lengths, k),
        method="L-BFGS-B",
        jac=True,
        options={"maxiter": maxiter, "ftol": tol, "gtol": tol},
    )

    pos_out = pos.copy()
    pos_out[free_idx] = result.x.reshape(-1, 2)
    return pos_out, result.fun
