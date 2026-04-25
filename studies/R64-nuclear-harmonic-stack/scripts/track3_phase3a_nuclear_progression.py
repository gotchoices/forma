"""
R64 Track 3 Phase 3a — Nuclear progression audit, H to U.

Tests R64's harmonic-stack model (flavor-aware additive winding on the
p-sheet at the magic point) against the observed nuclear binding curve
across the full stable-isotope chain.

Under flavor-aware composition with u = (1, +2), d = (1, −2) at the
magic point (ε_p=0.07309, s_p=0.19387, K_p=22.847 MeV/μ):
  - Proton (uud) → (3, +2) on p-sheet, mass 938.272 MeV (anchor)
  - Neutron (udd) → (3, −2), mass 939.565 MeV
  - Nucleus (Z, A) → (3·A, 2·(2Z − A)) under additive winding

Computes for each stable isotope:
  - Predicted mass m_pred = K_p · √((3A/ε_p)² + (2(2Z−A) − 3·s_p·A)²)
  - Predicted binding B_pred = Z·m_p + (A−Z)·m_n − m_pred
  - Compares to observed binding from AME2020

Phase 3b: for each A, scans Z to find mass-minimizing Z (predicted
valley of stability); compares to observed.

Outputs:
  outputs/track3_phase3a_nuclei.csv
  outputs/track3_phase3a_binding_curve.png
  outputs/track3_phase3b_valley_of_stability.png
  outputs/track3_phase3b_valley_of_stability.csv
"""

import math
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# ─── Magic point from R64 Track 1 Phase 1c ────────────────────────────

EPS_P = 0.073092553872
S_P   = 0.193871467423
K_P   = 22.846596    # MeV/μ-unit


# ─── Constants ─────────────────────────────────────────────────────────

M_P = 938.27208816    # MeV
M_N = 939.56542052    # MeV
M_E = 0.51099895      # MeV
U_TO_MEV = 931.49410242   # 1 atomic mass unit in MeV


