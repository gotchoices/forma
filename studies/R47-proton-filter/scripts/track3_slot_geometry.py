"""
Track 3: Proton slot geometry

Determines elliptical slot dimensions for the proton (1,3) mode torus.
Runs two scenarios:
  A) δμ/μ = α/(2π) — same prescription as electron (R46 Track 4)
  B) δμ/μ = κ_p = 1.793 — slots carry the full anomaly (exploratory)

At each scenario, sweeps h/w ratio (slot height / width) to minimize
charge leakage, reports physical dimensions in fm, and verifies that
the slot sizes don't perturb mode survival.

Physics model:
  - Scalar Sturm-Liouville eigensolver (same as Track 1 / Torus Lab)
  - 3 elliptical slots on the inner equator (θ₁ = 180°), placed at
    shear-adjusted 120° intervals (every-other node of the target)
  - Moment enhancement ∝ slot area × field intensity at slot
  - Charge leakage ∝ integral of charge density through aperture
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
M_P   = 1.67262192369e-27
M_E   = 9.1093837015e-31
LAMBDA_BAR_P = HBAR / (M_P * C)

NFOURIER = 16
DENSITY_N = 256

TARGET_N1 = 1
TARGET_N2 = 3
N_SLOTS   = 3

KAPPA_P = 1.7928473446     # proton anomalous magnetic moment


# ── Eigensolver (from Track 1) ────────────────────────────────────

def solve_eigenmodes(eps, qeff, parity):
    """Fourier-Galerkin eigensolver for the Sturm-Liouville problem
    on a torus tube cross-section.

    Equation:  -d/dθ₁ [p(θ₁) df/dθ₁] + V(θ₁)f = λ w(θ₁)f
    where p = 1 + ε cos θ₁, V = ε²q²/(1 + ε cos θ₁), w = p.
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


def charge_overlap(coeffs, parity, eps):
    """C = ∫ f·cos θ₁·(1+ε cos θ₁) dθ₁ / √(∫ f²·w dθ₁)."""
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
    q = n2 - s
    if q <= 0:
        return 0
    sn = math.sin(TAU * s)
    if abs(sn) < 1e-15:
        return 0
    mu = math.sqrt(1.0 / (eps * eps) + q * q)
    return mu * sn * sn / (4 * PI * q * q)


def solve_shear(eps, n2=TARGET_N2, target=ALPHA):
    lo, hi = 0.001, 0.499
    for _ in range(80):
        mid = (lo + hi) / 2
        if alpha_formula(eps, mid, n2) > target:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def mode_mu(eps, qeff):
    return math.sqrt(1.0 / (eps * eps) + qeff * qeff)


# ── Mode sweep ────────────────────────────────────────────────────

def sweep_modes(eps, shear):
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


# ── Slot positions ────────────────────────────────────────────────

def slot_positions_proton(shear):
    """3 slots at every-other node of the (1,3) standing wave.

    Nodes of sin²(q_eff · θ₂) are at θ₂ = k·180°/q_eff.
    Pick k = 0, 2, 4 (every other) → slots at 0°, 360°/q_eff, 720°/q_eff.
    """
    qeff = TARGET_N2 - shear * TARGET_N1
    node_spacing = 180.0 / qeff
    return [(2 * k) * node_spacing for k in range(N_SLOTS)]


# ── Survival ──────────────────────────────────────────────────────

def compute_survival(mode, th2_positions):
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


# ── Absolute dimensions ──────────────────────────────────────────

def compute_dimensions(eps, shear):
    qeff = TARGET_N2 - shear * TARGET_N1
    mu = math.sqrt(1.0 / (eps * eps) + qeff * qeff)
    L_tube = LAMBDA_BAR_P * mu
    L_ring = L_tube / eps
    a = L_tube / TAU
    R = L_ring / TAU
    area = L_tube * L_ring
    return {
        'mu': mu, 'qeff': qeff,
        'L_tube_m': L_tube, 'L_ring_m': L_ring,
        'a_m': a, 'R_m': R, 'area_m2': area,
        'L_tube_fm': L_tube * 1e15, 'L_ring_fm': L_ring * 1e15,
        'a_fm': a * 1e15, 'R_fm': R * 1e15,
        'area_fm2': area * 1e30,
    }


