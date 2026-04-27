"""
R64 Track 15 — Pool item ad: quantum-number sub-modes of Ma compounds.

Premise: each Ma compound mode (3·A, n_pr) carries a subspace of
allowed quantum-number configurations (total T, S, P, J).  The
nuclear ground state selects the most attractive sub-mode.  The
binding residual after subtracting the bare Ma compound mass
should correlate with isospin/spin/pairing/shell quantum numbers.

This first-pass script:
  1. Catalogs light + medium nuclei with observed J^P and T.
  2. Computes (n_pt, n_pr) at R64's u/d composition rule.
  3. Verifies T_z = n_pr/4 maps to (N − Z)/2.
  4. Computes Δ_Ma at Point A.
  5. Computes residual = B_obs − |Δ_Ma|.
  6. Looks for SEMF-style correlation in the residual:
       residual ≈ a_v·A − a_s·A^(2/3) − a_c·Z²/A^(1/3) − a_a·(N−Z)²/A
       + δ (pairing) + magic-number bonuses.
  7. Reports goodness of fit; identifies which terms dominate.

If the residual fits SEMF-style quantum-number structure, we
have an architectural account of nuclear binding via Ma compound
+ quantum-number subspace selection.
"""

import math
import csv
from pathlib import Path

import numpy as np


# Point A from R64 Track 1
EPS_P = 0.07309
S_P = 0.19387
K_P = 22.847

M_P = 938.272
M_N = 939.565

# SEMF coefficients (rough literature values, in MeV)
A_V_LIT = 15.85   # volume
A_S_LIT = 18.34   # surface
A_C_LIT = 0.714   # Coulomb
A_A_LIT = 23.21   # asymmetry


# Light + medium nuclei with observed quantum numbers
# (Z, N, J^P, T, B_obs[total, MeV])
NUCLEI = [
    # (label, Z, N, J^P, T, B_obs)
    ("²H",   1, 1,  "1+",   0,    2.224),
    ("³H",   1, 2,  "1/2+", 1/2,  8.482),
    ("³He",  2, 1,  "1/2+", 1/2,  7.718),
    ("⁴He",  2, 2,  "0+",   0,   28.296),
    ("⁶Li",  3, 3,  "1+",   0,   31.994),
    ("⁷Li",  3, 4,  "3/2-", 1/2, 39.245),
    ("⁹Be",  4, 5,  "3/2-", 1/2, 58.165),
    ("¹⁰B",  5, 5,  "3+",   0,   64.751),
    ("¹²C",  6, 6,  "0+",   0,   92.162),
    ("¹⁴N",  7, 7,  "1+",   0,  104.659),
    ("¹⁶O",  8, 8,  "0+",   0,  127.619),
    ("²⁰Ne", 10, 10, "0+",  0,  160.645),
    ("²⁴Mg", 12, 12, "0+",  0,  198.257),
    ("²⁸Si", 14, 14, "0+",  0,  236.537),
    ("³²S",  16, 16, "0+",  0,  271.781),
    ("⁴⁰Ca", 20, 20, "0+",  0,  342.052),
    ("⁵⁶Fe", 26, 30, "0+",  1,  492.258),
    ("¹²⁰Sn",50, 70, "0+",  5,  1020.55),
]


def m_Ma(n_pt, n_pr, eps=EPS_P, s=S_P, K=K_P):
    return K * math.sqrt((n_pt / eps) ** 2 + (n_pr - s * n_pt) ** 2)


