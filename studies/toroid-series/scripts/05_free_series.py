#!/usr/bin/env python3
"""
05_free_series.py — Unconstrained series decomposition of the WvM charge deficit.

Instead of *assuming* a geometric series, this script asks:
  "What set of N positive, decreasing terms sums to the charge deficit D,
   and what do the term-to-term ratios look like?"

For each N (number of correction terms, from 2 to 12):
  1. Optimizes a free N-term sequence to sum exactly to D = S_TARGET − 1,
     subject only to: all terms positive, monotonically decreasing, and
     the progression of successive ratios (t_{k+1}/t_k) is as smooth as
     possible (minimizing jerk in the ratio sequence).
  2. Reports the optimal terms, their successive ratios, and how close
     those ratios are to known constants.
  3. Compares the result to the best geometric series for that N.

The goal is to let the data speak: if the optimal free sequence turns out
to have nearly constant ratios, the geometric model is validated.  If the
ratios drift systematically, that points to a different functional form.

Reference: theory.md §5.2, STATUS.md item 1
"""

import math
import sys
import os
import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib import constants as C
from lib.wvm import S_TARGET
from lib.series import geometric_sum, solve_r_for_n

D = S_TARGET - 1.0   # deficit to fill ≈ 0.0985

KNOWN = [
    ("α",           C.alpha),
    ("2α",          2 * C.alpha),
    ("πα",          math.pi * C.alpha),
    ("2πα",         2 * math.pi * C.alpha),
    ("4πα",         4 * math.pi * C.alpha),
    ("√α",          math.sqrt(C.alpha)),
    ("α^(2/3)",     C.alpha ** (2.0/3)),
    ("1/11",        1.0 / 11),
    ("1/12",        1.0 / 12),
    ("1/(4π)",      1.0 / (4 * math.pi)),
    ("3/(4π)",      3.0 / (4 * math.pi)),
    ("1/ϕ²",        1.0 / C.phi ** 2),
    ("1/ϕ³",        1.0 / C.phi ** 3),
    ("1/(2π)²",     1.0 / (2 * math.pi) ** 2),
    ("α·ϕ·π",       C.alpha * C.phi * math.pi),
]


def nearest_constant(value):
    """Find the named constant closest to value."""
    best_name, best_dist = "—", float("inf")
    for name, val in KNOWN:
        d = abs(val - value)
        if d < best_dist:
            best_dist = d
            best_name = name
    pct = best_dist / max(abs(value), 1e-30) * 100
    return best_name, pct


# ── Parameterization ──────────────────────────────────────────────────────────
# We parameterize N positive decreasing terms via unconstrained variables x:
#   raw_i = exp(x_i)               (ensures positivity)
#   terms are sorted descending    (ensures monotonicity)
#   then scaled so they sum to D   (exact sum constraint)
#
# The optimizer minimizes a smoothness penalty on the log-ratio sequence.

def x_to_terms(x):
    """Map unconstrained vector x → N positive terms summing to D."""
    raw = np.exp(x)
    raw = np.sort(raw)[::-1]        # descending
    return raw * (D / raw.sum())


def smoothness_penalty(x):
    """
    Penalty that favors smooth ratio progressions.

    Given terms t_0 > t_1 > ... > t_{N-1}, define ratios r_k = t_{k+1}/t_k.
    We penalize:
      - Variance of the log-ratios (favors constant ratio, i.e. geometric)
      - Second differences of log-ratios (favors smooth drift)
    The balance lets the optimizer find geometric *or* smoothly-drifting
    sequences, but disfavors erratic jumps.
    """
    terms = x_to_terms(x)
    if np.any(terms <= 0):
        return 1e12

    ratios = terms[1:] / terms[:-1]
    if np.any(ratios <= 0) or np.any(ratios >= 1):
        return 1e12

    lr = np.log(ratios)

    # Variance of log-ratios (geometric = zero variance)
    var_penalty = np.var(lr)

    # Second differences (smooth drift = zero second difference)
    if len(lr) >= 3:
        d2 = np.diff(lr, n=2)
        jerk_penalty = np.sum(d2 ** 2)
    else:
        jerk_penalty = 0.0

    return var_penalty + 0.5 * jerk_penalty


def optimize_free_series(n_terms, n_restarts=40):
    """Find the smoothest N-term decomposition of D."""
    best_cost = float("inf")
    best_terms = None

    rng = np.random.default_rng(42)

    for _ in range(n_restarts):
        x0 = rng.standard_normal(n_terms)
        res = minimize(smoothness_penalty, x0, method="Nelder-Mead",
                       options={"maxiter": 20000, "xatol": 1e-14,
                                "fatol": 1e-14, "adaptive": True})
        if res.fun < best_cost:
            best_cost = res.fun
            best_terms = x_to_terms(res.x)

    return best_terms, best_cost


