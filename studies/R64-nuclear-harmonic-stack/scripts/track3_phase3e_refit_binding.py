"""
R64 Track 3 Phase 3e — Binding curve at the global re-fit point.

Phase 3d showed that an alternative (ε_p, s_p) = (0.205, +0.025)
gives a 4× better mass-residual fit to the nuclear chain than the
deuteron-anchored magic point.  This phase computes the predicted
binding curve at the re-fit point and compares to observation across
the full chain — answering whether the user's concern about pinning
too quickly to ²H opens a structurally better picture of the
harmonic-stack model.

Outputs:
  outputs/track3_phase3e_refit_binding.csv
  outputs/track3_phase3e_refit_binding.png
"""

import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from track3_phase3a_nuclear_progression import (
    NUCLEI, M_P, M_N, M_E, U_TO_MEV, nuclear_mass, observed_binding, mu2,
)

# ─── Magic-point and re-fit-point parameters ──────────────────────────

EPS_MAGIC = 0.073092553872
S_MAGIC   = 0.193871467423

EPS_REFIT = 0.2052
S_REFIT   = +0.0250

A_COULOMB = 0.71  # MeV (Bethe-Weizsäcker Coulomb coefficient)


def derive_K_p(eps, s):
    """Anchor proton mass at (3, +2) with this (ε, s)."""
    return M_P / math.sqrt(mu2(3, +2, eps, s))


def predicted_mass(Z, A, eps, s, K_p):
    n_pt = 3 * A
    n_pr = 2 * (2 * Z - A)
    return K_p * math.sqrt(mu2(n_pt, n_pr, eps, s))


def predicted_binding(Z, A, eps, s, K_p):
    return Z * M_P + (A - Z) * M_N - predicted_mass(Z, A, eps, s, K_p)


