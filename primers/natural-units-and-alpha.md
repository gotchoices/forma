# Natural Units and Why Alpha Is Still Alpha

What the vacuum is made of, why most physical constants are
bookkeeping, and how α emerges from the geometry of a confined
photon.  Assumes basic calculus and comfort with EM fields.

---

## 1. The two spring constants of the vacuum

Even in a perfect vacuum, electromagnetic fields exist and
propagate.  Two constants describe how the vacuum responds:

- **ε₀** (permittivity) — how much the vacuum resists an
  electric field.  Appears in Coulomb's law as a denominator:
  larger ε₀ → weaker electric force.

- **μ₀** (permeability) — how readily the vacuum supports a
  magnetic field.  Appears in the Biot-Savart law as a
  numerator: larger μ₀ → stronger magnetic force.

The energy stored in each field is:

    u_E = ½ ε₀ E²       (electric energy density)
    u_B = B² / (2μ₀)    (magnetic energy density)

These are exactly analogous to the energy ½kx² stored in a
spring with constant k.  So ε₀ is the spring constant for
electric fields, and 1/μ₀ is the spring constant for magnetic
fields.

In an electromagnetic wave, E and B are 90° out of phase —
energy sloshes between the electric "spring" and the magnetic
"spring," just like energy sloshes between a capacitor and an
inductor in an LC circuit:

| LC circuit          | EM wave in vacuum       |
|---------------------|-------------------------|
| Capacitor stores E  | ε₀ stores electric E    |
| Inductor stores E   | μ₀ stores magnetic E    |
| Resonant freq 1/√LC | Wave speed 1/√(ε₀μ₀)   |

That last line is Maxwell's great result:

    c = 1/√(ε₀ μ₀)

The speed of light is the resonant frequency of the vacuum's
own LC circuit.  This is not analogy — it is the same
mathematics.

