"""
k5_mode_sweep.py — Enumerate closure-satisfying modes on the K5 5-torus
manifold and match them to observed particles.

For each winding tuple {n1, n2, n3, n4, n5} with |n_i| <= cutoff:
  - Classify by substrate dimensionality (# of nonzero windings)
  - Apply closure rules per substrate kind:
      1D — n != 0 (no further rule for single-winding modes)
      2D — m_t | m_r per architecture.md §3.3.1, both tube/ring assignments
           tried; sign-flipped m_t admitted per config-neutrino.md §NS.2
      3+D — closure rule open (k5-manifold.md §3.3); admitted via --include-3d
            with a naive Σ(n_i/L_i)² mass formula, flagged in output
  - Compute mass via the 2-torus formula:
        m² = (2πℏc)² · [(m_t/L_t)² + ((m_r - σ_eff·m_t)/L_r)²]
  - Match against an observed-particle catalog within a relative-mass tolerance

Default dim sizes match k5-manifold.md §2.1. Parameters configurable:
dim sizes, winding cutoff, σ_eff (uniform or per-pair), match tolerance,
whether to include 3+D modes.

Inputs:
  --dim-sizes        5 floats (fm) for d1..d5
  --cutoff           max |n_i| (default 3)
  --sigma-eff        uniform σ_eff for 2D modes (default 2.0)
  --sigma-overrides  per-pair σ_eff: 'd1,d3=1.9764;d2,d3=1.9318;d3,d4=1.6837'
  --tolerance        relative-mass match tolerance (default 0.05)
  --include-3d       include 3+-winding modes (naive mass formula)
  --output-dir       output directory (default outputs/k5_mode_sweep)

Outputs:
  spectrum.csv  — all admitted modes sorted by mass
  matches.txt   — observed-particle matches, sorted by particle
  summary.txt   — parameter echo + counts per substrate kind/label

Cross-references:
  work/k5-manifold.md     — framework, §2.1 dim sizes, §3 modes, §4 inventory
  work/architecture.md    — §2 mode tuple, §3.3.1 closure rule
  work/cand-QY-ED.md      — K4 fitted σ_eff values for reproduction:
                              Ma(d1,d3) = 1.9764, Ma(d2,d3) = 1.9318,
                              Ma(d3,d4) = 1.6837 (per config-quark.md §QY.2)
  work/electron-tube.md   — σ_eff = 2 target on lepton sheets
  scripts/torus3d_modes.py — ancestor 3-torus enumerator (different output)
"""

import argparse
import csv
import math
from dataclasses import dataclass
from itertools import product
from pathlib import Path

HBARC_MEV_FM = 197.3269804
TWO_PI_HBARC_MEV_FM = 2 * math.pi * HBARC_MEV_FM

# K5 default dim sizes (fm) per work/k5-manifold.md §2.1
DEFAULT_DIM_SIZES_FM = (
    0.0073,     # d1: b/t spoke (pinned)
    1.0,        # d2: s/c spoke (mid-range)
    200.0,      # d3: quark hub (mid-range)
    2.4e3,      # d4: u/d spoke (electron-host floor)
    4.13e10,    # d5: neutrino circle (~41 µm, per neutrino_1d_fit R=6.578e9 fm)
)

# Observed fundamental particles (name, mass_MeV, spin, charge, note)
# Neutrino masses in MeV: 30 meV = 3e-8 MeV.
OBSERVED_PARTICLES = (
    ('nu1',  3.0e-8,    0.5,  0,    'lightest neutrino (~30 meV, normal ord.)'),
    ('nu2',  3.3e-8,    0.5,  0,    'middle neutrino (~33 meV)'),
    ('nu3',  6.0e-8,    0.5,  0,    'heaviest neutrino (~60 meV, normal ord.)'),
    ('e',    0.5109989, 0.5, -1,    'electron'),
    ('mu',   105.6584,  0.5, -1,    'muon'),
    ('tau',  1776.86,   0.5, -1,    'tau'),
    ('u',    2.16,      0.5,  2/3,  'up quark'),
    ('d',    4.67,      0.5, -1/3,  'down quark'),
    ('s',    93.4,      0.5, -1/3,  'strange quark'),
    ('c',    1270.0,    0.5,  2/3,  'charm quark'),
    ('b',    4180.0,    0.5, -1/3,  'bottom quark'),
    ('t',    172690.0,  0.5,  2/3,  'top quark'),
    ('H',    125250.0,  0,    0,    'Higgs boson'),
)


