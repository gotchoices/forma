#!/usr/bin/env python3
"""
R13 Track 3: Charge from the embedding.

Compute the monopole moment (apparent charge) of a circularly
polarized plane wave on flat T², embedded on a torus in 3D.

The photon on flat T² is a plane wave with wavevector (p, q)
and uniform amplitude.  When embedded, each surface point has
a normal component of E determined by the wave phase at that
point.  The monopole moment is the surface integral of this
normal component weighted by the area element.

Result: Q_monopole = 0 for any (p, q) with q >= 1.
This is exact and analytical (proven by the vanishing of
the phi integral of cos(q*phi) over [0, 2pi)).
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import (e, eps0, m_e, c, lambda_C)

r_e = e**2 / (4.0 * math.pi * eps0 * m_e * c**2)


def monopole_integral(p, q, R, a, N_theta=200, N_phi=200):
    """
    Compute the surface integral of cos(p*theta + q*phi) * dA
    over the torus.  This is the monopole moment (up to constants)
    of the E-field normal component.

    For circular polarization, E_n ~ cos(wave_phase) where
    wave_phase = p*theta + q*phi on flat T².

    With geometric phase correction (frame rotation from the
    embedding), E_n ~ cos((p-1)*theta + q*phi).

    Both give zero for q >= 1.
    """
    d_theta = 2.0 * math.pi / N_theta
    d_phi = 2.0 * math.pi / N_phi

    results = {}

    for label, m_eff, n_eff in [
        ("plain wave", p, q),
        ("with geometric phase", p - 1, q),
    ]:
        integral = 0.0
        total_area = 0.0

        for i in range(N_theta):
            theta = (i + 0.5) * d_theta
            for j in range(N_phi):
                phi = (j + 0.5) * d_phi
                rho = R + a * math.cos(theta)
                dA = abs(rho) * a * d_theta * d_phi
                total_area += dA
                integral += math.cos(m_eff * theta + n_eff * phi) * dA

        results[label] = (integral, total_area)

    return results


def main():
    print("=" * 66)
    print("R13 Track 3: Charge from the Embedding")
    print("=" * 66)
    print()

    p, q = 68, 137
    R = 2.79e-15
    a = 8.60e-16
    r = a / R

    path_len = 2.0 * math.pi * math.sqrt((p * a)**2 + (q * R)**2)

    print(f"Geometry: (p, q) = ({p}, {q})")
    print(f"  R = {R:.4e} m,  a = {a:.4e} m,  r = {r:.4f}")
    print(f"  Flat path / lambda_C = {path_len / lambda_C:.6f}")
    print()

    # ── Analytical argument ──

    print("ANALYTICAL RESULT")
    print("-" * 66)
    print()
    print("Surface charge density from circularly polarized plane wave:")
    print(f"  sigma ~ cos({p}*theta + {q}*phi)")
    print()
    print("Monopole = integral of sigma * dA over torus:")
    print(f"  Q ~ int int cos({p}*theta + {q}*phi)")
    print(f"              * (R + a*cos(theta)) dtheta dphi")
    print()
    print(f"  phi integral: int_0^2pi cos({q}*phi) dphi = 0")
    print(f"  => Q_monopole = 0  (exact)")
    print()
    print("With geometric phase correction (frame rotation = theta):")
    print(f"  sigma ~ cos({p-1}*theta + {q}*phi)")
    print(f"  phi integral: int_0^2pi cos({q}*phi) dphi = 0")
    print(f"  => Q_monopole = 0  (exact)")
    print()
    print("The result holds for ANY (p, q) with q >= 1, any (R, a).")
    print()

    # ── Numerical verification ──

    print("NUMERICAL VERIFICATION")
    print("-" * 66)

    results = monopole_integral(p, q, R, a)
    for label, (integral, area) in results.items():
        print(f"  {label}:")
        print(f"    integral = {integral:.4e}")
        print(f"    |integral|/area = {abs(integral)/area:.2e}")

    print()

    # ── Sanity check: p=1, q=0 should give nonzero ──

    print("SANITY CHECK: p=1, q=0 (pure tube loop)")
    print("-" * 66)

    results_check = monopole_integral(1, 0, R, a)
    analytic = 2.0 * math.pi**2 * a**2
    for label, (integral, area) in results_check.items():
        print(f"  {label}:")
        print(f"    numerical  = {integral:.6e}")
    print(f"    analytical = {analytic:.6e}")
    print()

    # ── What Fourier components survive? ──

    print("FOURIER ANALYSIS")
    print("-" * 66)
    print()
    print("Monopole requires the (0,0) Fourier component of")
    print("sigma * (R + a*cos(theta)).")
    print()
    print("For sigma ~ cos(m*theta + n*phi):")
    print("  cos(m*t + n*p) * (R + a*cos(t))")
    print("    = R*cos(m*t + n*p)")
    print("      + (a/2)*cos((m+1)*t + n*p)")
    print("      + (a/2)*cos((m-1)*t + n*p)")
    print()
    print("The (0,0) component is nonzero only when:")
    print("  n = 0  AND  (m = 0, or m = +1, or m = -1)")
    print()
    print("Since n = q >= 1 in all physical cases, the monopole")
    print("is identically zero.")
    print()

    # ── Paths forward ──

    print("=" * 66)
    print("PATHS FORWARD")
    print("=" * 66)
    print()
    print("The charge cannot arise from a uniform-amplitude plane")
    print("wave embedded on a torus.  Three candidates remain:")
    print()
    print("1. AMPLITUDE MODULATION: The embedding geometry")
    print("   modulates field amplitude (not just direction).")
    print("   E.g., E_0(theta) ~ 1/(R + a*cos(theta)), giving")
    print("   sigma ~ cos(p*theta + q*phi) / (R + a*cos(theta)).")
    print("   Expanding 1/(R+a*cos) in Fourier series introduces")
    print("   ALL harmonics of theta — potentially coupling to")
    print("   cos(q*phi) to produce a (0,0) term.")
    print()

    print("   For 1/(R+a*cos) amplitude: the (R+a*cos) area element")
    print("   cancels the 1/(R+a*cos) amplitude, leaving just")
    print("   cos(p*theta + q*phi) * a, which integrates to zero.")
    print("   No theta-only amplitude modulation can help: the phi")
    print("   integral of cos(q*phi) is always zero for q >= 1.")
    print()

    print("2. MODE MIXING: The embedded-torus wave equation")
    print("   couples the (p,q) mode to other modes including")
    print("   (0,0).  The coupling strength is determined by")
    print("   the embedding curvature.  This is a perturbation-")
    print("   theory calculation on the curved torus.")
    print()
    print("3. WVM MECHANISM REVISITED: WvM's charge comes from")
    print("   confining a photon's energy in a torus-shaped volume")
    print("   and computing the average radial E-field.  This is")
    print("   NOT the same as embedding a flat-space plane wave.")
    print("   The confined photon has a non-uniform field that")
    print("   reflects the boundary shape.  The charge may require")
    print("   solving Maxwell's equations WITH the torus boundary,")
    print("   not ON a flat T^2.")


if __name__ == '__main__':
    main()
