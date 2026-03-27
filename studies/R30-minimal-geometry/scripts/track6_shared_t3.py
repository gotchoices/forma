#!/usr/bin/env python3
"""
R30 Track 6: Shared-dimension T³ — can electron and proton share a surface?

Build a T³ solver (3 material dimensions, 3 shears) and test whether
the particle spectrum can be reproduced with fewer dimensions than Ma.

Dimensions:
    A — electron tube-like (large, ~400 fm)
    B — shared dimension (free parameter)
    C — proton ring-like (small, ~0.2 fm)

Charge: Q = -n_a + n_c  (analogous to Ma's Q = -n₁ + n₅)
Spin:   count odd |n_a|, |n_c|  (A and C are "tube-like")

Key question: does T³ reproduce e, p, n, μ, π, K with correct
mass, charge, AND spin?
"""

import sys, os, math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma import hbar_c_MeV_fm, M_E_MEV, M_P_MEV, M_N_MEV, ALPHA
from lib.ma import solve_shear_for_alpha
from lib.ma_solver import self_consistent_metric

TWO_PI_HC = 2 * math.pi * hbar_c_MeV_fm


# ══════════════════════════════════════════════════════════════════
#  T³ solver
# ══════════════════════════════════════════════════════════════════

def t3_metric(L_a, L_b, L_c, s_ab=0.0, s_bc=0.0, s_ac=0.0):
    """Build T³ scaled metric and inverse, analogous to Ma."""
    L = np.array([L_a, L_b, L_c])

    S = np.zeros((3, 3))
    S[0, 1] = s_ab
    S[1, 2] = s_bc
    S[0, 2] = s_ac

    B = np.diag(L) @ (np.eye(3) + S)
    G_phys = B.T @ B

    Gt = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            Gt[i, j] = G_phys[i, j] / (L[i] * L[j])

    Gti = np.linalg.inv(Gt)
    return Gt, Gti, L


def t3_energy(n, Gti, L):
    """Mode energy on T³ in MeV."""
    n = np.asarray(n, dtype=float)
    ntilde = n / L
    E2 = TWO_PI_HC**2 * ntilde @ Gti @ ntilde
    return math.sqrt(max(E2, 0.0))


def t3_charge(n):
    """Charge Q = -n_a + n_c."""
    return -int(n[0]) + int(n[2])


def t3_spin(n):
    """Spin count = number of odd tube-like windings (dims A, C)."""
    return (abs(int(n[0])) % 2) + (abs(int(n[2])) % 2)


def t3_circumferences(L_b, e_mode=(1, 2, 0), p_mode=(0, 1, 1),
                       s_ab=0.0, s_bc=0.0, s_ac=0.0):
    """
    Compute L_a and L_c from electron and proton mass constraints.

    Given L_b (free), winding numbers for e and p, and shears,
    find L_a and L_c such that the electron and proton modes
    have the correct masses.

    Uses numerical root-finding since shears couple the equations.
    """
    from scipy.optimize import brentq

    def electron_error(L_a):
        _, Gti, L = t3_metric(L_a, L_b, 1.0, s_ab, s_bc, s_ac)
        # Electron mode doesn't use C (n_c=0), but metric might couple
        # First pass: approximate L_c = 0.21 fm
        _, Gti2, L2 = t3_metric(L_a, L_b, 0.21, s_ab, s_bc, s_ac)
        return t3_energy(e_mode, Gti2, L2) - M_E_MEV

    def proton_error(L_c, L_a):
        _, Gti, L = t3_metric(L_a, L_b, L_c, s_ab, s_bc, s_ac)
        return t3_energy(p_mode, Gti, L) - M_P_MEV

    # For diagonal metric (no shear), analytical solution:
    # E_e² = TWO_PI_HC² × [(n_a_e/L_a)² + (n_b_e/L_b)²]
    # L_a = n_a_e × TWO_PI_HC / √(E_e² - (n_b_e × TWO_PI_HC / L_b)²)
    na_e, nb_e, _ = e_mode
    _, nb_p, nc_p = p_mode

    # Electron: E_e² = TWO_PI_HC² [(na/La)² + (nb/Lb)²]
    term_e = (M_E_MEV / TWO_PI_HC)**2 - (nb_e / L_b)**2
    if term_e <= 0:
        return None, None
    L_a = na_e / math.sqrt(term_e) if na_e > 0 else 1e10

    # Proton: E_p² = TWO_PI_HC² [(nb/Lb)² + (nc/Lc)²]
    term_p = (M_P_MEV / TWO_PI_HC)**2 - (nb_p / L_b)**2
    if term_p <= 0:
        return L_a, None
    L_c = nc_p / math.sqrt(term_p)

    # If shears are nonzero, refine numerically
    if abs(s_ab) > 1e-10 or abs(s_bc) > 1e-10 or abs(s_ac) > 1e-10:
        try:
            L_a = brentq(lambda la: t3_energy(e_mode,
                         *t3_metric(la, L_b, L_c, s_ab, s_bc, s_ac)[1:])
                         - M_E_MEV, L_a * 0.5, L_a * 2.0)
            L_c = brentq(lambda lc: t3_energy(p_mode,
                         *t3_metric(L_a, L_b, lc, s_ab, s_bc, s_ac)[1:])
                         - M_P_MEV, L_c * 0.5, L_c * 2.0)
        except (ValueError, RuntimeError):
            pass

    return L_a, L_c


