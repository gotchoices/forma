"""
R63 Track 11 Phase 11b — Curved-donut compound vs separated audit.

Tests whether the SL eigenvalue at the deuteron-compound primitive
(n_pt, n_pr) = (6, 12) on the curved-donut p-sheet metric differs
from 4·λ(3, 6) (i.e., is k-linearity broken by curvature?).

Under flat geometry (R62 derivation 4):
  μ²_flat(6, 12) = 4 · μ²_flat(3, 6)  exactly  → m_compound = 2·m_proton

Under curved-donut SL spectrum:
  λ(6, 12) may differ from 4·λ(3, 6).  If λ(6, 12) < 4·λ(3, 6), the
  compound mode is lighter than 2·m_p → curvature-induced binding.

Conditional on Phase 11a's outcome (which showed curvature shatters
the meson inventory): 11b tests whether the binding question itself
gets a definite answer at curved geometry, even if curvature
isn't viable as the global mass mechanism.

Output: outputs/track11_phase11b_compound.csv
"""

import sys
import os
import math
import csv
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
from scipy import linalg


def build_sl_eigensystem(eps, q_eff, N=512):
    h = 2 * math.pi / N
    theta = np.array([2 * math.pi * j / N for j in range(N)])
    p = 1 + eps * np.cos(theta)
    p_plus  = (p + np.roll(p, -1)) / 2
    p_minus = (p + np.roll(p, +1)) / 2
    main_diag = (p_minus + p_plus) / h**2 + (eps**2 * q_eff**2) / p
    upper_diag = -p_plus / h**2
    lower_diag = -p_minus / h**2
    S = np.zeros((N, N))
    for j in range(N):
        S[j, j] = main_diag[j]
        S[j, (j + 1) % N] = upper_diag[j]
        S[j, (j - 1) % N] = lower_diag[j]
    W = np.diag(p)
    return S, W


def sl_lambda(eps, n_t, n_r, s, N=512):
    if n_t == 0 and n_r == 0:
        return 0.0
    q_eff = n_r - s * n_t
    n_t_abs = abs(n_t)
    S, W = build_sl_eigensystem(eps, q_eff, N=N)
    eigvals = linalg.eigvalsh(S, W, subset_by_index=[0, 2 * n_t_abs])
    if n_t_abs == 0:
        return float(eigvals[0])
    idx = 1 + 2 * (n_t_abs - 1)
    return float(eigvals[idx])


def mu2_flat(n_t, n_r, eps, s):
    return (n_t / eps)**2 + (n_r - s * n_t)**2


# ─── Constants ─────────────────────────────────────────────────────────

