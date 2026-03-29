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


# ════════════════════════════════════════════════════════════════════
#  Dynamic model (α-impedance) — Phase 6 tests
# ════════════════════════════════════════════════════════════════════

from lib.ma_model import (
    PressureHarmonics, WallShape, DynamicCorrection,
    _compute_pressure_harmonics,
)


class TestDynamicBackwardCompat(unittest.TestCase):
    """dynamic=False must produce identical results to pre-dynamic code."""

    @classmethod
    def setUpClass(cls):
        cls.m_static = Ma(**REF)
        cls.m_dynamic_off = Ma(**REF, dynamic=False)

    def test_energy_identical(self):
        for mode in [ELECTRON, PROTON, NEUTRON, NEUTRINO]:
            self.assertAlmostEqual(
                self.m_static.energy(mode),
                self.m_dynamic_off.energy(mode),
                places=12, msg=f"mismatch at {mode}")

    def test_dynamic_flag_false_by_default(self):
        self.assertFalse(self.m_static.dynamic)

    def test_scan_delta_none_when_static(self):
        modes = self.m_static.scan_modes(n_max=1, E_max_MeV=100)
        for m in modes:
            self.assertIsNone(m.delta_E_MeV)


class TestPressureHarmonics(unittest.TestCase):

    def test_returns_namedtuple(self):
        m = Ma(**REF, dynamic=True)
        h = m.pressure_harmonics(1, 2, 8.906)
        self.assertIsInstance(h, PressureHarmonics)

    def test_r40_track11_match(self):
        """Proton (1,2) at r=8.906 must match Track 11 results."""
        m = Ma(**REF, dynamic=True)
        h = m.pressure_harmonics(1, 2, 8.906)
        c0 = h.c_k[0]
        self.assertGreater(c0, 0)
        rel_c2 = h.c_k[2] / c0
        self.assertAlmostEqual(rel_c2, 0.37, delta=0.02,
                               msg="|c₂/c₀| should be ≈0.37")
        self.assertGreater(h.delta_r_k[2], 0)
        self.assertAlmostEqual(h.delta_r_k[2], 6.7e-4, delta=1e-4,
                               msg="δr₂/a should be ≈6.7×10⁻⁴")

    def test_k2_dominant(self):
        """k=2 should be the dominant harmonic for (1,2) mode."""
        m = Ma(**REF, dynamic=True)
        h = m.pressure_harmonics(1, 2, 8.906)
        for k in range(3, len(h.delta_r_k)):
            self.assertGreater(h.delta_r_k[2], h.delta_r_k[k],
                               msg=f"k=2 should dominate over k={k}")

    def test_zero_for_no_tube_winding(self):
        h = _compute_pressure_harmonics(0, 2, 8.906)
        for k in range(len(h.delta_r_k)):
            self.assertAlmostEqual(h.delta_r_k[k], 0.0)

    def test_zero_for_no_ring_winding(self):
        h = _compute_pressure_harmonics(1, 0, 8.906)
        for k in range(len(h.delta_r_k)):
            self.assertAlmostEqual(h.delta_r_k[k], 0.0)

    def test_caching(self):
        """Same (n_tube, n_ring, r) should return cached result."""
        m = Ma(**REF, dynamic=True)
        h1 = m.pressure_harmonics(1, 2, 8.906)
        h2 = m.pressure_harmonics(1, 2, 8.906)
        self.assertIs(h1, h2)

    def test_sign_invariance(self):
        """Harmonics should be the same for ±n_tube, ±n_ring."""
        m = Ma(**REF, dynamic=True)
        h1 = m.pressure_harmonics(1, 2, 8.906)
        h2 = m.pressure_harmonics(-1, 2, 8.906)
        h3 = m.pressure_harmonics(1, -2, 8.906)
        np.testing.assert_array_almost_equal(h1.delta_r_k, h2.delta_r_k)
        np.testing.assert_array_almost_equal(h1.delta_r_k, h3.delta_r_k)


