"""Weight-(q+2) component of S_q (from the exact MZV combination) versus the conjectured closed form (zeta(q+2)+zeta(q+1,1))/q!."""
import sys
from math import factorial
from mpmath import mp, mpf
from exact_reduce import S_exact
from check_exact import mzv_val
mp.dps = 80
ok = True
for q in range(1, int(sys.argv[1])+1):
    tot = S_exact(q)
    top = sum(mpf(c.numerator)/c.denominator * mzv_val(w, 70) for (t, w), c in tot.items() if sum(w) == q+2)
    pred = (mzv_val((q+2,), 70) + mzv_val((q+1, 1), 70)) / factorial(q)
    d = abs(top - pred)
    good = d < mpf(10)**-60
    ok &= good
    print("top-weight q=%d: %s (|diff|=%s)" % (q, "OK" if good else "FAIL", mp.nstr(d, 3)), flush=True)
sys.exit(0 if ok else 1)
