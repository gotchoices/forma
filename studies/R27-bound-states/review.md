# R27 Review — r_p pinning verification

Reviewed 2026-03-28.  Focus: is r_p = 8.906 correct?

---

## Summary

**r_p = 8.906 is correct.**  Both neutron candidates give the same
r_p to 4 significant figures.  The reported σ_ep = -0.0906 is correct
for Candidate A (the preferred neutron mode).

---

## The two neutron candidates

R27 F10 identified two self-consistent neutron modes:

| | Candidate A | Candidate B |
|---|---|---|
| Mode | (0, -2, n₃_odd, 0, 0, +2) | (0, -5, n₃_odd, 0, 0, -2) |
| n₂ (electron tube) | -2 | -5 |
| n₆ (proton tube) | +2 | -2 |
| Preferred? | Yes (simpler quantum numbers) | No |

The findings (F15, F18) describe the neutron as Candidate A.
The track3 script (`track3_neutron_discovery.py` line 110) uses
Candidate B for the σ_ep pinning search:

```python
n_neutron = np.array([0, -5, -5, -5, 0, -2], dtype=float)
```

This is a discrepancy between the script and the findings.

## Does the discrepancy matter?

Independently recomputed the simultaneous neutron+muon crossing
for both candidates:

| | Candidate A | Candidate B |
|---|---|---|
| r_p at muon crossing | **8.9060** | **8.9038** |
| σ_ep at that r_p | -0.0906 | -0.0991 |
| m_n - m_p | 1.293 MeV (exact) | 1.293 MeV (exact) |
| E(muon) | 105.658 MeV (exact) | 105.658 MeV (exact) |

**r_p agrees to 4 significant figures** (Δr_p = 0.002).  The muon
mode energy is dominated by proton-scale dimensions, which are
nearly identical for both candidates.

**σ_ep differs by ~9%** (-0.091 vs -0.099).  This matters for any
downstream computation that depends on σ_ep (e.g., particle masses
in Track 5).

## Which candidate is actually correct?

Track 5 (`track5_particle_catalog.py`) performs an independent
mode search at the pinned point (r_p=8.906, σ_ep=-0.09064).
Searching all (n1, n2, n5, n6) with |n| ≤ 8 for charge=0, spin=½
nearest to 939.565 MeV, the search finds:

    Best: n2=-2, n6=+2, E=939.564992 MeV  → Candidate A

Candidate B at the same parameter point gives E = 939.709 MeV
(off by 0.14 MeV).  **Candidate A is the correct neutron mode
at the reported parameters.**

## How the findings got it right despite the script

The track3 script was an exploration tool — it used Candidate B
to map the σ_ep(r_p) landscape and find the approximate region
where the muon crosses.  The final reported values in F18 were
then verified at the Candidate A solution.  The track5 independent
search confirms Candidate A is the best match.

The numbers in the findings (r_p=8.906, σ_ep=-0.0906) are correct
for Candidate A.  They would be wrong if interpreted as coming from
the track3 script's Candidate B computation.

## Recommendation

The track3 script should be annotated to clarify that it explored
Candidate B during the search, and that the final parameters in
F18 were determined using Candidate A.  Alternatively, the script
could be updated to use Candidate A (changing line 110 to
`n_neutron = np.array([0, -2, 1, 0, 0, 2])`), though this is
cosmetic since the script is not the authoritative source for the
pinned values.
