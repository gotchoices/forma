"""
Saturation/overflow as the means by which energy crosses a sheet boundary.

ARENA — a cylinder: one extended direction x, one compact direction c, as a
product lattice. Four registers per node (+x, -x, +c, -c). Rings at neighbouring
x are joined along x, so anything made on a ring can in principle travel.

LINEAR SECTOR (--linear, default `pooled`). The ordinary GRID scatter
S = (2/N)J - I over all four registers. On a translation-invariant lattice this
already keeps the compact sectors apart exactly --- k_c is a Bloch label and no
linear rule mixes k_c = 0 with k_c != 0 --- while also supplying Kaluza-Klein
dispersion: cos(Omega) = (cos k_x + cos k_c)/2, even in k_x, with v_g(0) = 0 and
a mass tower Omega_0(n) rising with winding. It is strictly node-local and
reciprocal.

  An earlier version of this project used a bespoke coupling instead, on the
  belief that the pooled rule had to be replaced to keep the sectors separate.
  It does not: the separation is automatic. Those variants were worse on every
  count --- a constant rotation gave light a mass gap, and a winding-dependent
  one gave a band that was not even in k_x, so a mode "at rest" drifted at
  +0.107. `--linear separated` reproduces the pass-through variant for
  comparison; `--grad` reproduces the gradient coupling.

NONLINEAR SECTOR — the project's actual claim. Where a group's total |T|
exceeds --sat, the excess rotates between the x and c register pairs. Rotation
is exactly orthogonal, so the crossing conserves energy to machine precision
and accounts for whatever the ring already holds. Both directions run: x -> c
makes a particle, c -> x returns it.

  So the posit under test is about the NONLINEAR channel only: below the
  ceiling nothing crosses that the pooled rule would not already forbid; above
  it, overflow carries energy across in bulk.

DIAGNOSTICS (each reproduces a section of work/measurements.md):
  --bloch         exact dispersion table for the linear sector        (M3, M7)
  --timeseries    Omega measured from a long run at one (k_x, k_c)    (M3)
  --packet        launch a single-branch wound packet, report its
                  speed against Kaluza-Klein's v_g = c^2 k / Omega    (M3, M6)
  --seed-ring     seed a ring standing wave at rest, no drive, and
                  track its x-centroid                                (M3)
  --sweep LIST    drive-frequency sweep with per-frequency seed
                  statistics; --seeds sets the number of ZPE
                  realisations, which is the error bar on any
                  resonance claim                                     (M5)
With none of these, the script does one driven run: energy audit, overflow
event count, and the winding fraction.                                (M1, M2, M4)
"""
import argparse
import os
import numpy as np


def propagate(f):
    o = np.empty_like(f)
    o[0] = np.roll(f[0], 1, axis=0)
    o[1] = np.roll(f[1], -1, axis=0)
    o[2] = np.roll(f[2], 1, axis=1)
    o[3] = np.roll(f[3], -1, axis=1)
    return o


def scatter(f, mode):
    if mode == "pooled":
        return 0.5 * f.sum(0)[None, ...] - f
    return f.copy()                                   # separated: pass-through


def rotate_groups(f, ang):
    c, s = np.cos(ang), np.sin(ang)
    o = f.copy()
    o[0] = c * f[0] - s * f[2]; o[2] = s * f[0] + c * f[2]
    o[1] = c * f[1] - s * f[3]; o[3] = s * f[1] + c * f[3]
    return o


def gradient_couple(f, g):
    """Retained for reproduction only. Angle = g*(1-cos k_c): keeps light
    massless but gives a band that is NOT even in k_x, so a wound mode at rest
    drifts. Superseded by the pooled linear sector."""
    if not g:
        return f
    nc = f.shape[2]
    F = np.fft.fft(f, axis=2)
    th = g * (1.0 - np.cos(2 * np.pi * np.fft.fftfreq(nc)))
    c, s = np.cos(th), np.sin(th)
    G = np.empty_like(F)
    G[0] = c * F[0] - s * F[2]; G[2] = s * F[0] + c * F[2]
    G[1] = c * F[1] - s * F[3]; G[3] = s * F[1] + c * F[3]
    return np.real(np.fft.ifft(G, axis=2))


