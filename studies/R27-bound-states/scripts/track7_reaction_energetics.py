#!/usr/bin/env python3
"""
R27 Track 7: Reaction energetics.

Do Ma mode energies satisfy conservation laws in known reactions?

For each well-measured decay or scattering process, compare:
  (a) Observed: ΣM_in − ΣM_out  (kinetic Q-value from PDG masses)
  (b) Mode:     ΣE_in − ΣE_out  (using nearest Ma mode energies)

If the Ma picture is self-consistent, mode-level Q-values should
be non-negative for allowed decays and roughly track the observed
Q-values.

Also checks: do quantum numbers (charge, spin parity) conserve
at the mode level?

Uses the Track 5 catalog at pinned point (r_p=8.906, σ_ep=−0.0906).
"""

import sys
import os
import math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_solver import self_consistent_metric
from lib.ma import mode_energy, mode_charge, mode_spin, M_P_MEV, M_E_MEV

R_E, R_NU, R_P = 6.6, 5.0, 8.906
SIGMA_EP = -0.09064


# ── Mode catalog from Track 5 ────────────────────────────────────
# key: particle symbol
# value: (observed_mass, mode_n, mode_E, charge, spin_count)

MODE_DATA = {
    'e':   (  0.511, ( 1, 2, 0, 0, 0, 0),    0.511, -1, 1),
    'p':   (938.272, ( 0, 0, 0, 0, 1, 2),  938.272, +1, 1),
    'n':   (939.565, ( 0,-2, 1, 0, 0, 2),  939.565,  0, 1),
    'μ':   (105.658, (-1, 5, 0, 0,-2, 0),  105.658, -1, 1),
    'τ':   (1776.86, (-1, 8, 0, 0,-2,-4), 1876.375, -1, 1),
    'π+':  (139.570, ( 2,-8, 1, 0, 3, 0),  158.480, +1, 0),
    'π0':  (134.977, (-3, 8, 0, 0,-3, 0),  158.484,  0, 0),
    'K+':  (493.677, (-4,-8, 1, 0,-3,-1),  488.008, +1, 0),
    'K0':  (497.611, (-3,-8, 0, 0,-3, 1),  503.710,  0, 0),
    'η':   (547.862, (-5,-8, 0, 0,-5, 1),  551.172,  0, 0),
    "η'":  (957.78,  (-3,-8, 0, 0,-3, 2),  961.070,  0, 0),
    'ρ0':  (775.26,  (-7, 8, 0, 0,-7, 1),  613.426,  0, 2),
    'ω':   (782.66,  (-1, 8, 0, 0,-1,-2),  938.104,  0, 2),
    'φ':   (1019.461,(-7,-8, 0, 0,-7, 2), 1027.982,  0, 2),
    'Λ':   (1115.683,(-8, 8, 1, 0,-8, 2), 1050.875,  0, 1),
    'Σ+':  (1189.37, ( 7,-8, 0, 0, 8,-2), 1050.877, +1, 1),
    'Ξ0':  (1314.86, (-2, 8, 1, 0,-2,-3), 1407.566,  0, 1),
    'Δ++': (1232.0,  (-1,-8, 1, 0, 1, 3), 1407.407, +2, 3),
    'ν':   (0.0,     ( 0, 0, 1, 1, 0, 0),    0.0,    0, 1),
    'γ':   (0.0,      None,                   0.0,    0, 0),
}


def obs_mass(key):
    return MODE_DATA[key][0]


def mode_E(key):
    return MODE_DATA[key][2]


def mode_Q(key):
    return MODE_DATA[key][3]


def mode_S(key):
    return MODE_DATA[key][4]


# ── Reactions ─────────────────────────────────────────────────────
# Each: (label, [inputs], [outputs], conserves_spin_note)
# For antiparticles: charge flips, spin stays same.
# We track charge conservation explicitly.
# 'ν' stands for any neutrino (mass ≈ 0).
# 'γ' stands for photon.

