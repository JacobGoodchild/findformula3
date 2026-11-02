"""Half-iterate T(b,1/2) = f^{[1/2]}(1) of f(x) = b^x for 1 < b < e^{1/e}, via regular (Koenigs) iteration at the attracting fixed point L:
psi(x) = lim_n (f^n(x) - L)/lambda^n,  lambda = L ln b,  f^{[t]}(x) = psi^{-1}(lambda^t psi(x)).   S. Finch, arXiv:2509.24918 asks for T(4/3,1/2), T(5/4,1/2), T(6/5,1/2)."""
import sys
from mpmath import mp, mpf, log, exp, findroot, e, sqrt
mp.dps = 120
def fixed_point(b):
    # attracting fixed point = smaller root of b^L = L  (L < e)
    return findroot(lambda L: b**L - L, (mpf(1), mpf('1.2')), solver='secant', tol=mpf(10)**-70)
def half(b, nit=None):
    b = mpf(b)
    L = fixed_point(b)
    lam = L*log(b)
    n = nit or int(50.0/(-float(log(lam, 10)))) + 5      # lambda^n ~ 1e-50; precision 120 digits leaves ~70 digits in psi
    f = lambda x: b**x
    def psi(x, n=n):
        y = x
        for _ in range(n): y = f(y)
        return (y - L)/lam**n
    p1 = psi(mpf(1))
    target = sqrt(lam)*p1
    # solve psi(y) = target; psi is smooth and increasing near L; y in (1, b)
    y = findroot(lambda y: psi(y) - target, (mpf(1) + (b-1)/2, mpf(1) + (b-1)/2*1.1), solver='secant', tol=mpf(10)**-55)
    return L, lam, y, psi
if __name__ == "__main__":
    for b in ['4/3', '5/4', '6/5']:
        num, den = map(int, b.split('/'))
        L, lam, y, psi = half(mpf(num)/den)
        bb = mpf(num)/den
        # check: applying the half-iterate twice gives f(1)=b  (psi(y2) = lam*psi(1))
        res = psi(y) - sqrt(lam)*psi(mpf(1))
        print("T(%s,1/2) = %s   (fixed point L=%s, lambda=%s, |psi(y)-sqrt(lam)psi(1)|=%s)" % (b, mp.nstr(y, 40), mp.nstr(L, 12), mp.nstr(lam, 12), mp.nstr(abs(res), 3)))
