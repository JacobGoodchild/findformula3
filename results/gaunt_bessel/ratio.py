"""Gaunt's Open Problem 2.10 (solved with an unspecified constant in arXiv:2605.20983): R_{nu,gamma}(x) = int_0^x e^{-gamma t} I_nu(t) t^{-nu} dt / ( e^{-gamma x} I_{nu+1}(x) x^{-nu} ).
Limits: x->0: 2(nu+1); x->infinity: 1/(1-gamma).  Question tested here: is sup_x R = max{2(nu+1), 1/(1-gamma)} (best constant)?"""
import numpy as np
from scipy.special import ive, iv
from scipy.integrate import quad
def R(x, nu, g):
    # use scaled Bessel: e^{-gamma t} I_nu(t) = e^{-(gamma-1) t}... ive(nu,t)=I_nu(t) e^{-t}  =>  e^{-gamma t}I_nu(t) = ive(nu,t) e^{(1-gamma)t}
    f = lambda t: ive(nu, t)*np.exp((1-g)*t)*t**(-nu)
    num, _ = quad(f, 0, x, limit=500, epsabs=0, epsrel=1e-12)
    den = ive(nu+1, x)*np.exp((1-g)*x)*x**(-nu)
    return num/den
if __name__ == "__main__":
    worst = 0
    for nu in [-0.4, -0.2, 0.0, 0.5, 1.0, 2.0, 5.0]:
        for g in [0.05, 0.2, 0.5, 0.8, 0.95, 0.99]:
            xs = np.concatenate([np.logspace(-3, 2.3, 120)])
            vals = np.array([R(x, nu, g) for x in xs])
            lim0 = 2*(nu+1); liminf = 1/(1-g)
            sup = vals.max()
            cand = max(lim0, liminf)
            print("nu=%5.2f gamma=%4.2f : sup_x R = %.6f at x=%.3g ; max(2(nu+1),1/(1-gamma)) = %.6f %s" % (nu, g, sup, xs[vals.argmax()], cand, "" if sup <= cand*(1+1e-9) else "  <-- EXCEEDS"))
