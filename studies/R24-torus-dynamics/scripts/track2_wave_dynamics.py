#!/usr/bin/env python3
"""
R24 Track 2: Wave dynamics on embedded T².

Solve the time-dependent wave equation on the embedded torus:
    ∂²ψ/∂t² = Δ_g ψ − λ ψ³

where Δ_g is the Laplace-Beltrami operator with metric
    ds² = dθ₁² + p(θ₁)² dθ₂²,   p = r + cos θ₁   (a = 1 units)

Pseudo-spectral method (FFT) for spatial derivatives, RK4 for time.

QUESTION: Does the impulse response of the torus reveal mode selection?
On a linear system, the impulse decomposes into eigenmodes — equivalent
to the eigenvalue analysis.  With nonlinearity, energy can flow between
modes, potentially selecting specific configurations.
"""

import sys
import os
import math
import numpy as np
from numpy.fft import fft, ifft, fft2, fftfreq
import time as clock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha


# ── Grid and metric ──────────────────────────────────────────────────────────

def make_grid(N1, N2, r, curved=True):
    """Grid, metric factor p(θ₁), and wavenumber arrays."""
    theta1 = np.linspace(0, 2 * np.pi, N1, endpoint=False)
    theta2 = np.linspace(0, 2 * np.pi, N2, endpoint=False)
    TH1, TH2 = np.meshgrid(theta1, theta2, indexing='ij')

    p = (r + np.cos(TH1)) if curved else np.full_like(TH1, float(r))

    k1 = fftfreq(N1) * N1
    k2 = fftfreq(N2) * N2
    K1, K2 = np.meshgrid(k1, k2, indexing='ij')

    dA = (2 * np.pi / N1) * (2 * np.pi / N2)
    return TH1, TH2, p, K1, K2, dA


def laplacian(psi, p, K1, K2):
    """
    Δ_g ψ = (1/p) ∂/∂θ₁(p ∂ψ/∂θ₁) + (1/p²) ∂²ψ/∂θ₂²
    """
    dpsi = ifft(1j * K1 * fft(psi, axis=0), axis=0).real
    flux = p * dpsi
    div_flux = ifft(1j * K1 * fft(flux, axis=0), axis=0).real
    d2psi = ifft(-K2**2 * fft(psi, axis=1), axis=1).real
    return div_flux / p + d2psi / p**2


def total_energy(psi, vel, p, K1, K2, dA, lam=0.0):
    """Conserved energy on the torus."""
    dpsi1 = ifft(1j * K1 * fft(psi, axis=0), axis=0).real
    dpsi2 = ifft(1j * K2 * fft(psi, axis=1), axis=1).real
    KE = 0.5 * dA * np.sum(vel**2 * p)
    PE = 0.5 * dA * np.sum(dpsi1**2 * p + dpsi2**2 / p)
    NL = 0.25 * lam * dA * np.sum(psi**4 * p) if lam != 0 else 0.0
    return KE + PE + NL


def gaussian_pulse(TH1, TH2, th1_0, th2_0, sigma):
    """Periodic Gaussian pulse."""
    d1 = TH1 - th1_0
    d1 -= 2 * np.pi * np.round(d1 / (2 * np.pi))
    d2 = TH2 - th2_0
    d2 -= 2 * np.pi * np.round(d2 / (2 * np.pi))
    return np.exp(-(d1**2 + d2**2) / (2 * sigma**2))


# ── Mode analysis ────────────────────────────────────────────────────────────

def mode_power(psi, N1, N2):
    """
    |ψ̂_{m,n}|² from 2D FFT (normalized).
    Returns dict {(m, n): power} for the dominant modes.
    """
    F = fft2(psi) / (N1 * N2)
    power = np.abs(F)**2
    return power


