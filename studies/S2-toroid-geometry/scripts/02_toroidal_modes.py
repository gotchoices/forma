#!/usr/bin/env python3
"""
02_toroidal_modes.py — EM cavity modes of the WvM toroidal electron.

Solves Maxwell's equations (Helmholtz equation) for the lowest resonant
mode in a toroidal cavity, replacing WvM's uniform-field-in-a-sphere
estimate with the actual field distribution.

The WvM model specifies the major (transport) radius R = λ_C/(4π) but
leaves the tube radius a unspecified.  This script sweeps a/R and
computes the effective charge q for each geometry using the actual
mode shape rather than a uniform-field assumption.

Method
------
1. Axial symmetry reduces 3D Maxwell → 2D on the tube cross-section.
   Modes have azimuthal dependence e^{inφ}, giving the scalar equation:

       ∂²ψ/∂ρ² + (1/ρ)∂ψ/∂ρ + ∂²ψ/∂z² + (k² − n²/ρ²)ψ = 0

   with ψ = 0 on the tube wall (TM-like modes, radial E-field).

2. The substitution φ = √ρ·ψ yields a symmetric eigenvalue problem:

       [−∂²/∂ξ² − ∂²/∂ζ² + (n²−¼)/(β+ξ)²] φ = κ² φ

   where ξ,ζ are scaled tube coordinates, β = R/a, and κ = ka.
   This is solved with finite differences + scipy sparse eigensolver.

3. The physical field ψ = φ/√ρ is recovered, normalized to one photon
   of energy hc/λ_C, and the charge is derived by matching the E-field
   at the transport radius R to the Coulomb field.

Limitation: WvM envision a self-confined photon, not a hard-walled
cavity.  This gives the field distribution for the closest tractable
idealization.

Reference: theory.md §5.1, findings.md F7
"""

import math
import sys
import os
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib import constants as C
from lib.wvm import q_over_e as QE_WVM

R_PHYS = C.lambda_C / (4 * math.pi)


def solve_mode(beta, n_phi=1, N=81):
    """
    Lowest eigenmode of a toroidal cavity cross-section.

    After φ = √ρ·ψ, solves the symmetric problem:
        [−∇²_{ξζ} + V(ξ)] φ = κ² φ
    on the unit disk with V(ξ) = (n²−¼)/(β+ξ)² and Dirichlet BC.

    Parameters
    ----------
    beta : float
        R/a ratio (> 1 for a true torus with a hole).
    n_phi : int
        Azimuthal mode number.
    N : int
        Grid points per axis (odd recommended so center is on grid).

    Returns
    -------
    kappa_sq : float
        Dimensionless eigenvalue κ² = k²a².
    phi_2d : ndarray (N, N)
        Eigenfunction φ(ξ, ζ).
    xi, zeta : ndarray (N,)
        Grid coordinates in [−1, 1].
    mask : ndarray (N, N) of bool
        Interior points.
    """
    h = 2.0 / (N - 1)
    xi = np.linspace(-1, 1, N)
    zeta = np.linspace(-1, 1, N)
    XI, ZE = np.meshgrid(xi, zeta, indexing='ij')

    mask = (XI**2 + ZE**2) < (1 - 0.5 * h)**2

    idx = np.full((N, N), -1, dtype=int)
    pts = np.argwhere(mask)
    for k, (i, j) in enumerate(pts):
        idx[i, j] = k
    n_pts = len(pts)

    V_coeff = n_phi**2 - 0.25
    rows, cols, vals = [], [], []

    for k, (i, j) in enumerate(pts):
        rho_s = beta + xi[i]

        d = 4.0 / h**2 + V_coeff / rho_s**2
        rows.append(k); cols.append(k); vals.append(d)

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and idx[ni, nj] >= 0:
                rows.append(k)
                cols.append(idx[ni, nj])
                vals.append(-1.0 / h**2)

    H = sparse.csr_matrix((vals, (rows, cols)), shape=(n_pts, n_pts))

    n_eig = min(4, n_pts - 2)
    evals, evecs = eigsh(H, k=n_eig, which='SM')

    order = np.argsort(evals)
    kappa_sq = evals[order[0]]
    phi_vec = evecs[:, order[0]]

    phi_2d = np.zeros((N, N))
    for k, (i, j) in enumerate(pts):
        phi_2d[i, j] = phi_vec[k]

    return kappa_sq, phi_2d, xi, zeta, mask