# ── Slot geometry analysis ────────────────────────────────────────

def slot_field_integral(coeffs, parity, eps, theta1_center, h_rad):
    """Fraction of |f(θ₁)|²·w integrated over slot height, relative
    to the full tube circumference.  Used for charge leakage."""
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


def compute_slot_analysis(eps, shear, h_deg, w_deg, modes, n_slots=N_SLOTS):
    """Analyse one slot geometry: moment enhancement, charge leakage,
    and mode survival for all charged modes."""
    h_rad = math.radians(h_deg)
    w_rad = math.radians(w_deg)

    # Slot area as fraction of total torus surface area.
    # Torus area = ∫∫ (1+ε cos θ₁) dθ₁ dθ₂ = (2π)²·1  (for small ε).
    # At the inner equator θ₁=π the local metric factor is (1−ε).
    # Per-slot area fraction ≈ h_rad · w_rad · (1−ε) / (4π²).
    slot_area_frac = h_rad * w_rad * (1 - eps) / (4 * PI * PI)
    total_slot_area_frac = n_slots * slot_area_frac

    target = next((m for m in modes
                   if m['n1'] == TARGET_N1 and m['n2'] == TARGET_N2
                   and m['parity'] == 'even'), None)
    if not target:
        return None

    # Field intensity ratio at inner equator vs RMS
    NQ = 512
    dth = TAU / NQ
    f_at_slot = eval_f(target['coeffs'], 'even', PI)
    f_rms_sq = 0.0
    for q in range(NQ):
        th = (q + 0.5) * dth
        fv = eval_f(target['coeffs'], 'even', th)
        f_rms_sq += fv * fv * dth / TAU
    f_rms = math.sqrt(f_rms_sq)
    field_ratio = abs(f_at_slot) / f_rms if f_rms > 0 else 1.0

    moment_enhancement = total_slot_area_frac * field_ratio

    e_field_frac = slot_field_integral(target['coeffs'], 'even', eps, PI, h_rad)
    charge_leak_frac = n_slots * e_field_frac * (h_rad * w_rad) / TAU

    th2_positions = slot_positions_proton(shear)

    charged_modes = [m for m in modes if m['n1'] == 1 and m['parity'] == 'even']
    mode_survival = {}
    for m in charged_modes:
        label = f"(1,{m['n2']})"
        mode_survival[label] = compute_survival(m, th2_positions)

    return {
        'eps': eps, 'shear': shear,
        'h_deg': h_deg, 'w_deg': w_deg, 'n_slots': n_slots,
        'slot_area_frac': slot_area_frac,
        'total_slot_area_frac': total_slot_area_frac,
        'moment_enhancement': moment_enhancement,
        'charge_leak_frac': charge_leak_frac,
        'field_ratio': field_ratio,
        'mode_survival': mode_survival,
        'th2_positions': th2_positions,
    }


# ── SVG generation ────────────────────────────────────────────────

def svg_line_plot(data_series, x_label, y_label, title,
                  width=650, height=350, log_x=False, log_y=False):
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

    # α/(2π) reference line
    target_a = ALPHA / (2 * PI)
    if not log_y and y_min <= target_a <= y_max:
        yt = sy(target_a)
        lines.append(f'<line x1="{margin["l"]}" y1="{yt:.1f}" x2="{margin["l"]+pw}" y2="{yt:.1f}" '
                     f'stroke="#4c4" stroke-width="1" stroke-dasharray="4,3"/>')
        lines.append(f'<text x="{margin["l"]+pw+2}" y="{yt+4:.1f}" fill="#4c4" font-size="9">'
                     f'α/2π</text>')

    lines.append('</svg>')
    return '\n'.join(lines)


