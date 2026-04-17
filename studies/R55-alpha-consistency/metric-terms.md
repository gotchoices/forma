# R55 Metric Terms — 10×10 Reference (with ℵ dimension)

Model-E geometry extended with the ℵ (aleph) dimension
mediating Ma-S coupling.

## Hypothesis F parameters

The coupling direction (which side carries α) is symmetric in
the Schur complement — only the product σ_Ma × σ_ℵS matters
for universality (F19).  The physical picture (α lives in
the Ma→ℵ bending) is correct but the metric can't distinguish.

Two representative parameter choices:

| Version | σ_Ma (Ma-ℵ) | σ_ℵS (ℵ-S) | Product | Spectrum shift | Gap |
|---------|-------------|-------------|---------|---------------|-----|
| **Minimal shift** | 0.01 | 0.574 | 0.00574 | 0.4% | 3.7% |
| Balanced (1/2π) | 0.159 | 0.290 | 0.0462 | 1.4% | 3.6% |

The minimal-shift version is preferred for numerical work
(smallest perturbation to the particle spectrum).

| Parameter | Minimal-shift value | Source |
|-----------|-------------------|--------|
| Ma-ℵ ring coupling | ±0.01 | Small — α physics is here |
| σℵS | 0.574 | Large — direct capture |
| Effective Ma-S product | ±0.00574 | |
| √α | 0.0854 | For reference |

## Dimension assignments

| Index | Name | Type | L (fm) | G̃ diagonal | Role |
|-------|------|------|--------|------------|------|
| 0 | e-tube | Ma compact | 4,718 | 1.000 | Electron tube (charge n₁) |
| 1 | e-ring | Ma compact | 11.88 | 633,324 | Electron ring (generations) |
| 2 | ν-tube | Ma compact | 2.12×10¹¹ | 1.000 | Neutrino tube |
| 3 | ν-ring | Ma compact | 4.24×10¹⁰ | 1.012 | Neutrino ring (oscillation) |
| 4 | p-tube | Ma compact | 2.45 | 1.000 | Proton tube (charge n₅) |
| 5 | p-ring | Ma compact | 4.45 | 1.008 | Proton ring (generations) |
| 6 | ℵ | Internal | L_P | 1.000 | Aleph: sub-Planck edge dimension |
| 7 | S_x | Spatial | — | 1.000 | Space (flat) |
| 8 | S_y | Spatial | — | 1.000 | Space (flat) |
| 9 | S_z | Spatial | — | 1.000 | Space (flat) |

## Visual layout (10×10)

