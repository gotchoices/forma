# Chapter 9 (Appendix) — A second reading: the 1D harmonic-oscillator translation

The project's structural arc closes with [Chapter 8](08-closing-summary.md).
This appendix is a forward-looking hand-off rather than part of the
in-project derivation. It does not introduce any result that
chapters 3–8 use, and nothing here amends or revises what those
chapters established.

What the appendix does is recast the Chapter 2 mass spectrum

<!-- m_n = ℏ |n| / (R_u c) -->
$$
m_n \;=\; \frac{\hbar\,|n|}{R_u\,c}
$$

— which Chapter 2 derived by treating φ as a **classical wave** on
the manifold and applying the periodicity boundary condition
U(u + L_u) = U(u) — as the spectrum of a **one-dimensional harmonic
oscillator (HO)**, and explains what the second reading makes
available that the first does not. The classical wave derivation
needed no operator algebra, no Hilbert space — just separation of
variables and the requirement that a wave close smoothly on itself
around the compact direction. The HO reading dresses that same
spectrum in operator-algebra clothing.

The appendix is here so that later projects — [metric-charge](../metric-charge/)
in particular, when it adds a second compact direction — can lean
on HO formalism with the understanding that the underlying physics
has already been derived on geometric grounds inside metric-mass.

## 1. The ground-up derivation, in one paragraph

The u-piece of the wave equation, after separation, is

<!-- U''(u) + k_u² U(u) = 0,  with  k_u = n / R_u,  n ∈ ℤ -->
$$
U''(u) + k_u^2\,U(u) \;=\; 0,
\qquad
k_u \;=\; \frac{n}{R_u},\quad n \in \mathbb{Z}
$$

Chapter 2 noted three times that this is "the equation of a simple
harmonic oscillator." That observation was used as a *vocabulary
remark* — the ODE has the same shape as a mass on a spring. It was
not pursued algebraically. The integer n came from periodicity, the
dispersion came from the constraint among the separation constants,
and the mass m_n = ℏ|n|/(R_u c) came from matching the dispersion to
the relativistic energy-momentum identity.

Nothing in that path required operators, ladders, occupation numbers,
or a Hilbert space. The story is classical wave mechanics on a
manifold with a compact direction.

## 2. The same result, in HO clothing

The HO reading takes one further step: promote the mode amplitudes
to operators. Each independent classical mode of U becomes a pair of
ladder operators (a_n, a_n†) with

<!-- [a_n, a_m†] = δ_nm,   N̂_n = a_n† a_n -->
$$
[\,a_n,\;a_m^\dagger\,] \;=\; \delta_{nm},
\qquad
\hat{N}_n \;=\; a_n^\dagger\, a_n
$$

The integer n is no longer the winding number of a classical wave —
it is the eigenvalue of the occupation-number operator N̂_n acting on
the Fock space of u-mode excitations. The classical dispersion
m_n = ℏ|n|/(R_u c) becomes a ladder of energy levels separated by
ℏω_u with ω_u = c/R_u, plus a per-mode zero-point ℏω_u/2 that the
classical derivation silently dropped.

The translation, line by line:

| Classical wave reading (Chapter 2) | 1D HO reading |
|---|---|
| Mode function U_n(u) = e^{i n u / R_u} | Ladder operators a_n, a_n† |
| Integer winding n (from periodicity) | Occupation-number eigenvalue n |
| Dispersion m_n = ℏ\|n\| / (R_u c) | Energy ladder ℏω_u · n, with ω_u = c/R_u |
| Mode amplitude (a complex number) | Fock-space state vector |
| Standing wave: cos(n u / R_u) | Symmetric superposition of ±n number states |
| (silent on vacuum amplitude) | Zero-point energy ℏω_u/2 per mode |

The two columns are the same physics in different mathematical
clothing. The classical column makes the geometry transparent —
which coordinate is doing what work, what the boundary condition
means, why the integer is forced. The HO column makes the algebra
transparent — ladder structure, vacuum, Fock space, the operator
identities that the classical column does not need but can support.

Neither column is "more fundamental." The classical reading is the
one this project derives; the HO reading is the one that lets later
work use a mature toolkit.

## 3. What the HO reading opens up

