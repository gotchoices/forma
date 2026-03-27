#!/usr/bin/env python3
"""
R17 Track 4: Centrifugal forces on the (1,2) helix.

Compute the 3D curvature, centrifugal force, and Fourier
decomposition for a photon following the (1,2) geodesic
on a torus.  Check what harmonics are present and whether
the charge integral picks up a monopole component.
"""

import sys
import os
import math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import (h, hbar, c, eps0, e, alpha, m_e, lambda_C)


def torus_helix(phi_arr, R, a):
    """
    (1,2) helix on a torus: one tube winding per two ring circuits.
    theta = phi/2.  Full path covers phi in [0, 4pi).
    Returns 3D position (x, y, z).
    """
    theta = phi_arr / 2.0
    x = (R + a * np.cos(theta)) * np.cos(phi_arr)
    y = (R + a * np.cos(theta)) * np.sin(phi_arr)
    z = a * np.sin(theta)
    return x, y, z


def compute_curvature_and_forces(R, a, N=4000):
    """
    Compute the 3D curvature vector and centrifugal force
    along the (1,2) helix.
    """
    r = a / R
    phi = np.linspace(0, 4 * np.pi, N, endpoint=False)
    dphi = phi[1] - phi[0]
    theta = phi / 2.0

    x, y, z = torus_helix(phi, R, a)
    pos = np.stack([x, y, z], axis=-1)  # (N, 3)

    # Velocity (tangent) via finite differences
    dx = np.roll(pos, -1, axis=0) - np.roll(pos, 1, axis=0)
    ds = np.linalg.norm(dx, axis=-1, keepdims=True)
    tangent = dx / ds  # unit tangent

    # Arc length element
    ds_scalar = (ds.squeeze() / 2.0)  # half because central difference

    # Acceleration (curvature vector) via second derivative
    d2x = np.roll(pos, -1, axis=0) - 2 * pos + np.roll(pos, 1, axis=0)
    ds2 = ds_scalar**2

    # Curvature vector kappa = d²r/ds²  (approx)
    # Using d²r/dphi² / (ds/dphi)² - (d²s/dphi² / (ds/dphi)³) * dr/dphi
    # Simpler: kappa_vec = (dT/ds) where T is unit tangent
    dT = np.roll(tangent, -1, axis=0) - np.roll(tangent, 1, axis=0)
    kappa_vec = dT / (2.0 * ds_scalar[:, np.newaxis])

    kappa_mag = np.linalg.norm(kappa_vec, axis=-1)
    radius_of_curvature = 1.0 / kappa_mag

    # 3D speed (in flat T² metric, the photon moves at c;
    # in 3D, the speed varies)
    # ds/dphi for the (1,2) helix:
    # v_3D = ds/dt where dt = ds_flat / c
    # ds_3D/dphi = sqrt((d/dphi)[(R+a cos(phi/2))cos phi]² + ... )
    ds_dphi_3D = ds_scalar  # already computed

    # Flat-metric speed: ds_flat/dphi
    # On flat T²: ds² = a²dtheta² + R²dphi² = (a/2)²dphi² + R²dphi²
    # ds_flat/dphi = sqrt(a²/4 + R²)
    ds_dphi_flat = np.sqrt(a**2 / 4.0 + R**2)

    v_3D = ds_dphi_3D * c / ds_dphi_flat  # 3D speed when flat speed = c

    # Centrifugal force magnitude: F = p * v / rho = (E/c) * v_3D / rho
    # where rho = radius of curvature
    E_photon = m_e * c**2
    p_photon = E_photon / c
    F_cent = p_photon * v_3D / radius_of_curvature

    # Distance from ring center (cylindrical radius)
    rho_cyl = np.sqrt(x**2 + y**2)  # = R + a cos(theta)

    # Decompose the centrifugal force into components:
    # 1. Radial (cylindrical, away from ring center)
    rhat = np.stack([x / rho_cyl, y / rho_cyl, np.zeros_like(x)], axis=-1)
    F_radial = np.sum(kappa_vec * rhat, axis=-1) * (-1) * p_photon * v_3D
    # (centrifugal is opposite to curvature direction)

    # 2. Vertical (z-direction)
    zhat = np.array([0.0, 0.0, 1.0])
    F_vertical = np.sum(kappa_vec * zhat[np.newaxis, :], axis=-1) * (-1) * p_photon * v_3D

    # 3. Azimuthal (around the ring, tangent to ring circle)
    phihat = np.stack([-np.sin(phi), np.cos(phi), np.zeros_like(phi)], axis=-1)
    F_azimuthal = np.sum(kappa_vec * phihat, axis=-1) * (-1) * p_photon * v_3D

    return {
        'phi': phi,
        'theta': theta,
        'kappa_mag': kappa_mag,
        'radius_of_curvature': radius_of_curvature,
        'v_3D': v_3D,
        'F_cent': F_cent,
        'F_radial': F_radial,
        'F_vertical': F_vertical,
        'F_azimuthal': F_azimuthal,
        'rho_cyl': rho_cyl,
        'ds_dphi_3D': ds_dphi_3D,
        'ds_dphi_flat': ds_dphi_flat,
        'x': x, 'y': y, 'z': z,
    }


