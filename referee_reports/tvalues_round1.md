# Referee report, round 1: t({2}^N,1) = I(2N)/(2N)!

## 1. Verdict: COMPLETE MODULO MINOR

The proof is correct. Every displayed identity checks out. The minor points are presentational.

## 2. Issues

1. (minor) Wording of the Tonelli step. The first Tonelli use gives an identity of [0,inf]-valued quantities for each fixed u>0. Finiteness follows only afterwards, from the right-hand side, which is finite for all u. Suggested fix: add "the common value is finite, being equal to the integral below. Hence the left side is an entire power series in u^2 with non-negative coefficients converging for all u."
2. (minor) The coefficient comparison needs a justification. Both sides are power series in u^2 with non-negative coefficients that converge for all u, so equality for all u>0 gives equality of coefficients (identity theorem). The right-hand side's expansion is by Tonelli applied to cosh(u theta)-1 = sum_{N>=1} (u theta)^{2N}/(2N)!, using cot(theta) >= 0 on (0, pi/2). Both facts are true but should be stated.
3. (minor) Unused fact. The identity Gamma(1/2+iu/2)Gamma(1/2-iu/2) = pi/cosh(pi u/2) is not needed for the tail product Q_{2S-1}. It would only matter for the full product (S=0). The proof should say that it is not used, or drop it.
4. (minor) Index bookkeeping. State explicitly that "odd n > m = 2S-1" means n = 2r-1 with r >= S+1. State the telescoping product prod_{r>=R} (r-1/2+a)(r-1/2-a)/(r-1/2)^2 = Gamma(R-1/2)^2/(Gamma(R-1/2+a)Gamma(R-1/2-a)) with R = S+1. Say that convergence holds because the terms are 1 + O(r^-2), or by the Gamma asymptotics. The formula is right, but this is the step a reader will want written out.
5. (minor) Hypotheses of the "classical formula". It requires Re nu > -1 (here nu = 2S-1 >= 1) and a complex. State the reference (G&R 3.631.9; DLMF 5.12.1 is an equivalent form). Say that cos(i u theta) = cosh(u theta).
6. (minor) Convergence at the endpoints of f. f(cos theta) = cot(theta) is used for theta in (0, pi/2], where x = cos theta is in [0,1) and the binomial series converges. The integrand (cosh(u theta)-1)cot(theta) is O(theta) near 0, so it is integrable. The term-by-term integration over S is justified by non-negativity. State this.
7. (minor) The definition of t({2}^N,1) should be tied to the claim "e_N{1/n^2 : n odd > m}". With n_1>...>n_N>n_{N+1}=m, the exponents are 2 on the N larger indices and 1 on the smallest. This is correct as written, but say it in one sentence.

No fatal or major issues. No uncovered cases: N>=1 and all odd m>=1 (S>=1) are covered.

## 3. GIVEN formula

Correct. I tested it at 40 digits against direct quadrature of int theta^{2N} cot theta d theta / (2N)! for N=1..5. For N=1..4 the values agree to all 40 digits (e.g. N=1: 0.32923616284981706824..., which is (pi^2/8)ln2 - 7 zeta(3)/16). For N=5 they agree to about 36 digits. The difference there, about 1e-37 relative to 5e-7, is quadrature noise, not an error. The proof does not need the GIVEN formula. It needs it only for the final "hence equals the closed form" parenthetical. The main equality t({2}^N,1) = I(2N)/(2N)! is independent of it.

## 4. Steps verified, and how

- Generating-function setup. Re-derived by hand: t({2}^N,1) = sum_{m odd} (1/m) e_N{1/n^2, n odd > m}, and the y^N coefficient of Q_m is e_N. Brute-force numerics with the exact tail p1 = pi^2/8 - partial sums, and e_2 = (p1^2-p2)/2, give t(2,1) ~ 0.329205 (truncated at m < 8000, tail error about 3e-5) against the target 0.3292362. For N=2, 0.0233373498 against the target 0.0233373503. These agree up to the truncation error.
- Gamma product formula. Re-derived by hand. Checked numerically at S=2, u=1.5: nprod gives 1.310215913727989789607, and the Gamma ratio gives the same to 24 digits.
- Classical cosine-power integral and the duplication formula. Re-derived by hand. The constant c_S = 2 Gamma(S+1/2)/(sqrt(pi) Gamma(S)) is correct. The Wallis normalisation at u=0 is consistent.
- f'(x) = (1-x^2)^{-3/2}. Re-derived by hand, with the binomial coefficients Gamma(j+3/2)/(Gamma(3/2) j!) and Gamma(3/2) = sqrt(pi)/2. Then f = x/sqrt(1-x^2), so f(cos theta) = cot theta.
- Full generating-function identity at u=3/2. sum_{S>=1} (Q_{2S-1}-1)/(2S-1) = int_0^{pi/2} (cosh(u theta)-1) cot(theta) d theta. Both sides equal 0.8707893413935717649617537 (25 digits, mpmath nsum and quad).
- Tonelli/Fubini steps. Checked that every term is non-negative for u>0 (e_N >= 0, cosh-1 >= 0, c_S > 0, cos^{2S-1} >= 0, cot >= 0 on (0, pi/2)).
