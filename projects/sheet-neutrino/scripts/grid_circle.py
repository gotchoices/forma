"""GRID simulation of the lepton-domain neutrino circle (host G), Stage 1.

What it does
  Builds the circle as a GRID graph and computes its modes exactly:
    - a ring of three segments with l1, l2, l3 edges (the neutrino line);
    - at each of the three junctions, a small closed loop of ell edges
      (the shared electron circle), making the junction a 4-edge node;
    - optionally, one sign-flipping edge per segment (the Klein flip).
  Dynamics is the grid-duality Scattering model: two registers per edge
  (one per direction), and at every node of N edges the scattering
  S = (2/N)·J − I, which is lossless.  A flipped edge negates whatever
  crosses it.  The one-step update is then a fixed real orthogonal matrix,
  and its eigenvalues e^{iω} give the exact mode frequencies.

Outputs, for the three lowest modes (ν1, ν2, ν3; mass ∝ ω):
  - the splitting ratio Δm²31/Δm²21;
  - "fit fractions": the share of each mode's energy on each segment;
  - a mixing matrix: three flavor states, one per segment, chosen as the
    combinations of the three modes most concentrated on their segment
    (maximally localized, as in Wannier functions); |U|² then gives the
    weight of each mode in each flavor.

Modes: --equal (equal segments), --scan (search segment lengths for the
measured ratio), or explicit --lens.

Inputs: command-line options (see --help).  Outputs: printed tables.
"""
import argparse
import itertools

import numpy as np
from scipy.optimize import minimize

MEASURED_U2 = np.array([[0.68, 0.30, 0.02],      # ν_e
                        [0.10, 0.37, 0.53],      # ν_μ  (approximate)
                        [0.22, 0.33, 0.45]])     # ν_τ  (approximate)


