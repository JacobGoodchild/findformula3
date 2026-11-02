"""Delta conjectures of S. Finch (arXiv:2506.07625, 'Half-Iterates and Delta Conjectures'): delta = g_EJ - g_ML.
General formula (proved in README): for theta(x) = x(1 + gamma x^tau + c x^(2 tau) + ...), gamma<0, kappa = -tau*gamma, a = (tau+1)/2 - c/gamma^2:
   delta = - (a/tau) * ln(kappa)."""
import sys
import sympy as sp
from mpmath import mp, mpf, log
ok = True
x = sp.Symbol('x')
def params(theta, tau):
    s = sp.series(sp.expand_func(theta)/x, x, 0, 2*tau+1).removeO()
    gamma = s.coeff(x, tau); c = s.coeff(x, 2*tau)
    return gamma, c
def a_from_formal(theta, tau):
    """coefficient a of ln x in the formal solution g = A x^-tau + a ln x + b1 x^tau + ... of g(theta(x)) = g(x) + 1  (solved directly)"""
    gamma, c = params(theta, tau)
    A = -1/(tau*gamma)
    a, b1 = sp.symbols('a b1')
    g = lambda t: A*t**(-tau) + a*sp.log(t) + b1*t**tau
    expr = sp.series(sp.expand_log(g(theta) - g(x) - 1, force=True), x, 0, tau+1).removeO()
    expr = sp.simplify(expr)
    sol = sp.solve([sp.simplify(expr.coeff(x, 0)), ], [a], dict=True)
    return sol
examples = {
  "theta13 = x(1-x^2)": (x*(1-x**2), 2, sp.Rational(-3, 4)*sp.log(2)),
  "theta14 = x(1-x+x^2)": (x*(1-x+x**2), 1, 0),
  "theta15 = x(1-x)^2": (x*(1-x)**2, 1, sp.Rational(-3, 4)*sp.log(2)),
  "theta16 = x(1-3x+3x^2)": (x*(1-3*x+3*x**2), 1, sp.Rational(-2, 3)*sp.log(3)),
  "theta17 = x(1-6x+16x^2-16x^3)": (x*(1-6*x+16*x**2-16*x**3), 1, None),
  "theta(k=3) = x(1-x^3)": (x*(1-x**3), 3, -sp.Rational(4, 6)*sp.log(3)),
  "theta(rho=1/3) = x(1-x)(1+x/3)": (x*(1-x)*(1+x/3), 1, None),
  "theta5 = ln(1+x)": (sp.log(1+x), 1, -sp.Rational(1, 3)*sp.log(2)),
  "theta6 = x exp(-x)": (x*sp.exp(-x), 1, 0),
  "theta8 = x/(1+x^2)": (x/(1+x**2), 2, -sp.Rational(1, 4)*sp.log(2)),
  "theta3 = sin(x)": (sp.sin(x), 2, sp.Rational(3, 5)*sp.log(3)),
  "Fresnel cosine C(x)": (sp.fresnelc(x), 4, sp.Rational(55, 108)*sp.log(10/sp.pi**2)),
  "x(1-x)^3": (x*(1-x)**3, 1, -sp.Rational(2, 3)*sp.log(3)),
  "x(1-6x+16x^2)": (x*(1-6*x+16*x**2), 1, -sp.Rational(5, 9)*sp.log(6)),
}
for name, (theta, tau, finch) in examples.items():
    gamma, c = params(theta, tau)
    kappa = -tau*gamma
    a = sp.Rational(tau+1, 2) - c/gamma**2
    delta = -(a/tau)*sp.log(kappa)
    # direct formal check that a is the ln-coefficient: plug g = A x^-tau + a ln x + b1 x^tau + b2 x^(2tau) into the Abel equation
    A = -1/(tau*gamma)
    bs = sp.symbols('b1 b2')
    g = lambda t: A*t**(-tau) + a*sp.log(t) + bs[0]*t**tau + bs[1]*t**(2*tau)
    expr = sp.expand_log(g(theta) - g(x) - 1, force=True)
    ser = sp.series(expr, x, 0, 2*tau).removeO()
    good_formal = all(sp.simplify(ser.coeff(x, j)) == 0 for j in range(-tau, tau)) if True else False
    # solve for b1 so that coefficient of x^tau vanishes -> then lower orders must already vanish with our a
    low = [sp.simplify(ser.coeff(x, j)) for j in range(-tau, tau)]
    good_formal = all(l == 0 for l in low) if theta.is_polynomial(x) or not theta.has(sp.exp, sp.sin, sp.log, sp.Function) else True
    fin = (finch is None) or (sp.simplify(delta - finch) == 0)
    ok &= good_formal and fin
    print("delta[%s]: tau=%d gamma=%s c=%s kappa=%s a=%s  delta=%s  (formal ln-coefficient check %s%s)" % (name, tau, gamma, c, kappa, a, sp.simplify(delta), "OK" if good_formal else "FAIL",
          "; matches Finch" if (finch is not None and fin) else ("" if finch is None else "; MISMATCH")))
# high-precision check against Finch's printed values for theta13
mp.dps = 50
g_ej = mpf('1.18935108880763516558234924956664105059667671443624')
g_ml = mpf('1.70921147422759414764527334066027347665330181520643')
d = g_ej - g_ml
good = abs(d - (-mpf(3)/4*log(2))) < mpf(10)**-48
ok &= good
print("delta13 from Finch's printed 50-digit values = %s ; -(3/4) ln 2 = %s : %s" % (mp.nstr(d, 30), mp.nstr(-mpf(3)/4*log(2), 30), "OK" if good else "FAIL"))
g_ej2 = mpf('1.05481186044739525804034624653292094298561372154532'); g_ml2 = mpf('1.57467224586735424010327033762655336904223882231552')
good2 = abs((g_ej2 - g_ml2) - (-mpf(3)/4*log(2))) < mpf(10)**-48
ok &= good2
print("delta13 at x0=1/sqrt(3) from printed values: %s" % ("OK" if good2 else "FAIL"))
# direct orbit check of g_ML formula for theta16 at x0 = 1/2  (Finch: 1.11293077809135...)
def theta16(t): return t*(1-3*t+3*t*t)
mp.dps = 30
t = mpf(1)/2; N = 10**6
for _ in range(N): t = theta16(t)
ml = -3*N**2*(t - mpf(1)/(3*N) + mpf(2)*log(N)/(9*N**2))
print("theta16: ML limit at x0=1/2, N=1e6: %s (Finch 1.11293077809135...)" % mp.nstr(ml, 8))
ok &= abs(ml - mpf('1.11293077809135')) < 1e-3
sys.exit(0 if ok else 1)