def step(f, sat, gain, linear="pooled", grad=0.0):
    o = scatter(f, linear)
    if grad:
        o = gradient_couple(o, grad)
    nfire = 0
    if sat > 0:
        Tx = np.abs(o[0] + o[1]); Tc = np.abs(o[2] + o[3])
        over = np.maximum(Tx - sat, 0.0)
        back = np.maximum(Tc - sat, 0.0)
        nfire = int(((over > 0) | (back > 0)).sum())
        if nfire:
            o = rotate_groups(o, gain * (over - back))
    return propagate(o), nfire


# ----------------------------------------------------------------- analysis

def bloch(kx, kc, linear, grad=0.0):
    """Exact physical frequencies at (kx, kc) for the linear sector."""
    S = (0.5 * np.ones((4, 4)) - np.eye(4)) if linear == "pooled" else np.eye(4)
    if grad:
        th = grad * (1 - np.cos(kc)); c, s = np.cos(th), np.sin(th)
        S = np.array([[c, 0, -s, 0], [0, c, 0, -s],
                      [s, 0, c, 0], [0, s, 0, c]]) @ S
    P = np.diag([np.exp(-1j * kx), np.exp(1j * kx),
                 np.exp(-1j * kc), np.exp(1j * kc)])
    w = np.abs(np.angle(np.linalg.eigvals(P @ S)))
    O = (np.pi - w) if linear == "pooled" else w        # pooled band sits at pi
    O = O[O < np.pi - 1e-9]        # drop the flat non-propagating branch only
    return np.sort(np.unique(np.round(O, 9))) if len(O) else np.zeros(1)


def run_bloch(a):
    kc = 2 * np.pi * a.n / a.nc
    print(f"linear={a.linear}  grad={a.grad}  nc={a.nc}  winding n={a.n}  "
          f"(k_c={kc:.4f})")
    b0 = bloch(0.0, kc, a.linear, a.grad)
    w0 = b0.max() if len(b0) else 0.0
    cc = 1 / np.sqrt(2) if a.linear == "pooled" else 1.0
    print(f"rest frequency omega_0 = {w0:.6f}   lattice c = {cc:.4f}")
    print(f"{'k_x':>7} {'Omega':>10} {'KK sqrt(c^2k^2+w0^2)':>22} {'err':>8} {'v_g':>9}")
    for kx in (-0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3):
        w = bloch(kx, kc, a.linear, a.grad).max()
        kk = np.sqrt((cc * kx) ** 2 + w0 ** 2)
        vg = (bloch(kx + 0.01, kc, a.linear, a.grad).max()
              - bloch(kx - 0.01, kc, a.linear, a.grad).max()) / 0.02
        print(f"{kx:7.2f} {w:10.6f} {kk:22.6f} {100*(w-kk)/kk:7.1f}% {vg:9.5f}")
    e = np.isclose(bloch(-0.1, kc, a.linear, a.grad).max(),
                   bloch(0.1, kc, a.linear, a.grad).max())
    v0 = (bloch(0.01, kc, a.linear, a.grad).max()
          - bloch(-0.01, kc, a.linear, a.grad).max()) / 0.02
    print(f"even in k_x: {e}      v_g at rest: {v0:+.8f}   "
          f"{'(a mode at rest is at rest)' if abs(v0) < 1e-6 else '(DRIFTS)'}")
    print("light (k_c=0): " + ", ".join(
        f"k={k}: {bloch(k,0.0,a.linear,a.grad).max():.4f}" for k in (0.0, 0.1, 0.3)))
    print("mass tower:    " + ", ".join(
        f"n={m}: {bloch(0.0,2*np.pi*m/a.nc,a.linear,a.grad).max():.4f}"
        for m in (1, 2, 3)))


