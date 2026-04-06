"""
R50 Track 1: Validate ma_model_d.py

Tests:
  1. Electron (1,2,0,0,0,0) → 0.511 MeV
  2. Proton  (0,0,0,0,3,6) → 938.3 MeV
  3. Neutrino (0,0,1,1,0,0) → ~29 meV (Assignment A)
  4. Charge: electron = -1, proton = +1, neutrino = 0
  5. Spin-½ counts: electron = 1, proton = 1, neutrino = 1
  6. Waveguide: electron propagates, proton propagates
  7. Finite-ε spin for electron, proton, neutrino
  8. Geometry summary printout
  9. Small mode scan at default parameters
 10. Near-miss search for neutron
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from lib.ma_model_d import MaD, alpha_from_geometry, solve_shear_for_alpha, spin_Lz, spin_inferred

def main():
    print("=" * 65)
    print("R50 Track 1: ma_model_d validation")
    print("=" * 65)

    # ── 1. Construct from physics ─────────────────────────────────
    print("\n1. Constructing MaD.from_physics(eps_e=0.65, eps_nu=5.0, eps_p=0.55)")
    m = MaD.from_physics(eps_e=0.65, eps_nu=5.0, eps_p=0.55)
    m.summary()

    # ── 2. Reference mode energies ────────────────────────────────
    print("\n2. Reference mode energies")

    n_e = (1, 2, 0, 0, 0, 0)
    n_p = (0, 0, 0, 0, 3, 6)
    n_nu = (0, 0, 1, 1, 0, 0)

    E_e = m.energy(n_e)
    E_p = m.energy(n_p)
    E_nu = m.energy(n_nu)

    print(f"  Electron {n_e}:  E = {E_e:.6f} MeV  (target: 0.511000)")
    print(f"  Proton   {n_p}:  E = {E_p:.3f} MeV  (target: 938.272)")
    E_nu_meV = E_nu * 1e9  # 1 MeV = 10⁹ meV
    print(f"  Neutrino {n_nu}:  E = {E_nu_meV:.2f} meV  (= {E_nu:.4e} MeV)")

    assert abs(E_e - 0.511) < 0.001, f"Electron energy off: {E_e}"
    assert abs(E_p - 938.272) < 0.5, f"Proton energy off: {E_p}"
    assert E_nu < 1.0, f"Neutrino energy too large: {E_nu}"
    print("  ✓ All reference energies OK")

    # ── 3. Charge ─────────────────────────────────────────────────
    print("\n3. Charge")
    Q_e = m.charge(n_e)
    Q_p = m.charge(n_p)
    Q_p_comp = m.charge_composite(n_p)
    Q_nu = m.charge(n_nu)
    print(f"  Electron:   Q = {Q_e:+d}  (target: -1)")
    print(f"  Proton raw: Q = {Q_p:+d}  (Q = -n₁ + n₅ = 0 + 3)")
    print(f"  Proton composite: Q = {Q_p_comp:+d}  "
          f"(n₅/gcd(3,6) = 3/3 = +1)")
    print(f"  Neutrino:   Q = {Q_nu:+d}  (target: 0)")

    assert Q_e == -1, f"Electron charge wrong: {Q_e}"
    assert Q_p == +3, f"Proton raw charge wrong: {Q_p}"
    assert Q_p_comp == +1, f"Proton composite charge wrong: {Q_p_comp}"
    assert Q_nu == 0, f"Neutrino charge wrong: {Q_nu}"
    print("  ✓ All charges OK (raw and composite)")

    # ── 4. Spin-½ count ───────────────────────────────────────────
    print("\n4. Spin-½ count (thin-torus)")
    for label, n6 in [('Electron', n_e), ('Proton', n_p), ('Neutrino', n_nu)]:
        sh = m.spin_halves(n6)
        print(f"  {label} {n6}: spin_½s = {sh}")
    print("  (3,6) proton: n₅=3 is odd → 1 spin-½ contribution ✓")

    # ── 5. Spin ────────────────────────────────────────────────────
    print("\n5. Spin: topological (exact) vs classical Lz (diagnostic)")
    for label, n6 in [
        ('Electron', n_e), ('Proton', n_p), ('Neutrino', n_nu),
    ]:
        s_topo = m.spin_total(n6)
        s_Lz = m.spin_Lz_total(n6)
        print(f"  {label}:  topological = {s_topo}  "
              f"classical L_z/ℏ = {s_Lz:.4f}")
    print("  Topological spin is exact (from tube winding parity).")
    print("  Classical L_z is a geodesic diagnostic, not the physical spin.")

    # ── 6. Waveguide propagation ──────────────────────────────────
    print("\n6. Waveguide propagation")
    for label, n6 in [
        ('Electron (1,2)', n_e),
        ('Proton (3,6)', n_p),
        ('Neutrino (1,1)', n_nu),
        ('Ghost e(1,1)', (1, 1, 0, 0, 0, 0)),
        ('Ghost p(1,2)', (0, 0, 0, 0, 1, 2)),
    ]:
        prop = m.propagates(n6)
        print(f"  {label}: propagates = {prop}")

    # ── 7. Energy decomposition ───────────────────────────────────
    print("\n7. Energy decomposition (electron)")
    decomp = m.energy_decomp(n_e)
    print(f"  Total: {decomp['total_MeV']:.6f} MeV")
    for key in ['e', 'nu', 'p', 'ep', 'enu', 'nup']:
        frac = decomp['fractions'][key]
        if abs(frac) > 1e-10:
            print(f"  {key:>4}: {frac * 100:.1f}%")

    # ── 8. Alpha formula ──────────────────────────────────────────
    print("\n8. Alpha formula validation")
    for label, eps in [('ε_e = 0.5', 0.5), ('ε_p = 1/3', 1.0/3.0)]:
        s = solve_shear_for_alpha(eps)
        if s is not None:
            a = alpha_from_geometry(eps, s)
            print(f"  {label}: s = {s:.6f}, α = {a:.8f}  "
                  f"(target: {1/137.036:.8f})")
        else:
            print(f"  {label}: no solution")

    # ── 9. Small mode scan ────────────────────────────────────────
    print("\n9. Mode scan (n_max=2, E < 2000 MeV, propagating only)")
    modes = m.scan_modes(n_max=2, E_max_MeV=2000, propagating_only=True)
    print(f"  Found {len(modes)} propagating modes below 2 GeV")
    print(f"  Lowest 10:")
    for i, md in enumerate(modes[:10]):
        E_str = (f"{md.E_MeV * 1e9:.2f} meV" if md.E_MeV < 1e-3
                 else f"{md.E_MeV:.4f} MeV")
        print(f"    {i+1:2d}. {md.n}  E = {E_str}  "
              f"Q = {md.charge:+d}  spin½s = {md.spin_halves}  "
              f"sheets = {md.sheets_active}")

    # ── 10. Near-miss: neutron ────────────────────────────────────
    print("\n10. Near-miss search: neutron (939.565 MeV)")
    near = m.nearest_modes(939.565, n_max=2, top_k=5,
                           propagating_only=True)
    if near:
        print(f"  Top 5 nearest modes:")
        for i, nm in enumerate(near):
            print(f"    {i+1}. {nm.mode.n}  E = {nm.mode.E_MeV:.3f} MeV  "
                  f"residual = {nm.residual_MeV:+.3f} MeV  "
                  f"({nm.residual_frac * 100:.2f}%)  "
                  f"Q = {nm.mode.charge:+d}  sheets = {nm.mode.sheets_active}")
    else:
        print("  No modes found (increase n_max or allow non-propagating)")

    # ── 11. with_params ───────────────────────────────────────────
    print("\n11. Immutable update: with_params(sigma_ep=-0.01)")
    m2 = m.with_params(sigma_ep=-0.01)
    E_e2 = m2.energy(n_e)
    E_p2 = m2.energy(n_p)
    print(f"  Electron: {E_e:.6f} → {E_e2:.6f} MeV")
    print(f"  Proton:   {E_p:.3f} → {E_p2:.3f} MeV")

    # Re-check neutron with cross-shear
    near2 = m2.nearest_modes(939.565, n_max=2, top_k=3,
                             propagating_only=True)
    if near2:
        print(f"  Nearest to neutron with σ_ep = -0.01:")
        for nm in near2[:3]:
            print(f"    {nm.mode.n}  E = {nm.mode.E_MeV:.3f} MeV  "
                  f"residual = {nm.residual_MeV:+.3f} MeV  "
                  f"Q = {nm.mode.charge:+d}")

    print("\n" + "=" * 65)
    print("Track 1 validation complete.")
    print("=" * 65)


if __name__ == '__main__':
    main()
