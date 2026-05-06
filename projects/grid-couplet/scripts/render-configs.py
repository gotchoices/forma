#!/usr/bin/env python3
"""
render-configs — produce the chapter 2 §2 figure.

Renders the two configurations chapter 2 compares:
- Open 1D couplet chain (N points, N edges, trailing edge as inert stub)
- Closed 1D couplet loop (N points, N edges, all active)

Output: output/configs.png

The figure is purely structural — points are filled circles, edges are
labelled segments, the trailing-stub edge is rendered dashed. No
dynamics are simulated.
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)

N = 6  # number of couplets in each configuration

POINT_COLOR = "#222"
EDGE_COLOR = "#4477aa"
STUB_COLOR = "#aaaaaa"
LABEL_COLOR = "#444"


def draw_arrow(ax, x0, y0, x1, y1, color=EDGE_COLOR, linestyle="-", linewidth=1.6):
    arrow = FancyArrowPatch(
        (x0, y0), (x1, y1),
        arrowstyle="->",
        mutation_scale=14,
        linewidth=linewidth,
        color=color,
        linestyle=linestyle,
        shrinkA=10,
        shrinkB=10,
    )
    ax.add_patch(arrow)


def draw_open_chain(ax):
    ax.set_title("Open 1D couplet chain", fontsize=11)
    spacing = 1.0
    xs = np.arange(N) * spacing
    y = 0.0

    # Edges (point i tail → point i+1 head, with the trailing edge as a stub)
    for i in range(N - 1):
        draw_arrow(ax, xs[i], y, xs[i + 1], y)
        ax.text((xs[i] + xs[i + 1]) / 2, y + 0.13, f"e{i}",
                ha="center", va="bottom", fontsize=8, color=LABEL_COLOR)

    # Trailing stub: drawn dashed, no head attached
    stub_end_x = xs[-1] + spacing * 0.6
    draw_arrow(ax, xs[-1], y, stub_end_x, y, color=STUB_COLOR, linestyle="--", linewidth=1.2)
    ax.text((xs[-1] + stub_end_x) / 2, y + 0.13, f"e{N - 1} (stub)",
            ha="center", va="bottom", fontsize=8, color=STUB_COLOR)

    # Points
    for i, x in enumerate(xs):
        ax.plot(x, y, "o", markersize=12, color=POINT_COLOR, zorder=5)
        ax.text(x, y - 0.18, f"φ{i}", ha="center", va="top", fontsize=8, color=LABEL_COLOR)

    ax.set_xlim(-0.5, stub_end_x + 0.4)
    ax.set_ylim(-0.6, 0.6)
    ax.set_aspect("equal")
    ax.axis("off")


def draw_closed_loop(ax):
    ax.set_title("Closed 1D couplet loop", fontsize=11)
    radius = 1.0
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
    # Rotate so that point 0 sits at the top, going clockwise
    angles = np.pi / 2 - angles
    xs = radius * np.cos(angles)
    ys = radius * np.sin(angles)

    # Edges around the loop (point i → point (i+1) mod N)
    for i in range(N):
        j = (i + 1) % N
        draw_arrow(ax, xs[i], ys[i], xs[j], ys[j])
        # Mid-arc label position pushed slightly outward
        mid_angle = (angles[i] + angles[j]) / 2
        # Handle wrap: if angles[j] - angles[i] is near 2π (closure edge), use the wrap midpoint
        diff = angles[j] - angles[i]
        if diff > np.pi:
            mid_angle = (angles[i] + angles[j]) / 2 + np.pi
        if diff < -np.pi:
            mid_angle = (angles[i] + angles[j]) / 2 + np.pi
        label_r = radius + 0.18
        ax.text(label_r * np.cos(mid_angle), label_r * np.sin(mid_angle),
                f"e{i}", ha="center", va="center", fontsize=8, color=LABEL_COLOR)

    # Points
    for i, (x, y) in enumerate(zip(xs, ys)):
        ax.plot(x, y, "o", markersize=12, color=POINT_COLOR, zorder=5)
        # Place point label outside the dot
        lbl_r = radius - 0.22
        ax.text(lbl_r * np.cos(angles[i]), lbl_r * np.sin(angles[i]),
                f"φ{i}", ha="center", va="center", fontsize=8, color=LABEL_COLOR)

    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    draw_open_chain(axes[0])
    draw_closed_loop(axes[1])
    plt.tight_layout()
    out_path = os.path.join(OUTDIR, "configs.png")
    plt.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close()
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
