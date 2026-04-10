"""
R52 Track 4f: Model-D parameters with cross-sheet shear σ_ep.

Tracks 4d and 4e showed that the shear-induced sign rule
mechanism exists but that MaSt's WITHIN-PLANE shear
(s = solve_shear_for_alpha(ε)) is ~30% below the sign-flip
window at model-D's working ε values:

  ε_e = 0.65 → s_e = 0.0959 (window 0.152, gap -0.056)
  ε_p = 0.55 → s_p = 0.1110 (window 0.167, gap -0.056)

The gap is identical for both particles (~0.056 in shear) — a
structural feature, not particle-specific.

This track adds the missing ingredient: model-D's CROSS-SHEET
shear σ_ep = -0.13.  Tracks 4d/4e completely ignored σ_ep.
The magnitude |σ_ep| = 0.13 is more than enough to close the
0.056 gap if it adds (with the right sign and weighting) to
the within-plane shear.

This track also tests BOTH proton mode interpretations:
  - (1,3): leading candidate per model-D
  - (3,6): viable alternative; consistent with flux
    quantization formula (Q114)

Both interpretations use ε_p = 0.55 (model-D working value).
Different mode topology means different (n_tube, n_ring) and
therefore different sign-rule predictions.

PHYSICAL MOTIVATION:
- Model-D includes σ_ep as a real physical shear coupling
  between the electron and proton sheets (R50 T2)
- The within-plane shear (s_e or s_p) is computed by
  solve_shear_for_alpha to give α at the chosen ε
- σ_ep is an additional shear that the lib does NOT include
  in solve_shear_for_alpha — it's a cross-sheet coupling
  that affects how the wave on one sheet "sees" the other
- The combined effective shear is what the calculation should
  use

WAVE CONSTRUCTION:
For a (n_tube, n_ring) standing wave with within-plane shear
s and cross-sheet shear σ:
  ψ(θ_t, θ_r) = cos(n_tube × θ_t) × cos((n_ring - s_eff) × θ_r)

where s_eff = s + σ × weight.  The exact weighting depends on
how σ_ep enters the proton sheet wave equation.  We test
several weights to bracket the result.

ASSUMPTIONS (frozen for this track):
- Model-D: ε_e = 0.65, ε_p = 0.55, σ_ep = -0.13
- Within-plane shears from solve_shear_for_alpha
- Test BOTH (1,3) and (3,6) proton mode interpretations
- s_eff = s_within_plane + α × σ_ep where α is a weight
  in [0, 1]; sweep α to bracket the result
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from lib.ma_model_d import solve_shear_for_alpha, solve_shear_for_alpha_signed


# Model-D working values
EPSILON_E = 0.65
EPSILON_P = 0.55
SIGMA_EP = -0.13


# ── Surface discretization ─────────────────────────────────────────

def torus_grid(R, a, n_tube_cells, n_ring_cells):
    theta_tube = (np.arange(n_tube_cells) + 0.5) * (2 * np.pi / n_tube_cells)
    theta_ring = (np.arange(n_ring_cells) + 0.5) * (2 * np.pi / n_ring_cells)
    tt, tr = np.meshgrid(theta_tube, theta_ring, indexing='ij')
    cos_t, sin_t = np.cos(tt), np.sin(tt)
    cos_r, sin_r = np.cos(tr), np.sin(tr)
    rho = R + a * cos_t
    x = rho * cos_r
    y = rho * sin_r
    z = a * sin_t
    pos = np.stack([x, y, z], axis=-1)
    dtheta_t = 2 * np.pi / n_tube_cells
    dtheta_r = 2 * np.pi / n_ring_cells
    dA = a * rho * dtheta_t * dtheta_r
    return pos, dA, theta_tube, theta_ring


def signed_charge_density(theta_tube, theta_ring, n_tube, n_ring, shear_eff):
    """ψ(θ_t, θ_r) = cos(n_tube × θ_t) × cos((n_ring - shear_eff) × θ_r)"""
    tt, tr = np.meshgrid(theta_tube, theta_ring, indexing='ij')
    return np.cos(n_tube * tt) * np.cos((n_ring - shear_eff) * tr)


# ── Self-energy ─────────────────────────────────────────────────────

def coulomb_self_energy(pos, charge, eps):
    diff = pos[:, None, :] - pos[None, :, :]
    dist = np.linalg.norm(diff, axis=-1)
    np.fill_diagonal(dist, np.inf)
    dist = np.maximum(dist, eps)
    qq = charge[:, None] * charge[None, :]
    return 0.5 * np.sum(qq / dist)


def compute_U(R, a, n_tube, n_ring, shear_eff, n_tube_cells=24, n_ring_cells=48,
              eps_factor=0.5):
    pos, dA, tt, tr = torus_grid(R, a, n_tube_cells, n_ring_cells)
    psi = signed_charge_density(tt, tr, n_tube, n_ring, shear_eff)
    charge = (psi * dA).flatten()
    pos_flat = pos.reshape(-1, 3)
    mean_cell_size = np.sqrt(dA.mean())
    eps = eps_factor * mean_cell_size
    return coulomb_self_energy(pos_flat, charge, eps)


# ── Sign rule test for one mode ─────────────────────────────────────

def test_mode(epsilon, n_tube, n_ring, label, R=1.0, n_tube_cells=24, n_ring_cells=48):
    """
    For a given mode and aspect ratio, scan effective shear and find
    where δU changes sign.
    """
    a = epsilon * R
    s_within = solve_shear_for_alpha(epsilon)

    print(f"\n  ── {label} ──")
    print(f"    ε = {epsilon}")
    print(f"    Mode: ({n_tube}, {n_ring})")
    print(f"    Within-plane MaSt shear: s = {s_within:.4f}")

    U0 = compute_U(R, a, n_tube, n_ring, 0.0, n_tube_cells, n_ring_cells)

    # Scan effective shear from 0 to 0.30
    s_values = np.linspace(0.0, 0.30, 31)
    dU_values = np.zeros(len(s_values))
    for i, s in enumerate(s_values):
        U = compute_U(R, a, n_tube, n_ring, s, n_tube_cells, n_ring_cells)
        dU_values[i] = U - U0

    # Find sign-flip threshold (smallest s where dU changes sign)
    s_flip = None
    initial_sign = np.sign(dU_values[1])  # at first nonzero point
    for i in range(2, len(s_values)):
        if np.sign(dU_values[i]) != initial_sign and np.sign(dU_values[i]) != 0:
            s_flip = s_values[i]
            break

    s_str = f"{s_flip:.4f}" if s_flip else ">0.30"
    print(f"    Sign-flip threshold: s_eff = {s_str}")
    print(f"    δU at s_within = {compute_U(R, a, n_tube, n_ring, s_within) - U0:+.4f}")
    print(f"    δU at s_within + |σ_ep| = {compute_U(R, a, n_tube, n_ring, s_within + abs(SIGMA_EP)) - U0:+.4f}")
    print(f"    δU at s_within - |σ_ep| = {compute_U(R, a, n_tube, n_ring, s_within - abs(SIGMA_EP)) - U0:+.4f}")

    return s_within, s_flip, s_values, dU_values


# ── Main ───────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("R52 Track 4f: Model-D + cross-sheet shear σ_ep")
    print("=" * 70)
    print(__doc__)

    print(f"\nModel-D working values:")
    print(f"  ε_e = {EPSILON_E}")
    print(f"  ε_p = {EPSILON_P}")
    print(f"  σ_ep = {SIGMA_EP}")

    print(f"\n{'=' * 70}")
    print("PART 1: Electron sheet (1,2) at ε_e = 0.65")
    print(f"{'=' * 70}")
    s_e, sflip_e, sv_e, dU_e = test_mode(EPSILON_E, 1, 2, "Electron (1,2)")

    print(f"\n{'=' * 70}")
    print("PART 2: Proton sheet — TWO MODE INTERPRETATIONS")
    print(f"{'=' * 70}")

    print(f"\n--- Interpretation A: (1,3) ---")
    s_p13, sflip_p13, sv_p13, dU_p13 = test_mode(EPSILON_P, 1, 3, "Proton (1,3)")

    print(f"\n--- Interpretation B: (3,6) ---")
    s_p36, sflip_p36, sv_p36, dU_p36 = test_mode(EPSILON_P, 3, 6, "Proton (3,6)")

    print(f"\n{'=' * 70}")
    print("PART 3: Sign test with σ_ep included as effective shear")
    print(f"{'=' * 70}")

    # Sweep weight α from 0 to 1: s_eff = s_within + α × σ_ep
    # σ_ep is negative (-0.13), so positive α means subtractive
    weights = [0.0, 0.25, 0.5, 0.75, 1.0]

    print(f"\n  ── Electron (1,2) at ε_e = {EPSILON_E} ──")
    print(f"  s_within = {s_e:.4f}")
    print(f"  Sign-flip threshold: s_eff > {sflip_e if sflip_e else '>0.30'}")
    print()
    print(f"  {'weight':>8s}  {'s_eff':>10s}  {'δU(1,2)':>14s}  {'sign':>6s}")
    print("  " + "─" * 50)
    a = EPSILON_E
    U0 = compute_U(1.0, a, 1, 2, 0.0)
    for w in weights:
        s_eff = s_e + w * SIGMA_EP  # σ_ep is negative
        U = compute_U(1.0, a, 1, 2, s_eff)
        dU = U - U0
        sign = '+' if dU > 0 else '-'
        print(f"  {w:8.2f}  {s_eff:10.4f}  {dU:+14.4f}  {sign:>6s}")
    # Also try s_eff = s_e + |σ_ep| (positive direction)
    print(f"\n  Alternative: s_eff = s_within + |σ_ep|")
    s_eff_pos = s_e + abs(SIGMA_EP)
    U_pos = compute_U(1.0, a, 1, 2, s_eff_pos)
    dU_pos = U_pos - U0
    print(f"  s_eff = {s_eff_pos:.4f}, δU = {dU_pos:+.4f}, sign = {'+' if dU_pos > 0 else '-'}")

    print(f"\n  ── Proton (1,3) at ε_p = {EPSILON_P} ──")
    print(f"  s_within = {s_p13:.4f}")
    print(f"  Sign-flip threshold: s_eff > {sflip_p13 if sflip_p13 else '>0.30'}")
    print()
    print(f"  {'weight':>8s}  {'s_eff':>10s}  {'δU(1,3)':>14s}  {'sign':>6s}")
    print("  " + "─" * 50)
    a = EPSILON_P
    U0_13 = compute_U(1.0, a, 1, 3, 0.0)
    for w in weights:
        s_eff = s_p13 + w * SIGMA_EP
        U = compute_U(1.0, a, 1, 3, s_eff)
        dU = U - U0_13
        sign = '+' if dU > 0 else '-'
        print(f"  {w:8.2f}  {s_eff:10.4f}  {dU:+14.4f}  {sign:>6s}")
    print(f"\n  Alternative: s_eff = s_within + |σ_ep|")
    s_eff_pos = s_p13 + abs(SIGMA_EP)
    U_pos = compute_U(1.0, a, 1, 3, s_eff_pos)
    dU_pos = U_pos - U0_13
    print(f"  s_eff = {s_eff_pos:.4f}, δU = {dU_pos:+.4f}, sign = {'+' if dU_pos > 0 else '-'}")

    print(f"\n  ── Proton (3,6) at ε_p = {EPSILON_P} ──")
    print(f"  s_within = {s_p36:.4f}")
    print(f"  Sign-flip threshold: s_eff > {sflip_p36 if sflip_p36 else '>0.30'}")
    print()
    print(f"  {'weight':>8s}  {'s_eff':>10s}  {'δU(3,6)':>14s}  {'sign':>6s}")
    print("  " + "─" * 50)
    U0_36 = compute_U(1.0, a, 3, 6, 0.0)
    for w in weights:
        s_eff = s_p36 + w * SIGMA_EP
        U = compute_U(1.0, a, 3, 6, s_eff)
        dU = U - U0_36
        sign = '+' if dU > 0 else '-'
        print(f"  {w:8.2f}  {s_eff:10.4f}  {dU:+14.4f}  {sign:>6s}")
    print(f"\n  Alternative: s_eff = s_within + |σ_ep|")
    s_eff_pos = s_p36 + abs(SIGMA_EP)
    U_pos = compute_U(1.0, a, 3, 6, s_eff_pos)
    dU_pos = U_pos - U0_36
    print(f"  s_eff = {s_eff_pos:.4f}, δU = {dU_pos:+.4f}, sign = {'+' if dU_pos > 0 else '-'}")

    # ── Plot ──
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    ax = axes[0]
    ax.plot(sv_e, dU_e, 'b-o', markersize=4, label='δU(1,2)')
    ax.axhline(0, color='k', linestyle='--', alpha=0.3)
    ax.axvline(s_e, color='g', linestyle=':', label=f's_within = {s_e:.3f}')
    ax.axvline(s_e + abs(SIGMA_EP), color='r', linestyle=':',
               label=f's + |σ_ep| = {s_e + abs(SIGMA_EP):.3f}')
    ax.set_xlabel('Effective shear s')
    ax.set_ylabel('δU')
    ax.set_title(f'Electron (1,2) at ε = {EPSILON_E}')
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axes[1]
    ax.plot(sv_p13, dU_p13, 'r-^', markersize=4, label='δU(1,3)')
    ax.axhline(0, color='k', linestyle='--', alpha=0.3)
    ax.axvline(s_p13, color='g', linestyle=':', label=f's_within = {s_p13:.3f}')
    ax.axvline(s_p13 + abs(SIGMA_EP), color='r', linestyle=':',
               label=f's + |σ_ep| = {s_p13 + abs(SIGMA_EP):.3f}')
    ax.set_xlabel('Effective shear s')
    ax.set_ylabel('δU')
    ax.set_title(f'Proton (1,3) at ε = {EPSILON_P}')
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axes[2]
    ax.plot(sv_p36, dU_p36, 'm-^', markersize=4, label='δU(3,6)')
    ax.axhline(0, color='k', linestyle='--', alpha=0.3)
    ax.axvline(s_p36, color='g', linestyle=':', label=f's_within = {s_p36:.3f}')
    ax.axvline(s_p36 + abs(SIGMA_EP), color='r', linestyle=':',
               label=f's + |σ_ep| = {s_p36 + abs(SIGMA_EP):.3f}')
    ax.set_xlabel('Effective shear s')
    ax.set_ylabel('δU')
    ax.set_title(f'Proton (3,6) at ε = {EPSILON_P}')
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    out = Path(__file__).parent.parent / "track4f_results.png"
    plt.savefig(out, dpi=120)
    print(f"\n  Plot saved to {out}")

    # ── Final summary ──
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"""
Model-D parameters: ε_e = {EPSILON_E}, ε_p = {EPSILON_P}, σ_ep = {SIGMA_EP}

For the predicted sign pattern (electron δU > 0, proton δU < 0
relative to bare):

| Mode | s_within | s + |σ_ep| | δU at s + |σ_ep| | Crosses window? |
|------|----------|-----------|-----------------|-----------------|
""")
    for label, eps, n_t, n_r, s in [
        ("Electron (1,2)", EPSILON_E, 1, 2, s_e),
        ("Proton (1,3)",   EPSILON_P, 1, 3, s_p13),
        ("Proton (3,6)",   EPSILON_P, 3, 6, s_p36),
    ]:
        a = eps
        U0 = compute_U(1.0, a, n_t, n_r, 0.0)
        s_eff = s + abs(SIGMA_EP)
        U = compute_U(1.0, a, n_t, n_r, s_eff)
        dU = U - U0
        sign = '+' if dU > 0 else '-'
        print(f"  {label:15s}  s={s:.4f}  s+|σ|={s_eff:.4f}  δU={dU:+8.4f}  sign={sign}")


if __name__ == "__main__":
    main()