def charge_from_mode(beta, phi, xi, zeta, mask):
    """
    Derive effective charge from a toroidal mode shape.

    Physical mode: ψ = φ/√ρ.
    Energy normalization: ε₀ ∫ E² dV = hc/λ, with E² ∝ |ψ|².
    Charge: q = 4πε₀ R² · E(R, 0).

    Returns (q, q/e, F) where F is the field concentration factor.
    """
    a = R_PHYS / beta
    N = len(xi)
    h = 2.0 / (N - 1)

    i_c = N // 2
    j_c = N // 2
    phi_c = phi[i_c, j_c]

    # |ψ(R,0)|² = |φ(0,0)|² / R  (since ρ = R at tube center)
    psi_c_sq = phi_c**2 / R_PHYS

    # ∫|ψ|²ρ dρ dz = ∫|φ|² dρ dz  →  I_phys = 2πa² I_s
    I_s = h**2 * np.sum(phi**2 * mask)
    I_phys = 2 * math.pi * a**2 * I_s

    E_R = math.sqrt(abs(psi_c_sq) * C.h * C.c
                    / (C.eps0 * C.lambda_C * I_phys))

    q = 4 * math.pi * C.eps0 * R_PHYS**2 * E_R

    # Field concentration: F = |ψ(R)|² / ⟨|ψ|²⟩_volume
    # ⟨|ψ|²⟩ = I_phys / V_torus,  V_torus = 2π²Ra²
    # F = π|φ_c|² / I_s
    F = math.pi * phi_c**2 / I_s if I_s > 0 else 0.0

    return q, q / C.e, F


