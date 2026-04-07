#!/usr/bin/env python3
"""
Track 3, Step 1: Single-node analysis.

Place one diamond jack (4 edges, tetrahedral, 109.47°) and one
hexagonal wye (3 edges, planar, 120°) at the same origin.

For each orientation of the wye plane (θ, φ) and twist (ψ),
check whether any wye edge direction aligns exactly with any
jack edge direction.

The jack directions (tetrahedral vertices, normalized):
  d₁ = (+1,+1,+1)/√3
  d₂ = (+1,−1,−1)/√3
  d₃ = (−1,+1,−1)/√3
  d₄ = (−1,−1,+1)/√3

A wye edge in a plane with normal n̂(θ,φ), twisted by ψ, is
a unit vector in that plane.  Three such vectors at 120°
separation.

Alignment means: ê_wye = ±ê_jack (parallel or anti-parallel,
since edges are undirected).
"""

import numpy as np
from itertools import product
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).parent.parent / "output"
OUT.mkdir(exist_ok=True)

# ── The four jack directions (tetrahedral) ────────────────────

JACK = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=float) / np.sqrt(3)


def wye_directions(theta, phi, psi):
    """Compute the three wye edge directions for a plane with
    normal n̂(θ, φ) and in-plane twist ψ.

    Returns (3, 3) array of unit vectors.
    """
    # Normal vector
    ct, st = np.cos(theta), np.sin(theta)
    cp, sp = np.cos(phi), np.sin(phi)
    n = np.array([st * cp, st * sp, ct])

    # Two orthogonal vectors in the plane
    # e1 = d/dθ of n̂ (lies in plane, points "south")
    e1 = np.array([ct * cp, ct * sp, -st])
    # e2 = n × e1 (lies in plane, points "east")
    e2 = np.cross(n, e1)

    # Normalize (should already be unit, but be safe)
    e1 = e1 / (np.linalg.norm(e1) + 1e-30)
    e2 = e2 / (np.linalg.norm(e2) + 1e-30)

    # Three wye directions at 120° separation, twisted by ψ
    dirs = []
    for k in range(3):
        angle = psi + k * 2 * np.pi / 3
        d = np.cos(angle) * e1 + np.sin(angle) * e2
        dirs.append(d)

    return np.array(dirs)


def alignment_score(theta, phi, psi, tol_deg=0.1):
    """For a given (θ, φ, ψ), check how many wye edges align
    with jack edges.

    Returns:
        n_aligned: number of wye-jack edge pairs that are
                   parallel (within tol_deg)
        best_angle: smallest angle between any wye-jack pair
        details: list of (wye_idx, jack_idx, angle_deg) for
                 all aligned pairs
    """
    wye = wye_directions(theta, phi, psi)
    tol_rad = np.radians(tol_deg)

    details = []
    for wi in range(3):
        for ji in range(4):
            # Angle between wye edge and jack edge
            # (use absolute dot product — edges are undirected)
            dot = abs(np.dot(wye[wi], JACK[ji]))
            dot = min(dot, 1.0)  # clamp for numerical safety
            angle = np.arccos(dot)
            if angle < tol_rad:
                details.append((wi, ji, np.degrees(angle)))

    n_aligned = len(details)
    # Best (smallest) angle across ALL pairs
    all_angles = []
    for wi in range(3):
        for ji in range(4):
            dot = abs(np.dot(wye[wi], JACK[ji]))
            dot = min(dot, 1.0)
            all_angles.append(np.degrees(np.arccos(dot)))
    best_angle = min(all_angles)

    return n_aligned, best_angle, details


