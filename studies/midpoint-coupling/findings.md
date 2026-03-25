# R34 findings — The midpoint coupling

## Track 1 — Kramers-Kronig dispersive model


### F1. Pure Kramers-Kronig dispersion cannot reach 1/α = 24

A dispersive sum over T⁶ mode resonances adds to 1/α at
low energy (screening: modes below the probe energy push
1/α upward) but the contribution vanishes at high energy
(E ≫ all mode masses).  So 1/α → 80.5 at E → ∞, NOT 24.

To push 1/α below 80.5 requires a second mechanism:
vacuum polarization (logarithmic running from virtual
pair production), which monotonically decreases 1/α.


### F2. The hybrid model reduces to Lorentzian dispersion

Combining dispersive screening S(E) and vacuum-polarization
running R(E) as complementary functions (S + R = 1) gives
a one-parameter model:

    1/α(E) = 80.5 + 56.5 × (E*² − E²) / (E² + E*²)

Properties:
- 1/α(0) = 137  (exact)
- 1/α(E*) = 80.5  (exact midpoint)
- 1/α(∞) = 24  (exact)
- Only free parameter: E* (the crossover energy)

This is a Lorentzian dispersion curve — the simplest
function that interpolates between 137 and 24 with a
well-defined midpoint.


### F3. Fitting to α(m_Z) gives E* ≈ 310 GeV

Requiring 1/α(m_Z = 91.2 GeV) = 128 gives:

    E* = 310 GeV = 3.4 × m_Z = 330 × m_p

This is 1.26 × the Higgs vacuum expectation value
(v = 246 GeV), placing it at the electroweak scale.
No T⁶ geometric scale corresponds to 310 GeV.


### F4. The Lorentzian shape does not match SM running

The SM running is logarithmic: 1/α changes by ~9 between
E = 0 and m_Z, with most of the running occurring at
threshold crossings (fermion masses).

The Lorentzian is qualitatively different: it is flat at
both extremes and runs fastest at E*.  Comparison:

| Energy | SM 1/α | Lorentzian | Error |
|--------|--------|------------|-------|
| 0 | 137.0 | 137.0 | 0% |
| m_μ (106 MeV) | 135.9 | 137.0 | 0.8% |
| m_p (938 MeV) | 134 | 137.0 | 2.2% |
| m_Z (91.2 GeV) | 128 | 128.0 | 0% (fit) |
| m_H (125 GeV) | 127 | 121.2 | 4.6% |
| m_t (173 GeV) | 126 | 110.2 | 12.6% |
| 1 TeV | 125 | 33.9 | 72.9% |

Average error: 10.7%.  The model works below m_Z
(within ~3%) but catastrophically fails above m_Z.

The failure above m_Z means the Lorentzian cannot be
the full story.  The UV convergence to 1/24 (if real)
must happen much more slowly — logarithmically, not as
a power law.


### F5. Using T⁶ geometric scales for E* gives wrong running

| E* choice | 1/α at m_p | 1/α at m_Z | Comment |
|-----------|-----------|-----------|---------|
| Proton ring (467 MeV) | 46 | 24 | Way too fast |
| m_p (938 MeV) | 80.5 | 24 | Too fast |
| 2 GeV (T⁶ horizon) | 117 | 24 | Too fast |
| 310 GeV (fit) | 137 | 128 | Matches at m_Z |
| m_Z (91.2 GeV) | 137 | 73 | Overshoots |

Only E* ≫ m_Z gives a good fit at intermediate energies,
but then the UV convergence to 24 happens too slowly
(beyond Planck scale).  No T⁶ geometric scale works.


### F6. The midpoint scale has electroweak character

E* = 310 GeV ≈ 1.26 v (Higgs VEV).  This is NOT derived
from T⁶ geometry — it is the electroweak symmetry breaking
scale, which the T⁶ model does not yet address.

If 1/α truly passes through 80.5, it does so at or near
the scale where the Higgs mechanism operates.  This could
mean:
1. The Higgs VEV sets the resonance scale (Higgs as the
   "boundary" between compact and spatial physics)
