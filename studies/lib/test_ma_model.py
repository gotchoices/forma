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

from lib.ma_model import (
    Ma, alpha_ma, solve_shear_for_alpha,
    Mode, EnergyDecomp, Target, FitResult,
)

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
#  Energy decomposition
# ════════════════════════════════════════════════════════════════════

class TestEnergyDecomp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.m = Ma(**REF)

    def test_total_matches_energy(self):
        """Decomposition total must equal energy()."""
        for mode in [ELECTRON, PROTON, NEUTRON, NEUTRINO,
                     (1, 1, 0, 0, 0, 0), (0, 0, 1, 2, 0, 0)]:
            d = self.m.energy_decomp(mode)
            self.assertAlmostEqual(d.total, self.m.energy(mode), places=10,
                                   msg=f"total mismatch at {mode}")

    def test_parts_sum_to_E2(self):
        """Sheet + cross terms must sum to E²."""
        for mode in [ELECTRON, PROTON, NEUTRON]:
            d = self.m.energy_decomp(mode)
            E2_parts = (d.e_sheet + d.nu_sheet + d.p_sheet
                        + d.ep_cross + d.enu_cross + d.nup_cross)
            E2_total = d.total**2
            self.assertAlmostEqual(E2_parts, E2_total, places=8,
                                   msg=f"sum mismatch at {mode}")

    def test_fractions_sum_to_one(self):
        for mode in [ELECTRON, PROTON, NEUTRON]:
            d = self.m.energy_decomp(mode)
            total_frac = sum(d.fractions.values())
            self.assertAlmostEqual(total_frac, 1.0, places=10,
                                   msg=f"fractions don't sum to 1 at {mode}")

    def test_electron_is_mostly_e_sheet(self):
        """Electron (1,2,0,0,0,0) should be dominated by the e block."""
        d = self.m.energy_decomp(ELECTRON)
        self.assertGreater(d.fractions['e'], 0.99)

    def test_proton_is_mostly_p_sheet(self):
        """Proton (0,0,0,0,1,2) should be dominated by the p block."""
        d = self.m.energy_decomp(PROTON)
        self.assertGreater(d.fractions['p'], 0.99)

    def test_neutron_has_cross_coupling(self):
        """Neutron (0,-2,1,0,0,2) has nonzero cross-coupling from σ_ep."""
        d = self.m.energy_decomp(NEUTRON)
        # p-sheet dominates (n₅=0 but n₆=2 gives proton ring energy)
        self.assertGreater(d.fractions['p'], 0.9)
        # Cross-coupling should be nonzero (σ_ep ≠ 0)
        self.assertNotAlmostEqual(d.ep_cross, 0.0, places=3)

    def test_returns_namedtuple(self):
        d = self.m.energy_decomp(ELECTRON)
        self.assertIsInstance(d, EnergyDecomp)

    def test_zero_mode(self):
        d = self.m.energy_decomp((0, 0, 0, 0, 0, 0))
        self.assertAlmostEqual(d.total, 0.0)

    def test_no_cross_shear_no_cross_terms(self):
        """With σ_ep = 0, cross terms should be negligible for pure modes."""
        m0 = Ma(r_e=6.6, r_nu=5.0, r_p=8.906)  # no cross-shears
        d = m0.energy_decomp(ELECTRON)
        self.assertAlmostEqual(d.ep_cross, 0.0, places=10)
        self.assertAlmostEqual(d.enu_cross, 0.0, places=10)


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
#  Jacobian — validated against finite differences
# ════════════════════════════════════════════════════════════════════

