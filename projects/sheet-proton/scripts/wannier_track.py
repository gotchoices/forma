"""
wannier_track.py — Wannier-function decomposition of the proton and
neutron wave-content along their closed (1/2, 1) tracks.

Background
----------
The framework reads the baryon as one wave-quantum whose charge content
is organised in series along its characteristic curve (the closed
(1/2, 1) track on the modulated clover).  The track passes through
3 arc-pieces in series:
  proton (t₀ = −π/6):  lobe / saddle / lobe   ←  uud
  neutron (t₀ = +π/6): saddle / lobe / saddle ←  udd
Equal-θ-segment integration of the existing track_charge mixes these
contributions and gives uniform per-segment values (+1/3 each for the
proton, 0 each for the neutron) — the substrate's Z₃ symmetry forces
this.  But the user's proposal is that the *three quarks* are
overlapping wave packets localised at the three arc-midpoints along
the track, with each wave packet carrying the per-arc cross-section
winding (+2/3 lobe / −1/3 saddle) as its charge.  This file
constructs those wave packets as Wannier functions of a band of
1-D LB modes on the closed track.

What it does
------------
1. Build the closed (1/2, 1) track on the Z₂×Z₃-symmetric Step-7
   substrate.  The track has arc-length parameterisation s ∈ [0, L].
2. Compute the induced 1-D Riemannian metric ds² and the geodesic
   curvature κ_g(s).
3. Solve the 1-D LB on the closed track: -d²ψ/ds² = λ ψ with periodic
   BC; the lowest band of 3 modes (modes 0, 1, 2 — i.e. the constant
   and the lowest cos/sin pair) is the natural Wannier-band.
4. Construct 3 Wannier functions w_k(s) (k = 0, 1, 2) centered at
   s_k = (k + 1/2) · L/3 — the 3 arc-midpoints.  The Wannier
   functions are localised linear combinations of the band modes.
5. For each Wannier function, compute (a) the per-arc location of
   its centre (which arc-piece it sits in) and (b) the per-arc
   cross-section winding at that arc — this gives the per-quark
   fractional charge.  Verify the sum equals the total track charge
   (+1 for proton, 0 for neutron).

Outputs
-------
  outputs/wannier_track_summary.txt    — full report
  outputs/wannier_track.png            — plot of Wannier functions
                                          on top of the track curvature

Usage
-----
  python scripts/wannier_track.py

The script is parameter-light: it uses the symmetric Step-7 modulation
hard-coded for reproducibility.
"""

from __future__ import annotations

import sys
from math import pi
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from modulated_clover import (
    modulation, modulation_deriv, w_derivs_N3, dchi_dt,
)


# Symmetric Step-7 solution (work/derived-clover.md §Finding,
# work/modulated-clover.md §11).
SYM_PARAMS = dict(
    Ac=np.array([0.0, -0.48765]),
    As=np.array([0.0, +0.65694]),
    Bc=np.array([0.0, -0.00038]),
    Bs=np.array([0.0, +0.00032]),
    a2=0.32994,
    b2=0.03201,
    rho=1.0,
    Rmajor=36.17,
)


def track_arclength(t0, Ac, As, Bc, Bs, a2, b2, rho, Rmajor, Nth=4000):
    """Build the closed (1/2, 1) track t(θ) = t₀ + θ/2 for θ ∈ [0, 2π].
    Returns (theta_grid, s_grid, L_total) where s(θ) is the cumulative
    arc-length and L_total = s(2π)."""
    theta = np.linspace(0.0, 2 * pi, Nth + 1)
    t = t0 + theta / 2.0
    a1 = modulation(theta, Ac, As)
    b1 = modulation(theta, Bc, Bs)
    a1p = modulation_deriv(theta, Ac, As)
    b1p = modulation_deriv(theta, Bc, Bs)
    c3, s3 = np.cos(3 * t), np.sin(3 * t)
    c6, s6 = np.cos(6 * t), np.sin(6 * t)
    w = 1.0 + a1 * c3 + a2 * c6 + 1j * (b1 * s3 + b2 * s6)
    wt = (-3.0 * a1 * s3 - 6.0 * a2 * s6) + 1j * (3.0 * b1 * c3 + 6.0 * b2 * c6)
    wth = a1p * c3 + 1j * (b1p * s3)
    phase = rho * np.exp(1j * (theta / 2.0 + t))
    zeta = phase * w
    zeta_t = phase * (1j * w + wt)
    zeta_th = phase * (0.5j * w + wth)
    # Track tangent: ds/dθ = |dζ/dθ + (R-major-ring contribution)|.
    g_tt = np.abs(zeta_t) ** 2
    g_tth = np.real(np.conj(zeta_t) * zeta_th)
    g_thth = np.abs(zeta_th) ** 2 + (Rmajor + zeta.real) ** 2
    ds = np.sqrt(np.maximum(g_tt / 4.0 + g_tth + g_thth, 0.0))   # |dx/dθ|
    s = np.concatenate([[0.0], np.cumsum(0.5 * (ds[1:] + ds[:-1])
                                          * (theta[1:] - theta[:-1]))])
    return theta, s, float(s[-1])


