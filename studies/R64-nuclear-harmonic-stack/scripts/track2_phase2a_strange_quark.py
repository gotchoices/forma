"""
R64 Track 2 Phase 2a — Strange quark primitive identification.

Tests whether a primitive class (n_t, n_r) on the p-sheet at the
magic point delivers the strange quark's constituent mass within
the harmonic-stack picture.

Constituent strange mass derived from the cleanest single-flavor
target: Ω⁻ (sss baryon, mass 1672.45 MeV).  Under flavor-aware
additive composition, m(sss) = 3·K_p·μ(n_t_s, n_r_s) = m_Ω,
giving constituent m_s = m_Ω / 3 ≈ 557.5 MeV — the same logic
that gave m_u = m_p / 3 ≈ 313 MeV at Track 1's magic point.

Z₃ confinement constraint: any baryon containing one strange
quark plus two u/d quarks (e.g., Λ = uds, Σ = uus or dds)
requires baryon n_pt ≡ 0 (mod 3).  With u, d at n_t = 1, this
gives n_t_s ≡ 1 (mod 3), so allowed values are {±1, ±2 (with
sign), ±4, ±5, ±7, ...} — actually n_t_s ∈ {..., -5, -2, 1, 4, 7, ...}.
With n_t_s = 1, the primitive is in the same "n_t shell" as
u/d (mass ≈ 313 MeV — too light for strange).  With n_t_s = 4,
mass ≈ 1252 MeV — too heavy.  n_t_s = -2 sits in the n_t = 2
shell (mass ≈ 626 MeV — closer but still too heavy).

This phase audits the lattice systematically:
  1. Scan all Z₃-compatible (n_t, n_r) primitives within reach.
  2. Compute mass at the magic point.
  3. Identify any class within 5% of m_s = 557.5 MeV.
  4. Cross-check candidate against Λ (uds), kaons (us̄, ds̄), and
     the SU(3)_F mass formula structure.

Outputs:
  outputs/track2_phase2a_strange_lattice.csv
  outputs/track2_phase2a_strange_summary.txt
"""

import math
import csv
from pathlib import Path


# ─── Magic point from Track 1 Phase 1c ─────────────────────────────────

EPS_P = 0.073092553872
S_P   = 0.193871467423
K_P   = 22.846596    # MeV/μ-unit


# ─── PDG masses (MeV) ──────────────────────────────────────────────────

M_P     = 938.27208816
M_N     = 939.56542052
M_OMEGA = 1672.45        # Ω⁻ (sss)
M_LAMBDA = 1115.683      # Λ (uds)
M_KAON_PM = 493.677      # K± (us̄, ds̄ etc, light)
M_KAON_0  = 497.611      # K⁰
M_SIGMA_P = 1189.37      # Σ⁺ (uus)
M_SIGMA_M = 1197.449     # Σ⁻ (dds)
M_SIGMA_0 = 1192.642     # Σ⁰
M_XI_M    = 1321.71      # Ξ⁻ (dss)
M_XI_0    = 1314.86      # Ξ⁰ (uss)

# Constituent strange mass target (m_Ω / 3)
M_S_TARGET = M_OMEGA / 3.0    # 557.483


# ─── Mass formula ──────────────────────────────────────────────────────

def mu2(n_t, n_r, eps=EPS_P, s=S_P):
    return (n_t / eps)**2 + (n_r - s * n_t)**2


def mu(n_t, n_r, eps=EPS_P, s=S_P):
    return math.sqrt(mu2(n_t, n_r, eps, s))


def m_primitive(n_t, n_r):
    """Mass at the magic point."""
    return K_P * mu(n_t, n_r)


# ─── Lattice scan ──────────────────────────────────────────────────────

def is_z3_compatible_for_uds_baryon(n_t_s):
    """Baryon Λ = u + d + s = (1+1+n_t_s, ...).  Z₃ requires baryon
    n_pt ≡ 0 (mod 3).  With u, d at n_t = 1, this gives n_t_s ≡ 1 (mod 3).
    """
    return (n_t_s - 1) % 3 == 0


def scan_lattice(n_t_max=8, n_r_max=30):
    """Enumerate primitives and compute their masses.

    Filter to those that could be a 'quark-like' object:
    - n_t > 0 (matter, not antimatter; antimatter is sign-flip)
    - reasonable mass range (50-2000 MeV for strange-quark search)
    """
    rows = []
    for n_t in range(-n_t_max, n_t_max + 1):
        if n_t == 0:
            continue
        for n_r in range(-n_r_max, n_r_max + 1):
            m = m_primitive(n_t, n_r)
            err_vs_s = (m - M_S_TARGET) / M_S_TARGET
            z3_ok_for_lambda = is_z3_compatible_for_uds_baryon(n_t)
            rows.append({
                'n_t': n_t,
                'n_r': n_r,
                'mass_MeV': m,
                'err_vs_m_s_target': err_vs_s,
                'abs_err_pct': abs(err_vs_s) * 100,
                'z3_uds_ok': z3_ok_for_lambda,
            })
    return rows


