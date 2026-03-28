"""
Tests for embedded.py — Phase 1 (core geometry, charge, fields, multipoles).

Run from studies/:
    python -m unittest lib.test_embedded -v
"""

import math
import sys
import unittest
import numpy as np

if "studies" not in sys.path:
    sys.path.insert(0, "studies")

from lib.embedded import (
    EmbeddedSheet, field_at, field_at_points, potential_at,
    field_energy, interaction_energy, interaction_force,
    interaction_sweep, near_field_correction,
)


# ── Test geometry: a simple torus with known dimensions ───────────
# L_tube = 2π, L_ring = 2π  →  R = 1, a = 1 (unit torus)
UNIT_SHEET = EmbeddedSheet(L_tube=2 * math.pi, L_ring=2 * math.pi)

# Thin torus: a << R
THIN_SHEET = EmbeddedSheet(L_tube=0.2 * math.pi, L_ring=20 * math.pi)


class TestConstruction(unittest.TestCase):

    def test_from_circumferences(self):
        s = EmbeddedSheet.from_circumferences(L_tube=10.0, L_ring=5.0)
        self.assertAlmostEqual(s.L_tube, 10.0)
        self.assertAlmostEqual(s.L_ring, 5.0)
        self.assertAlmostEqual(s.a, 10.0 / (2 * math.pi))
        self.assertAlmostEqual(s.R, 5.0 / (2 * math.pi))

    def test_from_ma(self):
        L = np.array([100.0, 10.0, 200.0, 40.0, 30.0, 3.0])
        e = EmbeddedSheet.from_ma(L, sheet='e')
        self.assertAlmostEqual(e.L_tube, 100.0)
        self.assertAlmostEqual(e.L_ring, 10.0)
        p = EmbeddedSheet.from_ma(L, sheet='p')
        self.assertAlmostEqual(p.L_tube, 30.0)
        self.assertAlmostEqual(p.L_ring, 3.0)
        nu = EmbeddedSheet.from_ma(L, sheet='nu')
        self.assertAlmostEqual(nu.L_tube, 200.0)

    def test_invalid_sheet(self):
        L = np.ones(6)
        with self.assertRaises(ValueError):
            EmbeddedSheet.from_ma(L, sheet='x')

    def test_negative_circumference(self):
        with self.assertRaises(ValueError):
            EmbeddedSheet(L_tube=-1.0, L_ring=1.0)

    def test_aspect_ratio(self):
        s = EmbeddedSheet(L_tube=6.0, L_ring=3.0)
        self.assertAlmostEqual(s.aspect, 2.0)

    def test_surface_area(self):
        self.assertAlmostEqual(
            UNIT_SHEET.surface_area, 4 * math.pi**2, places=8)

    def test_immutable(self):
        with self.assertRaises(AttributeError):
            UNIT_SHEET.R = 5.0


class TestGeometry(unittest.TestCase):

    def test_outer_equator(self):
        """θ₁=0, θ₂=0 → (R+a, 0, 0)."""
        p = UNIT_SHEET.torus_point(0.0, 0.0)
        np.testing.assert_allclose(p, [2.0, 0.0, 0.0], atol=1e-12)

    def test_inner_equator(self):
        """θ₁=π, θ₂=0 → (R−a, 0, 0)."""
        p = UNIT_SHEET.torus_point(math.pi, 0.0)
        np.testing.assert_allclose(p, [0.0, 0.0, 0.0], atol=1e-12)

    def test_top(self):
        """θ₁=π/2, θ₂=0 → (R, 0, a)."""
        p = UNIT_SHEET.torus_point(math.pi / 2, 0.0)
        np.testing.assert_allclose(p, [1.0, 0.0, 1.0], atol=1e-12)

    def test_vectorized(self):
        theta1 = np.array([0.0, math.pi])
        theta2 = np.array([0.0, 0.0])
        pts = UNIT_SHEET.torus_point(theta1, theta2)
        self.assertEqual(pts.shape, (2, 3))


