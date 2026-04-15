# Q54. Is the dipole radiation pattern route to α effectively ruled out?

**Status:** Open — likely negative but uncomputed
**Source:** User question, R18 Track 2 analysis
**Connects to:** R15 F8 #6, R18 F7, Q51
**Model era:** Model A

R15 F8 Candidate 6 proposed: the circularly polarized photon's radiation pattern (power ∝ (1 + cos²Θ)/2) deforms the tube cross-section, breaking the θ-symmetry and enabling mode coupling to the charge-carrying (1,0) mode.

R18 tested a closely related mechanism (cos(2φ) deformation of the major radius) and found it fails: the Coulomb cost of the charge exceeds the photon energy saving by 96×.

For the dipole radiation pattern specifically:
- The radiation pattern rotates WITH the photon along the (1,2) geodesic, so the deformation depends on (θ+2φ), the same combination as the mode itself.
- Products like cos(θ+2φ) × f(θ+2φ) × cos θ still integrate to zero over the full torus because the φ-integral kills any n ≠ 0 harmonic.
- Time-averaged field energy density on the symmetric torus is φ-UNIFORM (the oscillating part averages away), so the time-averaged tube deformation is also uniform — no symmetry breaking.

The mechanism likely falls to the same φ-symmetry protection that kills R18. But a direct computation of the NEAR-FIELD radiation pattern (not the far-field dipole approximation) on the curved torus surface has NOT been done. The near-field pattern could have contributions at harmonics other than (θ+2φ), which might evade the protection.

Status: likely ruled out by the same φ-symmetry protection (R18 F7), but not yet directly computed. Low priority.