# ─── Stable nuclei H to U (representative, AME2020 atomic masses) ─────
# (name, Z, A, atomic_mass_u)
NUCLEI = [
    ("1H",     1,   1,  1.00782503207),
    ("2H",     1,   2,  2.01410177812),
    ("3H",     1,   3,  3.01604927791),
    ("3He",    2,   3,  3.01602932265),
    ("4He",    2,   4,  4.00260325413),
    ("6Li",    3,   6,  6.01512288742),
    ("7Li",    3,   7,  7.01600343426),
    ("9Be",    4,   9,  9.01218306500),
    ("10B",    5,  10, 10.01293695100),
    ("11B",    5,  11, 11.00930516000),
    ("12C",    6,  12, 12.00000000000),
    ("13C",    6,  13, 13.00335484430),
    ("14N",    7,  14, 14.00307400443),
    ("16O",    8,  16, 15.99491461957),
    ("19F",    9,  19, 18.99840316273),
    ("20Ne",  10,  20, 19.99244017540),
    ("23Na",  11,  23, 22.98976928200),
    ("24Mg",  12,  24, 23.98504170000),
    ("27Al",  13,  27, 26.98153853000),
    ("28Si",  14,  28, 27.97692653320),
    ("31P",   15,  31, 30.97376199842),
    ("32S",   16,  32, 31.97207117000),
    ("35Cl",  17,  35, 34.96885268000),
    ("40Ar",  18,  40, 39.96238312370),
    ("39K",   19,  39, 38.96370648700),
    ("40Ca",  20,  40, 39.96259086000),
    ("45Sc",  21,  45, 44.95590828000),
    ("48Ti",  22,  48, 47.94794198000),
    ("51V",   23,  51, 50.94395704000),
    ("52Cr",  24,  52, 51.94050623000),
    ("55Mn",  25,  55, 54.93804451000),
    ("56Fe",  26,  56, 55.93493633000),
    ("59Co",  27,  59, 58.93319429000),
    ("60Ni",  28,  60, 59.93078588000),
    ("63Cu",  29,  63, 62.92959772000),
    ("64Zn",  30,  64, 63.92914201000),
    ("70Ge",  32,  70, 69.92424875000),
    ("75As",  33,  75, 74.92159457000),
    ("80Se",  34,  80, 79.91652180000),
    ("84Kr",  36,  84, 83.91149773000),
    ("88Sr",  38,  88, 87.90561226000),
    ("89Y",   39,  89, 88.90584030000),
    ("90Zr",  40,  90, 89.90470373000),
    ("93Nb",  41,  93, 92.90637820000),
    ("98Mo",  42,  98, 97.90540482000),
    ("103Rh", 45, 103,102.90549800000),
    ("108Pd", 46, 108,107.90389220000),
    ("107Ag", 47, 107,106.90509300000),
    ("114Cd", 48, 114,113.90336509000),
    ("115In", 49, 115,114.90387800000),
    ("120Sn", 50, 120,119.90220163000),
    ("130Te", 52, 130,129.90622275000),
    ("127I",  53, 127,126.90447190000),
    ("132Xe", 54, 132,131.90415509000),
    ("133Cs", 55, 133,132.90545196000),
    ("138Ba", 56, 138,137.90524700000),
    ("139La", 57, 139,138.90636350000),
    ("140Ce", 58, 140,139.90544310000),
    ("141Pr", 59, 141,140.90765760000),
    ("142Nd", 60, 142,141.90772900000),
    ("152Sm", 62, 152,151.91973970000),
    ("153Eu", 63, 153,152.92123800000),
    ("158Gd", 64, 158,157.92411230000),
    ("159Tb", 65, 159,158.92535470000),
    ("164Dy", 66, 164,163.92918190000),
    ("165Ho", 67, 165,164.93032880000),
    ("166Er", 68, 166,165.93029950000),
    ("169Tm", 69, 169,168.93421790000),
    ("174Yb", 70, 174,173.93886640000),
    ("175Lu", 71, 175,174.94077720000),
    ("180Hf", 72, 180,179.94655940000),
    ("181Ta", 73, 181,180.94800300000),
    ("184W",  74, 184,183.95093090000),
    ("187Re", 75, 187,186.95575010000),
    ("192Os", 76, 192,191.96148070000),
    ("193Ir", 77, 193,192.96292160000),
    ("195Pt", 78, 195,194.96479170000),
    ("197Au", 79, 197,196.96656870000),
    ("202Hg", 80, 202,201.97064340000),
    ("205Tl", 81, 205,204.97442700000),
    ("208Pb", 82, 208,207.97665250000),
    ("209Bi", 83, 209,208.98039910000),
    ("232Th", 90, 232,232.03805580000),
    ("235U",  92, 235,235.04392990000),
    ("238U",  92, 238,238.05078826000),
]


def nuclear_mass(atomic_u, Z):
    """m_nuc = atomic_mass_u × 931.494 MeV/u − Z·m_e (electron binding ignored)."""
    return atomic_u * U_TO_MEV - Z * M_E


def observed_binding(Z, A, m_nuc):
    """B_obs = Z·m_p + (A−Z)·m_n − m_nuc."""
    return Z * M_P + (A - Z) * M_N - m_nuc


# ─── R64 prediction ────────────────────────────────────────────────────

def mu2(n_t, n_r, eps=EPS_P, s=S_P):
    return (n_t / eps)**2 + (n_r - s * n_t)**2


def predicted_mass(Z, A):
    """R64 flavor-aware additive composition:
       nucleus tuple = (3·A, 2·(2Z − A))
       mass = K_p · √((3A/ε)² + (2(2Z−A) − 3·s·A)²)
    """
    n_pt = 3 * A
    n_pr = 2 * (2 * Z - A)
    return K_P * math.sqrt(mu2(n_pt, n_pr))


