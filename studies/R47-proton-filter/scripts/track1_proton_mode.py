"""
Track 1: Proton (1,3) mode analysis

Sweeps the aspect ratio ε = a/R, and at each ε:
  1. Solves shear s from α(ε, s) = 1/137.036 with q_eff = 3 − s
  2. Computes all resonant modes via the Sturm-Liouville eigensolver
  3. Places 3 slots at 120° (shear-adjusted) on the inner equator
  4. Computes survival scores for target (1,3) and ghosts (1,1), (1,2)
  5. Computes charge overlap for each mode
  6. Derives absolute dimensions (a, R, area) from the proton mass

Outputs: console summary + SVG plots of survival, shear, charge,
and dimensions vs ε.
"""

import math
import numpy as np
import os

# ── Constants ─────────────────────────────────────────────────────
PI  = math.pi
TAU = 2 * PI
ALPHA = 7.2973525693e-3          # fine structure constant
HBAR  = 1.054571817e-34          # ℏ (J·s)
C     = 299792458.0              # speed of light (m/s)
M_P   = 1.67262192369e-27        # proton mass (kg)
LAMBDA_BAR_P = HBAR / (M_P * C)  # reduced Compton wavelength (m)

NFOURIER = 16
DENSITY_N = 256

# Target mode: proton = (1, 3)
TARGET_N1 = 1
TARGET_N2 = 3


# ── Eigensolver (ported from torus-lab / R46) ────────────────────

def solve_eigenmodes(eps, qeff, parity):
    """Fourier-Galerkin eigensolver for the Sturm-Liouville problem
    on a torus tube cross-section.

    Equation:  -d/dθ₁ [p(θ₁) df/dθ₁] + V(θ₁)f = λ w(θ₁)f
    where p(θ₁) = 1 + ε cos θ₁, V = ε²q²/(1 + ε cos θ₁),
    w(θ₁) = 1 + ε cos θ₁.

    Basis: cos(nθ₁) for even parity, sin(nθ₁) for odd.
    """
    N = NFOURIER
    is_even = (parity == 'even')
    dim = N + 1 if is_even else N
    NQ = 512
    dth = TAU / NQ

    H = np.zeros((dim, dim))
    M = np.zeros((dim, dim))

    for q in range(NQ):
        th = (q + 0.5) * dth
        ct = math.cos(th)
        p = 1 + eps * ct
        pot = eps * eps * qeff * qeff / p
        w = p

        phi = np.zeros(dim)
        dphi = np.zeros(dim)

        if is_even:
            for n in range(N + 1):
                phi[n] = 1.0 if n == 0 else math.cos(n * th)
                dphi[n] = 0.0 if n == 0 else -n * math.sin(n * th)
        else:
            for n in range(N):
                phi[n] = math.sin((n + 1) * th)
                dphi[n] = (n + 1) * math.cos((n + 1) * th)

        for i in range(dim):
            for j in range(i, dim):
                hij = (p * dphi[i] * dphi[j] + pot * phi[i] * phi[j]) * dth
                mij = (w * phi[i] * phi[j]) * dth
                H[i, j] += hij
                M[i, j] += mij
                if j != i:
                    H[j, i] += hij
                    M[j, i] += mij

    L = np.linalg.cholesky(M)
    Linv = np.linalg.inv(L)
    A = Linv @ H @ Linv.T
    eigenvalues, V = np.linalg.eigh(A)

    evecs = []
    for idx in range(dim):
        u = V[:, idx]
        v = np.linalg.solve(L.T, u)
        evecs.append(v)

    return eigenvalues, evecs


def eval_f(coeffs, parity, theta):
    """Evaluate f(θ₁) at a single angle."""
    f = 0.0
    if parity == 'even':
        for n, c in enumerate(coeffs):
            f += c * (1.0 if n == 0 else math.cos(n * theta))
    else:
        for n, c in enumerate(coeffs):
            f += c * math.sin((n + 1) * theta)
    return f


