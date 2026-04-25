"""
R64 Track 5 Phase 5c — Three-line nuclear binding model: R64-Ma + S-Coulomb + S-surface.

Phase 5b's two-line model failed because the Fe peak requires opposing
trends with A — surface (rising B/A as A grows) crossing Coulomb
(falling B/A).  This phase adds the standard Bethe-Weizsäcker surface
term as a "plugged" S-emergent contribution and re-fits R64-Ma jointly.

The hybrid framing accepts surface as an S-coordinate phenomenon
(spatial droplet of nucleons in 3D space, with boundary effects
∝ A^(2/3)), to be derived from first principles in MaSt later when
the spatial-distribution model is settled.

Total mass:
  m_total(Z, A) = m_R64-Ma(Z, A; ε_p, s_p) + a_C·Z(Z−1)/A^(1/3) + a_S·A^(2/3)

with a_C = 0.71 MeV (BW Coulomb), a_S = 18.34 MeV (BW surface).

If the Fe peak emerges and R64-Ma at the new fit point captures
~constant per-nucleon binding ≈ a_V (BW volume coefficient ~15.85),
then R64-Ma is correctly capturing the strong force's volume term.

Outputs:
  outputs/track5_phase5c_three_line.csv
  outputs/track5_phase5c_pointD_binding.csv
  outputs/track5_phase5c_three_line.png
"""

import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from track3_phase3a_nuclear_progression import (
    NUCLEI, M_P, M_N, U_TO_MEV, nuclear_mass, observed_binding,
)


A_COULOMB = 0.71   # MeV (Bethe-Weizsäcker Coulomb)
A_SURFACE = 18.34  # MeV (Bethe-Weizsäcker surface)


def mu2(n_t, n_r, eps, s):
    return (n_t / eps)**2 + (n_r - s * n_t)**2


def m_Ma(Z, A, eps, s, K_p):
    n_pt = 3 * A
    n_pr = 2 * (2 * Z - A)
    return K_p * math.sqrt(mu2(n_pt, n_pr, eps, s))


def E_Coulomb(Z, A):
    if A < 1:
        return 0.0
    return A_COULOMB * Z * (Z - 1) / (A ** (1.0 / 3.0))


def E_Surface(A):
    if A < 1:
        return 0.0
    return A_SURFACE * (A ** (2.0 / 3.0))


def m_total(Z, A, eps, s, K_p):
    return m_Ma(Z, A, eps, s, K_p) + E_Coulomb(Z, A) + E_Surface(A)


def derive_K_p(eps, s):
    """Anchor proton mass at (3, +2) on Ma side.
    For Z=1, A=1: E_Coulomb = 0, E_Surface = 18.34 MeV.
    So m_p = K_p · μ_Ma + 18.34 → K_p = (m_p - 18.34) / μ_Ma."""
    return (M_P - E_Surface(1)) / math.sqrt(mu2(3, +2, eps, s))


