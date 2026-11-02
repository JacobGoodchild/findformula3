"""Real completely monotonic degree of the Stirling remainders (arXiv:2610.33699, V. Krasniqi: 'exact real degrees remain open').

Setting. f_{n,m}(x) = (-1)^m (-1)^n [ d^m/dx^m ] ( log Gamma(x) - (x-1/2)log x + x - log(2 pi)/2 - sum_{k<=n} B_{2k}/(2k(2k-1)x^{2k-1}) )  = Laplace transform of  F(t) = t^m * k_n(t),
 k_n(t) = (-1)^n t^{-1} [ 1/(e^t-1) - 1/t + 1/2 - sum_{k=1}^n B_{2k} t^{2k-1}/(2k)! ]  >= 0.
d_CM(f) = sup{rho: x^rho f(x) is CM}.  Write rho = q + a with q = integer, 0<a<1, h = F^{(q)} (h(0)=0 since F = O(t^{2n+m})).
 x^rho L[F] = L[D^a h]   (Caputo = Riemann-Liouville here).  By Bernstein's theorem: x^rho f is CM  <=>  D^a h >= 0 on (0,infinity).
 Gamma(1-a) t^a D^a h(t) = H(a,t) := h(t) + a * int_0^1 (h(t) - h(tv)) (1-v)^(-1-a) dv.          (Lemma 2.2 of the paper)
So  d_CM = q + a*  with  a* = sup{a : min_t H(a,t) >= 0}.
"""
import sys
from mpmath import mp, mpf, bernoulli, factorial, exp, quad, findroot, binomial, nsum, inf
mp.dps = 30
def make_h(n, m, q):
    """h(t) = d^q/dt^q [ t^m k_n(t) ].  For t<=T0 use the Taylor series, otherwise exponential sum."""
    # t^m k_n(t) = (-1)^n sum_{k>n} B_{2k} t^{2k-2+m}/(2k)!  (|t|<2 pi)
    coef = []
    K = 120
    for k in range(n+1, K):
        e = 2*k - 2 + m
        if e - q < 0: continue
        c = (-1)**n * bernoulli(2*k) / factorial(2*k) * factorial(e) / factorial(e - q)
        coef.append((e - q, c))
    N = q
    def h_series(t):
        return sum(c * t**e for e, c in coef)
    def h_exp(t):
        # t^m * [ (-1)^n ( sum_j e^{-jt}/t - 1/t^2 + 1/(2t) - sum_{k<=n} B_{2k} t^{2k-2}/(2k)! ) ]  differentiated q times (Leibniz for t^m * stuff)
        # build F(t) pieces as list of (coef, power) for polynomial/rational parts, exp part separately.
        def dpow(c, p, order):          # d^order/dt^order of c*t^p
            r = c
            for i in range(order): r *= (p - i)
            return r * t**(p - order)
        # polynomial/rational part P(t) = (-1)^n( -t^{-2} + t^{-1}/2 - sum B_{2k} t^{2k-2}/(2k)! ), times t^m
        parts = [(-1)**n * (-1), m - 2], [(-1)**n * mpf(1)/2, m - 1]
        pl = [((-1)**n * (-1), m - 2), ((-1)**n * mpf(1)/2, m - 1)] + [((-1)**n * (-bernoulli(2*k) / factorial(2*k)), 2*k - 2 + m) for k in range(1, n+1)]
        val = sum(dpow(c, p, q) for c, p in pl)
        # exp part: (-1)^n t^{m-1} sum_j e^{-jt}; derivative by Leibniz: d^q [t^{m-1} e^{-jt}] = sum_i C(q,i) d^i(t^{m-1}) (-j)^{q-i} e^{-jt}
        def exp_term(j):
            s = mpf(0)
            for i in range(q + 1):
                di = mpf(1)
                for r in range(i): di *= (m - 1 - r)
                s += binomial(q, i) * di * t**(m - 1 - i) * (-j)**(q - i)
            return s * exp(-j*t)
        jmax = int(mp.dps * 2.4 / float(t)) + 3
        val += (-1)**n * sum(exp_term(j) for j in range(1, jmax + 1))
        return val
    T0 = mpf(3)
    return lambda t: h_series(t) if t <= T0 else h_exp(t)
def Hfun(h, a, t):
    ht = h(t)
    f = lambda v: (ht - h(t*v)) * (1 - v)**(-1 - a)
    I = quad(f, [0, mpf(1)/2, 1])
    return ht + a * I
if __name__ == "__main__":
    n, m = int(sys.argv[1]), int(sys.argv[2])
    q = 2*n + m - 2
    h = make_h(n, m, q)
    for t in [0.5, 1, 2, 4, 8, 16, 30]:
        print("t=%s h(t)=%s" % (t, mp.nstr(h(mpf(t)), 12)))

def H_caputo(hp, a, t):
    """Gamma(1-a) t^a D^a h (t) = t^a * int_0^t (t-u)^(-a) h'(u) du, via s=(t-u)^(1-a)."""
    S = t**(1 - a)
    g = lambda s: hp(t - s**(1/(1 - a)))
    pts = [0, S/8, S/4, S/2, S*3/4, S]
    return t**a * quad(g, pts) / (1 - a)
def amin(hp, a, ts):
    return min(H_caputo(hp, a, t) for t in ts)

def inner_min(hp, a, lo, hi, tol=mpf(10)**-10):
    """minimise t -> H(a,t) on [lo,hi] by golden section after a coarse grid"""
    N = 24
    grid = [lo + (hi - lo)*i/N for i in range(N+1)]
    vals = [H_caputo(hp, a, t) for t in grid]
    i = min(range(N+1), key=lambda j: vals[j])
    l, r = grid[max(i-1, 0)], grid[min(i+1, N)]
    gr = (mp.sqrt(5) - 1)/2
    c, d = r - gr*(r-l), l + gr*(r-l)
    fc, fd = H_caputo(hp, a, c), H_caputo(hp, a, d)
    while r - l > tol:
        if fc < fd:
            r, d, fd = d, c, fc; c = r - gr*(r-l); fc = H_caputo(hp, a, c)
        else:
            l, c, fc = c, d, fd; d = l + gr*(r-l); fd = H_caputo(hp, a, d)
    t = (l + r)/2
    return H_caputo(hp, a, t), t
def critical_a(n, m, lo_t=None, hi_t=None, verbose=False):
    q = 2*n + m - 2
    hp = make_h(n, m, q + 1)
    lo_t = lo_t or mpf(2); hi_t = hi_t or mpf(40*n)
    f = lambda a: inner_min(hp, a, lo_t, hi_t)
    lo, hi = mpf(0.5), mpf('0.999')
    assert f(lo)[0] > 0 and f(hi)[0] < 0
    for _ in range(40):
        mid = (lo + hi)/2
        v, t = f(mid)
        if verbose: print(float(mid), float(v), float(t))
        if v > 0: lo = mid
        else: hi = mid
        if hi - lo < mpf(10)**-11: break
    return (lo + hi)/2, t
if __name__ == "__main__":
    pass