def eval_density(coeffs, parity, n_samples):
    """Evaluate |f(θ₁)|² on a uniform grid, normalized to max=1."""
    is_even = (parity == 'even')
    out = np.zeros(n_samples)
    for i in range(n_samples):
        th = (i / n_samples) * TAU
        f = eval_f(coeffs, parity, th)
        out[i] = f * f
    mx = out.max()
    if mx > 0:
        out /= mx
    return out


def charge_overlap(coeffs, parity, eps):
    """Charge overlap C = ∫f·cosθ₁·(1+ε cosθ₁) dθ₁ / √(∫f²·w dθ₁)."""
    NQ = 512
    dth = TAU / NQ
    c_val = 0.0
    norm = 0.0
    for q in range(NQ):
        th = (q + 0.5) * dth
        ct = math.cos(th)
        f = eval_f(coeffs, parity, th)
        w = 1 + eps * ct
        c_val += f * ct * w * dth
        norm += f * f * w * dth
    return c_val / math.sqrt(norm) if norm > 0 else 0.0


# ── Physics helpers ───────────────────────────────────────────────

def alpha_formula(eps, s, n2=TARGET_N2):
    """α as a function of ε and shear s, for a (1, n2) target mode."""
    q = n2 - s
    if q <= 0:
        return 0
    sn = math.sin(TAU * s)
    if abs(sn) < 1e-15:
        return 0
    mu = math.sqrt(1.0 / (eps * eps) + q * q)
    return mu * sn * sn / (4 * PI * q * q)


def solve_shear(eps, n2=TARGET_N2, target=ALPHA):
    """Binary search for shear s such that α(ε, s) = target."""
    lo, hi = 0.001, 0.499
    for _ in range(80):
        mid = (lo + hi) / 2
        if alpha_formula(eps, mid, n2) > target:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def mode_mu(eps, qeff):
    """Dimensionless eigenvalue μ = √(1/ε² + q_eff²).
    Matches Torus Lab / R46 convention.
    """
    return math.sqrt(1.0 / (eps * eps) + qeff * qeff)


# ── Mode sweep ────────────────────────────────────────────────────

def sweep_modes(eps, shear):
    """Compute all resonant modes up to n₂=7, n₁=0..4."""
    modes = []
    for n2 in range(1, 8):
        for n1 in range(0, 5):
            for parity in ['even', 'odd']:
                if parity == 'odd' and n1 == 0:
                    continue
                qeff = n2 - shear * n1
                if qeff <= 0.01:
                    continue
                try:
                    evals, evecs = solve_eigenmodes(eps, qeff, parity)
                except np.linalg.LinAlgError:
                    continue
                eig_idx = n1 if parity == 'even' else max(0, n1 - 1)
                if eig_idx >= len(evecs):
                    continue
                coeffs = evecs[eig_idx]
                ev = evals[eig_idx]
                if ev < 0:
                    continue
                density = eval_density(coeffs, parity, DENSITY_N)
                C = charge_overlap(coeffs, parity, eps)
                mu = mode_mu(eps, qeff)
                modes.append({
                    'n1': n1, 'n2': n2, 'parity': parity,
                    'qeff': qeff, 'eigenvalue': ev,
                    'coeffs': coeffs, 'density': density,
                    'chargeOverlap': C, 'mu': mu,
                })
    modes.sort(key=lambda m: m['mu'])
    return modes


# ── Survival computation ─────────────────────────────────────────

def slot_positions_proton(shear, n_slots=3):
    """Shear-adjusted θ₂ positions at the target mode's standing-wave nodes.

    Nodes of sin²(q_eff · θ₂) are at θ₂ = k·180°/q_eff.
    For 3 slots, pick every-other node (k = 0, 2, 4) so the
    target has exactly zero density at each slot.
    """
    qeff = TARGET_N2 - shear * TARGET_N1
    node_spacing = 180.0 / qeff  # degrees between adjacent nodes
    return [(2 * k) * node_spacing for k in range(n_slots)]


