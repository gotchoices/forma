#!/usr/bin/env python3
"""
R35 Track 4: Coupling strength estimate

Computes the strength of I/O coupling to the neutrino sheet
via two channels:

Channel A: Flat Ma (neutron-gateway / cross-shear)
  EM → electron-T² → σ_eν → neutrino-T²
  Result: EXACTLY ZERO for EM-driven processes.
  Neutrino modes are uncharged (F8), modes don't mix (F9),
  so the EM field has no handle on the neutrino sheet.
  Non-EM (thermal) pathway is blocked by the MeV gap (F12).

Channel B: Elastic torus (geometric modulation)
  Molecular forces → δ(geometry) → ν-mode excitation
  Parametrized by compliance K (unknown).
  Computes what K values give biologically relevant I/O.
  Determines the Goldilocks window: K large enough to write,
  small enough to retain.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import math
from lib.ma import (build_scaled_metric, mode_energy, compute_scales,
                     hbar_c_MeV_fm, M_E_MEV, M_P_MEV, DM2_21, S34, ALPHA)

# ═══════════════════════════════════════════════════════════════════
#  Physical constants
# ═══════════════════════════════════════════════════════════════════

hbar_SI = 1.0546e-34      # J·s
c_SI = 2.998e8             # m/s
eV_J = 1.602e-19           # J/eV
kB = 8.617e-5              # eV/K
T_BODY = 310               # K
kT_eV = kB * T_BODY        # ~26.7 meV
N_ATOMS_CELL = 1e14
N_NEUTRONS_CELL = 5e13     # ~half of atoms have neutrons (avg Z/A ~ 0.5)


def neutrino_E0_eV():
    """Energy scale E₀ of the neutrino T²."""
    return math.sqrt(DM2_21 / (4 * S34))


def neutrino_mode_energy(n3, n4, r_nu, s34=S34):
    """Energy of mode (n₃, n₄) in eV."""
    E0 = neutrino_E0_eV()
    return E0 * math.sqrt(n3**2 / r_nu**2 + (n4 - n3 * s34)**2)


def mode_energy_sensitivity(n3, n4, r_nu, s34=S34, param='r'):
    """
    ∂E/∂p for neutrino mode, where p is r_ν or s₃₄.
    Returns dE/dp in eV per unit of p.
    """
    E0 = neutrino_E0_eV()
    E = neutrino_mode_energy(n3, n4, r_nu, s34)
    if E < 1e-30:
        return 0.0

    if param == 'r':
        # ∂E/∂r_ν = E₀ × (-n₃²/r_ν³) / μ
        mu = E / E0
        return E0 * (-n3**2 / r_nu**3) / mu if mu > 1e-30 else 0.0
    elif param == 's':
        # ∂E/∂s₃₄ = E₀ × (-n₃)(n₄ - n₃s) / μ
        mu = E / E0
        return E0 * (-n3) * (n4 - n3 * s34) / mu if mu > 1e-30 else 0.0
    return 0.0


# ═══════════════════════════════════════════════════════════════════
#  Channel A: Flat Ma coupling (null result)
# ═══════════════════════════════════════════════════════════════════

def flat_t6_coupling(r_nu, sigma_enu, r_e=6.6, r_p=6.6, sigma_ep=0.038):
    """
    Compute the flat-Ma EM coupling to neutrino modes.

    On a flat Ma:
    - Modes are exact plane waves (F9)
    - Charge is topological: Q = -n₁ + n₅ (F8)
    - Neutrino modes have n₁ = n₅ = 0 → Q = 0 EXACTLY
    - Cross-shear shifts energies but does not mix modes
    - EM coupling to neutrino modes = 0 (exact)

    Returns a dict with the coupling chain analysis.
    """
    Gt0, Gti0, L0, _ = build_scaled_metric(r_e, r_nu, r_p, sigma_ep=sigma_ep)
    Gt1, Gti1, L1, _ = build_scaled_metric(r_e, r_nu, r_p,
                                             sigma_ep=sigma_ep,
                                             sigma_enu=sigma_enu)
    n_nu = np.array([0, 0, 1, 2, 0, 0], dtype=float)
    n_e = np.array([1, 2, 0, 0, 0, 0], dtype=float)

    E_nu = mode_energy(tuple(n_nu.astype(int)), Gti0, L0)  # MeV
    E_e = mode_energy(tuple(n_e.astype(int)), Gti0, L0)

    delta_Gti = Gti1 - Gti0
    ntilde_nu = n_nu / L0
    ntilde_e = n_e / L0
    V = (2 * math.pi * hbar_c_MeV_fm)**2 * ntilde_e @ delta_Gti @ ntilde_nu

    c_mix = V / (E_nu**2 - E_e**2) if abs(E_nu**2 - E_e**2) > 1e-30 else 0
    energy_gap = E_e / (E_nu if E_nu > 0 else 1e-30)

    return {
        'E_nu_eV': E_nu * 1e6,
        'E_e_MeV': E_e,
        'V_MeV2': V,
        'c_mix': c_mix,
        'energy_gap': energy_gap,
        'Q_nu': 0,  # exact, topological
        'g_EM': 0.0,  # exact zero: Q = 0 → no EM coupling
        'note': 'Neutrino modes are EXACTLY uncharged. g_EM = 0 to all orders.'
    }


# ═══════════════════════════════════════════════════════════════════
#  Channel B: Elastic torus coupling
# ═══════════════════════════════════════════════════════════════════

def elastic_torus_write(n3, n4, r_nu, K, F_mol_eV,
                        s34=S34, channel='s'):
    """
    Energy deposited in neutrino mode by a molecular force
    through the elastic torus mechanism.

    F_mol acts on the geometry, changing the parameter p
    (either r_ν or s₃₄) by δp = K × F_mol.
    The mode energy shifts by δE = |∂E/∂p| × δp.

    Parameters
    ----------
    K : float — compliance (dimensionless change in geometry
        parameter per eV of molecular energy input, units: eV⁻¹)
    F_mol_eV : float — molecular energy in eV
    channel : 'r' or 's' — which geometry parameter is modulated

    Returns dict with write analysis.
    """
    dE_dp = mode_energy_sensitivity(n3, n4, r_nu, s34, channel)
    delta_p = K * F_mol_eV
    delta_E = abs(dE_dp * delta_p)

    E_mode = neutrino_mode_energy(n3, n4, r_nu, s34)

    # Compute mode spacing near this mode
    all_E = []
    for nn3 in range(-5, 6):
        for nn4 in range(-5, 6):
            if nn3 == 0 and nn4 == 0:
                continue
            Emn = neutrino_mode_energy(nn3, nn4, r_nu, s34)
            if Emn > 0:
                all_E.append(Emn)
    all_E.sort()
    min_spacing = E_mode
    for i in range(len(all_E) - 1):
        sp = all_E[i + 1] - all_E[i]
        if sp > 1e-12:
            min_spacing = min(min_spacing, sp)

    return {
        'mode': (n3, n4),
        'E_mode_eV': E_mode,
        'dE_dp': dE_dp,
        'delta_p': delta_p,
        'delta_E_eV': delta_E,
        'min_spacing_eV': min_spacing,
        'hops': delta_E / min_spacing if min_spacing > 0 else 0,
        'channel': channel,
    }


def elastic_torus_read(n3, n4, r_nu, K, s34=S34):
    """
    Observable effect of neutrino mode occupation on the
    cell's R³ properties through the elastic torus.

    If mode (n₃, n₄) is occupied with energy E_mode, the
    stored energy modulates the geometry.  The geometry change
    shifts molecular vibration frequencies by:

        δω/ω ~ K × E_mode_eV  (fractional shift)

    The compliance K appears in both write and read: it is
    the same parameter — geometry responds to energy.

    Thermal noise causes fluctuations of amplitude:
        δω/ω|_noise ~ K × kT

    SNR for single atom = (K × E_mode) / (K × kT) = E_mode/kT
    SNR collective = √N × E_mode/kT

    Note: in the elastic torus, the READ SNR is independent of K!
    The signal and noise both scale with K, so K cancels.
    Read is always viable if E_mode > kT/√N ~ 10⁻¹⁰ eV.
    """
    E_mode = neutrino_mode_energy(n3, n4, r_nu, s34)

    snr_single = E_mode / kT_eV if kT_eV > 0 else 0
    snr_collective = snr_single * math.sqrt(N_ATOMS_CELL)

    freq_shift_frac = K * E_mode
    noise_frac = K * kT_eV
    voltage_shift_mV = 70.0 * freq_shift_frac

    return {
        'mode': (n3, n4),
        'E_mode_meV': E_mode * 1e3,
        'freq_shift_frac': freq_shift_frac,
        'noise_frac': noise_frac,
        'voltage_shift_mV': voltage_shift_mV,
        'snr_single': snr_single,
        'snr_collective': snr_collective,
    }


def goldilocks_scan(r_nu, F_write, s34=S34, channel='s'):
    """
    Scan compliance K (eV⁻¹) to find the Goldilocks window.

    For the shear channel, the Goldilocks condition simplifies:
      hops = K × F × |∂E/∂s| / spacing
    When |∂E/∂s| ≈ spacing (true for uniformly spaced modes):
      hops ≈ K × F

    Write viable: K × F_write ≥ 1
    Retain viable: K × kT < 0.1
    Read viable: always (SNR = E/kT × √N, independent of K)
    """
    K_values = np.logspace(-3, 3, 500)

    results = []
    for K in K_values:
        w = elastic_torus_write(1, 2, r_nu, K, F_write, s34, channel)
        w_therm = elastic_torus_write(1, 2, r_nu, K, kT_eV, s34, channel)
        r = elastic_torus_read(1, 2, r_nu, K, s34)

        write_ok = w['hops'] >= 1.0
        retain_ok = w_therm['hops'] < 0.1
        read_ok = r['snr_collective'] >= 1.0

        results.append({
            'K': K,
            'write_hops': w['hops'],
            'write_ok': write_ok,
            'thermal_hops': w_therm['hops'],
            'retain_ok': retain_ok,
            'read_snr': r['snr_collective'],
            'read_ok': read_ok,
            'goldilocks': write_ok and read_ok and retain_ok,
        })

    return results


# ═══════════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════════

def main():
    print("=" * 72)
    print("R35 Track 4: Coupling Strength Estimate")
    print("=" * 72)

    r_nu = 100
    E0_eV = neutrino_E0_eV()

    # ── Part A: Flat Ma channel (null result) ─────────────────────
    print(f"\n{'='*72}")
    print("PART A: Flat Ma coupling — the null result")
    print("=" * 72)
    print("""