class TestWallShape(unittest.TestCase):

    def test_returns_namedtuple(self):
        m = Ma(**REF, dynamic=True)
        s = m.wall_shape(1, 2, 8.906)
        self.assertIsInstance(s, WallShape)

    def test_nearly_circular(self):
        """Wall should be close to r/a = 1 everywhere."""
        m = Ma(**REF, dynamic=True)
        s = m.wall_shape(1, 2, 8.906)
        self.assertTrue(np.all(s.r_over_a > 0.999))
        self.assertTrue(np.all(s.r_over_a < 1.001))

    def test_eccentricity_small(self):
        m = Ma(**REF, dynamic=True)
        s = m.wall_shape(1, 2, 8.906)
        self.assertLess(s.eccentricity, 0.001)
        self.assertGreater(s.eccentricity, 0.0)


class TestDynamicCorrection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.m = Ma(**REF, dynamic=True)

    def test_returns_namedtuple(self):
        corr = self.m.dynamic_correction(PROTON)
        self.assertIsInstance(corr, DynamicCorrection)

    def test_proton_correction_magnitude(self):
        """δE/E for proton should be ≈3.4×10⁻⁴ (from R40 Track 11)."""
        corr = self.m.dynamic_correction(PROTON)
        self.assertAlmostEqual(corr.delta_E_over_E, 3.4e-4, delta=1e-4)

    def test_perturbative_bound(self):
        """All corrections should be < α ≈ 0.0073."""
        from lib.constants import alpha
        for mode in [ELECTRON, PROTON, NEUTRON]:
            corr = self.m.dynamic_correction(mode)
            self.assertLess(abs(corr.delta_E_over_E), alpha,
                            msg=f"|δE/E| > α for mode {mode}")

    def test_no_tube_winding_zero_correction(self):
        """Modes with n_tube=0 on all sheets → zero correction."""
        mode = (0, 2, 0, 0, 0, 2)
        corr = self.m.dynamic_correction(mode)
        self.assertAlmostEqual(corr.delta_E_over_E, 0.0)

    def test_cpt_symmetry(self):
        """n and -n should have identical |δE/E|."""
        n_pos = (1, 2, 0, 0, 0, 0)
        n_neg = (-1, -2, 0, 0, 0, 0)
        c1 = self.m.dynamic_correction(n_pos)
        c2 = self.m.dynamic_correction(n_neg)
        self.assertAlmostEqual(abs(c1.delta_E_over_E),
                               abs(c2.delta_E_over_E), places=10)

    def test_per_sheet_dict(self):
        corr = self.m.dynamic_correction(PROTON)
        self.assertIn('p', corr.per_sheet)
        self.assertIn('e', corr.per_sheet)
        self.assertAlmostEqual(corr.per_sheet['e'], 0.0)
        self.assertGreater(corr.per_sheet['p'], 0.0)

    def test_dominant_k(self):
        """Proton (0,0,0,0,1,2): dominant k = 2|n₅| = 2."""
        corr = self.m.dynamic_correction(PROTON)
        self.assertEqual(corr.dominant_k, 2)


class TestDynamicEnergy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.m = Ma(**REF, dynamic=True)

    def test_dynamic_differs_from_static(self):
        E_dyn = self.m.energy(PROTON)
        E_st = self.m.energy_static(PROTON)
        self.assertNotAlmostEqual(E_dyn, E_st, places=6)
        self.assertAlmostEqual(E_dyn, E_st, delta=1.0)

    def test_energy_static_unchanged(self):
        """energy_static() should match Ma(dynamic=False).energy()."""
        m_off = Ma(**REF, dynamic=False)
        self.assertAlmostEqual(
            self.m.energy_static(PROTON),
            m_off.energy(PROTON), places=12)

    def test_scan_populates_delta(self):
        modes = self.m.scan_modes(n_max=1, E_max_MeV=1000)
        has_delta = any(m.delta_E_MeV is not None for m in modes)
        self.assertTrue(has_delta)


