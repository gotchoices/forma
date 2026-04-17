"""
R59 Track 1: Build the metric with time.

The 10D metric: 6 Ma + 3 S + 1 t (Lorentzian signature).

Key difference from R55: the time diagonal is NEGATIVE (-1),
giving Lorentzian signature.  This changes the Schur complement:

  Euclidean (R55):  A_eff = A - b bᵀ / (+1) = A - b bᵀ
     → coupling REDUCES effective metric → energy INCREASES

  Lorentzian (R59): A_eff = A - b bᵀ / (-1) = A + b bᵀ
     → coupling INCREASES effective metric → energy DECREASES

The mass-shell condition for a mode with Ma winding n, at rest
in S, with energy E:

  g^{μν} k_μ k_ν = 0

where k = (n₁/L₁, ..., n₆/L₆, 0, 0, 0, E/(ℏc)).

This gives a quadratic in E that determines the rest mass
including the Ma-t coupling correction.

Three approaches tested:
  A. Schur complement on time (integrate out t, effective spatial metric)
  B. Schur complement on Ma (integrate out Ma, effective St metric)
  C. Direct mass-shell condition (solve the full dispersion relation)

All three should agree.

Important: KK theory (compact momentum) may not apply directly
to MaSt (standing waves).  This computation tests what actually
happens — no KK assumptions imported.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np
from lib.metric import Metric
from lib.ma_model_d import _TWO_PI_HC, M_E_MEV, M_P_MEV

ALPHA = 1.0 / 137.036
TWO_PI_HC = _TWO_PI_HC  # ≈ 1239.8 MeV·fm

m = Metric.model_E()
A_6x6 = m.Gt       # 6×6 dimensionless Ma metric
L_6 = m.L           # circumferences (fm)

MODES = {
    'electron':  ((1, 2, 0, 0, 0, 0),    0.511,   -1),
    'proton':    ((0, 0, -2, 2, 1, 3),  938.272,   +1),
    'neutron':   ((0, -4, -1, 2, 0, -3), 939.565,   0),
    'ν₁':       ((0, 0, 1, 1, 0, 0),     2.92e-5,  0),
    'deuteron':  ((0, 0, 0, 0, 2, 6),  1875.61,    +2),
}


def build_10d_metric(A_6x6, b_Ma_t, b_Ma_S=None):
    """
    Build the 10×10 metric: 6 Ma + 3 S + 1 t.

    Indices 0-5: Ma, 6-8: S, 9: t

    Parameters
    ----------
    A_6x6 : Ma metric (dimensionless)
    b_Ma_t : ndarray (6,) — Ma-t off-diagonal coupling
    b_Ma_S : ndarray (6,3) or None — Ma-S off-diagonal (default: zero)
    """
    G = np.zeros((10, 10))

    # Ma block (0-5)
    G[:6, :6] = A_6x6

    # S block (6-8): +1 (spatial, Euclidean)
    G[6, 6] = 1.0
    G[7, 7] = 1.0
    G[8, 8] = 1.0

    # t block (9): -1 (Lorentzian)
    G[9, 9] = -1.0

    # Ma-t coupling (column/row 9, rows/cols 0-5)
    for i in range(6):
        G[i, 9] = b_Ma_t[i]
        G[9, i] = b_Ma_t[i]

    # Ma-S coupling (optional)
    if b_Ma_S is not None:
        for i in range(6):
            for j in range(3):
                G[i, 6+j] = b_Ma_S[i, j]
                G[6+j, i] = b_Ma_S[i, j]

    return G


def bare_mode_energy(n6):
    """Mode energy on the bare 6×6 Ma metric (no coupling)."""
    return m.mode_energy(n6)


def approach_A_schur_time(G10, L_6, n6):
    """
    Approach A: Integrate out time via Schur complement.

    The effective 9×9 spatial metric is:
      G_eff = G_spatial - g_t × g_t^T / g_tt

    where g_t is column 9 of the 10×10 (excluding the diagonal),
    and g_tt = -1.

    Division by -1 gives: G_eff = G_spatial + g_t ⊗ g_t
    (the coupling ADDS to the spatial metric)
    """
    # Extract spatial block (indices 0-8)
    G_spatial = G10[:9, :9].copy()

    # Extract time coupling column (excluding diagonal)
    g_t = G10[:9, 9].copy()
    g_tt = G10[9, 9]  # = -1

    # Schur complement
    G_eff = G_spatial - np.outer(g_t, g_t) / g_tt
    # = G_spatial + g_t ⊗ g_t  (because g_tt = -1)

    # Mode energy on the effective 9×9
    L_9 = np.concatenate([L_6, [1.0, 1.0, 1.0]])
    n_tilde = np.concatenate([np.array(n6, dtype=float) / L_6, [0, 0, 0]])

    try:
        G_inv = np.linalg.inv(G_eff)
        E2 = TWO_PI_HC**2 * n_tilde @ G_inv @ n_tilde
    except np.linalg.LinAlgError:
        return np.nan

    return math.sqrt(max(E2, 0))


def approach_C_mass_shell(G10, L_6, n6):
    """
    Approach C: Direct mass-shell condition.

    For a mode with Ma winding n, at rest in S, with energy E:
    The full 10D wavevector is k = (n/L, 0, 0, 0, E/(hbar c))

    The mass-shell condition: k^μ g_μν k^ν = 0

    In matrix form: kᵀ G⁻¹ k = 0

    But k contains E, so this is a quadratic in E.

    Actually, the standard approach: the mode energy satisfies
    g^{μν} p_μ p_ν + m² = 0 for a massive particle in 4D.
    But in the full 10D, the particle is "massless" (a photon),
    so g^{μν} k_μ k_ν = 0.

    k = (n₁/L₁, ..., n₆/L₆, 0, 0, 0, ω)
    where ω = E / (2π ℏc) and we solve for E.

    g^{μν} k_μ k_ν = Σ_{a,b in Ma} g^{ab} (n_a/L_a)(n_b/L_b)
                    + g^{tt} ω²
                    + 2 Σ_{a in Ma} g^{a,t} (n_a/L_a) ω
                    = 0

    This is: A_inv_term + g^{tt} ω² + 2 cross_term × ω = 0
    """
    try:
        G_inv = np.linalg.inv(G10)
    except np.linalg.LinAlgError:
        return np.nan

    n_tilde = np.array(n6, dtype=float) / L_6

    # Coefficients of the quadratic in ω:
    # a ω² + b ω + c = 0

    # a = g^{tt} (the (9,9) component of G⁻¹)
    a_coeff = G_inv[9, 9]

    # b = 2 Σ_a g^{a,t} (n_a/L_a) where a runs over Ma (0-5)
    b_coeff = 2.0 * np.dot(G_inv[:6, 9], n_tilde)

    # c = Σ_{a,b} g^{ab} (n_a/L_a)(n_b/L_b) where a,b run over Ma (0-5)
    c_coeff = n_tilde @ G_inv[:6, :6] @ n_tilde

    # Solve: a ω² + b ω + c = 0
    discriminant = b_coeff**2 - 4 * a_coeff * c_coeff
    if discriminant < 0:
        return np.nan

    # Two solutions (particle and antiparticle)
    omega_plus = (-b_coeff + math.sqrt(discriminant)) / (2 * a_coeff)
    omega_minus = (-b_coeff - math.sqrt(discriminant)) / (2 * a_coeff)

    # E = 2πℏc × |ω|  (take the positive energy solution)
    E_plus = TWO_PI_HC * abs(omega_plus)
    E_minus = TWO_PI_HC * abs(omega_minus)

    # Return the physical (positive, smaller) mass
    return min(E_plus, E_minus)


def main():
    print("=" * 75)
    print("R59 Track 1: Build the metric with time")
    print("=" * 75)
    print()
    print("  Metric: 6 Ma + 3 S + 1 t = 10D, Lorentzian signature")
    print("  Ma metric: model-E (flat, with internal shears)")
    print("  Time diagonal: g_tt = -1")
    print("  New: Ma-t off-diagonal entries")
    print()

    # ── Section 1: Bare metric (no coupling) ───────────────
    print("─" * 75)
    print("Section 1: Bare metric — no Ma-t or Ma-S coupling")
    print("─" * 75)
    print()

    b_zero = np.zeros(6)
    G10_bare = build_10d_metric(A_6x6, b_zero)

    print("  10×10 metric diagonal: ", np.diag(G10_bare))
    print()

    # Check: bare mode energies should match model-E
    print("  Bare mode energies (should match model-E):")
    print(f"  {'Mode':>10s}  {'E_model-E':>10s}  {'E_SchurT':>10s}  {'E_shell':>10s}  {'match?':>8s}")
    print(f"  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*8}")

    for name, (n6, m_obs, Q) in MODES.items():
        E_bare = bare_mode_energy(n6)
        E_schur = approach_A_schur_time(G10_bare, L_6, n6)
        E_shell = approach_C_mass_shell(G10_bare, L_6, n6)
        match = "✓" if (abs(E_bare - E_schur) / E_bare < 0.001 and
                        abs(E_bare - E_shell) / E_bare < 0.001) else "✗"
        print(f"  {name:>10s}  {E_bare:10.4f}  {E_schur:10.4f}  {E_shell:10.4f}  {match:>8s}")

    print()

    # ── Section 2: Ma-t coupling — tube dimensions ─────────
    print("─" * 75)
    print("Section 2: Ma-t coupling on TUBE dimensions (charge direction)")
    print("  b_Ma-t = [±σ, 0, 0, 0, ±σ, 0] (e-tube and p-tube)")
    print("─" * 75)
    print()

    print(f"  {'σ':>8s}  {'E_e':>8s}  {'E_p':>8s}  {'Δe%':>7s}  {'Δp%':>7s}  {'sig?':>5s}")
    print(f"  {'─'*8}  {'─'*8}  {'─'*8}  {'─'*7}  {'─'*7}  {'─'*5}")

    for sigma in [0.001, 0.01, 0.05, 0.1, 0.2, 0.3, 0.5]:
        b = np.array([-sigma, 0, 0, 0, +sigma, 0])
        G10 = build_10d_metric(A_6x6, b)

        # Check signature (should have 1 negative eigenvalue)
        eigs = np.linalg.eigvalsh(G10)
        n_neg = np.sum(eigs < 0)
        sig_ok = "✓" if n_neg == 1 else f"✗({n_neg})"

        E_e = approach_C_mass_shell(G10, L_6, MODES['electron'][0])
        E_p = approach_C_mass_shell(G10, L_6, MODES['proton'][0])
        E_e_bare = bare_mode_energy(MODES['electron'][0])
        E_p_bare = bare_mode_energy(MODES['proton'][0])

        de = (E_e - E_e_bare) / E_e_bare * 100 if not np.isnan(E_e) else float('nan')
        dp = (E_p - E_p_bare) / E_p_bare * 100 if not np.isnan(E_p) else float('nan')

        print(f"  {sigma:8.4f}  {E_e:8.4f}  {E_p:8.2f}  {de:+7.2f}  {dp:+7.2f}  {sig_ok:>5s}")

    print()

    # ── Section 3: Ma-t coupling — ring dimensions ─────────
    print("─" * 75)
    print("Section 3: Ma-t coupling on RING dimensions")
    print("  b_Ma-t = [0, ±σ, 0, ±σ, 0, ±σ] (e-ring, ν-ring, p-ring)")
    print("─" * 75)
    print()

    print(f"  {'σ':>8s}  {'E_e':>8s}  {'E_p':>8s}  {'Δe%':>7s}  {'Δp%':>7s}  {'sig?':>5s}")
    print(f"  {'─'*8}  {'─'*8}  {'─'*8}  {'─'*7}  {'─'*7}  {'─'*5}")

    for sigma in [0.001, 0.01, 0.05, 0.1, 0.2, 0.3, 0.5]:
        b = np.array([0, -sigma, 0, +sigma, 0, +sigma])
        G10 = build_10d_metric(A_6x6, b)

        eigs = np.linalg.eigvalsh(G10)
        n_neg = np.sum(eigs < 0)
        sig_ok = "✓" if n_neg == 1 else f"✗({n_neg})"

        E_e = approach_C_mass_shell(G10, L_6, MODES['electron'][0])
        E_p = approach_C_mass_shell(G10, L_6, MODES['proton'][0])
        E_e_bare = bare_mode_energy(MODES['electron'][0])
        E_p_bare = bare_mode_energy(MODES['proton'][0])

        de = (E_e - E_e_bare) / E_e_bare * 100 if not np.isnan(E_e) else float('nan')
        dp = (E_p - E_p_bare) / E_p_bare * 100 if not np.isnan(E_p) else float('nan')

        print(f"  {sigma:8.4f}  {E_e:8.4f}  {E_p:8.2f}  {de:+7.2f}  {dp:+7.2f}  {sig_ok:>5s}")

    print()

    # ── Section 4: Compare Schur vs mass-shell ─────────────
    print("─" * 75)
    print("Section 4: Compare approaches A and C at σ = 0.1 (ring)")
    print("─" * 75)
    print()

    b = np.array([0, -0.1, 0, +0.1, 0, +0.1])
    G10 = build_10d_metric(A_6x6, b)

    print(f"  {'Mode':>10s}  {'E_bare':>10s}  {'E_SchurT':>10s}  {'E_shell':>10s}  "
          f"{'Δ_schur%':>9s}  {'Δ_shell%':>9s}")
    print(f"  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*9}  {'─'*9}")

    for name, (n6, m_obs, Q) in MODES.items():
        E_bare = bare_mode_energy(n6)
        E_schur = approach_A_schur_time(G10, L_6, n6)
        E_shell = approach_C_mass_shell(G10, L_6, n6)

        ds = (E_schur - E_bare) / E_bare * 100
        dc = (E_shell - E_bare) / E_bare * 100

        print(f"  {name:>10s}  {E_bare:10.4f}  {E_schur:10.4f}  {E_shell:10.4f}  "
              f"{ds:+9.3f}  {dc:+9.3f}")

    print()

    # ── Section 5: What does the Lorentzian Schur complement do? ──
    print("─" * 75)
    print("Section 5: Effective Ma metric from Lorentzian Schur complement")
    print("─" * 75)
    print()
    print("  Euclidean (R55): A_eff = A - b bᵀ  (coupling REDUCES metric)")
    print("  Lorentzian (R59): A_eff = A + b bᵀ  (coupling INCREASES metric)")
    print()

    b = np.array([0, -0.1, 0, +0.1, 0, +0.1])

    # The correction: b ⊗ b / g_tt = b ⊗ b / (-1) → added (not subtracted)
    correction = np.outer(b, b) / (-1.0)  # = +b⊗b
    A_corrected = A_6x6 + correction

    print("  Correction matrix (b ⊗ b, with sign from Lorentzian):")
    for i in range(6):
        row = "  "
        for j in range(6):
            v = correction[i, j]
            if abs(v) > 1e-10:
                row += f" {v:+8.4f}"
            else:
                row += "        0"
        print(row)

    print()
    print("  The Lorentzian sign means Ma-t coupling ADDS to the")
    print("  diagonal, making modes slightly LESS energetic (lower mass).")
    print("  This is opposite to R55's spatial coupling, which made")
    print("  modes MORE energetic.")
    print()

    # ── Section 6: Can Ma-t coupling give α? ───────────────
    print("─" * 75)
    print("Section 6: Can we define α_eff from the Ma-t coupling?")
    print("─" * 75)
    print()

    print("  Define α_eff = |E_coupled - E_bare| / E_bare")
    print("  (fractional mass shift from the Ma-t coupling)")
    print()

    print(f"  {'σ':>8s}  {'α_e':>12s}  {'α_p':>12s}  {'α_ν':>12s}  "
          f"{'αe/α':>8s}  {'αp/α':>8s}  {'e=p?':>5s}")
    print(f"  {'─'*8}  {'─'*12}  {'─'*12}  {'─'*12}  "
          f"{'─'*8}  {'─'*8}  {'─'*5}")

    for sigma in [0.001, 0.005, 0.01, 0.02, 0.05, 0.08, 0.1, 0.15, 0.2]:
        # Ring coupling (same as R55 hypothesis F)
        b = np.array([0, -sigma, 0, +sigma, 0, +sigma])
        G10 = build_10d_metric(A_6x6, b)

        eigs = np.linalg.eigvalsh(G10)
        if np.sum(eigs < 0) != 1:
            print(f"  {sigma:8.4f}  invalid signature")
            continue

        E_e_bare = bare_mode_energy(MODES['electron'][0])
        E_p_bare = bare_mode_energy(MODES['proton'][0])
        E_nu_bare = bare_mode_energy(MODES['ν₁'][0])

        E_e = approach_C_mass_shell(G10, L_6, MODES['electron'][0])
        E_p = approach_C_mass_shell(G10, L_6, MODES['proton'][0])
        E_nu = approach_C_mass_shell(G10, L_6, MODES['ν₁'][0])

        ae = abs(E_e - E_e_bare) / E_e_bare if not np.isnan(E_e) else np.nan
        ap = abs(E_p - E_p_bare) / E_p_bare if not np.isnan(E_p) else np.nan
        an = abs(E_nu - E_nu_bare) / E_nu_bare if not np.isnan(E_nu) else np.nan

        equal = "YES" if (not np.isnan(ae) and not np.isnan(ap) and
                          abs(ae - ap) / max(ae, 1e-30) < 0.05) else "no"

        ae_s = f"{ae:.4e}" if not np.isnan(ae) else "NaN"
        ap_s = f"{ap:.4e}" if not np.isnan(ap) else "NaN"
        an_s = f"{an:.4e}" if not np.isnan(an) else "NaN"

        print(f"  {sigma:8.4f}  {ae_s:>12s}  {ap_s:>12s}  {an_s:>12s}  "
              f"{ae/ALPHA:8.4f}  {ap/ALPHA:8.4f}  {equal:>5s}")

    print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 75)
    print("SUMMARY")
    print("=" * 75)
    print()
    print("  Key findings from Track 1:")
    print()
    print("  1. Does the bare 10D metric reproduce model-E masses?")
    print("  2. Does Ma-t coupling shift masses?  In which direction?")
    print("  3. Is the shift universal (same α_eff for e and p)?")
    print("  4. Does the Lorentzian signature make a difference vs R55?")
    print("  5. Can we define α from the mass-shell condition?")
    print()
    print(f"  α = {ALPHA:.6e}")
    print()
    print("Track 1 complete.")


if __name__ == '__main__':
    main()