def sweep_coarse(n_theta=180, n_phi=360, n_psi=120, tol_deg=0.5):
    """Coarse sweep of (θ, φ, ψ) space.

    At each point, compute the number of aligned edges and the
    best (smallest) misalignment angle.

    Returns arrays for analysis.
    """
    thetas = np.linspace(0.01, np.pi - 0.01, n_theta)
    phis = np.linspace(0, 2 * np.pi, n_phi, endpoint=False)
    psis = np.linspace(0, 2 * np.pi / 3, n_psi, endpoint=False)  # 120° period

    results = []
    best_overall = 90.0
    best_params = None

    total = n_theta * n_phi * n_psi
    checked = 0
    last_pct = -1

    for theta in thetas:
        for phi in phis:
            for psi in psis:
                n_al, best_ang, details = alignment_score(
                    theta, phi, psi, tol_deg=tol_deg)
                if n_al > 0:
                    results.append({
                        'theta': theta, 'phi': phi, 'psi': psi,
                        'n_aligned': n_al,
                        'best_angle': best_ang,
                        'details': details,
                    })
                if best_ang < best_overall:
                    best_overall = best_ang
                    best_params = (theta, phi, psi)

                checked += 1
                pct = int(100 * checked / total)
                if pct > last_pct and pct % 10 == 0:
                    print(f"    {pct}% ({checked}/{total}), "
                          f"{len(results)} alignments found so far")
                    last_pct = pct

    return results, best_overall, best_params


def analyze_magic_angles(results):
    """Analyze the distribution of alignment orientations."""

    if not results:
        return

    # Group by number of aligned edges
    by_count = {}
    for r in results:
        n = r['n_aligned']
        if n not in by_count:
            by_count[n] = []
        by_count[n].append(r)

    print(f"\n  Alignment distribution:")
    print(f"  {'Aligned edges':>15s}  {'Orientations':>12s}  {'Best angle':>12s}")
    print("  " + "─" * 43)
    for n in sorted(by_count.keys()):
        best = min(r['best_angle'] for r in by_count[n])
        print(f"  {n:>15d}  {len(by_count[n]):>12d}  {best:>12.4f}°")

    # Analyze the 3-aligned cases (magic angles: all 3 wye edges match)
    if 3 in by_count:
        print(f"\n  Magic angles (3 edges aligned): {len(by_count[3])} orientations")
        print(f"  {'θ':>8s}  {'φ':>8s}  {'ψ':>8s}  {'best angle':>12s}")
        print("  " + "─" * 40)
        for r in sorted(by_count[3], key=lambda x: x['best_angle'])[:20]:
            print(f"  {np.degrees(r['theta']):8.2f}  "
                  f"{np.degrees(r['phi']):8.2f}  "
                  f"{np.degrees(r['psi']):8.2f}  "
                  f"{r['best_angle']:12.6f}°")

    return by_count


def analytical_check():
    """Analytical verification: at what plane orientations do
    jack edges project into 120°-separated directions?

    The tetrahedral face normals are the ⟨111⟩ directions.
    When the wye plane is perpendicular to a ⟨111⟩ direction,
    three of the four jack edges project into the plane at
    120° separation — matching the wye exactly.
    """
    print("\n  Analytical check: ⟨111⟩ face normals")
    print("  " + "─" * 50)

    face_normals = [
        np.array([+1, +1, +1]) / np.sqrt(3),
        np.array([+1, -1, -1]) / np.sqrt(3),
        np.array([-1, +1, -1]) / np.sqrt(3),
        np.array([-1, -1, +1]) / np.sqrt(3),
    ]

    for fi, fn in enumerate(face_normals):
        # Which jack edges are NOT along this normal?
        # The jack edge along fn projects to zero in the fn-plane.
        # The other 3 project at 120° separation.
        print(f"\n  Face normal {fi+1}: ({fn[0]:+.4f}, {fn[1]:+.4f}, {fn[2]:+.4f})")

        projections = []
        for ji, jd in enumerate(JACK):
            proj = jd - np.dot(jd, fn) * fn
            proj_len = np.linalg.norm(proj)
            if proj_len > 0.01:
                proj_unit = proj / proj_len
                projections.append((ji, proj_unit, proj_len))
                print(f"    Jack {ji+1}: projection length {proj_len:.4f}, "
                      f"direction ({proj_unit[0]:+.4f}, {proj_unit[1]:+.4f}, {proj_unit[2]:+.4f})")
            else:
                print(f"    Jack {ji+1}: projects to ~zero (along the normal)")

        # Check angles between projected directions
        if len(projections) >= 2:
            print(f"    Angles between projections:")
            for i in range(len(projections)):
                for j in range(i+1, len(projections)):
                    dot = np.dot(projections[i][1], projections[j][1])
                    dot = max(-1, min(1, dot))
                    angle = np.degrees(np.arccos(dot))
                    match = "✓ = 120°" if abs(angle - 120) < 0.1 else ""
                    print(f"      Jack {projections[i][0]+1} ↔ "
                          f"Jack {projections[j][0]+1}: {angle:.2f}°  {match}")