class TestFilterFactor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.m = Ma(**REF, dynamic=True)

    def test_fundamental_near_one(self):
        """(1,2) fundamental should have filter_factor ≈ 1."""
        ff = self.m.filter_factor(PROTON)
        self.assertAlmostEqual(ff, 1.0, delta=0.01)

    def test_higher_mode_suppressed(self):
        """Mode with higher tube winding should have ff < 1."""
        ff = self.m.filter_factor((0, 0, 0, 0, 3, 1))
        self.assertLess(ff, 0.1)


class TestDynamicSerialization(unittest.TestCase):

    def test_roundtrip_preserves_dynamic(self):
        m1 = Ma(**REF, dynamic=True)
        d = m1.to_dict()
        self.assertTrue(d['dynamic'])
        m2 = Ma.from_dict(d)
        self.assertTrue(m2.dynamic)
        self.assertAlmostEqual(
            m1.energy(PROTON), m2.energy(PROTON), places=8)

    def test_with_params_preserves_dynamic(self):
        m1 = Ma(**REF, dynamic=True)
        m2 = m1.with_params(sigma_ep=-0.10)
        self.assertTrue(m2.dynamic)

    def test_summary_includes_dynamic(self):
        m = Ma(**REF, dynamic=True)
        s = m.summary()
        self.assertIn('dynamic', s)
        self.assertIn('δE/E', s)

    def test_repr_includes_dynamic(self):
        m = Ma(**REF, dynamic=True)
        self.assertIn("dynamic='full'", repr(m))

    def test_shortcut_repr(self):
        m = Ma(**REF, dynamic='shortcut')
        self.assertIn("dynamic='shortcut'", repr(m))

    def test_shortcut_summary(self):
        m = Ma(**REF, dynamic='shortcut')
        self.assertIn('shortcut', m.summary())


# ════════════════════════════════════════════════════════════════════
#  Four-level dynamic hierarchy
# ════════════════════════════════════════════════════════════════════

