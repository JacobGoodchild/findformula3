"""Ulgenes (arXiv:2301.09699, Maple Trans. 2025), Conjecture 3.1: the principal inverse gamma function has the Newton series
 invG0(x) = 2 + sum_{n>=0} a_n prod_{i=1}^{n} ln(x/i!)   -- nodes s_k = ln(k!) (k>=1), values y_k = k+1 -- converging on (Gamma(alpha), infinity), alpha = 1.4616 (psi(alpha)=0).
(the coefficient formula in the paper is the divided-difference formula, so the content is the CONVERGENCE claim).  Numerical test with divided differences."""
import sys
from mpmath import mp, mpf, log, factorial, findroot, gamma, psi
mp.dps = 400
def newton_coeffs(N):
    s = [log(factorial(k)) for k in range(1, N+2)]          # s_1..s_{N+1}  (s_1 = 0)
    y = [mpf(k+1) for k in range(1, N+2)]                   # invG0(k!) = k+1
    # divided differences, in-place
    a = []
    col = y[:]
    a.append(col[0])
    for order in range(1, N+1):
        col = [(col[i+1] - col[i])/(s[i+order] - s[i]) for i in range(len(col)-1)]
        a.append(col[0])
    return s, a
def newton_eval(x, s, a, upto):
    lx = log(x)
    total = a[0]; prod = mpf(1); partial = [total]
    for n in range(1, upto+1):
        prod *= (lx - s[n-1])
        total += a[n]*prod
        partial.append(total)
    return partial
def invgamma(x):
    # principal inverse: solution t > alpha of Gamma(t) = x
    return findroot(lambda t: gamma(t) - x, mpf(3) if x > 2 else mpf('1.7'))
if __name__ == "__main__":
    N = int(sys.argv[1])
    s, a = newton_coeffs(N)
    for x in ['0.9', '1', '1.5', '2', '3', '4', '10', '100']:
        xx = mpf(x)
        part = newton_eval(xx, s, a, N)
        true = invgamma(xx)
        print("x=%s  true invG0=%s  partial sums at n=10,20,40,%d: %s | err=%s" % (x, mp.nstr(true, 12), N, [mp.nstr(part[n], 10) for n in (10, 20, 40, N)], mp.nstr(abs(part[N]-true), 3)))
