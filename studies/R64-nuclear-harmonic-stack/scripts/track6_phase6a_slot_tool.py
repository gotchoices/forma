"""
R64 Track 6 Phase 6a — Flexible slot-configuration tool for nuclear shell hypotheses.

This is a computational framework for testing nuclear-shell-structure
hypotheses against observed nuclear physics, with no commitment to a
specific MaSt interpretation.  Each hypothesis is a "slot configuration"
specifying:

  1. WHICH MaSt primitives serve as slots (e.g., gcd=1 only, or arbitrary
     user-provided lists)
  2. The ORDER in which slots fill (mass-order, user-specified, etc.)
  3. The PER-SLOT CAPACITY per isospin (1 or 2 nucleons typically)
  4. Whether to add S-emergent Coulomb energy

The tool reports fitness metrics:
  - Magic-A alignment: do shell-closure cumulative counts match observed?
  - B/A peak position: does the predicted curve peak near Fe (A≈56)?
  - Valley of stability: does Z/A trend match observed?
  - Mass-residual stats across the nuclear chain

Models slots under interpretation B3:
  - Each slot holds nucleons of one isospin (proton or neutron, not mixed)
  - Pauli capacity per slot = 2 (spin up/down) by default
  - Protons fill positive-n_r primitives, neutrons fill negative-n_r
    (configurable)
  - Magic numbers are PER-ISOSPIN (matches SM nuclear shell model)

Outputs:
  outputs/track6_phase6a_<config_name>.csv  (one per hypothesis)
"""

import math
import csv
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Callable

import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from track3_phase3a_nuclear_progression import (
    NUCLEI, M_P, M_N, U_TO_MEV, nuclear_mass, observed_binding,
)


# ─── Constants ──────────────────────────────────────────────────────────

EPS_P = 0.2052
S_P = 0.0250
K_P = 63.629  # MeV/μ-unit at Point B

A_COULOMB = 0.71  # MeV (Bethe-Weizsäcker Coulomb coefficient)

MAGIC_PER_ISOSPIN = [2, 8, 20, 28, 50, 82, 126]
DOUBLY_MAGIC_A = [4, 16, 40, 56, 100, 164, 252]

# SOC nuclear shell-model orbital sequence (per isospin), filling order
# Each entry: (label, j, capacity_per_isospin)
SOC_SHELL_SEQUENCE = [
    ("1s_1/2", 0.5, 2),
    ("1p_3/2", 1.5, 4),
    ("1p_1/2", 0.5, 2),
    ("1d_5/2", 2.5, 6),
    ("2s_1/2", 0.5, 2),
    ("1d_3/2", 1.5, 4),
    ("1f_7/2", 3.5, 8),
    ("2p_3/2", 1.5, 4),
    ("1f_5/2", 2.5, 6),
    ("2p_1/2", 0.5, 2),
    ("1g_9/2", 4.5, 10),
    ("1g_7/2", 3.5, 8),
    ("2d_5/2", 2.5, 6),
    ("2d_3/2", 1.5, 4),
    ("3s_1/2", 0.5, 2),
    ("1h_11/2", 5.5, 12),
    ("1h_9/2", 4.5, 10),
    ("2f_7/2", 3.5, 8),
    ("2f_5/2", 2.5, 6),
    ("3p_3/2", 1.5, 4),
    ("3p_1/2", 0.5, 2),
    ("1i_13/2", 6.5, 14),
]


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def mu2(n_t, n_r, eps=EPS_P, s=S_P):
    return (n_t / eps)**2 + (n_r - s * n_t)**2


def primitive_mass(n_t, n_r, eps=EPS_P, s=S_P, K_p=K_P):
    return K_p * math.sqrt(mu2(n_t, n_r, eps, s))


# ─── Slot configurations ───────────────────────────────────────────────

