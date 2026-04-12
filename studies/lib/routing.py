"""
Energy routing engine for the Ma × S manifold.

Given a metric and a starting configuration (set of occupied
modes), computes the energy cost of each available transition
and ranks them.

Two types of transitions:
  MA:  populate a new mode on the same T⁶ (excite a harmonic,
       fill a dark mode)
  S:   create a new particle at a different spatial location
       (pair production, spatial separation)

The engine doesn't decide physics — it ranks options by energy
cost.  The caller interprets which transitions are allowed by
selection rules.

Usage:
    from lib.metric import Metric
    from lib.routing import RoutingEngine

    m = Metric.model_E()
    engine = RoutingEngine(m)

    # What modes are near a target energy?
    modes = engine.modes_near(target_MeV=105.7, tolerance=5.0,
                              Q=-1, spin=0.5)

    # What's the cheapest next mode above a given energy?
    next_mode = engine.next_above(current_MeV=0.511, Q=-1, spin=0.5)

    # Compare Ma promotion vs S separation
    comparison = engine.promote_vs_separate(
        shell_n=1, Z=1, particle_mass=0.511)

    # Enumerate all modes below a ceiling
    census = engine.mode_census(E_max_MeV=2000)

    # Find a pathway between two configurations
    path = engine.find_pathway(start_mode, end_mode, max_steps=10)
"""

import math
import numpy as np
from itertools import product as iproduct
from collections import namedtuple

from lib.metric import Metric


# ════════════════════════════════════════════════════════════════
#  Data types
# ════════════════════════════════════════════════════════════════

Mode = namedtuple('Mode', ['n', 'E', 'Q', 'sh', 'sheets'])

Transition = namedtuple('Transition', [
    'source', 'target', 'delta_E', 'delta_n', 'kind'
])


