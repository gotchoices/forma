#!/usr/bin/env python3
"""
R8 Track 4: Shear analysis.

Compute the shear δ for each solution along the (q, r) curve,
express it in various units, and look for patterns —
especially connections to α, known length scales, and
relativistic/wave-mechanical effects.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha, m_e, lambda_C

r_e = e**2 / (4.0 * math.pi * eps0 * m_e * c**2)
lambda_bar_C = hbar / (m_e * c)  # reduced Compton wavelength
mu_B = e * hbar / (2 * m_e)      # Bohr magneton
a_0 = hbar / (m_e * c * alpha)   # Bohr radius


def compute_shape_factor(r, N_theta=32, N_phi=64):
    R0 = 1.0
    a0 = r * R0
    d_theta = 2.0 * math.pi / N_theta
    d_phi = 2.0 * math.pi / N_phi

    xs, ys, zs, dAs = [], [], [], []
    A_total = 0.0

    for i in range(N_theta):
        theta = (i + 0.5) * d_theta
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        rho = R0 + a0 * cos_t
        dA = abs(rho) * a0 * d_theta * d_phi

        for j in range(N_phi):
            phi = (j + 0.5) * d_phi
            xs.append(rho * math.cos(phi))
            ys.append(rho * math.sin(phi))
            zs.append(a0 * sin_t)
            dAs.append(dA)
            A_total += dA

    N = len(xs)
    dqs = [dA / A_total for dA in dAs]

    g_val = 0.0
    for i in range(N):
        qi = dqs[i]
        xi, yi, zi = xs[i], ys[i], zs[i]
        for j in range(i + 1, N):
            dx = xi - xs[j]
            dy = yi - ys[j]
            dz = zi - zs[j]
            dist = math.sqrt(dx * dx + dy * dy + dz * dz)
            g_val += qi * dqs[j] / dist

    return g_val


def main():
    print("R8 Track 4: Shear Analysis")
    print("=" * 72)
    print()

    print("Reference scales:")
    print(f"  λ_C       = {lambda_C:.6e} m   (Compton wavelength)")
    print(f"  λ̄_C       = {lambda_bar_C:.6e} m   (reduced Compton)")
    print(f"  r_e       = {r_e:.6e} m   (classical electron radius)")
    print(f"  α         = {alpha:.6e}")
    print(f"  1/α       = {1/alpha:.4f}")
    print(f"  α r_e     = {alpha * r_e:.6e} m")
    print(f"  α² λ̄_C    = {alpha**2 * lambda_bar_C:.6e} m   (= α r_e)")
    print(f"  a_0       = {a_0:.6e} m   (Bohr radius)")
    print()

    r_samples = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.31, 0.35,
                 0.40, 0.50, 0.60, 0.75, 1.00, 1.50, 2.00]

    print("Computing shape factors...")
    data = []
    for r in r_samples:
        g = compute_shape_factor(r, N_theta=32, N_phi=64)
        R = 2.0 * g * r_e
        a = r * R
        q_exact = lambda_C / (2 * math.pi * R * math.sqrt(1 + r**2 / 4))
        data.append((r, g, R, a, q_exact))
        print(f"  r = {r:.2f}  g = {g:.6f}  q = {q_exact:.2f}")

    print()
    print("=" * 72)
    print()

    # ── Table 1: δ in absolute and fractional terms ──

    print("Table 1: Shear δ — fractional and absolute")
    print()
    print(f"{'q':>5s}  {'r':>6s}  {'R(m)':>11s}  {'a(m)':>11s}"
          f"  {'δ/L_θ':>10s}  {'δ(m)':>11s}  {'δ/L_φ':>10s}")
    print("-" * 80)

    shear_data = []
    for r_val, g_val, R_val, a_val, q_val in data:
        q_int = round(q_val)
        if q_int < 50:
            continue

        L_theta = 2 * math.pi * a_val
        L_phi = 2 * math.pi * R_val

        delta_frac_Ltheta = 1.0 / (2 * q_int)
        delta_abs = L_theta / (2 * q_int)
        delta_frac_Lphi = delta_abs / L_phi

        shear_data.append({
            'q': q_int, 'r': r_val, 'g': g_val,
            'R': R_val, 'a': a_val,
            'L_theta': L_theta, 'L_phi': L_phi,
            'delta_abs': delta_abs,
            'delta_frac_Ltheta': delta_frac_Ltheta,
            'delta_frac_Lphi': delta_frac_Lphi,
        })

        print(f"{q_int:5d}  {r_val:6.3f}  {R_val:11.4e}  {a_val:11.4e}"
              f"  {delta_frac_Ltheta:10.6f}  {delta_abs:11.4e}"
              f"  {delta_frac_Lphi:10.6f}")

    print()

    # ── Table 2: δ in units of known length scales ──

    print("Table 2: δ compared to known length scales")
    print()
    print(f"{'q':>5s}  {'δ(m)':>11s}  {'δ/r_e':>10s}  {'δ/(αr_e)':>10s}"
          f"  {'δ/λ̄_C':>10s}  {'δ/(α²λ̄_C)':>10s}  {'δ/(αR)':>10s}")
    print("-" * 84)

    for d in shear_data:
        delta = d['delta_abs']
        print(f"{d['q']:5d}  {delta:11.4e}"
              f"  {delta/r_e:10.6f}"
              f"  {delta/(alpha*r_e):10.4f}"
              f"  {delta/lambda_bar_C:10.6f}"
              f"  {delta/(alpha**2 * lambda_bar_C):10.4f}"
              f"  {delta/(alpha * d['R']):10.4f}")

    print()

    # ── Table 3: Time and phase per circuit ──

    print("Table 3: Transit time and phase per major circuit")
    print()

    T_Compton = lambda_C / c
    print(f"  Compton period T_C = λ_C/c = {T_Compton:.4e} s")
    print(f"  Compton frequency ν_C = {c/lambda_C:.4e} Hz")
    print()

    print(f"{'q':>5s}  {'ℓ/circuit(m)':>13s}  {'T_circ(s)':>11s}"
          f"  {'T/T_C':>10s}  {'Δφ_phase':>10s}  {'pitch°':>8s}")
    print("-" * 72)

    for d in shear_data:
        q = d['q']
        l_per_circuit = lambda_C / q
        T_circuit = l_per_circuit / c
        T_ratio = T_circuit / T_Compton

        delta_phase = 2 * math.pi * d['L_phi'] / lambda_C

        pitch_angle = math.atan2(d['L_theta'] / 2, d['L_phi'])
        pitch_deg = math.degrees(pitch_angle)

        print(f"{q:5d}  {l_per_circuit:13.4e}  {T_circuit:11.4e}"
              f"  {T_ratio:10.6f}  {delta_phase:10.6f}"
              f"  {pitch_deg:8.3f}")

    print()

    # ── Table 4: Berry phase analysis ──

    print("Table 4: Berry phase per major circuit")
    print("  (geometric phase from propagation direction tracing")
    print("   a cone on the unit sphere)")
    print()

    print(f"{'q':>5s}  {'pitch°':>8s}  {'1-cosθ':>10s}  {'Berry/2π':>10s}"
          f"  {'δ/L_θ':>10s}  {'ratio':>8s}")
    print("-" * 65)

    for d in shear_data:
        q = d['q']
        sin_pitch = (d['L_theta'] / 2) / (lambda_C / q)
        cos_pitch = math.sqrt(1 - sin_pitch**2)
        pitch_deg = math.degrees(math.asin(sin_pitch))

        berry_per_rev = 1 - cos_pitch
        delta_frac = d['delta_frac_Ltheta']

        ratio = berry_per_rev / delta_frac if delta_frac > 0 else 0

        print(f"{q:5d}  {pitch_deg:8.3f}  {berry_per_rev:10.6f}"
              f"  {berry_per_rev:10.6f}  {delta_frac:10.6f}"
              f"  {ratio:8.3f}")

    print()

    # ── Table 5: What changes during one φ-crossing ──

    print("Table 5: 'What changed while the photon crossed?'")
    print("  Phase advance per circuit, and spatial 'wavelength mismatch'")
    print()

    print(f"{'q':>5s}  {'L_φ/λ_C':>10s}  {'L_φ/λ̄_C':>10s}"
          f"  {'nλ in L_φ':>10s}  {'residual':>10s}  {'resid×L_θ':>11s}"
          f"  {'δ':>11s}")
    print("-" * 88)

    for d in shear_data:
        q = d['q']
        ratio_Lphi_lambdaC = d['L_phi'] / lambda_C
        ratio_Lphi_lambdabarC = d['L_phi'] / lambda_bar_C

        n_waves = d['L_phi'] / lambda_C
        residual = n_waves - math.floor(n_waves)

        resid_times_Ltheta = residual * d['L_theta']

        print(f"{q:5d}  {ratio_Lphi_lambdaC:10.6f}  {ratio_Lphi_lambdabarC:10.4f}"
              f"  {n_waves:10.6f}  {residual:10.6f}  {resid_times_Ltheta:11.4e}"
              f"  {d['delta_abs']:11.4e}")

    print()

    # ── Table 6: Analytical relationships ──

    print("Table 6: Testing analytical hypotheses for δ")
    print()

    print("Hypothesis A:  δ = α × L_φ / (2π)")
    print("  (shear equals α times the major radius)")
    print()
    print(f"{'q':>5s}  {'δ':>11s}  {'αR':>11s}  {'δ/(αR)':>8s}")
    print("-" * 45)
    for d in shear_data:
        aR = alpha * d['R']
        print(f"{d['q']:5d}  {d['delta_abs']:11.4e}  {aR:11.4e}"
              f"  {d['delta_abs']/aR:8.4f}")

    print()
    print("Hypothesis B:  δ = α² × λ̄_C  (constant, independent of q)")
    print(f"  α² λ̄_C = {alpha**2 * lambda_bar_C:.4e} m")
    print()
    print(f"{'q':>5s}  {'δ':>11s}  {'δ/(α²λ̄_C)':>12s}")
    print("-" * 35)
    for d in shear_data:
        print(f"{d['q']:5d}  {d['delta_abs']:11.4e}"
              f"  {d['delta_abs']/(alpha**2 * lambda_bar_C):12.4f}")

    print()
    print("Hypothesis C:  δ = r²/(4q) × L_φ")
    print("  (from small-angle approximation of Berry phase: (1-cosθ) ≈ θ²/2,")
    print("   and θ ≈ r/2, giving Berry = r²/8 per revolution)")
    print()
    print(f"{'q':>5s}  {'δ':>11s}  {'r²L_φ/(4q)':>12s}  {'ratio':>8s}")
    print("-" * 48)
    for d in shear_data:
        pred = d['r']**2 * d['L_phi'] / (4 * d['q'])
        print(f"{d['q']:5d}  {d['delta_abs']:11.4e}  {pred:12.4e}"
              f"  {d['delta_abs']/pred:8.4f}")

    print()

    # ── Hypothesis D: δ = αR when r = 1/π ──

    print("Hypothesis D:  δ = αR exactly when r = 1/π")
    print()
    print("  Algebraically: δ/(αR) = πr/(qα).")
    print("  From mass constraint: qα = 1/(2g(r)√(1+r²/4)).")
    print("  So δ/(αR) = πr × 2g(r)√(1+r²/4) = 2πr g(r)√(1+r²/4).")
    print("  This equals 1 when g(r) = 1/(2πr√(1+r²/4)).")
    print()
    print(f"{'q':>5s}  {'r':>6s}  {'g(r)':>8s}  {'g_needed':>8s}"
          f"  {'2πrg√..':>8s}  {'δ/(αR)':>8s}")
    print("-" * 56)
    for d in shear_data:
        r = d['r']
        g = d['g']
        factor = 2 * math.pi * r * g * math.sqrt(1 + r**2 / 4)
        g_needed = 1 / (2 * math.pi * r * math.sqrt(1 + r**2 / 4))
        print(f"{d['q']:5d}  {r:6.3f}  {g:8.4f}  {g_needed:8.4f}"
              f"  {factor:8.4f}  {d['delta_abs']/(alpha * d['R']):8.4f}")

    print()
    print(f"  At r = 1/π = {1/math.pi:.4f}:")
    r_test = 1 / math.pi
    g_test = compute_shape_factor(r_test, N_theta=32, N_phi=64)
    g_needed_test = 1 / (2 * math.pi * r_test * math.sqrt(1 + r_test**2/4))
    q_test = 1 / (2 * alpha * g_test * math.sqrt(1 + r_test**2/4))
    print(f"    g(1/π) = {g_test:.6f}")
    print(f"    g needed for δ=αR: {g_needed_test:.6f}")
    print(f"    q at r=1/π: {q_test:.2f}")
    print(f"    2πrg√(1+r²/4) = {2*math.pi*r_test*g_test*math.sqrt(1+r_test**2/4):.4f}")
    print()

    # ── Special analysis for q ≈ 137 ──

    print("=" * 72)
    print()
    print("Detailed analysis: interpolated to q = 137")
    print()

    # Interpolate to find exact r for q=137
    d137 = None
    for i in range(len(data) - 1):
        q1, q2 = data[i][4], data[i+1][4]
        if q1 <= 137 <= q2 or q2 <= 137 <= q1:
            frac = (137 - q1) / (q2 - q1)
            r_137 = data[i][0] + frac * (data[i+1][0] - data[i][0])
            g_137 = data[i][1] + frac * (data[i+1][1] - data[i][1])
            R_137 = 2.0 * g_137 * r_e
            a_137 = r_137 * R_137
            L_theta = 2 * math.pi * a_137
            L_phi = 2 * math.pi * R_137
            delta_abs = L_theta / (2 * 137)
            d137 = {
                'q': 137, 'r': r_137, 'g': g_137,
                'R': R_137, 'a': a_137,
                'L_theta': L_theta, 'L_phi': L_phi,
                'delta_abs': delta_abs,
            }
            break

    if d137:
        delta = d137['delta_abs']
        q = d137['q']
        R = d137['R']
        a = d137['a']
        L_theta = d137['L_theta']
        L_phi = d137['L_phi']

        print(f"  q = {q}")
        print(f"  r = {d137['r']:.4f}")
        print(f"  R = {R:.4e} m  ({R/r_e:.4f} r_e)")
        print(f"  a = {a:.4e} m")
        print(f"  L_θ = {L_theta:.4e} m")
        print(f"  L_φ = {L_phi:.4e} m")
        print(f"  δ = {delta:.4e} m")
        print()

        print("  δ expressed as:")
        print(f"    δ/L_θ = 1/{2*q} = {1.0/(2*q):.6f}")
        print(f"    δ/L_φ = {delta/L_phi:.6e}")
        print(f"    δ/R   = {delta/R:.6e}")
        print(f"    δ/a   = {delta/a:.6e}")
        print(f"    δ/r_e = {delta/r_e:.6e}")
        print(f"    δ/λ_C = {delta/lambda_C:.6e}")
        print(f"    δ/λ̄_C = {delta/lambda_bar_C:.6e}")
        print()

        sin_pitch = (L_theta / 2) / (lambda_C / q)
        cos_pitch = math.sqrt(1 - sin_pitch**2)
        pitch = math.asin(sin_pitch)
        berry = 1 - cos_pitch

        print(f"  Pitch angle = {math.degrees(pitch):.3f}°")
        print(f"  sin(pitch) = {sin_pitch:.6f}")
        print(f"  1 - cos(pitch) = {berry:.6f}")
        print(f"  Berry phase per rev = {berry:.6f} × 2π")
        print(f"  Required δ/L_θ     = {1/(2*q):.6f}")
        print(f"  Berry / required    = {berry * 2 * q:.4f}")
        print()

        T_circuit = (lambda_C / q) / c
        print(f"  Transit time per circuit = {T_circuit:.4e} s")
        print(f"  = {T_circuit * c / lambda_C:.6f} × T_Compton")
        print(f"  = 1/{q} × T_Compton = α × T_Compton")
        print()

        print("  Distance the photon travels in one circuit:")
        print(f"    ℓ_circ = λ_C/{q} = {lambda_C/q:.4e} m")
        print(f"    = {lambda_C/(q * L_phi):.4f} × L_φ")
        print(f"    = {lambda_C/(q * L_theta):.4f} × L_θ")
        print()

        print("  Phase advance per circuit:")
        phi_phase = 2 * math.pi * L_phi / lambda_C
        print(f"    Δφ = 2π × L_φ/λ_C = 2π × {L_phi/lambda_C:.6f}")
        print(f"        = {phi_phase:.6f} rad")
        print(f"        = {math.degrees(phi_phase):.3f}°")
        print(f"        ≈ 2πα (= {2*math.pi*alpha:.6f} rad)")
        print()

        # The "one wavelength around the ring" analysis
        n_wavelengths_in_ring = L_phi / lambda_C
        phase_per_circuit_fraction = n_wavelengths_in_ring
        phase_deficit = 1.0 - q * n_wavelengths_in_ring
        print(f"  Phase closure check:")
        print(f"    L_φ/λ_C = {n_wavelengths_in_ring:.6f} wavelengths per circuit")
        print(f"    After {q} circuits: {q * n_wavelengths_in_ring:.6f} wavelengths")
        print(f"    (should be close to 1 for resonance)")
        print()

        # δ compared to the "excess" path length from helix vs straight
        l_straight = L_phi  # straight around major circle
        l_helix = math.sqrt(L_phi**2 + (L_theta/2)**2)  # helical path per circuit
        excess = l_helix - l_straight
        print(f"  Helical excess per circuit:")
        print(f"    Straight path = L_φ = {l_straight:.4e} m")
        print(f"    Helical path  = {l_helix:.4e} m")
        print(f"    Excess = {excess:.4e} m")
        print(f"    δ / excess = {delta / excess:.6f}")
        print(f"    excess / L_θ = {excess / L_theta:.6f}")
        print()

        # δ compared to Thomas-like precession angle × a
        # For a circular orbit, Thomas precession per revolution = 2π(γ-1)
        # which is undefined for v=c. But the "geometric" rotation is 2π(1-cosθ).
        # The spatial shift this induces on the minor circle:
        geom_shift = berry * L_theta
        print(f"  Geometric phase spatial shift (Berry × L_θ):")
        print(f"    = {berry:.6f} × {L_theta:.4e}")
        print(f"    = {geom_shift:.4e} m")
        print(f"    δ = {delta:.4e} m")
        print(f"    ratio (Berry shift / δ) = {geom_shift / delta:.4f}")


if __name__ == '__main__':
    main()