def build_graph(lens, ell, flips):
    """Return (tails, heads, signs, region) for the circle graph.

    region[e] = segment index 0..2 for ring edges, 3..5 for loop edges.
    """
    tails, heads, signs, region = [], [], [], []
    n_nodes = 0
    junction = []
    ring_nodes = []
    for s, l in enumerate(lens):                     # ring nodes, segment by segment
        junction.append(n_nodes)
        for i in range(l):
            ring_nodes.append((n_nodes, s))
            n_nodes += 1
    N_ring = n_nodes
    for idx, (node, s) in enumerate(ring_nodes):     # ring edges
        nxt = ring_nodes[(idx + 1) % N_ring][0]
        tails.append(node); heads.append(nxt); region.append(s)
        signs.append(1.0)
    if flips:                                        # one flipped edge mid-segment
        start = 0
        for s, l in enumerate(lens):
            signs[start + l // 2] = -1.0
            start += l
    for s, j in enumerate(junction):                 # small loop at each junction
        prev = j
        for i in range(ell - 1):
            tails.append(prev); heads.append(n_nodes); region.append(3 + s); signs.append(1.0)
            prev = n_nodes
            n_nodes += 1
        tails.append(prev); heads.append(j); region.append(3 + s); signs.append(1.0)
    return np.array(tails), np.array(heads), np.array(signs), np.array(region), n_nodes


def step_matrix(tails, heads, signs, n_nodes):
    """Real orthogonal one-step operator on registers [a_fwd (E); a_bwd (E)].

    a_fwd[e] travels tail→head and arrives at head; a_bwd[e] arrives at tail.
    At node n: out_e = (2/N_n)·Σ in − in_e, sent onto edge e away from n.
    """
    E = len(tails)
    coord = np.bincount(np.concatenate([tails, heads]), minlength=n_nodes)
    arriving = [[] for _ in range(n_nodes)]          # (register index, edge)
    for e in range(E):
        arriving[heads[e]].append((e, e))            # a_fwd[e] arrives at head
        arriving[tails[e]].append((E + e, e))        # a_bwd[e] arrives at tail
    U = np.zeros((2 * E, 2 * E))
    for n in range(n_nodes):
        N = coord[n]
        for (r_in, e_in) in arriving[n]:
            for (r_out_src, e_out) in arriving[n]:
                coef = 2.0 / N - (1.0 if r_in == r_out_src else 0.0)
                # outgoing onto e_out away from n: a_fwd if n is its tail, else a_bwd
                r_out = e_out if tails[e_out] == n else E + e_out
                U[r_out, r_in] += signs[e_out] * coef
    return U


def lowest_modes(U, n_modes, w_min):
    """Positive-frequency eigenpairs with the smallest ω above w_min."""
    vals, vecs = np.linalg.eig(U)
    w = np.angle(vals)
    keep = np.where(w > w_min)[0]
    order = keep[np.argsort(w[keep])][:n_modes]
    return w[order], vecs[:, order]


def region_weights(vecs, region, E):
    """Fraction of each mode's energy in each region (rows: region 0..5)."""
    energy = np.abs(vecs[:E]) ** 2 + np.abs(vecs[E:]) ** 2
    energy /= energy.sum(axis=0, keepdims=True)
    return np.array([energy[region == r].sum(axis=0) for r in range(6)])


def localized_flavors(vecs, region, E):
    """Unitary V (modes × flavors) maximizing Σ_α ⟨f_α|seg_α|f_α⟩.

    Segment α includes its own ring edges plus the loop at its start.
    Returns |V|² transposed (flavors × modes) and the localization per flavor.
    """
    vecs = vecs / np.linalg.norm(vecs, axis=0, keepdims=True)
    A = []
    for s in range(3):
        mask = np.concatenate([(region == s) | (region == 3 + s)] * 2).astype(float)
        A.append(vecs.conj().T @ (mask[:, None] * vecs))   # 3×3 Hermitian
    def unitary(p):
        H = np.zeros((3, 3), complex)
        iu = np.triu_indices(3, 1)
        H[iu] = p[:3] + 1j * p[3:6]
        H = H - H.conj().T + 1j * np.diag(p[6:9])
        w, v = np.linalg.eigh(-1j * H)                     # H anti-Hermitian → exp
        return v @ np.diag(np.exp(1j * w)) @ v.conj().T
    def neg_loc(p):
        V = unitary(p)
        return -sum(np.real(V[:, a].conj() @ A[a] @ V[:, a]) for a in range(3))
    best = None
    for seed in range(8):
        p0 = np.random.default_rng(seed).normal(0, 1, 9)
        r = minimize(neg_loc, p0, method="BFGS")
        if best is None or r.fun < best.fun:
            best = r
    V = unitary(best.x)
    loc = [np.real(V[:, a].conj() @ A[a] @ V[:, a]) for a in range(3)]
    return (np.abs(V) ** 2).T, np.array(loc)


def analyse(lens, ell, flips, verbose=True):
    tails, heads, signs, region, n_nodes = build_graph(lens, ell, flips)
    E = len(tails)
    U = step_matrix(tails, heads, signs, n_nodes)
    w, vecs = lowest_modes(U, 3, 1e-6)
    m2 = w ** 2
    ratio = (m2[2] - m2[0]) / (m2[1] - m2[0]) if m2[1] > m2[0] + 1e-15 else np.inf
    out = dict(w=w, ratio=ratio)
    if verbose:
        W = region_weights(vecs, region, E)
        U2, loc = localized_flavors(vecs, region, E)
        out.update(W=W, U2=U2, loc=loc)
    return out


def show(lens, ell, flips, label):
    r = analyse(lens, ell, flips)
    w = r["w"]
    print(f"\n== {label}: segments {lens}, loops of {ell} edges, flips {'on' if flips else 'off'}")
    print(f"  ω (lattice units) = {', '.join(f'{x:.5f}' for x in w)};  "
          f"ω₂/ω₁ − 1 = {w[1] / w[0] - 1:.2e};  ω₃/ω₁ = {w[2] / w[0]:.3f};  ratio = {r['ratio']:.2f}")
    print("  fit fractions (share of each mode's energy):")
    print("               ν1     ν2     ν3")
    for s in range(3):
        print(f"    segment {s + 1}  " + "  ".join(f"{r['W'][s, i]:.3f}" for i in range(3)))
    print(f"    loops      " + "  ".join(f"{r['W'][3:, i].sum():.3f}" for i in range(3)))
    print("  mixing |U|² (rows: flavor on segment 1, 2, 3; columns ν1, ν2, ν3):")
    for a in range(3):
        print(f"    flavor {a + 1}   " + "  ".join(f"{r['U2'][a, i]:.3f}" for i in range(3))
              + f"   (localization {r['loc'][a]:.2f})")
    return r


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base", type=int, default=60, help="segment length for --equal and scan centre")
    p.add_argument("--ell", type=int, nargs="+", default=[2, 4, 8], help="loop sizes (edges)")
    p.add_argument("--flips", choices=["on", "off", "both"], default="both")
    p.add_argument("--equal", action="store_true", help="report equal-segment circles")
    p.add_argument("--scan", action="store_true", help="scan segment lengths for the target ratio")
    p.add_argument("--span", type=int, default=12, help="± range of segment-length offsets in scan")
    p.add_argument("--target", type=float, default=33.6)
    p.add_argument("--top", type=int, default=3, help="best scan results to report in full")
    p.add_argument("--lens", type=int, nargs=3, default=None, help="explicit segment lengths")
    a = p.parse_args()
    flip_set = {"on": [True], "off": [False], "both": [False, True]}[a.flips]

    if a.lens:
        for ell in a.ell:
            for fl in flip_set:
                show(tuple(a.lens), ell, fl, "explicit")
    if a.equal:
        for ell in a.ell:
            for fl in flip_set:
                show((a.base,) * 3, ell, fl, "equal segments")
    if a.scan:
        for ell in a.ell:
            for fl in flip_set:
                hits = []
                for d1, d2 in itertools.product(range(-a.span, a.span + 1), repeat=2):
                    lens = (a.base + d1, a.base, a.base + d2)
                    if d1 > d2 or (d1 == 0 and d2 == 0):
                        continue
                    r = analyse(lens, ell, fl, verbose=False)
                    hits.append((abs(np.log(r["ratio"] / a.target)), lens, r["ratio"]))
                hits.sort()
                print(f"\n#### scan: loops {ell}, flips {'on' if fl else 'off'}; "
                      f"closest ratios: " + ", ".join(f"{h[1]}→{h[2]:.1f}" for h in hits[:6]))
                for h in hits[:a.top]:
                    show(h[1], ell, fl, f"scan hit (ratio {h[2]:.1f})")


if __name__ == "__main__":
    main()
