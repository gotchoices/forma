# Q98. Are quark generations real or a labeling convention?

**Status:** Likely — structural argument
**Related:**
  [Q86](Q86-three-generations.md) (three lepton/neutrino generations),
  [Q90](Q90-ephemeral-mode-decomposition.md) (quarks as transient sub-modes),
  R27 F17–F20 (muon/tau mode identification),
  R26 (neutrino mass splittings)

---


## 1. The Standard Model pattern

The SM arranges fermions into three generations:

| Gen | Leptons       | Quarks       |
|-----|---------------|--------------|
| 1   | e⁻,  ν_e     | u, d         |
| 2   | μ⁻,  ν_μ     | c, s         |
| 3   | τ⁻,  ν_τ     | t, b         |

Each generation is a heavier copy of the previous, with
identical charge and spin.  The SM offers no explanation for
why there are exactly three, or why the pattern is the same
across leptons and quarks.


## 2. What MaSt says about lepton generations

MaSt produces three charged leptons as **cross-sheet modes**
on Ma_e × Ma_p (Q86):

| Particle | Mode                    | Mass      | Sheets      |
|----------|-------------------------|-----------|-------------|
| e⁻       | (1, 2, 0, 0, 0, 0)     | 0.511 MeV | Ma_e only   |
| μ⁻       | (−1, +5, 0, 0, −2, 0)  | 105.7 MeV | Ma_e × Ma_p |
| τ⁻       | (−1, +5, 0, 0, −2, −4) | 1876 MeV  | Ma_e × Ma_p |

The mechanism: Ma_e has large radii (~386 fm circumferences),
so modes confined to it alone are light.  Ma_p has small
radii (~24 fm ring circumference), so each winding on Ma_p
contributes hundreds of MeV.  The muon and tau are Ma_e
modes that **reach into** the more energetic Ma_p sheet,
gaining mass without changing charge.


## 3. Three neutrino generations

R26 identifies three modes on Ma_ν with mass-squared
splittings matching experiment (Δm²₃₁/Δm²₂₁ = 33.6).
These are three solutions on the same sheet, analogous to
three standing-wave overtones.


## 4. Why there is only one proton generation

The generation mechanism for leptons is **asymmetric**: a
mode on a large-radii (low-energy) sheet gains mass by
adding windings on a small-radii (high-energy) sheet.

Ma_p is already the smallest sheet — the one with the
highest energy per winding.  There is no sheet below it
to reach into.

The only cross-sheet options are Ma_e and Ma_ν:

- A Ma_e winding adds ~0.25 MeV — a 0.03% perturbation
  on the proton's 938 MeV
- A Ma_ν winding adds ~0.02 eV — unmeasurable

Neither can create a dramatically heavier proton-like mode.
The cross-sheet mechanism that creates the muon at 207×
the electron mass cannot create a "muonic proton" at 207×
the proton mass, because there is no denser sheet to
draw energy from.

Higher-energy modes on Ma_p itself do exist — they are the
nuclear resonances (Δ, N*, Σ, …).  But these are excited
states on the same sheet (different winding numbers),
not cross-sheet generations.  Most are broad resonances
that decay in ~10⁻²³ s.  They are overtones, not
replicas.


## 5. What "quark generations" actually are

In the SM, the three quark generations (u/d → c/s → t/b)
appear structurally parallel to the three lepton
generations.  MaSt says this parallelism is misleading.

MaSt does not have fundamental quarks (Q90).  The proton
is a single (1,2) eigenmode on Ma_p.  When probed at high
energy, this mode briefly decomposes into three transient
sub-modes — which experimenters call quarks.

The six "quark flavors" map to different sub-mode winding
partitions of the parent hadron (Q90 §10.1):

| SM flavor | MaSt interpretation                    |
|-----------|----------------------------------------|
| u, d      | Sub-modes of the proton/neutron (1,2)  |
| s         | Sub-mode with higher winding number    |
| c, b, t   | Sub-modes of heavier hadronic modes    |

The three "generations" are not three replicas of the same
blueprint.  They are an organizational scheme that groups
sub-modes by charge into families.  The grouping is useful
for bookkeeping but does not reflect an underlying
three-copy symmetry.


## 6. The structural asymmetry

The SM treats lepton and quark generations identically.
MaSt reveals a deep structural difference:

| Feature          | Lepton generations          | "Quark generations"                  |
|------------------|-----------------------------|--------------------------------------|
| Mechanism        | Cross-sheet eigenmodes       | Sub-mode decomposition channels      |
| Fundamental?     | Yes — distinct stable modes  | No — transient patterns              |
| Why three?       | Mode counting + cavity Q     | Combinatorics of winding partitions  |
| Sheet direction  | Small → large (Ma_e into Ma_p) | N/A (all on Ma_p)                 |
| Proton analog?   | Cannot exist (Ma_p is smallest) | —                                 |

The SM's uniform three-generation structure is an artifact
of treating quarks as fundamental.  Once quarks are
recognized as emergent sub-modes, the generational symmetry
between leptons and quarks breaks.

Leptons genuinely come in three generations.  "Quarks" do
not — they come in as many varieties as there are ways to
ring the hadronic bell.


## 7. Testable consequence

If MaSt is correct, the lepton and quark generation counts
are **coincidentally both three**, not structurally linked.
A fourth lepton generation is excluded by the cavity Q
mechanism (R38).  But additional "quark-like" decomposition
channels are freely available at higher energies — and
indeed the SM already contains six flavors, not three,
plus exotic hadrons (tetraquarks, pentaquarks) that extend
the decomposition space.

The decisive test: if a fourth lepton generation is ever
found, MaSt's cavity Q prediction fails.  But discovering
new hadronic resonances (new "quark flavors") is expected
and carries no such implication.
