#!/usr/bin/env python3
"""
R17 Track 5: Wavepacket evolution under centrifugal forces.

Two effects of centrifugal force on a wavepacket traversing
the (1,2) helix:

A. WIDTH BREATHING — the 3D arc length per unit φ varies,
   so the wavepacket's 3D extent oscillates as it circulates.
   We prove the net magnification per circuit is exactly 1.

B. PATH DEFLECTION — the centrifugal force perpendicular to
   the geodesic (on the torus surface) would, if applied as
   an external force, deflect the path from θ = φ/2.  We
   compute this hypothetical deflection, check its Fourier
   content, and evaluate the effect on the charge integral.
"""

import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha as alpha_em, m_e, lambda_C


def track5(R, a, N=8000):
    r = a / R
    phi = np.linspace(0, 4 * np.pi, N, endpoint=False)
    dphi = phi[1] - phi[0]
    theta = phi / 2.0
    rho = R + a * np.cos(theta)

    # ── Surface basis vectors (unit, in 3D) ─────────────────
    e_th = np.stack([
        -np.sin(theta) * np.cos(phi),
        -np.sin(theta) * np.sin(phi),
        np.cos(theta),
    ], axis=-1)

    e_ph = np.stack([
        -np.sin(phi),
        np.cos(phi),
        np.zeros_like(phi),
    ], axis=-1)

    n_hat = np.stack([
        np.cos(theta) * np.cos(phi),
        np.cos(theta) * np.sin(phi),
        np.sin(theta),
    ], axis=-1)

    # ── Velocity / arc-length element ───────────────────────
    # dr/dφ = (a/2)ê_θ + ρ ê_φ   (exact, for θ = φ/2)
    v3 = (a / 2.0) * e_th + rho[:, None] * e_ph
    S = np.linalg.norm(v3, axis=-1)          # ds_3D / dφ
    v_hat = v3 / S[:, None]

    S_flat = np.sqrt((a / 2.0)**2 + R**2)    # ds_flat / dφ (constant)

    # ── Perpendicular direction on surface: ê_⊥ = n̂ × v̂ ───
    e_perp = np.cross(n_hat, v_hat)
    e_perp /= np.linalg.norm(e_perp, axis=-1, keepdims=True)

    # ── Curvature vector κ = dT̂/ds ─────────────────────────
    dv_hat = np.gradient(v_hat, dphi, axis=0)
    kappa_vec = dv_hat / S[:, None]
    kappa_mag = np.linalg.norm(kappa_vec, axis=-1)

    # ── Centrifugal force (away from centre of curvature) ───
    E_ph = m_e * c**2
    F_cent = -E_ph * kappa_vec

    # ── Decompose onto surface ──────────────────────────────
    F_n  = np.einsum('ij,ij->i', F_cent, n_hat)       # normal
    F_s  = F_cent - F_n[:, None] * n_hat               # surface tangential
    F_al = np.einsum('ij,ij->i', F_s, v_hat)           # along path
    F_pp = np.einsum('ij,ij->i', F_s, e_perp)          # ⊥ path, on surface

    F_tot = np.linalg.norm(F_cent, axis=-1)

    # ================================================================
    print(f"\n{'='*65}")
    print(f"  r = {r:.2f}   R = {R:.4e} m   a = {a:.4e} m")
    print(f"{'='*65}")

    # ── SECTION 1: Force decomposition ──────────────────────
    print(f"\nSECTION 1  Force Decomposition on Torus Surface")
    print("-" * 55)

    rms = lambda x: np.sqrt(np.mean(x**2))

    print(f"  |F_total|    RMS = {rms(F_tot):.4e} N")
    print(f"  |F_normal|   RMS = {rms(F_n):.4e} N  "
          f"({rms(F_n)/rms(F_tot)*100:5.1f}%)")
    print(f"  |F_along|    RMS = {rms(F_al):.4e} N  "
          f"({rms(F_al)/rms(F_tot)*100:5.1f}%)")
    print(f"  |F_perp|     RMS = {rms(F_pp):.4e} N  "
          f"({rms(F_pp)/rms(F_tot)*100:5.1f}%)")
    print(f"  F_along max / F_total RMS = "
          f"{np.max(np.abs(F_al))/rms(F_tot):.2e} (should be ~0)")

    # Fourier content of F_perp
    print(f"\n  F_perp Fourier content (half-integer harmonics):")
    pp_rms = rms(F_pp)
    for k in range(11):
        freq = k / 2.0
        if freq == 0:
            amp = abs(np.mean(F_pp))
        else:
            cn = 2 * np.mean(F_pp * np.cos(freq * phi))
            sn = 2 * np.mean(F_pp * np.sin(freq * phi))
            amp = np.sqrt(cn**2 + sn**2)
        if amp > 0.005 * pp_rms:
            lab = "DC" if freq == 0 else (
                f"n={int(freq)}" if freq == int(freq) else f"n={freq}")
            print(f"    {lab:>6s}: {amp:.4e} N  ({amp/pp_rms*100:5.1f}% of RMS)")

    # ── SECTION 2: Width breathing ──────────────────────────
    print(f"\nSECTION 2  Width Breathing (3D Extent)")
    print("-" * 55)

    S_outer = np.sqrt((a / 2)**2 + (R + a)**2)
    S_inner = np.sqrt((a / 2)**2 + (R - a)**2)
    br = S_outer / S_inner

    print(f"  ds/dφ  outer equator: {S_outer:.4e} m")
    print(f"  ds/dφ  inner equator: {S_inner:.4e} m")
    print(f"  Ratio (3D width outer / inner): {br:.4f}")
    print(f"  → Packet is {br:.2f}× wider at the outer equator in 3D")

    # σ_φ is constant in flat T², so σ_3D(φ) = σ_φ × S(φ)
    # Net magnification after one circuit:
    print(f"\n  Net σ_φ magnification per circuit:")
    print(f"    S(4π)/S(0) = {S[-1]/S[0]:.12f}  (should be 1.000…)")
    print(f"    Proof: S depends on cos(φ/2) which has period 4π,")
    print(f"    so S(4π) = S(0) identically.  σ_φ is conserved.")

    # Show profile at key tube positions
    i1, i2, i3 = N // 4, N // 2, 3 * N // 4
    print(f"\n  σ_3D / σ_3D(outer) at key tube positions:")
    print(f"    θ = 0    (outer):  {S[0]/S[0]:.4f}")
    print(f"    θ = π/2  (top):    {S[i1]/S[0]:.4f}")
    print(f"    θ = π    (inner):  {S[i2]/S[0]:.4f}")
    print(f"    θ = 3π/2 (bottom): {S[i3]/S[0]:.4f}")

    # ── SECTION 3: Hypothetical path deflection ─────────────
    print(f"\nSECTION 3  Hypothetical Path Deflection")
    print("-" * 55)
    print(f"  (What IF the centrifugal ⊥ force deflected the path?)")

    # dψ/ds = F_perp / E  →  dψ/dφ = (F_perp / E) × S
    f_drv = (F_pp / E_ph) * S                # angular drive, rad per dφ

    total_impulse = np.sum(f_drv) * dphi
    print(f"\n  Total angular impulse ∫(F⊥/E)ds = {total_impulse:.4e} rad")

    # Enforce zero-mean for periodic ψ
    f_drv -= np.mean(f_drv)
    psi_raw = np.cumsum(f_drv) * dphi

    # Choose ψ₀ so δ is periodic:  ψ₀ = −∫ψ_raw·S dφ / ∫S dφ
    psi0 = -np.sum(psi_raw * S) * dphi / (np.sum(S) * dphi)
    psi = psi_raw + psi0

    # Transverse displacement δ(φ) in 3D metres
    delta = np.cumsum(psi * S) * dphi
    delta -= delta[0]

    # Convert to tube-angle deviation Δθ
    # ê_⊥ ≈ (ρ/S) ê_θ + …  →  Δθ = δ × (ρ / S) / a  (approximately)
    proj_theta = rho / S          # ê_⊥ · ê_θ  (from n̂×v̂ decomposition)
    delta_theta = delta * proj_theta / a

    print(f"\n  Deflection amplitude:")
    print(f"    ψ   max = {np.max(np.abs(psi)):.4f} rad  "
          f"({np.max(np.abs(psi))*180/np.pi:.1f}°)")
    print(f"    δ   max = {np.max(np.abs(delta)):.4e} m  "
          f"({np.max(np.abs(delta))/a:.4f} tube radii)")
    print(f"    Δθ  max = {np.max(np.abs(delta_theta)):.4f} rad  "
          f"({np.max(np.abs(delta_theta))*180/np.pi:.1f}°)")

    # Periodicity check
    delta_end = delta[-1] + psi[-1] * S[-1] * dphi
    print(f"    δ periodicity: δ(4π)−δ(0) = {delta_end - delta[0]:.4e} m")

    # Fourier decomposition of Δθ
    dt_max = np.max(np.abs(delta_theta)) + 1e-30
    print(f"\n  Δθ(φ) Fourier content:")
    for k in range(11):
        freq = k / 2.0
        if freq == 0:
            amp = abs(np.mean(delta_theta))
        else:
            cn = 2 * np.mean(delta_theta * np.cos(freq * phi))
            sn = 2 * np.mean(delta_theta * np.sin(freq * phi))
            amp = np.sqrt(cn**2 + sn**2)
        if amp > 0.005 * dt_max:
            lab = "DC" if freq == 0 else (
                f"n={int(freq)}" if freq == int(freq) else f"n={freq}")
            print(f"    {lab:>6s}: {amp:.4f} rad  ({amp/dt_max*100:5.1f}%)")

    # Two-pass comparison
    N2 = N // 2
    dt1 = delta_theta[:N2]
    dt2 = delta_theta[N2:]
    asym = np.max(np.abs(dt1 - dt2))
    print(f"\n  Two-pass asymmetry:")
    print(f"    |Δθ_pass1 − Δθ_pass2|  max = {asym:.4f} rad")
    print(f"    (Non-zero → the deflection breaks two-pass cancellation)")

    # ── SECTION 4: Charge integrals ─────────────────────────
    print(f"\nSECTION 4  Charge Integrals")
    print("-" * 55)

    # (a) Delocalized wave on deflected path
    # Fold onto 2π ring; two passes contribute at each ring position
    phi_r = phi[:N2]
    th1_u = phi_r / 2.0
    th2_u = phi_r / 2.0 + np.pi
    th1_d = phi_r / 2.0 + delta_theta[:N2]
    th2_d = phi_r / 2.0 + np.pi + delta_theta[N2:]

    q_und = (np.cos(th1_u + 2 * phi_r) * (R + a * np.cos(th1_u)) +
             np.cos(th2_u + 2 * phi_r) * (R + a * np.cos(th2_u))) * a
    q_def = (np.cos(th1_d + 2 * phi_r) * (R + a * np.cos(th1_d)) +
             np.cos(th2_d + 2 * phi_r) * (R + a * np.cos(th2_d))) * a
    Q_und = np.sum(q_und) * dphi
    Q_def = np.sum(q_def) * dphi

    print(f"\n  (a) Fully delocalized wave:")
    print(f"      Undeflected Q/e = {Q_und/e:+.4e}")
    print(f"      Deflected   Q/e = {Q_def/e:+.4e}")
    if abs(Q_def) > 1e-25:
        alpha_d = Q_def**2 / (4 * np.pi * eps0 * hbar * c)
        print(f"      → α_deflected = {alpha_d:.4e}")
    else:
        print(f"      → Both zero (numerical noise)")

    # (b) Localized wavepacket — compare RMS charge
    print(f"\n  (b) Localized wavepacket — Q²_rms comparison:")
    print(f"      {'σ':>6s}  {'Q²_und':>13s}  {'Q²_def':>13s}"
          f"  {'ratio':>7s}  {'note':>10s}")

    sigma_vals = [0.5, 0.8, 1.0, 1.109, 1.5, 2.0, 3.0]
    n_samp = 200
    for sig in sigma_vals:
        Q2u = 0.0
        Q2d = 0.0
        for i in range(n_samp):
            p0 = i * 4 * np.pi / n_samp
            env = np.exp(-(phi - p0)**2 / sig**2)

            phase_u = 5 * phi / 2.0
            jac_u   = (R + a * np.cos(phi / 2.0)) * a
            qu = np.sum(env * np.cos(phase_u) * jac_u) * dphi
            Q2u += qu**2

            th_d    = phi / 2.0 + delta_theta
            phase_d = th_d + 2 * phi
            jac_d   = (R + a * np.cos(th_d)) * a
            qd = np.sum(env * np.cos(phase_d) * jac_d) * dphi
            Q2d += qd**2

        Q2u /= n_samp
        Q2d /= n_samp
        ratio = Q2d / Q2u if Q2u > 1e-60 else float('nan')
        note = "← α=1/137" if abs(sig - 1.109) < 0.01 else ""
        print(f"      {sig:6.3f}  {Q2u:13.4e}  {Q2d:13.4e}"
              f"  {ratio:7.4f}  {note:>10s}")

    return {
        'phi': phi, 'theta': theta,
        'F_n': F_n, 'F_al': F_al, 'F_pp': F_pp,
        'S': S, 'breathing': br,
        'delta_theta': delta_theta, 'psi': psi,
    }


