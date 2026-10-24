# Chapter 1: What any host must do

## §1. The chapter's job

In the MaSt framework, a particle is a standing wave on a small compact structure, its **host**. The electron and proton each have a 2D compact sheet. For the neutrino, the host is undecided: it could be a 1D closed line, a 2D sheet, or something else.

Before comparing hosts, it helps to know what any host has to achieve. This chapter collects those requirements from experiment, stated without reference to a particular host. Each requirement is graded by how firmly the data establish it.

Supporting numbers and references are collected in [reference/experimental-constraints.md](reference/experimental-constraints.md).

## §2. The neutrino in brief

The neutrino is an electrically neutral particle that interacts only through the **weak interaction**, the force responsible for radioactive beta decay (and, like everything with energy, through gravity). It interacts so feebly that about a hundred trillion neutrinos from the Sun pass through a person every second unnoticed.

Two ways of labeling neutrinos will both be needed:

- **Flavor.** A neutrino is produced alongside a charged partner: the electron, the muon, or the tau. It is labeled by that partner: ν_e, ν_μ, ν_τ. Flavor is the identity a neutrino has when it is created or detected.
- **Mass state.** Separately, there are three states of definite mass, ν₁, ν₂, ν₃, with masses m₁, m₂, m₃.

The two labelings do not coincide. Each flavor is a fixed *mixture* of the three mass states. That mismatch is what produces oscillation (§6).

## §3. Requirement 1: carry half-integer angular momentum

### Spin

**Spin** is angular momentum that a particle carries intrinsically, not because it is orbiting anything. It is measured in units of ℏ, the reduced Planck constant (ℏ ≈ 1.05×10⁻³⁴ J·s). Electrons, protons, and neutrons each have spin ½. Angular momentum from orbital motion, by contrast, always comes in whole units: 0, 1, 2, …

### Pauli's argument

In beta decay, a neutron turns into a proton and an electron. If those were the only products, the decay would read

> n → p + e⁻

On the left is spin ½. On the right, two spin-½ particles combine to a whole-number total (0 or 1), and adding any orbital angular momentum keeps it whole. A half-integer cannot equal a whole number, so angular momentum would not be conserved.

In 1930 Pauli proposed that a third, unseen particle is emitted. Today the decay is written

> n → p + e⁻ + ν̄

where ν̄ is an antineutrino. For the totals to balance, the antineutrino must have half-integer spin: ½, 3/2, 5/2, … The decay of the pion (spin 0) into a muon (spin ½) and a neutrino gives the same conclusion independently.

The argument uses nothing but conservation of angular momentum and well-measured spins of other particles. Half-integer spin is therefore about as firm as any fact in particle physics.

### What this requires of a host

The neutrino leaves the decay and travels away, often for astronomical distances. The angular momentum it carries goes with it. The other particles involved in the decay cannot hold it on the neutrino's behalf. Whatever the host is, it must be able to receive half-integer angular momentum when the neutrino is created and carry it away.

The argument says nothing about *how* the host stores that angular momentum internally. This is the first place where hosts can genuinely differ.

## §4. Requirement 2: behave as spin ½ from outside

Carrying the right amount of angular momentum is not the whole of being spin ½. A spin-½ particle also has three characteristic behaviors that an outside observer can, in principle, test.

### The sign change under rotation

Rotate a spin-½ particle by a full 360° and its quantum state does not return to itself: it returns with a minus sign. Only a 720° rotation restores it. A sign change on its own is invisible, but it becomes visible in interference, when the rotated part of a wave is recombined with an unrotated part. It was observed directly for neutrons in 1975 by neutron interferometry. For neutrinos it has not been tested directly, but it follows mathematically from half-integer angular momentum.

*Signals analogy:* a ring oscillator, a loop of an odd number of inverters. A signal sent once around the loop comes back inverted, and only after two trips is it restored.

### Fermi statistics

Particles with half-integer spin are **fermions**: no two identical fermions can occupy the same state (the **Pauli exclusion principle**). Particles with whole-number spin are **bosons** and have no such restriction. In relativistic quantum theory, the **spin-statistics theorem** ties the two together: half-integer spin means fermion. Neutrino statistics leave a measurable imprint on the early universe, which is weighted differently for fermions than for bosons (§7).
<!--EC I'm not sure what this paragraph is good for.  I don't want to defer to rules (like Pauli) unless we have a physical _reason_ behind the rule (like conservation).  And I don't want to defer to theories (big bang, early universe) as though they are fundamental/given. -->

### Helicity

**Helicity** is the projection of a particle's spin onto its direction of motion. For spin ½ it is +½ (right-handed: spinning like a right-hand screw advancing) or −½ (left-handed). The neutrinos that take part in weak interactions are observed to be left-handed, and antineutrinos right-handed. This was first measured by Goldhaber and collaborators in 1958.

### Exactly ½, not 3/2

