"""(u, t) cross-check of the ±n superposition for Chapter 4.

Three panels at fixed S = 0, all for the rest case (k_S = 0,
n = 1) so ω = ω_rest = c/R_u:

    Left:    Re(φ_+) — single +n mode, traveling wave around u
    Middle:  Re(φ_-) — single −n mode, opposite-direction traveling wave
    Right:   Re(φ_+ + φ_-) = 2 cos(u/R_u) · cos(ω t)
             — the superposition viewed as a standing wave

The point of the figure: the sum (right panel) IS the linear
combination of the two traveling waves (left, middle). The
two component waves are present mathematically — the
trigonometric identity cos(A) + cos(B) = 2 cos((A+B)/2) cos((A-B)/2)
makes this explicit. The standing-wave appearance of the sum is
the visible *consequence* of two distinct traveling waves
crossing, not evidence that they have annihilated each other.

Run:
    .venv/bin/python projects/metric-mass/figures/superposition-ut.py

Output:
    projects/metric-mass/figures/superposition-ut.png
"""

import os

import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "superposition-ut.png")

L_U = 2 * np.pi
R_U = 1.0
C = 1.0
N = 1
K_S = 0.0
S_FIXED = 0.0

OMEGA = C * np.sqrt(K_S ** 2 + (N / R_U) ** 2)  # = c/R_u

T_MIN, T_MAX = 0.0, 4 * np.pi / OMEGA  # two full periods
N_T, N_U = 400, 200

t_grid = np.linspace(T_MIN, T_MAX, N_T)
u_grid = np.linspace(0.0, L_U, N_U)
TT, UU = np.meshgrid(t_grid, u_grid)

phi_plus = np.cos(K_S * S_FIXED + (N / R_U) * UU - OMEGA * TT)
phi_minus = np.cos(K_S * S_FIXED - (N / R_U) * UU - OMEGA * TT)
phi_sum = phi_plus + phi_minus

vmax = 2.0
extent = (T_MIN, T_MAX, 0.0, L_U)

fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.5), constrained_layout=True)

panels = [
    ("Re(φ₊): single +n mode", phi_plus, 1.0,
     "diagonal stripes (slope du/dt = +c)"),
    ("Re(φ₋): single −n mode", phi_minus, 1.0,
     "diagonal stripes (slope du/dt = −c)"),
    ("Re(φ₊ + φ₋): superposition", phi_sum, vmax,
     "standing wave: 2 cos(u/R_u)·cos(ω t)"),
]

for ax, (title, data, vlim, subtitle) in zip(axes, panels):
    im = ax.imshow(
        data, origin="lower", aspect="auto", extent=extent,
        cmap="RdBu_r", vmin=-vlim, vmax=vlim,
    )
    ax.set_title(title + "\n" + subtitle, fontsize=10)
    ax.set_xlabel("t (time)")
    ax.set_ylabel("u (compact direction)")
    ax.axhline(0.0, color="k", linewidth=0.5, linestyle="--")
    ax.axhline(L_U, color="k", linewidth=0.5, linestyle="--")

cbar = fig.colorbar(im, ax=axes, location="right", shrink=0.8, pad=0.02)
cbar.set_label(r"amplitude")

fig.suptitle(
    r"Cross-check: $\pm n$ superposition viewed in $(u, t)$ at $S = 0$",
    fontsize=12,
)

fig.savefig(OUT, dpi=140)
print(f"wrote {OUT}")
