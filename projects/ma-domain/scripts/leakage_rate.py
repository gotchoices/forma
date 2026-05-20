#!/usr/bin/env python3
"""
leakage_rate.py - machinery check for the resonance-pole leakage rate.

Validates the claim of mode-stability.md (sec.4, sec.8 Phase 1): a mode's
decay rate Gamma obtained from the complex resonance pole of the Green's
function reduces, in the weak-coupling limit, to the Fermi-golden-rule (FGR)
expression - and the two diverge once the coupling is no longer weak.

MODEL - the flat-band Friedrichs model.
  One discrete state |0> at energy eps0, coupled with uniform amplitude to a
  flat continuum band [e_lo, e_hi]. The single raw coupling is
  gamma = v^2 * rho  (coupling amplitude squared x band density of states).
  This is the minimal system in which both rate methods apply:

    method A  resonance pole : Gamma = -2 Im(E_pole), with E_pole the root of
        E - eps0 - Sigma_II(E) = 0 on the second Riemann sheet, where
        Sigma_II(E) = gamma[ln(E-e_lo) - ln(E-e_hi)] - 2*pi*i*gamma .

    method B  Fermi golden rule : Gamma_FGR = 2*pi*gamma .

  It is a MACHINERY check: it validates the pole-finder and the FGR evaluator
  against each other on a model with a known answer, before candidate-specific
  junction operators V_k and densities of states are plugged in
  (leakage-rate.md sec.3). Units: hbar = 1.

INPUTS  (argparse): the continuum band edges, the discrete-state energy, and
        the list of raw couplings gamma to sweep.
OUTPUTS: a table Gamma_FGR vs Gamma_pole vs ratio over the gamma sweep,
        printed to stdout and written to outputs/leakage_rate.txt.
"""

import argparse
import math
import os

import numpy as np


def sigma_II(E, gamma, e_lo, e_hi):
    """Second-sheet self-energy of the flat-band Friedrichs model."""
    return gamma * (np.log(E - e_lo) - np.log(E - e_hi)) - 2j * math.pi * gamma


def sigma_II_deriv(E, gamma, e_lo, e_hi):
    """d/dE of sigma_II  (the -2*pi*i*gamma term is constant)."""
    return gamma * (1.0 / (E - e_lo) - 1.0 / (E - e_hi))


def find_pole(gamma, eps0, e_lo, e_hi, guess, tol=1e-13, maxit=200):
    """Complex-Newton root of  f(E) = E - eps0 - Sigma_II(E)   (method A)."""
    E = complex(guess)
    for _ in range(maxit):
        f = E - eps0 - sigma_II(E, gamma, e_lo, e_hi)
        fp = 1.0 - sigma_II_deriv(E, gamma, e_lo, e_hi)
        step = f / fp
        E -= step
        if abs(step) < tol:
            return E
    raise RuntimeError("pole search did not converge for gamma=%g" % gamma)


def gamma_fgr(gamma):
    """Fermi-golden-rule rate (method B): 2*pi*gamma for the flat band."""
    return 2.0 * math.pi * gamma


def run(eps0, e_lo, e_hi, gammas):
    """Sweep the raw coupling; return one result row per gamma."""
    rows = []
    guess = complex(eps0, -math.pi * gammas[0])  # FGR estimate of the pole
    for g in gammas:
        pole = find_pole(g, eps0, e_lo, e_hi, guess)
        guess = pole  # continuation: seed the next gamma with this pole
        g_pole = -2.0 * pole.imag
        g_fgr = gamma_fgr(g)
        rows.append({
            "gamma": g,
            "g_fgr": g_fgr,
            "g_pole": g_pole,
            "ratio": g_pole / g_fgr,
            "shift": pole.real - eps0,
        })
    return rows


