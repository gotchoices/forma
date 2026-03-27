#!/usr/bin/env python3
"""
R35 Track 1: Threshold detection statistics

Monte Carlo + analytical model of Reiter's beam-split experiment.
Tests whether threshold theory with parametric pre-load distributions
can reproduce Re/Rc ratios observed by Reiter (1960).

The experiment:
  - Source emits gamma rays (E_γ = 88 keV for Cd-109, 511 keV for Na-22)
  - Tandem geometry: thin detector #1, thick detector #2
  - Gamma can pass through det 1 (no interaction) or Compton scatter
  - In QM: photon is indivisible → coincidence = random only
  - In threshold model: gamma is classical wave, energy splits
  - Pre-loaded atoms can fire from partial energy → excess coincidence

Key observable: Re/Rc = (real coincidence rate) / (random coincidence rate)
  - Reiter measured: Re/Rc ≈ 33 for Cd-109, ≈ 963 for Na-22 (triple)
  - QM prediction: Re/Rc = 0 (only random background)
"""

import numpy as np
import math

np.random.seed(42)

# ═══════════════════════════════════════════════════════════════════
#  Physical parameters
# ═══════════════════════════════════════════════════════════════════

E_GAMMA_CD109 = 88.0    # keV
E_GAMMA_NA22 = 511.0     # keV (annihilation gamma)
M_E_KEV = 511.0          # electron mass in keV

R_SOURCE = 300.0          # source rate (events/s)
TAU_COINC = 1.0e-6        # coincidence window (1 μs)

SCA_LL_FRAC = 2.0 / 3.0  # SCA lower level (fraction of E_γ)
SCA_UL_FRAC = 1.5         # SCA upper level (fraction of E_γ)


def compton_max_transfer(E_keV):
    """Max fraction of gamma energy to Compton electron."""
    x = E_keV / M_E_KEV
    return 2 * x / (1 + 2 * x)


# ═══════════════════════════════════════════════════════════════════
#  Pre-load distributions (all return values in [0, 1) as E_pre/E_γ)
# ═══════════════════════════════════════════════════════════════════

def preload_uniform(n, frac):
    return np.random.uniform(0, frac, n)

def preload_exponential(n, mean_frac):
    return np.minimum(np.random.exponential(mean_frac, n), 0.9999)

def preload_beta(n, a, b):
    return np.random.beta(a, b, n)

def preload_zero(n):
    return np.zeros(n)


# ═══════════════════════════════════════════════════════════════════
#  Monte Carlo simulation
# ═══════════════════════════════════════════════════════════════════

def run_mc(N, E_keV, p_interact, preload_func, preload_params,
           R=R_SOURCE, tau=TAU_COINC, sca_ll=SCA_LL_FRAC, sca_ul=SCA_UL_FRAC):
    """
    Monte Carlo of the threshold beam-split experiment.

    Detection condition: SCA_LL ≤ (E_pre + E_dep)/E_γ ≤ SCA_UL
    """
    eta_max = compton_max_transfer(E_keV)

    interacted = np.random.random(N) < p_interact
    n_int = interacted.sum()

    # energy deposited in det 1 (fraction of E_γ)
    E_dep1 = np.zeros(N)
    if n_int > 0:
        E_dep1[interacted] = np.random.uniform(0, eta_max, n_int)

    # energy reaching det 2 (fraction of E_γ)
    E_dep2 = np.where(interacted, 1.0 - E_dep1, 1.0)

    # pre-loads
    E_pre1 = preload_func(N, *preload_params)
    E_pre2 = preload_func(N, *preload_params)

    # firing conditions (SCA window)
    total1 = E_pre1 + E_dep1
    total2 = E_pre2 + E_dep2
    det1_fires = (total1 >= sca_ll) & (total1 <= sca_ul)
    det2_fires = (total2 >= sca_ll) & (total2 <= sca_ul)

    S1 = det1_fires.sum()
    S2 = det2_fires.sum()
    C_real = (det1_fires & det2_fires).sum()

    T = N / R
    S1r = S1 / T
    S2r = S2 / T
    Rc = 2 * tau * S1r * S2r
    Re = C_real / T

    return {
        'S1': S1, 'S2': S2, 'C': C_real,
        'P_S1': S1/N, 'P_S2': S2/N, 'P_C': C_real/N,
        'Re_Rc': Re/Rc if Rc > 0 else float('inf'),
    }


