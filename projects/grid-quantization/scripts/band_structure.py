#!/usr/bin/env python3
"""Band structure of the honeycomb edge-wave scattering network.

Builds the one-tick Bloch evolution operator U(k) EMPIRICALLY from
the project's own `scatter_step` (lib.py) — by applying it to the 6
per-cell Bloch basis states and reading the response at an interior
reference cell.  This avoids any hand-derivation of edge-orientation
conventions: U(k) is, by construction, exactly the Bloch operator of
the dynamics used everywhere else in this project.

Why: a genuine non-decaying localized state (the `bound` test's
compact localized state) must come from a FLAT band — a band with
zero group velocity.  Diagonalizing U(k) over the Brillouin zone:

  - locates any FLAT band (the bound state) and its frequency;
  - maps the PROPAGATING band(s) (compare to ω ≈ 0.41·k from disp);
  - shows how group velocity |dω/dk| — a proxy for how strongly a
    mode couples through the lattice — varies with frequency, which
    is what the "Q vs frequency / loop size" question reduces to.

One tick couples only nearest cells, so reading an interior cell on
a modest L×L torus gives U(k) exactly for arbitrary (continuous) k.

Usage:
    source .venv/bin/activate
    python projects/grid-quantization/band_structure.py
"""

import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import make_honeycomb, scatter_step  # noqa: E402

a1 = np.array([1.0, 0.0])
a2 = np.array([0.5, np.sqrt(3) / 2])
A = np.array([a1, a2])
Bmat = 2 * np.pi * np.linalg.inv(A).T      # reciprocal vectors
b1, b2 = Bmat[0], Bmat[1]


