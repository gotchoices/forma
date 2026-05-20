"""
draw_candidate_map.py — spatial map of a QY-ED candidate plus the neutrino curve.

Draws the K4 candidate (QY-ED-share3) as a planar figure that Mermaid cannot
produce: the quark wye (hub + 3 spokes) centred inside the lepton delta
(triangle on the 3 spokes), with the 1D neutrino curve as an outer loop
coupled to the 3 delta corners at 120 deg.

Connection styles encode substrate dimensionality:
  - heavy solid line = a 2D-sheet connection (a Ma(i, j) torus pair)
  - dotted line      = a 1D-curve connection (the neutrino loop's coupling)

Colours follow the project Mermaid convention: red = quark, blue = lepton,
green = neutrino.

The neutrino loop can be a plain circle or the N = 3 tube-function curve
r(phi) = R[1 + a1 cos(3 phi) + a2 cos(6 phi)] — the actual shape the
neutrino fit prefers (neutrino_1d_fit.py finds a strongly 3-lobed curve).

Every layout and style parameter is an argparse knob, so the figure can be
re-tuned without editing the body.  Run with --help for the full list.

Outputs: an SVG (default) or PNG image, embeddable in the work .md files.
"""

from __future__ import annotations

import argparse
from math import cos, sin, radians, pi
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def polar(r, theta_deg):
    """(x, y) from radius r and angle theta in degrees."""
    t = radians(theta_deg)
    return r * cos(t), r * sin(t)


def lobe_r(psi, R, a1, a2):
    """Tube-function radius r(psi) = R[1 + a1 cos(3 psi) + a2 cos(6 psi)]."""
    return R * (1.0 + a1 * np.cos(3.0 * psi) + a2 * np.cos(6.0 * psi))


def lobe_phase(R, a1, a2, align, start_angle):
    """Rotation phi_rot that puts a lobe peak on a corner ('corners') or
       in a gap ('gaps'). Found by locating the loop's max-radius angle."""
    psi = np.linspace(0, 2 * pi, 3000, endpoint=False)
    psi_peak = psi[int(np.argmax(lobe_r(psi, R, a1, a2)))]
    target = radians(start_angle if align == "corners" else start_angle + 60.0)
    return target - psi_peak


def neutrino_loop_xy(R, shape, a1, a2, phi_rot, npts=900):
    """Sample the neutrino loop as (x, y) arrays."""
    phi = np.linspace(0, 2 * pi, npts)
    if shape == "lobed":
        r = lobe_r(phi - phi_rot, R, a1, a2)
    else:
        r = np.full_like(phi, R)
    return r * np.cos(phi), r * np.sin(phi)


def loop_radius_at(angle_deg, R, shape, a1, a2, phi_rot):
    """Radius of the neutrino loop at a given angle (for placing connectors)."""
    if shape != "lobed":
        return R
    return float(lobe_r(np.array([radians(angle_deg) - phi_rot]), R, a1, a2)[0])