def format_report(eps0, e_lo, e_hi, rows):
    """Render the sweep as a printable report with a verdict."""
    lines = []
    lines.append("=" * 78)
    lines.append("leakage_rate.py  -  resonance-pole vs Fermi-golden-rule machinery check")
    lines.append("flat-band Friedrichs model   (hbar = 1)")
    lines.append("=" * 78)
    lines.append("")
    lines.append("  discrete state eps0 = %+.4f    continuum band [%+.4f, %+.4f]"
                 % (eps0, e_lo, e_hi))
    in_band = e_lo < eps0 < e_hi
    lines.append("  eps0 is %s the band  ->  %s"
                 % ("inside" if in_band else "OUTSIDE",
                    "a genuine resonance" if in_band
                    else "WARNING: no on-shell continuum, expect Gamma = 0"))
    lines.append("")
    lines.append("  method A  resonance pole    : Gamma = -2 Im(E_pole)")
    lines.append("  method B  Fermi golden rule : Gamma_FGR = 2*pi*gamma")
    lines.append("")
    hdr = "  %10s  %15s  %15s  %13s  %13s" % (
        "gamma", "Gamma_FGR (B)", "Gamma_pole (A)", "A / B", "level shift")
    lines.append(hdr)
    lines.append("  " + "-" * (len(hdr) - 2))
    for r in rows:
        lines.append("  %10.5f  %15.7e  %15.7e  %13.9f  %+13.5e" % (
            r["gamma"], r["g_fgr"], r["g_pole"], r["ratio"], r["shift"]))
    lines.append("")
    weak, strong = rows[0], rows[-1]
    dev_weak = abs(weak["ratio"] - 1.0)
    dev_strong = abs(strong["ratio"] - 1.0)
    # leading correction:  A/B ~ 1 + c*gamma  at small gamma
    c_est = [(r["ratio"] - 1.0) / r["gamma"] for r in rows[:3]]
    c_lead = c_est[0]
    c_stable = all(abs(c - c_lead) < 0.1 * abs(c_lead) for c in c_est)
    lines.append("  Reading:")
    lines.append("   - weak coupling  (gamma = %.0e): A/B = %.9f   (deviation %.1e)"
                 % (weak["gamma"], weak["ratio"], dev_weak))
    lines.append("   - strong coupling (gamma = %.5f): A/B = %.6f   (deviation %.1e)"
                 % (strong["gamma"], strong["ratio"], dev_strong))
    lines.append("   - leading correction: A/B = 1 + c*gamma  with  c = %.4f  (%s"
                 " across the low-gamma rows)"
                 % (c_lead, "stable" if c_stable else "NOT stable"))
    lines.append("")
    if dev_weak < 1e-3 and c_stable and dev_strong > 10.0 * dev_weak:
        lines.append("  MACHINERY VALIDATED: the resonance pole reduces to FGR as")
        lines.append("  gamma -> 0 (A/B -> 1, linearly), and the two separate as the")
        lines.append("  coupling grows. FGR is the leading term; the pole supplies the")
        lines.append("  O(gamma) and higher corrections - exactly the relation")
        lines.append("  mode-stability.md sec.4 posits. Pole-finder and FGR evaluator")
        lines.append("  are mutually consistent on a model with a known answer.")
    else:
        lines.append("  CHECK: expected A/B -> 1 linearly at weak coupling and")
        lines.append("  divergence at strong; inspect the table before trusting it.")
    lines.append("=" * 78)
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--eps0", type=float, default=0.0,
                   help="discrete-state energy (default 0.0, the band centre)")
    p.add_argument("--e-lo", type=float, default=-1.0,
                   help="lower continuum band edge (default -1.0)")
    p.add_argument("--e-hi", type=float, default=1.0,
                   help="upper continuum band edge (default +1.0)")
    p.add_argument("--gammas", type=float, nargs="+",
                   default=[1e-5, 1e-4, 1e-3, 1e-2, 3e-2, 1e-1, 2e-1, 3e-1],
                   help="raw couplings gamma = v^2*rho to sweep")
    default_out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "..", "outputs", "leakage_rate.txt")
    p.add_argument("--outfile", default=default_out,
                   help="report output path")
    args = p.parse_args()

    gammas = sorted(args.gammas)
    rows = run(args.eps0, args.e_lo, args.e_hi, gammas)
    report = format_report(args.eps0, args.e_lo, args.e_hi, rows)
    print(report)

    outpath = os.path.abspath(args.outfile)
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, "w") as fh:
        fh.write(report + "\n")
    print("\nwritten: %s" % outpath)


if __name__ == "__main__":
    main()
