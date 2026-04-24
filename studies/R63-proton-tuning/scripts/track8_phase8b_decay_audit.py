"""
R63 Track 8 Phase 8b — Decay-conservation audit across the hadron zoo.

For each observed decay A → B + C + …, compute:
  - Δ_tuple = parent_tuple − Σ daughter_tuples  (winding check)
  - Mass residual = parent_mass_pred − Σ daughter_mass_preds
  - Comparison to the observed Q-value

Interpretation:
  - If Δ = 0 (zero vector): current g-candidate tuples respect
    winding conservation for this decay.
  - If Δ ≠ 0: either the tuples are not conservation-consistent
    (candidates for Phase 8c refinement) OR the decay is a
    winding-non-conservative process (e.g., flavor-changing weak
    decay, chiral-anomaly decay).

Photons carry no windings (level-1 promotions only) and no mass.
Neutrino flavor mixing (ν_e vs ν_μ vs ν_τ as mass eigenstates
ν₁/ν₂/ν₃) is handled by best-guess assignment; a more careful
treatment requires the PMNS matrix and is out of scope for 8b.

Outputs (../outputs/):
  - track8_phase8b_decays.csv — per-decay audit
  - track8_phase8b_summary.txt — printed table
"""

import sys, os
import csv
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

from track1_solver import (
    L_vector_from_params, mode_energy, mode_6_to_11,
    signature_ok,
)
from track7a_nuclei_H_to_Fe import build_working_metric


# ─── Tuple database (g-candidate, with Phase 8a neutron) ───────────

TUPLES = {
    # Fundamentals
    "electron": (1, 2, 0, 0, 0, 0),      # e⁻, Q=−1
    "proton":   (0, 0, 0, 0, 3, 6),      # p, Q=+1
    "neutron":  (1, 2, -1, -1, 3, 6),    # n, Q=0 (Phase 8a, β-consistent)
    "nu_1":     (0, 0, 1, 1, 0, 0),      # ν₁, Q=0
    "nu_2":     (0, 0, -1, 1, 0, 0),     # ν₂, Q=0
    "nu_3":     (0, 0, 1, 2, 0, 0),      # ν₃, Q=0
    "muon":     (1, 1, -2, -6, 0, 0),    # μ⁻, Q=−1 (R60 T19)
    "photon":   (0, 0, 0, 0, 0, 0),      # γ, Q=0, massless

    # Hadrons from R60 T19
    "Lambda":    (-3, 2, 1, -6, -3, -3),     # Λ, Q=0
    "Sigma_-":   (4, 0, -2, -6, 3, 5),       # Σ⁻, Q=−1
    "Sigma_+":   (2, -3, -2, -6, 3, 6),      # Σ⁺, Q=+1
    "Xi_-":      (-2, 4, 0, -6, -3, 6),      # Ξ⁻, Q=−1
    "Xi_0":      (-3, 2, 1, -6, -3, 6),      # Ξ⁰, Q=0
    "rho0":      (-3, -6, 1, -6, -3, 3),     # ρ⁰, Q=0
    "phi":       (-3, -6, 1, -6, -3, 6),     # φ, Q=0
    "K0":        (0, -1, -1, -6, 0, -4),     # K⁰, Q=0
    "K_plus":    (1, 3, -2, -6, 0, -4),      # K⁺, Q=+1
    "eta":       (0, -4, -1, -6, 0, -3),     # η, Q=0
    "eta_prime": (0, -6, -1, -6, 0, -6),     # η′, Q=0
    "pi0":       (0, 0, -1, -6, 0, -1),      # π⁰, Q=0
    "pi_plus":   (1, 2, -2, -6, 0, -1),      # π⁺, Q=+1
}

# Observed masses (MeV) for mass-residual computation
OBSERVED_MASS = {
    "electron": 0.510999, "proton": 938.272, "neutron": 939.565,
    "nu_1": 3.21e-8, "nu_2": 3.33e-8, "nu_3": 5.96e-8,
    "muon": 105.6584, "photon": 0.0,
    "Lambda": 1115.683, "Sigma_-": 1197.449, "Sigma_+": 1189.37,
    "Xi_-": 1321.71, "Xi_0": 1314.86,
    "rho0": 775.26, "phi": 1019.461,
    "K0": 497.611, "K_plus": 493.677,
    "eta": 547.862, "eta_prime": 957.78,
    "pi0": 134.977, "pi_plus": 139.570,
}