def run_timeseries(a):
    """Measure Omega from a long run, as an independent check on the exact
    Bloch spectrum. The state is seeded with ONE branch's eigenvector, or the
    signal is a mixture and the FFT reports whichever branch dominates."""
    nx = 64
    kx = 2 * np.pi * round(a.kx * nx / (2 * np.pi)) / nx
    kc = 2 * np.pi * a.n / a.nc
    v, Oex = branch_mode(kx, kc, a.linear, a.grad)
    x = np.arange(nx); c = np.arange(a.nc)
    ph = np.exp(1j * (np.outer(kx * x, np.ones(a.nc))
                      + np.outer(np.ones(nx), kc * c)))
    f = np.real(v[:, None, None] * ph[None, :, :]) * a.amp
    rec = np.zeros(a.steps)
    for t in range(a.steps):
        f, _ = step(f, 0.0, a.gain, a.linear, a.grad)
        rec[t] = f[0, 0, 0]
    S = np.abs(np.fft.rfft((rec - rec.mean()) * np.hanning(a.steps)))
    S[0] = 0.0                                    # DC is not a lattice mode
    w = 2 * np.pi * np.argmax(S) / a.steps
    O = (np.pi - w) if a.linear == "pooled" else w
    print(f"k_x={kx:.4f} n={a.n} nc={a.nc} linear={a.linear}")
    print(f"  measured Omega = {O:.4f}   exact = {Oex:.4f}   "
          f"error {100*(O-Oex)/Oex:+.2f}%   (resolution {2*np.pi/a.steps:.4f})")


def run_seed_ring(a):
    nx = 81; mid = nx // 2; x = np.arange(nx); c = np.arange(a.nc)
    f = np.zeros((4, nx, a.nc))
    prof = a.amp * np.cos(2 * np.pi * a.n * c / a.nc)
    f[2, mid, :] = prof; f[3, mid, :] = prof
    e0 = float((f ** 2).sum())
    for t in range(a.steps):
        f, _ = step(f, a.sat, a.gain, a.linear, a.grad)
    e = (f[2] ** 2 + f[3] ** 2).sum(axis=1)
    cen = (e * x).sum() / max(e.sum(), 1e-30) - mid
    print(f"ring seed amp={a.amp} n={a.n} sat={a.sat}: compact centroid moved "
          f"{cen:+.4f} nodes in {a.steps} ticks; compact energy "
          f"{float((f[2]**2+f[3]**2).sum()):.4e} of {e0:.4e}")


def run_driven(a, omega, seed):
    """One driven run. Returns (winding energy, total energy, overflow events)."""
    rng = np.random.default_rng(seed)
    f = np.zeros((4, a.nx, a.nc))
    m = 20; ramp = np.linspace(0, 0.10, m)
    sx = np.ones(a.nx); sx[:m] = 1 - ramp[::-1]; sx[-m:] = 1 - ramp
    drive = (np.pi - omega) if a.linear == "pooled" else omega
    fired = 0
    for t in range(a.steps):
        f, nf = step(f, a.sat, a.gain, a.linear, a.grad); fired += nf
        env = (a.amp * min(1.0, t / 80.0) if a.cw
               else a.amp * np.exp(-((t - 60.0) / 14.0) ** 2))
        if env > 1e-6 and not a.no_drive:
            f[0, a.pad, :] += env * np.cos(drive * t)
            f[1, a.nx - 1 - a.pad, :] += env * np.cos(drive * t)
        if a.zpe:
            f[:2] += a.zpe * rng.standard_normal(f[:2].shape)
        f *= sx[None, :, None]
    P = (np.abs(np.fft.fft(f[2], axis=1)) ** 2
         + np.abs(np.fft.fft(f[3], axis=1)) ** 2) / a.nc
    return float(P[:, 1:].sum()), float((f ** 2).sum()), fired