The two springs are cross-coupled: a changing E induces B
(Faraday's law) and a changing B induces E (Ampère's law with
Maxwell's correction).  This cross-coupling is what lets the
disturbance travel rather than ring in place.


## 2. Natural units — the springs are identical

In SI, ε₀ ≈ 8.854 × 10⁻¹² F/m and μ₀ ≈ 1.257 × 10⁻⁶ H/m.
They have different values, different units, different scales.
This makes E and B look like fundamentally different things.

They are not.

The asymmetry is entirely an artifact of the SI unit system,
which was built around human-scale quantities (amperes from
wire forces, volts from batteries) before anyone understood
that electricity and magnetism are two views of one phenomenon.

In special relativity, E and B are not even separate objects.
They are components of a single electromagnetic field tensor
F^μν.  A purely electric field in one reference frame has a
magnetic component in a moving frame, and vice versa.

**Natural units** make this manifest by setting:

    c = 1       (time and length are the same dimension)
    ε₀ = 1      (absorbs the charge-to-field conversion)
    μ₀ = 1      (follows from c = ε₀ = 1, since μ₀ = 1/(ε₀c²))

With these choices, Maxwell's equations become:

    ∇·E = ρ               (Gauss: charge creates E)
    ∇·B = 0               (no magnetic monopoles)
    ∇×E = −∂B/∂t          (Faraday: changing B creates E)
    ∇×B = J + ∂E/∂t       (Ampère-Maxwell: current and
                            changing E create B)

No dangling constants.  E and B have the same dimensions.
The two springs are manifestly identical in stiffness.


## 3. What collapses

SI has 7 independent base units.  Natural units reduce them
to 2 — a unit of length and a unit of energy.

| SI quantity       | Natural units            |
|-------------------|--------------------------|
| Time (seconds)    | Same dimension as length  |
| Mass (kg)         | Same dimension as energy  |
| Charge (coulombs) | → √energy               |
| Voltage (volts)   | → √energy               |
| Current (amperes) | → √energy / length      |
| B field (tesla)   | Same dimension as E field |

The most dramatic collapse is **charge**.  In SI, charge is an
independent base dimension — you cannot express coulombs in
terms of meters, kilograms, and seconds without ε₀ doing the
conversion.  Setting ε₀ = 1 eliminates that conversion,
and charge becomes expressible in terms of mass and length.

From Coulomb's law in natural units:

    F = q₁ q₂ / r²

Force has dimensions of energy/length.  Since r² has dimensions
of length², q² must have dimensions of energy.  So charge has
dimensions of √energy.

This is not a trick.  It reflects something real: **energy is
always bilinear**.  Coulomb energy requires two charges meeting
(q × q / r), just as kinetic energy requires velocity meeting
itself (m v²).  Charge is the amplitude; energy is the
amplitude squared.  One charge brings its √energy to the table;
two charges together produce energy.


## 4. The two scales of the electron

Every electron has two intrinsic energy scales.  Both are
measurable; neither is derived from the other.

### Scale 1: mass-energy

The electron has rest mass m_e.  In natural units (c = 1),
this is also its rest energy:

    E_mass = m_e

This sets a quantum length scale — the reduced Compton
wavelength:

    λ̄_C = 1/m_e

A photon with this wavelength carries exactly the electron's
rest mass energy.  In SI:

    λ̄_C = ℏ/(m_e c) ≈ 3.86 × 10⁻¹³ m

This is the electron's "quantum size" — the scale at which a
photon carries enough energy to be "aware" of the electron's
mass (pair production becomes kinematically possible).

### Scale 2: charge-energy

The electron has charge e.  The Coulomb energy of this charge,
evaluated at the Compton wavelength, is (in SI):

    U_charge = e²/(4πε₀ λ̄_C)

Now set ε₀ = 1 (natural units).  The ε₀ disappears, but the
4π stays — it comes from the surface area of a sphere
(Gauss's law in 3D), not from unit conventions:

    U_charge = e²/(4π λ̄_C)

Substitute λ̄_C = 1/m_e:

    U_charge = e² m_e / (4π)

Now form the ratio of the two energy scales:

    U_charge     e² m_e / (4π)     e²
    --------  =  -------------  =  ---
    E_mass            m_e          4π

The m_e cancels.  What remains is a pure number — independent
of every unit choice, independent of the electron's mass:

    α  =  e²/(4π)  ≈  1/137.036

**This is the fine-structure constant.**

No spectroscopy, no hydrogen atom, no historical accident.
Alpha is the answer to a single question: if you compare the
electron's electromagnetic energy to its total energy, at the
electron's own quantum scale, what fraction is electromagnetic?

The answer is about 1/137.


## 5. Alpha runs — but it's still alpha

The low-energy value α ≈ 1/137 is not the whole story.
Alpha is a function of the **probe energy** μ.

What does "probe energy" mean?  When two charged particles
interact, they exchange a virtual photon.  That photon has
an energy set by the collision.  The de Broglie relation
λ = ℏ/p means a higher-energy photon has a shorter wavelength
— it probes smaller distances.  So "probe energy" is just
the energy of the collision, which determines how closely you
examine the charge.

The running is governed by the renormalization group equation
(one-loop QED):

    1/α(μ) = 1/α₀ − (2/3π) ln(μ/m_e)

Plotted as 1/α vs. log(energy), it is a straight line with
slope −2/(3π), slanting downward — α gets larger (coupling
gets stronger) at higher energies.

The physical mechanism is **vacuum polarization**.  The vacuum
is not empty: virtual electron-positron pairs constantly
flicker in and out of existence.  Near a real charge, these
pairs polarize — the virtual positron is pulled toward the
real charge, the virtual electron pushed away — partially
screening the bare charge.  What you measure at a distance
is the screened charge, which is weaker than the bare charge.

Higher probe energy = shorter wavelength = you punch deeper
into the screening cloud = you see more of the bare charge =
stronger effective coupling.

Measured values across the energy spectrum:

| Scale              | 1/α     | How measured              |
|--------------------|---------|---------------------------|
| Atomic (~ 0)       | 137.036 | Hydrogen spectroscopy     |
| ~ 1 MeV            | ~ 136   | Electron scattering       |
| ~ 57 GeV           | ~ 130   | LEP (below Z peak)        |
| m_Z (91 GeV)       | 127.95  | LEP (Z pole)              |
| ~ 200 GeV          | ~ 127   | LEP2                      |

The running is experimentally confirmed across several orders
of magnitude in energy.  It is a smooth continuum, not two
discrete values — LEP traced the predicted logarithmic curve
precisely.

In natural units, the running equation contains no ε₀, no μ₀,
no ℏ, no c — just α and the fermion masses.  The constants
were never there.  Alpha is still alpha.


## 6. Three forces, one coupling?

Electromagnetism is not the only force with a running coupling
constant.  The Standard Model has three forces, each with its
own coupling that runs with energy:

| Force           | Carrier    | Coupling | Low energy |
|-----------------|------------|----------|------------|
| Electromagnetic | Photon     | α₁       | 1/137      |
| Weak            | W, Z       | α₂       | 1/30       |
| Strong          | Gluons     | α₃       | ~ 1        |

Each coupling runs according to the same type of equation,
but with a different slope determined by the force's internal
structure:

    1/αᵢ(μ) = 1/αᵢ(μ₀) − (bᵢ/2π) ln(μ/μ₀)

The sign of bᵢ is the key:

- **Electromagnetic (b₁ > 0):** photons are neutral, so only
  fermions contribute to screening.  α₁ increases with energy.
  The line 1/α₁ slopes downward.

- **Weak (b₂ < 0):** W bosons carry weak charge and interact
  with each other.  Their self-interaction anti-screens —
  overwhelming the fermion screening.  α₂ decreases with
  energy.  The line 1/α₂ slopes upward.

- **Strong (b₃ < 0, steep):** 8 gluons all carry color charge
  and interact vigorously.  Anti-screening dominates strongly.
  α₃ decreases with energy — this is **asymptotic freedom**
  (Nobel Prize 2004).  At low energies α₃ ≈ 1, making
  perturbation theory useless and quark confinement inevitable.

In the 1/α vs. log(energy) plot, two lines slope upward
and one slopes downward.  They converge.

### Do they meet?

In the Standard Model alone, the three lines nearly converge
at around 10¹⁵ GeV but miss by a small, statistically
significant margin — they form a tiny triangle.

With supersymmetry (SUSY) added, the beta coefficients shift
and the three lines meet at a single point:

    μ_GUT ≈ 2 × 10¹⁶ GeV       α_GUT ≈ 1/24

| Scale                  | α₁ (EM) | α₂ (weak) | α₃ (strong) |
|------------------------|---------|-----------|-------------|
| Low energy             | 1/137   | 1/30      | ~ 1         |
| m_Z (91 GeV)           | 1/128   | 1/32      | 0.118       |
| μ_GUT (SUSY, ~10¹⁶ GeV) | 1/24    | 1/24      | 1/24        |

If this convergence is real, it would mean that at extremely
high energies the three forces are manifestations of a single
unified force with coupling 1/24.  The enormous differences
we observe at low energies — α₁ = 1/137, α₃ ≈ 1, a factor
of 137 apart — would be entirely an artifact of 16 orders of
magnitude of logarithmic running from where they were born
equal.

The convergence is confirmed as a trend (all three run in the
right directions, at the right rates) but the meeting point
at 10¹⁶ GeV is an extrapolation — no collider has come close
to that energy.  It remains one of the strongest indirect
arguments for physics beyond the Standard Model.


## 7. What alpha is — summary

| Statement                              | In SI               | Natural units |
|----------------------------------------|----------------------|---------------|
| Photon energy at Compton wavelength     | ℏc/λ̄_C = m_e c²    | 1/λ̄_C = m_e  |
| Coulomb energy at Compton wavelength    | e²/(4πε₀ λ̄_C)      | α m_e         |
| Ratio: EM energy / total energy        | e²/(4πε₀ ℏc) = α   | α             |
| Bohr radius (atomic scale)             | ℏ/(m_e c α) = λ̄_C/α | 1/(α m_e)    |

Two ways to read α:

1. **A coupling strength.**  The probability of a charged
   particle emitting a photon is proportional to √α.  The
   probability of an EM interaction (two vertices) is
   proportional to α ≈ 1/137.  Because α ≪ 1, each
   additional photon exchange is 137× less likely — which is
   why perturbation theory works in QED.

2. **A ratio of scales.**  The electron's charge-scale (r_e)
   is α times its mass-scale (λ̄_C).  The atom's size (Bohr
   radius) is 1/α times its mass-scale.  Alpha is the bridge
   between the particle world and the atomic world.

Both are the same number.  Natural units make this transparent
by stripping away the unit conversions that obscure the
relationships in SI.

---

*Sources:*
- *Spring constants, natural units, running couplings:*
  Dialog in `reference/claude-epsilon-mu-alpha.md`
- *α as ratio of energy scales:*
  `studies/R7-torus-capacitance/findings.md`, F3
