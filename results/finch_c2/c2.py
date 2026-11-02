"""S. Finch, Exercises in Iterational Asymptotics III (arXiv:2503.13378), Sec. 3: x_{n+1} = x_n + 1 + 1/x_n^2, C(x0) = lim (x_n - n).
Finch: C(2) = 2.59878685582487..., C'(2) = prod (1 - 2/x_n^3) = 0.66156132404868..., and the series guess C''(2) = C' sum (1-2/x_n^3)^{-1} 6/x_n^4 = 0.3909 'appears wrong'; a finite-difference estimate gives 0.374626421983...
 'An independent confirmation of the 0.3746 estimate remains open.'
Exact derivation: D_n = dx_n/dx_0 = prod_{k<n} f'(x_k), E_n = d^2 x_n/dx_0^2 satisfies E_{n+1} = f'(x_n) E_n + f''(x_n) D_n^2, so  C''(x_0) = lim E_n = C'(x_0) * sum_{j>=0} f''(x_j) D_j / f'(x_j),  f' = 1 - 2/x^3, f'' = 6/x^4."""
import sys
from mpmath import mp, mpf, richardson
mp.dps = 60
def partial_sums(x0, Ns):
    x = mpf(x0); D = mpf(1); S = mpf(0); res = {}
    Nmax = max(Ns)
    for j in range(Nmax + 1):
        fp = 1 - 2/x**3; fpp = 6/x**4
        S += fpp*D/fp
        D *= fp
        x = x + 1 + 1/x**2
        if (j + 1) in Ns: res[j+1] = (S, D, x - (j+1))
    return res
def extrapolate(vals, Ns, powers):
    """Richardson: assume V(N) = V + sum_p a_p N^{-p}; solve the linear system for V using the given exponents"""
    k = len(powers) + 1
    A = mp.matrix(k, k); b = mp.matrix(k, 1)
    for i, N in enumerate(Ns[-k:]):
        A[i, 0] = 1
        for jj, p in enumerate(powers): A[i, jj+1] = mpf(N)**(-p)
        b[i] = vals[N]
    sol = mp.lu_solve(A, b)
    return sol[0]
if __name__ == "__main__":
    x0 = mpf(2)
    Ns = [500*2**i for i in range(0, 8)]
    r = partial_sums(x0, set(Ns))
    S = {N: r[N][0] for N in Ns}; D = {N: r[N][1] for N in Ns}; C = {N: r[N][2] for N in Ns}
    powers = [3, 4, 5, 6, 7, 8]
    Sinf = extrapolate(S, Ns, powers[:6]); Dinf = extrapolate(D, Ns, [1, 2, 3, 4, 5, 6][:6]); Cinf = extrapolate(C, Ns, [1, 2, 3, 4, 5, 6][:6])
    print("C(2)   =", mp.nstr(Cinf, 30), " (Finch 2.598786855824871348...)")
    print("C'(2)  =", mp.nstr(Dinf, 30), " (Finch 0.66156132404868607...)")
    print("C''(2) =", mp.nstr(Dinf*Sinf, 30), " (Finch finite difference 0.374626421983017341...)")
    # the (wrong) series from the paper: C' * sum 1/(1-2/x^3) 6/x^4  without the D_j factor
    x = x0; s2 = mpf(0)
    for j in range(200000):
        s2 += 6/x**4/(1 - 2/x**3); x = x + 1 + 1/x**2
    print("paper's series (without D_j) ~", mp.nstr(Dinf*s2, 8), "(Finch: 0.3909)")
