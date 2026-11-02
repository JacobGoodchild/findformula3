"""Verification for the proof of S. Finch's conjectured identities (arXiv:2503.00579):  A(x/(1+x)) = B(x)+1,  I(x/(1+x)) = J(x)+1."""
import sys
import sympy as sp
from fractions import Fraction as Fr
from mpmath import mp, mpf, log
ok = True
x = sp.Symbol('x')
h = x/(1+x)
fA = lambda t: t*(1-t);            gB = lambda t: t/(1+t+t**2)
fI = lambda t: t/(1+t-t**2);       fJ = lambda t: t*(1+t)/(1+2*t)
c1 = sp.simplify(fA(h) - h.subs(x, gB(x))) == 0
c2 = sp.simplify(fI(h) - h.subs(x, fJ(x))) == 0
print("finch conjugacy f_A(h(x)) = h(g_B(x)):", "OK" if c1 else "FAIL"); print("finch conjugacy f_I(h(x)) = h(f_J(x)):", "OK" if c2 else "FAIL")
ok &= c1 and c2
# exact orbits (rational): A-orbit of h(x0) is h(B-orbit of x0), I-orbit of h(x0) is h(J-orbit of x0)
def orbit(f, x0, n):
    o = [x0]
    for _ in range(n): o.append(f(o[-1]))
    return o
hh = lambda t: t/(1+t)
for (fa, gb, x0) in [(fA, gB, Fr(1)), (fA, gB, Fr(2)), (fI, fJ, Fr(1)), (fI, fJ, Fr(3, 2))]:
    ob = orbit(gb, x0, 6); oa = orbit(fa, hh(x0), 6)
    good = all(oa[k] == hh(ob[k]) for k in range(7))
    ok &= good
    print("finch exact rational orbits: x0=%s : %s" % (x0, "OK" if good else "FAIL"))
print("finch B-orbit of 1 starts", [str(t) for t in orbit(gB, Fr(1), 5)], "(Finch: 1, 1/3, 3/13, 39/217 ...); A-orbit of 1/2:", [str(t) for t in orbit(fA, Fr(1, 2), 5)])
# numerical: Abel function = lim [1/f^n(x) - n -/+ ln n]; check against Finch's printed digits
mp.dps = 40
def lim(f, x0, sgn, N):
    t = mpf(x0)
    for _ in range(N): t = f(t)
    return 1/t - N + sgn*log(N)          # A,B: 1/x_n = n + ln n + C  -> C = 1/x - n - ln n  (sgn=-1);  I,J: 1/x_n = n - ln n + C -> sgn=+1
N = 400000
vals = {"A(1/2)": (lim(fA, mpf(1)/2, -1, N), 1.76799378613615), "B(1)": (lim(gB, 1, -1, N), 0.76799378613615),
        "I(1/2)": (lim(fI, mpf(1)/2, +1, N), 1.64018851423988), "J(1)": (lim(fJ, 1, +1, N), 0.64018851423988)}
for k, (v, ref) in vals.items():
    good = abs(v - ref) < 2e-4
    ok &= good
    print("finch limit-normalisation %s = %s (Finch %s): %s" % (k, mp.nstr(v, 10), ref, "OK" if good else "FAIL"))
sys.exit(0 if ok else 1)
