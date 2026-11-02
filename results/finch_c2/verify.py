import sys
from mpmath import mp, mpf
from c2 import partial_sums, extrapolate
mp.dps = 60
x0 = mpf(2)
Ns = [500*2**i for i in range(8)]
r = partial_sums(x0, set(Ns))
S = {N: r[N][0] for N in Ns}; D = {N: r[N][1] for N in Ns}
Sinf = extrapolate(S, Ns, [3, 4, 5, 6, 7, 8]); Dinf = extrapolate(D, Ns, [1, 2, 3, 4, 5, 6])
c2 = Dinf*Sinf
ok = abs(c2 - mpf('0.37462642198301734111')) < mpf(10)**-18 and abs(Dinf - mpf('0.6615613240486860705677502635')) < mpf(10)**-18
print("finch_c2 C'(2)=%s C''(2)=%s vs Finch finite differences: %s" % (mp.nstr(Dinf, 22), mp.nstr(c2, 22), "OK" if ok else "FAIL"))
sys.exit(0 if ok else 1)
