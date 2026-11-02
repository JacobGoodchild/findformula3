"""For each odd m find the smallest k such that some c_n(k,m) < 0 (n <= 6k+200), i.e. the smallest counterexample to the Fasi-Higham conjecture with that m."""
import sys, time
from math import comb, factorial
from flint import arb, arb_series, ctx, fmpq
def neg_indices(k, m, N, prec=1024):
    while True:
        ctx.prec = prec; ctx.cap = N+1
        q = [arb(fmpq((-1)**j * comb(m, j) * factorial(k+m-j), factorial(k+m))) for j in range(m+1)]
        inv = arb_series(q).inv().coeffs()
        neg = [n for n in range(N+1) if inv[n].upper() < 0]
        unc = [n for n in range(N+1) if not (inv[n].lower() > 0 or inv[n].upper() < 0)]
        if not unc or prec >= 2**16: return neg, unc
        prec *= 2
if __name__ == "__main__":
    for m in range(int(sys.argv[1]), int(sys.argv[2])+1, 2):
        t = time.time(); found = None
        for k in range(0, int(sys.argv[3])+1):
            neg, unc = neg_indices(k, m, 6*k+200)
            if unc: print("  (uncertified at k=%d m=%d)" % (k, m))
            if neg: found = (k, neg[0], len(neg)); break
        print("m=%d: smallest k with a negative coefficient = %s [%.1fs]" % (m, found, time.time()-t), flush=True)
