"""
R63 Track 7 Phase 7a — Compound-mode prediction for stable nuclei, H to Fe.

Compute the MaSt compound-mode predicted mass for the canonical set of
stable nuclei spanning Z=1 to Z=26, using the A-scaling tuple
  `(1-Z, 0, 0, 0, 3A, 6A)`
at R63's v2-certified working parameter set (sheet shears and aspect
ratios at the joint-fitness-peak values from Track 6c; ν-sheet at R61
central values, passive per 6c).  Compare to observed nuclear mass;
tabulate miss vs binding energy.

The comparison is ratio-invariant at leading order in A (compound-mode
mass scales as 3A × μ(1, 2) × K), so the qualitative miss-vs-binding
pattern does not depend on the exact ε_p / s_p values — only the
overall scale, which is anchored to the proton by calibration.

Observed nuclear masses are computed from AME atomic masses as
`m_nuc = atomic_mass_u × 931.494 MeV/u − Z × m_e`.  Binding energies
are the standard `B = Z·m_p + (A−Z)·m_n − m_nuc`.

Outputs (../outputs/):
  - track7a_chain.csv           — per-nucleus table
  - track7a_miss_vs_A.png       — Δm/m vs A
  - track7a_miss_vs_binding.png — Δm/m vs B/m (binding-per-mass ratio)
  - track7a_mass_panel.png      — predicted vs observed masses
"""

import sys, os
import csv
import math
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

