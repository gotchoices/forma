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