On a flat Ma, the neutron-gateway coupling chain is:
    EM field → electron-T² → (σ_eν) → neutrino-T²

But this chain is BROKEN at every step:

1. Neutrino modes are EXACTLY uncharged (F8).
   Q = -n₁ + n₅ = 0 - 0 = 0.  Topological.
   The EM field has no direct handle on neutrino modes.

2. Cross-shear does NOT mix modes on a flat Ma (F9).
   Modes remain exact plane waves.  The "coupling matrix
   element" V shifts ENERGIES, not WAVEFUNCTIONS.

3. The MeV gap (F12) blocks thermal coupling.
   R³ thermal (meV) → electron T² (MeV): Boltzmann
   factor exp(-MeV/meV) ≈ 0.

Conclusion: g_flat = 0 (exact).  No Goldilocks window
exists on a flat Ma.
""")

    for sigma_enu in [0.001, 0.01, 0.05]:
        result = flat_t6_coupling(r_nu, sigma_enu)
        print(f"  σ_eν = {sigma_enu}")
        print(f"    E_ν = {result['E_nu_eV']*1e3:.4f} meV")
        print(f"    E_e = {result['E_e_MeV']:.4f} MeV")
        print(f"    Energy gap E_e/E_ν = {result['energy_gap']:.0e}")
        print(f"    V (cross-shear) = {result['V_MeV2']:.2e} MeV²")
        print(f"    c_mix (energy perturbation) = {abs(result['c_mix']):.2e}")
        print(f"    Q_neutrino = {result['Q_nu']} (exact, topological)")
        print(f"    g_EM = {result['g_EM']} (EXACT ZERO)")
        print()

    print("  VERDICT: Flat Ma channel is CLOSED.")
    print("  The neutron gateway (Q78 Theory B) requires the elastic")
    print("  torus to operate.  On a flat Ma, there is no I/O.")

    # ── Part B: Mode energy sensitivity ───────────────────────────
    print(f"\n{'='*72}")
    print("PART B: Neutrino mode energy sensitivity to geometry changes")
    print("=" * 72)
    print(f"\n  r_ν = {r_nu},  s₃₄ = {S34}")
    print(f"  E₀ = {E0_eV*1e3:.2f} meV")

    print(f"\n  {'(n₃,n₄)':>8s} {'E (meV)':>10s} {'∂E/∂r_ν (eV)':>14s} "
          f"{'∂E/∂s₃₄ (eV)':>14s} {'sensitivity':>12s}")
    print(f"  {'-'*64}")

    for n3, n4 in [(0,1), (0,2), (1,1), (1,2), (2,3), (0,3), (1,0)]:
        E = neutrino_mode_energy(n3, n4, r_nu)
        dE_dr = mode_energy_sensitivity(n3, n4, r_nu, S34, 'r')
        dE_ds = mode_energy_sensitivity(n3, n4, r_nu, S34, 's')
        sens = "r-sensitive" if abs(dE_dr) > abs(dE_ds) * 0.01 else "s-only"
        if n3 == 0:
            sens = "r-independent"
        print(f"  ({n3:2d},{n4:2d})  {E*1e3:10.4f} {dE_dr:14.2e} "
              f"{dE_ds:14.2e} {sens:>12s}")

    print(f"""
  Key observation: modes with n₃ = 0 are INDEPENDENT of r_ν.
  Only modes with n₃ ≠ 0 respond to r_ν changes, and their
  sensitivity goes as ~n₃/r_ν² (tiny at large r_ν).

  Shear s₃₄ sensitivity is much larger: ∂E/∂s₃₄ ~ E₀ for
  modes with n₃ ≠ 0.  The shear channel is the dominant
  geometric coupling.
