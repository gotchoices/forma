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

### Exclusion follows from the sign change

For electrons, a further behavior is well established: no two electrons can occupy the same state. This is the **Pauli exclusion principle**, and it is what gives atoms their shell structure. It is not an independent rule. Swapping two identical particles is geometrically equivalent to rotating one of them by 360° relative to the other, so a particle that changes sign under a 360° rotation also changes sign when two copies are swapped, and a state with two copies in the same place cancels itself. (The formal statement is the **spin-statistics theorem**.)

For neutrinos, exclusion has not been tested directly in any way that does not lean on theory. It is listed here as a consequence of the sign change, not as a separate requirement.

### Helicity

**Helicity** is the projection of a particle's spin onto its direction of motion. For spin ½ it is +½ (right-handed: spinning like a right-hand screw advancing) or −½ (left-handed). The neutrinos that take part in weak interactions are observed to be left-handed, and antineutrinos right-handed. This was first measured by Goldhaber and collaborators in 1958.

### Exactly ½, not 3/2

Pauli's argument permits ½, 3/2, 5/2, … Several independent measurements single out ½:
- the helicity measurement above;
- the rate at which Z bosons decay to unseen particles (§7), which is interpreted assuming spin-½ couplings;
- the precise shapes of beta-decay and muon-decay energy spectra.

None of these is a direct spin measurement. No neutrino magnetic moment has ever been detected, so the standard way of measuring spin, deflection in a magnetic field gradient, is unavailable. The evidence is indirect but consistent, and spin ½ is the only value that fits all of it.

### What "from outside" means

"From outside" means as measured by apparatus in ordinary 3D space: rotating the experiment, comparing the spin direction with the direction of travel, and detecting the neutrino in a target far from where it was made. In MaSt terms it means relative to space (S), not relative to the neutrino's own host.

That leaves room for spin ½ to reside in a *relationship* rather than wholly inside the host. There is, however, a limit on which relationships qualify. A neutrino made in the Sun reaches a detector on Earth, eight light-minutes away, still showing left-handed helicity. The spin-½ character cannot depend on the neutrino's continued relation to the particular electron or proton sheets it was created with, because those are left behind.

The relationship that does travel with the neutrino is its relationship to space itself. A 1D host whose orientation within S carries part of the half-integer character, so that a 360° rotation in S does not return the host to an equivalent configuration, would satisfy the requirement without holding it all internally. The electron and proton sheets of the source and of the detector matter at the moments of creation and detection, where angular momentum is handed over, but not in between.

### What this requires of a host

From outside, the host, together with its relationship to space, must show the 360° sign change and the observed helicity, and must keep showing them while it travels alone. This constrains behavior as seen from ordinary space, not the internal mechanism.

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

This reasoning assumes the host is about as large as the Compton wavelength, as MaSt's sheets are. A host much smaller than its Compton wavelength would loosen the constraint, though even then a unit charge separation would have to stay below about 10⁻³ fm.

### A test case: nested tori of opposite charge

Consider two tori, one inside the other, one carrying charge +e and the other −e. Seen from far away, the total is zero. Is the combination neutral enough?

A probe that scatters off the particle, such as an electron bouncing off it, does not see "regions." It sees how the charge is distributed in radius, which is exactly what ⟨r²⟩ measures. For charge +e at radius r₁ and −e at radius r₂, ⟨r²⟩ = r₁² − r₂². With r ≈ 25 μm, the limit of 10⁻³² cm² requires the two radii to agree to within about 2×10⁻³² m, roughly 10¹⁹ times smaller than the tori themselves.

Circulation makes it harder still. If the + charge circulates one way and the − charge the other, the two currents point the same way and their magnetic moments add. They cancel only if both charges circulate in the same sense, at the same radius.

So nested tori work only in the limit where the two coincide: + and − occupying the same place and moving together. That is not a loophole in the requirement but a way of meeting it, since such a structure has zero charge density at every point.

### What this requires of a host