def find_nearest_t3(target_mass, target_charge, target_spin,
                     Gti, L, n_max=15):
    """Find nearest T³ mode matching charge and spin."""
    best = None
    best_err = float('inf')

    for na in range(-n_max, n_max + 1):
        for nc in range(-n_max, n_max + 1):
            if -na + nc != target_charge:
                continue
            spin = (abs(na) % 2) + (abs(nc) % 2)
            if spin != target_spin:
                continue
            for nb in range(-n_max, n_max + 1):
                n = np.array([na, nb, nc], dtype=float)
                E = t3_energy(n, Gti, L)
                err = abs(E - target_mass)
                if err < best_err:
                    best_err = err
                    best = {'n': (na, nb, nc), 'E': E,
                            'gap': target_mass - E,
                            'pct': (target_mass - E) / target_mass * 100}
    return best


# ══════════════════════════════════════════════════════════════════
#  Particle catalog
# ══════════════════════════════════════════════════════════════════

PARTICLES = [
    ("e⁻",   0.511,    -1, 1, "electron"),
    ("p",    938.272,   +1, 1, "proton"),
    ("n",    939.565,    0, 1, "neutron"),
    ("μ⁻",   105.658,  -1, 1, "muon"),
    ("π⁺",   139.570,  +1, 0, "charged pion"),
    ("π⁰",   134.977,   0, 0, "neutral pion"),
    ("K⁺",   493.677,  +1, 0, "charged kaon"),
    ("K⁰",   497.611,   0, 0, "neutral kaon"),
    ("η",    547.862,   0, 0, "eta meson"),
    ("η′",   957.78,    0, 0, "eta prime"),
    ("φ",   1019.461,   0, 2, "phi meson"),
    ("Λ",   1115.683,   0, 1, "lambda baryon"),
    ("Σ⁺",  1189.37,   +1, 1, "sigma plus"),
]


# ══════════════════════════════════════════════════════════════════
#  Main computation
# ══════════════════════════════════════════════════════════════════

print("=" * 72)
print("R30 TRACK 6: SHARED-DIMENSION T³")
print("=" * 72)


# ── Section 1: Diagonal T³ (no shear) ───────────────────────────

print("\n\n── Section 1: Diagonal T³ at several L_b values ──\n")
print("  Electron mode: (1, 2, 0)  →  Q = -1, spin = 1 (½)")
print("  Proton mode:   (0, 1, 1)  →  Q = +1, spin = 1 (½)")
print()

# Minimum L_b: electron mode (1,2,0) needs 2/L_b < E_e/(2πℏc)
# → L_b > 2 × 2πℏc / E_e = 2 × 1239.8 / 0.511 ≈ 4854 fm
L_B_VALUES = [4900, 5000, 6000, 8000, 10000, 20000]

