"""
R53 Track 6: Ghost inventory at each confirmed geometry

For each precision solution from Track 5, enumerate all modes
on that sheet below 2 GeV and classify by charge, spin, energy,
and gcd (fragmentation potential).

Key question: does the shear-resonance mechanism naturally thin
the ghost spectrum compared to the Track 11 high-n₂ picture
(which had ~8500 ghosts between e and τ)?
"""

import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))


def mu(nt, nr, eps, s):
    return math.sqrt((nt / eps) ** 2 + (nr - nt * s) ** 2)


def inventory(label, eps, s, m_ref, mode_ref, E_max_MeV=2000,
              nt_max=15, nr_max=100):
    """
    Enumerate all modes below E_max on one sheet.
    m_ref and mode_ref set the energy scale: L_ring chosen so
    that mode_ref has mass m_ref.
    """
    mu_ref = mu(*mode_ref, eps, s)
    if mu_ref < 1e-15:
        print(f'  {label}: reference mode has μ ≈ 0, skipping')
        return
    scale = m_ref / mu_ref  # MeV per unit μ

    # Enumerate
    modes = []
    for nt in range(-nt_max, nt_max + 1):
        for nr in range(-nr_max, nr_max + 1):
            if nt == 0 and nr == 0:
                continue
            m = mu(nt, nr, eps, s)
            E = scale * m
            if E > E_max_MeV:
                continue
            spin = 0.5 if abs(nt) % 2 == 1 else 0.0
            Q_e = -nt  # e-sheet charge contribution
            g = math.gcd(abs(nt), abs(nr)) if (nt != 0 and nr != 0) else max(abs(nt), abs(nr))
            modes.append({
                'nt': nt, 'nr': nr, 'E': E, 'spin': spin,
                'Q_e': Q_e, 'gcd': g,
                'frag': 'frag' if g > 1 else 'irred',
            })

    modes.sort(key=lambda x: x['E'])

    print(f'  {label}')
    print(f'  ε = {eps:.2f}, s = {s:.6f}, scale = {scale:.4f} MeV/μ')
    print(f'  Reference: {mode_ref} → {m_ref} MeV')
    print(f'  Total modes below {E_max_MeV} MeV: {len(modes)}')
    print()

    # By energy band
    bands = [(0, 1), (1, 10), (10, 100), (100, 200), (200, 500),
             (500, 1000), (1000, 2000)]
    print(f'    {"Band (MeV)":>15s}  {"Total":>6s}  {"spin½":>6s}  '
          f'{"spin0":>6s}  {"irred":>6s}  {"frag":>6s}  '
          f'{"Q=±1":>6s}  {"Q=0":>6s}')
    print(f'    {"─"*15}  {"─"*6}  {"─"*6}  {"─"*6}  {"─"*6}  '
          f'{"─"*6}  {"─"*6}  {"─"*6}')
    for lo, hi in bands:
        band = [m for m in modes if lo <= m['E'] < hi]
        n = len(band)
        n_half = sum(1 for m in band if m['spin'] == 0.5)
        n_zero = sum(1 for m in band if m['spin'] == 0.0)
        n_irred = sum(1 for m in band if m['frag'] == 'irred')
        n_frag = sum(1 for m in band if m['frag'] == 'frag')
        n_charged = sum(1 for m in band if abs(m['Q_e']) == 1)
        n_neutral = sum(1 for m in band if m['Q_e'] == 0)
        print(f'    {lo:>6d}–{hi:<6d}  {n:>6d}  {n_half:>6d}  '
              f'{n_zero:>6d}  {n_irred:>6d}  {n_frag:>6d}  '
              f'{n_charged:>6d}  {n_neutral:>6d}')
    print()

    # Lightest 20 modes
    print(f'    20 lightest modes:')
    print(f'    {"(n_t,n_r)":>10s}  {"E (MeV)":>10s}  {"spin":>5s}  '
          f'{"Q_e":>4s}  {"gcd":>4s}  {"status":>6s}')
    print(f'    {"─"*10}  {"─"*10}  {"─"*5}  {"─"*4}  {"─"*4}  {"─"*6}')
    for m in modes[:20]:
        mode_str = f'({m["nt"]},{m["nr"]})'
        print(f'    {mode_str:>10s}  {m["E"]:>10.3f}  '
              f'{m["spin"]:>5.1f}  {m["Q_e"]:>+4d}  '
              f'{m["gcd"]:>4d}  {m["frag"]:>6s}')
    print()

    # How many Q=±1, spin-½, irreducible modes (the "lepton-like" ghosts)?
    lepton_ghosts = [m for m in modes
                     if abs(m['Q_e']) == 1 and m['spin'] == 0.5
                     and m['frag'] == 'irred']
    print(f'    Q=±1, spin-½, irreducible (lepton-like ghosts): '
          f'{len(lepton_ghosts)}')
    if lepton_ghosts:
        print(f'    Lightest 10:')
        for m in lepton_ghosts[:10]:
            print(f'      ({m["nt"]},{m["nr"]})  E = {m["E"]:.3f} MeV')
    print()
    print()


def main():
    print('=' * 70)
    print('R53 Track 6: Ghost inventory')
    print('=' * 70)
    print()

    # ── Lepton Solution B ───────────────────────────────────────
    inventory('ELECTRON SHEET — Lepton Solution B',
              eps=330.110, s=3.003842,
              m_ref=0.51099895, mode_ref=(1, 3))

    # ── Lepton Solution D ───────────────────────────────────────
    inventory('ELECTRON SHEET — Lepton Solution D',
              eps=397.074, s=2.004200,
              m_ref=0.51099895, mode_ref=(1, 2))

    # ── Model-D comparison ──────────────────────────────────────
    inventory('ELECTRON SHEET — Model-D (for comparison)',
              eps=0.65, s=0.09594,
              m_ref=0.51099895, mode_ref=(1, 2),
              nt_max=5, nr_max=20)

    # ── Down-type quark solution ────────────────────────────────
    inventory('PROTON SHEET — Down-type quarks',
              eps=570.428, s=0.799017,
              m_ref=4.67, mode_ref=(5, 4))

    # ── Model-D proton sheet ────────────────────────────────────
    inventory('PROTON SHEET — Model-D (for comparison)',
              eps=0.55, s=0.16204,
              m_ref=938.272, mode_ref=(1, 3),
              nt_max=5, nr_max=20)

    print('Track 6 complete.')


if __name__ == '__main__':
    main()
