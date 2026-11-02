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
sys.exit(0 if ok else 1)
