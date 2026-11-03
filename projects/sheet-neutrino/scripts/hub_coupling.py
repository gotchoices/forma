"""Neutrino flavors coupled through a common hub (star coupling), minimal test.

What it does
  Three neutral channel states, one per charged lepton (e, μ, τ), with bare
  mass² a_e, a_μ, a_τ.  Each couples to one common heavy hub state; at second
  order (hub mass ≫ neutrino masses) the hub adds the same amount c to every
  entry of the light mass² matrix:
        M² = diag(a_e, a_μ, a_τ) + c·J,   J = all-ones 3×3,
  a rank-one, all-to-all ("star") coupling.  The mass states are M²'s
  eigenvectors; flavor = channel (the e row is the e channel; μ and τ may be
  swapped).  The matrix is real, so the mixing is CP-conserving.

  With --couplings unequal, the hub term becomes g gᵀ with one coupling per
  channel (6 parameters, under-determined; for comparison only).

  Fit targets: Δm²21, Δm²31 (normal ordering) and the δ-independent mixing
  entries |U_e1|², |U_e2|², |U_e3|², |U_μ3|², |U_τ3|².  Common coupling:
  4 parameters against 5 numbers.  Also reports |U_α2|² (trimaximal check).

Inputs: command-line options.  Outputs: printed best fits.
"""
import argparse

import numpy as np
from scipy.optimize import minimize

DM21, DM31 = 7.53e-5, 2.51e-3
S12, S13 = 0.307, 0.0220


def targets(s23):
    c13 = 1 - S13
    return np.array([(1 - S12) * c13, S12 * c13, S13, s23 * c13, (1 - s23) * c13])


def spectrum(p, unequal):
    """p in units of DM31 (eV²): a_e, a_mu, a_tau ≥ 0 via squares; then coupling(s)."""
    a = p[:3] ** 2 * DM31
    if unequal:
        g = p[3:6] * np.sqrt(DM31)
        M = np.diag(a) + np.outer(g, g)
    else:
        M = np.diag(a) + p[3] * DM31 * np.ones((3, 3))
    w, v = np.linalg.eigh(M)
    return w, v                                       # ascending: ν1, ν2, ν3 (normal ordering)


def loss(p, s23, unequal):
    w, v = spectrum(p, unequal)
    if w[0] < -1e-12 or w[1] - w[0] <= 0:
        return 1e3
    d21, d31 = w[1] - w[0], w[2] - w[0]
    U2 = v ** 2                                       # rows: channels e, μ, τ; cols: ν1..ν3
    t = targets(s23)
    best = np.inf
    for mu, tau in ((1, 2), (2, 1)):
        got = np.array([U2[0, 0], U2[0, 1], U2[0, 2], U2[mu, 2], U2[tau, 2]])
        best = min(best, np.sum((got - t) ** 2))
    return np.log(d21 / DM21) ** 2 + np.log(d31 / DM31) ** 2 + best


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--couplings", choices=["common", "unequal"], default="common")
    p.add_argument("--s23", type=float, nargs="+", default=[0.45, 0.50, 0.55])
    p.add_argument("--restarts", type=int, default=200)
    p.add_argument("--seed", type=int, default=0)
    a = p.parse_args()
    unequal = a.couplings == "unequal"
    n = 6 if unequal else 4
    rng = np.random.default_rng(a.seed)
    for s23 in a.s23:
        best = None
        for _ in range(a.restarts):
            x0 = rng.normal(0, 1, n)
            r = minimize(loss, x0, args=(s23, unequal), method="Nelder-Mead",
                         options=dict(maxiter=4000, xatol=1e-10, fatol=1e-14))
            if best is None or r.fun < best.fun:
                best = r
        w, v = spectrum(best.x, unequal)
        U2 = v ** 2
        m = np.sqrt(np.clip(w, 0, None)) * 1e3
        print(f"\n== couplings {a.couplings}, sin²θ23 = {s23}: loss {best.fun:.3e}")
        print(f"  bare mass² (eV²): " + ", ".join(f"{x:.3e}" for x in best.x[:3] ** 2 * DM31)
              + (f";  hub term c = {best.x[3] * DM31:+.3e} eV²" if not unequal else ""))
        print(f"  masses (meV): {m[0]:.2f}, {m[1]:.2f}, {m[2]:.2f};  Δm²21 = {w[1] - w[0]:.3e}, "
              f"Δm²31 = {w[2] - w[0]:.3e} eV²")
        print("  |U|² (rows e, μ, τ channels; columns ν1 ν2 ν3):")
        for i, name in enumerate(("e", "μ", "τ")):
            print(f"    {name}  " + "  ".join(f"{x:.3f}" for x in U2[i]))
        s13 = U2[0, 2]
        s12 = U2[0, 1] / (1 - s13)
        print(f"  sin²θ12 = {s12:.3f} (measured 0.307), sin²θ13 = {s13:.4f} (0.0220); "
              f"ν2 column = {', '.join(f'{x:.3f}' for x in U2[:, 1])} (trimaximal: 0.333 each)")


if __name__ == "__main__":
    main()
