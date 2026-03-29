# Q91: Can the compact volume V_compact be derived independently?

**Status:** Open (may be addressed by R41)
**Related:**
  R40 F25 (α-impedance model),
  R40 F26 (constraint counting: r still free),
  R41 (dynamic model implementation),
  [Q34](Q34-selecting-r.md) (what selects r?),
  R37 (membrane mechanics)

## The question

The α-impedance model (R40 F25) says the torus fills (1−α) of the
available compact volume:

    V_torus = (1 − α) × V_compact

Given V_compact for each sheet, the force balance (tube expansion
vs vacuum spring) combined with the Compton constraint determines
the aspect ratio r = a/R uniquely — without needing the cross-sheet
coupling from the static model.

Currently, V_compact is computed FROM the known particle geometry
(which uses r from the static model).  This is circular.

**Can V_compact be derived from first principles?**

## What V_compact represents

V_compact is the 3D volume of compact space accessible to the
mode.  For a 2D sheet embedded in 6D compact space:

    V_compact = A_sheet × L_normal

where L_normal is the extent of the mode in the direction
perpendicular to the sheet.  From the α-impedance model:

    L_normal = a / (2(1−α)) ≈ a/2

The mode extends about half a tube-radius into the normal
direction.  This is an algebraic consequence of V = 2π²Ra²
and V_compact = V/(1−α), not an independent prediction.

## Possible approaches

1. **From the 6D metric.**  The compact space metric G̃ determines
   the effective volume available to each sheet.  The off-diagonal
   elements (cross-shears σ_ep, σ_eν, σ_νp) mix the sheets and
   set the effective normal extent.  Computing V_compact from G̃
   might give r without using particle masses.

2. **From the mode's evanescent profile.**  The photon's EM field
   decays evanescently in the normal direction.  The penetration
   depth depends on the mode frequency and the compact geometry.
   The (1−α) contour in the normal direction sits at L_normal.

3. **From cross-sheet coupling.**  The proton's L_normal ≈ 1.88 fm.
   This might be related to the distance between the proton and
   electron sheets in compact space.  If L_normal = f(σ_ep, L_e),
   the circle closes: σ_ep determines L_normal, which determines
   V_compact, which determines r.

## The payoff

If V_compact can be derived independently (from any of the above),
the α-impedance model would determine r from fundamental geometry
alone.  The cross-sheet coupling (R27) provides a separate
determination of r.  Agreement would be a non-trivial confirmation
that the static and dynamic models describe the same physics.

If they disagree, one of the models needs revision.

## Current values

| Sheet | a (fm) | R (fm) | V_torus (fm³) | V_compact (fm³) | L_normal (fm) |
|-------|--------|--------|---------------|-----------------|---------------|
| Proton | 3.74 | 0.42 | 115.7 | 116.6 | 1.88 |
| Electron | 529.9 | 1059.8 | 5.87×10⁹ | 5.92×10⁹ | 266.9 |