Pauli's argument permits ½, 3/2, 5/2, … Several independent measurements single out ½:
- the helicity measurement above;
- the rate at which Z bosons decay to unseen particles, which counts the light neutrino species and assumes spin-½ couplings;
- the early-universe count of light particles (§7);
- the precise shapes of beta-decay and muon-decay energy spectra.

None of these is a direct spin measurement. No neutrino magnetic moment has ever been detected, so the standard way of measuring spin, deflection in a magnetic field gradient, is unavailable. The evidence is indirect but consistent, and spin ½ is the only value that fits all of it.

<!--EC seems like _some_ aspect of the 1/2 spin could be contained in the way a (possibly) 1D neutrino host is disposed in relation to a hadron sheet, for example.  In a 1D neutrino, it might not need to full contain (internally) the 1/2 aspect of the information but rather it might require the context of the _relationship_ between the neutrino host and the electron/proton host sheets. 

Does "from the outside" mean "from the perspective of the electron and proton/neutron?
-->

### What this requires of a host

From outside, the host must show the 360° sign change, fermion statistics, and the observed helicity. Again, this constrains behavior as seen from ordinary space, not the internal mechanism.

## §5. Requirement 3: neutral everywhere, not just in total

### Two kinds of neutral

A particle can have zero total charge in two different ways:

- **Nothing to cancel:** no charge anywhere inside it.
- **Cancellation:** positive and negative regions that add to zero.

The neutron is neutral the second way. Its quarks carry charges +2/3 and −1/3, arranged so that the total is zero but not each point. Two measurable quantities expose such internal structure:

- **Charge radius.** The mean square charge radius, ⟨r²⟩, weights each bit of charge by the square of its distance from the center. For a particle with separated + and − regions, ⟨r²⟩ is nonzero even though the total charge is zero. Its sign says which charge sits further out. For the neutron, ⟨r²⟩ ≈ −0.116 fm², with the negative charge further out. (1 fm, a femtometer, is 10⁻¹⁵ m.)
- **Magnetic moment.** Circulating charge acts as a small magnet. The neutron's magnetic moment is large, −1.91 nuclear magnetons, even though its net charge is zero.

### What the neutrino shows

For the neutrino, neither quantity has been detected:
- the charge radius is limited to about 10⁻³² cm², roughly 100,000 times smaller than the neutron's;
- the magnetic moment is limited to less than about 6×10⁻¹² Bohr magnetons. A **Bohr magneton**, μ_B ≈ 9.27×10⁻²⁴ J/T, is the natural unit of magnetic moment for an electron.

### Why the limits are so restrictive

A particle's natural internal size is of order its **Compton wavelength**, λ = h/(mc), where h = 2πℏ is Planck's constant. Lighter particles have larger Compton wavelengths. For a neutrino mass of 0.05 eV, λ is about 25 μm, tens of micrometers. If structure on that scale contained separated + and − regions like the neutron's, the charge radius and magnetic moment would be enormous, not merely detectable.

### What this requires of a host

Neutrality by cancellation of separated charges is effectively ruled out. The host must generate no charge density anywhere, or cancel it at every point, not just in total.

<!--EC Have we jumped to conclusions here, or been too dogmatic?  For example, consider two tori, one inside the other, where one has + charge and the other has -.  Would this structure act like a neutrino because there are no localized + or - regions measurable? -->

## §6. Requirement 4: the mass spectrum

### Oscillation measures mass differences

Because each flavor is a mixture of mass states, a neutrino created as, say, ν_e is a superposition of ν₁, ν₂, and ν₃. As it travels, each mass component accumulates phase at a slightly different rate, so the mixture drifts. A detector far away finds some probability of a different flavor. This is **neutrino oscillation**, and its discovery earned the 2015 Nobel Prize.

Why the rates differ: a relativistic particle of energy E and mass m has momentum p ≈ E/c − m²c³/(2E). Two mass states with the same energy therefore have slightly different momenta, and hence slightly different wavelengths. Over a distance L, their relative phase grows in proportion to the difference of their squared masses, Δm² = m_i² − m_j². For two flavors with mixing angle θ, the probability of changing flavor is:

<!-- P = sin²(2θ) · sin²(Δm² c³ L / (4ℏE))  ≈ sin²(2θ) · sin²(1.27 · Δm²[eV²] · L[km] / E[GeV]) -->
$$
P = \sin^2(2\theta)\,\sin^2\!\left(\frac{\Delta m^2 c^3 L}{4\hbar E}\right) \approx \sin^2(2\theta)\,\sin^2\!\left(1.27\,\frac{\Delta m^2[\mathrm{eV}^2]\; L[\mathrm{km}]}{E[\mathrm{GeV}]}\right)
$$

(In particle physics, masses are quoted in energy units, writing m for mc², so Δm² is in eV².)

*Signals analogy:* two carriers at slightly different frequencies, launched together, produce a beat. Here the beat is in distance instead of time. The mixing angle sets how deep the beat goes, and Δm² sets how often it repeats.