class TestFourLevelHierarchy(unittest.TestCase):
    """Test the flat/elliptical/shortcut/full hierarchy."""

    @classmethod
    def setUpClass(cls):
        cls.m_flat = Ma(**REF, dynamic='flat')
        cls.m_ellip = Ma(**REF, dynamic='elliptical')
        cls.m_short = Ma(**REF, dynamic='shortcut')
        cls.m_full = Ma(**REF, dynamic='full')

    def test_flat_alias_off(self):
        """'off' should be accepted as alias for 'flat'."""
        m = Ma(**REF, dynamic='off')
        self.assertEqual(m.dynamic_method, 'flat')
        self.assertFalse(m.dynamic)

    def test_flat_alias_false(self):
        """False should map to 'flat'."""
        m = Ma(**REF, dynamic=False)
        self.assertEqual(m.dynamic_method, 'flat')

    def test_flat_method(self):
        self.assertEqual(self.m_flat.dynamic_method, 'flat')
        self.assertFalse(self.m_flat.dynamic)

    def test_elliptical_method(self):
        self.assertEqual(self.m_ellip.dynamic_method, 'elliptical')
        self.assertTrue(self.m_ellip.dynamic)

    def test_elliptical_repr(self):
        self.assertIn("dynamic='elliptical'", repr(self.m_ellip))

    def test_elliptical_summary(self):
        self.assertIn('elliptical', self.m_ellip.summary())

    def test_flat_energy_equals_static(self):
        """Flat model should give the same energy as energy_static."""
        for mode in [ELECTRON, PROTON, NEUTRON]:
            self.assertEqual(self.m_flat.energy(mode),
                             self.m_flat.energy_static(mode))

    def test_elliptical_correction_uniform(self):
        """Elliptical applies the SAME per-sheet correction to all modes."""
        corr_e = self.m_ellip.dynamic_correction(ELECTRON)
        corr_11 = self.m_ellip.dynamic_correction((1, 1, 0, 0, 0, 0))
        self.assertAlmostEqual(corr_e.per_sheet['e'],
                               corr_11.per_sheet['e'], places=15,
                               msg="Elliptical should give same e-sheet "
                                   "correction regardless of mode")

    def test_elliptical_differs_from_shortcut_for_nonstandard_modes(self):
        """Elliptical and shortcut should differ for modes != (1,2)."""
        mode_11 = (1, 1, 0, 0, 0, 0)
        E_ellip = self.m_ellip.energy(mode_11)
        E_short = self.m_short.energy(mode_11)
        self.assertNotAlmostEqual(E_ellip, E_short, places=10,
                                  msg="Elliptical and shortcut should differ "
                                      "for (1,1) mode")

    def test_elliptical_equals_shortcut_for_fundamental(self):
        """For the (1,2) fundamental, elliptical = shortcut."""
        E_ellip = self.m_ellip.energy(ELECTRON)
        E_short = self.m_short.energy(ELECTRON)
        self.assertAlmostEqual(E_ellip, E_short, places=12,
                               msg="Elliptical and shortcut should agree "
                                   "for the (1,2) fundamental")

    def test_energy_ordering_electron(self):
        """E_flat < E_elliptical ≈ E_shortcut ≈ E_full for electron."""
        E_f = self.m_flat.energy(ELECTRON)
        E_e = self.m_ellip.energy(ELECTRON)
        E_s = self.m_short.energy(ELECTRON)
        E_d = self.m_full.energy(ELECTRON)
        self.assertLess(E_f, E_e)
        self.assertAlmostEqual(E_e, E_s, places=10)
        self.assertAlmostEqual(E_s, E_d, places=6)

    def test_elliptical_correction_nonzero_for_ring_only(self):
        """Ring-only mode (0,1,0,0,0,0) gets correction in elliptical
        but NOT in shortcut (n_tube=0 → no coupling)."""
        mode_ring = (0, 1, 0, 0, 0, 0)
        corr_ellip = self.m_ellip.dynamic_correction(mode_ring)
        corr_short = self.m_short.dynamic_correction(mode_ring)
        self.assertGreater(abs(corr_ellip.delta_E_over_E), 1e-6,
                           msg="Elliptical should correct ring-only modes")
        self.assertAlmostEqual(corr_short.delta_E_over_E, 0.0, places=15,
                               msg="Shortcut should NOT correct ring-only modes")

    def test_serialization_roundtrip_elliptical(self):
        """Elliptical should survive to_dict → Ma(**d)."""
        d = self.m_ellip.to_dict()
        constructor_keys = {'r_e', 'r_nu', 'r_p', 'sigma_ep',
                            'sigma_enu', 'sigma_nup',
                            'self_consistent', 'dynamic'}
        m2 = Ma(**{k: v for k, v in d.items() if k in constructor_keys})
        self.assertEqual(m2.dynamic_method, 'elliptical')

    def test_with_params_preserves_elliptical(self):
        m2 = self.m_ellip.with_params(r_e=7.0)
        self.assertEqual(m2.dynamic_method, 'elliptical')

    def test_invalid_dynamic_raises(self):
        with self.assertRaises(ValueError):
            Ma(**REF, dynamic='bogus')


# ════════════════════════════════════════════════════════════════════
#  Full vs shortcut solve
# ════════════════════════════════════════════════════════════════════

