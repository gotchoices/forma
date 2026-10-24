# Experimental constraints on the neutrino

What is measured, what is inferred, and how firmly. Any host proposed in this project must meet these constraints. Values are approximate and reflect the literature as of late 2026; bounds tighten over time.

## 1. Basic facts

- **Three flavors.** ν_e, ν_μ, ν_τ, paired with the electron, muon, and tau. A *flavor* is the identity a neutrino has when it is produced or detected.
- **Three mass states.** ν₁, ν₂, ν₃, with definite masses m₁, m₂, m₃. A flavor state is a fixed mixture of mass states (§5).
- **Electrically neutral.** The neutrino interacts only through the weak force (and gravity).
- **Very light.** The masses are not individually known, only their differences (§4) and upper bounds on their size.

## 2. Spin: what is measured and what is inferred

**Spin** is intrinsic angular momentum, measured in units of ℏ (the reduced Planck constant). Electrons, protons, and neutrons have spin ½.

### 2.1 Half-integer spin is forced by conservation

This is Pauli's 1930 argument, and it uses only angular momentum conservation and the well-measured spins of other particles.

- In beta decay, n → p + e⁻ + ν̄. The neutron, proton, and electron each have spin ½.
- Orbital angular momentum always comes in whole units.
- Without the neutrino, the final state would have whole-number total angular momentum, while the initial state has ½. Conservation would fail.
- So the neutrino must have half-integer spin: ½, 3/2, 5/2, …

Pion decay, π⁺ → μ⁺ + ν (spin 0 → spin ½ + ν), gives the same conclusion independently.

**Grade: essentially certain**, as firm as angular momentum conservation itself.

### 2.2 Exactly ½ rests on several independent indirect checks

