#!/usr/bin/env python3
"""
R26 Track 2c: Neutron mode search on the proton material sheet.

Can the neutron (m_n = 939.565 MeV, Q = 0, spin ½) live on the
proton's material sheet?  Three search strategies:

1. Single uncharged modes near m_n
2. Two-mode composites that cancel charge
3. Extra energy injected into the proton cavity

If all fail, the fallback hypothesis is: neutron = proton + electron
bound by the Ma geometry, with 0.782 MeV of binding energy.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import h, hbar, c, eps0, e, alpha as ALPHA, m_e

import numpy as np
from scipy.optimize import brentq

M_P_MEV = 938.272
M_N_MEV = 939.565
M_E_MEV = 0.51100
DM_NP_MEV = M_N_MEV - M_P_MEV   # 1.293 MeV
Q_BETA = DM_NP_MEV - M_E_MEV    # 0.782 MeV


def alpha_ma(r, s):
    """Ma convention α formula (R19 Track 8)."""
    mu = math.sqrt(1/r**2 + (2 - s)**2)
    return r**2 * mu * math.sin(2*math.pi*s)**2 / (4*math.pi * (2-s)**2)


def solve_shear_kk(r, alpha_target=ALPHA):
    """Solve α_Ma(r, s) = α_target for s."""
    s_scan = np.linspace(0.001, 0.49, 5000)
    a_scan = [alpha_ma(r, s) for s in s_scan]
    roots = []
    for i in range(len(s_scan) - 1):
        if (a_scan[i] - alpha_target) * (a_scan[i+1] - alpha_target) < 0:
            roots.append(brentq(lambda s: alpha_ma(r, s) - alpha_target,
                                s_scan[i], s_scan[i+1], xtol=1e-14))
    return roots


def mu_mode(n3, n4, r, s):
    """Dimensionless mode energy μ(n3, n4)."""
    return math.sqrt((n3/r)**2 + (n4 - n3*s)**2)


def mode_mass(n3, n4, r, s, E0_MeV):
    """Physical mass of mode (n3, n4) in MeV."""
    return E0_MeV * mu_mode(n3, n4, r, s)


def charge_factor(n3, s):
    """Relative charge ∝ sin(2πn₃s)/(n₄ − n₃s).  Only n₃ matters for sign."""
    if n3 == 0:
        return 0.0
    return math.sin(2 * math.pi * n3 * s)


def spin_label(n3):
    """Spin type based on tube winding n₃."""
    if n3 == 0:
        return "boson"
    elif abs(n3) == 1:
        return "spin-½"
    else:
        return f"spin~{abs(n3)}/2"


def main():
    print("=" * 76)
    print("R26 Track 2c: Neutron Mode Search")
    print("=" * 76)

    print(f"""
  Target: neutral spin-½ fermion at m_n = {M_N_MEV:.3f} MeV
  Proton: (1,2) mode at m_p = {M_P_MEV:.3f} MeV
  Mass difference: Δm = {DM_NP_MEV:.3f} MeV
  Electron mass:   m_e = {M_E_MEV:.3f} MeV
  Beta Q-value:    Q_β = {Q_BETA:.3f} MeV
