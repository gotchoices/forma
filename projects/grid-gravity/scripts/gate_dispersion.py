"""
Gate go/no-go (dispersion leg) for projects/grid-gravity.

Question
--------
Does the congestion slow a wave by an amount INDEPENDENT of frequency (a
delay -> time dilation) or DEPENDENT on frequency (a low-pass filter ->
optical medium)?  work/local-time.md Commitment 3; work/congestion-falloff.md
sec 6.

Two edge models, run side by side, because the answer depends on the edge's
character:

  LOSSY edge  (leaky integrator): u_i(t+1) = (1-a) u_i + a u_{i-1}, a<1.
    A finite-bandwidth edge WITH loss. Attenuates high frequencies -> a
    low-pass. Expected: strongly dispersive (and lossy).

  LOSSLESS edge (reduced local wave speed): a proper energy-conserving wave
    equation u_tt = c(x)^2 u_xx, with c tapered below 1 in a loaded region.
    No damping -> lossless. Expected: a uniform delay ~ L(1/c - 1),
    frequency-independent -> non-dispersive.

The point of the comparison: losslessness was already required for the 1/r
falloff (work/shunt-check.md). This sim asks whether the SAME commitment
also buys non-dispersivity -- i.e. whether the dispersion seen in the lossy
model is a symptom of loss rather than of the mechanism.

Method: drive a windowed wavepacket of centre frequency omega, send it
through the loaded region, measure its arrival centroid at an output cell
vs a free (unloaded) run. Extra arrival time = group delay. Sweep omega;
flat group delay across the passband = non-dispersive.

Inputs (argparse)
-----------------
  --length   chain length (default 1600)
  --nload    loaded cells (default 300)
  --closs    lossless loaded wave speed, <1 (default 0.6)
  --aloss    lossy edge coefficient a<1 (default 0.6)
  --wmin/-wmax/-nw   omega sweep (default 0.1 .. 1.6, 24 pts)
  --out      output dir (default ../outputs)

Outputs: printed group-delay tables + passband flatness verdict; a PNG.
"""

import argparse
import os
import numpy as np


def centroid_amp(rec):
    """Arrival = time of the main transmitted pulse (peak of the smoothed
    envelope), robust to interface reflections; amplitude = that peak."""
    e = rec ** 2
    win = 41
    es = np.convolve(e, np.ones(win) / win, mode="same")
    i = int(np.argmax(es))
    return float(i), float(np.sqrt(es[i]))


def run_lossy(a_load, omega, length, nload, load_a, t0, sigma, nsteps, out_cell):
    u = np.zeros(length)
    a = np.ones(length)
    a[load_a:load_a + nload] = a_load
    a1 = a[1:]
    rec = np.empty(nsteps)
    for t in range(nsteps):
        un = u.copy()
        un[1:] = (1.0 - a1) * u[1:] + a1 * u[:-1]
        un[0] = np.exp(-((t - t0) / sigma) ** 2) * np.cos(omega * t)
        u = un
        rec[t] = u[out_cell]
    return centroid_amp(rec)


def run_lossless(c_load, omega, length, nload, load_a, t0, sigma, nsteps,
                 out_cell, src=200):
    """Energy-conserving leapfrog wave with a smoothly tapered slow region
    and sponge (absorbing) ends. Lossless in the interior."""
    cour = 0.95
    c = np.ones(length)
    taper = 30
    lo, hi = load_a, load_a + nload
    c[lo:hi] = c_load
    # smooth the speed profile to limit interface reflection
    k = np.ones(taper) / taper
    c = np.convolve(c, k, mode="same")
    c[:taper] = 1.0
    c[-taper:] = 1.0
    c2 = (c * cour) ** 2

    # sponge damping only in the outer margins (outside the measured region)
    damp = np.zeros(length)
    m = 60
    ramp = np.linspace(0, 0.08, m)
    damp[:m] = ramp[::-1]
    damp[-m:] = ramp

    up = np.zeros(length)   # u_{n-1}
    uc = np.zeros(length)   # u_n
    rec = np.empty(nsteps)
    for t in range(nsteps):
        lap = np.zeros(length)
        lap[1:-1] = uc[2:] - 2 * uc[1:-1] + uc[:-2]
        un = 2 * uc - up + c2 * lap
        un += cour ** 2 * np.exp(-((t - t0) / sigma) ** 2) * np.cos(omega * t) \
            * (np.arange(length) == src)
        un *= (1.0 - damp)          # sponge
        up, uc = uc, un
        rec[t] = uc[out_cell]
    return centroid_amp(rec)