class TestFullVsShortcut(unittest.TestCase):
    """Verify the iterative force-balance solve vs one-shot shortcut."""

    @classmethod
    def setUpClass(cls):
        cls.m_full = Ma(**REF, dynamic='full')
        cls.m_short = Ma(**REF, dynamic='shortcut')
        cls.m_static = Ma(**REF, dynamic=False)

    def test_dynamic_method_property(self):
        self.assertEqual(self.m_full.dynamic_method, 'full')
        self.assertEqual(self.m_short.dynamic_method, 'shortcut')
        self.assertEqual(self.m_static.dynamic_method, 'flat')

    def test_dynamic_bool_property(self):
        self.assertTrue(self.m_full.dynamic)
        self.assertTrue(self.m_short.dynamic)
        self.assertFalse(self.m_static.dynamic)

    def test_full_and_shortcut_energies_agree(self):
        """Full and shortcut should agree to O(α⁴) ≈ 3×10⁻⁹."""
        for mode in [ELECTRON, PROTON, NEUTRON]:
            E_full = self.m_full.energy(mode)
            E_short = self.m_short.energy(mode)
            rel_diff = abs(E_full - E_short) / E_full
            self.assertLess(rel_diff, 1e-6,
                            msg=f"Full vs shortcut differ by {rel_diff:.2e} "
                                f"for {mode}")

    def test_full_harmonics_differ_from_shortcut(self):
        """Full-solve harmonics should be slightly different (non-trivial)."""
        h_full = self.m_full.pressure_harmonics(1, 2, 8.906)
        h_short = self.m_short.pressure_harmonics(1, 2, 8.906)
        diff = abs(h_full.delta_r_k[2] - h_short.delta_r_k[2])
        self.assertGreater(diff, 0,
                           msg="Full and shortcut should not be identical")
        self.assertLess(diff, 1e-5,
                        msg="Difference should be small (O(α²) × δr)")

    def test_full_converged_is_self_consistent(self):
        """If we run one more iteration on the full result, nothing changes."""
        h = self.m_full.pressure_harmonics(1, 2, 8.906)
        h2 = _compute_pressure_harmonics(
            1, 2, 8.906, shape_delta=h.delta_r_k, shape_phi=h.phi_k)
        np.testing.assert_array_almost_equal(
            h.delta_r_k, h2.delta_r_k, decimal=9,
            err_msg="Full solve should be self-consistent to ~10⁻¹⁰")

    def test_shortcut_is_iteration_zero(self):
        """Shortcut should equal circular-cross-section computation."""
        h_short = self.m_short.pressure_harmonics(1, 2, 8.906)
        h_circ = _compute_pressure_harmonics(1, 2, 8.906)
        np.testing.assert_array_almost_equal(
            h_short.delta_r_k, h_circ.delta_r_k, decimal=12,
            err_msg="Shortcut should be identical to circular computation")

    def test_static_energy_independent_of_method(self):
        """energy_static() should be the same regardless of dynamic method."""
        for mode in [ELECTRON, PROTON]:
            E_full_st = self.m_full.energy_static(mode)
            E_short_st = self.m_short.energy_static(mode)
            E_static = self.m_static.energy(mode)
            self.assertAlmostEqual(E_full_st, E_static, places=12)
            self.assertAlmostEqual(E_short_st, E_static, places=12)

    def test_with_params_preserves_method(self):
        m2 = self.m_full.with_params(sigma_ep=-0.10)
        self.assertEqual(m2.dynamic_method, 'full')
        m3 = self.m_short.with_params(sigma_ep=-0.10)
        self.assertEqual(m3.dynamic_method, 'shortcut')

    def test_to_dict_records_method(self):
        d_full = self.m_full.to_dict()
        d_short = self.m_short.to_dict()
        d_static = self.m_static.to_dict()
        self.assertEqual(d_full['dynamic'], 'full')
        self.assertEqual(d_short['dynamic'], 'shortcut')
        self.assertFalse(d_static['dynamic'])

    def test_from_dict_roundtrip_method(self):
        for m_orig in [self.m_full, self.m_short, self.m_static]:
            m_rt = Ma.from_dict(m_orig.to_dict())
            self.assertEqual(m_rt.dynamic_method, m_orig.dynamic_method)

    def test_invalid_dynamic_raises(self):
        with self.assertRaises(ValueError):
            Ma(**REF, dynamic='bogus')


# ════════════════════════════════════════════════════════════════════
#  Bug tests — issues found during code review
# ════════════════════════════════════════════════════════════════════

