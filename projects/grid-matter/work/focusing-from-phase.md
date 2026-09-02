# GRID is focusing — because the bound is a PHASE, not a clipped amplitude

**The crux question answered: can the GRID substrate produce a focusing
(attractive) self-interaction? Yes — and it falls out of the compact phase
(the ℵ-line) for free.** Derivation + numerical confirmation
([`../scripts/sine_gordon.py`](../scripts/sine_gordon.py)).

## The sign confusion, resolved

The value-bound had been modeled as a **clip on a linear amplitude** — a hard
wall. A wall makes oscillation frequency *rise* with amplitude (particle-in-a-box)
⇒ **defocusing**. That is why clip, spillover, quantize all failed to bind, and it
is a *correct* statement about that interpretation.

But GRID's bounded quantity is a **compact PHASE**, not a clipped linear
amplitude. And that flips the sign.

*(Terminology: the mechanism below is scale-blind — it needs only "a compact
phase." For a **massive particle** that phase is a **Ma sheet** (its size sets the
mass, ω₀∝1/R); the **ℵ-line** is the Planck-scale compact phase, relevant to the
photon's substrate/gauge, not to ordinary mass. "ℵ-line" below should be read as
"the relevant compact dimension." See [promotion-hierarchy.md](promotion-hierarchy.md).)*

## Derivation

A compact phase φ ∈ [0, 2π) has a **periodic** on-site potential. The minimal
(lowest-harmonic) periodic potential is the cosine:

    U(φ) = m² (1 − cos φ)

Expand:

    U(φ) = m² ( φ²/2 − φ⁴/24 + φ⁶/720 − ⋯ )
                 ↑        ↑         ↑
               mass    quartic   sextic
              (KK gap)  −m²/24    +m²/720
                        < 0       > 0
                        FOCUSING  SATURATING

The quartic coefficient is **negative (attractive/focusing)** and the sextic is
**positive (saturating/stabilizing)** — *exactly* the focusing+saturating recipe
that produced the Q-ball, but here it is **not posited**: it falls out of
**periodicity alone**. Any compact-phase field is intrinsically
focusing-then-saturating.

The equation of motion is **sine-Gordon**:

    φ_tt − φ_xx + m² sin φ = 0

whose continuum theory has exact, stable, Lorentz-boostable **breathers**
(localized oscillating lumps) and **kinks** (topological windings). Same
boundedness as the clip; **opposite sign**, because a phase's potential *softens*
(turns over toward the top of the well) where a wall *hardens*.

## Numerical confirmation

| run | outcome |
|---|---|
| sine-Gordon breather, at rest | **STABLE, localized, energy drift 0.0%** (width fixed ~1.2; peak breathes 1.5↔0.8) |
| linear control (sin φ → φ) | **DISPERSES ×2.6** — same IC, focusing removed |
| breather, boosted (kx=0.3) | **STABLE and MOBILE** (speed 0.15, translates coherently) |

The energy drift is **0.0%** — unlike the Q-ball's ~10% — because this is a
genuine conservative soliton of an exactly-conservative potential. The linear
control isolates the effect: remove the cosine's focusing and the identical lump
disperses.

## Why this is GRID-native (not borrowed)

- The soliton mathematics (sine-Gordon, breathers, kinks) is classic. **The
  forma-native result is the derivation that GRID's own ℵ-line realizes it** —
  and therefore that GRID is *intrinsically* focusing+saturating, once the bound
  is read as the phase it is rather than a clipped amplitude.
- Sine-Gordon is the **continuum limit of a chain of coupled phases**
  (Frenkel–Kontorova: sites with a periodic on-site potential, coupled to
  neighbours) — a lattice of nodes (phases) and edges (coupling), i.e. a GRID.
  The impedance scatter supplies the coupling/kinetic term (φ_xx); the compact
  phase supplies the on-site cosine.
- **It unifies the earlier mechanisms.** Sine-Gordon has two soliton species:
  - **kink** = a 2π **winding** of the phase = mechanism III's topological charge
    (charge = winding), stable and mobile;
  - **breather** = a localized oscillation (a kink–antikink bound state) = a
    neutral contained-wave particle with rest energy = mass.
  One compact-phase potential ⇒ charge (kink) *and* mass (breather), both mobile.

## Discrete-lattice + dimensionality test ([`../scripts/discrete_sg2d.py`](../scripts/discrete_sg2d.py))

Ran the breather on a genuine **discrete (x,c) lattice** — coupling = the discrete
Laplacian the impedance scatter gives, on-site term = the compact-phase cosine:

| run | result |
|---|---|
| c-uniform breather, compact c, at rest | **STABLE** (x-width fixed ~6, energy drift 0.1%) — survives discretization |
| c-uniform breather, boosted (kx=0.2) | **STABLE & MOBILE** (speed 0.10) — survives the **Peierls–Nabarro** barrier |
| c-**localized** lump (c treated as 2nd *extended* dim, nc=32) | **DISPERSES** (width ×3.2, spreads in c) — the **Derrick** instability |

So on the lattice: **(x, compact-c) hosts a stable, mobile breather; a genuinely
2-extended-dimensional lump disperses.** The dimensionality advisory holds — the
compact phase, not extra extended dimensions, is what's needed; the ℵ-winding
(Q-ball charge) is the route to stability in higher *extended* dimensions.

## What is proven vs. still open

- **Proven (sign question):** a compact-phase field is focusing+saturating and
  supports stable, mobile solitons **on the discrete lattice** — so GRID *can* be
  focusing. The seven prior negatives were the wrong interpretation of the bound
  (amplitude-wall), not a property of GRID.
- **Proven (dimensionality):** (x, compact-c, c-uniform) is the right minimal
  setting; 2 extended dimensions break the real-scalar breather (Derrick),
  requiring the winding-charge Q-ball instead.
- **Still open — the honest gap in the reduction:** the test used a **node-field
  discrete sine-Gordon** (φ at nodes, Laplacian coupling + a *hand-added* cosine).
  The Laplacian coupling *is* what the impedance scatter reduces to, so that half
  is GRID-faithful. But the **on-site cosine was posited** as the natural
  compact-phase potential — its origin from the *literal directed-edge impedance
  scatter* (what pins a preferred phase / supplies the gap) is **not yet derived**.
  A pure XY/rotor coupling gives a *massless* phase (no cosine, no breather); the
  cosine needs a preferred-phase / mass term whose GRID source (the compact
  c-dimension? the vacuum?) is the remaining derivation.

## Next

1. **Close the reduction gap:** derive the on-site cosine from the *literal
   directed-edge impedance scatter* with compact-phase edges — what supplies the
   preferred phase / mass (candidates: the compact c-dimension via KK; a vacuum
   phase). This is the remaining step to make "GRID is focusing" a full
   first-principles result rather than coupling(derived)+potential(posited).
2. **Kink = winding = charge:** connect the sine-Gordon kink to mechanism III's
   ℵ-line winding and metric-charge; a kink–antikink pair = the breather = a
   neutral particle; pair creation = kink/antikink nucleation.
3. **Q-ball for higher-D:** the winding-charge-stabilized version for 2–3 extended
   dimensions (evading Derrick), toward real 3D-space particles.
4. **Born from the breather:** detection ∝ energy density on a genuinely
   localized, mobile, realist object.
