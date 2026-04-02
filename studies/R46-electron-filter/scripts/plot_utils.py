"""
Shared plotting utilities for R46.

All SVG generation goes through this module so that style,
layout, and common elements (geodesic overlays, colorbars,
annotations) are consistent across tracks.
"""

import os
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

# ── Default style ────────────────────────────────────────────────

FIGSIZE_WIDE = (10, 8)
FIGSIZE_PAIR = (14, 5)
FIGSIZE_SINGLE = (10, 5)
DPI = 150
SVG_KW = dict(format='svg', dpi=DPI, bbox_inches='tight')

CMAP_DIVERGE = 'RdBu_r'
GEODESIC_COLOR = '#222222'
GEODESIC_LW = 1.2
GEODESIC_ALPHA = 0.7


def save_svg(fig, directory, filename):
    """Save figure as SVG and close it.  Returns the full path."""
    path = os.path.join(directory, filename)
    fig.savefig(path, **SVG_KW)
    plt.close(fig)
    print(f"  Saved: {path}")
    return path


# ── Geodesic computation ────────────────────────────────────────

def geodesic_on_sheet(n1, n2, n_points=2000):
    """Compute a (n1, n2) geodesic on the unrolled torus sheet.

    In lattice coordinates the geodesic is a straight line:
        θ₁ = n1 · t · 360°
        θ₂ = n2 · t · 360°

    It closes at t = 1 because n1, n2 are integers.
    Shear does not change the geodesic path in lattice coords —
    it changes the metric (physical lengths) and the field
    pattern (q_eff = n₂ − s), but the winding path is the same.

    The line wraps around [0, 360) × [0, 360).  We break it into
    segments at wrapping boundaries so matplotlib doesn't draw
    connecting lines across the sheet.

    Returns list of (θ₂_deg_segment, θ₁_deg_segment) arrays.
    """
    t = np.linspace(0, 1, n_points)
    t1 = np.mod(n1 * t * 360, 360)
    t2 = np.mod(n2 * t * 360, 360)

    segments_t2 = []
    segments_t1 = []
    seg_t2 = [t2[0]]
    seg_t1 = [t1[0]]

    for i in range(1, len(t)):
        dt2 = abs(t2[i] - t2[i-1])
        dt1 = abs(t1[i] - t1[i-1])
        if dt2 > 180 or dt1 > 180:
            segments_t2.append(np.array(seg_t2))
            segments_t1.append(np.array(seg_t1))
            seg_t2 = [t2[i]]
            seg_t1 = [t1[i]]
        else:
            seg_t2.append(t2[i])
            seg_t1.append(t1[i])

    segments_t2.append(np.array(seg_t2))
    segments_t1.append(np.array(seg_t1))

    return list(zip(segments_t2, segments_t1))


def draw_geodesic(ax, n1, n2, color=None, lw=None,
                  alpha=None, label=None, ls='-'):
    """Draw a (n1,n2) geodesic on an axis with extent [0,360]²."""
    if color is None:
        color = GEODESIC_COLOR
    if lw is None:
        lw = GEODESIC_LW
    if alpha is None:
        alpha = GEODESIC_ALPHA

    segments = geodesic_on_sheet(n1, n2)
    for i, (seg_t2, seg_t1) in enumerate(segments):
        ax.plot(seg_t2, seg_t1, color=color, lw=lw, alpha=alpha,
                ls=ls, label=label if i == 0 else None)


# ── Heatmap with geodesic panel ──────────────────────────────────

