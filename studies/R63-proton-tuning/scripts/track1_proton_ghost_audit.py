"""
R63 Track 1 — Proton-sheet ghost audit (pure p-sheet scope).

Purpose: apply the e-sheet tuning discipline to the pure proton
sheet.  Enumerate only single-sheet p-modes (0,0,0,0,n_pt,n_pr);
for each, compute mass, effective charge, Z₃-free status, and
matter-decay accessibility.  Confirm the R60 T16 Z₃ selection
rule and show the ladder structure.

Inherits from R60:
  - T16 F89–F94: (1,2) is the confined quark strand; N=3 is the
    minimum Z₃-cancelling copy count; free p-sheet modes require
    n_pt ≡ 0 (mod 3); (3,6) is the proton.
  - T15 F84: nuclear scaling n_pt = 3A, n_pr = 6A, n_et = 1−Z.

Track 1 asks: after R60 T16's Z₃ filter, does the p-sheet
spectrum cleanly map to observed particles?  Are there any
Z₃-free modes below 2 GeV that are neither observed nor
matter-decay-accessible?  (These would be true p-sheet ghosts.)

Scope: pure p-sheet only.  (n_et, n_er, n_νt, n_νr) all zero.
Variables moved: none in this audit.  (Phase 2, if needed,
would move (ε_p, s_p).)
"""

import sys, os
from dataclasses import dataclass
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'R60-metric-11', 'scripts'))

from track1_solver import (
    derive_L_ring, L_vector_from_params, mode_energy, mode_6_to_11,
    signature_ok, M_P_MEV,
)
from track7b_resolve import build_aug_metric
from track15_phase1_mass import K_MODELF, modelF_baseline


# ─── Observed-particle inventory ────────────────────────────────────

@dataclass(frozen=True)
class Obs:
    name: str
    mass_MeV: float
    charge: int
    spin: Fraction

OBSERVED = [
    # photons / neutrinos (decay product pool only)
    Obs("γ",    0.0,        0,  Fraction(1)),
    Obs("ν",    3.3e-5,     0,  Fraction(1, 2)),
    # leptons
    Obs("e",    0.511,      -1, Fraction(1, 2)),
    Obs("μ",    105.658,    -1, Fraction(1, 2)),
    # mesons (pseudoscalar)
    Obs("π⁰",   134.977,    0,  Fraction(0)),
    Obs("π±",   139.570,    1,  Fraction(0)),
    Obs("K⁰",   497.611,    0,  Fraction(0)),
    Obs("K±",   493.677,    1,  Fraction(0)),
    Obs("η",    547.862,    0,  Fraction(0)),
    Obs("η′",   957.780,    0,  Fraction(0)),
    # mesons (vector)
    Obs("ρ",    775.3,      0,  Fraction(1)),   # ρ± at same mass
    Obs("φ",    1019.461,   0,  Fraction(1)),
    # baryons (octet)
    Obs("p",    938.272,    1,  Fraction(1, 2)),
    Obs("n",    939.565,    0,  Fraction(1, 2)),
    Obs("Λ",    1115.683,   0,  Fraction(1, 2)),
    Obs("Σ±",   1189.37,    1,  Fraction(1, 2)),
    Obs("Σ⁻",   1197.449,   -1, Fraction(1, 2)),
    Obs("Ξ⁰",   1314.86,    0,  Fraction(1, 2)),
    Obs("Ξ⁻",   1321.71,    -1, Fraction(1, 2)),
    # baryons (decuplet resonances — observed, short-lived)
    Obs("Δ⁺",   1232.0,     1,  Fraction(3, 2)),
    Obs("Ω⁻",   1672.45,    -1, Fraction(3, 2)),
    # heavy lepton
    Obs("τ",    1776.86,    -1, Fraction(1, 2)),
]


# ─── Composite-α and mass machinery ─────────────────────────────────

import math

def gcd_safe(a, b):
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        return 1
    if a == 0:
        return b
    if b == 0:
        return a
    return math.gcd(a, b)


def effective_charge(n_pt, n_pr):
    """Physical charge of a pure p-sheet mode under the composite-α rule.
    With n_et = 0, n_νt = 0:  Q_eff = n_pt / gcd(n_pt, n_pr).
    """
    g = gcd_safe(n_pt, n_pr)
    if g == 0:
        return 0
    return n_pt // g


def z3_free(n_pt):
    """R60 T16 selection rule: free p-sheet modes require n_pt ≡ 0 (mod 3)."""
    return n_pt % 3 == 0


def pure_p_mode(n_pt, n_pr):
    """Build the 6-tuple for a pure p-sheet mode."""
    return (0, 0, 0, 0, n_pt, n_pr)


# ─── Matter-decay threshold ─────────────────────────────────────────

