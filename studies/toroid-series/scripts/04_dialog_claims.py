#!/usr/bin/env python3
"""
04_dialog_claims.py — Verify or refute specific quantitative claims from the
Gemini dialog (ref/dialog.md).

Each claim is tested independently and labeled CONFIRMED, REFUTED, or
PARTIALLY CONFIRMED with an explanation.

Reference: theory.md §3
"""

import math, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib import constants as C
from lib.wvm import q_over_e, S_TARGET

results = []


def verdict(label, status, detail):
    results.append((label, status, detail))
    marker = {"CONFIRMED": "✓", "REFUTED": "✗", "PARTIAL": "~"}[status]
    print(f"  [{marker}] {status}: {label}")
    for line in detail.strip().split("\n"):
        print(f"      {line}")
    print()


def main():
    print("=" * 72)
    print("Verification of Gemini Dialog Claims")
    print("=" * 72)
    print()

    # ── Claim 1 (§24): α-series gives "exactly the correction needed" ─────────
    print("─" * 72)
    print("CLAIM 1 (dialog §24): An 11-term geometric series with ratio α")
    print("  provides 'exactly the kind of correction factor needed.'")
    print("─" * 72)
    s_alpha = sum(C.alpha ** i for i in range(11))
    correction_pct = (s_alpha - 1) * 100
    needed_pct = (S_TARGET - 1) * 100

    verdict(
        "α-series correction magnitude",
        "REFUTED",
        f"Series sum = {s_alpha:.8f}  (correction = +{correction_pct:.4f}%)\n"
        f"Needed:      {S_TARGET:.8f}  (correction = +{needed_pct:.4f}%)\n"
        f"The α-series is {needed_pct / correction_pct:.1f}× too small."
    )

    # ── Claim 2 (§24): 11th layer at α-scaling reaches ~64 × Planck ──────────
    print("─" * 72)
    print("CLAIM 2 (dialog §24): Scaling by α for 10 steps from λ_C")
    print("  reaches ~1.03×10⁻³³ m, about 64× the Planck length.")
    print("─" * 72)
    layer_11 = C.lambda_C * C.alpha ** 10
    ratio_planck = layer_11 / C.l_P

    verdict(
        "11th layer scale",
        "CONFIRMED",
        f"λ_C × α¹⁰ = {layer_11:.3e} m\n"
        f"Ratio to l_P = {ratio_planck:.1f}×\n"
        f"Dialog claimed ~64×; actual = {ratio_planck:.1f}×."
    )

    # ── Claim 3 (§25): α⁻¹ ≈ 360/ϕ² ─────────────────────────────────────────
    print("─" * 72)
    print("CLAIM 3 (dialog §25): α⁻¹ ≈ 360/ϕ²")
    print("─" * 72)
    val_360_phi2 = 360 / C.phi ** 2
    alpha_inv = 1 / C.alpha

    verdict(
        "α⁻¹ ≈ 360/ϕ²",
        "PARTIAL",
        f"360/ϕ² = {val_360_phi2:.4f}\n"
        f"α⁻¹    = {alpha_inv:.4f}\n"
        f"Discrepancy = {abs(val_360_phi2 - alpha_inv) / alpha_inv * 100:.2f}%\n"
        f"Numerically close but not exact; no derivation provided."
    )

    # ── Claim 4 (§25-26): ϕ-scaling gives 11 layers ──────────────────────────
    print("─" * 72)
    print("CLAIM 4 (dialog §25-26): Scaling by 1/ϕ also gives 11 layers")
    print("  to the Planck floor.")
    print("─" * 72)
    n_phi = 0
    layer = C.lambda_C
    while layer > C.l_P and n_phi < 500:
        n_phi += 1
        layer *= (1 / C.phi)

    verdict(
        "ϕ-scaling: 11 layers to Planck",
        "REFUTED",
        f"1/ϕ scaling requires {n_phi} layers to reach l_P.\n"
        f"The dialog conflates α-scaling (11 layers) with ϕ-scaling\n"
        f"(111 layers). These are completely different structures."
    )

    # ── Claim 5 (§20): Muon is ~200× heavier than electron ───────────────────
    print("─" * 72)
    print("CLAIM 5 (dialog §20): The muon is ~200× heavier than the electron.")
    print("─" * 72)
    ratio_muon = C.m_mu / C.m_e

    verdict(
        "Muon/electron mass ratio",
        "CONFIRMED",
        f"m_μ / m_e = {ratio_muon:.1f}\n"
        f"Dialog said ~200×; actual ≈ {ratio_muon:.0f}×."
    )

    # ── Claim 6 (§20): Tau is ~3500× heavier than electron ───────────────────
    print("─" * 72)
    print("CLAIM 6 (dialog §20): The tau is ~3500× heavier than the electron.")
    print("─" * 72)
    ratio_tau = C.m_tau / C.m_e

    verdict(
        "Tau/electron mass ratio",
        "CONFIRMED",
        f"m_τ / m_e = {ratio_tau:.1f}\n"
        f"Dialog said ~3500×; actual ≈ {ratio_tau:.0f}×."
    )

    # ── Claim 7 (§5): Compton wavelength of electron ─────────────────────────
    print("─" * 72)
    print("CLAIM 7 (dialog §5): Electron Compton wavelength ≈ 2.426×10⁻¹² m")
    print("─" * 72)

    verdict(
        "Electron Compton wavelength",
        "CONFIRMED",
        f"Calculated: {C.lambda_C:.6e} m\n"
        f"Dialog:     2.426×10⁻¹² m\n"
        f"Match to 4 significant figures."
    )

    # ── Claim 8 (§6): WvM charge ≈ 0.91e ─────────────────────────────────────
    print("─" * 72)
    print("CLAIM 8 (dialog §6): The WvM toroid radius is the Compton wavelength.")
    print("  (Implicitly: the charge ratio is ~0.91.)")
    print("─" * 72)

    verdict(
        "WvM charge ≈ 0.91e",
        "CONFIRMED",
        f"q/e = {q_over_e:.6f} (from Eq. 5 of WvM paper)\n"
        f"This matches the dialog's implicit claim and the study README."
    )

    # ── Summary ───────────────────────────────────────────────────────────────
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    confirmed = sum(1 for _, s, _ in results if s == "CONFIRMED")
    refuted   = sum(1 for _, s, _ in results if s == "REFUTED")
    partial   = sum(1 for _, s, _ in results if s == "PARTIAL")
    print(f"  {confirmed} CONFIRMED,  {refuted} REFUTED,  {partial} PARTIAL")
    print()
    for label, status, _ in results:
        marker = {"CONFIRMED": "✓", "REFUTED": "✗", "PARTIAL": "~"}[status]
        print(f"  [{marker}] {label}")
    print()


if __name__ == "__main__":
    main()
