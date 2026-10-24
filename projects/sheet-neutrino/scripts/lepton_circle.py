"""Modes of the lepton-domain neutrino circle (host G).

What it does
  Models the grand neutrino circle as three segments (one per charged-lepton
  sheet) joined at three junctions.  Each junction partially reflects the
  wave (a point scatterer of strength g, standing in for the coupling to an
  electron sheet).  Each segment carries a Klein flip of the wave's
  polarization; three flips give one net sign change per circuit, so the
  circle closes antiperiodically: ψ(L_total) = −ψ(0).

  Mass ∝ wavenumber k.  With equal segments the lowest two modes form an
  exactly degenerate pair (protected by 3-fold symmetry); unequal segments
  split it.  The script finds, for each g, the segment asymmetry d that gives
  the measured Δm²₃₁/Δm²₂₁, with segment lengths (1 − d, 1, 1 + d) × L/3.

Inputs: command-line options (see --help).  Outputs: printed tables.
"""
import argparse

import numpy as np
from scipy.optimize import brentq


def monodromy(k, lens, g):
    """Transfer matrix of (ψ, ψ') once around the circle."""
    T = np.eye(2)
    D = np.array([[1.0, 0.0], [g, 1.0]])               # point scatterer at each junction
    for l in lens:
        P = np.array([[np.cos(k * l), np.sin(k * l) / k],
                      [-k * np.sin(k * l), np.cos(k * l)]])
        T = D @ P @ T
    return T


def modes(lens, g, kmax, n_grid, sign=-1):
    """Wavenumbers with ψ(L) = sign·ψ(0); degenerate roots appear once per member."""
    f = lambda k: np.linalg.det(monodromy(k, lens, g) - sign * np.eye(2))
    ks = np.linspace(1e-3, kmax, n_grid)
    v = np.array([f(k) for k in ks])
    out = []
    for i in range(len(ks) - 1):
        if v[i] * v[i + 1] < 0:
            out.append(brentq(f, ks[i], ks[i + 1]))
    a = np.abs(v)
    for i in range(1, len(ks) - 1):                    # touching zeros = degenerate pairs
        if a[i] < a[i - 1] and a[i] < a[i + 1] and a[i] < 1e-6:
            out += [ks[i], ks[i]]
    return np.sort(out)


def ratio(k):
    m2 = np.sort(k)[:3] ** 2
    split = m2[1] - m2[0]
    return np.inf if split <= 0 else (m2[2] - m2[0]) / split


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--target", type=float, default=33.6, help="Δm²₃₁/Δm²₂₁ target")
    p.add_argument("--dm21", type=float, default=7.53e-5, help="solar Δm²₂₁ in eV²")
    p.add_argument("--g", type=float, nargs="+", default=[0.5, 1.0, 2.0, 4.0],
                   help="junction strengths (in units of 1/L_total × 2π)")
    p.add_argument("--kmax", type=float, default=4.0, help="largest wavenumber searched")
    p.add_argument("--n-grid", type=int, default=20000, help="root-search grid size")
    a = p.parse_args()
    L = 2 * np.pi                                       # plain antiperiodic loop → k = n + ½

    print("== Equal segments: lowest modes (k; plain loop would give 0.5, 0.5, 1.5, 1.5)")
    for g in [0.0] + a.g:
        k = modes([L / 3] * 3, g, a.kmax, a.n_grid)[:4]
        print(f"  g={g:4.1f}: k = {', '.join(f'{x:.4f}' for x in k)}")

    print(f"\n== Unequal segments (1−d, 1, 1+d)·L/3: asymmetry d giving ratio {a.target}")
    for g in a.g:
        f = lambda d: ratio(modes([L / 3 * (1 - d), L / 3, L / 3 * (1 + d)],
                                  g, a.kmax, a.n_grid)) - a.target
        try:
            d = brentq(f, 0.002, 0.3, xtol=1e-5)
        except ValueError:
            print(f"  g={g:4.1f}: target not bracketed for d ∈ [0.002, 0.3]")
            continue
        k = modes([L / 3 * (1 - d), L / 3, L / 3 * (1 + d)], g, a.kmax, a.n_grid)[:4]
        m2 = k[:3] ** 2
        unit = np.sqrt(a.dm21 / (m2[1] - m2[0]))
        mev = 1e3 * unit * k
        print(f"  g={g:4.1f}: d={d:.4f}  masses = {mev[0]:.1f}, {mev[1]:.1f}, {mev[2]:.1f} meV, "
              f"Σm = {mev[:3].sum():.0f} meV, m₃/m₁ = {k[2] / k[0]:.2f}; "
              f"4th state {mev[3]:.1f} meV (must be sterile)")


if __name__ == "__main__":
    main()
