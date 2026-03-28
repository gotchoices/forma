"""
Regression tests for the Ma model library.

Run from studies/:
    python -m unittest lib.test_lib
    python -m unittest lib.test_lib -v        (verbose)
    python -m unittest lib.test_lib.TestMa    (one class)

Pins numerical values against the current ma.py / ma_solver.py so
that any future refactor (including ma_model.py) can be validated.

Reference geometry:
    r_e = 6.6, r_nu = 5.0, r_p = 8.906, sigma_ep = -0.0906
"""

import math
import sys
import unittest
import numpy as np

if "studies" not in sys.path:
    sys.path.insert(0, "studies")


# ════════════════════════════════════════════════════════════════════
#  constants.py
# ════════════════════════════════════════════════════════════════════

class TestConstants(unittest.TestCase):
    """Physical constants match CODATA 2019 exact / PDG 2022."""

    def test_planck_exact(self):
        from lib.constants import h
        self.assertEqual(h, 6.62607015e-34)

    def test_speed_of_light_exact(self):
        from lib.constants import c
        self.assertEqual(c, 299_792_458)

    def test_elementary_charge_exact(self):
        from lib.constants import e
        self.assertEqual(e, 1.602176634e-19)

    def test_fine_structure(self):
        from lib.constants import alpha
        self.assertAlmostEqual(alpha, 7.2973525693e-3, places=13)

    def test_hbar_derived(self):
        from lib.constants import h, hbar
        self.assertAlmostEqual(hbar, h / (2 * math.pi), places=50)

    def test_lambda_C_derived(self):
        from lib.constants import h, m_e, c, lambda_C
        self.assertAlmostEqual(lambda_C, h / (m_e * c), delta=1e-25)

    def test_electron_mass(self):
        from lib.constants import m_e
        self.assertAlmostEqual(m_e, 9.1093837015e-31, places=40)


# ════════════════════════════════════════════════════════════════════
#  series.py
# ════════════════════════════════════════════════════════════════════

class TestSeries(unittest.TestCase):

    def test_geometric_sum_basic(self):
        from lib.series import geometric_sum
        self.assertAlmostEqual(geometric_sum(0.5, 2), 1.75)

    def test_geometric_sum_r_zero(self):
        from lib.series import geometric_sum
        self.assertAlmostEqual(geometric_sum(0.0, 10), 1.0)

    def test_geometric_sum_r_one(self):
        from lib.series import geometric_sum
        self.assertAlmostEqual(geometric_sum(1.0, 5), 6.0)
        self.assertAlmostEqual(geometric_sum(1.0, 0), 1.0)

    def test_infinite_sum_basic(self):
        from lib.series import infinite_sum
        self.assertAlmostEqual(infinite_sum(0.5), 2.0)

    def test_infinite_sum_r_one(self):
        from lib.series import infinite_sum
        self.assertEqual(infinite_sum(1.0), float('inf'))

    def test_solve_r_roundtrip(self):
        from lib.series import geometric_sum, solve_r_for_n
        r = solve_r_for_n(10, 5.0)
        self.assertAlmostEqual(geometric_sum(r, 10), 5.0, places=8)


# ════════════════════════════════════════════════════════════════════
#  wvm.py
# ════════════════════════════════════════════════════════════════════

class TestWvM(unittest.TestCase):

    def test_charge_ratio(self):
        from lib.wvm import wvm_charge_ratio
        # q/e ≈ 0.910 (WvM undershoots; e/q ≈ 1.099 is the correction)
        self.assertAlmostEqual(wvm_charge_ratio(), 0.9103, places=3)

    def test_charge_positive(self):
        from lib.wvm import wvm_charge
        self.assertGreater(wvm_charge(), 0)


# ════════════════════════════════════════════════════════════════════
#  ma.py — alpha formula
# ════════════════════════════════════════════════════════════════════

class TestAlpha(unittest.TestCase):

    def test_roundtrip_multiple_r(self):
        """solve_shear_for_alpha inverts alpha_ma at several r values."""
        from lib.ma import alpha_ma, solve_shear_for_alpha
        from lib.constants import alpha
        for r in [0.5, 2.0, 6.6, 8.906, 20.0]:
            s = solve_shear_for_alpha(r)
            if s is not None:
                self.assertAlmostEqual(
                    alpha_ma(r, s), alpha, places=10,
                    msg=f"roundtrip failed at r={r}")

    def test_alpha_at_6_6(self):
        from lib.ma import alpha_ma, solve_shear_for_alpha
        s = solve_shear_for_alpha(6.6)
        self.assertAlmostEqual(s, 0.01029, places=4)
        self.assertAlmostEqual(alpha_ma(6.6, s), 7.2973525693e-3, places=10)

    def test_no_solution_small_r(self):
        from lib.ma import solve_shear_for_alpha
        self.assertIsNone(solve_shear_for_alpha(0.1))

    def test_compute_scales_rejects_small_r(self):
        from lib.ma import compute_scales
        with self.assertRaises(ValueError):
            compute_scales(r_e=0.1, r_nu=5.0, r_p=6.6)


