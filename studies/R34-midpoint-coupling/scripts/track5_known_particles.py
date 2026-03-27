#!/usr/bin/env python3
"""
R34 Track 5: Running of α with known Ma particles only.

Premise: Ghost modes are empirically unobserved.  If nature
does not select them as real excitations, they should not
participate as virtual excitations in vacuum polarization
loops either.  The running of α comes ONLY from particles
that Ma predicts AND that nature confirms.

This is fundamentally different from the SM:
- No quarks → no color factor ×3
- Hadrons (proton, pions, kaons, etc.) are fundamental
  and enter vacuum polarization loops directly
- All charges are integers (±1, ±2)
- Many charged species between 140–1800 MeV

Procedure:
1. Enumerate known Ma particles with masses, charges, spins
2. Compute one-loop running of α
3. Fit the bare coupling 1/α₀ so that 1/α(m_e) = 137
4. Check: does 1/α(m_Z) = 128?
5. Compare running profile to SM
"""

import sys
import os
import math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

ALPHA_OBS = 1.0 / 137.036
INV_ALPHA_OBS = 137.036
INV_ALPHA_MZ = 128.0
M_Z = 91187.6  # MeV
M_E = 0.511


# ── Known Ma particle catalog ────────────────────────────────────────
# Each entry: (name, mass_MeV, |Q|, spin_type, notes)
# spin_type: "dirac" (spin 1/2 or 3/2), "scalar" (spin 0), "vector" (spin 1)
#
# Each entry represents a PARTICLE-ANTIPARTICLE PAIR counted once.
# (e.g., "e⁻" includes the positron contribution)
#
# For baryons with distinct antiparticles of opposite charge,
# the baryon+antibaryon pair is one Dirac fermion entry.
#
# Vacuum polarization b-coefficients:
#   Dirac fermion:    b = 4/3
#   Complex scalar:   b = 1/3
#   Massive vector:   b = 7  (Proca field — noted as uncertain)

T6_PARTICLES = [
    # ── Leptons ──
    ("e⁻",        0.511,    1,  "dirac"),
    ("μ⁻",      105.658,    1,  "dirac"),
    ("τ⁻",     1776.86,     1,  "dirac"),

    # ── Pseudoscalar mesons (spin 0) ──
    ("π±",       139.570,    1,  "scalar"),
    ("K±",       493.677,    1,  "scalar"),

    # ── Vector mesons (spin 1) ──
    ("ρ±",       775.26,     1,  "vector"),
    ("K*±",      891.67,     1,  "vector"),

    # ── Spin-1/2 baryons ──
    ("p",        938.272,    1,  "dirac"),
    ("Σ⁺",     1189.37,     1,  "dirac"),
    ("Σ⁻",     1197.449,    1,  "dirac"),
    ("Ξ⁻",     1321.71,     1,  "dirac"),

    # ── Spin-3/2 baryons (treated as Dirac for VP coefficient) ──
    ("Δ⁺⁺",    1232.0,      2,  "dirac"),   # Q=2 → Q²=4
    ("Δ⁺",     1232.0,      1,  "dirac"),
    ("Δ⁻",     1232.0,      1,  "dirac"),
    ("Σ*⁺",    1382.80,     1,  "dirac"),
    ("Σ*⁻",    1387.20,     1,  "dirac"),
    ("Ξ*⁻",    1535.0,      1,  "dirac"),
    ("Ω⁻",     1672.45,     1,  "dirac"),

    # ── N* resonances (spin 1/2 or 3/2) ──
    ("N*(1440)", 1440.0,     1,  "dirac"),   # Roper
    ("N*(1520)", 1520.0,     1,  "dirac"),
    ("N*(1535)", 1535.0,     1,  "dirac"),
    ("N*(1675)", 1675.0,     1,  "dirac"),
    ("N*(1680)", 1680.0,     1,  "dirac"),
]

B_COEFFICIENTS = {
    "dirac":  4.0 / 3.0,
    "scalar": 1.0 / 3.0,
    "vector": 7.0,
}


# ── SM particle catalog for comparison ────────────────────────────────
# In SM, quarks carry color (N_c = 3) and fractional charges.

SM_PARTICLES = [
    # Leptons
    ("e",      0.511,    1,    "dirac",  1),
    ("μ",    105.658,    1,    "dirac",  1),
    ("τ",   1776.86,     1,    "dirac",  1),
    # Quarks: (name, mass, |Q_frac|, type, N_c)
    # Q_frac for quarks: u-type = 2/3, d-type = 1/3
    ("u",      2.16,     2./3, "dirac",  3),
    ("d",      4.67,     1./3, "dirac",  3),
    ("s",     93.4,      1./3, "dirac",  3),
    ("c",   1270.0,      2./3, "dirac",  3),
    ("b",   4180.0,      1./3, "dirac",  3),
    ("t", 172760.0,      2./3, "dirac",  3),
]


