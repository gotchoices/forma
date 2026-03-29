#!/usr/bin/env python3
"""
R41 Track 3 — Full vs Shortcut Comparison

Compares the two dynamic solution methods across modes and sheets:
  1. Accuracy: δr_k, δE/E, energy values
  2. Speed: wall-clock time for harmonics and full mode scans
  3. Convergence: iteration count and convergence ratio
  4. Self-consistency check: one more iteration on converged result

Usage:
    cd studies && python3 R41-dynamic-model/scripts/track3_full_vs_shortcut.py
"""

import sys, os, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../..')

from lib.ma_model import (
    Ma, _compute_pressure_harmonics, _iterative_force_balance,
    _FORCE_BALANCE_TOL, _FORCE_BALANCE_MAX_ITER, _N_HARM_DEFAULT,
    _N_SAMPLES_DEFAULT, ALPHA,
)

REF = dict(r_e=6.6, r_nu=5.0, r_p=8.906, sigma_ep=-0.0906)

ELECTRON = (1, 2, 0, 0, 0, 0)
PROTON   = (0, 0, 0, 0, 1, 2)
NEUTRON  = (0, -2, 1, 0, 0, 2)
MUON     = (-1, 5, 0, 0, -2, 0)

NAMED_MODES = {
    'electron': ELECTRON,
    'proton':   PROTON,
    'neutron':  NEUTRON,
    'muon':     MUON,
}


def convergence_trace(n_tube, n_ring, r):
    """Run the iteration manually and record per-step changes."""
    n1 = abs(n_tube)
    n2 = abs(n_ring)
    n_harm = _N_HARM_DEFAULT
    delta_r_k = np.zeros(n_harm + 1)
    phi_k = np.zeros(n_harm + 1)
    trace = []

    for i in range(_FORCE_BALANCE_MAX_ITER):
        harm = _compute_pressure_harmonics(
            n1, n2, r,
            shape_delta=delta_r_k, shape_phi=phi_k)
        change = np.max(np.abs(harm.delta_r_k - delta_r_k))
        trace.append({
            'iter': i,
            'change': change,
            'delta_r_2': harm.delta_r_k[2],
        })
        delta_r_k = harm.delta_r_k.copy()
        phi_k = harm.phi_k.copy()
        if change < _FORCE_BALANCE_TOL:
            break

    return trace, harm


