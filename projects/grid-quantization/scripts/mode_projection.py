#!/usr/bin/env python3
"""How much of an excitation projects onto the bound (flat-band) sector?

Built to answer a specific question: is the ~50% energy a hexagon
circulation traps the zero-point ½?  Answer (see below): no — the
precise figure is ~0.57, it is excitation-dependent (a random state
hits the flat-band dimension fraction 1/3), and the ZPE ½ comes from
a different mechanism (a spectral average, a vacuum quantity).  What
*is* meaningful is that a circulating (photon-like) excitation
couples to the bound sector ~1.7× more than a random one.

Method: diagonalize the exact one-tick real-space evolution operator
on a small honeycomb torus, take the bound subspace as the
eigenvectors with eigenvalue ±1 (the ω=0 and ω=π flat bands), and
project each test excitation onto it.  Exact — no dynamics, no
wraparound.

Usage:
    source .venv/bin/activate
    python projects/grid-quantization/mode_projection.py
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import make_honeycomb, scatter_step           # noqa: E402
from run_recirculation import find_plaquettes, face_centroid  # noqa: E402


def build_operator(vei, vend, E):
    """Exact one-tick evolution matrix on the 2E half-edge space."""
    dim = 2 * E
    M = np.zeros((dim, dim))
    for c in range(dim):
        af = np.zeros(E)
        ab = np.zeros(E)
        if c < E:
            af[c] = 1.0
        else:
            ab[c - E] = 1.0
        nf, nb = scatter_step(af, ab, vei, vend, 3)
        M[:E, c] = nf
        M[E:, c] = nb
    return M


def main():
    L = 12
    pos, edges, vei, vend, ed, mid, box, wrap = make_honeycomb(L, L)
    E = len(edges)
    dim = 2 * E

    M = build_operator(vei, vend, E)
    lam, Vec = np.linalg.eig(M)                  # unitary ⇒ orthonormal
    bound = (np.abs(lam - 1) < 1e-6) | (np.abs(lam + 1) < 1e-6)
    Q, _ = np.linalg.qr(Vec[:, bound])           # orthonormal basis

    print("Mode projection onto the bound (flat-band) subspace")
    print(f"  lattice {L}×{L}, half-edge space dim {dim}")
    print(f"  bound subspace dim {bound.sum()} (≈ 2·L² = {2*L*L}); "
          f"fraction of full space = {bound.sum()/dim:.4f} (≈ 1/3)\n")

    def trapped(psi):
        psi = psi / np.linalg.norm(psi)
        p = Q.conj().T @ psi
        return float(np.real(np.vdot(p, p)))

    faces = find_plaquettes(edges, vei, vend, ed)
    cents = np.array([face_centroid(f, edges, pos) for f in faces])
    tf = faces[int(np.argmin(((cents - box / 2) ** 2).sum(axis=1)))]

    # circulation excitation on a hexagon
    psi = np.zeros(dim)
    for ei, side in tf:
        psi[ei if side == 0 else E + ei] = 1.0
    f_circ = trapped(psi)

    # random baseline (should hit the subspace dimension fraction)
    rng = np.random.default_rng(1)
    f_rand = np.mean([trapped(rng.standard_normal(dim)
                              + 1j * rng.standard_normal(dim))
                      for _ in range(50)])

    # single edge
    psi = np.zeros(dim)
    psi[tf[0][0] if tf[0][1] == 0 else E + tf[0][0]] = 1.0
    f_edge = trapped(psi)

    # the bound standing pattern (sanity: should be ~1)
    psi = np.zeros(dim)
    patt = [1, 1, -1, -1, -1, 1]
    for n, (ei, side) in enumerate(tf):
        psi[ei] = patt[n]
        psi[E + ei] = -patt[n]
    f_patt = trapped(psi)

    print(f"  {'excitation':<32s}{'trapped fraction':>16s}")
    print(f"  {'random state':<32s}{f_rand:>16.4f}")
    print(f"  {'single edge':<32s}{f_edge:>16.4f}")
    print(f"  {'hexagon circulation':<32s}{f_circ:>16.4f}")
    print(f"  {'bound pattern [+,+,-,-,-,+]':<32s}{f_patt:>16.4f}")
    print(f"\n  Circulation couples to the bound sector "
          f"{f_circ/f_rand:.2f}× more than random.")
    print(f"  It is NOT the zero-point ½: the value is ~{f_circ:.2f} "
          f"(not 0.5), is excitation-dependent, and the ZPE ½ is a")
    print(f"  spectral-average vacuum quantity (zpe_derivation.md), a "
          f"different object.")


if __name__ == "__main__":
    main()
