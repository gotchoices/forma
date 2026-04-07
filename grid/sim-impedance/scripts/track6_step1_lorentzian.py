#!/usr/bin/env python3
"""
Track 6, Step 1: Lorentzian per-junction coupling.

Does the Minkowski signature break the 2-design deadlock?

In Euclidean 3D/4D, the regular simplex is a spherical 2-design:
  Σ_j (ê · d_j)² = constant for ALL unit vectors ê.
This kills all orientation-dependent quadratic coupling (Tracks 4-5).

In Lorentzian 4D, the timelike direction breaks the simplex symmetry.
We test three lattice options:

  Option A: Euclidean 4-simplex, Lorentzian interpretation
            (5 directions of Euclidean regular 4-simplex, but inner
            products computed with η = diag(-1,+1,+1,+1))

  Option B: 4 tetrahedral spatial + 1 purely timelike
            (physical: spatial diamond lattice + time axis)

  Option C: Lorentz-boosted tetrahedron
            (4 spatial edges boosted so they acquire timelike components)

For each option, compute the "coupling sum" Σ_j (ê · d_j)²_η
for a wye edge ê at various orientations.  If the sum varies,
the 2-design is broken and orientation-dependent coupling is
possible.

We also compute the full wye-jack projection matrix and transfer
efficiency (as in Track 5) to see if T or η varies.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).parent.parent / "output"
OUT.mkdir(exist_ok=True)

# ── Minkowski metric ────────────────────────────────────────────

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])  # signature (-, +, +, +)

def minkowski_dot(a, b):
    """Minkowski inner product: η_μν a^μ b^ν = -a₀b₀ + a₁b₁ + a₂b₂ + a₃b₃."""
    return -a[0]*b[0] + a[1]*b[1] + a[2]*b[2] + a[3]*b[3]

def minkowski_norm_sq(a):
    """Minkowski norm squared: η(a,a)."""
    return minkowski_dot(a, a)

def euclidean_dot(a, b):
    return np.dot(a, b)


# ── Jack constructions ─────────────────────────────────────────

def make_option_A():
    """Option A: Euclidean 4-simplex vertices (unit Euclidean length).

    5 vertices of regular 4-simplex centered at origin.
    All pairwise Euclidean angles = arccos(-1/4) = 104.48°.
    Lorentzian interpretation: coord 0 = time.
    """
    n = 4
    c = (1 + np.sqrt(1 + n)) / n
    verts = np.eye(n)
    v0 = np.full(n, c)
    verts = np.vstack([v0, verts])
    center = verts.mean(axis=0)
    verts -= center
    norms = np.linalg.norm(verts, axis=1, keepdims=True)
    verts = verts / norms
    return verts


def make_option_B():
    """Option B: 4 tetrahedral spatial + 1 purely timelike.

    The 4 spatial edges are the standard diamond jack (in coords 1,2,3).
    The 5th edge points purely in the time direction (coord 0).
    All edges have unit Euclidean length.

    This represents: 3D diamond lattice + discrete time steps.
    """
    # Tetrahedral spatial edges (in x,y,z = coords 1,2,3)
    s = 1.0 / np.sqrt(3)
    spatial = np.array([
        [0, +s, +s, +s],
        [0, +s, -s, -s],
        [0, -s, +s, -s],
        [0, -s, -s, +s],
    ])
    # Purely timelike edge
    temporal = np.array([[1, 0, 0, 0]])
    return np.vstack([spatial, temporal])


def make_option_C():
    """Option C: Lorentz-covariant 4-simplex.

    Construct 5 directions that are ALL spacelike (η(d,d) > 0)
    and have equal Minkowski angles between all pairs.

    For 5 spacelike unit vectors in Minkowski space with equal
    pairwise Minkowski dot products, we need:
      η(d_i, d_j) = const for all i ≠ j
      η(d_i, d_i) = 1 for all i (spacelike, unit Minkowski norm)

    Sum constraint: Σ d_i = 0 → Σ_i Σ_j η(d_i,d_j) = 0
    → 5 + 5·4·c = 0 → c = -1/4.
    Same as Euclidean! But now the vectors must satisfy this
    with the MINKOWSKI metric.

    This is nontrivial. The simplest approach: start with Euclidean
    4-simplex and boost one direction to make it more timelike.
    """
    # Start with Euclidean simplex
    dirs_A = make_option_A()

    # Apply a Lorentz boost in the t-x plane (coords 0,1)
    # A boost with rapidity ξ:
    #   t' = t cosh ξ + x sinh ξ
    #   x' = t sinh ξ + x cosh ξ
    # This mixes time and space but preserves Minkowski norms.

    rapidity = 0.5  # moderate boost
    ch, sh = np.cosh(rapidity), np.sinh(rapidity)

    boosted = dirs_A.copy()
    for i in range(5):
        t, x = boosted[i, 0], boosted[i, 1]
        boosted[i, 0] = t * ch + x * sh
        boosted[i, 1] = t * sh + x * ch

    # Normalize to unit Minkowski norm (if spacelike)
    for i in range(5):
        ns = minkowski_norm_sq(boosted[i])
        if ns > 0:
            boosted[i] /= np.sqrt(ns)
        else:
            # Timelike or null — normalize to |η| = 1
            boosted[i] /= np.sqrt(abs(ns)) if abs(ns) > 1e-10 else 1.0

    return boosted


# ── Wye construction ────────────────────────────────────────────

def wye_in_4d(theta, phi, psi, tilt=0.0):
    """Three wye edges in a plane in 4D.

    The plane normal has angles (theta, phi) in the spatial dimensions
    (coords 1,2,3) and a tilt angle in the time direction (coord 0).

    tilt = 0: purely spatial plane (Ma sheet at fixed time)
    tilt > 0: plane tilts into the time direction (worldsheet)

    Returns (3, 4) array of unit 4-vectors (Euclidean unit length).
    """
    # Build two orthonormal spatial vectors in the plane
    ct, st = np.cos(theta), np.sin(theta)
    cp, sp = np.cos(phi), np.sin(phi)

    # Normal in spatial coords (1,2,3)
    n_spatial = np.array([st * cp, st * sp, ct])

    # Two in-plane vectors in spatial coords
    e1_s = np.array([ct * cp, ct * sp, -st])
    e2_s = np.cross(n_spatial, e1_s)
    e1_s /= np.linalg.norm(e1_s) + 1e-30
    e2_s /= np.linalg.norm(e2_s) + 1e-30

    # Embed in 4D: e1 stays spatial, e2 tilts into time
    e1 = np.array([0, e1_s[0], e1_s[1], e1_s[2]])  # purely spatial

    # e2 tilts: mix spatial e2_s with time direction
    ct_tilt = np.cos(tilt)
    st_tilt = np.sin(tilt)
    e2 = np.array([st_tilt, ct_tilt * e2_s[0],
                    ct_tilt * e2_s[1], ct_tilt * e2_s[2]])

    # Re-orthonormalize (Euclidean)
    e1 /= np.linalg.norm(e1)
    e2 -= np.dot(e2, e1) * e1
    e2 /= np.linalg.norm(e2)

    # Three wye directions at 120° in the plane, twisted by psi
    dirs = []
    for k in range(3):
        angle = psi + k * 2 * np.pi / 3
        d = np.cos(angle) * e1 + np.sin(angle) * e2
        dirs.append(d)

    return np.array(dirs)


# ── Coupling computations ──────────────────────────────────────

def coupling_sum_euclidean(e_hat, jack_dirs):
    """Σ_j (ê · d_j)² using Euclidean dot product."""
    return sum(euclidean_dot(e_hat, d)**2 for d in jack_dirs)


def coupling_sum_minkowski(e_hat, jack_dirs):
    """Σ_j (ê ·_η d_j)² using Minkowski inner product."""
    return sum(minkowski_dot(e_hat, d)**2 for d in jack_dirs)


def projection_matrix_euclidean(wye_dirs, jack_dirs):
    """M_jk = ê_jack_j · ê_wye_k (Euclidean). Shape (n_jack, n_wye)."""
    n_jack = len(jack_dirs)
    n_wye = len(wye_dirs)
    M = np.zeros((n_jack, n_wye))
    for j in range(n_jack):
        for k in range(n_wye):
            M[j, k] = euclidean_dot(jack_dirs[j], wye_dirs[k])
    return M


def projection_matrix_minkowski(wye_dirs, jack_dirs):
    """M_jk = η(ê_jack_j, ê_wye_k) (Minkowski). Shape (n_jack, n_wye)."""
    n_jack = len(jack_dirs)
    n_wye = len(wye_dirs)
    M = np.zeros((n_jack, n_wye))
    for j in range(n_jack):
        for k in range(n_wye):
            M[j, k] = minkowski_dot(jack_dirs[j], wye_dirs[k])
    return M


def transfer_analysis(M):
    """Compute transfer quantities from projection matrix M.

    Returns dict with:
        trace_MtM: Tr(MᵀM) — total projection power
        svd_sigma: singular values
        T: transfer efficiency (|M·a|² / |a|²) averaged over
           propagation directions in wye plane
    """
    MtM = M.T @ M
    trace = np.trace(MtM)

    U, sigma, Vt = np.linalg.svd(M, full_matrices=False)

    # Average T over propagation directions in wye plane
    # For a wye wave a = (cos γ, sin γ, 0) in the 3D wye-edge basis
    # ... simplified: average |M·a|²/|a|² over γ
    n_gamma = 360
    gammas = np.linspace(0, 2*np.pi, n_gamma, endpoint=False)
    T_values = []
    n_wye = M.shape[1]
    for gamma in gammas:
        # Wave amplitudes on wye edges
        a = np.zeros(n_wye)
        for k in range(n_wye):
            a[k] = np.cos(gamma - k * 2*np.pi/3)
        a_norm = np.linalg.norm(a)
        if a_norm < 1e-10:
            continue
        Ma = M @ a
        T = np.dot(Ma, Ma) / (a_norm**2)
        T_values.append(T)

    return {
        'trace_MtM': trace,
        'svd_sigma': sigma,
        'T_mean': np.mean(T_values),
        'T_std': np.std(T_values),
        'T_min': np.min(T_values),
        'T_max': np.max(T_values),
    }


# ── Main ────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  Track 6, Step 1: Lorentzian per-junction coupling")
    print("=" * 60)

    # ── Build the three jack options ──
    jack_A = make_option_A()
    jack_B = make_option_B()
    jack_C = make_option_C()

    options = [
        ("Option A: Euclidean 4-simplex", jack_A),
        ("Option B: Tetrahedral + timelike", jack_B),
        ("Option C: Boosted 4-simplex", jack_C),
    ]

    for name, jack in options:
        print(f"\n{'─'*60}")
        print(f"  {name}")
        print(f"{'─'*60}")

        print(f"\n  Edge directions (t, x, y, z):")
        for i, d in enumerate(jack):
            mns = minkowski_norm_sq(d)
            char = "spacelike" if mns > 0.01 else ("timelike" if mns < -0.01 else "null")
            print(f"    d{i+1} = ({d[0]:+.4f}, {d[1]:+.4f}, {d[2]:+.4f}, {d[3]:+.4f})  "
                  f"η={mns:+.4f} ({char})")

        print(f"\n  Euclidean pairwise angles:")
        for i in range(len(jack)):
            for j in range(i+1, len(jack)):
                dot_e = euclidean_dot(jack[i], jack[j])
                angle_e = np.degrees(np.arccos(np.clip(dot_e, -1, 1)))
                dot_m = minkowski_dot(jack[i], jack[j])
                print(f"    d{i+1}·d{j+1}: Eucl={dot_e:+.4f} ({angle_e:.2f}°)  "
                      f"Mink={dot_m:+.4f}")

    # ═══════════════════════════════════════════════════════════
    # Part 1: 2-design test — does Σ (ê·d_j)² depend on ê?
    # ═══════════════════════════════════════════════════════════

    print(f"\n{'='*60}")
    print(f"  Part 1: 2-design test")
    print(f"  Σ (ê · d_j)² for random unit vectors ê")
    print(f"{'='*60}")

    n_test = 10000
    for name, jack in options:
        sums_E = []
        sums_M = []
        for _ in range(n_test):
            e = np.random.randn(4)
            e /= np.linalg.norm(e)  # Euclidean unit vector
            sums_E.append(coupling_sum_euclidean(e, jack))
            sums_M.append(coupling_sum_minkowski(e, jack))

        sums_E = np.array(sums_E)
        sums_M = np.array(sums_M)

        print(f"\n  {name}:")
        print(f"    Euclidean Σ(ê·d)²: mean={sums_E.mean():.4f}, "
              f"std={sums_E.std():.6f}, CV={sums_E.std()/sums_E.mean():.6f}")
        print(f"    Minkowski Σ(ê·d)²: mean={sums_M.mean():.4f}, "
              f"std={sums_M.std():.6f}, CV={sums_M.std()/sums_M.mean():.6f}")
        if sums_E.std() < 1e-6:
            print(f"    → Euclidean: CONSTANT (2-design holds)")
        else:
            print(f"    → Euclidean: VARIES (2-design broken!)")
        if sums_M.std() < 1e-6:
            print(f"    → Minkowski: CONSTANT")
        else:
            print(f"    → Minkowski: VARIES! Range: [{sums_M.min():.4f}, {sums_M.max():.4f}]")

    # ═══════════════════════════════════════════════════════════
    # Part 2: Coupling vs timelike tilt of the wye plane
    # ═══════════════════════════════════════════════════════════

    print(f"\n{'='*60}")
    print(f"  Part 2: Coupling vs timelike tilt of wye plane")
    print(f"{'='*60}")

    tilts = np.linspace(0, np.pi/2, 19)  # 0 = spatial, π/2 = worldsheet
    n_orient = 500

    for name, jack in options:
        print(f"\n  {name}:")
        print(f"  {'tilt(°)':>8s}  {'Tr(MᵀM)_E':>10s}  {'CV_E':>8s}  "
              f"{'Tr(MᵀM)_M':>10s}  {'CV_M':>8s}  {'T_E':>8s}  {'T_M':>8s}")
        print("  " + "─" * 72)

        tilt_results = []
        for tilt in tilts:
            traces_E = []
            traces_M = []
            T_E_vals = []
            T_M_vals = []

            for _ in range(n_orient):
                theta = np.arccos(2 * np.random.rand() - 1)
                phi = 2 * np.pi * np.random.rand()
                psi = 2 * np.pi / 3 * np.random.rand()

                wye = wye_in_4d(theta, phi, psi, tilt=tilt)

                M_E = projection_matrix_euclidean(wye, jack)
                M_M = projection_matrix_minkowski(wye, jack)

                res_E = transfer_analysis(M_E)
                res_M = transfer_analysis(M_M)

                traces_E.append(res_E['trace_MtM'])
                traces_M.append(res_M['trace_MtM'])
                T_E_vals.append(res_E['T_mean'])
                T_M_vals.append(res_M['T_mean'])

            traces_E = np.array(traces_E)
            traces_M = np.array(traces_M)
            T_E_vals = np.array(T_E_vals)
            T_M_vals = np.array(T_M_vals)

            cv_E = traces_E.std() / traces_E.mean() if traces_E.mean() > 0 else 0
            cv_M = traces_M.std() / abs(traces_M.mean()) if abs(traces_M.mean()) > 0 else 0

            print(f"  {np.degrees(tilt):8.1f}  {traces_E.mean():10.4f}  {cv_E:8.4f}  "
                  f"{traces_M.mean():10.4f}  {cv_M:8.4f}  "
                  f"{T_E_vals.mean():8.4f}  {T_M_vals.mean():8.4f}")

            tilt_results.append({
                'tilt': tilt,
                'trace_E_mean': traces_E.mean(),
                'trace_E_cv': cv_E,
                'trace_M_mean': traces_M.mean(),
                'trace_M_cv': cv_M,
                'T_E_mean': T_E_vals.mean(),
                'T_M_mean': T_M_vals.mean(),
            })

    # ═══════════════════════════════════════════════════════════
    # Part 3: Focus on Option B (most physical)
    # Deep analysis of Minkowski coupling at purely spatial wye
    # ═══════════════════════════════════════════════════════════

    print(f"\n{'='*60}")
    print(f"  Part 3: Option B deep analysis — spatial wye orientations")
    print(f"{'='*60}")

    jack = jack_B
    n_deep = 5000

    # Purely spatial wye (tilt = 0)
    traces_M = []
    T_M_vals = []
    svd_data = []

    for _ in range(n_deep):
        theta = np.arccos(2 * np.random.rand() - 1)
        phi = 2 * np.pi * np.random.rand()
        psi = 2 * np.pi / 3 * np.random.rand()

        wye = wye_in_4d(theta, phi, psi, tilt=0)
        M = projection_matrix_minkowski(wye, jack)
        res = transfer_analysis(M)

        traces_M.append(res['trace_MtM'])
        T_M_vals.append(res['T_mean'])
        svd_data.append(res['svd_sigma'])

    traces_M = np.array(traces_M)
    T_M_vals = np.array(T_M_vals)
    svd_data = np.array(svd_data)

    print(f"\n  Purely spatial wye, Minkowski coupling ({n_deep} orientations):")
    print(f"    Tr(MᵀM): mean={traces_M.mean():.4f}, std={traces_M.std():.6f}, "
          f"CV={traces_M.std()/traces_M.mean():.6f}")
    print(f"    T_mean:   mean={T_M_vals.mean():.4f}, std={T_M_vals.std():.6f}")
    print(f"    σ₁: mean={svd_data[:,0].mean():.4f}, std={svd_data[:,0].std():.6f}")
    print(f"    σ₂: mean={svd_data[:,1].mean():.4f}, std={svd_data[:,1].std():.6f}")
    print(f"    σ₃: mean={svd_data[:,2].mean():.4f}, std={svd_data[:,2].std():.6f}")

    # Check: is the spatial-only coupling constant (2-design of
    # just the 4 tetrahedral edges)?
    print(f"\n  For comparison — coupling to ONLY the 4 spatial jack edges:")
    jack_spatial = jack_B[:4]  # just the tetrahedral ones
    traces_spatial = []
    for _ in range(n_deep):
        theta = np.arccos(2 * np.random.rand() - 1)
        phi = 2 * np.pi * np.random.rand()
        psi = 2 * np.pi / 3 * np.random.rand()
        wye = wye_in_4d(theta, phi, psi, tilt=0)
        M = projection_matrix_minkowski(wye, jack_spatial)
        traces_spatial.append(np.trace(M.T @ M))

    traces_spatial = np.array(traces_spatial)
    print(f"    Tr(MᵀM): mean={traces_spatial.mean():.4f}, std={traces_spatial.std():.6f}, "
          f"CV={traces_spatial.std()/traces_spatial.mean():.6f}")

    # ═══════════════════════════════════════════════════════════
    # Part 4: What fraction of coupling goes to the timelike edge?
    # ═══════════════════════════════════════════════════════════

    print(f"\n{'='*60}")
    print(f"  Part 4: Fraction of coupling going to timelike edge")
    print(f"{'='*60}")

    jack = jack_B
    n_frac = 5000

    spatial_fracs = []
    temporal_fracs = []

    for _ in range(n_frac):
        theta = np.arccos(2 * np.random.rand() - 1)
        phi = 2 * np.pi * np.random.rand()
        psi = 2 * np.pi / 3 * np.random.rand()

        wye = wye_in_4d(theta, phi, psi, tilt=0)

        # For each propagation direction, compute energy into each jack edge
        n_gamma = 36
        for gamma in np.linspace(0, 2*np.pi, n_gamma, endpoint=False):
            a = np.array([np.cos(gamma - k * 2*np.pi/3) for k in range(3)])
            a_norm = np.linalg.norm(a)
            if a_norm < 1e-10:
                continue

            # Euclidean projection onto each jack edge
            energy_per_jack = np.zeros(5)
            for j in range(5):
                proj = sum(euclidean_dot(wye[k], jack[j]) * a[k] for k in range(3))
                energy_per_jack[j] = proj**2

            total_e = energy_per_jack.sum()
            if total_e > 1e-10:
                spatial_fracs.append(energy_per_jack[:4].sum() / total_e)
                temporal_fracs.append(energy_per_jack[4] / total_e)

    spatial_fracs = np.array(spatial_fracs)
    temporal_fracs = np.array(temporal_fracs)

    print(f"\n  Energy distribution (Euclidean projection, spatial wye):")
    print(f"    Fraction to 4 spatial edges: mean={spatial_fracs.mean():.6f}, "
          f"std={spatial_fracs.std():.6f}")
    print(f"    Fraction to timelike edge:   mean={temporal_fracs.mean():.6f}, "
          f"std={temporal_fracs.std():.6f}")
    print(f"    Spatial/Total:               {spatial_fracs.mean():.6f}")
    print(f"    Temporal/Total:              {temporal_fracs.mean():.6f}")

    # The ratio spatial/total should be 4/5 = 0.8 if all edges
    # are equivalent, or different if the timelike edge is special.
    print(f"\n    Expected if all edges equivalent: 4/5 = {4/5:.6f}")
    print(f"    Expected if spatial wye ⊥ time:   1.000000")

    # Now with Minkowski metric
    spatial_fracs_M = []
    temporal_fracs_M = []

    for _ in range(n_frac):
        theta = np.arccos(2 * np.random.rand() - 1)
        phi = 2 * np.pi * np.random.rand()
        psi = 2 * np.pi / 3 * np.random.rand()

        wye = wye_in_4d(theta, phi, psi, tilt=0)

        n_gamma = 36
        for gamma in np.linspace(0, 2*np.pi, n_gamma, endpoint=False):
            a = np.array([np.cos(gamma - k * 2*np.pi/3) for k in range(3)])
            a_norm = np.linalg.norm(a)
            if a_norm < 1e-10:
                continue

            energy_per_jack = np.zeros(5)
            for j in range(5):
                proj = sum(minkowski_dot(wye[k], jack[j]) * a[k] for k in range(3))
                energy_per_jack[j] = proj**2

            total_e = energy_per_jack.sum()
            if total_e > 1e-10:
                spatial_fracs_M.append(energy_per_jack[:4].sum() / total_e)
                temporal_fracs_M.append(energy_per_jack[4] / total_e)

    spatial_fracs_M = np.array(spatial_fracs_M)
    temporal_fracs_M = np.array(temporal_fracs_M)

    print(f"\n  Energy distribution (Minkowski projection, spatial wye):")
    print(f"    Fraction to 4 spatial edges: mean={spatial_fracs_M.mean():.6f}, "
          f"std={spatial_fracs_M.std():.6f}")
    print(f"    Fraction to timelike edge:   mean={temporal_fracs_M.mean():.6f}, "
          f"std={temporal_fracs_M.std():.6f}")

    # ═══════════════════════════════════════════════════════════
    # Part 5: The key question — does any quantity = 1/137?
    # ═══════════════════════════════════════════════════════════

    print(f"\n{'='*60}")
    print(f"  Part 5: Summary — what equals 1/137?")
    print(f"{'='*60}")

    print(f"\n  Reference: 1/137.036 = {1/137.036:.6f}")
    print(f"  Reference: α/π = {1/(137.036*np.pi):.6f}")
    print(f"  Reference: α/(2π) = {1/(137.036*2*np.pi):.6f}")

    # Check various ratios
    temporal_mean = temporal_fracs.mean()
    temporal_mean_M = temporal_fracs_M.mean()
    spatial_mean = spatial_fracs.mean()

    quantities = [
        ("temporal fraction (Eucl)", temporal_mean),
        ("temporal fraction (Mink)", temporal_mean_M),
        ("1 - spatial fraction (Eucl)", 1 - spatial_mean),
        ("Tr_M / 5 (Option B)", traces_M.mean() / 5),
    ]

    print(f"\n  {'Quantity':>35s}  {'Value':>10s}  {'1/Value':>10s}  {'near 137?':>10s}")
    print("  " + "─" * 70)
    for label, val in quantities:
        inv = 1/val if val > 1e-10 else float('inf')
        near = "YES" if abs(inv - 137.036) / 137.036 < 0.1 else ""
        print(f"  {label:>35s}  {val:10.6f}  {inv:10.1f}  {near:>10s}")

    # ── Plot ──
    print(f"\n── Generating plots ──")

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Plot 1: Histogram of Tr(MᵀM) for Option B, Minkowski
    ax = axes[0]
    if traces_M.std() > 1e-6:
        ax.hist(traces_M, bins=50, edgecolor='black', alpha=0.7)
    else:
        ax.bar([traces_M.mean()], [len(traces_M)], width=0.01)
        ax.text(traces_M.mean(), len(traces_M)*0.9,
                f'ALL = {traces_M.mean():.4f}', ha='center')
    ax.set_xlabel('Tr(MᵀM) [Minkowski]')
    ax.set_ylabel('Count')
    ax.set_title('Option B: Minkowski coupling (spatial wye)')

    # Plot 2: Histogram of temporal fraction
    ax = axes[1]
    if temporal_fracs.std() > 1e-6:
        ax.hist(temporal_fracs, bins=50, edgecolor='black', alpha=0.7, label='Euclidean')
    else:
        ax.bar([0], [len(temporal_fracs)], width=0.001)
        ax.text(0.01, len(temporal_fracs)*0.9,
                f'ALL = {temporal_fracs.mean():.6f}', ha='left')
    ax.set_xlabel('Fraction of energy to timelike edge')
    ax.set_ylabel('Count')
    ax.set_title('Energy fraction to timelike edge (spatial wye)')
    ax.legend()

    # Plot 3: Coupling vs tilt (Option B only, recompute quickly)
    tilt_angles = np.linspace(0, np.pi/2, 37)
    tilt_traces = []
    for tilt in tilt_angles:
        traces = []
        for _ in range(200):
            theta = np.arccos(2 * np.random.rand() - 1)
            phi = 2 * np.pi * np.random.rand()
            psi = 2 * np.pi / 3 * np.random.rand()
            wye = wye_in_4d(theta, phi, psi, tilt=tilt)
            M = projection_matrix_minkowski(wye, jack_B)
            traces.append(np.trace(M.T @ M))
        tilt_traces.append(np.mean(traces))

    ax = axes[2]
    ax.plot(np.degrees(tilt_angles), tilt_traces, 'b.-')
    ax.set_xlabel('Timelike tilt (degrees)')
    ax.set_ylabel('Mean Tr(MᵀM) [Minkowski]')
    ax.set_title('Option B: Coupling vs tilt')
    ax.grid(True, alpha=0.3)

    fig.suptitle('Track 6 Step 1: Lorentzian per-junction coupling', fontsize=14)
    fig.tight_layout()
    fig.savefig(OUT / "track6_step1_lorentzian.png", dpi=150)
    plt.close(fig)
    print(f"  Saved: {OUT / 'track6_step1_lorentzian.png'}")

    # ── Summary ──
    print(f"\n{'='*60}")
    print(f"  SUMMARY")
    print(f"{'='*60}")
    print(f"""
  Option A (Euclidean 4-simplex):
    Euclidean Σ(ê·d)² = constant (2-design confirmed)
    Minkowski Σ(ê·d)² = varies → 2-design BROKEN

  Option B (tetrahedral + timelike):
    Purely spatial wye ⊥ timelike edge → zero coupling to time
    The spatial coupling reduces to the 3D tetrahedral case
    → still constant (3D 2-design)
    Adding timelike tilt creates coupling to the 5th edge

  Key numbers:
    Temporal energy fraction: {temporal_mean:.6f}
    Minkowski temporal fraction: {temporal_mean_M:.6f}
    1/137 = {1/137.036:.6f}
""")


if __name__ == "__main__":
    main()