class TestChargeDistribution(unittest.TestCase):

    def test_charge_conservation(self):
        """Total charge = Q."""
        pos, dq = UNIT_SHEET.charge_segments(1, 2, N=100, Q=-1.0)
        self.assertAlmostEqual(np.sum(dq), -1.0, places=12)

    def test_charge_conservation_with_weights(self):
        w = np.random.default_rng(42).random(100)
        pos, dq = UNIT_SHEET.charge_segments(1, 2, N=100, Q=3.0, weights=w)
        self.assertAlmostEqual(np.sum(dq), 3.0, places=12)

    def test_geodesic_shape(self):
        pos = UNIT_SHEET.geodesic(1, 2, N=200)
        self.assertEqual(pos.shape, (200, 3))

    def test_points_on_surface(self):
        """All geodesic points should satisfy (√(x²+y²) − R)² + z² = a²."""
        pos = UNIT_SHEET.geodesic(1, 2, N=500)
        rho = np.sqrt(pos[:, 0]**2 + pos[:, 1]**2)
        dist = (rho - UNIT_SHEET.R)**2 + pos[:, 2]**2
        np.testing.assert_allclose(dist, UNIT_SHEET.a**2, atol=1e-10)

    def test_phase_shift_changes_positions(self):
        pos0, _ = UNIT_SHEET.charge_segments(1, 2, N=50, phi=0.0)
        pos1, _ = UNIT_SHEET.charge_segments(1, 2, N=50, phi=math.pi)
        self.assertGreater(np.max(np.abs(pos0 - pos1)), 0.1)


class TestChargeDensity(unittest.TestCase):

    def test_integrates_to_Q(self):
        """∫∫ σ(θ₁,θ₂) × (R + a cos θ₁) × a dθ₁ dθ₂ ≈ Q."""
        Q = 2.5
        sigma = THIN_SHEET.charge_density(n1=1, n2=2, Q=Q)
        N = 200
        th1 = np.linspace(0, 2 * math.pi, N, endpoint=False)
        th2 = np.linspace(0, 2 * math.pi, N, endpoint=False)
        TH1, TH2 = np.meshgrid(th1, th2, indexing='ij')
        S = sigma(TH1, TH2)
        jacobian = (THIN_SHEET.R + THIN_SHEET.a * np.cos(TH1)) * THIN_SHEET.a
        dA = (2 * math.pi / N)**2
        integral = np.sum(S * jacobian) * dA
        self.assertAlmostEqual(integral, Q, delta=Q * 0.05)

    def test_returns_callable(self):
        sigma = UNIT_SHEET.charge_density(n1=1, n2=2)
        val = sigma(0.0, 0.0)
        self.assertIsInstance(float(val), float)

    def test_vectorized(self):
        sigma = UNIT_SHEET.charge_density(n1=1, n2=2)
        th1 = np.array([0.0, 1.0, 2.0])
        th2 = np.array([0.0, 0.5, 1.0])
        vals = sigma(th1, th2)
        self.assertEqual(vals.shape, (3,))


class TestFields(unittest.TestCase):

    def test_coulomb_far_field(self):
        """At large distance, field of a charge distribution → point charge."""
        pos, dq = THIN_SHEET.charge_segments(1, 2, N=200, Q=1.0)
        # Field at distance 1000 × R along x
        d = 1000 * THIN_SHEET.R
        E = field_at(pos, dq, point=[d, 0, 0])
        # Point charge: E_x = Q / d² (in natural units)
        E_point = 1.0 / d**2
        self.assertAlmostEqual(E[0], E_point, delta=E_point * 0.01)
        # Transverse components negligible
        self.assertAlmostEqual(E[1], 0.0, delta=E_point * 0.01)
        self.assertAlmostEqual(E[2], 0.0, delta=E_point * 0.01)

    def test_potential_far_field(self):
        """At large distance, potential → Q/r."""
        pos, dq = THIN_SHEET.charge_segments(1, 2, N=200, Q=1.0)
        d = 1000 * THIN_SHEET.R
        V = potential_at(pos, dq, point=[d, 0, 0])
        V_point = 1.0 / d
        self.assertAlmostEqual(V, V_point, delta=V_point * 0.01)

    def test_field_at_points_matches_scalar(self):
        pos, dq = THIN_SHEET.charge_segments(1, 2, N=100, Q=1.0)
        pts = np.array([[50.0, 0, 0], [0, 50.0, 0], [0, 0, 50.0]])
        E_batch = field_at_points(pos, dq, pts)
        for i in range(3):
            E_single = field_at(pos, dq, pts[i])
            np.testing.assert_allclose(E_batch[i], E_single, atol=1e-12)

    def test_self_energy_requires_eps(self):
        pos, dq = UNIT_SHEET.charge_segments(1, 2, N=50, Q=1.0)
        with self.assertRaises(ValueError):
            field_energy(pos, dq, eps=0.0)

    def test_self_energy_positive(self):
        """Self-energy of a positive charge distribution is positive."""
        pos, dq = UNIT_SHEET.charge_segments(1, 2, N=100, Q=1.0)
        U = field_energy(pos, dq, eps=0.01)
        self.assertGreater(U, 0)


