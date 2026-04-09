"""
R52 Track 4a: Pairwise antinode Coulomb energy.

Tests the simplest version of the three-phase sign hypothesis.

HYPOTHESIS:
The sign of the residual magnetic moment correction is determined by
the mode's ring-winding topology:
  - n_ring = 2 (electron, two-phase): additive correction (δμ > 0)
  - n_ring = 3 (proton, three-phase): subtractive correction (δμ < 0)

METHOD:
1. Place 2*n_ring point charges at antinode positions θ_k = k*π/n_ring
   around the ring (at fixed tube angle θ_tube = 0).
2. Each antinode carries sign s_k = (-1)^k from cos(n_ring * θ_k).
3. Compute pairwise Coulomb energy: U = (1/2) Σ_{i≠j} s_i s_j / d_{ij}
4. Compare U(n_ring=2) and U(n_ring=3).

CONVENTIONS:
- Lib convention: n1 = tube (poloidal), n2 = ring (toroidal)
- This script uses n_ring = n2 throughout

ASSUMPTIONS (frozen for this sub-track):
- Standing wave basis: ψ ∝ cos(n_tube * θ_tube) * cos(n_ring * θ_ring)
- Antinode positions: θ_ring_k = k * π / n_ring, k = 0..2*n_ring-1
- Antinode signs: s_k = (-1)^k (alternating)
- Tube angle: θ_tube = 0 (outer equator) for all antinodes
- Distance: chord through 3D space, using torus embedding with major
  radius R and minor radius a = r * R
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from lib.embedded import EmbeddedSheet


# ── Antinode positions ─────────────────────────────────────────────

def antinode_positions(sheet, n_ring, theta_tube=0.0):
    """
    Compute 3D positions of the 2*n_ring antinodes around the ring.

    Antinodes are at θ_ring_k = k * π / n_ring for k = 0..2*n_ring-1.
    """
    n_anti = 2 * n_ring
    theta_ring = np.array([k * np.pi / n_ring for k in range(n_anti)])
    theta_tubes = np.full(n_anti, theta_tube)
    pos = sheet.torus_point(theta_tubes, theta_ring)
    return pos


def antinode_signs(n_ring):
    """Alternating signs for the 2*n_ring antinodes: +-+-+-..."""
    return np.array([(-1) ** k for k in range(2 * n_ring)])


# ── Pairwise Coulomb energy ─────────────────────────────────────────

def pairwise_coulomb(positions, signs, eps=1e-12):
    """
    Compute U = (1/2) Σ_{i ≠ j} (s_i * s_j) / d_{ij}

    Sign of U:
    - Positive: same-sign pairs dominate (constructive)
    - Negative: opposite-sign pairs dominate (destructive)
    """
    n = len(positions)
    U = 0.0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d = np.linalg.norm(positions[i] - positions[j])
            U += 0.5 * signs[i] * signs[j] / max(d, eps)
    return U


def pairwise_decomposition(positions, signs):
    """
    Decompose U by separation distance bin.

    Returns a list of (separation, count, sign_sum, contribution)
    tuples, sorted by separation.
    """
    n = len(positions)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            d = np.linalg.norm(positions[i] - positions[j])
            ss = signs[i] * signs[j]
            pairs.append((d, ss, ss / d))
    pairs.sort(key=lambda x: x[0])
    return pairs


# ── Run the sign test ──────────────────────────────────────────────

def run_sign_test(r_aspect, R=1.0, label=""):
    """
    Compute U for n_ring = 2 (electron) and n_ring = 3 (proton)
    at the same aspect ratio r = a/R.
    """
    a = r_aspect * R
    L_tube = 2 * np.pi * a
    L_ring = 2 * np.pi * R
    sheet = EmbeddedSheet(L_tube=L_tube, L_ring=L_ring)

    results = {}
    for n_ring in [2, 3]:
        pos = antinode_positions(sheet, n_ring, theta_tube=0.0)
        signs = antinode_signs(n_ring)
        U = pairwise_coulomb(pos, signs)
        pairs = pairwise_decomposition(pos, signs)

        results[n_ring] = {
            'U': U,
            'pos': pos,
            'signs': signs,
            'pairs': pairs,
        }

    print(f"\n── {label} (r = a/R = {r_aspect}) ──")
    print(f"  R = {R}, a = {a}")

    for n_ring in [2, 3]:
        r = results[n_ring]
        n_anti = 2 * n_ring
        print(f"\n  n_ring = {n_ring}  ({n_anti} antinodes)")
        print(f"    Signs:    {r['signs']}")
        print(f"    Total U:  {r['U']:+.6f}")
        print(f"    Decomposition by separation:")
        # Group by approximate separation
        for d, ss, contrib in r['pairs']:
            sign_str = "++/--" if ss > 0 else "+/-"
            print(f"      d = {d:.4f}  ({sign_str})  contribution = {contrib:+.4f}")

    # Check sign pattern
    U2 = results[2]['U']
    U3 = results[3]['U']
    print(f"\n  Sign test:")
    print(f"    U(n=2) = {U2:+.6f}")
    print(f"    U(n=3) = {U3:+.6f}")
    if U2 > 0 and U3 < 0:
        print(f"    *** PREDICTED PATTERN: + for n=2, - for n=3 ***")
    elif U2 < 0 and U3 > 0:
        print(f"    REVERSED pattern: - for n=2, + for n=3")
    else:
        print(f"    SAME-SIGN: both have sign({np.sign(U2)})")

    return results


# ── Aspect-ratio scan ──────────────────────────────────────────────

def aspect_scan(r_values):
    """Scan U vs aspect ratio for both modes."""
    R = 1.0
    U2_arr = np.zeros(len(r_values))
    U3_arr = np.zeros(len(r_values))

    for i, r in enumerate(r_values):
        a = r * R
        L_tube = 2 * np.pi * a
        L_ring = 2 * np.pi * R
        sheet = EmbeddedSheet(L_tube=L_tube, L_ring=L_ring)

        for n_ring, arr in [(2, U2_arr), (3, U3_arr)]:
            pos = antinode_positions(sheet, n_ring)
            signs = antinode_signs(n_ring)
            arr[i] = pairwise_coulomb(pos, signs)

    return U2_arr, U3_arr


# ── Main ───────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("R52 Track 4a: Pairwise antinode Coulomb energy")
    print("=" * 70)
    print(__doc__)

    print("\n" + "=" * 70)
    print("PART 1: Sign test at multiple aspect ratios")
    print("=" * 70)

    # Test at three representative aspect ratios
    for r in [0.5, 2.0, 8.906]:
        if r == 8.906:
            label = "Proton aspect ratio (R27 F18)"
        elif r == 0.5:
            label = "Thin-tube limit"
        else:
            label = f"r = {r}"
        run_sign_test(r, label=label)

    print("\n" + "=" * 70)
    print("PART 2: Aspect ratio scan")
    print("=" * 70)

    r_values = np.linspace(0.1, 20.0, 50)
    U2, U3 = aspect_scan(r_values)

    print(f"\n  {'r':>8s}  {'U(n=2)':>12s}  {'U(n=3)':>12s}  {'U2/U3':>10s}")
    print("  " + "─" * 50)
    for i in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]:
        ratio = U2[i] / U3[i] if abs(U3[i]) > 1e-12 else float('inf')
        print(f"  {r_values[i]:8.3f}  {U2[i]:+12.6f}  {U3[i]:+12.6f}  {ratio:+10.4f}")

    # Check if signs ever differ
    sign_diff = np.sum(np.sign(U2) != np.sign(U3))
    print(f"\n  Aspect ratios with sign difference: {sign_diff} / {len(r_values)}")
    if sign_diff > 0:
        diff_idx = np.where(np.sign(U2) != np.sign(U3))[0]
        print(f"  At r = {r_values[diff_idx[0]]:.3f}: U2={U2[diff_idx[0]]:+.4f}, "
              f"U3={U3[diff_idx[0]]:+.4f}")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.plot(r_values, U2, 'b-', label='n_ring = 2 (electron)')
    ax.plot(r_values, U3, 'r-', label='n_ring = 3 (proton)')
    ax.axhline(0, color='k', linestyle='--', alpha=0.3)
    ax.set_xlabel('Aspect ratio r = a/R')
    ax.set_ylabel('Coulomb self-energy U')
    ax.set_title('Pairwise antinode Coulomb energy vs aspect ratio')
    ax.legend()
    ax.grid(alpha=0.3)

    ax = axes[1]
    ax.plot(r_values, np.sign(U2), 'bo-', label='sign(U2)', markersize=4)
    ax.plot(r_values, np.sign(U3), 'r^-', label='sign(U3)', markersize=4)
    ax.set_xlabel('Aspect ratio r = a/R')
    ax.set_ylabel('Sign')
    ax.set_title('Sign of U vs aspect ratio')
    ax.set_ylim(-1.5, 1.5)
    ax.legend()
    ax.grid(alpha=0.3)

    plt.tight_layout()
    out = Path(__file__).parent.parent / "track4a_results.png"
    plt.savefig(out, dpi=120)
    print(f"\n  Plot saved to {out}")

    # ── Summary ──
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    # Take the proton aspect ratio result
    a_p = 8.906
    L_tube_p = 2 * np.pi * a_p
    L_ring_p = 2 * np.pi
    sheet_p = EmbeddedSheet(L_tube=L_tube_p, L_ring=L_ring_p)

    pos2 = antinode_positions(sheet_p, 2)
    pos3 = antinode_positions(sheet_p, 3)
    s2 = antinode_signs(2)
    s3 = antinode_signs(3)
    U2_p = pairwise_coulomb(pos2, s2)
    U3_p = pairwise_coulomb(pos3, s3)

    print(f"\nAt proton aspect ratio (r = 8.906):")
    print(f"  n_ring = 2:  U = {U2_p:+.6f}")
    print(f"  n_ring = 3:  U = {U3_p:+.6f}")

    if U2_p > 0 and U3_p < 0:
        print("\n  *** SUCCESS: predicted sign pattern (+ for n=2, - for n=3) ***")
        print("  *** Sub-track 4a CONFIRMS the three-phase rule ***")
    elif U2_p < 0 and U3_p > 0:
        print("\n  REVERSED: U2 < 0 and U3 > 0")
        print("  Topology determines sign but with opposite convention")
    elif np.sign(U2_p) == np.sign(U3_p):
        print(f"\n  SAME-SIGN: both U2 and U3 are {np.sign(U2_p):+.0f}")
        print("  Sub-track 4a does NOT differentiate the modes by sign")
        print("  This is the expected outcome for the simplest pairwise picture")
        print("  Move to sub-track 4b (loop mutual inductance) and 4c (continuous)")


if __name__ == "__main__":
    main()
