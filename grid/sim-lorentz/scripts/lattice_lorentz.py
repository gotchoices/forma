#!/usr/bin/env python3
"""Lorentz-property tests for the GRID lattice.

Purpose
-------
Axiom A2 of grid/foundations.md *asserts* a Lorentzian signature.  This
script measures whether the lattice dynamics actually deliver the
observable consequences, rather than taking them as given.  Scope is
deliberately narrow: only properties that grid/ already assumes.

The specification being tested (derived in
primers/relativity-on-a-lattice.md):
  1. one wave speed, every direction          -> --isotropy
  2. rest mass invariant under boost          -> --boost
  3. length contraction by 1/gamma            -> --contraction
  4. coasting without radiating               -> --contraction (reported)

Inputs  : all via argparse; no hard-coded physics values.
Outputs : tables on stdout; ASCII energy profiles for --contraction
          (rms/second-moment width statistics are NOT used alone --
          they misread a split pulse as one broad one).

Modes
-----
--isotropy    Exact 6x6 Bloch operator for the GRID impedance scatter
              S = (2/N)J - I on a true honeycomb lattice.  Reports wave
              speed vs. propagation direction at several wavelengths.

--boost       Kaluza-Klein cylinder dispersion.  A mode winding the
              compact direction has a rest frequency w0; boosting it
              along x should leave w^2 - c^2 kx^2 constant.  Reports the
              drift, which is the Lorentz violation.
              NOTE: relativistic velocity addition is NOT an independent
              test for a free particle -- additivity of rapidity is
              algebraically equivalent to constancy of w^2 - c^2 k^2, so
              --boost already covers it.

--contraction Discrete sine-Gordon chain (grid-matter's reduction of the
              compact-phase sector: phi_tt = phi_xx - m^2 sin phi).  Seeds
              the exact continuum breather Lorentz-boosted to velocity v,
              evolves it, and measures the envelope width, the realised
              speed, and the energy drift.  A Lorentzian lattice should
              give width = width(v=0)/gamma, speed = v, and zero drift.
"""
import argparse
import numpy as np

# ----------------------------------------------------------------- honeycomb

A1 = np.array([1.0, 0.0])
A2 = np.array([0.5, np.sqrt(3) / 2])
DELTA = [np.zeros(2), -A1, -A2]   # A-cell -> B-cell offset, per edge type


def onetick(k):
    """6x6 one-tick operator at Bloch wavevector k.  Order a0,a1,a2,b0,b1,b2."""
    s3 = (2.0 / 3.0) * np.ones((3, 3)) - np.eye(3)
    m = np.zeros((6, 6), dtype=complex)
    for i in range(3):
        ph = np.exp(-1j * np.dot(k, DELTA[i]))
        for j in range(3):
            m[3 + i, j] = s3[i, j] * ph
            m[i, 3 + j] = s3[i, j] * np.conj(ph)
    return m


def omega_hex(k):
    """Lowest propagating branch frequency (radians per tick)."""
    w = np.abs(np.angle(np.linalg.eigvals(onetick(k))))
    w = np.sort(w[(w > 1e-9) & (w < np.pi - 1e-9)])
    return 0.0 if len(w) == 0 else w[0]


def run_isotropy(a):
    print("Wave speed vs. propagation direction on the honeycomb")
    print("(speed in cells per tick; anisotropy = (max-min)/mean)\n")
    print(f"{'|k|':>8} {'lambda/cells':>13} {'min speed':>11} "
          f"{'max speed':>11} {'anisotropy':>12}")
    for kmag in a.kmags:
        th = np.linspace(0.0, np.pi / 3.0, a.ndir)       # one symmetry wedge
        sp = np.array([omega_hex(kmag * np.array([np.cos(t), np.sin(t)])) / kmag
                       for t in th])
        aniso = (sp.max() - sp.min()) / sp.mean()
        print(f"{kmag:8.3f} {2*np.pi/kmag:13.1f} {sp.min():11.8f} "
              f"{sp.max():11.8f} {aniso:12.3e}")
    c = omega_hex(np.array([1e-4, 0.0])) / 1e-4
    print(f"\nlong-wavelength speed c = {c:.8f}   (1/sqrt(6) = "
          f"{1/np.sqrt(6):.8f}, diff {abs(c-1/np.sqrt(6)):.2e})")


