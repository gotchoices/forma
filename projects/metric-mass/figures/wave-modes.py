"""Wave-mode illustration for Chapter 2 §3 of metric-mass.

Renders the real part of three wave-equation solutions on M at a fixed
time t = 0, as 2D heatmaps over (S, u). Each panel is one mode of the
form

    φ(t, S, u) = exp(i (k_S S - ω t + n u / R_u))

for a different (n, k_S) pair. The u-axis is shown as the unrolled
compact direction, with periodic identification at u = 0 and u = L_u.

Conventions for the figure:
- L_u = 1 (compact circumference, in arbitrary length units)
- R_u = L_u / (2π)
- c = 1 (so that ω = sqrt(k_S² + (n/R_u)²))
- t = 0 fixed; figure is a snapshot at a single moment

Run:
    .venv/bin/python projects/metric-mass/figures/wave-modes.py

Output:
    projects/metric-mass/figures/wave-modes.png
"""

import os

import matplotlib.pyplot as plt
import numpy as np

# Output target
OUT = os.path.join(os.path.dirname(__file__), "wave-modes.png")

# Manifold parameters
L_U = 1.0
R_U = L_U / (2 * np.pi)
S_MIN, S_MAX = -2.0, 2.0
N_S, N_U = 400, 200

# Three modes to display
modes = [
    dict(
        n=0, k_S=2 * np.pi,
        title=r"$n = 0$, $k_S = 2\pi/L_u$",
        subtitle="Massless: wave propagates along S, no u-structure",
    ),
    dict(
        n=1, k_S=0.0,
        title=r"$n = 1$, $k_S = 0$",
        subtitle="Pure rest mode: closed wave on u, no S-propagation",
    ),
    dict(
        n=1, k_S=2 * np.pi,
        title=r"$n = 1$, $k_S = 2\pi/L_u$",
        subtitle="Massive + moving: helical wavefront in (S, u)",
    ),
]

S_grid = np.linspace(S_MIN, S_MAX, N_S)
u_grid = np.linspace(0.0, L_U, N_U)
SS, UU = np.meshgrid(S_grid, u_grid)

fig, axes = plt.subplots(
    1, 3, figsize=(13.5, 4.5), constrained_layout=True
)
fig.suptitle(
    r"Wave function $\mathrm{Re}\,\varphi(t=0,\,S,\,u)$ "
    "for three modes of the wave equation on M",
    fontsize=12,
)

vmin, vmax = -1.0, 1.0
extent = (S_MIN, S_MAX, 0.0, L_U)

for ax, m in zip(axes, modes):
    n, k_S = m["n"], m["k_S"]
    phase = k_S * SS + (n / R_U) * UU
    ReP = np.cos(phase)

    im = ax.imshow(
        ReP, origin="lower", aspect="auto", extent=extent,
        cmap="RdBu_r", vmin=vmin, vmax=vmax,
    )
    ax.set_title(m["title"] + "\n" + m["subtitle"], fontsize=10)
    ax.set_xlabel("S (extended spatial direction)")
    ax.set_ylabel("u (compact direction)")
    # Annotate the periodic boundary
    ax.axhline(0.0, color="k", linewidth=0.5, linestyle="--")
    ax.axhline(L_U, color="k", linewidth=0.5, linestyle="--")
    ax.text(
        S_MAX - 0.05, L_U - 0.04, r"$u = L_u$ (wraps to 0)",
        ha="right", va="top", fontsize=8,
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.7),
    )

cbar = fig.colorbar(im, ax=axes, location="right", shrink=0.8, pad=0.02)
cbar.set_label(r"$\mathrm{Re}\,\varphi$  (amplitude)")

fig.savefig(OUT, dpi=140)
print(f"wrote {OUT}")