def fit_residual(eps, s):
    if eps <= 0:
        return None
    K_p = derive_K_p(eps, s)
    if K_p <= 0:
        return None

    # Predict m_n: at Z=0, A=1, neutron is single particle, no Coulomb.
    # Surface for A=1 is 18.34 MeV (same as proton, baseline).
    # m_n = K_p · μ(3, -2) + 18.34
    m_n_pred = K_p * math.sqrt(mu2(3, -2, eps, s)) + E_Surface(1)
    delta_np = m_n_pred - M_P

    sum_sq = 0.0
    n_count = 0
    for name, Z, A, atomic_u in NUCLEI:
        m_obs = nuclear_mass(atomic_u, Z)
        m_pred = m_total(Z, A, eps, s, K_p)
        err = (m_pred - m_obs) / m_obs
        sum_sq += err * err
        n_count += 1

    rms = math.sqrt(sum_sq / n_count)
    return {
        'eps_p': eps, 's_p': s, 'K_p': K_p,
        'rms_mass_err': rms,
        'delta_n_p': delta_np,
    }


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 5 Phase 5c — Three-line model: R64-Ma + S-Coulomb + S-surface")
    print("=" * 110)
    print()
    print(f"  Coulomb coefficient: a_C = {A_COULOMB} MeV (BW)")
    print(f"  Surface coefficient: a_S = {A_SURFACE} MeV (BW)")
    print(f"  Total mass: m = m_R64-Ma + a_C·Z(Z−1)/A^(1/3) + a_S·A^(2/3)")
    print()

    # ─── Sweep ─────────────────────────────────────────────────────────
    eps_grid = np.linspace(0.05, 0.6, 56)
    s_grid = np.linspace(-0.05, 0.30, 36)

    results = []
    for eps in eps_grid:
        for s in s_grid:
            r = fit_residual(eps, s)
            if r is not None:
                results.append(r)

    results.sort(key=lambda r: r['rms_mass_err'])

    print("Top 10 (eps_p, s_p) by RMS mass residual:")
    print("-" * 100)
    print(f"  {'rank':>4s}  {'ε_p':>7s}  {'s_p':>9s}  {'K_p':>10s}  "
          f"{'Δ(n−p)':>9s}  {'RMS |Δm/m|':>12s}")
    for i, r in enumerate(results[:10]):
        print(f"  {i+1:>4d}  {r['eps_p']:>7.4f}  {r['s_p']:>+9.4f}  "
              f"{r['K_p']:>10.3f}  {r['delta_n_p']:>+9.3f}  "
              f"{r['rms_mass_err']:>11.3%}")
    print()

    constrained = [r for r in results
                   if abs(r['delta_n_p'] - 1.293) / 1.293 < 0.10]  # within 10%
    constrained.sort(key=lambda r: r['rms_mass_err'])

    if constrained:
        print("Top 5 fits constrained to Δ(n−p) ≈ +1.293 MeV (±10%):")
        print("-" * 100)
        for i, r in enumerate(constrained[:5]):
            print(f"  {i+1:>4d}  {r['eps_p']:>7.4f}  {r['s_p']:>+9.4f}  "
                  f"{r['K_p']:>10.3f}  {r['delta_n_p']:>+9.3f}  "
                  f"{r['rms_mass_err']:>11.3%}")
        best_D = constrained[0]
    else:
        print("  No fits within Δ(n-p) constraint, using global best.")
        best_D = results[0]
    print()

    print(f"  Best fit (Point D): "
          f"ε_p = {best_D['eps_p']:.4f}, s_p = {best_D['s_p']:+.4f}, "
          f"K_p = {best_D['K_p']:.3f}")
    print(f"  Δ(n−p) = {best_D['delta_n_p']:+.3f} MeV")
    print(f"  RMS mass error: {best_D['rms_mass_err']:.3%}")
    print()

    # ─── Compute binding curve at Point D ───────────────────────
    eps_D = best_D['eps_p']
    s_D = best_D['s_p']
    K_D = best_D['K_p']

    print(f"Binding curve at Point D (three-line model):")
    print("-" * 110)
    print(f"  {'nucleus':>8s} {'Z':>3s} {'A':>3s}  "
          f"{'m_Ma':>10s} {'E_Coul':>8s} {'E_Surf':>8s} "
          f"{'m_total':>10s}  {'B_obs':>9s} {'B_pred':>9s} {'ratio':>7s}  "
          f"{'B/A_pred':>9s}")

    binding_rows = []
    for name, Z, A, atomic_u in NUCLEI:
        m_obs = nuclear_mass(atomic_u, Z)
        b_obs = observed_binding(Z, A, m_obs)
        m_ma = m_Ma(Z, A, eps_D, s_D, K_D)
        e_c = E_Coulomb(Z, A)
        e_s = E_Surface(A)
        m_t = m_ma + e_c + e_s
        b_pred = Z * M_P + (A - Z) * M_N - m_t

        ratio = b_pred / b_obs if b_obs > 0.5 else 0
        binding_rows.append({
            'name': name, 'Z': Z, 'A': A,
            'm_obs': m_obs,
            'm_Ma': m_ma,
            'E_Coul': e_c,
            'E_Surf': e_s,
            'm_total': m_t,
            'B_obs': b_obs,
            'B_pred': b_pred,
            'ratio': ratio,
            'B_per_A_obs': b_obs / A, 'B_per_A_pred': b_pred / A,
            'rel_err': (b_pred - b_obs) / b_obs if b_obs > 0.5 else 0,
        })
        if name in ['1H', '2H', '4He', '12C', '16O', '24Mg', '40Ca',
                    '52Cr', '56Fe', '64Zn', '90Zr', '120Sn',
                    '138Ba', '158Gd', '208Pb', '238U']:
            print(f"  {name:>8s} {Z:>3d} {A:>3d}  "
                  f"{m_ma:>10.2f} {e_c:>8.2f} {e_s:>8.2f} "
                  f"{m_t:>10.2f}  {b_obs:>9.2f} {b_pred:>9.2f} "
                  f"{ratio:>7.3f}  {b_pred/A:>9.3f}")
    print()

    # ─── Peak finding ────────────────────────────────────────
    A_arr = np.array([r['A'] for r in binding_rows])
    BA_obs = np.array([r['B_per_A_obs'] for r in binding_rows])
    BA_pred = np.array([r['B_per_A_pred'] for r in binding_rows])

    obs_peak_idx = int(np.argmax(BA_obs))
    pred_peak_idx = int(np.argmax(BA_pred))

    print(f"  Observed B/A peak: {binding_rows[obs_peak_idx]['name']} "
          f"at A={A_arr[obs_peak_idx]} with B/A = {BA_obs[obs_peak_idx]:.3f}")
    print(f"  Predicted B/A peak: {binding_rows[pred_peak_idx]['name']} "
          f"at A={A_arr[pred_peak_idx]} with B/A = {BA_pred[pred_peak_idx]:.3f}")
    print()

    # Decode what R64-Ma is providing per-nucleon at the fit:
    # m_Ma(Z, A) ≈ K_p · 3A/eps for small enough deviations
    # per-nucleon Ma contribution = K_p · 3 / eps
    ma_per_nucleon = K_D * 3 / eps_D
    print(f"  R64-Ma per-nucleon mass: K_p·3/ε_p = "
          f"{ma_per_nucleon:.3f} MeV/nucleon")
    print(f"  Volume term equivalent (B = m_p − m_Ma_per_nucleon for stable) "
          f"≈ {M_P - ma_per_nucleon:.3f} MeV/A")
    print(f"  BW volume coefficient (a_V): 15.85 MeV/A (target)")
    print()

    # ─── Save ──────────────────────────────────────────────
    csv_sweep = out_dir / "track5_phase5c_three_line.csv"
    with open(csv_sweep, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader()
        w.writerows(results)

    csv_binding = out_dir / "track5_phase5c_pointD_binding.csv"
    with open(csv_binding, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(binding_rows[0].keys()))
        w.writeheader()
        w.writerows(binding_rows)

    # ─── Plot ───────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))

    # 1: B/A curve
    ax = axes[0, 0]
    ax.plot(A_arr, BA_obs, 'o-', color='tab:blue',
            label='B/A observed', markersize=5)
    ax.plot(A_arr, BA_pred, 's--', color='tab:orange',
            label='B/A 3-line predicted', markersize=4)
    ax.axvline(56, color='gray', linestyle=':', alpha=0.5,
               label='Fe (A=56)')
    ax.set_xlabel('A')
    ax.set_ylabel('B/A (MeV)')
    ax.set_title(f'Three-line: R64-Ma + Coulomb + Surface at Point D '
                 f'(ε={eps_D:.3f}, s={s_D:+.3f})')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)

    # 2: contributions decomposition
    ax = axes[0, 1]
    EC_arr = np.array([r['E_Coul'] for r in binding_rows])
    ES_arr = np.array([r['E_Surf'] for r in binding_rows])
    Ma_arr = np.array([r['m_Ma'] for r in binding_rows])
    # Plot per-nucleon contributions
    A_safe = A_arr.astype(float)
    A_safe[A_safe < 1] = 1
    ax.plot(A_arr, EC_arr / A_safe, 'r-', label='Coulomb / A')
    ax.plot(A_arr, ES_arr / A_safe, 'g-', label='Surface / A')
    ma_per_n_arr = Ma_arr / A_safe
    ax.plot(A_arr, ma_per_n_arr - M_P, 'b-',
            label='(R64-Ma − m_p) / A')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('A')
    ax.set_ylabel('per-nucleon contribution (MeV)')
    ax.set_title('Three contributions, per-nucleon')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)

    # 3: residuals
    ax = axes[1, 0]
    rel_err_pct = np.array([r['rel_err'] * 100 for r in binding_rows])
    ax.plot(A_arr, rel_err_pct, 'o-', color='tab:purple', markersize=4)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axhline(5, color='gray', linestyle=':', alpha=0.4)
    ax.axhline(-5, color='gray', linestyle=':', alpha=0.4)
    ax.set_xlabel('A')
    ax.set_ylabel('(B_pred − B_obs)/B_obs (%)')
    ax.set_title('Binding residuals at Point D')
    ax.grid(alpha=0.3)

    # 4: parameter heatmap
    ax = axes[1, 1]
    eps_vals = sorted(set(r['eps_p'] for r in results))
    s_vals = sorted(set(r['s_p'] for r in results))
    grid = np.full((len(s_vals), len(eps_vals)), np.nan)
    for r in results:
        i = s_vals.index(r['s_p'])
        j = eps_vals.index(r['eps_p'])
        grid[i, j] = r['rms_mass_err'] * 100

    extent = [eps_vals[0], eps_vals[-1], s_vals[0], s_vals[-1]]
    im = ax.imshow(grid, origin='lower', extent=extent, aspect='auto',
                   vmin=0, vmax=2, cmap='viridis_r')
    fig.colorbar(im, ax=ax, label='RMS |Δm/m| (%)')
    ax.set_xlabel('ε_p')
    ax.set_ylabel('s_p')
    ax.set_title('3-line fit landscape')
    ax.plot(0.2052, 0.025, 'r*', markersize=12, label='Point B')
    ax.plot(0.2300, 0.020, 'gs', markersize=10, label='Point C')
    ax.plot(eps_D, s_D, 'w^', markersize=12, label='Point D (5c)')
    ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(out_dir / "track5_phase5c_three_line.png",
                dpi=150, bbox_inches='tight')
    plt.close()

    # ─── Verdict ────────────────────────────────────────────
    print("=" * 110)
    print("VERDICT — Phase 5c")
    print("=" * 110)
    print()

    binding_errs = [abs(r['rel_err']) for r in binding_rows
                    if r['B_obs'] > 0.5]
    print(f"  Across {len(binding_errs)} non-trivial nuclei at Point D:")
    print(f"    Mean |Δ(B)/B|: {np.mean(binding_errs):.2%}")
    print(f"    Max  |Δ(B)/B|: {np.max(binding_errs):.2%}")
    print()

    fe_row = next(r for r in binding_rows if r['name'] == '56Fe')
    pb_row = next(r for r in binding_rows if r['name'] == '208Pb')
    he_row = next(r for r in binding_rows if r['name'] == '4He')
    d_row = next(r for r in binding_rows if r['name'] == '2H')
    print(f"  ²H ratio:    {d_row['ratio']:.3f}")
    print(f"  ⁴He ratio:   {he_row['ratio']:.3f}")
    print(f"  ⁵⁶Fe ratio:  {fe_row['ratio']:.3f}")
    print(f"  ²⁰⁸Pb ratio: {pb_row['ratio']:.3f}")
    print()

    if 30 <= A_arr[pred_peak_idx] <= 100:
        print(f"  ★ FE-LIKE PEAK PRODUCED: predicted at A={A_arr[pred_peak_idx]} "
              f"vs observed A={A_arr[obs_peak_idx]}.")
    else:
        print(f"  Peak at A={A_arr[pred_peak_idx]} (observed A={A_arr[obs_peak_idx]}).")
    print()

    print(f"  CSV (sweep): {csv_sweep}")
    print(f"  CSV (binding): {csv_binding}")
    print(f"  Plot: {out_dir / 'track5_phase5c_three_line.png'}")


if __name__ == "__main__":
    main()
