import sys
from mpmath import mp, mpf
sys.path.insert(0, '.')
from half import half
mp.dps = 120
ok = True
for b, expect in [('4/3', '1.2058374340430955949418393065071125669'), ('5/4', '1.1635953619650088490259432733584363128'), ('6/5', '1.1362624867271280841853009186474260255')]:
    n, d = map(int, b.split('/'))
    L, lam, y, psi = half(mpf(n)/d)
    good = abs(y - mpf(expect)) < mpf(10)**-36
    ok &= good
    print("tetration T(%s,1/2) = %s : %s" % (b, mp.nstr(y, 25), "OK" if good else "FAIL"))
sys.exit(0 if ok else 1)