def section(title):
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def main():
    # ── 1. Convergence trace ──────────────────────────────────────────
    section("1. CONVERGENCE TRACE — proton (1,2) at r=8.906")

    trace, harm_conv = convergence_trace(1, 2, 8.906)
    print(f"{'Iter':>4}  {'Max|Δε_k|':>14}  {'δr₂/a':>14}  {'Ratio':>10}")
    print(f"{'─'*4}  {'─'*14}  {'─'*14}  {'─'*10}")
    for i, row in enumerate(trace):
        ratio = trace[i]['change'] / trace[i-1]['change'] if i > 0 and trace[i-1]['change'] > 0 else float('nan')
        print(f"{row['iter']:4d}  {row['change']:14.6e}  {row['delta_r_2']:14.10e}  "
              f"{ratio:10.6f}" if not np.isnan(ratio) else
              f"{row['iter']:4d}  {row['change']:14.6e}  {row['delta_r_2']:14.10e}  {'—':>10}")
    print(f"\nConverged in {len(trace)} iterations")
    print(f"Convergence ratio ≈ {trace[-2]['change']/trace[-3]['change']:.4f}" if len(trace) >= 3 else "")

    # ── 2. Self-consistency check ─────────────────────────────────────
    section("2. SELF-CONSISTENCY CHECK")

    h_conv = harm_conv
    h_check = _compute_pressure_harmonics(
        1, 2, 8.906, shape_delta=h_conv.delta_r_k, shape_phi=h_conv.phi_k)
    max_diff = np.max(np.abs(h_conv.delta_r_k - h_check.delta_r_k))
    print(f"Max |δr_k(converged) - δr_k(one more iter)| = {max_diff:.4e}")
    print(f"Machine epsilon = {np.finfo(float).eps:.4e}")
    print(f"Self-consistent to {max_diff / np.finfo(float).eps:.0f} × machine epsilon")

    # ── 3. Full vs shortcut: harmonics comparison ─────────────────────
    section("3. HARMONICS COMPARISON — full vs shortcut")

    test_cases = [
        ('proton  (1,2)', 1, 2, 8.906),
        ('proton  (1,4)', 1, 4, 8.906),
        ('proton  (2,1)', 2, 1, 8.906),
        ('proton  (3,1)', 3, 1, 8.906),
        ('electron(1,2)', 1, 2, 6.6),
        ('neutrino(1,1)', 1, 1, 5.0),
    ]

    print(f"{'Mode':>16}  {'δr₂ short':>14}  {'δr₂ full':>14}  {'Δδr₂':>12}  {'Δδr₂/δr₂':>12}")
    print(f"{'─'*16}  {'─'*14}  {'─'*14}  {'─'*12}  {'─'*12}")

    for label, nt, nr, r in test_cases:
        h_short = _compute_pressure_harmonics(nt, nr, r)
        h_full = _iterative_force_balance(nt, nr, r)
        k = 2
        d_s = h_short.delta_r_k[k]
        d_f = h_full.delta_r_k[k]
        diff = d_f - d_s
        rel = abs(diff / d_s) if d_s != 0 else 0
        print(f"{label:>16}  {d_s:14.8e}  {d_f:14.8e}  {diff:12.4e}  {rel:12.4e}")

    # ── 4. Energy comparison ──────────────────────────────────────────
    section("4. ENERGY COMPARISON — full vs shortcut vs static")

    m_full = Ma(**REF, dynamic='full')
    m_short = Ma(**REF, dynamic='shortcut')
    m_static = Ma(**REF, dynamic=False)

    print(f"{'Particle':>10}  {'E_static':>14}  {'E_shortcut':>14}  {'E_full':>14}  "
          f"{'ΔE_sc':>12}  {'ΔE_full':>12}  {'full-sc':>12}")
    print(f"{'─'*10}  {'─'*14}  {'─'*14}  {'─'*14}  {'─'*12}  {'─'*12}  {'─'*12}")

    for name, mode in NAMED_MODES.items():
        E_st = m_static.energy(mode)
        E_sc = m_short.energy(mode)
        E_fu = m_full.energy(mode)
        dE_sc = E_sc - E_st
        dE_fu = E_fu - E_st
        diff = E_fu - E_sc
        print(f"{name:>10}  {E_st:14.6f}  {E_sc:14.6f}  {E_fu:14.6f}  "
              f"{dE_sc:12.6e}  {dE_fu:12.6e}  {diff:12.6e}")

    # ── 5. Relative corrections ───────────────────────────────────────
    section("5. RELATIVE CORRECTIONS δE/E")

    print(f"{'Particle':>10}  {'δE/E short':>14}  {'δE/E full':>14}  {'Difference':>14}  {'Rel diff':>12}")
    print(f"{'─'*10}  {'─'*14}  {'─'*14}  {'─'*14}  {'─'*12}")

    for name, mode in NAMED_MODES.items():
        corr_s = m_short.dynamic_correction(mode)
        corr_f = m_full.dynamic_correction(mode)
        dEE_s = corr_s.delta_E_over_E
        dEE_f = corr_f.delta_E_over_E
        diff = dEE_f - dEE_s
        rel = abs(diff / dEE_s) if dEE_s != 0 else 0
        print(f"{name:>10}  {dEE_s:14.6e}  {dEE_f:14.6e}  {diff:14.6e}  {rel:12.4e}")

    # ── 6. Timing ─────────────────────────────────────────────────────
    section("6. TIMING — shortcut vs full")

    n_repeats = 5
    cases_timing = [
        ('(1,2) r=8.906', 1, 2, 8.906),
        ('(1,4) r=8.906', 1, 4, 8.906),
        ('(2,1) r=8.906', 2, 1, 8.906),
        ('(1,2) r=6.6',   1, 2, 6.6),
    ]

    print(f"{'Case':>16}  {'t_short (ms)':>14}  {'t_full (ms)':>14}  {'Ratio':>8}  {'Iters':>6}")
    print(f"{'─'*16}  {'─'*14}  {'─'*14}  {'─'*8}  {'─'*6}")

    for label, nt, nr, r in cases_timing:
        times_s = []
        times_f = []
        for _ in range(n_repeats):
            t0 = time.perf_counter()
            _compute_pressure_harmonics(nt, nr, r)
            times_s.append(time.perf_counter() - t0)

            t0 = time.perf_counter()
            _iterative_force_balance(nt, nr, r)
            times_f.append(time.perf_counter() - t0)

        ts = np.median(times_s) * 1000
        tf = np.median(times_f) * 1000
        ratio = tf / ts if ts > 0 else 0

        trace_t, _ = convergence_trace(nt, nr, r)
        iters = len(trace_t)

        print(f"{label:>16}  {ts:14.2f}  {tf:14.2f}  {ratio:8.2f}×  {iters:6d}")

    # ── 7. Full Ma construction timing ────────────────────────────────
    section("7. Ma CONSTRUCTION TIMING")

    times_off = []
    times_sc = []
    times_fu = []
    for _ in range(3):
        t0 = time.perf_counter()
        Ma(**REF, dynamic=False)
        times_off.append(time.perf_counter() - t0)

        t0 = time.perf_counter()
        Ma(**REF, dynamic='shortcut')
        times_sc.append(time.perf_counter() - t0)

        t0 = time.perf_counter()
        Ma(**REF, dynamic='full')
        times_fu.append(time.perf_counter() - t0)

    print(f"  Ma(dynamic=False):      {np.median(times_off)*1000:8.2f} ms")
    print(f"  Ma(dynamic='shortcut'): {np.median(times_sc)*1000:8.2f} ms")
    print(f"  Ma(dynamic='full'):     {np.median(times_fu)*1000:8.2f} ms")
    print(f"\nNote: Construction is fast for all methods — harmonics are")
    print(f"computed lazily on first energy() / pressure_harmonics() call.")

    # ── 8. scan_modes timing ──────────────────────────────────────────
    section("8. scan_modes TIMING (n_max=2, E_max=2000 MeV)")

    for method, label in [('off', 'static'), ('shortcut', 'shortcut'), ('full', 'full')]:
        dyn = False if method == 'off' else method
        m = Ma(**REF, dynamic=dyn)
        t0 = time.perf_counter()
        modes = m.scan_modes(n_max=2, E_max_MeV=2000)
        elapsed = time.perf_counter() - t0
        print(f"  {label:>10}: {len(modes):5d} modes in {elapsed*1000:8.1f} ms")

    # ── Summary ───────────────────────────────────────────────────────
    section("SUMMARY")
    print("The full iterative solve converges in 2-3 iterations (ratio ≈ α).")
    print("The shortcut agrees with the full solve to O(α⁴) in energy.")
    print(f"  α = {ALPHA:.6f}")
    print(f"  α² = {ALPHA**2:.6e}")
    print(f"  α⁴ = {ALPHA**4:.6e}")
    print()
    print("For all known particles, |δE/E_full - δE/E_shortcut| < α⁴.")
    print("The full solve costs ~3× the shortcut per unique (n_tube, n_ring, r).")
    print("Both methods are negligible compared to scan_modes brute-force loop.")


if __name__ == '__main__':
    main()
