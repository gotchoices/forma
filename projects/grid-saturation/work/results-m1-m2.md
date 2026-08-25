# Cylinder sim — first results (M1 verified; M2 negative-so-far)

Sim: [`../scripts/cylinder.py`](../scripts/cylinder.py) — a 1D-space × 1D-compact
(x, c) cylinder with the N=4 equal-impedance scatter. Photon = c-uniform
(n=0) wave in x; mass = c-winding (n≥1). Figures in [`../outputs/`](../outputs/).

## M1 — the linear baseline: **verified**

Ran single, head-on, and winding injections with `--sat none`:

- **Photons propagate in x** at ~0.62 nodes/tick (the N=4 scatter speed; cf.
  sim-maxwell's ~0.7 for N=3). ✓
- **Two photons pass through each other** cleanly (head-on, linear). ✓
- **The compact sector is decoupled:** a c-uniform photon keeps E(n≥1) = 0.0000%
  exactly — nothing leaks into the winding modes. ✓ (This is the KK-decoupling
  check, never run dynamically in forma before.)
- **The winding (n=1) mode is massive/gapped:** injected, it does *not*
  propagate in x like the photon (speed ≈ 0) — correct KK behaviour. ✓
- Edge energy (the orthogonal-scatter conserved quantity Σin²) conserves to
  ~3% over the interior window (residual from window edges / sponge; the linear
  scatter is exactly orthogonal).

**M1 stands:** the cylinder is a faithful testbed — Maxwell-like propagation
in x with a compact dimension present, and the compact modes are decoupled and
gapped exactly as KK predicts.

## M2 — pair production (energy S → c): **negative so far, three solid findings**

The goal: drive two photons head-on into saturation and see whether energy
transfers into a **persistent** compact (n≥1) mode — a particle at rest. What
the runs actually established, in order of how they corrected each other:

1. **Symmetry must be broken — and the seed cannot ride the beam.** A perfectly
   c-uniform collision makes *zero* compact structure (symmetry forbids it). An
   early run with a c-structured *source* seed (`--cseed`) seemed to show
   spillover growing the compact fraction by +0.8% while clip did not — but that
   was an **artifact**: the n≥1 seed is **gapped and does not co-propagate**
   with the n=0 photon (exactly the KK decoupling M1 verified), so it **stays at
   the source** and never reaches the collision. Interior (collision-region)
   E(n≥1) was ~0 (machine epsilon) the whole time. **The symmetry-breaking must
   be present *at* the collision** — which is physical: real pair production is
   seeded by **vacuum fluctuations**, not carried in on the beam. (Added
   `--zpe`: a vacuum-noise field on every edge.)

2. **Head-on does not raise the per-edge amplitude.** Counter-propagating
   photons occupy *different directed edges* (+x vs −x), so per-edge saturation
   triggers at nearly the same amplitude for one photon as for two. The
   collision's specialness lives in the **node** (larger scatter sum T), not on
   any single edge — so there is no clean "single-below / collision-above"
   bound. The right test is **saturated vs linear control at identical
   parameters**, differencing out everything the saturation didn't cause.

3. **With a vacuum seed, saturation does NOT pump a trapped mode — at any tested
   frequency.** Control (`--sat none`) vs `clip` vs `spillover`, same seed,
   bound driven well into saturation (lost ≈ 17): interior E(n≥1) after the
   photons exit is **identical across all three** (retained ≈ 81% — but that
   81% is just the **static vacuum-noise floor**: gapped n≥1 modes don't
   propagate, so the noise *sits still*; it is **not** a created particle). A
   frequency sweep (ω = 0.2 … 1.4, same-seed differencing so the floor cancels)
   gives `spillover − control` ≈ **0 to slightly negative everywhere** — no
   resonance, no trapping. Saturation redirects/loses energy per tick, but the
   **linear scatter re-mixes c-edge energy back toward x on the next tick**, so
   nothing accumulates into the compact sector.

### What this means (non-dogmatically)

- **The n≥1 sector exists and is stable** — the vacuum floor persists because
  n≥1 is a gapped, non-propagating eigenmode of the scatter. **A trapped
  particle *could* live there.** The good news is real.
- **What's missing is a *pump*.** Clip and spillover are *per-edge, per-tick*
  responses; they do not phase-lock energy into the stable n≥1 eigenmode, and
  the linear scatter undoes their redirection each tick. Pair production needs a
  nonlinearity that **coherently pumps** the compact eigenmode, which these two
  do not provide.
- This is **"not yet," not "refuted."** The thesis (saturation → S→c transfer →
  a rest particle) is intact; the specific *clip/spillover* realizations don't
  pump. The obstruction is named and concrete.

### Honest caveats

- Only two saturation models tried (clip, spillover); **storage/temporal** and
  **node-state** nonlinearities are untested.
- The frequency sweep varied the *photon* ω; the true resonance may involve the
  c-circumference (nc), amplitude, and pulse shape jointly — a wider space.
- `--quantize` (discrete levels as the symmetry-breaker / trap) is untested.

## M2·A — the trap test: can a compact mode self-bind? **No — the bound is defocusing**

Before building a *pump*, test the *trap*: excite an n≥1 compact mode **at rest**
(injected at domain center on equal ±x edges, zero net x-momentum) and ask
whether it survives as a stable, localized object. Findings:

1. **Linear: a localized compact mode disperses and radiates away** — retained
   **0.0%** of peak (final E(n≥1) → machine zero) at every amplitude, though its
   *center* stays put (speed 0). This is textbook **KK dispersion**: a localized
   massive mode is a superposition of x-momenta with different velocities, so the
   wavepacket **spreads**. A linear massive field has no stable localized state.
   *(A stable particle must therefore be a **soliton** — a nonlinearly
   self-trapped mode where the nonlinearity balances dispersion.)*

2. **Saturation does not make a soliton — it makes dispersion worse.** With
   clip/spillover, a small residual (~2%) survives localized exactly at center —
   more than linear — hinting at weak self-trapping. But sweeping the saturation
   depth (amplitude 1 → 32 at fixed bound) the retained fraction **peaks at ~2%
   then falls to 0%**, the **opposite** of a soliton (which would rise and
   converge). Longer runs confirm the residual is a **slowly-decaying transient**
   (final E(n≥1): 23.6 → 12.5 → 11.0 → 10.4 over 600 → 3600 steps), not a
   plateau.

3. **Why:** a saturating / clipping bound **flattens peaks** — it is a
   **defocusing** nonlinearity, the *wrong sign* to make a bright soliton
   (which needs a *focusing*, peak-*enhancing* nonlinearity). Deeper saturation
   spreads the mode faster, so retention drops with amplitude. This is robust and
   general — not an artifact of the excitation choice.

### What this means (non-dogmatically)

- **The value-bound saturation cannot bind a compact mode into a particle by
  self-focusing.** It is defocusing. This is a real structural result, not a
  tuning miss — and it fits the [grid-gravity](../../grid-gravity/) lesson that
  the *value*-bound is the wrong flavour for long-range binding.
- **The indicated path is topological, not amplitude-focused.** The standard way
  to get a stable localized mode without focusing is a **topological soliton** —
  a **winding** of a *phase* that cannot unwind continuously. That is exactly the
  framework's own **charge = winding** ([metric-charge](../../metric-charge/))
  and the **ℵ-line as a compact phase (U(1))**. A particle is a *phase winding*,
  topologically protected — not a self-focused energy blob.
- **The current sim can't test that yet:** its compact dimension carries a **real
  amplitude harmonic** (cos(2πk/nc)), which has **no winding number** and no
  topological protection. Pair production (M2) is likewise a *winding-number
  ±1 creation* event — also invisible to a real scalar field. **Both the trap and
  the pump need the compact field to carry a genuine phase.**
- Saturation's role is thereby **narrowed but not eliminated**: it plausibly
  supplies **quantization** (the bound → integer occupation) and the *nonlinear
  event* that flips winding number, while **topology supplies the binding**.

## M2·B — a second candidate: containment by *discreteness* (probe inconclusive)

A distinct binding mechanism (user hypothesis, and the most GRID-native):
dispersion is *fractional* leakage — each tick a little energy dribbles to
neighbours. If a quantum is an **indivisible '1'** on an edge, the sub-unit
dribble is *forbidden*; the quantum is trapped until it can leave **as a whole
unit, all at once**. This is the lattice-physics of **discrete breathers /
Peierls–Nabarro pinning** — discreteness pins localized modes the continuum
disperses — and it needs **no phase field**, unlike the topological route.

**Crucial fork inside it:** it requires **hard-indivisible** units. A
**sigma-delta / dithered** discrete node (carry the fractional remainder, emit
whole units) *recovers the continuum in the average* — so it would recover
**dispersion** and **not** trap. The hypothesis lives specifically in the
hard-indivisible (non-remainder-carrying) substrate.

**Probe with the crude `--quantize` (hard rounding to {−1,0,+1}): inconclusive
— it breaks the dynamics.** The compact mode showed 67% stable retention (vs 0%
continuous), *perfectly* stable across 800–5000 steps with all loss taken once
during settling — which *looked* like a confirmation. **But the control kills
it:** under the same quantization a **photon also freezes** (speed 0.62 → 0) and
its energy blows up (a −900 "loss" = runaway). So the quantization freezes the
*whole lattice*, not selectively the particle — no selective containment was
shown. Crude rounding is **non-conserving** and fights the fractional-output
scatter, destroying coherent propagation for everything.

**What this establishes:** the hypothesis is **untested, not refuted** — and the
exact construction it needs is now clear: an **integer / whole-unit,
energy-conserving scatter** where **photons still propagate as coherent
unit-packets** while **fractional leakage is forbidden** so compact modes stay
put. That is a genuinely *different* update rule from `(2/N)J−I` + rounding
(which produces half-integers): a **lattice-gas-style** conservative discrete
collision, or grid-quantization's **bit-conserving whole-unit transport**. The
decisive test is the **selective-containment control**: photon propagates *and*
particle traps, under one conserving discrete rule.

## M2·C — the focusing diagnostic, and a tension in "integer edges"

**Focusing diagnostic (does the *right-sign* nonlinearity trap here?): weak.**
Added `--focus` (high-intensity nodes reflect more → Kerr self-trapping, the
opposite sign to clip). Retention peaks at ~1.8% (focus 0.05–0.1), no robust
breather, and it goes non-conserving (energy blow-up) by focus 0.4. So **soft**
nonlinearities of *either* sign (clip, spillover, Kerr focus) all give the same
~2% marginal residual — the lattice's **linear dispersion dominates** at these
scales. Trapping would need a **strong/singular** nonlinearity — i.e. exactly
the **hard-discrete** regime, not a soft term.

**But strict integer edges are in tension with the Maxwell scatter.** The
equal-impedance scatter `out_d = (2/N)T − in_d` is the thing that *gives
Maxwell*, and for N=4 it is `0.5·T − in_d`: with integer inputs the output is
**half-integer whenever T is odd**. So the impedance scatter **does not preserve
integer edges**. More generally, the only *orthogonal* (energy-conserving)
**integer** matrices are **signed permutations** — and `(2/N)J − I` is not one
(it has fractional entries). Therefore:

- **Rounding** the impedance scatter to integers is **non-conserving** — exactly
  what broke the `--quantize` probe (froze the lattice, energy blew up).
- A **sigma-delta** integer node (carry the remainder) is faithful to the
  continuum *on average* → it **recovers dispersion** → does **not** trap.
- A genuinely **integer-conservative** rule (signed-permutation / **lattice-gas**
  collision) exists — but it is a **different dynamics** from the impedance
  scatter (ballistic transport, not partial transmission).

**So "the Maxwell scatter, but with indivisible ±1 edges" is not a consistent
object.** Indivisibility and the impedance scatter pull apart. This is a real
constraint, and it reshapes the options rather than killing the intuition.

## Next steps — a fork (needs a steer)

The M2·A/B/C results converge on a genuine modeling decision:

- **(A) Lattice-gas / indivisible-particle substrate.** Drop partial
  transmission for a conservative integer collision. Indivisible particles;
  a **net-circulating (winding) c-cluster has no x-momentum and no head-on
  pairs to convert it to x-movers → it should stay trapped in x**, while
  x-streams (photons) propagate. Directly tests indivisibility — but it is a
  *different substrate* than the impedance scatter that gives Maxwell.
- **(B) Instantiation split (grid-quantization's own picture).** Keep the
  **continuous** impedance scatter (waves disperse and *interfere*, as they
  must), and put the discreteness in a **separate whole-quantum instantiation**
  overlay — the particle is the **indivisible click**, not a trapped blob. This
  dissolves the "trap a wavepacket" problem (M2·A) and reconnects to **M3/M4**
  (single instantiation; Born rule) and the pilot-wave structure already in the
  README. Indivisibility lives in *instantiation*, not in the field values.
- **(C) Topology.** Phase-winding (U(1) ℵ-line) binding — the M2·A fallback.

## Older next-step list (subsumed by the fork above)

Two candidate binding mechanisms are now on the table — **discreteness** (M2·B)
and **topology** (M2·A). Discreteness is more GRID-native and needs no new field,
so test it first.

1. **Build an integer/whole-unit, energy-conserving discrete scatter** (a
   lattice-gas-style conservative collision, or bit-conserving whole-unit
   transport — *not* `(2/N)J−I` + rounding, which is non-conserving). Run the
   **selective-containment control**: does a **photon still propagate as a
   coherent unit-packet** while a **compact mode stays trapped**? If both hold
   under one conserving rule, discreteness *is* the containment mechanism — and
   it unifies with grid-quantization's substrate.
2. **If discreteness gives no selective containment:** give the compact dimension
   a genuine **phase** (complex / U(1) ℵ-line) and test whether a **unit
   phase-winding** localized in x is **topologically stable** (the M2·A route).
3. **Redefine M2 accordingly:** pair production = a whole-quantum / ±1-winding
   creation event at a saturation collision (net conserved). Test whether the
   nonlinearity can create the trapped pair.
4. Only once a stable trapped particle exists: **momentum & pair check** (zero
   net x-momentum; ±winding = particle/antiparticle).
