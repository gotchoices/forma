"""
R64 Track 5 Phase 5a — Two-line nuclear binding model: Ma harmonic stack + S-Coulomb.

Tests the user's two-line hypothesis for the Fe peak:
  - Line 1 (strong, Ma-internal): R64's harmonic stack on the p-sheet.
  - Line 2 (Coulomb, S-emergent): a_C·Z(Z−1)/A^(1/3) standard form.

Total predicted nuclear mass:
  m_total(Z, A) = m_Ma(Z, A) + E_Coulomb(Z, A)

where m_Ma(Z, A) is R64's chain-fit Point B prediction and
E_Coulomb(Z, A) = a_C·Z(Z−1)/A^(1/3) with a_C ≈ 0.71 MeV.

Phase 5a tests at fixed Point B parameters (no joint refit yet).
Phase 5b will sweep parameters jointly with Coulomb to find the
optimal Ma-side fit.

Outputs:
  outputs/track5_phase5a_coulomb_added.csv
  outputs/track5_phase5a_binding_curve.png
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


# ─── R64 Point B parameters (chain-fit) ────────────────────────────────

EPS_P = 0.2052
S_P   = +0.0250
K_P   = 63.629    # MeV/μ-unit


# ─── Coulomb (Bethe-Weizsäcker form, S-emergent) ───────────────────────

A_COULOMB = 0.71  # MeV (standard SM value)


def mu2(n_t, n_r, eps=EPS_P, s=S_P):
    return (n_t / eps)**2 + (n_r - s * n_t)**2


def m_Ma(Z, A, eps=EPS_P, s=S_P, K_p=K_P):
    """R64 harmonic-stack mass (Line 1, strong, Ma-internal)."""
    n_pt = 3 * A
    n_pr = 2 * (2 * Z - A)
    return K_p * math.sqrt(mu2(n_pt, n_pr, eps, s))


def E_Coulomb(Z, A):
    """S-Coulomb energy (Line 2, EM, S-emergent).
    a_C·Z(Z−1)/A^(1/3) — standard Bethe-Weizsäcker form.
    Returns positive value (mass excess vs no Coulomb).
    """
    if A < 1:
        return 0.0
    return A_COULOMB * Z * (Z - 1) / (A ** (1.0/3.0))


def m_total(Z, A, eps=EPS_P, s=S_P, K_p=K_P):
    return m_Ma(Z, A, eps, s, K_p) + E_Coulomb(Z, A)


def predicted_binding(Z, A, eps=EPS_P, s=S_P, K_p=K_P):
    return Z * M_P + (A - Z) * M_N - m_total(Z, A, eps, s, K_p)


# ─── Main ──────────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 5 Phase 5a — Two-line nuclear binding model")
    print("=" * 110)
    print()
    print(f"  Line 1 (Ma harmonic stack at Point B):")
    print(f"    ε_p = {EPS_P}, s_p = {S_P:+}, K_p = {K_P:.3f} MeV/μ")
    print()
    print(f"  Line 2 (S-Coulomb): E_C = {A_COULOMB}·Z(Z−1)/A^(1/3) MeV")
    print(f"    α-scaling implicit in the Bethe-Weizsäcker coefficient.")
    print()

    # ─── Compute predictions for the full chain ───────────────────────
    print(f"  {'nucleus':>8s}  {'Z':>3s}  {'A':>3s}  "
          f"{'m_obs':>10s}  {'m_Ma':>10s}  {'E_Coul':>8s}  "
          f"{'m_total':>10s}  {'B_obs':>9s}  {'B_pred':>9s}  "
          f"{'B/A_obs':>8s}  {'B/A_pred':>9s}")

    rows = []
    for name, Z, A, atomic_u in NUCLEI:
        m_obs = nuclear_mass(atomic_u, Z)
        b_obs = observed_binding(Z, A, m_obs)
        m_ma_val = m_Ma(Z, A)
        e_c = E_Coulomb(Z, A)
        m_t = m_ma_val + e_c
        b_pred = Z * M_P + (A - Z) * M_N - m_t

        ba_obs = b_obs / A
        ba_pred = b_pred / A

        # Print only a sampling for clarity
        if name in ['1H', '2H', '4He', '6Li', '12C', '16O', '24Mg', '28Si',
                    '40Ca', '52Cr', '56Fe', '64Zn', '90Zr', '120Sn', '138Ba',
                    '158Gd', '184W', '208Pb', '232Th', '238U']:
            print(f"  {name:>8s}  {Z:>3d}  {A:>3d}  "
                  f"{m_obs:>10.2f}  {m_ma_val:>10.2f}  {e_c:>8.2f}  "
                  f"{m_t:>10.2f}  {b_obs:>9.2f}  {b_pred:>9.2f}  "
                  f"{ba_obs:>8.3f}  {ba_pred:>9.3f}")

        rows.append({
            'name': name, 'Z': Z, 'A': A,
            'm_obs_MeV': m_obs,
            'm_Ma_MeV': m_ma_val,
            'E_Coulomb_MeV': e_c,
            'm_total_MeV': m_t,
            'B_obs_MeV': b_obs,
            'B_pred_MeV': b_pred,
            'B_per_A_obs': ba_obs,
            'B_per_A_pred': ba_pred,
            'rel_err_mass': (m_t - m_obs) / m_obs,
            'rel_err_binding': (b_pred - b_obs) / b_obs if b_obs > 0.5 else 0,
        })
    print()

    # ─── Fe peak test ─────────────────────────────────────────────────
    print("Fe peak test:")
    print("-" * 110)
    A_arr = np.array([r['A'] for r in rows])
    BA_obs = np.array([r['B_per_A_obs'] for r in rows])
    BA_pred = np.array([r['B_per_A_pred'] for r in rows])

    obs_peak_idx = int(np.argmax(BA_obs))
    pred_peak_idx = int(np.argmax(BA_pred))
    print(f"  Observed B/A peak:   {rows[obs_peak_idx]['name']} at A={A_arr[obs_peak_idx]} "
          f"with B/A = {BA_obs[obs_peak_idx]:.3f} MeV")
    print(f"  Predicted B/A peak:  {rows[pred_peak_idx]['name']} at A={A_arr[pred_peak_idx]} "
          f"with B/A = {BA_pred[pred_peak_idx]:.3f} MeV")
    print()

    # Compare specific benchmarks
    print("  At key benchmarks:")
    print(f"  {'nucleus':>8s}  {'B_obs':>9s}  {'B_pred':>9s}  "
          f"{'ratio':>8s}  {'B/A_obs':>8s}  {'B/A_pred':>9s}")
    for name in ['2H', '4He', '12C', '16O', '40Ca', '56Fe',
                  '90Zr', '120Sn', '208Pb', '238U']:
        r = next(rr for rr in rows if rr['name'] == name)
        ratio = r['B_pred_MeV'] / r['B_obs_MeV'] if r['B_obs_MeV'] > 0 else 0
        print(f"  {name:>8s}  {r['B_obs_MeV']:>9.2f}  {r['B_pred_MeV']:>9.2f}  "
              f"{ratio:>8.3f}  {r['B_per_A_obs']:>8.3f}  {r['B_per_A_pred']:>9.3f}")
    print()

    # ─── Stats ────────────────────────────────────────────────────────
    rows_proper = [r for r in rows if r['B_obs_MeV'] > 0.5
                   and r['name'] not in ('1H',)]  # exclude H (binding=0)
    binding_errs = [abs(r['rel_err_binding']) for r in rows_proper]
    print(f"  Across {len(rows_proper)} non-trivial nuclei:")
    print(f"    Mean |Δ(B)/B|: {np.mean(binding_errs):.2%}")
    print(f"    Max  |Δ(B)/B|: {np.max(binding_errs):.2%}")
    print(f"    Median:        {np.median(binding_errs):.2%}")
    print()

    # ─── Save CSV ─────────────────────────────────────────────────
    csv_path = out_dir / "track5_phase5a_coulomb_added.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # ─── Plot ────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))

    # Top-left: B/A vs A — observed vs predicted
    ax = axes[0, 0]
    ax.plot(A_arr, BA_obs, 'o-', color='tab:blue',
            label='B/A observed', markersize=5)
    ax.plot(A_arr, BA_pred, 's--', color='tab:orange',
            label='B/A predicted (R64-Ma + Coulomb)', markersize=4)
    # Reference: Ma alone (no Coulomb)
    BA_ma_only = np.array([(Z * M_P + (A - Z) * M_N - m_Ma(Z, A)) / A
                           for r in rows for Z, A in [(r['Z'], r['A'])]])
    ax.plot(A_arr, BA_ma_only, '^:', color='tab:green',
            label='B/A R64-Ma alone (no Coulomb)', markersize=3, alpha=0.7)
    ax.axvline(56, color='gray', linestyle=':', alpha=0.5, label='Fe (A=56)')
    ax.set_xlabel('A')
    ax.set_ylabel('B/A (MeV)')
    ax.set_title('Binding-per-nucleon: two-line model vs observed')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    # Top-right: Coulomb energy alone vs A
    ax = axes[0, 1]
    EC_arr = np.array([r['E_Coulomb_MeV'] for r in rows])
    ax.plot(A_arr, EC_arr, 'o-', color='tab:red', markersize=4)
    ax.set_xlabel('A')
    ax.set_ylabel('E_Coulomb(Z, A) (MeV)')
    ax.set_title('Coulomb energy contribution alone')
    ax.grid(alpha=0.3)

    # Bottom-left: residuals
    ax = axes[1, 0]
    rel_err_pct = np.array([r['rel_err_binding'] * 100 for r in rows])
    ax.plot(A_arr, rel_err_pct, 'o-', color='tab:purple', markersize=4)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axhline(5, color='gray', linestyle=':', alpha=0.4, label='±5%')
    ax.axhline(-5, color='gray', linestyle=':', alpha=0.4)
    ax.set_xlabel('A')
    ax.set_ylabel('(B_pred − B_obs)/B_obs (%)')
    ax.set_title('Binding residuals (predicted vs observed)')
    ax.grid(alpha=0.3)
    ax.legend()

    # Bottom-right: peak shape comparison
    ax = axes[1, 1]
    ax.plot(A_arr, BA_obs, 'o-', color='tab:blue',
            label='B/A observed', markersize=5)
    ax.plot(A_arr, BA_pred, 's--', color='tab:orange',
            label='B/A R64+Coulomb', markersize=4)
    ax.set_xlim(0, 250)
    ax.set_xlabel('A')
    ax.set_ylabel('B/A (MeV)')
    ax.set_title('Peak shape (zoom)')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(out_dir / "track5_phase5a_binding_curve.png",
                dpi=150, bbox_inches='tight')
    plt.close()

    # ─── Verdict ────────────────────────────────────────────────
    print("=" * 110)
    print("VERDICT — Phase 5a")
    print("=" * 110)
    print()

    if A_arr[pred_peak_idx] > 30 and A_arr[pred_peak_idx] < 100:
        peak_status = (
            f"FE-LIKE PEAK PRODUCED: predicted peak at A={A_arr[pred_peak_idx]} "
            f"(observed at A={A_arr[obs_peak_idx]})"
        )
    elif A_arr[pred_peak_idx] >= 100:
        peak_status = (
            f"PEAK TOO HEAVY: predicted at A={A_arr[pred_peak_idx]} "
            f"(observed at A={A_arr[obs_peak_idx]})"
        )
    else:
        peak_status = (
            f"PEAK MISPLACED: predicted at A={A_arr[pred_peak_idx]} "
            f"vs observed A={A_arr[obs_peak_idx]}"
        )
    print(f"  → {peak_status}")
    print()

    fe_row = next(r for r in rows if r['name'] == '56Fe')
    pb_row = next(r for r in rows if r['name'] == '208Pb')
    he_row = next(r for r in rows if r['name'] == '4He')
    print(f"  Fe binding ratio (pred/obs): {fe_row['B_pred_MeV']/fe_row['B_obs_MeV']:.3f}")
    print(f"  Pb binding ratio (pred/obs): {pb_row['B_pred_MeV']/pb_row['B_obs_MeV']:.3f}")
    print(f"  ⁴He binding ratio:           {he_row['B_pred_MeV']/he_row['B_obs_MeV']:.3f}")
    print()

    print(f"  CSV: {csv_path}")
    print(f"  Plot: {out_dir / 'track5_phase5a_binding_curve.png'}")


if __name__ == "__main__":
    main()
