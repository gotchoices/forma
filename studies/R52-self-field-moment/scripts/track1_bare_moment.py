"""
R52 Track 1 — Bare magnetic moment from torus-knot geometry
============================================================

Computes the magnetic moment of (1,2) and (1,3) modes on their
respective material sheets, comparing two results:

  (a) The QUANTUM (topological) prediction:
        μ = |Q| × ℏ n₂ / (2m)
      This depends only on the winding number n₂ and the charge-to-
      mass ratio.  It is ε-independent (purely topological).

  (b) The CLASSICAL current-loop integral:
        μ_z = (Q / 2T) ∮ (r × dl)_z
      where the integral is over the embedded (n₁,n₂) torus knot
      in 3D.  This depends on the physical size of the torus (R, a)
      and gives a DIFFERENT answer from (a).

Understanding the difference is critical for Tracks 3–4: the Coulomb
self-field lives in 3D (size-dependent), and its back-reaction on the
QUANTUM state produces the anomalous moment.

Key analytical result (derived below and verified numerically):
  ∮ (x dy − y dx) = n₂ × π(2R² + a²)
  μ_classical / μ_quantum = (2R² + a²) / (2 ƛ_C²)
where ƛ_C = ℏ/(mc) is the reduced Compton wavelength.
"""

import sys, os, math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.constants import hbar, c, e as E_CHARGE, m_e, alpha as ALPHA
from lib.ma import solve_shear_for_alpha, mu_12, hbar_c_MeV_fm, M_E_MEV, M_P_MEV

M_P = 1.67262192369e-27  # proton mass (kg)

MU_B = E_CHARGE * hbar / (2 * m_e)     # Bohr magneton (J/T)
MU_N = E_CHARGE * hbar / (2 * M_P)     # nuclear magneton (J/T)


# ── Torus-knot area integral ─────────────────────────────────────────

def knot_area_integral(R, a, n1, n2, N=50000):
    """
    Numerically compute ∮ (x dy/dt − y dx/dt) dt for a (n1,n2)
    torus knot on a torus with major radius R, minor radius a.

    Analytical result: n₂ × π(2R² + a²)
    """
    t = np.linspace(0, 2 * np.pi, N, endpoint=False)
    dt = 2 * np.pi / N

    cos_n1 = np.cos(n1 * t)
    sin_n1 = np.sin(n1 * t)
    cos_n2 = np.cos(n2 * t)
    sin_n2 = np.sin(n2 * t)

    rho = R + a * cos_n1
    x = rho * cos_n2
    y = rho * sin_n2

    drho = -a * n1 * sin_n1
    dx = drho * cos_n2 - n2 * rho * sin_n2
    dy = drho * sin_n2 + n2 * rho * cos_n2

    integrand = x * dy - y * dx
    return np.sum(integrand) * dt


def classical_moment(Q_units, mass_kg, R_m, a_m, n1, n2):
    """
    Classical magnetic moment for charge |Q| on (n1,n2) torus knot.

    μ_z = |Q| / (2T) × ∮ (x dy − y dx) dt
    with T = 2πℏ/(mc²), the Compton period.
    """
    T = 2 * math.pi * hbar / (mass_kg * c**2)
    area = knot_area_integral(R_m, a_m, n1, n2)
    return abs(Q_units) * E_CHARGE * area / (2 * T)


def quantum_moment(Q_units, mass_kg, n2):
    """μ = |Q|e × ℏn₂ / (2m)  — the topological prediction."""
    return abs(Q_units) * E_CHARGE * hbar * n2 / (2 * mass_kg)


# ── Sheet geometry ───────────────────────────────────────────────────

def sheet_geometry(r, mass_MeV):
    """
    Compute torus dimensions for aspect ratio r and particle mass.

    Returns R (m), a (m), s, mu12.
    """
    s = solve_shear_for_alpha(r)
    if s is None:
        return None
    mu = mu_12(r, s)
    E0_MeV = mass_MeV / mu
    L_ring_fm = 2 * math.pi * hbar_c_MeV_fm / E0_MeV
    L_tube_fm = r * L_ring_fm
    R_fm = L_ring_fm / (2 * math.pi)
    a_fm = L_tube_fm / (2 * math.pi)
    return R_fm * 1e-15, a_fm * 1e-15, s, mu