for L_b in L_B_VALUES:
    L_a, L_c = t3_circumferences(L_b)
    if L_a is None or L_c is None:
        print(f"  L_b = {L_b}: no solution")
        continue
    _, Gti, L = t3_metric(L_a, L_b, L_c)
    E_e = t3_energy([1, 2, 0], Gti, L)
    E_p = t3_energy([0, 1, 1], Gti, L)

    # Neutron: (1, n_b, 1), Q=0, spin=2 (PROBLEM!)
    n_best = find_nearest_t3(M_N_MEV, 0, 2, Gti, L, n_max=600)
    # Also try spin=1 to show no match
    n_spin1 = find_nearest_t3(M_N_MEV, 0, 1, Gti, L, n_max=600)

    print(f"  L_b = {L_b} fm:")
    print(f"    L_a = {L_a:.1f} fm,  L_c = {L_c:.4f} fm")
    print(f"    e⁻: E = {E_e:.4f} MeV (target {M_E_MEV:.4f})")
    print(f"    p:  E = {E_p:.3f} MeV (target {M_P_MEV:.3f})")
    if n_best:
        print(f"    n (spin 0/1): mode {n_best['n']}, E = {n_best['E']:.3f} MeV"
              f" (gap = {n_best['pct']:+.3f}%)")
    if n_spin1:
        print(f"    n (spin ½):   mode {n_spin1['n']}, E = {n_spin1['E']:.3f} MeV"
              f" (gap = {n_spin1['pct']:+.3f}%)")
    else:
        print(f"    n (spin ½):   NO MODE WITH Q=0, SPIN=1")
    print()


# ── Section 2: THE SPIN PROBLEM ──────────────────────────────────

print("\n── Section 2: The spin problem for neutral particles ──\n")

print("  In T³ with Q = -n_a + n_c:")
print("    Q = 0  requires  n_a = n_c")
print("    Same n_a, n_c → same parity → spin count always 0 or 2")
print("    Spin ½ (count = 1) requires one odd, one even")
print("    But n_a = n_c forces BOTH odd or BOTH even")
print()
print("  STRUCTURAL IMPOSSIBILITY: no Q=0, spin-½ mode exists in T³")
print("  with this charge formula.")
print()
print("  Affected particles: neutron, Λ, K⁰, π⁰, η, η′")
print("  (any neutral particle with spin ½ or where spin ½ is needed)")
print()
print("  In Ma, the neutron gets spin ½ from the NEUTRINO tube (n₃=1).")
print("  This third tube dimension is the structural escape hatch.")
print()

# Verify exhaustively
print("  Exhaustive check — all (n_a, n_c) with Q=0, |n| ≤ 5:")
print(f"    {'(n_a, n_c)':>12s}  {'Q':>3s}  {'spin_count':>10s}  {'spin':>6s}")
for na in range(-5, 6):
    nc = na
    Q = -na + nc
    spin = (abs(na) % 2) + (abs(nc) % 2)
    if na >= 0:
        spin_label = {0: '0', 1: '½', 2: '0 or 1', 3: '3/2'}[spin]
        print(f"    ({na:+2d}, {nc:+2d})      {Q:+2d}  {spin:>10d}  {spin_label:>6s}")


# ── Section 3: Alternative charge formulas ───────────────────────

print("\n\n── Section 3: Can an alternative charge formula save T³? ──\n")

# What if B contributes to charge?
print("  Option 1: Q = -n_a + n_b + n_c")
print("    Q=0: n_a = n_b + n_c (not n_a = n_c)")
print("    e.g., (1, 2, -1): Q = -1+2-1 = 0, spin(1,_,-1) = 1+1 = 2")
print("    e.g., (1, 0, -1): Q = -1+0+1 = 0?  No: -1+0-1 = -2")
print()
print("  This doesn't help: if B contributes to charge, the electron")
print("  mode (1,2,0) would have Q = -1+2+0 = +1, not -1.")
print()

print("  Option 2: Q = -n_a + n_c (keep), but redefine spin")
print("    If only dimension A contributes to spin:")
print("    spin = |n_a| % 2")
print("    Then neutron (1,n,1): spin = 1 → ½  ✓")
print("    But proton (0,1,1): spin = 0 → 0   ✗ (need ½)")
print()

print("  Option 3: Q = -n_a + n_c (keep), spin from A only when")
print("    n_a ≠ 0, spin from C only when n_c ≠ 0")
print("    This is ad hoc and breaks the clean Ma structure.")
print()

print("  Option 4: Add a fourth dimension (neutrino tube)")
print("    T⁴ = (A, B, C, D) where D is the neutrino tube")
print("    D provides the odd winding for neutral spin-½ particles")
print("    This is T³ × T¹ — 4 material dimensions instead of 6.")
print("    Spin = (|n_a| % 2) + (|n_d| % 2) + (|n_c| % 2)")
print("    Neutron: (0, n_b, 0, 1): Q = 0+0 = 0, spin = 0+1+0 = 1 → ½  ✓")
print("    But this mode has no n_c winding → energy only from B and D")
print()


