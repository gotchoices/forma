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

But GRID's bounded quantity is the **ℵ-line: a compact PHASE**, not a clipped
linear amplitude. And that flips the sign.

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

## What is proven vs. still open

- **Proven (sign question):** a compact-phase field is focusing+saturating and
  supports stable, mobile solitons — so GRID *can* be focusing. The seven prior
  negatives were the wrong interpretation of the bound (amplitude-wall), not a
  property of GRID.
- **Still open (full GRID reduction):** show that the *actual impedance-scatter*
  with compact-phase edges reduces, in the continuum limit, to the **discrete
  sine-Gordon** with the right coefficients — i.e. that the scatter's coupling
  plays φ_xx and the ℵ-line plays the cosine, quantitatively. That is the next
  derivation. Discreteness will add a Peierls–Nabarro barrier (a mild pinning);
  whether that helps (extra stability) or hurts (impedes mobility) is to be
  measured on the discrete lattice.

## Next

1. **Discrete-lattice sine-Gordon** on a genuine GRID phase-scatter: does the
   breather survive discreteness (Peierls–Nabarro) and stay mobile?
2. **Kink = winding = charge:** connect the sine-Gordon kink to mechanism III's
   ℵ-line winding and metric-charge; a kink–antikink pair = the breather = a
   neutral particle; pair creation = kink/antikink nucleation.
3. **Born from the breather:** detection ∝ energy density on a genuinely
   localized, mobile, realist object.