def run_sweep(a):
    """Drive-frequency sweep with per-frequency seed statistics. The seed sets
    the ZPE noise, which is the only thing that breaks the ring's c-symmetry,
    so seed-to-seed scatter is the error bar on any resonance claim."""
    ws = [float(x) for x in a.sweep.split(",")]
    print(f"sweep: nc={a.nc} amp={a.amp} sat={a.sat} linear={a.linear} "
          f"steps={a.steps}, {a.seeds} seeds each")
    print("  mass tower: " + ", ".join(
        f"n={m}: {bloch(0.0, 2*np.pi*m/a.nc, a.linear, a.grad).max():.4f}"
        for m in (1, 2, 3)))
    print(f"{'Omega':>8} {'wound/total':>12} {'sd':>9} {'min':>8} {'max':>8} {'events':>9}")
    for w in ws:
        r = [run_driven(a, w, s) for s in range(1, a.seeds + 1)]
        q = np.array([x[0] / max(x[1], 1e-30) for x in r])
        print(f"{w:8.4f} {q.mean():12.4f} {q.std(ddof=1):9.4f} "
              f"{q.min():8.4f} {q.max():8.4f} {np.mean([x[2] for x in r]):9.0f}")


def branch_mode(kx, kc, linear, grad, heavy=True):
    """Eigenvector and physical frequency of one Bloch branch at (kx, kc)."""
    S = (0.5 * np.ones((4, 4)) - np.eye(4)) if linear == "pooled" else np.eye(4)
    if grad:
        th = grad * (1 - np.cos(kc)); c, s = np.cos(th), np.sin(th)
        S = np.array([[c, 0, -s, 0], [0, c, 0, -s],
                      [s, 0, c, 0], [0, s, 0, c]]) @ S
    P = np.diag([np.exp(-1j * kx), np.exp(1j * kx),
                 np.exp(-1j * kc), np.exp(1j * kc)])
    w, V = np.linalg.eig(P @ S)
    ang = np.angle(w)
    # Each (kx, kc) carries a conjugate PAIR with the same Omega and opposite
    # group velocity -- a mode and its time-reverse. Pick the forward-time one
    # by the sign of the eigenphase, or the packet's direction is arbitrary.
    O = (np.pi - ang) if linear == "pooled" else ang
    ok = np.where((ang > 0) & (O < np.pi - 1e-9) & (O > 1e-9))[0]
    if not len(ok):
        ok = np.where(O < np.pi - 1e-9)[0]
    i = ok[np.argmax(O[ok])] if heavy else ok[np.argmin(O[ok])]
    return V[:, i], O[i]


def run_packet(a):
    """Launch a single-branch wound packet at k_x and measure its speed against
    Kaluza-Klein's v_g = c^2 k / Omega. Periodic in x: no absorber, so the
    packet is the only thing in the box."""
    nx = a.nx; kc = 2 * np.pi * a.n / a.nc
    x = np.arange(nx); c = np.arange(a.nc)
    cc = 1 / np.sqrt(2) if a.linear == "pooled" else 1.0
    kx0 = 2 * np.pi * round(a.kx * nx / (2 * np.pi)) / nx
    F = np.zeros((4, nx, a.nc), dtype=complex)
    cw = np.exp(1j * kc * c)
    for j in range(nx):
        k = 2 * np.pi * j / nx
        d = np.angle(np.exp(1j * (k - kx0)))
        wgt = np.exp(-(d / a.kw) ** 2 / 2)
        if wgt < 1e-10:
            continue
        v, _ = branch_mode(k, kc, a.linear, a.grad)
        F += wgt * v[:, None, None] * np.exp(1j * k * x)[None, :, None] * cw[None, None, :]
    f = np.real(F); f *= a.amp / np.abs(f).max()
    _, O0 = branch_mode(kx0, kc, a.linear, a.grad)
    vkk = cc ** 2 * kx0 / O0

    def centroid(g):
        e = (g ** 2).sum(axis=(0, 2))
        ph = np.exp(2j * np.pi * x / nx)
        return np.angle((e * ph).sum() / e.sum()) * nx / (2 * np.pi)

    e0 = float((f ** 2).sum())
    ts = [0]; cs = [centroid(f)]; fired = 0
    for t in range(a.steps):
        f, nf = step(f, a.sat, a.gain, a.linear, a.grad); fired += nf
        if (t + 1) % 10 == 0:
            ts.append(t + 1); cs.append(centroid(f))
    # unwrap the periodic centroid, then fit a straight line for the speed
    cs = np.array(cs); ts = np.array(ts, dtype=float)
    u = np.concatenate([[cs[0]], cs[0] + np.cumsum(
        np.angle(np.exp(1j * 2 * np.pi * np.diff(cs) / nx)) * nx / (2 * np.pi))])
    v = np.polyfit(ts, u, 1)[0]
    d = u[-1] - u[0]
    print(f"packet n={a.n} k_x={kx0:.4f} nc={a.nc} sat={a.sat} linear={a.linear}"
          f"{f' grad={a.grad}' if a.grad else ''}")
    print(f"  Omega = {O0:.6f}   lattice c = {cc:.4f}")
    print(f"  moved {d:+.3f} nodes in {a.steps} ticks -> v = {v:+.5f}")
    print(f"  KK v_g = c^2 k / Omega = {vkk:+.5f}   "
          f"error {100*(v-vkk)/vkk if vkk else float('nan'):+.1f}%")
    P = (np.abs(np.fft.fft(f[2], axis=1)) ** 2
         + np.abs(np.fft.fft(f[3], axis=1)) ** 2) / a.nc
    tot = float((f ** 2).sum())
    print(f"  overflow events {fired}   wound/total {P[:,1:].sum()/tot:.4f}")
    print(f"  energy {e0:.6e} -> {tot:.6e}")