def coulomb_energy(Z, A):
    if A < 1:
        return 0.0
    return A_COULOMB * Z * (Z - 1) / (A ** (1.0 / 3.0))


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 3 Phase 3e — Binding curve at the global re-fit point")
    print("=" * 110)
    print()

    K_magic = derive_K_p(EPS_MAGIC, S_MAGIC)
    K_refit = derive_K_p(EPS_REFIT, S_REFIT)

    print(f"  Magic point (²H anchor): "
          f"ε={EPS_MAGIC:.4f}, s={S_MAGIC:+.4f}, K_p={K_magic:.3f}")
    print(f"  Re-fit point (chain fit): "
          f"ε={EPS_REFIT:.4f}, s={S_REFIT:+.4f}, K_p={K_refit:.3f}")
    print()

    # m_n at each point (proton anchored at both)
    mn_magic = K_magic * math.sqrt(mu2(3, -2, EPS_MAGIC, S_MAGIC))
    mn_refit = K_refit * math.sqrt(mu2(3, -2, EPS_REFIT, S_REFIT))
    print(f"  m_n predicted: magic = {mn_magic:.4f},   "
          f"re-fit = {mn_refit:.4f}, observed = {M_N:.4f}")
    print()

    # ─── Compute binding at both points for all nuclei ────────────────
    print(f"  {'nucleus':>8s}  {'B_obs':>9s}  "
          f"{'B_magic':>9s}  {'r_magic':>8s}  "
          f"{'B_refit':>9s}  {'r_refit':>8s}  "
          f"{'B_refit_nonC':>12s}  {'r_refit_nonC':>12s}")
    print("  " + "─" * 100)

    rows = []
    for name, Z, A, atomic_u in NUCLEI:
        m_obs = nuclear_mass(atomic_u, Z)
        b_obs = observed_binding(Z, A, m_obs)
        b_magic = predicted_binding(Z, A, EPS_MAGIC, S_MAGIC, K_magic)
        b_refit = predicted_binding(Z, A, EPS_REFIT, S_REFIT, K_refit)
        e_c = coulomb_energy(Z, A)
        b_obs_nonC = b_obs + e_c   # observed without Coulomb effect

        r_magic = b_magic / b_obs if b_obs > 0 else 0
        r_refit = b_refit / b_obs if b_obs > 0 else 0
        r_refit_nonC = b_refit / b_obs_nonC if b_obs_nonC > 0 else 0

        # Print only a sampling
        if name in ['1H', '2H', '4He', '12C', '16O', '40Ca', '56Fe',
                    '90Zr', '120Sn', '208Pb', '238U']:
            print(f"  {name:>8s}  {b_obs:>9.2f}  "
                  f"{b_magic:>9.2f}  {r_magic:>8.3f}  "
                  f"{b_refit:>9.2f}  {r_refit:>8.3f}  "
                  f"{b_obs_nonC:>12.2f}  {r_refit_nonC:>12.3f}")

        rows.append({
            'name': name, 'Z': Z, 'A': A,
            'B_obs': b_obs,
            'B_magic': b_magic,
            'B_refit': b_refit,
            'E_Coulomb': e_c,
            'B_obs_nonCoulomb': b_obs_nonC,
            'ratio_magic': r_magic,
            'ratio_refit': r_refit,
            'ratio_refit_nonC': r_refit_nonC,
        })
    print()

    # Mean ratios (excluding 1H which has B=0)
    rows_proper = [r for r in rows if r['B_obs'] > 0.5]
    mean_r_magic = np.mean([r['ratio_magic'] for r in rows_proper])
    mean_r_refit = np.mean([r['ratio_refit'] for r in rows_proper])
    mean_r_refit_nonC = np.mean([r['ratio_refit_nonC'] for r in rows_proper])

    print(f"  Mean (B_pred/B_obs) across all nuclei (excluding ¹H):")
    print(f"    Magic point:                  {mean_r_magic:.3f}  "
          f"(should be ~1.0)")
    print(f"    Re-fit point (vs raw obs):    {mean_r_refit:.3f}")
    print(f"    Re-fit point (vs non-Coulomb): {mean_r_refit_nonC:.3f}")
    print()

    # Binding error stats (relative) at re-fit point, excluding ²H outlier
    rows_no_d = [r for r in rows if r['name'] not in ('1H', '2H')
                 and r['B_obs'] > 0.5]
    refit_errs_raw  = [(r['B_refit'] - r['B_obs']) / r['B_obs']
                       for r in rows_no_d]
    refit_errs_nonC = [(r['B_refit'] - r['B_obs_nonCoulomb']) /
                        r['B_obs_nonCoulomb'] for r in rows_no_d]

    print(f"  Binding-curve fit at re-fit point (A ≥ 4 nuclei, excludes ²H):")
    print(f"    vs raw observed:        mean err = "
          f"{np.mean(refit_errs_raw):+.2%}, "
          f"max |err| = {max(abs(e) for e in refit_errs_raw):.2%}")
    print(f"    vs Coulomb-subtracted:  mean err = "
          f"{np.mean(refit_errs_nonC):+.2%}, "
          f"max |err| = {max(abs(e) for e in refit_errs_nonC):.2%}")
    print()

    # ─── Save CSV ─────────────────────────────────────────────────
    csv_path = out_dir / "track3_phase3e_refit_binding.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # ─── Plot ────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))

    A_arr = np.array([r['A'] for r in rows])
    bobs = np.array([r['B_obs'] for r in rows])
    bmagic = np.array([r['B_magic'] for r in rows])
    brefit = np.array([r['B_refit'] for r in rows])
    bobs_nonC = np.array([r['B_obs_nonCoulomb'] for r in rows])

    # 1: B/A comparison
    ax = axes[0, 0]
    safe_A = A_arr.astype(float)
    ax.plot(safe_A, bobs / safe_A, 'o-', color='tab:blue',
            label='B/A observed', markersize=4)
    ax.plot(safe_A, bmagic / safe_A, 's--', color='tab:orange',
            label=f'B/A at magic (ε=0.073, s=0.194)', markersize=3, alpha=0.8)
    ax.plot(safe_A, brefit / safe_A, '^-', color='tab:green',
            label=f'B/A at re-fit (ε=0.205, s=0.025)', markersize=4)
    ax.set_xlabel('A')
    ax.set_ylabel('B/A (MeV)')
    ax.set_title('Binding-per-nucleon: magic vs re-fit')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    # 2: B/A vs B_nonC/A
    ax = axes[0, 1]
    ax.plot(safe_A, bobs / safe_A, 'o-', color='tab:blue',
            label='B/A observed (raw)', markersize=4)
    ax.plot(safe_A, bobs_nonC / safe_A, '^-', color='tab:purple',
            label='B/A non-Coulomb (= obs + Coul/A)', markersize=4)
    ax.plot(safe_A, brefit / safe_A, 's-', color='tab:green',
            label='B/A R64 re-fit', markersize=4)
    ax.set_xlabel('A')
    ax.set_ylabel('B/A (MeV)')
    ax.set_title('Re-fit vs Coulomb-subtracted observation')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    # 3: Ratio plot
    ax = axes[1, 0]
    ratios_magic = bmagic / np.maximum(bobs, 0.1)
    ratios_refit = brefit / np.maximum(bobs, 0.1)
    ax.plot(safe_A, ratios_magic, 's--', color='tab:orange',
            label='B_magic / B_obs', markersize=4, alpha=0.8)
    ax.plot(safe_A, ratios_refit, '^-', color='tab:green',
            label='B_refit / B_obs', markersize=4)
    ax.axhline(1.0, color='black', linewidth=0.5)
    ax.set_xlabel('A')
    ax.set_ylabel('Predicted / observed binding')
    ax.set_title('Ratio of predicted to observed binding')
    ax.set_yscale('log')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    # 4: Binding-curve detail
    ax = axes[1, 1]
    ax.plot(safe_A[1:], bobs[1:], 'o-', color='tab:blue',
            label='Observed B', markersize=4)
    ax.plot(safe_A[1:], brefit[1:], '^-', color='tab:green',
            label='R64 re-fit B', markersize=4)
    ax.plot(safe_A[1:], bobs_nonC[1:], '^--', color='tab:purple',
            label='Observed + Coulomb', markersize=3, alpha=0.6)
    ax.set_xlabel('A')
    ax.set_ylabel('Total binding B (MeV)')
    ax.set_title('Total binding (re-fit vs observed)')
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    plt.tight_layout()
    fig.savefig(out_dir / "track3_phase3e_refit_binding.png",
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"  CSV: {csv_path}")
    print(f"  Plot: {out_dir / 'track3_phase3e_refit_binding.png'}")
    print()

    # ─── Verdict ─────────────────────────────────────────────────
    print("=" * 110)
    print("VERDICT — Phase 3e")
    print("=" * 110)
    print()
    print(f"  At the global re-fit point (ε=0.205, s=0.025):")
    print()

    fe = next(r for r in rows if r['name'] == '56Fe')
    pb = next(r for r in rows if r['name'] == '208Pb')
    he = next(r for r in rows if r['name'] == '4He')
    d = next(r for r in rows if r['name'] == '2H')

    print(f"  ²H:    obs {d['B_obs']:.2f}, refit {d['B_refit']:.2f}  "
          f"(off by {d['ratio_refit']:.2f}×)")
    print(f"  ⁴He:   obs {he['B_obs']:.2f}, refit {he['B_refit']:.2f}  "
          f"(ratio {he['ratio_refit']:.3f})")
    print(f"  ⁵⁶Fe:  obs {fe['B_obs']:.2f}, refit {fe['B_refit']:.2f}  "
          f"(ratio {fe['ratio_refit']:.3f})")
    print(f"  ²⁰⁸Pb: obs {pb['B_obs']:.2f}, refit {pb['B_refit']:.2f}  "
          f"(ratio {pb['ratio_refit']:.3f})")
    print()
    print(f"  vs Coulomb-subtracted observation:")
    print(f"  ⁴He:   obs+C {he['B_obs_nonCoulomb']:.2f}, "
          f"refit/(obs+C) = {he['ratio_refit_nonC']:.3f}")
    print(f"  ⁵⁶Fe:  obs+C {fe['B_obs_nonCoulomb']:.2f}, "
          f"refit/(obs+C) = {fe['ratio_refit_nonC']:.3f}")
    print(f"  ²⁰⁸Pb: obs+C {pb['B_obs_nonCoulomb']:.2f}, "
          f"refit/(obs+C) = {pb['ratio_refit_nonC']:.3f}")


if __name__ == "__main__":
    main()