```
              e-tube  e-ring  ν-tube  ν-ring  p-tube  p-ring    ℵ      Sx     Sy     Sz
           ┌────────┬────────┬────────┬────────┬────────┬────────┬────────┬──────┬──────┬──────┐
  e-tube   │  1.000 │ 795.82 │   0    │   0    │   0    │   0    │   0    │  0   │  0   │  0   │
           │  diag  │ GEN    │ inact  │ inact  │ inact  │ inact  │ inact  │  —   │  —   │  —   │
           ├────────┼────────┼────────┼────────┼────────┼────────┼────────┼──────┼──────┼──────┤
  e-ring   │        │ 633324 │ OPEN   │ OPEN   │ NEUTR  │ NEUTR  │-0.1592 │  0   │  0   │  0   │
           │        │  diag  │        │        │        │        │ Ma-ℵ   │  —   │  —   │  —   │
           ├────────┼────────┼────────┼────────┼────────┼────────┼────────┼──────┼──────┼──────┤
  ν-tube   │        │        │  1.000 │ +0.110 │   0    │   0    │   0    │  0   │  0   │  0   │
           │        │        │  diag  │ GEN    │ inact  │ inact  │ inact  │  —   │  —   │  —   │
           ├────────┼────────┼────────┼────────┼────────┼────────┼────────┼──────┼──────┼──────┤
  ν-ring   │        │        │        │  1.012 │ -0.180 │ +0.100 │+0.1592 │  0   │  0   │  0   │
           │        │        │        │  diag  │ NEUTR  │ NEUTR  │ Ma-ℵ   │  —   │  —   │  —   │
           ├────────┼────────┼────────┼────────┼────────┼────────┼────────┼──────┼──────┼──────┤
  p-tube   │        │        │        │        │  1.000 │ +0.089 │   0    │  0   │  0   │  0   │
           │        │        │        │        │  diag  │ GEN+α  │ inact  │  —   │  —   │  —   │
           ├────────┼────────┼────────┼────────┼────────┼────────┼────────┼──────┼──────┼──────┤
  p-ring   │        │        │        │        │        │  1.008 │+0.1592 │  0   │  0   │  0   │
           │        │        │        │        │        │  diag  │ Ma-ℵ   │  —   │  —   │  —   │
           ├────────┼────────┼────────┼────────┼────────┼────────┼────────┼──────┼──────┼──────┤
    ℵ      │        │        │        │        │        │        │  1.000 │+0.290│+0.290│+0.290│
           │        │        │        │        │        │        │  diag  │ ℵ-S  │ ℵ-S  │ ℵ-S  │
           ├────────┼────────┼────────┼────────┼────────┼────────┼────────┼──────┼──────┼──────┤
  Sx       │        │        │        │        │        │        │        │ 1.00 │  0   │  0   │
           │        │        │        │        │        │        │        │ flat │      │      │
           ├────────┼────────┼────────┼────────┼────────┼────────┼────────┼──────┼──────┼──────┤
  Sy       │        │        │        │        │        │        │        │      │ 1.00 │  0   │
           │        │        │        │        │        │        │        │      │ flat │      │
           ├────────┼────────┼────────┼────────┼────────┼────────┼────────┼──────┼──────┼──────┤
  Sz       │        │        │        │        │        │        │        │      │      │ 1.00 │
           │        │        │        │        │        │        │        │      │      │ flat │
           └────────┴────────┴────────┴────────┴────────┴────────┴────────┴──────┴──────┴──────┘
```

## Entry summary

| Category | Count | Values | Status |
|----------|------:|--------|--------|
| Diagonal (Ma) | 6 | From model-E | Known |
| Diagonal (ℵ) | 1 | 1.000 | Set (Planck/angular) |
| Diagonal (S) | 3 | 1.000 | Set (flat space) |
| In-sheet shears | 3 | s_e, s_ν, s_p | Known (model-E) |
| Cross-sheet (Ma-Ma) | 6 active | σ₂₃...σ₄₆ | 2 known, 4 open |
| Ma-ℵ | 3 active | ±1/(2π) on rings | Set (angular coord) |
| ℵ-S | 1 effective | 0.2902 | Tuned to α |
| Ma-S | 0 | All zero | Coupling goes through ℵ |
| S-S | 0 | All zero | Flat space |
| **Total entries** | **55** | | |
| **Free parameters** | 5 | 4 model-E + σℵS | |

## Key results

- **Universality:** electron and proton couple at the same α
  to within 3.6%.  All nuclei (deuteron through iron) get
  identical α.

- **Spectrum shift:** ~1.3% for p-sheet modes, ~1.4% for e-sheet.
  Compensable by re-tuning ε_p and ε_e slightly.

- **Neutrino coupling:** nonzero at 1.07α.  The ν-sheet
  couples through ℵ even though it carries no charge.

- **Ma-S = 0:** No direct Ma-to-S coupling in the metric.
  All coupling is mediated by ℵ.

## Physical interpretation

The ℵ-line on each lattice edge is the mechanism by which
bending of the 2D Ma surface produces electromagnetic coupling
to 3D space (sim-impedance Tracks 8-12).  The ring dimensions
of each sheet connect to ℵ at 1/(2π) per radian of angular
coordinate.  The ℵ-line then connects to S at strength σℵS.

The coupling is universal because ℵ is the same at every
lattice node — it doesn't depend on which sheet, which mode,
or which particle.  The 3.6% non-universality between e-sheet
and p-sheet comes from the different internal shears affecting
the Schur complement when ℵ is integrated out.
