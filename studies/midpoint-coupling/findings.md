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
