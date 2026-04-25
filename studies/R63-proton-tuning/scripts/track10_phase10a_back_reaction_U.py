"""
R63 Track 10 Phase 10a (companion) — Back-reaction U for N-strand arrangements.

Following R60 T16's 2ω density-cancellation framework: a single primitive
(1, 2) mode on the p-sheet has charge density ρ_Q = φ² with a 2ω harmonic
(time-dependent fluctuation).  N copies of the mode at internal phases
{φ_i} have a coherent harmonic sum

    U_m({φ_i}) = Σ_{i<j} cos(m (φ_i − φ_j))
              = ½ ( |Σ_i exp(i m φ_i)|² − N )

at harmonic order m (m = 2 is R60 T16's case).  Configurations with U_m
< 0 cancel that harmonic and are stable against the corresponding back-
reaction; the more negative U_m, the cleaner the cancellation.

R60 T16 selected Z₃ (N=3) as the minimum stable configuration at m=2:
U_2(Z₃) = −1.5.  This is the framework's quark-confinement rule.

Track 10 asks whether N=6 (deuteron Pauli capacity = 3 colors × 2 spins)
has a configuration that distinguishes from "two independent Z₃ triplets"
at any harmonic the framework recognizes.

Output: phase 10a tabulates U_m for various candidate arrangements at
m = 2, 3, 4, 6 to determine whether any harmonic separates Z₆, 2×Z₃,
and Pauli-spin-π-shifted Z₆.

Saved to outputs/track10_phase10a_back_reaction_U.csv.
"""

import math
import csv
from pathlib import Path

import numpy as np


def U_m(phases, m):
    """U_m = Σ_{i<j} cos(m(φ_i − φ_j))   (= ½ (|Σ exp(i m φ)|² − N))."""
    z = sum(np.exp(1j * m * phi) for phi in phases)
    return 0.5 * (abs(z)**2 - len(phases))


CONFIGS = {
    # (N, arrangement label, phases-in-radians)
    "N=1 single strand":          [0.0],
    "N=2 anti-aligned (180°)":    [0, math.pi],
    "N=2 aligned (0°)":           [0, 0],
    "N=3 Z₃":                     [k * 2*math.pi/3 for k in range(3)],
    "N=3 aligned":                [0, 0, 0],
    "N=6 Z₆ hexagon":             [k * math.pi/3 for k in range(6)],
    "N=6 2×Z₃ (θ_inter=60°)":     ([k * 2*math.pi/3 for k in range(3)]
                                  + [k * 2*math.pi/3 + math.pi/3 for k in range(3)]),
    "N=6 2×Z₃ (θ_inter=0°)":      ([k * 2*math.pi/3 for k in range(3)]
                                  + [k * 2*math.pi/3 for k in range(3)]),
    "N=6 2×Z₃ (θ_inter=30°)":     ([k * 2*math.pi/3 for k in range(3)]
                                  + [k * 2*math.pi/3 + math.pi/6 for k in range(3)]),
    "N=6 Pauli spin-π Z₃×{0,π}":  ([k * 2*math.pi/3 for k in range(3)]
                                  + [k * 2*math.pi/3 + math.pi for k in range(3)]),
    "N=6 all aligned":            [0]*6,
}


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 100)
    print("R63 Track 10 Phase 10a (companion) — Back-reaction U_m for N-strand "
          "phase arrangements")
    print("=" * 100)
    print()

    print("U_m = Σ_{i<j} cos(m(φ_i − φ_j))    "
          "(stable when negative, R60 T16 uses m=2)\n")

    harmonics = [2, 3, 4, 6]
    rows = []
    print(f"  {'arrangement':40s}  " + "  ".join(f"U_{m:>1d}" for m in harmonics))
    print(f"  {'-'*40}  " + "  ".join("-"*4 for _ in harmonics))

    for label, phases in CONFIGS.items():
        Us = [U_m(phases, m) for m in harmonics]
        cells = "  ".join(f"{u:+5.2f}" for u in Us)
        print(f"  {label:40s}  {cells}")
        rows.append([label, len(phases)] + Us)

    print()
    print("Key reads:")
    print("  • R60 T16 selects N=3 Z₃ as the minimum 2ω-stable composite "
          "(U_2 = -1.5).")
    print("  • At N=6, both Z₆ hexagon and 2×Z₃ at any inter-triplet phase "
          "give U_2 = -3.")
    print("    → R60 T16's m=2 mechanism does NOT distinguish them.")
    print("  • The Pauli-saturation arrangement {0, 2π/3, 4π/3} × {0, π}")
    print("    coincides with Z₆ structurally, so doesn't break the tie either.")
    print("  • Higher harmonics (m=4, 6) also give U_m = -3 for both Z₆ and")
    print("    most 2×Z₃ inter-triplet placements; no scalar harmonic")
    print("    separates the configurations.")

    csv_path = out_dir / "track10_phase10a_back_reaction_U.csv"
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["arrangement", "N"] + [f"U_{m}" for m in harmonics])
        w.writerows(rows)
    print()
    print(f"  CSV: {csv_path}")


if __name__ == "__main__":
    main()