def main():

    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nx", type=int, default=201)
    p.add_argument("--nc", type=int, default=24)
    p.add_argument("--steps", type=int, default=900)
    p.add_argument("--linear", choices=["pooled", "separated"], default="pooled")
    p.add_argument("--grad", type=float, default=0.0,
                   help="superseded gradient coupling; reproduction only")
    p.add_argument("--sat", type=float, default=0.8)
    p.add_argument("--gain", type=float, default=0.5)
    p.add_argument("--amp", type=float, default=0.5)
    p.add_argument("--omega", type=float, default=0.2618,
                   help="PHYSICAL drive frequency Omega")
    p.add_argument("--n", type=int, default=1, help="winding for diagnostics")
    p.add_argument("--kx", type=float, default=0.2945)
    p.add_argument("--zpe", type=float, default=1e-3)
    p.add_argument("--cw", action="store_true")
    p.add_argument("--no-drive", action="store_true")
    p.add_argument("--pad", type=int, default=30)
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--bloch", action="store_true")
    p.add_argument("--timeseries", action="store_true")
    p.add_argument("--seed-ring", action="store_true")
    p.add_argument("--packet", action="store_true")
    p.add_argument("--kw", type=float, default=0.05,
                   help="packet width in k_x")
    p.add_argument("--sweep", type=str, default=None,
                   help="comma-separated PHYSICAL drive frequencies to sweep")
    p.add_argument("--seeds", type=int, default=8,
                   help="seeds per sweep point (ZPE realisations)")
    a = p.parse_args()

    if a.bloch:
        return run_bloch(a)
    if a.timeseries:
        return run_timeseries(a)
    if a.seed_ring:
        return run_seed_ring(a)
    if a.packet:
        return run_packet(a)
    if a.sweep:
        return run_sweep(a)

    rng = np.random.default_rng(a.seed)
    probe = rng.standard_normal((4, 40, a.nc))
    e0 = float((probe ** 2).sum())
    q, _ = step(probe, a.sat, a.gain, a.linear, a.grad)
    print(f"step() energy audit: {e0:.6f} -> {float((q**2).sum()):.6f}   "
          f"drift {abs(float((q**2).sum())-e0)/e0:.2e}")

    wound, tot, fired = run_driven(a, a.omega, a.seed)
    print(f"linear={a.linear}  nc={a.nc}  Omega={a.omega:.4f}  sat={a.sat}  "
          f"amp={a.amp}  seed={a.seed}")
    print(f"  overflow events {fired}")
    print(f"  winding k_c!=0 {wound:.4e}  total {tot:.4e}  "
          f"wound/total {wound/max(tot,1e-30):.4f}")


if __name__ == "__main__":
    main()