# ------------------------------------------------------- KK cylinder dispersion

def run_boost(a):
    """w^2 - c^2 kx^2 should be constant along a boost.  Drift = violation."""
    c = omega_hex(np.array([1e-4, 0.0])) / 1e-4
    print(f"Rest-mass invariance under boost   (lattice c = {c:.8f})")
    print("w^2 - c^2 kx^2 should not change with kx.\n")
    for kc in a.kcs:
        w0 = omega_hex(np.array([0.0, kc]))
        print(f"  compact momentum kc = {kc}   rest frequency w0 = {w0:.6f}")
        print(f"  {'kx':>6} {'omega':>10} {'w^2-c^2kx^2':>14} {'drift':>10}")
        ref = None
        for kx in a.kxs:
            w = omega_hex(np.array([kx, kc]))
            inv = w * w - c * c * kx * kx
            if ref is None:
                ref = inv
            print(f"  {kx:6.2f} {w:10.6f} {inv:14.8f} "
                  f"{100*(inv-ref)/abs(ref):+9.3f}%")
        print()


# ------------------------------------------------- discrete sine-Gordon chain

def breather(x, t, m, om, v):
    """Exact continuum sine-Gordon breather, Lorentz-boosted to velocity v.

    Solves phi_tt - phi_xx + m^2 sin(phi) = 0.  0 < om < 1 sets how deeply
    bound the breather is; its rest envelope width is ~1/(m*sqrt(1-om^2)).
    """
    g = 1.0 / np.sqrt(1.0 - v * v)
    u = m * g * (x - v * t)          # boosted space, in units of 1/m
    s = m * g * (t - v * x)          # boosted time,  in units of 1/m
    r = np.sqrt(1.0 - om * om)
    return 4.0 * np.arctan((r / om) * np.sin(om * s) / np.cosh(r * u))


def energy_density(phi, pdot, m, h):
    grad = (np.roll(phi, -1) - phi) / h
    return 0.5 * pdot**2 + 0.5 * grad**2 + m * m * (1.0 - np.cos(phi))


def fwhm(prof, h):
    """Full width at half maximum, interpolated to sub-cell resolution.

    Counting cells above half-max quantises the width to +-1 cell, which
    is +-3% on a 30-cell envelope -- coarser than the effect being
    measured.  Linear interpolation of the two half-max crossings removes
    that floor.
    """
    pk = prof.max()
    if pk <= 0:
        return 0.0
    half = 0.5 * pk
    i = int(np.argmax(prof))
    above = np.where(prof >= half)[0]
    lo, hi = above.min(), above.max()
    # left crossing between lo-1 and lo; right between hi and hi+1
    if lo > 0:
        p0, p1 = prof[lo - 1], prof[lo]
        xl = (lo - 1) + (half - p0) / (p1 - p0) if p1 != p0 else float(lo)
    else:
        xl = float(lo)
    if hi < len(prof) - 1:
        p0, p1 = prof[hi], prof[hi + 1]
        xr = hi + (p0 - half) / (p0 - p1) if p0 != p1 else float(hi)
    else:
        xr = float(hi)
    return (xr - xl) * h


def ascii_profile(prof, centre, half=60, rows=9):
    """Print the energy profile around `centre` so the shape is visible."""
    n = len(prof)
    idx = (np.arange(centre - half, centre + half) % n).astype(int)
    seg = prof[idx]
    top = seg.max() if seg.max() > 0 else 1.0
    for r in range(rows, 0, -1):
        lvl = top * r / rows
        print("   |" + "".join("#" if s >= lvl else " " for s in seg))
    print("   +" + "-" * len(seg))


