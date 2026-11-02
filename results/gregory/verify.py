"""Re-checks Gr(ell) for ell = 3..8 (fast) with interval arithmetic; compares with the values of arXiv:2609.11072 (3..7) and our new ones."""
import sys
from grscan2 import certified_scan
EXPECT = {3: 11, 4: 36, 5: 113, 6: 346, 7: 1030, 8: 2995}
ok = True
for ell, g in EXPECT.items():
    bad, unk, prec = certified_scan(ell, 12000, 512)
    gr = bad[-1] + 1
    good = (gr == g)
    ok &= good
    print("gregory Gr(%d)=%d: %s" % (ell, gr, "OK" if good else "FAIL (expected %d)" % g))
# Conjecture 6.1 of arXiv:2609.11072 says 0.47*3^l < Gr(l) < 0.477*3^l for all l>=5
for ell in (5, 8):
    print("gregory Conjecture 6.1 violated at ell=%d: %s" % (ell, "OK" if EXPECT[ell] <= 0.47 * 3**ell else "FAIL"))
    ok &= EXPECT[ell] <= 0.47 * 3**ell
# integral representation / large-l machinery: n*(l) must lie in (Gr-1, Gr)
from big_ell import J, breakpoints, sign_change
from mpmath import mp, exp, pi, cot
mp.dps = 40
for ell, g in ((5, 113), (7, 1030)):
    r = exp(pi*cot(pi/ell))
    ns = sign_change(ell, 0.8*r, 3*r, iters=45)
    good = (g - 1 < ns <= g)
    ok &= good
    print("gregory integral-representation n*(%d) = %s in (%d, %d]: %s" % (ell, mp.nstr(ns, 10), g-1, g, "OK" if good else "FAIL"))
sys.exit(0 if ok else 1)
