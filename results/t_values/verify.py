"""Checks for the proof of Conjecture 4.5 of Chavan-Kobayashi-Layja (arXiv:2111.07097): t({2}^N,1) = I(2N)/(2N)!, I(n) = int_0^{pi/2} theta^n cot(theta) dtheta."""
import sys
from mpmath import mp, mpf, quad, pi, cot, factorial, zeta, log, gamma, cosh, sqrt, nsum, inf
from conj45 import t_two1, I
mp.dps = 30
ok = True
# (1) Q_{2S-1}(u) = prod_{n odd > 2S-1}(1+u^2/n^2) = Gamma(S+1/2)^2/(Gamma(S+1/2+iu/2) Gamma(S+1/2-iu/2)) = c_S int_0^{pi/2} cosh(u th) cos^{2S-1}(th) dth,  c_S = 2 Gamma(S+1/2)/(sqrt(pi) Gamma(S))
u = mpf('0.7')
for S in (1, 2, 5):
    prod_val = mpf(1)
    # product over odd n > 2S-1 up to large cutoff, using the convergent tail via the gamma form for the check of the other two forms only
    g = gamma(S + mpf(1)/2)**2/(gamma(S + mpf(1)/2 + 1j*u/2)*gamma(S + mpf(1)/2 - 1j*u/2))
    cS = 2*gamma(S + mpf(1)/2)/(sqrt(pi)*gamma(S))
    integ = cS*quad(lambda th: cosh(u*th)*mp.cos(th)**(2*S-1), [0, pi/2])
    # direct product: prod_{n odd>2S-1} (1+u^2/n^2) = cosh(pi u/2)/prod_{k odd<=2S-1}(1+u^2/k^2)
    direct = cosh(pi*u/2)
    for k in range(1, 2*S, 2): direct /= (1 + u**2/mpf(k)**2)
    good = abs(g.real - integ) < mpf(10)**-20 and abs(direct - integ) < mpf(10)**-20
    ok &= good
    print("t-values gamma/integral/product forms of Q_{2S-1} agree for S=%d: %s" % (S, "OK" if good else "FAIL"))
# (2) sum_{S>=1} c_S x^{2S-1}/(2S-1) = x/sqrt(1-x^2)  (so equals cot(theta) at x = cos(theta))
x = mpf('0.6')
cS = lambda S: 2*gamma(S + mpf(1)/2)/(sqrt(pi)*gamma(S))
val = nsum(lambda S: cS(int(S))*x**(2*int(S)-1)/(2*int(S)-1), [1, inf])
good = abs(val - x/sqrt(1 - x*x)) < mpf(10)**-15; ok &= good
print("t-values series sum c_S x^(2S-1)/(2S-1) = x/sqrt(1-x^2): %s" % ("OK" if good else "FAIL"))
# (3) the identity itself, numerically, for N = 1..4 (direct nested-sum evaluation vs I(2N)/(2N)!), reuse conj45 numerics
for N in (1, 2, 3):
    M = 3200
    # Richardson-free check at moderate accuracy: tail ~ M^{-N}; compare to 1e-3-ish for N=1, tighter for larger N
    v = t_two1(N, M); w = I(2*N)/factorial(2*N)
    tol = {1: 5e-4, 2: 1e-6, 3: 1e-8}[N]
    good = abs(v - w) < tol; ok &= good
    print("t-values t({2}^%d,1) partial sum (M=%d) vs I(2N)/(2N)!: %s (|diff|=%s)" % (N, M, "OK" if good else "FAIL", mp.nstr(abs(v-w), 3)))
# (4) closed form: I(2N)/(2N)! = 2^{-2N} sum_{j<N} (-1)^j pi^{2N-2j} eta(2j+1)/(2N-2j)! + (-1)^N 2 (1-2^{-2N-1}) zeta(2N+1)/(2N)!
eta = lambda s: log(2) if s == 1 else (1 - mpf(2)**(1 - s))*zeta(s)
for N in (1, 2, 3, 4):
    cf = (sum((-1)**j*pi**(2*N-2*j)*eta(2*j+1)/factorial(2*N-2*j) for j in range(N)) + (-1)**N*2*(1 - mpf(2)**(-2*N-1))*zeta(2*N+1))/mpf(2)**(2*N)
    good = abs(cf - I(2*N)/factorial(2*N)) < mpf(10)**-20; ok &= good
    print("t-values closed form for N=%d: %s" % (N, "OK" if good else "FAIL"))
sys.exit(0 if ok else 1)