# ── Section 4: Full spectrum comparison at L_b = 2000 ────────────

print("\n── Section 4: Particle spectrum on diagonal T³ (L_b = 5000) ──\n")

L_b = 5000.0
L_a, L_c = t3_circumferences(L_b)
_, Gti, L = t3_metric(L_a, L_b, L_c)

if L_a is None or L_c is None:
    print("  ERROR: no T³ solution at this L_b")
else:
    _, Gti, L = t3_metric(L_a, L_b, L_c)

    print(f"  L_a = {L_a:.1f} fm,  L_b = {L_b:.0f} fm,  L_c = {L_c:.4f} fm")
    print(f"  (cf. Ma: L₁ = 32209 fm, L₂ = 4880 fm, L₅ = 23.7 fm, L₆ = 2.66 fm)")
    print()
    print(f"  {'Particle':>8s} {'Mass':>8s} {'Q':>3s} {'S':>3s}"
          f" {'Mode':>14s} {'E_mode':>10s} {'Gap':>8s} {'Spin OK':>8s}")
    print(f"  {'─'*62}")

    for name, mass, Q, spin, desc in PARTICLES:
        m = find_nearest_t3(mass, Q, spin, Gti, L, n_max=30)
        if m is None:
            print(f"  {name:>8s} {mass:8.1f} {Q:+2d} {spin:>3d}  {'NO SPIN MATCH':>14s}")
            continue
        gap_str = f"{m['pct']:+.1f}%"
        spin_ok = "✓" if t3_spin(m['n']) == spin else "✗"
        print(f"  {name:>8s} {mass:8.1f} {Q:+2d} {spin:>3d}"
              f"  {str(m['n']):>14s} {m['E']:10.1f} {gap_str:>8s} {spin_ok:>8s}")


# ── Section 5: Spin-relaxed search ───────────────────────────────

print("\n\n── Section 5: Best mass matches ignoring spin ──\n")

L_b = 5000.0
L_a, L_c = t3_circumferences(L_b)
_, Gti, L = t3_metric(L_a, L_b, L_c)

print(f"  {'Particle':>8s} {'Mass':>8s} {'Q':>3s} {'Need S':>6s}"
      f" {'Mode':>14s} {'E_mode':>10s} {'Gap':>8s} {'Got S':>6s} {'Spin OK':>8s}")
print(f"  {'─'*72}")

for name, mass, Q, spin, desc in PARTICLES:
    # Search all spins
    best = None
    best_err = float('inf')
    for na in range(-30, 31):
        for nc in range(-30, 31):
            if -na + nc != Q:
                continue
            for nb in range(-30, 31):
                n = np.array([na, nb, nc], dtype=float)
                E = t3_energy(n, Gti, L)
                err = abs(E - mass)
                if err < best_err:
                    best_err = err
                    best = {'n': (na, nb, nc), 'E': E}

    if best is None:
        print(f"  {name:>8s} {mass:8.1f} {Q:+2d} {spin:>6d}  NO MODE")
        continue
    gap_pct = (mass - best['E']) / mass * 100
    got_spin = t3_spin(best['n'])
    spin_ok = "✓" if got_spin == spin else "✗"
    print(f"  {name:>8s} {mass:8.1f} {Q:+2d} {spin:>6d}"
          f"  {str(best['n']):>14s} {best['E']:10.1f} {gap_pct:+7.1f}% {got_spin:>6d} {spin_ok:>8s}")


# ── Section 6: Ghost mode count comparison ───────────────────────

print("\n\n── Section 6: Ghost mode count — T³ vs Ma ──\n")

# Count T³ modes below 2 GeV
t3_modes = set()
for na in range(-15, 16):
    for nc in range(-15, 16):
        Q = -na + nc
        if abs(Q) > 2:
            continue
        for nb in range(-15, 16):
            n = np.array([na, nb, nc], dtype=float)
            E = t3_energy(n, Gti, L)
            if E < 2000 and E > 0:
                t3_modes.add((round(E, 1), Q, t3_spin(n)))

