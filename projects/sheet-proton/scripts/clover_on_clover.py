"""
Render the nested fractal clover-on-clover cross-section profile.

Implements the recursive inscription rule specified in work/clover-on-clover.md:
each parent arc receives a balanced sub-feature unit (1 sub-lobe + 2 sub-saddles)
inscribed symmetrically about the parent arc midpoint. Iterates to user-specified
recursion depth.

Usage:
    python scripts/clover_on_clover.py [--max-level N]
                                       [--r-lobe-0 R0] [--chi-0 CHI0]
                                       [--rho-list RHO1,RHO2,...]
                                       [--chi-list CHI1,CHI2,...]
                                       [--delta-frac F]
                                       [--n-samples N] [--show]
                                       [--show-centers] [--no-color-by-sign]

Default produces a 3-panel figure with levels 1, 2, 3.

Outputs:
    outputs/clover_on_clover_panel_L<max_level>_chi0_<chi0>_delta<df>.png

Per work/clover-on-clover.md §3: each fractal level introduces a new length
scale via two parameters (rho_n = inter-level shrinkage, chi_n = per-level
saddle/lobe asymmetry).

Implementation notes and limitations
====================================

The script uses a SIMPLIFIED TANGENCY scheme:
  * Sub-saddle centers are placed tangent to the parent at entry/exit points
    (delta_frac of the parent arc's angular extent away from the midpoint).
  * Sub-lobe center is solved for by external-tangency with both sub-saddles.
  * Sub-arc angular extents are then COMPUTED FROM GEOMETRY, not enforced.

Consequence: the resulting sub-arcs do NOT in general have the canonical
240/120-degree extents that the work file spec requires. The script reports a
per-arc charge audit at each level (mean +0.67 for lobes / -0.33 for saddles
at level 0, decaying toward zero at deeper levels). The fractal structure
is visually correct, but strict charge preservation as in work/clover-on-clover.md
requires an additional constraint solver (deferred).

The parameter delta_frac must lie in a narrow window:
  * Too small => sub-lobe ends up INSIDE the parent's curve (notch, not bump).
  * Too large => sub-saddle centers are too far apart for the sub-lobe to bridge
    (inscription fails; parent kept unchanged).
The default delta_frac=0.22 with rho=0.3 produces visible outward bumps for
the level-0 parent lobes (r_p=1.0) at the cost of small bumps relative to the
parent size. For more visible recursion, try --rho-list 0.45,0.45,0.45 with
--delta-frac 0.30.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from math import pi, atan2, sqrt
from pathlib import Path
from typing import List, Tuple

import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Arc data structure
# -----------------------------------------------------------------------------


@dataclass
class Arc:
    """One circular-arc segment of the cross-section boundary.

    Conventions:
        - center: (x, y) of the kissing circle's center
        - radius: positive scalar
        - angle_start, angle_end: in radians; the arc is traced by sweeping
          the angle linearly from angle_start to angle_end
        - sign: +1 for convex (lobe-like, traversed CCW on its circle so
          angle_end > angle_start by 4*pi/3); -1 for concave (saddle-like,
          traversed CW so angle_end < angle_start by 2*pi/3)

    Curvature contribution to ∫κ ds (used for charge accounting):
        sign=+1: ∫κ ds = +(angle_end - angle_start) = +4*pi/3 for full lobe
        sign=-1: ∫κ ds = +(angle_start - angle_end) ... actually computed
                 as (1/radius) * sign * arc_length, see kappa_integral().
    """

    center: Tuple[float, float]
    radius: float
    angle_start: float
    angle_end: float
    sign: int  # +1 (lobe / convex) or -1 (saddle / concave)

    @property
    def angular_extent(self) -> float:
        """Magnitude of the angular sweep (always positive)."""
        return abs(self.angle_end - self.angle_start)

    @property
    def arc_length(self) -> float:
        return self.radius * self.angular_extent

    def kappa_integral(self) -> float:
        """Signed curvature integrated along this arc segment (= per-2*pi charge * 2*pi)."""
        return self.sign * self.angular_extent

    def sample(self, n: int = 100) -> Tuple[np.ndarray, np.ndarray]:
        """Sample (x, y) coordinates along the arc."""
        t = np.linspace(0.0, 1.0, n)
        angles = self.angle_start + t * (self.angle_end - self.angle_start)
        x = self.center[0] + self.radius * np.cos(angles)
        y = self.center[1] + self.radius * np.sin(angles)
        return x, y

    def point_at(self, t: float) -> Tuple[float, float]:
        """Return (x, y) at parameter t in [0, 1] along the arc."""
        a = self.angle_start + t * (self.angle_end - self.angle_start)
        return (
            self.center[0] + self.radius * np.cos(a),
            self.center[1] + self.radius * np.sin(a),
        )

    def midpoint(self) -> Tuple[float, float]:
        return self.point_at(0.5)


# -----------------------------------------------------------------------------
# Level 0 clover construction
# -----------------------------------------------------------------------------


def build_level0_clover(r_lobe: float, r_saddle: float) -> List[Arc]:
    """Build the standard kissing-circle clover at level 0.

    Returns 6 arcs in CCW traversal order:
        lobe-1, saddle-1, lobe-2, saddle-2, lobe-3, saddle-3

    Lobe centers at angles 0, 120, 240 deg from origin at radius d = r_lobe + r_saddle.
    Saddle centers at angles 60, 180, 300 deg at the same radius d (kissing circle
    relation d = r_lobe + r_saddle from clover-quarks.md §7).
    """
    d = r_lobe + r_saddle
    arcs: List[Arc] = []
    for k in range(3):
        # Lobe k centered at angle (2*pi/3) * k from origin
        alpha_L = 2.0 * pi / 3.0 * k
        cx_L = d * np.cos(alpha_L)
        cy_L = d * np.sin(alpha_L)
        # 240-deg arc CCW on the lobe circle, centered on the outward direction
        # The outward direction (from origin) is at angle alpha_L from origin,
        # which is also the angle from the lobe center to its outermost point.
        # The arc spans alpha_L - 120 deg to alpha_L + 120 deg on the lobe circle.
        arcs.append(
            Arc(
                center=(cx_L, cy_L),
                radius=r_lobe,
                angle_start=alpha_L - 2.0 * pi / 3.0,
                angle_end=alpha_L + 2.0 * pi / 3.0,
                sign=+1,
            )
        )
        # Saddle k+1/2 centered at angle alpha_L + 60 deg
        alpha_S = alpha_L + pi / 3.0
        cx_S = d * np.cos(alpha_S)
        cy_S = d * np.sin(alpha_S)
        # 120-deg arc traversed CW on the saddle circle, passing through the
        # saddle's INWARD midpoint (the point on the saddle circle closest to
        # origin, at angle alpha_S - pi on the saddle circle = alpha_S + pi).
        # Entry (junction with lobe-k): at angle alpha_S - 2*pi/3 on saddle circle.
        # Exit (junction with lobe-(k+1)): at angle alpha_S - 4*pi/3 (= alpha_S + 2*pi/3
        # mod 2*pi). Using the continuous angle alpha_S - 4*pi/3 (NOT the mod-2*pi
        # equivalent) gives a CW sweep of -2*pi/3 (short way, through the inward
        # midpoint at alpha_S - pi).
        arcs.append(
            Arc(
                center=(cx_S, cy_S),
                radius=r_saddle,
                angle_start=alpha_S - 2.0 * pi / 3.0,
                angle_end=alpha_S - 4.0 * pi / 3.0,
                sign=-1,
            )
        )
    return arcs


# -----------------------------------------------------------------------------
# Inscription: replace one parent arc with [parent_partial, S, L, S, parent_partial]
# -----------------------------------------------------------------------------


def inscribe_balanced_unit(
    parent: Arc, r_sub_lobe: float, r_sub_saddle: float, delta_frac: float = 0.4
) -> List[Arc]:
    """Replace the central portion of parent with a balanced sub-feature unit.

    The unit consists of: [sub_saddle_1, sub_lobe, sub_saddle_2]. It is
    inscribed symmetrically about the parent arc's midpoint.

    delta_frac controls how wide the inscribed region is. The unit replaces
    the parent's angular sweep from (midpoint - delta_frac/2 * extent) to
    (midpoint + delta_frac/2 * extent). Smaller delta_frac means the unit
    occupies less of the parent and the sub-saddles are placed nearer to the
    midpoint.

    Returns 5 arcs in CCW traversal order:
        [parent_partial_in, sub_saddle_1, sub_lobe, sub_saddle_2, parent_partial_out]

    The sub-saddle radius and sub-lobe radius are inputs. The sub-feature
    angular extents are 120 deg (sub-saddle) and 240 deg (sub-lobe) -- the
    per-arc charges are then +2/3 (sub-lobe) and -1/3 (sub-saddle) by
    Gauss-Bonnet, independent of the chosen radii.

    Tangency at the four junctions:
        parent <-> sub_saddle_1:  same-sign or opposite-sign depending on
                                  parent's sign. We compute the sub-saddle
                                  center on the appropriate side.
        sub_saddle_1 <-> sub_lobe: opposite-sign, external tangency
                                   distance = r_sub_lobe + r_sub_saddle.

    Implementation: place sub-saddle centers tangent to parent at the chosen
    entry/exit points, then place sub-lobe center along the parent midpoint's
    interior normal at distance such that it is tangent to both sub-saddles.
    """
    cx, cy = parent.center
    r_p = parent.radius
    a_start = parent.angle_start
    a_end = parent.angle_end
    sweep = a_end - a_start  # signed
    a_mid = a_start + 0.5 * sweep

    # Entry/exit angles on parent circle
    half_delta = 0.5 * delta_frac * sweep
    a_in = a_mid - half_delta
    a_out = a_mid + half_delta

    # Entry/exit points
    P_in = (cx + r_p * np.cos(a_in), cy + r_p * np.sin(a_in))
    P_out = (cx + r_p * np.cos(a_out), cy + r_p * np.sin(a_out))

    # Compute sub-saddle centers. A sub-saddle is concave (sign=-1). Its center
    # sits on the EXTERIOR side of the cross-section curve relative to the
    # junction point.
    #
    # For a CCW-traversed parent lobe (sign=+1): the parent's center is on the
    # interior side. Sub-saddle (concave): its center on opposite side from
    # parent's center. External tangency:
    #     C_subS = P_junction + r_subS * (P_junction - C_parent)/r_parent
    #
    # For a CW-traversed parent saddle (sign=-1): the parent's center is on the
    # exterior side. Sub-saddle (also concave): same side as parent's center.
    # Internal tangency (sub-saddle inside parent circle):
    #     C_subS = P_junction + r_subS * (C_parent - P_junction)/r_parent
    #            = P_junction - r_subS * (P_junction - C_parent)/r_parent
    #
    # Combined formula using parent.sign:
    #     C_subS = P_junction + sign(parent) * r_subS * (P_junction - C_parent)/r_parent
    def sub_saddle_center(P_junc, sign_par):
        dx = P_junc[0] - cx
        dy = P_junc[1] - cy
        unit = (dx / r_p, dy / r_p)
        return (
            P_junc[0] + sign_par * r_sub_saddle * unit[0],
            P_junc[1] + sign_par * r_sub_saddle * unit[1],
        )

    C_S1 = sub_saddle_center(P_in, parent.sign)
    C_S2 = sub_saddle_center(P_out, parent.sign)

    # Sub-lobe center: must be tangent to both sub-saddles externally
    # (sub-lobe convex, sub-saddle concave, opposite signs => external tangency).
    # Distance constraint: |C_L - C_S1| = |C_L - C_S2| = r_sub_lobe + r_sub_saddle.
    # By symmetry, C_L lies on the perpendicular bisector of the segment
    # C_S1-C_S2, which passes through the parent arc midpoint.
    P_mid = (cx + r_p * np.cos(a_mid), cy + r_p * np.sin(a_mid))
    # Midpoint of C_S1-C_S2 segment
    Mss_x = 0.5 * (C_S1[0] + C_S2[0])
    Mss_y = 0.5 * (C_S1[1] + C_S2[1])
    # Half-distance between sub-saddle centers
    d_S1S2 = sqrt((C_S2[0] - C_S1[0]) ** 2 + (C_S2[1] - C_S1[1]) ** 2)
    h = 0.5 * d_S1S2
    # Distance from Mss along perpendicular bisector to C_L
    tangent_sum = r_sub_lobe + r_sub_saddle
    if h >= tangent_sum:
        # Cannot fit: sub-saddles are farther apart than the lobe can bridge.
        # Caller should choose smaller delta_frac or larger r_sub_lobe.
        raise ValueError(
            f"Cannot inscribe unit on parent (r={r_p:.4f}): sub-saddle "
            f"centers separated by {d_S1S2:.4f} > 2*(r_lobe+r_saddle)="
            f"{2*tangent_sum:.4f}. Reduce delta_frac or increase sub-radii."
        )
    perp_dist = sqrt(tangent_sum * tangent_sum - h * h)

    # Direction from C_S midpoint toward parent midpoint (interior side
    # relative to the chord between sub-saddle junctions)
    # Sub-lobe should be on the OPPOSITE side from where the sub-saddles' centers
    # sit relative to the parent curve.
    #
    # For a parent lobe (sign=+1): sub-saddles' centers are on the exterior
    # side (outside the parent circle). Sub-lobe's center should be on the
    # INTERIOR side (inside the parent circle, same side as C_parent).
    #
    # For a parent saddle (sign=-1): sub-saddles' centers are on the exterior
    # side (further out from cross-section center, same side as C_parent
    # since C_parent is on the exterior for saddles). Sub-lobe's center should
    # be on the INTERIOR side (toward the cross-section interior).
    #
    # In both cases, the sub-lobe sits on the INTERIOR-side normal at the
    # parent midpoint. Interior normal = -sign(parent) * (M - C_parent)/r_parent.
    n_int_x = -parent.sign * (P_mid[0] - cx) / r_p
    n_int_y = -parent.sign * (P_mid[1] - cy) / r_p
    C_L = (Mss_x + perp_dist * n_int_x, Mss_y + perp_dist * n_int_y)

    # Now compute the sub-arc angle ranges.
    #
    # Sub-saddle 1: 120 deg arc, sign=-1 (concave, CW traversal). Starts
    # tangent to parent at P_in, ends tangent to sub-lobe at the junction
    # point J1 on the sub-saddle-1 circle. Angles measured from C_S1.
    def angle_of(P, C):
        return atan2(P[1] - C[1], P[0] - C[0])

    # Junction point J1: on the line between C_S1 and C_L, at distance
    # r_sub_saddle from C_S1 (and r_sub_lobe from C_L).
    def junction_pt(C1, C2, r1):
        dx = C2[0] - C1[0]
        dy = C2[1] - C1[1]
        d = sqrt(dx * dx + dy * dy)
        return (C1[0] + r1 * dx / d, C1[1] + r1 * dy / d)

    J1 = junction_pt(C_S1, C_L, r_sub_saddle)
    J2 = junction_pt(C_S2, C_L, r_sub_saddle)

    # Sub-saddle 1 arc: from angle(P_in) to angle(J1), CW (sign=-1).
    # CW means we decrease the angle. Need the SHORT path from start to end
    # going CW (decreasing). If start > end, just sweep directly. If start < end,
    # subtract 2*pi from end to make the sweep negative.
    a_S1_start = angle_of(P_in, C_S1)
    a_S1_end = angle_of(J1, C_S1)
    sweep_S1 = a_S1_end - a_S1_start
    # Force CW (negative sweep). If sweep is positive (>0), wrap by subtracting 2pi.
    while sweep_S1 > 0:
        sweep_S1 -= 2 * pi
    # If sweep is less than -2pi, add 2pi
    while sweep_S1 < -2 * pi:
        sweep_S1 += 2 * pi
    a_S1_end_corrected = a_S1_start + sweep_S1

    # Sub-saddle 2 arc: similarly, from angle(J2) to angle(P_out), CW.
    a_S2_start = angle_of(J2, C_S2)
    a_S2_end = angle_of(P_out, C_S2)
    sweep_S2 = a_S2_end - a_S2_start
    while sweep_S2 > 0:
        sweep_S2 -= 2 * pi
    while sweep_S2 < -2 * pi:
        sweep_S2 += 2 * pi
    a_S2_end_corrected = a_S2_start + sweep_S2

    # Sub-lobe arc: from angle(J1) to angle(J2) on C_L circle, CCW (sign=+1).
    a_L_start = angle_of(J1, C_L)
    a_L_end = angle_of(J2, C_L)
    sweep_L = a_L_end - a_L_start
    while sweep_L < 0:
        sweep_L += 2 * pi
    while sweep_L > 2 * pi:
        sweep_L -= 2 * pi
    a_L_end_corrected = a_L_start + sweep_L

    # Parent partial-in: from a_start to a_in (preserve parent sign)
    parent_in = Arc(
        center=parent.center,
        radius=parent.radius,
        angle_start=a_start,
        angle_end=a_in,
        sign=parent.sign,
    )
    sub_saddle_1 = Arc(
        center=C_S1,
        radius=r_sub_saddle,
        angle_start=a_S1_start,
        angle_end=a_S1_end_corrected,
        sign=-1,
    )
    sub_lobe = Arc(
        center=C_L,
        radius=r_sub_lobe,
        angle_start=a_L_start,
        angle_end=a_L_end_corrected,
        sign=+1,
    )
    sub_saddle_2 = Arc(
        center=C_S2,
        radius=r_sub_saddle,
        angle_start=a_S2_start,
        angle_end=a_S2_end_corrected,
        sign=-1,
    )
    parent_out = Arc(
        center=parent.center,
        radius=parent.radius,
        angle_start=a_out,
        angle_end=a_end,
        sign=parent.sign,
    )

    return [parent_in, sub_saddle_1, sub_lobe, sub_saddle_2, parent_out]


# -----------------------------------------------------------------------------
# Recursive build
# -----------------------------------------------------------------------------


def build_fractal_clover(
    r_lobe_0: float,
    chi_0: float,
    rhos: List[float],
    chis: List[float],
    delta_frac: float = 0.4,
) -> List[List[Arc]]:
    """Build the fractal clover up to N levels of recursion.

    Returns a list of arc-lists, one per level (level 0 = base clover, level k
    after applying k inscriptions).

    Parameters
    ----------
    r_lobe_0 : float
        Lobe radius at level 0.
    chi_0 : float
        r_saddle_0 / r_lobe_0 at level 0.
    rhos : list of float
        For each level k >= 1: rho_k = r_lobe_k / r_lobe_{k-1}. Must have
        len(rhos) = max_level.
    chis : list of float
        For each level k >= 1: chi_k = r_saddle_k / r_lobe_k. Must have
        len(chis) = max_level.
    delta_frac : float
        Fraction of each parent arc's angular sweep occupied by the inscribed
        unit. Smaller => smaller sub-features relative to the parent.
    """
    r_saddle_0 = chi_0 * r_lobe_0
    level0 = build_level0_clover(r_lobe_0, r_saddle_0)
    levels = [level0]

    r_lobe_n = r_lobe_0
    for k, (rho, chi) in enumerate(zip(rhos, chis), start=1):
        r_lobe_n = rho * r_lobe_n
        r_saddle_n = chi * r_lobe_n
        new_arcs: List[Arc] = []
        for arc in levels[-1]:
            try:
                new_arcs.extend(
                    inscribe_balanced_unit(arc, r_lobe_n, r_saddle_n, delta_frac)
                )
            except ValueError:
                # Cannot inscribe on this arc at the chosen parameters --
                # keep the parent arc unchanged.
                new_arcs.append(arc)
        levels.append(new_arcs)

    return levels


# -----------------------------------------------------------------------------
# Rendering
# -----------------------------------------------------------------------------


def render_curve(
    ax,
    arcs: List[Arc],
    samples_per_arc: int = 60,
    show_centers: bool = False,
    color_by_sign: bool = True,
) -> None:
    """Draw the closed curve formed by the arc list.

    If color_by_sign is True, lobe arcs are drawn in red and saddle arcs in
    green so the fractal's lobe/saddle alternation is visually clear.
    """
    # First the filled interior, sampled densely from all arcs concatenated:
    xs_all = []
    ys_all = []
    for arc in arcs:
        x, y = arc.sample(samples_per_arc)
        xs_all.append(x)
        ys_all.append(y)
    if not xs_all:
        return
    X = np.concatenate(xs_all)
    Y = np.concatenate(ys_all)
    ax.fill(X, Y, alpha=0.07, color="steelblue")

    # Now redraw each arc with sign-dependent color, for visual feature class
    if color_by_sign:
        for arc in arcs:
            x, y = arc.sample(samples_per_arc)
            color = "crimson" if arc.sign == +1 else "forestgreen"
            ax.plot(x, y, color=color, linewidth=0.9, alpha=0.95)
    else:
        ax.plot(X, Y, color="navy", linewidth=1.0)

    if show_centers:
        lobe_centers = {(round(a.center[0], 4), round(a.center[1], 4)) for a in arcs if a.sign == +1}
        saddle_centers = {(round(a.center[0], 4), round(a.center[1], 4)) for a in arcs if a.sign == -1}
        for c in lobe_centers:
            ax.plot(c[0], c[1], "o", color="crimson", markersize=1.8, alpha=0.4)
        for c in saddle_centers:
            ax.plot(c[0], c[1], "s", color="forestgreen", markersize=1.8, alpha=0.4)


def total_kappa_integral(arcs: List[Arc]) -> float:
    """Total ∫κ ds over the closed curve. Should be 2π for a simple closed curve."""
    return sum(a.kappa_integral() for a in arcs)


def count_features(arcs: List[Arc]) -> Tuple[int, int]:
    """(n_lobe_arcs, n_saddle_arcs)."""
    n_l = sum(1 for a in arcs if a.sign == +1)
    n_s = sum(1 for a in arcs if a.sign == -1)
    return n_l, n_s


def per_arc_charge_audit(arcs: List[Arc]) -> dict:
    """Report mean / min / max per-arc charge for lobe and saddle arcs.

    Spec target (work/clover-on-clover.md §3): each lobe arc has +2/3 charge
    and each saddle arc has -1/3 charge, from canonical 240/120-degree extents.

    The current implementation uses geometric tangency that does NOT in general
    produce canonical 240/120 extents at sub-levels; this audit shows the
    deviation. For strict spec compliance, the construction needs an additional
    constraint solver (deferred — see work/clover-on-clover.md §5).
    """
    lobe_charges = []
    saddle_charges = []
    for a in arcs:
        # Per-closure-path charge = (1/2*pi) * |∫κ ds| = (1/2*pi) * sign * sweep
        # For positive κ (lobe), 4*pi/3 sweep -> charge +2/3.
        # For negative κ (saddle), 2*pi/3 sweep -> charge -1/3.
        q = a.kappa_integral() / (2.0 * pi)
        if a.sign == +1:
            lobe_charges.append(q)
        else:
            saddle_charges.append(q)
    out = {}
    if lobe_charges:
        out["lobe_mean"] = float(np.mean(lobe_charges))
        out["lobe_min"] = float(np.min(lobe_charges))
        out["lobe_max"] = float(np.max(lobe_charges))
    if saddle_charges:
        out["saddle_mean"] = float(np.mean(saddle_charges))
        out["saddle_min"] = float(np.min(saddle_charges))
        out["saddle_max"] = float(np.max(saddle_charges))
    return out


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--max-level",
        type=int,
        default=3,
        help="Maximum recursion level (default: 3). Levels 1..max-level are rendered.",
    )
    parser.add_argument(
        "--r-lobe-0", type=float, default=1.0, help="Level-0 lobe radius (default: 1.0)"
    )
    parser.add_argument(
        "--chi-0",
        type=float,
        default=0.5,
        help="Level-0 saddle/lobe radius ratio (default: 0.5)",
    )
    parser.add_argument(
        "--rho-list",
        type=str,
        default=None,
        help="Comma-separated inter-level shrinkage factors rho_1,rho_2,... "
        "Default: 0.3 at every level.",
    )
    parser.add_argument(
        "--chi-list",
        type=str,
        default=None,
        help="Comma-separated per-level saddle/lobe ratios chi_1,chi_2,... "
        "Default: 1.0 at every sub-level (symmetric).",
    )
    parser.add_argument(
        "--delta-frac",
        type=float,
        default=0.22,
        help="Fraction of each parent arc occupied by inscribed unit "
        "(default: 0.22). delta_frac must be chosen in a narrow window: "
        "large enough that sub-lobes bump OUTWARD (otherwise the inscription "
        "is an inward notch), small enough that sub-saddle centers can be "
        "bridged by the sub-lobe.",
    )
    parser.add_argument(
        "--n-samples",
        type=int,
        default=60,
        help="Samples per arc segment for rendering (default: 60).",
    )
    parser.add_argument(
        "--show", action="store_true", help="Display the figure interactively"
    )
    parser.add_argument(
        "--show-centers",
        action="store_true",
        help="Show lobe-circle / saddle-circle centers as small markers",
    )
    parser.add_argument(
        "--no-color-by-sign",
        dest="color_by_sign",
        action="store_false",
        help="Draw the curve in a single navy color rather than sign-coloring "
        "lobes red and saddles green.",
    )
    parser.set_defaults(color_by_sign=True)
    parser.add_argument(
        "--outputs-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "outputs",
        help="Output directory",
    )
    args = parser.parse_args()

    if args.rho_list is not None:
        rhos = [float(x) for x in args.rho_list.split(",")]
    else:
        rhos = [0.3] * args.max_level
    if args.chi_list is not None:
        chis = [float(x) for x in args.chi_list.split(",")]
    else:
        chis = [1.0] * args.max_level

    if len(rhos) < args.max_level or len(chis) < args.max_level:
        parser.error(
            f"--rho-list and --chi-list must each have at least {args.max_level} entries"
        )

    rhos = rhos[: args.max_level]
    chis = chis[: args.max_level]

    levels = build_fractal_clover(
        r_lobe_0=args.r_lobe_0,
        chi_0=args.chi_0,
        rhos=rhos,
        chis=chis,
        delta_frac=args.delta_frac,
    )

    print(f"Built {len(levels)} levels (0..{len(levels)-1})")
    for k, arcs in enumerate(levels):
        n_l, n_s = count_features(arcs)
        total_kappa = total_kappa_integral(arcs)
        charges = per_arc_charge_audit(arcs)
        lobe_str = (
            f"Q_lobe mean={charges['lobe_mean']:+.4f} "
            f"(spec +0.6667, range [{charges['lobe_min']:+.4f},{charges['lobe_max']:+.4f}])"
            if "lobe_mean" in charges
            else "no lobes"
        )
        saddle_str = (
            f"Q_saddle mean={charges['saddle_mean']:+.4f} "
            f"(spec -0.3333, range [{charges['saddle_min']:+.4f},{charges['saddle_max']:+.4f}])"
            if "saddle_mean" in charges
            else "no saddles"
        )
        print(
            f"  Level {k}: {len(arcs)} arcs ({n_l} lobes + {n_s} saddles), "
            f"total ∫κ ds = {total_kappa:.4f} (target {2*pi:.4f})"
        )
        print(f"    {lobe_str}")
        print(f"    {saddle_str}")

    # Render the levels 1..max_level in a horizontal panel
    n_panels = args.max_level
    fig, axes = plt.subplots(1, n_panels, figsize=(5.5 * n_panels, 5.8))
    if n_panels == 1:
        axes = [axes]

    # Pick a uniform display extent based on the level-0 size
    extent = 1.15 * (args.r_lobe_0 + args.chi_0 * args.r_lobe_0 + args.r_lobe_0)

    for i, level_idx in enumerate(range(1, args.max_level + 1)):
        ax = axes[i]
        arcs = levels[level_idx]
        render_curve(
            ax,
            arcs,
            samples_per_arc=args.n_samples,
            show_centers=args.show_centers,
            color_by_sign=args.color_by_sign,
        )
        ax.set_xlim(-extent, extent)
        ax.set_ylim(-extent, extent)
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.3)
        ax.axhline(0, color="gray", linewidth=0.4, alpha=0.4)
        ax.axvline(0, color="gray", linewidth=0.4, alpha=0.4)
        ax.set_xlabel("x")
        if i == 0:
            ax.set_ylabel("y")
        n_l, n_s = count_features(arcs)
        if level_idx == 1:
            scale_str = f"rho_1={rhos[0]:.3f}, chi_1={chis[0]:.3f}"
        else:
            scale_str = "  ".join(
                f"rho_{k+1}={rhos[k]:.3f}, chi_{k+1}={chis[k]:.3f}"
                for k in range(level_idx)
            )
        ax.set_title(
            f"Level {level_idx}\n"
            f"{n_l} lobes + {n_s} saddles  ({len(arcs)} arcs)\n"
            f"{scale_str}",
            fontsize=9,
        )

    fig.suptitle(
        f"Clover-on-clover fractal cross-section  "
        f"(r_lobe_0={args.r_lobe_0:.2f}, chi_0={args.chi_0:.2f}, "
        f"delta_frac={args.delta_frac:.2f})",
        fontsize=11,
    )
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    args.outputs_dir.mkdir(parents=True, exist_ok=True)
    out_path = (
        args.outputs_dir
        / f"clover_on_clover_panel_L{args.max_level}_chi0_{args.chi_0:.2f}"
        f"_delta{args.delta_frac:.2f}.png"
    )
    fig.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"\nSaved: {out_path}")

    if args.show:
        plt.show()


if __name__ == "__main__":
    main()