# Observed charges
CHARGE = {
    "electron": -1, "proton": +1, "neutron": 0,
    "nu_1": 0, "nu_2": 0, "nu_3": 0, "muon": -1, "photon": 0,
    "Lambda": 0, "Sigma_-": -1, "Sigma_+": +1,
    "Xi_-": -1, "Xi_0": 0, "rho0": 0, "phi": 0,
    "K0": 0, "K_plus": +1,
    "eta": 0, "eta_prime": 0, "pi0": 0, "pi_plus": +1,
}


def C_conjugate(tup):
    """Antiparticle winding = negative of particle winding."""
    return tuple(-x for x in tup)


def get_tuple(name):
    """Resolve a particle name, supporting 'anti_X' for antiparticles."""
    if name.startswith("anti_"):
        base = name[5:]
        return C_conjugate(TUPLES[base])
    return TUPLES[name]


def get_mass(name):
    if name.startswith("anti_"):
        return OBSERVED_MASS[name[5:]]
    return OBSERVED_MASS[name]


def get_charge(name):
    if name.startswith("anti_"):
        return -CHARGE[name[5:]]
    return CHARGE[name]


# ─── Decay list ─────────────────────────────────────────────────────
# Each entry: (parent, [daughters], branching %, category)
# "anti_X" denotes the C-conjugate (antiparticle) of X.

DECAYS = [
    # β decay (canonical — defines neutron tuple)
    ("neutron",   ["proton", "electron", "anti_nu_1"],  100,   "beta"),

    # Baryon weak decays
    ("Lambda",    ["proton", "anti_pi_plus"],            64,   "weak-hadronic"),
    ("Lambda",    ["neutron", "pi0"],                    36,   "weak-hadronic"),
    ("Sigma_-",   ["neutron", "anti_pi_plus"],           99,   "weak-hadronic"),
    ("Sigma_+",   ["proton", "pi0"],                     52,   "weak-hadronic"),
    ("Sigma_+",   ["neutron", "pi_plus"],                48,   "weak-hadronic"),
    ("Xi_-",      ["Lambda", "anti_pi_plus"],            99,   "weak-hadronic"),
    ("Xi_0",      ["Lambda", "pi0"],                     99,   "weak-hadronic"),

    # Meson decays
    ("rho0",      ["pi_plus", "anti_pi_plus"],          100,   "strong"),
    ("K0",        ["pi_plus", "anti_pi_plus"],           69,   "weak"),       # K_S
    ("K_plus",    ["anti_muon", "nu_2"],                 64,   "weak-leptonic"),  # ν_μ ≈ ν_2
    ("K_plus",    ["pi_plus", "pi0"],                    21,   "weak-hadronic"),
    ("pi_plus",   ["anti_muon", "nu_2"],                100,   "weak-leptonic"),
    ("pi0",       ["photon", "photon"],                  99,   "EM-anomaly"),
    ("eta",       ["photon", "photon"],                  39,   "EM-anomaly"),
    ("eta",       ["pi0", "pi0", "pi0"],                 33,   "strong"),
    ("eta_prime", ["rho0", "photon"],                    29,   "EM"),
    ("eta_prime", ["eta", "pi0", "pi0"],                 43,   "strong"),
    ("phi",       ["K_plus", "anti_K_plus"],             49,   "strong"),
]


# ─── Audit ──────────────────────────────────────────────────────────