print(f"  T³ modes below 2 GeV (|Q| ≤ 2, n_max=15): {len(t3_modes)}")
print(f"  Ma modes below 2 GeV (R28 Track 2):       ~29,000 (raw)")
print(f"  Ma modes below 2 GeV (degenerate removed): ~900")
print()

# Cluster by energy
energies_t3 = sorted(set(e for e, q, s in t3_modes))
bands_t3 = []
for E in energies_t3:
    placed = False
    for b in bands_t3:
        if abs(E - b[0]) < 2.0:
            b.append(E)
            placed = True
            break
    if not placed:
        bands_t3.append([E])

print(f"  T³ energy bands below 2 GeV: {len(bands_t3)}")
print(f"  Ma energy bands below 2 GeV: ~48")
print()
print(f"  T³/Ma mode ratio: {len(t3_modes)/900:.1f}× "
      f"({'fewer' if len(t3_modes) < 900 else 'more'} ghosts)")


# ── Section 7: Comparison to Ma ─────────────────────────────────

print("\n\n── Section 7: Ma reference (for comparison) ──\n")

sc = self_consistent_metric(6.6, 5.0, 8.906, sigma_ep=-0.09064)
Gti6 = sc['Gtilde_inv']
L6 = sc['L']

from lib.ma import mode_energy as ma_energy, mode_charge as ma_charge, mode_spin as ma_spin

t6_particles = [
    ("e⁻",   0.511,    -1, 1, (1, 2, 0, 0, 0, 0)),
    ("p",    938.272,   +1, 1, (0, 0, 0, 0, 1, 2)),
    ("n",    939.565,    0, 1, (0, -2, 1, 0, 0, 2)),
    ("μ⁻",   105.658,  -1, 1, None),
    ("π⁺",   139.570,  +1, 0, None),
    ("K⁺",   493.677,  +1, 0, None),
]

print(f"  {'Particle':>8s} {'Ma gap':>10s} {'T³ gap (mass)':>14s} {'T³ spin':>10s}")
print(f"  {'─'*46}")

for name, mass, Q, spin, t6_mode in t6_particles:
    # Ma gap
    if t6_mode:
        E6 = ma_energy(t6_mode, Gti6, L6)
        gap6 = abs(mass - E6) / mass * 100
    else:
        gap6 = None

    # T³ gap (best mass, any spin)
    best3 = None
    best3_err = float('inf')
    for na in range(-30, 31):
        for nc in range(-30, 31):
            if -na + nc != Q:
                continue
            for nb in range(-30, 31):
                n = np.array([na, nb, nc], dtype=float)
                E = t3_energy(n, Gti, L)
                err = abs(E - mass)
                if err < best3_err:
                    best3_err = err
                    best3 = {'n': (na, nb, nc), 'E': E}

    gap3 = abs(mass - best3['E']) / mass * 100 if best3 else None
    spin3 = t3_spin(best3['n']) if best3 else None
    spin_ok = "✓" if spin3 == spin else f"✗ (got {spin3})"

    g6_str = f"{gap6:.2f}%" if gap6 is not None else "—"
    g3_str = f"{gap3:.2f}%" if gap3 is not None else "—"
    print(f"  {name:>8s} {g6_str:>10s} {g3_str:>14s} {spin_ok:>10s}")


# ── Summary ──────────────────────────────────────────────────────

print("\n\n── Summary ──\n")
print("  1. T³ with shared dimension CAN reproduce electron, proton,")
print("     and neutron MASSES to high accuracy.")
print()
print("  2. SPIN BREAKS: Q = 0 requires n_a = n_c → same parity →")
print("     spin count always 0 or 2, never 1.  No spin-½ neutral")
print("     particle exists in T³.  The NEUTRON cannot have spin ½.")
print()
print("  3. In Ma, the neutrino tube (dim 3) provides the odd winding")
print("     for neutral spin-½ particles.  This is a STRUCTURAL")
print("     necessity — not just parametric convenience.")
print()
print("  4. T³ needs at least one more 'tube' dimension to escape")
print("     the spin constraint.  The minimal extension is T⁴")
print("     (= T³ × T¹) with a neutrino tube dimension.")
print()
print("  5. Conclusion: the neutrino material dimension is structurally")
print("     required for the neutron's spin.  The electron-proton")
print("     surface CAN be shared (T³), but the neutrino dimension")
print("     cannot be eliminated.  Minimum: T⁴ = 4 material dimensions.")