EPS_P = 0.55
S_P = 0.162037
M_P_OBS = 938.272
M_D_OBS = 1875.613
B_D_OBS = 2.224  # observed deuteron binding


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R63 Track 11 Phase 11b — Curved-donut compound vs separated")
    print("=" * 100)
    print()
    print(f"  Geometry: p-sheet curved donut, ε_p = {EPS_P}, s_p = {S_P}")
    print(f"  Anchor:   m_proton = {M_P_OBS} MeV at primitive (3, 6)")
    print(f"  Target:   m_deuteron = {M_D_OBS} MeV (binding {B_D_OBS} MeV)")
    print()

    # ─── Compute SL eigenvalues at (3, 6), (6, 12), and the (1, 2) primitive ─
    print("SL eigenvalues at p-sheet primitives:")
    print("-" * 100)
    print(f"  {'mode':>10s}  {'q_eff':>9s}  {'λ_curved':>11s}  {'μ²_flat':>11s}  "
          f"{'ratio':>8s}")
    print("  " + "─" * 70)

    modes = [
        ("(1, 2)", 1, 2),
        ("(3, 6)", 3, 6),
        ("(2, 4)", 2, 4),
        ("(4, 8)", 4, 8),
        ("(6, 12)", 6, 12),
        ("(9, 18)", 9, 18),
        ("(12, 24)", 12, 24),
    ]
    rows = []
    for label, n_t, n_r in modes:
        l_curved = sl_lambda(EPS_P, n_t, n_r, S_P, N=512)
        l_flat = mu2_flat(n_t, n_r, EPS_P, S_P)
        q_eff = n_r - S_P * n_t
        ratio = l_curved / l_flat if l_flat > 0 else 0
        print(f"  {label:>10s}  {q_eff:>9.4f}  {l_curved:>11.4f}  "
              f"{l_flat:>11.4f}  {ratio:>8.4f}")
        rows.append({'mode': label, 'n_t': n_t, 'n_r': n_r,
                     'q_eff': q_eff, 'lambda_curved': l_curved,
                     'mu2_flat': l_flat, 'ratio': ratio})
    print()

    # ─── k-linearity test ─────────────────────────────────────────────
    print("k-linearity check: does λ(k·3, k·6) = k²·λ(3, 6)?")
    print("-" * 100)
    print(f"  {'k':>3s}  {'λ(k·3, k·6)':>14s}  {'k²·λ(3, 6)':>14s}  "
          f"{'deviation':>12s}")
    print("  " + "─" * 60)
    l_3_6 = sl_lambda(EPS_P, 3, 6, S_P, N=512)
    for k in [1, 2, 3, 4]:
        n_t, n_r = 3 * k, 6 * k
        l_k = sl_lambda(EPS_P, n_t, n_r, S_P, N=512)
        l_predicted = k * k * l_3_6
        dev = (l_k - l_predicted) / l_predicted
        print(f"  {k:>3d}  {l_k:>14.4f}  {l_predicted:>14.4f}  "
              f"{dev:>+11.4%}")
    print()

    # ─── Compound mass under both interpretations ────────────────────
    print("Deuteron compound mass:")
    print("-" * 100)
    l_p_curved = sl_lambda(EPS_P, 3, 6, S_P, N=512)
    mu_p_curved = math.sqrt(l_p_curved)
    K_p = M_P_OBS / mu_p_curved   # MeV per √λ unit (curved anchor)

    l_d_curved = sl_lambda(EPS_P, 6, 12, S_P, N=512)
    mu_d_curved = math.sqrt(l_d_curved)
    m_d_curved = K_p * mu_d_curved

    # Flat (R62 derivation 4) prediction
    l_p_flat = mu2_flat(3, 6, EPS_P, S_P)
    mu_p_flat = math.sqrt(l_p_flat)
    K_p_flat = M_P_OBS / mu_p_flat
    l_d_flat = mu2_flat(6, 12, EPS_P, S_P)
    mu_d_flat = math.sqrt(l_d_flat)
    m_d_flat = K_p_flat * mu_d_flat

    print(f"  Flat formula:  m_d = K_p_flat · μ_flat(6, 12) = "
          f"{m_d_flat:.4f} MeV  (= 2·m_p)")
    print(f"  Curved SL:     m_d = K_p_curved · √λ(6, 12) = "
          f"{m_d_curved:.4f} MeV")
    print()

    # ─── Binding ────────────────────────────────────────────────────
    binding_flat = 2 * M_P_OBS - m_d_flat       # = 0 by construction
    binding_curved = 2 * M_P_OBS - m_d_curved   # > 0 if compound lighter
    binding_obs = 2 * M_P_OBS - M_D_OBS         # ~ 0.93 MeV vs naive sum

    print(f"  Compound 'binding' = 2·m_p − m_compound:")
    print(f"    Observed (vs additive-tuple prediction): "
          f"2·m_p − m_d_obs = {binding_obs:+.4f} MeV")
    print(f"    Flat formula:   {binding_flat:+.4e} MeV  "
          f"(zero by k-linearity)")
    print(f"    Curved donut:   {binding_curved:+.4f} MeV")
    print()

    if abs(binding_curved) < 0.01:
        verdict = "CURVED k-LINEAR — λ(6,12) = 4·λ(3,6); curvature does not bind."
    elif binding_curved > 0:
        verdict = (f"CURVED BINDS by {binding_curved:.2f} MeV  "
                  f"(compare to 2.22 MeV deuteron)")
    else:
        verdict = (f"CURVED ANTI-BINDS by {-binding_curved:.2f} MeV  "
                  f"(compound heavier than 2·m_p)")
    print(f"  → {verdict}")
    print()

    # ─── Save CSV ───────────────────────────────────────────────────
    csv_path = out_dir / "track11_phase11b_compound.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    main()
