"""
Physical and mathematical constants used across studies.

Sources:
  - CODATA 2018 (NIST)
  - Particle Data Group (PDG) 2022 for particle masses
"""

import math

# ── Fundamental constants ─────────────────────────────────────────────────────
h     = 6.62607015e-34        # Planck constant (J·s), exact post-2019
hbar  = h / (2 * math.pi)    # reduced Planck constant (J·s)
c     = 299_792_458           # speed of light (m/s), exact
eps0  = 8.8541878128e-12      # vacuum permittivity (F/m)
mu0   = 1 / (eps0 * c**2)    # vacuum permeability (H/m)
e     = 1.602176634e-19       # elementary charge (C), exact post-2019
G     = 6.67430e-11              # gravitational constant (m³/(kg·s²))
alpha = 7.2973525693e-3       # fine-structure constant (dimensionless)
k_B   = 1.380649e-23          # Boltzmann constant (J/K), exact

# ── Particle masses ───────────────────────────────────────────────────────────
m_e   = 9.1093837015e-31      # electron mass (kg)
m_mu  = 1.883531627e-28       # muon mass (kg)
m_tau = 3.16754e-27            # tau mass (kg)

# ── Derived scales ────────────────────────────────────────────────────────────
lambda_C = h / (m_e * c)                    # electron Compton wavelength (m)
r_bar    = lambda_C / (4 * math.pi)         # WvM toroid transport radius (m)
l_P      = math.sqrt(hbar * G / c**3)             # Planck length (m), ~1.616e-35

# ── Mathematical constants ────────────────────────────────────────────────────
phi = (1 + math.sqrt(5)) / 2   # golden ratio ≈ 1.618034
