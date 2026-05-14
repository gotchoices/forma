"""
Render the corrugated torus surface in 3D.

Usage:
    python scripts/corrugated_torus.py [--r-lobe R_LOBE] [--r-saddle R_SADDLE]
                                       [--R-major R_MAJOR] [--tau TAU]
                                       [--sigma SIGMA]
                                       [--n-theta N] [--n-phi N]
                                       [--show] [--view ELEV AZIM]

Outputs:
    outputs/torus_chi<chi>_R<R_major>_<embed>_<color>[_sigma<sigma>].png

Per work/clover-quarks.md §9, the surface (in the parameter-shift embedding) is:
    r(theta, phi) = (R_major + P_x(phi + tau*theta)) * (cos theta, sin theta, 0)
                  + P_y(phi + tau*theta) * (0, 0, 1)

with profile P(phi) defined by ProfileParams(r_lobe, r_saddle) and tau = 1/3
by default.

The optional --sigma flag is the rolled-leaf intrinsic shear of
work/clover-quarks.md §1.3, §10.3. In the actual metric, sigma is a
constant addition to g_{theta,phi} only; it does not enter the 3D embedding
in a strictly isometric way. For visualization, this script uses an
effective twist (sigma + tau) for the parameter shift / rotation rate so
that sigma's "extra shear rate" effect is visible. The metric distinction
between sigma and tau (only tau is tied to the Z_3 Bloch-sector
quantization) is not visible in 3D; it lives in the spectroscopic sector
structure. See the sigma-comparison renderings in outputs/ at
(sigma, tau) = (0, 1/3), (0.10, 1/3), (0.30, 1/3) for the visual contrast.
"""

from __future__ import annotations

