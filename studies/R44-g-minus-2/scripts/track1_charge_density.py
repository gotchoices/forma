#!/usr/bin/env python3
"""
R44 Track 1: Charge density and magnetic moment on the sheared torus.

Computes:
  1. The surface charge density σ(θ₁, θ₂) from the R19 shear mechanism
  2. Verifies ∫σ dA = e
  3. Maps the charge distribution — where is charge concentrated?
  4. Computes the magnetic dipole moment from the actual charge distribution
  5. Computes the magnetic dipole moment from a uniform charge distribution
  6. Extracts the ratio μ_actual / μ_uniform — the charge-mass separation
     correction that could produce g − 2 ≈ α/π

PHYSICS
=======
The R19 shear mechanism gives a surface charge density on the embedded torus:

    σ(θ₁, θ₂) = ε₀ E₀ cos(θ₁ + q_eff θ₂)

where θ₁ is the physical tube angle, θ₂ is the ring angle, and
q_eff = 2 − s (the effective winding number with shear s).

The total charge Q = ∫σ dA = e integrates to a non-zero value because
the torus area element dA = a(R + a cos θ₁) dθ₁ dθ₂ weights the inner
and outer edges differently, and q_eff is non-integer (due to shear).

The magnetic moment μ_z from a surface current K = σ c v̂ on the
embedded torus is:

    μ_z = (c/2) ∫ σ × 2ρ²/|v_unnorm| × dA

where ρ = R + a cos θ₁ is the distance from the symmetry axis.

The ratio μ_actual / μ_uniform measures how the non-uniform charge
distribution shifts the moment relative to the energy-weighted baseline.
This ratio − 1 is the candidate for the anomalous moment correction.
"""

import sys
import os
import math
import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C


def geometry(r, s):
    """Torus geometry from Compton constraint on sheared (1,2) geodesic."""
    L_flat = lambda_C
    denom = math.sqrt(r**2 * (1 + 2*s)**2 + 4)
    R = L_flat / (2 * math.pi * denom)
    a = r * R
    return R, a


def E0_from_energy(a, R):
    """Field amplitude from total mode energy = m_e c²."""
    return math.sqrt(m_e * c**2 / (eps0 * math.pi**2 * a**2 * R))


def alpha_formula(r, s):
    """R19 α formula: α = r² sin²(2πs) / (4π(2−s)² √(r²(1+2s)²+4))."""
    sn = math.sin(2 * math.pi * s)
    q = 2.0 - s
    if abs(sn) < 1e-15 or abs(q) < 1e-15:
        return 0.0
    d = math.sqrt(r**2 * (1 + 2*s)**2 + 4)
    return r**2 * sn**2 / (4 * math.pi * q**2 * d)


def solve_shear(r):
    """Solve α(r, s) = 1/137.036 for s at given r."""
    def f(s):
        return alpha_formula(r, s) - alpha

    ss = np.linspace(0.001, 0.499, 10000)
    fs = np.array([f(si) for si in ss])
    for i in range(len(fs) - 1):
        if fs[i] * fs[i+1] < 0:
            return brentq(f, ss[i], ss[i+1], xtol=1e-14)
    return None


