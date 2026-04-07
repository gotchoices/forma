#!/usr/bin/env python3
"""
Track 5: Wavefront transfer efficiency — coherent signal
coupling from a 2D wye to a 3D jack at a shared node.

Computes:
1. The 4×3 projection matrix M(θ,φ,ψ) = ê_jack · ê_wye
2. SVD of M — singular values and their orientation dependence
3. Transfer efficiency T(k̂, θ,φ,ψ) = fraction of 2D wave
   energy that exits as a correctly-directed 3D wave
4. Orientation sweep and torus integral
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import time

OUT = Path(__file__).parent.parent / "output"
OUT.mkdir(exist_ok=True)

# ── Jack directions (tetrahedral) ────────────────────────────

JACK = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=float) / np.sqrt(3)


def wye_directions(theta, phi, psi):
    """3 wye edge directions in a plane with normal n̂(θ,φ),
    twisted by ψ."""
    ct, st = np.cos(theta), np.sin(theta)
    cp, sp = np.cos(phi), np.sin(phi)

    e1 = np.array([ct * cp, ct * sp, -st])
    e2 = np.array([-sp, cp, 0.0])

    norm1 = np.linalg.norm(e1)
    norm2 = np.linalg.norm(e2)
    if norm1 < 1e-10 or norm2 < 1e-10:
        return None
    e1 /= norm1
    e2 /= norm2

    dirs = np.zeros((3, 3))
    for k in range(3):
        angle = psi + k * 2 * np.pi / 3
        dirs[k] = np.cos(angle) * e1 + np.sin(angle) * e2
    return dirs


def projection_matrix(theta, phi, psi):
    """4×3 matrix M_jk = ê_jack_j · ê_wye_k"""
    wye = wye_directions(theta, phi, psi)
    if wye is None:
        return None
    M = JACK @ wye.T  # (4,3) @ (3,3)^T = (4,3)
    return M


def svd_analysis(M):
    """SVD of the 4×3 projection matrix."""
    U, sigma, Vt = np.linalg.svd(M, full_matrices=False)
    return sigma  # 3 singular values


def transfer_efficiency(theta, phi, psi, n_gamma=72):
    """Compute the wavefront transfer efficiency averaged over
    propagation directions γ within the wye plane.

    For each γ:
    - a = wye amplitudes for a wave in direction γ
    - b_desired = jack amplitudes for the same wave direction
    - b_projected = M @ a (what the wye projects onto the jack)
    - η = |b_projected · b_desired|² / (|b_proj|² |b_des|²)
    - energy_frac = |M @ a|² / |a|²
    - T = energy_frac × η (net forward transfer)

    Returns T_avg, T_array, details.
    """
    wye = wye_directions(theta, phi, psi)
    if wye is None:
        return 0, np.zeros(n_gamma), {}

    M = JACK @ wye.T  # 4×3

    # Normal to the wye plane
    n = np.cross(wye[0], wye[1])
    n /= np.linalg.norm(n)

    # Two orthonormal vectors in the wye plane
    e1 = wye[0].copy()
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    e2 /= np.linalg.norm(e2)

    gammas = np.linspace(0, 2 * np.pi, n_gamma, endpoint=False)
    T_array = np.zeros(n_gamma)
    eta_array = np.zeros(n_gamma)
    efrac_array = np.zeros(n_gamma)

    for gi, gamma in enumerate(gammas):
        # Propagation direction (in 3D, lying in the wye plane)
        k_hat = np.cos(gamma) * e1 + np.sin(gamma) * e2

        # Wye amplitudes: projection of k_hat onto each wye edge
        a = wye @ k_hat  # (3,)

        # Desired jack amplitudes for same propagation direction
        b_desired = JACK @ k_hat  # (4,)

        # Projected jack amplitudes from wye
        b_projected = M @ a  # (4,)

        # Energy fraction
        a_sq = np.dot(a, a)
        bp_sq = np.dot(b_projected, b_projected)
        if a_sq < 1e-30:
            continue
        energy_frac = bp_sq / a_sq

        # Pattern match (cosine similarity squared)
        bd_sq = np.dot(b_desired, b_desired)
        if bp_sq < 1e-30 or bd_sq < 1e-30:
            eta = 0
        else:
            dot = np.dot(b_projected, b_desired)
            eta = dot ** 2 / (bp_sq * bd_sq)

        T_array[gi] = energy_frac * eta
        eta_array[gi] = eta
        efrac_array[gi] = energy_frac

    T_avg = np.mean(T_array)

    details = {
        'T_avg': T_avg,
        'T_min': np.min(T_array),
        'T_max': np.max(T_array),
        'eta_avg': np.mean(eta_array),
        'efrac_avg': np.mean(efrac_array),
    }

    return T_avg, T_array, details


# ── Part 1: SVD analysis ─────────────────────────────────────

def part1_svd():
    """Analyze the singular values of M across orientations."""
    print("── Part 1: SVD of projection matrix M ──\n")

    n_theta, n_phi = 90, 180
    n_psi = 60

    sigma_all = []
    trace_all = []

    for ti, theta in enumerate(np.linspace(0.05, np.pi - 0.05, n_theta)):
        for phi in np.linspace(0, 2 * np.pi, n_phi, endpoint=False):
            # Find the ψ that maximizes σ₁ (best coupling orientation)
            best_sigma = None
            for psi in np.linspace(0, 2 * np.pi / 3, n_psi, endpoint=False):
                M = projection_matrix(theta, phi, psi)
                if M is None:
                    continue
                s = svd_analysis(M)
                if best_sigma is None or s[0] > best_sigma[0]:
                    best_sigma = s
            if best_sigma is not None:
                sigma_all.append(best_sigma)
                trace_all.append(np.sum(best_sigma ** 2))

    sigma_all = np.array(sigma_all)
    trace_all = np.array(trace_all)

    print(f"  Sampled {len(sigma_all)} orientations")
    print(f"\n  Singular value statistics (optimized over ψ):")
    print(f"  {'':>10s}  {'σ₁':>8s}  {'σ₂':>8s}  {'σ₃':>8s}  {'Tr(MᵀM)':>10s}")
    print("  " + "─" * 42)
    print(f"  {'Mean':>10s}  {np.mean(sigma_all[:,0]):8.4f}  "
          f"{np.mean(sigma_all[:,1]):8.4f}  "
          f"{np.mean(sigma_all[:,2]):8.4f}  "
          f"{np.mean(trace_all):10.4f}")
    print(f"  {'Min':>10s}  {np.min(sigma_all[:,0]):8.4f}  "
          f"{np.min(sigma_all[:,1]):8.4f}  "
          f"{np.min(sigma_all[:,2]):8.4f}  "
          f"{np.min(trace_all):10.4f}")
    print(f"  {'Max':>10s}  {np.max(sigma_all[:,0]):8.4f}  "
          f"{np.max(sigma_all[:,1]):8.4f}  "
          f"{np.max(sigma_all[:,2]):8.4f}  "
          f"{np.max(trace_all):10.4f}")
    print(f"  {'Std':>10s}  {np.std(sigma_all[:,0]):8.4f}  "
          f"{np.std(sigma_all[:,1]):8.4f}  "
          f"{np.std(sigma_all[:,2]):8.4f}  "
          f"{np.std(trace_all):10.4f}")

    # Check if Tr(MᵀM) = 4 everywhere (Track 4 identity)
    print(f"\n  Tr(MᵀM) = σ₁² + σ₂² + σ₃²:")
    print(f"    Mean = {np.mean(trace_all):.6f}")
    print(f"    Std  = {np.std(trace_all):.6f}")
    print(f"    Expected: 4.000000 (tetrahedral identity)")
    is_constant = np.std(trace_all) < 0.001
    print(f"    {'✓ Constant (as expected)' if is_constant else '✗ NOT constant'}")

    # Check if individual σ values are constant
    print(f"\n  Are individual singular values constant?")
    for i in range(3):
        cv = np.std(sigma_all[:, i]) / np.mean(sigma_all[:, i])
        print(f"    σ_{i+1}: mean={np.mean(sigma_all[:,i]):.4f}, "
              f"std={np.std(sigma_all[:,i]):.4f}, CV={cv:.4f} "
              f"({'constant' if cv < 0.01 else 'VARIES'})")

    return sigma_all


# ── Part 2: Transfer efficiency ──────────────────────────────

def part2_transfer():
    """Compute transfer efficiency T across orientations."""
    print("\n── Part 2: Transfer efficiency T(θ,φ,ψ) ──\n")

    # First: at specific important angles
    print("  Transfer efficiency at key orientations:\n")

    # ⟨111⟩ magic angle
    mn = np.array([1, 1, 1]) / np.sqrt(3)
    theta_magic = np.arccos(mn[2])
    phi_magic = np.arctan2(mn[1], mn[0])

    # Find best ψ at magic angle
    best_T = 0
    best_psi = 0
    for psi in np.linspace(0, 2 * np.pi / 3, 360):
        T, _, _ = transfer_efficiency(theta_magic, phi_magic, psi)
        if T > best_T:
            best_T = T
            best_psi = psi

    T_magic, T_arr, det = transfer_efficiency(
        theta_magic, phi_magic, best_psi, n_gamma=360)
    print(f"  ⟨111⟩ magic angle (θ={np.degrees(theta_magic):.1f}°, "
          f"φ={np.degrees(phi_magic):.1f}°, ψ={np.degrees(best_psi):.1f}°):")
    print(f"    T_avg = {det['T_avg']:.6f}")
    print(f"    T_min = {det['T_min']:.6f}, T_max = {det['T_max']:.6f}")
    print(f"    η_avg = {det['eta_avg']:.6f} (pattern match)")
    print(f"    E_frac = {det['efrac_avg']:.6f} (energy transfer)")

    # Random orientation
    np.random.seed(42)
    for trial in range(5):
        th = np.random.uniform(0.1, np.pi - 0.1)
        ph = np.random.uniform(0, 2 * np.pi)
        ps = np.random.uniform(0, 2 * np.pi / 3)
        T, _, det = transfer_efficiency(th, ph, ps, n_gamma=360)
        print(f"\n  Random #{trial+1} (θ={np.degrees(th):.1f}°, "
              f"φ={np.degrees(ph):.1f}°, ψ={np.degrees(ps):.1f}°):")
        print(f"    T_avg = {det['T_avg']:.6f}")
        print(f"    η_avg = {det['eta_avg']:.6f}")
        print(f"    E_frac = {det['efrac_avg']:.6f}")

    # Full sweep
    print(f"\n  Full orientation sweep...")
    n_theta, n_phi, n_psi = 45, 90, 30
    total = n_theta * n_phi * n_psi

    T_values = []
    eta_values = []
    efrac_values = []

    t0 = time.time()
    count = 0
    for theta in np.linspace(0.05, np.pi - 0.05, n_theta):
        for phi in np.linspace(0, 2 * np.pi, n_phi, endpoint=False):
            for psi in np.linspace(0, 2 * np.pi / 3, n_psi, endpoint=False):
                T, _, det = transfer_efficiency(theta, phi, psi, n_gamma=36)
                T_values.append(det['T_avg'])
                eta_values.append(det['eta_avg'])
                efrac_values.append(det['efrac_avg'])
                count += 1
                if count % (total // 10) == 0:
                    print(f"    {100*count//total}%")

    elapsed = time.time() - t0
    T_values = np.array(T_values)
    eta_values = np.array(eta_values)
    efrac_values = np.array(efrac_values)

    print(f"  Done in {elapsed:.0f}s ({total} orientations)\n")

    print(f"  Transfer efficiency statistics:")
    print(f"    T_avg:  mean={np.mean(T_values):.6f}, "
          f"std={np.std(T_values):.6f}, "
          f"min={np.min(T_values):.6f}, max={np.max(T_values):.6f}")
    print(f"    η_avg:  mean={np.mean(eta_values):.6f}, "
          f"std={np.std(eta_values):.6f}")
    print(f"    E_frac: mean={np.mean(efrac_values):.6f}, "
          f"std={np.std(efrac_values):.6f}")

    cv_T = np.std(T_values) / np.mean(T_values) if np.mean(T_values) > 0 else 0
    cv_eta = np.std(eta_values) / np.mean(eta_values) if np.mean(eta_values) > 0 else 0
    print(f"\n  Coefficient of variation:")
    print(f"    T:    CV = {cv_T:.4f} "
          f"({'VARIES' if cv_T > 0.01 else 'constant'})")
    print(f"    η:    CV = {cv_eta:.4f} "
          f"({'VARIES' if cv_eta > 0.01 else 'constant'})")
    print(f"    E_frac: CV = {np.std(efrac_values)/np.mean(efrac_values):.4f}")

    print(f"\n  Comparison to α:")
    print(f"    ⟨T⟩ = {np.mean(T_values):.6f}")
    print(f"    α   = {1/137:.6f}")
    print(f"    ⟨T⟩/α = {np.mean(T_values)/(1/137):.2f}")

    return T_values, eta_values, efrac_values


# ── Part 3: Torus integral ───────────────────────────────────

def part3_torus(T_sweep_data=None):
    """Compute the transfer efficiency averaged over a torus surface."""
    print("\n── Part 3: Torus integral ──\n")

    epsilons = [0.1, 0.2, 0.3, 0.5, 0.65, 0.8, 1.0, 1.5, 2.0]

    # Torus axis along [0,0,1] by default
    # Could also try axis along ⟨111⟩

    print(f"  Torus axis: [0, 0, 1]")
    print(f"  {'ε':>6s}  {'T_avg':>10s}  {'η_avg':>10s}  "
          f"{'E_frac':>10s}  {'1/T':>10s}")
    print("  " + "─" * 50)

    torus_results = []

    for eps in epsilons:
        # Sample the torus surface
        # Tube angle u goes 0 to 2π, ring angle v goes 0 to 2π
        # Surface normal at (u,v): depends on torus geometry
        n_u, n_v = 72, 72
        T_sum = 0
        eta_sum = 0
        ef_sum = 0
        area_sum = 0

        for ui, u in enumerate(np.linspace(0, 2 * np.pi, n_u, endpoint=False)):
            for vi, v in enumerate(np.linspace(0, 2 * np.pi, n_v, endpoint=False)):
                # Torus normal at (u, v)
                # For a torus with axis along z:
                # position = ((1 + ε cos u) cos v, (1 + ε cos u) sin v, ε sin u)
                # normal = (cos u cos v, cos u sin v, sin u)
                nx = np.cos(u) * np.cos(v)
                ny = np.cos(u) * np.sin(v)
                nz = np.sin(u)

                theta = np.arccos(np.clip(nz, -1, 1))
                phi = np.arctan2(ny, nx)

                # The twist ψ on the torus surface is determined by the
                # geodesic direction — for a (1,2) knot, the local
                # propagation direction sets ψ.  For now, use ψ = v
                # (the ring angle determines the local twist).
                psi = v

                # Area element: (1 + ε cos u) × ε
                dA = (1 + eps * np.cos(u)) * eps

                T, _, det = transfer_efficiency(theta, phi, psi, n_gamma=18)
                T_sum += det['T_avg'] * dA
                eta_sum += det['eta_avg'] * dA
                ef_sum += det['efrac_avg'] * dA
                area_sum += dA

        T_avg = T_sum / area_sum
        eta_avg = eta_sum / area_sum
        ef_avg = ef_sum / area_sum
        inv_T = 1 / T_avg if T_avg > 0 else float('inf')
        torus_results.append((eps, T_avg, eta_avg, ef_avg))

        print(f"  {eps:6.2f}  {T_avg:10.6f}  {eta_avg:10.6f}  "
              f"{ef_avg:10.6f}  {inv_T:10.1f}")

    # Check for any ε near 1/137
    print(f"\n  Target: T = 1/137 = {1/137:.6f}")
    for eps, T, eta, ef in torus_results:
        if abs(T - 1/137) / (1/137) < 0.5:
            print(f"  ★ ε = {eps:.2f}: T = {T:.6f} "
                  f"(within 50% of 1/137)")

    # Also try torus axis along ⟨111⟩
    print(f"\n  Torus axis: ⟨111⟩ (rotated frame)")
    print(f"  {'ε':>6s}  {'T_avg':>10s}  {'1/T':>10s}")
    print("  " + "─" * 30)

    # Rotation to put z-axis along ⟨111⟩
    z111 = np.array([1, 1, 1]) / np.sqrt(3)
    # Find rotation matrix that maps [0,0,1] to z111
    z = np.array([0, 0, 1.0])
    v_cross = np.cross(z, z111)
    s = np.linalg.norm(v_cross)
    c = np.dot(z, z111)
    vx = np.array([[0, -v_cross[2], v_cross[1]],
                    [v_cross[2], 0, -v_cross[0]],
                    [-v_cross[1], v_cross[0], 0]])
    R = np.eye(3) + vx + vx @ vx * (1 - c) / (s * s + 1e-30)

    for eps in [0.3, 0.5, 0.65, 1.0]:
        n_u, n_v = 72, 72
        T_sum = 0
        area_sum = 0

        for u in np.linspace(0, 2 * np.pi, n_u, endpoint=False):
            for v in np.linspace(0, 2 * np.pi, n_v, endpoint=False):
                # Normal in the rotated frame
                n_local = np.array([np.cos(u) * np.cos(v),
                                    np.cos(u) * np.sin(v),
                                    np.sin(u)])
                n_rot = R @ n_local

                theta = np.arccos(np.clip(n_rot[2], -1, 1))
                phi = np.arctan2(n_rot[1], n_rot[0])
                psi = v

                dA = (1 + eps * np.cos(u)) * eps
                T, _, det = transfer_efficiency(theta, phi, psi, n_gamma=18)
                T_sum += det['T_avg'] * dA
                area_sum += dA

        T_avg = T_sum / area_sum
        inv_T = 1 / T_avg if T_avg > 0 else float('inf')
        print(f"  {eps:6.2f}  {T_avg:10.6f}  {inv_T:10.1f}")


# ── Part 4: Plots ────────────────────────────────────────────

def part4_plots(T_values, eta_values, efrac_values):
    """Generate summary plots."""

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    axes[0].hist(T_values, bins=50, color='blue', alpha=0.7, edgecolor='black', linewidth=0.5)
    axes[0].axvline(1/137, color='red', linestyle='--', label='α = 1/137')
    axes[0].axvline(np.mean(T_values), color='green', linestyle='-', label=f'mean = {np.mean(T_values):.4f}')
    axes[0].set_xlabel('Transfer efficiency T')
    axes[0].set_ylabel('Count')
    axes[0].set_title('Distribution of T')
    axes[0].legend(fontsize=8)

    axes[1].hist(eta_values, bins=50, color='orange', alpha=0.7, edgecolor='black', linewidth=0.5)
    axes[1].axvline(np.mean(eta_values), color='green', linestyle='-', label=f'mean = {np.mean(eta_values):.4f}')
    axes[1].set_xlabel('Pattern match η')
    axes[1].set_ylabel('Count')
    axes[1].set_title('Distribution of η')
    axes[1].legend(fontsize=8)

    axes[2].hist(efrac_values, bins=50, color='green', alpha=0.7, edgecolor='black', linewidth=0.5)
    axes[2].axvline(np.mean(efrac_values), color='blue', linestyle='-', label=f'mean = {np.mean(efrac_values):.4f}')
    axes[2].set_xlabel('Energy fraction')
    axes[2].set_ylabel('Count')
    axes[2].set_title('Distribution of energy fraction')
    axes[2].legend(fontsize=8)

    fig.suptitle('Track 5: Wavefront transfer efficiency', fontsize=14)
    fig.tight_layout()
    fig.savefig(OUT / "track5_distributions.png", dpi=150)
    plt.close(fig)
    print(f"\n  Saved: {OUT / 'track5_distributions.png'}")


# ── Main ─────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("  Track 5: Wavefront transfer efficiency")
    print("=" * 65)

    # Part 1: SVD
    sigma_all = part1_svd()

    # Part 2: Transfer efficiency sweep
    T_values, eta_values, efrac_values = part2_transfer()

    # Part 3: Torus integral
    part3_torus()

    # Part 4: Plots
    part4_plots(T_values, eta_values, efrac_values)

    # Summary
    print("\n" + "=" * 65)
    print("  SUMMARY")
    print("=" * 65)

    print(f"\n  The wavefront transfer efficiency T decomposes as:")
    print(f"    T = (energy fraction) × (pattern match η)")
    print(f"\n  Global statistics:")
    print(f"    ⟨energy fraction⟩ = {np.mean(efrac_values):.6f}")
    print(f"    ⟨η⟩               = {np.mean(eta_values):.6f}")
    print(f"    ⟨T⟩               = {np.mean(T_values):.6f}")
    print(f"    α = 1/137         = {1/137:.6f}")

    cv_T = np.std(T_values) / np.mean(T_values)
    print(f"\n  Does T vary with orientation?")
    print(f"    CV(T) = {cv_T:.4f} "
          f"({'YES — varies' if cv_T > 0.01 else 'NO — constant'})")

    if cv_T > 0.01:
        print(f"    T varies → torus integral is meaningful")
        print(f"    T range: [{np.min(T_values):.6f}, {np.max(T_values):.6f}]")
    else:
        print(f"    T is constant → torus integral = ⟨T⟩ at all ε")
        print(f"    The wye-jack geometry alone determines the coupling")

    if abs(np.mean(T_values) - 1/137) / (1/137) < 0.1:
        print(f"\n  ★★★ ⟨T⟩ ≈ α to within 10% ★★★")
    elif abs(np.mean(T_values) - 1/137) / (1/137) < 0.5:
        print(f"\n  ★ ⟨T⟩ within 50% of α — intriguing")
    else:
        print(f"\n  ⟨T⟩ is {np.mean(T_values)/(1/137):.1f}× α")


if __name__ == "__main__":
    main()