# ═══════════════════════════════════════════════════════════════════
#  Dynamic equilibrium Monte Carlo
# ═══════════════════════════════════════════════════════════════════

def run_dynamic_mc(N_events, E_keV, p_interact, N_domains,
                   fill_rate_per_domain, leakage_rate,
                   R=R_SOURCE, tau=TAU_COINC,
                   sca_ll=SCA_LL_FRAC, sca_ul=SCA_UL_FRAC):
    """
    Dynamic Monte Carlo where pre-loads evolve over time.

    N_domains: number of neutrino domains per detector
    fill_rate_per_domain: energy fill rate (fraction of E_γ per event interval)
    leakage_rate: fraction of pre-load lost per event interval

    Each source event:
    1. All domains accumulate background energy (fill_rate)
    2. All domains lose energy to leakage
    3. One domain in each detector is hit by the gamma
    4. Check SCA firing condition
    """
    eta_max = compton_max_transfer(E_keV)
    dt = 1.0 / R

    preloads1 = np.zeros(N_domains)
    preloads2 = np.zeros(N_domains)

    S1 = S2 = C = 0

    for i in range(N_events):
        preloads1 += fill_rate_per_domain
        preloads2 += fill_rate_per_domain
        preloads1 *= (1 - leakage_rate)
        preloads2 *= (1 - leakage_rate)
        np.clip(preloads1, 0, 0.9999, out=preloads1)
        np.clip(preloads2, 0, 0.9999, out=preloads2)

        interacts = np.random.random() < p_interact
        if interacts:
            eta = np.random.uniform(0, eta_max)
            E_dep1 = eta
            E_dep2 = 1.0 - eta
        else:
            E_dep1 = 0.0
            E_dep2 = 1.0

        idx1 = np.random.randint(N_domains)
        idx2 = np.random.randint(N_domains)

        t1 = preloads1[idx1] + E_dep1
        t2 = preloads2[idx2] + E_dep2

        f1 = sca_ll <= t1 <= sca_ul
        f2 = sca_ll <= t2 <= sca_ul

        if f1:
            S1 += 1
            preloads1[idx1] = max(t1 - 1.0, 0)
        if f2:
            S2 += 1
            preloads2[idx2] = max(t2 - 1.0, 0)
        if f1 and f2:
            C += 1

    T = N_events / R
    S1r = S1 / T
    S2r = S2 / T
    Rc = 2 * tau * S1r * S2r
    Re = C / T

    return {
        'S1': S1, 'S2': S2, 'C': C,
        'P_S1': S1/N_events, 'P_S2': S2/N_events,
        'P_C': C/N_events,
        'Re_Rc': Re/Rc if Rc > 0 else float('inf'),
        'mean_preload': (preloads1.mean() + preloads2.mean())/2,
    }


# ═══════════════════════════════════════════════════════════════════
#  Main analysis
# ═══════════════════════════════════════════════════════════════════

