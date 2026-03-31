# Q99. The fourth neutrino mode — hidden partner or tension?

**Status:** Open — testable prediction
**Related:**
  [Q86](Q86-three-generations.md) (three generations),
  [Q97](Q97-shear-chirality-and-cp-violation.md) (shear chirality),
  [Q98](Q98-quark-generations-vs-lepton-generations.md) (generation asymmetry),
  [Q78](Q78-neutrino-sheet-access.md) (neutrino sheet access),
  [Q83](Q83-neutrino-sheet-coherence.md) (neutrino sheet coherence),
  R26 F31–F39 (Assignment A final resolution),
  R38 F4 (4th neutrino species identified)

---


## 1. The mode

Assignment A identifies three active neutrinos on Ma_ν:

| Mode | Mass (meV) | Status |
|------|-----------|--------|
| ν₁ = (1, 1) | 29.21 | active |
| ν₂ = (−1, 1) | 30.47 | active |
| ν₃ = (1, 2) | 58.17 | active |
| **(−1, 2)** | **59.45** | **4th species** |

The 4th mode is not the CPT conjugate of any of the three
identified neutrinos.  Its CPT partner is (1, −2), which has
the same mass (59.45 meV).  The (−1, 2) mode is a genuinely
new species — weakly charged (|n₃| = 1), spin-½, sitting only
1.28 meV above ν₃.

This mode is not optional.  It exists in the Ma_ν spectrum as
inevitably as ν₃ does.  The question is why it hasn't been
observed.


## 2. The Z width tension

The Z boson invisible width gives N_ν = 2.996 ± 0.007 — three
active neutrinos, not four.  At Z-decay energies (~91 GeV), a
59 meV neutrino is kinematically indistinguishable from a 58 meV
one.  If (−1, 2) couples to the Z with standard strength, it
contributes a full unit to N_ν, pushing the prediction to ~4.
This is excluded at >140σ (R38 F5).


## 3. Resolution: shear chirality suppression

The modes (1, 2) and (−1, 2) differ only in the sign of n₃ —
they wind around the tube in opposite directions.  On a sheared
torus (s₃₄ ≠ 0), this symmetry is broken.

The cross-plane shear σ_eν that couples Ma_ν to Ma_e (producing
the PMNS mixing matrix) acts along a preferred direction.  Modes
that co-wind with the shear couple strongly; modes that
counter-wind couple weakly.  This is the same chirality mechanism
proposed in Q97 for matter-antimatter asymmetry, applied to
neutrino flavor coupling.

If (−1, 2) counter-winds relative to σ_eν, its coupling to
flavor eigenstates (ν_e, ν_μ, ν_τ) is suppressed.  The PMNS
mixing elements |U_{α4}|² would be small.  Consequences:

- **Z width:** The 4th species contributes |U_{α4}|² to N_ν
  instead of a full unit.  If |U_{α4}|² ≲ 0.01, the
  contribution is ≲0.01 — within the Z width error bar.
- **Oscillation:** The 4th mode barely participates.  Standard
  3-neutrino fits remain good approximations.
- **Status:** Effectively sterile, not by fiat, but by the
  geometry of the shear.


## 4. Near-degenerate averaging

Even without coupling suppression, the near-degeneracy of ν₃
and ν₄ makes them hard to distinguish.

The mass-squared splitting:

    Δm²₄₃ = m₄² − m₃² ≈ 1.5 × 10⁻⁴ eV²

This is ~2× the solar splitting (Δm²₂₁ = 7.5 × 10⁻⁵ eV²)
and ~1/17 the atmospheric splitting (Δm²₃₁ = 2.5 × 10⁻³ eV²).

At atmospheric baselines (L ~ 300–1000 km), the ν₃-ν₄
oscillation frequency is high enough to be fully averaged.
Experiments see the average of ν₃ and ν₄ as a single effective
state with mass ≈ 58.8 meV and averaged mixing parameters.

At reactor baselines (~50–100 km), the splitting could in
principle be resolved.  The oscillation length for Δm²₄₃:

    L_osc = 4πE / Δm²₄₃ ≈ 83 km × (E / 1 MeV)

For reactor antineutrinos (E ~ 3 MeV), L_osc ≈ 250 km.
This is within the range of JUNO (baseline ~53 km) and
KamLAND (baseline ~180 km).

If both averaging and coupling suppression operate
simultaneously, the 4th mode is doubly hidden — its
oscillation signature is both weak (small mixing) and
partially averaged (comparable frequency to solar
oscillations).


## 5. Testable prediction

JUNO is designed to measure the neutrino mass ordering by
resolving the atmospheric-scale oscillation pattern at
~53 km baseline.  Its energy resolution (~3% at 1 MeV) is
sufficient to detect spectral distortions from a 4th mass
eigenstate at Δm²₄₃ ~ 10⁻⁴ eV², provided the mixing angle
is not too small.

Prediction: if the shear chirality suppression gives
|U_{α4}|² ~ 0.01–0.05, JUNO might see a subtle spectral
distortion consistent with a near-degenerate pair at
Δm² ~ 1.5 × 10⁻⁴ eV².  If |U_{α4}|² < 0.01, the effect
is below JUNO's sensitivity and requires next-generation
precision.


## 6. The decisive calculation

What determines whether this mode is hidden or exposed is
the coupling asymmetry between n₃ = +1 and n₃ = −1 modes
under the cross-plane shear σ_eν.

R26 F35 established that the surface parallel transport rule
gives equal weak charge to all |n₃| = 1 modes.  But this
was computed at zero cross-shear.  At nonzero σ_eν, the
cross-plane coupling could break the n₃ → −n₃ degeneracy
in the weak coupling strength.  Computing this asymmetry
requires extending the R26 Track 1e charge transport
calculation to the full 6D Ma metric with σ_eν ≠ 0.

This is the single most important calculation for resolving
the 4th neutrino question.


## 7. Speculative: biological relevance

*This section is exploratory and may belong in a future study
rather than the core physics.*

Q78 and Q83 propose that biological cells interact with Ma_ν
through neutron gateways (cross-shear coupling via σ_eν and
σ_νp).  If this coupling exists, the near-degenerate ν₃-ν₄
pair has a property that makes it biologically interesting.

The two modes differ only in tube-winding direction.  A cell's
electromagnetic field, mediated through the cross-shear, could
preferentially excite one winding direction over the other.
By modulating which mode it drives — (1, 2) vs (−1, 2) — a
cell could encode information into the beat between them.

The beat frequency:

    Δf = (59.45 − 58.17) meV / h ≈ 310 GHz

This is in the sub-THz range, within the band of molecular
vibrations and membrane dynamics.

Both individual modes are thermally protected at 300 K
(each has T_d ~ 680 K, well above body temperature; Q83).
The carrier is coherent; only the modulation pattern
(which mode is populated) encodes information.  This is
closer to frequency-shift keying (FSK) than continuous FM:
the cell switches between two protected carrier frequencies
to encode bits.

If the shear chirality argument (§3) is correct, one winding
direction couples more strongly to ordinary matter than the
other.  A cell would have a natural "loud" channel
(co-winding) and a natural "quiet" channel (counter-winding).
Shifting energy from the loud mode to the quiet mode — or
vice versa — would produce a detectable change in the
neutrino-sheet coupling strength at the 310 GHz beat
frequency.

This connects the 4th neutrino mode to the existing
biological framework (Q78, Q79, Q83) and reframes it from
a Z-width tension into a potential communication mechanism.
Whether the coupling is strong enough for biological
relevance depends on the per-neutron transfer rate (Q78
open question 1).