class TestJacobian(unittest.TestCase):
    """
    Validate the analytical Jacobian by comparing to central
    finite differences: ∂E/∂θ ≈ (E(θ+h) − E(θ−h)) / (2h).
    """

    def _finite_diff(self, mode, param, h=1e-6):
        """Numerical ∂E/∂param via central difference."""
        kw_plus = dict(**REF)
        kw_minus = dict(**REF)
        kw_plus[param] = REF.get(param, 0.0) + h
        kw_minus[param] = REF.get(param, 0.0) - h
        E_plus = Ma(**kw_plus).energy(mode)
        E_minus = Ma(**kw_minus).energy(mode)
        return (E_plus - E_minus) / (2 * h)

    def test_sigma_ep_electron(self):
        m = Ma(**REF)
        J = m.jacobian(ELECTRON)
        fd = self._finite_diff(ELECTRON, 'sigma_ep')
        self.assertAlmostEqual(J['sigma_ep'], fd, delta=abs(fd) * 0.01 + 1e-8)

    def test_sigma_ep_neutron(self):
        m = Ma(**REF)
        J = m.jacobian(NEUTRON)
        fd = self._finite_diff(NEUTRON, 'sigma_ep')
        self.assertAlmostEqual(J['sigma_ep'], fd, delta=abs(fd) * 0.01 + 1e-6)

    def test_sigma_enu(self):
        # sigma_enu = 0 in REF, so perturb around a nonzero value
        ref2 = dict(**REF, sigma_enu=0.01)
        m = Ma(**ref2)
        J = m.jacobian(NEUTRON)
        kw_p = dict(**ref2); kw_p['sigma_enu'] += 1e-6
        kw_m = dict(**ref2); kw_m['sigma_enu'] -= 1e-6
        fd = (Ma(**kw_p).energy(NEUTRON) - Ma(**kw_m).energy(NEUTRON)) / 2e-6
        self.assertAlmostEqual(J['sigma_enu'], fd, delta=abs(fd) * 0.01 + 1e-6)

    def test_r_e_electron(self):
        m = Ma(**REF)
        J = m.jacobian(ELECTRON)
        fd = self._finite_diff(ELECTRON, 'r_e', h=1e-5)
        self.assertAlmostEqual(J['r_e'], fd, delta=abs(fd) * 0.02 + 1e-6)

    def test_r_p_proton(self):
        m = Ma(**REF)
        J = m.jacobian(PROTON)
        fd = self._finite_diff(PROTON, 'r_p', h=1e-5)
        self.assertAlmostEqual(J['r_p'], fd, delta=abs(fd) * 0.02 + 1e-6)

    def test_r_p_neutron(self):
        m = Ma(**REF)
        J = m.jacobian(NEUTRON)
        fd = self._finite_diff(NEUTRON, 'r_p', h=1e-5)
        self.assertAlmostEqual(J['r_p'], fd, delta=abs(fd) * 0.02 + 1e-6)

    def test_r_nu(self):
        m = Ma(**REF)
        J = m.jacobian(NEUTRINO)
        fd = self._finite_diff(NEUTRINO, 'r_nu', h=1e-5)
        self.assertAlmostEqual(J['r_nu'], fd, delta=abs(fd) * 0.02 + 1e-8)

    def test_zero_mode(self):
        m = Ma(**REF)
        J = m.jacobian((0, 0, 0, 0, 0, 0))
        for v in J.values():
            self.assertAlmostEqual(v, 0.0)

    def test_returns_all_params(self):
        m = Ma(**REF)
        J = m.jacobian(ELECTRON)
        for key in ('r_e', 'r_nu', 'r_p', 'sigma_ep', 'sigma_enu', 'sigma_nup'):
            self.assertIn(key, J)


class TestSensitivity(unittest.TestCase):

    def test_returns_string(self):
        m = Ma(**REF)
        s = m.sensitivity(ELECTRON)
        self.assertIsInstance(s, str)
        self.assertIn('MeV', s)

    def test_contains_all_params(self):
        m = Ma(**REF)
        s = m.sensitivity(PROTON)
        for name in ('r_e', 'r_p', 'σ_ep'):
            self.assertIn(name, s)

    def test_strength_labels(self):
        m = Ma(**REF)
        s = m.sensitivity(NEUTRON)
        # At least one parameter should be non-negligible for the neutron
        self.assertTrue(
            any(w in s for w in ('strong', 'moderate', 'weak')),
            "Expected at least one non-negligible sensitivity")


# ════════════════════════════════════════════════════════════════════
#  Inverse solver (fit)
# ════════════════════════════════════════════════════════════════════

