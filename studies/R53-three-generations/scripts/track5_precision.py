"""
R53 Track 5: Precision values for all leading single-sheet solutions

Computes exact (ε, s) using Decimal arithmetic for each leading
candidate triple.  Records predicted masses, ring detunings, and
α diagnostics.  This is the authoritative reference table that
R54 inherits.
"""

import sys
import os
import math
from decimal import Decimal, getcontext

getcontext().prec = 50

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.ma_model_d import alpha_from_geometry


# ════════════════════════════════════════════════════════════════
#  Solver
# ════════════════════════════════════════════════════════════════

def solve_decimal(e, mu_m, tau_m, m1, m2, m3):
    """
    Exact solve for (ε, s) from three modes and three masses.
    Returns dict with all precision values, or None if x < 0.
    """
    p, q = e; r, t = mu_m; u, v = tau_m
    R1 = Decimal(str(m2)) / Decimal(str(m1))
    R2 = Decimal(str(m3)) / Decimal(str(m1))
    R1sq = R1 * R1; R2sq = R2 * R2

    a1 = Decimal(r**2) - R1sq * Decimal(p**2)
    b1 = Decimal(t**2) - R1sq * Decimal(q**2)
    c1 = Decimal(r * t) - R1sq * Decimal(p * q)
    a2 = Decimal(u**2) - R2sq * Decimal(p**2)
    b2 = Decimal(v**2) - R2sq * Decimal(q**2)
    c2 = Decimal(u * v) - R2sq * Decimal(p * q)

    det = Decimal(-2) * (a1 * c2 - a2 * c1)
    if abs(det) < Decimal('1e-30'):
        return None

    w = (Decimal(2) * b1 * c2 - Decimal(2) * b2 * c1) / det
    s_val = (-a1 * b2 + a2 * b1) / det
    x = w - s_val * s_val

    if x <= 0:
        return None

    eps_val = (Decimal(1) / x).sqrt()

    # Float versions for verification and α
    sf = float(s_val)
    ef = float(eps_val)

    def mu(nt, nr):
        return math.sqrt((nt / ef) ** 2 + (nr - nt * sf) ** 2)

    me = mu(*e); mm = mu(*mu_m); mt = mu(*tau_m)
    scale = float(m1) / me

    # Ring detunings
    d_e = q - p * sf
    d_mu = t - r * sf
    d_tau = v - u * sf

    # α diagnostic
    try:
        a = alpha_from_geometry(ef, sf, e[0], e[1])
    except Exception:
        a = float('nan')

    return {
        's': sf, 's_exact': str(s_val),
        'eps': ef, 'eps_exact': str(eps_val),
        'x': float(x),
        'E1': scale * me, 'E2': scale * mm, 'E3': scale * mt,
        'mu1': me, 'mu2': mm, 'mu3': mt,
        'd_e': d_e, 'd_mu': d_mu, 'd_tau': d_tau,
        'R1': float(R1), 'R2': float(R2),
        'alpha': a,
    }


def solve_float(e, mu_m, tau_m, m1, m2, m3):
    """Fast float check — returns True if x > 0."""
    p, q = e; r, t = mu_m; u, v = tau_m
    R1, R2 = m2 / m1, m3 / m1
    R1sq, R2sq = R1 * R1, R2 * R2
    a1 = r * r - R1sq * p * p
    b1 = t * t - R1sq * q * q
    c1 = r * t - R1sq * p * q
    a2 = u * u - R2sq * p * p
    b2 = v * v - R2sq * q * q
    c2 = u * v - R2sq * p * q
    det = -2 * (a1 * c2 - a2 * c1)
    if abs(det) < 1e-20:
        return False
    w = (2 * b1 * c2 - 2 * b2 * c1) / det
    s = (-a1 * b2 + a2 * b1) / det
    x = w - s * s
    return x > 1e-12


# ════════════════════════════════════════════════════════════════
#  Report
# ════════════════════════════════════════════════════════════════

