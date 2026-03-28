"""
Regression tests for ma_model.py.

Validates the new Ma class against the same reference values
pinned in test_lib.py.  If both test suites pass, the new module
is a drop-in replacement for legacy ma.py + ma_solver.py.

Run from studies/:
    python -m unittest lib.test_ma_model -v
"""

import math
import sys
import unittest
import numpy as np

if "studies" not in sys.path:
    sys.path.insert(0, "studies")

from lib.ma_model import Ma, alpha_ma, solve_shear_for_alpha, Mode

# Standard reference geometry
REF = dict(r_e=6.6, r_nu=5.0, r_p=8.906, sigma_ep=-0.0906)

# Reference modes
ELECTRON = (1, 2, 0, 0, 0, 0)
PROTON   = (0, 0, 0, 0, 1, 2)
NEUTRON  = (0, -2, 1, 0, 0, 2)
NEUTRINO = (0, 0, 1, 1, 0, 0)


# ════════════════════════════════════════════════════════════════════
#  Alpha formula
# ════════════════════════════════════════════════════════════════════

class TestAlphaModel(unittest.TestCase):

    def test_roundtrip(self):
        from lib.constants import alpha
        for r in [0.5, 2.0, 6.6, 8.906, 20.0]:
            s = solve_shear_for_alpha(r)
            if s is not None:
                self.assertAlmostEqual(
                    alpha_ma(r, s), alpha, places=10,
                    msg=f"roundtrip failed at r={r}")

    def test_no_solution_small_r(self):
        self.assertIsNone(solve_shear_for_alpha(0.1))


# ════════════════════════════════════════════════════════════════════
#  Ma construction
# ════════════════════════════════════════════════════════════════════

class TestConstruction(unittest.TestCase):

    def test_basic(self):
        m = Ma(**REF)
        self.assertAlmostEqual(m.r_e, 6.6)
        self.assertAlmostEqual(m.r_p, 8.906)

    def test_rejects_bad_r(self):
        with self.assertRaises(ValueError):
            Ma(r_e=0.1, r_nu=5.0, r_p=6.6)

    def test_rejects_bad_sigma(self):
        with self.assertRaises(ValueError):
            Ma(r_e=6.6, r_nu=5.0, r_p=8.906, sigma_ep=0.9)

    def test_immutable(self):
        m = Ma(**REF)
        with self.assertRaises(AttributeError):
            m.r_e = 7.0
        # Can't add new attributes (slots enforced)
        with self.assertRaises(AttributeError):
            m.new_attr = 42

    def test_with_params(self):
        m1 = Ma(**REF)
        m2 = m1.with_params(sigma_ep=-0.10)
        self.assertAlmostEqual(m2.sigma_ep, -0.10)
        # Original unchanged
        self.assertAlmostEqual(m1.sigma_ep, -0.0906)


# ════════════════════════════════════════════════════════════════════
#  Metric properties — match legacy ma.py values exactly
# ════════════════════════════════════════════════════════════════════