def main():
    print("=" * 65)
    print("R17 Track 5: Wavepacket Evolution Under Centrifugal Forces")
    print("=" * 65)

    for r_val in [0.25, 0.50]:
        R = lambda_C / (2 * np.pi * np.sqrt(4 + r_val**2))
        a = r_val * R
        track5(R, a)

    # ── SUMMARY ─────────────────────────────────────────────
    print(f"\n{'='*65}")
    print("SUMMARY")
    print("=" * 65)
    print("""
1. FORCE DECOMPOSITION
   The centrifugal force on the torus surface splits roughly
   equally between two orthogonal directions:
   - Normal to surface:     ~64-70%  (pushes field into 3D)
   - ⊥ to path on surface:  ~72-77%  (would deflect the path)
   - Along the path:         ~0%     (F ⊥ v exactly)
   (Percentages are of total RMS; they add in quadrature.)

   The along-path component is zero because the centrifugal
   force is perpendicular to v.  This rigorously kills any
   direct clumping/stretching from centrifugal force.

   The ⊥ component is dominated by the n = 1/2 harmonic.

2. WIDTH BREATHING
   The 3D wavepacket extent oscillates as the packet circulates:
   wider at the outer equator, narrower at the inner equator.
   The breathing ratio is S_outer/S_inner ≈ (1+r)/(1-r).

   The net magnification per circuit is EXACTLY 1 because
   S(φ) = sqrt(a²/4 + (R+a cos φ/2)²) is periodic with
   period 4π.  In the flat-T² metric, σ_φ is constant.

   ⇒ No net clumping from the velocity gradient.

3. HYPOTHETICAL DEFLECTION
   Solving dψ/ds = F⊥/E with periodic BCs gives an enormous
   hypothetical deflection (Δθ ≈ 8-16 rad — multiple full
   tube rotations!) because the centrifugal force at the
   Compton scale is ~0.5 N.

   The deflection is dominated by the n = 1/2 harmonic.
   The two passes get DIFFERENT Δθ values, which would
   break the two-pass cancellation — but the deflection
   doesn't physically occur (see interpretation).

4. CHARGE INTEGRALS
   - Delocalized wave: charge remains ~0 even with the
     hypothetical deflection.
   - Localized wavepacket: the deflection scrambles the
     phase (cos(5φ/2 + Δθ) with Δθ ~ 8 rad wraps many
     times), so the "deflected charge" is not physically
     meaningful — it's an artifact of applying the huge
     force as an external perturbation.

5. INTERPRETATION
   The centrifugal force is a CONSEQUENCE of the confinement,
   not an external perturbation.  The photon follows the flat-T²
   geodesic; the 3D curvature is already accounted for in the
   electron mass.

   The enormous magnitude of the hypothetical deflection
   (many full rotations around the tube) confirms that the
   centrifugal force equals the confinement force — they are
   the SAME force viewed from two frames (Newton's 3rd law
   for the compact-space embedding).

   F ⊥ v kills clumping; σ_φ = const kills breathing.
   The centrifugal force cannot determine σ at the classical
   level because it creates no σ-dependent potential in the
   flat-T² dynamics.
""")


if __name__ == '__main__':
    main()