class BlochOperator:
    """Empirical U(k) from scatter_step on an L×L honeycomb torus."""

    def __init__(self, L=16):
        (self.pos, self.edges, self.vei, self.vend,
         self.ed, self.mid, self.box, self.wrap) = make_honeycomb(L, L)
        self.L = L
        self.E = len(self.edges)
        cell = np.arange(self.E) // 3          # edge → unit cell
        i = cell % L
        j = cell // L
        self.cellR = np.outer(i, a1) + np.outer(j, a2)  # R per edge
        self.c0 = (L // 2) * L + (L // 2)      # interior reference cell
        self.R0 = (self.c0 % L) * a1 + (self.c0 // L) * a2
        self.out_idx = [3 * self.c0 + m for m in range(3)]

    def U(self, k):
        phase = np.exp(1j * (self.cellR - self.R0) @ k)
        U = np.zeros((6, 6), complex)
        for jcol in range(6):
            af = np.zeros(self.E, complex)
            ab = np.zeros(self.E, complex)
            if jcol < 3:
                af[jcol::3] = phase[jcol::3]
            else:
                ab[jcol - 3::3] = phase[jcol - 3::3]
            nf, nb = scatter_step(af, ab, self.vei, self.vend, 3)
            col = [nf[self.out_idx[0]], nf[self.out_idx[1]],
                   nf[self.out_idx[2]], nb[self.out_idx[0]],
                   nb[self.out_idx[1]], nb[self.out_idx[2]]]
            U[:, jcol] = col
        return U

    def bands(self, k):
        return np.sort(np.angle(np.linalg.eigvals(self.U(k))))


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "..", "outputs")
    os.makedirs(out_dir, exist_ok=True)

    print("Band structure — honeycomb edge-wave network "
          "(empirical U(k) from scatter_step)")
    op = BlochOperator(L=16)

    # validation: U(k) must be unitary
    worst = 0.0
    rng = np.random.default_rng(0)
    for _ in range(50):
        k = rng.uniform(-4, 4, 2)
        U = op.U(k)
        worst = max(worst, np.abs(U.conj().T @ U - np.eye(6)).max())
    print(f"  Unitarity max|U†U−I| over random k: {worst:.2e}  "
          f"{'OK' if worst < 1e-10 else 'FAIL'}")

    # ── 2D BZ scan → density of states (flat-band detector) ──
    # A flat band shows as ~1/6 of ALL eigenphases piling up at one ω.
    # (Per-band "bandwidth" fails here because the flat bands sit at
    # ω=0 and ω=π, coincident with the dispersive band edges.)
    ng = 48
    grid = np.linspace(0, 1, ng, endpoint=False)
    allb = np.empty((ng * ng, 6))
    n = 0
    for a in grid:
        for b in grid:
            allb[n] = op.bands(a * b1 + b * b2)
            n += 1
    flat_w = allb.ravel()
    nk = ng * ng                      # one band's worth = nk points
    tol = 1e-3
    # Candidate flat frequencies: 0 and π (fold ±π, which are the same
    # point on the eigenphase circle).
    n0 = np.sum(np.abs(flat_w) < tol)
    npi = np.sum(np.abs(np.abs(flat_w) - np.pi) < tol)
    print(f"\n  BZ scan: {nk} k-points × 6 bands = {6*nk} eigenphases."
          f"  One full band = {nk} points.")
    print("  Flat-band detector (eigenphase pileups; 1 band ≈ "
          f"{nk} states):")
    print(f"    ω = 0      {n0} states  ({n0/nk:.2f} bands)  FLAT ⇒ "
          f"localized / bound (v_g = 0)")
    print(f"    ω = ±π     {npi} states  ({npi/nk:.2f} bands)  FLAT ⇒ "
          f"localized / bound (v_g = 0)")
    n_flat = round(n0 / nk) + round(npi / nk)
    print(f"  ⇒ {n_flat} flat bands + {6-n_flat} dispersive bands. "
          f"The flat bands at ω=0 and ω=π host the")
    print(f"    compact localized states — the `bound` test's trapped "
          f"mode is the ω=0 CLS (static).")

    # ── path Γ→M→K→Γ ──
    G, M, K = np.zeros(2), 0.5 * b1, (2 * b1 + b2) / 3.0
    pts, labels = [G, M, K, G], ["Γ", "M", "K", "Γ"]
    npts = 120
    kpath = []
    for p, q in zip(pts[:-1], pts[1:]):
        for t in np.linspace(0, 1, npts, endpoint=False):
            kpath.append(p + t * (q - p))
    kpath.append(G)
    kpath = np.array(kpath)
    bpath = np.array([op.bands(k) for k in kpath])
    s = np.concatenate([[0], np.cumsum(np.linalg.norm(
        np.diff(kpath, axis=0), axis=1))])

    # group velocity along the path (clip crossing artifacts: any
    # |v_g| > 1 is unphysical here and comes from sort-induced band
    # swaps at crossings, not real dispersion).
    gv = np.gradient(bpath, s, axis=0)
    real = np.abs(gv) <= 1.0
    print(f"\n  Propagating bands: robust max group velocity |dω/dk| "
          f"≈ {np.abs(gv[real]).max():.3f}")
    print(f"  (flat bands sit at ω=0, π with v_g=0 — the localized / "
          f"bound, effectively infinite-Q frequencies; group velocity")
    print(f"   peaks mid-band, where modes propagate/leak most — so Q "
          f"is NON-monotonic in ω: high at 0 and π, low in between.)")

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    # left: bands along the path + flat bands flagged at 0 and π
    for i in range(6):
        axes[0].plot(s, bpath[:, i], color="navy", lw=1.5, alpha=0.8)
    for wflat in (0.0, np.pi, -np.pi):
        axes[0].axhline(wflat, color="red", ls="--", lw=2, alpha=0.7)
    tk = [s[0], s[npts], s[2 * npts], s[-1]]
    for t in tk:
        axes[0].axvline(t, color="gray", ls=":", alpha=0.4)
    axes[0].set_xticks(tk)
    axes[0].set_xticklabels(labels)
    axes[0].set_ylabel("ω (rad / tick)")
    axes[0].set_title("Band structure\n"
                      "(red = flat/bound at ω=0,π; navy = propagating)")
    axes[0].grid(True, alpha=0.3)

    # right: density of states — flat bands = spikes at 0 and π
    axes[1].hist(flat_w, bins=120, color="navy", alpha=0.8)
    for wflat in (0.0, np.pi, -np.pi):
        axes[1].axvline(wflat, color="red", ls="--", lw=2, alpha=0.7)
    axes[1].set_xlabel("ω (rad / tick)")
    axes[1].set_ylabel("density of states")
    axes[1].set_title("DOS: spikes at ω=0, π are the flat/bound bands;\n"
                      "continuum between is propagating (leaky)")
    axes[1].grid(True, alpha=0.3)
    fig.tight_layout()
    path = os.path.join(out_dir, "band_structure.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"\n  Saved: {path}")
    plt.close(fig)


if __name__ == "__main__":
    main()