REACTIONS = [
    # Leptonic decays
    ("n → p + e⁻ + ν̄ₑ",
     [('n', +1)],
     [('p', +1), ('e', +1), ('ν', -1)],
     "beta decay"),

    ("μ⁻ → e⁻ + ν̄ₑ + νμ",
     [('μ', +1)],
     [('e', +1), ('ν', -1), ('ν', +1)],
     "muon decay"),

    ("τ⁻ → μ⁻ + ν̄μ + ντ",
     [('τ', +1)],
     [('μ', +1), ('ν', -1), ('ν', +1)],
     "tau leptonic"),

    ("τ⁻ → e⁻ + ν̄ₑ + ντ",
     [('τ', +1)],
     [('e', +1), ('ν', -1), ('ν', +1)],
     "tau → electron"),

    # Pion decays
    ("π⁺ → μ⁺ + νμ",
     [('π+', +1)],
     [('μ', -1), ('ν', +1)],
     "pion leptonic"),

    ("π⁰ → γ + γ",
     [('π0', +1)],
     [('γ', +1), ('γ', +1)],
     "pion neutral"),

    # Kaon decays
    ("K⁺ → μ⁺ + νμ",
     [('K+', +1)],
     [('μ', -1), ('ν', +1)],
     "kaon leptonic"),

    ("K⁺ → π⁺ + π⁰",
     [('K+', +1)],
     [('π+', +1), ('π0', +1)],
     "kaon → 2π"),

    ("K⁺ → π⁺ + π⁺ + π⁻",
     [('K+', +1)],
     [('π+', +1), ('π+', +1), ('π+', -1)],
     "kaon → 3π"),

    ("K⁰ → π⁺ + π⁻",
     [('K0', +1)],
     [('π+', +1), ('π+', -1)],
     "K_S → 2π"),

    # Eta decays
    ("η → γ + γ",
     [('η', +1)],
     [('γ', +1), ('γ', +1)],
     "eta → 2γ"),

    ("η → π⁰ + π⁰ + π⁰",
     [('η', +1)],
     [('π0', +1), ('π0', +1), ('π0', +1)],
     "eta → 3π⁰"),

    # Vector meson decays
    ("ρ⁰ → π⁺ + π⁻",
     [('ρ0', +1)],
     [('π+', +1), ('π+', -1)],
     "rho → 2π"),

    ("ω → π⁺ + π⁻ + π⁰",
     [('ω', +1)],
     [('π+', +1), ('π+', -1), ('π0', +1)],
     "omega → 3π"),

    ("φ → K⁺ + K⁻",
     [('φ', +1)],
     [('K+', +1), ('K+', -1)],
     "phi → 2K"),

    # Baryon decays
    ("Λ → p + π⁻",
     [('Λ', +1)],
     [('p', +1), ('π+', -1)],
     "lambda → pπ"),

    ("Λ → n + π⁰",
     [('Λ', +1)],
     [('n', +1), ('π0', +1)],
     "lambda → nπ⁰"),

    ("Σ⁺ → p + π⁰",
     [('Σ+', +1)],
     [('p', +1), ('π0', +1)],
     "sigma → pπ⁰"),

    ("Σ⁺ → n + π⁺",
     [('Σ+', +1)],
     [('n', +1), ('π+', +1)],
     "sigma → nπ⁺"),

    ("Ξ⁰ → Λ + π⁰",
     [('Ξ0', +1)],
     [('Λ', +1), ('π0', +1)],
     "xi → Λπ⁰"),

    ("Δ⁺⁺ → p + π⁺",
     [('Δ++', +1)],
     [('p', +1), ('π+', +1)],
     "delta → pπ"),
]


def reaction_charge(particles):
    """Total charge for a reaction side. sign = +1 for particle, -1 for anti."""
    total = 0
    for key, sign in particles:
        q = mode_Q(key)
        total += sign * q
    return total