""")

    eps_values = [0.5, 1.0, 2.0, 3.0, 5.0, 6.6]

    for eps in eps_values:
        sols = solve_shear_kk(eps)
        if not sols:
            continue
        s = sols[0]
        mu12 = mu_mode(1, 2, eps, s)
        E0 = M_P_MEV / mu12

        print(f"{'='*76}")
        print(f"  ε = {eps:.1f}   s = {s:.6f}   E₀ = {E0:.1f} MeV   μ(1,2) = {mu12:.4f}")
        print(f"{'='*76}")

        # ── SEARCH 1: All single modes near m_n ──────────────────
        print()
        print(f"  SEARCH 1: Single modes with mass near m_n ({M_N_MEV:.1f} MeV)")
        print(f"  {'-'*68}")
        print(f"  {'mode':>8s} | {'mass(MeV)':>10s} | {'Δm_n(MeV)':>10s} | "
              f"{'charged':>8s} | {'spin':>8s} | {'viable':>7s}")
        print(f"  {'─'*8}─┼─{'─'*10}─┼─{'─'*10}─┼─{'─'*8}─┼─{'─'*8}─┼─{'─'*7}")

        n3_range = range(-4, 5)
        n4_range = range(-4, 7)
        candidates = []

        for n3 in n3_range:
            for n4 in n4_range:
                if n3 == 0 and n4 == 0:
                    continue
                m = mode_mass(n3, n4, eps, s, E0)
                if m < 0.1 or m > 2000:
                    continue
                dm = m - M_N_MEV
                charged = abs(charge_factor(n3, s)) > 1e-10
                sp = spin_label(n3)
                viable = (not charged) and (sp == "spin-½") and (abs(dm) < 50)

                if abs(dm) < 200:
                    candidates.append((n3, n4, m, dm, charged, sp, viable))

        candidates.sort(key=lambda x: abs(x[3]))
        for n3, n4, m, dm, charged, sp, viable in candidates[:20]:
            ch_str = "yes" if charged else "NO"
            v_str = "✓" if viable else "✗"
            label = f"({n3},{n4})"
            print(f"  {label:>8s} | {m:10.1f} | {dm:+10.1f} | "
                  f"{ch_str:>8s} | {sp:>8s} | {v_str:>7s}")

        viable_count = sum(1 for x in candidates if x[6])
        print()
        if viable_count == 0:
            print(f"  → No viable single-mode neutron candidates.")
            print(f"    Reason: all uncharged modes (n₃=0) are bosonic.")
            print(f"    All spin-½ modes (|n₃|=1) are charged (sin(2πs)≠0).")
        else:
            print(f"  → {viable_count} viable candidate(s) found!")

        # ── SEARCH 2: Two-mode charge-cancelling composites ──────
        print()
        print(f"  SEARCH 2: Two-mode composites with net charge = 0")
        print(f"  {'-'*68}")

        composites = []
        proton_mode = (1, 2)
        m_proton = mode_mass(1, 2, eps, s, E0)

        for n3a in range(-3, 4):
            for n4a in range(-3, 5):
                if n3a == 0 and n4a == 0:
                    continue
                for n3b in range(-3, 4):
                    for n4b in range(-3, 5):
                        if n3b == 0 and n4b == 0:
                            continue
                        if (n3b, n4b) <= (n3a, n4a):
                            continue

                        q_a = charge_factor(n3a, s)
                        q_b = charge_factor(n3b, s)
                        if abs(q_a) < 1e-10 or abs(q_b) < 1e-10:
                            continue
                        if abs(q_a + q_b) > 0.01 * max(abs(q_a), abs(q_b)):
                            continue

                        m_total = mode_mass(n3a, n4a, eps, s, E0) + \
                                  mode_mass(n3b, n4b, eps, s, E0)
                        dm = m_total - M_N_MEV

                        net_n3 = n3a + n3b
                        sp = "fermion" if net_n3 % 2 == 1 else "boson"

                        composites.append((n3a, n4a, n3b, n4b, m_total, dm, sp))

        composites.sort(key=lambda x: abs(x[5]))
        print(f"  {'mode A':>8s} + {'mode B':>8s} | {'mass(MeV)':>10s} | "
              f"{'Δm_n':>10s} | {'spin':>8s}")
        print(f"  {'─'*8}───{'─'*8}─┼─{'─'*10}─┼─{'─'*10}─┼─{'─'*8}")

        for n3a, n4a, n3b, n4b, m_t, dm, sp in composites[:10]:
            print(f"  ({n3a},{n4a}) + ({n3b},{n4b}) | {m_t:10.1f} | "
                  f"{dm:+10.1f} | {sp:>8s}")

        if composites:
            best = composites[0]
            print(f"\n  Nearest composite: {best[4]:.1f} MeV "
                  f"(Δm_n = {best[5]:+.1f} MeV)")
            print(f"  Binding needed to reach m_n: {best[5]:.1f} MeV")
        else:
            print(f"  No charge-cancelling pairs found.")

        # ── SEARCH 3: Proton + electron composite ────────────────
        print()
        print(f"  SEARCH 3: Proton + electron cross-plane composite")
        print(f"  {'-'*68}")
        m_pe = M_P_MEV + M_E_MEV
        deficit = M_N_MEV - m_pe
        print(f"    m_p + m_e       = {m_pe:.3f} MeV")
        print(f"    m_n             = {M_N_MEV:.3f} MeV")
        print(f"    m_n − (m_p+m_e) = {deficit:.3f} MeV  (= Q_β)")
        print(f"    Δm/m_e          = {deficit/M_E_MEV:.3f}")
        print(f"    Δm/m_p          = {deficit/M_P_MEV:.6f}")
        print()
        print(f"    The neutron is HEAVIER than p+e by {deficit:.3f} MeV.")
        print(f"    In a bound state, this energy must come from somewhere:")
        print(f"    either stored as kinetic/potential energy in the binding,")
        print(f"    or from a neutrino mode contribution.")
        print()

        # Check neutrino mode energies at this ε
        s_nu = 0.02199
        mu_nu_11 = mu_mode(1, 1, eps, s_nu)
        mu_nu_m11 = mu_mode(-1, 1, eps, s_nu)
        mu_nu_12 = mu_mode(1, 2, eps, s_nu)

        print(f"    Neutrino mode energies (s_ν = {s_nu}, same ε = {eps}):")
        print(f"      μ(1,1)  = {mu_nu_11:.4f}")
        print(f"      μ(-1,1) = {mu_nu_m11:.4f}")
        print(f"      μ(1,2)  = {mu_nu_12:.4f}")
        print(f"    (These are dimensionless; physical scale set by ν mass.)")
        print(f"    At Σm ≈ 117 meV, m_heaviest ≈ 50 meV = 5×10⁻⁵ MeV.")
        print(f"    Neutrino energies are ~10⁴× too small to account for")
        print(f"    the {deficit:.3f} MeV deficit.")

        print()

    # ── SECTION: Energy bookkeeping summary ──────────────────────
    print()
    print("=" * 76)
    print("SUMMARY: Neutron energy bookkeeping")
    print("=" * 76)
    print(f"""
  m_n − m_p = {DM_NP_MEV:.3f} MeV        (neutron-proton mass difference)
  m_e       = {M_E_MEV:.3f} MeV        (electron mass)
  Q_β       = {Q_BETA:.3f} MeV        (beta decay Q-value = kinetic release)
  Check: {M_E_MEV:.3f} + {Q_BETA:.3f} = {M_E_MEV + Q_BETA:.3f} = Δm ✓

  In beta decay: n → p + e⁻ + ν̄_e
    The neutron's extra {DM_NP_MEV:.3f} MeV goes to:
    • {M_E_MEV:.3f} MeV → rest mass of electron
    • {Q_BETA:.3f} MeV → shared kinetic energy of e⁻ and ν̄_e
