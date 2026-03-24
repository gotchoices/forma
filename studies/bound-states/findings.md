# R27 Findings

## Track 1. Self-consistent neutron mass

Scripts: [`scripts/track1_neutron_mass.py`](scripts/track1_neutron_mass.py),
[`scripts/track1b_asymmetric.py`](scripts/track1b_asymmetric.py)


### F1. Library validation — R26 results reproduced exactly

The shared T⁶ library (`lib/t6.py`) reproduces all R26 reference
results at zero cross-shear:

    electron (1,2,0,0,0,0):  E = 0.5110 MeV  ✓
    proton   (0,0,0,0,1,2):  E = 938.272 MeV  ✓
    neutrino Δm²₃₁/Δm²₂₁ = 33.61     (target: 33.60) ✓
    metric condition number = 1.25      ✓

The naive neutron mass match (σ_ep ≈ 0.038, R26 F67) is
also reproduced.  At that σ_ep, the proton mode has shifted
to 939.585 MeV, confirming R26 F74.


### F2. Self-consistent treatment inverts the neutron mass prediction

When circumferences L₂ and L₆ are iteratively adjusted so that
E(1,2,0,0,0,0) = m_e and E(0,0,0,0,1,2) = m_p exactly at each
σ_ep, the neutron mode (1,2,0,0,1,2) becomes LIGHTER than the
proton:

    σ_ep = +0.038:  m_n − m_p = −0.0195 MeV  (wrong sign)
    σ_ep = +0.100:  m_n − m_p = −0.0523 MeV
    σ_ep = +0.300:  m_n − m_p = −0.1809 MeV
    σ_ep = +0.500:  m_n − m_p = −0.4310 MeV

The self-consistency correction (enlarging L₂ and L₆ to keep m_e
and m_p fixed) more than compensates for the cross-shear energy
increase.  The neutron mode gets a "double dose" of the
circumference reduction — it has components on both the electron
and proton sheets — while the individual particles each get only
a single correction.

This OVERTURNS the naive R26 F67 result.  Positive symmetric
σ_ep cannot produce m_n > m_p self-consistently.


### F3. Negative σ_ep gives m_n > m_p

The sign of σ_ep matters in the self-consistent treatment (unlike
the naive case, where ΔE ∝ σ² was symmetric):

    σ_ep = −0.010:  m_n − m_p = +0.0053 MeV
    σ_ep = −0.100:  m_n − m_p = +0.0526 MeV
    σ_ep = −0.300:  m_n − m_p = +0.1811 MeV
    σ_ep = −0.500:  m_n − m_p = +0.4310 MeV
    σ_ep = −0.530:  m_n − m_p = +0.4981 MeV  (near positivity limit)

The relationship is approximately linear: m_n − m_p ≈ −σ_ep × 0.94.
The maximum achievable value before the metric becomes singular is
about +0.50 MeV at σ_ep ≈ −0.53.

This falls short of the measured m_n − m_p = 1.293 MeV by a
factor of ~2.6.


### F4. Aspect ratios have negligible effect on the neutron mass gap

Surveying r_e and r_p from 2.0 to 15.0 at σ_ep = −0.50:

    All (r_e, r_p) combinations give m_n − m_p ≈ 0.43 ± 0.02 MeV

The maximum variation is only ±4% across the entire aspect ratio
space.  The neutron mass gap is controlled almost entirely by
σ_ep, not by the aspect ratios.


### F5. Asymmetric cross-shears offer modest improvement

Scanning all 4 individual cross-shear entries (σ₁₅, σ₁₆, σ₂₅,
σ₂₆) independently:

    Best symmetric (collective) σ_ep:          +0.50 MeV
    Best asymmetric ("checkerboard" pattern):   +0.25 MeV

The "checkerboard" pattern (σ₁₅ = −σ₁₆ = σ₂₅ = −σ₂₆ ≈ 0.35)
corresponds to a relative twist between the tube and ring axes
of the two T² sheets.  It is worse than pure negative symmetric
σ_ep, not better.