class TestMultipoles(unittest.TestCase):

    def test_monopole(self):
        pos, dq = UNIT_SHEET.charge_segments(1, 2, N=100, Q=-1.0)
        Q = UNIT_SHEET.monopole(pos, dq)
        self.assertAlmostEqual(Q, -1.0, places=10)

    def test_dipole_shape(self):
        pos, dq = UNIT_SHEET.charge_segments(1, 2, N=100, Q=1.0)
        d = UNIT_SHEET.dipole(pos, dq)
        self.assertEqual(d.shape, (3,))

    def test_quadrupole_traceless(self):
        """Quadrupole tensor should be traceless."""
        pos, dq = UNIT_SHEET.charge_segments(1, 2, N=200, Q=1.0)
        Q_ij = UNIT_SHEET.quadrupole(pos, dq)
        self.assertAlmostEqual(np.trace(Q_ij), 0.0, places=8)

    def test_quadrupole_symmetric(self):
        pos, dq = UNIT_SHEET.charge_segments(1, 2, N=200, Q=1.0)
        Q_ij = UNIT_SHEET.quadrupole(pos, dq)
        np.testing.assert_allclose(Q_ij, Q_ij.T, atol=1e-12)

    def test_multipoles_monopole_matches(self):
        """l=0 multipole should agree with monopole()."""
        pos, dq = UNIT_SHEET.charge_segments(1, 2, N=100, Q=2.5)
        qlm = UNIT_SHEET.multipoles(pos, dq, l_max=1)
        # q_00 = Q / √(4π) for real spherical harmonics
        q00 = qlm[(0, 0)]
        Q_from_q00 = q00 * math.sqrt(4 * math.pi)
        self.assertAlmostEqual(Q_from_q00, 2.5, places=6)


class TestInteraction(unittest.TestCase):

    def test_coulomb_limit(self):
        """Two distributions far apart → Q1*Q2/d."""
        pos1, dq1 = THIN_SHEET.charge_segments(1, 2, N=100, Q=1.0)
        pos2, dq2 = THIN_SHEET.charge_segments(1, 2, N=100, Q=-1.0)
        d = 500 * THIN_SHEET.R
        pos2_shifted = pos2 + np.array([d, 0, 0])
        U = interaction_energy(pos1, dq1, pos2_shifted, dq2)
        U_coulomb = -1.0 / d
        self.assertAlmostEqual(U / U_coulomb, 1.0, delta=0.01)

    def test_symmetry_same_charges(self):
        """U(A,B) = U(B,A)."""
        pos1, dq1 = UNIT_SHEET.charge_segments(1, 2, N=50, Q=1.0)
        pos2, dq2 = UNIT_SHEET.charge_segments(1, 2, N=50, Q=1.0, phi=0.5)
        pos2_shifted = pos2 + np.array([10.0, 0, 0])
        U_ab = interaction_energy(pos1, dq1, pos2_shifted, dq2)
        U_ba = interaction_energy(pos2_shifted, dq2, pos1, dq1)
        self.assertAlmostEqual(U_ab, U_ba, places=10)