def build_parser():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    # --- output ---
    p.add_argument("--out", default=None,
                   help="output path (default: outputs/candidate-map.svg). "
                        "Extension picks the format (.svg or .png).")
    p.add_argument("--dpi", type=float, default=150, help="raster DPI for .png")
    p.add_argument("--figsize", type=float, nargs=2, default=[7.0, 7.0],
                   metavar=("W", "H"), help="figure size in inches")
    p.add_argument("--bg", choices=["white", "transparent"], default="white",
                   help="background")
    # --- layout ---
    p.add_argument("--corner-radius", type=float, default=1.50,
                   help="distance of the 3 delta corners from the hub")
    p.add_argument("--neutrino-radius", type=float, default=2.80,
                   help="mean radius of the neutrino loop")
    p.add_argument("--start-angle", type=float, default=90.0,
                   help="angle (deg) of corner m1; the others follow at 120 deg")
    p.add_argument("--margin", type=float, default=0.45,
                   help="blank margin beyond the neutrino loop")
    # --- neutrino loop shape ---
    p.add_argument("--neutrino-shape", choices=["circle", "lobed"],
                   default="lobed",
                   help="plain circle or N=3 tube-function curve (default lobed)")
    p.add_argument("--lobe-a1", type=float, default=-0.45,
                   help="cos(3 phi) amplitude of the neutrino loop "
                        "(fit prefers ~-0.85; -0.45 is a cleaner schematic depth)")
    p.add_argument("--lobe-a2", type=float, default=0.10,
                   help="cos(6 phi) amplitude of the neutrino loop")
    p.add_argument("--lobe-align", choices=["corners", "gaps"], default="corners",
                   help="align lobe peaks to the corners or to the gaps")
    p.add_argument("--loop-style", choices=["solid", "dotted", "dashed"],
                   default="solid", help="line style of the neutrino loop curve")
    # --- line styles ---
    p.add_argument("--heavy-width", type=float, default=4.2,
                   help="line width for 2D-sheet connections")
    p.add_argument("--dot-width", type=float, default=1.9,
                   help="line width for 1D-curve connections")
    p.add_argument("--loop-width", type=float, default=2.5,
                   help="line width for the neutrino loop curve")
    # --- nodes / labels ---
    p.add_argument("--node-size", type=float, default=430,
                   help="marker area for the dim nodes")
    p.add_argument("--font-size", type=float, default=12.0)
    p.add_argument("--no-node-labels", action="store_true",
                   help="hide the m1..m4 node labels")
    p.add_argument("--no-leg-labels", action="store_true",
                   help="hide the per-leg particle labels")
    p.add_argument("--region-labels", action="store_true",
                   help="show 'quark wye' / 'electron delta' / 'neutrino curve'")
    p.add_argument("--no-legend", action="store_true", help="hide the legend")
    p.add_argument("--title", default="QY-ED-share3 (K4) with the neutrino curve",
                   help="figure title (empty string for none)")
    p.add_argument("--quark-legs", nargs=3, default=["u/d", "s/c", "b/t"],
                   metavar=("L1", "L2", "L3"),
                   help="labels for the 3 quark wye legs (m1, m2, m3 spokes)")
    p.add_argument("--lepton-legs", nargs=3, default=["e", "τ", "μ"],
                   metavar=("L1", "L2", "L3"),
                   help="labels for the 3 lepton delta legs (m1-m2, m2-m3, m3-m1)")
    # --- colours ---
    p.add_argument("--quark-color", default="#c0392b")
    p.add_argument("--lepton-color", default="#2c5fb8")
    p.add_argument("--neutrino-color", default="#2e8b57")
    p.add_argument("--node-color", default="#222222")
    return p


def leg_label(ax, p0, p1, text, color, fontsize):
    """Place a white-boxed label at the midpoint of the segment p0--p1."""
    mx, my = 0.5 * (p0[0] + p1[0]), 0.5 * (p0[1] + p1[1])
    ax.annotate(text, (mx, my), ha="center", va="center", color=color,
                fontsize=fontsize, weight="bold", zorder=7,
                bbox=dict(boxstyle="round,pad=0.16", fc="white",
                          ec="none", alpha=0.88))