""")

    print("""
  SEARCH RESULTS:
  ──────────────────────────────────────────────────────────────

  1. SINGLE MODES: No viable neutron candidate on the proton material sheet.
     The fundamental obstacle is the charge-spin linkage (R25 F4):
     all spin-½ modes (|n₃| = 1) carry charge via sin(2πs) ≠ 0.
     All uncharged modes (n₃ = 0) are bosonic.  There is no
     uncharged fermion on a single sheared material sheet.

  2. TWO-MODE COMPOSITES: Charge-cancelling pairs exist (e.g.,
     (1,2) + (−1,−2) or (1,n) + (−1,n)), but their combined mass
     is ≈ 2m_p or higher — far above m_n.  The binding energy
     needed (~940 MeV) is unreasonably large.

  3. PROTON + ELECTRON: m_p + m_e = 938.783 MeV, which is
     0.782 MeV BELOW m_n.  The neutron is heavier than its
     constituents by the beta decay Q-value.  This is unusual
     for a bound state (normally bound states are lighter) but
     physical: the neutron is unstable precisely because it is
     heavier.

  INTERPRETATION:
  ──────────────────────────────────────────────────────────────

  The neutron cannot live as a single mode or mode pair on the
  proton material sheet.  The most natural picture is:

    neutron = proton Ma_p mode + electron Ma_e mode + 0.782 MeV

  where the extra 0.782 MeV is stored as cross-plane coupling
  energy in the Ma geometry.  This is consistent with:
  • Beta decay releasing exactly this energy
  • The neutron being unstable (stored energy wants to escape)
  • The neutron requiring both proton and electron material sheets to exist
  • The antineutrino carrying away part of the released energy

  The mechanism for cross-plane binding is a Track 4 question.
  The 0.782 MeV may relate to the cross-shear between the
  proton and electron material sheet subplanes, but quantifying this requires
  the full Ma framework.
""")


if __name__ == "__main__":
    main()
