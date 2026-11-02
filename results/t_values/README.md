# Proof of Conjecture 4.5 of Chavan-Kobayashi-Layja, "Integral evaluation of odd Euler sums, multiple t-value t(3,2,...,2) and multiple zeta value zeta(3,2,...,2)" (arXiv:2111.07097)

**Who asked.** Section 4: after Hoffman's evaluations of t(2,1), t(2,2,1), t(2,2,2,1) they observe "This pattern seems to continue further. However, we have not figured out why yet." and state
**Conjecture 4.5:**  t({2}^N, 1) = I(2N)/(2N)!  (and hence the explicit closed form below), where t(s_1,...,s_k) = sum_{n_1>...>n_k>=1, n_i odd} prod n_i^{-s_i} (Hoffman's multiple t-values) and I(n) = int_0^1 arcsin^n(x)/x dx = int_0^{pi/2} theta^n cot(theta) dtheta.
(The authors proved the closed form (2.3) for I(2N); Hoffman proved N = 1,2,3 case by case.)

## Theorem (PROVED).  For every N >= 1:
  t({2}^N, 1) = (1/(2N)!) int_0^{pi/2} theta^{2N} cot(theta) dtheta = 2^{-2N} [ sum_{j=0}^{N-1} (-1)^j pi^{2N-2j} eta(2j+1)/(2N-2j)! + (-1)^N 2 (1 - 2^{-2N-1}) zeta(2N+1) ],  eta(1) = ln 2, eta(s) = (1-2^{1-s}) zeta(s).
### Proof
Fix u > 0 and put Q_m = prod_{n odd > m} (1 + u^2/n^2) (m odd). Since e_N{1/n^2 : n odd > m} is the y^N coefficient of Q_m (y = u^2),
 sum_{N>=1} t({2}^N,1) u^{2N} = sum_{m odd} (1/m) (Q_m - 1)        (all terms >= 0, so the rearrangement is justified by Tonelli).
Write m = 2S-1. A Gamma-function evaluation of the product (k = 2r-1: 1 + u^2/k^2 = (r - 1/2 + iu/2)(r - 1/2 - iu/2)/(r-1/2)^2, and Gamma(1/2+iu/2)Gamma(1/2-iu/2) = pi/cosh(pi u/2)) gives
 Q_{2S-1} = Gamma(S+1/2)^2 / ( Gamma(S+1/2+iu/2) Gamma(S+1/2-iu/2) ).
The classical formula int_0^{pi/2} cos(a theta) cos^nu(theta) d theta = pi Gamma(nu+1) / ( 2^{nu+1} Gamma(1+(nu+a)/2) Gamma(1+(nu-a)/2) ) with nu = 2S-1, a = iu and the duplication formula gives
 Q_{2S-1} = c_S int_0^{pi/2} cosh(u theta) cos^{2S-1}(theta) d theta,   c_S = 2 Gamma(S+1/2)/(sqrt(pi) Gamma(S)),
and at u = 0 (Wallis) 1 = c_S int cos^{2S-1}. Hence Q_{2S-1} - 1 = c_S int_0^{pi/2} (cosh(u theta) - 1) cos^{2S-1}(theta) d theta and, by Tonelli again,
 sum_N t({2}^N,1) u^{2N} = int_0^{pi/2} (cosh(u theta) - 1) [ sum_{S>=1} c_S cos^{2S-1}(theta)/(2S-1) ] d theta.
Let f(x) = sum_{S>=1} c_S x^{2S-1}/(2S-1). Then f'(x) = sum_S c_S x^{2S-2} = (2/sqrt(pi)) sum_{j>=0} Gamma(j+3/2)/j! x^{2j} = (1-x^2)^{-3/2} (binomial series), so f(x) = x/sqrt(1-x^2), i.e. f(cos theta) = cot(theta).
Therefore sum_{N>=1} t({2}^N,1) u^{2N} = int_0^{pi/2} (cosh(u theta) - 1) cot(theta) d theta = sum_{N>=1} u^{2N} int_0^{pi/2} theta^{2N} cot(theta) d theta/(2N)!, and comparing coefficients gives the first equality. The second is the authors' closed form (2.3) for I(2N). []

## Checks (verify.py)
The Gamma/integral/product forms of Q_{2S-1} agree numerically (S = 1,2,5), the series for f matches x/sqrt(1-x^2), the identity itself is confirmed by direct nested-sum numerics (conj45.py: N = 1..4 agree to 19-32 digits with Richardson extrapolation),
and the closed form is checked for N = 1..4 (20 digits). Examples: t(2,1) = (pi^2/8) ln 2 - 7 zeta(3)/16, t(2,2,1) = I(4)/4!, ... (Hoffman's values).
Novelty: NOT FOUND (a quick search found no proof of this specific family; the argument is elementary). Label: PROVED.
