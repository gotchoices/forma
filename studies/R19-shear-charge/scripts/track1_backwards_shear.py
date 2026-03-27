#!/usr/bin/env python3
"""
R19 Track 1: Backwards shear calculation.

Input known α = 1/137.036, solve for the fractional shear s = δ/(2πa)
that produces charge Q = e on the sheared T².

The charge integral on the sheared T²:

    Q = ε₀ E₀ aπ × sin(2πs) / (2 − s)

where E₀ is the field amplitude from total energy = m_e c².

Convention: s = δ/(2πa) is the fractional shear (dimensionless).
This matches R12's shear_frac = δ/L_θ.

The (1,2) mode has q_eff = 2 − s. For s ∉ ℤ, Q ≠ 0.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C

import numpy as np
from scipy.optimize import brentq


def geometry(r):
    """Torus geometry from path constraint ℓ = λ_C on (1,2) knot."""
    R = lambda_C / (2.0 * math.pi * math.sqrt(4 + r**2))
    a = r * R
    return R, a


def E0_from_energy(a, R):
    """
    Field amplitude from total energy = m_e c².

    For a traveling wave E = E₀ cos(Θ + q_eff Φ) on the torus:
    - Time-averaged ⟨cos²⟩ = 1/2
    - E and B contribute equally, so U = ε₀ E₀² × (1/2) × V_torus
    - V_torus = 2π² a² R

    E₀² = m_e c² / (ε₀ π² a² R)
    """
    return math.sqrt(m_e * c**2 / (eps0 * math.pi**2 * a**2 * R))


def charge_from_shear(s, E0, a):
    """
    Charge Q(s) on the sheared T² with fractional shear s.

    Q = ε₀ E₀ a²π × |sin(2πs)| / |2 − s|

    Derivation (Gauss's law on the torus surface):
    - dA = a(R + a cos Θ) dΘ dΦ  (torus surface area element)
    - Q = ε₀ ∫∫ E₀ cos(Θ + q_eff Φ) × a(R + a cos Θ) dΘ dΦ
    - θ-integral: ε₀ E₀ a × [R×0 + a × π cos(q_eff Φ)]
    - φ-integral: ∫₀²π cos(q_eff Φ) dΦ = sin(2πq_eff)/q_eff
    - q_eff = 2 − s, so sin(2π(2−s)) = −sin(2πs)
    - |Q| = ε₀ E₀ a²π |sin(2πs)| / |2 − s|
    """
    q_eff = 2.0 - s
    if abs(q_eff) < 1e-15:
        return eps0 * E0 * a**2 * math.pi * 2 * math.pi
    return eps0 * E0 * a**2 * math.pi * abs(math.sin(2 * math.pi * s)) / abs(q_eff)


def main():
    print("=" * 70)
    print("R19 Track 1: Backwards Shear Calculation")
    print("=" * 70)
    print()

    # ── Section 1: Setup ──────────────────────────────────────
    print("SECTION 1: Physical setup")
    print("-" * 70)
    print()

    r_values = [0.25, 0.50, 1.00, 2.00]

    print(f"Target: Q = e = {e:.6e} C")
    print(f"        α = {alpha:.10f}")
    print(f"        λ_C = {lambda_C:.6e} m")
    print()

    for r in r_values:
        R, a = geometry(r)
        E0 = E0_from_energy(a, R)
        print(f"r = {r:.2f}:  R = {R:.4e} m,  a = {a:.4e} m,  "
              f"E₀ = {E0:.4e} V/m")
    print()

    # ── Section 2: Q(s) profile ───────────────────────────────
    print("SECTION 2: Charge Q(s) as a function of fractional shear")
    print("-" * 70)
    print()

    r = 0.50
    R, a = geometry(r)
    E0 = E0_from_energy(a, R)

    print(f"Using r = {r} (R = {R:.4e} m, a = {a:.4e} m)")
    print(f"E₀ = {E0:.4e} V/m (from total energy = m_e c²)")
    print()

    s_vals = np.linspace(0.001, 0.999, 200)
    Q_vals = np.array([charge_from_shear(s, E0, a) for s in s_vals])

    Q_max = np.max(Q_vals)
    s_at_max = s_vals[np.argmax(Q_vals)]

    print(f"Q_max = {Q_max:.4e} C = {Q_max/e:.4f} e  (at s = {s_at_max:.4f})")
    print()

    print(f"{'s':>8s} | {'δ/a (rad)':>10s} | {'δ/a (deg)':>10s} | "
          f"{'q_eff':>8s} | {'Q/e':>10s}")
    print("-" * 60)
    for s_sample in [0.01, 0.02, 0.05, 0.10, 0.15, 0.20, 0.25,
                     0.30, 0.40, 0.50]:
        Q = charge_from_shear(s_sample, E0, a)
        delta_over_a = 2 * math.pi * s_sample
        print(f"{s_sample:8.3f} | {delta_over_a:10.4f} | "
              f"{math.degrees(delta_over_a):10.2f} | "
              f"{2-s_sample:8.4f} | {Q/e:10.4f}")
    print()

    # ── Section 3: Solve for s that gives Q = e ──────────────
    print("SECTION 3: Required shear for Q = e")
    print("-" * 70)
    print()

    r_scan = np.arange(0.25, 4.01, 0.25)

    print(f"{'r':>6s} | {'Q_max/e':>8s} | {'s_req':>10s} | "
          f"{'δ/a (rad)':>10s} | {'δ/a (deg)':>10s} | {'q_eff':>8s}")
    print("-" * 75)

    for r in r_scan:
        R, a = geometry(r)
        E0 = E0_from_energy(a, R)

        s_fine = np.linspace(0.001, 0.999, 5000)
        Q_arr = np.array([charge_from_shear(s, E0, a) for s in s_fine])
        Q_max_r = np.max(Q_arr)

        if Q_max_r < e:
            print(f"{r:6.2f} | {Q_max_r/e:8.4f} | {'---':>10s} | "
                  f"{'---':>10s} | {'---':>10s} | {'---':>8s}")
            continue

        def f(s):
            return charge_from_shear(s, E0, a) - e

        # Find first solution (smallest s in first lobe)
        s_req = None
        for i in range(len(s_fine) - 1):
            if (Q_arr[i] - e) * (Q_arr[i+1] - e) < 0 and s_fine[i] < 0.5:
                s_req = brentq(f, s_fine[i], s_fine[i+1], xtol=1e-14)
                break

        if s_req is None:
            # Try second lobe
            for i in range(len(s_fine) - 1):
                if (Q_arr[i] - e) * (Q_arr[i+1] - e) < 0:
                    s_req = brentq(f, s_fine[i], s_fine[i+1], xtol=1e-14)
                    break

        if s_req is not None:
            delta_over_a = 2 * math.pi * s_req
            q_eff = 2 - s_req
            print(f"{r:6.2f} | {Q_max_r/e:8.4f} | {s_req:10.6f} | "
                  f"{delta_over_a:10.6f} | "
                  f"{math.degrees(delta_over_a):10.4f} | {q_eff:8.6f}")
        else:
            print(f"{r:6.2f} | {Q_max_r/e:8.4f} | {'???':>10s} | "
                  f"{'???':>10s} | {'???':>10s} | {'???':>8s}")

    print()

    # ── Section 4: Analytical formula ─────────────────────────
    print("SECTION 4: Analytical structure")
    print("-" * 70)
    print()

    print("Setting Q = e and squaring:")
    print()
    print("    e² = ε₀² E₀² a⁴π² sin²(2πs) / (2−s)²")
    print()
    print("With E₀² = m_e c² / (ε₀ π² a² R):")
    print()
    print("    e² = ε₀ m_e c² a² sin²(2πs) / (R (2−s)²)")
    print()
    print("Dividing by 4πε₀ℏc:")
    print()
    print("    α = m_e c a² sin²(2πs) / (4πℏ R (2−s)²)")
    print("      = (a²/(R ƛ_C)) × sin²(2πs) / (4π (2−s)²)")
    print("      = r² / √(r²+4) × sin²(2πs) / (4π (2−s)²)")
    print()
    print("This is a dimensionless equation in s and r alone!")
    print("For each aspect ratio r, it determines the required shear s.")
    print()
    print("Define C(r) = r² / (4π √(r²+4)).  Then α = C(r) × sin²(2πs)/(2−s)².")
    print()

    for r in r_values:
        R, a = geometry(r)
        coeff = r**2 / (4 * math.pi * math.sqrt(r**2 + 4))
        target = alpha / coeff
        max_f = 0.0
        for s_scan in np.linspace(0.001, 0.999, 10000):
            f_val = math.sin(2*math.pi*s_scan)**2 / (2 - s_scan)**2
            if f_val > max_f:
                max_f = f_val
        solvable = "✓" if target <= max_f else "✗ (no solution)"
        print(f"r = {r:.2f}:  C(r) = {coeff:.6f}")
        print(f"          sin²(2πs)/(2−s)² needed = {target:.6f}")
        print(f"          max sin²(2πs)/(2−s)² = {max_f:.4f}  {solvable}")
        print()

    # ── Section 5: Geometric interpretation ───────────────────
    print("SECTION 5: Does the required shear make sense?")
    print("-" * 70)
    print()

    # Find the critical aspect ratio
    r_test = np.linspace(0.1, 4.0, 1000)
    r_crit = None
    for r in r_test:
        R_t, a_t = geometry(r)
        E0_t = E0_from_energy(a_t, R_t)
        Qmax_t = max(charge_from_shear(s, E0_t, a_t)
                     for s in np.linspace(0.001, 0.999, 500))
        if Qmax_t >= e and r_crit is None:
            r_crit = r
            break

    if r_crit is not None:
        print(f"Critical aspect ratio: r_crit ≈ {r_crit:.3f}")
        print(f"  For r < r_crit, no shear can produce Q = e")
        print(f"  For r ≥ r_crit, a solution exists")
        print()

    for r in [1.0, 2.0]:
        R, a = geometry(r)
        E0 = E0_from_energy(a, R)

        s_fine = np.linspace(0.001, 0.999, 5000)
        Q_arr = np.array([charge_from_shear(s, E0, a) for s in s_fine])
        Q_max_check = np.max(Q_arr)

        if Q_max_check < e:
            continue

        def f(s):
            return charge_from_shear(s, E0, a) - e

        s_req = None
        for i in range(len(s_fine) - 1):
            if (Q_arr[i] - e) * (Q_arr[i+1] - e) < 0 and s_fine[i] < 0.5:
                s_req = brentq(f, s_fine[i], s_fine[i+1], xtol=1e-14)
                break

        if s_req is None:
            continue

        delta = s_req * 2 * math.pi * a
        delta_over_a = 2 * math.pi * s_req
        delta_over_R = delta / R
        delta_over_lambdaC = delta / lambda_C
        q_eff = 2 - s_req

        L1 = 2 * math.pi * a
        L2 = 2 * math.pi * R
        cos_angle = s_req * L1 / math.sqrt((s_req * L1)**2 + L2**2)
        lattice_angle = math.degrees(math.acos(cos_angle))
        shear_off_90 = 90 - lattice_angle

        print(f"For r = {r}  (R = {R:.4e} m, a = {a:.4e} m):")
        print(f"  Fractional shear:  s = {s_req:.8f}")
        print(f"  Linear shear:     δ = {delta:.6e} m")
        print(f"  δ/a             = {delta_over_a:.6f} rad "
              f"= {math.degrees(delta_over_a):.4f}°")
        print(f"  δ/R             = {delta_over_R:.6f}")
        print(f"  δ/λ_C           = {delta_over_lambdaC:.8f}")
        print(f"  q_eff           = {q_eff:.8f}")
        print(f"  Q_max/e         = {Q_max_check/e:.4f}")
        print(f"  Lattice angle   = {lattice_angle:.4f}° "
              f"(90° = no shear)")
        print(f"  Deviation from orthogonal: {shear_off_90:.4f}°")
        print()

        recognizable = [
            ("1/137", 1/137),
            ("α", alpha),
            ("√α", math.sqrt(alpha)),
            ("α/(2π)", alpha / (2 * math.pi)),
            ("1/(2π)", 1 / (2 * math.pi)),
            ("1/(4π)", 1 / (4 * math.pi)),
            ("r/2", r / 2),
            ("r/(2π)", r / (2 * math.pi)),
            ("1/q² = 1/4", 0.25),
            ("α/r", alpha / r),
            ("1/6", 1/6),
        ]
        print(f"  Comparison with recognizable values (r = {r}):")
        print(f"  {'Name':>12s} | {'Value':>12s} | {'s/value':>10s} | "
              f"{'value/s':>10s}")
        print("  " + "-" * 55)
        for name, val in recognizable:
            print(f"  {name:>12s} | {val:12.8f} | {s_req/val:10.4f} | "
                  f"{val/s_req:10.4f}")
        print()

    print()

    # ── Section 6: Normalization sensitivity ──────────────────
    print("SECTION 6: Normalization sensitivity")
    print("-" * 70)
    print()
    print("R15 Track 1 found Q_max/e ≈ 8 for the line-source model")
    print("with total energy normalization.  This means the E₀ from")
    print("U = m_e c² gives ~8× too much charge.  The actual coupling")
    print("fraction is κ ≈ α (only fraction α of the energy appears")
    print("as Coulomb field).")
    print()
    print("If the effective field for charge production is E₀_eff = E₀ × √κ")
    print("(with κ = α), then Q → Q × √α.  The required shear changes:")
    print()

    for kappa_label, kappa in [("1 (full E₀)", 1.0),
                                ("1/8² ≈ 2α", 2*alpha),
                                ("α", alpha),
                                ("√α", math.sqrt(alpha))]:
        r_k = 1.0
        R_k, a_k = geometry(r_k)
        E0_k = E0_from_energy(a_k, R_k) * math.sqrt(kappa)

        s_fine_k = np.linspace(0.001, 0.999, 5000)
        Q_arr_k = np.array([charge_from_shear(s, E0_k, a_k) for s in s_fine_k])
        Q_max_k = np.max(Q_arr_k)

        if Q_max_k < e:
            print(f"  κ = {kappa_label:12s}:  Q_max = {Q_max_k/e:.4f}e  "
                  f"(no solution)")
            continue

        def fk(s):
            return charge_from_shear(s, E0_k, a_k) - e

        s_req_k = None
        for i in range(len(s_fine_k) - 1):
            if ((Q_arr_k[i] - e) * (Q_arr_k[i+1] - e) < 0
                    and s_fine_k[i] < 0.5):
                s_req_k = brentq(fk, s_fine_k[i], s_fine_k[i+1], xtol=1e-14)
                break

        if s_req_k is not None:
            delta_a_k = 2 * math.pi * s_req_k
            print(f"  κ = {kappa_label:12s}:  s = {s_req_k:.6f},  "
                  f"δ/a = {delta_a_k:.4f} rad = "
                  f"{math.degrees(delta_a_k):.2f}°,  "
                  f"q_eff = {2-s_req_k:.6f}")
        else:
            print(f"  κ = {kappa_label:12s}:  Q_max = {Q_max_k/e:.4f}e,  "
                  f"no solution in first lobe")

    print()

    # ── Section 7: Verdict ────────────────────────────────────
    print("SECTION 7: Verdict")
    print("-" * 70)
    print()
    print("Summary of Track 1 results:")
    print()

    r = 1.0
    R, a = geometry(r)
    E0_full = E0_from_energy(a, R)

    s_fine_v = np.linspace(0.001, 0.999, 5000)
    Q_arr_v = np.array([charge_from_shear(s, E0_full, a) for s in s_fine_v])
    Q_max_full = np.max(Q_arr_v)

    def f_verdict(s):
        return charge_from_shear(s, E0_full, a) - e

    s_full = None
    if Q_max_full >= e:
        for i in range(len(s_fine_v) - 1):
            if ((Q_arr_v[i] - e) * (Q_arr_v[i+1] - e) < 0
                    and s_fine_v[i] < 0.5):
                s_full = brentq(f_verdict, s_fine_v[i], s_fine_v[i+1],
                                xtol=1e-14)
                break

    if s_full is not None:
        print(f"1. With full E₀ normalization (U = m_e c², r = {r}):")
        print(f"   Q_max/e = {Q_max_full/e:.4f}")
        print(f"   Required shear: s = {s_full:.6f}, "
              f"δ/a = {2*math.pi*s_full:.4f} rad "
              f"= {math.degrees(2*math.pi*s_full):.2f}°")
        print(f"   q_eff = {2-s_full:.6f}")
        print()

    print("2. The analytical formula is:")
    print("       α = C(r) × sin²(2πs) / (2−s)²")
    print("   where C(r) = r² / (4π √(r²+4))")
    print()
    print("   This is a clean dimensionless equation relating α, s, and r.")
    print("   Given α and r, it uniquely determines s.")
    print()
    if r_crit is not None:
        print(f"3. There is a CRITICAL aspect ratio r_crit ≈ {r_crit:.2f}.")
    else:
        print("3. There is a CRITICAL aspect ratio r_crit.")
    print("   For r < r_crit: Q_max < e (no shear produces enough charge).")
    print("   For r ≥ r_crit: a solution exists.")
    print("   This provides a NEW constraint on the aspect ratio.")
    print()
    print("4. For r = 1 (a = R), the required shear is modest (~9° from")
    print("   orthogonal) and the formula produces a clean, well-defined")
    print("   result.  The normalization question (Track 3) must be")
    print("   resolved to confirm whether E₀ from total energy is correct.")


if __name__ == "__main__":
    main()
