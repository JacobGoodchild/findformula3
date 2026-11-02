"""Check the integral representation used in the proof of Thm 5.1 of arXiv:2609.11072:
   (-1)^{n-1} G_n^{(l)} = int_1^infty h(z) f_n(z) dz,  h(z) = (-pi)^{l-1} H_l(log(z)/pi) (log^2 z + pi^2)^{-l} [= the explicit sum below],  f_n(z) = (1 - (-1)^l z^{n-l-1})/(z+1)^{n-l+1}   (n > l+3?)"""
import sys
from mpmath import mp, mpf, quad, log, pi, binomial, exp
from gr import coeffs
mp.dps = 40
def h(z, ell):
    L = log(z); s = mpf(0)
    for k in range(1, (ell+1)//2 + 1):
        s += (-1)**k * binomial(ell, 2*k-1) * L**(ell-2*k+1) * pi**(2*k-2)
    return (-1)**ell * s * (L**2 + pi**2)**(-ell)
def fn(z, n, ell):
    return (1 - (-1)**ell * z**(n-ell-1))/(z+1)**(n-ell+1)
def J(n, ell):
    # integrate over L=log z in (0,inf): dz = e^L dL
    f = lambda L: h(exp(L), ell)*fn(exp(L), n, ell)*exp(L)
    return quad(f, [0, 1, 3, 10, 30, 100, 400])
if __name__ == "__main__":
    ell = int(sys.argv[1])
    c = coeffs(ell, 60, 256)
    for n in (ell+4, ell+8, 20, 30, 50):
        g = (-1)**(n-1)*mpf(c[n].mid().str(40, radius=False))
        j = J(n, ell)
        print("ell=%d n=%d : (-1)^(n-1) G_n = %s ; integral = %s ; ratio = %s" % (ell, n, mp.nstr(g, 12), mp.nstr(j, 12), mp.nstr(j/g, 8)))