class RoutingEngine:
    """
    Energy routing engine for a given metric.

    Parameters
    ----------
    metric : Metric
        The T⁶ metric to use for all computations.
    n_ranges : list of (lo, hi) tuples, length 6
        Search ranges for each quantum number.
        Default: |n_t| ≤ 3, |n_r| ≤ 10 per sheet.
    """

    def __init__(self, metric, n_ranges=None):
        if not metric.valid:
            raise ValueError("Metric is not positive-definite")
        self._metric = metric
        self._n_ranges = n_ranges or [
            (-3, 3), (-10, 10),   # e-sheet
            (-3, 3), (-3, 3),     # ν-sheet
            (-3, 3), (-10, 10),   # p-sheet
        ]

    @property
    def metric(self):
        return self._metric

    # ── Mode enumeration ────────────────────────────────────────

    def mode_census(self, E_max_MeV=2000, Q=None, spin=None):
        """
        Enumerate all modes below E_max with optional Q and spin filter.

        Returns list of Mode, sorted by energy.
        """
        m = self._metric
        results = []

        for n in iproduct(*[range(lo, hi + 1) for lo, hi in self._n_ranges]):
            if all(ni == 0 for ni in n):
                continue
            if Q is not None and m.charge(n) != Q:
                continue
            sh = m.spin_half_count(n)
            if spin is not None:
                if spin == 0.0 and sh not in (0, 2):
                    continue
                if spin == 0.5 and sh not in (1, 3):
                    continue
                if spin == 1.0 and sh != 2:
                    continue
                if spin == 1.5 and sh != 3:
                    continue
            E = m.mode_energy(n)
            if E > E_max_MeV:
                continue
            results.append(Mode(
                n=n, E=E, Q=m.charge(n), sh=sh,
                sheets=m.sheets(n),
            ))

        results.sort(key=lambda x: x.E)
        return results

    def modes_near(self, target_MeV, tolerance_MeV=5.0,
                   Q=None, spin=None):
        """
        Find modes within tolerance of a target energy.

        Returns list of Mode, sorted by distance from target.
        """
        modes = self.mode_census(
            E_max_MeV=target_MeV + tolerance_MeV, Q=Q, spin=spin)
        near = [m for m in modes if abs(m.E - target_MeV) <= tolerance_MeV]
        near.sort(key=lambda x: abs(x.E - target_MeV))
        return near

    def next_above(self, current_MeV, Q=None, spin=None):
        """
        Find the cheapest mode above a given energy.

        Returns Mode or None.
        """
        modes = self.mode_census(
            E_max_MeV=current_MeV * 3, Q=Q, spin=spin)
        above = [m for m in modes if m.E > current_MeV * 1.001]
        return above[0] if above else None

    # ── Transition analysis ─────────────────────────────────────

    def transitions_from(self, source_mode, E_max_delta=100.0):
        """
        Enumerate all single-step transitions from a source mode.

        A single step changes one quantum number by ±1.
        Returns list of Transition, sorted by |delta_E|.
        """
        m = self._metric
        E_source = m.mode_energy(source_mode)
        results = []

        for dim in range(6):
            for delta in (-1, +1):
                target = list(source_mode)
                target[dim] += delta
                target = tuple(target)
                if all(ni == 0 for ni in target):
                    continue
                E_target = m.mode_energy(target)
                dE = E_target - E_source
                if abs(dE) > E_max_delta:
                    continue
                dn = [0] * 6
                dn[dim] = delta
                results.append(Transition(
                    source=source_mode,
                    target=target,
                    delta_E=dE,
                    delta_n=tuple(dn),
                    kind='Ma',
                ))

        results.sort(key=lambda x: abs(x.delta_E))
        return results

    def find_pathway(self, start, end, max_steps=20):
        """
        Find a least-energy path from start mode to end mode.

        Uses greedy search: at each step, pick the transition
        that moves closest to the target in mode space while
        minimizing energy cost.

        Parameters
        ----------
        start, end : tuple(6,)
        max_steps : int

        Returns
        -------
        list of Transition, or None if no path found
        """
        m = self._metric
        current = tuple(start)
        target = tuple(end)
        path = []
        visited = {current}

        for step in range(max_steps):
            if current == target:
                return path

            # All single-step transitions
            candidates = []
            for dim in range(6):
                for delta in (-1, +1):
                    next_mode = list(current)
                    next_mode[dim] += delta
                    next_mode = tuple(next_mode)
                    if next_mode in visited:
                        continue
                    if all(ni == 0 for ni in next_mode):
                        continue

                    # Distance to target in mode space
                    dist = sum(abs(next_mode[i] - target[i]) for i in range(6))
                    E = m.mode_energy(next_mode)
                    candidates.append((dist, E, next_mode, dim, delta))

            if not candidates:
                return None  # stuck

            # Greedy: minimize distance to target, break ties by energy
            candidates.sort(key=lambda x: (x[0], x[1]))
            dist, E, next_mode, dim, delta = candidates[0]

            E_current = m.mode_energy(current)
            dn = [0] * 6
            dn[dim] = delta
            path.append(Transition(
                source=current,
                target=next_mode,
                delta_E=E - E_current,
                delta_n=tuple(dn),
                kind='Ma',
            ))
            visited.add(next_mode)
            current = next_mode

        return path if current == target else None

    # ── Promote vs separate ─────────────────────────────────────

    def promote_vs_separate(self, current_mode, shell_n=1, Z=1):
        """
        Compare the cost of promoting to the next Ma mode vs
        separating to the next spatial shell.

        Parameters
        ----------
        current_mode : tuple(6,)
        shell_n : int — current Bohr shell number
        Z : int — nuclear charge

        Returns
        -------
        dict with 'promote_cost', 'separate_cost', 'cheaper'
        """
        m = self._metric
        E_current = m.mode_energy(current_mode)

        # Promote: cheapest Ma transition upward
        up_transitions = [t for t in self.transitions_from(current_mode)
                         if t.delta_E > 0]
        promote_cost = up_transitions[0].delta_E if up_transitions else float('inf')
        promote_target = up_transitions[0].target if up_transitions else None

        # Separate: Coulomb energy difference to next shell
        # E_n = -Z²α²m_e/(2n²) in MeV
        alpha = 1.0 / 137.036
        E_n = Z**2 * alpha**2 * 0.511 / (2 * shell_n**2)
        E_n1 = Z**2 * alpha**2 * 0.511 / (2 * (shell_n + 1)**2)
        separate_cost = (E_n - E_n1) * 1e3  # convert to keV for readability

        # Convert promote to keV too
        promote_keV = promote_cost * 1e3

        cheaper = 'separate' if separate_cost < promote_keV else 'promote'

        return {
            'promote_cost_keV': promote_keV,
            'promote_target': promote_target,
            'separate_cost_keV': separate_cost,
            'shell_n': shell_n,
            'cheaper': cheaper,
        }

    # ── Energy landscape ────────────────────────────────────────

    def energy_landscape(self, dim_vary, dim_value_range,
                         fixed_dims):
        """
        Compute energy as one quantum number varies.

        Parameters
        ----------
        dim_vary : int (0-5) — which dimension to vary
        dim_value_range : range or list — values to scan
        fixed_dims : dict {dim: value} — fixed quantum numbers

        Returns
        -------
        list of (n_value, E_MeV)
        """
        m = self._metric
        results = []
        for v in dim_value_range:
            n = [0] * 6
            for d, val in fixed_dims.items():
                n[d] = val
            n[dim_vary] = v
            if all(ni == 0 for ni in n):
                continue
            E = m.mode_energy(tuple(n))
            results.append((v, E))
        return results