# ── Main analysis ────────────────────────────────────────────────────

def analyze_mode(name, n1, n2, Q_units, mass_kg, mass_MeV,
                 magneton, mag_name, r_values, r_highlight=None):
    """Full analysis for one mode."""

    lambda_bar = hbar / (mass_kg * c)
    mu_q = quantum_moment(Q_units, mass_kg, n2)

    print(f"\n{'='*72}")
    print(f"  {name}: mode ({n1},{n2}), Q = {Q_units:+d}e, "
          f"m = {mass_MeV:.3f} MeV")
    print(f"{'='*72}")

    print(f"\n  Reduced Compton wavelength ƛ_C = {lambda_bar:.4e} m"
          f" = {lambda_bar*1e15:.4f} fm")

    print(f"\n  QUANTUM (topological) bare moment:")
    print(f"    μ_Q = |Q|ℏn₂/(2m) = {n2} × {mag_name}"
          f" = {mu_q/magneton:.4f} {mag_name}")
    print(f"    = {mu_q:.6e} J/T")
    print(f"    This is EXACT and geometry-independent.")

    print(f"\n  CLASSICAL current-loop integral vs aspect ratio r:")
    print(f"    Analytical: μ_cl = |Q|mc²n₂π(2R²+a²) / (4ℏ)")
    print(f"    Ratio:      μ_cl/μ_Q = (2R² + a²) / (2ƛ²)")
    print()
    hdr = (f"    {'r':>6s}  {'s':>8s}  {'R(fm)':>9s}  {'a(fm)':>9s}"
           f"  {'ε=a/R':>7s}  {'μ_cl/'+mag_name:>10s}"
           f"  {'μ_cl/μ_Q':>10s}  {'num_check':>10s}")
    print(hdr)
    print(f"    {'-'*6}  {'-'*8}  {'-'*9}  {'-'*9}"
          f"  {'-'*7}  {'-'*10}  {'-'*10}  {'-'*10}")

    for r in r_values:
        geom = sheet_geometry(r, mass_MeV)
        if geom is None:
            continue
        R_m, a_m, s, mu = geom
        R_fm = R_m * 1e15
        a_fm = a_m * 1e15
        eps = a_m / R_m

        mu_cl = classical_moment(Q_units, mass_kg, R_m, a_m, n1, n2)
        mu_cl_mag = mu_cl / magneton
        ratio = mu_cl / mu_q

        # Analytical ratio check
        ratio_analytical = (2 * R_m**2 + a_m**2) / (2 * lambda_bar**2)

        marker = "  ◀" if r_highlight and abs(r - r_highlight) < 0.01 else ""
        print(f"    {r:6.2f}  {s:8.5f}  {R_fm:9.3f}  {a_fm:9.3f}"
              f"  {eps:7.4f}  {mu_cl_mag:10.2f}"
              f"  {ratio:10.3f}  {ratio_analytical:10.3f}{marker}")

    # Analytical formula for ratio
    print(f"\n  Verification: analytical ratio formula (2R²+a²)/(2ƛ²)"
          f" matches numerical integral")
    print(f"  to machine precision (both compute the same quantity).")

    print(f"\n  INTERPRETATION:")
    print(f"    • The quantum result μ_Q = {n2}{mag_name} comes from"
          f" angular momentum quantization: L = ℏn₂.")
    print(f"    • The classical integral scales as R² (torus area),"
          f" not as ℏ (quantum).")
    print(f"    • For R >> ƛ_C (which is always the case), the"
          f" classical moment >> quantum moment.")
    print(f"    • The PHYSICAL bare moment is the quantum one"
          f" ({n2}{mag_name}).")
    print(f"    • The Coulomb FIELD, however, is classical and lives"
          f" in 3D at scale R.")
    print(f"    • Self-field corrections (Tracks 3-4) come from the"
          f" 3D field acting on the quantum state.")


# ══════════════════════════════════════════════════════════════════════

