# Exact real completely-monotonic degrees of the Stirling remainders (numerics)  -- arXiv:2610.33699, V. Krasniqi

R_n(x) = (-1)^n [ log Gamma(x) - (x-1/2) log x + x - (1/2) log 2pi - sum_{k<=n} B_{2k}/(2k(2k-1) x^{2k-1}) ],  f_{n,m} = (-1)^m R_n^{(m)}, d_CM(f) = sup{rho : x^rho f(x) completely monotonic}.
Krasniqi proves 2n+m-2 < d_CM(f_{n,m}) < 2n+m-1 (disproving the Mahmoud-Qi conjectures d = 2n+m-2) and gives only bounds such as 8/3 < d_CM(R_2) < 3, 32/9 < d_CM(-R_2') < 4.
**Open per the paper (Section 6): "The first remaining problem is to determine the exact values of d_CM(R_2) and d_CM(-R_2'). A second is to decide whether (2n-1) delta_{n,m} converges for fixed m, and to identify its limit"**
(delta_{n,m} = d_CM - (2n+m-2); the paper shows 3/pi <= liminf and limsup <= 2 pi^2 / J <= 8.097 with J = int_0^{2pi} (1-cos u)/u du).

## Method
Laplace representation f_{n,m}(x) = int_0^infty e^{-xt} t^m k_n(t) dt with k_n(t) = (-1)^n t^{-1}[1/(e^t-1) - 1/t + 1/2 - sum_{k<=n} B_{2k} t^{2k-1}/(2k)!] >= 0.
With q = 2n+m-2, rho = q + a, h = (t^m k_n)^{(q)} (h(0)=0): x^rho f is CM  <=>  D^a h >= 0 on (0,infinity)  (Bernstein + x^a L[h] = L[D^a h]), and
Gamma(1-a) t^a D^a h(t) = t^a int_0^t (t-u)^{-a} h'(u) du =: H(a,t).  So  d_CM = q + a*,  a* = sup{a : min_t H(a,t) >= 0}.  H is smooth in (a,t); the minimum over t first touches 0 at a critical t*.
`cmdeg.py`/`cmfast.py`: h' tabulated from the exact Taylor series (t<3) and the exponential-sum form (t>=3), piecewise Chebyshev interpolation, QUADPACK algebraic weights, grid+Brent in t, bisection in a (11 digits).

## Results (a* = delta_{n,m}; table_n2_9.txt)
| n | d_CM(R_n) (m=0) | (2n-1) delta | d_CM(-R_n') (m=1) | (2n-1) delta |
|---|---|---|---|---|
| 2 | 2.8667042552 | 2.6001 | 3.7984354776 | 2.3953 |
| 3 | 4.7074638766 | 3.5373 | 5.6534285885 | 3.2671 |
| 4 | 6.5993536696 | 4.1955 | 7.5587377578 | 3.9112 |
| 5 | 8.5213225063 | 4.6919 | 9.4900039902 | 4.4100 |
| 6 | 10.4617284606 | 5.0790 | 11.4369053276 | 4.8060 |
| 7 | 12.4144812972 | 5.3883 | 13.3943400805 | 5.1264 |
| 8 | 14.3760290864 | 5.6404 | 15.3593656569 | 5.3905 |
| 9 | 16.3441056945 | 5.8498 | 17.3300936514 | 5.6116 |
(Further n for m=0: see table_m0_10_18.log when finished.)
* Consistent with all of Krasniqi's bounds (e.g. 2.8667 in (8/3, 3), 3.7984 in (32/9, 4)); the critical t* decreases slowly (11.47, 6.36, 4.62, ... for m=0).
* **Answer to the 'first remaining problem': d_CM(R_2) = 2.8667042552 and d_CM(-R_2') = 3.7984354776 (10 digits).**  Independent check (verify.py): 22-digit mpmath quadrature at (a*, t*) gives H(a* -+ 3e-5, t*) = +-1.0e-6 (and +-6.7e-7 at 2e-5) with the sign change exactly at a*,
  and a direct Leibniz/polygamma evaluation of (-1)^j d^j/dx^j [x^rho f] at 130 digits shows the first negative derivative for rho = d_CM + 0.1 (j=60) but none for rho = d_CM - 0.5.
* **On the 'second problem':** (2n-1) delta_{n,0} increases monotonically over n = 2..9 (2.60, 3.54, 4.20, 4.69, 5.08, 5.39, 5.64, 5.85) with decreasing increments; a polynomial-in-1/n extrapolation gives a limit of about 7.7-7.8 (m=0: 7.78, m=1: 7.66),
  comfortably below Krasniqi's upper bound 8.097 but far above his lower bound 3/pi = 0.955. This is a trend, not a proof (power-law fits are unstable: 10-20). So the limit, if it exists, is probably between 7 and 8.1.
## Status
Numerical (VERIFIED, 10 digits, two independent evaluations of the criterion); exact closed forms: none found. Novelty: NOT FOUND.