def compute_running(particles, inv_alpha_bare, E_probe, cutoff,
                    use_color=False):
    """
    One-loop QFT running of 1/α from the cutoff scale down to E_probe.

    1/α(E) = 1/α₀ + Σ_k (b_k × N_c × Q_k²)/(3π) × ln(Λ/max(E, m_k))

    Screening increases 1/α at low energy.
    """
    delta = 0.0
    for entry in particles:
        if use_color:
            name, mass, Q, spin_type, Nc = entry
        else:
            name, mass, Q, spin_type = entry
            Nc = 1

        if mass >= cutoff:
            continue

        b = B_COEFFICIENTS[spin_type]
        E_eff = max(E_probe, mass)
        if E_eff < cutoff:
            delta += Nc * b * Q**2 / (3 * math.pi) * math.log(cutoff / E_eff)

    return inv_alpha_bare + delta


def total_screening(particles, E_low, E_high, use_color=False):
    """Total Δ(1/α) from running between E_low and E_high."""
    delta = 0.0
    for entry in particles:
        if use_color:
            name, mass, Q, spin_type, Nc = entry
        else:
            name, mass, Q, spin_type = entry
            Nc = 1

        b = B_COEFFICIENTS[spin_type]

        if mass > E_high:
            continue

        m_eff_low = max(E_low, mass)
        m_eff_high = E_high
        if m_eff_low < m_eff_high:
            delta += Nc * b * Q**2 / (3 * math.pi) * math.log(m_eff_high / m_eff_low)

    return delta


# ══════════════════════════════════════════════════════════════════════
print("=" * 70)
print("R34 Track 5: Running of α with known Ma particles only")
print("=" * 70)


# ── Section 1: Catalog ───────────────────────────────────────────────
print(f"\n{'='*70}")
print("SECTION 1: Known Ma particle catalog")
print("=" * 70)

total_Q2 = 0
print(f"\n  {'Name':<14s} {'Mass (MeV)':>12s} {'|Q|':>5s} {'Type':>8s} {'b':>6s} {'b×Q²':>6s}")
print(f"  {'─'*14} {'─'*12} {'─'*5} {'─'*8} {'─'*6} {'─'*6}")
for name, mass, Q, spin_type in T6_PARTICLES:
    b = B_COEFFICIENTS[spin_type]
    bQ2 = b * Q**2
    total_Q2 += bQ2
    print(f"  {name:<14s} {mass:12.3f} {Q:5d} {spin_type:>8s} {b:6.2f} {bQ2:6.2f}")

print(f"\n  Total particles: {len(T6_PARTICLES)}")
print(f"  Total Σ b×Q²:   {total_Q2:.2f}")
print(f"  Running rate:    Σ b×Q² / (3π) = {total_Q2/(3*math.pi):.4f} per unit ln(E)")

sm_total_Q2 = 0
for name, mass, Q, spin_type, Nc in SM_PARTICLES:
    b = B_COEFFICIENTS[spin_type]
    sm_total_Q2 += Nc * b * Q**2
print(f"\n  SM comparison:")
print(f"  Total Σ N_c×b×Q²: {sm_total_Q2:.2f}")
print(f"  SM running rate:   {sm_total_Q2/(3*math.pi):.4f} per unit ln(E)")
print(f"  Ma / SM ratio:    {total_Q2/sm_total_Q2:.3f}")


# ── Section 2: Total running from m_e to various scales ──────────────
print(f"\n\n{'='*70}")
print("SECTION 2: Total screening (Δ1/α) from m_e to various scales")
print("=" * 70)

scales = [
    ("m_μ",     105.658),
    ("m_π",     139.570),
    ("m_p",     938.272),
    ("2 GeV",   2000.0),
    ("m_Z",     M_Z),
    ("1 TeV",   1e6),
    ("10 TeV",  1e7),
    ("100 TeV", 1e8),
    ("1 PeV",   1e9),
    ("10 PeV",  1e10),
    ("GUT",     2e16 * 1000),  # ~2×10¹⁶ GeV in MeV
]

print(f"\n  {'Scale':>12s} {'Δ(1/α) Ma':>12s} {'Δ(1/α) SM':>12s} {'Ma/SM':>8s}")
print(f"  {'─'*12} {'─'*12} {'─'*12} {'─'*8}")