Neutrality by cancellation between **separated** charges is ruled out to extraordinary precision. The host must generate no charge density anywhere, or carry + and − contributions that coincide at every point, in position and in motion.

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
Cosmological analyses also quote a much tighter limit, Σm below about 70 meV. That number is derived *within* a cosmological model (the expansion history of the universe and the growth of structure in it), not measured independently of one. It is recorded here as context, not used as a requirement.

### What this requires of a host

Three states whose squared-mass differences match the table, arranged as a near-degenerate pair plus a separated third, with Σm of at least about 59 meV and masses below the direct limit.

## §7. Requirement 5: exactly three neutrinos that interact

### The count

The Standard Model has three neutrino flavors, one for each charged lepton. That number was built into the model to match observation; the model does not explain it. The measurement that checks it comes from the **Z boson**, a carrier of the weak force with a mass of about 91 GeV.

A Z boson can decay into any neutrino-antineutrino pair whose combined mass is less than its own, so any neutrino lighter than about 45 GeV (half the Z mass). Those decays are invisible to detectors, but they shorten the Z's lifetime and so broaden its resonance peak. Measuring the shape of that peak at the LEP collider gave the number of such neutrino types as N_ν = 2.984 ± 0.008. Converting the peak width into a count uses the weak-interaction theory's prediction of how much each neutrino type contributes, so the result is a measurement interpreted through that theory.

### "Light" and heavy neutrinos

"Light" here means lighter than about 45 GeV, the reach of the Z-decay count. All three known neutrinos are lighter than that by more than ten orders of magnitude. Heavier neutral particles that behave like neutrinos ("heavy neutral leptons") are proposed in some theories and searched for, but none has been found. So in practice "light neutrino" and "neutrino" refer to the same three, and the qualifier only marks the limit of what the Z count can see.

### What this requires of a host

A host may have more modes than three, but any extra modes below about 45 GeV must not couple to the Z in the ordinary way. Such non-coupling modes are called **sterile**.

## §8. Not yet requirements

Three properties are measured or measurable, but no theory currently predicts them. A host that predicted any of them correctly would gain a great deal. A host that is silent on them is not penalized.

- **Mixing angles.** The mixture of mass states in each flavor is described by three angles: θ₁₂ ≈ 33–34°, θ₂₃ ≈ 42–49° (close to the maximal 45°), and θ₁₃ ≈ 8.5°, together with a poorly measured phase that would make neutrinos and antineutrinos oscillate differently.
- **Majorana or Dirac.** A **Majorana** neutrino is its own antiparticle; a **Dirac** neutrino is distinct from it, as the electron is. The decisive experiments look for **neutrinoless double-beta decay**, a nuclear decay emitting two electrons and no neutrinos, which can happen only if the neutrino is Majorana. It has not yet been seen.
- **The lightest mass.** Oscillation leaves the overall mass scale free within the window of §6.

## §9. Summary

| # | Requirement | Firmness | Constrains |
|---|---|---|---|
| 1 | Carry half-integer angular momentum away | essentially certain (conservation) | what the host carries, not how |
| 2 | Behave as spin ½ relative to space, while traveling alone: 360° sign change (exclusion follows), helicity | very strong, indirect | external behavior; may reside partly in the host's relation to space |
| 3 | No charge density anywhere; any + and − must coincide in position and motion | strong (limits ~10⁵ below the neutron's) | rules out cancellation between separated charges |
| 4 | Squared-mass differences 7.5×10⁻⁵ and 2.5×10⁻³ eV²: a near-degenerate pair plus a distant third; Σm ≳ 59 meV; below the direct limit | measured | the host's mode spectrum |
| 5 | Exactly three types lighter than ~45 GeV that couple to the Z | measured, interpreted through weak-interaction theory | extra modes must be sterile |
| — | Mixing angles, Majorana or Dirac, lightest mass | measured or open; no theory predicts them | opportunities, not requirements |

The chapter list is in the [README](README.md#chapter-arc).