The key consequence: **oscillation measures differences of squared masses, not the masses themselves.**

### The measured values

| Quantity | Value | Typical measurement |
|---|---|---|
| Δm²₂₁ ("solar") | ≈ 7.5×10⁻⁵ eV² | solar neutrinos; reactor antineutrinos at ~180 km |
| \|Δm²₃₁\| ("atmospheric") | ≈ 2.5×10⁻³ eV² | neutrinos from cosmic rays in the atmosphere; accelerator beams over hundreds of km |
| Ratio Δm²₃₁ / Δm²₂₁ | ≈ 33.6 | |

The sign of Δm²₃₁ is not yet known. In **normal ordering**, ν₃ is the heaviest; in **inverted ordering**, ν₃ is the lightest. Current data mildly prefer normal ordering.

### The pattern

The ratio of about 34 has a structural meaning: **two of the mass states are nearly degenerate, and the third is well separated.** A host must contain something that splits a pair slightly while setting the third state much further away. A spectrum with roughly even spacing will not do.

### Absolute masses: a narrow window

The masses themselves are bounded from both sides:
- **From below:** the splittings require at least one mass to be ≳ 50 meV. With normal ordering and the lightest mass zero, the sum is Σm ≈ 0 + 8.7 + 50 ≈ 59 meV.
- **From above, directly:** the KATRIN experiment, which measures the endpoint of tritium beta decay, limits the mass to below 0.45 eV.
- **From above, through cosmology:** neutrino mass slows the growth of large-scale structure in the universe. Recent analyses that combine galaxy surveys (DESI) with the cosmic microwave background limit Σm to below about 70 meV within the standard cosmological model. This bound depends on that model, and it loosens in extended models.

Between about 59 and 70 meV, the window is narrow if the standard cosmological model holds.

### What this requires of a host

Three fermion-class states whose squared-mass differences match the table, arranged as a near-degenerate pair plus a separated third, with absolute masses inside the window above.

## §7. Requirement 5: exactly three light neutrinos that interact

Two independent counts agree that there are three light neutrino species that take part in weak interactions:

- **Z-boson decays.** The Z boson, a carrier of the weak force, can decay into any light neutrino-antineutrino pair. Measuring how often it decays into unseen particles at the LEP collider gave N_ν = 2.984 ± 0.008.
- **The early universe.** The expansion rate of the early universe depends on how many light particles were present. Fits to the cosmic microwave background and to the primordial abundances of light elements give N_eff ≈ 3.0. This count weights fermions by a factor of 7/8 relative to bosons, so it is also sensitive to neutrinos being fermions.
<!--EC I'm hesitant to bring big-bang theory into what we're doing here since it is purely theoretical.  I think Forma views bosons as spurious ringing on the manifold (and not a particle in the physicalist view).

What do we mean by "light neutrino" as opposed to just "neutrino"?  I think the standard model just recognizes 3 neutrino flavors.  Are there non-light neutrinos?
 -->

### What this requires of a host

A host may have more light modes than three, but any extra modes must not couple to the weak interaction in the ordinary way. Such modes are called **sterile**.

## §8. Not yet requirements

Three properties are measured or measurable, but no theory currently predicts them. A host that predicted any of them correctly would gain a great deal. A host that is silent on them is not penalized.

- **Mixing angles.** The mixture of mass states in each flavor is described by three angles: θ₁₂ ≈ 33–34°, θ₂₃ ≈ 42–49° (close to the maximal 45°), and θ₁₃ ≈ 8.5°, together with a poorly measured phase that would make neutrinos and antineutrinos oscillate differently.
- **Majorana or Dirac.** A **Majorana** neutrino is its own antiparticle; a **Dirac** neutrino is distinct from it, as the electron is. The decisive experiments look for **neutrinoless double-beta decay**, a nuclear decay emitting two electrons and no neutrinos, which can happen only if the neutrino is Majorana. It has not yet been seen.
- **The lightest mass.** Oscillation leaves the overall mass scale free within the window of §6.

## §9. Summary

| # | Requirement | Firmness | Constrains |
|---|---|---|---|
| 1 | Carry half-integer angular momentum away | essentially certain (conservation) | what the host carries, not how |
| 2 | Behave as spin ½ from outside: sign change, Fermi statistics, helicity | very strong, indirect | external behavior, not internal mechanism |
| 3 | No charge density anywhere | strong (limits ~10⁵ below the neutron's) | rules out neutrality by cancellation |
| 4 | Squared-mass differences 7.5×10⁻⁵ and 2.5×10⁻³ eV²: a near-degenerate pair plus a distant third, Σm in a narrow window | measured; upper Σm bound model-dependent | the host's mode spectrum |
| 5 | Exactly three light, weakly interacting states | measured | extra light modes must be sterile |
| — | Mixing angles, Majorana or Dirac, lightest mass | measured or open; no theory predicts them | opportunities, not requirements |

The chapter list is in the [README](README.md#chapter-arc).
