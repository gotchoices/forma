"""
R64 Track 14 — Nuclear binding from Ma compound mode mass deficit.

For each nucleus (Z, N), compute the predicted Ma compound mass at
Point A using R64's u/d composition rule:
    n_pt = 3·A
    n_pr = 2·Z − 2·N = 2·(2Z − A)

Compare to:
    M_free = Z·M_p + N·M_n
    M_obs  = M_free − B_obs  (binding releases mass)

The decomposition:
    Δ_Ma  = m_Ma(compound) − M_free
    Δ_S   = (M_free − B_obs) − m_Ma(compound) = -Δ_Ma − B_obs

If Δ_Ma alone explains B (Δ_S ≈ 0), the binding is "pure Ma compound."
If Δ_S < 0, S-side residual provides additional binding.
If Δ_S > 0, the compound is heavier than observed — Ma over-binds.

This is not a force calculation, just an energy assessment.
"""

import math
import csv
from pathlib import Path


# Point A from R64 Track 1 (calibrated to nucleon properties + G_F)
EPS_P = 0.07309
S_P = 0.19387
K_P = 22.847

# Point B from R64 Track 3 (calibrated to nuclear chain Ca→Sn)
EPS_P_B = 0.2052
S_P_B = 0.0250
K_P_B = 63.629

M_P = 938.272
M_N = 939.565


def m_Ma(n_pt, n_pr, eps=EPS_P, s=S_P, K=K_P):
    return K * math.sqrt((n_pt / eps) ** 2 + (n_pr - s * n_pt) ** 2)


# Nuclear data: Z, N, B_obs (MeV, total binding)
NUCLEI = [
    # (label, Z, N, B_obs_total_MeV)
    ("²H",   1, 1,    2.224),
    ("³H",   1, 2,    8.482),
    ("³He",  2, 1,    7.718),
    ("⁴He",  2, 2,   28.296),
    ("⁶Li",  3, 3,   31.994),
    ("⁷Li",  3, 4,   39.245),
    ("⁹Be",  4, 5,   58.165),
    ("¹⁰B",  5, 5,   64.751),
    ("¹²C",  6, 6,   92.162),
    ("¹⁴N",  7, 7,  104.659),
    ("¹⁶O",  8, 8,  127.619),
    ("²⁰Ne", 10, 10, 160.645),
    ("²⁴Mg", 12, 12, 198.257),
    ("²⁸Si", 14, 14, 236.537),
    ("³²S",  16, 16, 271.781),
    ("⁴⁰Ca", 20, 20, 342.052),
    ("⁵⁶Fe", 26, 30, 492.258),
    ("⁹⁰Zr", 40, 50, 783.893),
    ("¹²⁰Sn",50, 70, 1020.55),
]


def analyze(label_pt, eps, s, K):
    print()
    print("=" * 100)
    print(f"  {label_pt}: ε = {eps}, s = {s}, K = {K}")
    print("=" * 100)
    print(f"  {'nucleus':<6s} {'Z':>3s} {'N':>3s} {'A':>3s}  "
          f"{'(n_pt, n_pr)':>14s}  "
          f"{'m_Ma (MeV)':>11s}  {'M_free (MeV)':>13s}  "
          f"{'Δ_Ma':>9s}  {'B_obs':>9s}  {'Δ_S':>10s}  "
          f"{'Δ_S/B_obs':>10s}")
    print("  " + "─" * 110)

    rows = []
    for label, Z, N, B_obs in NUCLEI:
        A = Z + N
        n_pt = 3 * A
        n_pr = 2 * Z - 2 * N
        m_compound = m_Ma(n_pt, n_pr, eps, s, K)
        M_free = Z * M_P + N * M_N
        Δ_Ma = m_compound - M_free            # negative = Ma binding
        Δ_S = -Δ_Ma - B_obs                    # what S must add (negative = S binding)
        ratio = Δ_S / B_obs if B_obs > 0 else float('nan')
        print(f"  {label:<6s} {Z:>3d} {N:>3d} {A:>3d}  "
              f"({n_pt:>4d},{n_pr:>+5d})  "
              f"{m_compound:>11.3f}  {M_free:>13.3f}  "
              f"{Δ_Ma:>+9.3f}  {-B_obs:>+9.3f}  {Δ_S:>+10.3f}  "
              f"{ratio:>+10.3f}")
        rows.append({
            "nucleus": label, "Z": Z, "N": N, "A": A,
            "n_pt": n_pt, "n_pr": n_pr,
            "m_Ma_pred": m_compound, "M_free": M_free,
            "Delta_Ma": Δ_Ma, "B_obs": -B_obs,
            "Delta_S": Δ_S, "Delta_S_frac_of_B": ratio,
        })
    return rows


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R64 Track 14 — Nuclear binding from Ma compound mode mass")
    print("=" * 100)
    print()
    print("  Energy budget:")
    print("    Δ_Ma  = m_Ma(compound) − M_free   [predicted Ma binding]")
    print("    Δ_S   = -Δ_Ma − B_obs              [residual: S-side binding required]")
    print("    Δ_S = 0 means Ma-side fully accounts for binding")
    print("    Δ_S < 0 means S-side adds binding beyond Ma")
    print("    Δ_S/B_obs is the fractional S contribution")
    print()

    rows_A = analyze("Point A (Track 1)", EPS_P, S_P, K_P)
    rows_B = analyze("Point B (Track 3)", EPS_P_B, S_P_B, K_P_B)

    # Save CSV
    csv_path = out_dir / "track14_nuclear_compound_scan.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "point", "nucleus", "Z", "N", "A",
            "n_pt", "n_pr",
            "m_Ma_pred", "M_free",
            "Delta_Ma", "B_obs",
            "Delta_S", "Delta_S_frac_of_B",
        ])
        writer.writeheader()
        for r in rows_A:
            r2 = dict(r); r2["point"] = "A"; writer.writerow(r2)
        for r in rows_B:
            r2 = dict(r); r2["point"] = "B"; writer.writerow(r2)
    print()
    print(f"  CSV: {csv_path}")
    print()

    # ── Verdict ─────────────────────────────────────────────────────
    print("=" * 100)
    print("VERDICT — Track 14")
    print("=" * 100)
    print()
    # Compute Δ_Ma fraction of binding for both points
    for label, rows in [("Point A", rows_A), ("Point B", rows_B)]:
        ma_fracs = []
        for r in rows:
            if r["B_obs"] != 0:
                frac = -r["Delta_Ma"] / -r["B_obs"]   # Δ_Ma fraction of total binding
                ma_fracs.append((r["nucleus"], r["A"], frac))
        if ma_fracs:
            print(f"  {label}: Ma fraction of total binding (1.0 = Ma alone explains B)")
            for nuc, A, frac in ma_fracs[:5]:   # light nuclei
                print(f"    {nuc} (A={A}): {frac*100:>6.1f}% Ma  ({(1-frac)*100:>5.1f}% S)")
            print(f"    ...")
            for nuc, A, frac in ma_fracs[-3:]:  # heavy nuclei
                print(f"    {nuc} (A={A}): {frac*100:>6.1f}% Ma  ({(1-frac)*100:>5.1f}% S)")
            print()


if __name__ == "__main__":
    main()
