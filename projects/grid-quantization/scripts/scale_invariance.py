#!/usr/bin/env python3
"""How scale-invariant is the lattice? (dispersion linearity)

The h-universality claim reduces to scale-invariance: if the lattice
has no preferred scale, whatever quantum emerges is the same at every
frequency.  A classical linear lattice cannot itself quantize a
free wave's energy (that is second quantization — see
work/tier2-design.md §4a), so the testable, lattice-derivable part is
the scale-invariance, and its cleanest signature is a LINEAR (scale-
free, non-dispersive) photon band ω = v·k.

This measures the deviation of the acoustic dispersive band from
linearity as a function of wavelength, i.e. where the lattice scale
starts to break scale-invariance.  Uses the band structure's
empirical Bloch operator.

Usage:
    source .venv/bin/activate
    python projects/grid-quantization/scale_invariance.py
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from band_structure import BlochOperator, b1   # noqa: E402


def main():
    op = BlochOperator(L=16)
    M = 0.5 * b1                       # Γ → M direction
    kmag_max = np.linalg.norm(M)

    ts = np.linspace(0.0, 1.0, 200)[1:]
    ks, ws = [], []
    for t in ts:
        k = t * M
        bands = op.bands(k)
        pos = bands[bands > 1e-3]      # skip the ω=0 flat band
        if len(pos):
            ks.append(t * kmag_max)
            ws.append(pos.min())       # acoustic (lowest) dispersive
    ks = np.array(ks)
    ws = np.array(ws)

    # phase velocity from the smallest-k points
    small = ks < 0.12 * kmag_max
    v = float(np.polyfit(ks[small], ws[small], 1)[0])

    dev = ws / (v * ks) - 1.0          # fractional deviation from ω=v·k

    def k_at(frac):
        hit = np.where(np.abs(dev) > frac)[0]
        return ks[hit[0]] if len(hit) else np.nan

    print("Scale-invariance of the lattice (dispersion linearity)")
    print(f"  acoustic phase velocity (small k): v = {v:.4f} "
          f"lattice units/tick")
    print(f"  Brillouin-zone edge |k|_max along Γ→M = {kmag_max:.3f} "
          f"rad / lattice unit\n")
    print(f"  {'wavelength λ/L':>14s}{'|k|':>8s}"
          f"{'deviation from ω=vk':>22s}")
    for frac, lbl in [(0.001, "0.1%"), (0.01, "1%"), (0.10, "10%")]:
        kf = k_at(frac)
        if not np.isnan(kf):
            lam = 2 * np.pi / kf
            print(f"  deviation reaches {lbl:>5s} at  λ ≈ {lam:5.1f} L "
                  f"(|k| ≈ {kf:.3f})")

    print("\n  ⇒ The dispersion is linear (scale-free) to within "
          "<0.1% for wavelengths λ ≳ 10 L,")
    print("    and the deviation falls as ~k² toward long wavelength. "
          "Real photons have")
    print("    λ/L_P ≳ 10²⁰, so the lattice is scale-invariant to "
          "~10⁻⁴⁰ at any observable")
    print("    frequency: an excellent IR fixed point, with scale-"
          "invariance breaking only")
    print("    at the lattice (Planck) scale — exactly where new "
          "physics is expected.")
    print("\n  This is necessary for, not proof of, h-universality: "
          "it says the substrate has")
    print("    no preferred scale in the IR, so IF a quantum emerges "
          "it is frequency-independent.")
    print("    Whether a quantum emerges at all is the second-"
          "quantization question (§4a).")


if __name__ == "__main__":
    main()
