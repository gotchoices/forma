"""Dispersion-relation plot for Chapter 2 §4 of metric-mass.

Plots the (k_S, ω) curves of the dispersion relation

    ω² = c² k_S² + c² (n / R_u)²

for n = 0, 1, 2, 3 (only ω > 0 branch shown; ω < 0 mirrors below).

Conventions:
- L_u = 1, R_u = L_u / (2π)
- c = 1 (so ω is in units of 1/L_u, k_S in units of 1/L_u)
- The light-cone asymptote ω = c|k_S| is shown for reference
- Rest frequencies ω_n = c|n|/R_u marked on the ω-axis

Run:
    .venv/bin/python projects/metric-mass/figures/dispersion.py

Output:
    projects/metric-mass/figures/dispersion.png
"""

import os

import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "dispersion.png")

# Manifold
L_U = 1.0
R_U = L_U / (2 * np.pi)
C = 1.0

# k_S range
K_MAX = 4 * 2 * np.pi  # plot up to k_S = 4 · (2π/L_u)
k_S = np.linspace(-K_MAX, K_MAX, 600)

# Branches
N_VALUES = [0, 1, 2, 3]

fig, ax = plt.subplots(figsize=(7.5, 6.0), constrained_layout=True)

# Light-cone asymptote (n=0 branch, also the asymptotic form for large k_S)
asymptote = C * np.abs(k_S)
ax.plot(
    k_S, asymptote,
    color="0.7", linestyle="--", linewidth=1.0,
    label=r"$\omega = c|k_S|$  (light cone)",
)

# Branches
colors = ["#000000", "#1f77b4", "#ff7f0e", "#2ca02c"]
for n, color in zip(N_VALUES, colors):
    omega_n = np.sqrt((C * k_S) ** 2 + (C * n / R_U) ** 2)
    label = (
        rf"$n = {n}$" + (r"  (massless light)" if n == 0 else "")
    )
    ax.plot(k_S, omega_n, color=color, linewidth=2.0, label=label)

    # Mark rest frequency on the ω-axis (k_S = 0)
    if n != 0:
        omega_rest = C * n / R_U
        ax.plot([0], [omega_rest], "o", color=color, markersize=6)
        ax.annotate(
            rf"$\omega_{{rest}} = c \cdot {n}/R_u$",
            xy=(0, omega_rest), xytext=(0.6, omega_rest),
            color=color, fontsize=9, va="center",
            arrowprops=dict(
                arrowstyle="-", color=color, linewidth=0.8,
                connectionstyle="arc3,rad=0",
            ),
        )

# Cosmetics
ax.set_xlabel(r"$k_S$  (spatial wavenumber, units of $1/L_u$)")
ax.set_ylabel(r"$\omega$  (angular frequency, units of $c/L_u$)")
ax.set_title(
    "Dispersion relation $\\omega^2 = c^2 k_S^2 + c^2 (n/R_u)^2$\n"
    "One branch per integer $n$"
)
ax.set_xlim(-K_MAX, K_MAX)
ax.set_ylim(0, 1.15 * np.max(np.sqrt((C * k_S) ** 2 + (C * 3 / R_U) ** 2)))
ax.axhline(0, color="0.6", linewidth=0.5)
ax.axvline(0, color="0.6", linewidth=0.5)
ax.grid(True, alpha=0.25)
ax.legend(loc="upper right", framealpha=0.9, fontsize=9)

fig.savefig(OUT, dpi=140)
print(f"wrote {OUT}")