def _precompute_decay_thresholds():
    """For each charge Q, compute the lightest N-body decay to observed
    particles (including γ and ν as allowed products).  Distinguishes:

      SPLIT_MIN[Q]    — minimum m_sum across N-body (N=2, 3) combinations
                         with at least one MATTER product (non-γ, non-ν).
      LIGHTEST_OBS[Q] — lightest observed particle with charge Q.
                         For |Q| > max observed, this is None.

    Simple rule for |Q| > 3 where 2- or 3-body with observed products
    can't reach Q directly: extrapolate via |Q| × m_e (the simplest
    multi-electron emission threshold).
    """
    split_min = {}
    lightest = {}

    def consider_split(m_sum, has_matter, Q):
        if not has_matter:
            return
        if Q not in split_min or m_sum < split_min[Q]:
            split_min[Q] = m_sum

    def is_matter(p):
        return p.name not in ("γ", "ν")

    # 2-body
    for A in OBSERVED:
        for B in OBSERVED:
            m_sum = A.mass_MeV + B.mass_MeV
            has_matter = is_matter(A) or is_matter(B)
            for sa in (1, -1):
                for sb in (1, -1):
                    consider_split(m_sum, has_matter, sa*A.charge + sb*B.charge)

    # 3-body
    for A in OBSERVED:
        for B in OBSERVED:
            for C in OBSERVED:
                m_sum = A.mass_MeV + B.mass_MeV + C.mass_MeV
                has_matter = is_matter(A) or is_matter(B) or is_matter(C)
                for sa in (1, -1):
                    for sb in (1, -1):
                        for sc in (1, -1):
                            Q = sa*A.charge + sb*B.charge + sc*C.charge
                            consider_split(m_sum, has_matter, Q)

    # For high |Q|, use |Q| × m_e as the N-body electron-emission threshold
    M_E = 0.511
    for q in range(-20, 21):
        electron_threshold = abs(q) * M_E
        if q not in split_min or electron_threshold < split_min[q]:
            split_min[q] = electron_threshold

    # Lightest observed per Q (matter only — γ/ν not observed as mass targets)
    for p in OBSERVED:
        if not is_matter(p):
            continue
        q = p.charge
        for signed_q in (q, -q):
            if signed_q not in lightest or p.mass_MeV < lightest[signed_q]:
                lightest[signed_q] = p.mass_MeV

    return split_min, lightest


SPLIT_MIN, LIGHTEST_OBS = _precompute_decay_thresholds()


# ─── Classification ─────────────────────────────────────────────────

MATCH_THRESHOLD_DEFAULT = 0.02
MATCH_THRESHOLD_PION = 0.14


def match_observed(E, Q):
    """Find the best observed particle with compatible Q at matching mass.

    Note: we match on MASS and CHARGE only, not spin.  The pure p-sheet
    audit tests whether the predicted (mass, Q) points on the p-sheet
    correspond to any observed particle.  The spin of the realized
    particle depends on whether the mode manifests as 1-sheet (spin ½)
    or as a compound 2-/3-sheet with ν/e participation (spin 0, 1,
    3/2).  R60 T20's SM taxonomy says: a (mass, Q) that the p-sheet
    rings can be realized at whatever spin the compound architecture
    gives — so if a matching observed particle exists at any spin,
    it's not a ghost.
    """
    best = None
    for p in OBSERVED:
        if p.mass_MeV < 1.0:
            continue
        if abs(p.charge) != abs(Q):
            continue
        rel = abs(E - p.mass_MeV) / p.mass_MeV
        thr = MATCH_THRESHOLD_PION if p.name.startswith("π") else MATCH_THRESHOLD_DEFAULT
        if rel < thr:
            if best is None or rel < best[1]:
                best = (p, rel, thr)
    return best


def closest_observed(E, Q):
    best = None
    for p in OBSERVED:
        if p.mass_MeV < 1.0:
            continue
        if abs(p.charge) != abs(Q):
            continue
        rel = abs(E - p.mass_MeV) / p.mass_MeV
        if best is None or rel < best[1]:
            best = (p, rel)
    return best