# ════════════════════════════════════════════════════════════════════
#  ma.py — metric and mode properties
# ════════════════════════════════════════════════════════════════════

# Standard reference geometry
REF_R_E = 6.6
REF_R_NU = 5.0
REF_R_P = 8.906
REF_SIGMA_EP = -0.0906

# Reference modes
ELECTRON = (1, 2, 0, 0, 0, 0)
PROTON   = (0, 0, 0, 0, 1, 2)
NEUTRON  = (0, -2, 1, 0, 0, 2)
NEUTRINO = (0, 0, 1, 1, 0, 0)


class TestMa(unittest.TestCase):
    """Regression tests at the standard geometry."""

    @classmethod
    def setUpClass(cls):
        from lib.ma import build_scaled_metric
        cls.Gt, cls.Gti, cls.L, cls.info = build_scaled_metric(
            r_e=REF_R_E, r_nu=REF_R_NU, r_p=REF_R_P,
            sigma_ep=REF_SIGMA_EP)

    # ── Metric properties ─────────────────────────────────────────

    def test_metric_positive_definite(self):
        from lib.ma import is_positive_definite
        self.assertTrue(is_positive_definite(self.Gt))

    def test_metric_symmetric(self):
        np.testing.assert_array_almost_equal(self.Gt, self.Gt.T)

    def test_metric_diagonal_near_one(self):
        for i in range(6):
            self.assertAlmostEqual(self.Gt[i, i], 1.0, delta=0.02)

    def test_metric_inverse_roundtrip(self):
        product = self.Gt @ self.Gti
        np.testing.assert_array_almost_equal(product, np.eye(6), decimal=10)

    # ── Circumferences ────────────────────────────────────────────

    def test_L_electron_tube(self):
        self.assertAlmostEqual(self.L[0], 3.1955e4, delta=1.0)

    def test_L_electron_ring(self):
        self.assertAlmostEqual(self.L[1], 4.8416e3, delta=1.0)

    def test_L_aspect_ratio_e(self):
        self.assertAlmostEqual(self.L[0] / self.L[1], REF_R_E, places=10)

    def test_L_aspect_ratio_p(self):
        self.assertAlmostEqual(self.L[4] / self.L[5], REF_R_P, places=10)

    # ── Mode energies (non-self-consistent) ───────────────────────

    def test_electron_energy(self):
        from lib.ma import mode_energy
        E = mode_energy(ELECTRON, self.Gti, self.L)
        self.assertAlmostEqual(E, 0.51506, places=4)

    def test_proton_energy(self):
        from lib.ma import mode_energy
        E = mode_energy(PROTON, self.Gti, self.L)
        self.assertAlmostEqual(E, 945.459, places=0)

    def test_neutron_energy(self):
        from lib.ma import mode_energy
        E = mode_energy(NEUTRON, self.Gti, self.L)
        self.assertAlmostEqual(E, 946.762, places=0)

    def test_zero_mode_raises(self):
        from lib.ma import mode_energy
        # Zero mode should have E=0 (not an error, but test it)
        E = mode_energy((0, 0, 0, 0, 0, 0), self.Gti, self.L)
        self.assertAlmostEqual(E, 0.0)

    # ── Charge ────────────────────────────────────────────────────

    def test_electron_charge(self):
        from lib.ma import mode_charge
        self.assertEqual(mode_charge(ELECTRON), -1)

    def test_proton_charge(self):
        from lib.ma import mode_charge
        self.assertEqual(mode_charge(PROTON), +1)

    def test_neutron_charge(self):
        from lib.ma import mode_charge
        self.assertEqual(mode_charge(NEUTRON), 0)

    def test_neutrino_charge(self):
        from lib.ma import mode_charge
        self.assertEqual(mode_charge(NEUTRINO), 0)

    def test_charge_is_linear(self):
        """Q = -n1 + n5, so (2, 0, 0, 0, 3, 0) → -2 + 3 = +1."""
        from lib.ma import mode_charge
        self.assertEqual(mode_charge((2, 0, 0, 0, 3, 0)), +1)

    # ── Spin ──────────────────────────────────────────────────────

    def test_electron_spin(self):
        from lib.ma import mode_spin
        self.assertEqual(mode_spin(ELECTRON), 1)  # one odd tube winding

    def test_proton_spin(self):
        from lib.ma import mode_spin
        self.assertEqual(mode_spin(PROTON), 1)

    def test_neutron_spin(self):
        from lib.ma import mode_spin
        # NEUTRON = (0, -2, 1, 0, 0, 2): tube indices 0,2,4 = (0, 1, 0)
        # only n3=1 is odd → 1 spin-½ contribution
        self.assertEqual(mode_spin(NEUTRON), 1)

    def test_neutrino_spin(self):
        from lib.ma import mode_spin
        self.assertEqual(mode_spin(NEUTRINO), 1)

    def test_boson_spin(self):
        from lib.ma import mode_spin
        self.assertEqual(mode_spin((0, 2, 0, 0, 0, 0)), 0)

    def test_spin_label(self):
        from lib.ma import mode_spin_label
        self.assertEqual(mode_spin_label(ELECTRON), "fermion (½)")
        self.assertEqual(mode_spin_label((0, 2, 0, 0, 0, 0)), "boson")

    # ── Negative E² guard ─────────────────────────────────────────

    def test_negative_E2_raises(self):
        """A non-positive-definite inverse metric should raise."""
        from lib.ma import mode_energy
        bad_Gti = -np.eye(6)
        L = np.ones(6)
        with self.assertRaises(ValueError):
            mode_energy((1, 0, 0, 0, 0, 0), bad_Gti, L)


