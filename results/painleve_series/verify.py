"""Checks supporting the proof of Conjecture 7.1 of arXiv:2606.21145 (see README.md)."""
import sys, random
from fractions import Fraction as Fr
import sympy as sp
from series import compute, solveL
ok = True
# (1) key identity: with pi0=0, pi2=pi1:  e2 - (a2/a1) e1 - q0 pi1 a1/(1+a1) e0 == 0, and e2 does not involve a3, pi3, ...
xi, q0, pi1, pi2, pi3, pi4 = sp.symbols('xi q0 pi1 pi2 pi3 pi4')
a = sp.symbols('a1:7')
T = sum(a[i]*xi**(i+1) for i in range(6))
P = lambda u: pi1*u + pi2*u**2 + pi3*u**3 + pi4*u**4
E = sp.expand(sp.diff(T, xi, 2)*T - sp.diff(T, xi)**2 - (q0*sp.exp(-xi)*P(T) - 1))
E = sp.series(E, xi, 0, 4).removeO()
e = [sp.expand(E.coeff(xi, m)) for m in range(4)]
res = sp.simplify((e[2] - (a[1]/a[0])*e[1] - (q0*pi1*a[0]/(1+a[0]))*e[0]).subs(pi2, pi1))
g1 = (res == 0); ok &= g1
g2 = (not e[2].has(a[2])) and (not e[2].has(pi3)); ok &= g2
print("painleve identity e2 = (a2/a1) e1 + q0 pi1 a1/(1+a1) e0 :", "OK" if g1 else "FAIL")
print("painleve e2 independent of a3, pi3, pi4 :", "OK" if g2 else "FAIL")
# (2) solvability functional of L_s equals (const) * [x^2](rho e^{-s x})
random.seed(3)
g3 = True
for s in range(1, 8):
    for deg in range(0, 7):
        r = [Fr(random.randint(-9, 9)) for _ in range(deg+1)]
        _, resid = solveL(s, r)
        x = sp.Symbol('x')
        phi = sp.series(sum(sp.Rational(c.numerator, c.denominator)*x**i for i, c in enumerate(r))*sp.exp(-s*x), x, 0, 3).removeO().coeff(x, 2)
        phi = Fr(int(sp.numer(phi)), int(sp.denom(phi)))
        if resid != phi * Fr(2, s*s): g3 = False
ok &= g3
print("painleve solvability residual == (2/s^2) [x^2](rho e^{-sx}) for s=1..7, deg 0..6 :", "OK" if g3 else "FAIL")
# (3) exact recursion: p_k exist (all consistency residuals 0) for several P with pi0=0, pi1=pi2, up to S
tests = [([0,0,0,1], 25), ([0,0,0,0,1], 18), ([0,0,0,0,0,0,1], 12), ([0,1,1,0,1], 18), ([0,2,2,5,0,1], 12), ([0,-3,-3,1], 14), ([0,1,1,-2,3], 14)]
g4 = True
for Pc, S in tests:
    p, resid = compute([Fr(c) for c in Pc], S)
    good = (len(p) == S+1 and all(r == 0 for r in resid))
    g4 &= good
print("painleve exact p_k exist (all obstructions 0) for %d test polynomials :" % len(tests), "OK" if g4 else "FAIL")
ok &= g4
# (4) closed form for P = t^2 + t:  p_k = (x + H_k)/k!
p, resid = compute([Fr(0), Fr(1), Fr(1)], 12)
H = Fr(0); g5 = True
from math import factorial
for k in range(1, 13):
    H += Fr(1, k)
    g5 &= (p[k] == [H/factorial(k), Fr(1, factorial(k))])
ok &= g5
print("painleve P=t^2+t: p_k = (x+H_k)/k! for k<=12 :", "OK" if g5 else "FAIL")
sys.exit(0 if ok else 1)
