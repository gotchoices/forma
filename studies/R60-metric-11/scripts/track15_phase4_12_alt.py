"""
R60 Track 15 — Phase 4: (1, 2) proton alternative check.

The simplest ratio-rule-compliant proton is (1, 2) on the p-sheet
— same topology as the electron (1, 2) on e-sheet, different
geometry giving different mass.  Under ratio rule: spin = 1/2
(same as electron).  gcd(1, 2) = 1 so composite α rule = bare α
rule: no new interpretation needed, α = α for Q = 1 mode.

Sandboxed.  No changes to model-F.
"""

import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))

from track1_solver import (
    build_metric_11, signature_ok, alpha_coulomb, mode_6_to_11,
    derive_L_ring, mu_sheet, L_vector_from_params, mode_energy,
    ALPHA, SQRT_ALPHA, FOUR_PI, PI, M_P_MEV,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF, modelF_baseline


HBAR_C_MEV_FM = 197.3269804
TWO_PI_HC = 2 * PI * HBAR_C_MEV_FM


def main():
    print("=" * 72)
    print("R60 Track 15 — Phase 4: (1, 2) proton on p-sheet")
    print("=" * 72)
    print()
    print("  Hypothesis: (1, 2) topology on p-sheet, different mass")
    print("  from different geometry.  gcd = 1 so bare α rule applies.")
    print()

    # ── Option A: keep Track 12 (ε_p, s_p), recalibrate L_ring_p ──
    print("─" * 72)
    print("Option A: (ε_p, s_p) = (0.55, 0.162), recalibrate L_ring_p")
    print("─" * 72)
    L_p_A = derive_L_ring(M_P_MEV, 1, 2, 0.55, 0.162037, K_MODELF)
    print(f"  μ(1, 2, 0.55, 0.162) = {mu_sheet(1, 2, 0.55, 0.162037):.4f}")
    print(f"  L_ring_p (calibrated) = {L_p_A:.4f} fm")
    p = modelF_baseline(eps_p=0.55, s_p=0.162037, L_ring_p=L_p_A)
    G = build_aug_metric(p)
    L = L_vector_from_params(p)
    sig = signature_ok(G)
    print(f"  signature = {sig}")
    if sig:
        E_p = mode_energy(G, L, mode_6_to_11((0, 0, 0, 0, 1, 2)))
        a_p = alpha_coulomb(G, mode_6_to_11((0, 0, 0, 0, 1, 2))) / ALPHA
        print(f"  E(1, 2) = {E_p:.4f} MeV  (target {M_P_MEV})")
        print(f"  α/α     = {a_p:.4f}  (expect 1)")
    print()

    # ── Option B: magic shear (s_p = 2) for (1, 2) at shear cancellation ──
    print("─" * 72)
    print("Option B: magic shear s_p = 2, (1, 2) at shear cancellation point")
    print("─" * 72)
    print("  At s = 2, μ(1, 2) = 1/ε_p.  Simplest: ε_p = 1/m_p-dependent value")
    print()
    print(f"  {'ε_p':>6s}  {'L_ring_p (fm)':>14s}  {'sε':>5s}  "
          f"{'E(1,2) MeV':>12s}  {'α/α':>8s}  sig")
    for eps_p in [0.33, 0.5, 1.0, 1.5, 2.0]:
        L_p = TWO_PI_HC / (M_P_MEV * eps_p * math.sqrt(K_MODELF))
        p_b = modelF_baseline(eps_p=eps_p, s_p=2.0, L_ring_p=L_p)
        G_b = build_aug_metric(p_b)
        L_b = L_vector_from_params(p_b)
        sig_b = signature_ok(G_b)
        sε = eps_p * 2.0
        if sig_b:
            E = mode_energy(G_b, L_b, mode_6_to_11((0, 0, 0, 0, 1, 2)))
            a = alpha_coulomb(G_b, mode_6_to_11((0, 0, 0, 0, 1, 2))) / ALPHA
            E_str = f"{E:.4f}"
            a_str = f"{a:.4f}"
        else:
            E_str = "—"
            a_str = "—"
        sig_str = "YES" if sig_b else "NO"
        print(f"  {eps_p:>6.2f}  {L_p:>14.4f}  {sε:>5.2f}  "
              f"{E_str:>12s}  {a_str:>8s}  {sig_str}")
    print()

    # ── Nuclear scaling test for (1, 2) proton ──
    print("─" * 72)
    print("Nuclear scaling with (1, 2) proton base")
    print("─" * 72)
    print("  Natural scaling: n_pt = A, n_pr = 2A (single-strand per nucleon)")
    print("  α_sum = n_et − A + n_νt.  For α = Z²α: α_sum = ±Z.")
    print("  With n_νt = 0: need n_et = Z − A + Z = (2Z − A)")
    print()
    p = modelF_baseline(eps_p=0.55, s_p=0.162037, L_ring_p=L_p_A)
    G = build_aug_metric(p)
    L = L_vector_from_params(p)

    NUCLEI = [
        ("d (²H)",   2,   1,  1875.6128),
        ("⁴He",      4,   2,  3727.379),
        ("¹²C",     12,   6, 11177.929),
        ("⁵⁶Fe",    56,  26, 52089.77),
    ]
    print(f"  {'Nucleus':<10s}  {'(n_et,n_pt,n_pr)':<18s}  "
          f"{'E (MeV)':>12s}  {'target':>12s}  {'Δ':>9s}")
    for label, A, Z, target in NUCLEI:
        n_et = A - Z  # traditional choice; would give Q = -(A-Z) + A = Z ✓
        n_pt = A
        n_pr = 2 * A
        n6 = (n_et, 0, 0, 0, n_pt, n_pr)
        n11 = mode_6_to_11(n6)
        E_pred = mode_energy(G, L, n11)
        rel = (E_pred - target) / target
        tuple_str = f"({n_et},{n_pt},{n_pr})"
        print(f"  {label:<10s}  {tuple_str:<18s}  "
              f"{E_pred:>12.4f}  {target:>12.4f}  {rel:>+9.4%}")
    print()

    print("Phase 4 complete.")


if __name__ == "__main__":
    main()
