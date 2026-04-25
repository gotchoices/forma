"""
R64 Track 1 Phase 1c — α-precision audit of the magic point.

Phase 1b located the magic point at ε_p ≈ 0.073 by sweeping at 600 points
and finding the ε_p where deuteron binding crosses observed.  At that
precision the result is suspiciously close to 10·α = 10/137.036 ≈ 0.07297.

Phase 1c refines the magic-point search to high precision (~10⁻¹²) using
2D Newton iteration on the joint (ε_p, s_p) system, with PDG-precision
input masses, and tests whether the resulting ε_p coincides with
candidate α-relations:

  10·α            = 0.072974...
  10/α            = 1370.36...
  α/π             = 2.323e-3
  α²              = 5.32e-5
  100·α/(2π)      = 1.161e-2
  1/(10·137.036)  = same as 10·α/137 ≈ 7.29e-4

If ε_p = 10·α exactly (to part-per-thousand or better), this is a major
structural finding: the p-sheet aspect ratio is α-pinned, and Q134's
ground rules update.  If it's just close, the coincidence is filed away
and we move on.

Output: outputs/track1_phase1c_alpha_check.csv
"""

import math
import csv
from pathlib import Path


# ─── PDG-precision input masses (MeV) ──────────────────────────────────

# Source: PDG 2022 / CODATA 2018
M_P_OBS  = 938.27208816    # MeV
M_N_OBS  = 939.56542052    # MeV
M_D_OBS  = 1875.61294257   # MeV (deuteron, ²H)
B_D_OBS  = (M_P_OBS + M_N_OBS) - M_D_OBS   # = 2.22456611 MeV

# CODATA 2018 fine-structure constant
ALPHA_INV = 137.035999084
ALPHA     = 1.0 / ALPHA_INV


# ─── Mass formula ──────────────────────────────────────────────────────

def mu2(n_t, n_r, eps, s):
    return (n_t / eps)**2 + (n_r - s * n_t)**2


def mu(n_t, n_r, eps, s):
    return math.sqrt(mu2(n_t, n_r, eps, s))


# ─── Joint Newton solver in (ε, s) ─────────────────────────────────────

def residuals(eps, s):
    """Two residuals: mass ratio and deuteron binding.

    R1 = μ²(3, -2)/μ²(3, +2) - (m_n/m_p)²
    R2 = m_d_predicted - m_d_observed
       = K_p · μ(6, 0) - m_d_obs
       where K_p = m_p_obs / μ(3, +2)
    """
    mu2_p = mu2(3, +2, eps, s)
    mu2_n = mu2(3, -2, eps, s)
    R2_obs = (M_N_OBS / M_P_OBS)**2

    R1 = mu2_n / mu2_p - R2_obs

    K_p = M_P_OBS / math.sqrt(mu2_p)
    m_d_pred = K_p * math.sqrt(mu2(6, 0, eps, s))
    R2 = m_d_pred - M_D_OBS

    return R1, R2


def jacobian(eps, s, h_eps=1e-8, h_s=1e-10):
    """Numerical Jacobian for the (R1, R2) system."""
    R1_0, R2_0 = residuals(eps, s)

    R1_e, R2_e = residuals(eps + h_eps, s)
    dR1_de = (R1_e - R1_0) / h_eps
    dR2_de = (R2_e - R2_0) / h_eps

    R1_s, R2_s = residuals(eps, s + h_s)
    dR1_ds = (R1_s - R1_0) / h_s
    dR2_ds = (R2_s - R2_0) / h_s

    return [[dR1_de, dR1_ds], [dR2_de, dR2_ds]]


def newton_solve(eps0=0.073, s0=0.194, max_iter=100, tol=1e-14):
    """2D Newton on (ε, s) for joint mass-ratio + deuteron-binding match."""
    eps, s = eps0, s0
    history = [(eps, s)]
    for k in range(max_iter):
        R1, R2 = residuals(eps, s)
        if abs(R1) < tol and abs(R2) < tol:
            break
        J = jacobian(eps, s)
        det = J[0][0] * J[1][1] - J[0][1] * J[1][0]
        if abs(det) < 1e-30:
            break
        d_eps = (J[1][1] * R1 - J[0][1] * R2) / det
        d_s   = (J[0][0] * R2 - J[1][0] * R1) / det
        eps_new = eps - d_eps
        s_new   = s - d_s
        history.append((eps_new, s_new))
        if abs(eps_new - eps) < tol * abs(eps) and abs(s_new - s) < tol * abs(s):
            eps, s = eps_new, s_new
            break
        eps, s = eps_new, s_new
    return eps, s, history


