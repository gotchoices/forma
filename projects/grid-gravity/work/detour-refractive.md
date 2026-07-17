# Mechanism 2 — detour / refractive: foundation and derivation attempt

**Status:** Working note. States the detour/refractive micro rule (the
premise, on the table) and vets it against the shared gate
([README](../README.md#the-shared-evaluation-framework--the-gate)) from the
rule — settling the two open questions in order (dispersion first, then
range). Nothing about the field is imposed.

Grades: **[rule]**, **[derived]**, **[plausible]** (leading-order /
reasoned but not proven), **[forced]**, **[open]**.

---

## 1. The micro rule, stated explicitly

**(D1) Resonance gating [rule].** At a location with *no* resident standing
wave, coupling to the compact dimension requires an *exact quantum*
(mode-match). Off-quantum waves do not see the compact dimension — they pass
unaffected. **The vacuum is transparent.**

**(D2) Sub-quantum coupling, once a standing wave exists [rule].** A resident
standing wave (a mass) at node n₀ is a local oscillator at the compact-mode
frequency ω₀ = ω_Compton. A passing wave forces n₀ to a new value;
self-consistency then requires the standing wave to **re-phase**. A
*sub-quantum* bit of energy enters the compact dimension, nudges the phase,
and is **ejected within one compact cycle** — lossless (the energy returns).

**(D3) The effect [rule].** The passing wave is *delayed*, not absorbed: its
path is elongated by the excursion into the compact dimension. The local
region is thereby a **slower medium** — a refractive index n(x) = c/c_eff(x)
> 1 near the mass. This is the discrete-lattice image of optical-metric /
polarizable-vacuum gravity, target n(r) ≈ 1 + 2GM/rc².

## 2. Gate condition (0) — vacuum field [met]

The mechanism produces a **refractive index** n(x), which is a property of
the medium at every point, present whether or not a test wave is passing. So
there is a genuine vacuum field (the optical metric), and it is met *without*
requiring the mass to actively broadcast traffic — the awkward demand that
[micro-to-macro.md](micro-to-macro.md) forced on mechanism 1. This is the
structural advantage of mechanism 2: the field is a *medium modification*,
not a *source*. **[met, given range — §4]**

## 3. Gate condition (2) — dispersion [derived: non-dispersive for ω ≪ ω₀]

Settle this first; a dispersive answer kills the mechanism.

The passing wave (frequency ω) drives the compact oscillator (resonance ω₀)
and scatters with a phase shift δ(ω). The delay it accumulates per
interaction is the group (Wigner) delay τ(ω) = 2 dδ/dω. "Ejected within one
cycle" means the resonance is **broad** (quality factor Q ~ 1, width Γ ~ ω₀).
For such a resonance,

<!-- delta(omega) ~ arctan( (Gamma/2) / (omega_0 - omega) ),  tau = 2 d delta/d omega -->
$$
\delta(\omega) \approx \arctan\!\frac{\Gamma/2}{\omega_0-\omega},
\qquad \tau(\omega) = 2\,\frac{d\delta}{d\omega}.
$$

For ordinary light near a massive particle, **ω ≪ ω₀ = ω_Compton** (the wave
is far less energetic than the particle's rest mass). In that limit

<!-- tau(omega) ~ 2 (Gamma/2) / omega_0^2 = const + O((omega/omega_0)^2) -->
$$
\tau(\omega) \;\approx\; \frac{\Gamma}{\omega_0^{2}}
\;\sim\; \frac{1}{\omega_0}
\;=\; \tau_c \;+\; O\!\big((\omega/\omega_0)^2\big).
$$

So **the detour delay is a fixed ≈ one-compact-cycle time τ_c, set by the
mass (ω₀), independent of the passing wave's frequency** — to leading order,
with corrections only at O((ω/ω₀)²), i.e. only near the pair-production
scale. **Non-dispersive in the entire ordinary-gravity regime.**

This is a real, *derivable* pass — and it is better than mechanism 1, where
non-dispersivity had to be *assumed* (lossless reduced-c). Here it falls out
of off-resonant driven-oscillator physics and matches the "single cycle"
premise. **[derived, favorable]**

The dispersion that *does* appear (near ω ~ ω₀) is a genuine strong-field /
high-energy prediction, not a defect of the ordinary regime.

## 4. Gate condition (1) — range / falloff [plausible candidate; the open step]

The delay in §3 is what a wave passing *through* n₀ experiences. Gravity
needs the refractive well to **extend**: n(r) → a 1/r potential for waves
passing *near* n₀. Two ingredients:

**Source [plausible].** δn is sourced by the resident standing wave. As a
localized scalar object carrying energy E ∝ ω₀, it is a **monopole** source
of the refractive perturbation — the polarizable-vacuum reading, δn ∝ local
mass-energy. A monopole (not the dipole that sank mechanism 1's passive
reading) is the right multipole for a 1/r potential.

**Propagation [plausible → open].** The standing wave's influence reaches a
node at distance r through the **shared hexagonal loops** n₀ participates in
(the fractal-loop idea). If that constraint propagates by the lattice's own
operator — which is **lossless/unitary** (the confirmed scatter) and hence
**massless** — then the static response to a persistent monopole source is
the massless Green's function: **δn(r) ∝ 1/r (3D), log r (2D)**, isotropic on
the hex lattice. This is a *cleaner* candidate than mechanism 1's assumed
diffusive constitutive relation, because the propagator here is the confirmed
lattice operator, not a posited one.

**The open step.** That the loop-coupling *is* the lattice's massless
Green's function — rather than something shorter-ranged or anisotropic — is
**not derived**. It reduces to whether the loop-coupling is **scale-free**
(no preferred loop size), which is exactly GRID's block-spin RG fixed-point
question ([foundations.md](../../grid/foundations.md) Q1): scale-free ⇒ power
law (1/r); a preferred scale ⇒ Yukawa. So mechanism 2's range question is
the *same* open question as mechanism 1's, now with a concrete candidate
propagator (the lattice operator) and a sharp criterion (RG fixed point).
**[open — the make-or-break]**

## 5. The linchpin and the coefficient

- **Losslessness [met by construction].** The detour returns the energy
  within one cycle — no absorption. So the loss-driven failure modes (shunt →
  Yukawa; low-pass → dispersion) are structurally avoided.
- **Coefficient [open].** δn's magnitude must reproduce n(r) = 1 + 2GM/rc²,
  i.e. G = 1/(4ζ). It depends on the detour *rate/fraction* per pass and how
  it scales with proximity — downstream of the range (§4). The PV form is the
  target, and PV reproduces the weak-field tests (including the light-bending
  factor of 2), so *if* the mechanism yields n(r) of PV form the GR tests
  follow.

## 6. Where mechanism 2 stands against the gate

| Gate condition | Mechanism 1 (congestion) | Mechanism 2 (detour/refractive) |
|---|---|---|
| (0) vacuum field | fails passively; needs *active source* (forced, awkward) | **met** — refractive index is a medium property |
| (2) non-dispersive | *assumed* (lossless reduced-c) | **derived** for ω ≪ ω₀ (off-resonant delay ≈ τ_c) |
| linchpin (lossless) | contingent on the model | **met by construction** (detour, not absorption) |
| (1) falloff / range | *assumed* diffusive → 1/r | **plausible** via lattice Green's function; open step = RG scale-freeness |
| (3) coefficient | ∝ 1/κ ~ 1/ζ (direction) | PV target n = 1+2GM/rc²; open |

Mechanism 2 clears *more* of the gate **from the rule** (conditions 0 and 2
and the linchpin), and its one hard open — the range — has a **cleaner
candidate** (the confirmed lossless lattice operator as the propagator of a
monopole source) than mechanism 1's assumed constitutive relation.

## 7. Honest assessment

Not gate-cleared — condition (1) range and (3) coefficient are open. But
mechanism 2 is **materially better positioned** than mechanism 1: the vacuum
field, non-dispersivity, and losslessness are met from the rule (two
derived, one structural), rather than assumed or forced. The whole mechanism
now rests on **one make-or-break question**, sharply stated:

> Does the standing wave's self-consistency constraint, carried through the
> shared hexagonal loops, propagate as the lattice's **massless** Green's
> function (⇒ n(r) ∝ 1/r) — i.e. is the loop-coupling **scale-free** (the RG
> fixed point)?

That is the same question GRID's foundations already flag (Q1), now the load
bearing point of a well-motivated gravity mechanism.

## 8. Next

Vet §4 directly: does a persistent localized constraint on the hex lattice,
propagated by the *actual scatter operator*, produce a 1/r (log in 2D)
isotropic response — and is the loop-coupling scale-free? This is a
micro-rule calculation/sim with a *predicted* answer (the lattice Green's
function) to check against with **no free parameters** — the honest standard
the first round's sims missed. If it fails (Yukawa / anisotropic / not
scale-free), the fail-fast options and further mechanisms remain.