Half of the 6560 tested asymmetric configurations give m_n > m_p,
but none exceed +0.50 MeV.


### F6. Alternative charge-neutral modes exist near m_n

At σ_ep = 0.1, the T⁶ spectrum contains charge-0, spin-½ modes
near the neutron mass:

    Mode (0, −3, n₃_odd, n₄, 0, 2):  E = 939.20 MeV
    m_n − m_p = +0.93 MeV

These are NOT the (1,2,0,0,1,2) neutron candidate.  They have:
- n₁ = 0 (no electron tube winding → no electron charge)
- n₂ = −3 (electron ring winding → contributes to mass)
- n₃ = odd (neutrino tube → gives spin ½)
- n₅ = 0 (no proton tube → no proton charge)
- n₆ = 2 (proton ring → contributes ~m_p to mass)

Their charge is zero and their spin is ½, but through a
different mechanism than the (1,2,0,0,1,2) mode: the spin
comes from the neutrino tube winding, not from having two
cancelling tube windings.

These modes are degenerate in n₃ and n₄ (the neutrino dimensions
contribute negligible energy at the mm scale).  The energy is
set almost entirely by n₂ and n₆.

Caveat: these modes were computed at a single non-self-consistent
point.  A full self-consistent analysis at varied σ_ep is needed
to determine whether any of them hit m_n exactly.


### F7. The (1,2,0,0,1,2) neutron hypothesis is quantitatively insufficient

The single-mode neutron (1,2,0,0,1,2) with symmetric or
asymmetric cross-shear cannot achieve m_n − m_p = 1.293 MeV
under self-consistent treatment.  The maximum is ~0.50 MeV
(39% of the target).

The qualitative features survive: the mode is charge-neutral
and naturally heavier than the proton (for negative σ_ep).
But the quantitative prediction fails by a factor of ~2.6.

Possible paths forward:

1. **Alternative quantum numbers.**  The (0, −3, n₃, n₄, 0, 2)
   modes (F6) achieve 0.93 MeV at σ_ep = 0.1.  A self-consistent
   sweep might hit 1.293 MeV.  However, the physical picture is
   different: the neutron would be a proton-ring mode with
   neutrino-tube spin, rather than a "proton+electron" hybrid.

2. **Non-symmetric cross-shear blocks.**  The current study
   uses σ_ij = σ for all 4 pairs in a block, or varies them
   independently within a grid.  A continuous optimization over
   all 12 cross-shears simultaneously might find a sweet spot.

3. **Multi-mode neutron.**  The neutron might not be a single
   T⁶ mode but a bound state of multiple modes — analogous to
   how the standard model treats it as three quarks.  This would
   require the multi-mode formalism (R27 Track 2).

4. **Cross-block coupling.**  The current scan varied only the
   e-p block.  Including σ_eν and σ_νp simultaneously might
   open parameter space where (1,2,0,0,1,2) achieves higher
   m_n − m_p through indirect effects on the metric inverse.


### F8. Summary of Track 1

The self-consistent neutron mass calculation was the most
important prerequisite for the bound-state program.  Its
result is sobering: the straightforward (1,2,0,0,1,2) mode
with symmetric cross-shear cannot quantitatively reproduce
m_n − m_p = 1.293 MeV.

However, the result is not a dead end:

- **Negative σ_ep** is a genuine discovery — the sign breaks the
  naive quadratic symmetry and gives the correct sign for m_n > m_p.

- **Alternative modes** (F6) come closer to the target and need
  self-consistent investigation.

- **The qualitative neutron picture is intact:** a charge-neutral,
  heavier-than-proton, unstable cross-sheet excitation that decays
  to e + p + ν.  The specific quantum numbers may need revision.

R26's emergent neutron narrative (charge cancellation, natural
instability, m_n > m_p from geometry) remains correct in spirit.
The quantitative identification of which mode IS the neutron is
the open problem.
