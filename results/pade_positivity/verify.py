"""Quick re-check for verify_all.py: (a) rigorous all-n proof for odd m <= 21 on the diagonal (k=m); (b) the counterexamples (k,m,n) = (66,5,38), (44,7,37), (45,9,42) of arXiv:2610.39051 and our smaller (42,9);
(c) k*(m) for m = 9, 19, 29 equals 42, 54, 73 and k*(m)-2m is in [12, 25]."""
import sys
from math import comb, factorial
from fractions import Fraction as Fr
from rigorous_diag import prove
from kstar import kstar
from kmin import neg_indices
ok = True
for m in range(3, 22, 2):
    N0, msg = prove(m)
    good = N0 is not None
    ok &= good
    print("pade diag m=%d (all n>=0 positive): %s" % (m, "OK (%s)" % msg if good else "FAIL " + msg))
# exact rational check of the published counterexamples
def c_n(k, m, N):
    q = [(-1)**j * Fr(comb(m, j) * factorial(k+m-j), factorial(k+m)) for j in range(m+1)]
    c = [Fr(1)]
    for n in range(1, N+1):
        c.append(-sum(q[j]*c[n-j] for j in range(1, min(n, m)+1)))
    return c
for (k, m, n) in [(66, 5, 38), (44, 7, 37), (45, 9, 42), (42, 9, 41)]:
    good = c_n(k, m, n)[n] < 0
    ok &= good
    print("pade counterexample c_%d(%d,%d) < 0 (exact rational): %s" % (n, k, m, "OK" if good else "FAIL"))
for m, expect in [(9, 42), (19, 54), (29, 73)]:
    ks = kstar(m)
    good = (ks == expect)
    ok &= good
    print("pade k*(%d) = %d: %s" % (m, ks, "OK" if good else "FAIL (expected %d)" % expect))
sys.exit(0 if ok else 1)
