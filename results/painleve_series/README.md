# Exponential-polynomial expansions for  u'' u - (u')^2 = e^{-x} P(u) - 1   (arXiv:2606.21145, R. Habib & R. Hildebrand)

Ansatz: u(x) = sum_{k>=0} p_k(x) e^{-kx}, p_0(x) = x.  Write q = e^{-x}, P(t) = sum pi_j t^j.

**Conjecture 7.1 of the paper** (stated there after checking s <= 4 symbolically and s <= 10-20 numerically):
if pi_0 = 0 and pi_1 = pi_2, then for all k there are POLYNOMIALS p_k such that the formal series solves the ODE.

## Result 1: Conjecture 7.1 is TRUE.   Label: PROVED  (every step also machine-checked, see verify.py)

**Step 1 (the equation for p_s).** Collect the coefficient of q^s. The only terms containing p_s are L_s p_s with
L_s p = x p'' - 2 s x p' + s^2 x p - 2 (p' - s p). So  L_s p_s = rho_s, where rho_s is a polynomial built from p_1..p_{s-1} (and P).

**Step 2 (when is L_s p = rho solvable in polynomials?).** One checks L_s p = e^{sx} x^3 ( x^{-2} (e^{-sx} p)' )'.
(a) Necessity: a derivative of a Laurent series has no x^{-1} term, so Res_{x=0} [ e^{-sx} L_s p / x^3 ] = 0, i.e. phi_s(rho) := [x^2]( rho(x) e^{-sx} ) = 0.
(b) Sufficiency: L_s is injective on polynomials (kernel of the operator is spanned by e^{sx} and x^3 e^{sx}) and raises the degree by exactly 1,
    so L_s(polys of degree <= n) has codimension 1 in polys of degree <= n+1. phi_s is a nonzero functional on every such space and vanishes on the image, so image = ker phi_s.
    (verify.py checks that the explicit solvability residual of the recursion equals (2/s^2) * phi_s(rho).)
Hence: p_s exists  <=>  [x^2] E_s(x) = 0, where E_s(x) = e^{-sx} rho_s(x) is the q^s-coefficient of the residual of the truncated series T = sum_{j<s} p_j q^j.

**Step 3 (the obstruction always vanishes).** Put eps for the formal parameter (replace q by eps e^{-x}); T = sum_{j<s} p_j eps^j e^{-jx} solves the ODE up to O(eps^s), residual
E(x) = T''T - T'^2 - (eps e^{-x} P(T) - 1) = eps^s E_s(x) + O(eps^{s+1}).
T has a (formal-power-series) zero x_0 = O(eps) with T'(x_0) = a_1 = 1 + O(eps). Expand T = a_1 xi + a_2 xi^2 + ..., xi = x - x_0, and E(x_0 + xi) = sum e_m xi^m. With q_0 = eps e^{-x_0} one computes (pi_0 = 0):
 e_0 = 1 - a_1^2,   e_1 = -2 a_1 a_2 - q_0 pi_1 a_1,   e_2 = -2 a_2^2 - q_0 pi_1 a_2 - q_0 pi_2 a_1^2 + q_0 pi_1 a_1
 (a_3 cancels exactly -- this is the "resonance" of the equation at a simple zero of u -- and pi_3, pi_4, ... do not enter).
Eliminating a_2 and using pi_2 = pi_1 gives the identity (checked by sympy)
 **e_2 = (a_2/a_1) e_1 + (q_0 pi_1 a_1/(1 + a_1)) e_0.**
Now a_2 = O(eps) and q_0 = O(eps), while e_m = eps^s [x^m]E_s / m! + O(eps^{s+1}) (because x_0 = O(eps)). Comparing the coefficient of eps^s gives [x^2] E_s = 0. So p_s exists. Induct from s = 1,
where the obstruction is [x^2](e^{-x} P(x)) = pi_2 - pi_1 = 0 (this is where pi_1 = pi_2 comes from; pi_0 = 0 is needed for e_0 = 1 - a_1^2 / existence of a zero with slope +-1).
(If pi_1 != pi_2 the s=1 obstruction is pi_2 - pi_1 != 0: the conditions in the paper are necessary and sufficient.)

## Result 2 (towards Conjecture 7.2, nonnegativity when all pi_j >= 0): reduction + strong evidence.   Label: PARTIAL
* **Lemma B (proved).** Solve L_s p = rho by the top-down recursion  s^2 a_{m-1} = rho_m + 2 s (m-1) a_m - (m+1)(m-2) a_{m+1}  (m = D, D-1, ..., 1).  If rho_m >= 0 for all m >= 1 then all a_m >= 0.
  Proof: show by downward induction a_j >= (j/s) a_{j+1}.  Given it for j, a_{j-1} >= a_j [2 s (j-1) - (j+1)(j-2) s/j]/s^2 = a_j (j^2 - j + 2)/(s j) >= ((j-1)/s) a_j.  (The m = 0 equation is the consistency condition, which holds by Result 1.)
* Hence **Conjecture 7.2 follows once every rho_s (the right-hand side of L_s p_s = rho_s, built from p_1..p_{s-1}) has nonnegative coefficients (statement (A))**.
  (A) is NOT proved: rho_s = [q^{s-1}]P(u) - [q^s]N(v) with N(v) = v v'' - v'^2 sign-indefinite. But (A) holds in all 396 (P, s) cases tested (s <= 12, exact rational arithmetic, `rhs_positivity.py`),
  and symbolically p_1..p_4 (and the consistency condition) are polynomials in x, pi_1, pi_3, pi_4 with all coefficients positive (P = pi_1(t + t^2) + pi_3 t^3 + pi_4 t^4, sympy), which suggests a positive combinatorial formula.
* Useful identity (checked): e^{sx} [q^s] N(v) = (1/2) sum_{i+j=s} [ p_i'' p_j + p_i p_j'' - 2 p_i' p_j' + 2 (j-i)(p_i' p_j - p_i p_j') + (i-j)^2 p_i p_j ].

## Other (non-proof) data
* Exact rational recursion (series.py): the p_k exist and, in all cases tested, have only nonnegative coefficients when all pi_j >= 0 (Conjecture 7.2):
  P = t^3 up to k=40, t^4 up to 30, t^6 up to 20, t+t^2+t^3 up to 30, several random P to k=14. The authors' numerics reached k ~ 10-20 and were unstable; this is exact.
  NOT proved (no counterexample found, no proof found).
* P = t^2 + t has p_k = (x + H_k)/k!  (checked to k = 12), i.e. u = x e^q + sum_k H_k q^k/k!.  (Explicit solution; the paper's Section 4 treats this case.)
* Degrees (observed): deg p_k = (d-2)k + 1 for P = t^d (d = 3, 4, 6).
