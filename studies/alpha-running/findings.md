# R32. Findings

## Track 1 — KK mode running of α

### F1. The T⁶ has ~78,000 charged modes below 1000 TeV

With n_max = 8 for the electron/proton sheets (neutrino
excluded — correctly, since neutrino-only modes have Q = 0),
the T⁶ spectrum contains 78,608 charged modes.  Of these:

- 41,616 below 2 GeV  (vs ~40 known particles in this range)
- 78,608 below 1000 TeV

Classification by spin:
- 20,808 bosons (spin 0)
- 41,616 fermions (spin ½)
- 16,184 ambiguous (2×½ → spin 0 or 1)


### F2. The lightest charged T⁶ mode is 39 keV — not the electron

The mode (−1, 0, 0, 0, 0, 0) has charge −1 and mass
~39 keV (from the electron tube, L₁ ≈ 32,000 fm).  This
is 13× lighter than the electron.  There are 112 charged
modes below the electron mass (0.511 MeV).

These sub-electron charged modes are not observed in
nature.  The electron IS the lightest charged particle.
This is a known structural issue: on the electron T²,
modes with n₂ = 0 (no ring winding) are lighter than
(1,2) but carry charge.  The WvM spin mechanism
requires n₂ = 2 for spin ½, which is why the electron
is the lightest charged FERMION — but charged bosons
with n₂ = 0 exist at lower masses in the T⁶ spectrum.

These modes might be excluded by a selection rule not
yet identified (spin-statistics, stability, coupling).


### F3. Naive KK running is catastrophically fast

If all charged modes contribute to vacuum polarization
as independent quantum fields (standard one-loop QFT),
the running of 1/α is ~157,000× faster than the SM:

| Energy | SM 1/α | T⁶ 1/α (naive) |
|--------|--------|-----------------|
| 0 (input) | 137.0 | 137.0 |
| 0.5 MeV | 137.0 | 86 |
| 1 MeV | 137.0 | **−33** (Landau pole) |
| m_Z (91 GeV) | 127.9 | **−1,427,752** |

The Landau pole (1/α → 0) occurs at approximately 1 MeV.
This is completely incompatible with observation.

**The SM running**: Δ(1/α) = −9.1 from 0 to m_Z, from
~12 charged species (e, μ, τ, u, d, s, c, b quarks, W).

**The T⁶ running**: Δ(1/α) = −1,427,752 from 0 to m_Z,
from ~78,000 charged modes.


### F4. Ghost modes CANNOT contribute as independent quantum fields

This is the central finding.  The catastrophic running
provides independent confirmation of R31 Track 4:

- **R31 Track 4**: Naive KK Yukawa corrections to the
  Lamb shift exceed observation by 10⁵ → massive KK mode
  coupling must be suppressed by ≥10⁵.

- **R32 Track 1**: Naive KK vacuum polarization from the
  mode spectrum exceeds observation by ~10⁵ → massive KK
  mode contribution to running must be suppressed by a
  comparable factor.

Both results point to the same conclusion: the massive
modes of the T⁶ do not couple to the electromagnetic field
with the same strength as the zero mode (photon).  The
ghost modes are geometrically present (they are valid
solutions of the wave equation on T⁶) but electromagnetically
suppressed.


### F5. Suppression factor estimate

If each ghost mode's contribution is suppressed by a factor
κ, the total running from 0 to m_Z would be:

    Δ(1/α) = κ × (−1,427,752) ≈ −9.1  (SM value)

This gives κ ≈ 6.4 × 10⁻⁶, or suppression by a factor of
~160,000.  This is consistent with the R31 Track 4 estimate
of ≥10⁵ suppression for KK massive mode coupling.

The agreement between two independent observables (Lamb
shift and running of α) both requiring ~10⁵ suppression
is suggestive of a common geometric origin.


### F6. 1/α passes through 24 at ~1 MeV (but not as convergence)

In the naive (unsuppressed) running, 1/α drops through
~24 at approximately 1 MeV.  This is on the steep descent
to the Landau pole — not a stable convergence point.

The fact that the crossing energy (~1 MeV) is close to
the electron mass scale is notable but likely coincidental
given the catastrophic nature of the unsuppressed running.

Whether the SUPPRESSED running converges to 1/24 at some
higher energy depends on the spectrum of suppression
factors, which is not yet known.


### F7. The charge formula produces sub-electron charged modes

The charge formula Q = −n₁ + n₅ allows modes with n₁ = ±1
and all other quantum numbers zero.  These have charge ±1
and mass ~39 keV (from the electron tube circumference).
Their existence is a structural consequence of the charge
mechanism: charge requires only a single tube winding, but
the electron's mass requires both n₁ = 1 AND n₂ = 2.

Possible resolutions:
1. A selection rule (spin-statistics) excludes charged
   bosons from propagating
2. These modes are produced but instantly decay (lifetime
   ≪ any measurement)
3. They couple too weakly to be produced in any reaction
   (consistent with F4)

This is an open issue for the model.