2. It's a coincidence (310 ≠ 246; off by 26%)
3. The T⁶ model needs to incorporate electroweak physics
   to address the running at this scale


---

## Track 2 — Logarithmic running from 1/α₀ = 80


### F7. Ghost suppression factor f ≈ 6 × 10⁻⁵ fits the IR endpoint

To produce 57 units of screening (from 1/80 to 1/137)
via QFT logarithmic running, the ghost modes require a
suppression factor f ≈ 3–6 × 10⁻⁵ (depending on the
cutoff scale).  This is within the ~10⁻⁵ range established
by R31 (Lamb shift) and R32 (catastrophic running).

The SM fermions contribute only 2.7% of the total
screening.  Ghost modes provide 97.3%.


### F8. NULL RESULT: 1/α(m_Z) ≈ 101, not 128

With a 1 TeV cutoff, the model gives 1/α(m_Z) = 101 —
27 units below the measured 128.  The discrepancy shrinks
with higher cutoffs but persists:

| Cutoff | f | 1/α(m_Z) | Δ from 128 |
|--------|---|----------|------------|
| 1 TeV | 6.1 × 10⁻⁵ | 101 | −27 |
| 10 TeV | 4.5 × 10⁻⁵ | 110 | −18 |
| 100 TeV | 3.5 × 10⁻⁵ | 116 | −12 |
| 1 PeV | 2.9 × 10⁻⁵ | 119 | −9 |

Extrapolating: the model would reach 128 at a cutoff
of ~10¹² GeV (EeV scale).  This is below the GUT/Planck
scale but implies the "bare" coupling is defined at an
extremely high energy.


### F9. Root cause: ghost modes are too concentrated at low energy

The T⁶ mode spectrum puts most charged ghost modes below
2 GeV (41,616 out of 78,608).  These modes contribute
their screening mostly below 2 GeV, making the running
very fast at low energies and nearly flat above.

By m_Z, the ghost modes have already contributed most of
their screening (21 out of 55 units at 1 TeV cutoff).
The remaining screening between m_Z and E = 0 is only
~36 units instead of the needed 48 (= 128 − 80).

In the SM, running is spread over a wide energy range
because charged fermions span masses from 0.5 MeV (electron)
to 173 GeV (top).  In T⁶, the ghost modes cluster below
the predictive horizon (~2 GeV), causing front-loaded
running.


### F10. The discrepancy shrinks with higher cutoffs

As the cutoff increases:
- Each mode contributes more screening (larger ln(Λ/m_k))
- The relative contribution of high-mass vs low-mass modes
  shifts: at m_Z, only modes with m < m_Z contribute
- The fraction of total screening below m_Z decreases

1/α(m_Z) improves from 101 (1 TeV) to 119 (1 PeV).
Extrapolating: would reach ~128 at ~10¹² GeV cutoff.


### F11. The uniform-f model is the simplest, not the only, model

Track 2 tested a UNIFORM ghost suppression factor: every
ghost mode couples at the same fraction f of full strength.
This is the simplest assumption but not the most physical.

Untested models that could fix the m_Z discrepancy:

1. **Mass-dependent suppression**: f(m) decreasing with
   mass.  If lighter ghosts are more suppressed, less
   running would occur below 2 GeV, spreading it more
   evenly.

2. **Winding-number-dependent suppression**: modes with
   higher quantum numbers couple more weakly (R33 Track 4
   hypothesis).  This would preferentially suppress the
   many complex low-mass modes.

3. **Known T⁶ particles beyond e/p**: the muon, tau,
   pion, kaon, Lambda, Sigma are identified T⁶ modes
   (R27, R28) and should couple at full strength.
   Including these (~7 modes at 100–1200 MeV) would add
   non-ghost screening at intermediate energies.

4. **Higher-mass ghost modes**: the enumeration truncated
   at n_max=8.  Higher modes extend above 1000 TeV and
   could contribute above m_Z.

The null result applies to the uniform-f model, not to
the 1/80 hypothesis in general.


### F12. α = 1/137 is an input, not an output, of the T⁶ model

