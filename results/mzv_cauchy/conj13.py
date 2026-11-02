"""Test Conjecture 1.3 of arXiv:2609.11072 for depth-3 compositions:  C_n^{j;k;l} defined by  (1-x)^{-j} (x^d / Li_k(x))^l = sum C_n x^n.
Claims: C^{0;k;l}_n < 0 and C^{j;k;l}_n > binom(n+j-1,n)/zeta(k)^l  for n >> 0 (admissible k)."""
import sys, itertools, time
from flint import arb, arb_series, ctx
from cypari import pari
from mpmath import mp, mpf
def li_coeffs(k, N):
    """coefficients a_n of Li_k(x) = sum a_n x^n, n<=N  (nested sums)"""
    d = len(k)
    # inner[m] = sum over n_2>...>n_d with n_2<m  => build from the last component upward
    cur = [arb(0)]*(N+2)
    # level d:  t[n] = 1/n^{k_d}
    t = [arb(0)] + [arb(1)/arb(n)**k[-1] for n in range(1, N+1)]
    for lev in range(d-2, -1, -1):
        # prefix sums of t (strictly smaller index): P[n] = sum_{m<n} t[m]
        P = [arb(0)]*(N+1); s = arb(0)
        for n in range(1, N+1):
            P[n] = s; s += t[n]
        t = [arb(0)] + [P[n]/arb(n)**k[lev] for n in range(1, N+1)]
    return t
def C_coeffs(k, j, l, N, prec=256):
    ctx.prec = prec; ctx.cap = N+1
    d = len(k)
    a = li_coeffs(k, N+d)
    # Li_k(x)/x^d = sum_{n>=d} a_n x^{n-d}
    g = arb_series([a[n+d] for n in range(N+1)])
    r = (g.inv())**l if l > 1 else g.inv()
    if j > 0:
        # multiply by (1-x)^{-j}: j-fold prefix sums
        c = r.coeffs()
        for _ in range(j):
            s = arb(0); out = []
            for v in c:
                s += v; out.append(s)
            c = out
        return c
    return r.coeffs()
if __name__ == "__main__":
    N = int(sys.argv[1])
    from math import comb
    pari.set_real_precision(60)
    bad = 0
    for k in itertools.product(range(1, 5), repeat=3):
        if k[0] < 2: continue
        zk = arb(str(pari('zetamult(%s)' % list(k))).replace(' ', '').replace('E', 'e'))
        for l in (1, 2):
            c0 = C_coeffs(k, 0, l, N)
            neg0 = all(c0[n] < 0 for n in range(N//2, N+1))
            for j in (1, 2):
                cj = C_coeffs(k, j, l, N)
                ok = all(cj[n] > comb(n+j-1, n)/zk**l for n in range(N//2, N+1))
                if not (neg0 and ok):
                    bad += 1
                    print("k=%s l=%d j=%d : C^0<0 on [N/2,N]: %s ; C^j > binom/zeta^l: %s" % (k, l, j, neg0, ok), flush=True)
    print("done N=%d, failures=%d" % (N, bad))
