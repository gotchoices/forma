"""
Williamson–van der Mark model: derived quantities and utilities.

Based on: J.G. Williamson & M.B. van der Mark,
"Is the electron a photon with toroidal topology?",
Annales de la Fondation Louis de Broglie, Vol. 22 No. 2, 1997.
"""

import math
from . import constants as C


def wvm_charge():
    """WvM Eq. 5:  q = (1/2π) √(3 ε₀ ℏ c).  Returns charge in Coulombs."""
    return (1 / (2 * math.pi)) * math.sqrt(3 * C.eps0 * C.hbar * C.c)


def wvm_charge_ratio():
    """
    Analytic q/e ratio.

    From q = (1/2π)√(3ε₀ℏc)  and  e = √(4πε₀ℏcα):
        q/e = √3 / (4π √(πα))
    """
    return math.sqrt(3) / (4 * math.pi * math.sqrt(math.pi * C.alpha))


# Pre-computed for convenience
q_over_e = wvm_charge_ratio()
S_TARGET = 1 / q_over_e   # correction factor needed: e/q ≈ 1.0985