def main():
    print("R52 Track 1: Bare Magnetic Moment from Torus-Knot Geometry")
    print("=" * 72)

    # ── Electron (1,2) ────────────────────────────────────────────

    r_electron = [0.5, 1.0, 2.0, 3.0, 5.0, 6.6, 8.0, 10.0, 15.0, 20.0]
    analyze_mode(
        "ELECTRON", n1=1, n2=2, Q_units=-1,
        mass_kg=m_e, mass_MeV=M_E_MEV,
        magneton=MU_B, mag_name="μ_B",
        r_values=r_electron, r_highlight=6.6,
    )

    # ── Proton (1,3) ──────────────────────────────────────────────

    r_proton = [0.5, 1.0, 2.0, 3.0, 5.0, 6.6, 8.0, 8.906, 10.0, 15.0]
    analyze_mode(
        "PROTON", n1=1, n2=3, Q_units=+1,
        mass_kg=M_P, mass_MeV=M_P_MEV,
        magneton=MU_N, mag_name="μ_N",
        r_values=r_proton, r_highlight=8.906,
    )

    # ── Comparison table ──────────────────────────────────────────

    print(f"\n\n{'='*72}")
    print(f"  SUMMARY: Quantum bare moments and measured values")
    print(f"{'='*72}")
    print()
    print(f"    {'Particle':>10s}  {'Mode':>6s}  {'Bare μ':>10s}"
          f"  {'Measured μ':>12s}  {'Anomaly':>10s}  {'Sign':>8s}")
    print(f"    {'-'*10}  {'-'*6}  {'-'*10}  {'-'*12}  {'-'*10}  {'-'*8}")

    # Electron
    mu_e_bare = 2  # in μ_B
    mu_e_meas = 2.00231930436256
    anom_e = (mu_e_meas - mu_e_bare) / mu_e_bare
    print(f"    {'Electron':>10s}  {'(1,2)':>6s}  {mu_e_bare:8.1f} μ_B"
          f"  {mu_e_meas:10.5f} μ_B  {anom_e:+9.4%}  {'ADD':>8s}")

    # Proton
    mu_p_bare = 3  # in μ_N
    mu_p_meas = 2.7928473446
    anom_p = (mu_p_meas - mu_p_bare) / mu_p_bare
    print(f"    {'Proton':>10s}  {'(1,3)':>6s}  {mu_p_bare:8.1f} μ_N"
          f"  {mu_p_meas:10.5f} μ_N  {anom_p:+9.4%}  {'SUB':>8s}")

    print()
    print(f"  The electron anomaly is ADDITIVE  (+0.12%): self-field"
          f" enlarges the moment.")
    print(f"  The proton anomaly is SUBTRACTIVE (−6.9%): self-field"
          f" reduces the moment.")
    print(f"  Hypothesis: this sign difference arises from single-phase"
          f" (1,2) vs three-phase (1,3).")
    print()

    # ── What Track 1 establishes ──────────────────────────────────

    print(f"\n{'='*72}")
    print(f"  FINDINGS")
    print(f"{'='*72}")
    print("""
  F1. The quantum bare moment μ = n₂ × magneton is TOPOLOGICAL:
      it depends only on the winding number n₂ and charge-to-mass
      ratio, not on the torus geometry (R, a, ε, r).

  F2. The classical current-loop integral gives μ_classical that
      scales as (2R² + a²) — the physical area swept by the torus
      knot.  This is always LARGER than the quantum moment by a
      factor (2R² + a²)/(2ƛ²), which ranges from ~5 to ~500
      depending on r.

  F3. The bare moments are:
        Electron (1,2):  2 μ_B  (measured: 2.00232 μ_B, +0.12%)
        Proton   (1,3):  3 μ_N  (measured: 2.7928 μ_N,  −6.9%)

  F4. The SIGN of the anomaly differs:
        (1,2) single-phase → ADDITIVE   (moment > bare)
        (1,3) three-phase  → SUBTRACTIVE (moment < bare)
      This is the central hypothesis of R52.

  F5. For the self-field perturbation (Tracks 3-4), the relevant
      physics is: the 3D Coulomb field (which lives at scale R and
      carries energy α×mc²) acts as a perturbation on the QUANTUM
      wave equation on the flat torus.  The perturbation potential
      V(θ₁,θ₂) is geometry-dependent even though the bare moment
      is not.
""")


if __name__ == '__main__':
    main()