for name, E_high in scales:
    dt6 = total_screening(T6_PARTICLES, M_E, E_high)
    dsm = total_screening(SM_PARTICLES, M_E, E_high, use_color=True)
    ratio = dt6 / dsm if dsm > 0 else float('inf')
    print(f"  {name:>12s} {dt6:12.3f} {dsm:12.3f} {ratio:8.3f}")


# ── Section 3: Fit bare coupling ─────────────────────────────────────
print(f"\n\n{'='*70}")
print("SECTION 3: Fit bare coupling 1/α₀ from 1/α(m_e) = 137")
print("=" * 70)

print(f"\n  For a given cutoff Λ, the bare coupling is:")
print(f"  1/α₀ = 1/α(m_e) − Δ(1/α) from m_e to Λ")
print(f"  1/α₀ = 137.036 − Δ(m_e → Λ)")

print(f"\n  {'Cutoff':>12s} {'Δ(m_e→Λ) Ma':>14s} {'1/α₀ Ma':>10s} {'Δ(m_e→Λ) SM':>14s} {'1/α₀ SM':>10s}")
print(f"  {'─'*12} {'─'*14} {'─'*10} {'─'*14} {'─'*10}")

for name, E_high in scales:
    dt6 = total_screening(T6_PARTICLES, M_E, E_high)
    dsm = total_screening(SM_PARTICLES, M_E, E_high, use_color=True)
    bare_t6 = INV_ALPHA_OBS - dt6
    bare_sm = INV_ALPHA_OBS - dsm
    print(f"  {name:>12s} {dt6:14.3f} {bare_t6:10.2f} {dsm:14.3f} {bare_sm:10.2f}")


# ── Section 4: Running profile ───────────────────────────────────────
print(f"\n\n{'='*70}")
print("SECTION 4: Running profile — 1/α(E) from m_e to 1 TeV")
print("=" * 70)

# Use cutoff = GUT scale for "full" running
cutoff = 2e19  # ~2×10¹⁶ GeV = GUT scale in MeV

dt6_gut = total_screening(T6_PARTICLES, M_E, cutoff)
dsm_gut = total_screening(SM_PARTICLES, M_E, cutoff, use_color=True)
bare_t6 = INV_ALPHA_OBS - dt6_gut
bare_sm = INV_ALPHA_OBS - dsm_gut

print(f"\n  Cutoff: {cutoff:.0e} MeV (~GUT scale)")
print(f"  1/α₀ (Ma): {bare_t6:.2f}")
print(f"  1/α₀ (SM):  {bare_sm:.2f}")

energy_points = [
    ("m_e (0.511 MeV)",     M_E),
    ("1 MeV",               1.0),
    ("10 MeV",             10.0),
    ("m_μ (106 MeV)",     105.658),
    ("m_π (140 MeV)",     139.570),
    ("500 MeV",           500.0),
    ("m_p (938 MeV)",     938.272),
    ("2 GeV",            2000.0),
    ("5 GeV",            5000.0),
    ("10 GeV",          10000.0),
    ("m_Z (91.2 GeV)",  M_Z),
    ("200 GeV",        200000.0),
    ("1 TeV",         1000000.0),
]

print(f"\n  {'Energy':>25s} {'1/α Ma':>10s} {'1/α SM':>10s} {'Δ':>8s}")
print(f"  {'─'*25} {'─'*10} {'─'*10} {'─'*8}")

for name, E in energy_points:
    inv_t6 = compute_running(T6_PARTICLES, bare_t6, E, cutoff)
    inv_sm = compute_running(SM_PARTICLES, bare_sm, E, cutoff, use_color=True)
    diff = inv_t6 - inv_sm
    print(f"  {name:>25s} {inv_t6:10.2f} {inv_sm:10.2f} {diff:+8.2f}")


# ── Section 5: What cutoff gives 1/α₀ = 80? ─────────────────────────
print(f"\n\n{'='*70}")
print("SECTION 5: What cutoff gives 1/α₀ = 80?")
print("=" * 70)

target_bare = 80.0
target_screening = INV_ALPHA_OBS - target_bare  # = 57.036

print(f"\n  Need: Δ(1/α) from m_e to Λ = {target_screening:.3f}")
print(f"  Full running rate (all particles above threshold):")
print(f"    Ma: {total_Q2/(3*math.pi):.4f} per unit ln(E)")

# Binary search for the cutoff
log_cutoff_low = math.log10(M_E)
log_cutoff_high = 30  # 10³⁰ MeV