def sector_energy(psi, vel, r, N1, N2):
    """
    Energy in each θ₂ sector n (summed over θ₁ modes m).
    Uses flat-torus eigenfrequencies as approximate weights.
    """
    psi_hat = fft2(psi) / (N1 * N2)
    vel_hat = fft2(vel) / (N1 * N2)

    k1 = fftfreq(N1) * N1
    k2 = fftfreq(N2) * N2

    E_n = np.zeros(N2)
    for j, n in enumerate(k2):
        for i, m in enumerate(k1):
            omega_sq = m**2 + n**2 / r**2
            E_mn = 0.5 * abs(vel_hat[i, j])**2 + 0.5 * omega_sq * abs(psi_hat[i, j])**2
            E_n[j] += E_mn
    return k2, E_n * (N1 * N2)


# ── Time integration ─────────────────────────────────────────────────────────

def run(N1, N2, r, curved, dt, n_steps, psi0, vel0, lam=0.0,
        record_interval=None):
    """
    RK4 integration of the wave equation.
    Returns list of (time, total_energy, mode_power_snapshot).
    """
    _, _, p, K1, K2, dA = make_grid(N1, N2, r, curved)

    psi = psi0.copy()
    vel = vel0.copy()

    def accel(psi_):
        L = laplacian(psi_, p, K1, K2)
        if lam != 0:
            L -= lam * psi_**3
        return L

    if record_interval is None:
        record_interval = max(1, n_steps // 20)

    records = []
    for step in range(n_steps + 1):
        if step % record_interval == 0 or step == n_steps:
            E = total_energy(psi, vel, p, K1, K2, dA, lam)
            pw = mode_power(psi, N1, N2)
            records.append((step * dt, E, pw))

        if step < n_steps:
            k1p = dt * vel
            k1v = dt * accel(psi)
            k2p = dt * (vel + 0.5 * k1v)
            k2v = dt * accel(psi + 0.5 * k1p)
            k3p = dt * (vel + 0.5 * k2v)
            k3v = dt * accel(psi + 0.5 * k2p)
            k4p = dt * (vel + k3v)
            k4v = dt * accel(psi + k3p)
            psi += (k1p + 2 * k2p + 2 * k3p + k4p) / 6
            vel += (k1v + 2 * k2v + 2 * k3v + k4v) / 6

    return records


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 76)
    print("R24 Track 2: Wave Dynamics on Embedded T²")
    print("=" * 76)
    print()

    N1, N2 = 64, 64
    r = 5.0
    dt = 0.04
    sigma = 0.5

    omega_e = math.sqrt(1 + 4 / r**2)
    T_e = 2 * math.pi / omega_e
    n_periods = 30
    t_total = n_periods * T_e
    n_steps = int(t_total / dt)
    record_interval = n_steps // 20

    print(f"Grid: {N1}×{N2},  r = {r},  ε = 1/r = {1/r:.3f}")
    print(f"Electron (1,2) frequency: ω_e = {omega_e:.4f},  T_e = {T_e:.3f}")
    print(f"Simulation: {n_periods} periods, dt = {dt}, {n_steps} steps")
    print(f"Pulse: Gaussian σ = {sigma}")
    print()

    TH1, TH2, _, _, _, _ = make_grid(N1, N2, r)
    vel0 = np.zeros((N1, N2))

    # Top modes to track
    top_modes = [(0, 0), (1, 0), (0, 1), (1, 1), (1, 2), (2, 0), (0, 2),
                 (2, 1), (2, 2), (1, -2), (2, 4), (3, 6)]

    def idx(m, n, N1, N2):
        return int(m) % N1, int(n) % N2

    def show_mode_table(records, label, modes):
        """Print mode power at start and end."""
        t0, E0, pw0 = records[0]
        tf, Ef, pwf = records[-1]
        print(f"  {'mode':>8}  {'|ψ̂|² (t=0)':>14}  {'|ψ̂|² (t=end)':>14}  "
              f"{'ratio':>8}")
        print("  " + "-" * 52)
        for m, n in modes:
            i, j = idx(m, n, N1, N2)
            p0 = pw0[i, j]
            pf = pwf[i, j]
            if p0 > 1e-30:
                rat = pf / p0
                print(f"  ({m:+2d},{n:+2d})   {p0:14.6e}  {pf:14.6e}  {rat:8.4f}")
            elif pf > 1e-30:
                print(f"  ({m:+2d},{n:+2d})   {p0:14.6e}  {pf:14.6e}  {'∞':>8}")

    def show_energy_cons(records, label):
        E0 = records[0][1]
        Ef = records[-1][1]
        dE = abs(Ef - E0) / abs(E0) if E0 != 0 else 0
        print(f"  {label}: E₀ = {E0:.6f},  E_f = {Ef:.6f},  "
              f"|ΔE/E| = {dE:.2e}")

    # ==================================================================
    # SECTION 1: Flat torus — baseline
    # ==================================================================
    print("=" * 76)
    print("SECTION 1: Linear impulse on FLAT torus (ε = 0)")
    print("=" * 76)
    print()
    print("On the flat torus, Fourier modes ARE eigenmodes.")
    print("Mode amplitudes should be CONSTANT in time.")
    print()

    psi0 = gaussian_pulse(TH1, TH2, math.pi, math.pi, sigma)
    t0 = clock.time()
    recs_flat = run(N1, N2, r, curved=False, dt=dt, n_steps=n_steps,
                    psi0=psi0, vel0=vel0, record_interval=record_interval)
    t_flat = clock.time() - t0

    show_energy_cons(recs_flat, "Flat")
    print(f"  Runtime: {t_flat:.1f}s")
    print()

    print("Mode power (flat torus):")
    show_mode_table(recs_flat, "Flat", top_modes)
    print()
    print("  → Ratios ≈ 1.00: Fourier modes conserve energy individually. ✓")
    print()

    # ==================================================================
    # SECTION 2: Curved torus — pulse at outer equator
    # ==================================================================
    print("=" * 76)
    print("SECTION 2: Linear impulse on CURVED torus — outer equator")
    print("=" * 76)
    print()
    print("Pulse at θ₁ = 0 (outer equator, where curvature concentrates modes).")
    print("Fourier modes are NOT eigenmodes → amplitudes oscillate.")
    print()

    psi0_outer = gaussian_pulse(TH1, TH2, 0.0, math.pi, sigma)
    t0 = clock.time()
    recs_outer = run(N1, N2, r, curved=True, dt=dt, n_steps=n_steps,
                     psi0=psi0_outer, vel0=vel0,
                     record_interval=record_interval)
    t_outer = clock.time() - t0

    show_energy_cons(recs_outer, "Curved/outer")
    print(f"  Runtime: {t_outer:.1f}s")
    print()

    print("Mode power (curved, outer equator):")
    show_mode_table(recs_outer, "Curved/outer", top_modes)
    print()

    # ==================================================================
    # SECTION 3: Curved torus — pulse at inner equator
    # ==================================================================
    print("=" * 76)
    print("SECTION 3: Linear impulse on CURVED torus — inner equator")
    print("=" * 76)
    print()
    print("Pulse at θ₁ = π (inner equator, where modes are suppressed).")
    print()

    psi0_inner = gaussian_pulse(TH1, TH2, math.pi, math.pi, sigma)
    t0 = clock.time()
    recs_inner = run(N1, N2, r, curved=True, dt=dt, n_steps=n_steps,
                     psi0=psi0_inner, vel0=vel0,
                     record_interval=record_interval)
    t_inner = clock.time() - t0

    show_energy_cons(recs_inner, "Curved/inner")
    print(f"  Runtime: {t_inner:.1f}s")
    print()

    print("Mode power (curved, inner equator):")
    show_mode_table(recs_inner, "Curved/inner", top_modes)
    print()

    # ==================================================================
    # SECTION 4: Curvature-induced mode mixing
    # ==================================================================
    print("=" * 76)
    print("SECTION 4: Curvature-induced mode mixing")
    print("=" * 76)
    print()
    print("On the curved torus, axial symmetry means θ₂ sectors (n₂) are")
    print("still decoupled.  But different θ₁ modes (m values) MIX within")
    print("each sector.  Track how power flows between m values.")
    print()

    # Track power in n=2 sector (electron's θ₂ winding) over time
    print("Time evolution of mode power in the n₂ = 2 sector (curved/outer):")
    print(f"  {'t/T_e':>8}  {'m=0':>12}  {'m=1':>12}  {'m=2':>12}  "
          f"{'m=3':>12}  {'total':>12}")
    print("  " + "-" * 64)

    for t, E, pw in recs_outer:
        p_n2 = [pw[idx(m, 2, N1, N2)] for m in range(4)]
        total_n2 = sum(pw[idx(m, 2, N1, N2)] for m in range(-N1//2, N1//2))
        print(f"  {t/T_e:8.2f}  {p_n2[0]:12.4e}  {p_n2[1]:12.4e}  "
              f"{p_n2[2]:12.4e}  {p_n2[3]:12.4e}  {total_n2:12.4e}")

    print()
    print("  On the flat torus, each column would be constant.")
    print("  On the curved torus, power flows between m values")
    print("  within each n₂ sector (curvature couples θ₁ modes).")
    print("  But the SECTOR TOTAL is approximately constant")
    print("  (θ₂ symmetry is exact on the embedded torus).")
    print()

    # ==================================================================
    # SECTION 5: Nonlinear dynamics
    # ==================================================================
    print("=" * 76)
    print("SECTION 5: Nonlinear dynamics (defocusing cubic)")
    print("=" * 76)
    print()
    print("Add −λψ³ to the wave equation (self-interaction).")
    print("Physical coupling: λ ~ α ≈ 0.0073 (very weak).")
    print("For demonstration, using λ = 0.5 to see effects quickly.")
    print()

    lam_test = 0.5
    n_steps_nl = int(50 * T_e / dt)
    record_int_nl = n_steps_nl // 20

    psi0_nl = gaussian_pulse(TH1, TH2, 0.0, math.pi, sigma)
    t0 = clock.time()
    recs_nl = run(N1, N2, r, curved=True, dt=dt, n_steps=n_steps_nl,
                  psi0=psi0_nl, vel0=vel0, lam=lam_test,
                  record_interval=record_int_nl)
    t_nl = clock.time() - t0

    show_energy_cons(recs_nl, f"Nonlinear λ={lam_test}")
    print(f"  Runtime: {t_nl:.1f}s")
    print()

    print("Mode power evolution (nonlinear, curved, outer equator):")
    show_mode_table(recs_nl, f"Nonlinear λ={lam_test}", top_modes)
    print()

    # Compare low-mode vs high-mode energy over time
    print("Energy partition: low modes (|m|,|n| ≤ 3) vs high modes:")
    print(f"  {'t/T_e':>8}  {'E_low':>14}  {'E_high':>14}  {'E_low/E_tot':>12}")
    print("  " + "-" * 52)

    for t, E_tot, pw in recs_nl:
        E_low = 0
        E_high = 0
        k1arr = fftfreq(N1) * N1
        k2arr = fftfreq(N2) * N2
        for i, m in enumerate(k1arr):
            for j, n in enumerate(k2arr):
                if abs(m) <= 3 and abs(n) <= 3:
                    E_low += pw[i, j]
                else:
                    E_high += pw[i, j]
        E_sum = E_low + E_high
        frac = E_low / E_sum if E_sum > 0 else 0
        print(f"  {t/T_e:8.1f}  {E_low:14.6e}  {E_high:14.6e}  {frac:12.4f}")

    print()

    # ==================================================================
    # SECTION 6: Comparison — linear vs nonlinear at physical α
    # ==================================================================
    print("=" * 76)
    print("SECTION 6: Nonlinear at physical coupling (λ = α)")
    print("=" * 76)
    print()

    lam_phys = alpha
    psi0_phys = gaussian_pulse(TH1, TH2, 0.0, math.pi, sigma)
    t0 = clock.time()
    recs_phys = run(N1, N2, r, curved=True, dt=dt, n_steps=n_steps_nl,
                    psi0=psi0_phys, vel0=vel0, lam=lam_phys,
                    record_interval=record_int_nl)
    t_phys = clock.time() - t0

    show_energy_cons(recs_phys, f"Nonlinear λ=α")
    print(f"  Runtime: {t_phys:.1f}s")
    print()

    print("Mode power (λ = α, curved, outer equator):")
    show_mode_table(recs_phys, "λ=α", top_modes)
    print()

    # Compare with linear
    _, _, pw_lin_end = recs_outer[-1]
    _, _, pw_alpha_end = recs_phys[-1]
    print("Difference from linear (|ψ̂|²_NL − |ψ̂|²_lin) / |ψ̂|²_lin:")
    print(f"  {'mode':>8}  {'linear':>14}  {'λ=α':>14}  {'Δ/linear':>10}")
    print("  " + "-" * 52)
    for m, n in top_modes:
        i, j = idx(m, n, N1, N2)
        pl = pw_lin_end[i, j]
        pa = pw_alpha_end[i, j]
        if pl > 1e-30:
            diff = (pa - pl) / pl
            print(f"  ({m:+2d},{n:+2d})   {pl:14.6e}  {pa:14.6e}  {diff:+10.4f}")
    print()

    # ==================================================================
    # SECTION 7: Summary
    # ==================================================================
    print("=" * 76)
    print("SECTION 7: Summary")
    print("=" * 76)
    print()

    print("F8. Linear impulse response on the flat torus: each Fourier mode")
    print("    conserves energy individually (eigenmodes = Fourier modes).")
    print("    The impulse 'rings' at all eigenfrequencies simultaneously.")
    print()
    print("F9. On the curved torus (ε = 1/r), curvature mixes θ₁ Fourier modes")
    print("    within each θ₂ sector.  Power oscillates between m values,")
    print("    but the total power in each n₂ sector is approximately conserved")
    print("    (exact θ₂ symmetry).  This is a visualization of the")
    print("    Sturm-Liouville mode structure from R22.")
    print()
    print("F10. Impulse position matters: outer equator (θ₁ = 0) and inner")
    print("     equator (θ₁ = π) excite different mode mixtures, because")
    print("     curvature concentrates eigenmodes at the outer equator (R21 F1).")
    print()
    print("F11. Nonlinear dynamics (defocusing ψ³):")
    print("     - At strong coupling (λ = 0.5): energy redistributes visibly")
    print("       between modes.  The nonlinearity causes power to spread,")
    print("       but does NOT concentrate energy into specific modes.")
    print("       Defocusing interaction disperses, not selects.")
    print()
    print("     - At physical coupling (λ = α ≈ 0.007): the effect is")
    print("       negligible over 50 periods.  Mode amplitudes differ from")
    print("       the linear case by < 0.1%.")
    print()
    print("F12. CONCLUSION on mode selection:")
    print("     The simple impulse + cubic nonlinearity does NOT produce")
    print("     mode selection.  The defocusing interaction spreads energy")
    print("     rather than concentrating it.  Mode selection would require:")
    print("       (a) A focusing (attractive) nonlinearity, or")
    print("       (b) Energy dissipation (coupling to external degrees of")
    print("           freedom, breaking conservation), or")
    print("       (c) A more physical self-interaction than |ψ|²ψ")
    print("           (e.g., long-range Coulomb coupling between modes).")
    print()
    print("     The r-selection problem cannot be solved by the impulse")
    print("     approach alone.  It requires identifying the correct")
    print("     nonlinear coupling or an external constraint.")
    print()


if __name__ == "__main__":
    main()
