# Chapter 7 — Off-diagonal shear and the breaking of ±n degeneracy

**Status:** Bare outline. Each section is a sketch of the
derivation step that section will perform. To be filled out as
prose.

The ±n distinction has been examined repeatedly:

- [Chapter 3 §3](03-examining-the-modes.md) noted that ±n are
  linearly independent solutions of the wave equation but mass
  is symmetric in n (m = ℏ|n|/(R_u c)).
- [Chapter 4](04-mode-interactions.md) showed that for
  interactions in the bare diagonal metric, the ±n distinction
  is subtle: rest energies double in superposition, off-diagonal
  stress-energies cancel.
- [Chapter 5](05-metric-self-consistency.md) showed that mass
  *sources* off-diagonal metric entries when present, but the
  ±n superposition cancels the n-linear ones.
- [Chapter 6](06-gravitational-bending.md) showed that
  gravitational coupling is set by the (doubled) diagonal
  energy, so cancellation does not extend there.

What every previous chapter assumed is that the metric started
diagonal. This chapter asks the converse question: *given* an
off-diagonal entry in the metric, what does it do to the ±n
modes? In particular, can it lift the degeneracy and bias the
manifold toward one sign of n over the other?

The chapter is discovery-driven. We do not assert that the real
world has a shear; we compute what a shear would *do* and let
the implications follow.

---

## Concepts to be developed

| § | Concept |
|---|---------|
| 1 | The setup: introduce a g_Su shear into the metric |
| 2 | The dispersion relation in the sheared metric |
| 3 | At rest: ±n unchanged |
| 4 | Moving: the dispersion splits |
| 5 | The Kaluza-Klein parallel: shear as a "vector potential" |
| 6 | Net biasing under thermal ensembles |
| 7 | The real-world matter/antimatter question |
| 8 | Where the shear could come from |
| 9 | What this chapter does and does not establish |
| 10 | End of Chapter 7 |

---

## Bare outline

### 1. The setup

Modify Chapter 1's bare metric by adding a single off-diagonal
entry g_Su = γ. The modified metric:

```
g_μν = | -c²    0    0  |
       |  0     1    γ  |
       |  0     γ    1  |
```

Compute the inverse metric (g^Su = -γ/(1-γ²); diagonal entries
rescaled by 1/(1-γ²) for the spatial block). Note that γ is a
*parameter*: this chapter does not derive γ from anything. It
asks what consequences follow if γ ≠ 0, leaving the question of
whether γ ought to be nonzero to §8.

### 2. The dispersion relation in the sheared metric

Solve the wave equation g^μν k_μ k_ν = 0 in the modified metric.
Result:

<!-- ω²/c² = (k_S² + (n/R_u)² - 2γ k_S (n/R_u)) / (1 - γ²) -->
$$
\frac{\omega^2}{c^2}
\;=\; \frac{k_S^2 \;+\; (n/R_u)^2 \;-\; 2\,\gamma\,k_S\,(n/R_u)}{1 - \gamma^2}
$$

The cross-term 2γ k_S (n/R_u) is **linear in n**. This is the
key structural fact: the dispersion is no longer n²-symmetric.
Subsequent sections trace what follows.

### 3. At rest: ±n unchanged

Set k_S = 0. The dispersion reduces to ω² = c²(n/R_u)² / (1−γ²).
Result is identical for ±n: rest mass m_n = ℏ|n|/(R_u c · √(1−γ²))
shifted by a γ-dependent factor but symmetric in n.

Conclusion: shear does *not* break the rest-mass symmetry. A
particle at rest in S sees no asymmetric energy from γ.

### 4. Moving: the dispersion splits

For k_S ≠ 0, compute ω_+ and ω_- separately:

<!-- ω_+² - ω_-² = -4γ c² k_S (n/R_u) / (1-γ²) -->
$$
\omega_+^2 - \omega_-^2
\;=\; \frac{-4\,\gamma\,c^2\,k_S\,(n/R_u)}{1-\gamma^2}
$$

The two branches have different ω at the same k_S — a moving +n
and a moving −n with the same spatial momentum no longer have
the same energy. The splitting is direction-dependent: it
flips sign with sign(γ k_S n).

Sketch the (k_S, ω) diagram for the sheared metric, showing the
two branches separated. Show that no single sign of n is
"always lower energy" — the asymmetry is direction-dependent,
not absolute.

### 5. The Kaluza-Klein parallel

Compare to standard KK ([primers/kaluza-klein.md §5](../../primers/kaluza-klein.md)):
off-diagonal g_μ5 = A_μ couples to compact-direction momentum
(charge) to produce the Lorentz force, splitting +q and −q
modes' dynamics. Here, off-diagonal g_Su plays the same role
for our compact-direction momentum (which we read as
mass-handedness rather than charge). The math is the same; the
interpretation differs in the standing identification of compact
momentum.

Note: the shear-induced splitting *is* the Lorentz-force
mechanism, recast in mass-mode language. Whether this argues
for our framing or for standard KK's framing is a project-level
question, not settled here.