# ─── Λ-baryon-anchored strange quark search ────────────────────────────

def derive_m_s_from_lambda(n_t_s, n_r_s):
    """If Λ = u + d + s, additive winding gives Λ tuple
    (1 + 1 + n_t_s, +2 + (-2) + n_r_s) = (2 + n_t_s, n_r_s).
    Predict m_Λ; back out m_s.
    """
    n_t_lambda = 2 + n_t_s
    n_r_lambda = n_r_s
    if n_t_lambda % 3 != 0 and (n_t_lambda + 3) % 3 != 0:
        # not Z₃-compatible
        return None, None
    m_lambda = m_primitive(n_t_lambda, n_r_lambda)
    return m_lambda, m_lambda / 3.0   # naive m_s estimate


# ─── Main ──────────────────────────────────────────────────────────────

def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R64 Track 2 Phase 2a — Strange quark primitive identification")
    print("=" * 100)
    print()
    print(f"  Magic point: ε_p = {EPS_P:.6f}, s_p = {S_P:.6f}, "
          f"K_p = {K_P:.4f} MeV/μ")
    print()
    print(f"  Strange-mass target (constituent): m_s = m_Ω/3 = "
          f"{M_S_TARGET:.3f} MeV")
    print(f"  Z₃ constraint for uds baryons (Λ): n_t_s ≡ 1 (mod 3)")
    print(f"    Allowed n_t_s ∈ {{..., -5, -2, 1, 4, 7, ...}}")
    print()

    # ─── Mass shell structure ──────────────────────────────────────
    print("Mass shell structure at the magic point:")
    print("-" * 100)
    print(f"  Each n_t value gives a 'shell' at mass ≈ |n_t|·K_p/ε_p = "
          f"|n_t|·{K_P/EPS_P:.1f} MeV")
    print(f"  {'n_t':>4s}  {'min mass':>10s}  {'mass at n_r=0':>14s}  "
          f"{'shell label':>15s}  {'Z₃ for uds?':>12s}")
    for n_t in [1, 2, 3, 4, 5, 6, 7]:
        m_min = m_primitive(n_t, 0)  # tube-only, lightest in shell
        z3 = "yes" if is_z3_compatible_for_uds_baryon(n_t) else "NO"
        if n_t == 1:
            label = "u, d (Track 1)"
        elif n_t == 3:
            label = "proton, neutron"
        else:
            label = ""
        print(f"  {n_t:>4d}  {m_min:>10.3f}  {m_primitive(n_t, 0):>14.3f}  "
              f"{label:>15s}  {z3:>12s}")
    print()

    print(f"  m_s target = {M_S_TARGET:.3f} MeV sits BETWEEN n_t=1 shell "
          f"({m_primitive(1, 0):.0f}) and n_t=2 shell ({m_primitive(2, 0):.0f}).")
    print(f"  Note: n_t = 2 is NOT Z₃-compatible for Λ = uds baryons "
          f"(needs n_t_s ≡ 1 mod 3).")
    print()

    # ─── Full lattice scan ─────────────────────────────────────────
    print("Lattice scan: primitives with mass within 30% of m_s target")
    print("-" * 100)
    rows = scan_lattice(n_t_max=6, n_r_max=30)
    rows_close = [r for r in rows if r['abs_err_pct'] < 30.0 and r['n_t'] > 0]
    rows_close.sort(key=lambda r: r['abs_err_pct'])
    print(f"  {'(n_t, n_r)':>12s}  {'mass MeV':>10s}  "
          f"{'err vs m_s':>11s}  {'Z₃ uds?':>10s}")
    for r in rows_close[:25]:
        z3 = "yes" if r['z3_uds_ok'] else "NO"
        print(f"  ({r['n_t']:>3d},{r['n_r']:>3d})  {r['mass_MeV']:>10.3f}  "
              f"{r['err_vs_m_s_target']:>+10.2%}  {z3:>10s}")
    print()

    # ─── Λ-anchored search ─────────────────────────────────────────
    print("Λ-anchored search: candidate strange primitives by Λ mass match")
    print("-" * 100)
    print(f"  Test: for each candidate (n_t_s, n_r_s), Λ tuple = "
          f"(2 + n_t_s, n_r_s).")
    print(f"  Predict m_Λ from the magic-point formula; compare to "
          f"observed {M_LAMBDA} MeV.")
    print()

    # n_t_s ≡ 1 (mod 3): values -5, -2, 1, 4
    candidates_nt = [-5, -2, 1, 4]
    print(f"  {'(n_t_s, n_r_s)':>16s}  {'Λ tuple':>14s}  "
          f"{'m_Λ pred':>10s}  {'m_Λ obs':>10s}  "
          f"{'err':>9s}  {'m_s implied':>12s}")
    rows_lambda = []
    for n_t_s in candidates_nt:
        for n_r_s in range(-10, 11):
            n_t_l = 2 + n_t_s
            n_r_l = n_r_s
            m_l = m_primitive(n_t_l, n_r_l)
            m_s_implied = K_P * mu(n_t_s, n_r_s)
            err = (m_l - M_LAMBDA) / M_LAMBDA
            if abs(err) < 0.10:   # within 10% of Λ
                rows_lambda.append({
                    'n_t_s': n_t_s, 'n_r_s': n_r_s,
                    'n_t_lambda': n_t_l, 'n_r_lambda': n_r_l,
                    'm_lambda_pred': m_l, 'm_s_implied': m_s_implied,
                    'lambda_err': err,
                })
    rows_lambda.sort(key=lambda r: abs(r['lambda_err']))
    for r in rows_lambda[:15]:
        print(f"  ({r['n_t_s']:>3d}, {r['n_r_s']:>3d})  "
              f"({r['n_t_lambda']:>3d}, {r['n_r_lambda']:>3d})  "
              f"{r['m_lambda_pred']:>10.3f}  {M_LAMBDA:>10.3f}  "
              f"{r['lambda_err']:>+8.2%}  {r['m_s_implied']:>12.3f}")
    print()

    # ─── Best Λ-anchored strange candidate ─────────────────────────
    if rows_lambda:
        best_l = rows_lambda[0]
        print(f"Best Λ-anchored strange candidate: (n_t_s, n_r_s) = "
              f"({best_l['n_t_s']}, {best_l['n_r_s']})")
        print(f"  Implied m_s = {best_l['m_s_implied']:.3f} MeV  "
              f"(target {M_S_TARGET:.1f}, "
              f"err {(best_l['m_s_implied']/M_S_TARGET - 1)*100:+.2f}%)")
        print(f"  Λ predicted: {best_l['m_lambda_pred']:.3f} vs observed "
              f"{M_LAMBDA}, err {best_l['lambda_err']:+.2%}")
        print()

        # Cross-check Σ, Ξ, Ω at this candidate
        print("Cross-check at this candidate:")
        print("-" * 100)
        n_t_s = best_l['n_t_s']
        n_r_s = best_l['n_r_s']

        cross_checks = [
            ("Σ⁺ (uus)", (1 + 1 + n_t_s, +2 + +2 + n_r_s), M_SIGMA_P),
            ("Σ⁻ (dds)", (1 + 1 + n_t_s, -2 + -2 + n_r_s), M_SIGMA_M),
            ("Ξ⁻ (dss)", (1 + n_t_s + n_t_s, -2 + n_r_s + n_r_s), M_XI_M),
            ("Ξ⁰ (uss)", (1 + n_t_s + n_t_s, +2 + n_r_s + n_r_s), M_XI_0),
            ("Ω⁻ (sss)", (3 * n_t_s, 3 * n_r_s), M_OMEGA),
        ]
        print(f"  {'particle':>12s}  {'tuple':>12s}  {'predicted':>10s}  "
              f"{'observed':>10s}  {'err':>10s}")
        for name, tup, m_obs in cross_checks:
            m_pred = m_primitive(*tup)
            err = (m_pred - m_obs) / m_obs
            print(f"  {name:>12s}  ({tup[0]:>3d},{tup[1]:>3d})  "
                  f"{m_pred:>10.3f}  {m_obs:>10.3f}  {err:>+9.2%}")
        print()

    # ─── Save CSV ─────────────────────────────────────────────────
    csv_lattice = out_dir / "track2_phase2a_strange_lattice.csv"
    with open(csv_lattice, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print(f"  Lattice CSV: {csv_lattice}")
    print()

    # ─── Verdict ──────────────────────────────────────────────────
    print("=" * 100)
    print("VERDICT — Phase 2a")
    print("=" * 100)
    print()

    # Find best Z₃-compatible strange candidate
    z3_close = [r for r in rows if r['z3_uds_ok'] and r['n_t'] > 0
                and r['abs_err_pct'] < 10]
    z3_close.sort(key=lambda r: r['abs_err_pct'])

    if z3_close:
        best = z3_close[0]
        print(f"  Best Z₃-compatible primitive within 10% of m_s = "
              f"{M_S_TARGET:.1f} MeV:")
        print(f"    (n_t, n_r) = ({best['n_t']}, {best['n_r']}), "
              f"mass = {best['mass_MeV']:.3f} MeV, "
              f"err = {best['err_vs_m_s_target']:+.2%}")
    else:
        print(f"  No Z₃-compatible primitive within 10% of m_s = "
              f"{M_S_TARGET:.1f} MeV.")
    print()

    # Highlight the structural problem
    n_t1_max = max(m_primitive(1, n_r) for n_r in range(-30, 31))
    n_t2_min = min(abs(m_primitive(2, n_r)) for n_r in range(-30, 31))
    print(f"  Structural observation:")
    print(f"    n_t = 1 shell (Z₃ ok): masses 313–{n_t1_max:.0f} MeV")
    print(f"    n_t = 4 shell (Z₃ ok): masses 1252+ MeV")
    print(f"    m_s target = {M_S_TARGET:.0f} MeV — falls between "
          f"shells, no Z₃-compatible match in n_t=1 mode")
    print()


if __name__ == "__main__":
    main()