The R19 shear-charge formula α = r²μ sin²(2πs)/(4π(2−s)²)
has two free parameters (r and s).  The shear s is solved
from the requirement α = 1/137.  So the formula provides
a MECHANISM for how geometry produces a coupling constant
(shear → charge leakage), but does not DERIVE the value
1/137.

Similarly, 1/80 from the weighted gauge partition is a
geometric property of the metric channel distribution.
It describes how energy is partitioned among the 10D
metric components, weighted by the inverse-squared
circumferences.

Whether 137 and 80 are related (by running, dispersion,
or some other mechanism) remains open.  Track 2 showed
that uniform-f QFT running doesn't produce the right
profile, but more sophisticated models have not been
tested.


---

## Track 5 — Running with known T⁶ particles only


### F13. T⁶ particle content runs α ~2.4× too fast

With ONLY empirically confirmed T⁶ particles (no ghost
modes), the total screening from m_e to m_Z is:

    Δ(1/α) = 21.9  (T⁶ known particles)
    Δ(1/α) = 7.0   (SM one-loop)
    Δ(1/α) = 9.0   (measured)

This gives 1/α(m_Z) = 115, not 128.  The T⁶ model
overshoots the measured running by a factor of ~2.4.

Note: the SM one-loop also undershoots (7.0 vs 9.0)
because it omits higher-order corrections and non-
perturbative hadronic VP.  But the T⁶ error is in the
opposite direction and much larger.


### F14. The T⁶ running rate is 4.1× the SM rate

The total vacuum-polarization coefficient is:

    T⁶:  Σ b×Q² = 44.0   (23 charged species)
    SM:   Σ N_c×b×Q² = 10.7  (9 species × color)

The ratio is 4.1, driven by:
- 15 charged baryons at b = 4/3 each (vs 3 leptons in SM)
- Δ⁺⁺ with Q = +2 contributing Q² = 4 (11% alone)
- No color factor ×3, but compensated by many more species
- Vector mesons ρ± and K*± at b = 7 (32% of total)


### F15. Vector mesons dominate the uncertainty

The vacuum-polarization coefficient for massive spin-1
(Proca) fields is b = 7, much larger than b = 4/3
(Dirac) or b = 1/3 (scalar).  The ρ± and K*± together
contribute 32% of the total T⁶ screening.

Sensitivity:
    b_vector = 1/3:   Δ(m_e→m_Z) = 15.3
    b_vector = 4/3:   Δ(m_e→m_Z) = 16.3
    b_vector = 7:     Δ(m_e→m_Z) = 21.9

Even minimizing the vector contribution (b = 1/3),
Δ = 15.3 is still 70% above the measured 9.0.  The
overshooting is not solely due to the vector meson
coefficient.


### F16. The cutoff for 1/α₀ = 80 is ~168 TeV

With only known T⁶ particles, the cutoff needed to
accumulate 57 units of screening (from 80 to 137) is:

    T⁶: Λ = 168 TeV  (log₁₀ Λ/GeV = 5.2)
    SM:  Λ = 1.6 × 10²¹ GeV  (beyond Planck)

The T⁶ model reaches 1/α₀ = 80 at a much lower scale
because it runs faster.  168 TeV is above the LHC
(~14 TeV) but well below the GUT scale — it would
be accessible to a ~100× more powerful collider.


### F17. Charged baryons and Δ⁺⁺ are the distinctive T⁶ contribution

In the SM, protons do not appear in vacuum polarization
loops (quarks do).  In T⁶, the proton is fundamental
and contributes directly.  The per-particle breakdown
from m_e to m_Z:

    e⁻:     1.71  (7.8%)    ← same in both models
    μ⁻:     0.96  (4.4%)    ← same
    τ⁻:     0.56  (2.5%)    ← same
    π±:     0.23  (1.0%)    ← replaces u,d quarks
    K±:     0.18  (0.8%)    ← replaces s quark
    ρ±:     3.54  (16.1%)   ← no SM analogue
    K*±:    3.44  (15.7%)   ← no SM analogue
    p:      0.65  (3.0%)    ← no SM analogue (quarks instead)
    Δ⁺⁺:   2.44  (11.1%)   ← Q=+2, no SM analogue
    Other baryons: 6.15 (28.0%)

