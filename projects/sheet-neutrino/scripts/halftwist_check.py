"""Charged wye + half-twisted neutrino sheets on one large tube (5 dimensions).

What it does
  Dimensions: electron tubes T_e, T_μ, T_τ (= C/m at resonance), the wye's
  shared ring r, and one large neutrino tube B.
    electron sheets  (T_i → r), common shear σ_e = 2: (1, 2) resonant = e, μ, τ
    neutrino sheets  (B → ring_j), common half twist σ_ν = ½ + ε:
                     (2, 1) nearly resonant, neutral under the closure rule
                     (2 does not divide 1), mass² = (2C/B)² + (2εC/ring_j)².
  The neutrino-sheet rings are chosen from {T_μ, T_τ, r} (T_e is excluded: a
  neutrino sheet ringed by T_e carries a charged state near m_e/2, below the
  electron).  For each choice, solves for r, ε, B to match Δm²21, Δm²31 and a
  chosen lightest mass, then lists every state of the full geometry below
  2 GeV using lepton_search's mode rules (harmonics excluded).

Inputs: command-line options.  Outputs: printed solutions and spectra.
"""
import argparse
import itertools

import numpy as np
from scipy.optimize import brentq

import lepton_search as ls

C = ls.C_MEV_FM
TUBE = {"e": C / ls.LEPTONS[0], "mu": C / ls.LEPTONS[1], "tau": C / ls.LEPTONS[2]}
DM21, DM31 = ls.DM21, ls.DM31


def spectrum(r, B, eps, rings):
    """Masses and charge flags for the 5-dim geometry (dims: Te, Tmu, Ttau, r, B)."""
    L = np.array([TUBE["e"], TUBE["mu"], TUBE["tau"], r, B])
    idx = {"mu": 1, "tau": 2, "r": 3}
    sheets = [(0, 3), (1, 3), (2, 3)] + [(4, idx[j]) for j in rings]
    sig = [2.0, 2.0, 2.0] + [0.5 + eps] * 3
    vecs, charged, owner = ls.mode_table(5, sheets, 4, "asym")
    params = np.concatenate([np.log10(L), sig])
    return ls.masses(params, 5, sheets, vecs, owner), charged, vecs


def solve(rings, m1_meV):
    """r from the splitting ratio, then ε from Δm²21, B from the lightest mass."""
    def inv2(r, j):
        return 1.0 / {"mu": TUBE["mu"], "tau": TUBE["tau"], "r": r}[j] ** 2
    def ratio(lr):
        r = np.exp(lr)
        o = sorted(inv2(r, j) for j in rings)            # offsets ∝ 1/ring²
        return (o[2] - o[0]) / (o[1] - o[0]) - 33.6
    sols = []
    grid = np.linspace(np.log(1e-4), np.log(1e3), 4000)
    vals = [ratio(g) for g in grid]
    for i in range(len(grid) - 1):
        if np.isfinite(vals[i]) and np.isfinite(vals[i + 1]) and vals[i] * vals[i + 1] < 0:
            lr = brentq(ratio, grid[i], grid[i + 1])
            r = np.exp(lr)
            o = sorted(inv2(r, j) for j in rings)
            # Δm²21 [eV²] = (2εC)²(o1 − o0) with C in MeV·fm → convert MeV² to eV²
            eps = np.sqrt(DM21 / ((o[1] - o[0]) * 1e12)) / (2 * C)
            base = np.sqrt(max((m1_meV * 1e-9) ** 2 - (2 * eps * C) ** 2 * o[0], 1e-30))  # MeV
            B = 2 * C / base
            sols.append((r, eps, B))
    return sols


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--m1", type=float, default=20.0, help="lightest neutrino mass (meV)")
    a = p.parse_args()
    for rings in (("mu", "tau", "r"),):
        for r, eps, B in solve(rings, a.m1):
            m, ch, vecs = spectrum(r, B, eps, rings)
            order = np.argsort(m)
            neutral = [m[i] for i in order if not ch[i]][:4]
            charged = [m[i] for i in order if ch[i] and m[i] < 2000][:12]
            print(f"\n== rings {rings}: r = {r:.4g} fm, ε = {eps:.4g}, B = {B:.4g} fm")
            print("  lightest neutral (meV): " + ", ".join(f"{x * 1e9:.4g}" for x in neutral))
            mn = np.array(neutral[:3]) * 1e6
            print(f"  Δm²21 = {mn[1]**2 - mn[0]**2:.3e}, Δm²31 = {mn[2]**2 - mn[0]**2:.3e} eV²")
            print("  charged states below 2 GeV (MeV): " + ", ".join(f"{x:.4g}" for x in charged))


if __name__ == "__main__":
    main()