for iteration in range(200):
    log_cutoff_mid = (log_cutoff_low + log_cutoff_high) / 2
    cutoff_try = 10**log_cutoff_mid
    dt6 = total_screening(T6_PARTICLES, M_E, cutoff_try)
    if dt6 < target_screening:
        log_cutoff_low = log_cutoff_mid
    else:
        log_cutoff_high = log_cutoff_mid

cutoff_for_80 = 10**((log_cutoff_low + log_cutoff_high) / 2)
dt6_check = total_screening(T6_PARTICLES, M_E, cutoff_for_80)

print(f"\n  Cutoff for 1/α₀ = 80 (Ma):")
print(f"    Λ = {cutoff_for_80:.3e} MeV = {cutoff_for_80/1000:.3e} GeV")
print(f"    Δ(1/α) = {dt6_check:.3f} (target: {target_screening:.3f})")
print(f"    log₁₀(Λ/MeV) = {math.log10(cutoff_for_80):.2f}")
print(f"    log₁₀(Λ/GeV) = {math.log10(cutoff_for_80/1000):.2f}")

# Same for SM
log_cutoff_low = math.log10(M_E)
log_cutoff_high = 30

for iteration in range(200):
    log_cutoff_mid = (log_cutoff_low + log_cutoff_high) / 2
    cutoff_try = 10**log_cutoff_mid
    dsm = total_screening(SM_PARTICLES, M_E, cutoff_try, use_color=True)
    if dsm < target_screening:
        log_cutoff_low = log_cutoff_mid
    else:
        log_cutoff_high = log_cutoff_mid

cutoff_for_80_sm = 10**((log_cutoff_low + log_cutoff_high) / 2)
dsm_check = total_screening(SM_PARTICLES, M_E, cutoff_for_80_sm, use_color=True)

print(f"\n  Cutoff for 1/α₀ = 80 (SM):")
print(f"    Λ = {cutoff_for_80_sm:.3e} MeV = {cutoff_for_80_sm/1000:.3e} GeV")
print(f"    Δ(1/α) = {dsm_check:.3f}")
print(f"    log₁₀(Λ/GeV) = {math.log10(cutoff_for_80_sm/1000):.2f}")


# ── Section 6: Check 1/α(m_Z) ────────────────────────────────────────
print(f"\n\n{'='*70}")
print("SECTION 6: 1/α(m_Z) check — does it match 128?")
print("=" * 70)

# Use several cutoffs and see what 1/α(m_Z) comes out to
test_cutoffs = [
    ("1 TeV",   1e6),
    ("10 TeV",  1e7),
    ("GUT",     2e19),
    ("Λ for α₀=80 (Ma)", cutoff_for_80),
]

print(f"\n  For each cutoff, fit 1/α₀ from 1/α(m_e) = 137, then predict 1/α(m_Z):")
print(f"\n  {'Cutoff':>25s} {'1/α₀':>8s} {'1/α(m_Z)':>10s} {'Target':>8s} {'Δ':>8s}")
print(f"  {'─'*25} {'─'*8} {'─'*10} {'─'*8} {'─'*8}")

for cname, cval in test_cutoffs:
    dt6_full = total_screening(T6_PARTICLES, M_E, cval)
    bare = INV_ALPHA_OBS - dt6_full
    inv_mZ = compute_running(T6_PARTICLES, bare, M_Z, cval)
    print(f"  {cname:>25s} {bare:8.2f} {inv_mZ:10.2f} {INV_ALPHA_MZ:8.1f} {inv_mZ - INV_ALPHA_MZ:+8.2f}")

print(f"\n  SM comparison:")
print(f"  {'Cutoff':>25s} {'1/α₀':>8s} {'1/α(m_Z)':>10s} {'Target':>8s} {'Δ':>8s}")
print(f"  {'─'*25} {'─'*8} {'─'*10} {'─'*8} {'─'*8}")

for cname, cval in [("GUT", 2e19)]:
    dsm_full = total_screening(SM_PARTICLES, M_E, cval, use_color=True)
    bare = INV_ALPHA_OBS - dsm_full
    inv_mZ = compute_running(SM_PARTICLES, bare, M_Z, cval, use_color=True)
    print(f"  {cname:>25s} {bare:8.2f} {inv_mZ:10.2f} {INV_ALPHA_MZ:8.1f} {inv_mZ - INV_ALPHA_MZ:+8.2f}")


# ── Section 7: Per-particle contribution breakdown ───────────────────
print(f"\n\n{'='*70}")
print("SECTION 7: Per-particle screening contribution (m_e to m_Z)")
print("=" * 70)