def compute_survival(mode, th2_positions):
    """Product of (1 - ρ_2D) at each non-anchor slot."""
    anchor_th2 = th2_positions[0]
    d1_idx = int(0.5 * DENSITY_N) % DENSITY_N  # θ₁ = 180° (inner equator)
    d1 = mode['density'][d1_idx]
    s = 1.0
    for k in range(1, len(th2_positions)):
        dt2 = math.radians(th2_positions[k] - anchor_th2)
        d = d1 * math.sin(mode['qeff'] * dt2) ** 2
        s *= (1 - d)
    return s


# ── Absolute dimensions ──────────────────────────────────────────

def compute_dimensions(eps, shear):
    """Compute absolute tube/ring dimensions from proton mass.

    Returns dict with L_tube, L_ring (circumferences in m),
    a, R (radii in m), area (m²), and all in fm.
    """
    qeff = TARGET_N2 - shear * TARGET_N1
    mu = math.sqrt(1.0 / (eps * eps) + qeff * qeff)
    L_tube = LAMBDA_BAR_P * mu         # tube circumference
    L_ring = L_tube / eps              # ring circumference
    a = L_tube / TAU                   # tube radius
    R = L_ring / TAU                   # ring radius
    area = L_tube * L_ring
    return {
        'mu': mu, 'qeff': qeff,
        'L_tube_m': L_tube, 'L_ring_m': L_ring,
        'a_m': a, 'R_m': R,
        'area_m2': area,
        'L_tube_fm': L_tube * 1e15, 'L_ring_fm': L_ring * 1e15,
        'a_fm': a * 1e15, 'R_fm': R * 1e15,
        'area_fm2': area * 1e30,
    }


# ── SVG generation ────────────────────────────────────────────────

def svg_line_plot(data_series, x_label, y_label, title,
                  width=650, height=350, log_x=False, log_y=False):
    """Generate an SVG line plot."""
    margin = {'l': 75, 'r': 25, 't': 35, 'b': 45}
    pw = width - margin['l'] - margin['r']
    ph = height - margin['t'] - margin['b']

    all_x = np.concatenate([np.array(s['x']) for s in data_series])
    all_y = np.concatenate([np.array(s['y']) for s in data_series])

    if log_x:
        all_x = np.log10(all_x[all_x > 0])
    if log_y:
        all_y = np.log10(all_y[all_y > 0])

    x_min, x_max = all_x.min(), all_x.max()
    y_min, y_max = all_y.min(), all_y.max()
    y_pad = (y_max - y_min) * 0.08 or 0.01
    y_min -= y_pad
    y_max += y_pad

    def sx(x):
        xv = math.log10(x) if log_x else x
        return margin['l'] + (xv - x_min) / (x_max - x_min) * pw if x_max != x_min else margin['l'] + pw / 2

    def sy(y):
        yv = math.log10(y) if log_y else y
        return margin['t'] + ph - (yv - y_min) / (y_max - y_min) * ph if y_max != y_min else margin['t'] + ph / 2

    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             f'style="background:#0a0a14;font-family:monospace">']

    for i in range(5):
        yv_raw = y_min + (y_max - y_min) * i / 4
        y_px = margin['t'] + ph - ph * i / 4
        label = f'{10**yv_raw:.2e}' if log_y else f'{yv_raw:.4g}'
        lines.append(f'<line x1="{margin["l"]}" y1="{y_px:.1f}" x2="{margin["l"]+pw}" y2="{y_px:.1f}" '
                     f'stroke="#222" stroke-width="0.5"/>')
        lines.append(f'<text x="{margin["l"]-5}" y="{y_px+4:.1f}" fill="#999" font-size="10" '
                     f'text-anchor="end">{label}</text>')

    for i in range(5):
        xv_raw = x_min + (x_max - x_min) * i / 4
        x_px = margin['l'] + pw * i / 4
        label = f'{10**xv_raw:.2g}' if log_x else f'{xv_raw:.2g}'
        lines.append(f'<text x="{x_px:.1f}" y="{margin["t"]+ph+15}" fill="#999" font-size="10" '
                     f'text-anchor="middle">{label}</text>')

    for series in data_series:
        pts = []
        xs = np.array(series['x'])
        ys = np.array(series['y'])
        for x, y in zip(xs, ys):
            if log_x and x <= 0:
                continue
            if log_y and y <= 0:
                continue
            pts.append(f'{sx(x):.1f},{sy(y):.1f}')
        if pts:
            dash = f' stroke-dasharray="{series["dash"]}"' if 'dash' in series else ''
            lines.append(f'<polyline points="{" ".join(pts)}" fill="none" '
                         f'stroke="{series["color"]}" stroke-width="2" opacity="0.9"{dash}/>')

    lines.append(f'<line x1="{margin["l"]}" y1="{margin["t"]}" x2="{margin["l"]}" '
                 f'y2="{margin["t"]+ph}" stroke="#555" stroke-width="1"/>')
    lines.append(f'<line x1="{margin["l"]}" y1="{margin["t"]+ph}" x2="{margin["l"]+pw}" '
                 f'y2="{margin["t"]+ph}" stroke="#555" stroke-width="1"/>')

    lines.append(f'<text x="{margin["l"]+pw/2}" y="{height-5}" fill="#aaa" font-size="12" '
                 f'text-anchor="middle">{x_label}</text>')
    lines.append(f'<text x="12" y="{margin["t"]+ph/2}" fill="#aaa" font-size="12" '
                 f'text-anchor="middle" transform="rotate(-90,12,{margin["t"]+ph/2})">{y_label}</text>')
    lines.append(f'<text x="{margin["l"]+pw/2}" y="{margin["t"]-10}" fill="#ccc" font-size="14" '
                 f'text-anchor="middle">{title}</text>')

    ly = margin['t'] + 15
    for series in data_series:
        lines.append(f'<line x1="{margin["l"]+10}" y1="{ly}" x2="{margin["l"]+25}" '
                     f'y2="{ly}" stroke="{series["color"]}" stroke-width="2"/>')
        lines.append(f'<text x="{margin["l"]+30}" y="{ly+4}" fill="#bbb" font-size="10">'
                     f'{series["label"]}</text>')
        ly += 16

    lines.append('</svg>')
    return '\n'.join(lines)


