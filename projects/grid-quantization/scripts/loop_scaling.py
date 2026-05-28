#!/usr/bin/env python3
"""How does the trapped (bound) fraction scale with loop size?

The `bound` test (run_recirculation.py) showed that a single hexagon
traps ~51% of a circulating excitation in a non-radiating compact
localized state.  This script asks the natural follow-up — and the
question raised directly by "is a bigger loop more lossy?":

> Excite the BOUNDARY of a patch of K hexagons as a coherent
> circulating mode.  What fraction stays trapped vs. radiates, as the
> loop perimeter P grows?

A falling bound fraction with P means bigger loops are lossier (less
of the excitation projects onto the bound/flat-band states).  Runs
are kept wraparound-free so radiated energy cannot return.

Method: patches are the K nearest hexagonal faces to the centre
(centred-hexagonal K = 1, 7, 19, 37 give clean concentric "flowers").
A boundary edge belongs to exactly one patch face; its circulation
direction is read from that face's half-edge orientation (all faces
are traced with the same chirality, so the boundary circulates
consistently).

Usage:
    source .venv/bin/activate
    python projects/grid-quantization/loop_scaling.py
"""

import os
import sys
from collections import Counter

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import make_honeycomb, evolve, edge_energy   # noqa: E402
from run_recirculation import find_plaquettes, face_centroid  # noqa: E402


def patch_boundary(patch_faces):
    """Edges on the outer boundary of a set of faces, with the
    circulation orientation inherited from their (single) face."""
    count = Counter()
    orient = {}
    for f in patch_faces:
        for ei, side in f:
            count[ei] += 1
            orient[ei] = side
    boundary = [ei for ei, c in count.items() if c == 1]
    return boundary, {ei: orient[ei] for ei in boundary}


def bound_fraction(nx, ny, K):
    pos, edges, vei, vend, ed, mid, box, wrap = make_honeycomb(nx, ny)
    E = len(edges)
    faces = find_plaquettes(edges, vei, vend, ed)
    cents = np.array([face_centroid(f, edges, pos) for f in faces])
    order = np.argsort(((cents - box / 2) ** 2).sum(axis=1))
    patch = [faces[i] for i in order[:K]]

    bnd, orient = patch_boundary(patch)
    P = len(bnd)

    af = np.zeros(E)
    ab = np.zeros(E)
    for ei in bnd:
        if orient[ei] == 0:
            af[ei] = 1.0
        else:
            ab[ei] = 1.0

    # wraparound-free run length: radiated energy travels ≤0.73/tick
    t_safe = int(box[0] / (2 * 0.73)) - 1
    n_steps = min(max(2 * P, 24), t_safe)
    snaps = evolve(af, ab, vei, vend, n_steps, snapshot_interval=1, N=3)

    e0 = edge_energy(*snaps[0][1:])[bnd].sum()
    eloop = np.array([edge_energy(a, b)[bnd].sum() for _, a, b in snaps])
    eloop /= e0
    # plateau = mean after the prompt radiation burst (one perimeter)
    plateau = eloop[min(P, n_steps - 1):]
    return P, float(plateau.mean()), float(plateau.max() - plateau.min())


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "..", "outputs")
    os.makedirs(out_dir, exist_ok=True)

    print("Loop-size scaling of the trapped (bound) fraction")
    print("  patch = K nearest hexagons; excite the boundary loop;")
    print("  measure the non-radiating fraction (wraparound-free).\n")

    nx = ny = 120     # large enough to stay wraparound-free for big P
    Ks = [1, 7, 19, 37]
    rows = []
    print(f"  {'hexagons':>8s} {'perimeter':>9s} {'bound frac':>11s}"
          f" {'drift':>7s}")
    for K in Ks:
        P, frac, drift = bound_fraction(nx, ny, K)
        rows.append((K, P, frac))
        print(f"  {K:>8d} {P:>9d} {frac:>11.4f} {drift:>7.4f}")

    Ps = [r[1] for r in rows]
    fracs = [r[2] for r in rows]
    trend = ("FALLS — bigger loops are lossier"
             if fracs[-1] < fracs[0] - 0.02 else
             "≈ FLAT — bound fraction roughly size-independent"
             if abs(fracs[-1] - fracs[0]) <= 0.02 else
             "RISES — bigger loops trap more")
    print(f"\n  Trend: bound fraction {trend}.")
    print(f"  (Single-pulse return falls exponentially as (2/3)^(2P); "
          f"this measures the COHERENT-mode trapped fraction instead.)")

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(Ps, fracs, "o-", color="navy", ms=7)
    for K, P, f in rows:
        ax.annotate(f"{K} hex", (P, f), textcoords="offset points",
                    xytext=(6, 6), fontsize=8)
    ax.axhline(0.5, color="gray", ls=":", alpha=0.6)
    ax.set_xlabel("loop perimeter P (edges)")
    ax.set_ylabel("trapped (non-radiating) fraction")
    ax.set_ylim(0, 1)
    ax.set_title("Trapped fraction vs loop size\n"
                 "(does 'bigger loop = more lossy' hold?)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    path = os.path.join(out_dir, "loop_scaling.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"\n  Saved: {path}")
    plt.close(fig)


if __name__ == "__main__":
    main()