def main():
    print("=" * 72)
    print("R44 Track 1: Charge Density and Magnetic Moment")
    print("=" * 72)
    print()

    N = 500  # grid resolution per angle

    theta1 = np.linspace(0, 2*np.pi, N, endpoint=False)
    theta2 = np.linspace(0, 2*np.pi, N, endpoint=False)
    dth1 = 2 * np.pi / N
    dth2 = 2 * np.pi / N
    TH1, TH2 = np.meshgrid(theta1, theta2, indexing='ij')

    r_values = [0.54, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0]

    # ── Section 1: Charge density verification ────────────────
    print("SECTION 1: Charge density and total charge verification")
    print("-" * 72)
    print()
    print(f"Grid: {N}×{N} = {N*N} points")
    print(f"Target charge: e = {e:.6e} C")
    print(f"α = {alpha:.10f} = 1/{1/alpha:.3f}")
    print()

    print(f"{'r':>6s} | {'s':>10s} | {'q_eff':>10s} | "
          f"{'Q_num/e':>10s} | {'Q_analytic/e':>12s} | {'error':>10s}")
    print("-" * 72)

    results = []

    for r in r_values:
        s = solve_shear(r)
        if s is None:
            print(f"{r:6.2f} | {'no solution':>10s}")
            continue

        R, a = geometry(r, s)
        E0 = E0_from_energy(a, R)
        q_eff = 2.0 - s

        rho = R + a * np.cos(TH1)  # distance from z-axis

        sigma = eps0 * E0 * np.cos(TH1 + q_eff * TH2)
        dA = a * rho * dth1 * dth2

        Q_num = np.sum(sigma * dA)
        Q_analytic = -eps0 * E0 * a**2 * math.pi * math.sin(2*math.pi*s) / q_eff

        err = abs(Q_num / Q_analytic - 1)

        print(f"{r:6.2f} | {s:10.6f} | {q_eff:10.6f} | "
              f"{Q_num/e:10.6f} | {Q_analytic/e:12.6f} | {err:10.2e}")

        results.append((r, s, R, a, E0, q_eff, Q_num, Q_analytic))

    print()
    print("(Q should be ≈ ±e.  Sign depends on convention.)")
    print()

    # ── Section 2: Charge distribution map ────────────────────
    print()
    print("SECTION 2: Charge concentration — where does charge live?")
    print("-" * 72)
    print()

    print("Integrating σ×dA over θ₂ to get the effective charge per")
    print("unit tube angle.  The θ₂ integral gives:")
    print("  ∫σ dA_θ₂ ∝ cos(θ₁ − πs) × ρ")
    print()
    print("Charge peaks at θ₁ ≈ πs (outer equator for small s).")
    print()

    for r, s, R, a, E0, q_eff, Q_num, Q_analytic in results[:4]:
        print(f"r = {r:.2f}, s = {s:.6f}:")

        rho_1d = R + a * np.cos(theta1)
        q_per_angle = np.zeros(N)
        for i in range(N):
            integrand = eps0 * E0 * np.cos(theta1[i] + q_eff * theta2) * a * rho_1d[i]
            q_per_angle[i] = np.sum(integrand) * dth2

        i_max = np.argmax(q_per_angle)
        i_min = np.argmin(q_per_angle)

        print(f"  Peak +Q at θ₁ = {math.degrees(theta1[i_max]):6.1f}° "
              f"(πs = {math.degrees(math.pi*s):6.2f}°)")
        print(f"  Peak −Q at θ₁ = {math.degrees(theta1[i_min]):6.1f}°")
        print(f"  Ratio |max/min| = {abs(q_per_angle[i_max]/q_per_angle[i_min]):.4f}")

        rho_at_max = R + a * math.cos(theta1[i_max])
        rho_at_min = R + a * math.cos(theta1[i_min])
        print(f"  ρ at +Q peak: {rho_at_max/R:.4f} R  (ρ/R = 1 + r cos θ₁)")
        print(f"  ρ at −Q peak: {rho_at_min/R:.4f} R")

        charge_pos = np.sum(q_per_angle[q_per_angle > 0]) * dth1
        charge_neg = np.sum(q_per_angle[q_per_angle < 0]) * dth1
        print(f"  Total +Q contribution: {charge_pos/e:+.6f} e")
        print(f"  Total −Q contribution: {charge_neg/e:+.6f} e")
        print(f"  Net: {(charge_pos+charge_neg)/e:+.6f} e")
        print()

    # ── Section 3: Magnetic moment computation ────────────────
    print()
    print("SECTION 3: Magnetic dipole moment — charge-weighted vs uniform")
    print("=" * 72)
    print()
    print("The z-component of r×K simplifies to 2ρ²/|v_unnorm| by")
    print("azimuthal symmetry (the cross terms cancel).")
    print()
    print("  μ_actual  = (c/2) ∫∫ σ_actual × 2ρ²/|v| × dA")
    print("  μ_uniform = (c/2) ∫∫ σ_uniform × 2ρ²/|v| × dA")
    print()
    print("  ratio = μ_actual / μ_uniform")
    print("  target: ratio − 1 = α/(2π) = {:.8f}".format(alpha/(2*math.pi)))
    print()

    print(f"{'r':>6s} | {'s':>10s} | {'μ_act (A·m²)':>14s} | "
          f"{'μ_unif (A·m²)':>14s} | {'ratio':>12s} | "
          f"{'ratio−1':>12s} | {'α/(2π)':>12s}")
    print("-" * 100)

    target = alpha / (2 * math.pi)

    moment_data = []

    for r, s, R, a, E0, q_eff, Q_num, Q_analytic in results:
        rho = R + a * np.cos(TH1)

        v_sq = (1 + 2*s)**2 * a**2 + 4 * rho**2
        v_mag = np.sqrt(v_sq)

        sigma_actual = eps0 * E0 * np.cos(TH1 + q_eff * TH2)
        dA = a * rho * dth1 * dth2

        A_torus = np.sum(dA)
        sigma_uniform = abs(Q_analytic) / A_torus

        weight = 2 * rho**2 / v_mag

        mu_actual = (c / 2) * np.sum(sigma_actual * weight * dA)
        mu_uniform_pos = (c / 2) * sigma_uniform * np.sum(weight * dA)

        if abs(mu_uniform_pos) < 1e-50:
            continue

        ratio = mu_actual / mu_uniform_pos
        correction = ratio - 1.0

        mu_B = e * hbar / (2 * m_e)

        print(f"{r:6.2f} | {s:10.6f} | {mu_actual:14.6e} | "
              f"{mu_uniform_pos:14.6e} | {ratio:12.8f} | "
              f"{correction:12.8f} | {target:12.8f}")

        moment_data.append((r, s, ratio, correction, mu_actual, mu_uniform_pos))

    print()

    # ── Section 4: Detailed analysis of the ratio ─────────────
    print()
    print("SECTION 4: Analysis of the correction")
    print("-" * 72)
    print()
    print(f"Target anomalous correction: α/(2π) = {target:.8f}")
    print(f"                             α/π    = {alpha/math.pi:.8f}")
    print(f"                             α      = {alpha:.8f}")
    print()

    if moment_data:
        print(f"{'r':>6s} | {'correction':>14s} | {'corr/α':>10s} | "
              f"{'corr/(α/2π)':>12s} | {'corr/(α/π)':>12s}")
        print("-" * 70)

        for r, s, ratio, correction, mu_act, mu_unif in moment_data:
            print(f"{r:6.2f} | {correction:14.8f} | "
                  f"{correction/alpha:10.4f} | "
                  f"{correction/target:12.4f} | "
                  f"{correction/(alpha/math.pi):12.4f}")

    print()

    # ── Section 5: Analytical cross-check ─────────────────────
    print()
    print("SECTION 5: Analytical structure")
    print("-" * 72)
    print()
    print("The θ₂ integral of cos(θ₁ + q_eff θ₂) gives:")
    print("  -2 sin(πs) cos(θ₁ − πs) / (2−s)")
    print()
    print("So the moment ratio reduces to:")
    print("  ratio = ∫cos(θ₁−πs) × ρ³/|v| dθ₁")
    print("        / [∫cos(θ₁−πs) × ρ dθ₁ × (1/A)∫ρ³/|v| dθ₁ × 2π]")
    print()
    print("The correction comes from the CORRELATION between")
    print("cos(θ₁ − πs) (charge pattern) and ρ²/|v| (moment weighting).")
    print()

    if moment_data:
        print("Checking: does the charge pattern favor larger ρ?")
        print()
        for r, s, R, a, E0, q_eff, Q_num, Q_analytic in results[:5]:
            rho_1d = R + a * np.cos(theta1)

            cos_pattern = np.cos(theta1 - math.pi * s)

            rho_charge_avg = np.sum(cos_pattern * rho_1d * rho_1d * dth1) / np.sum(cos_pattern * rho_1d * dth1)
            rho_area_avg = np.sum(rho_1d * rho_1d * dth1) / np.sum(rho_1d * dth1)

            rho2_charge_avg = np.sum(cos_pattern * rho_1d**3 * dth1) / np.sum(cos_pattern * rho_1d * dth1)
            rho2_area_avg = np.sum(rho_1d**3 * dth1) / np.sum(rho_1d * dth1)

            print(f"r = {r:.2f}:")
            print(f"  ⟨ρ⟩_charge = {rho_charge_avg/R:.6f} R")
            print(f"  ⟨ρ⟩_area   = {rho_area_avg/R:.6f} R")
            print(f"  ⟨ρ²⟩_charge / ⟨ρ²⟩_area = {rho2_charge_avg/rho2_area_avg:.8f}")
            print()

    # ── Section 6: Verdict ────────────────────────────────────
    print()
    print("SECTION 6: Verdict")
    print("=" * 72)
    print()

    if moment_data:
        corrections = [c for _, _, _, c, _, _ in moment_data]
        ratios_to_target = [c / target if abs(target) > 1e-20 else 0
                            for c in corrections]

        print(f"Range of μ_actual/μ_uniform − 1:")
        print(f"  Min:  {min(corrections):.10f}")
        print(f"  Max:  {max(corrections):.10f}")
        print()
        print(f"Target (α/(2π)):  {target:.10f}")
        print(f"Target (α/π):     {alpha/math.pi:.10f}")
        print()

        if all(abs(c) < 1e-10 for c in corrections):
            print("RESULT: The correction is negligible (< 10⁻¹⁰).")
            print("The charge-mass separation from shear does NOT produce")
            print("an anomalous magnetic moment at this level.")
            print()
            print("This means either:")
            print("  (a) The shear is too small to create significant asymmetry")
            print("  (b) The ρ²/|v| weighting averages out the charge pattern")
            print("  (c) A different mechanism is needed for g−2")
        elif any(abs(c/target - 1) < 0.1 for c in corrections):
            match_r = [r for r, _, _, c, _, _ in moment_data
                       if abs(c/target - 1) < 0.1]
            print(f"MATCH FOUND near α/(2π) at r = {match_r}")
            print("The charge-mass separation produces the anomalous moment!")
        else:
            print(f"Corrections are non-zero but do not match α/(2π):")
            for r, s, ratio, correction, mu_act, mu_unif in moment_data:
                print(f"  r = {r:.2f}: correction = {correction:.10f} "
                      f"= {correction/target:.4f} × α/(2π)")


if __name__ == "__main__":
    main()