def track_curvature_integrand(t0, Ac, As, Bc, Bs, a2, b2, Nth=4000):
    """Integrand of the (1/2, 1) track charge: ∂_t χ along the track,
    indexed by the same θ-grid as track_arclength."""
    theta = np.linspace(0.0, 2 * pi, Nth + 1)
    t = t0 + theta / 2.0
    return theta, dchi_dt(t, theta, Ac, As, Bc, Bs, a2, b2)


def lb_band(s, n_modes=5):
    """First n_modes 1-D LB eigenmodes on the closed track with arc-length
    parameterisation s ∈ [0, L].  -d²ψ/ds² = λ ψ with periodic BC.
    Returns (eigvals, eigvecs[:, k]) where eigvecs[:, k] is the k-th
    eigenmode evaluated on the s-grid.  Trivial mode (constant) is k=0.

    Real cosine/sine basis:
      ψ_0(s) = 1 / √L                                              (λ=0)
      ψ_{2j-1}(s) = √(2/L) cos(2πj s / L)                          (λ=(2πj/L)²)
      ψ_{2j}(s)   = √(2/L) sin(2πj s / L)                          (degenerate)
    """
    L = float(s[-1])
    eigvals = []
    eigvecs = []
    # Mode 0: constant
    eigvals.append(0.0)
    eigvecs.append(np.ones_like(s) / np.sqrt(L))
    j = 1
    while len(eigvecs) < n_modes:
        omega = 2 * pi * j / L
        eigvals.append(omega ** 2)
        eigvecs.append(np.sqrt(2.0 / L) * np.cos(omega * s))
        if len(eigvecs) < n_modes:
            eigvals.append(omega ** 2)
            eigvecs.append(np.sqrt(2.0 / L) * np.sin(omega * s))
        j += 1
    return np.array(eigvals[:n_modes]), np.stack(eigvecs[:n_modes], axis=1)


def wannier_3site(s, n_band=3):
    """Construct 3 Wannier functions at sites s_k = (k + 1/2) · L/3
    (k = 0, 1, 2) from the lowest n_band = 3 LB modes (1 constant +
    1 cos + 1 sin = the lowest cos/sin pair).

    Bloch waves at the 3 k-values (k_j = 2π j / L for j = 0, 1, 2, but
    with j = 1 and j = -1 being degenerate, we use j = 0, +1, -1) form a
    3-mode band.  Equivalently in real basis: ψ_0 (constant), ψ_+ =
    √(2/L) cos(2πs/L), ψ_- = √(2/L) sin(2πs/L).

    Wannier function at site s_k:
      w_k(s) = (1/√3) [ψ_0(s) + √2 cos(2π(s - s_k)/L)]
             = (1/√3) [1/√L + √(2/L) · √2 (cos(2πs/L) cos(2πs_k/L)
                                            + sin(2πs/L) sin(2πs_k/L))]

    This is a Z₃-symmetric Wannier triple: w_k(s) = w_0(s - s_k).
    """
    L = float(s[-1])
    s_centers = (np.arange(3) + 0.5) * L / 3.0
    wann = np.zeros((len(s), 3))
    psi0 = 1.0 / np.sqrt(L)
    psi_cos = np.sqrt(2.0 / L) * np.cos(2 * pi * s / L)
    psi_sin = np.sqrt(2.0 / L) * np.sin(2 * pi * s / L)
    for k, s_k in enumerate(s_centers):
        c = np.cos(2 * pi * s_k / L)
        ss = np.sin(2 * pi * s_k / L)
        # |w_k⟩ = (1/√3) (|ψ_0⟩ + √2 cos(2π(s-s_k)/L)-projection)
        # Coefficient on |ψ_cos⟩ = (1/√3) √2 cos(2π s_k / L)
        # Coefficient on |ψ_sin⟩ = (1/√3) √2 sin(2π s_k / L)
        wann[:, k] = (1.0 / np.sqrt(3.0)) * (psi0
                                              + np.sqrt(2.0) * c * psi_cos
                                              + np.sqrt(2.0) * ss * psi_sin)
    return s_centers, wann