@dataclass
class SlotConfig:
    """Specifies a hypothesis for nuclear shell structure."""
    name: str
    slots_proton: List[Tuple[int, int]]   # ordered list of (n_t, n_r) for proton slots
    slots_neutron: List[Tuple[int, int]]  # ordered list of (n_t, n_r) for neutron slots
    capacity_per_isospin: int = 2          # nucleons per slot (Pauli with spin)
    add_coulomb: bool = False
    # Shell-closure binding bonuses: dict mapping (Z_magic, N_magic) tuples
    # to extra binding (positive value reduces predicted mass).
    # If None, no closure bonuses applied.
    shell_closure_bonuses: Optional[dict] = None
    description: str = ""

    def get_closure_bonus(self, Z, N):
        """Return shell-closure bonus binding (MeV) for a given (Z, N) nucleus.

        A 'magic' Z or N independently contributes a bonus.  Doubly-magic
        gets both.  By default uses standard SOC magic numbers.
        """
        if self.shell_closure_bonuses is None:
            return 0.0
        bonus = 0.0
        # Per-isospin: if Z is magic, add Z's bonus; same for N
        for (z_match, n_match), val in self.shell_closure_bonuses.items():
            if z_match is None or z_match == Z:
                if n_match is None or n_match == N:
                    bonus += val
        return bonus


def gen_mass_ordered_slots(eps=EPS_P, s=S_P, K_p=K_P,
                            gcd_filter=True,
                            n_t_max=8, n_r_max=25,
                            mass_max=4000.0):
    """Enumerate primitives for proton (n_r > 0) and neutron (n_r < 0) slots,
    sorted by mass.  Apply gcd=1 filter if requested.
    """
    proton_slots = []
    neutron_slots = []
    for n_t in range(1, n_t_max + 1):
        for n_r in range(-n_r_max, n_r_max + 1):
            if n_r == 0:
                continue
            if gcd_filter and gcd(n_t, abs(n_r)) != 1:
                continue
            m = primitive_mass(n_t, n_r, eps, s, K_p)
            if m > mass_max:
                continue
            if n_r > 0:
                proton_slots.append((m, n_t, n_r))
            else:
                neutron_slots.append((m, n_t, n_r))
    proton_slots.sort()
    neutron_slots.sort()
    return [(nt, nr) for _, nt, nr in proton_slots], \
           [(nt, nr) for _, nt, nr in neutron_slots]


def fill_to_capacity(slots, n_nucleons, capacity_per_slot=2):
    """Determine how many slots are filled to host n_nucleons.
    Returns (slots_used, last_slot_partially_filled, particles_in_last_slot).
    """
    full_slots = n_nucleons // capacity_per_slot
    remainder = n_nucleons - full_slots * capacity_per_slot
    return full_slots, remainder


def predicted_z_n_at_filling(n_protons, n_neutrons, config: SlotConfig):
    """Determine which slots are occupied for a given (Z, N) configuration."""
    p_full, p_rem = fill_to_capacity(n_protons, config.capacity_per_isospin)
    n_full, n_rem = fill_to_capacity(n_neutrons, config.capacity_per_isospin)
    return {
        'proton_slots_filled': p_full + (1 if p_rem > 0 else 0),
        'neutron_slots_filled': n_full + (1 if n_rem > 0 else 0),
        'proton_slots_full': p_full,
        'neutron_slots_full': n_full,
        'proton_remainder': p_rem,
        'neutron_remainder': n_rem,
    }


# ─── Fitness functions ─────────────────────────────────────────────────