def plot_field_with_geodesic(field_2d, title, out_dir, filename,
                             n1, n2, s, r,
                             field_label=r'$E_n$ (V/m)',
                             cmap=None, extra_geodesics=None):
    """Two-panel figure: field heatmap (top) + geodesic map (bottom).

    Parameters
    ----------
    field_2d : 2D array (N1 × N2), plotted on [0,360] × [0,360]
    title : str, figure suptitle
    out_dir, filename : output path
    n1, n2 : winding numbers for the primary geodesic
    s : shear
    r : aspect ratio (a/R), used for annotations
    field_label : colorbar label
    cmap : colormap (default: RdBu_r diverging)
    extra_geodesics : list of dicts with keys 'n1','n2','s','color',
                      'label','ls' for additional geodesics to draw
    """
    if cmap is None:
        cmap = CMAP_DIVERGE

    fig, (ax_field, ax_geo) = plt.subplots(
        2, 1, figsize=FIGSIZE_WIDE, height_ratios=[1, 1],
        sharex=True)

    # ── Top panel: field heatmap ──
    vmax = np.max(np.abs(field_2d))
    if vmax == 0:
        vmax = 1.0
    norm = TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)

    im = ax_field.imshow(field_2d, origin='lower', aspect='auto',
                         extent=[0, 360, 0, 360], cmap=cmap,
                         norm=norm, interpolation='bilinear',
                         rasterized=True)
    fig.colorbar(im, ax=ax_field, label=field_label, shrink=0.9)

    ax_field.set_ylabel(r'$\theta_1$ (tube, deg)')
    ax_field.set_title(title)

    # ── Bottom panel: geodesic map ──
    ax_geo.set_xlim(0, 360)
    ax_geo.set_ylim(0, 360)
    ax_geo.set_aspect('auto')
    ax_geo.set_facecolor('#f5f5f0')

    ax_geo.set_xlabel(r'$\theta_2$ (ring, deg)')
    ax_geo.set_ylabel(r'$\theta_1$ (tube, deg)')

    draw_geodesic(ax_geo, n1, n2,
                  color='#2060c0', lw=1.8, alpha=0.85,
                  label=f'({n1},{n2}) geodesic')

    if extra_geodesics:
        for eg in extra_geodesics:
            draw_geodesic(ax_geo,
                          eg.get('n1', 1), eg.get('n2', 1),
                          color=eg.get('color', '#c04020'),
                          lw=eg.get('lw', 1.4),
                          alpha=eg.get('alpha', 0.7),
                          ls=eg.get('ls', '-'),
                          label=eg.get('label', None))

    ax_geo.legend(loc='upper right', fontsize=8,
                  framealpha=0.8, edgecolor='gray')
    ax_geo.set_title(f'Geodesics on unrolled sheet (r = {r}, s = {s:.4f})')

    fig.tight_layout()
    return save_svg(fig, out_dir, filename)


# ── Side-by-side profiles ────────────────────────────────────────

def plot_dual_profiles(theta_deg, profiles_left, profiles_right,
                       title_left, title_right, suptitle,
                       xlabel, ylabel, out_dir, filename):
    """Two side-by-side line plots (e.g. electron vs ghost)."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIGSIZE_PAIR)

    for label, data in profiles_left.items():
        ax1.plot(theta_deg, data, label=label, lw=1.5)
    ax1.axhline(0, color='gray', lw=0.5)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.set_title(title_left)
    ax1.legend()

    for label, data in profiles_right.items():
        ax2.plot(theta_deg, data, label=label, lw=1.5)
    ax2.axhline(0, color='gray', lw=0.5)
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel(ylabel)
    ax2.set_title(title_right)
    ax2.legend()

    fig.suptitle(suptitle, fontsize=12)
    fig.tight_layout()
    return save_svg(fig, out_dir, filename)


# ── Comparison plots (two panels) ────────────────────────────────

def plot_dual_lines(xs, ys_left, ys_right,
                    xlabel, ylabel_left, ylabel_right,
                    title_left, title_right,
                    out_dir, filename, **kwargs):
    """Two side-by-side line/scatter plots."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    for label, (x, y, fmt) in ys_left.items():
        ax1.plot(x, y, fmt, label=label, lw=1.5)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel_left)
    ax1.set_title(title_left)
    ax1.legend()

    for label, (x, y, fmt) in ys_right.items():
        ax2.plot(x, y, fmt, label=label, lw=1.5)
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel(ylabel_right)
    ax2.set_title(title_right)
    if kwargs.get('hline_right') is not None:
        ax2.axhline(kwargs['hline_right'], color='gray', lw=0.5, ls='--')

    fig.tight_layout()
    return save_svg(fig, out_dir, filename)