def reaction_obs_E(particles):
    """Total observed mass for a reaction side."""
    return sum(obs_mass(key) for key, sign in particles)


def reaction_mode_E(particles):
    """Total mode energy for a reaction side."""
    return sum(mode_E(key) for key, sign in particles)


def section(n, title):
    print(f"\n{'='*70}")
    print(f"  SECTION {n}: {title}")
    print(f"{'='*70}\n")


def main():
    # ── Section 1: Observed Q-values ──────────────────────────────────
    section(1, "Observed Q-values (from PDG masses)")

    print(f"  {'Reaction':>30s}  {'ΣM_in':>10s}  {'ΣM_out':>10s}  "
          f"{'Q_obs':>10s}  {'ΔQ':>6s}  Note")
    print(f"  {'-'*80}")

    for label, ins, outs, note in REACTIONS:
        M_in = reaction_obs_E(ins)
        M_out = reaction_obs_E(outs)
        Q = M_in - M_out
        sign = "✓" if Q >= 0 else "✗"
        print(f"  {label:>30s}  {M_in:10.3f}  {M_out:10.3f}  "
              f"{Q:+10.3f}  {sign:>6s}  {note}")

    # ── Section 2: Mode-level Q-values ────────────────────────────────
    section(2, "Mode-level Q-values (from nearest Ma modes)")

    print(f"  {'Reaction':>30s}  {'ΣE_in':>10s}  {'ΣE_out':>10s}  "
          f"{'Q_mode':>10s}  {'ΔQ':>6s}  Note")
    print(f"  {'-'*80}")

    results = []
    for label, ins, outs, note in REACTIONS:
        E_in = reaction_mode_E(ins)
        E_out = reaction_mode_E(outs)
        Q_mode = E_in - E_out
        sign = "✓" if Q_mode >= 0 else "✗"
        print(f"  {label:>30s}  {E_in:10.3f}  {E_out:10.3f}  "
              f"{Q_mode:+10.3f}  {sign:>6s}  {note}")
        results.append((label, ins, outs, note, Q_mode))

    # ── Section 3: Comparison ─────────────────────────────────────────
    section(3, "Q_obs vs Q_mode comparison")

    print(f"  {'Reaction':>30s}  {'Q_obs':>10s}  {'Q_mode':>10s}  "
          f"{'Q_mode−Q_obs':>12s}  {'Status':>10s}")
    print(f"  {'-'*80}")

    n_ok = 0
    n_sign_flip = 0
    n_total = 0
    q_diffs = []

    for label, ins, outs, note in REACTIONS:
        Q_obs = reaction_obs_E(ins) - reaction_obs_E(outs)
        Q_mode = reaction_mode_E(ins) - reaction_mode_E(outs)
        diff = Q_mode - Q_obs
        n_total += 1
        q_diffs.append(diff)

        if Q_obs >= 0 and Q_mode >= 0:
            status = "both ✓"
            n_ok += 1
        elif Q_obs >= 0 and Q_mode < 0:
            status = "SIGN FLIP"
            n_sign_flip += 1
        elif Q_obs < 0 and Q_mode >= 0:
            status = "mode allows"
        else:
            status = "both ✗"
            n_ok += 1

        print(f"  {label:>30s}  {Q_obs:+10.3f}  {Q_mode:+10.3f}  "
              f"{diff:+12.3f}  {status:>10s}")

    print(f"\n  Reactions checked: {n_total}")
    print(f"  Sign-consistent:  {n_ok}")
    print(f"  Sign flips:       {n_sign_flip}")

    # ── Section 4: Charge conservation ────────────────────────────────
    section(4, "Charge conservation at mode level")

    print(f"  {'Reaction':>30s}  {'Q_in':>6s}  {'Q_out':>6s}  {'ΔQ':>6s}  Status")
    print(f"  {'-'*60}")

    for label, ins, outs, note in REACTIONS:
        q_in = reaction_charge(ins)
        q_out = reaction_charge(outs)
        dq = q_in - q_out
        status = "✓" if dq == 0 else "✗ VIOLATION"
        print(f"  {label:>30s}  {q_in:+6d}  {q_out:+6d}  {dq:+6d}  {status}")

    # ── Section 5: Gap cancellation ───────────────────────────────────
    section(5, "Gap cancellation in reactions")

    print("  Do mass gaps cancel in reactions? If a particle's observed")
    print("  mass differs from its mode energy, does the difference")
    print("  cancel between reactants and products?\n")

    print(f"  {'Reaction':>30s}  {'Σgap_in':>10s}  {'Σgap_out':>10s}  "
          f"{'Net gap':>10s}")
    print(f"  {'-'*70}")

    for label, ins, outs, note in REACTIONS:
        gap_in = sum(obs_mass(k) - mode_E(k) for k, s in ins)
        gap_out = sum(obs_mass(k) - mode_E(k) for k, s in outs)
        net = gap_in - gap_out
        print(f"  {label:>30s}  {gap_in:+10.3f}  {gap_out:+10.3f}  "
              f"{net:+10.3f}")

    # ── Section 6: Energy budget ──────────────────────────────────────
    section(6, "Energy accounting for representative decays")

    print("  For each decay, track where the energy goes:\n")

    examples = [
        ("n → p + e⁻ + ν̄ₑ", 'n', [('p',+1),('e',+1),('ν',-1)]),
        ("π⁺ → μ⁺ + νμ", 'π+', [('μ',-1),('ν',+1)]),
        ("K⁺ → π⁺ + π⁰", 'K+', [('π+',+1),('π0',+1)]),
        ("Λ → p + π⁻", 'Λ', [('p',+1),('π+',-1)]),
    ]

    for label, parent, products in examples:
        m_parent = obs_mass(parent)
        E_parent = mode_E(parent)
        gap_parent = m_parent - E_parent

        m_products = sum(obs_mass(k) for k,s in products)
        E_products = sum(mode_E(k) for k,s in products)
        gap_products = m_products - E_products

        Q_obs = m_parent - m_products
        Q_mode = E_parent - E_products

        print(f"  {label}:")
        print(f"    Parent mass:       {m_parent:10.3f} MeV")
        print(f"    Parent mode E:     {E_parent:10.3f} MeV  (gap = {gap_parent:+.3f})")
        print(f"    Product masses:    {m_products:10.3f} MeV")
        print(f"    Product mode Es:   {E_products:10.3f} MeV  (Σgap = {gap_products:+.3f})")
        print(f"    Q_obs (kinetic):   {Q_obs:+10.3f} MeV")
        print(f"    Q_mode:            {Q_mode:+10.3f} MeV")
        print(f"    Gap imbalance:     {gap_parent - gap_products:+10.3f} MeV")
        print()

    # ── Section 7: Summary ────────────────────────────────────────────
    section(7, "Summary")

    diffs = np.array(q_diffs)
    print(f"  Reactions tested:        {n_total}")
    print(f"  Sign-consistent (Q≥0):   {n_ok} / {n_total}")
    print(f"  Sign flips:              {n_sign_flip}")
    print(f"  Mean |Q_mode − Q_obs|:   {np.mean(np.abs(diffs)):.1f} MeV")
    print(f"  Median |Q_mode − Q_obs|: {np.median(np.abs(diffs)):.1f} MeV")
    print()

    if n_sign_flip == 0:
        print("  All observed decays remain energetically allowed")
        print("  at the mode level.")
    else:
        print(f"  {n_sign_flip} reaction(s) have sign flips: mode-level")
        print("  Q-value is negative for an observed allowed decay.")
        print("  These may indicate mode assignment issues or multi-mode")
        print("  effects.")


if __name__ == '__main__':
    main()