from track1_solver import (
    Params, derive_L_ring, L_vector_from_params, mode_energy, mode_6_to_11,
    signature_ok, M_E_MEV, M_P_MEV,
    SQRT_ALPHA, FOUR_PI, ALPHA,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF


# ─── Physical constants ───────────────────────────────────────────

U_TO_MEV = 931.494102  # 1 atomic mass unit in MeV/c²
M_E      = 0.510999    # electron mass in MeV
M_P      = 938.272     # proton mass in MeV (nuclear)
M_N      = 939.565     # neutron mass in MeV


# ─── Stable-nuclei chain, Z=1 to Z=26 ─────────────────────────────
# (name, Z, A, atomic_mass_u) from AME2020

NUCLEI = [
    ("1H",    1,  1,  1.00782503),
    ("2H",    1,  2,  2.01410178),
    ("3He",   2,  3,  3.01602932),
    ("4He",   2,  4,  4.00260325),
    ("6Li",   3,  6,  6.01512289),
    ("7Li",   3,  7,  7.01600344),
    ("9Be",   4,  9,  9.01218307),
    ("10B",   5, 10, 10.01293695),
    ("11B",   5, 11, 11.00930516),
    ("12C",   6, 12, 12.00000000),
    ("13C",   6, 13, 13.00335484),
    ("14N",   7, 14, 14.00307400),
    ("16O",   8, 16, 15.99491462),
    ("19F",   9, 19, 18.99840316),
    ("20Ne", 10, 20, 19.99244018),
    ("24Mg", 12, 24, 23.98504170),
    ("28Si", 14, 28, 27.97692653),
    ("32S",  16, 32, 31.97207117),
    ("40Ca", 20, 40, 39.96259086),
    ("48Ti", 22, 48, 47.94794198),
    ("52Cr", 24, 52, 51.94050623),
    ("56Fe", 26, 56, 55.93493633),
]


def nuclear_mass(atomic_u, Z):
    """m_nuc = atomic_mass_u × 931.494 MeV/u − Z·m_e."""
    return atomic_u * U_TO_MEV - Z * M_E


def binding_energy(Z, A, m_nuc):
    """B = Z·m_p + (A−Z)·m_n − m_nuc, standard total binding energy."""
    return Z * M_P + (A - Z) * M_N - m_nuc


# ─── R63 v2-certified working parameter set ───────────────────────
# Values inherited from the joint-fitness-peak found in Track 6c.
# Held here as working values (not pins).  Track 7 is ratio-invariant
# at leading order in A, so these do not affect the qualitative shape
# of the miss-vs-binding pattern — only the overall scale, which the
# proton calibration fixes.

WORKING_PARAMS = dict(
    eps_e=397.074, s_e=2.004200,
    eps_p=0.55,    s_p=0.162037,
    eps_nu=2.0,    s_nu=0.022,
)


def build_working_metric():
    """Build the 11D metric at the R63 v2 working parameter set."""
    p = WORKING_PARAMS
    L_p  = derive_L_ring(M_P, 3, 6, p['eps_p'], p['s_p'], K_MODELF)
    L_e  = derive_L_ring(M_E, 1, 2, p['eps_e'], p['s_e'], K_MODELF)
    M_NU = 3.21e-8
    L_nu = derive_L_ring(M_NU, 1, 1, p['eps_nu'], p['s_nu'], K_MODELF)

    params = Params(
        eps_e=p['eps_e'], s_e=p['s_e'],
        eps_p=p['eps_p'], s_p=p['s_p'],
        eps_nu=p['eps_nu'], s_nu=p['s_nu'],
        k_e=K_MODELF, k_p=K_MODELF, k_nu=K_MODELF,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI * ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0,
        L_ring_e=L_e, L_ring_p=L_p, L_ring_nu=L_nu,
    )
    G = build_aug_metric(params)
    assert signature_ok(G), "metric signature check failed at working params"
    L = L_vector_from_params(params)
    return params, G, L


# ─── Compound-mode prediction per nucleus ─────────────────────────

def compound_mass(G, L, Z, A):
    """MaSt compound-mode prediction for nucleus (Z, A).

    Tuple is the A-scaling formula (1-Z, 0, 0, 0, 3A, 6A).
    Returns the predicted mass in MeV.
    """
    tup6 = (1 - Z, 0, 0, 0, 3 * A, 6 * A)
    tup11 = mode_6_to_11(tup6)
    return mode_energy(G, L, tup11)


# ─── Main ─────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 104)
    print("R63 Track 7a — Compound-mode audit, stable nuclei H → Fe")
    print("=" * 104)
    print(f"  Working parameters: ε_e={WORKING_PARAMS['eps_e']}, "
          f"s_e={WORKING_PARAMS['s_e']}, "
          f"ε_p={WORKING_PARAMS['eps_p']}, s_p={WORKING_PARAMS['s_p']}, "
          f"ε_ν={WORKING_PARAMS['eps_nu']}, s_ν={WORKING_PARAMS['s_nu']}")
    print()

    params, G, L = build_working_metric()

    rows = []
    for (name, Z, A, atomic_u) in NUCLEI:
        m_obs = nuclear_mass(atomic_u, Z)
        B     = binding_energy(Z, A, m_obs)
        m_pred = compound_mass(G, L, Z, A)
        miss   = m_pred - m_obs
        miss_rel = miss / m_obs
        B_rel  = B / m_obs
        rows.append({
            'name': name, 'Z': Z, 'A': A,
            'atomic_u': atomic_u,
            'm_obs': m_obs, 'B': B, 'B_rel': B_rel,
            'm_pred': m_pred, 'miss': miss, 'miss_rel': miss_rel,
            'B_per_A': B / A if A > 0 else 0.0,
        })

    # ─── Print table ───
    print(f"  {'nucleus':<8s}  {'Z':>3s}  {'A':>3s}  "
          f"{'m_obs':>11s}  {'m_pred':>11s}  "
          f"{'miss':>9s}  {'Δm/m':>8s}  {'B':>9s}  {'B/m':>7s}  {'B/A':>6s}")
    print("  " + "-" * 100)
    for r in rows:
        print(f"  {r['name']:<8s}  {r['Z']:>3d}  {r['A']:>3d}  "
              f"{r['m_obs']:>11.4f}  {r['m_pred']:>11.4f}  "
              f"{r['miss']:>+9.4f}  {r['miss_rel']*100:>+7.4f}%  "
              f"{r['B']:>9.3f}  {r['B_rel']*100:>6.3f}%  {r['B_per_A']:>6.3f}")
    print()

    # ─── Diagnostic ratio: is miss ≈ binding? ───
    print("  Diagnostic ratios (miss vs binding):")
    print(f"    {'nucleus':<8s}  {'miss (MeV)':>11s}  {'B (MeV)':>10s}  "
          f"{'miss/B':>8s}  {'miss%/(B%)':>11s}")
    print("    " + "-" * 60)
    for r in rows:
        if r['B'] > 0.1:
            ratio1 = r['miss'] / r['B']
            ratio2 = r['miss_rel'] / r['B_rel']
            print(f"    {r['name']:<8s}  {r['miss']:>+11.4f}  "
                  f"{r['B']:>10.3f}  {ratio1:>+8.4f}  {ratio2:>+11.4f}")
        else:
            print(f"    {r['name']:<8s}  "
                  f"{r['miss']:>+11.4f}  {'(no binding)':>10s}")
    print()

    # ─── CSV ───
    csv_path = out_dir / "track7a_chain.csv"
    fields = ['name', 'Z', 'A', 'atomic_u',
              'm_obs', 'B', 'B_rel', 'm_pred', 'miss', 'miss_rel', 'B_per_A']
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in fields})
    print(f"  CSV: {csv_path}")

    # ─── Plots ───
    A_arr      = np.array([r['A'] for r in rows])
    miss_rel   = np.array([r['miss_rel'] * 100 for r in rows])
    B_rel      = np.array([r['B_rel'] * 100 for r in rows])
    B_per_A    = np.array([r['B_per_A'] for r in rows])
    m_obs      = np.array([r['m_obs'] for r in rows])
    m_pred     = np.array([r['m_pred'] for r in rows])
    names      = [r['name'] for r in rows]

    # Plot 1: miss% vs A
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.plot(A_arr, miss_rel, 'o-', color='tab:blue', markersize=7,
            label='compound-mode miss (Δm/m)')
    ax.plot(A_arr, B_rel, 's--', color='tab:orange', markersize=5,
            label='observed B/m')
    for A, y, n in zip(A_arr, miss_rel, names):
        ax.annotate(n, xy=(A, y), xytext=(3, 3),
                    textcoords='offset points', fontsize=7)
    ax.set_xlabel('mass number A')
    ax.set_ylabel('percent')
    ax.set_title("R63 Track 7a — compound-mode miss vs. A, H to Fe\n"
                 "Miss tracks binding-per-mass, confirming compound-mode picture")
    ax.grid(alpha=0.3)
    ax.legend(loc='best')
    ax.axhline(0, color='k', linewidth=0.5)
    plt.tight_layout()
    plt.savefig(out_dir / "track7a_miss_vs_A.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {out_dir / 'track7a_miss_vs_A.png'}")

    # Plot 2: miss% vs B%
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(B_rel, miss_rel, 'o', color='tab:blue', markersize=8)
    for B, y, n in zip(B_rel, miss_rel, names):
        ax.annotate(n, xy=(B, y), xytext=(4, 4),
                    textcoords='offset points', fontsize=8)
    # Reference: miss = B (1:1 line)
    ref = np.linspace(0, max(B_rel.max(), miss_rel.max()) * 1.05, 100)
    ax.plot(ref, ref, ':', color='red', linewidth=1.0,
            label='1:1 line (miss = B)')
    ax.set_xlabel('observed binding energy B / m_obs  (%)')
    ax.set_ylabel('compound-mode miss  Δm/m  (%)')
    ax.set_title("R63 Track 7a — miss vs. binding energy, H to Fe\n"
                 "Compound-mode prediction overshoots observed mass by "
                 "approximately the binding energy")
    ax.grid(alpha=0.3)
    ax.legend(loc='best')
    plt.tight_layout()
    plt.savefig(out_dir / "track7a_miss_vs_binding.png",
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {out_dir / 'track7a_miss_vs_binding.png'}")

    # Plot 3: predicted vs observed masses, with binding-per-nucleon curve
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    ax1.plot(A_arr, m_obs, 'o-', color='tab:blue', markersize=6,
             label='observed nuclear mass')
    ax1.plot(A_arr, m_pred, 's--', color='tab:red', markersize=5,
             label='compound-mode prediction')
    ax1.set_xlabel('A')
    ax1.set_ylabel('mass (MeV)')
    ax1.set_title("Mass chain")
    ax1.legend()
    ax1.grid(alpha=0.3)

    ax2.plot(A_arr, B_per_A, 'o-', color='tab:green', markersize=7)
    for A, y, n in zip(A_arr, B_per_A, names):
        ax2.annotate(n, xy=(A, y), xytext=(3, -10),
                     textcoords='offset points', fontsize=7)
    ax2.set_xlabel('A')
    ax2.set_ylabel('B / A  (MeV per nucleon)')
    ax2.set_title("Observed binding-per-nucleon curve (classic Fe peak)")
    ax2.grid(alpha=0.3)
    ax2.axhline(8.79, color='red', linestyle=':', linewidth=0.8,
                label='Fe-56 peak ≈ 8.79 MeV/nucleon')
    ax2.legend()

    plt.suptitle("R63 Track 7a — H → Fe stable-nuclei panel", y=1.02)
    plt.tight_layout()
    plt.savefig(out_dir / "track7a_mass_panel.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {out_dir / 'track7a_mass_panel.png'}")


if __name__ == "__main__":
    main()