# ════════════════════════════════════════════════════════════════════
#  ma.py — scan_modes
# ════════════════════════════════════════════════════════════════════

class TestScan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from lib.ma import build_scaled_metric
        cls.Gt, cls.Gti, cls.L, cls.info = build_scaled_metric(
            r_e=REF_R_E, r_nu=REF_R_NU, r_p=REF_R_P,
            sigma_ep=REF_SIGMA_EP)

    def test_scan_returns_sorted(self):
        from lib.ma import scan_modes
        modes = scan_modes(self.Gti, self.L, n_max=2, E_max_MeV=100)
        energies = [m['E_MeV'] for m in modes]
        self.assertEqual(energies, sorted(energies))

    def test_scan_excludes_zero(self):
        from lib.ma import scan_modes
        modes = scan_modes(self.Gti, self.L, n_max=1, E_max_MeV=1e6)
        for m in modes:
            self.assertFalse(all(ni == 0 for ni in m['n']))

    def test_scan_respects_energy_ceiling(self):
        from lib.ma import scan_modes
        ceiling = 50.0
        modes = scan_modes(self.Gti, self.L, n_max=2, E_max_MeV=ceiling)
        for m in modes:
            self.assertLessEqual(m['E_MeV'], ceiling)


# ════════════════════════════════════════════════════════════════════
#  ma_solver.py — self-consistent metric
# ════════════════════════════════════════════════════════════════════

class TestSolver(unittest.TestCase):

    def test_self_consistent_converges(self):
        from lib.ma_solver import self_consistent_metric
        r = self_consistent_metric(
            r_e=REF_R_E, r_nu=REF_R_NU, r_p=REF_R_P,
            sigma_ep=REF_SIGMA_EP)
        self.assertTrue(r['converged'])
        self.assertLessEqual(r['iterations'], 10)

    def test_self_consistent_electron_exact(self):
        from lib.ma_solver import self_consistent_metric
        from lib.ma import mode_energy, M_E_MEV
        r = self_consistent_metric(
            r_e=REF_R_E, r_nu=REF_R_NU, r_p=REF_R_P,
            sigma_ep=REF_SIGMA_EP)
        E_e = mode_energy(ELECTRON, r['Gtilde_inv'], r['L'])
        self.assertAlmostEqual(E_e, M_E_MEV, places=6)

    def test_self_consistent_proton_exact(self):
        from lib.ma_solver import self_consistent_metric
        from lib.ma import mode_energy, M_P_MEV
        r = self_consistent_metric(
            r_e=REF_R_E, r_nu=REF_R_NU, r_p=REF_R_P,
            sigma_ep=REF_SIGMA_EP)
        E_p = mode_energy(PROTON, r['Gtilde_inv'], r['L'])
        self.assertAlmostEqual(E_p, M_P_MEV, places=6)

    def test_self_consistent_not_positive_definite(self):
        from lib.ma_solver import self_consistent_metric
        r = self_consistent_metric(
            r_e=REF_R_E, r_nu=REF_R_NU, r_p=REF_R_P,
            sigma_ep=0.9)  # too large
        self.assertFalse(r['converged'])

    def test_find_modes_electron(self):
        from lib.ma_solver import find_modes
        results = find_modes(
            target_mass_MeV=0.511,
            target_charge=-1,
            target_spin_halves=1,
            r_e=REF_R_E, r_nu=REF_R_NU, r_p=REF_R_P,
            sigma_ep=REF_SIGMA_EP,
            n_max=3, mass_tolerance_MeV=1.0,
            self_consistent=True)
        self.assertGreater(len(results), 0)
        best = results[0]
        self.assertEqual(best['charge'], -1)
        self.assertAlmostEqual(best['E_MeV'], 0.511, places=3)


# ════════════════════════════════════════════════════════════════════
#  ma.py — epstein_zeta
# ════════════════════════════════════════════════════════════════════

class TestEpstein(unittest.TestCase):

    def test_positive(self):
        """Zeta sum of positive-definite quadratic form is positive."""
        from lib.ma import build_scaled_metric, epstein_zeta
        Gt, Gti, L, _ = build_scaled_metric(
            r_e=REF_R_E, r_nu=REF_R_NU, r_p=REF_R_P)
        Z = epstein_zeta(Gti, L, s_exp=5, n_max=2)
        self.assertGreater(Z, 0)


if __name__ == '__main__':
    unittest.main()
