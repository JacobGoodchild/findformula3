# Referee report, round 1: Painleve series polynomiality (Conjecture 7.1)

## 1. Verdict: COMPLETE MODULO MINOR

I found no fatal or major errors. The proof is correct as written. The points below are expository gaps that should be filled in, not mathematical errors.

## 2. Issues

1. (minor) Sign and factor convention for E_s. Step 2 defines L_s p_s = rho_s, so rho_s = -(q^s-coefficient of the residual of T). The text then says "E_s = e^{-sx} rho_s is the q^s-coefficient of the residual". Two things are off. (i) The sign: E_s = -e^{-sx} rho_s, with the residual defined as in Step 3. (ii) The e^{-sx} factor is not part of the q^s-coefficient; it enters only when q is replaced by eps e^{-x}. This does not affect the argument, because only [x^2]E_s = 0 matters. Fix: write E_s = -e^{-sx} rho_s, or define rho_s with the opposite sign.
2. (minor) a_2 = O(eps) is asserted without a reason. The reason is a_2 = T''(x_0)/2, and T'' = sum_{j>=1} eps^j (...) because p_0'' = 0. Add one line. The same applies to a_1 = 1 + O(eps), so that a_1 and 1 + a_1 (= 2 + O(eps)) are invertible in C[[eps]], which is what makes the division legitimate.
3. (minor) Existence of x_0 is stated, not argued. Add: T(x) = x + eps R(x, eps) with R entire in x and formal in eps, so the fixed-point iteration x_0 = -eps R(x_0, eps) converges eps-adically (formal implicit function theorem). For the Taylor shift E(x_0 + xi) = sum E^{(m)}(x_0) xi^m / m!, note that E = sum_{j>=s} eps^j e^{-jx} c_j(x) with c_j polynomial, so E_s^{(m)}(x_0) = E_s^{(m)}(0) + O(eps) holds eps-adically, and the O(eps^{s+1}) terms stay O(eps^{s+1}) after shifting.
4. (minor) Line 24 says the conditions "are necessary and sufficient". The proof only handles pi_0 = 0. With pi_0 != 0 the s=1 obstruction is -(pi_0/2 - pi_1 + pi_2) (I checked this: P = 2 + t + t^2 gives no polynomial p_1). Necessity of pi_0 = 0 is therefore not shown here. It is only needed for the paper's "iff" claim, and could be dropped or justified separately. The remark that pi_0 = 0 is "needed for e_0 = 1 - a_1^2" is cosmetic: with pi_0 != 0, e_0 just acquires a term -q_0 pi_0.
5. (minor) Step 1 should say explicitly why p_s enters only through L_s. In u''u - u'^2, p_s appears only multiplied by p_0 = x and its derivatives. In q P(u) it first appears at order q^{s+1}. Cross terms p_j p_{s-j} have 1 <= j <= s-1 and use only lower p's. pi_0 enters rho_1 only.
6. (minor) The induction should state that p_s is unique, since L_s is injective. Hence the polynomials p_1, ..., p_{s-1} used to build T in Step 3 are the ones produced earlier, and the formal series is determined. The proof is also valid in any characteristic-0 coefficient field, with pi_j treated as parameters.
7. (minor, observation) The identity in Step 3 holds as a pure polynomial identity: e2 - (a2/a1) e1 - (q0 pi1 a1/(1+a1)) e0 = a1^2 q0 (pi1 - pi2). It does not need e0 = 1 - a1^2 or any other constraint beyond the three formulas. This could be stated; the cleanest form is "e2 - (a2/a1) e1 - (q0 pi1 a1/(1+a1)) e0 = q0 a1^2 (pi1 - pi2)".

## 3. Steps verified, and how

- Operator L_s: I put u = x + e p(x) q^s with q an independent symbol and d/dx = ∂_x - q ∂_q, and took the coefficient of e q^s in u''u - u'^2 using sympy. This gives exactly x p'' - 2 s x p' + s^2 x p - 2(p' - s p) (difference simplified to 0, symbolic s).
- Identity L_s p = e^{sx} x^3 (x^{-2} (e^{-sx} p)')': sympy confirms the difference is 0 for symbolic s. The kernel is {e^{sx}, x^3 e^{sx}}, since (e^{-sx} p)' = c x^2. Neither is a polynomial for s >= 1. I checked L_s e^{sx} = 0 by hand.
- Degree: L_s x^n has leading term s^2 x^{n+1}, so L_s raises the degree by exactly 1 for s != 0.
- Codimension and necessity: the image of {deg <= n} has dimension n+1 inside {deg <= n+1}, of dimension n+2, so the codimension is 1. The functional phi_s(rho) = [x^2](rho e^{-sx}) vanishes on the image, because the residue of a derivative of a Laurent series is 0. It is nonzero on the constant 1 (value s^2/2), hence on every space {deg <= n+1}, n >= 0. So image = ker phi_s. Sufficiency is correct, including s = 1; there is no special s.
- Step 3 formulas: I re-derived the Taylor coefficients of E(x_0 + xi) = T''T - T'^2 - (q_0 e^{-xi} P(T) - 1) with sympy, using T up to a_5 xi^5 and P up to cubic. e0, e1, e2 match the paper exactly. a_3 (and a_4, a_5) do not appear. pi_3 does not appear (confirmed by taking the difference with pi_3 symbolic). The polynomial identity of item 7 was checked symbolically, and it becomes 0 when pi_2 = pi_1.
- Order counting: e_m = E^{(m)}(x_0)/m! = eps^s E_s^{(m)}(0)/m! + O(eps^{s+1}), by item 3. With e0, e1 = O(eps^s) and a_2, q_0 = O(eps), the identity gives e2 = O(eps^{s+1}), so [x^2]E_s = 0. The division by a_1 and 1 + a_1 is legitimate (both are units in C[[eps]]).
- Base case s = 1: T = x, x_0 = 0, a_1 = 1, a_2 = 0, E = -eps e^{-x} P(x). Then e_2 = -eps(pi_2 - pi_1) = 0, consistent with the identity.
- Brute force with sympy, solving L_s p_s = rho_s by linear algebra with free polynomial ansatz:
  - P = t + t^2 + t^3: p_1..p_5 are all polynomials, of degrees 2, 3, 4, 5, 6 (p_1 = x^2 + 3x + 3).
  - P = 3t + 3t^2 - 2t^3 + t^4 - 5t^5 (pi_0 = 0, pi_1 = pi_2): p_1, p_2, p_3 are polynomials, of degrees 4, 7, 10.
  - P = t + t^2: p_1..p_5 degree 1 (x + 1, (2x+3)/4, ...). (This P has pi_1 = pi_2, as required.)
  - Negative controls: P = t + 2t^2 and P = 2 + t + t^2 give no polynomial p_1, as predicted.
  This is numerical/algebraic evidence only; the proof itself is the argument above.