def run_contraction(a):
    h, dt, m, om = a.h, a.dt, a.m, a.omega
    x = (np.arange(a.nx) - a.nx // 2) * h
    rest_w = 1.0 / (m * np.sqrt(1.0 - om * om))
    print("Length contraction of a bound state under boost")
    print(f"chain nx={a.nx} h={h} dt={dt}   m={m} omega={om}")
    print(f"continuum rest envelope width ~ {rest_w:.2f} lattice units\n")
    print(f"{'v':>6} {'gamma':>7} {'width':>9} {'w(0)/gam':>9} {'w err':>8} "
          f"{'speed':>8} {'v err':>8} {'dE/E':>10}")

    widths = {}
    for v in a.vs:
        g = 1.0 / np.sqrt(1.0 - v * v)
        # seed from the exact boosted solution at two times -> Verlet start
        prev = breather(x, -dt, m, om, v)
        cur = breather(x, 0.0, m, om, v)

        lab_period = 2.0 * np.pi / (om * m) * g      # breather period in lab time
        nsteps = int(a.periods * lab_period / dt)
        navg = max(1, int(lab_period / dt))          # average over one period

        e0 = None
        acc = np.zeros(a.nx)
        nacc = 0
        cen_t, cen_x = [], []
        for n in range(nsteps):
            lap = (np.roll(cur, -1) - 2.0 * cur + np.roll(cur, 1)) / (h * h)
            nxt = 2.0 * cur - prev + dt * dt * (lap - m * m * np.sin(cur))
            prev, cur = cur, nxt
            if n % a.sample == 0:
                pdot = (cur - prev) / dt
                ed = energy_density(cur, pdot, m, h)
                tot = ed.sum() * h
                if e0 is None:
                    e0 = tot
                # centroid by circular mean (box is periodic)
                ang = 2 * np.pi * np.arange(a.nx) / a.nx
                cx = np.angle((ed * np.exp(1j * ang)).sum()) / (2 * np.pi) * a.nx
                cen_t.append(n * dt)
                cen_x.append(cx % a.nx)
                if n >= nsteps - navg:               # last period -> envelope
                    sh = int(round(cx % a.nx))
                    acc += np.roll(ed, -sh + a.nx // 2)
                    nacc += 1
        pdot = (cur - prev) / dt
        efin = (energy_density(cur, pdot, m, h).sum() * h)
        env = acc / max(nacc, 1)
        w = fwhm(env, h)
        widths[v] = w
        # unwrap the centroid track and fit a line for the realised speed
        ct = np.array(cen_t); cx = np.array(cen_x)
        d = np.diff(cx); d -= a.nx * np.round(d / a.nx)
        cxu = np.concatenate([[cx[0]], cx[0] + np.cumsum(d)])
        speed = np.polyfit(ct, cxu, 1)[0] * h
        pred = widths[a.vs[0]] / g if a.vs[0] == 0.0 else float("nan")
        werr = 100 * (w - pred) / pred if pred == pred and pred > 0 else float("nan")
        print(f"{v:6.2f} {g:7.4f} {w:9.2f} {pred:9.2f} {werr:+7.1f}% "
              f"{speed:8.4f} {100*(speed-v)/v if v else 0:+7.1f}% "
              f"{100*(efin-e0)/e0:+9.3f}%")
        if a.profiles:
            print(f"   envelope at v={v}:")
            ascii_profile(env, a.nx // 2, half=a.half)


# ------------------------------------------------------------------------ cli

def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--isotropy", action="store_true")
    p.add_argument("--boost", action="store_true")
    p.add_argument("--contraction", action="store_true")
    p.add_argument("--kmags", type=float, nargs="+",
                   default=[0.02, 0.2, 1.0, 2.0])
    p.add_argument("--ndir", type=int, default=61)
    p.add_argument("--kcs", type=float, nargs="+", default=[0.05, 0.5])
    p.add_argument("--kxs", type=float, nargs="+",
                   default=[0.0, 0.05, 0.1, 0.2, 0.4, 0.8])
    p.add_argument("--nx", type=int, default=8000)
    p.add_argument("--h", type=float, default=1.0)
    p.add_argument("--dt", type=float, default=0.05)
    p.add_argument("--m", type=float, default=0.05)
    p.add_argument("--omega", type=float, default=0.7)
    p.add_argument("--vs", type=float, nargs="+",
                   default=[0.0, 0.3, 0.6, 0.8, 0.9])
    p.add_argument("--periods", type=float, default=6.0)
    p.add_argument("--sample", type=int, default=5)
    p.add_argument("--profiles", action="store_true")
    p.add_argument("--half", type=int, default=60)
    a = p.parse_args()
    if a.isotropy:
        run_isotropy(a)
    if a.boost:
        run_boost(a)
    if a.contraction:
        run_contraction(a)
    if not (a.isotropy or a.boost or a.contraction):
        p.print_help()


if __name__ == "__main__":
    main()
