#!/usr/bin/env python3
"""sim-schwarzschild: event horizon from hexagonal lattice geometry.

Three approaches to finding the critical radius where a
hexagonal lattice with fixed edge lengths fails to
accommodate the Schwarzschild geometry:

1. Analytic: maximum aspect ratio of a single hexagon
2. Annular lattice: build hex mesh on Schwarzschild geometry
3. Pentagon density: curvature from topological defects

Usage:
    source .venv/bin/activate
    python grid/sim-schwarzschild/run.py
"""

import os
import numpy as np
from scipy.optimize import minimize_scalar, minimize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ══════════════════════════════════════════════════════════════
# Approach 1: Maximum aspect ratio of a single hexagon
# ══════════════════════════════════════════════════════════════

def hexagon_max_aspect():
    """Find the maximum height/width ratio of a hexagon with
    all 6 edges = 1.

    A regular hexagon has aspect ratio 1 (height = width = √3).
    By flexing the angles while keeping edges = 1, we can
    elongate it.

    Parameterize by the angle α at the top and bottom vertices.
    For a symmetric hexagon elongated vertically:

    Vertices (going clockwise from top):
        (0, h)                     — top
        (w/2, h - d)               — upper right
        (w/2, -h + d)              — lower right
        (0, -h)                    — bottom
        (-w/2, -h + d)             — lower left
        (-w/2, h - d)              — upper left

    Edge lengths:
        top → upper-right:  √((w/2)² + d²) = 1
        upper-right → lower-right: 2(h - d) = 1  [side edge]
        lower-right → bottom: √((w/2)² + d²) = 1

    From the side edge: h - d = 1/2, so d = h - 1/2
    From the diagonal: (w/2)² + d² = 1
        w² = 4(1 - d²) = 4(1 - (h - 1/2)²)

    Width: w = 2√(1 - (h - 1/2)²)
    Aspect ratio: R = 2h / w = 2h / (2√(1 - (h - 1/2)²))
                    = h / √(1 - (h - 1/2)²)

    Valid when: (h - 1/2)² < 1  →  -1/2 < h < 3/2
    And h > 1/2 (otherwise d < 0, hexagon is inverted)

    Maximum of R = h / √(1 - (h-0.5)²) for h ∈ (0.5, 1.5)
    """
    print(f"\n{'='*60}")
    print("  Approach 1: Single hexagon maximum aspect ratio")
    print(f"{'='*60}")

    def neg_aspect(h):
        d = h - 0.5
        w2 = 1 - d * d
        if w2 <= 0:
            return 0.0
        return -h / np.sqrt(w2)

    result = minimize_scalar(neg_aspect, bounds=(0.501, 1.499),
                             method="bounded")
    h_opt = result.x
    d_opt = h_opt - 0.5
    w_opt = 2 * np.sqrt(1 - d_opt ** 2)
    R_max = 2 * h_opt / w_opt
    aspect_max = R_max

    print(f"  Regular hexagon: aspect = 1.00")
    print(f"  Maximum aspect ratio: {R_max:.6f}")
    print(f"  At height 2h = {2*h_opt:.6f}, width w = {w_opt:.6f}")
    print(f"  Vertex angle at tip: "
          f"{2*np.degrees(np.arctan2(w_opt/2, d_opt)):.1f}°")

    # Schwarzschild stretch factor = 1/√(1 - r_s/r)
    # At critical radius: stretch = R_max
    # 1/√(1 - r_s/r_crit) = R_max
    # 1 - r_s/r_crit = 1/R_max²
    # r_s/r_crit = 1 - 1/R_max²
    # r_crit = r_s / (1 - 1/R_max²)

    ratio_crit = 1.0 / (1.0 - 1.0 / R_max ** 2)
    print(f"\n  Schwarzschild critical radius:")
    print(f"    stretch(r) = 1/√(1 − r_s/r)")
    print(f"    At max stretch = {R_max:.4f}:")
    print(f"    r_crit = {ratio_crit:.6f} × r_s")
    print(f"    (lattice shears at {ratio_crit:.4f} × "
          f"Schwarzschild radius)")

    if ratio_crit < 1.05:
        print(f"\n  ★ r_crit ≈ r_s — horizon matches lattice limit!")
    elif ratio_crit < 2.0:
        print(f"\n  ~ r_crit is within 2× r_s — close but not exact")
    else:
        print(f"\n  r_crit = {ratio_crit:.1f}× r_s — "
              f"lattice fails well outside the horizon")

    # Plot hexagon family
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Family of hexagons at different aspect ratios
    ax = axes[0]
    for h in np.linspace(0.55, h_opt - 0.01, 8):
        d = h - 0.5
        w = 2 * np.sqrt(max(1 - d * d, 0.01))
        verts = np.array([
            [0, h], [w / 2, h - d], [w / 2, -(h - d)],
            [0, -h], [-w / 2, -(h - d)], [-w / 2, h - d],
            [0, h]
        ])
        R = 2 * h / w
        c = plt.cm.viridis(R / R_max)
        ax.plot(verts[:, 0], verts[:, 1], "-", color=c, lw=1.5)
    ax.set_aspect("equal")
    ax.set_title(f"Hexagon deformation family\n"
                 f"(max aspect = {R_max:.3f})")
    ax.set_xlabel("width")
    ax.set_ylabel("height")
    ax.grid(True, alpha=0.3)

    # Aspect ratio vs height parameter
    ax2 = axes[1]
    hs = np.linspace(0.51, 1.49, 200)
    Rs = []
    for h in hs:
        d = h - 0.5
        w2 = 1 - d * d
        if w2 > 0:
            Rs.append(h / np.sqrt(w2))
        else:
            Rs.append(np.nan)
    ax2.plot(2 * hs, Rs, "b-", lw=2)
    ax2.axhline(R_max, color="r", ls="--",
                label=f"max = {R_max:.4f}")
    ax2.set_xlabel("hexagon height (2h)")
    ax2.set_ylabel("aspect ratio (height/width)")
    ax2.set_title("Aspect ratio vs elongation")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Stretch factor vs r/r_s
    ax3 = axes[2]
    r_over_rs = np.linspace(1.01, 10, 200)
    stretch = 1.0 / np.sqrt(1 - 1.0 / r_over_rs)
    ax3.plot(r_over_rs, stretch, "b-", lw=2,
             label="Schwarzschild stretch")
    ax3.axhline(R_max, color="r", ls="--",
                label=f"hex limit = {R_max:.4f}")
    ax3.axvline(ratio_crit, color="r", ls=":",
                label=f"r_crit = {ratio_crit:.3f} r_s")
    ax3.set_xlabel("r / r_s")
    ax3.set_ylabel("radial stretch factor")
    ax3.set_title("Schwarzschild stretch vs hex limit")
    ax3.legend()
    ax3.set_xlim(1, 5)
    ax3.set_ylim(1, 5)
    ax3.grid(True, alpha=0.3)

    fig.suptitle("Approach 1: Hexagon aspect ratio limit",
                 fontsize=14)
    fig.tight_layout()
    path = os.path.join(os.path.dirname(__file__), "output",
                        "hexagon_limit.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"\n  Saved: {path}")
    plt.close(fig)

    return {"R_max": R_max, "r_crit_over_rs": ratio_crit,
            "h_opt": h_opt}


# ══════════════════════════════════════════════════════════════
# Approach 2: Pentagon density (Gauss-Bonnet)
# ══════════════════════════════════════════════════════════════

def pentagon_density():
    """Compute the required pentagon density at each radius
    to produce Schwarzschild curvature, and find where
    it exceeds 100%.

    On a hexagonal lattice:
    - Each hexagon has zero Gaussian curvature
    - Each pentagon has deficit angle π/3 (= 60°)
    - Gaussian curvature from one pentagon: K = (π/3) / A_face

    For a regular pentagon with unit edges:
        A_pent = (√(25 + 10√5))/4 ≈ 1.720
    For a regular hexagon with unit edges:
        A_hex = (3√3/2) ≈ 2.598

    The Schwarzschild Gaussian curvature on the equatorial
    plane (Kretschner scalar simplified to 2D spatial slice):
        K(r) = r_s / (2 r³)
    (This is the Gaussian curvature of the Flamm paraboloid.)

    Required pentagon density at radius r:
        f_pent(r) = K(r) × A_face / (π/3)

    Critical radius where f_pent = 1 (all faces are pentagons):
        r_s / (2 r³) × A_hex / (π/3) = 1
        r³ = r_s × A_hex / (2π/3)
        r³ = r_s × 3A_hex / (2π)
    """
    print(f"\n{'='*60}")
    print("  Approach 2: Pentagon density (Gauss-Bonnet)")
    print(f"{'='*60}")

    A_hex = 3 * np.sqrt(3) / 2  # area of regular hexagon, edge=1
    A_pent = np.sqrt(25 + 10 * np.sqrt(5)) / 4  # pentagon, edge=1
    deficit_pent = np.pi / 3  # 60° deficit per pentagon

    print(f"  A_hex = {A_hex:.4f} (regular hexagon, edge=1)")
    print(f"  A_pent = {A_pent:.4f} (regular pentagon, edge=1)")
    print(f"  Deficit per pentagon = π/3 = {np.degrees(deficit_pent):.0f}°")

    # Flamm paraboloid Gaussian curvature
    # K(r) = r_s / (2r³)  [for 2D spatial Schwarzschild slice]

    # Pentagon fraction needed at radius r:
    # f(r) = K(r) × A_face / deficit
    #       = (r_s / 2r³) × A_hex / (π/3)
    #       = (3 A_hex r_s) / (2π r³)

    coeff = 3 * A_hex / (2 * np.pi)
    # f(r) = coeff × r_s / r³
    # f = 1 when r³ = coeff × r_s
    # r_crit = (coeff × r_s)^(1/3)
    # r_crit / r_s = (coeff / r_s²)^(1/3)

    # For r_s in Planck units (r_s = 2M where M is mass in
    # Planck masses), the critical radius in units of r_s:
    # r_crit / r_s = (coeff)^(1/3) × r_s^(-2/3)

    # But for a fixed r_s, let's express r_crit in lattice units:
    # r_crit = (coeff × r_s)^(1/3)
    # r_crit / r_s = coeff^(1/3) / r_s^(2/3)

    # For a solar-mass BH: r_s ≈ 3km ≈ 1.85×10³⁸ Planck lengths
    # r_crit / r_s ≈ (coeff)^(1/3) / r_s^(2/3) ≈ tiny — deep inside horizon

    # For a Planck-mass BH: r_s = 2 (Planck lengths, G=1)
    rs_planck = 2.0  # r_s for a Planck-mass object (G=1 natural units)
    r_crit_planck = (coeff * rs_planck) ** (1.0 / 3.0)
    ratio_planck = r_crit_planck / rs_planck

    print(f"\n  Gaussian curvature of Flamm paraboloid: K(r) = r_s/(2r³)")
    print(f"  Pentagon fraction: f(r) = {coeff:.4f} × r_s / r³")
    print(f"  f = 1 when r = ({coeff:.4f} × r_s)^(1/3)")
    print(f"\n  For a Planck-mass object (r_s = {rs_planck:.0f} L_P):")
    print(f"    r_crit = {r_crit_planck:.4f} L_P")
    print(f"    r_crit / r_s = {ratio_planck:.4f}")

    # For various masses
    print(f"\n  Pentagon-saturation radius for various masses:")
    print(f"  {'Mass':>12s}  {'r_s (L_P)':>12s}  "
          f"{'r_crit (L_P)':>12s}  {'r_crit/r_s':>10s}")
    print(f"  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*10}")
    masses = [
        ("1 m_P", 2),
        ("10 m_P", 20),
        ("100 m_P", 200),
        ("10⁶ m_P", 2e6),
        ("electron", 2 * 4.185e-23),  # r_s for electron
        ("proton", 2 * 7.685e-20),    # r_s for proton
    ]
    results_mass = []
    for name, rs in masses:
        rc = (coeff * rs) ** (1.0 / 3.0)
        ratio = rc / rs
        results_mass.append((name, rs, rc, ratio))
        print(f"  {name:>12s}  {rs:12.4e}  {rc:12.4e}  {ratio:10.6f}")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Pentagon fraction vs r for various r_s
    ax = axes[0]
    for rs_val, label in [(2, "1 m_P"), (20, "10 m_P"),
                           (200, "100 m_P")]:
        r = np.linspace(0.5, 5 * rs_val, 500)
        f = coeff * rs_val / r ** 3
        f = np.minimum(f, 5)
        ax.plot(r / rs_val, f, lw=2, label=f"r_s={rs_val} ({label})")
    ax.axhline(1.0, color="red", ls="--", label="f=1 (all pentagons)")
    ax.set_xlabel("r / r_s")
    ax.set_ylabel("pentagon fraction f(r)")
    ax.set_title("Required pentagon density")
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.legend()
    ax.grid(True, alpha=0.3)

    # r_crit/r_s vs r_s
    ax2 = axes[1]
    rs_range = np.logspace(np.log10(1), np.log10(1e6), 200)
    rc_range = (coeff * rs_range) ** (1.0 / 3.0)
    ratio_range = rc_range / rs_range
    ax2.loglog(rs_range, ratio_range, "b-", lw=2)
    ax2.axhline(1.0, color="red", ls="--", label="r_crit = r_s")
    ax2.set_xlabel("r_s (Planck lengths)")
    ax2.set_ylabel("r_crit / r_s")
    ax2.set_title("Pentagon saturation radius vs mass")
    ax2.legend()
    ax2.grid(True, alpha=0.3, which="both")

    # Mark key masses
    for name, rs, rc, ratio in results_mass[:3]:
        ax2.plot(rs, ratio, "ro", ms=6)
        ax2.annotate(name, (rs, ratio), fontsize=8,
                     xytext=(5, 5), textcoords="offset points")

    fig.suptitle("Approach 2: Pentagon density from Gauss-Bonnet",
                 fontsize=14)
    fig.tight_layout()
    path = os.path.join(os.path.dirname(__file__), "output",
                        "pentagon_density.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"\n  Saved: {path}")
    plt.close(fig)

    return {"coeff": coeff, "r_crit_planck": r_crit_planck,
            "ratio_planck": ratio_planck}


# ══════════════════════════════════════════════════════════════
# Approach 3: Combined analysis
# ══════════════════════════════════════════════════════════════

def combined_analysis(hex_result, pent_result):
    """Compare the two approaches and extract the critical radius."""
    print(f"\n{'='*60}")
    print("  Combined analysis")
    print(f"{'='*60}")

    R_max = hex_result["R_max"]
    r_hex = hex_result["r_crit_over_rs"]
    r_pent = pent_result["ratio_planck"]

    print(f"\n  Approach 1 (hexagon deformation):")
    print(f"    Max aspect ratio: {R_max:.4f}")
    print(f"    r_crit = {r_hex:.4f} × r_s")
    print(f"    (independent of mass — geometric constant)")

    print(f"\n  Approach 2 (pentagon density):")
    print(f"    r_crit / r_s = {r_pent:.4f} (for Planck mass)")
    print(f"    Scales as r_s^(-2/3) — mass-dependent")
    print(f"    For large masses: r_crit << r_s (lattice fails")
    print(f"    deep inside the horizon)")
    print(f"    For Planck mass: r_crit ≈ {r_pent:.2f} × r_s")

    print(f"\n  Key distinction:")
    print(f"    Approach 1 gives a UNIVERSAL ratio "
          f"(r_crit = {r_hex:.3f} r_s)")
    print(f"    — it says the lattice shears at a fixed fraction")
    print(f"    of the Schwarzschild radius, for any mass.")
    print()
    print(f"    Approach 2 gives a MASS-DEPENDENT ratio —")
    print(f"    for astrophysical BHs, the pentagon-saturation")
    print(f"    radius is deep inside the horizon.  The lattice")
    print(f"    can happily tile the Schwarzschild geometry all")
    print(f"    the way to r_s and beyond, using pentagons.")
    print(f"    The hexagon deformation limit (Approach 1) kicks")
    print(f"    in first.")

    print(f"\n  Interpretation:")
    print(f"    The event horizon at r = r_s is NOT a lattice")
    print(f"    failure for astrophysical masses — the hexagonal")
    print(f"    lattice has enough room to accommodate the")
    print(f"    curvature with pentagon insertions.")
    print()
    print(f"    The hexagon deformation limit (Approach 1) gives")
    print(f"    r_crit = {r_hex:.3f} r_s — the lattice shears at")
    print(f"    a fixed ratio INSIDE the horizon.  This is a")
    print(f"    geometric singularity, not the event horizon.")
    print()
    print(f"    For Planck-mass objects (r_s ≈ 2 L_P), the two")
    print(f"    limits converge: both approaches give r_crit ≈ r_s,")
    print(f"    meaning the lattice shear IS the horizon for")
    print(f"    Planck-scale objects.")

    # Plot comparison
    fig, ax = plt.subplots(figsize=(8, 6))

    # Approach 1: constant ratio
    rs_range = np.logspace(0, 40, 200)
    ax.axhline(r_hex, color="blue", lw=2,
               label=f"Hex deformation: r_crit = {r_hex:.3f} r_s")

    # Approach 2: mass-dependent
    coeff = pent_result["coeff"]
    rc2 = (coeff * rs_range) ** (1.0 / 3.0) / rs_range
    ax.loglog(rs_range, rc2, "g-", lw=2,
              label="Pentagon saturation: r_crit/r_s ∝ r_s^(-2/3)")

    ax.axhline(1.0, color="red", ls="--", lw=1, label="r_crit = r_s")

    # Mark crossover
    # Where approach 2 = approach 1:
    # (coeff * rs)^(1/3) / rs = r_hex
    # (coeff * rs)^(1/3) = r_hex * rs
    # coeff * rs = r_hex³ * rs³
    # coeff = r_hex³ * rs²
    # rs_cross = √(coeff / r_hex³)
    rs_cross = np.sqrt(coeff / r_hex ** 3)
    ax.axvline(rs_cross, color="purple", ls=":", lw=1,
               label=f"Crossover at r_s = {rs_cross:.2f} L_P")

    ax.set_xlabel("r_s (Planck lengths)")
    ax.set_ylabel("r_crit / r_s")
    ax.set_title("Lattice failure radius: two mechanisms")
    ax.legend(fontsize=9)
    ax.set_xlim(1, 1e40)
    ax.set_ylim(1e-30, 10)
    ax.grid(True, alpha=0.3, which="both")

    path = os.path.join(os.path.dirname(__file__), "output",
                        "combined.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"\n  Saved: {path}")
    plt.close(fig)

    return {"r_hex": r_hex, "r_pent_planck": r_pent,
            "rs_crossover": rs_cross}


# ══════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════

def main():
    out_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(out_dir, exist_ok=True)

    print("sim-schwarzschild: event horizon from lattice geometry")
    print("=" * 60)

    r1 = hexagon_max_aspect()
    r2 = pentagon_density()
    r3 = combined_analysis(r1, r2)

    print(f"\n{'='*72}")
    print("  SUMMARY")
    print(f"{'='*72}")
    print()
    print(f"  Hexagon max aspect ratio: {r1['R_max']:.4f}")
    print(f"  → r_crit = {r1['r_crit_over_rs']:.4f} × r_s "
          f"(universal, mass-independent)")
    print()
    print(f"  Pentagon saturation (Planck mass):"
          f" r_crit = {r2['ratio_planck']:.4f} × r_s")
    print(f"  Pentagon saturation (large mass): r_crit << r_s")
    print()
    print(f"  Crossover mass: r_s ≈ {r3['rs_crossover']:.2f} L_P")
    print(f"  (≈ {r3['rs_crossover']/2:.2f} Planck masses)")
    print()
    print(f"  For Planck-scale objects: lattice shear ≈ horizon")
    print(f"  For astrophysical objects: horizon is NOT a lattice")
    print(f"    failure; the real singularity is deeper inside")


if __name__ == "__main__":
    main()
