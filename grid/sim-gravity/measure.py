"""Displacement and strain field analysis.

Two measurement strategies:

1. **Displacement u(r)** — vertex shift from equilibrium.
   Analog of gravitational potential.  2D prediction: u ∝ log(r).
   Sensitive to boundary conditions.

2. **Edge strain ε(r)** — fractional edge-length change |Δl|/l₀.
   Analog of gravitational force / tidal field.  2D prediction: ε ∝ 1/r.
   Purely local, insensitive to boundary artifacts.

Strategy 2 is the primary diagnostic; Strategy 1 is secondary.
"""

import numpy as np


# ---------- displacement (potential) ----------

def displacement_field(pos_eq, pos_relaxed, exclude, centre):
    """(distance, displacement_magnitude) for non-excluded vertices."""
    free = sorted(set(range(len(pos_eq))) - exclude)
    disp = pos_relaxed[free] - pos_eq[free]
    u = np.sqrt(np.sum(disp ** 2, axis=1))
    r = np.sqrt(np.sum((pos_eq[free] - centre) ** 2, axis=1))
    return r, u


# ---------- edge strain (force / tidal field) ----------

def edge_strain_field(pos_eq, pos_relaxed, edges, rest_lengths,
                      centre, exclude_verts=frozenset()):
    """Fractional edge-length deviation as a function of distance.

    For each edge, compute:
      ε = |l_relaxed − l₀| / l₀
    and assign it a radial position = midpoint distance from centre.

    Edges touching excluded vertices are dropped.

    Returns (r_edge, eps) arrays.
    """
    a_idx = edges[:, 0]
    b_idx = edges[:, 1]

    d_eq = pos_eq[a_idx] - pos_eq[b_idx]
    d_rel = pos_relaxed[a_idx] - pos_relaxed[b_idx]

    l_rel = np.sqrt(np.sum(d_rel ** 2, axis=1))
    eps = np.abs(l_rel - rest_lengths) / rest_lengths

    mid = 0.5 * (pos_eq[a_idx] + pos_eq[b_idx])
    r_edge = np.sqrt(np.sum((mid - centre) ** 2, axis=1))

    if exclude_verts:
        exc = np.array(sorted(exclude_verts))
        a_ok = ~np.isin(a_idx, exc)
        b_ok = ~np.isin(b_idx, exc)
        keep = a_ok & b_ok
        r_edge = r_edge[keep]
        eps = eps[keep]

    return r_edge, eps


# ---------- binning ----------

def bin_radial(r, y, n_bins=60):
    """Azimuthally average into radial bins.

    Returns (r_mid, y_mean, y_std, counts) for bins with ≥ 2 samples.
    """
    r_max = r.max()
    edges = np.linspace(0, r_max, n_bins + 1)
    r_mid, y_mean, y_std, counts = [], [], [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        mask = (r >= lo) & (r < hi)
        if mask.sum() < 2:
            continue
        r_mid.append(0.5 * (lo + hi))
        y_mean.append(y[mask].mean())
        y_std.append(y[mask].std())
        counts.append(mask.sum())
    return (np.array(r_mid), np.array(y_mean),
            np.array(y_std), np.array(counts))


# ---------- fitting ----------

def fit_log(r_mid, u_mean, r_min=2.0, r_max=None):
    """Fit u = A · log(r) + B.  Returns (A, B, u_fit, R²)."""
    if r_max is None:
        r_max = r_mid.max() * 0.7
    mask = (r_mid >= r_min) & (r_mid <= r_max) & (u_mean > 0)
    if mask.sum() < 3:
        return np.nan, np.nan, np.full_like(r_mid, np.nan), 0.0

    log_r = np.log(r_mid[mask])
    u_data = u_mean[mask]

    A_mat = np.column_stack([log_r, np.ones_like(log_r)])
    coeffs, *_ = np.linalg.lstsq(A_mat, u_data, rcond=None)
    A, B = coeffs

    u_pred = A * log_r + B
    ss_res = np.sum((u_data - u_pred) ** 2)
    ss_tot = np.sum((u_data - u_data.mean()) ** 2)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    return A, B, A * np.log(r_mid) + B, r2


def fit_power_law(r, y, r_min=3.0, r_max=None):
    """Fit |y| = A · r^(−p) on log-log.  Returns (p, A, y_fit, R²)."""
    if r_max is None:
        r_max = r.max() * 0.7
    mask = (r >= r_min) & (r <= r_max) & (y > 0)
    if mask.sum() < 3:
        return np.nan, np.nan, np.full_like(r, np.nan), 0.0

    log_r = np.log(r[mask])
    log_y = np.log(y[mask])

    coeffs = np.polyfit(log_r, log_y, 1)
    slope = coeffs[0]
    p = -slope
    A = np.exp(coeffs[1])

    y_pred = coeffs[0] * log_r + coeffs[1]
    ss_res = np.sum((log_y - y_pred) ** 2)
    ss_tot = np.sum((log_y - log_y.mean()) ** 2)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    return p, A, A * r ** (-p), r2