def main():
    print("=" * 72)
    print("Toroidal Cavity Modes — Maxwell's Equations on the WvM Geometry")
    print("=" * 72)
    print()
    print(f"  Transport radius  R = λ_C/(4π) = {R_PHYS:.3e} m")
    print(f"  WvM charge (uniform sphere):  q/e = {QE_WVM:.6f}")
    print()

    # ── Validation ────────────────────────────────────────────────────────
    J01 = 2.4048
    J01_SQ = J01**2

    print("─" * 72)
    print("VALIDATION: Straight waveguide limit (β → ∞, n=0)")
    print(f"  Expected: κ² → j₀₁² = {J01_SQ:.4f}  (first zero of J₀)")
    print("─" * 72)
    print(f"  {'β':>6s}  {'κ²':>10s}  {'j₀₁²':>10s}  {'Error':>8s}")

    for beta in [3, 5, 10, 20, 50]:
        ksq, *_ = solve_mode(beta, n_phi=0, N=81)
        err = abs(ksq - J01_SQ) / J01_SQ * 100
        print(f"  {beta:>6.0f}  {ksq:>10.4f}  {J01_SQ:>10.4f}  {err:>7.3f}%")

    print()

    # ── Charge vs tube radius ─────────────────────────────────────────────
    print("─" * 72)
    print("CHARGE vs TUBE RADIUS  (azimuthal mode n = 1)")
    print()
    print("  β = R/a.   F = field concentration at tube center vs average.")
    print("  F > 1 → field stronger at R than average → larger q.")
    print("─" * 72)
    print()
    print(f"  {'a/R':>6s}  {'β':>6s}  {'κ²':>8s}  {'F':>8s}  "
          f"{'q/e':>8s}  {'vs WvM':>8s}")

    results = []
    a_values = np.concatenate([
        np.arange(0.10, 0.50, 0.05),
        np.arange(0.50, 0.96, 0.05),
    ])

    for a_over_R in a_values:
        beta = 1.0 / a_over_R
        ksq, phi, xi, ze, mask = solve_mode(beta, n_phi=1, N=81)
        q, qe, F = charge_from_mode(beta, phi, xi, ze, mask)
        shift = (qe / QE_WVM - 1) * 100
        results.append((a_over_R, beta, ksq, F, qe, shift))

        marker = ""
        if abs(qe - 1.0) < 0.02:
            marker = " ← q ≈ e"
        print(f"  {a_over_R:>6.2f}  {beta:>6.2f}  {ksq:>8.3f}  {F:>8.4f}  "
              f"{qe:>8.5f}  {shift:>+7.1f}%{marker}")

    print()

    # ── n=0 comparison ────────────────────────────────────────────────────
    print("─" * 72)
    print("MODE NUMBER SENSITIVITY: n=0 vs n=1 vs n=2")
    print("─" * 72)
    print()
    print(f"  {'a/R':>6s}  {'q/e (n=0)':>10s}  {'q/e (n=1)':>10s}  "
          f"{'q/e (n=2)':>10s}")

    for a_over_R in [0.20, 0.40, 0.60, 0.80, 0.90]:
        beta = 1.0 / a_over_R
        qe_list = []
        for n in [0, 1, 2]:
            _, phi, xi, ze, mask = solve_mode(beta, n_phi=n, N=81)
            _, qe, _ = charge_from_mode(beta, phi, xi, ze, mask)
            qe_list.append(qe)
        print(f"  {a_over_R:>6.2f}  {qe_list[0]:>10.5f}  {qe_list[1]:>10.5f}  "
              f"{qe_list[2]:>10.5f}")

    print()

    # ── Search for a/R where q = e ────────────────────────────────────────
    print("─" * 72)
    print("SEARCH: What tube radius gives q = e exactly?  (n = 1)")
    print("─" * 72)

    lo, hi = 0.05, 0.99
    qe_lo, qe_hi = None, None

    for _ in range(50):
        mid = (lo + hi) / 2
        beta = 1.0 / mid
        _, phi, xi, ze, mask = solve_mode(beta, n_phi=1, N=81)
        _, qe, _ = charge_from_mode(beta, phi, xi, ze, mask)
        if qe > 1.0:
            lo = mid
            qe_lo = qe
        else:
            hi = mid
            qe_hi = qe

    a_R_sol = (lo + hi) / 2
    beta_sol = 1.0 / a_R_sol

    # High-resolution verification
    _, phi_sol, xi_sol, ze_sol, mask_sol = solve_mode(
        beta_sol, n_phi=1, N=101)
    q_sol, qe_sol, F_sol = charge_from_mode(
        beta_sol, phi_sol, xi_sol, ze_sol, mask_sol)
    a_sol = a_R_sol * R_PHYS

    print()
    if abs(qe_sol - 1.0) < 0.01:
        print(f"  FOUND: a/R = {a_R_sol:.6f}  gives q/e = {qe_sol:.6f}")
        print(f"         a   = {a_sol:.6e} m")
        print(f"         β   = {beta_sol:.4f}")
        print(f"         F   = {F_sol:.4f}")
        print()
        print(f"  The tube radius is {a_R_sol:.2%} of the major radius.")
        print(f"  In terms of λ_C: a = {a_sol / C.lambda_C:.4f} λ_C")
    else:
        print(f"  No exact solution in [0.05, 0.99].")
        print(f"  Closest: a/R = {a_R_sol:.6f}, q/e = {qe_sol:.6f}")

    print()

    # ── Mode shape profile ────────────────────────────────────────────────
    print("─" * 72)
    print("MODE SHAPE PROFILE (at solution a/R, along ξ axis at ζ = 0)")
    print("─" * 72)
    print()
    j_c = len(xi_sol) // 2
    print(f"  {'ξ':>6s}  {'ρ/R':>6s}  {'|φ|':>10s}  {'|ψ|=|φ|/√ρ':>12s}  "
          f"{'bar':>20s}")

    max_psi = 0
    profile_data = []
    for i in range(len(xi_sol)):
        if mask_sol[i, j_c]:
            x = xi_sol[i]
            rho_over_R = 1 + x / beta_sol
            phi_val = abs(phi_sol[i, j_c])
            rho_phys = rho_over_R * R_PHYS
            psi_val = phi_val / math.sqrt(rho_phys) if rho_phys > 0 else 0
            profile_data.append((x, rho_over_R, phi_val, psi_val))
            if psi_val > max_psi:
                max_psi = psi_val

    for x, rr, pv, psv in profile_data[::max(1, len(profile_data)//20)]:
        bar_len = int(40 * psv / max_psi) if max_psi > 0 else 0
        bar = "█" * bar_len
        print(f"  {x:>6.3f}  {rr:>6.3f}  {pv:>10.6f}  {psv:>12.6f}  {bar}")

    print()

    # ── Summary ───────────────────────────────────────────────────────────
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print()

    if results:
        qe_vals = [r[4] for r in results]
        print(f"  q/e ranges from {min(qe_vals):.4f} to {max(qe_vals):.4f}")
        print(f"  as a/R varies from {results[0][0]:.2f} to {results[-1][0]:.2f}.")
        print()

    print(f"  WvM uniform-sphere estimate:   q/e = {QE_WVM:.6f}")

    if abs(qe_sol - 1.0) < 0.01:
        print(f"  Toroidal mode gives q = e at:  a/R = {a_R_sol:.4f}"
              f"  (a = {a_sol / C.lambda_C:.4f} λ_C)")
        print()
        print("  This means there EXISTS a toroidal geometry where the actual")
        print("  EM mode produces exactly the measured electron charge,")
        print("  without needing any series correction.")
    else:
        print("  No toroidal geometry gives q = e in the range tested.")

    print()
    print("  Caveats:")
    print("    - Hard-walled cavity, not self-confinement.")
    print("    - TM-like scalar mode; full vector treatment may differ.")
    print("    - The tube radius a is not predicted by the model.")
    print()


if __name__ == "__main__":
    main()
