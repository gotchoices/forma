"""
R63 Track 7 Phase 7b — Compound-mode prediction for nuclei from Fe
through Pb, through the known-heavy-unstable regime, and into the
hypothetical territory up to element 137.

Extends Phase 7a's A-scaling compound-mode calculation past ⁵⁶Fe.
For each nucleus, compute the predicted mass at the g-candidate
parameter set (the developing R63 refinement of model-F).  Where
an observed atomic mass exists (stable or long-lived), compare
to observation and tabulate miss vs binding energy.  For
elements beyond the known regime (Z > 118 or beyond AME values),
record the prediction without a comparison — the MaSt prediction
itself is the output.

The questions Phase 7b is designed to answer:

  1. Does the compound-mode miss pattern stay in the 1.3–1.4%
     plateau established by 7a, or does it diverge past Fe?
  2. Does any divergence coincide with the observed stability
     boundary (~²⁰⁹Bi at Z=83, or the end of primordial nuclides
     around Z=92)?
  3. What does MaSt predict for elements that cannot be stably
     assembled in nature?

The calculation is ratio-invariant at leading order in A, so the
qualitative pattern does not depend on the exact working
parameter values.

Outputs (../outputs/):
  - track7b_chain.csv            — per-nucleus table (extension)
  - track7b_chain_full.csv       — combined 7a + 7b full chain
  - track7b_miss_vs_A.png        — miss pattern across full chain
  - track7b_mass_panel.png       — mass + binding-per-nucleon panel
  - track7b_heavy_prediction.png — prediction beyond observed chain
"""

import sys, os
import csv
import math
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