def fourier_decompose(phi, f, n_max=10):
    """
    Decompose f(phi) into Fourier components on [0, 4pi).
    The (1,2) path has period 4pi, so the natural frequencies
    are half-integers: n/2 where n = 0, 1, 2, 3, ...
    
    Returns dict of {freq: (amplitude, phase)} where
    freq = n/2 (in units of 1/(2pi ring circumference)).
    """
    dphi = phi[1] - phi[0]
    N = len(phi)
    results = {}

    # DC component (n=0)
    a0 = np.mean(f)
    results[0.0] = (abs(a0), 0.0 if a0 >= 0 else np.pi)

    for n in range(1, 2 * n_max + 1):
        freq = n / 2.0  # half-integer frequencies
        cn = np.mean(f * np.cos(freq * phi))
        sn = np.mean(f * np.sin(freq * phi))
        amp = 2 * np.sqrt(cn**2 + sn**2)
        phase = np.arctan2(-sn, cn)
        if amp > 1e-15 * abs(a0 + 1e-30):
            results[freq] = (amp, phase)

    return results


def charge_integral_particle(phi, theta, R, a, charge_per_point=1.0):
    """
    In the particle picture: the photon carries charge and
    traces the (1,2) path.  The monopole charge is the integral
    of the charge density weighted by the time spent at each
    ring position.

    For a uniformly-moving particle on the path, the charge
    density at ring angle phi is proportional to 1/v_3D(phi).
    
    But the SIGN of the charge at each point depends on
    whether E points outward (WvM mechanism).  For the (1,2)
    winding with circular polarization, E always points outward
    (radially from torus surface).  So the charge at each point
    is POSITIVE.
    
    The monopole is: Q = ∫ (charge per unit phi) dphi
    """
    # The charge per unit phi is proportional to the surface
    # charge density × area element.  For a (1,2) mode:
    # sigma ∝ cos(theta + 2*phi) × (the WvM mechanism)
    #
    # Actually, in the WvM particle picture, sigma is a
    # delta function along the path, always positive (E outward).
    # The time-averaged charge density at ring angle phi
    # integrates over both passes:
    
    dphi = phi[1] - phi[0]
    N = len(phi)
    
    # Fold the 4pi path onto 2pi ring
    N_half = N // 2
    phi_ring = phi[:N_half]  # [0, 2pi)
    
    # Pass 1: phi in [0, 2pi), theta = phi/2
    # Pass 2: phi in [2pi, 4pi), same ring position, theta = phi/2
    
    # In WvM particle picture: at each path point, the charge
    # density (E pointing outward) has magnitude proportional
    # to cos(theta + 2*phi) where theta = phi/2:
    # sigma ∝ cos(phi/2 + 2*phi) = cos(5*phi/2)
    # This is the FIELD pattern, not the always-positive charge.
    #
    # WvM says E ALWAYS points outward due to commensurability.
    # But this means the charge density is |E_normal|, which is
    # always positive.  Or more precisely, E_normal = E₀ cos(0) = E₀
    # at every point (the commensurability aligns E with the normal).
    
    # Let's compute both:
    # (a) WvM: always-outward E (sigma = const along path)
    # (b) Wave: sigma = cos(theta + 2*phi) (oscillating)
    
    # Case (a): WvM always-outward
    # Charge density per unit path length is uniform.
    # Time at each ring position ∝ ds_3D/dphi.
    # Monopole = ∫ (charge per unit ring angle) dphi
    # Since the charge per unit path length is constant,
    # charge per unit phi ∝ ds_3D/dphi.
    # But we need to weight by the AREA seen from outside:
    # the E field at distance r falls as 1/r².
    # For the monopole, we just need the total charge,
    # which is e (conserved).  Not helpful for DERIVING charge.
    
    return None  # This approach can't derive charge from zero


