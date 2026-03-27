#!/usr/bin/env python3
"""
02_series_scan.py — Scan the (r, n) parameter space for the charge series.

Tests Proposition P1 (series hypothesis) and P2 (recognizable ratio).

Model:  e = q₀ × Σᵢ₌₀ⁿ rⁱ  =  q₀ × (1 − r^(n+1)) / (1 − r)
Target: S = e/q₀ ≈ 1.0985

The script:
  1. Computes S_target from the WvM baseline.
  2. For each candidate ratio r, finds the best n and the infinite-series sum.
  3. Performs a fine-grained sweep of r to find the exact value that gives
     S_target for each n.
  4. Reports which (r, n) pairs come closest to recognized constants.

Reference: theory.md §4 (P1, P2), §5.2
"""

import math, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib import constants as C
from lib.wvm import q_over_e, S_TARGET
from lib.series import geometric_sum, infinite_sum, solve_r_for_n

CANDIDATES = [
    ("α",           C.alpha),
    ("2α",          2 * C.alpha),
    ("πα",          math.pi * C.alpha),
    ("2πα",         2 * math.pi * C.alpha),
    ("4πα",         4 * math.pi * C.alpha),
    ("√α",          math.sqrt(C.alpha)),
    ("α^(2/3)",     C.alpha ** (2/3)),
    ("1/11",        1 / 11),
    ("1/12",        1 / 12),
    ("1/(4π)",      1 / (4 * math.pi)),
    ("3/(4π)",      3 / (4 * math.pi)),
    ("√3/(2π)",     math.sqrt(3) / (2 * math.pi)),
    ("1/ϕ²",        1 / C.phi ** 2),
    ("1/ϕ³",        1 / C.phi ** 3),
    ("1/ϕ⁴",        1 / C.phi ** 4),
    ("2/(3π)",      2 / (3 * math.pi)),
    ("1/(2π)²",     1 / (2 * math.pi) ** 2),
    ("α·ϕ·π",       C.alpha * C.phi * math.pi),
]


def r_exact_for_infinite():
    """The exact r such that 1/(1−r) = S_TARGET."""
    return 1 - 1 / S_TARGET


def find_best_n(r, tol=0.1):
    """Find smallest n such that geometric_sum(r, n) is within tol% of target."""
    for n in range(200):
        s = geometric_sum(r, n)
        if abs(s - S_TARGET) / S_TARGET < tol / 100:
            return n, s
    return None, geometric_sum(r, 199)


def main():
    r_exact = r_exact_for_infinite()

    print("=" * 72)
    print("Series Parameter Scan — Propositions P1 & P2")
    print("=" * 72)
    print()
    print(f"  q/e     = {q_over_e:.6f}")
    print(f"  S_target = e/q = {S_TARGET:.6f}")
    print(f"  Exact r (infinite series) = {r_exact:.6f}")
    print()

    # ── Part 1: Named candidate ratios ────────────────────────────────────────
    print("─" * 72)
    print(f"{'Candidate':<14s} {'r':>10s}  {'S(∞)':>10s}  {'Err %':>8s}  "
          f"{'n for 0.1%':>10s}  {'S(n)':>10s}")
    print("─" * 72)

    ranked = []
    for name, r in CANDIDATES:
        if not (0 < r < 1):
            continue
        s_inf = infinite_sum(r)
        err_inf = abs(s_inf - S_TARGET) / S_TARGET * 100
        best_n, s_n = find_best_n(r)
        n_str = str(best_n) if best_n is not None else ">200"
        ranked.append((err_inf, name, r, s_inf, n_str, s_n))

    ranked.sort()
    for err, name, r, s_inf, n_str, s_n in ranked:
        print(f"  {name:<12s} {r:>10.6f}  {s_inf:>10.6f}  {err:>7.4f}%  "
              f"{n_str:>10s}  {s_n:>10.6f}")

    print()

    # ── Part 2: What r is required for each n? ────────────────────────────────
    print("─" * 72)
    print("Required r to hit S_target exactly, for each n (number of sub-dims):")
    print("─" * 72)
    print(f"  {'n':>3s}  {'terms':>5s}  {'r_required':>12s}  {'S':>10s}  "
          f"{'Nearest constant':>20s}  {'Δ':>8s}")
    print()

    for n in range(1, 21):
        r_req = solve_r_for_n(n, S_TARGET)
        s_check = geometric_sum(r_req, n)

        best_name, best_dist = "", 1.0
        for name, r_cand in CANDIDATES:
            if 0 < r_cand < 1:
                dist = abs(r_cand - r_req)
                if dist < best_dist:
                    best_dist = dist
                    best_name = name
        delta = best_dist / r_req * 100

        print(f"  {n:>3d}  {n+1:>5d}  {r_req:>12.8f}  {s_check:>10.6f}  "
              f"{best_name:>20s}  {delta:>7.2f}%")

    print()

    # ── Part 3: Fine sweep around the exact r ─────────────────────────────────
    print("─" * 72)
    print(f"Fine sweep: ratios within ±5% of r_exact = {r_exact:.6f}")
    print("─" * 72)
    lo = r_exact * 0.95
    hi = r_exact * 1.05

    nearby = [(name, r) for name, r in CANDIDATES if lo <= r <= hi]
    if nearby:
        print("  Named constants in this window:")
        for name, r in nearby:
            s_inf = infinite_sum(r)
            err = abs(s_inf - S_TARGET) / S_TARGET * 100
            print(f"    {name:<14s} r = {r:.8f}  S(∞) = {s_inf:.8f}  err = {err:.4f}%")
    else:
        print("  No named constants fall in this window.")

    print()
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  Exact r for infinite series:  {r_exact:.8f}")
    print(f"  Best named candidate:         {ranked[0][1]} "
          f"(r={ranked[0][2]:.6f}, err={ranked[0][0]:.4f}%)")
    print(f"  Second best:                  {ranked[1][1]} "
          f"(r={ranked[1][2]:.6f}, err={ranked[1][0]:.4f}%)")
    print()


if __name__ == "__main__":
    main()