import argparse
import sys
from math import pi
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (registers 3d projection)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.geometry import ProfileParams, corrugated_torus_surface, aspect_ratio


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--r-lobe", type=float, default=1.0)
    parser.add_argument("--r-saddle", type=float, default=1.0)
    parser.add_argument(
        "--R-major",
        type=float,
        default=5.0,
        help="Major-ring radius (default: 5.0)",
    )
    parser.add_argument(
        "--tau",
        type=float,
        default=1.0 / 3.0,
        help="Twist parameter (default: 1/3)",
    )
    parser.add_argument(
        "--sigma",
        type=float,
        default=0.0,
        help="Rolled-leaf intrinsic shear (default: 0.0; see "
        "work/clover-quarks.md §1.3 and §10.3). Same units as tau. "
        "Visualised as an additional twist sigma+tau in the embedding.",
    )
    parser.add_argument(
        "--embedding",
        choices=["parameter-shift", "rotation"],
        default="parameter-shift",
        help="Surface embedding choice (see clover-quarks.md §9). "
        "'parameter-shift' keeps the embedded clover static and twists the "
        "phi-labels; 'rotation' physically rotates the clover cross-section "
        "by tau*theta around the ring. Both have identical topology but "
        "different metrics.",
    )
    parser.add_argument(
        "--n-theta", type=int, default=180, help="Theta samples (default: 180)"
    )
    parser.add_argument(
        "--n-phi", type=int, default=120, help="Phi samples (default: 120)"
    )
    parser.add_argument("--show", action="store_true")
    parser.add_argument(
        "--view",
        type=float,
        nargs=2,
        metavar=("ELEV", "AZIM"),
        default=(25.0, 45.0),
        help="Viewing elevation and azimuth (default: 25 45)",
    )
    parser.add_argument(
        "--color-by",
        choices=["radial", "lobe-saddle", "lobe-id", "phi-band"],
        default="phi-band",
        help="Surface coloring: 'radial' (distance from ring axis), "
        "'lobe-saddle' (two colors at lobe/saddle), 'lobe-id' (3 colors "
        "by twisted-phi lobe -- produces horizontal bands because each "
        "lobe is at a fixed z), or 'phi-band' (3 colors by untwisted phi "
        "-- produces helical bands that visibly wrap with the 1/3 twist)",
    )
    parser.add_argument(
        "--helices",
        type=int,
        default=0,
        help="Overlay N constant-phi helical curves on the surface "
        "(each curve wraps 3 times around the ring before closing, "
        "visualizing the 1/3 twist). Try --helices 6.",
    )
    parser.add_argument(
        "--surface-alpha",
        type=float,
        default=0.95,
        help="Surface opacity (lower to see overlaid helices through it; "
        "default 0.95)",
    )
    parser.add_argument(
        "--outputs-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "outputs",
    )
    args = parser.parse_args()

    params = ProfileParams(r_lobe=args.r_lobe, r_saddle=args.r_saddle)
    eps = aspect_ratio(params, args.R_major)

    print("Corrugated torus parameters")
    print(f"  r_lobe   = {params.r_lobe}")
    print(f"  r_saddle = {params.r_saddle}")
    print(f"  chi      = {params.chi:.4f}")
    print(f"  R_major  = {args.R_major}")
    print(f"  tau      = {args.tau}")
    print(f"  sigma    = {args.sigma}")
    print(f"  L_total  = {params.L_total:.4f}")
    print(f"  epsilon  = L_total/(2*pi*R_major) = {eps:.4f}")
    print()

    # Build (theta, phi) grid
    theta = np.linspace(0, 2 * pi, args.n_theta, endpoint=True)
    phi = np.linspace(0, 2 * pi, args.n_phi, endpoint=True)
    Theta, Phi = np.meshgrid(theta, phi, indexing="ij")

    # Compute surface positions
    X, Y, Z = corrugated_torus_surface(
        Theta, Phi, params, args.R_major, args.tau,
        embedding=args.embedding, sigma=args.sigma,
    )

    # Compute the twisted phi values for coloring (uses the effective twist
    # sigma + tau, matching what corrugated_torus_surface uses internally so
    # the color bands track the visible cross-section).
    twist_eff = args.sigma + args.tau
    twisted_phi = (Phi + twist_eff * Theta) % (2.0 * pi)

    # Color the surface
    fund_period = 2.0 * pi / 3.0
    fund_phi = twisted_phi % fund_period
    L_fund = params.arc_lobe + params.arc_saddle
    s = fund_phi * L_fund / fund_period
    is_lobe = s < params.arc_lobe
    fund_index = (twisted_phi // fund_period).astype(int) % 3  # which of 3 lobes/saddles

    # phi-band coloring uses the UNTWISTED profile-coordinate, so a constant
    # color follows a helical curve (phi=const, theta varies) and the 1/3 twist
    # appears as the three bands spiraling around the ring.
    phi_only = Phi % (2.0 * pi)
    phi_band_index = (phi_only // fund_period).astype(int) % 3
    phi_band_fund = phi_only % fund_period
    phi_band_s = phi_band_fund * L_fund / fund_period
    phi_band_is_lobe = phi_band_s < params.arc_lobe

    if args.color_by == "lobe-saddle":
        # Highlight whether each (theta, phi) point lies in a lobe region
        # or a saddle region of the profile. Mods out the 3-fold symmetry,
        # so the helical structure from the twist is not visible.
        colors = np.where(is_lobe, 1.0, -1.0)
        cmap = "coolwarm"
        clabel = "lobe (red) vs saddle (blue)"
        # Build facecolors directly
        facecolors = plt.colormaps[cmap](
            (colors - colors.min()) / (colors.max() - colors.min() + 1e-12)
        )
    elif args.color_by == "phi-band":
        # Color by untwisted phi (profile arc-length coordinate). Because the
        # surface point at (theta, phi) lives at twisted_phi = phi + tau*theta,
        # a constant-phi curve wraps around the ring as theta advances and
        # closes after 3 revolutions -- making the 3 color bands spiral
        # helically around the major ring, directly visualizing the 1/3 twist.
        lobe_hues = np.array(
            [
                [0.85, 0.15, 0.15],  # red
                [0.15, 0.70, 0.15],  # green
                [0.15, 0.30, 0.85],  # blue
            ]
        )
        saddle_hues = np.array(
            [
                [0.65, 0.45, 0.45],
                [0.45, 0.60, 0.45],
                [0.45, 0.50, 0.65],
            ]
        )
        facecolors = np.zeros((*Theta.shape, 4))
        for idx in range(3):
            mask_lobe = (phi_band_index == idx) & phi_band_is_lobe
            mask_saddle = (phi_band_index == idx) & (~phi_band_is_lobe)
            facecolors[mask_lobe, :3] = lobe_hues[idx]
            facecolors[mask_lobe, 3] = 1.0
            facecolors[mask_saddle, :3] = saddle_hues[idx]
            facecolors[mask_saddle, 3] = 1.0
        clabel = "helical phi-bands (1/3 twist visible)"
    elif args.color_by == "lobe-id":
        # Color each of the 3 lobes with a distinct hue; same for the 3 saddles
        # but at lower brightness. This makes the helical 1/3-twist structure
        # visible as 3 colored bands spiraling around the ring.
        # Hues: lobe-0 red, lobe-1 green, lobe-2 blue.
        # Saddles get the SAME hue as the preceding lobe but desaturated/darker.
        lobe_hues = np.array(
            [
                [0.85, 0.15, 0.15],  # red
                [0.15, 0.70, 0.15],  # green
                [0.15, 0.30, 0.85],  # blue
            ]
        )
        saddle_hues = np.array(
            [
                [0.65, 0.45, 0.45],  # muted red
                [0.45, 0.60, 0.45],  # muted green
                [0.45, 0.50, 0.65],  # muted blue
            ]
        )
        facecolors = np.zeros((*Theta.shape, 4))
        for idx in range(3):
            mask_lobe = (fund_index == idx) & is_lobe
            mask_saddle = (fund_index == idx) & (~is_lobe)
            facecolors[mask_lobe, :3] = lobe_hues[idx]
            facecolors[mask_lobe, 3] = 1.0
            facecolors[mask_saddle, :3] = saddle_hues[idx]
            facecolors[mask_saddle, 3] = 1.0
        clabel = "lobes red/green/blue; saddles muted"
    else:
        # Color by distance from ring axis (R + P_x)
        colors = np.sqrt(X**2 + Y**2)
        cmap = "viridis"
        clabel = "distance from ring axis"
        facecolors = plt.colormaps[cmap](
            (colors - colors.min()) / (colors.max() - colors.min() + 1e-12)
        )

    # Create figure
    fig = plt.figure(figsize=(11, 9))
    ax = fig.add_subplot(111, projection="3d")

    surf = ax.plot_surface(
        X,
        Y,
        Z,
        facecolors=facecolors,
        rstride=1,
        cstride=1,
        linewidth=0,
        antialiased=True,
        shade=True,
        alpha=args.surface_alpha,
    )

    # Overlay constant-phi helical curves to make the 1/3 twist visible.
    # At fixed phi, varying theta over [0, 6*pi] (3 ring revolutions) the curve
    # closes because twisted_phi = phi + tau*theta advances by 6*pi*tau = 2*pi
    # per ring revolution * 3 = full profile cycle. The curve is a helix wrapping
    # 3 times around the ring.
    if args.helices > 0:
        helix_theta = np.linspace(0, 6.0 * pi, 3 * args.n_theta, endpoint=True)
        helix_phi_starts = np.linspace(0, 2.0 * pi, args.helices, endpoint=False)
        helix_cmap = plt.colormaps["hsv"]
        for i, phi0 in enumerate(helix_phi_starts):
            phi_const = np.full_like(helix_theta, phi0)
            Hx, Hy, Hz = corrugated_torus_surface(
                helix_theta,
                phi_const,
                params,
                args.R_major,
                args.tau,
                embedding=args.embedding,
                sigma=args.sigma,
            )
            color = helix_cmap(i / args.helices)
            ax.plot(Hx, Hy, Hz, color=color, linewidth=1.8, alpha=0.95)

    # Set viewing angle
    ax.view_init(elev=args.view[0], azim=args.view[1])

    # Aesthetics
    extent_xy = args.R_major + params.d + params.r_lobe + 0.5
    extent_z = params.d + params.r_lobe + 0.5
    ax.set_xlim(-extent_xy, extent_xy)
    ax.set_ylim(-extent_xy, extent_xy)
    ax.set_zlim(-extent_z, extent_z)
    try:
        ax.set_box_aspect((1, 1, extent_z / extent_xy))
    except AttributeError:
        pass  # older matplotlib

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    sigma_title = f", sigma={args.sigma:.4f}" if args.sigma != 0.0 else ""
    ax.set_title(
        f"Corrugated torus ({args.embedding}): chi={params.chi:.2f}, "
        f"R_major={args.R_major}, tau={args.tau:.4f}{sigma_title}\n"
        f"epsilon = L_total/(2*pi*R_major) = {eps:.4f}; coloring: {clabel}"
    )

    args.outputs_dir.mkdir(parents=True, exist_ok=True)
    helix_suffix = f"_helices{args.helices}" if args.helices > 0 else ""
    sigma_suffix = f"_sigma{args.sigma:.2f}" if args.sigma != 0.0 else ""
    embed_tag = "pshift" if args.embedding == "parameter-shift" else "rot"
    out_path = (
        args.outputs_dir
        / f"torus_chi{params.chi:.2f}_R{args.R_major:.1f}"
        f"_{embed_tag}_{args.color_by}{sigma_suffix}{helix_suffix}.png"
    )
    fig.savefig(out_path, dpi=120, bbox_inches="tight")
    print(f"Saved: {out_path}")

    if args.show:
        plt.show()


if __name__ == "__main__":
    main()
