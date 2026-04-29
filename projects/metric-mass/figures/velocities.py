"""Phase- and group-velocity illustration for Chapter 2 §4.

Shows two (S, t) plots side-by-side:

  Left:   n = 0 mode (massless light) — phase and group velocities
          coincide; constant-phase stripes and the wave-packet envelope
          have the same slope.

  Right:  n = 1 mode (a "massive" branch) — phase velocity > c (steep
          stripes) while group velocity < c (less-steep envelope). The
          two slopes are different.

Both panels render Re(φ) of a Gaussian wave-packet centered at S = 0,
t = 0, propagating in +S direction. Reference lines are overlaid for
v_p and v_g.

Run:
    .venv/bin/python projects/metric-mass/figures/velocities.py

Output:
    projects/metric-mass/figures/velocities.png
"""

import os

import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "velocities.png")

# Manifold parameters
L_U = 1.0
R_U = L_U / (2 * np.pi)
C = 1.0

# Plot range (S, t) in units of L_u and L_u/c respectively
S_MAX, T_MAX = 6.0, 6.0
N_S, N_T = 600, 600

S = np.linspace(-S_MAX, S_MAX, N_S)
t = np.linspace(0.0, T_MAX, N_T)
SS, TT = np.meshgrid(S, t)

# Wave-packet parameters: a Gaussian envelope around k_0
SIGMA_K = 0.6  # bandwidth in k
N_MODES = 41


def packet(k0, n_branch):
    """Sum of N_MODES Gaussian-weighted plane waves around k_0."""
    ks = np.linspace(k0 - 3 * SIGMA_K, k0 + 3 * SIGMA_K, N_MODES)
    weights = np.exp(-((ks - k0) ** 2) / (2 * SIGMA_K ** 2))
    field = np.zeros_like(SS, dtype=complex)
    for k, w in zip(ks, weights):
        omega = C * np.sqrt(k ** 2 + (n_branch / R_U) ** 2)
        field += w * np.exp(1j * (k * SS - omega * TT))
    field /= np.sum(weights)
    return field.real


# Two panels
fig, axes = plt.subplots(1, 2, figsize=(13.5, 6.0), constrained_layout=True)

panels = [
    dict(
        n=0, k0=2 * np.pi,
        title=r"$n = 0$  (massless light)",
        subtitle=r"$v_p = v_g = c$ — slopes match",
        ax=axes[0],
    ),
    dict(
        n=1, k0=2 * np.pi,
        title=r"$n = 1$  (massive branch)",
        subtitle=r"$v_p > c$, $v_g < c$ — slopes differ",
        ax=axes[1],
    ),
]

vmax = None
for p in panels:
    field = packet(p["k0"], p["n"])
    if vmax is None:
        vmax = np.max(np.abs(field))
    p["field"] = field

extent = (-S_MAX, S_MAX, 0.0, T_MAX)

for p in panels:
    ax = p["ax"]
    im = ax.imshow(
        p["field"], origin="lower", aspect="auto", extent=extent,
        cmap="RdBu_r", vmin=-vmax, vmax=vmax,
    )
    ax.set_title(f"{p['title']}\n{p['subtitle']}", fontsize=11)
    ax.set_xlabel(r"$S$ (extended spatial direction)")
    ax.set_ylabel(r"$t$ (time)")

    # Compute the velocities at the central wavenumber
    k0 = p["k0"]
    n = p["n"]
    omega0 = C * np.sqrt(k0 ** 2 + (n / R_U) ** 2)
    v_p = omega0 / k0
    v_g = (C ** 2 * k0) / omega0

    # Overlay phase-velocity line (slope dS/dt = v_p): a representative
    # crest line passing through (S=0, t=0)
    t_line = np.linspace(0, T_MAX, 100)
    S_phase = v_p * t_line  # phase line: S = v_p · t
    ax.plot(
        S_phase, t_line, color="black", linestyle="-",
        linewidth=2.0, label=rf"$v_p = {v_p:.2f}\,c$  (crest slope)",
    )

    # Overlay group-velocity line: envelope center moves with v_g
    S_group = v_g * t_line
    ax.plot(
        S_group, t_line, color="gold", linestyle="--",
        linewidth=2.5, label=rf"$v_g = {v_g:.2f}\,c$  (envelope slope)",
    )

    # Light-cone reference (slope = c)
    S_light = C * t_line
    ax.plot(
        S_light, t_line, color="0.4", linestyle=":",
        linewidth=1.0, label=r"$c$  (light cone)",
    )

    ax.legend(loc="upper left", fontsize=9, framealpha=0.85)
    ax.set_xlim(-S_MAX, S_MAX)
    ax.set_ylim(0, T_MAX)

fig.suptitle(
    r"Velocities as slopes on $(S, t)$: phase = crests, group = envelope",
    fontsize=12,
)

fig.savefig(OUT, dpi=140)
print(f"wrote {OUT}")
