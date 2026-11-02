import sys, time
from cypari import pari
from mpmath import mp, mpf
from exact_reduce import S_exact
from numerics import S
def mzv_val(w, dps):
    pari.set_real_precision(dps+10)
    if w == (): return mpf(1)
    return mpf(str(pari('zetamult(%s)' % list(w))).replace(' ','').replace('E','e'))
if __name__ == "__main__":
    dps = 60
    for q in range(1, int(sys.argv[1])+1):
        t0 = time.time()
        tot = S_exact(q)
        assert all(k[0] == 0 for k in tot), "T terms remain"
        mp.dps = dps+10
        val = sum(mpf(c.numerator)/c.denominator * mzv_val(w, dps) for (t, w), c in tot.items())
        num = S(q, dps)
        mp.dps = dps
        print(q, "terms", len(tot), "exact-vs-numeric diff", mp.nstr(abs(val-num), 3), " [%.1fs]" % (time.time()-t0), flush=True)
