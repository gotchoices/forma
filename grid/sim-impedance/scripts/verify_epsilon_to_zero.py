#!/usr/bin/env python3
"""
Quick verification: does coincidence rate → 0 as tolerance → 0?

Uses the Track 1 (2D-in-2D) and Track 3 (wye-jack angular) setups
with epsilon pushed to very small values.
"""

import numpy as np
from scipy.spatial import cKDTree

# ── Track 1: 2D rotated lattices, node coincidence ──────────────

def triangular_lattice(n_rows, n_cols):
    pts = []
    for row in range(n_rows):
        for col in range(n_cols):
            x = col + 0.5 * (row % 2)
            y = row * np.sqrt(3) / 2
            pts.append((x, y))
    pts = np.array(pts)
    pts -= pts.mean(axis=0)
    return pts

def rotate(pts, theta_deg):
    t = np.radians(theta_deg)
    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])
    return pts @ R.T

def count_edge_coincidences(pts_a, pts_b, L=1.0, eps=0.02):
    tree_b = cKDTree(pts_b)
    outer = tree_b.query_ball_point(pts_a, L + eps)
    n_hits = 0
    for i, neighbours in enumerate(outer):
        if not neighbours:
            continue
        dists = np.linalg.norm(pts_b[neighbours] - pts_a[i], axis=1)
        n_hits += np.count_nonzero(dists >= L - eps)
    per_node = n_hits / len(pts_a)
    return per_node, per_node / 6.0

def count_node_coincidences(pts_a, pts_b, eps=0.02):
    """Count how many nodes in A are within eps of any node in B."""
    tree_b = cKDTree(pts_b)
    dists, _ = tree_b.query(pts_a)
    n_hits = np.count_nonzero(dists < eps)
    return n_hits, n_hits / len(pts_a)

# ── Track 3 setup: wye-jack angular alignment ───────────────────

JACK = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=float) / np.sqrt(3)

def wye_directions(theta, phi, psi):
    ct, st = np.cos(theta), np.sin(theta)
    cp, sp = np.cos(phi), np.sin(phi)
    n = np.array([st * cp, st * sp, ct])
    e1 = np.array([ct * cp, ct * sp, -st])
    e2 = np.cross(n, e1)
    e1 = e1 / (np.linalg.norm(e1) + 1e-30)
    e2 = e2 / (np.linalg.norm(e2) + 1e-30)
    dirs = []
    for k in range(3):
        angle = psi + k * 2 * np.pi / 3
        d = np.cos(angle) * e1 + np.sin(angle) * e2
        dirs.append(d)
    return np.array(dirs)

def alignment_fraction(n_theta=90, n_phi=180, n_psi=60, tol_deg=0.5):
    """Fraction of (θ,φ,ψ) orientations with ≥1 wye-jack alignment."""
    thetas = np.linspace(0.01, np.pi - 0.01, n_theta)
    phis = np.linspace(0, 2 * np.pi, n_phi, endpoint=False)
    psis = np.linspace(0, 2 * np.pi / 3, n_psi, endpoint=False)
    tol_rad = np.radians(tol_deg)
    count = 0
    total = n_theta * n_phi * n_psi
    for theta in thetas:
        for phi in phis:
            for psi in psis:
                wye = wye_directions(theta, phi, psi)
                aligned = False
                for wi in range(3):
                    for ji in range(4):
                        dot = abs(np.dot(wye[wi], JACK[ji]))
                        dot = min(dot, 1.0)
                        if np.arccos(dot) < tol_rad:
                            aligned = True
                            break
                    if aligned:
                        break
                if aligned:
                    count += 1
    return count / total


def main():
    print("=" * 65)
    print("  VERIFICATION: coincidence rate → 0 as ε → 0 ?")
    print("=" * 65)

    # ── Test 1: Track 1 style — edge coincidence (2D-in-2D) ──
    print("\n── Test 1: 2D rotated lattices, edge coincidence ──")
    print("  (Two triangular lattices rotated by 13.2°, count edges")
    print("   separated by 1 ± ε)\n")

    pts_a = triangular_lattice(80, 80)
    R_cut = 80 * 0.35
    mask = np.linalg.norm(pts_a, axis=1) < R_cut
    pts_a_cut = pts_a[mask]
    pts_b_cut = rotate(pts_a, 13.2)[mask]

    epsilons = [0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001,
                0.0005, 0.0002, 0.0001]

    print(f"  {'ε':>10s}  {'per_node':>10s}  {'rate/6':>12s}  {'1/rate':>10s}")
    print("  " + "─" * 48)
    for eps in epsilons:
        pn, ratio = count_edge_coincidences(pts_a_cut, pts_b_cut, L=1.0, eps=eps)
        inv = 1.0 / ratio if ratio > 0 else float('inf')
        print(f"  {eps:10.4f}  {pn:10.4f}  {ratio:12.8f}  {inv:10.1f}")

    # ── Test 2: Track 1 style — node coincidence (2D-in-2D) ──
    print("\n── Test 2: 2D rotated lattices, node coincidence ──")
    print("  (How many A-nodes land within ε of a B-node?)\n")

    print(f"  {'ε':>10s}  {'n_hits':>8s}  {'fraction':>12s}")
    print("  " + "─" * 36)
    for eps in epsilons:
        n_hits, frac = count_node_coincidences(pts_a_cut, pts_b_cut, eps=eps)
        print(f"  {eps:10.4f}  {n_hits:8d}  {frac:12.8f}")

    # ── Test 3: Track 3 style — angular alignment fraction ──
    print("\n── Test 3: Wye-jack angular alignment (Track 3 style) ──")
    print("  (Fraction of orientations with ≥1 edge aligned within tol°)")
    print("  Grid: 45θ × 90φ × 30ψ (smaller grid for speed)\n")

    tol_degs = [5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05]

    print(f"  {'tol (°)':>10s}  {'fraction':>12s}  {'1/frac':>10s}  {'1/137':>10s}")
    print("  " + "─" * 50)
    for tol in tol_degs:
        frac = alignment_fraction(n_theta=45, n_phi=90, n_psi=30, tol_deg=tol)
        inv = 1.0 / frac if frac > 0 else float('inf')
        print(f"  {tol:10.2f}  {frac:12.8f}  {inv:10.1f}  {137.036:10.1f}")

    # ── Conclusion ──
    print("\n" + "=" * 65)
    print("  CONCLUSION")
    print("=" * 65)
    print("""
  If all three tests show rate → 0 as ε → 0, this confirms that
  there is NO intrinsic coincidence rate.  The "1/137" that appeared
  in earlier tracks was an artifact of the chosen tolerance, not a
  geometric constant.

  The lattices are incommensurate: at generic orientations, zero
  nodes/edges coincide exactly (ε = 0 gives rate = 0).
""")


if __name__ == "__main__":
    main()