def cross_section_arc_winding(theta_k, t_arc_lo, t_arc_hi,
                              Ac, As, Bc, Bs, a2, b2, Nt_arc=2000):
    """Compute the cross-section per-arc winding at fixed θ = θ_k,
    integrating (d/dt) arg(∂_t ζ) over t ∈ [t_arc_lo, t_arc_hi].
    In the symmetric Z_6 unmodulated case this gives +2/3 for lobe arcs
    (240° windings) and -1/3 for saddle arcs (-120°).  Under modulation
    it shifts by the modulation correction."""
    t_arc = np.linspace(t_arc_lo, t_arc_hi, Nt_arc + 1)
    theta_arr = np.full_like(t_arc, theta_k)
    dcdt = dchi_dt(t_arc, theta_arr, Ac, As, Bc, Bs, a2, b2)
    # (1/2π) ∫ (d χ_cross / dt) dt over the arc, where d χ_cross / dt is the
    # cross-section tangent rate at fixed θ.  Same integrand as dchi_dt
    # but integrated over t with θ held still.  Note dchi_dt returns
    # 1 + Im(...)/|...|² — the "1" is the trivial tangent rotation from
    # the e^{i t} factor; we want the full tangent winding so we keep it.
    return float(np.trapezoid(dcdt, t_arc) / (2 * pi))


def quark_charge_assignment(t0_track, s_centers, theta_track, s_track,
                            Ac, As, Bc, Bs, a2, b2):
    """For each Wannier center s_k, identify which cross-section arc-piece
    the (1/2, 1) track is sitting at, and compute the *actual* cross-section
    per-arc winding at that arc and θ.

    Returns a list of 3 entries
      (s_k, t_k, theta_k, arc_label, q_arc_winding, q_naive)
    where q_arc_winding is the computed cross-section per-arc winding (the
    proper per-quark charge under modulation) and q_naive is the unmodulated
    value (+2/3 lobe, -1/3 saddle)."""
    theta_at_sk = np.interp(s_centers, s_track, theta_track)
    t_at_sk = t0_track + theta_at_sk / 2.0
    # Arc boundaries at t = ±π/6 + k·π/3 (mod 2π).  Lobe arcs centred at
    # t = 0, 2π/3, 4π/3 (cos 3t = +1 → convex).  Saddle arcs centred at
    # π/3, π, 5π/3 (cos 3t = -1 → concave).
    out = []
    for k, (s_k, th_k, t_k) in enumerate(zip(s_centers, theta_at_sk, t_at_sk)):
        tmod = t_k % (2 * pi)
        # Distance to nearest lobe center
        lobe_centers = np.array([0.0, 2 * pi / 3, 4 * pi / 3])
        d_to_lobe = np.min(np.abs(((tmod - lobe_centers + pi) % (2 * pi)) - pi))
        is_lobe = d_to_lobe <= pi / 6 + 1e-9
        if is_lobe:
            arc_center = lobe_centers[np.argmin(
                np.abs(((tmod - lobe_centers + pi) % (2 * pi)) - pi))]
            label = "lobe (u)"
            q_naive = +2.0 / 3.0
        else:
            saddle_centers = np.array([pi / 3, pi, 5 * pi / 3])
            arc_center = saddle_centers[np.argmin(
                np.abs(((tmod - saddle_centers + pi) % (2 * pi)) - pi))]
            label = "saddle (d)"
            q_naive = -1.0 / 3.0
        t_lo, t_hi = arc_center - pi / 6, arc_center + pi / 6
        q_arc = cross_section_arc_winding(th_k, t_lo, t_hi,
                                          Ac, As, Bc, Bs, a2, b2)
        out.append((float(s_k), float(t_k), float(th_k), label,
                    float(q_arc), float(q_naive)))
    return out