def plot_alignment_map(results, n_theta, n_phi):
    """Plot the best alignment angle as a function of (θ, φ),
    minimized over ψ."""
    if not results:
        return

    # Build a grid of best alignment angle at each (θ, φ)
    theta_bins = np.linspace(0, np.pi, n_theta)
    phi_bins = np.linspace(0, 2 * np.pi, n_phi)

    best_map = np.full((n_theta, n_phi), 90.0)
    count_map = np.zeros((n_theta, n_phi), dtype=int)

    for r in results:
        ti = np.argmin(np.abs(theta_bins - r['theta']))
        pi = np.argmin(np.abs(phi_bins - r['phi']))
        if r['best_angle'] < best_map[ti, pi]:
            best_map[ti, pi] = r['best_angle']
        count_map[ti, pi] = max(count_map[ti, pi], r['n_aligned'])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    im1 = ax1.pcolormesh(np.degrees(phi_bins), np.degrees(theta_bins),
                         best_map, cmap='viridis_r', shading='auto',
                         vmin=0, vmax=10)
    ax1.set_xlabel('φ (degrees)')
    ax1.set_ylabel('θ (degrees)')
    ax1.set_title('Best alignment angle (degrees), minimized over ψ')
    plt.colorbar(im1, ax=ax1, label='degrees')

    im2 = ax2.pcolormesh(np.degrees(phi_bins), np.degrees(theta_bins),
                         count_map, cmap='hot', shading='auto',
                         vmin=0, vmax=3)
    ax2.set_xlabel('φ (degrees)')
    ax2.set_ylabel('θ (degrees)')
    ax2.set_title('Max aligned edges at each (θ, φ)')
    plt.colorbar(im2, ax=ax2, label='# aligned edges')

    fig.suptitle('Track 3 Step 1: Wye-Jack edge alignment', fontsize=14)
    fig.tight_layout()
    fig.savefig(OUT / "track3_step1_alignment_map.png", dpi=150)
    plt.close(fig)
    print(f"\n  Saved: {OUT / 'track3_step1_alignment_map.png'}")


