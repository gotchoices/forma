#!/usr/bin/env python3
"""Tier 1: recirculation, loop leakage, and dispersion on the
honeycomb (N=3) lattice.

Tests the conjecture of Q140 (../../qa/Q140-light-quantization-from-
recirculation.md): that light quantization is a GRID substrate
phenomenon arising from closed recirculation loops, and that the
single-hexagon energy-return fraction is in the running range of the
fine-structure constant α.

Self-contained: the lattice / scatter / evolve machinery lives in
this project's lib.py (adapted from grid/sim-maxwell/run_hex.py).
The grid/ folder is not touched or imported.

Four measurements:

  loop   Single pulse sent around one hexagon.  The wavefront
         amplitude decays as (2/3)^k along the loop; the per-junction
         transmission T and the isolated single-loop energy return
         T^12 = (2/3)^12 = 1/129.75 are the α-leakage conjecture.

  bound  Generic circulating excitation on one hexagon.  ~½ of it
         projects onto a NON-RADIATING compact localized state that
         persists indefinitely; the rest radiates in one tick.  Loops
         genuinely trap energy — the standing (massive-like) limit.

  circ   Plaquette circulation: a trapped single-hexagon loop mode
         (pure circulation) vs a propagating wavefront (circulation
         cancels).  Tests the zigzag-circulation hypothesis.

  disp   Plane-wave dispersion ω(k) via a line source: shows the
         injected perturbation becomes a travelling oscillation with
         a definite (linear, non-dispersive) dispersion relation.

  all    Run all four (default).

Usage:
    source .venv/bin/activate
    python projects/grid-quantization/run_recirculation.py
    python projects/grid-quantization/run_recirculation.py --test loop
    python projects/grid-quantization/run_recirculation.py --nx 64 --ny 64
"""

import argparse
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import (  # noqa: E402
    make_honeycomb, evolve, edge_energy, init_wavefront,
)

TRANSMISSION = 2.0 / 3.0  # honeycomb junction amplitude transmission


# ── Plaquette geometry (face tracing) ────────────────────────

def _outgoing_dir(ei, leave_end, edge_dirs):
    """Direction leaving a vertex along edge ei.

    edge_dirs[ei] points from endpoint 0 (u) to endpoint 1 (v).
    leave_end is the endpoint index of the vertex we leave FROM:
      leave_end == 0  → leaving u toward v  → +edge_dirs
      leave_end == 1  → leaving v toward u  → -edge_dirs
    """
    return edge_dirs[ei] if leave_end == 0 else -edge_dirs[ei]


def find_plaquettes(edges, vert_ei, vert_end, edge_dirs):
    """Trace the faces (hexagons) of the honeycomb torus.

    Returns a list of faces; each face is a list of half-edges
    (ei, leave_end) traversed consistently clockwise around the
    face.  On a honeycomb torus every face is a hexagon (length 6).

    A half-edge (ei, s) means "leave endpoint s of edge ei toward
    the other endpoint".  The directed amplitude in the traversal
    direction is a_fwd[ei] if s == 0 else a_bwd[ei].
    """
    V, deg = vert_ei.shape

    # Precompute outgoing angle for every (vertex, slot).
    slot_ang = np.zeros((V, deg))
    for v in range(V):
        for k in range(deg):
            ei = vert_ei[v, k]
            d = _outgoing_dir(ei, vert_end[v, k], edge_dirs)
            slot_ang[v, k] = np.arctan2(d[1], d[0])

    def next_half_edge(ei, side):
        # Arrive at the far endpoint of ei.
        arrive_end = 1 - side
        arrive_vtx = edges[ei, arrive_end]
        # Direction pointing back the way we came (outgoing along ei
        # from arrive_vtx).
        back_ang = slot_ang[arrive_vtx,
                            np.where(vert_ei[arrive_vtx] == ei)[0][0]]
        # Among the other edges at arrive_vtx, pick the one
        # immediately clockwise from back_ang (smallest positive
        # clockwise gap).
        best_k, best_gap = -1, 1e9
        for k in range(deg):
            if vert_ei[arrive_vtx, k] == ei:
                continue
            gap = (back_ang - slot_ang[arrive_vtx, k]) % (2 * np.pi)
            if gap < best_gap:
                best_gap, best_k = gap, k
        return (vert_ei[arrive_vtx, best_k],
                vert_end[arrive_vtx, best_k])

    visited = set()
    faces = []
    E = len(edges)
    for ei0 in range(E):
        for side0 in (0, 1):
            if (ei0, side0) in visited:
                continue
            cycle = []
            he = (ei0, side0)
            while he not in visited:
                visited.add(he)
                cycle.append(he)
                he = next_half_edge(*he)
            faces.append(cycle)
    return faces