### 6. Net biasing under thermal ensembles

A single mode moving through a sheared region experiences a
direction-dependent dispersion shift. But "biasing the universe
toward +mass over −mass" requires a *net* asymmetry across an
ensemble of modes, not just direction-dependent shifts that
cancel when motion is averaged.

Compute: for a thermal distribution of mode momenta in a fixed
shear background, do +n and −n populations equilibrate to the
same density? Standard equilibrium statistical mechanics
(Boltzmann distribution: probability ∝ exp(−E/kT)) on the
sheared dispersion gives:

- At fixed n, integrate over k_S with weight exp(−ω(k_S, n)/kT).
- The integral picks up an n-dependent factor when γ ≠ 0,
  because ω(k_S, n) is no longer symmetric under k_S → −k_S
  (the cross term breaks that symmetry within each branch).
- Result: equilibrium density of +n modes ≠ density of −n modes
  when γ ≠ 0.

Magnitude of the asymmetry: order γ·(thermal velocity)·(rest
energy)/(thermal energy), or similar. The exact form depends
on the distribution but the *direction* of the asymmetry follows
γ's sign.

This is the bridge to real-world bias: a shear background
generates a thermal-ensemble preference for one sign of n over
the other.

### 7. The real-world matter/antimatter question

Standard physics treats matter/antimatter asymmetry
("baryogenesis") as an open problem. A small primordial
asymmetry (~10^-9, the baryon-to-photon ratio) developed in
the early universe and produced today's matter-dominated
cosmos. Mechanisms in the literature (Sakharov conditions, GUT
baryogenesis, electroweak baryogenesis, leptogenesis) all
require some CP-violation source.

In our framework, a primordial g_Su shear in the manifold's
geometry would produce exactly this kind of asymmetric
equilibrium: more +n modes than −n modes (or vice versa, by
sign of γ). This does not assert that the real world has such
a shear; it observes that the mechanism *is available* in our
minimal framework.

Frame this carefully: the real-world matter dominance is
empirical (measured); the mechanism for it is open; this
project's framework provides one mechanism, but distinguishing
it from other proposed mechanisms (Sakharov-style, etc.) is
beyond scope.

### 8. Where the shear could come from

Possible sources for the g_Su term, ordered by speculativeness:

- **Primordial geometric structure.** The manifold M might have
  inherited a small g_Su term from its initial conditions —
  i.e., the early universe started with this off-diagonal
  geometric component already present. This is the simplest
  hypothesis but it pushes the explanation onto initial
  conditions.
- **Sourced by an early matter-imbalanced state.** Per
  [Chapter 5](05-metric-self-consistency.md), mass-moving
  modes source g_Su (via T_Su = 2 k_S (n/R_u) |φ|²). An early
  universe with a small momentum or n imbalance could have
  sourced its own asymmetric shear, which then biased
  subsequent equilibration. This is a self-consistent
  bootstrapping picture but requires the original imbalance to
  come from somewhere.
- **Coupling to other fields.** If the project later admits
  additional fields (charge, second compact direction), shear
  might be sourced or stabilized by those fields.

The chapter does not commit to any of these. It notes them as
possibilities for follow-up work.

### 9. What this chapter does and does not establish

#### Established

- Adding a g_Su shear to the bare metric does not break the
  ±n rest-mass degeneracy.
- For moving modes, shear *does* break the ±n degeneracy via
  the n-linear cross-term in the dispersion relation.
- Under thermal equilibrium with γ ≠ 0, the densities of +n
  and −n modes differ. The framework provides a mechanism for
  net biasing of mass toward one sign over the other.

#### Not established

- That γ ≠ 0 in the real world.
- That this mechanism (vs. Sakharov-style mechanisms in
  standard cosmology) is *the* origin of real-world
  matter-antimatter asymmetry.
- The numerical magnitude of γ that would be required to match
  observed baryon asymmetry.
- Whether γ is itself a dynamical field or a fixed background
  parameter.

#### What this leaves open

- The dynamics of γ (does it have its own equation of motion?
  is it sourced by matter? does it dissipate?).
- Whether the bias is observable independently of mass (e.g.,
  effects on light propagating through sheared regions).
- The cosmological story: how a primordial shear could have
  evolved, dissipated, or persisted to today.

### 10. End of Chapter 7

Brief summary tying the chapter back to the project:

- Chapters 4-6 showed that ±n distinction is subtle on a
  symmetric (diagonal) manifold.
- Chapter 7 (this chapter) showed that off-diagonal shear is
  the natural mechanism that *would* lift the ±n degeneracy.
- The bias is direction-dependent at the single-mode level but
  produces net asymmetric equilibration in a thermal ensemble.
- The real-world matter dominance is consistent with (but not
  uniquely explained by) such a shear in the early universe's
  geometry.

The closing summary [Chapter 8](08-closing-summary.md)
consolidates this and the rest of the project's findings.

---

## What's next

For the next chapter and the rest of the project arc, see the
project [README's table of contents](README.md#chapters).