Three uses follow directly from having the bridge available. None
of them are developed in this project; they are flagged so that
later work can call on them.

**Localized particles via coherent states.** A single plane-wave
mode is delocalized over all of u. The HO reading provides
*coherent states* — minimum-uncertainty Gaussian wavepackets that
are eigenstates of the ladder operator a_n and that trace classical
trajectories without spreading in time. This is the natural
formalism for talking about a particle as a localized blob on M,
which a plane-wave mode framing has to work around with packet
arguments.

**Vacuum structure via the zero-point amplitude.** The HO ground
state |0⟩ has ⟨0| x² |0⟩ ≠ 0 — a vacuum fluctuation forced by
[x, p] = iℏ. Translated to our setting, even the "empty" diagonal
metric carries a per-mode vacuum amplitude on the compact direction.
The classical derivation is silent on this; the HO reading is not.
This becomes relevant when downstream work asks whether the bare
metric carries hidden stress-energy sources beyond what excited
modes contribute.

**Multi-direction generalization.** This is the largest payoff and
the most direct hand-off to [metric-charge](../metric-charge/). Add
a second compact direction w with its own radius R_w, and the
spectrum becomes that of a **2D harmonic oscillator**: two
independent towers of integer occupation numbers (n_u, n_w), one per
direction. The HO formalism turns this into algebra without further
geometric work.

The 2D case carries symmetry structure worth flagging here:

- A 2D HO with **distinct radii** R_u ≠ R_w has a U(1)×U(1) symmetry
  — one independent phase per ladder. This is the *generic*
  anisotropic case and the one our framework will most commonly
  inhabit, since there is no a-priori reason for two physical
  compact dimensions to share a radius. U(1)×U(1) is itself the
  natural geometric origin of *two commuting charges*.

- A 2D HO with **equal radii** R_u = R_w (the *isotropic* case) has
  spectrum E = ℏω(n_u + n_w + 1) that is degenerate under any
  unitary rotation of the two ladder operators. The U(1)×U(1) is
  enlarged to **SU(2)**. The extra generators that SU(2)/U(1) brings
  are not visible in the classical wave reading at all — they are a
  spectral degeneracy that only the operator-algebra formalism makes
  explicit. Isotropy is a special case, not the generic one, but it
  is the case where the symmetry algebra is largest.

- Three isotropic directions would give **SU(3)** by the same
  argument — flagged here only because it is the natural geometric
  candidate any framework with three matched compact directions
  could call on for an internal color-like symmetry.

The point of mentioning the 2D and 3D extensions now is that the
symmetry content of multi-direction extensions is what the HO
reading sees that the classical wave reading does not. When
[metric-charge](../metric-charge/) adds a second compact direction,
the U(1)×U(1) (or, in the equal-radii limit, SU(2)) charge structure
will follow from the geometry through this bridge, rather than being
postulated.

## 4. What this chapter is not claiming

- The HO reading is not the "correct" reading and does not replace
  Chapter 2's derivation. The classical wave story underwrites the
  spectrum on geometric grounds; the HO reading is a translation
  layer that exposes algebraic structure latent in that same
  spectrum.
- We do not commit to a quantization scheme. Promoting amplitudes
  to operators is a choice (canonical, path-integral, geometric);
  this chapter establishes a formal correspondence between two
  spectra, not a quantization prescription.
- We do not import HO machinery into the rest of metric-mass. The
  remaining chapters continue in the classical wave framing and are
  not rewritten.

## 5. What this chapter establishes

| Claim | Status |
|---|---|
| The Chapter 2 u-equation is formally the 1D SHO equation | Established (was already remarked in Ch. 2; this chapter makes the correspondence explicit) |
| The integer winding n of the classical derivation corresponds to the occupation-number eigenvalue of the HO reading | Established as a translation |
| The classical derivation drops a zero-point ℏω_u/2 per mode that the HO reading retains | Noted; consequences not pursued here |
| A 2D extension has U(1)×U(1) symmetry generically, enlarging to SU(2) when the two radii are equal | Stated; developed in [metric-charge](../metric-charge/) |

The hand-off is to metric-charge, where the second compact direction
turns the translation built here into a derived charge structure.