def main():
    N = 5_000_000
    print("=" * 72)
    print("R35 Track 1: Threshold Detection Statistics")
    print("=" * 72)

    for E_gamma, label, target in [
        (E_GAMMA_CD109, "Cd-109", 33),
        (E_GAMMA_NA22, "Na-22", 963),
    ]:
        eta_max = compton_max_transfer(E_gamma)
        sca_ll = SCA_LL_FRAC

        print(f"\n{'─'*72}")
        print(f"  {label}: E_γ = {E_gamma} keV")
        print(f"  Compton max transfer: {eta_max:.3f} ({eta_max*E_gamma:.1f} keV)")
        print(f"  Min energy to det 2 (after max scatter): "
              f"{(1-eta_max)*E_gamma:.1f} keV = {(1-eta_max):.3f} E_γ")
        print(f"  SCA lower level: {sca_ll:.3f} E_γ = {sca_ll*E_gamma:.1f} keV")
        print(f"  Det 2 always fires? {(1-eta_max) >= sca_ll} "
              f"  ((1-η_max)={1-eta_max:.3f} vs SCA_LL={sca_ll:.3f})")
        print(f"  Target Re/Rc: {target}")
        print(f"  1/(2τR) limit: {1/(2*TAU_COINC*R_SOURCE):.0f}")

    # ══════════════════════════════════════════════════════════════
    print(f"\n{'='*72}")
    print("PART A: Cd-109 (88 keV) — The Compton Asymmetry Problem")
    print("=" * 72)

    E = E_GAMMA_CD109
    eta_max = compton_max_transfer(E)
    print(f"""
At 88 keV, the Compton recoil transfers at most {eta_max:.1%} of the
gamma energy.  Detector 2 always receives ≥ {(1-eta_max):.1%} of E_γ,
which exceeds SCA_LL = {SCA_LL_FRAC:.1%}.  Therefore det 2 fires on
EVERY event where an interaction occurs — regardless of pre-load.

This makes Re/Rc = 1/(2τR), independent of the pre-load distribution.
""")

    p_int = 0.10
    print(f"Verification (p_interact = {p_int}, SCA_UL = 1.5):")
    print(f"{'Distribution':>20s} {'P(S1)':>7s} {'P(S2)':>7s} "
          f"{'P(C)':>9s} {'Re/Rc':>8s}")
    print("-" * 56)

    dists = [
        ("Zero", preload_zero, ()),
        ("Uniform(0,0.3)", preload_uniform, (0.3,)),
        ("Uniform(0,0.7)", preload_uniform, (0.7,)),
        ("Uniform(0,0.9)", preload_uniform, (0.9,)),
        ("Exp(mean=0.3)", preload_exponential, (0.3,)),
        ("Beta(2,5)", preload_beta, (2, 5)),
        ("Beta(5,2)", preload_beta, (5, 2)),
    ]

    for name, func, params in dists:
        r = run_mc(N, E, p_int, func, params)
        print(f"{name:>20s} {r['P_S1']:7.4f} {r['P_S2']:7.4f} "
              f"{r['P_C']:9.6f} {r['Re_Rc']:8.1f}")

    # ── SCA upper limit effect ───────────────────────────────────
    print(f"\n{'─'*72}")
    print("PART B: Effect of tight SCA window (Cd-109)")
    print("─" * 72)
    print(f"""
With a tight SCA window, high pre-loads push the pulse ABOVE the
upper limit, rejecting events.  This breaks the Re/Rc = 1/(2τR)
degeneracy by making P(S2) < 1.
""")

    print(f"{'SCA_UL':>8s}  {'Preload':>15s}  {'P(S1)':>7s} {'P(S2)':>7s} "
          f"{'P(C)':>9s} {'Re/Rc':>8s}")
    print("-" * 60)

    for sca_ul in [1.05, 1.10, 1.15, 1.20, 1.50]:
        for name, func, params in [
            ("Zero", preload_zero, ()),
            ("Uniform(0,0.5)", preload_uniform, (0.5,)),
            ("Uniform(0,0.9)", preload_uniform, (0.9,)),
        ]:
            r = run_mc(N, E, p_int, func, params, sca_ul=sca_ul)
            print(f"{sca_ul:8.2f}  {name:>15s}  {r['P_S1']:7.4f} {r['P_S2']:7.4f} "
                  f"{r['P_C']:9.6f} {r['Re_Rc']:8.1f}")
        print()

    # ══════════════════════════════════════════════════════════════
    print(f"{'='*72}")
    print("PART C: Na-22 (511 keV) — Both Detectors Need Pre-load")
    print("=" * 72)

    E = E_GAMMA_NA22
    eta_max = compton_max_transfer(E)
    print(f"""
At 511 keV, Compton max transfer = {eta_max:.3f}.  After maximum
scatter, det 2 gets only {(1-eta_max):.3f} × E_γ = {(1-eta_max)*E:.0f} keV,
which is BELOW SCA_LL = {SCA_LL_FRAC*E:.0f} keV.

Both detectors need pre-load to fire.  Re/Rc NOW depends on the
pre-load distribution.
""")

    print(f"{'Distribution':>20s} {'P(S1)':>7s} {'P(S2)':>7s} "
          f"{'P(C)':>9s} {'Re/Rc':>8s}")
    print("-" * 56)

    na_dists = [
        ("Zero", preload_zero, ()),
        ("Uniform(0,0.3)", preload_uniform, (0.3,)),
        ("Uniform(0,0.5)", preload_uniform, (0.5,)),
        ("Uniform(0,0.7)", preload_uniform, (0.7,)),
        ("Uniform(0,0.9)", preload_uniform, (0.9,)),
        ("Exp(mean=0.2)", preload_exponential, (0.2,)),
        ("Exp(mean=0.4)", preload_exponential, (0.4,)),
        ("Exp(mean=0.6)", preload_exponential, (0.6,)),
        ("Beta(2,5)", preload_beta, (2, 5)),
        ("Beta(5,2)", preload_beta, (5, 2)),
        ("Beta(2,2)", preload_beta, (2, 2)),
        ("Beta(0.5,0.5)", preload_beta, (0.5, 0.5)),
    ]

    for name, func, params in na_dists:
        r = run_mc(N, E, p_int, func, params)
        print(f"{name:>20s} {r['P_S1']:7.4f} {r['P_S2']:7.4f} "
              f"{r['P_C']:9.6f} {r['Re_Rc']:8.1f}")

    # ── Na-22 parameter sweep for Re/Rc ≈ 963 ───────────────────
    print(f"\n{'─'*72}")
    print("PART D: Na-22 sweep — hunting Re/Rc ≈ 963")
    print("─" * 72)
    print(f"\nSweeping uniform pre-load max (p_interact = 0.10):")
    print(f"{'unif_max':>10s} {'Re/Rc':>10s}")
    print("-" * 24)

    for u_max in np.arange(0.10, 1.01, 0.05):
        r = run_mc(N, E_GAMMA_NA22, 0.10, preload_uniform, (u_max,))
        print(f"{u_max:10.2f} {r['Re_Rc']:10.1f}")

    # ══════════════════════════════════════════════════════════════
    print(f"\n{'='*72}")
    print("PART E: Dynamic equilibrium Monte Carlo (small scale)")
    print("=" * 72)
    print(f"""
The parametric model treats pre-loads as static draws.  The dynamic
model tracks pre-load evolution: atoms accumulate energy from background
radiation and lose it to leakage.  The steady-state pre-load distribution
emerges naturally.
""")

    N_dyn = 200_000
    p_int = 0.10
    N_domains = 1000

    print(f"Events: {N_dyn:,}, domains per detector: {N_domains}")
    print(f"{'fill_rate':>10s} {'leak_rate':>10s} {'⟨preload⟩':>10s} "
          f"{'P(C)':>9s} {'Re/Rc':>8s}")
    print("-" * 54)

    for fill_rate in [1e-4, 5e-4, 1e-3, 5e-3, 1e-2]:
        for leak_rate in [1e-5, 1e-4, 1e-3, 1e-2]:
            r = run_dynamic_mc(N_dyn, E_GAMMA_CD109, p_int,
                               N_domains, fill_rate, leak_rate)
            if r['C'] > 0:
                print(f"{fill_rate:10.1e} {leak_rate:10.1e} "
                      f"{r['mean_preload']:10.4f} "
                      f"{r['P_C']:9.6f} {r['Re_Rc']:8.1f}")

    # Same for Na-22
    print(f"\nNa-22 dynamic (511 keV):")
    print(f"{'fill_rate':>10s} {'leak_rate':>10s} {'⟨preload⟩':>10s} "
          f"{'P(C)':>9s} {'Re/Rc':>8s}")
    print("-" * 54)

    for fill_rate in [1e-4, 5e-4, 1e-3, 5e-3, 1e-2]:
        for leak_rate in [1e-5, 1e-4, 1e-3, 1e-2]:
            r = run_dynamic_mc(N_dyn, E_GAMMA_NA22, p_int,
                               N_domains, fill_rate, leak_rate)
            if r['C'] > 0:
                print(f"{fill_rate:10.1e} {leak_rate:10.1e} "
                      f"{r['mean_preload']:10.4f} "
                      f"{r['P_C']:9.6f} {r['Re_Rc']:8.1f}")

    # ══════════════════════════════════════════════════════════════
    print(f"\n{'='*72}")
    print("PART F: Physics of the Re/Rc ratio")
    print("=" * 72)

    ideal = 1.0 / (2 * TAU_COINC * R_SOURCE)

    print(f"""
ANALYTICAL STRUCTURE OF Re/Rc
─────────────────────────────
Re = R × p_int × ⟨P₁(η) × P₂(η)⟩_η    (both fire from same gamma)
S₁ = R × p_int × ⟨P₁(η)⟩_η             (det 1 fires)
S₂ = R × [(1-p_int) + p_int × ⟨P₂(η)⟩_η]   (det 2 fires)
Rc = 2τ × S₁ × S₂                        (random coincidence)

where P₁(η) = P(E_pre + η ∈ SCA window)
      P₂(η) = P(E_pre + (1-η) ∈ SCA window)
      η = Compton electron fraction, uniform on [0, η_max]

LIMITING CASES:
""")
    print(f"  1/(2τR) = {ideal:.0f}  (maximum possible Re/Rc)")
    print(f"  Reiter Cd-109: Re/Rc = 33  ({33/ideal:.2%} of maximum)")
    print(f"  Reiter Na-22:  Re/Rc = 963 ({963/ideal:.2%} of maximum)")

    eta88 = compton_max_transfer(88)
    eta511 = compton_max_transfer(511)
    print(f"""
KEY FINDING: Cd-109 vs Na-22 split explained by Compton kinematics
──────────────────────────────────────────────────────────────────

  At 88 keV:  η_max = {eta88:.3f}  →  det 2 min = {1-eta88:.3f}  > SCA_LL = {SCA_LL_FRAC:.3f}
    ⇒ Det 2 ALWAYS fires  ⇒  P₂ = 1  ⇒  Re/Rc = 1/(2τR)
    ⇒ Model OVER-predicts by {ideal/33:.0f}×

  At 511 keV: η_max = {eta511:.3f}  →  det 2 min = {1-eta511:.3f}  < SCA_LL = {SCA_LL_FRAC:.3f}
    ⇒ Det 2 needs pre-load  ⇒  Re/Rc depends on P(E_pre)
    ⇒ Model can match Reiter — but only with specific distributions

IMPLICATIONS:
  - The 88 keV result means either:
    (a) The threshold model needs an SCA upper limit (tight window)
    (b) Pre-loads suppress det 2 at 88 keV by some other mechanism
    (c) The 88 keV result constrains the model differently than 511 keV

  - The 511 keV result is more informative: it genuinely constrains
    the pre-load distribution via Re/Rc.  The pre-load must have
    enough mass near (SCA_LL − (1−η_max)) to fire det 2, but not
    so much that Re/Rc is pushed to the maximum.
""")


if __name__ == '__main__':
    main()
