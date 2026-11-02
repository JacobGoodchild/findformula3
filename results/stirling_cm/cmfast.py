"""Fast double-precision determination of the real CM degree: hp = F^{(q+1)} tabulated by piecewise Chebyshev interpolation (built from 30-digit mpmath),
then H(a,t) = t^a * int_0^t (t-u)^{-a} hp(u) du with scipy QUADPACK 'alg' weights, minimised over t, bisection in a."""
import sys, time
import numpy as np
from numpy.polynomial import chebyshev as C
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from mpmath import mp, mpf
from cmdeg import make_h
mp.dps = 40
class Cheb:
    def __init__(self, f, edges, deg=140):
        self.edges = edges; self.pieces = []
        for lo, hi in zip(edges[:-1], edges[1:]):
            k = np.arange(deg+1)
            x = np.cos(np.pi*(k + 0.5)/(deg+1))           # Chebyshev nodes in [-1,1]
            ts = 0.5*(hi-lo)*x + 0.5*(hi+lo)
            ys = [float(f(mpf(float(t)))) for t in ts]
            self.pieces.append((lo, hi, C.chebfit(x, ys, deg)))
    def __call__(self, t):
        for lo, hi, c in self.pieces:
            if t <= hi:
                return C.chebval((2*t - (lo+hi))/(hi-lo), c)
        lo, hi, c = self.pieces[-1]
        return C.chebval((2*t - (lo+hi))/(hi-lo), c)
def build(n, m, Tmax=None):
    q = 2*n + m - 2
    hp = make_h(n, m, q+1)
    Tmax = Tmax or 60.0*n
    edges = [0.0, 1.0, 3.0, 6.0, 12.0, 24.0, Tmax] if Tmax > 24 else [0.0, 1.0, 3.0, 6.0, Tmax]
    return Cheb(hp, edges), q, Tmax
def H(hpf, a, t):
    v, err = quad(hpf, 0, t, weight='alg', wvar=(0, -a), limit=200, epsabs=1e-16, epsrel=1e-13)
    return t**a * v
def minH(hpf, a, T0, T1):
    ts = np.linspace(T0, T1, 61)
    vals = [H(hpf, a, t) for t in ts]
    i = int(np.argmin(vals))
    res = minimize_scalar(lambda t: H(hpf, a, t), bounds=(ts[max(i-1, 0)], ts[min(i+1, 60)]), method='bounded', options={'xatol': 1e-9})
    return res.fun, res.x
def crit(n, m, T0=2.0, T1=None, tol=1e-11):
    hpf, q, Tmax = build(n, m)
    T1 = T1 or Tmax*0.6
    lo, hi = 0.3, 0.999
    f_lo = minH(hpf, lo, T0, T1)[0]; f_hi = minH(hpf, hi, T0, T1)[0]
    assert f_lo > 0 and f_hi < 0, (f_lo, f_hi)
    while hi - lo > tol:
        mid = 0.5*(lo+hi); v, t = minH(hpf, mid, T0, T1)
        if v > 0: lo = mid
        else: hi = mid
    return q, 0.5*(lo+hi), t
if __name__ == "__main__":
    for n, m in [(2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (4, 1)]:
        t0 = time.time(); q, a, t = crit(n, m)
        print("n=%d m=%d: d_CM = %d + %.10f = %.10f   (critical t=%.4f) [%.0fs]" % (n, m, q, a, q + a, t, time.time()-t0), flush=True)