def classify_z3_free_mode(E, Q):
    """Classify a Z₃-free p-sheet mode against the observed spectrum.

    A sub-observed ghost is a mode predicted below the lightest
    observed particle of matching |Q| — the model says there's a
    particle the real world doesn't have.

    For charges with no observed particle at all (|Q| ≥ 3), we treat
    the mode as split-dominated provided the lightest |Q| electrons
    (matter) decay channel is energetically available.  Without an
    observed counterpart to be "below," the only concern is whether
    the mode can actually disperse energetically.
    """
    m = match_observed(E, Q)
    if m:
        p, rel, thr = m
        return 'observed', f"{p.name} (Δm/m = {rel*100:+.2f}%, thr {thr*100:.0f}%)"

    lightest = LIGHTEST_OBS.get(Q)
    split_thr = SPLIT_MIN.get(Q)

    if lightest is not None and E < lightest:
        return 'ghost-sub-observed', f"predicted at {E:.2f} MeV; lightest observed |Q|={abs(Q)} is {lightest:.2f} MeV"

    if split_thr is not None and E > split_thr:
        gap_str = f"gap above {lightest:.1f} MeV" if lightest else "no observed |Q|={} — decays via e-emission".format(abs(Q))
        return 'split-dominated', f"matter decay ≥ {split_thr:.2f} MeV; {gap_str}"

    return 'ghost-no-decay', f"E = {E:.2f} MeV; no decay path"


# ─── Enumeration ────────────────────────────────────────────────────

ENERGY_CAP_MEV = 2500.0  # go a bit above 2 GeV to catch (3, 9) Δ, (6, 12) d, etc.


def enumerate_pure_p_modes(G, L, n_pt_max=12, n_pr_max=18):
    """Enumerate pure p-sheet modes.  n_pt up to 12 covers (3,*), (6,*),
    (9,*), (12,*).  n_pr range wider to catch composite-like modes."""
    results = []
    for n_pt in range(-n_pt_max, n_pt_max + 1):
        for n_pr in range(-n_pr_max, n_pr_max + 1):
            if n_pt == 0 and n_pr == 0:
                continue
            n6 = pure_p_mode(n_pt, n_pr)
            n11 = mode_6_to_11(n6)
            E = mode_energy(G, L, n11)
            if E > ENERGY_CAP_MEV:
                continue
            g = gcd_safe(n_pt, n_pr)
            Q = effective_charge(n_pt, n_pr)
            free = z3_free(n_pt)
            results.append({
                'n_pt': n_pt, 'n_pr': n_pr,
                'E': E, 'gcd': g, 'Q_eff': Q, 'z3_free': free,
            })
    # Collapse antiparticle redundancy: (n_pt, n_pr) and (-n_pt, -n_pr)
    # are the same physical mode (charge conjugates).  Keep the one with
    # n_pt ≥ 0 (breaking ties on n_pr ≥ 0).
    seen = set()
    deduped = []
    for r in sorted(results, key=lambda x: (x['E'], x['n_pt'], x['n_pr'])):
        key = (r['E'], abs(r['Q_eff']), abs(r['n_pt']), abs(r['n_pr']))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(r)
    deduped.sort(key=lambda x: x['E'])
    return deduped


# ─── Phase 1 — baseline audit ───────────────────────────────────────