def geometric_for_n(n_terms):
    """Best geometric series with n_terms terms (indices 0..n_terms-1)."""
    n = n_terms - 1
    r = solve_r_for_n(n, S_TARGET)
    terms = np.array([r ** k for k in range(n_terms)])
    terms = terms * (D / terms.sum())
    return terms, r


def print_terms(terms, label=""):
    """Pretty-print a term sequence with ratios and nearest constants."""
    ratios = terms[1:] / terms[:-1]
    print(f"  {'k':>3s}  {'Term':>14s}  {'Cumul. sum':>14s}  "
          f"{'Ratio t_k/t_{k-1}':>18s}  {'Nearest':>10s}  {'Δ':>7s}")
    cumsum = 0.0
    for k, t in enumerate(terms):
        cumsum += t
        if k == 0:
            r_str = "—"
            near_str = "—"
            pct_str = "—"
        else:
            r_str = f"{ratios[k-1]:.8f}"
            name, pct = nearest_constant(ratios[k-1])
            near_str = name
            pct_str = f"{pct:.1f}%"
        print(f"  {k:>3d}  {t:>14.10f}  {cumsum:>14.10f}  "
              f"{r_str:>18s}  {near_str:>10s}  {pct_str:>7s}")

    if len(ratios) > 0:
        lr = np.log(ratios)
        cv = np.std(lr) / abs(np.mean(lr)) * 100 if abs(np.mean(lr)) > 1e-15 else 0
        print(f"\n  Log-ratio statistics:  mean = {np.mean(lr):.6f}  "
              f"std = {np.std(lr):.6f}  CV = {cv:.1f}%")
        if len(ratios) >= 2:
            drift = np.diff(lr)
            print(f"  Log-ratio drift (Δ):  {', '.join(f'{d:+.6f}' for d in drift)}")


def main():
    print("=" * 78)
    print("Free Series Decomposition of the WvM Charge Deficit")
    print("=" * 78)
    print()
    print(f"  S_TARGET = {S_TARGET:.8f}")
    print(f"  Deficit D = S − 1 = {D:.8f}")
    print()

    all_results = []

    for n_terms in range(2, 13):
        print("─" * 78)
        print(f"  N = {n_terms} terms")
        print("─" * 78)

        # Free (unconstrained) optimum
        free_terms, cost = optimize_free_series(n_terms)
        print(f"\n  FREE OPTIMUM (smoothness penalty = {cost:.2e}):\n")
        print_terms(free_terms)

        # Geometric comparison
        geo_terms, geo_r = geometric_for_n(n_terms)
        geo_ratios = geo_terms[1:] / geo_terms[:-1]
        print(f"\n  GEOMETRIC COMPARISON (r = {geo_r:.8f}):\n")
        print_terms(geo_terms)

        # How close is the free solution to geometric?
        free_ratios = free_terms[1:] / free_terms[:-1]
        if len(free_ratios) > 0:
            mean_ratio = np.exp(np.mean(np.log(free_ratios)))
            ratio_spread = np.std(np.log(free_ratios))
            all_results.append((n_terms, mean_ratio, ratio_spread, cost))
            name, pct = nearest_constant(mean_ratio)
            print(f"\n  Geometric mean of free ratios: {mean_ratio:.8f}"
                  f"  (nearest: {name}, Δ={pct:.1f}%)")
            print(f"  Spread (σ of log-ratios):      {ratio_spread:.6f}"
                  f"  {'← nearly geometric' if ratio_spread < 0.01 else ''}")

        print()

    # ── Summary ───────────────────────────────────────────────────────────────
    print("=" * 78)
    print("SUMMARY: How geometric is the free optimum?")
    print("=" * 78)
    print()
    print(f"  {'N':>3s}  {'Mean ratio':>12s}  {'σ(log r)':>10s}  "
          f"{'Penalty':>12s}  {'Nearest':>10s}  {'Δ':>7s}  {'Geometric?':>12s}")
    for n, mr, sp, cost in all_results:
        name, pct = nearest_constant(mr)
        geo_flag = "YES" if sp < 0.01 else ("~" if sp < 0.05 else "no")
        print(f"  {n:>3d}  {mr:>12.8f}  {sp:>10.6f}  "
              f"{cost:>12.2e}  {name:>10s}  {pct:>6.1f}%  {geo_flag:>12s}")

    print()
    print("If σ(log r) ≈ 0 for all N, the geometric model is the unique")
    print("smooth solution and the study can focus on identifying r.")
    print("If σ(log r) grows or shows structure, a non-geometric model")
    print("may be needed.")
    print()


if __name__ == "__main__":
    main()
