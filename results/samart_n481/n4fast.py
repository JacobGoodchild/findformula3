"""n_4(81) via Clausen: 3F2(1/4,1/2,3/4;1,1;z) = 2F1(1/8,3/8;1;z)^2 ;  n_4(s) = n_4(256) - int_s^256 Re[2F1(1/8,3/8;1;256/t + i0)^2] dt/t."""
import sys, time
from mpmath import mp, mpf, mpc, hyp2f1, quad, re, log, nsum, factorial, inf
mp.dps = int(sys.argv[1]) if len(sys.argv) > 1 else 40
def F(z):
    return hyp2f1(mpf(1)/8, mpf(3)/8, 1, mpc(z, mpf(10)**(-mp.dps-5)))**2
def n4_256():
    a = lambda n: factorial(4*n)/(factorial(n)**4*n*mpf(256)**n)
    return log(256) - nsum(a, [1, inf], method='r+s+e')
t0 = time.time()
base = n4_256()
f = lambda t: re(F(256/t))/t
for s in (81, 300, 648):
    s = mpf(s)
    if s < 256: val = base - quad(f, [s, 256])
    else: val = base + quad(f, [256, s])
    print("n_4(%s) = %s  [%.0fs]" % (s, mp.nstr(val, mp.dps-5), time.time()-t0), flush=True)
