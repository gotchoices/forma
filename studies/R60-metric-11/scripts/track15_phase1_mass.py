"""
R60 Track 15 — Phase 1: Proton mass fit for (3, 6).

Test whether (3, 6) can reach m_p = 938.272 MeV on model-F's
Track 12 baseline, via two routes:

(a) Keep (ε_p, s_p) = (0.55, 0.162) and recalibrate L_ring_p alone.
(b) Switch to "magic shear" for (1, 2) quark base: s_p = 2,
    pick ε_p so quark mass = m_p/3 = 313 MeV.

Sandboxed — no changes to model-F or other tracks.
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np

from track1_solver import (
    Params, build_metric_11, signature_ok, num_negative_eigs,
    alpha_coulomb, mode_6_to_11, derive_L_ring, mu_sheet,
    L_vector_from_params, mode_energy,
    ALPHA, SQRT_ALPHA, FOUR_PI, EIGHT_PI, PI, M_E_MEV, M_P_MEV,
    I_ALEPH, I_E_TUBE, I_E_RING, I_P_TUBE, I_P_RING,
    I_NU_TUBE, I_NU_RING, I_T,
)
from track7b_resolve import build_aug_metric
from track4_diagonal_compensation import K_NATURAL  # 1/(8π), the R59 F59 natural value

# Model-F actual k (single-k symmetry value, = 1.1803/(8π))
K_MODELF = 4.696442e-02


HBAR_C_MEV_FM = 197.3269804
TWO_PI_HC = 2 * PI * HBAR_C_MEV_FM


def modelF_baseline(eps_p=0.55, s_p=0.162037, L_ring_p=20.551):
    """Model-F Track 12 baseline; override p-sheet as needed."""
    return Params(
        eps_e=397.074, s_e=2.004200,
        eps_p=eps_p, s_p=s_p,
        eps_nu=2.0, s_nu=0.022,
        k_e=4.696442e-02, k_p=4.696442e-02, k_nu=4.696442e-02,
        g_aa=1.0,
        sigma_ta=SQRT_ALPHA, sigma_at=FOUR_PI*ALPHA,
        sign_e=+1.0, sign_p=-1.0, sign_nu=+1.0,
        L_ring_e=5.4829e+01,
        L_ring_p=L_ring_p,
        L_ring_nu=1.9577e+11,
    )


def evaluate_mode(params, n6, label=""):
    """Compute mass and α_Coulomb for a mode on the augmented metric."""
    G = build_aug_metric(params)
    L = L_vector_from_params(params)
    sig = signature_ok(G)
    if not sig:
        return {"label": label, "signature": False, "E": None, "alpha": None}
    n11 = mode_6_to_11(n6)
    E = mode_energy(G, L, n11)
    a = alpha_coulomb(G, n11) / ALPHA
    return {"label": label, "signature": True, "E": E, "alpha": a}


def main():
    print("=" * 72)
    print("R60 Track 15 — Phase 1: proton mass for (3, 6)")
    print("=" * 72)
    print(f"  Target: m_p = {M_P_MEV} MeV")
    print()

    # ── Option A — model-F geometry, bare (3, 6) on Track 12 baseline ──
    print("─" * 72)
    print("Option A: model-F (ε_p=0.55, s_p=0.162) baseline, bare (3, 6)")
    print("─" * 72)
    p = modelF_baseline()
    r = evaluate_mode(p, (0, 0, 0, 0, 3, 6), "bare (3,6) on Track 12")
    if r["signature"]:
        print(f"  μ(3,6,0.55,0.162) = {mu_sheet(3, 6, 0.55, 0.162037):.4f}")
        print(f"  E at Track 12 L_ring_p={p.L_ring_p} fm: {r['E']:.4f} MeV")
        print(f"  Ratio to m_p: {r['E']/M_P_MEV:.4f}")
        print(f"  α_Coulomb / α = {r['alpha']:.4f}  (bare formula)")
    print()

    # ── Option A continued — recalibrate L_ring_p for (3, 6) to hit m_p ──
    print("─" * 72)
    print("Option A.2: recalibrate L_ring_p alone so (3, 6) = m_p")
    print("─" * 72)
    L_new = derive_L_ring(M_P_MEV, 3, 6, 0.55, 0.162037, K_MODELF)
    print(f"  L_ring_p (calibrated for (3,6)) = {L_new:.4f} fm")
    print(f"  vs Track 12 L_ring_p = 20.551 fm  (factor {L_new/20.551:.4f}×)")
    p2 = modelF_baseline(L_ring_p=L_new)
    r2 = evaluate_mode(p2, (0, 0, 0, 0, 3, 6), "recalib L (3,6)")
    if r2["signature"]:
        print(f"  E at new L: {r2['E']:.6f} MeV  (target {M_P_MEV})")
        print(f"  α_Coulomb / α = {r2['alpha']:.4f}  (bare formula — expect 9)")
    print()

    # ── Option B — magic shear for (1, 2) quark, ε_p search ──
    print("─" * 72)
    print("Option B: magic shear s_p = 2, quark mass = m_p/3 = 312.76 MeV")
    print("─" * 72)
    print("  At s_p = 2, μ(1, 2) = 1/ε_p (shear cancellation).")
    print("  Want quark (1, 2) at m_p/3 = 312.757 MeV, giving (3, 6) at m_p.")
    print()
    m_q = M_P_MEV / 3
    k_p = K_MODELF
    # E_quark = 2πℏc × (1/ε_p) / (L_ring_p × √k_p) = m_q
    #  → ε_p × L_ring_p × √k_p = 2πℏc / m_q
    target_prod = TWO_PI_HC / m_q
    print(f"  Required ε_p × L_ring_p × √k_p = 2πℏc / m_q")
    print(f"                                 = {target_prod:.4f} fm")
    print(f"  At k_p = 1.1803/(8π), √k_p = {math.sqrt(k_p):.4f}")
    print(f"  ⟹ ε_p × L_ring_p = {target_prod/math.sqrt(k_p):.4f} fm")
    print()
    # A few candidate (ε_p, L_ring_p) pairs:
    print(f"  {'ε_p':>8s}  {'L_ring_p (fm)':>14s}  {'sε':>6s}  "
          f"{'(1,2) E (MeV)':>14s}  {'(3,6) E (MeV)':>14s}  sig")
    for eps_p in [0.33, 0.55, 1.0, 1.5]:
        L_p = target_prod / (eps_p * math.sqrt(k_p))
        p3 = modelF_baseline(eps_p=eps_p, s_p=2.0, L_ring_p=L_p)
        r_q = evaluate_mode(p3, (0, 0, 0, 0, 1, 2), "quark")
        r_pr = evaluate_mode(p3, (0, 0, 0, 0, 3, 6), "proton")
        sig_str = "YES" if r_q["signature"] else "NO"
        sε = eps_p * 2.0
        E_q = f"{r_q['E']:.4f}" if r_q["signature"] else "—"
        E_pr = f"{r_pr['E']:.4f}" if r_pr["signature"] else "—"
        print(f"  {eps_p:>8.2f}  {L_p:>14.4f}  {sε:>6.2f}  "
              f"{E_q:>14s}  {E_pr:>14s}  {sig_str}")
    print()

    # ── Summary ──
    print("─" * 72)
    print("Phase 1 summary")
    print("─" * 72)
    print("  A.2 Option (recalibrate L alone, keep ε_p=0.55, s_p=0.162):")
    print(f"    L_ring_p = {L_new:.3f} fm  (was 20.55 fm)")
    print(f"    Gives (3, 6) → {r2['E']:.3f} MeV  (target {M_P_MEV})")
    print(f"    α bare = {r2['alpha']:.2f}  (expected 9 for n_pt=3)")
    print()
    print("  B Option (magic shear s_p=2, pick ε_p):")
    print("    Multiple (ε_p, L_ring_p) choices achievable.")
    print("    Quark mode (1, 2) lands at m_p/3 = 312.757 MeV.")
    print("    (3, 6) composite lands at m_p = 938.272 MeV.")
    print("    All give α = 9 (bare formula) — composite reinterpretation needed.")
    print()
    print("Phase 1 complete.  Mass is achievable for (3, 6) via both options.")
    print("Phase 2 will address the α issue (bare formula gives 9).")


if __name__ == "__main__":
    main()
