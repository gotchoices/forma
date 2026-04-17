"""
R59 Track 1e: F4 diagnostics — resolve the mass-direction puzzle.

Three diagnostics from the review:

1. WHICH ROOT IS THE PARTICLE?
   The mass-shell gives two roots.  Under a consistent charge
   definition, one is particle, one is antiparticle.  If we've
   been picking the wrong one, the sign of ΔE/E flips.

2. FLIP THE SIGNATURE CONVENTION.
   Our metric uses (+,+,...,+,-) for (Ma, S, t).
   The other convention is (-,-,...,-,+) for (Ma, S, t).
   If ΔE/E changes sign with the convention, F4 is a
   coordinate artifact.

3. EXAMINE THE QUADRATIC STRUCTURE.
   The mass-shell is: a ω² + b ω + c = 0
   The two roots are ω = (-b ± √disc) / 2a.
   The sign of b (the cross-term between Ma and t) determines
   which root is heavier.  This cross-term IS the coupling.
   Analyze its structure.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np
from lib.ma_model_d import M_E_MEV, M_P_MEV, _TWO_PI_HC, solve_shear_for_alpha

ALPHA = 1.0 / 137.036
TWO_PI_HC = _TWO_PI_HC
INV_2PI = 1.0 / (2 * math.pi)


def sheet_metric(eps, s):
    return np.array([
        [1.0,       s * eps],
        [s * eps,   1.0 + s**2 * eps**2]
    ])


def sheet_L(eps, s, n_tube, n_ring, mass_MeV):
    mu = math.sqrt((n_tube/eps)**2 + (n_ring - n_tube*s)**2)
    L_ring = TWO_PI_HC * mu / mass_MeV
    return eps * L_ring, L_ring


def build_6D(A_2x2, sigma_ring_t, sign_convention='mostly_plus'):
    """
    6D: 2 Ma + 3 S + 1 t

    sign_convention:
      'mostly_plus':  Ma=+, S=+, t=-  (our current convention)
      'mostly_minus': Ma=-, S=-, t=+  (the alternative)
    """
    G = np.zeros((6, 6))
    G[0:2, 0:2] = A_2x2.copy()
    G[2, 2] = 1.0; G[3, 3] = 1.0; G[4, 4] = 1.0
    G[5, 5] = -1.0

    if sign_convention == 'mostly_minus':
        G[0:2, 0:2] = -A_2x2
        G[2, 2] = -1.0; G[3, 3] = -1.0; G[4, 4] = -1.0
        G[5, 5] = +1.0

    # Ring-t coupling
    G[1, 5] = sigma_ring_t
    G[5, 1] = sigma_ring_t

    return G


def build_7D_aleph(A_2x2, sigma_ring_aleph, sigma_aleph_t):
    """
    7D: 2 Ma + 1 ℵ + 3 S + 1 t
    Indices: 0 tube, 1 ring, 2 ℵ, 3-5 S, 6 t
    """
    G = np.zeros((7, 7))
    G[0:2, 0:2] = A_2x2
    G[2, 2] = 1.0  # ℵ
    G[3, 3] = 1.0; G[4, 4] = 1.0; G[5, 5] = 1.0  # S
    G[6, 6] = -1.0  # t

    G[1, 2] = sigma_ring_aleph; G[2, 1] = sigma_ring_aleph
    G[2, 6] = sigma_aleph_t; G[6, 2] = sigma_aleph_t

    return G


def mass_shell_full(G, idx_t, L_2, n2):
    """
    Returns both roots AND the quadratic coefficients.
    """
    try:
        Gi = np.linalg.inv(G)
    except:
        return np.nan, np.nan, {}, np.nan

    N = len(G)
    nt = np.zeros(N)
    nt[0] = n2[0] / L_2[0]
    nt[1] = n2[1] / L_2[1]

    a = Gi[idx_t, idx_t]
    b = 2.0 * (Gi[0, idx_t] * nt[0] + Gi[1, idx_t] * nt[1])
    c = nt @ Gi @ nt

    disc = b**2 - 4*a*c

    if disc < 0:
        return np.nan, np.nan, {'a': a, 'b': b, 'c': c, 'disc': disc}, np.nan

    w1 = (-b + math.sqrt(disc)) / (2*a)
    w2 = (-b - math.sqrt(disc)) / (2*a)

    E1 = TWO_PI_HC * w1  # SIGNED energy (not abs)
    E2 = TWO_PI_HC * w2

    # Also compute unsigned
    E1_abs = TWO_PI_HC * abs(w1)
    E2_abs = TWO_PI_HC * abs(w2)

    coeffs = {
        'a': a, 'b': b, 'c': c, 'disc': disc,
        'w1': w1, 'w2': w2,
        'E1_signed': E1, 'E2_signed': E2,
        'E1_abs': E1_abs, 'E2_abs': E2_abs,
    }

    return min(E1_abs, E2_abs), max(E1_abs, E2_abs), coeffs, disc


def main():
    print("=" * 75)
    print("R59 Track 1e: F4 diagnostics — mass-direction puzzle")
    print("=" * 75)
    print()

    eps_e = 397.074; s_e = 2.004200
    A_e = sheet_metric(eps_e, s_e)
    Le_tube, Le_ring = sheet_L(eps_e, s_e, 1, 2, M_E_MEV)
    L_2 = np.array([Le_tube, Le_ring])

    mu_12 = math.sqrt((1/eps_e)**2 + (2 - s_e)**2)
    E_bare = TWO_PI_HC * mu_12 / Le_ring

    print(f"  Bare electron: {E_bare:.6f} MeV")
    print()

    # ── Diagnostic 1: Which root is the particle? ──────────
    print("─" * 75)
    print("Diagnostic 1: Examine BOTH roots with signed energies")
    print("─" * 75)
    print()

    sigma = 0.00855  # D1 optimal

    G_D1 = build_6D(A_e, -sigma)
    E_lo, E_hi, coeffs, disc = mass_shell_full(G_D1, 5, L_2, (1, 2))

    print(f"  D1 (direct ring-t, σ = {sigma})")
    print(f"  Quadratic: a={coeffs['a']:.6f}, b={coeffs['b']:.6e}, c={coeffs['c']:.6e}")
    print(f"  Discriminant: {disc:.6e}")
    print(f"  ω₁ = {coeffs['w1']:.8e}  →  E₁ = {coeffs['E1_signed']:.6f} MeV (signed)")
    print(f"  ω₂ = {coeffs['w2']:.8e}  →  E₂ = {coeffs['E2_signed']:.6f} MeV (signed)")
    print(f"  |E₁| = {coeffs['E1_abs']:.6f}, |E₂| = {coeffs['E2_abs']:.6f}")
    print(f"  E_bare = {E_bare:.6f}")
    print()

    # Interpretation:
    # In Lorentzian physics, positive ω = positive energy (particle)
    # Negative ω = negative energy (antiparticle in Feynman picture)
    print(f"  Interpretation:")
    print(f"    ω₁ > 0: {'particle' if coeffs['w1'] > 0 else 'antiparticle'}")
    print(f"    ω₂ > 0: {'particle' if coeffs['w2'] > 0 else 'antiparticle'}")
    print()

    # Which is heavier?
    if coeffs['w1'] > 0 and coeffs['w2'] > 0:
        print(f"    Both roots are positive energy (both particles)")
        print(f"    Lower root ({min(coeffs['E1_abs'], coeffs['E2_abs']):.6f}) vs "
              f"bare ({E_bare:.6f}): "
              f"{'UP' if min(coeffs['E1_abs'], coeffs['E2_abs']) > E_bare else 'DOWN'}")
        print(f"    Higher root ({max(coeffs['E1_abs'], coeffs['E2_abs']):.6f}) vs "
              f"bare ({E_bare:.6f}): "
              f"{'UP' if max(coeffs['E1_abs'], coeffs['E2_abs']) > E_bare else 'DOWN'}")
    elif coeffs['w1'] > 0:
        E_particle = coeffs['E1_abs']
        print(f"    Particle root: E = {E_particle:.6f} "
              f"({'UP' if E_particle > E_bare else 'DOWN'} from bare)")
    elif coeffs['w2'] > 0:
        E_particle = coeffs['E2_abs']
        print(f"    Particle root: E = {E_particle:.6f} "
              f"({'UP' if E_particle > E_bare else 'DOWN'} from bare)")
    print()

    # Now do D2 (ℵ-mediated)
    sigma_at = 0.258
    G_D2 = build_7D_aleph(A_e, -INV_2PI, sigma_at)
    E_lo2, E_hi2, coeffs2, disc2 = mass_shell_full(G_D2, 6, L_2, (1, 2))

    print(f"  D2 (ℵ-mediated, σ_ℵt = {sigma_at})")
    print(f"  Quadratic: a={coeffs2['a']:.6f}, b={coeffs2['b']:.6e}, c={coeffs2['c']:.6e}")
    print(f"  ω₁ = {coeffs2['w1']:.8e}  →  E₁ = {coeffs2['E1_signed']:.6f} MeV (signed)")
    print(f"  ω₂ = {coeffs2['w2']:.8e}  →  E₂ = {coeffs2['E2_signed']:.6f} MeV (signed)")
    print()
    if coeffs2['w1'] > 0 and coeffs2['w2'] > 0:
        print(f"    Both roots positive")
        print(f"    Lower: {min(coeffs2['E1_abs'], coeffs2['E2_abs']):.6f} "
              f"({'UP' if min(coeffs2['E1_abs'], coeffs2['E2_abs']) > E_bare else 'DOWN'})")
        print(f"    Higher: {max(coeffs2['E1_abs'], coeffs2['E2_abs']):.6f} "
              f"({'UP' if max(coeffs2['E1_abs'], coeffs2['E2_abs']) > E_bare else 'DOWN'})")
    print()

    # ── Diagnostic 2: Flip signature convention ────────────
    print("─" * 75)
    print("Diagnostic 2: Flip signature convention")
    print("  Mostly-plus: (Ma+, S+, t-)")
    print("  Mostly-minus: (Ma-, S-, t+)")
    print("─" * 75)
    print()

    for conv_name, conv in [('mostly_plus', 'mostly_plus'),
                             ('mostly_minus', 'mostly_minus')]:
        G = build_6D(A_e, -sigma, sign_convention=conv)
        E_lo, E_hi, coeffs, disc = mass_shell_full(G, 5, L_2, (1, 2))

        print(f"  {conv_name}:")
        print(f"    a={coeffs['a']:.6f}, b={coeffs['b']:.6e}")
        print(f"    ω₁={coeffs['w1']:.6e}, ω₂={coeffs['w2']:.6e}")
        print(f"    |E₁|={coeffs['E1_abs']:.6f}, |E₂|={coeffs['E2_abs']:.6f}")

        # Which is closer to bare?
        E_lo_abs = min(coeffs['E1_abs'], coeffs['E2_abs'])
        E_hi_abs = max(coeffs['E1_abs'], coeffs['E2_abs'])
        print(f"    E_bare = {E_bare:.6f}")
        print(f"    Closer root: {E_lo_abs:.6f} ({'UP' if E_lo_abs > E_bare else 'DOWN'})")
        print(f"    Farther root: {E_hi_abs:.6f} ({'UP' if E_hi_abs > E_bare else 'DOWN'})")
        print()

    # ── Diagnostic 3: Analyze the b coefficient ────────────
    print("─" * 75)
    print("Diagnostic 3: The cross-term b in the quadratic")
    print("  a ω² + b ω + c = 0")
    print("  b = 2 × Σ_i G⁻¹[i,t] × n_i/L_i")
    print("  When b = 0: roots are symmetric (ω = ±√(c/a))")
    print("  When b ≠ 0: roots split asymmetrically")
    print("─" * 75)
    print()

    # Sweep σ and track how b changes
    print(f"  D1 (direct ring-t), sweeping σ:")
    print(f"  {'σ':>8s}  {'b':>12s}  {'ω₁':>12s}  {'ω₂':>12s}  "
          f"{'E_lo':>8s}  {'E_hi':>8s}  {'split':>8s}  {'lo dir':>7s}")
    print(f"  {'─'*8}  {'─'*12}  {'─'*12}  {'─'*12}  "
          f"{'─'*8}  {'─'*8}  {'─'*8}  {'─'*7}")

    for s in [0.0, 0.001, 0.005, 0.00855, 0.01, 0.05, 0.1]:
        G = build_6D(A_e, -s)
        _, _, co, _ = mass_shell_full(G, 5, L_2, (1, 2))
        if 'w1' not in co:
            continue
        E_lo = min(co['E1_abs'], co['E2_abs'])
        E_hi = max(co['E1_abs'], co['E2_abs'])
        split = E_hi - E_lo
        lo_dir = "UP" if E_lo > E_bare else "DOWN" if E_lo < E_bare else "same"

        print(f"  {s:8.4f}  {co['b']:12.4e}  {co['w1']:12.6e}  {co['w2']:12.6e}  "
              f"{E_lo:8.4f}  {E_hi:8.4f}  {split:8.4f}  {lo_dir:>7s}")

    print()

    # ── Diagnostic 4: What if we use (E_hi - E_bare) instead? ──
    print("─" * 75)
    print("Diagnostic 4: What if the HIGHER root is the physical particle?")
    print("  (The higher root always goes UP from bare)")
    print("─" * 75)
    print()

    # D1
    G = build_6D(A_e, -0.00855)
    _, _, co, _ = mass_shell_full(G, 5, L_2, (1, 2))
    E_hi = max(co['E1_abs'], co['E2_abs'])
    ae_hi = (E_hi - E_bare) / E_bare
    print(f"  D1: E_hi = {E_hi:.6f}, ΔE/E = {ae_hi:.6e} = {ae_hi/ALPHA:.4f}α")
    print(f"       (positive = mass INCREASES = correct Coulomb sign)")
    print()

    # D2
    G2 = build_7D_aleph(A_e, -INV_2PI, 0.258)
    _, _, co2, _ = mass_shell_full(G2, 6, L_2, (1, 2))
    E_lo2 = min(co2['E1_abs'], co2['E2_abs'])
    E_hi2 = max(co2['E1_abs'], co2['E2_abs'])
    ae_lo2 = (E_lo2 - E_bare) / E_bare
    ae_hi2 = (E_hi2 - E_bare) / E_bare
    print(f"  D2: E_lo = {E_lo2:.6f} (ΔE/E = {ae_lo2:.6e} = {ae_lo2/ALPHA:.4f}α, UP)")
    print(f"       E_hi = {E_hi2:.6f} (ΔE/E = {ae_hi2:.6e} = {ae_hi2/ALPHA:.4f}α, UP)")
    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 75)
    print("SUMMARY")
    print("=" * 75)
    print()
    print("  The mass-shell quadratic gives two roots (ω₁, ω₂).")
    print("  We have been taking the LOWER |E| root as the particle.")
    print()
    print("  Key question: is the physical particle the lower or higher root?")
    print("  - If LOWER: D1 gives mass DOWN (wrong), D2 gives mass UP (correct)")
    print("  - If HIGHER: D1 gives mass UP (correct!), D2 gives mass UP (correct)")
    print()
    print("  If the HIGHER root is the particle, BOTH D1 and D2 give the")
    print("  correct mass direction.  The D1 sign problem (F4) would be")
    print("  an artifact of choosing the wrong root.")
    print()
    print("Track 1e complete.")


if __name__ == '__main__':
    main()