def main():
    args = build_parser().parse_args()

    out = Path(args.out) if args.out else (
        Path(__file__).resolve().parents[1] / "outputs" / "candidate-map.svg")
    out.parent.mkdir(parents=True, exist_ok=True)

    qc, lc, nc = args.quark_color, args.lepton_color, args.neutrino_color
    dotstyle = (0, (1.6, 2.2))  # dotted pattern for 1D-curve connections
    a1, a2 = args.lobe_a1, args.lobe_a2

    phi_rot = (lobe_phase(args.neutrino_radius, a1, a2, args.lobe_align,
                          args.start_angle)
               if args.neutrino_shape == "lobed" else 0.0)

    fig, ax = plt.subplots(figsize=tuple(args.figsize))
    ax.set_aspect("equal")
    ax.axis("off")

    # --- node positions -------------------------------------------------
    hub = (0.0, 0.0)
    corner_ang = [args.start_angle + 120.0 * k for k in range(3)]
    corners = [polar(args.corner_radius, a) for a in corner_ang]

    # --- quark wye: hub -> each corner  (2D sheets -> heavy solid) -------
    for (cx, cy) in corners:
        ax.plot([hub[0], cx], [hub[1], cy], color=qc,
                lw=args.heavy_width, solid_capstyle="round", zorder=2)

    # --- lepton delta: corner -> corner  (2D sheets -> heavy solid) -----
    for i in range(3):
        x0, y0 = corners[i]
        x1, y1 = corners[(i + 1) % 3]
        ax.plot([x0, x1], [y0, y1], color=lc,
                lw=args.heavy_width, solid_capstyle="round", zorder=2)

    # --- neutrino loop --------------------------------------------------
    lx, ly = neutrino_loop_xy(args.neutrino_radius, args.neutrino_shape,
                              a1, a2, phi_rot)
    loop_ls = {"solid": "-", "dotted": dotstyle,
               "dashed": (0, (6, 3))}[args.loop_style]
    ax.plot(lx, ly, color=nc, lw=args.loop_width, ls=loop_ls, zorder=2)

    # --- neutrino connectors: corner -> loop  (1D curve -> dotted) ------
    for (cx, cy), a in zip(corners, corner_ang):
        rloop = loop_radius_at(a, args.neutrino_radius, args.neutrino_shape,
                               a1, a2, phi_rot)
        lxp, lyp = polar(rloop, a)
        ax.plot([cx, lxp], [cy, lyp], color=nc, lw=args.dot_width,
                ls=dotstyle, zorder=3)

    # --- leg labels -----------------------------------------------------
    if not args.no_leg_labels:
        for (cx, cy), lab in zip(corners, args.quark_legs):
            leg_label(ax, hub, (cx, cy), lab, qc, args.font_size - 2.0)
        for i in range(3):
            leg_label(ax, corners[i], corners[(i + 1) % 3],
                      args.lepton_legs[i], lc, args.font_size - 2.0)

    # --- nodes ----------------------------------------------------------
    nodes = [hub] + corners
    nx = [p[0] for p in nodes]
    ny = [p[1] for p in nodes]
    ax.scatter(nx, ny, s=args.node_size, color=args.node_color,
               edgecolors="white", linewidths=1.4, zorder=5)

    if not args.no_node_labels:
        for (px, py), nm in zip(nodes, ["m4", "m1", "m2", "m3"]):
            ax.annotate(nm, (px, py), ha="center", va="center", color="white",
                        fontsize=args.font_size - 2.5, zorder=6, weight="bold")

    # --- region annotations (optional) ---------------------------------
    if args.region_labels:
        gap = [args.start_angle + 60.0 + 120.0 * k for k in range(3)]
        gx, gy = polar(args.corner_radius * 0.40, gap[0])
        ax.annotate("quark wye", (gx, gy), ha="center", va="center",
                    color=qc, fontsize=args.font_size - 2.5, style="italic")
        mx, my = polar(args.corner_radius * 1.0, gap[1])
        ax.annotate("electron delta", (mx, my), ha="center", va="center",
                    color=lc, fontsize=args.font_size - 2.5, style="italic")
        ex, ey = polar(args.neutrino_radius * 0.62, gap[2])
        ax.annotate("neutrino curve", (ex, ey), ha="center", va="center",
                    color=nc, fontsize=args.font_size - 2.5, style="italic")

    # --- legend ---------------------------------------------------------
    if not args.no_legend:
        handles = [
            Line2D([0], [0], color=qc, lw=args.heavy_width,
                   label="quark sheet  (2D pair)"),
            Line2D([0], [0], color=lc, lw=args.heavy_width,
                   label="lepton sheet  (2D pair)"),
            Line2D([0], [0], color=nc, lw=args.loop_width, ls=loop_ls,
                   label="neutrino curve  (1D loop)"),
            Line2D([0], [0], color=nc, lw=args.dot_width, ls=dotstyle,
                   label="neutrino link  (1D-curve coupling)"),
        ]
        ax.legend(handles=handles, loc="upper left", frameon=False,
                  fontsize=args.font_size - 2.5, bbox_to_anchor=(-0.02, 1.02))

    if args.title:
        ax.set_title(args.title, fontsize=args.font_size, pad=10)

    lim = max(np.max(np.abs(lx)), np.max(np.abs(ly))) + args.margin
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    transparent = args.bg == "transparent"
    facecolor = "none" if transparent else "white"
    fig.savefig(out, dpi=args.dpi, bbox_inches="tight",
                transparent=transparent, facecolor=facecolor)
    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
