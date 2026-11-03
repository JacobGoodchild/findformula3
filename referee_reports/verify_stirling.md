# Independent check: CM-degrees of Stirling remainders R_2 and -R_2'

Code (written fresh, no repo files read): /tmp/verify_cm/{a,d,e,f,g,h}.py

## Result
- d_CM(R_2)   = 2.86670425523798  (agreement across quadrature sizes 300/500/900: 2.8667042552379836 / ...983 / ...978; ~14 digits)
- d_CM(-R_2') = 3.79843547761568  (3.798435477615688 / ...6817 / ...6777; ~14 digits)
Both lie inside the paper's bounds: 8/3=2.667 < 2.86670 < 3 and 32/9=3.556 < 3.79844 < 4.

## Method
R_2(x)=int_0^inf e^{-xt} h(t) dt with h(t)=t^{-1}(1/(e^t-1)-1/t+1/2-t/12+t^3/720)=sum_{k>=3}B_{2k}t^{2k-2}/(2k)! ~ t^5/30240
(from the Binet integral; sign (-1)^2=+, density >=0). -R_2'(x)=int e^{-xt} t h(t) dt, density ~ t^6.
Criterion: for rho<6 (resp. <7), x^rho f(x)=L[D^rho h], D^rho = Riemann-Liouville derivative; since h vanishes to order 5 at 0, with m=ceil(rho), a=m-rho,
D^rho h = I^a[h^(m)] = (1/Gamma(a)) int_0^t (t-s)^{a-1} h^(m)(s) ds (no boundary terms; L[I^a g]=x^{-a}L[g], L[u^(m)]=x^m L[u] when u,..,u^(m-1)->0 at 0).
By Bernstein + uniqueness of the Laplace transform, x^rho f is CM iff Phi_rho(t):=D^rho h(t) >= 0 for all t>0. (m=3 for R_2, m=4 for -R_2'; for the second use density t*h.)
d_CM = sup of rho such that Phi_rho>=0 on (0,inf). Numerics: substitution u=(T-s)^a removes the endpoint singularity, Gauss-Legendre in u;
h^(m) from Taylor series (s<3, 45 terms, radius 2pi) or closed form (3<=s<=40) or purely algebraic part (s>40, exp terms < 4e-18 relative).
Phi_rho(T) has a single negative-going dip near T~11.47 (R_2) and T~8.04 (-R_2'); I minimised over T (bounded Brent) and solved min_T Phi_rho(T)=0 in rho by Brent. At the root Phi~1e-19, Phi_T=0 (double root), i.e. a genuine tangency.
For rho below the root: min Phi>0 over T in [0.05,3000] (log grid) and at the local dip; large T behaves like t^{2-rho}/(360 Gamma(3-rho))>0, small T ~ t^{5-rho}>0.

## Independent sanity checks
1. mpmath (40 digits) evaluation of Phi at the critical (rho,T): ~2e-19 (R_2, tanh-sinh with same substitution); at rho_c +/- 1e-6 Phi = -/+ 4.9e-10 (R_2), -/+ 3.08e-9 (-R_2'): sign change linear in rho, as expected. (Note: naive mp quad without the substitution/splitting gave an inaccurate 9e-11 -- quadrature artefact, not a real discrepancy.)
2. Direct CM test not using the Laplace representation: exact derivatives of F=x^rho f via Leibniz with polygamma psi^(n-1) (mp.dps=300), tested (-1)^j F^(j)(x) on x=c*j/T, c in {.6,.8,1,1.25,1.6}, j up to 200:
   - R_2 at rho_c-0.02, -0.003: all positive, all j. At rho_c+0.02: negative already at j=20 (x~1.7); at rho_c+0.003: negative at j=120,200 (ratio min/max -4e-30, -1e-46).
   - -R_2' at rho_c-0.02,-0.003: positive; at rho_c+0.02: negative at j=60,120,200. (+0.003 not yet violated at j<=200; violations get sharper with j, as Post-Widder predicts.)
   This confirms the sharp transition and the location x~j/T.

## Caveats
- Evaluation is double precision; ~1e-14 level stability across quadrature sizes, so quote 12-13 digits safely: 2.866704255238, 3.798435477616.
- "Sup" assumes positivity of Phi for all rho below root (monotone in rho is plausible but I verified only on grids: rho_c-1e-6 and the scans at coarser steps 2.66..2.86, 3.5..3.75). Not a rigorous proof; no interval arithmetic used.
- Definitions used exactly as given (R_n with (-1)^n factor; -R_2' = int e^{-xt} t h dt).

## Follow-up: further n

Same method generalised: density h_n(t)=(-1)^n sum_{k>n} B_{2k} t^{2k-2}/(2k)! (times t for -R_n'), m=ceil(rho), Phi=I^{m-rho}[h^(m)]. Code /tmp/verify_cm/{n,n2,solve,solve2}.py, mpmath only (dps 50-60). h^(m) from Taylor series (s<4) or closed form with exponential sum (s>=4); the critical (rho,T) is found by 2D Newton on Phi=0, Phi_T=0 (Phi_T=I^a[h^(m+1)]), so each root is a genuine tangency of a dip (dip location T* given). Gauss-Legendre node count NG in the u=(T-s)^a substitution varied to test convergence.

| function | d_CM (this check) | tested value | dip T* | (2n-1)(d-(2n-2)) |
|---|---|---|---|---|
| R_3 | 4.70746387663468 | 4.7074638766 | 6.3646 | 3.53732 |
| R_5 | 8.5213225063384 | 8.5213225063 | 3.6639 | 4.69190 |
| R_10 | 18.317174514704 (NG=300; ±3e-13) | 18.3171745147 | 1.85666 | 6.02632 |
| R_22 | 42.1635160400 (NG=450: 42.16351603998; ±3e-11) | 42.1635160400 | 0.86652 | 7.03119 |
| -R_3' | 5.65342858845089 | 5.6534285885 | 5.3286 | |
| -R_5' | 9.49000399017 | 9.4900039902 | 3.3288 | |
(For reference n=2: 2.866704255238, factor 2.60011.)

All six agree with the tested values to the quoted digits (>= 10 digits; differences < 1e-10). Convergence in NG: n=3,5 and -R_3', -R_5' identical to 1e-14 between NG=80 and 120; n=10: 18.31717451489 (NG 80), ...4729 (120), ...470578 (200), ...470397 (300); n=22: 42.1635160419 (80), ...4030 (120), ...40017 (200), ...3998836 (300), ...3998351 (450). So 9+ digits for all; n=22 not worse than ~1e-10.
Sign checks (n=10, 22, NG=150): at rho_c-0.01 Phi>=0 on a T grid 0.2..40; at rho_c+0.01 Phi<0 near the dip for n=10 (T=1.8); for n=22 the dip is narrow (T~0.867) and my 0.2-spaced grid missed it, but the Newton tangency (Phi=Phi_T=0 at T*=0.8665 with Phi>0 at neighbours in the earlier scan at rho_ref+0.03 being negative at T=0.9) supports it. The independent Leibniz/polygamma derivative test was not repeated for these n. As before positivity below the root is checked on grids only, not proved. Observation: (2n-1)(d-(2n-2)) increases with n (2.60, 3.54, 4.69, 6.03, 7.03), i.e. d_CM-(2n-2) ~ O(1/ sqrt?)-like slowly growing numerator; no limit evident from these five values.