""")

    # ── Part C: Elastic torus — write analysis (shear channel) ──
    print(f"{'='*72}")
    print("PART C: Elastic torus — write via shear modulation")
    print("=" * 72)
    print(f"""
  Write mechanism: molecular forces modulate the torus shear s₃₄.
  The shear change shifts neutrino mode energies.
  If the shift exceeds the mode spacing, a mode transition occurs.

  Key insight: ∂E/∂s₃₄ ≈ E₀ ≈ mode spacing for n₃ ≠ 0 modes.
  This means: mode_hops ≈ K × F_mol  (geometry cancels out).
  The Goldilocks condition is PURELY THERMODYNAMIC.

  Molecular energy estimates:
    ATP hydrolysis:     ~0.5 eV per event
    Ion channel gating: ~70 meV (membrane voltage)
    Molecular vibration: ~50 meV (mid-IR quantum)
    Thermal fluctuation: ~27 meV (kT at 37°C)
""")

    F_mol_values = {
        'ATP hydrolysis': 0.5,
        'Ion channel': 0.070,
        'Molecular vibration': 0.050,
        'Thermal (kT)': kT_eV,
    }

    for K_val, K_label in [(0.1, "K=0.1 eV⁻¹"),
                            (1.0, "K=1 eV⁻¹"),
                            (5.0, "K=5 eV⁻¹"),
                            (20.0, "K=20 eV⁻¹")]:
        print(f"\n  {K_label}:")
        print(f"  {'Source':>22s} {'δs':>10s} {'δE (meV)':>12s} "
              f"{'mode hops':>10s} {'writable?':>10s}")
        print(f"  {'-'*68}")
        for src_name, F_mol in F_mol_values.items():
            w = elastic_torus_write(1, 2, r_nu, K_val, F_mol, channel='s')
            hop_str = f"{w['hops']:.2e}" if w['hops'] < 0.01 else f"{w['hops']:.2f}"
            ok = "YES" if w['hops'] >= 1.0 else "no"
            print(f"  {src_name:>22s} {w['delta_p']:10.4f} "
                  f"{w['delta_E_eV']*1e3:12.4f} {hop_str:>10s} {ok:>10s}")

    # ── Part D: Elastic torus — read analysis ─────────────────────
    print(f"\n{'='*72}")
    print("PART D: Elastic torus — read analysis")
    print("=" * 72)
    print(f"""
  Read mechanism: neutrino-sheet occupation → geometry change →
  molecular vibration frequency shift → detectable.

  CRITICAL INSIGHT: the read SNR is INDEPENDENT of K!
    SNR_single = E_mode / kT
    SNR_collective = √N × E_mode / kT

  Both signal and noise scale with K, so K cancels.  Reading
  is ALWAYS viable as long as E_mode > kT/√N ~ 10⁻¹⁰ eV.
  Since E_mode ~ 30 meV >> 10⁻¹⁰ eV, reading works at
  ANY compliance K.

  N_atoms = {N_ATOMS_CELL:.0e},  √N = {math.sqrt(N_ATOMS_CELL):.0e}
  kT = {kT_eV*1e3:.1f} meV