class TestFit(unittest.TestCase):

    def test_recover_sigma_ep_from_neutron(self):
        """
        Fit sigma_ep using the neutron mass alone.
        Should recover σ_ep ≈ -0.0906 (the R27 value).
        Note: r_e=6.6 is used here as a test fixture, not a physics claim.
        r_e is free (R30 F11); r_p=8.906 is pinned (R27).
        """
        result = Ma.fit(
            targets=[Target(n=NEUTRON, mass_MeV=939.565)],
            free_params=['sigma_ep'],
            fixed_params={'r_e': 6.6, 'r_nu': 5.0, 'r_p': 8.906},
        )
        self.assertTrue(result.converged)
        self.assertAlmostEqual(result.params['sigma_ep'], -0.0906, delta=0.002)
        self.assertAlmostEqual(result.residuals[0], 0.0, delta=0.01)
        self.assertIsInstance(result.ma, Ma)

    def test_recover_r_p_and_sigma_ep(self):
        """
        Fit r_p and sigma_ep from neutron + muon.
        The muon mode from R27 is (-1, 5, 0, 0, -2, 0).
        Should recover r_p ≈ 8.906, σ_ep ≈ -0.0906.
        """
        MUON = (-1, 5, 0, 0, -2, 0)
        result = Ma.fit(
            targets=[
                Target(n=NEUTRON, mass_MeV=939.565),
                Target(n=MUON, mass_MeV=105.658),
            ],
            free_params=['r_p', 'sigma_ep'],
            fixed_params={'r_e': 6.6, 'r_nu': 5.0},
        )
        self.assertTrue(result.converged,
                        f"Did not converge in {result.iterations} iterations. "
                        f"Residuals: {result.residuals}")
        self.assertAlmostEqual(result.params['r_p'], 8.906, delta=0.05)
        self.assertAlmostEqual(result.params['sigma_ep'], -0.0906, delta=0.005)

    def test_returns_fit_result(self):
        result = Ma.fit(
            targets=[Target(n=ELECTRON, mass_MeV=0.511)],
            free_params=['r_e'],
            fixed_params={'r_nu': 5.0, 'r_p': 8.906},
        )
        self.assertIsInstance(result, FitResult)
        self.assertIn('r_e', result.params)
        self.assertEqual(result.jacobian.shape[0], 1)  # 1 target
        self.assertEqual(result.jacobian.shape[1], 1)  # 1 param

    def test_covariance_square_system(self):
        """2 targets, 2 params → covariance matrix should exist."""
        MUON = (-1, 5, 0, 0, -2, 0)
        result = Ma.fit(
            targets=[
                Target(n=NEUTRON, mass_MeV=939.565),
                Target(n=MUON, mass_MeV=105.658),
            ],
            free_params=['r_p', 'sigma_ep'],
            fixed_params={'r_e': 6.6, 'r_nu': 5.0},
        )
        if result.converged:
            self.assertIsNotNone(result.cov)
            self.assertEqual(result.cov.shape, (2, 2))

    def test_underdetermined_null_space(self):
        """3 free params, 1 target → 2D null space."""
        result = Ma.fit(
            targets=[Target(n=NEUTRON, mass_MeV=939.565)],
            free_params=['r_p', 'sigma_ep', 'sigma_enu'],
            fixed_params={'r_e': 6.6, 'r_nu': 5.0},
        )
        if result.converged:
            self.assertIsNotNone(result.null_space)
            # Null space should have 2 columns (3 params - 1 constraint)
            self.assertEqual(result.null_space.shape[1], 2)

    def test_invalid_param_raises(self):
        with self.assertRaises(ValueError):
            Ma.fit(
                targets=[Target(n=ELECTRON, mass_MeV=0.511)],
                free_params=['invalid_param'],
            )

    def test_residuals_at_known_geometry(self):
        """
        If we fit at the geometry that already matches, residuals
        should be near zero and the solver should converge quickly.
        """
        # Build Ma at known good point, get its energies
        m = Ma(r_e=6.6, r_nu=5.0, r_p=8.906, sigma_ep=-0.0906,
               self_consistent=True)
        E_neutron = m.energy(NEUTRON)

        result = Ma.fit(
            targets=[Target(n=NEUTRON, mass_MeV=E_neutron)],
            free_params=['sigma_ep'],
            fixed_params={'r_e': 6.6, 'r_nu': 5.0, 'r_p': 8.906},
        )
        self.assertTrue(result.converged)
        self.assertAlmostEqual(result.params['sigma_ep'], -0.0906, delta=0.001)


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