@dataclass(frozen=True)
class Mode:
    windings: tuple              # signed (n1, n2, n3, n4, n5)
    nonzero_dims: tuple          # 1-based indices of nonzero windings
    n_kind: int                  # number of nonzero windings
    substrate_label: str         # e.g. 'Ma(d2,d4)'
    closure_status: str          # 'closed', 'open' (3+D), 'fail'
    tube_dim: int = 0            # 1-based; 0 if N/A
    sigma_eff: float = 0.0       # σ_eff used for 2D mass
    mass_mev: float = 0.0


def substrate_label(nonzero_dims):
    if not nonzero_dims:
        return 'Ma()'
    return 'Ma(' + ','.join(f'd{i}' for i in nonzero_dims) + ')'


def closure_2d(n_t, n_r):
    """Per architecture.md §3.3.1: m_t | m_r with both nonzero.
    Operates on absolute values; sign-flipped m_t admitted (config-neutrino §NS.2).
    """
    if n_t == 0 or n_r == 0:
        return False
    return abs(n_r) % abs(n_t) == 0


def mass_1d(n, L_fm):
    return TWO_PI_HBARC_MEV_FM * abs(n) / L_fm


def mass_2d(n_t, n_r, L_t_fm, L_r_fm, sigma_eff):
    delta = n_r - sigma_eff * n_t
    return TWO_PI_HBARC_MEV_FM * math.sqrt(
        (n_t / L_t_fm) ** 2 + (delta / L_r_fm) ** 2
    )


def mass_nd_naive(windings, dim_sizes_fm):
    """Naive multi-dim mass with no cross-coupling (3+D closure rule open)."""
    s = sum((n / L) ** 2 for n, L in zip(windings, dim_sizes_fm) if n != 0)
    return TWO_PI_HBARC_MEV_FM * math.sqrt(s)


def parse_sigma_overrides(s):
    """Parse 'd1,d3=1.9764;d2,d3=1.9318' into {(1,3): 1.9764, (2,3): 1.9318}.
    Pair keys are sorted tuples of 1-based dim indices.
    """
    out = {}
    if not s:
        return out
    for part in s.split(';'):
        part = part.strip()
        if not part:
            continue
        pair_str, val_str = part.split('=')
        dims = sorted(int(d.strip().lstrip('d')) for d in pair_str.split(','))
        out[tuple(dims)] = float(val_str)
    return out


def sigma_for_pair(pair_key, sigma_default, sigma_overrides):
    return sigma_overrides.get(pair_key, sigma_default)


def enumerate_modes(dim_sizes_fm, cutoff, sigma_default,
                    sigma_overrides, include_higher):
    """Yield Mode objects for every closure-admitted mode within the cutoff."""
    rng = range(-cutoff, cutoff + 1)
    n_dims = len(dim_sizes_fm)
    for windings in product(rng, repeat=n_dims):
        nonzero = tuple(i + 1 for i, n in enumerate(windings) if n != 0)
        n_kind = len(nonzero)
        if n_kind == 0:
            continue
        label = substrate_label(nonzero)

        if n_kind == 1:
            i = nonzero[0] - 1
            yield Mode(
                windings=windings,
                nonzero_dims=nonzero,
                n_kind=1,
                substrate_label=label,
                closure_status='closed',
                mass_mev=mass_1d(windings[i], dim_sizes_fm[i]),
            )
        elif n_kind == 2:
            a, b = nonzero[0] - 1, nonzero[1] - 1
            n_a, n_b = windings[a], windings[b]
            L_a, L_b = dim_sizes_fm[a], dim_sizes_fm[b]
            pair_key = tuple(sorted(nonzero))
            sigma = sigma_for_pair(pair_key, sigma_default, sigma_overrides)
            # Try both (tube, ring) orientations
            for tube_idx, n_t, n_r, L_t, L_r in (
                (a + 1, n_a, n_b, L_a, L_b),
                (b + 1, n_b, n_a, L_b, L_a),
            ):
                if closure_2d(n_t, n_r):
                    yield Mode(
                        windings=windings,
                        nonzero_dims=nonzero,
                        n_kind=2,
                        substrate_label=label,
                        closure_status='closed',
                        tube_dim=tube_idx,
                        sigma_eff=sigma,
                        mass_mev=mass_2d(n_t, n_r, L_t, L_r, sigma),
                    )
        elif n_kind >= 3 and include_higher:
            yield Mode(
                windings=windings,
                nonzero_dims=nonzero,
                n_kind=n_kind,
                substrate_label=label,
                closure_status='open',
                mass_mev=mass_nd_naive(windings, dim_sizes_fm),
            )


