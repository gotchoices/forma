#!/usr/bin/env python3
"""
sim-dial-comparison — head-to-head test of three dial models.

Question
--------
Does the composite dial derived in chapter 2 perform the same function
as the simpler dials grid (and grid-lab) implicitly use? Specifically:

  Model A: identical-share single-value dial — one φ, all edges contribute equally.
  Model B: cos-weighted single-value dial — grid-lab style, one φ with cos(φ_attach) weighting.
  Model C: composite dial — chapter 2 model, 3 constituent points + 3 internal
           edges in a closed loop, each external edge at its own constituent point.

Method
------
All three dials have 3 attach points (matching 2D hex-vertex coordination).
Drive attach 0 with a sinusoid; pin attaches 1 and 2 to zero.
Run the chapter 1 §7-style update for many cycles.
Measure: how does each dial transmit the drive signal to attaches 1 and 2?
Compute the steady-state amplitude and phase response at each attach point.

If A, B, C give similar transmission, the composite dial is operationally
equivalent to the simpler grid-style dial — safe to use in 2D implementations.
If they differ, the differences need to be characterized before chapter 6.

Run
---
    cd projects/grid-couplet/scripts
    python sim-dial-comparison.py

Output
------
    output/dial-comparison.png — time-evolution of all three models
    output/dial-comparison-notes.txt — numeric summary
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTDIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTDIR, exist_ok=True)

T = 1200
DRIVE_FREQ = 0.02   # cycles per clock step
DRIVE_AMP = 1.0
N = 3               # 3 attach points
ATTACH_ANGLES = np.array([0.0, 2 * np.pi / 3, -2 * np.pi / 3])

NOTES = []


def note(msg):
    print(msg)
    NOTES.append(msg)


def drive(t):
    """External driving signal at each attach point.

    Attach 0: sinusoidal drive. Attaches 1 and 2: held at zero.
    """
    return np.array([
        DRIVE_AMP * np.cos(2 * np.pi * DRIVE_FREQ * t),
        0.0,
        0.0,
    ])


# ---------- Model A: identical-share single-value dial ----------

def run_identical():
    """One internal phase. All edges contribute and read equally."""
    phi = 0.0
    e = np.zeros(N)
    h_phi = [phi]
    h_e = [e.copy()]
    for t in range(T):
        phi_ext = drive(t)
        # Inhale: dial sums all incoming edges (no angular weighting)
        phi_new = phi + e.sum()
        # Exhale: each edge integrates (phi_ext - phi)
        e_new = e + (phi_ext - phi_new)
        phi, e = phi_new, e_new
        h_phi.append(phi)
        h_e.append(e.copy())
    return np.array(h_phi), np.array(h_e)


# ---------- Model B: cos-weighted single-value dial (grid-lab style) ----------

def run_cos_weighted():
    """One internal phase. Dial gathers edges with cos(angle) weighting."""
    phi = 0.0
    e = np.zeros(N)
    cos_w = np.cos(ATTACH_ANGLES)
    h_phi = [phi]
    h_e = [e.copy()]
    for t in range(T):
        phi_ext = drive(t)
        # Inhale: dial gathers with cos weighting
        phi_new = phi + np.sum(e * cos_w)
        # Exhale: each edge integrates (phi_ext - phi)
        e_new = e + (phi_ext - phi_new)
        phi, e = phi_new, e_new
        h_phi.append(phi)
        h_e.append(e.copy())
    return np.array(h_phi), np.array(h_e)


# ---------- Model C: composite dial (chapter 2) ----------

def run_composite():
    """3 constituent points + 3 internal edges in a closed loop.

    Each constituent point i has connections:
      - internal edge (i-1) % N: incoming (loop direction, +1 sign)
      - internal edge i: outgoing (loop direction, -1 sign)
      - external edge i: to outside lattice (chosen sign +1)

    Update rule: chapter 1 §7 with simplified ±1 sign convention
    (no cos-weighting on the inter-constituent loop, since we want to
    preserve the wave-equation structure of the closed loop).
    """
    phi_c = np.zeros(N)
    e_int = np.zeros(N)
    e_ext = np.zeros(N)
    h_phi = [phi_c.copy()]
    h_e_int = [e_int.copy()]
    h_e_ext = [e_ext.copy()]
    for t in range(T):
        phi_ext = drive(t)
        # Inhale: each constituent point updates from its 3 connections
        phi_c_new = np.array([
            phi_c[i] + e_int[(i - 1) % N] - e_int[i] + e_ext[i]
            for i in range(N)
        ])
        # Exhale: edges integrate
        e_int_new = np.array([
            e_int[i] + phi_c_new[i] - phi_c_new[(i + 1) % N]
            for i in range(N)
        ])
        e_ext_new = e_ext + (phi_ext - phi_c_new)
        phi_c, e_int, e_ext = phi_c_new, e_int_new, e_ext_new
        h_phi.append(phi_c.copy())
        h_e_int.append(e_int.copy())
        h_e_ext.append(e_ext.copy())
    return np.array(h_phi), np.array(h_e_int), np.array(h_e_ext)


# ---------- Steady-state analysis ----------

def steady_state_amplitude(history, t_window):
    """Extract sinusoidal amplitude over the last t_window steps via FFT."""
    last = history[-t_window:]
    # Subtract mean to suppress DC
    last = last - last.mean(axis=0)
    fft = np.fft.rfft(last, axis=0)
    freqs = np.fft.rfftfreq(t_window)
    # Find the bin closest to DRIVE_FREQ
    bin_idx = np.argmin(np.abs(freqs - DRIVE_FREQ))
    amplitudes = (2.0 / t_window) * np.abs(fft[bin_idx])
    phases = np.angle(fft[bin_idx])
    return amplitudes, phases


def report_response(name, h_phi, h_e_ext):
    """Report steady-state amplitudes at each attach point."""
    note(f"\n=== {name} ===")
    if h_phi.ndim == 1:
        amp_phi, _ = steady_state_amplitude(h_phi.reshape(-1, 1), 600)
        note(f"  internal φ amplitude: {amp_phi[0]:.4f}")
    else:
        amp_phi, _ = steady_state_amplitude(h_phi, 600)
        for i, a in enumerate(amp_phi):
            note(f"  φ_const[{i}] amplitude: {a:.4f}")

    amp_e, phs_e = steady_state_amplitude(h_e_ext, 600)
    for i, (a, p) in enumerate(zip(amp_e, phs_e)):
        note(f"  e_ext[{i}] amplitude: {a:.4f}, phase: {np.degrees(p):+7.2f}°")

    # Transmission ratio: e_ext[1] / e_ext[0] and e_ext[2] / e_ext[0]
    if amp_e[0] > 1e-9:
        note(f"  transmission |e_ext[1]/e_ext[0]| = {amp_e[1] / amp_e[0]:.4f}")
        note(f"  transmission |e_ext[2]/e_ext[0]| = {amp_e[2] / amp_e[0]:.4f}")


# ---------- Plotting ----------

def main():
    h_phi_a, h_e_a = run_identical()
    h_phi_b, h_e_b = run_cos_weighted()
    h_phi_c, h_e_int_c, h_e_ext_c = run_composite()

    note("Drive: sinusoid at attach 0 (freq = {:.3f}, amp = {:.2f})".format(DRIVE_FREQ, DRIVE_AMP))
    note("Attaches 1 and 2: external phase pinned to 0")

    report_response("Model A: identical-share", h_phi_a, h_e_a)
    report_response("Model B: cos-weighted (grid-lab style)", h_phi_b, h_e_b)
    report_response("Model C: composite (chapter 2)", h_phi_c, h_e_ext_c)

    fig, axes = plt.subplots(3, 1, figsize=(13, 11), sharex=True)

    # Show the last portion to skip transients
    T_show_start = 400

    # Model A
    ax = axes[0]
    ax.plot(np.arange(T_show_start, T + 1), h_phi_a[T_show_start:], label="φ (single)", color="C0", linewidth=1.5)
    for i in range(N):
        ax.plot(np.arange(T_show_start, T + 1), h_e_a[T_show_start:, i],
                label=f"e_ext[{i}]", linestyle="--", alpha=0.7)
    ax.set_title("Model A: identical-share single-value dial")
    ax.legend(loc="upper right", fontsize=8, ncol=2)
    ax.set_ylabel("value")
    ax.grid(alpha=0.3)

    # Model B
    ax = axes[1]
    ax.plot(np.arange(T_show_start, T + 1), h_phi_b[T_show_start:], label="φ (single)", color="C0", linewidth=1.5)
    for i in range(N):
        ax.plot(np.arange(T_show_start, T + 1), h_e_b[T_show_start:, i],
                label=f"e_ext[{i}]", linestyle="--", alpha=0.7)
    ax.set_title("Model B: cos-weighted single-value dial (grid-lab style)")
    ax.legend(loc="upper right", fontsize=8, ncol=2)
    ax.set_ylabel("value")
    ax.grid(alpha=0.3)

    # Model C
    ax = axes[2]
    for i in range(N):
        ax.plot(np.arange(T_show_start, T + 1), h_phi_c[T_show_start:, i], label=f"φ_const[{i}]", linewidth=1.3)
    for i in range(N):
        ax.plot(np.arange(T_show_start, T + 1), h_e_ext_c[T_show_start:, i],
                label=f"e_ext[{i}]", linestyle="--", alpha=0.6)
    ax.set_title("Model C: composite dial (3 points + 3 internal edges)")
    ax.legend(loc="upper right", fontsize=8, ncol=2)
    ax.set_ylabel("value")
    ax.set_xlabel("clock step")
    ax.grid(alpha=0.3)

    plt.tight_layout()
    out_path = os.path.join(OUTDIR, "dial-comparison.png")
    plt.savefig(out_path, dpi=120, bbox_inches="tight")
    plt.close()

    with open(os.path.join(OUTDIR, "dial-comparison-notes.txt"), "w") as f:
        f.write("\n".join(NOTES) + "\n")

    print(f"\nwrote {out_path}")
    print(f"wrote {os.path.join(OUTDIR, 'dial-comparison-notes.txt')}")


if __name__ == "__main__":
    main()
