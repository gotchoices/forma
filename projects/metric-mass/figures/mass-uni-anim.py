"""Animated visualization of wave modes on the (t, S, u) cylinder.

For each frame, renders the (S, u) cylinder colored by Re(φ) at the
current animation time. The cylinder axis runs along x (= S);
u is angular in the y-z plane around the cylinder; the circular
extent of u "grows into y" as the user specified.

t is the animation parameter rather than a spatial axis. (The
user's preferred t-in-z layout would require a 4D rendering, so
this animation uses time-as-time and reserves the spatial axes
for the manifold's spatial coordinates.)

Three modes are rendered as separate sub-animations stacked in
sequence in the same GIF: n = 0 light, n = 1 rest, n = 1 moving.

Run:
    .venv/bin/python projects/metric-mass/figures/mass-uni-anim.py

Output:
    projects/metric-mass/figures/mass-uni-anim.gif
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.animation import FuncAnimation, PillowWriter

OUT = os.path.join(os.path.dirname(__file__), "mass-uni-anim.gif")

L_U = 2 * np.pi
R_U = 1.0
C = 1.0

S_MAX = 3.0
N_S, N_U = 80, 50

S_grid = np.linspace(-S_MAX, S_MAX, N_S)
u_grid = np.linspace(0, L_U, N_U)
SS, UU = np.meshgrid(S_grid, u_grid, indexing="ij")

# Cylinder embedding: axis along x = S, u angular in yz plane
theta = 2 * np.pi * UU / L_U
X = SS
Y = R_U * np.cos(theta)
Z_CYL = R_U * np.sin(theta)

# Three modes; the animation will sweep through all three.
modes = [
    dict(n=0, k_S=2 * np.pi, label=r"$n = 0$ (light)"),
    dict(n=1, k_S=0.0, label=r"$n = 1$, rest"),
    dict(n=1, k_S=2 * np.pi, label=r"$n = 1$, moving"),
]
FRAMES_PER_MODE = 30
T_PER_MODE = 1.5  # animation time spans 1.5 dimensionless units per mode

fig = plt.figure(figsize=(10, 4))
ax = fig.add_subplot(111, projection="3d")

vmax = 1.0
norm = plt.Normalize(-vmax, vmax)


def frame_to_state(frame_idx):
    """Map flat frame index to (mode, t)."""
    mode_idx = frame_idx // FRAMES_PER_MODE
    if mode_idx >= len(modes):
        mode_idx = len(modes) - 1
    sub_frame = frame_idx % FRAMES_PER_MODE
    t = sub_frame * T_PER_MODE / FRAMES_PER_MODE
    return mode_idx, t


def update(frame_idx):
    mode_idx, t = frame_to_state(frame_idx)
    m = modes[mode_idx]
    n, k_S = m["n"], m["k_S"]
    omega = C * np.sqrt(k_S ** 2 + (n / R_U) ** 2)
    phase = k_S * SS - omega * t + (n / R_U) * UU
    re_phi = np.cos(phase)
    colors = cm.RdBu_r(norm(re_phi))

    ax.clear()
    ax.plot_surface(
        X, Y, Z_CYL,
        facecolors=colors, rstride=1, cstride=1,
        shade=False, antialiased=True,
        edgecolor="none",
    )
    ax.set_xlim(-S_MAX, S_MAX)
    ax.set_ylim(-2 * R_U, 2 * R_U)
    ax.set_zlim(-2 * R_U, 2 * R_U)
    ax.view_init(elev=15, azim=-60)
    ax.set_xlabel(r"$S$ (extended)")
    ax.set_yticks([]); ax.set_zticks([])
    ax.set_title(
        f"{m['label']}    t = {t:.2f}    "
        rf"$\omega$ = {omega:.2f}",
        fontsize=10,
    )
    return []


total_frames = FRAMES_PER_MODE * len(modes)
ani = FuncAnimation(
    fig, update, frames=total_frames, interval=80, blit=False,
)
ani.save(OUT, writer=PillowWriter(fps=12))
print(f"wrote {OUT}")
