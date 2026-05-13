"""
Render the clover cross-section profile as a 2D figure.

Usage:
    python scripts/clover_profile.py [--r-lobe R_LOBE] [--r-saddle R_SADDLE]
                                     [--chi-list CHI1,CHI2,...]
                                     [--n-samples N] [--show]

Outputs:
    outputs/profile_chi<chi>.png                       (single profile)
    outputs/profile_panel_chi<chi1>_<chi2>_..._.png    (panel mode)

Single-profile mode (default): render one profile at the specified r_lobe,
r_saddle.

Panel mode (--chi-list): render N profiles side-by-side with r_lobe = 1.0
and r_saddle = chi for each chi in the list. r_lobe and r_saddle args are
ignored in this mode.

Verifies (per work/clover-quarks.md):
    - Geometric closure (Gauss-Bonnet total turning = 2*pi)
    - Per-arc charges: Q_lobe = +2/3, Q_saddle = -1/3
"""

from __future__ import annotations

import argparse
import sys
from math import pi
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.geometry import (
    ProfileParams,
    profile,
    gauss_bonnet_check,
    charge_per_arc,
)


def _draw_profile(ax, params: ProfileParams, n_samples: int) -> None:
    """Draw one clover profile onto the given Axes."""
    phi = np.linspace(0, 2 * pi, n_samples, endpoint=False)
    x, y = profile(phi, params)
    ax.plot(x, y, "b-", linewidth=2.0, label="profile")
    ax.fill(x, y, alpha=0.1, color="blue")

    for k in range(3):
        ang = k * 2 * pi / 3
        ax.plot(params.d * np.cos(ang), params.d * np.sin(ang), "ro", markersize=6)
        ang_s = ang + pi / 3
        ax.plot(params.d * np.cos(ang_s), params.d * np.sin(ang_s), "gs", markersize=6)

    extent = 1.3 * (params.d + params.r_lobe)
    ax.set_xlim(-extent, extent)
    ax.set_ylim(-extent, extent)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color="gray", linewidth=0.5, alpha=0.5)
    ax.axvline(0, color="gray", linewidth=0.5, alpha=0.5)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--r-lobe", type=float, default=1.0, help="Lobe-circle radius (default: 1.0)"
    )
    parser.add_argument(
        "--r-saddle",
        type=float,
        default=1.0,
        help="Saddle-circle radius (default: 1.0)",
    )
    parser.add_argument(
        "--chi-list",
        type=str,
        default=None,
        help="Comma-separated list of chi values (e.g. '0.5,1.0,2.0'). "
        "When provided, render a panel of profiles with r_lobe=1.0 and "
        "r_saddle=chi for each value, instead of a single profile.",
    )
    parser.add_argument(
        "--n-samples",
        type=int,
        default=2000,
        help="Number of profile samples (default: 2000)",
    )
    parser.add_argument(
        "--show", action="store_true", help="Display the figure interactively"
    )
    parser.add_argument(
        "--outputs-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "outputs",
        help="Output directory",
    )
    args = parser.parse_args()

    Q_lobe, Q_saddle = charge_per_arc()

    if args.chi_list is not None:
        chi_values = [float(c) for c in args.chi_list.split(",")]
        all_params = [ProfileParams(r_lobe=1.0, r_saddle=chi) for chi in chi_values]

        print(f"Clover profile panel: chi = {chi_values}")
        for p in all_params:
            print(
                f"  chi={p.chi:.2f}: L_total={p.L_total:.4f}, "
                f"Gauss-Bonnet={gauss_bonnet_check(p):.6f}"
            )
        print(f"  Per-arc charges: Q_lobe = {Q_lobe:+.4f}, Q_saddle = {Q_saddle:+.4f}")

        n = len(all_params)
        fig, axes = plt.subplots(1, n, figsize=(5 * n, 5.5))
        if n == 1:
            axes = [axes]
        for ax, p in zip(axes, all_params):
            _draw_profile(ax, p, args.n_samples)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_title(
                f"chi = {p.chi:.2f}\n"
                f"r_lobe={p.r_lobe:.2f}, r_saddle={p.r_saddle:.2f}\n"
                f"L/(2*pi) = {p.L_total / (2*pi):.3f}"
            )
        axes[-1].plot([], [], "ro", label="lobe center")
        axes[-1].plot([], [], "gs", label="saddle center")
        axes[-1].legend(loc="upper right", fontsize=9)
        fig.suptitle(
            "Clover profiles: 3 lobes (240 deg) + 3 saddles (120 deg); "
            f"Q_lobe={Q_lobe:+.4f}, Q_saddle={Q_saddle:+.4f}"
        )

        args.outputs_dir.mkdir(parents=True, exist_ok=True)
        chi_str = "_".join(f"{c:.2f}" for c in chi_values)
        out_path = args.outputs_dir / f"profile_panel_chi{chi_str}.png"
        fig.savefig(out_path, dpi=120, bbox_inches="tight")
        print(f"\nSaved: {out_path}")

        if args.show:
            plt.show()
        return

    # Single-profile mode
    params = ProfileParams(r_lobe=args.r_lobe, r_saddle=args.r_saddle)

    print("Clover profile parameters")
    print(f"  r_lobe   = {params.r_lobe}")
    print(f"  r_saddle = {params.r_saddle}")
    print(f"  chi      = r_saddle / r_lobe = {params.chi:.4f}")
    print(f"  d        = r_lobe + r_saddle = {params.d:.4f}")
    print(f"  L_total  = 2*pi*(2*r_lobe + r_saddle) = {params.L_total:.4f}")
    print()
    print(
        f"  Gauss-Bonnet total turning: {gauss_bonnet_check(params):.6f} "
        f"(expected: {2*pi:.6f})"
    )
    print(
        f"  Per-arc charges: Q_lobe = {Q_lobe:.6f} ({Q_lobe*3:.3f}/3), "
        f"Q_saddle = {Q_saddle:.6f} ({Q_saddle*3:.3f}/3)"
    )

    fig, ax = plt.subplots(1, 1, figsize=(7, 7))
    _draw_profile(ax, params, args.n_samples)
    ax.plot([], [], "ro", label="lobe center")
    ax.plot([], [], "gs", label="saddle center")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(
        f"Clover profile: r_lobe={params.r_lobe}, r_saddle={params.r_saddle}, "
        f"chi={params.chi:.2f}\n"
        f"L_total/(2*pi) = {params.L_total / (2*pi):.4f}, "
        f"3 lobes (240 deg) + 3 saddles (120 deg)"
    )
    ax.legend(loc="upper right")

    args.outputs_dir.mkdir(parents=True, exist_ok=True)
    out_path = args.outputs_dir / f"profile_chi{params.chi:.2f}.png"
    fig.savefig(out_path, dpi=120, bbox_inches="tight")
    print(f"\nSaved: {out_path}")

    if args.show:
        plt.show()


if __name__ == "__main__":
    main()
