"""Rigorous (interval) check of positivity of the first N Taylor coefficients of 1/q_{k,m} for the diagonal k=m, odd m."""
import sys, time
from math import comb, factorial
from flint import arb, arb_series, ctx, fmpq
def check(k, m, N, prec):
    ctx.prec = prec; ctx.cap = N+1
    q = [arb(fmpq((-1)**j * comb(m, j) * factorial(k+m-j), factorial(k+m))) for j in range(m+1)]
    inv = arb_series(q).inv().coeffs()
    neg = [n for n in range(N+1) if not inv[n].lower() > 0]
    return neg
if __name__ == "__main__":
    lo, hi, N, prec = map(int, sys.argv[1:5])
    for m in range(lo, hi+1, 2):
        t = time.time()
        neg = check(m, m, N, prec)
        print("m=%d (k=m) N=%d: %s [%.1fs]" % (m, N, "all %d coefficients certified positive" % (N+1) if not neg else "NOT certified positive at n=%s" % neg[:5], time.time()-t), flush=True)
