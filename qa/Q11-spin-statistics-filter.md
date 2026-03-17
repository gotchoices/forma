# Q11: Why are only winding numbers q = 1 and q = 2 physical?

**Status:** Answered  
**Source:** [`knot-zoo/findings.md`](../studies/knot-zoo/findings.md) F1  
**Related:** [Q13](Q13-three-compact-dimensions.md), [Q26](Q26-hadrons-photon-knots.md)

**Short answer:** The spin-statistics theorem requires particles to have
integer or half-integer spin. A (p, q) torus knot produces spin s = p/q.
Only q = 1 (integer spin, bosons) and q = 2 (half-integer spin, fermions)
are consistent with quantum mechanics. All higher q give non-standard
spin values that are excluded.

---

## Question

The knot-zoo study (R3/S3) found that only the (1,2) winding produces
a nonzero charge matching the electron. But the question is more general:
is there a physical principle that eliminates torus knots with q ≥ 3,
or is the restriction purely numerical?

## Answer

**Spin from winding ratio.** A photon traversing p loops of the major
circle for every q loops of the minor circle traces a (p, q) torus knot.
The angular momentum of this configuration, projected onto the symmetry
axis, is proportional to p/q. In units of ℏ, the spin of the resulting
particle is:

    s = p / q

**Spin-statistics constraint.** Quantum mechanics (more precisely, the
spin-statistics theorem) requires all particles to have spin that is an
integer or half-integer multiple of ℏ:

    s ∈ { 0, 1/2, 1, 3/2, 2, … }

This means p/q must be a ratio with denominator 1 or 2.

- **q = 1:** s = p/1 = p (integer spin). These are bosons. The photon
  itself (p = 1, q = 1) is the simplest case.
- **q = 2:** s = p/2 (half-integer for odd p). The electron is
  p = 1, q = 2 → s = 1/2.
- **q = 3:** s = p/3. For p not divisible by 3 this is non-integer,
  non-half-integer. No known fundamental particle has such spin. Excluded.
- **q ≥ 3 generally:** Unless p/q reduces to a fraction with denominator
  1 or 2, the spin is non-standard. Reduced fractions with q ≥ 3 are
  excluded.

**Fractional charges from higher q.** The knot-zoo study also found
that (p, 3) knots produce charges e/3 and 2e/3 — the quark charges. If
three such photons are Borromean-linked on T³ (see Q26, R14), they form
a baryon and their charges sum to e. The q = 3 exclusion applies to
*free* particles; confined quarks are not free particles.

**q = 0 is unphysical.** Zero winding on the minor circle means the
"photon" travels only along the major circle — a closed loop with no
minor winding, which corresponds to q = 0. The charge formula from S2
gives q/e → ∞ as q_winding → 0, i.e., no finite charge. The neutrino
(zero charge, spin 1/2) requires a separate topology discussion (see Q14
in INBOX).

## Summary

| Winding q | Spin | Status |
|-----------|------|--------|
| 1 | p (integer) | Allowed — bosons |
| 2 | p/2 (half-integer for odd p) | Allowed — fermions |
| 3 | p/3 | Excluded as free particles; confined quarks only |
| ≥ 4 | non-standard (generally) | Excluded |

The spin-statistics theorem acts as a hard filter: only q = 1 and q = 2
produce particles that quantum mechanics allows to exist as free states.
