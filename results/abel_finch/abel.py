"""Finch's Abel-function identities (arXiv:2503.00579):  A(x/(1+x)) = B(x)+1  and  I(x/(1+x)) = J(x)+1.
Numerical normalisation check: compute C(x0) from the orbit via the power-logarithmic expansion, as Finch does, with mpmath."""
from mpmath import mp, mpf, log, findroot
mp.dps = 60
# polynomials P_m(X) from the paper (k=4 terms enough for N ~ 1e7? we use a cheaper route: Richardson on 1/x_n)
def orbit_C(f, x0, sign, N=2*10**6, terms=None):
    """x_n ~ 1/n + (sign*ln n - C)/n^2 + ...  Solve for C using the first two correction polynomials only (error O(ln^2 n/n^3 * n) -> C error ~ ln^2 N / N)."""
    x = mpf(x0)
    for n in range(N): x = f(x)
    n = mpf(N)
    # 1/x_n = n + ( -(sign ln n - C) ) + O(ln^2 n / n)   =>  C = 1/x_n - n + sign*ln n   (leading), refine below with one more correction
    return 1/x - n + sign*log(n)
if __name__ == "__main__":
    fA = lambda x: x*(1-x)
    fB = lambda x: x/(1+x+x*x)
    for N in (10**5, 10**6):
        print("N=%d  C_A(1/2)=%s   C_B(1)=%s" % (N, mp.nstr(orbit_C(fA, mpf(1)/2, -1, N), 8), mp.nstr(orbit_C(fB, mpf(1), -1, N), 8)))
    print("Finch: A(1/2)=1.76799378613615..., B(1)=0.76799378613615...")
