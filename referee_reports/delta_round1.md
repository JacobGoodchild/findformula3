# Referee report, delta (round 1)

## (1) Verdict: COMPLETE MODULO MINOR

The theorem and proof are correct. The minor points concern hypotheses that should be stated and a few notational ambiguities.

## (2) Issues

1. (minor) Hypotheses on the orbit are not stated.
   - The proof needs x_n > 0 for all n and x_n -> 0, so that ln x_n is real and the expansion applies. It also needs the orbit to stay in the region where the expansion holds.
   - "0 < x < x*" is only asserted to be in the basin.
   - Fix: define the domain explicitly as {x > 0 : x_n > 0 for all n and x_n -> 0}. Say that gamma < 0 makes the positive real axis an attracting direction.

2. (minor) The GIVEN expansion is legitimate and standard, but the proof should say exactly what it uses.
   - It uses only the existence of one solution g of g(theta(x)) = g(x) + 1 on the real basin with g = A x^-tau + a ln x + beta + O(x^tau) as x -> 0+.
   - Nothing else is needed: no analyticity beyond the expansion, no uniqueness, no differentiability of the remainder.
   - Existence is Fatou-coordinate theory. The formal series is generally divergent, but an actual solution on an attracting petal has it as an asymptotic expansion. g is then extended to the whole basin by g(x) = g(x_n) - n.
   - The ln x branch is the real one on x > 0.
   - Uniqueness up to an additive constant follows in two lines and makes "g_EJ" and delta well defined. If g1 and g2 both have the expansion, h = g1 - g2 satisfies h(theta(x)) = h(x) and h = const + O(x^tau). Hence h(x) = h(x_n) -> beta1 - beta2, so h is constant.
   - Fix: add this remark. It shows delta is independent of x and independent of the choice of g, because beta = 0 fixes the constant.
   - Also say that A and a are forced by the formal solution (Item 1), so the expansion's coefficients are not extra assumptions.

3. (minor) Notation in Item 1.
   - "c" is used where c_2 is meant. The expansion theta = x(1 + gamma eps + c eps^2 + ...) has c = c_2, and c_1 = gamma.
   - Fix: write c_2 throughout.
   - Also state that the b_1 x^tau term first enters at eps^2 (b_1 (theta^tau - x^tau) = b_1 tau gamma eps^2 + ...). The proof says this parenthetically, which is correct.
   - The step "eps^1 term gives A(...) + a gamma = 0" should also say that a ln(theta/x) = a gamma eps + O(eps^2). It does, in the line before.

4. (minor) Error terms in Item 2.
   - The chain is correct, but the passage from "x_n^-tau = kappa[n + g_0 - beta - a ln x_n] + o(1)" to the final bracket should say that the o(1) enters relative size o(1/n). So it contributes o(n^(-1-1/tau)), which is negligible after multiplying by n^(1+1/tau).
   - The O(ln^2 n / n^2) term is the second-order term of (1 + delta_n/n)^(-1/tau), where delta_n = O(ln n). This is fine.
   - Replacing ln x_n by -(1/tau) ln(kappa n) + o(1) is justified because x_n^-tau ~ kappa n.
   - Fix: add a one-line remark that the o(1) in the log replacement is exactly what is used, and that the only things needed are x_n -> 0 and x_n^-tau ~ kappa n.

5. (minor) The statement that the ML formula "reduces to" the explicit Finch formulas depends on the general formula in item 2 being the definition. This is a transcription issue: the packet takes item 2 as the definition of g~.
   - I checked consistency with both explicit examples. For tau = k, gamma = -1, c_2 = 0: kappa = k, a = (k+1)/2, a/tau^2 = (k+1)/(2k^2), and the prefactor is -k. This matches the displayed formulas, and for k = 2 the 3/8 and -2 match.
   - Nothing to fix. Just ensure the final write-up quotes the source formula verbatim.

6. (cosmetic) tau = 1 is included. There a = 1 - c_2/gamma^2. For theta = x/(1+x), gamma = -1, c_2 = 1, so a = 0, which is correct since 1/x is exact.

No fatal or major issues.

## (3) Steps verified

- Re-derived A and a symbolically with sympy for tau = 1..5, for general gamma and c_2.
  - Result: A = -1/(tau gamma) = 1/kappa, and a = (tau+1)/2 - c_2/gamma^2 (difference 0 in each case).
  - The b_1 and b_2 terms did not affect the eps^0 and eps^1 coefficients.
  - Script: /tmp/claude-0/-home-user-findformula3/311c4a72-0704-5321-ad61-ef26a3a0bc55/scratchpad/referee/chk.py
- Re-derived the asymptotics of x_n by hand, with all error terms (see Issue 4). The result is g~ = g_0 - beta + (a/tau) ln kappa.
- Checked the orientation: A > 0 because gamma < 0, so g -> +infinity as x -> 0, consistent with g(theta(x)) = g(x) + 1.
- Numerical test with theta = x(1-x^2) and x_0 = 1/2, 40 digits, N = 4e5 steps.
  - g_EJ from A x_N^-2 + a ln x_N - N with Richardson extrapolation: 1.18935108877 (two extrapolations agree to about 1e-10).
  - ML limit with n^(3/2) scaling: raw values drift (1.7085, 1.7088, 1.7090 for n = 1e5, 2e5, 4e5), consistent with a ln^2 n / n error. A least-squares fit of c0 + (c1 ln^2 n + c2 ln n + c3)/n gives c0 = 1.7092115.
  - delta = g_EJ - g~ = -0.5198604 numerically, versus -(3/4) ln 2 = -0.5198604. Agreement to about 7 or more digits.
  - Script: /tmp/claude-0/-home-user-findformula3/311c4a72-0704-5321-ad61-ef26a3a0bc55/scratchpad/referee/num.py
- Checked the explicit ML examples in the packet (tau = 2 and general k) against the general formula: the constants match.
- Checked that the uniqueness-up-to-a-constant argument (Issue 2) is valid.