# ── Main ──────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("R47 Track 1: Proton (1,3) mode — ε sweep")
    print("=" * 65)
    print(f"  Target mode: ({TARGET_N1},{TARGET_N2})")
    print(f"  Proton mass: {M_P:.6e} kg")
    print(f"  ƛ_p = ℏ/(m_p c) = {LAMBDA_BAR_P:.6e} m = {LAMBDA_BAR_P*1e15:.4f} fm")
    print(f"  Ghosts to kill: (1,1) and (1,2)")
    print(f"  Slot geometry: 3 slots at 120° spacing")
    print()

    # ε > 1 → self-intersecting spindle torus; weight function goes
    # negative → Cholesky fails.  Physical tori have ε < 1.
    eps_values = np.linspace(0.05, 0.95, 37)

    results = []

    print(f"{'ε':>6} {'shear':>8} {'q_eff':>7} {'α check':>10} "
          f"{'(1,3)%':>7} {'(1,2)%':>7} {'(1,1)%':>7} "
          f"{'C(1,3)':>8} {'a(fm)':>8} {'R(fm)':>8}")
    print("-" * 95)

    for eps in eps_values:
        shear = solve_shear(eps)
        alpha_check = alpha_formula(eps, shear)
        qeff_target = TARGET_N2 - shear * TARGET_N1

        modes = sweep_modes(eps, shear)

        th2_pos = slot_positions_proton(shear)

        target_mode = next((m for m in modes
                            if m['n1'] == TARGET_N1 and m['n2'] == TARGET_N2
                            and m['parity'] == 'even'), None)
        ghost_11 = next((m for m in modes
                         if m['n1'] == 1 and m['n2'] == 1
                         and m['parity'] == 'even'), None)
        ghost_12 = next((m for m in modes
                         if m['n1'] == 1 and m['n2'] == 2
                         and m['parity'] == 'even'), None)

        surv_target = compute_survival(target_mode, th2_pos) if target_mode else 0
        surv_11 = compute_survival(ghost_11, th2_pos) if ghost_11 else 0
        surv_12 = compute_survival(ghost_12, th2_pos) if ghost_12 else 0

        C_target = target_mode['chargeOverlap'] if target_mode else 0

        dims = compute_dimensions(eps, shear)

        charged_modes = [m for m in modes if m['n1'] == 1 and m['parity'] == 'even']
        mode_survivals = {}
        for m in charged_modes:
            label = f"(1,{m['n2']})"
            mode_survivals[label] = compute_survival(m, th2_pos)

        results.append({
            'eps': eps, 'shear': shear, 'qeff': qeff_target,
            'alpha': alpha_check,
            'surv_target': surv_target,
            'surv_11': surv_11, 'surv_12': surv_12,
            'C_target': C_target,
            'dims': dims,
            'mode_survivals': mode_survivals,
        })

        print(f"{eps:6.2f} {shear:8.5f} {qeff_target:7.4f} "
              f"1/{1/alpha_check:.1f}  "
              f"{surv_target*100:6.1f}% {surv_12*100:6.1f}% {surv_11*100:6.1f}% "
              f"{C_target:8.4f} {dims['a_fm']:8.3f} {dims['R_fm']:8.3f}",
              flush=True)

    print()

    # ── Summary analysis ──────────────────────────────────────────
    print("=" * 65)
    print("ANALYSIS")
    print("=" * 65)

    # Find ε range where ghosts are killed and target survives
    viable = [r for r in results
              if r['surv_target'] > 0.5
              and r['surv_11'] < 0.1
              and r['surv_12'] < 0.1]

    if viable:
        print(f"\nViable ε range (target >50%, both ghosts <10%):")
        print(f"  ε = {viable[0]['eps']:.2f} to {viable[-1]['eps']:.2f}")
        print(f"  Best target survival: {max(v['surv_target'] for v in viable)*100:.1f}%")
        best = max(viable, key=lambda r: r['surv_target'])
        print(f"\n  Best point: ε = {best['eps']:.2f}")
        print(f"    shear s = {best['shear']:.5f}")
        print(f"    q_eff = {best['qeff']:.4f}")
        print(f"    (1,3) survival = {best['surv_target']*100:.1f}%")
        print(f"    (1,2) survival = {best['surv_12']*100:.1f}%")
        print(f"    (1,1) survival = {best['surv_11']*100:.1f}%")
        print(f"    charge overlap C = {best['C_target']:.4f}")
        d = best['dims']
        print(f"\n    Absolute dimensions:")
        print(f"      μ = {d['mu']:.4f}")
        print(f"      L_tube = {d['L_tube_fm']:.3f} fm   (a = {d['a_fm']:.3f} fm)")
        print(f"      L_ring = {d['L_ring_fm']:.3f} fm   (R = {d['R_fm']:.3f} fm)")
        print(f"      Area = {d['area_fm2']:.2f} fm²")
    else:
        print("\nNo viable ε found where target >50% and both ghosts <10%.")
        print("Relaxing criteria...")
        relaxed = [r for r in results if r['surv_target'] > 0.3]
        if relaxed:
            best = max(relaxed, key=lambda r: r['surv_target'] - r['surv_11'] - r['surv_12'])
            print(f"  Best separation at ε = {best['eps']:.2f}")
            print(f"    (1,3) = {best['surv_target']*100:.1f}%")
            print(f"    (1,2) = {best['surv_12']*100:.1f}%")
            print(f"    (1,1) = {best['surv_11']*100:.1f}%")

    # Extended mode survival at a few representative ε values
    print("\n\nExtended mode survival at representative ε values:")
    for eps_check in [0.3, 0.5, 1.0, 2.0, 5.0]:
        r = min(results, key=lambda r: abs(r['eps'] - eps_check))
        print(f"\n  ε = {r['eps']:.2f} (s = {r['shear']:.5f}):")
        for label, surv in sorted(r['mode_survivals'].items()):
            status = '✓' if surv > 0.9 else ('✗' if surv < 0.1 else '⚠')
            print(f"    {label}: {surv*100:6.1f}% {status}")
        d = r['dims']
        print(f"    Dimensions: a = {d['a_fm']:.3f} fm, R = {d['R_fm']:.3f} fm")

    # Dimension table
    print("\n\nDimension table (all ε):")
    print(f"{'ε':>6} {'a (fm)':>10} {'R (fm)':>10} {'Area (fm²)':>12} {'L_tube (fm)':>12} {'L_ring (fm)':>12}")
    print("-" * 72)
    for r in results:
        d = r['dims']
        print(f"{r['eps']:6.2f} {d['a_fm']:10.4f} {d['R_fm']:10.4f} "
              f"{d['area_fm2']:12.4f} {d['L_tube_fm']:12.4f} {d['L_ring_fm']:12.4f}")

    # ── SVG plots ─────────────────────────────────────────────────
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    os.makedirs(out_dir, exist_ok=True)

    eps_arr = np.array([r['eps'] for r in results])

    # Plot 1: Survival vs ε
    svg1 = svg_line_plot(
        [
            {'x': eps_arr, 'y': np.array([r['surv_target'] for r in results]),
             'color': '#4fc3f7', 'label': '(1,3) target'},
            {'x': eps_arr, 'y': np.array([r['surv_12'] for r in results]),
             'color': '#ff6e40', 'label': '(1,2) ghost'},
            {'x': eps_arr, 'y': np.array([r['surv_11'] for r in results]),
             'color': '#fdd835', 'label': '(1,1) ghost'},
        ],
        'ε (aspect ratio a/R)', 'survival',
        'Mode survival vs ε — 3 slots at 120°',
    )
    with open(os.path.join(out_dir, 'track1_survival_vs_eps.svg'), 'w') as f:
        f.write(svg1)

    # Plot 2: Shear vs ε
    svg2 = svg_line_plot(
        [
            {'x': eps_arr, 'y': np.array([r['shear'] for r in results]),
             'color': '#ab47bc', 'label': 'shear s'},
        ],
        'ε', 'shear s',
        'Shear vs ε for α = 1/137 with q = 3−s',
    )
    with open(os.path.join(out_dir, 'track1_shear_vs_eps.svg'), 'w') as f:
        f.write(svg2)

    # Plot 3: Charge overlap vs ε
    svg3 = svg_line_plot(
        [
            {'x': eps_arr, 'y': np.array([r['C_target'] for r in results]),
             'color': '#66bb6a', 'label': 'C(1,3)'},
        ],
        'ε', 'charge overlap C',
        'Charge overlap of (1,3) vs ε',
    )
    with open(os.path.join(out_dir, 'track1_charge_vs_eps.svg'), 'w') as f:
        f.write(svg3)

    # Plot 4: Absolute dimensions vs ε
    svg4 = svg_line_plot(
        [
            {'x': eps_arr, 'y': np.array([r['dims']['a_fm'] for r in results]),
             'color': '#ff6e40', 'label': 'a (tube radius)'},
            {'x': eps_arr, 'y': np.array([r['dims']['R_fm'] for r in results]),
             'color': '#4fc3f7', 'label': 'R (ring radius)'},
        ],
        'ε', 'radius (fm)',
        'Proton sheet dimensions vs ε',
        log_y=True,
    )
    with open(os.path.join(out_dir, 'track1_dimensions_vs_eps.svg'), 'w') as f:
        f.write(svg4)

    print(f"\nSVGs written to {out_dir}/")
    print("  track1_survival_vs_eps.svg")
    print("  track1_shear_vs_eps.svg")
    print("  track1_charge_vs_eps.svg")
    print("  track1_dimensions_vs_eps.svg")


if __name__ == '__main__':
    main()