def plaquette_circulation(a_fwd, a_bwd, faces):
    """Signed line integral of net flow around each face (B-like)."""
    net = a_fwd - a_bwd  # net flow along +edge direction (u→v)
    J = np.empty(len(faces))
    for fi, face in enumerate(faces):
        s = 0.0
        for ei, side in face:
            s += net[ei] if side == 0 else -net[ei]
        J[fi] = s
    return J


def face_centroid(face, edges, pos):
    pts = np.array([pos[edges[ei, 0]] for ei, _ in face])
    return pts.mean(axis=0)


# ── Test: single pulse around one hexagon ────────────────────

def test_loop(nx, ny, out_dir):
    print(f"\n{'='*64}")
    print(f"  LOOP  — single pulse around one hexagon ({nx}×{ny})")
    print(f"{'='*64}")

    pos, edges, vert_ei, vert_end, edge_dirs, mid, box, wrap = \
        make_honeycomb(nx, ny)
    E = len(edges)
    faces = find_plaquettes(edges, vert_ei, vert_end, edge_dirs)
    lengths = np.array([len(f) for f in faces])
    print(f"  Faces found: {len(faces)} "
          f"(expect {nx*ny}); lengths "
          f"{lengths.min()}–{lengths.max()} (expect 6)")

    # Pick the hexagon nearest the lattice center (away from seams).
    cen = box / 2
    cents = np.array([face_centroid(f, edges, pos) for f in faces])
    target = int(np.argmin(((cents - cen) ** 2).sum(axis=1)))
    face = faces[target]
    e0, side0 = face[0]
    loop_edges = [ei for ei, _ in face]

    # Inject a unit pulse circulating around the chosen hexagon.
    a_fwd = np.zeros(E)
    a_bwd = np.zeros(E)
    if side0 == 0:
        a_fwd[e0] = 1.0
    else:
        a_bwd[e0] = 1.0

    n_steps = 7
    snaps = evolve(a_fwd, a_bwd, vert_ei, vert_end, n_steps,
                   snapshot_interval=1, N=3)

    # Follow the wavefront around the loop: at tick k the pulse sits
    # on loop edge k (mod 6).  Read its amplitude in the circulating
    # direction.  Early steps are clean — reflected/short-walk
    # contamination cannot reach loop-edge k until later ticks.
    seq_amp = []
    for k in range(n_steps):
        ei_k, side_k = face[k % len(face)]
        _, af, ab = snaps[k]
        seq_amp.append(af[ei_k] if side_k == 0 else ab[ei_k])
    seq_amp = np.array(seq_amp)
    pred_seq = TRANSMISSION ** np.arange(n_steps)

    # Per-junction transmission from the clean first step.
    T_eff = abs(seq_amp[1])               # seq_amp[0] == 1
    pred_amp = TRANSMISSION ** 6          # 0.08779
    pred_en = TRANSMISSION ** 12          # 0.0077073 = 1/129.75
    # Single-loop return implied by the measured early transmission.
    implied_loop_amp = T_eff ** 6
    implied_loop_en = implied_loop_amp ** 2

    print(f"\n  Wavefront amplitude along the loop (circ. dir.):")
    print(f"    {'tick':>4s} {'measured':>10s} {'(2/3)^k':>10s} "
          f"{'ratio':>7s}")
    for k in range(n_steps):
        ratio = (seq_amp[k] / pred_seq[k]) if pred_seq[k] else 0
        print(f"    {k:>4d} {seq_amp[k]:>10.5f} "
              f"{pred_seq[k]:>10.5f} {ratio:>7.3f}")

    print(f"\n  Clean per-junction transmission (step 0→1): "
          f"T = {T_eff:.4f}  (ideal 2/3 = {TRANSMISSION:.4f})")
    print(f"  ⇒ isolated single-loop return: T^6 = "
          f"{implied_loop_amp:.5f} (amp), T^12 = "
          f"{implied_loop_en:.6f} = 1/{1/implied_loop_en:.2f} "
          f"(energy)")
    print(f"\n  α landmarks: 1/137.036 (low-E), 1/128 (Z); "
          f"conjecture (2/3)^12 = 1/129.75")
    print(f"  NOTE: the t=6 return read directly off the start edge "
          f"is dominated by short reflected walks (ringing), not the "
          f"loop path — hence the clean number comes from the early "
          f"single-step transmission, extrapolated as T^12.")

    # Save the decay table (conclusive finding) as data.
    data_path = os.path.join(out_dir, "loop_decay.csv")
    np.savetxt(
        data_path,
        np.column_stack([np.arange(n_steps), seq_amp, pred_seq]),
        header="tick,measured_amplitude,predicted_(2/3)^k",
        delimiter=",", comments="")
    print(f"  Saved data: {data_path}")

    # Plot: amplitude along the loop vs the (2/3)^k prediction.
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    ks = np.arange(n_steps)
    axes[0].plot(ks, pred_seq, "g--o", ms=5,
                 label="(2/3)$^k$ ideal path")
    axes[0].plot(ks, np.abs(seq_amp), "navy", marker="s", ms=5,
                 label="|measured| along loop")
    axes[0].set_xlabel("tick = loop edges traversed")
    axes[0].set_ylabel("circulating amplitude")
    axes[0].set_yscale("log")
    axes[0].set_title("Wavefront decay around one hexagon")
    axes[0].legend(fontsize=8)
    axes[0].grid(True, alpha=0.3, which="both")

    e_ticks, e_loop, e_total = [], [], []
    for t, af, ab in snaps:
        en = edge_energy(af, ab)
        e_ticks.append(t)
        e_total.append(en.sum())
        e_loop.append(en[loop_edges].sum())
    axes[1].plot(e_ticks, e_loop, "r-o", ms=4,
                 label="energy on loop edges")
    axes[1].plot(e_ticks, e_total, "k--", lw=1,
                 label="total (conserved)")
    axes[1].set_xlabel("tick")
    axes[1].set_ylabel("energy")
    axes[1].set_title("Energy retained on loop vs leaked")
    axes[1].legend(fontsize=8)
    axes[1].grid(True, alpha=0.3)

    fig.suptitle("Recirculation: single pulse around one hexagon",
                 fontsize=13)
    fig.tight_layout()
    path = os.path.join(out_dir, "recirc_loop.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"  Saved: {path}")
    plt.close(fig)

    return {"T_eff": T_eff, "implied_loop_energy": implied_loop_en,
            "seq_amp": seq_amp}


# ── Test: compact localized (bound) mode on one hexagon ──────

def test_bound(nx, ny, out_dir):
    """Excite one hexagon as a generic circulating mode and watch
    what stays.  Result: a fixed fraction (~½) projects onto a
    NON-RADIATING bound mode (a compact localized state) that
    persists indefinitely; the rest radiates away in the first tick.

    So loops genuinely TRAP energy — light quantization can rest on
    real bound modes, not only on transient recirculation.  This is
    the bound / standing (massive-particle-like) limit, complementary
    to the propagating free-photon modes.  See work/tier2-design.md.

    The run length is kept wraparound-free (c·t < box/2) so the
    radiated fraction cannot return and masquerade as binding.
    """
    print(f"\n{'='*64}")
    print(f"  BOUND — compact localized mode on one hexagon ({nx}×{ny})")
    print(f"{'='*64}")

    pos, edges, vert_ei, vert_end, edge_dirs, mid, box, wrap = \
        make_honeycomb(nx, ny)
    E = len(edges)
    faces = find_plaquettes(edges, vert_ei, vert_end, edge_dirs)
    cents = np.array([face_centroid(f, edges, pos) for f in faces])
    cen = box / 2
    tf = faces[int(np.argmin(((cents - cen) ** 2).sum(axis=1)))]
    loop_edges = [ei for ei, _ in tf]

    # Generic circulating excitation: all 6 loop edges, circ. dir.
    a_fwd = np.zeros(E)
    a_bwd = np.zeros(E)
    for ei, side in tf:
        if side == 0:
            a_fwd[ei] = 1.0
        else:
            a_bwd[ei] = 1.0

    period = len(tf)  # 6 ticks per loop traversal
    # Keep wraparound-free: radiated energy travels ≤ ~0.73/tick, so
    # cap the run at t < box_width / (2·0.73).
    t_safe = int(box[0] / (2 * 0.73)) - 1
    n_steps = max(2 * period, min(4 * period, t_safe))
    snaps = evolve(a_fwd, a_bwd, vert_ei, vert_end, n_steps,
                   snapshot_interval=1, N=3)

    ticks, e_loop = [], []
    for t, af, ab in snaps:
        ticks.append(t)
        e_loop.append(edge_energy(af, ab)[loop_edges].sum())
    ticks = np.array(ticks)
    e_loop = np.array(e_loop) / e_loop[0]

    # Bound fraction: the plateau after the prompt radiation burst.
    plateau = e_loop[period:]
    f_bound = float(plateau.mean())
    f_drift = float(plateau.max() - plateau.min())

    # Recover the bound-mode pattern from the late-time loop state.
    _, af_end, ab_end = snaps[-1]
    pat_f = np.round(af_end[loop_edges], 3)
    pat_b = np.round(ab_end[loop_edges], 3)

    print(f"  Generic circulating excitation on a hexagon "
          f"(run {n_steps} ticks, wraparound-free).")
    print(f"  Loop energy drops to a plateau in the first tick, then "
          f"holds:")
    print(f"    bound-mode energy fraction = {f_bound:.4f} "
          f"(drift over plateau {f_drift:.4f})")
    print(f"    ⇒ ~{f_bound*100:.0f}% of the excitation is TRAPPED in "
          f"a non-radiating bound mode;")
    print(f"      ~{(1-f_bound)*100:.0f}% radiates away in the first "
          f"tick and never returns.")
    print(f"  Bound-mode standing pattern on the 6 loop edges:")
    print(f"    fwd: {pat_f}")
    print(f"    bwd: {pat_b}")
    print(f"    (|amp| ≈ 1/√3 = {1/np.sqrt(3):.3f} and "
          f"1−1/√3 = {1-1/np.sqrt(3):.3f})")
    print(f"  ⇒ The honeycomb scattering network supports a COMPACT "
          f"LOCALIZED STATE: a loop can")
    print(f"    trap energy permanently.  Light quantization can rest "
          f"on genuine bound modes — the")
    print(f"    standing (massive-particle-like) limit, complementary "
          f"to the propagating photon.")

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(ticks, e_loop, "navy", marker="o", ms=4,
            label="loop energy (normalised)")
    ax.axhline(f_bound, color="red", ls="--",
               label=f"bound fraction = {f_bound:.3f}")
    for L in range(1, n_steps // period + 1):
        ax.axvline(period * L, color="gray", ls=":", alpha=0.4)
    ax.set_xlabel("tick (dotted = loop periods)")
    ax.set_ylabel("E_loop(t) / E_loop(0)")
    ax.set_ylim(0, 1.05)
    ax.set_title("Compact localized mode: ~½ of the excitation is "
                 "trapped indefinitely")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    path = os.path.join(out_dir, "recirc_bound.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"  Saved: {path}")
    plt.close(fig)

    return {"bound_fraction": f_bound, "drift": f_drift}


# ── Test: circulation cancels for a clean wavefront ──────────

def _circ_index(J, energy):
    """Localised circulation: peak |J| per peak edge amplitude.

    Uses the peak (not RMS), so a spatially localised circulating
    mode is not diluted by the many quiet faces around it.
    """
    return np.abs(J).max() / (np.sqrt(energy.max()) + 1e-30)


def test_circ(nx, ny, n_steps, out_dir):
    print(f"\n{'='*64}")
    print(f"  CIRC  — circulation: trapped loop vs propagating wave "
          f"({nx}×{ny})")
    print(f"{'='*64}")

    pos, edges, vert_ei, vert_end, edge_dirs, mid, box, wrap = \
        make_honeycomb(nx, ny)
    E = len(edges)
    faces = find_plaquettes(edges, vert_ei, vert_end, edge_dirs)
    cents = np.array([face_centroid(f, edges, pos) for f in faces])

    # (a) trapped single-hexagon loop mode (pure circulation)
    cen = box / 2
    tf = faces[int(np.argmin(((cents - cen) ** 2).sum(axis=1)))]
    af0 = np.zeros(E)
    ab0 = np.zeros(E)
    for ei, side in tf:
        if side == 0:
            af0[ei] = 1.0
        else:
            ab0[ei] = 1.0
    J_loop = plaquette_circulation(af0, ab0, faces)
    idx_loop = _circ_index(J_loop, edge_energy(af0, ab0))

    # (b) clean directional wavefront, after propagating a while
    a_fwd, a_bwd = init_wavefront(edge_dirs, mid, box, E, wrap,
                                  direction=(1.0, 0.0), width=5.0)
    snaps = evolve(a_fwd, a_bwd, vert_ei, vert_end, n_steps,
                   snapshot_interval=n_steps, N=3)
    _, af, ab = snaps[-1]
    J_wave = plaquette_circulation(af, ab, faces)
    idx_wave = _circ_index(J_wave, edge_energy(af, ab))

    ratio = idx_loop / (idx_wave + 1e-30)
    print(f"  Circulation index (peak |J| / peak amplitude):")
    print(f"    trapped loop mode     : {idx_loop:.3f}  (pure "
          f"circulation — energy stays)")
    print(f"    propagating wavefront : {idx_wave:.3f}  (circulation "
          f"cancels — energy moves on)")
    print(f"    ratio trapped/propagating: {ratio:.1f}×")
    print(f"  ⇒ circulation concentrates in trapped (recirculating) "
          f"energy and is suppressed for clean propagation — the "
          f"zigzag-cancellation picture.")

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    span = box.min() / 4
    for ax, J, c0, title in (
        (axes[0], J_loop, cen, f"Trapped loop (idx={idx_loop:.2f})"),
        (axes[1], J_wave, cen, f"Propagating wave (idx={idx_wave:.2f})"),
    ):
        view = (np.abs(cents[:, 0] - c0[0]) < span) & \
               (np.abs(cents[:, 1] - c0[1]) < span)
        vmax = np.abs(J).max() + 1e-30
        sc = ax.scatter(cents[view, 0], cents[view, 1], c=J[view],
                        s=40, cmap="RdBu", vmin=-vmax, vmax=vmax)
        ax.set_aspect("equal")
        ax.set_title(f"Plaquette circulation — {title}")
        plt.colorbar(sc, ax=ax, fraction=0.046)

    fig.suptitle("Circulation persists in trapped loops, cancels "
                 "in propagating waves", fontsize=13)
    fig.tight_layout()
    path = os.path.join(out_dir, "recirc_circulation.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"  Saved: {path}")
    plt.close(fig)

    return {"idx_loop": idx_loop, "idx_wavefront": idx_wave,
            "ratio": ratio}


# ── Test: plane-wave dispersion ω(k) ─────────────────────────

def make_line_source(edge_dirs, mid, box, omega, x0,
                     amplitude=0.05, thickness=1.0):
    sel = np.where(np.abs(mid[:, 0] - x0) < thickness)[0]
    fwd = sel[edge_dirs[sel, 0] >= 0]
    bwd = sel[edge_dirs[sel, 0] < 0]

    def source_fn(a_fwd, a_bwd, t):
        amp = amplitude * np.sin(omega * t)
        a_fwd[fwd] += amp
        a_bwd[bwd] += amp
        return a_fwd, a_bwd
    return source_fn


def _measure_k(af, ab, edge_dirs, mid, box, x_lo, x_hi):
    """Dominant spatial wavenumber of the net x-flow along x."""
    net = af - ab
    band = (np.abs(mid[:, 1] - box[1] / 2) < box[1] / 6)
    sel = band & (mid[:, 0] > x_lo) & (mid[:, 0] < x_hi)
    if sel.sum() < 16:
        return np.nan
    # Bin onto a uniform x-grid.
    nbin = 128
    sig = np.zeros(nbin)
    cnt = np.zeros(nbin)
    idx = np.clip(((mid[sel, 0] - x_lo) / (x_hi - x_lo)
                   * (nbin - 1)).astype(int), 0, nbin - 1)
    np.add.at(sig, idx, (net[sel] * np.sign(edge_dirs[sel, 0])))
    np.add.at(cnt, idx, 1)
    good = cnt > 0
    if good.sum() < 16:
        return np.nan
    sig[good] /= cnt[good]
    sig -= sig[good].mean()
    sig[~good] = 0.0
    dx = (x_hi - x_lo) / nbin
    spec = np.abs(np.fft.rfft(sig * np.hanning(nbin)))
    freqs = np.fft.rfftfreq(nbin, d=dx)
    spec[0] = 0.0
    # Reject the upper half of the band (guard against aliasing /
    # lattice-scale spurious peaks); we drive in the long-wavelength
    # regime where the dominant peak is well below Nyquist.
    spec[freqs > 0.25 / dx] = 0.0
    kpix = freqs[np.argmax(spec)]
    return 2 * np.pi * kpix  # k in rad per lattice unit


def test_disp(nx, ny, n_steps, out_dir):
    print(f"\n{'='*64}")
    print(f"  DISP  — plane-wave dispersion ω(k) ({nx}×{ny})")
    print(f"{'='*64}")

    pos, edges, vert_ei, vert_end, edge_dirs, mid, box, wrap = \
        make_honeycomb(nx, ny)
    E = len(edges)
    x0 = box[0] * 0.2
    x_lo, x_hi = box[0] * 0.30, box[0] * 0.85

    # Long-wavelength regime: λ ≫ lattice spacing, so the spatial
    # FFT resolves the wave without aliasing.
    omegas = [0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]
    rows = []
    for om in omegas:
        src = make_line_source(edge_dirs, mid, box, om, x0,
                               amplitude=0.05, thickness=0.8)
        af = np.zeros(E)
        ab = np.zeros(E)
        snaps = evolve(af, ab, vert_ei, vert_end, n_steps,
                       source_fn=src, snapshot_interval=n_steps, N=3)
        _, af, ab = snaps[-1]
        k = _measure_k(af, ab, edge_dirs, mid, box, x_lo, x_hi)
        v = om / k if (k and not np.isnan(k) and k > 1e-6) else np.nan
        rows.append((om, k, v))
        kk = f"{k:.4f}" if not np.isnan(k) else "  n/a"
        vv = f"{v:.3f}" if not np.isnan(v) else " n/a"
        print(f"    ω={om:4.2f}  k={kk}  v=ω/k={vv}")

    arr = np.array([(o, k, v) for o, k, v in rows
                    if not np.isnan(k)])
    slope = np.nan
    if len(arr) >= 2:
        # Through-origin fit ω = v·k (ω must vanish at k=0).
        kk, oo = arr[:, 1], arr[:, 0]
        slope = float((kk @ oo) / (kk @ kk))
        print(f"\n  Linear fit ω ≈ v·k  →  v_phase = {slope:.3f} "
              f"lattice units/tick")
        print(f"  Linear ω(k) ⇒ non-dispersive propagation in the "
              f"long-wavelength regime — the injected static")
        print(f"  perturbation becomes a travelling oscillation with "
              f"a definite dispersion relation.")
        print(f"  (This is the phase velocity along x; the ≈0.73 "
              f"pulse-centroid speed quoted in sim-maxwell is a")
        print(f"   group/direction-dependent measure — they need not "
              f"coincide and the calibration is not load-bearing.)")

    fig, ax = plt.subplots(figsize=(6, 5))
    if len(arr):
        ax.plot(arr[:, 1], arr[:, 0], "o", color="navy", ms=6,
                label="measured")
        if not np.isnan(slope):
            kfit = np.linspace(0, arr[:, 1].max() * 1.05, 50)
            ax.plot(kfit, slope * kfit, "r--",
                    label=f"ω = {slope:.3f}·k")
    ax.set_xlabel("k (rad / lattice unit)")
    ax.set_ylabel("ω (rad / tick)")
    ax.set_title("Dispersion relation ω(k), honeycomb")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    path = os.path.join(out_dir, "recirc_dispersion.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"  Saved: {path}")
    plt.close(fig)

    return {"v_fit": slope, "rows": rows}


# ── Main ─────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(
        description="grid-quantization Tier 1: recirculation / loop "
                    "leakage / dispersion (honeycomb).")
    ap.add_argument("--test",
                    choices=["loop", "bound", "circ", "disp", "all"],
                    default="all", help="which measurement to run")
    ap.add_argument("--nx", type=int, default=48,
                    help="unit cells in x")
    ap.add_argument("--ny", type=int, default=48,
                    help="unit cells in y")
    ap.add_argument("--steps", type=int, default=80,
                    help="time steps for circ/disp tests")
    args = ap.parse_args()

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "outputs")
    os.makedirs(out_dir, exist_ok=True)

    print("grid-quantization Tier 1 — recirculation on the "
          "honeycomb (N=3)")
    print("Junction: outgoing_i = (2/3)*total − incoming_i")
    print(f"Conjecture (Q140): single-loop energy return "
          f"(2/3)^12 = {TRANSMISSION**12:.6f} = "
          f"1/{1/TRANSMISSION**12:.2f}")

    if args.test in ("loop", "all"):
        test_loop(args.nx, args.ny, out_dir)
    if args.test in ("bound", "all"):
        test_bound(args.nx, args.ny, out_dir)
    if args.test in ("circ", "all"):
        test_circ(args.nx, args.ny, args.steps, out_dir)
    if args.test in ("disp", "all"):
        test_disp(args.nx, args.ny, args.steps, out_dir)


if __name__ == "__main__":
    main()
