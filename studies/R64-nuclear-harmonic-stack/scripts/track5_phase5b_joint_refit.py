"""
R64 Track 5 Phase 5b — Joint refit of (ε_p, s_p) with explicit S-Coulomb.

Phase 5a revealed that simply adding Coulomb to Point B's prediction
over-corrects, because Point B was implicitly absorbing Coulomb effects
when fit to raw observed binding.  Phase 5b re-fits (ε_p, s_p) jointly
with the explicit Coulomb term to find the parameter point where:

  m_total(Z, A) = m_R64-Ma(Z, A; ε_p, s_p) + a_C·Z(Z−1)/A^(1/3)

best matches observed nuclear masses across the chain.

The new working point (call it "Point C") represents the Ma-only
strong-force contribution; the Fe peak emerges from the interaction
of Point C's flat-ish Ma binding with the explicit Coulomb cost.

Outputs:
  outputs/track5_phase5b_joint_refit.csv (sweep results)
  outputs/track5_phase5b_joint_refit.png (parameter heatmap)
  outputs/track5_phase5b_pointC_binding.png (binding curve at Point C)
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


A_COULOMB = 0.71  # MeV (Bethe-Weizsäcker Coulomb coefficient)


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


def m_total(Z, A, eps, s, K_p):
    return m_Ma(Z, A, eps, s, K_p) + E_Coulomb(Z, A)


def derive_K_p(eps, s, m_target=M_P):
    """Anchor K_p so the proton mass = K_p · μ_Ma(3, +2) − E_Coul(1, 1).

    For the proton (Z=1, A=1), Coulomb is zero (Z(Z-1) = 0), so the
    anchor is m_p = K_p · μ(3, +2).  Same as before.
    """
    return m_target / math.sqrt(mu2(3, +2, eps, s))


def fit_residual(eps, s):
    """Compute the RMS mass-residual across all nuclei for given (eps, s),
    with K_p anchored to the proton and Coulomb explicitly included.

    Also enforce: predicted m_n − m_p must match observed (~1.293 MeV).
    """
    if eps <= 0:
        return None

    K_p = derive_K_p(eps, s)

    # m_n predicted (no Coulomb for neutron, Z(Z-1)=0)
    m_n_pred = K_p * math.sqrt(mu2(3, -2, eps, s)) + E_Coulomb(0, 1)
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


# ─── Sweep ─────────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 5 Phase 5b — Joint refit of (ε_p, s_p) with explicit S-Coulomb")
    print("=" * 110)
    print()
    print(f"  Coulomb coefficient: a_C = {A_COULOMB} MeV (BW standard)")
    print(f"  Target: m_n − m_p = +1.293 MeV (observed)")
    print(f"  Ma + S-Coulomb total mass: m(Z, A) = m_R64-Ma + a_C·Z(Z−1)/A^(1/3)")
    print()

    # ─── 2D parameter sweep ───────────────────────────────────────
    eps_grid = np.linspace(0.05, 0.6, 56)
    s_grid = np.linspace(-0.05, 0.30, 36)

    results = []
    for eps in eps_grid:
        for s in s_grid:
            r = fit_residual(eps, s)
            if r is not None:
                results.append(r)

    # Find best fits
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

    # Best fit constrained to give correct Δ(n-p) within 5%
    constrained = [r for r in results
                   if abs(r['delta_n_p'] - 1.293) / 1.293 < 0.05]
    constrained.sort(key=lambda r: r['rms_mass_err'])

    if constrained:
        print("Top 5 fits constrained to Δ(n−p) ≈ +1.293 MeV (±5%):")
        print("-" * 100)
        print(f"  {'rank':>4s}  {'ε_p':>7s}  {'s_p':>9s}  {'K_p':>10s}  "
              f"{'Δ(n−p)':>9s}  {'RMS |Δm/m|':>12s}")
        for i, r in enumerate(constrained[:5]):
            print(f"  {i+1:>4d}  {r['eps_p']:>7.4f}  {r['s_p']:>+9.4f}  "
                  f"{r['K_p']:>10.3f}  {r['delta_n_p']:>+9.3f}  "
                  f"{r['rms_mass_err']:>11.3%}")

        best_C = constrained[0]
        print()
        print(f"  Best constrained fit (Point C):")
        print(f"    ε_p = {best_C['eps_p']:.4f}, s_p = {best_C['s_p']:+.4f}, "
              f"K_p = {best_C['K_p']:.3f}")
        print(f"    Δ(n−p) = {best_C['delta_n_p']:+.3f} MeV (target +1.293)")
        print(f"    RMS mass error: {best_C['rms_mass_err']:.3%}")
        print()
        print(f"  Comparison to Track 3 Point B (no Coulomb):")
        print(f"    Point B: ε=0.2052, s=+0.0250, RMS=0.182%")
        print(f"    Point C: ε={best_C['eps_p']:.4f}, s={best_C['s_p']:+.4f}, "
              f"RMS={best_C['rms_mass_err']:.3%}")
    else:
        print("  NO viable point found within Δ(n-p) constraint.")
        best_C = results[0]
    print()

    # ─── Compute binding curve at Point C ───────────────────────
    eps_C = best_C['eps_p']
    s_C = best_C['s_p']
    K_C = best_C['K_p']

    print(f"Binding curve at Point C (ε={eps_C:.4f}, s={s_C:+.4f}):")
    print("-" * 100)
    print(f"  {'nucleus':>8s}  {'Z':>3s}  {'A':>3s}  "
          f"{'B_obs':>9s}  {'B_pred':>9s}  {'ratio':>8s}  "
          f"{'B/A_obs':>8s}  {'B/A_pred':>9s}")

    binding_rows = []
    for name, Z, A, atomic_u in NUCLEI:
        m_obs = nuclear_mass(atomic_u, Z)
        b_obs = observed_binding(Z, A, m_obs)
        m_p = m_total(Z, A, eps_C, s_C, K_C)
        b_pred = Z * M_P + (A - Z) * M_N - m_p
        ratio = b_pred / b_obs if b_obs > 0.5 else 0
        binding_rows.append({
            'name': name, 'Z': Z, 'A': A,
            'B_obs': b_obs, 'B_pred': b_pred,
            'ratio': ratio,
            'B_per_A_obs': b_obs / A, 'B_per_A_pred': b_pred / A,
        })
        if name in ['1H', '2H', '4He', '12C', '16O', '40Ca', '52Cr',
                    '56Fe', '64Zn', '90Zr', '120Sn', '138Ba', '158Gd',
                    '184W', '208Pb', '238U']:
            print(f"  {name:>8s}  {Z:>3d}  {A:>3d}  "
                  f"{b_obs:>9.2f}  {b_pred:>9.2f}  {ratio:>8.3f}  "
                  f"{b_obs/A:>8.3f}  {b_pred/A:>9.3f}")
    print()

    # Find peak of B/A
    A_arr = np.array([r['A'] for r in binding_rows])
    BA_obs = np.array([r['B_per_A_obs'] for r in binding_rows])
    BA_pred = np.array([r['B_per_A_pred'] for r in binding_rows])
    obs_peak_idx = int(np.argmax(BA_obs))
    pred_peak_idx = int(np.argmax(BA_pred))
    print(f"  Observed B/A peak:  {binding_rows[obs_peak_idx]['name']} "
          f"at A={A_arr[obs_peak_idx]} with B/A = {BA_obs[obs_peak_idx]:.3f}")
    print(f"  Predicted B/A peak: {binding_rows[pred_peak_idx]['name']} "
          f"at A={A_arr[pred_peak_idx]} with B/A = {BA_pred[pred_peak_idx]:.3f}")
    print()

    # ─── Save ─────────────────────────────────────────────────────
    csv_sweep = out_dir / "track5_phase5b_joint_refit.csv"
    with open(csv_sweep, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader()
        w.writerows(results)

    csv_binding = out_dir / "track5_phase5b_pointC_binding.csv"
    with open(csv_binding, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(binding_rows[0].keys()))
        w.writeheader()
        w.writerows(binding_rows)

    # ─── Plots ────────────────────────────────────────────────────
    # Heatmap of RMS error
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    eps_vals = sorted(set(r['eps_p'] for r in results))
    s_vals = sorted(set(r['s_p'] for r in results))
    grid = np.full((len(s_vals), len(eps_vals)), np.nan)
    for r in results:
        i = s_vals.index(r['s_p'])
        j = eps_vals.index(r['eps_p'])
        grid[i, j] = r['rms_mass_err'] * 100

    ax = axes[0]
    extent = [eps_vals[0], eps_vals[-1], s_vals[0], s_vals[-1]]
    im = ax.imshow(grid, origin='lower', extent=extent, aspect='auto',
                   vmin=0, vmax=2, cmap='viridis_r')
    fig.colorbar(im, ax=ax, label='RMS |Δm/m| (%)')
    ax.set_xlabel('ε_p')
    ax.set_ylabel('s_p')
    ax.set_title('Joint refit: RMS mass residual (Ma + Coulomb)')
    ax.plot(0.2052, 0.025, 'r*', markersize=15,
            label='Point B (Track 3, no Coulomb)')
    ax.plot(eps_C, s_C, 'w^', markersize=12,
            label=f'Point C (5b best, with Coulomb)')
    ax.legend(fontsize=9)

    # Binding curve at Point C
    ax = axes[1]
    ax.plot(A_arr, BA_obs, 'o-', color='tab:blue',
            label='B/A observed', markersize=5)
    ax.plot(A_arr, BA_pred, 's--', color='tab:orange',
            label=f'B/A R64-Ma + Coulomb (Point C)', markersize=4)
    ax.axvline(56, color='gray', linestyle=':', alpha=0.5,
               label='Fe (A=56)')
    ax.set_xlabel('A')
    ax.set_ylabel('B/A (MeV)')
    ax.set_title(f'Two-line model at Point C (ε={eps_C:.3f}, s={s_C:+.3f})')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig(out_dir / "track5_phase5b_joint_refit.png",
                dpi=150, bbox_inches='tight')
    plt.close()

    # ─── Verdict ───────────────────────────────────────────────
    print("=" * 110)
    print("VERDICT — Phase 5b")
    print("=" * 110)
    print()

    binding_errs = [abs(r['ratio'] - 1) for r in binding_rows
                    if r['B_obs'] > 0.5]
    print(f"  Across {len(binding_errs)} non-trivial nuclei at Point C:")
    print(f"    Mean |Δ(B)/B|: {np.mean(binding_errs):.2%}")
    print(f"    Max  |Δ(B)/B|: {np.max(binding_errs):.2%}")
    print()

    fe_row = next(r for r in binding_rows if r['name'] == '56Fe')
    pb_row = next(r for r in binding_rows if r['name'] == '208Pb')
    he_row = next(r for r in binding_rows if r['name'] == '4He')
    d_row = next(r for r in binding_rows if r['name'] == '2H')
    print(f"  ²H ratio:  {d_row['B_pred']/max(d_row['B_obs'], 0.01):.3f}")
    print(f"  ⁴He ratio: {he_row['B_pred']/he_row['B_obs']:.3f}")
    print(f"  ⁵⁶Fe ratio: {fe_row['B_pred']/fe_row['B_obs']:.3f}")
    print(f"  ²⁰⁸Pb ratio: {pb_row['B_pred']/pb_row['B_obs']:.3f}")
    print()

    if 30 <= A_arr[pred_peak_idx] <= 100:
        print(f"  ★ FE-LIKE PEAK: predicted at A={A_arr[pred_peak_idx]} "
              f"vs observed A={A_arr[obs_peak_idx]}.")
    else:
        print(f"  Peak misplaced: predicted A={A_arr[pred_peak_idx]} "
              f"vs observed A={A_arr[obs_peak_idx]}.")
    print()

    print(f"  CSV (sweep): {csv_sweep}")
    print(f"  CSV (binding): {csv_binding}")
    print(f"  Plot: {out_dir / 'track5_phase5b_joint_refit.png'}")


if __name__ == "__main__":
    main()