# ─── α-relation candidates ─────────────────────────────────────────────

def alpha_candidates():
    """Various natural α-related quantities at the right magnitude."""
    return [
        ("10·α",                   10 * ALPHA,                  "linear in α"),
        ("α^(1/2)",                math.sqrt(ALPHA),            "square-root"),
        ("α·π",                    ALPHA * math.pi,             "α/π up by π²"),
        ("α/(2·π)·137",            ALPHA / (2 * math.pi) * 137, "structurally awkward"),
        ("1/(10/α)",               ALPHA / 10,                  "α/10 (way off)"),
        ("(α·137.036)/10·1.001",   1/137.036/10 * 1.001,        "10·α with tiny shift"),
        ("10/137",                 10.0/137.0,                  "α with α^(-1) rounded to 137"),
        ("α^(1/3)",                ALPHA**(1.0/3.0),            "cube-root"),
        ("π·α",                    math.pi * ALPHA,             "α scaled by π"),
        ("α/sin(1)",               ALPHA / math.sin(1),         "control / spurious"),
    ]


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R64 Track 1 Phase 1c — α-precision audit of the magic point")
    print("=" * 100)
    print()
    print(f"  Input masses (PDG/CODATA):")
    print(f"    m_p  = {M_P_OBS:.8f} MeV")
    print(f"    m_n  = {M_N_OBS:.8f} MeV")
    print(f"    m_d  = {M_D_OBS:.8f} MeV")
    print(f"    B(²H) = {B_D_OBS:.8f} MeV")
    print(f"    α^-1 = {ALPHA_INV:.9f}")
    print(f"    α    = {ALPHA:.12e}")
    print(f"    10·α = {10*ALPHA:.12e}")
    print()

    # ─── Joint Newton solve ────────────────────────────────────────
    print("Joint Newton solve on (ε_p, s_p):")
    print("-" * 100)

    eps_star, s_star, hist = newton_solve(eps0=0.073, s0=0.194)
    R1, R2 = residuals(eps_star, s_star)

    print(f"  Iterations: {len(hist) - 1}")
    print(f"  Final residuals: |R1| = {abs(R1):.3e}, |R2| = {abs(R2):.3e}")
    print(f"  ε_p (12 sig figs)   = {eps_star:.12f}")
    print(f"  s_p (12 sig figs)   = {s_star:.12f}")
    print()

    K_p = M_P_OBS / math.sqrt(mu2(3, +2, eps_star, s_star))
    m_p_pred = K_p * mu(3, +2, eps_star, s_star)
    m_n_pred = K_p * mu(3, -2, eps_star, s_star)
    m_d_pred = K_p * mu(6,  0, eps_star, s_star)
    print(f"  K_p (MeV per μ-unit) = {K_p:.6f}")
    print(f"  Sanity check:")
    print(f"    m_p predicted = {m_p_pred:.8f}  (input {M_P_OBS})")
    print(f"    m_n predicted = {m_n_pred:.8f}  (input {M_N_OBS})")
    print(f"    m_d predicted = {m_d_pred:.8f}  (input {M_D_OBS})")
    print()

    # ─── Compare ε_p to α candidates ──────────────────────────────
    print("Comparing ε_p to candidate α-relations:")
    print("-" * 100)
    print(f"  {'candidate':25s}  {'value':>16s}  {'ε_p − cand':>14s}  "
          f"{'rel diff':>11s}")
    print("  " + "─" * 80)
    rows = []
    for label, val, note in alpha_candidates():
        diff = eps_star - val
        rel = diff / val if val != 0 else float('inf')
        flag = ""
        if abs(rel) < 1e-3:
            flag = "  ←★ within 0.1%"
        elif abs(rel) < 1e-2:
            flag = "  ← within 1%"
        print(f"  {label:25s}  {val:>16.12e}  {diff:>+14.3e}  {rel:>+10.2%}{flag}")
        rows.append({
            'candidate': label, 'value': val, 'eps_minus_cand': diff,
            'rel_diff': rel, 'note': note,
        })
    print()

    # ─── Compare s_p to α candidates ──────────────────────────────
    print("Comparing s_p to candidate α-relations:")
    print("-" * 100)
    print(f"  {'candidate':25s}  {'value':>16s}  {'s_p − cand':>14s}  "
          f"{'rel diff':>11s}")
    print("  " + "─" * 80)
    s_candidates = [
        ("α·26.6",                 ALPHA * 26.6,                  "near-fit at 26.6×α"),
        ("(s_p·m_p)/m_n − 0",      0.194,                         "self-consistency"),
        ("α^(1/2)·26.6",           math.sqrt(ALPHA) * 26.6,       "sqrt scaling"),
        ("π/16",                   math.pi / 16,                  "rational π fraction"),
        ("π/16.2",                 math.pi / 16.2,                "near π/16"),
        ("1/(10·α)·0.0014",        0.0014 / (10 * ALPHA),         "control"),
        ("α^(2/3)·1.5",            ALPHA**(2/3) * 1.5,            "α^(2/3)"),
        ("0.20",                   0.20,                          "round number"),
        ("3·α^(1/2)",              3 * math.sqrt(ALPHA),          "3·sqrt(α)"),
    ]
    for label, val, note in s_candidates:
        diff = s_star - val
        rel = diff / val if val != 0 else float('inf')
        flag = ""
        if abs(rel) < 1e-3:
            flag = "  ←★ within 0.1%"
        elif abs(rel) < 1e-2:
            flag = "  ← within 1%"
        print(f"  {label:25s}  {val:>16.12e}  {diff:>+14.3e}  {rel:>+10.2%}{flag}")
    print()

    # ─── Special focused test: is ε_p = 10α exactly? ─────────────
    print("=" * 100)
    print("Focused test: ε_p vs 10·α to high precision")
    print("=" * 100)
    print()
    print(f"  ε_p (Newton)  = {eps_star:.15f}")
    print(f"  10·α (CODATA) = {10*ALPHA:.15f}")
    print(f"  Δ (absolute)  = {eps_star - 10*ALPHA:+.6e}")
    print(f"  Δ (relative)  = {(eps_star - 10*ALPHA)/(10*ALPHA):+.6e}  "
          f"({(eps_star - 10*ALPHA)/(10*ALPHA)*100:+.4f}%)")
    print()
    if abs((eps_star - 10*ALPHA)/(10*ALPHA)) < 1e-4:
        print("  → ε_p = 10·α to better than 0.01% — ALMOST CERTAINLY STRUCTURAL")
    elif abs((eps_star - 10*ALPHA)/(10*ALPHA)) < 1e-3:
        print("  → ε_p = 10·α to within 0.1% — likely structural, worth pursuing")
    elif abs((eps_star - 10*ALPHA)/(10*ALPHA)) < 1e-2:
        print("  → ε_p ≈ 10·α to within 1% — suggestive but not pinning")
    else:
        print("  → ε_p ≠ 10·α at meaningful precision — likely coincidence")
    print()

    # ─── Save CSV ─────────────────────────────────────────────────
    csv_path = out_dir / "track1_phase1c_alpha_check.csv"
    with open(csv_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['quantity', 'value'])
        w.writerow(['eps_p_magic',          f'{eps_star:.15f}'])
        w.writerow(['s_p_magic',            f'{s_star:.15f}'])
        w.writerow(['K_p_magic_MeV',        f'{K_p:.10f}'])
        w.writerow(['ten_alpha',            f'{10*ALPHA:.15f}'])
        w.writerow(['eps_p_minus_10_alpha', f'{eps_star - 10*ALPHA:.6e}'])
        w.writerow(['rel_diff_pct',
                   f'{(eps_star - 10*ALPHA)/(10*ALPHA)*100:.6f}'])

    print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    main()