class TestBug1_PureTubeWinding(unittest.TestCase):
    """
    Issue: _compute_pressure_harmonics returns null for n_ring=0.
    A pure tube mode (1,0) still follows a 3D path with curvature
    and should have nonzero pressure harmonics.
    """

    def test_pure_tube_mode_has_pressure(self):
        """Mode (1,0) — tube winding only — should have nonzero pressure."""
        m = Ma(**REF, dynamic=True)
        # (1,0) on a torus still curves in 3D (it's a circle around the tube)
        harm = m.pressure_harmonics(n_tube=1, n_ring=0, r=8.906)
        # Current code returns all zeros — this test should FAIL
        # A (1,0) mode circles the tube once, no ring advance.
        # On the embedding: x = (R+a cos t) cos 0, y = 0, z = a sin t
        # This is a circle of radius a in the xz-plane, centered at (R,0,0).
        # Curvature = 1/a (constant). Pressure should be uniform (k=0 only).
        self.assertNotEqual(harm.c_k[0], 0.0,
                            "Pure tube mode (1,0) should have nonzero mean pressure")


class TestBug2_JacobianDynamicInconsistency(unittest.TestCase):
    """
    Issue: jacobian() calls self.energy(n) which includes dynamic
    correction when dynamic=True, but the derivative formulas only
    compute ∂E_static/∂θ. The E used in the denominator (2E) is
    dynamic, but the numerator is static-only.
    """

    def test_jacobian_uses_static_E_in_formula(self):
        """
        When dynamic=True, jacobian should either:
        (a) compute ∂E_dynamic/∂θ consistently, or
        (b) explicitly use E_static in the formula.

        Currently it mixes: E from energy() (dynamic) in the denominator,
        but ∂E²/∂θ from static formulas in the numerator.
        """
        m_static = Ma(**REF, dynamic=False)
        m_dynamic = Ma(**REF, dynamic=True)

        mode = PROTON
        J_static = m_static.jacobian(mode)
        J_dynamic = m_dynamic.jacobian(mode)

        # The static Jacobian should equal the dynamic Jacobian
        # for cross-shear derivatives (∂G̃/∂σ is the same),
        # adjusted only by the E ratio in the denominator.
        # If the code is inconsistent, the ratio won't match E_ratio.
        E_st = m_static.energy(mode)
        E_dyn = m_dynamic.energy(mode)
        E_ratio = E_st / E_dyn  # should be close to 1

        # For sigma_ep: the numerator (ñᵀ ∂G̃⁻¹/∂σ ñ) is identical.
        # So J_dynamic/J_static should equal E_st/E_dyn (from 1/(2E)).
        if abs(J_static['sigma_ep']) > 1e-10:
            actual_ratio = J_dynamic['sigma_ep'] / J_static['sigma_ep']
            # This SHOULD equal E_ratio if the code is consistent
            self.assertAlmostEqual(actual_ratio, E_ratio, places=4,
                                   msg="Jacobian mixes dynamic E with static ∂E²/∂θ")


class TestBug3_FilterFactorReference(unittest.TestCase):
    """
    Issue: _fundamental_dEE always uses the dominant sheet's r to
    compute the (1,2) reference, but for a mode that lives mostly
    on the neutrino sheet, the reference should use r_nu not r_p.
    """

    def test_neutrino_mode_uses_neutrino_r(self):
        """
        A pure neutrino mode's filter factor reference should use r_nu,
        not r_p or r_e.
        """
        m = Ma(**REF, dynamic=True)
        # Pure neutrino mode (0,0,1,2,0,0) — lives entirely on Ma_nu
        mode_nu = (0, 0, 1, 2, 0, 0)
        corr = m.dynamic_correction(mode_nu)

        # The reference should be (1,2) on the neutrino sheet at r_nu=5.0
        harm_nu_ref = m.pressure_harmonics(1, 2, m.r_nu)
        expected_fund_dEE = harm_nu_ref.delta_r_k[2] / 2.0

        # The filter factor should be |corr.delta_E_over_E| / expected_fund_dEE
        if expected_fund_dEE != 0:
            expected_ff = abs(corr.delta_E_over_E) / expected_fund_dEE
            # Current code may use a different sheet's r
            self.assertAlmostEqual(corr.filter_factor, expected_ff, places=4,
                                   msg="Filter factor uses wrong sheet's r for reference")