""")

    print(f"  {'(n₃,n₄)':>8s} {'E (meV)':>8s} {'SNR(1)':>10s} "
          f"{'SNR(coll)':>10s} {'readable?':>10s}")
    print(f"  {'-'*52}")
    for n3, n4 in [(0,1), (1,1), (1,2), (2,3), (0,3)]:
        r = elastic_torus_read(n3, n4, r_nu, 1.0)
        ok = "YES" if r['snr_collective'] >= 1.0 else "no"
        print(f"  ({n3:2d},{n4:2d})  {r['E_mode_meV']:8.3f} "
              f"{r['snr_single']:10.2f} "
              f"{r['snr_collective']:10.2e} {ok:>10s}")

    print(f"\n  ALL modes are readable with collective enhancement.")
    print(f"  Even the lowest mode (0,1) at {neutrino_mode_energy(0,1,r_nu)*1e3:.1f} meV")
    print(f"  has SNR_collective ~ {neutrino_mode_energy(0,1,r_nu)/kT_eV * math.sqrt(N_ATOMS_CELL):.0e}.")

    # ── Part E: Goldilocks analysis ─────────────────────────────
    print(f"\n{'='*72}")
    print("PART E: Goldilocks analysis — the thermodynamic criterion")
    print("=" * 72)
    print(f"""
  On the shear channel, ∂E/∂s₃₄ ≈ E₀ ≈ mode spacing.
  This makes the Goldilocks condition PURELY THERMODYNAMIC:

    mode_hops ≈ K × F_energy  (geometry cancels out)

  Write:  K × F_write ≥ 1    (≥ 1 mode hop)
  Retain: K × kT < 0.1       (< 0.1 hops from thermal noise)
  Read:   always viable       (SNR independent of K, Part D)

  Combined: F_write / kT > 10  (necessary condition)
