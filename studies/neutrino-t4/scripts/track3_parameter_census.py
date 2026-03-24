#!/usr/bin/env python3
"""
R26 Track 3: Parameter census for the T⁶ model.

Enumerate every parameter in the three-torus model, identify its
constraint source (if any), and determine the system's degree of
freedom: under-, exactly-, or over-determined.

The flat T⁶ metric has 6×7/2 = 21 independent components.  We
organize these as 6 circumferences, 3 within-plane shears, and
12 cross-plane shears.
"""

import sys
import os
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lib.constants import alpha as ALPHA

# Experimental inputs
M_E_MEV   = 0.51100
M_P_MEV   = 938.272
M_N_MEV   = 939.565
DM2_21    = 7.53e-5     # eV², solar
DM2_31    = 2.53e-3     # eV², atmospheric
RATIO_31_21 = DM2_31 / DM2_21  # ≈ 33.6
SIGMA_NU  = 0.120       # eV, cosmological upper bound

THETA_12  = 33.41       # degrees, solar angle
THETA_23  = 49.0        # degrees, atmospheric angle
THETA_13  = 8.54        # degrees, reactor angle
DELTA_CP  = 195.0       # degrees, CP phase (poorly measured)

GF_GEV2   = 1.1664e-5   # Fermi constant (GeV⁻²)
M_MU_MEV  = 105.658
M_TAU_MEV = 1776.86


