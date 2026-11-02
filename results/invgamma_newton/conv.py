import sys, time
from mpmath import mp, mpf, log, gamma, findroot
import newton
mp.dps = 600
N = int(sys.argv[1])
t0 = time.time()
s, a = newton.newton_coeffs(N)
print("coefficients computed [%.0fs]" % (time.time()-t0), flush=True)
def inv(x):
    x = mpf(x)
    # solve Gamma(t) = x for t>1.4616 by bisection-safeguarded secant
    lo, hi = mpf('1.4616321449683623412626595423257213284682'), mpf(60)
    for _ in range(300):
        mid = (lo+hi)/2
        if gamma(mid) < x: lo = mid
        else: hi = mid
    return (lo+hi)/2
for x in sys.argv[2:]:
    xx = mpf(x); true = inv(xx)
    part = newton.newton_eval(xx, s, a, N)
    errs = [(n, abs(part[n]-true)) for n in (25, 50, 100, 200, N) if n <= N]
    print("x=%s true=%s  errors: %s" % (x, mp.nstr(true, 10), ["n=%d: %s" % (n, mp.nstr(e, 3)) for n, e in errs]), flush=True)