""")

    sources = [
        ('Passive vibration', 0.050),
        ('Ion channel', 0.070),
        ('ATP hydrolysis', 0.500),
        ('2 × ATP', 1.000),
    ]

    print(f"  {'Write source':>20s} {'F (eV)':>8s} {'F/kT':>8s} "
          f"{'K_min (eV⁻¹)':>12s} {'K_max (eV⁻¹)':>12s} {'window?':>10s}")
    print(f"  {'-'*76}")

    for name, F_w in sources:
        ratio = F_w / kT_eV
        K_min = 1.0 / F_w  # write threshold
        K_max = 0.1 / kT_eV  # retain limit
        has_window = K_min < K_max
        span_str = f"{K_max/K_min:.1f}×" if has_window else "—"
        print(f"  {name:>20s} {F_w:8.3f} {ratio:8.1f} "
              f"{K_min:12.2f} {K_max:12.2f} "
              f"{'YES (' + span_str + ')' if has_window else 'NO':>10s}")

    print(f"""
  The threshold is F_write / kT > 10, i.e. F_write > {10*kT_eV*1e3:.0f} meV.

  Passive vibrations (50 meV):  ratio = 1.9  → NO WINDOW
  Ion channels (70 meV):        ratio = 2.6  → NO WINDOW
  ATP hydrolysis (500 meV):     ratio = 18.7 → WINDOW EXISTS

  *** ATP IS THE MINIMUM VIABLE WRITE ENERGY ***
  Writing to the neutrino sheet REQUIRES metabolic energy.
  Passive thermal/vibrational processes cannot write.