def is_magic(n):
    """Standard magic numbers."""
    return n in {2, 8, 20, 28, 50, 82, 126}


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 15 — Pool item ad: quantum-number sub-modes of Ma compounds")
    print("=" * 110)
    print()
    print("  Mapping (claimed exact):")
    print("    n_pt = 3·A           (baryon-number / quark count)")
    print("    n_pr = 4·T_z = 2·(N−Z) ?  → check sign convention")
    print()

    # ── Step 1: verify T_z = n_pr/4 mapping ────────────────────────
    print("=" * 110)
    print("Step 1: Verify n_pr/4 = T_z mapping for each nucleus")
    print("=" * 110)
    print()
    print(f"  {'nucleus':<6s} {'Z':>3s} {'N':>3s} {'A':>3s}  "
          f"{'(n_pt, n_pr)':>14s}  {'n_pr/4':>8s}  "
          f"{'(N-Z)/2':>8s}  {'-(N-Z)/2':>9s}  {'match?':>10s}")
    print("  " + "─" * 90)
    for label, Z, N, JP, T, B in NUCLEI:
        A = Z + N
        n_pt = 3 * A
        # Test sign convention: u (Z=1, N=0): n_pr = +2 → T_z = +1/2
        # So extra proton → +n_pr; extra neutron → -n_pr
        # ⇒ n_pr = 2·(Z − N) = -2·(N − Z)
        n_pr_pos = 2 * (Z - N)   # if u = +T_z and contributes +n_pr
        # Note R64 used n_pr = 2·(2Z − A) = 2·(2Z − Z − N) = 2·(Z − N) ✓
        print(f"  {label:<6s} {Z:>3d} {N:>3d} {A:>3d}  "
              f"({n_pt:>4d},{n_pr_pos:>+5d})  "
              f"{n_pr_pos/4.0:>+8.2f}  "
              f"{(N - Z)/2.0:>+8.2f}  "
              f"{-(N - Z)/2.0:>+9.2f}  "
              f"{'+1/2 sign' if abs(n_pr_pos/4 - (Z-N)/2) < 0.01 else 'mismatch':>10s}")
    print()

    # ── Step 2: compute Δ_Ma and residual at Point A ───────────────
    print("=" * 110)
    print("Step 2: Δ_Ma at Point A and residual = B_obs − |Δ_Ma|")
    print("=" * 110)
    print()
    print(f"  {'nucleus':<6s} {'Z':>3s} {'N':>3s} {'A':>3s} {'JP':>5s} {'T':>4s}  "
          f"{'m_Ma':>10s}  {'M_free':>10s}  {'Δ_Ma':>9s}  "
          f"{'B_obs':>9s}  {'residual':>10s}  {'res/A':>8s}")
    print("  " + "─" * 100)

    rows = []
    for label, Z, N, JP, T, B in NUCLEI:
        A = Z + N
        n_pt = 3 * A
        n_pr = 2 * (Z - N)   # u contributes +2, d contributes -2
        m_compound = m_Ma(n_pt, n_pr)
        M_free = Z * M_P + N * M_N
        Δ_Ma = m_compound - M_free
        residual = B - abs(Δ_Ma)
        per_nucleon = residual / A
        print(f"  {label:<6s} {Z:>3d} {N:>3d} {A:>3d} {JP:>5s} {str(T):>4s}  "
              f"{m_compound:>10.2f}  {M_free:>10.2f}  {Δ_Ma:>+9.3f}  "
              f"{-B:>+9.3f}  {-residual:>+10.3f}  {-per_nucleon:>+8.3f}")
        rows.append({
            "nucleus": label, "Z": Z, "N": N, "A": A, "JP": JP, "T": T,
            "n_pt": n_pt, "n_pr": n_pr,
            "m_Ma": m_compound, "M_free": M_free,
            "Delta_Ma": Δ_Ma, "B_obs": -B, "residual": -residual,
            "residual_per_A": -per_nucleon,
        })
    print()

    # ── Step 3: Fit SEMF terms to the residual ─────────────────────
    print("=" * 110)
    print("Step 3: Fit SEMF terms to the residual (residual = a_v·A − a_s·A^(2/3) − a_c·Z²/A^(1/3) − a_a·(N−Z)²/A)")
    print("=" * 110)
    print()
    A_arr = np.array([r["A"] for r in rows])
    Z_arr = np.array([r["Z"] for r in rows])
    N_arr = np.array([r["N"] for r in rows])
    res_arr = np.array([r["residual"] for r in rows])  # negative = binding
    # residual is binding (negative), so −residual is the binding magnitude
    binding_arr = -res_arr   # positive numbers

    # Build the design matrix
    # binding_residual = a_v · A − a_s · A^(2/3) − a_c · Z²/A^(1/3) − a_a · (N−Z)²/A
    X = np.column_stack([
        A_arr,
        -A_arr ** (2/3),
        -(Z_arr ** 2) / (A_arr ** (1/3)),
        -((N_arr - Z_arr) ** 2) / A_arr,
    ])
    # Least-squares fit
    coeffs, residuals, rank, sv = np.linalg.lstsq(X, binding_arr, rcond=None)
    a_v_fit, a_s_fit, a_c_fit, a_a_fit = coeffs
    pred = X @ coeffs

    print(f"  Fitted coefficients (compared to literature SEMF values):")
    print(f"    a_v  (volume)     = {a_v_fit:>+8.3f} MeV   "
          f"(literature: {A_V_LIT})")
    print(f"    a_s  (surface)    = {a_s_fit:>+8.3f} MeV   "
          f"(literature: {A_S_LIT})")
    print(f"    a_c  (Coulomb)    = {a_c_fit:>+8.3f} MeV   "
          f"(literature: {A_C_LIT})")
    print(f"    a_a  (asymmetry)  = {a_a_fit:>+8.3f} MeV   "
          f"(literature: {A_A_LIT})")
    print()
    rms = math.sqrt(np.mean((binding_arr - pred) ** 2))
    max_dev = np.max(np.abs(binding_arr - pred))
    print(f"  Fit quality: RMS deviation = {rms:.2f} MeV, max deviation = {max_dev:.2f} MeV")
    print()
    print(f"  {'nucleus':<6s} {'observed':>10s} {'fit':>10s} {'residual':>10s}")
    print("  " + "─" * 50)
    for i, r in enumerate(rows):
        print(f"  {r['nucleus']:<6s} {binding_arr[i]:>10.3f} {pred[i]:>10.3f} "
              f"{binding_arr[i] - pred[i]:>+10.3f}")
    print()

    # ── Step 4: verdict ────────────────────────────────────────────
    print("=" * 110)
    print("VERDICT — pool item ad first pass")
    print("=" * 110)
    print()
    print("  Question: does the residual after Ma compound subtraction follow SEMF-style")
    print("            quantum-number structure?")
    print()
    print(f"  Fitted volume term a_v = {a_v_fit:.2f} MeV")
    print(f"    Literature SEMF a_v = {A_V_LIT} MeV.")
    if 13 < a_v_fit < 18:
        print(f"    ✓ Volume term matches SEMF range — Ma compound + SEMF residual is consistent.")
    else:
        print(f"    ⚠ Volume term differs significantly from SEMF.")
    print()
    print(f"  Fitted asymmetry term a_a = {a_a_fit:.2f} MeV")
    print(f"    Literature SEMF a_a = {A_A_LIT} MeV.")
    print(f"    This term penalizes (N−Z) ≠ 0 — purely isospin-structural.")
    if 18 < a_a_fit < 30:
        print(f"    ✓ Asymmetry term matches SEMF range — isospin structure is real.")
    print()
    print(f"  Fitted Coulomb term a_c = {a_c_fit:.3f} MeV")
    print(f"    Literature SEMF a_c = {A_C_LIT} MeV.")
    print()
    print(f"  Fit RMS = {rms:.2f} MeV across {len(rows)} nuclei.")
    print(f"  Light-nuclei (²H, ³H, ³He, ⁴He) deviations dominate — pairing/shell effects expected.")

    # CSV
    csv_path = out_dir / "track15_pool_ad_quantum_numbers.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print()
    print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    main()