def main():
    print("=" * 60)
    print("  Track 3, Step 1: Single-node wye-jack alignment")
    print("=" * 60)

    # ── Part 1: Analytical check ──
    print("\n── Part 1: Analytical — ⟨111⟩ face projections ──")
    analytical_check()

    # ── Part 2: Brute-force sweep ──
    print("\n── Part 2: Brute-force sweep of (θ, φ, ψ) ──")
    print(f"  Tolerance: 0.5° (coarse scan)")
    print(f"  Grid: 90 θ × 180 φ × 60 ψ = {90*180*60:,} points")

    results, best_overall, best_params = sweep_coarse(
        n_theta=90, n_phi=180, n_psi=60, tol_deg=0.5)

    print(f"\n  Total orientations with ≥1 alignment: {len(results)}")
    print(f"  Total orientations checked: {90*180*60:,}")
    print(f"  Fraction with any alignment: "
          f"{len(results)/(90*180*60):.6f}")
    print(f"  Best overall angle: {best_overall:.4f}° at "
          f"θ={np.degrees(best_params[0]):.1f}°, "
          f"φ={np.degrees(best_params[1]):.1f}°, "
          f"ψ={np.degrees(best_params[2]):.1f}°")

    # ── Part 3: Analyze the alignment distribution ──
    print("\n── Part 3: Alignment distribution ──")
    by_count = analyze_magic_angles(results)

    # ── Part 4: Fine sweep around magic angles ──
    if 3 in by_count:
        print("\n── Part 4: Fine sweep around magic angles (0.1° tolerance) ──")
        # Take the first magic angle and sweep finely around it
        magic = by_count[3][0]
        th0, ph0, ps0 = magic['theta'], magic['phi'], magic['psi']
        fine_results = []
        delta = np.radians(5)  # ±5° around the magic angle
        n_fine = 50
        for dth in np.linspace(-delta, delta, n_fine):
            for dph in np.linspace(-delta, delta, n_fine):
                for dps in np.linspace(-delta, delta, n_fine):
                    th = th0 + dth
                    ph = ph0 + dph
                    ps = ps0 + dps
                    n_al, best_ang, details = alignment_score(
                        th, ph, ps, tol_deg=0.1)
                    if n_al > 0:
                        fine_results.append({
                            'theta': th, 'phi': ph, 'psi': ps,
                            'n_aligned': n_al,
                            'best_angle': best_ang,
                            'dtheta': np.degrees(dth),
                            'dphi': np.degrees(dph),
                            'dpsi': np.degrees(dps),
                        })

        print(f"  Fine sweep: {len(fine_results)} alignments in "
              f"±5° around magic angle")
        if fine_results:
            fine_by_count = {}
            for r in fine_results:
                n = r['n_aligned']
                if n not in fine_by_count:
                    fine_by_count[n] = []
                fine_by_count[n].append(r)
            for n in sorted(fine_by_count.keys()):
                print(f"    {n} aligned: {len(fine_by_count[n])} orientations")

            # How quickly does alignment drop from 3 → 2 → 1 → 0?
            print(f"\n  Alignment vs angular deviation from magic:")
            print(f"  {'deviation':>10s}  {'3-aligned':>10s}  "
                  f"{'2-aligned':>10s}  {'1-aligned':>10s}")
            for dev_max in [0.5, 1.0, 2.0, 3.0, 5.0]:
                n3 = sum(1 for r in fine_results
                         if r['n_aligned'] == 3 and
                         max(abs(r['dtheta']), abs(r['dphi']),
                             abs(r['dpsi'])) < dev_max)
                n2 = sum(1 for r in fine_results
                         if r['n_aligned'] == 2 and
                         max(abs(r['dtheta']), abs(r['dphi']),
                             abs(r['dpsi'])) < dev_max)
                n1 = sum(1 for r in fine_results
                         if r['n_aligned'] == 1 and
                         max(abs(r['dtheta']), abs(r['dphi']),
                             abs(r['dpsi'])) < dev_max)
                print(f"  {dev_max:10.1f}°  {n3:10d}  {n2:10d}  {n1:10d}")

    # ── Part 5: Plot ──
    print("\n── Part 5: Generating alignment map ──")
    plot_alignment_map(results, 90, 180)

    # ── Summary ──
    print("\n" + "=" * 60)
    print("  SUMMARY")
    print("=" * 60)
    total_checked = 90 * 180 * 60
    print(f"\n  Orientations checked: {total_checked:,}")
    print(f"  Orientations with ≥1 alignment: {len(results)}")
    print(f"  Fraction: {len(results)/total_checked:.6f}")
    print(f"  1/137 = {1/137:.6f}")
    print(f"  Ratio to 1/137: {(len(results)/total_checked) / (1/137):.2f}")

    if by_count:
        for n in sorted(by_count.keys()):
            frac = len(by_count[n]) / total_checked
            print(f"  {n}-aligned fraction: {frac:.6f} "
                  f"(= 1/{1/frac:.1f})" if frac > 0 else "")

    # Save
    with open(OUT / "track3_step1_results.txt", "w") as f:
        f.write("Track 3 Step 1: Single-node wye-jack alignment\n\n")
        f.write(f"Tolerance: 0.5° (coarse), 0.1° (fine)\n")
        f.write(f"Grid: 90 θ × 180 φ × 60 ψ = {total_checked:,}\n\n")
        f.write(f"Orientations with ≥1 alignment: {len(results)}\n")
        f.write(f"Fraction: {len(results)/total_checked:.6f}\n")
        f.write(f"1/137 = {1/137:.6f}\n\n")
        if by_count:
            for n in sorted(by_count.keys()):
                f.write(f"{n}-aligned: {len(by_count[n])} orientations "
                        f"({len(by_count[n])/total_checked:.6f})\n")

    print(f"\n  Results saved to {OUT / 'track3_step1_results.txt'}")


if __name__ == "__main__":
    main()