def main():
    print("=" * 78)
    print("R26 Track 3: T⁶ Parameter Census")
    print("=" * 78)

    # ── SECTION 1: Parameter inventory ────────────────────────────
    print()
    print("SECTION 1: Complete parameter inventory")
    print("-" * 78)
    print("""
  The flat T⁶ metric has 21 independent components (symmetric 6×6).
  We label the compact coordinates (x₁,x₂,x₃,x₄,x₅,x₆) where:
    (x₁,x₂) = electron T²
    (x₃,x₄) = neutrino T²
    (x₅,x₆) = proton T²

  Parameters decompose as:

  A. CIRCUMFERENCES (6):
     L₁, L₂ (electron), L₃, L₄ (neutrino), L₅, L₆ (proton)

  B. WITHIN-PLANE SHEARS (3):
     s₁₂ (electron), s₃₄ (neutrino), s₅₆ (proton)

  C. CROSS-PLANE SHEARS (12):
     Electron–neutrino: s₁₃, s₁₄, s₂₃, s₂₄   (4)
     Electron–proton:   s₁₅, s₁₆, s₂₅, s₂₆   (4)
     Neutrino–proton:   s₃₅, s₃₆, s₄₅, s₄₆   (4)

  Total: 6 + 3 + 12 = 21 parameters.
""")

    # Reparametrize
    print("  Equivalent reparametrization:")
    print("  ┌──────────────────────────────────────────────────────┐")
    print("  │  3 aspect ratios:  r_e = L₁/L₂, r_ν = L₃/L₄,      │")
    print("  │                    r_p = L₅/L₆                      │")
    print("  │  3 overall scales: L₂, L₄, L₆                      │")
    print("  │  3 within-plane shears: s₁₂, s₃₄, s₅₆              │")
    print("  │  12 cross-plane shears: s_ij (i,j in different T²s) │")
    print("  └──────────────────────────────────────────────────────┘")

    # ── SECTION 2: Constraints from experiment ────────────────────
    print()
    print("SECTION 2: Experimental constraints")
    print("-" * 78)
    print()

    constraints = [
        ("C1", "m_e = 0.511 MeV",
         "Sets L₂ (given r_e, s₁₂): L₂ = 2πR_e, R_e = λ̄_e μ_e(r_e,s₁₂)",
         "equality", "scale"),
        ("C2", "m_p = 938.3 MeV",
         "Sets L₆ (given r_p, s₅₆): L₆ = 2πR_p, R_p = λ̄_p μ_p(r_p,s₅₆)",
         "equality", "scale"),
        ("C3", "α = 1/137.036",
         "Fixes s₁₂(r_e) via α_KK formula (R19 Track 8 F35)",
         "equality", "shear"),
        ("C4", "α = 1/137.036",
         "Fixes s₅₆(r_p) via same α_KK formula (same charge +e)",
         "equality", "shear"),
        ("C5", "Δm²₃₁/Δm²₂₁ = 33.6",
         f"Fixes s₃₄ = 0.02199 (r-independent under KK, Track 1a)",
         "equality", "shear"),
        ("C6", "Σm_ν ≤ 120 meV",
         "Upper bound on L₄ (given r_ν, s₃₄): constrains neutrino scale",
         "inequality", "scale"),
        ("C7", "Δm²₂₁ = 7.53×10⁻⁵ eV²",
         "Fixes L₄ in terms of r_ν: combined with C5, pins neutrino scale",
         "equality", "scale"),
    ]

    print(f"  {'ID':>3s} │ {'Observable':>25s} │ {'Constrains':>55s} │ {'Type':>10s}")
    print(f"  {'─'*3}─┼─{'─'*25}─┼─{'─'*55}─┼─{'─'*10}")
    for cid, obs, desc, ctype, domain in constraints:
        print(f"  {cid:>3s} │ {obs:>25s} │ {desc[:55]:>55s} │ {ctype:>10s}")

    print(f"""
  Constraints C1–C5 are equalities (5 equations).
  C6 is an inequality (bound, not equality).
  C7 is an equality if we treat Δm²₂₁ as exactly measured.

  These 6 equalities constrain:
    • L₂ (from C1, given r_e)
    • L₆ (from C2, given r_p)
    • s₁₂ (from C3, given r_e)
    • s₅₆ (from C4, given r_p)
    • s₃₄ (from C5, independent of r_ν)
    • L₄ (from C7, given r_ν)

  Remaining free after C1–C7:  21 − 6 = 15 parameters
    • r_e, r_ν, r_p              (3 aspect ratios)
    • L₁, L₃, L₅                (3 tube circumferences — but
                                   L₁ = r_e L₂, L₃ = r_ν L₄,
                                   L₅ = r_p L₆, so these are
                                   determined by the aspect ratios)
    • 12 cross-plane shears       (completely unconstrained so far)

  Correction: L₁ = r_e × L₂ etc., so the tube circumferences
  are NOT independent — they're determined by the aspect ratio
  and the ring circumference.  The 6 circumferences reduce to
  3 aspect ratios + 3 ring scales.  With C1, C2, C7 fixing the
  3 ring scales (given r's), we have:

  FREE PARAMETERS: 3 aspect ratios + 12 cross-shears = 15
""")

    # ── SECTION 3: Potential additional constraints ───────────────
    print()
    print("SECTION 3: Potential additional constraints")
    print("-" * 78)
    print()

    potential = [
        ("P1", "PMNS θ₁₂ = 33.4°",
         "e–ν cross-shears (s₁₃,s₁₄,s₂₃,s₂₄)", "4 shears", "measured"),
        ("P2", "PMNS θ₂₃ = 49.0°",
         "e–ν cross-shears", "", "measured"),
        ("P3", "PMNS θ₁₃ = 8.54°",
         "e–ν cross-shears", "", "measured"),
        ("P4", "PMNS δ_CP = 195°",
         "e–ν cross-shears", "", "poorly measured"),
        ("P5", "G_F = 1.166×10⁻⁵ GeV⁻²",
         "Overall coupling strength of cross-plane shears", "1 combination", "measured"),
        ("P6", "m_n − m_p = 1.293 MeV",
         "e–p cross-shears (s₁₅,s₁₆,s₂₅,s₂₆)", "4 shears", "measured"),
        ("P7", "τ_n = 880 s",
         "Coupling between all three T² planes", "combination", "measured"),
        ("P8", "m_μ = 105.7 MeV",
         "Unknown — may require excited modes or separate T²", "?", "measured"),
        ("P9", "m_τ = 1777 MeV",
         "Unknown — may require excited modes or separate T²", "?", "measured"),
    ]

    for pid, obs, target, scope, status in potential:
        print(f"  {pid}: {obs}")
        print(f"      → {target}")
        if scope:
            print(f"      Scope: {scope}")
        print()

    # ── SECTION 4: Constraint counting ────────────────────────────
    print()
    print("SECTION 4: Degrees of freedom")
    print("-" * 78)
    print()

    print("  PARAMETERS:")
    print(f"    Aspect ratios (r_e, r_ν, r_p):          3")
    print(f"    Cross-plane shears:                     12")
    print(f"    ─────────────────────────────────────────")
    print(f"    Total free:                             15")
    print()
    print("  ESTABLISHED CONSTRAINTS (C1–C7):           6")
    print("  (These fix: L₂, L₄, L₆, s₁₂, s₃₄, s₅₆)")
    print()
    print("  POTENTIAL CONSTRAINTS (P1–P7):              7")
    print("  (PMNS: 4, G_F: 1, Δm_np: 1, τ_n: 1)")
    print()

    n_params = 15
    n_established = 0  # already subtracted in the 15
    n_potential = 7

    print(f"  If PMNS + G_F + Δm_np + τ_n all map to cross-shears:")
    print(f"    Free = 15 − 7 = 8 (under-determined)")
    print()
    print(f"  If muon and tau masses also constrain parameters:")
    print(f"    Free = 15 − 9 = 6 (still under-determined)")
    print()
    print(f"  ASSESSMENT: The T⁶ model is UNDER-DETERMINED with")
    print(f"  current observables.  At least 6–8 parameters (mainly")
    print(f"  cross-shears) have no known experimental handle.")
    print()
    print(f"  However, many of the 12 cross-shears may be zero or")
    print(f"  related by symmetry.  Geometric consistency of T⁶")
    print(f"  (positive-definite metric) imposes inequalities that")
    print(f"  may further reduce the viable parameter space.")

    # ── SECTION 5: What the three aspect ratios control ───────────
    print()
    print()
    print("SECTION 5: Role of the three aspect ratios")
    print("-" * 78)
    print()

    print("  r_e (electron aspect ratio):")
    print("    Controls: electron T² shape, s₁₂ via α formula")
    print("    Observable consequences: electron g−2 correction (?),")
    print("      electron form factor at high Q²")
    print("    Status: FREE (no clean experimental constraint)")
    print()
    print("  r_ν (neutrino aspect ratio):")
    print("    Controls: neutrino T² shape, absolute mass scale")
    print("    Observable consequences: individual neutrino masses,")
    print("      Σm_ν (cosmological)")
    print("    Status: FREE (Δm² ratio is r-independent; absolute")
    print("      scale depends on r_ν but Σm is only bounded)")
    print()

    # Compute Σm vs r_ν
    s34 = 0.02199
    print("    Σm_ν predictions at s₃₄ = 0.02199:")
    print(f"    {'r_ν':>6s} │ {'m₁(meV)':>10s} │ {'m₂(meV)':>10s} │ "
          f"{'m₃(meV)':>10s} │ {'Σm(meV)':>10s} │ {'viable':>7s}")
    print(f"    {'─'*6}─┼─{'─'*10}─┼─{'─'*10}─┼─{'─'*10}─┼─{'─'*10}─┼─{'─'*7}")

    for r_nu in [0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 50.0]:
        mu11 = math.sqrt(1/r_nu**2 + (1 - s34)**2)
        mum11 = math.sqrt(1/r_nu**2 + (1 + s34)**2)
        mu12 = math.sqrt(1/r_nu**2 + (2 - s34)**2)

        dm2_21_dimless = mum11**2 - mu11**2  # = 4s₃₄
        dm2_31_dimless = mu12**2 - mu11**2    # = 3 - 2s₃₄

        E0_sq = DM2_21 / dm2_21_dimless  # eV²
        E0 = math.sqrt(E0_sq) * 1e3  # meV

        m1 = E0 * mu11
        m2 = E0 * mum11
        m3 = E0 * mu12
        sigma = m1 + m2 + m3
        viable = "✓" if sigma <= 120 else "✗"

        print(f"    {r_nu:6.1f} │ {m1:10.2f} │ {m2:10.2f} │ "
              f"{m3:10.2f} │ {sigma:10.2f} │ {viable:>7s}")

    print()
    print("  r_p (proton aspect ratio):")
    print("    Controls: proton T² shape, s₅₆ via α formula")
    print("    Observable consequences: proton mode spectrum,")
    print("      neutron binding energy (via cross-plane coupling)")
    print("    Status: FREE")

    # ── SECTION 6: The observables scorecard ──────────────────────
    print()
    print()
    print("SECTION 6: Observables scorecard")
    print("-" * 78)
    print()

    scorecard = [
        ("m_e", "0.511 MeV", "INPUT", "sets electron scale"),
        ("m_p", "938.3 MeV", "INPUT", "sets proton scale"),
        ("Q_e", "−e", "DERIVED", "from (1,2) mode + shear → α"),
        ("Q_p", "+e", "DERIVED", "same mechanism, same α formula"),
        ("spin_e", "½", "DERIVED", "from |n₁|=1 tube winding"),
        ("spin_p", "½", "DERIVED", "from |n₅|=1 tube winding"),
        ("g_e", "≈2", "DERIVED", "leading order from (1,2) winding ratio"),
        ("g_p", "—", "NOT YET", "requires quark substructure or full mode calc"),
        ("α", "1/137", "INPUT", "fixes within-plane shears s₁₂, s₅₆"),
        ("Δm²₃₁/Δm²₂₁", "33.6", "INPUT", "fixes s₃₄ = 0.02199"),
        ("Σm_ν", "≤120 meV", "PREDICTION", f"117 meV at ε≥3.2 (Track 1f)"),
        ("ν spin", "½", "DERIVED", "from |n₃|=1 on neutrino T²"),
        ("ν charge", "0", "DERIVED", "from n₁=n₅=0 on e/p T²s"),
        ("m_n−m_p", "1.293 MeV", "NOT YET", "requires T⁶ cross-plane coupling"),
        ("τ_n", "880 s", "NOT YET", "requires cross-plane coupling rates"),
        ("PMNS θ₁₂", "33.4°", "NOT YET", "maps to e–ν cross-shears"),
        ("PMNS θ₂₃", "49.0°", "NOT YET", "maps to e–ν cross-shears"),
        ("PMNS θ₁₃", "8.54°", "NOT YET", "maps to e–ν cross-shears"),
        ("m_μ", "105.7 MeV", "NOT YET", "unknown placement in T⁶"),
        ("m_τ", "1777 MeV", "NOT YET", "unknown placement in T⁶"),
    ]

    print(f"  {'Observable':>15s} │ {'Value':>12s} │ {'Status':>10s} │ Notes")
    print(f"  {'─'*15}─┼─{'─'*12}─┼─{'─'*10}─┼─{'─'*30}")
    for obs, val, status, note in scorecard:
        print(f"  {obs:>15s} │ {val:>12s} │ {status:>10s} │ {note}")

    # ── SECTION 7: Summary ────────────────────────────────────────
    print()
    print()
    print("SECTION 7: Track 3 Summary")
    print("=" * 78)
    print(f"""
  PARAMETERS:  21 total in the T⁶ metric
    6 constrained by established physics (C1–C7):
      L₂ (m_e), L₄ (Δm²₂₁), L₆ (m_p), s₁₂ (α), s₃₄ (Δm² ratio), s₅₆ (α)
    15 remaining free:
      3 aspect ratios (r_e, r_ν, r_p)
      12 cross-plane shears

  OBSERVABLES:  ≥16 independent measurements available
    5 used as inputs: m_e, m_p, α, Δm² ratio, Δm²₂₁
    6 derived (predictions or consistency checks):
      Q_e, Q_p, spin_e, spin_p, g_e, ν charge
    1 testable prediction: Σm_ν ≈ 117 meV
    ≥8 not yet connected to parameters:
      m_n−m_p, τ_n, PMNS (3+1), m_μ, m_τ, G_F

  STATUS:  UNDER-DETERMINED
    15 free parameters vs ≤9 potential additional constraints
    (PMNS 4, G_F 1, Δm_np 1, τ_n 1, m_μ 1, m_τ 1)
    → at least 6 unconstrained parameters remain

  KEY INSIGHT:
    The model has 12 cross-plane shears but only ~7 observables
    that plausibly map to them.  Either:
    (a) symmetry or geometric consistency reduces the 12 to fewer
        independent parameters, or
    (b) the model is genuinely under-determined and some cross-
        shears are not physically observable.

  WHAT WOULD CLOSE THE SYSTEM:
    If the 3 aspect ratios could be fixed (by a principle we
    haven't identified), the 12 cross-shears would face ≥7
    constraints from 15 free → potentially solvable.  The
    aspect ratios are the critical open problem.
""")


if __name__ == "__main__":
    main()
