"""Census of light modes on ma-domain's K5 five-torus, read as ONE torus.

What it does
  Takes K5's best-fit geometry (ma-domain outputs/cand_K5.txt; ranged sizes at
  representative values) and enumerates every primitive circulation vector
  n ∈ [−K, K]⁵.  Mass uses the single-torus (product) reading: a lap of a
  sheet's tube shifts that sheet's ring, for every sheet at once,
      k_d = (n_d − Σ_{s: R_s = d} σ_s n_{T_s}) / L_d,   m = C·|k|.
  For comparison it also gives ma-domain's per-sheet value for each two-
  dimension sheet mode.  Prints the lightest modes, the number of dimensions
  each one circulates in, and where the e, μ, τ masses fall.

Inputs: command-line options.  Outputs: printed tables.
"""
import argparse
import itertools
from math import gcd

import numpy as np

C = 2 * np.pi * 197.3269804                      # MeV·fm
DIMS = ["d1", "d2", "d3", "d4", "d5"]
L = {"d1": 1.0, "d2": 0.007344, "d3": 300.0, "d4": 4.062e10, "d5": 1.593e11}
# (tube, ring, σ_eff, host) from K5's best discrete solution
SHEETS = [("d3", "d1", 2.00, "s/c"), ("d3", "d2", 2.00, "b/t"), ("d4", "d3", 2.00, "u/d"),
          ("d1", "d2", 1.9932, "tau"), ("d4", "d1", 1.9996, "e"), ("d4", "d2", 2.0000, "mu"),
          ("d5", "d4", 0.0507, "nu")]


def product_mass(n):
    k = np.array(n, float)
    for T, R, s, _ in SHEETS:
        k[DIMS.index(R)] -= s * n[DIMS.index(T)]
    return C * np.sqrt(np.sum((k / np.array([L[d] for d in DIMS])) ** 2))


def sheet_mass(T, R, s, mt, mr):
    return C * np.sqrt((mt / L[T]) ** 2 + ((mr - s * mt) / L[R]) ** 2)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--K", type=int, default=3)
    p.add_argument("--top", type=int, default=25)
    a = p.parse_args()

    print("== Per-sheet (ma-domain) masses of the hosted (1, 2) modes")
    for T, R, s, h in SHEETS:
        print(f"  {h:4s} on ({T}→{R}), σ={s}: T(1,2) = {sheet_mass(T, R, s, 1, 2):.4g} MeV")

    rows = []
    for n in itertools.product(range(-a.K, a.K + 1), repeat=5):
        if not any(n):
            continue
        g = 0
        for x in n:
            g = gcd(g, abs(x))
        first = next(x for x in n if x != 0)
        if g != 1 or first < 0:
            continue
        rows.append((product_mass(n), n))
    rows.sort()
    print(f"\n== Single-torus reading: lightest {a.top} modes (|n_i| ≤ {a.K})")
    for m, n in rows[:a.top]:
        support = sum(1 for x in n if x)
        print(f"  {m:12.5g} MeV   n = {n}   circulates in {support} dims")
    for name, target in (("e", 0.511), ("mu", 105.66), ("tau", 1776.9)):
        near = min(rows, key=lambda r: abs(np.log(r[0] / target)))
        print(f"  nearest to {name} ({target} MeV): {near[0]:.4g} MeV, n = {near[1]}, "
              f"{sum(1 for x in near[1] if x)} dims")
    two_d = {(DIMS.index(T), DIMS.index(R)) for T, R, *_ in SHEETS}
    for T, R, s, h in SHEETS[3:6]:
        n = [0] * 5
        n[DIMS.index(T)], n[DIMS.index(R)] = 1, 2
        print(f"  {h}'s sheet mode {tuple(n)} in the single-torus reading: {product_mass(n):.4g} MeV")


if __name__ == "__main__":
    main()
