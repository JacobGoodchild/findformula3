"""k*(m) := smallest k for which 1/q_{k,m} has a negative Taylor coefficient (bisection; monotonicity in k checked on a sample)."""
import sys, time
from kmin import neg_indices
def fails(k, m):
    neg, unc = neg_indices(k, m, 5*k + 300)
    assert not unc, ("uncertified", k, m)
    return bool(neg)
def kstar(m, hi=None):
    hi = hi or 4*m + 100
    assert fails(hi, m), "no failure up to hi"
    lo = 0   # fails(lo) False assumed (checked below)
    assert not fails(lo, m)
    while hi - lo > 1:
        mid = (lo+hi)//2
        if fails(mid, m): hi = mid
        else: lo = mid
    # sanity: previous k passes, next 20 fail
    assert not fails(hi-1, m) and all(fails(hi+t, m) for t in range(0, 20))
    return hi
if __name__ == "__main__":
    for m in range(int(sys.argv[1]), int(sys.argv[2])+1, int(sys.argv[3])):
        t = time.time(); k = kstar(m)
        print("m=%d k*=%d k*/m=%.4f  k*-2m=%d [%.0fs]" % (m, k, k/m, k-2*m, time.time()-t), flush=True)
