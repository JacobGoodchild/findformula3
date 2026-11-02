"""S_{k_n} for the alpha-convex Koebe function k_n(z) = [ n int_0^z xi^{n-1} (1-xi)^{-2n} dxi ]^{1/n}  (alpha = 1/n); Bravo-Carrasco-Hernandez-Venegas, arXiv:2606.21574, Sec. on Schwarzian norm.
 G(z) = int_0^z xi^{n-1}(1-xi)^{-2n} dxi * n? In the paper G(z) = B(z; n, 1-2n) (incomplete beta), f = (n G)^{1/n}.
 Formula (22):  S_f = S_G + ((1-alpha^2)/2) (G'/G)^2  with alpha = 1/n.  G' = z^{n-1}(1-z)^{-2n}."""
import numpy as np, sys
from mpmath import mp, mpf, mpc, betainc, quad
def Gfun(z, n):
    return quad(lambda t: (z*t)**(n-1)*(1-z*t)**(-2*n)*z, [0, 1])
def schw_norm_point(z, n):
    # S_G = (G''/G')' - (1/2)(G''/G')^2 with G' = z^{n-1}(1-z)^{-2n}: G''/G' = (n-1)/z + 2n/(1-z)
    p = (n-1)/z + 2*n/(1-z)
    dp = -(n-1)/z**2 + 2*n/(1-z)**2
    SG = dp - p*p/2
    G = Gfun(z, n); Gp = z**(n-1)*(1-z)**(-2*n)
    al = mpf(1)/n
    S = SG + (1-al**2)/2*(Gp/G)**2
    return S
if __name__ == "__main__":
    mp.dps = 25
    n = int(sys.argv[1])
    best = (0, None)
    for r in [0.05, 0.3, 0.6, 0.8, 0.9, 0.95, 0.99, 0.999]:
        for th in np.linspace(0, np.pi, 25):
            z = mpc(r*np.cos(th), r*np.sin(th))
            v = abs(schw_norm_point(z, n))*(1-abs(z)**2)**2
            if v > best[0]: best = (v, (r, th))
    print("n=%d: max sampled %.8f at r,theta=%s ; conj 2(3-1/n)(1-1/n)=%.8f ; S(0)-value 6n(n-1)/((n+1)(n+2))=%.8f" % (n, best[0], best[1], 2*(3-1/n)*(1-1/n), 6*n*(n-1)/((n+1)*(n+2))))
