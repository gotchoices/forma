"""
R56 Track 4: Free 3D couplet packing — when does shell 2 start?

For each N couplets at Z = 2N (neutral atom):
  - Freely optimize all 3N coordinates
  - Use basin-hopping for global minimum
  - Record radii of all couplets
  - Check: unimodal (one shell) or bimodal (two shells)?

The shell-1 capacity is where the radius distribution first
splits into two distinct groups.
"""

import numpy as np
from scipy.optimize import minimize, basinhopping
import math

ALPHA = 1.0 / 137.036
HC = 197.3269804  # MeV·fm
A0 = 52917.7  # Bohr radius in fm

R_EFF = 751.0  # fm (model-E electron)
Q = 2.0  # couplet charge


def V_ne(r, Z):
    if r < 1.0:
        r = 1.0
    if r > R_EFF:
        return -Z * Q * ALPHA * HC / r
    else:
        return -Z * Q * ALPHA * HC / R_EFF


def V_cc(d):
    if d < 1.0:
        d = 1.0
    if d > R_EFF:
        return Q**2 * ALPHA * HC / d
    else:
        return Q**2 * ALPHA * HC / R_EFF


def total_energy(params, Z, N):
    positions = params.reshape(N, 3)
    E = 0.0
    for i in range(N):
        r = np.linalg.norm(positions[i])
        E += V_ne(r, Z)
    for i in range(N):
        for j in range(i + 1, N):
            d = np.linalg.norm(positions[i] - positions[j])
            E += V_cc(d)
    return E


def optimize_N(N, Z):
    """Basin-hopping global optimization for N couplets."""
    scale = A0 / Z

    def energy(params):
        return total_energy(params, Z, N)

    best = None

    # Basin-hopping from multiple starts
    for trial in range(5):
        x0 = np.random.randn(3 * N) * scale * 0.5
        minimizer_kwargs = {'method': 'L-BFGS-B'}

        try:
            result = basinhopping(energy, x0,
                                   minimizer_kwargs=minimizer_kwargs,
                                   niter=100, T=abs(energy(x0)) * 0.1,
                                   seed=trial)
            if best is None or result.fun < best.fun:
                best = result
        except Exception:
            pass

    # Also try structured initial conditions
    for config in generate_configs(N, scale):
        result = minimize(energy, config.flatten(), method='L-BFGS-B')
        if best is None or result.fun < best.fun:
            best = result

    positions = best.x.reshape(N, 3)
    radii = np.array([np.linalg.norm(p) for p in positions])
    return best.fun, radii, positions


def generate_configs(N, scale):
    """Generate structured starting configurations."""
    configs = []

    # All on a sphere
    for r in [scale * 0.3, scale * 0.5, scale * 0.8]:
        pos = np.random.randn(N, 3)
        pos = pos / np.linalg.norm(pos, axis=1, keepdims=True) * r
        configs.append(pos)

    # Thomson-like: evenly spaced on sphere
    if N <= 12:
        # Fibonacci sphere
        golden = (1 + math.sqrt(5)) / 2
        for r in [scale * 0.3, scale * 0.5]:
            pos = []
            for i in range(N):
                theta = math.acos(1 - 2 * (i + 0.5) / N)
                phi = 2 * math.pi * i / golden
                pos.append([r * math.sin(theta) * math.cos(phi),
                           r * math.sin(theta) * math.sin(phi),
                           r * math.cos(theta)])
            configs.append(np.array(pos))

    # Two shells: inner + outer
    if N >= 3:
        for n_inner in range(1, min(N, 4)):
            n_outer = N - n_inner
            r_in = scale * 0.2
            r_out = scale * 0.6
            pos_in = np.random.randn(n_inner, 3)
            pos_in = pos_in / np.linalg.norm(pos_in, axis=1, keepdims=True) * r_in
            pos_out = np.random.randn(n_outer, 3)
            pos_out = pos_out / np.linalg.norm(pos_out, axis=1, keepdims=True) * r_out
            configs.append(np.vstack([pos_in, pos_out]))

    return configs


