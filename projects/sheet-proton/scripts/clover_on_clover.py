"""
Render the bisect-and-insert primitive-replacement fractal clover.

Construction (per design discussion):
  * Primitive: S-L-L-S where lobe arcs sum to 2/3 of the primitive's net rotation
    and saddle arcs sum to 1/3. At level n the primitive's lobe arcs are
    120° / 2^(n-1) each and saddle arcs are 60° / 2^(n-1) each.
        Level 1 primitive: S60-L120-L120-S60, net rotation +120°.
        Level 2 primitive: S30-L60-L60-S30, net rotation +60°.
        Level 3 primitive: S15-L30-L30-S15, net rotation +30°.
  * Level 1: the basic clover, rendered as 3 primitives joined into a
    simple closed curve. Geometrically identical to the standard
    3-lobe-3-saddle clover.
  * Level n+1: each lobe arc of level n is BISECTED, its central HALF removed,
    and a level-(n+1) primitive inserted in the gap. The removed half has
    rotation equal to the inserted primitive's rotation, so Gauss-Bonnet is
    preserved exactly (total ∫κ ds = 2π at every level, no self-intersection).
    Saddle arcs are NEVER modified.

Geometric constraint (one DOF per level):
    Forcing canonical sub-arc extents and C¹ continuity yields
        r_p = r_L_new · √3 + r_S_new · (√3 − 1)
    where r_p is the parent lobe radius being bisected. The user picks
    r_L_new freely (within [r_p / (2·√3 - 1), r_p / √3]) and r_S_new is
    determined.

Usage:
    python scripts/clover_on_clover.py [--max-level N]
                                       [--r-lobe-1 R1] [--r-saddle-1 RS1]
                                       [--lobe-shrink-list F2,F3,...]
                                       [--n-samples N] [--show]

Each --lobe-shrink F is r_L_(n) / r_L_(n-1). Saddle radii are computed from
the closure constraint and reported. Default lobe-shrink = 0.5 at every level.

Outputs:
    outputs/clover_on_clover_L<max_level>_panel.png
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import pi, atan2, sqrt, cos, sin
from pathlib import Path
from typing import List, Tuple

import numpy as np
import matplotlib.pyplot as plt


SQRT3 = sqrt(3.0)


# -----------------------------------------------------------------------------
# Arc data structure
# -----------------------------------------------------------------------------


@dataclass
class Arc:
    center: Tuple[float, float]
    radius: float
    angle_start: float
    angle_end: float
    sign: int  # +1 convex (CCW), -1 concave (CW)
    label: str = ""
    level_created: int = 1  # Level at which this arc was created.
    is_sub_lobe: bool = False  # True for newly-inserted primitive sub-lobes
                                # (bisectable at the next level).

    @property
    def angular_extent(self) -> float:
        return abs(self.angle_end - self.angle_start)

    @property
    def signed_extent(self) -> float:
        """Signed rotation contribution: positive for convex, negative for concave."""
        return self.sign * self.angular_extent

    def kappa_integral(self) -> float:
        return self.sign * self.angular_extent

    def sample(self, n: int = 100) -> Tuple[np.ndarray, np.ndarray]:
        t = np.linspace(0.0, 1.0, n)
        a = self.angle_start + t * (self.angle_end - self.angle_start)
        return (
            self.center[0] + self.radius * np.cos(a),
            self.center[1] + self.radius * np.sin(a),
        )


# -----------------------------------------------------------------------------
# Geometric helpers
# -----------------------------------------------------------------------------


def saddle_radius_for_lobe(r_p: float, r_L_new: float, A: float) -> float:
    """Solve r_p = 2 r_L_new cos(A/4) + r_S_new (2 cos(A/4) − 1) for r_S_new.

    A is the parent lobe's angular extent in radians. For A = 2π/3 (level 1 →
    level 2, parent L120), this reduces to r_p = r_L √3 + r_S (√3 − 1).
    """
    c = cos(A / 4.0)
    return (r_p - 2.0 * r_L_new * c) / (2.0 * c - 1.0)


def valid_lobe_shrink_range(A: float, r_p: float = 1.0) -> Tuple[float, float]:
    """Range of valid r_L_new / r_p for parent extent A:
       - min: r_S_new = r_L_new (symmetric) gives r_L_new = r_p / (4 cos(A/4) − 1)
       - max: r_S_new = 0 gives r_L_new = r_p / (2 cos(A/4))
    """
    c = cos(A / 4.0)
    lo = r_p / (4.0 * c - 1.0)
    hi = r_p / (2.0 * c)
    return lo, hi


# -----------------------------------------------------------------------------
# Level 1: the basic clover as 3 primitives = 12 arcs
# -----------------------------------------------------------------------------


def build_level1_clover(r_L: float, r_S: float) -> List[Arc]:
    """
    Build the level-1 clover: 6 lobe arcs (120° each) + 6 saddle arcs (60° each),
    in CCW traversal order forming 3 primitives (S60-L120-L120-S60 each, with
    consecutive primitives sharing tangent points).

    The 3 main lobes are at angles 0, 120°, 240° from the origin at distance
    d = r_L + r_S. The 3 main saddles are at 60°, 180°, 300°.
    """
    arcs: List[Arc] = []
    d = r_L + r_S
    for k in range(3):
        alpha_L = 2 * pi * k / 3.0
        # Saddle preceding this lobe (second half of the saddle, from inward midpoint to lobe)
        alpha_S_prev = alpha_L - pi / 3.0
        cx_Sp = d * cos(alpha_S_prev)
        cy_Sp = d * sin(alpha_S_prev)
        a_Sp_mid = alpha_S_prev - pi               # inward midpoint
        a_Sp_end = alpha_S_prev - 4 * pi / 3.0      # junction with this lobe
        arcs.append(
            Arc(
                center=(cx_Sp, cy_Sp),
                radius=r_S,
                angle_start=a_Sp_mid,
                angle_end=a_Sp_end,
                sign=-1,
                label="S60_L1",
            )
        )
        # Lobe k (240°, split into two L120 halves at outward midpoint)
        cx_L = d * cos(alpha_L)
        cy_L = d * sin(alpha_L)
        a_L_start = alpha_L - 2 * pi / 3.0
        a_L_mid = alpha_L
        a_L_end = alpha_L + 2 * pi / 3.0
        arcs.append(
            Arc(
                center=(cx_L, cy_L),
                radius=r_L,
                angle_start=a_L_start,
                angle_end=a_L_mid,
                sign=+1,
                label="L120_L1",
                level_created=1,
                is_sub_lobe=True,
            )
        )
        arcs.append(
            Arc(
                center=(cx_L, cy_L),
                radius=r_L,
                angle_start=a_L_mid,
                angle_end=a_L_end,
                sign=+1,
                label="L120_L1",
                level_created=1,
                is_sub_lobe=True,
            )
        )
        # Saddle following this lobe (first half)
        alpha_S_next = alpha_L + pi / 3.0
        cx_Sn = d * cos(alpha_S_next)
        cy_Sn = d * sin(alpha_S_next)
        a_Sn_start = alpha_S_next - 2 * pi / 3.0   # junction with this lobe
        a_Sn_mid = alpha_S_next - pi                # inward midpoint
        arcs.append(
            Arc(
                center=(cx_Sn, cy_Sn),
                radius=r_S,
                angle_start=a_Sn_start,
                angle_end=a_Sn_mid,
                sign=-1,
                label="S60_L1",
            )
        )
    return arcs


# -----------------------------------------------------------------------------
# Insertion: bisect a parent lobe arc and insert a level-(n+1) primitive in the gap
# -----------------------------------------------------------------------------


def insert_primitive_at_lobe_center(
    parent: Arc, r_L_new: float, level_label: int
) -> List[Arc]:
    """Bisect the parent L (any angular extent) and insert a level-(n+1)
    primitive (S-L-L-S) at the center, replacing the central HALF of the
    parent.

    The parent L has signed_extent = +A radians (with sign +1). The removed
    half has rotation +A/2. The inserted primitive has rotation +A/2 as well
    (lobe arcs at A/4 each, saddle arcs at A/8 each), so total rotation is
    preserved.

    r_L_new is the lobe radius for the inserted primitive. r_S_new is
    derived from the closure constraint:
        r_p = r_L_new · √3 + r_S_new · (√3 − 1)
    where r_p is the parent's radius.

    Returns 6 arcs in CCW order:
        [parent_left_half_inner, S_a, L_a, L_b, S_b, parent_right_half_inner]
    The "inner half" of each parent half (closer to the center of the
    original parent) is the part where the parent was cut; this is the
    actual remnant after removal of the central half.

    Wait — the user's design: parent L of extent A is split at midpoint,
    and the CENTRAL HALF (A/2 of extent centered on the midpoint) is REMOVED.
    The OUTER halves (A/4 each, on either side of the central region)
    REMAIN as parent remnants.

    So the 6 output arcs are:
        - parent_remnant_left (A/4 of parent, from start to start + A/4)
        - sub-saddle 1 (A/8 of new primitive)
        - sub-lobe a (A/4 of new primitive)
        - sub-lobe b (A/4 of new primitive)
        - sub-saddle 2 (A/8 of new primitive)
        - parent_remnant_right (A/4 of parent, from end - A/4 to end)

    With:
        sub_lobe_arc_extent = parent_extent / 2 = A/2 (total)  ← wait, no:
            Each sub-lobe is at radius r_L_new and has SIGNED extent +A/4
            (so two sub-lobes total +A/2 of rotation).
        sub_saddle_arc_extent = -A/8 each (so two sub-saddles total -A/4 of rotation).
        Total primitive rotation = +A/2 - A/4 = +A/4? NO wait that's wrong.

    Re-derive: parent total rotation = +A. Remove central half (extent A/2,
    contributing +A/2 to rotation). Insert primitive contributing what?

    For total rotation preserved (curve stays simple): insertion must
    contribute +A/2.

    Primitive structure (per user's spec): 2 sub-lobes + 2 sub-saddles.
    Let each sub-lobe contribute angle ℓ (positive) and each sub-saddle
    contribute angle s (positive, so signed contribution -s).

    Net primitive rotation = 2ℓ - 2s.
    Set = A/2: 2ℓ - 2s = A/2, i.e. ℓ - s = A/4.

    Also per the user: each sub-lobe is half of parent's lobe-arc-equivalent
    angular extent, and each sub-saddle is half of parent's saddle-arc-equivalent.

    For level 1 → 2: parent L120 has A = 120° = 2π/3. Removed central A/2 = 60°.
    Sub-lobes ℓ = 60° = π/3 each. Sub-saddles s = 30° = π/6 each.
    ℓ - s = 60° - 30° = 30° = A/4. ✓

    For level 2 → 3: parent L60 has A = 60° = π/3. Removed central A/2 = 30°.
    Sub-lobes ℓ = 30° each. Sub-saddles s = 15° each.
    ℓ - s = 15° = A/4. ✓

    So the angular extents scale linearly with the parent's extent.
    """
    A = parent.angular_extent  # parent's angular extent in radians (positive)
    cx, cy = parent.center
    r_p = parent.radius

    # Compute r_S_new from the closure constraint, parameterized by the
    # parent's angular extent A.
    r_S_new = saddle_radius_for_lobe(r_p, r_L_new, A)
    if r_S_new < 0:
        raise ValueError(
            f"r_L_new={r_L_new:.4f} too small (r_p={r_p:.4f}); "
            f"r_S_new would be {r_S_new:.4f} (negative)."
        )

    # Parent arc parameterization (already in angle_start..angle_end)
    a_start = parent.angle_start
    a_end = parent.angle_end
    sweep = a_end - a_start  # signed; for sign +1 lobe, sweep > 0

    # Bisection: parent midpoint M is at angle a_mid = a_start + sweep/2
    a_mid = a_start + sweep / 2.0

    # Central half is from a_mid - sweep/4 to a_mid + sweep/4 (signed sweep)
    a_left_inner_end = a_mid - sweep / 4.0   # end of left remnant, start of removed
    a_right_inner_start = a_mid + sweep / 4.0  # end of removed, start of right remnant

    # Removed-region endpoints (these become the insertion points for the primitive)
    P_left = (cx + r_p * cos(a_left_inner_end), cy + r_p * sin(a_left_inner_end))
    P_right = (cx + r_p * cos(a_right_inner_start), cy + r_p * sin(a_right_inner_start))

    # Outward normals at these points (for a convex parent, exterior side is
    # AWAY from C_parent)
    n_ext_left = (
        (P_left[0] - cx) / r_p,
        (P_left[1] - cy) / r_p,
    )
    n_ext_right = (
        (P_right[0] - cx) / r_p,
        (P_right[1] - cy) / r_p,
    )

    # Level-(n+1) saddle centers, on the exterior side at distance r_S_new
    C_S_a = (P_left[0] + r_S_new * n_ext_left[0], P_left[1] + r_S_new * n_ext_left[1])
    C_S_b = (P_right[0] + r_S_new * n_ext_right[0], P_right[1] + r_S_new * n_ext_right[1])

    # M_ss between sub-saddle centers
    M_ss = ((C_S_a[0] + C_S_b[0]) / 2, (C_S_a[1] + C_S_b[1]) / 2)

    # Sub-lobe center C_L_new on the perpendicular bisector of C_S_a-C_S_b,
    # on the INTERIOR side (toward C_parent) at distance d_perp where
    # d_perp² + h² = (r_L_new + r_S_new)², h = |M_ss - C_S_a|.
    h = sqrt((C_S_b[0] - C_S_a[0]) ** 2 + (C_S_b[1] - C_S_a[1]) ** 2) / 2.0
    tangent_sum = r_L_new + r_S_new
    if tangent_sum < h:
        raise ValueError(
            f"Construction fails: tangent_sum={tangent_sum:.4f} < h={h:.4f}; "
            f"r_L_new={r_L_new:.4f}, r_S_new={r_S_new:.4f}, r_p={r_p:.4f}."
        )
    d_perp = sqrt(tangent_sum ** 2 - h ** 2)

    vec_to_Cp = (cx - M_ss[0], cy - M_ss[1])
    vec_len = sqrt(vec_to_Cp[0] ** 2 + vec_to_Cp[1] ** 2)
    if vec_len < 1e-12:
        unit_to_Cp = (1.0, 0.0)
    else:
        unit_to_Cp = (vec_to_Cp[0] / vec_len, vec_to_Cp[1] / vec_len)

    C_L_new = (M_ss[0] + d_perp * unit_to_Cp[0], M_ss[1] + d_perp * unit_to_Cp[1])

    # Build the 6 output arcs
    parent_left_half = Arc(
        center=parent.center,
        radius=parent.radius,
        angle_start=a_start,
        angle_end=a_left_inner_end,
        sign=+1,
        label=f"L_remnant_from_L{parent.level_created}",
        level_created=parent.level_created,
        is_sub_lobe=False,  # remnants are NOT bisected at future levels
    )
    parent_right_half = Arc(
        center=parent.center,
        radius=parent.radius,
        angle_start=a_right_inner_start,
        angle_end=a_end,
        sign=+1,
        label=f"L_remnant_from_L{parent.level_created}",
        level_created=parent.level_created,
        is_sub_lobe=False,
    )

    # Sub-saddle 1: P_left -> J1, 30° CW (or A/8 in general)
    def angle_of(P, C):
        return atan2(P[1] - C[1], P[0] - C[0])

    # J1 lies on the segment from C_S_a to C_L_new at distance r_S_new from C_S_a
    def junction(C1, C2, r1):
        dx = C2[0] - C1[0]
        dy = C2[1] - C1[1]
        d = sqrt(dx ** 2 + dy ** 2)
        return (C1[0] + r1 * dx / d, C1[1] + r1 * dy / d)

    J1 = junction(C_S_a, C_L_new, r_S_new)
    J2 = junction(C_S_b, C_L_new, r_S_new)

    # Sub-arc extents: each sub-lobe is A/2 on its kissing circle, each
    # sub-saddle is A/4. Primitive net rotation = 2(A/2) - 2(A/4) = A/2,
    # matching the parent's removed central extent (A/2).
    saddle_extent = A / 4.0
    lobe_extent = A / 2.0

    # Sub-saddle 1: from P_left at angle on C_S_a, CW sweep -saddle_extent, ending at J1
    a_S1_start = angle_of(P_left, C_S_a)
    a_S1_end = a_S1_start - saddle_extent  # CW means decreasing angle
    sub_saddle_1 = Arc(
        center=C_S_a,
        radius=r_S_new,
        angle_start=a_S1_start,
        angle_end=a_S1_end,
        sign=-1,
        label=f"S_sub_L{level_label}",
        level_created=level_label,
    )

    # Sub-saddle 2: from J2 (start) to P_right, CW sweep -saddle_extent
    a_S2_end = angle_of(P_right, C_S_b)
    a_S2_start = a_S2_end + saddle_extent  # CW from start to end means start > end
    sub_saddle_2 = Arc(
        center=C_S_b,
        radius=r_S_new,
        angle_start=a_S2_start,
        angle_end=a_S2_end,
        sign=-1,
        label=f"S_sub_L{level_label}",
        level_created=level_label,
    )

    # Sub-lobes: 2 × L of extent lobe_extent each, going CCW on C_L_new circle from J1 to J2
    # via the outward midpoint.
    a_L_J1 = angle_of(J1, C_L_new)
    a_L_J2 = angle_of(J2, C_L_new)
    # The CCW sweep we want is 2 × lobe_extent = A/2 total.
    total_sublobe_sweep = 2 * lobe_extent
    # CCW from J1: we want to sweep total_sublobe_sweep ending at J2.
    # The actual angle from J1 to J2 going CCW is (a_L_J2 - a_L_J1) mod 2π.
    # If that mod-2π value equals total_sublobe_sweep, we're good. Otherwise we
    # might need to wrap.
    delta_ccw = (a_L_J2 - a_L_J1) % (2 * pi)
    # If delta_ccw is much smaller than total_sublobe_sweep, we're going the wrong
    # way; use the long route.
    if abs(delta_ccw - total_sublobe_sweep) > pi:
        # Long way around
        actual_sweep = delta_ccw - 2 * pi if delta_ccw > pi else delta_ccw + 2 * pi
    else:
        actual_sweep = delta_ccw
    # By symmetric construction, actual_sweep should equal total_sublobe_sweep.
    # In case of slight numerical drift, use the geometric sweep.
    a_L_mid = a_L_J1 + actual_sweep / 2.0

    sub_lobe_a = Arc(
        center=C_L_new,
        radius=r_L_new,
        angle_start=a_L_J1,
        angle_end=a_L_mid,
        sign=+1,
        label=f"L_sub_L{level_label}",
        level_created=level_label,
        is_sub_lobe=True,  # bisectable at next level
    )
    sub_lobe_b = Arc(
        center=C_L_new,
        radius=r_L_new,
        angle_start=a_L_mid,
        angle_end=a_L_J1 + actual_sweep,
        sign=+1,
        label=f"L_sub_L{level_label}",
        level_created=level_label,
        is_sub_lobe=True,
    )

    return [parent_left_half, sub_saddle_1, sub_lobe_a, sub_lobe_b, sub_saddle_2, parent_right_half]


# -----------------------------------------------------------------------------
# Recursive build
# -----------------------------------------------------------------------------


def build_fractal_clover(
    r_L1: float, r_S1: float, lobe_shrinks: List[float]
) -> Tuple[List[List[Arc]], List[float]]:
    """Build levels 1 .. len(lobe_shrinks) + 1.

    lobe_shrinks[k] = r_L_(k+2) / r_L_(k+1) (level k+2 lobe radius shrinkage).

    Returns (levels, saddle_radii) where saddle_radii[k] is r_S for level k+2
    (computed from the closure constraint).
    """
    level1 = build_level1_clover(r_L1, r_S1)
    levels = [level1]
    saddle_radii: List[float] = []
    r_L_n = r_L1
    # Parent extent for level n -> n+1 bisection. Starts at 2*pi/3 (level-1
    # lobe arcs are 120°) and halves at each level.
    A_n = 2.0 * pi / 3.0
    for k, f in enumerate(lobe_shrinks, start=2):
        r_L_n_new = f * r_L_n
        # parent radius at this level is the LOBE radius of the previous level
        r_S_n_new = saddle_radius_for_lobe(r_L_n, r_L_n_new, A_n)
        saddle_radii.append(r_S_n_new)
        new_arcs: List[Arc] = []
        n_fail = 0
        for arc in levels[-1]:
            # Only bisect the previous level's NEW sub-lobes (not remnants of
            # earlier levels, which have different parent radii and would
            # produce non-canonical sub-arc extents).
            if arc.is_sub_lobe and arc.level_created == k - 1:
                try:
                    new_arcs.extend(
                        insert_primitive_at_lobe_center(arc, r_L_n_new, k)
                    )
                except ValueError:
                    new_arcs.append(arc)
                    n_fail += 1
            else:
                new_arcs.append(arc)
        if n_fail:
            print(f"Level {k}: {n_fail} lobe insertions failed; parents kept.")
        levels.append(new_arcs)
        r_L_n = r_L_n_new
        A_n = A_n / 2.0  # next level's parent extent (sub-lobes are A/2 of parent)
    return levels, saddle_radii


# -----------------------------------------------------------------------------
# Reporting
# -----------------------------------------------------------------------------


def total_kappa(arcs: List[Arc]) -> float:
    return sum(a.signed_extent for a in arcs)


def count_features(arcs: List[Arc]) -> Tuple[int, int]:
    nl = sum(1 for a in arcs if a.sign == +1)
    ns = sum(1 for a in arcs if a.sign == -1)
    return nl, ns


def extent_summary(arcs: List[Arc]) -> str:
    le = sorted({round(a.angular_extent * 180 / pi, 1) for a in arcs if a.sign == +1})
    se = sorted({round(a.angular_extent * 180 / pi, 1) for a in arcs if a.sign == -1})
    return f"L extents (deg): {le}; S extents (deg): {se}"


# -----------------------------------------------------------------------------
# Rendering
# -----------------------------------------------------------------------------


def render_curve(ax, arcs: List[Arc], samples_per_arc: int = 80) -> None:
    xs, ys = [], []
    for a in arcs:
        x, y = a.sample(samples_per_arc)
        xs.append(x); ys.append(y)
    X = np.concatenate(xs); Y = np.concatenate(ys)
    ax.fill(X, Y, alpha=0.08, color="steelblue")
    for a in arcs:
        x, y = a.sample(samples_per_arc)
        color = "crimson" if a.sign == +1 else "forestgreen"
        ax.plot(x, y, color=color, linewidth=1.1, alpha=0.95)


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-level", type=int, default=3)
    parser.add_argument("--r-lobe-1", type=float, default=1.0)
    parser.add_argument("--r-saddle-1", type=float, default=0.5)
    parser.add_argument(
        "--lobe-shrink-list",
        type=str,
        default=None,
        help="Comma-separated lobe shrinkage factors r_L_(n)/r_L_(n-1) for n>=2. "
        "Default 0.5,0.5. Each must be in (1/(2√3−1)≈0.41, 1/√3≈0.577) for a "
        "valid construction.",
    )
    parser.add_argument("--n-samples", type=int, default=100)
    parser.add_argument("--show", action="store_true")
    parser.add_argument("--outputs-dir", type=Path,
                        default=Path(__file__).resolve().parents[1] / "outputs")
    args = parser.parse_args()

    n_sub = args.max_level - 1
    if args.lobe_shrink_list is not None:
        shrinks = [float(x) for x in args.lobe_shrink_list.split(",")]
    else:
        shrinks = [0.5] * n_sub
    if len(shrinks) < n_sub:
        parser.error(f"lobe-shrink-list must have at least {n_sub} entries.")
    shrinks = shrinks[:n_sub]

    A_print = 2.0 * pi / 3.0
    for i, f in enumerate(shrinks):
        lo, hi = valid_lobe_shrink_range(A_print, 1.0)
        if not (lo < f < hi):
            print(
                f"WARNING: lobe-shrink-list[{i}]={f:.4f} outside valid range "
                f"({lo:.4f}, {hi:.4f}) for parent extent {A_print * 180/pi:.1f}°."
            )
        A_print = A_print / 2.0

    levels, sub_saddles = build_fractal_clover(
        args.r_lobe_1, args.r_saddle_1, shrinks
    )

    print(f"\nLevels: {len(levels)}")
    print(f"  Level 1: r_L = {args.r_lobe_1:.4f}, r_S = {args.r_saddle_1:.4f}")
    r_L_n = args.r_lobe_1
    for k, (f, r_S_new) in enumerate(zip(shrinks, sub_saddles), start=2):
        r_L_n = f * r_L_n
        print(
            f"  Level {k}: r_L = {r_L_n:.4f} (shrink {f:.4f}), "
            f"r_S = {r_S_new:.4f} (computed)"
        )

    print()
    for k, arcs in enumerate(levels, start=1):
        nl, ns = count_features(arcs)
        tk = total_kappa(arcs)
        print(
            f"  Level {k}: {len(arcs)} arcs ({nl}L + {ns}S), "
            f"∫κds = {tk:.4f} (target {2*pi:.4f})"
        )
        print(f"    {extent_summary(arcs)}")

    n_panels = args.max_level
    fig, axes = plt.subplots(1, n_panels, figsize=(5.5 * n_panels, 5.8))
    if n_panels == 1:
        axes = [axes]
    extent = 1.15 * (args.r_lobe_1 + args.r_saddle_1 + args.r_lobe_1)
    for i, level_idx in enumerate(range(1, args.max_level + 1)):
        ax = axes[i]
        arcs = levels[level_idx - 1]
        render_curve(ax, arcs, samples_per_arc=args.n_samples)
        ax.set_xlim(-extent, extent)
        ax.set_ylim(-extent, extent)
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.3)
        ax.axhline(0, color="gray", linewidth=0.4, alpha=0.4)
        ax.axvline(0, color="gray", linewidth=0.4, alpha=0.4)
        ax.set_xlabel("x")
        if i == 0:
            ax.set_ylabel("y")
        nl, ns = count_features(arcs)
        if level_idx == 1:
            param_str = f"r_L = {args.r_lobe_1:.2f}, r_S = {args.r_saddle_1:.2f}"
        else:
            param_str_parts = []
            r_L_track = args.r_lobe_1
            for k, (f, rS) in enumerate(zip(shrinks[:level_idx-1], sub_saddles[:level_idx-1]), start=2):
                r_L_track = f * r_L_track
                param_str_parts.append(f"r_L{k}={r_L_track:.3f}, r_S{k}={rS:.3f}")
            param_str = "\n".join(param_str_parts)
        ax.set_title(
            f"Level {level_idx}\n{nl}L + {ns}S ({len(arcs)} arcs)\n{param_str}",
            fontsize=9,
        )
    fig.suptitle(
        "Bisect-and-insert primitive fractal clover (closure-preserving)",
        fontsize=11,
    )
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    args.outputs_dir.mkdir(parents=True, exist_ok=True)
    out_path = args.outputs_dir / f"clover_on_clover_L{args.max_level}_panel.png"
    fig.savefig(out_path, dpi=130, bbox_inches="tight")
    print(f"\nSaved: {out_path}")
    if args.show:
        plt.show()


if __name__ == "__main__":
    main()
