"""Wave modes plotted in the (u, t) plane at fixed S = 0.

Companion to wave-modes.py (which shows the same modes in the
(u, S) plane at fixed t = 0). The two views together show that
each mode has structure in BOTH spatial and temporal cross-sections,
not necessarily the same structure in each.

Key observation: a mode "at rest" in S (k_S = 0) has *no* (u, S)
structure beyond uniform u-winding, but it DOES have (u, t)
structure — its phase rotates uniformly in time around u even
though it sits still in space.

Modes (same as wave-modes.py for direct comparison):
    Left:   n = 0, k_S ≠ 0   — light: phase varies in t (and S), uniform in u
    Middle: n = 1, k_S = 0   — mass at rest: phase varies in BOTH u and t
    Right:  n = 1, k_S ≠ 0   — mass moving: phase varies in u and t (and S)

Run:
    .venv/bin/python projects/metric-mass/figures/u-vs-t.py

Output:
    projects/metric-mass/figures/u-vs-t.png
"""

import os

import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "u-vs-t.png")

ALPHA = 1.0
L_U = 1.0
R_U = L_U / (2 * np.pi)
C = 1.0
S_FIXED = 0.0  # cross-section at S = 0

T_MIN, T_MAX = 0.0, 4.0 * L_U / C  # time range
N_T, N_U = 400, 200

modes = [
    dict(
        n=0, k_S=2 * np.pi,
        title=r"$n = 0$, $k_S = 2\pi/L_u$",
        subtitle="light: phase varies in t, uniform in u",
    ),
    dict(
        n=1, k_S=0.0,
        title=r"$n = 1$, $k_S = 0$",
        subtitle="mass at rest: phase varies in BOTH u and t",
    ),
    dict(
        n=1, k_S=2 * np.pi,
        title=r"$n = 1$, $k_S = 2\pi/L_u$",
        subtitle="mass moving: phase varies in u and t",
    ),
]

t_grid = np.linspace(T_MIN, T_MAX, N_T)
u_grid = np.linspace(0.0, L_U, N_U)
TT, UU = np.meshgrid(t_grid, u_grid)

fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.5), constrained_layout=True)
fig.suptitle(
    r"Wave function $\mathrm{Re}\,\varphi(t, S = 0, u)$ — $(u, t)$ cross-section at $S = 0$",
    fontsize=12,
)

vmin, vmax = -1.0, 1.0
extent = (T_MIN, T_MAX, 0.0, L_U)

for ax, m in zip(axes, modes):
    n, k_S = m["n"], m["k_S"]
    omega = C * np.sqrt(k_S ** 2 + (n / R_U) ** 2)
    phase = k_S * S_FIXED - omega * TT + (n / R_U) * UU
    ReP = np.cos(phase)

    im = ax.imshow(
        ReP, origin="lower", aspect="auto", extent=extent,
        cmap="RdBu_r", vmin=vmin, vmax=vmax,
    )
    ax.set_title(m["title"] + "\n" + m["subtitle"], fontsize=10)
    ax.set_xlabel("t (time)")
    ax.set_ylabel("u (compact direction)")
    ax.axhline(0.0, color="k", linewidth=0.5, linestyle="--")
    ax.axhline(L_U, color="k", linewidth=0.5, linestyle="--")
    ax.text(
        T_MAX - 0.05, L_U - 0.04, r"$u = L_u$ (wraps to 0)",
        ha="right", va="top", fontsize=8,
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.7),
    )

cbar = fig.colorbar(im, ax=axes, location="right", shrink=0.8, pad=0.02)
cbar.set_label(r"$\mathrm{Re}\,\varphi$  (amplitude)")

fig.savefig(OUT, dpi=140)
print(f"wrote {OUT}")
