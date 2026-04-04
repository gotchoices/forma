"""
Track 4: Spindle torus and proton anomalous moment

Tests whether a spindle torus (ε > 1) can explain the proton's
anomalous magnetic moment through geometric charge obscuration.

Model:
  - Proton is (1,2) on Ma_p (spin ½, same as electron)
  - Spindle: ε = a/R > 1 → surface self-intersects
  - Hidden region: where 1 + ε cos θ₁ < 0 (surface normal flips)
  - Charge integral restricted to visible surface
  - Magnetic moment from full current loop (not restricted)
  - Target: g_p / g_Dirac = 2.793 enhancement

Two charge models:
  SCALAR: integrand = cos(θ₁) × cos(θ₁) × (1+ε cos θ₁)
          mode shape oscillates → wrong physics
  WvM:    integrand = cos(θ₁) × (1+ε cos θ₁)
          E always outward-normal (circ. polarization) → correct

The WvM model gives the correct direction (spindle reduces Q)
but the geometric ceiling is f → 0.5 as ε → ∞.
"""

import math
import numpy as np
import os

PI  = math.pi
TAU = 2 * PI
ALPHA = 7.2973525693e-3
HBAR  = 1.054571817e-34
C     = 299792458.0
M_P   = 1.67262192369e-27
M_E   = 9.1093837015e-31
LAMBDA_BAR_P = HBAR / (M_P * C)

MU_P_OVER_MU_N = 2.7928473446   # μ_p / μ_N
G_PROTON = 2 * MU_P_OVER_MU_N   # g_p = 5.5857
G_DIRAC  = 2.0
TARGET_F = G_DIRAC / G_PROTON    # 0.3581 — required visible fraction

TARGET_N2 = 2  # proton is (1,2)

NQ = 2048  # quadrature points for integrals


def alpha_formula(eps, s, n2=TARGET_N2):
    q = n2 - s
    if q <= 0:
        return 0
    sn = math.sin(TAU * s)
    if abs(sn) < 1e-15:
        return 0
    mu = math.sqrt(1.0 / (eps * eps) + q * q)
    return mu * sn * sn / (4 * PI * q * q)


def solve_shear(eps, n2=TARGET_N2, target=ALPHA):
    lo, hi = 0.001, 0.499
    for _ in range(80):
        mid = (lo + hi) / 2
        if alpha_formula(eps, mid, n2) > target:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def compute_dimensions(eps, shear):
    qeff = TARGET_N2 - shear
    mu = math.sqrt(1.0 / (eps * eps) + qeff * qeff)
    L_tube = LAMBDA_BAR_P * mu
    L_ring = L_tube / eps
    a = L_tube / TAU
    R = L_ring / TAU
    return {
        'mu': mu, 'qeff': qeff,
        'L_tube_fm': L_tube * 1e15, 'L_ring_fm': L_ring * 1e15,
        'a_fm': a * 1e15, 'R_fm': R * 1e15,
        'area_fm2': L_tube * L_ring * 1e30,
    }


def visible_region(eps):
    """Return (theta_c, is_spindle).

    For ε ≤ 1: entire surface visible, theta_c = π.
    For ε > 1: visible where 1 + ε cos θ₁ ≥ 0,
               i.e. θ₁ ∈ [0, θ_c] ∪ [2π-θ_c, 2π]
               where θ_c = arccos(-1/ε).
    """
    if eps <= 1.0:
        return PI, False
    return math.acos(-1.0 / eps), True


def integrate_charge_scalar(eps, theta_lo, theta_hi):
    """SCALAR charge integral: ∫ cos²(θ₁)·(1+ε cos θ₁) dθ₁.
    Uses mode shape f(θ₁) = cos(θ₁) — oscillates, wrong physics.
    """
    dth = (theta_hi - theta_lo) / NQ
    total = 0.0
    for i in range(NQ):
        th = theta_lo + (i + 0.5) * dth
        w = 1.0 + eps * math.cos(th)
        total += math.cos(th)**2 * w * dth
    return total


def integrate_charge_wvm(eps, theta_lo, theta_hi):
    """WvM charge integral: ∫ cos(θ₁)·(1+ε cos θ₁) dθ₁.
    E is always outward-normal (circular polarization).
    cos(θ₁) is purely the far-field projection factor.
    """
    dth = (theta_hi - theta_lo) / NQ
    total = 0.0
    for i in range(NQ):
        th = theta_lo + (i + 0.5) * dth
        w = 1.0 + eps * math.cos(th)
        total += math.cos(th) * w * dth
    return total


