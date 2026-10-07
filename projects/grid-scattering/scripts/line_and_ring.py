"""
Saturation/overflow as the means by which energy crosses a sheet boundary.

Topology (README §3), corrected after the first run:

    x is ONE linear array of nodes, 2 registers each (+x, -x).
    At every x coordinate there is a RING --- its own array of nc nodes,
    2 registers each (+c, -c).
    The line and a ring are NOT connected. They connect only during an
    overflow, at one point: ring node 0, the junction.

This is not a product grid. An (nx x nc) lattice would be nc parallel x-lines,
and a photon spread across them saturates every ring at once --- which injects
uniformly around each ring, gives winding 0 and makes no particle. That was the
first run's negative result; this topology is the fix.

Dynamics. Below the ceiling each array is a pass-through delay line: out[d] =
in[d], and propagation moves things along. The line and the rings are isolated.

Overflow. Each node has two degrees of freedom. If |T| = |in[+] + in[-]| at an
x node exceeds --sat, the excess is removed from that node's x outputs (half
each) and injected into that coordinate's ring at the junction, half into +c and
half into -c --- so it leaves in both directions at once and meets itself on the
far side. The reverse runs at the junction too: if the ring's junction node
saturates, the excess goes back into the line.

Resonance. A ring of nc nodes has a round-trip time of nc ticks at one node per
tick. A drive of angular frequency w has period 2*pi/w ticks, i.e. a wavelength
of the same number of nodes. Repeated overflow should add in phase when the
round trip is a whole number of drive periods --- nc = m * lambda --- and that
is the fit condition this script is built to test.

Conservation is MEASURED, not engineered: amplitude is moved, energy goes as
amplitude squared, so the books will not balance. The drift is reported.
"""
import argparse
import os
import numpy as np


def step(xin, rin, sat, one_way=False):
    """One tick. xin (2, nx); rin (2, nx, nc). Pass-through + overflow coupling."""
    xout, rout = xin.copy(), rin.copy()

    Tx = xin[0] + xin[1]                       # x-node totals
    ex = np.sign(Tx) * np.maximum(np.abs(Tx) - sat, 0.0)
    xout[0] -= ex / 2; xout[1] -= ex / 2
    # Amplitude bookkeeping: the excess e leaves x and arrives split e/2 each
    # way around the ring. This is NOT energy-conserving -- two registers at e/2
    # carry e^2/2 where the removed amplitude e would carry e^2 -- and the sign
    # of the loss is fixed, so the drift is a known bias rather than a
    # measurement. Splitting e/sqrt(2) each way overshoots instead: it injects
    # more amplitude than was removed and runs away once the reverse channel
    # opens (tested: nc=12 reaches 1e16). Exact conservation needs either
    # explicit energy accounting (a square root, foreign to an amplitude
    # substrate) or a rotation. Left as-is and reported; see work/STATUS.md.
    rout[0, :, 0] += ex / 2
    rout[1, :, 0] += ex / 2

    nback = 0
    if not one_way:
        Tc = rin[0, :, 0] + rin[1, :, 0]       # junction-node totals
        ec = np.sign(Tc) * np.maximum(np.abs(Tc) - sat, 0.0)
        rout[0, :, 0] -= ec / 2; rout[1, :, 0] -= ec / 2
        xout[0] += ec / 2; xout[1] += ec / 2   # back into the line
        nback = int((ec != 0).sum())

    nx_ = np.zeros_like(xout); nr = np.zeros_like(rout)
    nx_[0, 1:] = xout[0, :-1]; nx_[1, :-1] = xout[1, 1:]        # x propagation
    nr[0] = np.roll(rout[0], 1, axis=1)                          # around the ring
    nr[1] = np.roll(rout[1], -1, axis=1)
    return nx_, nr, int((ex != 0).sum()), nback


def run(a):
    rng = np.random.default_rng(a.seed)
    xin = np.zeros((2, a.nx)); rin = np.zeros((2, a.nx, a.nc))
    m = 20
    ramp = np.linspace(0, 0.10, m)
    sx = np.ones(a.nx); sx[:m] = 1 - ramp[::-1]; sx[-m:] = 1 - ramp

    t0, wt, mid = 60.0, a.width, a.nx // 2
    peakT, fwd, back, ring_hist = 0.0, 0, 0, []
    for t in range(a.steps):
        xin, rin, f, b = step(xin, rin, a.sat if a.sat > 0 else np.inf, a.one_way)
        fwd += f; back += b
        env = (a.amp * min(1.0, t / 80.0) if a.cw
               else np.exp(-((t - t0) / wt) ** 2) * a.amp)
        if env > 1e-6 and not a.no_drive:
            xin[0, a.pad] += env * np.cos(a.omega * (t - t0))
            xin[1, a.nx - 1 - a.pad] += env * np.cos(a.omega * (t - t0))
        if a.zpe:
            xin += a.zpe * rng.standard_normal(xin.shape)
        xin *= sx[None, :]
        peakT = max(peakT, float(np.abs(xin[0] + xin[1]).max()))
        ring_hist.append(float((rin[:, mid, :] ** 2).sum()))
    return xin, rin, peakT, fwd, back, np.array(ring_hist)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nx", type=int, default=201, help="length of the x line (nodes)")
    p.add_argument("--nc", type=int, default=24, help="ring circumference (nodes)")
    p.add_argument("--steps", type=int, default=600)
    p.add_argument("--sat", type=float, default=0.8, help="ceiling on |T|; 0 disables")
    p.add_argument("--amp", type=float, default=0.5)
    p.add_argument("--omega", type=float, default=0.5236,
                   help="drive frequency; wavelength = 2*pi/omega nodes")
    p.add_argument("--width", type=float, default=14.0)
    p.add_argument("--zpe", type=float, default=0.0, help="jitter on the x line per tick")
    p.add_argument("--one-way", action="store_true", help="disable the ring->line channel")
    p.add_argument("--cw", action="store_true",
                   help="sustained periodic drive instead of a single pulse; "
                        "required for resonant build-up (a pulse injects once)")
    p.add_argument("--no-drive", action="store_true")
    p.add_argument("--pad", type=int, default=30)
    p.add_argument("--seed", type=int, default=1)
    a = p.parse_args()

    xin, rin, peakT, fwd, back, hist = run(a)
    mid = a.nx // 2
    lam = 2 * np.pi / a.omega
    fld = rin[0, mid] + rin[1, mid]
    P = np.abs(np.fft.fft(fld)) ** 2
    Ering = float((rin[:, mid, :] ** 2).sum())
    Eline = float((xin ** 2).sum())
    Etot = Ering_all = float((rin ** 2).sum()) + Eline
    print(f"nc={a.nc}  lambda={lam:.2f}  nc/lambda={a.nc / lam:.3f}  sat={a.sat}")
    print(f"  peak |T_x| {peakT:.4f} vs ceiling {a.sat}"
          + ("   <-- NEVER REACHED" if a.sat > 0 and peakT < a.sat else ""))
    print(f"  overflow events: line->ring {fwd}, ring->line {back}")
    print(f"  ring energy at the collision node: peak {hist.max():.4e}, final {Ering:.4e}")
    print(f"  line energy remaining {Eline:.4e}   total (line+all rings) {Etot:.4e}")
    if P[1:].sum() > 0:
        top = np.argsort(P[1:a.nc // 2 + 1])[::-1][:3] + 1
        print(f"  winding n=0 {P[0]:.3e}   n!=0 {P[1:].sum():.3e}   "
              + "modes: " + ", ".join(f"n={int(n)} ({P[int(n)]:.2e})" for n in top))


if __name__ == "__main__":
    main()