from track1_solver import (
    Params, derive_L_ring, L_vector_from_params, mode_energy, mode_6_to_11,
    signature_ok, M_E_MEV, M_P_MEV,
    SQRT_ALPHA, FOUR_PI, ALPHA,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF

from track7a_nuclei_H_to_Fe import (
    NUCLEI as NUCLEI_7A,
    nuclear_mass, binding_energy, compound_mass, build_working_metric,
    U_TO_MEV, M_E, M_P, M_N, WORKING_PARAMS,
)


# ─── Extended nuclei chain, Fe → hypothetical Z=137 ───────────────
# (name, Z, A, atomic_mass_u, category)
#   category: 'stable', 'primordial' (long-lived enough to be naturally
#             present), 'unstable' (known but short-lived),
#             'hypothetical' (no observed mass)
# atomic_mass_u values are NaN for hypothetical entries.

NUCLEI_7B = [
    # Stable heavy chain (27 ≤ Z ≤ 82)
    ("59Co",   27,  59,  58.933194,  'stable'),
    ("58Ni",   28,  58,  57.935343,  'stable'),
    ("63Cu",   29,  63,  62.929598,  'stable'),
    ("64Zn",   30,  64,  63.929142,  'stable'),
    ("75As",   33,  75,  74.921595,  'stable'),
    ("80Se",   34,  80,  79.916522,  'stable'),
    ("85Rb",   37,  85,  84.911790,  'stable'),  # Rb-85 is stable (Rb-87 primordial)
    ("89Y",    39,  89,  88.905842,  'stable'),
    ("93Nb",   41,  93,  92.906373,  'stable'),
    ("98Mo",   42,  98,  97.905405,  'stable'),
    ("107Ag",  47, 107, 106.905092,  'stable'),
    ("113Cd",  48, 113, 112.904408,  'stable'),
    ("120Sn",  50, 120, 119.902203,  'stable'),
    ("127I",   53, 127, 126.904472,  'stable'),
    ("133Cs",  55, 133, 132.905452,  'stable'),
    ("138Ba",  56, 138, 137.905247,  'stable'),
    ("140Ce",  58, 140, 139.905444,  'stable'),
    ("159Tb",  65, 159, 158.925354,  'stable'),
    ("175Lu",  71, 175, 174.940777,  'stable'),  # technically 2.8e10 yr, often listed stable
    ("181Ta",  73, 181, 180.947996,  'stable'),
    ("184W",   74, 184, 183.950930,  'stable'),
    ("197Au",  79, 197, 196.966552,  'stable'),
    ("208Pb",  82, 208, 207.976652,  'stable'),

    # Primordial long-lived (naturally present on Earth)
    ("209Bi",  83, 209, 208.980398,  'primordial'),  # t½ ≈ 2×10¹⁹ yr
    ("232Th",  90, 232, 232.038054,  'primordial'),  # t½ ≈ 1.4×10¹⁰ yr
    ("235U",   92, 235, 235.043929,  'primordial'),  # t½ ≈ 7×10⁸ yr
    ("238U",   92, 238, 238.050788,  'primordial'),  # t½ ≈ 4.5×10⁹ yr

    # Known but short-lived heavy
    ("244Pu",  94, 244, 244.064200,  'unstable'),
    ("248Cm",  96, 248, 248.072349,  'unstable'),
    ("252Cf",  98, 252, 252.081627,  'unstable'),
    ("257Fm", 100, 257, 257.095106,  'unstable'),
    ("262Rf", 104, 262, 262.109920,  'unstable'),
    ("269Sg", 106, 269, 269.128495,  'unstable'),
    ("278Nh", 113, 278, 278.170600,  'unstable'),  # AME estimate
    ("294Og", 118, 294, 294.213920,  'unstable'),  # heaviest observed

    # Hypothetical beyond observed nuclei (no atomic mass available)
    #   A chosen to approximate N/Z ≈ 1.6–1.7 typical of heavy/superheavy
    ("~300_120", 120, 300, float('nan'), 'hypothetical'),
    ("~316_125", 125, 316, float('nan'), 'hypothetical'),
    ("~330_130", 130, 330, float('nan'), 'hypothetical'),
    ("~342_135", 135, 342, float('nan'), 'hypothetical'),
    ("~348_137", 137, 348, float('nan'), 'hypothetical'),  # Feynman-limit Z
]


# ─── Main ─────────────────────────────────────────────────────────

def per_nucleus_row(G, L, name, Z, A, atomic_u, category):
    m_pred = compound_mass(G, L, Z, A)
    if math.isnan(atomic_u):
        m_obs = float('nan')
        B     = float('nan')
        B_rel = float('nan')
        miss  = float('nan')
        miss_rel = float('nan')
    else:
        m_obs = nuclear_mass(atomic_u, Z)
        B     = binding_energy(Z, A, m_obs)
        B_rel = B / m_obs
        miss  = m_pred - m_obs
        miss_rel = miss / m_obs
    return {
        'name': name, 'Z': Z, 'A': A,
        'category': category,
        'atomic_u': atomic_u,
        'm_obs': m_obs, 'B': B, 'B_rel': B_rel,
        'm_pred': m_pred, 'miss': miss, 'miss_rel': miss_rel,
        'B_per_A': (B / A if (not math.isnan(B)) and A > 0 else float('nan')),
    }


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 120)
    print("R63 Track 7b — Compound-mode audit, Fe → hypothetical element 137")
    print("=" * 120)
    print(f"  Working parameters (g-candidate): "
          f"ε_e={WORKING_PARAMS['eps_e']}, s_e={WORKING_PARAMS['s_e']}, "
          f"ε_p={WORKING_PARAMS['eps_p']}, s_p={WORKING_PARAMS['s_p']}")
    print()

    params, G, L = build_working_metric()

    # ─── Compute full chain (7a + 7b) ───
    NUCLEI_ALL = ([(n, Z, A, u, 'stable')
                   for (n, Z, A, u) in NUCLEI_7A] +
                  NUCLEI_7B)
    rows = []
    for (name, Z, A, atomic_u, category) in NUCLEI_ALL:
        r = per_nucleus_row(G, L, name, Z, A, atomic_u, category)
        rows.append(r)

    # ─── Print 7b-specific table ───
    print("  Phase 7b extension (Z ≥ 27):")
    print(f"  {'nucleus':<10s}  {'Z':>3s}  {'A':>4s}  "
          f"{'m_obs':>12s}  {'m_pred':>12s}  "
          f"{'miss':>10s}  {'Δm/m':>8s}  {'B/m':>6s}  {'B/A':>6s}  {'category':<14s}")
    print("  " + "-" * 118)
    for r in rows[len(NUCLEI_7A):]:
        if math.isnan(r['m_obs']):
            m_obs_s = '{:>12s}'.format('(none)')
            miss_s  = '{:>10s}'.format('—')
            miss_rs = '{:>8s}'.format('—')
            B_rs    = '{:>6s}'.format('—')
            B_pAs   = '{:>6s}'.format('—')
        else:
            m_obs_s = f"{r['m_obs']:>12.3f}"
            miss_s  = f"{r['miss']:>+10.3f}"
            miss_rs = f"{r['miss_rel']*100:>+7.4f}%"
            B_rs    = f"{r['B_rel']*100:>5.3f}%"
            B_pAs   = f"{r['B_per_A']:>6.3f}"
        print(f"  {r['name']:<10s}  {r['Z']:>3d}  {r['A']:>4d}  "
              f"{m_obs_s}  {r['m_pred']:>12.3f}  "
              f"{miss_s}  {miss_rs}  {B_rs}  {B_pAs}  {r['category']:<14s}")
    print()

    # ─── Summary by category ───
    print("  Summary by category:")
    for cat in ('stable', 'primordial', 'unstable', 'hypothetical'):
        miss_rels = [r['miss_rel']*100 for r in rows
                     if r['category'] == cat and not math.isnan(r['miss_rel'])]
        n = len(miss_rels)
        n_hypothetical = len([r for r in rows if r['category'] == cat])
        if n > 0:
            print(f"    {cat:<14s}: {n:>3d} with observed mass; "
                  f"miss% range [{min(miss_rels):+.3f}, {max(miss_rels):+.3f}], "
                  f"mean {sum(miss_rels)/n:+.3f}")
        else:
            print(f"    {cat:<14s}: {n_hypothetical:>3d} without observed mass "
                  f"(prediction only)")
    print()

    # ─── CSVs ───
    csv_path = out_dir / "track7b_chain.csv"
    full_csv = out_dir / "track7b_chain_full.csv"
    fields = ['name', 'Z', 'A', 'category', 'atomic_u',
              'm_obs', 'B', 'B_rel', 'm_pred', 'miss', 'miss_rel', 'B_per_A']
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows[len(NUCLEI_7A):]:
            w.writerow({k: r[k] for k in fields})
    with open(full_csv, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in fields})
    print(f"  CSVs: {csv_path}, {full_csv}")

    # ─── Plots ───
    A_arr      = np.array([r['A'] for r in rows], dtype=float)
    Z_arr      = np.array([r['Z'] for r in rows], dtype=float)
    miss_rel   = np.array([r['miss_rel']*100 if not math.isnan(r['miss_rel'])
                            else np.nan for r in rows])
    B_rel      = np.array([r['B_rel']*100 if not math.isnan(r['B_rel'])
                            else np.nan for r in rows])
    B_per_A    = np.array([r['B_per_A'] if not math.isnan(r['B_per_A'])
                            else np.nan for r in rows])
    m_obs_arr  = np.array([r['m_obs'] if not math.isnan(r['m_obs'])
                            else np.nan for r in rows])
    m_pred_arr = np.array([r['m_pred'] for r in rows], dtype=float)
    cats       = [r['category'] for r in rows]

    cat_colors = {'stable': 'tab:blue', 'primordial': 'tab:green',
                  'unstable': 'tab:orange', 'hypothetical': 'tab:red'}
    cat_markers = {'stable': 'o', 'primordial': 's',
                   'unstable': '^', 'hypothetical': 'D'}

    # Plot 1: miss% vs A across full chain, colored by category
    fig, ax = plt.subplots(figsize=(13, 6.5))
    for cat in ('stable', 'primordial', 'unstable', 'hypothetical'):
        idx = [i for i, c in enumerate(cats) if c == cat]
        A_cat = A_arr[idx]
        miss_cat = miss_rel[idx]
        mask = ~np.isnan(miss_cat)
        if mask.any():
            ax.plot(A_cat[mask], miss_cat[mask],
                    cat_markers[cat], color=cat_colors[cat],
                    markersize=7, label=cat, linestyle='none')
    # Guide lines
    ax.axvline(56, color='gray', linestyle=':', alpha=0.6, label='Fe (A=56)')
    ax.axvline(209, color='red', linestyle=':', alpha=0.6,
               label='Bi (A=209, end of primordial)')
    ax.axvline(238, color='orange', linestyle=':', alpha=0.6,
               label='U-238 (end of long-lived)')
    ax.axhline(1.4, color='lightgray', linestyle='--', alpha=0.7,
               label='1.4% plateau from 7a')
    ax.set_xlabel('mass number A')
    ax.set_ylabel('compound-mode miss  Δm/m  (%)')
    ax.set_title("R63 Track 7b — compound-mode miss vs. A, full chain\n"
                 "H through Pb and into known-unstable; hypothetical elements "
                 "shown as prediction-only")
    ax.grid(alpha=0.3)
    ax.legend(loc='best', fontsize=9)
    ax.set_xlim(0, 360)
    plt.tight_layout()
    plt.savefig(out_dir / "track7b_miss_vs_A.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {out_dir / 'track7b_miss_vs_A.png'}")

    # Plot 2: mass panel across full chain
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6.5))
    for cat in ('stable', 'primordial', 'unstable', 'hypothetical'):
        idx = [i for i, c in enumerate(cats) if c == cat]
        A_cat = A_arr[idx]
        m_obs_cat = m_obs_arr[idx]
        m_pred_cat = m_pred_arr[idx]
        mask = ~np.isnan(m_obs_cat)
        if mask.any():
            ax1.plot(A_cat[mask], m_obs_cat[mask], 'o-',
                     color=cat_colors[cat], markersize=5,
                     label=f'{cat} (observed)', alpha=0.8)
        ax1.plot(A_cat, m_pred_cat, cat_markers[cat],
                 color=cat_colors[cat], markerfacecolor='none',
                 markersize=7, label=f'{cat} (compound-mode)', linestyle=':')
    ax1.set_xlabel('A')
    ax1.set_ylabel('mass (MeV)')
    ax1.set_title("Mass chain (observed vs. compound-mode prediction)")
    ax1.grid(alpha=0.3)
    ax1.legend(loc='best', fontsize=8)

    # Binding-per-nucleon curve
    for cat in ('stable', 'primordial', 'unstable'):
        idx = [i for i, c in enumerate(cats) if c == cat]
        A_cat = A_arr[idx]
        B_per_A_cat = B_per_A[idx]
        mask = ~np.isnan(B_per_A_cat)
        if mask.any():
            ax2.plot(A_cat[mask], B_per_A_cat[mask],
                     cat_markers[cat], color=cat_colors[cat],
                     markersize=6, label=cat, linestyle='none')
    ax2.axhline(8.79, color='red', linestyle=':', linewidth=0.8,
                label='Fe-56 peak ≈ 8.79 MeV/nucleon')
    ax2.axvline(56, color='gray', linestyle=':', alpha=0.6)
    ax2.set_xlabel('A')
    ax2.set_ylabel('B / A  (MeV per nucleon)')
    ax2.set_title("Observed binding-per-nucleon curve across the chain")
    ax2.grid(alpha=0.3)
    ax2.legend(loc='best', fontsize=9)

    plt.suptitle("R63 Track 7b — full stable + unstable + hypothetical chain", y=1.02)
    plt.tight_layout()
    plt.savefig(out_dir / "track7b_mass_panel.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {out_dir / 'track7b_mass_panel.png'}")

    # Plot 3: dedicated view of prediction through the heavy + hypothetical regime
    fig, ax = plt.subplots(figsize=(12, 6))
    idx_heavy = [i for i, r in enumerate(rows) if r['Z'] >= 26]
    A_h = A_arr[idx_heavy]
    m_pred_h = m_pred_arr[idx_heavy]
    Z_h = Z_arr[idx_heavy]
    cats_h = [cats[i] for i in idx_heavy]

    for cat in ('stable', 'primordial', 'unstable', 'hypothetical'):
        ii = [i for i, c in enumerate(cats_h) if c == cat]
        ax.plot(A_h[ii], m_pred_h[ii], cat_markers[cat],
                color=cat_colors[cat], markersize=8,
                label=f'g-candidate prediction ({cat})', linestyle='none')
    # also overlay observed where available
    m_obs_h = m_obs_arr[idx_heavy]
    mask = ~np.isnan(m_obs_h)
    ax.plot(A_h[mask], m_obs_h[mask], 'x', color='black',
            markersize=5, label='observed nuclear mass', alpha=0.6)
    ax.axvline(209, color='red', linestyle=':', alpha=0.6,
               label='Bi (end primordial)')
    ax.axvline(294, color='purple', linestyle=':', alpha=0.6,
               label='Og (heaviest observed)')
    ax.set_xlabel('A')
    ax.set_ylabel('mass (MeV)')
    ax.set_title("R63 Track 7b — compound-mode prediction, Fe → hypothetical element 137")
    ax.grid(alpha=0.3)
    ax.legend(loc='upper left', fontsize=9)
    plt.tight_layout()
    plt.savefig(out_dir / "track7b_heavy_prediction.png",
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Plot: {out_dir / 'track7b_heavy_prediction.png'}")


if __name__ == "__main__":
    main()
