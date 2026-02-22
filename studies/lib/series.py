"""
Geometric series utilities for the toroid-series study.
"""


def geometric_sum(r, n):
    """Sum of finite geometric series: Σᵢ₌₀ⁿ rⁱ = (1 − r^(n+1)) / (1 − r)."""
    if abs(r) < 1e-15:
        return 1.0
    return (1 - r ** (n + 1)) / (1 - r)


def infinite_sum(r):
    """Sum of infinite geometric series: 1 / (1 − r), for |r| < 1."""
    return 1 / (1 - r)


def solve_r_for_n(n, target):
    """Binary search for r that gives target sum with exactly n+1 terms."""
    lo, hi = 1e-10, 0.9999
    for _ in range(200):
        mid = (lo + hi) / 2
        if geometric_sum(mid, n) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2