def charge_integral_wave(R, a, N_theta=200, N_phi=200):
    """
    In the wave picture: the field pattern on the torus surface
    is cos(theta + 2*phi).  The charge integral is:
    
    Q = ∫∫ cos(theta + 2*phi) × (R + a cos theta) × a dtheta dphi
    
    We compute this for:
    (a) Perfect torus (standard area element)
    (b) Deformed torus (non-circular cross-section from
        centrifugal pressure)
    """
    theta = np.linspace(0, 2*np.pi, N_theta, endpoint=False)
    phi = np.linspace(0, 2*np.pi, N_phi, endpoint=False)
    dtheta = theta[1] - theta[0]
    dphi_grid = phi[1] - phi[0]
    
    TH, PH = np.meshgrid(theta, phi, indexing='ij')
    
    # Surface charge density from (1,2) mode
    sigma = np.cos(TH + 2 * PH)
    
    # (a) Perfect torus
    J_perfect = (R + a * np.cos(TH)) * a
    Q_perfect = np.sum(sigma * J_perfect) * dtheta * dphi_grid
    
    # (b) Deformed cross-section: rho(theta) = a(1 + eps*cos(theta))
    # This models the centrifugal deformation (denser on outside)
    # The Jacobian changes because the tube is no longer circular
    r = a / R
    eps = r / 2.0  # rough estimate of deformation magnitude
    
    a_deformed = a * (1 + eps * np.cos(TH))
    # Modified area element for deformed tube
    # (R + a_deformed cos theta) × a_deformed
    # ≈ (R + a(1+eps cos theta) cos theta) × a(1+eps cos theta)
    J_deformed = (R + a_deformed * np.cos(TH)) * a_deformed
    Q_deformed = np.sum(sigma * J_deformed) * dtheta * dphi_grid
    
    # (c) With velocity modulation: the field amplitude is
    # modulated by the inverse of the 3D speed ratio.
    # sigma_mod = sigma / (1 + r*cos(theta))  (denser where slower)
    sigma_mod = sigma / (1 + r * np.cos(TH))
    Q_velocity = np.sum(sigma_mod * J_perfect) * dtheta * dphi_grid
    
    return Q_perfect, Q_deformed, Q_velocity


