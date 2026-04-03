"""
Track 4: Slot geometry and anomalous moment

Computes the slot dimensions (elliptical aperture) needed to produce
the observed anomalous magnetic moment α/(2π), then sweeps the
height/width ratio to minimize charge perturbation.

Physics model:
  - Scalar Sturm-Liouville eigensolver (same as Torus Lab) gives
    the tube profile f(θ₁) for each mode
  - 4 elliptical slots on the inner equator (θ₁ = 180°), equally
    spaced at shear-corrected intervals
  - Moment enhancement ∝ slot area × field intensity at slot
  - Charge leakage ∝ integral of f(θ₁) × metric over slot area
"""

import math
import numpy as np
import os

# ── Constants ─────────────────────────────────────────────────────
PI  = math.pi
TAU = 2 * PI
ALPHA = 7.2973525693e-3
HBAR  = 1.054571817e-34
C     = 299792458.0
M_E   = 9.1093837015e-31
E_CHARGE = 1.602176634e-19

NFOURIER = 16
DENSITY_N = 256

# ── Eigensolver (ported from torus-lab.html) ──────────────────────

def solve_eigenmodes(eps, qeff, parity):
    """Fourier-Galerkin eigensolver for the Sturm-Liouville problem
    on a torus tube cross-section.

    Returns (eigenvalues, eigenvectors) sorted by ascending eigenvalue.

    The equation is:
      -d/dθ₁ [p(θ₁) df/dθ₁] + V(θ₁)f = λ w(θ₁)f
    where p(θ₁) = 1 + ε cos θ₁,  V = ε²q²/(1 + ε cos θ₁),
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

    # Generalized eigenvalue problem H v = λ M v via Cholesky
    L = np.linalg.cholesky(M)
    Linv = np.linalg.inv(L)
    A = Linv @ H @ Linv.T

    eigenvalues, V = np.linalg.eigh(A)

    # Transform back: eigenvectors in original basis
    evecs = []
    for idx in range(dim):
        u = V[:, idx]
        v = np.linalg.solve(L.T, u)
        evecs.append(v)

    return eigenvalues, evecs


def eval_density(coeffs, parity, n_samples):
    """Evaluate |f(θ₁)|² on a uniform grid, normalized to max=1."""
    is_even = (parity == 'even')
    out = np.zeros(n_samples)
    for i in range(n_samples):
        th = (i / n_samples) * TAU
        f = 0.0
        if is_even:
            for n, c in enumerate(coeffs):
                f += c * (1.0 if n == 0 else math.cos(n * th))
        else:
            for n, c in enumerate(coeffs):
                f += c * math.sin((n + 1) * th)
        out[i] = f * f
    mx = out.max()
    if mx > 0:
        out /= mx
    return out


def eval_f(coeffs, parity, theta):
    """Evaluate f(θ₁) at a single angle (radians)."""
    f = 0.0
    if parity == 'even':
        for n, c in enumerate(coeffs):
            f += c * (1.0 if n == 0 else math.cos(n * theta))
    else:
        for n, c in enumerate(coeffs):
            f += c * math.sin((n + 1) * theta)
    return f


def charge_overlap(coeffs, parity, eps):
    """Charge overlap integral C = ∫f·cosθ₁·(1+ε cosθ₁) dθ₁ / √(∫f²·w dθ₁)."""
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

def alpha_formula(eps, s):
    q = 2 - s
    if q <= 0:
        return 0
    sn = math.sin(TAU * s)
    if abs(sn) < 1e-15:
        return 0
    mu = math.sqrt(1 / (eps * eps) + q * q)
    return mu * sn * sn / (4 * PI * q * q)


def solve_shear(eps, target=ALPHA):
    lo, hi = 0.001, 0.499
    for _ in range(80):
        mid = (lo + hi) / 2
        if alpha_formula(eps, mid) > target:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def mode_mu(eps, qeff):
    return math.sqrt(1 / (eps * eps) + qeff * qeff)


# ── Mode sweep ────────────────────────────────────────────────────

def sweep_modes(eps, shear):
    """Sweep all resonant modes, return list of mode dicts."""
    modes = []
    for n2 in range(1, 7):
        for n1 in range(0, 4):
            for parity in ['even', 'odd']:
                if parity == 'odd' and n1 == 0:
                    continue
                qeff = n2 - shear * n1
                if qeff <= 0.01:
                    continue
                evals, evecs = solve_eigenmodes(eps, qeff, parity)
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


# ── Slot model ────────────────────────────────────────────────────

def slot_positions(eps, shear, n_slots=4):
    """Compute shear-adjusted θ₂ positions for equally spaced slots.

    Slots are placed at electron's standing-wave nodes:
      θ₂_k = k × 180° / q_eff_electron  (in degrees)
    """
    qeff_e = 2 - shear
    spacing = 180.0 / qeff_e
    return [k * spacing for k in range(n_slots)]


def slot_field_integral(coeffs, parity, eps, theta1_center, h_rad):
    """Integrate |f(θ₁)|² × metric weight over a slot centered at theta1_center
    with half-height h_rad (in radians).

    Returns the integral ∫ |f(θ₁)|² (1 + ε cos θ₁) dθ₁ over the slot,
    normalized by the full-circumference integral.
    """
    NQ = 512
    dth = TAU / NQ
    slot_lo = theta1_center - h_rad
    slot_hi = theta1_center + h_rad

    slot_sum = 0.0
    full_sum = 0.0
    for q in range(NQ):
        th = (q + 0.5) * dth
        f = eval_f(coeffs, parity, th)
        w = 1 + eps * math.cos(th)
        val = f * f * w * dth
        full_sum += val
        # Check if this θ₁ falls within the slot
        th_wrapped = th % TAU
        s_lo = slot_lo % TAU
        s_hi = slot_hi % TAU
        if s_lo <= s_hi:
            if s_lo <= th_wrapped <= s_hi:
                slot_sum += val
        else:
            if th_wrapped >= s_lo or th_wrapped <= s_hi:
                slot_sum += val

    return slot_sum / full_sum if full_sum > 0 else 0.0


def compute_field_properties(modes, eps):
    """Pre-compute field properties for each mode (done once)."""
    theta1_center = PI
    props = {}
    for m in modes:
        key = f"({m['n1']},{m['n2']})_{m['parity']}"
        field_frac_fn = lambda h_rad, m=m: slot_field_integral(
            m['coeffs'], m['parity'], eps, theta1_center, h_rad)
        f_at_slot = eval_f(m['coeffs'], m['parity'], PI)
        NQ = 512
        dth = TAU / NQ
        f_rms_sq = 0.0
        for q in range(NQ):
            th = (q + 0.5) * dth
            fv = eval_f(m['coeffs'], m['parity'], th)
            f_rms_sq += fv * fv * dth / TAU
        f_rms = math.sqrt(f_rms_sq)
        d1_idx = int(0.5 * DENSITY_N) % DENSITY_N  # θ₁=180° → idx = N/2
        d1_at_slot = m['density'][d1_idx]
        props[key] = {
            'f_at_slot': f_at_slot,
            'f_rms': f_rms,
            'field_ratio': abs(f_at_slot) / f_rms if f_rms > 0 else 1.0,
            'd1_at_slot': d1_at_slot,
        }
    return props


def compute_survival_for_mode(mode, th2_positions):
    """Product of (1 - ρ_2D) at each non-anchor slot."""
    anchor_th2 = th2_positions[0]
    d1_idx = int(0.5 * DENSITY_N) % DENSITY_N
    d1 = mode['density'][d1_idx]
    s = 1.0
    for k in range(1, len(th2_positions)):
        dt2 = math.radians(th2_positions[k] - anchor_th2)
        d = d1 * math.sin(mode['qeff'] * dt2) ** 2
        s *= (1 - d)
    return s


def compute_slot_analysis(eps, shear, h_deg, w_deg, modes, field_props,
                          n_slots=4):
    """For an elliptical slot of half-axes h_deg × w_deg (in degrees),
    compute moment enhancement and charge leakage fraction.

    modes and field_props are pre-computed (passed in).
    """
    h_rad = math.radians(h_deg)
    w_rad = math.radians(w_deg)

    slot_area_frac = PI * h_rad * w_rad * (1 - eps) / (4 * PI * PI * eps)
    total_slot_area_frac = n_slots * slot_area_frac

    e_mode = next((m for m in modes if m['n1'] == 1 and m['n2'] == 2 and m['parity'] == 'even'), None)
    g_mode = next((m for m in modes if m['n1'] == 1 and m['n2'] == 1 and m['parity'] == 'even'), None)

    if not e_mode or not g_mode:
        return None

    e_key = f"({e_mode['n1']},{e_mode['n2']})_even"
    e_props = field_props[e_key]

    e_field_frac = slot_field_integral(e_mode['coeffs'], 'even', eps, PI, h_rad)

    moment_enhancement = total_slot_area_frac * e_props['field_ratio']
    charge_leak_frac = n_slots * e_field_frac * (PI * h_rad * w_rad) / TAU

    th2_positions = slot_positions(eps, shear, n_slots)

    results = {
        'eps': eps, 'shear': shear,
        'h_deg': h_deg, 'w_deg': w_deg, 'n_slots': n_slots,
        'slot_area_frac': slot_area_frac,
        'total_slot_area_frac': total_slot_area_frac,
        'moment_enhancement': moment_enhancement,
        'charge_leak_frac': charge_leak_frac,
        'field_ratio_at_slot': e_props['field_ratio'],
        'e_survival': compute_survival_for_mode(e_mode, th2_positions),
        'g_survival': compute_survival_for_mode(g_mode, th2_positions),
        'th2_positions': th2_positions,
    }

    charged_modes = [m for m in modes if m['n1'] == 1 and m['parity'] == 'even']
    results['mode_survival'] = {}
    for m in charged_modes:
        label = f"({m['n1']},{m['n2']})"
        results['mode_survival'][label] = compute_survival_for_mode(m, th2_positions)

    return results


# ── SVG generation ────────────────────────────────────────────────

def svg_line_plot(data_series, x_label, y_label, title, width=600, height=350):
    """Generate an SVG line plot from data series.

    data_series: list of dicts with 'x', 'y' (arrays), 'color', 'label'
    """
    margin = {'l': 65, 'r': 20, 't': 35, 'b': 45}
    pw = width - margin['l'] - margin['r']
    ph = height - margin['t'] - margin['b']

    all_x = np.concatenate([s['x'] for s in data_series])
    all_y = np.concatenate([s['y'] for s in data_series])
    x_min, x_max = all_x.min(), all_x.max()
    y_min, y_max = all_y.min(), all_y.max()
    y_pad = (y_max - y_min) * 0.1 or 0.01
    y_min -= y_pad
    y_max += y_pad

    def sx(x):
        return margin['l'] + (x - x_min) / (x_max - x_min) * pw if x_max != x_min else margin['l'] + pw / 2
    def sy(y):
        return margin['t'] + ph - (y - y_min) / (y_max - y_min) * ph if y_max != y_min else margin['t'] + ph / 2

    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             f'style="background:#0a0a14;font-family:monospace">']

    # Grid
    for i in range(5):
        yv = y_min + (y_max - y_min) * i / 4
        y_px = sy(yv)
        lines.append(f'<line x1="{margin["l"]}" y1="{y_px:.1f}" x2="{margin["l"]+pw}" y2="{y_px:.1f}" '
                     f'stroke="#222" stroke-width="0.5"/>')
        lines.append(f'<text x="{margin["l"]-5}" y="{y_px+4:.1f}" fill="#999" font-size="10" '
                     f'text-anchor="end">{yv:.4f}</text>')

    # Data
    for series in data_series:
        pts = ' '.join(f'{sx(x):.1f},{sy(y):.1f}' for x, y in zip(series['x'], series['y']))
        lines.append(f'<polyline points="{pts}" fill="none" stroke="{series["color"]}" '
                     f'stroke-width="2" opacity="0.9"/>')

    # Axes
    lines.append(f'<line x1="{margin["l"]}" y1="{margin["t"]}" x2="{margin["l"]}" '
                 f'y2="{margin["t"]+ph}" stroke="#555" stroke-width="1"/>')
    lines.append(f'<line x1="{margin["l"]}" y1="{margin["t"]+ph}" x2="{margin["l"]+pw}" '
                 f'y2="{margin["t"]+ph}" stroke="#555" stroke-width="1"/>')

    # Labels
    lines.append(f'<text x="{margin["l"]+pw/2}" y="{height-5}" fill="#aaa" font-size="12" '
                 f'text-anchor="middle">{x_label}</text>')
    lines.append(f'<text x="12" y="{margin["t"]+ph/2}" fill="#aaa" font-size="12" '
                 f'text-anchor="middle" transform="rotate(-90,12,{margin["t"]+ph/2})">{y_label}</text>')
    lines.append(f'<text x="{margin["l"]+pw/2}" y="{margin["t"]-10}" fill="#ccc" font-size="14" '
                 f'text-anchor="middle">{title}</text>')

    # Legend
    ly = margin['t'] + 15
    for series in data_series:
        lines.append(f'<line x1="{margin["l"]+pw-120}" y1="{ly}" x2="{margin["l"]+pw-105}" '
                     f'y2="{ly}" stroke="{series["color"]}" stroke-width="2"/>')
        lines.append(f'<text x="{margin["l"]+pw-100}" y="{ly+4}" fill="#bbb" font-size="10">'
                     f'{series["label"]}</text>')
        ly += 16

    # Target line for anomalous moment
    target = ALPHA / (2 * PI)
    if y_min <= target <= y_max:
        yt = sy(target)
        lines.append(f'<line x1="{margin["l"]}" y1="{yt:.1f}" x2="{margin["l"]+pw}" y2="{yt:.1f}" '
                     f'stroke="#4c4" stroke-width="1" stroke-dasharray="4,3"/>')
        lines.append(f'<text x="{margin["l"]+pw+2}" y="{yt+4:.1f}" fill="#4c4" font-size="9">'
                     f'α/2π</text>')

    lines.append('</svg>')
    return '\n'.join(lines)


# ── Main ──────────────────────────────────────────────────────────

def main():
    eps = 0.5
    shear = solve_shear(eps)
    target_moment = ALPHA / (2 * PI)  # ≈ 1.161e-3

    print(f"Track 4: Slot geometry analysis")
    print(f"{'='*55}")
    print(f"  ε = {eps}")
    print(f"  shear s = {shear:.6f}")
    print(f"  α = 1/{1/alpha_formula(eps, shear):.3f}")
    print(f"  target δμ/μ = α/(2π) = {target_moment:.6e}")
    print()

    # Step 1: Compute modes ONCE
    print("Step 1: Computing eigenmodes (once)...")
    modes = sweep_modes(eps, shear)
    field_props = compute_field_properties(modes, eps)
    print(f"  {len(modes)} modes computed")
    print()

    # Step 2: Compute slot positions
    positions = slot_positions(eps, shear)
    print(f"Slot positions (shear-adjusted, {len(positions)} slots):")
    for k, p in enumerate(positions):
        print(f"  slot {k}: θ₂ = {p:.2f}°")
    print()

    # Step 3: Find area that gives target moment
    print("Step 3: Scanning slot area vs moment enhancement...")
    baseline = compute_slot_analysis(eps, shear, 1.0, 1.0, modes, field_props,
                                      n_slots=4)
    print(f"  Baseline (h=1°, w=1°): moment enh = {baseline['moment_enhancement']:.6e}")
    print(f"  Field ratio at inner equator: {baseline['field_ratio_at_slot']:.4f}")
    print(f"  Slot area fraction (per slot): {baseline['slot_area_frac']:.6e}")
    print()

    area_frac_needed = target_moment / baseline['field_ratio_at_slot']
    hw_product = area_frac_needed * 4 * PI * PI * eps / (4 * (1 - eps))
    sq_rad = math.sqrt(hw_product / PI)
    sq_deg = math.degrees(sq_rad)
    print(f"  Required total area fraction: {area_frac_needed:.6e}")
    print(f"  For circular slot: h = w = {sq_deg:.4f}°")
    print()

    # Step 4: Sweep h/w ratio at constant area
    print("Step 4: Sweeping h/w ratio at constant slot area...")
    print(f"  Constant hw_product = {hw_product:.6e} rad²")
    print()

    ratios = np.logspace(-1, 1, 30)  # h/w from 0.1 to 10
    moments = []
    charges = []
    e_survivals = []
    g_survivals = []
    h_degs = []
    w_degs = []

    for ratio in ratios:
        h_r = math.sqrt(ratio * hw_product / PI)
        w_r = math.sqrt(hw_product / (PI * ratio))
        h_d = math.degrees(h_r)
        w_d = math.degrees(w_r)
        h_degs.append(h_d)
        w_degs.append(w_d)

        result = compute_slot_analysis(eps, shear, h_d, w_d, modes,
                                        field_props, n_slots=4)
        moments.append(result['moment_enhancement'])
        charges.append(result['charge_leak_frac'])
        e_survivals.append(result['e_survival'])
        g_survivals.append(result['g_survival'])

    # Print summary table
    print(f"  {'h/w':>6} {'h(°)':>8} {'w(°)':>8} {'δμ/μ':>12} {'Q_leak':>12} {'e⁻ surv':>8} {'ghost':>8}")
    print(f"  {'-'*6} {'-'*8} {'-'*8} {'-'*12} {'-'*12} {'-'*8} {'-'*8}")
    for i in range(0, len(ratios), 3):
        print(f"  {ratios[i]:6.2f} {h_degs[i]:8.4f} {w_degs[i]:8.4f} "
              f"{moments[i]:12.6e} {charges[i]:12.6e} "
              f"{e_survivals[i]*100:7.1f}% {g_survivals[i]*100:7.1f}%")
    print()

    # Find optimal: min charge leakage
    min_charge_idx = np.argmin(np.abs(charges))
    opt_ratio = ratios[min_charge_idx]
    print(f"Optimal h/w ratio (min charge leakage): {opt_ratio:.3f}")
    print(f"  h = {h_degs[min_charge_idx]:.4f}°, w = {w_degs[min_charge_idx]:.4f}°")
    print(f"  moment enhancement = {moments[min_charge_idx]:.6e}")
    print(f"  charge leakage = {charges[min_charge_idx]:.6e}")
    print(f"  electron survival = {e_survivals[min_charge_idx]*100:.1f}%")
    print(f"  ghost survival = {g_survivals[min_charge_idx]*100:.1f}%")
    print()

    # Full survival table at optimal
    opt_result = compute_slot_analysis(eps, shear, h_degs[min_charge_idx],
                                       w_degs[min_charge_idx], modes,
                                       field_props, n_slots=4)
    print(f"Mode survival at optimal geometry:")
    for label, surv in sorted(opt_result['mode_survival'].items()):
        status = '✓' if surv > 0.9 else ('✗' if surv < 0.1 else '⚠')
        print(f"  {label}: {surv*100:.1f}% {status}")

    # Step 4: Generate SVG plots
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    os.makedirs(out_dir, exist_ok=True)

    # Plot 1: Moment and charge vs h/w
    svg1 = svg_line_plot(
        [
            {'x': ratios, 'y': np.array(moments), 'color': '#ff6e40', 'label': 'δμ/μ'},
        ],
        'h/w ratio', 'δμ/μ',
        'Moment enhancement vs slot aspect ratio',
    )
    with open(os.path.join(out_dir, 'track4_moment_vs_ratio.svg'), 'w') as f:
        f.write(svg1)

    svg2 = svg_line_plot(
        [
            {'x': ratios, 'y': np.array(charges), 'color': '#4fc3f7', 'label': 'Q_leak frac'},
        ],
        'h/w ratio', 'charge leak frac',
        'Charge leakage vs slot aspect ratio',
    )
    with open(os.path.join(out_dir, 'track4_charge_vs_ratio.svg'), 'w') as f:
        f.write(svg2)

    # Plot 3: Survival vs h/w
    svg3 = svg_line_plot(
        [
            {'x': ratios, 'y': np.array(e_survivals), 'color': '#ff6e40', 'label': 'electron'},
            {'x': ratios, 'y': np.array(g_survivals), 'color': '#fdd835', 'label': 'ghost'},
        ],
        'h/w ratio', 'survival',
        'Mode survival vs slot aspect ratio',
    )
    with open(os.path.join(out_dir, 'track4_survival_vs_ratio.svg'), 'w') as f:
        f.write(svg3)

    print(f"\nSVGs written to {out_dir}/")
    print("  track4_moment_vs_ratio.svg")
    print("  track4_charge_vs_ratio.svg")
    print("  track4_survival_vs_ratio.svg")


if __name__ == '__main__':
    main()