def phase1_audit(eps_p=0.55, s_p=0.162037, label="baseline"):
    print("=" * 100)
    print(f"R63 Track 1 — Pure p-sheet audit  ({label})")
    print("=" * 100)
    print()
    L_ring_p = derive_L_ring(M_P_MEV, 3, 6, eps_p, s_p, K_MODELF)
    params = modelF_baseline(eps_p=eps_p, s_p=s_p, L_ring_p=L_ring_p)
    G = build_aug_metric(params)
    L = L_vector_from_params(params)
    print(f"  ε_p = {eps_p},  s_p = {s_p},  L_ring_p = {L_ring_p:.3f} fm")
    print()

    modes = enumerate_pure_p_modes(G, L)
    print(f"  Enumerated {len(modes)} distinct pure p-sheet modes below {ENERGY_CAP_MEV:.0f} MeV.")
    print()

    # ─── Strand modes (Z₃-confined constituents) ────────────────────
    print("─" * 100)
    print("  Z₃-CONSTITUENTS (n_pt ≢ 0 mod 3) — confined; cannot exist as free modes")
    print("─" * 100)
    print(f"    {'E (MeV)':>10s}  {'(n_pt,n_pr)':>12s}  {'gcd':>4s}  {'|Q_eff|':>7s}  role")
    print("    " + "─" * 96)
    strands = [m for m in modes if not m['z3_free']]
    for m in strands[:25]:
        role = ""
        if m['n_pt'] == 1 and m['n_pr'] == 2:
            role = "QUARK STRAND → forms (3,6) proton"
        elif m['n_pt'] == 2 and m['n_pr'] == 4:
            role = "diquark strand → forms (6,12) deuteron"
        elif abs(m['n_pt']) == 1:
            role = f"(1,{m['n_pr']}) strand → triples to (3,{3*m['n_pr']})"
        elif abs(m['n_pt']) == 2:
            role = f"(2,{m['n_pr']}) strand → triples to (6,{3*m['n_pr']})"
        print(f"    {m['E']:>10.3f}  ({m['n_pt']:>+3d},{m['n_pr']:>+3d})  "
              f"{m['gcd']:>4d}  {abs(m['Q_eff']):>7d}  {role}")
    print()

    # ─── Z₃-free modes ──────────────────────────────────────────────
    print("─" * 100)
    print("  Z₃-FREE MODES (n_pt ≡ 0 mod 3) — can exist as free particles")
    print("─" * 100)
    print(f"    {'E (MeV)':>10s}  {'(n_pt,n_pr)':>12s}  {'gcd':>4s}  "
          f"{'|Q_eff|':>7s}  classification, detail")
    print("    " + "─" * 96)
    free_modes = [m for m in modes if m['z3_free']]
    for m in free_modes:
        cls, detail = classify_z3_free_mode(m['E'], m['Q_eff'])
        marker = ""
        if cls.startswith('ghost'):
            marker = " ⚠️"
        elif cls == 'observed':
            marker = " ✓"
        print(f"    {m['E']:>10.3f}  ({m['n_pt']:>+3d},{m['n_pr']:>+3d})  "
              f"{m['gcd']:>4d}  {abs(m['Q_eff']):>7d}  {cls:<22s}  {detail}{marker}")
    print()

    # ─── Summary ─────────────────────────────────────────────────────
    print("─" * 100)
    print(f"  Summary for {label}:")
    print(f"    {len(strands)} Z₃-confined strand modes (expected; not ghost candidates)")
    print(f"    {len(free_modes)} Z₃-free candidate modes  "
          f"(observed + split-dominated + ghost)")
    by_cls = {}
    for m in free_modes:
        cls, _ = classify_z3_free_mode(m['E'], m['Q_eff'])
        by_cls[cls] = by_cls.get(cls, 0) + 1
    for cls in ('observed', 'split-dominated', 'ghost-sub-observed',
                'ghost-no-observed', 'ghost-no-decay'):
        n = by_cls.get(cls, 0)
        if n > 0:
            print(f"      {cls:>22s}: {n}")
    print()
    sub_obs_ghosts = [m for m in free_modes
                      if classify_z3_free_mode(m['E'], m['Q_eff'])[0] == 'ghost-sub-observed']
    if not sub_obs_ghosts:
        print(f"  VERDICT: no sub-observed ghosts at {label}.  Every predicted mode either")
        print(f"           matches a particle or sits above the lightest observed of")
        print(f"           matching charge (where decay channels are always available).")
    else:
        print(f"  VERDICT: {len(sub_obs_ghosts)} sub-observed ghost(s) at {label}:")
        for g in sub_obs_ghosts:
            tup = f"({g['n_pt']:+d},{g['n_pr']:+d})"
            print(f"           {tup} at E = {g['E']:.2f} MeV, |Q|={abs(g['Q_eff'])}")
    print()
    return free_modes, len(sub_obs_ghosts)


# ─── Main ───────────────────────────────────────────────────────────

def main():
    # Phase 1 — baseline
    free_baseline, ghosts_baseline = phase1_audit(0.55, 0.162037, "baseline")

    # Phase 2 — Track 21's pion-optimal point for comparison
    free_t21, ghosts_t21 = phase1_audit(0.15, 0.05, "Track 21 pion candidate")

    # Final summary
    print("=" * 100)
    print("R63 Track 1 — pure p-sheet audit — final summary")
    print("=" * 100)
    print()
    print(f"  Baseline (ε_p=0.55, s_p=0.162):  {ghosts_baseline} sub-observed ghosts")
    print(f"  Track 21  (ε_p=0.15, s_p=0.05):  {ghosts_t21} sub-observed ghosts")
    print()
    if ghosts_baseline == 0:
        print("  ✓ R60 T16's Z₃ rule, at baseline, produces a CLEAN pure-p-sheet")
        print("    spectrum BELOW the proton.  Every predicted Z₃-free mode either")
        print("    matches an observed particle (proton, Ξ, etc.) or sits above the")
        print("    lightest observed particle of matching charge (where decay")
        print("    channels are always available).  The user's recollection of")
        print("    \"we eliminated ghosts below 3 × (1,2)\" is validated.")
        print()
    if ghosts_t21 > 0:
        print(f"  ⚠️  Track 21's (ε_p=0.15, s_p=0.05) INTRODUCES {ghosts_t21} sub-observed ghost(s)")
        print("    by inflating L_ring_p so much that pure p-ring modes fall BELOW")
        print("    the lightest observed neutral matter (π⁰ at 135 MeV).  This is a")
        print("    real concern for the naive Track 21 pion-fix proposal — the shift")
        print("    that closes the pion gap also creates sub-pion neutral predictions.")


if __name__ == "__main__":
    main()
