# Q18: Can α be derived from geometry?

**Status:** Open — active research front  
**Source:** S2-toroid-geometry F6, R7, R8 Tracks 4–5, R1, R11, R12  
**Related:** [Q29](Q29-variational-principle-alpha.md), [Q30](Q30-prime-q-harmonic-avoidance.md), [Q31](Q31-discrete-torus-digital-counter.md), [Q32](Q32-energy-geometry-fundamentals.md), [R13](../studies/R13-kk-charge-t3/)

**Question:** R8 Track 4 found δ ≈ αR (within ~6%) near q ≈ 137. Track 5 showed this
is approximate, not exact. The shear selects q and hence α — but what selects the shear?

---

δ ≈ αR (within ~6%) near q ≈ 137.  Track 5 showed this is
approximate, not exact.  The shear selects q and hence α —
but what selects the shear?

Ruled out mechanisms:
- *EM self-force:* photons don't couple to EM fields.
- *KK gravitational self-consistent metric:* R1 showed
  Gm_e/(Rc²) ~ 10⁻⁴³, which is 41 orders of magnitude too
  weak.  The 6D Einstein equations would return "flat T², no
  shear" to extreme precision.
- *Berry phase:* wrong scaling (R8 Track 4).

Active leads:
1. **KK charge from flat T² (R13, backlog):**
   R12 showed the charge calculation must be done entirely from
   the flat-T² perspective (KK decomposition), not by mixing
   flat-T² path lengths with 3D-embedded Coulomb energies.
   Set up 6D field equations on M₄ × flat T², compute the 4D
   effective charge and self-energy from KK modes, and check
   whether requiring self-energy = m_e c²/2 constrains the
   shear without using e as input.

Closed leads (R11):
- *Variational / energy cost:* Coulomb energy favors low q
  (monotonic, no minimum at 137).  See Q29.
- *Prime q / harmonic avoidance:* five linear tests found no
  prime/composite distinction.  See Q30.

Key insights:
- **The shear MUST exist** (independent of its value).  On
  an unsheared T², the geodesic slope IS the spin ratio.  You
  cannot simultaneously have exact spin-½ AND dense torus
  coverage.  The shear decouples these — its existence is
  forced, only its magnitude is undetermined.
- **q ~ 1/α is partly tautological.**  The model uses the
  measured charge e as input.  Since α = e²/(4πε₀ℏc), the
  charge constraint forces R ~ r_e and the mass constraint
  forces q ~ 1/α.  The value ~137 is a restatement of the
  input, not a prediction.  The real free parameter is
  **r (the aspect ratio)**, not q.
- Breaking the circularity requires deriving the shear from
  field self-consistency WITHOUT using e as input.

On the running of α: α runs in QED (1/137 → ~1/128 at Z-mass),
but q must be an odd integer (discrete), so the geometric α
can't vary continuously.  The running likely reflects vacuum
polarization screening in 3+1D, not compact geometry changes.
The bare α is fixed; the dressed α runs.
*Source: S2-toroid-geometry F6, R7, R8 Tracks 4–5, R1 (gravity
too weak), R11 (tautology analysis)*
R12 results (COMPLETE):
- Track 1: flat-T² wave equation has no modes at ω_C (spectral
  gap of ~137×).  Shear unconstrained.
- Track 2: curved-torus geodesics give q ≈ 193 (not 137);
  holonomy is zero.  Confirms compact space must be
  intrinsically flat.
- Corrected picture: R8's use of flat T² for mass/spin and
  3D embedding for charge is the correct physical procedure
  (internal vs external domains), not an inconsistency.
  Charge is a projection property of the embedding.

R13 results (COMPLETE):
- Track 1: electron is a winding mode, not KK momentum mode.
- Track 2: four candidate mechanisms for determining the
  embedding.  7D cross-terms eliminated.
- Track 3: R8-multi-winding (68, 137) breaks WvM charge mechanism.
  p = 68 ≠ 1 destroys commensurability between polarization
  rotation and frame rotation.  Monopole = 0 (exact).  R8 used
  charge e as input — never derived it.
- The α problem ≡ the charge mechanism problem.  α ≈ 1/137
  forces a tradeoff between correct Coulomb energy (needs small
  torus, R8-multi-winding) and correct charge (needs p = 1).

*Status: → Q34 (8 candidate paths for charge mechanism)*
