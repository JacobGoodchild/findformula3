"""Fasi-Higham positivity conjecture (arXiv 2610.39051, Conjecture 1): for odd m, all Taylor coefficients c_n of 1/q_{k,m}(z) are positive,
q_{k,m}(z) = sum_{j=0}^m (-1)^j binom(m,j) (k+m-j)!/(k+m)! z^j.   Diagonal case k=m (open in the paper).  Exact rational recursion."""
import sys, time
from fractions import Fraction as Fr
from math import comb, factorial
def coeffs_q(k, m):
    return [(-1)**j * Fr(comb(m, j) * factorial(k+m-j), factorial(k+m)) for j in range(m+1)]
def first_nonpositive(k, m, N):
    q = coeffs_q(k, m)
    c = [Fr(1)]
    for n in range(1, N+1):
        s = Fr(0)
        for j in range(1, min(n, m)+1):
            s -= q[j]*c[n-j]
        c.append(s)
        if s <= 0: return n, s
    return None
if __name__ == "__main__":
    k_equals_m = True
    t = time.time()
    for m in range(1, int(sys.argv[1])+1, 2):
        r = first_nonpositive(m, m, int(sys.argv[2]))
        print("m=%d k=m: %s" % (m, "all c_n>0 for n<=%s" % sys.argv[2] if r is None else "FIRST NONPOSITIVE c_%d = %s" % (r[0], float(r[1]))), flush=True)
    print("[%.1fs]" % (time.time()-t))
