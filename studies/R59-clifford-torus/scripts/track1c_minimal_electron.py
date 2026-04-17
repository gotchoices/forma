"""
R59 Track 1c: Start minimal — one electron sheet + ℵ + S + t.

Instead of bolting coupling onto the full model-E metric,
start from scratch with the simplest possible system:

  1. One 2-torus (electron sheet): tube + ring
  2. One ℵ dimension (switchable — on or off)
  3. Three spatial dimensions (S)
  4. One time dimension (t)

Total: 2 Ma + 1 ℵ + 3 S + 1 t = 7D (or 6D without ℵ)

Step by step:
  A. Bare electron sheet: find (ε, s) that give m_e = 0.511 MeV
  B. Add time: sweep Ma-t entries, measure coupling
  C. Add ℵ: sweep Ma-ℵ and ℵ-t entries, measure coupling
  D. Compare: which setup gives clean α coupling without
     disturbing the electron mass?
  E. Check: did we touch any entries that a proton or neutrino
     sheet would need?

The point: isolate the coupling question on the SIMPLEST
system before adding complexity.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import math
import numpy as np
from lib.ma_model_d import M_E_MEV, _TWO_PI_HC, ALPHA as ALPHA_CONST

ALPHA = 1.0 / 137.036
TWO_PI_HC = _TWO_PI_HC


def build_electron_metric(eps, s):
    """
    Build the 2×2 dimensionless metric for one sheet.

    G̃ = [[1, s*ε], [s*ε, 1 + s²*ε²]]

    (tube is dim 0, ring is dim 1)
    """
    return np.array([
        [1.0,        s * eps],
        [s * eps,    1.0 + s**2 * eps**2]
    ])


def electron_L_ring(eps, s):
    """Derive L_ring (fm) from (ε, s) to give m_e."""
    mu = math.sqrt((1/eps)**2 + (2 - s)**2)  # mode (1,2)
    return TWO_PI_HC * mu / M_E_MEV


def build_full_metric(A_2x2, L_ring, eps, include_aleph=False,
                       sigma_Ma_t=None, sigma_Ma_aleph=None,
                       sigma_aleph_t=0.0, sigma_aleph_S=0.0):
    """
    Build the full metric for one electron sheet + S + t (+ ℵ).

    Without ℵ: 6D = 2 Ma + 3 S + 1 t
      Indices: 0 tube, 1 ring, 2 Sx, 3 Sy, 4 Sz, 5 t

    With ℵ: 7D = 2 Ma + 1 ℵ + 3 S + 1 t
      Indices: 0 tube, 1 ring, 2 ℵ, 3 Sx, 4 Sy, 5 Sz, 6 t
    """
    if include_aleph:
        N = 7
        idx_aleph = 2
        idx_S = [3, 4, 5]
        idx_t = 6
    else:
        N = 6
        idx_aleph = None
        idx_S = [2, 3, 4]
        idx_t = 5

    G = np.zeros((N, N))

    # Ma block (0-1)
    G[0:2, 0:2] = A_2x2

    # ℵ diagonal
    if include_aleph:
        G[idx_aleph, idx_aleph] = 1.0

    # S diagonal
    for j in idx_S:
        G[j, j] = 1.0

    # t diagonal (Lorentzian)
    G[idx_t, idx_t] = -1.0

    # Ma-t coupling (direct)
    if sigma_Ma_t is not None:
        for i in range(2):
            G[i, idx_t] = sigma_Ma_t[i]
            G[idx_t, i] = sigma_Ma_t[i]

    # Ma-ℵ coupling
    if include_aleph and sigma_Ma_aleph is not None:
        for i in range(2):
            G[i, idx_aleph] = sigma_Ma_aleph[i]
            G[idx_aleph, i] = sigma_Ma_aleph[i]

    # ℵ-t coupling
    if include_aleph:
        G[idx_aleph, idx_t] = sigma_aleph_t
        G[idx_t, idx_aleph] = sigma_aleph_t

    # ℵ-S coupling
    if include_aleph:
        for j in idx_S:
            G[idx_aleph, j] = sigma_aleph_S
            G[j, idx_aleph] = sigma_aleph_S

    return G, idx_t


def mass_shell(G, idx_t, L_2, n2):
    """
    Solve mass-shell on the full metric.

    k = (n₁/L_tube, n₂/L_ring, [0 for ℵ], 0, 0, 0, ω)
    Returns (E_low, E_high).
    """
    try:
        Gi = np.linalg.inv(G)
    except:
        return np.nan, np.nan

    N = len(G)
    nt = np.zeros(N)
    nt[0] = n2[0] / L_2[0]
    nt[1] = n2[1] / L_2[1]
    # All other spatial/ℵ components = 0

    # Quadratic in ω: a ω² + b ω + c = 0
    a = Gi[idx_t, idx_t]
    b = 2.0 * np.dot(Gi[:, idx_t], nt)  # includes all cross terms with t
    # But nt only has nonzero Ma components, so:
    b = 2.0 * (Gi[0, idx_t] * nt[0] + Gi[1, idx_t] * nt[1])
    c = nt @ Gi @ nt

    disc = b**2 - 4*a*c
    if disc < 0:
        return np.nan, np.nan

    w1 = (-b + math.sqrt(disc)) / (2*a)
    w2 = (-b - math.sqrt(disc)) / (2*a)

    return min(TWO_PI_HC * abs(w1), TWO_PI_HC * abs(w2)), \
           max(TWO_PI_HC * abs(w1), TWO_PI_HC * abs(w2))


def main():
    print("=" * 75)
    print("R59 Track 1c: Minimal electron sheet + ℵ + S + t")
    print("=" * 75)
    print()

    # ── Step A: Bare electron sheet ────────────────────────
    print("─" * 75)
    print("Step A: Bare electron sheet — (ε, s) for m_e = 0.511 MeV")
    print("─" * 75)
    print()

    # Model-E values
    eps_e = 397.074
    s_e = 2.004200

    A_e = build_electron_metric(eps_e, s_e)
    L_ring = electron_L_ring(eps_e, s_e)
    L_tube = eps_e * L_ring
    L_2 = np.array([L_tube, L_ring])

    mu_12 = math.sqrt((1/eps_e)**2 + (2 - s_e)**2)
    E_bare = TWO_PI_HC * mu_12 / L_ring

    print(f"  ε_e = {eps_e}, s_e = {s_e}")
    print(f"  L_tube = {L_tube:.4f} fm, L_ring = {L_ring:.4f} fm")
    print(f"  μ(1,2) = {mu_12:.6f}")
    print(f"  E(1,2) = {E_bare:.4f} MeV (target: {M_E_MEV:.4f})")
    print()
    print(f"  2×2 metric:")
    print(f"    G̃ = [[{A_e[0,0]:.4f}, {A_e[0,1]:.4f}],")
    print(f"         [{A_e[1,0]:.4f}, {A_e[1,1]:.1f}]]")
    print(f"  Off-diagonal ratio: {abs(A_e[0,1])/math.sqrt(A_e[0,0]*A_e[1,1]):.6f}")
    print(f"  (0.999999 = at PD boundary, as R55 found)")
    print()

    # Verify mass-shell on bare metric (no coupling)
    G_bare, idx_t = build_full_metric(A_e, L_ring, eps_e,
                                        include_aleph=False)
    E_lo, E_hi = mass_shell(G_bare, idx_t, L_2, (1, 2))
    print(f"  Mass-shell on 6D bare metric: E = {E_lo:.4f} MeV")
    print(f"  Match: {'✓' if abs(E_lo - M_E_MEV)/M_E_MEV < 0.001 else '✗'}")
    print()

    # ── Step B: Direct Ma-t (no ℵ) ────────────────────────
    print("─" * 75)
    print("Step B: Add time — direct Ma-t coupling (no ℵ)")
    print("─" * 75)
    print()

    # Sweep: try tube-only, ring-only, and both
    configs = [
        ("tube-only",  lambda s: np.array([-s, 0])),
        ("ring-only",  lambda s: np.array([0, -s])),
        ("both equal", lambda s: np.array([-s, -s])),
    ]

    for config_name, make_b in configs:
        print(f"  Config: {config_name}")
        print(f"  {'σ':>8s}  {'sig':>4s}  {'E_lo':>8s}  {'E_hi':>8s}  "
              f"{'Δm%':>7s}  {'|Δm|/m':>10s}  {'ratio/α':>8s}  {'dir':>5s}")
        print(f"  {'─'*8}  {'─'*4}  {'─'*8}  {'─'*8}  "
              f"{'─'*7}  {'─'*10}  {'─'*8}  {'─'*5}")

        for sigma in [0.001, 0.005, 0.01, 0.05, 0.1, 0.3, 0.5]:
            b = make_b(sigma)
            G, it = build_full_metric(A_e, L_ring, eps_e,
                                       include_aleph=False,
                                       sigma_Ma_t=b)
            eigs = np.linalg.eigvalsh(G)
            n_neg = np.sum(eigs < 0)
            sig_ok = "✓" if n_neg == 1 else f"✗{n_neg}"

            Elo, Ehi = mass_shell(G, it, L_2, (1, 2))
            if np.isnan(Elo):
                print(f"  {sigma:8.4f}  {sig_ok:>4s}  NaN")
                continue

            dm = (Elo - E_bare) / E_bare * 100
            ae = abs(Elo - E_bare) / E_bare
            direction = "UP" if Elo > E_bare else "DOWN"

            print(f"  {sigma:8.4f}  {sig_ok:>4s}  {Elo:8.4f}  {Ehi:8.4f}  "
                  f"{dm:+7.3f}  {ae:10.6f}  {ae/ALPHA:8.4f}  {direction:>5s}")

        print()

    # ── Step C: ℵ-mediated (Ma-ℵ-t chain) ─────────────────
    print("─" * 75)
    print("Step C: Add ℵ — coupling through Ma-ℵ-t chain")
    print("  Ma-ℵ on ring at -1/(2π), ℵ-t = σ (one knob)")
    print("─" * 75)
    print()

    sigma_Ma_a = np.array([0, -1/(2*math.pi)])  # ring only, negative for electron

    print(f"  Ma-ℵ = [0, {sigma_Ma_a[1]:+.6f}]")
    print()

    print(f"  {'σ_ℵt':>8s}  {'sig':>4s}  {'E_lo':>8s}  {'E_hi':>8s}  "
          f"{'Δm%':>7s}  {'|Δm|/m':>10s}  {'ratio/α':>8s}  {'dir':>5s}")
    print(f"  {'─'*8}  {'─'*4}  {'─'*8}  {'─'*8}  "
          f"{'─'*7}  {'─'*10}  {'─'*8}  {'─'*5}")

    for sigma_at in [0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0]:
        G, it = build_full_metric(A_e, L_ring, eps_e,
                                   include_aleph=True,
                                   sigma_Ma_aleph=sigma_Ma_a,
                                   sigma_aleph_t=sigma_at)
        eigs = np.linalg.eigvalsh(G)
        n_neg = np.sum(eigs < 0)
        sig_ok = "✓" if n_neg == 1 else f"✗{n_neg}"

        # Need L_2 for the 7D metric — same as before for Ma dims
        Elo, Ehi = mass_shell(G, it, L_2, (1, 2))
        if np.isnan(Elo):
            print(f"  {sigma_at:8.4f}  {sig_ok:>4s}  NaN")
            continue

        dm = (Elo - E_bare) / E_bare * 100
        ae = abs(Elo - E_bare) / E_bare
        direction = "UP" if Elo > E_bare else "DOWN"

        print(f"  {sigma_at:8.4f}  {sig_ok:>4s}  {Elo:8.4f}  {Ehi:8.4f}  "
              f"{dm:+7.3f}  {ae:10.6f}  {ae/ALPHA:8.4f}  {direction:>5s}")

    print()

    # ── Step D: Fine-tune for α ────────────────────────────
    print("─" * 75)
    print("Step D: Fine-tune — find σ that gives |Δm|/m = α")
    print("─" * 75)
    print()

    # D1: Direct ring-only Ma-t
    print("  D1: Direct ring-only Ma-t (no ℵ)")
    lo, hi = 0.001, 0.5
    for _ in range(200):
        mid = (lo+hi)/2
        b = np.array([0, -mid])
        G, it = build_full_metric(A_e, L_ring, eps_e,
                                   include_aleph=False, sigma_Ma_t=b)
        eigs = np.linalg.eigvalsh(G)
        if np.sum(eigs < 0) != 1: hi = mid; continue
        Elo, _ = mass_shell(G, it, L_2, (1, 2))
        if np.isnan(Elo): hi = mid; continue
        ae = abs(Elo - E_bare) / E_bare
        if ae < ALPHA: lo = mid
        else: hi = mid

    opt1 = (lo+hi)/2
    G1, it1 = build_full_metric(A_e, L_ring, eps_e,
                                  include_aleph=False,
                                  sigma_Ma_t=np.array([0, -opt1]))
    E1_lo, E1_hi = mass_shell(G1, it1, L_2, (1, 2))
    dir1 = "UP" if E1_lo > E_bare else "DOWN"
    print(f"  σ = {opt1:.8f}, E = {E1_lo:.6f}, direction = {dir1}")
    print(f"  |Δm|/m = {abs(E1_lo-E_bare)/E_bare:.8f} (target α = {ALPHA:.8f})")
    print()

    # D2: ℵ-mediated (ring Ma-ℵ, single ℵ-t)
    print("  D2: ℵ-mediated (ring Ma-ℵ = -1/2π, single σ_ℵt)")
    lo, hi = 0.01, 5.0
    for _ in range(200):
        mid = (lo+hi)/2
        G, it = build_full_metric(A_e, L_ring, eps_e,
                                   include_aleph=True,
                                   sigma_Ma_aleph=sigma_Ma_a,
                                   sigma_aleph_t=mid)
        eigs = np.linalg.eigvalsh(G)
        if np.sum(eigs < 0) != 1: hi = mid; continue
        Elo, _ = mass_shell(G, it, L_2, (1, 2))
        if np.isnan(Elo): hi = mid; continue
        ae = abs(Elo - E_bare) / E_bare
        if ae < ALPHA: lo = mid
        else: hi = mid

    opt2 = (lo+hi)/2
    G2, it2 = build_full_metric(A_e, L_ring, eps_e,
                                  include_aleph=True,
                                  sigma_Ma_aleph=sigma_Ma_a,
                                  sigma_aleph_t=opt2)
    E2_lo, E2_hi = mass_shell(G2, it2, L_2, (1, 2))
    dir2 = "UP" if E2_lo > E_bare else "DOWN"
    print(f"  σ_ℵt = {opt2:.8f}, E = {E2_lo:.6f}, direction = {dir2}")
    print(f"  |Δm|/m = {abs(E2_lo-E_bare)/E_bare:.8f} (target α = {ALPHA:.8f})")
    print()

    # ── Step E: What entries did we touch? ─────────────────
    print("─" * 75)
    print("Step E: Which metric entries were touched?")
    print("─" * 75)
    print()

    print("  D1 (direct Ma-t, no ℵ):")
    print(f"    Touched: G̃[ring, t] = {-opt1:+.8f}")
    print(f"    NOT touched: G̃[tube, *], G̃[tube,ring] (the shear s_e)")
    print(f"    A proton sheet would need its OWN ring-t entry (independent)")
    print(f"    A neutrino sheet would need its OWN ring-t entry (independent)")
    print(f"    No conflict with other sheets.")
    print()

    print("  D2 (ℵ-mediated):")
    print(f"    Touched: G̃[ring, ℵ] = {sigma_Ma_a[1]:+.8f}")
    print(f"    Touched: G̃[ℵ, t] = {opt2:+.8f}")
    print(f"    NOT touched: G̃[tube, *], G̃[tube,ring] (the shear s_e)")
    print(f"    A proton sheet would share the SAME ℵ and ℵ-t entry")
    print(f"    (universality comes from ℵ being common to all sheets)")
    print(f"    Each sheet adds its own ring-ℵ entry.")
    print()

    # ── Step F: Other modes on this sheet ──────────────────
    print("─" * 75)
    print("Step F: Other modes on the electron sheet")
    print("  (Do generation candidates work on the coupled metric?)")
    print("─" * 75)
    print()

    test_modes = [(1,1), (1,2), (1,3), (2,4), (3,5), (3,8), (1,-1)]

    for label, G_test, it_test in [
        ("D1 (direct)", G1, it1),
        ("D2 (ℵ-med)", G2, it2),
    ]:
        print(f"  {label}:")
        print(f"    {'mode':>8s}  {'E_bare':>10s}  {'E_coupled':>10s}  {'ratio':>8s}  {'Δ%':>7s}")
        print(f"    {'─'*8}  {'─'*10}  {'─'*10}  {'─'*8}  {'─'*7}")

        for n in test_modes:
            mu = math.sqrt((n[0]/eps_e)**2 + (n[1] - n[0]*s_e)**2)
            Eb = TWO_PI_HC * mu / L_ring
            Elo, Ehi = mass_shell(G_test, it_test, L_2, n)
            ratio = Elo / E_bare if E_bare > 0 else 0
            dm = (Elo - Eb) / Eb * 100 if Eb > 0 and not np.isnan(Elo) else 0
            label_mode = ""
            if n == (1,2): label_mode = " ← electron"
            if abs(ratio - 206.77) < 30: label_mode = " ← muon range"
            print(f"    {str(n):>8s}  {Eb:10.4f}  {Elo:10.4f}  {ratio:8.1f}  {dm:+7.3f}{label_mode}")

        print()

    # ── Summary ────────────────────────────────────────────
    print("=" * 75)
    print("SUMMARY")
    print("=" * 75)
    print()
    print(f"  Electron sheet: ε={eps_e}, s={s_e}")
    print(f"  m_e = {E_bare:.4f} MeV")
    print()
    print(f"  D1 (direct ring-t): σ = {opt1:.6f}, mass {dir1}")
    print(f"  D2 (ℵ-mediated):   σ_ℵt = {opt2:.6f}, mass {dir2}")
    print()
    print(f"  Entries touched:")
    print(f"    D1: ring-t only (one entry per sheet)")
    print(f"    D2: ring-ℵ + ℵ-t (one entry per sheet + one shared)")
    print()
    print(f"  Neither touches the tube dimension or the internal shear.")
    print(f"  Both are compatible with adding proton/neutrino sheets later.")
    print()
    print(f"  α = {ALPHA:.6e}")
    print()
    print("Track 1c complete.")


if __name__ == '__main__':
    main()