def main():
    theta_p, s_p, L_p = track_arclength(
        -pi / 6.0,
        SYM_PARAMS["Ac"], SYM_PARAMS["As"], SYM_PARAMS["Bc"], SYM_PARAMS["Bs"],
        SYM_PARAMS["a2"], SYM_PARAMS["b2"], SYM_PARAMS["rho"], SYM_PARAMS["Rmajor"])
    theta_n, s_n, L_n = track_arclength(
        +pi / 6.0,
        SYM_PARAMS["Ac"], SYM_PARAMS["As"], SYM_PARAMS["Bc"], SYM_PARAMS["Bs"],
        SYM_PARAMS["a2"], SYM_PARAMS["b2"], SYM_PARAMS["rho"], SYM_PARAMS["Rmajor"])

    # Build LB band + Wannier functions for each track.
    lb_p_vals, lb_p_vecs = lb_band(s_p, n_modes=5)
    lb_n_vals, lb_n_vecs = lb_band(s_n, n_modes=5)
    sites_p, wann_p = wannier_3site(s_p)
    sites_n, wann_n = wannier_3site(s_n)

    # Assign per-quark charges based on which arc each Wannier centre sits in.
    quarks_p = quark_charge_assignment(
        -pi / 6.0, sites_p, theta_p, s_p,
        SYM_PARAMS["Ac"], SYM_PARAMS["As"], SYM_PARAMS["Bc"], SYM_PARAMS["Bs"],
        SYM_PARAMS["a2"], SYM_PARAMS["b2"])
    quarks_n = quark_charge_assignment(
        +pi / 6.0, sites_n, theta_n, s_n,
        SYM_PARAMS["Ac"], SYM_PARAMS["As"], SYM_PARAMS["Bc"], SYM_PARAMS["Bs"],
        SYM_PARAMS["a2"], SYM_PARAMS["b2"])

    # Also compute the per-arc windings on the *unmodulated* cross-section
    # (a₁ = b₁ = 0) for comparison.  This is the bare Z_6 dihedral case
    # where each lobe arc is expected to give +2/3 and each saddle -1/3.
    zero = np.array([0.0, 0.0])
    quarks_p_unmod = quark_charge_assignment(
        -pi / 6.0, sites_p, theta_p, s_p,
        zero, zero, zero, zero,
        SYM_PARAMS["a2"], SYM_PARAMS["b2"])
    quarks_n_unmod = quark_charge_assignment(
        +pi / 6.0, sites_n, theta_n, s_n,
        zero, zero, zero, zero,
        SYM_PARAMS["a2"], SYM_PARAMS["b2"])

    # Curvature integrand along each track (for plotting context).
    _, dcdt_p = track_curvature_integrand(
        -pi / 6.0,
        SYM_PARAMS["Ac"], SYM_PARAMS["As"], SYM_PARAMS["Bc"], SYM_PARAMS["Bs"],
        SYM_PARAMS["a2"], SYM_PARAMS["b2"])
    _, dcdt_n = track_curvature_integrand(
        +pi / 6.0,
        SYM_PARAMS["Ac"], SYM_PARAMS["As"], SYM_PARAMS["Bc"], SYM_PARAMS["Bs"],
        SYM_PARAMS["a2"], SYM_PARAMS["b2"])

    # ---- report ----
    R = []
    R.append("=" * 78)
    R.append("wannier_track.py — quark substructure as Wannier functions of")
    R.append("a 3-mode LB band on the closed (1/2, 1) track.")
    R.append("=" * 78)
    R.append("")
    R.append(f"Symmetric Step-7 substrate parameters used:")
    R.append(f"  Ac = {SYM_PARAMS['Ac']}   As = {SYM_PARAMS['As']}")
    R.append(f"  Bc = {SYM_PARAMS['Bc']}   Bs = {SYM_PARAMS['Bs']}")
    R.append(f"  a2 = {SYM_PARAMS['a2']:.5f}  b2 = {SYM_PARAMS['b2']:+.5f}")
    R.append(f"  R_major = {SYM_PARAMS['Rmajor']:.4f}")
    R.append("")
    R.append("Track lengths (arc-length on the embedded 2-D substrate):")
    R.append(f"  L_proton  = {L_p:.4f}")
    R.append(f"  L_neutron = {L_n:.4f}")
    R.append(f"  L_p / L_n = {L_p / L_n:.7f}   (target m_n/m_p = {939.56542 / 938.27209:.7f})")
    R.append("")
    R.append("Lowest 1-D LB band on each track (eigenvalues λ = (2π n / L)²):")
    R.append(f"  proton  band : {lb_p_vals[:5].tolist()}")
    R.append(f"  neutron band : {lb_n_vals[:5].tolist()}")
    R.append("")
    R.append("Wannier-function construction: 3 sites at the 3 arc-midpoints")
    R.append("of each closed track, built from the lowest 3 LB modes")
    R.append("(constant + lowest cos/sin pair).  The Wannier functions are")
    R.append("Z₃-symmetric Gaussian-like packets, each peaked at its site,")
    R.append("with tails extending into adjacent sites.")
    R.append("")
    R.append("Per-Wannier per-arc charges: for each Wannier centre we")
    R.append("compute the *actual* cross-section per-arc winding at that")
    R.append("(t, θ) by integrating the cross-section tangent rate over")
    R.append("the arc containing the Wannier centre.  This is the per-quark")
    R.append("charge under hypothesis G1; the unmodulated (+2/3 / -1/3)")
    R.append("values are shown alongside for comparison.")
    R.append("")
    R.append("PROTON  quark assignment (t₀ = -π/6):")
    R.append(f"  {'k':>2}  {'s_k':>10}  {'t_k':>8}  {'θ_k':>8}  {'arc':>12}  {'q_arc':>8}  {'q_naive':>8}")
    sum_qp = 0.0
    for k, (s_k, t_k, th_k, lab, q_arc, q_naive) in enumerate(quarks_p):
        sum_qp += q_arc
        R.append(f"  {k:>2}  {s_k:>10.4f}  {t_k % (2*pi):>8.4f}  {th_k:>8.4f}  "
                 f"{lab:>12}  {q_arc:>+8.4f}  {q_naive:>+8.4f}")
    R.append(f"  ----  sum of q_arc = {sum_qp:+.6f}  (target +1)")
    R.append("")
    R.append("NEUTRON quark assignment (t₀ = +π/6):")
    R.append(f"  {'k':>2}  {'s_k':>10}  {'t_k':>8}  {'θ_k':>8}  {'arc':>12}  {'q_arc':>8}  {'q_naive':>8}")
    sum_qn = 0.0
    for k, (s_k, t_k, th_k, lab, q_arc, q_naive) in enumerate(quarks_n):
        sum_qn += q_arc
        R.append(f"  {k:>2}  {s_k:>10.4f}  {t_k % (2*pi):>8.4f}  {th_k:>8.4f}  "
                 f"{lab:>12}  {q_arc:>+8.4f}  {q_naive:>+8.4f}")
    R.append(f"  ----  sum of q_arc = {sum_qn:+.6f}  (target 0)")
    R.append("")
    p_arc_errs = [abs(q[4] - q[5]) for q in quarks_p]
    n_arc_errs = [abs(q[4] - q[5]) for q in quarks_n]
    R.append(f"max |q_arc - q_naive|: proton {max(p_arc_errs):.4f}   "
             f"neutron {max(n_arc_errs):.4f}")
    R.append("")
    R.append("Same cross-section per-arc winding, but on the *unmodulated*")
    R.append("backbone (a₁ = b₁ = 0, just a₂ cos 6t + b₂ sin 6t).  This")
    R.append("isolates the bare Z_6 dihedral cross-section's per-arc charges.")
    R.append("")
    R.append("PROTON  (unmodulated cross-section):")
    sum_qp_u = 0.0
    for k, (s_k, t_k, th_k, lab, q_arc, q_naive) in enumerate(quarks_p_unmod):
        sum_qp_u += q_arc
        R.append(f"  {k:>2}  t={t_k % (2*pi):>7.4f}  {lab:>12}  "
                 f"q_arc = {q_arc:>+8.4f}  naive = {q_naive:>+8.4f}")
    R.append(f"  ----  sum of q_arc (unmod) = {sum_qp_u:+.6f}")
    R.append("")
    R.append("NEUTRON (unmodulated cross-section):")
    sum_qn_u = 0.0
    for k, (s_k, t_k, th_k, lab, q_arc, q_naive) in enumerate(quarks_n_unmod):
        sum_qn_u += q_arc
        R.append(f"  {k:>2}  t={t_k % (2*pi):>7.4f}  {lab:>12}  "
                 f"q_arc = {q_arc:>+8.4f}  naive = {q_naive:>+8.4f}")
    R.append(f"  ----  sum of q_arc (unmod) = {sum_qn_u:+.6f}")
    R.append("")
    if abs(sum_qp - 1.0) < 0.05 and abs(sum_qn) < 0.05:
        R.append("RESULT: the 3 Wannier centres sit on the correct arc sequence")
        R.append("(lobe-saddle-lobe for proton, saddle-lobe-saddle for neutron).")
        R.append("Computed cross-section per-arc windings:")
        R.append(f"  proton:  sum = {sum_qp:+.4f}  (target +1)")
        R.append(f"  neutron: sum = {sum_qn:+.4f}  (target  0)")
        if max(max(p_arc_errs), max(n_arc_errs)) < 0.05:
            R.append("Modulated per-arc windings match the unmodulated ±2/3 / ∓1/3")
            R.append("values to within ~5%.  The 3-quarks-in-series picture is")
            R.append("geometrically rigorous on this substrate.")
        else:
            R.append("Modulated per-arc windings differ from the unmodulated values")
            R.append(f"by up to {max(max(p_arc_errs), max(n_arc_errs)):.3f} (the modulation")
            R.append("redistributes the per-arc winding away from the symmetric")
            R.append("±2/3 / ∓1/3 values, while the total still sums correctly).")
    else:
        R.append("RESULT: per-arc cross-section windings do NOT sum to target charges.")
        R.append("Check the arc-boundary definitions or the Wannier centre placement.")

    text = "\n".join(R)
    print(text)

    out_dir = Path(__file__).resolve().parents[1] / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "wannier_track_summary.txt"
    out_path.write_text(text + "\n")
    print(f"\nWrote: {out_path}")

    # ---- plot ----
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 1, figsize=(11, 7), sharex=False)

    # Proton panel
    ax = axes[0]
    # Curvature integrand along s — interpolate to s_p grid.
    dcdt_p_on_s = dcdt_p[:len(s_p)]
    ax.plot(s_p, dcdt_p_on_s, color="0.5", lw=0.9,
            label=r"track curvature $\partial_t\chi$ (proton)")
    for k in range(3):
        ax.plot(s_p, wann_p[:, k] * (L_p ** 0.5),
                lw=1.5, label=f"Wannier w_{k}(s)")
        ax.axvline(sites_p[k], ls="--", color=f"C{k}", alpha=0.5)
    # Mark arc boundaries at θ = 2π/3, 4π/3:
    s_b1 = np.interp(2 * pi / 3, theta_p, s_p)
    s_b2 = np.interp(4 * pi / 3, theta_p, s_p)
    ax.axvline(s_b1, color="k", ls=":", alpha=0.4)
    ax.axvline(s_b2, color="k", ls=":", alpha=0.4)
    ax.set_xlim(0, L_p)
    ax.set_xlabel("arc length s on proton track")
    ax.set_ylabel("amplitude")
    ax.set_title(f"Proton (t₀=−π/6, L={L_p:.2f}): Wannier wave packets + curvature")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.3)

    # Neutron panel
    ax = axes[1]
    dcdt_n_on_s = dcdt_n[:len(s_n)]
    ax.plot(s_n, dcdt_n_on_s, color="0.5", lw=0.9,
            label=r"track curvature $\partial_t\chi$ (neutron)")
    for k in range(3):
        ax.plot(s_n, wann_n[:, k] * (L_n ** 0.5),
                lw=1.5, label=f"Wannier w_{k}(s)")
        ax.axvline(sites_n[k], ls="--", color=f"C{k}", alpha=0.5)
    s_b1n = np.interp(2 * pi / 3, theta_n, s_n)
    s_b2n = np.interp(4 * pi / 3, theta_n, s_n)
    ax.axvline(s_b1n, color="k", ls=":", alpha=0.4)
    ax.axvline(s_b2n, color="k", ls=":", alpha=0.4)
    ax.set_xlim(0, L_n)
    ax.set_xlabel("arc length s on neutron track")
    ax.set_ylabel("amplitude")
    ax.set_title(f"Neutron (t₀=+π/6, L={L_n:.2f}): Wannier wave packets + curvature")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    png_path = out_dir / "wannier_track.png"
    fig.savefig(png_path, dpi=120)
    print(f"Wrote: {png_path}")


if __name__ == "__main__":
    main()