The 3 leptons contribute identically in both models
(3.23 total).  The difference is entirely in the
hadronic sector: T⁶ hadrons contribute 18.7 vs SM
quarks' 3.75 (a factor of 5×).


### F18. Open question: should short-lived resonances contribute?

Many of the T⁶ baryons are extremely short-lived:
- Δ resonances: τ ~ 10⁻²³ s (strong decay)
- N* resonances: τ ~ 10⁻²³ s
- ρ±: τ ~ 4 × 10⁻²⁴ s

In the SM, these are not fundamental — they're composite
resonances and do NOT appear as separate VP contributions.
Instead, their effect is implicitly included in the non-
perturbative hadronic VP (computed from e⁺e⁻ data).

In T⁶, they ARE fundamental modes.  But their extreme
instability (widths Γ ~ 100–300 MeV, comparable to their
masses) raises the question: should a mode with Γ ~ m
really be treated as a sharp mass threshold in the VP
sum?  Or should its contribution be smeared over a wide
energy range, effectively diluting its impact?

This is not a small effect: the Δ, N*, ρ, and K*
together account for ~75% of the T⁶ screening.  If
their contribution is reduced by form factors or width
effects, the T⁶ running could approach the measured
value.


---

## Track 3 — Backing into the shear


### F19. The shear scales as √α, with identical ratio on both sheets

Solving s from α₀ = 1/80 instead of 1/137:

    Electron: s goes from 0.01029 to 0.01347 (ratio 1.308)
    Proton:   s goes from 0.00764 to 0.00999 (ratio 1.308)

The ratio is identical for both sheets and equals
√(137/80) = 1.308.  This is expected: for small s,
sin(2πs) ≈ 2πs, so α ∝ s² and s ∝ √α.

The shear encodes the coupling directly, and changing
the target α simply rescales s by √(α_new/α_old).


### F20. Neither shear matches any obvious geometric constant

Tested against 1/2π, 1/r, 1/12, 1/24, √α, and 18
other candidates.  The only near-matches:

    s_e(137) ≈ 1/100   (ratio 1.029 — 3% off)
    s_p(80)  ≈ 1/100   (ratio 0.999 — 0.1% off!)

The s_p(80) ≈ 1/100 match is striking (0.1% accuracy)
but may be coincidental given that 1/100 has no known
geometric significance for tori.  The proton shear for
α₀ = 1/137 gives s_p(137) ≈ α (ratio 1.046 — 5% off).


### F21. The prefactor is nearly s-independent

Decomposing α = prefactor(r,s) × sin²(2πs):

    Electron: prefactor = 1.747 (at s₁₃₇) vs 1.750 (at s₈₀)
    Proton:   prefactor = 3.173 (at s₁₃₇) vs 3.177 (at s₈₀)

The prefactor r²μ/(4π(2−s)²) depends very weakly on s
(because s ≪ 2).  All the variation in α comes from
sin²(2πs).  The formula is effectively:

    α ≈ C(r) × (2πs)²    for small s

where C(r) = r²√(1/r² + 4) / (16π) is determined
entirely by the aspect ratio.

    C(r_e = 6.6) = 1.747
    C(r_p = 8.906) = 3.173


### F22. The standard denominator 4π(2−s)² ≈ 50, not 24

    Electron: 4π(2−s)² = 49.75
    Proton:   4π(2−s)² = 49.88
    Ratio to 24:  ~2.07

Replacing the denominator with 24 (gauge channel count)
approximately doubles α.  With the standard shear
(from 1/137), the 24-denominator formula gives α ≈ 1/66,
not 1/137 or 1/80.


### F23. The shear is a continuous free parameter with no selection

The α formula can produce any value of α between 0 and
~2 (for r_e) by varying s from 0 to ~0.26.  There is
no potential minimum, quantization condition, or
topological constraint that selects a particular s.

This confirms F12: the formula provides a MECHANISM
(shear → charge leakage → coupling) but not a VALUE.
To derive α from geometry, one needs a dynamical
principle that fixes s — such as energy minimization,
modular invariance, or a variational condition on the
metric.
