"""Gr(l) for LARGE l from the exact integral representation  (-1)^{n-1} G_n^{(l)} = int_0^inf h(e^L) f_n(e^L) e^L dL  (n real allowed).
The last sign change n*(l) of n -> J(n) (n real) satisfies Gr(l) = floor(n*)+1 (checked against the exact values l<=14)."""
import sys
from mpmath import mp, mpf, mpc, quad, log, pi, exp, cot, im, findroot
mp.dps = 50
def Hval(L, ell):
    return (-1)**(ell-1)*im(mpc(L, pi)**ell)/(pi*(L*L+pi*pi)**ell)
def J(n, ell, pts):
    def f(L):
        z = exp(L)
        fn = (1 - (-1)**ell*z**(n-ell-1))/(z+1)**(n-ell+1)
        return Hval(L, ell)*fn*z
    return quad(f, pts)
def breakpoints(n, ell):
    r = [pi*cot(k*pi/ell) for k in range(1, ell)]             # zeros of h in L, decreasing in k
    r = sorted([x for x in r if x > 0])
    top = log(n) + 40
    pts = [mpf(0)] + r + [log(n) - 2, log(n), log(n) + 2, log(n) + 5, log(n) + 12, top]
    return sorted(set(p for p in pts if p >= 0))
def sign_change(ell, lo, hi, iters=60):
    """bisection in log n for the LAST sign change: assumes J(lo)<0<J(hi)"""
    a, b = log(mpf(lo)), log(mpf(hi))
    for _ in range(iters):
        m = (a+b)/2; n = exp(m)
        if J(n, ell, breakpoints(n, ell)) > 0: b = m
        else: a = m
    return exp((a+b)/2)
if __name__ == "__main__":
    known = {5: 113, 6: 346, 7: 1030, 8: 2995, 9: 8580, 10: 24303, 11: 68283, 12: 190698, 13: 530152, 14: 1468691}
    for ell in [int(a) for a in sys.argv[1:]]:
        r = exp(pi*cot(pi/ell))
        lo, hi = 0.8*r, 3*r
        # make sure lo is negative side, hi positive side
        nlo = J(mpf(lo), ell, breakpoints(mpf(lo), ell)); nhi = J(mpf(hi), ell, breakpoints(mpf(hi), ell))
        ns = sign_change(ell, lo, hi)
        print("l=%d : n* = %s ; r = %s ; n*/r = %s %s" % (ell, mp.nstr(ns, 14), mp.nstr(r, 10), mp.nstr(ns/r, 10), ("; exact Gr = %d" % known[ell]) if ell in known else ""), flush=True)
