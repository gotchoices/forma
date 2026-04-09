"""
R52 Track 4b: Coaxial tube-loop mutual inductance.

HYPOTHESIS:
Each "tube winding" of the (1, n_ring) standing wave can be modeled as
a current loop in 3D.  The n_ring loops sit at different positions
around the ring direction.  Their mutual inductance determines whether
the bare moment is enhanced or reduced.

METHOD:
1. Treat the (1, n_ring) mode as n_ring coaxial circular current loops.
2. Each loop has radius a (tube minor radius) and is centered on the
   ring at angle θ_k = k * 2π/n_ring.
3. All loops carry the same current direction (positive sense).
4. Compute the mutual inductance matrix M_ij using the Neumann formula
   (closed-form via elliptic integrals for two coaxial circular loops).
5. Total inductance = Σ M_ii + Σ_{i≠j} M_ij.
6. The off-diagonal sum is the inter-loop interaction; its sign tells
   us whether n_ring = 2 vs n_ring = 3 differs.

ASSUMPTIONS (frozen for this sub-track):
- Each loop is a circle of radius a in a plane perpendicular to its
  position vector from the torus center.
- Loops are NOT coaxial in the strict sense (their axes diverge from
  the ring center).  We use the Neumann integral for non-coaxial
  loops via numerical integration.
- All loops carry equal currents in the same rotational sense.
- Mutual inductance is computed via Biot-Savart line integral.

NOTE: this sub-track is the most "classical" and may give same-sign
for both modes (co-circulating loops always reinforce). It serves as
a baseline.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ── Loop construction ──────────────────────────────────────────────

def make_loop(theta_ring_center, R, a, n_segments=200):
    """
    Make a circular current loop on the torus surface.

    The loop is at ring angle θ_ring_center, parameterized by tube
    angle θ_tube ∈ [0, 2π).  Returns (positions, tangent vectors).
    """
    theta_tube = np.linspace(0, 2 * np.pi, n_segments, endpoint=False)
    cos_t = np.cos(theta_tube)
    sin_t = np.sin(theta_tube)
    cos_r = np.cos(theta_ring_center)
    sin_r = np.sin(theta_ring_center)

    rho = R + a * cos_t
    x = rho * cos_r
    y = rho * sin_r
    z = a * sin_t
    pos = np.stack([x, y, z], axis=-1)

    # Tangent: d(pos)/d(theta_tube)
    drho = -a * sin_t
    dx = drho * cos_r
    dy = drho * sin_r
    dz = a * cos_t
    tan = np.stack([dx, dy, dz], axis=-1)

    # Length element (uniform)
    dl = 2 * np.pi / n_segments

    return pos, tan * dl


def neumann_inductance(loop_a, loop_b, eps=1e-9):
    """
    Compute the Neumann mutual inductance integral for two loops:
        M_ab = (μ₀/4π) ∮∮ (dl_a · dl_b) / |r_a - r_b|

    We drop the μ₀/4π prefactor (returns a geometric factor).

    For self-inductance (loop_a = loop_b), excludes the diagonal
    singularity using the eps softening.
    """
    pos_a, dl_a = loop_a
    pos_b, dl_b = loop_b

    # Compute pairwise distances and dot products
    # pos_a: (N_a, 3), pos_b: (N_b, 3)
    diff = pos_a[:, None, :] - pos_b[None, :, :]  # (N_a, N_b, 3)
    dist = np.linalg.norm(diff, axis=-1)  # (N_a, N_b)

    # Dot products of tangent vectors
    dot = np.einsum('ik,jk->ij', dl_a, dl_b)  # (N_a, N_b)

    # Avoid singularity
    dist_safe = np.maximum(dist, eps)
    integrand = dot / dist_safe

    return integrand.sum()


def loop_inductance_matrix(R, a, n_ring, n_segments=200):
    """
    Compute the n_ring × n_ring mutual inductance matrix for a
    (1, n_ring) mode treated as n_ring tube loops at evenly spaced
    ring positions.

    For self-terms (diagonal), use a coarser softening to avoid
    Coulomb singularities; the diagonal is essentially the same for
    all loops, so we just compute one and copy.
    """
    loops = []
    for k in range(n_ring):
        theta_k = 2 * np.pi * k / n_ring
        loops.append(make_loop(theta_k, R, a, n_segments))

    M = np.zeros((n_ring, n_ring))
    for i in range(n_ring):
        for j in range(n_ring):
            if i == j:
                # Self-inductance: use larger softening
                M[i, j] = neumann_inductance(loops[i], loops[j], eps=0.05 * a)
            else:
                M[i, j] = neumann_inductance(loops[i], loops[j], eps=1e-9)
    return M


# ── Sign test ───────────────────────────────────────────────────────

def run_sign_test(r_aspect, R=1.0, n_segments=200, label=""):
    """
    Compute mutual inductance matrix for n_ring = 2 and n_ring = 3.
    """
    a = r_aspect * R

    print(f"\n── {label} (r = a/R = {r_aspect}) ──")
    print(f"  R = {R}, a = {a}")

    results = {}
    for n_ring in [2, 3]:
        M = loop_inductance_matrix(R, a, n_ring, n_segments)
        diag = np.trace(M)
        off_diag = np.sum(M) - diag
        ratio = off_diag / diag if diag != 0 else float('inf')

        results[n_ring] = {
            'M': M,
            'diag': diag,
            'off_diag': off_diag,
            'ratio': ratio,
        }

        print(f"\n  n_ring = {n_ring}:")
        print(f"    Inductance matrix:")
        for row in M:
            print(f"      {' '.join(f'{x:+8.3f}' for x in row)}")
        print(f"    Diagonal sum (self-ind): {diag:+.4f}")
        print(f"    Off-diagonal sum (mutual): {off_diag:+.4f}")
        print(f"    Ratio (mutual/self):     {ratio:+.4f}")

    print(f"\n  Sign test:")
    print(f"    Off-diag(n=2) = {results[2]['off_diag']:+.4f}")
    print(f"    Off-diag(n=3) = {results[3]['off_diag']:+.4f}")
    if results[2]['off_diag'] > 0 and results[3]['off_diag'] < 0:
        print(f"    *** PREDICTED: + for n=2, - for n=3 ***")
    elif results[2]['off_diag'] < 0 and results[3]['off_diag'] > 0:
        print(f"    REVERSED")
    else:
        print(f"    SAME-SIGN: both have sign({np.sign(results[2]['off_diag'])})")

    return results


# ── Main ───────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("R52 Track 4b: Coaxial tube-loop mutual inductance")
    print("=" * 70)
    print(__doc__)

    print("\n" + "=" * 70)
    print("PART 1: Sign test at multiple aspect ratios")
    print("=" * 70)

    for r in [0.5, 2.0, 8.906]:
        if r == 8.906:
            label = "Proton aspect ratio (R27 F18)"
        elif r == 0.5:
            label = "Thin-tube limit"
        else:
            label = f"r = {r}"
        run_sign_test(r, label=label, n_segments=200)

    print("\n" + "=" * 70)
    print("PART 2: Aspect ratio scan")
    print("=" * 70)

    r_values = np.linspace(0.5, 15.0, 20)
    off2_arr = np.zeros(len(r_values))
    off3_arr = np.zeros(len(r_values))

    for i, r in enumerate(r_values):
        a = r * 1.0
        M2 = loop_inductance_matrix(1.0, a, 2, n_segments=120)
        M3 = loop_inductance_matrix(1.0, a, 3, n_segments=120)
        off2_arr[i] = np.sum(M2) - np.trace(M2)
        off3_arr[i] = np.sum(M3) - np.trace(M3)

    print(f"\n  {'r':>6s}  {'off2':>10s}  {'off3':>10s}  {'sign2':>6s}  {'sign3':>6s}")
    print("  " + "─" * 50)
    for i in range(0, len(r_values), 2):
        print(f"  {r_values[i]:6.2f}  {off2_arr[i]:+10.4f}  {off3_arr[i]:+10.4f}  "
              f"{int(np.sign(off2_arr[i])):+6d}  {int(np.sign(off3_arr[i])):+6d}")

    sign_diff = np.sum(np.sign(off2_arr) != np.sign(off3_arr))
    print(f"\n  Aspect ratios with sign difference: {sign_diff} / {len(r_values)}")

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(r_values, off2_arr, 'b-o', label='n_ring = 2 (electron)', markersize=5)
    ax.plot(r_values, off3_arr, 'r-^', label='n_ring = 3 (proton)', markersize=5)
    ax.axhline(0, color='k', linestyle='--', alpha=0.3)
    ax.set_xlabel('Aspect ratio r = a/R')
    ax.set_ylabel('Off-diagonal sum (mutual inductance)')
    ax.set_title('Inter-loop mutual inductance vs aspect ratio')
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    out = Path(__file__).parent.parent / "track4b_results.png"
    plt.savefig(out, dpi=120)
    print(f"\n  Plot saved to {out}")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    M2_p = loop_inductance_matrix(1.0, 8.906, 2, n_segments=200)
    M3_p = loop_inductance_matrix(1.0, 8.906, 3, n_segments=200)
    off2_p = np.sum(M2_p) - np.trace(M2_p)
    off3_p = np.sum(M3_p) - np.trace(M3_p)

    print(f"\nAt proton aspect ratio (r = 8.906):")
    print(f"  n_ring = 2:  off-diag mutual = {off2_p:+.4f}")
    print(f"  n_ring = 3:  off-diag mutual = {off3_p:+.4f}")

    if off2_p > 0 and off3_p < 0:
        print("\n  *** SUCCESS: predicted sign pattern ***")
    elif off2_p < 0 and off3_p > 0:
        print("\n  REVERSED")
    elif np.sign(off2_p) == np.sign(off3_p):
        print(f"\n  SAME-SIGN: both {np.sign(off2_p):+.0f}")
        print("  Loop mutual inductance does not differentiate the modes")
        print("  This is expected for co-circulating loops")
        print("  Move to sub-track 4c (continuous wave self-energy)")


if __name__ == "__main__":
    main()