def analyze_radii(radii):
    """Check if radii are unimodal or bimodal."""
    sorted_r = np.sort(radii)
    N = len(sorted_r)

    if N <= 2:
        return 'single', sorted_r, []

    # Look for the largest gap between consecutive sorted radii
    gaps = np.diff(sorted_r)
    max_gap_idx = np.argmax(gaps)
    max_gap = gaps[max_gap_idx]

    # Compare max gap to median gap
    median_gap = np.median(gaps)
    mean_r = np.mean(sorted_r)

    # Bimodal if the largest gap is > 3× the median AND > 10% of mean radius
    if max_gap > 3 * median_gap and max_gap > 0.1 * mean_r:
        inner = sorted_r[:max_gap_idx + 1]
        outer = sorted_r[max_gap_idx + 1:]
        return 'bimodal', inner, outer
    else:
        return 'single', sorted_r, []


def main():
    print("=" * 70)
    print("R56 Track 4: Free 3D couplet packing")
    print("=" * 70)
    print()
    print("N couplets at Z = 2N (neutral atom).  All positions free.")
    print("Basin-hopping for global minimum.  Watch for shell splitting.")
    print()

    print(f"  {'N':>3s}  {'Z':>3s}  {'Ne':>4s}  {'E(keV)':>10s}  "
          f"{'ΔE':>10s}  {'struct':>8s}  "
          f"{'inner r(pm)':>20s}  {'outer r(pm)':>20s}  {'geometry':>15s}")
    print(f"  {'─'*3}  {'─'*3}  {'─'*4}  {'─'*10}  {'─'*10}  {'─'*8}  "
          f"{'─'*20}  {'─'*20}  {'─'*15}")

    prev_E = 0.0
    for N in range(1, 13):
        Z = 2 * N  # neutral atom

        E, radii, positions = optimize_N(N, Z)
        E_keV = E * 1e3
        dE = E_keV - prev_E
        prev_E = E_keV

        structure, inner, outer = analyze_radii(radii)
        sorted_r = np.sort(radii)

        # Determine geometry
        if N == 1:
            geom = 'point'
        elif N == 2:
            geom = 'linear'
        elif N == 3:
            geom = 'triangle'
        elif N == 4:
            geom = 'tetrahedron?'
        elif N == 5:
            geom = 'bipyramid?'
        elif N == 6:
            geom = 'octahedron?'
        else:
            geom = ''

        inner_str = ', '.join(f'{r/100:.1f}' for r in inner[:5])
        outer_str = ', '.join(f'{r/100:.1f}' for r in outer[:5])
        if len(inner) > 5:
            inner_str += '...'
        if len(outer) > 5:
            outer_str += '...'

        print(f"  {N:>3d}  {Z:>3d}  {2*N:>4d}  {E_keV:>10.2f}  "
              f"{dE:>+10.2f}  {structure:>8s}  "
              f"{inner_str:>20s}  {outer_str:>20s}  {geom:>15s}")

    print()

    # ── Also test with Z ≠ 2N to see shell filling ─────────────
    print("=" * 70)
    print("Fixed Z = 18 (argon), vary N couplets from 1 to 11")
    print("(Shows how couplets fill around a fixed nucleus)")
    print("=" * 70)
    print()

    Z = 18
    print(f"  {'N':>3s}  {'Ne':>4s}  {'E(keV)':>10s}  {'ΔE':>10s}  "
          f"{'struct':>8s}  {'radii (pm, sorted)':>40s}")
    print(f"  {'─'*3}  {'─'*4}  {'─'*10}  {'─'*10}  {'─'*8}  {'─'*40}")

    prev_E = 0.0
    for N in range(1, 12):
        E, radii, positions = optimize_N(N, Z)
        E_keV = E * 1e3
        dE = E_keV - prev_E
        prev_E = E_keV

        structure, inner, outer = analyze_radii(radii)
        sorted_r = np.sort(radii)

        r_str = ', '.join(f'{r/100:.1f}' for r in sorted_r[:8])
        if len(sorted_r) > 8:
            r_str += '...'

        print(f"  {N:>3d}  {2*N:>4d}  {E_keV:>10.2f}  {dE:>+10.2f}  "
              f"{structure:>8s}  {r_str:>40s}")

    print()
    print("Track 4 complete.")


if __name__ == '__main__':
    main()
