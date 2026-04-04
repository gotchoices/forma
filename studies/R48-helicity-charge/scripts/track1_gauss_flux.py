#!/usr/bin/env python3
"""
R48 Track 1: Gauss flux integral for circularly polarized
standing waves on a torus.

For each mode (n₁, n₂) and aspect ratio ε = a/R, compute the
total outward E-field flux through the torus surface.  Nonzero
flux = charge.  Zero flux = dark mode.

The question: does (1,1) give zero flux while (1,2) gives
nonzero flux?  If so, the helicity of circular polarization
selects which modes carry charge.

Physics:
- The torus has tube radius a, ring radius R, aspect ratio ε = a/R
- A standing wave on the torus has mode numbers (n₁, n₂):
  n₁ cycles around the tube, n₂ around the ring
- Circular polarization: E rotates helically in the plane
  perpendicular to the local propagation direction
- The charge-producing component is E · n̂ (normal to surface)
- Gauss's law: Q = ε₀ ∮ E · n̂ dA

All calculations in natural units (ε₀ = 1).
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).parent.parent / "outputs"
OUT.mkdir(exist_ok=True)


def torus_geometry(theta1, theta2, eps):
    """Compute torus surface geometry at each point.

    Parameters:
        theta1: (M, N) array of tube angles
        theta2: (M, N) array of ring angles
        eps: aspect ratio a/R  (a = eps, R = 1)

    Returns:
        pos: (M, N, 3) position vectors
        normal: (M, N, 3) outward unit normals
        dA: (M, N) area element (R + a cos θ₁) dθ₁ dθ₂
    """
    a = eps
    R = 1.0
    ct1, st1 = np.cos(theta1), np.sin(theta1)
    ct2, st2 = np.cos(theta2), np.sin(theta2)

    rho = R + a * ct1  # distance from torus axis

    # Position
    pos = np.stack([rho * ct2, rho * st2, a * st1], axis=-1)

    # Outward unit normal
    normal = np.stack([ct1 * ct2, ct1 * st2, st1], axis=-1)

    # Area element (for integration: ∫∫ f dA with dθ₁ dθ₂ grid)
    dtheta1 = 2 * np.pi / theta1.shape[0]
    dtheta2 = 2 * np.pi / theta1.shape[1]
    dA = rho * dtheta1 * dtheta2

    return pos, normal, dA


def propagation_directions(theta1, theta2, eps, n1, n2):
    """Compute the local propagation direction of the (n₁, n₂)
    mode at each point on the torus surface.

    The propagation direction is tangent to the surface, along
    the (n₁, n₂) geodesic.  On the flat sheet this is constant;
    on the embedded torus it varies because the metric depends
    on θ₁.

    Returns:
        k_hat: (M, N, 3) unit propagation direction
        e_perp: (M, N, 3) in-surface direction perpendicular to k
    """
    a = eps
    R = 1.0
    ct1, st1 = np.cos(theta1), np.sin(theta1)
    ct2, st2 = np.cos(theta2), np.sin(theta2)
    rho = R + a * ct1

    # Tangent vectors (unnormalized)
    # ∂r/∂θ₁ = a × (−sin θ₁ cos θ₂, −sin θ₁ sin θ₂, cos θ₁)
    e1 = np.stack([-a * st1 * ct2, -a * st1 * st2, a * ct1], axis=-1)
    # ∂r/∂θ₂ = (−ρ sin θ₂, ρ cos θ₂, 0)
    e2 = np.stack([-rho * st2, rho * ct2, np.zeros_like(theta1)], axis=-1)

    # The geodesic direction in coordinate space: n₁ e₁ + n₂ e₂
    # (This is the direction of the (n₁, n₂) wave on the surface)
    k = n1 * e1 + n2 * e2
    k_norm = np.linalg.norm(k, axis=-1, keepdims=True)
    k_hat = k / np.where(k_norm > 0, k_norm, 1)

    # In-surface perpendicular: normal × k_hat
    normal = np.stack([ct1 * ct2, ct1 * st2, st1], axis=-1)
    e_perp = np.cross(normal, k_hat)
    ep_norm = np.linalg.norm(e_perp, axis=-1, keepdims=True)
    e_perp = e_perp / np.where(ep_norm > 0, ep_norm, 1)

    return k_hat, e_perp


def cp_field_normal(theta1, theta2, eps, n1, n2):
    """Compute E · n̂ for a circularly polarized standing wave.

    The CP field at each point:
        E = E₀ [cos(φ) n̂ + sin(φ) ê_perp]

    where φ = n₁θ₁ + n₂θ₂ is the wave phase, n̂ is the surface
    normal, and ê_perp is the in-surface direction perpendicular
    to the propagation.

    The normal component is:
        E · n̂ = E₀ cos(φ)

    But this is the NAIVE decomposition.  The actual CP field
    rotates in the plane perpendicular to the LOCAL propagation
    direction k̂.  That plane contains n̂ and ê_perp (the two
    directions perpendicular to k̂ at the surface).

    For a wave traveling along the (n₁, n₂) geodesic, the
    phase accumulates as φ = n₁θ₁ + n₂θ₂.  The CP rotation
    is synchronized with the phase: E rotates by 2π for each
    2π of phase advance.

    Returns:
        E_n: (M, N) array of E · n̂ at each surface point
    """
    phi = n1 * theta1 + n2 * theta2
    E_n = np.cos(phi)
    return E_n


def gauss_flux(eps, n1, n2, N_grid=512):
    """Compute the total Gauss flux ∮ E · n̂ dA for mode (n₁, n₂).

    Returns:
        Q: total flux (proportional to charge)
        Q_abs: integral of |E · n̂| dA (total unsigned flux)
        E_n_field: the E · n̂ field on the surface (for plotting)
    """
    theta1 = np.linspace(0, 2 * np.pi, N_grid, endpoint=False)
    theta2 = np.linspace(0, 2 * np.pi, N_grid, endpoint=False)
    T1, T2 = np.meshgrid(theta1, theta2, indexing='ij')

    _, normal, dA = torus_geometry(T1, T2, eps)
    E_n = cp_field_normal(T1, T2, eps, n1, n2)

    Q = np.sum(E_n * dA)
    Q_abs = np.sum(np.abs(E_n) * dA)

    return Q, Q_abs, E_n


def sweep_modes(epsilons, modes, N_grid=512):
    """Sweep over aspect ratios and modes, compute Gauss flux."""
    results = []

    for eps in epsilons:
        for n1, n2 in modes:
            Q, Q_abs, _ = gauss_flux(eps, n1, n2, N_grid)
            # Normalize: Q / Q_abs gives the charge efficiency
            # (fraction of total flux that is net, not cancelling)
            efficiency = Q / Q_abs if Q_abs > 0 else 0
            results.append({
                'eps': eps,
                'n1': n1, 'n2': n2,
                'Q': Q, 'Q_abs': Q_abs,
                'efficiency': efficiency,
            })

    return results


def plot_field(eps, n1, n2, N_grid=256):
    """Plot E · n̂ on the unrolled torus surface."""
    theta1 = np.linspace(0, 2 * np.pi, N_grid, endpoint=False)
    theta2 = np.linspace(0, 2 * np.pi, N_grid, endpoint=False)
    T1, T2 = np.meshgrid(theta1, theta2, indexing='ij')

    E_n = cp_field_normal(T1, T2, eps, n1, n2)
    _, _, dA = torus_geometry(T1, T2, eps)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # E · n̂ (raw field)
    im1 = ax1.pcolormesh(T2, T1, E_n, cmap='RdBu_r', shading='auto',
                         vmin=-1, vmax=1)
    ax1.set_xlabel('θ₂ (ring)')
    ax1.set_ylabel('θ₁ (tube)')
    ax1.set_title(f'E · n̂  for ({n1},{n2}), ε = {eps}')
    plt.colorbar(im1, ax=ax1, label='E · n̂ / E₀')

    # E · n̂ × dA (flux density — what Gauss integrates)
    flux_density = E_n * dA
    vmax = np.max(np.abs(flux_density))
    im2 = ax2.pcolormesh(T2, T1, flux_density, cmap='RdBu_r',
                         shading='auto', vmin=-vmax, vmax=vmax)
    ax2.set_xlabel('θ₂ (ring)')
    ax2.set_ylabel('θ₁ (tube)')
    ax2.set_title(f'E · n̂ × dA  (flux density)')
    plt.colorbar(im2, ax=ax2, label='flux density')

    fig.suptitle(f'Mode ({n1},{n2}), ε = {eps:.2f}', fontsize=14)
    fig.tight_layout()
    fname = OUT / f"field_{n1}_{n2}_eps{eps:.2f}.png"
    fig.savefig(fname, dpi=150)
    plt.close(fig)
    return fname


def main():
    print("=" * 60)
    print("  R48 Track 1: Gauss flux for CP modes on a torus")
    print("=" * 60)
    print()

    modes = [
        (1, 1), (1, 2), (1, 3), (1, 4),
        (2, 1), (2, 2), (2, 4),
        (3, 3), (3, 6),
        (0, 1), (0, 2),
    ]

    epsilons = [0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0]

    # ── Part 1: Full sweep ──
    print("── Part 1: Gauss flux sweep ──")
    print()

    results = sweep_modes(epsilons, modes, N_grid=512)

    # Print table
    print(f"  {'mode':>8s}  ", end='')
    for eps in epsilons:
        print(f"{'ε='+str(eps):>10s}", end='  ')
    print()
    print("  " + "─" * (10 + 12 * len(epsilons)))

    for n1, n2 in modes:
        mode_results = [r for r in results if r['n1'] == n1 and r['n2'] == n2]
        print(f"  ({n1},{n2})", end='    ')
        for r in mode_results:
            Q = r['Q']
            if abs(Q) < 1e-10:
                print(f"{'0':>10s}", end='  ')
            else:
                print(f"{Q:>10.4f}", end='  ')
        print()

    # ── Part 2: Efficiency (net flux / total flux) ──
    print()
    print("── Part 2: Charge efficiency |Q| / Q_abs ──")
    print("  (1.0 = all flux in one direction; 0.0 = perfect cancellation)")
    print()

    print(f"  {'mode':>8s}  ", end='')
    for eps in epsilons:
        print(f"{'ε='+str(eps):>10s}", end='  ')
    print()
    print("  " + "─" * (10 + 12 * len(epsilons)))

    for n1, n2 in modes:
        mode_results = [r for r in results if r['n1'] == n1 and r['n2'] == n2]
        print(f"  ({n1},{n2})", end='    ')
        for r in mode_results:
            eff = abs(r['efficiency'])
            if eff < 1e-10:
                print(f"{'0':>10s}", end='  ')
            else:
                print(f"{eff:>10.6f}", end='  ')
        print()

    # ── Part 3: Field plots for key modes ──
    print()
    print("── Part 3: Field plots ──")
    print()

    plot_modes = [(1, 1), (1, 2), (1, 3), (2, 4), (3, 6)]
    plot_eps = [0.3, 0.5, 1.0]

    for eps in plot_eps:
        for n1, n2 in plot_modes:
            fname = plot_field(eps, n1, n2)
            print(f"  Saved: {fname}")

    # ── Part 4: Does the metric weighting matter? ──
    print()
    print("── Part 4: Metric weighting analysis ──")
    print()
    print("  The torus area element dA = (R + a cos θ₁) dθ₁ dθ₂")
    print("  weights the outer equator (θ₁ = 0) more than the inner (θ₁ = π).")
    print("  This asymmetry can break the cos(φ) cancellation.")
    print()
    print("  For mode (n₁, n₂) with E · n̂ = cos(n₁θ₁ + n₂θ₂):")
    print("  Q = ∫∫ cos(n₁θ₁ + n₂θ₂) × (1 + ε cos θ₁) dθ₁ dθ₂")
    print()
    print("  The θ₂ integral:")
    print("    ∫₀²π cos(n₁θ₁ + n₂θ₂) dθ₂ = 0  for n₂ ≠ 0")
    print("    ∫₀²π cos(n₁θ₁ + n₂θ₂) dθ₂ = 2π cos(n₁θ₁)  for n₂ = 0")
    print()
    print("  Therefore: Q = 0 for ALL modes with n₂ ≠ 0,")
    print("  regardless of ε, n₁, or any other parameter.")
    print()
    print("  This is an EXACT ANALYTIC RESULT.")
    print()

    # Verify numerically
    print("  Numerical verification:")
    for eps in [0.3, 0.5, 1.0]:
        for n1, n2 in [(1, 1), (1, 2), (0, 1), (1, 0)]:
            Q, Q_abs, _ = gauss_flux(eps, n1, n2, N_grid=1024)
            status = "✓ zero" if abs(Q) < 1e-8 else f"≠ 0: Q = {Q:.6f}"
            print(f"    ({n1},{n2}) ε={eps}: Q = {Q:+.2e}, "
                  f"Q_abs = {Q_abs:.4f}  {status}")

    # ── Summary ──
    print()
    print("=" * 60)
    print("  SUMMARY")
    print("=" * 60)
    print()
    print("  The naive CP model E · n̂ = cos(n₁θ₁ + n₂θ₂) gives")
    print("  Q = 0 for ALL modes with n₂ ≠ 0.  This is exact:")
    print("  the θ₂ integral of cos(... + n₂θ₂) vanishes by")
    print("  orthogonality for any n₂ ≠ 0.")
    print()
    print("  This means the naive CP decomposition does NOT")
    print("  produce charge for ANY mode — including (1,2).")
    print("  The WvM charge mechanism requires something more")
    print("  than just cos(φ) in the normal direction.")
    print()
    print("  Possible resolutions:")
    print("  1. The CP synchronization (E always outward) is a")
    print("     separate mechanism from the standing-wave phase")
    print("     cos(n₁θ₁ + n₂θ₂).  WvM describes a TRAVELING")
    print("     wave, not a standing wave.  The standing wave")
    print("     E · n̂ oscillates; the traveling wave E · n̂ is")
    print("     constant.  Charge may require a circulating")
    print("     (traveling) component, not a pure standing wave.")
    print()
    print("  2. The normal component of CP is not simply cos(φ).")
    print("     The full 3D decomposition of the helical E field")
    print("     into normal and tangential components on the")
    print("     curved torus surface may give a more complex")
    print("     pattern than cos(n₁θ₁ + n₂θ₂).")
    print()
    print("  3. Charge comes from TOPOLOGY (GRID: 2π phase")
    print("     winding), not from the field integral directly.")
    print("     The Gauss flux is nonzero because of the")
    print("     topological winding, and the field pattern")
    print("     adjusts to be consistent with it — not the")
    print("     other way around.")
    print()
    print("  Resolution 3 aligns with GRID foundations: charge")
    print("  is topological (axiom A3), not a field integral")
    print("  result.  But then Q104 (does helicity select modes?)")
    print("  cannot be answered by the Gauss integral alone —")
    print("  it requires understanding how topology constrains")
    print("  which modes can carry a winding.")


if __name__ == "__main__":
    main()