# ════════════════════════════════════════════════════════════════════
#  Missing test coverage
# ════════════════════════════════════════════════════════════════════

class TestDynamicEnergyMagnitude(unittest.TestCase):
    """Validate dynamic energy correction against R40 F25 numbers."""

    def test_proton_dEE_matches_R40(self):
        """R40 F25: δE/E ≈ 3.4×10⁻⁴ for the proton (1,2) mode."""
        m = Ma(**REF, dynamic=True)
        corr = m.dynamic_correction(PROTON)
        # R40 F25 table: δλ/λ = 3.4e-4 for n₁=1
        self.assertAlmostEqual(abs(corr.delta_E_over_E), 3.4e-4, delta=1e-4,
                               msg="Proton δE/E should be ~3.4×10⁻⁴ per R40 F25")

    def test_dynamic_energy_differs_from_static(self):
        """Dynamic energy should differ from static by the correction amount."""
        m = Ma(**REF, dynamic=True)
        E_dyn = m.energy(PROTON)
        E_stat = m.energy_static(PROTON)
        corr = m.dynamic_correction(PROTON)
        expected = E_stat * (1 + corr.delta_E_over_E)
        self.assertAlmostEqual(E_dyn, expected, places=10)
        self.assertNotAlmostEqual(E_dyn, E_stat, places=6,
                                  msg="Dynamic and static energies should differ")

    def test_mass_shift_proton(self):
        """R40 F25: δM ≈ 0.32 MeV for the proton."""
        m = Ma(**REF, dynamic=True)
        E_dyn = m.energy(PROTON)
        E_stat = m.energy_static(PROTON)
        dM = abs(E_dyn - E_stat)
        self.assertAlmostEqual(dM, 0.32, delta=0.1,
                               msg="Proton mass shift should be ~0.32 MeV per R40 F25")


class TestFitDynamic(unittest.TestCase):
    """Test the inverse solver with dynamic=True."""

    def test_fit_with_dynamic_converges(self):
        """fit() with dynamic=True should still recover r_p and σ_ep."""
        result = Ma.fit(
            targets=[Target(n=NEUTRON, mass_MeV=939.565)],
            free_params=['sigma_ep'],
            fixed_params={'r_e': 6.6, 'r_nu': 5.0, 'r_p': 8.906},
            dynamic=True,
        )
        self.assertTrue(result.converged,
                        f"Dynamic fit did not converge: residuals={result.residuals}")
        # σ_ep should be close to the static value (dynamic correction is small)
        self.assertAlmostEqual(result.params['sigma_ep'], -0.0906, delta=0.005)


class TestJacobianDynamicDerivatives(unittest.TestCase):
    """
    Verify jacobian() against finite differences when dynamic=True.
    This catches the inconsistency where the formula uses dynamic E
    but static ∂E²/∂θ.
    """

    def test_sigma_ep_dynamic_vs_finite_diff(self):
        m = Ma(**REF, dynamic=True)
        J = m.jacobian(PROTON)

        h = 1e-6
        kw_p = dict(**REF, dynamic=True); kw_p['sigma_ep'] += h
        kw_m = dict(**REF, dynamic=True); kw_m['sigma_ep'] -= h
        fd = (Ma(**kw_p).energy(PROTON) - Ma(**kw_m).energy(PROTON)) / (2 * h)

        self.assertAlmostEqual(J['sigma_ep'], fd,
                               delta=abs(fd) * 0.05 + 1e-6,
                               msg="Dynamic jacobian doesn't match finite diff for sigma_ep")


if __name__ == '__main__':
    unittest.main()
