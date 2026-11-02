"""n_4(s) = 4 m(x^4+y^4+z^4+1+s^{1/4} x y z) (Mahler measure), s>256: n_4(s) = log s - sum_{n>=1} (4n)!/((n!)^4 n) s^{-n}.
s n_4'(s) = 3F2(1/4,1/2,3/4;1,1;256/s) (analytic continuation to z=256/s>1, take real part).
n_4(81) = n_4(256) - int_{81}^{256} Re 3F2(1/4,1/2,3/4;1,1;256/s) ds / s."""
import sys
from mpmath import mp, mpf, hyp3f2, quad, log, nsum, factorial, inf, re
mp.dps = 30
def n4_at_256():
    # n_4(256) = log 256 - sum_n (4n)!/((n!)^4 n 256^n);  terms ~ n^{-5/2}: use Richardson via nsum
    a = lambda n: factorial(4*n)/(factorial(n)**4*n*mpf(256)**n)
    s = nsum(a, [1, inf], method='r+s+e')
    return log(256) - s
def n4(s):
    s = mpf(s)
    if s >= 256:
        return log(s) - nsum(lambda n: factorial(4*n)/(factorial(n)**4*n*s**n), [1, inf])
    f = lambda t: re(hyp3f2(mpf(1)/4, mpf(1)/2, mpf(3)/4, 1, 1, 256/t))/t
    return n4_at_256() - quad(f, [s, 256])
if __name__ == "__main__":
    print("n_4(256) =", mp.nstr(n4_at_256(), 30))
    print("n_4(81)  =", mp.nstr(n4(81), 30))
    # sanity: continuity at 300 using both formulas
    print("n_4(300) series:", mp.nstr(n4(300), 25))
    f = lambda t: re(hyp3f2(mpf(1)/4, mpf(1)/2, mpf(3)/4, 1, 1, 256/t))/t
    print("n_4(300) via integral from 256:", mp.nstr(n4_at_256() + quad(f, [256, 300]), 25))
