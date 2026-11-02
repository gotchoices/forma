"""Is the wye-width near-fit special to the charged-lepton masses?

Fits only the two segment lengths of the neutrino circle (junction_fit model,
flips off, point flavors) for the lepton-mass widths and for 20 random width
sets spanning the same total range (log-uniform), and prints each loss.
Run from the repository root.  Output: printed losses.
"""
import sys; sys.path.insert(0, 'projects/sheet-neutrino/scripts')
import numpy as np, junction_fit as jf
from scipy.optimize import minimize
class A: pass
a=A(); a.phases=False; a.flips=False; a.kmax=4; a.n_grid=1200; a.n_per_seg=120; a.flavor="point"; a.ratio_weight=.3; a.s23=.5; a.junction="free"
def fit(w):
    r=np.array([(w[i-1]-w[i])/(w[i-1]+w[i]) for i in range(3)])
    X=lambda p: np.concatenate([[p[0],p[1]],np.arctanh(np.clip(r,-.999999,.999999))])
    f=lambda p: jf.evaluate(X(p),a)[0]
    rng=np.random.default_rng(1)
    return min(minimize(f,rng.uniform(.2,2.5,2),method="Nelder-Mead",options=dict(maxiter=300)).fun for _ in range(6))
print("lepton-mass widths (e,tau,mu):", f"{fit(np.array([2426.0,0.6977,11.73])):.2e}", flush=True)
rng=np.random.default_rng(42)
for i in range(20):
    lw=np.sort(rng.uniform(0,np.log(3477),2)); w=np.exp(np.array([0.0,lw[0],lw[1]]))   # span up to the same total range
    w=rng.permutation(w)
    print(f"random widths {np.round(w,2)}: loss {fit(w):.2e}", flush=True)