# ── Main ──────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("R47 Track 3: Proton slot geometry")
    print("=" * 70)
    print(f"  Target mode: ({TARGET_N1},{TARGET_N2})")
    print(f"  Slots: {N_SLOTS} at 120° (shear-adjusted)")
    print(f"  Proton mass: {M_P:.6e} kg")
    print(f"  ƛ_p = {LAMBDA_BAR_P*1e15:.4f} fm")
    print(f"  Scenario A target: δμ/μ = α/(2π) = {ALPHA/(2*PI):.6e}")
    print(f"  Scenario B target: δμ/μ = κ_p = {KAPPA_P:.6f}")
    print()

    eps_values = [0.30, 0.50]

    for eps in eps_values:
        shear = solve_shear(eps)
        qeff = TARGET_N2 - shear * TARGET_N1
        dims = compute_dimensions(eps, shear)

        print(f"\n{'─'*70}")
        print(f"  ε = {eps:.2f}")
        print(f"  shear s = {shear:.6f}")
        print(f"  q_eff = {qeff:.4f}")
        print(f"  α check = 1/{1/alpha_formula(eps, shear):.3f}")
        print(f"  μ = {dims['mu']:.4f}")
        print(f"  L_tube = {dims['L_tube_fm']:.3f} fm   (a = {dims['a_fm']:.3f} fm)")
        print(f"  L_ring = {dims['L_ring_fm']:.3f} fm   (R = {dims['R_fm']:.3f} fm)")
        print(f"  Area = {dims['area_fm2']:.4f} fm²")
        print()

        modes = sweep_modes(eps, shear)
        th2_pos = slot_positions_proton(shear)
        print(f"  Slot positions: {', '.join(f'{p:.2f}°' for p in th2_pos)}")
        print(f"  Modes computed: {len(modes)}")
        print()

        # Field intensity at inner equator
        target_mode = next((m for m in modes
                           if m['n1'] == TARGET_N1 and m['n2'] == TARGET_N2
                           and m['parity'] == 'even'), None)
        if not target_mode:
            print("  ERROR: target mode (1,3) not found!")
            continue

        # Baseline: unit-degree slot to calibrate scaling
        baseline = compute_slot_analysis(eps, shear, 1.0, 1.0, modes)
        print(f"  Baseline (h=1°, w=1°):")
        print(f"    moment enhancement = {baseline['moment_enhancement']:.6e}")
        print(f"    field ratio at inner equator = {baseline['field_ratio']:.4f}")
        print(f"    per-slot area fraction = {baseline['slot_area_frac']:.6e}")
        print()

        # For each scenario, find required total slot area
        scenarios = [
            ('A', ALPHA / (2 * PI), 'α/(2π)'),
            ('B', KAPPA_P,          'κ_p'),
        ]

        for label, target_moment, desc in scenarios:
            print(f"  ── Scenario {label}: δμ/μ = {desc} = {target_moment:.6e} ──")

            # Required area fraction: moment_enh = total_area_frac × field_ratio
            # → total_area_frac = target_moment / field_ratio
            area_frac_needed = target_moment / baseline['field_ratio']

            # Per-slot area fraction
            per_slot_frac = area_frac_needed / N_SLOTS

            # Convert to h×w product in radians²:
            #   per_slot_frac = h_rad × w_rad × (1−ε) / (4π²)
            # For ellipse: actual area = π·h_rad·w_rad/4, but the
            # area-fraction formula uses the bounding rectangle h×w.
            # We use the rectangle convention (consistent with R46).
            hw_product = per_slot_frac * 4 * PI * PI / (1 - eps)

            # Check: what fraction of the torus is removed?
            sheet_frac_pct = area_frac_needed * 100

            print(f"    Required total area fraction: {area_frac_needed:.6e} ({sheet_frac_pct:.3f}% of sheet)")
            print(f"    h×w product: {hw_product:.6e} rad²")
            print()

            # Sweep h/w ratio
            ratios = np.logspace(-1, 1, 30)
            moments = []
            charges = []
            h_degs_arr = []
            w_degs_arr = []
            h_fms = []
            w_fms = []

            for ratio in ratios:
                h_r = math.sqrt(ratio * hw_product)
                w_r = math.sqrt(hw_product / ratio)
                h_d = math.degrees(h_r)
                w_d = math.degrees(w_r)
                h_degs_arr.append(h_d)
                w_degs_arr.append(w_d)

                # Physical size in fm
                h_fm = h_r * dims['a_m'] * 1e15
                w_fm = w_r * dims['R_m'] * 1e15
                h_fms.append(h_fm)
                w_fms.append(w_fm)

                result = compute_slot_analysis(eps, shear, h_d, w_d, modes)
                moments.append(result['moment_enhancement'])
                charges.append(result['charge_leak_frac'])

            # Summary table
            print(f"    {'h/w':>6} {'h(°)':>8} {'w(°)':>8} {'h(fm)':>8} {'w(fm)':>8} "
                  f"{'δμ/μ':>12} {'Q_leak':>12}")
            print(f"    {'-'*6} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*12} {'-'*12}")
            for i in range(0, len(ratios), 3):
                print(f"    {ratios[i]:6.2f} {h_degs_arr[i]:8.4f} {w_degs_arr[i]:8.4f} "
                      f"{h_fms[i]:8.3f} {w_fms[i]:8.3f} "
                      f"{moments[i]:12.6e} {charges[i]:12.6e}")
            print()

            # Optimal: min |charge leakage|
            min_idx = np.argmin(np.abs(charges))
            print(f"    Optimal h/w (min charge leakage): {ratios[min_idx]:.3f}")
            print(f"      h = {h_degs_arr[min_idx]:.4f}° ({h_fms[min_idx]:.3f} fm)")
            print(f"      w = {w_degs_arr[min_idx]:.4f}° ({w_fms[min_idx]:.3f} fm)")
            print(f"      δμ/μ = {moments[min_idx]:.6e}")
            print(f"      Q_leak = {charges[min_idx]:.6e}")

            # Check if scenario B slots overlap
            if label == 'B':
                angular_separation = th2_pos[1] - th2_pos[0] if len(th2_pos) > 1 else 360
                slot_width = w_degs_arr[min_idx]
                gap = angular_separation - slot_width
                print(f"      Slot angular separation: {angular_separation:.1f}°")
                print(f"      Slot width: {slot_width:.4f}°")
                print(f"      Gap between slots: {gap:.1f}°")
                if gap < 0:
                    print(f"      ⚠ SLOTS OVERLAP — small-aperture assumption breaks down")

            # Mode survival at optimal
            opt = compute_slot_analysis(eps, shear,
                                        h_degs_arr[min_idx],
                                        w_degs_arr[min_idx], modes)
            print(f"\n    Mode survival at optimal geometry:")
            for mode_label, surv in sorted(opt['mode_survival'].items()):
                status = '✓' if surv > 0.9 else ('✗' if surv < 0.1 else '⚠')
                print(f"      {mode_label}: {surv*100:.1f}% {status}")
            print()

    # ── Comparison with electron (R46) ────────────────────────────
    print(f"\n{'='*70}")
    print("COMPARISON: Electron (R46 Track 4) vs Proton (R47 Track 3)")
    print(f"{'='*70}")
    print()

    # Electron at ε=0.5 for comparison
    e_shear = solve_shear(0.5, n2=2)
    e_qeff = 2 - e_shear
    LAMBDA_BAR_E = HBAR / (M_E * C)
    e_mu = math.sqrt(1.0 / (0.5 * 0.5) + e_qeff * e_qeff)
    e_L_tube = LAMBDA_BAR_E * e_mu
    e_L_ring = e_L_tube / 0.5
    e_a = e_L_tube / TAU
    e_R = e_L_ring / TAU
    e_area = e_L_tube * e_L_ring

    p_dims = compute_dimensions(0.5, solve_shear(0.5))

    print(f"  {'':>20} {'Electron':>14} {'Proton':>14}")
    print(f"  {'':>20} {'-'*14} {'-'*14}")
    print(f"  {'Mode':>20} {'(1,2)':>14} {'(1,3)':>14}")
    print(f"  {'Slots':>20} {'4':>14} {'3':>14}")
    print(f"  {'ε':>20} {'0.50':>14} {'0.50':>14}")
    print(f"  {'q_eff':>20} {e_qeff:14.4f} {p_dims['qeff']:14.4f}")
    print(f"  {'μ':>20} {e_mu:14.4f} {p_dims['mu']:14.4f}")
    print(f"  {'L_tube (fm)':>20} {e_L_tube*1e15:14.3f} {p_dims['L_tube_fm']:14.3f}")
    print(f"  {'L_ring (fm)':>20} {e_L_ring*1e15:14.3f} {p_dims['L_ring_fm']:14.3f}")
    print(f"  {'a (fm)':>20} {e_a*1e15:14.4f} {p_dims['a_fm']:14.4f}")
    print(f"  {'R (fm)':>20} {e_R*1e15:14.4f} {p_dims['R_fm']:14.4f}")
    print(f"  {'Area (fm²)':>20} {e_area*1e30:14.4f} {p_dims['area_fm2']:14.4f}")
    print(f"  {'Mass ratio m_p/m_e':>20} {'':>14} {M_P/M_E:14.2f}")
    print(f"  {'Size ratio (area)':>20} {'':>14} {p_dims['area_fm2']/(e_area*1e30):14.4f}")
    print()

    # ── SVG plots ─────────────────────────────────────────────────
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
    os.makedirs(out_dir, exist_ok=True)

    # Generate charge-leakage plots for each ε (scenario A only)
    for eps in eps_values:
        shear = solve_shear(eps)
        modes = sweep_modes(eps, shear)
        dims = compute_dimensions(eps, shear)

        target_moment = ALPHA / (2 * PI)
        baseline = compute_slot_analysis(eps, shear, 1.0, 1.0, modes)
        area_frac_needed = target_moment / baseline['field_ratio']
        hw_product = (area_frac_needed / N_SLOTS) * 4 * PI * PI / (1 - eps)

        ratios = np.logspace(-1, 1, 30)
        moments_arr = []
        charges_arr = []

        for ratio in ratios:
            h_r = math.sqrt(ratio * hw_product)
            w_r = math.sqrt(hw_product / ratio)
            h_d = math.degrees(h_r)
            w_d = math.degrees(w_r)
            result = compute_slot_analysis(eps, shear, h_d, w_d, modes)
            moments_arr.append(result['moment_enhancement'])
            charges_arr.append(result['charge_leak_frac'])

        eps_tag = f"{eps:.2f}".replace('.', '')

        svg1 = svg_line_plot(
            [{'x': ratios, 'y': np.array(charges_arr),
              'color': '#4fc3f7', 'label': 'Q_leak frac'}],
            'h/w ratio', 'charge leak frac',
            f'Charge leakage vs slot aspect ratio (ε={eps:.2f})',
            log_x=True,
        )
        with open(os.path.join(out_dir, f'track3_charge_vs_ratio_eps{eps_tag}.svg'), 'w') as f:
            f.write(svg1)

        svg2 = svg_line_plot(
            [{'x': ratios, 'y': np.array(moments_arr),
              'color': '#ff6e40', 'label': 'δμ/μ'}],
            'h/w ratio', 'δμ/μ',
            f'Moment enhancement vs slot aspect ratio (ε={eps:.2f})',
            log_x=True,
        )
        with open(os.path.join(out_dir, f'track3_moment_vs_ratio_eps{eps_tag}.svg'), 'w') as f:
            f.write(svg2)

    print(f"SVGs written to {out_dir}/")
    for eps in eps_values:
        eps_tag = f"{eps:.2f}".replace('.', '')
        print(f"  track3_charge_vs_ratio_eps{eps_tag}.svg")
        print(f"  track3_moment_vs_ratio_eps{eps_tag}.svg")


if __name__ == '__main__':
    main()
