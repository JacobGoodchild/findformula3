"""Phi(z) = S_{k_n}(z) (1-z^2)^2 is holomorphic in the disc and |S|(1-|z|^2)^2 <= |Phi|; by the maximum principle sup_D |Phi| is attained on the circle. Check |Phi(e^{i theta})| <= L_n = 2(3-1/n)(1-1/n)."""
import numpy as np, sys
from mpmath import mp, mpf, mpc, quad, exp, pi
mp.dps = 30
def Phi(z, n):
    # G(z) = int_0^z xi^{n-1} (1-xi)^{-2n} dxi  (path: straight segment; for |z|=1, z != 1 integrand integrable)
    G = quad(lambda t: (z*t)**(n-1)*(1-z*t)**(-2*n)*z, [0, mpf(1)/2, 1])
    p = (n-1)/z + 2*n/(1-z); dp = -(n-1)/z**2 + 2*n/(1-z)**2
    SG = dp - p*p/2
    Gp = z**(n-1)*(1-z)**(-2*n)
    al = mpf(1)/n
    S = SG + (1-al**2)/2*(Gp/G)**2
    return S*(1-z**2)**2
if __name__ == "__main__":
    for n in [2, 3, 4, 6, 10, 20]:
        L = 2*(3-1.0/n)*(1-1.0/n)
        vals = []
        for th in np.concatenate([np.linspace(0.02, 3.1, 40), [3.14159]]):
            z = mpc(np.cos(th), np.sin(th))
            vals.append((float(abs(Phi(z, n))), th))
        m = max(vals)
        print("n=%d  L_n=%.6f   max_theta |Phi(e^{i theta})| = %.6f at theta=%.3f (values at theta=0.02,0.5,1,2,3: %s)" % (n, L, m[0], m[1], [round(v[0], 4) for v in (vals[0], vals[8], vals[16], vals[26], vals[38])]))