def fitness_magic_alignment(config: SlotConfig):
    """Check if cumulative slot count matches observed magic numbers.

    Magic per isospin: 2, 8, 20, 28, 50, 82, 126
    Slots needed (at capacity 2 nucleons/slot): 1, 4, 10, 14, 25, 41, 63

    For mass-ordered configs, this is just slot count after k slots.
    The "match" tests if the kth slot represents a SHELL BOUNDARY in some
    sense.  Without explicit shell-boundary identification, this is
    informational only.
    """
    target_slot_counts = [m // config.capacity_per_isospin for m in MAGIC_PER_ISOSPIN]
    results = []
    for i, target in enumerate(target_slot_counts):
        if target <= len(config.slots_proton):
            # Slot at index target-1 is the LAST slot of this magic group
            last_slot = config.slots_proton[target - 1]
            results.append({
                'magic_per_isospin': MAGIC_PER_ISOSPIN[i],
                'magic_A_doubly': DOUBLY_MAGIC_A[i],
                'target_slots_per_isospin': target,
                'slot_at_boundary': last_slot,
                'mass_at_boundary': primitive_mass(*last_slot),
            })
        else:
            results.append({
                'magic_per_isospin': MAGIC_PER_ISOSPIN[i],
                'magic_A_doubly': DOUBLY_MAGIC_A[i],
                'target_slots_per_isospin': target,
                'slot_at_boundary': None,
                'mass_at_boundary': None,
            })
    return results


def predicted_mass(Z, A, config: SlotConfig):
    """Predicted nuclear mass under config + R64 Point B + optional Coulomb
    + optional shell-closure binding bonuses.
    """
    n_pt = 3 * A
    n_pr = 2 * (2 * Z - A)
    m_ma = primitive_mass(n_pt, n_pr)
    if config.add_coulomb:
        e_coul = A_COULOMB * Z * (Z - 1) / (A ** (1.0 / 3.0)) if A >= 1 else 0
    else:
        e_coul = 0.0
    N = A - Z
    # Shell-closure bonus REDUCES mass (binds more)
    bonus = config.get_closure_bonus(Z, N)
    return m_ma + e_coul - bonus


def fitness_binding_curve(config: SlotConfig, nuclei=NUCLEI):
    """Compute binding curve prediction for the chain."""
    rows = []
    for name, Z, A, atomic_u in nuclei:
        m_obs = nuclear_mass(atomic_u, Z)
        b_obs = observed_binding(Z, A, m_obs)
        m_pred = predicted_mass(Z, A, config)
        b_pred = Z * M_P + (A - Z) * M_N - m_pred
        rows.append({
            'name': name, 'Z': Z, 'A': A,
            'B_obs': b_obs, 'B_pred': b_pred,
            'B_per_A_obs': b_obs / A, 'B_per_A_pred': b_pred / A,
            'rel_err': (b_pred - b_obs) / b_obs if b_obs > 0.5 else 0,
        })
    return rows


def find_BA_peak(binding_rows):
    """Find the A value with maximum B/A in the predicted curve."""
    rows_proper = [r for r in binding_rows if r['B_obs'] > 0.5]
    obs_peak = max(rows_proper, key=lambda r: r['B_per_A_obs'])
    pred_peak = max(rows_proper, key=lambda r: r['B_per_A_pred'])
    return obs_peak, pred_peak


def fitness_valley_of_stability(config: SlotConfig, A_values=None):
    """For each A, find Z minimizing predicted mass (the predicted valley)."""
    if A_values is None:
        A_values = list(range(2, 240, 4))
    rows = []
    for A in A_values:
        if A < 2:
            continue
        best_z = None
        best_m = float('inf')
        for Z in range(1, A):
            m = predicted_mass(Z, A, config)
            if m < best_m:
                best_m = m
                best_z = Z
        if best_z is None:
            continue
        rows.append({
            'A': A,
            'Z_optimal': best_z,
            'Z_over_A_predicted': best_z / A,
            'm_min_predicted': best_m,
        })
    return rows


# ─── Main runner ──────────────────────────────────────────────────────

def run_hypothesis(config: SlotConfig, out_dir: Path, verbose: bool = True):
    """Run all fitness functions and save results."""
    if verbose:
        print()
        print("=" * 110)
        print(f"HYPOTHESIS: {config.name}")
        print("=" * 110)
        print(f"  {config.description}")
        print(f"  capacity_per_isospin = {config.capacity_per_isospin} nucleons/slot")
        print(f"  add_coulomb = {config.add_coulomb}")
        print(f"  proton slots (first 14): {config.slots_proton[:14]}")
        print()

    # 1. Magic alignment
    magic_results = fitness_magic_alignment(config)
    if verbose:
        print(f"  Magic-A alignment (slot at boundary):")
        for r in magic_results:
            slot_str = str(r['slot_at_boundary']) if r['slot_at_boundary'] else 'N/A'
            mass_str = f"{r['mass_at_boundary']:.1f}" if r['mass_at_boundary'] else 'N/A'
            print(f"    A={r['magic_A_doubly']:>3d}: target {r['target_slots_per_isospin']:>3d} slots → "
                  f"slot {slot_str:<14s} at mass {mass_str:>8s} MeV")
    print()

    # 2. Binding curve
    binding_rows = fitness_binding_curve(config)
    obs_peak, pred_peak = find_BA_peak(binding_rows)

    rows_proper = [r for r in binding_rows if r['B_obs'] > 0.5]
    rel_errs = [abs(r['rel_err']) for r in rows_proper]
    if verbose:
        print(f"  Binding curve fitness:")
        print(f"    Mean |Δ(B)/B|: {np.mean(rel_errs):.2%}")
        print(f"    Max  |Δ(B)/B|: {np.max(rel_errs):.2%}")
        print(f"    Predicted B/A peak: {pred_peak['name']} (A={pred_peak['A']}) "
              f"with B/A = {pred_peak['B_per_A_pred']:.2f}")
        print(f"    Observed  B/A peak: {obs_peak['name']} (A={obs_peak['A']}) "
              f"with B/A = {obs_peak['B_per_A_obs']:.2f}")
        for name in ['4He', '56Fe', '208Pb']:
            r = next((rr for rr in binding_rows if rr['name'] == name), None)
            if r:
                ratio = r['B_pred'] / r['B_obs'] if r['B_obs'] > 0 else 0
                print(f"    {name}: B_pred/B_obs = {ratio:.3f}")
        print()

    # 3. Valley of stability — use observed A values directly
    obs_A_list = sorted({A for _, _, A, _ in NUCLEI})
    valley_rows = fitness_valley_of_stability(config, A_values=obs_A_list)
    if verbose:
        print(f"  Valley of stability (predicted Z/A vs A):")
        for sample_A in [4, 16, 40, 56, 120, 208, 238]:
            r = next((rr for rr in valley_rows if rr['A'] == sample_A), None)
            obs = next((nn for nn in NUCLEI if nn[2] == sample_A), None)
            if r and obs:
                obs_Z = obs[1]
                print(f"    A={sample_A:>3d}: predicted Z={r['Z_optimal']:>3d} "
                      f"(Z/A={r['Z_over_A_predicted']:.3f}), "
                      f"observed Z={obs_Z:>3d} (Z/A={obs_Z/sample_A:.3f})")
        print()

    # Save
    safe_name = config.name.replace(' ', '_').replace('/', '_').replace('=', '')
    csv_binding = out_dir / f"track6_phase6a_{safe_name}_binding.csv"
    with open(csv_binding, 'w', newline='') as f:
        if binding_rows:
            w = csv.DictWriter(f, fieldnames=list(binding_rows[0].keys()))
            w.writeheader()
            w.writerows(binding_rows)

    return {
        'config_name': config.name,
        'magic_results': magic_results,
        'binding_rows': binding_rows,
        'valley_rows': valley_rows,
        'mean_err': np.mean(rel_errs),
        'max_err': np.max(rel_errs),
        'pred_peak': pred_peak,
        'obs_peak': obs_peak,
    }


def main():
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)

    print("=" * 110)
    print("R64 Track 6 Phase 6a — Flexible slot-configuration tool")
    print("=" * 110)
    print()
    print(f"  Magic per isospin:  {MAGIC_PER_ISOSPIN}")
    print(f"  Doubly-magic A:     {DOUBLY_MAGIC_A}")
    print(f"  Per-shell pair counts (SOC-shell-model): "
          f"{[1, 3, 6, 4, 11, 16, 22]}")
    print()

    # Generate mass-ordered slot lists (Point B parameters, gcd=1)
    proton_mass_ordered, neutron_mass_ordered = gen_mass_ordered_slots()
    print(f"  Mass-ordered proton slots (first 20):")
    for i, slot in enumerate(proton_mass_ordered[:20]):
        m = primitive_mass(*slot)
        print(f"    slot {i+1}: (n_t={slot[0]}, n_r={slot[1]:>+3d}), mass = {m:.2f} MeV")
    print()

    # ─── Hypothesis library ──────────────────────────────────────
    # H1: mass-ordered, gcd=1, B3 (capacity=2 per isospin), no Coulomb
    H1 = SlotConfig(
        name="H1_mass_ordered_no_coulomb",
        slots_proton=proton_mass_ordered,
        slots_neutron=neutron_mass_ordered,
        capacity_per_isospin=2,
        add_coulomb=False,
        description="Mass-ordered (gcd=1), B3 capacity, no Coulomb. Baseline.",
    )

    # H2: same as H1 but with Coulomb
    H2 = SlotConfig(
        name="H2_mass_ordered_with_coulomb",
        slots_proton=proton_mass_ordered,
        slots_neutron=neutron_mass_ordered,
        capacity_per_isospin=2,
        add_coulomb=True,
        description="Mass-ordered (gcd=1), B3 capacity, S-Coulomb added. "
                    "Tests if Coulomb fixes the valley of stability.",
    )

    # H3: H2 + Bethe-Weizsäcker surface term
    # (R64-Ma + Coulomb + plugged BW surface, like Track 5 Phase 5c)
    # This requires extending predicted_mass to include surface — implemented
    # as a "negative bonus" applied to all nuclei.
    h3_bonuses = {(None, None): -A_COULOMB * 0}  # placeholder; surface added below
    H3 = SlotConfig(
        name="H3_with_BW_surface",
        slots_proton=proton_mass_ordered,
        slots_neutron=neutron_mass_ordered,
        capacity_per_isospin=2,
        add_coulomb=True,
        shell_closure_bonuses=None,
        description="H2 plus Bethe-Weizsäcker surface (handled inline; same as Track 5 5c).",
    )
    # We'll handle surface inline in H3's mass evaluation.

    # H4: H2 + shell-closure bonuses at observed magic numbers
    # Bonus values calibrated to standard SOC nuclear shell-model gap energies
    # (rough, in MeV per shell closure):
    #   Magic 2: ~10 MeV (1s closure stabilization)
    #   Magic 8: ~5 MeV
    #   Magic 20: ~3 MeV
    #   Magic 28: ~2 MeV
    #   Magic 50: ~1 MeV
    #   Magic 82: ~1 MeV
    #   Magic 126: ~1 MeV
    closure_bonuses = {}
    closure_values = {2: 10.0, 8: 5.0, 20: 3.0, 28: 2.0, 50: 1.0, 82: 1.0, 126: 1.0}
    for z_magic, bonus in closure_values.items():
        closure_bonuses[(z_magic, None)] = bonus  # bonus if Z is magic
        closure_bonuses[(None, z_magic)] = bonus  # bonus if N is magic
    H4 = SlotConfig(
        name="H4_mass_ordered_with_closure_bonuses",
        slots_proton=proton_mass_ordered,
        slots_neutron=neutron_mass_ordered,
        capacity_per_isospin=2,
        add_coulomb=True,
        shell_closure_bonuses=closure_bonuses,
        description="H2 + magic-number shell-closure bonuses (10, 5, 3, 2, 1, 1, 1 MeV per isospin).",
    )

    # Run hypotheses
    results = []
    for config in [H1, H2, H4]:
        result = run_hypothesis(config, out_dir, verbose=True)
        results.append(result)

    # ─── Summary table ──────────────────────────────────────────
    print("=" * 110)
    print("SUMMARY")
    print("=" * 110)
    print()
    print(f"  {'Hypothesis':>40s}  {'mean err':>10s}  {'max err':>10s}  "
          f"{'B/A peak A':>12s}  {'peak ratio':>11s}")
    for r in results:
        print(f"  {r['config_name']:>40s}  {r['mean_err']:>9.2%}  "
              f"{r['max_err']:>9.2%}  {r['pred_peak']['A']:>12d}  "
              f"{r['pred_peak']['B_per_A_pred']/r['obs_peak']['B_per_A_obs']:>11.3f}")
    print()


if __name__ == "__main__":
    main()