def predicted_binding(Z, A):
    return Z * M_P + (A - Z) * M_N - predicted_mass(Z, A)


# ─── Main ──────────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 3 Phase 3a — Nuclear progression audit, H to U")
    print("=" * 110)
    print()
    print(f"  Magic point: ε_p = {EPS_P:.6f}, s_p = {S_P:.6f}, K_p = {K_P:.4f}")
    print()
    print(f"  R64 composition rule: (Z, A) → (3A, 2(2Z-A)) on p-sheet, "
          f"flat-formula mass.")
    print()

    # ─── Phase 3a: nuclei mass and binding ──────────────────────────
    print(f"Phase 3a — Mass and binding for {len(NUCLEI)} nuclei")
    print("-" * 110)
    print(f"  {'nucleus':>8s} {'Z':>3s} {'A':>3s}  "
          f"{'m_obs (MeV)':>12s} {'m_pred (MeV)':>14s} "
          f"{'Δm (MeV)':>10s} {'Δm/m':>8s}  "
          f"{'B_obs':>8s} {'B_pred':>9s} {'B/A_obs':>9s} {'B/A_pred':>9s}")

    rows = []
    for name, Z, A, atomic_u in NUCLEI:
        m_obs = nuclear_mass(atomic_u, Z)
        b_obs = observed_binding(Z, A, m_obs)
        m_pred = predicted_mass(Z, A)
        b_pred = predicted_binding(Z, A)
        d_m = m_pred - m_obs
        rel = d_m / m_obs

        print(f"  {name:>8s} {Z:>3d} {A:>3d}  "
              f"{m_obs:>12.3f} {m_pred:>14.3f} "
              f"{d_m:>+10.3f} {rel:>+7.3%}  "
              f"{b_obs:>8.2f} {b_pred:>9.3f} {b_obs/A:>9.3f} {b_pred/A:>9.4f}")
        rows.append({
            'name': name, 'Z': Z, 'A': A,
            'atomic_u': atomic_u,
            'm_obs_MeV': m_obs, 'm_pred_MeV': m_pred,
            'delta_m': d_m, 'delta_m_over_m': rel,
            'B_obs_MeV': b_obs, 'B_pred_MeV': b_pred,
            'B_per_A_obs': b_obs / A, 'B_per_A_pred': b_pred / A,
        })

    print()
    max_rel = max(abs(r['delta_m_over_m']) for r in rows)
    mean_rel = np.mean([abs(r['delta_m_over_m']) for r in rows])
    print(f"  Max |Δm/m| = {max_rel:.2%}, mean |Δm/m| = {mean_rel:.2%}")
    print()

    # Save
    csv_path = out_dir / "track3_phase3a_nuclei.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # ─── Plot binding curve ──────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))

    A_arr = np.array([r['A'] for r in rows])
    Z_arr = np.array([r['Z'] for r in rows])
    Bobs_arr = np.array([r['B_obs_MeV'] for r in rows])
    Bpred_arr = np.array([r['B_pred_MeV'] for r in rows])
    BA_obs = np.array([r['B_per_A_obs'] for r in rows])
    BA_pred = np.array([r['B_per_A_pred'] for r in rows])

    # Top-left: B/A vs A
    ax = axes[0, 0]
    ax.plot(A_arr, BA_obs, 'o-', color='tab:blue', label='Observed', markersize=4)
    ax.plot(A_arr, BA_pred, 's--', color='tab:orange', label='R64 predicted',
            markersize=3, alpha=0.8)
    ax.set_xlabel('A')
    ax.set_ylabel('B/A (MeV)')
    ax.set_title('Binding energy per nucleon')
    ax.grid(alpha=0.3)
    ax.legend()

    # Top-right: total binding vs A (log-log)
    ax = axes[0, 1]
    ax.plot(A_arr, Bobs_arr, 'o-', color='tab:blue', label='Observed',
            markersize=4)
    ax.plot(A_arr, np.maximum(Bpred_arr, 1e-3), 's--', color='tab:orange',
            label='R64 predicted', markersize=3, alpha=0.8)
    ax.set_xlabel('A')
    ax.set_ylabel('Total binding (MeV)')
    ax.set_yscale('symlog', linthresh=1)
    ax.set_title('Total binding (predicted vs observed)')
    ax.grid(alpha=0.3)
    ax.legend()

    # Bottom-left: relative mass error
    ax = axes[1, 0]
    rel_arr = np.array([r['delta_m_over_m'] * 100 for r in rows])
    ax.plot(A_arr, rel_arr, 'o-', color='tab:red', markersize=4)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('A')
    ax.set_ylabel('Δm/m (%)')
    ax.set_title('Predicted - observed mass (relative)')
    ax.grid(alpha=0.3)

    # Bottom-right: predicted binding-per-nucleon detail
    ax = axes[1, 1]
    ax.plot(A_arr, BA_pred, 's-', color='tab:orange', markersize=3)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xlabel('A')
    ax.set_ylabel('B/A predicted (MeV)')
    ax.set_title('R64 prediction shape (zoomed)')
    ax.grid(alpha=0.3)

    plt.tight_layout()
    fig.savefig(out_dir / "track3_phase3a_binding_curve.png",
                dpi=150, bbox_inches='tight')
    plt.close()

    # ─── Phase 3b: valley of stability ──────────────────────────
    print()
    print("Phase 3b — Valley of stability (predicted vs observed)")
    print("-" * 110)
    print()

    # Analytical: optimal Z for fixed A under additive winding
    # μ²(3A, 2(2Z-A)) = (3A/ε)² + (2(2Z-A) - 3sA)²
    # Minimum w.r.t. Z when 2(2Z-A) = 3sA → Z = A·(2 + 3s)/4
    Z_optimal_factor = (2 + 3 * S_P) / 4
    print(f"  Analytical Z_optimal/A = (2 + 3·s_p)/4 = "
          f"{Z_optimal_factor:.6f}")
    print(f"  Predicted: Z/A ≈ {Z_optimal_factor:.4f} for ALL A "
          f"(constant — proton-rich)")
    print()

    print(f"  Comparison at observed data points:")
    print(f"  {'nucleus':>8s} {'A':>3s} {'Z_obs':>6s} {'Z/A_obs':>9s} "
          f"{'Z_pred':>8s} {'Z/A_pred':>9s} {'ΔZ':>6s}")
    valley_rows = []
    for name, Z, A, _ in NUCLEI:
        Z_pred = Z_optimal_factor * A
        d_z = Z_pred - Z
        print(f"  {name:>8s} {A:>3d} {Z:>6d} {Z/A:>9.4f} "
              f"{Z_pred:>8.2f} {Z_optimal_factor:>9.4f} {d_z:>+6.1f}")
        valley_rows.append({
            'name': name, 'Z_obs': Z, 'A': A,
            'Z_obs_over_A': Z / A,
            'Z_pred_optimal': Z_pred,
            'Z_pred_over_A': Z_optimal_factor,
            'delta_Z': d_z,
        })

    csv_b = out_dir / "track3_phase3b_valley_of_stability.csv"
    with open(csv_b, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(valley_rows[0].keys()))
        w.writeheader()
        w.writerows(valley_rows)

    # Valley plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    Zobs_arr = np.array([r['Z_obs'] for r in valley_rows])
    A_arr2 = np.array([r['A'] for r in valley_rows])
    Zpred_arr = np.array([r['Z_pred_optimal'] for r in valley_rows])

    ax = axes[0]
    ax.plot(A_arr2, Zobs_arr, 'o-', color='tab:blue', label='Observed Z',
            markersize=5)
    ax.plot(A_arr2, Zpred_arr, 's--', color='tab:orange',
            label=f'R64 predicted Z = {Z_optimal_factor:.4f}·A',
            markersize=4, alpha=0.8)
    ax.plot(A_arr2, A_arr2 / 2, ':', color='gray', alpha=0.5,
            label='Z = A/2 (light-nucleus reference)')
    ax.set_xlabel('A')
    ax.set_ylabel('Z (proton number)')
    ax.set_title('Valley of stability: R64 vs observed')
    ax.grid(alpha=0.3)
    ax.legend()

    ax = axes[1]
    ax.plot(A_arr2, Zobs_arr / A_arr2, 'o-', color='tab:blue',
            label='Observed Z/A', markersize=5)
    ax.axhline(Z_optimal_factor, color='tab:orange', linestyle='--',
               label=f'R64 prediction = {Z_optimal_factor:.4f}')
    ax.axhline(0.5, color='gray', linestyle=':', alpha=0.5,
               label='Z/A = 0.5')
    ax.set_xlabel('A')
    ax.set_ylabel('Z/A')
    ax.set_title('Z/A ratio: R64 (constant) vs observed (decreasing)')
    ax.grid(alpha=0.3)
    ax.legend()

    plt.tight_layout()
    fig.savefig(out_dir / "track3_phase3b_valley_of_stability.png",
                dpi=150, bbox_inches='tight')
    plt.close()

    # ─── Verdict ────────────────────────────────────────────────
    print()
    print("=" * 110)
    print("VERDICT — Phase 3a + 3b")
    print("=" * 110)
    print()

    # Summary
    fe_row = next(r for r in rows if r['name'] == '56Fe')
    pb_row = next(r for r in rows if r['name'] == '208Pb')
    he_row = next(r for r in rows if r['name'] == '4He')
    d_row  = next(r for r in rows if r['name'] == '2H')

    print("  Binding-energy comparison at key benchmarks:")
    print(f"    {'nucleus':>8s} {'B_obs':>10s} {'B_pred':>10s} "
          f"{'ratio (pred/obs)':>20s}")
    for r in [d_row, he_row, fe_row, pb_row]:
        ratio = r['B_pred_MeV'] / r['B_obs_MeV']
        print(f"    {r['name']:>8s} {r['B_obs_MeV']:>10.2f} "
              f"{r['B_pred_MeV']:>10.3f} {ratio:>19.4f}")
    print()

    print("  Valley-of-stability:")
    print(f"    R64 predicts: Z/A = {Z_optimal_factor:.4f} (constant, "
          f"proton-rich)")
    print(f"    Observed:     Z/A ≈ 0.5 (light) decreasing to ~0.40 (Pb)")
    print(f"    R64 predicts WRONG DIRECTION: more protons than neutrons.")
    print()

    print("  Mass prediction errors:")
    print(f"    Max |Δm/m| = {max_rel:.2%}")
    print(f"    Mean |Δm/m| = {mean_rel:.2%}")
    print()

    print(f"  Predicted vs observed B(²H) ratio: "
          f"{d_row['B_pred_MeV']/d_row['B_obs_MeV']:.4f}")
    print(f"  Predicted vs observed B(⁴He) ratio: "
          f"{he_row['B_pred_MeV']/he_row['B_obs_MeV']:.4f}")
    print(f"  Predicted vs observed B(⁵⁶Fe) ratio: "
          f"{fe_row['B_pred_MeV']/fe_row['B_obs_MeV']:.4f}")
    print(f"  Predicted vs observed B(²⁰⁸Pb) ratio: "
          f"{pb_row['B_pred_MeV']/pb_row['B_obs_MeV']:.4f}")
    print()

    print(f"  CSVs:  {csv_path}")
    print(f"         {csv_b}")
    print(f"  Plots: {out_dir / 'track3_phase3a_binding_curve.png'}")
    print(f"         {out_dir / 'track3_phase3b_valley_of_stability.png'}")


if __name__ == "__main__":
    main()