def match_particles(modes, particles, tolerance):
    """For each particle, find the closest-mass mode."""
    results = []
    for name, mass_mev, spin, charge, note in particles:
        best = None
        best_rel = float('inf')
        for mode in modes:
            if mode.mass_mev <= 0:
                continue
            rel = abs(mode.mass_mev - mass_mev) / mass_mev
            if rel < best_rel:
                best_rel = rel
                best = mode
        results.append({
            'name': name, 'mass_mev': mass_mev, 'spin': spin,
            'charge': charge, 'note': note,
            'best_mode': best, 'rel_err': best_rel,
            'matched': best_rel <= tolerance,
        })
    return results


def write_spectrum_csv(modes, out_path):
    sorted_modes = sorted(modes, key=lambda m: m.mass_mev)
    with open(out_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow([
            'mass_MeV', 'substrate', 'kind', 'closure',
            'n1', 'n2', 'n3', 'n4', 'n5',
            'tube_dim', 'sigma_eff',
        ])
        for m in sorted_modes:
            w.writerow([
                f'{m.mass_mev:.6e}',
                m.substrate_label,
                f'{m.n_kind}D',
                m.closure_status,
                *m.windings,
                f'd{m.tube_dim}' if m.tube_dim else '',
                f'{m.sigma_eff:.4f}' if m.tube_dim else '',
            ])


def fmt_params_header(dim_sizes_fm, cutoff, sigma_default,
                       sigma_overrides, tolerance, include_3d):
    lines = []
    lines.append(f'  dim sizes (fm):  d1={dim_sizes_fm[0]:.4g}  '
                  f'd2={dim_sizes_fm[1]:.4g}  d3={dim_sizes_fm[2]:.4g}  '
                  f'd4={dim_sizes_fm[3]:.4g}  d5={dim_sizes_fm[4]:.4g}')
    lines.append(f'  winding cutoff:  |n_i| <= {cutoff}')
    lines.append(f'  sigma_eff:       {sigma_default} (uniform default)')
    if sigma_overrides:
        for pair, val in sorted(sigma_overrides.items()):
            pair_str = ','.join(f'd{i}' for i in pair)
            lines.append(f'                   {pair_str}: {val}')
    if tolerance is not None:
        lines.append(f'  match tol:       {tolerance:.1%}')
    lines.append(f'  include 3+D:     {include_3d}')
    return lines


def write_matches_report(matches, out_path, dim_sizes_fm, cutoff,
                          sigma_default, sigma_overrides, tolerance,
                          include_3d):
    lines = []
    lines.append('K5 mode sweep — observed-particle matches')
    lines.append('=' * 78)
    lines.append('')
    lines.append('Parameters:')
    lines.extend(fmt_params_header(
        dim_sizes_fm, cutoff, sigma_default,
        sigma_overrides, tolerance, include_3d,
    ))
    lines.append('')
    lines.append(
        f'{"Particle":<8}{"Mass (MeV)":>14}  {"Best-match mode":<38}'
        f'{"Mode mass":>14}  {"rel err":>10}  match'
    )
    lines.append('-' * 98)
    for m in matches:
        mode = m['best_mode']
        if mode is None:
            lines.append(f'{m["name"]:<8}{m["mass_mev"]:>14.4g}  (no modes)')
            continue
        wins = '{' + ','.join(f'{w:+d}' for w in mode.windings) + '}'
        tube = f' tube=d{mode.tube_dim}' if mode.tube_dim else ''
        mode_str = f'{mode.substrate_label} {wins}{tube}'
        flag = ' YES' if m['matched'] else ''
        lines.append(
            f'{m["name"]:<8}{m["mass_mev"]:>14.4g}  {mode_str:<38}'
            f'{mode.mass_mev:>14.4g}  {m["rel_err"]:>10.2%}{flag}'
        )
    lines.append('')
    n_match = sum(1 for m in matches if m['matched'])
    lines.append(f'Matched within {tolerance:.0%}: {n_match} / {len(matches)}')
    with open(out_path, 'w') as f:
        f.write('\n'.join(lines) + '\n')


def write_summary(modes, out_path, dim_sizes_fm, cutoff,
                   sigma_default, sigma_overrides, include_3d):
    by_kind = {}
    by_substrate = {}
    for m in modes:
        by_kind[m.n_kind] = by_kind.get(m.n_kind, 0) + 1
        by_substrate[m.substrate_label] = by_substrate.get(m.substrate_label, 0) + 1

    lines = []
    lines.append('K5 mode sweep — summary')
    lines.append('=' * 78)
    lines.append('')
    lines.append('Parameters:')
    lines.extend(fmt_params_header(
        dim_sizes_fm, cutoff, sigma_default,
        sigma_overrides, None, include_3d,
    ))
    lines.append('')
    lines.append('Mode counts by substrate kind:')
    for k in sorted(by_kind):
        lines.append(f'  {k}D: {by_kind[k]}')
    lines.append(f'  total: {sum(by_kind.values())}')
    lines.append('')
    lines.append('Mode counts by substrate (top 25):')
    for label, count in sorted(by_substrate.items(),
                                key=lambda kv: -kv[1])[:25]:
        lines.append(f'  {label}: {count}')
    with open(out_path, 'w') as f:
        f.write('\n'.join(lines) + '\n')


def main():
    p = argparse.ArgumentParser(
        description='K5 5-torus mode sweep and observed-particle matching.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument('--dim-sizes', nargs=5, type=float,
                   default=list(DEFAULT_DIM_SIZES_FM),
                   metavar=('d1', 'd2', 'd3', 'd4', 'd5'),
                   help='Dim sizes in fm (default: K5 spec)')
    p.add_argument('--cutoff', type=int, default=3,
                   help='Max |n_i| in winding tuples (default: 3)')
    p.add_argument('--sigma-eff', type=float, default=2.0,
                   help='Uniform sigma_eff for 2D modes (default: 2.0)')
    p.add_argument('--sigma-overrides', type=str, default='',
                   help='Per-pair sigma_eff overrides; format '
                        '"d1,d3=1.9764;d2,d3=1.9318;d3,d4=1.6837"')
    p.add_argument('--tolerance', type=float, default=0.05,
                   help='Relative-mass match tolerance (default: 0.05)')
    p.add_argument('--include-3d', action='store_true',
                   help='Include 3+-winding modes (naive mass formula)')
    p.add_argument('--output-dir', type=Path,
                   default=Path('outputs/k5_mode_sweep'),
                   help='Output directory (default: outputs/k5_mode_sweep)')
    args = p.parse_args()

    if any(L <= 0 for L in args.dim_sizes):
        raise SystemExit('All dim sizes must be positive.')
    if args.cutoff < 1:
        raise SystemExit('Cutoff must be >= 1.')

    args.output_dir.mkdir(parents=True, exist_ok=True)
    dim_sizes_fm = tuple(args.dim_sizes)
    sigma_overrides = parse_sigma_overrides(args.sigma_overrides)

    print('K5 mode sweep')
    print(f'  dim sizes (fm): {dim_sizes_fm}')
    print(f'  cutoff: {args.cutoff}, sigma_eff: {args.sigma_eff}, '
          f'include_3d: {args.include_3d}')
    if sigma_overrides:
        print(f'  sigma overrides: {sigma_overrides}')

    modes = list(enumerate_modes(
        dim_sizes_fm, args.cutoff,
        args.sigma_eff, sigma_overrides, args.include_3d,
    ))
    print(f'  {len(modes)} modes admitted')

    matches = match_particles(modes, OBSERVED_PARTICLES, args.tolerance)
    n_match = sum(1 for m in matches if m['matched'])
    print(f'  {n_match}/{len(OBSERVED_PARTICLES)} particles matched '
          f'within {args.tolerance:.0%}')

    write_spectrum_csv(modes, args.output_dir / 'spectrum.csv')
    write_matches_report(
        matches, args.output_dir / 'matches.txt',
        dim_sizes_fm, args.cutoff,
        args.sigma_eff, sigma_overrides, args.tolerance, args.include_3d,
    )
    write_summary(
        modes, args.output_dir / 'summary.txt',
        dim_sizes_fm, args.cutoff,
        args.sigma_eff, sigma_overrides, args.include_3d,
    )
    print(f'  outputs written to {args.output_dir}/')


if __name__ == '__main__':
    main()