def sweep(model, param, omegas, length, nload, load_a):
    t0, sigma = 300.0, 80.0
    out_cell = load_a + nload + 80
    nsteps = int(2 * (out_cell + length) + 6 * sigma + 1200)
    delays, trans = [], []
    for om in omegas:
        if model == "lossy":
            tl, al = run_lossy(param, om, length, nload, load_a, t0, sigma,
                               nsteps, out_cell)
            tf, af = run_lossy(1.0, om, length, nload, load_a, t0, sigma,
                               nsteps, out_cell)
        else:
            tl, al = run_lossless(param, om, length, nload, load_a, t0, sigma,
                                  nsteps, out_cell)
            tf, af = run_lossless(1.0, om, length, nload, load_a, t0, sigma,
                                  nsteps, out_cell)
        delays.append(tl - tf)
        trans.append(al / af if af > 0 else np.nan)
    return np.array(delays), np.array(trans)


def report(name, omegas, delays, trans, floor=0.7):
    print(f"\n--- {name} ---")
    print("  omega   group_delay   transmission")
    for om, d, t in zip(omegas, delays, trans):
        print(f"  {om:5.2f}   {d:10.2f}   {t:7.3f}")
    band = trans >= floor
    if np.count_nonzero(band) >= 3:
        d = delays[band]
        rel = (d.max() - d.min()) / abs(d.mean()) if d.mean() else np.nan
        print(f"  passband (transmission>{floor}): "
              f"omega in [{omegas[band].min():.2f},{omegas[band].max():.2f}], "
              f"delay {d.mean():.1f}, spread {100*rel:.1f}%")
        verdict = ("NON-DISPERSIVE across passband (time dilation)" if rel < 0.05
                   else "mild dispersion — inspect" if rel < 0.15
                   else "DISPERSIVE (optical medium)")
        print(f"  -> {verdict}")
    else:
        print(f"  passband too narrow (transmission collapses) -> strongly "
              f"low-pass / dispersive")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--length", type=int, default=1600)
    p.add_argument("--nload", type=int, default=300)
    p.add_argument("--closs", type=float, default=0.6)
    p.add_argument("--aloss", type=float, default=0.6)
    p.add_argument("--wmin", type=float, default=0.1)
    p.add_argument("--wmax", type=float, default=1.6)
    p.add_argument("--nw", type=int, default=24)
    p.add_argument("--out", type=str,
                   default=os.path.join(os.path.dirname(__file__), "..", "outputs"))
    args = p.parse_args()

    load_a = 500
    omegas = np.linspace(args.wmin, args.wmax, args.nw)
    print(f"chain {args.length}, loaded {args.nload} cells at [{load_a}], "
          f"omega {args.wmin}..{args.wmax} ({args.nw} pts)")

    dl_lossy, tr_lossy = sweep("lossy", args.aloss, omegas, args.length,
                               args.nload, load_a)
    report(f"LOSSY edge (leaky integrator, a={args.aloss})",
           omegas, dl_lossy, tr_lossy)

    dl_ll, tr_ll = sweep("lossless", args.closs, omegas, args.length,
                         args.nload, load_a)
    report(f"LOSSLESS edge (reduced speed c={args.closs})",
           omegas, dl_ll, tr_ll)

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        outdir = os.path.abspath(args.out)
        os.makedirs(outdir, exist_ok=True)
        fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
        ax[0].plot(omegas, dl_lossy, 'o-', ms=4, label=f"lossy a={args.aloss}")
        ax[0].plot(omegas, dl_ll, 's-', ms=4, label=f"lossless c={args.closs}")
        ax[0].set_xlabel("omega"); ax[0].set_ylabel("group delay (ticks)")
        ax[0].set_title("Group delay vs frequency (flat = non-dispersive)")
        ax[0].legend()
        ax[1].plot(omegas, tr_lossy, 'o-', ms=4, label="lossy")
        ax[1].plot(omegas, tr_ll, 's-', ms=4, label="lossless")
        ax[1].axhline(0.7, color='gray', ls='--', lw=0.8)
        ax[1].set_xlabel("omega"); ax[1].set_ylabel("transmission")
        ax[1].set_title("Transmission (loss = dispersion)")
        ax[1].legend()
        fig.tight_layout()
        png = os.path.join(outdir, "gate_dispersion.png")
        fig.savefig(png, dpi=110)
        print(f"\nsaved {png}")
    except Exception as e:
        print(f"(plot skipped: {e})")


if __name__ == "__main__":
    main()