def report(label, modes, masses, names):
    e, mu_m, tau_m = modes
    m1, m2, m3 = masses
    n1, n2, n3 = names

    sol = solve_decimal(e, mu_m, tau_m, m1, m2, m3)
    if sol is None:
        print(f'  {label}: NO REAL SOLUTION (x < 0)')
        print()
        return None

    inv_a = 1.0 / sol['alpha'] if sol['alpha'] > 0 and not math.isnan(sol['alpha']) else float('nan')

    print(f'  {label}')
    print(f'  {"─" * 60}')
    print(f'    {n1:>8s} = {str(e):>10s}    {n2:>8s} = {str(mu_m):>10s}    {n3:>8s} = {str(tau_m):>10s}')
    print()
    print(f'    s   = {sol["s"]:.15f}')
    print(f'    ε   = {sol["eps"]:.10f}')
    print(f'    1/ε² = {sol["x"]:.12e}')
    print()
    print(f'    Ring detunings (n_r − n_t · s):')
    print(f'      {n1:>8s}: {sol["d_e"]:+.10f}')
    print(f'      {n2:>8s}: {sol["d_mu"]:+.10f}')
    print(f'      {n3:>8s}: {sol["d_tau"]:+.10f}')
    print()
    print(f'    Predicted masses:')
    print(f'      {n1:>8s}: {sol["E1"]:.8f} MeV  (input: {m1})')
    print(f'      {n2:>8s}: {sol["E2"]:.6f} MeV  (observed: {m2})')
    print(f'      {n3:>8s}: {sol["E3"]:.4f} MeV  (observed: {m3})')
    print()
    print(f'    α at this geometry: {sol["alpha"]:.6f}  (1/α = {inv_a:.2f})')
    print(f'    Target: 1/α = 137.036')
    print()
    return sol


# ════════════════════════════════════════════════════════════════
#  Find best (1,2)-electron solution via float pre-scan
# ════════════════════════════════════════════════════════════════

def find_best_12_electron():
    """Scan for the most fundamental (1,2)-based lepton solution."""
    M_E, M_MU, M_TAU = 0.51099895, 105.6583755, 1776.86
    modes = []
    for nt in range(-7, 8):
        if nt == 0 or abs(nt) % 2 == 0:
            continue
        for nr in range(-30, 31):
            modes.append((nt, nr))

    best = None
    for e in [(1, 2), (-1, 2), (1, -2), (-1, -2)]:
        for mu_m in modes:
            if mu_m == e:
                continue
            for tau_m in modes:
                if tau_m == e or tau_m == mu_m:
                    continue
                if not solve_float(e, mu_m, tau_m, M_E, M_MU, M_TAU):
                    continue
                max_nr = max(abs(e[1]), abs(mu_m[1]), abs(tau_m[1]))
                total = sum(abs(n) for m in (e, mu_m, tau_m) for n in m)
                if best is None or (max_nr, total) < (best[0], best[1]):
                    best = (max_nr, total, e, mu_m, tau_m)
    return best


# ════════════════════════════════════════════════════════════════
#  Main
# ════════════════════════════════════════════════════════════════