| Evidence | What it shows |
|---|---|
| Goldhaber et al. (1958) | Direct measurement of neutrino helicity (the spin's projection along its direction of motion): left-handed, consistent with −½ |
| LEP: decays of the Z boson to unseen particles | Counts N_ν = 2.984 ± 0.008 light neutrino species, assuming spin-½ couplings. Spin 3/2 would change the rate. |
| Cosmology (cosmic microwave background, Big Bang nucleosynthesis) | N_eff ≈ 3.0 light species. *Model-dependent context, not used as a requirement:* derived within a cosmological model. |
| Weak-interaction spectra | Beta-decay electron spectra and muon-decay distributions match spin-½ predictions to high precision |

There is no direct "Stern–Gerlach" measurement, which would deflect particles by their magnetic moment, because no neutrino magnetic moment has been detected (§3).

**Grade: very strong but indirect.** Among half-integer values, ½ is the only one consistent with all of the above.

### 2.3 What the constraint actually requires of a host

Conservation dictates what the neutrino must carry and how it must behave as seen from ordinary space. It does not dictate how the neutrino stores that angular momentum internally. Separating the two:

**Required externally, whatever the host:**
1. **Carry half-integer angular momentum away.** The neutrino leaves the decay and travels macroscopic distances, so the electron and proton sheets cannot account for the missing angular momentum. It moves with the neutrino.
2. **Transform as spin ½.** Under a 360° rotation in ordinary space, the state changes sign; a 720° rotation restores it. This follows mathematically from half-integer angular momentum. It was measured directly for neutrons by neutron interferometry (Rauch et al., 1975), but has not been measured for neutrinos.
3. **Exclusion (Fermi statistics) follows.** Swapping two identical particles is geometrically equivalent to a 360° relative rotation, so the sign change in item 2 implies that two identical neutrinos cannot share a state (the spin-statistics theorem). Not directly tested for neutrinos; listed as a consequence, not a separate requirement.
4. **Show the observed helicity.** Neutrinos that interact are left-handed, and antineutrinos right-handed.

**Not required:** that the internal storage looks like spin-½ on a 2D sheet, for example spin from a 1:2 winding ratio as in the WvM model (see [R25](../../../studies/R25-neutrino-spin/README.md)). A 1D host, or a host whose angular momentum is handed off from the electron or proton sheet during the decay, may realize items 1–4 by a different internal route.

## 3. Neutrality: limits on charge and charge distribution

A particle can be neutral overall but have internal regions of + and − charge, as the neutron does. That shows up as a nonzero charge radius and a magnetic moment. The neutrino shows neither.

| Quantity | Neutron (measured) | Neutrino (experimental limit) |
|---|---|---|
| Charge radius² ⟨r²⟩ | −0.116 fm² = −1.16×10⁻²⁷ cm² | ≲ 10⁻³² cm², about 5 orders of magnitude smaller |
| Magnetic moment | −1.91 nuclear magnetons | < ~6×10⁻¹² Bohr magnetons (XENONnT, Borexino) |
| Net charge | 0 (to high precision) | ≲ 10⁻¹² e directly (reactor experiments); far tighter indirect bounds from charge conservation and astrophysics |

**The scale makes this sharper.** A particle's natural internal size is of order its Compton wavelength, λ = h/(mc). For m ≈ 0.05 eV, λ is about 25 μm, or about 4 μm for the reduced form λ/2π. If the neutrino had neutron-like + and − regions anywhere near that size, the resulting charge radius and moment would be huge, not merely detectable.

**Consequence for hosts.** Neutrality by *cancellation of separated charges* (neutron-like) is effectively excluded. A host must be neutral because it generates no charge density anywhere, or because whatever charge it generates is cancelled at every point, not just in total.

## 4. Masses

| Quantity | Value |
|---|---|
| Solar splitting Δm²₂₁ | ≈ 7.5×10⁻⁵ eV² |
| Atmospheric splitting \|Δm²₃₁\| | ≈ 2.5×10⁻³ eV² |
| Ratio Δm²₃₁/Δm²₂₁ | ≈ 33.6 |
| Ordering | Normal (ν₃ heaviest) mildly preferred over inverted; not settled |
| Direct mass limit (KATRIN, tritium beta decay) | m_ν < 0.45 eV |
| Sum Σm from cosmology | ≲ 0.07 eV within the standard cosmological model (DESI + CMB, 2024–25). *Model-dependent context, not a requirement.* |
| Minimum Σm allowed by the splittings | ≈ 0.06 eV (normal ordering, m₁ = 0) |

**The pattern is a near-degenerate pair plus a distant third.** Δm²₂₁ is about 1/34 of Δm²₃₁. A host must produce a small parameter that splits a pair slightly. This is a structural requirement, not just a number to fit.

**Cosmology as context.** If the standard cosmological model holds, the window between the oscillation minimum (≈ 0.06 eV) and its bound (≈ 0.07 eV) is narrow. Because that bound is derived within a model, this project records hosts' Σm against it for comparison but does not treat it as a requirement.

## 5. Oscillation and mixing

A neutrino is produced in a flavor state, which is a mixture of the three mass states. The mass states have slightly different masses, so as the neutrino travels they accumulate phase at slightly different rates, and the mixture drifts. The detected flavor therefore changes with distance. The phase difference between mass states i and j grows as Δm²ᵢⱼ·L/(4E), where L is the distance traveled and E the energy.

*Signals analogy:* three carriers at slightly different frequencies. The neutrino is emitted as one specific sum of them, and a detector sees the beat envelope. Oscillation is a beat note in distance rather than in time.

The mixture is described by the **PMNS matrix** (after Pontecorvo, Maki, Nakagawa, Sakata), parameterized by three mixing angles:

| Angle | Value | Character |
|---|---|---|
| θ₁₂ (solar) | ≈ 33–34° | large |
| θ₂₃ (atmospheric) | ≈ 42–49° | near maximal (45°); which side of 45° is unsettled |
| θ₁₃ (reactor) | ≈ 8.5° | small |

There is also a CP-violating phase (CP: the combined charge-conjugation and mirror symmetry), currently poorly measured. No accepted theory predicts these angles, so any host that did would be significant.

**Requirements for oscillation components:**
1. They must have different masses; degenerate components never dephase.
2. They must share a spin class; a fermion cannot be superposed with a boson.
3. Their splittings must match §4.
4. Their mixing must match the angles above.

## 6. Majorana or Dirac: open

A **Majorana** neutrino is its own antiparticle. A **Dirac** neutrino is distinct from its antiparticle, as the electron is. This is unsettled. The deciding experiments search for **neutrinoless double-beta decay**, a nuclear decay that emits two electrons and no neutrinos. It is possible only if the neutrino is Majorana. None has been seen so far.

For a Majorana neutrino, "neutrino" and "antineutrino" are the left- and right-handed helicity states of one particle. A host that predicts Majorana or Dirac is making a testable commitment.