""")

    # ── Part F: ATP Goldilocks window — from scan ──────────────────
    print(f"{'='*72}")
    print("PART F: ATP-driven Goldilocks window — numerical scan")
    print("=" * 72)

    F_ATP = 0.5  # eV

    # Get actual min_spacing from one test call
    w_test = elastic_torus_write(1, 2, r_nu, 1.0, F_ATP, channel='s')
    actual_spacing = w_test['min_spacing_eV']
    sensitivity = abs(w_test['dE_dp'])
    ratio = sensitivity / actual_spacing if actual_spacing > 0 else 0

    print(f"\n  Mode (1,2): |∂E/∂s₃₄| = {sensitivity*1e3:.2f} meV")
    print(f"  Actual min spacing nearby = {actual_spacing*1e3:.3f} meV")
    print(f"  Effective amplification = |∂E/∂s| / spacing = {ratio:.1f}×")
    print(f"  → hops ≈ {ratio:.1f} × K × F")

    K_write = 1.0 / (ratio * F_ATP) if ratio * F_ATP > 0 else float('inf')
    K_retain = 0.1 / (ratio * kT_eV) if ratio * kT_eV > 0 else float('inf')

    print(f"\n  Corrected thresholds:")
    print(f"    Write (≥1 hop): K ≥ {K_write:.4f} eV⁻¹")
    print(f"    Retain (<0.1):  K < {K_retain:.4f} eV⁻¹")

    if K_write < K_retain:
        span = K_retain / K_write
        print(f"    Window: K ∈ [{K_write:.4f}, {K_retain:.4f}] eV⁻¹")
        print(f"    Span: {span:.1f}×")
    else:
        span = 0
        print(f"    NO WINDOW (write threshold > retain limit)")

    results = goldilocks_scan(r_nu, F_ATP, channel='s')

    # Find actual window from scan
    K_gold_low = None
    K_gold_high = None
    for r in results:
        if r['goldilocks']:
            if K_gold_low is None:
                K_gold_low = r['K']
            K_gold_high = r['K']

    if K_gold_low and K_gold_high:
        scan_span = K_gold_high / K_gold_low
        print(f"\n  Scan confirms: K ∈ [{K_gold_low:.4f}, {K_gold_high:.4f}]")
        print(f"  Scan span: {scan_span:.1f}×")
        span = scan_span

        print(f"\n  {'K (eV⁻¹)':>10s} {'ATP hops':>10s} {'therm hops':>10s} "
              f"{'status':>12s}")
        print(f"  {'-'*48}")
        for r in results:
            if 0.5 * K_gold_low <= r['K'] <= 2.0 * K_gold_high:
                status = "GOLDILOCKS" if r['goldilocks'] else (
                    "write fails" if not r['write_ok'] else "retain fails")
                print(f"  {r['K']:10.4f} {r['write_hops']:10.3f} "
                      f"{r['thermal_hops']:10.4f} {status:>12s}")
    else:
        print(f"\n  Scan found NO Goldilocks window!")
        print(f"  Sampling near the analytical thresholds:")
        print(f"  {'K (eV⁻¹)':>10s} {'ATP hops':>10s} {'therm hops':>10s}")
        print(f"  {'-'*36}")
        for r in results:
            if 0.3 * K_write <= r['K'] <= 3.0 * K_retain:
                print(f"  {r['K']:10.4f} {r['write_hops']:10.3f} "
                      f"{r['thermal_hops']:10.4f}")

    # ── Part G: Biological predictions ────────────────────────────
    print(f"\n{'='*72}")
    print("PART G: Biological predictions from the Goldilocks window")
    print("=" * 72)
    print(f"""
  The ATP requirement for writing has sharp biological predictions:

  1. DEAD CELLS CANNOT WRITE (no ATP)
     But the stored pattern persists (retention is passive).
     New cells growing into the location read the old pattern.
     → Explains Levin's planaria memory surviving decapitation.

  2. METABOLICALLY ACTIVE CELLS WRITE FASTER
     Write rate ∝ ATP turnover rate.
     Neurons (high ATP consumption) write faster than glia.
     → Predicts correlation between metabolic rate and
       pattern encoding speed.

  3. READING IS PASSIVE AND ALWAYS ON
     SNR is independent of K and does not require ATP.
     Even dead cells can be "read" by neighbors.
     → Gap junctions (Levin's "data bus") transmit the
       read signal, not the write energy.

  4. ANESTHESIA SLOWS WRITING BUT NOT READING
     Anesthetics reduce ATP turnover (mitochondrial
     suppression).  This slows writing without affecting
     the stored pattern or the read signal.
     → Predicts that anesthetized organisms retain patterns
       but cannot form new ones.

  5. THE MEMBRANE VOLTAGE PATTERN IS A READ-OUT
     The non-uniform voltage on the cell membrane (F20)
     is a continuous projection of the neutrino-sheet state.
     Levin's Vmem observations are the DC component of
     this rich harmonic pattern.

  6. CO-RESONANCE BETWEEN CELLS IS THE READ MECHANISM
     Two cells with the same ν-pattern have matching
     molecular vibration frequencies → sympathetic resonance.
     Different patterns → no resonance.  This operates at
     the meV molecular scale, not at MeV.
""")

    atp_rate = 1e10  # ATP molecules/cell/second (typical)
    E_per_atp = 0.5  # eV

    mode_E = neutrino_mode_energy(1, 2, r_nu)
    K_mid = (K_write + K_retain) / 2 if K_write < K_retain else 0.05

    hops_per_atp = ratio * K_mid * E_per_atp
    print(f"  Estimate: ATP rate ~ {atp_rate:.0e} /cell/s")
    print(f"  Mode energy ~ {mode_E*1e3:.1f} meV")
    print(f"  At K = {K_mid:.4f} eV⁻¹ (mid-window):")
    print(f"  Each ATP event shifts by {hops_per_atp:.1f} mode hops")
    print(f"  → Writing is fast compared to biological timescales")

    # ── Summary ───────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("SUMMARY")
    print("=" * 72)
    print(f"""
Key results:

F22. Flat Ma coupling is EXACTLY ZERO.
     Neutrino modes are uncharged (Q = 0, topological).
     Cross-shear does not mix modes (flat Ma eigenstates
     are exact plane waves).  The EM field has no handle
     on the neutrino sheet.  The neutron-gateway chain
     (EM → e-T² → σ_eν → ν-T²) is broken at every step.
     No Goldilocks window exists on a flat Ma.

F23. The elastic torus shifts the coupling channel from EM
     to geometry.  Molecular forces → geometry change →
     neutrino mode energy shift → mode hop.  This bypasses
     all three protection layers (charge, gap, collective).

F24. Mode sensitivity is dominated by the shear channel.
     Modes with n₃ = 0 are r_ν-independent.
     Modes with n₃ ≠ 0 respond primarily to s₃₄ with
     ∂E/∂s₃₄ ≈ E₀ ≈ mode spacing.  The Goldilocks condition
     reduces to a purely thermodynamic criterion:
       F_write / kT > 10.

F25. Read SNR is independent of compliance K.
     Both signal and noise scale with K → K cancels.
     Collective SNR = √N × E_mode/kT ~ 10⁷ × 1 ~ 10⁷.
     Reading is ALWAYS viable.  No constraint on K from read.

F26. Passive vibrations CANNOT write: F/kT = 1.9 < 10.
     Molecular vibrations (50 meV) vs thermal noise (27 meV)
     gives insufficient margin.  The Goldilocks criterion
     (write ≥ 1 hop, thermal < 0.1 hops) is not satisfied
     at any K.

F27. ATP-driven write opens a Goldilocks window:
     K ∈ [{K_write:.4f}, {K_retain:.4f}] eV⁻¹  (span {span:.1f}×).
     ATP hydrolysis (0.5 eV) vs kT (27 meV) gives F/kT = 18.7.
     This exceeds the threshold of 10.
     Writing to the neutrino sheet REQUIRES metabolic energy.
     Predictions:
       - Dead cells cannot write (no ATP) but can be read
       - Metabolically active cells write faster
       - Anesthesia (reduced ATP) slows writing
       - Writing is an active, ATP-consuming process

F28. The metric compliance K is the master parameter.
     K must be in [{K_write:.4f}, {K_retain:.4f}] eV⁻¹.
     Computing K from first principles requires the moduli
     potential of the Ma geometry — the deepest remaining
     open question.
""")


if __name__ == '__main__':
    main()