def main():
    print('=' * 70)
    print('R53 Track 5: Precision reference values')
    print('=' * 70)
    print()

    # ── PDG masses ──────────────────────────────────────────────
    M_E = 0.51099895       # MeV (electron)
    M_MU = 105.6583755     # MeV (muon)
    M_TAU = 1776.86        # MeV (tau)

    M_U = 2.16             # MeV (up quark, MS-bar at 2 GeV)
    M_C = 1270.0           # MeV (charm)
    M_T = 172760.0         # MeV (top, pole mass)

    M_D = 4.67             # MeV (down quark)
    M_S = 93.4             # MeV (strange)
    M_B = 4180.0           # MeV (bottom)

    # ── ELECTRON SHEET ──────────────────────────────────────────
    print('═══════════════════════════════════════════════════════')
    print('ELECTRON SHEET — charged leptons (e, μ, τ)')
    print('═══════════════════════════════════════════════════════')
    print()

    report('Solution B: (1,3)/(3,8)/(3,−8)  [confirmed, chirality partner]',
           ((1, 3), (3, 8), (3, -8)), (M_E, M_MU, M_TAU),
           ('e', 'μ', 'τ'))

    report('New candidate: (3,1)/(7,2)/(5,4)  [smallest max n_r = 4]',
           ((3, 1), (7, 2), (5, 4)), (M_E, M_MU, M_TAU),
           ('e', 'μ', 'τ'))

    report('New candidate: (3,1)/(7,2)/(5,−4)  [sign variant]',
           ((3, 1), (7, 2), (5, -4)), (M_E, M_MU, M_TAU),
           ('e', 'μ', 'τ'))

    # Find best (1,2) electron solution
    print('  Searching for best (1,2)-electron solution...', flush=True)
    best12 = find_best_12_electron()
    if best12:
        max_nr, total, e, mu_m, tau_m = best12
        report(f'Best (1,2)-electron: {e}/{mu_m}/{tau_m}  [max n_r = {max_nr}]',
               (e, mu_m, tau_m), (M_E, M_MU, M_TAU),
               ('e', 'μ', 'τ'))
    else:
        print('  No (1,2)-electron solution found in |n_r| ≤ 30')
    print()

    # ── NEUTRINO SHEET ──────────────────────────────────────────
    print('═══════════════════════════════════════════════════════')
    print('NEUTRINO SHEET — from R26/R49 (not re-solved)')
    print('═══════════════════════════════════════════════════════')
    print()
    print('  Modes: ν₁ = (1,1), ν₂ = (−1,1), ν₃ = (1,2)')
    print('  s_ν = 0.02199  (from Δm²₃₁/Δm²₂₁ = 33.6)')
    print('  ε_ν = 5.0  (Family A)')
    print('  Σm_ν = 117.8 meV')
    print('  Note: small hierarchy (ratios ≈ 1:1:1.2),')
    print('  R53 shear-resonance mechanism not needed.')
    print()

    # ── PROTON SHEET — UP TYPE ──────────────────────────────────
    print('═══════════════════════════════════════════════════════')
    print('PROTON SHEET — up-type quarks (u, c, t)')
    print('═══════════════════════════════════════════════════════')
    print()

    report('Up-type A: (1,3)/(−1,3)/(3,9)  [ε≈0.5, chirality pair]',
           ((1, 3), (-1, 3), (3, 9)), (M_U, M_C, M_T),
           ('u', 'c', 't'))

    report('Up-type B: (1,3)/(−1,3)/(3,−9)  [sign variant]',
           ((1, 3), (-1, 3), (3, -9)), (M_U, M_C, M_T),
           ('u', 'c', 't'))

    report('Up-type C: (1,3)/(1,3)/(3,9) — same modes check',
           ((1, 3), (1, 3), (3, 9)), (M_U, M_C, M_T),
           ('u', 'c', 't'))

    # ── PROTON SHEET — DOWN TYPE ────────────────────────────────
    print('═══════════════════════════════════════════════════════')
    print('PROTON SHEET — down-type quarks (d, s, b)')
    print('═══════════════════════════════════════════════════════')
    print()

    report('Down-type A: (5,4)/(1,1)/(5,5)  [from Track 4]',
           ((5, 4), (1, 1), (5, 5)), (M_D, M_S, M_B),
           ('d', 's', 'b'))

    report('Down-type B: (7,3)/(5,2)/(3,5)  [smallest max n_r = 5]',
           ((7, 3), (5, 2), (3, 5)), (M_D, M_S, M_B),
           ('d', 's', 'b'))

    report('Down-type C: (7,2)/(3,1)/(5,5)  [alt]',
           ((7, 2), (3, 1), (5, 5)), (M_D, M_S, M_B),
           ('d', 's', 'b'))

    report('Down-type D: (5,4)/(1,1)/(5,−5)  [sign variant]',
           ((5, 4), (1, 1), (5, -5)), (M_D, M_S, M_B),
           ('d', 's', 'b'))

    # ── SUMMARY TABLE ───────────────────────────────────────────
    print('═══════════════════════════════════════════════════════')
    print('SUMMARY — R53 precision reference (for R54 handoff)')
    print('═══════════════════════════════════════════════════════')
    print()
    print('  Sheet    Family     ε             s              Status')
    print('  ─────    ──────     ─             ─              ──────')
    print('  Ma_e     leptons    see above     see above      confirmed or pending')
    print('  Ma_ν     neutrinos  5.0           0.02199        R49 (unchanged)')
    print('  Ma_p     up-type    see above     see above      confirmed or pending')
    print('  Ma_p     down-type  see above     see above      confirmed or pending')
    print()
    print('Track 5 complete.')


if __name__ == '__main__':
    main()
