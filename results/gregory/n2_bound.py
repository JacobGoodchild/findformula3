"""Re-implementation of the (effective) tail criterion from the proof of Thm 5.1 in arXiv:2609.11072 (Section 6) to get n2(ell) with
(-1)^(n-1) G_n^(ell) > 0 for ALL n >= n2(ell).  Uses mpmath quadrature (not interval arithmetic) -> 'numerically certified'.
h(z) = sum_k (-1)^(k+ell) C(ell,2k-1) log(z)^(ell-2k+1) pi^(2k-2) (log^2 z + pi^2)^(-ell);  r = exp(pi*cot(pi/ell))."""
import sys
from mpmath import mp, mpf, quad, log, pi, cot, exp, binomial
mp.dps = 30
def h(z, ell):
    L = log(z)
    s = mpf(0)
    for k in range(1, (ell+1)//2 + 1):
        s += (-1)**k * binomial(ell, 2*k-1) * L**(ell-2*k+1) * pi**(2*k-2)
    return (-1)**ell * s * (L**2 + pi**2)**(-ell)
def n2(ell, start=None):
    r = exp(pi*cot(pi/ell))
    alpha = quad(lambda z: h(z, ell), [0, 1/r**2, 1/r]) if False else quad(lambda z: h(z, ell), [mpf(0), mpf(1)/r**3, mpf(1)/r**2, 1/r])
    assert alpha > 0
    def ok(n):
        if n < ell + 2*r + 2: return False
        e = n - ell + 1
        if ell % 2 == 0:
            I = quad(lambda z: abs(h(z, ell)) / z**2 * ((1/r + 1)/(1/z + 1))**e, [1, 2, r])
            return alpha - I > 0
        else:
            I1 = quad(lambda z: abs(h(z, ell)) / z**2 * ((1/r + 1)/(1/z + 1))**e, [1, 2])
            I2 = quad(lambda z: abs(h(z, ell)) * (1 + mpf(2)**(-(n-ell-1))) / z**2 * ((1/r + 1)/(1/z + 1))**e, [2, r])
            return alpha - I1 - I2 > 0
    n = int(start or ell + 2*r + 3)
    # criterion is monotone in n (the integrals decrease) -> bisection
    lo = n; hi = n
    while not ok(hi): hi *= 2
    while hi - lo > 1:
        mid = (lo + hi)//2
        if ok(mid): hi = mid
        else: lo = mid
    return hi
if __name__ == "__main__":
    for ell in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        print(ell, n2(ell), flush=True)
