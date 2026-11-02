"""Re-checks d_CM(R_2) = 2.86670425... (two independent evaluations of the fractional-derivative minimum: double-precision Chebyshev/QUADPACK and 22-digit mpmath quadrature at the critical point)."""
import sys
import numpy as np
from mpmath import mp, mpf
from cmfast import crit
from cmdeg import make_h, H_caputo
ok = True
q, a, t = crit(2, 0)
good = abs(q + a - 2.8667042552) < 2e-9
ok &= good
print("stirling d_CM(R_2) = %.10f : %s" % (q + a, "OK" if good else "FAIL"))
mp.dps = 22
hp = make_h(2, 0, q + 1)
a0 = mpf(a)
vm = H_caputo(hp, a0 - mpf(3)/10**5, mpf(t)); vp = H_caputo(hp, a0 + mpf(3)/10**5, mpf(t))
good = (vm > 0) and (vp < 0)
ok &= good
print("stirling independent mp check: H(a*-3e-5, t*) = %s > 0 and H(a*+3e-5, t*) = %s < 0 : %s" % (mp.nstr(vm, 3), mp.nstr(vp, 3), "OK" if good else "FAIL"))
sys.exit(0 if ok else 1)