def vec_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def vec_sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def sum_tuples(names):
    total = (0, 0, 0, 0, 0, 0)
    for n in names:
        total = vec_add(total, get_tuple(n))
    return total


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    params, G, L = build_working_metric()

    def E_pred(tup):
        try:
            return mode_energy(G, L, mode_6_to_11(tup))
        except Exception:
            return float('nan')

    # Build rows
    rows = []
    for parent, daughters, branch, category in DECAYS:
        try:
            parent_tup = get_tuple(parent)
            daughters_tup = sum_tuples(daughters)
        except KeyError as e:
            rows.append({
                'parent': parent, 'daughters': '+'.join(daughters),
                'branch_pct': branch, 'category': category,
                'error': f'missing tuple: {e}',
            })
            continue

        delta = vec_sub(parent_tup, daughters_tup)
        delta_zero = all(d == 0 for d in delta)

        # Mass residuals from the metric predictions
        m_parent = E_pred(parent_tup)
        m_daughters_sum = sum(E_pred(get_tuple(d)) for d in daughters)
        mass_resid_pred = m_parent - m_daughters_sum

        # Observed Q-value: parent observed - sum daughter observed
        try:
            m_p_obs = get_mass(parent)
            m_d_obs_sum = sum(get_mass(d) for d in daughters)
            Q_observed = m_p_obs - m_d_obs_sum
        except KeyError:
            Q_observed = float('nan')

        # Charge conservation (ingredient sum)
        Q_parent = get_charge(parent)
        Q_daughters = sum(get_charge(d) for d in daughters)
        charge_ok = (Q_parent == Q_daughters)

        rows.append({
            'parent': parent, 'daughters': ' + '.join(daughters),
            'branch_pct': branch, 'category': category,
            'parent_tuple': str(parent_tup).replace(' ', ''),
            'daughter_sum': str(daughters_tup).replace(' ', ''),
            'delta': str(delta).replace(' ', ''),
            'delta_zero': delta_zero,
            'Q_parent': Q_parent,
            'Q_daughters_sum': Q_daughters,
            'charge_ok': charge_ok,
            'm_parent_pred': m_parent,
            'm_daughters_sum_pred': m_daughters_sum,
            'mass_resid_pred': mass_resid_pred,
            'Q_observed': Q_observed,
            'error': '',
        })

    # Print
    log_lines = []
    def emit(line):
        print(line); log_lines.append(line)

    emit("=" * 130)
    emit("R63 Track 8 Phase 8b — Decay-conservation audit")
    emit("=" * 130)
    emit(f"  {'parent':<10s}  {'decay':<32s}  {'BR%':>4s}  "
         f"{'Δ_tuple':<18s}  {'winding':<7s}  {'Q parent / Σ':>12s}  "
         f"{'mass resid (pred)':>17s}  {'Q_obs (MeV)':>11s}")
    emit("  " + "-" * 128)

    n_conservative = 0
    n_violation = 0
    for r in rows:
        if r.get('error'):
            emit(f"  {r['parent']:<10s}  ERROR: {r['error']}")
            continue
        cons_flag = '✓ OK ' if r['delta_zero'] else '✗ NO'
        chg_flag = '✓' if r['charge_ok'] else '✗'
        if r['delta_zero']:
            n_conservative += 1
        else:
            n_violation += 1
        emit(f"  {r['parent']:<10s}  "
             f"→ {r['daughters']:<30s}  {r['branch_pct']:>4d}  "
             f"{r['delta']:<18s}  {cons_flag:<7s}  "
             f"{r['Q_parent']:>+3d}/{r['Q_daughters_sum']:>+3d} {chg_flag:>2s}  "
             f"{r['mass_resid_pred']:>+15.3f}  {r['Q_observed']:>11.3f}")

    emit("  " + "-" * 128)
    emit(f"  Summary: {n_conservative} of {n_conservative + n_violation} "
         f"decays are winding-conservative under current tuples.")
    emit("")

    # Group results by decay category
    emit("  Breakdown by decay type:")
    cat_stats = {}
    for r in rows:
        if r.get('error'): continue
        cat = r['category']
        if cat not in cat_stats:
            cat_stats[cat] = [0, 0]
        if r['delta_zero']:
            cat_stats[cat][0] += 1
        else:
            cat_stats[cat][1] += 1
    for cat, (n_ok, n_bad) in sorted(cat_stats.items()):
        emit(f"    {cat:<18s}: {n_ok:>2d} conservative, {n_bad:>2d} violations")

    with open(out_dir / "track8_phase8b_summary.txt", 'w') as f:
        f.write("\n".join(log_lines))

    # CSV
    csv_path = out_dir / "track8_phase8b_decays.csv"
    fields = ['parent', 'daughters', 'branch_pct', 'category',
              'parent_tuple', 'daughter_sum', 'delta', 'delta_zero',
              'Q_parent', 'Q_daughters_sum', 'charge_ok',
              'm_parent_pred', 'm_daughters_sum_pred', 'mass_resid_pred',
              'Q_observed']
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            if r.get('error'): continue
            w.writerow({k: r[k] for k in fields})
    emit(f"\n  CSV: {csv_path}")


if __name__ == "__main__":
    main()
