# Independent verification: half-iterate tetration and C(x0) (fresh code, scratch /tmp/verify_tc)

## Task 1: T(b,1/2) = f^[1/2](1), f(x)=b^x, regular (Koenigs) iteration
Method A: phi(x)=lim lam^-n (f^n(x)-L); half-iterate g(x)=psi(sqrt(lam) phi(x)), psi(s)=lim f^{-n}(L+lam^n s) (f^{-1}=log_b). 500-digit arithmetic, n=150/200/300 compared.
Method B (independent): power series of psi=phi^-1 from psi(lam t)=f(psi(t)) (120 terms, 80 digits), Newton for phi(1), then psi(sqrt(lam) phi(1)). Agrees with A to all 50 digits printed.

| b | L | lam | T(b,1/2) |
|---|---|-----|----------|
| 4/3 | 1.57167727089176302049718642361 | 0.452143374515501488 | 1.20583743404309559494183930650711256690056498925584326509378 |
| 5/4 | 1.35220351364068086116443136121 | 0.301735494133334001 | 1.16359536196500884902594327335843631288394241874945448027187 |
| 6/5 | 1.25773454137652642105098282263 | 0.229312119617298837 | 1.13626248672712808418530091864742602558935546503741898785324 |

Convergence: n=200 vs n=300 differ by 2e-71 (4/3, precision-limited by lam^n vs 500 digits; truly converged to ~1e-70 at n=200, 4/3 worst), <1e-107 (5/4), <1e-131 (6/5). So all values are correct to >= 70 digits (4/3), 100+ (others); the digits listed are the n=300 values (60 digits shown are safe for 4/3 to ~70).
Checks: g(g(x))-b^x at x in {1,0.3,2,3.7,-1}: |residual| <= 4e-87 (4/3), 3e-131 (5/4), 3e-161 (6/5) (residual limited by n, as expected). g(L)=L, g increasing on [-2,3] (21 sample points, all three bases), analytic by construction (composition of analytic maps, phi analytic near L and extended by f^n).
Caveat: tetration here is b^^0=1, b^^1=b, b^^(1/2)=g(1); g(g(1))=b verified.

Is this canonical? For 1<b<=e^{1/e}, the regular iteration at the attracting fixed point (Koenigs 1884; Szekeres 1958 for Abel/regular iteration; Kneser-type constructions are for b>e^{1/e}) is the standard definition: it is the unique real-analytic iteration that is analytic at L (Szekeres), the one used by e.g. Kouznetsov / Trappmann--Kouznetsov "Uniqueness of analytic Abel functions in absence of a real fixed point" and in Henryk Trappmann's treatments. Other (non-analytic-at-L) iterations exist (add 1-periodic functions to the Abel function), so "canonical" = regular, not unique among all solutions of g(g)=f. From memory, no document opened.

## Task 2: x_{n+1}=x_n+1+1/x_n^2, C(x0)=lim(x_n-n), x0=2
Asymptotics (sympy, ansatz with log terms, all log coefficients came out 0): y_n=x_n-n = C - 1/n + (C-1/2)/n^2 + (-C^2+C-5/6)/n^3 + (C^3-3C^2/2+5C/2-5/4)/n^4 + ... (through 1/n^9). Fixed point C = y_N - E(N;C), derivatives by implicit differentiation using exact orbit recursions p_{n+1}=(1-2/x_n^3)p_n, q_{n+1}=(1-2/x_n^3)q_n+6p_n^2/x_n^4.

| N | C(2) | C'(2) | C''(2) |
|---|------|-------|--------|
| 1000 | 2.598786855824871348259966500070 | 0.66156132404868607056775027426 | 0.374626421983017341116776275599 |
| 3000 | 2.598786855824871348259966495188 | 0.66156132404868607056775026357 | 0.374626421983017341116776248793 |
| 10000 | 2.5987868558248713482599664951883 | 0.66156132404868607056775026356993 | 0.37462642198301734111677624879289 |
| 30000 | 2.5987868558248713482599664951883 | 0.66156132404868607056775026356993 | 0.37462642198301734111677624879289 |

Final (N=1e4 vs 3e4 agree to ~35 digits for C, ~33 for C', ~35 for C''):
C(2)  = 2.59878685582487134825996649518832
C'(2) = 0.661561324048686070567750263570
C''(2)= 0.374626421983017341116776248793
Matches the expected magnitudes (not tuned). Finite differences (h=1e-15, 70 digits): C'=0.6615613240486860705677503, C''=0.3746264219830173411168 (agree to 25 and 22 digits).

Exact series (derived, verified): C'(x0)=prod_{k>=0}(1-2/x_k^3) and, with P_k=prod_{j<k}(1-2/x_j^3),
C''(x0) = C'(x0) * sum_{k>=0} 6 P_k / (x_k^4 - 2 x_k)   [from q_n/p_n recursion: q_{n+1}/p_{n+1}=q_n/p_n+6p_n/(x_n^4(1-2/x_n^3))].
Summed 2e5 terms: C' ~ 0.66156132406522 (tail 1-2*sum x^-3 ~ 1-2.5e-11 predicts 0.6615613240487 -> consistent), C'' ~ 0.37462642199238 (tail ~1e-11, consistent). Terms decay like k^-3 (product) and k^-4 (sum), so convergent; tail needs correction for high precision, hence the asymptotic method above is the one used for digits.
Caveats: none of the interchanges of limit and derivative is proved rigorously here (uniform convergence of p_n, q_n is evident from the summable terms); results are numerical, not interval-certified.
