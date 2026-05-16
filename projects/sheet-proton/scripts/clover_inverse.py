"""
clover_inverse.py — V2 cross-section: 3 outer convex lobes + 3 inner concave
lobes connected by short convex connectors.

Construction:
  * 3 OUTER LOBES of radius r_outer, 240° convex arcs bulging away from
    cross-section center. Centers at angles {0°, 120°, 240°} on a circle of
    radius D_outer = r_outer + r_inner.
  * 3 INNER LOBES of radius r_inner, 240° concave arcs bulging toward
    cross-section center. Centers at angles {60°, 180°, 300°} on a circle
    of radius D_inner = r_outer − r_conn.
  * 6 CONNECTORS of radius r_conn, 60° convex arcs joining each
    outer-lobe to an adjacent inner-lobe.

Closure verification:
  total ∫κ ds = 3·(+240°) + 3·(−240°) + 6·(+60°) = +360° = 2π. Simple
  closed curve.

Per-arc Gauss-Bonnet charges:
  outer lobe: Q = +240°/360° = +2/3
  inner lobe: Q = −240°/360° = −2/3
  connector:  Q = +60°/360°  = +1/6

Bounds on the three free radii:
  r_outer > 0
  0 < r_conn < r_outer
  0 < r_inner < (r_outer − r_conn) · √3 / 2

Usage:
    .venv/bin/python scripts/clover_inverse.py
        [--r-outer R]       outer-lobe radius (default 1.0)
        [--r-inner R]       inner-lobe radius (default 0.3)
        [--r-conn R]        connector radius (default 0.2)
        [--n-samples N]     samples per arc for rendering (default 100)
        [--show]            display interactively
        [--with-level-2]    also render level-2 (bisect-and-insert recursion)

Output: outputs/clover_inverse_panel.png
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import pi, sqrt, cos, sin, atan2
from pathlib import Path
from typing import List, Tuple

import numpy as np
import matplotlib.pyplot as plt


SQRT3 = sqrt(3.0)


@dataclass
class Arc:
    """Same Arc dataclass as clover_on_clover.py — kept here so this module
    is self-contained. center, radius, angle_start/end (radians), sign:
    +1 convex (CCW on its circle), -1 concave (CW on its circle). label,
    level_created, is_sub_lobe used by recursive variants.
    """
    center: Tuple[float, float]
    radius: float
    angle_start: float
    angle_end: float
    sign: int
    label: str = ""
    level_created: int = 1
    is_sub_lobe: bool = False

    @property
    def angular_extent(self) -> float:
        return abs(self.angle_end - self.angle_start)

    def signed_extent(self) -> float:
        return self.sign * self.angular_extent

    def sample(self, n: int = 100) -> Tuple[np.ndarray, np.ndarray]:
        t = np.linspace(0.0, 1.0, n)
        a = self.angle_start + t * (self.angle_end - self.angle_start)
        return (
            self.center[0] + self.radius * np.cos(a),
            self.center[1] + self.radius * np.sin(a),
        )


# -----------------------------------------------------------------------------
# Level-1 builder
# -----------------------------------------------------------------------------


def validate_radii(r_outer: float, r_inner: float, r_conn: float) -> None:
    """Raise ValueError if the radii violate the closure / non-overlap bounds."""
    if r_outer <= 0:
        raise ValueError(f"r_outer must be > 0 (got {r_outer})")
    if not (0 < r_conn < r_outer):
        raise ValueError(
            f"r_conn must be in (0, r_outer): got r_conn={r_conn}, r_outer={r_outer}"
        )
    inner_max = (r_outer - r_conn) * SQRT3 / 2
    if not (0 < r_inner < inner_max):
        raise ValueError(
            f"r_inner must be in (0, (r_outer-r_conn)*sqrt(3)/2 = {inner_max:.4f}): "
            f"got r_inner={r_inner}"
        )


def build_clover_inverse_arcs(
    r_outer: float, r_inner: float, r_conn: float
) -> List[Arc]:
    """Build the level-1 clover-inverse profile as 12 arcs in CCW order.

    Traversal order (one of three Z₃-symmetric blocks):
        outer-lobe-k, connector-k-up, inner-lobe-k, connector-k-down, ...

    The block is repeated 3 times (k = 0, 1, 2).
    """
    validate_radii(r_outer, r_inner, r_conn)
    D_outer = r_outer + r_inner
    D_inner = r_outer - r_conn

    arcs: List[Arc] = []
    for k in range(3):
        alpha_outer = 2 * pi * k / 3
        alpha_inner_next = alpha_outer + pi / 3  # next inner lobe (going CCW)

        # Outer lobe k: 240° convex arc on circle at D_outer in direction alpha_outer.
        # Arc midpoint = outermost point at angle alpha_outer on its kissing
        # circle. The 240° arc spans angle (alpha_outer - 120°, alpha_outer + 120°)
        # CCW. Tangent endpoints sit at the start (alpha_outer - 120°) and the
        # end (alpha_outer + 120°).
        cx_o = D_outer * cos(alpha_outer)
        cy_o = D_outer * sin(alpha_outer)
        a_out_start = alpha_outer - 2 * pi / 3
        a_out_end = alpha_outer + 2 * pi / 3
        arcs.append(Arc(
            center=(cx_o, cy_o), radius=r_outer,
            angle_start=a_out_start, angle_end=a_out_end,
            sign=+1, label="outer_L1", level_created=1, is_sub_lobe=True,
        ))

        # Connector "up" (from outer-k to inner at angle alpha_outer + 60°).
        # Center: at C_outer + (r_outer - r_conn) · (cos(alpha_outer + 120°),
        #                                            sin(alpha_outer + 120°))
        # 60° convex CCW arc, from angle (alpha_outer + 120°) to (alpha_outer + 180°)
        # on its kissing circle.
        ang_to_junction = alpha_outer + 2 * pi / 3
        cx_c = cx_o + (r_outer - r_conn) * cos(ang_to_junction)
        cy_c = cy_o + (r_outer - r_conn) * sin(ang_to_junction)
        a_c_start = ang_to_junction
        a_c_end = ang_to_junction + pi / 3
        arcs.append(Arc(
            center=(cx_c, cy_c), radius=r_conn,
            angle_start=a_c_start, angle_end=a_c_end,
            sign=+1, label="conn_L1", level_created=1, is_sub_lobe=False,
        ))

        # Inner lobe at angle alpha_inner_next: 240° concave arc traversed CW
        # on its kissing circle. The kissing circle is at C_inner =
        # D_inner * (cos alpha_inner_next, sin alpha_inner_next), radius r_inner.
        #
        # The 240° arc passes through the INNERMOST point (closest to origin)
        # at angle (alpha_inner_next + π) on the kissing circle. By symmetry
        # the two junctions are 120° away from this on either side:
        #   junction with up-connector:  angle (alpha_inner_next + π) + 120°
        #                              = alpha_inner_next + 5π/3  (mod 2π)
        #                              = alpha_inner_next - π/3
        #   junction with down-connector: angle (alpha_inner_next + π) - 120°
        #                               = alpha_inner_next + π/3
        # Going CW from the first junction by 240° = 4π/3 reaches the second.
        cx_i = D_inner * cos(alpha_inner_next)
        cy_i = D_inner * sin(alpha_inner_next)
        a_in_start = alpha_inner_next - pi / 3
        a_in_end = a_in_start - 4 * pi / 3   # CW sweep of 240° (signed: -4π/3)
        arcs.append(Arc(
            center=(cx_i, cy_i), radius=r_inner,
            angle_start=a_in_start, angle_end=a_in_end,
            sign=-1, label="inner_L1", level_created=1, is_sub_lobe=True,
        ))

        # Connector "down" from inner to outer-(k+1).
        # By mirror symmetry of the up-connector across the inner-lobe's axis,
        # its kissing circle center is at C_inner + (r_inner + r_conn) ·
        # (cos(alpha_inner_next - 120°), sin(alpha_inner_next - 120°))
        # — opposite-side tangency between concave inner-lobe and convex connector.
        # Wait: that's external tangency (concave + convex => opposite-side).
        # Distance = r_inner + r_conn, in the direction OPPOSITE to the inner-lobe's
        # outward normal at the junction point.
        # Junction point: exit from inner-lobe at angle a_in_end on the kissing
        # circle = alpha_inner_next - 4*pi/3 (equivalent to alpha_inner_next + 2*pi/3).
        a_junction_inner_exit = a_in_end  # = alpha_inner_next - 4*pi/3
        jx = cx_i + r_inner * cos(a_junction_inner_exit)
        jy = cy_i + r_inner * sin(a_junction_inner_exit)
        # Tangent direction at junction (CW on inner-lobe circle = going along
        # the curve CCW around cross-section): perpendicular to radius, rotated
        # 90° CW (since traversal is CW on kissing circle).
        # The connector's kissing center is on the OPPOSITE side from C_inner at
        # this junction, at distance r_conn.
        # Unit vector from C_inner to junction: (cos a, sin a).
        # C_conn_down center: at junction + r_conn · (unit vector from C_inner to junction)
        #   = junction + r_conn · ((jx-cx_i)/r_inner, (jy-cy_i)/r_inner)
        ux = (jx - cx_i) / r_inner
        uy = (jy - cy_i) / r_inner
        cx_cd = jx + r_conn * ux
        cy_cd = jy + r_conn * uy
        # On this connector's kissing circle, the junction angle = atan2 of
        # (junction - C_conn) = -(ux, uy), so angle = atan2(-uy, -ux).
        a_cd_start = atan2(-uy, -ux)
        a_cd_end = a_cd_start + pi / 3  # 60° CCW
        arcs.append(Arc(
            center=(cx_cd, cy_cd), radius=r_conn,
            angle_start=a_cd_start, angle_end=a_cd_end,
            sign=+1, label="conn_L1", level_created=1, is_sub_lobe=False,
        ))
    return arcs


# -----------------------------------------------------------------------------
# Diagnostics
# -----------------------------------------------------------------------------


def total_kappa(arcs: List[Arc]) -> float:
    return sum(a.signed_extent() for a in arcs)


def per_class_counts(arcs: List[Arc]) -> dict:
    out: dict = {}
    for a in arcs:
        out[a.label] = out.get(a.label, 0) + 1
    return out


def per_arc_extents(arcs: List[Arc]) -> dict:
    out: dict = {}
    for a in arcs:
        deg = round(a.angular_extent * 180 / pi, 1)
        out.setdefault(a.label, set()).add(deg)
    return {k: sorted(v) for k, v in out.items()}


# -----------------------------------------------------------------------------
# Rendering
# -----------------------------------------------------------------------------


def render_curve(ax, arcs: List[Arc], samples_per_arc: int = 100) -> None:
    xs, ys = [], []
    for a in arcs:
        x, y = a.sample(samples_per_arc)
        xs.append(x); ys.append(y)
    X = np.concatenate(xs); Y = np.concatenate(ys)
    ax.fill(X, Y, alpha=0.08, color="steelblue")
    for a in arcs:
        x, y = a.sample(samples_per_arc)
        if a.label.startswith("outer"):
            color = "crimson"
        elif a.label.startswith("inner"):
            color = "darkviolet"
        else:
            color = "darkorange"
        ax.plot(x, y, color=color, linewidth=1.2, alpha=0.95)


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--r-outer", type=float, default=1.0)
    parser.add_argument("--r-inner", type=float, default=0.3)
    parser.add_argument("--r-conn", type=float, default=0.2)
    parser.add_argument("--n-samples", type=int, default=100)
    parser.add_argument("--show", action="store_true")
    parser.add_argument(
        "--outputs-dir", type=Path,
        default=Path(__file__).resolve().parents[1] / "outputs",
    )
    parser.add_argument("--variants", type=str, default=None,
                        help="Comma-separated triples r_outer:r_inner:r_conn "
                             "to render in a panel.")
    args = parser.parse_args()

    # Build a panel either of multiple parameter variants or just one.
    if args.variants:
        cfgs = []
        for triple in args.variants.split(","):
            ro, ri, rc = (float(x) for x in triple.split(":"))
            cfgs.append((ro, ri, rc))
    else:
        cfgs = [(args.r_outer, args.r_inner, args.r_conn)]

    n_panels = len(cfgs)
    fig, axes = plt.subplots(1, n_panels, figsize=(5.5 * n_panels, 5.8))
    if n_panels == 1:
        axes = [axes]

    max_extent = 0.0
    all_arcs = []
    for cfg in cfgs:
        arcs = build_clover_inverse_arcs(*cfg)
        all_arcs.append(arcs)
        D_outer = cfg[0] + cfg[1]
        max_extent = max(max_extent, 1.15 * (D_outer + cfg[0]))

    for i, (cfg, arcs) in enumerate(zip(cfgs, all_arcs)):
        ax = axes[i]
        render_curve(ax, arcs, samples_per_arc=args.n_samples)
        ax.set_xlim(-max_extent, max_extent)
        ax.set_ylim(-max_extent, max_extent)
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.3)
        ax.axhline(0, color="gray", linewidth=0.4, alpha=0.4)
        ax.axvline(0, color="gray", linewidth=0.4, alpha=0.4)
        ax.set_xlabel("x")
        if i == 0:
            ax.set_ylabel("y")
        ro, ri, rc = cfg
        counts = per_class_counts(arcs)
        extents = per_arc_extents(arcs)
        title = (
            f"r_outer={ro:.2f}, r_inner={ri:.2f}, r_conn={rc:.2f}\n"
            f"D_outer={ro+ri:.2f}, D_inner={ro-rc:.2f}\n"
            f"{counts}\n"
            f"∫κds = {total_kappa(arcs):.3f} (target {2*pi:.3f})"
        )
        ax.set_title(title, fontsize=8)

    fig.suptitle(
        "Clover-inverse: 3 outer convex lobes + 3 inner concave lobes "
        "+ 6 connectors", fontsize=11,
    )
    plt.tight_layout(rect=[0, 0, 1, 0.94])

    args.outputs_dir.mkdir(parents=True, exist_ok=True)
    out_path = args.outputs_dir / (
        "clover_inverse_panel.png" if not args.variants
        else f"clover_inverse_variants.png"
    )
    fig.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"Saved: {out_path}")

    # Print a summary
    for cfg, arcs in zip(cfgs, all_arcs):
        ro, ri, rc = cfg
        print(f"\n--- r_outer={ro}, r_inner={ri}, r_conn={rc} ---")
        print(f"  D_outer = {ro + ri:.4f}")
        print(f"  D_inner = {ro - rc:.4f}")
        print(f"  inner-lobe max bound = {(ro - rc) * SQRT3 / 2:.4f}")
        print(f"  arcs: {len(arcs)} total, classes = {per_class_counts(arcs)}")
        print(f"  ∫κ ds = {total_kappa(arcs):.6f} (target {2*pi:.6f})")
        print(f"  per-class angular extents: {per_arc_extents(arcs)}")

    if args.show:
        plt.show()


if __name__ == "__main__":
    main()