def integrate_abs_area(eps, theta_lo, theta_hi):
    """Physical area: ∫ |1+ε cos θ₁| dθ₁."""
    dth = (theta_hi - theta_lo) / NQ
    total = 0.0
    for i in range(NQ):
        th = theta_lo + (i + 0.5) * dth
        total += abs(1.0 + eps * math.cos(th)) * dth
    return total


def main():
    print("=" * 72)
    print("R47 Track 4: Spindle torus — proton anomalous moment")
    print("=" * 72)
    print(f"  Proton mode: (1, {TARGET_N2})")
    print(f"  g_Dirac = {G_DIRAC}")
    print(f"  g_proton = {G_PROTON:.4f}")
    print(f"  Target visible fraction f = {TARGET_F:.4f}")
    print(f"  ƛ_p = {LAMBDA_BAR_P*1e15:.4f} fm")

    eps_values = np.concatenate([
        np.linspace(0.10, 0.95, 10),
        np.linspace(1.05, 5.0, 20),
        np.linspace(6.0, 50.0, 10),
    ])

    # ── Section 1: WvM charge model (correct physics) ──────────────
    print()
    print("=" * 72)
    print("WvM CHARGE MODEL  (E always outward-normal, σ > 0 everywhere)")
    print("  Integrand: cos(θ₁) × (1 + ε cos θ₁)")
    print("  Q_full = πε  (analytic)")
    print("=" * 72)
    print()
    print(f"{'ε':>6} {'θ_c(°)':>7} {'Q_vis':>9} {'Q_full':>9} "
          f"{'f=Qv/Qf':>9} {'g_eff':>7} {'max_g':>7}")
    print("-" * 62)

    wvm_results = []
    for eps in eps_values:
        theta_c, is_spindle = visible_region(eps)
        Q_vis = 2 * integrate_charge_wvm(eps, 0, theta_c)
        Q_full = PI * eps  # analytic
        f_ch = Q_vis / Q_full if Q_full > 1e-15 else 1.0
        g_eff = G_DIRAC / f_ch if f_ch > 0 else float('inf')

        wvm_results.append({
            'eps': eps, 'theta_c': theta_c, 'is_spindle': is_spindle,
            'Q_vis': Q_vis, 'Q_full': Q_full, 'f': f_ch, 'g_eff': g_eff,
        })

        tc = math.degrees(theta_c)
        print(f"{eps:6.2f} {tc:7.1f} {Q_vis:9.4f} {Q_full:9.4f} "
              f"{f_ch:9.4f} {g_eff:7.3f} {'← MAX' if not is_spindle else ''}")

    print()
    spindle = [r for r in wvm_results if r['is_spindle']]
    if spindle:
        f_min = min(r['f'] for r in spindle)
        print(f"  Smallest f in spindle regime: {f_min:.4f}")
        print(f"  Corresponding max g_eff:      {G_DIRAC/f_min:.3f}")
        print(f"  Asymptotic limit (ε→∞):       f → 0.5000,  g → 4.000")
        print(f"  Target f = {TARGET_F:.4f}  →  g_p = {G_PROTON:.4f}")
        if f_min > TARGET_F:
            print()
            print(f"  *** GEOMETRIC CEILING: f cannot go below 0.5000 ***")
            print(f"  *** Target {TARGET_F:.4f} is unreachable.            ***")
            print(f"  *** Maximum achievable g ≈ 4.0, need {G_PROTON:.3f}   ***")

    # ── Section 2: Scalar model comparison ──────────────────────────
    print()
    print("=" * 72)
    print("SCALAR CHARGE MODEL  (mode shape cos θ₁ — WRONG physics)")
    print("  Integrand: cos²(θ₁) × (1 + ε cos θ₁)")
    print("  Q_full = π  (analytic, ε-independent)")
    print("=" * 72)
    print()
    print(f"{'ε':>6} {'Q_vis':>9} {'Q_full':>9} {'f=Qv/Qf':>9} {'direction':>12}")
    print("-" * 52)

    for eps in [0.50, 0.95, 1.05, 2.0, 5.0, 10.0, 20.0]:
        theta_c, is_spindle = visible_region(eps)
        Q_vis = 2 * integrate_charge_scalar(eps, 0, theta_c)
        Q_full = PI
        f_ch = Q_vis / Q_full
        direction = "WRONG (↑Q)" if f_ch > 1.001 else "ok" if abs(f_ch-1) < 0.001 else "reduces Q"
        print(f"{eps:6.2f} {Q_vis:9.4f} {Q_full:9.4f} {f_ch:9.4f} {direction:>12}")

    print()
    print("  The scalar model has f > 1 in the spindle regime:")
    print("  hiding inner surface INCREASES visible charge (wrong direction).")
    print("  This is because cos²(θ₁) ≥ 0 always, so the hidden region's")
    print("  negative metric weight directly subtracts from Q_full.")

    # ── Section 3: naive current-loop g-factor ──────────────────────
    print()
    print("=" * 72)
    print("NAIVE CURRENT-LOOP g-FACTOR")
    print("  g = μ_dimless / (π·ε) = 2R/ƛ_p")
    print("=" * 72)
    print()
    print(f"{'ε':>6} {'s':>8} {'q_eff':>7} {'μ_dim':>8} "
          f"{'g_loop':>8} {'R(fm)':>8} {'a(fm)':>8}")
    print("-" * 62)

    best_eps, best_g, best_diff = 0, 0, 1e9
    for eps in np.linspace(0.05, 0.95, 50):
        s = solve_shear(eps)
        q = TARGET_N2 - s
        mu = math.sqrt(1/(eps*eps) + q*q)
        g = mu / (PI * eps)
        d = compute_dimensions(eps, s)
        diff = abs(g - G_PROTON)
        if diff < best_diff:
            best_diff, best_eps, best_g = diff, eps, g
        if eps in [0.05] or abs(eps - 0.10) < 0.01 or abs(eps - 0.20) < 0.01 \
           or abs(eps - 0.25) < 0.01 or abs(eps - 0.30) < 0.01 \
           or abs(eps - 0.40) < 0.01 or abs(eps - 0.50) < 0.01 \
           or abs(eps - 0.70) < 0.01 or abs(eps - 0.90) < 0.01:
            marker = " ←" if diff < 0.15 else ""
            print(f"{eps:6.2f} {s:8.5f} {q:7.4f} {mu:8.4f} "
                  f"{g:8.4f} {d['R_fm']:8.4f} {d['a_fm']:8.4f}{marker}")

    # Refine
    lo, hi = 0.05, 0.95
    for _ in range(60):
        mid = (lo + hi) / 2
        s_mid = solve_shear(mid)
        q_mid = TARGET_N2 - s_mid
        mu_mid = math.sqrt(1/(mid*mid) + q_mid*q_mid)
        g_mid = mu_mid / (PI * mid)
        if g_mid > G_PROTON:
            lo = mid
        else:
            hi = mid
    eps_ex = (lo + hi) / 2
    s_ex = solve_shear(eps_ex)
    q_ex = TARGET_N2 - s_ex
    mu_ex = math.sqrt(1/(eps_ex**2) + q_ex**2)
    g_ex = mu_ex / (PI * eps_ex)
    d_ex = compute_dimensions(eps_ex, s_ex)

    print()
    print(f"  Exact match to g_p = {G_PROTON:.6f}:")
    print(f"    ε       = {eps_ex:.6f}")
    print(f"    shear   = {s_ex:.6f}")
    print(f"    q_eff   = {q_ex:.6f}")
    print(f"    μ_dim   = {mu_ex:.6f}")
    print(f"    g_loop  = {g_ex:.6f}")
    print(f"    α check = 1/{1/alpha_formula(eps_ex, s_ex):.3f}")
    print(f"    R       = {d_ex['R_fm']:.4f} fm")
    print(f"    a       = {d_ex['a_fm']:.4f} fm")
    print(f"    R/ƛ_p   = {d_ex['R_fm']/(LAMBDA_BAR_P*1e15):.4f}")
    print()
    R_CH = 0.8414
    print(f"    Proton charge radius (exp): {R_CH} fm")
    print(f"    R/r_ch  = {d_ex['R_fm']/R_CH:.4f}")
    print(f"    a/r_ch  = {d_ex['a_fm']/R_CH:.4f}")
    print()
    print(f"  Caveat: g = μ/(πε) does NOT reproduce g = 2 for the")
    print(f"  electron.  At ε = 0.5:")
    s_e = solve_shear(0.5, n2=2)
    q_e = 2 - s_e
    mu_e = math.sqrt(4 + q_e**2)
    g_e = mu_e / (PI * 0.5)
    print(f"    g_loop(electron) = {g_e:.4f}  (should be ≈ 2.0)")


if __name__ == '__main__':
    main()
