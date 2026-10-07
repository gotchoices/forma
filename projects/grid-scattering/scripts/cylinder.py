"""
Saturation/overflow as the means by which energy crosses a sheet boundary.

ARENA — a cylinder (README §3). One extended direction x and one compact
direction c, as a product lattice: every node has four registers (+x, -x, +c,
-c) and sits on both the x line through it and the c ring through it. Rings at
neighbouring x are therefore connected along x, which is what lets anything
made on a ring afterwards move.

This replaces an earlier "comb" arena --- one x line with a ring hung off each
x position at a fixed point --- which was wrong twice: it gave every ring a
privileged attachment point, breaking translation symmetry along c (the
symmetry whose conserved quantity is the winding), and it left ring nodes with
no x edges at all, so nothing made there could ever travel.

SCATTER — the x pair and the c pair are separate groups. Below the ceiling they
exchange nothing, and within a group a 1D line has no junction to scatter at,
so the rule is pass-through: out[d] = in[d], propagation does the moving.
--theta adds a weak always-on exchange between the groups (an exact rotation,
so unitary at any angle); theta = 0 is the ideal node, small theta the leaky
one. Only unitarity is a per-node constraint --- the lattice is fixed and can
absorb momentum, so per-node momentum conservation is not required.

OVERFLOW — where a node's x-group total |T| exceeds --sat, the excess is moved
into that node's c-group by a ROTATION, which is exactly energy-conserving and
accounts for whatever the ring already holds. Adding amplitude instead destroys
energy through the cross term with existing content, worst when out of phase,
which corrupted an earlier set of measurements.

--one-point: at each x only the single c-position with the largest |T| may
overflow. A photon is uniform around c, so without this every c-position
saturates together and injects uniformly --- winding 0, no particle. The tie is
broken by the background (--zpe), so the symmetry is broken by the STATE, never
by the rule.

Reports the energy drift, which should be at machine level.
"""
import argparse
import os
import numpy as np


def propagate(f):
    o = np.empty_like(f)
    o[0] = np.roll(f[0], 1, axis=0)          # +x
    o[1] = np.roll(f[1], -1, axis=0)         # -x
    o[2] = np.roll(f[2], 1, axis=1)          # +c
    o[3] = np.roll(f[3], -1, axis=1)         # -c
    return o


def rotate_groups(f, ang):
    """Exact rotation of (x,c) register pairs by `ang` (array over nodes)."""
    c, s = np.cos(ang), np.sin(ang)
    o = f.copy()
    o[0] = c * f[0] - s * f[2]; o[2] = s * f[0] + c * f[2]
    o[1] = c * f[1] - s * f[3]; o[3] = s * f[1] + c * f[3]
    return o


def step(f, sat, gain, theta, one_point):
    o = f.copy()
    if theta:
        o = rotate_groups(o, np.full(o.shape[1:], theta))
    nfire = 0
    if sat > 0:
        T = np.abs(o[0] + o[1])
        over = np.maximum(T - sat, 0.0)
        if one_point:
            keep = np.zeros_like(over, dtype=bool)
            keep[np.arange(over.shape[0]), T.argmax(axis=1)] = True
            over = over * keep
        nfire = int((over > 0).sum())
        if nfire:
            o = rotate_groups(o, gain * over)
    return propagate(o), nfire


def run(a):
    rng = np.random.default_rng(a.seed)
    f = np.zeros((4, a.nx, a.nc))
    m = 20
    ramp = np.linspace(0, 0.10, m)
    sx = np.ones(a.nx); sx[:m] = 1 - ramp[::-1]; sx[-m:] = 1 - ramp

    fired = 0
    for t in range(a.steps):
        f, n = step(f, a.sat, a.gain, a.theta, a.one_point)
        fired += n
        env = (a.amp * min(1.0, t / 80.0) if a.cw
               else a.amp * np.exp(-((t - 60.0) / a.width) ** 2))
        if env > 1e-6 and not a.no_drive:
            f[0, a.pad, :] += env * np.cos(a.omega * t)
            f[1, a.nx - 1 - a.pad, :] += env * np.cos(a.omega * t)
        if a.zpe:
            f[:2] += a.zpe * rng.standard_normal(f[:2].shape)
        f *= sx[None, :, None]
    return f, fired


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nx", type=int, default=201)
    p.add_argument("--nc", type=int, default=24)
    p.add_argument("--steps", type=int, default=900)
    p.add_argument("--sat", type=float, default=0.8, help="ceiling on a group's |T|; 0 disables")
    p.add_argument("--gain", type=float, default=0.5, help="radians of rotation per unit of excess")
    p.add_argument("--theta", type=float, default=0.0, help="weak always-on x<->c exchange (radians/tick)")
    p.add_argument("--one-point", action="store_true", default=True)
    p.add_argument("--all-points", dest="one_point", action="store_false")
    p.add_argument("--amp", type=float, default=0.5)
    p.add_argument("--omega", type=float, default=0.2618, help="drive; wavelength = 2*pi/omega nodes")
    p.add_argument("--width", type=float, default=14.0)
    p.add_argument("--cw", action="store_true")
    p.add_argument("--zpe", type=float, default=1e-3, help="background on the x group only")
    p.add_argument("--no-drive", action="store_true")
    p.add_argument("--pad", type=int, default=30)
    p.add_argument("--seed", type=int, default=1)
    a = p.parse_args()

    # energy audit: drive and sponge are external, so audit step() alone
    rng = np.random.default_rng(99)
    probe = rng.standard_normal((4, 40, a.nc))
    e0 = float((probe ** 2).sum())
    q, _ = step(probe, a.sat, a.gain, a.theta, a.one_point)
    e1 = float((q ** 2).sum())
    print(f"step() energy audit: {e0:.6f} -> {e1:.6f}   drift {abs(e1-e0)/e0:.2e}")

    f, fired = run(a)
    P = np.abs(np.fft.fft(f[2] + f[3], axis=1)) ** 2
    lam = 2 * np.pi / a.omega
    print(f"nc={a.nc}  lambda={lam:.2f}  nc/lambda={a.nc/lam:.3f}  sat={a.sat}  theta={a.theta}")
    print(f"  overflow events {fired}")
    print(f"  compact content   n=0 {P[:,0].sum():.4e}   n!=0 {P[:,1:].sum():.4e}")
    print(f"  total energy {float((f**2).sum()):.4e}")


if __name__ == "__main__":
    main()
