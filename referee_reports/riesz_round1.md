# Referee report, round 1: Riesz-energy proof (Conjectures 5.9 and 5.6)

## (1) Verdict: COMPLETE MODULO MINOR

No fatal or major gaps. Theorem 1 (Conjecture 5.9) and Theorem 2 (Conjecture 5.6: energy, support and masses) follow from the stated GIVEN results. The issues below are omissions of routine justifications that should be written out. Every displayed identity and the key lemma checked out numerically (details in section 3).

## (2) Issues

1. (minor) Theorem 2 never states the step "U(P_N) = max over subsets of at most 3 points of U(subset)". It follows from Bjorck (GIVEN 2). An equilibrium measure mu* of P_N has at most 3 support points S, so U(P_N) = U(S) <= max over triples, and the reverse inequality holds because the maximum is over a larger set. Two-point supports are handled as the degenerate case: U = |p-q|^r/2 <= c_max^r/2. Add this sentence. Also state that "triple" includes 2-point subsets, because Lemma 5.7 is only quoted for 3 distinct points.

2. (minor) The support and mass part of Conjecture 5.6 is established only implicitly. Add an explicit paragraph:
   - The conjectured triple T* = {1, e^{i(pi-pi/N)}, e^{-i(pi-pi/N)}} consists of vertices of P_N, since (N-1)/2 is an integer for odd N.
   - Its sides are a = 2 sin(pi/N) (base) and b = c = 2 sin(theta_N) (legs). So a^r + b^r > c^r holds trivially, and the 3-point branch of Lemma 5.7 applies.
   - The energy is then 2z^2/(4z-x), with x = a^r and z = c^r. This equals 2^{r-1} sin^r(theta)/(1-2^{r-2}cos^r(theta)), using a = 4 sin(theta) cos(theta). I verified this symbolically.
   - Since U(P_N) <= U(T*) (all triples are bounded by U(T*)) and T* is a subset of P_N, we get U(P_N) = U(T*).
   - Hence the measure given by Lemma 5.7 on T* (all three masses positive, e.g. N=7, r=3: 0.4887, 0.2556, 0.2556) attains the maximum. It is therefore an equilibrium measure of P_N, supported on exactly these 3 points. This gives support and masses. Without this paragraph the "support/masses" part is only implied.
   - Note that the conjecture says "an" equilibrium measure. Uniqueness is not claimed and not proved (it is not needed). The proof gives existence of an equilibrium measure with the stated support and masses. State that.

3. (minor) The claim "strictly increasing if r > 2" in Theorem 1 is not justified by the written Lemma, which gives only ">=". Strictness is easy: F is strictly increasing then strictly decreasing, since (B/A)^r is strictly increasing. F(2) = 0 and F(r_1) >= 0, so F > 0 on (2, r_1). Hence t_r > t_2 and d log U/d psi > 0 in the interior of the 3-point branch. Add this, or weaken the claim to "nondecreasing" (which is all that is used).

4. (minor) Boundary and strictness hypotheses of the Lemma (0 < A < B < 1, strict) hold only for 0 < psi < 2pi - 3phi. The endpoints psi = 0 (A = B) and psi = 2pi - 3phi (B = 1) are covered by continuity of U in psi. Also note that the Lemma is applied for r in [2, r_1) (3-point branch, s > 0, i.e. A^r + B^r > 1 means r < r_1). Say so. Also say that phi = 2pi/3 gives the degenerate interval {0}, so the claim is trivial there.

5. (minor) The statement "a 3-point stretch can never be followed by a 2-point stretch" should be made explicit. Suppose the branch switches at psi_0 (s = 0). Then U(psi_0) = z/2. But before psi_0, U > z/2 (since s > 0) and U is nondecreasing there, so U(psi_0) > z/2 by continuity, a contradiction. The packet's formula U - z/2 = (z/2) s^2/D is correct (verified). Also note the 2-to-3-point switch is the only possibility, and U is continuous at s = 0.