def main():
    r_values = [0.25, 0.50, 1.0]
    
    print("=" * 70)
    print("R17 Track 4: Centrifugal Forces on the (1,2) Helix")
    print("=" * 70)
    
    for r in r_values:
        R = lambda_C / (2.0 * np.pi * np.sqrt(4 + r**2))
        a = r * R
        
        print()
        print(f"{'='*70}")
        print(f"Aspect ratio r = a/R = {r}")
        print(f"R = {R:.4e} m,  a = {a:.4e} m")
        print(f"{'='*70}")
        
        data = compute_curvature_and_forces(R, a)
        phi = data['phi']
        theta = data['theta']
        
        # ── Section 1: 3D speed modulation ──────────────────
        print()
        print("SECTION 1: 3D Speed Modulation")
        print("-" * 50)
        v = data['v_3D']
        print(f"  v_3D/c  min = {np.min(v)/c:.4f}")
        print(f"  v_3D/c  max = {np.max(v)/c:.4f}")
        print(f"  v_3D/c mean = {np.mean(v)/c:.4f}")
        print(f"  Modulation depth = {(np.max(v)-np.min(v))/(2*np.mean(v)):.4f}")
        print(f"  Expected: 1-r to 1+r = {1-r:.4f} to {1+r:.4f}")
        
        # ── Section 2: Curvature ────────────────────────────
        print()
        print("SECTION 2: 3D Curvature Along the Path")
        print("-" * 50)
        kappa = data['kappa_mag']
        roc = data['radius_of_curvature']
        print(f"  κ min = {np.min(kappa):.4e} m⁻¹  (ρ = {np.max(roc):.4e} m)")
        print(f"  κ max = {np.max(kappa):.4e} m⁻¹  (ρ = {np.min(roc):.4e} m)")
        print(f"  κ mean = {np.mean(kappa):.4e} m⁻¹")
        print(f"  κ_max/κ_min = {np.max(kappa)/np.min(kappa):.4f}")
        
        # ── Section 3: Centrifugal force ────────────────────
        print()
        print("SECTION 3: Centrifugal Force Components")
        print("-" * 50)
        print(f"  |F_cent| range: {np.min(data['F_cent']):.4e} to {np.max(data['F_cent']):.4e} N")
        print()
        
        for name, key in [("Radial (away from ring center)", 'F_radial'),
                          ("Vertical (z-direction)", 'F_vertical'),
                          ("Azimuthal (around the ring)", 'F_azimuthal')]:
            F = data[key]
            print(f"  {name}:")
            print(f"    Range: [{np.min(F):.4e}, {np.max(F):.4e}] N")
            print(f"    Mean:  {np.mean(F):.4e} N")
            print(f"    RMS:   {np.sqrt(np.mean(F**2)):.4e} N")
            
            # Fourier decomposition
            harmonics = fourier_decompose(phi, F)
            sorted_h = sorted(harmonics.items(),
                            key=lambda x: x[1][0], reverse=True)
            print(f"    Fourier components (top 5):")
            for freq, (amp, phase) in sorted_h[:5]:
                if freq == 0:
                    label = "DC"
                elif freq == int(freq):
                    label = f"n={int(freq)}"
                else:
                    label = f"n={freq}"
                rel = amp / (sorted_h[0][1][0] + 1e-30)
                print(f"      {label:>6s}: amp = {amp:.4e} N  "
                      f"({rel*100:6.1f}%)")
            print()
        
        # ── Section 4: Charge integrals ─────────────────────
        print()
        print("SECTION 4: Charge Integrals (Wave Picture)")
        print("-" * 50)
        Q_perf, Q_def, Q_vel = charge_integral_wave(R, a)
        
        Q_ref = e  # reference scale
        print(f"  (a) Perfect torus, cos(θ+2φ) field:")
        print(f"      Q = {Q_perf:.6e} C  (Q/e = {Q_perf/Q_ref:.6e})")
        print()
        print(f"  (b) Deformed tube (ε = r/2 = {r/2:.3f}):")
        print(f"      Q = {Q_def:.6e} C  (Q/e = {Q_def/Q_ref:.6e})")
        print()
        print(f"  (c) Velocity-modulated field:")
        print(f"      Q = {Q_vel:.6e} C  (Q/e = {Q_vel/Q_ref:.6e})")
        
        # ── Section 5: Detailed harmonic analysis ───────────
        print()
        print("SECTION 5: Harmonic Content of Curvature")
        print("-" * 50)
        print("  The curvature κ(phi) along the path contains")
        print("  harmonics at half-integer frequencies because")
        print("  the (1,2) path has period 4π in φ.")
        print()
        
        harmonics_k = fourier_decompose(phi, kappa)
        sorted_k = sorted(harmonics_k.items(),
                         key=lambda x: x[1][0], reverse=True)
        dc_amp = harmonics_k.get(0.0, (0, 0))[0]
        print(f"  Curvature κ(φ) Fourier components:")
        for freq, (amp, phase) in sorted_k[:8]:
            if freq == 0:
                label = "DC"
            elif freq == int(freq):
                label = f"n={int(freq)}"
            else:
                label = f"n={freq}"
            rel = amp / (dc_amp + 1e-30)
            print(f"    {label:>6s}: {amp:.4e} m⁻¹  ({rel*100:6.1f}% of DC)")
        
        # ── Section 6: Check for nonzero charge from ────────
        # the nonlinear metric mapping
        print()
        print("SECTION 6: Nonlinear Metric Coupling")
        print("-" * 50)
        print("  The product cos(θ+2φ) × 1/(R+a cos θ) introduces")
        print("  cross-terms.  Check if any survive the φ integral.")
        print()
        
        # On the surface, with θ and φ independent:
        N_th = 500
        N_ph = 500
        th = np.linspace(0, 2*np.pi, N_th, endpoint=False)
        ph = np.linspace(0, 2*np.pi, N_ph, endpoint=False)
        dth = th[1] - th[0]
        dph = ph[1] - ph[0]
        TH, PH = np.meshgrid(th, ph, indexing='ij')
        
        sigma_field = np.cos(TH + 2*PH)
        J_area = (R + a * np.cos(TH)) * a
        
        # The integrand
        integrand = sigma_field * J_area
        
        # φ-marginal (integrate over θ first)
        phi_marginal = np.sum(integrand, axis=0) * dth
        print(f"  φ-marginal of charge integrand:")
        print(f"    max = {np.max(phi_marginal):.6e}")
        print(f"    min = {np.min(phi_marginal):.6e}")
        print(f"    mean = {np.mean(phi_marginal):.6e}")
        print(f"    (should be ~0 if φ-symmetry holds)")
        
        # θ-marginal (integrate over φ first)
        theta_marginal = np.sum(integrand, axis=1) * dph
        print(f"  θ-marginal of charge integrand:")
        print(f"    max = {np.max(theta_marginal):.6e}")
        print(f"    min = {np.min(theta_marginal):.6e}")
        print(f"    mean = {np.mean(theta_marginal):.6e}")
        print(f"    (should be ~0 because ∫cos(2φ)dφ = 0)")
        
        # Now try with the FULL (non-separable) metric coupling.
        # sigma_effective = cos(θ+2φ) / (R + a cos θ)
        # This is what the 3D field looks like when the flat-T²
        # uniform wave maps to 3D.
        sigma_eff = np.cos(TH + 2*PH) / (R + a * np.cos(TH))
        integrand_eff = sigma_eff * J_area
        Q_eff = np.sum(integrand_eff) * dth * dph
        print()
        print(f"  Effective charge with metric coupling:")
        print(f"    Q = {Q_eff:.6e} C  (Q/e = {Q_eff/e:.6e})")
        
        # Check: does 1/(R + a cos θ) × cos(θ+2φ) × (R + a cos θ)
        # just reduce to cos(θ+2φ)?
        # Yes: the (R + a cos θ) cancels!
        integrand_cancel = np.cos(TH + 2*PH) * a
        Q_cancel = np.sum(integrand_cancel) * dth * dph
        print(f"    (Cancellation check: {Q_cancel:.6e} — should match)")
    
    # ── Summary ─────────────────────────────────────────────
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("1. The 3D speed modulation is real and large:")
    print("   v_3D oscillates between c(1-r) and c(1+r).")
    print("   For r = 0.5: speed varies from 0.5c to 1.5c.")
    print()
    print("2. The curvature of the (1,2) helix varies strongly")
    print("   along the path.  The force Fourier decomposition")
    print("   has components at half-integer frequencies (n/2)")
    print("   because the path period is 4π, not 2π.")
    print()
    print("3. ALL charge integrals give ZERO on a symmetric torus.")
    print("   The φ integral ∫cos(2φ)dφ = 0 kills the monopole")
    print("   regardless of any θ-dependent modification.")
    print("   This holds for:")
    print("   - Perfect torus")
    print("   - Deformed tube cross-section")
    print("   - Velocity-modulated field")
    print("   - Nonlinear metric coupling (1/(R+a cos θ) cancels)")
    print()
    print("4. The centrifugal force has three components:")
    print("   - Radial (away from ring center): φ-independent → no charge")
    print("   - Vertical (z): φ-independent → no charge")
    print("   - Azimuthal (along ring): this is the tangential")
    print("     acceleration/deceleration of the photon.")
    print()
    print("5. KEY QUESTION: does the azimuthal force component")
    print("   create a φ-dependent effect that survives averaging?")
    print("   The azimuthal force has the force profile shown above.")
    print("   If it modulates the photon's velocity around the ring")
    print("   in a way that breaks the two-pass cancellation,")
    print("   charge could emerge.  But on a symmetric torus,")
    print("   the two-pass cancellation appears exact.")
    print()
    print("CONCLUSION: On a symmetric torus, the centrifugal")
    print("deformation (tube or ring) preserves the φ-rotational")
    print("symmetry.  The monopole charge integral is exactly zero")
    print("regardless of the deformation magnitude.  To generate")
    print("charge, the φ-symmetry itself must be broken.")


if __name__ == '__main__':
    main()