class TestSweep(unittest.TestCase):

    def test_sweep_shape(self):
        d_vals = np.array([10.0, 20.0, 30.0])
        phi_vals = np.array([0.0, math.pi])
        result = interaction_sweep(
            THIN_SHEET, THIN_SHEET, n1=1, n2=2, N=50,
            Q1=1.0, Q2=1.0,
            d_values=d_vals, phi_values=phi_vals)
        self.assertEqual(result.U.shape, (3, 2))
        self.assertEqual(result.U_coulomb.shape, (3,))
        self.assertEqual(result.ratio.shape, (3, 2))

    def test_sweep_coulomb_limit(self):
        """At large d, all phases should give ~Q1*Q2/d."""
        d_vals = np.array([500 * THIN_SHEET.R])
        phi_vals = np.array([0.0, math.pi / 2, math.pi])
        result = interaction_sweep(
            THIN_SHEET, THIN_SHEET, n1=1, n2=2, N=100,
            Q1=1.0, Q2=-1.0,
            d_values=d_vals, phi_values=phi_vals)
        for j in range(len(phi_vals)):
            self.assertAlmostEqual(result.ratio[0, j], 1.0, delta=0.02)

    def test_sweep_periodicity(self):
        """U(d, φ) = U(d, φ+2π) — period 2π in phase."""
        d_vals = np.array([5.0])
        phi_vals = np.array([0.7, 0.7 + 2 * math.pi])
        result = interaction_sweep(
            UNIT_SHEET, UNIT_SHEET, n1=1, n2=2, N=200,
            Q1=1.0, Q2=1.0,
            d_values=d_vals, phi_values=phi_vals)
        self.assertAlmostEqual(result.U[0, 0], result.U[0, 1], places=10)

    def test_sweep_mixed_sheets(self):
        """Sweep should work with two different sheets."""
        d_vals = np.array([20.0])
        phi_vals = np.array([0.0])
        result = interaction_sweep(
            THIN_SHEET, UNIT_SHEET, n1=1, n2=2, N=50,
            Q1=-1.0, Q2=1.0,
            d_values=d_vals, phi_values=phi_vals)
        # Should be negative (opposite charges attract)
        self.assertLess(result.U[0, 0], 0)


class TestForce(unittest.TestCase):

    def test_repulsive_like_charges(self):
        """Same-sign charges should repel (positive force along axis)."""
        pos1, dq1 = THIN_SHEET.charge_segments(1, 2, N=100, Q=1.0)
        pos2, dq2 = THIN_SHEET.charge_segments(1, 2, N=100, Q=1.0)
        d = 50 * THIN_SHEET.R
        pos2_shifted = pos2.copy()
        pos2_shifted[:, 2] += d
        F = interaction_force(pos1, dq1, pos2_shifted, dq2, axis=2)
        self.assertGreater(F, 0)

    def test_attractive_opposite_charges(self):
        """Opposite charges should attract (negative force along axis)."""
        pos1, dq1 = THIN_SHEET.charge_segments(1, 2, N=100, Q=1.0)
        pos2, dq2 = THIN_SHEET.charge_segments(1, 2, N=100, Q=-1.0)
        d = 50 * THIN_SHEET.R
        pos2_shifted = pos2.copy()
        pos2_shifted[:, 2] += d
        F = interaction_force(pos1, dq1, pos2_shifted, dq2, axis=2)
        self.assertLess(F, 0)


class TestNearField(unittest.TestCase):

    def test_near_field_extraction(self):
        d_vals = np.array([5.0, 10.0])
        phi_vals = np.linspace(0, 2 * math.pi, 8, endpoint=False)
        result = interaction_sweep(
            UNIT_SHEET, UNIT_SHEET, n1=1, n2=2, N=50,
            Q1=1.0, Q2=1.0,
            d_values=d_vals, phi_values=phi_vals)
        nf = near_field_correction(result)
        self.assertEqual(nf.U_avg.shape, (2,))
        self.assertEqual(nf.delta_U.shape, (2, 8))
        self.assertEqual(nf.delta_U_pi.shape, (2,))
        self.assertEqual(nf.barrier_factor.shape, (2,))

    def test_delta_averages_to_zero(self):
        """Phase deviations should average to zero by definition."""
        d_vals = np.array([5.0, 10.0, 20.0])
        phi_vals = np.linspace(0, 2 * math.pi, 12, endpoint=False)
        result = interaction_sweep(
            UNIT_SHEET, UNIT_SHEET, n1=1, n2=2, N=80,
            Q1=1.0, Q2=1.0,
            d_values=d_vals, phi_values=phi_vals)
        nf = near_field_correction(result)
        for i in range(len(d_vals)):
            self.assertAlmostEqual(
                np.mean(nf.delta_U[i, :]), 0.0, places=10)


if __name__ == '__main__':
    unittest.main()