6. (minor) Reduction of an arbitrary acute triple to the Conjecture 5.9 parametrisation is sketched but not spelled out. Write:
   - Label the vertices so that BC is a longest side. Let gamma_A be the inscribed angle at A. Acute implies gamma_A in [pi/3, pi/2), so phi = pi - gamma_A is in (pi/2, 2pi/3].
   - Rotate so B, C = e^{+-i phi}. A lies on the arc through angle 0, so A = e^{i psi} with |psi| < phi.
   - Reflect to get psi >= 0.
   - AC = 2 sin((phi+psi)/2) >= AB. The condition AC <= BC is equivalent to (phi+psi)/2 <= pi - phi, i.e. psi <= 2pi - 3phi. This uses sin symmetric about pi/2 and (phi+psi)/2 < phi.
   - Ties (isosceles, and equilateral triples when 3 | N, e.g. N = 9) are included because the inequalities are non-strict. This is the phi = 2pi/3, psi = 0 case.
   - Chord lengths in P_N are 2 sin(k pi/N) with 1 <= k <= (N-1)/2, so k pi/N < pi/2. Hence c = 2 sin(k pi/N) = 2 sin(alpha/2) with alpha = 2k pi/N, and alpha = 2pi - 2phi in [2pi/3, pi - pi/N].
   - The isosceles triangle at psi = 2pi - 3phi has legs c, c and base 2 sin(2pi - 2phi) = 2 sin(alpha), so it is congruent to the Lemma 5.8 triangle (apex at 1, B, C = e^{+-i alpha}). Energy depends only on side lengths. I checked the base length computation.
   Note that the intermediate triangles produced by Theorem 1 are not vertex triples of P_N. This is fine, since Theorem 1 is purely about three points on the circle.

7. (minor) Obtuse case. State that no right triangles occur (no diameters for N odd), and that the equality c <= c_max = 2 sin(theta_N) together with U(T*) >= c_max^r/2 holds because T* contains a pair at distance c_max (its two legs). Also (a/c)^r + (b/c)^r <= (a/c)^2 + (b/c)^2 < 1 for r >= 2 (a, b < c). The packet says this; it is correct.

8. (minor/presentational) In the Lemma proof, the concavity statement for D(u) = k(u) - k(1-u) should include its second derivative D'' = (2u-1)/(u(1-u)) <= 0 on (0,1/2], and continuity at 0 (k(0+) = 0). Also say F(r_1) is computed with w = B^{r_1} in (1/2, 1) because B > A.

9. (minor) Notation: the symbol phi is used both for the angle and for the function phi(s) in the Lemma. Rename the function (e.g. g(s)). Also the Lemma letters A, B collide with the points A, B. Rename them (e.g. p, q).

## (3) Steps verified, and how

- Clark-Laugesen formula (GIVEN 1) vs direct constrained maximisation of the quadratic form (SLSQP, 200 random triples, r in [2,6]): max discrepancy about 7e-6 (optimiser tolerance; the formula is not in doubt).
- Derivative formulas d log U/dx, d log U/dy: derived by hand (D = 4xy - s^2, dD/dx = 4y - 2s) and agree.
- d log U/d psi formula: tested against mpmath numerical differentiation at 40 digits, 50 random points: relative error about 1e-38.
- Identity cot(alpha)/cot(beta) = (sin phi + sin psi)/(sin phi - sin psi), and the t_2 = sin psi/sin phi computation: verified by hand.
- Identity A^2 + B^2 - 1 = -2 sin(alpha) sin(beta) cos(phi)/sin^2(phi): verified numerically to 1e-30 and by the classical identity.
- Lemma: 200,000 random (A, B, r) with the hypotheses, zero violations; proof read line by line (unimodality of F, endpoint reduction, phi(s) monotonicity, k(1-w) >= k(w), concavity of D). All correct.
- Sign of the bracket: the positivity of cot(beta) (beta <= pi - phi < pi/2) and of z + x - y > 0 (z >= y) was checked.
- Theorem 1 on a grid (7 values of r from 2 to 30, 25 values of phi, 400 values of psi): U nondecreasing everywhere, zero failures. Lemma 5.8 (GIVEN 3) was likewise checked monotone on a grid.
- Theorem 2 brute force: for N in {5,7,9,11,13,15,21} and r in {2.01, 2.5, 3, 4, 7}, the maximum of the Lemma 5.7 energy over all vertex triples equals the conjectured closed form to 1e-12. For N <= 13 a direct quadratic-programme maximum over all of P_N agrees (to optimiser tolerance, about 1e-5 at r = 7). Masses on T* are positive.
- Closed form of U(T*): derived by hand from 2z^2/(4z-x) with a = 4 sin(theta) cos(theta), matching the conjectured formula.
- Parametrisation coverage (relabelling, reflection, phi and psi ranges, alpha = 2k pi/N, tie and equilateral cases, absence of right triangles for odd N): checked by hand as in item 6.

Dependence on external results: Bjorck's theorem (r > 2), Clark-Laugesen Thm 8 and the paper's Lemma 5.8 are used as GIVEN and were not re-proved. Lemma 5.8 is only used at r > 2 and in the non-strict form.