class TestMetric(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.m = Ma(**REF)

    def test_positive_definite(self):
        self.assertTrue(self.m.is_positive_definite())

    def test_symmetric(self):
        np.testing.assert_array_almost_equal(self.m.Gt, self.m.Gt.T)

    def test_diagonal_near_one(self):
        for i in range(6):
            self.assertAlmostEqual(self.m.Gt[i, i], 1.0, delta=0.02)

    def test_inverse_roundtrip(self):
        product = self.m.Gt @ self.m.Gti
        np.testing.assert_array_almost_equal(product, np.eye(6), decimal=10)

    def test_L_electron_tube(self):
        self.assertAlmostEqual(self.m.L[0], 3.1955e4, delta=1.0)

    def test_L_electron_ring(self):
        self.assertAlmostEqual(self.m.L[1], 4.8416e3, delta=1.0)

    def test_L_aspect_e(self):
        self.assertAlmostEqual(self.m.L[0] / self.m.L[1], 6.6, places=10)

    def test_L_aspect_p(self):
        self.assertAlmostEqual(self.m.L[4] / self.m.L[5], 8.906, places=10)


# ════════════════════════════════════════════════════════════════════
#  Mode energies — match legacy values
# ════════════════════════════════════════════════════════════════════

class TestEnergy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.m = Ma(**REF)

    def test_electron(self):
        self.assertAlmostEqual(self.m.energy(ELECTRON), 0.51506, places=4)

    def test_proton(self):
        self.assertAlmostEqual(self.m.energy(PROTON), 945.459, places=0)

    def test_neutron(self):
        self.assertAlmostEqual(self.m.energy(NEUTRON), 946.762, places=0)

    def test_zero_mode(self):
        self.assertAlmostEqual(self.m.energy((0,0,0,0,0,0)), 0.0)

    def test_negative_E2_raises(self):
        # Construct a Ma from a bad inverse metric
        m = Ma.from_legacy(Gtilde_inv=-np.eye(6), L=np.ones(6))
        with self.assertRaises(ValueError):
            m.energy((1, 0, 0, 0, 0, 0))


# ════════════════════════════════════════════════════════════════════
#  Charge and spin
# ════════════════════════════════════════════════════════════════════

class TestChargeAndSpin(unittest.TestCase):

    def test_electron_charge(self):
        self.assertEqual(Ma.charge(ELECTRON), -1)

    def test_proton_charge(self):
        self.assertEqual(Ma.charge(PROTON), +1)

    def test_neutron_charge(self):
        self.assertEqual(Ma.charge(NEUTRON), 0)

    def test_charge_linear(self):
        self.assertEqual(Ma.charge((2, 0, 0, 0, 3, 0)), +1)

    def test_electron_spin(self):
        self.assertEqual(Ma.spin(ELECTRON), 1)

    def test_proton_spin(self):
        self.assertEqual(Ma.spin(PROTON), 1)

    def test_neutron_spin(self):
        # (0, -2, 1, 0, 0, 2): tube indices 0,2,4 = (0, 1, 0) → 1 odd
        self.assertEqual(Ma.spin(NEUTRON), 1)

    def test_boson_spin(self):
        self.assertEqual(Ma.spin((0, 2, 0, 0, 0, 0)), 0)

    def test_spin_label(self):
        self.assertEqual(Ma.spin_label(ELECTRON), "fermion (½)")
        self.assertEqual(Ma.spin_label((0, 2, 0, 0, 0, 0)), "boson")


# ════════════════════════════════════════════════════════════════════
#  Self-consistent metric
# ════════════════════════════════════════════════════════════════════

class TestSelfConsistent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.m = Ma(**REF, self_consistent=True)

    def test_converged(self):
        self.assertTrue(self.m.converged)
        self.assertLessEqual(self.m.iterations, 10)

    def test_electron_exact(self):
        from lib.ma_model import M_E_MEV
        self.assertAlmostEqual(self.m.energy(ELECTRON), M_E_MEV, places=6)

    def test_proton_exact(self):
        from lib.ma_model import M_P_MEV
        self.assertAlmostEqual(self.m.energy(PROTON), M_P_MEV, places=6)


# ════════════════════════════════════════════════════════════════════
#  Scanning
# ════════════════════════════════════════════════════════════════════

class TestScan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.m = Ma(**REF)

    def test_sorted(self):
        modes = self.m.scan_modes(n_max=2, E_max_MeV=100)
        energies = [m.E_MeV for m in modes]
        self.assertEqual(energies, sorted(energies))

    def test_excludes_zero(self):
        modes = self.m.scan_modes(n_max=1, E_max_MeV=1e6)
        for m in modes:
            self.assertFalse(all(ni == 0 for ni in m.n))

    def test_energy_ceiling(self):
        ceiling = 50.0
        modes = self.m.scan_modes(n_max=2, E_max_MeV=ceiling)
        for m in modes:
            self.assertLessEqual(m.E_MeV, ceiling)

    def test_charge_filter(self):
        modes = self.m.scan_modes(n_max=2, E_max_MeV=1000, charge=-1)
        for m in modes:
            self.assertEqual(m.charge, -1)

    def test_returns_mode_namedtuples(self):
        modes = self.m.scan_modes(n_max=1, E_max_MeV=100)
        if modes:
            m = modes[0]
            self.assertIsInstance(m, Mode)
            self.assertIsInstance(m.n, tuple)


# ════════════════════════════════════════════════════════════════════
#  Serialization
# ════════════════════════════════════════════════════════════════════

class TestSerialization(unittest.TestCase):

    def test_roundtrip(self):
        m1 = Ma(**REF)
        d = m1.to_dict()
        m2 = Ma.from_dict(d)
        self.assertAlmostEqual(m1.energy(ELECTRON), m2.energy(ELECTRON),
                               places=12)
        self.assertAlmostEqual(m1.energy(PROTON), m2.energy(PROTON),
                               places=12)

    def test_dict_has_required_keys(self):
        m = Ma(**REF)
        d = m.to_dict()
        for key in ('r_e', 'r_nu', 'r_p', 'sigma_ep', 's12', 'L'):
            self.assertIn(key, d)


# ════════════════════════════════════════════════════════════════════
#  Legacy interop
# ════════════════════════════════════════════════════════════════════

class TestLegacyInterop(unittest.TestCase):

    def test_from_legacy_energy_matches(self):
        """Ma.from_legacy reproduces energies from the legacy metric."""
        m_new = Ma(**REF)
        Gti, L = m_new.to_legacy()
        m_wrap = Ma.from_legacy(Gti, L)
        self.assertAlmostEqual(
            m_new.energy(ELECTRON), m_wrap.energy(ELECTRON), places=12)
        self.assertAlmostEqual(
            m_new.energy(PROTON), m_wrap.energy(PROTON), places=12)

    def test_to_legacy_roundtrip(self):
        m = Ma(**REF)
        Gti, L = m.to_legacy()
        self.assertEqual(Gti.shape, (6, 6))
        self.assertEqual(L.shape, (6,))
        np.testing.assert_array_almost_equal(Gti, m.Gti, decimal=12)


# ════════════════════════════════════════════════════════════════════
#  Cross-validate against legacy ma.py
# ════════════════════════════════════════════════════════════════════

class TestCrossValidation(unittest.TestCase):
    """
    Verify that ma_model.py produces identical results to legacy
    ma.py for the same inputs.
    """

    def test_energies_match_legacy(self):
        from lib.ma import build_scaled_metric, mode_energy
        # Legacy
        Gt_old, Gti_old, L_old, _ = build_scaled_metric(**REF)
        # New
        m = Ma(**REF)
        for mode in [ELECTRON, PROTON, NEUTRON, NEUTRINO,
                     (1, 1, 0, 0, 0, 0), (0, 0, 0, 0, 2, 1)]:
            E_old = mode_energy(mode, Gti_old, L_old)
            E_new = m.energy(mode)
            self.assertAlmostEqual(E_old, E_new, places=10,
                                   msg=f"Mismatch at mode {mode}")

    def test_L_matches_legacy(self):
        from lib.ma import build_scaled_metric
        _, _, L_old, _ = build_scaled_metric(**REF)
        m = Ma(**REF)
        np.testing.assert_array_almost_equal(m.L, L_old, decimal=10)

    def test_metric_matches_legacy(self):
        from lib.ma import build_scaled_metric
        Gt_old, Gti_old, _, _ = build_scaled_metric(**REF)
        m = Ma(**REF)
        np.testing.assert_array_almost_equal(m.Gt, Gt_old, decimal=10)
        np.testing.assert_array_almost_equal(m.Gti, Gti_old, decimal=10)

    def test_self_consistent_matches_legacy(self):
        from lib.ma_solver import self_consistent_metric
        from lib.ma import mode_energy as legacy_energy
        # Legacy
        r = self_consistent_metric(**REF)
        E_e_old = legacy_energy(ELECTRON, r['Gtilde_inv'], r['L'])
        E_p_old = legacy_energy(PROTON, r['Gtilde_inv'], r['L'])
        # New
        m = Ma(**REF, self_consistent=True)
        self.assertAlmostEqual(m.energy(ELECTRON), E_e_old, places=10)
        self.assertAlmostEqual(m.energy(PROTON), E_p_old, places=10)

    def test_scan_count_matches_legacy(self):
        from lib.ma import build_scaled_metric, scan_modes
        Gt_old, Gti_old, L_old, _ = build_scaled_metric(**REF)
        modes_old = scan_modes(Gti_old, L_old, n_max=2, E_max_MeV=100)
        m = Ma(**REF)
        modes_new = m.scan_modes(n_max=2, E_max_MeV=100)
        self.assertEqual(len(modes_old), len(modes_new))


# ════════════════════════════════════════════════════════════════════
#  Phase 2 stubs raise NotImplementedError
# ════════════════════════════════════════════════════════════════════

class TestStubs(unittest.TestCase):

    def test_fincke_pohst_stub(self):
        from lib.ma_model import _fincke_pohst_enumerate
        with self.assertRaises(NotImplementedError):
            _fincke_pohst_enumerate(np.eye(6), 1.0)


if __name__ == '__main__':
    unittest.main()
