# The range crux, from GRID's foundations — blocked on a missing carrier

**Status:** Derivation (GRID-native, per the user's "model from the
foundations, not scalar-tensor" instruction). Asks whether GRID's own
structure carries the local refractive index out to 1/r. **Outcome: blocked
— GRID's specified spectrum has no massless, neutral, propagating mode to do
it, and the ℵ-line size is specified as a per-particle *parameter*, not a
spatial *field*.** Not a refutation; a precisely-located foundations gap.

Grades: **[rigorous]** (math), **[from foundations]**, **[assessment]**,
**[open]**.

---

## 1. The requirement is math, not borrowed physics [rigorous]

A static field falling off as **1/r** is the Green's function of a **massless**
operator; a massive one falls off as a short-range Yukawa e^(−Mr)/r. So the
range needs a **massless** carrier. It must also be sourced by **neutral
energy** (gravity acts on neutral matter), and it must **propagate** (a purely
local quantity has no range). Three necessary properties: *massless,
neutral-energy-sourced, propagating.* This is not an appeal to any theory — it
is the falloff theorem.

## 2. GRID's specified spectrum does not contain such a mode [from foundations]

Walk the modes GRID actually specifies
([grid/foundations.md](../../grid/foundations.md),
[grid/photon-from-aleph.md](../../grid/photon-from-aleph.md)):

| Mode | Massless? | Neutral-sourced? | Verdict for range |
|---|---|---|---|
| n=0 photon (EM gauge field) | yes | **no** — couples to *charge*; a neutral mass sources no photon field | can't carry it |
| n≥1 KK modes | **no** — Planck-mass m_n = nℏ/R_ℵ | yes | Planck-contact (Yukawa), no range |
| graviton | — | — | **not derived** in GRID (synthesis.md) |
| ℵ-line dilation / radion (size R_ℵ) | *unspecified* | yes (couples to energy) | the only candidate — see §3 |

So the massless channel (photon) is charge-coupled (useless for neutral mass),
and the neutral channel (KK) is Planck-massive (short-range). **No mode in the
specified spectrum is both massless and neutral.** The only candidate is the
ℵ-line dilation.

## 3. The ℵ-line size is specified as a *parameter*, not a *field* [from foundations]

For the dilation to carry the range it must be a **spatially-varying, massless,
propagating field** — a mass shifts R_ℵ locally, and that shift spreads as 1/r.
But GRID specifies R_ℵ (L_compact) as a **particle-dependent length**
([grid/foundations.md](../../grid/foundations.md): "≈ 10¹⁹ L_P for an
electron") — a *property of a particle/sheet*, not a spatial field with a
dispersion relation. GRID gives R_ℵ **no dynamics**: no gradient coupling
between neighbouring edges' sizes, no wave equation, no statement that a local
δR_ℵ propagates.

**Update-function view (the GRID-native check).** The scatter
S = (2/N)J − I acts on edge *signal amplitudes* (the ℵ-line mode content),
not on the structural size R_ℵ. So under GRID's actual dynamics, a shift in
R_ℵ is **not a propagating signal** — it is a structural change, local to its
edge. The scatter propagates the *photon* (massless, but charge-coupled, §2)
and the *KK excitations* (Planck-massive, §2); it does not propagate the size.
So there is nothing in the specified update rule that carries a size-shift to
distance r.

## 4. Verdict — blocked, and where [assessment]

Putting §1–§3 together, honestly and in both directions:

- **Not "it works."** GRID's foundations, as specified, do **not** provide a
  massless neutral propagating mode, and the natural reading of R_ℵ (a
  per-particle parameter with no spatial dynamics) gives **no range**. The
  local index is real; it stays local.
- **Not "refuted."** This is not a proof that no GRID mechanism can give
  gravity's range. It is that the range requires structure — a massless
  neutral **ℵ-line-dilation field** with its own dynamics — that GRID **does
  not currently specify**. Adding it is *positing new foundations*, not
  deriving from the given ones, and is out of this project's scope (it belongs
  to grid-primitive / a substrate project).

So the range crux is **blocked on a specific, identified foundations gap: GRID
has no massless neutral carrier, and does not make the ℵ-line size a
propagating field.**

Two consequences worth recording:
- **This is *why* gravity resists a mechanical derivation here.** Gravity's
  1/r needs a massless neutral mode; GRID's spectrum (charged-massless photon +
  neutral-Planck-massive KK) lacks one. Forma's **Jacobson** route sidesteps
  this precisely because the metric emerges *as an equation of state*, not as a
  fundamental propagating mode — so it never needs a massless neutral carrier
  in the spectrum. That is a real reason the statistical route is the natural
  home for gravity in GRID.
- **Even if the dilation field were added and massless,** two further hurdles
  remain ([gauge-invariant-coupling.md](gauge-invariant-coupling.md) §4): does a
  neutral mass source it as a **scalar monopole ∝ energy**, and does it give the
  right **light-bending coefficient** (a radion coupling to F² does bend light,
  but hitting PPN γ = 1 is the classic scalar-tensor constraint). These are
  downstream of the missing carrier and untouched here.

## 5. What would unblock it

A foundations-level result — *not* in this project — establishing that GRID's
ℵ-line size is a **dynamical, spatially-varying, massless** degree of freedom
(a genuine modulus with propagating dynamics), sourced by energy. Until such a
result exists, mechanism 2's range has no carrier, and the mechanism is
**blocked at the range** — local index solid, 1/r extension unsupported by the
current foundations.
