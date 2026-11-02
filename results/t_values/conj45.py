"""Conjecture 4.5 of Chavan-Kobayashi-Layja (arXiv:2111.07097):  t({2}^N, 1) = I(2N)/(2N)!,  I(n) = int_0^1 arcsin^n(x)/x dx = int_0^{pi/2} theta^n cot(theta) dtheta,
where t(s_1..s_k) = sum_{n_1>...>n_k>=1, all n_i odd} n_1^{-s_1}...n_k^{-s_k}  (Hoffman's multiple t-value).
Numerics: inner sum via generating function  e_N{1/n^2 : n odd > m} = [y^N] cosh(pi sqrt(y)/2) / prod_{k odd<=m}(1+y/k^2)."""
import sys
from mpmath import mp, mpf, quad, pi, cot, factorial, sinh, cosh, nsum, inf, richardson
mp.dps = 40
def series_coeffs_inner(m, Nmax):
    """coefficients c_0..c_Nmax of cosh(pi sqrt(y)/2) / prod_{k odd <= m}(1+y/k^2) in y"""
    num = [(pi/2)**(2*j)/factorial(2*j) for j in range(Nmax+1)]       # cosh(pi sqrt(y)/2) = sum (pi^2 y/4)^j/(2j)!
    for k in range(1, m+1, 2):
        a = mpf(1)/k**2
        # divide by (1 + a y): c_j <- c_j - a c_{j-1}  (series division)
        new = [num[0]]
        for j in range(1, Nmax+1): new.append(num[j] - a*new[j-1])
        num = new
    return num
def t_two1(N, M):
    """partial sum over odd m <= M of (1/m) * c_N(m)"""
    num = [(pi/2)**(2*j)/factorial(2*j) for j in range(N+1)]
    total = mpf(0)
    for m in range(1, M+1, 2):
        a = mpf(1)/m**2
        new = [num[0]]
        for j in range(1, N+1): new.append(num[j] - a*new[j-1])
        num = new
        total += num[N]/m
    return total
def I(n):
    return quad(lambda th: th**n*cot(th), [0, pi/4, pi/2])
if __name__ == "__main__":
    for N in range(1, 5):
        # Richardson in M: tail ~ sum_{m>M odd} (1/m) c_N(m) ~ M^{-N} * ...; use several M and extrapolate in powers 1/M
        Ms = [200*2**i for i in range(6)]
        vals = {M: t_two1(N, M) for M in Ms}
        # polynomial extrapolation in 1/M with exponents N, N+1, ...
        from mpmath import matrix, lu_solve
        k = 5
        A = matrix(k+1, k+1); b = matrix(k+1, 1)
        for i, M in enumerate(Ms[-(k+1):]):
            A[i, 0] = 1
            for jj in range(k): A[i, jj+1] = mpf(M)**(-(N+jj))
            b[i] = vals[M]
        sol = lu_solve(A, b)
        print("N=%d: t({2}^N,1) ~ %s ; I(2N)/(2N)! = %s ; diff = %s" % (N, mp.nstr(sol[0], 20), mp.nstr(I(2*N)/factorial(2*N), 20), mp.nstr(abs(sol[0]-I(2*N)/factorial(2*N)), 3)))
