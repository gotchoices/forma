#!/usr/bin/env python3
"""
01_wvm_baseline.py — Reproduce the WvM charge prediction from first principles.

Derives q from Eq. 5 of Williamson & van der Mark (1997) and compares it to
the measured elementary charge.  Establishes the numerical baseline that all
other scripts in this study depend on.

Reference: theory.md §1, §5.1
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib import constants as C
from lib.wvm import wvm_charge, wvm_charge_ratio, q_over_e, S_TARGET


def main():
    q       = wvm_charge()
    deficit = (1 - q_over_e) * 100

    print("=" * 64)
    print("WvM Baseline: Charge Prediction from Eq. 5")
    print("=" * 64)
    print()
    print("Physical constants used:")
    print(f"  ℏ        = {C.hbar:.6e} J·s")
    print(f"  c        = {C.c} m/s")
    print(f"  ε₀       = {C.eps0:.10e} F/m")
    print(f"  α        = 1/{1/C.alpha:.6f}")
    print(f"  e        = {C.e:.6e} C")
    print(f"  m_e      = {C.m_e:.6e} kg")
    print(f"  λ_C      = {C.lambda_C:.6e} m")
    print(f"  r̄ = λ_C/4π = {C.r_bar:.6e} m")
    print()

    print("WvM prediction:")
    print(f"  q = (1/2π)√(3ε₀ℏc) = {q:.6e} C")
    print(f"  q / e               = {q_over_e:.6f}")
    print(f"  q in units of e     = {q_over_e:.6f} e")
    print()

    print("Comparison to measured charge:")
    print(f"  e (measured)         = {C.e:.6e} C")
    print(f"  q (WvM)              = {q:.6e} C")
    print(f"  Deficit              = {deficit:.2f}%")
    print(f"  Correction factor    = e/q = {S_TARGET:.6f}")
    print()

    print("This correction factor is the TARGET for the series study.")
    print(f"  S_target = {S_TARGET:.6f}")
    print()

    q_over_e_numerical = q / C.e
    assert abs(q_over_e - q_over_e_numerical) < 1e-6, \
        f"Analytic ({q_over_e}) vs numerical ({q_over_e_numerical}) mismatch"
    print("✓ Analytic and numerical q/e agree.")


if __name__ == "__main__":
    main()