print(f"\n  {'Name':<14s} {'Mass':>10s} {'|Q|':>4s} {'b':>6s} {'ln range':>10s} {'Δ(1/α)':>10s} {'% of total':>10s}")
print(f"  {'─'*14} {'─'*10} {'─'*4} {'─'*6} {'─'*10} {'─'*10} {'─'*10}")

contributions = []
for name, mass, Q, spin_type in T6_PARTICLES:
    b = B_COEFFICIENTS[spin_type]
    if mass >= M_Z:
        ln_range = 0
        delta = 0
    else:
        m_low = max(M_E, mass)
        ln_range = math.log(M_Z / m_low)
        delta = b * Q**2 / (3 * math.pi) * ln_range
    contributions.append((name, mass, Q, b, ln_range, delta))

total_delta_mZ = sum(c[5] for c in contributions)

for name, mass, Q, b, ln_range, delta in contributions:
    pct = 100 * delta / total_delta_mZ if total_delta_mZ > 0 else 0
    print(f"  {name:<14s} {mass:10.3f} {Q:4d} {b:6.2f} {ln_range:10.3f} {delta:10.4f} {pct:9.1f}%")

print(f"\n  Total Δ(1/α) from m_e to m_Z: {total_delta_mZ:.4f}")

# SM comparison
print(f"\n  SM per-particle (m_e to m_Z):")
print(f"  {'Name':<8s} {'Mass':>10s} {'Q':>6s} {'N_c':>4s} {'Δ(1/α)':>10s}")
print(f"  {'─'*8} {'─'*10} {'─'*6} {'─'*4} {'─'*10}")

sm_total = 0
for name, mass, Q, spin_type, Nc in SM_PARTICLES:
    b = B_COEFFICIENTS[spin_type]
    if mass >= M_Z:
        delta = 0
    else:
        m_low = max(M_E, mass)
        delta = Nc * b * Q**2 / (3 * math.pi) * math.log(M_Z / m_low)
    sm_total += delta
    print(f"  {name:<8s} {mass:10.3f} {Q:6.3f} {Nc:4d} {delta:10.4f}")

print(f"\n  SM total Δ(1/α) from m_e to m_Z: {sm_total:.4f}")
print(f"  Ma total: {total_delta_mZ:.4f}")
print(f"  Ratio Ma/SM: {total_delta_mZ/sm_total:.3f}")
print(f"\n  SM measured: Δ(1/α) = 137 − 128 = 9.036")
print(f"  SM computed: {sm_total:.3f}")
print(f"  Ma computed: {total_delta_mZ:.3f}")


# ── Section 8: Sensitivity to vector meson coefficient ────────────────
print(f"\n\n{'='*70}")
print("SECTION 8: Sensitivity to vector meson VP coefficient")
print("=" * 70)

print(f"\n  The b-coefficient for spin-1 (Proca) fields is uncertain.")
print(f"  Testing b_vector = 1/3, 4/3, 7:")

for b_test in [1.0/3, 4.0/3, 7.0]:
    delta = 0
    for name, mass, Q, spin_type in T6_PARTICLES:
        if spin_type == "vector":
            b = b_test
        else:
            b = B_COEFFICIENTS[spin_type]
        if mass >= M_Z:
            continue
        m_low = max(M_E, mass)
        delta += b * Q**2 / (3 * math.pi) * math.log(M_Z / m_low)

    print(f"    b_vector = {b_test:.2f}: Δ(1/α) from m_e to m_Z = {delta:.3f}")


# ── SUMMARY ──────────────────────────────────────────────────────────
print(f"\n\n{'='*70}")
print("SUMMARY")
print(f"{'='*70}")

print(f"""
Known Ma particle content (no ghosts):
  Charged species: {len(T6_PARTICLES)}
  Total b×Q²:      {total_Q2:.2f}
  (SM total N_c×b×Q²: {sm_total_Q2:.2f})

Running from m_e to m_Z:
  Ma particles: Δ(1/α) = {total_delta_mZ:.3f}
  SM particles:  Δ(1/α) = {sm_total:.3f}
  Measured:      Δ(1/α) = 9.036

Cutoff needed for 1/α₀ = 80:
  Ma: Λ = {cutoff_for_80:.2e} MeV ({cutoff_for_80/1e6:.2e} TeV)

Key question answered:
  Does Ma particle content (no ghosts) reproduce the
  observed running of α?  Compare Ma Δ = {total_delta_mZ:.1f} to
  measured Δ = 9.0 over the range m_e to m_Z.
""")
