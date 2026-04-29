"""3D cylinder rendering of wave modes for Chapter 3 §4.

Renders three panels, each showing the real part of φ on the
(t, S, u) cylinder embedding at fixed time t = 0. The cylinder
surface is colored by Re(φ).

Cylinder embedding (display coordinates):
    x_display = R_u · cos(2π u / L_u)
    y_display = R_u · sin(2π u / L_u)
    z_display = S

Modes shown:
    Left:   n = 0, k_S ≠ 0     — light: flat bands along S, no u-twist
    Middle: n = 1, k_S = 0     — mass at rest: phase wraps once around u
    Right:  n = 1, k_S ≠ 0     — mass moving: helical phase in (S, u)

Run:
    .venv/bin/python projects/metric-mass/figures/cylinder-modes.py

Output:
    projects/metric-mass/figures/cylinder-modes.png
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

OUT = os.path.join(os.path.dirname(__file__), "cylinder-modes.png")

# Choose units so the geometry renders cleanly: set L_u = 2π so
# R_u = L_u / (2π) = 1. Then u ∈ [0, 2π) and the cylinder has unit
# radius. S range is whatever shows the structure clearly.
L_U = 2 * np.pi
R_U = 1.0
C = 1.0

S_MAX = 3.0
N_S, N_U = 220, 90

S_grid = np.linspace(-S_MAX, S_MAX, N_S)
u_grid = np.linspace(0.0, L_U, N_U)
SS, UU = np.meshgrid(S_grid, u_grid, indexing="ij")

# Cylinder surface
theta = 2 * np.pi * UU / L_U
X = R_U * np.cos(theta)
Y = R_U * np.sin(theta)
Z = SS

# Three modes. For visual texture pick a k_S that gives ~3 cycles
# across the displayed S range.
K_S = 2 * np.pi  # ≈ 6.28, giving 3 cycles over S range [-3, 3]

modes = [
    dict(
        n=0, k_S=K_S,
        title=r"$n = 0$  (light)",
        subtitle="phase varies along $S$, uniform in $u$",
    ),
    dict(
        n=1, k_S=0.0,
        title=r"$n = 1$, $k_S = 0$  (mass at rest)",
        subtitle="phase winds once around $u$, uniform in $S$",
    ),
    dict(
        n=1, k_S=K_S,
        title=r"$n = 1$, $k_S \neq 0$  (mass moving)",
        subtitle="phase helical in $(S, u)$",
    ),
]

fig = plt.figure(figsize=(15, 6))
fig.suptitle(
    r"Wave modes on the $(t, S, u)$ cylinder at fixed $t = 0$  "
    r"(cylinder axis = $S$, angular = $u$)",
    fontsize=12, y=0.96,
)

vmax = 1.0
norm = plt.Normalize(vmin=-vmax, vmax=vmax)

for i, m in enumerate(modes):
    ax = fig.add_subplot(1, 3, i + 1, projection="3d")
    n, k_S = m["n"], m["k_S"]
    phase = k_S * SS + (n / R_U) * UU  # t = 0
    re_phi = np.cos(phase)
    colors = cm.RdBu_r(norm(re_phi))

    ax.plot_surface(
        X, Y, Z,
        facecolors=colors, rstride=1, cstride=1,
        shade=False, antialiased=True,
        edgecolor="none",
    )

    ax.set_title(f"{m['title']}\n{m['subtitle']}", fontsize=10, pad=10)
    ax.view_init(elev=12, azim=30)
    ax.set_box_aspect([1, 1, 3])  # tall cylinder

    # Light axis labels (the rendering itself shows geometry)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_zlabel(r"$S$", fontsize=9)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_zticks([-S_MAX, 0, S_MAX])
    ax.tick_params(axis="z", labelsize=8)

    # Subtle pane background
    for pane in (ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane):
        pane.set_facecolor((1, 1, 1, 0))
        pane.set_edgecolor((0.85, 0.85, 0.85, 1))

# Shared colorbar
sm = plt.cm.ScalarMappable(cmap=cm.RdBu_r, norm=norm)
sm.set_array([])
cbar_ax = fig.add_axes([0.92, 0.20, 0.012, 0.55])
cbar = fig.colorbar(sm, cax=cbar_ax)
cbar.set_label(r"$\mathrm{Re}\,\varphi$", fontsize=10)

plt.subplots_adjust(left=0.02, right=0.90, top=0.88, bottom=0.05, wspace=0.0)

fig.savefig(OUT, dpi=140, bbox_inches="tight")
print(f"wrote {OUT}")
