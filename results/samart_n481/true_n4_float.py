import numpy as np
from scipy.integrate import quad
from scipy.special import hyp2f1, gamma
def G(x, nterms=400000):
    # 3F2(1/2,1/2,1/2;5/4,3/4;x) by recurrence (float64), x in (0,1]
    term = 1.0; s = 1.0
    for n in range(nterms):
        term *= (0.5+n)**3/((1.25+n)*(0.75+n)*(n+1))*x
        s += term
        if abs(term) < 1e-17*abs(s) and n > 20: break
    return s
G1 = G(1.0, 4000000)
F1 = hyp2f1(1/8, 3/8, 1, 1.0)**2
c = F1/G1
print("c =", c, " (F(1) =", F1, ", 3F2 at 1 =", G1, ")")
n256 = 5.41273981692507642
def n4_true(s):
    f = lambda t: c*np.sqrt(t/256)*G(t/256)/t
    return n256 - quad(f, s, 256, epsabs=1e-12, epsrel=1e-12, limit=200)[0]
for k, direct in ((3.9, 5.2844726), (3.5, 4.7783773), (3.0, 4.1655352), (2.5, 3.5825156), (2.0, 3.0403441)):
    v = n4_true(k**4)
    print("k=%.1f  n_4 (exponent-1/2 branch) = %.8f   direct 2-D integral = %.7f   diff = %.2e" % (k, v, direct, v - direct))
